# Agentic AI: autonomous workloads for government development

This guide explains how to move beyond prompt-and-response AI assistance into autonomous agentic workflows — where your AI tool plans, delegates, and executes complex tasks independently.

New to the AI tools used in this workshop? Start with the basics first:
- [Getting Started with Claude Code](getting-started-claude-code.md)
- [Getting Started with AWS Kiro](getting-started-aws-kiro.md)

---

## The difference between AI assistance and agentic AI

Most developers start by using AI tools reactively: ask a question, review the answer, ask another question. This works well for focused tasks but creates a bottleneck — you are still the coordinator.

Agentic AI flips this. You describe a goal. The AI plans the work, coordinates specialist agents, executes steps, and returns results. You review the outcome rather than managing every step.

### What agentic means in practice

| Approach | What you do | What the AI does |
|----------|-------------|-----------------|
| AI assistance | Prompt by prompt | Responds to each request |
| Agentic AI | Describe the goal | Plans, delegates, executes, reports |

**AI assistance example:**
> You ask for a security review. Claude audits one file, you review, you ask it to check another file, and so on.

**Agentic AI example:**
> You ask for a security review across the whole service. Claude spawns a read-only security sub-agent that explores all files, runs checks across the codebase, and returns a prioritised report. You review the report.

The agentic approach is faster for complex, multi-file tasks. It also keeps your main conversation context focused — verbose tool output stays in sub-agent contexts, not clogging your conversation.

---

## Why this matters for government services

Government projects regularly involve:

- Multiple quality gates running in parallel (accessibility, security, compliance)
- Long-running investigations across large codebases
- Repetitive checks that must run consistently (WCAG audits, OWASP reviews)
- Documentation that needs to stay synchronised with code changes

These are exactly the tasks where agentic workflows reduce effort and improve consistency.

**Example government scenarios:**

| Scenario | Agentic approach |
|----------|-----------------|
| New service accessibility audit | Orchestrator spawns accessibility sub-agent across all templates simultaneously |
| Security vulnerability assessment | Orchestrator runs security and dependency sub-agents in parallel, combines reports |
| Spec-to-code for a new feature | Kiro's Spec Mode generates requirements, design, and tasks autonomously |
| Test coverage check after refactor | Automated hook triggers test-writer agent on every file save |
| Documentation sync after API changes | Hook fires on file edit and prompts agent to update docs |

---

## Two tools, two agentic models

Both Claude Code and Kiro support agentic workflows, but they approach it differently.

### Claude Code: sub-agents and orchestration

Claude Code uses a sub-agent model. The main Claude session acts as an orchestrator and spawns specialist sub-agents to handle specific tasks. Each sub-agent runs in its own isolated context with its own tool permissions and model selection.

Key capabilities:
- **Custom sub-agents** defined as Markdown files with YAML frontmatter in `.claude/agents/`
- **Automatic delegation** based on sub-agent descriptions — Claude decides when to delegate
- **Parallel execution** — spawn multiple sub-agents to run independent tasks simultaneously
- **Programmatic mode** (`claude -p`) to run Claude Code non-interactively in scripts and CI/CD pipelines
- **Background tasks** — sub-agents run concurrently while you continue working

[Full Claude Code agentic guide](getting-started-agentic-claude-code.md)

### Kiro: hooks, agents, and autonomous tasks

Kiro takes a complementary approach. Within the IDE, you configure specialist agents and hooks that trigger automatically when events occur. Kiro also offers a cloud-based autonomous agent (currently in preview) that works asynchronously across repositories without requiring an active IDE session.

Key capabilities:
- **Custom agents** defined as Markdown files in `.kiro/agents/` with automated routing
- **Hooks** that trigger agent actions automatically on file events, tool use, and task lifecycle events
- **Spec Mode** as a structured autonomous workflow — requirements, design, and tasks generated in sequence
- **Kiro CLI** for running agents in the terminal without the IDE
- **Kiro autonomous agent** (preview) for long-running background tasks that create pull requests

[Full Kiro agentic guide](getting-started-agentic-aws-kiro.md)

---

## Choosing the right approach

The tools have complementary strengths. Both are applicable to the challenges in this workshop.

| Need | Claude Code | Kiro |
|------|-------------|------|
| Parallel research across codebase | Sub-agents run simultaneously | Multiple agent sessions |
| Automated checks on every file save | PostToolUse hooks | File save hooks |
| Structured feature development | CLAUDE.md context + orchestration | Spec Mode |
| Non-interactive scripting and CI/CD | `claude -p` | Kiro CLI |
| Long-running background tasks | Background sub-agents | Kiro autonomous agent |
| Read-only investigation agents | Tool-restricted sub-agents | Read-only agent permissions |
| Persistent knowledge across sessions | Agent memory files | Steering files |

You do not need to choose one permanently. Many teams use Claude Code for interactive development and scripting, and Kiro's hooks for automated quality gates.

---

## Getting started with agentic workflows

The fastest path to agentic AI is to start with one well-defined specialist agent for a task you do repeatedly.

### For Claude Code users

1. Identify a task you repeat often — accessibility review, security check, test generation
2. Create a sub-agent file in `.claude/agents/` with a focused system prompt
3. Give it only the tools it needs
4. Ask Claude to use it: "Use the accessibility-reviewer sub-agent on all templates in src/"

[See the full guide with configuration examples](getting-started-agentic-claude-code.md)

### For Kiro users

1. Identify an event you always respond to — a file save, a task completion, a new file created
2. Create a hook in `.kiro/hooks/` that triggers an agent prompt on that event
3. Start with a simple hook and expand once you see it working

[See the full guide with configuration examples](getting-started-agentic-aws-kiro.md)

---

## Agentic patterns in the challenge levels

Each challenge level has playbooks for both Claude Code and Kiro. The table below shows which agentic patterns are most relevant at each level.

| Level | Challenge | Relevant agentic pattern |
|-------|-----------|--------------------------|
| 1 | PDF to Digital Service | Parallel accessibility and GOV.UK compliance agents |
| 2 | Data Processing | Sub-agent for data validation; hook for dashboard updates |
| 3 | Database CRUD | Schema review sub-agent; audit trail verification hook |
| 4 | Legacy Modernisation | Parallel analysis agents across multiple legacy files |
| 5 | Business Logic | Spec Mode for rules engine; test-rule sub-agent |
| 6 | Security Assessment | Security review sub-agent with read-only tool restriction |
| 7 | Performance Investigation | Background agent for log analysis across large files |
| 8 | Testing Strategy | Test-writer sub-agent; PostToolUse hook for auto-coverage |
| 9 | Multi-Service Architecture | Multi-agent research across service boundaries |
| 10 | Production Deployment | Ops-analysis sub-agent; deployment validator hook |

---

## Further reading

- [Claude Code sub-agents documentation](https://code.claude.com/docs/en/sub-agents)
- [Claude Code programmatic mode](https://code.claude.com/docs/en/headless)
- [Kiro hooks documentation](https://kiro.dev/docs/hooks/)
- [Kiro autonomous agent](https://kiro.dev/autonomous-agent/)
- [Kiro CLI](https://kiro.dev/blog/introducing-kiro-cli/)
- [Model Context Protocol](https://modelcontextprotocol.io)
