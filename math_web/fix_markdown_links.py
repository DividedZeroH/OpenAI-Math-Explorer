import re

def fix_links():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add cache buster to fetch
    content = content.replace("fetch('data.json');", "fetch('data.json?t=' + new Date().getTime());")

    # 2. Add renderMarkdownLinks function
    js_func = """
        function fixMathNotation(text) {
            if (!text) return text;
            return text.replace(/\\$\\`(.*?)\\`\\$/g, '\\\\($1\\\\)');
        }

        function renderMarkdownLinks(text) {
            if (!text) return text;
            // Parse Markdown links [Text](URL)
            return text.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, '<a href="$2" target="_blank" class="text-book-link hover:underline font-bold">$1</a>');
        }"""
        
    pattern = r'function fixMathNotation\(text\) \{.*?\n        \}'
    content = re.sub(pattern, js_func, content, flags=re.DOTALL)

    # 3. Apply it to abstract and description rendering
    # abstract = fixMathNotation(abstract);
    content = content.replace('abstract = fixMathNotation(abstract);', 'abstract = renderMarkdownLinks(fixMathNotation(abstract));')
    
    # ${fixMathNotation(family.description)}
    content = content.replace('${fixMathNotation(family.description)}', '${renderMarkdownLinks(fixMathNotation(family.description))}')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_links()
