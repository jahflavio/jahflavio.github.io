import os
import re

HTML_FILES = [
    'diseno.html', 'diseno-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'proyectos.html', 'proyectos-en.html',
    'index.html', 'index-en.html',
    'cv-impresion.html', 'cv-impresion-en.html'
]

# The old favicon link
old_pattern = re.compile(r"<link rel=\"icon\" href=\"data:image/svg\+xml,.*?>")
# The new favicon link
new_favicon = "<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20100%20100'%3E%3Crect%20width='100'%20height='100'%20rx='20'%20fill='%230a0a0a'/%3E%3Ctext%20x='50%25'%20y='50%25'%20dominant-baseline='middle'%20text-anchor='middle'%20font-size='65'%20font-weight='bold'%20fill='white'%20font-family='sans-serif'%3EF%3C/text%3E%3C/svg%3E\">"

def update_favicon():
    for filename in HTML_FILES:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        updated_content = old_pattern.sub(new_favicon, content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)

if __name__ == '__main__':
    update_favicon()
    print("Favicon updated to match dark identity.")
