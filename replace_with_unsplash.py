import os

replacements = {
    # Hero images
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/01/20055231/mobile-app.jpg": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09115446/Automotive-e1566306829467.jpg": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/20064712/perry-grone-lbLgFFlADrY-unsplash.jpg": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/20064625/markus-spiske-Skf7HxARcoc-unsplash.jpg": "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=1600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/23154600/randy-fath-GDLdU80UDko-unsplash.jpg": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=1600&q=80",
    
    # Timeline & Founders
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09101405/leaders.jpg": "https://images.unsplash.com/photo-1556761175-5973dc0f32b7?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/20061653/white-flower.jpg": "https://images.unsplash.com/photo-1497215898147-5ddf364fd01c?w=600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/20061806/next-step.jpg": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/20061901/expansion.jpg": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/20062224/product-launch.jpg": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22050604/shanky.jpg": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400&q=80",

    # What We Do
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/21121011/charles-Lks7vei-eAg-unsplash.jpg": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09095757/testing-1.jpg": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/22093801/software-engineer.jpg": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09080931/standup.jpg": "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09095231/calyxpod-1.jpg": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/08/09082909/ireflect-bg.jpg": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80",

    # Careers
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/07/15125851/B-Celebration.jpg": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1600&q=80",
    "https://www.joshtechnologygroup.com/wp-content/uploads/2019/07/15125755/61__1561961634_103.206.163.146.jpg": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=1600&q=80",
}

d = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"

# Generic fallback for unmapped broken images
fallback_img = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80"
# Load all broken urls
broken_urls = set(open(r'c:\Users\hp\Downloads\broken_urls.txt', 'r', encoding='utf-8').read().splitlines())
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
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Replaced broken images with Unsplash in {path}")
