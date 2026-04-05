import os
import re
import yaml

def get_author_metadata(author_dir):
    index_path = os.path.join(author_dir, 'index.md')
    if not os.path.exists(index_path):
        return "Unknown Author", {}

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract name from frontmatter
    frontmatter_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    author_name = os.path.basename(author_dir).capitalize()
    if frontmatter_match:
        try:
            fm = yaml.safe_load(frontmatter_match.group(1))
            author_name = fm.get('title', author_name)
        except:
            pass

    # Extract author dates from the biography text
    dates = ""
    nacio_match = re.search(r'naci(?:ó|o).*?(\d{4})', content)
    murio_match = re.search(r'muri(?:ó|o).*?(\d{4})', content)
    if nacio_match and murio_match:
        dates = f"{nacio_match.group(1)} - {murio_match.group(1)}"
    elif nacio_match:
        dates = f"n. {nacio_match.group(1)}"

    # Map titles to book info
    work_map = {}
    sections = re.split(r'([A-Z][^(\n]+? \(\d{4}\))', content)
    for i in range(1, len(sections), 2):
        current_book = sections[i].strip()
        items_text = sections[i+1]
        titles = re.findall(r'(?:\d+\.\s+|[—–-]\s+|ÍNDICE:\s+|Narrativa:\s+)([A-Z][^,.\n]{3,})', items_text)
        for t in titles:
            work_map[t.strip().lower()] = current_book

    full_author_info = f"{author_name}"
    if dates:
        full_author_info += f" ({dates})"

    return full_author_info, work_map

def reformat_file(filepath, author_metadata, work_map):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return None
    
    frontmatter_raw = match.group(1).strip()
    body = match.group(2).strip()
    
    try:
        fm = yaml.safe_load(frontmatter_raw)
    except:
        return None

    title = fm.get('title', 'Unknown Title')
    book_info = work_map.get(title.lower(), "")
    
    # 1. Strip redundant metadata from start of body
    meta_end_match = re.search(r'\([^)]*\d{4}[^)]*\)\s*(?:[^A-Z\n]*\([^)]*\d{4}[^)]*\)\s*)*', body)
    if meta_end_match and meta_end_match.start() < 100:
        potential_body_start = body[meta_end_match.end():].strip()
        second_meta_match = re.search(r'^[^(.]+\(\d{4}\)', potential_body_start)
        if second_meta_match:
             potential_body_start = potential_body_start[second_meta_match.end():].strip()
        real_start = re.search(r'[A-Z][a-z]+\s+[a-z]+\s+[a-z]+', potential_body_start)
        if real_start:
            body = potential_body_start[real_start.start():].strip()

    # 2. Standardize Dialogue
    body = re.sub(r'^\s*[-–—]\s*', '— ', body, flags=re.MULTILINE)
    body = re.sub(r'([.?!])\s+[-–—]\s+([A-Z])', r'\1\n\n— \2', body)
    body = re.sub(r'\s+M-bM-\^@M-\^T\s*', r'\n\n— ', body)

    # 3. Conservative Paragraphing
    if body.count('\n') < 5 and len(body) > 500:
        sentences = re.split(r'([.?!])\s+([A-Z][a-z]{2,})', body)
        new_body = ""
        current_len = 0
        for i in range(0, len(sentences), 3):
            part = sentences[i]
            new_body += part
            current_len += len(part)
            if i + 1 < len(sentences):
                punct = sentences[i+1]
                next_start = sentences[i+2]
                new_body += punct
                if current_len > 400:
                    new_body += "\n\n"
                    current_len = 0
                else:
                    new_body += " "
                new_body += next_start
        body = new_body

    # 4. Standardize separators
    body = re.sub(r'^\s*\* \* \*\s*$', '***', body, flags=re.MULTILINE)
    body = re.sub(r'^\s*\*\*\*\s*$', '***', body, flags=re.MULTILINE)

    # 5. Clean up redundant year at the end
    body = re.sub(r'\n\s*\(\d{4}\)\s*$', '', body)

    # Reconstruct
    new_content = "---\n" + frontmatter_raw + "\n---\n\n"
    new_content += f"# {title}\n\n"
    new_content += f"*{author_metadata}*\n"
    if book_info:
        new_content += f"*{book_info}*\n"
    new_content += "\n" + body.strip() + "\n"
    
    return new_content

def process_author(author_dir):
    author_info, work_map = get_author_metadata(author_dir)
    print(f"Processing author: {author_info}")
    
    for filename in os.listdir(author_dir):
        if filename == 'index.md' or not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(author_dir, filename)
        new_content = reformat_file(filepath, author_info, work_map)
        
        if new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Reformatted: {filename}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_author(sys.argv[1])
    else:
        print("Usage: python reformat_author.py <author_dir>")
