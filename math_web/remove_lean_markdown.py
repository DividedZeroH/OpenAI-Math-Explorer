import json
import re

def clean_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for family in data:
        if 'description' in family and family['description']:
            # Use regex to strip out "([Lean](...))"
            # e.g., " ([Lean](lean/docs/005.md))"
            cleaned = re.sub(r'\s*\(\[Lean\]\([^)]+\)\)', '', family['description'])
            family['description'] = cleaned

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    clean_data()
