# Level 3: Database-Backed CRUD Operations

**Theme: AI-powered centralised service architecture and cross-government platform design**

## Challenge Overview

Government departments handle millions of citizen enquiries annually, but these enquiries are managed through fragmented, department-specific systems that create inconsistent user experiences and duplicate operational overhead. The 2025 State of Digital Government Review found that "fragmented structures of public sector organisations still lead to duplication of services and systems" with citizens often required to "navigate the gaps between multiple public services and organisations to administer basic life events." 

Another area of particular inconsistency is how citizens interact with departments when they have queries that aren't answerable with existing content or digital services. Citizens encounter completely different enquiry processes for tax queries (HMRC), court guidance (HMCTS), council tax questions (local authorities), and agricultural support (Defra) - violating the fundamental service design principle of "be familiar to users." 

As an example of how complex this fragmentation can become, GOV.UK One Login was created specifically to "consolidate 19 different account setups and 44 unique sign-in methods into a single, unified login system."

Under the Government Digital Service (GDS) Service Standard Point 13 ("Use and contribute to open standards, common components and patterns") and the Government Technology Innovation Strategy, departments must adopt shared platforms that deliver consistent citizen experiences whilst reducing operational costs and technical debt.

**The specific problems with current enquiry management across government:**

- Each department builds similar case management functionality in isolation
- Inconsistent response times and quality across government services
- No cross-government learning from citizen enquiries or failure demand analysis
- Staff in different departments solving identical technical and operational challenges
- Citizens must learn different processes for fundamentally similar government interactions
- No systematic analysis of enquiries to identify content gaps and service improvement opportunities

**The opportunity:** Just as GOV.UK Notify solved email and SMS fragmentation by providing a single platform that departments integrate with, we can solve enquiry management fragmentation with GOV.UK Enquiries - a centralised platform where departments register their services and integrate enquiry handling through APIs and SDKs. This approach creates consistent citizen experiences, reduces duplicate development costs, and enables AI-powered insights across government enquiry data to drive continuous service improvement.

## The Challenge

**Objective:** Design and build the complete data architecture for GOV.UK Enquiries - focusing on the multi-tenant data model that could support a centralised enquiry management platform

- Start with comprehensive data model design supporting multi-tenant government workflows across all enquiry types
- Design the database schema, relationships, and business logic for enquiry lifecycle management
- Build a simple case management interface to demonstrate how government staff would manage enquiries and prove the data model works
- Generate realistic sample data at scale to validate the data model design
- Include mock authentication to simulate departmental staff access
- Discuss (but don't implement) how AI-powered features for response generation, sentiment analysis, and failure demand insights could be added in the future

## Success Criteria

### Core Requirements

- **Complete multi-tenant data model:** Comprehensive database schema supporting all government enquiry types with secure data isolation between departments
- **Enquiry lifecycle management:** Full data model for enquiry workflow from submission through resolution with configurable stages
- **Scalable architecture:** Database design that can handle thousands of enquiries across multiple departments
- **Business logic implementation:** Proper data validation, constraints, and relationships reflecting government workflows
- **Demonstration interface:** Simple frontend showing how the data model works in practice with real case management scenarios
- **Sample data generation:** Realistic multi-departmental dataset proving the model works at scale

### Government-Specific Requirements

- **Cross-government consistency:** Standardised enquiry categories and workflow stages that work across all departments
- **Audit and compliance:** Complete data lineage and change tracking suitable for government accountability requirements
- **Multi-tenant security:** Department-level data isolation while enabling system-wide operational insights

## Source Materials: Government Enquiry Types for Data Model Design

Use these real government enquiry categories as examples to inform your generic data model design. Your data architecture should be flexible enough to handle ALL types of government enquiries, of which these are representative examples:

### High-Volume Transactional Enquiries
- **HMRC tax queries:** Self-assessment deadlines, payment plans, VAT registration status
- **DVLA vehicle services:** Licence renewals, medical fitness requirements, vehicle taxation
- **Council tax queries:** Payment issues, exemptions, property band challenges

### Complex Advisory Enquiries  
- **Court service guidance:** What citizens can/cannot do during ongoing cases, procedure clarifications
- **Planning permission queries:** Application requirements, local policy interpretation, appeal processes
- **Benefits advice:** Eligibility questions, application status, appeal procedures

### Specialist Technical Enquiries
- **Defra agricultural support:** Cattle registration, subsidy applications, environmental compliance
- **Companies House:** Business registration, filing requirements, dissolution procedures  
- **Land Registry:** Property searches, boundary disputes, title registration

### Emergency and Time-Critical Enquiries
- **NHS patient urgent queries:** Appointment access, prescription issues, health advice escalation
- **Housing emergency support:** Homelessness prevention, urgent repairs, temporary accommodation
- **Business continuity:** Licensing for emergency trading, temporary permissions, crisis support

## Supporting Resources

This challenge requires **data model-first architecture** - starting with comprehensive database design before building any application features. The key principle is: **start with the data model, not the application**.

### Approach 1: Prompt-Driven Development ("Data Model First")

This approach uses AI tools to design comprehensive database architectures and business logic before generating any user interface code.

**When to use:** Greenfield database design, complex government workflows, when data integrity and business rules are paramount.

#### Phase 1: Meta-Prompting for Data Architecture Planning

Use your AI tool's chat/planning capabilities to think through the domain before designing. Many AI tools have specific modes for this kind of architectural thinking.

```
"I need to design a comprehensive data model for GOV.UK Enquiries - a multi-tenant 
platform for all UK government enquiry management. Before we start building anything, 
help me think through the domain and create the most effective data modelling approach.

I need to support enquiry types ranging from:
- Simple transactional queries (tax deadlines, licence renewals)
- Complex advisory requests (court guidance, planning permission)
- Specialist technical queries (agricultural compliance, business registration)  
- Emergency/time-critical cases (health appointments, housing emergencies)

Can you help me:
1. Identify the core entities and relationships I'll need
2. Think through multi-tenant security and data isolation requirements
3. Consider government-specific audit and compliance needs
4. Plan for configurable workflows that different departments can customise
5. Design for scale (millions of enquiries across hundreds of departments)

What questions should I be asking myself about government enquiry management 
that I might not have considered? Help me build a comprehensive understanding 
of this domain before I start designing the actual database schema."
```

**Benefits of this planning approach:**

- Leverages AI's domain knowledge to identify requirements you might miss
- Helps you understand complex government workflows before technical design
- Creates opportunity to visualise relationships and dependencies
- Enables iterative refinement of your understanding before committing to schema
- Produces better technical prompts because your requirements are clearer

#### Phase 2: Comprehensive Data Model Generation

Once you understand the domain, generate your complete database architecture:

```
"You are designing the complete database schema for GOV.UK Enquiries - a multi-tenant 
platform supporting all UK government enquiry management.

DOMAIN UNDERSTANDING:
- Support all government enquiry types from simple transactional to complex advisory
- Multi-tenant architecture with complete departmental data isolation
- Configurable workflows allowing different departments to customise their processes
- Government-grade audit trails and compliance requirements
- Scale to handle millions of enquiries across hundreds of government organisations

DATA MODEL REQUIREMENTS:
- Citizens can submit enquiries to any government department
- Enquiries are automatically routed to appropriate departmental staff
- Staff can manage enquiries through configurable workflow stages
- Complete audit trail of all actions, decisions, and status changes
- Departmental managers can configure enquiry types and approval workflows
- System administrators can manage department setup and user access

TECHNICAL CONSTRAINTS:
- PostgreSQL database with appropriate indexes and constraints
- Row-level security ensuring departmental data isolation
- Efficient querying for both operational use and management reporting
- Data retention and archival strategies for government compliance
- Schema designed for both transactional operations and analytical queries

Generate a complete database design including:
1. Entity Relationship Diagram showing all tables and relationships
2. Detailed table definitions with data types, constraints, and indexes
3. Multi-tenant security model with row-level security policies
4. Sample data generation strategy demonstrating all enquiry types
5. Business logic constraints ensuring data consistency
6. Government-specific compliance features (audit trails, data retention)

Create a schema that is generic enough to handle any government enquiry type 
whilst being specific enough to enforce proper workflow and business rules."
```

#### Phase 3: Business Logic and Interface Design

With your data model established, generate the application logic and simple interface:

```
"Based on the data model you've designed, create a simple case management interface 
that demonstrates how government staff would use this system in practice.

INTERFACE REQUIREMENTS:
- Simple login system (can be mocked) allowing staff to access their department's enquiries
- Dashboard showing enquiry queues, priorities, and staff workload
- Enquiry details view with full history and action capabilities
- Ability to update enquiry status, add notes, and assign to colleagues
- Basic reporting on enquiry volumes and resolution times

TECHNICAL APPROACH:
- Focus on demonstrating the data model works, not production-ready features
- Include sample data showing different enquiry types and workflow stages
- Simple frontend (HTML/JavaScript or basic web framework) 
- Emphasise data integrity and business rule enforcement over visual design
- Show how the multi-tenant data model enables departmental isolation

Generate a working demonstration that proves your data model can handle 
real government enquiry management scenarios."
```

### Approach 2: Spec-Driven Development

This approach creates executable specifications for database systems, following structured phases that ensure comprehensive data architecture.

**When to use:** Complex data requirements, when you need reproducible architectures, or formal documentation for technical approval.

#### Setting Up Spec-Driven Development

**Phase 1: Data Architecture Specification (/specify)**

```
/specify Design a complete multi-tenant database architecture for GOV.UK Enquiries 
supporting all UK government enquiry management with proper data isolation and workflow management.

The system must:
- Support secure multi-tenant data architecture with complete isolation between departments
- Handle all government enquiry types from transactional to complex advisory cases
- Provide configurable workflow stages that departments can customise
- Maintain comprehensive audit trails for government accountability requirements
- Scale to support hundreds of departments handling millions of annual enquiries
- Enable both operational enquiry management and analytical reporting
- Meet government data protection and retention compliance requirements

Government departments currently operate isolated enquiry systems creating inconsistent 
citizen experiences and duplicating technical development across government.
```

**Phase 2: Technical Data Model Planning (/plan)**

```
/plan The GOV.UK Enquiries database architecture must use:

DATABASE DESIGN:
- PostgreSQL with comprehensive indexing strategies for government-scale performance
- Properly normalised schema design preventing data inconsistency
- Row-level security policies ensuring departmental data isolation
- Configurable workflow tables supporting departmental customisation
- Audit table architecture with tamper-evident change tracking
- Automated data retention and archival meeting government compliance requirements

MULTI-TENANCY ARCHITECTURE:
- Department-level data isolation using PostgreSQL row-level security
- Shared schema design with tenant-aware queries and constraints
- Performance optimisation for mixed departmental workloads
- Analytics capabilities that respect departmental boundaries
- Configuration management allowing departmental workflow customisation

BUSINESS LOGIC CONSTRAINTS:
- Database-level enforcement of workflow stage transitions
- Referential integrity ensuring data consistency across entities
- Validation constraints reflecting government business rules
- Performance optimisation for both operational and reporting queries
- Data retention automation with configurable policies per department
```

**Phase 3: Implementation Tasks (/tasks)**

The tool will create structured implementation tasks covering database schema design, business logic implementation, sample data generation, and demonstration interface development.

### Hybrid Approach

Combine both methodologies for optimal data model development:

- Use **data model-first** for initial domain understanding and schema design
- Use **spec-driven** for formal technical documentation and constraint specification
- Use **data model-first** for rapid iteration and sample data generation
- Return to **spec-driven** for formal compliance and approval documentation

## Mini Prompt Library

Use these focused prompts for specific aspects of your database design:

### Data Model Design Prompts

```
"Design a comprehensive entity relationship diagram for government enquiry management 
that can handle all enquiry types from simple transactional to complex advisory cases. 
Include proper relationships, constraints, and multi-tenant isolation strategies."

"Create database table definitions for enquiry lifecycle management with configurable 
workflow stages that different government departments can customise whilst maintaining 
data integrity and audit requirements."
```

### Multi-Tenant Architecture Prompts

```
"Design row-level security policies for PostgreSQL that ensure complete data isolation 
between government departments whilst enabling system administrators to manage 
cross-departmental operations and analytics."

"Create a data model for configurable government workflows that allows departments 
to define their own enquiry types, approval stages, and escalation rules whilst 
maintaining consistent core functionality."
```

### Sample Data Generation Prompts

```
"Generate realistic sample enquiries across multiple government departments (HMRC, DVLA, 
local councils, courts) demonstrating different enquiry types, complexity levels, and 
workflow stages. Include citizen details, staff assignments, and status histories."

"Create sample departmental configurations showing how different government organisations 
would set up enquiry categories, workflow stages, and staff roles in the database. 
Demonstrate multi-tenant customisation capabilities."
```

### Business Logic Prompts

```
"Generate database constraints and validation rules for government enquiry management 
that ensure data quality whilst remaining flexible enough to handle different 
departmental requirements and enquiry types."

"Create audit logging database design for government enquiry systems that tracks all 
changes with tamper-evident trails suitable for public sector accountability and 
compliance requirements."
```

## Implementation Sequence

Follow this structured sequence to build your data model and demonstration effectively:

### 1. Data Model Foundation
- Use AI to design comprehensive multi-tenant database schema
- Define all entities, relationships, and constraints for enquiry management
- Create database indexes and performance optimisation strategies

### 2. Sample Data Generation  
- Generate realistic multi-departmental enquiry datasets
- Create sample department configurations and staff user accounts
- Populate database with data demonstrating all enquiry types and workflow stages

### 3. Simple Management Interface
- Build basic login system (can be mocked) for departmental staff access
- Create enquiry management dashboard showing case queues and details
- Implement basic enquiry update functionality demonstrating the data model works

### 4. Validation and Testing
- Test multi-tenant data isolation works correctly
- Validate business logic constraints and workflow transitions
- Demonstrate scale with large sample datasets across multiple departments

## Things to Reflect on in Your Evaluation

### During Development

- **Multi-Tenant Complexity:** How effectively did the AI understand government data isolation and departmental autonomy requirements?
- **Data Model Quality:** What prompting techniques worked best for capturing comprehensive government enquiry workflows and business rules?
- **Business Logic Integration:** Where did you need to provide additional context about government compliance and audit requirements?
- **Cross-Government Patterns:** How well did the AI identify common patterns that could work across different government enquiry types?
- **Scale Considerations:** What aspects of government-scale database design required the most manual refinement?

### Post-Completion

- **Data Model Completeness:** How well does the generated schema handle the full complexity of government enquiry management across different departments?
- **Multi-Tenant Security:** What additional steps would be required to meet full government data isolation and security standards?
- **Workflow Flexibility:** How easily could this data model accommodate different departmental requirements and future changes?
- **Performance at Scale:** How well would this database design perform with millions of enquiries across hundreds of departments?
- **Integration Readiness:** What would be needed to integrate this data model with existing government systems and identity management?

### Team Discussion

- **Data Model Quality:** How does AI-generated database design compare to traditional enterprise data modelling approaches in government contexts?
- **Multi-Tenant Complexity:** What new challenges does AI-generated multi-tenant architecture create, and what safeguards are essential for government data isolation?
- **Business Logic Automation:** How effectively can AI capture complex government business rules and workflow requirements in database constraints?
- **Future AI Integration:** How could AI be used to support failure demand analysis and cross-government insights if this service were taken forward into production?
- **Scalability Realism:** How well would this data model handle the reality of hundreds of government departments with varying requirements and technical capabilities?
- **Technical Debt Prevention:** How might this approach reduce technical debt compared to traditional government department-by-department system development?