import re

path = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\who-we-are\index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

imgs = re.findall(r'<img.*?src="(.*?)".*?>', html)
for i in range(min(5, len(imgs))):
    print(imgs[i])
