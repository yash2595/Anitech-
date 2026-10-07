import os
import re

html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'

with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Replace s3.amazonaws.com links with Unsplash links
unsplash_images = [
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&q=80",
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80",
    "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&q=80",
    "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&q=80",
    "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&q=80",
    "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=800&q=80",
    "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800&q=80",
    "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=80",
    "https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?w=800&q=80",
    "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?w=800&q=80",
    "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&q=80",
    "https://images.unsplash.com/photo-1543269865-cbf427effbad?w=800&q=80",
    "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=800&q=80"
]

matches = list(set(re.findall(r'(https://s3\.amazonaws\.com/jtg-marcomm/[^"\']+)', content)))
for i, match in enumerate(matches):
    # If it's a small icon or something, we can replace it with a generic placeholder, 
    # but the Unsplash images will also work.
    new_img = unsplash_images[i % len(unsplash_images)]
    content = content.replace(match, new_img)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Replaced {len(matches)} AWS S3 images with Unsplash images in index.html!")
