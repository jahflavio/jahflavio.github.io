import os
import re

ux_ui_dir = 'ux ui'
files = os.listdir(ux_ui_dir)

# Separate into redes and web
redes_files = []
web_files = {}

for f in files:
    lower_f = f.lower()
    # Handle the typo "refes" as well
    if 'redes' in lower_f or 'refes' in lower_f:
        redes_files.append(f)
    else:
        # Determine project
        if 'gobogy' in lower_f:
            proj = 'GoBogy'
            desc = 'Diseño de interfaces web orientadas a la experiencia del usuario para productos naturistas de la marca GoBogy.'
            desc_en = 'Web interface design focused on user experience for GoBogy natural products.'
        elif 'm4' in lower_f or 'm4tel' in lower_f:
            proj = 'M4 Connectivity'
            desc = 'Diseño de interfaz de usuario y landing page para M4 Connectivity, destacando soluciones de conectividad y dispositivos inteligentes.'
            desc_en = 'User interface and landing page design for M4 Connectivity, highlighting connectivity solutions and smart devices.'
        elif 'polyglobal' in lower_f:
            proj = 'Polyglobal'
            desc = 'Diseño web corporativo para Polyglobal, presentando sus soluciones de empaque y materiales sostenibles de manera profesional.'
            desc_en = 'Corporate web design for Polyglobal, presenting their packaging solutions and sustainable materials in a professional manner.'
        elif 'dcobys' in lower_f:
            proj = 'Dcobys'
            desc = 'Diseño de interfaz web moderna e intuitiva para servicios especializados.'
            desc_en = 'Modern and intuitive web interface design for specialized services.'
        elif 'essenzia' in lower_f:
            proj = 'Essenzia Española'
            desc = 'Diseño web elegante y sofisticado para Essenzia Española, enfocado en vestidos de novia y alta costura.'
            desc_en = 'Elegant and sophisticated web design for Essenzia Española, focused on wedding dresses and haute couture.'
        elif 'f&r' in lower_f:
            proj = 'F&R Clinic'
            desc = 'Diseño web centrado en el usuario para clínica de terapias y bienestar.'
            desc_en = 'User-centric web design for therapy and wellness clinic.'
        elif 'huntress' in lower_f:
            proj = 'Huntress Films'
            desc = 'Sitio web moderno y visualmente impactante para el estudio cinematográfico Huntress Films, resaltando sus producciones audiovisuales.'
            desc_en = 'Modern and visually striking website for the Huntress Films film studio, highlighting its audiovisual productions.'
        elif 'labbe' in lower_f:
            proj = 'Labbe'
            desc = 'Diseño UI para portal de laboratorio clínico, optimizando la experiencia de usuario para consultar resultados médicos y agendar citas.'
            desc_en = 'UI design for a clinical laboratory portal, optimizing the user experience for checking medical results and scheduling appointments.'
        elif 'lego' in lower_f:
            proj = 'LEGO'
            desc = 'Páginas promocionales interactivas para campañas de LEGO, diseñadas para captar la atención del público infantil y familiar.'
            desc_en = 'Interactive promotional pages for LEGO campaigns, designed to capture the attention of children and families.'
        elif 'the counter' in lower_f:
            proj = 'The Counter'
            desc = 'Diseño de interfaz web dinámica para portal de hamburguesas The Counter.'
            desc_en = 'Dynamic web interface design for The Counter burger portal.'
        else:
            proj = 'Otros Proyectos'
            desc = 'Diseños adicionales de interfaces y experiencia de usuario.'
            desc_en = 'Additional interface and user experience designs.'
            
        if proj not in web_files:
            web_files[proj] = {'files': [], 'desc': desc, 'desc_en': desc_en}
        web_files[proj]['files'].append(f)

# Sort files inside projects
for p in web_files:
    web_files[p]['files'].sort()

# Build HTML for UX UI
def build_uxui_html(is_en=False):
    html = []
    for proj, data in web_files.items():
        desc = data['desc_en'] if is_en else data['desc']
        html.append(f'<div class="w-full mb-12">')
        html.append(f'    <h2 class="text-3xl font-bold mb-2 text-gray-800">{proj}</h2>')
        html.append(f'    <p class="text-gray-600 mb-6 text-lg">{desc}</p>')
        html.append(f'    <div class="editorial-gallery">')
        for f in data['files']:
            html.append(f'        <div class="gallery-item"><a href="ux ui/{f}" class="lightbox-trigger"><img src="ux ui/{f}" alt="{proj} UX/UI Design" loading="lazy" decoding="async" class="rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-300"></a></div>')
        html.append(f'    </div>')
        html.append(f'</div>')
    return '\n'.join(html)

uxui_es = build_uxui_html(False)
uxui_en = build_uxui_html(True)

# Replace in ux-ui.html and ux-ui-en.html
def replace_section(filename, new_content):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # The section starts after <section class="editorial-section">
    # and ends before </section> ... wait, let's just use regex
    match = re.search(r'(<section class="editorial-section">)(.*?)(</section>)', content, re.DOTALL)
    if match:
        content = content.replace(match.group(2), '\n' + new_content + '\n    ')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

replace_section('ux-ui.html', uxui_es)
replace_section('ux-ui-en.html', uxui_en)


# Now build Redes section for diseno.html
def build_redes_html(is_en=False):
    title = "Redes, arte y más" if not is_en else "Social Media, Art & More"
    desc = "Diseños para redes sociales, banners, y diversos materiales gráficos." if not is_en else "Designs for social media, banners, and various graphic materials."
    
    html = []
    html.append(f'<div class="w-full mt-16 mb-12" id="redes">')
    html.append(f'    <h2 class="text-3xl font-bold mb-2 text-gray-800">{title}</h2>')
    html.append(f'    <p class="text-gray-600 mb-6 text-lg">{desc}</p>')
    html.append(f'    <div class="editorial-gallery">')
    for f in sorted(redes_files):
        html.append(f'        <div class="gallery-item"><a href="ux ui/{f}" class="lightbox-trigger"><img src="ux ui/{f}" alt="Design" loading="lazy" decoding="async" class="rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-300"></a></div>')
    html.append(f'    </div>')
    html.append(f'</div>')
    return '\n'.join(html)

redes_es = build_redes_html(False)
redes_en = build_redes_html(True)

def append_to_diseno(filename, new_content):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Append before the last </section> that contains galleries.
    # In diseno.html, there is <section class="editorial-section">... galleries ... </section>
    match = re.search(r'(<section class="editorial-section">.*?)(</section>)', content, re.DOTALL)
    if match:
        # Check if already added
        if 'id="redes"' not in content:
            new_section = match.group(1) + '\n' + new_content + '\n    ' + match.group(2)
            content = content.replace(match.group(0), new_section)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

append_to_diseno('diseno.html', redes_es)
append_to_diseno('diseno-en.html', redes_en)

print("Rebuild complete.")
