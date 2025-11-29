# Level 5: Complex Business Logic Implementation

**Build an intelligent rules engine that automates government policy decisions**

## What you'll build

A Carbon Reduction Plan assessment system that evaluates supplier environmental compliance for government contracts.

This system must:

- implement complex policy rules with interdependent criteria
- score applications transparently with clear justifications
- handle edge cases and incomplete data gracefully
- adapt quickly when policy changes
- generate audit trails that can withstand legal scrutiny

## Why this matters

Government departments evaluate thousands of Carbon Reduction Plans each year under Procurement Policy Note 06/21. Currently, this happens manually - and it's causing real problems.

**Inconsistent decisions** - different teams interpret the same policy differently, creating unfair outcomes and legal risk.

**Slow processing** - manual assessment creates bottlenecks that delay procurement.

**Scattered guidance** - policy rules live across multiple documents, making consistent application nearly impossible.

**High stakes errors** - wrong decisions expose government to procurement challenges and undermine Net Zero commitments.

**The opportunity**: AI tools can transform complex policy documents into consistent, auditable, explainable decision systems.

## The policy you'll implement

Carbon Reduction Plan assessment requires evaluating four interconnected areas:

| Category | Weight | What you're assessing |
|----------|--------|----------------------|
| Baseline measurement | 25% | Historical emissions data quality and completeness |
| Reduction targets | 30% | Whether targets align with science-based Net Zero pathways |
| Action plan credibility | 25% | How realistic and measurable the proposed interventions are |
| Governance | 20% | Board commitment and accountability structures |

### The complexity: threshold-based rules

Different rules apply depending on organisation size:

- **Over 5 million pounds turnover**: requires enhanced verification
- **Over 500 employees**: must align with science-based targets
- **Over 1000 employees**: needs dedicated Net Zero governance role
- **High-risk sectors** (aviation, shipping, steel): additional criteria apply

### The complexity: conditional logic

Rules interact with each other:

- If Scope 3 emissions exceed 40% of total AND no supplier engagement programme exists, the application fails governance requirements
- If science-based targets aren't aligned BUT the organisation commits to SBTi validation within 12 months, conditional compliance is acceptable
- If historical data is incomplete BUT third-party verification is committed, reduced baseline scoring applies

## What success looks like

### Your rules engine must deliver

**Correct policy implementation** - rules accurately reflect current environmental policy requirements.

**Transparent scoring** - every decision includes clear reasoning that civil servants can explain and defend.

**Robust edge case handling** - incomplete applications and exceptional circumstances don't break the system.

**Rapid adaptability** - policy changes can be incorporated without rebuilding the system.

**Complete audit trails** - full decision history with reasoning chains for accountability.

**Efficient processing** - handles high-volume government procurement workloads.

### Government-specific requirements

**Legal defensibility** - decisions must withstand procurement challenge procedures.

**Cross-departmental consistency** - the same application should receive the same assessment regardless of which team processes it.

**Regulatory update integration** - mechanisms for incorporating new environmental regulations as they emerge.

## Source materials

Your implementation should reference:

- **Procurement Policy Note 06/21**: Taking account of Carbon Reduction Plans in major government contracts
- **Environmental Reporting Guidelines**: HM Treasury greenhouse gas reporting requirements
- **Net Zero Strategy**: UK Government decarbonisation plan
- **Science Based Targets Initiative**: International framework for corporate emissions reduction

## Approaches to consider

### Prompt-driven development

Use AI tools to systematically transform policy documents into executable business rules.

**Works well when**: business stakeholders need to understand and validate rule logic quickly.

### Spec-driven development

Create executable specifications for the rules engine, following structured phases with formal sign-off.

**Works well when**: formal policy implementation requiring approval, or complex regulatory compliance requirements.

### Hybrid approach

Combine both: use prompt-driven development for rapid policy decomposition, spec-driven for formal architecture and validation.

## Assessment criteria

| Area | Weight | What we're looking for |
|------|--------|----------------------|
| Baseline measurement rules | 25% | Correct implementation of data completeness, verification standards, boundary definitions |
| Reduction target rules | 30% | Science-based alignment, timeframe validation, scope coverage, trajectory credibility |
| Action plan rules | 25% | Intervention specificity, investment validation, timeline feasibility, technology assessment |
| Governance rules | 20% | Board commitment, organisational structure, reporting requirements, supply chain engagement |

All rules must correctly implement threshold-based variations and conditional logic interactions.

## What to do next

1. Review the policy documents to understand the assessment criteria
2. Choose your development approach
3. Design your rules engine architecture
4. Implement the business logic with full test coverage
5. Validate against edge cases and exceptional circumstances
