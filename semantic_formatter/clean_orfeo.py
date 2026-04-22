import re

def clean_orfeo(content):
    # Frontmatter handling (assuming it's already okay, but we'll preserve it)
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content # Something is wrong
    
    frontmatter = parts[1]
    body = parts[2]
    
    # 1. Standardize Header and Metadata
    new_header = """# Sonetos a Orfeo

**Rainer Maria Rilke**

*Die Sonette an Orpheus (1923)*
*Versión de Carlos Barral (Primera Parte) y Jaime Ferreiro Alemparte (Segunda Parte)*
"""
    
    # 2. Process Body
    lines = body.split('\n')
    new_body_lines = []
    
    # Roman numeral pattern
    roman_pattern = r'^(I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX|XX|XXI|XXII|XXIII|XXIV|XXV|XXVI|XXVII|XXVIII|XXIX)$'
    
    current_part = None
    
    for line in lines:
        stripped = line.strip().strip('#').strip().replace('*', '').split('[')[0].strip()
        
        # Detect Part Headers
        if 'PRIMERA PARTE' in line.upper():
            new_body_lines.append("## Primera Parte")
            continue
        if 'SEGUNDA PARTE' in line.upper():
            new_body_lines.append("## Segunda Parte")
            continue
        
        # Detect Sonnet Numbers
        if re.match(roman_pattern, stripped, re.IGNORECASE):
            # Check if there's a note marker like [22]
            note_marker = ""
            if '[' in line:
                note_marker = ' [' + line.split('[')[1].split(']')[0] + ']'
            new_body_lines.append(f"**{stripped.upper()}**{note_marker}")
            continue
            
        # Clean up text from previous mess
        line = re.sub(r'([A-Z]+)\*\*([A-Z]+)\*\*', r'\1\2', line)
        line = re.sub(r'\*\*([A-Z]+)\*\*([A-Z]+)', r'\1\2', line)
        line = line.replace('****', '**') # Clean double bolding
        # Fix the specific words
        line = line.replace('V**II**', 'VII')
        line = line.replace('XX**II**', 'XXII')
        line = line.replace('X**XV**', 'XXV')
        line = line.replace('siglo **XV**', 'siglo XV')
        
        # Remove redundant author/title info in body if accidentally kept
        if line.strip() in ["*Rainer María Rilke*", "*(Praga,*", "*1875 - Suiza, 1926)*", "Sonetos a Orfeo (1923)", "(Die Sonette an Orpheus)", "Versión de Carlos Barral", "Versión de Jaime Ferreiro Alemparte"]:
            continue
            
        new_body_lines.append(line)
        
    final_body = '\n'.join(new_body_lines)
    # Remove leading blank lines from body
    while final_body.startswith('\n'):
        final_body = final_body[1:]
        
    return f"---{frontmatter}--- \n{new_header}\n{final_body}"

file_path = '/home/szortofbad/projects/literatura-us-2.0/site/src/content/authors/rmr/rmr_orfeo.md'
with open(file_path, 'r') as f:
    content = f.read()

fixed_content = clean_orfeo(content)

with open(file_path, 'w') as f:
    f.write(fixed_content)
print("Cleaned orfeo.md")
