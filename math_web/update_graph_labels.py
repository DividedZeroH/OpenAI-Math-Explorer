import re

def update_labels():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to change:
    # label: `Prob ${f.id}`,
    # to something that wraps f.title
    
    # We can inject a helper function inside initGraph
    helper_code = """
        function initGraph(data) {
            function wrapText(str, width) {
                if (!str) return "";
                const words = str.split(' ');
                let line = '';
                let result = '';
                for (let n = 0; n < words.length; n++) {
                    const testLine = line + words[n] + ' ';
                    if (testLine.length > width && n > 0) {
                        result += line + '\\n';
                        line = words[n] + ' ';
                    } else {
                        line = testLine;
                    }
                }
                result += line;
                return result.trim();
            }
            
            const nodes = [];
"""
    content = content.replace('        function initGraph(data) {\n            const nodes = [];', helper_code)

    # Now change the label
    # label: `Prob ${f.id}`,
    # Add title: f.title
    
    new_node_code = """
                nodes.push({
                    id: f.id,
                    label: wrapText(f.title, 25),
                    title: f.title,
"""
    content = re.sub(r'nodes\.push\(\{\s*id: f\.id,\s*label: `Prob \$\{f\.id\}`,\s*', new_node_code, content, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_labels()
