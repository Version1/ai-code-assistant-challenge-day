# AI Code Assistant Gameday for UK Public Sector teams

Welcome to the AI Code Assistant (AICA) Gameday challenges. This event has been pulled together to provide practical AI coding existing experience through progressive challenge based learning, working in teams of 2-3, focusing on real-world government delivery scenarios.

## Workshop Objectives

- **Challenge-Based Learning**: Progressive 10-level challenge system with increasing difficulty and scoring
- **Practical AI Experience**: Hands-on experience with modern AI development tools (we've included guides for Claude Code and Amazon Kiro - these challenges work for any AICA, and we'll add more guides for more tools in the near future)
- **Production-Ready Practices**: Focus on maintainable, scalable, and secure solutions suitable for government services
- **Collaborative Problem Solving**: Team-based challenges tackling real government service scenarios
- **Knowledge Transfer**: Create lasting resources for continued AI-assisted development across departments

New to AI coding assistants? See the **[Glossary](glossary.md)** for explanations of key terms like agents, MCP, hooks, and more.

### Challenge System
- **10-Level Challenge System** - Progressive challenges from Level 1 to Level 10
- **Level 1-3**: Foundation challenges (Digital transformation, data processing, data modeling)
- **Level 4-6**: Intermediate challenges (Legacy modernization, business logic, security)
- **Level 7-10**: Advanced challenges (Performance, testing, architecture, production deployment)

Each challenge directory contains:
- `challenge-summary.md` - What the challenge is and why it matters
- `playbook-claude-code.md` - Getting started guide for Claude Code users
- `playbook-aws-kiro.md` - Getting started guide for AWS Kiro users

#### Challenge Table

| Challenge Name | Difficulty Level |
|----------------|------------------|
| [PDF to Digital Service Transformation](level-01/) | Level 1 |
| [Data Processing & Visualisation](level-02/) | Level 2 |
| [Database-Backed CRUD Operations](level-03/) | Level 3 |
| [Legacy Code Modernisation](level-04/) | Level 4 |
| [Complex Business Logic Implementation](level-05/) | Level 5 |
| [Security Vulnerability Assessment & Remediation](level-06/) | Level 6 |
| [Performance Investigation & System Resilience](level-07/) | Level 7 |
| [Adaptive Testing Strategy & Risk-Based Quality Engineering](level-08/) | Level 8 |
| [Multi-Service Architecture Design](level-09/) | Level 9 |
| [Production Deployment & Incident Response](level-10/) | Level 10 |


## Gameday Schedule

### The schedule

| Time | Session | Summary |
|------|---------|---------|
| 09:00-09:30 | Optional AI Clinic | Optional support session for tooling setup, challenge selection guidance, and individual help getting started |
| 09:30-10:15 | Challenge Kick-Off | Introduction to 10-level challenge system, scoring explained, overview of available challenges, AI tools and prompting best practices refresher |
| 10:15-12:30 | Challenge Sprint 1 | Individual hands-on development working through selected challenges (Levels 1-10), facilitator support available, focus on practical implementation |
| 12:30-13:30 | Lunch | Working lunch with informal discussions, peer support and knowledge sharing encouraged |
| 13:30-15:30 | Challenge Sprint 2 | Final development push, challenge completion and documentation, consolidation of learning and insights |
| 15:30-16:15 | Group Feedback & Scoreboard Review | Collaborative discussion on tool effectiveness, successful approaches, prompting strategies, key insights, challenge completion scoring, and peer recognition with awards |
| 16:15-16:30 | Wrap-Up & Next Steps | Summary of collective learnings, resources for continued development, event conclusion |

## Context

All materials in this repository consider public sector requirements:
- **Security**: Government security standards and data protection requirements
- **Accessibility**: WCAG compliance and inclusive design principles
- **Transparency**: Open source approaches and auditable development practices
- **Scalability**: Patterns suitable for citizen-facing services at scale
- **Compliance**: GDS standards and cross-government best practices

## Supported AI Tools

While tool-agnostic in approach, the workshop focuses on:
- **Claude Code**: Anthropic's development-focused AI assistant
- **Amazon Kiro**: AI-powered development assistant
- **Amazon Q Developer**: AWS-integrated development assistant (formerly CodeWhisperer)
- **GitHub Copilot**: Traditional IDE-integrated assistance, with "agent" mode
- **Cursor**: AI-first development environment

### Getting Started Guides

New to these tools? Start here:
- **[Getting Started with Claude Code](getting-started-claude-code.md)** - Introduction for newcomers
- **[Getting Started with AWS Kiro](getting-started-aws-kiro.md)** - Introduction for newcomers

## Additional Tools Available 
We've open sourced some other tools that you can connect to these code assistants to help you work and to give some deeper compliance support for UK governement specific standards:

- **Example Government AI SDLC MCP Server**: [https://github.com/Version1/uk-gov-example-ai-sdlc](https://github.com/Version1/uk-gov-example-ai-sdlc)
- **Example Government Standards MCP Server**: [https://github.com/Version1/uk-gov-tech-standards-mcp](https://github.com/Version1/uk-gov-tech-standards-mcp)

Amazon Kiro is spec-driven by default, to use a spec-driven approach in the other tools, consider this open source framework that works with all major AICA:
- **Spec-Kit**: [Github Spec-Kit](https://github.com/github/spec-kit)

*This repository serves as both a workshop resource and a long-term reference for AI-assisted development in government contexts. We hope it provides lasting value for your teams and projects!*
