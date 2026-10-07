import re

def remove_dumb_highlighter():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the highlightKeywords function
    pattern_func = r'function highlightKeywords\(text\) \{.*?\n        \}'
    content = re.sub(pattern_func, '', content, flags=re.DOTALL)

    # Remove the calls to highlightKeywords
    content = content.replace('highlightKeywords(renderMarkdownLinks(', 'renderMarkdownLinks(')
    # Be careful with the closing parenthesis
    content = content.replace('fixMathNotation(abstract)));', 'fixMathNotation(abstract));')
    content = content.replace('fixMathNotation(family.description)))}', 'fixMathNotation(family.description))}')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    remove_dumb_highlighter()
