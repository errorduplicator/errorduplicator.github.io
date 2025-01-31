import os
import re
import requests

# Define the CSS file
css_file = "/workspaces/errorduplicator.github.io/cmu-serif"

# Check if the CSS file exists
if not os.path.isfile(css_file):
    print(f"CSS file not found: {css_file}")
    exit(1)

# Read the CSS file
with open(css_file, 'r') as file:
    css_content = file.read()

# Extract URLs from the CSS file
urls = re.findall(r'url\("([^"]+\.ttf)"', css_content)

# Download the .ttf files
for url in urls:
    full_url = f"https://fontlibrary.org{url}"
    local_path = f"/workspaces/errorduplicator.github.io/assets/fonts/{os.path.basename(url)}"
    print(f"Downloading {full_url} to {local_path}")
    response = requests.get(full_url)
    if response.status_code == 200:
        with open(local_path, 'wb') as font_file:
            font_file.write(response.content)
    else:
        print(f"Failed to download {full_url}")