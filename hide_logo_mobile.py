import os

html_path = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add a CSS rule to hide .logo--full on mobile screens (max-width 767px)
if 'hide-logo-mobile' not in html:
    html = html.replace('</head>', '<style id="hide-logo-mobile">@media (max-width: 767px) { .logo--full { display: none !important; } }</style></head>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Added CSS to hide .logo--full on mobile")
