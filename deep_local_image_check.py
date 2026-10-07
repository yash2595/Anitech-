import os
import re

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
broken_images = set()

for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Find relative paths
            img_srcs = re.findall(r'<img[^>]+src=["\']([^"\'h]+)["\']', content)
            
            for src in img_srcs:
                if src.startswith("data:"): continue
                if src.startswith("//"): continue
                if src.startswith("#"): continue
                
                # Resolve relative path
                resolved = os.path.normpath(os.path.join(root, src))
                if not os.path.exists(resolved):
                    print(f"BROKEN LOCAL: {src} in {os.path.relpath(path, d)} -> {resolved}")
                    broken_images.add(resolved)

print(f"Done! Found {len(broken_images)} broken local images.")
