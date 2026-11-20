---
name: "loisir-meteo-astro-hebdo"
description: "Rédige en français une fiche d'aide à la décision « astronomie » pour les 7 prochaines nuits au lieu d'observation de l'utilisateur (Clères / La Rue-Saint-Pierre, 76690) avec son Celestron C8 : nuages, Lune (avec graphisme des phases et frises horaires), crépuscules, seeing, transparence, buée, note et verdict par nuit, cibles conseillées. Publie une page artifact en thème rouge et noir. À utiliser quand l'utilisateur demande « fiche météo astro », « météo astro de la semaine », « /loisir-meteo-astro-hebdo », « est-ce que je sors le télescope cette semaine », « quelles nuits pour observer » ou « prévisions astro »."
metadata:
  version: "0.1.0"
---

# Fiche météo astro hebdomadaire

Produire en français une fiche d'aide à la décision « astronomie » pour les **7 prochaines nuits**, à partir du jour de lancement.

## Contexte fixe

**Lieu d'observation** : 224 Route du Clos Saint-Pierre, 76690 (Seine-Maritime, Normandie, secteur Clères / La Rue-Saint-Pierre, au nord de Rouen). Coordonnées approximatives : 49,56° N, 1,22° E, altitude environ 150 m. Fuseau Europe/Paris.

**Matériel** : Celestron C8 (Schmidt-Cassegrain 203 mm, F/D 10, focale 2032 mm), oculaires de 10 à 50 mm (grossissements d'environ 40× à 200×). Tube fermé à lame : sensible à la buée et à la mise en température.

## Règles impératives

- **Ne rien inventer.** Chaque valeur (nuages, heures, illumination, seeing) doit venir d'une source consultée. Si une donnée manque, l'écrire (« non disponible ») plutôt que l'estimer.
- **Recouper au moins deux sources** pour la couverture nuageuse et la Lune.
- **Fiabilité** : rappeler que les prévisions au-delà de 3 ou 4 jours sont incertaines.

## Étape 1 — Collecter

Utiliser la recherche web et les outils météo disponibles (outil AccuWeather s'il est présent ; sites comme Meteoblue « seeing astronomique », Clear Outside, Météo-France, Windy). Lancer en parallèle les recherches indépendantes.

1. Couverture nuageuse heure par heure pendant la nuit (nuages bas, moyens et hauts séparément si possible).
2. Lune : phase et pourcentage d'illumination, croissante ou décroissante, heures de lever et de coucher pour chaque nuit, et donc les plages de nuit sans Lune.
3. Heures de coucher / lever du Soleil, crépuscules et nuit astronomique (Soleil à −18°).
4. Seeing (turbulence) et transparence de l'atmosphère, jet-stream si disponible.
5. Humidité relative, point de rosée et écart avec la température (risque de buée), vent (au sol, rafales), température minimale.
6. Risque de brouillard ou de pluie.
7. Bonus : objets remarquables visibles cette semaine adaptés à un C8 (planètes et heure de passage au méridien, ciel profond de saison, événements : conjonctions, pluies d'étoiles filantes, comètes visibles).

## Étape 2 — Analyser et noter

Pour chaque nuit, attribuer une note de 1 à 5 étoiles et un verdict parmi :
- « Sortir le matériel »
- « Peut-être (créneau court ou incertain) »
- « Ne pas sortir »

Indiquer la meilleure fenêtre horaire. Raisonner selon le type d'observation :
- **Ciel profond** (galaxies, nébuleuses) : exige ciel dégagé, bonne transparence ET peu ou pas de Lune.
- **Planétaire / lunaire / étoiles doubles** : la Lune gêne peu, mais le seeing compte beaucoup (oculaire de 10 mm seulement si le seeing est bon).

Préciser lequel des deux types la nuit favorise et quel oculaire est conseillé. Rappeler de sortir le C8 environ 45 min avant pour la mise en température, et conseiller un pare-buée ou une résistance chauffante si l'humidité est élevée.

## Étape 3 — Graphisme de la phase de Lune (obligatoire)

Tout en **SVG inline** dans la page, aucune image externe. SVG avec `viewBox` et largeur 100 % pour rester lisible sur mobile.

1. **Icône de Lune par nuit** (environ 40 px, dans le tableau) : disque sombre et partie éclairée tracée géométriquement à partir de la fraction éclairée réelle *k* — terminateur = demi-cercle + demi-ellipse de demi-axe horizontal *r·|1−2k|* (l'ellipse ajoute de la lumière si *k* > 0,5, en retire sinon). Orientation vue de l'hémisphère nord : partie éclairée **à droite** si la Lune est croissante, **à gauche** si décroissante. Sous l'icône : nom de la phase (Nouvelle Lune, Premier croissant, Premier quartier, Gibbeuse croissante, Pleine Lune, Gibbeuse décroissante, Dernier quartier, Dernier croissant) et pourcentage.
2. **Bandeau « Lune de la semaine »** en tête de page, sous le résumé : les 7 icônes plus grandes (environ 70 px) alignées avec leur date.
3. **Frise horaire par nuit** (du coucher au lever du Soleil) : crépuscules et nuit astronomique (dégradé du rouge sombre vers le noir), période où la Lune est au-dessus de l'horizon (bande rouge clair, intensité proportionnelle à l'illumination), meilleure fenêtre d'observation en surbrillance. Graduations horaires lisibles.
4. **Couleurs** : partie éclairée en rouge clair (#ff6b6b ou #e05050), partie sombre en rouge très sombre (#2a0a0a) avec un fin contour. Aucune couleur blanche ou bleue vive.
5. **Contrôle** : l'icône, le nom de la phase et le pourcentage doivent correspondre aux données collectées.

## Étape 4 — Rédiger et publier

Structure de la fiche :
1. Résumé de 2 ou 3 phrases avec la ou les meilleures nuits, suivi du bandeau « Lune de la semaine ».
2. Tableau des 7 nuits : date, note, verdict, nuages, Lune (icône, illumination et heures), seeing / transparence, humidité / buée, meilleure fenêtre.
3. Sous le tableau, les frises horaires des 7 nuits.
4. Un court paragraphe par nuit intéressante (note ≥ 3) avec les cibles conseillées.
5. Une ligne sur la fiabilité des prévisions.
6. Une liste « Sources: » avec les liens utilisés.

Publier la fiche sous forme de **page artifact** (HTML lisible sur mobile, thème sombre rouge et noir pour préserver la vision nocturne). Envoyer ensuite à l'utilisateur, via `SendUserMessage`, un court message résumant les meilleures nuits.
