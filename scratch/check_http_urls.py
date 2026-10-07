import re
html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

urls = re.findall(r'http://[^\s\"\']+', html)
for u in set(urls):
    print(u)
