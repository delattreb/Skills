# Changelog — pro-mcp-creator

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions [SemVer](https://semver.org/lang/fr/).
Chaque version publiée est marquée par un tag Git `pro-mcp-creator-vX.Y.Z`.

## [Non publié]
### Ajouté
- Première version : création d'un squelette de serveur MCP (Python FastMCP par défaut, TypeScript sur demande).
- Outils, ressources et prompts avec annotations de type et docstrings.
- Tests par outil, lancement de l'Inspector MCP, bloc de configuration pour Claude Desktop.
- README et CHANGELOG générés, secrets lus uniquement depuis les variables d'environnement.

### Modifié
- Python : la classe est `MCPServer` (SDK `mcp` 2.x, `mcp.server.mcpserver`) au lieu de `FastMCP`, qui n'existe plus dans cette version. Vérification de la version installée imposée avant d'écrire le code.
