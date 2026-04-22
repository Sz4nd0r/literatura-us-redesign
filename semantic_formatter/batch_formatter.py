import os
import re
import yaml
from formatter_utils import classify_file, get_word_count, detect_metadata_in_body, clean_dialogue, standardize_headers

def format_file(filepath, title, write=False):
    """
    Applies formatting to a single file and optionally writes it back.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        full_content = f.read()
            
    parts = re.split(r'^---\s*$', full_content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return None, None
        
    frontmatter_raw = parts[1]
    body = parts[2]
    
    # 1. Detect and separate metadata
    metadata_lines, content = detect_metadata_in_body(body)
    
    # 2. Classify (currently mostly for reporting)
    category = classify_file(content)
    orig_body_wc = get_word_count(body)
    orig_char_count = len(body)
    
    # 3. Apply formatting based on category
    formatted_content = content
    if category == 'story':
        formatted_content = clean_dialogue(content)
    
    formatted_content = standardize_headers(formatted_content, title)
    
    # 4. Reconstruct body
    new_body = ""
    if metadata_lines:
        new_body += "\n".join(metadata_lines) + "\n\n"
    new_body += formatted_content
    
    new_full_content = f"---\n{frontmatter_raw}---\n{new_body}\n"
    
    # Verification: check word count and char count
    new_body_wc = get_word_count(new_body)
    new_char_count = len(new_body)
    
    if write:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_full_content)
            
    return (orig_body_wc, new_body_wc, orig_char_count, new_char_count)

def process_author(author_dir, write=False):
    """
    Orchestrates the processing of all files for a specific author.
    """
    files = [f for f in os.listdir(author_dir) if f.endswith('.md') and f != 'index.md']
    print(f"Processing {len(files)} files in {author_dir} (Write: {write})...")
    
    results = []
    for filename in files:
        filepath = os.path.join(author_dir, filename)
        
        # Get title from frontmatter
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        fm_match = re.search(r'^title:\s*(.*)$', content, re.MULTILINE)
        title = fm_match.group(1).strip() if fm_match else filename
        
        orig_wc, new_wc, orig_cc, new_cc = format_file(filepath, title, write=write)
        
        if orig_wc is not None:
            wdiff = new_wc - orig_wc
            cdiff_pct = (new_cc - orig_cc) / orig_cc if orig_cc > 0 else 0
            
            results.append({
                'filename': filename,
                'wdiff': wdiff,
                'cdiff_pct': cdiff_pct
            })
            
            if abs(wdiff) > 20 or abs(cdiff_pct) > 0.05:
                status = "WARNING" if abs(cdiff_pct) > 0.05 else "INFO"
                print(f"  [{status}] {filename}: WC Diff: {wdiff}, Char Diff: {cdiff_pct:.2%}")
        
    return results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Batch Semantic Formatter')
    parser.add_argument('path', help='Directory to process')
    parser.add_argument('--write', action='store_true', help='Actually write changes to files')
    args = parser.parse_args()
    
    if os.path.isdir(args.path):
        process_author(args.path, write=args.write)
    else:
        print(f"Error: {args.path} is not a directory.")
