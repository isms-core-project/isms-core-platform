# INSTRUCTIONS FOR NEXT SESSION - ANNEXES (S5)
## ISMS Control 8.28 - Secure Coding - Annexes Creation Guide

**Session Context**: This document provides instructions for completing the Annexes (S5) section of the ISMS Control 8.28 Secure Coding Policy Framework.

**Status**: Policy sections S1, S2 (including S2.1-S2.4), S3, and S4 are complete and will be uploaded to the project before this session.

---

## 1. OVERVIEW

### 1.1 What Needs to Be Created

**5 Annex Documents**:
1. **ISMS-POL-A.8.28-S5** - Annexes Overview (~300 lines)
2. **ISMS-POL-A.8.28-S5.A** - Language-Specific Guidelines (~400 lines)
3. **ISMS-POL-A.8.28-S5.B** - Code Review Checklist Template (~400 lines)
4. **ISMS-POL-A.8.28-S5.C** - Vulnerability Response Procedures (~400 lines)
5. **ISMS-POL-A.8.28-S5.D** - Quick Reference Guide (~300 lines)

**Total Estimated**: ~1,800 lines, approximately 35-40K tokens

### 1.2 Purpose of Annexes

Annexes provide **practical, operational guidance** that supplements the policy requirements:
- S5.A: Technology-specific secure coding practices
- S5.B: Actionable checklist for code reviewers
- S5.C: Step-by-step vulnerability handling procedures
- S5.D: One-page quick reference for developers

---

## 2. DOCUMENT SPECIFICATIONS

### 2.1 Standard Document Header (Use for All Annexes)
````markdown
# ISMS-POL-A.8.28-S5[.X]
## Secure Coding - [Section Title]

**Document ID**: ISMS-POL-A.8.28-S5[.X]
**Title**: Secure Coding - [Section Title]  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead / [Role] | Initial [document type] |

**Review Cycle**: [Frequency]
**Next Review Date**: [Approval Date + period]
**Approvers**: 
- Primary: [Role]
- Technical Review: [Role]
- [Additional as needed]

**Distribution**: [Target audience]
**Related Documents**: [References to other sections]

---
````

### 2.2 Formatting Standards

- **Line limit**: 300-400 lines per document (hard limit)
- **Code blocks**: Use triple backticks with language identifiers
- **Tables**: Use for structured comparisons, checklists
- **Examples**: ✅ CORRECT vs. ❌ INCORRECT pattern
- **Quotes**: Use Feynman/engineering wisdom quotes sparingly
- **Cross-references**: Link to policy sections (e.g., "See ISMS-POL-A.8.28-S2.2")

---

## 3. DETAILED SPECIFICATIONS BY DOCUMENT

### 3.1 ISMS-POL-A.8.28-S5 (Annexes Overview)

**Target Length**: ~300 lines

**Document Control**:
- Review Cycle: Annual
- Approvers: CISO (primary), Application Security Lead (technical review)
- Distribution: All developers, security team

**Content Structure**:

#### 3.1.1 Introduction
- Purpose of annexes (practical supplement to policy)
- How annexes relate to policy sections
- When to use each annex

#### 3.1.2 Annex Inventory
Table listing all annexes:

| Annex ID | Title | Purpose | Primary Audience |
|----------|-------|---------|------------------|
| S5.A | Language-Specific Guidelines | Secure coding practices per language | Developers (by language) |
| S5.B | Code Review Checklist | Security-focused review criteria | Code reviewers, Security Champions |
| S5.C | Vulnerability Response | Incident handling procedures | Security Team, Developers |
| S5.D | Quick Reference | One-page developer guide | All developers |

#### 3.1.3 Annex Maintenance
- How annexes are updated (more frequently than core policy)
- Approval process (simpler than policy - Application Security Lead approval)
- Technology-specific update triggers (new language adopted, framework updated)

#### 3.1.4 Relationship to External Standards
Brief mapping to:
- OWASP ASVS (Application Security Verification Standard)
- SEI CERT Coding Standards
- Language-specific security guides (Microsoft, Oracle, etc.)
- Industry cheat sheets (OWASP Cheat Sheet Series)

#### 3.1.5 Usage Guidance
- When to reference annexes (during code review, when starting new project)
- How to contribute improvements (developer feedback process)
- Integration with tooling (IDE plugins, linters referencing standards)

---

### 3.2 ISMS-POL-A.8.28-S5.A (Language-Specific Guidelines)

**Target Length**: ~400 lines

**Document Control**:
- Review Cycle: Semi-annual (or when major language version released)
- Approvers: Application Security Lead (primary), Senior Developers (by language, consulted)
- Distribution: All developers

**Content Structure**:

#### 3.2.1 Introduction
- Purpose: Language-specific secure coding patterns
- Coverage philosophy: High-value vulnerabilities for commonly-used languages
- Reference to external standards (OWASP, SEI CERT, vendor documentation)

#### 3.2.2 Language Coverage
For each language organization uses (prioritize top 5-6):

**Language Template** (repeat for each language, ~50 lines each):

##### 3.2.2.X [Language Name] (e.g., Python)

**Common Vulnerability Patterns**:
- Top 3-5 vulnerabilities specific to this language
- Example: Python pickle deserialization, SQL injection with string formatting

**Security Best Practices**:
- Input validation (language-specific mechanisms)
- Output encoding (template engines, encoding libraries)
- Authentication/authorization (framework-specific)
- Cryptography (recommended libraries: Python cryptography, secrets module)
- Database access (parameterized queries, ORM security)

**Code Examples** (3-4 examples):

✅ **CORRECT - Secure Pattern**:
````python
# Parameterized query
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
````

❌ **INSECURE - Avoid This**:
````python
# SQL injection vulnerability
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
````

**Recommended Tools**:
- SAST tools: Bandit, Semgrep
- Linters: Pylint with security plugins
- Dependency scanners: Safety, pip-audit

**Reference Standards**:
- OWASP Python Security Cheat Sheet
- Python Packaging Authority Security Guidelines

---

**Suggested Language Coverage** (prioritize based on organization usage):
1. **Python**: SQL injection, pickle deserialization, command injection
2. **Java**: Deserialization, XXE, SQL injection, authentication
3. **JavaScript/TypeScript**: XSS, prototype pollution, CSRF, regex DoS
4. **C#/.NET**: SQL injection, XXE, deserialization, authentication
5. **Go**: SQL injection, command injection, race conditions
6. **PHP**: SQL injection, remote code execution, file inclusion (if still used)

#### 3.2.3 Framework-Specific Guidance (Optional)
If organization heavily uses specific frameworks:
- React security (XSS prevention, dangerouslySetInnerHTML)
- Django security (CSRF, SQL injection prevention)
- Spring security (authentication, authorization)

#### 3.2.4 Cross-Language Security Principles
Universal patterns applicable to all languages:
- Never trust user input (regardless of language)
- Use framework security features (don't reinvent authentication)
- Keep dependencies updated (applies to all ecosystems)
- Fail securely (default deny in all languages)

#### 3.2.5 Language Update Process
How to request additions for new languages or framework updates

---

### 3.3 ISMS-POL-A.8.28-S5.B (Code Review Checklist Template)

**Target Length**: ~400 lines

**Document Control**:
- Review Cycle: Quarterly (or when OWASP Top 10 updated)
- Approvers: Application Security Lead (primary), Security Champions (consulted)
- Distribution: Code reviewers, Security Champions, developers

**Content Structure**:

#### 3.3.1 Introduction
- Purpose: Actionable security checklist for code reviewers
- How to use: Not every item for every review (risk-based)
- Integration: Link to PR templates, review tools

#### 3.3.2 Pre-Review Checklist
Before starting review:
- [ ] Automated checks passed (SAST, tests, linters)?
- [ ] Change description clear (what and why)?
- [ ] Risk level identified (Critical/High/Medium/Low)?
- [ ] Security-relevant changes flagged?

#### 3.3.3 Core Security Review Checklist

**Format: Checkbox list with guidance**

##### Authentication & Session Management
- [ ] **Authentication checks present**: All protected endpoints verify authentication
  - *Check for*: Missing authentication on API endpoints, admin pages
  - *Tools*: Manual review, SAST
- [ ] **Session tokens secure**: Random, unpredictable, HttpOnly/Secure flags
  - *Check for*: Predictable session IDs, tokens in URLs
  - *Reference*: S2.2 Section 2.2.5.3
- [ ] **Password handling secure**: Hashed (bcrypt/Argon2), not logged
  - *Check for*: Plaintext passwords, weak hashing (MD5/SHA1)
  - *Reference*: S2.2 Section 2.2.5.1

##### Input Validation
- [ ] **All input validated**: Server-side validation, whitelist approach
  - *Check for*: Client-side only, blacklist validation
  - *Reference*: S2.2 Section 2.2.3
- [ ] **SQL injection prevented**: Parameterized queries, no string concatenation
  - *Check for*: String concatenation in SQL, dynamic query building
  - *Reference*: S2.2 Section 2.2.3.2.A
- [ ] **Command injection prevented**: No direct shell calls with user input
  - *Check for*: os.system(), exec(), shell=True with user input
  - *Reference*: S2.2 Section 2.2.3.2.B

##### Output Encoding
- [ ] **XSS prevention**: Output encoded for context (HTML, JS, URL)
  - *Check for*: Unencoded user input in templates, innerHTML usage
  - *Reference*: S2.2 Section 2.2.4.1
- [ ] **CSRF protection**: Tokens present for state-changing operations
  - *Check for*: Missing CSRF tokens on POST/PUT/DELETE
  - *Reference*: S2.2 Section 2.2.4.2

##### Authorization
- [ ] **Authorization enforced**: Server-side checks, not just UI hiding
  - *Check for*: Client-side authorization, missing server checks
  - *Reference*: S2.2 Section 2.2.6.1
- [ ] **IDOR prevention**: Verify user owns resources before access
  - *Check for*: Direct ID access without ownership check
  - *Reference*: S2.2 Section 2.2.6.1.B
- [ ] **Least privilege**: Operations use minimum necessary permissions
  - *Check for*: Overly permissive roles, admin-level operations

##### Cryptography
- [ ] **Approved algorithms**: AES-GCM, RSA-2048+, SHA-256+
  - *Check for*: DES, MD5, SHA1, ECB mode, custom crypto
  - *Reference*: S2.2 Section 2.2.7.1
- [ ] **No hardcoded secrets**: Credentials from environment/vault
  - *Check for*: API keys in code, passwords in config files
  - *Reference*: S2.1 Section 2.1.6.2.C
- [ ] **Secure random**: Using cryptographically secure RNG
  - *Check for*: random.random() for tokens, predictable IDs
  - *Reference*: S2.2 Section 2.2.7.3

##### Error Handling & Logging
- [ ] **No information disclosure**: Generic error messages to users
  - *Check for*: Stack traces, database errors, file paths in responses
  - *Reference*: S2.2 Section 2.2.8.1
- [ ] **Security events logged**: Authentication, authorization, validation failures
  - *Check for*: Missing security event logging
  - *Reference*: S2.2 Section 2.2.8.2
- [ ] **No sensitive data in logs**: Passwords, tokens, PII excluded
  - *Check for*: Logging request bodies, full exception details
  - *Reference*: S2.2 Section 2.2.8.2.B

##### Third-Party Dependencies
- [ ] **No new vulnerable dependencies**: SCA scan passed
  - *Check for*: New libraries with known CVEs
  - *Reference*: S2.4 Section 2.4.2
- [ ] **Dependencies justified**: Necessary additions, not convenience
  - *Check for*: Unnecessary dependencies, abandoned packages
  - *Reference*: S2.4 Section 2.4.4

##### File Handling
- [ ] **File upload validation**: Type, size, content validation
  - *Check for*: Extension-only checks, no content validation
  - *Reference*: S2.2 Section 2.2.3.3
- [ ] **File storage secure**: Outside web root, renamed, scanned
  - *Check for*: Files in public directories, original names preserved
  - *Reference*: S2.2 Section 2.2.3.3.B

#### 3.3.4 Risk-Based Review Guidance

**Critical Risk Changes** (require 2+ reviewers including Security Champion):
- Authentication/authorization changes
- Cryptographic implementations
- Payment processing
- Privilege escalation
- Admin functionality

**High Risk Changes**:
- API endpoints (public or internal)
- Database queries
- File uploads
- External integrations

**Medium Risk Changes**:
- Business logic
- Data validation
- UI changes handling user data

**Low Risk Changes**:
- Refactoring (no functional change)
- Documentation
- Test code (except security tests)

#### 3.3.5 Review Outcome Actions

**Approve**:
- All checklist items passed
- No security concerns identified
- Automated checks passed

**Request Changes**:
- Security issues identified (specify which checklist items failed)
- Document specific concerns in review comments
- Link to relevant policy sections

**Escalate to Security Team**:
- Complex security concern beyond reviewer expertise
- Suspected vulnerability requiring Security Team validation
- Architecture-level security concern

#### 3.3.6 Post-Review Actions
- [ ] Security findings tracked (JIRA, GitHub Issues)
- [ ] Developer acknowledged and addressed feedback
- [ ] Re-review if significant changes made

---

### 3.4 ISMS-POL-A.8.28-S5.C (Vulnerability Response Procedures)

**Target Length**: ~400 lines

**Document Control**:
- Review Cycle: Annual (or after major incident)
- Approvers: CISO (primary), Application Security Lead, Incident Response Lead
- Distribution: Security Team, Development Managers, DevOps, Security Champions

**Content Structure**:

#### 3.4.1 Introduction
- Purpose: Step-by-step procedures for vulnerability handling
- Scope: Vulnerabilities in organizational code (not infrastructure, not vendor products)
- Integration: Links to Incident Response Policy

#### 3.4.2 Vulnerability Discovery

**Discovery Sources**:
1. **Internal**: SAST, DAST, SCA scans, code review, penetration testing
2. **External**: Security researchers, bug bounty, customer reports
3. **Public Disclosure**: CVE databases, vendor advisories, social media

**Initial Actions** (within 24 hours):
- Log vulnerability report (tracking system)
- Assign initial severity (Critical/High/Medium/Low - can be adjusted later)
- Assign to Application Security Team for triage
- Acknowledge receipt to reporter (if external)

#### 3.4.3 Vulnerability Triage

**Triage Process** (within 48 hours of discovery):

**Step 1 - Validate Vulnerability**:
- Reproduce vulnerability in test environment
- Confirm exploitability (is it actually exploitable or false positive?)
- Identify affected versions/components
- Document proof of concept

**Step 2 - Severity Assessment**:
Use CVSS 3.1 scoring or organizational risk matrix:

| Severity | CVSS Score | Impact Examples | Initial Response |
|----------|------------|-----------------|------------------|
| **Critical** | 9.0-10.0 | RCE, authentication bypass, data breach | Immediate escalation to CISO |
| **High** | 7.0-8.9 | SQL injection, XSS, privilege escalation | Escalate to Application Security Lead |
| **Medium** | 4.0-6.9 | Authorization bypass (limited), CSRF | Standard remediation process |
| **Low** | 0.1-3.9 | Information disclosure (limited), minor issues | Standard remediation process |

**Step 3 - Impact Analysis**:
- Which applications/services affected?
- Which environments exposed (production, staging, development)?
- How many users/customers potentially impacted?
- Regulatory implications (GDPR breach notification required?)
- Reputational risk

**Step 4 - Assignment**:
- Assign to development team/developer for remediation
- Set remediation deadline per SLA (S2.3 Section 2.3.3.3.B)
- Create tracking ticket with all triage information
- Notify stakeholders (Development Manager, Product Owner if customer-impacting)

#### 3.4.4 Vulnerability Remediation

**Remediation Options** (in priority order):

1. **Patch/Fix** (preferred):
   - Develop code fix
   - Add regression test (ensure vulnerability doesn't return)
   - Test fix in dev/staging
   - Deploy via standard release process

2. **Workaround** (temporary if patch not immediately available):
   - Disable vulnerable feature
   - Add input validation or filtering
   - Implement rate limiting or monitoring
   - Document workaround with plan for permanent fix

3. **Compensating Control** (if fix infeasible):
   - WAF rule to block exploitation attempts
   - Enhanced monitoring to detect exploitation
   - Access restriction (limit who can reach vulnerable code)
   - Document control with risk acceptance

4. **Accept Risk** (rare, requires CISO approval):
   - Vulnerability impact minimal
   - Remediation cost exceeds risk
   - Compensating controls in place
   - Formal risk acceptance documented

**Remediation SLAs** (from S2.3 Section 2.3.3.3.B):
- Critical: 7 days (14 days if architectural fix required)
- High: 30 days
- Medium: 90 days
- Low: Next major release

**SLA Escalation**:
- 50% of SLA elapsed: Reminder to developer + Development Manager
- 75% of SLA elapsed: Escalate to Application Security Lead
- 100% of SLA elapsed: Escalate to CISO + CTO

#### 3.4.5 Vulnerability Verification

**Verification Process** (after fix deployed):

**Step 1 - Code Review**:
- Security-focused review of fix
- Verify fix addresses root cause (not just symptom)
- Check for similar vulnerabilities in codebase

**Step 2 - Testing**:
- Regression test confirms vulnerability is fixed
- Security test confirms exploitation no longer possible
- Rescan with security tools (SAST, DAST) if applicable

**Step 3 - Deployment Verification**:
- Confirm fix deployed to all affected environments
- Version verification (correct version running in production)
- Functionality testing (fix didn't break legitimate use)

**Step 4 - Closure**:
- Update tracking ticket (status: Verified/Closed)
- Document verification evidence
- Notify stakeholders of closure
- Archive vulnerability details for lessons learned

#### 3.4.6 External Vulnerability Reporting

**Responsible Disclosure** (when vulnerability reported by external researcher):

**Acknowledgment** (within 24 hours):
- Thank researcher for report
- Provide expected response timeline
- Request additional information if needed

**Communication** (during remediation):
- Update researcher on progress (weekly for Critical/High)
- Coordinate disclosure timeline
- Negotiate embargo period if needed (typically 90 days)

**Disclosure** (after fix deployed):
- Coordinate public disclosure with researcher
- Publish security advisory (if warranted)
- Credit researcher (if they desire attribution)
- Update CVE database if assigned CVE ID

**Bug Bounty** (if program exists):
- Assess report per bug bounty rules
- Award bounty per severity and quality
- Process payment per program terms

#### 3.4.7 Critical Vulnerability Emergency Response

**Emergency Response** (for Critical vulnerabilities actively exploited):

**Immediate Actions** (within 1 hour):
1. **Contain**: Block exploitation (WAF rule, network rule, disable feature)
2. **Notify**: CISO, CTO, Incident Response Team
3. **Assess**: Determine if breach occurred (log analysis)
4. **Communicate**: Internal stakeholders, prepare customer communication

**Emergency Fix Process**:
- Fast-track development (bypass standard release process if necessary)
- Security Team + Developer pair to develop fix
- Expedited testing (focus on security, accept some testing shortcuts)
- Emergency deployment (off-hours deployment if needed)

**Post-Emergency**:
- Full testing post-deployment
- Incident report and lessons learned
- Update emergency response procedures if gaps identified

#### 3.4.8 Vulnerability Metrics and Reporting

**Metrics Tracked**:
- Vulnerability count by severity (trend over time)
- Mean time to remediate (MTTR) by severity
- SLA compliance rate (% fixed within SLA)
- Vulnerability age distribution (how long vulnerabilities remain open)
- Repeat vulnerability rate (same issue recurring)

**Reporting**:
- Monthly vulnerability aging report (to Application Security Lead)
- Quarterly vulnerability summary (to CISO, Development Management)
- Critical vulnerabilities immediately reported to CISO
- Annual vulnerability trend analysis (to executive management)

#### 3.4.9 Lessons Learned

**Post-Incident Review** (for Critical/High vulnerabilities):
- Root cause analysis: Why was vulnerability introduced?
- Process gaps: Why wasn't it caught earlier (SAST, code review)?
- Prevention: What process improvements prevent recurrence?
- Policy updates: Does this indicate policy gap?
- Training needs: Developer training needed on this vulnerability class?

**Knowledge Sharing**:
- Share lessons learned with development teams
- Update training materials with real examples
- Add to prohibited practices registry (S2.2)
- Contribute to industry knowledge (anonymized case studies)

#### 3.4.10 Appendix: Vulnerability Report Template

Include template for vulnerability reports (for external researchers):
````markdown
## Vulnerability Report Template

**Reporter Information**:
- Name:
- Email:
- Organization (optional):

**Vulnerability Details**:
- Vulnerability Type (e.g., SQL Injection, XSS):
- Affected Component/URL:
- Severity Assessment (your opinion):

**Steps to Reproduce**:
1. 
2. 
3. 

**Proof of Concept**:
[Code, screenshots, video]

**Impact**:
[What can attacker do?]

**Suggested Fix** (optional):
[Your recommendation]

**Disclosure Preference**:
[ ] Public disclosure after fix
[ ] Private disclosure only
[ ] Credit desired: Yes/No
````

---

### 3.5 ISMS-POL-A.8.28-S5.D (Quick Reference Guide)

**Target Length**: ~300 lines

**Document Control**:
- Review Cycle: Quarterly
- Approvers: Application Security Lead (primary)
- Distribution: All developers (onboarding material)

**Content Structure**:

#### 3.5.1 Introduction
- Purpose: One-page developer security quick reference
- When to use: New projects, daily development, pre-commit checklist
- Not comprehensive: Links to full policy for details

#### 3.5.2 Secure Coding Top 10 Principles

**Quick list format** (1-2 sentences each):

1. **Validate All Input**: Trust nothing from users, databases, APIs, or files
2. **Encode All Output**: HTML-encode, JS-encode, or SQL-parameterize based on context
3. **Parameterize Queries**: Never concatenate strings to build SQL/NoSQL queries
4. **Use Framework Security**: Don't reinvent authentication, use proven libraries
5. **Fail Securely**: Default deny, never fail open, never expose stack traces
6. **Hash Passwords**: bcrypt/Argon2, never MD5/SHA1/plaintext
7. **No Hardcoded Secrets**: Environment variables or secret managers only
8. **Keep Dependencies Updated**: Monitor SCA alerts, patch within SLA
9. **Review Your Code**: Peer review mandatory, use S5.B checklist
10. **Test for Security**: Write security test cases, don't assume it works

#### 3.5.3 Pre-Commit Checklist

**Developer self-check** (before submitting PR):

- [ ] No secrets in code (search for "password", "api_key", "token")
- [ ] Input validation present (all user input validated)
- [ ] Output encoding correct (XSS prevention)
- [ ] SQL queries parameterized (no string concatenation)
- [ ] No vulnerable dependencies (SCA scan green)
- [ ] Code reviewed locally (read your own changes)
- [ ] Tests passing (including security tests)
- [ ] Commit message clear (what and why)

#### 3.5.4 Security Tools Quick Reference

**Tools developers use daily**:

| Tool | Purpose | How to Use | When |
|------|---------|------------|------|
| **SAST** | Find vulnerabilities in code | Runs automatically in CI/CD | Every commit |
| **SCA** | Find vulnerable dependencies | Runs automatically in CI/CD | Every build |
| **Secret Scanner** | Detect committed secrets | Pre-commit hook + CI/CD | Before commit |
| **Linter** | Enforce coding standards | IDE integration | While coding |
| **DAST** | Test running application | Security team runs | Pre-release |

#### 3.5.5 Common Vulnerability Quick Fixes

**Problem → Solution format**:

**SQL Injection**:
- ❌ `query = f"SELECT * FROM users WHERE id = {user_id}"`
- ✅ `cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))`

**XSS**:
- ❌ `<div>{user_input}</div>` (unencoded)
- ✅ `<div>{htmlEncode(user_input)}</div>` (encoded)

**Hardcoded Secret**:
- ❌ `API_KEY = "sk_live_abc123"`
- ✅ `API_KEY = os.environ.get("API_KEY")`

**Weak Password Hash**:
- ❌ `hash = hashlib.md5(password).hexdigest()`
- ✅ `hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())`

#### 3.5.6 When to Escalate

**Escalate to Security Champion**:
- Unsure if code is secure
- Need security design advice
- SAST finding unclear
- Security testing question

**Escalate to Application Security Team**:
- Discovered vulnerability in production
- Complex security architecture question
- Need threat modeling session
- Exception request needed

**Emergency Escalation to CISO**:
- Active exploitation of vulnerability
- Data breach suspected
- Critical vulnerability in production

#### 3.5.7 Key Policy References

**Quick links to frequently-needed sections**:

- **Secure Coding Standards**: ISMS-POL-A.8.28-S2.2
- **Code Review Requirements**: ISMS-POL-A.8.28-S2.3, S5.B (checklist)
- **Dependency Management**: ISMS-POL-A.8.28-S2.4
- **Language-Specific Guides**: ISMS-POL-A.8.28-S5.A
- **Vulnerability Response**: ISMS-POL-A.8.28-S5.C
- **Training Resources**: [Internal training portal link]

#### 3.5.8 Security Resources

**External resources for developers**:
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- CWE Top 25: https://cwe.mitre.org/top25/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/

#### 3.5.9 Secure Development Workflow

**Visual workflow** (can be ASCII art or table):
````
┌─────────────────────────────────────────────────────────┐
│ 1. DESIGN                                               │
│    → Threat model (if high-risk)                        │
│    → Security requirements defined                      │
└─────────────────┬───────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────────────┐
│ 2. CODE                                                 │
│    → Follow secure coding standards (S2.2)              │
│    → Use security linters/IDE plugins                   │
│    → Run tests locally                                  │
└─────────────────┬───────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────────────┐
│ 3. COMMIT                                               │
│    → Pre-commit checks pass (secrets, formatting)       │
│    → Clear commit message                               │
└─────────────────┬───────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────────────┐
│ 4. PULL REQUEST                                         │
│    → Automated checks pass (SAST, SCA, tests)           │
│    → Peer code review with security checklist (S5.B)    │
│    → Security Champion review (if high-risk)            │
└─────────────────┬───────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────────────┐
│ 5. MERGE & DEPLOY                                       │
│    → All approvals obtained                             │
│    → CI/CD security gates pass                          │
│    → Production deployment                              │
└─────────────────────────────────────────────────────────┘
````

#### 3.5.10 Remember

**Key takeaways** (3-4 memorable points):

1. **Security is everyone's job** - not just the security team's responsibility
2. **Shift left** - catch vulnerabilities early (cheapest to fix)
3. **When in doubt, ask** - Security Champions and Security Team are here to help
4. **Learn from mistakes** - every vulnerability is a learning opportunity

---

## 4. CREATION SEQUENCE

**Recommended order**:
1. **S5** (Overview) - Establishes context for other annexes
2. **S5.C** (Vulnerability Response) - Critical operational procedure
3. **S5.B** (Code Review Checklist) - High developer impact
4. **S5.D** (Quick Reference) - Summary of key points
5. **S5.A** (Language Guidelines) - Most detailed, requires language research

**Token Budget Management**:
- S5: ~6K tokens
- S5.C: ~8K tokens
- S5.B: ~8K tokens
- S5.D: ~6K tokens
- S5.A: ~8K tokens
- **Total**: ~36K tokens (comfortably within 190K budget)

---

## 5. QUALITY CHECKS

Before considering section complete:

**Content Quality**:
- [ ] Practical and actionable (not theoretical)
- [ ] Code examples included where applicable
- [ ] Clear cross-references to policy sections
- [ ] Appropriate for target audience skill level

**Format Quality**:
- [ ] Within line limit (300-400 lines)
- [ ] Proper markdown formatting
- [ ] Tables used effectively
- [ ] No excessive repetition from policy sections

**Completeness**:
- [ ] All required sections present
- [ ] Document control properly filled
- [ ] Cross-references accurate
- [ ] External standards cited appropriately

---

## 6. ANTI-PATTERNS TO AVOID

**Don't**:
- ❌ Repeat policy requirements verbatim (annexes supplement, not duplicate)
- ❌ Create language guides for languages organization doesn't use
- ❌ Make checklist so long it's unusable (focus on high-impact items)
- ❌ Create theoretical guidance without practical examples
- ❌ Forget to link back to authoritative policy sections

**Do**:
- ✅ Focus on practical, actionable guidance
- ✅ Use real code examples (correct vs incorrect)
- ✅ Keep language appropriate for developers (not just security team)
- ✅ Make checklists actually usable (not 100-item lists)
- ✅ Link to external standards (OWASP, CERT) rather than reinventing

---

**END OF ANNEX INSTRUCTIONS**