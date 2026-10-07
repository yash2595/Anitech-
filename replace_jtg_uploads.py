import os
import re

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

replacements = {
    # Replace JTG logo with our Anitech logo (if any)
    # But wait, we want to replace uploads with unsplash
    # Let's just regex replace all of them with different Unsplash images
}

unsplash_images = [
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80",
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80",
    "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80",
    "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&q=80",
    "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=80"
]

img_idx = 0

for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html") or f.endswith(".css"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Find all joshtechnologygroup.com/wp-content/uploads/ images
            matches = set(re.findall(r'(https://www\.joshtechnologygroup\.com/wp-content/uploads/[a-zA-Z0-9_/\.\-]+)', content))
            if matches:
                for match in matches:
                    new_img = unsplash_images[img_idx % len(unsplash_images)]
                    content = content.replace(match, new_img)
                    img_idx += 1
                
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Replaced {len(matches)} JTG uploads in {os.path.relpath(path, d)}")

# Also replace any remaining JTG text mentions just to be sure!
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            new_content = content.replace("JTG", "Anitech")
            new_content = new_content.replace("Josh Technology Group", "Anitech Consulting Services")
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Replaced JTG text in {os.path.relpath(path, d)}")

print("Done replacing JTG uploads and text!")
