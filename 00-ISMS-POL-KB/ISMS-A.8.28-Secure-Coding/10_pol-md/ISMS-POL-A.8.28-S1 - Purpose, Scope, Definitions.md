# ISMS-POL-A.8.28-S1
## Secure Coding - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.8.28-S1
**Title**: Secure Coding - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / Application Security Lead | Initial foundational document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead / Development Manager
- Compliance Review: Legal/Compliance Officer

**Distribution**: Development teams, security teams, DevOps, architecture review boards  
**Related Documents**: ISMS-POL-A.8.28 (Master), ISO/IEC 27001:2022 A.8.28

---

## 1.1 Purpose

### 1.1.1 Policy Objective

This document establishes the purpose, scope, and key definitions for the organization's Secure Coding policy framework, implementing ISO/IEC 27001:2022 Annex A Control 8.28 (Secure Coding).

The policy framework aims to:

- **Prevent** security vulnerabilities from being introduced during software development
- **Establish** secure coding standards and practices across all development activities
- **Enable** developers to create secure, resilient, and maintainable code
- **Reduce** the attack surface through secure-by-design principles
- **Detect** vulnerabilities early through code review and security testing
- **Comply** with legal, regulatory, and contractual security requirements for software development

*"It doesn't matter how beautiful your theory is, it doesn't matter how smart you are. If it doesn't agree with experiment, it's wrong."* - Richard Feynman

This policy embraces empirical verification: secure coding isn't about following rituals, it's about producing measurably more secure software through systematic engineering discipline.

### 1.1.2 Control Alignment

This policy implements ISO/IEC 27001:2022 Annex A.8.28:

> **A.8.28 Secure Coding**  
> *Rules for secure coding shall be applied to software development.*

The control guidance (ISO 27002:2022) emphasizes:
- Organizational expectations and recognized principles for secure coding
- Common coding practices and errors leading to security vulnerabilities
- Configuration of development tools to enforce secure code creation
- Developer training in writing secure code
- Secure design and architecture, including threat modeling
- Use of secure programming standards
- Code review and security testing during and after development

### 1.1.3 Risk Management Context

Secure coding serves as a **preventive control** addressing software security risks throughout the development lifecycle. Software vulnerabilities represent significant organizational risk:

**Business Impacts:**
- Data breaches exposing confidential or personal information
- Service disruptions from exploited vulnerabilities
- Financial losses from incident response, remediation, and potential fines
- Reputational damage affecting customer trust and business relationships
- Intellectual property theft through application exploitation
- Regulatory sanctions for failure to protect data adequately

**Attack Vectors Addressed:**
- Injection attacks (SQL, command, LDAP, XPath, etc.)
- Authentication and session management flaws
- Cross-site scripting (XSS) and cross-site request forgery (CSRF)
- Insecure deserialization and object manipulation
- Security misconfiguration vulnerabilities
- Exposure of sensitive data through inadequate protection
- Insufficient logging and monitoring enabling undetected breaches
- Use of components with known vulnerabilities

The organization recognizes that **"shifting security left"** (addressing security early in development) is more effective and economical than attempting to retrofit security into completed software. This policy establishes requirements that integrate security throughout the software development lifecycle (SDLC).

---

## 1.2 Scope

### 1.2.1 In Scope

This policy framework applies to:

**Development Activities**:
- New software development (greenfield projects)
- Software modifications and enhancements (existing systems)
- Software maintenance (bug fixes, patches, updates)
- Prototypes and proof-of-concept implementations intended for production
- Scripts and automation code with security implications
- Infrastructure-as-Code (IaC) and configuration management code
- API development (RESTful, GraphQL, SOAP, gRPC, etc.)
- Microservices and containerized application development
- Mobile application development (iOS, Android, cross-platform)
- Web application and web service development
- Database schema and stored procedure development
- Security-relevant scripts (PowerShell, Python, Bash, etc.)

**Development Types**:
- **Internal development** - Software developed by organizational staff
- **Outsourced development** - Software developed by external contractors, vendors, or offshore teams
- **Hybrid development** - Collaborative development involving internal and external resources
- **Open-source integration** - Integration and customization of open-source software
- **Low-code/no-code development** - Applications built using visual development platforms where security configuration is required

**Development Environments**:
- Development workstations and development VMs
- Development infrastructure (repositories, CI/CD pipelines, build servers)
- Test environments where code execution occurs
- Integration and staging environments
- Development containers and cloud development environments

**Personnel**:
- Software developers (all levels and specializations)
- DevOps engineers and site reliability engineers (SREs)
- Database administrators and developers
- Security engineers and security champions
- QA engineers and test automation specialists
- Technical architects and solution designers
- Third-party developers with access to organizational code repositories
- Contractors and consultants performing development work

**Programming Languages and Technologies**:
All programming languages and development frameworks used by the organization, including but not limited to:
- Object-oriented languages (Java, C#, Python, C++, etc.)
- Web languages (JavaScript, TypeScript, PHP, Ruby, etc.)
- Functional languages (Scala, Haskell, Clojure, etc.)
- Systems languages (C, C++, Rust, Go, etc.)
- Scripting languages (Python, PowerShell, Bash, Perl, etc.)
- Query languages (SQL, GraphQL, etc.)
- Markup and configuration languages (YAML, JSON, XML, etc.)
- Mobile development frameworks (Swift, Kotlin, React Native, Flutter, etc.)

### 1.2.2 Out of Scope

The following are explicitly excluded from this policy:

- **Hardware development** (covered under separate hardware security policies if applicable)
- **Physical security controls** (covered under physical security policies)
- **Network security architecture** not related to application security (covered under network security policies)
- **End-user computing** (personal scripts, macros, formulas) without organizational security impact
- **Vendor product selection** unrelated to secure development requirements
- **Purely cosmetic UI changes** with no security implications
- **Documentation updates** without code changes

**Note**: While third-party and open-source software **selection** is covered (Section S2.4), this policy does not govern the development practices of external vendors creating commercial off-the-shelf (COTS) products. However, organizations should prefer vendors demonstrating secure development practices.

### 1.2.3 Development Phases Covered

This policy applies across all phases of the Software Development Lifecycle (SDLC):

**Pre-Development Phase**:
- Requirements gathering and security requirement definition
- Threat modeling and risk assessment
- Architecture and design reviews
- Technology selection and evaluation

**Development Phase**:
- Code implementation following secure coding standards
- Peer code reviews with security focus
- Unit testing including security test cases
- Static application security testing (SAST)
- Developer security training

**Testing Phase**:
- Integration testing with security scenarios
- Dynamic application security testing (DAST)
- Penetration testing
- Security regression testing
- Vulnerability scanning

**Deployment Phase**:
- Security configuration verification
- Deployment pipeline security
- Production environment hardening
- Security documentation and handoff

**Maintenance Phase**:
- Vulnerability management and patching
- Security updates and hotfixes
- Ongoing monitoring and incident response
- Periodic security reassessment

### 1.2.4 Technology Neutrality

This policy framework is **vendor-agnostic** and **technology-independent**. Requirements are expressed in terms of secure development principles and capabilities rather than specific products, tools, or methodologies.

Organizations implementing this policy may choose:
- Any SDLC methodology (Agile, Waterfall, DevSecOps, etc.) that incorporates security requirements
- Any development tools and IDEs that support security objectives
- Any SAST/DAST/SCA tools appropriate to their environment
- Any programming languages meeting business and security requirements

Technology selection should be based on:
- Security capabilities and vendor reputation for secure products
- Integration with existing development infrastructure
- Developer productivity and learning curve
- Total cost of ownership including security tooling
- Scalability and performance requirements
- Community support and security update responsiveness

---

## 1.3 Definitions

### 1.3.1 Core Development Terminology

**Secure Coding**  
The practice of writing software code that is resistant to security vulnerabilities and attacks. Secure coding follows established principles, standards, and best practices to minimize security weaknesses during development.

**Software Development Lifecycle (SDLC)**  
The process framework defining phases and activities for software development from initial concept through development, testing, deployment, and maintenance. Security should be integrated throughout the SDLC (sometimes called "Secure SDLC" or "S-SDLC").

**Security Vulnerability**  
A weakness in software design, implementation, or configuration that could be exploited to violate security policies, compromise data, or disrupt services. Vulnerabilities may result from coding errors, design flaws, misconfigurations, or use of insecure components.

**Common Weakness Enumeration (CWE)**  
A community-developed dictionary of software and hardware weakness types maintained by MITRE. CWE provides a common language for identifying and describing vulnerabilities (e.g., CWE-79: Cross-site Scripting).

**Common Vulnerabilities and Exposures (CVE)**  
A publicly available database of known security vulnerabilities in software products, maintained by MITRE. Each CVE entry provides a unique identifier, description, and references for a specific vulnerability.

**OWASP Top 10**  
The Open Web Application Security Project's list of the ten most critical web application security risks, updated periodically. The OWASP Top 10 serves as a widely recognized standard for web application security awareness and risk prioritization.

**Security by Design**  
The practice of designing security into systems from the outset rather than adding security controls after development. Security by design considers threat models, attack surfaces, and security requirements throughout architectural and design decisions.

### 1.3.2 Code Review and Testing Terminology

**Code Review**  
Systematic examination of source code by developers or security specialists to identify defects, security vulnerabilities, and deviations from coding standards. Code reviews may be manual (peer review) or automated (static analysis).

**Peer Review**  
Manual code inspection performed by developers other than the code author. Peer reviews verify functionality, adherence to standards, and identification of security issues before code integration.

**Static Application Security Testing (SAST)**  
Automated security testing performed on source code, bytecode, or binaries without executing the software. SAST tools analyze code structure to identify potential vulnerabilities based on known patterns.

**Dynamic Application Security Testing (DAST)**  
Automated security testing performed on running applications by simulating attacks. DAST tools interact with applications as an external attacker would, identifying vulnerabilities through behavioral analysis.

**Interactive Application Security Testing (IAST)**  
Hybrid security testing approach combining elements of SAST and DAST. IAST instruments applications with agents that monitor runtime behavior, providing detailed vulnerability context.

**Software Composition Analysis (SCA)**  
Automated analysis of software dependencies (third-party libraries, frameworks, open-source components) to identify known vulnerabilities, license compliance issues, and supply chain risks.

**Penetration Testing**  
Manual security testing performed by skilled security professionals who attempt to exploit vulnerabilities in applications, systems, or networks. Penetration testing simulates real-world attacks to identify exploitable weaknesses.

**Security Regression Testing**  
Retesting of previously identified and fixed security vulnerabilities to verify that fixes remain effective and that new code changes have not reintroduced vulnerabilities.

### 1.3.3 Secure Development Practices

**Threat Modeling**  
Structured process for identifying, categorizing, and prioritizing potential threats to a system during design. Threat models help developers understand attack vectors and design appropriate countermeasures (e.g., STRIDE, PASTA, DREAD methodologies).

**Security Champions**  
Developers or engineers designated within development teams who receive additional security training and serve as security advocates, promoting secure coding practices and serving as liaisons to security teams.

**Shift-Left Security**  
Philosophy of integrating security activities earlier in the development lifecycle (moving "left" on the timeline). Shift-left aims to identify and remediate security issues during development rather than late in testing or after deployment.

**DevSecOps**  
Integration of security practices within DevOps processes, emphasizing automation, collaboration between development, security, and operations teams, and continuous security validation throughout the delivery pipeline.

**Secure Code Repository**  
Version control system with access controls, encryption, and audit logging to protect source code confidentiality, integrity, and availability. Repositories should enforce branch protection, require code reviews, and integrate with security scanning tools.

**CI/CD Security**  
Integration of security controls into Continuous Integration and Continuous Deployment pipelines, including automated security testing, vulnerability scanning, and security gates preventing vulnerable code deployment.

**Security Baseline**  
Minimum security configuration or control set required for systems, applications, or components. Development environments and applications should be configured to meet organizational security baselines.

### 1.3.4 Vulnerability Management Terminology

**Vulnerability Severity**  
Risk classification assigned to vulnerabilities based on exploitability, impact, and context. Common severity frameworks include CVSS (Common Vulnerability Scoring System) with ratings: Critical, High, Medium, Low.

**Remediation**  
Process of fixing identified security vulnerabilities through code changes, configuration updates, patches, or compensating controls. Remediation timelines are typically risk-based (critical vulnerabilities require fastest remediation).

**Compensating Control**  
Alternative security control implemented when a primary control cannot be applied. For example, if a vulnerability cannot be immediately patched, a web application firewall (WAF) rule might provide temporary protection.

**False Positive**  
Security finding incorrectly identified as a vulnerability by automated tools. False positives require validation and may be suppressed with appropriate justification to reduce alert fatigue.

**Technical Debt (Security)**  
Accumulated security issues that remain unaddressed due to time constraints, resource limitations, or prioritization decisions. Security technical debt increases risk and future remediation effort if not systematically managed.

### 1.3.5 Third-Party and Open-Source Terminology

**Third-Party Component**  
Software library, framework, module, or package developed externally and integrated into organizational applications. Third-party components may be commercial (licensed) or open-source.

**Open-Source Software (OSS)**  
Software with source code publicly available under licenses permitting use, modification, and distribution. OSS introduces supply chain security considerations requiring vulnerability and license management.

**Dependency**  
External software component required by an application. Dependencies may be direct (explicitly referenced) or transitive (required by direct dependencies). Dependency trees must be analyzed for vulnerabilities.

**Software Bill of Materials (SBOM)**  
Comprehensive inventory of all components, libraries, and dependencies used in software. SBOMs enable vulnerability tracking, license compliance, and supply chain risk management.

**Supply Chain Attack**  
Attack targeting software supply chains by compromising third-party components, libraries, or development tools. Examples include malicious packages in public repositories or compromised software updates.

---

## 1.4 Related Policies and Standards

### 1.4.1 Internal ISMS Policies

This secure coding policy interacts with and references the following organizational policies:

**Application Security:**
- **ISMS Software Development Lifecycle (SDLC) Policy** (Control 8.25) - Overall secure development lifecycle framework
- **ISMS Application Security Requirements Policy** (Control 8.26) - Security requirements definition and specification
- **ISMS Secure System Architecture Policy** (Control 8.27) - Secure architectural design principles
- **ISMS Security Testing in Development and Acceptance Policy** (Control 8.29) - Security testing requirements and acceptance criteria
- **ISMS Outsourced Development Policy** (Control 8.30) - Security requirements for third-party developers
- **ISMS Separation of Development, Test, and Production Environments Policy** (Control 8.31) - Environment isolation requirements

**Supporting Policies:**
- **ISMS Change Management Policy** (Control 8.32) - Secure change control processes
- **ISMS Access Control Policy** - Developer access and privilege management
- **ISMS Cryptography Policy** (Control 8.24) - Use of cryptographic controls in code
- **ISMS Logging and Monitoring Policy** (Control 8.16) - Security logging requirements in applications
- **ISMS Incident Response Policy** - Security incident handling and vulnerability disclosure
- **ISMS Acceptable Use Policy** - Developer responsibilities and prohibited activities
- **ISMS Vendor Management Policy** - Third-party developer security requirements

### 1.4.2 External Standards and Frameworks

**International Standards:**
- **ISO/IEC 27001:2022** - Information Security Management Systems (Annex A Control 8.28)
- **ISO/IEC 27002:2022** - Information Security Controls (Control 8.28 guidance)
- **ISO/IEC 27034** - Application Security - Standard for application security
- **ISO/IEC 25010** - Systems and software Quality Requirements and Evaluation (SQuaRE)

**Secure Development Frameworks:**
- **OWASP Secure Coding Practices** - Quick Reference Guide and detailed documentation
- **OWASP Top 10** - Web application security risks (updated periodically)
- **OWASP ASVS** - Application Security Verification Standard (verification levels 1-3)
- **OWASP SAMM** - Software Assurance Maturity Model (maturity assessment)
- **NIST SP 800-53** - Security and Privacy Controls (especially SA family - System and Services Acquisition)
- **NIST SP 800-218** - Secure Software Development Framework (SSDF)
- **NIST SP 800-64** - Security Considerations in the System Development Life Cycle
- **CIS Controls** - Critical Security Controls (especially Control 16: Application Software Security)

**Common Vulnerability Databases:**
- **CWE** - Common Weakness Enumeration (software weakness taxonomy)
- **CVE** - Common Vulnerabilities and Exposures (public vulnerability database)
- **CVSS** - Common Vulnerability Scoring System (severity rating)
- **OWASP Dependency-Check** - Software composition analysis

**Language-Specific Guidelines:**
- **SEI CERT Coding Standards** - Carnegie Mellon Software Engineering Institute secure coding standards for C, C++, Java, Perl, and other languages
- **Microsoft Secure Coding Guidelines** - Language-specific guidance for .NET, C#, C++
- **Oracle Secure Coding Guidelines for Java** - Java-specific secure development practices
- **MISRA** - Motor Industry Software Reliability Association (C/C++ automotive coding standards)

### 1.4.3 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this ISMS policy are categorized as follows:

#### Mandatory Compliance

The following are **legally or contractually binding** requirements for this organization:

- **ISO/IEC 27001:2022** - Organizational commitment to certification/compliance
- **Swiss Federal Data Protection Act (FADP / nDSG)** - Data protection by design and by default requirements
- **EU General Data Protection Regulation (GDPR)** - Applicable where processing EU personal data (Article 25: Data protection by design and by default; Article 32: Security of processing)
- **[Industry-specific regulations]** - PCI-DSS (if processing payment cards), HIPAA (if healthcare), financial services regulations, etc.
- **Customer contractual requirements** - Secure development requirements in customer contracts

#### Informational Reference / Best Practice Alignment

The following are referenced for **technical guidance and best practices** but are not legally mandatory unless specifically required by contract:

- **OWASP** - Open Web Application Security Project guidance
- **NIST Special Publications (SP 800-series)** - Cybersecurity guidance and technical standards
- **CIS Controls** - Center for Internet Security benchmarks
- **SEI CERT** - Software Engineering Institute secure coding standards
- **MITRE CWE/CVE** - Vulnerability classification and tracking

#### United States Federal Requirements

References to United States federal frameworks and regulations (FISMA, FedRAMP, NIST mandatory requirements, DoD secure development standards, etc.) apply **only** where the organization:

- Develops software for US federal agencies as contractor or subcontractor
- Provides software or services to customers subject to such regulations
- Has explicit contractual obligations requiring such compliance
- Operates facilities or processes data within US jurisdiction subject to federal oversight

**In all other cases**, these references are provided for **informational or technical alignment purposes only** and do not constitute mandatory compliance requirements.

For complete regulatory categorization, refer to **ISMS-POL-00 - Regulatory Applicability Framework**.

---

## 1.5 Policy Framework Structure

This document (S1) is part of a modular policy framework for Secure Coding. The complete framework consists of:

**ISMS-POL-A.8.28-S1** - Purpose, Scope, Definitions (this document)  
**ISMS-POL-A.8.28-S2** - Requirements Overview  
**ISMS-POL-A.8.28-S2.1** - Pre-Development Requirements  
**ISMS-POL-A.8.28-S2.2** - Secure Coding Standards  
**ISMS-POL-A.8.28-S2.3** - Code Review & Testing Requirements  
**ISMS-POL-A.8.28-S2.4** - Third-Party & OSS Management  
**ISMS-POL-A.8.28-S3** - Roles and Responsibilities  
**ISMS-POL-A.8.28-S4** - Policy Governance  
**ISMS-POL-A.8.28-S5** - Annexes

Each section is independently versionable to support granular change management and targeted stakeholder reviews.

---

## 1.6 Document Maintenance

### 1.6.1 Review and Updates

This document shall be reviewed:
- **Annually** as part of the ISMS policy review cycle
- **Upon significant changes** to development practices, technology stacks, or threat landscape
- **Following security incidents** where secure coding gaps are identified
- **When new vulnerability classes** emerge requiring policy updates (e.g., new OWASP Top 10 release)
- **After major SDLC or tooling changes** affecting secure development practices

### 1.6.2 Change Management

Changes to this document require:
- Proposal with business/security justification
- Risk assessment of proposed changes
- Review by Development Leadership and Security Team
- Technical validation by Application Security Lead
- Approval by Policy Owner (CISO)
- Communication to development teams and stakeholders
- Update to related implementation documentation and training materials

### 1.6.3 Version Control

This document uses semantic versioning:
- **Major version** (X.0): Significant structural changes, scope modifications, or new mandatory requirements
- **Minor version** (X.Y): Content updates, clarifications, additional guidance, or examples without scope change

All versions are retained in the organization's document management system with full change history.

---

## 1.7 Compliance and Enforcement

### 1.7.1 Policy Violations

Violations of secure coding policies may include:
- Bypassing or disabling security controls in development/test environments
- Committing code with known high/critical vulnerabilities without remediation plan
- Failure to conduct required code reviews or security testing
- Unauthorized use of prohibited libraries or insecure components
- Hardcoding credentials, API keys, or sensitive data in source code
- Disabling security scanning tools or suppressing findings without justification
- Failure to remediate vulnerabilities within required timelines
- Unauthorized deployment of code to production without security approval

Violations are subject to disciplinary action in accordance with organizational policies and may include:
- Verbal or written warnings
- Mandatory security training or re-certification
- Removal of code commit privileges
- Project delays pending security remediation
- Suspension or termination of employment/contract
- Legal action where violations involve malicious activity or gross negligence

### 1.7.2 Monitoring and Auditing

The organization reserves the right to:
- Monitor code commits and development activities for security compliance
- Review code repositories, CI/CD pipelines, and development tool configurations
- Audit adherence to secure coding standards and security testing requirements
- Analyze vulnerability scan results and remediation timelines
- Conduct surprise security code reviews or architecture assessments
- Track security metrics and KPIs for development teams

Developers should expect that code and development activities are subject to security review and audit. All monitoring activities will be conducted in accordance with applicable laws and organizational policies.

### 1.7.3 No Expectation of Privacy

Source code and development artifacts stored in organizational repositories are organizational property. Developers have no expectation of privacy in code they write for the organization. Security teams and management may access and review code for security, quality, and compliance purposes without advance notice.

---

**END OF DOCUMENT**

*"The first principle is that you must not fool yourself — and you are the easiest person to fool." - Richard Feynman*

**Translation for ISMS Context**: Don't fool yourself into thinking you're secure just because you have policies. Secure coding requires continuous verification through testing, measurement, and evidence-based improvement.