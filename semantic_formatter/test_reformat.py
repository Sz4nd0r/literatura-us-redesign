import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from reformat_author import get_author_metadata, reformat_file

author_dir = '/home/szortofbad/projects/literatura-us-2.0/site/src/content/authors/augusto'
author_info, work_map = get_author_metadata(author_dir)
print(f"Author: {author_info}")
# print(f"Work Map: {work_map}")

test_file = os.path.join(author_dir, 'baldio.md')
new_content = reformat_file(test_file, author_info, work_map)
if new_content:
    print("--- NEW CONTENT START ---")
    print("\n".join(new_content.split('\n')[:20]))
    print("...")
    print("\n".join(new_content.split('\n')[-10:]))
    print("--- NEW CONTENT END ---")
else:
    print("Failed to reformat.")
