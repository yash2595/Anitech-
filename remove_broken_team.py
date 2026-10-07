import urllib.request
import urllib.error
import re

path = r"c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com\who-we-are\index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Find all team cards
cards = re.findall(r'(<a\s+class="team__card">.*?</a>)', html, flags=re.DOTALL)
print(f"Found {len(cards)} team cards.")

removed = 0
for card in cards:
    # Find the primary image src
    match = re.search(r'src="(https://www\.joshtechnologygroup\.com/wp-content/uploads/[^"]+)"', card)
    if match:
        url = match.group(1)
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            resp = urllib.request.urlopen(req)
            content_type = resp.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                html = html.replace(card, '')
                removed += 1
                print(f"Removed soft 404 card: {url}")
        except Exception as e:
            html = html.replace(card, '')
            removed += 1
            print(f"Removed broken card: {url} ({e})")

if removed > 0:
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Removed {removed} broken team cards and saved.")
else:
    print("No broken cards found.")
