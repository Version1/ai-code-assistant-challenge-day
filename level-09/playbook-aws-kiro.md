# Kiro Playbook: Multi-Service Architecture Design

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for designing architecture that orchestrates government services around the "Starting University" life event.

This is an architecture design challenge. Your output is documentation and design artifacts, not code.

## Mode recommendation: Spec Mode

Use Spec Mode throughout this challenge. Here is why:

- Architecture decisions need documented rationale - stakeholders must understand why you chose specific patterns
- EARS-format requirements create traceable links between citizen needs and technical design
- Cross-departmental coordination requires explicit documentation of integration contracts
- Government architecture review boards expect defensible design decisions
- Audit trails must show how design choices address failure scenarios and security requirements

Vibe Mode works for exploring individual integration patterns. Switch to Spec Mode once you start documenting your architecture.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this system does
Orchestrates the "Starting University" life event across five departments:
Student Finance, Local Authority, NHS, Electoral Registration, and Banking.

## Who uses this system
- Students navigating university transition
- Department staff processing cross-service requests
- System administrators managing service integrations

## Core capabilities
- Single authentication across all participating services
- Coordinated workflows that handle multi-stage approvals
- Graceful handling when individual services are unavailable
- Consistent data synchronisation across departmental boundaries

## Success metrics
- Students complete life event tasks without understanding departmental structure
- Service failures do not cascade to unrelated functions
- Policy changes propagate without requiring system rebuilds
```

### tech.md

```markdown
# Technical Standards

## Integration patterns
- Event-driven architecture for loose coupling between services
- API contracts with versioning for independent service evolution
- Saga pattern for distributed transactions across departments

## Authentication and authorisation
- Federated identity using GOV.UK One Login where available
- Attribute-based access control for cross-service authorisation
- Consent management for data sharing between departments

## Resilience patterns
- Circuit breakers to prevent cascade failures
- Bulkhead isolation between service dependencies
- Compensating transactions for saga rollback scenarios

## Data consistency
- Eventual consistency with explicit conflict resolution
- Event sourcing for audit trail and state reconstruction
- Clear ownership boundaries for each data domain

## Constraints
- Each department retains operational autonomy
- Existing departmental systems cannot be replaced wholesale
- Security classification limits data sharing between some services
```

## Agent for this challenge

Save this in `.kiro/agents/service-integration-analyst.md`.

```markdown
# Service Integration Analyst Agent

You analyse cross-service dependencies and design integration patterns.

## Your expertise
- Identifying coupling types between services (data, temporal, contract)
- Mapping data contracts and ownership boundaries
- Spotting failure modes in distributed workflows
- Designing resilient integration patterns for government services

## When analysing service integrations
- Ask "What happens when this service is unavailable?"
- Check for hidden temporal coupling (service A must complete before B starts)
- Identify data that crosses departmental boundaries and its sensitivity
- Look for circular dependencies that create brittleness

## Coupling assessment criteria
- **Tight coupling**: Services share database or require synchronous calls
- **Moderate coupling**: Services share contracts but communicate asynchronously
- **Loose coupling**: Services communicate through events with no direct dependency

## Red flags in integration design
- Synchronous chains longer than two services
- Single points of failure with no fallback
- Data ownership disputed between departments
- Authentication requiring multiple identity proofs
```

## Hook for this challenge

Save this in `.kiro/hooks/architecture-completeness-check.yaml`.

```yaml
name: architecture-completeness-check
event: file_saved
match: "**/*{architecture,design,integration}*.md"
prompt: |
  Check this architecture document for completeness. Score each section:

  Required sections (flag if missing):
  - Service boundaries and responsibilities
  - Communication patterns between services
  - Authentication and authorisation design
  - Failure handling and resilience strategy
  - Data consistency approach
  - Deployment and evolution strategy

  For each section present, verify:
  - Does it address the "Starting University" life event specifically?
  - Are failure scenarios explicitly handled?
  - Is departmental autonomy preserved?

  Output a completeness score (sections present / 6) and list gaps.
```

## Effective spec prompts

Use these prompts to guide Kiro through your architecture design.

### Service orchestration design

> Design the service orchestration architecture for the "Starting University" life event. Cover: which services participate in each citizen task; how workflows coordinate across departmental boundaries; where synchronous versus asynchronous communication is appropriate; how the orchestration layer handles partial completion. Include a sequence diagram showing the student loan application workflow involving Student Finance, university systems, and banking.

### Authentication federation architecture

> Design the authentication and authorisation architecture for cross-government service access. Cover: how students authenticate once and access all relevant services; how consent is captured for data sharing between departments; how attribute-based access control determines service-specific permissions; what happens when a student's status changes (suspension, withdrawal, graduation). Address integration with GOV.UK One Login where applicable.

### Failure resilience strategy

> Design the failure handling strategy for the multi-service architecture. Cover: circuit breaker configuration for each service dependency; bulkhead isolation to prevent cascade failures; compensating transactions when distributed workflows fail mid-process; graceful degradation paths when non-critical services are unavailable. Include a failure mode analysis for the council tax exemption workflow that depends on Student Finance confirmation.

### Policy change adaptation design

> Design how the architecture adapts when policy changes affect multiple services. Cover: how new eligibility rules propagate across departments; how workflow changes deploy without disrupting in-flight transactions; how services evolve independently while maintaining contract compatibility; what governance ensures coordinated releases. Use the example of a policy change that modifies student loan eligibility criteria.

## Gotchas specific to architecture design with Kiro

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Steering file not loading | File path or naming does not match Kiro conventions | Verify files are in `.kiro/steering/` with exact names `product.md` and `tech.md` |
| Hook match pattern misses files | Glob pattern does not match your actual file names | Test pattern against your file names; use `**/*design*.md` for broader matching |
| Spec mode skips design phase | Kiro jumps from requirements to tasks without design document | Explicitly request design document generation; do not approve requirements until design exists |
| Agent not triggering | Agent file not in correct location or not referenced | Place in `.kiro/agents/` directory; reference agent by name in your prompts |
| Mermaid diagrams not rendering | Kiro generates diagram syntax but preview does not display | Copy diagram code to Mermaid Live Editor to verify syntax; some VS Code extensions need configuration |

## Quality checkpoints

### Spec completeness

- [ ] Requirements document captures all five department integrations
- [ ] EARS-format requirements link citizen needs to technical capabilities
- [ ] Design document covers all six required sections (service boundaries, communication, authentication, failure handling, data consistency, deployment)
- [ ] Tasks are specific enough to estimate and assign

### Design traceability

- [ ] Each design decision traces back to a requirement
- [ ] Failure handling covers scenarios identified in requirements
- [ ] Authentication design addresses citizen privacy requirements
- [ ] Data flows respect departmental ownership boundaries

### Resilience coverage

- [ ] Circuit breakers specified for each external service dependency
- [ ] Graceful degradation paths documented for non-critical service failures
- [ ] Compensating transactions defined for distributed workflow rollback
- [ ] Recovery procedures exist for each identified failure mode

### Hook validation

- [ ] Architecture completeness hook passes with score of 6/6
- [ ] All required sections present and address the specific life event
- [ ] Failure scenarios explicitly documented in each section
- [ ] Departmental autonomy preserved in integration design

### Submission package

- [ ] Architecture overview document suitable for technical review board
- [ ] Service integration diagrams showing communication patterns
- [ ] Failure mode analysis with mitigation strategies
- [ ] Implementation roadmap for phased departmental adoption
- [ ] Governance model for cross-departmental coordination

## Reflection questions

When you finish, consider:

- Did Spec Mode help you maintain traceability from citizen needs to technical design?
- Which integration patterns worked best for preserving departmental autonomy?
- What failure scenarios did the AI help you identify that you would have missed?
- Could your architecture approach be applied to other government life events?
- What assumptions about cross-departmental coordination did the design process reveal?
