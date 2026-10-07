import sys

old = open('original_contact.html', 'r', encoding='utf-16le', errors='ignore').read()
new = open(r'MyWebSites\josh\www.joshtechnologygroup.com\contact-us\index.html', 'r', encoding='utf-8', errors='ignore').read()

# Just print the exact lines where `<div class="contact-hero__detail-section">` appears
import re

old_section = re.search(r'<div class="contact-hero__detail-section">.*?</section>', old, re.DOTALL)
new_section = re.search(r'<div class="contact-hero__detail-section">.*?</section>', new, re.DOTALL)

if old_section:
    print("OLD SECTION:")
    print(old_section.group(0)[:500].encode('ascii', 'ignore').decode('ascii'))
if new_section:
    print("NEW SECTION:")
    print(new_section.group(0)[:500].encode('ascii', 'ignore').decode('ascii'))
