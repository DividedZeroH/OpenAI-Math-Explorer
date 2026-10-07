import re

def remove_svgs():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the function getGraphForProblem
    # It starts with 'function getGraphForProblem(family, langObj) {'
    # and ends with '        }'
    pattern_func = r'function getGraphForProblem\(family, langObj\) \{.*?\n        \}'
    content = re.sub(pattern_func, '', content, flags=re.DOTALL)

    # Remove the injection logic
    pattern_inject = r'// Inject dynamic graph if this is the first paper in the family\s*if \(index === 0\) \{\s*abstractContent \+= getGraphForProblem\(family, lang\);\s*\}'
    content = re.sub(pattern_inject, '', content, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    remove_svgs()
