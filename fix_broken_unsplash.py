import os

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

replacements = {
    "https://images.unsplash.com/photo-1556761175-5973dc0f32b7?w=800&q=80": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80",
    "https://images.unsplash.com/photo-1497215898147-5ddf364fd01c?w=600&q=80": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80",
    # Just in case, replace the Josh occurrences that I missed
    "Josh family": "Anitech family",
    "for Josh with": "for Anitech with"
}

for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)
                
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Updated {os.path.relpath(path, d)}")

print("Done fixing broken Unsplash links and missing Josh texts!")
