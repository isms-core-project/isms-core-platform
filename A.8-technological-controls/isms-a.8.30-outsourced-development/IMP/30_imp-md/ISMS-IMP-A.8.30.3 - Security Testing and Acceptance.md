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

---

## 1. Workbook Purpose

This workbook tracks security testing activities and acceptance criteria for outsourced development deliverables.

**Primary Use Cases**:
- Track code review completion for outsourced code
- Document security testing results (SAST, DAST, SCA, penetration testing)
- Manage Software Bill of Materials (SBOM) for deliverables
- Track security acceptance sign-off
- Evidence collection for audits

---

## 2. Workbook Structure

### Sheet 1: Deliverable Inventory

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Deliverable_ID | Unique deliverable identifier | Text | DEL-XXXX format |
| Contract_ID | Link to contract | Reference | Valid Contract_ID |
| Vendor_ID | Delivering vendor | Reference | Valid Vendor_ID |
| Deliverable_Name | Name/description of deliverable | Text | Required |
| Deliverable_Type | Type of deliverable | Dropdown | Application, Module, Component, Library, API |
| Project_Classification | Risk classification | Dropdown | Critical, High, Standard |
| Planned_Delivery | Planned delivery date | Date | DD.MM.YYYY |
| Actual_Delivery | Actual delivery date | Date | DD.MM.YYYY |
| Code_Review_Status | Internal code review status | Dropdown | Pending, In Progress, Complete, N/A |
| Security_Test_Status | Security testing status | Dropdown | Pending, In Progress, Complete |
| SBOM_Received | SBOM received | Dropdown | Yes, No, N/A |
| Acceptance_Status | Final acceptance status | Dropdown | Pending, Accepted, Rejected, Conditional |
| Acceptance_Date | Date of acceptance | Date | DD.MM.YYYY |
| Accepted_By | Acceptance authority | Text | Name + Role |

### Sheet 2: Code Review Tracking

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Review_ID | Unique review identifier | Text | REV-XXXX format |
| Deliverable_ID | Link to deliverable | Reference | Valid Deliverable_ID |
| Review_Type | Type of review | Dropdown | Peer Review, Security Review, Architecture Review |
| Review_Date | Date of review | Date | DD.MM.YYYY |
| Reviewer | Person conducting review | Text | Name |
| Reviewer_Role | Reviewer's role | Dropdown | Developer, Security Team, Security Architect |
| Files_Reviewed | Number of files reviewed | Number | Integer |
| Security_Findings | Number of security findings | Number | Integer |
| Critical_Findings | Critical findings count | Number | Integer |
| High_Findings | High findings count | Number | Integer |
| Medium_Findings | Medium findings count | Number | Integer |
| Low_Findings | Low findings count | Number | Integer |
| Review_Result | Review outcome | Dropdown | Approved, Approved with Findings, Rejected |
| Findings_Reference | Link to findings detail | Text | File path/URL |
| Notes | Additional notes | Text | Optional |

### Sheet 3: Security Testing Results

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Test_ID | Unique test identifier | Text | TST-XXXX format |
| Deliverable_ID | Link to deliverable | Reference | Valid Deliverable_ID |
| Test_Type | Type of security test | Dropdown | SAST, DAST, SCA, Penetration Test, Manual Review |
| Test_Tool | Tool used | Text | Tool name |
| Test_Date | Date of test | Date | DD.MM.YYYY |
| Tester | Person/team conducting test | Text | Name/Team |
| Scope | Testing scope | Text | Description |
| Total_Findings | Total findings count | Number | Integer |
| Critical_Findings | Critical findings | Number | Integer |
| High_Findings | High findings | Number | Integer |
| Medium_Findings | Medium findings | Number | Integer |
| Low_Findings | Low findings | Number | Integer |
| False_Positives | Confirmed false positives | Number | Integer |
| Findings_Remediated | Findings fixed | Number | Integer |
| Findings_Outstanding | Remaining findings | Number | Integer |
| Report_Reference | Test report location | Text | File path/URL |
| Retest_Required | Retest needed | Dropdown | Yes, No |
| Retest_Date | Scheduled retest date | Date | DD.MM.YYYY |
| Retest_Status | Retest outcome | Dropdown | Pending, Passed, Failed, N/A |

### Sheet 4: SBOM Management

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| SBOM_ID | Unique SBOM identifier | Text | SBOM-XXXX format |
| Deliverable_ID | Link to deliverable | Reference | Valid Deliverable_ID |
| SBOM_Format | Format of SBOM | Dropdown | CycloneDX, SPDX, Spreadsheet, Other |
| SBOM_Date | Date SBOM generated | Date | DD.MM.YYYY |
| Total_Components | Total third-party components | Number | Integer |
| Direct_Dependencies | Direct dependencies | Number | Integer |
| Transitive_Dependencies | Transitive dependencies | Number | Integer |
| Known_Vulnerabilities | Components with known vulns | Number | Integer |
| Critical_Vulns | Critical vulnerabilities | Number | Integer |
| High_Vulns | High vulnerabilities | Number | Integer |
| License_Issues | Components with license concerns | Number | Integer |
| Outdated_Components | Components needing update | Number | Integer |
| Review_Status | SBOM review status | Dropdown | Pending, Reviewed, Accepted, Rejected |
| Reviewed_By | Person who reviewed | Text | Name |
| Review_Date | Date reviewed | Date | DD.MM.YYYY |
| SBOM_Reference | SBOM file location | Text | File path/URL |
| Action_Plan | Remediation plan if issues | Text | Description |

### Sheet 5: Acceptance Sign-off

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Acceptance_ID | Unique acceptance record | Text | ACC-XXXX format |
| Deliverable_ID | Link to deliverable | Reference | Valid Deliverable_ID |
| Acceptance_Criteria | Criteria being verified | Text | Criteria description |
| Criteria_Category | Category of criteria | Dropdown | Functional, Security, Performance, Documentation |
| Status | Criteria met | Dropdown | Met, Not Met, Waived, N/A |
| Evidence_Reference | Evidence of criteria met | Text | File path/URL |
| Verified_By | Person who verified | Text | Name |
| Verification_Date | Date verified | Date | DD.MM.YYYY |
| Waiver_Reason | If waived, reason | Text | Optional |
| Waiver_Approver | If waived, approver | Text | Name + Role |

**Standard Security Acceptance Criteria**:
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

---

## 3. Data Sources

| Data Element | Source System | Collection Method |
|--------------|---------------|-------------------|
| Deliverable information | Project management system | Manual entry |
| Code review data | Version control (GitHub, GitLab) | API import / Manual |
| SAST results | SAST tool (SonarQube, Checkmarx) | API import / Report upload |
| DAST results | DAST tool (OWASP ZAP, Burp) | Report upload |
| SCA results | SCA tool (Snyk, Dependabot) | API import / Report upload |
| Penetration test results | Pentest provider | Report upload |
| SBOM | Vendor submission | File upload |

---

## 4. Testing Workflow

```
Deliverable Received:
1. Deliverable registered in inventory
         ↓
2. Code review initiated
         ↓
3. SAST scan executed
         ↓
4. SCA scan executed (SBOM generated)
         ↓
5. DAST scan (for web apps) on staging
         ↓
6. Penetration test (for Critical projects)
         ↓
7. Findings triaged and prioritized
         ↓
8. Vendor remediates findings
         ↓
9. Retest for Critical/High findings
         ↓
10. Acceptance criteria verified
         ↓
11. Sign-off by appropriate authority
         ↓
12. Deliverable accepted or rejected
```

---

## 5. Metrics and KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Code review completion | 100% before acceptance | Reviewed deliverables / Total deliverables |
| SAST scan completion | 100% | Scanned deliverables / Total deliverables |
| Critical findings pre-acceptance | 0 | Open Critical findings at acceptance |
| High findings pre-acceptance | 0 (or exception) | Open High findings at acceptance |
| SBOM compliance | 100% received | Deliverables with SBOM / Total deliverables |
| Acceptance with exceptions | <10% | Conditional acceptances / Total acceptances |
| Average remediation time (Critical) | ≤7 days | Days from finding to fix |

---

## 6. Automation Requirements

**Automated Imports**:
- SAST findings from security scanning tools
- SCA findings from dependency scanners
- Code review status from version control

**Automated Calculations**:
- Outstanding findings (Total - Remediated - False Positives)
- Acceptance criteria completion percentage
- Days in testing (Delivery to Acceptance)

**Automated Alerts**:
- Critical findings detected
- Testing overdue (> planned delivery + 5 days)
- SBOM not received (> delivery + 3 days)

---

## 7. Evidence Package

For ISO 27001 audit, generate:
- Deliverable inventory with acceptance status
- Code review completion summary
- Security testing summary by test type
- SBOM compliance report
- Acceptance sign-off records
- Findings remediation timeline analysis
- Sample test reports for Critical projects

---

**END OF SPECIFICATION**

---

*"Quality is not an act, it is a habit."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-01 -->
