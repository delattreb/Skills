---
name: agenda
description: Parcourt l'agenda professionnel Outlook (connecteur Microsoft 365) sur les 7 prochains jours et, pour chaque rendez-vous, reconstitue le contexte à partir des e-mails (12 mois), des conversations Teams (3 mois) et de tous les comptes rendus de réunions liés, afin de préparer chaque réunion et de ne pas être surpris. Écrit le résultat dans Obsidian, coffre NeomaVault, fichier Agenda/agenda.md (remplacé à chaque lancement). À utiliser quand l'utilisateur demande « /agenda », « prépare ma semaine », « prépare mes réunions », « qu'est-ce que j'ai cette semaine », « contexte de mes rendez-vous », « brief de réunion », ou parle de préparer ses rendez-vous à venir, même sans citer Outlook ni le skill.
metadata:
  version: "0.1.0"
---

# Agenda : préparer les réunions de la semaine

Pour chaque rendez-vous des 7 prochains jours, retrouver ce qui a déjà été dit, décidé et promis, qui sont les participants, et ce qui risque d'être abordé, puis consigner le tout dans une fiche unique `agenda.md` lue dans Obsidian. Objectif : arriver préparé à chaque réunion et ne pas être pris au dépourvu.

## Règles impératives

- **Lecture seule côté Microsoft 365.** Ne jamais envoyer, répondre, transférer, déplacer ni supprimer un e-mail ou un message Teams. Ne jamais créer, modifier, accepter ou refuser un rendez-vous Outlook. Seuls les outils de recherche et de lecture sont utilisés.
- **Une seule écriture : `agenda.md`.** C'est le seul fichier créé ou modifié, et il est remplacé entièrement à chaque lancement.
- **Ne rien inventer.** Chaque affirmation repose sur un mail, un message Teams ou un compte rendu consulté. Une information incertaine est marquée « (à confirmer) ». Un mail qui n'a qu'un lien apparent avec la réunion (même mot, autre sujet) est écarté.
- **Résumer, ne pas recopier.** Pas de copie intégrale de mail ou de message. Une citation courte est permise quand la formulation exacte compte (engagement, chiffre, désaccord).
- **Connecteur indisponible.** Si les outils `mcp__Microsoft_365__*` sont absents ou renvoient une erreur d'authentification, s'arrêter et le dire en une ligne : « Le connecteur Microsoft 365 est indisponible ou la connexion a expiré : reconnectez-le pour préparer l'agenda. » Ne pas écrire de fiche vide. Si seul Teams échoue, continuer avec les mails et le signaler dans la fiche et dans la réponse finale.

## Étape 1 — Préparer

1. Charger les outils via ToolSearch si nécessaire : `select:mcp__Microsoft_365__get_me,mcp__Microsoft_365__outlook_calendar_search,mcp__Microsoft_365__outlook_email_search,mcp__Microsoft_365__chat_message_search,mcp__Microsoft_365__teams_list_chats,mcp__Microsoft_365__teams_list_channels,mcp__Microsoft_365__teams_list_channel_messages,mcp__Microsoft_365__search_people,mcp__Microsoft_365__sharepoint_search,mcp__Microsoft_365__read_resource`, et les outils Google Drive (`search_files`, `get_file_metadata`, `create_file`, `update_file`).
2. Appeler `get_me` : nom, adresse et fuseau de l'utilisateur. L'adresse sert à repérer les réunions qu'il organise, ce qu'il a envoyé et ce qu'on attend de lui.
3. Calculer la période : **du jour de lancement 00:00 à J+6 23:59** (7 jours glissants, week-end compris), fuseau Europe/Paris sauf indication contraire de `get_me`.
4. Calculer les fenêtres de recherche : **mails = 12 mois** avant le jour de lancement, **Teams = 3 mois**, **comptes rendus = sans limite de date**.

## Étape 2 — Lister les rendez-vous

Avec `outlook_calendar_search` sur la période (paginer jusqu'au bout), relever pour chaque rendez-vous : titre, date, heure de début et de fin, lieu ou lien Teams, organisateur, participants (obligatoires et facultatifs), description, récurrence, statut de réponse.

Écarter :
- les rendez-vous **annulés** ;
- les rendez-vous **refusés** par l'utilisateur ;
- les **blocs sans invité** (focus, déjeuner, blocs personnels, rappels).

Conserver les réunions dont l'utilisateur est l'organisateur et les marquer « organisée par moi ». Pour une réunion récurrente, chaque occurrence de la période est traitée ; les recherches de contexte communes peuvent être mutualisées entre occurrences.

Annoncer le nombre de rendez-vous retenus avant de lancer les recherches.

## Étape 3 — Identifier les participants

Pour chaque participant (hors utilisateur), établir une ligne de rôle :
- fonction et service avec `search_people` (ou la signature de ses derniers mails si l'annuaire ne renvoie rien) ;
- organisation, si externe (domaine de l'adresse, signature) ;
- **dernier échange** avec l'utilisateur : date et objet du dernier mail ou message Teams.

Ne pas répéter la recherche d'une personne qui apparaît dans plusieurs réunions : réutiliser le résultat. Au-delà de 10 participants, ne détailler que l'organisateur et les participants avec qui l'utilisateur a échangé ; regrouper les autres en une ligne (« et 14 autres participants »).

## Étape 4 — Rechercher le contexte

Lancer en parallèle les recherches indépendantes. Pour chaque rendez-vous :

1. **E-mails (12 mois)** avec `outlook_email_search` :
   - une requête par participant clé (organisateur et participants obligatoires), en expéditeur ou destinataire ;
   - une requête par thème, avec les mots distinctifs du titre et de la description (ignorer les mots vides et les termes génériques comme « réunion », « point », « suivi ») ;
   - l'invitation elle-même et ses éventuelles pièces jointes ou ordre du jour.
   Commencer par les 3 derniers mois ; n'élargir jusqu'à 12 mois que si le contexte récent est insuffisant.
2. **Teams (3 mois)** avec `chat_message_search`, `teams_list_chats` et `teams_list_channels` / `teams_list_channel_messages` :
   - conversations privées et de groupe avec au moins un participant clé ;
   - conversation de la réunion elle-même (réunions récurrentes ou déjà tenues) ;
   - canaux dont le nom ou le sujet recoupe le titre ou la description : lister les canaux d'abord, puis ne lire que ceux qui correspondent.
3. **Comptes rendus (sans limite de date)** : rechercher tous les comptes rendus qui concernent les sujets ou les participants de la réunion :
   - récapitulatifs de réunion Teams, notes et messages postés dans la conversation de réunion ;
   - mails et messages contenant « compte rendu », « CR », « relevé de décisions », « récap », « notes de réunion », « minutes » avec le titre ou les mots-clés du sujet ;
   - documents de compte rendu dans OneDrive / SharePoint avec `sharepoint_search` (lecture seule).
   Une transcription n'est pas lue en entier : n'en reprendre que les décisions et actions déjà résumées dans le récapitulatif ou le compte rendu.

Une requête par participant clé et une par thème suffisent : ne pas multiplier les variantes proches.

## Étape 5 — Lire et analyser

1. Retenir pour chaque réunion **5 à 10 fils au maximum** (mails, conversations Teams et comptes rendus confondus), les plus récents d'abord, et les ouvrir avec `read_resource` pour en comprendre le contenu.
2. **Les comptes rendus font foi** pour les décisions prises. Pour chaque action qu'ils attribuent (responsable, échéance), vérifier dans les mails et messages plus récents si elle est close ; ne présenter comme ouvertes que celles qui le sont encore. Si deux comptes rendus se contredisent, retenir le plus récent et le signaler.
3. Repérer ce qui peut surprendre l'utilisateur en réunion : engagements qu'il a pris, demandes restées sans réponse de sa part, désaccords, tensions, sujets RH ou budgétaires, retards, changements de périmètre, nouvelles personnes, questions qu'on risque de lui poser.
4. Les sujets sensibles sont restitués en détail : la fiche est privée et destinée à l'utilisateur seul.

## Étape 6 — Rédiger `agenda.md`

Respecter cette structure :

```markdown
# Agenda du [JJ mois] au [JJ mois AAAA]

*Généré le [JJ/MM/AAAA à HH:MM] — [N] réunions, [N] avec contexte, [N] sans contexte trouvé.*

## Sommaire

| Jour | Heure | Réunion | Organisateur | Contexte |
|---|---|---|---|---|
| Lun 16/11 | 09:00–10:00 | [[#Titre de la réunion]] | Prénom Nom | ✅ trouvé |
| Lun 16/11 | 14:00–14:30 | [[#Autre réunion]] | moi | ❌ rien trouvé |

## Lundi 16 novembre

### 09:00–10:00 · Titre de la réunion

- **Lieu :** salle / lien Teams
- **Organisateur :** Prénom Nom (ou « organisée par moi »)
- **Récurrence :** hebdomadaire (si applicable)

**Participants**
- Prénom Nom — fonction, service / organisation. Dernier échange : JJ/MM, « objet ».

**Objet de la réunion**
2 ou 3 phrases : pourquoi cette réunion a lieu et ce qui est attendu.

**Historique**
Prose : le fil des échanges précédents (mails, Teams, réunions passées) et ce qu'il implique pour cette réunion.

**Décisions déjà prises**
- Décision — source (compte rendu du JJ/MM/AAAA, mail du JJ/MM).

**Actions en cours**
- Action — responsable — échéance — ouverte / en retard.

**Points de vigilance**
- Ce qui peut surprendre : engagement pris, demande sans réponse, désaccord, question probable.

**À préparer**
- Document à relire, chiffre à avoir, question à poser.

**Sources**
- Mail · JJ/MM/AAAA · expéditeur · « objet »
- Teams · JJ/MM/AAAA · conversation ou canal
- Compte rendu · JJ/MM/AAAA · « titre »
```

Règles de rédaction :
- Un titre `##` par jour (jours sans réunion omis), réunions dans l'ordre horaire.
- Les liens du sommaire pointent vers le titre exact de la section de la réunion (`[[#…]]`). Si deux réunions ont le même titre, ajouter l'heure au titre de section pour les distinguer.
- Une rubrique sans contenu est omise, sauf « Points de vigilance » qui affiche « Rien de notable. »
- **Réunion sans contexte :** garder l'en-tête et les participants, puis écrire uniquement : « **Contexte :** aucun échange ni compte rendu trouvé (mails 12 mois, Teams 3 mois). »
- Si Teams n'a pas pu être consulté, l'indiquer en italique sous la ligne de génération.
- Style : français, factuel, concis, sans formule d'introduction. Dates au format JJ/MM.

## Étape 7 — Enregistrer dans Obsidian

Cible : **`Mon Drive/ObsidianVault/NeomaVault/Agenda/agenda.md`** sur Google Drive (chemin local indicatif : `G:/Mon Drive/ObsidianVault/NeomaVault/Agenda/agenda.md`).

1. Retrouver le dossier `Agenda` et **vérifier la chaîne complète des parents** : `Agenda → NeomaVault → ObsidianVault → Mon Drive`. Un dossier nommé `Agenda` ne suffit pas : ne jamais écrire dans `MonVault` ni dans une copie homonyme. Si la chaîne est introuvable ou ambiguë, s'arrêter et demander le lien du dossier.
2. Si `agenda.md` existe dans ce dossier, **remplacer son contenu** (`update_file`) ; sinon, le **créer** (`create_file`) avec le dossier `Agenda` vérifié comme parent explicite. Ne jamais créer de doublon (`agenda (1).md`, etc.).
3. Enregistrer un vrai fichier texte UTF-8 `.md` (type `text/markdown`), **sans conversion en Google Doc**, pour qu'il reste lisible dans Obsidian.
4. Relire le fichier enregistré : nom, parent, début du contenu. Ne pas affirmer que la synchronisation locale Obsidian est terminée.

Si l'écriture Drive est impossible, livrer le contenu complet d'`agenda.md` dans le chat et expliquer ce qui a bloqué.

## Étape 8 — Réponse finale

Un bilan court dans le chat, sans recopier la fiche :
- nombre de réunions traitées, avec contexte, sans contexte ;
- nombre de réunions appuyées sur un compte rendu ;
- les 3 points de vigilance les plus importants de la semaine, une ligne chacun ;
- sources indisponibles (Teams, SharePoint) s'il y en a ;
- le lien vers `agenda.md`.
