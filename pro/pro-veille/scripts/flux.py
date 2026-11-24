#!/usr/bin/env python3
"""Lit les flux RSS/Atom de config/flux.json et liste les entrées publiées dans la fenêtre.

Lecture : python3 -I flux.py --debut 2026-11-24T07:00:00+01:00 [--fin ...] [--categorie ia] [--par-flux 3] [--resume]
Test    : python3 -I flux.py --tester [--ecrire]   (--ecrire désactive les flux en échec dans flux.json)
Sortie en Markdown simple, une ligne par entrée, groupée par catégorie.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import email.utils
import gzip
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

CONFIG = pathlib.Path(__file__).resolve().parent.parent / "config" / "flux.json"
UTC = dt.timezone.utc


def lire(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (veille)", "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"})
    with urllib.request.urlopen(req, timeout=30) as r:
        b = r.read()
    return gzip.decompress(b) if b[:2] == bytes([0x1f, 0x8b]) else b


def date(txt):
    if not txt:
        return None
    try:
        d = email.utils.parsedate_to_datetime(txt)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(txt.strip())
        except ValueError:
            return None
    return d if d.tzinfo else d.replace(tzinfo=UTC)


def propre(url):
    """Retire fragment et paramètres de suivi (utm_*, at_*, traffic_source, xtor) : moins de volume."""
    u = urllib.parse.urlsplit(url)
    q = [(k, v) for k, v in urllib.parse.parse_qsl(u.query) if not k.startswith(("utm_", "at_", "xtor")) and k != "traffic_source"]
    return urllib.parse.urlunsplit((u.scheme, u.netloc, u.path, urllib.parse.urlencode(q), ""))


def texte(el, *noms):
    for e in el.iter():
        if e.tag.rsplit("}", 1)[-1] in noms and (e.text or "").strip():
            return e.text.strip()
    return ""


def entrees(url):
    """Retourne [(date, titre, lien, résumé)] d'un flux RSS ou Atom."""
    racine = ET.fromstring(lire(url))
    sortie = []
    for it in racine.iter():
        nom = it.tag.rsplit("}", 1)[-1]
        if nom not in ("item", "entry"):
            continue
        lien = texte(it, "link")
        if not lien:  # Atom : <link href="...">
            for l in it:
                if l.tag.rsplit("}", 1)[-1] == "link" and l.get("href"):
                    lien = l.get("href")
                    break
        resume = re.sub(r"<[^>]+>|\s+", " ", texte(it, "description", "summary")).strip()[:200]
        sortie.append((date(texte(it, "pubDate", "published", "updated", "date")), texte(it, "title"), lien, resume))
    return sortie


def tester(f):
    try:
        e = entrees(f["url"])
        dates = [x[0] for x in e if x[0]]
        if not e:
            return f, "aucune entrée"
        if not dates:
            return f, "aucune date lisible"
        return f, None
    except Exception as ex:
        return f, f"{ex.__class__.__name__}: {ex}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--debut", help="début de fenêtre ISO 8601 avec fuseau")
    p.add_argument("--fin", help="fin de fenêtre (défaut : maintenant)")
    p.add_argument("--categorie", help="une seule catégorie")
    p.add_argument("--tester", action="store_true", help="vérifie chaque flux actif")
    p.add_argument("--ecrire", action="store_true", help="avec --tester : désactive les flux en échec")
    p.add_argument("--par-flux", type=int, default=3, help="entrées les plus récentes gardées par flux (défaut 3)")
    p.add_argument("--resume", action="store_true", help="ajoute le résumé de chaque entrée")
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    flux = [f for f in cfg["flux"] if f["actif"] and (not a.categorie or f["categorie"] == a.categorie)]

    with cf.ThreadPoolExecutor(12) as ex:
        if a.tester:
            ko = 0
            for f, err in ex.map(tester, flux):
                print(f"{'OK ' if not err else 'KO '} {f['categorie']:<13} {f['nom']}" + (f" | {err}" if err else ""))
                if err:
                    ko += 1
                    if a.ecrire:
                        f["actif"], f["note"] = False, f"inaccessible au test du {dt.date.today():%d/%m/%Y} : {err[:120]}"
            if a.ecrire:
                CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"\n{len(flux) - ko} OK, {ko} KO")
            return

        if not a.debut:
            sys.exit("--debut est requis.")
        debut = dt.datetime.fromisoformat(a.debut)
        fin = dt.datetime.fromisoformat(a.fin) if a.fin else dt.datetime.now(UTC)
        if debut.tzinfo is None or fin.tzinfo is None:
            sys.exit("Les dates doivent comporter un fuseau, par exemple +01:00.")

        def un(f):
            try:
                return f, [e for e in entrees(f["url"]) if e[0] and debut <= e[0] <= fin], None
            except Exception as err:
                return f, [], f"{err.__class__.__name__}: {err}"

        par_cat = {}
        for f, e, err in ex.map(un, flux):
            if err:
                print(f"ERREUR | {f['nom']} | {err}", file=sys.stderr)
            for d, titre, lien, resume in sorted(e, key=lambda x: x[0], reverse=True)[: a.par_flux]:
                par_cat.setdefault(f["categorie"], []).append((d, f["nom"], titre, lien, resume))

    for cat, lignes in par_cat.items():
        print(f"## {cat} ({len(lignes)})")
        for d, nom, titre, lien, resume in sorted(lignes, reverse=True):
            print(f"- {d.astimezone():%d/%m %H:%M} | {nom} | {titre[:150]} | {propre(lien)}" + (f" | {resume}" if resume and a.resume else ""))
        print()


if __name__ == "__main__":
    main()
