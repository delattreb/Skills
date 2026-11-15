# Schéma version 1

Fichier UTF-8 Markdown avec frontmatter YAML. Le modèle contient des variables à remplacer : ce n'est pas une recette prête à publier.

- `type`: recette ; `schema_version`: entier 1.
- `id`: UUID stable sous forme de chaîne ; ne jamais réattribuer un identifiant existant.
- `titre`: chaîne non vide ; nom du fichier compatible Windows, sans renommer une fiche existante sans nécessité.
- `categorie`: Plat ou Dessert, ou null si indéterminée. Vérifier les propriétés des Bases actuelles avant de changer un classement existant ; demander si une nouvelle catégorie est nécessaire.
- `portions`: nombre positif ou null.
- `preparation_min`, `cuisson_min`, `repos_min`: entiers positifs ou nuls, ou null si inconnus. Zéro signifie une absence confirmée.
- `difficulte`: Facile, Moyenne, Difficile ou null ; ne pas inventer une évaluation attribuée à la source.
- `statut`: brouillon ou complete. Complete exige une image durable et des informations suffisantes pour réaliser la recette ; ne signifie pas testée en cuisine.
- `sources`: liste de chaînes (URL, livre et page, document, ou provenance utilisateur).
- `image`: chemin relatif à la racine du coffre vers un fichier image réel ; null seulement pour un brouillon incomplet.
- `image_type`: generee. Lors d'une reprise, préserver la provenance réelle d'une ancienne photo ; ne jamais la réétiqueter comme générée.
- `tags`: liste de chaînes comprenant recette.
- `date_creation`, `date_modification`: chaînes YYYY-MM-DD, selon la date locale utilisateur ; préserver la création existante.
- `skill_version`: chaîne 0.1.4 pour cette version.

Préserver les champs additionnels et les notes de l'utilisateur. L'image est aussi intégrée dans le corps par un lien Obsidian `![[chemin/relatif.png]]`.

## Présentation obligatoire

La section Ingrédients contient un tableau Markdown à quatre colonnes : Ingrédient, Quantité, Unité, Précision. Une ligne par ingrédient ; ne jamais substituer une liste. Cette règle vaut aussi pour les brouillons. Conserver les autres tableaux et annotations existants.
