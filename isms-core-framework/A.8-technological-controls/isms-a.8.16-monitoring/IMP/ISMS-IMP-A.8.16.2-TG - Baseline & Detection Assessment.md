<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.16.2-TG:framework:TG:a.8.16.2 -->
**ISMS-IMP-A.8.16.2-TG - Baseline & Detection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.16.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Baseline Establishment & Anomaly Detection Capabilities |
| **Related Policy** | ISMS-POL-A.8.16, Section 2.2 (Baseline & Anomaly Detection Requirements) |
| **Purpose** | Assess baseline establishment for normal behavior, evaluate anomaly detection capabilities, and verify detection effectiveness across monitoring infrastructure |
| **Target Audience** | SOC Analysts, Security Engineers, Threat Intelligence Analysts, Detection Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly (Baselines evolve, detection rules require continuous tuning) |
| **Date** | 22.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original] | Initial technical specification | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a816_2_baseline_detection.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.16.2` |
| **Output Filename** | `ISMS-IMP-A.8.16.2_Baseline_&_Anomaly_Detection_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Baseline & Anomaly Detection Assessment |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #808080 | 808080 | Gray (Disabled) |
| #B4C7E7 | B4C7E7 | Light Blue (Planned/Info) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FF6666 | FF6666 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: 1. Baseline Inventory

---

## Sheet 3: 2. Detection Rules

---

## Sheet 4: 3. MITRE ATT&CK Coverage

---

## Sheet 5: 4. Rule Performance

---

## Sheet 6: 5. Testing Validation

---

## Sheet 7: Summary Dashboard

---

## Sheet 8: Evidence Register

---

## Sheet 9: Approval Sign-Off

---

## Sheet 10: Instructions

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=IF(B8<>` | B8 is Assessment Date |

---

## Sheet 11: Baseline_Inventory

**Data Rows:** 30 (rows 8–37)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Baseline Name/ID | 28 |
| B | Baseline Type | 22 |
| C | Scope/Target | 30 |
| D | Data Source | 25 |
| E | Baseline Period | 18 |
| F | Established Date | 16 |
| G | Last Updated | 16 |
| H | Update Frequency | 18 |
| I | Anomaly Detection Method | 25 |
| J | Threshold/Criteria | 25 |
| K | Alert Rules Linked | 20 |
| L | Baseline Status | 18 |
| M | Days Since Update | 16 |
| N | Compliance Status | 18 |
| O | Issues/Gaps | 30 |
| P | Owner | 20 |
| Q | Priority | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A8:A37)` | Total Baselines Defined |
| — | `=COUNTIF(L8:L37,\` | Active Baselines |
| — | `=COUNTIF(M8:M37,\` | Stale Baselines (>90 days) |
| — | `=COUNTIF(B8:B37,\` | Baselines by Type: User Activity |
| — | `=COUNTIF(I8:I37,\` | Automated Anomaly Detection |
| — | `=COUNTIFS(K8:K37,\` | Baselines with Linked Rules |
| BN | `=COUNTIF(Q54:Q68,` |  |

---

## Sheet 12: Detection_Rules

**Data Rows:** 50 (rows 8–57)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Rule ID/Name | 30 |
| B | Rule Type | 22 |
| C | Description | 40 |
| D | Severity | 15 |
| E | Data Source(s) | 30 |
| F | Rule Logic Summary | 40 |
| G | MITRE Tactic | 25 |
| H | MITRE Technique | 25 |
| I | Created Date | 16 |
| J | Last Modified | 16 |
| K | Last Triggered | 16 |
| L | Trigger Count (30d) | 18 |
| M | True Positives (30d) | 18 |
| N | False Positives (30d) | 18 |
| O | Precision % | 15 |
| P | Rule Status | 18 |
| Q | Tuning Status | 18 |
| R | Owner | 20 |
| S | Compliance Status | 18 |
| T | Issues/Notes | 35 |
| U | Priority | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(P8:P57,\` | Total Active Rules |
| — | `=COUNTIF(D8:D57,\` | Rules by Severity: Critical |
| — | `=SUM(L8:L57)` | Rules Triggered (30d) |
| — | `=COUNTIF(Q8:Q57,\` | Rules Needing Tuning |
| — | `=COUNTIF(L8:L57,0)` | Rules Not Triggered (30d) |
| — | `=COUNTIFS(J8:J57,\` | Rules Updated (30d) |
| BN | `=COUNTIF(U74:U88,` |  |

---

## Sheet 13: Mitre_Coverage

**Data Rows:** 50 (rows 10–59)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | MITRE Tactic | 25 |
| B | MITRE Technique ID | 20 |
| C | Technique Name | 35 |
| D | Technique Description | 45 |
| E | Risk Level | 15 |
| F | Detection Rules | 30 |
| G | Rule Count | 12 |
| H | Data Sources Available | 30 |
| I | Coverage Status | 18 |
| J | Detection Quality | 18 |
| K | Last Tested | 16 |
| L | Test Result | 15 |
| M | Notes/Gaps | 35 |
| N | Priority | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTIF(A$10:A$59,` |  |
| CN | `=COUNTIFS(A$10:A$59,` |  |
| FN | `=IF(B{row}>0,ROUND(C{row}/B{row}*100,1)&` |  |
| BN | `=SUM(B64:B77)` |  |
| CN | `=SUM(C64:C77)` |  |
| DN | `=SUM(D64:D77)` |  |
| EN | `=SUM(E64:E77)` |  |
| FN | `=IF(B78>0,ROUND(C78/B78*100,1)&` |  |
| BN | `=COUNTIF(N84:N98,` |  |

---

## Sheet 14: Rule_Performance

**Data Rows:** 30 (rows 8–37)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Rule ID/Name | 30 |
| B | Total Triggers | 15 |
| C | True Positives | 15 |
| D | False Positives | 15 |
| E | False Negatives | 15 |
| F | Precision % | 12 |
| G | Recall % | 12 |
| H | F1 Score | 12 |
| I | MTTD (minutes) | 15 |
| J | Tuning Actions | 30 |
| K | Last Tuned | 16 |
| L | Tuning Status | 18 |
| M | Performance Trend | 18 |
| N | Owner | 20 |
| O | Issues | 30 |
| P | Priority | 15 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(F8:F37,\` | Rules with Precision <70% |
| — | `=COUNTIF(F8:F37,` | Rules with high FP rate (>30%) |
| — | `=COUNTIF(L8:L37,` | Rules requiring tuning |
| — | `=COUNTIFS(K8:K37,\` | Rules tuned in last 30 days |
| BN | `=COUNTIF(P68:P82,` |  |

---

## Sheet 15: Testing_Validation

**Data Rows:** 30 (rows 8–37)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Test ID | 15 |
| B | Rule ID/Name | 30 |
| C | Test Date | 16 |
| D | Test Type | 20 |
| E | Test Scenario | 40 |
| F | Expected Result | 35 |
| G | Actual Result | 35 |
| H | Test Result | 15 |
| I | Detection Time | 15 |
| J | Issues Identified | 35 |
| K | Remediation Action | 35 |
| L | Retested | 15 |
| M | Tested By | 20 |
| N | Notes | 35 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B8:B37)` | Total Tests Performed |
| — | `=COUNTIF(H8:H37,` | Tests Passed |
| — | `=IF(COUNTA(H8:H37)>0,ROUND(COUNTIF(H8:H37,` | Pass Rate % |
| — | `=COUNTIF(L8:L37,` | Tests Requiring Retest |
| BN | `=COUNTIF(N54:N68,` |  |

---

## Sheet 16: Summary_Dashboard

**Data Rows:** 15 (rows 54–68)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(F{row}>0,ROUND(B{row}/(F{row}-E{row})*100,1)&` |  |
| HN | `=IF(G{row}=` |  |
| BN | `=SUM(B7:B11)` |  |
| CN | `=SUM(C7:C11)` |  |
| DN | `=SUM(D7:D11)` |  |
| EN | `=SUM(E7:E11)` |  |
| FN | `=SUM(F7:F11)` |  |

---

## Sheet 17: Base_Validations

---

## Sheet 18: Evidence_Register

---

## Sheet 19: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Those who can imagine anything, can create the impossible."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
