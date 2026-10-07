import re
content = open(r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html', encoding='utf-8').read()
print(re.findall(r'href="([^"]*resources[^"]*)"', content))
