# Glossary

Key terms and concepts for AI-assisted development.

## Core concepts

### Agentic AI
AI that takes actions rather than just suggesting them. An agentic coding assistant can create files, run commands, and modify code directly - not just tell you what to do. This requires more trust but dramatically increases productivity.

### Context window
The amount of text an AI can consider at once, measured in tokens. Larger context windows let the AI understand more of your codebase simultaneously. When you exceed the context window, the AI "forgets" earlier parts of the conversation.

### Tokens
Units of text that AI models process. Roughly 4 characters per token in English. A 200,000 token context window means the AI can consider approximately 150,000 words at once. Token usage affects API costs.

### Prompt
Instructions or questions you give to an AI. Better prompts produce better results. Effective prompts are specific, provide context, and clearly state what you want.

### Hallucination
When an AI generates plausible-sounding but incorrect information. Common with API names, library functions, or specific technical details. Always verify AI-generated code works as expected.

### Large Language Model (LLM)
The underlying AI technology powering coding assistants. Trained on vast amounts of text and code to predict and generate human-like responses. Examples: Claude, GPT-4, Gemini.

## Tool-specific terms

### MCP (Model Context Protocol)
An open protocol that lets AI assistants connect to external tools and data sources. MCP servers extend what your AI can do - accessing databases, APIs, or specialised tools. Both Claude Code and Kiro support MCP.

### Agents
Specialised AI personas configured for specific tasks. In Kiro, agents live in `.kiro/agents/` and have custom system prompts defining their expertise (security reviewer, accessibility auditor). In other tools, "agent" may refer to the AI's ability to work autonomously.

### Hooks
Event-driven automation triggers. When something happens (file saved, code committed), a hook can automatically run checks, format code, or invoke agents. Kiro uses hooks in `.kiro/hooks/`. Claude Code uses hooks configured in settings.

### Steering files
Configuration files that give Kiro persistent context about your project. Located in `.kiro/steering/`, they describe your product, tech stack, and codebase structure. Similar in purpose to CLAUDE.md files.

### CLAUDE.md
Memory files for Claude Code. Claude reads these at session start to understand your project. Can exist at project root, in parent directories, or in your home folder (`~/.claude/CLAUDE.md`). Provides persistent context across sessions.

### Specs (Specifications)
Structured documents in Kiro capturing requirements, design decisions, and implementation tasks. Created through Spec Mode, they provide traceability from "why" to "what" to "how". Stored in `.kiro/specs/`.

### Vibe Mode
Kiro's conversational mode for quick tasks. Chat naturally, let it code, iterate fast. Best for prototyping, bug fixes, and exploration.

### Spec Mode
Kiro's structured mode for complex features. Follows a Requirements → Design → Tasks workflow. Best for production code, team projects, and anything needing documentation.

### Slash commands
Custom commands in Claude Code created as markdown files in `.claude/commands/`. A file named `review.md` becomes the command `/project:review`. Useful for standardising common prompts across a team.

### Custom commands
Reusable prompt templates. In Claude Code, these are slash commands. In Kiro, similar functionality comes through agents and the command palette.

## Development workflow terms

### CI/CD (Continuous Integration / Continuous Deployment)
Automated pipelines that build, test, and deploy code when changes are pushed. AI assistants can help generate pipeline configurations and deployment scripts.

### Pair programming
Two developers working together on the same code. AI coding assistants function as a virtual pair programmer - one who never gets tired and has read a lot of documentation.

### Code review
Examining code changes before merging. AI assistants can perform initial reviews, checking for common issues, but human review remains important for architectural decisions and business logic.

### Refactoring
Restructuring existing code without changing its behaviour. AI assistants excel at mechanical refactoring tasks like renaming, extracting functions, and updating patterns across files.

## Government-specific terms

### GDS (Government Digital Service)
The UK government organisation that sets standards for digital services. Their Service Standard defines how government services should be built and operated.

### WCAG (Web Content Accessibility Guidelines)
International standards for web accessibility. UK government services must meet WCAG 2.2 AA level. AI assistants can help check compliance but automated testing alone is insufficient.

### GOV.UK Design System
Component library and design patterns for UK government services. Ensures consistency across government websites. AI assistants should generate code that uses these patterns.

### Service Standard
GDS's 14-point standard for building government services. Covers user needs, accessibility, technology choices, and operational requirements. Point 8 (performance) and Point 10 (testing) are particularly relevant to these challenges.

## Common abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CLI | Command Line Interface |
| IDE | Integrated Development Environment |
| JSON | JavaScript Object Notation |
| LLM | Large Language Model |
| MCP | Model Context Protocol |
| PR | Pull Request |
| UI | User Interface |
| UX | User Experience |

## Tool comparison

| Concept | Claude Code | AWS Kiro |
|---------|-------------|----------|
| Project memory | CLAUDE.md files | Steering files |
| Custom prompts | Slash commands | Agents |
| Automation | Hooks (in settings) | Hooks (in .kiro/hooks/) |
| Extensions | MCP servers | MCP servers + Agents |
| Operating modes | Single conversational mode | Vibe Mode + Spec Mode |
| Structured workflow | Manual | Built-in specs |
| Configuration location | .claude/ | .kiro/ |

## Further reading

- **Claude Code documentation**: https://docs.anthropic.com/en/docs/claude-code
- **AWS Kiro documentation**: https://kiro.dev/docs
- **MCP specification**: https://modelcontextprotocol.io
- **GDS Service Standard**: https://www.gov.uk/service-manual/service-standard
- **WCAG guidelines**: https://www.w3.org/WAI/standards-guidelines/wcag/
