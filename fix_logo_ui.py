import os
import re

base_dir = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com'

def fix_logo_ui(html):
    # Match the custom-logo img tag and replace it with a responsive one
    pattern = r'<img[^>]*class="custom-logo"[^>]*>'
    
    def replacer(match):
        img_tag = match.group(0)
        # Extract the src
        src_match = re.search(r'src="([^"]+)"', img_tag)
        src = src_match.group(1) if src_match else ''
        
        # We will use a clean img tag without srcset and explicit width/height that cause distortion
        return f'<img src="{src}" class="custom-logo" alt="Anitech" style="max-height: 80px; width: auto; max-width: 100%; object-fit: contain; object-position: left center;" />'
        
    html = re.sub(pattern, replacer, html)
    return html

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = fix_logo_ui(content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Updated {path}')
