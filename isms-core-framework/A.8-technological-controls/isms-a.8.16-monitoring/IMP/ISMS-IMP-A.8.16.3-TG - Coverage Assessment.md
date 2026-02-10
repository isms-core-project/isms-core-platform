<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.16.3-TG:framework:TG:a.8.16.3 -->
**ISMS-IMP-A.8.16.3-TG - Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.16.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Monitoring Coverage (Assets, Networks, Users, Applications) |
| **Related Policy** | ISMS-POL-A.8.16, Section 2.1.2 (Log Source Coverage), Section 2.1.3 (Coverage Assessment) |
| **Purpose** | Assess completeness of monitoring coverage across all organizational assets, identify blind spots, and document remediation plans |
| **Target Audience** | Asset Owners, IT Operations, Security Operations, Network Teams, Application Teams, Compliance Officers |
| **Assessment Type** | Coverage Analysis & Gap Assessment |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | 22.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original] | Initial technical specification | ISMS Implementation Team |

---

# Appendix: Coverage Assessment Quick Reference


> Auto-generated from `generate_a816_3_coverage_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.16.3` |
| **Output Filename** | `ISMS-IMP-A.8.16.3_Coverage_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Coverage Assessment |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: 1. Asset Coverage

---

## Sheet 3: 2. Network Coverage

---

## Sheet 4: 3. User Identity Coverage

---

## Sheet 5: 4. Application Coverage

---

## Sheet 6: 5. Gap Analysis

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
| BN | `=IF(B8<>` |  |

---

## Sheet 11: Asset_Coverage

**Data Rows:** 43 (rows 8–50)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset ID | 15 |
| B | Asset Name | 28 |
| C | Asset Type | 22 |
| D | Operating System | 22 |
| E | Location | 18 |
| F | Business Unit | 20 |
| G | Asset Owner | 20 |
| H | Data Classification | 18 |
| I | Criticality | 15 |
| J | Regulatory Scope | 22 |
| K | Monitoring Required | 16 |
| L | Currently Monitored | 16 |
| M | Log Types Collected | 30 |
| N | Monitoring Platform | 22 |
| O | Baseline Established | 16 |
| P | Detection Rules Active | 18 |
| Q | Last Log Verified | 14 |
| R | Coverage Status | 18 |
| S | Gap Reason | 30 |
| T | Exception Approved | 16 |
| U | Target Coverage Date | 14 |
| V | Responsible Party | 20 |
| W | Notes | 25 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTIF(W55:W69,` |  |

---

## Sheet 12: Network_Coverage

**Data Rows:** 25 (rows 8–32)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Network Segment/Zone | 28 |
| B | Segment Type | 22 |
| C | IP Range/CIDR | 20 |
| D | VLAN ID | 12 |
| E | Number of Assets | 15 |
| F | Criticality | 15 |
| G | Data Classification | 18 |
| H | Perimeter Monitoring | 18 |
| I | Flow Monitoring | 16 |
| J | DNS Monitoring | 16 |
| K | Endpoint Monitoring | 18 |
| L | Log Collection Active | 18 |
| M | Network Tap/SPAN | 16 |
| N | Isolation Status | 16 |
| O | Coverage Status | 18 |
| P | Gaps Identified | 30 |
| Q | Exception Approved | 16 |
| R | Target Date | 14 |
| S | Responsible Party | 20 |
| T | Notes | 25 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTIF(T37:T46,` |  |

---

## Sheet 13: User_Identity_Coverage

**Data Rows:** 19 (rows 1–19)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Identity System | 25 |
| B | System Type | 22 |
| C | User Count | 15 |
| D | Privileged Account Count | 20 |
| E | Service Account Count | 20 |
| F | Authentication Logs Collected | 22 |
| G | Authorization Logs Collected | 22 |
| H | Password Change Logs | 20 |
| I | Privilege Escalation Logs | 22 |
| J | MFA Events Logged | 18 |
| K | SSO Events Logged | 18 |
| L | Failed Login Monitoring | 20 |
| M | After-Hours Access Monitoring | 22 |
| N | Geographic Anomaly Detection | 22 |
| O | User Behavior Analytics | 22 |
| P | Privileged Access Monitoring | 22 |
| Q | Coverage Status | 18 |
| R | Gaps/Issues | 30 |
| S | Priority | 16 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTIF(S27:S41,` |  |

---

## Sheet 14: Application_Coverage

**Data Rows:** 25 (rows 8–32)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Application/Service Name | 28 |
| B | Application Type | 22 |
| C | Business Unit | 20 |
| D | Application Owner | 20 |
| E | Data Classification | 18 |
| F | Criticality | 15 |
| G | User Base | 18 |
| H | Application Logs Collected | 22 |
| I | API Logs Collected | 18 |
| J | Database Logs Collected | 22 |
| K | Error/Exception Logging | 20 |
| L | Transaction Logging | 18 |
| M | Access Control Logs | 20 |
| N | Data Export Monitoring | 20 |
| O | Performance Monitoring | 20 |
| P | WAF Integration | 16 |
| Q | APM Integration | 16 |
| R | Coverage Status | 18 |
| S | Gaps | 30 |
| T | Target Date | 14 |
| U | Priority | 16 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTIF(U37:U51,` |  |

---

## Sheet 15: Gap_Analysis

**Data Rows:** 40 (rows 8–47)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | Gap Category | 22 |
| C | Affected Asset/System | 28 |
| D | Gap Description | 35 |
| E | Business Impact | 30 |
| F | Risk Level | 15 |
| G | Root Cause | 30 |
| H | Exception Approved | 16 |
| I | Exception ID | 15 |
| J | Compensating Controls | 30 |
| K | Remediation Plan | 35 |
| L | Remediation Owner | 20 |
| M | Target Date | 14 |
| N | Budget Required | 15 |
| O | Status | 18 |
| P | Status Date | 14 |
| Q | Verification Method | 25 |
| R | Notes | 30 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B8:B47)` | Total Gaps Identified |
| — | `=COUNTIF(F8:F47,` | Critical Gaps |
| — | `=COUNTIF(O8:O47,` | Open Gaps |
| — | `=SUMPRODUCT((O8:O47<>` | Overdue (Past Target Date) |
| BN | `=COUNTIF(R64:R78,` |  |

---

## Sheet 16: Summary_Dashboard

**Data Rows:** 43 (rows 8–50)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Assets in Inventory |
| — | `=COUNTIF(` | Assets Monitored |
| — | `=IF(B6>0,ROUND(B7/B6*100,1)&\` | % Asset Coverage |
| — | `=COUNTIFS(` | Critical Assets - 100% Monitored |
| — | `=IF(COUNTIF(` | High Assets - % Monitored |
| GN | `=IF(F{row}>0,ROUND(B{row}/(F{row}-E{row})*100,1)&` |  |
| HN | `=IF(G{row}=` |  |
| BN | `=SUM(B22:B26)` |  |
| CN | `=SUM(C22:C26)` |  |
| DN | `=SUM(D22:D26)` |  |
| EN | `=SUM(E22:E26)` |  |
| FN | `=SUM(F22:F26)` |  |

---

## Sheet 17: Base_Validations

---

## Sheet 18: Evidence_Register

---

## Sheet 19: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Mathematical reasoning may be regarded rather schematically as the exercise of a combination of two facilities, which we may call intuition and ingenuity."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
