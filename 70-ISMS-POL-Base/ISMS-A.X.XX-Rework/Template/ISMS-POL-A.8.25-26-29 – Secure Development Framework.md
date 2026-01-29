# ISMS-POL-A.8.25-26-29 – Secure Development Framework

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Secure Development Framework |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.25-26-29 |
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
| 1.0 | [Date] | CISO / Application Security Lead / Development Manager | Initial consolidated secure development framework |

**Review Cycle**: Annual (or upon significant SDLC methodology changes, regulatory updates, or major security incidents)  
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead
- Technical Review: Development Manager / Engineering Director
- Technical Review: QA Manager / Test Automation Lead
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (CEO)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.28 (Secure Coding)
- ISMS-POL-A.8.4 (Access to Source Code)
- ISMS-POL-A.8.31 (Separation of Development, Testing, and Production Environments)
- ISMS-POL-A.8.32 (Change Management)
- ISMS-IMP-A.8.25-26-29-S1 through S5 (Implementation Guides)
- ISMS-REF-A.8.25-26-29 (Security Testing Tools Reference)
- ISMS-CTX-A.8.25-26-29 (SDLC Security Evolution Context)
- ISO/IEC 27001:2022 Controls A.8.25, A.8.26, A.8.29

---

## Executive Summary

This policy establishes [Organization]'s Secure Development Framework, implementing ISO/IEC 27001:2022 Controls A.8.26 (Application Security Requirements), A.8.25 (Secure Development Lifecycle), and A.8.29 (Security Testing in Development and Acceptance) as a unified security framework.

**Scope**: This policy applies to all application development activities (new development, enhancements, security patches), all development methodologies (Waterfall, Agile, DevOps), all development models (internal, outsourced, hybrid), and all applications regardless of deployment model (on-premises, cloud, mobile).

**Purpose**: Define organizational requirements for secure software development throughout the software development lifecycle (SDLC). This policy establishes WHAT security practices are required, WHEN they must be applied, and WHO is accountable. Implementation procedures (HOW security is implemented) are documented separately in ISMS-IMP-A.8.25-26-29 Implementation Guides.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG (data protection by design), EU GDPR Article 25 (data protection by design and default), and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

**Why Secure Development Matters**: Software vulnerabilities represent one of the most significant security risks. Industry research shows that 84% of cyber attacks target the application layer, fixing security vulnerabilities in production costs 30x more than fixing them during design, and 70% of applications have at least one security vulnerability. This framework addresses these risks through systematic security integration throughout the SDLC.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control Statements

**ISO/IEC 27001:2022 Annex A.8.26 - Application Security Requirements**

> *Information security requirements should be identified, specified and approved when developing or acquiring applications.*

**ISO/IEC 27001:2022 Annex A.8.25 - Secure Development Lifecycle**

> *Rules for the secure development of software and systems should be established and applied.*

**ISO/IEC 27001:2022 Annex A.8.29 - Security Testing in Development and Acceptance**

> *Security testing processes should be defined and implemented in the development life cycle.*

### 1.2 Combined Control Framework Rationale

[Organization] implements these three controls as a unified framework because they represent sequential phases of a complete secure development process:

1. **Requirements Foundation (A.8.26)**: Security requirements must be specified BEFORE development begins
2. **Development Integration (A.8.25)**: Security must be integrated into HOW software is developed
3. **Verification & Validation (A.8.29)**: Security testing verifies THAT requirements are met

**Process Flow**:
```
A.8.26 Security Requirements → A.8.25 Secure Development → A.8.29 Security Testing
      ↓                              ↓                            ↓
  Requirements Spec            Secure SDLC Activities      Testing & Verification
  Threat Models               Secure Coding Standards       SAST/DAST/SCA/Pentest
  Architecture Review         Code Reviews                  Vulnerability Remediation
  Acceptance Criteria         Security Tools                Acceptance Testing
                                                                  ↓
                                                            FEEDBACK LOOP
```

**Implementation Synergy**: Combined approach eliminates redundant assessments, enables shared evidence collection (requirements, test results, remediation tracking), and provides unified security tool integration (SAST/DAST/SCA support multiple controls).

### 1.3 What This Policy Does

This policy:
- **Defines** security requirements specification process for applications
- **Establishes** secure development lifecycle integration requirements
- **Specifies** security testing requirements throughout development
- **Assigns** accountability for secure development governance
- **References** applicable regulatory requirements per ISMS-POL-00
- **Provides** framework for risk-based security implementation

### 1.4 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.8.25-26-29 Implementation Guides)
- **Define specific security testing tool configurations** (see ISMS-REF-A.8.25-26-29 Security Testing Tools Reference)
- **Provide step-by-step secure coding procedures** (see ISMS-POL-A.8.28 Secure Coding Policy and related implementation guides)
- **Select specific development tools or vendors** (technology selection based on [Organization]'s risk assessment)
- **Define detailed SDLC methodology procedures** (see ISMS-CTX-A.8.25-26-29 SDLC Security Evolution for awareness context)
- **Replace threat modeling or risk assessment** (security requirements determined through [Organization]'s risk assessment process)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving threat landscape and technology changes
- Technical agility for tool updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Methodology-neutral framework applicable to Waterfall, Agile, DevOps, or hybrid approaches

### 1.5 Scope

**This policy applies to**:

**Applications**:
- All internally developed applications (web, mobile, desktop, embedded)
- Applications under active development or enhancement
- Acquired applications requiring customization or integration
- Third-party applications integrated into organizational systems
- APIs and web services
- Infrastructure-as-Code (IaC) and configuration management code

**Development Activities**:
- New application development (greenfield projects)
- Application enhancements and feature additions
- Security patches and vulnerability remediation
- Application modernization and refactoring
- Cloud migration and cloud-native development

**Development Models**:
- Internal development teams
- Outsourced development (contractors, offshore teams)
- Hybrid development models
- Open-source contributions affecting organizational systems
- Low-code/no-code platforms (where security configuration is required)

**SDLC Methodologies**:
- Waterfall development
- Agile/Scrum
- DevOps/DevSecOps
- Iterative and incremental development
- Hybrid methodologies
- Continuous delivery and continuous deployment (CI/CD)

**Out of Scope**:
- Commercial Off-The-Shelf (COTS) software without customization (covered by vendor security assessment per ISMS-REF-A.5.23)
- Infrastructure management outside application code (covered by infrastructure security policies)
- Production vulnerability management post-deployment (covered by ISMS-POL-A.8.8 Vulnerability Management)
- Operational security monitoring of production applications (covered by ISMS-POL-A.8.15-16 Logging and Monitoring)

### 1.6 Control Integration Summary

**Control A.8.26 (Application Security Requirements)**:

**Purpose**: Establish security requirements specification process

**Key Requirements**:
- Application risk classification (High/Medium/Low)
- Security requirements specification for functional security, non-functional security, and data protection
- Threat modeling requirements (STRIDE or equivalent methodology)
- Security architecture review requirements
- Requirements traceability (requirements → design → code → tests)

**Detailed Requirements**: See Section 2

**Assessment Evidence**: Application inventory with risk classification, security requirements documentation per application, threat models, security architecture review reports, requirements traceability matrices

**Control A.8.25 (Secure Development Lifecycle)**:

**Purpose**: Integrate security throughout the software development lifecycle

**Key Requirements**:
- SDLC security framework (security activities in each phase)
- Secure coding standards (reference to ISMS-POL-A.8.28)
- Code review requirements (peer review + security-focused review)
- Security tools integration (SAST, SCA, secret scanning, IDE plugins)
- Secure development environment (workstation security, tool security)
- Developer security training
- Security defect management

**Detailed Requirements**: See Section 3

**Assessment Evidence**: SDLC security activity tracking, secure coding standard compliance, code review records, security tool deployment status, developer training records, security defect tracking data

**Control A.8.29 (Security Testing in Development and Acceptance)**:

**Purpose**: Validate security through comprehensive testing

**Key Requirements**:
- Security testing strategy (types, frequency, coverage)
- Static Application Security Testing (SAST)
- Dynamic Application Security Testing (DAST)
- Software Composition Analysis (SCA)
- Interactive Application Security Testing (IAST - where applicable)
- Penetration testing
- Security acceptance testing
- Vulnerability remediation workflows

**Detailed Requirements**: See Section 4

**Assessment Evidence**: Security testing tool configurations, SAST/DAST/SCA scan results and remediation records, penetration testing reports, security testing coverage metrics, vulnerability remediation tracking data

### 1.7 Integration with Other ISMS Controls

This Secure Development Framework integrates with other ISO 27001:2022 controls:

**A.8.28 (Secure Coding)**: Secure coding standards referenced in A.8.25 SDLC activities; coding standards enforced through code review and SAST

**A.8.4 (Access to Source Code)**: Source code access controls protect code repositories; integrated with development environment security

**A.8.31 (Separation of Environments)**: Development, test, staging, production separation; security testing conducted in non-production environments

**A.8.32 (Change Management)**: Security testing results integrated into change approval; security sign-off required for production deployment

**A.5.24-27 (Incident Management)**: Security vulnerabilities discovered in production trigger incident response; lessons learned improve secure development practices

**A.8.8 (Vulnerability Management)**: Production vulnerability management references development security controls; remediation follows secure development practices

---

## 2. Application Security Requirements (A.8.26)

### 2.1 Application Risk Classification

[Organization] SHALL classify all applications by risk level to determine appropriate security requirements.

**Risk Classification Criteria**:

**High-Risk Applications** meet ANY of these criteria:
- Processes or stores Confidential or Restricted data (per organizational data classification)
- Handles personally identifiable information (PII) subject to GDPR, FADP, or equivalent
- Processes payment card information (PCI DSS scope)
- Internet-facing (publicly accessible)
- Accessible by external third parties (customers, partners, suppliers)
- Critical business function (downtime causes significant business impact)
- Financial transaction processing
- Executes with elevated privileges or direct database write access

**Medium-Risk Applications** meet ANY of these criteria:
- Processes Internal Use data
- Limited PII exposure (names, email addresses only)
- Internal-only access (intranet, VPN-protected)
- Important but not critical business function
- Workarounds exist if application unavailable

**Low-Risk Applications** meet ALL of these criteria:
- Processes only Public data
- No PII, no sensitive business data
- Public information systems (read-only)
- Non-critical business function

**Risk Classification Process**:
- Product Manager/Application Owner completes risk classification
- Security Architect reviews and validates classification
- High-Risk: CISO approval required
- Medium-Risk: Security Architect approval required
- Low-Risk: Product Manager determination
- Classification reviewed annually or when application characteristics change

### 2.2 Security Requirements Specification Process

[Organization] SHALL specify security requirements for all applications based on risk classification.

**Process Requirements**:
1. **Gather Application Context**: Purpose, users, data types, deployment environment, technology stack, integration points, compliance requirements
2. **Identify Security Requirements**: Review requirements baseline, apply based on risk classification, consider threat landscape
3. **Conduct Threat Modeling**: Required for High-Risk (mandatory), Recommended for Medium-Risk
4. **Define Acceptance Criteria**: Translate requirements into testable criteria, define success metrics
5. **Document Requirements**: Structured Security Requirements Specification (SRS) document
6. **Obtain Approval**: Security Architect (Medium/High), CISO (High-Risk mandatory)

**Security Requirements Specification SHALL contain**:
- Application Overview (purpose, users, data, technology)
- Risk Classification (High/Medium/Low with justification)
- Functional Security Requirements (authentication, authorization, input validation, encryption, logging)
- Non-Functional Security Requirements (performance, resilience, secure defaults)
- Data Protection Requirements (encryption, retention, deletion, privacy)
- Security Testing Requirements (SAST, DAST, SCA, penetration testing)
- Security Acceptance Criteria (measurable success criteria)
- Threat Model (High-Risk mandatory, Medium-Risk recommended)
- Compliance Requirements (GDPR, PCI DSS, industry regulations)

**Requirements SHALL be**:
- Written in structured format (SHALL/SHOULD/MAY)
- Uniquely identified (e.g., SR-001, SR-002)
- Traceable to security controls and test cases
- Version-controlled
- Approved before implementation begins

### 2.3 Functional Security Requirements

[Organization] SHALL specify functional security requirements addressing:

**Authentication Requirements**:
- All Applications: Authentication for non-public functionality, strong password policies, account lockout, credential protection, secure session management
- High-Risk Applications: Multi-factor authentication (MFA) for privileged users, adaptive authentication, Single Sign-On (SSO) integration

**Authorization Requirements**:
- All Applications: Role-based access control (RBAC) or attribute-based access control (ABAC), principle of least privilege, deny access by default, server-side validation
- High-Risk Applications: Fine-grained authorization (resource-level, field-level), segregation of duties controls, authorization logging

**Input Validation Requirements**:
- All Applications: Validate all input from untrusted sources, whitelist validation, validate type/length/format/range, reject malicious patterns, sanitize input, server-side validation
- High-Risk Applications: Context-aware validation, output encoding, parameterized queries, anti-automation controls

**Cryptography Requirements**:
- All Applications: Encrypt data in transit (TLS 1.2+), use strong cipher suites, validate TLS certificates, encrypt sensitive data at rest
- High-Risk Applications: End-to-end encryption for highly sensitive data, cryptographic key management, hardware security modules (HSM) or key management services (KMS)
- See ISMS-POL-A.8.24 (Use of Cryptography) for detailed requirements

**Session Management Requirements**:
- All Applications: Cryptographically random session identifiers, session invalidation on logout, session timeout, session regeneration after authentication, secure cookie attributes
- High-Risk Applications: Concurrent session control, session binding, session logging

**Error Handling and Logging Requirements**:
- All Applications: Secure error handling (generic user messages), prevent information disclosure, log security-relevant events, protect logs from tampering, implement log retention
- High-Risk Applications: Centralized logging (SIEM integration), real-time monitoring and alerting, administrative action logging, audit trail for compliance
- See ISMS-POL-A.8.15-16 (Logging and Monitoring) for detailed requirements

**API Security Requirements** (where applicable):
- All Applications with APIs: API authentication, API authorization, API rate limiting, API input validation, API versioning
- High-Risk Applications with APIs: OAuth 2.0 or OpenID Connect, API gateway, API request signing, API response encryption, API call logging

**File Upload Requirements** (where applicable):
- All Applications: Validate file type, validate file size, scan for malware, store outside web root, generate random filenames, implement access controls
- High-Risk Applications: File content inspection, sandbox file processing, file encryption at rest, file upload logging

### 2.4 Non-Functional Security Requirements

[Organization] SHALL specify non-functional security requirements addressing:

**Security Performance Requirements**:
- All Applications: Maintain acceptable performance under security controls
- High-Risk Applications: Performance under attack scenarios (DDoS), performance monitoring for security controls

**Resilience Requirements**:
- All Applications: Fail securely (deny access on error), fail closed (reject invalid input), handle resource exhaustion gracefully
- High-Risk Applications: Circuit breaker patterns, rate limiting, graceful degradation, security monitoring for anomalies

**Secure Defaults Requirements**:
- All Applications: Secure default configuration (no default passwords, secure cipher suites), require explicit security changes, disable unused features, principle of least privilege in default configuration

### 2.5 Data Protection Requirements

[Organization] SHALL specify data protection requirements based on data sensitivity and regulatory requirements.

**Data Classification Requirements**:
- All Applications: Identify data types processed/stored, classify data per organizational policy, apply protection controls based on classification, document data flows

**Data Encryption Requirements**:
- High-Risk Applications: Encrypt Confidential and Restricted data at rest, encrypt in transit (TLS 1.2+), implement database encryption, encrypt backups, implement key management
- Medium-Risk Applications: Encrypt Confidential data in transit and at rest (passwords, credentials, sensitive PII)
- Low-Risk Applications: Encrypt credentials and secrets at rest

**Data Retention Requirements**:
- All Applications: Define retention periods per organizational policy and regulatory requirements, implement automated deletion after retention expires, document retention requirements, implement archival where required

**Data Deletion Requirements**:
- All Applications: Implement secure data deletion, support data subject rights (GDPR Article 17 - Right to Erasure), document deletion procedures, implement deletion verification
- High-Risk Applications: Audit trail for deletion, deletion automation, cascading deletion across systems
- See ISMS-POL-A.8.10 (Information Deletion) for detailed requirements

**Privacy Requirements** (for applications processing PII):
- All Applications: Privacy by design and by default (GDPR Article 25), minimize data collection, support data subject rights (access, rectification, erasure, portability, objection), implement consent management, document privacy impact assessment (PIA) for high-risk processing

### 2.6 Threat Modeling Requirements

[Organization] SHALL conduct threat modeling for High-Risk applications (mandatory) and Medium-Risk applications (recommended).

**Threat Modeling Process**:
1. **Define Scope**: Application boundaries, assets, trust boundaries
2. **Create Architecture Diagram**: Data flow diagram (DFD) with external entities, processes, data stores, data flows, trust boundaries
3. **Identify Threats**: Use STRIDE methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) or alternative
4. **Determine Countermeasures**: Identify security controls to mitigate threats, prioritize by risk
5. **Document Threat Model**: Architecture diagrams, threat enumeration, risk assessment, countermeasures, residual risks
6. **Review and Approve**: Security Architect reviews, CISO approves (High-Risk applications)

**Threat Model Maintenance**:
- Update when application architecture changes significantly
- Update when new threats emerge (security incidents, threat intelligence)
- Annual review for High-Risk applications
- Before major releases or feature additions

### 2.7 Security Architecture Review Requirements

[Organization] SHALL conduct security architecture review for High-Risk applications (mandatory) and Medium-Risk applications (recommended).

**Architecture Review Scope**:
- Application architecture diagrams (system context, component, deployment)
- Data flow diagrams (data flows, trust boundaries)
- Security controls architecture (authentication, authorization, encryption)
- Integration architecture (external systems, APIs, third-party services)
- Deployment architecture (infrastructure, network, cloud)

**Architecture Review Process**:
1. Schedule review after requirements specification, before development
2. Development team provides architecture documentation
3. Security Architect reviews documentation and conducts walkthrough
4. Security Architect identifies gaps and recommendations
5. Security Architect validates threat model alignment
6. Security Architect documents review report with findings, recommendations, approval status
7. Development team addresses gaps (High-severity mandatory, Medium/Low-severity as appropriate)
8. Security Architect approves architecture (CISO approval for High-Risk applications)
9. Architecture approval required before development phase begins

### 2.8 Third-Party Component Security Requirements

[Organization] SHALL specify security requirements for third-party components and open-source software.

**Third-Party Component Assessment**:
- All Applications: Identify all third-party components (libraries, frameworks, SDKs, APIs), assess security (CVE database, vendor track record), verify license compliance, document component inventory, implement update process
- High-Risk Applications: Conduct security assessment of critical components, implement Software Composition Analysis (SCA) for automated vulnerability detection, establish vendor security requirements, continuously monitor for new vulnerabilities

**Open-Source Software Security**:
- All Applications: Assess security before adoption, verify authenticity (checksum, signature), review code for critical components, monitor for vulnerabilities (SCA tools), contribute security fixes where applicable
- High-Risk Applications: Stricter approval process (Security Architect approval), assess community health, implement compensating controls for unmaintained components

**Third-Party Service Security** (for integrated services):
- All Applications: Assess service security posture (ISO 27001, SOC 2, security questionnaire), implement secure integration patterns, define security SLAs, implement monitoring, implement fallback mechanisms

### 2.9 Requirements Traceability

[Organization] SHALL maintain traceability from security requirements through implementation and testing.

**Traceability Requirements**:
- Security Requirement ID → Design Decision → Code Implementation → Test Case
- Security Control → Security Requirement → Test Case → Test Result
- Threat → Security Requirement → Mitigation Control → Test Validation

**Traceability Documentation**:
- Requirements Management Tool (Jira, Azure DevOps, etc.)
- Traceability Matrix (spreadsheet or database)
- Security Requirements Specification document
- Test Case Documentation

**Requirements Validation**:
- Complete: All security requirements identified and documented
- Correct: Requirements accurately reflect security needs
- Consistent: No conflicting requirements
- Testable: Requirements can be validated through testing
- Traceable: Requirements linked to threats, controls, tests

---

**[END OF PART 1]**

**Next Part 2 will contain**: Section 3 (Secure Development Lifecycle - A.8.25) and Section 4 (Security Testing - A.8.29)

**Checkpoint: Part 1 delivered - ~380 lines. Ready for Part 2?**
## 3. Secure Development Lifecycle (A.8.25)

### 3.1 SDLC Security Integration Requirements

[Organization] SHALL integrate security into all SDLC phases regardless of development methodology.

**SDLC Methodology Adaptation**:

This framework applies to all SDLC methodologies. [Organization] SHALL adapt security activities to the specific methodology in use:

**Waterfall**: Security gates at phase transitions, security sign-off before proceeding to next phase

**Agile/Scrum**: Security activities integrated into each sprint, security requirements in product backlog, security testing in Definition of Done (DoD)

**DevOps/DevSecOps**: Security automation in CI/CD pipeline, continuous security testing, Infrastructure-as-Code (IaC) security scanning

**Hybrid**: Combine security practices from multiple methodologies, maintain security rigor regardless of methodology

### 3.2 Security Activities by SDLC Phase

[Organization] SHALL implement security activities in each SDLC phase. The depth and rigor of activities scale with application risk classification (High/Medium/Low).

**Phase 1: Requirements**
- Classify application risk (High/Medium/Low)
- Specify security requirements based on risk classification
- Conduct initial threat identification
- Define security acceptance criteria
- Obtain security requirements approval
- **Security Gate**: Requirements approved before proceeding to Design

**Phase 2: Design**
- Conduct security architecture review
- Complete threat modeling (STRIDE or equivalent)
- Apply security design patterns
- Assess third-party components
- Document security design decisions
- **Security Gate**: Architecture approved before proceeding to Development

**Phase 3: Development**
- Apply secure coding standards (per ISMS-POL-A.8.28)
- Conduct code review (peer review + security-focused review for high-risk code)
- Use security tools (SAST, SCA, secret scanning, IDE plugins)
- Remediate security defects
- Track security technical debt
- **Security Gate**: Security defects below acceptable threshold before proceeding to Testing

**Phase 4: Testing**
- Execute security test cases
- Run SAST/DAST/SCA scans
- Conduct penetration testing (High-Risk applications)
- Perform security acceptance testing
- Verify security requirements implementation
- Remediate and retest vulnerabilities
- **Security Gate**: Security testing passed before proceeding to Deployment

**Phase 5: Deployment**
- Review production security configuration
- Complete deployment security checklist
- Configure security monitoring and alerting
- Validate encryption and access controls
- Enable security logging
- Conduct production security validation
- **Security Gate**: Production security validated before go-live

**Phase 6: Maintenance**
- Monitor for vulnerabilities
- Apply security patches
- Update threat model when changes occur
- Conduct periodic security assessments
- Respond to security incidents

### 3.3 Secure Coding Standards

[Organization] SHALL apply secure coding standards to all application development.

**Secure Coding Requirements**:
- All Developers: Follow organizational secure coding standards per ISMS-POL-A.8.28
- All Developers: Implement security requirements from A.8.26
- All Developers: Use security design patterns from architecture phase
- All Developers: Apply OWASP Top 10 prevention techniques

**Detailed secure coding standards are defined in ISMS-POL-A.8.28 (Secure Coding Policy).**

### 3.4 Code Review Requirements

[Organization] SHALL implement code review for all code changes.

**Peer Code Review** (All code):
- Reviewer: Team member (peer developer)
- Focus: Code quality, functionality, maintainability, basic security
- Timing: Before merge to main branch
- Coverage: 100% of code changes (no code merged without review)
- Documentation: Code review comments and approval in version control system

**Security-Focused Code Review** (High-risk code):
- Reviewer: Security Champion (trained developer) or Security Team member
- Focus: Security vulnerabilities, secure coding compliance, threat model alignment
- Checklist: Security code review checklist (OWASP, CWE, organizational standards)
- Timing: Before merge for critical code, or within sprint for high-risk features
- Documentation: Security review findings logged and tracked

**High-Risk Code Requiring Security Review**:
- Authentication and authorization logic
- Cryptography implementation
- Input validation and sanitization
- File upload and processing
- Payment processing
- PII processing
- API security controls
- Database access logic
- External system integration

### 3.5 Security Tools Integration

[Organization] SHALL deploy and use security tools during development.

**Static Application Security Testing (SAST)**:
- Purpose: Analyze source code for security vulnerabilities
- Deployment: Integrated into CI/CD pipeline
- Coverage: All code repositories
- Configuration: Enable security rule sets (OWASP Top 10, CWE Top 25), tune for language and framework, set failure thresholds
- Remediation: Critical/high findings MUST be fixed, medium/low findings tracked per SLA
- Tool selection: See ISMS-REF-A.8.25-26-29 (Security Testing Tools Reference)

**Software Composition Analysis (SCA)**:
- Purpose: Identify vulnerabilities in third-party dependencies
- Deployment: Integrated into CI/CD pipeline
- Coverage: All projects with third-party dependencies
- Configuration: Monitor all dependency manifests, alert on vulnerabilities (CVEs), check license compliance, recommend updates
- Remediation: Update dependencies to non-vulnerable versions, apply patches if available, accept risk if no fix available (with approval), remove obsolete dependencies
- Tool selection: See ISMS-REF-A.8.25-26-29 (Security Testing Tools Reference)

**Secret Scanning**:
- Purpose: Detect hardcoded secrets (passwords, API keys, tokens) in code
- Deployment: Pre-commit hooks and CI/CD pipeline
- Coverage: All code repositories
- Configuration: Scan for common secret patterns, block commits containing secrets (pre-commit hook), alert on secrets in repository history
- Remediation: Remove secrets from code immediately, rotate compromised secrets, store secrets in secure secret management system

**IDE Security Plugins**:
- Purpose: Real-time security feedback during coding
- Deployment: Recommended IDE plugins for all developers
- Benefits: Catch security issues before commit, educate developers in real-time, reduce findings in CI/CD pipeline

### 3.6 Security Defect Management

[Organization] SHALL track and remediate security defects systematically.

**Security Defect Tracking**:
- Track security defects separately from functional defects
- Classify by severity (Critical/High/Medium/Low) aligned with vulnerability classification
- Assign to developers for remediation
- Define remediation SLAs by severity:
  - Critical: 7 days
  - High: 30 days
  - Medium: 90 days
  - Low: 180 days
- Escalate overdue defects to development management and security team
- Track security technical debt (accepted defects not yet remediated)

**Security Defect Sources**:
- SAST scan findings
- SCA scan findings (vulnerable dependencies)
- Code review findings
- Security testing findings (DAST, penetration testing)
- Security incident root cause analysis
- Threat model updates

### 3.7 Developer Security Training

[Organization] SHALL provide security training for all developers.

**Initial Security Training** (All Developers):
- Timing: Before writing production code
- Duration: Minimum 4 hours
- Topics: Secure coding principles (OWASP Top 10, CWE Top 25), organizational secure coding standards (ISMS-POL-A.8.28), security tools usage, code review expectations, threat modeling basics, security incident reporting, defect remediation process
- Delivery: Instructor-led (preferred) or online training with hands-on exercises
- Assessment: Quiz or practical exercise
- Documentation: Training completion tracked and certificate retained

**Annual Security Training Refreshers** (All Developers):
- Duration: Minimum 2 hours annually
- Topics: Secure coding review, new vulnerabilities and attacks (past year), organizational security incidents and lessons learned, updated tools and processes, new requirements or regulations
- Delivery: Online training, webinars, lunch-and-learn sessions

**Security Champion Training** (Security Champions):
- Duration: Minimum 8 hours (initial) + 4 hours annually
- Topics: Advanced secure coding, security code review skills, threat modeling facilitation, security testing methodologies, security tool configuration and tuning, security mentorship and coaching
- Delivery: External training providers (SANS, OWASP, etc.), internal security team mentorship, security conferences

**Just-in-Time Security Training** (As Needed):
- Triggers: Critical vulnerabilities emerge (Log4Shell, etc.), new attack techniques identified, security incidents occur, new security tools deployed, new security requirements introduced
- Delivery: Security bulletins and alerts, emergency training sessions, internal wiki documentation, security team office hours

### 3.8 Security Champion Program

[Organization] SHOULD establish a Security Champion program.

**Security Champion Role**:
- Serve as security point-of-contact within development team
- Conduct security code reviews for high-risk code
- Facilitate threat modeling sessions
- Mentor team members on secure coding
- Advocate for security in development decisions
- Participate in security community of practice

**Security Champion Responsibilities**:
- Attend monthly Security Champion meetings
- Complete specialized security training
- Conduct security code reviews (10-20% of time)
- Stay current on security threats and best practices
- Report security concerns to security team
- Promote security culture within team

**Security Champion Selection**:
- Nominated by development management or self-nominated
- Approved by security team
- Passionate about security
- Respected by team members
- Willing to invest time in security activities
- Typical Ratio: 1 Security Champion per 10-15 developers

### 3.9 Secure Development Environment

[Organization] SHALL secure the development environment.

**Developer Workstation Security**:
- All Workstations: Endpoint protection (antivirus, EDR), full disk encryption, automatic security updates, strong authentication (password + MFA for VPN/corporate systems), screen lock, approved software only
- High-Risk Application Developers: Dedicated workstations for development (not shared with personal use), mobile device management (MDM) if developing on mobile devices, data loss prevention (DLP) controls

**Development Tool Security**:
- Approve development tools before use (IDE, libraries, frameworks)
- Verify tool authenticity (checksum, signature verification)
- Update tools regularly (security patches)
- Configure tools securely (disable unnecessary features, enable security features)
- Monitor tool vulnerabilities

**Source Code Repository Security**:
- Implement access controls (role-based access)
- Enable multi-factor authentication (MFA) for repository access
- Enable branch protection (prevent direct commits to main branch)
- Enable code review requirements (pull requests required)
- Enable audit logging (track all access and changes)
- Implement backup and disaster recovery
- Scan repositories for secrets (prevent hardcoded credentials)
- See ISMS-POL-A.8.4 (Access to Source Code) for detailed requirements

### 3.10 Outsourced and Third-Party Development

[Organization] SHALL apply secure development requirements to outsourced and third-party development.

**Contractual Requirements**:
- Security requirements included in contracts
- Secure coding standards compliance required
- Security testing requirements specified
- Security tool usage required (SAST, SCA)
- Security training requirements for developers
- Code review requirements
- Vulnerability remediation SLAs
- Security incident notification requirements

**Oversight and Validation**:
- Security architecture review (same as internal development)
- Code review (internal or third-party security review)
- Security testing (SAST, DAST, SCA, penetration testing)
- Source code escrow (for critical applications)
- Security assessment of third-party development environment

**Third-Party Developer Access**:
- Least privilege access to organizational systems
- MFA required for all access
- Access revoked upon contract termination
- Separate accounts from internal employees
- Audit logging of all third-party access

---

## 4. Security Testing Framework (A.8.29)

### 4.1 Security Testing Strategy

[Organization] SHALL define and implement security testing requirements based on application risk classification.

**Security Testing by Application Risk**:

**High-Risk Applications**:
- SAST (Static Application Security Testing): Per commit or daily
- DAST (Dynamic Application Security Testing): Per deployment or weekly
- SCA (Software Composition Analysis): Daily or continuous
- Penetration Testing: Annually minimum, or per major release
- Security Acceptance Testing: Before each production deployment

**Medium-Risk Applications**:
- SAST: Per commit or daily
- DAST: Monthly or per major release
- SCA: Daily or continuous
- Penetration Testing: Every 2 years, or per major release (recommended)
- Security Acceptance Testing: Before each production deployment

**Low-Risk Applications**:
- SAST: Per commit or weekly
- SCA: Weekly or per release
- DAST, Penetration Testing: Optional (risk-based decision)
- Security Acceptance Testing: Basic checklist before deployment

**Security Testing Types Overview**:
- SAST: Analyze source code for vulnerabilities (Development stage, per commit/daily)
- SCA: Identify vulnerable dependencies (Development stage, daily/continuous)
- DAST: Test running application for vulnerabilities (Pre-Production stage, per deployment/weekly)
- IAST: Runtime analysis during testing (Testing stage, continuous if deployed)
- Penetration Testing: Manual security testing by experts (Pre-Production stage, annually/per major release)
- Security Acceptance: Validate security requirements met (Pre-Production stage, per deployment)

**Tool selection guidance**: See ISMS-REF-A.8.25-26-29 (Security Testing Tools Reference)

### 4.2 Static Application Security Testing (SAST)

[Organization] SHALL implement SAST for all applications.

**SAST Deployment**:
- Deploy tools supporting organization's programming languages and frameworks
- Automate SAST scans in CI/CD build pipeline
- Provide IDE plugins for real-time developer feedback
- Scan all code repositories

**SAST Configuration**:
- Enable security rule sets (OWASP Top 10, CWE Top 25, language-specific rules)
- Tune for accuracy (balance false positives vs. false negatives)
- Set severity levels (Critical, High, Medium, Low)
- Configure for language/framework (ensure tool understands frameworks)

**SAST Results Management**:
- Triage findings (identify true positives vs. false positives)
- Classify true positives by severity
- Suppress false positives with documented justification
- Track false positive rate (goal: <20%)

**SAST Remediation**:
- Critical: Remediate within 7 days (block deployment if not fixed)
- High: Remediate within 30 days (block deployment if overdue)
- Medium: Remediate within 90 days (track as technical debt)
- Low: Remediate within 180 days or next major release

### 4.3 Dynamic Application Security Testing (DAST)

[Organization] SHALL implement DAST for High and Medium-Risk applications.

**DAST Deployment**:
- Deploy tools supporting web applications and APIs
- Deploy in staging/pre-production environments
- Configure credentials for authenticated testing
- Scan all web applications and APIs

**DAST Configuration**:
- Configure scan profiles (web app vs. API testing)
- Provide test credentials for authenticated scans
- Define scan scope (URLs/endpoints to scan, avoid production and third-party sites)
- Configure scan speed (avoid overwhelming application)
- Enable attack vectors (OWASP Top 10 tests, API security tests)

**DAST Scan Types**:
- Unauthenticated Scans: Test as unauthenticated user (public access), identify vulnerabilities in public pages
- Authenticated Scans: Test as authenticated user, identify vulnerabilities in protected functionality (Required for High-Risk applications)
- API Scans: Test API endpoints using API specification (OpenAPI/Swagger) for comprehensive testing (Required for High-Risk applications with APIs)

**DAST Remediation**:
- Critical: Remediate within 7 days (block deployment if not fixed)
- High: Remediate within 30 days (block deployment if overdue)
- Medium: Remediate within 90 days
- Low: Remediate within 180 days or next major release

### 4.4 Software Composition Analysis (SCA)

[Organization] SHALL implement SCA for all applications.

**SCA Deployment**:
- Deploy tools supporting package managers (npm, Maven, pip, NuGet, Bundler, Go modules, etc.)
- Automate dependency scanning in CI/CD build pipeline
- Monitor dependencies for new CVEs daily
- Scan all projects with third-party dependencies

**SCA Configuration**:
- Use multiple vulnerability databases (NVD, vendor advisories, GitHub Security Advisories)
- Define severity thresholds (acceptable vulnerability levels)
- Define license policies (allowed/forbidden licenses)
- Enable automated fix suggestions

**SCA Remediation**:
- Critical (CVSS 9.0-10.0): Update dependency within 7 days
- High (CVSS 7.0-8.9): Update dependency within 30 days
- Medium (CVSS 4.0-6.9): Update dependency within 90 days
- Low (CVSS 0.1-3.9): Update dependency within 180 days

**Dependency Update Strategies**:
1. Update to non-vulnerable version (preferred)
2. Apply patch (if available from vendor)
3. Replace dependency (use alternative library)
4. Accept risk (if no fix available and risk acceptable - requires approval)
5. Implement compensating controls (WAF rule, input validation)

### 4.5 Interactive Application Security Testing (IAST)

[Organization] MAY implement IAST for High-Risk applications.

**IAST Benefits**:
- Runtime analysis during testing
- Combination of SAST and DAST benefits
- Low false positive rate (validates exploitability)
- Detailed remediation guidance (code location, data flow)

**IAST Deployment** (if implemented):
- Deploy IAST agent in testing/staging environment (never production)
- Configure for application framework
- Integrate results into defect tracking system
- Monitor performance impact

### 4.6 Penetration Testing

[Organization] SHALL conduct penetration testing for High-Risk applications (mandatory) and Medium-Risk applications (recommended).

**Penetration Testing Requirements**:

**High-Risk Applications**:
- Frequency: Annually minimum
- Timing: Before major releases (recommended), after significant architecture changes (mandatory)
- Tester: External penetration testers (independent assessment preferred)

**Medium-Risk Applications**:
- Frequency: Every 2 years
- Timing: Before major releases (if budget permits)
- Tester: Internal or external

**Penetration Testing Scope**:
- Web application testing (OWASP Testing Guide methodology)
- API testing (authentication, authorization, input validation, rate limiting)
- Authentication testing (password policies, MFA, session management, credential stuffing)
- Authorization testing (privilege escalation, access control bypass)
- Business logic testing (business logic flaws unique to application)
- Infrastructure testing (if in scope - network, servers, databases)

**Penetration Testing Types**:
- Black Box: No knowledge of internals (simulates external attacker)
- Gray Box: Limited knowledge (documentation, credentials) - Most common, balanced approach
- White Box: Full knowledge (source code, architecture) - Most comprehensive, for High-Risk applications

**Penetration Testing Deliverables**:
- Executive Summary (high-level findings, risk summary, recommendations)
- Methodology (testing approach, tools used, scope)
- Findings (detailed descriptions, severity ratings, exploitation steps, evidence, recommendations)
- Technical Details (vulnerability details for development team)
- Remediation Guidance (step-by-step instructions)
- Retest Results (if applicable - verification of fixes)

**Severity Ratings**:
- Critical: Immediate risk of data breach or system compromise
- High: Significant security risk (authentication bypass, privilege escalation, sensitive data exposure)
- Medium: Moderate security risk (XSS, CSRF, information disclosure)
- Low: Minor security concerns (verbose errors, missing headers)

### 4.7 Security Acceptance Testing

[Organization] SHALL conduct security acceptance testing before production deployment.

**Security Acceptance Testing Validates**:
- Security requirements implemented correctly
- Security controls functioning as designed
- No critical or high-severity vulnerabilities remain
- Application meets security acceptance criteria

**Security Acceptance Testing Requirements**:

**Validate Security Requirements Implementation**:
- Review Security Requirements Specification (from Section 2)
- Test each security requirement
- Document test results (pass/fail)
- Obtain sign-off from Security Architect

**Verify Security Test Results**:
- Confirm SAST/DAST/SCA scans completed
- Verify critical/high vulnerabilities remediated
- Verify penetration testing completed (if required)
- Review open security defects and risk acceptances

**Execute Security Acceptance Test Cases**:
- Authentication testing (login, logout, password reset, MFA, session timeout)
- Authorization testing (access control enforcement, privilege escalation attempts)
- Input validation testing (injection attacks, file upload, parameter tampering)
- Cryptography testing (TLS configuration, data encryption, key management)
- Session management testing (session fixation, session hijacking, concurrent sessions)
- Error handling testing (error messages, no sensitive information disclosure)
- Logging testing (security events logged, log integrity)

**Obtain Security Sign-Off**:
- Security Architect reviews test results
- Security Architect approves deployment to production
- Sign-off documented and retained

### 4.8 Vulnerability Remediation Workflows

[Organization] SHALL establish vulnerability remediation workflows.

**Vulnerability Lifecycle**:
1. Identified: Vulnerability discovered by security testing
2. Triaged: Reviewed, severity assigned, assigned to developer
3. In Progress: Developer working on remediation
4. Fixed: Fix completed, awaiting verification
5. Verified: Fix verified by security testing (retest)
6. Closed: Vulnerability remediated and verified
7. Risk Accepted: Vulnerability accepted as residual risk (not fixed)

**Vulnerability Remediation Process**:
1. Identification: Security testing identifies vulnerability, documented in defect tracking system
2. Triage: Security team reviews vulnerability, validates true positive, assigns severity, prioritizes, assigns to developer, sets due date based on SLA
3. Remediation: Developer implements fix, tests fix, submits for code review, fix deployed to test environment
4. Verification: Security team or QA re-tests vulnerability, confirms fixed, updates status to Verified/Closed
5. Closure: Vulnerability marked closed, time to remediate calculated, lessons learned documented

**Remediation SLAs**:

| Severity | CVSS Score | Remediation SLA | Action if Overdue |
|----------|-----------|-----------------|-------------------|
| Critical | 9.0-10.0 | 7 days | Block deployment, escalate to CISO |
| High | 7.0-8.9 | 30 days | Block deployment, escalate to Development Manager |
| Medium | 4.0-6.9 | 90 days | Track as technical debt, plan remediation |
| Low | 0.1-3.9 | 180 days or next major release | Track as technical debt |

**SLA Exceptions**:
- SLA may be extended if: Fix requires significant refactoring, fix introduces breaking changes, fix awaits vendor patch (third-party vulnerability)
- Exception requires Security Architect approval
- Compensating controls required during exception period

### 4.9 Security Testing in CI/CD Pipeline

[Organization] SHALL integrate security testing into CI/CD pipeline.

**CI/CD Security Integration**:

**Commit Stage**:
- Pre-commit hooks: Secret scanning
- Commit triggers: SAST scan (for critical code paths)

**Build Stage**:
- SAST scan: Full scan on build
- SCA scan: Dependency vulnerability scan
- Secret scanning: Repository-wide scan
- Unit tests: Include security test cases

**Test Stage**:
- DAST scan: Scan application in test environment
- Integration tests: Include security integration tests
- Security acceptance tests: Execute automated security test suite

**Staging Stage**:
- DAST scan: Full scan (authenticated + unauthenticated)
- Penetration testing: Automated or manual (before production deployment)

**Production Deployment Gate**:
- Security sign-off required
- No critical/high vulnerabilities open (or risk accepted)
- Security acceptance testing passed

**Security Gates**:

**Build Security Gate**:
- Trigger: After SAST/SCA scan
- Criteria: No critical vulnerabilities, high vulnerabilities below threshold
- Action if failed: Block build, notify developer, create defect

**Test Security Gate**:
- Trigger: After DAST scan in test environment
- Criteria: No critical vulnerabilities, high vulnerabilities below threshold
- Action if failed: Block promotion to staging, notify security team

**Staging Security Gate**:
- Trigger: Before production deployment
- Criteria: Security acceptance testing passed, penetration testing completed (if required), no critical/high vulnerabilities open
- Action if failed: Block production deployment, require security sign-off

---

**[END OF PART 2]**

**Next Part 3 will contain**: Section 5 (Governance), Section 6 (Regulatory Framework), Section 7 (Roles), Annex, Approval

**Checkpoint: Part 2 delivered - ~380 lines. Ready for Part 3 (final)?**
## 5. Governance and Compliance

### 5.1 Assessment and Verification

[Organization] SHALL verify secure development control effectiveness through structured assessment.

**Assessment Domains**:
1. Security Requirements Compliance (A.8.26): Application risk classification, security requirements documentation, threat modeling, architecture review, requirements traceability
2. SDLC Security Activities (A.8.25): Security activities by phase, secure coding compliance, code review, security tool deployment, developer training, defect management
3. Security Testing Results (A.8.29): Testing coverage, SAST/DAST/SCA results, penetration testing, security acceptance testing
4. Vulnerability Remediation Tracking (A.8.29): Open vulnerabilities, remediation SLA compliance, vulnerability trends
5. Secure Development Maturity Dashboard: Consolidated metrics and gap analysis

**Implementation Note**: Assessment methodology, evidence requirements, workbooks, and compliance calculation procedures are defined in ISMS-IMP-A.8.25-26-29 (Implementation Guidance Suite). Assessment tools maintained separately from policy to enable frequent updates.

**Assessment Frequency**:
- Comprehensive assessment: Annually (aligned with internal audit programme)
- High-Risk applications: Quarterly verification (testing metrics, vulnerability tracking, compliance trends)
- Medium-Risk applications: Semi-annual verification
- Low-Risk applications: Annual verification
- Triggered assessment: Within 30 days of significant security incidents, major application changes, audit findings, regulatory changes

### 5.2 Exception Management

[Organization] SHALL manage exceptions to secure development policy requirements through formal approval process.

**Exception Request Requirements**:
- Documented business or technical justification
- Risk assessment (likelihood, impact, residual risk)
- Proposed compensating controls (where feasible)
- Timeline for achieving full compliance (where applicable)
- Formal approval per authority matrix

**Approval Authority**:
- Low-Risk applications: Security Architect approval
- Medium-Risk applications: CISO approval
- High-Risk applications: CISO approval + Risk Committee approval (for high-impact risks)

**Exception Process**:
1. Product Owner or Development Manager submits exception request documenting requirement not met, justification, risk assessment, compensating controls, duration/remediation plan
2. Security Architect reviews exception request and assesses risk
3. Appropriate authority approves or denies exception
4. Exception documented and tracked in exception register
5. Exceptions reviewed quarterly for continued validity

**Risk Acceptance**:
- Residual risks may be accepted when security controls reduce risk to acceptable level, remaining risk is within organizational risk appetite, cost of additional controls exceeds benefit
- Risk acceptance requires Security Architect documentation, Product Owner and Security Architect assessment, CISO acceptance (or escalation to Risk Committee for high-impact risks)
- Accepted risks documented in risk register and reviewed annually

### 5.3 Incident Response

[Organization] SHALL respond to secure development security incidents.

**Secure Development Security Incidents** include:
- Critical vulnerabilities discovered in production (indicates testing gaps)
- Security defect SLA violations (systemic remediation failures)
- Hardcoded secrets discovered in code repositories
- Third-party component vulnerabilities with active exploitation
- Failed security gate bypasses
- Security tool tampering or circumvention attempts

**Response Process**:
1. Detection & Reporting: Incident identified, security team notified
2. Assessment: Incident classification based on severity and impact
3. Investigation: Root cause analysis, scope determination
4. Containment: Immediate actions (patch deployment, access restriction, secret rotation)
5. Recovery: System restoration, preventive measures implementation
6. Post-Incident: Lessons learned, control improvements, policy/process updates

**Critical Incidents**: Production vulnerabilities with active exploitation treated as high-priority security incidents requiring immediate emergency response and patch deployment.

**Detailed Procedures**: ISMS-IMP-A.8.25-26-29 Implementation Guides provide incident classification criteria, response workflows, escalation procedures, and coordination with application security and operations teams.

### 5.4 Policy Governance

**Policy Review**:
- Frequency: Annual minimum
- Triggers: Regulatory changes, major security incidents, significant threat landscape changes, organizational changes (new SDLC methodologies, technology stack changes), audit findings
- Reviewers: CISO, Application Security Team, Development Management, Legal/Compliance
- Approval: CISO (technical), Executive Management (strategic)

**Implementation Standards Review**:
- Frequency: Based on threat landscape and technology evolution (at least semi-annual)
- Authority: Security Team proposes updates, CISO approves
- Note: Implementation standard updates (ISMS-IMP-A.8.25-26-29) do not require policy revision

**Policy Updates**:
- Minor (clarifications, references, examples): CISO approval, communication within 30 days
- Major (scope changes, new requirements, methodology changes): Full approval chain, implementation timeline per change management
- Emergency (critical threats, zero-day vulnerabilities): CISO approval, immediate communication and implementation

**Communication**: Policy published in ISMS document repository. Changes communicated organization-wide through development management, security team, and training updates. Training provided for significant changes affecting developer responsibilities or processes.

### 5.5 Continuous Improvement

[Organization] SHALL implement continuous improvement for secure development practices.

**Improvement Process**:
1. Analyze Assessment Results: Identify compliance gaps, common deficiencies, root causes
2. Prioritize Improvements: By risk (High-Risk applications first), by impact (improvements benefiting multiple applications), by effort (quick wins vs. long-term initiatives)
3. Develop Improvement Plan: Define actions (specific, measurable, achievable), assign responsibility, set completion dates, allocate resources
4. Execute Improvement Plan: Application owners implement improvements, Security Team provides guidance, track progress, escalate delays
5. Validate Improvements: Re-assess applications, verify compliance improvement, document lessons learned, update methodology if needed
6. Share Best Practices: Document successes, share across teams, update standards and templates, conduct training sessions

**Continuous Monitoring**:
- Daily: Vulnerability dashboards, security testing execution
- Weekly: Compliance trends, remediation progress
- Monthly: Portfolio-wide metrics, executive dashboard
- Quarterly: Comprehensive assessment results

---

## 6. Regulatory Framework

This section identifies legal and regulatory requirements relevant to secure software development, organized per ISMS-POL-00 (Regulatory Applicability Framework).

### 6.1 Mandatory Compliance (Tier 1)

**ISO/IEC 27001:2022**:
- Applicability: Organizations seeking or maintaining ISO 27001 certification
- Controls: A.8.25 (Secure Development Lifecycle), A.8.26 (Application Security Requirements), A.8.29 (Security Testing in Development and Acceptance)
- Requirements: Documented policies, procedures, evidence of implementation
- Audit Evidence: This framework, implementation guides, assessment workbooks, security testing results

**Swiss Federal Data Protection Act (FADP/nDSG)**:
- Applicability: All operations based in or serving Switzerland
- Article 8: Appropriate technical and organizational measures for data protection
- Article 26: Security by design and by default
- Impact: Applications processing personal data must implement security by design (privacy requirements in specifications, data protection controls in development, privacy testing and validation)

**EU General Data Protection Regulation (GDPR)**:
- Applicability: When processing personal data of EU residents
- Article 25: Data protection by design and by default
- Article 32: Security of processing (encryption, pseudonymization, resilience testing)
- Impact: Security requirements must include data protection impact assessment (DPIA) for high-risk processing, development must implement privacy-enhancing technologies, testing must validate encryption, access controls, and data subject rights

### 6.2 Conditional Compliance (Tier 2)

**DORA (Digital Operational Resilience Act)**:
- Applicability: If organization is an EU financial entity (credit institutions, payment institutions, investment firms, crypto-asset service providers)
- Article 9: ICT risk management framework including secure software development
- Article 24: Digital operational resilience testing
- Impact: Security requirements specification mandatory (Article 9.2.a), secure development lifecycle mandatory (Article 9.2.b), security testing mandatory including penetration testing (Article 24), third-party software security assessment mandatory (Article 28)

**NIS2 Directive (Network and Information Security)**:
- Applicability: If organization is an essential or important entity under NIS2 (energy, transport, health, digital infrastructure)
- Article 21: Cybersecurity risk management measures
- Impact: Security measures include secure development practices, supply chain security (third-party development), incident management for security vulnerabilities

**FINMA Circular 2023/1 (Swiss Financial Institutions)**:
- Applicability: If organization is a Swiss financial institution supervised by FINMA
- Margin 50-62: Information security including secure development
- Impact: Security requirements for financial applications, secure development practices for critical systems, security testing before production deployment

**PCI DSS (Payment Card Industry Data Security Standard)**:
- Applicability: If organization processes, stores, or transmits payment card data
- Requirement 6: Develop and maintain secure systems and applications
- Impact: Security requirements specification (6.3.1), secure coding practices (6.2.4), security testing before production (6.3.2, 6.4.3), vulnerability management (6.2, 6.3.3)

### 6.3 Informational Reference (Tier 3)

**Industry Frameworks** (non-binding references for best practices):
- OWASP SAMM (Software Assurance Maturity Model): Maturity levels for security practices
- NIST SP 800-218 (Secure Software Development Framework): Secure development practices
- BSI APP.3.1 (Web Applications): Web application security guidance
- OWASP ASVS (Application Security Verification Standard): Security requirements specification
- OWASP Testing Guide: Security testing methodologies

**For complete regulatory categorization and applicability, refer to ISMS-POL-00 (Regulatory Applicability Framework).**

---

## 7. Roles and Responsibilities

### 7.1 Governance and Oversight

**Chief Executive Officer (CEO)**:
- Ultimate accountability for secure development framework
- Approves secure development policy
- Allocates resources for secure development program
- Receives executive reports on secure development maturity

**Chief Information Security Officer (CISO)**:
- Overall accountability for secure development framework implementation
- Policy approval and governance oversight
- Resource allocation and budget approval for security tools and training
- Executive reporting on secure development metrics and compliance
- Escalation point for critical security issues and risk acceptances

### 7.2 Security Team

**Application Security Lead**:
- Framework implementation ownership
- Security requirements review and approval
- Security architecture review and threat modeling oversight
- Security tool selection, deployment, and optimization
- Security testing program management
- Developer security training program oversight
- Security champion program management
- Vulnerability management oversight

**Security Architects**:
- Security requirements specification review and approval
- Security architecture review execution
- Threat modeling facilitation and review
- Security design pattern guidance
- Security tool configuration and tuning
- Complex security issue resolution

**Security Analysts**:
- Security assessment execution
- Vulnerability triage and analysis
- Security testing results review
- Security metrics collection and reporting
- Security tool operation and maintenance

**Penetration Testers**:
- Penetration testing execution
- Security testing methodology development
- Vulnerability exploitation and validation
- Penetration testing reporting

### 7.3 Development Organization

**Development Manager / Engineering Manager**:
- SDLC security integration execution
- Developer training and security champion program support
- Code review process enforcement
- Security tool adoption and developer support
- Security defect remediation oversight
- Resource allocation for security activities

**Security Champions** (within development teams):
- Security requirements advocacy within teams
- Secure coding mentorship and guidance
- Security code review execution
- Security tool usage and best practice promotion
- Security defect triage and remediation coordination
- Security awareness promotion within team

**Developers**:
- Security requirements implementation
- Secure coding practice adherence (per ISMS-POL-A.8.28)
- Code review participation (peer review and security review)
- Security tool usage (SAST, SCA, IDE plugins)
- Vulnerability remediation
- Security training completion

**Solution Architects / Technical Leads**:
- Security architecture design
- Security design pattern application
- Threat modeling participation
- Security architecture review coordination
- Technical security decision making

### 7.4 Quality Assurance and Testing

**QA Manager / Test Automation Lead**:
- Security testing integration into QA process
- Security test case development oversight
- Security testing tool deployment (DAST)
- Security acceptance testing coordination

**QA Engineers / Test Engineers**:
- Security test case execution
- Security testing tool operation (DAST, API testing)
- Security defect reporting
- Security regression testing execution

### 7.5 DevOps and Operations

**DevOps Lead / SRE Manager**:
- Security tool integration into CI/CD pipelines
- Security testing automation
- Deployment security validation
- Production security configuration management

**DevOps Engineers / SRE**:
- CI/CD security gate implementation
- Security tool automation (SAST, DAST, SCA in pipeline)
- Production security configuration
- Security monitoring and alerting setup

### 7.6 Application Management

**Product Manager / Application Owner**:
- Application risk classification
- Security requirements specification initiation
- Business justification for security requirements
- Security requirements approval and sign-off
- Security exception requests and risk acceptance
- Evidence provision for security assessments

**Project Manager**:
- SDLC security activity scheduling
- Security resource coordination
- Security milestone tracking
- Security deliverable management

### 7.7 Audit and Compliance

**Internal Auditor**:
- Framework compliance verification
- Assessment methodology validation
- Evidence collection and validation for audits
- Gap identification and remediation tracking
- Audit reporting to management and audit committee

**Compliance Officer**:
- Regulatory alignment validation (GDPR, FADP, DORA, NIS2)
- Compliance evidence collection
- Regulatory change monitoring and impact assessment
- Privacy requirements integration (DPIA, consent management)

### 7.8 Executive Management

**Executive Management**:
- Strategic oversight of secure development program
- Resource allocation and budget approval
- Risk appetite definition
- Major security exception approval (high-risk)
- Regulatory compliance accountability

---

## 8. Integration with ISMS

### 8.1 Related ISMS Controls

This Secure Development Framework integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Secure development controls selected based on [Organization]'s risk assessment
- Application risk classification determines security requirements depth
- Threat modeling integrates with organizational risk treatment

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Controls A.8.25, A.8.26, A.8.29 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported through assessment framework

**Related Controls**:
- A.8.28 (Secure Coding): Coding standards and practices referenced throughout this framework
- A.8.4 (Access to Source Code): Repository security and access control
- A.8.31 (Environment Separation): Dev/test/prod isolation for security testing
- A.8.32 (Change Management): Security sign-off in release process
- A.5.24-27 (Incident Management): Security incident response and lessons learned
- A.8.8 (Vulnerability Management): Production vulnerability remediation
- A.8.15-16 (Logging and Monitoring): Security logging requirements

### 8.2 Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.25-26-29 Suite):
- ISMS-IMP-A.8.25-26-29-S1: Security Requirements Process (requirements elicitation, threat modeling, architecture review)
- ISMS-IMP-A.8.25-26-29-S2: SDLC Security Integration (security activities by phase, methodology-specific guidance)
- ISMS-IMP-A.8.25-26-29-S3: Secure Coding Practices (secure coding implementation, code review, tool deployment)
- ISMS-IMP-A.8.25-26-29-S4: Security Testing Implementation (SAST/DAST/SCA configuration, penetration testing, testing automation)
- ISMS-IMP-A.8.25-26-29-S5: Secure Development Assessment (assessment methodology, evidence collection, compliance scoring)

**Assessment Tools**:
- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers
- Gap analysis templates
- Remediation tracking
- Compliance dashboards

**Supporting References**:
- ISMS-REF-A.8.25-26-29 (Security Testing Tools Reference): Tool comparison, selection criteria, language support matrices
- ISMS-CTX-A.8.25-26-29 (SDLC Security Evolution Context): Industry trends, methodology evolution, emerging practices

### 8.3 Training & Awareness

**Security Awareness** (All Personnel):
- Annual training module on secure development and security responsibilities
- User responsibilities in development lifecycle
- Recognizing and reporting security concerns

**Technical Training** (Development Teams):
- Initial secure development training (before writing production code)
- Annual refresher training (emerging threats, new tools)
- Security Champion specialized training
- Just-in-time training for critical vulnerabilities

**Operational Training** (DevOps, QA):
- Security testing tool operation
- CI/CD security gate configuration
- Security incident response procedures
- Vulnerability remediation workflows

---

## 9. Definitions

**Application**: Software system developed, acquired, or integrated by [Organization], including web applications, mobile applications, desktop applications, APIs, web services, and Infrastructure-as-Code.

**Application Risk Classification**: Systematic categorization of applications as High, Medium, or Low risk based on data sensitivity, exposure, business criticality, and privilege level to determine appropriate security requirements.

**DAST (Dynamic Application Security Testing)**: Security testing technique that analyzes running applications to identify vulnerabilities by simulating attacks against the application in a runtime environment.

**DevSecOps**: Development methodology integrating security practices throughout the DevOps pipeline, emphasizing automation, continuous testing, and shift-left security.

**Penetration Testing**: Manual security testing performed by qualified security professionals to identify vulnerabilities through simulated attacks, providing deeper analysis than automated tools.

**SAST (Static Application Security Testing)**: Security testing technique that analyzes source code, bytecode, or binaries to identify security vulnerabilities without executing the application.

**SCA (Software Composition Analysis)**: Security testing technique that identifies vulnerabilities in third-party and open-source components by analyzing dependencies and comparing against vulnerability databases.

**SDLC (Software Development Lifecycle)**: Structured process for developing software systems, encompassing requirements, design, development, testing, deployment, and maintenance phases.

**Security Champion**: Developer within a development team who receives specialized security training and serves as security point-of-contact, conducts security code reviews, and promotes security awareness.

**Security Requirements Specification (SRS)**: Formal document defining security requirements for an application, including functional security requirements, non-functional requirements, data protection requirements, and compliance requirements.

**Shift-Left Security**: Practice of integrating security activities earlier in the development lifecycle (requirements and design phases) rather than only testing at the end, reducing cost and time to fix vulnerabilities.

**Threat Modeling**: Structured approach to identify security threats and vulnerabilities in application design through systematic analysis of attack scenarios, typically using methodologies like STRIDE.

**Vulnerability Remediation**: Process of fixing security vulnerabilities identified through security testing, including triage, prioritization, fix implementation, verification, and closure.

---

## Annex A: Secure Development Maturity Levels (Quick Reference)

### Purpose

This annex provides a maturity framework to guide risk-based implementation of secure development controls. Organizations can use this framework to:
- Assess current secure development maturity
- Define target maturity based on organizational risk appetite
- Plan phased implementation (avoiding "boil the ocean" approach)
- Demonstrate continuous improvement to auditors and stakeholders

**Note**: This maturity model is for organizational self-assessment and planning. ISO 27001 does not mandate specific maturity levels - compliance requires implementing controls appropriate to organizational risk context.

### Maturity Level Definitions

**Level 1: Initial (Ad Hoc)**
- Security Requirements: Informal or undocumented
- SDLC Integration: Security activities reactive, not systematic
- Security Testing: Manual, inconsistent, performed before major releases
- Suitable for: Low-Risk applications only

**Level 2: Managed (Documented)**
- Security Requirements: Documented for High-Risk applications, basic requirements for others
- SDLC Integration: Security activities defined and documented, manual execution
- Security Testing: SAST/SCA deployed, manual code review, basic DAST
- Suitable for: Medium-Risk applications minimum

**Level 3: Defined (Standardized)**
- Security Requirements: Comprehensive requirements specification process, threat modeling for High-Risk
- SDLC Integration: Security integrated into all SDLC phases, Security Champion program established
- Security Testing: Automated SAST/SCA/DAST in CI/CD, penetration testing for High-Risk applications
- Suitable for: High-Risk applications minimum

**Level 4: Quantitatively Managed (Measured)**
- Security Requirements: Requirements traceability, architecture review process
- SDLC Integration: Security metrics tracked, trend analysis, continuous improvement
- Security Testing: Comprehensive testing coverage, automated security gates, vulnerability SLA tracking
- Suitable for: Organizations with mature secure development programs

**Level 5: Optimizing (Continuous Improvement)**
- Security Requirements: Automated requirements generation from threat intelligence
- SDLC Integration: Security embedded in culture, proactive threat hunting
- Security Testing: AI-assisted testing, real-time vulnerability remediation, predictive security analytics
- Suitable for: Organizations with advanced security capabilities

### Implementation Approach by Application Risk

**High-Risk Applications**:
- Minimum Target: Level 3 (Defined)
- Recommended: Level 4 (Quantitatively Managed)
- Timeline: Achieve Level 3 within 12 months of policy adoption

**Medium-Risk Applications**:
- Minimum Target: Level 2 (Managed)
- Recommended: Level 3 (Defined)
- Timeline: Achieve Level 2 within 18 months of policy adoption

**Low-Risk Applications**:
- Minimum Target: Level 1 (Initial) with documentation
- Recommended: Level 2 (Managed)
- Timeline: Basic controls within 24 months

### Phased Rollout Strategy

**Phase 1 (Months 0-6): Foundation**
- Establish security requirements process (A.8.26)
- Deploy basic security tools (SAST, SCA)
- Conduct initial developer training
- Achieve Level 2 maturity for High-Risk applications

**Phase 2 (Months 6-12): Integration**
- Integrate security into SDLC (A.8.25)
- Establish Security Champion program
- Deploy DAST and penetration testing
- Achieve Level 3 maturity for High-Risk applications

**Phase 3 (Months 12-18): Optimization**
- Implement comprehensive security testing (A.8.29)
- Automate security gates in CI/CD
- Establish metrics and continuous improvement
- Achieve Level 2 maturity for Medium-Risk applications

**Phase 4 (Months 18-24): Maturity**
- Expand coverage to Low-Risk applications
- Implement advanced testing and monitoring
- Demonstrate sustained compliance
- Achieve Level 3+ maturity for High-Risk applications

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Application Security Lead** | [Name] | [Date] |
| **Development Manager / Engineering Director** | [Name] | [Date] |
| **QA Manager / Test Automation Lead** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Chief Executive Officer (CEO)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for secure software development. Implementation procedures (HOW) are documented in ISMS-IMP-A.8.25-26-29 Implementation Guides. Technical tool guidance is provided in ISMS-REF-A.8.25-26-29 (Security Testing Tools Reference). Industry context and awareness information is provided in ISMS-CTX-A.8.25-26-29 (SDLC Security Evolution Context).*