import os
import re

html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'
base_dir = os.path.dirname(html_path)

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# find all src="something"
srcs = re.findall(r'src=\"([^\"]+)\"', html)

missing = []
for src in srcs:
    if src.startswith('http') or src.startswith('//'):
        continue
    
    # Check if local file exists
    local_path = os.path.join(base_dir, src.split('?')[0].lstrip('/'))
    if not os.path.exists(local_path):
        missing.append(src)

print(f"Total missing: {len(missing)}")
for m in missing[:20]:
    print(m)
