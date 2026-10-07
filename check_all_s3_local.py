import os
import re

base_dir = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com'

total_found = 0
total_missing = 0

for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            matches = list(set(re.findall(r'(https?://s3\.amazonaws\.com/jtg-marcomm/(wp-content/uploads/[^"\']+))', content)))
            for match_full, local_path in matches:
                total_found += 1
                full_local_path = os.path.join(base_dir, local_path)
                if not os.path.exists(full_local_path):
                    total_missing += 1

print(f"Total S3 links found: {total_found}")
print(f"Missing locally: {total_missing}")
