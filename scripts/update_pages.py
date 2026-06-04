import os
import glob
import re

files = [
    'proyectos.html', 'proyectos-en.html', 
    'diseno.html', 'diseno-en.html', 
    'ux-ui.html', 'ux-ui-en.html'
]

nav_template = """<nav class="fixed top-0 w-full z-50 glass-light border-b border-slate-200 py-4 px-6 md:px-12 flex justify-between items-center transition-all">
        <div class="font-display font-bold text-2xl text-slate-900 tracking-wide">
            Fabián<span class="text-accent">Flores</span>
        </div>
        <div class="hidden md:flex gap-6 text-sm font-medium items-center">
            <a href="{idx_link}" class="hover:text-accent transition"><i class="fas fa-arrow-left mr-1"></i> CV</a>
            <span class="text-slate-300">|</span>
            <a href="{proy_link}" class="hover:text-accent transition">Web</a>
            <a href="{dis_link}" class="hover:text-accent transition">Graphic</a>
            <a href="{ux_link}" class="hover:text-accent transition">UX/UI</a>
            <span class="text-slate-300">|</span>
            <a href="{lang_link}" class="text-emerald-600 hover:text-emerald-500 transition">{lang_text}</a>
        </div>
    </nav>"""

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
    lang_text = 'Spanish' if is_en else 'English'
    
    nav_html = nav_template.format(idx_link=idx_link, proy_link=proy_link, dis_link=dis_link, ux_link=ux_link, lang_link=lang_link, lang_text=lang_text)

    # Replace body class
    content = re.sub(r'<body class="[^"]*">', '<body class="bg-slate-50 text-slate-700 w-full overflow-x-hidden selection:bg-accent selection:text-white">', content)
    
    # Remove the top decorative bar and old header
    content = re.sub(r'<div class="h-2 bg-gradient[^>]*></div>', '', content)
    
    # Extract Title and Subtitle from header
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    sub_match = re.search(r'<p[^>]*class="mt-2 text-gray-500"[^>]*>(.*?)</p>', content)
    
    title = title_match.group(1) if title_match else ""
    subtitle = sub_match.group(1) if sub_match else ""
    
    # Remove header
    content = re.sub(r'<header.*?</header>', nav_html + f'''
    <div class="w-full pt-32 pb-10 px-6 md:px-24 max-w-[1600px] mx-auto border-b border-slate-200">
         <h1 class="font-display text-4xl md:text-5xl font-bold text-slate-900 mb-4">{title}</h1>
         <p class="text-slate-500 text-lg">{subtitle}</p>
    </div>
    ''', content, flags=re.DOTALL)
    
    # Modify main wrapper
    content = content.replace('<main class="p-10 w-full max-w-[1600px] mx-auto">', '<main class="w-full max-w-[1600px] mx-auto px-6 md:px-24 py-16">')
    
    # Replace Card Classes
    content = content.replace('bg-white rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-1 transition-transform duration-300', 
                              'glass-light rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-xl transition-all duration-300 border border-slate-200 flex flex-col')
    
    # Replace Image classes
    content = content.replace('class="w-full h-48 object-cover"', 'class="w-full h-56 object-cover border-b border-slate-200"')
    
    # Replace internal padding to flex
    content = content.replace('<div class="p-6">', '<div class="p-8 flex-1 flex flex-col">')
    
    # Replace Text classes
    content = content.replace('text-primary mb-2', 'text-slate-900 mb-3')
    content = content.replace('text-gray-600 mb-4', 'text-slate-600 mb-6 flex-1')
    
    # Replace buttons
    content = content.replace('inline-block bg-accent text-white text-xs font-bold px-4 py-2 rounded-md hover:bg-indigo-700 transition', 
                              'inline-flex items-center justify-center bg-accent text-white font-medium px-5 py-2.5 rounded-lg hover:bg-accentDark transition shadow-sm')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated 6 files.")
