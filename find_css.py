css_path = r"c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\wp-content\cache\autoptimize\css\autoptimize_65cbc919937503353ec6db2012d7f050_v2.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

idx = 0
while True:
    idx = css.find(".solutions__text_header", idx)
    if idx == -1:
        break
    start = max(0, idx - 50)
    end = min(len(css), idx + 200)
    print("---")
    print(css[start:end])
    idx += 1
