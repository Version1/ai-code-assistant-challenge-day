# Level 8: Adaptive Testing Strategy & Risk-Based Quality Engineering

**Theme: AI-powered adaptive testing and context-driven quality validation for government digital services**

## Challenge Overview

Government digital services require testing approaches that adapt to the specific risks, user contexts, and failure modes of each service rather than applying generic testing templates. Under the Government Service Standard Point 10 ("Test the end-to-end service") and Point 4 ("Make the service simple to use"), departments must implement testing strategies that validate not just that features work, but that they work appropriately for the citizens who depend on them.

The 2024 Central Digital and Data Office Service Assessment Report identified "testing that validates technical compliance but misses real user failure modes" as a critical gap in government service delivery, with standardised testing approaches failing to identify the specific ways that different citizen groups experience service failures.

**The challenge:** Now that you've built a working government digital service in previous levels, how do you validate that it actually works for the citizens who need to use it? Different services have different risks - a housing benefit form has different failure modes than a data dashboard or enquiry system.

**The specific challenge of government service testing:**

Government digital services serve diverse citizen populations with varying:
- **Technical capabilities:** Citizens with different levels of digital literacy and access to modern devices
- **Accessibility needs:** Users requiring different assistive technologies and interaction approaches  
- **Circumstantial constraints:** Citizens completing applications under stress, time pressure, or complex personal situations
- **Risk tolerance:** Citizens who cannot afford service failures (benefit applications, licensing, emergency services)
- **Service contexts:** Applications completed in libraries, on mobile devices, with intermittent connectivity

**The opportunity:** AI tools can analyze specific government services and generate adaptive testing strategies that explore the unique risks, failure modes, and citizen contexts relevant to each service. This approach transforms testing from generic compliance checking into investigative quality engineering that discovers how services actually perform for the citizens who need them most.

## The Challenge

**Objective:** Take the government digital service you built in Level 1, 2, or 3 and use AI tools to develop an adaptive testing strategy that investigates the specific ways this service could fail for different citizen groups

- Choose your Level 1 (PDF transformation), Level 2 (data dashboard), or Level 3 (enquiry management) application
- Use AI tools to analyze the specific risks and failure modes relevant to YOUR service and citizen context
- Create investigative testing that explores how citizens with different constraints and capabilities would experience your service
- Build practical test implementation covering the failure scenarios most critical to your service's citizen outcomes
- Demonstrate adaptive testing approaches that government teams can apply to understand their own service risks

## Success Criteria

### Core Requirements

- **Service-specific risk analysis:** Clear identification of the failure modes most critical to YOUR chosen service and its specific citizen users
- **Adaptive test strategy:** Testing approach tailored to the actual risks, constraints, and failure patterns of your specific government service
- **Investigative test implementation:** Practical tests that explore how your service behaves under realistic citizen usage constraints and edge conditions
- **Citizen-context validation:** Testing that validates service performance for different citizen circumstances, capabilities, and environmental constraints
- **Failure mode exploration:** Systematic investigation of the ways your service could fail that would most impact citizen outcomes
- **Practical implementation:** Working tests covering the critical failure scenarios identified through your risk analysis

### Government-Specific Requirements

- **Vulnerable user consideration:** Testing approaches that specifically explore how citizens with the highest stakes experience your service
- **Real-world constraint validation:** Testing under conditions that reflect actual citizen environments and circumstances
- **Service-specific compliance:** Accessibility and security testing tailored to the particular requirements of YOUR chosen service
- **Operational context testing:** Validation of how your service performs under the specific operational pressures of its government context

## Source Materials: Your Previous Challenge Application

**Choose one of your completed applications:**

### Level 1: PDF to Digital Service Transformation
If you chose Level 1, your testing will investigate:
- **Form completion under pressure:** How do citizens complete housing benefit applications when facing eviction deadlines?
- **Accessibility across capabilities:** How do citizens with varying technical skills navigate multi-step application processes?
- **Error recovery scenarios:** What happens when citizens make mistakes or need to return to partially completed applications?
- **Document submission challenges:** How do citizens without scanners or smartphones submit required evidence?

### Level 2: Data Processing & Visualisation Dashboard  
If you chose Level 2, your testing will investigate:
- **Data comprehension across literacy levels:** How do citizens with different educational backgrounds interpret the data visualizations you created?
- **Mobile usage constraints:** How does your dashboard perform for citizens accessing government data on older smartphones with limited data plans?
- **Critical decision-making scenarios:** How do citizens use your dashboard to make important decisions, and where could misinterpretation cause problems?
- **Accessibility across devices:** How do citizens using screen readers or other assistive technologies access and understand your data presentations?

### Level 3: Database-Backed CRUD Operations
If you chose Level 3, your testing will investigate:
- **Enquiry submission under stress:** How do citizens submit urgent enquiries when experiencing crisis situations (homelessness, benefit suspensions, court deadlines)?
- **Multi-channel expectation management:** How do citizens understand response times and follow-up processes across different enquiry types?
- **Staff workflow validation:** How do government staff handle enquiry volumes during peak periods and system performance issues?
- **Data privacy understanding:** How do citizens understand what information is being collected and how it will be used in their enquiry?

## Supporting Resources

This challenge requires **adaptive testing design** - using AI tools to investigate the specific failure modes and citizen contexts most relevant to your chosen government service. The key principle is: **test what matters most for your specific service and citizen outcomes**.

### Approach 1: AI-Assisted Risk-Based Testing ("Service Investigation")

This approach uses AI tools to analyze your specific government service and generate testing strategies that explore the unique ways it could fail for different citizen groups.

**When to use:** Services with diverse citizen users, complex citizen journeys, high-stakes government services where failure has significant citizen impact.

#### Phase 1: Service-Specific Risk Analysis

Use AI to analyze the particular risks and failure modes of YOUR chosen service:

```
"I built a [Level 1 PDF transformation/Level 2 data dashboard/Level 3 enquiry system] 
for [describe your specific service] and I want to create testing that investigates 
how this specific service could fail for the citizens who depend on it.

Help me analyze the unique risks and failure modes of MY service by considering:
- Who are the specific citizens who would use this service and what are their varying circumstances?
- What are the highest-stakes situations where citizens would need this service to work correctly?
- What environmental and technical constraints do citizens face when using this specific service?
- What are the most critical failure points where the service not working properly would significantly impact citizen outcomes?
- What assumptions did I make about citizen capabilities, circumstances, or contexts when building this service?

Create a risk-based testing strategy that investigates these specific concerns rather than 
applying generic testing templates. Focus on the failure modes that would most impact 
the actual citizens who would use my particular government service."
```

#### Phase 2: Contextual Testing Implementation

Once you understand your service-specific risks, generate tests that investigate these particular concerns:

```
"Based on your analysis of my [specific service], create practical tests that investigate 
the specific ways this service could fail for different citizen groups and usage contexts.

CONTEXTUAL TESTING REQUIREMENTS:
For my [Level 1/2/3] government service, create tests that explore:

SERVICE-SPECIFIC FAILURE MODES:
- The critical points where my service could fail that would most impact citizen outcomes
- Edge cases and unusual but valid citizen circumstances that my service needs to handle
- Performance under the specific constraints citizens face when using my service
- Error scenarios and recovery paths relevant to the actual citizen journey I created

CITIZEN-CONTEXT VALIDATION:
- How citizens with different technical capabilities would experience my service
- Service behavior under realistic citizen environmental constraints (slow internet, older devices, distractions)
- Accessibility testing specific to the interaction patterns my service requires
- Completion testing for citizens under realistic time and stress pressures

INVESTIGATIVE TESTING APPROACH:
- Tests that explore "what if" scenarios specific to my service context
- Validation of citizen task completion rather than just technical functionality
- Investigation of how citizens would recover from errors or interruptions
- Testing of edge cases that could occur in real government operational environments

PRACTICAL IMPLEMENTATION:
Create working test code that:
- Focuses on the failure scenarios most critical to MY specific service
- Uses testing tools appropriate for the technology stack I chose
- Includes both automated tests for consistent validation and exploratory approaches for discovering unexpected issues
- Provides clear insight into how well my service serves its actual intended citizen users

Generate test implementation that investigates my specific service rather than 
applying generic government testing templates."
```

#### Phase 3: Adaptive Testing Methodology

With service-specific tests implemented, create systematic approaches for adaptive testing:

```
"Based on the contextual testing you've created for my specific government service, 
develop systematic approaches that other government development teams can use to create 
adaptive testing strategies for their own services.

ADAPTIVE TESTING METHODOLOGY:
Create approaches that help teams:
- Analyze the specific risks and failure modes of their particular government service
- Identify the citizen contexts and constraints most relevant to their service
- Design testing that explores service-specific failure scenarios rather than generic compliance
- Balance automated testing for consistency with investigative testing for discovery
- Adapt testing strategies as they learn more about their service and citizen usage patterns

PRACTICAL GUIDANCE:
- How to use AI tools to analyze service-specific risks and citizen contexts
- Methods for creating testing that focuses on citizen outcomes rather than just technical functionality
- Approaches for exploring edge cases and failure modes relevant to specific government services
- Integration of adaptive testing with government development workflows and compliance requirements

Generate methodology guidance that enables government teams to create testing strategies 
tailored to their specific services and citizen contexts."
```

### Approach 2: Spec-Driven Testing Strategy

This approach creates structured specifications for adaptive testing that can be systematically applied to different government services.

#### Phase 1: Adaptive Testing Specification (/specify)

```
/specify Create adaptive testing strategy for a specific government digital service that 
investigates service-specific failure modes, citizen contexts, and real-world usage 
constraints rather than applying generic testing templates.

The testing approach must:
- Analyze the specific risks and failure modes most critical to the chosen government service
- Validate service performance under realistic citizen usage constraints and environmental conditions
- Explore edge cases and unusual but valid citizen circumstances relevant to the specific service context
- Focus testing on citizen outcomes and task completion rather than just technical functionality
- Investigate how citizens with different capabilities and constraints experience the particular service
- Create practical test implementation covering the failure scenarios most critical to citizen success

Generic testing approaches fail to identify the service-specific failure modes that most 
impact citizens who depend on government digital services for critical life events and 
essential services.
```

### Mini Prompt Library

Use these focused prompts for specific aspects of adaptive testing:

#### Risk Analysis Prompts

```
"Analyze my specific [Level 1/2/3] government service and identify the failure modes that 
would most impact the citizens who depend on it. Focus on real-world usage constraints 
and high-stakes citizen situations where service failure has significant consequences."

"What are the critical assumptions I made about citizen capabilities and circumstances 
when building this service? Create testing that challenges these assumptions and explores 
how citizens with different constraints would experience the service."
```

#### Contextual Testing Prompts

```
"Create tests that explore how citizens complete [specific task from my service] under 
realistic constraints like time pressure, limited technical skills, or using older devices. 
Focus on task completion rather than just technical functionality."

"Generate testing that investigates the edge cases and error scenarios specific to my 
government service, particularly focusing on how citizens would recover from problems 
or interruptions during critical processes."
```

## Implementation Sequence

### 1. Service-Specific Risk Analysis
- Use AI to analyze your chosen Level 1/2/3 application and identify its specific failure modes and citizen contexts
- Create risk assessment focusing on the citizen outcomes most critical to your particular service
- Identify the assumptions and constraints most important to validate through testing

### 2. Contextual Test Design and Implementation  
- Generate tests that investigate your service's specific failure scenarios and citizen usage contexts
- Implement practical testing covering the risks most critical to your service's citizen outcomes
- Create both automated validation and investigative testing appropriate for your service context

### 3. Testing Validation and Methodology Development
- Validate that your testing approach effectively explores the critical aspects of your specific service
- Create systematic approaches that other government teams can adapt for their own service-specific testing
- Document the adaptive testing methodology for broader government application

## Things to Reflect on in Your Evaluation

### During Development

- **Service-Specific Analysis:** How effectively did AI tools identify the unique risks and failure modes of your particular government service rather than generic testing concerns?
- **Citizen Context Understanding:** What prompting techniques worked best for getting AI to consider realistic citizen constraints and usage scenarios for your specific service?
- **Adaptive Test Design:** Where did you need to provide additional context about your service's particular citizen users and their circumstances?
- **Practical Implementation:** How well did AI tools translate service-specific risks into practical, implementable tests rather than theoretical testing approaches?

### Post-Completion

- **Testing Relevance:** How well do your generated tests focus on the failure modes most critical to your specific service and citizen outcomes?
- **Context Validation:** How effectively do your tests explore realistic citizen usage constraints and environmental conditions for your particular service?
- **Adaptive Methodology:** How easily could other government teams apply your testing approach to analyze and test their own services?
- **Citizen Impact Focus:** How well do your tests validate citizen task completion and service effectiveness rather than just technical functionality?

### Team Discussion

- **Adaptive vs. Template Testing:** How does service-specific, risk-based testing compare to standardized testing approaches in discovering critical issues for government services?
- **AI-Assisted Risk Analysis:** What new capabilities does AI bring to understanding service-specific failure modes and citizen contexts?
- **Context-Driven Government Testing:** How could adaptive testing approaches improve government service quality by focusing on actual citizen usage patterns and constraints?
- **Testing Strategy Evolution:** How might risk-based, service-specific testing change government approaches to quality assurance and citizen service validation?