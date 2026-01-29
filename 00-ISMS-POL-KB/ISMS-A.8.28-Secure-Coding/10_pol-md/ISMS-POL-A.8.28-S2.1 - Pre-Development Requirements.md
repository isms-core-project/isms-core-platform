# ISMS-POL-A.8.28-S2.1
## Secure Coding - Pre-Development Requirements

**Document ID**: ISMS-POL-A.8.28-S2.1
**Title**: Secure Coding - Pre-Development Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead / Security Architect | Initial pre-development requirements |

**Review Cycle**: Annual (or upon significant changes to SDLC methodology)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead / Security Architect
- Process Owner: Development Manager / Engineering Director
- Compliance Review: Legal/Compliance Officer

**Distribution**: Development managers, architects, security team, project managers  
**Related Documents**: ISMS-POL-A.8.28-S2 (Requirements Overview), ISMS-IMP-A.8.28.1 (SDLC Assessment)

---

## 2.1.1 Introduction

This section establishes security requirements for the **pre-development phase** - activities performed before writing production code. Pre-development security activities are the most cost-effective phase for preventing vulnerabilities, as discovered by Barry Boehm's research: fixing defects in requirements/design costs 5-10x less than fixing them in implementation, and 100x less than fixing them post-deployment.

*"The question of whether computers can think is like the question of whether submarines can swim."* - Edsger Dijkstra

**Application to Secure Development**: Just as submarines achieve their purpose through engineering rather than mimicking fish, secure software is achieved through systematic engineering discipline, not through hoping developers intuitively avoid vulnerabilities.

**Pre-Development Phase Coverage**:
- Security requirements definition and analysis
- Threat modeling and attack surface analysis
- Secure architecture and design principles
- Developer security training and qualification
- Development environment security configuration
- Security planning and resource allocation

**Primary Stakeholders**: Security Architects, Application Security Team, Development Managers, Project Managers

---

## 2.1.2 Security Requirements Definition

### 2.1.2.1 Mandatory Requirements

All development projects **SHALL**:

**REQ-2.1.2.1-A: Document Security Requirements**
- Identify and document security requirements as part of project requirements gathering
- Security requirements must be:
  - **Specific**: Clear, unambiguous statements (e.g., "User passwords must be hashed using bcrypt with cost factor ≥12")
  - **Measurable**: Testable through automated or manual verification
  - **Approved**: Reviewed and accepted by Application Security Team
  - **Traceable**: Linked to specific security controls, threats, or compliance obligations
  - **Prioritized**: Classified by criticality (Critical/High/Medium/Low)

**REQ-2.1.2.1-B: Conduct Security Risk Assessment**
- Perform security-focused risk assessment for:
  - New applications or systems
  - Major feature additions to existing systems
  - Applications processing sensitive data (PII, financial, health, confidential business information)
  - Public-facing applications or APIs
  - Changes affecting authentication, authorization, or cryptography

Risk assessment must:
- Identify security risks specific to the application context
- Evaluate likelihood and impact of security incidents
- Document risk treatment decisions (mitigate, accept, transfer, avoid)
- Receive CISO or Application Security Lead approval

**REQ-2.1.2.1-C: Define Security Acceptance Criteria**
- Establish security acceptance criteria before development begins
- Criteria must be documented in project requirements or user stories
- Minimum criteria include:
  - No unresolved Critical or High severity vulnerabilities
  - Security test cases passed (unit, integration, SAST, DAST)
  - Code review completed with security sign-off
  - Third-party components scanned and approved
  - Security documentation completed

**REQ-2.1.2.1-D: Align with Regulatory Requirements**
- Identify applicable regulations and compliance obligations:
  - Data protection regulations (GDPR, FADP, etc.)
  - Industry-specific requirements (PCI-DSS, HIPAA, etc.)
  - Contractual security obligations
- Document how security requirements address compliance obligations
- Obtain Legal/Compliance review for high-risk applications

### 2.1.2.2 Security Requirement Categories

Security requirements should address all relevant categories:

| Category | Examples | Assessment Reference |
|----------|----------|---------------------|
| **Authentication** | MFA requirements, password policies, session management | IMP-A.8.28.2 |
| **Authorization** | RBAC model, least privilege, segregation of duties | IMP-A.8.28.2 |
| **Data Protection** | Encryption at rest/in transit, data retention, PII handling | IMP-A.8.28.2 |
| **Input Validation** | Whitelist validation, sanitization, injection prevention | IMP-A.8.28.2 |
| **Output Encoding** | XSS prevention, context-aware encoding | IMP-A.8.28.2 |
| **Cryptography** | Algorithm selection, key management, secure RNG | IMP-A.8.28.2 |
| **Error Handling** | Secure error messages, exception management | IMP-A.8.28.2 |
| **Logging & Monitoring** | Security event logging, audit trail requirements | IMP-A.8.28.2 |
| **API Security** | Authentication, rate limiting, input validation | IMP-A.8.28.2 |
| **Configuration** | Security defaults, hardening requirements | IMP-A.8.28.2 |

---

## 2.1.3 Threat Modeling

### 2.1.3.1 Mandatory Threat Modeling Requirements

**REQ-2.1.3.1-A: Threat Modeling for High-Risk Applications**

Threat modeling is **REQUIRED** for:
- New applications handling sensitive data
- Major architectural changes to existing applications
- Public-facing applications or APIs
- Applications integrating with critical business systems
- Applications processing financial transactions or PII

Threat modeling is **RECOMMENDED** but not mandatory for:
- Internal tools with limited sensitive data exposure
- Minor feature additions without architectural changes
- Applications operating in isolated, low-trust environments

**REQ-2.1.3.1-B: Threat Modeling Timing**
- Conduct threat modeling during design phase, before significant development begins
- Update threat models when:
  - Architecture significantly changes
  - New attack vectors are discovered
  - Regulatory requirements change
  - Post-incident analysis identifies threat model gaps

**REQ-2.1.3.1-C: Threat Modeling Documentation**

Threat models must document:

1. **System Overview**
   - Architecture diagram (data flow, trust boundaries)
   - External dependencies and integrations
   - User roles and privilege levels
   - Data classification (sensitivity levels)

2. **Threat Identification**
   - Potential threats using structured methodology (STRIDE, PASTA, Attack Trees, etc.)
   - Attack scenarios and attacker profiles
   - Attack surface analysis

3. **Threat Prioritization**
   - Risk rating for each identified threat (likelihood × impact)
   - DREAD or CVSS-based scoring where applicable

4. **Mitigation Strategy**
   - Security controls to address high-priority threats
   - Mapping of controls to specific threats
   - Residual risk assessment and acceptance

5. **Validation Plan**
   - How mitigations will be verified (testing, code review, configuration audit)

### 2.1.3.2 Threat Modeling Methodologies

Organizations may use any threat modeling methodology appropriate to their context:

**STRIDE** (Microsoft model - recommended for general applications):
- **S**poofing identity
- **T**ampering with data
- **R**epudiation
- **I**nformation disclosure
- **D**enial of service
- **E**levation of privilege

**PASTA** (Process for Attack Simulation and Threat Analysis - recommended for risk-focused analysis):
- Stage-based methodology linking business objectives to technical risks
- Particularly useful for compliance-driven environments

**Attack Trees** (recommended for specific threat scenario analysis):
- Visual representation of attack paths
- Useful for identifying required combinations of vulnerabilities

**OWASP Threat Dragon / Microsoft Threat Modeling Tool**:
- Tool-assisted threat modeling
- Suitable for teams new to threat modeling

### 2.1.3.3 Threat Model Review and Approval

**REQ-2.1.3.3-A: Security Team Review**
- Threat models must be reviewed by Application Security Team or Security Architect
- Review verifies:
  - Completeness of threat identification
  - Appropriateness of risk ratings
  - Adequacy of mitigation strategies
  - Alignment with organizational risk appetite

**REQ-2.1.3.3-B: Approval Authority**
- Threat models for high-risk applications: CISO or Application Security Lead approval required
- Threat models for medium-risk applications: Security Architect approval required
- Approved threat models must be retained as part of project documentation

---

## 2.1.4 Secure Architecture and Design

### 2.1.4.1 Security-by-Design Principles

All applications **SHALL** incorporate the following security-by-design principles:

**REQ-2.1.4.1-A: Defense in Depth**
- Multiple layers of security controls
- No single point of failure for security
- Example: Authentication + authorization + input validation + output encoding (not just authentication alone)

**REQ-2.1.4.1-B: Least Privilege**
- Users, processes, and systems granted minimum necessary permissions
- Time-limited privileges where appropriate (JIT - Just-In-Time access)
- Regular review and revocation of unnecessary permissions

**REQ-2.1.4.1-C: Fail Securely**
- System failures must default to secure state
- Error conditions must not expose sensitive information
- Graceful degradation maintaining security controls

**REQ-2.1.4.1-D: Separation of Duties**
- Critical operations require multiple independent actions
- No single user can compromise security end-to-end
- Example: Code commit + peer review + security scan + approval

**REQ-2.1.4.1-E: Economy of Mechanism**
- Simple designs are easier to secure and verify
- Avoid unnecessary complexity
- Clear separation of concerns

**REQ-2.1.4.1-F: Complete Mediation**
- Every access to every object must be checked for authorization
- No caching of security decisions that could be bypassed

**REQ-2.1.4.1-G: Open Design**
- Security through obscurity is not acceptable as primary control
- Assume attackers have full knowledge of system design
- Security depends on secrets (keys, credentials) not on design secrecy

**REQ-2.1.4.1-H: Psychological Acceptability**
- Security mechanisms must be usable by developers and users
- Overly complex security drives workarounds and bypasses
- Balance security with usability

### 2.1.4.2 Architecture Security Review

**REQ-2.1.4.2-A: Architecture Review for High-Risk Systems**

Architecture security review is **REQUIRED** for:
- New applications (greenfield development)
- Major architectural refactoring
- Integration with external systems or third-party services
- Cloud migration or multi-cloud architecture
- Microservices or distributed system architecture

Architecture review must verify:
- Application of security-by-design principles
- Secure communication patterns (encryption, authentication)
- Trust boundary definition and enforcement
- Authentication and authorization model
- Data flow and storage security
- Secret management approach
- Logging and monitoring strategy
- Incident response capabilities

**REQ-2.1.4.2-B: Review Participants**
- Minimum attendees: Security Architect, Application Security Lead, Solution Architect
- Optional: Development Lead, Infrastructure Architect, Compliance Officer

**REQ-2.1.4.2-C: Review Documentation**
- Architecture diagrams (logical and physical)
- Data flow diagrams
- Trust boundary maps
- Integration points and external dependencies
- Security control inventory

Review outcomes must be documented with:
- Identified security concerns and recommendations
- Required remediation actions before development proceeds
- Approval or conditional approval with follow-up

### 2.1.4.3 Secure Design Patterns

**REQ-2.1.4.3-A: Use of Approved Design Patterns**

Developers should leverage secure design patterns addressing common security challenges:

| Security Challenge | Recommended Pattern | Reference |
|-------------------|---------------------|-----------|
| Authentication | OAuth 2.0 / OpenID Connect for web/mobile; Kerberos for enterprise | ISMS-POL-A.8.28-S5.A |
| Authorization | RBAC (Role-Based Access Control) or ABAC (Attribute-Based) | ISMS-POL-A.8.28-S5.A |
| Session Management | Stateless JWT with refresh tokens; or server-side session with secure cookies | ISMS-POL-A.8.28-S2.2 |
| Input Validation | Whitelist validation with sanitization libraries | ISMS-POL-A.8.28-S2.2 |
| Cryptography | Use vetted crypto libraries; never implement custom crypto | ISMS-POL-A.8.28-S2.2 |
| Secrets Management | Vault-based (HashiCorp Vault, Azure Key Vault, AWS Secrets Manager) | ISMS-POL-A.8.28-S2.2 |
| API Security | API Gateway with rate limiting, authentication, and input validation | ISMS-POL-A.8.28-S5.A |

---

## 2.1.5 Developer Security Training

### 2.1.5.1 Mandatory Training Requirements

**REQ-2.1.5.1-A: Initial Secure Coding Training**

All developers **MUST** complete secure coding training:
- **Timing**: Within 30 days of starting development work
- **Duration**: Minimum 4 hours of interactive training
- **Content Coverage**:
  - OWASP Top 10 vulnerabilities
  - Secure coding principles
  - Common vulnerability patterns (injection, XSS, authentication flaws, etc.)
  - Organization-specific coding standards
  - Use of security tools (SAST, SCA, etc.)

**REQ-2.1.5.1-B: Annual Refresher Training**
- Annual secure coding training for all active developers
- Minimum 2 hours annually
- Updated content reflecting current threat landscape and new vulnerabilities

**REQ-2.1.5.1-C: Language-Specific Training**
- Developers must complete training specific to their primary programming language(s)
- Training addresses language-specific vulnerabilities and secure coding practices
- Examples: Java secure coding (deserialization, XXE), JavaScript (XSS, prototype pollution), Python (pickle vulnerabilities, SQL injection)

**REQ-2.1.5.1-D: Training Documentation**
- Training completion tracked in HR/LMS system
- Training records retained for audit purposes (minimum 3 years)
- Non-completion of required training may result in restricted code commit privileges

### 2.1.5.2 Advanced Security Training

**REQ-2.1.5.2-A: Security Champions Program**

Organizations **SHOULD** establish a Security Champions program:
- Identify developer volunteers interested in security
- Provide advanced security training (threat modeling, secure architecture, security testing)
- Security champions serve as security advocates within development teams
- Security champions receive quarterly training updates
- Minimum 1 security champion per 10 developers (recommended)

**REQ-2.1.5.2-B: Specialist Training**

Specialist training recommended for:
- **Security Team Members**: Advanced offensive security, penetration testing, SAST/DAST tool tuning
- **Architects**: Secure architecture, cloud security, zero-trust architecture
- **DevOps Engineers**: CI/CD pipeline security, infrastructure-as-code security, container security
- **Incident Responders**: Forensics, malware analysis, incident handling

### 2.1.5.3 Training Effectiveness Measurement

**REQ-2.1.5.3-A: Training Assessment**

Organizations **SHOULD** measure training effectiveness through:
- Pre/post training knowledge assessments
- Reduction in vulnerability density over time
- Developer security awareness in code reviews
- Security champion engagement levels
- Feedback surveys from training participants

---

## 2.1.6 Development Environment Security

### 2.1.6.1 Development Workstation Security

**REQ-2.1.6.1-A: Baseline Security Configuration**

Developer workstations **MUST** meet organizational security baseline:
- Full-disk encryption enabled
- Endpoint protection (antivirus/EDR) installed and active
- Firewall enabled with restrictive default-deny rules
- Automatic security updates enabled for OS and critical applications
- Screensaver lock after 10 minutes of inactivity
- No local administrator rights for daily development work (use separate admin account for privileged tasks)

**REQ-2.1.6.1-B: Secure Development Tools**

Development tools and IDEs **SHOULD** be configured with:
- Security linters and static analysis plugins enabled
- Automatic code formatting to prevent accidental security issues
- Version control integration (Git, SVN, etc.)
- Secret detection plugins preventing credential commits
- Regular tool updates and patch management

### 2.1.6.2 Source Code Repository Security

**REQ-2.1.6.2-A: Repository Access Controls**

Source code repositories **MUST** implement:
- Multi-factor authentication (MFA) for all repository access
- Role-based access control (developers, reviewers, administrators)
- Least privilege access (developers only access repositories for their projects)
- Automated access review and revocation for departed employees
- Audit logging of all repository access and changes

**REQ-2.1.6.2-B: Branch Protection Rules**

Production/main branches **MUST** be protected with:
- Prohibition of direct commits (all changes via pull request)
- Requirement for code review approval before merge
- Passing CI/CD security checks before merge
- Signed commits (GPG or SSH signature) where feasible
- Restriction of force-push and branch deletion

**REQ-2.1.6.2-C: Secret Management**

Developers **MUST NOT**:
- Commit credentials, API keys, or secrets to repositories (even private repos)
- Store secrets in code comments or configuration files
- Share secrets via email, chat, or unencrypted channels

Developers **MUST**:
- Use environment variables or secret management systems for credentials
- Use `.gitignore` to prevent accidental secret commits
- Utilize pre-commit hooks to detect and block secret commits
- Rotate credentials immediately if accidentally committed (even if reverted)

### 2.1.6.3 Build and CI/CD Pipeline Security

**REQ-2.1.6.3-A: Secure Build Pipeline**

CI/CD pipelines **MUST** incorporate:
- Automated SAST scanning on every commit or pull request
- Automated SCA (dependency vulnerability scanning) on every build
- Security test execution as part of automated testing
- Secrets scanning to detect accidental credential exposure
- Build artifact signing for integrity verification

**REQ-2.1.6.3-B: Deployment Gates**

Pipelines deploying to production **MUST** include security gates:
- No Critical or High severity vulnerabilities in passing builds
- Required security testing passed (SAST, DAST, SCA)
- Code review approval documented
- Manual security approval for high-risk changes
- Automated rollback capability if security issues detected post-deployment

### 2.1.6.4 Development/Test Data Security

**REQ-2.1.6.4-A: Production Data Restrictions**

Developers **MUST NOT**:
- Use production data in development or test environments without explicit authorization
- Extract production data for local testing
- Share production database credentials

**REQ-2.1.6.4-B: Test Data Requirements**

If production data is required for testing:
- Obtain written approval from Data Protection Officer and CISO
- Apply data masking/anonymization to PII and sensitive data
- Limit data extraction to minimum necessary records
- Enforce same access controls as production environment
- Delete test data when no longer needed

**REQ-2.1.6.4-C: Synthetic Test Data**

Organizations **SHOULD**:
- Use synthetic/mock data for development and testing where possible
- Invest in test data generation tools
- Maintain test data sets representing realistic scenarios without using production data

---

## 2.1.7 Security Planning and Resource Allocation

### 2.1.7.1 Security Activity Integration

**REQ-2.1.7.1-A: Security in Project Planning**

Project plans **MUST** include:
- Time allocation for security activities (threat modeling, code review, security testing)
- Security milestones and checkpoints
- Security resource requirements (Application Security Team involvement)
- Risk assessment and mitigation planning
- Security training needs for project team

**REQ-2.1.7.1-B: Agile/Sprint Planning**

For Agile development:
- Security stories explicitly included in sprint backlogs
- "Definition of Done" includes security criteria (code review, SAST passed, vulnerabilities addressed)
- Security sprint retrospectives to identify security process improvements
- Security representation in sprint planning meetings for high-risk projects

### 2.1.7.2 Security Resource Requirements

**REQ-2.1.7.2-A: Application Security Team Engagement**

Projects **MUST** engage Application Security Team for:
- Threat modeling (for high-risk applications)
- Architecture security review (for new applications or major changes)
- Security test plan review
- Penetration testing coordination
- Security incident response planning

**REQ-2.1.7.2-B: Budget Allocation**

Project budgets **SHOULD** include:
- Security tooling costs (SAST, DAST, SCA licenses)
- Security training costs
- External security assessment costs (penetration testing, security audit)
- Security-related technical debt remediation

---

## 2.1.8 Compliance and Evidence

### 2.1.8.1 Pre-Development Documentation Requirements

For audit and compliance purposes, projects **MUST** maintain:

| Artifact | Purpose | Retention |
|----------|---------|-----------|
| Security requirements document | Define security controls and acceptance criteria | Duration of application lifetime |
| Threat model | Document identified threats and mitigations | Duration of application lifetime (updated periodically) |
| Architecture diagrams | Show trust boundaries and security controls | Duration of application lifetime (version controlled) |
| Security risk assessment | Risk decisions and approvals | 7 years (regulatory requirement) |
| Training records | Developer security training completion | 3 years minimum |
| Security review approvals | Architecture/design security sign-off | Duration of application lifetime |

### 2.1.8.2 Assessment Integration

Pre-development requirements compliance is assessed in:
- **ISMS-IMP-A.8.28.1**: SDLC Assessment (Section: Pre-Development Phase)

Evidence includes:
- Documented security requirements in project documentation
- Completed threat models with approval signatures
- Architecture review meeting minutes and decisions
- Developer training completion certificates
- Security activity inclusion in project plans/sprint backlogs

---

**END OF DOCUMENT**

*"It is not the strongest of the species that survives, nor the most intelligent, but the one most responsive to change." - Charles Darwin*

**Application to Secure Development**: Organizations that continuously adapt their secure development practices to evolving threats, technologies, and lessons learned will produce the most secure software.