**ISMS-OP-POL-A.8.28 — Secure Coding**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure Coding |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.28 |
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

- ISO/IEC 27001:2022 Control A.8.28 — Secure coding
- ISO/IEC 27002:2022 Section 8.28 — Implementation guidance for secure coding
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1
- NIST SP 800-53 Rev 5 — SA-15 (Development Process, Standards, and Tools), SA-16 (Developer-Provided Training), SA-17 (Developer Security Architecture and Design)
- OWASP Secure Coding Practices — Quick Reference Guide
- OWASP Top 10 (2021) — Web Application Security Risks
- CWE/SANS Top 25 — Most Dangerous Software Weaknesses (2025 edition)
- CIS Controls v8 — Safeguard 16.1–16.14 (Application Software Security)
- CERT Secure Coding Standards (SEI/Carnegie Mellon)

**Related Annex A Controls**:

| Control | Relationship to Secure Coding |
|---------|-------------------------------|
| A.5.8 Information security in project management | Security requirements defined at project initiation |
| A.5.23 Information security for use of cloud services | Secure coding for cloud-deployed applications |
| A.8.4 Access to source code | Repository access control and branch protection |
| A.8.8 Management of technical vulnerabilities | Vulnerability remediation for deployed code |
| A.8.9 Configuration management | Secure configuration of development tools and environments |
| A.8.15 Logging | Application-level security logging requirements |
| A.8.24 Use of cryptography | Cryptographic implementation in application code |
| A.8.25–26–29 Secure development lifecycle | Overarching SDLC framework; security requirements, testing |
| A.8.31 Separation of environments | Isolation of development, test, and production |
| A.8.32 Change management | Controlled deployment of code changes to production |

**Related Internal Policies**:

- Secure Development Lifecycle Policy
- Access to Source Code Policy
- Vulnerability Management Policy
- Use of Cryptography Policy
- Change Management Policy
- Logging and Monitoring Policy

---

# Secure Coding Policy

## Purpose

The purpose of this policy is to establish mandatory secure coding principles that shall be applied throughout the software development lifecycle. Secure coding prevents vulnerabilities from entering the codebase, reducing the attack surface and protecting the organisation's information assets, customers, and reputation. Poor coding practices — improper input validation, weak key generation, hard-coded credentials, insufficient error handling — create exploitable weaknesses that adversaries routinely target.

This policy supports Swiss nFADP (revDSG) Art. 7 (data protection by design and default) and Art. 8 (technical and organisational measures) by requiring that security is integrated into application code from the design phase. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 25 (data protection by design and default) and Art. 32 (security of processing) requirements also apply. Secure coding is a foundational technical measure for demonstrating that systems processing personal data are built to prevent unauthorised access, data breaches, and integrity violations.

## Scope

All software development activities where the organisation writes, modifies, or maintains source code. This includes:

- All internally developed applications (web, mobile, desktop, API, microservices).
- Infrastructure-as-Code (IaC), configuration management scripts, and CI/CD pipeline definitions.
- Custom integrations, plugins, and extensions to third-party platforms.
- Open source contributions made under the organisation's name.
- Code written by contractors, outsourced development teams, and offshore developers working on the organisation's behalf.

All developers, security engineers, QA engineers, DevOps engineers, contractors, and third-party development teams writing code for the organisation.

**Out of scope**: Commercial off-the-shelf (COTS) software without customisation (covered under vendor security assessment); production runtime vulnerability management post-deployment (covered under A.8.8); secure development lifecycle governance (covered under A.8.25-26-29); source code access control (covered under A.8.4).

## Principle

All source code produced for or on behalf of the organisation shall follow documented secure coding standards. Security shall be considered before coding begins, applied during coding, and verified after coding is complete. Developers shall not rely on security testing alone to find defects — secure coding prevents defects from being introduced in the first place.

The organisation shall explicitly define which coding standards it follows, referencing recognised industry frameworks (OWASP, CWE/SANS Top 25, CERT, or language-specific guidelines). Generic claims of "coding securely" without citing a framework are insufficient for audit purposes.

---

## Secure Coding Standards

The organisation shall establish and maintain documented secure coding standards applicable to each programming language and framework in active use.

**Baseline Frameworks**:

| Framework | Scope | Application |
|-----------|-------|-------------|
| OWASP Top 10 (2021) | Web application vulnerabilities | Mandatory reference for all web-facing code |
| CWE/SANS Top 25 | Most dangerous software weaknesses | Mandatory reference for all code |
| OWASP Secure Coding Practices | Technology-agnostic coding checklist | Mandatory reference for all development |
| CERT Secure Coding Standards | Language-specific secure coding (C, C++, Java, Perl) | Mandatory where language-specific standards exist |

**Language-Specific Standards**:

The Development Manager shall maintain a register of approved languages and their associated secure coding references. At minimum:

| Language / Framework | Secure Coding Reference |
|----------------------|------------------------|
| Python | PEP 8 + OWASP Python Security + Bandit rule set |
| JavaScript / TypeScript | ESLint security plugin rules + OWASP NodeGoat reference |
| Java | CERT Oracle Secure Coding Standard for Java + SpotBugs/FindSecBugs rules |
| C / C++ | CERT C/C++ Secure Coding Standards + compiler warning enforcement |
| Go | Go security best practices + govulncheck |
| .NET / C# | Microsoft Secure Coding Guidelines + Roslyn analysers |
| PHP | OWASP PHP Security Cheat Sheet + Psalm/PHPStan rules |

Where a language is used that has no entry in this register, the Development Manager shall document the applicable secure coding reference before the language enters production use.

**Coding Standards Review**: Secure coding standards shall be reviewed annually, or when a new language or framework is adopted, or when a significant vulnerability class emerges that requires additional guidance.

---

## Common Vulnerability Prevention

Developers shall write code that prevents the vulnerability classes identified by the OWASP Top 10 and CWE/SANS Top 25. The following sections define mandatory coding practices for the most prevalent vulnerability categories.

### Input Validation

All input from external sources shall be treated as untrusted and validated before processing.

**Requirements**:

- Validate all input on the server side, regardless of client-side validation. Client-side validation improves user experience but does not provide security.
- Use allowlist (positive) validation: define what is permitted, reject everything else. Denylist (negative) validation is insufficient as a sole control.
- Validate data type, length, range, and format. Reject malformed input before processing.
- Validate and sanitise all inputs from forms, URL parameters, HTTP headers, cookies, API payloads, file uploads, and data from upstream systems.
- Use parameterised queries or prepared statements for all database interactions. Concatenation of user input into SQL statements is prohibited.
- Validate file uploads: restrict permitted file types, enforce size limits, scan for malware, store uploaded files outside the web root, and never execute uploaded files.

### Output Encoding

All output rendered to users or external systems shall be encoded to prevent injection attacks.

**Requirements**:

- Apply context-appropriate output encoding (HTML, JavaScript, URL, CSS, XML) when rendering dynamic content.
- Use framework-provided encoding functions rather than custom implementations.
- Encode output at the point of rendering, not at the point of storage.
- Set Content-Type and charset headers correctly on all HTTP responses.
- Implement Content Security Policy (CSP) headers to mitigate cross-site scripting (XSS) risks.

### Authentication and Session Management

Application code implementing authentication and session handling shall follow established secure patterns.

**Requirements**:

- Do not implement custom authentication schemes. Use the organisation's approved authentication framework or identity provider.
- Store passwords using approved adaptive hashing algorithms (bcrypt, scrypt, or Argon2id) with unique salts. MD5, SHA-1, and unsalted hashes are prohibited.
- Implement account lockout or progressive delays after repeated failed authentication attempts.
- Generate session identifiers using cryptographically secure random number generators. Session IDs shall be of sufficient length (minimum 128 bits of entropy).
- Set secure cookie attributes: `Secure`, `HttpOnly`, `SameSite`. Transmit session cookies only over TLS.
- Invalidate sessions on logout, password change, and privilege escalation. Set appropriate session timeout values.
- Do not expose session identifiers in URLs, error messages, or logs.

### Error Handling and Logging

Application error handling shall prevent information disclosure and support security monitoring.

**Requirements**:

- Display generic error messages to users. Do not expose stack traces, database error messages, internal file paths, framework version numbers, or server configuration details.
- Log all security-relevant events: authentication successes and failures, authorisation failures, input validation failures, application errors, and administrative actions.
- Log sufficient context for investigation: timestamp (UTC), user identity, source IP address, action attempted, resource affected, and success or failure status.
- Do not log sensitive data: passwords, session tokens, personal data, credit card numbers, or encryption keys.
- Use a centralised logging framework. Do not write custom logging mechanisms that bypass the organisation's logging infrastructure.
- Ensure log entries containing untrusted data cannot execute as code in the log viewing interface (log injection prevention).

### Cryptographic Practices

Application code that implements or uses cryptography shall follow the organisation's cryptographic policy.

**Requirements**:

- Use cryptographic libraries provided by the platform or approved third-party libraries. Do not implement custom cryptographic algorithms.
- Use current, approved algorithms: AES-256 for symmetric encryption, RSA-2048+ or ECDSA P-256+ for asymmetric operations, SHA-256+ for hashing. MD5 and SHA-1 are prohibited for security purposes.
- TLS 1.2 minimum (TLS 1.3 preferred) for all data in transit. SSL, TLS 1.0, and TLS 1.1 are prohibited.
- Generate cryptographic keys using cryptographically secure random number generators. Do not use predictable seeds.
- Do not hard-code cryptographic keys, API keys, or secrets in source code. Use the organisation's approved secrets management solution.
- Refer to ISMS-OP-POL-A.8.24 (Use of Cryptography) for the full cryptographic requirements.

### Access Control in Code

Application code shall enforce authorisation consistently.

**Requirements**:

- Enforce access control on the server side for every request. Do not rely solely on hiding UI elements.
- Default to deny: if a user's permission level cannot be determined, deny access.
- Apply the principle of least privilege in code: grant the minimum permissions required for each function.
- Validate authorisation for every API endpoint, including indirect object references.
- Do not trust client-supplied role or permission claims without server-side verification.

---

## Dependency and Library Management

Third-party libraries, frameworks, and open source components introduce supply chain risk and shall be managed throughout their lifecycle.

**Requirements**:

- Maintain a dependency inventory for each application. High-risk applications shall maintain a Software Bill of Materials (SBOM) in CycloneDX or SPDX format.
- Use Software Composition Analysis (SCA) tooling ([SCA Tool] — e.g., Dependabot, Snyk, OWASP Dependency-Check, or equivalent) to scan dependencies for known vulnerabilities.
- SCA scanning shall run on every build (CI/CD pipeline integration). Builds shall fail if critical or high-severity dependency vulnerabilities are detected and unresolved.
- Pin dependency versions in lock files. Do not use floating version ranges (e.g., `*` or `>=`) for production dependencies.
- Evaluate new dependencies before adoption: check maintenance status, known vulnerabilities, licence compatibility, and community activity. Abandoned or unmaintained libraries shall not be introduced.
- Remove unused dependencies. Conduct a dependency audit at least annually to identify and remove libraries no longer in use.

**Remediation SLAs for Dependency Vulnerabilities**:

| Severity | CVSS Score | Remediation SLA |
|----------|------------|-----------------|
| Critical | 9.0–10.0 | 7 days |
| High | 7.0–8.9 | 30 days |
| Medium | 4.0–6.9 | 90 days |
| Low | 0.1–3.9 | Next planned release |

---

## Code Review Requirements

All code changes shall be reviewed before merging to protected branches.

**Review Types**:

| Review Type | When Required | Reviewer |
|-------------|---------------|----------|
| Peer code review | All code changes | At least one developer other than the author |
| Security-focused code review | Changes to authentication, authorisation, cryptography, input validation, session handling, or data protection code | Developer with security training or Security Champion |
| Automated code review | All code changes | [SAST Tool] integrated into CI/CD pipeline |

**Peer Code Review Requirements**:

- The code author shall not approve their own code (separation of duties).
- Reviewers shall verify adherence to the organisation's secure coding standards.
- Reviewers shall check for: hard-coded secrets, insecure coding patterns, missing input validation, missing output encoding, excessive permissions, inadequate error handling, and missing logging.
- Pull requests shall include a description of changes, link to the related issue or ticket, and evidence of testing.
- Reviews shall be completed before the code is merged to a protected branch.

**Security-Focused Code Review Checklist**:

- [ ] Input validation applied to all external inputs
- [ ] Output encoding applied at rendering points
- [ ] No hard-coded secrets, keys, or credentials
- [ ] Parameterised queries used for database interactions
- [ ] Authentication and session handling use approved libraries
- [ ] Error messages do not disclose internal details
- [ ] Security-relevant events are logged
- [ ] Sensitive data is not logged
- [ ] Cryptographic operations use approved algorithms and libraries
- [ ] Access control checks are server-side and applied per request
- [ ] Dependencies are pinned and free of known critical vulnerabilities

---

## Static Application Security Testing (SAST)

Automated static analysis shall be integrated into the development workflow to detect security defects before deployment.

**Requirements**:

- The organisation shall deploy a SAST tool ([SAST Tool] — e.g., SonarQube, Semgrep, CodeQL, Checkmarx, or equivalent) integrated into the CI/CD pipeline.
- SAST scans shall run on every pull request or merge request to a protected branch.
- SAST results shall be reviewed before merging. Critical and high-severity findings shall block the merge until resolved or explicitly accepted as false positives with documented justification.
- SAST rule sets shall cover, at minimum, the OWASP Top 10 and CWE/SANS Top 25 vulnerability classes.
- False positives shall be documented and suppressed with a justification comment in the code or tool configuration. Suppression without justification is prohibited.
- SAST tool configuration and rule sets shall be reviewed annually by the Development Manager and Security Team.

**SAST Coverage Requirements**:

| Application Classification | Scan Frequency | Findings Review |
|---------------------------|----------------|-----------------|
| Production applications | Per commit / pull request | Before merge |
| Internal tools | Per commit / pull request | Before merge |
| Proof of concepts | Weekly (if stored in organisational repositories) | Weekly triage |

---

## Secure Coding Training

Developers shall receive training to write secure code effectively.

**Training Requirements**:

| Training Type | Audience | Frequency | Minimum Duration |
|---------------|----------|-----------|------------------|
| Secure coding fundamentals | All developers (including contractors) | Before writing production code | 4 hours |
| Annual refresher | All developers | Annually | 2 hours |
| Security Champion training | Designated Security Champions | Initial + annual | 8 hours initial; 4 hours refresher |
| Language-specific secure coding | Developers adopting a new language | Before production use of that language | 2 hours |

**Training Content** shall cover, at minimum:

- OWASP Top 10 and CWE/SANS Top 25 vulnerability classes.
- Secure coding standards applicable to the developer's primary language.
- Input validation, output encoding, and injection prevention.
- Authentication, session management, and access control patterns.
- Secrets management and the prohibition on hard-coded credentials.
- Secure use of cryptographic libraries.
- Dependency management and supply chain security.
- Use of the organisation's SAST and SCA tools.

**Training Evidence**: Completion records shall be maintained in [HR System / LMS] and reviewed by the Development Manager quarterly.

---

## Insecure Coding Practices — Prohibition

The following coding practices are prohibited:

| Prohibited Practice | Reason | Required Alternative |
|---------------------|--------|---------------------|
| Hard-coded passwords, API keys, or secrets in source code | Secrets exposed via repository access or code leaks | Use environment variables or approved secrets management ([Secrets Manager]) |
| SQL statement construction by string concatenation with user input | SQL injection vulnerability | Use parameterised queries or prepared statements |
| Deserialisation of untrusted data without validation | Remote code execution risk | Validate and sanitise before deserialisation; use safe deserialisation libraries |
| Use of deprecated or insecure cryptographic algorithms (MD5, SHA-1, DES, RC4) | Known weaknesses; brute-force or collision attacks | Use approved algorithms per cryptographic policy |
| Disabled or bypassed TLS certificate validation | Man-in-the-middle attack exposure | Enforce certificate validation in all environments except isolated test |
| Unapproved code samples copied from public sources without review | May contain vulnerabilities, backdoors, or licence violations | Review and adapt; verify licence compatibility; scan with SAST |
| Logging of sensitive data (passwords, tokens, personal data) | Data exposure through log files | Use data masking or exclude sensitive fields from logging |
| Use of `eval()` or equivalent dynamic code execution with user input | Code injection vulnerability | Use safe alternatives; validate and sanitise input |

---

## Outsourced Development

Code produced by external contractors and outsourced development teams shall meet the same secure coding standards as internally developed code.

**Contractual Requirements**:

- Contracts shall require adherence to the organisation's secure coding standards and this policy.
- Contractors shall provide evidence of secure coding training for their developers.
- All contractor-produced code shall undergo the same code review and SAST scanning as internal code.
- Contractors shall remediate security findings within the organisation's defined SLAs.
- The organisation retains the right to audit contractor secure coding practices.

**Verification**:

- Contractor code shall be reviewed by an internal developer before merging.
- SAST and SCA results for contractor-produced code shall be visible to the organisation's Security Team.
- High-risk code produced by contractors (authentication, authorisation, cryptography, data protection) shall receive a security-focused code review by a Security Champion or Security Architect.

---

## Exception Management

Exceptions to this policy shall be requested in writing and shall include:

- Specific requirement(s) requiring exception.
- Business justification.
- Compensating controls.
- Requested exception duration (maximum 12 months).
- Risk assessment and acceptance.

Exceptions shall be approved by the Development Manager and Information Security Manager (mandatory), plus the CISO for production application exceptions. All active exceptions shall be reviewed quarterly.

Where technically infeasible to meet a requirement (e.g., legacy code base that cannot be refactored immediately), compensating controls shall be implemented, documented, verified by the Information Security Manager, and reviewed annually.

---

## Definitions

| Term | Definition |
|------|------------|
| **CSP** | Content Security Policy — HTTP response header that restricts which resources a browser is allowed to load for a page, mitigating XSS |
| **CWE** | Common Weakness Enumeration — a community-developed list of software and hardware weakness types |
| **Dependency** | A third-party library, framework, or component used by application code |
| **Injection** | A class of vulnerabilities where untrusted data is sent to an interpreter as part of a command or query (e.g., SQL injection, XSS, command injection) |
| **OWASP** | Open Worldwide Application Security Project — non-profit foundation producing standards, tools, and guidance for application security |
| **Parameterised query** | A database query technique that separates SQL logic from user-supplied data, preventing SQL injection |
| **SAST** | Static Application Security Testing — automated analysis of source code to identify security defects without executing the application |
| **SBOM** | Software Bill of Materials — a machine-readable inventory of all components, libraries, and dependencies in a software application |
| **SCA** | Software Composition Analysis — automated scanning of third-party dependencies for known vulnerabilities and licence risks |
| **Security Champion** | A developer with specialised security training who acts as the security contact within a development team |
| **TLS** | Transport Layer Security — cryptographic protocol for securing data in transit |
| **XSS** | Cross-Site Scripting — a vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; exception approval for production applications; oversight of secure coding compliance; annual policy review; reporting to Executive Management |
| **Development Manager** | Secure coding standards maintenance (per language); code review enforcement; SAST/SCA tool selection and configuration; developer training coordination; compliance reporting to CISO |
| **Information Security Manager** | Policy maintenance; exception review; security monitoring and incident investigation; audit coordination; quarterly compliance reporting to CISO |
| **Security Champions** | Security-focused code reviews; secure coding mentorship within development teams; secure coding standards advocacy; escalation of security concerns to Security Team |
| **Security Team** | SAST/SCA tool management and rule set updates; security-focused code review for high-risk changes; security testing coordination; incident response for code-level vulnerabilities |
| **DevOps Engineers** | CI/CD pipeline integration of SAST and SCA tools; build pipeline enforcement of security gates; secrets management infrastructure |
| **Individual Developers and Contractors** | Adherence to secure coding standards; code review participation; timely remediation of security findings; completion of secure coding training; incident reporting for security defects |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Secure coding standards register** (approved languages, frameworks, and associated coding references) | Development Manager | Maintained continuously; reviewed annually | Current version + 3 years |
| 2 | **SAST scan results** (tool execution logs, findings, false positive justifications) | Development Manager / DevOps | Per pull request; reviewed monthly | 2 years |
| 3 | **SCA dependency scan results** (vulnerability findings, SBOM outputs, remediation records) | Development Manager / DevOps | Per build; reviewed monthly | 2 years |
| 4 | **Code review records** (pull request reviews, security review checklists, approval records) | Development Manager | Per code change | 3 years |
| 5 | **Security-focused code review records** for high-risk changes (authentication, authorisation, cryptography) | Security Champions / Security Team | Per applicable change | 3 years |
| 6 | **Secure coding training completion records** (fundamentals, refresher, language-specific, Security Champion) | Development Manager / HR | Annually; per onboarding | Employment duration + 3 years |
| 7 | **Dependency vulnerability remediation records** (finding-to-closure tracking with SLA compliance) | Development Manager | Per finding | 3 years |
| 8 | **SAST/SCA tool configuration records** (rule sets, enabled checks, suppression justifications) | Security Team / DevOps | Reviewed annually | Current version + 1 year |
| 9 | **Prohibited practices violation records** (incidents of hard-coded secrets, insecure patterns detected and remediated) | Security Team | Per incident | 3 years |
| 10 | **Exception register** (requests, approvals, compensating controls, quarterly reviews) | Information Security Manager | Maintained continuously; reviewed quarterly | Exception duration + 3 years |
| 11 | **Outsourced development secure coding evidence** (contractor training records, code review records, SLA compliance) | Development Manager / Procurement | Per contractor engagement | Contract duration + 3 years |
| 12 | **Annual secure coding standards review records** (review date, changes made, approval) | Development Manager | Annually | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, SAST/SCA tool reports, code review completion records, training completion records, dependency audit results, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Code changes with completed peer review before merge | 100% | Monthly |
| SAST scans executed per pull request (production applications) | >= 95% | Monthly |
| Critical/high SAST findings remediated before merge or documented as false positive | >= 95% | Monthly |
| Critical/high dependency vulnerabilities remediated within SLA | >= 90% | Monthly |
| Developers with current secure coding training | >= 95% | Quarterly |
| Hard-coded secrets detected and remediated within 24 hours | 100% | Per incident |

**Compliance Scoring**:

| Component | Weight | Calculation |
|-----------|--------|-------------|
| Code Review Compliance | 30% | (Code changes with completed review) / Total code changes x 100 |
| SAST Coverage | 25% | (Pull requests with passing SAST scan) / Total pull requests x 100 |
| Dependency Security | 25% | (Critical/high dependency vulnerabilities remediated within SLA) / Total critical/high findings x 100 |
| Training Compliance | 20% | (Developers with current training) / Total developers x 100 |

**Non-Compliance Handling**: Below 70% requires immediate CISO escalation and remediation plan. 70-89% requires Information Security Manager oversight with monthly reviews. 90% and above follows standard quarterly monitoring.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months). Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Policy violations shall be documented, investigated by the Information Security Manager, and reported to the CISO.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider emerging vulnerability classes, changes to the OWASP Top 10 and CWE/SANS Top 25, new programming languages or frameworks adopted by the organisation, evolution of SAST/SCA tooling, audit findings, and lessons learned from security incidents involving application-level vulnerabilities.

---

# Areas of the ISO 27001 Standard Addressed

Secure Coding Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.4 Access to source code |
| | 8.25 Secure development lifecycle |
| | 8.26 Application security requirements |
| | **8.28 Secure coding** |
| | 8.29 Security testing in development and acceptance |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 7 — Data protection by design and default; Art. 8 — Technical and organisational measures; secure coding as a preventive technical measure |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security, including application-level controls |
| EU GDPR (where applicable) | Art. 25 — Data protection by design and default; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 8.28 — Secure coding |
| ISO/IEC 27002:2022 | Section 8.28 — Implementation guidance for secure coding |
| NIST SP 800-218 (SSDF) v1.1 | PW.4 — Create source code adhering to secure coding practices; PW.5 — Configure build process securely; PW.6 — Review and test code |
| NIST SP 800-53 Rev 5 | SA-15 (Development Process, Standards, and Tools), SA-16 (Developer-Provided Training), SA-17 (Developer Security Architecture and Design) |
| CIS Controls v8 | 16.1 (Secure Application Development Process), 16.2 (Manage Software Architecture), 16.4 (Secure Custom-Developed Software), 16.12 (Implement Code-Level Security Checks) |
| OWASP Top 10 (2021) | A01–A10 — Web application security risk categories addressed through secure coding practices |
| CWE/SANS Top 25 (2025) | Most dangerous software weaknesses addressed through input validation, output encoding, and secure coding standards |

---

<!-- QA_VERIFIED: 2026-02-07 -->
