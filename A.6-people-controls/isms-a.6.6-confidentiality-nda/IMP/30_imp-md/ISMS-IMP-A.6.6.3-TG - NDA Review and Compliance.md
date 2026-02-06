**ISMS-IMP-A.6.6.3-TG - NDA Review and Compliance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6: Confidentiality or Non-Disclosure Agreements

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.3-TG |
| **Document Title** | NDA Review and Compliance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.6.6: Confidentiality or Non-Disclosure Agreements |
| **Parent Policy** | ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification

This section provides technical details for the NDA Review and Compliance workbook implementation.

---

## 9. Workbook Technical Structure

### 9.1 Workbook Properties

| Property | Value |
|----------|-------|
| File Format | .xlsx (Excel 2016+) |
| Sheet Protection | Structure protected, cells unlocked for input |
| Workbook Protection | Structure only |
| File Naming | ISMS-IMP-A.6.6.3_NDA_Review_and_Compliance_YYYYMMDD.xlsx |

### 9.2 Sheet Configuration

| Sheet | Tab Colour | Protection Level | Hidden |
|-------|------------|------------------|--------|
| Instructions | Grey (#A6A6A6) | Full protection | No |
| Periodic_Review | Blue (#4472C4) | Input cells unlocked | No |
| Template_Adequacy | Green (#70AD47) | Input cells unlocked | No |
| Coverage_Analysis | Orange (#ED7D31) | Input cells unlocked | No |
| Compliance_Check | Purple (#7030A0) | Input cells unlocked | No |
| Gap_Register | Red (#C00000) | Input cells unlocked | No |
| Evidence_Register | Teal (#00B0F0) | Input cells unlocked | No |
| Approval_SignOff | Gold (#FFC000) | Input cells unlocked | No |
| Validation Lists | Grey (#A6A6A6) | Full protection | Yes |

---

## 10. Sheet Specifications

### 10.1 Sheet 2: Periodic_Review – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Review_ID | 15 | Text | Format: REV-YYYY-NNN | Yes |
| B | Review_Type | 25 | List | See validation list | Yes |
| C | Review_Scope | 50 | Text | Description | Yes |
| D | Planned_Date | 15 | Date | DD.MM.YYYY | Yes |
| E | Actual_Date | 15 | Date | DD.MM.YYYY | Conditional |
| F | Reviewer | 25 | Text | Name | Yes |
| G | Findings_Count | 10 | Number | Integer >= 0 | Conditional |
| H | Gaps_Identified | 10 | Number | Integer >= 0 | Conditional |
| I | Status | 15 | List | See validation list | Yes |
| J | Next_Review | 15 | Date | DD.MM.YYYY | Yes |
| K | Notes | 40 | Text | Optional | No |

**Validation Lists:**

```
Review_Type: Annual Full Review, Quarterly Check, Template Update Review, Triggered Review, Ad-hoc Review
Status: Scheduled, In Progress, Completed, Overdue, Cancelled
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Status = "Overdue" | Red fill |
| Planned_Date < TODAY() AND Status = "Scheduled" | Orange fill |
| Status = "Completed" | Green fill |

### 10.2 Sheet 3: Template_Adequacy – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Template_ID | 15 | Text | From registry | Yes |
| B | Template_Name | 35 | Text | Name | Yes |
| C | Template_Version | 10 | Text | Version | Yes |
| D | Last_Legal_Review | 15 | Date | DD.MM.YYYY | Yes |
| E | Legal_Review_Due | 15 | Date | Calculated | Auto |
| F | Regulatory_Current | 12 | List | Yes,Partial,No | Yes |
| G | Covers_All_Info_Types | 12 | List | Yes,Partial,No | Yes |
| H | Post_Term_Adequate | 12 | List | Yes,No,Partial | Yes |
| I | Remedies_Adequate | 12 | List | Yes,No,Partial | Yes |
| J | Jurisdiction_Correct | 12 | List | Yes,No | Yes |
| K | Overall_Adequacy | 20 | List | See validation | Yes |
| L | Action_Required | 40 | Text | If inadequate | Conditional |
| M | Action_Owner | 20 | Text | If action required | Conditional |
| N | Notes | 40 | Text | Optional | No |

**Formulas:**

```excel
Legal_Review_Due (E2):
=EDATE(D2,12)
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Overall_Adequacy = "Inadequate" | Red fill |
| Overall_Adequacy = "Partially Adequate" | Yellow fill |
| Legal_Review_Due < TODAY() | Orange fill |

### 10.3 Sheet 4: Coverage_Analysis – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Stakeholder_Category | 25 | Text | Category name | Yes |
| B | Total_Count | 10 | Number | Integer >= 0 | Yes |
| C | NDA_Required | 10 | Number | Integer >= 0 | Yes |
| D | NDA_Signed | 10 | Number | Integer >= 0 | Yes |
| E | Coverage_Rate | 10 | Percentage | Calculated | Auto |
| F | Expired_NDAs | 10 | Number | Integer >= 0 | Yes |
| G | Missing_NDAs | 10 | Number | Calculated | Auto |
| H | Gap_Status | 20 | List | See validation | Yes |
| I | Remediation_Owner | 20 | Text | If gap | Conditional |
| J | Target_Date | 15 | Date | If gap | Conditional |
| K | Notes | 40 | Text | Optional | No |

**Formulas:**

```excel
Coverage_Rate (E2):
=IF(C2=0,0,D2/C2)

Missing_NDAs (G2):
=MAX(0,C2-D2)
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Coverage_Rate < 90% | Red fill |
| Coverage_Rate < 100% AND >= 90% | Yellow fill |
| Coverage_Rate = 100% | Green fill |

### 10.4 Sheet 5: Compliance_Check – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | NDA_ID | 15 | Text | From execution tracking | Yes |
| B | Counterparty | 30 | Text | Name | Yes |
| C | Category | 20 | Text | Stakeholder category | Yes |
| D | Correctly_Executed | 12 | List | Yes,No | Yes |
| E | Within_Validity | 12 | List | Yes,No,Perpetual | Yes |
| F | Appropriate_Template | 12 | List | Yes,No | Yes |
| G | All_Parties_Signed | 12 | List | Yes,No | Yes |
| H | Securely_Stored | 12 | List | Yes,No | Yes |
| I | Overall_Compliance | 15 | List | See validation | Yes |
| J | Issues_Found | 40 | Text | If non-compliant | Conditional |
| K | Action_Required | 40 | Text | If action needed | Conditional |
| L | Notes | 40 | Text | Optional | No |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Overall_Compliance = "Non-Compliant" | Red fill |
| Overall_Compliance = "Partially Compliant" | Yellow fill |
| Overall_Compliance = "Compliant" | Green fill |

### 10.5 Sheet 6: Gap_Register – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Gap_ID | 15 | Text | Format: GAP-YYYY-NNN | Yes |
| B | Gap_Type | 20 | List | See validation | Yes |
| C | Description | 50 | Text | Gap details | Yes |
| D | Affected_Area | 30 | Text | Who/what affected | Yes |
| E | Severity | 12 | List | Critical,High,Medium,Low | Yes |
| F | Identified_Date | 15 | Date | DD.MM.YYYY | Yes |
| G | Source_Review | 15 | Text | Review ID | Yes |
| H | Owner | 20 | Text | Remediation owner | Yes |
| I | Remediation_Action | 50 | Text | What to do | Yes |
| J | Target_Date | 15 | Date | DD.MM.YYYY | Yes |
| K | Status | 20 | List | See validation | Yes |
| L | Closure_Date | 15 | Date | DD.MM.YYYY | Conditional |
| M | Evidence_Reference | 30 | Text | Evidence ID | Conditional |
| N | Notes | 40 | Text | Optional | No |

**Validation Lists:**

```
Gap_Type: Missing NDA, Expired NDA, Inadequate Template, Unsigned, Wrong Template, Storage Issue, Execution Error, Coverage Gap, Other
Severity: Critical, High, Medium, Low
Status: Open, In Progress, Remediated, Verified Closed, Risk Accepted
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Status = "Open" AND Severity = "Critical" | Red fill, bold |
| Status = "Open" AND Target_Date < TODAY() | Red fill |
| Status = "Verified Closed" | Green fill |

---

## 11. Automation Requirements

### 11.1 Automated Alerts

| Trigger | Alert Type | Recipients | Timing |
|---------|------------|------------|--------|
| Review overdue | Email | ISM | Daily |
| Critical gap open > 3 days | Email | ISM, CISO | Daily |
| High gap open > 20 days | Email | ISM, Owner | Daily |
| Coverage below 95% | Dashboard flag | ISM | Continuous |
| Template legal review due | Email | ISM, Legal | 30 days before |

### 11.2 Data Validation Automation

| Validation | Action | Frequency |
|------------|--------|-----------|
| Review_ID uniqueness | Prevent duplicate | On entry |
| Gap_ID uniqueness | Prevent duplicate | On entry |
| Date format | Auto-format to DD.MM.YYYY | On entry |
| Coverage calculation | Auto-calculate | Real-time |
| Required field completion | Highlight | Real-time |

---

## 12. Metrics and KPIs

### 12.1 Review Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Review completion rate | 100% on schedule | Completed on time / Total | ISM |
| Annual review completion | 100% | Annual review done / Required | ISM |
| Quarterly checks | 4 per year | Checks completed | ISM |

### 12.2 Coverage Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Overall coverage | 100% | Total signed / Total required | ISM |
| Employee coverage | 100% | Employee signed / Employee required | HR |
| Vendor coverage | 100% | Vendor signed / Vendor required | Procurement |

### 12.3 Gap Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Open critical gaps | 0 | Count Critical + Open | ISM |
| Gap closure SLA | >95% | Closed in SLA / Total | ISM |
| Gap trend | Declining | Current - Previous | ISM |

---

## 13. Evidence Package for ISO 27001 Audit

### 13.1 Standard Evidence Package

| Document | Purpose | Preparation |
|----------|---------|-------------|
| Review schedule | Review planning evidence | Export Sheet 2 |
| Template assessment | Template adequacy evidence | Export Sheet 3 |
| Coverage analysis | Coverage verification | Export Sheet 4 |
| Compliance check | Individual NDA compliance | Export Sheet 5 |
| Gap register | Gap management | Export Sheet 6 |
| Approval records | Governance evidence | Export Sheet 8 |

### 13.2 Audit Preparation Checklist

- [ ] Export current review status
- [ ] Generate coverage analysis summary
- [ ] Prepare gap statistics and trends
- [ ] Gather approval evidence
- [ ] Compile template assessment summary
- [ ] Document remediation completion

---

## 14. Generator Script Reference

### 14.1 Script Location

```
10-isms-scr-base/
└── isms-a.6.6-confidentiality-nda/
    └── 10_generator-master/
        └── generate_a66_3_nda_review_compliance.py
```

### 14.2 Script Execution

```bash
cd 10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master
python3 generate_a66_3_nda_review_compliance.py
mv *.xlsx ../90_workbooks/
```

### 14.3 Output

```
ISMS-IMP-A.6.6.3_NDA_Review_and_Compliance_YYYYMMDD.xlsx
```

---

**END OF SPECIFICATION**

---

*"In God we trust; all others must bring data."*
— W. Edwards Deming

<!-- QA_VERIFIED: 2026-02-06 -->
