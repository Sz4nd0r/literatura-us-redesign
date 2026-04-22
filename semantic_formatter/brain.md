# Semantic Formatter for markdown files

## Goal

Modify markdown files to a semantic format that can be used to generate a website with semantic html tags and a clear structure.

## How it works

For each markdown with a row block of text:

1. You should structure the text by identifying the meaning of the sentences.
2. Identify citations; quotes; titles; headings; subheadings; references; emphasis; paragraphs; lists; etc. by the context and the meaning of the sentences.
3. Format the text in markdown using the appropriate tags (syntax).


## Rules

* Do not add any extra text or explanation nor remove or modify existing text.
* Have in mind that the text is going to be rendered in a website with css styles using 11ty.
* Ommit the file if it has a clear structure and does not need any modification.
* Do not add h1 or # elements as they are already present in the website by "title: <title>".

## Contents

The markdown files are located in the `site/src/content/authors/` directory that consist of subdirectories for each author. Each author directory contains the markdown files for the works of that author.


## Output

For each markdown file, you should modify the content of the original markdown file changing it's structure to a semantic format that can be used to generate a website with semantic html tags and a clear structure.