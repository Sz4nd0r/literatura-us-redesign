import os
import re
import sys

def restore_paragraphs(text, max_chars=500):
    """Restores paragraph breaks in flattened text based on sentence ends."""
    if not text.strip():
        return text
    
    # Heuristic: Find period followed by space and uppercase letter
    # but avoid common abbreviations like Sr., Dr., etc.
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z¿¡])', text)
    
    paragraphs = []
    current_para = []
    current_len = 0
    
    for sentence in sentences:
        current_para.append(sentence)
        current_len += len(sentence)
        if current_len >= max_chars:
            paragraphs.append(" ".join(current_para))
            current_para = []
            current_len = 0
            
    if current_para:
        paragraphs.append(" ".join(current_para))
        
    return "\n\n".join(paragraphs)

def format_cronologia(text):
    """Formats Chronology section as a bulleted list."""
    # Look for patterns like "1920: Nace..."
    lines = re.split(r'(\d{4}:)', text)
    if len(lines) <= 1:
        return text
    
    result = []
    # If there's text before the first date
    intro = lines[0].strip()
    if intro:
        result.append(intro)
    
    for i in range(1, len(lines), 2):
        date_part = lines[i]
        content_part = lines[i+1].strip() if i+1 < len(lines) else ""
        # Remove trailing date part if it's there
        content_part = re.sub(r'\s*\d{4}:$', '', content_part)
        result.append(f"- **{date_part[:-1]}**: {content_part}")
        
    return "\n".join(result)

def format_indice(text):
    """Attempts to format the INDICE section conservatively."""
    if not text.strip():
        return text
        
    # Pre-process: Identify sub-categories like "Novela:", "Cuentos:", "Narrativa:"
    # and turn them into headers
    text = re.sub(r'(^|\s)(Novela|Cuentos|Narrativa|Poesía|Ensayo|Obras en colaboración|Teoría|Crítica):', r'\1\n#### \2\n', text, flags=re.IGNORECASE)
    
    # Pattern: Book Title (Year)
    parts = re.split(r'([A-Za-zñáéíóúÜ\s,.:;]+ \(\d{4}(?:-\d{4})?\):?)', text)
    if len(parts) <= 1:
        return restore_paragraphs(text)
    
    result = []
    intro = parts[0].strip()
    if intro:
        result.append(restore_paragraphs(intro))
        
    for i in range(1, len(parts), 2):
        book_part = parts[i].strip()
        book_part = re.sub(r'^[\s,.:;]+', '', book_part)
        
        stories_part = parts[i+1].strip() if i+1 < len(parts) else ""
        
        if book_part:
            # If it looks like a year-only or very short, don't H3 it
            if len(book_part) > 5:
                result.append(f"\n### {book_part}")
            else:
                result.append(f"\n**{book_part}**")
        
        # Don't bullet stories anymore, just restore paragraphs/spacing
        # This is much safer.
        if stories_part.strip():
            # If there are manual line breaks or double spaces, preserve them as bullets
            if "\n" in stories_part or "  " in stories_part:
                stories = re.split(r'\n|\s{2,}', stories_part)
                for s in stories:
                    s_clean = s.strip()
                    if s_clean:
                        if s_clean.startswith('####'):
                            result.append(f"\n{s_clean}")
                        else:
                            result.append(f"- {s_clean}")
            else:
                # Just restore paragraphs
                result.append(restore_paragraphs(stories_part))
            
    return "\n".join(result)

def reformat_index(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content:
        return

    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return
    
    frontmatter = fm_match.group(0)
    body = content[fm_match.end():].strip()
    
    if not body:
        return

    # Image handling
    img_match = re.search(r'!\[\]\(/assets/images/[^)]+\)', body)
    if img_match:
        img_tag = img_match.group(0)
        body = body.replace(img_tag, "").strip()
        first_line_match = re.match(r'^[^.!?\n]+[.!?\n]', body)
        if first_line_match:
            pos = first_line_match.end()
            body = body[:pos].strip() + "\n\n" + img_tag + "\n\n" + body[pos:].strip()
        else:
            body = img_tag + "\n\n" + body

    # Split Sections
    # Fix existing mess
    body = re.sub(r'## (Cronología|ÍNDICE|Obras|CONTENIDO|Entrevistas)', r'\1', body, flags=re.IGNORECASE)
    body = re.sub(r'#{1,3}\s*', '', body) # Remove any hashes we might have added incorrectly
    
    sections = re.split(r'(Cronología|ÍNDICE:|Obras:|CONTENIDO:|Entrevistas:)', body, flags=re.IGNORECASE)
    
    new_chunks = []
    bio = sections[0].strip()
    if bio:
        new_chunks.append(restore_paragraphs(bio))
    
    for i in range(1, len(sections), 2):
        section_header = sections[i].strip()
        section_content = sections[i+1].strip() if i+1 < len(sections) else ""
        
        if section_content.startswith(":"):
            section_content = section_content[1:].strip()
            
        header_text = section_header.replace(":", "").capitalize()
        new_chunks.append(f"\n\n## {header_text}")
        
        if "Cronología" in header_text:
            new_chunks.append(format_cronologia(section_content))
        elif "Índice" in header_text or "Obras" in header_text:
            new_chunks.append(format_indice(section_content))
        else:
            new_chunks.append(restore_paragraphs(section_content))

    final_body = "".join(new_chunks).strip()
    final_content = frontmatter + "\n" + final_body + "\n"
    
    # Final cleanup of double headers and empty headers
    final_content = re.sub(r'## (Índice|Obras)\n####', r'## \1\n\n####', final_content)
    final_content = re.sub(r'### \n', '', final_content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Reformatted index: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path):
            reformat_index(path)
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                if 'index.md' in files:
                    reformat_index(os.path.join(root, 'index.md'))
