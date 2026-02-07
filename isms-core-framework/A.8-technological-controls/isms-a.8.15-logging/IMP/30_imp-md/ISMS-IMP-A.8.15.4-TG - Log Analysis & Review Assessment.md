**ISMS-IMP-A.8.15.4-TG - Log Analysis & Review Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Log Analysis, Review Process, Threat Detection & SOC Effectiveness |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.4 (Log Review & Analysis Requirements), Section 2.1 (Event Logging Requirements) |
| **Purpose** | Assess log review process effectiveness, SIEM use case maturity, alert management, SOC performance metrics, threat detection coverage |
| **Target Audience** | Security Operations Center (SOC), Threat Detection Team, Security Engineers, InfoSec Manager, CISO, Incident Response Team, Auditors, Workbook Developers |
| **Assessment Type** | Operational Effectiveness & Process Maturity |
| **Review Cycle** | Quarterly (full assessment), Monthly (SOC metrics review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook Developers (Python/Excel script maintainers)


> Auto-generated from `generate_a815_4_log_analysis_review.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.15.4` |
| **Output Filename** | `ISMS-IMP-A.8.15.4_Log_Analysis_Review_YYYYMMDD.xlsx` |
| **Total Sheets** | 24 (24 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.15: Logging |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #E7E6E6 | end_color | Light Gray (Example Rows) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Log Review Schedule

---

## Sheet 3: Alert Management

---

## Sheet 4: Investigation Workflow

---

## Sheet 5: Analysis Tools & Capabilities

---

## Sheet 6: Review Findings

---

## Sheet 7: Continuous Monitoring

---

## Sheet 8: Performance Metrics

---

## Sheet 9: Gap Analysis

---

## Sheet 10: Evidence Register

---

## Sheet 11: Summary Dashboard

---

## Sheet 12: Approval & Sign-Off

---

## Sheet 13: Instructions

**Frozen Panes:** A3

---

## Sheet 14: Log_Review_Schedule

**Purpose:** "If you don't look at your logs, you don't have logs." - Ancient SOC wisdom

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Review ID | 15 |
| B | Review Type | 25 |
| C | Log Source / Scope | 30 |
| D | Frequency | 18 |
| E | Responsible Party | 25 |
| F | Review Procedure | 40 |
| G | Last Review Date | 18 |
| H | Next Review Due | 18 |
| I | Status | 15 |
| J | Days Overdue | 15 |
| K | Completion Rate % | 18 |
| L | Findings (Last Review) | 40 |
| M | Actions Taken | 40 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `review_type_dv` |
| D | D9:D100 | `frequency_dv` |
| I | I9:I100 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |
| JN | `=IF(AND(H{data_row}<>` |  |

---

## Sheet 15: Alert_Management

**Data Rows:** 142 (rows 9–150) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Alert ID | 15 |
| B | Alert Name | 30 |
| C | Alert Type | 20 |
| D | Severity | 15 |
| E | MITRE ATT&CK Tactic | 25 |
| F | Detection Logic | 40 |
| G | Threshold | 20 |
| H | Alerts/Month | 15 |
| I | True Positives | 15 |
| J | False Positives | 15 |
| K | True Positive Rate % | 18 |
| L | Tuning Required | 18 |
| M | Playbook Exists | 18 |
| N | Last Tuned | 15 |
| O | Status | 15 |
| P | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C9:C150 | `alert_type_dv` |
| D | D9:D150 | `severity_dv` |
| L | L9:L150 | `yes_no_dv` |
| M | M9:M150 | `yes_no_dv` |
| O | O9:O150 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |
| KN | `=IF(AND(I{data_row}<>` |  |

---

## Sheet 16: Investigation_Workflow

**Data Rows:** 192 (rows 9–200) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Incident ID | 15 |
| B | Detection Date | 15 |
| C | Alert Source | 25 |
| D | Severity | 15 |
| E | Incident Type | 25 |
| F | Status | 15 |
| G | Assigned To | 25 |
| H | MTTD (hours) | 15 |
| I | MTTR (hours) | 15 |
| J | Root Cause | 40 |
| K | Actions Taken | 40 |
| L | Lessons Learned | 40 |
| M | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D9:D200 | `severity_dv` |
| E | E9:E200 | `incident_type_dv` |
| F | F9:F200 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 17: Analysis_Tools

**Data Rows:** 42 (rows 9–50) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Tool / Capability | 30 |
| B | Category | 20 |
| C | Vendor / Product | 25 |
| D | Version | 15 |
| E | Purpose | 40 |
| F | Users Trained | 20 |
| G | Usage Frequency | 18 |
| H | Effectiveness | 18 |
| I | Integration with SIEM | 18 |
| J | Last Updated | 15 |
| K | Status | 15 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B50 | `category_dv` |
| G | G9:G50 | `frequency_dv` |
| H | H9:H50 | `effectiveness_dv` |
| I | I9:I50 | `integration_dv` |
| K | K9:K50 | `status_dv` |

---

## Sheet 18: Review_Findings

**Data Rows:** 192 (rows 9–200) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Finding ID | 15 |
| B | Review Date | 15 |
| C | Review Type | 20 |
| D | Log Source | 25 |
| E | Finding Description | 50 |
| F | Severity | 15 |
| G | Category | 20 |
| H | Action Required | 40 |
| I | Assigned To | 25 |
| J | Due Date | 15 |
| K | Status | 15 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C9:C200 | `review_type_dv` |
| F | F9:F200 | `severity_dv` |
| G | G9:G200 | `category_dv` |
| K | K9:K200 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 19: Continuous_Monitoring

**Data Rows:** 90 (rows 9–98) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Metric Date | 15 |
| B | Total Events/Day | 20 |
| C | Security Alerts Generated | 20 |
| D | Alerts Investigated | 20 |
| E | True Positives | 18 |
| F | False Positives | 18 |
| G | True Positive Rate % | 18 |
| H | Avg MTTD (hours) | 18 |
| I | Avg MTTR (hours) | 18 |
| J | Critical Incidents | 18 |
| K | Review Completion % | 18 |
| L | Notes | 40 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(AND(E{data_row}<>` |  |

---

## Sheet 20: Performance_Metrics

**Data Rows:** 200 (rows 9–208)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Incidents |
| — | `=COUNTIF(` | Critical Incidents |
| DN | `=IF(B{row}>0,\` |  |

---

## Sheet 21: Gap_Analysis

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | Gap Category | 25 |
| C | Description | 50 |
| D | Impact | 40 |
| E | Policy Requirement | 25 |
| F | Priority | 15 |
| G | Remediation Action | 50 |
| H | Owner | 25 |
| I | Target Date | 15 |
| J | Budget Required | 15 |
| K | Status | 15 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `category_dv` |
| F | F9:F100 | `priority_dv` |
| J | J9:J100 | `budget_dv` |
| K | K9:K100 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 22: Evidence_Register

**Data Rows:** 42 (rows 9–50) | **Frozen Panes:** A9

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 12 |
| B | Evidence Type | 18 |
| C | Description | 35 |
| D | Related Sheet | 18 |
| E | Source System | 18 |
| F | File Name/Location | 30 |
| G | Date Collected | 14 |
| H | Collected By | 15 |
| I | Classification | 14 |
| J | Retention Period | 14 |
| K | Status | 12 |
| L | Notes | 25 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| K | K9:K50 | `status_dv` |
| I | I9:I50 | `class_dv` |

---

## Sheet 23: Summary_Dashboard

**Data Rows:** 142 (rows 9–150)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(` | Review Completion Rate |
| DN | `=IF(B{row}>0,\` |  |
| BN | `=COUNTIFS(\` |  |

---

## Sheet 24: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"We can only see a short distance ahead, but we can see plenty there that needs to be done."*
- Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
