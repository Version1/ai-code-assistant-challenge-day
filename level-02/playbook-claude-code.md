# Claude Code Playbook: Data Processing and Visualisation

Your starter kit for building government data dashboards. For Claude Code basics, see [Getting Started](../getting-started-claude-code.md).

---

## Challenge-specific CLAUDE.md

Copy this into your project's CLAUDE.md before you start. It sets expectations for every prompt.

```markdown
## Project: Government Data Dashboard

Transform data.gov.uk datasets into citizen-facing visualisations.

### API handling standards
- Implement retry logic with exponential backoff (3 attempts, 1s/2s/4s delays)
- Cache responses locally to reduce API calls and handle offline scenarios
- Log all API errors with timestamps for debugging
- Provide meaningful fallback content when APIs are unavailable

### data.gov.uk specifics
- Base URL: https://data.gov.uk/api/action/
- Rate limiting: respect 429 responses, implement backoff
- Expect inconsistent date formats across datasets (ISO, UK format, Unix timestamps)
- Some endpoints return CSV, others JSON - handle both

### GOV.UK Design System requirements
- Use govuk-frontend components throughout
- Follow the service manual layout patterns
- Include phase banner (alpha/beta as appropriate)
- Footer must include OGL licence and data.gov.uk attribution

### Accessibility requirements for visualisations
- Every chart needs a data table alternative (visible or accessible)
- Colour alone must not convey meaning - use patterns or labels
- Screen reader announcements for dynamic data updates
- Minimum touch target size 44x44px on interactive elements
- All charts need descriptive titles and axis labels

### File organisation
src/
  services/         # API clients with retry logic
  components/       # Reusable UI and chart components
  utils/            # Date parsing, data transformation
  hooks/            # Data fetching with caching (if React)
```

---

## Custom slash commands

Save these files in `.claude/commands/` for quick access during the challenge.

### `.claude/commands/a11y-chart-review.md`

```markdown
---
description: Check visualisation accessibility against WCAG 2.2 AA
---

Review $ARGUMENTS for visualisation accessibility. Check these specific requirements:

**Data table alternatives:**
- Is there a table showing the same data as the chart?
- Is the table accessible (proper headers, scope attributes)?
- Can users switch between chart and table views?

**Colour independence:**
- Does the chart use patterns, labels, or textures alongside colour?
- Do adjacent colours have sufficient contrast?
- Would the chart make sense in greyscale?

**Screen reader support:**
- Does the chart have a descriptive title and summary?
- Are axis labels and data points announced meaningfully?
- Do dynamic updates use aria-live regions?

**Keyboard and touch:**
- Can users navigate data points with keyboard?
- Are interactive elements at least 44x44px?
- Do tooltips work with keyboard focus?

Report each issue with the WCAG criterion violated and specific fix needed.
```

### `.claude/commands/api-resilience-check.md`

```markdown
---
description: Review API error handling and resilience patterns
---

Review $ARGUMENTS for API resilience. Check:

**Retry logic:**
- Does the code retry failed requests?
- Is there exponential backoff (not hammering the API)?
- Is there a maximum retry limit?

**Error handling:**
- Are different error types handled (network, 4xx, 5xx)?
- Do users see helpful messages, not technical errors?
- Are errors logged for debugging?

**Offline support:**
- Is there local caching of successful responses?
- Does the UI show cached data when API fails?
- Is "last updated" timestamp displayed?

**Loading states:**
- Do users see loading indicators during requests?
- Is there skeleton content to prevent layout shift?
- Can users still interact with cached data while refreshing?

For each gap, explain the risk and provide implementation guidance.
```

---

## Model recommendations

| Task | Model | Why |
|------|-------|-----|
| API service layer | Sonnet | Handles standard patterns quickly |
| Chart component generation | Sonnet | Fast iteration on visual components |
| Complex data transformation | Opus | Better at edge cases and validation |
| Accessibility audit | Opus | More thorough, catches subtle issues |
| Error boundary implementation | Sonnet | Straightforward pattern application |
| Performance optimisation | Opus | Understands caching trade-offs |

**Switch with `/model`** - use Sonnet for speed, Opus for depth.

---

## Effective prompts for this challenge

**API service layer with resilience:**
> "Create an API service for data.gov.uk that includes: retry logic with exponential backoff (max 3 attempts), response caching with 5-minute TTL, proper error typing for network/4xx/5xx errors, and TypeScript interfaces for the response data. The service should work offline by returning cached data when available."

**Accessible chart component:**
> "Create a bar chart component that displays [dataset]. Include: a data table alternative that screen readers can access, patterns or labels that work without colour, keyboard navigation between data points, and aria-live announcements when data updates. Use Chart.js but override its accessibility defaults."

**Offline-first data layer:**
> "Implement a data fetching hook that: checks localStorage cache first, fetches from API if cache is stale (over 5 minutes old), updates cache on successful fetch, falls back to stale cache if API fails, and exposes loading/error/lastUpdated state. Show 'Data from [timestamp]' when using cached data."

**Error boundaries with GOV.UK styling:**
> "Create an error boundary component using GOV.UK Design System styling. Show the standard error page pattern with: a clear heading explaining something went wrong, guidance on what users can do, a way to retry the action, and a 'last working data' fallback where possible. Log errors to console with full stack traces."

**Location filter with autocomplete:**
> "Build a location filter using the GOV.UK accessible autocomplete component. It should: search UK postcodes and local authority names, handle the inconsistent location formats in data.gov.uk (some use LA codes, some use names), show 'No results' gracefully, and filter the dashboard data when a location is selected."

---

## Tips and gotchas

### data.gov.uk API gotchas

| Issue | What to do |
|-------|------------|
| CORS errors in browser | Use a backend proxy or serverless function - direct browser calls often blocked |
| Inconsistent date formats | Parse defensively with fallbacks - ISO, UK format (DD/MM/YYYY), and Unix timestamps all appear |
| Rate limiting (429 errors) | Implement backoff and cache aggressively - no published rate limits, but they exist |
| Large datasets | Request pagination or use LIMIT parameters - some endpoints return millions of rows |
| Stale data | Check metadata for update frequency - some "live" datasets update monthly |

### GOV.UK Frontend gotchas

| Issue | What to do |
|-------|------------|
| Styles not loading | Import the full CSS or check you have the right SCSS setup |
| JavaScript components not initialising | Call `initAll()` after DOM ready or component render |
| Build errors with Nunjucks | Use HTML templates if your framework does not support Nunjucks macros |

### Accessibility gotchas

| Issue | What to do |
|-------|------------|
| Chart.js not accessible by default | Must add custom plugins for keyboard nav and screen reader support |
| Dynamic content not announced | Wrap updating content in aria-live regions |
| Colour-only legends | Add patterns, direct labels, or accessible legend alternatives |
| Missing chart descriptions | Every visualisation needs a text summary of what it shows |

### Caching gotchas

| Issue | What to do |
|-------|------------|
| localStorage limits | Compress data or use IndexedDB for larger datasets |
| Stale cache served forever | Always show "last updated" so users know data age |
| Cache invalidation | Clear cache when user explicitly refreshes, not just on page load |

---

## Reflection questions

After completing the challenge, consider:

- How did you handle the gap between "live data" expectations and actual API reliability?
- What accessibility issues did Chart.js (or your charting library) create that you had to fix?
- Where did cached data help user experience versus create confusion about data freshness?
- What would you add to CLAUDE.md for a similar project?
- How much prompt iteration did the chart accessibility requirements need?
- Would a spec-driven approach have helped with the API integration complexity?
