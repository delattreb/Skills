#!/usr/bin/env python3
"""Objets observables dans une fenêtre horaire, avec hauteur, culmination et écart à la Lune.

Usage : python3 scripts/objets.py AAAA-MM-JJ HH:MM HH:MM
  AAAA-MM-JJ : date du soir de la nuit. Fenêtre en heure de Paris ; une fin avant 12:00 est le lendemain.
Un objet est retenu si sa hauteur atteint 30° dans la fenêtre à un moment où la Lune est
sous l'horizon ou à 30° ou plus de lui. Sortie : une ligne JSON par objet, triée par heure de
culmination dans la fenêtre. `python3 scripts/objets.py --test` lance un contrôle.
"""
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import ephem

TZ, UTC = ZoneInfo("Europe/Paris"), ZoneInfo("UTC")
RAD = 57.29578
PLANETES = [ephem.Mercury, ephem.Venus, ephem.Mars, ephem.Jupiter, ephem.Saturn, ephem.Uranus, ephem.Neptune]
NOMS_FR = {"Mercury": "Mercure", "Venus": "Vénus", "Mars": "Mars", "Jupiter": "Jupiter",
           "Saturn": "Saturne", "Uranus": "Uranus", "Neptune": "Neptune"}


def hm(d):
    return ephem.Date(d).datetime().replace(tzinfo=UTC).astimezone(TZ).strftime("%H:%M")


def corps():
    out = []
    for o in json.loads((Path(__file__).parent.parent / "references/objets.json").read_text(encoding="utf-8"))["objets"]:
        b = ephem.FixedBody()
        b._ra, b._dec, b._epoch = ephem.hours(o["ra"]), ephem.degrees(o["dec"]), "2000"
        out.append((o["id"], o["nom"], o["type"], b))
    out += [(NOMS_FR[p.__name__], NOMS_FR[p.__name__], "planète", p()) for p in PLANETES]
    return out


def visibles(jour, debut, fin):
    y, m, d = map(int, jour.split("-"))
    h0, m0 = map(int, debut.split(":"))
    h1, m1 = map(int, fin.split(":"))
    t0 = datetime(y, m, d, h0, m0, tzinfo=TZ)
    t1 = datetime(y, m, d, h1, m1, tzinfo=TZ) + timedelta(days=1 if h1 < 12 else 0)
    e0, e1 = ephem.Date(t0.astimezone(UTC).replace(tzinfo=None)), ephem.Date(t1.astimezone(UTC).replace(tzinfo=None))
    obs = ephem.Observer()
    obs.lat, obs.lon, obs.elevation, obs.pressure = "49.56", "1.22", 150, 0
    lune, res = ephem.Moon(), []
    for oid, nom, typ, b in corps():
        pts, t = [], e0
        while t <= e1:
            obs.date = t
            b.compute(obs)
            lune.compute(obs)
            sep = float(ephem.separation(b, lune)) * RAD
            if float(b.alt) * RAD >= 30 and (float(lune.alt) < 0 or sep >= 30):
                pts.append((t, float(b.alt) * RAD, sep))
            t = ephem.Date(t + 10 / 1440)
        if pts:
            haut = max(pts, key=lambda p: p[1])
            res.append((haut[0], {"id": oid, "nom": nom, "type": typ, "culmination_dans_la_fenetre": hm(haut[0]),
                                  "hauteur_max_deg": round(haut[1]), "visible_de": hm(pts[0][0]), "visible_jusqu_a": hm(pts[-1][0]),
                                  "ecart_lune_min_deg": round(min(p[2] for p in pts))}))
    return [r for _, r in sorted(res, key=lambda x: x[0])]


def test():
    # M31 culmine vers 21:04 (heure de Paris) le 29 nov. 2026 : recoupe le calcul à la main
    # (temps sidéral local à 20:00 UT proche de l'ascension droite 0 h 43).
    r = {o["id"]: o for o in visibles("2026-11-29", "19:00", "22:50")}
    h, mi = map(int, r["M31"]["culmination_dans_la_fenetre"].split(":"))
    assert abs((h * 60 + mi) - (21 * 60 + 4)) <= 10, r["M31"]
    assert "M42" not in r  # Orion pas assez haut avant 22:50 ce soir-là
    print("ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        test()
    else:
        for o in visibles(*sys.argv[1:4]):
            print(json.dumps(o, ensure_ascii=False))
