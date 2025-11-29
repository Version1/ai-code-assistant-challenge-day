# Level 9: Multi-Service Architecture Design

## The Problem You Are Solving

When someone starts university, they must navigate five or more government services independently. They repeat their name, address, and circumstances to each one. They maintain separate accounts, remember different passwords, and understand which department handles what. If something goes wrong with one service, they have no idea how it affects the others.

This is not a technology problem. It is a design problem. Citizens experience life events as single journeys. Government delivers them as fragmented services.

## What You Will Design

A comprehensive multi-service architecture for the "Starting University" life event. Your design must coordinate five government departments into a seamless citizen experience.

| Department | Services to Integrate |
|------------|----------------------|
| Student Finance | Loan applications, maintenance grants, tuition fee payments |
| Local Authority | Council tax exemption, electoral registration, library access |
| NHS | GP registration, medical record transfer, prescription continuity |
| Electoral Registration | Voter registration, postal vote applications |
| Banking | Student account opening, identity verification, loan disbursement |

Your architecture must handle:

- **Service orchestration** - coordinating complex workflows across departments
- **Data consistency** - ensuring changes propagate correctly across all services
- **Authentication federation** - citizens authenticate once, access all services
- **Failure resilience** - one service going down should not block the entire journey
- **Policy adaptation** - when rules change in one department, the system adapts

## Why This Matters

### The citizen cost of fragmentation

Current government services force citizens to:

- Complete separate applications for each department
- Provide the same information repeatedly
- Understand departmental boundaries that are meaningless to them
- Track multiple reference numbers and accounts
- Start over when one service cannot talk to another

### The policy mandate

The Government Transformation Strategy and Digital Government Vision 2025 explicitly require "life event" approaches to service delivery. This is not optional innovation. It is policy direction.

### The technical debt

Every siloed system we build today makes future integration harder. Architecture decisions made now determine whether joined-up services are possible later.

## The Complexity You Must Address

### Multi-stage approval processes

Starting university involves sequential dependencies:

1. Academic offer confirmed
2. Means testing completed
3. Credit checks passed
4. Loan approved
5. Enrollment finalised

Each stage involves different departments, different timelines, and different data requirements.

### Conditional dependencies

Your architecture must handle logic such as:

- IF student finance approved AND enrolled at qualifying institution THEN enable council tax exemption application
- IF GP registration complete AND previous GP confirmed THEN initiate medical record transfer
- IF term-time address confirmed THEN offer electoral registration at new address

### Data synchronisation

When a student changes their address:

- Student Finance must update correspondence and payment details
- Local Authority must update council tax records
- NHS must update GP registration
- Electoral Registration must update voter roll
- Banking must update account details

Your design must ensure this happens consistently, even when some services are temporarily unavailable.

### Failure scenarios

Your architecture must define behaviour when:

- Student Finance system is down during peak application period
- NHS record transfer fails due to previous GP not responding
- Banking identity verification cannot complete
- Electoral registration deadline approaches but address unconfirmed

Citizens should not be blocked entirely. They should understand what is happening and what they can do.

## Success Criteria

Your architecture design is successful when it demonstrates:

| Criterion | What We Are Looking For |
|-----------|------------------------|
| Comprehensive scope | All five departments addressed with clear integration points |
| Service orchestration | Patterns for coordinating multi-stage, multi-department workflows |
| Resilience design | Graceful degradation when individual services fail |
| Data consistency | Strategy for keeping information synchronised across services |
| Cross-departmental coordination | How departments communicate and resolve conflicts |
| Identity federation | Single authentication providing appropriate access to all services |

## How to Approach This Challenge

### Phase 1: Life event analysis and service mapping

Understand the citizen journey before designing the architecture. Map what happens today, identify pain points, and define what "good" looks like for someone starting university.

### Phase 2: Architecture design and integration patterns

Design the technical architecture that enables the citizen experience you defined. Choose patterns for orchestration, data flow, and failure handling.

### Phase 3: Technical specification and documentation

Document your architecture with enough detail that teams could implement it. Include decision rationale so future teams understand why, not just what.

## What Makes This Challenge Different

This is not a coding exercise. You are designing architecture that must:

- Work across organisational boundaries with different governance
- Handle services with different availability and reliability characteristics
- Support policy changes without requiring coordinated releases
- Scale to handle peak periods (clearing, term start) without degradation
- Maintain citizen trust through transparency about what is happening

Your AI assistant can help you think through trade-offs, identify patterns, and document decisions. But the design choices are yours to make and justify.

## Before You Begin

Consider these questions:

1. What does the citizen actually need to accomplish, step by step?
2. Which integrations are essential versus nice-to-have?
3. What happens when the ideal flow cannot complete?
4. How do citizens know what is happening and what to do next?
5. How do departments maintain their own governance while participating?

Your architecture should answer these questions clearly.
