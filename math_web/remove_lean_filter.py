import re

def remove_lean_filter():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove HTML
    html_pattern = r'<label class="flex items-center space-x-2 cursor-pointer ml-4">.*?<input type="checkbox" id="leanFilter".*?</label>'
    content = re.sub(html_pattern, '', content, flags=re.DOTALL)

    # 2. Remove JS
    content = re.sub(r"const onlyLean = document\.getElementById\('leanFilter'\)\.checked;\s*", "", content)
    
    # In applyFilters:
    # const matchesLean = !onlyLean || family.has_lean;
    # return matchesDiscipline && matchesLean;
    # Replace with: return matchesDiscipline;
    content = re.sub(r"const matchesLean = !onlyLean \|\| family\.has_lean;\s*return matchesDiscipline && matchesLean;", "return matchesDiscipline;", content)

    # 3. Remove event listener
    content = re.sub(r"document\.getElementById\('leanFilter'\)\.addEventListener\('change', applyFilters\);\s*", "", content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    remove_lean_filter()
