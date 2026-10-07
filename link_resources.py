import os
import re

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

# The links we want to fix
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Determine relative prefix
            rel_path = os.path.relpath(path, d)
            depth = rel_path.count(os.sep)
            
            # For root, depth is 0. For what-we-do/index.html, depth is 1.
            prefix = "../" * depth
            resource_link = f"{prefix}resources/index.html"
            privacy_link = f"{prefix}index.html"
            
            # Replace Resource Centre links
            # They might currently be href="#" or href="https://resources"
            content = re.sub(
                r'<a href="[^"]*" class="main-footer__links-item main-footer__links-item--heading">Resource Centre</a>',
                f'<a href="{resource_link}" class="main-footer__links-item main-footer__links-item--heading">Resource Centre</a>',
                content
            )
            
            content = re.sub(
                r'<a href="[^"]*" class="main-footer__links-item">Blogs</a>',
                f'<a href="{resource_link}" class="main-footer__links-item">Blogs</a>',
                content
            )
            
            content = re.sub(
                r'<a href="[^"]*" class="main-footer__links-item">Culture</a>',
                f'<a href="{resource_link}" class="main-footer__links-item">Culture</a>',
                content
            )
            
            # Privacy policy and terms of use
            content = re.sub(
                r'<a href="[^"]*">Privacy Policy</a>',
                f'<a href="{privacy_link}">Privacy Policy</a>',
                content
            )
            content = re.sub(
                r'<a href="[^"]*">Terms of Use</a>',
                f'<a href="{privacy_link}">Terms of Use</a>',
                content
            )
            
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Updated footer links in {rel_path}")

print("Done!")
