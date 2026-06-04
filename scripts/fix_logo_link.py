import os
import re

files = [
    'index.html', 'index-en.html',
    'proyectos.html', 'proyectos-en.html', 
    'diseno.html', 'diseno-en.html', 
    'ux-ui.html', 'ux-ui-en.html'
]

pattern = re.compile(
    r'<div class="font-display font-bold text-2xl text-slate-900 tracking-wide">\s*'
    r'Fabián<span class="text-accent">Flores</span>\s*'
    r'</div>'
)

for filename in files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_en = '-en' in filename
    target_link = 'index-en.html' if is_en else 'index.html'
    
    replacement = f"""<a href="{target_link}" class="font-display font-bold text-2xl text-slate-900 tracking-wide hover:opacity-80 transition cursor-pointer">
            Fabián<span class="text-accent">Flores</span>
        </a>"""
        
    new_content = pattern.sub(replacement, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Logo wrapped in a tags.")
