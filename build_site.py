import re
import json

def parse_all():
    # 1. Parse disciplines from overview.tex
    with open('overview.tex', 'r', encoding='utf-8') as f:
        overview_content = f.read()
    
    disciplines_by_family_id = {}
    current_discipline = "Other"
    
    for line in overview_content.splitlines():
        # Match \cataloguesection{Discipline}{count}
        m_cat = re.match(r'\\cataloguesection{([^}]+)}{', line)
        if m_cat:
            current_discipline = m_cat.group(1).strip()
            continue
        
        # Match \resultentry{001}...
        m_res = re.match(r'\\resultentry{(\d{3})}', line)
        if m_res:
            family_id = m_res.group(1)
            disciplines_by_family_id[family_id] = current_discipline

    # 2. Parse Lean formalizations from lean/formalization.yaml using regex
    lean_papers = set()
    try:
        with open('lean/formalization.yaml', 'r', encoding='utf-8') as f:
            for line in f:
                # look for id: ../preprints/FolderName/paper.pdf
                m = re.search(r'id:\s*(\S+)', line)
                if m:
                    source_id = m.group(1)
                    path_parts = source_id.split('/')
                    if len(path_parts) > 2:
                        lean_papers.add(path_parts[-2]) # add folder name
    except Exception as e:
        print(f"Warning: Could not parse lean/formalization.yaml: {e}")

    # 3. Parse CONTENTS.md
    with open('CONTENTS.md', 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.findall(r'<tbody><tr>\s*<td>(.*?)</td>\s*</tr></tbody>', content, re.DOTALL)
    
    families = []
    current_family = None
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        family_match = re.match(r'\*\*(\d{3})\.\s+(.*?)\*\*\s*(.*)', block, re.DOTALL)
        if family_match:
            if current_family:
                families.append(current_family)
            fid = family_match.group(1)
            current_family = {
                "id": fid,
                "title": family_match.group(2).strip(),
                "description": family_match.group(3).strip(),
                "discipline": disciplines_by_family_id.get(fid, "General"),
                "has_lean": False,
                "papers": []
            }
        else:
            paper_match = re.search(r'\[(.*?)\]\((.*?)\)\s*(.*)', block, re.DOTALL)
            if paper_match and current_family:
                url = paper_match.group(2).strip()
                # Check if this paper has lean by checking its folder in the URL
                has_lean = False
                for lp in lean_papers:
                    if lp in url:
                        has_lean = True
                        break
                
                if has_lean:
                    current_family["has_lean"] = True

                current_family["papers"].append({
                    "title": paper_match.group(1).strip(),
                    "url": url,
                    "abstract": paper_match.group(3).strip(),
                    "has_lean": has_lean
                })
    if current_family:
        families.append(current_family)

    with open('math_web/data.json', 'w', encoding='utf-8') as f:
        json.dump(families, f, ensure_ascii=False, indent=2)
        
    print(f"Parsed {len(families)} families.")

if __name__ == '__main__':
    parse_all()
