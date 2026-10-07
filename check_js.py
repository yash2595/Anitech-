import os
import re
import urllib.parse

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"
html = open(os.path.join(base_dir, 'index.html'), encoding='utf-8').read()
scripts = set(re.findall(r'<script[^>]*src=[\'\"]([^\'\"]+)[\'\"]', html))

missing = []
for s in scripts:
    if not s.startswith('http') and not s.startswith('//'):
        if not os.path.exists(os.path.join(base_dir, urllib.parse.unquote(s))):
            missing.append(s)

print("Missing JS in index.html:", missing)
