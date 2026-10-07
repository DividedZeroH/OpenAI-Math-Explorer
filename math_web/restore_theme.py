import re

def restore_theme():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the tailwind config script
    pattern = r'<script>\s*tailwind\.config\s*=\s*\{.*?</script>'
    content = re.sub(pattern, '', content, flags=re.DOTALL)

    # 2. Revert Backgrounds
    content = content.replace('bg-brand-950', 'bg-white')  # Cards, header, footer
    content = content.replace('bg-brand-900', 'bg-[#efeae1]') # Body, abstract
    content = content.replace('bg-brand-800', 'bg-[#fffcf5]') # Selectors

    # 3. Revert Texts
    content = content.replace('text-brand-50', 'text-gray-900')
    content = content.replace('text-brand-100', 'text-gray-800')
    content = content.replace('text-brand-200', 'text-gray-700')
    content = content.replace('text-brand-300', 'text-gray-600')
    content = content.replace('text-brand-400', 'text-gray-500')
    content = content.replace('text-brand-700', 'text-gray-300')
    
    # Revert Blue Texts
    content = content.replace('text-blue-300', 'text-blue-900')
    content = content.replace('text-blue-200', 'text-blue-950')
    content = content.replace('text-blue-400', 'text-blue-800')
    content = content.replace('text-blue-100', 'text-[#4d473e]')
    content = content.replace('text-brand-950', 'text-[#fffcf5]')

    # 4. Revert Borders
    content = content.replace('border-brand-800', 'border-gray-100')
    content = content.replace('border-brand-700', 'border-[#e2dcd0]')
    content = content.replace('border-brand-600', 'border-[#c2b496]')
    
    # 5. Other specific background/borders
    content = content.replace('bg-blue-300', 'bg-blue-900')
    content = content.replace('bg-pink-800', 'bg-pink-600')
    content = content.replace('border-pink-500', 'border-pink-700')

    # 6. SVG internal colors mapping
    content = content.replace('#93c5fd', '#1e3a8a') # back to dark blue stroke
    content = content.replace('#475569', '#cbd5e1') # back to light slate grid
    content = content.replace('#120b07', '#ffffff') # back to white outlines
    content = content.replace('#180B07', '#fffcf5') # back to cream outlines
    content = content.replace('#470F00', '#f1f5f9') # critical strip bg
    content = content.replace('#FFA38A', '#64748b') # Re(s)=0 text
    content = content.replace('#A32300', '#94a3b8') # critical strip borders
    content = content.replace('#f472b6', '#db2777') # Re(s)=7/8 line
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    restore_theme()
