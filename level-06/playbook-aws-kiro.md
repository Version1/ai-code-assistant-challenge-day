# Kiro Playbook: Security Vulnerability Assessment and Remediation

This playbook assumes you have read the [challenge summary](challenge-summary.md) and [Kiro setup guide](../getting-started-aws-kiro.md). What follows is your starter kit for fixing security vulnerabilities in a Flask application.

## Mode recommendation: Spec Mode

Use Spec Mode for this challenge. Here is why:

- Security remediations need traceable documentation - auditors will ask why each fix was applied
- Acceptance criteria prove vulnerabilities are actually fixed, not just modified
- Each fix must not introduce new vulnerabilities - specs force you to consider side effects
- Government compliance requires audit trails from vulnerability scan to deployed fix
- CWE identifiers need explicit mapping to code changes

Vibe Mode works for understanding individual vulnerabilities. Switch to Spec Mode when implementing fixes.

## Steering files for this challenge

Copy these into your `.kiro/steering/` directory.

### product.md

```markdown
# Product Context

## What this system does
Flask web application handling citizen data. Currently contains security
vulnerabilities identified by OWASP ZAProxy scanning.

## Security hardening context
This application processes sensitive information. Security is not optional -
it is a legal and ethical requirement. Every vulnerability is a potential
breach affecting citizens.

## Compliance requirements
Fixes must reference CWE identifiers where applicable:
- CWE-89: SQL Injection
- CWE-79: Cross-Site Scripting
- CWE-306: Missing Authentication
- CWE-434: Unrestricted File Upload
- CWE-693: Protection Mechanism Failure

All remediation work must produce audit-ready documentation.

## Stakeholders
- **Security oversight**: need evidence that vulnerabilities are addressed
- **Users**: need continued access to all existing functionality
- **Audit team**: need traceability from scan findings to code changes
- **Operations**: need deployment-ready fixes without breaking changes
```

### tech.md

```markdown
# Technical Standards

## Flask security patterns

### SQL injection prevention
- Use parameterised queries exclusively
- Never concatenate user input into SQL strings
- Prefer ORM methods over raw SQL where possible

### XSS prevention
- Enable Jinja2 auto-escaping globally
- Use `| safe` filter only when content is verified safe
- Validate and sanitise all user input server-side

### Authentication and session security
- Use Flask-Login or equivalent for session management
- Set secure session cookies (HttpOnly, Secure, SameSite)
- Implement proper logout that invalidates server-side session
- Hash passwords with bcrypt or argon2 (never MD5 or SHA1 alone)

### File upload security
- Validate file extensions against allowlist
- Check MIME types server-side
- Limit file size
- Store uploads outside webroot with generated filenames

### Security headers (mandatory)
- Content-Security-Policy
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- Strict-Transport-Security (for production)
- Referrer-Policy: strict-origin-when-cross-origin

## Testing requirements
- Prove each vulnerability is fixed with targeted tests
- Verify application functionality remains intact
- Test edge cases that could bypass security controls

## Mandatory security libraries
- Flask-Talisman for security headers
- Werkzeug secure functions for file handling
- Parameterised database queries (sqlite3 ? placeholders)
```

## Agent for this challenge

Save this in `.kiro/agents/security-remediator.md`.

```markdown
# Security Remediator Agent

You are a security specialist who fixes vulnerabilities without breaking functionality.

## Your expertise
- OWASP Top 10 vulnerability patterns
- Flask security best practices
- Defence in depth - multiple layers of protection
- Secure coding patterns that prevent entire classes of vulnerability

## When analysing vulnerabilities
- Identify the root cause, not just the symptom
- Check for the same vulnerability pattern elsewhere in the codebase
- Consider how an attacker would exploit this

## When implementing fixes
- Fix the root cause, not just the specific instance
- Verify the fix does not introduce new vulnerabilities
- Test that existing functionality still works
- Document what was changed and why

## Red flags to catch
- Fixes that only address one instance of a pattern
- New code that reintroduces fixed vulnerability types
- Over-restrictive fixes that break legitimate functionality
```

## Hook for this challenge

Save this in `.kiro/hooks/security-review.yaml`.

```yaml
name: security-review
event: file_saved
match: "**/*.py"
prompt: |
  Check this Python file for security vulnerabilities:
  - SQL queries using string formatting or concatenation
  - Unescaped user input in templates or responses
  - Missing authentication checks on sensitive endpoints
  - File operations without path validation
  - Hardcoded secrets or credentials
  - Missing input validation or sanitisation
  Report specific line numbers and recommended fixes.
```

## Effective spec prompts

Use these prompts to guide Kiro through your security remediation.

### Initial security assessment spec

> Create requirements for a security assessment of this Flask application. Cover: how to systematically identify all vulnerabilities matching the ZAProxy findings; how to prioritise by risk to citizen data; what acceptance criteria prove each vulnerability is fixed. Reference relevant CWE identifiers.

### SQL injection remediation task

> Design the SQL injection remediation. Cover: every database query in the application; conversion to parameterised queries; edge cases where user input reaches SQL; verification that fixes do not break search or login functionality. Show before and after patterns.

### Security headers implementation

> Create requirements for implementing security headers. Cover: which headers to add and why; Content-Security-Policy that allows the application to function; testing approach to verify headers are present; documentation of header purposes for the audit trail.

### Session hardening with audit trail

> Design session security improvements. Cover: secure cookie settings; password hashing upgrade path; session invalidation on logout; what to log for security audit purposes. Include acceptance criteria that auditors can verify.

## Gotchas specific to security remediation

| Problem | Why it happens | Prevention |
|---------|----------------|------------|
| Fix introduces new vulnerability | Escaping for one context creates risk in another | Test fixes against multiple attack vectors; review for unintended side effects |
| Over-escaping breaks functionality | Applying HTML escaping to data that should allow formatting | Understand what each escaping function does; test with legitimate content |
| CSP too restrictive | Content-Security-Policy blocks inline scripts the app needs | Audit existing functionality before setting CSP; use nonces for legitimate inline scripts |
| Password hashing breaks existing accounts | Changing hash algorithm invalidates stored passwords | Implement migration strategy: verify old hash, upgrade to new hash on successful login |
| Auth bypass still possible | Fixed the obvious route but missed alternative paths | Map all routes to endpoints; test each endpoint directly, not just through UI |

## Quality checkpoints

### Pre-remediation baseline

- [ ] All vulnerabilities from scan documented with severity
- [ ] Application functionality tested and baseline established
- [ ] Each vulnerability mapped to specific code locations
- [ ] Remediation priority determined by citizen data risk

### Per-vulnerability verification

- [ ] Vulnerability root cause identified and documented
- [ ] Fix addresses root cause, not just symptom
- [ ] Same vulnerability pattern checked across entire codebase
- [ ] Fix tested with attack payloads that previously worked
- [ ] Application functionality verified still working

### Integration validation

- [ ] All fixes work together without conflicts
- [ ] No new vulnerabilities introduced by fixes
- [ ] Performance not significantly degraded
- [ ] User workflows complete successfully

### Audit readiness

- [ ] Each fix linked to original vulnerability finding
- [ ] CWE identifiers referenced where applicable
- [ ] Before and after code documented
- [ ] Test evidence showing vulnerability is resolved
- [ ] Rationale documented for any accepted risks

## Reflection questions

When you finish, consider:

- Did fixing one vulnerability reveal others you had not spotted?
- Could someone follow your documentation to verify each fix works?
- Which vulnerabilities would have been prevented by better original design?
- If a new developer joins tomorrow, would they understand the security decisions?
- How would you prevent these vulnerability types in future projects?
