# Getting Started with AWS Kiro

This guide covers everything you need to know to start using AWS Kiro effectively. Read this before your first session.

## What is AWS Kiro?

AWS Kiro is an agentic IDE built on VS Code that combines familiar coding with AI-powered development. Unlike traditional AI assistants that simply respond to prompts, Kiro can work autonomously on complex tasks, understand your entire project through steering files, and follow structured development workflows. Think of it as having an architect who can also do the building work.

## Key concepts

Before you start, understand these foundational ideas:

### Kiro has two modes

**Vibe Mode** is for quick tasks - prototyping, exploration, simple fixes. Just chat and let it code.

**Spec Mode** is for complex features - production code, team projects, anything you would write a design document for. It follows a Requirements to Design to Tasks workflow.

Rule of thumb: If you would write a design doc for it anyway, use Spec Mode.

### Steering files give Kiro context

Steering files tell Kiro about your project - your tech stack, coding standards, and architecture. Without them, you get generic solutions. With them, you get code that fits your codebase.

### Specs create traceability

Specs are structured documents that capture requirements, design decisions, and implementation tasks. They create an audit trail from "why" to "what" to "how" - useful for complex features and team handovers.

### Agents and hooks automate expertise

Agents are specialised AI personas for specific tasks (security review, accessibility audit). Hooks are event-driven triggers that automate repetitive workflows (format on save, run tests on commit).

## Essential setup

Complete these steps before your first coding session:

### 1. Install Kiro

Download and install from kiro.dev. It runs as a standalone IDE based on VS Code.

### 2. Open your project

Launch Kiro and open your project folder, just as you would in VS Code.

### 3. Create the .kiro directory structure

Create this folder structure at your project root:

```
project/
  .kiro/
    steering/
      product.md     <- What your product does
      tech.md        <- Your tech stack and standards
      structure.md   <- How your codebase is organised
    agents/          <- Custom AI personas
    hooks/           <- Automation triggers
    specs/           <- Feature specifications
    settings/        <- Kiro configuration
```

### 4. Set up basic steering files

Start with these three files in `.kiro/steering/`:

**product.md** - What your product does, who it serves, core features

**tech.md** - Languages, frameworks, coding standards, testing approach

**structure.md** - Key directories, important files, architectural patterns

Ten minutes here saves hours later. Kiro reads these files to understand your project context.

## Core workflow

### Vibe Mode - for quick tasks

1. Open the Kiro chat panel
2. Describe what you want
3. Let Kiro code
4. Review and iterate

Use for: bug fixes, small features, exploring ideas, learning a codebase.

### Spec Mode - for complex features

1. Describe the feature you want to build
2. Kiro generates a Requirements document - review and edit
3. Kiro generates a Design document - review and edit
4. Kiro generates a Task list with checkboxes
5. Work through tasks, ticking them off as you go

Use for: new features, refactoring, anything that affects multiple files or needs documentation.

## Key features

### Steering files - project memory

Steering files in `.kiro/steering/` persist context across sessions. Unlike chat history, they survive when you close and reopen Kiro.

Update them when:

- Your tech stack changes
- You establish new patterns
- You want to enforce standards

### Specs - structured development

Specs live in `.kiro/specs/` and capture the full journey from requirement to implementation. Each spec contains:

- **Requirements**: What and why
- **Design**: How, with technical decisions
- **Tasks**: Step-by-step implementation checklist

Keep specs focused - one feature per spec. Overly broad specs become unwieldy.

### Agents - domain expertise

Agents in `.kiro/agents/` are custom AI personas with specific expertise. Create agents for:

- Security review
- Accessibility audit
- Performance analysis
- Code review against your standards

### Hooks - automation

Hooks in `.kiro/hooks/` trigger on events like file save or commit. Use them to:

- Auto-format code
- Run linting
- Execute tests
- Update documentation

## Tips for effective use

### Invest in steering files

The single biggest factor in getting good results is context. Spend time on your steering files. Be specific about your standards and patterns.

### Start with Vibe, graduate to Spec

Get comfortable with conversational coding before tackling the structured workflow. Vibe Mode teaches you how Kiro thinks.

### Review generated specs

Specs are editable documents, not sacred texts. Kiro drafts them; you refine them. The requirements and design phases are where you catch mistakes early.

### Keep specs focused

One feature per spec. If your spec has multiple unrelated requirements, split it up. Focused specs produce better implementations.

### Iterate on steering as your project evolves

Steering files are living documents. Update them as you establish patterns, change technologies, or learn what works.

## Where to get help

### Documentation

- **Official docs**: kiro.dev/docs
- **Quick start**: kiro.dev/docs/getting-started

### Within Kiro

Ask Kiro about Kiro. It knows its own capabilities and can explain features.

### Workshop support

- Facilitators are available throughout the session
- The 09:00-09:30 AI Clinic provides setup support
- Peer learning with your team

### Community

- Discord community for discussions and tips

## Common gotchas

### Forgetting steering files

**Problem**: Kiro generates code that does not match your project patterns or tech stack.

**Solution**: Create steering files before serious coding. Even basic context dramatically improves results.

### Using Spec Mode for trivial tasks

**Problem**: You spend more time on requirements and design than the task warrants.

**Solution**: Use Vibe Mode for quick fixes and small tasks. Reserve Spec Mode for features that genuinely need structure.

### Skipping the design phase

**Problem**: You rush through specs to get to implementation, then hit architectural problems.

**Solution**: The design phase exists to catch issues early. Review it properly. Changing a document is cheaper than changing code.

### Overly broad specs

**Problem**: Your spec tries to cover an entire system, becoming unwieldy and producing unfocused output.

**Solution**: One feature per spec. Break large initiatives into multiple focused specs.

### Not reviewing generated content

**Problem**: You accept Kiro's output without checking, introducing inconsistencies or errors.

**Solution**: Review everything - requirements, design, and code. Kiro drafts; you approve.

### Outdated steering files

**Problem**: Your project has evolved but your steering files still describe the old approach.

**Solution**: Update steering files when patterns change. Outdated context produces outdated solutions.

### Missing .kiro directory in git

**Problem**: Your team cannot benefit from your steering files and specs because they are not committed.

**Solution**: Add `.kiro/` to version control. Steering files and specs are project documentation - share them.

### Expecting magic without context

**Problem**: You ask Kiro to build something complex without explaining your requirements, standards, or constraints.

**Solution**: Context is everything. The more Kiro knows about what you need, the better the results.

## Quick reference

### Starting a session

1. Launch Kiro
2. Open your project folder
3. Verify `.kiro/` directory exists with steering files

### First actions in a new project

1. Create `.kiro/` directory structure
2. Write basic steering files (product.md, tech.md, structure.md)
3. Start with a simple Vibe Mode task to test setup
4. Graduate to Spec Mode for complex features

### Choosing your mode

| Situation | Use |
|-----------|-----|
| Quick fix or bug | Vibe Mode |
| Exploring an idea | Vibe Mode |
| Learning a codebase | Vibe Mode |
| New feature | Spec Mode |
| Multi-file refactor | Spec Mode |
| Team project | Spec Mode |
| Production code | Spec Mode |

### When things go wrong

1. Check your steering files are up to date
2. Be more specific in your prompts
3. For Spec Mode issues, review and edit the requirements and design documents
4. Ask Kiro to explain its approach before implementing
5. Start fresh if context becomes confused

---

You are now ready to start using AWS Kiro. Begin with Vibe Mode on a simple task to get comfortable, then try Spec Mode on a feature that would benefit from structured documentation. Remember: steering files and specificity are your best tools for getting good results.
