---
name: "pro-veille-informatique"
description: "Veille informatique quotidienne : scanne la presse IT francophone et anglophone, les sources officielles (CERT-FR, ANSSI, CNIL) et les blogs IA et éditeurs, puis rédige en français un résumé « Management SI / DSI » et « IA et IA générative » pour un responsable SI, enregistré dans Obsidian (coffre NeomaVault, Veille/AAAA-MM-JJ.md). À utiliser pour « /pro-veille-informatique », « veille du jour », « fais ma veille », « quoi de neuf dans l'IT », « actus DSI », « résumé de l'actualité informatique », « revue de presse tech », y compris pour l'exécution planifiée du matin, même si l'utilisateur ne cite ni Obsidian ni le skill."
metadata:
  version: "0.1.0"
---

# Veille informatique quotidienne

Chaque jour ouvré, lire l'actualité publiée depuis la dernière veille, ne garder que ce qui compte pour un responsable SI (management SI, IA), et la résumer dans une note Obsidian lisible en 5 minutes. La valeur de la veille tient à son tri : mieux vaut 8 articles qui comptent que 30 titres qu'il faut relire soi-même.

## Lecteur

Responsable SI / Head of IT dans l'enseignement supérieur (NEOMA), environ 20 ans d'expérience : transformation SI, pilotage d'équipes et de budget, marchés, ERP (Sage X3, Aurion), ITIL, agilité. Il lit la veille pour décider, anticiper et nourrir ses échanges avec la direction, pas pour suivre la technique au jour le jour. Chaque article retenu doit répondre à la question : « qu'est-ce que ça change pour un DSI ? »

## Règles

- **Ne rien inventer.** Chaque article cité a été ouvert et lu (au moins son chapeau et ses premiers paragraphes). Pas de résumé à partir du seul titre ni d'un résultat de recherche. Une date de publication invérifiable exclut l'article.
- **Résumer, ne pas recopier.** Pas de paragraphe copié d'un article ; une citation courte entre guillemets seulement si la formulation exacte compte (chiffre, déclaration).
- **Une seule écriture : la note du jour** dans `Veille/`. Rien d'autre n'est créé, modifié ni envoyé.
- **Sources inaccessibles** : les lister dans la note (« Sources non consultées ») plutôt que les remplacer en silence.

## Étape 1 — Fenêtre de veille

Fuseau Europe/Paris.
- Mardi à vendredi : les 24 dernières heures.
- Lundi : depuis vendredi matin (72 h), pour couvrir le week-end.
- Lancement manuel : depuis la dernière note présente dans `Veille/` (voir étape 5), 7 jours au maximum ; sans note précédente, 24 h.

Lire la note de veille précédente (s'il y en a une) pour ne pas reprendre un sujet déjà traité, sauf fait nouveau, qu'on signale alors comme « suite ».

## Étape 2 — Collecter

Les sources sont listées dans `references/sources.md`. Lancer en parallèle une collecte par source :

1. Ouvrir le flux RSS du site s'il en a un (souvent `/feed/`, `/rss`, lien « RSS » en pied de page), sinon la page d'actualités. Le flux donne les dates fiables et évite de charger la page d'accueil.
2. Si la page refuse l'accès automatisé, faire une recherche web limitée au domaine (`allowed_domains`) avec les mots des thèmes et l'année en cours, et ne garder que des articles datés dans la fenêtre.
3. Hacker News : ne garder que les sujets du top du jour en rapport avec les thèmes.

Ne pas multiplier les requêtes presque identiques. Noter, pour chaque source, si elle a été lue, vide sur la fenêtre, ou inaccessible.

## Étape 3 — Trier

Thèmes suivis, dans cet ordre :

1. **Management SI / DSI** : stratégie et gouvernance SI, budgets et coûts IT, organisation et métiers de la DSI, transformation numérique, ERP et grands éditeurs de gestion (Sage, SAP, Oracle, Workday), achats et marchés publics IT, licences et tarifs, souveraineté, SI de l'enseignement supérieur et du secteur public, réglementation qui touche la DSI (NIS2, DORA, RGPD).
2. **IA et IA générative** : annonces des grands acteurs (Anthropic, OpenAI, Google, Microsoft, Mistral, Meta), usages en entreprise et retours d'expérience, outils pour les équipes (Copilot, Claude, ChatGPT, Mistral Le Chat), coûts, gouvernance et AI Act, impacts sur les métiers.

Hors thèmes, une seule exception : la rubrique **« À ne pas rater »** reprend, en une ligne chacune et 5 au maximum :
- les alertes CERT-FR (rubrique « Alertes », pas les simples avis) ;
- les décisions ou recommandations CNIL et les étapes de l'AI Act ;
- les fins de support et changements majeurs d'éditeurs (Microsoft 365, Windows, Sage...) ;
- une cyberattaque d'ampleur contre un établissement d'enseignement supérieur ou une collectivité en France.
Le reste de la cybersécurité, du cloud et du matériel est ignoré : l'utilisateur ne suit pas ces thèmes.

Pour chaque article candidat :
- **Fusionner les doublons** : un même fait couvert par plusieurs sites devient une seule entrée, avec la source la plus complète en lien principal et les autres en liens secondaires. Préférer la source primaire (annonce de l'éditeur, communiqué officiel) quand elle existe.
- **Écarter** : contenus sponsorisés et publi-rédactionnels, tests de produits grand public, rumeurs non sourcées, articles hors fenêtre, tribunes sans fait nouveau.
- **Classer** par importance pour le lecteur : impact sur ses décisions (budget, contrat, conformité, organisation) > tendance de fond > annonce produit.

Garder 5 à 8 articles par thème au maximum. Un jour calme donne une note courte : ne pas combler avec des articles faibles.

## Étape 4 — Rédiger

Structure de la note :

```markdown
---
date: AAAA-MM-JJ
type: veille
fenetre: "du JJ/MM HH:MM au JJ/MM HH:MM"
tags: [veille, management-si, ia]
---

# Veille informatique du [jour JJ mois AAAA]

## L'essentiel du jour
3 à 5 phrases : les 2 ou 3 faits qui comptent le plus et pourquoi.

## À ne pas rater
- **[Type : alerte CERT-FR / CNIL / fin de support...]** fait en une ligne. [Source](lien)
(rubrique omise si rien)

## Management SI / DSI

### [Titre reformulé, informatif]
*Source · JJ/MM* — [Lire l'article](lien)

Résumé en 2 ou 3 phrases : le fait, les chiffres, qui est concerné.

**Pour un DSI :** une phrase sur l'impact concret ou la question à se poser.

(autres sources : [Site B](lien), [Site C](lien))

## IA et IA générative
(même format)

## Sources
- Lues : Site A (N articles retenus), Site B (0, rien dans la fenêtre)...
- Non consultées : Site C (accès refusé)...
```

Rédaction : français, phrases courtes, sans formule d'introduction ni conclusion. Titres reformulés en français même pour un article anglais. Dates au format JJ/MM. « Pour un DSI » est concret (« vérifier si nos licences E3 sont concernées avant le renouvellement »), jamais générique (« à suivre de près »). Une rubrique de thème vide affiche « Rien de notable dans la fenêtre. »

## Étape 5 — Enregistrer dans Obsidian

Cible : **`Mon Drive/ObsidianVault/NeomaVault/Veille/AAAA-MM-JJ.md`** sur Google Drive (coffre `NeomaVault`, sans espace).

1. Charger les outils Google Drive via ToolSearch si nécessaire (`search_files`, `get_file_metadata`, `create_file`, `update_file`, `read_file_content`).
2. Retrouver le dossier `Veille` et **vérifier la chaîne des parents** : `Veille → NeomaVault → ObsidianVault → Mon Drive`. Un dossier homonyme ailleurs (autre coffre, copie) ne convient pas. Si `Veille` n'existe pas mais que `NeomaVault` est trouvé avec la bonne chaîne, créer `Veille` dedans (dossier Drive). Si `NeomaVault` est introuvable ou ambigu, s'arrêter et demander le lien du dossier (en mode planifié : livrer la note dans la réponse et signaler le blocage).
3. Pour l'étape 1, la note précédente est le fichier `AAAA-MM-JJ.md` le plus récent de `Veille/`.
4. Si la note du jour existe déjà (second lancement), **remplacer son contenu** (`update_file`) ; sinon la créer (`create_file`) avec `Veille` comme parent explicite, `contentMimeType` `text/markdown` et `disableConversionToGoogleType: true`, pour obtenir un vrai fichier `.md` lisible dans Obsidian et non un Google Doc. Ne jamais créer de doublon (`2026-11-21 (1).md`).
5. Relire le fichier enregistré : nom, dossier parent, début du contenu. Ne pas affirmer que la synchronisation Obsidian locale est faite.

Si l'écriture échoue, livrer la note complète dans la réponse et expliquer ce qui a bloqué.

## Étape 6 — Réponse finale

Un bilan court, sans recopier la note : la fenêtre couverte, le nombre d'articles retenus par thème, « l'essentiel du jour » en 3 lignes, les sources non consultées, et le lien vers la note. Si l'outil SendUserMessage est disponible (exécution planifiée), y envoyer ce même bilan.

## Exécution planifiée

La veille tourne du lundi au vendredi vers 7 h 30 (heure de Paris) via une tâche planifiée. Personne ne répond aux questions dans ce mode : ne rien demander, appliquer les règles, et signaler dans la note et le bilan tout ce qui a bloqué.

## Faire évoluer les sources

Si l'utilisateur demande d'ajouter ou de retirer une source ou un thème, modifier `references/sources.md` ou la liste de l'étape 3, et le noter dans `CHANGELOG.md`. Si une source est inaccessible plusieurs jours de suite, le signaler dans le bilan et proposer une source de remplacement plutôt que de la changer d'office.
