import os

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'portfolio-gsap.html']

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    # 1. Add CSS link if not present (pointing to dist-style.css)
    if 'dist-style.css' not in content:
        # Insert before </head>
        css_tag = '<link rel="stylesheet" href="dist-style.css">'
        content = content.replace('</head>', f'    {css_tag}\n</head>')
    
    # 2. Add GSAP CDN and main-static.js if not present
    if 'main-static.js' not in content:
        js_tags = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="main-static.js"></script>
"""
        # Insert before </body>
        content = content.replace('</body>', f'{js_tags}\n</body>')

    # 3. Remove Vite script tag if present
    content = content.replace('<script type="module" src="/main.js"></script>', '')
    
    with open(filename, 'w') as f:
        f.write(content)

print(f"Updated {len(html_files)} files to use static assets.")
