# Level 10: Production Deployment and Incident Response

This playbook helps you create operations documentation tailored to YOUR service - the government application you built in Levels 1-5. Generic DevOps templates fail because they don't understand your specific citizen journeys, data flows, and compliance requirements.

Your application serves citizens who depend on it. Operations documentation must reflect that responsibility.

## CLAUDE.md Configuration

Add this snippet to your project's CLAUDE.md file. Replace placeholders with your actual service details.

```markdown
## Operations Context

### Service Identity
- Service name: [Your service from Levels 1-5]
- Primary citizen journey: [What citizens come here to do]
- Peak usage patterns: [When citizens use this most]
- Data sensitivity: [What personal data you handle]

### Deployment Constraints
- Zero-downtime deployments required - citizens cannot see error pages
- Database migrations must be backward-compatible with previous version
- All deployments require audit trail for compliance review
- Rollback capability mandatory within 5 minutes of deployment
- Feature flags control new functionality exposure

### Incident Priorities
- P1: Citizens cannot complete primary journey (payment, application submission)
- P2: Citizens experience degraded service (slow response, partial failures)
- P3: Internal systems affected, citizen-facing service operational

### Monitoring Endpoints
- Health check: /health (returns service status)
- Readiness: /ready (returns dependency status)
- Metrics: /metrics (Prometheus format)
- Citizen journey completion: tracked via [your analytics approach]
```

## Custom Slash Commands

Create these files in your `.claude/commands/` directory.

### /project:ops-analysis

**File:** `.claude/commands/ops-analysis.md`

```markdown
Analyse this service for production readiness. Focus on three areas:

## Deployment Readiness
Review the codebase and identify:
- Database migration approach - are migrations backward-compatible?
- Configuration management - how do environment variables flow?
- Dependency health checks - what external services does this need?
- Deployment artifacts - what gets built and how?

## Failure Mode Analysis
Examine each citizen-facing endpoint and answer:
- What happens when the database is unavailable?
- What happens when an external API times out?
- What happens when a citizen submits invalid data?
- What partial failure states could occur mid-transaction?

## Compliance Checkpoints
Check the codebase for:
- Audit logging of citizen data access
- Personal data handling in error messages and logs
- Session management and timeout behaviour
- Data retention and deletion capability

Provide specific findings with file paths and line numbers. Recommend concrete changes, not general principles.
```

### /project:incident-runbook

**File:** `.claude/commands/incident-runbook.md`

```markdown
Generate an incident runbook for this service. Base all content on actual code, not assumptions.

## Detection
From the codebase, identify:
- What health checks exist and what they verify
- What metrics are exposed and what thresholds matter
- What log patterns indicate problems
- What citizen-facing symptoms appear first

## Diagnosis
Create decision trees based on actual error handling:
- Map error codes to their source in the codebase
- Trace each API endpoint's failure paths
- Document database query patterns that could fail
- List external service dependencies and their failure modes

## Remediation
For each failure mode identified, document:
- Immediate actions to restore service
- Commands to verify the fix worked
- Citizen communication triggers
- Escalation criteria

## Post-Incident
Define requirements for:
- Timeline reconstruction from available logs
- Citizen impact assessment approach
- Root cause categories relevant to this service
- Prevention measures to consider

Output as a structured runbook with copy-paste commands where applicable.
```

## Model Selection

| Task | Recommended Model | Why |
|------|-------------------|-----|
| Failure mode analysis | Opus | Traces complex paths through actual code, identifies subtle interaction failures |
| Incident runbook generation | Opus | Produces comprehensive, specific procedures from codebase analysis |
| Deployment pipeline configuration | Sonnet | Generates correct YAML/config quickly, handles standard patterns well |
| Monitoring query creation | Sonnet | Writes Prometheus queries and dashboard configs efficiently |
| Quick ops questions | Sonnet | Answers deployment questions without deep analysis overhead |

Use Opus when you need to understand how your specific code fails. Use Sonnet when you need to generate standard configuration.

## Effective Prompts

### 1. Deployment Pipeline Design

```
Design a deployment pipeline for this GOV.UK service. Requirements:
- Zero-downtime deployment using [your platform]
- Database migrations run before new code deploys
- Automated rollback if health checks fail within 5 minutes
- Audit log entry for each deployment with deployer identity
- Smoke tests verify citizen journey completion

Review the current codebase structure and produce pipeline configuration that works with these specific files and dependencies.
```

### 2. Citizen Journey Monitoring

```
Create a monitoring strategy for citizen journeys in this service. Analyse the codebase to identify:

1. Journey entry points and completion endpoints
2. Steps where citizens most likely abandon (form submissions, payment, file uploads)
3. External dependencies that could block completion
4. Data points we can capture without storing personal information

Produce Prometheus metrics definitions and Grafana dashboard JSON that tracks journey completion rates, step-by-step drop-off, and time-to-completion percentiles.
```

### 3. Failure Scenario Runbook

```
Generate a runbook for this specific failure scenario: [describe scenario]

Trace through the actual codebase to document:
- Exact log messages that appear when this fails
- Database state that results from partial completion
- API responses citizens see
- Recovery steps with actual commands for this codebase
- Verification that service is restored

Include file paths for all referenced code so on-call engineers can investigate quickly.
```

### 4. Peak Demand Preparation

```
This service experiences peak demand during [time period, e.g., tax deadline, school admissions].

Analyse the codebase and identify:
- Database queries that scale poorly with concurrent users
- API endpoints with expensive operations
- Session storage approach and its limits
- External service rate limits that could throttle us

Recommend specific code changes, caching strategies, and infrastructure scaling that addresses these bottlenecks. Include load test scenarios that verify improvements.
```

### 5. Compliance-as-Code

```
Review this codebase for compliance requirements and generate automated checks.

For GDPR / UK data protection:
- Identify all personal data fields and their storage locations
- Check logging statements for accidental PII exposure
- Verify deletion capability exists for each data type
- Document data retention periods in code comments or configuration

For accessibility:
- Check error messages are screen-reader friendly
- Verify timeout warnings give adequate notice
- Ensure form validation provides clear guidance

Output as automated test cases that run in CI/CD pipeline.
```

## Tips and Gotchas

| Tip | Why It Matters |
|-----|----------------|
| Trace failures through actual code paths | Generic runbooks say "check the database" - useful runbooks say "run this query against this table to find stuck transactions" |
| Generate runbooks from code, not documentation | Documentation drifts from reality; code shows what actually happens when things fail |
| Test rollback procedures before you need them | First time you run a rollback should not be during a P1 incident at 3am |
| Include compliance context in incident response | A data breach has different response requirements than a performance degradation |
| Model citizen behaviour during incidents | Citizens refresh pages, retry submissions, contact support - your incident response must account for this amplification |

## Reflection Questions

After generating operations documentation, verify quality by answering:

### 1. Failure Mode Coverage

Look at your runbooks and cross-reference with the codebase:
- Have you documented what happens when each external dependency fails?
- Do your runbooks cover partial transaction failures, not just complete outages?
- Can an on-call engineer who has never seen this code follow your procedures?

### 2. Runbook Specificity

Review the commands and procedures in your runbooks:
- Do they reference actual file paths, table names, and endpoint URLs from this codebase?
- Can someone copy-paste the commands without modification?
- Do decision trees lead to specific actions, not "investigate further"?

### 3. Compliance Integration

Check that compliance is embedded in operations, not bolted on:
- Do incident severity levels account for data protection implications?
- Does your deployment pipeline enforce audit requirements automatically?
- Can you demonstrate compliance through logs and metrics, not just policy documents?

---

## Quick Reference

**Before deploying:** Run `/project:ops-analysis` to verify readiness

**Before on-call rotation:** Generate runbooks with `/project:incident-runbook`

**During incident:** Use Opus to trace failures through actual code paths

**After incident:** Document what the runbook missed and update it

Your operations documentation is only as good as your last incident. Update it continuously.
