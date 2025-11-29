# Kiro Playbook: Complex Business Logic Implementation

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for building a rules engine that implements Carbon Reduction Plan assessments.

## Mode recommendation: Spec Mode

Use Spec Mode for this challenge. Here is why:

- Weighted scoring must be documented before implementation - stakeholders need to verify the methodology
- Threshold-based rules have interdependencies - specs expose these relationships before they become bugs
- Audit trail requirements demand traceability from policy to code
- Government procurement decisions need defensible documentation of how rules were implemented

Vibe Mode works for exploring individual rule patterns, but switch to Spec Mode once you start implementing the scoring engine.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this system does
Carbon Reduction Plan (CRP) assessment engine. Evaluates supplier environmental
compliance for government contracts under Procurement Policy Note 06/21.

## Who uses this system
- **Procurement officers**: assess incoming CRP submissions
- **Policy admins**: configure scoring weights and thresholds
- **Auditors**: review decision trails and verify consistency
- **Suppliers**: understand why their submission received a particular score

## Scoring methodology
Four assessment categories with fixed weights:
- Baseline measurement: 25% (emissions data quality)
- Reduction targets: 30% (Net Zero alignment)
- Action plan credibility: 25% (intervention feasibility)
- Governance: 20% (board commitment and accountability)

## Decision transparency requirements
Every score must include:
- Which rules applied and why
- How each category score was calculated
- What thresholds triggered special conditions
- What would change the outcome (actionable feedback)
```

### tech.md

```markdown
# Technical Standards

## Rules engine architecture
- Separate rule definitions from execution engine
- Rules stored as data, not hardcoded in business logic
- Rule metadata includes: effective date, version, category, weight
- Engine evaluates rules in defined order with short-circuit capability

## Scoring methodology implementation
- Weighted average calculation: sum(category_score * weight) / sum(weights)
- Category scores normalised to 0-100 scale before weighting
- Missing data handling: exclude category from calculation, flag incomplete
- Partial scores: calculate with available data, clearly mark limitations

## Threshold patterns
- All thresholds configurable via policy configuration
- Threshold definitions include: boundary value, operator, consequence
- Organisation size thresholds: turnover > 5M, employees > 500, employees > 1000
- Sector risk thresholds: high-risk industries require additional criteria

## Audit trail design
- Every rule evaluation logged with: rule ID, input values, outcome, timestamp
- Decision chains show which rules led to final score
- Policy version captured at assessment time (immutable snapshot)
- Explanation generator creates human-readable reasoning

## Conditional logic patterns
- Use explicit rule chaining, not nested if statements
- Document rule interactions in dependency graph
- Handle mutual exclusions (if A then not B)
- Support conditional compliance (pass with conditions)
```

## Agent for this challenge

Save this in `.kiro/agents/rules-engine-expert.md`.

```markdown
# Rules Engine Expert Agent

You are a business rules specialist who designs transparent, auditable scoring systems.

## Your expertise
- Weighted scoring methodologies and normalisation
- Threshold-based decision logic with configurable boundaries
- Rule dependency management and evaluation order

## When designing scoring logic
- Verify weights sum to expected total (usually 100%)
- Check threshold boundaries for gaps and overlaps
- Identify rule interactions that could produce unexpected results

## When reviewing implementations
- Trace every score back to source rules
- Verify missing data does not crash calculations
- Confirm audit trail captures enough detail to reconstruct decisions
```

## Hook for this challenge

Save this in `.kiro/hooks/scoring-validator.yaml`.

```yaml
name: scoring-validator
event: file_saved
match: "**/*{rule,score,assess,weight,threshold}*.{js,ts,py,cs}"
prompt: |
  Check this scoring logic implementation for common errors:
  - Do weights sum to 100% (or document why not)?
  - Are threshold boundaries clear (is 500 employees "over 500" or "500 or more")?
  - Can missing data cause division by zero or null reference?
  - Is the rule evaluation order deterministic?
  - Are audit trail entries created for each rule evaluation?
  Report any gaps that could cause inconsistent scoring.
```

## Effective spec prompts

Use these prompts to guide Kiro through your rules engine development.

### Requirements for weighted scoring system

> Create requirements for the weighted scoring system covering: how the four categories (baseline 25%, targets 30%, action plan 25%, governance 20%) combine into a final score; how missing data affects calculation; what thresholds determine pass, conditional pass, and fail. Include acceptance criteria verifying scores are reproducible.

### Design spec for threshold-based rules

> Design the threshold-based rule system. Cover: how organisation size thresholds trigger additional rules; how sector risk affects which rules apply; how conditional compliance works; how rule conflicts are resolved. Show how policy admins configure thresholds without code changes.

### Task breakdown for rules engine core

> Break the rules engine into implementation tasks. For each: what it implements, inputs and outputs, edge cases to handle, how to verify correctness. Order tasks so foundational scoring comes before threshold variations.

### Audit trail and explanation system

> Design the audit and explanation system. Include: what to capture for each rule evaluation; how to generate human-readable explanations; how to show what would change the outcome; how to handle policy version changes. Output must satisfy auditors months later.

## Gotchas specific to rules engines

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Weights do not sum to 100% | Individual weights edited without checking total | Add validation that rejects weight configurations not summing to 100% |
| Threshold boundaries unclear | "Over 500" vs "500 or more" interpreted differently | Document boundary operators explicitly: >, >=, <, <= |
| Rule order affects outcome | Later rules override earlier rules unexpectedly | Design rules to be order-independent or document explicit precedence |
| Missing data crashes scoring | Division by zero when category has no applicable rules | Handle missing data explicitly: skip category, use default, or flag incomplete |
| Policy changes break audits | Old decisions no longer reproducible with new rules | Snapshot policy version at assessment time; store with decision record |

## Quality checkpoints

### Scoring logic
- [ ] Weights sum to 100% (or intentional deviation documented)
- [ ] Category scores normalised consistently (all 0-100)
- [ ] Missing data handled without crashes or silent failures
- [ ] Final score reproducible given same inputs

### Threshold configuration
- [ ] All thresholds configurable without code changes
- [ ] Boundary operators explicit (>, >=, <, <=)
- [ ] Overlapping thresholds have defined resolution

### Audit completeness
- [ ] Every rule evaluation logged with inputs and outcome
- [ ] Policy version captured at assessment time
- [ ] Human-readable explanation generated for each decision
- [ ] Actionable feedback shows what would change outcome

### Rule interdependencies
- [ ] Rule interactions documented in dependency graph
- [ ] Conditional compliance criteria clear
- [ ] Circular dependencies impossible or detected

### Policy versioning
- [ ] Old assessments reproducible with historical policy
- [ ] Policy changes tracked with effective dates

## Reflection questions

When you finish, consider:

- Could two procurement officers get different scores for the same submission?
- If a policy changes next month, how much of your code needs updating?
- Can an auditor understand why a specific supplier received their score?
- What happens if a supplier submits data for only two of the four categories?
