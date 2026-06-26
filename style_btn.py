import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The user wants "fondo blanco con letras negras" (white background with black text)
    # We will replace the class `editorial-btn-filled` with a new style.
    
    # Let's just find the button in the hero and add the style to it.
    # In index.html: <a href="cv-general.html" target="_blank" class="editorial-btn editorial-btn-filled">
    # We'll replace it with: <a href="cv-general.html" target="_blank" class="editorial-btn editorial-btn-filled" style="background-color: #ffffff; color: #000000;">
    
    content = content.replace(
        'class="editorial-btn editorial-btn-filled">',
        'class="editorial-btn editorial-btn-filled" style="background-color: #ffffff !important; color: #000000 !important;">'
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('index.html')
update_file('index-en.html')
print("Done")
