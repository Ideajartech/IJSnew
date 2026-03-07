with open('/Users/amitsunda/Desktop/Code/CU/IJS-Website/IJSnew/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements for title and meta description
content = content.replace(
    '<title>Idea Jar Studio | Growth Marketing for Tech & Product-led businesses AI, SaaS & DeepTech</title>',
    '<title>Growth Marketing for Tech & Product Companies | Idea Jar Studio</title>'
)

content = content.replace(
    '<meta property="og:title"\n      content="Idea Jar Studio | Growth Marketing for Tech & Product-led businesses AI, SaaS & DeepTech">',
    '<meta property="og:title"\n      content="Growth Marketing for Tech & Product Companies | Idea Jar Studio">'
)

content = content.replace(
    '<meta name="twitter:title"\n      content="Idea Jar Studio | Growth Marketing for Tech & Product-led businesses AI, SaaS & DeepTech">',
    '<meta name="twitter:title"\n      content="Growth Marketing for Tech & Product Companies | Idea Jar Studio">'
)

old_desc = "Move beyond referral-led growth. We build inbound marketing systems that help tech-driven and product-led companies get discovered, trusted, and chosen."
new_desc = "Move beyond referral-led growth. We build inbound marketing systems for tech-driven and product-led companies using SEO, content, and positioning so they get discovered, trusted, and chosen."

content = content.replace(
    f'<meta name="description"\n      content="{old_desc}">',
    f'<meta name="description"\n      content="{new_desc}">'
)

content = content.replace(
    f'<meta property="og:description"\n      content="{old_desc}">',
    f'<meta property="og:description"\n      content="{new_desc}">'
)

content = content.replace(
    f'<meta name="twitter:description"\n      content="{old_desc}">',
    f'<meta name="twitter:description"\n      content="{new_desc}">'
)

# Replacements for Hero Banner
content = content.replace(
    '<h1 class="text-anime-style-2 stats-section-hero-title">Build predictable inbound demand beyond referrals</h1>',
    '<h1 class="text-anime-style-2 stats-section-hero-title">Build predictable inbound demand beyond referrals.</h1>'
)

content = content.replace(
    '<p class="lead">We help AI, SaaS, and deeptech companies get discovered, trusted, and chosen through integrated\n            inbound marketing, before sales steps in</p>',
    '<p class="lead">We help tech-driven and product-led companies become discovered, trusted, and impossible to ignore through inbound marketing, before sales steps in.</p>'
)

# And also updating the commented out slider just in case
content = content.replace(
    '<h1 class="text-anime-style-2 text-start text-heading" data-cursor="-opaque">Build\n                                       predictable inbound demand beyond referrals.</span></h1>',
    '<h1 class="text-anime-style-2 text-start text-heading" data-cursor="-opaque">Build predictable inbound demand beyond referrals.</span></h1>'
)
content = content.replace(
    '<p class="text-start hero-subheading">We help AI, SaaS, and deeptech companies get\n                                       discovered, trusted, and chosen through integrated inbound marketing, before\n                                       sales steps in.</p>',
    '<p class="text-start hero-subheading">We help tech-driven and product-led companies become discovered, trusted, and impossible to ignore through inbound marketing, before sales steps in.</p>'
)



with open('/Users/amitsunda/Desktop/Code/CU/IJS-Website/IJSnew/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("success")
