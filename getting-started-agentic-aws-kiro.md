# Autonomous agents with AWS Kiro

This guide covers configuring Kiro for autonomous agentic workflows — custom agents, hooks-driven automation, the Kiro CLI, and the Kiro autonomous agent for long-running background tasks.

For Kiro basics (installation, steering files, Vibe Mode, Spec Mode, MCP), see [Getting Started with AWS Kiro](getting-started-aws-kiro.md). This guide builds on that foundation.

For a tool comparison and introduction to agentic AI, see the [Agentic AI guide](agentic-ai-guide.md).

---

## How Kiro's agentic system works

Kiro has three distinct agentic layers:

1. **Custom agents** — specialist AI personas for specific tasks, defined as Markdown files in `.kiro/agents/`. Kiro routes requests to them automatically, or you invoke them explicitly.

2. **Hooks** — event-driven triggers that run agent prompts or shell commands automatically when things happen (file saved, tool used, task status changed). These create autonomous workflows without user intervention.

3. **Kiro autonomous agent** (preview) — a cloud-based agent that works asynchronously across repositories, runs in sandboxed environments, and creates pull requests for you to review.

These three layers can be used independently or combined. Start with custom agents to specialise Kiro's behaviour. Add hooks to automate quality gates. Graduate to the autonomous agent for long-running tasks that span multiple repositories.

---

## Custom agents

Custom agents give Kiro a specialist mindset for specific tasks. Kiro automatically selects the right agent based on its description, or you can invoke one explicitly.

### File format and location

Custom agents are Markdown files with an optional YAML-like header. Save them in:

- `.kiro/agents/` — project-level, available to your team (check into version control)
- `~/.kiro/agents/` — user-level, available across all your projects

**Basic format:**

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities and OWASP Top 10 issues
model: claude-sonnet-4
tools: ["read"]
---

You are a security engineer reviewing government service code.

When invoked, focus on:
- Authentication and session management
- Input validation and SQL injection risks
- Cross-site scripting (XSS) vulnerabilities
- Hardcoded secrets or API keys
- Missing CSRF protection
- Sensitive data in logs or error messages

Report findings with: file path, vulnerability type, severity (critical/high/medium/low), and remediation steps.
```

### Configuration fields

| Field | What it does | Example |
|-------|-------------|---------|
| `name` | Unique identifier for the agent | `security-reviewer` |
| `description` | What the agent does — Kiro uses this to route requests | `Reviews code for security vulnerabilities` |
| `model` | Which model the agent uses | `claude-sonnet-4` |
| `tools` | Tool access permissions | `["read"]`, `["read", "write"]` |
| `toolsSettings` | Granular tool permissions with path restrictions | See example below |
| `resources` | Steering files to load automatically | `[".kiro/steering/tech.md"]` |

### Tool permissions

Control what the agent can read and write:

```json
{
  "name": "db-analyst",
  "description": "Analyses database queries and schema. Read-only access.",
  "tools": ["read", "shell"],
  "toolsSettings": {
    "shell": {
      "allowedCommands": ["psql", "pg_dump"],
      "blockedCommands": ["DROP", "DELETE", "UPDATE", "INSERT"]
    }
  }
}
```

Common tool values: `read`, `write`, `shell`, `web`

### Invoking agents

Kiro routes to agents automatically based on their descriptions. You can also invoke them explicitly:

```
Use the security-reviewer agent to check the authentication module
```

```
@security-reviewer Review src/auth/ for vulnerabilities
```

### Built-in agents

Kiro includes two built-in agents:

- **kiro_default** — The general-purpose agent used for new sessions. Handles everyday coding tasks.
- **Auto agent** — Dynamically selects the optimal model for each task based on complexity. Use when you want Kiro to balance speed and capability automatically.

---

## Hooks

Hooks are the most powerful tool for building autonomous workflows in Kiro. They trigger agent prompts or shell commands automatically when events occur.

### What hooks enable

Without hooks, you ask Kiro to review code. With hooks, Kiro reviews code automatically every time you save a file. The difference is whether you drive the workflow or the workflow runs itself.

### Hook configuration format

Hooks are stored in `.kiro/hooks/` as JSON files with the `.kiro.hook` extension.

**Basic structure:**

```json
{
  "name": "Hook Name",
  "description": "What this hook does",
  "version": "1",
  "when": {
    "type": "fileEdited",
    "patterns": ["**/*.ts", "!**/node_modules/**"]
  },
  "then": {
    "type": "askAgent",
    "prompt": "Natural language instruction for the agent"
  }
}
```

### Trigger types

| Trigger type | When it fires | Use for |
|-------------|--------------|---------|
| `fileEdited` | When a matching file is saved | Auto-formatting, linting, test updates |
| `fileCreate` | When a matching file is created | Boilerplate injection, import maintenance |
| `fileDelete` | When a matching file is deleted | Cleanup, reference removal |
| `userTriggered` | Manual trigger on demand | On-demand reviews, scans |
| `promptSubmit` | When a user submits a prompt | Context injection, prompt logging |
| `agentStop` | After agent completes a response | Code compilation, formatting after agent changes |
| `preToolUse` | Before agent invokes a tool | Block specific operations, inject context |
| `postToolUse` | After tool execution completes | Logging, formatting, follow-up actions |
| `preTaskExecution` | When a spec task starts | Environment setup, prerequisites |
| `postTaskExecution` | When a spec task completes | Test execution, documentation updates |

### Action types

| Action type | What it does |
|-------------|-------------|
| `askAgent` | Runs an agent prompt with the specified instructions |
| `runCommand` | Executes a shell command |

### File pattern matching

Patterns use GLOB syntax. Prefix with `!` to exclude:

```json
"patterns": [
  "**/*.ts",
  "!**/*.test.ts",
  "!**/*.spec.ts",
  "!**/node_modules/**"
]
```

### Practical hook examples

**Auto-update tests when source files change:**

```json
{
  "name": "test-updater",
  "description": "Updates test files when source TypeScript changes",
  "version": "1",
  "when": {
    "type": "fileEdited",
    "patterns": ["src/**/*.ts", "!src/**/*.test.ts"]
  },
  "then": {
    "type": "askAgent",
    "prompt": "A TypeScript source file was modified. Check the corresponding test file and update it to cover any new or changed functions. Keep existing passing tests. Add tests for new functionality only."
  }
}
```

**Accessibility check on every template save:**

```json
{
  "name": "accessibility-check",
  "description": "Checks accessibility compliance when Nunjucks templates are saved",
  "version": "1",
  "when": {
    "type": "fileEdited",
    "patterns": ["**/*.njk", "**/*.html"]
  },
  "then": {
    "type": "askAgent",
    "prompt": "A GOV.UK template was saved. Review it for accessibility issues: missing labels, absent aria-describedby on error messages, images without alt text, heading hierarchy problems, and non-descriptive link text. Report issues with line numbers and fixes. Do not make changes — report only."
  }
}
```

**Documentation sync after API changes:**

```json
{
  "name": "docs-sync",
  "description": "Updates API documentation when route handlers change",
  "version": "1",
  "when": {
    "type": "fileEdited",
    "patterns": ["src/routes/**/*.ts", "src/controllers/**/*.ts"]
  },
  "then": {
    "type": "askAgent",
    "prompt": "A route or controller file changed. Review the changes and update the corresponding documentation in docs/api/. Update endpoint descriptions, request/response schemas, and examples where they have changed. Do not remove documentation for endpoints that still exist."
  }
}
```

**Run security scan before spec tasks execute:**

```json
{
  "name": "pre-task-security",
  "description": "Validates security requirements before task execution",
  "version": "1",
  "when": {
    "type": "preTaskExecution"
  },
  "then": {
    "type": "askAgent",
    "prompt": "Before this spec task executes, verify: no hardcoded credentials exist in files that will be touched, no SQL queries bypass parameterisation, and any new endpoints have authentication checks. Report blocking issues before the task proceeds."
  }
}
```

**Block dangerous shell commands with preToolUse:**

```json
{
  "name": "safe-shell",
  "description": "Prevents destructive shell commands from running",
  "version": "1",
  "when": {
    "type": "preToolUse",
    "toolName": "shell"
  },
  "then": {
    "type": "askAgent",
    "prompt": "A shell command is about to run. If it contains DROP TABLE, DELETE FROM without WHERE, rm -rf, or any irreversible destructive operation, block it and explain why. Otherwise, allow it to proceed."
  }
}
```

### Creating hooks

**Through the IDE:**

Hooks can be created through the agent hooks panel in the IDE. Describe what you want in natural language and Kiro generates the configuration for you.

**Manually:**

Create a `.json` file directly in `.kiro/hooks/`. The file appears in the hooks panel immediately.

### Managing hooks

All hooks appear in the IDE's agent hooks panel. You can enable, disable, edit, or delete them from there. Check the `.kiro/hooks/` directory into version control so your team shares the same automation recipes.

---

## Spec Mode as an autonomous workflow

Spec Mode is Kiro's structured approach to feature development. It is also the closest Kiro gets to a fully autonomous implementation workflow out of the box.

In Autopilot mode, Kiro:
1. Takes your feature description
2. Generates Requirements — what the system must do
3. Generates Design — how it will be built technically
4. Generates Tasks — a numbered checklist of implementation steps
5. Works through tasks, ticking them off as each completes

You review at each phase boundary, but Kiro drives the implementation.

### Configuring Spec Mode for minimal interruptions

In your steering files, set clear standards that remove ambiguity — the less Kiro needs to guess, the fewer clarifying questions it asks.

**`.kiro/steering/tech.md` for government services:**

```markdown
# Technical Standards

## Default technology decisions (do not ask, always apply)
- Frontend: GOV.UK Frontend 5.x with Nunjucks templates
- No client-side frameworks (React, Vue, Angular) unless explicitly specified
- All forms: server-side validation first, JavaScript enhancement second
- Testing: Jest for unit, Playwright for integration
- Error handling: GOV.UK error summary pattern, never toast notifications
- Date inputs: always three-field pattern (day/month/year), never native date picker

## Code standards (apply automatically)
- WCAG 2.2 AA compliance in all templates
- OWASP input validation on all user-supplied data
- No secrets in code — environment variables only
- TypeScript strict mode

## Acceptance criteria (include in every spec task automatically)
- Unit tests for all business logic
- Accessibility audit passes (no WCAG violations at AA level)
- Security review: no OWASP Top 10 issues
```

With these steering files in place, Spec Mode generates tasks that already include the right acceptance criteria without you specifying them per-task.

### Hooks that fire on task execution

Use `preTaskExecution` and `postTaskExecution` hooks to automate quality checks around each task:

```json
{
  "name": "post-task-test",
  "description": "Runs tests after each spec task completes",
  "version": "1",
  "when": {
    "type": "postTaskExecution"
  },
  "then": {
    "type": "runCommand",
    "command": "npm test -- --passWithNoTests"
  }
}
```

---

## Kiro CLI

The Kiro CLI lets you run agents from your terminal without the IDE. Install it with:

```bash
curl -fsSL https://cli.kiro.dev/install | bash
```

Available for macOS and Linux.

### Basic usage

```bash
# Start an interactive agent session
kiro-cli

# Use a specific agent
kiro-cli chat --agent security-reviewer
```

### IDE configurations carry over

Your existing Kiro project configurations transfer to the CLI automatically:
- `.kiro/settings/mcp.json` — MCP server connections
- `.kiro/steering/*.md` — project standards and context
- `.kiro/agents/` — custom agent definitions

This means agents you create in the IDE work identically in the CLI and in CI/CD pipelines.

### CLI agent configuration

CLI agents support `resources` to load steering files automatically:

```json
{
  "name": "ci-reviewer",
  "description": "Reviews code changes in CI pipeline",
  "prompt": "You are a code reviewer in a CI pipeline. Review the diff provided and report any issues blocking release.",
  "tools": ["read"],
  "resources": [".kiro/steering/tech.md", ".kiro/steering/product.md"]
}
```

### Use in CI/CD

The Kiro CLI enables AI-assisted checks in your pipeline without requiring the IDE:

```yaml
# GitHub Actions example
- name: AI code review
  run: |
    kiro-cli chat --agent ci-reviewer \
      --input "$(git diff ${{ github.event.before }}..HEAD)" \
      --output-format json
```

---

## Kiro autonomous agent (preview)

The Kiro autonomous agent is a cloud-based system that handles long-running tasks asynchronously — without requiring an active IDE session.

### What it does

- Accepts a high-level task description
- Spins up an isolated sandbox environment mirroring your setup
- Clones and analyses the relevant repositories
- Breaks work into requirements and acceptance criteria
- Coordinates specialist sub-agents for research, coding, and verification
- Opens pull requests with detailed change explanations
- Never merges changes automatically — all changes require your review

### Multi-repository coordination

Unlike in-IDE agents working on a single project, the autonomous agent can coordinate changes across multiple repositories simultaneously. Upgrading a shared library used by 15 microservices becomes a single task rather than 15 separate operations.

### Integration

During preview, the autonomous agent integrates with:
- GitHub and GitLab (for repository access and PR creation)
- Jira and Confluence (for ticket and documentation context)
- Slack and Teams (for notifications)

Assign tasks by attaching the `kiro` label to a GitHub issue, or mentioning `/kiro` in an issue comment.

### Security controls

The autonomous agent offers tiered network access:
- **Integration only** — access to GitHub/GitLab proxy only
- **Common dependencies** — access to npm, PyPI, Maven registries
- **Open internet** — with optional domain allowlists

Environment variables and credentials are encrypted and never exposed in logs or pull requests.

### When to use the autonomous agent vs in-IDE agents

| Scenario | Use |
|----------|-----|
| Quick review or fix during development | In-IDE agent or hook |
| Automated check on every file save | Hook |
| Long-running refactor across many files | Autonomous agent |
| Cross-repository coordination | Autonomous agent |
| CI/CD integration | Kiro CLI |
| Team needs to review changes before merge | Autonomous agent (creates PRs) |

---

## Practical example: government service quality workflow

This example combines custom agents, hooks, and Spec Mode for a full automated quality workflow on a GOV.UK digital service.

### Custom agents

**`.kiro/agents/accessibility-reviewer.md`**

```markdown
---
name: accessibility-reviewer
description: Reviews templates for WCAG 2.2 AA compliance and GOV.UK Design System conformance
model: claude-sonnet-4
tools: ["read"]
resources: [".kiro/steering/tech.md"]
---

You are an accessibility specialist reviewing government service templates.

Systematically check:
- Form inputs: every input must have a visible label, not placeholder-only
- Error handling: error summary required at page top, aria-describedby on each field with an error
- GOV.UK components: use govukInput, govukRadios, etc. — not native HTML inputs
- Date fields: three-field pattern only (day/month/year) — never native date picker
- Heading hierarchy: one h1 per page, no skipped levels
- Images: meaningful images need descriptive alt text, decorative images need alt=""
- Links: descriptive text that makes sense out of context

Report findings as: file path | line number | WCAG criterion | severity | fix
```

**`.kiro/agents/security-reviewer.md`**

```markdown
---
name: security-reviewer
description: Reviews code for OWASP Top 10 vulnerabilities and government security requirements
model: claude-sonnet-4
tools: ["read"]
---

You are a security engineer auditing government service code.

Check for:
- SQL injection: parameterised queries required, no string concatenation in queries
- XSS: template output properly escaped, no raw HTML injection
- CSRF: form submissions protected
- Authentication: session configuration secure (httpOnly, secure, sameSite)
- Secrets: no hardcoded API keys, passwords, or tokens
- Input validation: all user-supplied data validated before use
- Error messages: no sensitive data exposed in errors or logs

Report: file | line | vulnerability type | severity (critical/high/medium/low) | remediation
```

### Hooks

**`.kiro/hooks/accessibility-check.kiro.hook`**

```json
{
  "name": "accessibility-check",
  "description": "Accessibility review on template save",
  "version": "1",
  "when": {
    "type": "fileEdited",
    "patterns": ["**/*.njk", "**/*.html", "!**/node_modules/**"]
  },
  "then": {
    "type": "askAgent",
    "prompt": "Use the accessibility-reviewer agent to check this template for WCAG 2.2 AA and GOV.UK Design System issues. Report only — do not make changes."
  }
}
```

**`.kiro/hooks/post-task-verify.kiro.hook`**

```json
{
  "name": "post-task-verify",
  "description": "Runs tests after each spec task completes",
  "version": "1",
  "when": {
    "type": "postTaskExecution"
  },
  "then": {
    "type": "runCommand",
    "command": "npm test -- --passWithNoTests && npx axe-core-cli http://localhost:3000"
  }
}
```

### How the workflow runs

1. You write a feature spec in Spec Mode
2. Kiro generates requirements, design, and task list
3. As Kiro implements each task, the `post-task-verify` hook runs tests automatically
4. When you save templates, the `accessibility-check` hook fires and flags WCAG issues
5. The `security-reviewer` agent is available on demand to audit completed features

---

## Tips and gotchas

### Hook glob patterns need care

Overly broad patterns trigger hooks on files you did not intend. Test patterns before relying on them:

- `**/*.ts` matches all TypeScript — use `src/**/*.ts` to limit to source files
- Add `!**/node_modules/**` and `!**/dist/**` to exclude generated files
- For deployment hooks specifically, use `**/pipeline*.yml` or `**/deploy/**/*.yaml`

### Avoid hook-agent circular triggers

If a hook fires an agent that modifies a file, and that modification triggers another hook, you can create loops. Break the cycle by:
- Naming agent-generated files with a pattern you exclude from hook patterns
- Using `postToolUse` hooks only on specific tool types, not broadly
- Adding debounce logic for hooks that could retrigger

### Spec tasks work best with granular, time-bounded scope

When generating tasks in Spec Mode, aim for tasks completable in 30-60 minutes with clear done criteria. If a generated task is too broad ("implement authentication"), ask Kiro to break it down before proceeding.

### Steering files are always loaded first

Custom agents with `resources` load steering files into their context at startup. Make sure your steering files are accurate — outdated technology choices in `tech.md` will produce outdated code from every agent.

### The autonomous agent never merges

If you are evaluating the Kiro autonomous agent, protect your main branch from direct pushes in your GitHub or GitLab settings. The agent creates pull requests — you review and merge. This is intentional: human review remains in the loop.

---

## Where to go next

- [Kiro hooks documentation](https://kiro.dev/docs/hooks/)
- [Kiro autonomous agent](https://kiro.dev/autonomous-agent/)
- [Kiro CLI](https://kiro.dev/blog/introducing-kiro-cli/)
- [Kiro agent configuration](https://kiro.dev/docs/agents/)
- [Agentic AI guide](agentic-ai-guide.md) — comparison with Claude Code and pattern recommendations for each challenge level
