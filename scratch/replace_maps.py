import os
import re

new_link = "https://www.google.co.in/maps/place/Essential+Oil+Association+of+India/@28.6147101,77.3633376,17z/data=!4m6!3m5!1s0x390ce5681f7c1f49:0x3a57de9bc495c391!8m2!3d28.6147054!4d77.3659125!16s%2Fg%2F11b_255j2v?entry=ttu&g_ep=EgoyMDI2MTAwNC4wIKXMDSoASAFQAw%3D%3D"
new_embed = "https://maps.google.com/maps?q=Essential+Oil+Association+of+India,+Noida&t=&z=15&ie=UTF8&iwloc=&output=embed"

base_dir = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com'

for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                html = file.read()
            
            original_html = html
            
            # Replace links
            html = re.sub(r'https://www\.google\.com/maps/search/[^\'\"<]+', new_link, html)
            
            # Replace iframe src
            html = re.sub(r'https://maps\.google\.com/maps\?q=[^\'\"&]+&t=&z=13&ie=UTF8&iwloc=&output=embed', new_embed, html)
            
            if html != original_html:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(html)
                print(f"Updated {path}")
