import re

def revert_links(filename, lang='es'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if lang == 'es':
        pdf_file = "assets/CV_Fabian_Flores_v2.pdf"
        desktop_text = "Descargar PDF"
        mobile_text = "Descargar CV PDF"
    else:
        pdf_file = "assets/CV_Fabian_Flores_EN_v2.pdf"
        desktop_text = "Download PDF"
        mobile_text = "Download CV PDF"

    # Replace Desktop button
    # Currently it is: <a href="cv-general.html" target="_blank" class="editorial-btn editorial-btn-filled" style="background-color: #ffffff !important; color: #000000 !important;"><i class="fas fa-file-pdf"></i> Descargar CV (PDF)</a>
    
    # We want to replace ONLY the href and text, keeping classes and style.
    # regex to match href="cv-general.html" or href="cv-general-en.html"
    content = re.sub(
        r'href="cv-general(?:-en)?\.html"([^>]+)><i class="fas fa-file-pdf"></i>.*?</a>',
        f'href="{pdf_file}" download="{pdf_file.split("/")[-1]}"\\1><i class="fas fa-file-pdf"></i> {desktop_text}</a>',
        content
    )

    # Revert Mobile menu link
    # Currently it is: <a href="assets/CV_Fabian_Flores_v2.pdf" download="CV_Fabian_Flores_v2.pdf" target="_blank"><i class="fas fa-file-pdf"></i> Descargar CV PDF</a>
    # Wait, the previous script DID NOT touch the mobile menu in fix_pdf_links.py! 
    # Let's ensure mobile menu is correct.
    content = re.sub(
        r'<a href="cv-general(-en)?\.html" target="_blank"><i class="fas fa-file-pdf"></i>.*?</a>',
        f'<a href="{pdf_file}" download="{pdf_file.split("/")[-1]}" target="_blank"><i class="fas fa-file-pdf"></i> {mobile_text}</a>',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Reverted links in {filename}")

if __name__ == '__main__':
    revert_links('index.html', 'es')
    revert_links('index-en.html', 'en')
