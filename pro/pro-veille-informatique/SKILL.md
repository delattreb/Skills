---
name: "pro-veille-informatique"
description: "Rédige en français une veille informatique hebdomadaire couvrant les 7 derniers jours sur sept catégories : IA et outils IA, SI de l'enseignement supérieur, Microsoft 365 et cloud, cybersécurité, réglementation et données, infrastructure réseau et poste de travail, marché et éditeurs. S'appuie uniquement sur des recherches web, ne retient que des informations confirmées, chacune datée et sourcée par un lien, et l'enregistre dans Obsidian (coffre MonVault, dossier veille, un fichier horodaté par lancement : AAAA-MM-JJ veille informatique.md). À utiliser quand l'utilisateur demande « veille informatique », « veille IT », « veille techno », « /pro-veille-informatique », « quoi de neuf en IT cette semaine », « actus IA / cyber / Microsoft 365 / enseignement supérieur » ou lance la veille hebdomadaire planifiée."
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
- **Une seule écriture par lancement : le fichier horodaté** `AAAA-MM-JJ veille informatique.md` (date du jour de lancement) dans `MonVault/veille` (voir l'étape 5). Les veilles des semaines précédentes ne sont jamais modifiées.
- **Informations confirmées uniquement.** Un élément n'entre dans la veille que s'il est confirmé par une **source primaire** (éditeur, organisme officiel, établissement concerné) ou par un **média reconnu** (voir `references/sources-et-requetes.md`). Un élément connu seulement par des agrégateurs, des blogs anonymes, des pages générées automatiquement ou des réseaux sociaux est **exclu**, même s'il paraît important. Il n'y a pas de rubrique « à confirmer ».
- **Ne rien inventer.** Chaque élément a au moins un lien et une date de publication. Pas de lien reconstruit de mémoire : uniquement des URL renvoyées par la recherche ou ouvertes.
- **Période stricte.** Ne retenir que des informations publiées entre début et fin de période (étape 1). Une annonce plus ancienne n'entre que si un fait nouveau est publié dans la période (déploiement effectif, date de fin de support qui approche), et ce fait nouveau est alors daté.
- **Statut explicite.** Indiquer « (annonce) », « (préversion) » ou « (déployé) » quand le statut n'est pas évident.
- **Une seule catégorie par élément.** Un même fait n'apparaît qu'une fois, dans la catégorie la plus utile ; les autres angles peuvent être mentionnés dans la ligne « Pour NEOMA ».
- **Recherche web indisponible.** Si aucun outil de recherche web n'est disponible ou qu'il échoue, s'arrêter et l'indiquer en une ligne. Ne pas produire de veille de mémoire.

## Étape 1 : Préparer

1. Charger l'outil de recherche web via ToolSearch si nécessaire (par exemple `select:WebSearch`).
2. Calculer les bornes : **début = jour de lancement − 7 jours**, **fin = jour de lancement** (fuseau Europe/Paris). Noter la date du jour au format `AAAA-MM-JJ` pour le nom du fichier.
3. Lire `references/sources-et-requetes.md` : sources fiables, requêtes de départ par catégorie et indices de pertinence.

## Étape 2 : Collecter (lancer les recherches indépendantes en parallèle)

Pour chaque catégorie, lancer plusieurs requêtes (françaises et anglaises) en y ajoutant le mois et l'année en cours :

1. **IA et outils IA** : nouveaux modèles et fonctionnalités des principaux éditeurs, Copilot et assistants, agents, usages en entreprise et dans l'enseignement.
2. **SI de l'enseignement supérieur** : écoles de commerce et universités, éditeurs du secteur (scolarité, LMS, ENT, admissions, examens), RENATER, ministère, projets marquants dans le secteur.
3. **Microsoft 365 et cloud** : nouvelles fonctionnalités et changements Microsoft 365 (Teams, Outlook, SharePoint, OneDrive, Copilot, Entra), Azure, Google Workspace, retraits de fonctionnalités.
4. **Cybersécurité** : vulnérabilités critiques activement exploitées, alertes CERT-FR et ANSSI, attaques touchant l'enseignement supérieur, campagnes d'hameçonnage notables.
5. **Réglementation et données** : RGPD et décisions CNIL, AI Act, NIS2, accessibilité numérique (RGAA), obligations nouvelles pour les établissements.
6. **Infra, réseau et poste de travail** : Windows et Windows Server, Intune, réseau et Wi-Fi, matériel, pannes de services majeures, fins de support.
7. **Marché et éditeurs** : rachats, changements de prix et de licences, évolutions de contrats, éditeurs utilisés par NEOMA.

Ouvrir les articles les plus prometteurs pour vérifier la date, le fond et le statut. Remonter à la source primaire quand une information vient d'une reprise ; si aucune source primaire ni média reconnu ne la confirme, l'écarter.

## Étape 3 : Trier

- Écarter les éléments non confirmés (voir les règles impératives), les doublons (garder une entrée, source primaire en premier), le contenu promotionnel, les tribunes sans fait nouveau, les tutoriels et les articles hors période.
- Pour chaque élément retenu, évaluer la **pertinence pour NEOMA** : impact sur les utilisateurs, les licences, la sécurité, la conformité, les projets SI, la pédagogie. Garder 2 à 5 éléments par catégorie, classés du plus au moins important.
- Repérer les **échéances** (fins de support, changements de prix, entrées en application de textes, dates de déploiement) dans les semaines ou mois à venir.

## Étape 4 : Rédiger

Respecter exactement ce format :

```
# Veille informatique : semaine du [JJ mois] au [JJ mois AAAA]

## À retenir
- [3 points maximum, une ligne chacun : le plus important de la semaine toutes catégories confondues]

## IA et outils IA
### [Titre court et factuel]
[2 à 3 phrases : ce qui s'est passé, statut, date.]
**Pour NEOMA :** [impact concret ou action possible, une phrase.]
Source : [Nom du site, JJ/MM/AAAA](URL)

## SI de l'enseignement supérieur
…

## Microsoft 365 et cloud
…

## Cybersécurité
…

## Réglementation et données
…

## Infra, réseau et poste de travail
…

## Marché et éditeurs
…

## Échéances à surveiller
- [JJ/MM/AAAA] : [échéance] ([source](URL))
```

Style : concis, professionnel, sans remplissage ni formule d'introduction. Une catégorie sans actualité confirmée affiche « Rien de notable sur la période. » plutôt que d'être complétée avec des éléments faibles, non confirmés ou hors période. La rubrique « Échéances à surveiller » est omise si aucune échéance n'a été trouvée.

## Étape 5 : Enregistrer dans Obsidian

Cible : **`Mon Drive/ObsidianVault/MonVault/veille/AAAA-MM-JJ veille informatique.md`**, où `AAAA-MM-JJ` est la date du jour de lancement (exemple : `2026-11-21 veille informatique.md` ; chemin local : `G:\Mon Drive\ObsidianVault\MonVault\veille\2026-11-21 veille informatique.md`). Le dossier `veille` est à la racine du coffre MonVault et s'écrit en minuscules. Ne jamais écrire dans le coffre de `pro-agenda`, `pro-1to1` ou `pro-point-avancement`.

1. Si les outils du dossier connecté de l'ordinateur sont disponibles et que `G:\Mon Drive\ObsidianVault\MonVault` y est accessible, écrire le fichier directement dans `MonVault\veille` (créer ce dossier s'il n'existe pas). Sinon, passer par Google Drive.
2. Via Google Drive : retrouver le dossier `MonVault` et **vérifier la chaîne complète des parents** : `MonVault → ObsidianVault → Mon Drive`. Ne jamais écrire dans un autre coffre ni dans une copie homonyme. Si la chaîne est introuvable ou ambiguë, s'arrêter et demander le lien du dossier.
3. Dans ce `MonVault` vérifié, chercher le sous-dossier `veille` directement à la racine du coffre. S'il n'existe pas, le créer (`create_file`, type `application/vnd.google-apps.folder`) avec `MonVault` comme parent explicite. Ne jamais créer un second dossier `veille` ou `Veille`.
4. Créer le fichier du jour (`create_file`) avec `veille` comme parent explicite. Si un fichier portant **la même date** existe déjà (veille relancée le même jour), mettre l'ancien à la corbeille (`trash_file`) avant de créer le nouveau, et le signaler dans la réponse finale. Ne jamais créer de doublon (`… (1).md`) et ne jamais toucher aux fichiers d'autres dates.
5. Enregistrer un vrai fichier texte UTF-8 `.md` (`contentMimeType` `text/markdown`, `disableConversionToGoogleType` à vrai), **sans conversion en Google Doc**, pour qu'il reste lisible dans Obsidian. Le contenu est exactement la veille de l'étape 4.
6. Relire les métadonnées du fichier enregistré : nom, parent, type. Ne pas affirmer que la synchronisation locale Obsidian est terminée.

Si l'écriture est impossible, livrer la veille complète dans le chat et expliquer ce qui a bloqué.

## Étape 6 : Réponse finale

Livrer dans le chat un court bilan : le nom et l'emplacement du fichier (lien Drive si disponible) et les points de la rubrique « À retenir », une ligne chacun. Ne pas recopier toute la veille sauf si l'écriture a échoué. Si l'outil SendUserMessage est disponible (notamment en exécution planifiée sans personne présente), y envoyer ce même bilan. Ne pas l'envoyer par e-mail ni sur Teams.
