import os
import re

files = [
    'proyectos.html', 'proyectos-en.html', 
    'diseno.html', 'diseno-en.html', 
    'ux-ui.html', 'ux-ui-en.html'
]

nav_es = """
    <!-- Navigation/Header -->
    <nav class="fixed top-0 left-0 w-full z-50 glass-light border-b border-slate-200 py-4 px-6 md:px-12 flex justify-between items-center transition-all">
        <a href="{idx_link}" class="font-display font-bold text-2xl text-slate-900 tracking-wide hover:opacity-80 transition cursor-pointer">
            Fabián<span class="text-accent">Flores</span>
        </a>
        
        <!-- Hamburger Button -->
        <button id="mobile-menu-btn" class="md:hidden text-slate-700 hover:text-accent focus:outline-none transition-colors" aria-label="Toggle Menu">
            <i class="fas fa-bars text-xl"></i>
        </button>

        <!-- Desktop Menu -->
        <div class="hidden md:flex gap-6 text-sm font-medium items-center">
            <a href="{idx_link}" class="hover:text-accent transition"><i class="fas fa-arrow-left mr-1"></i> Volver al CV</a>
            <span class="text-slate-300">|</span>
            <a href="{proy_link}" class="hover:text-accent transition">Proyectos Web</a>
            <a href="{ux_link}" class="hover:text-accent transition">UX/UI</a>
            <a href="{dis_link}" class="hover:text-accent transition">Diseño Gráfico</a>
            <span class="text-slate-300">|</span>
            <a href="{lang_link}" class="text-emerald-600 hover:text-emerald-500 transition">English</a>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div id="mobile-menu" class="hidden absolute top-full left-0 w-full bg-white/95 backdrop-blur-md border-b border-slate-200 py-6 px-6 flex flex-col gap-4 shadow-lg transition-all duration-300" style="top: 100%; z-index: 9999;">
            <a href="{idx_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-arrow-left text-xs"></i> Volver al CV</a>
            <a href="{proy_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-laptop-code text-xs"></i> Proyectos Web</a>
            <a href="{ux_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-drafting-compass text-xs"></i> UX/UI</a>
            <a href="{dis_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-palette text-xs"></i> Diseño Gráfico</a>
            <a href="{lang_link}" class="text-emerald-600 hover:text-emerald-500 transition py-2 flex items-center gap-2"><i class="fas fa-globe text-xs"></i> English</a>
        </div>
    </nav>
"""

nav_en = """
    <!-- Navigation/Header -->
    <nav class="fixed top-0 left-0 w-full z-50 glass-light border-b border-slate-200 py-4 px-6 md:px-12 flex justify-between items-center transition-all">
        <a href="{idx_link}" class="font-display font-bold text-2xl text-slate-900 tracking-wide hover:opacity-80 transition cursor-pointer">
            Fabián<span class="text-accent">Flores</span>
        </a>
        
        <!-- Hamburger Button -->
        <button id="mobile-menu-btn" class="md:hidden text-slate-700 hover:text-accent focus:outline-none transition-colors" aria-label="Toggle Menu">
            <i class="fas fa-bars text-xl"></i>
        </button>

        <!-- Desktop Menu -->
        <div class="hidden md:flex gap-6 text-sm font-medium items-center">
            <a href="{idx_link}" class="hover:text-accent transition"><i class="fas fa-arrow-left mr-1"></i> Back to CV</a>
            <span class="text-slate-300">|</span>
            <a href="{proy_link}" class="hover:text-accent transition">Web Projects</a>
            <a href="{ux_link}" class="hover:text-accent transition">UX/UI</a>
            <a href="{dis_link}" class="hover:text-accent transition">Graphic Design</a>
            <span class="text-slate-300">|</span>
            <a href="{lang_link}" class="text-emerald-600 hover:text-emerald-500 transition">Spanish</a>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div id="mobile-menu" class="hidden absolute top-full left-0 w-full bg-white/95 backdrop-blur-md border-b border-slate-200 py-6 px-6 flex flex-col gap-4 shadow-lg transition-all duration-300" style="top: 100%; z-index: 9999;">
            <a href="{idx_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-arrow-left text-xs"></i> Back to CV</a>
            <a href="{proy_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-laptop-code text-xs"></i> Web Projects</a>
            <a href="{ux_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-drafting-compass text-xs"></i> UX/UI</a>
            <a href="{dis_link}" class="hover:text-accent transition py-2 border-b border-slate-100 flex items-center gap-2"><i class="fas fa-palette text-xs"></i> Graphic Design</a>
            <a href="{lang_link}" class="text-emerald-600 hover:text-emerald-500 transition py-2 flex items-center gap-2"><i class="fas fa-globe text-xs"></i> Spanish</a>
        </div>
    </nav>
"""

for filename in files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_en = '-en' in filename
    
    idx_link = 'index-en.html' if is_en else 'index.html'
    proy_link = 'proyectos-en.html' if is_en else 'proyectos.html'
    dis_link = 'diseno-en.html' if is_en else 'diseno.html'
    ux_link = 'ux-ui-en.html' if is_en else 'ux-ui.html'
    lang_link = filename.replace('-en', '') if is_en else filename.replace('.html', '-en.html')
    
    nav_template = nav_en if is_en else nav_es
    nav_html = nav_template.format(idx_link=idx_link, proy_link=proy_link, dis_link=dis_link, ux_link=ux_link, lang_link=lang_link)

    # 1. Remove the old nav
    content = re.sub(r'<nav.*?</nav>', '', content, flags=re.DOTALL)
    
    # 2. Add the new nav right after the body tag
    content = re.sub(r'(<body[^>]*>)', r'\1\n' + nav_html, content)
    
    # 3. Ensure the title banner doesn't have max-w-[1600px] on the wrapper so it can be full width background
    # But keep the content centered.
    # Look for: <div class="w-full pt-32 pb-10 px-6 md:px-24 max-w-[1600px] mx-auto border-b border-slate-200">
    # Replace with a full width wrapper and an inner max-w wrapper.
    header_regex = r'<div class="w-full pt-32 pb-10 px-6 md:px-24 max-w-\[1600px\] mx-auto border-b border-slate-200">(.*?)</div>'
    match = re.search(header_regex, content, re.DOTALL)
    if match:
        inner = match.group(1)
        new_header = f'''
    <div class="w-full pt-32 pb-10 border-b border-slate-200 bg-white">
        <div class="max-w-[1600px] mx-auto px-6 md:px-24">
            {inner.strip()}
        </div>
    </div>
        '''
        content = re.sub(header_regex, new_header, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navbars corrected.")
