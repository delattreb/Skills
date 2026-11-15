---
name: agenda-contexte
description: Parcourt les rendez-vous de l'agenda Outlook Microsoft 365 et, pour chacun, recherche dans les anciens e-mails les échanges liés (participants, sujet, décisions passées), puis consigne le contexte dans une note Markdown « contexte agenda » du dossier Agenda sur Google Drive. À utiliser dès que l'utilisateur parle de son agenda, de ses rendez-vous ou réunions à venir, d'un ordre du jour à préparer, d'un brief ou d'une préparation de réunion, ou demande « qu'est-ce que j'ai cette semaine », même sans citer Outlook ni le skill.
---

# Agenda - Contexte : consigner le contexte des rendez-vous

## Objectif

Pour chaque rendez-vous de la période demandée, retrouver dans les anciens e-mails ce qui a déjà été échangé avec les participants et sur le même sujet, puis rédiger une synthèse. Le résultat est écrit dans une note Markdown « contexte agenda » (dossier Agenda, Google Drive), lue ensuite dans Obsidian. L'utilisateur y retrouve l'ordre du jour expliqué sans rechercher ses mails.

## Déroulé

1. **Fixer la période.** Par défaut, les 7 prochains jours, fuseau Europe/Paris.
2. **Lister les rendez-vous** avec la recherche d'agenda Microsoft 365 (titre, date, heure, organisateur, participants, description). Écarter les rendez-vous annulés et les blocs personnels sans invité. Repérer ceux que l'utilisateur organise lui-même : ils sont traités comme les autres (recherche et rédaction), mais placés dans une section à part de la note. Annoncer le nombre trouvé avant de lancer les recherches de mails.
3. **Chercher les échanges passés** pour chaque rendez-vous avec la recherche d'e-mails Microsoft 365 :
   - par adresse de chaque participant clé (expéditeur ou destinataire) ;
   - par mots-clés distinctifs tirés du titre et de la description (ignorer les mots vides) ;
   - sur 12 mois par défaut.
   Une requête par participant clé et une par thème suffisent. Inutile de multiplier les variantes proches.
4. **Lire les fils pertinents.** Prendre 5 à 10 fils au maximum par rendez-vous, les plus récents d'abord, et ne retenir que ce qui éclaire la réunion : décisions, questions ouvertes, engagements, dates, chiffres, désaccords.
5. **Rédiger le bloc de chaque rendez-vous** (format ci-dessous).
6. **Écrire la note « contexte agenda »** (règle d'écriture ci-dessous).

## Format du bloc par rendez-vous

Chaque rendez-vous a un sous-titre (date, heure, intervenant principal) suivi de :

- **Synthèse** : 3 à 5 phrases en prose, en français, qui expliquent le fil des échanges précédents et ce qu'ils impliquent pour cette réunion.
- **Points en suspens** : liste courte, uniquement ce qui est réellement ouvert dans les mails.
- **Dernier échange** : date, expéditeur, objet du mail.
- **Sources** : objets des mails et dates, sans copie de leur contenu.

Si aucun échange pertinent n'est trouvé, le bloc se réduit à : « Synthèse : aucun échange pertinent trouvé dans les e-mails des 12 derniers mois. »

## Règle d'écriture

- **Une seule note, créée ou remplacée.** La note s'appelle « contexte agenda.md » et se trouve dans le dossier Agenda de Google Drive. Si elle existe déjà, elle est remplacée par la nouvelle version, sans doublon. Elle est enregistrée en Markdown (sans conversion en Google Doc) pour rester lisible dans Obsidian.
- **Structure de la note :** un titre avec la période, puis une section « Réunions organisées par moi » et une section « Réunions organisées par d'autres ». Chaque rendez-vous y a son bloc.
- **Ne jamais modifier l'agenda Outlook.** Aucun rendez-vous n'est réécrit dans Outlook, même si l'outil de mise à jour est disponible. Les modifications d'agenda sont hors du périmètre de ce skill tant que l'utilisateur ne les demande pas explicitement, et que la permission d'écriture est accordée.
- **Ne pas exposer les mails privés inutilement.** Le contenu reste un résumé : pas de copie de mail, pas d'extrait long, et les sujets sensibles (RH, par exemple) ne sont mentionnés que par leur existence, sans détail.

## Règles générales

- Ne rien inventer. Si rien de pertinent n'existe, écrire le message prévu plutôt que de combler par des suppositions.
- Résumer, ne jamais recopier un mail ni reproduire de longs extraits.
- Aucun e-mail n'est envoyé, déplacé ni supprimé. Aucun rendez-vous Outlook n'est modifié.
- Un mail qui n'a qu'un lien apparent avec la réunion (même mot, autre sujet) est écarté plutôt que forcé dans le contexte.
- Une recherche en échec ou un agenda vide est signalé clairement dans la réponse finale.

## Réponse finale

Une courte liste : nombre de rendez-vous traités, nombre avec contexte trouvé, nombre sans échange pertinent, et le lien vers la note « contexte agenda ». Pas de copie de la note dans le chat, sauf demande explicite.
