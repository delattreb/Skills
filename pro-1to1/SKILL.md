---
name: "pro-1to1"
description: "Prépare un entretien individuel (1to1) avec un membre de l'équipe à partir des mails, Teams et agenda Outlook (Microsoft 365, lecture seule). À utiliser pour « 1to1 », « prépare mon 1to1 avec X »."
---

# 1to1 : préparation d'un entretien individuel

Objectif : donner au manager une fiche courte et actionnable pour un entretien avec une personne de son équipe, construite uniquement à partir de faits retrouvés dans Microsoft 365. Tout est en lecture seule : ne jamais envoyer, répondre, créer ou modifier quoi que ce soit.

## Entrée
Le nom de la personne (prénom et nom). Si absent, le demander. Période par défaut : 3 mois pour les mails, Teams et le calendrier passé, 3 semaines pour le calendrier à venir.

## Méthode
1. Charger les outils Microsoft 365 nécessaires via ToolSearch en un seul appel : outlook_email_search, outlook_calendar_search, chat_message_search, read_resource, get_me.
2. Ne pas compter sur search_people : la permission People.Read est souvent refusée. Chercher directement par nom.
3. Lancer en parallèle :
   - mails : recherche texte sur le nom, afterDateTime = 3 mois ;
   - calendrier : attendee = nom de famille ou adresse, passé 3 mois puis à venir 3 semaines (order oldest pour le futur) ;
   - Teams : messages envoyés par la personne (sender) et à elle (recipient).
4. Lire en détail (read_resource) uniquement les 3 à 6 éléments les plus utiles : demandes formelles ou RH en cours, relances, projets en retard, mails où elle attend une réponse du manager. Si le corps d'un mail est long (tableaux, historiques), en extraire les faits et les dates, pas le texte.
5. Le chat Teams 1:1 avec le manager est informel : ne pas en citer le contenu. Les canaux de projet et réunions peuvent alimenter les projets.
6. Les résultats sont paginés : indiquer ce qui a été couvert et ce qui ne l'a pas été.

## Contenu de la fiche (écrite dans Obsidian, pas affichée dans la réponse)
- Sujet sensible prioritaire, si l'un existe (rémunération, évolution, conflit, charge) : état des lieux chronologique, engagements pris par le manager avec leur échéance, ce que la personne attend précisément.
- Projets en cours : un court paragraphe par projet avec l'état, les retards, les décisions récentes, les points où elle attend quelque chose.
- Agenda à venir avec elle (heures en fuseau Europe/Paris) et mention s'il n'existe aucun 1to1 dédié.
- Trame proposée pour l'entretien, 4 à 6 points ordonnés par importance.
- Limites de la recherche : accès refusés, pages non lues, sources non consultées.

## Règles
- Faits seulement : chaque affirmation vient d'un mail, d'un événement ou d'un message retrouvé. Ne rien inférer sur la personnalité, le moral ou les intentions.
- Les sujets RH et de rémunération sont traités avec sobriété : chiffres uniquement s'ils sont nécessaires à la préparation, pas de jugement, pas de conseil juridique. Ne jamais recopier ces éléments dans la mémoire ni les diffuser ailleurs que dans la réponse au manager.
- Ne pas reprendre les plaisanteries ou propos informels de Teams.
- Signaler les échéances proches ou dépassées en gras.
- Style : français, concis, sans emojis ni tirets cadratins.
- Terminer en proposant, sans le faire : un brouillon de réponse écrite sur un sujet ouvert.

## Dépôt dans Obsidian (systématique)
Après la réponse, écrire la fiche en Markdown dans le coffre Obsidian NeomaVault, dans un répertoire nommé `1to1`, avec un sous-répertoire par semaine :
- chemin : `1to1/AAAA-SNN/prenom-nom.md`, où AAAA-SNN est la semaine ISO de la date du jour (exemple : `1to1/2026-S47/caroline-martinot.md`) ;
- créer le répertoire de la semaine s'il n'existe pas ;
- si le fichier de la personne existe déjà cette semaine, le remplacer par la version à jour ;
- en tête de fichier, un bloc YAML : personne, date de préparation, semaine, période analysée ;
- le contenu est la fiche complète, écrite directement dans Obsidian sans être recopiée dans la réponse ;
- retrouver l'emplacement du coffre via les dossiers connectés de l'ordinateur (device_list_dir sur le dossier connecté, ou Google Drive si le coffre y est synchronisé) ; si le coffre est introuvable, le dire et proposer d'ajouter le dossier, sans écrire ailleurs ;
- la réponse au manager se limite au chemin exact du fichier créé et à 1 à 3 points d'alerte (échéances proches ou dépassées, demandes en attente). Ne pas reproduire la fiche dans la réponse.