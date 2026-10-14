import re

def fix_graph_labels():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    js_code = """
            function cleanForGraph(str) {
                if (!str) return "";
                // Remove HTML tags like <i>
                str = str.replace(/<[^>]+>/g, '');
                // Remove the $, `, and \ symbols from math to make it readable plain text
                str = str.replace(/[\\$\\`\\\\]/g, '');
                // Replace common math commands
                str = str.replace(/mathsf|mathbb|mathcal|mathrm/g, '');
                // Clean up braces
                str = str.replace(/[{}]/g, '');
                return str;
            }
            
            function wrapText(str, width) {
                if (!str) return "";
                str = cleanForGraph(str);
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
"""
    # Replace the existing wrapText
    pattern_wrap = r'function wrapText\(str, width\) \{.*?\n            \}'
    content = re.sub(pattern_wrap, js_code.strip(), content, flags=re.DOTALL)

    # We also need to fix the tooltip title so it doesn't show raw HTML/Math in the tooltip bubble either,
    # or keep it as is. Usually tooltips are okay with plain text math, but raw HTML `<i>` shows up as literal text in Vis-Network tooltips.
    # So let's clean it too.
    content = content.replace('title: f.title,', 'title: cleanForGraph(f.title),')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_graph_labels()
