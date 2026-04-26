import os

def remove_h1_titles(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # Remove lines that start with exactly one #
                    # We check if it starts with # and NOT ##
                    new_lines = [line for line in lines if not (line.startswith('*#') and not line.startswith('*##'))]
                    
                    if len(new_lines) != len(lines):
                        print(f"Updating: {file_path}")
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(new_lines)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    target_dir = "/home/szortofbad/projects/literatura-us-2.0/site/src/content/authors"
    print(f"Starting H1 title removal in {target_dir}...")
    remove_h1_titles(target_dir)
    print("Done.")
