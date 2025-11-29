# Kiro Playbook: Legacy Code Modernisation

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for modernising undocumented VB.NET systems.

## Mode recommendation: Spec Mode

Use Spec Mode for this challenge. Here is why:

- Hidden business rules need documentation before transformation - you cannot modernise what you do not understand
- Zero business logic loss is a hard constraint - specs create audit trails proving parity
- Government working day calculations are implicit in legacy code - they need explicit requirements
- Stakeholders need documented evidence that nothing was lost in translation

Vibe Mode works for exploring the legacy codebase initially, but switch to Spec Mode once you start extracting business rules.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this system does
Parliamentary Question (PQ) tracking system. Monitors questions from MPs,
calculates response deadlines, and manages the workflow from receipt to answer.

## Critical constraint
Zero business logic loss. Every calculation, validation, and workflow rule in
the legacy system must exist in the modern version. Missing a deadline rule
could cause ministerial embarrassment.

## Core domain concepts
- **PQ Types**: Named Day (specific answer date), Ordinary Written (working days deadline)
- **Status workflow**: Draft > In Progress > With Minister > Answered
- **Working days**: Excludes weekends and bank holidays - affects all deadline calculations
- **Reference numbers**: Format varies by PQ type and must be preserved exactly

## Business rules extracted from legacy
Document each rule you extract here. Example format:
- Ordinary Written PQs: deadline = tabling date + 5 working days (excludes weekends, bank holidays)
- Named Day PQs: deadline = date specified by MP
- Status can only move forward in workflow (no regression without admin override)
- Reference format: PQ-[TYPE]-[YEAR]-[SEQUENCE] (e.g., PQ-OW-2024-00123)
```

### tech.md

```markdown
# Technical Standards

## Source system (legacy)
- VB.NET Windows Forms application
- CSV file storage (no database)
- Business logic embedded in form event handlers
- No separation of concerns
- Mixed naming conventions throughout

## Target system (modern)
- Web application (framework of your choice)
- Proper separation: UI, business logic, data access
- Works on mobile and desktop
- Accessible to screen reader users
- Runs on any operating system

## Migration requirements
- Data format: plan how CSV data maps to modern storage
- Reference number continuity: existing numbers must remain valid
- Parallel running: design for side-by-side verification

## Code quality standards
- Business rules in dedicated service layer (not controllers or UI)
- Working day calculations in reusable utility (not scattered)
- All date handling explicit about time zones
- Comprehensive error messages for validation failures

## Legacy code smells to address
- DateTime.Nothing vs DBNull.Value handling (VB.NET quirk)
- Case-insensitive string comparisons hidden in legacy
- Comma handling in CSV fields (quoted strings)
- Implicit type conversions throughout
```

## Agent for this challenge

Save this in `.kiro/agents/` to get help extracting legacy business rules.

### legacy-analyzer.md

```markdown
# Legacy Analyzer Agent

You are a VB.NET specialist who extracts business rules from undocumented code.

## Your expertise
- Reading VB.NET Windows Forms applications
- Identifying business logic hidden in event handlers
- Understanding VB.NET quirks (Nothing vs DBNull, implicit conversions)
- Documenting rules in plain English

## When analysing legacy code
- Look for calculations in Button_Click handlers
- Check Form_Load for initialisation rules
- Find validation in TextChanged and Validating events
- Trace workflow through status field changes
- Identify hardcoded values that represent business rules

## Output format
For each rule you find, document:
1. What the rule does (plain English)
2. Where you found it (file and method)
3. Edge cases the code handles
4. Assumptions that are implicit (not documented)
```

## Hook for this challenge

Save this in `.kiro/hooks/` to verify your modern code matches legacy behaviour.

### parity-check.yaml

```yaml
name: parity-check
event: file_saved
match: "**/*.{js,ts,cs,py}"
prompt: |
  Check this business logic implementation against legacy requirements:
  - Working day calculations exclude weekends AND bank holidays
  - Date comparisons handle null/empty values correctly
  - String comparisons are case-insensitive where legacy was
  - Status transitions follow the defined workflow
  - Reference number format matches legacy pattern exactly
  Report any deviations that could cause different behaviour.
```

## Effective spec prompts

Use these prompts to guide Kiro through your modernisation.

### Initial business logic extraction

> I need to understand this legacy VB.NET PQ tracking system before modernising it. Please analyse the codebase and document:
>
> - What data entities exist (look at the CSV structure and form fields)
> - What business rules govern PQ deadlines (look for date calculations)
> - What workflow states exist and how PQs move between them
> - What validation rules are enforced (look for error messages and checks)
>
> For each rule, tell me where you found it and what assumptions are implicit.

### Design spec for architecture

> Based on the business rules we extracted, design the modern application architecture:
>
> - How to structure the codebase (separation of concerns)
> - Where business rules will live (isolated and testable)
> - How to handle working day calculations (reusable utility)
> - What the data model looks like compared to the CSV structure
>
> For each design decision, explain how it preserves the legacy behaviour.

### Task decomposition with parity focus

> Break the modernisation into implementation tasks. For each task:
>
> - What legacy behaviour it replaces
> - How we will verify parity (specific test cases)
> - What edge cases from the legacy code must be covered
>
> Order tasks so we can verify parity incrementally - do not leave testing until the end.

### Data migration planning

> Design the data migration from CSV to our modern storage:
>
> - Field mapping from CSV columns to new schema
> - Data transformation rules (date formats, status values)
> - Validation checks to run after migration
> - Rollback strategy if migration fails
>
> Include specific test cases to verify no data is lost or corrupted.

## Gotchas specific to legacy modernisation

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Working days calculated wrong | Legacy includes bank holidays implicitly; modern version uses calendar days | Ask Kiro to find ALL date arithmetic and list what days are excluded |
| DateTime Nothing crashes | VB.NET Nothing differs from DBNull.Value; modern nulls behave differently | Document null handling before writing any date logic |
| Search finds wrong records | Legacy search was case-insensitive; modern defaults to case-sensitive | Check every string comparison in legacy for .ToLower() or Option Compare |
| CSV import corrupts data | Commas inside fields need quote handling; legacy code may have workarounds | Test import with real legacy data containing commas |
| Status workflow breaks | Implicit rules about who can change status and when | Map every status transition in legacy before building workflow |

## Quality checkpoints

### Business logic extraction

- [ ] All date calculations documented with working day rules
- [ ] Status workflow mapped with all valid transitions
- [ ] Reference number format captured with examples
- [ ] Validation rules listed with error messages
- [ ] Implicit assumptions made explicit

### Design parity

- [ ] Every legacy entity has a modern equivalent
- [ ] Business rules isolated in testable components
- [ ] Working day calculation handles bank holidays
- [ ] Null handling matches legacy behaviour
- [ ] String comparisons match legacy case sensitivity

### Implementation testing

- [ ] Test cases exist for each extracted business rule
- [ ] Edge cases from legacy code covered
- [ ] Working day calculations verified against known dates
- [ ] Status transitions tested for all valid paths
- [ ] Reference number generation matches legacy format

### Data migration

- [ ] CSV import handles quoted fields correctly
- [ ] All legacy records migrate without errors
- [ ] Dates convert correctly (check edge cases)
- [ ] No data truncation or corruption
- [ ] Migrated data passes validation rules

### User workflow

- [ ] Users can complete all tasks from legacy system
- [ ] Same data entry produces same results
- [ ] Error messages help users fix problems
- [ ] Mobile and desktop both work
- [ ] Screen reader users can complete tasks

## Reflection questions

When you finish, consider:

- How many business rules did you find that were not obvious from reading the code?
- Which VB.NET quirks caused bugs in your first modern implementation?
- Did the spec-driven approach help you achieve feature parity, or did you find gaps late?
- How confident are you that working day calculations match the legacy system exactly?
- What would you add to your steering files for the next legacy modernisation?
- If you ran both systems side by side, would they produce identical outputs?
