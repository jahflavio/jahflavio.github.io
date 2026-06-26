import re

with open('generate_cvs_extra.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all software_icons with the general one
gen_icons = "['text:Ai', 'text:Ps', 'text:Id', 'fab fa-figma', 'fab fa-js', 'fab fa-react', 'fab fa-html5', 'fab fa-css3-alt', 'text:Tw', 'fab fa-wordpress', 'fas fa-chart-line', 'text:Ads', 'fab fa-git-alt', 'text:Pr']"
content = re.sub(r"'software_icons': \[.*?\],", f"'software_icons': {gen_icons},", content)

# Hand Creative Job - ES
hand_creative_es = ",\n        {'title': 'Project Manager', 'company': 'Hand Creative', 'date': 'Jun 2017 - Jul 2019', 'bullets': ['Gestión de ciclo de vida de proyectos y coordinación de equipos de diseño y desarrollo.', 'Análisis de requerimientos y optimización de flujos de trabajo.']}"

# Hand Creative Job - EN
hand_creative_en = ",\n        {'title': 'Project Manager', 'company': 'Hand Creative', 'date': 'Jun 2017 - Jul 2019', 'bullets': ['Managed the project lifecycle and coordinated design and development teams.', 'Analyzed requirements and optimized workflows.']}"

# Append Hand Creative ES where it is missing (UX/UI ES, PM ES)
# For UX/UI ES, it ends with M4 TEL Ago 2019 - May 2020.
content = content.replace(
    "'bullets': ['Creación de assets visuales y layouts intuitivos para tiendas de e-commerce y campañas promocionales.']}\n    ]",
    "'bullets': ['Creación de assets visuales y layouts intuitivos para tiendas de e-commerce y campañas promocionales.']}" + hand_creative_es + "\n    ]"
)

# For PM ES, it ends with M4 TEL Ago 2019 - May 2020.
content = content.replace(
    "'bullets': ['Apoyo en la coordinación de entregables gráficos para campañas de lanzamiento tecnológico.']}\n    ]",
    "'bullets': ['Apoyo en la coordinación de entregables gráficos para campañas de lanzamiento tecnológico.']}" + hand_creative_es + "\n    ]"
)

# Hand Creative EN (UX/UI EN, PM EN)
# UX/UI EN
content = content.replace(
    "'bullets': ['Created visual assets and intuitive layouts for e-commerce stores and high-impact promotional campaigns.']}\n    ]",
    "'bullets': ['Created visual assets and intuitive layouts for e-commerce stores and high-impact promotional campaigns.']}" + hand_creative_en + "\n    ]"
)

# PM EN
content = content.replace(
    "'bullets': ['Supported the coordination of graphic deliverables for high-profile technological product launch campaigns.']}\n    ]",
    "'bullets': ['Supported the coordination of graphic deliverables for high-profile technological product launch campaigns.']}" + hand_creative_en + "\n    ]"
)

with open('generate_cvs_extra.py', 'w', encoding='utf-8') as f:
    f.write(content)
