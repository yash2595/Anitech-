import re
html = open(r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\index.html', encoding='utf-8').read()
match = re.search(r'<div id="responsive-menu-container".*?</nav>', html, re.DOTALL)
if match:
    # insert line breaks for readability
    print(match.group(0).replace('><', '>\n<'))
else:
    print('not found')
