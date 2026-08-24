import re

def optimize_right_column(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We only want to target the right column which starts with:
    # <div class="w-[35%]">
    # So we can split the file into two parts, before and after that div.
    parts = content.split('<div class="w-[35%]">')
    if len(parts) == 2:
        left_part = parts[0]
        right_part = parts[1]

        # In the right part, change section margins
        right_part = right_part.replace('class="mb-8"', 'class="mb-4"')
        
        # Change header margins
        right_part = right_part.replace('pb-2 mb-4', 'pb-1 mb-2')
        
        # Change Hard Skills list spacing from space-y-2 to space-y-1
        right_part = right_part.replace('class="space-y-2 text-[9.5px]', 'class="space-y-1 text-[9.5px]')
        
        # We can also reduce the height of the certifications items slightly by removing pb-0.5
        right_part = right_part.replace('border-b border-gray-100 pb-0.5', 'border-b border-gray-100 pb-0')

        new_content = left_part + '<div class="w-[35%]">' + right_part
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
optimize_right_column('cv-profesional-unificado.html')
optimize_right_column('cv-profesional-unificado-en.html')
