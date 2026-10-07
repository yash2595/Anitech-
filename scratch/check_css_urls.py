import re
css_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\wp-content\cache\autoptimize\css\autoptimize_65cbc919937503353ec6db2012d7f050_v2.css'
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

urls = re.findall(r'url\([\'\"]?([^\)\'\"]+)[\'\"]?\)', css)
for u in set(urls):
    if 'data:image' not in u and 'fonts' not in u:
        print(u)
