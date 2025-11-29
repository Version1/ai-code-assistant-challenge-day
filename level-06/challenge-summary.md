# Level 6: Security Vulnerability Assessment and Remediation

## What this challenge is about

Government services handle sensitive citizen data. Security vulnerabilities put that data at risk. This challenge tests whether AI tools can help you fix security problems faster and more systematically than manual approaches.

You will take real security scan results, use AI tools to understand and prioritise the vulnerabilities, then fix them without breaking the application.

## Why this matters for government

The National Cyber Security Centre's 2023 Annual Report found that government organisations face sophisticated cyber threats, but manual security review creates "critical gaps between vulnerability identification and remediation deployment."

**Current problems with security vulnerability management:**

- Security specialists are scarce - they become bottlenecks
- Manual code review cannot scale to catch all vulnerability types
- Teams interpret and prioritise vulnerabilities inconsistently
- Fixes sometimes introduce new vulnerabilities
- No systematic way to learn from vulnerability patterns

**The specific problem you will address:**

Government departments use specialist security tools like OWASP ZAProxy, but struggle to convert scan results into actual fixes. AI tools can bridge this gap.

## What you need to do

1. Take the OWASP ZAProxy scan results for a vulnerable Flask application
2. Use AI tools to analyse and prioritise the vulnerabilities
3. Fix all identified security issues
4. Keep the application working exactly as before
5. Document your approach so others can repeat it

## How success will be measured

### Core requirements

| Requirement | What this means |
|-------------|-----------------|
| Fix all vulnerabilities | Every issue from the security scan must be addressed |
| Keep functionality working | Users can still do everything they could before |
| Prevent similar issues | Your fixes should stop the same vulnerability types recurring |
| Maintain code quality | Fixes should be clean and fit the existing code style |
| Test thoroughly | Prove fixes work and nothing else broke |
| Document clearly | Others should be able to follow your approach |

### Government-specific requirements

| Requirement | What this means |
|-------------|-----------------|
| Prioritise by risk | Fix the most dangerous vulnerabilities first, based on citizen data impact |
| Create audit trails | Document everything for security oversight |
| Align with standards | Fixes should meet government security requirements |
| Make it reusable | Your approach should work for other government services |

## The vulnerable application

**Location:** `security-challenge/`

This is a deliberately vulnerable Flask application. It represents common security issues found in departmental digital services.

### Known vulnerabilities

| Vulnerability | Description |
|---------------|-------------|
| SQL Injection | Login forms use string concatenation instead of parameterised queries |
| Cross-Site Scripting (XSS) | Search functionality does not escape user input |
| Missing Authentication | Some protected pages can be accessed directly via URL |
| Unrestricted File Upload | No validation of file type or size |
| Missing Security Headers | No X-Frame-Options, Content Security Policy, or HSTS |
| Session Management Issues | Weak session handling |

### Application files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with vulnerable endpoints |
| `templates/` | HTML templates for login, profile, search, upload |
| `vulnerable_app.db` | SQLite database with test accounts |
| `README.md` | Application overview |

### Running the application

```bash
cd security-challenge/
pip install flask
python app.py
```

Open http://localhost:5001 in your browser.

**Test accounts:** admin/admin123, user1/password, test/test

## Approaches to consider

### Prompt-driven development

Use AI tools to interpret security scan results and generate fixes that address root causes.

**Best for:** Time-sensitive remediation, teams with limited security expertise.

### Spec-driven development

Create structured specifications for each vulnerability fix, with defined phases and acceptance criteria.

**Best for:** Formal compliance requirements, systematic improvement across multiple applications.

### Hybrid approach

Use prompt-driven for rapid analysis and initial fixes, then spec-driven for formal validation and compliance documentation.

## What to do next

Choose your approach and start with the security scan results. The implementation guidance for your chosen approach will walk you through the detailed steps.
