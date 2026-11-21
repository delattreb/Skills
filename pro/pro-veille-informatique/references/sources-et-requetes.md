# Sources et requêtes de départ

Ces listes orientent la recherche ; elles ne sont pas exhaustives. Vérifier chaque fois que l'URL citée a bien été renvoyée par la recherche, par le script ou ouverte.

Tests d'accès faits le 21/11/2026 depuis l'environnement cloud de la veille planifiée : la plupart des sites d'actualité ne peuvent **pas être ouverts directement** (réseau limité), mais ils restent **interrogeables par la recherche web** avec `allowed_domains`. La méthode de collecte repose donc sur trois piliers, dans cet ordre : flux lus par script, recherche web restreinte aux domaines fiables, recherche web libre en complément.

## 1. Flux lus directement (script `scripts/flux_veille.py`)

| Source | Contenu | Accès |
|---|---|---|
| Feuille de route Microsoft 365 (RSS officiel) `https://www.microsoft.com/releasecommunications/api/v2/m365/rss` | Nouveautés Microsoft 365, Teams, Exchange, SharePoint, Copilot, Edge, Intune, avec statut (In development, Rolling out, Launched) et date | Ouvrable |
| Catalogue CISA des vulnérabilités exploitées (KEV) `https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json` | Vulnérabilités dont l'exploitation est confirmée, date d'ajout, éditeur, produit | Ouvrable |
| Newsroom Anthropic `https://www.anthropic.com/news` | Annonces Claude | Ouvrable |

Pour la feuille de route Microsoft 365, ne retenir que ce qui touche l'environnement de NEOMA (Teams, Exchange, Outlook, SharePoint, OneDrive, Copilot, Entra, Intune, Edge, Planner) ; ignorer Dynamics 365 et les clouds GCC, GCC High et DoD. Pour le KEV, citer la page officielle `https://www.cisa.gov/known-exploited-vulnerabilities-catalog` et compléter par une recherche sur le CVE pour trouver un article qui explique l'exploitation.

## 2. Recherche web restreinte aux domaines fiables (`allowed_domains`)

Lancer pour chaque catégorie au moins une recherche avec la liste de domaines ci-dessous, avec la date du jour ou de la veille dans la requête (par exemple « 20 novembre 2026 » ou « November 20 2026 »). Ces listes ont été testées : le moteur les accepte.

| Catégorie | `allowed_domains` |
|---|---|
| Presse IT française (toutes catégories) | `lemagit.fr`, `lemondeinformatique.fr`, `silicon.fr`, `next.ink`, `usine-digitale.fr`, `cio-online.com`, `itforbusiness.fr`, `journaldunet.com`, `channelnews.fr`, `linformaticien.com` |
| IA et outils IA | `openai.com`, `anthropic.com`, `blog.google`, `deepmind.google`, `mistral.ai`, `ai.meta.com`, `microsoft.com`, `techcrunch.com`, `venturebeat.com`, `9to5google.com`, `theregister.com` |
| SI de l'enseignement supérieur | `campusmatin.com`, `letudiant.fr`, `newstank.fr`, `enseignementsup-recherche.gouv.fr`, `renater.fr`, `amue.fr`, `insidehighered.com`, `educause.edu`, `timeshighereducation.com`, `edtechmagazine.com`, `universityworldnews.com` |
| Microsoft 365 et cloud | `techcommunity.microsoft.com`, `learn.microsoft.com`, `azure.microsoft.com`, `workspaceupdates.googleblog.com`, `blogs.windows.com`, `office365itpros.com`, `neowin.net`, `windowscentral.com`, `bleepingcomputer.com` |
| Cybersécurité | `cert.cyber.gouv.fr`, `cert.ssi.gouv.fr`, `cyber.gouv.fr`, `cisa.gov`, `msrc.microsoft.com`, `bleepingcomputer.com`, `securityweek.com`, `therecord.media`, `thehackernews.com`, `helpnetsecurity.com`, `darkreading.com` |
| Réglementation et données | `cnil.fr`, `edpb.europa.eu`, `digital-strategy.ec.europa.eu`, `commission.europa.eu`, `legifrance.gouv.fr`, `numerique.gouv.fr`, `cyber.gouv.fr`, `dalloz-actualite.fr`, `next.ink`, `lemagit.fr` |
| Infra, réseau et poste de travail | `learn.microsoft.com`, `support.microsoft.com`, `blogs.windows.com`, `bleepingcomputer.com`, `neowin.net`, `windowscentral.com`, `theregister.com`, `lemondeinformatique.fr`, `lemagit.fr` |
| Marché et éditeurs | `lemondeinformatique.fr`, `lemagit.fr`, `silicon.fr`, `channelnews.fr`, `journaldunet.com`, `theregister.com`, `techcrunch.com`, `cio-online.com` |
| Geekerie | `raspberrypi.com`, `hackaday.com`, `cnx-software.com`, `blender.org`, `blendernation.com`, `krita.org`, `tomshardware.com`, `creativebloq.com`, `80.lv`, `espressif.com`, `arduino.cc` |

**Domaines refusés par le moteur de recherche** (une requête qui en contient un échoue en entier, erreur 400 « not accessible to our user agent ») : `01net.com`, `zdnet.fr`, `frandroid.com`, `lesnumeriques.com`, `numerama.com`, `arstechnica.com`, `reuters.com`, `theverge.com`, `lemonde.fr`, `lesechos.fr`. Ne jamais les mettre dans `allowed_domains`. Si un autre domaine provoque cette erreur, le retirer de la liste, relancer, et le signaler dans le bilan.

Recherches à fort rendement constatées :
- « CERT-FR avis [date] » sur `cert.cyber.gouv.fr` : liste les avis du jour avec leur référence et leur URL (Moodle, Citrix, VMware, GitLab…).
- « vulnerability exploited [date] » sur les domaines cybersécurité : exploitation confirmée, avec CVE.
- « actualité informatique [date] » sur la presse IT française : articles du jour du Monde Informatique, de LeMagIT, de Next et du JDN.

## 3. Sources acceptées et exclues

- **Sources primaires (acceptées)** : sites, blogs officiels et communiqués des éditeurs ; organismes publics (ministères, CNIL, ANSSI, CERT-FR, CISA, Commission européenne, Journal officiel) ; communiqués de l'établissement concerné.
- **Médias reconnus (acceptés)** : LeMagIT, Le Monde Informatique, CIO Online, Silicon.fr, Next, Usine Digitale, JDN, IT for Business, Channelnews, L'Informaticien, EducPros (L'Étudiant), Campus Matin, News Tank, Inside Higher Ed, EDUCAUSE Review, Times Higher Education, EdTech Magazine, TechCrunch, VentureBeat, The Register, 9to5Google, BleepingComputer, SecurityWeek, The Record, The Hacker News, Help Net Security, Dark Reading, Neowin, Windows Central, Office 365 for IT Pros ; pour la Geekerie : Hackaday, Tom's Hardware, CNX Software, BlenderNation, 80.lv, Creative Bloq. 01net, ZDNet, Les Échos, Le Monde, Reuters, The Verge et Ars Technica restent fiables, mais le moteur ne les interroge pas : ne les citer que s'ils apparaissent dans une recherche libre.
- **Exclues comme seule source** : agrégateurs et « trackers » de sorties d'IA, sites de digests générés automatiquement (y compris les newsletters Substack ou les pages « AI news du jour »), blogs personnels ou de revendeurs, forums, réseaux sociaux, sites de reprise sans rédaction identifiée (par exemple armees.com pour les avis CERT-FR), revendications de groupes criminels non reprises par un média reconnu. Elles peuvent servir de piste pour trouver la source primaire, jamais de preuve.

## 4. Requêtes libres de complément

Ajouter le mois et l'année en cours ; varier français et anglais. À utiliser après les recherches restreintes, pour combler une catégorie vide.

| Catégorie | Exemples de requêtes |
|---|---|
| IA | « nouveau modèle IA annonce », « Copilot nouveautés », « AI agents enterprise announcement », « IA générative enseignement supérieur » |
| Enseignement sup. | « école de commerce système d'information », « EdTech enseignement supérieur annonce », « LMS higher education update », « Moodle release » |
| Microsoft 365 / cloud | « Microsoft 365 nouveautés », « Microsoft Teams change rollout », « Google Workspace update », « panne Microsoft 365 » |
| Cybersécurité | « cyberattaque université », « university cyberattack », « école cyberattaque », « hameçonnage campagne » |
| Réglementation | « CNIL sanction », « AI Act application », « NIS2 transposition », « RGAA accessibilité obligation », « eIDAS 2 » |
| Infra / poste | « Windows update known issue », « end of support Microsoft », « Intune new features » |
| Marché / éditeurs | « Microsoft licensing price change », « rachat éditeur logiciel », « hausse prix licences », « Broadcom VMware licences » |
| Geekerie | « Raspberry Pi news », « Arduino new board », « ESP32 announcement », « Blender release », « Krita release », « Procreate update », « tablette graphique nouvelle » |

## Indices de pertinence pour NEOMA

| Indice | Pertinence |
|---|---|
| Change ce que voient ou font les utilisateurs (étudiants, enseignants, personnel) | Haute |
| Vulnérabilité exploitée sur un produit utilisé, ou attaque dans le secteur | Haute |
| Touche le coût des licences, un contrat, une fin de support ou une obligation légale | Haute |
| Concerne une école de commerce, une université ou un éditeur utilisé dans le secteur | Haute |
| Nouvelle capacité IA utilisable à court terme (pédagogie, productivité, support) | Moyenne à haute |
| Annonce lointaine, préversion limitée aux États-Unis, levée de fonds sans produit | Basse : ne retenir que si rien de plus important |

## Indices d'intérêt pour la Geekerie

| Indice | Intérêt |
|---|---|
| Nouvelle version majeure d'un logiciel (Blender, Krita, Procreate…) ou nouvelle carte (Raspberry Pi, Arduino, ESP32) | Haut |
| Fonctionnalité qui change la façon de peindre, modéliser ou prototyper | Haut |
| Baisse ou hausse de prix notable, rupture de stock, fin de vie d'un produit | Moyen |
| Projet communautaire remarquable publié par un média reconnu | Moyen |
| Bêta mineure, correctif sans nouveauté, contenu sponsorisé | Bas : écarter |
