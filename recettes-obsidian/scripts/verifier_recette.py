"""Valider une fiche locale : python verifier_recette.py fiche.md --vault coffre."""
import argparse
import datetime
import pathlib
import re
import sys
import uuid
import yaml


def validate(path, vault=None):
    text = path.read_text(encoding='utf-8-sig')
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return ['Frontmatter YAML absent ou non fermé.']
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == '---'), None)
    if end is None:
        return ['Frontmatter YAML absent ou non fermé.']
    parts = ['', '\n'.join(lines[1:end]), '\n'.join(lines[end + 1:])]
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        return [f'YAML invalide : {exc}']
    if not isinstance(data, dict):
        return ['Le YAML doit être une table de propriétés.']
    errors = []
    for key in ('type', 'schema_version', 'id', 'titre', 'categorie', 'portions',
                'preparation_min', 'cuisson_min', 'repos_min', 'difficulte',
                'statut', 'sources', 'image', 'image_type', 'tags',
                'date_creation', 'date_modification', 'skill_version'):
        if key not in data:
            errors.append(f'Champ absent : {key}')
    if data.get('type') != 'recette' or type(data.get('schema_version')) is not int or data.get('schema_version') != 1:
        errors.append('Type ou version de schéma incorrect.')
    try:
        uuid.UUID(str(data.get('id')))
    except ValueError:
        errors.append('UUID invalide.')
    if not isinstance(data.get('titre'), str) or not data['titre'].strip():
        errors.append('Titre vide.')
    for key in ('preparation_min', 'cuisson_min', 'repos_min'):
        value = data.get(key)
        if value is not None and (type(value) is not int or value < 0):
            errors.append(f'{key} doit être un entier positif ou nul, ou null.')
    portions = data.get('portions')
    if portions is not None and (type(portions) not in (int, float) or not 0 < portions < float('inf')):
        errors.append('Portions invalides.')
    for key, allowed in [('categorie', (None, 'Plat', 'Dessert')),
                         ('difficulte', (None, 'Facile', 'Moyenne', 'Difficile')),
                         ('statut', ('brouillon', 'complete'))]:
        if data.get(key) not in allowed:
            errors.append(f'Valeur incorrecte : {key}')
    for key in ('sources', 'tags'):
        value = data.get(key)
        if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
            errors.append(f'{key} doit être une liste de chaînes.')
    if isinstance(data.get('tags'), list) and 'recette' not in data['tags']:
        errors.append('Tag recette absent.')
    for key in ('date_creation', 'date_modification'):
        try:
            datetime.date.fromisoformat(str(data.get(key)))
        except ValueError:
            errors.append(f'Date invalide : {key}')
    if '{{' in text:
        errors.append('Variables de modèle non remplacées.')
    image = data.get('image')
    if image is None:
        if data.get('statut') == 'complete':
            errors.append('Image obligatoire pour une fiche complète.')
        if '![[' in parts[2]:
            errors.append('Image intégrée alors que le champ image est null.')
    elif not isinstance(image, str) or not image.strip():
        errors.append('Image invalide : utiliser un chemin relatif ou null pour un brouillon.')
    else:
        relative = pathlib.PurePosixPath(image.replace('\\', '/'))
        if relative.is_absolute() or '..' in relative.parts or ':' in image:
            errors.append('Le chemin image doit rester relatif au coffre.')
        elif vault:
            root = vault.resolve()
            target = (root / str(relative)).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                errors.append('Fichier image absent ou extérieur au coffre.')
        if f'![[{image}]]' not in parts[2]:
            errors.append('Image non intégrée dans le corps de la fiche.')
    section = re.search(r'^## Ingrédients\s*\n(.*?)(?=^## |\Z)', parts[2], re.M | re.S)
    if not section:
        errors.append('Section Ingrédients absente.')
    else:
        rows = [line.strip() for line in section.group(1).splitlines() if line.strip() and not line.strip().startswith('<!--')]
        def cells(row):
            return re.split(r'(?<!\\)\|', row.strip().strip('|'))
        expected = ['Ingrédient', 'Quantité', 'Unité', 'Précision']
        if len(rows) < 3 or [c.strip() for c in cells(rows[0])] != expected:
            errors.append('Tableau ingrédients obligatoire : Ingrédient | Quantité | Unité | Précision.')
        else:
            if len(cells(rows[1])) != 4 or not all(re.fullmatch(r':?-{3,}:?', c.strip()) for c in cells(rows[1])):
                errors.append('Séparateur du tableau ingrédients invalide.')
            if any(not row.startswith('|') or not row.endswith('|') or len(cells(row)) != 4 for row in rows[2:]):
                errors.append('Chaque ingrédient doit occuper une ligne de tableau à quatre colonnes.')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fiche', type=pathlib.Path)
    parser.add_argument('--vault', type=pathlib.Path)
    args = parser.parse_args()
    try:
        issues = validate(args.fiche, args.vault)
    except OSError as exc:
        issues = [str(exc)]
    print('\n'.join(issues) if issues else 'Structure valide ; vérifier séparément le contenu culinaire et l’image.')
    sys.exit(bool(issues))
