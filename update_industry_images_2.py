import os
import re

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

replacements = {
    "Healthcare": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80",
    "Transport + Travel": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=800&q=80",
    "Automotive": "https://images.unsplash.com/photo-1518779532559-67993afad5e2?w=800&q=80",
    "E-Commerce": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80",
    "Software Engineering": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80",
    "Video-Audio Solutions": "https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?w=800&q=80",
    "Digital Marketing &#038; Advertising": "https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?w=800&q=80",
    "Customer Relationship Management": "https://images.unsplash.com/photo-1556761175-5973dc0f32b7?w=800&q=80"
}

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            for industry, new_img in replacements.items():
                # Pattern for what-we-do/index.html layout
                pattern = r'(<img class="image-grid__image" src=")[^"]+(" alt="[^"]*"><div class="image-grid__item-content">\s*' + re.escape(industry) + r'\s*</div>)'
                content = re.sub(pattern, r'\1' + new_img + r'\2', content)
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated images in {path}")
