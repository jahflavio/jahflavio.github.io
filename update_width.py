import os
import glob
import re

html_files = glob.glob('*.html')
# We exclude the index files since they are already fully redesigned
exclude = ['index.html', 'index_backup.html', 'index-en.html', 'index-en_backup.html', 'portfolio-gsap.html']
html_files = [f for f in html_files if f not in exclude]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace tailwind CDN and config with Vite entry point
    content = re.sub(
        r'<script src="https://cdn\.tailwindcss\.com"></script>\s*<link href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/.*?\s*<link\s*href="https://fonts\.googleapis\.com/css2\?family=Inter.*?\s*<script>\s*tailwind\.config = \{.*?\s*</script>',
        '''<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;500;700;800&display=swap" rel="stylesheet">
    <script type="module" src="/main.js"></script>''',
        content,
        flags=re.DOTALL
    )

    # 2. Replace width constraints
    content = content.replace('class="max-w-[210mm] mx-auto', 'class="w-full')
    content = content.replace('class="max-w-7xl mx-auto"', 'class="w-full max-w-[1600px] mx-auto px-6 md:px-24"')
    content = content.replace('<main class="p-10">', '<main class="p-10 w-full max-w-[1600px] mx-auto">')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files: {', '.join(html_files)}")
