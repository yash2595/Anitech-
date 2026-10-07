import os
import re

base_dir = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com'

def update_links(filepath, root_dir):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    original = content
    
    rel_path = os.path.relpath(root_dir, filepath)
    depth = rel_path.count('..')
    prefix = '../' * depth if depth > 0 else './'
    
    if filepath == os.path.join(root_dir, 'index.html'):
        prefix = './'
    elif depth == 0:
        prefix = './'

    content = re.sub(r'href="[^"]*terms-of-use/?([^"]*)"', r'href="{prefix}terms.html\1"'.format(prefix=prefix), content)
    content = re.sub(r'href="[^"]*privacy-policy/?([^"]*)"', r'href="{prefix}privacy-policy.html\1"'.format(prefix=prefix), content)
    
    content = re.sub(r'href="https://anitechcs.com/terms-of-use/?"', r'href="https://anitechcs.com/terms.html"', content)
    content = re.sub(r'href="https://anitechcs.com/privacy-policy/?"', r'href="https://anitechcs.com/privacy-policy.html"', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            update_links(filepath, base_dir)

print("Done updating links")
