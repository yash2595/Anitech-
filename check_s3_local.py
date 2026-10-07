import os
import re

html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'

with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

matches = list(set(re.findall(r'(https://s3\.amazonaws\.com/jtg-marcomm/wp-content/uploads/[^"\']+)', content)))
missing = []

for match in matches:
    local_path = match.replace("https://s3.amazonaws.com/jtg-marcomm/", "")
    full_local_path = os.path.join(r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com", local_path)
    if not os.path.exists(full_local_path):
        missing.append(match)

print(f"Total S3 links found: {len(matches)}")
print(f"Missing locally: {len(missing)}")
if missing:
    for m in missing[:5]:
        print(f"Missing: {m}")
