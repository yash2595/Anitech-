import os

replacements = {
    # Gallery & Life at Josh
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22054341/house-party.jpg": "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09101513/45471172_1885762358206412_374259236810522624_o.jpg": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22053700/party.jpg": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09102743/Discussion.jpg": "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22052052/team.jpg": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22053215/rishu.jpg": "https://images.unsplash.com/photo-1556761175-5973dc0f32b7?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22053642/harshil.jpg": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22054046/meet.jpg": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&q=80",
    
    # What We Do
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/01/22124839/mobile-apps.jpg": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/02/22124425/devops.jpg": "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/02/22124736/AI.jpg": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/02/22124509/web-frameworks.jpg": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/02/22124801/saas1.jpg": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/02/22124556/big-data1.jpg": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/01/22125003/quality.jpg": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80",
}

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

# Generic fallback for unmapped broken images
fallback_img = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80"
# Load all 15 broken urls
broken_urls = set(open(r'c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\all_broken_urls.txt', 'r', encoding='utf-8').read().splitlines())
broken_urls = {u.strip() for u in broken_urls if u.strip()}

for root, _, files in os.walk(d):
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            new_content = content
            for url in broken_urls:
                if url in new_content:
                    replacement = replacements.get(url, fallback_img)
                    new_content = new_content.replace(url, replacement)
                    
            # ALSO fix the double ../ bug that happened earlier
            new_content = new_content.replace("../https://images.unsplash.com", "https://images.unsplash.com")
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Replaced broken images with Unsplash in {path}")
