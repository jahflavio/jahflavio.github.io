import os

css_content = ""
with open('assets/dist-style-CRK6gnrE.css', 'r') as f:
    css_content = f.read()

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'portfolio-gsap.html']

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    # Replace the existing CSS link with the style tag
    import re
    # Match any link tag that looks like it's the main stylesheet
    content = re.sub(r'<link rel="stylesheet".*?href=".*?assets/dist-style.*?".*?>', f'<style>{css_content}</style>', content)
    
    # Also handle the dist-style.css I added manually earlier
    content = content.replace('<link rel="stylesheet" href="dist-style.css">', f'<style>{css_content}</style>')

    # Fallback: if no style tag exists yet, insert before </head>
    if f'<style>{css_content[:20]}' not in content:
        content = content.replace('</head>', f'<style>{css_content}</style>\n</head>')

    with open(filename, 'w') as f:
        f.write(content)

print(f"Injected CSS into {len(html_files)} files.")
