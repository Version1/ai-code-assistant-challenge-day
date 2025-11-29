# Claude Code Playbook: PDF to Digital Service

Your starter kit for this challenge. For Claude Code basics, see [Getting Started](../getting-started-claude-code.md).

---

## Challenge-specific CLAUDE.md

Copy this into your project's CLAUDE.md before you start. It saves you repeating requirements in every prompt.

```markdown
## Project: PDF Form to GOV.UK Digital Service

Transform a PDF form into an accessible digital service.

### Technical requirements
- GOV.UK Design System components (govuk-frontend)
- HTML-first, then progressive enhancement with JavaScript
- WCAG 2.2 AA compliance throughout
- Nunjucks templates (or plain HTML if no build pipeline)

### GOV.UK patterns to follow
- One question per page
- Error summary at page top, inline errors below fields
- "Check your answers" before submission
- Clear confirmation page with reference number
- Start page explaining the service

### Accessibility non-negotiables
- All form inputs have visible labels (not placeholder-only)
- Error messages linked via aria-describedby
- Focus management after errors and page transitions
- Conditional reveals use GOV.UK pattern with proper aria
- Works without CSS and JavaScript

### Content standards
- User-friendly labels (not technical field names from PDF)
- Hint text for any field that needs explanation
- Error messages say what went wrong AND how to fix it
- Plain English throughout
```

---

## Custom slash commands

Drop these files in `.claude/commands/` to reuse them throughout the challenge.

### `.claude/commands/accessibility-check.md`

```markdown
---
description: Check accessibility against WCAG 2.2 AA and GOV.UK requirements
---

Run an accessibility review on $ARGUMENTS. Check against these specific criteria:

**WCAG 2.2 AA requirements:**
- All interactive elements are keyboard accessible
- Focus indicators are visible
- Form inputs have programmatically associated labels
- Error messages are linked to inputs via aria-describedby
- Colour contrast meets 4.5:1 for text, 3:1 for UI components
- Content is readable at 200% zoom

**GOV.UK Design System compliance:**
- Error summary present at page top with anchor links to errors
- Conditional reveals use the correct pattern
- Hint text associated with inputs correctly
- Fieldsets and legends used appropriately for grouped inputs

**Progressive enhancement:**
- Core functionality works without JavaScript
- Forms submit and validate server-side

Report issues with:
1. What the problem is
2. Which WCAG criterion or GOV.UK guideline it violates
3. How to fix it
```

### `.claude/commands/govuk-review.md`

```markdown
---
description: Review code against GOV.UK Design System patterns
---

Review $ARGUMENTS for GOV.UK Design System compliance.

Check:
- Component usage matches the Design System exactly
- Class names follow govuk- prefix convention
- HTML structure matches documented patterns
- Form validation follows the error message pattern
- Page flow follows one question per page

For any deviation, explain:
1. What pattern should be used instead
2. Where to find the correct pattern in the Design System
3. The specific changes needed
```

---

## Model recommendations

| Task | Model | Why |
|------|-------|-----|
| Initial PDF extraction | Sonnet | Fast, accurate for structured data |
| Standard form generation | Sonnet | Handles GOV.UK patterns well |
| Complex conditional logic | Opus | Better at multi-step validation flows |
| Accessibility audit | Opus | More thorough, catches subtle issues |
| Quick iterations | Sonnet | Faster feedback loop |

**Switch models with `/model`** - use Sonnet for most work, Opus when you need depth.

---

## Effective prompts for this challenge

**Extracting from the PDF:**
> "Read [form.pdf] and extract every field. For each field, identify: the label text, whether it's required, any validation constraints, and which GOV.UK component maps to it."

**Generating the service:**
> "Create a multi-page GOV.UK form service based on this field mapping. Follow one question per page. Group related fields logically. Include a start page, check your answers, and confirmation page."

**Fixing accessibility issues:**
> "Review this form against WCAG 2.2 AA. For each issue you find, show me the current code, explain the problem, and provide the corrected code."

**Getting proper error handling:**
> "Add validation with GOV.UK error handling. I need: error summary at page top with anchor links, inline error messages below each field, aria-describedby linking, and focus moved to error summary on submission."

**Forcing progressive enhancement:**
> "Refactor this to work without JavaScript. The form must submit and validate server-side. Add JavaScript enhancement only after the HTML works independently."

---

## Tips that save time

**Start with the PDF directly.** Claude Code reads PDFs natively. Drop it in your project and ask for a structured extraction before generating any code.

**Set accessibility expectations in your first prompt.** Adding "ensure WCAG 2.2 AA" from the start is far easier than retrofitting accessibility later.

**Ask for HTML-first.** Claude defaults to JavaScript-heavy solutions. Be explicit about progressive enhancement or you'll get forms that break without JS.

---

## Watch out for

| Issue | What to do |
|-------|------------|
| Missing error summary | Request explicitly - Claude often forgets the summary at page top |
| Placeholder-only labels | Ask for visible labels above inputs, hint text separate |
| Broken conditional reveals | Specify "GOV.UK conditional reveal pattern with proper aria" |
| JavaScript-dependent validation | Request server-side validation first, JS enhancement second |
| Technical field names | Ask for "user-friendly labels following GOV.UK content guidelines" |

---

## Reflection questions

After completing the challenge, consider:

- Where did Claude need more context to produce useful output?
- What accessibility issues did you catch (or miss) in review?
- How much of the generated code could you use directly versus needing fixes?
- What would you add to CLAUDE.md for a similar project?
- Did the custom commands save time? What others would help?
