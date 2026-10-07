import os
import re

base_dir = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com'

def unhide_login(html):
    # Find the login li item and add display: block !important
    html = re.sub(
        r'<li class="menu-item menu-item-type-post_type menu-item-object-page">\s*<a href="([^"]*login.html[^"]*)">Login</a>\s*</li>',
        r'<li class="menu-item menu-item-type-post_type menu-item-object-page" style="display: block !important; height: auto !important; opacity: 1 !important; transform: none !important;"><a href="\1">Login</a></li>',
        html
    )
    return html

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = unhide_login(content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Updated {path}')
