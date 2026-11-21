# Changelog — loisir-information

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).

## [0.1.0] — 2026-11-21
### Ajouté
- Fichier de configuration `config/sources.json` : médias et sources officielles activables, volet de chaque source, seuil de confirmation.
- Première version : point d'information quotidien en français sur deux volets, international et France, avec une rubrique « À surveiller » pour les échéances officielles.
- Fenêtre de 24 h (72 h le lundi, depuis le dernier point pour un lancement manuel), 5 éléments au plus par volet, un fichier daté par jour.
- Règle de confirmation : deux médias reconnus indépendants, ou une source officielle. Ni agrégateur, ni réseau social comme preuve.
- Neutralité : faits attribués, sujets disputés sans conclusion, statut « en cours d'établissement » signalé.
- Enregistrement dans Obsidian MonVault, dossier `information` à la racine du coffre.
- Référence `references/sources.md` : médias reconnus, sources officielles, requêtes de départ et indices d'importance.
