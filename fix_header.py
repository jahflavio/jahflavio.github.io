import re

def fix_header(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the .page to have NO horizontal padding (so yellow extends full width)
    #    The header already uses negative margins (-mx-[2cm]) to compensate for padding
    #    Instead, we'll restructure so body has no padding and yellow is truly full-width.

    # 2. Change the header yellow section:
    #    Current: p-[2cm] print:p-[2cm] print:pb-[3cm] pb-12
    #    Want: same padding top/sides as what we started with, but reduce bottom to match top
    #    The top padding is 2cm, bottom is 3cm (print) or pb-12. Reduce to match top.
    
    # Fix yellow header: reduce pb to match pt (equal padding)
    content = content.replace(
        'class="-mt-[2cm] -mx-[2cm] print:-mt-[1.5cm] print:-mx-[2cm] bg-[#d4e036] p-[2cm] print:p-[2cm] print:pb-[3cm] pb-12 flex gap-8 relative"',
        'class="-mt-[2cm] -mx-[2cm] print:-mt-[1.5cm] print:-mx-[2cm] bg-[#d4e036] p-[2cm] print:p-[2cm] pb-[2cm] flex gap-8 relative"'
    )

    # 3. Make the page full-width (no white margin frame).
    #    Change: max-width: 21cm; margin: 2cm auto; padding: 2cm;
    #    To: max-width: 100%; margin: 0; padding: 2cm; (no horizontal centering)
    
    # Fix .page in <style>
    content = content.replace(
        '        .page {\r\n            max-width: 21cm;\r\n            min-height: 29.7cm;\r\n            margin: 2cm auto;\r\n            background-color: var(--bg-color);\r\n            padding: 2cm;\r\n            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);\r\n        }',
        '        .page {\r\n            max-width: 100%;\r\n            min-height: 29.7cm;\r\n            margin: 0;\r\n            background-color: var(--bg-color);\r\n            padding: 2cm;\r\n            box-shadow: none;\r\n        }'
    )

    # Also fix body background to white (not grey)
    content = content.replace(
        '            background-color: #f5f5f5;',
        '            background-color: #ffffff;'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed: {filename}")

fix_header('cv-general.html')
fix_header('cv-general-en.html')
