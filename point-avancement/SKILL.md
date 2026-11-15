---
name: point-avancement
description: Rédige en français un court point d'avancement hebdomadaire couvrant les 7 derniers jours, à partir des e-mails envoyés et reçus, du calendrier Outlook et des messages Teams (connecteur Microsoft 365, lecture seule). À utiliser quand l'utilisateur demande « point d'avancement », « point hebdo », « /point-avancement », « résumé de ma semaine », « sur quoi j'ai travaillé cette semaine », « weekly status » ou « rapport hebdomadaire ».
metadata:
  version: "0.1.0"
---

# Point d'avancement hebdomadaire

Produire un point d'avancement factuel, en français, d'une page maximum, sur la période des 7 jours précédant le jour de lancement, à partir des données Outlook / Teams de l'utilisateur.

## Règles impératives

- **Lecture seule.** Ne jamais répondre à un e-mail, envoyer un message, créer ou modifier un brouillon, un événement, un libellé ou quoi que ce soit dans Outlook, Teams ou SharePoint. N'utiliser que les outils de recherche et de lecture listés ci-dessous.
- **Ne rien inventer.** Chaque puce doit reposer sur un e-mail, une réunion ou un message consulté. Si une information est incertaine (statut flou, décision implicite, réunion sans compte rendu), l'indiquer explicitement : « (à confirmer) », « (non vérifié) ».
- **Connecteur indisponible.** Si les outils `mcp__Microsoft_365__*` sont absents, renvoient une erreur d'authentification ou une session expirée, s'arrêter et l'indiquer en une ligne (ex. : « Le connecteur Microsoft 365 est indisponible ou la connexion a expiré : reconnectez-le pour générer le point d'avancement. »). Ne pas produire de résumé vide ni partiel déguisé.

## Étape 1 — Préparer

1. Charger les outils via ToolSearch si nécessaire : `select:mcp__Microsoft_365__get_me,mcp__Microsoft_365__outlook_email_search,mcp__Microsoft_365__outlook_calendar_search,mcp__Microsoft_365__chat_message_search,mcp__Microsoft_365__read_resource`.
2. Appeler `get_me` pour connaître le nom et l'adresse de l'utilisateur (sert à distinguer envoyé / reçu et à repérer ce qu'on attend de lui).
3. Calculer les bornes : **début = jour de lancement − 7 jours**, **fin = jour de lancement** (fuseau de l'utilisateur). Calculer aussi la fenêtre « à venir » : jour de lancement → jour de lancement + 7 jours.

## Étape 2 — Collecter (lancer les recherches indépendantes en parallèle)

1. **E-mails envoyés** sur la période (`outlook_email_search`, dossier Éléments envoyés / expéditeur = utilisateur). Source principale de ce qui a été fait, décidé ou promis. Paginer jusqu'à couvrir toute la période.
2. **E-mails reçus importants** sur la période : demandes adressées à l'utilisateur, validations, questions. Repérer ceux restés **sans réponse** de sa part (aucun envoi ultérieur dans le même fil).
3. **Calendrier** (`outlook_calendar_search`) : réunions tenues sur la période, puis réunions clés des 7 prochains jours.
4. **Teams** (`chat_message_search`), si disponible : décisions et engagements pris sur la période. En cas d'absence ou d'erreur de cet outil, continuer sans et le signaler en fin de résumé.

Ouvrir les fils pertinents (`read_resource` ou lecture du message) pour comprendre le contexte avant de conclure. Voir `references/tri-et-classement.md` pour le filtrage du bruit et les indices de classement.

## Étape 3 — Analyser

- Regrouper les éléments par **projet / sujet** (objet des fils, interlocuteurs, nom de projet récurrent).
- Classer chaque élément dans une seule rubrique : réalisation, décision, en suspens, à venir.
- Pour chaque décision : qui l'a prise ou validée, quoi, sur quel sujet.
- Pour chaque point en suspens : nommer la personne concernée (qui attend quoi de qui).

## Étape 4 — Rédiger

Respecter exactement ce format (une page maximum) :

```
# Point d'avancement – semaine du [JJ mois] au [JJ mois AAAA]

## Principales réalisations
**[Projet / sujet A]**
- [fait, factuel, verbe au passé composé]
**[Projet / sujet B]**
- …
(3 à 7 puces au total)

## Décisions prises
- [Sujet] : [qui] a décidé / validé [quoi] ([date]).

## En suspens / à suivre
- [Sujet] : [question sans réponse / action promise / blocage / relance] — [personne concernée].

## À venir
- [jour JJ/MM] : [réunion ou échéance] — [enjeu en quelques mots].
```

Style : concis, professionnel, sans remplissage ni formule d'introduction. Une rubrique sans contenu affiche « Rien de notable sur la période. » plutôt que d'être inventée. Si Teams n'a pas pu être consulté, ajouter une ligne finale en italique le signalant.

## Étape 5 — Livrer

Livrer le point d'avancement dans la réponse finale, prêt à copier-coller. Si l'outil SendUserMessage est disponible (notamment en exécution planifiée sans personne présente), envoyer aussi le texte complet via SendUserMessage. Ne pas l'envoyer par e-mail ni sur Teams.
