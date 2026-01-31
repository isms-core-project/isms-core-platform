# ISMS-POL-A.8.28 – Secure Coding

## Document Control

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
| **Version Date** | [Date] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Application Security Lead | Consolidated policy from 14 separate documents into unified framework |

**Review Cycle**: Annual (or upon significant organizational/regulatory/threat landscape changes)  
**Next Review Date**: 24.01.2027  
**Approval Chain**: 
- Chief Information Security Officer (CISO)
- Chief Technology Officer (CTO) / VP Engineering
- Legal/Compliance Officer
- Executive Management

**Distribution**: All developers, security team, architects, QA engineers, DevOps, third-party development vendors

**Related Documents**: 
- **ISMS-POL-00** (Regulatory Applicability Framework) ← **MANDATORY REFERENCE**
- **ISMS-IMP-A.8.28.1** (SDLC Assessment Specification)
- **ISMS-IMP-A.8.28.2** (Standards & Tools Assessment Specification)
- **ISMS-IMP-A.8.28.3** (Code Review & Testing Assessment Specification)
- **ISMS-IMP-A.8.28.4** (Third-Party & OSS Assessment Specification)
- **ISMS-IMP-A.8.28.5** (Compliance Dashboard Specification)
- **ISMS-CTX-A.8.28** (Language-Specific Guidelines - Technical Context)
- **ISMS-REF-A.8.28** (Code Review Technical Reference)
- **ISO/IEC 27001:2022** Control A.8.28
- **ISO/IEC 27002:2022** Control 8.28

---

## Executive Summary

This policy establishes [Organization]'s framework for secure software development, implementing ISO/IEC 27001:2022 Control A.8.28 (Secure Coding). Software vulnerabilities represent significant organizational risk—data breaches, service disruptions, financial losses, reputational damage, and regulatory sanctions. This policy addresses these risks by integrating security throughout the Software Development Lifecycle (SDLC), shifting security "left" to prevent vulnerabilities rather than attempting costly remediation after deployment.

**Scope**: This policy applies to all software development activities within [Organization], including internal development, outsourced development, and acquired software customization. It covers all application types (web, mobile, desktop, APIs, microservices, embedded systems), all development phases (requirements through maintenance), and all programming languages used by [Organization]. The policy establishes mandatory requirements for secure coding standards, code review processes, security testing, developer training, and third-party component management.

**Purpose**: Define organizational requirements for secure software development. This policy establishes **WHAT** controls are required and **WHO** is accountable. Technical implementation details (**HOW**) are documented in ISMS-IMP-A.8.28 specifications, enabling policy stability while allowing operational flexibility as technologies and threats evolve.

**Regulatory Context**: Per **ISMS-POL-00 (Regulatory Applicability Framework)**, [Organization] must comply with Swiss Federal Data Protection Act (FADP), EU GDPR (where processing EU personal data), and ISO/IEC 27001:2022. This policy aligns with OWASP, NIST SP 800-218 SSDF, CWE Top 25, and industry best practices as informational references for technical implementation guidance.

**Approach**: This framework uses **system engineering methodology** rather than traditional paperwork-based compliance. Requirements are measurable, assessments are automated via Python-generated Excel workbooks, and compliance is verified through objective evidence rather than subjective self-reporting. This approach prevents "cargo cult compliance"—implementing controls that appear legitimate but provide no genuine protection.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.28

**ISO/IEC 27001:2022 Annex A.8.28 - Secure Coding**

> *Principles for secure coding shall be applied to software development.*

**Control Objective** (ISO/IEC 27002:2022 Control 8.28):

Principles for secure coding should be applied in software development to reduce the number of security vulnerabilities in software. Secure coding principles address:
- Organizational expectations and recognized principles for secure coding
- Common coding practices and errors leading to security vulnerabilities
- Configuration of development tools to enforce secure code creation
- Developer training in writing secure code
- Secure design and architecture, including threat modeling
- Use of secure programming standards
- Code review and security testing during and after development

**This Control Addresses**:
- **Prevention** of security vulnerabilities introduced during software development
- **Reduction** of attack surface through secure-by-design principles
- **Detection** of vulnerabilities early in the development lifecycle (shift-left)
- **Compliance** with legal, regulatory, and contractual security requirements
- **Protection** of organizational data, systems, and intellectual property
- **Mitigation** of common software security risks (OWASP Top 10, CWE Top 25)

**Business Risks Addressed**:
- Data breaches exposing confidential or personal information
- Service disruptions from exploited vulnerabilities
- Financial losses from incident response, remediation, and potential regulatory fines
- Reputational damage affecting customer trust and business relationships
- Intellectual property theft through application exploitation
- Regulatory sanctions for failure to adequately protect data

**Attack Vectors Prevented**:
- Injection attacks (SQL, command, LDAP, XPath, NoSQL)
- Authentication and session management flaws
- Cross-site scripting (XSS) and cross-site request forgery (CSRF)
- Insecure deserialization and object manipulation
- Security misconfiguration vulnerabilities
- Exposure of sensitive data through inadequate protection
- Insufficient logging and monitoring enabling undetected breaches
- Use of components with known vulnerabilities
- Insufficient input validation and output encoding

### 1.2 What This Policy Establishes

This policy defines mandatory requirements for:

**Governance Framework**:
- Secure coding standards applicable to all development activities
- Developer training and competency requirements
- Security champion program integration within development teams
- Exception management and risk acceptance procedures
- Policy review and update mechanisms

**Development Requirements**:
- Pre-development security activities (threat modeling, security requirements, secure design)
- Secure coding practices aligned with OWASP, NIST, and industry standards
- Code review processes with security-focused criteria
- Security testing requirements (SAST, DAST, SCA, penetration testing)
- Third-party and open-source component security management
- Vulnerability management and remediation SLAs

**Accountability**:
- Clear roles and responsibilities (RACI framework)
- Escalation paths for security issues
- Compliance monitoring and reporting
- Evidence collection requirements for audit readiness

**Assessment & Verification**:
- How compliance is measured (via ISMS-IMP-A.8.28 assessments)
- Evidence requirements demonstrating control effectiveness
- Metrics and KPIs for secure development maturity
- Gap analysis and remediation tracking

### 1.3 What This Policy Does NOT Establish

This policy does NOT include:

**Technical Implementation Details** → See **ISMS-IMP-A.8.28** specifications:
- Step-by-step procedures for threat modeling
- Specific tool configurations (SAST, DAST, SCA tools)
- CI/CD pipeline security integration procedures
- Detailed vulnerability remediation workflows
- Tool-specific usage documentation

**Technology Selection** → Risk-based organizational decisions:
- SAST/DAST/SCA vendor selection
- Programming language choices
- Development framework selections
- IDE and development tool standards
- Version control platform decisions

**Operational Runbooks** → Defined by operational teams:
- Daily operational procedures for security tools
- Incident response tactical playbooks (see ISMS Incident Management)
- Deployment procedures (see ISMS Change Management)
- Monitoring and alerting configurations

**Language-Specific Guidance** → See **ISMS-CTX-A.8.28** (Technical Context):
- Python, Java, JavaScript, C#, Go, PHP secure coding patterns
- Language-specific vulnerability prevention techniques
- Framework-specific security configurations
- Technology landscape and evolution awareness

**Detailed Technical Procedures** → See **ISMS-REF-A.8.28** (Technical Reference):
- Code review checklists and methodologies
- Security testing execution procedures
- Tool comparison and evaluation matrices

**Rationale for Separation**:
- **Policy (POL)**: Stable governance requirements (annual review cycle)
- **Implementation (IMP)**: Tactical procedures and assessments (quarterly updates possible)
- **Context (CTX)**: Technology landscape awareness (semi-annual updates)
- **Reference (REF)**: Detailed technical methods (quarterly updates as needed)
- **Operations**: Dynamic operational details (continuous evolution)

This separation enables **policy stability** while allowing **operational flexibility** as technologies, tools, and threats evolve. Policy defines "WHAT is required and WHO is accountable." Implementation specifications define "HOW to implement and assess." Technical references provide "detailed methods and options."

### 1.4 Scope

#### 1.4.1 In Scope

This policy applies to:

**Development Activities**:
- New software development (greenfield projects)
- Maintenance and enhancements of existing applications
- Bug fixes and patches
- Refactoring and technical debt reduction
- Proof-of-concept and prototype development (when security-relevant)
- Emergency hotfixes

**Development Types**:
- Internal development by [Organization] employees
- Outsourced development by third-party vendors or contractors
- Acquired software requiring customization or integration
- Open-source software modifications
- Joint development partnerships

**Application Types**:
- Web applications (front-end and back-end)
- Mobile applications (iOS, Android, cross-platform)
- Desktop applications (Windows, macOS, Linux)
- APIs and microservices
- Serverless functions and cloud-native applications
- Embedded systems and IoT firmware
- Scripts and automation tools (when handling sensitive data or privileged access)

**Development Phases**:
- Requirements gathering and security requirements definition
- Design and architecture (including threat modeling)
- Implementation and coding
- Testing (unit, integration, system, security, acceptance)
- Deployment and release
- Maintenance and support

**Technology Components**:
- All programming languages used by [Organization]
- Development frameworks and libraries
- Third-party commercial components
- Open-source libraries and dependencies
- APIs consumed from external services
- Infrastructure-as-code (Terraform, CloudFormation, etc.)
- Configuration files handling security-relevant settings

**Development Environments**:
- Development environments
- Testing and QA environments
- Staging/pre-production environments
- Production environments
- CI/CD pipelines and build systems

**Personnel**:
- Developers (full-time, contractors, interns)
- Security Champions embedded in development teams
- Code reviewers
- QA and test engineers
- DevOps and platform engineers
- Architects and technical leads
- Development managers
- Third-party development vendors and subcontractors

#### 1.4.2 Out of Scope

This policy does NOT apply to:

**Non-Security-Relevant Activities**:
- Documentation-only changes (user manuals, README files)
- Purely cosmetic UI changes with no code modification
- Static content updates (images, text, translations)

**Excluded Technologies** (covered by other policies):
- Infrastructure configuration management → See ISMS-POL-A.8.9 (Configuration Management)
- Network security controls → See ISMS-POL-A.8.20-21-22 (Network Security)
- Cryptographic key management → See ISMS-POL-A.8.24 (Use of Cryptography)
- Access control implementation → See ISMS-POL-A.8.2-3-5 (Authentication & Access)

**Third-Party Vendor-Managed Software**:
- Commercial off-the-shelf (COTS) software used without customization
- SaaS applications where [Organization] does not control source code
- Managed services where vendor retains full development responsibility
- **Note**: Third-party software **IS** in scope for component security assessment (Section 2.4)

**Personal/Hobby Projects**:
- Employee personal projects not related to [Organization] business
- Hobby development on personal time using personal resources
- **Exception**: If employee contribution to open-source projects used by [Organization], guidance available but not mandatory

#### 1.4.3 Applicability Notes

**Risk-Based Tailoring**:
- Requirements may be tailored based on **risk assessment** of the application
- Critical applications (handling sensitive data, privileged access, financial transactions) require full compliance
- Low-risk applications (internal tools, non-sensitive data) may have reduced requirements with documented risk acceptance
- **Exception process** defined in Section 4.4

**Organizational Context**:
- [Organization] determines which programming languages, frameworks, and tools are in active use
- Policy requirements apply to ALL languages/technologies used, but specific implementation guidance in ISMS-CTX-A.8.28 prioritized by usage
- Organizations SHALL document their technology stack and map policy requirements accordingly

**Phased Implementation**:
- New projects SHALL comply fully from inception
- Existing projects SHOULD achieve compliance within 12 months (per risk-based prioritization)
- Legacy systems MAY have documented exceptions with compensating controls
- Remediation roadmap tracked via ISMS-IMP-A.8.28.5 (Compliance Dashboard)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

#### 1.5.1 Tier 1: Mandatory Compliance

| Regulation | Applicability | Key Requirements for Secure Coding |
|------------|---------------|-------------------------------------|
| **Swiss Federal Data Protection Act (FADP/nDSG)** | All Swiss operations | Art. 8: Technical and organizational measures to ensure data security. Secure coding prevents data breaches through application vulnerabilities. |
| **EU General Data Protection Regulation (GDPR)** | Processing EU personal data | Art. 32: Technical measures ensuring appropriate security. Secure coding implements "security by design and by default" (Art. 25). |
| **ISO/IEC 27001:2022** | ISMS certification | Control A.8.28: Secure coding principles applied to software development (mandatory for certification). |
| **Customer Contracts** | Contract-specific | Secure software development often required by customer contracts, especially in regulated industries (financial services, healthcare, government). |

#### 1.5.2 Tier 2: Conditional Applicability

| Regulation | Trigger Condition | Requirements |
|------------|-------------------|--------------|
| **PCI DSS v4.0** | Processing payment card data | Requirement 6: Secure development of software and systems. SAST, code review, vulnerability management for payment applications. |
| **HIPAA Security Rule** | Handling US health information | § 164.308(a)(8): Evaluation of software security controls. Secure coding for applications accessing ePHI. |
| **FDA Cybersecurity Guidance** | Medical device software | Premarket guidance on cybersecurity for medical devices. Secure coding for firmware and device software. |
| **DORA (EU)** | Financial entities in EU | ICT risk management requirements include secure software development for financial services. |
| **NIS2 Directive (EU)** | Essential/important entities | Cybersecurity risk management measures include secure software development practices. |
| **Industry-Specific Regulations** | As applicable to [Organization] | [Organization] SHALL document industry-specific secure coding requirements in risk assessment. |

**Note**: Conditional applicability is determined during **ISMS risk assessment** and documented in **Statement of Applicability (SoA)**. When triggered, conditional requirements become **mandatory** for [Organization].

#### 1.5.3 Tier 3: Informational Reference / Best Practice Alignment

The following frameworks provide **technical guidance and best practices** but are not legally mandatory unless explicitly required by contract:

**Application Security Standards**:
- **OWASP** (Open Web Application Security Project):
  - OWASP Top 10 (Web, Mobile, API Security Risks)
  - OWASP ASVS (Application Security Verification Standard)
  - OWASP SAMM (Software Assurance Maturity Model)
  - OWASP Cheat Sheet Series
- **CWE Top 25** (Most Dangerous Software Weaknesses)
- **SANS Top 25** (Most Dangerous Software Errors)
- **MITRE ATT&CK** (Adversarial Tactics, Techniques, and Common Knowledge)

**Secure Development Frameworks**:
- **NIST SP 800-218** (Secure Software Development Framework - SSDF)
- **NIST SP 800-53 Rev. 5** (Security and Privacy Controls - SA family)
- **ISO/IEC 27034** (Application Security - all parts)
- **Microsoft Security Development Lifecycle (SDL)**
- **SAFECode** (Fundamental Practices for Secure Software Development)

**Coding Standards**:
- **SEI CERT Coding Standards** (C, C++, Java, Perl, Android)
- **Language-Specific Secure Coding Guidelines** (Python, JavaScript, Go, etc.)

**Usage**: These frameworks inform [Organization]'s secure coding standards and technical implementation but are referenced as **guidance**, not as **mandatory compliance obligations**. [Organization] adopts practices from these frameworks based on **risk assessment** and **organizational context**.

**Exception**: If customer contracts or industry certifications explicitly require compliance with specific frameworks (e.g., "OWASP ASVS Level 2 compliance required"), those requirements become **Tier 1 Mandatory** for the contracted scope.

#### 1.5.4 United States Federal Requirements

References to United States federal frameworks and regulations (FISMA, FedRAMP, NIST cybersecurity requirements, DoD secure development standards, etc.) apply **only** where [Organization]:

- Develops software for US federal agencies as contractor or subcontractor
- Provides software or services to customers subject to such regulations
- Has explicit contractual obligations requiring such compliance
- Operates facilities or processes data within US jurisdiction subject to federal oversight

**In all other cases**, these references are provided for **informational or technical alignment purposes only** and do not constitute mandatory compliance requirements.

**For complete regulatory categorization, refer to ISMS-POL-00 - Regulatory Applicability Framework.**

---

## 2. Requirements Framework

This section establishes secure coding requirements organized by development lifecycle phase. Requirements balance security objectives with development velocity, focusing on measurable, evidence-based controls that prevent vulnerabilities rather than security theater.

*"For a successful technology, reality must take precedence over public relations, for nature cannot be fooled."* - Richard Feynman

**Translation**: Secure coding theater (policies without enforcement or measurement) provides zero actual security. This framework demands evidence-based verification through ISMS-IMP-A.8.28 assessments.

---

### 2.1 Pre-Development Requirements

**Objective**: Establish security foundations before code is written. Pre-development security activities are the most cost-effective phase for preventing vulnerabilities - fixing defects during requirements/design costs 5-10x less than during implementation, and 100x less than post-deployment (Barry Boehm research).

#### 2.1.1 Security Requirements Definition

All development projects SHALL:

**Security Requirements Documentation**:
- Identify and document security requirements during project requirements gathering
- Requirements must be specific (clear, unambiguous), measurable (testable), approved (Application Security Team review), traceable (linked to controls/threats/compliance), and prioritized (Critical/High/Medium/Low)
- Security requirements address: authentication, authorization, data protection, input validation, output encoding, cryptography, error handling, logging, API security, configuration management

**Security Risk Assessment**:
- Required for: new applications, major features, applications processing sensitive data, public-facing applications/APIs, changes affecting authentication/authorization/cryptography
- Must identify application-specific security risks, evaluate likelihood and impact, document risk treatment decisions, and receive CISO/Application Security Lead approval

**Security Acceptance Criteria**:
- Establish security acceptance criteria before development begins
- Minimum criteria: no unresolved Critical/High vulnerabilities, security test cases passed, code review completed with security sign-off, third-party components scanned/approved, security documentation completed

**Regulatory Alignment**:
- Identify applicable regulations (GDPR, FADP, PCI-DSS, HIPAA, etc.) and contractual obligations
- Document how security requirements address compliance
- Obtain Legal/Compliance review for high-risk applications

#### 2.1.2 Threat Modeling

**Threat Modeling Requirements**:

Threat modeling is **REQUIRED** for:
- New applications handling sensitive data
- Major architectural changes
- Public-facing applications or APIs
- Applications integrating with critical business systems
- Applications processing financial transactions or PII

Threat modeling is **RECOMMENDED** for:
- Internal tools with limited sensitive data exposure
- Minor feature additions without architectural changes

**Timing**:
- Conduct during design phase before significant development
- Update when architecture changes, new attack vectors discovered, regulatory requirements change, or post-incident analysis identifies gaps

**Documentation Requirements**:

Threat models must document:
1. **System Overview**: Architecture diagram (data flow, trust boundaries), external dependencies, user roles, data classification
2. **Threat Identification**: Potential threats using structured methodology (STRIDE, PASTA, Attack Trees), attack scenarios, attack surface analysis
3. **Threat Prioritization**: Risk rating for each threat (likelihood × impact), DREAD or CVSS-based scoring
4. **Mitigation Strategy**: Security controls addressing high-priority threats, mapping controls to threats, residual risk assessment
5. **Validation Plan**: How mitigations will be verified (testing, code review, configuration audit)

**Methodologies**: Organizations may use STRIDE (Microsoft), PASTA (Process for Attack Simulation), Attack Trees, OWASP Threat Dragon, or Microsoft Threat Modeling Tool

**Review and Approval**:
- Application Security Team or Security Architect must review threat models
- Review verifies completeness, threat accuracy, mitigation appropriateness, and compliance alignment
- Critical applications require CISO approval

#### 2.1.3 Secure Architecture and Design

**Security-by-Design Principles**:

All applications SHALL apply security-by-design principles:

**Principle of Least Privilege**:
- Users, processes, and systems granted minimum permissions necessary
- Privilege escalation requires explicit approval and justification
- Temporary elevated privileges automatically expire

**Defense in Depth**:
- Multiple security layers (network, application, data)
- Failure of one control does not compromise entire system
- Compensating controls for high-risk areas

**Fail Securely**:
- Security failures default to secure state (deny access, log event, alert)
- Error conditions do not expose sensitive information or bypass security
- Graceful degradation maintains security posture

**Separation of Duties**:
- Critical operations require multiple actors
- No single user can compromise security controls
- Audit trail for privileged operations

**Secure Defaults**:
- Applications ship with secure configuration out-of-box
- Users must explicitly enable less-secure options
- Security settings clearly documented

**Complete Mediation**:
- Every access to resources checked for authorization
- No caching of authorization decisions for sensitive operations
- Authorization enforced server-side, never client-side only

**Open Design**:
- Security does not rely on secrecy of implementation ("security through obscurity")
- Cryptographic algorithms and security mechanisms use publicly reviewed standards
- Security architecture reviewable by security experts

**Psychological Acceptability**:
- Security mechanisms do not significantly impede usability
- Security processes designed for realistic user behavior
- Balance security requirements with user experience

**Architecture Review**:
- Security architecture review required for:
  - New applications (before development sprint 1)
  - Significant architectural changes (new authentication mechanism, data store migration, API redesign)
  - Integration with external systems
  - Cloud service adoption or migration

**Review Documentation**:
- Architecture diagrams (system context, component, deployment)
- Data flow diagrams showing sensitive data paths
- Trust boundaries and security zones
- Authentication and authorization model
- Cryptography usage (what data encrypted, key management approach)
- Security control placement
- Disaster recovery and business continuity considerations

#### 2.1.4 Developer Security Training

**Training Requirements**:

All developers (employees, contractors, third-party developers) SHALL complete security training:

**Initial Training** (before writing production code):
- Secure coding fundamentals (OWASP Top 10, common vulnerabilities)
- Organization-specific secure coding standards
- Security tools usage (SAST, SCA, code review tools)
- Incident reporting procedures
- Acceptable use and security policies

**Annual Refresher Training**:
- Updates on emerging threats and vulnerabilities
- Lessons learned from organizational security incidents
- New tools, standards, or methodologies
- Regulatory changes affecting secure development

**Language-Specific Training** (for languages used in production):
- Secure coding patterns for specific programming languages
- Language-specific vulnerability patterns
- Framework security features and best practices
- See ISMS-CTX-A.8.28 for language-specific guidance

**Training Verification**:
- Completion tracked in learning management system
- Assessments demonstrating knowledge comprehension
- Training completion percentage reported to management quarterly
- Non-compliance escalated to Development Manager and CISO

**Specialized Training** (for specific roles):
- **Security Champions**: Advanced training in threat modeling, security testing, code review
- **Architects**: Secure architecture and design patterns, threat modeling methodologies
- **DevOps**: CI/CD security integration, infrastructure security, secrets management

**Training Sources**:
- Internal training materials developed by Application Security Team
- External training (SANS, OWASP, vendor-specific courses)
- Conference attendance (security conferences, developer conferences with security tracks)
- Hands-on labs and capture-the-flag (CTF) exercises

#### 2.1.5 Development Environment Security

**Development Environment Requirements**:

Development environments (local workstations, cloud-based IDEs, development servers) SHALL be secured:

**Access Control**:
- Role-based access to development environments
- MFA for accessing source code repositories, CI/CD systems, development cloud environments
- Least privilege access to production data (use masked/anonymized data in development)

**Workstation Security**:
- Full disk encryption
- Endpoint protection (antivirus, EDR)
- OS and application patching (automated where possible)
- Screen lock with automatic timeout
- Secure configuration per organizational standards

**Source Code Management**:
- All code stored in version control (Git, SVN, etc.)
- Branch protection rules (require code review, prevent force push to main branches)
- Commit signing for authenticity verification (recommended)
- Access logging and monitoring

**Secrets Management**:
- NO hardcoded secrets in source code (API keys, passwords, private keys, tokens)
- Secrets stored in secret management systems (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, etc.)
- Secret scanning integrated into CI/CD (git-secrets, TruffleHog, Gitleaks)
- Secrets rotated regularly, especially after employee departure

**Development Tool Security**:
- IDEs and development tools kept updated
- Security plugins installed (linters, SAST plugins, secret scanning)
- Secure defaults configured (code analysis enabled, insecure functions flagged)

**Network Security**:
- Development environments segmented from production networks
- VPN required for remote access to development resources
- Development/test data does not leave authorized networks

#### 2.1.6 Security Planning and Resource Allocation

**Project Security Planning**:

Security activities SHALL be integrated into project plans and sprints:

**Security Activities in Project Schedule**:
- Threat modeling sessions scheduled during design phase
- Security architecture review milestone before development sprint 1
- SAST/SCA scans automated in CI/CD pipeline
- Security-focused code reviews scheduled for each sprint/release
- DAST testing scheduled in QA environment
- Penetration testing scheduled before production release (for high-risk applications)
- Vulnerability remediation time allocated in sprint planning

**Resource Allocation**:
- Dedicated Application Security Team or personnel
- Security Champion role formally recognized (percentage of time allocated)
- Budget for security tools (SAST, DAST, SCA, secret scanning)
- Training budget for developers
- External penetration testing budget (for high-risk applications)

**Success Criteria**:
- Security activities completed on schedule (not cut due to time pressure)
- Security findings addressed before release (not deferred to backlog unless explicitly risk-accepted)
- Security metrics tracked and improving over time

---

### 2.2 Secure Coding Standards

**Objective**: Define secure coding practices that developers must follow during implementation. Standards provide concrete, actionable guidance preventing common vulnerabilities.

#### 2.2.1 Language-Agnostic Secure Coding Principles

All development SHALL follow universal secure coding principles regardless of programming language:

**Input Validation**:
- Validate ALL input (user input, API parameters, file uploads, environment variables, database reads)
- Whitelist validation preferred over blacklist (define what IS allowed, not what ISN'T)
- Validate data type, length, format, range
- Reject invalid input, do not attempt to sanitize (sanitization is error-prone)
- Validation performed server-side (client-side validation is UX only, not security)

**Output Encoding**:
- Encode ALL output based on context (HTML, JavaScript, URL, CSS, SQL, LDAP, XML, etc.)
- Use framework-provided encoding functions (never roll your own)
- Context-aware encoding (HTML attribute encoding differs from JavaScript encoding)
- Prevent cross-site scripting (XSS) through proper output encoding

**Authentication**:
- Use strong password hashing (bcrypt, Argon2, scrypt) with appropriate cost factor
- Never store plaintext passwords or use weak hashing (MD5, SHA1, unsalted SHA256)
- Implement account lockout after failed login attempts
- Support multi-factor authentication (MFA) for sensitive applications
- Session tokens cryptographically random (use framework session management, never custom tokens)
- Session timeout for inactive users
- Invalidate sessions on logout and password change

**Authorization**:
- Enforce authorization server-side for every request
- Never rely on client-side authorization (hidden UI elements, disabled buttons)
- Implement least privilege (users access only what they need)
- Prevent Insecure Direct Object References (IDOR) - verify user ownership before accessing resources
- Role-Based Access Control (RBAC) or Attribute-Based Access Control (ABAC) recommended

**Cryptography**:
- Use strong, industry-standard algorithms (AES-256, RSA-2048+, ECDSA P-256+)
- NEVER implement custom cryptography
- Use framework-provided cryptographic libraries
- Proper key management (keys separate from code, rotated regularly)
- Use cryptographically secure random number generators (CSPRNG)
- TLS 1.2+ for data in transit (TLS 1.3 preferred)
- See ISMS-POL-A.8.24 (Use of Cryptography) for detailed requirements

**Error Handling and Logging**:
- Generic error messages to users (do not expose stack traces, SQL errors, file paths)
- Detailed error logging server-side for troubleshooting
- Security events logged (authentication, authorization failures, input validation failures, admin actions)
- Logs protected from tampering, retained per policy
- No sensitive data in logs (passwords, tokens, PII unless specifically required and encrypted)

**Secure Configuration**:
- Remove or disable unnecessary features, services, ports
- Change default passwords and credentials
- Disable debugging in production
- Security headers configured (Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security)
- CORS policies restrictive (do not use wildcard origins for sensitive operations)

**Dependency Management**:
- Keep frameworks and libraries updated
- Monitor for vulnerabilities in dependencies (SCA tools)
- Prefer well-maintained, widely-used libraries over obscure alternatives
- Validate checksums/signatures when downloading dependencies

#### 2.2.2 Language-Specific Secure Coding Guidelines

**Language-Specific Requirements**:

For detailed language-specific secure coding patterns, see **ISMS-CTX-A.8.28 (Language-Specific Guidelines)** covering:
- Python secure coding patterns
- Java secure coding patterns
- JavaScript/TypeScript secure coding patterns
- C#/.NET secure coding patterns
- Go secure coding patterns
- PHP secure coding patterns
- C/C++ secure coding patterns
- Other languages as used by [Organization]

**Language Selection Considerations**:
- Memory-safe languages preferred where applicable (Rust, Go, Java, C#, Python) over memory-unsafe (C, C++)
- Strongly-typed languages reduce certain vulnerability classes
- Mature framework availability (avoid languages lacking secure libraries/frameworks)

#### 2.2.3 Prohibited Practices

The following practices are **PROHIBITED** and constitute security policy violations:

**Code Practices**:
- Hardcoded secrets (API keys, passwords, private keys, tokens) in source code
- Use of deprecated or insecure functions (gets(), strcpy(), MD5, SHA1 for passwords, eval() with user input)
- Dynamic SQL query construction via string concatenation (use parameterized queries)
- Disabling security features (certificate validation, CSRF protection, XSS filters) without documented exception approval
- Custom cryptography implementations
- Storing sensitive data in plaintext

**Configuration Practices**:
- Default credentials unchanged in production
- Debugging enabled in production
- Overly permissive file/directory permissions
- Wildcard CORS origins (Access-Control-Allow-Origin: *) for authenticated endpoints
- Unnecessary services/ports exposed to internet

**Violations**: Prohibited practices discovered during code review or security testing must be remediated before deployment. Exceptions require CISO approval with documented compensating controls.

---

### 2.3 Code Review and Testing Requirements

**Objective**: Identify and remediate security vulnerabilities through systematic review and testing. Multiple layers of testing (manual + automated, static + dynamic) maximize vulnerability detection.

#### 2.3.1 Peer Code Review

**Code Review Requirements**:

All code changes SHALL undergo peer code review before merging to main branch:

**Review Scope**:
- All production code changes (features, bug fixes, refactoring)
- Configuration changes affecting security (authentication, authorization, encryption, network access)
- Infrastructure-as-code changes
- CI/CD pipeline modifications

**Security Review Criteria**:
- Input validation present and correct
- Output encoding appropriate for context
- Authentication and authorization properly enforced
- Sensitive data handled securely
- Error handling does not expose sensitive information
- Security logging implemented
- No hardcoded secrets
- Third-party dependencies vetted
- See **ISMS-REF-A.8.28 (Code Review Reference)** for detailed checklist

**Review Process**:
- Minimum one reviewer per change (two reviewers for security-sensitive changes)
- Security Champions participate in reviews for their teams
- Application Security Team reviews high-risk changes (authentication, cryptography, payment processing)
- Documented approval required before merge

**Review Documentation**:
- Code review comments captured in version control system
- Security issues flagged and tracked to resolution
- Review approval recorded

#### 2.3.2 Static Application Security Testing (SAST)

**SAST Requirements**:

[Organization] SHALL implement automated static code analysis:

**SAST Tool Deployment**:
- SAST tools integrated into CI/CD pipeline
- Scans automated on every commit or pull request (PR)
- Language coverage for all languages used in production

**Scan Configuration**:
- Scan rules configured for organizational context (not just default rulesets)
- False positive management (suppress confirmed false positives with documentation)
- Baseline established (existing vulnerabilities tracked separately from new introductions)

**Thresholds and Gates**:
- Build fails on new Critical or High severity findings (configurable per project risk)
- Medium/Low findings tracked but may not block build (organization-specific)
- Security gate before merge to main branch or deployment to production

**Findings Management**:
- Vulnerabilities tracked in issue tracking system
- Remediation SLAs by severity:
  - Critical: 7 days
  - High: 30 days
  - Medium: 90 days
  - Low: 180 days or next major release
- Exceptions require Application Security Lead or CISO approval

**Tool Effectiveness**:
- SAST tool effectiveness evaluated annually
- False positive rate monitored and reduced through tuning
- Coverage gaps identified and addressed

#### 2.3.3 Software Composition Analysis (SCA)

**SCA Requirements**:

[Organization] SHALL implement automated dependency vulnerability scanning:

**SCA Tool Deployment**:
- SCA tools integrated into CI/CD pipeline
- Scans on every build and scheduled periodic scans (daily/weekly)
- Monitors all dependency types (direct dependencies, transitive dependencies, container images)

**Vulnerability Monitoring**:
- Continuous monitoring for newly disclosed vulnerabilities in dependencies
- Alerts generated when vulnerabilities discovered in deployed applications
- Vulnerability severity based on CVSS, exploitability, and application context

**Dependency Management**:
- Software Bill of Materials (SBOM) generated for each application
- Dependencies with known vulnerabilities blocked from deployment (Critical/High severity)
- Dependency update process defined (patching schedule, testing requirements)

**License Compliance**:
- Open-source license obligations identified
- Incompatible licenses flagged (GPL in proprietary software, etc.)
- Legal review for copyleft licenses

**Remediation**:
- Update vulnerable dependencies to patched versions
- If no patch available: apply vendor workaround, implement compensating controls, or accept risk (with CISO approval)
- Track remediation per SLAs (same as SAST)

#### 2.3.4 Dynamic Application Security Testing (DAST)

**DAST Requirements**:

DAST is REQUIRED for:
- Web applications exposed to internet or untrusted networks
- APIs with public or partner access
- Applications processing sensitive data

DAST is RECOMMENDED for:
- Internal applications with elevated privileges
- Applications accessible from corporate network

**DAST Implementation**:
- Automated DAST scans in QA/staging environment (not production)
- Scheduled scans (weekly or per release)
- Authenticated scanning for applications requiring login
- Coverage of critical user journeys and APIs

**Scan Scope**:
- All publicly accessible endpoints
- All authenticated user roles
- File upload functionality
- Search and query functionality
- Form submissions

**Findings Remediation**:
- DAST findings prioritized alongside SAST findings
- Same SLA framework applies (Critical: 7 days, High: 30 days, etc.)

#### 2.3.5 Penetration Testing

**Penetration Testing Requirements**:

Penetration testing is REQUIRED for:
- New applications before production launch
- Applications after major changes (architecture redesign, authentication changes)
- Annually for high-risk applications (payment processing, PII processing, public-facing)

Penetration testing MAY be performed by:
- Internal security team (if appropriately skilled)
- External third-party penetration testing firms (preferred for objectivity)

**Penetration Test Scope**:
- Defined scope agreement (in-scope systems, out-of-scope systems, testing constraints)
- Testing methodologies (OWASP Testing Guide, PTES, etc.)
- Testing types (black-box, gray-box, white-box as appropriate)

**Findings and Remediation**:
- Penetration test report with findings, evidence, and remediation recommendations
- Critical/High findings must be remediated before production deployment
- Medium/Low findings remediated per SLA or risk-accepted with approval
- Retest performed to validate remediation

**Penetration Test Documentation**:
- Test report retained for audit
- Findings tracked in vulnerability management system
- Remediation evidence documented

---

### 2.4 Third-Party and Open-Source Software Management

**Objective**: Manage security risks from external code dependencies and components. Modern applications are predominantly composed of third-party code; supply chain attacks increasingly target dependencies.

#### 2.4.1 Third-Party Component Approval

**Component Introduction Process**:

Before introducing new third-party components (libraries, frameworks, SDKs, APIs), developers SHALL:

**Evaluation Criteria**:
- **Security**: Known vulnerabilities, security track record, vendor security practices
- **Maintenance**: Active development, timely security patches, community support
- **Licensing**: Compatible with organizational use, no unexpected obligations
- **Functionality**: Meets requirements without introducing unnecessary attack surface
- **Alternatives**: Evaluation of alternative components

**Approval Process**:
- Security Champion or Application Security Team approval required
- Critical components require additional architecture review
- Approval documented (wiki, component registry, decision log)

**Prohibited Components**:
- Components with unpatched Critical vulnerabilities
- Abandoned or unmaintained components (no updates in 2+ years)
- Components with incompatible licenses
- Components from untrusted sources

#### 2.4.2 Software Composition Analysis (SCA) Integration

**SCA Implementation**: See Section 2.3.3 for SCA technical requirements.

**Component Inventory (SBOM)**:
- Automated SBOM generation for each application
- SBOM includes: component name, version, license, known vulnerabilities
- SBOM updated on every build
- SBOM retained for deployed applications

**Vulnerability Response**:
- Automated alerts when new vulnerabilities disclosed in dependencies
- Vulnerability assessment (exploitability, application impact, patch availability)
- Remediation per SLA framework or risk acceptance with approval

#### 2.4.3 Dependency Update Management

**Dependency Patching**:

Dependencies SHALL be kept reasonably current:

**Update Frequency**:
- Security patches: Applied within SLA for vulnerability severity
- Minor version updates: Evaluated quarterly, applied if stable and low-risk
- Major version updates: Evaluated for security improvements, breaking changes assessed

**Update Process**:
- Dependency update tested in non-production environment
- Regression testing performed
- Security testing repeated post-update
- Rollback plan documented

**Legacy Dependency Management**:
- Dependencies approaching end-of-life (EOL) identified
- Migration plan developed before EOL
- Compensating controls if migration not feasible (network isolation, additional monitoring)

#### 2.4.4 Supply Chain Security

**Supply Chain Risk Management**:

[Organization] implements supply chain security controls:

**Component Provenance**:
- Verify component source (official repositories, trusted mirrors)
- Checksum or signature verification when downloading components
- Avoid downloading from unofficial sources

**Repository Security**:
- Private package repositories (npm, Maven, NuGet, PyPI mirrors) where feasible
- Repository access controls
- Vulnerability scanning of repositories

**Build Security**:
- CI/CD pipeline security (access controls, audit logging)
- Build environments isolated and secured
- Dependency pinning or lock files (package-lock.json, requirements.txt, Gemfile.lock)

**Vendor Security Assessment**:
- For commercial components: Vendor security questionnaire
- Review of vendor security practices, incident response, and patching cadence
- Contractual security obligations where applicable

---

## 3. Roles, Governance & Incident Response

This section defines roles and responsibilities using RACI methodology, establishes governance framework for policy lifecycle, and defines incident management procedures for security vulnerabilities.

*"You can delegate authority, but you cannot delegate responsibility."* - Byron Dorgan

**Translation for Security**: Every security activity requires clear accountability. When everyone is responsible, no one is responsible. This framework eliminates ambiguity.

---

### 3.1 Roles and Responsibilities

**RACI Methodology**:
- **R** (Responsible): Performs the work
- **A** (Accountable): Ultimately answerable for completion (only one A per activity)
- **C** (Consulted): Provides input and expertise
- **I** (Informed): Kept updated on progress

#### 3.1.1 Executive and Leadership Roles

**Chief Information Security Officer (CISO)**:
- **Accountability**: Overall secure coding program governance and risk acceptance
- **Responsibilities**: Approve policy framework and updates, accept residual risk for unresolved vulnerabilities, allocate budget for security tools and training, oversee Application Security Team, report security metrics to Board/Executive Management, approve policy exceptions, escalate critical issues to executive leadership
- **Authority**: Block production deployments with Critical/High unresolved vulnerabilities, mandate security training, require security assessments for high-risk applications
- **RACI**: **A** for policy governance, risk acceptance, exception approvals

**Chief Technology Officer (CTO) / VP Engineering**:
- **Accountability**: Development organization's adherence to secure coding practices
- **Responsibilities**: Ensure development teams follow secure coding standards, allocate resources for security activities, support Security Champions program, include security metrics in performance reviews, escalate resource conflicts to CISO, foster security-aware engineering culture
- **Authority**: Prioritize security remediation in roadmaps, adjust timelines for security requirements, performance management for non-compliance
- **RACI**: **A** for development organization compliance

**Chief Legal Officer / General Counsel**:
- **Accountability**: Legal and regulatory compliance for software development
- **Responsibilities**: Advise on open-source license compliance, review vendor contracts, assess legal risk from vulnerabilities, advise on data protection regulations, support incident response legal implications
- **Authority**: Block use of software with incompatible licenses, require legal review for high-risk vendor contracts, mandate disclosure of security incidents per legal requirements
- **RACI**: **A** for license compliance, **C** for vendor contracts and regulatory compliance

#### 3.1.2 Security Team Roles

**Application Security Lead**:
- **Accountability**: Application security program implementation and effectiveness
- **Responsibilities**: Define/maintain secure coding standards, configure/maintain security tools (SAST, DAST, SCA), review threat models and security architectures, triage vulnerabilities and assign severity, coordinate penetration testing, train Security Champions and developers, track vulnerability remediation and SLA compliance, report metrics to CISO
- **Authority**: Approve/reject threat models and security designs, classify vulnerability severity, approve security exceptions (with CISO), require security testing before production deployment
- **RACI**: **R** for security tool configuration, threat model review, vulnerability triage; **A** for application security program execution

**Security Architect**:
- **Accountability**: Secure system architecture and design
- **Responsibilities**: Conduct architecture security reviews, develop secure architecture patterns, provide security design guidance, review threat models, assess cloud security architecture, define security requirements for new technologies
- **Authority**: Approve/reject security architecture designs, require architecture changes to meet standards, approve technology selections with security implications
- **RACI**: **R** for architecture reviews, **A** for secure architecture decisions

**Security Engineer / Analyst**:
- **Accountability**: Security tool operation and vulnerability analysis
- **Responsibilities**: Operate SAST/DAST/SCA tools, analyze scan results and eliminate false positives, support development teams with remediation, monitor security alerts and threat intelligence, maintain tool configurations, document findings and remediation guidance
- **Authority**: Classify findings as true/false positive, recommend remediation approaches, escalate unresolved vulnerabilities to Application Security Lead
- **RACI**: **R** for tool operation and vulnerability analysis

#### 3.1.3 Development Team Roles

**Development Manager / Engineering Lead**:
- **Accountability**: Team adherence to secure coding practices and remediation timelines
- **Responsibilities**: Allocate sprint capacity for security activities, prioritize vulnerability remediation, ensure developers complete security training, support Security Champions, enforce code review processes, escalate blocked security work to CTO
- **Authority**: Prioritize security work in sprints, defer features for security remediation, enforce security gates for deployment
- **RACI**: **A** for team-level compliance, **R** for sprint-level security prioritization

**Software Developer / Engineer**:
- **Accountability**: Writing secure code and remediating identified vulnerabilities
- **Responsibilities**: Follow secure coding standards, complete security training, participate in code reviews, fix vulnerabilities within SLA, integrate security tools in development workflow, consult Security Champions for security questions, report security concerns
- **Authority**: Request security guidance, propose secure design alternatives
- **RACI**: **R** for secure code implementation, vulnerability remediation, **C** for threat modeling and architecture review

**Security Champion**:
- **Accountability**: Security advocacy and knowledge transfer within development team
- **Responsibilities**: Act as security liaison between development team and Application Security Team, promote secure coding practices, participate in threat modeling, review security-sensitive code changes, assist developers with security questions, track team security metrics
- **Authority**: Recommend security improvements, escalate security concerns, participate in security tool selection
- **RACI**: **C** for team-level security decisions, **R** for security knowledge transfer

**Architect / Technical Lead**:
- **Accountability**: Secure architecture decisions for applications/systems
- **Responsibilities**: Design security architecture, conduct threat modeling, define security requirements, review high-risk code changes, select frameworks and technologies with security considerations, document security design decisions
- **Authority**: Approve architecture decisions, require security controls in design, select technologies meeting security standards
- **RACI**: **A** for architecture security decisions, **R** for threat modeling

#### 3.1.4 Supporting Roles

**QA / Test Engineer**:
- **Accountability**: Security testing execution and validation
- **Responsibilities**: Execute security test cases, operate DAST tools in QA environment, verify vulnerability fixes, test security requirements, document security test results, escalate security test failures
- **Authority**: Block QA approval for unresolved security issues
- **RACI**: **R** for security testing execution, **C** for security test case design

**DevOps / Platform Engineer**:
- **Accountability**: CI/CD security integration and infrastructure security
- **Responsibilities**: Integrate SAST/DAST/SCA tools into CI/CD pipeline, configure security gates, maintain build security, manage secrets in pipelines, implement deployment security controls, monitor security tool performance
- **Authority**: Configure pipeline security requirements, block insecure deployments
- **RACI**: **R** for CI/CD security automation, **A** for pipeline security configuration

**Product Owner / Product Manager**:
- **Accountability**: Security requirements prioritization in product backlog
- **Responsibilities**: Include security requirements in user stories, prioritize security work alongside features, accept security acceptance criteria, support security sprint planning, communicate security impacts to stakeholders
- **Authority**: Accept/reject user stories based on security completeness
- **RACI**: **C** for security requirements, **I** for vulnerability remediation

#### 3.1.5 RACI Matrix - Key Activities

| Activity | CISO | App Sec Lead | Developer | Dev Manager | Security Champion | QA Engineer | DevOps |
|----------|------|--------------|-----------|-------------|-------------------|-------------|--------|
| **Policy approval** | A | R | I | C | I | I | I |
| **Threat modeling** | I | C | R | C | C | I | I |
| **Secure code implementation** | I | C | R | A | C | I | I |
| **Code review (security)** | I | C | R | A | R | I | I |
| **SAST tool configuration** | I | A | I | C | I | I | R |
| **Vulnerability triage** | I | A | I | C | C | I | I |
| **Vulnerability remediation** | I | C | R | A | C | I | I |
| **Security testing (DAST)** | I | C | I | C | I | R | R |
| **Penetration testing** | C | A | I | I | I | C | I |
| **Exception approval** | A | C | I | C | I | I | I |
| **Training delivery** | I | A | R | C | C | I | I |
| **CI/CD security integration** | I | C | I | C | I | I | A |
| **SCA scanning** | I | A | I | C | I | I | R |
| **Metrics reporting** | A | R | I | C | I | I | I |

---

### 3.2 Policy Governance

**Governance Objectives**:
- Maintain policy relevance in rapidly evolving threat landscape
- Ensure proper approval and oversight
- Communicate policies clearly to diverse technical stakeholders
- Monitor compliance and measure effectiveness
- Continuously improve based on vulnerability trends and lessons learned

*"In God we trust. All others must bring data."* - W. Edwards Deming

**Application to Security Governance**: Governance is not about trust—it's about verification. Metrics, evidence, and continuous monitoring prove policy effectiveness.

#### 3.2.1 Policy Lifecycle

**Lifecycle Stages**:
1. **Creation**: Policy developed in response to organizational need, vulnerability trends, regulatory requirement, or risk assessment
2. **Review**: Stakeholder review (Security, Development, Legal, Compliance) and feedback integration
3. **Approval**: Formal approval by designated authorities per approval matrix
4. **Publication**: Communication and distribution to development organization
5. **Implementation**: Technical implementation (tools, processes, training)
6. **Monitoring**: Ongoing compliance monitoring and effectiveness measurement
7. **Review/Update**: Periodic or triggered review and updates based on threat intelligence
8. **Retirement**: Archival when policy is superseded or no longer applicable

**Policy Owner**: CISO is accountable for policy lifecycle management, supported by Application Security Lead (technical content), Development Management (operational feasibility), and Legal/Compliance (regulatory alignment).

#### 3.2.2 Policy Review and Updates

**Scheduled Reviews**:
- **Annual Review** (mandatory): Full policy framework reviewed annually, scheduled [Approval anniversary + 12 months], participants: CISO, Application Security Lead, Development Management, Legal/Compliance, outcome: Approve as-is, update, or defer
- **Quarterly Reviews** (targeted): Effectiveness metrics analysis, stakeholder feedback collection, threat landscape monitoring, tool performance evaluation

**Triggered Reviews**:

Policy review SHALL be triggered by:
- Significant regulatory changes (new GDPR guidance, CRA implementation, PCI-DSS updates)
- Major security incidents related to code vulnerabilities
- Vulnerability trend analysis indicating systemic gaps (OWASP Top 10 updates)
- Technology changes affecting control applicability (new programming languages, cloud migration)
- Organizational structure changes (M&A, new business lines)
- Tool changes (new SAST/DAST/SCA vendor, major version upgrade)
- Audit findings indicating policy gaps or ineffectiveness

**Review Process**:
1. Impact assessment (affected stakeholders, systems, tools)
2. Stakeholder consultation (Security, Development, Legal, DevOps)
3. Draft revision prepared with tracked changes
4. Legal/Compliance review (mandatory for scope or compliance changes)
5. Review and approval by CISO and required stakeholders
6. Communication plan executed
7. Tool configuration updates if required (deploy new rules, test, tune)
8. Implementation tracking (30/60/90 day checkpoints)
9. Post-implementation review (effectiveness, false positives, user feedback)

#### 3.2.3 Approval Process

**Approval Authority**:

| Change Type | Approval Required | Review Required |
|-------------|-------------------|-----------------|
| Major policy update (scope, requirements, SLAs, roles) | CISO + CTO + Legal + Executive | All stakeholders |
| Minor policy update (clarifications, examples) | CISO + Application Security Lead | Affected stakeholders |
| Clarification (typo fixes, formatting) | Application Security Lead | CISO (informed) |
| Implementation specifications (IMP-A.8.28.x) | Application Security Lead | Development Management (consulted) |
| Emergency changes (critical vulnerabilities, zero-days) | CISO verbal/email approval | Formal documentation within 5 business days |

**Approval Process**:
1. Proposal submission with justification (what changed and why)
2. Impact assessment (security benefit vs. operational impact)
3. Stakeholder review (5-10 business days for standard, up to 20 for complex)
4. Approval authority decision (Approve / Approve with Conditions / Deny / Defer)
5. Version update and communication
6. Implementation tracking

#### 3.2.4 Exception Management

**Exception Request Requirements**:

Exceptions to secure coding policy requirements require:
- **Documented business or technical justification**: Specific reason why compliance not feasible
- **Risk assessment**: Likelihood and impact of non-compliance, residual risk evaluation
- **Compensating controls**: Alternative protections where feasible (additional monitoring, access restrictions, enhanced logging)
- **Timeline**: Duration of exception and path to achieving full compliance (if temporary)
- **Formal approval** per authority matrix

**Approval Authority**:

| Exception Type | Approval Required | Maximum Duration |
|----------------|-------------------|------------------|
| **Single project exception (Low risk)** | Application Security Lead + Dev Manager | 12 months |
| **Single project exception (High risk)** | CISO + CTO | 6 months |
| **Technology/tool exception** | CISO + CTO + Legal | Annual re-approval required |
| **Remediation SLA extension (Critical/High)** | CISO | Case-by-case |
| **Prohibited practice override** | NOT PERMITTED | N/A |

**Exception Documentation**:

All approved exceptions SHALL be documented including:
- Business justification and necessity
- Risk assessment (inherent risk, compensating controls, residual risk)
- Approval signatures and dates
- Exception duration and review schedule
- Monitoring and compliance verification requirements
- Conditions for exception revocation

**Exception Monitoring**:

Active exceptions are:
- Reviewed quarterly for continued validity
- Monitored for compliance with compensating controls
- Revoked if business justification changes or compensating controls fail
- Escalated if risk profile increases (new exploit, vulnerability severity increase)
- Automatically expired at end of approved duration (no implicit renewal)

**Exception Register**: All exceptions tracked in exception register (ISMS-IMP-A.8.28.5 Compliance Dashboard).

#### 3.2.5 Compliance Monitoring

**Monitoring Methods**:
- Automated compliance checks via security tools (SAST, SCA, code quality gates)
- Periodic assessments via ISMS-IMP-A.8.28.1 through .4 workbooks
- Audit reviews (internal and external)
- Self-assessments by development teams
- Continuous metrics collection (vulnerability trends, remediation SLAs, training completion)

**Monitoring Frequency**:

| Control Criticality | Assessment Frequency | Audit Frequency |
|---------------------|---------------------|-----------------|
| Critical (authentication, cryptography, input validation) | Quarterly | Annual |
| High (authorization, session management, logging) | Semi-annual | Biennial |
| Medium (error handling, configuration) | Annual | On-demand |
| Low (code quality, comments) | Biennial | On-demand |

**Non-Compliance Management**:

Non-compliance handling process:
1. **Detection**: Identification through monitoring (tool alerts, audit findings, self-assessment)
2. **Assessment**: Impact and root cause analysis (was this gap known? systemic or isolated?)
3. **Remediation**: Corrective action plan with timeline (immediate fix vs. planned remediation)
4. **Escalation**: Risk-based escalation to CISO/Executive Management
5. **Verification**: Validation of remediation effectiveness (retest, re-scan)
6. **Tracking**: Non-compliance register maintenance (ISMS-IMP-A.8.28.5)

**Escalation Thresholds**:
- Critical findings → Immediate CISO notification + executive briefing
- High findings → CISO notification within 24 hours
- Medium findings → Monthly compliance report
- Low findings → Quarterly compliance report

#### 3.2.6 Version Control

**Versioning Scheme**: Major.Minor (e.g., 1.0, 1.1, 2.0)

**Major Version (X.0)**:
- Scope changes (new application types, new requirements, exclusions)
- New mandatory requirements (new SAST tool, new training requirements)
- Role redefinitions (accountability changes)
- SLA changes (remediation timelines)
- Requires full re-approval per approval matrix

**Minor Version (X.Y)**:
- Clarifications (examples, code samples, process clarification)
- Example updates (new language examples, updated references)
- Non-substantive improvements (formatting, cross-references)
- Tool version updates (SAST tool upgraded, no process change)
- Requires limited approval (Application Security Lead + CISO informed)

**Change Tracking**:
- Version history table maintained in Document Control section
- Change rationale documented in version history
- Previous versions archived (retain for audit)
- Stakeholder notification process (email, wiki, training updates)

---

### 3.3 Assessment and Verification

[Organization] verifies secure coding control effectiveness through structured assessment.

**Assessment Domains**:
1. **SDLC Integration** (ISMS-IMP-A.8.28.1): Threat modeling, security requirements, architecture review, training
2. **Standards & Tools** (ISMS-IMP-A.8.28.2): Coding standards adoption, SAST/DAST/SCA deployment, tool configuration
3. **Code Review & Testing** (ISMS-IMP-A.8.28.3): Peer review processes, security testing execution, penetration testing
4. **Third-Party & OSS** (ISMS-IMP-A.8.28.4): SCA implementation, SBOM generation, dependency management
5. **Compliance Dashboard** (ISMS-IMP-A.8.28.5): Consolidated metrics, gap analysis, executive reporting

**Assessment Methodology**:
1. Self-assessment by control owners (development teams, security teams)
2. Evidence collection and documentation (screenshots, reports, configurations)
3. Technical validation where applicable (scan results, tool configurations)
4. Management review and approval (Development Manager, Application Security Lead, CISO)
5. Gap identification and remediation planning

**Evidence Requirements**:

Required evidence types:

| Requirement Area | Evidence Type | Examples |
|------------------|---------------|----------|
| **Training** | Records, certificates | LMS completion reports, training attendance |
| **Threat Modeling** | Documentation | Threat model documents, architecture diagrams |
| **Code Review** | Process records | PR approval records, review comments |
| **SAST/DAST/SCA** | Tool reports | Scan results, vulnerability reports, trend graphs |
| **Penetration Testing** | Test reports | Pentest reports, remediation evidence |
| **Compliance** | Metrics, dashboards | Vulnerability aging reports, SLA compliance metrics |

**Evidence Quality Standards**:
- Objective and verifiable (not subjective opinions)
- Time-stamped and attributable (who, when, what)
- Sufficient to demonstrate compliance (auditor would accept)
- Maintained per retention policy (minimum: duration of application support lifecycle)

**Compliance Metrics**:

Key Performance Indicators (KPIs):

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| % Developers trained annually | 100% | Quarterly | Application Security Lead |
| % Projects with threat models | 90% (high-risk apps) | Quarterly | Security Architect |
| % Code commits with peer review | 95% | Monthly | Development Management |
| Critical vulnerabilities remediated within 7 days | 95% | Monthly | Application Security Lead |
| High vulnerabilities remediated within 30 days | 90% | Monthly | Application Security Lead |
| SAST false positive rate | <20% | Quarterly | Security Engineer |

**Trend Analysis**:
- Quarterly compliance trending
- Year-over-year comparison
- Benchmark against industry standards (BSIMM, OWASP SAMM)

**Audit Readiness**:

Audit support process:
- Consolidated evidence repository (ISMS-IMP-A.8.28 workbooks)
- Assessment workbooks current (maximum 6 months old for annual audits)
- Exception register up-to-date
- Compliance dashboard accessible to auditors
- Control owner interview preparation (RACI roles understand responsibilities)

**Audit Process**:
1. Provide policy and implementation specifications to auditor
2. Present compliance dashboard and metrics
3. Demonstrate evidence for sampled requirements
4. Explain exceptions with compensating controls and risk acceptance
5. Show continuous improvement initiatives (vulnerability trend reduction, tool improvements)

---

### 3.4 Incident Response

**Security Incident Definition**:

Security incidents related to secure coding include:
- **Production vulnerabilities**: Vulnerabilities discovered in deployed applications
- **Breach via code vulnerability**: Security incidents caused by exploited application vulnerabilities
- **Supply chain compromise**: Compromised dependencies or third-party components
- **Code repository breach**: Unauthorized access to source code or secrets
- **Security tool compromise**: SAST/DAST/SCA tools compromised

**Incident Classification**:

| Severity | Definition | Response Time | Escalation |
|----------|------------|---------------|------------|
| **Critical** | Active exploitation, data breach, production compromise | Immediate (< 1 hour) | CISO + CTO + Executive |
| **High** | High-severity vulnerability in production, no active exploitation yet | < 4 hours | CISO + Development Management |
| **Medium** | Medium-severity vulnerability in production, low exploitability | < 1 business day | Application Security Lead |
| **Low** | Low-severity vulnerability, minimal impact | < 3 business days | Security Engineer |

**Incident Response Process**:

1. **Detection & Reporting**:
   - Vulnerability discovered (security testing, penetration test, bug bounty, public disclosure)
   - Security event detected (intrusion attempt, anomalous behavior)
   - Reported via incident response channel (security@, incident management system)

2. **Assessment**:
   - Incident classification (severity, scope, impact)
   - Vulnerability analysis (exploitability, affected systems, data exposure)
   - Business impact assessment (regulatory, financial, reputational)

3. **Containment**:
   - **Immediate**: Disable vulnerable functionality, apply WAF rules, isolate affected systems
   - **Short-term**: Deploy hotfix, apply patches, update configurations
   - **Long-term**: Code remediation, architecture changes

4. **Investigation**:
   - Root cause analysis (how vulnerability introduced, why not detected earlier)
   - Scope determination (other applications affected, similar vulnerabilities)
   - Evidence collection (logs, scan results, code changes)

5. **Remediation**:
   - Emergency patching (Critical: within 24-48 hours)
   - Code fix development and testing
   - Deployment coordination (change control, communication)
   - Verification (retest, rescan, penetration test)

6. **Recovery**:
   - Service restoration
   - Monitoring for recurrence
   - Communication to stakeholders

7. **Post-Incident**:
   - Lessons learned session (security, development, operations)
   - Policy/process improvements (update standards, improve detection)
   - Tool tuning (SAST rules, DAST coverage)
   - Training updates (incorporate lessons learned)

**Communication**:
- **Internal**: Development teams, security team, management (per severity)
- **External**: Customers (if data breach), regulators (per legal requirements), public disclosure (coordinated disclosure for responsible disclosure)
- **Media**: Legal/PR approval required

**Documentation**:
- Incident report (timeline, root cause, impact, remediation)
- Lessons learned document
- Policy/process updates
- Evidence retention (logs, communications, decisions)

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Secure coding controls selected based on [Organization]'s risk assessment identifying software security risks
- Threat landscape assessment determines prevention, detection, and response requirements
- Risk treatment plans document secure coding control implementation, residual risks, and acceptance
- Vulnerability risk scored using CVSS, organizational impact assessment, and exploitability analysis

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.8.28 applicability justified in [Organization]'s SoA based on software development activities
- Implementation status tracked and reported in management review
- Control effectiveness measured through ISMS-IMP-A.8.28 assessment program

**Related Controls**:

| Control | Integration Point |
|---------|-------------------|
| **A.5.7** | Threat Intelligence - Informs secure coding priorities (OWASP Top 10 updates, CWE trends, zero-day vulnerabilities) |
| **A.5.9** | Asset Inventory - Application inventory identifies systems requiring secure coding controls |
| **A.5.10** | Acceptable Use - Defines acceptable development practices and tool usage |
| **A.5.12** | Information Classification - Determines security requirements based on data sensitivity |
| **A.5.15** | Access Control - Secure coding implements application-level access controls |
| **A.5.16** | Identity Management - Authentication implementation follows secure coding standards |
| **A.5.17** | Authentication Information - Credential management in code (no hardcoded secrets) |
| **A.5.23** | Cloud Services - Secure coding for cloud-native applications (serverless, containers) |
| **A.5.24-28** | Incident Management - Code vulnerabilities trigger incident response processes |
| **A.5.33** | Records Protection - Secure logging implementation per secure coding standards |
| **A.5.34** | Privacy & PII Protection - PII handling in code per privacy-by-design principles |
| **A.6.6** | Security Requirements in Contracts - Vendor development contracts include secure coding obligations |
| **A.6.8** | Information Security in Project Management - Security integrated into SDLC project management |
| **A.8.1** | User Endpoint Devices - Secure development environment requirements |
| **A.8.2-3-5** | Authentication & Access - Secure coding implements authentication and authorization logic |
| **A.8.9** | Configuration Management - Configuration-as-code follows secure coding practices |
| **A.8.15** | Logging - Secure logging implementation (what to log, PII exclusion) |
| **A.8.16** | Monitoring Activities - Security events from applications feed SIEM |
| **A.8.19** | Software Installation - Change management for code deployments |
| **A.8.24** | Use of Cryptography - Cryptographic implementation in code follows crypto policy |
| **A.8.25** | Secure Development Lifecycle - This policy IS the SDLC security control |
| **A.8.26** | Application Security Requirements - Security requirements defined in threat models |
| **A.8.27** | Secure System Architecture - Architecture reviews validate secure design |
| **A.8.29** | Security Testing - SAST, DAST, SCA, penetration testing per this policy |
| **A.8.30** | Outsourced Development - Third-party development follows same secure coding requirements |
| **A.8.32** | Change Management - Code changes follow change control with security gates |

### 4.2 Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.28 Suite):

[Organization] implements secure coding controls using structured assessment workbooks:

- **ISMS-IMP-A.8.28.1**: SDLC Assessment Specification
  - Threat modeling maturity and coverage
  - Security requirements definition processes
  - Architecture security review procedures
  - Developer security training programs
  - Development environment security
  - Security planning and resource allocation
  - Excel workbook: SDLC Security Assessment

- **ISMS-IMP-A.8.28.2**: Standards & Tools Assessment Specification
  - Secure coding standards adoption
  - Language-specific guidelines implementation
  - SAST, DAST, SCA tool deployment
  - Tool configuration and effectiveness
  - False positive management
  - Security gate configuration
  - Excel workbook: Standards & Tools Assessment

- **ISMS-IMP-A.8.28.3**: Code Review & Testing Assessment Specification
  - Peer code review processes
  - Security-focused code review criteria
  - SAST findings management
  - DAST testing coverage
  - Penetration testing frequency and scope
  - Vulnerability remediation SLA tracking
  - Excel workbook: Code Review & Testing Assessment

- **ISMS-IMP-A.8.28.4**: Third-Party & OSS Assessment Specification
  - SCA tool implementation
  - SBOM generation and tracking
  - Dependency vulnerability monitoring
  - License compliance management
  - Component approval processes
  - Supply chain security controls
  - Excel workbook: Third-Party & OSS Assessment

- **ISMS-IMP-A.8.28.5**: Compliance Dashboard Specification
  - Executive summary reporting
  - KPI tracking and trending
  - Gap analysis and remediation tracking
  - Annual compliance assessment
  - Audit readiness verification
  - Excel workbook: Secure Coding Compliance Dashboard

**Assessment Tools**:
- Python-generated Excel workbooks with automated compliance calculations
- Data validation dropdowns (Yes/No/Partial/Planned/N/A response values)
- Compliance scoring and gap analysis
- Evidence registers and remediation tracking
- Executive dashboard with trend analysis
- Multi-sheet workbooks (Instructions, Assessment Questions, Gap Analysis, Evidence Register, Approval, Dashboard)

**Supporting Materials**:
- Exception request procedures and templates
- User communication templates (training announcements, policy updates)
- Quick reference guides (Annex B: Developer Quick Reference)
- Incident response playbooks (vulnerability response procedures in Annex A)
- Tool evaluation criteria (SAST/DAST/SCA vendor selection)

**Technical Reference Documents**:
- **ISMS-CTX-A.8.28**: Language-Specific Guidelines (Technical Context Document)
  - Python secure coding patterns
  - Java secure coding patterns
  - JavaScript/TypeScript secure coding patterns
  - C#/.NET secure coding patterns
  - Go secure coding patterns
  - Other languages as used by [Organization]
  - **Document Type**: Internal - Technical Reference (Not ISMS)
  - **Status**: Informational Only
  - **Update Frequency**: Semi-annual or when language versions/frameworks change

- **ISMS-REF-A.8.28**: Code Review Technical Reference
  - Detailed code review checklists by language
  - Security review criteria and patterns
  - Common vulnerability patterns to detect
  - Code review tools and techniques
  - **Document Type**: Internal - Technical Reference (Not ISMS)
  - **Status**: Informational Only
  - **Update Frequency**: Quarterly

**Automation**: All assessment workbooks generated via Python scripts (`generate_a828_1.py` through `generate_a828_5.py` plus `normalize_assessment_files_a828.py`) to ensure consistency, repeatability, and maintainability.

### 4.3 Regulatory Mapping

This policy addresses secure coding requirements from multiple regulatory frameworks:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | HIPAA* | SOX* | DORA/NIS2* |
|---------------------|-----------|---------|-----------|---------|--------|------|------------|
| **Secure Development** | Art. 8 (Security measures) | Art. 25 (Security by design), Art. 32 (Security of processing) | A.8.28 (Secure coding) | Req. 6 (Develop secure systems) | § 164.308(a)(8) (Evaluation) | ITGC (Change management) | Art. 9 (ICT risk management), Art. 21 (Security measures) |
| **Vulnerability Management** | Art. 8 | Art. 32 | A.8.28, A.8.29 | Req. 6.2 (Vulnerabilities), Req. 11.3 (Testing) | § 164.308(a)(8) | ITGC | Art. 9, Art. 26 (Testing) |
| **Code Review** | Art. 8 | Art. 32 | A.8.28 | Req. 6.3.2 (Code review) | § 164.308(a)(8) | ITGC | Art. 9 |
| **Third-Party Components** | Art. 8 | Art. 28 (Processor), Art. 32 | A.8.28, A.8.30 | Req. 6.3.3 (Components), Req. 12.8 (Service providers) | § 164.308(b) (Business associates) | SOC 2 Type II | Art. 28 (Critical services) |
| **Security Testing** | Art. 8 | Art. 32 | A.8.28, A.8.29 | Req. 11 (Security testing) | § 164.308(a)(8) | ITGC | Art. 26 (Threat-led penetration testing) |
| **Developer Training** | Art. 8 | Art. 32 | A.8.28 | Req. 6.1 (Training), Req. 12.6 (Awareness) | § 164.308(a)(5) (Training) | N/A | Art. 21 (Staff awareness) |
| **Change Management** | Art. 8 | Art. 32 | A.8.28, A.8.32 | Req. 6.5 (Change control) | § 164.308(a)(8) | ITGC | Art. 9 |
| **Logging** | Art. 8 | Art. 32, Art. 33 (Breach notification) | A.8.28, A.8.15 | Req. 10 (Logging and monitoring) | § 164.308(a)(1)(ii)(D), § 164.312(b) (Audit controls) | ITGC | Art. 17 (Detection capabilities) |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.8.28.5 (Compliance Dashboard).

### 4.4 Training & Awareness

**Security Awareness** (All Personnel Involved in Development):
- Annual secure coding training module (OWASP Top 10, common vulnerabilities)
- User responsibilities and reporting procedures
- Organizational secure coding standards
- Security tool usage (SAST, SCA in IDE)
- Incident reporting for security issues

**Technical Training** (Developers, QA Engineers, DevOps):
- Secure coding fundamentals (initial training before production code)
- Language-specific secure coding (Python, Java, JavaScript, etc.)
- Threat modeling techniques (STRIDE, PASTA)
- Security testing tools (SAST, DAST, SCA operation)
- Code review security criteria
- Annual refresher training

**Specialized Training** (Security Champions, Application Security Team):
- Advanced threat modeling
- Security architecture and design patterns
- Security tool configuration and tuning
- Penetration testing methodologies
- Incident response for code vulnerabilities
- Conference attendance (AppSec conferences, DEF CON, Black Hat)

**Training Delivery Methods**:
- Internal training materials (developed by Application Security Team)
- External training (SANS, OWASP, vendor-specific courses)
- Hands-on labs and exercises (CTF competitions, vulnerable application practice)
- Lunch-and-learn sessions (Security Champions present to teams)
- Online learning platforms (Secure Code Warrior, HackTheBox, PentesterLab)

**Training Verification**:
- Completion tracked in learning management system (LMS)
- Assessments demonstrating knowledge comprehension
- Training completion percentage reported quarterly
- Non-compliance escalated to Development Manager and CISO

**Continuous Learning**:
- Security Champions community of practice
- Regular security bulletins and vulnerability alerts
- Lessons learned sessions after incidents
- Tool vendor training updates

---

## 5. Definitions

**Application Security (AppSec)**: Discipline focused on securing software applications throughout their lifecycle, from design through deployment and maintenance. Includes secure coding, security testing, vulnerability management, and security architecture.

**Attack Surface**: The sum of all points (attack vectors) where an unauthorized user can try to enter data or extract data from an application. Includes APIs, web forms, file uploads, authentication endpoints, and any interface accepting input.

**Authentication**: Process of verifying the identity of a user, system, or entity. In secure coding context: proper implementation of login, session management, MFA, and credential handling.

**Authorization**: Process of verifying what a user, system, or entity has permission to access or do. In secure coding context: enforcement of access controls, RBAC/ABAC implementation, and prevention of privilege escalation.

**Common Vulnerabilities and Exposures (CVE)**: Publicly disclosed security vulnerabilities with unique identifiers (e.g., CVE-2024-12345) maintained by MITRE Corporation. Used for tracking and referencing specific vulnerabilities.

**Common Vulnerability Scoring System (CVSS)**: Standardized framework for rating vulnerability severity on scale of 0.0-10.0. CVSS v3.1 considers exploitability, scope, and impact to produce severity ratings: None (0.0), Low (0.1-3.9), Medium (4.0-6.9), High (7.0-8.9), Critical (9.0-10.0).

**Common Weakness Enumeration (CWE)**: Community-developed catalog of software and hardware weakness types (e.g., CWE-79 for Cross-Site Scripting). Used for classifying vulnerability types and understanding root causes.

**Compensating Control**: Alternative security control implemented when primary control cannot be implemented. Must provide equivalent protection and be documented with risk acceptance.

**Cross-Site Request Forgery (CSRF)**: Attack forcing authenticated users to execute unwanted actions. Prevention: CSRF tokens, SameSite cookie attribute, double-submit cookies.

**Cross-Site Scripting (XSS)**: Injection vulnerability enabling attackers to inject malicious scripts into web pages viewed by other users. Types: Reflected XSS, Stored XSS, DOM-based XSS. Prevention: output encoding, Content Security Policy, input validation.

**Cryptographically Secure Pseudo-Random Number Generator (CSPRNG)**: Random number generator suitable for cryptographic use. Examples: /dev/urandom, crypto.randomBytes(), SecureRandom. Never use Math.random() or rand() for security.

**Dynamic Application Security Testing (DAST)**: Automated security testing technique analyzing running applications by simulating attacks. Tests applications from outside (black-box testing) to identify runtime vulnerabilities. Examples: OWASP ZAP, Burp Suite, Acunetix.

**False Positive**: Security tool finding incorrectly flagging secure code as vulnerable. Requires manual review and tool tuning to reduce.

**Injection**: Vulnerability class where untrusted data sent to interpreter as part of command or query. Types: SQL injection, command injection, LDAP injection, XPath injection, NoSQL injection. Prevention: parameterized queries, prepared statements, input validation.

**Input Validation**: Process of verifying user input meets expected format, type, length, and range. Whitelist validation preferred (define what IS allowed). Performed server-side, not just client-side.

**Insecure Direct Object Reference (IDOR)**: Vulnerability where application exposes internal implementation objects (database keys, filenames) without proper authorization. Prevention: indirect references, authorization checks before access.

**Interactive Application Security Testing (IAST)**: Hybrid security testing approach combining SAST and DAST by instrumenting running application. Provides real-time vulnerability detection during testing with lower false positive rates.

**Open Web Application Security Project (OWASP)**: Non-profit foundation producing freely-available security tools, documentation, and standards. OWASP Top 10 lists most critical web application security risks.

**Output Encoding**: Process of converting data to safe format for specific context (HTML, JavaScript, URL, SQL, etc.) to prevent injection attacks. Use context-appropriate encoding functions.

**Penetration Testing (Pentest)**: Manual security testing by skilled professionals attempting to exploit vulnerabilities. Types: black-box (no knowledge), gray-box (limited knowledge), white-box (full knowledge). Provides validation of security controls.

**Proof of Concept (PoC)**: Demonstration of vulnerability exploitability. In secure development: PoC code should NEVER be production code (security shortcuts acceptable for prototypes but must be removed).

**Role-Based Access Control (RBAC)**: Authorization approach assigning permissions to roles rather than individual users. Users assigned to roles based on job function. Implements least privilege.

**Secure Development Lifecycle (SDLC)**: Integration of security activities throughout software development lifecycle. Phases: requirements (threat modeling), design (security architecture), implementation (secure coding), testing (SAST/DAST), deployment (security gates), maintenance (vulnerability management).

**Security Champion**: Developer embedded within development team serving as security advocate and liaison to Application Security Team. Participates in threat modeling, reviews security-sensitive code, assists with security questions.

**Security Misconfiguration**: Vulnerability resulting from insecure default configurations, incomplete configurations, or unnecessary features enabled. Examples: default credentials, debugging enabled in production, verbose error messages, missing security headers.

**Sensitive Data Exposure**: Vulnerability where application insufficiently protects sensitive information (PII, financial data, health data, credentials). Prevention: encryption in transit and at rest, proper access controls, data minimization.

**Software Bill of Materials (SBOM)**: Comprehensive inventory of all components (libraries, frameworks, dependencies) in software application. Format: SPDX, CycloneDX. Used for vulnerability tracking and license compliance.

**Software Composition Analysis (SCA)**: Automated analysis of application dependencies (open-source libraries, third-party components) to identify known vulnerabilities and license compliance issues. Examples: Snyk, WhiteSource, Black Duck, Dependabot.

**SQL Injection**: Injection vulnerability where attacker inserts malicious SQL code into queries. Prevention: parameterized queries (prepared statements), ORM frameworks, input validation, least privilege database accounts.

**Static Application Security Testing (SAST)**: Automated source code analysis to identify security vulnerabilities without executing code (white-box testing). Examples: SonarQube, Checkmarx, Fortify, Semgrep. Best practice: integrate into CI/CD pipeline.

**Supply Chain Attack**: Attack targeting less-secure elements in supply chain (compromised dependencies, malicious packages). Examples: event-stream npm incident, SolarWinds breach. Mitigation: SCA tools, dependency verification, SBOM.

**Threat Modeling**: Systematic approach to identifying, analyzing, and mitigating security threats during design phase. Methodologies: STRIDE (Microsoft), PASTA, Attack Trees. Output: threat inventory, risk prioritization, mitigation strategy.

**True Positive**: Security tool finding correctly identifying actual vulnerability. Requires remediation per SLA.

**Vulnerability**: Security weakness in software that could be exploited by attacker. Classified by severity (Critical/High/Medium/Low) using CVSS scoring and organizational impact assessment.

**Zero-Day Vulnerability**: Vulnerability unknown to vendor/public for which no patch exists. Particularly dangerous as attackers have advantage before mitigation available. Response: emergency patching, compensating controls, monitoring.

---

---

## Annex A: Vulnerability Response Procedures

**Purpose**: Operational procedures for handling discovered vulnerabilities in application code.

**Scope**: This annex provides step-by-step procedures operationalizing vulnerability management requirements from Section 2.3.

**When to Use**: When vulnerabilities are discovered through SAST, DAST, SCA, penetration testing, code review, or external security researcher reports.

---

### A.1 Vulnerability Discovery and Initial Response

#### A.1.1 Discovery Sources

**Internal Sources**:
- Automated security scanning (SAST, DAST, SCA, container scanning)
- Manual security testing (code review, penetration testing)
- Development activities (developer reports, architecture reviews)
- Security Champions (issues identified during development)

**External Sources**:
- Security researchers (responsible disclosure, bug bounty)
- Customer reports (security concerns via support)
- Public disclosure (CVE databases, security advisories, news)

#### A.1.2 Initial Actions (Within 24 Hours)

**Step 1 - Log Vulnerability Report**:
- Create ticket in vulnerability tracking system
- Assign unique vulnerability ID
- Record: source, date reported, reporter contact, initial description

**Step 2 - Assign Initial Severity**:
- Preliminary assessment: Critical/High/Medium/Low
- Use CVSS Quick Score or organizational risk matrix
- Note: Severity adjusted during triage

**Step 3 - Assign to Application Security Team**:
- Route to Application Security Team for triage
- Set triage deadline: 48 hours from discovery

**Step 4 - Acknowledge Receipt** (for external reports):
- Respond to reporter within 24 hours
- Confirm receipt, provide tracking ID
- Set expectations: triage timeline, communication frequency

**Template Email**:
```
Subject: Security Report Received - [Tracking ID]

Thank you for reporting a potential security issue. Your report has been logged 
as [Tracking ID] and assigned to our Application Security Team.

Timeline:
- Triage completion: 48 hours
- Initial assessment: 5 business days
- Regular updates provided

Please reference tracking ID for additional information.

Best regards,
[Organization] Security Team
```

---

### A.2 Vulnerability Triage (Within 48 Hours)

#### A.2.1 Validate Vulnerability

**Actions**:
- Reproduce vulnerability in test environment
- Confirm exploitability (theoretical vs. practical)
- Identify affected versions/branches
- Document proof of concept with reproduction steps

**Outcomes**:
- **Valid**: Confirmed vulnerability → proceed to severity assessment
- **False Positive**: No actual vulnerability → document reason, close ticket
- **Needs More Information**: Request clarification from reporter

#### A.2.2 Severity Assessment

**CVSS 3.1 Scoring Framework**:

| Severity | CVSS Score | Exploitability | Impact | Response SLA |
|----------|------------|----------------|--------|--------------|
| **Critical** | 9.0-10.0 | Network, no auth required | RCE, auth bypass, data breach | < 4 hours |
| **High** | 7.0-8.9 | Network, low privilege | SQL injection, privilege escalation | < 8 hours |
| **Medium** | 4.0-6.9 | Auth required, local | Authorization bypass (limited), CSRF | 3 business days |
| **Low** | 0.1-3.9 | Complex exploitation | Information disclosure (minor) | 5 business days |

**Severity Adjustment Factors**:
- **Increase**: Production exposure, sensitive data, regulatory impact
- **Decrease**: Non-production only, compensating controls present, difficult exploitation

#### A.2.3 Impact Analysis

**Assess**:
- **Systems Affected**: Which applications, versions, environments
- **Data Risk**: What data could be accessed/modified
- **User Impact**: How many users affected
- **Business Impact**: Revenue, reputation, compliance implications
- **Regulatory Risk**: GDPR breach notification, other regulatory obligations

#### A.2.4 Assign Owner and Remediation Timeline

**Ownership**:
- **Development Team**: Owns code, implements fix
- **Application Security Team**: Validates fix, tracks to closure
- **Security Architect**: Consulted for architectural fixes

**Remediation SLAs** (from discovery to fix deployed):

| Severity | Production | Non-Production | Exception Approval |
|----------|-----------|----------------|-------------------|
| **Critical** | 7 days | 14 days | CISO only |
| **High** | 30 days | 60 days | Application Security Lead + Dev Manager |
| **Medium** | 90 days | 120 days | Dev Manager |
| **Low** | 180 days | Next major release | Dev Manager |

**SLA Clock Starts**: Date vulnerability validated (not reported)

---

### A.3 Remediation Planning and Execution

#### A.3.1 Remediation Strategy Selection

**Options** (in order of preference):

1. **Code Fix** (permanent remediation):
   - Fix root cause in code
   - Deploy to all affected versions
   - Preferred for all vulnerabilities

2. **Configuration Change** (if code fix not immediately possible):
   - Disable vulnerable feature
   - Apply restrictive configuration
   - Temporary until code fix deployed

3. **Compensating Controls** (short-term risk reduction):
   - WAF rules blocking exploit attempts
   - Network restrictions limiting access
   - Enhanced monitoring and alerting
   - Not a permanent solution

4. **Risk Acceptance** (last resort):
   - Vulnerability remains unpatched
   - Requires CISO approval and documented justification
   - Only for low-severity with mitigating circumstances

#### A.3.2 Fix Development Process

**Step 1 - Create Fix Branch**:
- Branch from affected version: `security/vuln-[ID]-[description]`
- Never commit sensitive information (PoC exploits, vulnerability details)

**Step 2 - Develop Fix**:
- Implement fix addressing root cause (not just symptoms)
- Add regression test preventing recurrence
- Update security test cases
- Document fix approach

**Step 3 - Security Review**:
- Application Security Team reviews fix
- Validates vulnerability eliminated
- Checks for unintended side effects
- May request revisions

**Step 4 - Testing**:
- Unit tests (fix doesn't break functionality)
- Security tests (vulnerability eliminated)
- Regression tests (no new issues introduced)
- Performance tests (if relevant)

**Step 5 - Deployment**:
- Follow standard change management process
- Prioritize deployment per severity SLA
- Emergency change process for Critical vulnerabilities
- Document deployment date and version

#### A.3.3 Verification

**Validation Steps**:
- Re-scan with security tools (SAST, DAST, SCA)
- Manual verification by Application Security Team
- Penetration testing for Critical/High vulnerabilities
- Confirm fix deployed to all affected environments

**Verification Evidence**:
- Scan results showing vulnerability resolved
- Test results demonstrating fix effectiveness
- Deployment logs confirming version deployed

---

### A.4 Communication and Disclosure

#### A.4.1 Internal Communication

**Stakeholders to Inform**:
- **Critical/High**: CISO, CTO, affected Development Teams, Security Team
- **Medium**: Application Security Team, affected Development Teams
- **Low**: Development Teams only

**Communication Content**:
- Vulnerability summary (severity, impact, affected systems)
- Remediation plan and timeline
- Actions required from teams
- Status updates (weekly for Critical/High, monthly for Medium/Low)

#### A.4.2 External Communication

**Security Researchers**:
- Acknowledge triage completion
- Provide severity assessment and timeline
- Update on remediation progress (at agreed intervals)
- Notify when fix deployed
- Credit researcher (if desired and appropriate)

**Customers** (if vulnerability affects them):
- Inform if data breach or service impact
- Provide remediation guidance
- Offer support and mitigation steps
- Follow breach notification requirements (GDPR, etc.)

**Public Disclosure** (coordinated):
- Wait until fix deployed (typically 90 days from vendor notification)
- CVE assignment for significant vulnerabilities
- Security advisory published
- Credit security researcher appropriately

#### A.4.3 Disclosure Timeline

**Standard Process**:
1. Day 0: Vulnerability reported
2. Day 2: Triage completed
3. Day 7-30: Fix developed (per severity)
4. Day 30-90: Fix deployed to production
5. Day 90+: Public disclosure (if applicable)

**Accelerated Timeline** (for active exploitation):
- Immediate containment (< 4 hours)
- Hotfix development (< 24-48 hours)
- Emergency deployment
- Public advisory if necessary

---

### A.5 Closure and Lessons Learned

#### A.5.1 Closure Criteria

Vulnerability closed when:
- Fix deployed to all affected environments
- Verification tests confirm vulnerability eliminated
- Security tools no longer flag issue
- Application Security Team approves closure
- Documentation completed

**Documentation Requirements**:
- Vulnerability summary and severity
- Root cause analysis (how introduced)
- Fix description and deployment evidence
- Lessons learned for prevention

#### A.5.2 Lessons Learned Session

**Conduct for Critical/High vulnerabilities**:

**Participants**: Development Team, Application Security Team, Security Architect, DevOps

**Discussion Points**:
1. How was vulnerability introduced?
2. Why wasn't it caught earlier (code review, testing)?
3. What process/tool improvements prevent recurrence?
4. Training needs identified?
5. Policy/standard updates required?

**Outputs**:
- Process improvement actions (assigned owner, due date)
- Tool tuning recommendations (SAST rules, DAST coverage)
- Training material updates
- Policy amendments (if needed)

#### A.5.3 Metrics and Reporting

**Track and Report**:
- **Vulnerability volume**: Count by severity, trending over time
- **Time to remediate**: Average days from discovery to closure
- **SLA compliance**: % vulnerabilities remediated within SLA
- **Recurrence rate**: Same vulnerability type reintroduced
- **Source effectiveness**: Which detection methods finding most issues

**Reporting Frequency**:
- **Monthly**: Development Managers (team-level metrics)
- **Quarterly**: CISO, Executive Management (program-level trends)
- **Annual**: Board of Directors (risk posture, maturity)

---

## Annex B: Developer Quick Reference Guide

**Purpose**: One-page security cheat sheet for daily development.

**When to Use**: Daily coding, pre-commit checks, new projects, quick security reminders.

**This guide is NOT comprehensive** - for detailed guidance see:
- Language-specific patterns → ISMS-CTX-A.8.28 (Language Guidelines)
- Code review criteria → ISMS-REF-A.8.28 (Code Review Reference)
- Vulnerability handling → Annex A (Vulnerability Response Procedures)
- Full policy → Sections 2.1-2.4 (Requirements Framework)

---

### B.1 Secure Coding Top 10 Principles

**1. Validate All Input**
- Trust nothing: users, databases, APIs, files, environment variables
- Server-side validation always (client-side is UX only, not security)
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
- Use proven libraries (bcrypt, crypto libraries, sanitizers)
- Keep frameworks updated

**5. Fail Securely**
- Default deny (whitelist approach)
- Never fail open (authentication fails → deny access, not grant)
- Generic error messages to users (log details server-side)

**6. Hash Passwords Properly**
- bcrypt (cost factor 12+), Argon2, or scrypt
- Never MD5, SHA1, SHA256 alone (even with salt)
- Never store plaintext passwords (not even temporarily)

**7. No Hardcoded Secrets**
- Environment variables or secret manager only
- No API keys, passwords, tokens, private keys in code
- Scan for secrets before commit (use pre-commit hooks)

**8. Keep Dependencies Updated**
- Monitor SCA alerts daily
- Patch within SLA (Critical: 7 days, High: 30 days)
- Pin dependency versions (lock files: package-lock.json, requirements.txt)

**9. Review Your Code**
- Peer review mandatory (security checklist for high-risk changes)
- Read your own changes before submitting PR
- Think like an attacker: "How could I exploit this?"

**10. Test for Security**
- Write security test cases (negative tests, boundary tests)
- Don't assume it works - verify with tests
- Test authentication, authorization, input validation

---

### B.2 Pre-Commit Checklist (2 Minutes)

Run through this BEFORE submitting PR:

- [ ] **No secrets in code**: Search for `password`, `api_key`, `token`, `secret`
  - *Tool*: `git diff | grep -iE "(password|api_key|secret|token)"`

- [ ] **Input validation present**: All user input validated server-side
  - *Check*: Forms, URL params, headers, API requests

- [ ] **Output encoding correct**: XSS prevention applied
  - *Check*: Template auto-escaping enabled, no `innerHTML` with user input

- [ ] **SQL queries parameterized**: No string concatenation in queries
  - *Check*: All database queries use parameters or ORM

- [ ] **No vulnerable dependencies**: SCA scan green
  - *Tool*: `npm audit`, `pip-audit`, or CI/CD check

- [ ] **Code reviewed locally**: Read your own changes critically
  - *Ask*: "How could I exploit this?"

- [ ] **Tests passing**: Including security tests
  - *Check*: Unit tests, integration tests green

- [ ] **Commit message clear**: What changed and why
  - *Format*: "Fix SQL injection in user search [VULN-123]"

---

### B.3 Quick Tool Reference

| Tool | Purpose | Usage | Frequency |
|------|---------|-------|-----------|
| **SAST** | Find code vulnerabilities | Automatic in CI/CD | Every commit |
| **SCA** | Find dependency vulnerabilities | Automatic in CI/CD | Every build |
| **Secret Scanner** | Detect committed secrets | Pre-commit hook + CI/CD | Before commit |
| **Linter** | Enforce coding standards | IDE integration | While coding |
| **DAST** | Test running application | QA environment | Weekly/per release |

---

### B.4 Security Contacts

**Questions or Issues?**

| Need | Contact | Channel |
|------|---------|---------|
| **Security guidance** | Security Champion (your team) | Slack #security-champions |
| **Vulnerability report** | Application Security Team | security@[organization].com |
| **Code review support** | Application Security Team | Slack #appsec |
| **Tool issues** | DevOps Team | Slack #devops-support |
| **Urgent security issue** | CISO / Security Team | Incident response hotline |

**External Reporting**: security@[organization].com (PGP key available)

---

### B.5 Common Vulnerability Patterns to Avoid

| Vulnerability | Bad Code Pattern | Secure Alternative |
|---------------|------------------|-------------------|
| **SQL Injection** | `query = "SELECT * FROM users WHERE id=" + user_id` | Use parameterized queries: `cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))` |
| **XSS** | `element.innerHTML = user_input` | Use textContent or framework auto-escaping |
| **Hardcoded Secret** | `API_KEY = "sk-1234567890abcdef"` | Use environment variables: `API_KEY = os.environ['API_KEY']` |
| **Weak Hash** | `hash = md5(password)` | Use bcrypt: `hash = bcrypt.hashpw(password, bcrypt.gensalt())` |
| **Command Injection** | `os.system("ping " + user_input)` | Use parameterized calls: `subprocess.run(['ping', user_input])` |
| **Path Traversal** | `open("/uploads/" + filename)` | Validate filename: `safe_filename = os.path.basename(filename)` |

---

### B.6 Resources and Training

**Internal Resources**:
- Secure Coding Wiki: [internal-wiki]/security/secure-coding
- Training Portal: [LMS]/security-training
- Code Review Checklist: ISMS-REF-A.8.28
- Language Guidelines: ISMS-CTX-A.8.28

**External Resources**:
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- CWE Top 25: https://cwe.mitre.org/top25/

**Training Available**:
- Annual secure coding training (mandatory)
- Language-specific training (Python, Java, JavaScript)
- Security Champions advanced training
- Conference attendance (AppSec conferences)

---

*"The first principle is that you must not fool yourself—and you are the easiest person to fool." - Richard Feynman*

**Application**: Security theater (policies without evidence) provides zero protection. Write code that is measurably secure, not code that looks secure.

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Technology Officer (CTO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.28. Technical reference information is provided in ISMS-CTX-A.8.28 and ISMS-REF-A.8.28.*