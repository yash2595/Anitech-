import re
html = open(r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\index.html', encoding='utf-8').read()
match = re.search(r'(.{0,300}responsive-menu-item-387.{0,300})', html, re.DOTALL)
if match:
    print(match.group(0).replace('><', '>\n<'))
else:
    print('not found')
