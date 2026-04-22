import re

def clean_breve(content):
    # Preserve frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content
    frontmatter = parts[1]
    body = parts[2]
    
    new_header = """# Brevísima Antología Poética

**Rainer Maria Rilke**

*Selección de poemas de diversas colecciones*
"""
    
    # Collection names for H2
    collections = [
        "Ofrenda a los Lares",
        "Coronado sueño",
        "Adviento",
        "Poemas tempranos",
        "Libro de las horas",
        "Libro de las Imágenes",
        "Nuevos poemas"
    ]
    
    # 1. Strip the redundant headers from the start of the body
    # Look for the first occurrence of a collection or poem and start there
    # Or just remove the specific block if found
    body = re.sub(r'(?s)^.*?## Ofrenda a los Lares', '## Ofrenda a los Lares', body)
    
    lines = body.split('\n')
    new_body_lines = []
    
    roman_headers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    
    for line in lines:
        # Detect legacy headers like # ## Title or ### ## Title
        # Strip all hashes, stars, and spaces
        stripped_full = line.strip().replace('#', '').replace('*', '').strip()
        
        # Detect Collection Headers (H2)
        match_collection = False
        for c in collections:
            if stripped_full.upper() == c.upper() or (c.upper() in stripped_full.upper() and len(stripped_full) < len(c) + 10):
                new_body_lines.append(f"## {c}")
                match_collection = True
                break
        if match_collection:
            continue
            
        # Detect Poem Titles (H3)
        # If the line starts with hashes or is all caps and reasonably short
        if (line.strip().startswith('#') or line.strip().startswith('*')) and len(stripped_full) > 0:
            if len(stripped_full.split()) < 10 and not stripped_full.isdigit():
                 new_body_lines.append(f"### {stripped_full.title()}")
                 continue
                 
        # Detect Roman numerals in brackets like [ 1 ]
        if re.match(r'^\[\s*\d+\s*\]$', stripped_full):
            new_body_lines.append(f"**{stripped_full.replace(' ', '')}**")
            continue

        new_body_lines.append(line)
        
    final_body = '\n'.join(new_body_lines)
    final_body = re.sub(r'\n{3,}', '\n\n', final_body).strip()
    
    return f"---{frontmatter}--- \n{new_header}\n\n{final_body}"

file_path = '/home/szortofbad/projects/literatura-us-2.0/site/src/content/authors/rmr/rmr_breve.md'
with open(file_path, 'r') as f:
    content = f.read()

fixed_content = clean_breve(content)

with open(file_path, 'w') as f:
    f.write(fixed_content)
print("Final Cleaned breve.md")
