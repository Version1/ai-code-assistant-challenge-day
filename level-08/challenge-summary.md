# Level 8: Adaptive Testing Strategy and Risk-Based Quality Engineering

Test your government service the way real citizens will use it.

## What this challenge is about

You have built a government digital service. Now you need to find out if it actually works for the people who will depend on it.

Generic testing templates check whether features work. They do not check whether your service works for a citizen completing a benefits application on their phone while facing an eviction deadline. Or for someone using a screen reader in a library with unreliable wifi.

Government services serve people who cannot afford failures. A broken checkout on a shopping site is frustrating. A broken benefits application can mean missed rent payments.

This challenge asks you to use AI tools to develop testing that investigates how your specific service could fail for different citizen groups.

## Why this matters

The Government Service Standard requires you to:

- Test the end-to-end service (Point 10)
- Make the service simple to use (Point 4)

The 2024 Central Digital and Data Office Service Assessment Report found a critical gap: testing that validates technical compliance but misses real user failure modes.

Your service needs testing that explores actual citizen contexts, not just technical requirements.

## What you will do

1. Choose the government service you built in Level 1, 2, or 3
2. Use AI tools to analyse the specific risks and failure modes for your service
3. Create investigative testing that explores how different citizens would experience your service
4. Build practical tests covering the failure scenarios most critical to your users

## Choose your service

Pick one application you have already built.

### Level 1: PDF to Digital Service

Your testing should investigate:

- Form completion under deadline pressure (facing eviction, benefit deadlines)
- Accessibility across varying technical skills
- Error recovery when applications are partially completed
- Document submission for citizens without scanners or smartphones

### Level 2: Data Dashboard

Your testing should investigate:

- Data comprehension across different literacy levels
- Mobile usage on older devices with limited data plans
- Critical decision-making based on the information displayed
- Screen reader and assistive technology access

### Level 3: Enquiry Management

Your testing should investigate:

- Enquiry submission during crisis situations
- Response time expectations and follow-up handling
- Staff workflow during peak demand periods
- Citizen understanding of data privacy

## What government service testing must consider

Citizens using your service have different:

- **Technical capabilities** - digital literacy levels, device access, connectivity quality
- **Accessibility needs** - assistive technologies, visual or cognitive requirements
- **Circumstances** - stress levels, time pressure, competing demands
- **Stakes** - consequences of service failure (some citizens cannot afford mistakes)
- **Environments** - libraries, mobile phones, shared computers, poor wifi

Your testing strategy should explore how your service performs across these variations.

## Success criteria

Your testing strategy must demonstrate:

**Service-specific focus**
- Clear identification of failure modes critical to your chosen service
- Testing tailored to actual risks, not generic templates

**Citizen context coverage**
- Testing for different circumstances, capabilities, and environments
- Specific attention to citizens with highest stakes

**Practical implementation**
- Working tests covering critical failure scenarios
- Systematic investigation of ways your service could fail

**Government requirements**
- Accessibility validation for your service
- Performance under realistic operational conditions

## Approaches to consider

### AI-assisted risk-based testing

Use AI tools to analyse your specific service and generate testing that explores unique failure modes for different citizen groups.

Works well when your service has diverse users, complex journeys, or high-stakes outcomes.

### Spec-driven testing strategy

Create structured specifications for adaptive testing that can be systematically applied.

Works well when you need formal testing documentation or systematic coverage requirements.

### Hybrid approach

Combine AI risk analysis with structured specifications for comprehensive coverage.

## What to do next

Choose which of your Level 1, 2, or 3 services to test, then use AI tools to analyse its specific risks and citizen contexts.
