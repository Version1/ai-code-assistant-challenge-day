# Level 3: Database-Backed CRUD Operations

## What you will build

A complete data architecture for GOV.UK Enquiries - a centralised platform where government departments could manage citizen enquiries through a single, shared system.

You will design the database schema, build a simple case management interface, and generate realistic sample data to prove the model works at scale.

## Why this matters

Citizens currently face completely different enquiry processes depending on which department they contact. Tax queries go to HMRC. Court guidance goes to HMCTS. Council tax questions go to local authorities. Each department has built its own system, creating:

- Inconsistent experiences for citizens doing fundamentally similar things
- Duplicated effort across departments solving identical problems
- No way to learn from enquiries across government
- Different response times and quality standards

The 2025 State of Digital Government Review found that "fragmented structures of public sector organisations still lead to duplication of services and systems" - citizens must "navigate the gaps between multiple public services."

GOV.UK Notify solved this problem for email and SMS by providing a single platform departments integrate with. This challenge explores how a similar approach could work for enquiry management.

## The challenge

Design and build:

1. **A multi-tenant data model** - database schema supporting enquiries from multiple departments with secure data isolation
2. **Enquiry lifecycle management** - data structures for tracking enquiries from submission through resolution
3. **A demonstration interface** - simple frontend showing how government staff would use the system
4. **Realistic sample data** - enough data across multiple departments to prove the model works

You should also discuss (without implementing) how AI-powered features could enhance the platform in future.

## Success criteria

### Your data model must support

- **Multiple departments** using the same system with their data kept separate
- **Configurable workflows** - different enquiry types may need different stages
- **Complete audit trails** - who did what, when, for government accountability
- **Scale** - thousands of enquiries across multiple departments

### Your demonstration must show

- How staff would view and manage enquiries for their department
- How enquiries move through workflow stages
- How the multi-tenant model keeps departmental data isolated

## Government enquiry types to inform your design

Your data model should be generic enough to handle these real enquiry categories:

| Category | Examples |
|----------|----------|
| High-volume transactional | HMRC tax queries, DVLA vehicle services, council tax |
| Complex advisory | Court service guidance, planning permission, benefits advice |
| Specialist technical | Defra agricultural support, Companies House, Land Registry |
| Emergency and time-critical | NHS urgent queries, housing emergencies, business continuity |

## Approaches you might take

This challenge requires **data model-first thinking** - design your database architecture before building application features.

### Prompt-driven development
Use AI tools to design comprehensive database architectures and business logic before generating any interface code.

Best for: Exploring the domain, rapid iteration, when you want to understand the problem space quickly.

### Spec-driven development
Create formal specifications for your database system, following structured phases that ensure comprehensive architecture.

Best for: Complex data requirements, when you need reproducible designs, or formal documentation for technical review.

### Combining both approaches
Many practitioners start with prompt-driven exploration to understand the domain, then use spec-driven methods for formal documentation, returning to prompt-driven for iteration and sample data generation.

## Government context

This challenge aligns with:

- **GDS Service Standard Point 13** - use and contribute to open standards, common components and patterns
- **Government Technology Innovation Strategy** - departments adopting shared platforms for consistent citizen experiences
