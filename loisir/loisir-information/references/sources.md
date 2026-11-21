# Sources et requêtes de départ

La liste active des sources (médias, sources officielles, activation, volet) est dans `config/sources.json`, qui fait foi. Les listes ci-dessous sont des repères ; elles ne sont pas exhaustives. Vérifier chaque fois que l'URL citée a bien été renvoyée par la recherche ou ouverte.

## Médias reconnus

Un fait confirmé par **deux médias reconnus indépendants** entre dans le point (ils ne doivent pas se citer l'un l'autre : vérifier que le second a bien son propre reportage ou sa propre dépêche).

- **Internationaux** : Reuters, AFP, Associated Press, BBC News, The Guardian, Le Monde (rubrique international), Financial Times, The New York Times, Al Jazeera (rubrique internationale), France 24, RFI.
- **Français** : AFP, Le Monde, Le Figaro, Les Échos, franceinfo, Libération, Le Parisien, La Croix, Ouest-France, Le Point, L'Obs, Mediapart, Politico Europe (édition France).

## Sources officielles (confirmation seule suffisante)

- **France** : Journal officiel (journal-officiel.gouv.fr, Légifrance), gouvernement.fr, elysee.fr, Assemblée nationale, Sénat, service-public.fr, Banque de France, Insee, Conseil constitutionnel, Conseil d'État, autorités de régulation (ARCEP, AMF, CNIL), Santé publique France, Météo-France pour les alertes.
- **International** : ONU (un.org, communiqués et comptes rendus), Union européenne (europa.eu, Journal officiel de l'UE), G7 et G20 (communiqués), Banque centrale européenne, Fonds monétaire international, Banque mondiale, OMS (who.int), Agences de sécurité civile et sismologie (USGS, EMSC) pour les séismes.

## Exclues comme seule source

Agrégateurs de nouvelles, sites de digest générés automatiquement, blogs personnels, forums, réseaux sociaux, comptes anonymes, sites de désinformation connus. Ils peuvent servir de piste pour trouver la source primaire, jamais de preuve.

## Limites de l'outil de recherche

- Le filtre `allowed_domains` est refusé pour Reuters, AP, BBC, Le Monde, AFP, The Guardian et RFI : ne pas l'utiliser pour ces médias. Recherche sans filtre, puis lecture des URL renvoyées.
- Les dépêches d'agence sont souvent reprises sur des sites régionaux ou nationaux : la reprise nommée de l'agence fait foi (voir `config/sources.json`).

## Requêtes de départ

Ajouter le mois et l'année en cours ; varier français et anglais.

| Volet | Exemples de requêtes |
|---|---|
| International | « breaking news world today », « international news [mois année] », « sommet international annonce », « ONU résolution [mois année] », « economy markets news today », « conflit actualité [mois année] » |
| France | « actualité France aujourd'hui », « gouvernement annonce [mois année] », « Journal officiel décret publié », « loi adoptée Parlement », « Banque de France annonce », « actualité économique France [mois année] » |
| Échéances | « entrée en vigueur [mois année] », « date limite [mois année] France », « élections [année] calendrier » |

## Indices d'importance

| Indice | Importance |
|---|---|
| Touche de nombreuses personnes ou un pays entier, ou change une règle applicable à tous | Haute |
| Décision officielle (texte publié, sommet, décision d'une institution) | Haute |
| Effet économique mesurable (taux, prix, emploi, marchés) | Haute |
| Événement inédit ou catastrophe avec bilan confirmé | Haute |
| Déclaration sans décision ni effet concret | Faible |
| Sujet de niche sans portée au-delà de son milieu | Faible |
