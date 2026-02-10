<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.30.3-UG:framework:UG:a.8.30.3 -->
**ISMS-IMP-A.8.30.3-UG - Security Testing and Acceptance**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.3-UG |
| **Document Title** | Security Testing and Acceptance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

This section provides step-by-step guidance for completing the Security Testing and Acceptance workbook. Follow this guide to ensure comprehensive security validation of outsourced development deliverables before acceptance.

---

## Assessment Overview

### Purpose

The Security Testing and Acceptance workbook tracks security testing activities, manages software composition analysis, and documents acceptance criteria verification for all outsourced development deliverables. It ensures that code delivered by external vendors meets security requirements before integration into production systems.

ISO/IEC 27001:2022 Control A.8.30 states:

> *"The organisation should direct, monitor and review the activities related to outsourced system development."*

Security testing and formal acceptance are critical monitoring activities that verify vendors have met security requirements specified in contracts and policies.

### Scope and Applicability

**This workbook applies to:**

| Deliverable Type | Testing Required | Acceptance Level |
|------------------|------------------|------------------|
| Custom applications | Full testing suite | Formal acceptance |
| Application modules | Appropriate testing | Formal acceptance |
| API components | Full testing suite | Formal acceptance |
| Libraries/SDKs | SCA mandatory, code review | Formal acceptance |
| Configuration changes | Code review, targeted testing | Documented review |
| Database scripts | Code review, integrity testing | Formal acceptance |
| Infrastructure as Code | Security scan, review | Formal acceptance |
| Documentation only | Review for completeness | Sign-off |

**This workbook does NOT apply to:**

- Internally developed code (covered by A.8.25-29)
- Third-party commercial software (use procurement process)
- SaaS platform configuration (no code delivery)
- Maintenance patches from software vendors

### Business Context

**Why Security Testing Matters:**

Outsourced code introduces unique risks that require verification before acceptance:

1. **Unknown Quality**: Vendor development practices may differ from internal standards
2. **Hidden Vulnerabilities**: Code may contain security flaws not visible in functional testing
3. **Dependency Risks**: Third-party components introduce supply chain vulnerabilities
4. **Compliance Gaps**: Code may not meet regulatory requirements
5. **Intellectual Property Issues**: Open source licenses may create legal exposure
6. **Backdoors/Malware**: Deliberate or accidental inclusion of malicious code

**Testing Philosophy:**

| Principle | Implementation |
|-----------|----------------|
| Trust but verify | All vendor code undergoes independent security testing |
| Defence in depth | Multiple testing types complement each other |
| Shift left | Security testing during development, not just at delivery |
| Risk-based | Testing depth proportional to criticality |
| Evidence-driven | All findings documented and tracked |

### Assessment Outputs

Upon completion, this workbook provides:

| Output | Purpose | Audience |
|--------|---------|----------|
| Deliverable Inventory | Track all outsourced code deliveries | Project Managers, IT Security |
| Code Review Records | Document review findings | Development Teams, IT Security |
| Security Test Results | Vulnerability findings by test type | IT Security, Vendors |
| SBOM Registry | Third-party component tracking | IT Security, Legal |
| Acceptance Records | Formal sign-off evidence | Management, Auditors |
| Compliance Evidence | ISO 27001 audit documentation | External Auditors |

---

## Prerequisites

### Required Inputs

Before beginning security testing, ensure you have:

| Input | Source | Required For |
|-------|--------|--------------|
| Deliverable package | Vendor | All testing |
| Source code access | Vendor | Code review, SAST |
| Build instructions | Vendor | Reproducible builds |
| Deployment package | Vendor | DAST testing |
| Test environment | IT Operations | DAST, penetration testing |
| SBOM from vendor | Vendor | SCA verification |
| Contract security requirements | Legal | Acceptance criteria |
| Project classification | Project Manager | Testing depth determination |

### Required Approvals Before Testing

| Approval Type | Approver | Purpose |
|---------------|----------|---------|
| Test environment availability | IT Operations | Confirms environment ready |
| Test authorisation (pen testing) | System Owner | Authorises security testing |
| Budget approval (external testing) | Finance | If external pentest required |
| Vendor notification | Project Manager | Inform vendor testing will occur |

### Required Knowledge

Testing personnel should understand:

- Secure development lifecycle (SDLC) concepts
- OWASP Top 10 and common vulnerability classes
- Security testing tools (SAST, DAST, SCA)
- Code review techniques
- Vulnerability classification (CVSS)
- Acceptance criteria interpretation
- Evidence documentation requirements

### Tool Requirements

| Tool Category | Example Tools | Purpose |
|---------------|---------------|---------|
| SAST | SonarQube, Checkmarx, Fortify, Snyk Code | Static code analysis |
| DAST | OWASP ZAP, Burp Suite Pro, Acunetix | Dynamic application testing |
| SCA | Snyk, WhiteSource, Dependabot, OWASP Dependency-Check | Component analysis |
| Secret Scanner | GitLeaks, TruffleHog, GitHub Secret Scanning | Credential detection |
| Code Review | GitHub, GitLab, Bitbucket, Gerrit | Peer review platform |
| Test Management | Excel, Jira, TestRail | Finding tracking |

---

## Completion Walkthrough

### Sheet 1: Deliverable Inventory – Completion Guide

**Purpose**: Maintain a comprehensive list of all deliverables from outsourced development with their testing and acceptance status.

**Step-by-Step Completion:**

**Step 1: Generate Deliverable ID**

Create a unique identifier using the format `DEL-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | DEL- | DEL- |
| Sequential Number | 4 digits | 0178 |
| Full ID | DEL-XXXX | DEL-0178 |

**Step 2: Link to Contract and Vendor**

| Field | Source | Validation |
|-------|--------|------------|
| Contract_ID | ISMS-IMP-A.8.30.2 | Must be Active contract |
| Vendor_ID | ISMS-IMP-A.8.30.1 | Must be Approved vendor |

**Step 3: Enter Deliverable Details**

| Field | Guidance |
|-------|----------|
| Deliverable_Name | Descriptive name (e.g., "User Authentication Module v2.0") |
| Deliverable_Type | Application, Module, Component, Library, API |
| Project_Classification | Determines testing depth (Critical, High, Standard) |
| Planned_Delivery | Contractual delivery date |
| Actual_Delivery | Date deliverable received |

**Step 4: Track Testing Status**

| Status | Definition | Next Action |
|--------|------------|-------------|
| Pending | Testing not started | Initiate testing |
| In Progress | Testing underway | Monitor progress |
| Complete | All testing finished | Review results for acceptance |
| N/A | No testing required | Document justification |

**Step 5: Track SBOM Status**

| Status | Definition |
|--------|------------|
| Yes | SBOM received and reviewed |
| No | SBOM not received (follow up required) |
| N/A | SBOM not applicable (no third-party components) |

**Step 6: Record Acceptance Status**

| Status | Definition | Authority |
|--------|------------|-----------|
| Pending | Acceptance not determined | N/A |
| Accepted | Meets all criteria, no blocking issues | Acceptance authority |
| Rejected | Critical issues, requires remediation | Acceptance authority |
| Conditional | Accepted with documented conditions | Acceptance authority + CISO |

### Sheet 2: Code Review Tracking – Completion Guide

**Purpose**: Document code review activities and findings for outsourced deliverables.

**Step-by-Step Completion:**

**Step 1: Generate Review ID**

Create unique identifier using format `REV-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | REV- | REV- |
| Sequential Number | 4 digits | 0312 |
| Full ID | REV-XXXX | REV-0312 |

**Step 2: Select Review Type**

| Review Type | Purpose | When Required |
|-------------|---------|---------------|
| Peer Review | General code quality | All deliverables |
| Security Review | Security-focused examination | All deliverables |
| Architecture Review | Design and structure evaluation | Complex deliverables |

**Step 3: Assign Appropriate Reviewer**

| Reviewer Role | Responsibilities | For Which Reviews |
|---------------|------------------|-------------------|
| Developer | Code quality, logic, standards | Peer Review |
| Security Team | Security vulnerabilities, OWASP | Security Review |
| Security Architect | Design flaws, threat modelling | Architecture Review |

**Step 4: Conduct Review**

**Review Focus Areas:**

| Category | Check Items |
|----------|-------------|
| Input Validation | All user inputs validated, parameterized queries |
| Authentication | Proper auth mechanisms, session management |
| Authorisation | Access controls, privilege checks |
| Cryptography | Proper algorithms, key management |
| Error Handling | Secure error handling, no information disclosure |
| Logging | Security events logged, no sensitive data in logs |
| Data Protection | PII handling, encryption at rest |
| Dependencies | Third-party component security |

**Step 5: Document Findings**

Record findings by severity:

| Severity | Definition | Examples |
|----------|------------|----------|
| Critical | Direct path to system compromise | SQL injection, auth bypass, RCE |
| High | Significant security impact | XSS, IDOR, insecure deserialization |
| Medium | Limited security impact | Information disclosure, weak crypto |
| Low | Best practice recommendations | Missing security headers |

**Step 6: Determine Review Result**

| Result | Criteria | Action |
|--------|----------|--------|
| Approved | No Critical/High findings | Proceed to next testing |
| Approved with Findings | No Critical, minor High acceptable | Proceed with remediation tracked |
| Rejected | Critical or multiple High findings | Return to vendor for remediation |

### Sheet 3: Security Testing Results – Completion Guide

**Purpose**: Track security testing activities and findings across all test types.

**Step-by-Step Completion:**

**Step 1: Generate Test ID**

Create unique identifier using format `TST-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | TST- | TST- |
| Sequential Number | 4 digits | 0456 |
| Full ID | TST-XXXX | TST-0456 |

**Step 2: Select Test Type**

| Test Type | Description | When Required |
|-----------|-------------|---------------|
| SAST | Static Application Security Testing | All code deliverables |
| DAST | Dynamic Application Security Testing | Web applications, APIs |
| SCA | Software Composition Analysis | All code with dependencies |
| Penetration Test | Manual security testing | Critical projects |
| Manual Review | Targeted manual analysis | Complex logic, crypto |

**Step 3: Execute Testing**

**SAST Testing Procedure:**

1. Configure scanner with organisation ruleset
2. Scan all source code files
3. Review and triage results
4. Remove false positives
5. Document confirmed findings
6. Generate report

**DAST Testing Procedure:**

1. Deploy application to test environment
2. Configure scanner authentication (if required)
3. Execute automated scan
4. Review and triage results
5. Perform manual verification of findings
6. Document confirmed findings

**SCA Testing Procedure:**

1. Generate or receive SBOM
2. Scan against vulnerability databases
3. Identify known vulnerabilities in components
4. Assess license compliance
5. Document findings and recommendations

**Penetration Testing Procedure:**

1. Define scope and rules of engagement
2. Execute reconnaissance
3. Identify and exploit vulnerabilities
4. Document attack paths and impacts
5. Provide remediation recommendations
6. Conduct re-test after remediation

**Step 4: Record Findings**

For each test, document:

| Field | Description |
|-------|-------------|
| Total_Findings | All findings before triage |
| Critical_Findings | Findings rated Critical |
| High_Findings | Findings rated High |
| Medium_Findings | Findings rated Medium |
| Low_Findings | Findings rated Low |
| False_Positives | Confirmed false positives |
| Findings_Remediated | Fixed by vendor |
| Findings_Outstanding | Still open |

**Step 5: Determine Retest Requirements**

| Condition | Retest Required | Scope |
|-----------|-----------------|-------|
| Critical findings remediated | Yes | Critical findings |
| High findings remediated | Yes | High findings |
| Medium/Low remediated | Optional | Risk-based |
| No changes | No | N/A |

### Sheet 4: SBOM Management – Completion Guide

**Purpose**: Track Software Bill of Materials for all deliverables, identifying third-party component risks.

**Step-by-Step Completion:**

**Step 1: Generate SBOM ID**

Create unique identifier using format `SBOM-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | SBOM- | SBOM- |
| Sequential Number | 4 digits | 0089 |
| Full ID | SBOM-XXXX | SBOM-0089 |

**Step 2: Receive and Validate SBOM**

**Acceptable SBOM Formats:**

| Format | Standard | Preference |
|--------|----------|------------|
| CycloneDX | OWASP | Preferred |
| SPDX | Linux Foundation | Acceptable |
| Spreadsheet | Custom | Acceptable with validation |

**SBOM Completeness Check:**

| Required Element | Description |
|------------------|-------------|
| Component name | Package/library name |
| Version | Specific version number |
| License | License type |
| Source | Repository/download location |
| Hash | Integrity verification |

**Step 3: Analyse Components**

Record component statistics:

| Field | Description |
|-------|-------------|
| Total_Components | All third-party components |
| Direct_Dependencies | Explicitly declared dependencies |
| Transitive_Dependencies | Dependencies of dependencies |

**Step 4: Identify Vulnerabilities**

Scan SBOM against vulnerability databases:

| Database | Coverage |
|----------|----------|
| NVD (National Vulnerability Database) | Comprehensive CVE coverage |
| GitHub Advisory Database | GitHub-tracked vulnerabilities |
| Snyk Vulnerability Database | Commercial intelligence |
| OSV (Open Source Vulnerabilities) | Google-maintained |

Record vulnerability counts:

| Field | Severity |
|-------|----------|
| Critical_Vulns | CVSS 9.0-10.0 |
| High_Vulns | CVSS 7.0-8.9 |
| Known_Vulnerabilities | Total vulnerable components |

**Step 5: Assess License Compliance**

| License Category | Risk | Action |
|------------------|------|--------|
| Permissive (MIT, BSD, Apache) | Low | Document |
| Weak Copyleft (LGPL) | Medium | Review usage |
| Strong Copyleft (GPL) | High | Legal review |
| Unknown | High | Investigate |

**Step 6: Review and Approve**

| Review Status | Criteria |
|---------------|----------|
| Accepted | No Critical/High vulns, acceptable licenses |
| Rejected | Critical vulnerabilities, problematic licenses |

**Step 7: Document Action Plan**

For issues requiring remediation:

| Issue Type | Action Plan |
|------------|-------------|
| Critical vulnerability | Vendor must update before acceptance |
| High vulnerability | Update required within SLA |
| License issue | Legal review and decision |
| Outdated component | Update recommended |

### Sheet 5: Acceptance Sign-off – Completion Guide

**Purpose**: Document formal acceptance decision for each deliverable based on testing results.

**Step-by-Step Completion:**

**Step 1: Generate Acceptance ID**

Create unique identifier using format `ACC-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | ACC- | ACC- |
| Sequential Number | 4 digits | 0234 |
| Full ID | ACC-XXXX | ACC-0234 |

**Step 2: Review Acceptance Criteria**

Verify each standard security acceptance criterion:

**Criterion 1: Code Review Completed**
- All code reviewed
- No unresolved Critical/High findings

**Criterion 2: SAST Scan Completed**
- Full source code scanned
- No unresolved Critical/High findings

**Criterion 3: SCA Scan Completed**
- All dependencies analysed
- No Critical/High vulnerable dependencies (or exception approved)

**Criterion 4: DAST Scan Completed (Web Applications)**
- Dynamic scan executed
- No unresolved Critical/High findings

**Criterion 5: Penetration Test Passed (Critical Projects)**
- Manual testing completed
- Critical findings remediated

**Criterion 6: SBOM Received and Reviewed**
- SBOM in acceptable format
- Components analysed and approved

**Criterion 7: No Secrets in Codebase**
- Secret scanning completed
- No credentials, API keys, or tokens

**Criterion 8: Security Documentation Complete**
- Security design documented
- Deployment security guide provided

**Criterion 9: Vulnerability SLAs Met**
- All remediation within contractual SLAs
- Or exceptions documented and approved

**Criterion 10: Security Training Verified**
- Vendor personnel completed security training
- Evidence provided

**Step 3: Document Status for Each Criterion**

| Status | Definition | Evidence Required |
|--------|------------|-------------------|
| Met | Criterion fully satisfied | Test reports, sign-offs |
| Not Met | Criterion not satisfied | Gap description |
| Waived | Exception approved | Waiver approval |
| N/A | Criterion not applicable | Justification |

**Step 4: Obtain Waivers (If Required)**

When criteria cannot be met:

| Waiver Requirement | Approver | Documentation |
|--------------------|----------|---------------|
| Non-critical criterion | IT Security Manager | Waiver form |
| Critical criterion (Standard project) | CISO | Waiver + risk acceptance |
| Critical criterion (Critical project) | CISO + Executive | Waiver + compensating controls |

**Step 5: Final Acceptance Decision**

| Decision | Criteria | Sign-off Authority |
|----------|----------|-------------------|
| Accepted | All criteria Met or waived | Per project classification |
| Rejected | Critical criteria Not Met | Acceptance authority |
| Conditional | Some criteria waived | CISO involvement required |

---

## Evidence Collection

### Evidence Requirements

Evidence must be collected for all testing activities:

| Evidence Category | Retention Period | Storage Location |
|-------------------|------------------|------------------|
| Test reports | 7 years | ISMS Evidence Library |
| Code review records | 7 years | ISMS Evidence Library |
| SBOM files | Duration of use + 3 years | ISMS Evidence Library |
| Acceptance sign-offs | 7 years | ISMS Evidence Library |
| Waiver approvals | 7 years | ISMS Evidence Library |
| Finding remediation | 7 years | ISMS Evidence Library |

### Evidence Folder Structure

```
ISMS-Evidence-Library/
└── Security-Testing/
    └── A.8.30-Outsourced-Development/
        └── [DEL-ID]-[Deliverable_Name]/
            ├── Code-Reviews/
            │   ├── REV-XXXX-Security-Review.pdf
            │   └── REV-XXXX-Findings.xlsx
            ├── SAST/
            │   ├── TST-XXXX-SAST-Report.pdf
            │   └── TST-XXXX-Findings.xlsx
            ├── DAST/
            │   └── TST-XXXX-DAST-Report.pdf
            ├── SCA/
            │   ├── SBOM-XXXX-CycloneDX.json
            │   └── TST-XXXX-SCA-Report.pdf
            ├── Penetration-Test/
            │   └── TST-XXXX-PenTest-Report.pdf
            └── Acceptance/
                ├── ACC-XXXX-Checklist.xlsx
                └── ACC-XXXX-Sign-off.pdf
```

### Evidence for Audit

During ISO 27001 audit, be prepared to demonstrate:

| Auditor Request | Evidence to Provide |
|-----------------|---------------------|
| "How do you verify security of outsourced code?" | Testing procedure + sample test results |
| "Show me code review for a recent deliverable" | Sheet 2 records + review findings |
| "What security testing do you perform?" | Sheet 3 + sample SAST/DAST reports |
| "How do you manage third-party components?" | Sheet 4 + SBOM examples |
| "What are acceptance criteria?" | Sheet 5 criteria list + sample acceptance |
| "What happens when criteria aren't met?" | Waiver records, rejection examples |

---

## Common Pitfalls

### Testing Coverage Errors

❌ **MISTAKE: Accepting code without any security testing**
All outsourced code must undergo security testing proportional to risk. Skipping testing creates unquantified risk.

❌ **MISTAKE: Relying solely on vendor's test results**
Vendor testing is valuable but insufficient. Independent testing by receiving organisation is essential.

❌ **MISTAKE: Not testing after remediation (no retest)**
When vendors remediate findings, retest is required to verify fixes. Accepting without retest may miss incomplete fixes.

❌ **MISTAKE: Skipping DAST for "internal" applications**
Internal applications still require DAST. Insider threats and lateral movement make internal apps targets.

### Finding Management Errors

❌ **MISTAKE: Accepting "won't fix" without risk acceptance**
If vendor won't fix a finding, formal risk acceptance is required. Never leave findings in limbo.

❌ **MISTAKE: Not tracking false positives**
False positives should be documented, not deleted. They may need re-evaluation in future scans.

❌ **MISTAKE: Treating all findings equally**
Critical findings must block acceptance. Low findings should not block acceptance but should be tracked.

### SBOM Errors

❌ **MISTAKE: Not requiring SBOM from vendors**
SBOMs are essential for vulnerability management. Require them contractually and verify delivery.

❌ **MISTAKE: One-time SBOM review**
SBOMs should be updated with each delivery. New vulnerabilities affect previously-cleared components.

❌ **MISTAKE: Ignoring transitive dependencies**
Vulnerabilities in transitive dependencies (dependencies of dependencies) are just as dangerous as direct ones.

### Acceptance Errors

❌ **MISTAKE: Accepting with open Critical findings**
Critical findings must be remediated before acceptance. No exceptions without CISO + Executive approval.

❌ **MISTAKE: Informal acceptance without documentation**
Acceptance must be formally documented. Verbal or email approval without checklist completion is insufficient.

❌ **MISTAKE: Single-person acceptance for Critical systems**
Critical system acceptance requires multiple sign-offs (technical and management).

---

## Quality Checklist

### Pre-Testing Checklist

Before beginning security testing:

- [ ] Deliverable registered in inventory
- [ ] Contract and vendor verified
- [ ] Project classification confirmed
- [ ] Test environment available
- [ ] Testing authorisation obtained
- [ ] SBOM received from vendor
- [ ] Testing tools configured

### Testing Completeness Checklist

Before proceeding to acceptance:

**Code Review**
- [ ] Security review completed
- [ ] Findings documented
- [ ] Critical/High findings addressed

**SAST**
- [ ] Full source code scanned
- [ ] Findings triaged
- [ ] False positives documented
- [ ] Critical/High findings remediated or risk accepted

**DAST (if applicable)**
- [ ] Application deployed to test environment
- [ ] Scan completed
- [ ] Findings triaged
- [ ] Critical/High findings addressed

**SCA**
- [ ] SBOM received and validated
- [ ] Vulnerability scan completed
- [ ] License compliance verified
- [ ] Critical vulnerabilities addressed

**Penetration Test (if required)**
- [ ] Scope defined and approved
- [ ] Testing completed
- [ ] Report received
- [ ] Critical findings addressed

### Acceptance Readiness Checklist

Before sign-off:

- [ ] All applicable testing complete
- [ ] All Critical findings resolved
- [ ] All High findings resolved or waived
- [ ] SBOM approved
- [ ] No secrets detected
- [ ] Documentation complete
- [ ] Acceptance criteria verified
- [ ] Evidence package complete
- [ ] Appropriate approver identified

---

## Review and Approval

### Testing Approval Authority

| Testing Activity | Approver |
|------------------|----------|
| Test plan for Critical project | CISO |
| Test plan for High/Standard | IT Security Manager |
| Penetration test scope | System Owner + IT Security |

### Acceptance Authority

| Project Classification | Acceptance Authority |
|------------------------|---------------------|
| Critical | CISO + System Owner + Project Sponsor |
| High | IT Security Manager + System Owner |
| Standard | IT Security Lead + Project Manager |

### Acceptance Workflow

```
All Testing Complete
         ↓
Findings Remediated and Verified
         ↓
Acceptance Criteria Checklist Completed
         ↓
Evidence Package Assembled
         ↓
Acceptance Authority Review
         ↓
    ├── All criteria met → Accepted
    ├── Waivers required → Waiver approval process
    └── Critical gaps → Rejected, return to vendor
```

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
