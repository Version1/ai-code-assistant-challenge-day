# Claude Code Playbook: Security Vulnerability Assessment and Remediation

Your starter kit for fixing security vulnerabilities in a Flask application. For Claude Code basics, see [Getting Started](../getting-started-claude-code.md).

---

## Challenge-specific CLAUDE.md

Copy this into your project's CLAUDE.md before you start.

```markdown
## Project: Security Vulnerability Remediation

Fixing OWASP Top 10 vulnerabilities in a Flask application without breaking functionality.

### OWASP priority order for this application
Fix in this order (highest impact to citizen data first):
1. SQL Injection - direct database compromise risk
2. Broken Authentication - session/access control bypass
3. Cross-Site Scripting (XSS) - stored and reflected
4. Unrestricted File Upload - remote code execution risk
5. Missing Security Headers - clickjacking, MIME sniffing

### Flask secure coding patterns

**SQL Injection prevention:**
```python
# WRONG - string concatenation
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# RIGHT - parameterised queries
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

**XSS prevention:**
- Jinja2 auto-escapes in {{ }} by default - do not disable with |safe
- For user content in JavaScript, use json.dumps() with proper escaping
- Validate and sanitise on input, escape on output

**Authentication decorator pattern:**
```python
from functools import wraps
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated
```

**File upload security:**
- Whitelist allowed extensions (not blacklist)
- Generate new filenames (do not trust user input)
- Store outside web root or use secure serving
- Check file content, not just extension

**Security headers (add to all responses):**
```python
@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```

### Functional preservation requirements
After every fix, verify:
- Login still works with test accounts (admin/admin123, user1/password)
- Protected pages redirect unauthenticated users to login
- Search returns correct results
- File upload accepts valid files
- Profile displays correctly

### Testing commands
```bash
# Run application
python app.py

# Test login (should succeed)
curl -X POST http://localhost:5001/login -d "username=admin&password=admin123"

# Test SQL injection (should fail after fix)
curl -X POST http://localhost:5001/login -d "username=admin'--&password=anything"

# Test XSS (should be escaped after fix)
curl "http://localhost:5001/search?q=<script>alert(1)</script>"
```
```

---

## Custom slash commands

Save these files in `.claude/commands/`.

### `.claude/commands/security-audit.md`

```markdown
---
description: OWASP-based security audit of Flask application
---

Conduct a systematic security audit of this Flask application.

**For each OWASP Top 10 category, check:**

1. **Injection (A03:2021):** Find all database queries. Are they parameterised? Check cursor.execute(), raw SQL, ORM queries.

2. **Broken Authentication (A07:2021):** Map all routes. Which need authentication? Is session handling secure? Check for missing @login_required decorators.

3. **XSS (A03:2021):** Find all user input rendering. Is Jinja2 auto-escape disabled anywhere? Check for |safe filter misuse.

4. **Security Misconfiguration (A05:2021):** Check for debug mode, default secrets, missing security headers, verbose error messages.

5. **Unrestricted File Upload (A04:2021):** Find file upload handlers. What validation exists? Where are files stored?

**Report format for each finding:**
- Location: file and line number
- Vulnerability type: OWASP category
- Severity: Critical/High/Medium/Low
- Current code: what is vulnerable
- Fix approach: how to remediate
- Test case: how to verify the fix
```

### `.claude/commands/verify-remediation.md`

```markdown
---
description: Verify security fixes and functional preservation
---

Verify that security fixes are complete and functionality is preserved.

**Security verification:**
For each vulnerability that was fixed:
1. Attempt the original exploit - it should fail
2. Check the fix follows secure coding patterns from CLAUDE.md
3. Verify no new vulnerabilities were introduced

**Functional verification:**
Test these user journeys still work:
1. Login with valid credentials (admin/admin123)
2. Access protected pages when authenticated
3. Redirect to login when not authenticated
4. Search returns expected results
5. File upload accepts valid files, rejects invalid
6. Profile displays user information correctly

**Regression checks:**
- No Python syntax errors (python -m py_compile app.py)
- Application starts without errors
- No broken imports or missing dependencies

**Report:**
- Security tests: PASS/FAIL with evidence
- Functional tests: PASS/FAIL with evidence
- Overall status: Ready for deployment / Needs attention
```

---

## Model recommendations

| Task | Model | Why |
|------|-------|-----|
| Authentication architecture redesign | Opus | Security-critical decisions need careful reasoning |
| Complex vulnerability analysis | Opus | Understanding attack vectors requires deep context |
| SQL injection fixes | Sonnet | Pattern-based replacement once approach is clear |
| XSS fixes in templates | Sonnet | Straightforward escaping patterns |
| Security header implementation | Sonnet | Standard Flask patterns |
| Verifying fix completeness | Opus | Finding gaps in security coverage |

**Switch with `/model`** - use Opus for architecture and security analysis, Sonnet for pattern-based fixes.

---

## Effective prompts for this challenge

**Systematic vulnerability triage:**
> "Analyse the OWASP ZAP scan results and the application code. For each vulnerability: explain what the attacker could do, identify the exact code location, and rate severity based on citizen data impact. Prioritise fixes by: 1) direct data compromise risk, 2) authentication bypass, 3) session hijacking, 4) information disclosure. Give me a remediation order."

**SQL injection remediation with context:**
> "Fix the SQL injection vulnerability in the login function. The current code uses string concatenation. Convert to parameterised queries using SQLite's ? placeholder syntax. Preserve the existing login logic - users must still be able to log in with correct credentials. Show me the fix, then show me how to test that injection no longer works but valid login still does."

**Authentication architecture:**
> "Review all routes in app.py and identify which should require authentication. Create a login_required decorator that checks session state. Apply it to protected routes. Handle the redirect flow: unauthenticated users go to login, then return to their original destination after successful login. Do not break existing functionality for public pages."

**Comprehensive file upload security:**
> "Secure the file upload endpoint against: arbitrary file type upload, path traversal attacks, oversized files, and malicious filenames. Implement: extension whitelist (images only), content-type verification, size limits, secure filename generation, and storage outside web root. Keep the upload feature working for legitimate image files."

**Security headers and hardening:**
> "Add security headers to all responses using Flask's after_request hook. Include: X-Frame-Options (DENY), X-Content-Type-Options (nosniff), Content-Security-Policy (restrict to self), and X-XSS-Protection. Also: ensure debug mode is off, generate a secure secret key, and remove any sensitive information from error messages."

---

## Tips and gotchas

### AI may over-sanitise

| Issue | What to do |
|-------|------------|
| Breaks legitimate queries | Test with real data after each fix, not just attack payloads |
| Escapes content that should render | Check if |safe was intentionally used for trusted content |
| Rejects valid file uploads | Test with actual files users would upload |

### Template changes need template context

| Issue | What to do |
|-------|------------|
| XSS fix breaks page rendering | Check what variables the template expects |
| Missing template variables | Ensure route still passes all required context |
| JavaScript in templates | User data in JS needs json.dumps(), not just Jinja escaping |

### Session and auth changes can lock you out

| Issue | What to do |
|-------|------------|
| Cannot log in after changes | Keep a browser session open while testing |
| Session key changes | Clear browser cookies and test fresh |
| Decorator breaks routes | Test each protected route individually |

### Secret key generation pitfalls

| Issue | What to do |
|-------|------------|
| Hardcoded secret in code | Use environment variable or secrets file |
| Weak secret generation | Use secrets.token_hex(32) not random strings |
| Secret in version control | Add to .gitignore, use .env file |

### False sense of security

| Issue | What to do |
|-------|------------|
| "Fixed SQL injection" but missed one query | Search entire codebase for all execute() calls |
| Headers added but CSP too permissive | Test headers with browser dev tools |
| Auth decorator exists but not applied | Verify every sensitive route is decorated |

---

## Reflection questions

After completing the challenge, consider:

- How did you verify that security fixes did not break legitimate functionality?
- What was your strategy for finding all instances of a vulnerability type, not just the obvious ones?
- How would you explain the fixes to a non-technical stakeholder who needs to approve deployment?
- Where did AI help most - understanding vulnerabilities, writing fixes, or verifying completeness?
- What would you add to CLAUDE.md to help the next person maintaining this application?
