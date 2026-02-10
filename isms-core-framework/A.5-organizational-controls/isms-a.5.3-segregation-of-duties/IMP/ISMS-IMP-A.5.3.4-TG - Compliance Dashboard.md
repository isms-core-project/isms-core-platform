<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.3.4-TG:framework:TG:a.5.3.4 -->
**ISMS-IMP-A.5.3.4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.4-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.3 Segregation of Duties |
| **Parent Policy** | ISMS-POL-A.5.3 - Segregation of Duties |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.3.4-UG.

---

# Technical Specification


> Auto-generated from `generate_a53_4_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.3.4` |
| **Output Filename** | `ISMS-IMP-A.5.3.4_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Executive_Dashboard

**Data Rows:** 6 (rows 20–25)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Target |
| C | Current |
| D | Status |

---

## Sheet 2: KPI_Scorecard

**Data Rows:** 4 (rows 3–6)

### Columns

| Col | Header |
|-----|--------|
| A | KPI_Name |
| B | Target |
| C | Q1 |
| D | Q2 |
| E | Q3 |
| F | Q4 |
| G | YTD |
| H | Status |
| I | Trend |

---

## Sheet 3: Conflict_Status

**Data Rows:** 7 (rows 1–7)

---

## Sheet 4: Remediation_Progress

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Remediation_ID |
| B | Gap_ID |
| C | Owner |
| D | Target_Date |
| E | Status |
| F | Days_Remaining |
| G | Escalation_Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E100 | `status_dv` |

---

## Sheet 5: Exception_Monitoring

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Exception_ID |
| B | Gap_ID |
| C | Justification |
| D | Compensating_Controls |
| E | Expiry_Date |
| F | Days_Until_Expiry |
| G | Last_Review |
| H | Control_Effective |
| I | Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H2:H100 | `eff_dv` |
| I | I2:I100 | `status_dv` |

---

## Sheet 6: Trend_Analysis

**Data Rows:** 6 (rows 2–7)

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Total_Conflicts |
| C | Critical_Conflicts |
| D | Resolved_Count |
| E | MTTR_Days |
| F | Compliance_Pct |
| G | Exceptions_Active |
| H | Trend_vs_Prior |

---

## Sheet 7: Department_View

**Data Rows:** 4 (rows 2–5)

### Columns

| Col | Header |
|-----|--------|
| A | Department |
| B | Total_Roles |
| C | Conflicts_Identified |
| D | Conflicts_Resolved |
| E | Active_Exceptions |
| F | Compliance_Pct |
| G | Status |

---

## Sheet 8: Audit_Evidence

**Data Rows:** 49 (rows 2–50)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_Item |
| B | Document_ID |
| C | Location |
| D | Date |
| E | Status |
| F | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E50 | `status_dv` |

---

## Sheet 9: Data_Sources

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Source_Name |
| B | Document_ID |
| C | File_Location |
| D | Last_Refresh |
| E | Refresh_Frequency |
| F | Responsible_Party |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E20 | `freq_dv` |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `DEPARTMENTS` | Executive, Finance, IT, Operations, HR, Legal, Sales, Marketing, Engineering, Support, Procuremen... |
| `EVIDENCE_STATUSES` | Ready, In Progress, Missing |
| `EXCEPTION_CONTROL_STATUS` | Yes, No, Partial |
| `KPI_NAMES` | Conflict Identification Rate, Resolution Rate, Mean Time to Resolution (days), Exception Ratio, C... |
| `REFRESH_FREQUENCIES` | Daily, Weekly, Monthly, Quarterly |
| `REMEDIATION_STATUSES` | Not Started, In Progress, Completed, Cancelled, Overdue |

---

**END OF SPECIFICATION**

---

*"You can't manage what you don't measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
