import os
import re
import urllib.request
import concurrent.futures

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

def check_url(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=5)
        if not resp.headers.get('Content-Type', '').startswith('image/'):
            return url
    except Exception:
        return url
    return None

all_urls = set()
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            urls = set(re.findall(r'src="(https://www\.joshtechnologygroup\.com/wp-content/uploads/[^"]+)"', content))
            urls.update(re.findall(r'url\(\'?\"?(https://www\.joshtechnologygroup\.com/wp-content/uploads/[^\'\")]+)\'?\"?\)', content))
            all_urls.update(urls)

print(f"Found {len(all_urls)} unique urls to check...")
broken = []
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(check_url, all_urls)
    for url in results:
        if url:
            broken.append(url)

print(f"Found {len(broken)} broken urls.")
with open(r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\all_broken_urls.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(broken))
