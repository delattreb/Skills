---
name: agenda-contexte
description: Parcourt les rendez-vous de l'agenda Outlook Microsoft 365 et, pour chacun, recherche dans les anciens e-mails les échanges liés (participants, sujet, décisions passées), puis ajoute le résultat dans la description du rendez-vous sous un titre « Contexte ». À utiliser dès que l'utilisateur parle de son agenda, de ses rendez-vous ou réunions à venir, d'un ordre du jour à préparer, d'un brief ou d'une préparation de réunion, ou demande « qu'est-ce que j'ai cette semaine », même sans citer Outlook ni le skill.
---

# Agenda - Contexte : ajouter le contexte aux rendez-vous Outlook

## Objectif

Pour chaque rendez-vous de la période demandée, retrouver dans les anciens e-mails ce qui a déjà été échangé avec les participants et sur le même sujet, puis écrire une synthèse dans le rendez-vous lui-même, sous un titre « Contexte ». Le but est que l'utilisateur ouvre l'événement et comprenne l'ordre du jour sans rechercher ses mails.

## Déroulé

1. **Fixer la période.** Par défaut, les 7 prochains jours, fuseau Europe/Paris.
2. **Lister les rendez-vous** avec la recherche d'agenda Microsoft 365 (titre, date, heure, organisateur, participants, description). Écarter les rendez-vous annulés et les blocs personnels sans invité. Repérer ceux que l'utilisateur organise lui-même : ils ne sont jamais modifiés (voir la règle d'écriture). Annoncer le nombre trouvé avant de lancer les recherches de mails.
3. **Chercher les échanges passés** pour chaque rendez-vous avec la recherche d'e-mails Microsoft 365 :
   - par adresse de chaque participant clé (expéditeur ou destinataire) ;
   - par mots-clés distinctifs tirés du titre et de la description (ignorer les mots vides) ;
   - sur 12 mois par défaut.
   Une requête par participant clé et une par thème suffisent. Inutile de multiplier les variantes proches.
4. **Lire les fils pertinents.** Prendre 5 à 10 fils au maximum par rendez-vous, les plus récents d'abord, et ne retenir que ce qui éclaire la réunion : décisions, questions ouvertes, engagements, dates, chiffres, désaccords.
5. **Rédiger le bloc « Contexte »** de chaque rendez-vous (format ci-dessous).
6. **Écrire dans le rendez-vous**, en respectant la règle d'écriture ci-dessous.

## Format du bloc « Contexte »

Le bloc commence par un titre « Contexte » et contient, dans cet ordre :

- **Synthèse** : 3 à 5 phrases en prose, en français, qui expliquent le fil des échanges précédents et ce qu'ils impliquent pour cette réunion.
- **Points en suspens** : liste courte, uniquement ce qui est réellement ouvert dans les mails.
- **Dernier échange** : date, expéditeur, objet du mail.
- **Sources** : objets des mails et dates, sans copie de leur contenu.

Si aucun échange pertinent n'est trouvé, le bloc se réduit à : « Contexte — aucun échange pertinent trouvé dans les e-mails des 12 derniers mois. »

## Règle d'écriture dans le rendez-vous

- **Conserver la description existante.** Le bloc « Contexte » est ajouté à la fin, après une ligne de séparation. Ne jamais supprimer ni réécrire ce qui était déjà là.
- **Ne jamais dupliquer.** Si un titre « Contexte » existe déjà dans la description, remplacer uniquement ce bloc par la nouvelle version, sans toucher au reste.
- **Ne jamais écrire dans les rendez-vous organisés par l'utilisateur.** Sa description est visible par tous les invités, et le contexte tiré de ses mails privés ne doit pas leur être exposé. Ces rendez-vous sont traités comme les autres pour la recherche, mais le bloc rédigé est seulement présenté dans la réponse finale, sous une section dédiée, pour que l'utilisateur le colle lui-même s'il le souhaite.
- **Modifier uniquement la description.** Ne pas changer le titre, l'horaire, le lieu ni les participants. Lors de la réécriture de la description, reprendre à l'identique tout le contenu existant (y compris les blocs de connexion aux réunions Teams).
- **Ignorer les événements non modifiables.** Si l'outil de mise à jour refuse (événement d'un autre organisateur, par exemple), ne pas insister : le signaler dans la réponse finale avec le contexte rédigé, pour que l'utilisateur puisse le coller lui-même.

## Règles générales

- Ne rien inventer. Si rien de pertinent n'existe, écrire le message prévu plutôt que de combler par des suppositions.
- Résumer, ne jamais recopier un mail ni reproduire de longs extraits.
- Aucun e-mail n'est envoyé, déplacé ni supprimé. Seule la description des rendez-vous est modifiée.
- Un mail qui n'a qu'un lien apparent avec la réunion (même mot, autre sujet) est écarté plutôt que forcé dans le contexte.
- Une recherche en échec ou un agenda vide est signalé clairement dans la réponse finale.

## Réponse finale

Une courte liste : nombre de rendez-vous traités, nombre avec contexte trouvé, nombre sans échange pertinent, nombre de rendez-vous écrits. Ensuite, une section « Réunions organisées (non modifiées) » avec le bloc « Contexte » rédigé pour chacune, et les éventuels rendez-vous qui n'ont pas pu être modifiés (avec le texte à coller). Pas de copie des fiches dans le chat, sauf demande explicite.
