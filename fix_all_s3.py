import os
import re

base_dir = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com'

unsplash_images = [
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&q=80",
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80",
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&q=80",
    "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&q=80"
]

total_local_replacements = 0
total_unsplash_replacements = 0

for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            matches = list(set(re.findall(r'(https?://s3\.amazonaws\.com/jtg-marcomm/(wp-content/uploads/[^"\']+))', content)))
            if not matches:
                continue
            
            rel_level = os.path.relpath(root, base_dir)
            if rel_level == ".":
                prefix = ""
            else:
                prefix = "../" * len(rel_level.split(os.sep))
            
            new_content = content
            for i, (match_full, local_path) in enumerate(matches):
                full_local_path = os.path.join(base_dir, local_path)
                if os.path.exists(full_local_path):
                    # Replace with relative path
                    new_content = new_content.replace(match_full, prefix + local_path)
                    total_local_replacements += 1
                else:
                    # Replace with Unsplash
                    new_img = unsplash_images[i % len(unsplash_images)]
                    new_content = new_content.replace(match_full, new_img)
                    total_unsplash_replacements += 1
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)

print(f"Replaced {total_local_replacements} images with local paths.")
print(f"Replaced {total_unsplash_replacements} images with Unsplash placeholders.")
