import os

base_dir = r"MyWebSites\josh\www.joshtechnologygroup.com"

replacements_keys = [
    "https://s3.amazonaws.com/jtg-marcomm/wp-content/",
    "http://s3.amazonaws.com/jtg-marcomm/wp-content/",
    "https://s3.amazonaws.com/Anitech-marcomm/wp-content/",
    "http://s3.amazonaws.com/Anitech-marcomm/wp-content/",
    "https://www.joshtechnologygroup.com/wp-content/",
    "http://www.joshtechnologygroup.com/wp-content/"
]

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # calculate depth relative to base_dir
            rel_dir = os.path.relpath(root, base_dir)
            if rel_dir == '.':
                prefix = ""
            else:
                depth = len(rel_dir.split(os.sep))
                prefix = "../" * depth
            
            new_val = prefix + "wp-content/"
            
            original_content = content
            for old in replacements_keys:
                content = content.replace(old, new_val)
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {path} with prefix '{prefix}'")
