import os
import re

FILES = ['proyectos.html', 'proyectos-en.html']

def reorder_projects():
    for filepath in FILES:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract the gallery section
        start_marker = '<div class="editorial-gallery">'
        end_marker = '</section>'
        
        start_idx = content.find(start_marker)
        if start_idx == -1:
            continue
            
        start_idx += len(start_marker)
        end_idx = content.find(end_marker, start_idx)
        
        gallery_content = content[start_idx:end_idx]
        
        # Split into individual items using '<!-- Project' as delimiter
        # But we must be careful since there's an ending </div> for the editorial-gallery inside gallery_content
        # Actually, let's find the closing </div> of editorial-gallery. It is right before </section>
        
        items_raw = re.split(r'(?=<!-- Project)', gallery_content)
        
        # There's whitespace before the first project, keep it.
        pre_content = items_raw[0]
        items = items_raw[1:]
        
        # The last item might contain the closing </div> for the editorial-gallery.
        # Let's clean it up:
        last_item = items[-1]
        closing_div_idx = last_item.rfind('</div>')
        # Actually, the last closing div is for the gallery. We need to be careful.
        # Let's just use regular expressions to extract each gallery-item completely.
        
        items = re.findall(r'<!-- Project \d+ -->\s*<div class="gallery-item">.*?</div>\s*</article>\s*</div>', gallery_content, flags=re.DOTALL)
        
        # Also need the trailing closing div
        trailing = "\n        </div>\n    "
        
        # Now reorder the items
        def get_identifier(item_html):
            if 'B drive' in item_html: return 1
            if 'HUNTRESS' in item_html: return 2
            if 'studioMac' in item_html: return 3
            if 'Dcobys TRAVEL' in item_html: return 4
            if 'Dcobys Consulting' in item_html: return 5
            # the rest stay in their original relative order (Polyglobals, then Essence)
            # They were 4, 5, 8, 9. 
            if 'Polyglobal MX' in item_html: return 6
            if 'Polyglobal US' in item_html: return 7
            if 'Essence MX' in item_html: return 8
            if 'Essenzia' in item_html: return 9
            return 99

        items.sort(key=get_identifier)
        
        # Renumber the comments <!-- Project X -->
        for i in range(len(items)):
            items[i] = re.sub(r'<!-- Project \d+ -->', f'<!-- Project {i+1} -->', items[i])
            
        new_gallery_content = "\n            " + "\n\n            ".join(items) + trailing
        
        new_content = content[:start_idx] + new_gallery_content + content[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Reordered projects in {filepath}")

if __name__ == '__main__':
    reorder_projects()
