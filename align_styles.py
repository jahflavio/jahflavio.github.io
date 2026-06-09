import os
import re

files = [
    'servicios.html', 'servicios-en.html',
    'proyectos.html', 'proyectos-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'diseno.html', 'diseno-en.html'
]

header_regex = re.compile(r'<header class="editorial-page-header">\s*<h1>(.*?)</h1>\s*<p>(.*?)</p>\s*</header>', re.DOTALL)

for fname in files:
    if not os.path.exists(fname):
        print(f"{fname} not found.")
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header
    def repl_header(m):
        title = m.group(1).strip()
        subtitle = m.group(2).strip()
        return f'''<section class="editorial-hero editorial-hero--dark">
        <div class="hero-inner" style="align-items: center; text-align: center; max-width: 800px; margin: 0 auto;">
            <h1 class="hero-title hero-text" style="font-size: clamp(2.5rem, 6vw, 4rem); text-transform: none; line-height: 1.1; margin-bottom: 1rem;">{title}</h1>
            <p class="hero-subtitle hero-text" style="font-size: clamp(1rem, 1.5vw, 1.25rem); max-width: 100%; margin: 0 auto; color: #cccccc;">{subtitle}</p>
        </div>
    </section>'''
    
    content = header_regex.sub(repl_header, content)

    # For projects/ux/design
    content = content.replace('class="editorial-project"', 'class="editorial-card"')
    
    # Fix the project content elements
    def repl_card_body(m):
        inner = m.group(1)
        # replace <h3>
        inner = inner.replace('<h3>', '<h3 class="card-title">')
        # replace <p> exactly
        inner = re.sub(r'<p>', r'<p class="card-desc">', inner)
        # replace <a> tags lacking a class. Avoid replacing ones that already have class (like lightbox-trigger)
        inner = re.sub(r'<a href="([^"]+)"( target="_blank")?>([^<]+)</a>', r'<a href="\1"\2 class="card-link">\3</a>', inner)
        return f'<div class="card-body">{inner}</div>'

    content = re.sub(r'<div class="editorial-project-content">(.*?)</div>', repl_card_body, content, flags=re.DOTALL)

    # For servicios.html specifically
    if 'servicios' in fname:
        content = re.sub(r'class="glass-card[^"]+"', 'class="editorial-sidebar-block flex flex-col h-full"', content)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print("Styles aligned successfully.")
