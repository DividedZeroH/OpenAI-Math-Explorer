import re

def refine_contrast():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Make the book-text and book-title pure black
    content = content.replace("text: '#1C1917'", "text: '#000000'")
    content = content.replace("title: '#2D241E'", "title: '#000000'")

    # Change the Problem badge back to dark blue
    # It currently is: class="px-2.5 py-0.5 rounded-none text-xs font-medium bg-book-title text-book-bg"
    # We want: bg-blue-900 text-white
    content = content.replace('bg-book-title text-book-bg', 'bg-blue-900 text-white')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    refine_contrast()
