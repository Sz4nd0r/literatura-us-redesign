import re

def classify_file(content):
    """
    Classifies a markdown file into Poetry, Story, or Essay.
    Returns: 'poetry', 'story', 'essay', or 'unknown'
    """
    # Check for poetry-specific patterns (short lines, stanzas)
    lines = [l for l in content.split('\n') if l.strip()]
    if not lines:
        return 'unknown'
        
    short_lines = [l for l in lines if len(l.strip()) < 60]
    if len(short_lines) / len(lines) > 0.8:
        return 'poetry'
    
    # Check for dialogue (Story)
    if '—' in content or '«' in content or '»' in content or '"' in content:
        return 'story'
    
    return 'essay'

def get_word_count(text):
    """Counts words, ignoring markdown symbols and whitespace."""
    clean_text = re.sub(r'[#*`\-_[\]()]', ' ', text)
    return len(clean_text.split())

def clean_dialogue(text):
    """
    Standardizes dialogue to use em-dashes.
    - Replaces start-of-line hyphens/quotes with em-dash.
    - No space after em-dash (RAE standard for opening dialogue).
    """
    # Replace simple dashes, double dashes, or opening quotes at start of paragraph with em-dash
    text = re.sub(r'^[—–\-\s]*["“«"]', '—', text, flags=re.MULTILINE)
    text = re.sub(r'^[—–\-]{1,2}\s*', '—', text, flags=re.MULTILINE)
    
    # Standardize closing quotes if they were used for dialogue
    text = re.sub(r'["”»]\s*$', '', text, flags=re.MULTILINE)
    
    return text

def standardize_headers(text, title):
    """
    Ensures the title is an H1 and section headers are H2.
    """
    lines = text.split('\n')
    new_lines = []
    title_fixed = False
    
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            new_lines.append(line)
            continue
            
        # If line is exactly the title or uppercase version of the title, make it H1 if not already
        if clean_line.lower() == title.lower() or (clean_line.isupper() and len(clean_line) > 3):
            if not title_fixed:
                new_lines.append(f"# {clean_line.title()}")
                title_fixed = True
            else:
                new_lines.append(f"## {clean_line}")
        elif re.match(r'^#{1,6}\s+', clean_line):
            new_lines.append(line)
        else:
            new_lines.append(line)
            
    return '\n'.join(new_lines)

def detect_metadata_in_body(text):
    """
    Detects metadata lines at the top of the body.
    Supports italics, parentheticals, dates, and publication info.
    """
    lines = text.strip().split('\n')
    metadata_lines = []
    content_start_index = 0
    
    # Common metadata patterns
    date_pattern = r'^\s*\(?(\d{4}|\d{4}\s*-\s*\d{4})\)?\s*$'
    city_date_pattern = r'^\s*\(.*,?\s*\d{4}\s*-\s*.*,?\s*\d{4}\)\s*$'
    tagline_pattern = r'^\s*“.*”|^\s*\(“.*”\)'
    pub_pattern = r'^\s*Originalmente publicado|^\s*Publicado en'
    italics_pattern = r'^\s*(\*|_).*(\*|_)\s*$'
    
    for i, line in enumerate(lines):
        clean_line = line.strip()
        if not clean_line:
            continue
            
        # Specific metadata patterns
        matches_pattern = (
            re.match(italics_pattern, clean_line) or
            re.match(date_pattern, clean_line) or
            re.match(city_date_pattern, clean_line) or
            re.match(tagline_pattern, clean_line) or
            re.match(pub_pattern, clean_line, re.IGNORECASE) or
            (clean_line.startswith('(') and (clean_line.endswith(')') or clean_line.endswith(').') or clean_line.endswith('),') or clean_line.endswith('-58.'))) or
            (("Para " in clean_line or "A " in clean_line) and i < 5)
        )
        
        # Also include short lines at the very beginning that are likely names or titles
        is_suspiciously_short = len(clean_line) < 80
        
        if matches_pattern or (i < 12 and is_suspiciously_short):
            metadata_lines.append(f"*{clean_line.strip('*_')}*")
            content_start_index = i + 1
        else:
            break
            
    return metadata_lines, '\n'.join(lines[content_start_index:]).strip()
