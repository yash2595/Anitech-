import os

base_dir = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com"

replacements = {
    "autoptimize_65cbc919937503353ec6db2012d7f050.css": "autoptimize_65cbc919937503353ec6db2012d7f050_v2.css",
    "autoptimize_9e3506d709f92300da4df7dd2b1b0e07.css": "autoptimize_9e3506d709f92300da4df7dd2b1b0e07_v2.css",
    "autoptimize_bdfdc65c4a3d614fd24e8b557ea94b79.css": "autoptimize_bdfdc65c4a3d614fd24e8b557ea94b79_v2.css",
    "autoptimize_143cfde1cb300b3b4c71b581a4cd4a33.js": "autoptimize_143cfde1cb300b3b4c71b581a4cd4a33_v2.js",
    "autoptimize_b0b477517470edadf130b4af03a6a245.js": "autoptimize_b0b477517470edadf130b4af03a6a245_v2.js",
    "autoptimize_08ac5fd6ab0212a0a70592e5b4b4b651.js": "autoptimize_08ac5fd6ab0212a0a70592e5b4b4b651_v2.js",
    "autoptimize_8b680355b71296aa970a6d60b2d3cbf9.js": "autoptimize_8b680355b71296aa970a6d60b2d3cbf9_v2.js"
}

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for old, new in replacements.items():
                content = content.replace(old, new)
                
            if content != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed {path}")
