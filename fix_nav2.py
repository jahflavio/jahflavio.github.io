import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

def process_nav(nav_content):
    lines = nav_content.split('\n')
    serv_lines = []
    other_lines = []
    for l in lines:
        if 'servicios.html' in l or 'servicios-en.html' in l:
            serv_lines.append(l)
        else:
            other_lines.append(l)
            
    # Find insert index: just before English
    insert_idx = len(other_lines)
    for i, l in enumerate(other_lines):
        if 'English' in l or 'Español' in l or 'nav-lang' in l or 'globe' in l:
            # Check if previous is nav-separator
            if i > 0 and 'nav-separator' in other_lines[i-1]:
                insert_idx = i - 1
            else:
                insert_idx = i
            break
            
    return '\n'.join(other_lines[:insert_idx] + serv_lines + other_lines[insert_idx:])


for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig_content = content
    
    # Process nav-links
    def repl_nav(m):
        return '<div class="nav-links">' + process_nav(m.group(1)) + '</div>'
        
    content = re.sub(r'<div class="nav-links">(.*?)</div>', repl_nav, content, flags=re.DOTALL)
    
    # Process mobile-menu
    def repl_mob(m):
        return m.group(1) + process_nav(m.group(2)) + '</div>'
        
    content = re.sub(r'(<div id="mobile-menu"[^>]*>)(.*?)(</div>)', repl_mob, content, flags=re.DOTALL)
    
    if content != orig_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

print("Done")
