# Claude Code Playbook: Complex Business Logic Implementation

Your starter kit for building a Carbon Reduction Plan rules engine. For Claude Code basics, see [Getting Started](../getting-started-claude-code.md).

---

## Challenge-specific CLAUDE.md

Copy this into your project's CLAUDE.md before you start.

```markdown
## Project: Carbon Reduction Plan Assessment Engine

A rules engine that evaluates supplier environmental compliance for government contracts.

### Scoring methodology
Four weighted categories that must total 100%:
- Baseline measurement: 25% (historical emissions data quality)
- Reduction targets: 30% (science-based Net Zero alignment)
- Action plan credibility: 25% (realistic, measurable interventions)
- Governance: 20% (board commitment and accountability)

Use integer weights (25, 30, 25, 20) not floats (0.25, 0.30) - sum to 100, divide at end.

### Threshold definitions (OR logic applies)
Enhanced verification required if:
- Turnover exceeds 5 million pounds OR
- Employees exceed 500

Science-based targets mandatory if:
- Employees exceed 500 OR
- High-risk sector (aviation, shipping, steel)

Dedicated Net Zero governance role required if:
- Employees exceed 1000

### Conditional logic patterns
Rules interact - order of evaluation matters:
1. IF Scope 3 emissions > 40% of total AND no supplier engagement programme THEN fail governance
2. IF science-based targets not aligned BUT SBTi validation committed within 12 months THEN conditional pass
3. IF baseline data incomplete BUT third-party verification committed THEN apply reduced scoring (50% weight)

### Audit trail requirements
Every decision must record:
- Rule evaluated (with version identifier)
- Input values used
- Threshold applied and whether met
- Score contribution (before and after weighting)
- Timestamp and data source reference
```

---

## Custom slash commands

Save these files in `.claude/commands/`.

### `.claude/commands/test-rule.md`

```markdown
---
description: Test individual scoring rules with sample data
---

Test the scoring rule for $ARGUMENTS with these checks:

**Boundary behaviour:**
- Value exactly at threshold (e.g., exactly 500 employees)
- Value one unit below threshold
- Value one unit above threshold

**Edge cases:**
- Null or missing input value
- Zero value

**Conditional interactions:**
- Does this rule depend on other rules' outputs?
- What happens if a dependent rule returns null?
- Are OR conditions evaluated correctly (any true = true)?

**Output verification:**
- Score is within valid range (0-100 or 0-weight)
- Audit trail entry is complete
- Reasoning text is human-readable

Report: input, expected output, actual output, PASS/FAIL for each test.
```

### `.claude/commands/validate-policy.md`

```markdown
---
description: Full compliance check against policy requirements
---

Run a complete policy validation for $ARGUMENTS (organisation data or test scenario).

**Category scoring (must sum to 100):**
- Baseline measurement rules (25%): data completeness, verification standards, boundary definitions
- Reduction target rules (30%): science-based alignment, timeframe validation, scope coverage
- Action plan rules (25%): intervention specificity, investment validation, timeline feasibility
- Governance rules (20%): board commitment, reporting requirements, supply chain engagement

**Threshold verification:**
- Identify which thresholds apply based on turnover, employees, and sector
- Verify OR logic is applied correctly (any threshold breach triggers requirement)
- Check conditional rules in correct order

**Audit trail check:**
- Every rule evaluation has complete audit entry
- Decision chain is traceable from input to final score

**Report format:**
1. Organisation profile and thresholds triggered
2. Score by category with rule-by-rule breakdown
3. Overall compliance status (Pass/Conditional/Fail)
4. Complete audit trail
```

---

## Model recommendations

| Task | Model | Why |
|------|-------|-----|
| Rules engine architecture | Opus | Complex interdependencies need careful design |
| Threshold logic with OR conditions | Opus | Boolean logic errors are subtle and costly |
| Individual rule implementation | Sonnet | Straightforward once design is clear |
| Unit test creation | Sonnet | Mechanical once edge cases are defined |
| Edge case hunting | Opus | Finding gaps requires adversarial thinking |

**Switch with `/model`** - use Opus for architecture and complex logic, Sonnet for implementation.

---

## Effective prompts for this challenge

**Architecture design:**
> "Design a rules engine architecture for Carbon Reduction Plan assessment. It must: evaluate four weighted categories, apply threshold-based rules that vary by organisation size, handle conditional logic where rules interact, and generate complete audit trails. Show how rules are registered, how evaluation order is determined, and how scores are aggregated. Explain your design decisions."

**Threshold implementation with OR logic:**
> "Implement threshold checking for enhanced verification requirements. The rule is: required if turnover exceeds 5 million pounds OR employees exceed 500. This is OR logic - either condition triggers the requirement. Handle: exactly-at-threshold values, missing data for one field, missing data for both fields. Include audit trail entries showing which condition triggered."

**Scoring with interdependencies:**
> "Implement the governance scoring rule: IF Scope 3 emissions exceed 40% of total AND no supplier engagement programme exists THEN fail governance. This depends on baseline emissions data being calculated first. Show: how to ensure baseline runs before governance, how to pass data between rules, what happens if baseline calculation failed or returned null, complete audit trail."

**Audit trail generation:**
> "Create an audit trail system for the rules engine. Each entry must record: rule identifier with version, all input values used, threshold applied and result, score contribution, timestamp. The trail must be queryable to explain any decision. Design for legal defensibility - someone challenging a procurement decision will read this."

**Edge case hunting:**
> "Review the rules engine for edge cases that could produce incorrect or unexplainable results. Consider: null propagation through scoring calculations, circular dependencies between rules, boundary values at thresholds, organisations that meet multiple conditional rules, partial data where some fields are missing. For each edge case, explain the risk and recommend handling."

---

## Tips and gotchas

### Floating point weights

| Issue | What to do |
|-------|------------|
| Rounding errors | Use integers (25, 30, 25, 20) and divide by 100 at the end |
| Weights not summing to 100 | Validate on engine initialisation, fail fast if wrong |
| Percentage display | Calculate from raw score, do not store pre-weighted values |

### OR vs AND in thresholds

| Issue | What to do |
|-------|------------|
| Confusing OR conditions | "Turnover > 5m OR employees > 500" means either triggers - test both separately |
| AND in conditionals | "Scope 3 > 40% AND no programme" means both must be true to fail |
| Missing data in OR | If one condition is true and other is null, result is true (any true = true) |
| Missing data in AND | If one condition is null, result may be indeterminate - decide and document |

### Circular dependencies

| Issue | What to do |
|-------|------------|
| Rule A needs Rule B which needs Rule A | Detect cycles during engine initialisation |
| Implicit dependencies | Governance depends on baseline totals - make dependencies explicit |
| Evaluation order | Sort rules topologically by dependencies before running |

### Null propagation

| Issue | What to do |
|-------|------------|
| Score + null = ? | Decide: null, zero, or error? Document clearly |
| Null in weighted average | Exclude nulls and re-weight, or fail the category? |
| Audit trail for nulls | Always record that a value was null, not silently skip |

### Threshold boundary behaviour

| Issue | What to do |
|-------|------------|
| Exactly 500 employees | "Exceeds 500" means > 500, so 500 exactly does not trigger |
| Text says "over" or "more than" | Both mean > not >= unless policy says otherwise |
| Boundary tests | Always test: threshold - 1, threshold exactly, threshold + 1 |

---

## Reflection questions

After completing the challenge, consider:

- How did you ensure rules are evaluated in the correct order when they depend on each other?
- What happens to the overall score when one category cannot be calculated?
- Could someone challenge a decision using only the audit trail? What would they need?
- How would you add a new threshold rule without breaking existing ones?
- Where did the AI tool help most - understanding policy, designing architecture, or finding edge cases?
