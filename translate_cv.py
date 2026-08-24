import re

with open('cv-profesional-unificado-en.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    '<html lang="es">': '<html lang="en">',
    'Volver a Web': 'Back to Web',
    'Imprimir PDF': 'Print PDF',
    'Comunicador Audiovisual y Líder de Producto Digital con sólida trayectoria integrando Diseño de Experiencia de Usuario (UX/UI), Desarrollo Web Front-End (React, GSAP, Tailwind) y Estrategia Integral de Marketing Digital (SEO/SEM, CRO, GA4). Especialista en gobernar el ciclo de vida completo de productos digitales: desde investigación de usuarios, arquitectura de información y diseño atómico, hasta la implementación técnica en código, analítica avanzada y optimización de rentabilidad del negocio.': 'Audiovisual Communicator and Digital Product Lead with a solid track record integrating User Experience Design (UX/UI), Front-End Web Development (React, GSAP, Tailwind) and Comprehensive Digital Marketing Strategy (SEO/SEM, CRO, GA4). Specialist in governing the complete lifecycle of digital products: from user research, information architecture and atomic design, to technical code implementation, advanced analytics and business profitability optimization.',
    'Experiencia Profesional': 'Professional Experience',
    'Maestro Diseño, Diseño Web & Mkt. Digital': 'Design Instructor, Web Design & Digital Mkt.',
    'Ene 2026 - Presente': 'Jan 2026 - Present',
    'Liderazgo en la estrategia digital de la empresa, gestionando y optimizando la arquitectura web corporativa para maximizar la tasa de conversión (CRO) y captación de prospectos.': 'Leadership in the company\'s digital strategy, managing and optimizing the corporate web architecture to maximize the conversion rate (CRO) and prospect acquisition.',
    'Planificación y ejecución de campañas multicanal de Marketing Digital (Google Ads geolocalizado y Meta Ads) enfocadas en adquisición y retención de clientes.': 'Planning and execution of omnichannel Digital Marketing campaigns (geolocated Google Ads and Meta Ads) focused on customer acquisition and retention.',
    'Diseño e impartición de programas curriculares y talleres especializados en UX/UI, maquetación web moderna e ilustración digital.': 'Design and delivery of curricular programs and specialized workshops in UX/UI, modern web layout, and digital illustration.',
    'App Designer & Programador Freelance': 'Freelance App Designer & Programmer',
    'Desarrollo integral de interfaces (UI/UX) escalables para aplicaciones móviles y web, garantizando altos estándares de usabilidad, accesibilidad y diseño centrado en el usuario.': 'Comprehensive development of scalable interfaces (UI/UX) for mobile and web applications, guaranteeing high standards of usability, accessibility, and user-centered design.',
    'Programación de scripts avanzados y dashboards automatizados en Python orientados al análisis técnico y trading algorítmico en mercados financieros de EE. UU. (MetaTrader 5 / Alpaca Trading).': 'Programming of advanced scripts and automated dashboards in Python oriented towards technical analysis and algorithmic trading in US financial markets (MetaTrader 5 / Alpaca Trading).',
    'May 2024 - Dic 2025': 'May 2024 - Dec 2025',
    'Creación, gobernanza y mantenimiento de sistemas de diseño (Design Systems) en Figma; maquetación e implementación Front-end con React y Tailwind CSS asegurando SEO técnico y Core Web Vitals.': 'Creation, governance, and maintenance of design systems in Figma; Front-end layout and implementation with React and Tailwind CSS, ensuring technical SEO and Core Web Vitals.',
    'Diseño y optimización de interfaces de usuario y flujos de navegación para plataformas corporativas (bdrive.ai) y aplicaciones de autoservicio (B-Care canteen app), reduciendo tasas de rebote y tiempos de tarea.': 'Design and optimization of user interfaces and navigation flows for corporate platforms (bdrive.ai) and self-service applications (B-Care canteen app), reducing bounce rates and task times.',
    'Líder de Proyectos Digitales & UX': 'Digital Projects & UX Lead',
    'Sep 2023 - Dic 2023': 'Sep 2023 - Dec 2023',
    'Dirección de investigación de usuarios (UX Research), entrevistas y auditorías heurísticas para la reestructuración y modernización de plataformas digitales de salud.': 'Leadership in user research (UX Research), interviews, and heuristic audits for the restructuring and modernization of corporate digital health platforms.',
    'Formulación y despliegue de estrategias de SEO on-page / técnico y marketing de contenidos, incrementando el posicionamiento orgánico calificado y la conversión transaccional de pacientes.': 'Formulation and deployment of on-page/technical SEO and content marketing strategies, increasing qualified organic positioning and transactional patient conversion.',
    'May 2022 - Ago 2023': 'May 2022 - Aug 2023',
    'Conceptualización, wireframing y prototipado interactivo de alta fidelidad para micrositios y activaciones publicitarias 360° para cuentas transnacionales.': 'Conceptualization, wireframing, and high-fidelity interactive prototyping for microsites and 360° interactive advertising campaigns for transnational accounts.',
    'Coordinación ágil (Scrum) entre departamentos creativos y equipos de ingeniería de software para asegurar consistencia visual, optimización técnica y medición de eventos en Google Tag Manager.': 'Agile coordination (Scrum) between creative departments and software engineering teams to ensure visual consistency, technical optimization, and event measurement in Google Tag Manager.',
    'Diseño UI/UX B2B corporativo y administración técnica de ecosistemas web en WordPress y WooCommerce, implementando auditorías de performance y mejores prácticas de SEO (Rank Math / Yoast).': 'B2B corporate UI/UX design and technical administration of web ecosystems in WordPress and WooCommerce, implementing performance audits and SEO best practices (Rank Math / Yoast).',
    'Experiencia Previa Destacada': 'Notable Previous Experience',
    'Creación de layouts para e-commerce.': 'Creation of layouts for e-commerce.',
    'Diseño de layouts interactivos y material visual para comercio electrónico y retail de telefonía móvil.': 'Design of interactive layouts and visual material for e-commerce and mobile telephony retail.',
    'Gestión ágil de proyectos digitales, control de cronogramas y coordinación directa de equipos de diseño y desarrollo.': 'Agile management of digital projects, timeline control, and direct coordination of design and development teams.',
    'Competencias': 'Competencies',
    'Hard Skills & Frameworks': 'Hard Skills & Frameworks',
    'UX/UI & Producto:': 'UX/UI & Product:',
    'Arquitectura, Auditorías Heurísticas, Usabilidad, CRO, Wireframing, User Flows.': 'Architecture, Heuristic Audits, Usability, CRO, Wireframing, User Flows.',
    'Mkt Digital & Analytics:': 'Digital Mkt & Analytics:',
    'SEO Técnico y On-Page, GA4, GTM, Search Console, Google Ads, Meta Ads, Media Planning, Email Mkt.': 'Technical & On-Page SEO, GA4, GTM, Search Console, Google Ads, Meta Ads, Media Planning, Email Mkt.',
    'Backend & Auto:': 'Backend & Automation:',
    'Trading algorítmico.': 'Algorithmic trading.',
    'Creative & Gestión:': 'Creative & Management:',
    'Metodología Ágil / Scrum.': 'Agile Methodology / Scrum.',
    'Educación': 'Education',
    'Licenciatura en Comunicación Visual': 'Bachelor\'s Degree in Visual Communication',
    'Universidad de la Comunicación': 'University of Communication',
    'Ago 2005 - Dic 2009': 'Aug 2005 - Dec 2009',
    'Idiomas': 'Languages',
    'Español': 'Spanish',
    'Nativo': 'Native',
    'Inglés': 'English',
    'Avanzado (C1/C2)': 'Advanced (C1/C2)',
    'Certificados Clave': 'Key Certifications',
    'IA en RR.HH. & Algoritmos': 'AI in HR & Algorithms',
    'Ciberseguridad / React': 'Cybersecurity / React',
    'Certificación Scrum': 'Scrum Certification',
    'Mkt Digital / Web Dev': 'Digital Mkt / Web Dev'
}

for es, en in replacements.items():
    html = html.replace(es, en)

with open('cv-profesional-unificado-en.html', 'w', encoding='utf-8') as f:
    f.write(html)
