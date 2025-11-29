# Claude Code Playbook: Legacy Code Modernisation

Your starter kit for transforming undocumented VB.NET applications into modern web services. For Claude Code basics, see [Getting Started](../getting-started-claude-code.md).

---

## Challenge-specific CLAUDE.md

Copy this into your project's CLAUDE.md before you start. It captures what you will discover about the legacy system.

```markdown
## Project: PQ Tracker Modernisation

Modernising a VB.NET Parliamentary Question tracking system to a modern web application.

### Legacy analysis approach
- Understand before rebuilding - never generate modern code until you can explain the legacy behaviour
- Map every form, button, and event handler before writing replacements
- Document business rules in plain English as you discover them
- Test legacy behaviour manually to verify your understanding

### Known business rules (PQ Tracker)
**Deadline calculations:**
- Answer deadline = tabled date + 5 working days (Monday-Friday only)
- No bank holiday handling in legacy system - working days are simply Mon-Fri
- DaysRemaining is calculated on display, not stored

**Reference format:**
- Pattern: PQ-YYYY-NNNNN (e.g., PQ-2024-00042)
- Year from tabled date, number auto-increments per year
- Leading zeros padded to 5 digits

**Status workflow:**
- Valid statuses: Draft, Tabled, Answered, Withdrawn
- No validation on transitions - any status can change to any other
- Status changes not timestamped in legacy

### Data structure (CSV storage)
- Single CSV file: pq_data.csv
- Fields: Reference, TabledDate, Question, Minister, Status, AnswerDate, Answer
- Dates stored as dd/MM/yyyy
- Commas in Question/Answer fields may break parsing (legacy bug)

### Modernisation constraints
- Preserve ALL functionality - users must be able to do everything they could before
- Match existing workflows exactly before adding improvements
- Data migration must handle malformed CSV records gracefully
- Do not assume business rules - verify against legacy code
```

---

## Custom slash commands

Save these files in `.claude/commands/` for systematic legacy analysis.

### `.claude/commands/analyze-legacy.md`

```markdown
---
description: Systematic analysis of legacy VB.NET code
---

Analyse the legacy VB.NET code in $ARGUMENTS. Work through these phases:

**Phase 1: Structure mapping**
- List all forms, modules, and classes
- Identify entry points and main navigation flow
- Document file dependencies and references

**Phase 2: Business logic extraction**
- Find calculations (especially date arithmetic)
- Identify validation rules and constraints
- Map status values and allowed transitions
- Document reference number generation logic

**Phase 3: Data handling**
- How is data persisted? (files, database, registry)
- What is the data format and schema?
- How are dates and numbers formatted?
- What happens with special characters?

**Phase 4: User interactions**
- What actions can users take on each form?
- What triggers save/load operations?
- How are errors communicated to users?

Output a structured report with:
1. Component inventory (forms, modules, classes)
2. Business rules in plain English
3. Data model diagram or description
4. Risks and edge cases discovered
5. Questions that need manual testing to answer
```

### `.claude/commands/verify-parity.md`

```markdown
---
description: Check modern implementation matches legacy behaviour
---

Compare the modern implementation against legacy behaviour for $ARGUMENTS.

**Functional parity checklist:**
- Does creating a new PQ generate the correct reference format?
- Does deadline calculation match legacy (tabled date + 5 working days, Mon-Fri only)?
- Can users perform all status transitions that legacy allowed?
- Does data display match legacy field-for-field?

**Data handling parity:**
- Can the modern system read all existing CSV records?
- Are dates parsed correctly from dd/MM/yyyy format?
- How does it handle commas embedded in text fields?
- Are empty vs null values handled consistently?

**Edge case verification:**
- PQ tabled on Friday: deadline should be following Friday
- PQ tabled on weekend: how does legacy handle this?
- DaysRemaining when deadline has passed (negative values?)
- Reference number rollover at year boundary

**Report format:**
For each check, state:
- Expected behaviour (from legacy analysis)
- Actual behaviour (from modern implementation)
- PASS/FAIL/UNTESTED
- Fix required if FAIL
```

---

## Model recommendations

| Task | Model | Why |
|------|-------|-----|
| Initial legacy analysis | Opus | Complex reasoning needed to understand undocumented code |
| Business rule extraction | Opus | Must infer intent from implementation details |
| Data model design | Opus | Needs to handle legacy quirks and plan migration |
| API endpoint implementation | Sonnet | Standard patterns once requirements are clear |
| UI component building | Sonnet | Straightforward once behaviour is defined |
| Parity verification | Opus | Catches subtle differences in business logic |
| Test case generation | Sonnet | Mechanical once edge cases are identified |

**Switch with `/model`** - use Opus for analysis and complex reasoning, Sonnet for implementation.

---

## Effective prompts for this challenge

**Business rule extraction:**
> "Analyse the btnSave_Click event handler in frmPQEntry.vb. Extract every business rule - validation, calculations, data transformations. For each rule, explain: what triggers it, what it checks or calculates, what happens when it fails. Pay special attention to date calculations and reference number generation."

**Data model translation:**
> "Based on the CSV structure in the legacy PQ tracker, design a modern data model. The CSV has: Reference, TabledDate, Question, Minister, Status, AnswerDate, Answer. Consider: What should be separate tables? What constraints should exist? How will you handle the calculated DaysRemaining field? Show the schema with explanations for each design decision."

**Test case generation:**
> "Generate test cases for the working day deadline calculation. The legacy rule is: deadline = tabled date + 5 working days (Monday-Friday). Include: PQs tabled each day of the week, PQs tabled on weekends, PQs where the 5-day span crosses month/year boundaries. For each test case, show the input date and expected deadline date."

**Migration verification:**
> "Create a verification script that compares legacy CSV data against the modern database after migration. For each record, check: reference matches exactly, dates converted correctly, text fields preserved including any special characters, status values mapped correctly. Report any discrepancies with details."

**UI-to-API mapping:**
> "Map the user interactions in frmPQList.vb to REST API endpoints. For each button/action in the form, specify: the HTTP method, endpoint path, request body, response format, and any business logic that should happen server-side vs client-side. Include the DataGridView operations for sorting and filtering."

---

## Tips and gotchas

### Working day calculation

| Issue | What to do |
|-------|------------|
| Off-by-one errors | The legacy adds 5 working days, not 5 days - Monday + 5 working days = following Monday, not Saturday |
| Weekend handling | If tabled on Saturday/Sunday, legacy may behave unexpectedly - test manually |
| No bank holidays | Legacy ignores bank holidays entirely - do not add them unless explicitly required |
| Day counting | Day 1 is the day after tabling, not the tabling day itself |

### Null vs empty string handling

| Issue | What to do |
|-------|------------|
| AnswerDate when unanswered | Legacy may store empty string, your database wants NULL - decide and be consistent |
| Empty Question field | Legacy allows it, should your modern system? Preserve behaviour first |
| Whitespace | Legacy may store leading/trailing spaces - trim on migration or preserve? |

### CSV parsing fragility

| Issue | What to do |
|-------|------------|
| Commas in text fields | Legacy may not quote fields properly - Question text with commas corrupts data |
| Line breaks in answers | Multi-line answers may split CSV records |
| Character encoding | Legacy likely uses Windows-1252, not UTF-8 - watch for corrupted characters |
| Empty trailing fields | Some CSV parsers drop empty fields at end of line |

### Calculated fields

| Issue | What to do |
|-------|------------|
| DaysRemaining not stored | This is calculated from deadline and current date - do not look for it in storage |
| Display vs storage | The grid shows calculated values but only base data persists |
| Negative days | When deadline passes, DaysRemaining goes negative - does legacy show this? |

### Status workflow

| Issue | What to do |
|-------|------------|
| No transition rules | Legacy allows any status to change to any other - chaotic but preserve it |
| Withdrawn from any state | Users may withdraw Draft, Tabled, or even Answered PQs |
| No audit trail | Legacy does not track when status changed or by whom |

---

## Reflection questions

After completing the challenge, consider:

- How much time did you spend understanding versus building? Was the ratio right?
- What business rules did you discover that were not obvious from the code structure?
- Where did the AI tool help most - finding patterns, explaining logic, or generating code?
- What would you do differently if modernising a larger legacy system?
- How confident are you that no functionality was lost in translation?
- What documentation would help the next person maintain your modern version?
