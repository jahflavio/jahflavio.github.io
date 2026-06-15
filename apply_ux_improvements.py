import os
import glob
import re

css_addition = """
/* Compact Hero for subpages */
.editorial-hero--compact {
    min-height: 40vh !important;
    padding: 8rem 1.5rem 3rem !important;
}
@media (min-width: 768px) {
    .editorial-hero--compact {
        min-height: 40vh !important;
        padding: 10rem 3rem 4rem !important;
    }
}
@media (min-width: 1024px) {
    .editorial-hero--compact {
        padding: 10rem 6rem 5rem !important;
    }
}
"""

min_css_addition = ".editorial-hero--compact{min-height:40vh!important;padding:8rem 1.5rem 3rem!important}@media(min-width:768px){.editorial-hero--compact{min-height:40vh!important;padding:10rem 3rem 4rem!important}}@media(min-width:1024px){.editorial-hero--compact{padding:10rem 6rem 5rem!important}}"

def update_css():
    # Update editorial.css
    with open('editorial.css', 'r', encoding='utf-8') as f:
        content = f.read()
    if '.editorial-hero--compact' not in content:
        content += css_addition
        with open('editorial.css', 'w', encoding='utf-8') as f:
            f.write(content)

    # Update editorial.min.css
    with open('editorial.min.css', 'r', encoding='utf-8') as f:
        content = f.read()
    if '.editorial-hero--compact' not in content:
        content += min_css_addition
        with open('editorial.min.css', 'w', encoding='utf-8') as f:
            f.write(content)

def update_html_files():
    files = [
        'proyectos.html', 'proyectos-en.html',
        'servicios.html', 'servicios-en.html',
        'diseno.html', 'diseno-en.html',
        'ux-ui.html', 'ux-ui-en.html'
    ]
    for filename in files:
        if not os.path.exists(filename):
            continue
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update hero section class
        if 'editorial-hero--compact' not in content:
            content = content.replace('class="editorial-hero editorial-hero--dark"', 'class="editorial-hero editorial-hero--dark editorial-hero--compact"')
            content = content.replace("class='editorial-hero editorial-hero--dark'", "class='editorial-hero editorial-hero--dark editorial-hero--compact'")

        # Update title inline styles
        # Old: style="font-size: clamp(2.5rem, 6vw, 4rem); text-transform: none; line-height: 1.1; margin-bottom: 1rem;"
        # We will use regex to catch variations of clamp(..., 4rem) and change to clamp(3.5rem, 8vw, 5.5rem)
        content = re.sub(
            r'font-size:\s*clamp\([^,]+,\s*[^,]+,\s*4rem\)',
            'font-size: clamp(3.5rem, 8vw, 5.5rem)',
            content
        )
        # Give title more margin bottom if subtitle is right below
        content = content.replace('margin-bottom: 1rem;', 'margin-bottom: 1.5rem;')

        # For "ux-ui.html" and "proyectos.html", there's an inner div that aligns it. It's okay.
        # Let's add a bit more modern touch to the subtilte
        content = content.replace('color: #cccccc;', 'color: #e2e8f0; font-weight: 300;')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

if __name__ == '__main__':
    update_css()
    update_html_files()
    print("Done")
