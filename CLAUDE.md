# Consignes pour Claude dans ce dépôt

## Release : version du plugin

- Toute release met à jour `.claude-plugin/plugin.json` (champ `version`) dans le même commit que la section `## [X.Y.Z]` de `CHANGELOG.md` racine.
- Le tag Git, le nom du zip et la version du manifeste sont identiques (`X.Y.Z`). Ne jamais créer un tag sans cette montée de version.
- Avant de créer un tag, vérifier : `git show X.Y.Z:.claude-plugin/plugin.json` doit afficher `"version": "X.Y.Z"`. Sinon, ne pas tagger et signaler le problème.
- Ne jamais déplacer ou supprimer un tag publié sans accord explicite de l'utilisateur.
- `.claude-plugin/marketplace.json` ne porte pas de champ `version` : la version vient de `plugin.json`, qui l'emporte sur l'entrée de la marketplace. Ne pas l'ajouter.
- La `description` de l'entrée du plugin dans `marketplace.json` reste identique à celle de `plugin.json`. À vérifier à chaque release.
- Procédure complète : `RELEASE.md`.
