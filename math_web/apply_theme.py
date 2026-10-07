import re

def update_theme():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject tailwind config
    tailwind_script = """<script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#FFEBE6',
                            100: '#FFC7B8',
                            200: '#FFA38A',
                            300: '#FF7F5C',
                            400: '#FF5B2E',
                            500: '#FF3900',
                            600: '#D12D00',
                            700: '#A32300',
                            800: '#751900',
                            900: '#470F00',
                            950: '#1A0600',
                        }
                    }
                }
            }
        }
    </script>"""
    
    if "tailwind.config" not in content:
        content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', tailwind_script)

    # 2. Backgrounds
    content = content.replace('bg-[#efeae1]', 'bg-brand-50')
    content = content.replace('bg-[#f8f4e6]', 'bg-white')
    content = content.replace('bg-[#e2d5bc]', 'bg-brand-100')
    content = content.replace('bg-[#fffcf5]', 'bg-brand-50')
    content = content.replace('bg-[#fcfaf5]', 'bg-brand-50')
    content = content.replace('bg-[#ede6d5]', 'bg-brand-200')
    
    # 4. Borders
    content = content.replace('border-[#e2dcd0]', 'border-brand-200')
    content = content.replace('border-[#c2b496]', 'border-brand-300')
    content = content.replace('border-[#d6ccb6]', 'border-brand-300')
    content = content.replace('border-gray-100', 'border-brand-100')
    content = content.replace('border-gray-200', 'border-brand-200')
    content = content.replace('border-gray-300', 'border-brand-300')
    
    # Do NOT replace text-blue-* or svg internal strokes (#1e3a8a, etc)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_theme()
