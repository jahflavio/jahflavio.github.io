import glob, re
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'servicios.html#marketing' in content or 'services.html#marketing' in content:
        print('Found in ' + file)
        content = re.sub(r'\s*<a href="servicios.html#marketing">Marketing</a>', '', content)
        content = re.sub(r'\s*<a href="services.html#marketing">Marketing</a>', '', content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
