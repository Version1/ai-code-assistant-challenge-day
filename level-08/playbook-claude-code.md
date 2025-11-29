# Level 8: Adaptive Testing Strategy and Risk-Based Quality Engineering

This playbook helps you test government digital services by focusing on citizen harm, not just technical failures. You will apply risk-based testing to a service you built in Level 1, 2, or 3.

Traditional testing asks "Does it work?" Risk-based testing asks "Who gets hurt when it fails, and how badly?"

---

## CLAUDE.md Snippet

Add this to your project's `CLAUDE.md` file to give Claude context for adaptive testing:

```markdown
## Testing Context: Risk-Based Quality Engineering

This project uses citizen-harm-centred testing for government digital services.

### Risk Categories (by citizen impact)
- CRITICAL: Citizen denied service, data breach, accessibility barrier preventing completion
- HIGH: Confusing error recovery, timeout losing entered data, unclear next steps
- MEDIUM: Slow performance degrading experience, minor confusion points
- LOW: Cosmetic issues, non-blocking visual inconsistencies

### Citizen Personas for Testing
- Low digital literacy user on shared library computer
- Screen reader user on mobile with intermittent 3G connection
- Stressed parent completing form one-handed while holding child
- Elderly user with outdated browser and limited technical vocabulary

### Test Environment Constraints
Simulate real conditions: slow 3G networks, interrupted sessions, shared devices, assistive technologies. Prioritise real device testing over emulators.

### Testing Philosophy
Test recovery paths as thoroughly as happy paths. Every error state needs a clear route back to success.
```

---

## Custom Slash Commands

### /project:analyze-service-risks

Create `.claude/commands/analyze-service-risks.md`:

```markdown
Analyse this service for citizen harm risks. Review the codebase and identify:

## Critical Risks (citizen denied service or harmed)
- Points where citizens could be blocked from completing their task
- Data handling that could expose personal information
- Accessibility barriers that prevent specific users from proceeding

## High Risks (frustrating but recoverable)
- Error states without clear recovery paths
- Form timeouts that lose entered data
- Confusing messaging that leaves citizens unsure what to do

## Medium Risks (degraded experience)
- Performance bottlenecks under load
- Minor usability friction points

## For Each Risk Identified
1. Describe the failure scenario
2. Identify which citizen personas are most affected
3. Rate likelihood (common, occasional, rare)
4. Recommend specific test cases

Focus on $ARGUMENTS or scan the full service if no area specified.
```

### /project:generate-citizen-scenarios

Create `.claude/commands/generate-citizen-scenarios.md`:

```markdown
Generate realistic test scenarios for the citizen persona: $ARGUMENTS

Create 5 end-to-end scenarios that reflect how this person actually uses digital services:

## Scenario Structure
For each scenario, include:
- **Starting context**: Where are they? What device? What's their mental state?
- **Task goal**: What are they trying to accomplish?
- **Realistic interruptions**: What might break their flow?
- **Environmental constraints**: Connection speed, time pressure, device limitations
- **Success criteria**: How do they know they've completed the task?
- **Failure recovery**: What happens if something goes wrong mid-task?

## Personas Available
- `library-user`: Low digital literacy, shared computer, time-limited session
- `screen-reader-mobile`: Assistive tech user, poor connectivity, small screen
- `parent-one-handed`: Distracted, mobile device, frequent interruptions
- `elderly-outdated`: Limited tech vocabulary, old browser, cautious about errors

Generate scenarios that expose edge cases and recovery path gaps.
```

---

## Model Recommendations

| Task | Recommended Model | Why |
|------|-------------------|-----|
| Risk analysis across codebase | Opus | Needs deep reasoning about failure cascades and citizen impact |
| Generating test scenarios | Sonnet | Good balance of creativity and consistency for persona-based scenarios |
| Accessibility barrier identification | Opus | Requires understanding interaction between code, assistive tech, and user behaviour |
| Test case prioritisation | Sonnet | Structured analysis with clear ranking criteria |
| Recovery path mapping | Opus | Complex flow analysis requiring multiple failure state consideration |

---

## Effective Prompts for Risk-Based Testing

### 1. Failure Mode Analysis

```
Analyse this form submission flow for failure modes that harm citizens.

For each failure mode:
- What triggers it (user action, system state, external factor)?
- Which citizen personas are most likely to encounter it?
- What data could be lost?
- What is the current recovery path?
- What should the recovery path be?

Rank by citizen harm severity, not technical complexity.
Focus on: [paste component or describe flow]
```

### 2. Accessibility Stress Testing

```
Design accessibility stress tests for this service combining:
- Assistive technology (screen reader, voice control, switch access)
- Environmental constraints (slow connection, interruptions, shared device)
- Cognitive load factors (time pressure, unfamiliar terminology, anxiety)

For each test combination:
- Describe the specific test setup
- List what to observe during the test
- Define pass/fail criteria based on task completion, not just WCAG compliance
- Note required real devices vs acceptable emulation

Prioritise tests by likelihood of real-world occurrence.
```

### 3. Recovery Path Analysis

```
Map every error state in this service to its recovery path.

For each error state:
- What message does the citizen see?
- What actions are available to them?
- How many steps to return to their task?
- What data is preserved vs lost?
- Does recovery work with assistive technology?

Flag any error states where:
- Recovery requires starting over
- The message doesn't explain what to do next
- The path back isn't keyboard accessible
- Citizens might not understand the terminology used

Present as a table: Error State | Current Recovery | Citizen Impact | Recommended Fix
```

### 4. Environment Simulation Testing

```
Create a test plan for realistic environment conditions:

- Network: 3G throttling, intermittent drops, high latency (500ms+)
- Device: Shared browser with cleared cookies, outdated browser, aggressive battery saving
- Session: Form abandoned 20 minutes, browser back button, tab reopened from history

For each condition, specify how to simulate it, what behaviour to test, expected graceful degradation, and actual current behaviour.
```

### 5. Citizen Harm Assessment

```
Assess citizen harm potential for this service failure: [describe failure]

Rate on: Severity (worst outcome), Breadth (how many affected), Vulnerability (disproportionate impact on disadvantaged), Recoverability (can they fix it alone), Detectability (will we know).

Provide overall harm rating, personas most at risk, recommended test coverage, and monitoring suggestions.
```

---

## Tips and Gotchas

| Situation | What to do | What to avoid |
|-----------|------------|---------------|
| **Prioritising test coverage** | Rank by citizen harm potential first, then by likelihood of occurrence | Ranking by technical severity or ease of testing |
| **Creating persona scenarios** | Base scenarios on real user research and support tickets | Inventing convenient personas that don't reflect actual users |
| **Testing environment constraints** | Use real devices and actual network throttling tools | Relying solely on browser dev tools simulation |
| **Integrating accessibility** | Test with actual assistive technology users when possible | Treating automated accessibility scans as sufficient |
| **Managing session state** | Test interrupted journeys, expired sessions, and browser back button behaviour | Assuming users complete forms in single uninterrupted sessions |

---

## Reflection Questions

After completing your testing work, consider:

1. **Harm-centred prioritisation**: Did you prioritise test cases by potential citizen harm, or did technical factors influence your ranking? Which critical-harm scenarios did you initially overlook?

2. **Persona authenticity**: Do your test personas reflect real citizens using your service, or idealised users? What would change if you based personas on actual support requests and user research?

3. **Coverage versus depth**: Did you test many scenarios superficially, or fewer scenarios thoroughly including recovery paths? Where would deeper testing of high-harm scenarios have revealed more issues than broader coverage?

---

Test critical and high-risk areas first. A service with thorough critical-risk coverage and known low-risk gaps serves citizens better than one with even coverage across all risk levels.
