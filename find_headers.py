import re

with open(r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\index.html", encoding="utf-8") as f:
    html = f.read()

matches = re.findall(r'<p class="solutions__text_header.*?</p>', html)
for m in matches:
    print(m)
