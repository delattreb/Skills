---
name: "pro-sauvegarde-contexte"
description: "Sauvegarde la conversation en cours dans Obsidian (NeomaVault, dossier Sauvegarde) sous forme de fiche : idée générale, résumé, décisions, actions, ressources, tags réutilisés. À utiliser pour « sauvegarde la conversation », « /pro-sauvegarde-contexte », « fais une fiche de cette conversation », « note où on en est »."
---

# Sauvegarde de conversation

Objectif : transformer la conversation en cours en une fiche Obsidian autonome, taguée et classée par sujet, qui permet de la retrouver et de la reprendre sans relire l'historique. La fiche est une synthèse : la conversation n'est pas recopiée.

## Entrée
Un titre court facultatif. Sinon, le déduire du sujet principal de la conversation. Ne poser aucune question sauf si le coffre est introuvable.

## Méthode
1. Retrouver le coffre NeomaVault via les dossiers connectés de l'ordinateur (ou Google Drive si le coffre y est synchronisé). Introuvable : le dire, proposer d'ajouter le dossier, ne rien écrire ailleurs.
2. Lister les sous-dossiers de `Sauvegarde/` et lire les tags déjà utilisés dans les fiches de ce dossier (YAML `tags`).
3. Choisir le sujet : réutiliser un sous-dossier existant s'il convient, n'en créer un (nom court, une majuscule, singulier) qu'en dernier recours.
4. Choisir 3 à 6 tags : réutiliser les tags existants en priorité, en créer un seul si aucun ne convient. Format kebab-case sans accents, sans espace.
5. Chercher une fiche du même sujet dans `Sauvegarde/` (titre, tags). Si elle existe, la nouvelle fiche la référence (voir Doublons).
6. Écrire la fiche, puis répondre.

## Emplacement et nom
- Chemin : `Sauvegarde/<Sujet>/AAAA-MM-JJ titre.md`, date du jour, titre court sans caractères interdits (`/ \ : * ? " < > |`).
- Créer le sous-dossier s'il n'existe pas.
- Si le nom existe déjà, suffixer ` 2`, ` 3`. Ne jamais écraser une fiche.

## Doublons
Si une fiche du même sujet existe : créer quand même la nouvelle fiche, y mettre `suite_de: "[[AAAA-MM-JJ titre]]"` dans le YAML et un lien `[[...]]` dans « Idée générale ». Ne pas modifier l'ancienne fiche.

## Format de la fiche
En tête, un bloc YAML :
```yaml
---
titre: ""
date: AAAA-MM-JJ
tags: []
type: décision | recherche | dev | idée | apprentissage | résolution de problème
contexte_technique:
  depot: ""
  branche: ""
  outils: []
  session: ""
suite_de: ""
---
```
- `contexte_technique` : ne renseigner que ce qui est connu (dépôt, branche, outils ou skills utilisés, URL de session). Retirer les clés vides.
- `suite_de` : seulement en cas de doublon, sinon retirer la clé.

Sections, dans cet ordre, une section vide est omise :
1. **Idée générale** : 2 à 3 phrases.
2. **Résumé** : points clés, courtes puces.
3. **Décisions et conclusions** : ce qui a été décidé ou conclu, avec la raison quand elle compte.
4. **Actions et suite** : prochaines étapes ordonnées, puis questions restées ouvertes.
5. **Ressources et extraits** : chemins de fichiers, liens, commandes, code ou extraits notables, en blocs de code.

## Règles
- Faits seulement : ce qui a été dit, décidé ou fait dans la conversation. Ne rien inventer ni extrapoler.
- Mots de passe, jetons, clés d'API et secrets : jamais écrits. Ajouter une ligne « Élément sensible omis » à l'endroit concerné. Le reste (noms, données) est conservé tel quel.
- Fiche courte : 1 à 2 pages au plus.
- Style : français, concis, sans emojis ni tirets cadratins.

## Réponse
Le chemin exact de la fiche, la liste des tags retenus (signaler le tag créé, s'il y en a un), et le lien vers la fiche précédente en cas de doublon. Ne pas recopier la fiche.
