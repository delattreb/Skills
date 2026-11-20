# Changelog — pro-point-avancement

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Chaque version publiée est marquée par un tag Git `pro-point-avancement-vX.Y.Z`.

## [Non publié]
### Renommé
- Skill renommé : `point-avancement` devient `pro-point-avancement` (dossier, champ `name`, commande `/pro-point-avancement`, tags Git `pro-point-avancement-vX.Y.Z`).

## [0.2.0] — 2026-11-18
### Modifié
- Le rapport final est désormais enregistré dans Obsidian : `G:\Mon Drive\ObsidianVault\Neoma Vault\Agenda\point avancement.md` (remplacé à chaque lancement, vérification de la chaîne de dossiers parents, pas de doublon).
- Réponse finale réduite à un bilan court (emplacement du fichier et 3 points clés) ; le rapport complet n'est recopié dans le chat qu'en cas d'échec de l'écriture.
- La règle de lecture seule est précisée : elle porte sur Microsoft 365 ; `point avancement.md` est la seule écriture autorisée.

## [0.1.0] — 2026-11-15
### Ajouté
- Première version : point d'avancement hebdomadaire en français (7 derniers jours) à partir des e-mails envoyés et reçus, du calendrier Outlook et de Teams via le connecteur Microsoft 365.
- Format : réalisations par projet, décisions, en suspens / à suivre, à venir (7 jours suivants).
- Lecture seule stricte ; signalement en une ligne si le connecteur est indisponible.
- Référence `references/tri-et-classement.md` pour filtrer le bruit et classer les éléments.
