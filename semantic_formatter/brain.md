# Semantic Formatter for markdown files

## Goal

Convert markdown files to a semantic format that can be used to generate a website.

## How it works

For each markdown with a row block of text:

1. You should structure the text by identifying the meaning of the sentences.
2. Identify citations; quotes; titles; headings; subheadings; references; emphasis; paragraphs; lists; etc. by the context and the meaning of the sentences.
3. Format the text in markdown using the appropriate tags (syntax).


## Rules

* Do not add any extra text or explanation nor remove or modify existing text.
* Have in mind that the text is going to be rendered in a website with css styles using 11ty.

## Contents

The markdown files are located in the `site/src/content/authors/` directory that consist of subdirectories for each author. Each author directory contains the markdown files for the works of that author. Please ommit the `site/src/content/authors/acs` directory, as it has already been processed (you can use it as an example of what you can do but not limited to what you can do).


## Output

For each markdown file, you should create a new markdown file with the same name but with the semantic format. The new markdown file should be located in the same directory as the original markdown file. Or simply modify the content of the original markdown file.