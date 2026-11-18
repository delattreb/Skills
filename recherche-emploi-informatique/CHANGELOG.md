# Changelog — recherche-emploi-informatique

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Chaque version publiée est marquée par un tag Git `recherche-emploi-informatique-vX.Y.Z`.

## [0.2.0] — 2026-11-18
### Ajouté
- Tri de la boîte Gmail, libellé « Emploi » : parcours de tous les messages, détection des offres en doublon, corbeille des doublons (jamais de suppression définitive), passage en lu des alertes exploitées.
- Règles de lecture des alertes volumineuses (Indeed : environ 25 000 jetons par mail) et de détection des doublons par l'offre en tête d'objet.
- Point 7 du rapport : bilan du tri Gmail. Le tri s'exécute aussi dans la recherche planifiée du lundi.

## [0.1.0]
### Ajouté
- Recherche d'offres de responsable informatique à Rouen, classement sur 5 selon le profil de référence, règles de fraîcheur, de salaire et de dates.
