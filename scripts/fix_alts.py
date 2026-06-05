import os
import re

HTML_FILES = [
    'diseno.html', 'diseno-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'proyectos.html', 'proyectos-en.html',
    'index.html', 'index-en.html'
]

img_pattern = re.compile(r'<img\s+([^>]*?)>', re.IGNORECASE)

def fix_alts():
    for filename in HTML_FILES:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def replace_alt(match):
            attributes = match.group(1)
            if 'alt=' not in attributes:
                attributes += ' alt="Portfolio Image"'
            return f'<img {attributes}>'
            
        updated_content = img_pattern.sub(replace_alt, content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)

if __name__ == '__main__':
    fix_alts()
    print("Fixed alt attributes.")
