# Kiro Playbook: PDF to Digital Service

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for this specific challenge.

## Mode recommendation: Spec Mode

Use Spec Mode for this challenge. Here is why:

- Government services need documented rationale for design decisions
- Accessibility requirements need traceability from standard to implementation
- The one-thing-per-page pattern requires deliberate task breakdown
- You will want the audit trail when reviewing against WCAG criteria

Vibe Mode works for quick fixes during implementation, but start with Spec Mode for your form structure.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory and adapt for your chosen PDF.

### product.md

```markdown
# Product Context

## What this service does
Replaces a PDF form with an accessible digital service that captures [FORM PURPOSE].
Citizens can complete and submit their application online without downloading,
printing, or posting paper forms.

## Who uses this service
- Citizens applying for [SERVICE]
- Users of assistive technologies (screen readers, voice control, switch devices)
- Users on mobile devices with limited connectivity
- Users with low digital confidence

## Service standards
This service must meet:
- GOV.UK Service Standard (all 14 points)
- WCAG 2.2 Level AA
- Public Sector Bodies Accessibility Regulations 2018

## Design principles
- One thing per page: each screen asks one question or makes one decision
- Progressive disclosure: only show what users need right now
- Error prevention over error messages: design to prevent mistakes
- Progressive enhancement: core functionality works without JavaScript
```

### tech.md

```markdown
# Technical Standards

## Frontend
- GOV.UK Frontend 5.x
- Nunjucks templating
- No client-side frameworks (React, Vue, etc.)
- Progressive enhancement: all forms work without JavaScript

## Form patterns (mandatory)
- Use GOV.UK date input (3 separate fields) - never native date pickers
- Error summary at page top AND inline errors on fields
- Focus management: errors move focus to summary
- Radios and checkboxes use GOV.UK components, not native inputs

## Accessibility requirements
- All form inputs have visible labels (no placeholder-only labels)
- Error messages identify the field and describe how to fix the problem
- Conditional reveals work with keyboard and screen readers
- Heading hierarchy is logical (h1 > h2 > h3, no skipped levels)
- Link text describes destination (no "click here")

## URLs
- GOV.UK Design System: https://design-system.service.gov.uk
- GOV.UK Frontend: https://frontend.design-system.service.gov.uk
- WCAG 2.2: https://www.w3.org/WAI/WCAG22/quickref/
```

## Hooks for this challenge

Save these in `.kiro/hooks/` to catch common problems automatically.

### accessibility-check.yaml

```yaml
name: accessibility-check
event: file_saved
match: "**/*.njk"
prompt: |
  Review this template for accessibility issues:
  - Form inputs without associated labels
  - Missing aria-describedby for error messages
  - Placeholder text used instead of labels
  - Images without alt text
  - Heading hierarchy problems (skipped levels)
  - Links with non-descriptive text ("click here", "read more")
  Report issues with line numbers and suggested fixes.
```

### govuk-patterns.yaml

```yaml
name: govuk-patterns
event: file_saved
match: "**/*.njk"
prompt: |
  Check this template follows GOV.UK patterns:
  - Uses govukInput, govukRadios, govukCheckboxes (not native HTML)
  - Date fields use three separate inputs (day/month/year)
  - Error summary exists if there are inline errors
  - Page has exactly one h1 matching the fieldset legend or label
  - Back link uses GOV.UK component
  Flag any deviations with the correct pattern to use.
```

## Starting your spec

These prompts help you get a useful requirements document. Adapt them for your PDF.

### Opening prompt

> I am transforming [PDF NAME] into a GOV.UK digital service. The PDF collects [BRIEF DESCRIPTION OF DATA]. I need to create an accessible online form that follows GOV.UK Design System patterns and meets WCAG 2.2 AA.
>
> The service needs: a start page, one-thing-per-page question flow, check your answers page, and confirmation page.
>
> Please create a spec for this service. Focus on the question flow first - we need to break the PDF into logical screens that each ask one thing.

### Follow-up prompt for question flow

> Looking at the PDF, the data captured includes: [LIST FIELDS FROM PDF].
>
> Group these into a logical question flow. Consider: what does the user need to know first? What questions depend on earlier answers? What can we skip based on conditional logic?
>
> For each screen, specify: the question, the input type (text/radio/checkbox/date), any validation rules, and the error message if validation fails.

### Prompt for accessibility requirements

> Add explicit accessibility acceptance criteria to each requirement. Each screen must specify:
> - The exact error message text (must identify field and explain how to fix)
> - Keyboard interaction behaviour
> - Screen reader announcements for dynamic content
> - Focus management after errors

## Gotchas specific to this challenge

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Questions in wrong order | PDF field order is not user-logical order | Map the user journey before mapping PDF fields |
| Missing error summary | Kiro adds inline errors but forgets the summary | Add "error summary component required" to every form screen requirement |
| Too many questions per page | Kiro groups related fields together | Specify "one question per page" in product.md and repeat in requirements |
| Wrong date picker | Native HTML date inputs are inaccessible | Explicitly require "GOV.UK date input pattern (three separate fields)" |
| Conditional reveals break | Complex show/hide logic fails for keyboard users | Add "test with keyboard only" to acceptance criteria |
| Labels inside inputs | Placeholder-as-label pattern is common but inaccessible | Require "visible label above input" for every field |

## Quality checkpoints

Before considering your service complete, verify:

**Structure**
- [ ] Start page explains what users need before they begin
- [ ] Each form page asks exactly one question (or one closely related set)
- [ ] Check your answers page shows all captured data
- [ ] Confirmation page provides reference number and next steps

**Accessibility**
- [ ] Every input has a visible label
- [ ] Error summary appears at top of page and lists all errors
- [ ] Each error message identifies the field and explains the fix
- [ ] Tab order is logical (top to bottom, left to right)
- [ ] Service works with JavaScript disabled

**GOV.UK compliance**
- [ ] All form components use GOV.UK Frontend (not native HTML)
- [ ] Dates use three-field pattern
- [ ] Back links appear on every page except start page
- [ ] Page titles follow pattern: "Question - Service name - GOV.UK"

## Reflection questions

When you finish, consider:

- How did the spec-driven approach affect your accessibility compliance?
- Which gotchas caught you despite reading these tips?
- Did Kiro's generated requirements miss anything from the PDF?
- How much manual review did the one-thing-per-page pattern require?
- What would you add to your steering files for the next form you digitise?
