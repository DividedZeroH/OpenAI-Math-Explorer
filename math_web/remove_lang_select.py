import re

def remove_language_selector():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the HTML for langSelect
    html_pattern = r'<!-- Selector de idioma -->\s*<select id="langSelect".*?</select>'
    content = re.sub(html_pattern, '', content, flags=re.DOTALL)

    # 2. Remove the JS event listener
    js_pattern = r"document\.getElementById\('langSelect'\)\.addEventListener\('change', \(e\) => \{.*?\}\);"
    content = re.sub(js_pattern, '', content, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    remove_language_selector()
