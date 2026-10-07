import os

css_path = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com\wp-content\cache\autoptimize\css\autoptimize_65cbc919937503353ec6db2012d7f050_v2.css'

with open(css_path, 'a', encoding='utf-8') as f:
    f.write('''
@media (max-width: 1024px) {
    .solutions__text_header.not-mobile,
    .solutions__text_header {
        display: block !important;
        position: static !important;
        transform: none !important;
        height: auto !important;
        margin: 0 auto !important;
        padding: 3rem 1rem !important;
        text-align: center !important;
        width: 100% !important;
        left: 0 !important;
        right: 0 !important;
        top: 0 !important;
    }
}
''')

print("Added mobile/tablet override to CSS")
