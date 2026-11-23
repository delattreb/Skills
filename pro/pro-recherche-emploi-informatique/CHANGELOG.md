# Changelog — pro-recherche-emploi-informatique

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Chaque version publiée est marquée par un tag Git `pro-recherche-emploi-informatique-vX.Y.Z`.

## [Non publié]
### Ajouté
- Gmail : repérage des messages qui appellent une réponse et des demandes de contact, avec section « À traiter dans Gmail » en tête du rapport.
### Modifié
- Gmail : tous les messages passés en revue sont marqués lus (la notification LinkedIn n'est plus une exception).
- Profil de référence déplacé dans `references/profil.md` ; SKILL.md allégé.
- Indeed : usage du connecteur (`search_jobs`, `get_job_details`, `get_company_data`) plutôt que des pages web.
- Rapport : ajout d'une synthèse de trois lignes en tête, cellules du tableau en une phrase.
### Renommé
- Skill renommé : `recherche-emploi-informatique` devient `pro-recherche-emploi-informatique` (dossier, champ `name`, commande `/pro-recherche-emploi-informatique`, tags Git `pro-recherche-emploi-informatique-vX.Y.Z`).

## [0.3.0] — 2026-11-18
### Modifié
- Critère télétravail supprimé : il ne qualifie ni n'exclut une offre, et la colonne « Lieu / télétravail » devient « Lieu ».
- Zone de recherche : Rouen et alentours dans un rayon de 30 km (au lieu de Rouen, environs et télétravail partiel). Les offres au-delà sont écartées.

## [0.2.0] — 2026-11-18
### Ajouté
- Tri de la boîte Gmail, libellé « Emploi » : parcours de tous les messages, détection des offres en doublon, corbeille des doublons (jamais de suppression définitive), passage en lu des alertes exploitées.
- Règles de lecture des alertes volumineuses (Indeed : environ 25 000 jetons par mail) et de détection des doublons par l'offre en tête d'objet.
- Point 7 du rapport : bilan du tri Gmail. Le tri s'exécute aussi dans la recherche planifiée du lundi.

## [0.1.0]
### Ajouté
- Recherche d'offres de responsable informatique à Rouen, classement sur 5 selon le profil de référence, règles de fraîcheur, de salaire et de dates.
