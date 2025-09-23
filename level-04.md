# Level 4: Legacy Code Modernisation

**Theme: AI-powered legacy system transformation and cross-platform migration**

## Challenge Overview

UK government departments operate thousands of legacy desktop applications built between 2000-2010 that remain business-critical but increasingly difficult to maintain, support, and integrate with modern digital services. The 2023 Government Digital and Data Strategy identified "legacy technical debt" as a primary barrier to digital transformation, with departments spending up to 60% of their technology budgets maintaining aging systems rather than delivering new citizen services.

Under the Cabinet Office's Technology Code of Practice (TCoP) Point 4 ("Make use of open standards and common government platforms") and Point 6 ("Make things accessible and inclusive"), departments must modernise legacy applications to web-based services that integrate with GOV.UK infrastructure whilst maintaining business continuity.

**The specific problems with government legacy desktop applications:**

- Built with deprecated technologies (VB.NET, Access databases, Flash) that vendors no longer support
- Undocumented business logic embedded in desktop applications, creating knowledge risks when staff leave
- Cannot integrate with modern authentication systems like GOV.UK One Login
- Exclude remote workers and fail to meet current accessibility standards
- Create security risks through outdated dependencies and lack of centralised patch management
- Prevent data sharing across departments, blocking joined-up government initiatives
- Expensive to maintain with specialised contractor knowledge becoming increasingly rare

**The opportunity:** AI tools can rapidly analyse undocumented legacy systems, extract business logic, and generate modern web applications that preserve institutional knowledge whilst enabling integration with current government platforms. This approach reduces modernisation costs, preserves business continuity, and enables departments to redirect technology spending from maintenance to innovation.

## The Challenge

**Objective:** Use AI tools to modernise a legacy VB.NET government desktop application into a modern, accessible web service that preserves all business functionality

- Analyse an undocumented VB.NET Parliamentary Question tracking system that has been mocked up to represent typical government departmental applications
- Extract and document the embedded business logic using AI code analysis capabilities
- Transform the desktop application into a modern web application using your chosen contemporary frameworks
- Preserve all government-specific business rules whilst improving user experience and accessibility

## Success Criteria

### Core Requirements

- **Complete functionality preservation:** All features from the legacy application must work in the modern version
- **Business logic documentation:** Clear documentation of government-specific rules (PQ deadline calculations, reference formats)
- **Modern web architecture:** Contemporary framework with proper separation of concerns and maintainable code structure
- **Cross-platform accessibility:** Works on mobile and desktop with screen reader compatibility
- **Data migration strategy:** Clear approach for migrating existing data to modern storage solutions
- **Error handling and validation:** Robust input validation and user-friendly error messaging

### Government-Specific Requirements

- **Service continuity:** Modern system maintains all operational workflows from the legacy application
- **Professional presentation:** Clean, accessible interface suitable for government departmental use
- **Documentation standards:** Comprehensive technical documentation for future maintenance and development
- **Testing approach:** Validation strategy ensuring complete functional preservation during modernisation

## Source Materials: Legacy VB.NET Parliamentary Question Tracker

**GitHub Repository:** https://github.com/stevewalton28/ai-native-app-mod-exercise-vb

You will work with a complete VB.NET Windows Forms application that tracks Parliamentary Questions for a UK government department. This application was deliberately built as a legacy training exercise with authentic technical debt characteristics.

### Application Characteristics
The application includes typical government Parliamentary Question management features:
- **Parliamentary Question Management:** Core PQ tracking functionality with government-specific business rules
- **Business Logic:** Embedded deadline calculations and workflow management
- **Reference Management:** PQ numbering and tracking systems
- **Status Tracking:** Multi-stage workflow from receipt through departmental response
- **Team Assignment:** Basic departmental routing and assignment capabilities
- **Data Management:** Simple persistence and basic reporting features

### Authentic Legacy Technical Debt
As stated in the repository: *"This is not a real application, it is a mocked up application that is used for training purposes. It has no documentation and is ugly and legacy on purpose."*

- **Zero documentation:** Intentionally undocumented codebase with no README, comments, or technical guidance
- **Legacy coding patterns:** Deliberately poor coding practices including mixed naming conventions, hardcoded values, and minimal error handling
- **Monolithic architecture:** Business logic embedded within form event handlers following typical legacy government application patterns
- **Basic file storage:** Simple persistence approach with no backup, versioning, or data integrity safeguards
- **Platform dependency:** Windows-only executable representing typical government desktop application constraints

## Supporting Resources

The challenge requires **analysis-first modernisation** - using AI tools to comprehensively understand the legacy system before beginning transformation. The key principle is: **understand before you rebuild**.

### Approach 1: Prompt-Driven Development ("Legacy Archaeology")

This approach uses AI tools to systematically analyse and document legacy applications before generating modern equivalents that preserve all business functionality.

**When to use:** Complex legacy systems with embedded domain knowledge, when business continuity is paramount, rapid modernisation timelines.

#### Phase 1: Meta-Prompting for Legacy Analysis Planning

Use AI tools to develop comprehensive strategies for analysing undocumented legacy applications:

```
"I need to modernise a legacy VB.NET government application for Parliamentary Question 
tracking, but it has zero documentation. Help me create a systematic approach for 
using AI tools to analyse and understand this legacy system before modernisation.

The legacy application handles:
- Parliamentary question deadline calculations with UK government-specific rules
- Multiple PQ types with different response timeframes  
- Team assignment workflows for policy departments
- Status tracking through approval processes
- Reference number generation following government conventions

Can you help me:
1. Plan a systematic approach for analysing undocumented VB.NET code
2. Identify key business logic patterns I should extract and document
3. Create strategies for understanding government-specific workflows
4. Develop approaches for testing business rule preservation during migration
5. Plan modern architecture that maintains operational continuity

What systematic questions should I ask AI tools to ensure I capture all 
business-critical functionality before starting the modernisation? Help me 
create a comprehensive legacy analysis methodology."
```

**Benefits of this planning approach:**

- Leverages AI's code analysis capabilities to identify critical business logic
- Creates systematic documentation of previously undocumented government processes
- Reduces risk of losing institutional knowledge during modernisation
- Enables validation that modern system preserves all legacy functionality
- Produces clear requirements for modern system architecture

#### Phase 2: Comprehensive Legacy System Analysis

Once you understand your analysis approach, systematically document the legacy application:

```
"You are analysing a legacy VB.NET government application for Parliamentary Question 
tracking from this GitHub repository: https://github.com/stevewalton28/ai-native-app-mod-exercise-vb

This application was deliberately built with no documentation and poor coding practices 
for training purposes. I need you to comprehensively analyse this codebase and extract 
all business logic for modernisation.

ANALYSIS REQUIREMENTS:
- Download and examine the complete VB.NET codebase from the repository
- Document all business rules and government workflows embedded in the code
- Extract data models and relationships from the existing application structure
- Map user interface patterns and operational workflows
- Identify all hardcoded values, configuration settings, and business assumptions
- Catalogue integration points and external dependencies

GOVERNMENT CONTEXT:
- This represents a typical government departmental desktop application
- Parliamentary Questions have strict legal response requirements in UK government
- The application likely contains authentic government workflow patterns
- Business logic preservation is critical for operational continuity
- Staff depend on embedded workflows that may not be documented elsewhere

CODE ANALYSIS FOCUS:
- Business logic embedded throughout form event handlers and user interface code
- Validation rules and business constraints scattered across the application
- Data persistence patterns and file management approaches
- Error handling strategies and user feedback mechanisms
- Government-specific calculations and reference generation logic
- Workflow patterns reflecting departmental operational requirements

Generate comprehensive documentation including:
1. Business Rules Documentation: All government workflow rules with examples
2. Data Model Analysis: Entities, relationships, and validation requirements
3. User Interface Analysis: Interaction patterns and operational workflows
4. Technical Architecture Review: Current system structure and improvement opportunities
5. Integration Assessment: External dependencies and system boundaries
6. Modernisation Recommendations: Specific areas requiring technical improvement

Create documentation detailed enough to rebuild this system's functionality in 
a modern web application whilst preserving all embedded government business logic."
```

#### Phase 3: Modern System Generation with Business Continuity

With comprehensive legacy analysis complete, generate the modernised system:

```
"Based on your analysis of the legacy VB.NET Parliamentary Question system from 
https://github.com/stevewalton28/ai-native-app-mod-exercise-vb, create a complete 
modern web application that preserves all business functionality whilst modernising 
the technical architecture.

MODERNISATION REQUIREMENTS:
- Modern web framework of your choice suitable for this application
- Clean, responsive design working effectively on mobile devices and tablets
- Your chosen technology stack with proper separation of concerns
- Modern data storage replacing any file-based storage approaches
- Comprehensive error handling with user-friendly messaging

BUSINESS CONTINUITY CONSTRAINTS:
- All government business rules discovered in your analysis must work identically to the legacy system
- Any reference number generation or formatting must maintain institutional consistency  
- Departmental workflows and operational processes must be preserved exactly
- Data migration must handle existing data files without any data loss
- User workflows should feel familiar to current system users whilst improving user experience
- All status tracking, assignment, and approval processes must be maintained

GOVERNMENT COMPLIANCE:
- Professional interface design appropriate for departmental use
- Security considerations suitable for this type of application
- Performance optimised for operational environments and user expectations

TECHNICAL ARCHITECTURE:
- Clean, maintainable codebase with comprehensive documentation
- Modern authentication system appropriate for departmental users
- Scalable data design supporting multiple concurrent departmental staff
- Modern application architecture enabling future enhancements
- Automated testing ensuring all business rule preservation from legacy system
- Clear deployment approach suitable for modern hosting environments

Create a complete modern application including:
- Professional user interface with good accessibility practices
- Backend implementation with all discovered business logic properly implemented and documented
- Modern data design and any necessary data migration strategies
- Comprehensive technical documentation for development teams
- Testing strategy validating that all legacy system functionality is preserved
- Deployment and hosting recommendations suitable for modern infrastructure

Ensure the modernised system maintains 100% functional parity with the legacy 
application whilst providing all the benefits of modern web architecture and 
extensibility for future requirements."
```

### Approach 2: Spec-Driven Development

This approach creates executable specifications for legacy modernisation, following structured phases that ensure comprehensive system understanding and systematic transformation.

**When to use:** Complex government systems requiring formal documentation, when multiple stakeholders need to approve modernisation approaches, reproducible transformation processes.

#### Setting Up Spec-Driven Legacy Modernisation

**Phase 1: Legacy Analysis Specification (/specify)**

```
/specify Analyse and document a legacy VB.NET Parliamentary Question tracking system 
to enable comprehensive modernisation while preserving all government business functionality.

The system must be analysed to extract:
- Parliamentary question handling business rules with UK government-specific deadline calculations
- Workflow patterns for departmental team assignment and approval processes
- Data models and validation requirements embedded within desktop application code
- User interface patterns and operational workflows currently used by government staff
- Integration requirements and data exchange patterns with existing government systems
- Security considerations and compliance requirements for government departmental use

Government staff currently depend on this undocumented desktop application for 
managing Parliamentary Questions with legal response deadline requirements.
```

**Phase 2: Modernisation Architecture Planning (/plan)**

```
/plan The Parliamentary Question system modernisation must use:

ANALYSIS APPROACH:
- Systematic code analysis extracting business logic from VB.NET form event handlers
- Government workflow documentation capturing departmental approval processes  
- Data model extraction identifying entities, relationships, and validation rules
- User experience mapping preserving familiar operational patterns
- Integration requirement analysis for future government platform connectivity

MODERN ARCHITECTURE:
- Contemporary web framework suitable for government applications with clean design integration
- Clean separation of concerns replacing monolithic desktop application structure
- Modern database design with proper normalisation and performance optimisation
- Modern application architecture enabling future enhancements and integrations
- Comprehensive security design appropriate for government departmental data
- Responsive design supporting mobile and desktop government operational requirements

BUSINESS CONTINUITY:
- 100% functional parity with legacy system ensuring no operational disruption
- Data migration strategy handling existing data files and reference number continuity
- User workflow preservation maintaining familiar operational patterns for government staff
- Performance requirements meeting government operational standards and response times
- Compliance with government accessibility, security, and technical standards
```

**Phase 3: Implementation Tasks (/tasks)**

The tool will create structured implementation tasks covering legacy analysis, modern architecture design, business logic preservation, and government compliance validation.

### Hybrid Approach

Combine both methodologies for comprehensive legacy modernisation:

- Use **analysis-first** for systematic legacy system understanding and documentation
- Use **spec-driven** for formal modernisation planning and stakeholder approval
- Use **analysis-first** for rapid modern system generation and iteration
- Return to **spec-driven** for formal testing, compliance validation, and deployment planning

## Mini Prompt Library

Use these focused prompts for specific aspects of your legacy modernisation:

### Legacy Analysis Prompts

```
"Analyse the VB.NET government application at https://github.com/stevewalton28/ai-native-app-mod-exercise-vb 
and extract all business rules and government workflows. This deliberately undocumented 
codebase contains authentic government operational patterns that must be preserved 
during modernisation."

"Convert the business logic discovered in this legacy VB.NET Parliamentary Question 
system to modern web application code while preserving exactly the same government 
workflows and ensuring identical operational results for all departmental processes."
```

### Business Logic Preservation Prompts

```
"Transform the legacy desktop user interface workflows from the VB.NET Parliamentary 
Question application at https://github.com/stevewalton28/ai-native-app-mod-exercise-vb 
into a modern web interface following good design patterns while maintaining 
exactly the same operational steps and government processes."

"Design a modern web application architecture that replaces the file-based persistence 
in this legacy VB.NET system while providing better performance, security, and 
maintainability for government Parliamentary Question management at departmental scale."
```

### Modern Architecture Prompts

```
"Create a comprehensive data migration strategy for moving existing data from the 
legacy VB.NET Parliamentary Question system at https://github.com/stevewalton28/ai-native-app-mod-exercise-vb 
to a modern database system while preserving all historical records and maintaining 
operational continuity for government staff."

"Ensure this modernised Parliamentary Question system (based on analysis of 
https://github.com/stevewalton28/ai-native-app-mod-exercise-vb) meets professional 
accessibility standards and follows good design patterns while preserving 
all the business functionality from the legacy VB.NET desktop application."
```

### Government Compliance Prompts

```
"Design professional interfaces for this Parliamentary Question system that enable 
smooth operations whilst maintaining security and performance appropriate for 
departmental use, based on the workflows discovered in the legacy VB.NET application."
```

## Implementation Sequence

Follow this structured sequence to modernise your legacy system effectively:

### 1. Legacy System Analysis
- Use AI to comprehensively analyse the undocumented VB.NET application
- Extract and document all business rules, workflows, and data models
- Create comprehensive system documentation that preserves institutional knowledge

### 2. Modern Architecture Design
- Design contemporary web application architecture that addresses legacy system limitations
- Plan database design that improves upon file-based storage while preserving data integrity
- Create application design enabling future enhancements and integrations

### 3. Business Logic Preservation
- Implement modern system ensuring 100% functional parity with legacy application
- Validate that all Parliamentary Question rules and workflows operate identically
- Create comprehensive testing ensuring no business functionality is lost during modernisation

### 4. Professional Standards Integration
- Apply good design patterns for consistent professional user experience
- Implement accessibility compliance throughout the modernised system
- Ensure security and performance meet professional operational requirements

## Things to Reflect on in Your Evaluation

### During Development

- **Legacy Analysis Quality:** How effectively did AI tools extract business logic from undocumented VB.NET code?
- **Business Rule Preservation:** What prompting techniques worked best for ensuring government-specific workflows were maintained?
- **Architecture Translation:** Where did you need to provide additional context about translating desktop patterns to web applications?
- **Government Context Understanding:** How well did AI tools understand Parliamentary Question business rules and UK government operational requirements?
- **Documentation Generation:** What aspects of legacy system analysis required the most manual validation and refinement?

### Post-Completion

- **Functional Parity:** How completely does the modernised system replicate all legacy application functionality?
- **Code Quality Improvement:** What aspects of the modern system represent genuine improvements over the legacy architecture?
- **Professional Standards:** How well does the modernised system meet current technical and accessibility standards?
- **Maintainability Gains:** How much easier would this system be for government technical teams to maintain and extend?
- **Future Readiness:** How effectively could this modernised system accommodate future enhancements and integrations?

### Team Discussion

- **AI-Assisted Legacy Analysis:** How does AI-powered code analysis compare to traditional legacy system documentation approaches in government contexts?
- **Business Continuity Risks:** What new risks does AI-assisted modernisation create, and what safeguards are essential for government system transformation?
- **Institutional Knowledge Preservation:** How effectively can AI tools capture and document the institutional knowledge embedded in undocumented government systems?
- **Scaling Modernisation:** How could this AI-assisted approach scale across the thousands of legacy applications currently running in government departments?
- **Technical Debt Reduction:** How much technical debt could government departments eliminate by systematically applying AI-assisted legacy modernisation approaches?
- **Future-Proofing Strategies:** How might this modernisation approach position government systems for future technological changes and integration requirements?