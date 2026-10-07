import os
import re

base_dir = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com'

def replace_text(html):
    # Replace the text mentions
    html = re.sub(r'\bJosh Technology Group\b', 'Anitech', html, flags=re.IGNORECASE)
    html = re.sub(r'\bJTG\b', 'Anitech', html)
    
    # Also fix the logo size
    # Find something like: <img width="190" height="190" src="..." class="custom-logo"
    html = re.sub(r'width="190"\s+height="190"([^>]*)class="custom-logo"', r'width="100" height="100" style="max-height: 100px; width: auto; object-fit: contain;"\1class="custom-logo"', html)
    
    # We should also replace it if the order is different, e.g. class="custom-logo" ... width="190" height="190"
    
    return html

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = replace_text(content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Updated {path}')
