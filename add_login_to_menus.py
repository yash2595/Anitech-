import os
import re

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

missing = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            m = re.search(r'<ul id=[\'"]menu-primary-menu-2[\'"][^>]*>.*?</ul>', content, re.I|re.S)
            if m and 'Login' not in m.group(0):
                missing.append(path)

for path in missing:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add login to menu-primary-menu-2
    content = re.sub(
        r'(<ul id=[\'"]menu-primary-menu-2[\'"][^>]*>.*?)(</ul>)',
        r'\1<li class="menu-item menu-item-type-post_type_archive"><a href="../login.html">Login</a></li>\2',
        content,
        flags=re.I|re.S
    )
    
    # Also ensure responsive menu has it
    m2 = re.search(r'<ul id=[\'"]menu-main-1[\'"][^>]*>.*?</ul>', content, re.I|re.S)
    if m2 and 'Login' not in m2.group(0):
        content = re.sub(
            r'(<ul id=[\'"]menu-main-1[\'"][^>]*>.*?)(</ul>)',
            r'\1<li class="menu-item menu-item-type-post_type_archive"><a href="../login.html">Login</a></li>\2',
            content,
            flags=re.I|re.S
        )
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added Login to {path}")
