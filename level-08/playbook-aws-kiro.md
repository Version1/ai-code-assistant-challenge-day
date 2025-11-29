# Kiro Playbook: Adaptive Testing Strategy and Risk-Based Quality Engineering

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for testing a government service the way real citizens will use it.

## Mode recommendation: Spec Mode

Use Spec Mode for this challenge. Here is why:

- Risk-based testing needs documented rationale - stakeholders must understand why certain scenarios receive more attention
- EARS-format requirements create clear acceptance criteria that prove coverage
- Traceability from risk assessment to test implementation satisfies audit requirements
- Accessibility testing decisions need defensible documentation
- Test priorities based on citizen impact require explicit justification

Vibe Mode works for exploring individual failure scenarios. Switch to Spec Mode once you start building your test suite.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this system does
Validates a citizen-facing government service built in Level 1, 2, or 3.
Testing must explore how real citizens experience the service.

## Who we are protecting
- Citizens under deadline pressure (benefit applications, eviction notices)
- Users with accessibility needs (screen readers, limited motor control)
- People on older devices with poor connectivity
- Those who cannot afford service failures

## Quality goals
- Zero critical failures in citizen journeys
- WCAG 2.1 AA compliance across all interactive elements
- Graceful degradation under poor network conditions
- Clear error recovery paths for all failure modes
```

### tech.md

```markdown
# Technical Standards

## Test frameworks
- Playwright or Cypress for end-to-end journey testing
- axe-core for automated accessibility validation
- Lighthouse for performance auditing under constraints

## Testing approaches
- Risk-based test selection: prioritise by citizen impact
- Condition simulation: test under degraded circumstances
- Failure mode injection: verify recovery paths work

## Environment simulation
- 3G throttling for mobile users on limited data
- Offline mode transitions for unstable connections
- Session timeout handling for interrupted journeys
- Viewport testing for older mobile devices
```

## Agent for this challenge

Save this in `.kiro/agents/risk-analyzer.md`.

```markdown
# Risk Analyzer Agent

You analyse features for failure modes and score risks by citizen impact.

## Your expertise
- Identifying how government services fail for vulnerable users
- Scoring risks by likelihood and consequence to citizens
- Mapping feature dependencies to failure cascades
- Recognising accessibility barriers before they affect users

## When analysing features
- Ask "What happens if this fails for someone facing eviction?"
- Consider users who cannot retry or wait for fixes
- Check for assumptions about device capability or connectivity
- Identify single points of failure in citizen journeys

## Risk scoring approach
- **Critical**: Blocks citizen from completing essential task
- **High**: Causes significant confusion or requires workaround
- **Medium**: Degrades experience but allows completion
- **Low**: Minor inconvenience with obvious recovery

## Red flags in service design
- Features that assume reliable internet throughout
- Error messages that require technical knowledge to understand
- Forms that lose data on timeout or back-button
- Accessibility implemented as afterthought
```

## Hook for this challenge

Save this in `.kiro/hooks/test-coverage-validator.yaml`.

```yaml
name: test-coverage-validator
event: file_saved
match: "**/*.{spec,test}.{js,ts}"
prompt: |
  Check this test file for citizen-focused coverage:
  - Does it test accessibility with axe-core or equivalent?
  - Does it simulate poor network conditions (3G, offline)?
  - Does it verify error recovery paths work?
  - Does it test with keyboard-only navigation?
  - Does it check timeout handling for interrupted sessions?
  Flag missing coverage areas critical to government services.
```

## Effective spec prompts

Use these prompts to guide Kiro through your testing strategy development.

### Risk-based prioritisation matrix

> Create a risk prioritisation matrix for my government service. For each feature: identify failure modes; score by likelihood and citizen impact; determine which user groups face highest stakes; recommend test depth based on risk score. Prioritise features where failure causes irreversible harm to vulnerable citizens.

### Accessibility test suite

> Design accessibility testing requirements covering: WCAG 2.1 AA criteria relevant to my service; automated checks using axe-core; manual verification scenarios for screen readers; keyboard-only navigation paths; focus management during form interactions. Include acceptance criteria that prove compliance, not just absence of errors.

### Environmental resilience testing

> Create requirements for testing under degraded conditions. Cover: form completion on 3G-throttled connections; session recovery after network interruption; behaviour when JavaScript fails to load; timeout handling for users who step away mid-task. Define what graceful degradation looks like for each scenario.

### Failure mode analysis

> Analyse my service for citizen-critical failure modes. For each identified failure: what triggers it; who is affected most severely; what the user experiences; what recovery path exists; how to test that recovery works. Focus on failures that prevent citizens from completing essential tasks.

## Gotchas specific to Kiro testing workflows

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Spec scope creep | Risk analysis expands to cover every possible scenario | Constrain specs to top 10 risks by citizen impact; defer lower-risk items to backlog |
| Hook over-triggering | Test file hook fires on every save, slowing workflow | Use specific file patterns; batch validation rather than per-save checks |
| Steering file conflicts | Product goals and tech constraints create contradictory requirements | Review steering files together; resolve conflicts before starting specs |
| Agent hallucination on WCAG | AI invents accessibility criteria that do not exist in standards | Always verify WCAG references against official documentation; use axe-core rules as source of truth |
| Task granularity mismatch | Specs generate tasks too large to complete or too small to be meaningful | Request tasks completable in 30-60 minutes; split or combine as needed during implementation |

## Quality checkpoints

### Risk assessment phase

- [ ] All citizen journeys mapped for your chosen service
- [ ] Failure modes identified for each journey step
- [ ] Risks scored by likelihood and citizen impact
- [ ] High-stakes user groups explicitly identified
- [ ] Test priorities justified by risk scores

### Accessibility coverage

- [ ] WCAG 2.1 AA criteria mapped to service features
- [ ] Automated axe-core checks implemented
- [ ] Screen reader testing scenarios documented
- [ ] Keyboard navigation paths verified
- [ ] Focus management tested during interactions

### Environmental testing

- [ ] 3G throttling tests for form submissions
- [ ] Offline transition handling verified
- [ ] Session timeout recovery tested
- [ ] Graceful degradation defined and verified
- [ ] Error messages understandable without technical knowledge

### Failure recovery

- [ ] Critical failure modes have documented recovery paths
- [ ] Recovery paths tested and working
- [ ] Error states do not lose user progress
- [ ] Back-button and refresh behaviour tested
- [ ] Timeout warnings give users time to respond

### Deliverable quality

- [ ] Tests could be run by another team member
- [ ] Risk rationale documented for audit purposes
- [ ] Test coverage traceable to identified risks
- [ ] Results show pass/fail against acceptance criteria

## Reflection questions

When you finish, consider:

- Did risk-based prioritisation focus your testing on what matters most?
- Which citizen groups did your initial design overlook?
- What failures did you discover that you would not have found with generic testing?
- Could your testing approach be applied to other government services?
- What assumptions about users did testing reveal were wrong?
