import os
import re

base_dir = r'c:\Users\kushb\OneDrive\Desktop\anitech\MyWebSites\josh\www.joshtechnologygroup.com'

def add_login_links(html, filepath):
    # Determine the relative path to the root directory from this file's directory
    rel_path_to_root = os.path.relpath(base_dir, os.path.dirname(filepath)).replace('\\', '/')
    if rel_path_to_root == '.':
        login_href = 'login.html'
    else:
        login_href = f'{rel_path_to_root}/login.html'

    # Primary menu
    # <li ...><a href="...">Contact</a></li>
    # We will find the Contact link and append the Login link
    primary_contact_re = re.compile(r'(<a[^>]*href="[^"]*contact-us/index\.html"[^>]*>Contact</a></li>)')
    if primary_contact_re.search(html):
        html = primary_contact_re.sub(r'\1<li class="menu-item menu-item-type-post_type menu-item-object-page"><a href="' + login_href + '">Login</a></li>', html)

    # Secondary/Responsive menu
    # <a href="..." class="responsive-menu-item-link">Contact Us</a></li>
    resp_contact_re = re.compile(r'(<a[^>]*href="[^"]*contact-us/index\.html"[^>]*class="responsive-menu-item-link"[^>]*>Contact Us</a></li>)')
    if resp_contact_re.search(html):
        html = resp_contact_re.sub(r'\1<li class="menu-item menu-item-type-post_type menu-item-object-page responsive-menu-item"><a href="' + login_href + '" class="responsive-menu-item-link">Login</a></li>', html)
        
    # Also add to footer menu if there is one
    footer_contact_re = re.compile(r'(<a[^>]*href="[^"]*contact/"[^>]*>Contact</a>)')
    if footer_contact_re.search(html):
        html = footer_contact_re.sub(r'\1 | <a href="' + login_href + '">Login</a>', html)

    return html

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            new_content = add_login_links(content, path)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Updated {path}')
