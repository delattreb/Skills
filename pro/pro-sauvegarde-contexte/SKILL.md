---
name: "pro-sauvegarde-contexte"
description: "Sauvegarde le contexte de la conversation en cours (objectif, décisions, état, prochaines étapes) dans une note Obsidian, pour reprendre le travail dans une nouvelle session. À utiliser pour « sauvegarde le contexte », « /pro-sauvegarde-contexte », « note où on en est », « prépare la reprise »."
---

# Sauvegarde du contexte

Objectif : écrire une note autonome qui permet de reprendre le travail dans une conversation vierge, sans relire l'historique. Rien n'est envoyé ni modifié hors de cette note.

## Entrée
Un titre court facultatif. Sinon, le déduire du sujet principal de la conversation.

## Contenu de la note
- Objectif : ce que l'utilisateur veut obtenir, en 1 à 3 phrases.
- Décisions prises, avec leur raison quand elle compte.
- État d'avancement : ce qui est fait, ce qui est en cours, ce qui est bloqué.
- Prochaines étapes, ordonnées.
- Éléments à retrouver : chemins de fichiers, branches, URL, commandes, identifiants non secrets.
- Questions ouvertes.

## Règles
- Faits seulement : ce qui a été dit, décidé ou fait dans la conversation. Ne rien inventer ni extrapoler.
- Jamais de secrets (mots de passe, jetons, clés) ni de données RH ou de santé. Les signaler comme omis.
- Pas de copie de l'historique : synthèse seule, une note de 1 à 2 pages au plus.
- Style : français, concis, sans emojis ni tirets cadratins.

## Dépôt dans Obsidian
Écrire la note dans le coffre NeomaVault :
- chemin : `Contexte/AAAA-MM-JJ titre.md` (date du jour) ; créer le dossier s'il n'existe pas ;
- si le fichier existe déjà, ne pas l'écraser : ajouter un suffixe ` 2`, ` 3`, etc. ;
- en tête, un bloc YAML : titre, date, sujet, statut (`en cours`, `terminé`, `bloqué`) ;
- retrouver le coffre via les dossiers connectés de l'ordinateur (ou Google Drive si le coffre y est synchronisé) ; si le coffre est introuvable, le dire et proposer d'ajouter le dossier, sans écrire ailleurs.

## Réponse
Le chemin exact de la note, puis une phrase de reprise à coller dans la prochaine session, par exemple : « Reprends à partir de la note Contexte/AAAA-MM-JJ titre.md ». Ne pas recopier la note.
