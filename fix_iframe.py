import os
import re

path = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\contact-us\index.html"
with open(path, "r", encoding="utf-8") as file:
    content = file.read()

content = re.sub(r'<iframe class="js-map-iframe".*?</iframe>', '', content)

with open(path, "w", encoding="utf-8") as file:
    file.write(content)
print("Removed iframe")
