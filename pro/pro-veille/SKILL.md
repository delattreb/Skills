---
name: "pro-veille"
description: "Rédige en français une veille quotidienne (dernières 24 h, 72 h le lundi) classée en six catégories : politique générale (France et international), économie, IA, informatique, développement, 3D. Lit d'abord des flux RSS (config/flux.json, flux inaccessibles désactivés), complète par la recherche web sur des sites d'information accessibles, ne retient que des informations confirmées, chacune datée et sourcée par un lien, et l'enregistre dans Obsidian (coffre MonVault, dossier Veille, un fichier par jour : AAAA-MM-JJ veille.md). Remplace pro-veille-informatique et perso-information. À utiliser quand l'utilisateur demande « veille », « veille du jour », « fais ma veille », « veille informatique », « actualités », « infos du jour », « point info », « actus IA », « actus dev », « actus Blender / 3D », « /pro-veille »."
tags: [pro, veille, actualites, politique, economie, ia, informatique, developpement, 3d]
metadata:
  version: "1.0.0"
---

## Approach

- Read existing files before writing. Don't re-read unless changed.
- Thorough in reasoning, concise in output.
- Skip files over 100KB unless required.
- No sycophantic openers or closing fluff.
- No emojis or em-dashes.
- Do not guess APIs, versions, flags, commit SHAs, or package names. Verify by reading code or docs before asserting.

# Veille quotidienne

Produire chaque jour une veille factuelle, en français, sur l'actualité publiée dans la fenêtre de l'étape 1, classée en six catégories : **Politique** (France et international), **Économie**, **IA**, **Informatique** (dont cybersécurité), **Développement**, **3D** (Blender, moteurs, impression 3D, maker). Elle ne donne ni avis ni commentaire politique : elle décrit ce qui s'est passé, qui l'a dit, quelle est la portée, et ce qui reste incertain.

## Règles impératives

- **Sources web uniquement.** Ne consulter ni la messagerie, ni l'agenda, ni Teams. Ordre de collecte : flux RSS (script), puis recherche web sur des sites d'information accessibles, puis lecture d'une page pour vérifier un article.
- **Sites accessibles uniquement.** Ne jamais contourner un paywall, une connexion obligatoire, un CAPTCHA ni une interdiction d'accès. Une page illisible n'est pas lue ; un flux inaccessible est désactivé (étape 0). Un titre et un résumé de flux, ou un résultat de recherche daté avec son URL, valent lecture de l'élément.
- **Une seule écriture par lancement : le fichier horodaté** `AAAA-MM-JJ veille.md` (date du jour de lancement) dans `MonVault/Veille`. Les veilles des jours précédents ne sont jamais modifiées.
- **Confirmation selon la catégorie.**
  - *Politique et Économie* : fait confirmé par **deux médias reconnus indépendants** ou par **une source officielle** (gouvernement, Journal officiel, institution internationale, BCE, banque centrale, organisme public, communiqué de l'entité concernée). Une dépêche d'agence (AFP, Reuters, AP) reprise ailleurs compte pour l'agence, à condition que le texte la cite ; une agence ne vaut pas deux médias à elle seule. Un fait à **source unique** (un seul média reconnu) peut figurer dans sa catégorie, jamais dans « À retenir », et il est marqué « source unique » avec attribution (« selon Euronews »).
  - *IA, Informatique, Développement, 3D* : une **source primaire** (éditeur, projet, organisme officiel) ou **un média reconnu** suffit.
  - Agrégateurs, digests automatiques, blogs anonymes, forums et réseaux sociaux sont **exclus** comme preuve ; ils servent seulement de piste pour trouver la source primaire. Pas de rubrique « à confirmer ».
- **Ne rien inventer.** Chaque élément a au moins un lien et une date. Uniquement des URL issues du script, de la recherche ou d'une page ouverte, jamais reconstruites de mémoire.
- **Neutralité.** Sujets disputés (politique, conflits, élections, débats de société) : présenter les positions en les attribuant, sans adjectif évaluatif ni conclusion. Signaler un fait en cours d'établissement (« selon les premières informations »).
- **Période stricte.** Ne retenir que des informations publiées entre début et fin de période. Un fait plus ancien n'entre que s'il y a un fait nouveau daté dans la période, signalé par « (suite) ».
- **Statut explicite** pour la tech : « (annonce) », « (préversion) » ou « (déployé) » quand il n'est pas évident.
- **Une seule catégorie par élément.** Un même fait n'apparaît qu'une fois, dans la catégorie la plus utile.
- **Recherche et flux indisponibles.** Si le script échoue entièrement et qu'aucun outil de recherche web n'est disponible, s'arrêter et l'indiquer en une ligne. Ne pas produire de veille de mémoire.

## Étape 0 : Tester les flux (à la demande)

Seulement si l'utilisateur demande de tester ou de mettre à jour les sources, ou si plusieurs flux sont en erreur au lancement : `python3 -I scripts/flux.py --tester --ecrire` depuis le dossier du skill. Le script vérifie chaque flux actif et passe à `"actif": false`, avec une `note`, ceux qui sont inaccessibles. Pour ajouter une source : une entrée dans `config/flux.json` (`nom`, `categorie` parmi `politique`, `economie`, `ia`, `informatique`, `developpement`, `3d`, `url`, `actif`), puis `--tester --ecrire`. Ne jamais réactiver à la main un flux en échec sans l'avoir retesté.

## Étape 1 : Préparer

1. Charger l'outil de recherche web via ToolSearch si nécessaire (par exemple `select:WebSearch`). Invoquer ensuite le skill `caveman:caveman` (outil Skill) : il règle le style des messages de travail et du bilan final dans le chat, jamais celui de la note enregistrée.
2. Calculer la fenêtre (fuseau Europe/Paris), **fin = moment du lancement** :
   - mardi à samedi : les 24 dernières heures ;
   - lundi : depuis vendredi matin (72 h) ;
   - lancement manuel : depuis la date de la dernière veille de `MonVault/Veille` (7 jours au maximum) ; sans veille précédente, 24 h.
   Noter la date du jour `AAAA-MM-JJ` pour le nom du fichier.
3. Lire la veille précédente (le fichier `AAAA-MM-JJ veille.md` le plus récent de `MonVault/Veille`, s'il existe) pour ne pas reprendre un sujet déjà traité, sauf fait nouveau (« (suite) »). Les anciens fichiers `… veille informatique.md` et `… information.md` comptent aussi comme veilles précédentes.

## Étape 2 : Collecter

1. **Flux RSS** : `python3 -I scripts/flux.py --debut <début ISO avec fuseau> --fin <fin ISO avec fuseau>` depuis le dossier du skill. Sortie groupée par catégorie, 3 entrées les plus récentes par flux (`--par-flux N` pour changer, `--resume` pour ajouter le résumé, `--categorie ia` pour une seule catégorie). Les erreurs de flux vont sur la sortie d'erreur : les signaler dans le bilan, continuer. Les flux généralistes (Le Monde, Le Figaro, etc.) mélangent sport, culture et faits divers : ne retenir que ce qui relève des six catégories.
2. **Recherche web** pour les catégories vides ou maigres et pour la **double confirmation** des faits politiques et économiques retenus : une ou deux requêtes par catégorie, avec le mois et l'année, en français et en anglais (requêtes de départ dans `references/recherche.md`). Lancer les recherches indépendantes en parallèle. Un domaine refusé par l'outil de recherche (erreur 400 « not accessible to our user agent ») est retiré de la requête, la requête est relancée sans filtre, et le domaine est signalé dans le bilan.
3. **Lecture d'un article** quand c'est nécessaire pour vérifier la date, le fond ou le statut. Si la lecture directe échoue (blocage anti-robot, rendu JavaScript), une page **publique** peut être lue avec le skill `apify:apify-ultimate-scraper` (Actor `apify/rag-web-browser`, schéma d'entrée récupéré avec `apify actors info "apify/rag-web-browser" --input --json` avant l'appel), 5 pages au plus par lancement. Page toujours illisible, CLI absente ou non authentifiée : ne pas insister, appliquer la règle « titre et résumé de flux ou résultat de recherche daté ».

## Étape 3 : Trier

- Écarter : faits non confirmés selon la catégorie, doublons (garder une entrée, source officielle ou primaire en premier), éditoriaux sans fait nouveau, contenu promotionnel ou sponsorisé, tutoriels, fait divers et sport hors sujet, articles hors période.
- Évaluer l'**importance** : personnes touchées, portée juridique, économique ou technique, effet durable, caractère inédit. Garder au plus **5 éléments** pour Politique et Économie, **3** pour IA, Informatique, Développement et 3D, du plus au moins important. Un jour calme donne une note courte : ne pas combler avec des éléments faibles.
- Indices tech : nouvelle version majeure ou nouveau modèle, vulnérabilité activement exploitée, changement de prix ou de licence, fin de support, projet remarquable publié par un média reconnu ; une bêta mineure ou un correctif sans nouveauté est écarté.
- Repérer les **échéances** officielles ou datées dans les semaines à venir (entrée en vigueur d'un texte, élection, sommet, décision attendue, fin de support, date de sortie).

## Étape 4 : Rédiger

Le champ `tags` du frontmatter contient toujours `veille`, puis un tag par catégorie qui a au moins un élément, dans l'ordre du format : `politique`, `economie`, `ia`, `informatique`, `developpement`, `3d`. Tags en minuscules, sans espace ni accent.

Respecter exactement ce format. Les six catégories suivent toujours cet ordre.

```
---
date: AAAA-MM-JJ
type: veille
fenetre_debut: AAAA-MM-JJ HH:MM
fenetre_fin: AAAA-MM-JJ HH:MM
categories_avec_actualite: N
elements: N
tags: [veille, ...]
---

# Veille du [jour JJ mois AAAA]

> [!summary] À retenir
> - [3 points maximum, une ligne chacun, tous sujets confondus, jamais un fait à source unique]

## Vue d'ensemble

| Catégorie | Éléments |
|---|---|
| Politique | N |
| Économie | N |
| IA | N |
| Informatique | N |
| Développement | N |
| 3D | N |

---

## [Catégorie (N) : seulement celles ayant au moins un élément, dans l'ordre fixe ci-dessus]

> [!info] [Titre court et factuel]
> [2 à 3 phrases : ce qui s'est passé, qui est concerné, date, statut ou incertitude.]
>
> Sources : [Nom du média, JJ/MM/AAAA](URL), [Nom du média, JJ/MM/AAAA](URL)

---

## Échéances à surveiller
- [JJ/MM/AAAA] : [échéance] ([source](URL))
```

Règles de présentation :
- Le tableau liste les six catégories, y compris celles à 0, qui n'ont alors aucune section dans le corps.
- Pour une source officielle ou primaire seule : « Source officielle : [Nom, JJ/MM/AAAA](URL) ». Pour un fait à source unique : « Source unique : [Nom, JJ/MM/AAAA](URL) ».
- Callout `[!info]` par défaut, `[!warning]` pour un fait de portée majeure (vulnérabilité activement exploitée, décision de loi ou de budget, crise).
- La section « Échéances à surveiller » est omise si rien n'a été trouvé.
- Si aucun élément n'est retenu, le corps se réduit à « Rien de notable dans la fenêtre. » sous « À retenir ».
- Frontmatter : `fenetre_debut` et `fenetre_fin` en Europe/Paris, `elements` = éléments retenus, `categories_avec_actualite` = catégories avec au moins un élément. Aucun autre champ.

Style : concis, factuel, sans remplissage, sans formule d'introduction, sans adjectif évaluatif.

## Étape 5 : Enregistrer dans Obsidian

Cible : **`Mon Drive/ObsidianVault/MonVault/Veille/AAAA-MM-JJ veille.md`** (chemin local : `G:\Mon Drive\ObsidianVault\MonVault\Veille\2026-11-24 veille.md`). `Veille` est à la racine du coffre, avec une majuscule. Ne jamais écrire ailleurs dans le coffre (`Information`, `Dessin`, `Cuisine`, etc.) ni dans le coffre d'un autre skill, ni dans une copie homonyme de MonVault.

Repères Drive, à revalider par lecture des métadonnées et des parents avant chaque écriture : ObsidianVault `1Q3dr6rASJAsU_wtcZHiKROWukoyLr5Mf`, MonVault `1zZRUuQVhlIg_Vvnt0m0BqOq2Q5nnCsQV`. Chaîne à vérifier : `Veille → MonVault → ObsidianVault → Mon Drive`.

1. **Accès local d'abord.** Si `G:\Mon Drive\ObsidianVault\MonVault` est accessible, écrire directement dans `MonVault\Veille` (le créer s'il manque), avec de vrais retours à la ligne, puis relire le fichier pour vérifier qu'il comporte plusieurs lignes.
2. **Sinon, Google Drive.** Vérifier la chaîne complète des parents. Chaîne introuvable ou ambiguë : s'arrêter et demander le lien du dossier. Chercher `Veille` directement sous MonVault, le créer sinon (`create_file`, type `application/vnd.google-apps.folder`, MonVault comme parent explicite), jamais un second dossier à une autre casse.
3. Si un fichier de **la même date** existe déjà (veille relancée), le mettre à la corbeille (`trash_file`) avant de créer le nouveau, et le signaler. Jamais de doublon `… (1).md`, jamais de modification des fichiers d'autres dates.
4. Créer un vrai fichier texte UTF-8 `.md` (`contentMimeType` `text/markdown`, `disableConversionToGoogleType` à vrai), **sans conversion en Google Doc**, contenu exact de l'étape 4 sur plusieurs lignes. Méthode préférée : écrire d'abord un fichier local temporaire (outil Write), puis l'envoyer avec `base64Content` sous forme de référence `sha256:<empreinte>:<chemin absolu>`. À défaut, `textContent` avec de vrais retours à la ligne, jamais le texte littéral `\n` ni `<br>`.
5. Relire le fichier enregistré (nom, parent, type, contenu) : frontmatter encadré par deux lignes `---`, titre `#` seul sur sa ligne, sections `##` en début de ligne, aucun `\n` littéral. Sinon corbeille et recréation ; si le défaut persiste, le signaler. Ne pas affirmer que la synchronisation Obsidian est terminée.

Si l'écriture est impossible, livrer la veille complète dans le chat et expliquer ce qui a bloqué.

## Étape 6 : Réponse finale

Court bilan, dans le style `caveman:caveman` : nom et emplacement du fichier (lien Drive si disponible), points de « À retenir » (une ligne chacun), flux en erreur ou domaines retirés. Ne pas recopier la veille sauf si l'écriture a échoué. Si l'outil SendUserMessage est disponible (notamment en exécution planifiée), y envoyer ce même bilan. Ne pas l'envoyer par e-mail ni sur Teams.

## Exécution planifiée

Personne ne répond aux questions dans ce mode : ne rien demander, appliquer les règles, et signaler dans le bilan tout ce qui a bloqué (flux en erreur, dossier introuvable, écriture impossible).
