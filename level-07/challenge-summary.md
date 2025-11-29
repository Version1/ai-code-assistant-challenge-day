# Level 7: Performance Investigation and System Resilience

## What you will do

You will investigate a performance incident that brought down a council booking service. Your job is to find the real cause - not the obvious one - and design monitoring that would catch similar problems before citizens are affected.

This challenge tests whether AI tools can help you analyse complex performance data and spot patterns that manual investigation would miss.

## Why this matters

Government services must work when citizens need them. Tax deadlines, school applications, benefit renewals - these all create peak demand that services must handle reliably.

The Central Digital and Data Office found that performance failures hit vulnerable citizens hardest. When manual investigation takes hours, citizens who depend on digital services are locked out.

**Common problems with reactive performance management:**

- Investigation starts after citizens are already affected
- Obvious symptoms point toward wrong solutions
- Teams scale infrastructure when the real problem is elsewhere
- Same types of incidents keep happening
- No systematic way to learn from failures

## The incident you will investigate

A Local Council Community Centre Booking System went down on Monday 15th January 2025, from 9:00 AM to 2:00 PM.

**What happened:**
- Page loads went from 2 seconds to over 45 seconds
- Bookings started failing
- Citizens complained on social media and to the service desk

**What the surface data shows:**
- Database connections exhausted
- Memory pressure warnings
- CPU spikes

**What you need to find:**
The true root cause. The materials contain red herrings pointing toward obvious scaling solutions. The actual problem requires careful analysis across multiple data sources.

## What success looks like

**Find the root cause**

Identify the actual problem through systematic analysis, not the surface symptoms.

**Connect the evidence**

Show how infrastructure metrics, application behaviour, and citizen impact relate to each other.

**Design better monitoring**

Create a monitoring approach that would have detected this issue before citizens noticed.

**Build in resilience**

Recommend changes that prevent this class of problem, not just this specific incident.

**Make it reusable**

Document your investigation method so others can apply it to different incidents.

## Source materials

All materials are in the `performance-challenge/` folder.

### Logs

Located in `performance-challenge/logs/`:

| File | Contains |
|------|----------|
| `app.log` | Application errors and resource warnings |
| `db.log` | Query times, connection pool metrics, contention data |
| `access.log` | Request patterns, response codes, user behaviour |

### Monitoring data

Located in `performance-challenge/monitoring/`:

| File | Contains |
|------|----------|
| `metrics.csv` | CPU, memory, network, response times at 5-minute intervals |
| `dashboard-data.json` | Booking success rates, search performance |
| `alerts.json` | System alerts during the incident |

### Citizen impact

Located in `performance-challenge/citizen-impact/`:

| File | Contains |
|------|----------|
| `service-desk-tickets.json` | Citizen complaints with timestamps |
| `social-media-mentions.txt` | Public response to service issues |

## Approaches to consider

### Prompt-driven investigation

Use AI tools to analyse incident data, correlate sources, and identify root causes through pattern recognition.

Works well when you need to move quickly through complex data with non-obvious causes.

### Spec-driven investigation

Create structured specifications for each investigation phase and monitoring design.

Works well when you need formal documentation or are building monitoring for others to implement.

### Combined approach

Use prompt-driven methods for the forensic investigation, then spec-driven methods for designing monitoring architecture.

## Government context

This challenge reflects the Government Service Standard (Point 8: performance must meet user needs) and Technology Code of Practice (Point 9: monitoring and incident response).

Your recommendations should work for:

- Different council services with similar patterns
- Teams with varying technical expertise
- Services that cannot afford extended downtime
- Organisations that need to justify infrastructure spending with evidence
