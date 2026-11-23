#!/usr/bin/env python3
"""Lit les flux primaires accessibles sans navigateur et liste les entrées publiées dans la fenêtre de la veille.

Sources :
- Feuille de route Microsoft 365 (RSS officiel) ;
- Catalogue CISA des vulnérabilités exploitées (KEV, copie officielle sur GitHub).

Usage : python3 -I flux_veille.py --debut 2026-11-20T07:00:00+01:00 [--fin 2026-11-21T07:00:00+01:00]
Sans --fin, la fin est l'instant présent. Sortie en Markdown simple, une ligne par entrée.
"""
import argparse
import datetime as dt
import email.utils
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET

M365_RSS = "https://www.microsoft.com/releasecommunications/api/v2/m365/rss"
KEV_JSON = "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json"
KEV_PAGE = "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"


def lire(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (veille-informatique)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def m365(debut, fin):
    racine = ET.fromstring(lire(M365_RSS))
    lignes = []
    for item in racine.iter("item"):
        brut = item.findtext("pubDate")
        if not brut:
            continue
        date = email.utils.parsedate_to_datetime(brut)
        if debut <= date <= fin:
            cats = ", ".join(c.text for c in item.findall("category") if c.text)
            lignes.append((date, f"- {date:%d/%m/%Y %H:%M} UTC | {item.findtext('title', '').strip()} | {cats} | {item.findtext('link', '').strip()}"))
    return [l for _, l in sorted(lignes, reverse=True)]


def kev(debut, fin):
    data = json.loads(lire(KEV_JSON))
    lignes = []
    for v in data.get("vulnerabilities", []):
        ajout = dt.date.fromisoformat(v["dateAdded"])
        if debut.date() <= ajout <= fin.date():
            lignes.append(
                f"- {ajout:%d/%m/%Y} | {v['cveID']} | {v['vendorProject']} {v['product']} | "
                f"{v['vulnerabilityName']} | échéance fédérale {v['dueDate']} | rançongiciel : {v.get('knownRansomwareCampaignUse', '?')}"
            )
    return lignes


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--debut", required=True, help="début de fenêtre ISO 8601 avec fuseau")
    p.add_argument("--fin", help="fin de fenêtre ISO 8601 avec fuseau (défaut : maintenant)")
    a = p.parse_args()
    debut = dt.datetime.fromisoformat(a.debut)
    fin = dt.datetime.fromisoformat(a.fin) if a.fin else dt.datetime.now(dt.timezone.utc)
    if debut.tzinfo is None or fin.tzinfo is None:
        sys.exit("Les dates doivent comporter un fuseau, par exemple +01:00.")

    for titre, fonction, source in (
        ("Feuille de route Microsoft 365", m365, M365_RSS),
        ("CISA KEV : vulnérabilités ajoutées", kev, KEV_PAGE),
    ):
        print(f"## {titre} ({source})")
        try:
            lignes = fonction(debut, fin)
            print("\n".join(lignes) if lignes else "- aucune entrée dans la fenêtre")
        except Exception as e:  # source indisponible : le signaler sans bloquer l'autre
            print(f"- ERREUR : source inaccessible ({e.__class__.__name__}: {e})")
        print()


if __name__ == "__main__":
    main()
