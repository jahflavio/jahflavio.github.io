import os
import re

files = ['index.html', 'index-en.html']

for filename in files:
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Hide navbar
    content = re.sub(
        r'<nav class="fixed top-0 w-full z-50',
        r'<nav class="fixed top-0 w-full z-50 print:hidden',
        content
    )
    
    # Hide background effects
    content = content.replace('w-[600px] h-[600px] bg-accent/10 rounded-full blur-[120px] -z-10 pointer-events-none"', 'w-[600px] h-[600px] bg-accent/10 rounded-full blur-[120px] -z-10 pointer-events-none print:hidden"')
    content = content.replace('w-[400px] h-[400px] bg-purple-600/5 rounded-full blur-[100px] -z-10 pointer-events-none"', 'w-[400px] h-[400px] bg-purple-600/5 rounded-full blur-[100px] -z-10 pointer-events-none print:hidden"')
    
    # Hide hero buttons
    content = content.replace('hero-text flex flex-wrap gap-4 pt-4"', 'hero-text flex flex-wrap gap-4 pt-4 print:hidden"')
    
    # Hide footer
    content = re.sub(
        r'<footer class="w-full bg-slate-50',
        r'<footer class="w-full bg-slate-50 print:hidden',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Print classes added.")
