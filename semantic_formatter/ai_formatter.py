import os
import re
import time
import google.generativeai as genai
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('models/gemini-2.0-flash-lite')

PROMPT_TEMPLATE = """You are a semantic formatter for a literature website. Your task is to take the following raw text from a literary work and format it semantically in Markdown.

Rules:
1. Structure the text by identifying the meaning of the sentences.
2. Identify citations, quotes, titles, headings, subheadings, references, emphasis, paragraphs, lists, etc.
3. Use appropriate Markdown tags.
4. Do not add any extra text or explanation.
5. Do not remove or modify existing text content (preserving text integrity is CRITICAL).
6. The text will be rendered with CSS/11ty.
7. Do not add H1 or # elements (they are handled by the site's template). Use H2 (##) or lower if needed for internal sections.
8. Standardize dialogue to use em-dashes (—) at the start of paragraphs, following Spanish RAE standards (no space after the em-dash).
9. If the text already has a clear structure, return it exactly as is.

Text to format:
---START OF TEXT---
{text}
---END OF TEXT---

Return ONLY the formatted markdown content. No preamble, no postamble."""

def format_text_with_ai(text):
    """
    Sends the text to Gemini API for semantic formatting.
    Has exponential backoff for 429 errors.
    """
    if not text.strip():
        return text

    prompt = PROMPT_TEMPLATE.format(text=text)
    
    wait_time = 10
    for attempt in range(5):
        try:
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text.strip()
            else:
                print(f"Empty response from AI on attempt {attempt + 1}")
        except Exception as e:
            err_str = str(e)
            print(f"Error calling Gemini API: {err_str}")
            if "429" in err_str:
                print(f"Quota exceeded. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff
            else:
                time.sleep(2)
    
    return None

def process_file(filepath, write=False):
    """
    Reads a file, extracts body, formats with AI, and reconstructs the file.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        full_content = f.read()

    # Split frontmatter
    parts = re.split(r'^---\s*$', full_content, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        # No frontmatter?
        frontmatter = ""
        body = full_content
    else:
        frontmatter = parts[1]
        body = parts[2]

    formatted_body = format_text_with_ai(body)
    
    if formatted_body is None:
        print(f"Skipping {filepath} due to API errors.")
        return False

    new_content = f"---\n{frontmatter}---\n\n{formatted_body}\n"
    
    if write:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    else:
        # Dry run: print a snippet
        print(f"--- PREVIEW for {os.path.basename(filepath)} ---")
        print(formatted_body[:500] + "...")
        print("-" * 30)
        return True

def process_directory(directory, write=False, limit=None):
    """
    Processes all markdown files in a directory recursively.
    """
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and not file == 'index.md':
                md_files.append(os.path.join(root, file))

    if limit:
        md_files = md_files[:limit]

    print(f"Found {len(md_files)} files to process in {directory}.")
    
    success_count = 0
    for filepath in tqdm(md_files, desc="Formatting files"):
        if process_file(filepath, write=write):
            success_count += 1
        # Moderate rate limit to avoid 429
        time.sleep(1)

    print(f"Finished. Successfully processed {success_count}/{len(md_files)} files.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='AI Semantic Formatter using Gemini')
    parser.add_argument('path', help='File or directory to process')
    parser.add_argument('--write', action='store_true', help='Actually write changes to files')
    parser.add_argument('--limit', type=int, help='Limit number of files to process')
    args = parser.parse_args()

    if os.path.isfile(args.path):
        process_file(args.path, write=args.write)
    elif os.path.isdir(args.path):
        process_directory(args.path, write=args.write, limit=args.limit)
    else:
        print(f"Error: {args.path} is not a valid file or directory.")
