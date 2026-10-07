import os
import re

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

url_prefixes = [
    "https://www.joshtechnologygroup.com/",
    "http://www.joshtechnologygroup.com/",
    "https://joshtechnologygroup.com/",
    "http://joshtechnologygroup.com/",
    "//www.joshtechnologygroup.com/",
    "//joshtechnologygroup.com/"
]

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # calculate depth relative to base_dir
            rel_dir = os.path.relpath(root, base_dir)
            if rel_dir == '.':
                prefix = "./"
            else:
                depth = len(rel_dir.split(os.sep))
                prefix = "../" * depth
            
            # Replace absolute URLs to the site with relative prefix
            for url in url_prefixes:
                content = content.replace(url, prefix)
            
            # Replace email
            content = content.replace("connect@joshtechnologygroup.com", "connect@anitech.com")
            
            # Replace any other leftover joshtechnologygroup.com (like in text)
            content = content.replace("joshtechnologygroup.com", "anitech.com")
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {path}")
