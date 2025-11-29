# Kiro Playbook: Production Deployment and Incident Response

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for creating service-specific DevOps for a government application you built in Levels 1-5.

This is operational design tailored to your service. Generic templates will not pass.

## Mode recommendation: Spec Mode

Use Spec Mode throughout this challenge. Here is why:

- Deployment procedures need documented rationale - auditors must understand why you chose specific rollback windows
- Runbook accuracy depends on traceable links between failure modes and response steps
- Compliance validation requires explicit documentation of what checks run and when
- Change management demands defensible records showing deployments followed approved processes
- Knowledge transfer fails without documentation that operators can actually follow

Vibe Mode works for exploring individual failure scenarios. Switch to Spec Mode once you start documenting your deployment pipeline.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this system operates
[Your Level 1-5 service] handling citizen interactions that cannot tolerate
extended outages or inconsistent behaviour.

## Operational priorities
- Citizen service continuity during all deployments
- Detection of problems before citizens report them
- Recovery procedures any team member can execute
- Compliance validation that runs automatically, not manually

## Critical user journeys
- [List the 2-3 journeys in your service where failure causes real harm]
- [Include peak demand periods specific to your service]

## Peak demand patterns
- [When does your service experience surge traffic?]
- [What external events trigger increased load?]
```

### tech.md

```markdown
# Technical Standards

## Runtime environment
- [Your service's deployment target: ECS, Lambda, EC2, etc.]
- [Infrastructure-as-code approach: CloudFormation, Terraform, CDK]
- [Container registry and artifact storage]

## Deployment pipeline
- GitHub Actions / AWS CodePipeline / Jenkins
- Quality gates: unit tests, integration tests, security scans, accessibility checks
- Deployment strategy: blue-green, canary, or rolling depending on service criticality

## Observability stack
- CloudWatch for metrics and logs
- X-Ray for distributed tracing
- Service-level objectives based on citizen experience, not server health
- Alert routing via PagerDuty or equivalent

## Compliance controls
- WCAG 2.1 AA validation in pipeline
- OWASP dependency scanning
- Data protection impact assessment triggers
- Audit logging for all deployment actions
```

## Agent for this challenge

Save this in `.kiro/agents/ops-analyst.md`.

```markdown
# Ops Analyst Agent

You analyse service-specific operational requirements and identify gaps in deployment
and incident response procedures.

## Your expertise
- Deployment analysis: identifying rollback risks and zero-downtime requirements
- Incident analysis: mapping failure modes to detection and response procedures
- Monitoring analysis: designing alerts based on citizen impact, not system metrics

## When analysing deployments
- Ask "What happens to in-flight requests during this deployment?"
- Check for database migration risks that could block rollback
- Identify external dependencies that deployments might disrupt
- Verify rollback procedures actually work for this service

## When designing incident response
- Start with citizen impact, not technical symptoms
- Check that runbooks can be followed at 3am by someone unfamiliar with the service
- Verify escalation paths account for out-of-hours scenarios
- Ensure post-incident reviews capture actionable improvements

## Red flags in operational design
- Deployment procedures that assume nothing will go wrong
- Alerts based on arbitrary thresholds rather than citizen impact
- Runbooks requiring knowledge only one person has
- Recovery procedures never actually tested
```

## Hook for this challenge

Save this in `.kiro/hooks/deployment-validator.yaml`.

```yaml
name: deployment-validator
event: file_saved
match: "**/*{deploy,pipeline,release,rollback}*.{yaml,yml,json,md}"
prompt: |
  Check this deployment configuration for government service requirements:

  Rollback capability:
  - Can the deployment be reversed within 15 minutes?
  - Are database changes backwards-compatible?
  - Is there a tested rollback procedure documented?

  Zero-downtime compliance:
  - Will in-flight citizen requests complete successfully?
  - Are health checks configured to prevent premature traffic shift?
  - Is there a deployment window that avoids peak demand periods?

  Compliance controls:
  - Are security scans configured to run before deployment?
  - Is accessibility validation included in the pipeline?
  - Are audit logs captured for deployment actions?

  Citizen impact:
  - What happens to citizens using the service during deployment?
  - How quickly would operators detect a bad deployment?
  - Is there a communication plan for extended incidents?

  Flag gaps that could cause citizen service disruption.
```

## Effective spec prompts

Use these prompts to guide Kiro through your operational design.

### Deployment pipeline specification

> Create the deployment pipeline specification for my [Level X] government service. Cover: which quality gates must pass before deployment proceeds; how the pipeline validates accessibility and security compliance; what deployment strategy minimises citizen disruption; how rollback triggers automatically when health checks fail. Include specific tests for the failure modes identified in my service analysis.

### Incident response runbook specification

> Design incident response runbooks for my specific service. For each failure mode I identified: what alerts detect the problem; what the on-call person sees and does first; how to confirm the problem is real; step-by-step recovery actions assuming no prior knowledge of the service; when and how to escalate; what to communicate to affected citizens. Write for someone handling their first incident at 3am.

### Monitoring and alerting specification

> Create the monitoring strategy for my government service. Cover: which service-level objectives reflect citizen experience; what metrics detect problems before citizens report them; how alert thresholds derive from citizen impact rather than arbitrary numbers; what dashboards show operators during incidents. Focus on the citizen journeys critical to my service.

### Compliance automation specification

> Design automated compliance validation for my service's pipeline. Cover: which WCAG 2.1 AA checks run and when; how security scanning integrates with deployment gates; what audit records the pipeline creates for deployment actions; how policy changes propagate through the compliance checks. Include acceptance criteria proving compliance, not just absence of errors.

## Gotchas specific to DevOps with Kiro

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Steering file scope creep | Operations context expands to cover every possible failure | Constrain to top 5 failure modes by citizen impact; defer others to backlog |
| Hook glob over-matching | Deployment hook fires on every YAML file, not just pipeline configs | Use specific patterns like `**/pipeline*.yml` or `**/deploy/**/*.yaml` |
| Spec task granularity mismatch | Specs generate runbook tasks too broad ("handle database failures") or too narrow ("check connection string") | Request tasks completable in 30-60 minutes with clear done criteria |
| Agent context window saturation | Ops analyst agent given entire codebase loses focus on critical paths | Scope agent context to deployment configs, monitoring setup, and runbook files only |
| Hook-agent circular triggers | Deployment validator hook triggers agent which modifies file which triggers hook | Add file-modification debounce; exclude agent-generated changes from hook patterns |

## Quality checkpoints

### Spec artifact completeness

- [ ] Deployment pipeline specification covers all quality gates and rollback procedures
- [ ] Incident runbooks exist for each failure mode identified in service analysis
- [ ] Monitoring specification defines SLOs based on citizen journeys
- [ ] Compliance automation specification covers accessibility, security, and audit requirements

### Service specificity validation

- [ ] Pipeline tests address your service's actual failure modes, not generic scenarios
- [ ] Runbooks reference your service's specific components and dependencies
- [ ] Alert thresholds derive from your service's citizen impact analysis
- [ ] Compliance checks match your service's data handling and accessibility requirements

### Operational readiness

- [ ] Rollback procedure tested and completes within 15 minutes
- [ ] Health checks detect actual service problems, not just container status
- [ ] Alerts fire before citizens would notice problems
- [ ] On-call rotation and escalation paths documented and agreed

### Documentation for operators

- [ ] Runbooks executable by someone with no prior service knowledge
- [ ] Decision points clear: when to escalate, when to rollback, when to communicate
- [ ] Recovery steps verified by someone other than the author
- [ ] Post-incident review template ready for use

### Citizen impact validation

- [ ] Deployment procedures tested during realistic load
- [ ] Incident communication templates ready for your service's stakeholders
- [ ] Recovery time objectives align with citizen tolerance for outage
- [ ] Monitoring dashboards show citizen experience, not just server metrics

## Reflection questions

When you finish, consider:

- Does your deployment pipeline catch the specific problems your service is likely to have?
- Could a team member who has never touched your service follow your runbooks at 3am?
- Do your alerts detect problems before citizens notice, or after they complain?
- What would happen if your service failed during its peak demand period?
- How would you prove to an auditor that a specific deployment followed approved procedures?
