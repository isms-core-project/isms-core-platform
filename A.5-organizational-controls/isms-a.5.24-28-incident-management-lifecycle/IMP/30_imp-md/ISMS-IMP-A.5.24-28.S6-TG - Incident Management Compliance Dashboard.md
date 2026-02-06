**ISMS-IMP-A.5.24-28.S6-TG - Incident Management Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.24-28: Incident Management Lifecycle

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Incident Management Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S6-TG |
| **Assessment Domain** | Domain 6 - Compliance Dashboard (Consolidated) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Incident Response Team Lead / CSIRT Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial compliance dashboard specification |

**Review Cycle**: Annual (or after significant incident management changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S1 (Framework Assessment - A.5.24)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment - A.5.25)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment - A.5.26)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment - A.5.28)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment - A.5.27)
- ISO/IEC 27002:2022 Controls A.5.24-28
- NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)
- ISO/IEC 27035-1:2023 (Incident Management Principles)

---

# Technical Specification

# Workbook Structure

## Sheet Summary

| Sheet # | Sheet Name | Purpose | Rows | Key Features |
|---------|------------|---------|------|--------------|
| 1 | Instructions | User guidance | ~60 | Read-only, colour legend |
| 2 | Executive_Summary | Management overview | ~50 | KPIs, heat map, recommendations |
| 3 | Compliance_Scores | Control breakdown | ~80 | Per-control scoring, weightings |
| 4 | Gap_Analysis | Gap inventory | ~120 | 100 gap capacity, aging calculation |
| 5 | Incident_KPIs | Operational metrics | ~80 | Trend data, target comparison |
| 6 | Evidence_Register | Evidence tracking | ~120 | 100 evidence items, status tracking |
| 7 | Approval_Sign_Off | Approval workflow | ~50 | Signature fields, distribution |

## Column Specifications

### Sheet 1: Instructions

| Column | Width | Content |
|--------|-------|---------|
| A | 25 | Labels |
| B | 60 | Content/Instructions |
| C | 20 | Notes |

### Sheet 2: Executive_Summary

| Column | Width | Content |
|--------|-------|---------|
| A | 35 | Metric names |
| B | 15 | Current values |
| C | 15 | Targets |
| D | 15 | Status (traffic light) |
| E | 15 | Trend |
| F | 25 | Notes |

### Sheet 3: Compliance_Scores

| Column | Width | Content |
|--------|-------|---------|
| A | 12 | Control ID |
| B | 35 | Control Name |
| C | 25 | Domain |
| D | 10 | Weight |
| E | 12 | Score |
| F | 12 | Status |
| G | 35 | Source Reference |
| H | 35 | Notes |

### Sheet 4: Gap_Analysis

| Column | Width | Content |
|--------|-------|---------|
| A | 15 | Gap_ID |
| B | 12 | Source |
| C | 12 | Control |
| D | 20 | Domain |
| E | 40 | Gap_Description |
| F | 10 | Severity |
| G | 25 | Impact |
| H | 25 | Root_Cause |
| I | 30 | Remediation_Action |
| J | 18 | Owner |
| K | 12 | Status |
| L | 12 | Due_Date |
| M | 10 | Days_Open |
| N | 20 | Evidence |
| O | 30 | Notes |

### Sheet 5: Incident_KPIs

| Column | Width | Content |
|--------|-------|---------|
| A | 35 | KPI Name |
| B | 15 | Current Value |
| C | 15 | Target |
| D | 15 | Status |
| E | 15 | Trend |
| F | 12 | Period |
| G | 30 | Notes |

### Sheet 6: Evidence_Register

| Column | Width | Content |
|--------|-------|---------|
| A | 18 | Evidence_ID |
| B | 35 | Source_Workbook |
| C | 12 | Control |
| D | 20 | Domain |
| E | 40 | Evidence_Description |
| F | 15 | Evidence_Type |
| G | 40 | Storage_Location |
| H | 12 | Date_Collected |
| I | 18 | Collected_By |
| J | 15 | Verification_Status |
| K | 12 | Last_Verified |
| L | 12 | Expiry_Date |
| M | 30 | Notes |

### Sheet 7: Approval_Sign_Off

| Column | Width | Content |
|--------|-------|---------|
| A | 25 | Field labels |
| B | 25 | Values |
| C | 20 | Status/Date |
| D | 30 | Signature/Notes |

---

# Cell Styling

## Colour Palette

| Colour Name | Hex Code | Usage |
|-------------|----------|-------|
| Navy (Header) | #003366 | Sheet titles, primary headers |
| Blue (Subheader) | #4472C4 | Section headers |
| Light Blue (Section) | #D8E4F8 | Section breaks |
| Grey (Column Header) | #D9D9D9 | Column headers |
| Yellow (Input) | #FFFFCC | User input cells |
| Green (Good) | #C6EFCE | Compliant/passing metrics |
| Amber (Warning) | #FFEB9C | Partial compliance/warning |
| Red (Bad) | #FFC7CE | Non-compliant/critical |
| White (Read-only) | #FFFFFF | Information/labels |

## Font Specifications

| Element | Font | Size | Bold | Colour |
|---------|------|------|------|--------|
| Sheet Title | Calibri | 14 | Yes | White |
| Section Header | Calibri | 12 | Yes | White/Black |
| Column Header | Calibri | 10 | Yes | Black |
| Body Text | Calibri | 10 | No | Black |
| KPI Value | Calibri | 12 | Yes | Black |

## Border Specifications

| Border Type | Style | Colour | Usage |
|-------------|-------|--------|-------|
| Thin | Solid 1pt | Black (#000000) | All data cells |
| None | - | - | Merged header cells |

## Alignment

| Content Type | Horizontal | Vertical | Wrap Text |
|--------------|------------|----------|-----------|
| Headers | Centre | Centre | Yes |
| Labels | Left | Centre | Yes |
| Numbers | Centre | Centre | No |
| Descriptions | Left | Top | Yes |
| Dates | Centre | Centre | No |

---

# Data Validation

## Dropdown Lists

### Control Dropdown (Sheet 3, 4, 6)

```
A.5.24,A.5.25,A.5.26,A.5.27,A.5.28
```

### Source Dropdown (Sheet 4, 6)

```
S1-Framework,S2-Detection,S3-Response,S4-Forensic,S5-Learning
```

### Severity Dropdown (Sheet 4)

```
Critical,High,Medium,Low
```

### Status Dropdown (Gaps) (Sheet 4)

```
Open,In Progress,Closed
```

### Verification Status Dropdown (Sheet 6)

```
Verified,Pending,Expired
```

### Evidence Type Dropdown (Sheet 6)

```
Document,Screenshot,Record,Attestation
```

### Trend Dropdown (Sheet 2, 5)

```
▲ Improving,▬ Stable,▼ Declining
```

### Status (Traffic Light) Dropdown (Sheet 2, 3, 5)

```
GREEN - Compliant,AMBER - Partial,RED - Non-Compliant
```

---

# Formulas

## Overall Compliance Score (Sheet 2)

```excel
=ROUND((B_A524*0.25 + B_A525*0.20 + B_A526*0.25 + B_A527*0.15 + B_A528*0.15), 1)

Where:
B_A524 = 'Compliance_Scores'!E[A.5.24 Total Row]
B_A525 = 'Compliance_Scores'!E[A.5.25 Total Row]
B_A526 = 'Compliance_Scores'!E[A.5.26 Total Row]
B_A527 = 'Compliance_Scores'!E[A.5.27 Total Row]
B_A528 = 'Compliance_Scores'!E[A.5.28 Total Row]
```

## Status Traffic Light (Sheet 2, 3, 5)

```excel
=IF(B5>=90,"GREEN - Compliant",IF(B5>=75,"AMBER - Partial","RED - Non-Compliant"))
```

## Gap Aging (Sheet 4, Column M)

```excel
=IF(K5="Closed","N/A",DATEDIF(DATE(LEFT(A5,4),MID(A5,6,2),RIGHT(A5,2)),TODAY(),"D"))

Alternative (if no open date in Gap_ID):
=IF(K5="Closed","N/A",TODAY()-L5)
```

## Gap Count by Severity (Sheet 2)

```excel
Critical Gaps = COUNTIFS('Gap_Analysis'!F:F,"Critical",'Gap_Analysis'!K:K,"<>Closed")
High Gaps = COUNTIFS('Gap_Analysis'!F:F,"High",'Gap_Analysis'!K:K,"<>Closed")
Medium Gaps = COUNTIFS('Gap_Analysis'!F:F,"Medium",'Gap_Analysis'!K:K,"<>Closed")
Low Gaps = COUNTIFS('Gap_Analysis'!F:F,"Low",'Gap_Analysis'!K:K,"<>Closed")
```

## Evidence Currency Check (Sheet 6)

```excel
=IF(K5="","",IF(TODAY()-K5>365,"EXPIRED",IF(TODAY()-K5>300,"DUE SOON","CURRENT")))
```

## KPI Status (Sheet 5)

```excel
=IF(B5="","",IF(VALUE(B5)<=VALUE(C5),"GREEN - Met",IF(VALUE(B5)<=VALUE(C5)*1.2,"AMBER - Warning","RED - Critical")))
```

---

# Conditional Formatting

## Compliance Score Cells (Sheet 2, 3)

| Condition | Format |
|-----------|--------|
| Value ≥ 90 | Green fill (#C6EFCE) |
| Value 75-89 | Amber fill (#FFEB9C) |
| Value < 75 | Red fill (#FFC7CE) |

## Gap Severity (Sheet 4, Column F)

| Value | Format |
|-------|--------|
| "Critical" | Red fill (#FFC7CE) |
| "High" | Orange fill (#FFD9B3) |
| "Medium" | Amber fill (#FFEB9C) |
| "Low" | Green fill (#C6EFCE) |

## Gap Status (Sheet 4, Column K)

| Value | Format |
|-------|--------|
| "Open" | Red fill (#FFC7CE) |
| "In Progress" | Amber fill (#FFEB9C) |
| "Closed" | Green fill (#C6EFCE) |

## Days Open (Sheet 4, Column M)

| Condition | Format |
|-----------|--------|
| >90 days | Red fill (#FFC7CE), Bold |
| 60-90 days | Orange fill (#FFD9B3) |
| 30-59 days | Amber fill (#FFEB9C) |
| <30 days | No special formatting |

## Evidence Verification (Sheet 6, Column J)

| Value | Format |
|-------|--------|
| "Verified" | Green fill (#C6EFCE) |
| "Pending" | Amber fill (#FFEB9C) |
| "Expired" | Red fill (#FFC7CE) |

---

# Sheet Protection

## Protection Settings

| Sheet | Protected | Unlocked Cells |
|-------|-----------|----------------|
| Instructions | Yes (no password) | None |
| Executive_Summary | Yes (no password) | Input cells (yellow) |
| Compliance_Scores | Yes (no password) | Input cells (yellow), Notes |
| Gap_Analysis | Yes (no password) | All data entry rows |
| Incident_KPIs | Yes (no password) | All data entry rows |
| Evidence_Register | Yes (no password) | All data entry rows |
| Approval_Sign_Off | Yes (no password) | All input fields |

## Locked Cells

- All calculated cells
- Headers and labels
- Formula cells
- Instructions text

---

# File Naming Convention

**Format:** `ISMS-IMP-A.5.24-28.S6_Compliance_Dashboard_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.24-28.S6_Compliance_Dashboard_20260203.xlsx`

---

# Excel Version Compatibility

**Target Version:** Excel 2016 or later (Windows/Mac), Office 365

**Features Used:**

- Data Validation (dropdown lists)
- Conditional Formatting (colour scales, rules)
- Named Ranges
- Cell Protection
- Basic formulas (IF, COUNTIF, COUNTIFS, SUMIF, DATEDIF)

**Compatibility Notes:**

- All formulas compatible with Excel 2016+
- Conditional Formatting tested for Excel 2016 compatibility
- No Power Query or Pivot Tables (keep simple for broad compatibility)
- DATEDIF function may not appear in function wizard but is supported

---

# Workbook Generation Script Template

**Python Script:** `generate_a524_28_s6_compliance_dashboard.py`

**Libraries:**

- `openpyxl` (Excel file creation and manipulation)
- `datetime` (date handling)
- `logging` (standard logging)

**Script Structure:**

1. Create workbook
2. Create sheets (Instructions, Executive_Summary, Compliance_Scores, Gap_Analysis, Incident_KPIs, Evidence_Register, Approval_Sign_Off)
3. Set column widths
4. Create headers with styling
5. Add data validation (dropdowns)
6. Add conditional formatting
7. Add formulas (compliance scoring, gap aging, KPI status)
8. Protect sheets (leave input cells unlocked)
9. Save workbook with timestamp

**Script Length:** ~600-800 lines (comprehensive header documentation + implementation)

---

# Source Data References

## S1-S5 Workbook References

| Source | Workbook Name | Key Sheets | Data Elements |
|--------|---------------|------------|---------------|
| S1 | ISMS-IMP-A.5.24-28.S1_Framework_Assessment | Dashboard, Gap Analysis | A.5.24 compliance scores, governance gaps |
| S2 | ISMS-IMP-A.5.24-28.S2_Detection_Classification | Dashboard, Gap Analysis | A.5.25 compliance scores, detection gaps |
| S3 | ISMS-IMP-A.5.24-28.S3_Response_Capabilities | Dashboard, Gap Analysis | A.5.26 compliance scores, response gaps |
| S4 | ISMS-IMP-A.5.24-28.S4_Forensic_Evidence | Dashboard, Gap Analysis | A.5.28 compliance scores, evidence gaps |
| S5 | ISMS-IMP-A.5.24-28.S5_Learning_Improvement | Dashboard, Gap Analysis | A.5.27 compliance scores, learning gaps |

## External Data Sources

| Data Element | Source System | Refresh Frequency |
|--------------|---------------|-------------------|
| Incident counts | Incident ticketing system | Quarterly |
| MTTD/MTTR metrics | SIEM/SOAR platform | Quarterly |
| Training completion | LMS/HR system | Quarterly |
| Exercise data | Exercise management system | Per exercise |

---

**END OF SPECIFICATION**

---

*"The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards."*
— Gene Spafford

<!-- QA_VERIFIED: 2026-02-06 -->
