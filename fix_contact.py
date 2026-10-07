import os
import re

path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\contact-us\index.html'

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# I want to add a spacer div inside the map-section to hold the height and fix the layout!
old_str = '<div class="contact-hero__map-section" id="location"><p></p></div>'
new_str = '<div class="contact-hero__map-section" id="location"><p><div style="width:100%; height:100%; min-height: 50vh;"></div></p></div>'

if old_str in content:
    content = content.replace(old_str, new_str)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced successfully!")
else:
    print("Could not find the target string!")
