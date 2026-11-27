---
name: "perso-decision-sortie-astro"
description: "Décide si sortir le Celestron C8 sur monture Skysensor 2000 GoTo les 7 prochaines nuits à La Rue-Saint-Pierre (76690) : verdict oui, peut-être ou non par nuit selon la météo, la Lune et le matériel, avec objets classés par heure de passage. Fiche Obsidian dans MonVault. À utiliser quand l'utilisateur demande « je sors le télescope ? », « quelles nuits observer », « décision de sortie astro », « /perso-decision-sortie-astro »."
metadata:
  version: "0.1.0"
---

# Décision de sortie astronomie (C8 + Skysensor 2000 GoTo)

Produire, pour chacune des 7 prochaines nuits, un verdict de sortie fiable et la liste des objets à observer, classés par heure croissante dans la nuit. Le résultat est une fiche Obsidian hebdomadaire, en français.

## Contexte fixe

- **Lieu** : 224 Route du Clos Saint-Pierre, 76690 La Rue-Saint-Pierre (Seine-Maritime). Coordonnées approximatives : 49,56° N, 1,22° E, altitude environ 150 m. Fuseau Europe/Paris.
- **Matériel** : télescope Celestron C8 (ouverture 203 mm, focale 2032 mm), oculaires 10 à 50 mm, monture équatoriale Skysensor 2000 motorisée avec GoTo.
- **Destination** : MonVault (Google Drive), dossier `astronomie/météo/`.

## Entrées

- **Météo** : prévisions horaires sur 7 jours via le connecteur AccuWeather. Relever nuages bas, moyens et hauts, humidité, point de rosée, vent, température et transparence si disponible.
- **Lune** : phase, illumination, hauteur et heure de coucher pour chaque nuit.

## Étapes

1. Calculer la fenêtre de nuit noire de chaque nuit (crépuscule astronomique terminé, Soleil sous -18°) et la présence de la Lune dans cette fenêtre.
2. Pour chaque heure de la fenêtre, noter nuages, humidité, écart point de rosée et température, vent, seeing estimé.
3. Repérer les plages utiles : nuages totaux faibles, humidité sous le seuil de buée, vent modéré, Lune basse ou couchée.
4. Attribuer le verdict :
   - **oui** : au moins 2 heures consécutives utiles, sans nuage dominant, humidité sous 85 % et vent inférieur à 25 km/h.
   - **peut-être** : plage utile plus courte, dégradation probable en cours de nuit, ou Lune gênante.
   - **non** : nuages dominants, pluie, humidité élevée ou vent fort sur toute la fenêtre.
   Ces seuils sont des valeurs de départ à recalibrer avec le retour d'expérience.
5. Pour une nuit en oui ou peut-être, sélectionner 4 à 8 objets visibles pendant la plage utile : hauteur d'au moins 30° au-dessus de l'horizon, écart d'au moins 30° avec la Lune, variété (planète, amas, nébuleuse, galaxie, étoile double). Classer par heure de passage au méridien croissante.
6. Ajouter les points matériel : temps d'équilibrage thermique du C8 à prévoir avant la première observation, rappel de l'alignement GoTo (deux étoiles de référence avant la première cible), risque de buée sur le tube et le correcteur, pare-buée ou chauffage si humidité élevée.

## Sortie

Fiche Obsidian, un fichier par semaine : `semaine-AAAA-MM-JJ.md` (date du lundi). Structure :

- Tableau des 7 nuits : date, verdict, fenêtre utile, Lune, nuages, humidité, vent.
- Une section par nuit en oui ou peut-être : objets classés par heure, avec heure de passage et hauteur.
- Points matériel à anticiper.

Si l'écriture dans MonVault n'est pas possible, produire la fiche en fichier Markdown et le signaler clairement.

## Règles

- Ne jamais annoncer un verdict sans données horaires de la nuit concernée.
- Les objets proposés doivent être réellement visibles pendant la plage utile, pas seulement pendant la nuit.
- Ce skill est distinct de `perso-meteo-astro-hebdo`, qu'il ne remplace pas. Le carnet du ciel (huit cibles fixes) reste un autre livrable.
