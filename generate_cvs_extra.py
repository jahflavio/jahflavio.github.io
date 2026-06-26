import os
import re

def get_template(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    header_end = content.find('<!-- HEADER -->')
    prefix = content[:header_end]
    
    suffix = '''
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="main-static.js"></script>
</body>
</html>'''
    return prefix, suffix

def build_cv(title_es, role, profile, skills_col1, skills_col2, software_icons, certs, edu, exp, prefix, suffix, lang='es'):
    contact_title = "Contact" if lang == 'en' else "Contacto"
    mexico_city = "Mexico City" if lang == 'en' else "Ciudad de México"
    
    header = f'''<!-- HEADER HYBRID YELLOW -->
        <div class="-mt-[2cm] -mx-[2cm] print:-mt-[1.5cm] print:-mx-[2cm] bg-[#d4e036] p-[2cm] print:p-[2cm] print:pb-[3cm] pb-12 flex gap-8 relative">
            
            <!-- LEFT COLUMN (Contact Info) -->
            <div class="w-[28%] z-10">
                <h3 class="uppercase text-[18px] tracking-widest text-gray-800 mb-4 font-bold">{contact_title}</h3>
                <div class="space-y-4 text-[11px] font-semibold tracking-wide text-gray-800">
                    <p class="flex items-center gap-3"><i class="fas fa-phone w-4 text-center"></i> <a href="tel:+522223441091" class="hover:underline">+52 222 344 1091</a></p>
                    <p class="flex items-center gap-3"><i class="fas fa-envelope w-4 text-center"></i> <a href="mailto:fabianfloram@gmail.com" class="hover:underline">fabianfloram@gmail.com</a></p>
                    <p class="flex items-center gap-3"><i class="fab fa-linkedin-in w-4 text-center"></i> <a href="https://www.linkedin.com/in/fabian-f-71858b209" target="_blank" class="hover:underline">/in/fabian-f-71858b209</a></p>
                    <p class="flex items-center gap-3"><i class="fas fa-globe w-4 text-center"></i> <a href="https://jahflavio.github.io/" target="_blank" class="hover:underline">jahflavio.github.io</a></p>
                    <p class="flex items-center gap-3"><i class="fas fa-map-marker-alt w-4 text-center"></i> {mexico_city}</p>
                </div>
            </div>
            
            <!-- RIGHT COLUMN (Name, Profile) -->
            <div class="w-[72%] z-10">
                <div class="border-t-[3px] border-black pt-4">
                    <h1 class="text-[54px] font-bold leading-none tracking-tight uppercase text-[#1a1a1a]">Fabián Flores</h1>
                    <div class="mt-4 inline-block bg-black text-[#d4e036] font-bold text-[14px] px-5 py-1.5 rounded-full uppercase tracking-widest shadow-sm">
                        {role}
                    </div>
                    <p class="mt-6 text-[11.5px] leading-relaxed text-justify font-medium tracking-wide text-gray-800">
                        {profile}
                    </p>
                </div>
            </div>
            
            <!-- CV BADGE -->
            <div class="absolute -bottom-8 left-[28%] w-16 h-16 bg-white rounded-full border-4 border-black flex items-center justify-center z-20" style="margin-left: -0.5rem;">
                <span class="font-bold text-xl font-display">CV</span>
            </div>
        </div>
'''

    software_html = ""
    if software_icons:
        sw_title = "Software & Tools" if lang == 'en' else "Software y Herramientas"
        software_html = f'''
        <div class="mb-8 mt-8">
            <h3 class="uppercase text-[18px] tracking-widest text-gray-800 mb-4 font-bold">{sw_title}</h3>
            <div class="flex flex-wrap gap-2 text-[18px] text-gray-700">'''
        for icon in software_icons:
            if icon.startswith('text:'):
                text_content = icon.split('text:')[1]
                software_html += f'<span class="font-bold text-[12px] bg-gray-100 text-black border border-gray-300 px-1.5 h-7 min-w-[1.75rem] flex items-center justify-center rounded-md">{text_content}</span>'
            else:
                software_html += f'<div class="w-7 h-7 flex items-center justify-center bg-gray-100 rounded-md border border-gray-300"><i class="{icon} text-[14px]"></i></div>'
        software_html += '</div></div>'

    skills_title = "Skills" if lang == 'en' else "Habilidades"
    skills = f'''
        <!-- BOTTOM WHITE SECTION -->
        <div class="flex gap-8 mt-12 pb-8">
            <!-- LEFT COLUMN (Skills, Software, Certs) -->
            <div class="w-[28%]">
                <div class="mb-8">
                    <h3 class="uppercase text-[18px] tracking-widest text-gray-800 mb-4 font-bold">{skills_title}</h3>
                    <div class="bg-[#f4f2eb] p-3 rounded-xl border border-[#e8e6df]">
                        <ul class="custom-list text-[11px] font-semibold tracking-wide space-y-1">
'''
    for skill in skills_col1 + skills_col2:
        skills += f'                            <li>{skill}</li>\n'
    
    certs_title = "Education & Certifications" if lang == 'en' else "Educación y Certificados"
    certs_html = f'''
        <div class="mb-8 mt-8">
            <h3 class="uppercase text-[18px] tracking-widest text-gray-800 mb-4 font-bold">{certs_title}</h3>
            <div class="mb-5">
                <span class="font-bold text-[11px] uppercase tracking-wide block text-[#1a1a1a]">{edu['title']}</span>
                <span class="text-[10px] text-gray-600 block">{edu['school']} | {edu['date']}</span>
            </div>
            <div class="flex flex-col gap-1.5 text-[10.5px] font-medium tracking-wide">'''
    if certs:
        for cert in certs:
            certs_html += f'<div><span class="font-bold">{cert["title"]}</span> | {cert["issuer"]} | {cert["year"]}</div>\n'
    certs_html += '</div></div>'

    skills += f'''                        </ul>
                    </div>
                </div>
                {software_html}
                {certs_html}
            </div>
            
            <!-- RIGHT COLUMN (Experience, Education) -->
            <div class="w-[72%]">
                <div class="mb-8">
                    <h3 class="uppercase text-[18px] tracking-widest text-gray-800 mb-4 font-bold">{"Experience" if lang=='en' else "Experiencia"}</h3>
'''
    for job in exp:
        skills += f'''
                    <div class="flex gap-4 mb-4 items-start">
                        <div class="w-24 flex-shrink-0 pt-1 text-right border-r-2 border-gray-200 pr-3">
                            <span class="text-[9px] font-bold text-gray-500 uppercase tracking-widest block leading-tight">{job['date']}</span>
                        </div>
                        <div class="flex-1 bg-[#f4f2eb] p-4 rounded-xl border border-[#e8e6df] shadow-sm relative">
                            <div class="absolute top-3 -left-3 w-3 h-[2px] bg-gray-200"></div>
                            <h4 class="font-bold text-[14px] text-[#a3ad29] leading-tight mb-1">{job['title']}</h4>
                            <p class="font-bold text-[11px] text-gray-500 uppercase tracking-wider mb-2">{job['company']}</p>
                            <ul class="custom-list text-[11.5px] font-medium leading-relaxed text-gray-800">
'''
        for bullet in job['bullets']:
            skills += f'                                <li>{bullet}</li>\n'
        skills += '''                            </ul>
                        </div>
                    </div>
'''
    
    skills += f'''
                </div>
            </div>
        </div>
'''
    
    content = prefix + header + skills + suffix
    
    if lang == 'en':
        content = content.replace('index.html', 'index-en.html')
        content = content.replace('Volver a Web', 'Back to Web')
        content = content.replace('Imprimir PDF', 'Print to PDF')
        
    return content

shared_certs_es = [
    {'title': 'Ciberseguridad', 'issuer': 'B drive', 'year': '2025'},
    {'title': 'IA en RR.HH.', 'issuer': 'UBITS', 'year': '2025'},
    {'title': 'Diseño de Algoritmos', 'issuer': 'UBITS', 'year': '2025'},
    {'title': 'Primeros pasos React', 'issuer': 'UBITS', 'year': '2025'},
    {'title': 'Scrum', 'issuer': 'CertJoin', 'year': '2024'},
    {'title': 'SEO', 'issuer': 'HubSpot Academy', 'year': '2024'},
    {'title': 'Foundations of UX', 'issuer': 'Google', 'year': '2022'},
    {'title': 'Conceptos Mkt. Digital', 'issuer': 'Google', 'year': '2021'},
    {'title': 'Mkt. Digital Fund.', 'issuer': 'Google', 'year': '2021'},
    {'title': 'JavaScript II', 'issuer': 'Grasshopper', 'year': '2021'},
    {'title': 'Intro Pág. Web', 'issuer': 'Google', 'year': '2021'},
    {'title': 'HTML, CSS, JS Intro', 'issuer': 'Grasshopper', 'year': '2021'},
    {'title': 'Digitaliza tu Negocio', 'issuer': 'Google', 'year': '2021'},
]

shared_certs_en = [
    {'title': 'Cybersecurity', 'issuer': 'B drive', 'year': '2025'},
    {'title': 'AI in HR', 'issuer': 'UBITS', 'year': '2025'},
    {'title': 'Algorithm Design', 'issuer': 'UBITS', 'year': '2025'},
    {'title': 'React Basics', 'issuer': 'UBITS', 'year': '2025'},
    {'title': 'Scrum', 'issuer': 'CertJoin', 'year': '2024'},
    {'title': 'SEO', 'issuer': 'HubSpot Academy', 'year': '2024'},
    {'title': 'Foundations of UX', 'issuer': 'Google', 'year': '2022'},
    {'title': 'Digital Mkt Concepts', 'issuer': 'Google', 'year': '2021'},
    {'title': 'Digital Mkt Fund.', 'issuer': 'Google', 'year': '2021'},
    {'title': 'JavaScript II', 'issuer': 'Grasshopper', 'year': '2021'},
    {'title': 'Intro to Web Pages', 'issuer': 'Google', 'year': '2021'},
    {'title': 'HTML, CSS, JS Intro', 'issuer': 'Grasshopper', 'year': '2021'},
    {'title': 'Digitize Your Business', 'issuer': 'Google', 'year': '2021'},
]

# UX/UI Data
data_ux_es = {
    'title_es': 'UX/UI Design',
    'role': 'UX/UI Designer',
    'profile': 'UX/UI Designer centrado en el usuario con sólida experiencia en la investigación, conceptualización y diseño de productos digitales. Poseo un enfoque holístico que combina la empatía por las necesidades del usuario con una profunda comprensión técnica del desarrollo front-end. Utilizo metodologías de Design Thinking y herramientas como Figma para crear wireframes, prototipos interactivos y sistemas de diseño escalables. Mi objetivo es resolver problemas complejos mediante interfaces intuitivas, accesibles y estéticamente atractivas que potencien la conversión y satisfacción del cliente.',
    'skills_col1': ['UX Research & User Journeys', 'Diseño de Interfaces (UI) & Sistemas de Diseño', 'Prototipado Interactivo (Figma)', 'Wireframing & Arquitectura de la Información'],
    'skills_col2': ['Pruebas de Usabilidad & A/B Testing', 'Accesibilidad Web (WCAG)', 'HTML5, CSS3, JS (Bases Front-end)', 'Design Thinking & Metodologías Ágiles'],
    'software_icons': ['fab fa-figma', 'fab fa-html5', 'fab fa-css3-alt', 'fab fa-js', 'text:Ps', 'text:Ai'],
    'certs': shared_certs_es,
    'edu': {'title': 'Licenciatura en Comunicación Visual', 'school': 'Universidad de la Comunicación', 'date': 'Ago 2005 - Dic 2009'},
    'exp': [
        {'title': 'UX/UI Designer & Front-end', 'company': 'B-Drive', 'date': 'May 2024 - Dic 2025', 'bullets': ['Diseño y prototipado de interfaces centradas en el usuario, optimizando flujos de navegación para reducir la fricción en landing pages.', 'Creación y mantenimiento de sistemas de diseño escalables en Figma para asegurar consistencia visual en todas las plataformas.', 'Colaboración estrecha con desarrolladores para garantizar una implementación pixel-perfect y el cumplimiento de accesibilidad.']},
        {'title': 'Líder de UX & Proyectos Digitales', 'company': 'Lapi Laboratorio', 'date': 'Ene 2023 - Ene 2024', 'bullets': ['Liderazgo en la investigación de usuarios y auditorías heurísticas para el rediseño de plataformas digitales, mejorando la retención.', 'Definición de user personas y mapeo del customer journey para alinear los objetivos del producto con las necesidades de pacientes.']},
        {'title': 'UX/UI Designer', 'company': 'Archer Troy', 'date': 'Mar 2022 - Dic 2022', 'bullets': ['Conceptualización de flujos de interacción y prototipado de alta fidelidad para micrositios de campañas interactivas.', 'Análisis de comportamiento mediante heatmaps para iterar en el diseño y mejorar la tasa de conversión.']},
        {'title': 'Web & UI Designer', 'company': 'Polyglobal', 'date': 'Jun 2020 - Feb 2022', 'bullets': ['Diseño de interfaces corporativas enfocadas en la usabilidad B2B y adaptación a múltiples dispositivos (Responsive Design).', 'Aplicación de pruebas de usabilidad tempranas para validar conceptos antes de la etapa de desarrollo front-end.']},
        {'title': 'Visual Designer', 'company': 'M4 TEL', 'date': 'Ago 2019 - May 2020', 'bullets': ['Creación de assets visuales y layouts intuitivos para tiendas de e-commerce y campañas promocionales.']}
    ]
}

data_ux_en = {
    'title_es': 'UX/UI Design',
    'role': 'UX/UI Designer',
    'profile': 'User-centered UX/UI Designer with solid experience in research, conceptualization, and digital product design. I take a holistic approach that combines empathy for user needs with a deep technical understanding of front-end development. I utilize Design Thinking methodologies and tools like Figma to create wireframes, interactive prototypes, and scalable design systems. My goal is to solve complex problems through intuitive, accessible, and aesthetically pleasing interfaces that boost conversion and user satisfaction.',
    'skills_col1': ['UX Research & User Journeys', 'User Interface (UI) & Design Systems', 'Interactive Prototyping (Figma)', 'Wireframing & Information Architecture'],
    'skills_col2': ['Usability Testing & A/B Testing', 'Web Accessibility (WCAG)', 'HTML5, CSS3, JS (Front-end Basics)', 'Design Thinking & Agile Methodologies'],
    'software_icons': ['fab fa-figma', 'fab fa-html5', 'fab fa-css3-alt', 'fab fa-js', 'text:Ps', 'text:Ai'],
    'certs': shared_certs_en,
    'edu': {'title': 'BA Visual Communication', 'school': 'University of Communication', 'date': 'Aug 2005 - Dec 2009'},
    'exp': [
        {'title': 'UX/UI Designer & Front-end', 'company': 'B-Drive', 'date': 'May 2024 - Dec 2025', 'bullets': ['Designed and prototyped user-centric interfaces, optimizing navigation flows to significantly reduce friction on landing pages.', 'Created and maintained scalable design systems in Figma to ensure visual consistency across all digital platforms.', 'Collaborated closely with developers to ensure pixel-perfect implementation and strict adherence to accessibility standards.']},
        {'title': 'UX & Digital Projects Lead', 'company': 'Lapi Laboratory', 'date': 'Jan 2023 - Jan 2024', 'bullets': ['Led user research and heuristic audits for the redesign of digital platforms, resulting in improved user retention.', 'Defined user personas and mapped customer journeys to align product goals with the actual needs of healthcare patients.']},
        {'title': 'UX/UI Designer', 'company': 'Archer Troy', 'date': 'Mar 2022 - Dec 2022', 'bullets': ['Conceptualized interaction flows and developed high-fidelity prototypes for interactive campaign microsites.', 'Analyzed user behavior via heatmaps to iteratively improve UI design and maximize overall conversion rates.']},
        {'title': 'Web & UI Designer', 'company': 'Polyglobal', 'date': 'Jun 2020 - Feb 2022', 'bullets': ['Designed corporate interfaces focused on B2B usability, ensuring seamless adaptation across multiple devices (Responsive Design).', 'Conducted early-stage usability testing to validate design concepts prior to front-end development handoff.']},
        {'title': 'Visual Designer', 'company': 'M4 TEL', 'date': 'Aug 2019 - May 2020', 'bullets': ['Created visual assets and intuitive layouts for e-commerce stores and high-impact promotional campaigns.']}
    ]
}

# PM Data
data_pm_es = {
    'title_es': 'Project Management',
    'role': 'Digital Project Manager',
    'profile': 'Digital Project Manager certificado en Scrum, especializado en liderar equipos multidisciplinarios para la entrega exitosa de productos tecnológicos. Con sólida experiencia técnica en desarrollo web, UX/UI y marketing digital, funciono como un puente efectivo entre los stakeholders, el equipo de diseño y los desarrolladores. Me enfoco en la planificación ágil, la gestión de riesgos, el análisis de KPIs y la optimización continua de procesos para asegurar que cada proyecto se entregue a tiempo, dentro del presupuesto y superando los objetivos de negocio.',
    'skills_col1': ['Gestión Ágil de Proyectos (Scrum)', 'Liderazgo de Equipos Multidisciplinarios', 'Planificación de Sprints & Roadmapping', 'Análisis de KPIs & OKRs'],
    'skills_col2': ['Gestión de Presupuesto y Riesgos', 'Comunicación con Stakeholders', 'Background Técnico (Web/UX/SEO)', 'Optimización de Procesos'],
    'software_icons': ['fab fa-trello', 'fab fa-jira', 'fab fa-wordpress', 'fab fa-google'],
    'certs': shared_certs_es,
    'edu': {'title': 'Licenciatura en Comunicación Visual', 'school': 'Universidad de la Comunicación', 'date': 'Ago 2005 - Dic 2009'},
    'exp': [
        {'title': 'Technical Project Manager', 'company': 'B-Drive', 'date': 'May 2024 - Dic 2025', 'bullets': ['Gestión ágil de proyectos de desarrollo web y estrategias digitales, coordinando eficientemente a los equipos técnicos y creativos.', 'Implementación de ceremonias Scrum (Daily, Planning, Retrospective) para mantener la alineación y velocidad de entrega del equipo.', 'Gestión de requerimientos, control de calidad (QA) técnico y despliegue exitoso de plataformas web orientadas a conversión.']},
        {'title': 'Líder de Proyectos Digitales', 'company': 'Lapi Laboratorio', 'date': 'Ene 2023 - Ene 2024', 'bullets': ['Liderazgo en la gestión integral del ciclo de vida de proyectos digitales en el sector salud, desde la definición de alcance hasta el despliegue.', 'Asignación de recursos y monitorización del cumplimiento de presupuestos, asegurando el ROI esperado por la dirección.', 'Comunicación continua con directivos y presentación de reportes de progreso y KPIs mediante dashboards analíticos.']},
        {'title': 'Coordinador Web & Marketing', 'company': 'Archer Troy', 'date': 'Mar 2022 - Dic 2022', 'bullets': ['Coordinación del lanzamiento de campañas publicitarias digitales, asegurando entregas a tiempo en entornos de alta presión.', 'Resolución de bloqueos técnicos entre áreas de diseño, contenido y desarrollo front-end para campañas interactivos.']},
        {'title': 'Gestor de Proyectos Web', 'company': 'Polyglobal', 'date': 'Jun 2020 - Feb 2022', 'bullets': ['Supervisión del desarrollo y mantenimiento de portales corporativos, actuando como enlace principal con clientes internos.', 'Definición de cronogramas y priorización de backlog enfocado en optimizar el rendimiento (WPO) y reducir tasas de abandono.']},
        {'title': 'Diseñador Visual', 'company': 'M4 TEL', 'date': 'Ago 2019 - May 2020', 'bullets': ['Apoyo en la coordinación de entregables gráficos para campañas de lanzamiento tecnológico.']}
    ]
}

data_pm_en = {
    'title_es': 'Project Management',
    'role': 'Digital Project Manager',
    'profile': 'Scrum-certified Digital Project Manager specialized in leading multidisciplinary teams for the successful delivery of technology products. With a solid technical background in web development, UX/UI, and digital marketing, I act as an effective bridge between stakeholders, design teams, and developers. I focus on agile planning, risk management, KPI analysis, and continuous process optimization to ensure every project is delivered on time, within budget, and exceeding business goals.',
    'skills_col1': ['Agile Project Management (Scrum)', 'Multidisciplinary Team Leadership', 'Sprint Planning & Roadmapping', 'KPI & OKR Analysis'],
    'skills_col2': ['Budget & Risk Management', 'Stakeholder Communication', 'Technical Background (Web/UX/SEO)', 'Process Optimization'],
    'software_icons': ['fab fa-trello', 'fab fa-jira', 'fab fa-wordpress', 'fab fa-google'],
    'certs': shared_certs_en,
    'edu': {'title': 'BA Visual Communication', 'school': 'University of Communication', 'date': 'Aug 2005 - Dec 2009'},
    'exp': [
        {'title': 'Technical Project Manager', 'company': 'B-Drive', 'date': 'May 2024 - Dec 2025', 'bullets': ['Managed agile web development projects and digital strategies, efficiently coordinating technical and creative teams.', 'Implemented Scrum ceremonies (Daily, Planning, Retrospective) to maintain team alignment and consistent delivery velocity.', 'Handled requirements gathering, technical Quality Assurance (QA), and the successful deployment of conversion-oriented platforms.']},
        {'title': 'Digital Projects Lead', 'company': 'Lapi Laboratory', 'date': 'Jan 2023 - Jan 2024', 'bullets': ['Led the end-to-end lifecycle management of digital projects in the healthcare sector, from scoping to final deployment.', 'Allocated resources and monitored budget adherence, ensuring the ROI expected by the executive board.', 'Maintained continuous communication with stakeholders and presented progress reports and KPIs via analytical dashboards.']},
        {'title': 'Web & Marketing Coordinator', 'company': 'Archer Troy', 'date': 'Mar 2022 - Dec 2022', 'bullets': ['Coordinated the launch of digital advertising campaigns, ensuring on-time deliverables in high-pressure, fast-paced environments.', 'Resolved technical blockers between design, content, and front-end development areas for interactive campaigns.']},
        {'title': 'Web Project Manager', 'company': 'Polyglobal', 'date': 'Jun 2020 - Feb 2022', 'bullets': ['Supervised the development and maintenance of corporate portals, acting as the primary liaison with internal clients.', 'Defined schedules and prioritized the product backlog, focused on optimizing web performance (WPO) and reducing bounce rates.']},
        {'title': 'Visual Designer', 'company': 'M4 TEL', 'date': 'Aug 2019 - May 2020', 'bullets': ['Supported the coordination of graphic deliverables for high-profile technological product launch campaigns.']}
    ]
}

# General Data
data_general_es = {
    'title_es': 'General',
    'role': 'Digital Marketing, SEO, Front End, UX/UI',
    'profile': 'Comunicador Audiovisual especializado en Multimedia UX Design, Desarrollo Web y Marketing Digital. Con una sólida trayectoria como Diseñador Senior, Media Planner y Project Manager, aporto una visión holística a cada proyecto. Domino HTML, CSS, JS, React, WordPress, Adobe Suite y Figma, integrando estrategias SEO/SEM para asegurar que los productos digitales no solo sean estéticamente impactantes y centrados en el usuario, sino que también alcancen sus objetivos de negocio de manera efectiva.',
    'skills_col1': ['UX/UI Design & Multimedia', 'Desarrollo Web (HTML, CSS, JS)', 'Gestión de Proyectos & Scrum', 'WordPress & E-commerce'],
    'skills_col2': ['Marketing Digital (SEO/SEM)', 'Adobe Suite & Figma', 'Estrategia de Medios', 'Analítica Web (Google)'],
    'software_icons': ['text:Ai', 'text:Ps', 'text:Id', 'fab fa-figma', 'fab fa-js', 'fab fa-react', 'fab fa-html5', 'fab fa-css3-alt', 'text:Tw', 'fab fa-wordpress', 'fas fa-chart-line', 'text:Ads', 'fab fa-git-alt', 'text:Pr'],
    'certs': shared_certs_es,
    'edu': {'title': 'Licenciatura en Comunicación Visual', 'school': 'Universidad de la Comunicación', 'date': 'Ago 2005 - Dic 2009'},
    'exp': [
        {'title': 'Multimedia UX Designer & Front-end', 'company': 'B-Drive', 'date': 'May 2024 - Dic 2025', 'bullets': ['Diseño y prototipado de interfaces centradas en el usuario, optimizando flujos de navegación para reducir la fricción en landing pages.', 'Creación y mantenimiento de sistemas de diseño escalables en Figma para asegurar consistencia visual en todas las plataformas.']},
        {'title': 'Líder de Proyectos Digitales', 'company': 'Lapi Laboratorio', 'date': 'Ene 2023 - Ene 2024', 'bullets': ['Liderazgo en la investigación de usuarios y auditorías heurísticas para el rediseño de plataformas digitales, mejorando la retención.', 'Dirección integral de estrategias SEO y marketing de contenidos, logrando un aumento sostenido en la visibilidad orgánica.']},
        {'title': 'Web & Marketing Coordinator', 'company': 'Archer Troy', 'date': 'Mar 2022 - Dic 2022', 'bullets': ['Conceptualización de flujos de interacción y prototipado de alta fidelidad para micrositios de campañas interactivas.', 'Coordinación del lanzamiento de campañas publicitarias digitales, asegurando entregas a tiempo en entornos de alta presión.']},
        {'title': 'Web & UI Designer', 'company': 'Polyglobal', 'date': 'Jun 2020 - Feb 2022', 'bullets': ['Diseño de interfaces corporativas enfocadas en la usabilidad B2B y adaptación a múltiples dispositivos (Responsive Design).', 'Administración y mantenimiento integral de sitios web corporativos en WordPress, optimizando el rendimiento (WPO).']},
        {'title': 'Visual Designer', 'company': 'M4 TEL', 'date': 'Ago 2019 - May 2020', 'bullets': ['Creación de assets visuales y layouts intuitivos para tiendas de e-commerce y campañas promocionales.']}
    ]
}

data_general_en = {
    'title_es': 'General',
    'role': 'Digital Marketing, SEO, Front End, UX/UI',
    'profile': 'Audiovisual Communicator specializing in Multimedia UX Design, Web Development, and Digital Marketing. With a solid background as a Senior Designer, Media Planner, and Project Manager, I bring a holistic vision to every project. I am proficient in HTML, CSS, JS, React, WordPress, Adobe Suite, and Figma, integrating SEO/SEM strategies to ensure that digital products are not only aesthetically striking and user-centered but also achieve their business goals effectively.',
    'skills_col1': ['UX/UI Design & Multimedia', 'Web Development (HTML, CSS, JS)', 'Project Management & Scrum', 'WordPress & E-commerce'],
    'skills_col2': ['Digital Marketing (SEO/SEM)', 'Adobe Suite & Figma', 'Media Planning', 'Web Analytics (Google)'],
    'software_icons': ['text:Ai', 'text:Ps', 'text:Id', 'fab fa-figma', 'fab fa-js', 'fab fa-react', 'fab fa-html5', 'fab fa-css3-alt', 'text:Tw', 'fab fa-wordpress', 'fas fa-chart-line', 'text:Ads', 'fab fa-git-alt', 'text:Pr'],
    'certs': shared_certs_en,
    'edu': {'title': 'BA Visual Communication', 'school': 'University of Communication', 'date': 'Aug 2005 - Dec 2009'},
    'exp': [
        {'title': 'Multimedia UX Designer & Front-end', 'company': 'B-Drive', 'date': 'May 2024 - Dec 2025', 'bullets': ['Designed and prototyped user-centric interfaces, optimizing navigation flows to significantly reduce friction on landing pages.', 'Created and maintained scalable design systems in Figma to ensure visual consistency across all digital platforms.']},
        {'title': 'Digital Projects Lead', 'company': 'Lapi Laboratory', 'date': 'Jan 2023 - Jan 2024', 'bullets': ['Led user research and heuristic audits for the redesign of digital platforms, resulting in improved user retention.', 'Comprehensive direction of SEO strategies and content marketing, achieving a sustained increase in organic visibility.']},
        {'title': 'Web & Marketing Coordinator', 'company': 'Archer Troy', 'date': 'Mar 2022 - Dec 2022', 'bullets': ['Conceptualized interaction flows and developed high-fidelity prototypes for interactive campaign microsites.', 'Coordinated the launch of digital advertising campaigns, ensuring on-time deliverables in high-pressure environments.']},
        {'title': 'Web & UI Designer', 'company': 'Polyglobal', 'date': 'Jun 2020 - Feb 2022', 'bullets': ['Designed corporate interfaces focused on B2B usability, ensuring seamless adaptation across multiple devices (Responsive Design).', 'Comprehensive administration and maintenance of corporate websites in WordPress, optimizing web performance (WPO).']},
        {'title': 'Visual Designer', 'company': 'M4 TEL', 'date': 'Aug 2019 - May 2020', 'bullets': ['Created visual assets and intuitive layouts for e-commerce stores and high-impact promotional campaigns.']}
    ]
}

def main():
    prefix_es, suffix_es = get_template("cv-seo.html")
    prefix_en, suffix_en = get_template("cv-seo-en.html")
    
    def write_cv(filename, data, prefix, suffix, lang='es'):
        html = build_cv(
            data['title_es'],
            data['role'],
            data['profile'],
            data['skills_col1'],
            data['skills_col2'],
            data.get('software_icons', []),
            data.get('certs', []),
            data['edu'],
            data['exp'],
            prefix,
            suffix,
            lang
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created {filename}")

    write_cv("cv-ux-ui.html", data_ux_es, prefix_es, suffix_es, 'es')
    write_cv("cv-ux-ui-en.html", data_ux_en, prefix_en, suffix_en, 'en')
    write_cv("cv-project-manager.html", data_pm_es, prefix_es, suffix_es, 'es')
    write_cv("cv-project-manager-en.html", data_pm_en, prefix_en, suffix_en, 'en')
    write_cv("cv-general.html", data_general_es, prefix_es, suffix_es, 'es')
    write_cv("cv-general-en.html", data_general_en, prefix_en, suffix_en, 'en')

if __name__ == "__main__":
    main()

