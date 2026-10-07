import os

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

old_address = "#861, Phase 5, Udyog Vihar, Gurugram, Haryana. National Capital Region. INDIA. 122016"
new_address = "C56A/25, C Block, Phase 2, Industrial Area, Sector 62, Noida, Uttar Pradesh 201309"

old_iframe = 'src="https://snazzymaps.com/embed/131366"'
new_iframe = 'src="https://maps.google.com/maps?q=C56A%2F25%2C%20C%20Block%2C%20Phase%202%2C%20Industrial%20Area%2C%20Sector%2062%2C%20Noida%2C%20Uttar%20Pradesh%20201309&t=&z=13&ie=UTF8&iwloc=&output=embed"'

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Replace address text
            content = content.replace(old_address, new_address)
            
            # Replace snazzymaps iframe
            content = content.replace(old_iframe, new_iframe)
            
            if content != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {path}")
