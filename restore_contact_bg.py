import re

css_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\wp-content\cache\autoptimize\css\autoptimize_65cbc919937503353ec6db2012d7f050_v2.css'

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

old_rule = "height:100vh;background-image:none;background-size:100% auto"
new_rule = "height:100vh;background-image:url(//www.joshtechnologygroup.com/wp-content/themes/jtg-marcom/./assets/images/contact-form-bg.png);background-size:100% auto"

if old_rule in css:
    css = css.replace(old_rule, new_rule)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Fixed CSS successfully!")
else:
    print("Could not find the target string in CSS!")
