import re

# index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'<a href="assets/CV_Fabian_Flores_v2.pdf".*?Descargar PDF</a>',
    '<a href="cv-general.html" target="_blank" class="editorial-btn editorial-btn-filled"><i class="fas fa-file-pdf"></i> Descargar CV (PDF)</a>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# index-en.html
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'<a href="assets/CV_Fabian_Flores_EN_v2.pdf".*?Download PDF</a>',
    '<a href="cv-general-en.html" target="_blank" class="editorial-btn editorial-btn-filled"><i class="fas fa-file-pdf"></i> Download CV (PDF)</a>',
    content
)

with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated links to point to cv-general.html and cv-general-en.html")
