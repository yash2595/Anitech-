import re
content = open(r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\who-we-are\index.html', encoding='utf-8').read()
m = re.search(r'<ul class="slides gallery-main">.*?</ul>', content, flags=re.DOTALL)
if m:
    slides = re.findall(r'<li class="slide[^>]*>.*?</li>', m.group(0), flags=re.DOTALL)
    for i, slide in enumerate(slides):
        print(f"Slide {i+1}:")
        bg_match = re.search(r'background-image:\s*url\([^)]+\)', slide)
        img_match = re.search(r'<img[^>]*src="([^"]+)"', slide)
        print("  BG:", bg_match.group(0) if bg_match else "None")
        print("  IMG:", img_match.group(1) if img_match else "None")
else:
    print("Gallery not found")
