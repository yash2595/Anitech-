import os
import re

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

links = set()
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(r'href=[\'"]([^\'"]*joshtechnologygroup\.com[^\'"]*)[\'"]', content)
            for m in matches:
                links.add(m)

for link in sorted(links):
    print(link)
