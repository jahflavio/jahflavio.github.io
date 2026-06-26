import re

def update_button(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the button and add inline styles
    content = re.sub(
        r'(<a href="assets/CV_Fabian_Flores.*?\.pdf" download=".*?" target="_blank" class="editorial-btn">)',
        r'\1'.replace('class="editorial-btn"', 'class="editorial-btn" style="background: #ffffff; color: #000000 !important; font-weight: 700; border: none;"'),
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

if __name__ == '__main__':
    update_button('index.html')
    update_button('index-en.html')
