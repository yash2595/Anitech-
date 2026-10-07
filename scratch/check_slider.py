html_path = r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start = html.find('<div class="solutions__slider')
end = html.find('<section class="landing-page__section flex-col gallery-section"')

if start != -1 and end != -1:
    print(html[start:end])
else:
    print("Could not find bounds")
