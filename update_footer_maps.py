import os

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

old_map_url = "https://www.google.com/maps/place/Anitech/@28.503129,77.0853488,19z/data=!4m5!3m4!1s0x390d19440d251b57:0x5d93a3ac9d62d3ae!8m2!3d28.503129!4d77.085896"
new_map_url = "https://www.google.com/maps/search/C56A%2F25,+C+Block,+Phase+2,+Industrial+Area,+Sector+62,+Noida,+Uttar+Pradesh+201309/"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            content = content.replace(old_map_url, new_map_url)
            
            if content != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated footer map URL in {path}")
