import os
import re

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

def fix_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix JS files
    html = re.sub(r'(wp-content/cache/autoptimize/js/autoptimize_[a-f0-9]+)\.js', r'\1_v2.js', html)

    # 2. Fix Logos
    # Use relative prefix based on depth
    is_subpage = ('what-we-do' in filepath or 'who-we-are' in filepath or 'careers' in filepath or 'about' in filepath or 'contact' in filepath or 'resources' in filepath)
    prefix = "../" if is_subpage else ""
    anitech_logo = prefix + "wp-content/themes/jtg-marcom/assets/images/anitech-logo.jpg"
    
    html = re.sub(r'https://www\.joshtechnologygroup\.com/wp-content/themes/jtg-marcom/assets/images/logo-full\.svg', anitech_logo, html)
    html = re.sub(r'wp-content/themes/jtg-marcom/assets/images/logo-full\.svg', anitech_logo, html)
    html = re.sub(r'\.\./wp-content/themes/jtg-marcom/assets/images/logo-full\.svg', anitech_logo, html)
    
    html = re.sub(r'https://s3\.amazonaws\.com/jtg-marcomm/wp-content/uploads/2019/08/09103847/cropped-jtg-logo-[^\s\'\"]+', anitech_logo, html)

    # Replace alt text to say Anitech
    html = html.replace('alt="Josh Technology Group"', 'alt="Anitech"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            fix_page(os.path.join(root, f))
            
print("Done fixing JS and Logos!")
