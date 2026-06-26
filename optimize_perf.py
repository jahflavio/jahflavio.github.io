import re
import glob

def optimize_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Optimize Vanta.js
    content = content.replace('mouseControls: true', 'mouseControls: false')
    content = content.replace('touchControls: true', 'touchControls: false')

    # 2. Add loading="lazy" to imgs that don't have it
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading="lazy"' not in img_tag and 'loading=\'lazy\'' not in img_tag:
            # Inject loading="lazy" right after <img
            return img_tag.replace('<img ', '<img loading="lazy" ')
        return img_tag

    content = re.sub(r'<img [^>]+>', add_lazy, content)
    
    # 3. Increase scale to render at a slightly lower resolution in WebGL (improves perf)
    content = content.replace('scale: 2.00', 'scale: 4.00')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Optimized {filename}")

for f in glob.glob('*.html'):
    optimize_html(f)

