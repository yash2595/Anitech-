import os
import re
import urllib.request

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            urls = set(re.findall(r'src="(https://www\.joshtechnologygroup\.com/wp-content/uploads/[^"]+)"', content))
            urls.update(re.findall(r'url\(\'(https://www\.joshtechnologygroup\.com/wp-content/uploads/[^\']+)\'\)', content))
            for url in urls:
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    resp = urllib.request.urlopen(req)
                    if not resp.headers.get('Content-Type', '').startswith('image/'):
                        print(f"BROKEN (Soft 404): {url} in {path}")
                except Exception as e:
                    print(f"BROKEN ({e}): {url} in {path}")
