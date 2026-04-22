# Semantic Formatting Plan for WF Author Directory

This plan outlines the systematic approach to format William Faulkner's 88 files according to semantic formatting rules, with careful chunking for large works.

## File Analysis Results

**WF Directory Structure:**
- 88 total files (88,049 bytes total)
- 5 small reference files (cruz.md, index.md, jjoyce.md, sa.md, vw.md)
- 83 story files ranging from 10KB to 884KB
- **Critical large files requiring chunking:**
  - wf_abs.md (884KB) - Absalom, Absalom!
  - wf_absalom.md (768KB) - Another major novel
  - wf_sound.md (570KB) - The Sound and the Fury
  - wf_gambito.md (220KB), wf_villo.md (222KB), wf_hogar.md (177KB)

## Current Formatting State

**Well-structured files (minimal work needed):**
- index.md - Already has proper headings, lists, emphasis
- Most files already have basic frontmatter and author attribution

**Common formatting opportunities identified:**
- Long paragraphs need breaking into semantic chunks
- Dialogue needs proper quote formatting
- Chapter/section headings need h2/h3 markup
- Internal thoughts/monologues need italic emphasis
- Citations and references need blockquote formatting

## Chunking Strategy

**Phase 1: Small Files (5-10KB each)**
- Process 15-20 small files in batches
- Focus on dialogue, emphasis, and paragraph structure

**Phase 2: Medium Files (20-80KB each)**
- Process in groups of 5-8 files
- Identify and format chapter breaks, character dialogue

**Phase 3: Large Files (100KB+)**
- wf_abs.md: Break into ~10 sections by chapter (I, II, III, etc.)
- wf_absalom.md: Similar chapter-based approach
- wf_sound.md: Multiple narrator sections need careful formatting

## Semantic Formatting Priorities

1. **Dialogue & Quotes**: Convert to proper markdown quote syntax
2. **Chapter Headers**: Format numbered sections as h2 headings
3. **Character Monologues**: Italicize internal thoughts
4. **Literary References**: Use blockquotes for citations
5. **Paragraph Structure**: Break overly long paragraphs logically
6. **Lists**: Convert any enumerated sequences to markdown lists

## Implementation Approach

**Per-file workflow:**
1. Read and analyze current structure
2. Identify semantic elements needing formatting
3. Apply changes incrementally (no content addition/removal)
4. Validate formatting preserves original meaning

**Quality checks:**
- Ensure no h1/# headers added
- Verify all original text preserved
- Check semantic accuracy of applied formatting

## Ready to Begin

Starting with Phase 1 small files to establish workflow patterns before tackling the large novels. The chunking approach ensures manageable, high-quality semantic formatting for this substantial collection.
