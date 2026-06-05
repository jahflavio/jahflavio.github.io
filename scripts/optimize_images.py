import os
import re

html_files = [
    'diseno.html', 'diseno-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'proyectos.html', 'proyectos-en.html',
    'index.html', 'index-en.html'
]

img_pattern = re.compile(r'<img\s+([^>]*?)>', re.IGNORECASE)

for filename in html_files:
    if not os.path.exists(filename):
        continue
        
    print(f"Optimizing images in {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    def replace_img(match):
        attributes = match.group(1)
        
        # Don't touch if it already has loading=
        if 'loading=' in attributes:
            return match.group(0)
            
        # We only want to lazy-load portfolio images (jpg, png, jpeg), not small logo SVGs or very small badges
        # But honestly, lazy loading everything except critical above-the-fold content is fine.
        # Let's add loading="lazy" decoding="async"
        new_attributes = attributes
        if 'decoding=' not in new_attributes:
            new_attributes += ' decoding="async"'
        new_attributes += ' loading="lazy"'
        
        return f'<img {new_attributes}>'
        
    updated_content = img_pattern.sub(replace_img, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(updated_content)

print("Image optimization completed.")
