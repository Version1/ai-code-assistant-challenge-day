Level 1: PDF to Digital Service Transformation

Theme: AI-powered service digitisation and prompt engineering fundamentals


Challenge Overview
PDF forms create significant barriers for citizens and fail to meet government accessibility requirements. Under the Public Sector Bodies Accessibility Regulations 2018 (as amended in 2022) and Section 149 of the Equality Act 2010, government departments have a legal duty to ensure their digital services are accessible to all users, including those with disabilities.
The problem with PDFs:

Inherently inaccessible to screen readers and assistive technologies
Exclude citizens with disabilities from accessing services independently
Create friction for all users: download → print → complete by hand → scan/post → wait for response
No real-time validation, leading to incomplete applications and delays
Disproportionately impact vulnerable groups who most need government services
The opportunity: AI tools can rapidly transform these legacy processes into accessible, user-centred digital services that comply with WCAG 2.2 AA standards and follow proven government service design patterns - delivering better outcomes for citizens whilst meeting legal obligations.
The Challenge
Objective: Transform a legacy PDF form into a complete digital service

Take a real government PDF form that currently requires manual completion
Use AI tools to generate a fully functional digital equivalent
Apply government design standards and accessibility requirements
Include form validation, error handling, and submission workflows
Success Criteria
Core Requirements

Functional digital form that captures all data from the original PDF
GOV.UK Design System compliance using appropriate components and patterns
Accessibility compliance meeting WCAG 2.2 AA standards
Form validation with clear, helpful error messages
Progressive enhancement working without JavaScript
Responsive design working on mobile and desktop
Government-Specific Requirements

Clear service start page explaining the process
Check your answers page before submission
Confirmation page with reference number
Email confirmation capability (mocked/simulated)
Appropriate service naming following GDS conventions


Source Materials: UK Government PDF Forms
Choose one of these real, currently-used PDF forms to digitise:
Housing & Benefits

Housing Benefit Application Forms: Many councils still use PDF-based housing benefit claims
Council Tax Support Forms: Often combined with housing benefit in PDF format
Example sources:South Gloucestershire Housing Benefit Form
City of London Housing Benefit Application
Licensing & Permits

Event License Applications: Temporary event notices, premises licenses
Business License Forms: Street trading, alcohol licenses
Building Control Applications: Building regulations approval forms
Community Services

School Admission Forms: Many schools still use PDF application forms
Community Centre Bookings: Facility hire forms
Allotment Applications: Waiting list registrations


Supporting Resources
The challenge can be approached using two complementary methodologies:
Approach 1:  Prompt-Driven Development ("Vibe Coding")
This approach uses strong, comprehensive prompting combined with AI tools' internal planning capabilities to generate government services directly.
When to use: Quick prototypes, straightforward forms, when you want rapid iteration and immediate results.
Meta-Prompting for Planning
Before starting development, use AI tools to help you create the most effective prompt for your specific task. Ask the AI to help you write an excellent prompt that will get the most out of itself.
"I need to digitise a UK government PDF form into a GOV.UK digital service. Help me create
a comprehensive prompt that will generate the best possible result from you. 

The form is for [housing benefit/licensing/etc] and needs to:
- Follow GOV.UK Design System patterns
- Meet WCAG 2.2 AA accessibility standards
- Work without JavaScript (progressive enhancement)
- Include proper validation and error handling

What should I include in my prompt to you to ensure you understand all the government 
requirements and constraints? Help me craft a prompt that will produce a complete, 
compliant digital service on the first attempt."

Benefits of meta-prompting:

Leverages the AI's knowledge of its own capabilities and limitations
Creates prompts tailored to the specific AI tool you're using
Ensures you include all necessary context and constraints
Produces more targeted and effective generation prompts
Reduces trial-and-error in prompt crafting
Comprehensive Initial Prompts
Once you've completed your planning phase, use a single, comprehensive prompt to generate your initial codebase. This approach is crucial because AI tools tend to rebuild projects from scratch when given major new requirements, so it's essential to establish all constraints, requirements, and expectations upfront.
Why comprehensive prompts work better:

Prevents the need to retrofit accessibility, design system compliance, or technical constraints
Reduces major rework cycles that waste time and break existing functionality
Ensures the foundation is solid from the first generation
Allows for refinement rather than reconstruction
Example:
"You are building a UK government digital service to replace this PDF form: [attach or describe the actual PDF form].

REQUIREMENTS:
- Use GOV.UK Design System components only
- Must meet WCAG 2.2 AA accessibility standards from the start
- Follow progressive enhancement (works without JavaScript)
- Mobile-first responsive design
- Government-appropriate language and error messaging
- Include proper form validation and error handling

CONSTRAINTS:
- Do not use custom CSS outside GOV.UK Frontend
- Do not suggest frameworks or build tools
- Do not create components that already exist in the design system
- Do not assume users have high-speed internet or modern devices

Create a complete service including: start page, form pages, check answers page, and confirmation page."

Approach 2: Spec-Driven Development
This approach creates executable specifications that generate working implementations, following structured phases from intent to code.
When to use: Complex services, when you need reproducible results, multiple implementation variations, or formal documentation requirements.
Setting Up Spec-Driven Development
Many AI development tools now support spec-driven approaches. For example, using GitHub's Spec-Kit methodology:
Phase 1: Specification (/specify)
/specify Build a UK government digital service to replace [specific PDF form].

The service must:
- Allow citizens to submit [housing benefit/licensing/community service] applications online
- Follow complete GOV.UK service design patterns from start page through confirmation
- Meet WCAG 2.2 AA accessibility standards throughout
- Support progressive enhancement (work without JavaScript)
- Handle form validation and error messaging appropriately
- Provide check-answers functionality before submission
- Generate confirmation pages with reference numbers

Citizens currently must download, print, complete by hand, and post this form back to the council.

Phase 2: Technical Planning (/plan)
/plan This government service must use:
- GOV.UK Design System components only
- Progressive enhancement principles (vanilla HTML/CSS/JS)
- No custom frameworks or build tools
- Mobile-first responsive design
- Government-appropriate language and tone
- Proper semantic HTML structure for accessibility
- Form validation that works server-side and client-side
- Error messaging following GDS patterns

Phase 3: Task Implementation (/tasks) The tool will create structured tasks for implementation, ensuring all government requirements are systematically addressed.
Benefits of spec-driven approach:

Reproducible results: Same specification generates consistent implementations
Comprehensive planning: Forces consideration of all government requirements upfront
Multiple variations: Can generate different technical implementations from same spec
Documentation: Creates formal specifications for compliance and handover
Systematic coverage: Ensures no government standards are missed
Hybrid Approach
You can combine both methodologies:

Use spec-driven for initial architecture and comprehensive planning
Use prompt-driven for rapid iteration and refinement
Return to spec-driven for formal documentation and compliance verification


Things to reflect on in your evaluation
During Development

Which prompting style did you select?
Which tool did you select?
How effectively did the AI understand your specific requirements?
What prompting techniques worked best for design system compliance?
Where did you need to provide additional context or examples?
How did the AI handle complex form validation logic?
Post-Completion

User experience: How much better is this than the original PDF process?
Technical quality: What aspects required the most manual intervention?
Accessibility: Did AI-generated code meet accessibility standards out-of-the-box?
Maintainability: How readable and maintainable is the generated code?
Team Discussion

What surprised you about AI's ability to handle these requirements?
Which aspects of government service design are hardest for AI to get right?
How could this approach scale across your organisation?
What safeguards would you need for production use? For this type of use, how important does 
