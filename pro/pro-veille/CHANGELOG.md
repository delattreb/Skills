# Changelog — pro-veille

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Ce skill remplace `pro-veille-informatique` (dernière version 0.7.0) et `perso-information` (dernière version 0.5.1).

## [1.0.0] — 2026-11-24
### Ajouté
- Six catégories : politique, économie, IA, informatique, développement, 3D.
- `config/flux.json` (85 flux, 75 actifs après test du 24/11/2026) et `scripts/flux.py` : lecture des flux RSS/Atom en parallèle, filtre par fenêtre, 3 entrées par flux, test d'accessibilité avec désactivation des flux en échec.
- `references/recherche.md` : sources officielles, médias reconnus, requêtes de complément.
### Modifié
- Confirmation : une seule source suffit (source primaire ou officielle, ou média reconnu), pour toutes les catégories. Plus de double confirmation ni de marque « source unique ».
- Une note par jour : `Veille/AAAA-MM-JJ veille.md`.
### Supprimé
- Catégories NEOMA (enseignement supérieur, Microsoft 365, réglementation, marché, geekerie), ligne « Pour NEOMA » et `references/contexte-neoma.md`.
- Script KEV et recherche restreinte par `allowed_domains`.
