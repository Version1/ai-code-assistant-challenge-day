# Kiro Playbook: Data Processing and Visualisation

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for this specific challenge.

## Mode recommendation: Spec Mode

Use Spec Mode for this challenge. Here is why:

- Data.gov.uk APIs vary in reliability and format - you need documented error handling
- Accessible visualisations require explicit acceptance criteria you can test against
- Caching and offline strategies need design decisions captured upfront
- Government compliance requires traceability from requirement to implementation

Vibe Mode works for experimenting with chart layouts, but use Spec Mode for your data architecture and accessibility approach.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory and adapt for your chosen dataset.

### product.md

```markdown
# Product Context

## What this service does
Transforms raw [DATASET NAME] data from data.gov.uk into an accessible dashboard
that helps citizens understand [WHAT THE DATA SHOWS] in their area.

## Who uses this service
- Citizens checking [DATA TYPE] in their local area
- Users of assistive technologies (screen readers, voice control, magnification)
- Users on mobile devices with intermittent connectivity
- Users with low data literacy who need plain English explanations

## Service standards
This service must meet:
- GOV.UK Service Standard
- WCAG 2.2 Level AA
- Public Sector Bodies Accessibility Regulations 2018

## Design principles
- Data without context is noise: every visualisation needs plain English explanation
- Tables are the accessible default: charts enhance, tables inform
- Stale data is worse than no data: always show when data was last updated
- Offline-first: cached data beats loading spinners
```

### tech.md

```markdown
# Technical Standards

## API handling
- Use a proxy to handle CORS (data.gov.uk does not allow direct browser requests)
- Implement retry logic: 3 attempts with exponential backoff
- Cache responses: 15 minutes minimum, longer for rarely-updated datasets
- Never fail silently: always tell users when data is unavailable

## Visualisation requirements
- Every chart must have a data table alternative (toggle or adjacent)
- Charts must work without colour alone (patterns, labels, or both)
- Minimum touch target: 44x44px for interactive elements
- Responsive: charts must be readable on 320px viewport

## GOV.UK Design System
- Use GOV.UK Frontend 5.x for all non-chart components
- Follow typography scale and colour palette for charts
- Error messages follow GDS patterns
- Loading states use GOV.UK spinner pattern

## Offline support
- Service worker caches last successful API response
- Show cached data with "Last updated" timestamp when offline
- Clear indication when showing cached vs live data

## Data attribution
- Every page shows data source with link to original dataset
- Last updated timestamp visible without scrolling
- Open Government Licence acknowledgement in footer
```

## Hooks for this challenge

Save these in `.kiro/hooks/` to catch common problems automatically.

### accessibility-check.yaml

```yaml
name: accessibility-check
event: file_saved
match: "**/*.{js,jsx,ts,tsx,njk,html}"
prompt: |
  Review this file for visualisation accessibility issues:
  - Charts without data table alternatives
  - Colour-only data differentiation (needs patterns or labels)
  - Missing axis labels or chart titles
  - Interactive elements smaller than 44x44px
  - Images or canvas elements without text alternatives
  - Focus indicators missing on interactive charts
  Report issues with line numbers and suggested fixes.
```

### govuk-patterns.yaml

```yaml
name: govuk-patterns
event: file_saved
match: "**/*.{njk,html,css}"
prompt: |
  Check this file follows GOV.UK patterns:
  - Typography uses GDS scale (16, 19, 24, 36, 48px)
  - Colours from GOV.UK palette only
  - Focus states visible (yellow background, black border)
  - Error summary pattern for any validation failures
  - Page has exactly one h1
  - Heading hierarchy logical (no skipped levels)
  Flag deviations with the correct GOV.UK pattern to use.
```

## Starting your spec

These prompts help you get useful requirements. Adapt them for your dataset.

### Opening prompt for initial spec

> I am building a citizen dashboard using [DATASET NAME] from data.gov.uk. The data shows [WHAT IT CONTAINS]. Citizens need to understand [USER NEED].
>
> The dashboard needs: landing page explaining the data, visualisation with filtering, data table view, and clear data attribution.
>
> Please create a spec for this service. Start with the data flow - how we fetch, cache, and display the data.

### Prompt for error handling requirements

> The data.gov.uk API may be slow, return errors, or be temporarily unavailable. Add requirements for:
> - Loading states while fetching data
> - Error states when API fails (with retry option)
> - Cached data fallback when offline
> - Clear messaging about data freshness
>
> For each state, specify what the user sees and what actions they can take.

### Prompt for visualisation accessibility

> Add explicit accessibility acceptance criteria for the visualisation:
> - The data table alternative and how users access it
> - How colour-blind users distinguish data series
> - Keyboard navigation through chart elements
> - What screen readers announce for each data point
> - Touch target sizes for mobile users
>
> Reference WCAG 2.2 success criteria where relevant.

### Prompt for caching and offline

> Add requirements for offline support:
> - What data is cached and for how long
> - How users know they are viewing cached data
> - What happens when cached data expires
> - How the service recovers when connectivity returns
>
> Specify the user experience for each scenario.

## Gotchas specific to this challenge

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| CORS blocks API calls | Browser security blocks cross-origin requests | Set up a proxy server from day one |
| Charts fail accessibility audit | Libraries default to colour-only differentiation | Require "works without colour" in every chart requirement |
| Stale data confuses users | Cached data displays without timestamp | Add "show last updated time" to every data display requirement |
| Mobile charts unreadable | Complex charts do not scale down | Require "readable at 320px viewport" and test early |
| Touch targets too small | Chart libraries create tiny interactive elements | Specify "44x44px minimum" in tech.md |
| No fallback when API fails | Happy path dominates implementation | Write error handling requirements before success requirements |
| Data tables as afterthought | Charts built first, tables added late | Require "data table as primary, chart as enhancement" |
| Loading states missing | Fast local development hides slow API | Add artificial delay during development to test loading states |

## Quality checkpoints

### After requirements phase

- [ ] Error states documented for every API interaction
- [ ] Data table requirements exist for every visualisation
- [ ] Accessibility acceptance criteria reference specific WCAG criteria
- [ ] Caching behaviour specified with clear user messaging

### After design phase

- [ ] Design includes loading, error, cached, and success states
- [ ] Colour choices work for colour-blind users
- [ ] Mobile and desktop layouts both specified
- [ ] Data attribution placement decided

### During implementation

- [ ] Proxy server working before any API calls
- [ ] Error handling implemented before happy path
- [ ] Data table built before or alongside chart
- [ ] Touch targets tested on actual mobile device

### Before submission

- [ ] Works with JavaScript disabled (shows data table at minimum)
- [ ] Works offline (shows cached data with clear messaging)
- [ ] Passes automated accessibility checks (axe, WAVE)
- [ ] Tested with screen reader (VoiceOver or NVDA)
- [ ] Loading states visible (test with network throttling)
- [ ] Last updated timestamp visible on all data displays

## Reflection questions

When you finish, consider:

- Did your data table end up as an afterthought despite your intentions?
- Which error states did you discover only through testing?
- How did spec-driven requirements affect your accessibility compliance?
- What API behaviours surprised you that the spec did not anticipate?
- What would you add to your steering files for your next data dashboard?
