# ISMS-IMP-A.8.30.3 – Security Testing and Acceptance

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.3 |
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

# PART I: USER COMPLETION GUIDE

This section provides step-by-step guidance for completing the Security Testing and Acceptance workbook. Follow this guide to ensure comprehensive security validation of outsourced development deliverables before acceptance.

---

## 1. Assessment Overview

### 1.1 Purpose

The Security Testing and Acceptance workbook tracks security testing activities, manages software composition analysis, and documents acceptance criteria verification for all outsourced development deliverables. It ensures that code delivered by external vendors meets security requirements before integration into production systems.

ISO/IEC 27001:2022 Control A.8.30 states:

> *"The organisation should direct, monitor and review the activities related to outsourced system development."*

Security testing and formal acceptance are critical monitoring activities that verify vendors have met security requirements specified in contracts and policies.

### 1.2 Scope and Applicability

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

### 1.3 Business Context

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

### 1.4 Assessment Outputs

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

## 2. Prerequisites

### 2.1 Required Inputs

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

### 2.2 Required Approvals Before Testing

| Approval Type | Approver | Purpose |
|---------------|----------|---------|
| Test environment availability | IT Operations | Confirms environment ready |
| Test authorisation (pen testing) | System Owner | Authorises security testing |
| Budget approval (external testing) | Finance | If external pentest required |
| Vendor notification | Project Manager | Inform vendor testing will occur |

### 2.3 Required Knowledge

Testing personnel should understand:

- Secure development lifecycle (SDLC) concepts
- OWASP Top 10 and common vulnerability classes
- Security testing tools (SAST, DAST, SCA)
- Code review techniques
- Vulnerability classification (CVSS)
- Acceptance criteria interpretation
- Evidence documentation requirements

### 2.4 Tool Requirements

| Tool Category | Example Tools | Purpose |
|---------------|---------------|---------|
| SAST | SonarQube, Checkmarx, Fortify, Snyk Code | Static code analysis |
| DAST | OWASP ZAP, Burp Suite Pro, Acunetix | Dynamic application testing |
| SCA | Snyk, WhiteSource, Dependabot, OWASP Dependency-Check | Component analysis |
| Secret Scanner | GitLeaks, TruffleHog, GitHub Secret Scanning | Credential detection |
| Code Review | GitHub, GitLab, Bitbucket, Gerrit | Peer review platform |
| Test Management | Excel, Jira, TestRail | Finding tracking |

---

## 3. Workbook Structure Overview

### 3.1 Sheet Summary

The workbook contains five sheets covering the testing and acceptance lifecycle:

| Sheet | Purpose | Primary Owner | Update Frequency |
|-------|---------|---------------|------------------|
| 1: Deliverable Inventory | Track all deliverables | Project Manager | Per delivery |
| 2: Code Review Tracking | Document review findings | Security Reviewer | Per review |
| 3: Security Testing Results | Capture test findings | Security Tester | Per test |
| 4: SBOM Management | Track third-party components | IT Security | Per deliverable |
| 5: Acceptance Sign-off | Document acceptance decisions | Acceptance Authority | Per acceptance |

### 3.2 Sheet Dependencies

```
Sheet 1: Deliverable Inventory (Master)
         ↓ (Deliverable_ID reference)
Sheet 2: Code Review Tracking
         ↓ (parallel)
Sheet 3: Security Testing Results
         ↓ (parallel)
Sheet 4: SBOM Management
         ↓ (all feed into)
Sheet 5: Acceptance Sign-off
```

### 3.3 Data Flow

1. **Deliverable Received**: Registered in Sheet 1
2. **Testing Initiated**: Code review (Sheet 2), security testing (Sheet 3), SBOM review (Sheet 4)
3. **Findings Triaged**: Critical/High findings sent to vendor
4. **Remediation Verified**: Retesting completed
5. **Acceptance Determined**: Criteria verified in Sheet 5
6. **Sign-off Recorded**: Formal acceptance documented

---

## 4. Completion Walkthrough

### 4.1 Sheet 1: Deliverable Inventory – Completion Guide

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

### 4.2 Sheet 2: Code Review Tracking – Completion Guide

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

### 4.3 Sheet 3: Security Testing Results – Completion Guide

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

### 4.4 Sheet 4: SBOM Management – Completion Guide

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

### 4.5 Sheet 5: Acceptance Sign-off – Completion Guide

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

## 5. Evidence Collection

### 5.1 Evidence Requirements

Evidence must be collected for all testing activities:

| Evidence Category | Retention Period | Storage Location |
|-------------------|------------------|------------------|
| Test reports | 7 years | ISMS Evidence Library |
| Code review records | 7 years | ISMS Evidence Library |
| SBOM files | Duration of use + 3 years | ISMS Evidence Library |
| Acceptance sign-offs | 7 years | ISMS Evidence Library |
| Waiver approvals | 7 years | ISMS Evidence Library |
| Finding remediation | 7 years | ISMS Evidence Library |

### 5.2 Evidence Folder Structure

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

### 5.3 Evidence for Audit

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

## 6. Common Pitfalls

### 6.1 Testing Coverage Errors

❌ **MISTAKE: Accepting code without any security testing**
All outsourced code must undergo security testing proportional to risk. Skipping testing creates unquantified risk.

❌ **MISTAKE: Relying solely on vendor's test results**
Vendor testing is valuable but insufficient. Independent testing by receiving organisation is essential.

❌ **MISTAKE: Not testing after remediation (no retest)**
When vendors remediate findings, retest is required to verify fixes. Accepting without retest may miss incomplete fixes.

❌ **MISTAKE: Skipping DAST for "internal" applications**
Internal applications still require DAST. Insider threats and lateral movement make internal apps targets.

### 6.2 Finding Management Errors

❌ **MISTAKE: Accepting "won't fix" without risk acceptance**
If vendor won't fix a finding, formal risk acceptance is required. Never leave findings in limbo.

❌ **MISTAKE: Not tracking false positives**
False positives should be documented, not deleted. They may need re-evaluation in future scans.

❌ **MISTAKE: Treating all findings equally**
Critical findings must block acceptance. Low findings should not block acceptance but should be tracked.

### 6.3 SBOM Errors

❌ **MISTAKE: Not requiring SBOM from vendors**
SBOMs are essential for vulnerability management. Require them contractually and verify delivery.

❌ **MISTAKE: One-time SBOM review**
SBOMs should be updated with each delivery. New vulnerabilities affect previously-cleared components.

❌ **MISTAKE: Ignoring transitive dependencies**
Vulnerabilities in transitive dependencies (dependencies of dependencies) are just as dangerous as direct ones.

### 6.4 Acceptance Errors

❌ **MISTAKE: Accepting with open Critical findings**
Critical findings must be remediated before acceptance. No exceptions without CISO + Executive approval.

❌ **MISTAKE: Informal acceptance without documentation**
Acceptance must be formally documented. Verbal or email approval without checklist completion is insufficient.

❌ **MISTAKE: Single-person acceptance for Critical systems**
Critical system acceptance requires multiple sign-offs (technical and management).

---

## 7. Quality Checklist

### 7.1 Pre-Testing Checklist

Before beginning security testing:

- [ ] Deliverable registered in inventory
- [ ] Contract and vendor verified
- [ ] Project classification confirmed
- [ ] Test environment available
- [ ] Testing authorisation obtained
- [ ] SBOM received from vendor
- [ ] Testing tools configured

### 7.2 Testing Completeness Checklist

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

### 7.3 Acceptance Readiness Checklist

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

## 8. Review and Approval

### 8.1 Testing Approval Authority

| Testing Activity | Approver |
|------------------|----------|
| Test plan for Critical project | CISO |
| Test plan for High/Standard | IT Security Manager |
| Penetration test scope | System Owner + IT Security |

### 8.2 Acceptance Authority

| Project Classification | Acceptance Authority |
|------------------------|---------------------|
| Critical | CISO + System Owner + Project Sponsor |
| High | IT Security Manager + System Owner |
| Standard | IT Security Lead + Project Manager |

### 8.3 Acceptance Workflow

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

# PART II: TECHNICAL SPECIFICATION

This section provides technical details for the Security Testing and Acceptance workbook implementation.

---

## 9. Workbook Technical Structure

### 9.1 Workbook Properties

| Property | Value |
|----------|-------|
| File Format | .xlsx (Excel 2016+) |
| Sheet Protection | Structure protected, cells unlocked for input |
| Workbook Protection | Structure only |
| File Naming | ISMS-IMP-A.8.30.3_Security_Testing_Acceptance_YYYYMMDD.xlsx |

### 9.2 Sheet Configuration

| Sheet | Tab Colour | Protection Level | Hidden |
|-------|------------|------------------|--------|
| Deliverable Inventory | Blue (#4472C4) | Input cells unlocked | No |
| Code Review Tracking | Green (#70AD47) | Input cells unlocked | No |
| Security Testing Results | Orange (#ED7D31) | Input cells unlocked | No |
| SBOM Management | Purple (#7030A0) | Input cells unlocked | No |
| Acceptance Sign-off | Red (#C00000) | Input cells unlocked | No |
| Validation Lists | Grey (#A6A6A6) | Full protection | Yes |
| Dashboard | Dark Blue (#002060) | Full protection | No |

---

## 10. Sheet Specifications

### 10.1 Sheet 1: Deliverable Inventory – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Deliverable_ID | 15 | Text | Format: DEL-#### | Yes |
| B | Contract_ID | 15 | Reference | Must exist | Yes |
| C | Vendor_ID | 15 | Reference | Must exist | Yes |
| D | Deliverable_Name | 40 | Text | Max 200 chars | Yes |
| E | Deliverable_Type | 15 | List | Application,Module,Component,Library,API | Yes |
| F | Project_Classification | 15 | List | Critical,High,Standard | Yes |
| G | Planned_Delivery | 15 | Date | DD.MM.YYYY | Yes |
| H | Actual_Delivery | 15 | Date | DD.MM.YYYY | Conditional |
| I | Code_Review_Status | 15 | List | Pending,In Progress,Complete,N/A | Yes |
| J | Security_Test_Status | 15 | List | Pending,In Progress,Complete | Yes |
| K | SBOM_Received | 12 | List | Yes,No,N/A | Yes |
| L | Acceptance_Status | 15 | List | Pending,Accepted,Rejected,Conditional | Yes |
| M | Acceptance_Date | 15 | Date | DD.MM.YYYY | Conditional |
| N | Accepted_By | 25 | Text | Name + Role | Conditional |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Acceptance_Status = "Rejected" | Red fill |
| Acceptance_Status = "Conditional" | Yellow fill |
| SBOM_Received = "No" AND Actual_Delivery not blank | Orange fill |
| Security_Test_Status = "Pending" AND Actual_Delivery not blank > 5 days | Orange fill |

### 10.2 Sheet 2: Code Review Tracking – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Review_ID | 15 | Text | Format: REV-#### | Yes |
| B | Deliverable_ID | 15 | Reference | Must exist | Yes |
| C | Review_Type | 20 | List | Peer Review,Security Review,Architecture Review | Yes |
| D | Review_Date | 15 | Date | DD.MM.YYYY | Yes |
| E | Reviewer | 25 | Text | Name | Yes |
| F | Reviewer_Role | 20 | List | Developer,Security Team,Security Architect | Yes |
| G | Files_Reviewed | 10 | Number | Integer >= 0 | Yes |
| H | Security_Findings | 10 | Number | Integer >= 0 | Yes |
| I | Critical_Findings | 10 | Number | Integer >= 0 | Yes |
| J | High_Findings | 10 | Number | Integer >= 0 | Yes |
| K | Medium_Findings | 10 | Number | Integer >= 0 | Yes |
| L | Low_Findings | 10 | Number | Integer >= 0 | Yes |
| M | Review_Result | 25 | List | Approved,Approved with Findings,Rejected | Yes |
| N | Findings_Reference | 40 | Text | File path/URL | Conditional |
| O | Notes | 40 | Text | Optional | No |

**Formulas:**

```excel
Security_Findings (H2) - Validation:
=I2+J2+K2+L2
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Review_Result = "Rejected" | Red fill |
| Critical_Findings > 0 | Red text, bold |
| High_Findings > 0 | Orange text |

### 10.3 Sheet 3: Security Testing Results – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Test_ID | 15 | Text | Format: TST-#### | Yes |
| B | Deliverable_ID | 15 | Reference | Must exist | Yes |
| C | Test_Type | 20 | List | SAST,DAST,SCA,Penetration Test,Manual Review | Yes |
| D | Test_Tool | 25 | Text | Tool name | Yes |
| E | Test_Date | 15 | Date | DD.MM.YYYY | Yes |
| F | Tester | 25 | Text | Name/Team | Yes |
| G | Scope | 40 | Text | Description | Yes |
| H | Total_Findings | 10 | Number | Integer >= 0 | Yes |
| I | Critical_Findings | 10 | Number | Integer >= 0 | Yes |
| J | High_Findings | 10 | Number | Integer >= 0 | Yes |
| K | Medium_Findings | 10 | Number | Integer >= 0 | Yes |
| L | Low_Findings | 10 | Number | Integer >= 0 | Yes |
| M | False_Positives | 10 | Number | Integer >= 0 | Yes |
| N | Findings_Remediated | 10 | Number | Integer >= 0 | Yes |
| O | Findings_Outstanding | 10 | Number | Calculated | Auto |
| P | Report_Reference | 40 | Text | File path/URL | Yes |
| Q | Retest_Required | 12 | List | Yes,No | Yes |
| R | Retest_Date | 15 | Date | DD.MM.YYYY | Conditional |
| S | Retest_Status | 15 | List | Pending,Passed,Failed,N/A | Conditional |

**Formulas:**

```excel
Findings_Outstanding (O2):
=H2-M2-N2
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Critical_Findings > 0 | Red fill in cell |
| High_Findings > 0 | Orange fill in cell |
| Retest_Required = "Yes" AND Retest_Status = "Pending" | Yellow row |
| Retest_Status = "Failed" | Red row |

### 10.4 Sheet 4: SBOM Management – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | SBOM_ID | 15 | Text | Format: SBOM-#### | Yes |
| B | Deliverable_ID | 15 | Reference | Must exist | Yes |
| C | SBOM_Format | 15 | List | CycloneDX,SPDX,Spreadsheet,Other | Yes |
| D | SBOM_Date | 15 | Date | DD.MM.YYYY | Yes |
| E | Total_Components | 10 | Number | Integer >= 0 | Yes |
| F | Direct_Dependencies | 10 | Number | Integer >= 0 | Yes |
| G | Transitive_Dependencies | 10 | Number | Integer >= 0 | Yes |
| H | Known_Vulnerabilities | 10 | Number | Integer >= 0 | Yes |
| I | Critical_Vulns | 10 | Number | Integer >= 0 | Yes |
| J | High_Vulns | 10 | Number | Integer >= 0 | Yes |
| K | License_Issues | 10 | Number | Integer >= 0 | Yes |
| L | Outdated_Components | 10 | Number | Integer >= 0 | Yes |
| M | Review_Status | 15 | List | Pending,Reviewed,Accepted,Rejected | Yes |
| N | Reviewed_By | 25 | Text | Name | Conditional |
| O | Review_Date | 15 | Date | DD.MM.YYYY | Conditional |
| P | SBOM_Reference | 40 | Text | File path/URL | Yes |
| Q | Action_Plan | 50 | Text | If issues | Conditional |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Critical_Vulns > 0 | Red fill |
| High_Vulns > 0 | Orange fill |
| License_Issues > 0 | Yellow fill |
| Review_Status = "Rejected" | Red row |

### 10.5 Sheet 5: Acceptance Sign-off – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Acceptance_ID | 15 | Text | Format: ACC-#### | Yes |
| B | Deliverable_ID | 15 | Reference | Must exist | Yes |
| C | Acceptance_Criteria | 50 | Text | Pre-populated | Yes |
| D | Criteria_Category | 15 | List | Functional,Security,Performance,Documentation | Yes |
| E | Status | 12 | List | Met,Not Met,Waived,N/A | Yes |
| F | Evidence_Reference | 40 | Text | File path/URL | Conditional |
| G | Verified_By | 25 | Text | Name | Conditional |
| H | Verification_Date | 15 | Date | DD.MM.YYYY | Conditional |
| I | Waiver_Reason | 40 | Text | If Waived | Conditional |
| J | Waiver_Approver | 25 | Text | Name + Role | Conditional |

**Pre-populated Security Criteria (10 standard items per deliverable):**

1. Code review completed with no unresolved Critical/High findings
2. SAST scan completed with no unresolved Critical/High findings
3. SCA scan completed with no Critical/High vulnerable dependencies
4. DAST scan completed (for web applications)
5. Penetration test passed (for Critical projects)
6. SBOM received and reviewed
7. No secrets detected in codebase
8. Security documentation complete
9. Vulnerability remediation SLAs met
10. Security training completed by all developers

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Status = "Not Met" | Red fill |
| Status = "Waived" | Yellow fill |
| Status = "Met" | Green fill |
| Status = "N/A" | Grey fill |

---

## 11. Automation Requirements

### 11.1 Automated Alerts

| Trigger | Alert Type | Recipients | Timing |
|---------|------------|------------|--------|
| Critical findings detected | Email + Dashboard | IT Security Manager, CISO | Immediate |
| Testing overdue | Email | IT Security, Project Manager | Daily |
| SBOM not received | Email | IT Security, Vendor | 3 days after delivery |
| Retest overdue | Email | IT Security, Vendor | 3 days after due |
| Acceptance pending > 10 days | Email | Acceptance authority | Daily |

### 11.2 Data Validation Automation

| Validation | Action | Frequency |
|------------|--------|-----------|
| ID uniqueness | Prevent duplicate | On entry |
| Reference existence | Validation error | On entry |
| Finding counts | Auto-sum validation | On entry |
| Outstanding calculation | Auto-calculate | Real-time |
| Required field completion | Highlight | Real-time |

### 11.3 Dashboard Calculations

| Metric | Formula | Refresh |
|--------|---------|---------|
| Deliverables pending testing | COUNT where Test_Status = Pending | Daily |
| Open Critical findings | SUM of Critical across all tests | Daily |
| Acceptance rate | Accepted / (Accepted + Rejected) | Weekly |
| Average test cycle | Avg days from delivery to acceptance | Weekly |
| SBOM compliance | Received / Total deliverables | Daily |

---

## 12. Metrics and KPIs

### 12.1 Testing Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Code review completion | 100% | Reviewed / Total | IT Security |
| SAST scan completion | 100% | Scanned / Total | IT Security |
| DAST completion (web apps) | 100% | Scanned / Applicable | IT Security |
| Critical findings at acceptance | 0 | Count at acceptance | IT Security |

### 12.2 SBOM Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| SBOM compliance | 100% | Received / Total | IT Security |
| Vulnerable component rate | <5% | Vulnerable / Total components | IT Security |
| License compliance | 100% | Compliant / Total | Legal/IT Security |

### 12.3 Acceptance Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| First-pass acceptance rate | >80% | Accepted first time / Total | IT Security |
| Average test cycle time | <10 days | Avg (Acceptance - Delivery) | IT Security |
| Conditional acceptance rate | <10% | Conditional / Total accepted | CISO |

---

## 13. Evidence Package for ISO 27001 Audit

### 13.1 Standard Evidence Package

| Document | Purpose | Preparation |
|----------|---------|-------------|
| Deliverable inventory | All outsourced deliveries | Export Sheet 1 |
| Testing summary | Test completion statistics | Dashboard export |
| Sample test reports | Detailed testing evidence | 3-5 complete packages |
| SBOM compliance report | Component management | Sheet 4 summary |
| Acceptance records | Sign-off evidence | Sheet 5 samples |
| Finding remediation | Vulnerability handling | Remediation timeline |

### 13.2 Audit Preparation Checklist

- [ ] Export deliverable inventory (12 months)
- [ ] Generate testing statistics
- [ ] Prepare sample packages for each project classification
- [ ] Compile SBOM compliance report
- [ ] Gather acceptance sign-off examples
- [ ] Document finding remediation process

---

## 14. Generator Script Reference

### 14.1 Script Location

```
10-isms-scr-base/
└── isms-a.8.30-outsourced-development/
    └── 10_generator-master/
        └── generate_a830_3_security_testing.py
```

### 14.2 Script Execution

```bash
cd 10-isms-scr-base/isms-a.8.30-outsourced-development/10_generator-master
python3 generate_a830_3_security_testing.py
mv *.xlsx ../90_workbooks/
```

### 14.3 Output

```
ISMS-IMP-A.8.30.3_Security_Testing_Acceptance_YYYYMMDD.xlsx
```

---

**END OF SPECIFICATION**

---

*"Quality is not an act, it is a habit."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-03 -->
