import os
import re

html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'
base_dir = os.path.dirname(html_path)

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

srcs = re.findall(r'src=\"([^\"]+)\"', html)

def check_case_sensitive(path):
    parts = os.path.normpath(path).split(os.sep)
    current = parts[0] + os.sep
    for part in parts[1:]:
        if part == '': continue
        try:
            # os.listdir is case-sensitive in the list it returns
            dir_contents = os.listdir(current)
            if part not in dir_contents:
                return False
            current = os.path.join(current, part)
        except Exception:
            return False
    return True

missing = []
for src in srcs:
    if src.startswith('http') or src.startswith('//'):
        continue
    
    local_path = os.path.join(base_dir, src.split('?')[0].lstrip('/'))
    if not os.path.exists(local_path):
        missing.append((src, "Not found at all"))
    elif not check_case_sensitive(local_path):
        missing.append((src, "Case mismatch"))

print(f"Total missing or case mismatch: {len(missing)}")
for m in missing[:20]:
    print(m)
