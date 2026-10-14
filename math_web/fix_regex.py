import re

def fix_graph_labels():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the broken regex
    content = content.replace("str = str.replace(/[\\$\\`\\]/g, '');", "str = str.replace(/[\\\\$\\\\`\\\\\\\\]/g, '');")
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_graph_labels()
