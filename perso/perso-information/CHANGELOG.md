# Changelog — perso-information

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).

## [Non publié]
### Modifié
- Renommage : le préfixe `loisir-` devient `perso-` (dossier, champ `name`, commande slash). Le dossier `loisir/` du dépôt devient `perso/`. Changement incompatible pour les commandes existantes.

## [0.5.0] — 2026-11-21
### Ajouté
- Fait à source unique : un fait confirmé par une seule source listée figure dans les volets, marqué « source unique », jamais dans « À retenir ».

## [0.4.0] — 2026-11-21
### Ajouté
- Rubrique « En cours » : sujets suivis sur plusieurs jours, avec le dernier fait confirmé.
- Rubrique « Agenda officiel » remplace « À surveiller » : échéances officielles uniquement.
- Phrase de climat en tête si aucun fait n'est confirmé, à partir des seuls faits confirmés.
- Étape 2 : requêtes d'agenda officiel et de sujets ouverts.

## [0.3.0] — 2026-11-21
### Ajouté
- Sources : Euronews, Le Temps, Public Sénat, The National (médias actifs) ; Ministère de l'Intérieur, CIJ, Refworld (officielles actives). Anadolu et Democracy Now présents mais inactifs (`actif: false`).

## [0.2.2] — 2026-11-21
### Modifié
- Sources retirées de `config/sources.json` : domaines refusés par l'outil de recherche (Reuters, AP, BBC, The Guardian, Le Monde, AFP, RFI). Leurs dépêches reprises nommément restent acceptées.

## [0.2.1] — 2026-11-21
### Modifié
- Dossier de destination renommé `Information` (majuscule initiale), selon le nom réel dans le coffre.
- Rien de notable : un volet sans fait confirmé affiche « Rien de notable dans la fenêtre. » ; aucun résumé d'agrégateur ni piste non vérifiée n'est ajouté. Si les deux volets sont vides, le point le signale en une phrase.

## [0.2.0] — 2026-11-21
### Modifié
- Fenêtre portée à 48 h (72 h le lundi), après test : une actualité de la veille, comme la CIJ le 19 novembre 2026, était exclue.
- Confirmation par dépêche d'agence reprise nommément (AFP, Reuters, AP), sur un autre site.
- Limites de l'outil de recherche documentées (`allowed_domains` refusé pour les grands médias).

## [0.1.0] — 2026-11-21
### Ajouté
- Fichier de configuration `config/sources.json` : médias et sources officielles activables, volet de chaque source, seuil de confirmation.
- Première version : point d'information quotidien en français sur deux volets, international et France, avec une rubrique « À surveiller » pour les échéances officielles.
- Fenêtre de 24 h (72 h le lundi, depuis le dernier point pour un lancement manuel), 5 éléments au plus par volet, un fichier daté par jour.
- Règle de confirmation : deux médias reconnus indépendants, ou une source officielle. Ni agrégateur, ni réseau social comme preuve.
- Neutralité : faits attribués, sujets disputés sans conclusion, statut « en cours d'établissement » signalé.
- Enregistrement dans Obsidian MonVault, dossier `Information` à la racine du coffre.
- Référence `references/sources.md` : médias reconnus, sources officielles, requêtes de départ et indices d'importance.
