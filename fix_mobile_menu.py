import os

files = [
    'servicios.html', 'servicios-en.html',
    'proyectos.html', 'proyectos-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'diseno.html', 'diseno-en.html'
]

script_to_add = """
    <script>
        // Mobile menu toggle
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        if (btn && menu) {
            btn.addEventListener('click', () => {
                menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
            });
        }
    </script>
</body>"""

for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "Mobile menu toggle" not in content:
        content = content.replace("</body>", script_to_add)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
print("Added mobile menu script where missing.")
