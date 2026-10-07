import os

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

# Revert S3 urls back to joshtechnologygroup
for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            original = content
            content = content.replace("https://s3.amazonaws.com/jtg-marcomm/wp-content/uploads/", "https://www.joshtechnologygroup.com/wp-content/uploads/")
            
            if content != original:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Fixed S3 URLs in {path}")
print("Done")
