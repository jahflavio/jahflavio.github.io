import os
import re

HTML_FILES = [
    'diseno.html', 'diseno-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'proyectos.html', 'proyectos-en.html',
    'index.html', 'index-en.html'
]

def remove_lazy_loading():
    for filename in HTML_FILES:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove loading="lazy" and decoding="async"
        content = content.replace(' loading="lazy"', '')
        content = content.replace(' decoding="async"', '')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    remove_lazy_loading()
    print("Removed lazy loading to fix GSAP scroll stutter.")
