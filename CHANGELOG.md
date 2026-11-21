# Changelog

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
La version du plugin (`.claude-plugin/plugin.json`) sert de version unique de release. Le détail par skill reste dans le `CHANGELOG.md` de chaque skill.

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
