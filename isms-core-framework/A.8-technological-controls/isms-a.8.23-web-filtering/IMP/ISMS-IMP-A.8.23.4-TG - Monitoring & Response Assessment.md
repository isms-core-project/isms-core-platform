<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.23.4-TG:framework:TG:a.8.23.4 -->
**ISMS-IMP-A.8.23.4-TG - Monitoring & Response Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.23.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Web Filtering Monitoring, Logging & Incident Response |
| **Related Policy** | ISMS-POL-A.8.23, Section 2.4 (Logging and Monitoring), ISMS-POL-A.8.23, Section 3.4 (Incident Response) |
| **Purpose** | Assess operational monitoring, alerting, logging, and incident response capabilities for web filtering infrastructure |
| **Target Audience** | SOC Analysts, Security Engineers, IT Operations, Incident Responders, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Technical |
| **Review Cycle** | Quarterly or After Major Incidents/Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Web Filtering Monitoring & Incident Response assessment workbook | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a823_4_monitoring_response.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.23.4` |
| **Output Filename** | `ISMS-IMP-A.8.23.4_Monitoring_&_Response_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Monitoring & Response Assessment |
| **Total Sheets** | 11 (11 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | header_dark | Dark Blue (Headers) |
| #4472C4 | header_medium | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #8FAADC | header_light | Custom |
| #BDD7EE | status_blue | Light Blue (Alt) |
| #C6EFCE | status_green | Light Green (Compliant/Pass) |
| #D9D9D9 | status_gray | Light Gray (Column Headers) |
| #F2F2F2 | light_gray | Very Light Gray (Protected/Alternating) |
| #FFC7CE | status_red | Light Red (Non-Compliant/Fail) |
| #FFEB9C | status_yellow | Light Yellow/Amber (Partial) |
| #FFFFCC | input_yellow | Light Yellow (User Input) |

## Sheet 1: Instructions_Legend

**Frozen Panes:** A4

---

## Sheet 2: Log_Collection

**Data Rows:** 30 (rows 6–35) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 14 |
| B |  | 28 |
| C |  | 22 |
| D |  | 25 |
| E |  | 20 |
| F |  | 22 |
| G |  | 14 |
| H |  | 16 |
| I |  | 18 |
| J |  | 18 |
| K |  | 14 |
| L |  | 18 |
| M |  | 35 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B6:B35)` | Total log sources configured: |
| — | `=COUNTIF(C6:C35,` | Blocked request log sources: |
| — | `=COUNTIF(I6:I35,` | Sources meeting retention: |
| — | `=IF(COUNTA(I6:I35)>0,COUNTIF(I6:I35,` | Retention compliance rate: |
| — | `=COUNTIF(K6:K35,` | Implemented sources: |

---

## Sheet 3: Alert_Configuration

**Data Rows:** 40 (rows 6–45) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 12 |
| B |  | 32 |
| C |  | 20 |
| D |  | 38 |
| E |  | 18 |
| F |  | 14 |
| G |  | 22 |
| H |  | 25 |
| I |  | 20 |
| J |  | 25 |
| K |  | 15 |
| L |  | 14 |
| M |  | 14 |
| N |  | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTIF(C6:C45,` |  |
| CN | `=COUNTIFS(C6:C45,` |  |
| — | `=COUNTA(B6:B45)` | Total alert rules configured: |
| — | `=COUNTIF(L6:L45,` | Implemented alerts: |
| — | `=COUNTIF(F6:F45,` | Critical severity alerts: |
| — | `=COUNTIF(K6:K45,` | Alerts with auto-response: |
| — | `=IF(COUNTA(B6:B45)>0,COUNTIF(L6:L45,` | Alert coverage score: |

---

## Sheet 4: Monitoring_Dashboard

**Data Rows:** 20 (rows 6–25) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 14 |
| B |  | 32 |
| C |  | 20 |
| D |  | 20 |
| E |  | 18 |
| F |  | 18 |
| G |  | 45 |
| H |  | 18 |
| I |  | 14 |
| J |  | 18 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B6:B25)` | Total dashboards configured: |
| — | `=COUNTIF(H6:H25,` | Dashboards with alerting: |
| — | `=COUNTIF(E6:E25,` | Real-time dashboards: |
| — | `=COUNTA(B30:B49)` | KPIs defined: |

---

## Sheet 5: Incident_Response

**Data Rows:** 15 (rows 6–20) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 14 |
| B |  | 32 |
| C |  | 16 |
| D |  | 20 |
| E |  | 20 |
| F |  | 20 |
| G |  | 30 |
| H |  | 20 |
| I |  | 14 |
| J |  | 20 |

---

## Sheet 6: Blocked_Events_Analysis

**Data Rows:** 20 (rows 6–25) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 14 |
| B |  | 30 |
| C |  | 20 |
| D |  | 20 |
| E |  | 16 |
| F |  | 25 |
| G |  | 14 |
| H |  | 16 |
| I |  | 35 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B6:B25)` | Categories tracked: |
| — | `=COUNTIF(H6:H25,` | Categories requiring action: |
| — | `=COUNTIF(G6:G25,` | High-risk categories: |
| — | `=COUNTIF(E6:E25,` | Categories with increasing trend: |

---

## Sheet 7: False_Positive_Mgmt

**Data Rows:** 50 (rows 6–55) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 12 |
| B |  | 14 |
| C |  | 20 |
| D |  | 28 |
| E |  | 35 |
| F |  | 20 |
| G |  | 22 |
| H |  | 14 |
| I |  | 20 |
| J |  | 14 |
| K |  | 14 |
| L |  | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B6:B55)` | Total FPs reported (last 90 days) |
| — | `=IFERROR(AVERAGE(I6:I55),` | Average resolution time (hours) |
| — | `=COUNTIF(K6:K55,` | Open FPs |
| — | `=IFERROR(COUNTIF(F6:F55,` | Confirmed FP rate |
| — | `=IFERROR((COUNTIF(J6:J55,` | Recurring FP percentage |
| — | `=COUNTIF(G6:G55,` | FPs resolved via whitelist |

---

## Sheet 8: Reporting_Schedule

**Data Rows:** 20 (rows 6–25) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 12 |
| B |  | 32 |
| C |  | 18 |
| D |  | 14 |
| E |  | 18 |
| F |  | 28 |
| G |  | 18 |
| H |  | 40 |
| I |  | 14 |
| J |  | 14 |
| K |  | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IFERROR(C{0}/B{0},0)` |  |
| — | `=COUNTA(B6:B25)` | Total reports configured: |
| — | `=COUNTIF(E6:E25,` | Automated reports: |
| — | `=COUNTIF(J6:J25,` | Reports implemented: |
| — | `=COUNTIF(D6:D25,` | Daily reports: |
| — | `=COUNTIF(D30:D37,` | Stakeholders with full coverage: |

---

## Sheet 9: Gap_Analysis

**Data Rows:** 30 (rows 6–35) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 14 |
| B |  | 18 |
| C |  | 40 |
| D |  | 30 |
| E |  | 30 |
| F |  | 14 |
| G |  | 25 |
| H |  | 35 |
| I |  | 20 |
| J |  | 14 |
| K |  | 15 |
| L |  | 12 |
| M |  | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(C6:C35)` | Total gaps identified: |
| — | `=COUNTIF(F6:F35,` | Critical gaps: |
| — | `=COUNTIF(K6:K35,` | Open gaps: |
| — | `=COUNTIFS(K6:K35,` | Gaps past target date: |
| BN | `=COUNTIF(B6:B35,` |  |
| CN | `=COUNTIFS(B6:B35,` |  |

---

## Sheet 10: Evidence_Register

**Data Rows:** 100 (rows 6–105) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 14 |
| B |  | 35 |
| C |  | 22 |
| D |  | 20 |
| E |  | 16 |
| F |  | 14 |
| G |  | 18 |
| H |  | 40 |
| I |  | 14 |
| J |  | 18 |
| K |  | 30 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B6:B105)` | Total evidence items: |
| — | `=COUNTIF(J6:J105,` | Verified evidence: |
| — | `=COUNTIF(D6:D105,` | Evidence by Log_Collection: |

---

## Sheet 11: Approval_Sign_Off

**Data Rows:** 20 (rows 40–59) | **Frozen Panes:** A4

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(Incident_Response!G40:G59,` | Open Incidents: |

---

**END OF SPECIFICATION**

---

*"The ideas I had about supernatural beings came to me the same way that my mathematical ideas did. So I took them seriously."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
