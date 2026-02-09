import os
import re

root_dir = r"e:\XAMMP\htdocs\IJSnew"
target_url = "https://cal.com/mythri-ideajarstudio/strategy-call"

# Regex to find the anchor tag with the specific URL
# We want to insert target="_blank" if it doesn't exist
pattern = re.compile(f'href="{re.escape(target_url)}"', re.IGNORECASE)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if target_url in content:
                    # Simple strategy: replace the href string with the href string + target="_blank"
                    # But we should check if target="_blank" is already there to avoid duplicates
                    
                    # This is slightly naive but effective for this codebase structure:
                    # <a href="..." class="..."> -> <a href="..." target="_blank" rel="noopener" class="...">
                    
                    # Let's use a more robust replacement:
                    # Find instances where the URL is in the href, and check if target="_blank" is present in that tag.
                    
                    # Using a simple replacement for now since I know the structure from previous view_file
                    # Original: href="https://cal.com/mythri-ideajarstudio/strategy-call"
                    # New: href="https://cal.com/mythri-ideajarstudio/strategy-call" target="_blank"
                    
                    # Check if it already has target="_blank" nearby
                    # We'll replace the URL match specifically
                    
                    def add_target(match):
                        full_match = match.group(0)
                        # Look ahead in the content to see if target="_blank" exists for this tag
                        # Or just replace and handle duplicates later. 
                        # Given the previous task, I just added these links, so they won't have it.
                        return f'{full_match} target="_blank"'

                    new_content = content.replace(f'href="{target_url}"', f'href="{target_url}" target="_blank"')
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Added target='_blank' to: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
