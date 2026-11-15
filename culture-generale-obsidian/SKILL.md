---
name: "culture-generale-obsidian"
description: "Créer et gérer les fiches illustrées de culture générale du parcours CGI dans Obsidian MonVault (Google Drive), vérifier les publications, les index et les révisions."
---

# Culture générale Obsidian

## Accès et périmètre
Utiliser Google Drive connecté pour les opérations cloud. Vérifier la chaîne ObsidianVault / MonVault / Culture G avant toute écriture. Le dossier Culture G a l'ID 1Vb8hOBI6ZP1vFAc-MssyRoENeoRMhEhH. Ne jamais confondre avec Dessin/MonVault. En local, utiliser le même coffre uniquement après vérification du chemin réel; ne pas créer un coffre de remplacement. Préserver les autres notes, les annotations, les réglages et les partages.

Lire en premier les consignes actives sur Drive : https://drive.google.com/file/d/1_Ejyq1RhhLPpMRjfcQzr1szbCr78UwtY/view . L'« Annexe — copie de secours des consignes » ci-dessous est une copie de secours datée du 14 novembre 2026, pas une autorisation d'ignorer une version ultérieure.

## Organisation
- 00_Pilotage : consignes actives, modèle, index, page du jour, Journal.
- 01_Fiches : uniquement le parcours actif CGI-0001 à CGI-0365.
- 90_Regie : programme, réserve, anciens programmes et anciennes fiches CG conservés en place, sans les compter dans le parcours CGI. ID Drive : 12dglUciO8D9WvNYxzSUxfuZc4HA7bVS0.
Le regroupement de la régie dans le coffre remplace l'ancienne consigne de stockage hors coffre. Ne pas afficher les futurs sujets dans l'accueil, l'index ou les comptes rendus. Ne pas supprimer les archives.

## Publication
Suivre le parcours parcours-illustre-2026, calendrier à partir du 9 novembre 2026, Europe/Paris. Avant une création, lire fiches et journaux : identifier par YAML id et parcours, même si le fichier a été renommé. Au maximum une publication par date civile, aucune si une publication a déjà eu lieu ou est en cours. Réparer le suivi après interruption avant de produire davantage. Ne pas confondre les anciens CG et les nouveaux CGI.

Lire la ligne correspondante du programme; les pistes ne sont pas des sources vérifiées. Ouvrir au moins deux sources pertinentes, de préférence primaires et d'organismes différents. Expliquer mécanisme, preuves, limites et termes. Inclure une illustration explicative précise : Mermaid, tableau avec unités ou SVG joint avec légende et texte alternatif. Signaler les données fictives et schémas conceptuels. Un exercice à réponse repliée si pertinent et zéro à trois liens valides vers des fiches antérieures. Aucun PowerPoint. Ne pas publier si les sources ou l'accès sont insuffisants.

Écrire un Markdown UTF-8 CGI-NNNN.md sans écrasement, avec id, parcours, jour, date_publication réelle, date_decouverte vide, apprentissage non-lu et tags culture-generale. Ne jamais inventer une lecture, cocher une révision ou modifier les dates utilisateur. Préserver le type Date de date_decouverte.

Relire le fichier publié dans Drive, vérifier contenu, YAML, sources, liens et pièces jointes. Actualiser les sections AUTO de l'index et de la page du jour par leurs IDs stables, préserver le texte hors marqueurs. Journaliser uniquement le résultat réellement vérifié. L'index ne liste que les CGI disponibles. Calculer les rappels J+1, J+7, J+30 depuis les dates de découverte renseignées et tenir compte des révisions déjà faites. À 365 CGI vérifiées, suspendre la tâche existante avec l'outil approprié; aucune année 2 sans demande.

## Automatisation et limites
Le plugin contient une méthode réutilisable, il n'est pas un ordonnanceur. Réutiliser l'unique tâche cloud existante à 07:00 Europe/Paris. Ne pas créer une deuxième tâche, ne pas prétendre qu'une tâche existe ou fonctionne sans lecture de son état. Un déplacement Drive conservant les IDs ne nécessite pas de remplacer les liens. Si un connecteur manque, signaler précisément l'opération non effectuée; ne jamais annoncer une écriture locale comme une écriture cloud.

## Contrôle de maintenance
Pour ranger des fichiers : inventorier, lire les parents actuels, déplacer sans copier avec addParents/removeParents, conserver les IDs et vérifier les parents après écriture. En cas de doublon d'ID YAML ou conflit utilisateur, préserver les deux fichiers et signaler le conflit.

## Annexe — copie de secours des consignes (14 novembre 2026)

### Production cloud du parcours illustré

Ces consignes constituent la version active à partir du 9 novembre 2026. Elles remplacent les anciennes dates, le préfixe CG et le programme initial encore mentionnés dans le prompt historique. Lire ce fichier en premier et suivre exclusivement le parcours CGI. La première fiche est déjà déposée. Continuer avec CGI-0002 à la prochaine exécution quotidienne. Le calendrier de référence commence le 9 novembre 2026, heure de Paris. Garder l’unique tâche cloud existante à 07:00 Europe/Paris.

### Sources de travail — Culture G/90_Regie

- Programme : https://drive.google.com/file/d/1nbYWquwkUwm1cBlCBFRoWFkIPPzHptkc/view
- Réserve : https://drive.google.com/file/d/1yLC7KXVcGIP7tRA0qeVmDs5e2Qqw6QO9/view

Lire en entier ou extraire la ligne CGI nécessaire du fichier brut si le rendu de Drive est tronqué. Consulter la réserve pour les 28 premières fiches. La première est finalisée. Pour les versions courtes, vérifier les références, développer le mécanisme et les preuves, puis réaliser les visuels avant dépôt. Après cette réserve, rédiger depuis le programme privé. Le programme et la réserve sont regroupés dans Culture G/90_Regie à la demande du propriétaire. Les intitulés à venir restent dans ces consignes opérationnelles. Ne pas recopier le programme dans la navigation, les journaux, les fiches ou les comptes rendus. Les pistes documentaires sont des points de départ.

### Écriture quotidienne

Consulter le dossier des fiches par son ID Drive 1mgO1_GxTnT5uZDbRDTjmPOdDeaSrhQ24. Compter uniquement les propriétés YAML parcours: parcours-illustre-2026 et les identifiants CGI-0001 à CGI-0365. Choisir le premier identifiant manquant arrivé à échéance. Ne publier qu’une fiche par date civile de Paris et reprendre le premier jour manquant après interruption. Avant tout import, vérifier l’absence du même nom et du même identifiant, même après renommage. En cas de relance, réparer l’index et le journal de la fiche déjà écrite avant d’envisager un nouvel import. Si un fichier est incomplet, signaler le problème sans écraser les annotations. À 365 fiches vérifiées, suspendre la tâche existante et signaler l’achèvement sans dévoiler le programme.

Rédiger en français une fiche Markdown UTF-8. Expliquer le mécanisme, distinguer observation, expérience et interprétation, indiquer les limites et citer des sources effectivement ouvertes. Inclure au moins une illustration explicative que le lecteur doit lire, décoder ou comparer. Utiliser Mermaid, un tableau de données avec unités, ou un SVG légendé en pièce jointe avec référence et texte alternatif. Signaler clairement les schémas conceptuels et les données fictives. Préférer un exercice avec réponse repliée quand il s’y prête. Ajouter de un à trois liens vers les fiches déjà parues de ce parcours, selon leur pertinence. Une fiche sans antécédent peut rester sans lien. Aucun PowerPoint.

Utiliser le nom CGI-NNNN.md et les propriétés id, parcours, jour, date_publication, date_decouverte vide, apprentissage non-lu et tags culture-generale. Garder la propriété Obsidian date_decouverte au type Date. N’écrire aucune lecture ou révision à la place de l’utilisateur.

Importer le Markdown puis relire le fichier dans Drive. Vérifier l’identifiant, le contenu, les sources et les cibles des liens. Actualiser les sections AUTO de l’index et de la page du jour en place, via leurs IDs stables 1r2D0zteCG-S3FpDQu79eCZM24bbS1wA6 et 13rFkxgDowuwypHurBKBvvQU6zKpN3bGF. Conserver le contenu hors marqueurs. L’index contient uniquement les fiches parues. La page du jour montre la dernière fiche et les rappels dus à J+1, J+7 et J+30 calculés sur les dates réelles renseignées par le lecteur. Journaliser le résultat par date dans 1T7hTxTNE1108YEN6BpKv-hm9gnvnnXBJ. Après réussite, indiquer seulement la fiche parue. En cas d’échec, signaler l’étape et le résultat réellement observé.