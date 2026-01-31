# ISMS-POL-A.8.28-S5.B
## Secure Coding - Code Review Checklist Template

**Document ID**: ISMS-POL-A.8.28-S5.B
**Title**: Secure Coding - Code Review Checklist Template  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead | Initial code review checklist template |

**Review Cycle**: Quarterly (or when OWASP Top 10 updated)
**Next Review Date**: [Approval Date + 3 months] 
**Approvers**: 
- Primary: Application Security Lead
- Consulted: Security Champions

**Distribution**: Code reviewers, Security Champions, all developers
**Related Documents**: 
- ISMS-POL-A.8.28-S2.2 (Secure Coding Standards)
- ISMS-POL-A.8.28-S2.3 (Code Review & Testing Requirements)
- ISMS-POL-A.8.28-S5.A (Language-Specific Guidelines)
- ISMS-POL-A.8.28-S5.D (Quick Reference Guide)

---

## 1. Introduction

### 1.1 Purpose

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool." - Richard Feynman*

This checklist provides **actionable security criteria** for code reviewers. It operationalizes the code review requirements from ISMS-POL-A.8.28-S2.3, translating policy into practical review steps.

**Goal**: Enable code reviewers to identify security issues systematically without requiring deep security expertise for every review.

### 1.2 How to Use This Checklist

**Not Every Item for Every Review**:
- **High-risk changes**: Use full checklist (authentication, cryptography, payments)
- **Medium-risk changes**: Focus on relevant sections (API endpoints: input validation + authorization)
- **Low-risk changes**: Minimal security review (refactoring, documentation)

**Integration Points**:
- **Pull Request Templates**: Include relevant checklist items
- **Review Tools**: Link checklist items in review comments
- **Training**: Use checklist in code review training workshops

**Risk-Based Approach**: See Section 4 for guidance on which items apply to which risk levels.

### 1.3 When to Escalate

**Escalate to Security Champion**:
- Checklist item unclear or ambiguous
- Security concern beyond your expertise
- Multiple checklist items failed

**Escalate to Application Security Team**:
- Suspected vulnerability requiring expert validation
- Architecture-level security concern
- Need for threat modeling session

---

## 2. Pre-Review Checklist

**Complete BEFORE reviewing code** (saves time, ensures quality):

- [ ] **Automated checks passed**: SAST, SCA, unit tests, linters all green?
  - *If not*: Review automated findings first, ensure they're addressed
  
- [ ] **Change description clear**: PR description explains WHAT changed and WHY?
  - *Check for*: Vague descriptions ("fixed bug"), missing context
  - *Action*: Request clarification if unclear

- [ ] **Risk level identified**: Does PR indicate risk level (Critical/High/Medium/Low)?
  - *If not identified*: Assess risk per Section 4 criteria
  
- [ ] **Security-relevant changes flagged**: Does PR author identify security implications?
  - *Check for*: Authentication, authorization, input handling, cryptography, data access
  - *Action*: If security-relevant but not flagged, apply appropriate checklist sections

- [ ] **Change scope reasonable**: Is PR focused (not changing 50 files unrelated changes)?
  - *If too large*: Request split into smaller, reviewable PRs
  
- [ ] **Tests included**: Are security-relevant changes covered by tests?
  - *Check for*: Input validation tests, authorization tests, negative test cases
  - *Reference*: ISMS-POL-A.8.28-S2.3 Section 2.3.2

---

## 3. Core Security Review Checklist

### 3.1 Authentication & Session Management

- [ ] **Authentication checks present**: All protected endpoints verify user authentication
  - *Check for*: Missing authentication on API endpoints, admin pages, data access
  - *Test*: Can endpoint be accessed without authentication?
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.5.3

- [ ] **Session tokens secure**: Tokens are random, unpredictable, with HttpOnly/Secure flags
  - *Check for*: Predictable session IDs, sequential tokens, tokens in URLs
  - *Verify*: Cookie attributes include `HttpOnly`, `Secure`, `SameSite=Strict/Lax`
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.5.3

- [ ] **Password handling secure**: Passwords hashed with bcrypt/Argon2, never logged
  - *Check for*: Plaintext passwords, weak hashing (MD5, SHA1, SHA256 without salt)
  - *Verify*: No passwords in logs, error messages, or debug output
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.5.1
  - *Example*: See S5.A Python Section 2.4 for correct hashing

- [ ] **Multi-factor authentication (MFA) enforced**: MFA required for privileged accounts
  - *Check for*: Admin accounts, financial operations bypassing MFA
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.5.4

- [ ] **Session timeout appropriate**: Sessions expire after inactivity period
  - *Check for*: No timeout, excessively long timeout (>30 min for high-risk apps)
  - *Verify*: Timeout documented and tested

- [ ] **Logout functionality secure**: Logout invalidates session on server-side
  - *Check for*: Client-side only logout, session still valid after logout
  - *Test*: Session token rejected after logout

### 3.2 Input Validation

- [ ] **All input validated**: Server-side validation present for ALL user input
  - *Check for*: Client-side only validation, missing validation on API endpoints
  - *Sources*: Forms, URL parameters, headers, cookies, file uploads, API requests
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.3

- [ ] **Whitelist approach used**: Validation uses allowlist (not blocklist)
  - *Check for*: Blacklist patterns ("reject if contains X"), incomplete blocklists
  - *Correct*: "Accept only if matches Y" (e.g., alphanumeric only)
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.3.1

- [ ] **SQL injection prevented**: Parameterized queries used, no string concatenation
  - *Check for*: String concatenation in SQL (f-strings, +, .format()), dynamic query building
  - *Verify*: All database queries use parameterized statements or ORM safely
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.3.2.A
  - *Example*: See S5.A Python Section 2.2, SQL Section 4.1

- [ ] **Command injection prevented**: No direct shell calls with user input
  - *Check for*: `os.system()`, `subprocess` with `shell=True`, `eval()`, `exec()`
  - *Verify*: Commands use argument lists, not string concatenation
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.3.2.B
  - *Example*: See S5.A Python Section 2.2

- [ ] **Path traversal prevented**: File paths validated, no directory traversal
  - *Check for*: Direct concatenation of user input to file paths
  - *Verify*: Paths resolved and validated within allowed directory
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.3.2.C
  - *Example*: See S5.A Python Section 2.2

- [ ] **XML external entity (XXE) prevented**: XML parsing disables external entities
  - *Check for*: Default XML parser configuration (often vulnerable)
  - *Verify*: External entities explicitly disabled in parser configuration
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.3.2.D

- [ ] **File upload validation**: Type, size, content validation present
  - *Check for*: Extension-only validation, no content validation, no size limits
  - *Verify*: Magic number validation, malware scanning, size limits enforced
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.3.3

- [ ] **Input length limits**: Maximum length enforced (prevent buffer overflow, DoS)
  - *Check for*: Unlimited input length, excessively large limits
  - *Verify*: Limits appropriate for data type and use case

### 3.3 Output Encoding & XSS Prevention

- [ ] **XSS prevention**: Output encoded for context (HTML, JavaScript, URL, CSS)
  - *Check for*: Unencoded user input in HTML, `innerHTML`, `dangerouslySetInnerHTML`
  - *Verify*: Framework auto-escaping used or manual encoding applied
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.4.1
  - *Example*: See S5.A JavaScript Section 3.2

- [ ] **Content Security Policy (CSP) headers**: CSP configured to mitigate XSS impact
  - *Check for*: Missing CSP headers, overly permissive CSP (`unsafe-inline`, `unsafe-eval`)
  - *Verify*: CSP restricts script sources, disables inline scripts where possible
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.4.1.B

- [ ] **CSRF protection**: Tokens present for state-changing operations
  - *Check for*: Missing CSRF tokens on POST/PUT/DELETE/PATCH
  - *Verify*: Tokens validated on server-side, tokens unpredictable
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.4.2
  - *Example*: See S5.A JavaScript Section 3.5

- [ ] **HTTP security headers**: Security headers configured properly
  - *Check for*: Missing `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`
  - *Verify*: Headers present and correctly configured
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.4.3

### 3.4 Authorization & Access Control

- [ ] **Authorization enforced server-side**: All access control checks on server
  - *Check for*: Client-side only authorization (hidden UI elements), missing server checks
  - *Verify*: Every protected resource has server-side authorization check
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.6.1

- [ ] **IDOR prevention**: User ownership verified before resource access
  - *Check for*: Direct ID access without ownership check (e.g., `/api/orders/123` accessible by any user)
  - *Test*: Can user access another user's resources by changing ID?
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.6.1.B

- [ ] **Least privilege principle**: Operations use minimum necessary permissions
  - *Check for*: Overly permissive roles, admin-level operations for user tasks
  - *Verify*: Database connections use limited privileges, not root/admin
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.6.2

- [ ] **Role-based access control (RBAC)**: Roles correctly assigned and checked
  - *Check for*: Hardcoded user IDs instead of roles, missing role checks
  - *Verify*: Role assignment follows principle of least privilege

- [ ] **Privilege escalation prevented**: No way to elevate privileges improperly
  - *Check for*: User-controllable role assignments, missing authorization on privilege changes
  - *Test*: Can user grant themselves admin role?

### 3.5 Cryptography

- [ ] **Approved algorithms only**: AES-256-GCM, RSA-2048+, ECDSA-256+, SHA-256+
  - *Check for*: DES, 3DES, RC4, MD5, SHA1, RSA-1024, ECB mode, custom crypto
  - *Verify*: Algorithms from approved list (S2.2 Section 2.2.7.1)
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.7.1

- [ ] **No hardcoded secrets**: Credentials from environment variables or secret manager
  - *Check for*: API keys, passwords, tokens, private keys in code
  - *Tools*: Use secret scanning tool (Gitleaks, TruffleHog, GitHub Secret Scanning)
  - *Reference*: ISMS-POL-A.8.28-S2.1 Section 2.1.6.2.C
  - *Action*: If found, rotate credentials immediately

- [ ] **Secure random generation**: Cryptographically secure RNG used
  - *Check for*: `random.random()`, `Math.random()`, time-based seeds for security tokens
  - *Verify*: Using `secrets` (Python), `crypto.randomBytes()` (Node.js)
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.7.3
  - *Example*: See S5.A Python Section 2.4

- [ ] **Encryption key management**: Keys stored securely, not in code or config
  - *Check for*: Encryption keys in environment variables (better but not ideal), keys in code
  - *Verify*: Keys in proper key management service (AWS KMS, Azure Key Vault, HashiCorp Vault)
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.7.4

- [ ] **TLS/HTTPS enforced**: All sensitive communication over HTTPS
  - *Check for*: HTTP for authentication, sensitive data transmission
  - *Verify*: TLS 1.2+ configured, certificate validation enabled
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.7.5

- [ ] **Certificate validation**: Certificate validation not disabled
  - *Check for*: `verify=False` (Python requests), `rejectUnauthorized: false` (Node.js)
  - *Action*: Never disable certificate validation in production

### 3.6 Error Handling & Logging

- [ ] **No information disclosure**: Generic error messages to users
  - *Check for*: Stack traces, database errors, file paths, internal IPs in user-facing errors
  - *Verify*: Production errors return generic message ("An error occurred")
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.8.1

- [ ] **Detailed errors logged securely**: Full error details logged server-side only
  - *Check for*: Missing error logging, insufficient context in logs
  - *Verify*: Errors logged with context (user ID, request ID, timestamp, stack trace)
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.8.1

- [ ] **Security events logged**: Authentication, authorization, validation failures logged
  - *Check for*: Missing logs for login attempts, access denials, security violations
  - *Verify*: Logs include: who, what, when, where, outcome
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.8.2

- [ ] **No sensitive data in logs**: Passwords, tokens, PII excluded from logs
  - *Check for*: Logging request bodies, full exception details with sensitive data
  - *Verify*: Sensitive fields redacted or excluded
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.8.2.B

- [ ] **Exception handling complete**: No unhandled exceptions exposing system details
  - *Check for*: Bare `except:` blocks hiding errors, missing exception handlers
  - *Verify*: All exceptions caught and handled appropriately

### 3.7 Third-Party Dependencies

- [ ] **No new vulnerable dependencies**: SCA scan passed, no Critical/High CVEs
  - *Check for*: New libraries with known vulnerabilities
  - *Tools*: npm audit, pip-audit, Snyk, OWASP Dependency-Check
  - *Reference*: ISMS-POL-A.8.28-S2.4 Section 2.4.2

- [ ] **Dependencies justified**: New dependencies necessary, not for convenience
  - *Check for*: Unnecessary libraries, abandoned packages, excessive dependencies
  - *Verify*: Purpose documented, alternatives considered
  - *Reference*: ISMS-POL-A.8.28-S2.4 Section 2.4.4

- [ ] **Dependencies from trusted sources**: Official package repositories only
  - *Check for*: Unofficial repositories, typosquatting packages, suspicious maintainers
  - *Verify*: Package names correct (check for typos), from official npm/PyPI/Maven
  - *Reference*: ISMS-POL-A.8.28-S2.4 Section 2.4.3

- [ ] **Dependency versions pinned**: Exact versions or compatible ranges specified
  - *Check for*: Unpinned versions (`*`, `latest`), overly broad ranges
  - *Verify*: Lock files committed (package-lock.json, Pipfile.lock, go.sum)
  - *Reference*: ISMS-POL-A.8.28-S2.4 Section 2.4.5

### 3.8 Data Protection

- [ ] **Sensitive data encrypted**: PII, credentials, financial data encrypted at rest
  - *Check for*: Plaintext storage of passwords, credit cards, SSNs
  - *Verify*: Encryption at database level or application level
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.7

- [ ] **Data minimization**: Only necessary data collected and stored
  - *Check for*: Excessive data collection, retaining data longer than needed
  - *Verify*: Data retention policy followed
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.9

- [ ] **Secure data transmission**: Sensitive data encrypted in transit (HTTPS/TLS)
  - *Check for*: HTTP for sensitive data, weak TLS configuration
  - *Verify*: TLS 1.2+ only, strong cipher suites
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.7.5

### 3.9 Business Logic Security

- [ ] **Business logic validated**: Server-side checks for business rules
  - *Check for*: Client-side only validation, missing boundary checks
  - *Example*: Negative quantities, past dates for future events, excessive discounts
  - *Verify*: All business rules enforced on server

- [ ] **Race condition prevention**: Concurrent operations handled safely
  - *Check for*: Time-of-check-time-of-use (TOCTOU) bugs, missing locks
  - *Verify*: Database transactions used, optimistic/pessimistic locking where needed
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.10

- [ ] **Rate limiting**: API endpoints have rate limiting to prevent abuse
  - *Check for*: Missing rate limits on authentication, resource-intensive operations
  - *Verify*: Rate limits appropriate for endpoint type
  - *Reference*: ISMS-POL-A.8.28-S2.2 Section 2.2.11

---

## 4. Risk-Based Review Guidance

### 4.1 Change Risk Classification

**Critical Risk Changes** (require 2+ reviewers including Security Champion):
- Authentication/authorization logic changes
- Cryptographic implementations
- Payment processing
- Privilege escalation functionality
- Admin/superuser functionality
- Security control modifications (WAF rules, CSP, rate limiting)

**High Risk Changes** (require careful review, consider Security Champion):
- API endpoints (public-facing or internal)
- Database queries (especially with user input)
- File upload/download functionality
- External service integrations (APIs, webhooks)
- Session management
- Input validation changes

**Medium Risk Changes** (standard security review):
- Business logic modifications
- Data validation updates
- UI changes handling user data
- Configuration changes
- Dependency updates

**Low Risk Changes** (minimal security review):
- Refactoring without functional changes
- Documentation updates
- Test code (except security tests)
- Cosmetic UI changes (CSS, styling)
- Code comments

### 4.2 Checklist Sections by Risk Level

| Risk Level | Checklist Sections to Apply |
|------------|----------------------------|
| **Critical** | ALL sections (3.1 - 3.9) |
| **High** | 3.1, 3.2, 3.3, 3.4, 3.5, 3.7 (authentication, input, output, authorization, crypto, dependencies) |
| **Medium** | 3.2, 3.3, 3.8, 3.9 (input validation, output encoding, data protection, business logic) |
| **Low** | 3.6 (error handling), 3.7 if dependencies changed |

### 4.3 Security Champion Review Requirements

**When Security Champion review REQUIRED**:
- Critical risk changes (always)
- High risk changes with multiple security concerns
- Developer unfamiliar with security requirements
- SAST findings not understood by developer

**Security Champion Responsibilities**:
- Use full checklist (all sections)
- Validate security test coverage
- Approve or escalate to Application Security Team
- Provide mentoring feedback to developer

---

## 5. Review Outcome Actions

### 5.1 Approve

**Criteria**:
- All applicable checklist items passed
- No security concerns identified
- Automated checks passed (SAST, SCA, tests)
- Security tests adequate for risk level

**Action**:
- Approve pull request
- No additional comments needed (unless suggesting improvements)

### 5.2 Request Changes

**Criteria**:
- Security issues identified (checklist items failed)
- Insufficient test coverage for security-relevant changes
- SAST findings not addressed

**Action**:
- **Document specific concerns**: Which checklist items failed
- **Link to policy sections**: Reference relevant S2.2 requirements
- **Provide examples**: Show correct pattern (link to S5.A if applicable)
- **Set expectations**: What needs to change for approval

**Example Comment**:
```
**Security Concern - Input Validation (S5.B #3.2)**

SQL query is vulnerable to SQL injection (S2.2 Section 2.2.3.2.A):

❌ Current code:
query = f"SELECT * FROM users WHERE id = {user_id}"

✅ Required change:
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

See S5.A Python Section 2.2 for examples.
```

### 5.3 Escalate to Security Team

**When to Escalate**:
- Complex security concern beyond reviewer expertise
- Suspected vulnerability requiring expert validation
- Architecture-level security design issue
- Need for threat modeling session
- Developer disputes security finding

**Escalation Process**:
1. **Document concern**: Clear description of security issue
2. **Tag Security Team**: Mention @security-team in PR comments
3. **Provide context**: Risk level, affected components, potential impact
4. **Continue review**: Other non-security aspects can be reviewed in parallel

**Security Team Response SLA**:
- Critical: 4 business hours
- High: 1 business day
- Medium: 3 business days

---

## 6. Post-Review Actions

### 6.1 Tracking Security Findings

- [ ] **Security findings documented**: Issues logged in tracking system (JIRA, GitHub Issues)
  - *Include*: Checklist item failed, affected code, remediation guidance
  
- [ ] **Developer acknowledged feedback**: Developer responded to all security comments
  - *Verify*: Understood the issue, committed to fixing
  
- [ ] **Re-review scheduled**: If significant changes made, re-review required
  - *Criteria*: More than 20% of code changed, new functionality added

### 6.2 Learning and Improvement

- [ ] **Patterns documented**: Common security mistakes added to team wiki
  
- [ ] **Checklist updated**: If checklist missed an issue, propose update to Application Security Lead
  
- [ ] **Developer training**: Recommend training if repeated security issues

---

## 7. Appendix: Quick Reference Card

**For quick reviews, check these high-priority items**:

✅ **Top 10 Security Review Items**:
1. Authentication present on protected endpoints
2. Input validated (SQL injection, command injection prevention)
3. Output encoded (XSS prevention)
4. Authorization enforced server-side
5. No hardcoded secrets (scan for passwords, API keys)
6. Cryptographically secure RNG for tokens
7. No vulnerable dependencies (SCA scan green)
8. Generic error messages (no information disclosure)
9. Security events logged
10. HTTPS enforced for sensitive data

---

## 8. Document History

| Date | Version | Change Summary | Author |
|------|---------|----------------|--------|
| [Approval Date] | 1.0 | Initial code review checklist template | Application Security Lead |

---

**END OF DOCUMENT**