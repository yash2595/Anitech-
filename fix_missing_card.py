import os
import re

file_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\what-we-do\index.html'

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = r'<div class="image-grid__item-content">\s*Software Engineering\s*</div>\s*</div>'

def replacer(m):
    return m.group(0) + """<div class="image-grid__item"> <img class="image-grid__image" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80" alt="Financial Technology"><div class="image-grid__item-content"> Financial Technology</div></div>"""

new_content = re.sub(target, replacer, content)

if new_content != content:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed missing card!")
else:
    print("Target not found.")
