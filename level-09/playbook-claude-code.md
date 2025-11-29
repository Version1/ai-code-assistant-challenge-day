# Level 9: Multi-Service Architecture Design Playbook

Design a distributed system for the "Starting University" life event. Five government departments must coordinate student transitions - from loan applications to NHS registration. Your output: architecture documentation, not code.

---

## CLAUDE.md Configuration

```markdown
## Level 9: Multi-Service Architecture

### Domain Context
Design architecture for "Starting University" spanning five departments:
- Student Loans Company (SLC): funding applications, payment disbursement
- HMRC: tax status, part-time work registration
- NHS: GP registration, health records transfer
- Home Office: visa status for international students
- Department for Education (DfE): course enrolment, qualification verification

### Architecture Principles
- Event-driven communication between departments
- Data sovereignty: each department owns and controls its data
- Saga pattern for distributed transactions
- Circuit breakers for resilience
- Eventual consistency (not immediate consistency)

### Output Artifacts
- C4 diagrams (context, container, component levels)
- Sequence diagrams for key user journeys
- API contracts (OpenAPI format)
- Data flow matrices showing what moves where
```

---

## Custom Slash Commands

### /project:map-dependencies

**File:** `.claude/commands/map-dependencies.md`

```markdown
Map service dependencies for Starting University architecture.

## Dependency Graph
Show which services call others, data flow direction, sync vs async connections.

## Coupling Assessment
For each dependency: coupling type (data/temporal/semantic), strength, risk level.

## Critical Path
Identify bottlenecks and longest completion time for student registration.

## Integration Patterns
Recommend for each point: request/response vs event-driven, sync vs async.

Output table: Source | Target | Pattern | Coupling | Risk
```

### /project:analyze-failures

**File:** `.claude/commands/analyze-failures.md`

```markdown
Analyse failure modes for Starting University multi-service architecture.

## Failure Catalog
Document failures: network, service, data, integration, business rule violations.

## Impact Assessment
For each: blast radius, recovery time, data impact, user experience.

## Resilience Patterns
Recommend: circuit breakers, retry policies, fallbacks, bulkheads.

## Graceful Degradation
Design degraded experiences when SLC, NHS, or HMRC become unavailable.

Output matrix: Failure | Probability | Impact | Detection | Response
```

---

## Model Recommendations

| Task | Model | Reasoning |
|------|-------|-----------|
| High-level system design | Opus | Balances competing concerns across departments |
| Failure mode brainstorming | Opus | Benefits from creative, adversarial thinking |
| Component-level design | Sonnet | Detailed work within established boundaries |
| API contract drafting | Sonnet | Structured OpenAPI output |
| Sequence diagrams | Sonnet | Systematic documentation of known flows |
| Trade-off analysis | Opus | Weighs political and technical factors |

---

## Effective Prompts

### 1. Service Boundary Definition

```
Define service boundaries for the Starting University journey.

For each department (SLC, HMRC, NHS, Home Office, DfE), identify:
- Core responsibilities that cannot be delegated
- Data entities this department must own
- Events produced and consumed

Apply: single responsibility, clear data ownership, operational autonomy.
Flag responsibilities that could belong to multiple departments.
```

### 2. Authentication Federation

```
Design federated authentication for Starting University portal.

Requirements:
- Single sign-on across five departmental services
- Departments retain their authorisation rules
- Handle international students lacking UK identity documents
- Manage status changes (visa renewal, address updates)

Address: identity provider choice, token claims, session management.
Produce sequence diagram for student accessing SLC after DfE authentication.
```

### 3. Saga Orchestration

```
Design a saga for complete student registration.

Steps: DfE enrolment -> SLC loan -> HMRC tax status -> NHS GP -> Home Office visa

Define:
- Orchestrator location (central vs choreography)
- Compensating transactions for each step
- Timeout handling for slow responses
- Partial completion states

Create state diagram showing in-progress, completed, failed, and suspended states.
```

### 4. Cross-Departmental Data Consistency

```
Design data consistency for student information across departments.

Solve: change propagation, conflict resolution, stale data handling, audit trail.

Constraints:
- No shared database (data sovereignty)
- Updates may take hours to propagate
- Departments have maintenance windows
- Students may provide conflicting information to different departments

Output matrix: Entity | Owner | Consumers | Update frequency | Staleness tolerance
```

### 5. Policy Change Adaptation

```
Design for adaptability when government policy changes.

Examples: new visa categories, loan threshold changes, NHS devolution differences.

Address:
- Where policy rules live (code, config, rules engine)
- Deployment without system-wide releases
- Testing and rollback strategies

Classify each integration point: stable, configurable, or dynamic.
Produce policy change impact matrix.
```

---

## Tips and Gotchas

| Tip | Why It Matters |
|-----|----------------|
| Start with failure modes | Distributed systems fail constantly. Design for failure first. |
| Map data sovereignty early | Each department owns specific data. Violations create political blockers. |
| Use correlation IDs everywhere | One student action touches five departments. Without IDs, debugging is impossible. |
| Design for departmental autonomy | Departments reject designs requiring core system changes. Adapt to their constraints. |
| Version everything from day one | APIs, events, schemas will change. Retrofitting versioning causes outages. |

---

## Reflection Questions

### 1. Consistency vs Availability
A student updates their address with SLC. NHS shows the old address for 4 hours. Is this acceptable? Which entities need stronger consistency? What's the cost?

### 2. Failure Blast Radius
Home Office goes down. Can domestic students complete registration? How do international students know what's happening? What manual processes activate?

### 3. Evolution and Extensibility
Next year, accommodation services join. How does a new department integrate? What contracts must they implement? What's minimum viable integration?

---

## Success Criteria

- [ ] Each department can deploy independently
- [ ] Single service failure doesn't stop the entire journey
- [ ] Data ownership is clear and respected
- [ ] New departments can join without redesigning existing services
- [ ] Students understand their application status at all times

Architecture is about trade-offs. Document yours.
