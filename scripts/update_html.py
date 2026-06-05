import os

HTML_FILES = [
    'diseno.html', 'diseno-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'proyectos.html', 'proyectos-en.html',
    'index.html', 'index-en.html',
    'cv-impresion.html', 'cv-impresion-en.html'
]

preload_tags = """
    <!-- Performance & SEO -->
    <meta name="theme-color" content="#0a0a0a">
    <link rel="preload" href="editorial.min.css" as="style">
    <link rel="preload" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" as="style">"""

for filename in HTML_FILES:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update CSS link
    content = content.replace('<link rel="stylesheet" href="editorial.css">', '<link rel="stylesheet" href="editorial.min.css">')
    
    # Add preloads and theme-color
    if 'theme-color' not in content:
        content = content.replace('</head>', preload_tags + '\n</head>')
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files with minified CSS and preload tags.")
