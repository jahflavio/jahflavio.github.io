import re

with open('index-en.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '<html lang="es">': '<html lang="en">',
    'CV - Fabián Flores | Desarrollador Front-End': 'CV - Fabián Flores | Front-End Developer',
    'Desarrollador Front-End y Comunicador Visual. Especialista en crear experiencias web responsivas, intuitivas y de alto rendimiento con HTML5, CSS3, JavaScript, y optimización SEO.': 'Front-End Developer and Visual Communicator. Specialist in creating responsive, intuitive, and high-performance web experiences with HTML5, CSS3, JavaScript, and SEO optimization.',
    'Desarrollador Front-End y Comunicador Visual. Especialista en crear experiencias web responsivas, intuitivas y de alto rendimiento.': 'Front-End Developer and Visual Communicator. Specialist in creating responsive, intuitive, and high-performance web experiences.',
    'Comunicador Visual y Desarrollador Front-End especializado en crear experiencias web\n                        responsivas, intuitivas y de alto rendimiento. Experto en transformar diseños complejos en\n                        código limpio (HTML5, CSS3, JS) y optimizar para SEO y UX.': 'Visual Communicator and Front-End Developer specialized in creating responsive,\n                        intuitive, and high-performance web experiences. Expert in transforming complex designs into\n                        clean code (HTML5, CSS3, JS) and optimizing for SEO and UX.',
    'proyectos.html': 'proyectos-en.html',
    'diseno.html': 'diseno-en.html',
    'ux-ui.html': 'ux-ui-en.html',
    'Proyectos Web': 'Web Projects',
    'Diseño Gráfico': 'Graphic Design',
    'Diseño UX/UI': 'UX/UI Design',
    'Diseño & UX': 'Design & UX',
    'Prototipado UI': 'UI Prototyping',
    'Diseño Responsivo': 'Responsive Design',
    'Accesibilidad (WCAG)': 'Accessibility (WCAG)',
    'SEO Técnico (On/Off Page)': 'Technical SEO (On/Off Page)',
    'Educación': 'Education',
    'Lic. Comunicación Visual': 'BA Visual Communication',
    'Universidad de la Comunicación': 'University of Communication',
    'Dic 2005 - Jun 2009': 'Dec 2005 - Jun 2009',
    'Idiomas': 'Languages',
    'Español': 'Spanish',
    'Nativo': 'Native',
    'Inglés': 'English',
    'Profesional': 'Professional',
    'Experiencia Profesional': 'Professional Experience',
    'Desarrollo de interfaces web responsivas y landing pages de alta conversión.': 'Development of responsive web interfaces and high-converting landing pages.',
    'Implementación pixel-perfect de diseños UX/UI con HTML5, CSS3 y JS.': 'Pixel-perfect implementation of UX/UI designs with HTML5, CSS3 and JS.',
    'Optimización de Core Web Vitals y SEO técnico para mejorar ranking.': 'Optimization of Core Web Vitals and technical SEO to improve ranking.',
    'Líder de Proyectos Digitales': 'Digital Projects Lead',
    'Lapi\n                                Laboratorio Médico': 'Lapi\n                                Medical Laboratory',
    'Gestión de ciclo de vida de proyectos digitales y coordinación de equipos\n                                dev/design.': 'Digital projects lifecycle management and coordination of dev/design\n                                teams.',
    'Análisis de KPIs y métricas para optimización de estrategias digitales.': 'Analysis of KPIs and metrics to optimize digital strategies.',
    'Diseño y desarrollo de micrositios y assets digitales para campañas.': 'Design and development of microsites and digital assets for campaigns.',
    'Adaptación de creatividades para formatos web responsive.': 'Adaptation of creative assets for responsive web formats.',
    'Maquetación de sitios corporativos y mantenimiento cross-browser.': 'Layout of corporate sites and cross-browser maintenance.',
    'Integración de Heatmaps y Analytics para decisiones de UX.': 'Integration of Heatmaps and Analytics for UX decisions.',
    'Diseño visual y front-end para campañas de marketing.': 'Visual and front-end design for marketing campaigns.',
    'Diseño Gráfico Web': 'Web Graphic Design',
    'Certificaciones Destacadas': 'Featured Certifications',
    'Ciberseguridad': 'Cybersecurity',
    'IA generativa\n                            en RR. HH.: introducción y visión general': 'Generative AI\n                            in HR: Introduction and Overview',
    'Introducción\n                            al diseño de algoritmos': 'Introduction\n                            to Algorithm Design',
    'Marketing\n                            global': 'Global\n                            Marketing',
    'Pilares del\n                            pensamiento computacional': 'Pillars of\n                            Computational Thinking',
    'Primeros pasos\n                            en React': 'First steps\n                            in React',
    'Upskilling y\n                            reskilling: cómo auto reinventarte': 'Upskilling and\n                            reskilling: how to reinvent yourself',
    'Conceptos de\n                            marketing Digital': 'Digital\n                            Marketing Concepts',
    'Fundamentos de\n                            codificación JavaScript II': 'JavaScript\n                            Coding Fundamentals II',
    'Introducción a\n                            páginas web': 'Introduction to\n                            Web Pages',
    'introducción a\n                            páginas web HTML, CSS, JS': 'Introduction to\n                            Web Pages HTML, CSS, JS',
    'Digitaliza\n                            paso a paso tu negocio con herramientas de Google': 'Digitize\n                            your business step by step with Google Tools',
    'Descargar PDF': 'Download PDF'
}

for k, v in replacements.items():
    text = text.replace(k, v)

# Update the language switcher link in index-en.html to point to index.html and show ES instead of English Version
import re
text = re.sub(
    r'<a href="index-en\.html-en\.html"(.*?)<span class="font-bold text-emerald-700">English Version</span>',
    r'<a href="index.html"\1<span class="font-bold text-emerald-700">Versión en Español</span>',
    text, flags=re.DOTALL
)

with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(text)
