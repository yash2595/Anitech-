import os
import re
import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

base_dir = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
html_path = os.path.join(base_dir, "index.html")

with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Find all img src
img_srcs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', content)
# Find all background-images in inline styles
bg_imgs = re.findall(r'background-image:\s*url\([\'"]?(.*?)[\'"]?\)', content)
# Find all background images in autoptimize css
css_dir = os.path.join(base_dir, "wp-content", "cache", "autoptimize", "css")
css_imgs = []
if os.path.exists(css_dir):
    for f in os.listdir(css_dir):
        if f.endswith(".css"):
            css_path = os.path.join(css_dir, f)
            with open(css_path, "r", encoding="utf-8", errors="ignore") as f2:
                css_content = f2.read()
                css_imgs.extend(re.findall(r'url\([\'"]?(.*?)[\'"]?\)', css_content))

all_images = set(img_srcs + bg_imgs + css_imgs)

print(f"Found {len(all_images)} unique images/urls to check.")

broken = []

for img in all_images:
    if img.startswith("data:"):
        continue
    
    # Resolve relative paths
    url_to_check = img
    
    if img.startswith("http"):
        # External URL
        try:
            req = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, context=context, timeout=5)
            if res.status != 200:
                broken.append((img, f"HTTP {res.status}"))
        except Exception as e:
            broken.append((img, str(e)))
    else:
        # Local file
        # Convert absolute local path if starts with /
        if img.startswith("/"):
            local_path = os.path.join(base_dir, img.lstrip("/"))
        else:
            # Relative to index.html which is at base_dir
            # For CSS images, they are relative to the CSS file location!
            if img in css_imgs:
                local_path = os.path.normpath(os.path.join(css_dir, img))
            else:
                local_path = os.path.normpath(os.path.join(base_dir, img))
            
        if not os.path.exists(local_path):
            broken.append((img, "File not found locally"))

if broken:
    print("\n--- BROKEN IMAGES ---")
    for b in broken:
        print(f"BROKEN: {b[0]} - {b[1]}")
else:
    print("All images are working!")
