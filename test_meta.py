import urllib.request

with open('/Users/amitsunda/Desktop/Code/CU/IJS-Website/IJSnew/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's verify that the replacements took place as expected
import re
print("TITLE:", re.search(r'<title>(.*?)</title>', content).group(1))

# Search for the old and new description
m1 = re.search(r'<meta name="description"[^>]+content="(.*?)"', content, re.DOTALL | re.IGNORECASE)
if m1:
    print("META DESC:", m1.group(1))

m2 = re.search(r'<h1 class="text-anime-style-2 stats-section-hero-title">(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
if m2:
    print("NEW HERO TITLE:", m2.group(1).strip())

m3 = re.search(r'<p class="lead">(.*?)</p>', content, re.DOTALL | re.IGNORECASE)
if m3:
    print("NEW HERO SUBTEXT:", m3.group(1).strip())

print("success")
