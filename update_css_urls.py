import glob
import re

css_files = glob.glob(r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\wp-content\cache\autoptimize\css\*.css')
for f in css_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Replace //www.anitech.com/wp-content/ with ../../../
    new_content = re.sub(r'//www\.anitech\.com/wp-content/', r'../../../', content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
