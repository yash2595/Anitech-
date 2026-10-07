import re
html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\contact-us\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("IFRAMES:")
for iframe in re.findall(r'<iframe[^>]+>', html, re.IGNORECASE):
    print(iframe)

print("\nLINKS:")
for link in re.findall(r'<a[^>]+href=[\'\"]([^\'\"]*)[\'\"][^>]*>', html, re.IGNORECASE):
    if 'map' in link.lower() or 'google' in link.lower():
        print(link)
