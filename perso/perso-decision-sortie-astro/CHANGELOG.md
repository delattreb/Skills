# Changelog : perso-decision-sortie-astro

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).

## [0.4.0] — 2026-11-27
### Ajouté
- `references/objets.json` : 37 objets (amas, nébuleuses, galaxies, étoiles doubles) avec coordonnées J2000 arrondies. Fin des objets saisis de mémoire par le modèle.
- `scripts/objets.py` : visibilité dans une fenêtre horaire (hauteur d'au moins 30°, écart à la Lune d'au moins 30° ou Lune couchée), planètes comprises, tri par heure de culmination. Contrôle intégré : `python3 -I scripts/objets.py --test`.
### Modifié
- Seuil de rafales : rafales de 35 km/h et plus limitent le verdict à « peut-être », 50 km/h et plus donnent « non ». Valeurs de départ à recalibrer.
- Étape 3 : les objets viennent du script, rien n'est ajouté hors de sa sortie.

## [0.3.0] — 2026-11-27
### Ajouté
- `scripts/lune.py` (dépendance `ephem`, `requirements.txt`) : nuit noire, phase, illumination, créneaux Lune levée et hauteur de la Lune pour N nuits, calculés hors ligne. Corrige l'échec des pages Lune inaccessibles constaté au test.
### Modifié
- La Lune vient du script, la recherche web sert au recoupement et de repli.
- Destination corrigée en `Astronomie/météo/` (le dossier réel est `Astronomie`). Le dossier `météo` est créé s'il manque.

## [0.2.0] — 2026-11-27
### Modifié
- Remplace `perso-meteo-astro-hebdo` (supprimé). Le skill reprend sa couverture : seeing, transparence, recoupement des sources, événements de la semaine.
- Chaque nuit reçoit un verdict. Sans prévision horaire, le verdict est « indicatif » (un « oui » est plafonné à « peut-être »), plus de « non rendu ».
- Sources météo en cascade : AccuWeather horaire, puis Meteoblue, Clear Outside, Windy ou Météo-France, puis AccuWeather journalier.
- Lune obligatoire (phase, illumination, lever, coucher), recoupée sur deux sources. Sans Lune, seulement planètes et étoiles doubles.
- Exactement 7 nuits, du jour du lancement. Fichier `semaine-AAAA-MM-JJ.md` daté de la première nuit.
- Front matter YAML défini (type, date, nuits, lieu, sources réelles, tags).
- Écriture MonVault : chargement des outils Google Drive par ToolSearch avant de conclure à une impossibilité.
- Temps de mise en température aligné sur l'ancien skill (environ 45 min). Colonne « Fiabilité » et section « À surveiller » ajoutées.

## [0.1.0]
### Ajouté
- Première version : verdict oui, peut-être ou non par nuit, objets classés par heure de passage, fiche Obsidian.
