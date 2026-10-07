import re

def fix_i18n():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add data-i18n to buttons
    content = content.replace('id="btnTabList" onclick="switchTab(\'list\')" class="', 'id="btnTabList" onclick="switchTab(\'list\')" data-i18n="tab_list" class="')
    content = content.replace('id="btnTabGraph" onclick="switchTab(\'graph\')" class="', 'id="btnTabGraph" onclick="switchTab(\'graph\')" data-i18n="tab_graph" class="')

    # 2. Add to ES dictionary
    content = content.replace("'sources_title': 'Fuentes y Referencias',", "'sources_title': 'Fuentes y Referencias',\n                'tab_list': 'Catálogo',\n                'tab_graph': 'Grafo de Relaciones',")

    # 3. Add to EN dictionary
    content = content.replace("'sources_title': 'Sources & References',", "'sources_title': 'Sources & References',\n                'tab_list': 'Catalog',\n                'tab_graph': 'Relationship Graph',")

    # 4. Add to PT dictionary
    # Wait, PT dictionary ends slightly differently. Let's find it.
    # It has 'sources_title': 'Fontes e Referências',
    content = content.replace("'sources_title': 'Fontes e Referências',", "'sources_title': 'Fontes e Referências',\n                'tab_list': 'Catálogo',\n                'tab_graph': 'Grafo de Relações',")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_i18n()
