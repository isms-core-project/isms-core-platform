# ISMS-IMP-A.8.25-26-29-S2
## SDLC Security Integration - Implementation Guide
### ISO/IEC 27001:2022 Control A.8.25 (Secure Development Lifecycle)

---

## Document Control

**Document ID:** ISMS-IMP-A.8.25-26-29-S2  
**Implementation Area:** Secure Development Lifecycle Integration  
**Related Policy:** ISMS-POL-A.8.25-26-29-S3 (Secure Development Lifecycle - A.8.25)  
**Purpose:** Step-by-step implementation guidance for integrating security throughout the software development lifecycle

**Regulatory Context:**
- ISO/IEC 27001:2022 Control A.8.25 (Secure Development Lifecycle)
- OWASP SAMM - Implementation domain
- NIST SP 800-218 - Secure Software Development Framework
- See ISMS-POL-00 for complete regulatory applicability framework

---

## 1. Overview

### 1.1 Purpose

This implementation guide provides practical, step-by-step procedures for integrating security throughout the Software Development Lifecycle (SDLC) as defined in POL-S3. It covers:

- Security activities for each SDLC phase (Requirements → Deployment)
- SDLC methodology-specific implementation (Waterfall, Agile, DevOps)
- Security champion program establishment
- Developer security training programs
- Security gate implementation
- Assessment workbook usage and evidence collection

### 1.2 Target Audience

- **Primary:** Development Managers, DevOps Leads, Security Champions
- **Supporting:** Developers, QA Engineers, Release Managers
- **Oversight:** CISO, Security Leadership, Engineering Leadership

### 1.3 Prerequisites

**Before implementing this process:**
- [ ] Read ISMS-POL-A.8.25-26-29-S3 (Secure Development Lifecycle Policy)
- [ ] Security requirements process established (IMP-S1)
- [ ] SDLC methodology documented (Waterfall, Agile, DevOps, hybrid)
- [ ] Development team structure known
- [ ] CI/CD pipeline infrastructure identified
- [ ] Security tools budget and resources allocated

### 1.4 Process Dependencies

**Integrates with:**
- Security requirements specification (IMP-S1)
- Secure coding practices (IMP-S3)
- Security testing processes (IMP-S4)
- Change management (ISMS-POL-A.8.32)
- Environment separation (ISMS-POL-A.8.31)
- Source code access control (ISMS-POL-A.8.4)

---

## 2. Security Activities by SDLC Phase

### 2.1 Phase-Based Security Framework

**Core Principle:** Security activities must be integrated into EVERY phase of the SDLC, not bolted on at the end.

**Security Gate Approach:**
- Each phase has entry criteria (security inputs required)
- Each phase has security activities (what to do)
- Each phase has exit criteria (security outputs/approvals required)
- Gates prevent progression without security completion

### 2.2 Requirements Phase Security

**Phase Overview:**
- Business requirements gathering
- Functional and non-functional requirements definition
- Feasibility analysis and planning

**Entry Criteria:**
- [ ] Project charter approved
- [ ] Initial stakeholders identified
- [ ] Business objectives defined

**Security Activities:**

**Activity 1: Application Risk Classification**
- **When:** Project initiation
- **Owner:** Product Owner + Security Architect
- **Process:** Use risk scoring from IMP-S1 Section 2
- **Output:** Risk classification (High/Medium/Low)
- **Timeline:** 1-2 days

**Activity 2: Security Requirements Elicitation**
- **When:** Requirements gathering workshops
- **Owner:** Product Owner + Security Architect
- **Process:** Use requirements template from IMP-S1 Section 3.2
- **Output:** Security requirements document (SEC-REQ-XXX)
- **Timeline:** 1-2 weeks (concurrent with functional requirements)

**Activity 3: Regulatory Compliance Mapping**
- **When:** After business requirements defined
- **Owner:** Compliance Officer + Security Architect
- **Process:** Identify applicable regulations (GDPR, PCI DSS, HIPAA, etc.)
- **Output:** Compliance requirements matrix
- **Timeline:** 3-5 days

**Activity 4: Data Classification and Flow Mapping**
- **When:** After functional requirements draft complete
- **Owner:** Security Architect + Business Analyst
- **Process:** Identify data types, classify sensitivity, map data flows
- **Output:** Data flow diagram (DFD), data classification matrix
- **Timeline:** 2-4 days

**Exit Criteria:**
- [ ] Security requirements documented and approved
- [ ] Risk classification assigned
- [ ] Regulatory requirements identified
- [ ] Data classification complete
- [ ] Security requirements linked to project plan

**Artifacts:**
- Security Requirements Document
- Risk Classification Record
- Compliance Requirements Matrix
- Data Flow Diagram

### 2.3 Design Phase Security

**Phase Overview:**
- High-level architecture design
- Detailed design specifications
- Technology stack selection
- Integration planning

**Entry Criteria:**
- [ ] Security requirements approved (from Requirements phase)
- [ ] Functional requirements finalized
- [ ] Technology constraints identified

**Security Activities:**

**Activity 1: Threat Modeling**
- **When:** After initial architecture design
- **Owner:** Security Architect + Application Architect
- **Process:** Use STRIDE/PASTA/LINDDUN from IMP-S1 Section 4
- **Output:** Threat model document, mitigation plan
- **Timeline:** 1 week (includes workshop)

**Activity 2: Security Architecture Review**
- **When:** After architecture design complete
- **Owner:** Security Architect (lead reviewer)
- **Process:** Use architecture review checklist from IMP-S1 Section 5.2
- **Output:** Architecture review report, findings list
- **Timeline:** 2 weeks (prep + review + remediation)

**Activity 3: Secure Design Patterns Selection**
- **When:** During detailed design
- **Owner:** Application Architect + Development Lead
- **Process:** Select proven secure design patterns (authentication, authorization, session management, encryption)
- **Output:** Design patterns documentation
- **Timeline:** 3-5 days

**Activity 4: Security Technology Selection**
- **When:** Technology stack selection
- **Owner:** Architecture Team + Security Team
- **Process:** Evaluate security features of frameworks, libraries, platforms
- **Output:** Technology selection rationale with security considerations
- **Timeline:** 1 week

**Activity 5: Third-Party Component Security Review**
- **When:** Before committing to third-party components
- **Owner:** Security Team + Development Lead
- **Process:** Vulnerability scanning, license review, vendor security assessment
- **Output:** Third-party component approval list
- **Timeline:** Ongoing during design

**Exit Criteria:**
- [ ] Threat model approved
- [ ] Architecture review passed (no open critical findings)
- [ ] Secure design patterns documented
- [ ] Third-party components reviewed and approved
- [ ] Security architecture documented

**Artifacts:**
- Threat Model Document
- Architecture Review Report
- Secure Design Patterns Documentation
- Third-Party Component Approval List

### 2.4 Development Phase Security

**Phase Overview:**
- Code implementation
- Unit testing
- Code review
- Integration

**Entry Criteria:**
- [ ] Architecture review approved (from Design phase)
- [ ] Development environment secured (see Section 6)
- [ ] Developers trained on secure coding (see Section 4)

**Security Activities:**

**Activity 1: Secure Coding Standards Application**
- **When:** All code development
- **Owner:** Developers
- **Process:** Follow secure coding standards from IMP-S3
- **Output:** Code compliant with standards
- **Timeline:** Continuous

**Activity 2: Security-Focused Code Review**
- **When:** Before code merge/commit
- **Owner:** Peer Developers + Security Champion
- **Process:** Use code review checklist from IMP-S3
- **Output:** Code review approval, security findings log
- **Timeline:** Per pull request/code review cycle

**Activity 3: Static Application Security Testing (SAST)**
- **When:** Per commit (automated in CI/CD)
- **Owner:** Developers + DevOps Team
- **Process:** SAST tool scans code, flags vulnerabilities
- **Output:** SAST scan results, remediation tracking
- **Timeline:** Automated (5-30 min per scan)

**Activity 4: Software Composition Analysis (SCA)**
- **When:** Per build (automated in CI/CD)
- **Owner:** Developers + DevOps Team
- **Process:** SCA tool scans dependencies, identifies vulnerabilities
- **Output:** Dependency vulnerability report, update plan
- **Timeline:** Automated (2-10 min per scan)

**Activity 5: Secret Scanning**
- **When:** Pre-commit (automated hook)
- **Owner:** Developers
- **Process:** Scan for hardcoded credentials, API keys, tokens
- **Output:** Blocked commits with secrets, remediation
- **Timeline:** Automated (<1 min per commit)

**Activity 6: Security Unit Testing**
- **When:** Unit test development
- **Owner:** Developers
- **Process:** Write tests for security requirements (authentication, authorization, input validation)
- **Output:** Security unit tests, coverage metrics
- **Timeline:** Concurrent with development

**Exit Criteria:**
- [ ] Code review completed and approved
- [ ] SAST scans passed (no unaddressed high/critical findings)
- [ ] SCA scans passed (no unaddressed high/critical vulnerabilities)
- [ ] No hardcoded secrets in code
- [ ] Security unit tests written and passing
- [ ] Requirements traceability updated

**Artifacts:**
- Code Review Records
- SAST Scan Reports
- SCA Vulnerability Reports
- Secret Scanning Logs
- Unit Test Results

### 2.5 Testing Phase Security

**Phase Overview:**
- Integration testing
- System testing
- User acceptance testing
- Performance testing

**Entry Criteria:**
- [ ] Development phase security activities complete
- [ ] Test environment secured (see IMP on A.8.31)
- [ ] No production data in test environment

**Security Activities:**

**Activity 1: Dynamic Application Security Testing (DAST)**
- **When:** After application deployment to test environment
- **Owner:** Security Team + QA Team
- **Process:** DAST tool scans running application for vulnerabilities
- **Output:** DAST scan results, remediation tracking
- **Timeline:** Weekly or per release candidate

**Activity 2: Security Acceptance Testing**
- **When:** During UAT phase
- **Owner:** QA Team + Security Champion
- **Process:** Execute security test cases from requirements traceability matrix
- **Output:** Security acceptance test results
- **Timeline:** 1-2 weeks (concurrent with UAT)

**Activity 3: Penetration Testing (High-Risk Applications)**
- **When:** Pre-production for high-risk applications
- **Owner:** Security Team (or external pentesters)
- **Process:** Manual security testing, exploit attempts
- **Output:** Penetration test report, remediation plan
- **Timeline:** 1-2 weeks (depending on scope)

**Activity 4: Security Regression Testing**
- **When:** After security bug fixes
- **Owner:** QA Team
- **Process:** Re-test fixed vulnerabilities, verify no regression
- **Output:** Regression test results
- **Timeline:** Per bug fix cycle

**Exit Criteria:**
- [ ] DAST scans passed (no unaddressed high/critical findings)
- [ ] Security acceptance tests passed
- [ ] Penetration testing completed (high-risk apps) with findings addressed
- [ ] Security regression tests passed
- [ ] All security requirements verified

**Artifacts:**
- DAST Scan Reports
- Security Acceptance Test Results
- Penetration Test Report (if applicable)
- Security Regression Test Results

### 2.6 Deployment Phase Security

**Phase Overview:**
- Production deployment
- Release management
- Go-live preparation

**Entry Criteria:**
- [ ] Testing phase security activities complete
- [ ] Production environment secured (infrastructure security)
- [ ] Deployment procedures documented and reviewed

**Security Activities:**

**Activity 1: Pre-Deployment Security Checklist**
- **When:** Before production deployment
- **Owner:** Security Team + DevOps Team
- **Process:** Verify all security controls in place (TLS, authentication, authorization, logging, monitoring)
- **Output:** Deployment security checklist (approved)
- **Timeline:** 1-2 days before deployment

**Activity 2: Security Configuration Review**
- **When:** Production configuration setup
- **Owner:** Security Team + Operations Team
- **Process:** Review production configurations (no debug mode, strong passwords, least privilege)
- **Output:** Configuration review approval
- **Timeline:** Day of deployment

**Activity 3: Security Monitoring Setup**
- **When:** Production deployment
- **Owner:** Security Operations + DevOps
- **Process:** Configure security monitoring, alerting, logging (SIEM integration)
- **Output:** Monitoring dashboard, alert rules
- **Timeline:** Before go-live

**Activity 4: Security Runbook Preparation**
- **When:** Before go-live
- **Owner:** Security Team + Operations
- **Process:** Document security incident response procedures, escalation paths
- **Output:** Security runbook
- **Timeline:** 1 week before deployment

**Exit Criteria:**
- [ ] Pre-deployment security checklist approved
- [ ] Production configurations reviewed and approved
- [ ] Security monitoring operational
- [ ] Security runbook documented
- [ ] Final security sign-off obtained

**Artifacts:**
- Pre-Deployment Security Checklist
- Configuration Review Report
- Security Monitoring Configuration
- Security Runbook

### 2.7 Maintenance Phase Security

**Phase Overview:**
- Post-production monitoring
- Bug fixes and patches
- Feature enhancements
- Decommissioning

**Entry Criteria:**
- [ ] Application deployed to production
- [ ] Security monitoring operational

**Security Activities:**

**Activity 1: Vulnerability Monitoring**
- **When:** Continuous
- **Owner:** Security Team
- **Process:** Monitor CVEs, vendor advisories, security alerts for application components
- **Output:** Vulnerability alerts, patch requirements
- **Timeline:** Continuous

**Activity 2: Security Patch Management**
- **When:** Per vulnerability alert
- **Owner:** Development Team + Operations
- **Process:** Assess impact, test patch, deploy to production
- **Output:** Patch deployment record
- **Timeline:** Per SLA (critical: 24-72 hours, high: 7-14 days)

**Activity 3: Security Log Review**
- **When:** Daily/weekly (based on risk)
- **Owner:** Security Operations
- **Process:** Review security logs, identify anomalies, investigate incidents
- **Output:** Security review reports, incident tickets
- **Timeline:** Daily for high-risk apps, weekly for medium-risk

**Activity 4: Annual Security Reassessment**
- **When:** Annually or after major changes
- **Owner:** Security Architect
- **Process:** Re-run threat modeling, architecture review, update security requirements
- **Output:** Updated threat model, architecture review, security requirements
- **Timeline:** 2-3 weeks annually

**Activity 5: Secure Decommissioning**
- **When:** Application retirement
- **Owner:** Security Team + Operations
- **Process:** Data deletion, credential revocation, access removal, audit logging
- **Output:** Decommissioning checklist
- **Timeline:** 1 week

**Artifacts:**
- Vulnerability Monitoring Reports
- Patch Deployment Records
- Security Log Reviews
- Annual Reassessment Reports
- Decommissioning Checklist

---

## 3. SDLC Methodology-Specific Implementation

### 3.1 Waterfall Security Integration

**Characteristics:**
- Sequential phases (Requirements → Design → Development → Testing → Deployment)
- Phase gates with formal approvals
- Comprehensive upfront planning
- Less frequent releases

**Security Implementation Strategy:**

**Security Gates:**
- **Gate 1 (After Requirements):** Security requirements approved
- **Gate 2 (After Design):** Threat model + architecture review approved
- **Gate 3 (After Development):** SAST/SCA passed, code review complete
- **Gate 4 (After Testing):** DAST/pentest passed, security acceptance complete
- **Gate 5 (Before Deployment):** Pre-deployment checklist approved, final security sign-off

**Timeline Integration:**

```
┌─────────────────────────────────────────────────────────────────┐
│ WATERFALL SDLC WITH SECURITY GATES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Requirements (4 weeks)                                          │
│   ├─ Week 1-2: Functional requirements                         │
│   ├─ Week 2-3: Security requirements (IMP-S1)                  │
│   └─ Week 4: Security requirements approval ✓ [GATE 1]         │
│                                                                 │
│ Design (6 weeks)                                                │
│   ├─ Week 1-2: High-level architecture                         │
│   ├─ Week 3: Threat modeling workshop                          │
│   ├─ Week 4-5: Detailed design                                 │
│   └─ Week 6: Architecture review ✓ [GATE 2]                    │
│                                                                 │
│ Development (12 weeks)                                          │
│   ├─ Week 1-10: Coding (SAST/SCA automated per commit)         │
│   ├─ Week 11: Final code review                                │
│   └─ Week 12: SAST/SCA clean, review approved ✓ [GATE 3]       │
│                                                                 │
│ Testing (4 weeks)                                               │
│   ├─ Week 1-2: QA testing + DAST scanning                      │
│   ├─ Week 3: Security acceptance testing                       │
│   └─ Week 4: Pentest (if high-risk) ✓ [GATE 4]                 │
│                                                                 │
│ Deployment (1 week)                                             │
│   ├─ Day 1-2: Pre-deployment checklist                         │
│   ├─ Day 3: Production deployment                              │
│   └─ Day 4-5: Security monitoring verification ✓ [GATE 5]      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Success Factors:**
- Front-load security activities (requirements, threat modeling)
- Formal security gate approvals with documentation
- Comprehensive upfront threat modeling (fewer changes later)
- Dedicated security review time built into schedule

**Common Pitfalls:**
- ❌ Skipping threat modeling to save time (expensive later)
- ❌ Late security involvement (after design complete)
- ❌ Inadequate security gate enforcement (approve with findings)

### 3.2 Agile/Scrum Security Integration

**Characteristics:**
- Iterative sprints (typically 2 weeks)
- Continuous planning and adaptation
- Frequent releases
- User stories and acceptance criteria

**Security Implementation Strategy:**

**Sprint 0 (Pre-Development):**
- Security requirements elicitation
- Initial threat modeling
- Architecture review
- Security tooling setup (SAST, SCA, secret scanning in CI/CD)

**Per Sprint Security Activities:**

**Sprint Planning:**
- [ ] Security user stories prioritized (e.g., "As a user, I need MFA to protect my account")
- [ ] Security acceptance criteria defined for each user story
- [ ] Security tasks sized and assigned

**During Sprint:**
- [ ] SAST/SCA automated per commit (developers fix immediately)
- [ ] Code review includes security checklist (peer review + security champion review)
- [ ] Security unit tests written and executed
- [ ] Threat model updated if architecture changes

**Sprint Review:**
- [ ] Security acceptance criteria demonstrated
- [ ] Security findings from sprint reviewed

**Sprint Retrospective:**
- [ ] Security process improvements identified
- [ ] Security tool effectiveness discussed

**Definition of Done (DoD) - Security Criteria:**
- ✅ Security acceptance criteria met
- ✅ SAST scan passed (no high/critical findings)
- ✅ SCA scan passed (no high/critical vulnerabilities)
- ✅ Code review approved with security checklist
- ✅ Security unit tests passing
- ✅ No hardcoded secrets

**Release Security Activities:**
- [ ] DAST scan on release candidate
- [ ] Security regression testing
- [ ] Pre-production security checklist
- [ ] Security sign-off for release

**Timeline Integration:**

```
┌──────────────────────────────────────────────────────────────┐
│ AGILE/SCRUM WITH SECURITY INTEGRATION                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ Sprint 0 (2 weeks) - Security Foundation                    │
│   ├─ Security requirements elicitation                      │
│   ├─ Initial threat modeling                                │
│   ├─ Architecture review                                    │
│   └─ Security tool setup (SAST, SCA, CI/CD)                 │
│                                                              │
│ Sprint 1-N (2 weeks each) - Iterative Development           │
│   ├─ Sprint Planning: Security stories prioritized          │
│   ├─ Daily Development:                                     │
│   │   ├─ SAST/SCA automated per commit                      │
│   │   ├─ Code review (security checklist)                   │
│   │   └─ Security unit tests                                │
│   ├─ Sprint Review: Security acceptance criteria verified   │
│   └─ Retrospective: Security process improvements           │
│                                                              │
│ Release Sprint (every 4-6 sprints)                          │
│   ├─ DAST scanning                                          │
│   ├─ Security regression testing                            │
│   ├─ Pre-production checklist                               │
│   └─ Security sign-off                                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Key Success Factors:**
- Embed security in Definition of Done
- Automate security testing (SAST, SCA) for fast feedback
- Security champion in each team (see Section 4.3)
- Security stories treated as first-class work items

**Common Pitfalls:**
- ❌ Treating security as "tech debt" (never prioritized)
- ❌ No security in DoD (security bypassed for velocity)
- ❌ Manual security testing (too slow for sprint cadence)

### 3.3 DevOps/DevSecOps Security Integration

**Characteristics:**
- Continuous Integration/Continuous Deployment (CI/CD)
- Infrastructure as Code (IaC)
- High deployment frequency (daily/weekly)
- Heavy automation

**Security Implementation Strategy:**

**"Shift Left" Security:**
- Security integrated early (requirements, design)
- Security automated in CI/CD pipeline
- Security feedback in real-time (not batch/manual)

**CI/CD Pipeline Security Integration:**

```
┌──────────────────────────────────────────────────────────────┐
│ DEVSECOPS CI/CD PIPELINE                                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ Developer Workstation                                        │
│   ├─ IDE security plugins (real-time SAST)                  │
│   ├─ Pre-commit hooks (secret scanning)                     │
│   └─ Local unit tests (including security tests)            │
│          ↓                                                   │
│ Commit to Version Control (Git)                             │
│          ↓                                                   │
│ CI Pipeline (Automated)                                      │
│   ├─ Step 1: Build                                          │
│   ├─ Step 2: SAST scan (SonarQube, Snyk Code, etc.)         │
│   │   └─ FAIL build if high/critical findings              │
│   ├─ Step 3: SCA scan (Snyk, Dependabot, etc.)              │
│   │   └─ FAIL build if high/critical vulnerabilities       │
│   ├─ Step 4: Secret scanning (TruffleHog, GitGuardian)      │
│   │   └─ FAIL build if secrets detected                    │
│   ├─ Step 5: Unit tests (including security tests)          │
│   └─ Step 6: Container image scanning (if containers)       │
│          ↓                                                   │
│ Deploy to Test Environment                                  │
│          ↓                                                   │
│ Test Pipeline (Automated)                                    │
│   ├─ Step 1: DAST scan (OWASP ZAP, Burp Suite)              │
│   ├─ Step 2: API security testing                           │
│   └─ Step 3: Security acceptance tests                      │
│          ↓                                                   │
│ Deploy to Staging (if applicable)                           │
│   ├─ Infrastructure security scan (IaC analysis)             │
│   └─ Security configuration validation                      │
│          ↓                                                   │
│ Manual Security Gate (High-Risk Apps)                       │
│   ├─ Security Architect review                              │
│   └─ Penetration testing (periodic)                         │
│          ↓                                                   │
│ Deploy to Production                                        │
│   ├─ Production security checklist (automated)              │
│   ├─ Security monitoring enabled                            │
│   └─ Security dashboards updated                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Pipeline Configuration:**

**Build Stage:**
```yaml
# Example: GitLab CI/CD security integration
stages:
  - build
  - security_scan
  - test
  - deploy

build:
  stage: build
  script:
    - mvn clean package

sast_scan:
  stage: security_scan
  script:
    - sonar-scanner
  allow_failure: false  # FAIL pipeline on high/critical findings

sca_scan:
  stage: security_scan
  script:
    - snyk test --severity-threshold=high
  allow_failure: false

secret_scan:
  stage: security_scan
  script:
    - trufflehog --regex --entropy=False .
  allow_failure: false

dast_scan:
  stage: test
  script:
    - zap-baseline.py -t https://test.example.com
  allow_failure: false  # Fail on high findings
```

**Infrastructure as Code (IaC) Security:**
- Scan IaC templates (Terraform, CloudFormation) for misconfigurations
- Tools: Checkov, Terrascan, tfsec
- Enforce security baselines (no public S3 buckets, encryption required, etc.)

**Container Security:**
- Scan container images for vulnerabilities (Trivy, Clair, Snyk Container)
- Enforce base image security policies (only approved images)
- Runtime security monitoring (Falco, Aqua Security)

**Key Success Factors:**
- Full automation of security testing (no manual gates except high-risk)
- Fast feedback loops (security results in minutes, not days)
- Fail fast (break builds on critical security findings)
- Security metrics in dashboards (visibility)

**Common Pitfalls:**
- ❌ Bypassing security checks for "urgent" deploys
- ❌ Alert fatigue from too many false positives (tune tools)
- ❌ No rollback plan when security issues found in production

### 3.4 Hybrid SDLC Security Integration

**Characteristics:**
- Mix of methodologies (e.g., Agile for development, Waterfall for infrastructure)
- Legacy and modern systems coexisting
- Gradual DevOps adoption

**Security Implementation Strategy:**
- Apply methodology-specific guidance above to each component
- Ensure security requirements consistent across methodologies
- Use hybrid security gates (formal for Waterfall components, automated for Agile/DevOps)

**Example Hybrid Model:**
- Core platform: Waterfall with formal security gates
- Feature development: Agile sprints with automated security
- Infrastructure: DevOps with IaC security scanning

---

## 4. Security Champion Program

### 4.1 Program Overview

**Purpose:** Establish a network of security advocates within development teams to promote security awareness and best practices.

**Model:** Distributed security responsibility
- **Not:** Dedicated security team members in each team (too expensive)
- **Instead:** Developers with additional security responsibilities (10-20% time)

**Benefits:**
- Scales security expertise across organization
- Faster security feedback (embedded in teams)
- Security culture improvement
- Reduced bottlenecks (not all security through central team)

### 4.2 Security Champion Selection

**Selection Criteria:**

**Required Attributes:**
- Active developer in team (not manager)
- Genuine interest in security (not voluntold)
- Respected by team (peer influence)
- Good communicator (can explain security to non-experts)
- Minimum 2 years development experience

**Desirable Attributes:**
- Prior security experience (training, certifications, CTF participation)
- Cross-functional skills (knows infrastructure, DevOps)
- Proactive problem-solver

**Selection Process:**

**Step 1: Call for Volunteers**
- Announce program to all development teams
- Explain role, responsibilities, benefits
- Request volunteers (self-nomination)

**Step 2: Manager Endorsement**
- Volunteer's manager confirms availability (10-20% time allocation)
- Manager acknowledges champion responsibilities

**Step 3: Security Team Interview**
- Security team interviews candidates (30 min)
- Assess security interest, communication skills
- Explain program expectations

**Step 4: Selection and Onboarding**
- Select 1-2 champions per team (redundancy)
- Provide onboarding training (see Section 4.4)
- Assign buddy (existing champion for mentorship)

### 4.3 Security Champion Responsibilities

**Core Responsibilities:**

**1. Security Code Review (30% of time)**
- Review pull requests with security focus
- Use security code review checklist (IMP-S3)
- Escalate complex security issues to Security Team

**2. Security Advocacy (20% of time)**
- Promote secure coding practices in team
- Share security news, vulnerabilities, lessons learned
- Organize security brown bag sessions (optional)

**3. Security Requirements Support (20% of time)**
- Support security requirements elicitation
- Help translate security requirements to user stories
- Participate in threat modeling workshops

**4. Security Tool Triage (20% of time)**
- Triage SAST/SCA findings (true positive vs. false positive)
- Help developers understand and fix security findings
- Provide feedback to Security Team on tool effectiveness

**5. Security Incident Support (10% of time)**
- Assist Security Team during security incidents affecting their team
- Provide context on code, architecture during investigations
- Support remediation efforts

**Not Responsible For:**
- ❌ Architecture security reviews (Security Architect's role)
- ❌ Penetration testing (Security Team's role)
- ❌ Security policy creation (Security Team's role)
- ❌ Replacing Security Team (champions augment, not replace)

### 4.4 Security Champion Training

**Initial Training (2 days):**

**Day 1: Security Fundamentals**
- OWASP Top 10 deep dive (with coding examples)
- Secure coding principles (input validation, output encoding, authentication, authorization)
- Cryptography basics (when to encrypt, which algorithms)
- Threat modeling introduction (STRIDE overview)
- Security requirements basics

**Day 2: Tools and Processes**
- SAST/SCA tool training (how to read results, triage findings)
- Code review for security (using security checklist)
- CI/CD security integration
- Incident response basics
- Security champion program logistics

**Ongoing Training (quarterly):**
- Advanced security topics (e.g., API security, cloud security, container security)
- New vulnerabilities and exploits (CVE analysis)
- Security tool updates
- Guest speakers (security researchers, pentesters)

**Self-Paced Learning:**
- Access to security training platforms (Pluralsight, Coursera, SANS Cyber Aces)
- Capture The Flag (CTF) challenges
- Bug bounty programs (ethical hacking practice)

### 4.5 Security Champion Community

**Monthly Security Champion Meetings:**
- Share lessons learned across teams
- Discuss common security challenges
- Feedback to Security Team on tools, processes
- Security news and updates
- Recognition and awards

**Communication Channels:**
- Dedicated Slack/Teams channel (#security-champions)
- Email distribution list
- Knowledge base (Confluence, SharePoint) with security resources

**Recognition and Incentives:**
- Quarterly "Security Champion of the Quarter" award
- Annual security champions conference/offsite
- Security certifications sponsored (GSSP, CEH, OSCP)
- Career development opportunities (path to Security Team)

### 4.6 Program Metrics

**Champion Engagement:**
- % of teams with active security champions (target: 100%)
- Champion retention rate (target: >80% annually)
- Champion training completion rate (target: 100%)

**Impact Metrics:**
- Security code review coverage (target: 100% of PRs)
- SAST/SCA finding remediation time (target: <7 days for high findings)
- Security incidents attributed to code (target: <5 per quarter)
- Developer security knowledge (measured via surveys/quizzes)

**Track Quarterly:**
- Champions conduct retrospective with Security Team
- Adjust program based on feedback
- Update training materials

---

## 5. Developer Security Training Program

### 5.1 Training Program Overview

**Purpose:** Ensure all developers have foundational security knowledge and skills to write secure code.

**Training Tiers:**

**Tier 1: All Developers (Mandatory)**
- Initial secure coding training (onboarding)
- Annual refresher training

**Tier 2: Security Champions (Enhanced Training)**
- Security champion training (Section 4.4)
- Quarterly advanced topics

**Tier 3: Senior Developers/Architects (Specialized)**
- Threat modeling training
- Security architecture training
- Language/framework-specific deep dives

### 5.2 Initial Secure Coding Training

**Target Audience:** All new developers (within 30 days of hire)

**Duration:** 8 hours (1 day instructor-led OR 2-week self-paced online)

**Training Outline:**

**Module 1: Security Fundamentals (1.5 hours)**
- Why security matters (cost of breaches, regulatory requirements)
- Security principles (least privilege, defense in depth, fail secure)
- Security in SDLC (shift left approach)
- Threat landscape overview (common attacks)

**Module 2: OWASP Top 10 (3 hours)**
- Injection attacks (SQL injection, command injection, XSS)
- Broken authentication and session management
- Sensitive data exposure
- XML external entities (XXE)
- Broken access control
- Security misconfiguration
- Cross-site scripting (XSS)
- Insecure deserialization
- Using components with known vulnerabilities
- Insufficient logging and monitoring

*Each topic includes:*
- Vulnerability explanation
- Code examples (vulnerable vs. secure)
- Hands-on exercise (fix vulnerable code)

**Module 3: Secure Coding Practices (2 hours)**
- Input validation (allowlist validation, sanitization)
- Output encoding (context-aware encoding)
- Authentication and password management (hashing, MFA)
- Authorization (RBAC, least privilege)
- Cryptography (when to use, which algorithms)
- Error handling and logging (generic errors, secure logging)
- Session management (secure session tokens)

**Module 4: Security Tools and Processes (1 hour)**
- SAST/SCA tool introduction (how to read results)
- Code review for security (checklist overview)
- Security testing overview (DAST, pentesting)
- Security requirements and threat modeling overview

**Module 5: Hands-On Lab (0.5 hours)**
- Vulnerable web application (WebGoat, Juice Shop, DVWA)
- Find and fix vulnerabilities
- Run SAST/DAST tools

**Assessment:**
- Online quiz (80% passing score required)
- Retake if failed (no limit on attempts)
- Training completion tracked in HR system

**Training Delivery Options:**
- **Option A:** Instructor-led (1 day onsite or virtual)
- **Option B:** Self-paced online (e.g., Pluralsight, Coursera, SANS Cyber Aces)
- **Option C:** Hybrid (online modules + 2-hour instructor Q&A)

### 5.3 Annual Refresher Training

**Target Audience:** All developers

**Duration:** 4 hours (self-paced online)

**Content:**
- Security policy updates
- New vulnerabilities and attack trends (last 12 months)
- OWASP Top 10 updates (if released)
- Case studies (security incidents, lessons learned)
- Tool updates (new SAST/SCA features)
- Security success stories (recognition)

**Assessment:**
- Online quiz (80% passing score)
- Training completion tracked

**Timeline:** Annually (anniversary of initial training)

### 5.4 Language-Specific Training

**Purpose:** Deep dive into security for specific programming languages/frameworks.

**Target Audience:** Developers working in specific language

**Languages Covered:**
- Java / Spring Framework
- Python / Django / Flask
- JavaScript / Node.js / React / Angular
- C# / .NET / ASP.NET Core
- Go
- PHP
- Ruby / Rails

**Content (per language):**
- Language-specific vulnerabilities (e.g., deserialization in Java, prototype pollution in JavaScript)
- Framework security features (e.g., Spring Security, Django auth)
- Secure coding patterns for language
- SAST tool results interpretation for language
- Common pitfalls and anti-patterns

**Duration:** 4 hours per language

**Delivery:** Self-paced online OR instructor-led workshop

### 5.5 Training Resources

**Internal Resources:**
- Secure coding standards (IMP-S3)
- Security code review checklists
- Vulnerable code examples (internal repository)
- Security champions knowledge base
- Recorded security presentations

**External Resources:**
- **OWASP:** Free resources (cheat sheets, testing guide, Top 10)
  - https://owasp.org/www-project-top-ten/
  - https://cheatsheetseries.owasp.org/
- **SANS Cyber Aces:** Free online tutorials
  - https://www.cyberaces.org/
- **Pluralsight:** Secure coding courses (subscription required)
- **Coursera:** Cybersecurity specializations
- **PortSwigger Web Security Academy:** Free interactive learning
  - https://portswigger.net/web-security
- **Secure Code Warrior:** Gamified secure coding training
- **CTF Platforms:** Hack The Box, TryHackMe, OverTheWire

### 5.6 Training Tracking and Compliance

**Tracking Mechanism:**
- HR/Learning Management System (LMS)
- Training completion records
- Quiz scores
- Certification expiration tracking

**Compliance Monitoring:**
- Monthly reports: % of developers trained
- Escalation: Developers overdue for training (manager notification)
- Consequences: Training completion required for annual review

**Metrics:**
- Initial training completion rate (target: 100% within 30 days of hire)
- Annual refresher completion rate (target: 100% within training window)
- Average quiz score (target: >85%)
- Training satisfaction score (target: >4.0/5.0)

---

## 6. Secure Development Environment

### 6.1 Development Environment Security Overview

**Purpose:** Ensure development environments are configured securely to prevent vulnerabilities from being introduced through environment compromise.

**Scope:**
- Developer workstations (laptops, desktops)
- Development tools (IDEs, version control clients, build tools)
- Development infrastructure (build servers, CI/CD, code repositories)
- Development network access

### 6.2 Developer Workstation Security

**Security Baseline:**

**Operating System Security:**
- [ ] Operating system fully patched (auto-update enabled)
- [ ] Disk encryption enabled (BitLocker, FileVault, LUKS)
- [ ] Screen lock after 10 minutes of inactivity
- [ ] Firewall enabled
- [ ] Antivirus/EDR installed and active

**Access Control:**
- [ ] Developers do NOT have local admin rights (privilege escalation as needed)
- [ ] Multi-factor authentication (MFA) for all accounts (VPN, corporate apps, code repos)
- [ ] Password manager mandatory (no plaintext passwords in notes/files)

**Software Restrictions:**
- [ ] Only approved software installed (software allowlist)
- [ ] Automatic security updates for development tools
- [ ] No pirated or unlicensed software

**Data Protection:**
- [ ] Production data NOT permitted on developer workstations
- [ ] Synthetic/anonymized data for development and testing
- [ ] Data classification labels respected (no sensitive data in dev environment)

**Monitoring:**
- [ ] Endpoint Detection and Response (EDR) installed
- [ ] Security logs forwarded to central SIEM (login attempts, privilege escalation)

### 6.3 Development Tool Security

**IDE Security Plugins:**
- **SonarLint:** Real-time SAST feedback in IDE (IntelliJ, VS Code, Eclipse)
- **Snyk Code:** IDE security scanning for vulnerabilities
- **GitGuardian:** Secret scanning in IDE (prevent commits with secrets)
- **Checkmarx CxIAST Plugin:** Interactive security testing in IDE

**IDE Configuration:**
- Auto-save disabled for sensitive files (prevent accidental commits of secrets)
- Diff review before commit (catch accidental secrets)
- Code snippet templates include security best practices

**Version Control Client Security:**
- **Git Hooks:** Pre-commit hooks for secret scanning (TruffleHog, git-secrets)
- **Signed Commits:** GPG-signed commits for authenticity (recommended for high-risk projects)
- **Credential Management:** Use SSH keys or PATs (Personal Access Tokens), never passwords

**Build Tool Security:**
- **Dependency Verification:** Verify checksums/signatures for dependencies (Maven, npm, pip)
- **Repository Restrictions:** Only trusted repositories (no public repos without approval)
- **Build Isolation:** Builds run in isolated environments (containers, VMs)

### 6.4 Code Repository Security

**Access Control:**
- [ ] Multi-factor authentication (MFA) required for all users
- [ ] Role-based access control (RBAC): Developers have write access to their repos only
- [ ] Branch protection: Main/master branch requires pull request + approval
- [ ] No direct commits to main/master (enforce PR workflow)

**Secret Protection:**
- [ ] Secret scanning enabled (GitHub secret scanning, GitGuardian, GitLab secret detection)
- [ ] Pre-receive hooks block commits with secrets
- [ ] Historical secret scanning (scan existing commits for secrets)

**Audit and Monitoring:**
- [ ] Audit logging enabled (all access, commits, PR approvals)
- [ ] Alerts for suspicious activity (mass deletions, unauthorized access)
- [ ] Periodic access reviews (remove inactive users)

**Repository Configuration:**
- [ ] Public repositories require approval (prevent accidental exposure)
- [ ] README includes security contact (security@example.com)
- [ ] SECURITY.md file with vulnerability disclosure policy

### 6.5 CI/CD Pipeline Security

**Build Server Security:**
- [ ] Dedicated build servers (not shared with production)
- [ ] Build servers patched and hardened (minimal software installed)
- [ ] Build isolation (each build in isolated container/VM)
- [ ] No production credentials on build servers

**Pipeline Configuration Security:**
- [ ] Pipeline-as-Code (Jenkinsfile, .gitlab-ci.yml, GitHub Actions) version-controlled
- [ ] Code review required for pipeline changes
- [ ] Secret management: Secrets stored in vault (HashiCorp Vault, AWS Secrets Manager), not hardcoded
- [ ] Least privilege: Pipelines run with minimal permissions

**Artifact Security:**
- [ ] Artifacts signed (code signing certificates)
- [ ] Artifact scanning before deployment (malware, vulnerabilities)
- [ ] Artifact repository access control (only authorized users/systems)

**Deployment Credential Protection:**
- [ ] No hardcoded deployment credentials in code or pipelines
- [ ] Credential rotation (90 days or per policy)
- [ ] Just-in-time (JIT) credentials where possible (temporary AWS keys, etc.)

### 6.6 Development Network Segmentation

**Network Architecture:**

```
┌──────────────────────────────────────────────────┐
│ Corporate Network Segmentation                   │
├──────────────────────────────────────────────────┤
│                                                  │
│ Production Network (Isolated)                    │
│   ├─ Production Servers                         │
│   ├─ Production Databases                       │
│   └─ NO direct access from development          │
│                     ↑                            │
│         Firewall / Access Control                │
│                     ↓                            │
│ Development/Test Network (Segmented)             │
│   ├─ Development Servers                        │
│   ├─ Test Databases (synthetic data)            │
│   ├─ CI/CD Infrastructure                       │
│   └─ Developer VPN access                       │
│                     ↑                            │
│         Firewall / Access Control                │
│                     ↓                            │
│ Developer Workstations (Managed)                 │
│   ├─ Corporate laptops (EDR, encryption)        │
│   └─ VPN for remote access                      │
│                                                  │
└──────────────────────────────────────────────────┘
```

**Access Control:**
- Developers have NO direct access to production (see A.8.31)
- Development/test network separated from production
- VPN required for remote development work
- Multi-hop access for production (bastion hosts, privileged access management)

---

## 7. Assessment Workbook 2 Specification (Script 2)

### 7.1 Workbook Overview

**Workbook Name:** `ISMS_A825_SDLC_Security_Activities_Assessment_[Date].xlsx`

**Purpose:** Assess security activities throughout SDLC per application and track compliance with secure development lifecycle requirements.

**Assessment Scope:**
- ISO/IEC 27001:2022 Control A.8.25 (Secure Development Lifecycle)
- Security activities per SDLC phase
- Secure coding standards adoption
- Code review and security testing
- Security tools deployment and usage
- Developer training compliance
- Security defect management

### 7.2 Workbook Sheet Structure

**Sheet 1: Instructions & Legend**
- Workbook purpose and scope
- How to use the workbook
- Status legend (emoji indicators)
- Acceptable evidence examples
- Scoring methodology overview

**Sheet 2: SDLC_Phase_Activities**
- Application name
- SDLC methodology (Waterfall, Agile, DevOps, Hybrid)
- Security activities by phase (Requirements, Design, Development, Testing, Deployment, Maintenance)
- Activity completion status (✅ Complete, ⏳ In Progress, ❌ Not Done, N/A)
- Evidence location/link
- Compliance score per phase (auto-calculated)

**Sheet 3: Secure_Coding_Standards**
- Application name
- Secure coding standard adopted (OWASP, CWE, language-specific)
- Standard documented and accessible? (Yes/No)
- Developers trained on standard? (Yes/No)
- Standard enforced via tools? (Yes/No)
- Standard enforced via code review? (Yes/No)
- Last standard update date
- Compliance score (auto-calculated)

**Sheet 4: Code_Review_Metrics**
- Application name
- Code review process documented? (Yes/No)
- Code review coverage (% of code reviewed)
- Security checklist used in reviews? (Yes/No)
- Security champion involved in reviews? (Yes/No)
- Average code review turnaround time (days)
- Security findings from code review (count)
- Code review compliance score (auto-calculated)

**Sheet 5: Security_Tools_Deployment**
- Tool type (SAST, SCA, Secret Scanning, DAST, Container Scanning)
- Tool name/vendor
- Deployment status (✅ Deployed, ⏳ In Progress, ❌ Not Deployed)
- Applications covered by tool
- Integration point (IDE, CI/CD, Manual)
- Tool configuration reviewed? (Yes/No)
- Tool effectiveness (findings detected, false positive rate)

**Sheet 6: Security_Tools_Usage**
- Application name
- SAST scans per week/month (frequency)
- SCA scans per week/month (frequency)
- Secret scanning enabled? (Yes/No)
- DAST scans per release
- Average finding remediation time (days)
- Tool usage compliance score (auto-calculated)

**Sheet 7: Developer_Training**
- Developer name or team
- Initial secure coding training completed? (Yes/No/Date)
- Annual refresher training completed? (Yes/No/Date)
- Language-specific training completed? (Yes/No/Date)
- Security champion training (if applicable)? (Yes/No/Date)
- Training quiz score (%)
- Training overdue? (Yes/No - auto-calculated)
- Training compliance (% trained)

**Sheet 8: Security_Defect_Management**
- Application name
- Open security defects (count by severity: Critical, High, Medium, Low)
- Average age of open security defects (days)
- Security defect SLA compliance (% fixed within SLA)
- Security technical debt (count of accepted risks)
- Defect trends (month-over-month)

**Sheet 9: Compliance_Summary**
- **Dashboard view** with overall SDLC security scores
- Overall SDLC compliance score (weighted average)
- Compliance by SDLC phase
- Compliance by application
- Gap summary (activities not performed, tools not deployed, training overdue)
- Conditional formatting (green/yellow/red)

**Sheet 10: Evidence_Register**
- Evidence type (SDLC checklist, code review record, training certificate, tool report)
- Application name or team
- Document title/description
- Document location/link
- Last updated
- Owner
- Status (Current, Outdated, Missing)

**Sheet 11: Approval_Sign_Off**
- Assessment information (date, assessor, organization)
- Approval table (Approver, Role, Date, Signature/Comments)
- Overall compliance determination
- Recommended actions

### 7.3 Data Sources

**SDLC Phase Activities (Sheet 2):**
- Source: Project documentation, SDLC checklists, security gate records
- Update: After each project phase or sprint

**Secure Coding Standards (Sheet 3):**
- Source: Secure coding standard documents, training materials
- Update: Quarterly or when standards updated

**Code Review Metrics (Sheet 4):**
- Source: Code review tools (GitHub PR reviews, GitLab MR reviews, Azure DevOps PR stats)
- Update: Monthly (aggregate monthly metrics)

**Security Tools Deployment (Sheet 5):**
- Source: DevOps/Security Team inventory, CI/CD pipeline configurations
- Update: Quarterly

**Security Tools Usage (Sheet 6):**
- Source: SAST/SCA/DAST tool reports, vulnerability management system
- Update: Monthly

**Developer Training (Sheet 7):**
- Source: HR/LMS (Learning Management System), training records
- Update: Monthly

**Security Defect Management (Sheet 8):**
- Source: Issue tracking system (Jira, Azure DevOps, GitHub Issues)
- Update: Monthly

### 7.4 Scoring Algorithms

**SDLC Phase Activities Compliance (Sheet 2):**

For each SDLC phase, calculate:
```
Phase Score = (Completed Activities / Total Applicable Activities) × 100%

Overall SDLC Score = Average of all phase scores
```

Example Excel Formula (if 10 activities tracked per phase):
```
=COUNTIF(C4:L4,"✅ Complete")/COUNTIF(C4:L4,"<>N/A")*100
```

**Secure Coding Standards Compliance (Sheet 3):**

```
Standards Score = (Sum of Yes responses / Total questions) × 100%

Where questions are:
1. Standard documented? (Yes=25%)
2. Developers trained? (Yes=25%)
3. Enforced via tools? (Yes=25%)
4. Enforced via code review? (Yes=25%)
```

Example Excel Formula:
```
=((IF(C4="Yes",25,0))+(IF(D4="Yes",25,0))+(IF(E4="Yes",25,0))+(IF(F4="Yes",25,0)))
```

**Code Review Compliance (Sheet 4):**

```
Code Review Score = (
    (Code review process documented? × 20%) +
    (Code review coverage% × 40%) +
    (Security checklist used? × 20%) +
    (Security champion involved? × 20%)
)
```

Example Excel Formula:
```
=IF(B4="Yes",20,0)+(C4*0.4)+IF(D4="Yes",20,0)+IF(E4="Yes",20,0)
```

**Security Tools Usage Compliance (Sheet 6):**

```
Tool Usage Score = (
    (SAST frequency meets target × 25%) +
    (SCA frequency meets target × 25%) +
    (Secret scanning enabled × 25%) +
    (DAST per release × 25%)
)

Targets:
- SAST: ≥ 1 per week (Agile/DevOps) or per phase (Waterfall)
- SCA: ≥ 1 per week (Agile/DevOps) or per phase (Waterfall)
- Secret scanning: Enabled (binary)
- DAST: ≥ 1 per release
```

**Developer Training Compliance (Sheet 7):**

```
Training Compliance = (Trained Developers / Total Developers) × 100%

Trained = (Initial training complete AND Annual refresher current)
```

Example Excel Formula:
```
=IF(AND(B4<>"",C4<>"",C4>=TODAY()-365),1,0)
```

**Overall SDLC Compliance Score (Sheet 9):**

```
Overall Score = (
    SDLC Activities Score × 30% +
    Standards Compliance × 15% +
    Code Review Score × 15% +
    Tool Usage Score × 20% +
    Training Compliance × 10% +
    Defect Management Score × 10%
)
```

**Compliance Status:**
- ✅ **Compliant:** Overall Score ≥ 80%
- ⚠️ **Partial Compliance:** Overall Score 60-79%
- ❌ **Non-Compliant:** Overall Score < 60%

### 7.5 Conditional Formatting Rules

**Apply to Sheet 9 (Compliance_Summary):**

**Overall Compliance Score:**
- Green (C6EFCE): Score ≥ 80%
- Yellow (FFEB9C): Score 60-79%
- Red (FFC7CE): Score < 60%

**Training Overdue (Sheet 7):**
- Red bold: Overdue training (last training > 365 days ago)

**Security Defect Age (Sheet 8):**
- Red bold: Critical defects > 7 days old
- Orange: High defects > 30 days old
- Yellow: Medium defects > 90 days old

### 7.6 Example Data Rows

**Sheet 2 Example (SDLC_Phase_Activities):**

| Application | Methodology | Req Phase: Sec Req Defined | Design Phase: Threat Model | Dev Phase: SAST Enabled | Test Phase: DAST Scan | Deploy Phase: Sec Checklist | Phase Compliance |
|-------------|-------------|---------------------------|---------------------------|------------------------|----------------------|---------------------------|------------------|
| Customer Portal | Agile | ✅ Complete | ✅ Complete | ✅ Complete | ✅ Complete | ✅ Complete | 100% |
| Internal HR | Waterfall | ✅ Complete | ✅ Complete | ⏳ In Progress | ❌ Not Done | N/A | 50% |
| Marketing Site | DevOps | ✅ Complete | N/A | ✅ Complete | ✅ Complete | ✅ Complete | 100% |

**Sheet 7 Example (Developer_Training):**

| Developer/Team | Initial Training | Annual Refresher | Language Training | Security Champion | Quiz Score | Overdue? |
|----------------|------------------|------------------|-------------------|-------------------|------------|----------|
| Alice Johnson | 2024-03-15 | 2025-01-10 | 2024-06-20 | N/A | 92% | No |
| Bob Williams | 2023-05-10 | 2024-01-15 | N/A | Yes (2024-08-12) | 88% | Yes |
| Dev Team A | 85% trained | 70% current | 60% | 2 champions | Avg: 86% | 30% overdue |

### 7.7 Data Validation Dropdowns

**SDLC Methodology:**
- Values: "Waterfall", "Agile", "Scrum", "DevOps", "DevSecOps", "Hybrid"

**Activity Status:**
- Values: "✅ Complete", "⏳ In Progress", "❌ Not Done", "N/A"

**Yes/No Fields:**
- Values: "Yes", "No"

**Tool Deployment Status:**
- Values: "✅ Deployed", "⏳ In Progress", "❌ Not Deployed", "N/A"

**Evidence Status:**
- Values: "Current", "Outdated", "Missing"

---

## 8. Implementation Timeline

### 8.1 Phased Rollout Plan

**Phase 1: Foundation (Month 1-2)**

*Month 1:*
- [ ] Document current SDLC methodology
- [ ] Establish security gate criteria
- [ ] Select and train initial security champions (1-2 per team)
- [ ] Deploy basic security tools (SAST, SCA) in CI/CD

*Month 2:*
- [ ] Conduct initial developer security training (all developers)
- [ ] Implement pre-commit secret scanning
- [ ] Document secure coding standards
- [ ] Pilot SDLC security integration in 1-2 projects

**Phase 2: SDLC Integration (Month 3-6)**

*Month 3-4:*
- [ ] Roll out security gates to all new projects
- [ ] Implement automated security testing in CI/CD (all projects)
- [ ] Establish code review security checklist
- [ ] Deploy IDE security plugins

*Month 5-6:*
- [ ] Integrate security requirements into backlog/project planning
- [ ] Conduct threat modeling training (architects, senior devs)
- [ ] Establish security defect SLAs
- [ ] First SDLC security assessment (Assessment Workbook 2)

**Phase 3: Optimization (Month 7-12)**

*Month 7-9:*
- [ ] Refine security tooling (reduce false positives)
- [ ] Advanced security training (language-specific, advanced topics)
- [ ] Expand security champion program (all teams)
- [ ] Implement security metrics dashboards

*Month 10-12:*
- [ ] Annual security training refresher
- [ ] Process optimization based on metrics
- [ ] Threat model updates for existing applications
- [ ] Continuous improvement planning

**Phase 4: Maturity (Year 2+)**

*Ongoing:*
- [ ] Maintain training compliance
- [ ] Quarterly security assessments
- [ ] Annual SDLC process review
- [ ] Continuous tool and process improvements

### 8.2 Resource Requirements

**Roles and Time Commitment:**

**Security Architects:**
- SDLC framework design: 2-4 weeks (one-time)
- Security gate reviews: 2-4 hours per project
- Threat modeling facilitation: 3-4 hours per application
- Tool deployment and configuration: 2-3 weeks (one-time)

**Development Managers:**
- SDLC process updates: 1-2 weeks per team (one-time)
- Security gate integration: Ongoing (1-2 hours per sprint/phase)
- Resource allocation for security activities

**Security Champions:**
- Initial training: 2 days (one-time)
- Ongoing responsibilities: 10-20% time (4-8 hours/week)
- Monthly champion meetings: 1 hour/month

**Developers:**
- Initial secure coding training: 1 day (one-time)
- Annual refresher training: 4 hours/year
- Security activities in SDLC: Built into normal development time

**DevOps/Infrastructure:**
- CI/CD security tool integration: 2-4 weeks (one-time)
- Tool maintenance: 2-4 hours/week (ongoing)

### 8.3 Success Metrics

**Process Metrics:**
- % of projects with security gates implemented (target: 100%)
- Security gate pass rate (target: >90% first-time pass after first year)
- Average security gate review time (target: <2 days)

**Tool Adoption Metrics:**
- % of applications with SAST enabled (target: 100%)
- % of applications with SCA enabled (target: 100%)
- % of commits scanned for secrets (target: 100%)
- % of releases with DAST scan (target: 100% for high-risk)

**Training Metrics:**
- % of developers with initial training (target: 100%)
- % of developers current on annual refresher (target: >95%)
- Average training quiz score (target: >85%)

**Security Outcome Metrics:**
- Security vulnerabilities found in production (target: <5 per quarter)
- Average time to remediate high-severity vulnerabilities (target: <14 days)
- Security incidents caused by code defects (target: <2 per year)

**Champion Program Metrics:**
- % of teams with security champions (target: 100%)
- Security champion retention rate (target: >80%)
- Champion satisfaction score (target: >4.0/5.0)

---

## 9. Common Pitfalls and Solutions

### 9.1 SDLC Integration Pitfalls

**Pitfall 1: Security as Afterthought**

❌ **Problem:** Security activities added at end of SDLC (e.g., "security review before production")  
**Impact:** Expensive to fix, delays releases, poor security outcomes

✅ **Solution:**
- Integrate security from requirements phase
- Implement security gates (cannot progress without security completion)
- Make security part of "definition of done"

**Pitfall 2: Manual Security Bottlenecks**

❌ **Problem:** All security activities require manual Security Team involvement  
**Impact:** Security Team overwhelmed, becomes release bottleneck

✅ **Solution:**
- Automate security testing (SAST, SCA, DAST) in CI/CD
- Distribute security responsibility (security champions)
- Reserve manual Security Team effort for high-value activities (architecture reviews, pentesting)

**Pitfall 3: Security vs. Velocity False Dichotomy**

❌ **Problem:** Security seen as slowing down development  
**Impact:** Developers bypass security, pressure to skip security gates

✅ **Solution:**
- Fast security feedback (automated tools, seconds/minutes not days)
- Shift left (find vulnerabilities early when cheap to fix)
- Demonstrate cost of security incidents (downtime, breach response)

### 9.2 Tool Implementation Pitfalls

**Pitfall 1: Alert Fatigue**

❌ **Problem:** SAST/SCA tools generate thousands of findings (many false positives)  
**Impact:** Developers ignore findings, tools become noise

✅ **Solution:**
- Tune tools (reduce false positives, focus on high-severity)
- Start with blocking only critical findings, expand gradually
- Triage findings (security champions help categorize true vs. false positives)

**Pitfall 2: Tool Sprawl**

❌ **Problem:** Too many security tools, no integration  
**Impact:** Tool overlap, findings not consolidated, alert fatigue

✅ **Solution:**
- Consolidate tools (one SAST tool, one SCA tool, one DAST tool)
- Centralized vulnerability management (aggregate findings from all tools)
- Integrate tools with issue tracking (Jira, Azure DevOps)

**Pitfall 3: No Remediation Workflow**

❌ **Problem:** Tools find vulnerabilities but no process to fix them  
**Impact:** Findings accumulate, never addressed

✅ **Solution:**
- Define remediation SLAs (critical: 7 days, high: 30 days, etc.)
- Integrate findings into sprint planning (security stories)
- Track remediation metrics (time to fix, % fixed within SLA)

### 9.3 Training Pitfalls

**Pitfall 1: One-Time Training**

❌ **Problem:** Developers trained once at onboarding, never again  
**Impact:** Knowledge outdates, new vulnerabilities not covered

✅ **Solution:**
- Annual refresher training (mandatory)
- Quarterly security updates (security champion meetings)
- Just-in-time training (when SAST/SCA findings detected)

**Pitfall 2: Generic Training**

❌ **Problem:** Training not relevant to developers' languages/frameworks  
**Impact:** Developers don't see value, don't apply learning

✅ **Solution:**
- Language-specific training (Java, Python, JavaScript, etc.)
- Framework-specific training (Spring, Django, React, etc.)
- Real code examples from organization's codebase

**Pitfall 3: No Training Verification**

❌ **Problem:** Training completion tracked but not knowledge retention  
**Impact:** Developers "complete" training without learning

✅ **Solution:**
- Post-training quiz (80% passing score required)
- Hands-on exercises (fix vulnerable code)
- Measure security outcomes (vulnerabilities in code declining)

---

## 10. Templates and Resources

### 10.1 Available Templates

**SDLC Security Checklist:**
- File: `SDLC_Security_Checklist_[Methodology].xlsx`
- Location: `/templates/sdlc-security/`
- Versions: Waterfall, Agile, DevOps

**Security Gate Approval Form:**
- File: `Security_Gate_Approval_Form.docx`
- Location: `/templates/sdlc-security/`
- Use: Formal security gate approvals

**Code Review Security Checklist:**
- File: `Code_Review_Security_Checklist.xlsx`
- Location: `/templates/code-review/`
- Referenced in IMP-S3

**Security Champion Onboarding Guide:**
- File: `Security_Champion_Onboarding.pdf`
- Location: `/templates/security-champions/`

### 10.2 Tool Configuration Examples

**SAST Tool Configuration (SonarQube):**
- File: `sonar-project.properties.example`
- Location: `/templates/tools/sast/`

**SCA Tool Configuration (Snyk):**
- File: `.snyk.example`
- Location: `/templates/tools/sca/`

**Pre-Commit Hook (Secret Scanning):**
- File: `pre-commit-secret-scan.sh`
- Location: `/templates/tools/secret-scanning/`

### 10.3 Training Resources

**Internal Training Materials:**
- Secure Coding Training Slides (per language)
- Vulnerable Code Examples Repository
- Security Champion Training Materials

**External Training:**
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
- Secure Code Warrior: https://www.securecodewarrior.com/
- PortSwigger Web Security Academy: https://portswigger.net/web-security

---

## 11. Integration with Other ISMS Controls

### 11.1 Integration Points

**A.8.26 (Security Requirements - IMP-S1):**
- Security requirements feed into SDLC requirements phase
- Threat models inform security requirements

**A.8.28 (Secure Coding - IMP-S3):**
- Secure coding standards applied during development phase
- Code review process integrates with SDLC

**A.8.29 (Security Testing - IMP-S4):**
- Security testing activities in testing phase
- SAST/DAST/SCA tools integrated in SDLC

**A.8.31 (Environment Separation):**
- Dev/test/prod environment separation enforced in SDLC
- No production data in development/test environments

**A.8.32 (Change Management):**
- Release management integrated with deployment phase
- Security sign-off part of change approval

**A.8.4 (Source Code Access Control):**
- Code repository security enforced in development phase
- Access control policies applied

---

## 12. Continuous Improvement

### 12.1 Process Review

**Quarterly Review:**
- SDLC security metrics review
- Security gate effectiveness
- Tool performance (false positive rate, finding remediation time)
- Security champion feedback
- Process bottlenecks identification

**Annual Review:**
- Comprehensive SDLC security assessment
- Benchmark against industry standards
- Update SDLC framework for new threats/technologies
- Update training materials

### 12.2 Metrics-Driven Improvement

**Track:**
- Security gate pass rate (should improve over time)
- Average finding remediation time (should decrease)
- Security incidents from code defects (should approach zero)
- Developer security knowledge (via quiz scores, surveys)

**Analyze:**
- Trends over time
- Correlation between training and outcomes
- Tool effectiveness
- Process efficiency

**Improve:**
- Refine security gates (adjust criteria based on data)
- Tune tools (reduce false positives)
- Enhance training (address knowledge gaps)
- Optimize processes (remove bottlenecks)

### 12.3 Staying Current

**Industry Updates:**
- Monitor OWASP Top 10 updates
- Follow security research and CVEs
- Attend security conferences (OWASP AppSec, RSA, Black Hat)
- Participate in security communities

**Technology Updates:**
- Evaluate new security tools (SAST, SCA, DAST vendors)
- Update SDLC for new development methodologies
- Adapt to cloud-native development (containers, serverless)

**Regulatory Updates:**
- Monitor regulatory changes (GDPR, PCI DSS, HIPAA updates)
- Update security requirements templates
- Update training materials for compliance

---

## 13. Support and Escalation

### 13.1 Support Contacts

**SDLC Security Questions:**
- Contact: Security Architecture Team
- Email: security-architecture@[organization].com
- Response SLA: 2 business days

**Security Champion Support:**
- Contact: Security Champion Program Lead
- Email: security-champions@[organization].com
- Slack: #security-champions

**Security Tool Support:**
- Contact: DevOps/Security Tools Team
- Email: security-tools@[organization].com
- Ticket System: [Tool Support Portal]

**Training Support:**
- Contact: Learning & Development Team
- Email: training@[organization].com

### 13.2 Escalation Path

**Issue:** Security gate blocking release (disagreement on findings)  
**Escalation:** Development Manager → Security Architect → CISO + CTO

**Issue:** Inadequate security resources (training budget, tool licenses)  
**Escalation:** Development Manager → Engineering Leadership → CISO

**Issue:** Security champion overwhelmed (too many responsibilities)  
**Escalation:** Security Champion → Security Champion Program Lead → CISO

---

## 14. Conclusion

This implementation guide provides comprehensive, step-by-step procedures for integrating security throughout the Software Development Lifecycle as defined in ISMS-POL-A.8.25-26-29-S3.

**Key Takeaways:**
- Security must be integrated into EVERY phase of SDLC (shift left)
- Security gates ensure security completion before phase progression
- Automation is critical (SAST, SCA, DAST in CI/CD for fast feedback)
- Security champions scale security expertise across organization
- Developer training is foundational (cannot write secure code without knowledge)
- Metrics drive continuous improvement

**Success Factors:**
- Executive support and resource allocation
- Methodology-specific SDLC integration (Waterfall vs. Agile vs. DevOps)
- Tool automation and integration
- Strong security champion program
- Effective training program
- Clear security gates and criteria

**Next Steps:**
1. Review this guide with Development and Security teams
2. Assess current SDLC security maturity (Assessment Workbook 2)
3. Develop implementation plan based on gaps
4. Pilot SDLC security integration in 1-2 projects
5. Refine and roll out organization-wide

For questions or support, contact the Security Architecture team.

---

**Document End**
