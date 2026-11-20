# Accès et synchronisation

## Découvrir l'environnement

Coffre cible : `Mon Drive/ObsidianVault/MonVault` (chemin local indicatif : `G:/Mon Drive/ObsidianVault/MonVault`). Recettes : `Cuisine/Recette` ; illustrations : `Attachment` ; vue existante : `Base/BDDCuisine.base`.

### Identifier le bon coffre

Ne jamais choisir le premier dossier homonyme. La copie `Mon Drive/Dessin/MonVault` n’est pas le coffre cible et ne doit pas recevoir les recettes.

Repères Drive vérifiés le 10 novembre 2026, à revalider par lecture des métadonnées et des parents avant chaque écriture :

| Dossier | Identifiant Drive |
|---|---|
| ObsidianVault | `1Q3dr6rASJAsU_wtcZHiKROWukoyLr5Mf` |
| MonVault | `1zZRUuQVhlIg_Vvnt0m0BqOq2Q5nnCsQV` |
| Cuisine | `1tzGKUAxX-FjfUcZVOiJsGUxcsjqDUY4O` |
| Recette | `1o30lVGy6BOe3fZRiQuaJnM1OAJIwfWWn` |
| Attachment | `1rxnWt_HvFUp7NPorRdgdWWSRwUFTrizg` |

Vérifier les relations : `Recette → Cuisine → MonVault → ObsidianVault → Mon Drive` et `Attachment → MonVault`. En accès local, vérifier le chemin absolu réel. Si ces repères deviennent invalides, retrouver la chaîne complète ; ne pas basculer vers une copie homonyme. Si plusieurs cibles restent indiscernables, demander le chemin ou le lien du coffre avant toute écriture.

Chercher les doublons dans le dossier cible vérifié. Une recherche globale peut révéler une fiche dans un autre coffre : ne pas la déclarer présente dans les recettes du coffre cible. Pour corriger une fiche mal rangée à la demande de l’utilisateur, vérifier les parents source et destination, préserver son identifiant et ses annotations, déplacer aussi son image si nécessaire, puis contrôler les parents et les liens après déplacement.

Dans Codex, utiliser les outils locaux autorisés si le coffre est accessible. Dans ChatGPT, utiliser un connecteur capable de lire et écrire de véritables fichiers Markdown et leurs images ; un Google Doc n'est pas un substitut à un fichier `.md`. Sans capacité d'écriture, livrer Markdown et image à importer. Ne jamais annoncer un enregistrement sur la seule base de la génération d'un fichier temporaire.

## Écrire sans écraser une modification récente

1. Lire le fichier cible et retenir son empreinte ou sa révision ; pour une création, vérifier que la cible n'existe pas.
2. Préparer note et image hors de la version finale. Conserver une copie récupérable du fichier existant avant remplacement.
3. Relire la révision avant écriture. Si elle a changé, comparer et intégrer les changements ou présenter le conflit ; ne pas écraser.
4. En accès local, utiliser un remplacement atomique lorsque possible. En accès distant, employer une précondition de révision si le service en offre une.
5. Enregistrer l'image avant la note qui la référence. Relire note et image, vérifier les liens et les propriétés ainsi que leur appartenance au coffre cible par les parents Drive ou les chemins absolus. Un succès d’envoi ne prouve pas le bon classement. Ne pas affirmer que la synchronisation locale Obsidian est terminée sans l’avoir observée.

Une simple relecture suivie d'une écriture n'empêche pas une course concurrente. Sans précondition fiable, ne pas prétendre garantir l'absence de conflit ; éviter les modifications simultanées et remettre une proposition séparée si un autre éditeur travaille sur la fiche. Drive synchronise les fichiers mais n'assure pas une transaction commune avec l'accès local.

## Versions du Skill

GitHub sera la source du Skill seulement après création ou publication autorisée du dépôt. Distribuer le même paquet versionné aux deux environnements ; pas de mise à jour automatique supposée depuis GitHub. Une mise à jour du Skill ne migre pas les recettes. Ne pas éditer un dépôt ni publier sur la seule instruction de créer une recette.

## Reprise après erreur

L'instruction de créer une recette autorise son enregistrement dans les dossiers ci-dessus. Découvrir les capacités du connecteur avant de conclure que Drive est inaccessible ; un coffre local absent dans Codex n'empêche pas l'utilisation du connecteur Drive disponible. Ne pas inventer de commande ni de capacité d'envoi d'images.

Pour Drive, créer un vrai fichier UTF-8 `.md` avec le dossier Recette vérifié comme parent explicite ; le nom seul ne classe pas le fichier. Envoyer l'image binaire dans Attachment si l'outil permet d'accéder à ses octets, puis vérifier son parent et sa disponibilité. Une image affichée dans ChatGPT ou enregistrée dans sa bibliothèque n'est pas automatiquement copiée dans Drive. Si les octets ne sont pas accessibles, enregistrer la note en brouillon sans lien cassé.

Après un délai dépassé ou une réponse incertaine, rechercher et relire la cible par parent, titre et source avant toute nouvelle création. Réutiliser une note déjà créée et son UUID ; ne pas ajouter un doublon à chaque tentative. Vérifier la note même si l'image échoue. Rapporter séparément : note enregistrée, image enregistrée, état brouillon ou complet, blocage restant.

## Transfert d'une illustration générée vers Drive

Parcours vérifié le 11 novembre 2026 sur une création réelle : image PNG et note Markdown envoyées avec le connecteur Drive, puis parents et contenu relus. Adapter les appels aux signatures réellement disponibles.

1. Conserver le résultat de génération sans imprimer son contenu binaire. Si l'outil fournit un chemin local, utiliser ce fichier. Si le résultat contient une URL de données `data:image/png;base64,...`, décoder la partie après la virgule vers un vrai PNG dans le dossier temporaire autorisé. Cette matérialisation sert à intégrer l'image au coffre ; elle n'est pas nécessaire pour simplement afficher l'image dans ChatGPT. Ne pas chercher une image homonyme dans la bibliothèque.
2. Avec `google_drive_upload_file`, envoyer le chemin local absolu dans `file_uri`, avec `file_name` explicite, `mime_type: image/png` et `parent_folder_id` égal à l'identifiant Attachment vérifié. Ne jamais envoyer le texte base64 comme si c'était le PNG.
3. Relire les métadonnées de l'image créée : parent Attachment attendu, type image/png et taille non nulle. Conserver son identifiant pour les reprises.
4. Renseigner la note avec le chemin relatif `Attachment/<nom>.png`, son intégration Obsidian et la mention d'illustration générée. Reprendre les propriétés observées dans les fiches actuelles, notamment `title`, `couverture: "[[Attachment/<nom>.png]]"` et le tag `cuisine/recette` si utilisés par la collection.
5. Envoyer le vrai fichier UTF-8 Markdown avec `file_uri`, `mime_type: text/markdown` et le parent Recette vérifié. Relire sa teneur et son parent. Passer à `statut: complete` seulement si les conditions du schéma sont remplies.

En cas d'échec d'envoi ou de résultat incertain, appliquer la reprise sans doublon ci-dessus. Ne pas régénérer une image déjà disponible uniquement parce que son transfert doit être repris. L'enregistrement Drive ne prouve pas la fin de la synchronisation sur le PC.
