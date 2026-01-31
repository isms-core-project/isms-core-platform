# ISMS-POL-A.8.28-S2.3
## Secure Coding - Code Review & Testing Requirements

**Document ID**: ISMS-POL-A.8.28-S2.3
**Title**: Secure Coding - Code Review & Testing Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead / QA Manager | Initial code review and testing requirements |

**Review Cycle**: Annual (or upon changes to testing tools or methodologies)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead
- Process Owner: QA Manager / Testing Lead
- Stakeholder Review: Development Manager

**Distribution**: Developers, QA engineers, security team, code reviewers, DevOps  
**Related Documents**: ISMS-POL-A.8.28-S2.2 (Secure Coding Standards), ISMS-POL-A.8.28-S5.B (Code Review Checklist), ISMS-IMP-A.8.28.3 (Code Review & Testing Assessment)

---

## 2.3.1 Introduction

This section establishes requirements for **security verification activities** throughout the development lifecycle. Testing and code review serve as critical defenses, detecting vulnerabilities before they reach production.

*"Program testing can be used to show the presence of bugs, but never to show their absence!"* - Edsger Dijkstra

**Translation for Security**: No amount of testing guarantees absence of vulnerabilities. However, systematic, multilayered security testing (peer review + SAST + DAST + penetration testing) dramatically reduces the probability of shipping exploitable vulnerabilities.

**Testing Philosophy - Defense in Depth**:
- **Peer Code Review**: Human intelligence, context awareness, logic flaws
- **SAST (Static Analysis)**: Comprehensive code coverage, known vulnerability patterns
- **DAST (Dynamic Analysis)**: Runtime behavior, integration issues
- **IAST (Interactive Analysis)**: Hybrid approach, runtime context with code-level detail
- **Penetration Testing**: Real-world attack simulation, creative exploitation

**Primary Stakeholders**: Developers, QA Engineers, Security Team, Security Champions

---

## 2.3.2 Peer Code Review

### 2.3.2.1 Mandatory Code Review Requirements

**REQ-2.3.2.1-A: All Code Must Be Reviewed**

All code changes **MUST** undergo peer review before merging to protected branches:
- **Production code**: Mandatory review with security focus
- **Test code**: Review for test quality and security test coverage
- **Infrastructure-as-Code**: Review for security misconfigurations
- **Configuration changes**: Review for security implications
- **Documentation updates**: Review when affecting security guidance

**Exceptions** (review optional but recommended):
- Personal experiments in individual developer branches
- Proof-of-concept code not intended for production

**REQ-2.3.2.1-B: Review Approval Requirements**

Code review approval requirements based on risk:

| Risk Level | Approval Requirements | Examples |
|------------|----------------------|----------|
| **Critical** | 2+ reviewers, including Security Team | Authentication, cryptography, payment processing |
| **High** | 1+ reviewer with security training, Security Champion review | Authorization, input validation, data access |
| **Medium** | 1+ peer reviewer | Business logic, API endpoints, database queries |
| **Low** | 1+ peer reviewer (may be automated for trivial changes) | UI changes, documentation, refactoring |

**REQ-2.3.2.1-C: Reviewer Qualifications**

Code reviewers **MUST**:
- Have completed secure coding training
- Be familiar with secure coding standards (ISMS-POL-A.8.28-S2.2)
- Have completed at least 10 code reviews (shadowing senior reviewers for first 5)

Security-focused reviewers **MUST** additionally:
- Be designated Security Champions OR
- Have completed advanced application security training OR
- Be members of Application Security Team

### 2.3.2.2 Code Review Process

**REQ-2.3.2.2-A: Pull Request (PR) / Merge Request (MR) Workflow**

Standard code review workflow:

1. **Developer submits PR/MR**:
   - Clear description of changes and rationale
   - Reference to user story, ticket, or issue
   - Self-review checklist completed
   - Automated checks passed (build, unit tests, linters)

2. **Automated Pre-Review**:
   - SAST scan executes automatically
   - Unit tests and security tests run
   - Code coverage analysis
   - Dependency vulnerability scan (SCA)

3. **Peer Review**:
   - Reviewer examines code for functionality, security, maintainability
   - Security checklist applied (ISMS-POL-A.8.28-S5.B)
   - Comments and change requests documented
   - Approval or request for changes

4. **Developer addresses feedback**:
   - Implements requested changes
   - Responds to reviewer comments
   - Re-submits for review

5. **Merge approval**:
   - All reviewers approve
   - All automated checks pass
   - Code merged to target branch

**REQ-2.3.2.2-B: Security-Focused Review Criteria**

Reviewers **MUST** verify:

| Category | Review Focus | Reference |
|----------|-------------|-----------|
| **Input Validation** | All external input validated, whitelist approach used | S2.2, Section 2.2.3 |
| **Output Encoding** | User data properly encoded for context (HTML, JS, SQL) | S2.2, Section 2.2.4 |
| **Authentication** | Proper authentication checks, session management | S2.2, Section 2.2.5 |
| **Authorization** | Authorization enforced server-side, IDOR prevention | S2.2, Section 2.2.6 |
| **Cryptography** | Approved algorithms, secure key management, secure RNG | S2.2, Section 2.2.7 |
| **Error Handling** | No information disclosure in errors, proper logging | S2.2, Section 2.2.8 |
| **Secrets Management** | No hardcoded credentials, proper secret storage | S2.1, Section 2.1.6.2 |
| **Dependencies** | No new vulnerable dependencies introduced | S2.4 |

**REQ-2.3.2.2-C: Review Documentation**

Code reviews **MUST** be documented:
- Review comments preserved in version control system
- Security findings tagged appropriately
- Approval decisions recorded with timestamps
- Deviations from standards documented with justification

### 2.3.2.3 Security-Focused Code Review

**REQ-2.3.2.3-A: Dedicated Security Review for High-Risk Changes**

Changes requiring dedicated security review (beyond peer review):
- New authentication or authorization mechanisms
- Cryptographic implementations
- Payment processing or financial transactions
- New APIs exposing sensitive data
- Privilege escalation functionality
- Security control implementations

Dedicated security review includes:
- Application Security Team involvement
- Use of comprehensive security checklist (ISMS-POL-A.8.28-S5.B)
- Threat model review and update
- Additional testing requirements identification

**REQ-2.3.2.3-B: Pair Programming as Alternative**

Organizations **MAY** use pair programming or mob programming as alternative/supplement to traditional code review:
- Security Champion participates in pairing session
- Security considerations discussed during development
- Code still undergoes SAST and automated security checks
- Pairing session documented (participants, duration, focus areas)

---

## 2.3.3 Static Application Security Testing (SAST)

### 2.3.3.1 SAST Tool Requirements

**REQ-2.3.3.1-A: SAST Tool Deployment**

Organizations **MUST** deploy SAST tooling that:
- Supports all programming languages used by the organization
- Integrates with CI/CD pipeline for automated scanning
- Detects OWASP Top 10 and CWE Top 25 vulnerability patterns
- Provides actionable remediation guidance
- Supports custom rule development or configuration

**REQ-2.3.3.1-B: SAST Scan Frequency**

SAST scans **MUST** execute:
- **On every commit/PR**: Fast scan (critical/high severity rules only) - Results within 5-10 minutes
- **Daily**: Full scan of main/production branch - Comprehensive ruleset
- **On-demand**: Developers can trigger full scan for their branches

**REQ-2.3.3.1-C: SAST Coverage Requirements**

SAST tooling **MUST** scan:
- Application source code (all languages)
- Infrastructure-as-Code (Terraform, CloudFormation, Kubernetes manifests)
- Configuration files (security-relevant configurations)
- Dependency manifests (package.json, requirements.txt, pom.xml)

### 2.3.3.2 SAST Configuration and Tuning

**REQ-2.3.3.2-A: Baseline Ruleset**

SAST tools **MUST** be configured to detect:
- **OWASP Top 10 vulnerabilities** (injection, XSS, broken authentication, etc.)
- **CWE Top 25** software weaknesses
- **Language-specific vulnerabilities** (deserialization, XXE for Java; prototype pollution for JavaScript, etc.)
- **Hardcoded secrets** (credentials, API keys, tokens)
- **Insecure cryptography** (weak algorithms, hardcoded keys)

**REQ-2.3.3.2-B: False Positive Management**

SAST false positives **SHOULD** be managed systematically:
- Investigate each finding to confirm false positive status
- Document justification for false positive classification
- Suppress finding in tool with documented reason (not in code)
- Review suppressed findings quarterly to validate continued appropriateness

❌ **PROHIBITED**: Blanket suppression of vulnerability classes without individual review

**REQ-2.3.3.2-C: Custom Rules**

Organizations **SHOULD** develop custom SAST rules for:
- Organization-specific security patterns and anti-patterns
- Framework-specific vulnerabilities (custom framework security)
- Historical vulnerability patterns found in incidents
- Compliance-specific requirements (e.g., GDPR data handling)

### 2.3.3.3 SAST Findings Management

**REQ-2.3.3.3-A: Vulnerability Severity Classification**

SAST findings **MUST** be classified by severity:
- **Critical (CVSS 9.0-10.0)**: Code execution, authentication bypass, privilege escalation
- **High (CVSS 7.0-8.9)**: SQL injection, XSS, insecure deserialization, sensitive data exposure
- **Medium (CVSS 4.0-6.9)**: Authorization issues, CSRF, information disclosure
- **Low (CVSS 0.1-3.9)**: Security misconfigurations, missing security headers

**REQ-2.3.3.3-B: SAST Remediation SLAs**

Vulnerabilities discovered by SAST **MUST** be remediated per defined SLAs:

| Severity | Remediation SLA | Blocking Deployment? |
|----------|----------------|---------------------|
| **Critical** | 7 calendar days | ✅ YES - Blocks production deployment |
| **High** | 30 calendar days | ✅ YES - Blocks production deployment |
| **Medium** | 90 calendar days | ⚠️ Risk acceptance required for deployment |
| **Low** | Next major release | ❌ NO - Does not block deployment |

**SLA Exceptions**: Risk acceptance required, documented justification, CISO or Application Security Lead approval.

---

## 2.3.4 Dynamic Application Security Testing (DAST)

### 2.3.4.1 DAST Tool Requirements

**REQ-2.3.4.1-A: DAST Tool Deployment**

Organizations **MUST** deploy DAST tooling for web applications and APIs that:
- Simulates real-world attacks (injection, XSS, authentication testing)
- Tests running applications (integration/staging environment)
- Supports authentication and session management testing
- Covers modern frameworks (SPAs, RESTful APIs, GraphQL)

**REQ-2.3.4.1-B: DAST Scan Frequency**

DAST scans **MUST** execute:
- **Pre-production**: Full scan before production deployment (staging/pre-prod environment)
- **Weekly**: Automated scans of staging environment
- **After significant changes**: Authentication, authorization, or API changes

**REQ-2.3.4.1-C: DAST Scope**

DAST scans **MUST** cover:
- All public-facing web applications
- Internal web applications processing sensitive data
- RESTful APIs and GraphQL endpoints
- Authentication and session management flows

### 2.3.4.2 DAST Configuration

**REQ-2.3.4.2-A: Authenticated Scanning**

DAST tools **SHOULD** be configured for authenticated scanning:
- Test both authenticated and unauthenticated attack surfaces
- Use test accounts with various privilege levels (admin, user, guest)
- Cover authorization bypass scenarios

**REQ-2.3.4.2-B: DAST Test Environment**

DAST scans **MUST** execute in:
- **Staging/pre-production environments** (production-like configuration)
- **NOT production** (except for passive scans with approval)

Test environments **MUST**:
- Mirror production configuration
- Use test data (no production PII)
- Have appropriate access controls

### 2.3.4.3 DAST Findings Management

**REQ-2.3.4.3-A: DAST Remediation SLAs**

DAST vulnerabilities follow same SLAs as SAST (Section 2.3.3.3.B).

**REQ-2.3.4.3-B: DAST vs SAST Finding Correlation**

Organizations **SHOULD**:
- Correlate DAST findings with SAST findings (same vulnerability detected by both?)
- Prioritize findings confirmed by multiple tools
- Investigate DAST findings not detected by SAST (SAST blind spots)

---

## 2.3.5 Interactive Application Security Testing (IAST)

### 2.3.5.1 IAST Implementation (Optional)

**REQ-2.3.5.1-A: IAST as Supplement**

Organizations **MAY** deploy IAST tooling as supplement to SAST/DAST:
- IAST instruments application with runtime agents
- Provides code-level detail for runtime-detected vulnerabilities
- Reduces false positives (confirms exploitability)
- Integrates with functional testing (security testing during QA)

**REQ-2.3.5.1-B: IAST Deployment Scope**

If deployed, IAST **SHOULD** be used in:
- Development and QA environments
- During automated integration testing
- For applications with complex business logic

---

## 2.3.6 Software Composition Analysis (SCA)

**Note**: Third-party dependency scanning (SCA) is covered in detail in **ISMS-POL-A.8.28-S2.4** (Third-Party & OSS Management).

For code review and testing purposes, SCA **MUST**:
- Execute automatically on every build
- Block builds with Critical/High severity dependency vulnerabilities
- Be integrated with code review process (flagged in PRs)

---

## 2.3.7 Security Unit Testing

### 2.3.7.1 Security Test Cases

**REQ-2.3.7.1-A: Security Test Development**

Developers **SHOULD** write security-focused unit tests for:
- Input validation logic (test with malicious input)
- Authentication and authorization checks
- Cryptographic operations (key generation, encryption/decryption)
- Error handling (verify no information disclosure)

**REQ-2.3.7.1-B: Security Test Examples**

✅ **Example - Input Validation Test**:
```python
def test_sql_injection_prevention():
    """Verify SQL injection is prevented"""
    malicious_input = "'; DROP TABLE users; --"
    result = search_users(malicious_input)
    
    # Should return empty results, not execute SQL injection
    assert len(result) == 0
    assert user_table_still_exists()  # Verify table not dropped
```

✅ **Example - Authorization Test**:
```python
def test_unauthorized_access_blocked():
    """Verify users cannot access others' data"""
    user1_token = authenticate(user1)
    
    # Attempt to access user2's account with user1's token
    response = get_account(user2_account_id, token=user1_token)
    
    # Should return 403 Forbidden
    assert response.status_code == 403
```

### 2.3.7.2 Test Coverage

**REQ-2.3.7.2-A: Security Test Coverage Targets**

Organizations **SHOULD** target:
- **Overall code coverage**: ≥80% (includes security tests)
- **Security-critical code coverage**: ≥95% (authentication, authorization, cryptography)

---

## 2.3.8 Penetration Testing

### 2.3.8.1 Penetration Testing Requirements

**REQ-2.3.8.1-A: Penetration Testing Frequency**

Penetration testing **MUST** be performed:

| Application Risk Level | Penetration Test Frequency | Scope |
|----------------------|---------------------------|-------|
| **Critical** (Public, processes PII/financial data) | Annually + after major changes | Full scope (black box + gray box) |
| **High** (Internal, sensitive data) | Annually | Focused scope (critical functions) |
| **Medium** (Internal, limited sensitive data) | Every 2 years | Risk-based scope |
| **Low** (Internal, no sensitive data) | Optional | As needed |

**Major Changes** triggering penetration test:
- New authentication/authorization mechanisms
- Major architectural changes
- New API endpoints exposing sensitive data
- Significant security control modifications

**REQ-2.3.8.1-B: Penetration Testing Scope**

Penetration tests **MUST** include:
- **OWASP Top 10 testing**: All categories
- **Business logic testing**: Application-specific logic flaws
- **Authentication/Authorization testing**: Privilege escalation, session hijacking
- **API security testing**: RESTful API, GraphQL security
- **Configuration testing**: Security misconfigurations

**REQ-2.3.8.1-C: Penetration Tester Qualifications**

Penetration testers **MUST**:
- Be independent from development team (internal Security Team OR external firm)
- Hold recognized certifications (OSCP, GWAPT, CEH, or equivalent)
- Have demonstrable experience with similar applications/technologies
- Sign NDA and adhere to responsible disclosure

### 2.3.8.2 Penetration Testing Process

**REQ-2.3.8.2-A: Pre-Test Preparation**

Before penetration testing:
1. Define scope and rules of engagement
2. Identify critical functionality and sensitive data
3. Provide test accounts with various privilege levels
4. Establish communication channels (emergency contact)
5. Obtain necessary approvals and sign agreements

**REQ-2.3.8.2-B: Post-Test Remediation**

After penetration testing:
1. Receive detailed report with findings and evidence
2. Classify findings by severity (CVSS scoring)
3. Assign findings to development teams for remediation
4. Track remediation progress
5. Verify fixes (retest or proof-of-remediation)
6. Obtain closure sign-off from Security Team

**REQ-2.3.8.2-C: Penetration Test Remediation SLAs**

Findings from penetration tests follow same SLAs as SAST/DAST (Section 2.3.3.3.B), with exception:
- **Critical findings**: 14 days (extended from 7 days to allow for architectural fixes)

---

## 2.3.9 Security Regression Testing

### 2.3.9.1 Regression Testing Requirements

**REQ-2.3.9.1-A: Automated Security Regression Tests**

Organizations **MUST** implement automated security regression testing:
- Fixed vulnerabilities added to regression test suite
- Regression tests execute on every build
- Tests verify vulnerability does not recur

**REQ-2.3.9.1-B: Regression Test Examples**

For each fixed vulnerability:
1. Create test case reproducing original vulnerability
2. Verify test fails before fix is applied
3. Verify test passes after fix is applied
4. Add test to automated regression suite
5. Document test in vulnerability tracking system

---

## 2.3.10 Security Testing in CI/CD Pipeline

### 2.3.10.1 CI/CD Security Gates

**REQ-2.3.10.1-A: Automated Security Gates**

CI/CD pipelines **MUST** include security gates:

| Pipeline Stage | Security Check | Failure Action |
|---------------|----------------|---------------|
| **Commit** | SAST (fast scan), Secret scanning | ⚠️ Warning, does not block |
| **Pull Request** | SAST (full scan), SCA, Unit tests | ❌ Blocks merge if Critical/High found |
| **Integration** | Integration tests with security tests | ❌ Blocks promotion to staging |
| **Staging Deployment** | DAST scan | ❌ Blocks promotion to production |
| **Production Deployment** | Final security checklist verification | ❌ Blocks deployment if checklist incomplete |

**REQ-2.3.10.1-B: Manual Override**

Security gate overrides **REQUIRE**:
- Documented justification
- Risk acceptance from CISO or delegate
- Remediation plan with timeline
- Tracking in exception register

---

## 2.3.11 Vulnerability Remediation and Tracking

### 2.3.11.1 Vulnerability Tracking

**REQ-2.3.11.1-A: Centralized Vulnerability Management**

Organizations **MUST** maintain centralized vulnerability tracking:
- All findings from SAST, DAST, SCA, penetration testing
- Vulnerability status (open, in-progress, fixed, risk-accepted)
- Assigned owner and remediation deadline
- Retest status and verification

**REQ-2.3.11.1-B: Vulnerability Aging Reports**

Organizations **MUST** generate monthly vulnerability aging reports:
- Count of open vulnerabilities by severity
- Vulnerabilities exceeding SLA by severity
- Trend analysis (improving or worsening?)
- Remediation velocity (average time to fix)

### 2.3.11.2 Remediation Verification

**REQ-2.3.11.2-A: Fix Verification**

Vulnerability fixes **MUST** be verified:
- Developer self-verifies fix before marking as complete
- Security Champion or Security Team verifies fix
- Automated regression test confirms vulnerability is gone
- Retest with original tool (SAST, DAST) confirms remediation

**REQ-2.3.11.2-B: Root Cause Analysis for Critical Findings**

Critical vulnerabilities **SHOULD** trigger root cause analysis:
- Why was vulnerability introduced?
- Why didn't existing controls detect it earlier?
- What process improvement would prevent recurrence?
- Lessons learned shared with development teams

---

## 2.3.12 Compliance and Evidence

### 2.3.12.1 Testing Evidence Requirements

Compliance with code review and testing requirements is assessed in:
- **ISMS-IMP-A.8.28.3**: Code Review & Testing Assessment

Evidence includes:
- Code review records (PR/MR histories with approvals)
- SAST/DAST/SCA scan reports (recent scans with findings)
- Penetration test reports (annual tests with remediation tracking)
- Vulnerability tracking reports (aging reports, remediation metrics)
- Regression test results (automated security test execution logs)
- Security gate enforcement (CI/CD pipeline configurations and logs)

### 2.3.12.2 Metrics and KPIs

Organizations **SHOULD** track:
- **Code review coverage**: % of commits with peer review
- **SAST coverage**: % of codebase scanned, % of builds with SAST
- **DAST coverage**: # of applications scanned, scan frequency
- **Vulnerability density**: Vulnerabilities per 1000 lines of code
- **Mean time to remediate (MTTR)**: Average days to fix by severity
- **SLA compliance**: % of vulnerabilities fixed within SLA
- **Shift-left effectiveness**: % vulnerabilities found in dev vs. prod

---

**END OF DOCUMENT**

*"Testing shows the presence, not the absence of bugs." - Edsger Dijkstra*

**Application to Security**: Perfect security is impossible. Our goal is systematic risk reduction through layered testing, continuous improvement, and rapid remediation of discovered vulnerabilities.