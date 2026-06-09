import os

files = [
    'ux-ui.html', 'ux-ui-en.html',
    'diseno.html', 'diseno-en.html',
    'servicios.html', 'servicios-en.html'
]

script_to_add = '<script src="https://cdn.tailwindcss.com"></script>\n    <link rel="stylesheet" href="editorial.min.css">'

for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "cdn.tailwindcss.com" not in content:
        content = content.replace('<link rel="stylesheet" href="editorial.min.css">', script_to_add)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
print("Restored Tailwind CDN.")
