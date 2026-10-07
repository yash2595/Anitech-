import os
import re

broken_urls = set(open(r'c:\Users\hp\Downloads\broken_urls.txt', 'r', encoding='utf-8').read().splitlines())
broken_urls = {u.strip() for u in broken_urls if u.strip()}

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
transparent_img = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"

for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html") or f.endswith(".css"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            new_content = content
            for url in broken_urls:
                if url in new_content:
                    new_content = new_content.replace(url, transparent_img)
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Replaced broken images in {path}")
