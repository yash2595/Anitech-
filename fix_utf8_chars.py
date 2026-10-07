import os
import re

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
                
            # Let's fix the corrupted characters
            new_content = content.replace("Wed", "We'd").replace("Weâ€™d", "We'd").replace("Lets", "Let's").replace("Letâ€™s", "Let's")
            if "We" in content and "d" in content:
                # regex replace We...d where ... is the replacement char
                new_content = re.sub(r'We[^\x00-\x7F]d', "We'd", new_content)
                new_content = re.sub(r'Let[^\x00-\x7F]s', "Let's", new_content)
                
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Fixed utf-8 corruption in {path}")
