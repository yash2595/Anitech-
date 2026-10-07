import os

html_path = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Restore not-mobile to the solutions__text_header
html = html.replace('class="solutions__text_header"', 'class="solutions__text_header not-mobile"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Restored not-mobile class to Our Digital Solutions text")
