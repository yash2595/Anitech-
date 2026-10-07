import re

with open(r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\index.html", encoding="utf-8") as f:
    html = f.read()

m = re.search(r"<section class=\"solutions.*?(</p>|<div class=\"solutions__slide\">)", html, re.DOTALL)
if m:
    print(m.group(0))
