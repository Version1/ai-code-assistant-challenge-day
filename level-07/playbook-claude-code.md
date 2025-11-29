# Claude Code Playbook: Performance Investigation and System Resilience

Your starter kit for investigating performance incidents and designing better monitoring. For Claude Code basics, see [Getting Started](../getting-started-claude-code.md).

---

## Challenge-specific CLAUDE.md

Copy this into your project's CLAUDE.md before you start.

```markdown
## Project: Performance Incident Investigation

Finding the root cause of a council booking service outage, not just the obvious symptoms.

### Data sources and their purpose

**Logs (performance-challenge/logs/):**
- `app.log` - Application errors, resource warnings, error timestamps
- `db.log` - Query execution times, connection pool state, lock contention
- `access.log` - Request patterns, response codes, user journey failures

**Monitoring (performance-challenge/monitoring/):**
- `metrics.csv` - Infrastructure metrics at 5-minute intervals (CPU, memory, response times)
- `dashboard-data.json` - Business metrics (booking success rates, search performance)
- `alerts.json` - System alerts with thresholds and trigger times

**Citizen impact (performance-challenge/citizen-impact/):**
- `service-desk-tickets.json` - Citizen complaints with timestamps
- `social-media-mentions.txt` - Public response and timing

### Timestamp correlation rules
Different sources use different formats. When correlating:
- Logs: ISO format (2025-01-15T09:23:45Z)
- Metrics CSV: Unix timestamps or HH:MM format
- Alerts JSON: ISO format with timezone
- Service desk: Human-readable ("9:45 AM")

Always convert to a single format before building timelines. Look for events within 1-2 minute windows, not exact matches.

### Red herring awareness
Surface symptoms that are NOT root causes:
- High memory usage (symptom of something else)
- CPU spikes (reaction to load)
- Database connection exhaustion (consequence, not cause)
- Citizen complaints (lag actual events by 10-30 minutes)

The root cause is what CHANGED to trigger the cascade. Ask: "What was different before this started?"

### Root cause investigation pattern
1. Establish baseline - what did normal look like before the incident?
2. Find first anomaly - not the worst, the FIRST deviation from baseline
3. Build causation chain - what did that first anomaly cause?
4. Verify hypothesis - does the timeline support cause-before-effect?
```

---

## Custom slash commands

Save these files in `.claude/commands/`.

### `.claude/commands/correlate-timeline.md`

```markdown
---
description: Build correlated timeline across all performance data sources
---

Build a correlated incident timeline from all available data sources.

**For each data source:**
1. Extract all events with timestamps from the incident window (09:00-14:00 on 15 January 2025)
2. Convert timestamps to consistent ISO format
3. Note what each event represents (metric change, error, alert, citizen complaint)

**Build the timeline:**
- Order all events chronologically
- Mark each event as: CAUSE (triggered something else), SYMPTOM (result of something else), or UNKNOWN
- Note time gaps between related events
- Identify the FIRST anomaly that deviates from baseline

**Correlation questions to answer:**
- Which event appears first in the data?
- What happens in other data sources within 2 minutes of each event?
- Do citizen complaints match service degradation timestamps?
- Is there a clear cascade pattern (A triggers B triggers C)?

**Output:**
Chronological timeline with event type, source, timestamp, and cause/symptom classification.
```

### `.claude/commands/identify-anomalies.md`

```markdown
---
description: Statistical analysis to identify baselines and anomalies in metrics
---

Analyse the metrics data to establish baselines and identify statistically significant anomalies.

**Baseline establishment:**
For each metric (CPU, memory, response time, success rate):
1. Calculate mean and standard deviation from pre-incident data
2. Define "normal" as within 2 standard deviations of mean
3. Document what "healthy" looks like for this service

**Anomaly detection:**
For each metric during the incident window:
1. Find the first point that exceeds 2 standard deviations from baseline
2. Calculate how far outside normal the peak values went
3. Note the duration of the anomaly

**Pattern analysis:**
- Which metric deviated first?
- Is there a leading indicator that predicts other failures?
- Do anomalies correlate with specific request patterns?

**Output:**
Table of metrics with baseline values, first anomaly timestamp, peak deviation, and recovery time.
```

---

## Model recommendations

| Task | Model | Why |
|------|-------|-----|
| Initial data exploration | Sonnet | Fast pattern recognition across large files |
| Timeline construction | Sonnet | Mechanical correlation work |
| Statistical baseline analysis | Sonnet | Calculation-heavy, pattern-based |
| Root cause hypothesis | Opus | Requires reasoning about causation chains |
| Challenging red herrings | Opus | Needs to distinguish correlation from causation |
| Monitoring architecture design | Opus | Complex trade-off decisions |

**Switch with `/model`** - use Sonnet to explore data quickly, switch to Opus when forming and testing hypotheses.

---

## Effective prompts for this challenge

**Finding the first anomaly (not the worst):**
> "Analyse metrics.csv and find the FIRST metric that deviated from its baseline, not the metric with the worst values. Establish what normal looked like before 09:00, then identify the earliest timestamp where any metric exceeded 2 standard deviations from normal. What was that metric, and what was happening at that exact time in other data sources?"

**Building causation chains:**
> "I have a correlated timeline of events. For each event, determine whether it is a CAUSE (triggered subsequent events) or a SYMPTOM (result of prior events). Look for temporal ordering - causes must precede effects. Start from the first anomaly and trace forward: what did it cause? Then trace that effect forward. Build the complete causation chain from root cause to citizen impact."

**Root cause hypothesis with Opus:**
> "Based on the timeline and causation chain, form a hypothesis about the root cause. The root cause is what CHANGED to start the incident, not the resource that eventually failed. Consider: what was different on this day compared to normal operation? Test your hypothesis: does it explain the sequence of events? Could another explanation fit the data better?"

**Challenging red herrings:**
> "The obvious interpretation is that [insert surface symptom] caused the outage. Challenge this hypothesis. Is this a cause or a symptom? What evidence would prove it is the root cause versus a consequence? What came BEFORE this in the timeline? If we fixed only this symptom, would the underlying problem remain?"

**Designing proactive monitoring:**
> "Based on this root cause analysis, design a monitoring architecture that would detect this class of problem BEFORE citizens are affected. Include: leading indicators that predict failure, appropriate thresholds based on the baselines we established, alert escalation that matches incident severity, and dashboards that distinguish causes from symptoms. Explain what each alert would catch and how early warning it provides."

---

## Tips and gotchas

### AI fixates on loudest errors

| Issue | What to do |
|-------|------------|
| Reports the biggest spike, not the first | Explicitly ask for "first deviation from baseline, not worst" |
| Focuses on errors over warnings | Ask for chronological ordering regardless of severity |
| Misses subtle early signals | Ask to compare pre-incident baseline to early incident period |

### Confuses correlation with causation

| Issue | What to do |
|-------|------------|
| "High memory caused slow queries" | Ask: "What caused high memory?" - it is probably also a symptom |
| Events happen at same time | Ask: "Which came first at sub-minute granularity?" |
| Assumes obvious explanation | Challenge with: "What else could explain this pattern?" |

### Citizen complaints lag actual events

| Issue | What to do |
|-------|------------|
| Uses complaint time as incident time | Complaints follow problems by 10-30 minutes |
| Treats social media as real-time | Citizens post after repeated failures, not first failure |
| Missing the early warning window | Service desk tickets are lagging indicators, not leading |

### Infrastructure metrics are symptoms

| Issue | What to do |
|-------|------------|
| "CPU spike caused the outage" | CPU responds to load - what caused the load? |
| "Memory exhaustion was the problem" | What was consuming memory? That is closer to root cause |
| "Database connections ran out" | Why were connections held? What blocked them? |

### Timestamp format mismatches

| Issue | What to do |
|-------|------------|
| Cannot correlate across sources | Convert all timestamps to single format first |
| Timezone confusion | Check if times are UTC or local |
| Precision differences | Some sources have seconds, others only minutes |

---

## Reflection questions

After completing the challenge, consider:

- How did you distinguish root cause from symptoms that appeared more dramatic?
- What was the gap between first technical anomaly and first citizen complaint?
- Could your monitoring design have detected this before 09:00?
- What assumptions did the AI make that you had to correct?
- How would you explain your investigation method to a team investigating a different incident?
