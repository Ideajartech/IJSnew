import os
import re

root_dir = r"e:\XAMMP\htdocs\IJSnew"
source_file = os.path.join(root_dir, "index.html")

# Read the source testimonial section
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

testimonial_match = re.search(r'<!-- Testimonial Section Start -->.*?<!-- Testimonial Section End -->', content, re.DOTALL)
if not testimonial_match:
    print("Could not find testimonial section in index.html")
    exit(1)

new_testimonial = testimonial_match.group(0)

# Target files with the same 10-slide layout
target_files = ["about.html", "mvg.html"]

for target_file in target_files:
    file_path = os.path.join(root_dir, target_file)
    if not os.path.exists(file_path):
        continue
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        # Check if markers exist
        if "<!-- Testimonial Section Start -->" in file_content and "<!-- Testimonial Section End -->" in file_content:
            updated_content = re.sub(r'<!-- Testimonial Section Start -->.*?<!-- Testimonial Section End -->', new_testimonial, file_content, flags=re.DOTALL)
            
            if updated_content != file_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Updated testimonial section in: {target_file}")
            else:
                print(f"No changes needed in {target_file}")
        else:
            print(f"Markers not found in {target_file}")
    except Exception as e:
        print(f"Error processing {target_file}: {e}")
