import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig_content = content

    # 1. Add nav-scroll.js before </body> if not present
    if 'nav-scroll.js' not in content:
        content = content.replace('</body>', '    <script src="nav-scroll.js"></script>\n</body>')
    
    # 2. Move Servicios to the end of the navigation list
    
    # Let's extract the nav-links block
    nav_links_match = re.search(r'<div class="nav-links">(.*?)</div>', content, re.DOTALL)
    if nav_links_match:
        nav_links = nav_links_match.group(1)
        # Find servicios links
        # Could be <a href="servicios.html">Servicios</a> or <a href="servicios.html#marketing">Marketing</a>
        
        # We find all lines containing servicios.html
        lines = nav_links.split('\n')
        servicios_lines = [l for l in lines if 'servicios.html' in l]
        other_lines = [l for l in lines if 'servicios.html' not in l]
        
        # Where to insert? Before the English link or at the end
        # Find index of line containing 'English' or 'nav-lang'
        insert_idx = len(other_lines)
        for i, l in enumerate(other_lines):
            if 'English' in l or 'nav-lang' in l:
                # also consider if the previous line is a separator
                if i > 0 and 'nav-separator' in other_lines[i-1]:
                    insert_idx = i - 1
                else:
                    insert_idx = i
                break
        
        new_lines = other_lines[:insert_idx] + servicios_lines + other_lines[insert_idx:]
        new_nav_links = '\n'.join(new_lines)
        
        content = content.replace(nav_links_match.group(0), f'<div class="nav-links">{new_nav_links}</div>')

    # 3. Do the same for mobile-menu
    mobile_menu_match = re.search(r'(<div id="mobile-menu"[^>]*>)(.*?)(</div>)', content, re.DOTALL)
    if mobile_menu_match:
        prefix = mobile_menu_match.group(1)
        mobile_menu = mobile_menu_match.group(2)
        suffix = mobile_menu_match.group(3)
        
        lines = mobile_menu.split('\n')
        servicios_lines = [l for l in lines if 'servicios.html' in l]
        other_lines = [l for l in lines if 'servicios.html' not in l]
        
        insert_idx = len(other_lines)
        for i, l in enumerate(other_lines):
            if 'English' in l or 'nav-lang' in l or 'globe' in l:
                insert_idx = i
                break
        
        new_lines = other_lines[:insert_idx] + servicios_lines + other_lines[insert_idx:]
        new_mobile_menu = '\n'.join(new_lines)
        
        content = content.replace(mobile_menu_match.group(0), f'{prefix}{new_mobile_menu}{suffix}')
        
    if content != orig_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

print("Done")
