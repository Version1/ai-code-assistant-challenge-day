# Getting Started with Claude Code

This guide covers everything you need to know to start using Claude Code effectively. Read this before your first session.

## What is Claude Code?

Claude Code is Anthropic's official command-line interface for Claude. Unlike chat-based AI tools, Claude Code runs in your terminal and can directly read, write, and execute code in your development environment. It understands your project context, runs commands, creates files, and works alongside you as an agentic coding assistant. Think of it as having a senior developer pair-programming with you who can actually type.

## Key concepts

Before you start, understand these foundational ideas:

### Claude Code is agentic

Claude Code does not just suggest code - it takes action. When you ask it to create a file, it creates the file. When you ask it to run tests, it runs them. This makes it powerful but means you should review what it does.

### Context is everything

Claude Code works better when it understands your project. The more context you provide (through CLAUDE.md files, clear prompts, and project structure), the better the results. Without context, you get generic solutions.

### Conversations have memory within a session

During a single session, Claude Code remembers everything you have discussed. It knows what files you have worked on, what decisions you made, and what you are trying to achieve. This compounds - early context improves later work.

### Sessions are ephemeral

When you start a new session (or run `/clear`), Claude Code forgets the conversation. This is why CLAUDE.md files matter - they persist context across sessions.

## Essential setup

Complete these steps before your first coding session:

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Authenticate

```bash
claude login
```

This opens a browser window to authenticate with your Anthropic account.

### 3. Verify installation

```bash
claude --version
claude /doctor
```

The `/doctor` command checks your setup and reports any issues.

### 4. Navigate to your project

```bash
cd your-project-folder
claude
```

Claude Code launches in interactive mode within your project directory.

## Core commands

These slash commands are the ones you will use most often:

| Command | Purpose | When to use |
|---------|---------|-------------|
| `/help` | Show all available commands | When you forget a command |
| `/memory` | Add persistent context to CLAUDE.md | At project start, when requirements change |
| `/compact` | Summarise conversation to free context | When responses slow down or become less accurate |
| `/clear` | Start fresh conversation | When switching tasks or context becomes confused |
| `/cost` | Show session token usage | To monitor API costs |
| `/status` | Show current session state | To check model, permissions, context |
| `/add-dir` | Include additional directories | When working across multiple folders |
| `/model` | Change the Claude model | When you need different capabilities |

### Using commands

Type the command directly in the Claude Code prompt:

```
> /memory
```

Some commands accept arguments:

```
> /add-dir ../shared-library
```

## Key features

### CLAUDE.md - project memory

CLAUDE.md files store persistent context that Claude Code reads at the start of every session. Create one at your project root:

```
project/
  CLAUDE.md          <- Claude reads this automatically
  src/
  package.json
```

Use `/memory` to add content, or edit the file directly. Include:

- Project purpose and architecture
- Coding standards and conventions
- Technology stack and versions
- Patterns to follow or avoid

Claude Code also reads CLAUDE.md files from parent directories and your home folder (`~/.claude/CLAUDE.md`), giving you layered context from personal preferences to project specifics.

### Custom slash commands

Create reusable prompts in `.claude/commands/`:

```
project/
  .claude/
    commands/
      review.md      <- becomes /project:review
      test.md        <- becomes /project:test
```

Command files contain the prompt template. Use `$ARGUMENTS` to accept parameters:

```markdown
---
description: Run security review on specified file
---

Review $ARGUMENTS for security vulnerabilities. Check for:
- Input validation issues
- Authentication flaws
- Data exposure risks

Report findings with severity and fix recommendations.
```

Invoke with: `/project:review src/auth.js`

### MCP servers

Model Context Protocol (MCP) servers extend Claude Code with additional capabilities - database access, external APIs, specialised tools. Configure them in `.claude/settings.json`:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@your-org/mcp-server"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

#### UK Government MCP servers

Two MCP servers are available for UK public sector challenges:

**Government AI SDLC** - Provides guidance on secure development lifecycle practices for government projects:

```json
{
  "mcpServers": {
    "gov-sdlc": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-fetch"],
      "env": {}
    }
  }
}
```

Repository: https://github.com/Version1/uk-gov-example-ai-sdlc

**Government Tech Standards** - Provides access to UK government technology standards and compliance requirements:

Repository: https://github.com/Version1/uk-gov-tech-standards-mcp

Follow the setup instructions in each repository's README to configure the servers for your environment.

For more on MCP configuration, see the official documentation: https://docs.anthropic.com/en/docs/claude-code/mcp

### Permissions

Claude Code asks permission before potentially risky actions (writing files, running commands, accessing the network). You will see prompts like:

```
Claude wants to write to src/app.js
Allow? [y/n/always]
```

Options:
- `y` - Allow this once
- `n` - Deny this action
- `always` - Allow this action type for the session

For trusted projects, you can pre-configure permissions in settings.json.

## Tips for effective prompting

### Be specific about requirements

Instead of:

> Create a form

Say:

> Create a form with fields for name (required, max 100 chars), email (required, validated), and message (optional, max 500 chars). Use semantic HTML with accessible labels.

### Provide context and examples

Instead of:

> Add validation

Say:

> Add validation following the pattern in user-form.js. Show inline errors below each field. Use our existing ErrorMessage component from components/forms/.

### Break complex tasks into steps

Instead of:

> Build me a complete user authentication system

Say:

> Let's build user authentication. Start with the login form component. We will add the API integration and session handling next.

### Ask Claude Code to explain its approach

> Before implementing, explain your approach and what files you will create.

This lets you course-correct before code is written.

### Use the project memory

Start sessions by asking Claude Code to read and confirm it understands the CLAUDE.md:

> Read CLAUDE.md and summarise the key requirements you need to follow.

### Request verification

> After making these changes, verify the tests still pass.

> Check this code against our accessibility requirements.

## Where to get help

### Documentation

- **Official docs**: https://docs.anthropic.com/en/docs/claude-code
- **Quickstart**: https://docs.anthropic.com/en/docs/claude-code/quickstart
- **MCP configuration**: https://docs.anthropic.com/en/docs/claude-code/mcp

### Within Claude Code

- `/help` - List all commands
- `/doctor` - Diagnose setup issues
- Ask Claude Code directly: "How do I use custom commands?"

### Workshop support

- Facilitators are available throughout the session
- The 09:00-09:30 AI Clinic provides setup support
- Peer learning with your team

### Community

- Anthropic Discord server
- GitHub issues for bug reports

## Common gotchas

### Forgetting to use /memory

**Problem**: You explain project requirements in conversation, then start a new session and Claude Code has no idea what you were doing.

**Solution**: Use `/memory` to save important context to CLAUDE.md before ending sessions.

### Letting context grow too large

**Problem**: After extensive conversation, Claude Code becomes slow and starts forgetting earlier context.

**Solution**: Run `/compact` periodically to summarise and free up context space. Start fresh with `/clear` when switching to unrelated tasks.

### Not reviewing generated code

**Problem**: Claude Code writes code that technically works but does not follow your patterns or introduces subtle issues.

**Solution**: Always review generated code. Ask Claude Code to explain its choices. Request changes when something is not right.

### Accepting the first solution

**Problem**: The first attempt works but is not optimal.

**Solution**: Iterate. Ask "Can this be improved?" or "What are the alternatives?" Claude Code often has better solutions when pushed.

### Not using custom commands

**Problem**: You keep typing the same complex prompts repeatedly.

**Solution**: Create custom commands in `.claude/commands/` for frequently used prompts. This ensures consistency and saves time.

### Ignoring the cost command

**Problem**: You are surprised by API usage.

**Solution**: Run `/cost` periodically to understand token consumption. Use `/compact` to reduce ongoing costs.

### Starting without context

**Problem**: You jump straight into coding without setting up project context.

**Solution**: Spend the first few minutes of any project setting up CLAUDE.md with requirements, standards, and patterns. This investment pays off immediately.

### Vague prompts for complex tasks

**Problem**: "Make it better" or "Fix the bugs" produces unhelpful results.

**Solution**: Be specific. "Improve the error handling in auth.js to provide user-friendly messages and log technical details to our logging service."

## Quick reference

### Starting a session

```bash
cd your-project
claude
```

### First actions in a new project

1. Run `/doctor` to check setup
2. Create or review CLAUDE.md with `/memory`
3. Add any custom commands you need
4. Begin work

### Ending a session

1. Run `/cost` to check usage
2. Use `/memory` to save any important context
3. Exit with Ctrl+C or Ctrl+D

### When things go wrong

1. `/doctor` - Check for setup issues
2. `/clear` - Reset if context is confused
3. `/status` - Verify current state
4. Be more specific in your prompts
5. Ask Claude Code to explain what it is trying to do

---

You are now ready to start using Claude Code. Begin with a simple task to get comfortable with the workflow, then gradually tackle more complex challenges. Remember: context and specificity are your best tools for getting good results.
