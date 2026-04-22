import re

def fix_sonnets(content):
    lines = content.split('\n')
    new_lines = []
    
    # Roman numeral pattern for detection
    roman_pattern = r'^(I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX|XX|XXI|XXII|XXIII|XXIV|XXV|XXVI|XXVII|XXVIII|XXIX)$'
    
    for line in lines:
        # 1. Detect if it's a sonnet header line
        # Strip potential mess markers from previous failed attempt
        stripped = line.strip().strip('#').strip().replace('*', '')
        
        if re.match(roman_pattern, stripped, re.IGNORECASE):
            # It's a sonnet number. Standardize it to uppercase bold.
            new_lines.append(f"**{stripped.upper()}**")
            continue

        # 2. Fix partial bolding in text (like XX**II**)
        # Undo any ** inside words
        line = re.sub(r'([A-Z]+)\*\*([A-Z]+)\*\*', r'\1\2', line)
        line = re.sub(r'\*\*([A-Z]+)\*\*([A-Z]+)', r'\1\2', line)
        
        # Specific fixes for known breaks
        line = line.replace('XX**II**', 'XXII')
        line = line.replace('V**II**', 'VII')
        line = line.replace('X**XV**', 'XXV')
        line = line.replace('**XV****II**I', 'XVIII')
        line = line.replace('**XV****II**', 'XVII')
        
        # Also fix the weird multi-hash headers I introduced
        if line.startswith('## ## ## ##'):
             # If it's something like ## ## ## ## XXIX, it should have been caught by the roman_pattern
             # But if it wasn't, let's look at what's left
             remainder = line.replace('#', '').strip().replace('*', '')
             if re.match(roman_pattern, remainder, re.IGNORECASE):
                 new_lines.append(f"**{remainder.upper()}**")
                 continue
        
        new_lines.append(line)
            
    return '\n'.join(new_lines)

file_path = '/home/szortofbad/projects/literatura-us-2.0/site/src/content/authors/rmr/rmr_orfeo.md'
with open(file_path, 'r') as f:
    content = f.read()

fixed_content = fix_sonnets(content)

with open(file_path, 'w') as f:
    f.write(fixed_content)
print("Fixed orfeo.md")
