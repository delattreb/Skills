# Procédure de release

Une release = une version du plugin, un tag Git et une GitHub Release.

## Règles

- Version unique, `MAJOR.MINOR.PATCH`, portée par `.claude-plugin/plugin.json`.
- Tag Git au format `X.Y.Z`, identique à la version du manifeste (ex. `1.6.0`). Le workflow `.github/workflows/release.yml` le crée automatiquement sur `main` après la fusion de la Pull Request.
- Le `CHANGELOG.md` racine reçoit une section par release. Les `CHANGELOG.md` des skills gardent leur détail propre.
- La branche `dev` reçoit les commits. La branche `main` reçoit la release par Pull Request.

## Étapes

1. Sur `dev`, mettre à jour `.claude-plugin/plugin.json` (`version`) dans le même commit que le CHANGELOG. Cette étape est obligatoire : sans elle, l'import du zip affiche l'ancienne version (règle détaillée dans `CLAUDE.md`).
   Vérifier aussi que la `description` du plugin dans `.claude-plugin/marketplace.json` est identique à celle de `plugin.json` (la marketplace ne porte pas de `version`).
2. Ajouter la section `## [X.Y.Z] — AAAA-MM-JJ` dans `CHANGELOG.md` racine (Ajouté, Modifié, Corrigé, Supprimé).
3. Committer (`release X.Y.Z`) et pousser `dev`.
4. Ouvrir une Pull Request de `dev` vers `main` (brouillon), la relire et la fusionner.
5. Le workflow `release` se lance au push sur `main`. Il lit la version de `plugin.json`, vérifie la `description` de `marketplace.json` (identique, sans champ `version`), puis crée le tag `X.Y.Z` et la GitHub Release avec les notes de la section `## [X.Y.Z]` du `CHANGELOG.md`. Il ne fait rien si la release existe déjà. Relance manuelle : onglet Actions, `release`, Run workflow.
6. Vérifier que la Release existe et que `git show X.Y.Z:.claude-plugin/plugin.json` affiche `"version": "X.Y.Z"`.

## Versionnement

- PATCH : correctif sans nouvelle fonctionnalité.
- MINOR : nouvelle fonctionnalité ou nouveau skill, ou évolution compatible.
- MAJOR : changement incompatible, par exemple renommage d'une commande slash.
