import os
import re

files = [
    'ux-ui.html', 'ux-ui-en.html',
    'diseno.html', 'diseno-en.html'
]

for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_img_src(m):
        href = m.group(1)
        img_tag = m.group(2)
        # replace src="..." inside img_tag with src="href"
        img_tag = re.sub(r'src="[^"]+"', f'src="{href}"', img_tag)
        return f'<a href="{href}" class="lightbox-trigger">{img_tag}</a>'
    
    content = re.sub(r'<a href="([^"]+)" class="lightbox-trigger">(<img [^>]+>)</a>', replace_img_src, content)
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated image src to match href in ux-ui and diseno")
