**ISMS-POL-A.8.28 – Secure Coding**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure Coding Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.28 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Technology Officer (CTO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)


**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.28.1-5 (Implementation Assessment Suite)
- ISMS-CTX-A.8.28 (Language-Specific Secure Coding Guidelines)
- ISMS-REF-A.8.28 (Code Review Technical Reference)
- ISO/IEC 27001:2022 Control A.8.28
- ISO/IEC 27002:2022 Control 8.28


---

## Executive Summary

This policy establishes [Organization]'s requirements for secure software development in accordance with ISO/IEC 27001:2022 Control A.8.28 (Secure Coding).

**Purpose**: Define WHAT secure coding controls are required and WHO is accountable. Technical implementation details (HOW) are documented in ISMS-IMP-A.8.28 specifications.

**Scope**: All software development activities including internal development, outsourced development, and acquired software customization. Applies to all application types, development phases, and programming languages.

**Business Risk Addressed**: Software vulnerabilities leading to data breaches, service disruptions, financial losses, reputational damage, and regulatory sanctions.

**Regulatory Alignment**: Per ISMS-POL-00 (Regulatory Applicability Framework):

- **Mandatory**: Swiss FADP, EU GDPR (Art. 32), ISO 27001:2022
- **Informational**: OWASP Top 10, NIST SP 800-218 SSDF, CWE Top 25


---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.28

**Control Statement**:
> *Principles for secure coding shall be applied to software development.*

**Control Objective**: Reduce the number of security vulnerabilities in software by applying secure coding principles throughout the development lifecycle.

**This Control Addresses**:

- Prevention of vulnerabilities during development (shift-left security)
- Common vulnerability prevention (injection, XSS, authentication flaws, etc.)
- Secure design and architecture principles
- Developer training and competency
- Code review and security testing
- Third-party component security


## Scope Definition

**In Scope**:

- All software development (new, maintenance, enhancements, patches)
- All development types (internal, outsourced, contracted, acquired)
- All application types (web, mobile, API, desktop, embedded, serverless)
- All languages and frameworks used by [Organization]
- Development, staging, and production environments


**Out of Scope**:

- Infrastructure configuration (see A.8.9 Configuration Management)
- Network security (see A.8.20-22 Network Security)
- Cryptographic key management (see A.8.24 Cryptography)


## Document Hierarchy

| Document Type | Content | Update Frequency |
|---------------|---------|------------------|
| **This Policy (POL)** | Requirements, governance, accountability | Annual |
| **Implementation (IMP)** | Assessment procedures, workbook specs | Quarterly |
| **Context (CTX)** | Language-specific patterns, technology guidance | Semi-annual |
| **Reference (REF)** | Checklists, technical methods | As needed |

---

# Secure Development Requirements

## Pre-Development Security

**Security Requirements Definition**:

- Security requirements SHALL be defined for all projects handling sensitive data
- Requirements derived from data classification, regulatory needs, and threat landscape
- Security acceptance criteria defined before development begins


**Threat Modeling Requirements**:

| Project Type | Requirement |
|--------------|-------------|
| New applications with sensitive data | Mandatory |
| Major architectural changes | Mandatory |
| Public-facing applications/APIs | Mandatory |
| Financial/PII processing | Mandatory |
| Internal tools (limited exposure) | Recommended |

**Threat Model Documentation**:

- System architecture and data flows
- Trust boundaries and attack surface
- Identified threats with risk ratings
- Mitigation controls mapped to threats
- Validation approach


**Threat Modeling Methodology**: [Organization] SHALL use a recognized methodology (STRIDE, PASTA, DREAD, or OWASP Threat Dragon). Methodology selection documented per application; consistency within application families encouraged.

**Verification**: Threat models reviewed by Application Security Team; approval documented in Workbook 1. Critical applications require CISO sign-off.

**Secure Architecture Review**:

- Required before development sprint 1 for new applications
- Required for significant architectural changes
- Security Architect or Application Security Team approval required
- Critical applications require CISO approval


## Developer Security Training

**Training Requirements**:

| Training Type | Audience | Frequency |
|---------------|----------|-----------|
| Secure coding fundamentals | All developers | Initial + Annual |
| Language-specific security | Developers using language | Initial |
| Security Champions advanced | Security Champions | Quarterly |
| OWASP Top 10 updates | All developers | When updated |

**Training Verification**:

- Completion tracked in enterprise learning management system (e.g., Workday Learning, SAP SuccessFactors, or equivalent)
- Knowledge assessments required with minimum passing score: 85% for secure coding fundamentals and language-specific training; 80% for awareness training (OWASP Top 10 updates). Passing threshold justification: Security-critical competencies require deeper understanding than general awareness.
- Completion certificates retained as evidence
- Non-compliance escalated to Development Manager after 30 days; CISO notification after 60 days


**Training Content Ownership**:

- Application Security Team maintains training content
- Content reviewed and updated annually or when OWASP Top 10/CWE Top 25 updates
- Language-specific training aligned with ISMS-CTX-A.8.28


**Verification**: Training completion reports generated quarterly from LMS; completion rates tracked as KPI (target: 100%). Sample certificates retained for audit.

## Secure Coding Standards

**Universal Requirements** (all languages):

**Input Validation**:

- Validate ALL input (user, API, file, environment, database)
- Whitelist validation preferred over blacklist
- Server-side validation mandatory (client-side is UX only)
- Reject invalid input; do not attempt sanitization


**Output Encoding**:

- Context-appropriate encoding (HTML, JavaScript, URL, SQL)
- Use framework-provided encoding functions
- Prevent XSS through proper output encoding


**Authentication & Session Management**:

- Strong password hashing (bcrypt, Argon2, scrypt)
- Never store plaintext passwords
- Cryptographically random session tokens
- Session timeout and invalidation on logout
- MFA support for sensitive applications


**Authorization**:

- Server-side enforcement for every request
- Least privilege principle
- Prevent IDOR vulnerabilities
- RBAC or ABAC implementation


**Cryptography**:

- Industry-standard algorithms only (AES-256, RSA-2048+)
- Never implement custom cryptography
- Proper key management (keys separate from code)
- TLS 1.2+ for data in transit (TLS 1.3 preferred)


**Error Handling**:

- Generic error messages to users
- Detailed logging server-side (no sensitive data in logs)
- Security events logged for monitoring


**Language-Specific Guidelines**: See ISMS-CTX-A.8.28 for Python, JavaScript, Java, C#, Go, SQL patterns.

## Prohibited Practices

The following are **PROHIBITED**:

- Hardcoded secrets (API keys, passwords, tokens) in source code
- Deprecated/insecure functions (gets(), strcpy(), MD5 for passwords, eval() with user input)
- SQL query construction via string concatenation
- Disabled security controls in production
- Committing secrets to version control (even in history)
- Ignoring security tool findings without documented exception


## Secrets Management

- NO hardcoded secrets in source code
- Secrets stored in approved secret management systems (e.g., HashiCorp Vault, AWS Secrets Manager, Azure Key Vault)
- Secret scanning integrated into CI/CD pipeline (e.g., GitLeaks, TruffleHog, GitHub Secret Scanning)
- Pre-commit hooks configured to block commits containing detected secrets
- Secrets rotated regularly and upon employee departure


**Secret Detection Response**:

- Pre-commit block: Developer must remove secret before commit proceeds
- CI/CD detection: Build fails; secret must be removed and rotated before merge
- Post-commit detection: Immediate rotation required; incident logged


**Verification**: Secret scanning tool configuration documented in Workbook 2; detection events logged and reviewed weekly by Application Security Team.

## Third-Party & Open Source Components

**Component Selection**:

- Evaluate security posture before adoption
- Prefer well-maintained, widely-used libraries
- Check for known vulnerabilities before inclusion
- Verify license compatibility


**Ongoing Management**:

- Maintain component inventory (Software Bill of Materials)
- Monitor for vulnerabilities via SCA tools
- Patch/update within defined SLAs
- Remove unused dependencies


---

# Code Review & Security Testing

## Code Review Requirements

**Peer Review**:

- All production code changes require peer review
- Security-focused review for changes touching authentication, authorization, cryptography, input handling
- Branch protection prevents merging without approval


**Security Review Criteria**: See ISMS-REF-A.8.28 for detailed checklist.

## Security Testing Requirements

**Static Application Security Testing (SAST)**:

- Integrated into CI/CD pipeline (e.g., SonarQube, Checkmarx, Snyk Code, Semgrep)
- Run on every build/commit; build fails on Critical/High findings
- Findings triaged and remediated per SLA
- False positives documented and tuned (target: <20% false positive rate)


**Dynamic Application Security Testing (DAST)**:

- Run against staging/QA environments (e.g., OWASP ZAP, Burp Suite, Qualys WAS)
- Required before production release for web applications
- API security testing for all APIs (e.g., Postman security tests, OWASP API Security)


**Software Composition Analysis (SCA)**:

- Integrated into CI/CD pipeline (e.g., Snyk, Dependabot, OWASP Dependency-Check)
- Monitors all third-party dependencies
- Alerts on new vulnerabilities in dependencies; build fails on Critical/High


**Tool Integration Verification**:

- CI/CD pipeline configuration documented in Workbook 2
- Tool selection and deployment status tracked
- Last 90 days scan reports available on request
- Pipeline logs demonstrate automated execution


**Verification**: Security tool dashboard (or consolidated report) reviewed weekly; tool coverage and scan success rates tracked as KPIs.

**Penetration Testing**:

| Application Type | Frequency | Scope |
|------------------|-----------|-------|
| Critical/High-risk | Annual minimum | Full application (all OWASP Top 10 categories) |
| Internet-facing | Annual minimum | External attack surface (authentication, APIs, input handling) |
| After major changes | As needed | Changed components + integration points |

**Scoping Criteria**:

- Critical applications: Include authentication bypass, privilege escalation, data exfiltration scenarios
- API testing: Include all public endpoints, authentication mechanisms, rate limiting
- Post-test: Findings remediated per SLA; retest for Critical/High findings


**Retest Requirements**:

- Critical and High findings SHALL be retested after remediation to verify effectiveness
- Retest may be scoped to affected components (not requiring full application retest)
- Medium and Low findings verified through internal security testing (DAST or manual testing) unless customer or regulatory requirement mandates external retest
- Retest evidence documented in Workbook 3


**Verification**: Penetration test reports retained per Section 7.3; remediation evidence documented in Workbook 3.

## Vulnerability Remediation SLAs

| Severity | CVSS Score | Remediation SLA |
|----------|------------|-----------------|
| **Critical** | 9.0-10.0 | 7 days |
| **High** | 7.0-8.9 | 30 days |
| **Medium** | 4.0-6.9 | 90 days |
| **Low** | 0.1-3.9 | Best effort / next release |

**SLA Tracking Mechanism**:

- Vulnerabilities tracked in issue tracking system (e.g., Jira, Azure DevOps) with severity and discovery date
- Aging calculated automatically; overdue items flagged
- Weekly SLA compliance review by Application Security Team
- Monthly SLA report to Development Management and CISO


**Exception Process**:

- Documented business justification required
- Risk assessment and compensating controls (e.g., WAF rule, network isolation, enhanced monitoring)
- Approval: Medium by Security Lead, High/Critical by CISO
- Maximum exception duration: 90 days (renewable)
- Exceptions tracked in central exception register (Workbook 3)


**Verification**: Vulnerability aging dashboard reviewed weekly; SLA compliance rates tracked as KPI (Critical ≥95%, High ≥90%).

---

# Roles and Responsibilities

## Executive Management

- Approve secure coding policy
- Allocate budget for security tools and training
- Review security metrics quarterly
- Escalation point for critical vulnerabilities


## Chief Information Security Officer (CISO)

- Overall accountability for secure development program
- Approve security tool selection
- Approve high-risk exceptions
- Review vulnerability trends and remediation status


## Application Security Team

- Maintain secure coding standards
- Perform threat model reviews
- Manage security testing tools (SAST, DAST, SCA)
- Triage and track vulnerabilities
- Conduct security training
- Support incident response for code vulnerabilities


## Development Management

- Ensure developers complete security training
- Allocate time for security activities in sprints
- Enforce code review requirements
- Escalate unresolved security findings


## Security Champions

- Embedded security advocates within development teams
- First point of contact for security questions
- Participate in threat modeling
- Promote secure coding practices


**Program Structure**:

- Coverage target: Minimum 1 Security Champion per development team (or per 10 developers)
- Selection: Nominated by Development Manager, approved by Application Security Team
- Designation: Formal role documented in HR system; 10-20% time allocation for security activities
- Training: Quarterly advanced security training (beyond standard developer training)
- Recognition: Security Champion contributions included in performance reviews


**Verification**: Security Champions roster maintained by Application Security Team; coverage tracked in Workbook 1.

## Developers

- Complete required security training
- Follow secure coding standards
- Address security findings in their code
- Participate in code reviews
- Report security concerns
- Not commit secrets to repositories


## Third-Party Developers

- Comply with [Organization]'s secure coding standards
- Complete security training as required
- Submit to code reviews and security testing
- Remediate vulnerabilities within SLAs


**Compliance Enforcement**:

- Contractual obligation: Secure coding requirements included in vendor agreements (per A.5.20)
- Onboarding: Third-party developers complete secure coding training before access granted
- Code review: All third-party code subject to same review standards as internal code
- Security testing: Third-party deliverables scanned with SAST/SCA before acceptance
- Attestation: Annual compliance attestation signed by vendor management


**Verification**: Third-party developer compliance tracked in Workbook 4; attestations retained for audit.

---

# Governance and Compliance

## Policy Compliance Monitoring

**Continuous Monitoring**:

- SAST/DAST/SCA results tracked in security dashboard
- Vulnerability aging monitored
- Training completion tracked


**Periodic Assessment**:

- Quarterly: Vulnerability metrics, training compliance, exception review
- Annual: Full secure coding program assessment (ISMS-IMP-A.8.28)


## Non-Compliance Handling

**Progressive Response**:
1. First occurrence: Training and documented warning
2. Repeat occurrence: Manager escalation
3. Continued non-compliance: Development privileges restricted
4. Willful violation: Disciplinary action per HR policies

## Exception Management

- All exceptions require documented business justification
- Risk assessment and compensating controls mandatory
- Approval authority based on risk level
- Exceptions tracked in central exception register (Workbook 3)
- Maximum duration: 90 days (renewable with re-approval)


**Compensating Controls Guidance**:

- WAF rules blocking known attack patterns for unpatched vulnerabilities
- Network segmentation limiting exposure of vulnerable components
- Enhanced monitoring/alerting for exploitation attempts
- Rate limiting reducing attack feasibility
- Input validation at network edge (reverse proxy)


**Compensating Controls Adequacy Criteria**: Compensating controls SHALL demonstrate equivalent risk reduction via:

- **Effectiveness**: Control mitigates the specific exploitation path (not generic security)
- **Reliability**: Control operates continuously with alerting on failure
- **Verifiability**: Control operation can be tested and monitored
- **Scope**: Control covers all affected systems/data flows


Application Security Team assesses adequacy; CISO approval for High/Critical exceptions includes compensating control validation.

**Verification**: Exception register reviewed quarterly; expired exceptions escalated for closure or renewal.

## Metrics and Reporting

**Key Performance Indicators**:

| Metric | Target | Frequency | Data Source |
|--------|--------|-----------|-------------|
| Developer training completion | 100% | Quarterly | LMS completion reports |
| Code review coverage | ≥95% | Monthly | Git/PR merge statistics |
| Critical vulnerabilities within SLA | ≥95% | Monthly | Vulnerability tracker aging report |
| High vulnerabilities within SLA | ≥90% | Monthly | Vulnerability tracker aging report |
| Threat model coverage (high-risk apps) | ≥90% | Quarterly | Workbook 1 application inventory |

**Metrics Dashboard**: Security metrics consolidated in dashboard (Workbook 5) or security operations platform; reviewed monthly by CISO.

---

# Integration with Other Controls

## Related ISMS Controls

| Control | Integration |
|---------|-------------|
| **A.5.7 Threat Intelligence** | Informs secure coding priorities |
| **A.5.24-28 Incident Management** | Code vulnerabilities trigger incident response |
| **A.8.2-3-5 Authentication & Access** | Secure coding implements auth/authz logic |
| **A.8.9 Configuration Management** | Secure configuration in code |
| **A.8.15-16 Logging & Monitoring** | Secure logging implementation |
| **A.8.24 Cryptography** | Cryptographic implementation in code |
| **A.8.25-27 Secure Development** | Complementary SDLC controls |
| **A.8.29 Security Testing** | Testing requirements align |
| **A.8.30 Outsourced Development** | Third-party requirements |
| **A.8.32 Change Management** | Security gates in deployment |

## Regulatory Mapping

| Requirement | Swiss FADP | EU GDPR | ISO 27001 |
|-------------|-----------|---------|-----------|
| Secure development | Art. 8 | Art. 32 | A.8.28 |
| Security testing | Art. 8 | Art. 32 | A.8.29 |
| Vulnerability management | Art. 8 | Art. 32 | A.8.8 |

---

# Evidence Requirements

## Audit Evidence

**For ISO 27001:2022 certification audits, [Organization] SHALL maintain**:

- Secure coding standards documentation
- Developer training records and completion rates
- Threat model examples for high-risk applications
- Code review records (PR approvals, comments)
- SAST/DAST/SCA scan reports and trend data
- Vulnerability remediation evidence
- Penetration test reports
- Exception register with approvals
- Third-party developer compliance attestations


## Assessment Workbooks

Compliance assessed using standardized workbooks:

- ISMS-IMP-A.8.28.1: SDLC Assessment
- ISMS-IMP-A.8.28.2: Standards & Tools Assessment
- ISMS-IMP-A.8.28.3: Code Review & Testing Assessment
- ISMS-IMP-A.8.28.4: Third-Party & OSS Assessment
- ISMS-IMP-A.8.28.5: Compliance Dashboard


**Note**: Workbook specifications and assessment procedures documented in ISMS-IMP-A.8.28 suite.

## Evidence Retention

- Training records: Duration of employment + 2 years
- Code review records: Application lifecycle + 2 years
- Security scan results: 3 years
- Penetration test reports: 5 years
- Vulnerability remediation evidence: 3 years


---

# Implementation Resources

## Supporting Documentation

| Document | Purpose |
|----------|---------|
| **ISMS-IMP-A.8.28.1-5** | Assessment specifications and workbooks |
| **ISMS-CTX-A.8.28** | Language-specific guidelines (Python, Java, JS, C#, Go, SQL) |
| **ISMS-REF-A.8.28** | Code review checklists and technical reference |

## External References

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
- CWE Top 25: https://cwe.mitre.org/top25/
- NIST SP 800-218 SSDF: Secure Software Development Framework


---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Technology Officer (CTO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for secure software development. Implementation procedures, assessment methodologies, and workbook specifications are documented in ISMS-IMP-A.8.28. Language-specific guidelines are in ISMS-CTX-A.8.28. Code review checklists are in ISMS-REF-A.8.28.*

<!-- QA_VERIFIED: 2026-02-01 -->
