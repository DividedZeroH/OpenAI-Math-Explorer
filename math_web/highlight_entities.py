import json
import re

def highlight_semantic_entities():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Regex to match names of theorems, conjectures, etc.
    # Examples: "Milne's rationality conjecture", "quasi-Riemann hypothesis", "Birch-Swinnerton-Dyer formula"
    # Matches: Capitalized Word (optional following words) (conjecture|hypothesis|theorem|formula|problem|constant|equation|lemma)
    pattern = re.compile(r'\b([A-Z][A-Za-z\-\–\']*(?:\s+[a-z]+)*\s+(?:conjecture|hypothesis|theorem|formula|problem|constant|equation|lemma|inequality|principle|space|manifold|variety))\b', re.IGNORECASE)

    def highlight(text):
        if not text:
            return text
        # Only highlight if it looks like a named entity (contains a capital letter to avoid highlighting generic "the equation")
        def repl(m):
            phrase = m.group(1)
            if any(c.isupper() for c in phrase):
                return f'<span class="font-bold underline decoration-[#CFC4B4] underline-offset-2">{phrase}</span>'
            return phrase
        return pattern.sub(repl, text)

    for family in data:
        if 'description' in family:
            family['description'] = highlight(family['description'])
        for paper in family.get('papers', []):
            if 'abstract' in paper:
                paper['abstract'] = highlight(paper['abstract'])

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    highlight_semantic_entities()
