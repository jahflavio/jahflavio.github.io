import os
import re
from PIL import Image

# Directories
ASSETS_DIR = 'assets'
HTML_FILES = [
    'diseno.html', 'diseno-en.html',
    'ux-ui.html', 'ux-ui-en.html',
    'proyectos.html', 'proyectos-en.html',
    'index.html', 'index-en.html',
    'cv-impresion.html', 'cv-impresion-en.html'
]
CSS_FILES = ['editorial.css']

MAX_WIDTH = 1920

# Keep track of old to new filenames mapping
image_mapping = {}

def process_images():
    print("Processing images in assets/...")
    for filename in os.listdir(ASSETS_DIR):
        if filename.endswith('.svg') or filename.endswith('.webp'):
            continue
            
        filepath = os.path.join(ASSETS_DIR, filename)
        
        # We only want to convert jpg, jpeg, png
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                with Image.open(filepath) as img:
                    # Convert RGBA to RGB for JPEG/WEBP if needed, though WebP supports alpha.
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB") if not filename.lower().endswith('.png') else img
                        
                    # Resize if too large
                    if img.width > MAX_WIDTH:
                        ratio = MAX_WIDTH / float(img.width)
                        new_height = int((float(img.height) * float(ratio)))
                        img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
                        
                    # Save as WebP
                    basename = os.path.splitext(filename)[0]
                    new_filename = f"{basename}.webp"
                    new_filepath = os.path.join(ASSETS_DIR, new_filename)
                    
                    img.save(new_filepath, 'WEBP', quality=85)
                    print(f"Converted {filename} -> {new_filename}")
                    
                    # Store mapping for HTML replacement
                    image_mapping[filename] = new_filename
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def update_references():
    print("Updating HTML and CSS references...")
    files_to_update = HTML_FILES + CSS_FILES
    
    for filename in files_to_update:
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Replace occurrences
        for old_img, new_img in image_mapping.items():
            # In HTML: src="assets/old_img" -> src="assets/new_img"
            # In CSS: url('assets/old_img') -> url('assets/new_img')
            content = content.replace(f"assets/{old_img}", f"assets/{new_img}")
            
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated references in {filename}")

if __name__ == '__main__':
    process_images()
    update_references()
    print("Done!")
