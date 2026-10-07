import os
import re

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
hrefs = set()

for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            matches = re.findall(r'href="([^"]*resources[^"]*)"', content)
            hrefs.update(matches)

print("Unique resource links found:")
for h in hrefs:
    print(h)
