# ISMS-POL-A.8.28-S3
## Secure Coding - Roles and Responsibilities

**Document ID**: ISMS-POL-A.8.28-S3
**Title**: Secure Coding - Roles and Responsibilities  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / HR / Development Management | Initial roles and responsibilities framework |

**Review Cycle**: Annual (or upon significant organizational structure changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Organizational Review: Chief Technology Officer (CTO) / VP Engineering
- HR Review: Human Resources (role definition accuracy)
- Legal Review: Legal/Compliance Officer (accountability framework)

**Distribution**: All personnel involved in software development lifecycle  
**Related Documents**: ISMS-POL-A.8.28 (Master Policy), Organizational Job Descriptions, ISMS Role Definitions

---

## 3.1 Introduction

This section defines **roles and responsibilities** for secure coding implementation using RACI methodology:
- **R**esponsible: Performs the work
- **A**ccountable: Ultimately answerable for completion (only one A per activity)
- **C**onsulted: Provides input and expertise
- **I**nformed: Kept updated on progress

*"You can delegate authority, but you cannot delegate responsibility."* - Byron Dorgan

**Translation for Security**: Every security activity requires clear accountability. When everyone is responsible, no one is responsible. This framework eliminates ambiguity.

**Role Framework Principles:**
1. **Single Accountability**: Each requirement has one accountable role
2. **Clear Responsibility**: Roles performing work are explicitly defined
3. **Expertise Integration**: Subject matter experts are consulted
4. **Stakeholder Awareness**: Affected parties are informed
5. **Escalation Paths**: Clear chain of command for issues and exceptions

---

## 3.2 Organizational Roles

### 3.2.1 Executive and Leadership Roles

#### 3.2.1.1 Chief Information Security Officer (CISO)

**Primary Accountability**: Overall secure coding program governance and risk acceptance

**Responsibilities**:
- Approve secure coding policy framework and updates
- Accept residual risk for unresolved vulnerabilities (with justification)
- Allocate budget for security tools (SAST, DAST, SCA) and training
- Oversee Application Security Team performance
- Report security metrics to Board/Executive Management
- Approve exceptions to security policies
- Escalate critical security issues to executive leadership

**Authority**:
- Block production deployments with Critical/High unresolved vulnerabilities
- Mandate security training for development personnel
- Require security assessments for high-risk applications

**Reports to**: Chief Executive Officer (CEO) or Chief Technology Officer (CTO)

**RACI Summary**: **A** for policy governance, risk acceptance, exception approvals

---

#### 3.2.1.2 Chief Technology Officer (CTO) / VP Engineering

**Primary Accountability**: Development organization's adherence to secure coding practices

**Responsibilities**:
- Ensure development teams follow secure coding standards
- Allocate development resources for security activities (threat modeling, code review, remediation)
- Support Security Champions program with management backing
- Include security metrics in development performance reviews
- Escalate resource conflicts (security vs. delivery timeline) to CISO
- Foster security-aware engineering culture

**Authority**:
- Prioritize security remediation work in development roadmaps
- Adjust project timelines to accommodate security requirements
- Performance management for developers not adhering to security standards

**Reports to**: Chief Executive Officer (CEO)

**RACI Summary**: **A** for development organization compliance with security requirements

---

#### 3.2.1.3 Chief Legal Officer / General Counsel

**Primary Accountability**: Legal and regulatory compliance for software development

**Responsibilities**:
- Advise on open-source license compliance
- Review contracts with third-party development vendors (security clauses)
- Assess legal risk from security vulnerabilities
- Advise on data protection regulations (GDPR, FADP) affecting development
- Support incident response for security breaches (legal implications)

**Authority**:
- Block use of software with incompatible licenses
- Require legal review for high-risk vendor contracts
- Mandate disclosure of security incidents per legal requirements

**Reports to**: Chief Executive Officer (CEO)

**RACI Summary**: **A** for license compliance, **C** for vendor contracts and regulatory compliance

---

### 3.2.2 Security Team Roles

#### 3.2.2.1 Application Security Lead

**Primary Accountability**: Application security program implementation and effectiveness

**Responsibilities**:
- Define and maintain secure coding standards (ISMS-POL-A.8.28-S2.2)
- Configure and maintain security tools (SAST, DAST, SCA)
- Review threat models and security architectures
- Triage security vulnerabilities and assign severity
- Coordinate penetration testing (internal or external)
- Train Security Champions and developers
- Track vulnerability remediation and SLA compliance
- Report security metrics to CISO

**Authority**:
- Approve or reject threat models and security designs
- Classify vulnerability severity (Critical/High/Medium/Low)
- Approve security exceptions (in consultation with CISO)
- Require security testing before production deployment

**Reports to**: CISO

**RACI Summary**: **R** for security tool configuration, threat model review, vulnerability triage; **A** for application security program execution

---

#### 3.2.2.2 Security Architect

**Primary Accountability**: Secure system architecture and design

**Responsibilities**:
- Conduct architecture security reviews
- Develop secure architecture patterns and reference architectures
- Provide security design guidance to development teams
- Review threat models for completeness and accuracy
- Assess cloud security architecture and configurations
- Define security requirements for new technologies/frameworks

**Authority**:
- Approve or reject security architecture designs
- Require architecture changes to meet security standards
- Approve technology selections with security implications

**Reports to**: CISO or CTO (depending on organization)

**RACI Summary**: **R** for architecture reviews, **A** for secure architecture decisions

---

#### 3.2.2.3 Security Engineer / Analyst

**Primary Accountability**: Security tool operation and vulnerability analysis

**Responsibilities**:
- Operate SAST, DAST, SCA tools (scan execution, configuration)
- Analyze security scan results and eliminate false positives
- Support development teams with vulnerability remediation
- Monitor security alerts and threat intelligence
- Maintain security tool configurations and rule sets
- Document security findings and remediation guidance

**Authority**:
- Classify findings as true positive or false positive
- Recommend remediation approaches
- Escalate unresolved vulnerabilities to Application Security Lead

**Reports to**: Application Security Lead

**RACI Summary**: **R** for tool operation and vulnerability analysis

---

### 3.2.3 Development Team Roles

#### 3.2.3.1 Development Manager / Engineering Manager

**Primary Accountability**: Team-level compliance with secure coding practices

**Responsibilities**:
- Ensure developers complete security training
- Allocate time for security activities (code review, testing, remediation)
- Support Security Champion within team
- Review and approve security-related resource requests
- Include security metrics in team performance reviews
- Escalate resource conflicts to CTO/VP Engineering
- Foster team culture prioritizing security

**Authority**:
- Prioritize security work within team backlog
- Require code review completion before merge
- Adjust sprint commitments to accommodate security remediation

**Reports to**: Director of Engineering or CTO

**RACI Summary**: **A** for team compliance with secure coding requirements, **R** for resource allocation

---

#### 3.2.3.2 Software Developer

**Primary Accountability**: Writing secure code following organizational standards

**Responsibilities**:
- Follow secure coding standards (ISMS-POL-A.8.28-S2.2)
- Complete mandatory security training (initial + annual)
- Conduct peer code reviews with security focus
- Write security unit tests for critical functionality
- Remediate vulnerabilities within defined SLAs
- Participate in threat modeling sessions
- Use security linters and IDE plugins
- Report security concerns to Security Champion or Security Team

**Authority**:
- Request security guidance from Security Champion or Security Team
- Reject code in peer review with security issues
- Request security exception (via manager) if unable to meet SLA

**Reports to**: Development Manager

**RACI Summary**: **R** for writing secure code, remediating vulnerabilities

---

#### 3.2.3.3 Security Champion

**Primary Accountability**: Team-level security advocacy and expertise

**Responsibilities**:
- Serve as security point-of-contact for development team
- Participate in security champion community meetings
- Review code for security issues (in addition to peer review)
- Mentor developers on secure coding practices
- Escalate security concerns to Application Security Team
- Share security updates and threat intelligence with team
- Contribute to secure coding standards and guidelines
- Support threat modeling facilitation

**Authority**:
- Recommend security improvements to team practices
- Request Application Security Team involvement for complex issues
- Participate in security tool evaluation and configuration

**Reports to**: Development Manager (functionally); dotted line to Application Security Lead

**RACI Summary**: **R** for team security advocacy, **C** for security reviews and guidance

**Selection Criteria**:
- Volunteer basis (interest in security)
- Minimum 2 years development experience
- Completed advanced security training
- Strong communication and mentoring skills

**Time Allocation**: 10-20% of work time for security champion activities

---

#### 3.2.3.4 Senior Developer / Tech Lead

**Primary Accountability**: Technical leadership including security best practices

**Responsibilities**:
- Model secure coding practices for junior developers
- Conduct thorough security-focused code reviews
- Mentor developers on vulnerability remediation
- Participate in architecture and threat modeling sessions
- Represent team in technical security discussions
- Contribute to coding standards and best practices documentation

**Authority**:
- Block code merge for security issues
- Escalate architectural security concerns to Security Architect
- Recommend security improvements in team processes

**Reports to**: Development Manager or Engineering Manager

**RACI Summary**: **R** for technical security leadership within team

---

### 3.2.4 Quality Assurance and Testing Roles

#### 3.2.4.1 QA Engineer / Test Engineer

**Primary Accountability**: Security testing execution and verification

**Responsibilities**:
- Execute security test cases (functional security testing)
- Validate vulnerability remediation (retest fixed issues)
- Report security defects with appropriate severity
- Maintain security test automation
- Verify security acceptance criteria before release
- Coordinate with Security Team for specialized testing

**Authority**:
- Fail builds/releases with unresolved Critical/High vulnerabilities
- Request penetration testing for high-risk changes
- Escalate untested security requirements to QA Manager

**Reports to**: QA Manager

**RACI Summary**: **R** for security testing execution, **C** for test planning

---

#### 3.2.4.2 QA Manager

**Primary Accountability**: Security testing coverage and quality

**Responsibilities**:
- Ensure security testing integrated in test plans
- Allocate resources for security testing activities
- Review security test coverage and effectiveness
- Coordinate with Application Security Team for testing strategy
- Report security testing metrics
- Escalate testing resource needs to management

**Authority**:
- Require security testing before production deployment
- Delay releases for incomplete security testing
- Request additional security testing resources

**Reports to**: VP Engineering or CTO

**RACI Summary**: **A** for security testing adequacy

---

### 3.2.5 DevOps and Infrastructure Roles

#### 3.2.5.1 DevOps Engineer / Platform Engineer

**Primary Accountability**: Secure CI/CD pipeline and development infrastructure

**Responsibilities**:
- Configure and maintain CI/CD security gates (SAST, SCA integration)
- Secure build environments and artifact repositories
- Implement secrets management solutions
- Maintain infrastructure-as-code security scanning
- Monitor pipeline security events and failures
- Support developers with pipeline security issues
- Maintain container base image security

**Authority**:
- Configure pipeline security gates and thresholds
- Block deployments failing security checks
- Require security tool integration in pipelines

**Reports to**: DevOps Manager or Infrastructure Manager

**RACI Summary**: **R** for CI/CD pipeline security implementation

---

#### 3.2.5.2 Infrastructure Security Engineer

**Primary Accountability**: Development infrastructure security

**Responsibilities**:
- Harden development and build environments
- Monitor infrastructure for security anomalies
- Manage access controls for development systems
- Patch and update development tools and systems
- Respond to infrastructure security incidents
- Implement network segmentation for dev/test/prod

**Authority**:
- Require security hardening before system deployment
- Restrict access to development infrastructure
- Enforce patching schedules for development systems

**Reports to**: CISO or Infrastructure Manager

**RACI Summary**: **R** for development infrastructure security

---

### 3.2.6 Specialized Roles

#### 3.2.6.1 Security Architect (Application)

**Primary Accountability**: Application-level security architecture

**Responsibilities**:
- Design security controls for applications
- Define security patterns for common use cases
- Review and approve application security designs
- Conduct threat modeling workshops
- Provide security guidance for cloud/microservices architectures
- Evaluate new security technologies and frameworks

**Authority**:
- Approve or reject security architecture designs
- Require security architecture documentation
- Mandate specific security controls for high-risk applications

**Reports to**: CISO or Chief Architect

**RACI Summary**: **A** for application security architecture decisions

---

#### 3.2.6.2 Penetration Tester (Internal or External)

**Primary Accountability**: Manual security testing and vulnerability validation

**Responsibilities**:
- Conduct penetration testing per defined schedule
- Validate SAST/DAST findings with manual testing
- Test business logic vulnerabilities
- Document findings with proof-of-concept exploits
- Provide remediation recommendations
- Retest fixed vulnerabilities

**Authority**:
- Define penetration testing scope and methodology
- Escalate Critical findings to Application Security Lead
- Recommend deployment blocks for severe vulnerabilities

**Reports to**: Application Security Lead (if internal) or engaged as vendor

**RACI Summary**: **R** for penetration testing execution

---

#### 3.2.6.3 Compliance Officer

**Primary Accountability**: Regulatory compliance for software development

**Responsibilities**:
- Identify applicable regulations affecting development (GDPR, FADP, industry-specific)
- Map security requirements to regulatory obligations
- Coordinate compliance audits (ISO 27001, SOC 2, etc.)
- Review security policies for regulatory alignment
- Track compliance metrics and gaps
- Advise on data protection requirements

**Authority**:
- Require compliance evidence for audits
- Mandate security controls for regulatory compliance
- Escalate compliance gaps to executive management

**Reports to**: Chief Legal Officer or CISO

**RACI Summary**: **A** for regulatory compliance verification

---

### 3.2.7 Vendor and Third-Party Roles

#### 3.2.7.1 Procurement / Vendor Management

**Primary Accountability**: Vendor security requirements and contract compliance

**Responsibilities**:
- Include security requirements in vendor RFPs
- Negotiate security clauses in development contracts
- Conduct vendor security assessments
- Monitor vendor compliance with security obligations
- Manage vendor security incidents and breaches
- Track vendor security performance

**Authority**:
- Reject vendors not meeting security requirements
- Require vendor security assessments before engagement
- Terminate contracts for security non-compliance

**Reports to**: CFO or COO

**RACI Summary**: **A** for vendor security contractual requirements

---

#### 3.2.7.2 Third-Party Developer (Vendor)

**Primary Accountability**: Adherence to organizational secure coding requirements

**Responsibilities**:
- Follow organizational secure coding standards
- Provide SBOM for delivered software
- Conduct security testing per contract requirements
- Report discovered vulnerabilities
- Remediate vulnerabilities within contractual SLAs
- Participate in security assessments and audits
- Maintain developer security training

**Authority**:
- Request clarification on security requirements
- Propose alternative security controls (subject to approval)

**Reports to**: Vendor management chain

**RACI Summary**: **R** for secure code delivery per contract

---

## 3.3 RACI Matrix by Activity

### 3.3.1 Pre-Development Activities

| Activity | CISO | App Sec Lead | Sec Architect | Dev Manager | Developer | Sec Champion | QA | DevOps |
|----------|------|-------------|--------------|-------------|-----------|--------------|----|----|
| **Security Requirements Definition** | I | C | C | A | R | C | I | I |
| **Threat Modeling** | I | C | A | I | R | R | I | I |
| **Architecture Security Review** | I | C | A | I | C | C | I | I |
| **Security Training (Developer)** | A | R | C | I | R | C | I | I |
| **Development Environment Security** | I | C | C | A | I | I | I | R |

### 3.3.2 Development Activities

| Activity | CISO | App Sec Lead | Sec Architect | Dev Manager | Developer | Sec Champion | QA | DevOps |
|----------|------|-------------|--------------|-------------|-----------|--------------|----|----|
| **Secure Code Writing** | I | C | C | A | R | C | I | I |
| **Peer Code Review** | I | I | I | A | R | R | I | I |
| **SAST Execution** | I | C | I | I | I | I | I | R |
| **SCA Execution** | I | C | I | I | I | I | I | R |
| **Vulnerability Remediation** | I | C | C | A | R | C | I | I |

### 3.3.3 Testing Activities

| Activity | CISO | App Sec Lead | Sec Architect | Dev Manager | Developer | Sec Champion | QA | DevOps |
|----------|------|-------------|--------------|-------------|-----------|--------------|----|----|
| **Security Unit Testing** | I | C | I | I | R | C | C | I |
| **DAST Execution** | I | R | I | I | I | I | C | C |
| **Penetration Testing** | I | A | C | I | I | I | C | I |
| **Security Test Case Execution** | I | C | I | I | I | C | R | I |
| **Vulnerability Verification** | I | C | I | I | C | C | R | I |

### 3.3.4 Third-Party and OSS Management

| Activity | CISO | App Sec Lead | Legal | Procurement | Dev Manager | Developer | DevOps |
|----------|------|-------------|-------|-------------|-------------|-----------|--------|
| **Component Selection** | I | C | I | I | A | R | I |
| **License Compliance Review** | I | C | A | I | I | R | I |
| **SBOM Generation** | I | C | I | I | I | R | R |
| **Dependency Vulnerability Mgmt** | I | A | I | I | C | R | C |
| **Vendor Security Assessment** | I | C | C | A | I | I | I |

### 3.3.5 Governance Activities

| Activity | CISO | App Sec Lead | CTO | Dev Manager | Compliance |
|----------|------|-------------|-----|-------------|-----------|
| **Policy Approval** | A | R | C | I | C |
| **Risk Acceptance** | A | R | I | I | C |
| **Exception Approval** | A | C | I | I | C |
| **Security Metrics Reporting** | A | R | I | I | C |
| **Audit Coordination** | I | C | I | I | A |

**Legend**:
- **R** (Responsible): Does the work
- **A** (Accountable): Ultimately answerable (only one per activity)
- **C** (Consulted): Provides input
- **I** (Informed): Kept updated

---

## 3.4 Escalation Paths

### 3.4.1 Technical Escalation

**Level 1**: Developer → Security Champion  
**Level 2**: Security Champion → Application Security Lead  
**Level 3**: Application Security Lead → Security Architect  
**Level 4**: Security Architect → CISO

**Escalation Triggers**:
- Unable to remediate vulnerability within SLA
- Disagreement on vulnerability severity
- Architectural security concern beyond team expertise
- Need for risk acceptance decision

### 3.4.2 Management Escalation

**Level 1**: Developer → Development Manager  
**Level 2**: Development Manager → Director of Engineering  
**Level 3**: Director of Engineering → CTO / VP Engineering  
**Level 4**: CTO → CEO

**Escalation Triggers**:
- Resource conflict (security vs. delivery timeline)
- Cross-team coordination issues
- Budget requirements for security tools
- Policy compliance issues

### 3.4.3 Risk Escalation

**Level 1**: Application Security Lead → CISO  
**Level 2**: CISO → CTO + General Counsel  
**Level 3**: CISO + CTO → CEO  
**Level 4**: CEO → Board of Directors

**Escalation Triggers**:
- Critical vulnerability in production
- Supply chain security incident
- Major security breach or data compromise
- Regulatory compliance violation

---

## 3.5 Role Qualifications and Training

### 3.5.1 Minimum Qualifications by Role

| Role | Education/Experience | Certifications (Preferred) | Training Requirements |
|------|---------------------|---------------------------|----------------------|
| **Application Security Lead** | Bachelor's + 5 years security | OSCP, GWAPT, CSSLP | Annual security conference |
| **Security Architect** | Bachelor's + 7 years IT/security | CISSP, CCSP, SABSA | Annual security conference |
| **Security Champion** | 2+ years development | None required | Quarterly security training |
| **Developer** | Bachelor's or equivalent experience | None required | Annual secure coding training |
| **Penetration Tester** | Bachelor's + 3 years security | OSCP, GPEN, CEH | Annual offensive security training |

### 3.5.2 Role-Specific Training

**Application Security Lead**:
- Advanced secure coding (OWASP, SANS)
- Security tool configuration and tuning
- Threat modeling methodologies
- Cloud security architecture

**Security Champion**:
- Secure coding fundamentals
- OWASP Top 10 deep dive
- Threat modeling basics
- Security testing tools usage

**Developer**:
- Secure coding principles (mandatory)
- Language-specific security (for primary language)
- Security testing tools (SAST, SCA usage)

---

## 3.6 Performance Metrics by Role

### 3.6.1 Developer Metrics

- Code review participation rate (% of PRs reviewed)
- Vulnerability introduction rate (vulnerabilities per 1000 LOC)
- Remediation SLA compliance (% fixed within SLA)
- Security training completion

### 3.6.2 Application Security Team Metrics

- Vulnerability discovery rate (SAST/DAST/pentesting findings)
- False positive rate (% of findings correctly classified)
- Mean time to triage (days from discovery to severity assignment)
- Security tool availability (% uptime)

### 3.6.3 Development Manager Metrics

- Team security training completion rate
- Team vulnerability remediation velocity
- Code review coverage (% of commits reviewed)
- Security Champion engagement (hours dedicated)

---

## 3.7 Accountability for Security Incidents

### 3.7.1 Incident Roles

**Incident Commander**: Application Security Lead (for security incidents)  
**Technical Lead**: Developer or DevOps Engineer (for remediation)  
**Communications Lead**: CISO or designate (for stakeholder communication)  
**Legal Advisor**: General Counsel (for regulatory/legal implications)

### 3.7.2 Post-Incident Review

**Required Participants**: Developer(s) involved, Development Manager, Application Security Lead, CISO  
**Output**: Lessons learned, process improvements, policy updates  
**Timeline**: Within 2 weeks of incident resolution

---

**END OF DOCUMENT**

*"Accountability breeds response-ability."* - Stephen Covey

**Application to Security**: When roles and responsibilities are clear, people know what's expected and can be held accountable. Ambiguity is the enemy of security - clarity enables action.