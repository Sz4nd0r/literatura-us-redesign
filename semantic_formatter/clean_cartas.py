import re

def clean_cartas(content):
    parts = content.split('---', 2)
    frontmatter = parts[1]
    body = parts[2]
    
    new_header = """# Cartas a un joven poeta

**Rainer Maria Rilke**

*Versión y prólogo de Franz Xaver Kappus*
"""
    
    # Pre-clean the body of common junk before line-by-line processing
    body = re.sub(r'\*# Cartas A Un Joven Poeta\*', '', body)
    body = re.sub(r'\*Rainer María Rilke\*', '', body)
    body = re.sub(r'\*\(Praga,\*', '', body)
    body = re.sub(r'\*1875 - Suiza, 1926\)\*', '', body)
    
    lines = body.split('\n')
    new_body_lines = []
    
    roman_headers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    current_roman = "I"
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip().strip('#').strip().replace('*', '')
        
        # Detect Intro
        if stripped == "Introducción":
            new_body_lines.append("## Introducción")
            i += 1
            continue
            
        # Detect Roman Numerals
        if stripped in roman_headers:
            current_roman = stripped
            i += 1
            continue
            
        # Detect Location/Date (can be multi-line)
        # We look for a line starting with a capital letter (City) and containing a date
        # or followed by a date.
        date_pattern = r'^[A-Z].*, a \d+ de [a-z]+ de \d+'
        
        # Check if current line + next line forms a date
        possible_date = stripped
        look_ahead = 1
        found_date = False
        while i + look_ahead < len(lines) and look_ahead < 3:
            next_stripped = lines[i+look_ahead].strip().strip('#').strip().replace('*', '')
            possible_date += " " + next_stripped
            if re.match(date_pattern, possible_date):
                new_body_lines.append(f"## Carta {current_roman}: {possible_date}")
                i += look_ahead + 1
                found_date = True
                break
            look_ahead += 1
            
        if found_date:
            continue
            
        # Single line date match
        if re.match(date_pattern, stripped):
             new_body_lines.append(f"## Carta {current_roman}: {stripped}")
             i += 1
             continue

        # Detect Notes
        if stripped == "Notas":
            new_body_lines.append("## Notas")
            i += 1
            continue
            
        new_body_lines.append(line)
        i += 1
        
    final_body = '\n'.join(new_body_lines)
    # Remove excessive blank lines
    final_body = re.sub(r'\n{3,}', '\n\n', final_body).strip()
    
    return f"---{frontmatter}--- \n{new_header}\n\n{final_body}"

file_path = '/home/szortofbad/projects/literatura-us-2.0/site/src/content/authors/rmr/rmr_cartas.md'
with open(file_path, 'r') as f:
    content = f.read()

fixed_content = clean_cartas(content)

with open(file_path, 'w') as f:
    f.write(fixed_content)
print("Deep Cleaned cartas.md")
