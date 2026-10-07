import json

def replace_endash():
    with open('data.json', 'r', encoding='utf-8') as f:
        content = f.read()

    # The user specifically requested to replace '–' (U+2013) with ' ' (space)
    content = content.replace('–', ' ')

    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    replace_endash()
