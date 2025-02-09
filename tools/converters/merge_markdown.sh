#!/bin/bash

# Output file
output_file="merged_markdown.md"
temp_toc="temp_toc.md"

# Clear or create output file
> "$output_file"
> "$temp_toc"

# Counter for sections
counter=1

# Function to process markdown files
process_markdown_files() {
    local dir="$1"
    
    # Find all .md files recursively
    find "$dir" -type f -name "*.md" | while read -r file; do
        # Get relative path
        rel_path="${file#./}"
        
        # Create section header for TOC
        echo "[$counter. $(basename "$file" .md)]($rel_path)" >> "$temp_toc"
        
        # Add file content with metadata section
        echo "# $counter. $(basename "$file" .md)" >> "$output_file"
        echo "" >> "$output_file"
        echo "meta:" >> "$output_file"
        echo "- path.fs: $rel_path" >> "$output_file"
        echo "" >> "$output_file"
        
        # Add file content
        cat "$file" >> "$output_file"
        echo -e "\n\n---\n\n" >> "$output_file"
        
        ((counter++))
    done
}

# Add initial TOC header if there are markdown files
if [ $(find . -type f -name "*.md" | wc -l) -gt 1 ]; then
    echo "# Table of Contents" > "$output_file"
    echo "" >> "$output_file"
fi

# Process all markdown files
process_markdown_files "."

# If we have more than one file, add the TOC
if [ $(find . -type f -name "*.md" | wc -l) -gt 1 ]; then
    # Combine TOC with main content
    cat "$temp_toc" "$output_file" > "temp_merge.md"
    mv "temp_merge.md" "$output_file"
fi

# Clean up temporary file
rm -f "$temp_toc"

echo "Markdown files have been merged into $output_file"