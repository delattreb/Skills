# Procédure de release

Une release = une version du plugin, un tag Git et une GitHub Release.

## Règles

- Version unique, `MAJOR.MINOR.PATCH`, portée par `.claude-plugin/plugin.json`.
- Tag Git au format `X.Y.Z`, identique à la version du manifeste (ex. `1.6.0`), créé sur la branche `dev`.
- Le `CHANGELOG.md` racine reçoit une section par release. Les `CHANGELOG.md` des skills gardent leur détail propre.
- La branche `dev` reçoit les commits. La branche `main` reçoit la release par Pull Request.

## Étapes

1. Sur `dev`, mettre à jour `.claude-plugin/plugin.json` (`version`) dans le même commit que le CHANGELOG. Cette étape est obligatoire : sans elle, l'import du zip affiche l'ancienne version (règle détaillée dans `CLAUDE.md`).
   Vérifier aussi que la `description` du plugin dans `.claude-plugin/marketplace.json` est identique à celle de `plugin.json` (la marketplace ne porte pas de `version`).
2. Ajouter la section `## [X.Y.Z] — AAAA-MM-JJ` dans `CHANGELOG.md` racine (Ajouté, Modifié, Corrigé, Supprimé).
3. Committer (`release X.Y.Z`) et pousser `dev`.
4. Créer le tag `X.Y.Z` sur le commit de `dev`, puis le pousser : `git tag X.Y.Z && git push origin X.Y.Z`.
5. Créer la GitHub Release à partir du tag, avec les notes de la section racine du CHANGELOG.
6. Ouvrir une Pull Request de `dev` vers `main` (brouillon), la relire et la fusionner.

## Versionnement

- PATCH : correctif sans nouvelle fonctionnalité.
- MINOR : nouvelle fonctionnalité ou nouveau skill, ou évolution compatible.
- MAJOR : changement incompatible, par exemple renommage d'une commande slash.
