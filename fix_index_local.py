import os
import re

html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'

with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Replace all S3 links with local relative links
new_content = re.sub(r'https?://s3\.amazonaws\.com/jtg-marcomm/(wp-content/uploads/[^"\']+)', r'\1', content)

if new_content != content:
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replaced S3 links with local links successfully!")
else:
    print("No changes made.")
