# Level 4: Legacy Code Modernisation

Transform an undocumented government desktop application into a modern web service using AI-assisted analysis.

## What you will do

You will modernise a VB.NET Parliamentary Question tracking system - a deliberately legacy application with no documentation, poor coding practices, and business logic buried in form event handlers.

Your task is to:

1. Use AI tools to analyse and understand the undocumented codebase
2. Extract and document the embedded business rules
3. Rebuild it as a modern, accessible web application
4. Preserve every piece of functionality from the original

## Why this matters

Government departments spend up to 60% of technology budgets maintaining legacy systems rather than building new services. These ageing desktop applications:

- run on deprecated technologies that vendors no longer support
- contain undocumented business logic that walks out the door when staff leave
- cannot connect to modern platforms like GOV.UK One Login
- fail current accessibility standards and exclude remote workers
- create security risks through outdated dependencies
- block data sharing across departments

The Government Digital and Data Strategy identifies legacy technical debt as a primary barrier to digital transformation. AI tools offer a way to rapidly analyse these systems, extract institutional knowledge, and generate modern replacements.

## The source application

**Repository:** see [App Mode application](../app-mod-challenge)

A VB.NET Windows Forms application that tracks Parliamentary Questions. It was built as a training exercise with authentic technical debt:

- No README, comments, or documentation of any kind
- Business logic embedded directly in form event handlers
- Mixed naming conventions and hardcoded values throughout
- Simple file-based storage with no backup capability
- Runs only on Windows

## What success looks like

**Preserve all functionality**
Every feature in the legacy application must work in your modern version. Nothing gets lost in translation.

**Document the business logic**
Create clear documentation of government-specific rules - PQ deadline calculations, reference number formats, workflow requirements.

**Build for modern standards**
Use a contemporary framework with proper separation of concerns. The application must work on mobile and desktop, and be compatible with screen readers.

**Plan for data migration**
Show how existing data would move to your modern storage solution.

**Handle errors gracefully**
Include robust input validation and error messages that help users fix problems.

## Approaches you might take

This challenge requires understanding before rebuilding. You cannot modernise what you do not understand.

### Prompt-driven development

Use AI tools as archaeological instruments - systematically analysing the legacy codebase, asking questions about what you find, and building understanding piece by piece before generating modern equivalents.

Works well when: The legacy system contains complex domain knowledge and business continuity matters more than speed.

### Spec-driven development

Create formal specifications for the modernisation, working through structured phases with documented outputs at each stage.

Works well when: Stakeholders need to review and approve the approach, or when you need audit trails for complex government systems.

### Combining approaches

Start with prompt-driven analysis to understand what you are dealing with. Use spec-driven methods for formal planning and sign-off. Return to prompt-driven development for implementation.

---

This document summarises the challenge. For detailed guidance on how to approach the work, see the implementation guides in this repository.
