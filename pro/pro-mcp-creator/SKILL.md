---
name: "pro-mcp-creator"
description: "Crée un squelette de serveur MCP (Python MCPServer ou TypeScript) avec outils, ressources, tests et configuration client. À utiliser pour « crée un serveur MCP », « MCP creator », « nouveau connecteur MCP »."
---

# MCP creator : création d'un serveur MCP

Objectif : produire un serveur MCP minimal, fonctionnel et testable, prêt à être versionné dans un dépôt Git et branché à un client (Claude Desktop, Claude Code).

## Entrée
Demander seulement ce qui manque parmi :
- le nom du serveur et ce qu'il doit faire (un ou plusieurs outils, avec leurs paramètres et leur retour attendu) ;
- les ressources ou prompts éventuels ;
- le langage : Python par défaut (SDK `mcp` 2.x, classe `MCPServer`), TypeScript si demandé ;
- le transport : `stdio` par défaut (serveur lancé localement par le client), `streamable-http` si le serveur doit tourner à distance.

Si l'utilisateur ne précise pas le langage ni le transport, prendre les valeurs par défaut et le dire en une phrase au début de la réponse.

## Méthode
1. Vérifier la documentation officielle avant d'écrire le code : les SDK évoluent vite. Pour Python, consulter https://py.sdk.modelcontextprotocol.io/ et vérifier la version installée (`pip show mcp`). Avec `mcp` 2.x, la classe est `MCPServer`, importée depuis `mcp.server.mcpserver` ; `FastMCP` de `mcp.server.fastmcp` n'existe plus dans cette version. Pour un code en `mcp` 1.x, épingler `mcp<2` et utiliser `FastMCP`. Pour TypeScript, consulter le dépôt `modelcontextprotocol/typescript-sdk`. Ne jamais affirmer une API, un import ou une version sans l'avoir vérifié dans la version installée.
2. Créer l'arborescence :
   ```
   mon-mcp-server/
   ├── server.py (ou src/index.ts)
   ├── pyproject.toml (ou package.json)
   ├── README.md
   ├── CHANGELOG.md
   └── tests/ (au moins un test par outil)
   ```
3. Écrire chaque outil avec :
   - un décorateur (`@mcp.tool()` en Python) ;
   - des annotations de type précises, qui servent de schéma aux paramètres ;
   - une docstring courte et exacte, qui devient la description visible par le modèle.
4. Gérer les erreurs : un outil ne doit jamais laisser remonter une trace brute. Renvoyer un message d'erreur clair et court.
5. Lire les secrets (clés d'API, jetons) uniquement depuis les variables d'environnement. Ne jamais les écrire dans le code ni dans le dépôt, et ajouter `.env` au `.gitignore`.
6. Tester :
   - `uv run mcp dev server.py` lance l'Inspector MCP pour appeler chaque outil ;
   - écrire au moins un test automatisé par outil, sans appel réseau réel quand c'est possible (mocker les dépendances externes).
7. Fournir la configuration client, par exemple pour `claude_desktop_config.json` :
   ```json
   {
     "mcpServers": {
       "mon-mcp-server": {
         "command": "uv",
         "args": ["run", "--directory", "/chemin/absolu/mon-mcp-server", "server.py"]
       }
     }
   }
   ```
   Indiquer que le chemin doit être absolu et que le client doit être redémarré.

## Contenu du README
- Ce que fait le serveur, la liste des outils avec leurs paramètres ;
- les variables d'environnement requises (sans valeurs) ;
- les commandes d'installation, de test et de lancement ;
- la configuration client.

## Versionnement (dépôt « Mes Skills »)
- Le serveur créé est un livrable séparé : ne pas le placer dans le dossier d'un skill.
- Créer un `CHANGELOG.md` au format Keep a Changelog, version initiale `0.1.0`, section « Ajouté » listant les outils.

## Règles
- Code minimal : pas d'abstraction, de classe ou de dépendance qui ne sert pas à un outil demandé.
- Fonctions en lecture seule par défaut. Toute action qui écrit, supprime ou envoie quelque chose doit être explicite dans la docstring et, si possible, demander une confirmation dans le paramètre.
- Ne pas inventer d'API tierce : si un outil appelle un service externe, demander la documentation ou l'URL du service.
- Style : français pour la documentation et les messages ; pas d'emojis ni de tirets cadratins.

## Réponse finale
Donner le chemin du dossier créé, la commande de test, le bloc de configuration client, et un point d'attention si une vérification de version n'a pas pu être faite.
