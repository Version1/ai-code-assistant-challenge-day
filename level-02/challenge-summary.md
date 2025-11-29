# Level 2: Data Processing and Visualisation

Transform government open data into dashboards that citizens can actually use.

## What you will build

A working dashboard that takes real data from data.gov.uk and presents it in a way that helps citizens understand information that affects their lives.

## Why this matters

Government departments publish vast amounts of open data through data.gov.uk. Under the UK's Open Government Licence and the Public Sector Information Directive, departments have committed to making public data "findable, accessible, interoperable and reusable" (FAIR principles).

But raw data remains largely inaccessible to the citizens who could benefit from it most.

**Current problems with government data access:**

- Raw datasets require technical expertise to interpret
- No standardised presentation layer across government sources
- Citizens cannot easily find relevant local information (air quality, transport delays, planning applications)
- Data exists in silos, preventing meaningful cross-departmental insights
- Mobile-unfriendly formats exclude citizens accessing services on the go
- No real-time updates or alerts for time-sensitive information

**The opportunity:** AI tools can rapidly transform government open data into accessible, real-time dashboards. You will create a visualisation layer that any department could use to make their data.gov.uk datasets citizen-ready.

## Your objective

Build a deployable government data dashboard that transforms raw data.gov.uk datasets into citizen-facing digital services.

You will:

- Select a real dataset from data.gov.uk that affects citizens directly
- Use AI tools to generate a complete dashboard with data visualisation
- Apply GOV.UK Design System patterns for consistent government presentation
- Include relevant filtering options

## Success criteria

### Core requirements

Your dashboard must demonstrate:

- **Live data consumption** - connect to actual data.gov.uk APIs or datasets
- **GOV.UK Design System compliance** - use appropriate components and patterns
- **Responsive visualisation** - work effectively on mobile and desktop
- **Error handling** - graceful fallbacks when APIs are unavailable
- **Accessibility compliance** - meet WCAG 2.2 AA standards
- **Performance optimisation** - appropriate caching and loading states

### Government-specific requirements

Your dashboard must also include:

- **Clear service naming** - follow GDS conventions for data services
- **Data source transparency** - clear attribution and last-updated timestamps
- **Citizen-focused language** - explain what the data means for users
- **Location-based filtering** - where geographically relevant
- **Export functionality** - allow citizens to download relevant subsets
- **Update notifications** - refresh mechanisms for time-sensitive data

## Finding your dataset

Choose one or more published datasets from [data.gov.uk](https://data.gov.uk) to build your dashboard.

Look for datasets that:

- Affect citizens directly
- Update regularly
- Have clear geographic or demographic relevance
- Would benefit from visualisation

## Approaches you can take

### Prompt-driven development

Use strong, comprehensive prompting to generate government data dashboards that consume real APIs and present data following government design patterns.

**Best for:** Rapid prototyping, straightforward data visualisation, when you want immediate visual results with real data integration.

### Spec-driven development

Create executable specifications for data dashboards, following structured phases that ensure comprehensive API integration and government compliance.

**Best for:** Complex data integration, reproducible dashboards across multiple datasets, formal documentation for departmental reuse.

### Hybrid approach

Combine both methodologies:

1. Use spec-driven for initial API integration architecture and error handling
2. Use prompt-driven for rapid visualisation iteration and user interface refinement
3. Return to spec-driven for formal testing and cross-dataset template creation

---

*Detailed implementation guidance for each approach is available in the separate playbook documents.*
