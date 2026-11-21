# Changelog — pro-veille-informatique

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Chaque version publiée est marquée par un tag Git `pro-veille-informatique-vX.Y.Z`.

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
