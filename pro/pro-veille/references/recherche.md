# Recherche web et sources officielles

Les flux RSS sont dans `config/flux.json`. Ce fichier sert aux recherches de complément et à la confirmation. Vérifier que chaque URL citée a été renvoyée par le script, la recherche ou ouverte.

## Sources officielles (suffisent seules pour politique et économie)

France : `gouvernement.fr`, `elysee.fr`, `legifrance.gouv.fr`, `journal-officiel.gouv.fr`, `assemblee-nationale.fr`, `senat.fr`, `service-public.fr`, `vie-publique.fr`, `banque-france.fr`, `insee.fr`, `conseil-constitutionnel.fr`, `conseil-etat.fr`, `interieur.gouv.fr`, `cnil.fr`, `cyber.gouv.fr`, `cert.ssi.gouv.fr`.
International : `un.org`, `europa.eu` (dont `ecb.europa.eu`), `imf.org`, `worldbank.org`, `who.int`, `usgs.gov`, `icj-cij.org`, `cisa.gov`.

## Médias reconnus

- Généralistes : Le Monde, Le Figaro, Libération, franceinfo, Ouest-France, La Croix, Le Parisien, Public Sénat, France 24, RFI, Euronews, Politico Europe, BBC, The Guardian, Al Jazeera, The New York Times, Financial Times, Les Échos, Reuters, Associated Press, AFP.
- IA et informatique : LeMagIT, Le Monde Informatique, Next, Silicon.fr, Numerama, 01net, The Register, Ars Technica, The Verge, TechCrunch, VentureBeat, MIT Technology Review, BleepingComputer, The Hacker News, Krebs on Security, ZATAZ, Neowin, Windows Central.
- Développement : GitHub Blog, Stack Overflow Blog, InfoQ, Developpez.com, blogs officiels des langages et outils (Rust, Go, .NET, TypeScript, Node.js, VS Code, JetBrains, Docker, Cloudflare).
- 3D : Blender, BlenderNation, CG Channel, 80 Level, Prusa, Hackaday, Godot.

Un site dont le flux est désactivé dans `config/flux.json` reste citable s'il apparaît dans une recherche et que sa page s'ouvre.

## Requêtes de départ (ajouter le mois et l'année)

| Catégorie | Exemples |
|---|---|
| Politique | « Assemblée nationale vote », « gouvernement décret Journal officiel », « sommet G7 OR G20 OR UE », « conflit cessez-le-feu » |
| Économie | « BCE taux directeur », « Banque de France conjoncture », « inflation Insee », « budget loi de finances », « marchés Bourse » |
| IA | « nouveau modèle IA annonce », « AI agents announcement », « AI Act application » |
| Informatique | « CERT-FR avis », « vulnerability exploited CVE », « Microsoft 365 nouveautés », « Windows update known issue », « cyberattaque » |
| Développement | « release notes », « Python OR Rust OR TypeScript OR .NET release », « GitHub Copilot update » |
| 3D | « Blender release », « impression 3D nouveauté », « Godot OR Unreal OR Unity release », « Raspberry Pi OR Arduino annonce » |

## Faits à forte valeur

- Journal officiel et décrets : source officielle suffisante.
- CVE exploitée : citer `cisa.gov` (catalogue KEV) ou le CERT-FR, puis un article qui explique l'exploitation.
- Tech : un communiqué ou billet de l'éditeur ou du projet vaut source primaire.
