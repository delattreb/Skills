# Changelog — pro-veille-informatique

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Chaque version publiée est marquée par un tag Git `pro-veille-informatique-vX.Y.Z`.

## [Non publié]
### Ajouté
- Le skill invoque `caveman:caveman` à l'étape 1 pour le style des messages de travail et du bilan (jamais pour la note enregistrée) et `apify:apify-ultimate-scraper` avant la lecture renforcée.
- Passe 4 de l'étape 2 « Lecture renforcée (Apify) » : lecture des articles importants que la lecture directe n'ouvre pas, via le skill `apify:apify-ultimate-scraper` et l'Actor `apify/rag-web-browser`. Pages publiques et domaines acceptés seulement, 5 pages au plus par lancement, repli sur la confirmation par résultat de recherche si Apify est indisponible.
### Modifié
- Format de la note : tableau « Vue d'ensemble » des huit catégories, ordre fixe, callouts Obsidian colorés selon la pertinence, catégories sans élément absentes du corps.
- Frontmatter du skill : champ `tags` ajouté.
- Frontmatter YAML de la veille : le champ `tags` porte `veille`, `informatique` et un tag par catégorie qui a au moins un élément retenu (`ia`, `enseignement-superieur`, `microsoft-365`, `cybersecurite`, `reglementation`, `infrastructure`, `marche-editeurs`, `geekerie`), au lieu de la liste fixe `[veille, informatique]`.

## [0.6.0] — 2026-11-21
### Ajouté
- Sources testées avec le moteur de recherche (`allowed_domains`) et renvoyant des résultats datés : `cafepedagogique.net`, `cybermalveillance.gouv.fr`, `enisa.europa.eu`, `zataz.com`, `eur-lex.europa.eu`, `huggingface.co`, `forum.obsidian.md`, `blog.adafruit.com`, `skyandtelescope.org`. Ajoutées aux listes de domaines de leur catégorie ; `zataz.com`, `cafepedagogique.net` et `skyandtelescope.org` ajoutés aux médias reconnus.

### Modifié
- Version des métadonnées : 0.6.0.
- `obsidian.md` confirmé par le test et retiré des domaines non testés.

### Retiré
- Domaines non testés ou sans résultat : `supnumerique.gouv.fr`, `decision-atelier.com`, `blog.prusa3d.com`, `makezine.com`, `stellarium.org`, `siril.org`, `celestron.com`, `cieletespace.fr` (ces deux derniers restent cités comme sources de la sous-rubrique astronomie, mais ne sont pas dans les listes de recherche).

## [0.5.0] — 2026-11-21
### Ajouté
- Référence `references/contexte-neoma.md` : outils réellement utilisés à NEOMA, à compléter ; les sections « À compléter » ne sont pas utilisées. La ligne « Pour NEOMA » cite l'outil concerné quand il est renseigné.
- Geekerie : sous-rubrique astronomie amateur (instruments, Stellarium, Siril, KStars), domaines de recherche et indice de pertinence associés.
- IA et outils IA : suivi d'Obsidian (versions majeures, licence, synchronisation), domaine `obsidian.md`.
- Frontmatter YAML dans chaque veille : `date`, `type`, `fenetre_debut`, `fenetre_fin`, `categories_avec_actualite`, `elements`, `tags`.

### Modifié
- Dossier cible : `MonVault/Veille` (majuscule initiale), au lieu de `veille`.
- Deux requêtes web au maximum par catégorie, passes restreinte et libre comprises (une requête libre au plus pour une catégorie vide ou maigre).
- Domaines ajoutés sans test préalable (`obsidian.md`, `stellarium.org`, `siril.org`, `celestron.com`, `cieletespace.fr`) : signalés dans la référence, à vérifier au premier lancement.

### Supprimé
- Section « Exécution planifiée », mentions de planification dans la description, l'étape 1 (dimanche) et l'étape 6.

## [0.4.0] — 2026-11-21
### Modifié
- Collecte en trois passes : flux primaires lus par script, recherche web restreinte aux domaines fiables (`allowed_domains`), puis recherche libre en complément.
- Nouveau script `scripts/flux_veille.py` : feuille de route Microsoft 365 (RSS officiel) et catalogue CISA KEV, filtrés sur la fenêtre de la veille ; ces deux sources sont accessibles depuis l'environnement cloud.
- `references/sources-et-requetes.md` réécrit : listes de domaines testées par catégorie, ajout de sources accessibles et pertinentes (Next, JDN, Usine Digitale, IT for Business, Channelnews, Inside Higher Ed, EDUCAUSE, Times Higher Education, EdTech Magazine, VentureBeat, 9to5Google, The Hacker News, Help Net Security, Dark Reading, Neowin, Windows Central, Office 365 for IT Pros, CISA).
- Domaines refusés par le moteur de recherche (01net, ZDNet, Frandroid, Les Numériques, Numerama, Ars Technica, Reuters, The Verge, Le Monde, Les Échos) retirés des listes de recherche restreinte.
- Quand une page ne peut pas être ouverte, un résultat de recherche daté provenant d'un domaine accepté vaut confirmation.
- Fenêtre de 24 h étendue au samedi.

## [0.3.0] — 2026-11-21
### Corrigé
- Le fichier Obsidian ne doit plus contenir toute la veille sur une seule ligne : contenu multiligne exigé (vrais sauts de ligne, ligne vide entre les blocs, aucun `\n` littéral).
- Écriture via Google Drive : la veille est d'abord écrite dans un fichier local puis envoyée par référence de fichier (`base64Content` `sha256:<empreinte>:<chemin>`) ; `textContent` seulement à défaut, avec de vrais retours à la ligne.
- Relecture du contenu enregistré (et plus seulement des métadonnées) ; si le fichier tient sur une ligne, il est remplacé, et le défaut persistant est signalé dans le bilan.
- Version des métadonnées du skill alignée sur le changelog.

## [0.2.0] — 2026-11-21
### Modifié
- Veille quotidienne au lieu d'hebdomadaire : fenêtre des dernières 24 h (72 h le lundi, depuis la dernière veille pour un lancement manuel), 3 éléments au plus par catégorie, un fichier daté par jour.
- Lecture de la veille précédente pour ne pas reprendre un sujet déjà traité, sauf fait nouveau signalé « (suite) ».
- Section « Exécution planifiée » : aucune question en mode planifié, blocages signalés dans le bilan.
- Reprise de la PR concurrente (veille quotidienne dans NeomaVault) : sa fréquence et sa fenêtre sont intégrées ; son fichier `references/sources.md` est retiré, ses sources utiles rejoignent `references/sources-et-requetes.md`.

## [0.1.0] — 2026-11-21
### Ajouté
- Première version : veille informatique hebdomadaire en français (7 derniers jours) sur huit catégories : IA et outils IA, SI de l'enseignement supérieur, Microsoft 365 et cloud, cybersécurité, réglementation et données, infra réseau et poste de travail, marché et éditeurs, geekerie (digital painting, Raspberry Pi, Arduino, Blender, impression 3D, électronique DIY), cette dernière avec une ligne « Pourquoi c'est intéressant » et hors rubrique « À retenir ».
- Sources web uniquement ; seules les informations confirmées par une source primaire ou un média reconnu sont retenues, chacune datée et sourcée ; impact pour NEOMA et échéances à surveiller.
- Un fichier horodaté par lancement, `veille/AAAA-MM-JJ veille informatique.md`, dans Obsidian MonVault (Google Drive) ; dossier `veille` à la racine du coffre créé s'il n'existe pas ; historique des semaines précédentes conservé. Aucun impact sur les autres skills ni sur leur coffre.
- En-tête « Approach » (consignes de concision) pour limiter la consommation de tokens.
- Référence `references/sources-et-requetes.md` : sources acceptées et exclues, sources par catégorie, requêtes de départ et indices de pertinence.
