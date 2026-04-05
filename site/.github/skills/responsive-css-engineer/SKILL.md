---
name: responsive-css-engineer
description: |
  **WORKFLOW SKILL** — Style responsive webpages following a predefined structure and pattern. Identify areas for improvement, suggest and implement modern, DRY, and readable CSS solutions. Follow best practices for maintainable, scalable, and accessible front-end code.
version: 1.0.0
---

# Responsive CSS Engineer Skill

## Purpose

Enable agents (or users) to:

- Style webpages responsively using modern CSS (Flexbox, Grid, media queries, custom properties, etc.)
- Follow a consistent, maintainable structure and naming convention
- Identify and suggest improvements for code clarity, DRYness, and accessibility
- Apply best practices for cross-browser support and performance

## Workflow

_You are also encouraged to leverage established CSS frameworks (such as Tailwind, Bootstrap, etc.) where appropriate. Use these tools in a complementary way, taking advantage of their best features to accelerate development, ensure consistency, and enhance maintainability. Always combine framework utilities with custom CSS thoughtfully, choosing the best solution for each scenario._

1. **Analyze Structure**: Review the HTML/templating structure and existing CSS for layout, semantics, and patterns.
2. **Identify Improvements**: Spot areas for DRYing up, modernizing, or making more accessible/responsive.
3. **Propose Changes**: Suggest improvements, refactors, or new patterns (with rationale).
4. **Implement**: Apply changes using modern, supported CSS (Flexbox, Grid, custom properties, etc.).
5. **Validate**: Check for responsiveness, accessibility, and code clarity. Ensure no regressions.
6. **Document**: Briefly document new patterns or conventions introduced.

## Decision Points

- Use CSS frameworks (e.g., Tailwind, Bootstrap) when they provide a clear benefit, but do not force-fit them where custom CSS is more suitable
- Combine framework utilities and custom CSS for optimal results
- Use CSS custom properties for theme/consistency if repeated values are found
- Prefer utility classes for repeated patterns, but avoid excessive class proliferation
- Use semantic HTML and ARIA where appropriate
- Always check for mobile-first responsiveness
- Avoid vendor prefixes unless absolutely necessary (use Autoprefixer if build allows)

## Quality Criteria

- Layout adapts smoothly to all screen sizes
- Code is DRY, readable, and well-organized
- Accessibility is not regressed (color contrast, focus, semantics)
- No unnecessary specificity or !important usage
- Follows BEM or project’s preferred naming convention

## Completion Checklist

- [ ] Responsive at all breakpoints
- [ ] No duplicated or dead CSS
- [ ] Modern layout techniques used
- [ ] Accessibility checked
- [ ] Code is commented where non-obvious
- [ ] Patterns/conventions documented

## Example Prompts

- "Make this page fully responsive and DRY up the CSS."
- "Suggest improvements for our CSS structure and implement them."
- "Refactor this layout to use CSS Grid and document the pattern."
- "Audit our CSS for accessibility and responsiveness."

## Related Customizations

- CSS utility class generator
- Accessibility audit skill
- HTML semantic structure skill
