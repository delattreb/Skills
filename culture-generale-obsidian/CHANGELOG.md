# Changelog — culture-generale-obsidian

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Chaque version publiée est marquée par un tag Git `culture-generale-obsidian-vX.Y.Z`.

## [Non publié]
### Rationalisation
- Réécriture du SKILL.md en un seul fonctionnement : production hebdomadaire, structure de fiche conservée, programme annuel conservé dans 90_Regie.
- Suppression de l'annexe « copie de secours des consignes » du 14 novembre et de l'ancien texte quotidien : ils sont dans l'historique Git.
- Suppression des liens Drive vers le programme et la réserve privés : le dépôt est public. Seuls les IDs de dossiers et de notes restent.
- Un seul endroit par règle : programme, production, sources, données et révisions, vérification.

### Ajouté
- Section « Production hebdomadaire par lots » : tâche cloud unique, jusqu'à sept fiches chaque dimanche à 7 h (Europe/Paris) à partir du 15 novembre 2026 ; classement par lot du dimanche au samedi dans `Culture G/01_Fiches/` ; manifeste de lot et reprise sans doublon après interruption ; propriétés `lot` et `date_lecture_conseillee` ; note `00_Lire_cette_semaine.md` par lot ; page Aujourd'hui en vue hebdomadaire ; arrêt à 365 fiches.
- Les liens vers le programme et la réserve privés ne figurent pas dans la section ajoutée : le dépôt est public.
- Structure de la fiche : titre, mécanisme, ce qui permet de le vérifier, lire le visuel, vérification, connexions et sources, dans cet ordre.
- Section « Données, révisions et index » : propriété `date_decouverte` de type Date, champs `revision_N_faite`, rappels J+1/J+7/J+30, index, connexions, sources, journal et NotebookLM, repris de la règle de production quotidienne.
- Non repris de la production quotidienne : le rythme quotidien, les IDs `CG-NNNN`, le chemin Windows du coffre, le modèle de 600 à 800 mots avec quiz, qui entrent en conflit avec la structure de fiche et le lot hebdomadaire.

### Modifié
- Description du skill : mention du lot hebdomadaire.
- Publication : suppression de la règle « une publication par date civile » au profit de la règle anti-doublon et de la règle « pas de publication pendant une autre exécution ».
- Rappels J+1, J+7, J+30 : recalculés pendant le passage hebdomadaire et non plus quotidiennement.

### Inchangé
- Annexe « copie de secours des consignes » (14 novembre 2026), conservée telle quelle comme trace historique ; la section hebdomadaire prime sur elle.
