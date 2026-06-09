import os
import re

files = ['servicios.html', 'servicios-en.html']

for filename in files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Simplify header class
    content = re.sub(r'<header class="editorial-page-header[^"]*">', '<header class="editorial-page-header">', content)
    
    # Simplify h1 class (remove Tailwind)
    content = re.sub(r'<h1 class="[^"]*">', '<h1>', content)
    
    # Simplify p class (remove Tailwind)
    content = re.sub(r'<p class="text-xl text-slate-600 max-w-2xl mx-auto">', '<p>', content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Servicios headers normalized.")
