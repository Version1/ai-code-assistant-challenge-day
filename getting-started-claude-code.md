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

Claude Code requires Node.js 18 or higher. Check your version with `node --version` and update if needed.

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Authenticate

```bash
claude login
```

This opens a browser window to authenticate with your Anthropic account.

Alternatively, you can authenticate using:

- **Environment variable**: Set `ANTHROPIC_API_KEY` with your API key
- **Command line flag**: Pass `--api-key YOUR_KEY` when starting Claude Code

### 3. Verify installation

Check Claude Code is installed correctly:

```bash
claude --version
```

Then start a Claude Code session and run the `/doctor` slash command to check your setup:

```bash
claude
```

```
> /doctor
```

The `/doctor` command runs inside an active session and reports any configuration issues.

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

**A note on /compact**: This command uses Claude to summarise the conversation, which itself consumes tokens and may lose some context details. Worth the trade-off for long sessions where you have built up extensive context, but be aware you may need to re-explain some nuances afterwards.

### Model selection

Claude Code can use different Claude models depending on your needs:

| Model | Best for |
|-------|----------|
| claude-sonnet-4-5-20250929 | Most work - balanced speed and capability |
| claude-opus-4-5-20251101 | Complex reasoning - most capable but slower |
| claude-haiku-3-5-20241022 | Quick simple tasks - fastest and cheapest |

**How to select a model**:

- During a session: Use the `/model` command
- When starting: Use the `--model` flag (e.g., `claude --model claude-opus-4-5-20251101`)
- As a default: Set the `CLAUDE_MODEL` environment variable

**General guidance**: Start with Sonnet for everyday work. Switch to Opus when you need deeper analysis or complex multi-step reasoning. Use Haiku for quick questions or simple tasks where speed matters more than depth.

Use `/cost` to track your token usage across different models.

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

**How multiple CLAUDE.md files are loaded**: When CLAUDE.md files exist in multiple locations, they are all concatenated together - not overridden. The loading order is:

1. User-level (`~/.claude/CLAUDE.md`) - your personal preferences and defaults
2. Parent directories - working down through the folder hierarchy
3. Project root - the most specific context for this project

This means you can set general coding standards at your user level, team conventions in a shared parent folder, and project-specific details at the root. All of this context is available to Claude Code in every session.

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

### Agents

Agents are specialised AI personas with custom system prompts for specific tasks. While custom slash commands give you reusable prompts, agents go further - they change how Claude Code thinks and responds for an entire interaction.

Use agents when you need Claude Code to adopt a particular mindset or expertise, such as reviewing code for security vulnerabilities, auditing accessibility, or writing tests in a specific style.

#### Where agent files live

Create agent configuration files in `.claude/agents/`:

```
project/
  .claude/
    agents/
      security-reviewer.json    <- becomes /security-reviewer
      a11y-auditor.json         <- becomes /a11y-auditor
      test-writer.json          <- becomes /test-writer
```

You can also create user-level agents in `~/.claude/agents/` that work across all your projects. Project-level agents override user-level agents with the same identifier.

#### Configuration format

Each agent file uses JSON with three required fields:

```json
{
  "identifier": "security-reviewer",
  "whenToUse": "Review code for security vulnerabilities and OWASP Top 10 issues",
  "systemPrompt": "You are a senior security engineer conducting a code review. Focus on identifying vulnerabilities including injection flaws, authentication issues, data exposure risks, and insecure configurations.\n\nFor each issue found, provide:\n- Severity (critical, high, medium, low)\n- Location in the code\n- Explanation of the risk\n- Recommended fix with code example"
}
```

- **identifier**: The name you use to invoke the agent (no spaces)
- **whenToUse**: A description that helps you remember what this agent does
- **systemPrompt**: Instructions that shape how Claude Code behaves when this agent is active

#### Example agents

**Accessibility auditor** - Reviews code against WCAG guidelines:

```json
{
  "identifier": "a11y-auditor",
  "whenToUse": "Audit components for accessibility compliance",
  "systemPrompt": "You are an accessibility specialist auditing code against WCAG 2.1 AA standards.\n\nCheck for:\n- Semantic HTML usage\n- Keyboard navigation support\n- Screen reader compatibility\n- Colour contrast issues\n- Focus management\n- ARIA attribute correctness\n\nProvide specific fixes with code examples."
}
```

**Test writer** - Generates tests following your project's patterns:

```json
{
  "identifier": "test-writer",
  "whenToUse": "Write unit and integration tests",
  "systemPrompt": "You write tests following these principles:\n- One assertion per test where practical\n- Descriptive test names that explain the scenario\n- Arrange-Act-Assert structure\n- Mock external dependencies\n- Test edge cases and error conditions\n\nMatch the testing patterns already used in this project."
}
```

#### Invoking agents

Use a forward slash followed by the agent identifier:

```
> /security-reviewer Check the authentication module in src/auth/
```

```
> /a11y-auditor Review the form components in src/components/forms/
```

```
> /test-writer Write tests for the user service in src/services/user.js
```

The agent's system prompt shapes Claude Code's response for that specific request.

#### Tips for writing effective agents

**Keep system prompts focused** - Aim for under 1500 words. A concise prompt that covers the essentials works better than an exhaustive one.

**Use newlines for readability** - In JSON, use `\n` for line breaks within the systemPrompt value:

```json
"systemPrompt": "First paragraph.\n\nSecond paragraph with a list:\n- Item one\n- Item two"
```

**Escape quotes properly** - If your prompt includes quotation marks, escape them with a backslash:

```json
"systemPrompt": "When reviewing code, ask \"What could go wrong here?\""
```

**Test your agents** - After creating an agent, invoke it with a simple request to check the prompt works as expected.

**Combine with custom commands** - For complex workflows, create a custom command that invokes an agent with specific instructions.

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

### Hooks

Hooks let you run commands automatically before or after Claude Code takes actions. They are configured in `.claude/settings.json` and are useful for automating repetitive tasks like formatting code or running linters.

**Event types**:

- **PreToolUse** - Runs before Claude Code uses a tool (such as writing a file or running a command)
- **PostToolUse** - Runs after a tool completes
- **Notification** - Runs when Claude Code sends a notification
- **Stop** - Runs when Claude Code stops working on a task

**Example: Auto-format code after writes**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

This hook runs Prettier on any file Claude Code writes, keeping your code formatted without manual intervention. The `$CLAUDE_FILE_PATH` variable contains the path to the file that was just written.

Common uses include auto-formatting, running linters, triggering builds, or sending notifications when Claude Code completes tasks.

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

For trusted projects, you can pre-configure permissions in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git *)",
      "Write(src/**)"
    ],
    "deny": [
      "Bash(rm -rf *)"
    ]
  }
}
```

This example allows Claude Code to run npm scripts, use git commands, and write to files in the `src/` folder without asking. It blocks any `rm -rf` commands entirely. Adjust the patterns to match your workflow and risk tolerance.

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

### Use git integration

Claude Code works well with git. It can generate commit messages based on your changes, help create pull requests, and review code differences. Simply describe what you want to commit and ask Claude Code to help:

> I've finished the login form changes. Help me commit these with a good message.

> Review the changes I've made since the last commit and suggest improvements.

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

### Keyboard shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+C | Interrupt current operation |
| Ctrl+D | Exit Claude Code |
| Escape | Cancel current input |
| Up arrow | Browse command history |

---

You are now ready to start using Claude Code. Begin with a simple task to get comfortable with the workflow, then gradually tackle more complex challenges. Remember: context and specificity are your best tools for getting good results.
