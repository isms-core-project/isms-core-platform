# ISMS-POL-A.8.25-26-29-S4
## Security Testing Framework (A.8.29)

**Document ID**: ISMS-POL-A.8.25-26-29-S4  
**Title**: Security Testing Framework - Security Testing in Development and Acceptance (A.8.29)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead / QA Manager | Initial security testing framework |

**Review Cycle**: Annual (or upon significant testing methodology or tool changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead
- Testing Owner: QA Manager / Test Automation Lead
- Development Review: Development Manager

**Distribution**: Security team, QA team, development teams, DevOps  
**Related Documents**: 
- ISMS-POL-A.8.25-26-29-S1 (Executive Summary)
- ISMS-POL-A.8.25-26-29-S2 (Security Requirements - A.8.26)
- ISMS-POL-A.8.25-26-29-S3 (Secure Development Lifecycle - A.8.25)
- ISMS-IMP-A.8.25-26-29-S4 (Security Testing Implementation Guide)
- ISO/IEC 27001:2022 A.8.29

---

## 1. Purpose and Scope

### 1.1 Purpose

This document establishes **mandatory requirements** for security testing throughout the development lifecycle and before production deployment, implementing ISO/IEC 27001:2022 Control A.8.29 (Security Testing in Development and Acceptance).

**Control Text (ISO/IEC 27001:2022 A.8.29)**:
> *Security testing processes should be defined and implemented in the development life cycle.*

### 1.2 Objectives

- **Verify** security requirements are correctly implemented (validation against A.8.26)
- **Detect** security vulnerabilities before production deployment
- **Test** applications using multiple methodologies for comprehensive coverage
- **Remediate** identified vulnerabilities within defined SLAs
- **Prevent** vulnerable code from reaching production environments
- **Measure** security testing coverage and effectiveness

### 1.3 Scope

**In Scope**:
- All security testing types: SAST, DAST, SCA, IAST, penetration testing, security acceptance testing
- All applications regardless of risk classification (testing depth varies by risk)
- Testing in development, staging, and pre-production environments
- Automated and manual security testing
- Vulnerability remediation workflows
- Security testing metrics and reporting

**Out of Scope**:
- Production vulnerability scanning (covered by A.8.8 Management of Technical Vulnerabilities)
- Functional testing (non-security QA testing)
- Performance testing (unless security-related, e.g., DoS resilience)
- Security requirements specification (covered by A.8.26)
- Secure development practices (covered by A.8.25)

**Primary Stakeholders**: Application Security Team, QA Team, Development Teams, DevOps  
**Implementation Evidence**: ISMS-IMP-A.8.25-26-29-S4, Assessment Workbooks 3 & 4 (Security Testing Results, Vulnerability Remediation)

---

## 2. Security Testing Strategy

### 2.1 Testing Philosophy

Security testing **SHALL** follow these principles:

**Shift-Left Testing**:
- Test security **as early as possible** in SDLC (reduce remediation costs)
- Automated testing in CI/CD pipeline (continuous security validation)
- Developer-friendly feedback (fast, actionable results)

**Defense in Depth Testing**:
- **Multiple testing types** for comprehensive coverage
- SAST (code analysis) + DAST (runtime analysis) + SCA (dependency analysis) + penetration testing (human expertise)
- Each testing type finds different vulnerability classes

**Risk-Based Testing**:
- **Testing depth** based on application risk classification (High/Medium/Low)
- **Testing frequency** based on risk and change velocity
- **Resource allocation** prioritized to high-risk applications

**Continuous Testing**:
- **Automated testing** in CI/CD (every commit, every build)
- **Periodic testing** (scheduled scans, annual penetration testing)
- **Event-driven testing** (major releases, significant changes)

### 2.2 Security Testing Types

Organizations **SHALL** implement multiple security testing types:

```
┌────────────────────────────────────────────────────────────────┐
│            Security Testing Comprehensive Coverage             │
└────────────────────────────────────────────────────────────────┘

┌─────────────────────┬─────────────────────┬──────────────────┐
│   SAST              │   DAST              │   SCA            │
│   (White Box)       │   (Black Box)       │   (Composition)  │
├─────────────────────┼─────────────────────┼──────────────────┤
│ • Source code       │ • Running app       │ • Dependencies   │
│ • Before compile    │ • Runtime behavior  │ • Vulnerabilities│
│ • Fast feedback     │ • Real exploits     │ • Licenses       │
│ • CI/CD integrated  │ • Web apps/APIs     │ • Supply chain   │
│                     │                     │                  │
│ Finds:              │ Finds:              │ Finds:           │
│ • Injection flaws   │ • Config issues     │ • Known CVEs     │
│ • Hardcoded secrets │ • Auth/session bugs │ • Outdated libs  │
│ • Crypto misuse     │ • Business logic    │ • License issues │
└─────────────────────┴─────────────────────┴──────────────────┘
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
      ┌──────────┐    ┌──────────┐    ┌──────────┐
      │   IAST   │    │ Pentest  │    │ Security │
      │ (Hybrid) │    │ (Manual) │    │ Accept.  │
      └──────────┘    └──────────┘    └──────────┘
           │               │                │
           └───────────────┴────────────────┘
                           │
                           ▼
                  Comprehensive Security
                     Validation
```

### 2.3 Testing Coverage Requirements

**High Risk Applications SHALL**:
- **All testing types**: SAST + DAST + SCA + Penetration Testing + Security Acceptance Testing
- **Automated testing**: SAST/SCA in CI/CD (every commit or daily)
- **DAST**: Weekly or per deployment
- **Penetration testing**: Annually minimum (or per major release)
- **Coverage target**: 80%+ code coverage for SAST, 100% API endpoint coverage for DAST
- **Pass criteria**: Zero critical/high vulnerabilities in production

**Medium Risk Applications SHALL**:
- **Core testing types**: SAST + SCA + DAST (recommended) + Security Acceptance Testing
- **Automated testing**: SAST/SCA in CI/CD
- **DAST**: Per release or monthly
- **Penetration testing**: Recommended (every 2 years or per major release)
- **Coverage target**: 60%+ code coverage for SAST
- **Pass criteria**: Zero critical vulnerabilities in production

**Low Risk Applications SHOULD**:
- **Basic testing**: SAST + SCA (minimum)
- **Automated testing**: SAST/SCA in CI/CD (if feasible)
- **DAST**: Optional (recommended for internet-facing)
- **Penetration testing**: Optional
- **Pass criteria**: Critical vulnerabilities addressed

### 2.4 Testing Frequency

| Testing Type | High Risk | Medium Risk | Low Risk |
|--------------|-----------|-------------|----------|
| **SAST** | Per commit or daily | Per commit or daily | Daily or weekly |
| **SCA** | Daily (continuous monitoring) | Daily | Weekly |
| **Secret Scanning** | Per commit (pre-commit hooks) | Per commit | Per commit |
| **DAST** | Weekly or per deployment | Per release | Optional |
| **IAST** | Continuous (if deployed) | Continuous (if deployed) | N/A |
| **Penetration Testing** | Annual + per major release | Every 2 years or major release | Optional |
| **Security Acceptance** | Every release | Every release | Major releases |

---

## 3. Static Application Security Testing (SAST)

### 3.1 SAST Overview

**Purpose**: Analyze source code for security vulnerabilities without executing the code

**Benefits**:
- **Early detection**: Find vulnerabilities during development (shift-left)
- **Fast feedback**: Results in minutes (developer-friendly)
- **Broad coverage**: Analyze entire codebase, including dead code paths
- **Compliance**: Demonstrate secure development practices

**Limitations**:
- **False positives**: May report non-exploitable issues (requires triage)
- **Context limitations**: Cannot detect runtime vulnerabilities (use DAST for these)
- **Configuration dependent**: Requires proper tool configuration for language/framework

### 3.2 SAST Implementation Requirements

Organizations **SHALL**:

**Deploy SAST tools**:
- **Tool selection**: Choose tools supporting organization's programming languages and frameworks
- **CI/CD integration**: Automate SAST scans in build pipeline
- **IDE integration**: Provide IDE plugins for real-time developer feedback
- **Coverage**: Scan all code repositories

**Configure SAST appropriately**:
- **Enable security rule sets**: OWASP Top 10, CWE Top 25, language-specific rules
- **Tune for accuracy**: Balance false positives vs. false negatives
- **Set severity levels**: Critical, High, Medium, Low (aligned with organizational classification)
- **Configure language/framework**: Ensure tool understands frameworks (Spring, Django, .NET, React, etc.)

**Define scan triggers**:
- **Per commit**: Incremental scans on changed code (fast feedback)
- **Daily builds**: Full codebase scans (comprehensive analysis)
- **Pre-release**: Mandatory full scan before production deployment
- **On-demand**: Developers can trigger scans manually

**Set quality gates**:
- **Break build** for critical/high vulnerabilities (configurable threshold)
- **Warn** for medium/low vulnerabilities (don't block, but track)
- **Require remediation** before merge to main/production branch

### 3.3 SAST Scan Results Management

Organizations **SHALL**:

**Triage SAST findings**:
1. **Classify**: True positive, false positive, or acceptable risk
2. **Prioritize**: Based on severity, exploitability, and business impact
3. **Assign**: Assign to developer for remediation
4. **Track**: Track findings in defect tracking system

**Remediate SAST findings**:
- **Critical findings**: Remediate immediately (same day if possible)
- **High findings**: Remediate within 30 days
- **Medium findings**: Remediate within 90 days
- **Low findings**: Remediate within 180 days or next major release

**Suppress false positives**:
- **Document justification**: Why finding is false positive
- **Require approval**: Security Champion or Security Team approval
- **Review periodically**: Validate suppressions remain valid (annually)

**Track SAST metrics**:
- **Findings by severity**: Count of critical/high/medium/low findings
- **Findings by category**: Injection, XSS, authentication, crypto, etc.
- **True positive rate**: % of findings that are real vulnerabilities
- **Mean time to remediate (MTTR)**: Average time to fix vulnerabilities
- **Scan coverage**: % of codebase scanned
- **Trend analysis**: Are vulnerabilities increasing or decreasing over time?

### 3.4 SAST Tool Examples

Organizations may select SAST tools appropriate to their needs. Examples include (not exhaustive):

**Commercial Tools**:
- Checkmarx
- Fortify (Micro Focus)
- Veracode
- Snyk Code
- CodeQL (GitHub)

**Open-Source Tools**:
- SonarQube (Community Edition + commercial)
- Semgrep
- Bandit (Python)
- Brakeman (Ruby)
- ESLint with security plugins (JavaScript)
- SpotBugs / FindBugs (Java)

**Selection criteria**: Language support, framework support, accuracy, CI/CD integration, reporting, cost

---

## 4. Dynamic Application Security Testing (DAST)

### 4.1 DAST Overview

**Purpose**: Test running applications for security vulnerabilities by simulating attacks

**Benefits**:
- **Runtime vulnerabilities**: Find issues only visible when application is running (configuration, environment, business logic)
- **Real exploits**: Validate exploitability of vulnerabilities
- **Platform-agnostic**: Works regardless of programming language (tests HTTP/APIs)
- **Production-like**: Tests in realistic environment

**Limitations**:
- **Later in SDLC**: Requires running application (cannot test during development)
- **Coverage limitations**: Only tests exposed interfaces (cannot reach dead code)
- **Slower**: Scans take longer than SAST (minutes to hours)
- **Environment dependent**: Results depend on test environment configuration

### 4.2 DAST Implementation Requirements

Organizations **SHALL**:

**Deploy DAST tools**:
- **Tool selection**: Choose tools supporting web applications and APIs
- **Staging integration**: Deploy in staging/pre-production environments
- **Authenticated scanning**: Configure credentials for authenticated testing
- **Coverage**: Scan all web applications and APIs

**Configure DAST appropriately**:
- **Scan profiles**: Configure for web app vs. API testing
- **Authentication**: Provide test credentials for authenticated scans
- **Scan scope**: Define URLs/endpoints to scan (avoid production, third-party sites)
- **Rate limiting**: Configure scan speed to avoid overwhelming application
- **Attack vectors**: Enable OWASP Top 10 tests, API security tests

**Define scan triggers**:
- **Per deployment**: Automated DAST scan when application deployed to staging
- **Weekly/monthly**: Scheduled scans of stable applications
- **Pre-release**: Mandatory scan before production deployment
- **On-demand**: Security team can trigger scans for investigations

**Set quality gates**:
- **Block deployment** for critical vulnerabilities
- **Review required** for high vulnerabilities before production
- **Track** medium/low vulnerabilities for future remediation

### 4.3 DAST Authenticated vs. Unauthenticated Scanning

Organizations **SHALL** perform both authenticated and unauthenticated scans:

**Unauthenticated Scanning**:
- **Purpose**: Test attack surface visible to anonymous users
- **Use cases**: Public-facing websites, login pages, password reset
- **Vulnerabilities found**: Authentication bypass, information disclosure, injection in public endpoints

**Authenticated Scanning**:
- **Purpose**: Test attack surface visible to logged-in users
- **Use cases**: Internal applications, authenticated APIs, user portals
- **Credentials**: Test user accounts (not production admin accounts)
- **Vulnerabilities found**: Authorization bypass, privilege escalation, IDOR, business logic flaws

**Multi-role scanning** (for complex applications):
- **Multiple test accounts**: Test with different user roles (user, manager, admin)
- **Purpose**: Find horizontal and vertical privilege escalation vulnerabilities

### 4.4 DAST Scan Results Management

Organizations **SHALL**:

**Validate DAST findings**:
- **Confirm exploitability**: Manually validate critical/high findings
- **Check false positives**: DAST can report false positives (e.g., WAF blocks, rate limiting)
- **Document findings**: Screenshot evidence, request/response data

**Remediate DAST findings**:
- Same SLAs as SAST: Critical (7 days), High (30 days), Medium (90 days), Low (180 days)
- **Retest after remediation**: Run targeted DAST scan to verify fix

**Track DAST metrics**:
- **Findings by severity**
- **Findings by category**: Authentication, authorization, injection, XSS, CSRF, etc.
- **API coverage**: % of API endpoints tested
- **Scan duration**: Time to complete scan
- **Trend analysis**

### 4.5 DAST Tool Examples

**Commercial Tools**:
- Burp Suite Professional / Enterprise
- Acunetix
- AppScan (HCL)
- Netsparker / Invicti
- Veracode DAST

**Open-Source Tools**:
- OWASP ZAP (Zed Attack Proxy)
- Nikto (web server scanner)
- Arachni

**Selection criteria**: Web app vs. API support, authentication support, CI/CD integration, accuracy, reporting

---

## 5. Software Composition Analysis (SCA)

### 5.1 SCA Overview

**Purpose**: Identify security vulnerabilities and license compliance issues in third-party dependencies

**Benefits**:
- **Supply chain security**: Detect vulnerable dependencies before use
- **Continuous monitoring**: Alert when new CVEs affect existing dependencies
- **License compliance**: Identify license conflicts (GPL, MIT, Apache, proprietary)
- **Automated remediation**: Suggest version updates or patches

**Scope**:
- Open-source libraries and frameworks
- Third-party commercial components
- Transitive dependencies (dependencies of dependencies)

### 5.2 SCA Implementation Requirements

Organizations **SHALL**:

**Deploy SCA tools**:
- **Tool selection**: Choose tools supporting package managers (npm, Maven, pip, NuGet, Bundler, Go modules, etc.)
- **CI/CD integration**: Automated dependency scanning in build pipeline
- **Continuous monitoring**: Monitor dependencies for new CVEs daily
- **Coverage**: Scan all projects with third-party dependencies

**Configure SCA appropriately**:
- **Vulnerability databases**: Use multiple sources (NVD, vendor advisories, GitHub Security Advisories)
- **Severity thresholds**: Define acceptable vulnerability levels
- **License policies**: Define allowed/forbidden licenses
- **Update recommendations**: Enable automated fix suggestions

**Define scan triggers**:
- **Per build**: Scan dependencies when added or updated
- **Daily monitoring**: Check for new CVEs affecting existing dependencies
- **Continuous**: Real-time alerts for critical vulnerabilities
- **Pre-release**: Validate no vulnerable dependencies in production build

**Set quality gates**:
- **Block builds** with critical vulnerabilities in dependencies
- **Warn** for high vulnerabilities (require review/remediation plan)
- **Track** medium/low vulnerabilities for scheduled updates

### 5.3 Dependency Vulnerability Remediation

Organizations **SHALL**:

**Remediate vulnerable dependencies**:

**Preferred remediation**: Update to non-vulnerable version
- **Check for updates**: Identify latest secure version
- **Test compatibility**: Verify application works with updated dependency
- **Apply update**: Update dependency version in manifest (package.json, pom.xml, requirements.txt, etc.)
- **Verify fix**: Re-scan to confirm vulnerability resolved

**Alternative remediations** (if update not available):
- **Apply patch**: Use vendor-provided patch or backport fix
- **Replace dependency**: Use alternative library with same functionality
- **Accept risk**: Document risk acceptance with compensating controls and CISO approval
- **Remove dependency**: If dependency not essential, remove it

**Dependency remediation SLAs**:
- **Critical vulnerabilities**: 7 days (or immediate if actively exploited)
- **High vulnerabilities**: 30 days
- **Medium vulnerabilities**: 90 days
- **Low vulnerabilities**: 180 days or next major release

### 5.4 License Compliance

Organizations **SHALL** manage open-source license compliance:

**Identify licenses**: SCA tools detect licenses in dependencies

**Define license policy**:
- **Approved licenses**: MIT, Apache 2.0, BSD, ISC (permissive licenses)
- **Restricted licenses**: GPL, LGPL, AGPL (copyleft licenses - require legal review)
- **Forbidden licenses**: Licenses incompatible with organizational use

**License compliance actions**:
- **Approved licenses**: Use freely
- **Restricted licenses**: Legal review required before use
- **Forbidden licenses**: Do not use (find alternative or obtain commercial license)

### 5.5 SCA Tool Examples

**Commercial Tools**:
- Snyk
- WhiteSource (Mend)
- Black Duck (Synopsys)
- Sonatype Nexus Lifecycle

**Open-Source / Free Tools**:
- OWASP Dependency-Check
- Dependabot (GitHub)
- Renovate Bot
- npm audit / pip-audit / bundler-audit (language-specific)

**Selection criteria**: Package manager support, vulnerability database, license detection, CI/CD integration, automated fix suggestions

---

## 6. Interactive Application Security Testing (IAST)

### 6.1 IAST Overview

**Purpose**: Hybrid approach combining SAST and DAST - analyze application security during runtime using instrumentation

**Benefits**:
- **Accurate**: Lower false positive rate (validates exploitability at runtime)
- **Comprehensive**: Combines code analysis with runtime behavior
- **Fast**: Faster than DAST (results during testing, not separate scan)
- **Developer-friendly**: Integrates with development/testing workflow

**Deployment**:
- **Instrumentation agent**: Deployed in application runtime (JVM agent, .NET profiler, etc.)
- **Test execution**: Runs during functional testing, QA testing, or staging
- **Not for production**: IAST agents have performance overhead

### 6.2 IAST Implementation (Optional)

Organizations **MAY** implement IAST:

**IAST is recommended for**:
- High-risk applications requiring maximum accuracy
- Applications with complex business logic (DAST may miss these)
- Organizations with mature testing practices (IAST leverages existing functional tests)

**IAST deployment**:
- **Agent installation**: Install IAST agent in staging/test environment
- **Test execution**: Run functional tests or QA tests (IAST observes)
- **Results analysis**: Review IAST findings (typically more accurate than DAST)
- **Remediation**: Follow same SLAs as SAST/DAST

**IAST Tool Examples**:
- Contrast Security
- Hdiv Detection (Hdiv Security)
- Seeker (Synopsys)

---

## 7. Penetration Testing

### 7.1 Penetration Testing Overview

**Purpose**: Simulate real-world attacks by security experts to identify vulnerabilities automated tools miss

**Benefits**:
- **Human expertise**: Security experts think like attackers
- **Business logic flaws**: Find vulnerabilities automated tools cannot detect
- **Comprehensive**: Combines automated scanning with manual exploitation
- **Validation**: Confirm exploitability of vulnerabilities
- **Compliance**: Many regulations require penetration testing (PCI DSS, HIPAA, DORA)

**Types**:
- **Black box**: No knowledge of application internals (simulate external attacker)
- **Gray box**: Limited knowledge (e.g., user account)
- **White box**: Full knowledge including source code, architecture

### 7.2 Penetration Testing Requirements

**High Risk Applications SHALL**:
- Conduct penetration testing **annually minimum**
- Conduct penetration testing **before major releases** (new features, architecture changes)
- **Scope**: All internet-facing components, APIs, authentication/authorization, sensitive data handling
- **Tester qualifications**: Professional penetration testers (OSCP, CEH, GPEN, or equivalent experience)
- **Methodology**: OWASP Testing Guide, PTES (Penetration Testing Execution Standard), or similar

**Medium Risk Applications SHOULD**:
- Conduct penetration testing **every 2 years**
- Conduct penetration testing **before major releases** (recommended)
- **Scope**: Internet-facing components, authentication/authorization
- **Tester qualifications**: Professional penetration testers or experienced security team

**Low Risk Applications MAY**:
- Conduct penetration testing **as needed** (optional)

### 7.3 Penetration Testing Process

Organizations **SHALL** follow structured penetration testing process:

**Phase 1: Planning and Scoping**:
- **Define scope**: Applications, systems, networks in scope (and out of scope)
- **Define rules of engagement**: Testing windows, acceptable testing methods, contacts
- **Obtain approvals**: Management approval, legal review, service provider notifications (if cloud-hosted)
- **Provide documentation**: Application documentation, architecture diagrams, test accounts

**Phase 2: Reconnaissance and Scanning**:
- **Information gathering**: OSINT, subdomain enumeration, technology fingerprinting
- **Automated scanning**: Vulnerability scanning, port scanning
- **Manual analysis**: Application mapping, functionality enumeration

**Phase 3: Exploitation and Validation**:
- **Vulnerability exploitation**: Attempt to exploit identified vulnerabilities
- **Privilege escalation**: Test for privilege escalation opportunities
- **Lateral movement**: Test for lateral movement possibilities (if network in scope)
- **Data access**: Validate unauthorized data access (without exfiltrating real data)

**Phase 4: Reporting**:
- **Executive summary**: High-level findings, business impact
- **Technical findings**: Detailed vulnerability descriptions, steps to reproduce, evidence (screenshots, logs)
- **Severity ratings**: Critical, High, Medium, Low (with CVSS scores)
- **Remediation guidance**: Specific recommendations for each finding
- **Risk assessment**: Overall security posture assessment

**Phase 5: Remediation and Retesting**:
- **Remediate findings**: Follow remediation SLAs based on severity
- **Retest**: Penetration testers retest fixed vulnerabilities (included in engagement or separate)
- **Close findings**: Mark verified fixes as closed

### 7.4 Penetration Testing Methodology

Organizations **SHOULD** require testers to follow established methodologies:

**OWASP Testing Guide**:
- Comprehensive web application testing methodology
- Covers OWASP Top 10 and beyond
- Information gathering, configuration testing, authentication, authorization, session management, input validation, business logic, etc.

**PTES (Penetration Testing Execution Standard)**:
- Structured approach: Pre-engagement, intelligence gathering, threat modeling, vulnerability analysis, exploitation, post-exploitation, reporting

**NIST SP 800-115 (Technical Guide to Information Security Testing)**:
- Government standard for security testing
- Testing techniques, tools, metrics

### 7.5 Penetration Testing Deliverables

Penetration testing **SHALL** produce:
- **Penetration test report**: Executive summary + detailed technical findings
- **Findings prioritization**: Critical/High/Medium/Low severity
- **Evidence**: Screenshots, logs, proof-of-concept exploits (if safe)
- **Remediation recommendations**: Specific, actionable guidance
- **Retest report**: Verification of remediated vulnerabilities (if retesting performed)

### 7.6 Internal vs. External Penetration Testing

**External penetration testing** (third-party):
- **Benefits**: Independent assessment, fresh perspective, specialized expertise
- **Required**: High-risk applications (annual minimum), compliance requirements (PCI DSS, HIPAA)
- **Cost**: Higher cost but professional quality

**Internal penetration testing** (security team):
- **Benefits**: Lower cost, knowledge of internal architecture, continuous testing
- **Suitable**: Medium/low-risk applications, preliminary testing before external pentest
- **Limitation**: Potential bias, limited fresh perspective

**Recommendation**: High-risk applications should use external penetration testers; internal testing can supplement

---

## 8. Security Acceptance Testing

### 8.1 Security Acceptance Testing Overview

**Purpose**: Verify security requirements are implemented before production deployment

**Integration with SDLC**:
- **Part of acceptance testing**: Security acceptance criteria defined in requirements (A.8.26)
- **Gate before production**: Security sign-off required for production deployment
- **Evidence collection**: Demonstrate security requirements are met

### 8.2 Security Acceptance Testing Requirements

Organizations **SHALL** conduct security acceptance testing:

**Security test cases**:
- **Derived from security requirements**: Each security requirement (A.8.26) has corresponding test case
- **Traceability**: Link test cases to requirements (Requirements Traceability Matrix)
- **Positive and negative tests**: Test both correct behavior and attack scenarios

**Test execution**:
- **Automated tests**: Security test automation (API tests, UI tests with security focus)
- **Manual tests**: Manual validation of security controls (authentication flows, authorization, encryption)
- **Regression tests**: Re-test security after changes

**Security acceptance criteria** (examples):
- ✅ Authentication requires valid credentials (positive test)
- ✅ Invalid credentials are rejected (negative test)
- ✅ Multi-factor authentication is enforced for high-risk operations
- ✅ Authorization prevents unauthorized access (horizontal and vertical privilege escalation)
- ✅ Sensitive data is encrypted in transit (HTTPS/TLS)
- ✅ Sensitive data is encrypted at rest (if required)
- ✅ Input validation rejects malicious input (SQL injection, XSS, command injection)
- ✅ Security logging captures authentication, authorization, and security events
- ✅ Error messages do not expose sensitive information
- ✅ Session timeout is enforced
- ✅ No critical/high vulnerabilities in SAST/DAST/SCA scans
- ✅ Penetration testing findings remediated (if penetration test conducted)

**Security sign-off**:
- **Approval**: Application Security Lead or Security Team approves for production
- **Documentation**: Security acceptance test results, security testing evidence
- **Conditions**: All critical/high vulnerabilities remediated, security requirements met

### 8.3 Security Regression Testing

Organizations **SHALL** perform security regression testing:

**Purpose**: Ensure security is not degraded by changes (new features, bug fixes, refactoring)

**Scope**: Re-run security tests after changes:
- **Automated security tests**: Run in CI/CD pipeline
- **SAST/SCA scans**: Run automatically on every build
- **DAST scans**: Run on deployments to staging
- **Manual tests**: Re-test security-critical areas affected by changes

---

## 9. Vulnerability Remediation Workflows

### 9.1 Vulnerability Lifecycle

Vulnerabilities **SHALL** be managed through structured lifecycle:

```
Detection → Validation → Prioritization → Remediation → Verification → Closure
     ↑                                                                      │
     └──────────────────────────────────────────────────────────────────────┘
                            (Continuous monitoring)
```

### 9.2 Vulnerability Remediation Process

Organizations **SHALL** follow remediation process:

**1. Detection**:
- Vulnerability identified by SAST, DAST, SCA, penetration test, or security researcher
- Automatically logged in defect tracking system

**2. Validation**:
- **Verify vulnerability is real** (true positive vs. false positive)
- **Assess exploitability**: Can it actually be exploited?
- **Assess business impact**: What data/functionality is at risk?

**3. Prioritization**:
- **Assign severity**: Critical, High, Medium, Low (based on CVSS, exploitability, business impact)
- **Apply SLA**: Remediation deadline based on severity
- **Assign owner**: Developer responsible for fixing

**4. Remediation**:
- **Develop fix**: Code changes to address vulnerability
- **Code review**: Review fix for correctness and security
- **Test fix**: Functional and security testing of fix
- **Deploy fix**: Deploy to production (or schedule for next release)

**5. Verification**:
- **Retest**: Re-run security test to confirm fix (SAST rescan, DAST rescan, manual validation)
- **Validate**: Ensure vulnerability is resolved and no regression introduced

**6. Closure**:
- **Close ticket**: Mark vulnerability as resolved in defect tracking
- **Update documentation**: Update security test cases, threat model if needed
- **Lessons learned**: Analyze root cause, update standards/training if needed

### 9.3 Remediation SLAs

Organizations **SHALL** remediate vulnerabilities within defined SLAs:

| Severity | SLA | Response |
|----------|-----|----------|
| **Critical** | 7 days | Immediate triage, hotfix deployment, executive notification if in production |
| **High** | 30 days | Prioritized remediation, next release or hotfix |
| **Medium** | 90 days | Scheduled remediation, regular release cycle |
| **Low** | 180 days | Backlog item, next major release |

**SLA Modifiers**:
- **Production vulnerabilities**: Shorter SLAs (critical: 24-48 hours, high: 7 days)
- **Internet-facing**: Increase priority
- **Active exploitation**: Immediate remediation (critical severity regardless of CVSS)
- **Compensating controls**: May extend SLA if strong mitigations in place (requires approval)

**SLA Breach Escalation**:
- **First breach**: Notification to development manager
- **Second breach**: Escalation to engineering director and CISO
- **Repeated breaches**: Executive escalation, resource allocation review

### 9.4 Remediation Tracking

Organizations **SHALL** track remediation metrics:

**Metrics**:
- **Open vulnerabilities by severity**: Count of unresolved vulnerabilities
- **Overdue vulnerabilities**: Count of vulnerabilities past SLA
- **Mean Time to Remediate (MTTR)**: Average time to fix vulnerabilities by severity
- **Remediation rate**: Vulnerabilities closed per month
- **Backlog growth**: Is backlog increasing or decreasing?
- **SLA compliance**: % of vulnerabilities remediated within SLA

**Reporting**:
- **Weekly**: Security team reviews open vulnerabilities, overdue items
- **Monthly**: Report to engineering management (trends, blockers, resource needs)
- **Quarterly**: Report to executive management and board (overall security posture)

---

## 10. Security Testing in CI/CD Pipeline

### 10.1 CI/CD Security Integration

Organizations **SHALL** integrate security testing into CI/CD pipelines:

**Security Pipeline Stages**:

```
Code Commit
    ↓
Pre-Commit Hooks (Secret Scanning)
    ↓
Build
    ↓
SAST (Static Analysis) - Fast incremental scan
    ↓
SCA (Dependency Scanning) - Check for vulnerable deps
    ↓
Unit Tests (including security tests)
    ↓
Build Artifacts
    ↓
Deploy to Staging
    ↓
DAST (Dynamic Analysis) - Scan staging deployment
    ↓
Integration Tests (including security tests)
    ↓
Security Gate (Pass/Fail based on findings)
    ↓
Deploy to Production (if security gate passed)
    ↓
Runtime Monitoring (production security)
```

### 10.2 Security Gates

Organizations **SHALL** define security gates in CI/CD:

**Break Build Criteria** (High Risk Applications):
- Critical SAST findings
- Critical SCA findings (vulnerable dependencies)
- Secrets detected (hardcoded passwords, API keys)
- High DAST findings (for staging deployments)

**Warning Criteria** (don't block, but notify):
- High SAST findings
- High SCA findings
- Medium DAST findings

**Configuration**:
- **Thresholds are configurable** per application risk level
- **False positive suppression** allowed with approval
- **Emergency bypass** process for critical hotfixes (requires CISO approval, followed by immediate remediation)

### 10.3 Pipeline Performance

Organizations **SHOULD** optimize security testing for speed:

**Fast Feedback**:
- SAST incremental scans: < 5 minutes (scan only changed code)
- SCA scans: < 2 minutes (check dependency manifest)
- Secret scanning: < 1 minute (pre-commit hooks)

**Comprehensive Scans**:
- Full SAST scans: Nightly (outside development hours)
- DAST scans: Per deployment to staging (can take hours)

**Balance**: Fast incremental checks in main pipeline, comprehensive checks in scheduled scans

---

## 11. Compliance and Audit Evidence

### 11.1 Evidence Collection

Organizations **SHALL** collect evidence of security testing:

**Testing Evidence**:
- **SAST reports**: Scan results, findings, remediation records
- **DAST reports**: Scan results, findings, remediation records
- **SCA reports**: Dependency vulnerabilities, license compliance
- **Penetration test reports**: External pentest reports, retests
- **Security acceptance test results**: Test execution evidence, sign-off approvals

**Metrics Evidence**:
- **Testing coverage**: % of applications tested, % of code covered
- **Vulnerability trends**: Open vulnerabilities over time
- **Remediation compliance**: SLA compliance metrics
- **Testing frequency**: Evidence of regular testing

### 11.2 Assessment Workbooks

Security testing compliance is assessed via:

**Assessment Workbook 3: Security Testing Results Compliance**:
- SAST scan results by application
- DAST scan results by application
- SCA scan results (vulnerable dependencies)
- Penetration testing results
- Security testing coverage metrics

**Assessment Workbook 4: Vulnerability Remediation Tracking**:
- Open vulnerabilities by severity and age
- Remediation SLA compliance
- Vulnerability trends over time
- Security technical debt

---

## Conclusion

This Security Testing Framework establishes comprehensive security testing throughout the development lifecycle for [Organization]. By implementing these requirements:

✅ **Vulnerabilities are detected early** through automated SAST/SCA in CI/CD  
✅ **Multiple testing types** provide defense-in-depth validation  
✅ **Human expertise** complements automation through penetration testing  
✅ **Remediation is systematic** with clear SLAs and tracking  
✅ **Production deployments** are protected by security gates  
✅ **Evidence is collected** for compliance and continuous improvement  

**Next Steps**:
1. Review Section 5 (Assessment & Evidence Framework) for compliance tracking
2. Consult ISMS-IMP-A.8.25-26-29-S4 for detailed security testing implementation
3. Deploy Assessment Workbooks 3 & 4 for testing and remediation tracking

---

**Document End**

*This document establishes security testing requirements (A.8.29). Assessment and evidence framework (comprehensive compliance tracking) is covered in the next section.*
