#!/bin/bash

# Define the CSS file
css_file="/workspaces/errorduplicator.github.io/cmu-serif"

# Check if the CSS file exists
if [ ! -f "$css_file" ]; then
    echo "CSS file not found: $css_file"
    exit 1
fi

# Extract URLs from the CSS file and download the .ttf files
grep -oP 'url\("\K[^"]+\.ttf' "$css_file" | while IFS= read -r url; do
    # Download the file
    wget https://fontlibrary.org/face/cmu-serif$url -O "/workspaces/"errorduplicator".github.io/assets/fonts/$(basename $url)"
done