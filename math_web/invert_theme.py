import re

def invert_theme():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply the new tailwind configuration with rgb colors
    tailwind_script = """<script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: 'rgb(248 241 237)',
                            100: 'rgb(235 215 204)',
                            200: 'rgb(222 190 171)',
                            300: 'rgb(212 171 148)',
                            400: 'rgb(195 138 105)',
                            500: 'rgb(182 113 73)',
                            600: 'rgb(150 93 60)',
                            700: 'rgb(117 72 47)',
                            800: 'rgb(84 52 33)',
                            900: 'rgb(51 32 20)',
                            950: 'rgb(18 11 7)'
                        }
                    }
                }
            }
        }
    </script>"""
    
    # Replace the old tailwind config script block
    pattern = r'<script src="https://cdn.tailwindcss.com"></script>.*?<\/script>'
    content = re.sub(pattern, tailwind_script, content, flags=re.DOTALL)

    # Invert Backgrounds
    content = content.replace('bg-white', 'bg-brand-950')
    content = content.replace('bg-brand-50', 'bg-brand-900')
    content = content.replace('bg-brand-100', 'bg-brand-800')
    content = content.replace('bg-brand-200', 'bg-brand-800')
    content = content.replace('bg-[#fcfaf5]', 'bg-brand-900')

    # Invert Texts
    content = content.replace('text-gray-900', 'text-brand-50')
    content = content.replace('text-gray-800', 'text-brand-100')
    content = content.replace('text-gray-700', 'text-brand-200')
    content = content.replace('text-gray-600', 'text-brand-300')
    content = content.replace('text-gray-500', 'text-brand-400')
    content = content.replace('text-gray-300', 'text-brand-700')
    
    # Blue Texts (inverting dark blue to light blue)
    content = content.replace('text-blue-900', 'text-blue-300')
    content = content.replace('text-blue-950', 'text-blue-200')
    content = content.replace('text-blue-800', 'text-blue-400')
    content = content.replace('text-[#4d473e]', 'text-blue-100')
    content = content.replace('text-[#fffcf5]', 'text-brand-950')

    # Invert Borders
    content = content.replace('border-brand-100', 'border-brand-800')
    content = content.replace('border-brand-200', 'border-brand-700')
    content = content.replace('border-brand-300', 'border-brand-600')
    
    # Other specific background/borders
    content = content.replace('bg-blue-900', 'bg-blue-300')
    content = content.replace('bg-pink-600', 'bg-pink-800')
    content = content.replace('border-pink-700', 'border-pink-500')

    # SVG internal colors mapping
    content = content.replace('#1e3a8a', '#93c5fd') # dark blue to light blue (blue-300)
    content = content.replace('#cbd5e1', '#475569') # light gray grid to dark slate grid
    content = content.replace('#ffffff', '#120b07') # white outlines to dark background
    content = content.replace('#f1f5f9', '#470F00') # critical strip bg
    content = content.replace('#64748b', '#FFA38A') # Re(s)=0 text
    content = content.replace('#94a3b8', '#A32300') # critical strip borders
    content = content.replace('#db2777', '#f472b6') # Re(s)=7/8 line to lighter pink
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    invert_theme()
