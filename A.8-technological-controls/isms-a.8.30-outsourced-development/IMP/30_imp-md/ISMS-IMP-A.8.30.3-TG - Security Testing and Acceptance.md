**ISMS-IMP-A.8.30.3-TG - Security Testing and Acceptance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.3-TG |
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

# Technical Specification

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

<!-- QA_VERIFIED: 2026-02-06 -->
