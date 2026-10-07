import re
html = open(r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\index.html', encoding='utf-8').read()
links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
for i, (href, text) in enumerate(links):
    text_clean = re.sub(r'<[^>]+>', '', text).strip()
    print(f"{i}: {href} - {text_clean}")
