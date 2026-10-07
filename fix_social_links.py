import os
import re

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            content = content.replace("https://www.facebook.com/LifeAtJosh/", "https://www.facebook.com/anitech/")
            content = content.replace("https://www.facebook.com/LifeAtJosh", "https://www.facebook.com/anitech")
            
            content = content.replace("https://www.linkedin.com/company/josh-technology-group/", "https://www.linkedin.com/company/anitech/")
            content = content.replace("https://www.linkedin.com/company/josh-technology-group", "https://www.linkedin.com/company/anitech")
            
            content = content.replace("Josh+Technology+Group", "Anitech")
            
            # Any other mentions of josh in hrefs?
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {path}")
