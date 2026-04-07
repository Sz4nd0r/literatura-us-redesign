import sys
import os

LOCAL_PATH = os.getenv("LOCAL_PATH", os.getcwd())
# Ensure LOCAL_PATH doesn't end with a slash for consistent concatenation
LOCAL_PATH = LOCAL_PATH.rstrip("/")

BASE_DIR = os.path.join(LOCAL_PATH, "site/src/content/authors")

def format():
    # For all files in all authors' directories
    if len(sys.argv) == 1:
        dir = BASE_DIR

    # For all files in a specified author's directory
    elif len(sys.argv) == 2:
        dir = f"{BASE_DIR}/{sys.argv[1]}"
    
    # For a single file in a specified author's directory
    elif len(sys.argv) == 3:
        dir = f"{BASE_DIR}/{sys.argv[1]}/{sys.argv[2]}"
    
    else:
        print("Usage: python trim_footer.py [author] [work]")
        sys.exit(1)
        
    for root, dirs, files in os.walk(dir):
        for file in files:
            trim_footer_out(f"{os.path.join(root, file)}")

def trim_footer_out(file):
    with open(file, "r") as f:
        content = f.read()
        print(f"Processing {file}")
        content = content.replace("Literatura.us Mapa | Quiénes Somos | Aviso Legal | Contactar", "")
        content = content.replace("""Literatura
.us
Mapa de la biblioteca | Aviso Legal | Quiénes Somos | Contactar""", "")
        with open(file, "w") as f:
            f.write(content)
    
if __name__ == "__main__":
    format()