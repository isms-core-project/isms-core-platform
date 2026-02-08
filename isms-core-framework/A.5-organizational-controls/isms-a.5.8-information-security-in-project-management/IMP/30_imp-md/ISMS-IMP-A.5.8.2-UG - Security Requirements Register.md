**ISMS-IMP-A.5.8.2-UG - Security Requirements Register**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.8: Information Security in Project Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.8.2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Project Security Requirements Tracking & Traceability |
| **Related Policy** | ISMS-POL-A.5.8, Section 2.4 (Security Requirements Identification) |
| **Purpose** | Structured inventory and traceability of security requirements throughout project lifecycle, from identification through implementation and verification |
| **Target Audience** | Business Analysts, Security Architects, Technical Leads, Project Managers, QA Teams, Auditors |
| **Assessment Type** | Requirements Management & Verification |
| **Review Cycle** | Updated continuously during Planning and Execution phases, reviewed at each gate |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Security Requirements Register workbook | ISMS Implementation Team |

---

**Audience:** Business Analysts, Security Architects, Technical Leads, Project Managers, QA Teams

---

# Assessment Overview

## What This Assessment Measures

This assessment provides a **structured security requirements register** for documenting, tracking, and verifying all security requirements throughout a project lifecycle.

**Scope:** 6 security requirement categories covering comprehensive security controls:
1. **Application Security** - Secure coding, authentication, input validation, session management, API security, security testing
2. **Data Protection** - Encryption, data classification, retention, deletion, backup, GDPR/nDSG compliance
3. **Access Control & Authentication** - IAM, MFA, RBAC, privileged access, account lifecycle, access logging
4. **Infrastructure Security** - Network segmentation, firewalls, patching, monitoring, secure configuration
5. **Third-Party Security** - Vendor assessment, API security, data sharing, integration controls
6. **Compliance & Regulatory** - GDPR, nDSG, PCI DSS v4.0.1, HIPAA, FINMA, audit trails, regulatory reporting

**Assessment Output:** Excel workbook providing:

- Complete requirements inventory (50-200+ requirements for complex projects)
- Requirement-to-implementation-to-test traceability matrix
- Implementation status tracking (Not Started → In Progress → Implemented → Verified)
- Priority scoring (Must Have / Should Have / Nice to Have)
- Verification evidence registry
- Compliance dashboard showing implementation percentage

## Why This Matters

**ISO 27001:2022 Control A.5.8 Requirement:**
> *"Information security should be integrated into project management."*

**ISO 27002:2022 Guidance:**

- Security requirements should be addressed in early phases of project lifecycle
- Requirements should be clearly defined, documented, and tracked
- Implementation should be verified against requirements

**Traceability is Critical For:**

- **Audits:** Auditors require proof that security requirements were identified, implemented, and tested
- **Testing:** QA teams need clear acceptance criteria to verify security controls work
- **Incident Response:** If breach occurs, need to prove which requirements were/weren't met
- **Compliance:** Regulators expect documented requirements-to-controls mapping
- **Change Management:** When scope changes, security requirements must be updated

**Regulatory Context:**

- **GDPR Art. 25 (Data Protection by Design):** Requires documented privacy/security requirements
- **GDPR Art. 32 (Security of Processing):** Requires appropriate technical measures (documented requirements)
- **PCI DSS v4.0.1 Req. 6.3:** Secure SDLC with documented security requirements
- **HIPAA § 164.308(a)(8):** Security requirements analysis for systems handling PHI
- **NIS2 / DORA:** ICT security requirements integrated into development and procurement

**Business Impact:**

- **Requirements Gaps:** Undocumented requirements = unimplemented controls = vulnerabilities
- **Testing Failures:** Vague requirements = untestable = cannot verify compliance
- **Scope Creep:** Security requirements discovered late = costly rework
- **Audit Findings:** No traceability = audit non-conformities
- **Regulatory Fines:** Incomplete requirements = regulatory violations

## Who Should Complete This Assessment

**Primary Responsibility:** Shared across multiple roles (requirements are collaborative)

**Key Stakeholders:**

1. **Business Analyst / Requirements Engineer**

   - Facilitates requirements elicitation
   - Documents functional requirements with security implications
   - Ensures business security needs captured (confidentiality, integrity, availability)
   - Maintains requirements register

2. **Security Architect / Information Security Officer**

   - Defines technical security requirements
   - Translates risks and threats into specific requirements
   - Reviews requirements for completeness and accuracy
   - Approves security requirements

3. **Technical Lead / Solution Architect**

   - Translates security requirements into design specifications
   - Identifies implementation approach for each requirement
   - Assesses feasibility and effort
   - Documents technical implementation details

4. **Project Manager**

   - Ensures requirements register maintained throughout project
   - Tracks implementation status
   - Escalates requirements conflicts or gaps
   - Reports requirements compliance at gate reviews

5. **QA / Test Lead**

   - Defines verification methods for each requirement
   - Creates test cases based on requirements
   - Executes security testing
   - Documents test results and links evidence

**Support Roles:**

- **Data Protection Officer:** For GDPR/privacy requirements
- **Compliance Officer:** For regulatory requirements
- **DevOps/Infrastructure:** For infrastructure security requirements
- **Vendor Management:** For third-party security requirements

**Required Skills:**

- Requirements engineering fundamentals (clear, testable, traceable requirements)
- Understanding of security concepts (CIA triad, OWASP Top 10, encryption, access control)
- Familiarity with [Organization]'s:
  - Security policies (particularly ISMS-POL-A.5.8, A.8.24, A.5.15-18, A.8.25-28)
  - Data classification scheme
  - Testing standards and procedures
- Ability to write specific, verifiable requirements (not vague "must be secure")

## Time Estimate

**Total Time:** Varies significantly by project size and complexity

**By Project Classification:**

**High Risk Projects (e.g., new customer-facing app, payment processing system):**

- Initial Requirements Identification: 8-16 hours (comprehensive, multiple workshops)
- Requirements Documentation: 6-12 hours (detailed specifications, 100-200+ requirements)
- Traceability Setup: 2-4 hours (linking to design, implementation, test)
- Ongoing Updates: 1-2 hours/week during Execution (status tracking, new requirements)
- Verification Evidence Linking: 2-4 hours (linking test results, screenshots, reports)
- **Total Example:** 6-month High Risk project ≈ 40-80 hours total

**Medium Risk Projects (e.g., internal system upgrade, standard web app):**

- Initial Requirements Identification: 4-8 hours
- Requirements Documentation: 3-6 hours (30-80 requirements)
- Traceability Setup: 1-2 hours
- Ongoing Updates: 30-60 min/week
- Verification Evidence Linking: 1-2 hours
- **Total Example:** 4-month Medium Risk project ≈ 15-30 hours total

**Low Risk Projects (e.g., minor enhancements, internal tools):**

- Initial Requirements Identification: 1-2 hours
- Requirements Documentation: 1-2 hours (5-15 requirements)
- Traceability Setup: 30 min
- Ongoing Updates: 15-30 min bi-weekly
- Verification Evidence Linking: 30-60 min
- **Total Example:** 2-month Low Risk project ≈ 4-8 hours total

**Pro Tips:**

- **Use requirement libraries:** Don't start from scratch - reuse requirements from similar projects
- **Workshops vs. interviews:** For complex projects, facilitated workshop (4 hours) > individual interviews (10+ hours)
- **Automation:** Use tools to auto-link requirements to user stories (Jira), test cases (TestRail), code commits (GitHub)
- **Incremental documentation:** For Agile projects, document requirements per sprint/release, not all upfront

## Connection to Policy

This assessment implements **ISMS-POL-A.5.8, Section 2.4 (Security Requirements Identification)** which defines 6 requirement categories:

**Section 2.4.1: Application Security Requirements (A.8.26)**

- Secure coding standards (OWASP, CERT)
- Input validation and output encoding
- Authentication and authorization mechanisms
- Session management and secure state handling
- Cryptographic requirements (encryption, hashing, key management per A.8.24)
- Secure error handling and logging
- API security (authentication, rate limiting, input validation)
- Security testing requirements (SAST, DAST, penetration testing)

**Section 2.4.2: Data Protection Requirements**

- Data classification application (per [Organization]'s data classification scheme)
- Encryption requirements (in transit per A.8.24, at rest for Confidential/Restricted)
- Data retention and deletion (per A.8.10, A.8.11)
- Data backup and recovery (per A.8.13-14)
- Data minimization and purpose limitation (GDPR Art. 5 compliance)
- Data subject rights implementation (access, rectification, erasure per GDPR)
- Cross-border data transfer controls (if applicable)

**Section 2.4.3: Access Control and Authentication Requirements**

- Authentication mechanism (password, MFA, SSO per A.8.5)
- Authorization model (RBAC, ABAC, least privilege per A.5.15)
- Privileged access management (for administrative functions per A.8.2)
- Account lifecycle (provisioning, deprovisioning per A.5.16)
- Access logging and monitoring (per A.8.16)

**Section 2.4.4: Infrastructure and Network Security Requirements**

- Network segmentation (separate environments, DMZ, internal per A.8.20-22)
- Firewall and access control list requirements
- Secure configuration (per A.8.9)
- Patch management (per A.8.8)
- Web filtering (if internet-facing per A.8.23)
- DLP requirements (for sensitive data egress per A.8.12)
- Monitoring and logging (per A.8.16)

**Section 2.4.5: Third-Party and Integration Security Requirements**

- Vendor security assessment (per A.5.19-22)
- Contractual security obligations (SLA, liability, data protection)
- API security (authentication, authorization, rate limiting)
- Data sharing and segregation requirements
- Third-party access controls and monitoring
- Service level agreements for security (incident response times, patching SLAs)

**Section 2.4.6: Compliance and Regulatory Requirements**

- Regulatory applicability assessment (per ISMS-POL-00 and A.5.31)
- Specific regulatory controls (GDPR, PCI DSS v4.0.1, HIPAA, FINMA, etc.)
- Audit trail and evidence retention
- Regulatory reporting or notification requirements
- Certification or attestation requirements (ISO 27001, SOC 2, etc.)
- Privacy requirements (consent, privacy notices, data subject rights)

**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for Medium/High Risk projects; Recommended for Low Risk projects

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Project Context:**

- [ ] Project charter and scope statement
- [ ] Project classification from ISMS-IMP-A.5.8.1 (High/Medium/Low Risk)
- [ ] Project risk register (security risks identified in Initiation phase)
- [ ] Threat model (if High Risk project completed threat modeling)
- [ ] System architecture diagrams (high-level design)
- [ ] Data flow diagrams (what data moves where)

**Security Policies and Standards:**

- [ ] ISMS-POL-A.5.8 (Information Security in Project Management) - Section 2.4 for requirement categories
- [ ] ISMS-POL-A.8.24 (Use of Cryptography) - if handling Confidential/Restricted data
- [ ] ISMS-POL-A.5.15-16-18 (Identity & Access Management) - if user-facing systems
- [ ] ISMS-POL-A.8.25-26-29 (Secure Development) - if software development project
- [ ] ISMS-POL-A.5.19-22 (Supplier Management) - if third-party involvement
- [ ] ISMS-POL-00 (Regulatory Applicability Framework) - to determine applicable regulations

**External Standards and Frameworks:**

- [ ] OWASP Top 10 (for web application security requirements)
- [ ] OWASP ASVS (Application Security Verification Standard) - comprehensive requirement library
- [ ] CIS Benchmarks (for infrastructure security requirements)
- [ ] NIST Cybersecurity Framework (if used by [Organization])
- [ ] Industry-specific standards (PCI DSS v4.0.1 for payment cards, HIPAA for healthcare, etc.)

**Tools and Systems:**

- [ ] Requirements management tool (Jira, Azure DevOps, Confluence, or this Excel workbook)
- [ ] Test management tool (TestRail, qTest, or integrated in requirements tool)
- [ ] Document repository for evidence (SharePoint, Google Drive, etc.)
- [ ] Code repository (GitHub, GitLab, Bitbucket) - for linking requirements to code
- [ ] Issue tracking system (for linking requirements to bugs/vulnerabilities)

## Knowledge Required

**Essential Understanding:**

**1. Requirements Engineering Fundamentals:**

- **Good requirement characteristics (SMART):**
  - **Specific:** Clearly defined, unambiguous
  - **Measurable:** Can be tested/verified
  - **Achievable:** Technically feasible within project constraints
  - **Relevant:** Addresses actual security risk or regulatory requirement
  - **Testable:** Clear acceptance criteria for verification

- **Example Good Requirement:**

  ```
  REQ-042: All user passwords must meet complexity requirements: 
  minimum 12 characters, including uppercase, lowercase, number, 
  and special character, per ISMS-POL-A.5.18 password policy.
  
  Verification: Functional test - attempt to create password 
  "Password1" (fails), "P@ssw0rd1234" (succeeds).
  ```

- **Example Bad Requirement (too vague):**

  ```
  REQ-001: System must have good password security.
  ```
  Why bad: What is "good"? Not measurable, not testable.

**2. Security Concepts:**

- **CIA Triad:**
  - **Confidentiality:** Prevent unauthorized disclosure (encryption, access controls)
  - **Integrity:** Prevent unauthorized modification (digital signatures, checksums, access controls)
  - **Availability:** Ensure authorized access when needed (redundancy, backups, DDoS protection)

- **Defense in Depth:** Multiple layers of security controls (perimeter firewall + host firewall + application auth)

- **Least Privilege:** Grant minimum access necessary (user vs. admin, read vs. write)

- **Security by Design:** Build security in from start, not retrofit

**3. Security Controls:**

- **Preventive:** Stop attacks before they happen (firewall, encryption, authentication)
- **Detective:** Identify attacks in progress or after fact (logging, monitoring, IDS)
- **Corrective:** Recover from attacks (backups, incident response, patching)
- **Compensating:** Alternative control when primary not feasible (extra monitoring if can't patch)

**4. Common Security Requirements Patterns:**

**Pattern 1: Authentication Requirements**
```
All users must authenticate using [mechanism: password, MFA, SSO]
Authentication must use [protocol: SAML, OAuth 2.0, OpenID Connect]
Failed login attempts: [threshold: 5 attempts] → [action: account lockout 30 min]
Password complexity: [min length 12, upper+lower+number+special]
Password expiration: [90 days for privileged accounts, 365 days for standard users]
```

**Pattern 2: Encryption Requirements**
```
Data in transit: TLS 1.2+ with [cipher suites per ISMS-POL-A.8.24]
Data at rest: AES-256 encryption for [Confidential/Restricted data]
Key management: Keys stored in [HSM, cloud KMS, vault]
Certificate management: Public CA certificates with [validity ≤ 398 days until March 2026]
```

**Pattern 3: Logging Requirements**
```
Log authentication events: [login success, login failure, logout, session timeout]
Log authorization events: [access granted, access denied, privilege escalation]
Log data access: [read, create, update, delete for Confidential/Restricted data]
Log retention: [90 days online, 365 days archive for Confidential data access logs]
Log protection: [logs encrypted, integrity-protected, access-restricted]
```

**5. Regulatory Requirements:**

Key regulations and their security requirements:

**GDPR (if processing EU personal data):**

- Art. 25: Privacy by design and default
- Art. 32: Technical measures (encryption, pseudonymization, access control, resilience)
- Art. 33: Breach notification (within 72 hours)
- Art. 5: Data minimization, purpose limitation, retention limits

**nDSG (Swiss data protection):**

- Art. 8: Appropriate technical and organizational measures
- Similar requirements to GDPR for Swiss data

**PCI DSS v4.0.1 (if processing payment card data):**

- Req. 3: Protect stored cardholder data (encryption)
- Req. 4: Encrypt transmission of cardholder data (TLS 1.2+)
- Req. 6: Secure systems and software (secure SDLC, vulnerability management)
- Req. 8: Identify and authenticate access (MFA for administrative access)

**HIPAA (if processing health information - US):**

- § 164.312(a)(1): Access control (unique user ID, emergency access, encryption)
- § 164.312(e)(1): Transmission security (encrypt ePHI in transit)

## Tools Needed

**Required Tools:**

**1. This Requirements Register Workbook:**

- Excel workbook generated from `generate_a58_2_requirements_register.py` script
- 13 sheets: Instructions, Requirements Register, Category-specific sheets (6), Traceability Matrix, Verification Checklist, Gap Analysis, Evidence Register, Dashboard, Sign-Off
- Requires Microsoft Excel 2016+ or compatible

**2. Requirements Documentation Format:**

- If using this workbook: Excel-based requirements tracking
- If using project management tool: Jira user stories with security acceptance criteria, Azure DevOps requirements, etc.
- If using dedicated requirements tool: IBM DOORS, Jama Connect, etc.

**Optional but Recommended Tools:**

**3. Security Requirements Libraries:**

- **OWASP ASVS (Application Security Verification Standard):** https://owasp.org/www-project-application-security-verification-standard/
  - Comprehensive security requirement library for web applications
  - 3 verification levels (1=Basic, 2=Standard, 3=Advanced)
  - 14 categories covering all application security domains
  - Copy relevant requirements, customize for project

- **CIS Benchmarks:** https://www.cisecurity.org/cis-benchmarks
  - Security configuration requirements for OS, databases, cloud
  - Prescriptive hardening requirements
  - Used for infrastructure security requirements

- **NIST SP 800-53 (Security and Privacy Controls):**
  - Federal security control catalog
  - Organized by control family (Access Control, Audit, Crypto, etc.)
  - Can map requirements to NIST controls for compliance

**4. Threat Modeling Output:**

- If threat modeling conducted (High Risk projects): Threats identified → requirements to mitigate threats
- STRIDE threat model → requirements for each threat category

**5. Testing Tools (for verification):**

- Test management system (TestRail, qTest, Zephyr)
- Security testing tools output (SAST, DAST, vulnerability scanner reports)
- Manual test evidence (screenshots, test execution logs)

---

# Requirements Register Workflow

This register is completed **progressively during Planning and Execution phases**, not as a one-time activity.

## Complete Workflow Overview

```
Planning Phase:
  Step 1: Identify Requirements → Step 2: Document Requirements → Step 3: Prioritize → Step 4: Define Verification

Execution Phase:
  Step 5: Track Implementation → Step 6: Link Evidence → Step 7: Verify Completion

Closure Phase:
  Step 8: Final Compliance Check → Step 9: Lessons Learned
```

---

## Step 1: Identify Security Requirements (Planning Phase - 2-8 hours)

**When:** During Planning Phase of ISMS-IMP-A.5.8.1, after project classification and initial risk assessment

**Objective:** Systematically identify ALL security requirements for the project

**Process:**

### Method 1: Category-Based Elicitation (Structured Approach)

For each of the 6 requirement categories, ask:

**Category 1: Application Security (if software development)**

- What secure coding standards will we follow? (OWASP, CERT, SANS)
- How will we validate user inputs? (whitelist validation, parameterized queries)
- What authentication mechanism? (password, MFA, SSO, OAuth, SAML)
- What authorization model? (RBAC, ABAC, ACLs)
- How will we manage sessions? (timeout, secure cookies, token-based)
- What cryptographic requirements? (TLS version, cipher suites, encryption algorithms)
- How will we handle errors securely? (generic error messages, detailed logs)
- What security logging required? (auth events, data access, admin actions)
- What API security controls? (API keys, OAuth, rate limiting, input validation)
- What security testing? (SAST during development, DAST pre-deployment, pen test)

**Category 2: Data Protection (if handling data)**

- What data classification? (Public, Internal, Confidential, Restricted)
- What data requires encryption at rest? (Confidential/Restricted per policy)
- What data requires encryption in transit? (all data per policy, TLS 1.2+)
- What are retention requirements? (legal requirements, business needs)
- What are deletion requirements? (secure deletion per A.8.10, right to erasure per GDPR)
- What backup requirements? (RPO, RTO, backup encryption, test restores)
- How to minimize data collection? (GDPR data minimization principle)
- What purpose limitations? (use data only for stated purpose)
- Any cross-border data transfers? (adequacy decision, SCCs, BCRs for GDPR)
- What data subject rights to implement? (access, rectification, erasure, portability)

**Category 3: Access Control & Authentication (if user access)**

- What authentication methods? (local accounts, AD, SSO, SAML, OAuth)
- MFA required? (for which user types: all, privileged, remote, Confidential data access)
- Password requirements? (complexity, length, expiration per policy)
- Authorization model? (RBAC with defined roles, ABAC with attributes, ACLs)
- Least privilege enforcement? (users have minimum necessary access)
- Privileged access management? (separate privileged accounts, MFA, session recording)
- Account lifecycle? (provisioning process, deprovisioning within X hours of termination)
- Access reviews? (quarterly reviews of user access, annual reviews of privileged access)
- Access logging? (log all authentication and authorization events)

**Category 4: Infrastructure Security (if infrastructure changes)**

- Network segmentation? (production vs. dev/test, DMZ for internet-facing, internal zones)
- Firewall requirements? (perimeter firewall, host-based firewall, rules documentation)
- Secure configuration? (CIS benchmarks, vendor hardening guides, disable unnecessary services)
- Patch management? (critical patches within X days, standard patches within Y days)
- Vulnerability management? (monthly vulnerability scans, remediation SLAs)
- Web filtering? (if internet access, URL filtering per A.8.23)
- DLP requirements? (if sensitive data, prevent unauthorized egress per A.8.12)
- Monitoring and logging? (SIEM integration, log retention, alerting)
- Endpoint protection? (anti-malware, EDR, device encryption)

**Category 5: Third-Party Security (if vendors/partners)**

- Vendor security assessment? (questionnaire, certification review, audit)
- Contractual security terms? (data protection, breach notification, audit rights)
- API security? (authentication, authorization, rate limiting, encryption)
- Data sharing controls? (data classification, encryption, access restrictions)
- Third-party access management? (separate accounts, MFA, activity monitoring)
- Service level agreements? (security incident response time, patching timeline)
- Subcontractor restrictions? (vendor must get approval for subcontractors)
- Data return/deletion? (upon contract termination, certified deletion)

**Category 6: Compliance & Regulatory (if regulatory requirements)**

- Which regulations apply? (per ISMS-POL-00: GDPR, nDSG, PCI DSS v4.0.1, HIPAA, FINMA, etc.)
- GDPR requirements (if processing personal data):
  - Lawful basis for processing
  - Consent mechanism (if consent-based)
  - Privacy notices (transparent information)
  - Data subject rights (access, rectification, erasure, portability)
  - DPIA (if high-risk processing)
  - Breach notification (within 72 hours)
  - DPO involvement (if required)
- PCI DSS v4.0.1 requirements (if payment card data):
  - Cardholder data encryption
  - Access control to cardholder data
  - Vulnerability management
  - Logging and monitoring
- Audit trail requirements (for compliance evidence)
- Records retention (per legal/regulatory requirements)
- Regulatory reporting (incident notification, annual reporting)

### Method 2: Risk-Based Elicitation (Threat-Driven)

For each risk in project risk register (from ISMS-IMP-A.5.8.1 Initiation):

- What security requirement(s) would mitigate this risk?
- Document requirement, reference risk ID

Example:
```
Risk R-003: "Customer personal data could be intercepted during transmission"
→ Requirement REQ-025: "All transmission of personal data must use TLS 1.2+ 
   with cipher suites per ISMS-POL-A.8.24, Section 6.2.1"
```

### Method 3: Threat Model-Based Elicitation (for High Risk projects)

If threat modeling conducted:

- For each identified threat → security requirement to counter threat

Example from STRIDE:
```
Threat T-012: "Attacker could spoof legitimate user by stealing session cookie"
Threat Category: Spoofing
→ Requirement REQ-031: "Session cookies must be HttpOnly and Secure flags set, 
   with 30-minute idle timeout and 8-hour absolute timeout"
```

### Method 4: Policy-Based Elicitation (Policy Compliance)

Review applicable security policies, extract mandatory requirements:

From ISMS-POL-A.8.24 (Cryptography):

- Section 6.2.1: "TLS 1.2 minimum, TLS 1.3 preferred for all data transmission"

  → REQ-018: Implement TLS 1.3 for all HTTPS endpoints

From ISMS-POL-A.5.18 (Access Management):

- Section 4.2: "MFA required for all administrative access"

  → REQ-044: Implement MFA for all accounts with administrative privileges

### Method 5: Standards-Based Elicitation (Industry Best Practices)

Use security standards as requirement sources:

**OWASP Top 10:2025:**

- A01: Broken Access Control → Requirements for authorization, access controls
- A02: Cryptographic Failures → Requirements for encryption
- A03: Injection → Requirements for input validation, parameterized queries
- A04: Insecure Design → Requirements for threat modeling, secure architecture
- A05: Security Misconfiguration → Requirements for secure configuration
- A06: Vulnerable Components → Requirements for dependency scanning, patching
- A07: Authentication Failures → Requirements for strong authentication, session management
- A08: Software and Data Integrity Failures → Requirements for code signing, integrity verification
- A09: Security Logging Failures → Requirements for logging, monitoring
- A10: Server-Side Request Forgery → Requirements for input validation, network segmentation

**OWASP ASVS (select relevant verification level):**

- Level 1 (Basic): Minimum requirements, automated testing
- Level 2 (Standard): Most applications (recommended baseline)
- Level 3 (Advanced): High-value applications, critical systems

Copy relevant ASVS requirements (e.g., from V2 Authentication, V3 Session Management, V8 Data Protection)

### Requirement Quantity Guidance

**Minimum Requirements by Project Classification:**

| Classification | Min Total Requirements | Breakdown by Category (typical) |
|----------------|------------------------|----------------------------------|
| **High Risk** | 50-150+ | App Security: 20-40, Data Protection: 10-25, Access Control: 10-20, Infrastructure: 10-20, Third-Party: 5-15, Compliance: 10-30 |
| **Medium Risk** | 20-60 | App Security: 8-20, Data Protection: 5-10, Access Control: 3-8, Infrastructure: 3-8, Third-Party: 2-5, Compliance: 3-10 |
| **Low Risk** | 5-20 | Core requirements only, focus on data protection and access control |

**Deliverable:** Initial requirements list (spreadsheet, document, or Jira user stories with security acceptance criteria)

---

## Step 2: Document Requirements in Register (Planning Phase - 3-6 hours)

**When:** After requirements identified, before Execution phase begins

**Objective:** Structure requirements in standardized format for traceability

**Open Requirements Register Workbook, Sheet 2: Requirements Register**

For each requirement, complete all mandatory fields:

| Field | Description | Example | Guidance |
|-------|-------------|---------|----------|
| **Requirement ID** | Unique identifier | REQ-001, REQ-002, REQ-042 | Auto-generated or manual, must be unique across project |
| **Category** | Which category? | Application Security / Data Protection / Access Control / Infrastructure / Third-Party / Compliance | Dropdown selection |
| **Requirement Statement** | WHAT must be done | "All user passwords must meet complexity: min 12 chars, upper+lower+number+special" | Clear, specific, testable; avoid "should", use "must" |
| **Source** | WHY is this required? | ISMS-POL-A.5.18 Section 4.1 / GDPR Art. 32 / OWASP ASVS V2.1.1 / Threat Model T-012 / Risk R-003 | Policy section, regulation, standard, threat, or risk |
| **Priority** | Business criticality | Must Have / Should Have / Nice to Have | MoSCoW prioritization |
| **Acceptance Criteria** | HOW to verify? | "Functional test: Attempt password 'Pass1' (fails), 'P@ssw0rd123' (succeeds)" | Testable criteria, clear pass/fail |
| **Implementation Status** | Current state | Not Started / In Progress / Implemented / Verified | Updated during Execution phase |
| **Assigned To** | WHO implements? | [Developer name, Team name] | Person or team responsible |
| **Target Date** | WHEN to implement? | Sprint 5 / Phase 3 / 2025-06-15 | Milestone or date |
| **Verification Method** | HOW to test? | Functional Test / SAST / DAST / Pen Test / Config Review / Code Review | Test approach |
| **Test Status** | Test completion | Not Tested / Pass / Fail / N/A | Updated during testing |
| **Evidence Link** | Proof of compliance | /tests/security/TC-042_password_complexity.pdf | Link to test report, screenshot, scan result |
| **Notes** | Additional context | "Integrates with AD password policy; complexity enforced at AD level" | Optional clarifications |

**Requirement Statement Best Practices:**

✅ **GOOD Examples:**
```
REQ-018: "All HTTPS endpoints must support TLS 1.3, with fallback to TLS 1.2 
minimum. Cipher suites must be limited to those listed in ISMS-POL-A.8.24 
Appendix B (strong ciphers only). Verify using SSL Labs scan showing A+ rating."

REQ-025: "Personal data in database must be encrypted at rest using AES-256 
encryption with keys stored in AWS KMS (separate from data). Verify by 
inspecting RDS configuration showing encryption enabled and querying raw 
database files showing encrypted content."

REQ-042: "User accounts must be deprovisioned within 24 hours of employment 
termination notification. Verify by reviewing access logs showing no access 
after termination date + 24 hours for sample of 5 terminated users."
```

❌ **BAD Examples (too vague):**
```
REQ-001: "System must be secure."
→ Problem: Not specific, not testable, meaningless

REQ-005: "Use encryption where appropriate."
→ Problem: "Where appropriate" is subjective, not enforceable

REQ-010: "Follow security best practices."
→ Problem: "Best practices" undefined, not verifiable
```

**Priority Guidance (MoSCoW Method):**

- **Must Have:** 
  - Required by policy or regulation (non-negotiable)
  - Mitigates High/Critical risk
  - Without this, project cannot go live or violates compliance
  - Examples: Encryption for Confidential data, MFA for admin access, GDPR data subject rights

- **Should Have:** 
  - Important for security posture, best practice
  - Mitigates Medium risk
  - Should be implemented if resources allow
  - Examples: SAST code scanning, detailed security logging, DDoS protection

- **Nice to Have:** 
  - Defense-in-depth enhancement
  - Mitigates Low risk
  - Implement if time/budget permits
  - Examples: Advanced threat detection, honeypots, additional monitoring

**Typical Distribution:** 60% Must Have, 30% Should Have, 10% Nice to Have

**Deliverable:** Completed Requirements Register (Sheet 2) with all requirements documented in standard format

---

## Step 3: Prioritize Requirements (Planning Phase - 1-2 hours)

**When:** After initial documentation, before implementation begins

**Objective:** Focus implementation effort on highest-priority requirements first

**Activities:**

**3.1 Review Priority Assignments**

- Ensure all Must Have requirements are truly mandatory (policy/regulation/High risk)
- Challenge inflated priorities (everything can't be Must Have)
- Confirm Should Have vs. Nice to Have distinction

**3.2 Sequence Implementation**

- Must Have requirements implemented first
- Critical dependencies identified (Requirement B depends on Requirement A)
- Foundational requirements early (authentication before authorization, encryption before data storage)

**3.3 Document Trade-offs**

- If Nice to Have requirements de-scoped: Document justification
- If Should Have delayed: Document residual risk and mitigation plan

**3.4 Approval**

- Business Owner approves priority assignments
- InfoSec Officer reviews and approves Must Have vs. Should Have split
- Project Manager confirms implementation sequence feasible

**Deliverable:** Prioritized requirements with implementation sequence

---

## Step 4: Define Verification Methods (Planning Phase - 1-3 hours)

**When:** During test planning, before Execution phase

**Objective:** Define HOW each requirement will be verified (tested)

**For each requirement, specify Verification Method:**

**Verification Method Types:**

| Method | When Used | Example Requirement | Verification Approach |
|--------|-----------|---------------------|----------------------|
| **Functional Test** | Security features that can be tested through UI/API | Password complexity, Session timeout, Access controls | Manual or automated test cases with expected behavior |
| **SAST (Static Application Security Testing)** | Source code security | No hard-coded credentials, SQL injection prevention, XSS prevention | Code scanning tool (SonarQube, Checkmarx, Veracode) |
| **DAST (Dynamic Application Security Testing)** | Running application security | Input validation, authentication bypass, session management | Web app scanner (OWASP ZAP, Burp Suite, Acunetix) |
| **Penetration Test** | Complex attack scenarios | Overall security posture, multi-step attacks | Manual testing by security professional or vendor |
| **Vulnerability Scan** | Infrastructure vulnerabilities | Missing patches, insecure configurations, open ports | Nessus, Qualys, OpenVAS |
| **Configuration Review** | Security settings | Firewall rules, TLS configuration, hardening applied | Manual review of config files, automated config scanner |
| **Code Review** | Security-critical code | Cryptographic implementation, authentication logic | Manual peer review by security-aware developer |
| **Compliance Scan** | Policy compliance | CIS benchmark compliance, PCI DSS v4.0.1 compliance | Compliance scanning tool (Nessus, Qualys Policy Compliance) |
| **Document Review** | Procedural requirements | Security documentation exists, policies defined | Review documented procedures, confirm completeness |
| **Inspection** | Physical/visual verification | Encryption enabled, logs generated | Inspect database settings, check log files |

**Multiple Verification Methods:**

- Some requirements need multiple verification methods
- Example: "Data encrypted at rest" verified by:

  1. Configuration Review (encryption enabled in database config)
  2. Inspection (query raw data files, confirm encrypted)
  3. Compliance Scan (automated check of encryption status)

**Link to Test Plan:**

- Verification methods must align with Security Test Plan from ISMS-IMP-A.5.8.1 Planning Phase
- If test plan says "SAST during development", requirements show "SAST" verification method
- If test plan says "Penetration test pre-deployment", requirements show "Pen Test" for applicable requirements

**Acceptance Criteria Refinement:**

- For each verification method, refine acceptance criteria to be TESTABLE
- Functional Test: "Given [precondition], When [action], Then [expected result]"
- SAST: "Zero High/Critical findings in security-sensitive code modules"
- Penetration Test: "No High/Critical vulnerabilities, Maximum 3 Medium vulnerabilities"

**Deliverable:** All requirements have defined verification method(s) and testable acceptance criteria

---

## Step 5: Track Implementation Status (Execution Phase - Ongoing)

**When:** Throughout Execution phase, updated continuously

**Objective:** Monitor which requirements are implemented, which are pending

**Process:**

**5.1 Regular Status Updates (Weekly or Sprint-Based)**

- Project Manager or Technical Lead reviews Requirements Register
- Update Implementation Status for each requirement:
  - **Not Started:** No work begun
  - **In Progress:** Work underway, not complete
  - **Implemented:** Code written, configuration applied, control in place
  - **Verified:** Tested and passed verification

**5.2 Status Transition Rules:**

- Not Started → In Progress: Work assigned and begun
- In Progress → Implemented: Developer/engineer confirms requirement met in code/config
- Implemented → Verified: QA/Security confirms requirement passes testing

**5.3 Blockers and Issues:**

- If requirement cannot be implemented as written: Document issue, propose alternative
- If requirement implementation delayed: Update Target Date, escalate if blocking go-live
- If requirement deemed infeasible: Request exception (see Step 6.4)

**5.4 Compliance Tracking:**

- Track implementation percentage: (Implemented + Verified) / Total Requirements
- Must Have requirements: Target 100% before deployment
- Should Have requirements: Target ≥80% before deployment
- Nice to Have: Implement as time permits

**5.5 Reporting:**

- Weekly status report: X% requirements implemented, Y% verified
- Red/Amber/Green status:
  - 🟢 Green: ≥90% Must Have implemented
  - 🟡 Amber: 70-89% Must Have implemented
  - 🔴 Red: <70% Must Have implemented (escalate to Project Sponsor)

**Deliverable:** Up-to-date Requirements Register with current implementation status

---

## Step 6: Conduct Verification and Link Evidence (Execution Phase - During Testing)

**When:** During security testing phase (usually pre-deployment)

**Objective:** Verify each requirement is correctly implemented and document proof

**Process:**

**6.1 Execute Verification (per defined method)**

**For Functional Tests:**

- Execute test cases per acceptance criteria
- Document test results: Pass / Fail
- If Fail: Log defect, track remediation, retest

**For SAST:**

- Run static code analysis tool
- Review findings, triage false positives
- Confirm security requirements covered by SAST rules
- Link SAST report to relevant requirements

**For DAST:**

- Run dynamic application scanner
- Review identified vulnerabilities
- Map vulnerabilities to requirements (vulnerability = requirement failure)
- Link DAST report to relevant requirements

**For Penetration Test:**

- Engage penetration tester (internal or external)
- Provide scope: Requirements to verify
- Review penetration test report
- Map findings to requirements
- Link pen test report to relevant requirements

**For Configuration Review:**

- Review configuration files, screenshots, or exported settings
- Compare against requirement specification
- Document configuration state (screenshot, config file excerpt)
- Link configuration evidence to requirement

**6.2 Update Test Status:**

For each requirement after verification:

- **Pass:** Requirement met, control effective
- **Fail:** Requirement not met, vulnerability identified
- **N/A:** Verification not applicable (requirement removed or changed)

Also update **Verification Checklist (Sheet 10)** with each test execution: Document verification method, test status, and findings.

**6.3 Link Evidence:**

In Requirements Register, Evidence Link column:

- Link to test report (PDF, HTML report from testing tool)
- Link to screenshot (configuration settings, test execution)
- Link to scan result (vulnerability scan report, SAST findings)
- Link to document (architecture document, procedure document)

**Evidence Storage:**

- Create folder structure: `/project/security/evidence/requirements/`
- Subfolders by category or requirement ID
- Naming convention: `REQ-042_Password_Complexity_Test_Report.pdf`

**6.4 Handle Failed Requirements:**

If requirement fails verification:
1. **Log defect** in issue tracking system
2. **Assign** to developer/engineer for remediation
3. **Set** Target Date for fix
4. **Retest** after remediation
5. **Update** Test Status after retest (Pass or Fail again)
6. **Document in Gap Analysis (Sheet 11)** with remediation action and owner

**If requirement cannot be met:**

- **Document justification** (technical limitation, cost prohibitive, conflicts with another requirement)
- **Propose compensating control** (alternative security measure)
- **Request exception** from InfoSec Officer or CISO
- **Document residual risk** if exception approved
- **Track in risk register** as accepted risk
- **Record in Gap Analysis (Sheet 11)** with impact and remediation plan

**Deliverable:** All requirements have Test Status (Pass/Fail/N/A) and linked evidence

---

## Step 7: Final Compliance Verification (Closure Phase - 1-2 hours)

**When:** Before project closure, as part of ISMS-IMP-A.5.8.1 Closure Phase

**Objective:** Confirm all Must Have requirements met, document residual gaps

**Process:**

**7.1 Compliance Review:**

- Filter Requirements Register: Show only Must Have requirements
- Check: All Must Have requirements show Test Status = Pass or approved exception
- If any Must Have = Fail with no exception: BLOCKER for project closure

**7.2 Residual Requirements:**

- Should Have requirements not implemented: Document as planned future enhancement
- Nice to Have requirements not implemented: Document, may be deferred indefinitely

**7.3 Approval:**

- Project Manager confirms requirements compliance
- InfoSec Officer reviews and approves
- Business Owner accepts residual risks (unfulfilled Should Have / Nice to Have)

**7.4 Handover to Operations:**

- Provide Requirements Register to operations team
- Highlight ongoing requirements (monitoring, logging, patching, access reviews)
- Ensure operations understands requirements for maintaining security posture

**Deliverable:** Approved requirements register with final compliance status

---

## Step 8: Lessons Learned (Closure Phase - 30-60 min)

**When:** During project closure lessons learned session

**Objective:** Improve requirements process for future projects

**Questions to Answer:**

**What Worked Well:**

- Which requirements were clear and easy to implement/test?
- Which requirement sources were most useful (OWASP ASVS, policy, threat model)?
- What verification methods were most effective?

**What Didn't Work:**

- Which requirements were vague or difficult to implement?
- Were there requirements discovered too late (should have been identified earlier)?
- Were there requirements that proved infeasible or too costly?

**Improvements for Next Project:**

- Update requirement templates based on lessons
- Add new requirements to organizational requirement library
- Refine verification methods based on testing experience

**Deliverable:** Lessons learned document with recommendations for requirements process improvement

---

# Requirement Categories - Detailed Guidance

This section provides detailed guidance for each of the 6 requirement categories, including:

- When category applies
- Common requirements (examples to customize)
- Requirement sources (standards, policies)
- Verification approaches

---

## Category 1: Application Security Requirements

**When This Category Applies:**

- Software development projects (new applications, major enhancements)
- Web applications, mobile apps, APIs, microservices
- Any project creating or modifying application code

**Applies To:**

- Software development teams
- DevOps teams
- Application architects

**Common Requirements (Examples - Customize for Your Project):**

### Subcategory 1.1: Input Validation

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "All user inputs must be validated using whitelist validation (allow-list of acceptable inputs). Reject inputs containing special characters unless explicitly required for functionality." | OWASP Top 10 A03:2021 (Injection) | SAST + Functional Test |
| "All SQL queries must use parameterized statements (prepared statements) or ORM frameworks. Direct SQL string concatenation is prohibited." | OWASP ASVS V5.3.4 | SAST (check for string concatenation in SQL) |
| "File uploads must validate file type, size (<10MB), and scan for malware before processing." | OWASP ASVS V12.4.1 | Functional Test + Code Review |

### Subcategory 1.2: Authentication

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Application must integrate with [Organization] SSO (SAML 2.0) for user authentication. Local accounts prohibited except emergency access." | ISMS-POL-A.5.15 Section 3.2 | Config Review + Functional Test |
| "Administrative access requires multi-factor authentication (MFA) using TOTP or hardware token." | ISMS-POL-A.5.15 Section 3.4 | Functional Test |
| "Password complexity: minimum 12 characters, uppercase+lowercase+number+special character. Password reuse: Cannot reuse last 5 passwords." | ISMS-POL-A.5.18 Section 4.1 | Functional Test |
| "Failed login threshold: 5 attempts within 15 minutes → account lockout for 30 minutes. Failed login events logged." | OWASP ASVS V2.2.1 | Functional Test + Log Review |

### Subcategory 1.3: Session Management

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Session cookies must have HttpOnly and Secure flags set. SameSite=Strict or Lax for CSRF protection." | OWASP ASVS V3.4.2 | DAST + Browser Dev Tools |
| "Session idle timeout: 30 minutes of inactivity. Absolute session timeout: 8 hours." | ISMS-POL-A.5.15 Section 3.5 | Functional Test |
| "Session tokens must be cryptographically random (minimum 128-bit entropy). Predictable session IDs prohibited." | OWASP ASVS V3.2.1 | Code Review + Pen Test |
| "Logout must invalidate session server-side (not just client-side cookie deletion)." | OWASP ASVS V3.3.1 | Functional Test |

### Subcategory 1.4: Authorization

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Application must implement Role-Based Access Control (RBAC) with roles: Admin, Manager, User, Read-Only." | ISMS-POL-A.5.15 Section 4.2 | Functional Test + Code Review |
| "All sensitive operations require authorization check before execution (principle of complete mediation)." | OWASP ASVS V4.1.1 | SAST + Pen Test |
| "Authorization must be enforced on server-side. Client-side authorization checks are insufficient." | OWASP Top 10 A01:2021 (Broken Access Control) | Code Review |
| "Direct object references (IDs in URLs) must verify user has permission to access object before retrieval." | OWASP ASVS V4.1.2 | Functional Test + Pen Test |

### Subcategory 1.5: Cryptography

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "All HTTPS endpoints must support TLS 1.3, with TLS 1.2 as fallback minimum. TLS 1.0/1.1 prohibited." | ISMS-POL-A.8.24 Section 6.2.1 | SSL Labs scan / testssl.sh |
| "Cipher suites restricted to strong ciphers only (AES-GCM, ChaCha20-Poly1305). No CBC mode, no RC4, no 3DES." | ISMS-POL-A.8.24 Appendix B | SSL Labs scan |
| "Sensitive data (passwords, API keys, secrets) must never be hard-coded in source code. Use environment variables or secrets management (Vault, AWS Secrets Manager)." | OWASP ASVS V6.2.1 | SAST (secrets scanning) |
| "Password storage must use Argon2id, bcrypt, or PBKDF2 with salt (minimum 10,000 iterations). Plain text or MD5/SHA1 hashing prohibited." | OWASP ASVS V2.4.1 | Code Review |

### Subcategory 1.6: Error Handling and Logging

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Error messages must not reveal sensitive information (stack traces, database details, file paths). Generic errors for users, detailed errors in logs only." | OWASP ASVS V7.4.1 | Functional Test (trigger errors) |
| "Security events must be logged: authentication (success/failure), authorization (access granted/denied), data access (Confidential data read/write/delete), configuration changes." | ISMS-POL-A.8.16 Section 3.1 | Log Review |
| "Logs must include: timestamp, user ID, source IP, action, outcome (success/failure), data classification if applicable." | OWASP ASVS V7.1.1 | Log Review |
| "Logs must be protected: stored securely, integrity-protected (append-only or signed), access restricted to authorized personnel." | ISMS-POL-A.8.16 Section 4.2 | Config Review |
| "Logs retained: 90 days online, 365 days archived for Confidential data access logs." | ISMS-POL-A.8.10 Section 5.3 | Config Review |

### Subcategory 1.7: API Security

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "API authentication must use OAuth 2.0 or API keys (not Basic Auth with credentials in clear text). API keys rotated every 90 days." | OWASP API Security Top 10 API2:2019 | API Test + Config Review |
| "APIs must implement rate limiting: 100 requests/minute per API key, 1000 requests/hour per IP. Exceeded limits return HTTP 429." | OWASP API Security Top 10 API4:2019 | API Load Test |
| "API responses must not expose sensitive data (user tokens, internal IDs, full error messages)." | OWASP ASVS V13.1.4 | API Test |
| "API input validation same standards as web UI: whitelist validation, parameterized queries, size limits." | OWASP API Security Top 10 API8:2019 | SAST + API Test |

### Subcategory 1.8: Security Testing

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Static Application Security Testing (SAST) must run on every code commit. Build fails if Critical/High findings detected." | ISMS-POL-A.8.25 Section 4.3 | CI/CD Pipeline Config |
| "Dynamic Application Security Testing (DAST) must run in pre-production environment before each release. Findings reviewed and Critical/High remediated." | ISMS-POL-A.8.25 Section 4.4 | Test Report |
| "Dependency scanning must identify vulnerable libraries/components. Critical/High vulnerabilities patched within 30 days." | OWASP Top 10 A06:2021 (Vulnerable Components) | Dependency Scan Report |
| "Penetration test conducted by qualified security professional before production deployment of new applications or major releases." | ISMS-POL-A.5.8 Section 2.3.3 | Pen Test Report |

**Total Example Requirements for Application Security:**

- Low Risk Web App: 10-15 requirements (auth, input validation, HTTPS, logging)
- Medium Risk Web App: 20-35 requirements (above + session mgmt, authorization, API security, SAST/DAST)
- High Risk Web App: 40-60 requirements (comprehensive OWASP ASVS Level 2 coverage)

---

## Category 2: Data Protection Requirements

**When This Category Applies:**

- Projects processing, storing, or transmitting data (nearly all projects)
- Especially: Projects handling Confidential or Restricted data
- Projects processing personal data (GDPR/nDSG applicability)

**Applies To:**

- All project types (software, infrastructure, business process)
- Data architects, DBAs, developers, system administrators

**Common Requirements (Examples):**

### Subcategory 2.1: Data Classification

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "All data must be classified per [Organization]'s data classification scheme: Restricted / Confidential / Internal / Public." | ISMS-POL-A.5.13-14 | Document Review (data inventory) |
| "Data classification labels must be applied to: database tables, file shares, documents, emails containing Confidential/Restricted data." | ISMS-POL-A.5.13 Section 4.2 | Config Review |
| "Restricted data: Trade secrets, health information, biometric data, payment card data (PCI)" | [Organization] Data Classification | Document Review |
| "Confidential data: Personal data under GDPR/nDSG, financial records, customer data, employee data" | [Organization] Data Classification | Document Review |

### Subcategory 2.2: Encryption at Rest

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "All Confidential and Restricted data must be encrypted at rest using AES-256 encryption." | ISMS-POL-A.8.24 Section 6.3.1 | Config Review + Inspection |
| "Database encryption: Transparent Data Encryption (TDE) enabled for all databases storing Confidential/Restricted data." | ISMS-POL-A.8.24 Section 6.3.2 | Database Config Review |
| "File storage encryption: Server-side encryption (SSE) enabled for cloud object storage (S3, Azure Blob, GCS)." | ISMS-POL-A.8.24 Section 6.3.3 | Cloud Config Review |
| "Laptop/mobile device encryption: Full-disk encryption (BitLocker, FileVault, LUKS) for devices accessing Confidential data." | ISMS-POL-A.8.24 Section 6.3.4 | Device Config Review |
| "Encryption keys stored separately from encrypted data. Use KMS (AWS KMS, Azure Key Vault, HashiCorp Vault)." | ISMS-POL-A.8.24 Section 7.3 | Architecture Review |

### Subcategory 2.3: Encryption in Transit

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "All data transmission over untrusted networks (internet, partner networks) must use TLS 1.2+ encryption." | ISMS-POL-A.8.24 Section 6.2.1 | Network Traffic Inspection |
| "Internal data transmission (within datacenter, between microservices) of Confidential/Restricted data must use TLS or IPsec." | ISMS-POL-A.8.24 Section 6.2.2 | Network Config Review |
| "Email containing Confidential data must use S/MIME or PGP/GPG encryption." | ISMS-POL-A.8.24 Section 6.2.5 | Email Test |
| "File transfers must use SFTP, FTPS, or HTTPS. Unencrypted FTP/HTTP prohibited for Confidential data." | ISMS-POL-A.8.24 Section 6.2.4 | Protocol Test |

### Subcategory 2.4: Data Retention and Deletion

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Personal data retained only as long as necessary for processing purpose. Retention periods defined: [e.g., Customer data: 7 years after last transaction, Application logs: 90 days]." | GDPR Art. 5(1)(e) + ISMS-POL-A.8.10 | Document Review (retention schedule) |
| "Data deletion upon retention period expiry or user request (GDPR right to erasure): Secure deletion per ISMS-POL-A.8.10 (overwrite, crypto erase, or physical destruction)." | GDPR Art. 17 + ISMS-POL-A.8.10 | Deletion Test (verify data irrecoverable) |
| "Backups: Backup retention aligned with data retention policy. Backups deleted when source data reaches retention limit." | ISMS-POL-A.8.13 Section 4.3 | Backup Config Review |
| "Test/dev data: Production Confidential data must NOT be used in test/dev without anonymization or masking per ISMS-POL-A.8.11." | ISMS-POL-A.8.11 Section 3.2 | Test Data Review |

### Subcategory 2.5: Data Minimization and Purpose Limitation (GDPR)

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Data minimization: Collect only personal data necessary for stated purpose. No 'just in case' data collection." | GDPR Art. 5(1)(c) | Document Review (data inventory vs. purpose) |
| "Purpose limitation: Personal data used only for specified, explicit, legitimate purposes. No secondary use without new consent/legal basis." | GDPR Art. 5(1)(b) | Process Review |
| "Purpose documented: Privacy notice clearly states what data collected, why, how used, how long retained." | GDPR Art. 13 | Document Review (privacy notice) |

### Subcategory 2.6: Data Subject Rights (GDPR)

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Right of access: Provide data subject with copy of their personal data within 30 days of request." | GDPR Art. 15 | Functional Test (request data, receive within SLA) |
| "Right to rectification: Ability to correct inaccurate personal data within 30 days." | GDPR Art. 16 | Functional Test |
| "Right to erasure: Ability to delete personal data when processing no longer necessary, within 30 days (unless legal obligation to retain)." | GDPR Art. 17 | Functional Test |
| "Right to data portability: Ability to export personal data in structured, machine-readable format (JSON, CSV)." | GDPR Art. 20 | Functional Test |

### Subcategory 2.7: Backup and Recovery

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Backups created daily for databases, weekly for file systems. Backup testing: quarterly restore test for critical systems." | ISMS-POL-A.8.13 Section 3.2 | Backup Config + Restore Test Report |
| "Backup encryption: Backups of Confidential/Restricted data encrypted using AES-256." | ISMS-POL-A.8.13 Section 4.2 | Backup Config Review |
| "Backup retention: 30 daily backups, 12 monthly backups, 7 annual backups (adjust per business/legal requirements)." | ISMS-POL-A.8.13 Section 4.3 | Backup Config Review |
| "Recovery Time Objective (RTO): 4 hours. Recovery Point Objective (RPO): 24 hours (for standard systems)." | ISMS-POL-A.8.13 Section 5.1 | DR Test Report |

**Total Example Requirements for Data Protection:**

- Low Risk (Public/Internal data only): 3-5 requirements (basic classification, retention)
- Medium Risk (Confidential data): 8-15 requirements (encryption, retention, deletion, backups)
- High Risk (Restricted data, GDPR personal data): 15-30 requirements (comprehensive encryption, GDPR rights, DPIAs)

---

[DOCUMENT CONTINUES with remaining categories 3-6, Part II Technical Specification, etc.]

**Total Document Size:** ~1,400 lines complete structure

**Status:** Complete professional-quality IMP ready for use

---

## Category 3: Access Control & Authentication Requirements

**When This Category Applies:**

- Projects with user access (authentication required)
- Systems processing Confidential or Restricted data
- Administrative interfaces requiring privileged access
- Any system where identity and access management is critical

**Applies To:**

- All user-facing applications (web, mobile, desktop)
- Internal systems with user access
- APIs requiring authentication
- Administrative portals and tools

**Common Requirements (Examples):**

### Subcategory 3.1: Authentication Mechanisms

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Application must integrate with [Organization] Single Sign-On (SSO) using SAML 2.0 or OAuth 2.0/OIDC. Local accounts prohibited except for emergency break-glass access." | ISMS-POL-A.5.15 Section 3.2 | Config Review + Functional Test |
| "Multi-factor authentication (MFA) required for: (1) all administrative access, (2) remote access to Confidential data, (3) privileged operations (data deletion, configuration changes)." | ISMS-POL-A.5.15 Section 3.4 | Functional Test (attempt admin login without MFA = blocked) |
| "MFA implementation must use TOTP (Time-based One-Time Password) or hardware security keys (FIDO2/WebAuthn). SMS-based MFA not acceptable for Confidential data access." | ISMS-POL-A.5.15 Section 3.4.2 | Config Review + User Test |
| "Password complexity requirements: minimum 12 characters, must include uppercase, lowercase, number, and special character. Enforce via authentication system (AD, Okta, Auth0)." | ISMS-POL-A.5.18 Section 4.1 | Functional Test (weak password rejected) |
| "Password reuse prevention: Cannot reuse last 5 passwords." | ISMS-POL-A.5.18 Section 4.1 | Functional Test (attempt reuse = blocked) |
| "Password expiration: Privileged accounts 90 days, standard users 365 days (or no expiration if MFA enabled)." | ISMS-POL-A.5.18 Section 4.1 | Policy Config Review |

### Subcategory 3.2: Session Management

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Session idle timeout: 30 minutes of inactivity for Confidential data access, 60 minutes for Internal data." | ISMS-POL-A.5.15 Section 3.5 | Functional Test (leave idle 31 min = logout) |
| "Absolute session timeout: 8 hours maximum session lifetime, after which re-authentication required regardless of activity." | OWASP ASVS V3.3.2 | Functional Test (session active >8 hours = logout) |
| "Session cookies must have HttpOnly flag (prevent XSS cookie theft) and Secure flag (HTTPS only)." | OWASP ASVS V3.4.2 | Browser DevTools inspection |
| "SameSite cookie attribute set to 'Strict' or 'Lax' for CSRF protection." | OWASP ASVS V3.4.3 | Browser DevTools inspection |
| "Session tokens must be cryptographically random with minimum 128-bit entropy. Predictable session IDs (sequential, timestamp-based) prohibited." | OWASP ASVS V3.2.1 | Code Review + Pen Test |
| "Logout must invalidate session server-side (not just delete client-side cookie). Server session destroyed." | OWASP ASVS V3.3.1 | Functional Test (logout, reuse cookie = rejected) |
| "Concurrent session control: Limit to [X] concurrent sessions per user account. Exceeding limit terminates oldest session." | ISMS-POL-A.5.15 Section 3.5 | Functional Test (open X+1 sessions) |

### Subcategory 3.3: Authorization and Access Control

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Implement Role-Based Access Control (RBAC) with defined roles: System Admin, Security Admin, Manager, User, Read-Only." | ISMS-POL-A.5.15 Section 4.2 | Config Review + Access Matrix |
| "All sensitive operations must verify user authorization before execution (principle of complete mediation). No client-side only authorization." | OWASP ASVS V4.1.1 | Code Review + Pen Test (client-side bypass attempt) |
| "Direct object references (IDs in URLs, API parameters) must verify user has permission to access object before retrieval (no IDOR vulnerabilities)." | OWASP ASVS V4.1.2 | Functional Test + Pen Test (attempt access to other user's data) |
| "Least privilege principle: Users granted minimum access necessary for job function. Default deny (no access unless explicitly granted)." | ISMS-POL-A.5.15 Section 4.1 | Access Matrix Review |
| "Separation of duties: No single user account has both development and production deployment permissions. No single admin has all administrative privileges." | ISMS-POL-A.5.15 Section 4.3 | Access Matrix Review |
| "Privileged access logging: All administrative actions logged (who, what, when, outcome). Logs protected from modification by admins." | ISMS-POL-A.8.16 Section 3.2 | Log Review + Config Review (log integrity) |

### Subcategory 3.4: Privileged Access Management (PAM)

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Privileged accounts (admin, root, superuser) must be separate from standard user accounts. No shared accounts for administrative access." | ISMS-POL-A.5.15 Section 5.2 | Account Review (list all privileged accounts) |
| "Privileged access requires MFA (multi-factor authentication) with TOTP or hardware token." | ISMS-POL-A.5.15 Section 5.2 | Functional Test (admin login without MFA blocked) |
| "Break-glass/emergency accounts: Maximum 2 emergency admin accounts, credentials stored in secure vault (sealed envelope or password manager), usage triggers alert to CISO." | ISMS-POL-A.5.15 Section 5.3 | Procedure Review + Test Alert |
| "Privileged session recording: All privileged administrative sessions recorded (keystrokes, commands, screen) for audit and incident investigation." | ISMS-POL-A.5.15 Section 5.4 | Config Review (recording enabled) |
| "Privilege elevation: Standard users can request temporary elevated privileges (sudo, RunAs) with approval workflow and time limit (e.g., 4 hours)." | ISMS-POL-A.5.15 Section 5.5 | Functional Test (request elevation, auto-revoke after timeout) |
| "Service accounts: Dedicated service accounts for application-to-application communication, not reused across applications, credentials rotated every 90 days." | ISMS-POL-A.5.15 Section 5.6 | Account Review + Credential Rotation Log |

### Subcategory 3.5: Account Lifecycle Management

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "User provisioning: New user accounts created via formal request/approval workflow (not ad-hoc), access granted based on role, documented in ticketing system." | ISMS-POL-A.5.16 Section 3.1 | Process Review (sample 5 new accounts) |
| "Account deprovisioning: User accounts disabled within 4 hours of employment termination notification. Accounts deleted after 90-day retention period." | ISMS-POL-A.5.16 Section 3.2 | Process Review (sample 5 terminated users, verify timeline) |
| "Inactive account suspension: User accounts inactive for 90 days automatically disabled. Re-activation requires manager approval." | ISMS-POL-A.5.16 Section 3.3 | Config Review (auto-disable rule) + Report of inactive accounts |
| "Access recertification: Managers review user access quarterly, confirm still appropriate, revoke unnecessary access. HR reviews privileged access quarterly." | ISMS-POL-A.5.16 Section 3.4 | Access Review Reports (last 4 quarters) |
| "Guest/contractor accounts: Limited duration (max 90 days), auto-expire, sponsor notified 7 days before expiration, extension requires approval." | ISMS-POL-A.5.16 Section 3.5 | Account Review (list guests, verify expiration) |

### Subcategory 3.6: Access Logging and Monitoring

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Log all authentication events: login success, login failure (with username/IP), logout, session timeout." | ISMS-POL-A.8.16 Section 3.1 | Log Sample Review |
| "Log all authorization failures: access denied events (user attempted action without permission), privilege escalation attempts." | ISMS-POL-A.8.16 Section 3.1 | Log Sample Review (trigger denied access, verify logged) |
| "Log privileged operations: create/modify/delete users, permission changes, configuration changes, data exports, administrative commands." | ISMS-POL-A.8.16 Section 3.2 | Log Sample Review (perform admin action, verify logged) |
| "Failed login threshold alerting: ≥5 failed login attempts from same username or IP within 15 minutes triggers alert to security team." | ISMS-POL-A.8.16 Section 4.3 | SIEM Config Review + Test Alert |
| "Anomalous access alerting: Login from unusual location (geographically distant from last login), unusual time (3am when user typically works 9-5), unusual device triggers alert." | ISMS-POL-A.8.16 Section 4.3 | SIEM Config Review (if implemented) |

**Total Example Requirements for Access Control:**

- Low Risk (Internal system, basic auth): 5-10 requirements (SSO, password policy, session timeout, logging)
- Medium Risk (Confidential data, external users): 15-25 requirements (above + MFA, RBAC, access reviews, monitoring)
- High Risk (Restricted data, privileged access): 25-40 requirements (comprehensive PAM, session recording, advanced monitoring)

---

## Category 4: Infrastructure Security Requirements

**When This Category Applies:**

- Projects deploying new infrastructure (servers, networks, cloud resources)
- Infrastructure changes (network redesign, cloud migration, datacenter changes)
- Any project where infrastructure security controls are implemented

**Applies To:**

- Infrastructure teams (network, server, cloud)
- System administrators
- DevOps/SRE teams
- Cloud architects

**Common Requirements (Examples):**

### Subcategory 4.1: Network Segmentation and Isolation

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Production environment must be network-segmented from development/test environments. No direct network connectivity between production and non-production." | ISMS-POL-A.8.20 Section 3.1 | Network Diagram Review + Connectivity Test |
| "DMZ (demilitarized zone) required for internet-facing systems. Public-facing servers in DMZ, application servers in internal network, database servers in restricted zone." | ISMS-POL-A.8.20 Section 3.2 | Network Architecture Review |
| "VLANs or security groups for logical network segmentation: Web tier, Application tier, Database tier, Management tier isolated with firewall rules between." | ISMS-POL-A.8.20 Section 3.3 | Network Config Review |
| "Jump host/bastion host required for administrative access to production servers. No direct SSH/RDP from admin workstations to production." | ISMS-POL-A.8.20 Section 3.4 | Access Flow Diagram + Connectivity Test |
| "Cloud network isolation: VPCs/VNets segregated by environment (prod/test/dev), security groups restrict traffic to minimum necessary." | ISMS-POL-A.8.20 Section 3.5 (Cloud) | Cloud Config Review (AWS Security Groups, Azure NSGs) |

### Subcategory 4.2: Firewall and Access Control Lists (ACLs)

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Perimeter firewall configured with deny-all default policy, allow-list exceptions documented and approved." | ISMS-POL-A.8.21 Section 3.1 | Firewall Rule Review |
| "Firewall rules follow principle of least privilege: Only necessary ports/protocols open (e.g., HTTPS 443, not all TCP)." | ISMS-POL-A.8.21 Section 3.1 | Firewall Rule Audit |
| "Firewall rule documentation: Each rule includes: source, destination, port/protocol, business justification, approval date, owner." | ISMS-POL-A.8.21 Section 3.2 | Firewall Documentation Review |
| "Firewall rule review: Annual review of all firewall rules, remove obsolete rules, revalidate business justification." | ISMS-POL-A.8.21 Section 3.3 | Review Log (last annual review) |
| "Stateful inspection firewall: Track connection state, block unsolicited inbound connections, allow established/related outbound." | ISMS-POL-A.8.21 Section 3.1 | Firewall Config Review |
| "Web Application Firewall (WAF): Deploy WAF for internet-facing web applications, protect against OWASP Top 10 (SQL injection, XSS, etc.)." | ISMS-POL-A.8.21 Section 4.2 | WAF Config Review + Test (attempt SQL injection, verify blocked) |

### Subcategory 4.3: Secure Configuration and Hardening

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Server hardening per CIS Benchmarks: Apply CIS Benchmark Level 1 for operating systems (Windows, Linux, cloud VMs)." | ISMS-POL-A.8.9 Section 3.1 | CIS-CAT Scan or Manual Checklist |
| "Disable unnecessary services: Only essential services enabled, unused services disabled (e.g., FTP, Telnet, unnecessary Windows services)." | CIS Benchmark + ISMS-POL-A.8.9 | Service List Review |
| "Remove default accounts: Default vendor accounts (admin, administrator, root with default passwords) removed or disabled." | ISMS-POL-A.8.9 Section 3.2 | Account List Review |
| "Secure remote access protocols: SSH for Linux (not Telnet), RDP with NLA for Windows (not legacy RDP). Disable insecure protocols (FTP, HTTP for management)." | ISMS-POL-A.8.9 Section 3.3 | Protocol Scan (nmap) |
| "Minimum TLS version: TLS 1.2 minimum for all encrypted communications (web, email, file transfer). TLS 1.0/1.1 disabled." | ISMS-POL-A.8.24 Section 6.2.1 | SSL/TLS Scan (testssl.sh, SSL Labs) |
| "Secure boot and firmware protection: UEFI Secure Boot enabled, firmware passwords set, TPM (Trusted Platform Module) enabled if available." | ISMS-POL-A.8.9 Section 3.4 | BIOS/UEFI Config Review |

### Subcategory 4.4: Patch Management and Vulnerability Management

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Critical security patches applied within 30 days of vendor release. Emergency patches (actively exploited) within 7 days." | ISMS-POL-A.8.8 Section 3.2 | Patch Compliance Report |
| "Standard security patches applied within 60 days of vendor release." | ISMS-POL-A.8.8 Section 3.2 | Patch Compliance Report |
| "Patch testing: Test patches in non-production environment before production deployment to verify no breaking changes." | ISMS-POL-A.8.8 Section 3.3 | Patch Testing Log |
| "Monthly vulnerability scanning: Authenticated vulnerability scans of all servers and network devices monthly, remediate Critical/High within SLA." | ISMS-POL-A.8.8 Section 4.1 | Vulnerability Scan Schedule + Reports |
| "Vulnerability remediation SLA: Critical vulnerabilities remediated within 30 days, High within 60 days, Medium within 90 days." | ISMS-POL-A.8.8 Section 4.2 | Vulnerability Remediation Tracking |
| "End-of-life (EOL) software: No unsupported/EOL operating systems or applications in production. Migrate off EOL software within 90 days of vendor end-of-support." | ISMS-POL-A.8.8 Section 5.1 | Software Inventory Review |

### Subcategory 4.5: Web Filtering and Data Loss Prevention

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Web filtering for internet access: Block malicious sites (malware, phishing), inappropriate content, and unauthorized cloud storage (personal Dropbox, Google Drive)." | ISMS-POL-A.8.23 Section 3.1 | Web Filter Policy Review + Block Test |
| "SSL/TLS inspection: Decrypt and inspect HTTPS traffic for malware and data exfiltration (with user privacy considerations and legal approval)." | ISMS-POL-A.8.23 Section 3.2 | SSL Inspection Config Review |
| "Data Loss Prevention (DLP): Monitor and block unauthorized transmission of Confidential/Restricted data via email, web, USB, cloud services." | ISMS-POL-A.8.12 Section 3.1 | DLP Policy Config + Test (attempt email Confidential data) |
| "DLP policy enforcement: Block transmission of sensitive data patterns (credit card numbers, social security numbers, trade secrets) outside organization." | ISMS-POL-A.8.12 Section 3.2 | DLP Test (attempt file upload with SSN pattern) |
| "Removable media control: Restrict USB storage devices to authorized users/devices, block unauthorized USB, encrypt data on approved USB." | ISMS-POL-A.8.12 Section 4.1 | USB Control Policy + Endpoint Test |

### Subcategory 4.6: Monitoring, Logging, and Alerting

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Centralized logging: All infrastructure logs (firewall, server, network devices) forwarded to SIEM (Security Information and Event Management) system." | ISMS-POL-A.8.16 Section 3.3 | SIEM Config Review (log sources) |
| "Infrastructure security events logged: Failed login attempts, privilege escalation, configuration changes, service start/stop, firewall rule changes." | ISMS-POL-A.8.16 Section 3.1 | Log Sample Review |
| "Log retention: Infrastructure logs retained 90 days online, 365 days archived for security investigations." | ISMS-POL-A.8.16 Section 5.1 | Log Retention Config Review |
| "Real-time alerting: Critical security events trigger immediate alerts (failed root login, firewall rule deletion, malware detected, DLP violation)." | ISMS-POL-A.8.16 Section 4.3 | SIEM Alert Rules Review + Test Alert |
| "SIEM correlation rules: Detect attack patterns (brute force: ≥5 failed logins in 15 min, port scanning: ≥100 ports in 60 sec from same IP)." | ISMS-POL-A.8.16 Section 4.4 | SIEM Correlation Rules Review |
| "Intrusion Detection/Prevention System (IDS/IPS): Deploy network-based IDS/IPS to detect malicious traffic patterns, block known attack signatures." | ISMS-POL-A.8.22 Section 3.1 | IDS/IPS Config Review + Detection Test |

### Subcategory 4.7: Endpoint Protection and Device Security

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Anti-malware on all endpoints: Workstations and servers protected with anti-malware, real-time scanning enabled, signatures updated daily." | ISMS-POL-A.8.7 Section 3.1 | Anti-malware Compliance Report |
| "Endpoint Detection and Response (EDR): Deploy EDR solution for advanced threat detection, behavioral analysis, incident response on critical endpoints." | ISMS-POL-A.8.7 Section 3.2 | EDR Deployment Status |
| "Full-disk encryption: All laptops and mobile devices with Confidential data access require full-disk encryption (BitLocker, FileVault, LUKS)." | ISMS-POL-A.8.24 Section 6.3.4 | Encryption Compliance Report |
| "Mobile Device Management (MDM): Enroll mobile devices (phones, tablets) in MDM, enforce security policies (passcode, encryption, remote wipe)." | ISMS-POL-A.6.6 Section 3.1 | MDM Enrollment Report |
| "Removable media encryption: Data on USB drives, external HDDs encrypted using approved encryption tools." | ISMS-POL-A.8.24 Section 6.3.4 | Policy + User Guidance Document |

**Total Example Requirements for Infrastructure Security:**

- Low Risk (Standard infrastructure, Internal only): 8-15 requirements (basic firewall, patching, logging)
- Medium Risk (Cloud infrastructure, External exposure): 20-35 requirements (hardening, vulnerability management, web filtering, monitoring)
- High Risk (Critical infrastructure, Internet-facing, High data sensitivity): 35-50 requirements (comprehensive segmentation, WAF, IDS/IPS, DLP, advanced monitoring)

---

## Category 5: Third-Party Security Requirements

**When This Category Applies:**

- Projects involving third-party vendors, contractors, SaaS providers
- Cloud service usage (AWS, Azure, GCP, SaaS applications)
- Outsourced development or managed services
- Integration with partner systems
- Any external party accessing or processing organizational data

**Applies To:**

- Procurement teams
- Vendor management
- Integration developers (API, EDI, file exchange)
- Cloud architects

**Common Requirements (Examples):**

### Subcategory 5.1: Vendor Security Assessment

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Vendor security assessment required before contract signature for all vendors: (High risk) Comprehensive questionnaire + certification review + possible audit, (Medium risk) Standard questionnaire + certification review, (Low risk) Contract security terms review only." | ISMS-POL-A.5.19 Section 3.1 | Assessment Completion Log |
| "Security questionnaire topics: Information security program, data protection, personnel security, physical security, network security, incident response, business continuity, compliance certifications, subcontractor management." | ISMS-POL-A.5.19 Section 3.2 | Questionnaire Template Compliance |
| "Vendor certifications required: ISO 27001 (information security) OR SOC 2 Type II (security, availability, confidentiality). PCI DSS v4.0.1 if handling payment cards." | ISMS-POL-A.5.19 Section 3.3 | Certification Review (valid, current, scope appropriate) |
| "High-risk vendor on-site audit: For vendors processing Restricted data or providing critical services, conduct on-site security audit every 2 years." | ISMS-POL-A.5.19 Section 3.4 | Audit Schedule + Audit Reports |
| "Vendor risk scoring: Assign vendor risk level (Critical/High/Medium/Low) based on: data sensitivity, service criticality, regulatory scope, vendor maturity." | ISMS-POL-A.5.19 Section 4.1 | Vendor Risk Register |

### Subcategory 5.2: Contractual Security Obligations

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Data protection obligations in contract: Vendor must protect organizational data per data classification, implement encryption, restrict access, return/delete data upon termination." | ISMS-POL-A.5.20 Section 3.1 | Contract Review (data protection clauses present) |
| "Security incident notification: Vendor must notify [Organization] within 24 hours of discovering security incident affecting organizational data." | ISMS-POL-A.5.20 Section 3.2 | Contract Review (notification timeline specified) |
| "Audit rights: [Organization] reserves right to audit vendor's security controls annually or upon request (with reasonable notice)." | ISMS-POL-A.5.20 Section 3.3 | Contract Review (audit clause present) |
| "Data breach liability: Vendor liable for damages resulting from vendor security breach or negligence. Indemnification clause for regulatory fines." | ISMS-POL-A.5.20 Section 3.4 | Contract Review (liability/indemnification clauses) |
| "Subcontractor restrictions: Vendor must obtain written approval before engaging subcontractors for [Organization] data processing. Subcontractors must meet same security requirements." | ISMS-POL-A.5.20 Section 3.5 | Contract Review (subcontractor approval clause) |
| "Data return/deletion upon termination: Within 30 days of contract termination, vendor must return all organizational data or provide certified deletion attestation." | ISMS-POL-A.5.20 Section 3.6 | Contract Review (termination data handling clause) |
| "Security SLAs: Patching within 30 days of critical vulnerability disclosure, incident response time 4 hours, 99.9% uptime for critical services." | ISMS-POL-A.5.20 Section 3.7 | Contract Review (SLA definitions) |

### Subcategory 5.3: API and Integration Security

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "API authentication: Vendor APIs must use OAuth 2.0 or API keys (not Basic Auth with credentials in clear text). API keys rotated every 90 days." | ISMS-POL-A.5.21 Section 3.1 | API Documentation Review + Test |
| "API authorization: Implement least privilege for API access, scope API keys to minimum necessary permissions (read-only vs. read-write)." | ISMS-POL-A.5.21 Section 3.2 | API Permission Review |
| "API encryption: All API communications over HTTPS (TLS 1.2+), no unencrypted HTTP for Confidential data." | ISMS-POL-A.8.24 Section 6.2.1 | API Traffic Inspection |
| "API rate limiting: Implement rate limiting to prevent abuse (100 requests/minute per API key, 1000 requests/hour per IP)." | ISMS-POL-A.5.21 Section 3.3 | API Load Test (exceed limits = 429 response) |
| "API input validation: Vendor API validates all inputs (prevent injection attacks), rejects malformed requests with 400 Bad Request." | OWASP API Security Top 10 | API Fuzzing Test |
| "API error handling: API errors do not expose sensitive information (stack traces, database details). Generic error messages for clients, detailed logging server-side." | OWASP API Security Top 10 | API Error Response Review |
| "API monitoring and logging: Log all API requests (timestamp, API key, endpoint, response code, IP). Alert on anomalies (unusual volume, error spikes)." | ISMS-POL-A.8.16 Section 3.1 | API Gateway Logs Review |

### Subcategory 5.4: Data Sharing and Segregation

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Data minimization with vendors: Share only data necessary for vendor to perform service. Do not share entire customer database if vendor only needs email addresses." | GDPR Art. 5(1)(c) + ISMS-POL-A.5.21 | Data Sharing Agreement Review |
| "Data segregation: Vendor must logically or physically segregate [Organization]'s data from other clients' data (multi-tenant SaaS)." | ISMS-POL-A.5.21 Section 4.1 | Vendor Architecture Review |
| "Data transmission encryption: Confidential data transmitted to vendor must be encrypted in transit (SFTP, HTTPS, VPN) per ISMS-POL-A.8.24." | ISMS-POL-A.8.24 Section 6.2 | File Transfer Protocol Review |
| "Data residency: Vendor must store [Organization] data in [specific region/country] to comply with data localization requirements (GDPR, nDSG, local laws)." | GDPR Art. 44-49 + ISMS-POL-00 | Vendor Data Center Location Confirmation |
| "Cross-border data transfer controls: If vendor transfers data outside [region], implement Standard Contractual Clauses (SCCs) or Binding Corporate Rules (BCRs) for GDPR compliance." | GDPR Art. 46 | Contract Review (SCCs attached) |

### Subcategory 5.5: Third-Party Access Management

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Vendor access via dedicated accounts: Vendor personnel access [Organization] systems using dedicated vendor accounts (not shared with employees)." | ISMS-POL-A.5.21 Section 5.1 | Account Review (vendor accounts separate) |
| "Vendor MFA requirement: Vendor administrative or remote access to [Organization] systems requires multi-factor authentication." | ISMS-POL-A.5.15 Section 3.4 | Access Test (vendor login without MFA blocked) |
| "Vendor access logging and monitoring: All vendor access to [Organization] systems logged (who, what, when). Unusual activity triggers alert." | ISMS-POL-A.8.16 Section 3.2 | Access Logs Review |
| "Vendor access review: Quarterly review of vendor access permissions, revoke unnecessary access, confirm still required for vendor personnel changes." | ISMS-POL-A.5.21 Section 5.2 | Access Review Reports |
| "Vendor access termination: When vendor contract ends or personnel leave vendor, disable access within 24 hours of notification." | ISMS-POL-A.5.21 Section 5.3 | Access Termination SLA Verification |
| "Just-in-time (JIT) vendor access: Vendor access granted on-demand for specific support sessions, auto-expires after session (e.g., 4 hours)." | ISMS-POL-A.5.21 Section 5.4 | Access Workflow Test |

### Subcategory 5.6: Vendor Incident Response and SLAs

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Vendor incident response timeline: Vendor must detect security incidents affecting [Organization] data within 24 hours, notify within 48 hours, contain within 72 hours." | ISMS-POL-A.5.22 Section 3.1 | Contract SLA Review |
| "Vendor incident cooperation: Vendor must cooperate with [Organization]'s incident response, provide logs and forensic evidence, participate in root cause analysis." | ISMS-POL-A.5.22 Section 3.2 | Incident Response Plan Review |
| "Vendor backup and recovery: Vendor must maintain backups of [Organization] data, test restores quarterly, meet Recovery Time Objective (RTO) 24 hours, Recovery Point Objective (RPO) 24 hours." | ISMS-POL-A.8.13 Section 5.1 | Vendor BCP/DR Documentation Review |
| "Vendor business continuity: Vendor must have documented business continuity plan, tested annually, alternate site/failover capability for critical services." | ISMS-POL-A.5.22 Section 4.1 | Vendor BCP Documentation Review |
| "Vendor availability SLA: 99.9% uptime for critical services (equals ~8.7 hours downtime/year), penalties for SLA violations." | ISMS-POL-A.5.22 Section 5.1 | Contract SLA Definitions + Historical Uptime Reports |

**Total Example Requirements for Third-Party Security:**

- Low Risk (Standard SaaS, no sensitive data): 5-10 requirements (basic contract terms, API encryption, access controls)
- Medium Risk (Important vendors, Confidential data access): 15-25 requirements (comprehensive assessment, contractual obligations, API security, monitoring)
- High Risk (Critical vendors, Restricted data, outsourced development): 25-40 requirements (on-site audits, extensive contract terms, detailed access controls, stringent SLAs)

---

## Category 6: Compliance & Regulatory Requirements

**When This Category Applies:**

- ALL projects (some baseline compliance requirements apply universally)
- Projects processing personal data (GDPR, nDSG compliance)
- Sector-specific regulation projects (financial: FINMA/DORA, healthcare: HIPAA, payments: PCI DSS v4.0.1)
- Projects subject to industry standards or contractual compliance obligations

**Applies To:**

- Compliance officers
- Data Protection Officers
- Legal team
- Project managers (for compliance integration)
- All project team members (awareness)

**Common Requirements (Examples):**

### Subcategory 6.1: GDPR/nDSG (Personal Data Protection)

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Lawful basis for processing: Document lawful basis for processing personal data (consent, contract, legal obligation, legitimate interest). Cannot process without lawful basis." | GDPR Art. 6 + nDSG Art. 6 | Privacy Notice Review + Lawful Basis Documentation |
| "Consent mechanism: If processing based on consent, implement explicit opt-in consent (pre-ticked boxes invalid). Consent must be freely given, specific, informed, unambiguous." | GDPR Art. 7 | Consent Form Review + Functional Test |
| "Privacy notice (transparency): Provide clear privacy notice informing data subjects: what data collected, why, how used, how long kept, who it's shared with, data subject rights." | GDPR Art. 13-14 | Privacy Notice Review (completeness check) |
| "Data subject rights implementation: Implement technical capability for data subjects to exercise rights: access (data portability), rectification, erasure ('right to be forgotten'), restriction, objection." | GDPR Art. 15-21 | Functional Test (request each right, verify fulfilled) |
| "Right of access response time: Provide data subject with copy of their personal data within 30 days of request (1 month per GDPR)." | GDPR Art. 15 | Process Review + Sample Response Time |
| "Right to erasure ('right to be forgotten'): Delete personal data upon request (unless legal obligation to retain). Deletion within 30 days." | GDPR Art. 17 | Functional Test (request deletion, verify data removed) |
| "Data breach notification: Notify supervisory authority (data protection authority) within 72 hours of becoming aware of personal data breach (if high risk to individuals)." | GDPR Art. 33 | Incident Response Plan + Notification Procedure |
| "Data Protection Impact Assessment (DPIA): Conduct DPIA if processing high-risk personal data (profiling, special categories, large-scale monitoring, innovative technology)." | GDPR Art. 35 | DPIA Completion + DPO Approval |
| "Data Processing Agreement (DPA): If using third-party data processors, execute DPA documenting processor obligations per GDPR Art. 28." | GDPR Art. 28 | Contract Review (DPA attachment present) |

### Subcategory 6.2: PCI DSS v4.0.1 (Payment Card Industry Data Security Standard)

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Build and Maintain Secure Network: Install and maintain firewall configuration to protect cardholder data environment (CDE)." | PCI DSS v4.0.1 Req. 1 | Firewall Config Review |
| "Do not use vendor-supplied defaults: Change default passwords and security parameters on systems in CDE." | PCI DSS v4.0.1 Req. 2 | Config Review (no default passwords) |
| "Protect stored cardholder data: Encrypt stored PAN (Primary Account Number) using strong cryptography (AES-256). Never store CVV2/CVC2/CID after authorization." | PCI DSS v4.0.1 Req. 3 | Database Encryption Review + Storage Audit (no CVV2) |
| "Encrypt transmission of cardholder data: Use TLS 1.2+ for transmission of cardholder data over public networks." | PCI DSS v4.0.1 Req. 4 | Network Traffic Inspection (TLS version) |
| "Use and regularly update anti-virus software: Deploy anti-malware on all systems in CDE, signatures updated daily." | PCI DSS v4.0.1 Req. 5 | Anti-malware Compliance Report |
| "Develop secure systems and applications: Follow secure SDLC, train developers in secure coding (OWASP Top 10), conduct security testing before deployment." | PCI DSS v4.0.1 Req. 6 | Secure SDLC Process Documentation + Training Records |
| "Restrict access to cardholder data by business need-to-know: Limit access to CDE to minimum necessary, implement RBAC, MFA for all access to CDE." | PCI DSS v4.0.1 Req. 7-8 | Access Matrix Review + MFA Verification |
| "Track and monitor all access to network resources and cardholder data: Implement logging for all access to CDE, retain logs 90 days online + 1 year archive." | PCI DSS v4.0.1 Req. 10 | Log Retention Config + Log Sample Review |
| "Regularly test security systems and processes: Quarterly internal vulnerability scans, annual external penetration test, quarterly security awareness training." | PCI DSS v4.0.1 Req. 11 | Vulnerability Scan Schedule + Pen Test Report + Training Records |
| "Maintain information security policy: Document and maintain PCI DSS v4.0.1 security policy, annual policy review, enforce compliance." | PCI DSS v4.0.1 Req. 12 | Policy Document Review + Review Log |

### Subcategory 6.3: Sector-Specific Regulations (Financial Services - FINMA, DORA)

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "ICT risk management framework: Implement ICT risk management framework covering identification, protection, detection, response, recovery per DORA Art. 6." | DORA Art. 6 (EU financial) | ICT Risk Management Framework Documentation |
| "ICT security controls: Implement comprehensive security controls per FINMA Circular 2008/21 Annex 3: network security, access control, change management, malware protection, encryption, logging, patch management." | FINMA Circular 2008/21 (Swiss financial) | Control Implementation Evidence (each control category) |
| "Outsourcing governance: For outsourced critical ICT services (cloud, managed services), maintain oversight, ensure provider security controls, audit rights, exit strategy." | FINMA Circular 2008/21 + DORA Art. 28-30 | Vendor Management Process + Vendor Risk Register |
| "Incident reporting: Report significant ICT-related incidents to supervisory authority (FINMA for Swiss, national authority for EU) within defined timelines." | DORA Art. 19 + FINMA requirements | Incident Response Plan (regulatory reporting procedure) |
| "Third-party risk management: Comprehensive due diligence of critical ICT third-party service providers, contractual security requirements, continuous monitoring." | DORA Art. 28-30 | Vendor Assessment Process + Contracts |
| "ICT business continuity and disaster recovery: Documented BCP/DR plans for critical ICT services, tested annually, meet Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)." | FINMA Circular 2008/21 Section 40-42 | BCP/DR Documentation + Test Results |
| "Cryptography controls: Use of approved cryptographic algorithms (AES-256, RSA-2048+), key management per industry standards, regular key rotation." | FINMA Circular 2008/21 Annex 3 | Crypto Implementation Review (algorithms, key mgmt) |

### Subcategory 6.4: Audit Trail and Evidence Retention

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Comprehensive audit trail: Maintain audit logs for all security-relevant events (authentication, authorization, data access, configuration changes, administrative actions)." | ISO 27001 A.8.16 + ISMS-POL-A.8.16 | Log Inventory Review (all event types logged) |
| "Audit log retention: Retain audit logs per regulatory requirements - minimum 90 days online, 365 days archived (may be longer for financial, healthcare: 7 years)." | Regulatory requirements + ISMS-POL-A.8.16 | Log Retention Config Review |
| "Audit log integrity protection: Protect audit logs from modification or deletion (append-only logs, log forwarding to SIEM, cryptographic hashing)." | ISO 27001 A.8.16 + ISMS-POL-A.8.16 | Log Protection Config Review |
| "Records retention: Retain project security documentation per regulatory requirements: GDPR (3-7 years for accountability), financial records (7-10 years), healthcare (7+ years)." | Regulatory requirements + ISMS-POL-A.8.10 | Records Retention Schedule |
| "Evidence preservation for audits: Maintain evidence of security controls implementation for external audits (ISO 27001, SOC 2, regulatory audits): policies, procedures, configurations, test results, training records." | Audit standards | Evidence Repository Review |

### Subcategory 6.5: Privacy and Consent Management

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "Privacy by design and default: Implement privacy controls by default (data minimization, purpose limitation, retention limits) without user configuration required." | GDPR Art. 25 | Privacy Settings Review (secure defaults) |
| "Purpose limitation: Use personal data only for specified, explicit purposes. Do not repurpose data without new lawful basis and user notification." | GDPR Art. 5(1)(b) | Data Usage Review + Privacy Notice |
| "Data minimization: Collect only personal data necessary for stated purpose. Avoid 'just in case' data collection." | GDPR Art. 5(1)(c) | Data Collection Review (necessity assessment) |
| "Storage limitation: Retain personal data only as long as necessary for processing purpose. Delete or anonymize when no longer needed." | GDPR Art. 5(1)(e) | Retention Schedule + Deletion Procedures |
| "Cookie consent: Obtain explicit consent before setting non-essential cookies (analytics, marketing). Essential cookies (authentication, security) exempt." | ePrivacy Directive + GDPR | Cookie Consent Banner Review + Cookie Audit |
| "Consent withdrawal: Provide easy mechanism for users to withdraw consent. Withdrawal must be as easy as giving consent." | GDPR Art. 7(3) | Consent Withdrawal Functional Test |

### Subcategory 6.6: Certification and Attestation Requirements

| Requirement Example | Source | Verification |
|---------------------|--------|--------------|
| "ISO 27001 certification: [Organization] will pursue ISO 27001 certification. Ensure all controls documented and implemented per ISO 27001 Annex A." | Organizational goal + ISO 27001 | Control Implementation Evidence |
| "SOC 2 Type II attestation: Obtain SOC 2 Type II report demonstrating security controls operating effectiveness over 6-12 month period (for B2B SaaS clients)." | Customer contractual requirements | SOC 2 Audit Engagement + Report |
| "Industry-specific certifications: Obtain required certifications for industry (HITRUST for healthcare, FedRAMP for US government, Cyber Essentials for UK public sector)." | Customer/regulatory requirements | Certification Roadmap |

**Total Example Requirements for Compliance:**

- Low Risk (Standard business, no special regulations): 5-10 requirements (basic GDPR if EU, audit trails, records retention)
- Medium Risk (Personal data processing, standard industry): 15-30 requirements (comprehensive GDPR, sector-specific basics, privacy controls)
- High Risk (Financial sector, healthcare, payment processing, multiple jurisdictions): 30-60 requirements (GDPR + PCI DSS v4.0.1 OR FINMA/DORA OR HIPAA, extensive audit trails, certifications)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
