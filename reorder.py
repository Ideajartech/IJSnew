import re

with open('/Users/amitsunda/Desktop/Code/CU/IJS-Website/IJSnew/results.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find the <div class="row"> inside our-letest-blog section
start_idx = content.find('<div class="our-letest-blog section position-relative">')
start_row = content.find('<div class="row">', start_idx)
end_row = content.find('</div>\n        </div>\n    </div>\n    <!-- Letest Blog Section End -->', start_row)

row_content = content[start_row + len('<div class="row">'):end_row]

# Extract each col block
blocks = []
current_block = ""
lines = row_content.split('\n')
for line in lines:
    if '<div class="col-lg-4 col-md-6">' in line:
        if current_block.strip():
            blocks.append(current_block)
        current_block = line + '\n'
    else:
        current_block += line + '\n'

if current_block.strip():
    blocks.append(current_block)

# Now we have the blocks
# We define a function to match a block by checking if its title contains specific keywords
def find_block(keywords):
    for b in list(blocks):
        found = True
        for kw in keywords:
            if kw.lower() not in b.lower():
                found = False
        if found:
            blocks.remove(b)
            return b
    print("Could not find block for:", keywords)
    return ""

new_blocks = []
new_blocks.append(find_block(["145k+ reach", "19.06%"]))
new_blocks.append(find_block(["75k views", "30% rise"]))
b_aprisio = find_block(["0 to 50.4"])
b_aprisio = b_aprisio.replace("0 to 50.4 K+", "0 &rarr; 50.4 K+")
new_blocks.append(b_aprisio)
new_blocks.append(find_block(["14k+ mav", "58%"]))
new_blocks.append(find_block(["81% increase", "organic traffic"]))
new_blocks.append(find_block(["222 signups", "hsbc"]))
new_blocks.append(find_block(["40 signups", "linkedin"]))
b_team = find_block(["0 to 100 k+"])
b_team = b_team.replace("0 to 100 K+", "0 &rarr; 100 K+")
new_blocks.append(b_team)
new_blocks.append(find_block(["2808%", "content reach"]))
new_blocks.append(find_block(["571 program signups"]))
new_blocks.append(find_block(["11.4x overall roas"]))
new_blocks.append(find_block(["56% visibility reach"]))
new_blocks.append(find_block(["modern beverage"]))
new_blocks.append(find_block(["927.9k+", "17 leads"]))

# If any leftovers, append them (should not happen if all match)
for b in blocks:
    if b.strip():
        new_blocks.append(b)

new_row_content = "".join(new_blocks)

new_content = content[:start_row + len('<div class="row">\n')] + new_row_content + content[end_row:]

with open('/Users/amitsunda/Desktop/Code/CU/IJS-Website/IJSnew/results.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("success")
