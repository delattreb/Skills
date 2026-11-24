# Changelog

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
La version du plugin (`.claude-plugin/plugin.json`) sert de version unique de release. Le détail par skill reste dans le `CHANGELOG.md` de chaque skill.

## [2.5.0] — 2026-11-24
### Ajouté
- `pro-veille-informatique` 0.7.0 : passe 4 « Lecture renforcée (Apify) » (skill `apify:apify-ultimate-scraper`, Actor `apify/rag-web-browser`) pour lire les articles que la lecture directe n'ouvre pas ; pages publiques seulement, 5 pages au plus par lancement. Le skill invoque aussi `caveman:caveman` pour le style des messages de travail et du bilan.
### Modifié
- `pro-veille-informatique` : format de la note (tableau « Vue d'ensemble », callouts Obsidian selon la pertinence) et tags YAML par catégorie.
- Règle `marketplace.json` : pas de champ `version`, description alignée sur `plugin.json` (`CLAUDE.md`, `RELEASE.md`).

## [2.4.0] — 2026-11-23
### Ajouté
- `perso-information` 0.5.1 : sept médias ajoutés dans `config/sources.json` (BBC News, The Guardian, Le Monde, RFI, Reuters, Associated Press, AFP), à chercher sans `allowed_domains`, pour élargir les sources éligibles à la double confirmation.

## [2.3.0] — 2026-11-23
### Ajouté
- Marketplace Claude Code : `.claude-plugin/marketplace.json` expose le plugin `skills-perso`. Installation par `/plugin marketplace add delattreb/Skills` puis `/plugin install skills-perso@skills-perso` (voir `README.md`).
### Modifié
- Manifeste `plugin.json` : ajout du champ `author`.

## [2.2.0] — 2026-11-23
### Ajouté
- `pro-recherche-emploi-informatique` 0.5.0 : repli sur `curl` quand l'outil de lecture de pages échoue, lecture de `datePosted` et `validThrough` dans les données JSON-LD des offres, page 404 traitée comme offre retirée.

## [2.1.0] — 2026-11-23
### Ajouté
- `pro-recherche-emploi-informatique` 0.4.0 : repérage des messages Gmail qui appellent une réponse ou une demande de contact, section « À traiter dans Gmail », tous les messages passés en revue marqués lus.
### Modifié
- `pro-recherche-emploi-informatique` : profil de référence dans `references/profil.md`, connecteur Indeed, synthèse en tête du rapport.

## [2.0.0] — 2026-11-21
### Modifié
- Renommage (changement incompatible) : le dossier `loisir/` devient `perso/`, et chaque skill `loisir-*` devient `perso-*`. Les commandes slash changent en conséquence (par exemple `/loisir-information` devient `/perso-information`).
- Manifeste `plugin.json` : chemins `./pro/` et `./perso/`, description et version 2.0.0.

## [1.7.0] — 2026-11-21
### Ajouté
- Skill `loisir-information` 0.5.0 : point d'information quotidien en deux volets (international et France), avec faits confirmés par deux médias reconnus, une source officielle ou une dépêche d'agence reprise nommément ; faits à source unique marqués ; rubriques « En cours » et « Agenda officiel ».
- Enregistrement dans Obsidian MonVault, dossier `Information`, un fichier daté par jour.
- Configuration des sources dans `loisir/loisir-information/config/sources.json`.

## [1.6.2] — 2026-11-21
### Modifié
- Règle de release : la version de `.claude-plugin/plugin.json` est mise à jour dans le même commit que le CHANGELOG et vérifiée avant le tag (`CLAUDE.md`, `RELEASE.md`).

## [1.6.1] — 2026-11-21
### Modifié
- `pro-veille-informatique` : tags YAML par catégorie dans la veille et champ `tags` dans le frontmatter du skill ; format de la note fixé (tableau « Vue d'ensemble », callouts colorés).

## [1.6.0] — 2026-11-21
### Modifié
- `pro-veille-informatique` 0.5.0 : dossier Veille, astronomie, Obsidian, YAML, deux requêtes maximum.
- `pro-veille-informatique` 0.6.0 : sources testées avec le moteur de recherche, renvoyant des résultats datés ; domaines ajoutés aux catégories et aux médias reconnus.
