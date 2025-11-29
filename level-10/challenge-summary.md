# Level 10: Production Deployment and Incident Response

## What You Will Build

Take an application you built in Levels 1-5 and create production deployment and incident response specifically tailored to that service's citizen needs.

This is service-specific DevOps, not generic templates.

## Why This Matters

Government digital services handle millions of citizen interactions. When they fail, real people cannot access benefits, submit tax returns, or apply for essential services.

| Problem | Impact on Citizens |
|---------|-------------------|
| Manual deployments | Disruption during critical periods (tax deadlines, benefit renewals) |
| Reactive incident response | Extended outages affecting vulnerable users |
| Knowledge in individual heads | Inconsistent recovery when key staff unavailable |
| Manual compliance checks | Security and accessibility gaps reaching production |

**The scale of the problem:**

- 40% of operational effort spent firefighting preventable incidents (NAO Report 2024)
- Legal obligations under Equality Act 2010 to ensure services remain accessible
- Parliamentary scrutiny when high-profile services fail

## The Problem You Are Solving

Current government operations often rely on:

- **Manual release processes** that create citizen disruption during deployments
- **Inconsistent deployment practices** across teams and departments
- **Reactive incident management** that extends outages rather than preventing them
- **Tribal knowledge** where operational expertise exists only in individuals
- **Manual compliance validation** for security and accessibility requirements

## What Makes Government Different

Government services have requirements commercial services do not face:

| Requirement | Why It Matters |
|-------------|----------------|
| Zero-downtime during crises | Citizens cannot wait when benefits stop or deadlines approach |
| Regulatory compliance automation | GDPR, accessibility standards, security frameworks |
| Cross-departmental coordination | Services depend on shared platforms and data sources |
| Audit trails | Parliamentary questions and FOI requests require full history |
| Peak demand management | Policy announcements and deadlines create predictable surges |

## Choose Your Service

Select one application from Levels 1-5. Each has distinct operational requirements:

### Level 1: PDF Generation Service

**Citizen-critical scenarios:**
- Form submission reliability during benefit renewal periods
- Accessibility compliance for all generated documents
- Peak demand handling when deadlines approach

**Key failure modes:**
- Template rendering failures blocking applications
- Accessibility validation gaps creating legal risk
- Memory exhaustion under load

### Level 2: Performance Dashboard

**Citizen-critical scenarios:**
- Data pipeline failures hiding service problems
- Mobile performance affecting users with limited connectivity
- Cross-departmental data integration accuracy

**Key failure modes:**
- Stale data masking emerging issues
- Visualisation errors misleading decision-makers
- Authentication failures blocking access

### Level 3: Enquiry Management System

**Citizen-critical scenarios:**
- Multi-tenant service continuity across departments
- Data protection compliance for sensitive enquiries
- Crisis-driven volume spikes (flooding, policy changes)

**Key failure modes:**
- Queue processing delays extending response times
- Data leakage between tenants
- Workflow failures losing citizen context

### Level 4: Parliamentary Questions Tracker

**Citizen-critical scenarios:**
- Parliamentary deadline criticality (constitutional implications)
- Data migration validation when systems change
- Answer accuracy affecting democratic accountability

**Key failure modes:**
- Deadline tracking errors causing parliamentary breaches
- Workflow failures leaving questions unassigned
- Audit trail gaps under scrutiny

### Level 5: Benefits Rules Engine

**Citizen-critical scenarios:**
- Assessment consistency across all applications
- Legal challenge audit trails for disputed decisions
- Policy update deployment without service interruption

**Key failure modes:**
- Rule evaluation inconsistencies between deployments
- Version control gaps preventing audit
- Rollback failures when policy changes cause problems

## What You Will Deliver

### Deployment Pipeline

A CI/CD pipeline tailored to your chosen service:

- Automated testing specific to your service's failure modes
- Quality gates that catch issues before citizens experience them
- Deployment strategies appropriate to your service's availability requirements
- Rollback procedures tested and documented

### Monitoring and Alerting

Observability focused on citizen experience, not system metrics:

- Service-level objectives based on user journeys
- Alerts that detect problems before citizens report them
- Dashboards showing citizen impact, not server health

### Incident Response

Runbooks specific to your service's failure scenarios:

- Detection procedures for each failure mode
- Response steps written for the person on call at 3am
- Communication templates for affected citizens and stakeholders
- Post-incident review process

## Success Criteria

Your implementation is complete when:

| Criterion | Evidence |
|-----------|----------|
| Application-specific pipeline | Deployment process addresses your service's unique risks |
| Comprehensive quality automation | Tests cover your service's critical citizen journeys |
| Service-specific monitoring | Alerts based on citizen impact, not generic thresholds |
| Tailored incident runbooks | Response procedures for your service's actual failure modes |
| Production-ready implementation | Could deploy to live environment with confidence |

## How To Approach This

### Phase 1: Operational Analysis

Understand your specific service:

- Map citizen-critical journeys and where they can fail
- Identify peak demand patterns and risk periods
- Document dependencies on other services and data sources
- List compliance requirements specific to your service

### Phase 2: CI/CD and Monitoring

Build infrastructure tailored to your analysis:

- Design pipeline stages that address identified risks
- Create quality gates specific to your service's requirements
- Implement monitoring that detects your service's failure modes
- Set thresholds based on citizen impact, not arbitrary numbers

### Phase 3: Incident Response

Prepare for when things go wrong:

- Write runbooks for each failure mode you identified
- Create communication templates for your service's stakeholders
- Document escalation paths specific to your service
- Plan post-incident review process

## What Good Looks Like

**Generic approach (not what we want):**
"Deploy using blue-green strategy with standard health checks"

**Service-specific approach (what we want):**
"For the Benefits Rules Engine: Deploy rule changes with shadow evaluation comparing new rules against production decisions for 1 hour before cutover, with automatic rollback if assessment differences exceed 0.1%"

Your operational setup should reflect deep understanding of your specific service's citizen impact, not general DevOps best practices applied without context.
