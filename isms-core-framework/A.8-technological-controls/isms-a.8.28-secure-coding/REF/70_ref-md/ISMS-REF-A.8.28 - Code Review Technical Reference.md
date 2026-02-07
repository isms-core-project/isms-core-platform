**ISMS-REF-A.8.28 - Code Review Technical Reference**

**Document Control - ISMS-REF-A.8.28**

| Field | Value |
|-------|-------|
| **Document Title** | Code Review Technical Reference |
| **Document Type** | Technical Reference (REF) |
| **Document ID** | ISMS-REF-A.8.28 |
| **Document Creator** | Application Security Lead |
| **Document Owner** | Application Security Lead |
| **Approved By** | Application Security Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [Date] |
| **Classification** | Internal |
| **Status** | Draft |

---

## Disclaimer

**CRITICAL**: This is an informational reference document and is **NOT** part of the formal ISMS policy framework.

The information contained herein provides technical guidance and methodological details but **does NOT establish mandatory requirements**.

**Binding policy requirements** are defined in **ISMS-POL-A.8.28 (Secure Coding Policy)**.

**Purpose**: Support code review implementation by providing:

- Detailed security code review checklists
- Method comparisons and guidance
- Risk-based review approaches
- Implementation best practices

**Usage**: Technical reference for code reviewers, Security Champions, and development teams. Content may require updates as vulnerability patterns evolve—check publication date.

---

# Purpose & Scope

## Reference Objective

This document provides **actionable security criteria** for code reviewers. It operationalizes the code review requirements from ISMS-POL-A.8.28 Section 2.3, translating policy into practical review steps.

*"The first principle is that you must not fool yourself—and you are the easiest person to fool." - Richard Feynman*

**Goal**: Enable code reviewers to identify security issues systematically without requiring deep security expertise for every review.

## Topics Covered

- Pre-review preparation checklist
- Core security review criteria (authentication, input validation, authorization, cryptography, logging, error handling)
- Risk-based review approach
- Common patterns and anti-patterns
- Escalation procedures

## Relationship to Policy

**ISMS-POL-A.8.28 requires** (binding):

- Peer code review for all production code
- Security-focused review criteria
- Security Champions participation in reviews
- Application Security Team review for high-risk changes

**This REF document explains** (informational):

- HOW to perform security-focused code reviews
- WHAT security issues to look for
- WHEN to escalate to Security Champions or Application Security Team
- Risk-based checklist application

---

# How to Use This Checklist

## Not Every Item for Every Review

**Risk-Based Approach**:

**High-Risk Changes** (use full checklist):

- Authentication or authorization changes
- Cryptography implementation
- Payment or financial transaction handling
- PII processing or data exposure
- Security control modifications
- Third-party integrations with sensitive data

**Medium-Risk Changes** (focus on relevant sections):

- API endpoints → Input validation + Authorization
- Database queries → SQL injection prevention
- File operations → Path traversal prevention
- Web UI changes → XSS + CSRF prevention

**Low-Risk Changes** (minimal security review):

- Refactoring without functionality changes
- Documentation updates
- Configuration changes (non-security)
- Test-only changes

## Integration Points

**Pull Request Templates**:
```markdown
# Security Checklist (if applicable)

- [ ] Input validation present and correct
- [ ] Output encoding appropriate for context
- [ ] SQL queries parameterized
- [ ] No hardcoded secrets
- [ ] Authorization checks present

```

**Review Tools**:

- Link checklist items in review comments (e.g., "Fails 3.2.3: SQL injection risk")
- Use review tool labels (security-review-required, security-approved)

**Training**:

- Use checklist in code review training workshops
- Security Champions master checklist application
- Periodic checklist refreshers

## When to Escalate

**Escalate to Security Champion**:

- Checklist item unclear or ambiguous
- Security concern beyond your expertise
- Multiple checklist items failed
- Complex security pattern requiring validation

**Escalate to Application Security Team**:

- Suspected vulnerability requiring expert validation
- Architecture-level security concern
- Need for threat modeling session
- Critical/High severity finding from automated tools

**Escalation Channels**:

- Slack: #security-champions or #appsec
- Email: security@[organization].com
- Tag in PR: @security-champions or @appsec-team

---

# Pre-Review Checklist

**Complete BEFORE reviewing code** (saves time, ensures quality):

- [ ] **Automated checks passed**: SAST, SCA, unit tests, linters all green?
  - *If not*: Review automated findings first, ensure they're addressed or suppressed with justification
  
- [ ] **Change description clear**: PR description explains WHAT changed and WHY?
  - *Check for*: Vague descriptions ("fixed bug", "updates"), missing context
  - *Action*: Request clarification if unclear

- [ ] **Risk level identified**: Does PR indicate risk level (Critical/High/Medium/Low)?
  - *If not identified*: Assess risk per Section 2.1 criteria
  
- [ ] **Security-relevant changes flagged**: Does PR author identify security implications?
  - *Check for*: Authentication, authorization, input handling, cryptography, data access
  - *Action*: If security-relevant but not flagged, apply appropriate checklist sections

- [ ] **Change scope reasonable**: Is PR focused (not changing 50 files with unrelated changes)?
  - *If too large*: Request split into smaller, reviewable PRs
  
- [ ] **Tests included**: Are security-relevant changes covered by tests?
  - *Check for*: Input validation tests, authorization tests, negative test cases
  - *Policy Reference*: ISMS-POL-A.8.28 Section 2.3.1

---

# Core Security Review Checklist

## Authentication & Session Management

- [ ] **Authentication checks present**: All protected endpoints verify user authentication
  - *Check for*: Missing authentication on API endpoints, admin pages, data access
  - *Test*: Can endpoint be accessed without authentication?
  - *Policy Reference*: ISMS-POL-A.8.28 Section 2.2

- [ ] **Session tokens secure**: Tokens are random, unpredictable, with HttpOnly/Secure flags
  - *Check for*: Predictable session IDs, sequential tokens, tokens in URLs
  - *Verify*: Cookie attributes include `HttpOnly`, `Secure`, `SameSite=Strict/Lax`

- [ ] **Password handling secure**: Passwords hashed with bcrypt/Argon2, never logged
  - *Check for*: Plaintext passwords, weak hashing (MD5, SHA1, SHA256 without salt)
  - *Verify*: No passwords in logs, error messages, or debug output
  - *Example*: See ISMS-CTX-A.8.28 Python Section 2.6

- [ ] **Multi-factor authentication (MFA) enforced**: MFA required for privileged accounts
  - *Check for*: Admin accounts, financial operations bypassing MFA

- [ ] **Session timeout appropriate**: Sessions expire after inactivity period
  - *Check for*: No timeout, excessively long timeout (>30 min for high-risk apps)

- [ ] **Logout functionality secure**: Logout invalidates session on server-side
  - *Check for*: Client-side only logout, session still valid after logout
  - *Test*: Session token rejected after logout

## Input Validation

- [ ] **All input validated**: Server-side validation present for ALL user input
  - *Check for*: Client-side only validation, missing validation on API endpoints
  - *Sources*: Forms, URL parameters, headers, cookies, file uploads, API requests
  - *Policy Reference*: ISMS-POL-A.8.28 Section 2.2

- [ ] **Whitelist approach used**: Validation uses allowlist (not blocklist)
  - *Check for*: Blacklist patterns ("reject if contains X"), incomplete blocklists
  - *Correct*: "Accept only if matches Y" (e.g., alphanumeric only)

- [ ] **SQL injection prevented**: Parameterized queries used, no string concatenation
  - *Check for*: String concatenation in SQL (f-strings, +, .format()), dynamic query building
  - *Verify*: All database queries use parameterized statements or ORM safely
  - *Example*: See ISMS-CTX-A.8.28 Python Section 2.2, SQL Section 7

- [ ] **Command injection prevented**: No direct shell calls with user input
  - *Check for*: `os.system()`, `subprocess` with `shell=True`, `eval()`, `exec()`
  - *Verify*: Commands use argument lists, not string concatenation
  - *Example*: See ISMS-CTX-A.8.28 Python Section 2.3

- [ ] **Path traversal prevented**: File paths validated, no directory traversal
  - *Check for*: Direct concatenation of user input to file paths
  - *Verify*: Paths resolved and validated within allowed directory
  - *Example*: See ISMS-CTX-A.8.28 Python Section 2.4

- [ ] **XML external entity (XXE) prevented**: XML parsing disables external entities
  - *Check for*: Default XML parser configuration (often vulnerable)
  - *Verify*: External entities explicitly disabled in parser configuration
  - *Example*: See ISMS-CTX-A.8.28 Java Section 4.3

- [ ] **File upload validation**: Type, size, content validation present
  - *Check for*: Extension-only validation, no content validation, no size limits
  - *Verify*: Magic number validation, malware scanning, size limits enforced

- [ ] **Input length limits**: Maximum length enforced (prevent buffer overflow, DoS)
  - *Check for*: Unlimited input length, excessively large limits

## Output Encoding & XSS Prevention

- [ ] **XSS prevention**: Output encoded for context (HTML, JavaScript, URL, CSS)
  - *Check for*: Unencoded user input in HTML, `innerHTML`, `dangerouslySetInnerHTML`
  - *Verify*: Framework auto-escaping used or manual encoding applied
  - *Example*: See ISMS-CTX-A.8.28 JavaScript Section 3.2

- [ ] **Content Security Policy (CSP) headers**: CSP configured to mitigate XSS impact
  - *Check for*: Missing CSP headers, overly permissive CSP (`unsafe-inline`, `unsafe-eval`)
  - *Verify*: CSP restricts script sources, disables inline scripts where possible

- [ ] **CSRF protection**: Tokens present for state-changing operations
  - *Check for*: Missing CSRF tokens on POST/PUT/DELETE/PATCH
  - *Verify*: Tokens validated on server-side, tokens unpredictable
  - *Example*: See ISMS-CTX-A.8.28 JavaScript Section 3.4

- [ ] **HTTP security headers**: Security headers configured properly
  - *Check for*: Missing `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`
  - *Verify*: Headers present and correctly configured

## Authorization & Access Control

- [ ] **Authorization enforced server-side**: All access control checks on server
  - *Check for*: Client-side only authorization (hidden UI elements), missing server checks
  - *Verify*: Every protected resource has server-side authorization check

- [ ] **IDOR prevention**: User ownership verified before resource access
  - *Check for*: Direct ID access without ownership check (e.g., `/api/orders/123` accessible by any user)
  - *Test*: Can user access another user's resources by changing ID?

- [ ] **Least privilege principle**: Operations use minimum necessary permissions
  - *Check for*: Overly permissive roles, admin-level operations for user tasks
  - *Verify*: Database connections use limited privileges, not root/admin

- [ ] **Role-based access control (RBAC)**: Roles correctly assigned and checked
  - *Check for*: Hardcoded user IDs instead of roles, missing role checks

- [ ] **Privilege escalation prevented**: No way to elevate privileges improperly
  - *Check for*: User-controllable role assignments, missing authorization on privilege changes
  - *Test*: Can user grant themselves admin role?

## Cryptography

- [ ] **Approved algorithms only**: AES-256-GCM, RSA-2048+, ECDSA-256+, SHA-256+
  - *Check for*: DES, 3DES, RC4, MD5, SHA1, RSA-1024, ECB mode, custom crypto
  - *Policy Reference*: ISMS-POL-A.8.28 Section 2.2, ISMS-POL-A.8.24 (Cryptography)

- [ ] **No hardcoded secrets**: Credentials from environment variables or secret manager
  - *Check for*: API keys, passwords, tokens, private keys in code
  - *Tools*: Use secret scanning tool (Gitleaks, TruffleHog, GitHub Secret Scanning)
  - *Action*: If found, rotate credentials immediately

- [ ] **Secure random generation**: Cryptographically secure RNG used
  - *Check for*: `random.random()`, `Math.random()`, time-based seeds for security tokens
  - *Verify*: Using `secrets` (Python), `crypto.randomBytes()` (Node.js), `SecureRandom` (Java)
  - *Example*: See ISMS-CTX-A.8.28 language-specific sections

- [ ] **Encryption key management**: Keys stored securely, not in code or config
  - *Check for*: Encryption keys in environment variables (better but not ideal), keys in code
  - *Verify*: Keys in proper key management service (AWS KMS, Azure Key Vault, HashiCorp Vault)

- [ ] **TLS/HTTPS enforced**: All sensitive communication over HTTPS
  - *Check for*: HTTP for authentication, sensitive data transmission
  - *Verify*: HSTS headers present, no mixed content

## Error Handling & Logging

- [ ] **Generic error messages to users**: No stack traces, SQL errors, file paths exposed
  - *Check for*: Detailed error messages revealing system information
  - *Verify*: User-facing errors are generic ("An error occurred"), details logged server-side

- [ ] **Security events logged**: Authentication, authorization failures, input validation failures logged
  - *Check for*: Missing security event logging
  - *Verify*: Sufficient detail for incident investigation (user, action, result, timestamp)
  - *Policy Reference*: ISMS-POL-A.8.28 Section 2.2

- [ ] **No sensitive data in logs**: Passwords, tokens, PII excluded from logs
  - *Check for*: Full request/response logging, password logging, credit card numbers
  - *Verify*: Sensitive data redacted or excluded

- [ ] **Exceptions handled securely**: Catch blocks don't expose sensitive information
  - *Check for*: Empty catch blocks, exceptions propagated to user interface

## Data Protection

- [ ] **Sensitive data encrypted**: PII, financial data, credentials encrypted at rest and in transit
  - *Check for*: Plaintext storage of sensitive data
  - *Policy Reference*: ISMS-POL-A.8.24 (Cryptography)

- [ ] **Data minimization**: Only necessary data collected and retained
  - *Check for*: Excessive data collection, indefinite retention

- [ ] **Secure data deletion**: Sensitive data deleted securely when no longer needed
  - *Verify*: Not just marked deleted but actually removed or cryptographically erased
  - *Policy Reference*: ISMS-POL-A.8.10 (Information Deletion)

## Third-Party Dependencies

- [ ] **Dependencies scanned for vulnerabilities**: SCA tool reports reviewed
  - *Check for*: New vulnerable dependencies introduced
  - *Verify*: No Critical/High vulnerabilities in dependencies

- [ ] **Dependencies from trusted sources**: Official repositories used
  - *Check for*: Dependencies from unknown or untrusted sources
  - *Verify*: Package integrity (checksums, signatures)

- [ ] **Dependency versions pinned**: Lock files present and updated
  - *Check for*: Unpinned versions, missing lock files
  - *Verify*: `package-lock.json`, `requirements.txt`, `Gemfile.lock` committed

---

# Risk-Based Review Guidelines

## Critical Risk Changes

**Triggers**:

- Authentication system changes
- Authorization model changes
- Cryptographic implementation
- Payment processing
- PII handling changes

**Review Approach**:

- Full checklist application (all sections)
- Mandatory Security Champion or Application Security Team review
- Threat modeling session (if architectural change)
- Penetration testing (if significant change)
- Extensive testing including negative test cases

**Approval**:

- Development Manager + Security Champion + Application Security Lead

## High Risk Changes

**Triggers**:

- New API endpoints with data access
- Database query changes
- File upload functionality
- Third-party integrations with data sharing
- Admin interface changes

**Review Approach**:

- Relevant checklist sections (focus on input validation, authorization, data protection)
- Security Champion review recommended
- Security testing (SAST, DAST)
- Functional and security test cases

**Approval**:

- Development Manager + Security Champion

## Medium Risk Changes

**Triggers**:

- UI changes with user input
- Report generation with data access
- Configuration changes affecting security
- Logging or monitoring changes

**Review Approach**:

- Targeted checklist items (input validation, XSS prevention)
- Peer review with security awareness
- Automated security scanning

**Approval**:

- Peer reviewer with security training

## Low Risk Changes

**Triggers**:

- Refactoring without functionality changes
- Documentation updates
- Test-only changes
- UI styling (CSS) without logic changes

**Review Approach**:

- Standard code review
- Verify no unintended security impact
- Quick scan for accidentally introduced issues

**Approval**:

- Standard peer review

---

# Common Patterns and Anti-Patterns

## Secure Patterns (Encourage)

**Input Validation Pattern**:
```python
# Whitelist validation
ALLOWED_FIELDS = {'name', 'email', 'age'}
def validate_input(data):
    if not all(key in ALLOWED_FIELDS for key in data.keys()):
        raise ValidationError("Invalid field")
    # Additional validation...
```

**Authorization Pattern**:
```python
# Ownership check before resource access
def get_order(order_id, current_user):
    order = Order.query.get(order_id)
    if order.user_id != current_user.id:
        raise Forbidden("Access denied")
    return order
```

**Secure Configuration Pattern**:
```python
# Environment-based configuration
API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ConfigError("API_KEY must be set")
```

## Anti-Patterns (Discourage)

**String Concatenation for SQL**:
```python
# ANTI-PATTERN - SQL injection vulnerability
query = f"SELECT * FROM users WHERE id = {user_id}"
```

**Client-Side Authorization**:
```javascript
// ANTI-PATTERN - Authorization must be server-side
if (user.role === 'admin') {
  showAdminPanel();  // Client-side only, easily bypassed
}
```

**Weak Password Hashing**:
```python
# ANTI-PATTERN - Weak hashing
import hashlib
hash = hashlib.md5(password.encode()).hexdigest()
```

---

# Review Documentation

## Review Comment Template

```
**Security Issue: [Issue Type]**

**Severity**: [Critical/High/Medium/Low]

**Issue**: [Brief description of security problem]

**Location**: [File and line number]

**Risk**: [What attacker could do]

**Recommendation**: [How to fix]

**Reference**: ISMS-POL-A.8.28 Section [X.Y] / Checklist item [4.X]

**Example**: [Code example or link to ISMS-CTX-A.8.28]
```

## Security Approval Comment

```
**Security Review Complete**

Reviewed by: [Security Champion Name]
Date: [DD.MM.YYYY]

Checklist sections applied:

- [X] Authentication (4.1)
- [X] Input Validation (4.2)
- [X] Authorization (4.4)

Findings:

- [Issue 1]: Addressed in commit [hash]
- [Issue 2]: Risk accepted with justification [link]

**Approved for merge** with no outstanding security issues.
```

---

# Escalation Procedures

## When to Escalate

**To Security Champion**:

- Unclear checklist application
- Security pattern validation needed
- Multiple failed checklist items
- Training or guidance needed

**To Application Security Team**:

- Suspected Critical/High vulnerability
- Architecture-level security concern
- Need for threat modeling
- Tool findings requiring expert validation
- Penetration testing recommendation

## Escalation Channels

| Issue Type | Channel | Response Time |
|------------|---------|---------------|
| **Question during review** | Slack #security-champions | < 4 hours (business hours) |
| **Security concern (non-urgent)** | Slack #appsec | < 1 business day |
| **Security vulnerability (High)** | Email security@org.com + Slack | < 4 hours |
| **Security vulnerability (Critical)** | Incident response process | Immediate |

---

# Document Maintenance

**Update Frequency**: Quarterly or when:

- OWASP Top 10 updated
- New vulnerability patterns identified
- Organizational technology stack changes
- Policy requirements change (ISMS-POL-A.8.28 updates)

**Owner**: Application Security Lead

**Review Triggers**:

- Major security incidents requiring checklist updates
- Developer feedback on checklist clarity or completeness
- Security tool integration changes
- Training effectiveness feedback

**Collaboration**:

- Security Champions validate practical applicability
- Development Teams provide usability feedback
- Application Security Team ensures technical accuracy

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead | Initial code review reference extracted from consolidated policy |

---

**END OF ISMS-REF-A.8.28**

*This technical reference supports ISMS-POL-A.8.28 implementation. Binding requirements are in the policy, not this document.*
<!-- QA_VERIFIED: 2026-02-01 -->
