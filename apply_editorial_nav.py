import os
import re

files = [
    'proyectos.html', 'proyectos-en.html', 
    'diseno.html', 'diseno-en.html', 
    'ux-ui.html', 'ux-ui-en.html',
    'servicios.html', 'servicios-en.html'
]

nav_es = """
    <!-- Navigation -->
    <nav class="editorial-nav">
        <a href="{idx_link}" class="nav-logo">Fabián<span>Flores</span></a>
        
        <button id="mobile-menu-btn" class="mobile-btn" aria-label="Toggle Menu">
            <i class="fas fa-bars"></i>
        </button>

        <div class="nav-links">
            <a href="{idx_link}"><i class="fas fa-arrow-left"></i> Volver al CV</a>
            <div class="nav-separator"></div>
            <a href="{serv_link}">Servicios</a>
            <a href="{proy_link}">Proyectos Web</a>
            <a href="{ux_link}">UX/UI</a>
            <a href="{dis_link}">Diseño Gráfico</a>
            <div class="nav-separator"></div>
            <a href="{lang_link}" class="nav-lang">English</a>
        </div>

        <div id="mobile-menu" class="editorial-mobile-menu" style="top: 100%; z-index: 9999;">
            <a href="{idx_link}"><i class="fas fa-arrow-left"></i> Volver al CV</a>
            <a href="{serv_link}"><i class="fas fa-concierge-bell"></i> Servicios</a>
            <a href="{proy_link}"><i class="fas fa-laptop-code"></i> Proyectos Web</a>
            <a href="{ux_link}"><i class="fas fa-drafting-compass"></i> UX/UI</a>
            <a href="{dis_link}"><i class="fas fa-palette"></i> Diseño Gráfico</a>
            <a href="{lang_link}"><i class="fas fa-globe"></i> English</a>
        </div>
    </nav>
"""

nav_en = """
    <!-- Navigation -->
    <nav class="editorial-nav">
        <a href="{idx_link}" class="nav-logo">Fabián<span>Flores</span></a>
        
        <button id="mobile-menu-btn" class="mobile-btn" aria-label="Toggle Menu">
            <i class="fas fa-bars"></i>
        </button>

        <div class="nav-links">
            <a href="{idx_link}"><i class="fas fa-arrow-left"></i> Back to CV</a>
            <div class="nav-separator"></div>
            <a href="{serv_link}">Services</a>
            <a href="{proy_link}">Web Projects</a>
            <a href="{ux_link}">UX/UI</a>
            <a href="{dis_link}">Graphic Design</a>
            <div class="nav-separator"></div>
            <a href="{lang_link}" class="nav-lang">Spanish</a>
        </div>

        <div id="mobile-menu" class="editorial-mobile-menu" style="top: 100%; z-index: 9999;">
            <a href="{idx_link}"><i class="fas fa-arrow-left"></i> Back to CV</a>
            <a href="{serv_link}"><i class="fas fa-concierge-bell"></i> Services</a>
            <a href="{proy_link}"><i class="fas fa-laptop-code"></i> Web Projects</a>
            <a href="{ux_link}"><i class="fas fa-drafting-compass"></i> UX/UI</a>
            <a href="{dis_link}"><i class="fas fa-palette"></i> Graphic Design</a>
            <a href="{lang_link}"><i class="fas fa-globe"></i> Spanish</a>
        </div>
    </nav>
"""

for filename in files:
    if not os.path.exists(filename): 
        print(f"Skipping {filename}, does not exist.")
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_en = '-en' in filename
    
    idx_link = 'index-en.html' if is_en else 'index.html'
    proy_link = 'proyectos-en.html' if is_en else 'proyectos.html'
    dis_link = 'diseno-en.html' if is_en else 'diseno.html'
    ux_link = 'ux-ui-en.html' if is_en else 'ux-ui.html'
    serv_link = 'servicios-en.html' if is_en else 'servicios.html'
    
    if is_en:
        lang_link = filename.replace('-en.html', '.html')
    else:
        lang_link = filename.replace('.html', '-en.html')
    
    nav_template = nav_en if is_en else nav_es
    nav_html = nav_template.format(
        idx_link=idx_link, proy_link=proy_link, dis_link=dis_link, 
        ux_link=ux_link, serv_link=serv_link, lang_link=lang_link
    )

    # Remove the old nav
    # The old nav could be starting with <nav class="fixed..." or <nav class="editorial-nav...
    # We will match <nav ... </nav>
    content = re.sub(r'<nav.*?</nav>', nav_html.strip(), content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated nav in {filename}")

print("Navbars corrected.")
