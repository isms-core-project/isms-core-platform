**ISMS-IMP-A.5.4.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.5-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification

### 11. Excel Workbook Structure

#### 11.1 Sheet Overview

| # | Sheet Name | Purpose | Rows | Key Features |
|---|------------|---------|------|--------------|
| 1 | Instructions | User guidance | ~40 | Read-only |
| 2 | Executive_Summary | High-level status | ~25 | Domain status table, KPI metrics |
| 3 | Compliance_KPIs | KPI tracking | ~20 | Pre-populated KPIs, data validation |
| 4 | Compliance_Scorecard | Requirement scoring | ~20 | Weighted scoring, gap linkage |
| 5 | Gap_Analysis | Gap remediation | ~30 | Risk levels, progress tracking |
| 6 | Audit_Readiness | Evidence checklist | ~20 | Pre-populated checks |
| 7 | Trend_Analysis | Historical trends | ~10 | Quarterly periods |
| 8 | Evidence_Register | Evidence tracking | ~30 | Storage locations, retention |
| 9 | Approval_SignOff | Approval workflow | ~20 | Signature table, declaration |

### 12. Sheet Specifications

#### 12.1 Instructions Sheet

**Purpose**: Provide user guidance and document metadata

**Content Structure**:
```
Row 1: Document title (ISMS-IMP-A.5.4.5 - Management Responsibilities Compliance Dashboard)
Rows 3-5: Purpose statement
Rows 7-14: Source workbooks listing
Rows 16-25: Sheet descriptions
Rows 27-31: Compliance scoring methodology
Rows 33-36: Refresh frequency guidance
Row 38-39: Document metadata (generated date, control reference)
```

**Formatting**:
- Column A width: 90
- Title: Bold 14pt
- Section headers: Bold 11pt

#### 12.2 Executive_Summary Sheet

**Header Row** (Row 6):

| Column | Header | Width | Notes |
|--------|--------|:-----:|-------|
| A | Assessment Domain | 40 | |
| B | Workbook | 20 | |
| C | Status | 15 | Data validation |
| D | Score % | 18 | Input (yellow) |
| E | Key Issues | 12 | Input (yellow) |

**Pre-Populated Domains** (Rows 7-11):
1. Management Commitment (A.5.4.1)
2. Compliance Oversight (A.5.4.2)
3. Leadership Metrics (A.5.4.3)
4. Security Culture (A.5.4.4)
5. OVERALL A.5.4 (Consolidated) - bold

**Key Metrics Section** (Row 14+):

| Column | Header | Width |
|--------|--------|:-----:|
| A | Metric | 40 |
| B | Target | 20 |
| C | Current | 15 |
| D | Status | 18 |
| E | Trend | 12 |

**Data Validations**:
- Status (C7:C11): "Compliant,Partially Compliant,Non-Compliant"

#### 12.3 Compliance_KPIs Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | KPI_ID | 15 | |
| B | KPI_Name | 28 | |
| C | Description | 45 | |
| D | Target | 12 | |
| E | Current_Value | 15 | ✓ |
| F | Measurement_Method | 35 | |
| G | Frequency | 12 | |
| H | Data_Source | 25 | |
| I | Owner | 18 | |
| J | Status | 12 | ✓ |
| K | Trend | 12 | ✓ |
| L | Comments | 30 | ✓ |

**Pre-Populated KPIs** (Rows 2-8):
- A54-KPI-001 through A54-KPI-007 as specified in Section 5

**Data Validations**:
- Status (J2:J20): "On Target,At Risk,Below Target"
- Trend (K2:K20): "Improving,Stable,Declining"
- Frequency (G2:G20): "Monthly,Quarterly,Semi-annual,Annual"

#### 12.4 Compliance_Scorecard Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Requirement_ID | 12 | |
| B | Requirement | 50 | |
| C | Source | 10 | |
| D | Weight | 8 | |
| E | Evidence_Available | 18 | ✓ |
| F | Implementation_Status | 22 | ✓ |
| G | Score | 8 | ✓ |
| H | Max_Score | 10 | |
| I | Gap_Description | 35 | ✓ |
| J | Remediation_Status | 18 | ✓ |

**Pre-Populated Requirements** (Rows 2-11):
- REQ-001 through REQ-010 as specified in Section 5

**Data Validations**:
- Evidence_Available (E2:E20): "Yes,Partial,No"
- Implementation_Status (F2:F20): "Fully Implemented,Partially Implemented,Not Implemented,Not Applicable"
- Remediation_Status (J2:J20): "Not Required,In Progress,Planned,Completed"

#### 12.5 Gap_Analysis Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Gap_ID | 10 | ✓ |
| B | Requirement_Reference | 18 | ✓ |
| C | Gap_Description | 40 | ✓ |
| D | Risk_Level | 10 | ✓ |
| E | Root_Cause | 30 | ✓ |
| F | Remediation_Action | 40 | ✓ |
| G | Owner | 18 | ✓ |
| H | Target_Date | 12 | ✓ |
| I | Status | 12 | ✓ |
| J | Progress | 10 | ✓ |
| K | Evidence_of_Closure | 25 | ✓ |
| L | Notes | 30 | ✓ |

**Data Validations**:
- Risk_Level (D2:D30): "Critical,High,Medium,Low"
- Status (I2:I30): "Open,In Progress,Closed,Deferred"
- Progress (J2:J30): "0%,25%,50%,75%,100%"

#### 12.6 Audit_Readiness Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Check_ID | 10 | |
| B | Audit_Requirement | 38 | |
| C | Evidence_Required | 35 | |
| D | Evidence_Location | 30 | ✓ |
| E | Evidence_Available | 18 | ✓ |
| F | Last_Reviewed | 15 | ✓ |
| G | Reviewer | 18 | ✓ |
| H | Status | 18 | ✓ |
| I | Notes | 30 | ✓ |

**Pre-Populated Checks** (Rows 2-11):
- AUD-001 through AUD-010 as specified in Section 5

**Data Validations**:
- Evidence_Available (E2:E20): "Yes,Partial,No"
- Status (H2:H20): "Ready,Action Required,Not Applicable"

#### 12.7 Trend_Analysis Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Period | 12 | |
| B | Commitment_Score | 18 | ✓ |
| C | Training_Compliance | 20 | ✓ |
| D | Violation_Response | 20 | ✓ |
| E | Access_Review_Rate | 18 | ✓ |
| F | Culture_Score | 15 | ✓ |
| G | Overall_Score | 15 | ✓ |
| H | Key_Changes | 35 | ✓ |
| I | Notes | 30 | ✓ |

**Pre-Populated Periods** (Rows 2-9):
- Q1 2025 through Q4 2026

#### 12.8 Evidence_Register Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Evidence_ID | 12 | ✓ |
| B | Evidence_Type | 20 | ✓ |
| C | Description | 40 | ✓ |
| D | Related_Requirement | 18 | ✓ |
| E | Date_Created | 15 | ✓ |
| F | Created_By | 20 | ✓ |
| G | Storage_Location | 40 | ✓ |
| H | Retention_Period | 15 | ✓ |
| I | Review_Date | 15 | ✓ |
| J | Status | 15 | ✓ |
| K | Notes | 30 | ✓ |

**Data Validations**:
- Evidence_Type (B2:B50): "Assessment Record,Training Record,Violation Record,Review Record,Survey Results,Approval Record,Other"
- Status (J2:J50): "Current,Archived,Pending Review"

#### 12.9 Approval_SignOff Sheet

**Title Section** (Row 1):
- Merged A1:F1
- Title: "A.5.4 Compliance Dashboard - Approval & Sign-Off"
- Dark blue fill, white bold 16pt font

**Assessment Details** (Rows 3-5):
- Assessment Period (B3)
- Assessment Date (B4)
- Prepared By (B5)

**Approval Table** (Row 8+):

| Column | Header | Width |
|--------|--------|:-----:|
| A | Role | 35 |
| B | Name | 25 |
| C | Date | 15 |
| D | Signature | 20 |
| E | Comments | 40 |

**Pre-Populated Roles**:
1. Prepared By (Security Analyst)
2. Reviewed By (Security Manager)
3. Validated By (HR Director)
4. Approved By (CISO)

**Declaration** (Below approval table):
Merged cells with declaration text confirming accuracy and completeness.

### 13. Styling Specifications

#### 13.1 Colour Palette

| Element | Hex Code | RGB | Usage |
|---------|----------|-----|-------|
| Header Fill | #2F5496 | 47,84,150 | Column headers |
| Title Fill | #1F4E79 | 31,78,121 | Sheet titles |
| Input Fill | #FFFFCC | 255,255,204 | User input cells |
| Calculated Fill | #E2EFDA | 226,239,218 | Formula cells |
| Compliant Fill | #C6EFCE | 198,239,206 | Green status |
| Partial Fill | #FFEB9C | 255,235,156 | Amber status |
| Non-Compliant Fill | #FFC7CE | 255,199,206 | Red status |

#### 13.2 Font Specifications

| Element | Font | Size | Style | Colour |
|---------|------|:----:|-------|--------|
| Title | Calibri | 16pt | Bold | White |
| Section Header | Calibri | 12pt | Bold | #1F4E79 |
| Column Header | Calibri | 11pt | Bold | White |
| Data Cell | Calibri | 11pt | Regular | Black |
| Instructions | Calibri | 11pt | Regular | Black |

#### 13.3 Border Style

All data cells use thin black borders on all sides.

### 14. Generator Script Reference

**Script**: `generate_a54_5_compliance_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.4-management-responsibilities/10_generator-master/`

**Output**: `ISMS-IMP-A.5.4.5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.4-management-responsibilities/10_generator-master
python3 generate_a54_5_compliance_dashboard.py
mv *.xlsx ../90_workbooks/
```

**Dependencies**:
- Python 3.8+
- openpyxl

### 15. Integration Points

#### 15.1 Source Workbook Dependencies

| Source | Sheet | Data Extracted |
|--------|-------|----------------|
| A.5.4.1 | Summary_Scores | Overall commitment score |
| A.5.4.1 | Manager_Assessments | Managers meeting threshold |
| A.5.4.2 | Training_Oversight | Compliance percentages |
| A.5.4.2 | Policy_Violations | Response times |
| A.5.4.2 | Access_Reviews | Completion rates |
| A.5.4.2 | Escalation_Triggers | Trigger counts |
| A.5.4.3 | Department_Metrics | Departmental scores |
| A.5.4.4 | Response_Data | Culture scores by category |

#### 15.2 Downstream Consumers

| Consumer | Usage |
|----------|-------|
| Management Review | Quarterly compliance reporting |
| Internal Audit | Pre-audit evidence verification |
| External Audit | Stage 2 audit evidence |
| CISO Dashboard | Executive compliance summary |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
