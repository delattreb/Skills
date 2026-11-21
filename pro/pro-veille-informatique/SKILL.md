---
name: "pro-veille-informatique"
description: "Rédige en français une veille informatique hebdomadaire couvrant les 7 derniers jours sur trois thèmes : IA et outils IA, SI de l'enseignement supérieur, Microsoft 365 et cloud. S'appuie uniquement sur des recherches web, chaque élément étant daté et sourcé par un lien, et l'enregistre dans Obsidian (coffre NeomaVault, veille/veille informatique.md, remplacé à chaque lancement). À utiliser quand l'utilisateur demande « veille informatique », « veille IT », « veille techno », « /pro-veille-informatique », « quoi de neuf en IT cette semaine », « actus IA / Microsoft 365 / enseignement supérieur » ou lance la veille hebdomadaire planifiée."
metadata:
  version: "0.1.0"
---

## Approach

- Read existing files before writing. Don't re-read unless changed.
- Thorough in reasoning, concise in output.
- Skip files over 100KB unless required.
- No sycophantic openers or closing fluff.
- No emojis or em-dashes.
- Do not guess APIs, versions, flags, commit SHAs, or package names. Verify by reading code or docs before asserting.

# Veille informatique hebdomadaire

Produire une veille factuelle, en français, sur les 7 jours précédant le jour de lancement, utile à un responsable informatique d'une école de commerce (NEOMA) : ce qui a changé, ce que cela implique, ce qu'il faut surveiller.

## Règles impératives

- **Sources web uniquement.** Ne consulter ni la messagerie, ni l'agenda, ni Teams. Utiliser l'outil de recherche web disponible (WebSearch ou équivalent) et, si besoin, la lecture de page pour vérifier un article.
- **Une seule écriture : `veille informatique.md`.** C'est le seul fichier créé ou modifié (voir l'étape 5). Il est remplacé entièrement à chaque lancement.
- **Ne rien inventer.** Chaque élément repose sur au moins une source consultée, avec son lien et sa date de publication. Pas de lien reconstruit de mémoire : uniquement des URL renvoyées par la recherche ou ouvertes.
- **Période stricte.** Ne retenir que des informations publiées entre début et fin de période (étape 1). Une annonce plus ancienne n'entre que si un fait nouveau est publié dans la période (déploiement effectif, date de fin de support qui approche), et ce fait nouveau est alors daté.
- **Distinguer annonce, rumeur et déploiement.** Indiquer « (annonce) », « (préversion) », « (déployé) » ou « (non confirmé) » quand le statut n'est pas évident.
- **Recherche web indisponible.** Si aucun outil de recherche web n'est disponible ou qu'il échoue, s'arrêter et l'indiquer en une ligne. Ne pas produire de veille de mémoire.

## Étape 1 : Préparer

1. Charger l'outil de recherche web via ToolSearch si nécessaire (par exemple `select:WebSearch`).
2. Calculer les bornes : **début = jour de lancement − 7 jours**, **fin = jour de lancement** (fuseau Europe/Paris).
3. Lire `references/sources-et-requetes.md` : sources prioritaires et requêtes de départ par thème.

## Étape 2 : Collecter (lancer les recherches indépendantes en parallèle)

Pour chacun des trois thèmes, lancer plusieurs requêtes (françaises et anglaises) en y ajoutant le mois et l'année en cours :

1. **IA et outils IA** : nouveaux modèles et fonctionnalités des principaux éditeurs, Copilot, agents, usages en entreprise et dans l'enseignement, réglementation (AI Act, CNIL).
2. **SI de l'enseignement supérieur** : écoles de commerce et universités, éditeurs du secteur (scolarité, LMS, ENT, admissions), RENATER, ministère, incidents ou projets marquants dans le secteur.
3. **Microsoft 365 et cloud** : nouveautés et changements Microsoft 365 (Teams, Outlook, SharePoint, Copilot, Entra), Azure, Google Workspace, licences et prix, fins de support, retraits de fonctionnalités.

Ouvrir les articles les plus prometteurs pour vérifier la date, le fond et le statut. Préférer la source primaire (annonce de l'éditeur, communiqué officiel) à une reprise ; citer la reprise en français seulement si elle apporte du contexte.

## Étape 3 : Trier

- Écarter les doublons (même annonce reprise par plusieurs médias : garder une entrée, avec la source primaire en premier).
- Écarter le contenu promotionnel, les tribunes sans fait nouveau, les tutoriels et les articles hors période.
- Pour chaque élément retenu, évaluer la **pertinence pour NEOMA** : impact sur les utilisateurs, les licences, la sécurité, les projets SI, la pédagogie. Garder 3 à 6 éléments par thème, classés du plus au moins important.
- Repérer les **échéances** (fins de support, changements de prix, dates de déploiement) dans les semaines ou mois à venir.

## Étape 4 : Rédiger

Respecter exactement ce format :

```
# Veille informatique : semaine du [JJ mois] au [JJ mois AAAA]

## À retenir
- [3 points maximum, une ligne chacun : le plus important de la semaine tous thèmes confondus]

## IA et outils IA
### [Titre court et factuel]
[2 à 3 phrases : ce qui s'est passé, statut, date.]
**Pour NEOMA :** [impact concret ou action possible, une phrase.]
Source : [Nom du site, JJ/MM/AAAA](URL)

## SI de l'enseignement supérieur
…

## Microsoft 365 et cloud
…

## Échéances à surveiller
- [JJ/MM/AAAA] : [échéance] ([source](URL))
```

Style : concis, professionnel, sans remplissage ni formule d'introduction. Un thème sans actualité pertinente affiche « Rien de notable sur la période. » plutôt que d'être complété avec des éléments faibles ou hors période. La rubrique « Échéances à surveiller » est omise si aucune échéance n'a été trouvée.

## Étape 5 : Enregistrer dans Obsidian

Cible : **`Mon Drive/ObsidianVault/NeomaVault/veille/veille informatique.md`** (chemin local : `G:\Mon Drive\ObsidianVault\NeomaVault\veille\veille informatique.md`). Le dossier `veille` est à la racine du coffre et s'écrit en minuscules. Le nom du fichier contient une espace : ne pas le confondre avec `veille-informatique.md`.

1. Si les outils du dossier connecté de l'ordinateur sont disponibles et que `G:\Mon Drive\ObsidianVault\NeomaVault` y est accessible, écrire le fichier directement dans `NeomaVault\veille`. Sinon, passer par Google Drive.
2. Via Google Drive : retrouver le dossier `NeomaVault` et **vérifier la chaîne complète des parents** : `NeomaVault → ObsidianVault → Mon Drive`. Ne jamais écrire dans `MonVault` ni dans une copie homonyme. Si la chaîne est introuvable ou ambiguë, s'arrêter et demander le lien du dossier.
3. Dans ce `NeomaVault` vérifié, prendre le sous-dossier `veille` situé directement à la racine du coffre. Ne jamais créer un autre dossier `veille` ou `Veille` : s'il est introuvable, s'arrêter et demander le lien du dossier.
4. Si `veille informatique.md` existe déjà dans `veille`, **remplacer son contenu** (`update_file`) ; sinon le **créer** (`create_file`) avec `veille` comme parent explicite. Ne jamais créer de doublon (`veille informatique (1).md`, etc.).
5. Enregistrer un vrai fichier texte UTF-8 `.md` (type `text/markdown`), **sans conversion en Google Doc**, pour qu'il reste lisible dans Obsidian. Le contenu est exactement la veille de l'étape 4.
6. Relire le fichier enregistré : nom, parent, début du contenu. Ne pas affirmer que la synchronisation locale Obsidian est terminée.

Si l'écriture est impossible, livrer la veille complète dans le chat et expliquer ce qui a bloqué.

## Étape 6 : Réponse finale

Livrer dans le chat un court bilan : l'emplacement du fichier `veille informatique.md` (lien Drive si disponible) et les points de la rubrique « À retenir », une ligne chacun. Ne pas recopier toute la veille sauf si l'écriture a échoué. Si l'outil SendUserMessage est disponible (notamment en exécution planifiée sans personne présente), y envoyer ce même bilan. Ne pas l'envoyer par e-mail ni sur Teams.
