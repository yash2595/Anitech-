import os
import urllib.request
import re

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

# 1. Fix HTML Encoding & paths
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            original = content
            content = content.replace("â€™", "’")
            content = content.replace("â€œ", "“")
            content = content.replace("â€\x9d", "”")
            content = content.replace("â€ ", "”")
            content = content.replace("â€”", "—")
            content = content.replace("â€“", "–")
            content = content.replace("â€˜", "‘")
            content = content.replace("https://wp-content/uploads/", "https://s3.amazonaws.com/jtg-marcomm/wp-content/uploads/")
            content = content.replace("\"wp-content/uploads/", "\"https://s3.amazonaws.com/jtg-marcomm/wp-content/uploads/")
            if content != original:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Fixed {path}")

# 2. Download missing SVGs
svgs = ["flexi-hours.svg", "idea.svg", "prank.svg"]
for svg in svgs:
    url = f"https://www.joshtechnologygroup.com/wp-content/themes/jtg-marcom/assets/images/{svg}"
    dest = os.path.join(d, r"wp-content\themes\jtg-marcom\assets\images", svg)
    if not os.path.exists(dest):
        try:
            urllib.request.urlretrieve(url, dest)
            print(f"Downloaded {svg}")
        except Exception as e:
            print(e)

# 3. Fix CSS map-gurugram
css_dir = os.path.join(d, r"wp-content\cache\autoptimize\css")
if os.path.exists(css_dir):
    for f in os.listdir(css_dir):
        if f.endswith(".css"):
            path = os.path.join(css_dir, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            original = content
            content = re.sub(r"url\([^)]*map-gurugram\.png\)", "none", content)
            if ".main-footer__social-list-item img{width:28px!important" not in content:
                content += "\n.main-footer__social-list-item img{width:28px!important;height:28px!important;object-fit:contain}\n"
            if content != original:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Fixed {path}")
print("Done")
