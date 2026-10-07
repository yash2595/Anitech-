import re
path = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\contact-us\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
for match in re.findall(r'href="([^"]+)"', content):
    print(match)
