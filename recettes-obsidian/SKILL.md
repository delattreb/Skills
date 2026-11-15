---
name: recettes-obsidian
description: Créer, illustrer et modifier des recettes Markdown dans Obsidian à partir de textes, liens, photos ou documents, avec YAML, sources, adaptation des portions et contrôle des doublons.
---

# Recettes Obsidian

Version : 0.1.4. Format des fiches : 1.

Produire des recettes en français, complètes et illustrées, avec les mêmes conventions dans ChatGPT et Codex. Les instructions explicites de l'utilisateur priment sur ce Skill.

## Préparer

Lire [le schéma](references/schema-recette.md) et [les règles culinaires](references/regles-culinaires.md). Pour accéder au coffre ou enregistrer, lire [accès et synchronisation](references/acces-et-synchronisation.md).

Identifier les outils réellement disponibles : lecture et écriture de fichiers Markdown, génération d'images, stockage des illustrations. Ne pas supposer qu'un Skill donne accès au disque ou à Drive. Si l'accès manque, produire les fichiers importables et expliquer ce qui reste à enregistrer.

Avant toute recherche de doublon ou écriture, vérifier la chaîne complète des dossiers jusqu’à la racine du coffre selon la référence d’accès. Un dossier nommé `MonVault` ou `Recette` ne suffit pas à identifier le coffre. Vérifier que note et image appartiennent au même coffre cible.

Avant de créer, rechercher une recette par identifiant, titre et source. Avant de modifier, lire la fiche actuelle et préserver ses annotations et propriétés inconnues. Vérifier les conventions du coffre sur des exemples existants ; ne pas déplacer ni convertir toute une collection.

## Lire un lien fourni

Extraire la destination réelle d'un lien Markdown, même si son libellé ou sa ponctuation est échappé (par exemple `https\\://www\\.elle.fr`). Retirer uniquement les échappements de présentation ; conserver le domaine, le chemin et les paramètres utiles. Consulter la page et vérifier titre, ingrédients et préparation. Si un outil échoue, essayer un autre outil de lecture disponible. Si le contenu reste inaccessible, expliquer le blocage et demander le texte ; ne pas reconstruire la recette de mémoire.

## Rédiger

Utiliser [le modèle](assets/recette.md). Remplacer les variables, générer un UUID pour une nouvelle recette et garder cet identifiant lors des modifications. Extraire la source sans inventer de données. Signaler les informations manquantes dans la fiche. Distinguer les suggestions, variantes et adaptations du contenu d'origine.

Adapter les quantités uniquement sur demande : appliquer le rapport portions demandées / portions source aux quantités numériques pertinentes, conserver les unités et indiquer les arrondis. Ne pas multiplier automatiquement durées, températures ou dimensions du moule. Ne pas convertir masse et volume sans équivalence documentée.

## Formalisme obligatoire

Conserver le modèle et les conventions des fiches existantes à chaque création et modification. La section « Ingrédients » doit être un tableau Markdown avec exactement les colonnes « Ingrédient | Quantité | Unité | Précision », une ligne par ingrédient. Ne jamais remplacer ce tableau par une liste ou de la prose, même pour une recette courte ou un brouillon. Conserver les quantités inconnues vides avec une précision explicite ; échapper les barres verticales dans les cellules.
Garder le YAML, le titre, l’illustration, les étapes numérotées, les conseils et les sources. Préserver les tableaux supplémentaires et annotations d’une fiche existante. Tout changement de formalisme exige une demande explicite de l’utilisateur.
Avant enregistrement, contrôler le tableau et les quatre colonnes avec le validateur. Sans exécution possible, effectuer le même contrôle manuellement. Corriger toute non-conformité avant livraison, puis relire le Markdown réellement enregistré.

## Illustrer systématiquement

Chaque nouvelle recette doit avoir une image générée du plat. Utiliser l'outil de génération d'images disponible, en respectant ses instructions. Construire le prompt avec les ingrédients et la préparation connus : rendu culinaire réaliste, plat lisible, sans texte ni garniture inventée qui ferait croire à un ingrédient obligatoire. Une image illustre le résultat attendu ; elle ne prouve pas qu'une recette a été testée.

Enregistrer le véritable fichier image dans le dossier de pièces jointes du coffre, renseigner `image`, `image_type: generee` et afficher l'image dans le corps avec la mention « Illustration générée du résultat attendu ». Un lien temporaire de génération n'est pas un enregistrement durable. Pour transférer un PNG retourné en base64 ou par chemin local vers Drive, appliquer le parcours vérifié de la référence d'accès. Pour modifier une image, suivre le mécanisme d'édition de l'outil disponible.

Lors d'une mise à jour, conserver l'image si elle correspond toujours à la recette ; sinon la régénérer. Si aucune image n'existe, en générer une. Si la génération ou l'enregistrement de l'image échoue, enregistrer tout de même la note dans le dossier de recettes vérifié lorsque l'écriture y est disponible : `statut: brouillon`, `image: null`, sans lien d'image inexistant ni légende prétendant qu'une illustration est présente. Documenter le blocage dans « Points à vérifier ». Fournir les fichiers importables si l'écriture est indisponible. Ne pas déclarer la fiche complète. Ne jamais utiliser une image sans rapport pour satisfaire la présence d'un fichier.

## Vérifier et livrer

Vérifier le YAML, les quantités, les étapes, les sources et la présence réelle de l'image liée. Le script `scripts/verifier_recette.py` peut contrôler la structure et le chemin de l'image en accès local ; il nécessite PyYAML. Il ne valide pas la justesse culinaire.

Enregistrer seulement dans la portée de la demande. Relire la version enregistrée et vérifier ses parents ainsi que ceux de l’image jusqu’au coffre cible. Ne pas présenter une fiche trouvée dans une autre copie comme déjà rangée dans le bon coffre. Annoncer le nom de la fiche, son emplacement, l'image et les points manquants. Distinguer les fichiers préparés des fichiers effectivement enregistrés dans le coffre. Ne pas créer de dépôt, publier, modifier les Bases ou lancer une migration générale sans demande correspondante.
