<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.25-26-29:operational:OP-POL:a.8.25-26-29 -->
**ISMS-OP-POL-A.8.25-26-29 — Secure Development Lifecycle**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure Development Lifecycle |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.25-26-29 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.25 — Secure development lifecycle
- ISO/IEC 27001:2022 Control A.8.26 — Application security requirements
- ISO/IEC 27001:2022 Control A.8.29 — Security testing in development and acceptance
- OWASP Application Security Verification Standard (ASVS) 4.0
- OWASP Top 10:2025
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1

**Related Annex A Controls**:

| Control | Relationship to Secure Development |
|---------|-------------------------------------|
| A.5.8 Information security in project management | Security requirements integrated into project lifecycle |
| A.5.15–16–18 Identity and access management | Access control for repositories, environments, and deployment tools |
| A.8.4 Access to source code | Source code access restriction and protection |
| A.8.8 Management of technical vulnerabilities | Vulnerability remediation for deployed applications |
| A.8.28 Secure coding | Secure coding standards and practices |
| A.8.31 Separation of development, test, and production environments | Environment segregation requirements |
| A.8.32 Change management | Change control for code promotion and deployment |
| A.8.33 Test information | Protection of test data |

**Related Internal Policies**:

- Access Control Policy
- Vulnerability Management Policy
- Change Management Policy
- Information Classification and Handling Policy
- Endpoint Security Policy

---

# Secure Development Lifecycle Policy

## Purpose

The purpose of this policy is to ensure information security is designed and implemented within the development lifecycle of software and systems, that security requirements are identified and specified when developing or acquiring applications, and that security testing is defined and performed before deployment to production.

This policy supports Swiss nFADP (revDSG) by implementing technical and organisational measures appropriate to risk to protect personal data, in accordance with Art. 7 (data protection by design and by default) and Art. 8 (technical and organisational security measures). Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply (Art. 25 — data protection by design and by default; Art. 32 — security of processing).

## Scope

System development of bespoke organisation software solutions, including web applications, APIs, mobile applications, and infrastructure-as-code.

All internally developed and outsourced development activities deemed in scope by the ISO 27001 scope statement.

All employees and third-party users involved in software development, testing, and deployment.

## Principle

Secure software and system engineering principles and standards are implemented and tested throughout the software development lifecycle.

Information security and privacy are by design and by default, in accordance with NIST SP 800-218 (SSDF) practice groups: Prepare the Organisation (PO), Protect the Software (PS), Produce Well-Secured Software (PW), and Respond to Vulnerabilities (RV).

Security controls are applied proportionally to application risk, with higher-risk applications subject to more rigorous requirements.

---

## Development Security Toolchain

The organisation shall maintain an approved security toolchain integrated into the development lifecycle.

**Approved Security Toolchain**:

| Category | Purpose | Owner | Integration Point |
|----------|---------|-------|-------------------|
| **Source code repository** | Version control, branch protection, access control | DevOps / Platform Team | Development phase |
| **SAST** (Static Application Security Testing) | Source code vulnerability detection (e.g., SonarQube, Semgrep, Checkmarx, or equivalent) | DevOps / Development Manager | CI/CD pipeline — build stage |
| **SCA** (Software Composition Analysis) | Open-source dependency vulnerability detection (e.g., Snyk, OWASP Dependency-Check, or equivalent) | DevOps / Development Manager | CI/CD pipeline — build stage |
| **DAST** (Dynamic Application Security Testing) | Runtime vulnerability detection (e.g., OWASP ZAP, Burp Suite, or equivalent) | QA / Security Team | Pre-deployment stage |
| **Secret scanning** | Detection of credentials, API keys, tokens in code (e.g., GitLeaks, TruffleHog, or equivalent) | DevOps / Platform Team | Pre-commit hook + CI/CD pipeline |
| **Dependency database** | Vulnerability intelligence for third-party components (e.g., NVD, OSV, GitHub Advisory Database) | Development Manager | Continuous monitoring |
| **SBOM generator** | Software Bill of Materials generation (e.g., Syft, CycloneDX CLI, or equivalent) | DevOps / Platform Team | CI/CD pipeline — build stage |
| **Code review platform** | Peer review, approval workflow, audit trail (e.g., GitHub, GitLab, Bitbucket, or equivalent) | Development Manager | Pre-merge stage |
| **Penetration testing** | Manual security assessment by qualified external specialists | CISO | Pre-release (High-Risk) / periodic |

The toolchain shall be reviewed annually by the Development Manager and CISO. Tool changes shall follow the change management process. All tools shall be maintained at current supported versions.

---

## Environment Segregation

Development, test, and production environments shall be separated and shall not share common components, databases, or storage.

Development, test, and production environments shall be on separate networks or network segments.

There shall be a segregation of administrative duties between development/test and production environments. Personnel with write access to development repositories shall not have direct administrative access to production systems without separate authorisation.

Data shall not flow from production to development or test environments without explicit approval and appropriate sanitisation (see Test Data Protection section).

Configuration of environment segregation shall be documented, and compliance shall be verified at least annually.

---

## Application Risk Classification

All applications shall be classified by risk level to determine the appropriate security requirements.

**Risk Classification Criteria**:

| Risk Level | Criteria |
|------------|----------|
| **High-Risk** | Meets ANY: processes Confidential or Restricted data; handles PII subject to nFADP/GDPR; internet-facing or accessible by external parties; critical business function or financial transaction processing; payment card information (if PCI scope exists) |
| **Medium-Risk** | Meets ANY: processes Internal Use data; limited PII exposure (names, email addresses only); internal-only access; important but not critical business function |
| **Low-Risk** | Meets ALL: processes only Public data; no PII, no sensitive business data; non-critical business function |

Application risk classifications shall be reviewed annually by the Development Manager and CISO.

**Classification review triggers** (in addition to annual review):

| Trigger Event | Action |
|---------------|--------|
| New data type processed (e.g., PII, financial, health) | Re-classify within 14 days |
| Change in network exposure (internal → internet-facing) | Re-classify before deployment |
| Significant architecture change (new API, new integration) | Re-classify at design phase |
| Regulatory change affecting the application | Re-classify within 30 days |
| Security incident involving the application | Re-classify within 14 days of incident closure |
| Acquisition or merger affecting application scope | Re-classify within 60 days |

**Re-classification process**: (1) Application Owner submits change request with justification → (2) Development Manager assesses against classification criteria → (3) CISO approves if classification increases → (4) Updated security requirements applied within 60 days if classification increases → (5) Updated classification recorded in register.

The classification shall be recorded in the application risk classification register.

---

## Security Requirements

Security requirements shall be specified for all applications based on risk classification.

**Mandatory Requirements by Risk Level**:

| Requirement | High-Risk | Medium-Risk | Low-Risk |
|-------------|-----------|-------------|----------|
| Security requirements specification | Mandatory | Mandatory | Basic checklist |
| Threat modelling (e.g., STRIDE, PASTA, or Attack Trees) | Mandatory | Recommended | Optional |
| Security architecture review | Mandatory | Recommended | Optional |
| Requirements traceability | Mandatory | Recommended | Optional |

**Threat Modelling Process**:

Where threat modelling is required (mandatory for High-Risk, recommended for Medium-Risk), the following process shall be followed:

| Step | Activity | Output |
|------|----------|--------|
| 1. **Preparation** | Assemble team (developer, architect, Security Champion/CISO); gather system documentation, data flow diagrams, architecture diagrams | Scope definition and materials pack |
| 2. **Threat identification** | Apply STRIDE methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to each component and data flow | Threat catalogue |
| 3. **Risk rating** | Assess likelihood and impact of each identified threat using organisational risk criteria | Prioritised threat list |
| 4. **Mitigation planning** | Define security controls and requirements to address each threat; map to implementation tasks | Mitigation plan with owners and deadlines |
| 5. **Documentation** | Record threat model in approved format; link to security requirements specification | Completed threat model document |

Threat models shall be reviewed and updated: at each major release; when the application architecture changes significantly; when new threat intelligence relevant to the application is identified; and at least annually for High-Risk applications.

**Security requirements shall address the following areas as a minimum**:

- **Authentication and authorisation** — identity verification, role-based access, session handling.
- **Input validation and output encoding** — defence against injection attacks (OWASP Top 10 A05:2025).
- **Cryptography** — encryption of data in transit (TLS 1.2 minimum) and at rest per the Use of Cryptography Policy.
- **Session management** — secure session tokens, timeouts, invalidation on logout.
- **Error handling and logging** — no sensitive data in error messages; security events logged per the Logging Policy.
- **API security** — authentication, rate limiting, input validation for all API endpoints.
- **Data protection** — personal data handling per nFADP Art. 7 (privacy by design and default); data minimisation; secure deletion.

For applications that provide transactional services between the organisation and external parties, additional requirements shall address identity trust levels, integrity of exchanged information, non-repudiation, and confidentiality of transactions.

**Security Requirements Template**:

Security requirements specifications shall follow a standardised template covering the following sections:

| # | Section | Description |
|---|---------|-------------|
| 1 | Application overview | Name, purpose, risk classification, data classification |
| 2 | Data flow diagram | System context diagram showing data flows, trust boundaries, external interfaces |
| 3 | Authentication requirements | Authentication methods, MFA requirements, session management |
| 4 | Authorisation requirements | Access control model (RBAC/ABAC), privilege levels, segregation of duties |
| 5 | Input validation | Validation rules by input type, encoding requirements, file upload restrictions |
| 6 | Cryptography requirements | Encryption standards (per Use of Cryptography Policy), key management |
| 7 | API security | Authentication, rate limiting, input validation, versioning, error handling |
| 8 | Data protection | PII handling, data minimisation, retention, deletion, nFADP Art. 7 compliance |
| 9 | Logging and monitoring | Security events to log, log format, retention, alerting thresholds |
| 10 | Error handling | Error message content restrictions, fallback behaviour, graceful degradation |
| 11 | Third-party integration | Trust assessment, data sharing, API security, SLA requirements |
| 12 | Compliance requirements | Regulatory requirements (nFADP, GDPR where applicable), industry standards |
| 13 | Threat model summary | Key threats identified, mitigations required (for High-Risk applications) |
| 14 | Security testing plan | Required testing types, scope, schedule, acceptance criteria |

Security requirements shall be approved by the CISO (High-Risk) or Development Manager (Medium/Low-Risk) before development begins.

---

## Secure Coding Guidelines

Software shall be designed and developed based on industry-recognised secure coding guidelines, including:

- **OWASP** — OWASP Top 10:2025, OWASP Application Security Verification Standard (ASVS), and OWASP Secure Coding Practices.
- **NIST SP 800-218 (SSDF)** — Secure Software Development Framework for mitigating the risk of software vulnerabilities.
- **CWE/SANS Top 25** — Most dangerous software weaknesses, addressing categories such as injection, memory corruption, and authentication failures.

Language-specific secure coding standards shall be documented and maintained for each programming language in active use. These shall cover, at a minimum:

- Prohibited functions and insecure patterns.
- Required input validation and output encoding techniques.
- Approved cryptographic libraries and usage patterns.
- Secure error handling and logging practices.
- Dependency management and version pinning.

**Example — Python Secure Coding Standard** (illustrative; each language shall have equivalent documentation):

| Category | Requirement |
|----------|-------------|
| **Prohibited functions** | `eval()`, `exec()`, `pickle.loads()` on untrusted input, `os.system()` (use `subprocess.run()` with shell=False), `yaml.load()` without SafeLoader |
| **Required practices** | Parameterised queries (no string concatenation for SQL), `secrets` module for random generation (not `random`), type hints for security-critical functions, input validation using allowlists |
| **Approved crypto libraries** | `cryptography` library (preferred), `hashlib` (hashing only); prohibited: `pycrypto` (unmaintained), custom crypto implementations |
| **Error handling** | No sensitive data in exception messages; use structured logging; catch specific exceptions (not bare `except:`) |
| **Dependencies** | Pin versions in `requirements.txt` or `pyproject.toml`; review changelogs before major version upgrades; no dependencies with known critical CVEs |

Language-specific standards shall be stored in the code repository (e.g., `docs/secure-coding/` or equivalent), reviewed annually, and updated when new vulnerabilities or patterns emerge.

All developers shall complete secure coding training before being granted access to write production code (see Developer Security Training section).

---

## Code Repositories and Version Control

Development code shall be stored in a secure code repository that enforces and meets the requirements of the Access Control Policy and segregation of duty.

Repository access shall follow the principle of least privilege:

- Access shall be granted based on project assignment and role.
- Repository access shall be reviewed at least annually, aligned with identity and access management reviews.
- Former team members shall have access revoked within the same business day of departure.

Code repositories shall enforce:

- **Version control** with appropriate version archiving and branching strategy.
- **Branch protection** on main/production branches — direct commits prohibited; changes require pull/merge request approval.
- **Commit signing** recommended for High-Risk applications.
- **Secret scanning** to prevent accidental commit of credentials, API keys, or tokens.

**Secret Scanning and Secrets Management**:

Secret scanning shall detect, at a minimum: API keys, access tokens, private keys, database connection strings, cloud provider credentials, and webhook URLs.

**Detected secret remediation process**:

| Step | Action | Timeframe |
|------|--------|-----------|
| 1 | **Block commit** (pre-commit hook) or flag in CI/CD pipeline | Immediate |
| 2 | **Revoke and rotate** the exposed credential | Within 4 hours for production secrets; within 24 hours for non-production |
| 3 | **Remove from repository history** (if committed) using approved tools (e.g., git filter-branch, BFG Repo-Cleaner) | Within 24 hours |
| 4 | **Investigate exposure** — determine if the secret was accessed by unauthorised parties | Within 48 hours |
| 5 | **Document incident** — record in incident log; escalate to CISO if production secret exposed to external parties | Per incident management policy |

**Approved secrets management**:

| Environment | Approved Method |
|-------------|-----------------|
| Development | Environment variables, `.env` files (excluded from version control via `.gitignore`) |
| Test | Secrets manager or encrypted environment variables |
| Production | Dedicated secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, or equivalent) |
| CI/CD pipelines | Pipeline secrets store (e.g., GitHub Secrets, GitLab CI/CD Variables, or equivalent); no hardcoded secrets in pipeline definitions |

Hardcoded secrets in source code are prohibited. Secret scanning results shall be reviewed weekly by the Development Manager.

---

## Code Review

All code shall be reviewed prior to release by skilled personnel other than the code author or developer.

Code shall be reviewed against the secure coding guidelines documented by the organisation.

Code reviews shall employ both manual and automated techniques:

- **Manual peer review** — required for all code changes before merge to protected branches.
- **Security-focused review** — required for High-Risk applications, conducted by a Security Champion or security-trained reviewer.
- **Automated review** — SAST (Static Application Security Testing) tools integrated into the CI/CD pipeline (e.g., SonarQube, Semgrep, Checkmarx, or equivalent).

**Code Review Workflow**:

| Step | Activity | Responsible |
|------|----------|-------------|
| 1. **Submission** | Developer creates pull/merge request with description, linked requirements, and self-review checklist | Developer |
| 2. **Automated checks** | CI/CD pipeline runs SAST, SCA, secret scanning, linting, unit tests | Automated (DevOps) |
| 3. **Manual peer review** | Reviewer checks logic, readability, adherence to coding standards, test coverage | Peer reviewer |
| 4. **Security review** | Security-focused review against secure coding checklist (High-Risk: mandatory; Medium-Risk: recommended) | Security Champion or security-trained reviewer |
| 5. **Approval and merge** | Reviewer(s) approve; merge to protected branch | Reviewer(s) / Development Manager |

**Secure Code Review Checklist** (minimum items for security-focused review):

1. Input validation applied to all external inputs (user input, API parameters, file uploads)
2. Output encoding applied where data is rendered (HTML, JSON, SQL, LDAP)
3. Authentication and authorisation checks present and correct
4. No hardcoded secrets, credentials, or API keys
5. Cryptographic functions use approved libraries and algorithms
6. Error handling does not expose sensitive information
7. Logging includes security-relevant events without logging sensitive data
8. SQL queries use parameterised statements (no string concatenation)
9. File operations validate paths (no path traversal)
10. Third-party dependencies are pinned to reviewed versions

**Approval requirements by risk level**:

| Risk Level | Minimum Approvers | Security Review Required |
|------------|-------------------|--------------------------|
| High-Risk | 2 (including Security Champion or CISO-designated reviewer) | Mandatory |
| Medium-Risk | 1 | Recommended |
| Low-Risk | 1 | Optional |

Code review findings shall be documented and tracked to resolution before code is approved for promotion.

Code shall be approved before being promoted into test or production environments.

---

## CI/CD Pipeline Security Gates

Security checks shall be automated within the CI/CD pipeline at defined gates.

**Pipeline Security Gates**:

| Gate | Stage | Checks | Failure Action |
|------|-------|--------|----------------|
| **Gate 1: Pre-commit** | Developer workstation | Secret scanning (pre-commit hook) | Block commit; developer must remove secret |
| **Gate 2: Build** | CI pipeline — build stage | SAST scan, SCA dependency scan, licence compliance check, unit tests | Block merge; developer must remediate |
| **Gate 3: Pre-deployment** | CI pipeline — pre-deployment | DAST scan (High/Medium-Risk), integration tests, security regression tests | Block deployment; remediate or escalate |
| **Gate 4: Production deployment** | Deployment pipeline | Approval check (required approvers), change ticket verification, environment validation | Block deployment until approvals obtained |

**Failure thresholds** (automated gate blocking):

| Finding Severity | SAST/SCA Gate 2 | DAST Gate 3 |
|------------------|-----------------|-------------|
| Critical | Block | Block |
| High | Block | Block |
| Medium | Warn (track as technical debt) | Warn (track as technical debt) |
| Low | Log only | Log only |

**Override rules**: Pipeline gate overrides require CISO approval (documented in change ticket with risk acceptance and compensating controls). Emergency deployments may bypass Gate 3 DAST with CISO approval and mandatory retrospective scan within 72 hours.

Pipeline security gate results shall be reported to the Development Manager weekly and the CISO monthly.

---

## Security Testing Requirements

Security testing processes shall be defined and implemented in the development lifecycle. Testing shall validate that security requirements have been met before deployment to production.

**Required Testing by Risk Level**:

| Testing Type | High-Risk | Medium-Risk | Low-Risk |
|--------------|-----------|-------------|----------|
| **SAST** (Static Application Security Testing) | Per commit or daily | Per commit or daily | Weekly |
| **SCA** (Software Composition Analysis / dependency scanning) | Daily or continuous | Daily or continuous | Weekly |
| **DAST** (Dynamic Application Security Testing) | Per deployment or weekly | Monthly | Optional |
| **Penetration testing** | Annually + before initial release + after significant change | Every 2 years | Optional |

**Testing baseline requirements**:

- All application security testing shall, at a minimum, test for the **OWASP Top 10:2025** categories: Broken Access Control, Security Misconfiguration, Software Supply Chain Failures, Cryptographic Failures, Injection, Insecure Design, Authentication Failures, Software or Data Integrity Failures, Security Logging and Alerting Failures, and Mishandling of Exceptional Conditions.
- All pre-production testing shall occur in a test environment that mirrors the production environment as closely as possible.

**Testing environment similarity requirements**:

| Component | Production Parity Requirement |
|-----------|-------------------------------|
| Operating system | Same OS and version |
| Runtime / framework versions | Same major and minor versions |
| Database engine | Same engine and major version |
| Network architecture | Same segmentation model and firewall rules (IP ranges may differ) |
| TLS/SSL configuration | Same cipher suites and protocol versions |
| Authentication | Same authentication mechanism and MFA configuration |
| Load balancer / reverse proxy | Same type and configuration |
| Containerisation / orchestration | Same platform and version (if applicable) |

**Acceptable differences**: IP addresses, hostnames, scale (fewer instances permitted in test), monitoring volume thresholds, and synthetic/anonymised data instead of production data.

**Environment verification**: Environment parity shall be verified before major security tests (penetration testing, DAST). Verification shall be documented and signed off by the DevOps / Platform Team.

**Test environment security**: Test environments shall be subject to the same access controls as production environments. Test environments shall not be accessible from the internet unless required for DAST testing (with time-limited firewall rules).
- All penetration testing shall be conducted by an external specialist company.
- All public-facing web applications shall be tested using manual or automated vulnerability security tools at least annually or after a significant change.

**Penetration Testing Standards and Scope**:

| Application Type | Testing Approach | Frequency |
|------------------|------------------|-----------|
| Internet-facing web application (High-Risk) | Full OWASP Testing Guide assessment + business logic testing | Annually + before initial release + after significant change |
| Internet-facing web application (Medium-Risk) | OWASP Top 10 focused assessment | Every 2 years |
| Internal application (High-Risk) | Authenticated testing with business logic review | Annually |
| API-only service (High-Risk) | API security testing (OWASP API Security Top 10) | Annually |
| Mobile application | Mobile-specific testing (OWASP MASTG) | Annually for High-Risk |

**In scope** (minimum): Authentication and session management, authorisation and access control, input validation (injection, XSS, SSRF), business logic, API security, cryptographic implementation, configuration and deployment, error handling and information disclosure.

**Out of scope** (unless explicitly included): Denial-of-service testing, social engineering, physical security testing, third-party hosted components (tested separately by vendor).

**Testing standards**: Penetration tests shall follow OWASP Testing Guide v4.2 and/or PTES (Penetration Testing Execution Standard). Test reports shall include: executive summary, methodology, findings with CVSS scoring, evidence (screenshots, request/response), remediation recommendations, and re-test verification.

**Vendor selection criteria**: Penetration testing vendors shall hold relevant certifications (e.g., CREST, OSCP, CEH) and provide evidence of professional indemnity insurance. Vendor engagements shall include signed rules of engagement and NDA.

**Post-test actions**: (1) Remediate findings per Vulnerability Remediation SLAs → (2) Vendor re-tests critical/high findings after remediation → (3) Final report with re-test results presented to CISO and Management Review Team → (4) Lessons learned incorporated into secure coding standards → (5) Report retained for 5 years.

**Software Bill of Materials (SBOM)**:

- High-Risk applications shall maintain an SBOM in CycloneDX or SPDX format.
- SBOMs shall be generated automatically during the build process (every build for High-Risk; weekly for Medium-Risk).
- SBOMs shall be updated upon dependency changes and reviewed quarterly for known vulnerabilities.

**SBOM content requirements**: Each SBOM shall include: component name and version, supplier/author, licence type, dependency relationships (direct and transitive), and known vulnerability status (CVE references where applicable).

**Quarterly SBOM review process**: (1) Generate current SBOM → (2) Cross-reference all components against vulnerability databases (NVD, OSV, GitHub Advisory Database) → (3) Identify components with known vulnerabilities, end-of-life status, or licence changes → (4) Create remediation plan for identified issues (per Vulnerability Remediation SLAs).

**SBOM vulnerability monitoring**: SCA tools shall continuously monitor SBOM components against vulnerability databases. New critical/high vulnerabilities affecting SBOM components shall trigger alerts to the Development Manager within 24 hours.

**SBOM retention**: SBOMs shall be retained for the lifecycle of the application plus 3 years.

Test results, including penetration testing reports, shall be reported to the Management Review Team.

---

## Vulnerability Remediation

Security vulnerabilities identified during development and testing shall be remediated within defined timeframes based on severity.

**Remediation Service Level Agreements**:

| Severity | CVSS Score | Remediation SLA | Deployment Impact |
|----------|------------|-----------------|-------------------|
| **Critical** | 9.0–10.0 | 7 days | Block deployment if unresolved |
| **High** | 7.0–8.9 | 30 days | Block deployment if overdue |
| **Medium** | 4.0–6.9 | 90 days | Track as technical debt |
| **Low** | 0.1–3.9 | 180 days | Plan for next major release |

All vulnerabilities identified as part of the testing phase, including penetration testing, shall be corrected prior to promotion to production or managed via the risk management and exception process.

**Escalation process**:

- Vulnerabilities exceeding the remediation SLA shall be escalated to the CISO and Application Owner.
- Critical and High vulnerabilities overdue beyond the SLA shall block subsequent deployments until remediated or an exception is approved with compensating controls.
- Vulnerability remediation status shall be reviewed monthly and reported quarterly to the Management Review Team.

---

## Test Data Protection

Production data shall not be used for testing or development.

Personal data (as defined by Swiss nFADP Art. 5) shall not be used for testing or development.

If sensitive information is required as part of the testing process, it shall be:

- **sanitised** (sensitive fields removed or replaced),
- **anonymised** (irreversible removal of identifying characteristics), or
- **pseudonymised** (identifying data replaced with artificial identifiers).

**Synthetic data** (artificially generated data with no connection to real individuals) is the preferred approach and shall be used where feasible.

The creation and use of test data sets shall be documented and approved by the data owner. Test data sets containing transformed personal data shall be treated as Internal classification at a minimum.

Test data shall be securely deleted when no longer required.

---

## Promoting Code to Production

Code shall be promoted to production by approved personnel only and shall be subject to the documented change management process.

Before promotion to production:

- All required security gates shall be passed (security testing, code review, vulnerability remediation).
- The production environment shall be backed up to facilitate rollback in the event of a failed change.
- Test data shall be removed from the application.
- No development files, debug configurations, test accounts, or test data shall be present in the production environment.
- For High-Risk applications, the CISO or designated security authority shall provide explicit sign-off.

Promotion records shall include the change ticket reference, approver, security gate status, and deployment timestamp.

---

## Outsourced Development

Where software development is outsourced to third-party contractors or development partners, the organisation's secure development requirements shall apply.

**Contractual requirements shall include**:

- Compliance with the organisation's secure coding standards and security requirements.
- Security testing obligations (SAST, DAST, SCA) with reporting to the organisation.
- Vulnerability remediation SLAs aligned with this policy.
- Security incident notification within 24 hours of discovery.
- The organisation's right to audit contractor security practices upon 30 days' notice.
- Code review and security architecture review participation rights.

**Verification of contractor compliance**:

- Contractors shall submit security testing reports (SAST/DAST/SCA results, remediation status) at agreed intervals.
- High-Risk outsourced projects shall undergo security review by the organisation's security-qualified personnel at major milestones (design approval, pre-production).
- Code delivered by contractors shall undergo the same code review and security testing process as internally developed code before acceptance.

---

## Developer Security Training

All developers shall complete security training appropriate to their role and responsibilities.

**Training Requirements**:

| Training Type | Audience | Frequency | Minimum Duration |
|---------------|----------|-----------|------------------|
| **Initial security training** | All developers | Before production code access | 4 hours |
| **Annual refresher** | All developers | Annually | 2 hours |
| **Security Champion training** (optional for SMEs) | Nominated Security Champions | Initial + annually | 8 hours + 4 hours |

Training shall cover, at a minimum:

- OWASP Top 10 vulnerabilities and mitigation techniques.
- Secure coding practices relevant to the developer's technology stack.
- The organisation's secure development policy and coding standards.
- Common software weaknesses (CWE/SANS Top 25).

Training completion shall be recorded and verified before granting production code access. Training records shall be retained for the duration of employment plus 3 years.

Where resources permit, the organisation should establish a **Security Champion programme** — nominated developers within each team who receive advanced security training and serve as the first point of contact for security questions within their team.

**Security Champion Programme** (where established):

**Selection criteria**: Security Champions shall be nominated from development teams based on: demonstrated interest in security, minimum 2 years development experience, willingness to commit approximately 10% of working time to security activities, and team lead endorsement.

**Responsibilities**:
- Conduct security-focused code reviews for High-Risk changes within their team.
- Provide secure coding guidance and mentorship to team members.
- Participate in threat modelling sessions as the team security representative.
- Escalate security concerns to the CISO or security team.
- Stay current on emerging threats and vulnerabilities relevant to the team's technology stack.
- Champion security culture and awareness within the team.

**Training**: Initial training: 8 hours (OWASP Top 10 deep dive, secure architecture patterns, threat modelling, security testing tools). Annual refresher: 4 hours (emerging threats, new attack techniques, updated standards).

**Incentives**: Security Champion contributions shall be recognised in performance reviews. The organisation should consider conference attendance, certification sponsorship, or similar professional development opportunities.

**Programme metrics**: Number of active Security Champions (target: at least 1 per development team), security review participation rate, security findings identified in code review, training completion rate.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; security gate approval for High-Risk applications; exception approval; escalation authority; training programme oversight |
| **Development Manager** | SDLC security integration; code review enforcement; secure coding standards maintenance; vulnerability remediation oversight; application risk classification |
| **Security Champion** (where established) | Security advocacy within development team; security-focused code review; secure coding mentorship |
| **Developers** | Adherence to secure coding standards; vulnerability remediation; security training completion; code review participation |
| **QA / Test Lead** | Security testing execution; test environment management; test data protection; security test reporting |
| **DevOps / Platform Team** | CI/CD security tool integration; environment segregation; deployment automation; secret scanning |
| **Application Owner** | Application risk classification input; exception requests; security requirements approval |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Application risk classification register** (all applications classified by risk level) | Development Manager / CISO | *Maintained continuously; reviewed annually; target: 100% of applications classified* |
| 2 | **Security requirements documentation** (requirements specifications, threat models for High-Risk) | Development Manager | *Per project; retained for lifecycle of application* |
| 3 | **SAST/SCA scan reports** (tool execution logs, findings, remediation status) | DevOps / Development Manager | *Per policy frequency by risk level; retained 2 years* |
| 4 | **Penetration test reports** (scope, findings, remediation verification) | CISO | *Annually for High-Risk; every 2 years for Medium-Risk; retained 5 years* |
| 5 | **Code review records** (review comments, approval records, merge request history) | Development Manager | *Per code change; retained 2 years* |
| 6 | **Vulnerability remediation records** (tickets with SLA tracking, closure evidence) | Development Manager | *Per vulnerability; reviewed monthly; retained 3 years* |
| 7 | **Environment segregation documentation** (network diagrams, access control records) | DevOps / IT Operations | *Reviewed annually; updated upon change* |
| 8 | **Developer security training records** (completion dates, training content covered) | CISO / HR | *Tracked per developer; reviewed annually; target: 100% completion* |
| 9 | **Outsourced development security reports** (contractor SAST/DAST/SCA results, audit records) | Development Manager / CISO | *Per contract terms; retained for contract duration + 3 years* |
| 10 | **Production deployment records** (change tickets, security gate sign-off, rollback plans) | Change Management / DevOps | *Per deployment; retained 3 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, SAST/DAST/SCA scan reports, code review records, penetration test reports, developer training records, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team. Emergency deployments bypassing security gates require CISO approval and retrospective security validation within 72 hours.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to secure development standards (OWASP, NIST SSDF, CWE/SANS Top 25), emerging threats and attack techniques, regulatory changes, development tooling and methodology changes, and lessons learned from security incidents and penetration tests.

---

# Areas of the ISO 27001 Standard Addressed

Secure Development Lifecycle Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.4 Access to source code |
| | **8.25 Secure development lifecycle** |
| | **8.26 Application security requirements** |
| | 8.27 Secure system architecture and engineering principles |
| | 8.28 Secure coding |
| | **8.29 Security testing in development and acceptance** |
| | 8.30 Outsourced development |
| | 8.31 Separation of development, test, and production environments |
| | 8.33 Test information |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 7 — Data protection by design and by default; Art. 8 — Technical and organisational measures for data protection |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 25 — Data protection by design and by default; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Controls 8.25, 8.26, 8.29 — Secure development, application security requirements, security testing |
| ISO/IEC 27002:2022 | Sections 8.25–8.31, 8.33 — Implementation guidance for secure development controls |
| NIST SP 800-218 (SSDF) | Secure Software Development Framework — practice groups PO, PS, PW, RV |
| OWASP Top 10:2025 | Minimum testing baseline — includes Software Supply Chain Failures and Mishandling of Exceptional Conditions |
| CWE/SANS Top 25 | Most dangerous software weaknesses — secure coding reference |

---

<!-- QA_VERIFIED: 2026-02-07 -->
