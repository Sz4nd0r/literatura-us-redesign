---
name: semantic-formatter
version: 1.0
scope: workspace
summary: >
  Workflow for converting markdown files to a semantic format for web publishing.
description: |
  This skill provides a step-by-step workflow for transforming markdown files into a semantic structure suitable for static site generation (e.g., 11ty). It ensures that text is structured with proper markdown tags reflecting the meaning and context of each sentence, without altering or adding content.

workflow:
  - Identify markdown files in site/src/content/authors/ and subdirectories.
  - For each file:
      1. Review the text and segment it by meaning (citations, quotes, titles, headings, subheadings, references, emphasis, paragraphs, lists, etc.).
      2. Apply appropriate markdown syntax to each segment, reflecting its semantic role.
      3. Do not add, remove, or modify the original text content—only change structure/formatting.
      4. If a file is already well-structured, omit it from changes.
  - Output: Modified markdown files with semantic structure, ready for web rendering.

criteria:
  - No extra explanations or content changes.
  - Semantic tags must match the meaning/context of the text.
  - Output must be compatible with 11ty and CSS styling.
  - Omit files that do not require changes.

examples:
  - "Format all markdown files in site/src/content/authors/ to use semantic markdown tags."
  - "Review and semantically structure the works of Borges for web publishing."
  - "Skip files that are already well-structured."

related:
  - Consider a skill for batch auditing or reporting which files were changed or skipped.
  - Consider a skill for previewing the semantic output before saving changes.
