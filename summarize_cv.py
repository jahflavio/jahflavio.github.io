import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

replacements_es = {
    # Freelance
    'Desarrollo integral de interfaces (UI/UX) escalables para aplicaciones móviles y web, garantizando altos estándares de usabilidad, accesibilidad y diseño centrado en el usuario.': 'Desarrollo de interfaces UI/UX escalables para web y móvil, asegurando usabilidad y accesibilidad.',
    'Programación de scripts avanzados y dashboards automatizados en Python orientados al análisis técnico y trading algorítmico en mercados financieros de EE. UU. (MetaTrader 5 / Alpaca Trading).': 'Programación de scripts y dashboards en Python para análisis técnico y trading algorítmico (mercados de EE. UU.).',
    # studioMac
    'Liderazgo en la estrategia digital de la empresa, gestionando y optimizando la arquitectura web corporativa para maximizar la tasa de conversión (CRO) y captación de prospectos.': 'Liderazgo en estrategia digital y optimización de arquitectura web para maximizar CRO y captación.',
    'Planificación y ejecución de campañas multicanal de Marketing Digital (Google Ads geolocalizado y Meta Ads) enfocadas en adquisición y retención de clientes.': 'Ejecución de campañas multicanal (Google Ads, Meta Ads) para adquisición y retención de clientes.',
    'Diseño e impartición de programas curriculares y talleres especializados en UX/UI, maquetación web moderna e ilustración digital.': 'Diseño e impartición de programas formativos en UX/UI, maquetación web e ilustración digital.',
    # B-Drive
    'Creación, gobernanza y mantenimiento de sistemas de diseño (Design Systems) en Figma; maquetación e implementación Front-end con React y Tailwind CSS asegurando SEO técnico y Core Web Vitals.': 'Gobernanza de Design Systems en Figma y desarrollo Front-end (React, Tailwind) con enfoque en SEO técnico.',
    'Diseño y optimización de interfaces de usuario y flujos de navegación para plataformas corporativas (bdrive.ai) y aplicaciones de autoservicio (B-Care canteen app), reduciendo tasas de rebote y tiempos de tarea.': 'Optimización de interfaces y flujos UX para plataformas corporativas, reduciendo tasas de rebote y fricción.',
    # Lapi
    'Dirección de investigación de usuarios (UX Research), entrevistas y auditorías heurísticas para la reestructuración y modernización de plataformas digitales de salud.': 'Dirección de UX Research y auditorías heurísticas para modernizar plataformas digitales de salud.',
    'Formulación y despliegue de estrategias de SEO on-page / técnico y marketing de contenidos, incrementando el posicionamiento orgánico calificado y la conversión transaccional de pacientes.': 'Estrategias SEO técnico/on-page y de contenidos, incrementando posicionamiento orgánico y conversión.',
    # Archer Troy
    'Conceptualización, wireframing y prototipado interactivo de alta fidelidad para micrositios y activaciones publicitarias 360° para cuentas transnacionales.': 'Prototipado interactivo y wireframing de alta fidelidad para campañas 360° de cuentas transnacionales.',
    'Coordinación ágil (Scrum) entre departamentos creativos y equipos de ingeniería de software para asegurar consistencia visual, optimización técnica y medición de eventos en Google Tag Manager.': 'Coordinación ágil (Scrum) de equipos creativos y de ingeniería, asegurando calidad técnica y medición (GTM).',
    # Polyglobal
    'Diseño UI/UX B2B corporativo y administración técnica de ecosistemas web en WordPress y WooCommerce, implementando auditorías de performance y mejores prácticas de SEO (Rank Math / Yoast).': 'Diseño UI/UX B2B y administración de ecosistemas web, optimizando performance y SEO.',
    # Previa
    'Diseño de layouts interactivos y material visual para comercio electrónico y retail de telefonía móvil.': 'Diseño de material visual e interactivo para retail de telefonía móvil.',
    'Gestión ágil de proyectos digitales, control de cronogramas y coordinación directa de equipos de diseño y desarrollo.': 'Gestión ágil de proyectos digitales y coordinación de equipos.'
}

replacements_en = {
    # Freelance
    'Comprehensive development of scalable interfaces (UI/UX) for mobile and web applications, guaranteeing high standards of usability, accessibility, and user-centered design.': 'Development of scalable UI/UX interfaces for web and mobile, ensuring high usability and accessibility standards.',
    'Programming of advanced scripts and automated dashboards in Python oriented towards technical analysis and algorithmic trading in US financial markets (MetaTrader 5 / Alpaca Trading).': 'Programming Python scripts and dashboards for technical analysis and algorithmic trading in US markets.',
    # studioMac
    'Leadership in the company\'s digital strategy, managing and optimizing the corporate web architecture to maximize the conversion rate (CRO) and prospect acquisition.': 'Digital strategy leadership and web architecture optimization to maximize CRO and prospect acquisition.',
    'Planning and execution of omnichannel Digital Marketing campaigns (geolocated Google Ads and Meta Ads) focused on customer acquisition and retention.': 'Execution of omnichannel digital marketing campaigns (Google Ads, Meta Ads) for customer acquisition.',
    'Design and delivery of curricular programs and specialized workshops in UX/UI, modern web layout, and digital illustration.': 'Design and delivery of training programs in UX/UI, modern web development, and digital illustration.',
    # B-Drive
    'Creation, governance, and maintenance of design systems in Figma; Front-end layout and implementation with React and Tailwind CSS, ensuring technical SEO and Core Web Vitals.': 'Governance of Figma Design Systems and Front-end development (React, Tailwind) with technical SEO focus.',
    'Design and optimization of user interfaces and navigation flows for corporate platforms (bdrive.ai) and self-service applications (B-Care canteen app), reducing bounce rates and task times.': 'UX optimization for corporate platforms and applications, reducing bounce rates and improving task efficiency.',
    # Lapi
    'Leadership in user research (UX Research), interviews, and heuristic audits for the restructuring and modernization of corporate digital health platforms.': 'Leadership in UX Research and heuristic audits to modernize corporate digital health platforms.',
    'Formulation and deployment of on-page/technical SEO and content marketing strategies, increasing qualified organic positioning and transactional patient conversion.': 'Technical/On-page SEO and content strategies, increasing organic positioning and patient conversion.',
    # Archer Troy
    'Conceptualization, wireframing, and high-fidelity interactive prototyping for microsites and 360° interactive advertising campaigns for transnational accounts.': 'Interactive prototyping and high-fidelity wireframing for 360° advertising campaigns of global accounts.',
    'Agile coordination (Scrum) between creative departments and software engineering teams to ensure visual consistency, technical optimization, and event measurement in Google Tag Manager.': 'Agile coordination (Scrum) of creative and engineering teams, ensuring technical quality and GTM tracking.',
    # Polyglobal
    'B2B corporate UI/UX design and technical administration of web ecosystems in WordPress and WooCommerce, implementing performance audits and SEO best practices (Rank Math / Yoast).': 'B2B UI/UX design and technical administration of web ecosystems, optimizing performance and SEO.',
    # Previa
    'Design of interactive layouts and visual material for e-commerce and mobile telephony retail.': 'Design of interactive layouts and visual materials for mobile telephony retail.',
    'Agile management of digital projects, timeline control, and direct coordination of design and development teams.': 'Agile management of digital projects and direct coordination of design and development teams.'
}

update_file('cv-profesional-unificado.html', replacements_es)
update_file('cv-profesional-unificado-en.html', replacements_en)
