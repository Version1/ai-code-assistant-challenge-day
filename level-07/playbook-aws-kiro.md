# Kiro Playbook: Performance Investigation and System Resilience

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for investigating a performance incident and designing monitoring that protects citizens from future outages.

## Mode recommendation: Hybrid approach

Use both modes for this challenge, but at different stages.

**Vibe Mode for investigation**: When you are correlating logs, testing hypotheses, and hunting for the root cause. Investigation is exploratory - you do not know what you will find until you find it. Vibe Mode lets you pivot quickly as evidence points in new directions.

**Spec Mode for monitoring design**: Once you know what went wrong, switch to Spec Mode to design the monitoring architecture. Monitoring systems need documented requirements, clear thresholds, and traceable decisions about what to alert on.

The investigation produces evidence. The spec produces a defensible monitoring design.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this system does
Council booking service that went down during a peak period. You are investigating
what caused the outage and designing monitoring to prevent recurrence.

## Citizen impact considerations
When this service fails, citizens cannot book community facilities. Vulnerable
users who depend on these services are disproportionately affected - they may
lack alternatives or flexibility to return later.

## Stakeholders
- **Incident commander**: needs clear timeline of what happened and why
- **Operations team**: needs actionable monitoring they can implement
- **Service owner**: needs confidence this will not happen again
- **Citizens**: need the service to work when they need it

## Success criteria
- Root cause identified with supporting evidence (not just symptoms)
- Timeline showing how the incident developed
- Monitoring design that would detect this before citizens notice
- Recommendations that prevent this class of problem
```

### tech.md

```markdown
# Technical Standards

## Log correlation methodology
- Align timestamps across all sources before analysis
- Look for events that precede symptoms, not just correlate with them
- Question obvious explanations - surface symptoms often mislead

## Evidence hierarchy
1. Timestamped events that precede the incident
2. Metrics showing gradual degradation before failure
3. Patterns that explain the cascade of symptoms
4. Correlation does not equal causation - verify the mechanism

## Root cause investigation patterns
- Work backwards from symptoms to triggers
- Check what changed before the incident started
- Look for the first anomaly, not the loudest one
- Distinguish between cause, contributing factors, and symptoms

## Monitoring architecture standards (four golden signals)
- **Latency**: time to serve requests (track percentiles, not averages)
- **Traffic**: demand on the system (requests per second)
- **Errors**: rate of failed requests
- **Saturation**: how full the system is (queue depths, connection pools)

## Alerting principles
- Alert on symptoms that affect citizens, not just internal metrics
- Set thresholds based on evidence, not guesswork
- Avoid alert fatigue - fewer meaningful alerts beat many ignored ones
- Include runbook links in alerts so responders know what to do
```

## Agent for this challenge

Save this in `.kiro/agents/incident-investigator.md`.

```markdown
# Incident Investigator Agent

You are an SRE specialist who finds root causes, not just symptoms.

## Your expertise
- Log correlation across multiple data sources
- Distinguishing symptoms from causes
- Identifying the cascade that led to visible failure
- Designing monitoring that catches problems early

## When investigating incidents
- Start with timestamps - what happened first?
- Question the obvious explanation - it is often wrong
- Look for what changed before symptoms appeared
- Check for gradual build-up that was not noticed

## Red flags in analysis
- Jumping to scaling solutions before understanding the cause
- Treating correlated events as causation
- Missing the first anomaly because later symptoms are louder
- Confirmation bias - only seeing evidence that supports initial theory
```

## Hook for this challenge

Save this in `.kiro/hooks/analysis-validator.yaml`.

```yaml
name: analysis-validator
event: file_saved
match: "**/*{analysis,investigation,findings,timeline}*.md"
prompt: |
  Check this incident analysis for completeness:
  - Is the root cause distinct from symptoms?
  - Are timestamps aligned across all evidence sources?
  - Does the timeline show what happened BEFORE visible symptoms?
  - Is there evidence showing the mechanism, not just correlation?
  - Are alternative explanations considered and ruled out?
  Flag any gaps that would weaken the investigation findings.
```

## Effective spec prompts

Use these prompts to guide Kiro through your investigation and monitoring design.

### Timeline reconstruction

> Analyse the logs and metrics to build a timeline of this incident. Start from 8:00 AM (before symptoms appeared) and identify: the first anomaly, when symptoms became visible, when citizens were affected, and how the incident cascaded. Align timestamps across all sources before correlating events.

### Root cause analysis spec

> Create requirements for validating the root cause. Cover: what evidence confirms the cause (not just correlates); what alternative explanations must be ruled out; how to verify the mechanism that led to failure. The root cause must explain all observed symptoms.

### Monitoring architecture design

> Design a monitoring system based on the four golden signals. Cover: what specific metrics to track; threshold values based on evidence from this incident; which alerts would have fired before citizens noticed; how to avoid alert fatigue. Include runbook outlines for each alert.

### Citizen impact assessment

> Analyse the citizen impact data alongside the technical timeline. Cover: when citizens first experienced problems versus when systems showed symptoms; how long different user journeys were affected; what the blast radius was. Use this to set monitoring thresholds that protect citizens.

## Gotchas specific to performance investigation

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Treating symptoms as root cause | Database connection exhaustion is visible; its trigger is not | Ask "what caused this to happen?" until you reach something that changed |
| Timestamp misalignment | Different systems log in different timezones or formats | Normalise all timestamps to UTC before correlating events |
| Confirmation bias | First theory feels right so you stop looking | Actively seek evidence that contradicts your theory |
| Missing gradual build-up | Focus on the crash misses the slow degradation | Check metrics from hours before the incident for trends |
| Over-alerting in response | Fear of recurrence leads to alerts on everything | Base thresholds on evidence; test that alerts are actionable |

## Quality checkpoints

### Investigation phase

- [ ] Timestamps aligned across all data sources
- [ ] Timeline starts before symptoms appeared
- [ ] First anomaly identified (not just loudest symptom)
- [ ] Alternative explanations considered and ruled out
- [ ] Mechanism explained (not just correlation)

### Root cause validation

- [ ] Root cause explains all observed symptoms
- [ ] Evidence shows what changed before the incident
- [ ] Cause is distinct from symptoms
- [ ] Contributing factors identified separately

### Monitoring design

- [ ] Four golden signals covered appropriately
- [ ] Thresholds based on evidence from this incident
- [ ] Alerts would fire before citizen impact
- [ ] Alert volume manageable (not alert fatigue)
- [ ] Runbooks outline response actions

### Deliverable quality

- [ ] Another team could implement this monitoring
- [ ] Investigation method documented for reuse
- [ ] Recommendations prevent this class of problem
- [ ] Findings defensible if challenged

## Reflection questions

When you finish, consider:

- Did the AI help you find patterns you would have missed manually?
- How long did investigation take versus how long it would take without AI assistance?
- Could your monitoring design be applied to other council services?
- What assumptions did you make that turned out to be wrong?
- Would your investigation method work for a different type of incident?
