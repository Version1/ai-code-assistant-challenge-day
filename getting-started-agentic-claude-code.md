# Autonomous agents with Claude Code

This guide covers configuring Claude Code for autonomous agentic workflows — where Claude orchestrates specialist sub-agents to complete complex tasks independently.

For the Claude Code basics (installation, CLAUDE.md, custom commands, MCP), see [Getting Started with Claude Code](getting-started-claude-code.md). This guide builds on that foundation.

For a tool comparison and introduction to agentic AI, see the [Agentic AI guide](agentic-ai-guide.md).

---

## How Claude Code's sub-agent system works

Claude Code uses a hierarchical model. The main Claude session — running in your terminal — acts as an orchestrator. When it encounters a task that matches a sub-agent's description, it delegates to that sub-agent, which works independently and returns results.

Each sub-agent:
- Runs in its own isolated context window (separate from your main conversation)
- Has its own system prompt defining its specialisation
- Can have restricted tool access — read-only agents cannot write files
- Can use a different model — route expensive tasks to Opus, routine checks to Haiku
- Cannot spawn further sub-agents (only the main conversation can orchestrate)

This design keeps your main conversation focused. Verbose output from test runs, log analysis, or large-scale searches stays in the sub-agent's context. Only the summary returns to you.

---

## Built-in sub-agents

Claude Code includes three built-in sub-agents that Claude uses automatically. Understanding them helps you design your own.

| Sub-agent | Model | Tools | When Claude uses it |
|-----------|-------|-------|---------------------|
| Explore | Haiku | Read-only | Searching and analysing codebases without making changes |
| Plan | Inherits | Read-only | Gathering context during plan mode before presenting a proposal |
| General-purpose | Inherits | All tools | Complex multi-step tasks requiring both exploration and action |

You do not need to invoke these directly — Claude decides when to use them. You can create custom sub-agents that work alongside them.

---

## Creating custom sub-agents

### File format and location

Sub-agents are Markdown files with YAML frontmatter. Save them in:

- `.claude/agents/` — project-level, available to your team (check into version control)
- `~/.claude/agents/` — user-level, available across all your projects

When multiple sub-agents share the same name, project-level takes precedence over user-level.

**Basic format:**

```markdown
---
name: accessibility-reviewer
description: Reviews templates for WCAG 2.2 AA compliance. Use proactively after any template changes.
tools: Read, Grep, Glob
model: sonnet
---

You are an accessibility specialist reviewing code against WCAG 2.2 AA standards and GOV.UK Design System requirements.

When invoked:
1. Identify all template files in the target directory
2. Check each template for accessibility issues
3. Report findings with file paths, line numbers, and remediation steps

Check for:
- Form inputs without associated labels
- Missing or incorrect aria-describedby for error messages
- Images without alt text
- Heading hierarchy problems (skipped levels)
- Links with non-descriptive text
- Colour contrast issues in custom styles
- GOV.UK Design System component misuse
```

### Required fields

| Field | Required | What it does |
|-------|----------|--------------|
| `name` | Yes | Unique identifier (lowercase, hyphens only) |
| `description` | Yes | When Claude should delegate to this sub-agent — write this to help Claude decide |
| Body (Markdown) | Yes | The system prompt that defines how the sub-agent behaves |

### Optional configuration fields

| Field | What it does | Example values |
|-------|-------------|----------------|
| `tools` | Which tools the sub-agent can use (allowlist) | `Read, Grep, Glob, Bash` |
| `disallowedTools` | Tools to deny (denylist alternative to tools) | `Write, Edit` |
| `model` | Model to use | `sonnet`, `opus`, `haiku`, `inherit` |
| `permissionMode` | How the sub-agent handles permission prompts | `default`, `acceptEdits`, `bypassPermissions`, `plan` |
| `maxTurns` | Maximum turns before the sub-agent stops | `10` |
| `memory` | Persistent memory directory across sessions | `user`, `project`, `local` |
| `background` | Always run as a background task | `true` |
| `isolation` | Run in a temporary git worktree | `worktree` |
| `hooks` | Lifecycle hooks scoped to this sub-agent | See hooks section below |
| `skills` | Skill content to inject at startup | `- api-conventions` |
| `mcpServers` | MCP servers available to this sub-agent | See MCP docs |

### Writing effective descriptions

The `description` field is what Claude reads to decide when to delegate. Write it to be specific about the trigger condition.

**Weak description** — Claude may not delegate at the right time:
```
description: Code reviewer
```

**Strong description** — Claude knows exactly when to use it:
```
description: Reviews code for security vulnerabilities. Use proactively after any changes to authentication, authorisation, session handling, or data persistence code.
```

Add "use proactively" when you want Claude to delegate without being asked.

---

## Restricting tool access

Limiting what a sub-agent can do is one of the most important agentic design decisions. A read-only investigation agent cannot accidentally modify production data. A security reviewer that cannot write files cannot introduce changes.

### Allowlist with `tools`

Specify exactly which tools the sub-agent may use:

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities. Use proactively after changes to auth, sessions, or data handling.
tools: Read, Grep, Glob
---
```

Available built-in tools include: `Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`, `WebFetch`, `WebSearch`, `Task`.

### Denylist with `disallowedTools`

Inherit all tools but block specific ones:

```markdown
---
name: safe-analyst
description: Analyses performance and reports findings without making changes.
disallowedTools: Write, Edit
---
```

### Restricting which sub-agents can be spawned

If you are running Claude Code as an autonomous orchestrator (using `claude --agent`), you can restrict which sub-agent types the orchestrator can spawn:

```markdown
---
name: coordinator
description: Orchestrates security and accessibility reviews
tools: Task(security-reviewer, accessibility-reviewer), Read, Bash
---
```

Only the `security-reviewer` and `accessibility-reviewer` sub-agents can be spawned. Any attempt to spawn another type will fail.

---

## Model selection

Route tasks to the right model based on complexity and cost.

| Model alias | When to use |
|-------------|-------------|
| `haiku` | Fast, cheap tasks — file discovery, simple pattern matching, log scanning |
| `sonnet` | Most work — code analysis, reviews, implementation |
| `opus` | Deep reasoning — architectural analysis, complex debugging, edge case hunting |
| `inherit` | Use the same model as the main conversation (default) |

```markdown
---
name: file-explorer
description: Discovers and lists files matching patterns
model: haiku
tools: Read, Glob, Grep
---
```

---

## Permission modes

Control how the sub-agent handles permission prompts:

| Mode | Behaviour |
|------|-----------|
| `default` | Standard permission checks with prompts |
| `acceptEdits` | Auto-accept file edits without prompting |
| `bypassPermissions` | Skip all permission checks — use with caution |
| `plan` | Read-only exploration, cannot make changes |

For autonomous workflows where you want uninterrupted execution, `acceptEdits` is often the right balance — the sub-agent can write files but cannot run arbitrary Bash commands without prompting.

---

## Parallel execution

Spawn multiple sub-agents simultaneously for independent tasks. Each runs in its own context window while your main conversation waits for all to complete.

**Requesting parallel sub-agents:**

```
Research the authentication module, database layer, and API endpoints in parallel using separate sub-agents. I need to understand each independently before we discuss changes.
```

**What Claude does:**
1. Spawns three sub-agents simultaneously
2. Each explores its module independently
3. Results return to your main conversation
4. Claude synthesises findings

This is most effective when tasks are genuinely independent — each sub-agent should not depend on another's output.

### Background tasks

Ask Claude to run a sub-agent in the background, freeing you to continue working:

```
Run the test suite in the background using a sub-agent and tell me when it's done. I'll keep working on the auth module.
```

Press **Ctrl+B** to background a running task.

For tasks that need sustained parallelism beyond what a single session supports, the [Agent Teams](https://code.claude.com/docs/en/agent-teams) feature provides each worker with its own independent session.

---

## Persistent memory for sub-agents

Give a sub-agent a persistent memory directory so it builds up knowledge across sessions:

```markdown
---
name: codebase-analyst
description: Analyses codebase patterns and architecture. Use when exploring unfamiliar code.
memory: project
model: sonnet
tools: Read, Grep, Glob
---

You are a codebase analyst. Update your agent memory as you discover patterns, architectural decisions, key file locations, and data flows. This builds institutional knowledge across conversations.

When starting work:
1. Check your memory for relevant notes about this codebase
2. Complete the analysis
3. Update your memory with new findings
```

Memory scopes:

| Scope | Location | Use when |
|-------|----------|----------|
| `user` | `~/.claude/agent-memory/<name>/` | Knowledge applies across all projects |
| `project` | `.claude/agent-memory/<name>/` | Knowledge is project-specific and shareable |
| `local` | `.claude/agent-memory-local/<name>/` | Project-specific but should not be committed |

The first 200 lines of `MEMORY.md` in the memory directory are injected into the sub-agent's context at startup.

---

## Hooks within sub-agents

Sub-agents can define their own hooks that run during their lifecycle — separate from the project-level hooks in `settings.json`.

**Example: run linting after every file the sub-agent edits**

```markdown
---
name: refactorer
description: Refactors code to modern patterns. Use when modernising legacy code.
tools: Read, Edit, Bash
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "npx eslint --fix $CLAUDE_FILE_PATH"
---
```

**Example: validate Bash commands before execution**

```markdown
---
name: safe-executor
description: Runs validation scripts safely
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-command.sh"
---
```

---

## Running Claude Code non-interactively

Use `claude -p` (the `-p` or `--print` flag) to run Claude Code without an interactive session. This is useful for:

- CI/CD pipelines that need AI-assisted checks
- Automation scripts that process outputs programmatically
- Batch processing across multiple files or repositories

```bash
# Basic non-interactive use
claude -p "What does the auth module do?"

# Allow specific tools without prompting
claude -p "Run the test suite and fix any failures" \
  --allowedTools "Bash,Read,Edit"

# Return structured JSON output
claude -p "Summarise this project" --output-format json

# Continue the most recent conversation
claude -p "Now check the security implications" --continue
```

### Using structured output in scripts

```bash
# Extract a structured result with jq
claude -p "List all API endpoints in src/" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"endpoints":{"type":"array","items":{"type":"string"}}},"required":["endpoints"]}' \
  | jq '.structured_output.endpoints'
```

### Piping content to Claude

```bash
# Review a PR diff for security issues
gh pr diff 42 | claude -p \
  --append-system-prompt "You are a security reviewer. Identify vulnerabilities." \
  --output-format json
```

### Creating commit messages automatically

```bash
claude -p "Look at my staged changes and create an appropriate commit" \
  --allowedTools "Bash(git diff *),Bash(git log *),Bash(git status *),Bash(git commit *)"
```

The space before `*` in `Bash(git diff *)` is important — it enables prefix matching. Without the space, `git diff*` would also match `git diff-index`.

---

## CLAUDE.md for autonomous workflows

When designing Claude to act as an orchestrator, your CLAUDE.md should include explicit orchestration instructions.

**Example CLAUDE.md snippet for a government service review workflow:**

```markdown
## Autonomous review workflow

When asked to perform a full service review, always delegate to specialist sub-agents:

1. Spawn the accessibility-reviewer sub-agent across all templates in src/
2. Spawn the security-reviewer sub-agent across authentication and data handling
3. Run both in parallel — they are independent
4. Synthesise findings from both sub-agents into a prioritised action list

Never perform these reviews yourself in the main conversation — the sub-agents have focused system prompts and restricted tools designed for these tasks.

## Sub-agents available in this project

- `accessibility-reviewer` — WCAG 2.2 AA and GOV.UK Design System compliance
- `security-reviewer` — OWASP Top 10 and government security standards
- `test-writer` — Unit and integration test generation following project patterns
- `db-analyst` — Read-only database query analysis
```

---

## Practical example: government service review

This example shows a complete autonomous workflow for reviewing a GOV.UK digital service before release.

### Sub-agent definitions

**`.claude/agents/accessibility-reviewer.md`**

```markdown
---
name: accessibility-reviewer
description: Reviews templates for WCAG 2.2 AA and GOV.UK Design System compliance. Use proactively after any template changes or before release.
tools: Read, Grep, Glob
model: sonnet
---

You are an accessibility specialist. Review templates for WCAG 2.2 AA compliance and GOV.UK Design System conformance.

When invoked:
1. Find all template files using Glob
2. Check each for accessibility issues
3. Produce a prioritised report (critical, high, medium, low)

Check for:
- Form inputs without visible labels (not placeholder-only)
- Missing aria-describedby for error messages
- Error summary component absent when errors exist
- Images without alt text (or empty alt for decorative images)
- Heading hierarchy issues (skipped levels, multiple h1 elements)
- Non-descriptive link text ("click here", "read more")
- GOV.UK components used incorrectly (native inputs instead of govukInput etc.)
- Date inputs using native date picker instead of three-field pattern

For each issue, provide: file path, line number, WCAG criterion violated, recommended fix.
```

**`.claude/agents/security-reviewer.md`**

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities. Use proactively after changes to authentication, session handling, database queries, or file handling.
tools: Read, Grep, Glob
model: sonnet
---

You are a security engineer reviewing government service code.

When invoked:
1. Focus on authentication, session management, data input/output, and database interactions
2. Check for OWASP Top 10 vulnerabilities
3. Produce findings with severity (critical, high, medium, low)

Check for:
- SQL injection via unsanitised query parameters
- Cross-site scripting (XSS) in template output
- Insecure session configuration (missing secure/httpOnly cookie flags)
- Missing CSRF protection on form submissions
- Hardcoded secrets or API keys
- Sensitive data logged or exposed in error messages
- File upload handling without type validation
- Missing input validation on all user-supplied data

For each issue: file path, line number, vulnerability type, severity, remediation.
```

### Running the workflow

```
Perform a full release readiness review of this service. Run the accessibility-reviewer and security-reviewer sub-agents in parallel across the entire src/ directory. When both complete, give me a combined prioritised action list — critical issues first.
```

Claude spawns both sub-agents simultaneously. Each explores the codebase independently. When complete, Claude synthesises the findings and presents a prioritised list.

---

## Tips and gotchas

### Design focused sub-agents

Each sub-agent should do one thing well. An "everything checker" sub-agent with a long system prompt produces unfocused results. A `security-reviewer` and a separate `accessibility-reviewer` each produce sharper, more actionable findings.

### Test sub-agents before relying on them

After creating a sub-agent, invoke it on a small, known piece of code first. Verify the output matches your expectations before running it across a large codebase.

### Use the /agents command

The `/agents` command in an interactive session provides a guided interface for creating, editing, and deleting sub-agents. It also shows which sub-agents are active and which are overridden.

### Sub-agents cannot spawn sub-agents

Only the main conversation can orchestrate sub-agents. If you need nested delegation, chain sub-agents from the main conversation — instruct Claude to use one sub-agent, then another when the first completes.

### Background tasks need upfront permission approval

Before a background sub-agent runs, Claude Code prompts for any tool permissions it will need. Grant these upfront — once running in the background, the sub-agent auto-denies anything not pre-approved.

### Long-running tasks use worktree isolation

For sub-agents that make extensive file changes, `isolation: worktree` gives them a temporary git worktree — an isolated copy of the repository. The worktree is cleaned up automatically if the sub-agent makes no changes.

```markdown
---
name: large-refactorer
description: Refactors large portions of the codebase
isolation: worktree
tools: Read, Edit, Write, Bash
---
```

---

## Where to go next

- [Agent Teams](https://code.claude.com/docs/en/agent-teams) — coordinate agents across separate sessions for sustained parallel work
- [Claude Code headless / Agent SDK](https://code.claude.com/docs/en/headless) — run Claude Code programmatically in CI/CD
- [MCP servers](https://code.claude.com/docs/en/mcp) — extend sub-agents with external tools and data
- [Hooks](https://code.claude.com/docs/en/hooks) — automate actions based on Claude Code events
- [Agentic AI guide](agentic-ai-guide.md) — comparison with Kiro and pattern recommendations for each challenge level
