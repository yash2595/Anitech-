import re
with open(r'MyWebSites\josh\www.joshtechnologygroup.com\what-we-do\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

links = re.findall(r'href\s*=\s*["\']([^"\']+\.css.*?|[^"\']+\.css)["\']', text, re.IGNORECASE)
for link in links:
    print(link)
