# ISMS-POL-A.8.28-S5.D
## Secure Coding - Quick Reference Guide

**Document ID**: ISMS-POL-A.8.28-S5.D
**Title**: Secure Coding - Quick Reference Guide  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead | Initial quick reference guide |

**Review Cycle**: Quarterly
**Next Review Date**: [Approval Date + 3 months] 
**Approvers**: 
- Primary: Application Security Lead

**Distribution**: All developers (onboarding material, print and post at workstations)
**Related Documents**: 
- ISMS-POL-A.8.28-S2.2 (Secure Coding Standards)
- ISMS-POL-A.8.28-S5.A (Language-Specific Guidelines)
- ISMS-POL-A.8.28-S5.B (Code Review Checklist)

---

## 1. Introduction

### 1.1 Purpose

> *"What I cannot create, I do not understand." - Richard Feynman*

This is your **one-page security cheat sheet** for daily development. Keep it visible (printed, pinned in IDE, second monitor).

**This guide is NOT comprehensive** - for detailed guidance, see:
- Language-specific patterns → **S5.A**
- Code review criteria → **S5.B**
- Vulnerability handling → **S5.C**
- Full policy → **S2.2**

### 1.2 When to Use

- **Daily coding**: Quick reminders of security basics
- **Pre-commit**: Self-review checklist
- **New projects**: Security considerations from day one
- **Stuck on security issue**: Quick reference before escalating

---

## 2. Secure Coding Top 10 Principles

### 2.1 The Essential Ten

**1. Validate All Input**
- Trust nothing: users, databases, APIs, files, environment variables
- Server-side validation always (client-side is UX, not security)
- Whitelist over blacklist ("allow only X" vs. "block if Y")

**2. Encode All Output**
- Context matters: HTML-encode, JavaScript-encode, URL-encode, SQL-parameterize
- Never trust data inserted into HTML, JavaScript, SQL, shell commands

**3. Parameterize Queries**
- Never concatenate strings to build SQL/NoSQL queries
- Use ORM or parameterized statements for all database access
- Even for "read-only" queries (information disclosure risk)

**4. Use Framework Security Features**
- Don't reinvent: authentication, session management, CSRF protection
- Use proven libraries (bcrypt, cryptography, DOMPurify)
- Keep frameworks updated

**5. Fail Securely**
- Default deny (whitelist approach)
- Never fail open (authentication fails → deny access, not grant)
- Generic error messages to users (log details server-side)

**6. Hash Passwords Properly**
- bcrypt (cost factor 12+) or Argon2
- Never MD5, SHA1, SHA256 alone (even with salt)
- Never store plaintext passwords (not even temporarily)

**7. No Hardcoded Secrets**
- Environment variables or secret manager only
- No API keys, passwords, tokens, private keys in code
- Scan for secrets before commit (use pre-commit hooks)

**8. Keep Dependencies Updated**
- Monitor SCA alerts daily
- Patch within SLA (Critical: 7 days, High: 30 days)
- Pin dependency versions (lock files)

**9. Review Your Code**
- Peer review mandatory (security checklist for high-risk changes)
- Read your own changes before submitting PR
- Think like an attacker

**10. Test for Security**
- Write security test cases (negative tests, boundary tests)
- Don't assume it works - verify
- Test authentication, authorization, input validation

---

## 3. Pre-Commit Checklist

**Run through this BEFORE submitting PR** (2 minutes):

- [ ] **No secrets in code**: Search for `password`, `api_key`, `token`, `secret`
  - *Tool*: `git diff | grep -iE "(password|api_key|secret|token)"`
  
- [ ] **Input validation present**: All user input validated server-side
  - *Check*: Forms, URL params, headers, API requests
  
- [ ] **Output encoding correct**: XSS prevention applied
  - *Check*: Template auto-escaping enabled, no `innerHTML` with user input
  
- [ ] **SQL queries parameterized**: No string concatenation in queries
  - *Check*: All `cursor.execute()`, `query()` use parameters
  
- [ ] **No vulnerable dependencies**: SCA scan green
  - *Tool*: `npm audit`, `pip-audit`, or CI/CD check
  
- [ ] **Code reviewed locally**: Read your own changes critically
  - *Ask*: "How could I exploit this?"
  
- [ ] **Tests passing**: Including security tests
  - *Check*: Unit tests, integration tests green
  
- [ ] **Commit message clear**: What changed and why
  - *Format*: "Fix SQL injection in user search [VULN-123]"

---

## 4. Security Tools Quick Reference

### 4.1 Developer Tools

| Tool | Purpose | How to Use | When |
|------|---------|------------|------|
| **SAST** | Find vulnerabilities in code | Runs automatically in CI/CD | Every commit |
| **SCA** | Find vulnerable dependencies | Runs automatically in CI/CD | Every build |
| **Secret Scanner** | Detect committed secrets | Pre-commit hook + CI/CD | Before commit |
| **Linter** | Enforce coding standards | IDE integration | While coding |
| **DAST** | Test running application | Security team runs | Pre-release |

### 4.2 Quick Commands
```bash
# Python - Scan for vulnerabilities
bandit -r . -f json -o bandit-report.json
pip-audit

# JavaScript/Node.js - Scan dependencies
npm audit
npm audit fix

# Search for secrets in code
git diff | grep -iE "(password|api_key|secret|token|private_key)"

# Check for hardcoded IPs
git diff | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"
```

---

## 5. Common Vulnerability Quick Fixes

### 5.1 SQL Injection

**Problem**: String concatenation in queries
```python
# ❌ WRONG
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)
```

**Solution**: Parameterized queries
```python
# ✅ CORRECT
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### 5.2 Cross-Site Scripting (XSS)

**Problem**: Unencoded user input in HTML
```javascript
// ❌ WRONG
element.innerHTML = userInput;
```

**Solution**: Use framework auto-escaping or textContent
```javascript
// ✅ CORRECT
element.textContent = userInput;  // Safe for text
// Or in React: <div>{userInput}</div>  (JSX auto-escapes)
```

### 5.3 Hardcoded Secrets

**Problem**: Credentials in code
```python
# ❌ WRONG
API_KEY = "sk_live_abc123456789"
DATABASE_PASSWORD = "MyP@ssw0rd"
```

**Solution**: Environment variables or secret manager
```python
# ✅ CORRECT
import os
API_KEY = os.environ.get("API_KEY")
# Or use secret manager (AWS Secrets Manager, Azure Key Vault, etc.)
```

### 5.4 Weak Password Hashing

**Problem**: MD5, SHA1, or plaintext
```python
# ❌ WRONG
import hashlib
hashed = hashlib.md5(password.encode()).hexdigest()
```

**Solution**: bcrypt or Argon2
```python
# ✅ CORRECT
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
```

### 5.5 Command Injection

**Problem**: Shell command with user input
```python
# ❌ WRONG
os.system(f"ls {user_directory}")
subprocess.run(f"tar -czf backup.tar {filename}", shell=True)
```

**Solution**: Use argument lists, no shell
```python
# ✅ CORRECT
subprocess.run(['ls', user_directory])
subprocess.run(['tar', '-czf', 'backup.tar', filename])
```

### 5.6 Path Traversal

**Problem**: Direct path concatenation
```python
# ❌ WRONG
filepath = f"/uploads/{user_filename}"
with open(filepath) as f:
    content = f.read()
```

**Solution**: Validate and resolve paths
```python
# ✅ CORRECT
from pathlib import Path
UPLOAD_DIR = Path('/uploads')
requested = (UPLOAD_DIR / user_filename).resolve()
if not requested.is_relative_to(UPLOAD_DIR):
    raise ValueError("Invalid path")
```

### 5.7 Insecure Random

**Problem**: Non-cryptographic random for security
```python
# ❌ WRONG
import random
token = str(random.randint(100000, 999999))
```

**Solution**: Cryptographically secure random
```python
# ✅ CORRECT
import secrets
token = secrets.token_urlsafe(32)  # 256 bits
```

---

## 6. When to Escalate

### 6.1 Escalation Paths

**Escalate to Security Champion** when:
- Unsure if code is secure
- Need security design advice
- SAST finding unclear (false positive?)
- Security testing question
- Need help with S5.B checklist item

**Escalate to Application Security Team** when:
- Discovered vulnerability in production
- Complex security architecture question
- Need threat modeling session
- Exception request (can't meet policy requirement)

**Emergency Escalation to CISO** when:
- Active exploitation of vulnerability detected
- Data breach suspected
- Critical vulnerability in production
- Regulatory reporting required

### 6.2 Contact Information

**Security Champion**: [Team-specific Security Champion name/email]
**Application Security Team**: security@organization.com
**Emergency Security Hotline**: [Phone number] (24/7 for Critical issues)
**Vulnerability Reporting**: vulnerabilities@organization.com

---

## 7. Key Policy References

### 7.1 Frequently-Needed Sections

**Core Standards**:
- Secure Coding Standards: **ISMS-POL-A.8.28-S2.2**
- Input Validation: S2.2 Section 2.2.3
- Output Encoding: S2.2 Section 2.2.4
- Cryptography: S2.2 Section 2.2.7

**Practical Guidance**:
- Language-Specific Guides: **ISMS-POL-A.8.28-S5.A**
- Code Review Checklist: **ISMS-POL-A.8.28-S5.B**
- Vulnerability Response: **ISMS-POL-A.8.28-S5.C**

**Process**:
- Code Review Requirements: **ISMS-POL-A.8.28-S2.3**
- Dependency Management: **ISMS-POL-A.8.28-S2.4**

### 7.2 External Resources

**OWASP Resources**:
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- ASVS: https://owasp.org/www-project-application-security-verification-standard/

**Other Standards**:
- CWE Top 25: https://cwe.mitre.org/top25/
- SANS Top 25: https://www.sans.org/top25-software-errors/
- SEI CERT: https://wiki.sei.cmu.edu/confluence/

**Training**:
- Internal Training Portal: [Link to internal training]
- OWASP WebGoat: https://owasp.org/www-project-webgoat/
- PortSwigger Academy: https://portswigger.net/web-security

---

## 8. Secure Development Workflow

### 8.1 Visual Workflow
```
┌─────────────────────────────────────────────────────────────────────┐
│ 1. DESIGN                                                           │
│    → Identify security requirements                                 │
│    → Threat model (if high-risk: payment, auth, admin)             │
│    → Choose secure frameworks and libraries                         │
│    → Reference: S2.1 (Pre-Development Requirements)                 │
└────────────────────────────┬────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 2. CODE                                                             │
│    → Follow secure coding standards (S2.2, S5.A)                    │
│    → Use security linters/IDE plugins                               │
│    → Apply Top 10 Principles (Section 2.1)                          │
│    → Run tests locally (unit, integration)                          │
└────────────────────────────┬────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 3. SELF-REVIEW                                                      │
│    → Pre-commit checklist (Section 3)                               │
│    → Secret scan (no hardcoded credentials)                         │
│    → Read your own changes critically                               │
│    → Think: "How could I exploit this?"                             │
└────────────────────────────┬────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 4. COMMIT                                                           │
│    → Pre-commit hooks pass (secrets, formatting)                    │
│    → Clear commit message (what + why)                              │
│    → Reference ticket/issue if applicable                           │
└────────────────────────────┬────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 5. PULL REQUEST                                                     │
│    → Automated checks pass (SAST, SCA, tests, linters)             │
│    → Peer code review (use S5.B checklist for security)            │
│    → Security Champion review (if high-risk)                        │
│    → Address all feedback                                           │
└────────────────────────────┬────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 6. MERGE & DEPLOY                                                   │
│    → All approvals obtained                                         │
│    → CI/CD security gates pass                                      │
│    → Deploy to staging → production                                 │
│    → Monitor for issues post-deployment                             │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2 Risk-Based Approach

**High-Risk Changes** (require extra scrutiny):
- Authentication/authorization
- Payment processing
- Cryptography
- Admin functionality
- Public-facing APIs

**Security Champions Required**: High-risk changes reviewed by Security Champion

**Standard Changes**: Peer review with security awareness

---

## 9. Security Mindset

### 9.1 Think Like an Attacker

**Questions to Ask**:
- What's the worst that could happen if this input is malicious?
- Can I bypass this check?
- What if I send 10,000 requests per second?
- What if this external service is compromised?
- What if I change this ID to access someone else's data?

### 9.2 Defense in Depth

**Multiple Layers**:
1. **Input Validation**: Reject bad input at the door
2. **Output Encoding**: Encode even if input was validated
3. **Least Privilege**: Run with minimum permissions
4. **Monitoring**: Detect if layers 1-3 fail
5. **Incident Response**: Respond quickly when breach occurs

**Don't rely on one layer**: Assume every layer can fail.

### 9.3 Shift Left

**Find vulnerabilities early** (cheaper to fix):
- Design phase: Threat modeling (Critical/High-risk features)
- Code phase: Secure coding, linters, SAST
- Review phase: Security-focused peer review
- Test phase: Security testing, DAST
- Production: Monitoring, vulnerability scanning

**Cost to fix increases 10x-100x at each stage** - catch early!

---

## 10. Remember

### 10.1 Key Takeaways

**1. Security is Everyone's Job**
Not just the Security Team's responsibility - every developer writes secure code.

**2. Shift Left**
Catch vulnerabilities early (design/code) - cheapest to fix, easiest to prevent.

**3. When in Doubt, Ask**
Security Champions and Application Security Team are here to help - no question is too small.

**4. Learn from Mistakes**
Every vulnerability is a learning opportunity - read post-mortems, improve processes.

### 10.2 Cargo Cult Warning

> *"The first principle is that you must not fool yourself—and you are the easiest person to fool." - Richard Feynman*

**Don't do security theater**:
- ❌ Validation client-side only (attacker bypasses browser)
- ❌ Security through obscurity (hiding API endpoints, hoping nobody finds them)
- ❌ "Nobody will attack us" mindset (they will, and they do)
- ❌ Copy-paste security code without understanding it

**Do real security**:
- ✅ Understand WHY something is secure (not just that it is)
- ✅ Server-side validation always
- ✅ Assume attackers are sophisticated
- ✅ Test security controls (don't just trust they work)

### 10.3 Growth Mindset

**Security skills develop over time**:
- Everyone makes security mistakes (even experts)
- Learn from code reviews and vulnerabilities
- Ask questions - there are no stupid questions
- Read post-mortems and security advisories
- Contribute improvements to this guide

**We're all learning together.**

---

## 11. Quick Security Checklist (Printable)

**Print and post at workstation:**
```
┌─────────────────────────────────────────────────────────────────┐
│                   SECURE CODING QUICK CHECKLIST                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BEFORE EVERY COMMIT:                                           │
│  ☐ No secrets in code (API keys, passwords)                    │
│  ☐ Input validated server-side                                 │
│  ☐ Output encoded (XSS prevention)                             │
│  ☐ SQL queries parameterized                                   │
│  ☐ Dependencies not vulnerable (SCA green)                     │
│                                                                 │
│  SECURITY TOP 10:                                               │
│  1. Validate all input                                          │
│  2. Encode all output                                           │
│  3. Parameterize queries                                        │
│  4. Use framework security features                             │
│  5. Fail securely                                               │
│  6. Hash passwords (bcrypt/Argon2)                              │
│  7. No hardcoded secrets                                        │
│  8. Keep dependencies updated                                   │
│  9. Review your code                                            │
│  10. Test for security                                          │
│                                                                 │
│  WHEN TO ESCALATE:                                              │
│  → Unsure → Security Champion                                   │
│  → Vulnerability found → Application Security Team              │
│  → Active exploit → CISO (emergency)                            │
│                                                                 │
│  RESOURCES:                                                     │
│  Policy: ISMS-POL-A.8.28-S2.2 (Standards)                       │
│  Guides: ISMS-POL-A.8.28-S5.A (Languages)                       │
│  Checklist: ISMS-POL-A.8.28-S5.B (Code Review)                  │
│  OWASP: https://owasp.org/www-project-top-ten/                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 12. Document History

| Date | Version | Change Summary | Author |
|------|---------|----------------|--------|
| [Approval Date] | 1.0 | Initial quick reference guide | Application Security Lead |

---

**END OF DOCUMENT**

**Remember**: This is a REFERENCE, not a replacement for thinking. Security requires understanding, not just following checklists.

*"The test of all knowledge is experiment. Experiment is the sole judge of scientific truth." - Feynman*

**Test your security assumptions. Don't just trust—verify.**