---
name: "perso-decision-sortie-astro"
description: "Décide si sortir le Celestron C8 sur monture Skysensor 2000 GoTo les 7 prochaines nuits à La Rue-Saint-Pierre (76690) : verdict oui, peut-être ou non pour chaque nuit selon la météo, la Lune, le seeing et le matériel, avec objets classés par heure de passage. Fiche Obsidian dans MonVault. Remplace perso-meteo-astro-hebdo. À utiliser quand l'utilisateur demande « je sors le télescope ? », « quelles nuits observer », « météo astro de la semaine », « prévisions astro », « décision de sortie astro », « /perso-decision-sortie-astro »."
metadata:
  version: "0.4.0"
---

# Décision de sortie astronomie (C8 + Skysensor 2000 GoTo)

Produire, pour chacune des 7 prochaines nuits, un verdict de sortie et la liste des objets à observer, classés par heure croissante. Résultat : une fiche Obsidian en français. Ce skill remplace `perso-meteo-astro-hebdo`.

## Contexte fixe

- **Lieu** : 224 Route du Clos Saint-Pierre, 76690 La Rue-Saint-Pierre (Seine-Maritime). Coordonnées approximatives : 49,56° N, 1,22° E, altitude environ 150 m. Fuseau Europe/Paris.
- **Matériel** : Celestron C8 (ouverture 203 mm, focale 2032 mm, tube fermé à lame, sensible à la buée), oculaires 10 à 50 mm (environ 40× à 200×), monture équatoriale Skysensor 2000 motorisée avec GoTo.
- **Destination** : MonVault (Google Drive), dossier `Astronomie/météo/` (le dossier `Astronomie` existe déjà, avec une majuscule).

## Règles impératives

- **Sept nuits exactement**, de la nuit qui commence le jour du lancement jusqu'à 6 nuits plus tard. Ne mentionner aucune autre nuit, ni dans le tableau ni dans le texte.
- **Ne rien inventer.** Chaque valeur vient d'une source consultée. Une donnée absente s'écrit « non disponible », jamais estimée.
- **Chaque nuit reçoit un verdict**, jamais « non rendu ». Quand les données horaires manquent, le verdict est marqué **indicatif** (voir étape 2) et la colonne « Fiabilité » le dit.
- **La Lune est obligatoire**, calculée par `scripts/lune.py` et recoupée avec une source web quand c'est possible. Elle sert à choisir le type d'objet, donc elle ne se saute jamais sans le signaler en tête de fiche.
- **Une seule source ne suffit pas pour les nuages** : recouper deux sources dès que la première ne couvre pas la nuit en horaire.

## Étape 1 : collecter

Lancer les recherches indépendantes en parallèle.

**Météo, par ordre de priorité**

1. Connecteur AccuWeather (charger ses outils par ToolSearch s'ils ne sont pas disponibles). Relever heure par heure : nuages bas, moyens et hauts, humidité, point de rosée, température, vent et rafales. Noter jusqu'où vont les prévisions horaires (souvent 12 h seulement) et la station utilisée.
2. Pour les nuits que l'horaire AccuWeather ne couvre pas, recherche web sur des prévisions horaires à plusieurs jours : Meteoblue (aussi pour le seeing), Clear Outside, Windy, Météo-France. Si une page ne s'ouvre pas, passer à la suivante sans s'arrêter.
3. En dernier recours, prévisions journalières d'AccuWeather (couverture nuageuse de la nuit). Elles servent seulement au verdict indicatif.

**Lune et nuit noire**, par le script local (calcul d'éphéméride, ne dépend d'aucun site) :

```
pip install -r requirements.txt   # une seule fois (ephem)
python3 -I scripts/lune.py AAAA-MM-JJ 7
```

Une ligne JSON par nuit : début et fin de la nuit noire (Soleil sous -18°), illumination en pourcentage au début de la nuit noire, nom de la phase, croissante ou décroissante, créneaux où la Lune est levée pendant la nuit noire, hauteur de la Lune au début de la nuit noire. Lancer depuis le dossier du skill. Si `ephem` ne s'installe pas, recourir à la recherche web (timeanddate.com, IMCCE ou équivalent) pour les mêmes valeurs, et le signaler dans les notes de méthode.

Recouper l'illumination avec une source web quand c'est possible : un écart de quelques points est normal (heure de référence différente), un écart de 10 points ou plus est à signaler.

**Seeing et transparence** : Meteoblue ou Clear Outside. Sinon « non disponible ».

**Alertes** : vigilance Météo-France en cours (grand froid, brouillard, pluie, vent).

## Étape 2 : verdict

Pour chaque nuit, fenêtre de nuit noire = fin du crépuscule astronomique jusqu'au début de l'aube, avec la Lune sous l'horizon ou basse si possible.

Seuils de départ, à recalibrer avec le retour d'expérience :

- **oui** : au moins 2 heures consécutives utiles, sans nuage dominant, humidité sous 85 %, vent moyen inférieur à 25 km/h et rafales inférieures à 35 km/h.
- **peut-être** : plage utile plus courte, dégradation probable en cours de nuit, Lune gênante, ou rafales de 35 à 49 km/h (le tube vibre, la mise au point et les forts grossissements en pâtissent).
- **non** : nuages dominants, pluie, humidité élevée, vent moyen fort ou rafales de 50 km/h et plus sur toute la fenêtre.

**Verdict indicatif** (nuit sans prévision horaire exploitable) : appliquer les mêmes seuils aux valeurs journalières de la nuit. Écrire le verdict suivi de « (indicatif) ». Un verdict « oui » indicatif est plafonné à « peut-être » tant qu'aucune prévision horaire ne le confirme. Mentionner la date à laquelle refaire un point horaire.

**Buée** : écart température et point de rosée sous 3 °C, ou humidité d'au moins 85 %, signale un risque de buée sur le tube et le correcteur. Ce signal va dans les points matériel, il ne change pas le verdict.

**Lune et type d'observation** : ciel profond exige peu ou pas de Lune et une bonne transparence. Planétaire, lunaire et étoiles doubles supportent la Lune, mais demandent un bon seeing (oculaire de 10 mm seulement si le seeing est bon). Indiquer pour chaque nuit en oui ou peut-être le type favorisé.

Si la Lune est absente des données, ne proposer que des planètes et des étoiles doubles, et le dire.

## Étape 3 : objets

Pour une nuit en oui ou peut-être (indicatif compris), lancer le script avec la plage utile retenue (heure de Paris) :

```
python3 -I scripts/objets.py AAAA-MM-JJ HH:MM HH:MM
```

Il lit `references/objets.json` (37 objets : amas, nébuleuses, galaxies, étoiles doubles) et calcule les planètes. Il ne garde que les objets qui atteignent 30° de hauteur dans la fenêtre à un moment où la Lune est couchée ou à 30° ou plus d'eux, déjà triés par heure de culmination dans la fenêtre. Choisir 4 à 8 de ces objets en variant les types (planète, amas, nébuleuse, galaxie, étoile double), et reporter leur heure de culmination, leur hauteur maximale et leur écart à la Lune. N'ajouter aucun objet absent de la sortie du script.

Les coordonnées du catalogue sont arrondies : elles servent à décider de sortir, pas à pointer (le GoTo a sa propre base). Pour ajouter un objet, l'ajouter à `references/objets.json` avec ses coordonnées J2000.

Ajouter, si une nuit est favorable, les événements de la semaine adaptés au C8 (conjonctions, pluie d'étoiles filantes, comète visible) quand une source les confirme.

Si aucune nuit n'est en oui ou peut-être, donner « À surveiller » : la nuit la moins défavorable et ce qui doit changer pour qu'elle passe en peut-être.

## Étape 4 : points matériel

- Sortir le C8 environ 45 min avant la première observation pour la mise en température.
- Alignement GoTo : deux étoiles de référence avant la première cible.
- Buée : pare-buée ou chauffage du correcteur si le signal de l'étape 2 est actif.
- Froid : protéger la monture et les batteries si une vigilance grand froid est en cours ou si la température descend sous 0 °C.

## Sortie

Fiche Markdown Obsidian, un fichier par lancement : `semaine-AAAA-MM-JJ.md`, où la date est celle de la **première nuit** (le jour du lancement), pas celle d'un lundi.

Front matter YAML :

```yaml
---
type: decision-astro
date: AAAA-MM-JJ
nuits: 7
lieu: La Rue-Saint-Pierre
sources: [liste des sources réellement consultées]
tags: [astronomie, meteo]
---
```

Corps, dans cet ordre :

1. Titre et lieu, matériel, sources météo utilisées (station, portée de l'horaire).
2. Résumé de 2 ou 3 phrases : meilleures nuits, ou « aucune sortie conseillée ».
3. Tableau des 7 nuits : date, verdict, fiabilité (horaire ou indicatif), fenêtre utile, Lune (phase, illumination, coucher), nuages, seeing et transparence, humidité et point de rosée, vent.
4. Une section par nuit en oui ou peut-être : type d'observation favorisé, oculaire conseillé, objets classés par heure.
5. Lune (récapitulatif de la semaine) et « À surveiller » si nécessaire.
6. Points matériel à anticiper.
7. Fiabilité : les prévisions au-delà de 3 ou 4 jours sont incertaines.
8. Notes de méthode : seuils utilisés, données manquantes.

## Écriture dans MonVault

1. Charger les outils Google Drive par ToolSearch (`Google Drive`) s'ils ne sont pas déjà disponibles.
2. Chercher MonVault, puis son sous-dossier `Astronomie`, puis `météo` dedans (recherche par `parentId`, pas par titre seul). Si `météo` manque, le créer sous `Astronomie` ; si `Astronomie` ou MonVault manque, ne rien créer et passer à l'étape 3. Créer le fichier dans `météo`. Si un fichier du même nom existe déjà, le mettre à jour au lieu d'en créer un second.
3. Si le connecteur Drive est absent ou refuse l'écriture, enregistrer la fiche en fichier Markdown local, donner son chemin complet et signaler clairement que MonVault n'a pas été mis à jour. Ne pas conclure à une impossibilité avant d'avoir cherché les outils Drive.

Terminer par un court message dans la conversation : meilleures nuits, ou absence de nuit favorable, et emplacement de la fiche.
