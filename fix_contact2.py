import os

path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\contact-us\index.html'

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the broken `<p><div...` with just a clean div
content = content.replace('<div class="contact-hero__map-section" id="location"><p><div style="width:100%; height:100%; min-height: 50vh;"></div></p></div>', '<div class="contact-hero__map-section" id="location"><div style="width: 100%; height: 100vh;"></div></div>')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed HTML structure!")
