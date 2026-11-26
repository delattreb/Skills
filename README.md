# Skills

Mes skills personnels pour Claude.

| Skill | Rôle |
|---|---|
| [pro-1to1](pro/pro-1to1/SKILL.md) | Préparer un entretien 1to1 avec un membre de mon équipe à partir de mes mails, Teams et agenda (Microsoft 365, lecture seule), archivé dans Obsidian (NeomaVault). |
| [pro-agenda](pro/pro-agenda/SKILL.md) | Préparer mes réunions des 7 prochains jours avec le contexte tiré de mes mails, de Teams et des comptes rendus, dans Obsidian (NeomaVault). |
| [pro-point-avancement](pro/pro-point-avancement/SKILL.md) | Rédiger mon point d'avancement hebdomadaire à partir d'Outlook et Teams (lecture seule). |
| [pro-mcp-creator](pro/pro-mcp-creator/SKILL.md) | Créer un squelette de serveur MCP (Python FastMCP ou TypeScript) avec outils, tests et configuration client. |
| [pro-ppt-neoma](pro/pro-ppt-neoma/SKILL.md) | Créer un PowerPoint modifiable au format NEOMA. |
| [pro-sauvegarde-contexte](pro/pro-sauvegarde-contexte/SKILL.md) | Sauvegarder la conversation en cours en fiche taguée dans Obsidian (NeomaVault, dossier Sauvegarde, classée par sujet). |
| [pro-recherche-emploi-informatique](pro/pro-recherche-emploi-informatique/SKILL.md) | Rechercher et classer des offres de responsable informatique à Rouen, et trier ma boîte Gmail « Emploi ». |
| [pro-veille-informatique](pro/pro-veille-informatique/SKILL.md) | Veille informatique quotidienne (IA, enseignement supérieur, Microsoft 365 et cloud, cyber, réglementation, infra, marché, geekerie) à partir du web, un fichier daté par jour dans Obsidian (MonVault). |
| [perso-critique-dessin](perso/perso-critique-dessin/SKILL.md) | Critiquer mes dessins, les intégrer dans mes fiches Obsidian et suivre ma progression. |
| [perso-culture-generale-obsidian](perso/perso-culture-generale-obsidian/SKILL.md) | Créer et gérer les fiches illustrées de culture générale du parcours CGI dans Obsidian. |
| [perso-information](perso/perso-information/SKILL.md) | Point d'information quotidien : actualité internationale et française importante, uniquement des faits confirmés, dans Obsidian (MonVault). |
| [perso-meteo-astro-hebdo](perso/perso-meteo-astro-hebdo/SKILL.md) | Fiche météo astro des 7 prochaines nuits pour mon C8, avec graphisme des phases de Lune. |
| [perso-recettes-obsidian](perso/perso-recettes-obsidian/SKILL.md) | Créer, illustrer et modifier des recettes Markdown dans Obsidian. |

## Installation

Le dépôt est un plugin Claude (`.claude-plugin/plugin.json`) qui regroupe tous les skills de `pro/` et `perso/`.

- **Marketplace Claude Code** :

  ```
  /plugin marketplace add delattreb/Skills
  /plugin install skills-perso@skills-perso
  ```

- **Tout d'un coup** : importer dans Claude (Paramètres → Capacités) une archive .zip du dépôt dont la racine contient `.claude-plugin/`.
- **Un seul skill** : importer une archive .zip qui ne contient que le dossier de ce skill (par exemple `pro-agenda/` avec son `SKILL.md`).
