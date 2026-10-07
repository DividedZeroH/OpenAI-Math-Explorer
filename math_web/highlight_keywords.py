import re

def highlight_keywords():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    js_code = """
        function highlightKeywords(text) {
            if (!text) return text;
            // Keywords that are mathematically significant
            const keywords = ['proves', 'prove', 'resolves', 'resolve', 'establishes', 'shows', 'conjecture', 'theorem', 'lemma', 'hypothesis', 'formula', 'equation', 'constant', 'irrational', 'rational', 'irrationality', 'density', 'manifold', 'topology', 'geometry', 'algebraic', 'integral', 'derivative', 'equivalence', 'generalization', 'bounds', 'asymptotically', 'finite', 'infinite', 'zero-free', 'independent', 'convergence'];
            
            const regex = new RegExp('\\\\b(' + keywords.join('|') + ')\\\\b', 'gi');
            
            // Split by HTML tags to avoid messing up attributes (like hrefs or classes)
            const parts = text.split(/(<[^>]+>)/g);
            for (let i = 0; i < parts.length; i++) {
                // If it's not an HTML tag, apply highlighting
                if (!parts[i].startsWith('<')) {
                    parts[i] = parts[i].replace(regex, '<span class="font-bold underline decoration-[#CFC4B4] underline-offset-2">$1</span>');
                }
            }
            return parts.join('');
        }
"""
    
    # Inject the function before renderMarkdownLinks
    content = content.replace('function renderMarkdownLinks(text) {', js_code + '\n        function renderMarkdownLinks(text) {')

    # Apply to abstract: abstract = renderMarkdownLinks(fixMathNotation(abstract));
    content = content.replace('abstract = renderMarkdownLinks(fixMathNotation(abstract));', 'abstract = highlightKeywords(renderMarkdownLinks(fixMathNotation(abstract)));')
    
    # Apply to description: ${renderMarkdownLinks(fixMathNotation(family.description))}
    content = content.replace('${renderMarkdownLinks(fixMathNotation(family.description))}', '${highlightKeywords(renderMarkdownLinks(fixMathNotation(family.description)))}')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    highlight_keywords()
