---
name: "pro-veille-informatique"
description: "Rédige en français une veille informatique quotidienne (dernières 24 h, 72 h le lundi) sur huit catégories : IA et outils IA, SI de l'enseignement supérieur, Microsoft 365 et cloud, cybersécurité, réglementation et données, infrastructure réseau et poste de travail, marché et éditeurs, geekerie (digital painting, Raspberry Pi, Arduino, Blender, impression 3D, électronique DIY, astronomie). S'appuie uniquement sur des recherches web, ne retient que des informations confirmées, chacune datée et sourcée par un lien, et l'enregistre dans Obsidian (coffre MonVault, dossier Veille, un fichier horodaté par jour : AAAA-MM-JJ veille informatique.md). À utiliser quand l'utilisateur demande « veille informatique », « veille du jour », « fais ma veille », « veille IT », « veille techno », « /pro-veille-informatique », « quoi de neuf en IT », « actus IA / cyber / Microsoft 365 / enseignement supérieur / Raspberry / Blender / astronomie »."
metadata:
  version: "0.5.0"
---

## Approach

- Read existing files before writing. Don't re-read unless changed.
- Thorough in reasoning, concise in output.
- Skip files over 100KB unless required.
- No sycophantic openers or closing fluff.
- No emojis or em-dashes.
- Do not guess APIs, versions, flags, commit SHAs, or package names. Verify by reading code or docs before asserting.

# Veille informatique quotidienne

Produire chaque jour une veille factuelle, en français, sur l'actualité publiée depuis la veille précédente (fenêtre de l'étape 1), utile à un responsable informatique d'une école de commerce (NEOMA) : ce qui a changé, ce que cela implique, ce qu'il faut surveiller. La catégorie « Geekerie » couvre en plus ses centres d'intérêt personnels (création numérique, makers, astronomie amateur).

## Règles impératives

- **Sources web uniquement.** Ne consulter ni la messagerie, ni l'agenda, ni Teams. Utiliser le script de flux (`scripts/flux_veille.py`), l'outil de recherche web (WebSearch ou équivalent) et, quand elle fonctionne, la lecture de page pour vérifier un article.
- **Une seule écriture par lancement : le fichier horodaté** `AAAA-MM-JJ veille informatique.md` (date du jour de lancement) dans `MonVault/Veille` (voir l'étape 5). Les veilles des jours précédents ne sont jamais modifiées.
- **Informations confirmées uniquement.** Un élément n'entre dans la veille que s'il est confirmé par une **source primaire** (éditeur, organisme officiel, établissement concerné) ou par un **média reconnu** (voir `references/sources-et-requetes.md`). Quand la page ne peut pas être ouverte (réseau limité), un résultat de recherche vaut confirmation s'il provient d'un domaine accepté, porte une date explicite dans la fenêtre et donne l'URL de l'article ; s'en tenir alors aux faits présents dans le résultat. Un élément connu seulement par des agrégateurs, des blogs anonymes, des pages générées automatiquement ou des réseaux sociaux est **exclu**, même s'il paraît important. Il n'y a pas de rubrique « à confirmer ».
- **Ne rien inventer.** Chaque élément a au moins un lien et une date de publication. Pas de lien reconstruit de mémoire : uniquement des URL renvoyées par la recherche ou ouvertes.
- **Période stricte.** Ne retenir que des informations publiées entre début et fin de période (étape 1). Une annonce plus ancienne n'entre que si un fait nouveau est publié dans la période (déploiement effectif, date de fin de support qui approche), et ce fait nouveau est alors daté.
- **Statut explicite.** Indiquer « (annonce) », « (préversion) » ou « (déployé) » quand le statut n'est pas évident.
- **Une seule catégorie par élément.** Un même fait n'apparaît qu'une fois, dans la catégorie la plus utile ; les autres angles peuvent être mentionnés dans la ligne « Pour NEOMA ».
- **Recherche web indisponible.** Si aucun outil de recherche web n'est disponible ou qu'il échoue, s'arrêter et l'indiquer en une ligne. Ne pas produire de veille de mémoire.

## Étape 1 : Préparer

1. Charger l'outil de recherche web via ToolSearch si nécessaire (par exemple `select:WebSearch`).
2. Calculer la fenêtre (fuseau Europe/Paris), **fin = moment du lancement** :
   - mardi à samedi : les 24 dernières heures ;
   - lundi : depuis vendredi matin (72 h), pour couvrir le week-end ;
   - lancement manuel : depuis la date de la dernière veille présente dans `MonVault/Veille` (7 jours au maximum) ; sans veille précédente, 24 h.
   Noter la date du jour au format `AAAA-MM-JJ` pour le nom du fichier.
3. Lire la veille précédente (le fichier `AAAA-MM-JJ veille informatique.md` le plus récent de `MonVault/Veille`, s'il existe) pour ne pas reprendre un sujet déjà traité, sauf fait nouveau, signalé alors par « (suite) ».
4. Lire `references/sources-et-requetes.md` : flux lus directement, listes de domaines pour la recherche restreinte, domaines refusés, sources acceptées, requêtes de départ et indices de pertinence.
5. Lire `references/contexte-neoma.md` : outils réellement utilisés à NEOMA. Une section marquée « À compléter » n'est pas utilisée ; ne rien en déduire.

## Étape 2 : Collecter (lancer les recherches indépendantes en parallèle)

Collecter en trois passes, dans cet ordre. Deux requêtes web au maximum par catégorie, passes 2 et 3 comprises.

1. **Flux primaires** : lancer `python3 -I scripts/flux_veille.py --debut <début ISO avec fuseau> --fin <fin ISO avec fuseau>` depuis le dossier du skill. Il liste les nouveautés de la feuille de route Microsoft 365 et les vulnérabilités ajoutées au catalogue CISA KEV dans la fenêtre. Si une source est en erreur, continuer et le signaler dans le bilan.
2. **Recherche restreinte** : pour chaque catégorie, une recherche avec `allowed_domains` réglé sur la liste de la catégorie (section 2 de la référence), avec la date dans la requête. Lancer ces recherches en parallèle. Ne jamais inclure un domaine de la liste « refusés par le moteur ».
3. **Recherche libre** : pour les catégories encore vides ou maigres, une seule requête libre (française ou anglaise) avec le mois et l'année.

Thèmes à couvrir par catégorie :

1. **IA et outils IA** : nouveaux modèles et fonctionnalités des principaux éditeurs, Copilot et assistants, agents, usages en entreprise et dans l'enseignement, Obsidian (versions majeures, changements de licence ou de synchronisation).
2. **SI de l'enseignement supérieur** : écoles de commerce et universités, éditeurs du secteur (scolarité, LMS, ENT, admissions, examens), RENATER, ministère, projets marquants dans le secteur.
3. **Microsoft 365 et cloud** : nouvelles fonctionnalités et changements Microsoft 365 (Teams, Outlook, SharePoint, OneDrive, Copilot, Entra), Azure, Google Workspace, retraits de fonctionnalités.
4. **Cybersécurité** : vulnérabilités critiques activement exploitées, alertes CERT-FR et ANSSI, attaques touchant l'enseignement supérieur, campagnes d'hameçonnage notables.
5. **Réglementation et données** : RGPD et décisions CNIL, AI Act, NIS2, accessibilité numérique (RGAA), obligations nouvelles pour les établissements.
6. **Infra, réseau et poste de travail** : Windows et Windows Server, Intune, réseau et Wi-Fi, matériel, pannes de services majeures, fins de support.
7. **Marché et éditeurs** : rachats, changements de prix et de licences, évolutions de contrats, éditeurs utilisés par NEOMA.
8. **Geekerie** : digital painting (Krita, Procreate, Clip Studio Paint, Photoshop, Rebelle, tablettes graphiques), Raspberry Pi, Arduino et microcontrôleurs (ESP32, RP2040), Blender et 3D, impression 3D, électronique DIY, astronomie amateur (télescopes et accessoires, caméras, logiciels comme Stellarium, Siril, KStars) : nouvelles versions, nouveau matériel, fonctionnalités marquantes, projets remarquables.

Ouvrir les articles les plus prometteurs pour vérifier la date, le fond et le statut quand c'est possible ; si l'ouverture échoue pour cause de réseau, ne pas réessayer sur le même site et appliquer la règle de confirmation par résultat de recherche. Remonter à la source primaire quand une information vient d'une reprise ; si aucune source primaire ni média reconnu ne la confirme, l'écarter.

## Étape 3 : Trier

- Écarter les éléments non confirmés (voir les règles impératives), les doublons (garder une entrée, source primaire en premier), le contenu promotionnel, les tribunes sans fait nouveau, les tutoriels et les articles hors période.
- Pour chaque élément retenu, évaluer la **pertinence pour NEOMA** : impact sur les utilisateurs, les licences, la sécurité, la conformité, les projets SI, la pédagogie. Quand `references/contexte-neoma.md` renseigne l'outil concerné, le citer nommément dans la ligne « Pour NEOMA ». Pour la Geekerie, évaluer plutôt l'intérêt pratique : nouvelle version ou nouveau matériel utilisable, fonctionnalité qui change la façon de travailler, prix. Garder au plus 3 éléments par catégorie, classés du plus au moins important. Un jour calme donne une veille courte : ne pas combler avec des éléments faibles.
- Repérer les **échéances** (fins de support, changements de prix, entrées en application de textes, dates de déploiement) dans les semaines ou mois à venir.

## Étape 4 : Rédiger

Respecter exactement ce format, frontmatter compris :

```
---
date: AAAA-MM-JJ
type: veille-informatique
fenetre_debut: AAAA-MM-JJ HH:MM
fenetre_fin: AAAA-MM-JJ HH:MM
categories_avec_actualite: N
elements: N
tags: [veille, informatique]
---

# Veille informatique du [jour JJ mois AAAA]

## À retenir
- [3 points maximum, une ligne chacun : le plus important du jour, catégories professionnelles uniquement (hors Geekerie)]

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

## Geekerie
### [Titre court et factuel]
[2 à 3 phrases : ce qui est sorti ou annoncé, statut, date, prix si connu.]
**Pourquoi c'est intéressant :** [ce que ça change ou permet, une phrase.]
Source : [Nom du site, JJ/MM/AAAA](URL)

## Échéances à surveiller
- [JJ/MM/AAAA] : [échéance] ([source](URL))
```

Frontmatter : remplir `fenetre_debut` et `fenetre_fin` en Europe/Paris, `elements` avec le nombre d'éléments retenus, et `categories_avec_actualite` avec le nombre de rubriques autres que « Rien de notable ». Ne pas ajouter d'autres champs.

Style : concis, professionnel, sans remplissage ni formule d'introduction. Une catégorie sans actualité confirmée affiche « Rien de notable dans la fenêtre. » plutôt que d'être complétée avec des éléments faibles, non confirmés ou hors période. La rubrique « Échéances à surveiller » est omise si aucune échéance n'a été trouvée.

## Étape 5 : Enregistrer dans Obsidian

Cible : **`Mon Drive/ObsidianVault/MonVault/Veille/AAAA-MM-JJ veille informatique.md`**, où `AAAA-MM-JJ` est la date du jour de lancement (exemple : `2026-11-21 veille informatique.md` ; chemin local : `G:\Mon Drive\ObsidianVault\MonVault\Veille\2026-11-21 veille informatique.md`). Le dossier `Veille` est à la racine du coffre MonVault, avec une majuscule initiale. Ne jamais écrire dans le coffre de `pro-agenda`, `pro-1to1` ou `pro-point-avancement`.

1. Si les outils du dossier connecté de l'ordinateur sont disponibles et que `G:\Mon Drive\ObsidianVault\MonVault` y est accessible, écrire le fichier directement dans `MonVault\Veille` (créer ce dossier s'il n'existe pas), avec de vrais retours à la ligne, puis relire le fichier pour vérifier qu'il comporte plusieurs lignes. Sinon, passer par Google Drive.
2. Via Google Drive : retrouver le dossier `MonVault` et **vérifier la chaîne complète des parents** : `MonVault → ObsidianVault → Mon Drive`. Ne jamais écrire dans un autre coffre ni dans une copie homonyme. Si la chaîne est introuvable ou ambiguë, s'arrêter et demander le lien du dossier.
3. Dans ce `MonVault` vérifié, chercher le sous-dossier `Veille` directement à la racine du coffre. S'il n'existe pas, le créer (`create_file`, type `application/vnd.google-apps.folder`) avec `MonVault` comme parent explicite. Ne jamais créer un second dossier de même nom à une autre casse (`veille`, `VEILLE`).
4. Créer le fichier du jour (`create_file`) avec `Veille` comme parent explicite. Si un fichier portant **la même date** existe déjà (veille relancée le même jour), mettre l'ancien à la corbeille (`trash_file`) avant de créer le nouveau, et le signaler dans la réponse finale. Ne jamais créer de doublon (`… (1).md`) et ne jamais toucher aux fichiers d'autres dates.
5. Enregistrer un vrai fichier texte UTF-8 `.md` (`contentMimeType` `text/markdown`, `disableConversionToGoogleType` à vrai), **sans conversion en Google Doc**, pour qu'il reste lisible dans Obsidian. Le contenu est exactement la veille de l'étape 4, frontmatter compris, **sur plusieurs lignes** : un vrai saut de ligne après chaque titre, paragraphe, ligne « Pour NEOMA » ou « Pourquoi c'est intéressant », ligne « Source » et élément de liste, et une ligne vide entre les blocs. Un fichier dont tout le texte tient sur une seule ligne est un échec.
   - Méthode à privilégier : écrire d'abord la veille dans un fichier local temporaire (outil Write, avec de vrais retours à la ligne), puis l'envoyer avec `base64Content` sous forme de référence de fichier `sha256:<empreinte>:<chemin absolu>` (empreinte calculée avec `sha256sum`), ce qui transmet les octets tels quels.
   - À défaut, passer le texte dans `textContent` avec de vrais retours à la ligne dans la valeur. Ne jamais y mettre les deux caractères littéraux `\n`, ni `<br>`, ni concaténer les lignes avec des espaces.
6. Relire le fichier enregistré : métadonnées (nom, parent, type) **et contenu** (`download_file_content` ou `read_file_content`). Vérifier que le contenu comporte bien plusieurs lignes (frontmatter encadré par deux lignes `---`, titre `#` seul sur sa ligne, sections `##` en début de ligne) et ne contient pas de `\n` littéral. Sinon, mettre le fichier à la corbeille et le recréer avec la méthode par référence de fichier ; si le défaut persiste, le signaler dans le bilan. Ne pas affirmer que la synchronisation locale Obsidian est terminée.

Si l'écriture est impossible, livrer la veille complète dans le chat et expliquer ce qui a bloqué.

## Étape 6 : Réponse finale

Livrer dans le chat un court bilan : le nom et l'emplacement du fichier (lien Drive si disponible) et les points de la rubrique « À retenir », une ligne chacun. Ne pas recopier toute la veille sauf si l'écriture a échoué. Si l'outil SendUserMessage est disponible, y envoyer ce même bilan. Ne pas l'envoyer par e-mail ni sur Teams.
