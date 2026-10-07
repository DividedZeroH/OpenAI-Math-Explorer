import re

def set_english_fallbacks():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace specific fallback texts in the HTML
    content = re.sub(r'>\s*Catálogo\s*<', '>Catalog<', content)
    content = re.sub(r'>\s*Grafo de Relaciones\s*<', '>Relationship Graph<', content)
    content = re.sub(r'>\s*Solo con Lean\s*<', '>Only with Lean<', content)

    # Note: 'Todas las disciplinas', 'Cargando datos...', 'Fuentes y Referencias' were already replaced
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    set_english_fallbacks()
