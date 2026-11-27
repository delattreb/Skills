#!/usr/bin/env python3
"""Lune et nuit noire pour les N prochaines nuits au lieu d'observation.

Usage : python3 scripts/lune.py [AAAA-MM-JJ] [nombre_de_nuits]
Date par défaut : aujourd'hui (Europe/Paris), 7 nuits. Sortie : une ligne JSON par nuit.
"""
import json
import sys
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import ephem

TZ = ZoneInfo("Europe/Paris")
LAT, LON, ALT = "49.56", "1.22", 150  # La Rue-Saint-Pierre, approximatif


def local(d):
    return ephem.Date(d).datetime().replace(tzinfo=ZoneInfo("UTC")).astimezone(TZ)


def phase_name(k, waxing):
    if k < 3:
        return "Nouvelle Lune"
    if k > 97:
        return "Pleine Lune"
    if 47 <= k <= 53:
        return "Premier quartier" if waxing else "Dernier quartier"
    if k < 47:
        return "Premier croissant" if waxing else "Dernier croissant"
    return "Gibbeuse croissante" if waxing else "Gibbeuse décroissante"


def nuit(jour):
    obs = ephem.Observer()
    obs.lat, obs.lon, obs.elevation, obs.pressure = LAT, LON, ALT, 0
    soleil, lune = ephem.Sun(), ephem.Moon()
    midi = datetime(jour.year, jour.month, jour.day, 12, tzinfo=TZ).astimezone(ZoneInfo("UTC"))
    obs.date = ephem.Date(midi)
    obs.horizon = "-18"
    debut = obs.next_setting(soleil, use_center=True)
    obs.date = debut
    fin = obs.next_rising(soleil, use_center=True)
    obs.horizon = "0"
    # Lune au-dessus de l'horizon : échantillon toutes les 10 min dans la nuit noire
    segments, t, haut = [], debut, None
    while t <= fin:
        obs.date = t
        lune.compute(obs)
        if (lune.alt > 0) and haut is None:
            haut = t
        if (lune.alt <= 0) and haut is not None:
            segments.append((local(haut).strftime("%H:%M"), local(t).strftime("%H:%M")))
            haut = None
        t = ephem.Date(t + 10 / 1440)
    if haut is not None:
        segments.append((local(haut).strftime("%H:%M"), local(fin).strftime("%H:%M")))
    obs.date = debut
    lune.compute(obs)
    k = lune.phase
    obs.date = ephem.Date(debut + 1 / 24)
    lune.compute(obs)
    croissante = lune.phase > k
    obs.date = debut
    lune.compute(obs)
    return {
        "nuit": f"{jour} -> {jour + timedelta(days=1)}",
        "nuit_noire": [local(debut).strftime("%H:%M"), local(fin).strftime("%H:%M")],
        "illumination_pct": round(k),
        "phase": phase_name(k, croissante),
        "croissante": croissante,
        "lune_levee_pendant_nuit_noire": segments,
        "hauteur_lune_debut_nuit_deg": round(float(lune.alt) * 57.29578),
    }


if __name__ == "__main__":
    depart = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.now(TZ).date()
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    for i in range(n):
        print(json.dumps(nuit(depart + timedelta(days=i)), ensure_ascii=False))
