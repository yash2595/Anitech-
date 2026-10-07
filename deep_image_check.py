import os
import re
import urllib.request
from urllib.error import URLError, HTTPError
import time

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
broken_images = set()
checked_urls = set()

print("Starting deep image check...")
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Find all image src and CSS url() inside HTML
            img_srcs = re.findall(r'<img[^>]+src=["\'](http[^"\']+)["\']', content)
            bg_urls = re.findall(r'url\([\'"]?(http[^\'"]+)[\'"]?\)', content)
            
            urls = set(img_srcs + bg_urls)
            for url in urls:
                if url in checked_urls:
                    continue
                checked_urls.add(url)
                
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    resp = urllib.request.urlopen(req, timeout=5)
                    # if it succeeds, it's fine
                except HTTPError as e:
                    print(f"BROKEN ({e.code}): {url} in {os.path.relpath(path, d)}")
                    broken_images.add(url)
                except URLError as e:
                    print(f"BROKEN (URL Error): {url} in {os.path.relpath(path, d)}")
                    broken_images.add(url)
                except Exception as e:
                    print(f"BROKEN ({e}): {url} in {os.path.relpath(path, d)}")
                    broken_images.add(url)

print(f"Done! Found {len(broken_images)} broken images.")
