# ISMS-POL-A.8.25-26-29-S3
## Secure Development Lifecycle Framework (A.8.25)

**Document ID**: ISMS-POL-A.8.25-26-29-S3  
**Title**: Secure Development Lifecycle Framework - Rules for Secure Development (A.8.25)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead / Development Manager | Initial secure development lifecycle framework |

**Review Cycle**: Annual (or upon significant SDLC methodology changes or tooling updates)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead
- Implementation Owner: Development Manager / Engineering Director
- DevOps Review: DevOps Lead / SRE Manager

**Distribution**: Development teams, DevOps, security team, QA, architecture team  
**Related Documents**: 
- ISMS-POL-A.8.25-26-29-S1 (Executive Summary)
- ISMS-POL-A.8.25-26-29-S2 (Security Requirements - A.8.26)
- ISMS-POL-A.8.28 (Secure Coding - detailed coding standards)
- ISMS-IMP-A.8.25-26-29-S2 (SDLC Security Integration Implementation Guide)
- ISO/IEC 27001:2022 A.8.25

---

## 1. Purpose and Scope

### 1.1 Purpose

This document establishes **mandatory requirements** for integrating security throughout the Software Development Lifecycle (SDLC), implementing ISO/IEC 27001:2022 Control A.8.25 (Secure Development Lifecycle).

**Control Text (ISO/IEC 27001:2022 A.8.25)**:
> *Rules for the secure development of software and systems should be established and applied.*

### 1.2 Objectives

- **Integrate** security into every phase of the SDLC (not as an afterthought)
- **Establish** secure development practices and rules for all development activities
- **Deploy** security tools to detect vulnerabilities during development
- **Train** developers in secure coding and security awareness
- **Track** security defects and technical debt systematically
- **Create** a culture of security ownership within development teams

### 1.3 Scope

**In Scope**:
- All SDLC phases: Requirements, Design, Development, Testing, Deployment, Maintenance
- All development methodologies: Waterfall, Agile/Scrum, DevOps/DevSecOps, Iterative, Hybrid
- All development types: Internal, outsourced, hybrid, open-source integration
- All security tools: SAST, SCA, secret scanning, IDE security plugins
- Developer training and security champion programs
- Code review processes
- Security defect management

**Out of Scope**:
- Detailed secure coding standards (covered by ISMS-POL-A.8.28 Secure Coding - referenced herein)
- Security testing methodologies (covered by ISMS-POL-A.8.25-26-29-S4 Security Testing - A.8.29)
- Application security requirements (covered by ISMS-POL-A.8.25-26-29-S2 - A.8.26)

**Primary Stakeholders**: Development Teams, DevOps, Application Security Team, QA  
**Implementation Evidence**: ISMS-IMP-A.8.25-26-29-S2, Assessment Workbook 2 (SDLC Security Activities Compliance)

---

## 2. SDLC Security Integration Framework

### 2.1 Security-Integrated SDLC Overview

Security **SHALL** be integrated into every phase of the SDLC, regardless of methodology:

```
┌──────────────────────────────────────────────────────────────────┐
│            Security-Integrated SDLC (Universal)                  │
└──────────────────────────────────────────────────────────────────┘

Phase 1: Requirements
├─ Security requirements specification (A.8.26)
├─ Threat modeling initiation
├─ Compliance requirements identification
└─ Security acceptance criteria

Phase 2: Design  
├─ Security architecture review
├─ Threat model completion
├─ Security design patterns
└─ Third-party component security assessment

Phase 3: Development
├─ Secure coding (A.8.28)
├─ Code review (peer + security)
├─ SAST/SCA/secret scanning
└─ IDE security plugins

Phase 4: Testing
├─ Security testing (A.8.29 - SAST, DAST, SCA, pentest)
├─ Security acceptance testing
└─ Vulnerability remediation

Phase 5: Deployment
├─ Security configuration review
├─ Deployment security checklist
├─ Production security validation
└─ Security sign-off

Phase 6: Maintenance
├─ Security patch management
├─ Vulnerability remediation
├─ Periodic security reassessment
└─ Decommissioning security
```

### 2.2 SDLC Methodology Adaptations

This framework is **methodology-agnostic** and adapts to different SDLC approaches:

#### 2.2.1 Waterfall / V-Model

**Security Integration**:
- **Sequential phases** with security gates at phase transitions
- **Formal security reviews** at each gate (requirements review, design review, code review, testing review)
- **Security sign-off** required before proceeding to next phase
- **Documentation-heavy**: Security requirements specs, architecture docs, test plans

**Security Gates**:
- Requirements → Design: Security requirements approved, threat model initiated
- Design → Development: Security architecture approved, threat model complete
- Development → Testing: Code review complete, SAST findings resolved
- Testing → Deployment: Security testing complete, vulnerabilities remediated
- Deployment → Maintenance: Production security validated, monitoring configured

#### 2.2.2 Agile / Scrum

**Security Integration**:
- **Security in every sprint**: Security stories in backlog, security tasks in sprint planning
- **Security champion** embedded in each team
- **Definition of Done** includes security criteria (code review, SAST scan, no high vulnerabilities)
- **Sprint security retrospectives**: Review security issues, improve practices

**Security Activities**:
- **Sprint 0 / Project Kickoff**: Security requirements, threat modeling, security architecture
- **Each Sprint**:
  - Security stories prioritized in backlog
  - Code review for all code (peer + security-focused)
  - Automated security scanning (SAST/SCA in CI/CD)
  - Security testing for features
  - Vulnerability remediation
- **Release / Sprint Review**: Security acceptance testing, security sign-off

#### 2.2.3 DevOps / DevSecOps

**Security Integration**:
- **Security automation** in CI/CD pipeline (shift-left security)
- **Continuous security testing**: SAST/DAST/SCA automated in every build
- **Policy-as-Code**: Security policies enforced programmatically
- **Infrastructure-as-Code (IaC) security**: Terraform/CloudFormation scanning
- **Container security**: Image scanning, runtime protection

**CI/CD Security Pipeline**:
```
Code Commit
    ↓
Secret Scanning (pre-commit hooks)
    ↓
SAST (static analysis on every commit)
    ↓
SCA (dependency scanning)
    ↓
Build
    ↓
Container Image Scanning (if containerized)
    ↓
DAST (dynamic testing in staging)
    ↓
Security Tests (automated security test suites)
    ↓
Security Gate (pass/fail criteria)
    ↓
Deployment (if security gate passed)
    ↓
Runtime Monitoring (production security)
```

**Security Automation Requirements**:
- **Automated security checks** must not significantly slow down CI/CD (optimize for speed)
- **Break the build** for critical/high vulnerabilities (configurable thresholds)
- **Non-blocking warnings** for medium/low vulnerabilities (track, don't block)
- **Fast feedback**: Security results visible to developers within minutes

#### 2.2.4 Iterative / Incremental

**Security Integration**:
- **Security in first iteration**: Establish security foundation (authentication, authorization, logging)
- **Security refinement** in subsequent iterations
- **Incremental security testing**: Test security as features are added
- **Security checkpoints** at iteration boundaries

### 2.3 Security Activities Matrix by SDLC Phase

The following matrix defines **mandatory security activities** for each SDLC phase, applicable to all methodologies:

| SDLC Phase | Security Activity | Responsibility | Deliverable |
|------------|-------------------|----------------|-------------|
| **Requirements** | Security requirements specification | Product Manager + Security Architect | Security requirements document |
| | Threat modeling initiation | Security Architect | Initial threat model |
| | Compliance requirements | Legal/Compliance + Security | Regulatory requirements list |
| **Design** | Security architecture review | Security Architect | Architecture review report |
| | Threat model completion | Security Architect + Developers | Threat model document |
| | Security design patterns | Developers + Security | Design documentation |
| | Third-party component assessment | Developers + Security | Component security assessment |
| **Development** | Secure coding (A.8.28) | Developers | Source code |
| | Code review (peer) | Developers | Code review records |
| | Code review (security-focused) | Security Champion / Security Team | Security review records |
| | SAST scanning | Automated (CI/CD) | SAST scan results |
| | SCA scanning | Automated (CI/CD) | SCA scan results |
| | Secret scanning | Automated (CI/CD) | Secret scan results |
| **Testing** | Security testing (A.8.29) | QA + Security | Test results |
| | SAST/DAST/SCA | Security + QA | Vulnerability reports |
| | Penetration testing | Security / External | Pentest report |
| | Security acceptance testing | QA + Security | Test evidence |
| **Deployment** | Security configuration review | DevOps + Security | Configuration checklist |
| | Deployment checklist | DevOps | Deployment evidence |
| | Production security validation | Security | Validation report |
| **Maintenance** | Security patch management | DevOps + Developers | Patch records |
| | Vulnerability remediation | Developers + Security | Remediation tracking |
| | Periodic security reassessment | Security | Reassessment reports |

---

## 3. Security Activities by SDLC Phase (Detailed Requirements)

### 3.1 Phase 1: Requirements - Security Requirements

**Activities** (covered in detail by ISMS-POL-A.8.25-26-29-S2):
- Identify security requirements based on risk classification
- Conduct initial threat modeling
- Document security acceptance criteria
- Identify compliance requirements (GDPR, PCI DSS, etc.)

**Outputs**:
- Security requirements specification (see A.8.26)
- Initial threat model
- Security user stories / requirements (for Agile)
- Compliance requirements checklist

**Security Sign-Off**: Security Architect approves security requirements before design phase

### 3.2 Phase 2: Design - Security Architecture

**Activities**:

Organizations **SHALL**:

1. **Conduct security architecture review**:
   - Validate security requirements are addressed in design
   - Review trust boundaries and data flows
   - Evaluate authentication and authorization architecture
   - Review cryptography design (key management, encryption)
   - Assess third-party component security
   - Validate network architecture and segmentation
   - Review logging and monitoring design

2. **Complete threat modeling**:
   - Identify attack scenarios and threat actors
   - Map threats to security controls
   - Assess residual risks
   - Document risk treatment decisions
   - Update threat model throughout development

3. **Apply security design patterns**:
   - **Authentication patterns**: OAuth 2.0, OpenID Connect, SAML, multi-factor authentication
   - **Authorization patterns**: RBAC, ABAC, policy-based access control
   - **Data protection patterns**: Encryption at rest/in transit, tokenization, data masking
   - **API security patterns**: API gateway, rate limiting, OAuth scopes
   - **Resilience patterns**: Circuit breaker, bulkhead, timeout, retry with backoff

4. **Assess third-party components**:
   - Identify all third-party libraries, frameworks, APIs
   - Review component security (CVE history, vendor responsiveness)
   - Verify license compliance
   - Document component inventory
   - Plan for component updates and patching

**Outputs**:
- Security architecture diagrams
- Threat model document (complete)
- Security design decisions document
- Third-party component security assessment
- Architecture review report

**Security Sign-Off**: Security Architect approves security design before development phase

### 3.3 Phase 3: Development - Secure Coding and Review

This is the **core security integration phase** where security controls are implemented.

#### 3.3.1 Secure Coding Requirements

**Organizations SHALL**:

1. **Apply secure coding standards**:
   - Follow organizational secure coding standards (ISMS-POL-A.8.28)
   - Implement security requirements from A.8.26
   - Use security design patterns from architecture phase
   - Apply OWASP Top 10 prevention techniques

2. **Use secure development tools**:
   - IDE security plugins (real-time security feedback)
   - Linting tools with security rules
   - Dependency management tools
   - Code analysis tools

**Detailed secure coding standards are defined in ISMS-POL-A.8.28 (Secure Coding Policy).**

#### 3.3.2 Code Review Requirements

**Mandatory Code Review**:

All code **SHALL** undergo code review before merging to main/production branches:

**Peer Code Review** (for all code):
- **Minimum**: One peer reviewer (developer on same team)
- **Focus**: Code quality, logic, maintainability, basic security
- **Timing**: Before merge (pull request / merge request review)
- **Tool**: Code review platform (GitHub PR, GitLab MR, Bitbucket PR, Gerrit)
- **Criteria**: Reviewer must approve before merge

**Security-Focused Code Review** (for high-risk code):

High-risk code **SHALL** undergo additional security-focused review:

**High-Risk Code Includes**:
- Authentication and authorization logic
- Cryptography implementation
- Input validation and sanitization
- Database queries (especially dynamic SQL)
- File upload/download handling
- API endpoints (especially public-facing)
- Privilege escalation functions
- Financial transaction processing
- Personal data processing
- Security configuration code

**Security Review Requirements**:
- **Reviewer**: Security Champion (trained developer) or Security Team member
- **Focus**: Security vulnerabilities, secure coding compliance, threat model alignment
- **Checklist**: Use security code review checklist (based on OWASP, CWE, organizational standards)
- **Timing**: Before merge for critical code, or within sprint for high-risk features
- **Documentation**: Security review findings logged and tracked

**Code Review Checklist** (minimum items):
- ✅ Input validation on all user input
- ✅ Output encoding for all output contexts
- ✅ Parameterized queries for database access (no SQL concatenation)
- ✅ Authentication and authorization checks present
- ✅ Sensitive data encrypted (if applicable)
- ✅ Error handling does not expose sensitive information
- ✅ Logging of security events (authentication, authorization, failures)
- ✅ No hardcoded secrets (passwords, API keys, encryption keys)
- ✅ Third-party libraries are approved and current versions
- ✅ Security requirements from A.8.26 implemented

#### 3.3.3 Security Tools Integration

Organizations **SHALL** deploy security tools in the development environment:

**Static Application Security Testing (SAST)**:
- **Purpose**: Analyze source code for security vulnerabilities
- **Deployment**: Integrated into CI/CD pipeline (automated on every commit/build)
- **Coverage**: All code repositories
- **Tools** (examples): SonarQube, Checkmarx, Fortify, Snyk Code, Semgrep, CodeQL
- **Configuration**:
  - Enable security-focused rule sets
  - Configure for programming language and framework
  - Set severity thresholds (critical, high, medium, low)
  - Define break-build criteria (e.g., no critical/high findings)
- **Results Triage**:
  - Developers review findings
  - Classify as true positive, false positive, or acceptable risk
  - Remediate true positives before merge (or document exception)
  - Suppress false positives with justification
- **Frequency**: Per commit (fast scans) or daily (comprehensive scans)

**Software Composition Analysis (SCA)**:
- **Purpose**: Identify vulnerable dependencies and license compliance
- **Deployment**: Integrated into CI/CD pipeline
- **Coverage**: All projects with third-party dependencies
- **Tools** (examples): Snyk, Dependabot, WhiteSource, Black Duck, OWASP Dependency-Check
- **Configuration**:
  - Monitor all dependency manifests (pom.xml, package.json, requirements.txt, Gemfile, etc.)
  - Alert on vulnerabilities (CVEs)
  - Check license compliance
  - Recommend updates and patches
- **Remediation**:
  - Update dependencies to non-vulnerable versions
  - Apply patches if available
  - Accept risk if no patch available (with justification)
  - Remove dependency if obsolete or too risky
- **Frequency**: Continuous (daily checks for new vulnerabilities)

**Secret Scanning**:
- **Purpose**: Detect hardcoded secrets (passwords, API keys, tokens, certificates)
- **Deployment**: Pre-commit hooks + CI/CD pipeline + periodic repository scans
- **Coverage**: All code repositories, configuration files, IaC templates
- **Tools** (examples): git-secrets, TruffleHog, GitHub Secret Scanning, GitLab Secret Detection, Snyk
- **Configuration**:
  - Detect common secret patterns (AWS keys, API tokens, passwords)
  - Custom patterns for organizational secrets
  - Prevent commits with secrets (pre-commit hooks)
  - Alert security team on secret detection
- **Remediation**:
  - **Immediately rotate exposed secrets**
  - Remove secrets from code history (BFG Repo-Cleaner, git-filter-repo)
  - Move secrets to secure secret management (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault)
  - Educate developer on secret management

**IDE Security Plugins**:
- **Purpose**: Real-time security feedback to developers during coding
- **Deployment**: Recommended/required IDE plugins for developers
- **Coverage**: Developers' local development environments
- **Tools** (examples):
  - IntelliJ IDEA: SonarLint, Snyk plugin
  - Visual Studio Code: SonarLint, Snyk, ESLint (security rules)
  - Eclipse: FindBugs/SpotBugs, SonarLint
- **Benefits**:
  - Immediate feedback (fix vulnerabilities while coding)
  - Education (developers learn secure coding)
  - Reduced findings in CI/CD (catch issues earlier)

**Tool Integration Requirements**:
- **Automated**: Tools run automatically in CI/CD (no manual execution)
- **Fast feedback**: Results available within build/commit cycle (minutes, not hours)
- **Developer-friendly**: Results presented clearly with remediation guidance
- **Centralized reporting**: Aggregate results in dashboard for visibility
- **Break-build policies**: Define when builds fail due to security findings

#### 3.3.4 Secure Development Environment

Organizations **SHALL** secure the development environment:

**Source Code Repository Security**:
- **Access control**: Least privilege access to repositories (see ISMS-POL-A.8.4)
- **Branch protection**: Require code review before merge to main/production branches
- **Audit logging**: Log all repository access and changes
- **Encryption**: Repositories encrypted at rest and in transit (HTTPS/SSH)
- **Backup**: Regular backups with encryption

**Developer Workstation Security**:
- **Operating system**: Hardened and patched OS
- **Endpoint protection**: Antivirus, EDR (Endpoint Detection and Response)
- **Disk encryption**: Full disk encryption (BitLocker, FileVault, LUKS)
- **Screen lock**: Auto-lock after inactivity
- **VPN**: Remote developers use VPN to access corporate resources
- **No shared accounts**: Each developer has unique credentials

**Build and CI/CD Security**:
- **Access control**: Restrict access to CI/CD systems (least privilege)
- **Secret management**: Secrets stored in secret management systems (not in code or CI/CD configs)
- **Immutable builds**: Build artifacts are immutable and signed
- **Audit logging**: Log all build and deployment activities
- **Isolated environments**: Build agents isolated from production

**Development/Test Data Security**:
- **No production data in dev/test**: Use synthetic or anonymized data
- **Data masking**: Mask sensitive data if production-like data needed
- **Access control**: Restrict access to test data
- **Data retention**: Delete test data after testing complete

---

## 4. Security Tools - Detailed Requirements

### 4.1 SAST (Static Application Security Testing)

**Tool Selection Criteria**:
- **Language support**: Supports organization's programming languages
- **Framework support**: Understands frameworks (Spring, Django, .NET, React, etc.)
- **Accuracy**: Low false positive rate
- **Integration**: Integrates with CI/CD, IDEs, code repositories
- **Reporting**: Clear findings with remediation guidance
- **Scalability**: Handles organization's codebase size

**Implementation Requirements**:

Organizations **SHALL**:
- **Deploy SAST** in CI/CD pipeline for all projects
- **Configure rules** appropriate to language and framework
- **Set thresholds** for build failures:
  - **High Risk Applications**: No critical or high vulnerabilities in production builds
  - **Medium Risk Applications**: No critical vulnerabilities in production builds
  - **Low Risk Applications**: No critical vulnerabilities (high vulnerabilities documented)
- **Triage findings** promptly:
  - Critical: Immediate remediation (same day)
  - High: Remediation within sprint or release cycle
  - Medium/Low: Remediation prioritized in backlog
- **Track metrics**:
  - Number of findings by severity
  - Remediation time by severity
  - False positive rate
  - Code coverage

**SAST Scanning Frequency**:
- **Per commit/PR**: Fast incremental scans (detect new issues)
- **Nightly**: Full scan of entire codebase
- **Pre-release**: Comprehensive scan before production deployment

### 4.2 SCA (Software Composition Analysis)

**Tool Selection Criteria**:
- **Vulnerability database**: Up-to-date CVE database
- **Package manager support**: npm, Maven, pip, NuGet, RubyGems, etc.
- **License detection**: Identify open-source licenses
- **Remediation guidance**: Suggest version updates or patches
- **Integration**: CI/CD, repositories, IDEs

**Implementation Requirements**:

Organizations **SHALL**:
- **Deploy SCA** in CI/CD pipeline for all projects with dependencies
- **Monitor continuously** for new vulnerabilities in existing dependencies
- **Set remediation SLAs**:
  - **Critical vulnerabilities**: 7 days
  - **High vulnerabilities**: 30 days
  - **Medium vulnerabilities**: 90 days
  - **Low vulnerabilities**: Next release or 180 days
- **Approve dependencies**: Maintain approved library/framework list
- **License compliance**: Ensure open-source licenses are compatible with organizational use
- **Track metrics**:
  - Number of vulnerable dependencies
  - Remediation time by severity
  - License compliance violations

**SCA Scanning Frequency**:
- **Per commit/build**: Check new dependencies
- **Daily**: Monitor existing dependencies for new CVEs
- **Continuous**: Real-time alerts for critical new vulnerabilities

### 4.3 Secret Scanning

**Tool Selection Criteria**:
- **Pattern detection**: Detects common secret patterns (API keys, passwords, certificates)
- **Custom patterns**: Supports organizational secret patterns
- **Pre-commit integration**: Prevents commits with secrets
- **Historical scanning**: Scans repository history for exposed secrets

**Implementation Requirements**:

Organizations **SHALL**:
- **Deploy pre-commit hooks** to prevent committing secrets
- **Scan repositories** periodically for historical secrets
- **Alert security team** immediately when secrets detected
- **Rotate exposed secrets** immediately:
  - Invalidate compromised credentials
  - Generate new credentials
  - Update applications with new credentials
  - Investigate potential unauthorized access
- **Remove secrets from history** (git history rewriting)
- **Educate developers** on secret management best practices

**Remediation Process for Exposed Secrets**:
1. **Detect**: Secret scanning tool alerts
2. **Validate**: Confirm secret is real (not false positive)
3. **Rotate**: Immediately invalidate and rotate secret
4. **Remove**: Remove secret from code and git history
5. **Investigate**: Check for unauthorized use of exposed secret
6. **Secure**: Move secret to secret management system
7. **Educate**: Train developer on proper secret handling

### 4.4 IDE Security Plugins

**Deployment**:
- **Recommended** for all developers (install security plugins in IDEs)
- **Mandatory** for security-critical projects
- **Documentation**: Provide setup guides for IDE security plugin installation

**Benefits**:
- **Shift-left**: Catch vulnerabilities during coding (earliest possible point)
- **Education**: Developers learn secure coding in real-time
- **Productivity**: Fix issues immediately (no context switching)

---

## 5. Developer Security Training

### 5.1 Security Training Requirements

**Organizations SHALL provide security training** to all developers:

**Initial Security Training** (for new developers):
- **Timing**: Within first month of employment or starting development work
- **Duration**: Minimum 4 hours
- **Content**:
  - Secure coding principles (OWASP Top 10, CWE Top 25)
  - Organizational secure coding standards (A.8.28)
  - Security tools usage (SAST, SCA, IDE plugins)
  - Code review expectations
  - Threat modeling basics
  - Security incident reporting
- **Delivery**: Online course, in-person workshop, or blended
- **Verification**: Completion certificate or assessment

**Annual Security Refresher Training**:
- **Timing**: Annually
- **Duration**: Minimum 2 hours
- **Content**:
  - Updates to secure coding standards
  - New vulnerability classes and attack techniques
  - Lessons learned from security incidents
  - Tool updates and new features
  - Regulatory changes (GDPR, PCI DSS updates)
- **Delivery**: Online course, lunch-and-learn, workshop
- **Verification**: Completion tracking

**Role-Specific Training**:

**Security Champions** (additional training):
- **Security architecture** principles
- **Threat modeling** methodologies
- **Advanced secure coding** techniques
- **Security testing** (SAST/DAST/SCA interpretation)
- **Security code review** techniques
- **Incident response** for developers

**Third-Party Developers / Contractors**:
- **Mandatory** security training before code access
- **Same standards** as internal developers
- **Verification** required (training certificate)

### 5.2 Security Awareness Activities

Organizations **SHOULD** conduct ongoing security awareness:

**Activities**:
- **Security newsletters**: Monthly security tips, vulnerability alerts, best practices
- **Lunch-and-learn sessions**: Security topics, demos, case studies
- **CTF (Capture the Flag)**: Security challenges for hands-on learning
- **Bug bounty / vulnerability disclosure**: Internal programs for finding vulnerabilities
- **Security retrospectives**: Team reviews of security issues and improvements
- **Gamification**: Security badges, leaderboards, recognition for secure code

### 5.3 Security Champion Program

Organizations **SHOULD** establish a **Security Champion Program**:

**Security Champions**:
- **Embedded** in each development team (1 per team or squad)
- **Volunteers** with security interest (not forced assignment)
- **Training**: Enhanced security training (see role-specific training)
- **Responsibilities**:
  - Security advocate within team
  - Security code review for high-risk code
  - Security tool triage and remediation support
  - Threat modeling facilitation
  - Security knowledge sharing (teach team)
  - Liaison with security team
- **Time allocation**: 10-20% of work time for security champion activities
- **Recognition**: Visibility, career development, certifications, compensation consideration

**Benefits**:
- **Scales security expertise** across organization
- **Faster security decisions** (champions can answer questions without security team bottleneck)
- **Better security culture** (security becomes team responsibility, not just security team)
- **Developer career growth** (security champion experience valuable for advancement)

---

## 6. Security Defect Management

### 6.1 Security Defect Lifecycle

Security defects **SHALL** be tracked systematically:

```
┌─────────────────────────────────────────────────────────────┐
│           Security Defect Lifecycle                          │
└─────────────────────────────────────────────────────────────┘

1. Detection
   ├─ SAST/DAST/SCA findings
   ├─ Code review findings
   ├─ Penetration test findings
   ├─ Security researcher reports
   └─ Production incident investigations

2. Triage
   ├─ Validate (true positive vs false positive)
   ├─ Severity assessment (Critical, High, Medium, Low)
   ├─ Exploitability assessment
   └─ Business impact assessment

3. Prioritization
   ├─ Remediation SLA based on severity
   ├─ Business criticality
   ├─ Exposure (internet-facing vs internal)
   └─ Regulatory requirements

4. Remediation
   ├─ Assign to developer
   ├─ Develop fix
   ├─ Code review
   ├─ Testing (functional + security)
   └─ Deploy fix

5. Verification
   ├─ Retest to confirm fix
   ├─ Update security tools (suppress if fixed)
   └─ Close defect

6. Tracking
   ├─ SLA compliance monitoring
   ├─ Trend analysis
   └─ Lessons learned
```

### 6.2 Security Defect Severity Classification

Organizations **SHALL** classify security defects by severity:

**Critical Severity**:
- **Definition**: Vulnerability allows unauthenticated remote code execution, complete system compromise, or unauthorized access to highly sensitive data
- **Examples**: SQL injection in public-facing application, authentication bypass, remote code execution, exposed encryption keys
- **Remediation SLA**: 7 days maximum (ideally 24-48 hours for production vulnerabilities)
- **Response**: Immediate triage, hotfix deployment, security incident if exploited

**High Severity**:
- **Definition**: Vulnerability allows authenticated remote code execution, privilege escalation, or access to sensitive data
- **Examples**: Privilege escalation, stored XSS, insecure deserialization, SSRF, IDOR with sensitive data exposure
- **Remediation SLA**: 30 days maximum
- **Response**: Prioritized remediation, included in next release

**Medium Severity**:
- **Definition**: Vulnerability requires user interaction or special conditions to exploit, limited impact
- **Examples**: Reflected XSS, CSRF, information disclosure (limited), insecure direct object reference (non-sensitive data)
- **Remediation SLA**: 90 days maximum
- **Response**: Scheduled remediation in regular release cycle

**Low Severity**:
- **Definition**: Vulnerability with minimal security impact or requires unlikely conditions
- **Examples**: Missing security headers (best practice), verbose error messages, rate limiting issues
- **Remediation SLA**: 180 days or next major release
- **Response**: Backlog item, addressed when convenient

**Severity Modifiers** (adjust severity based on context):
- **Internet-facing**: Increase severity (critical → critical, high → critical, medium → high)
- **High-risk application**: Increase severity
- **Internal-only**: Decrease severity (medium → low in some cases)
- **Exploit availability**: Increase severity if public exploit exists
- **Compensating controls**: May decrease severity if strong mitigating controls present

### 6.3 Security Defect Tracking

Organizations **SHALL**:

**Track security defects** in defect tracking system:
- **Unique identifier**: Defect ID
- **Severity**: Critical, High, Medium, Low
- **Status**: Open, In Progress, Fixed, Verified, Closed
- **Source**: SAST, DAST, SCA, Code Review, Pentest, etc.
- **Application**: Which application is affected
- **Description**: Vulnerability details
- **Remediation**: Fix description and timeline
- **SLA**: Target remediation date based on severity
- **Owner**: Developer assigned to fix

**Report security metrics**:
- **Open vulnerabilities** by severity
- **Overdue vulnerabilities** (past SLA)
- **Mean time to remediate (MTTR)** by severity
- **Vulnerability trends** (increasing/decreasing over time)
- **Vulnerability sources** (SAST vs DAST vs code review)

**Escalation**:
- **SLA breach**: Escalate to development manager
- **Repeated SLA breaches**: Escalate to engineering director
- **Critical vulnerabilities not fixed**: Escalate to CISO and executive management

### 6.4 Security Technical Debt

Organizations **SHALL** manage security technical debt:

**Definition**: Security issues that are known but not yet addressed (deferred remediation, known limitations, legacy vulnerabilities)

**Security Technical Debt Includes**:
- Vulnerabilities with accepted risk (temporarily)
- Legacy code with security issues (planned for refactoring)
- Third-party components with no available patches
- Security requirements not yet implemented (phased rollout)

**Management Requirements**:
- **Document** all security technical debt in risk register
- **Review periodically** (at least quarterly)
- **Assess risk changes** (does the risk increase over time?)
- **Plan remediation** (when will technical debt be addressed?)
- **Track trends** (is technical debt increasing or decreasing?)
- **Executive visibility**: Report high security technical debt to management

**Acceptable Security Technical Debt**:
- **Temporary** with clear remediation plan
- **Risk accepted** by appropriate authority (see Section 7.3)
- **Compensating controls** in place to mitigate risk
- **Monitored** for changes in risk level

**Unacceptable Security Technical Debt**:
- **Critical vulnerabilities** with no remediation plan
- **Indefinite deferral** without risk acceptance
- **Accumulating** faster than remediation
- **No compensating controls** or monitoring

---

## 7. Code Review Process

### 7.1 Code Review Objectives

Code review serves multiple purposes:
- **Quality assurance**: Ensure code correctness and maintainability
- **Knowledge sharing**: Spread knowledge across team
- **Mentoring**: Senior developers guide junior developers
- **Security**: Identify security vulnerabilities

### 7.2 Peer Code Review

**Mandatory for all code**:

Organizations **SHALL** require peer code review:
- **Minimum one peer reviewer** before merging code
- **Reviewer qualifications**: Proficient in programming language and codebase
- **Review scope**: Code correctness, logic, maintainability, basic security
- **Review tool**: Pull request / merge request platform (GitHub, GitLab, Bitbucket, Gerrit)
- **Approval required**: Reviewer must approve before merge
- **Author cannot self-merge**: Code author cannot merge their own code without review

**Peer Review Checklist** (minimum):
- ✅ Code is readable and maintainable
- ✅ Logic is correct and handles edge cases
- ✅ Tests are included and passing
- ✅ Documentation is updated (if applicable)
- ✅ No obvious security issues (hardcoded secrets, SQL concatenation, etc.)
- ✅ Code follows organizational coding standards

### 7.3 Security-Focused Code Review

**Required for high-risk code** (see Section 3.3.2):

Organizations **SHALL** require security-focused review for high-risk code:
- **Reviewer**: Security Champion or Security Team member
- **Reviewer qualifications**: Security training, secure coding expertise
- **Review scope**: Security vulnerabilities, secure coding compliance, threat model alignment
- **Review tool**: Same as peer review (pull request comments)
- **Security checklist**: Use comprehensive security code review checklist

**Security Code Review Checklist** (comprehensive):

**Input Validation**:
- ✅ All user input is validated server-side
- ✅ Whitelist validation used where possible
- ✅ Input validation occurs before use in sensitive operations
- ✅ File upload validation includes content-type verification
- ✅ File size limits enforced

**Injection Prevention**:
- ✅ SQL queries use parameterized statements (no string concatenation)
- ✅ No dynamic SQL construction with user input
- ✅ Command execution uses parameterized APIs (no shell execution with user input)
- ✅ LDAP queries use parameterized methods
- ✅ XML parsing disables external entity processing (XXE prevention)

**Output Encoding**:
- ✅ Output encoding applied based on context (HTML, JavaScript, URL, CSS)
- ✅ Template engine auto-escaping enabled
- ✅ Content Security Policy (CSP) headers configured

**Authentication**:
- ✅ Authentication required for protected resources
- ✅ Password hashing uses strong algorithms (bcrypt, scrypt, Argon2)
- ✅ Passwords never logged or displayed
- ✅ Account lockout implemented for failed login attempts
- ✅ Multi-factor authentication implemented (for high-risk apps)

**Session Management**:
- ✅ Session tokens are cryptographically random
- ✅ Session tokens not exposed in URLs
- ✅ Secure cookie flags set (Secure, HttpOnly, SameSite)
- ✅ Session timeout implemented
- ✅ Session invalidated on logout
- ✅ Session regenerated after login (session fixation prevention)

**Authorization**:
- ✅ Authorization checks performed server-side for all operations
- ✅ Vertical access control enforced (prevent privilege escalation)
- ✅ Horizontal access control enforced (users can't access other users' data)
- ✅ Default deny (require explicit permissions)
- ✅ Sensitive operations require additional authentication (step-up auth)

**Cryptography**:
- ✅ Strong encryption algorithms used (AES-256, ChaCha20)
- ✅ TLS 1.2 or higher configured
- ✅ No hardcoded encryption keys
- ✅ Cryptographically secure random number generators used
- ✅ No use of deprecated algorithms (MD5, SHA-1, DES, RC4)

**Error Handling**:
- ✅ Error messages don't expose sensitive information
- ✅ Stack traces not returned to users in production
- ✅ Detailed errors logged server-side (not exposed to users)
- ✅ Custom error pages configured
- ✅ Global exception handling implemented

**Logging**:
- ✅ Security events logged (authentication, authorization, input validation failures)
- ✅ Sensitive data not logged (passwords, session tokens, credit cards)
- ✅ Logs include timestamp, user, action, result
- ✅ Logs protected from unauthorized access
- ✅ Logs forwarded to centralized logging system

**Secrets Management**:
- ✅ No hardcoded passwords, API keys, or credentials
- ✅ Secrets retrieved from secret management system
- ✅ Secrets not committed to version control
- ✅ Secrets not logged or displayed

**Third-Party Components**:
- ✅ Third-party libraries are approved versions
- ✅ No known vulnerabilities in dependencies (SCA scan passed)
- ✅ Dependencies are up-to-date
- ✅ Licenses are compatible

**Threat Model Alignment**:
- ✅ Identified threats are mitigated
- ✅ Security requirements from A.8.26 are implemented
- ✅ Security design decisions are followed

---

## 8. Security in Different SDLC Phases (Expanded Guidance)

### 8.1 Requirements Phase - Security Requirements

**Security Activities** (see ISMS-POL-A.8.25-26-29-S2 for details):
- Identify security requirements based on application risk classification
- Document functional security requirements (authentication, authorization, encryption, logging)
- Document non-functional security requirements (fail secure, defense in depth)
- Document data protection requirements (encryption, retention, privacy)
- Initiate threat modeling
- Identify regulatory compliance requirements
- Create security user stories (for Agile) or requirements specifications (for Waterfall)

**Security Deliverables**:
- Security requirements document
- Initial threat model
- Security acceptance criteria
- Compliance requirements checklist

### 8.2 Design Phase - Security Architecture

**Security Activities**:
- Complete threat modeling (identify threats, assess risks, define mitigations)
- Conduct security architecture review
- Apply security design patterns
- Document security mechanisms (authentication, authorization, encryption, logging)
- Assess third-party components
- Design secure APIs
- Design secure data flows
- Plan security testing approach

**Security Deliverables**:
- Threat model document (complete)
- Security architecture diagrams
- Security design document
- Third-party component assessment
- Architecture review report

### 8.3 Development Phase - Secure Coding

**Security Activities**:
- Implement security requirements
- Follow secure coding standards (A.8.28)
- Conduct peer code review
- Conduct security-focused code review (for high-risk code)
- Run SAST scans (automated in CI/CD)
- Run SCA scans (dependency scanning)
- Run secret scanning
- Use IDE security plugins
- Remediate security findings
- Document security implementation

**Security Deliverables**:
- Source code (secure)
- Code review records
- SAST/SCA scan results
- Remediation records

### 8.4 Testing Phase - Security Testing

**Security Activities** (see ISMS-POL-A.8.25-26-29-S4 for details):
- Execute security test cases
- Run SAST/DAST/SCA scans
- Conduct penetration testing (for high-risk applications)
- Perform security acceptance testing
- Verify security requirements implementation
- Remediate identified vulnerabilities
- Retest after remediation

**Security Deliverables**:
- Security test results
- SAST/DAST/SCA reports
- Penetration test report
- Vulnerability remediation records
- Security acceptance evidence

### 8.5 Deployment Phase - Production Security

**Security Activities**:
- Review production security configuration
- Validate security controls in production environment
- Complete deployment security checklist
- Configure security monitoring and alerting
- Verify encryption (TLS certificates, data-at-rest)
- Validate access controls
- Enable security logging
- Conduct production security validation
- Obtain security sign-off before go-live

**Security Deliverables**:
- Deployment security checklist (complete)
- Production security configuration
- Security validation report
- Security sign-off approval

**Deployment Security Checklist** (minimum):
- ✅ TLS/HTTPS configured and validated
- ✅ Strong cipher suites configured
- ✅ Security headers configured (HSTS, CSP, X-Frame-Options, etc.)
- ✅ Database encryption configured (if required)
- ✅ Access controls configured and tested
- ✅ Secrets deployed via secret management system (not hardcoded)
- ✅ Security logging and monitoring enabled
- ✅ Alerts configured for security events
- ✅ Backup and recovery tested (with encryption)
- ✅ Security patches applied to infrastructure
- ✅ Unnecessary services disabled
- ✅ Default credentials changed
- ✅ Security testing complete (SAST/DAST/SCA/pentest)
- ✅ Vulnerability remediation complete (or risk accepted)

### 8.6 Maintenance Phase - Ongoing Security

**Security Activities**:
- Monitor security alerts and incidents
- Apply security patches promptly
- Remediate newly discovered vulnerabilities
- Conduct periodic security reassessments (annual)
- Update threat model as application evolves
- Respond to security incidents
- Decommission securely when application retired

**Security Deliverables**:
- Patch management records
- Vulnerability remediation tracking
- Security incident records
- Periodic security assessment reports

**Patch Management**:
- **Critical security patches**: Apply within 7 days
- **High security patches**: Apply within 30 days
- **Medium security patches**: Apply within 90 days
- **Low security patches**: Apply with regular updates

**Decommissioning Security**:
When application is retired:
- ✅ Revoke all access credentials
- ✅ Securely delete sensitive data
- ✅ Remove application from production
- ✅ Archive code and documentation securely
- ✅ Update network configurations (remove firewall rules, DNS entries)
- ✅ Decommission infrastructure securely

---

## 9. Compliance and Audit Evidence

### 9.1 Evidence Collection

Organizations **SHALL** collect evidence of SDLC security activities:

**Evidence Types**:
- **SDLC documentation**: Documented security activities per phase
- **Security tool outputs**: SAST/SCA/secret scanning reports
- **Code review records**: Pull request approvals, review comments
- **Training records**: Developer security training completion
- **Defect tracking**: Security defect lifecycle and remediation
- **Metrics**: Security metrics dashboard and trends

### 9.2 Assessment Workbook

SDLC security compliance is assessed via **Assessment Workbook 2: SDLC Security Activities Compliance**, which tracks:
- Security activities by SDLC phase (planned vs executed)
- Secure coding standard compliance
- Code review completion rate
- Security tool deployment status
- Developer training completion
- Security defect remediation SLA compliance
- Compliance scoring per application

---

## 10. Exceptions and Risk Acceptance

### 10.1 Exception Process

SDLC security requirements may be waived through formal exception process (see Section 13 of ISMS-POL-A.8.25-26-29-S2 for detailed exception process).

**Common Exceptions**:
- Security tool not deployed (legacy system, technical limitations)
- Code review not performed (urgent hotfix, small change)
- Security training delayed (new hire, backlog)

**Approval Authority**:
- Low/Medium exceptions: Application Security Lead
- High exceptions: CISO
- Critical exceptions: CISO + Executive Management

### 10.2 Risk Acceptance

Exceptions constitute risk acceptance decisions and must be:
- Documented in risk register
- Reviewed periodically (at least annually)
- Include compensating controls
- Include remediation plan (if temporary exception)

---

## Conclusion

This Secure Development Lifecycle Framework establishes systematic security integration throughout the SDLC for [Organization]. By implementing these requirements:

✅ **Security is integrated** into every SDLC phase (not an afterthought)  
✅ **Developers are empowered** with training and tools to write secure code  
✅ **Vulnerabilities are detected early** through automated tools and code review  
✅ **Security defects are tracked** and remediated systematically  
✅ **Evidence is collected** for compliance and continuous improvement  

**Next Steps**:
1. Review Section 4 (Security Testing - A.8.29) for detailed testing requirements
2. Review Section 5 (Assessment & Evidence Framework) for compliance tracking
3. Consult ISMS-IMP-A.8.25-26-29-S2 for detailed SDLC integration procedures
4. Deploy Assessment Workbook 2 for SDLC activity tracking

---

**Document End**

*This document establishes secure development lifecycle integration (A.8.25). Security testing (A.8.29) is covered in the next section.*
