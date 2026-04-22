import os
import re

AUTHORS_DIR = "/home/szortofbad/projects/literatura-us-2.0/site/src/content/authors"

def audit_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {"error": "Invalid frontmatter"}
    
    body = parts[2].strip()
    lines = body.split('\n')
    
    score = 0
    issues = []
    
    # 1. Header Health (Critical)
    if not body.startswith('# '):
        score += 50
        issues.append("missing_h1")
    
    # 2. Author Name Line
    if len(lines) > 1 and not re.search(r'\*[A-Z].*\*$', lines[1].strip() or lines[2].strip()):
        # Lower penalty if it's there but maybe not italicized correctly
        if re.search(r'[A-Z][a-z]+ [A-Z][a-z]+', lines[1].strip() or lines[2].strip()):
            score += 5
            issues.append("author_italics_missing")
        else:
            score += 20
            issues.append("author_line_missing")

    # 3. Dialogue Check (for prose)
    if '—' not in body and ('"' in body or '«' in body or '“' in body):
        score += 30
        issues.append("legacy_quotes_only")
    
    # 4. Metadata Residuals
    if re.search(r'\(n\. \d+\)', body) or re.search(r'Fragmento de', body, re.I):
        score += 15
        issues.append("metadata_residuals")

    # 5. Joined First Paragraph (Common bug)
    if len(lines) > 0 and re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+ [A-Z]', lines[0]): # e.g. "Title Word..."
         # This check is fuzzy, better to check if first line is very long and has title-like start
         pass

    return {"score": score, "issues": issues}

def run_audit():
    author_scores = {}
    
    for author in sorted(os.listdir(AUTHORS_DIR)):
        author_path = os.path.join(AUTHORS_DIR, author)
        if not os.path.isdir(author_path):
            continue
            
        total_score = 0
        file_count = 0
        all_issues = set()
        
        for root, _, files in os.walk(author_path):
            for file in files:
                if file.endswith('.md') and file != 'index.md':
                    file_path = os.path.join(root, file)
                    result = audit_file(file_path)
                    if "error" not in result:
                        total_score += result["score"]
                        file_count += 1
                        all_issues.update(result["issues"])
        
        if file_count > 0:
            avg_score = total_score / file_count
            author_scores[author] = {
                "score": round(avg_score, 2),
                "total_score": total_score,
                "file_count": file_count,
                "issues": list(all_issues)
            }

    # Sort by score descending
    sorted_authors = sorted(author_scores.items(), key=lambda x: x[1]["score"], reverse=True)
    
    print(f"{'Author':<20} | {'Score':<6} | {'Files':<5} | {'Issues'}")
    print("-" * 60)
    for auth, data in sorted_authors:
        if data["score"] > 0:
            print(f"{auth:<20} | {data['score']:<6} | {data['file_count']:<5} | {', '.join(data['issues'])}")
            if auth == "marcos":
                 print(f"DEBUG: Found 'marcos' in {os.path.join(AUTHORS_DIR, auth)}")

if __name__ == "__main__":
    run_audit()
