**ISMS-IMP-A.8.30.1-TG - Vendor Assessment and Registry**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.1-TG |
| **Document Title** | Vendor Assessment and Registry Workbook Specification |
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

This section provides technical details for the Vendor Assessment and Registry workbook implementation, including Excel specifications, data validation rules, and automation requirements.

---

## 9. Workbook Technical Structure

### 9.1 Workbook Properties

| Property | Value |
|----------|-------|
| File Format | .xlsx (Excel 2016+) |
| Sheet Protection | Structure protected, cells unlocked for input |
| Workbook Protection | Structure only (prevent sheet deletion) |
| File Naming | ISMS-IMP-A.8.30.1_Vendor_Assessment_Registry_YYYYMMDD.xlsx |

### 9.2 Sheet Configuration

| Sheet | Tab Colour | Protection Level | Hidden |
|-------|------------|------------------|--------|
| Vendor Registry | Blue (#4472C4) | Input cells unlocked | No |
| Security Assessment | Green (#70AD47) | Input cells unlocked | No |
| Due Diligence Checklist | Orange (#ED7D31) | Input cells unlocked | No |
| Environment Security | Purple (#7030A0) | Input cells unlocked | No |
| Validation Lists | Grey (#A6A6A6) | Full protection | Yes |
| Dashboard | Dark Blue (#002060) | Full protection | No |

---

## 10. Sheet Specifications

### 10.1 Sheet 1: Vendor Registry – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Vendor_ID | 15 | Text | Format: VND-#### | Yes |
| B | Vendor_Name | 40 | Text | Max 200 chars | Yes |
| C | Registry_Status | 15 | List | Approved,Pending,Suspended,Removed | Yes |
| D | Risk_Tier | 12 | List | Critical,High,Standard | Yes |
| E | Initial_Assessment_Date | 15 | Date | DD.MM.YYYY | Yes |
| F | Last_Assessment_Date | 15 | Date | DD.MM.YYYY | Yes |
| G | Next_Assessment_Due | 15 | Date | DD.MM.YYYY, formula | Auto |
| H | ISO_27001_Certified | 12 | List | Yes,No,In Progress | Yes |
| I | SOC2_Type2 | 12 | List | Yes,No,N/A | Yes |
| J | Primary_Contact | 30 | Text | Email format | Yes |
| K | Approved_Project_Types | 25 | Text | Critical,High,Standard (multi) | Yes |
| L | Approved_By | 25 | Text | Name + Role | Yes |
| M | Notes | 50 | Text | Max 500 chars | No |

**Data Validation Rules:**

```excel
Vendor_ID: Custom formula =AND(LEFT(A2,4)="VND-",LEN(A2)=8,ISNUMBER(VALUE(RIGHT(A2,4))))
Registry_Status: List validation from Validation Lists sheet
Risk_Tier: List validation from Validation Lists sheet
Dates: Date validation with Swiss format
Primary_Contact: Custom formula for email pattern
```

**Formulas:**

```excel
Next_Assessment_Due (G2):
=IF(D2="Critical",EDATE(F2,3),IF(D2="High",EDATE(F2,6),EDATE(F2,12)))
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Registry_Status = "Suspended" | Red fill, white text |
| Next_Assessment_Due < TODAY() | Orange fill |
| Next_Assessment_Due < TODAY()+30 | Yellow fill |
| ISO_27001_Certified = "No" AND Risk_Tier = "Critical" | Red border |

### 10.2 Sheet 2: Security Assessment – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Assessment_ID | 15 | Text | Format: ASM-#### | Yes |
| B | Vendor_ID | 15 | Reference | Must exist in Registry | Yes |
| C | Assessment_Date | 15 | Date | DD.MM.YYYY | Yes |
| D | Assessment_Type | 12 | List | Initial,Annual,Triggered | Yes |
| E | Assessor | 20 | Text | Employee name | Yes |
| F | Security_Certification | 15 | List | ISO 27001,SOC 2,Both,None | Yes |
| G | Cert_Expiry_Date | 15 | Date | DD.MM.YYYY | Conditional |
| H | SDLC_Maturity | 15 | List | Mature,Developing,Basic,Unknown | Yes |
| I | Security_Incident_History | 12 | List | None,Minor,Major | Yes |
| J | SAST_DAST_Tooling | 30 | Text | Tool names | Yes |
| K | Personnel_Screening | 15 | List | Verified,Attested,Unknown | Yes |
| L | Dev_Environment_Security | 15 | List | Compliant,Partial,Non-Compliant | Yes |
| M | Overall_Risk_Rating | 12 | List | Low,Medium,High,Critical | Yes |
| N | Recommendation | 15 | List | Approve,Conditional,Reject | Yes |
| O | Conditions | 50 | Text | If conditional | Conditional |
| P | Evidence_Location | 40 | Text | Path/URL | Yes |

**Formulas:**

```excel
Risk Rating Suggestion (helper column):
=IF(AND(F2<>"None",H2="Mature",I2="None",L2="Compliant"),"Low",
 IF(AND(OR(F2<>"None",H2="Mature"),I2<>"Major",L2<>"Non-Compliant"),"Medium",
 IF(I2="Major","Critical","High")))
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Recommendation = "Reject" | Red fill |
| Recommendation = "Conditional" | Yellow fill |
| Overall_Risk_Rating = "Critical" | Red text, bold |
| Cert_Expiry_Date < TODAY()+60 | Orange fill |

### 10.3 Sheet 3: Due Diligence Checklist – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Vendor_ID | 15 | Reference | Must exist in Registry | Yes |
| B | Check_Category | 25 | Text | Category name | Yes |
| C | Check_Item | 50 | Text | Check description | Yes |
| D | Status | 12 | List | Complete,Pending,N/A | Yes |
| E | Evidence_Type | 15 | List | Certificate,Attestation,Document,Interview | Conditional |
| F | Evidence_Reference | 40 | Text | File path/URL | Conditional |
| G | Verified_By | 20 | Text | Name | Conditional |
| H | Verified_Date | 15 | Date | DD.MM.YYYY | Conditional |
| I | Notes | 40 | Text | Optional | No |

**Pre-populated Categories (50 rows per vendor):**

| Category | Check Items Count |
|----------|-------------------|
| 1. Security Certification Verification | 5 |
| 2. Secure Development Practices | 5 |
| 3. Security Incident History | 4 |
| 4. Technical Security Capabilities | 4 |
| 5. Personnel Security | 4 |
| 6. Physical Security | 4 |
| 7. Subcontractor Management | 4 |
| 8. Business Continuity | 4 |
| 9. Insurance Coverage | 3 |
| 10. Reference Checks | 3 |

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Status = "Complete" | Green fill |
| Status = "Pending" | Yellow fill |
| Status = "N/A" | Grey fill |

### 10.4 Sheet 4: Environment Security Assessment – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Vendor_ID | 15 | Reference | Must exist in Registry | Yes |
| B | Assessment_Date | 15 | Date | DD.MM.YYYY | Yes |
| C | MFA_Enabled | 12 | List | Yes,Partial,No | Yes |
| D | Network_Isolation | 12 | List | Isolated,Segmented,Shared | Yes |
| E | Endpoint_Security | 15 | List | Compliant,Partial,Non-Compliant | Yes |
| F | Code_Repository | 15 | List | Secure,Partial,Unsecure | Yes |
| G | Secret_Scanning | 12 | List | Yes,No | Yes |
| H | Branch_Protection | 12 | List | Yes,Partial,No | Yes |
| I | Data_Handling | 20 | List | No Prod Data,Masked,Raw (Non-Compliant) | Yes |
| J | Attestation_Received | 12 | List | Yes,No | Yes |
| K | Attestation_Date | 15 | Date | DD.MM.YYYY | Conditional |
| L | Compliance_Status | 15 | List | Compliant,Conditional,Non-Compliant | Yes |

**Formulas:**

```excel
Compliance Score (helper column):
=COUNTIF(C2:I2,"Yes")+COUNTIF(C2:I2,"Compliant")+COUNTIF(C2:I2,"Isolated")+COUNTIF(C2:I2,"Secure")+COUNTIF(I2,"No Prod Data")

Suggested Compliance Status:
=IF(Compliance_Score>=6,"Compliant",IF(Compliance_Score>=4,"Conditional","Non-Compliant"))
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Data_Handling = "Raw (Non-Compliant)" | Red fill, bold |
| Compliance_Status = "Non-Compliant" | Red fill |
| MFA_Enabled = "No" | Orange fill |

---

## 11. Data Sources and Integration

### 11.1 Data Source Mapping

| Data Element | Source System | Collection Method | Update Frequency |
|--------------|---------------|-------------------|------------------|
| Vendor legal information | Procurement/ERP | Manual entry | Per engagement |
| Certification status | Certification bodies | Manual verification | Quarterly |
| Assessment responses | Security questionnaire platform | Export/Import | Per assessment |
| Environment evidence | Vendor submission | File upload | Per assessment |
| Reference feedback | Direct contact | Manual entry | Per assessment |

### 11.2 Import/Export Specifications

**Import Format (CSV):**

```csv
Vendor_ID,Vendor_Name,Registry_Status,Risk_Tier,Initial_Assessment_Date,Last_Assessment_Date,...
VND-0001,Acme Development AG,Approved,High,15.01.2026,15.01.2026,...
```

**Export Format for Reporting:**

| Report | Format | Frequency | Recipient |
|--------|--------|-----------|-----------|
| Approved Vendor List | Excel/PDF | Monthly | Procurement, Project Managers |
| Assessment Summary | Excel | Per assessment | Assessment requestor |
| Compliance Dashboard | Excel/PowerBI | Weekly | CISO, Management |
| Audit Evidence Package | Excel + PDFs | Per audit | External Auditors |

---

## 12. Automation Requirements

### 12.1 Automated Alerts

| Trigger | Alert Type | Recipients | Timing |
|---------|------------|------------|--------|
| Certification expiry approaching | Email | IT Security, Vendor Contact | 60, 30, 7 days before |
| Reassessment due | Email | IT Security Assessor | 30, 14, 7 days before |
| Reassessment overdue | Email + Dashboard flag | CISO, IT Security Manager | Daily until resolved |
| Vendor status changed to Suspended | Email | Procurement, Active Project Managers | Immediate |
| New vendor pending assessment | Email | IT Security Assessor | Daily digest |

### 12.2 Data Validation Automation

| Validation | Action | Frequency |
|------------|--------|-----------|
| Vendor_ID uniqueness | Prevent duplicate | On entry |
| Date format | Auto-format to DD.MM.YYYY | On entry |
| Required field completion | Highlight incomplete | Real-time |
| Cross-reference validation | Verify Vendor_ID exists | On entry |
| Email format validation | Validate pattern | On entry |

### 12.3 Dashboard Automation

| Metric | Calculation | Refresh |
|--------|-------------|---------|
| Total approved vendors | COUNT where Status=Approved | Daily |
| Assessments pending | COUNT where Status=Pending | Daily |
| Overdue reassessments | COUNT where Next_Due < TODAY | Daily |
| High/Critical risk vendors | COUNT where Risk_Tier IN (Critical,High) | Daily |
| Certification coverage | Certified / Total Approved | Weekly |

---

## 13. Metrics and KPIs

### 13.1 Operational Metrics

| Metric | Target | Formula | Owner |
|--------|--------|---------|-------|
| Assessment completion rate | 100% before engagement | Completed / Required | IT Security |
| Assessment SLA compliance | 100% within SLA | On-time / Total | IT Security |
| Registry accuracy | 100% current | Current assessments / Total approved | IT Security |
| Reassessment timeliness | 100% on schedule | On-time reassessments / Due | IT Security |
| High-risk vendor review | 100% quarterly | Reviewed / High-risk total | CISO |

### 13.2 Compliance Metrics

| Metric | Target | Measurement | Reporting |
|--------|--------|-------------|-----------|
| Vendor certification rate | >80% | Certified vendors / Total | Quarterly |
| Due diligence completion | 100% | Complete checks / Required | Per assessment |
| Conditional approval closure | 100% within 90 days | Closed conditions / Total conditions | Monthly |
| Audit finding rate | 0 major findings | Major findings count | Per audit |

### 13.3 Risk Metrics

| Metric | Threshold | Action Trigger | Escalation |
|--------|-----------|----------------|------------|
| Critical vendors without certification | 0 | Immediate | CISO |
| Overdue reassessments | <5% | Weekly review | IT Security Manager |
| Rejected vendors re-engaging | 0 | Immediate | CISO |
| Vendor incidents | Any Major | Triggered assessment | CISO |

---

## 14. Evidence Package for ISO 27001 Audit

### 14.1 Standard Evidence Package Contents

| Document | Purpose | Preparation |
|----------|---------|-------------|
| Approved Vendor Registry | Current approved vendors | Export Sheet 1 |
| Assessment Summary Report | Assessment statistics | Dashboard export |
| Sample Vendor Files (3-5) | Detailed assessment evidence | Complete vendor folders |
| Due Diligence Checklists | Verification evidence | Sheet 3 exports with evidence |
| Procedure Documentation | Process evidence | This IMP document |
| Training Records | Competence evidence | Training system export |

### 14.2 Audit Preparation Checklist

- [ ] Export current Vendor Registry
- [ ] Verify all evidence links are valid
- [ ] Prepare sample vendor packages for each risk tier
- [ ] Generate assessment statistics report
- [ ] Confirm all overdue items addressed or documented
- [ ] Review procedure documentation currency
- [ ] Prepare assessor interview availability

---

## 15. Generator Script Reference

### 15.1 Script Location

```
10-isms-scr-base/
└── isms-a.8.30-outsourced-development/
    └── 10_generator-master/
        └── generate_a830_1_vendor_assessment.py
```

### 15.2 Script Execution

```bash
cd 10-isms-scr-base/isms-a.8.30-outsourced-development/10_generator-master
python3 generate_a830_1_vendor_assessment.py
mv *.xlsx ../90_workbooks/
```

### 15.3 Output

```
ISMS-IMP-A.8.30.1_Vendor_Assessment_Registry_YYYYMMDD.xlsx
```

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
