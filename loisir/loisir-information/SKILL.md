---
name: "loisir-information"
description: "Rédige en français un point d'information quotidien (dernières 48 h, 72 h le lundi) sur deux volets : l'actualité internationale importante et l'actualité française importante. S'appuie uniquement sur des recherches web, ne retient que des informations confirmées par au moins deux médias reconnus ou par une source officielle, chacune datée et sourcée par un lien, et l'enregistre dans Obsidian (coffre MonVault, dossier information, un fichier horodaté par jour). À utiliser quand l'utilisateur demande « actualités », « infos du jour », « qu'est-ce qui s'est passé », « point info », « /loisir-information », « actu internationale », « actu France », « résumé de l'actu » ou lance le point d'information planifié."
metadata:
  version: "0.4.0"
---

## Approach

- Read existing files before writing. Don't re-read unless changed.
- Thorough in reasoning, concise in output.
- Skip files over 100KB unless required.
- No sycophantic openers or closing fluff.
- No emojis or em-dashes.
- Do not guess APIs, versions, flags, commit SHAs, or package names. Verify by reading code or docs before asserting.

# Point d'information quotidien

Produire chaque jour un point factuel, en français, sur l'actualité publiée depuis la fenêtre de l'étape 1, en deux volets : **international** et **France**. Le point ne donne ni avis ni commentaire politique : il décrit ce qui s'est passé, qui l'a dit, quelle est la portée, et ce qui reste incertain.

## Règles impératives

- **Sources web uniquement.** Utiliser l'outil de recherche web disponible (WebSearch ou équivalent) et, si besoin, la lecture de page pour vérifier un article. Ne consulter ni la messagerie, ni l'agenda, ni Teams.
- **Une seule écriture par lancement : le fichier horodaté** `AAAA-MM-JJ information.md` (date du jour de lancement) dans `MonVault/Information` (étape 5). Les points des jours précédents ne sont jamais modifiés.
- **Informations confirmées uniquement.** Un fait entre dans le point s'il est confirmé soit par **deux médias reconnus indépendants** (sources actives de `config/sources.json`), soit par **une source officielle** (gouvernement, Journal officiel, institution internationale, organisme public, communiqué de l'entité concernée). Une dépêche d'agence (AFP, Reuters, Associated Press) reprise sur un autre site compte pour l'agence, à condition que le texte la cite nommément ; une dépêche d'agence ne compte pas pour deux médias à elle seule : il faut un second média reconnu indépendant, ou la reprise de l'agence sur deux sites distincts, qui la citent nommément (voir `confirmation.agences_reprises` dans le fichier de configuration). Un fait repris seulement par un agrégateur, un blog anonyme, une page générée automatiquement ou un réseau social est **exclu**, même s'il paraît important. Il n'y a pas de rubrique « à confirmer ».
- **Ne rien inventer.** Chaque élément a au moins un lien et une date de publication. Uniquement des URL renvoyées par la recherche ou ouvertes ; jamais de lien reconstruit de mémoire.
- **Neutralité.** Pour les sujets disputés (politique, conflits, élections, débats de société), présenter les positions des acteurs concernés en les attribuant, sans adjectif évaluatif ni conclusion. Indiquer quand un fait est encore en cours d'établissement (« selon les premières informations », « non confirmé par les autorités à cette heure »).
- **Période stricte.** Ne retenir que des informations publiées entre début et fin de période (étape 1). Un événement plus ancien n'entre que si un fait nouveau est publié dans la période, et ce fait nouveau est alors daté.
- **Une seule rubrique par élément.** Un même fait n'apparaît qu'une fois.
- **Recherche web indisponible.** Si aucun outil de recherche web n'est disponible ou qu'il échoue, s'arrêter et l'indiquer en une ligne. Ne pas produire de point de mémoire.

## Étape 1 : Préparer

1. Charger l'outil de recherche web via ToolSearch si nécessaire (par exemple `select:WebSearch`).
2. Calculer la fenêtre (fuseau Europe/Paris), **fin = moment du lancement** :
   - mardi à vendredi : les 48 dernières heures ;
   - lundi : depuis vendredi matin (72 h), pour couvrir le week-end ;
   - lancement manuel : depuis la date du dernier point présent dans `MonVault/Information` (7 jours au maximum) ; sans point précédent, 48 h.
   Noter la date du jour au format `AAAA-MM-JJ`.
3. Lire le point précédent (le fichier `AAAA-MM-JJ information.md` le plus récent de `MonVault/Information`, s'il existe) pour ne pas reprendre un sujet déjà traité, sauf fait nouveau, signalé alors par « (suite) ».
4. Lire `config/sources.json` : sources actives (médias et officielles), seuil de confirmation et volet de chaque source. Ne jamais utiliser une source `actif: false`. Lire `references/sources.md` pour les requêtes de départ et les critères d'importance.

## Étape 2 : Collecter (lancer les recherches indépendantes en parallèle)

Lancer plusieurs requêtes par volet, en français et en anglais, avec le mois et l'année en cours :

1. **International** : événements politiques et diplomatiques majeurs, conflits, économie et marchés, décisions des grandes institutions (ONU, UE, G7, G20, banques centrales), catastrophes naturelles, sciences et santé publique à portée mondiale.
2. **France** : décisions du gouvernement et du Parlement (textes publiés au Journal officiel), actualité politique et sociale majeure, économie et emploi, justice, grands événements, sécurité et santé publique, décisions de la Banque de France et des grandes autorités de régulation.
3. **Agenda et suivi** : échéances officielles des semaines à venir (Journal officiel, préfectures, gouvernement, sommets annoncés, calendrier électoral), et sujets ouverts du point précédent (rubrique « En cours »), à reprendre seulement s'il y a un fait nouveau.

Ouvrir les articles les plus importants pour vérifier la date, le fond et la confirmation. Pour chaque fait retenu, vérifier la règle de double confirmation (`confirmation.min_medias_independants`), de dépêche d'agence ou de source officielle ; sinon l'écarter. Un média dont le `volet` est `both` peut servir aux deux volets.

## Étape 3 : Trier

- Si aucun fait ne passe la règle de confirmation dans un volet, afficher « Rien de notable dans la fenêtre. » pour ce volet. Ne jamais compléter avec des résumés d'agrégateurs, des pistes non confirmées ou des remarques entre parenthèses non vérifiées. Si les deux volets sont vides, le point se limite au titre, à la fenêtre couverte et à une phrase : « Aucun fait confirmé dans la fenêtre. »
- Écarter les faits non confirmés selon la règle impérative, les doublons (garder une entrée, source officielle en premier), les éditoriaux et analyses sans fait nouveau, les contenus promotionnels, les faits hors période.
- Évaluer l'**importance** : nombre de personnes touchées, portée juridique ou économique, effet durable, caractère inédit. Garder au plus **5 éléments par volet**, du plus au moins important. Un jour calme donne un point court : ne pas combler avec des éléments faibles.
- Repérer les **échéances** (entrée en vigueur d'un texte, élection, sommet, date limite, publication attendue) dans les semaines à venir, si elles sont officielles.

## Étape 4 : Rédiger

Respecter exactement ce format :

```
# Point d'information du [jour JJ mois AAAA]

## À retenir
- [3 points maximum, une ligne chacun : le plus important du jour, tous volets confondus]

## International
### [Titre court et factuel]
[2 à 3 phrases : ce qui s'est passé, qui est concerné, date, statut si incertain.]
Sources : [Nom du média, JJ/MM/AAAA](URL), [Nom du média, JJ/MM/AAAA](URL)

## France
### [Titre court et factuel]
[2 à 3 phrases : ce qui s'est passé, qui est concerné, date, statut si incertain.]
Sources : [Nom du média, JJ/MM/AAAA](URL), [Nom du média, JJ/MM/AAAA](URL)

## En cours
### [Sujet suivi sur plusieurs jours]
[1 à 2 phrases : où en est le sujet, avec la date du dernier fait confirmé. Si rien de nouveau dans la fenêtre : « Pas de fait nouveau dans la fenêtre. », suivi de la date du dernier fait.]
Sources : [Nom du média, JJ/MM/AAAA](URL)

## Agenda officiel
- [JJ/MM/AAAA] : [échéance officielle, par exemple arrêté préfectoral, Conseil des ministres, publication au Journal officiel, sommet, calendrier électoral] ([source officielle](URL))
```

Pour une information officielle seule, écrire « Source officielle : [Nom, JJ/MM/AAAA](URL) » à la place de la double source. Une rubrique sans fait confirmé affiche « Rien de notable dans la fenêtre. ». La rubrique « En cours » est omise s'il n'y a aucun sujet suivi d'un jour à l'autre. La rubrique « Agenda officiel » est omise si aucune échéance officielle n'a été trouvée. En tête du point, si aucun fait n'est confirmé, une phrase résume le climat général à partir des seuls faits confirmés de la période, sans adjectif évaluatif.

Style : concis, factuel, sans remplissage ni formule d'introduction, sans adjectif évaluatif.

## Étape 5 : Enregistrer dans Obsidian

Coffre cible : **MonVault** (`Mon Drive/ObsidianVault/MonVault`, chemin local indicatif : `G:/Mon Drive/ObsidianVault/MonVault`). Dossier cible : **`Information`**, à la racine du coffre, avec une majuscule initiale. Fichier : **`AAAA-MM-JJ information.md`**, où la date est celle du jour de lancement (exemple : `2026-11-21 information.md`). Ne jamais écrire dans un autre dossier du coffre (`veille`, `Dessin`, `Cuisine`, etc.) ni dans une copie homonyme de MonVault (par exemple `Mon Drive/Dessin/MonVault`).

Repères Drive, à revalider par lecture des métadonnées et des parents avant chaque écriture :

| Dossier | Identifiant Drive |
|---|---|
| ObsidianVault | `1Q3dr6rASJAsU_wtcZHiKROWukoyLr5Mf` |
| MonVault | `1zZRUuQVhlIg_Vvnt0m0BqOq2Q5nnCsQV` |
| Information | à retrouver ou créer sous MonVault (pas encore connu) |

Chaîne à vérifier : `information → MonVault → ObsidianVault → Mon Drive`.

1. **Accès local d'abord.** Si l'ordinateur connecté est disponible et que le chemin réel `G:/Mon Drive/ObsidianVault/MonVault` est accessible, écrire directement dans `MonVault/Information` (le créer s'il n'existe pas). Vérifier le chemin absolu réel avant écriture.
2. **Sinon, connecteur Google Drive.** Vérifier la chaîne complète des parents à partir de l'identifiant MonVault ci-dessus. Si la chaîne est introuvable ou ambiguë, s'arrêter et demander le lien du dossier MonVault.
3. Chercher le sous-dossier `Information` directement sous MonVault. S'il n'existe pas, le créer (`create_file`, type `application/vnd.google-apps.folder`) avec MonVault comme parent explicite. Ne jamais créer un second dossier homonyme.
4. Vérifier qu'aucun fichier de la même date n'existe déjà dans `Information`. Si un point du même jour existe (point relancé), le mettre à la corbeille (`trash_file`) avant de créer le nouveau, et le signaler dans la réponse finale. Ne jamais créer de doublon (`… (1).md`) et ne jamais toucher aux fichiers d'autres dates.
5. Créer le fichier avec `Information` comme parent explicite : vrai fichier texte UTF-8 `.md` (`contentMimeType` `text/markdown`, `disableConversionToGoogleType` à vrai), **sans conversion en Google Doc**, pour qu'il reste lisible dans Obsidian. Le contenu est exactement le point de l'étape 4.
6. Relire le fichier enregistré : contenu, nom, parent, type. Ne pas affirmer que la synchronisation locale Obsidian est terminée sans l'avoir observée.

Si l'écriture est impossible, livrer le point complet dans le chat et expliquer ce qui a bloqué.

## Étape 6 : Réponse finale

Livrer dans le chat un court bilan : le nom et l'emplacement du fichier (lien Drive si disponible) et les points de la rubrique « À retenir », une ligne chacun. Ne pas recopier tout le point sauf si l'écriture a échoué. Si l'outil SendUserMessage est disponible (notamment en exécution planifiée), y envoyer ce même bilan.

## Exécution planifiée

Le point peut être lancé chaque jour par une tâche planifiée. Personne ne répond aux questions dans ce mode : ne rien demander, appliquer les règles, et signaler dans le bilan tout ce qui a bloqué (source inaccessible, dossier introuvable, écriture impossible).
