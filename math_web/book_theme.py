import re

def apply_book_theme():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    tailwind_script = """<script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        book: {
                            bg: '#F4F0E6',
                            text: '#2D2A26',
                            title: '#4A3F35',
                            link: '#6B4F2A',
                            border: '#CFC4B4',
                        }
                    }
                }
            }
        }
    </script>"""
    
    # Ensure no old tailwind config exists
    pattern = r'<script>\s*tailwind\.config\s*=\s*\{.*?</script>'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', tailwind_script)

    # 1. Backgrounds
    content = content.replace('bg-[#efeae1]', 'bg-book-bg')
    content = content.replace('bg-white', 'bg-[#FCFAF5]') # Cards slightly lighter than bg
    content = content.replace('bg-[#fffcf5]', 'bg-[#FCFAF5]') # Selectors / header
    content = content.replace('bg-[#ede6d5]', 'bg-book-bg') 

    # 2. Texts & Titles
    content = content.replace('text-gray-900', 'text-book-title')
    content = content.replace('text-gray-800', 'text-book-text')
    content = content.replace('text-gray-700', 'text-book-text')
    content = content.replace('text-gray-600', 'text-book-text opacity-90')
    content = content.replace('text-gray-500', 'text-book-text opacity-70')
    
    content = content.replace('text-blue-900', 'text-book-title')
    content = content.replace('text-blue-950', 'text-book-title font-bold')
    content = content.replace('text-blue-800', 'text-book-title')
    content = content.replace('text-[#fffcf5]', 'text-book-bg')

    # Links
    # Links are usually a tag or specific buttons
    content = content.replace('hover:text-[#4d473e]', 'hover:text-book-link')
    content = content.replace('hover:text-blue-950', 'hover:text-book-link')
    content = content.replace('text-blue-900 hover', 'text-book-link hover') # For the paper URLs
    content = content.replace('text-blue-300', 'text-book-link') # Just in case

    # 3. Borders
    content = content.replace('border-gray-100', 'border-book-border opacity-50')
    content = content.replace('border-[#e2dcd0]', 'border-book-border')
    content = content.replace('border-[#c2b496]', 'border-book-border')
    content = content.replace('border-[#d6ccb6]', 'border-book-border')
    content = content.replace('border-gray-300', 'border-book-border')

    # 4. Badges and Accents
    content = content.replace('bg-blue-900', 'bg-book-title') # Problem badge
    content = content.replace('bg-pink-600', 'bg-book-link') # Lean badge
    content = content.replace('border-pink-700', 'border-book-title')
    
    # 5. SVGs internal colors (Ink style)
    content = content.replace('#1e3a8a', '#2D2A26') # Dark ink
    content = content.replace('#3b82f6', '#4A3F35') # Title ink
    content = content.replace('#93c5fd', '#6B4F2A') # Link ink / lighter lines
    content = content.replace('#cbd5e1', '#CFC4B4') # Grid lines -> book-border
    content = content.replace('#f1f5f9', '#F4F0E6') # Complex plane strip -> book-bg
    content = content.replace('#64748b', '#4A3F35') # Re(s)=0 text
    content = content.replace('#94a3b8', '#CFC4B4') # Grid
    content = content.replace('#db2777', '#6B4F2A') # Re(s)=7/8 line

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    apply_book_theme()
