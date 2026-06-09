import os
import re

files = [
    'proyectos.html', 'proyectos-en.html', 
    'diseno.html', 'diseno-en.html', 
    'ux-ui.html', 'ux-ui-en.html',
    'servicios.html', 'servicios-en.html'
]

footer_html = """
    <!-- Footer -->
    <footer class="editorial-footer no-print">
        <p>© 2026 Fabián Flores. Todos los derechos reservados.</p>
    </footer>
"""

for filename in files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the footer block entirely
    content = re.sub(r'<footer.*?</footer>', footer_html.strip(), content, flags=re.DOTALL)
    
    # Also clean up any body tags to be exactly <body>
    content = re.sub(r'<body[^>]*>', '<body>', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Footers and Body tags fixed.")
