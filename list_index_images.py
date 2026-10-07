import re

html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'

with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print("IMAGES FOUND IN HTML:")
for img in images:
    print(img)
