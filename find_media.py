import re

css_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\wp-content\cache\autoptimize\css\autoptimize_65cbc919937503353ec6db2012d7f050_v2.css'
with open(css_path, "r", encoding="utf-8", errors="ignore") as f:
    css = f.read()

idx = css.find('.solutions__text_header,.industries__text_header{display:none}')
if idx != -1:
    before = css[:idx]
    # Find last @media
    media_idx = before.rfind('@media')
    if media_idx != -1:
        print(before[media_idx:media_idx+100])
    else:
        print("No @media found before!")
else:
    print("Not found!")
