Level 2: Data Processing & Visualisation


Theme: AI-powered public data consumption and citizen-focused visualization
Challenge Overview
Government departments publish vast amounts of open data through data.gov.uk, but this raw data remains largely inaccessible to citizens who could benefit from it most. Under the UK's Open Government Licence and the Public Sector Information Directive, departments have committed to making public data "findable, accessible, interoperable and reusable" (FAIR principles).
The problem with current data access:

Raw datasets require technical expertise to interpret and visualize
No standardized presentation layer across government data sources
Citizens cannot easily access relevant local information (air quality, transport delays, planning applications)
Data exists in silos, preventing meaningful cross-departmental insights
Mobile-unfriendly formats exclude citizens accessing services on-the-go
No real-time updates or alerts for time-sensitive information
The opportunity: AI tools can rapidly transform government open data into accessible, real-time dashboards that serve citizens directly - creating a deployable visualization layer that any department can use to make their data.gov.uk datasets citizen-ready whilst maintaining compliance with accessibility standards and data protection requirements.
The Challenge
Objective: Build a deployable government data dashboard that transforms raw data.gov.uk datasets into citizen-facing digital services

Select a real dataset from data.gov.uk that affects citizens directly
Use AI tools to generate a complete dashboard with data visualisation
Apply GOV.UK Design System patterns for consistent government presentation
Include relevant filtering
Success Criteria
Core Requirements

Live data consumption from actual data.gov.uk APIs or datasets
GOV.UK Design System compliance using appropriate components and patterns
Responsive visualization working effectively on mobile and desktop
Error handling with graceful fallbacks when APIs are unavailable
Accessibility compliance meeting WCAG 2.2 AA standards
Performance optimization with appropriate caching and loading states
Government-Specific Requirements

Clear service naming following GDS conventions for data services
Data source transparency with clear attribution and last-updated timestamps
Citizen-focused language explaining what the data means for users
Location-based filtering where geographically relevant
Export functionality allowing citizens to download relevant subsets
Update notifications or refresh mechanisms for time-sensitive data
Source Materials: data.gov.uk Datasets
Choose one (or more) of the published datasets at https://data.gov.uk on to build your dashboard.
Supporting Resources
The challenge can be approached using two complementary methodologies:
Approach 1: Prompt-Driven Development ("Vibe Coding")
This approach uses strong, comprehensive prompting to generate government data dashboards that consume real APIs and present data following government design patterns.
When to use: Rapid prototyping, straightforward data visualization, when you want immediate visual results with real data integration.
Meta-Prompting for Data Dashboard Planning
Before starting development, use AI tools to help you create the most effective prompt for your specific data visualization task.
"I need to create a UK government data dashboard that consumes live data from data.gov.uk
and presents it to citizens. Help me create a comprehensive prompt that will generate 
the best possible result from you.

The dashboard will show [air quality/transport/planning] data and needs to:
- Consume real APIs from data.gov.uk with proper error handling
- Follow GOV.UK Design System patterns for data presentation
- Meet WCAG 2.2 AA accessibility standards  
- Work offline-first with appropriate caching
- Present data in citizen-friendly language
- Include location-based filtering where relevant

What should I include in my prompt to ensure you understand all the government 
data presentation requirements and API integration constraints? Help me craft a prompt 
that will produce a complete, compliant data dashboard that handles real-world API 
challenges."


Benefits of meta-prompting:

Leverages AI knowledge of data visualization best practices
Creates prompts specific to government data presentation standards
Ensures proper consideration of API reliability and error states
Produces more robust data handling approaches
Addresses citizen accessibility needs from the start
Comprehensive Data Dashboard Prompts
Once you've completed your planning phase, use a single, comprehensive prompt to generate your initial dashboard. This is crucial because data dashboards require coordinated API handling, visualization, and error management that must work together from the foundation.
Example comprehensive prompt:
"You are building a UK government data dashboard to make this data.gov.uk dataset
accessible to citizens: [specify dataset and API endpoint].

REQUIREMENTS:
- Consume live data from the actual API endpoint provided
- Use GOV.UK Design System components for all UI elements
- Present data visualizations that are accessible to screen readers
- Include proper loading states, error handling, and offline fallbacks
- Use citizen-friendly language to explain what the data means
- Implement location-based filtering where geographically relevant
- Meet WCAG 2.2 AA accessibility standards throughout

CONSTRAINTS:
- Do not use custom charting libraries outside GOV.UK Frontend
- Handle API rate limiting and timeout scenarios gracefully  
- Do not assume reliable internet connectivity
- Cache data appropriately but show when information was last updated
- Design for mobile-first government service usage patterns

API INTEGRATION:
- Include proper attribution for data sources
- Handle different data formats (JSON, XML, CSV) as provided
- Implement appropriate refresh mechanisms for time-sensitive data
- Show clear error messages when data is unavailable
- Provide export functionality for citizen data portability

Create a complete dashboard including: service start page, data visualization interface, 
filtering controls, and data export functionality."


Approach 2: Spec-Driven Development
This approach creates executable specifications for data dashboards, following structured phases that ensure comprehensive API integration and government compliance.
When to use: Complex data integration, when you need reproducible dashboards across multiple datasets, or formal documentation for departmental reuse.
Setting Up Spec-Driven Data Dashboard Development
Phase 1: Dashboard Specification (/specify)
/specify Build a UK government data dashboard service that makes [specific data.gov.uk dataset]
accessible to citizens through a web interface.

The service must:
- Consume live data from data.gov.uk APIs with robust error handling
- Present visualizations following GOV.UK Design System patterns  
- Allow citizens to filter and explore data relevant to their location/needs
- Meet WCAG 2.2 AA accessibility standards for all visualizations
- Work effectively on mobile devices with limited connectivity
- Cache data appropriately while showing freshness indicators
- Provide clear explanations of what the data means for citizens
- Include export functionality for transparency and reuse

Citizens currently cannot easily access or understand this government data despite 
its relevance to their daily lives and decisions.


Phase 2: Technical Integration Planning (/plan)
/plan This government data dashboard must use:
- GOV.UK Design System components for all interface elements
- Progressive enhancement principles (works without JavaScript for core functionality)
- Accessible data visualization techniques (not just visual charts)
- Appropriate caching strategies for government API consumption
- Error handling that maintains service availability during API outages
- Mobile-first responsive design optimized for government service usage
- Semantic HTML structure that works with assistive technologies
- Performance budgets appropriate for citizen internet access patterns

API integration requirements:
- Respect rate limiting and implement appropriate backoff strategies
- Handle multiple data formats as provided by government sources
- Include proper attribution and data provenance information
- Implement data validation for citizen safety and accuracy


Phase 3: Task Implementation (/tasks) The tool will create structured tasks covering API integration, visualization development, accessibility testing, and error handling implementation.
Benefits of spec-driven approach:

Reproducible dashboards: Same specification works across different datasets
Comprehensive API handling: Forces consideration of all failure scenarios
Cross-departmental reuse: Creates templates other teams can adapt
Documentation: Formal specifications for compliance and maintenance
Systematic testing: Ensures all government requirements are verified
Hybrid Approach
Combine both methodologies for optimal results:

Use spec-driven for initial API integration architecture and error handling
Use prompt-driven for rapid visualization iteration and user interface refinement
Return to spec-driven for formal testing and cross-dataset template creation
Mini Prompt Library
Use these focused prompts for specific aspects of your data dashboard development:
API Integration Prompts
"Generate robust error handling for a government API that may have rate limits,
timeouts, and maintenance windows. Show loading states and fallback content 
that maintains service availability."

"Create caching logic for government data that balances freshness requirements 
with API reliability. Include clear timestamps showing when data was last updated."


Data Visualization Prompts
"Transform this raw government dataset into accessible visualizations using only
GOV.UK Design System components. Ensure charts work with screen readers and 
include data tables as alternatives."

"Create citizen-friendly explanations for this government data that explain what 
the numbers mean for people's daily lives, using plain English and avoiding 
technical jargon."


Mobile & Performance Prompts
"Optimize this data dashboard for mobile government service usage, assuming
limited bandwidth and older devices. Prioritize essential information and 
progressive disclosure."

"Implement offline-first patterns for a government data dashboard, ensuring 
citizens can still access cached information when connectivity is poor."


Things to Reflect on in Your Evaluation
During Development

API Understanding: How effectively did the AI understand the data structure and API constraints?
Error Handling: What prompting techniques worked best for robust error management?
Government Context: Where did you need to provide additional context about citizen needs?
Visualization Accessibility: How did the AI handle making data visualizations screen-reader friendly?
Performance Considerations: What aspects of mobile-first government service design required manual intervention?
Post-Completion

Citizen Value: How much more accessible is this data compared to raw datasets?
Technical Resilience: How well does the dashboard handle real-world API failures and connectivity issues?
Accessibility Compliance: Did AI-generated visualizations meet accessibility standards out-of-the-box?
Departmental Reusability: How easily could other teams adapt this approach for their datasets?
Team Discussion

Data Democracy: How could this approach democratize access to government data across departments?
Scaling Challenges: What aspects of government data visualization are hardest for AI to get right?
Operational Readiness: What safeguards would you need before deploying this to serve real citizens?
Cross-Government Impact: How might this change how departments think about publishing open data?
Citizen Engagement: What new opportunities does AI-powered data presentation create for government transparency?
