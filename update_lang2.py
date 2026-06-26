import glob

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Replace in nav-lang (desktop)
    if 'class="nav-lang">Spanish</a>' in content:
        content = content.replace('class="nav-lang">Spanish</a>', 'class="nav-lang">EN/ES</a>')
        modified = True
        
    # Replace in mobile menu
    if '<i class="fas fa-globe"></i> Spanish</a>' in content:
        content = content.replace('<i class="fas fa-globe"></i> Spanish</a>', '<i class="fas fa-globe"></i> EN/ES</a>')
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
