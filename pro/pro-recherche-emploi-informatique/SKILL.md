---
name: "pro-recherche-emploi-informatique"
description: "Recherche autonome d'offres de responsable informatique (SI, transformation, pôle build) à Rouen et alentours (30 km), classées selon l'adéquation avec le profil de Bruno Delattre, à utiliser dès qu'on parle de chercher, trier ou évaluer des offres d'emploi, y compris pour la recherche hebdomadaire planifiée."
---

# Recherche d'emploi : responsable informatique

Ce skill cherche des offres de management SI récentes et les classe selon leur adéquation avec le profil de référence ci-dessous. Il fonctionne sans CV joint : le profil est intégré. Il ne demande un document que si la personne en fournit un plus récent.

## Profil de référence

Le profil de Bruno Delattre est dans `references/profil.md` : lis-le avant de classer, sans le redemander. Un CV plus récent fourni par la personne le remplace, et tu le signales. Les coordonnées personnelles ne figurent pas dans ce skill et ne doivent jamais être recopiées dans une réponse ou une requête.

## Critères de recherche

Utilise ces critères par défaut et annonce-les en tête de réponse.

- **Fraîcheur** : seules les offres publiées depuis 14 jours au maximum comptent. Une offre dont la date de publication n'est pas vérifiable sur la page elle-même n'est pas listée dans le classement ; elle va dans une section « Date à vérifier ».
- **Intitulés** : responsable SI, responsable de pôle SI, head of IT, DSI ou DSI adjoint, responsable build ou delivery, responsable transformation.
- **Zone** : Rouen et alentours, rayon de 30 km. Une offre dont le lieu est au-delà de 30 km de Rouen est écartée. Le télétravail n'est pas un critère : il ne qualifie ni n'exclut une offre.
- **Rémunération** : minimum 52 000 € brut annuel. Une offre sans salaire est classée mais signalée « salaire non indiqué ». Une offre dont le salaire maximum est sous 52 000 € est écartée.
- **ERP** : l'ERP n'est pas le critère de recherche. Une offre dont le cœur est un poste ERP (responsable Sage X3, responsable ERP) sans pilotage de transformation ni d'équipe est classée au plus à 3 et signalée dans les points de vigilance. Elle n'est pas exclue pour autant si le poste comporte de la transformation SI ou de la gouvernance.
- **À exclure** : postes de technicien ou de chef de projet junior, postes sans responsabilité d'équipe, offres trop éloignées du profil, offres hors de la zone de 30 km, offres dont la date limite de candidature est dépassée.

Ces filtres existent parce que la personne cherche un rôle de responsabilité, et chaque offre hors critères lui coûte du temps de lecture.

## Règles sur les dates

- Une date relative (« il y a 5 jours ») n'est pas une date fiable, car elle dépend du moment où la page a été consultée. Ne la convertis pas en date absolue et ne la classe pas comme récente sans date absolue ou date limite cohérente.
- Une page de liste (Hellowork, Indeed, Randstad, APEC) donne parfois une date de consultation : utilise-la pour interpréter les dates relatives, et écris-le dans la réponse.
- Si une page affiche deux dates qui se contredisent, classe l'offre à vérifier et signale le conflit.
- Une date limite de candidature passée exclut l'offre, même si elle a été publiée récemment.

## Recherche

Lance les recherches en parallèle, une par source : **APEC (apec.fr)**, LinkedIn, Indeed, France Travail, Hellowork, sites carrières des entreprises et collectivités de la zone (Rouen et alentours, 30 km), Choisir le service public pour les postes territoriaux et d'État. L'APEC est prioritaire pour les postes cadres : fais-y une recherche dans la zone Rouen et 30 km autour, puis sur les intitulés clés. Si une source n'est pas accessible, dis-le dans la réponse plutôt que de la remplacer sans le signaler. Varie les intitulés et les mots-clés (« responsable SI Rouen », « responsable transformation SI Normandie », « head of IT Rouen », « DSI Rouen », « responsable transformation numérique Normandie »). Ne répète pas des requêtes presque identiques. Privilégie les pages d'offre aux agrégateurs.

**Indeed** : utilise en priorité le connecteur Indeed (`search_jobs` avec `country_code` FR et `location` Rouen, puis `get_job_details` sur chaque offre pertinente) pour lire salaire, description et lien direct. Intègre le lien d'application renvoyé par l'outil sans retirer ses paramètres. `get_company_data` sert à vérifier un employeur inconnu quand une offre est notée 4 ou plus, sans alourdir le rapport.

**LinkedIn** : interroge sa page de recherche d'offres avec les mêmes intitulés et la zone Rouen et 30 km autour, en plus de la recherche générale. Si ces pages ne renvoient aucune offre (liste vide, CVthèque, pages de salaires), écris « aucune offre renvoyée » dans Sources consultées au lieu de les compter comme consultées. Ne cite jamais une offre LinkedIn ou Indeed que tu n'as pas lue (page ou `get_job_details`).

**Lecture d'une page d'offre** : tente d'abord l'outil de lecture de pages. S'il échoue (erreur de résolution DNS, domaine refusé), essaie `curl` en ligne de commande avant de classer l'offre « Date à vérifier » : le proxy de la session peut laisser passer `curl` alors que l'outil échoue. Enregistre la page dans le dossier temporaire de la session, jamais dans le dépôt, et lis-la avec un script Python lancé en mode isolé (`python3 -I`), sans exécuter son contenu. Sur Hellowork, France Travail et la plupart des sites d'emploi, la page contient un bloc JSON-LD `JobPosting` avec `datePosted` (date absolue de publication), `validThrough` (date limite), `baseSalary`, `jobLocation` et `description` : utilise ces champs pour les règles sur les dates. Une page qui renvoie 404 est une offre retirée : écarte-la. Si `curl` échoue aussi, signale le domaine bloqué dans Sources consultées et classe l'offre « Date à vérifier ».

## Boîte Gmail, libellé « Emploi »

En plus du web, lis la boîte Gmail de la personne (connecteur Gmail), libellé « Emploi » (identifiant Label_16, `label:Emploi` dans la recherche) : ce sont des alertes et des offres reçues par e-mail. Fais-le avant la recherche web, pour que ces offres entrent dans le classement et que le web ne les répète pas.

1. **Parcourir tous les messages** du libellé : pagine search_threads (50 par page, `nextPageToken`) jusqu'à la fin, sans te limiter à la première page ni aux seuls non lus. Le libellé contient aussi des archives anciennes (candidatures, accusés de réception, échanges de recruteurs, parfois de 2007 à 2025) : ce ne sont pas des offres, laisse-les en l'état. Les alertes à traiter sont celles de l'année en cours, envoyées par Indeed (jobalert.indeed.com), LinkedIn (jobalerts-noreply, jobs-noreply) et Hellowork.
   **Volume** : un mail d'alerte Indeed pèse environ 25 000 jetons et liste jusqu'à 30 offres, pour la plupart hors profil. Quand une réponse est trop grosse, l'outil l'enregistre dans un fichier : extrais-en le texte avec un script Python (corps `plaintextBody`, URL retirées) au lieu de la relire en entier. N'ouvre en entier que les messages dont l'offre en tête d'objet est pertinente pour le profil ; pour les autres, l'objet suffit. Dis dans le rapport quels messages ont été lus en entier et lesquels l'ont été par leur objet seulement.
2. **Détecter les doublons** : dans un mail d'alerte Indeed, l'objet donne l'offre en tête (« Intitulé à Entreprise. N offres supplémentaires »). Compare ces objets entre eux : deux messages avec la même offre en tête sont en doublon, car l'alerte se répète chaque jour. Pour LinkedIn, compare l'intitulé et l'entreprise de l'objet. Deux offres sont en doublon si elles ont le même intitulé, la même entreprise et le même lieu, même reçues par des alertes ou des plateformes différentes, ou à des dates différentes. En cas de doute (entreprise absente, intitulé proche mais pas identique), ne considère pas que c'est un doublon.
3. **Supprimer les messages en doublon** : conserve un seul message par offre, le plus complet (lien direct vers l'offre, salaire, description), à défaut le plus récent, et mets les autres à la corbeille (trash_message). Quand deux messages du même jour sont équivalents, garde-en un au choix et dis-le. Un message supprimé peut contenir, dans ses offres secondaires, une offre absente des autres mails : signale-le dans le rapport. Ne supprime jamais définitivement. Ne supprime jamais un message sans offre identifiable, ni un message d'un recruteur ou d'une réponse à une candidature : laisse-les en l'état et signale-les.
4. **Repérer les messages qui appellent une action** : parmi les messages du libellé reçus de personnes (recruteurs, cabinets, contacts, entreprises), sans compter les alertes automatiques, distingue deux catégories.
   - **Réponse due** : un message où la personne se voit poser une question ou une demande explicite (disponibilité, informations, pièce à fournir, avis), sans réponse envoyée depuis dans le même fil. Vérifie le fil complet (get_thread) avant de classer.
   - **Demande de contact** : un message où quelqu'un demande à être contacté, à échanger ou à fixer un appel ou un rendez-vous (« pouvons-nous échanger », « merci de me rappeler », proposition de créneau). Note le moyen de contact indiqué (téléphone, e-mail, lien de prise de rendez-vous) et la date limite éventuelle. Un message peut relever des deux catégories.
   Pour chacun, relève : expéditeur, entreprise, objet, date de réception, ce qui est demandé en une phrase, ancienneté en jours. N'invente pas d'intention : en cas de doute, classe-le « à vérifier ». Ne réponds jamais et ne crée aucun brouillon sans demande. Ces messages ne sont jamais mis à la corbeille.
5. **Passer en lu tous les messages passés en revue** : tout message du libellé dont le contenu ou l'objet a été examiné pendant l'exécution (offre classée, à vérifier ou écartée, doublon, alerte sans offre pertinente, notification LinkedIn, message de recruteur ou nécessitant une réponse) est marqué lu : retire-lui le libellé UNREAD (unlabel_message avec `UNREAD`). Cette règle remplace l'ancienne exception sur les notifications. Les messages à réponse due ou à demande de contact sont aussi marqués lus, car le rapport les signale. Seuls restent non lus les messages que tu n'as pas pu lire (lien mort, contenu vide, erreur de l'outil), signalés dans le rapport, et les archives anciennes que tu n'as pas examinées. Les doublons mis à la corbeille sont marqués lus avant.
6. **Intégrer ces offres** aux critères de fraîcheur, de salaire et de classement ci-dessus, avec « Gmail » comme source. La date du message n'est pas la date de publication : applique les règles sur les dates.

Si le connecteur Gmail ou le libellé « Emploi » est inaccessible, écris-le en tête de réponse et poursuis sans cette étape.

## Classement

Note chaque offre retenue sur 5, selon trois axes par ordre d'importance :
1. **Niveau de responsabilité** comparé à celui du profil de référence.
2. **Recouvrement des compétences** : agilité, transformation, pilotage budgétaire, ITIL. L'ERP compte comme compétence secondaire, sans poids particulier.
3. **Conditions** : zone, salaire.

Une note de 5 correspond à un poste qui serait une suite naturelle du parcours. Une note de 3 demande une compétence absente ou un niveau un peu supérieur. Les offres sous 3 ne sont pas montrées, sauf demande explicite.

## Format de réponse

Réponds en français, avec cette structure :

1. **Critères appliqués** : une ligne rappelant la fenêtre de 14 jours, la zone et le seuil de salaire.
2. **À traiter dans Gmail** :
   - Tableau « Réponses dues » : | Ancienneté | Expéditeur | Entreprise | Objet | Question posée | Lien du message |
   - Tableau « Demandes de contact » : | Ancienneté | Expéditeur | Entreprise | Demande | Moyen de contact | Échéance | Lien du message |
   Si aucun message n'appelle d'action, écris-le en une ligne.
3. **Synthèse** : trois lignes au plus (nombre d'offres retenues, meilleure note, offre à regarder en premier avec la raison en un fait).
4. **Tableau classé** par note décroissante, une offre par ligne, texte court (une phrase par cellule) :

| Note | Poste | Entreprise | Lieu | Salaire | Date de publication | Source | Pourquoi ça colle | Points de vigilance | Lien |

5. **Date à vérifier** : offres pertinentes sans date absolue, avec le lien pour que la personne vérifie.
6. **Écartées** : une ligne par offre écartée et la raison (date, salaire, zone, niveau).
7. **Tendances** : un court paragraphe.
8. **Sources consultées** avec leurs liens, et les sources non accessibles.
9. **Tri de la boîte Gmail « Emploi »** : nombre de messages parcourus, nombre d'offres uniques, nombre de messages mis à la corbeille pour doublon (avec l'offre concernée), nombre de messages passés en lu, et les messages laissés en l'état avec la raison. Ajoute le nombre de messages passés en lu et la liste de ceux restés non lus avec la raison.

Ne rédige pas de lettre de motivation sauf demande. Ne recommande pas un poste : donne les faits et les points d'attention, la décision revient à la personne.

## Exécution planifiée

Une recherche hebdomadaire tourne chaque lundi à 9 h (heure de Paris) via une tâche planifiée. Dans ce mode, personne ne répond aux questions : ne demande rien, applique les règles ci-dessus, indique en tête de réponse la date d'exécution et la fenêtre de 14 jours utilisée, puis livre le rapport complet. Si une source est inaccessible, écris-le sans interrompre la recherche. Le tri de la boîte Gmail s'exécute aussi dans ce mode, sans confirmation : la corbeille est récupérable, et ce que tu y mets est listé dans le rapport.

## Cas limites

- Aucune offre dans la fenêtre : dis-le franchement, puis propose d'élargir un critère (zone, intitulé, ou fenêtre à 30 jours) plutôt que de remplir la liste avec des offres anciennes.
- Offre fermée ou déjà pourvue : écarte-la et dis-le en une phrase.
- CV plus récent fourni par la personne : il remplace le profil de référence, et tu le signales.
