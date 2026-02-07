**ISMS-IMP-A.8.9.2-TG - Change Control Assessment Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

**Document ID**: ISMS-IMP-A.8.9.2-TG  
**Title**: Change Control Assessment Specification  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Configuration Manager  
**Status**: Draft  

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Change Control and Configuration Updates - Change Classification, CAB Operations, Approval Workflows, Testing, Rollback |
| **Related Policy** | ISMS-POL-A.8.9, Section 2.3 (Change Control & Configuration Updates) |
| **Purpose** | Assess change control processes, CAB operations, approval workflows, testing procedures, and rollback capabilities for configuration changes to ensure controlled and authorized modifications |
| **Target Audience** | Configuration Manager, CAB Members, Change Coordinators, System Administrators, IT Operations, Service Owners, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Change Control assessment workbook | ISMS Implementation Team |

### Approvers

- Primary: Configuration Manager
- Technical Review: Security Architect
- Security Review: Chief Information Security Officer (CISO)

### Distribution

Configuration management team, system administrators, IT operations, security engineers, auditors

### Related Documents

- ISMS-POL-A.8.9: Configuration Management Policy (Consolidated)
- ISMS-CTX-A.8.9: Configuration Management Reference (NOT ISMS)


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a89_2_change_control.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.9.2` |
| **Output Filename** | `ISMS-IMP-A.8.9.2_Change_Control_YYYYMMDD.xlsx` |
| **Workbook Title** | Change Control Assessment |
| **Total Sheets** | 12 (12 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.9: Configuration Management |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | header_main | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | header_sub | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #9C6500 | 9C6500 | Dark Yellow (Caution) |
| #C00000 | critical | Dark Red (Blocked) |
| #C6EFCE | compliant | Light Green (Compliant/Pass) |
| #D9D9D9 | column_header | Light Gray (Column Headers) |
| #E7E6E6 | info_bg | Light Gray (Example Rows) |
| #F2F2F2 | protected_cell | Very Light Gray (Protected/Alternating) |
| #FFA500 | orange | Orange (High Priority) |
| #FFC7CE | non_compliant | Light Red (Non-Compliant/Fail) |
| #FFEB9C | partial | Light Yellow/Amber (Partial) |

## Sheet 1: Instructions

**Data Rows:** 2 (rows 1–2)

---

## Sheet 2: Change_Request_Register

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Change ID | 18 |
| B | Change Title | 35 |
| C | Change Type | 15 |
| D | Priority | 15 |
| E | Affected Systems/Assets | 35 |
| F | Requestor Name | 20 |
| G | Requestor Contact | 20 |
| H | Request Date | 15 |
| I | Required Implementation Date | 15 |
| J | Change Status | 18 |
| K | Current Phase | 18 |
| L | Days in Current Phase | 12 |
| M | Overall Status Indicator | 18 |
| N | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| C3:CN | equal  |  |
| C3:CN | equal  |  |
| D3:DN | equal  | Fill: non_compliant |
| D3:DN | equal  | Fill: partial |
| J3:JN | equal  | Fill: compliant |
| J3:JN | equal  | Fill: non_compliant |
| M3:MN | equal  |  |
| M3:MN | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| KN | `=IF(J{row}=` |  |
| LN | `=IF(H{row}=` |  |
| MN | `=IF(OR(J{row}=` |  |

---

## Sheet 3: Change_Approval_Workflow

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 18 |
| B |  | 30 |
| C |  | 18 |
| D |  | 20 |
| E |  | 18 |
| F |  | 15 |
| G |  | 20 |
| H |  | 18 |
| I |  | 15 |
| J |  | 20 |
| K |  | 18 |
| L |  | 15 |
| M |  | 25 |
| N |  | 30 |
| O |  | 18 |
| P |  | 15 |
| Q |  | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| N3:NN | equal  | Fill: compliant |
| N3:NN | equal  | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| ON | `=IF(C{row}=` |  |
| PN | `=IF(O{row}=` |  |

---

## Sheet 4: Impact_Assessment

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 18 |
| B |  | 30 |
| C |  | 12 |
| D |  | 35 |
| E |  | 15 |
| F |  | 15 |
| G |  | 20 |
| H |  | 15 |
| I |  | 35 |
| J |  | 35 |
| K |  | 15 |
| L |  | 20 |
| M |  | 35 |
| N |  | 35 |
| O |  | 12 |
| P |  | 25 |
| Q |  | 15 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| H3:HN | equal  | Fill: critical |
| H3:HN | equal  | Fill: non_compliant |
| O3:ON | greaterThanOrEqual 12 | Fill: non_compliant |
| O3:ON | between 6 | Fill: partial |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| ON | `=IF(H{row}=` |  |

---

## Sheet 5: Testing_Validation

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 18 |
| B |  | 30 |
| C |  | 15 |
| D |  | 20 |
| E |  | 15 |
| F |  | 15 |
| G |  | 12 |
| H |  | 30 |
| I |  | 12 |
| J |  | 12 |
| K |  | 12 |
| L |  | 12 |
| M |  | 12 |
| N |  | 12 |
| O |  | 18 |
| P |  | 18 |
| Q |  | 20 |
| R |  | 15 |
| S |  | 35 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| L3:LN | greaterThanOrEqual 95 | Fill: compliant |
| L3:LN | between 80 | Fill: partial |
| L3:LN | lessThan 80 | Fill: non_compliant |
| P3:PN | equal  | Fill: compliant |
| P3:PN | equal  | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(OR(E{row}=` |  |
| LN | `=IF(I{row}=0,` |  |

---

## Sheet 6: Implementation_Log

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 18 |
| B |  | 30 |
| C |  | 20 |
| D |  | 20 |
| E |  | 20 |
| F |  | 12 |
| G |  | 20 |
| H |  | 20 |
| I |  | 40 |
| J |  | 35 |
| K |  | 20 |
| L |  | 30 |
| M |  | 35 |
| N |  | 18 |
| O |  | 18 |
| P |  | 18 |
| Q |  | 15 |
| R |  | 20 |
| S |  | 35 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| O3:ON | equal  | Fill: compliant |
| O3:ON | equal  | Fill: non_compliant |
| Q3:QN | equal  | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| FN | `=IF(OR(D{row}=` |  |
| PN | `=IF(O{row}=` |  |

---

## Sheet 7: Rollback_Capability

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 18 |
| B |  | 30 |
| C |  | 15 |
| D |  | 18 |
| E |  | 40 |
| F |  | 35 |
| G |  | 20 |
| H |  | 18 |
| I |  | 15 |
| J |  | 20 |
| K |  | 35 |
| L |  | 18 |
| M |  | 15 |
| N |  | 25 |
| O |  | 20 |
| P |  | 18 |
| Q |  | 35 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| P3:PN | equal  | Fill: compliant |
| P3:PN | equal  | Fill: non_compliant |
| P3:PN | equal  | Fill: partial |
| J3:JN | equal  | Fill: compliant |
| J3:JN | equal  | Fill: non_compliant |
| J3:JN | equal  | Fill: non_compliant |
| L3:LN | equal  | Fill: non_compliant |
| L3:LN | equal  | Fill: partial |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| PN | `=IF(C{row}=` |  |

---

## Sheet 8: Emergency_Changes

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 18 |
| B |  | 30 |
| C |  | 25 |
| D |  | 40 |
| E |  | 20 |
| F |  | 20 |
| G |  | 20 |
| H |  | 12 |
| I |  | 25 |
| J |  | 30 |
| K |  | 20 |
| L |  | 15 |
| M |  | 25 |
| N |  | 18 |
| O |  | 18 |
| P |  | 40 |
| Q |  | 40 |
| R |  | 35 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| M3:MN | equal  | Fill: compliant |
| M3:MN | equal  | Fill: non_compliant |
| M3:MN | equal  | Fill: partial |
| O3:ON | equal  |  |
| O3:ON | equal  |  |
| O3:ON | equal  |  |
| K3:KN | equal  | Fill: non_compliant |
| K3:KN | equal  | Fill: compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=IF(OR(F{row}=` |  |
| ON | `=IF(AND(H{row}>48,N{row}=` |  |

---

## Sheet 9: Change_Success_Metrics

**Data Rows:** 100 (rows 3–102)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Change_Request_Register!A3:A102)-COUNTBLANK(Change_Request_Register!A3:A` | Total Changes (All Types) |
| — | `=COUNTIF(Change_Request_Register!J3:J102,` | Completed Changes |
| — | `=IF((B6+B7+B8)=0,0,B6/(B6+B7+B8)*100)` | Overall Success Rate % |
| — | `=COUNTIF(Change_Request_Register!C3:C102,` | Standard |
| CN | `=IF($B$5=0,0,B{row}/$B$5*100)` |  |
| CN | `=COUNTIFS(Change_Request_Register!C3:C102,` |  |
| DN | `=IF(B{row}=0,0,C{row}/B{row}*100)` |  |
| — | `=COUNTA(Emergency_Changes!A3:A52)-COUNTBLANK(Emergency_Changes!A3:A52)` | Total Emergency Changes |
| — | `=COUNTIF(Emergency_Changes!M3:M52,` | Emergency Changes Not Reviewed |
| — | `=COUNTIF(Emergency_Changes!O3:O52,` | Process Abuse Flagged |

---

## Sheet 10: Compliance_Dashboard

**Data Rows:** 100 (rows 3–102)

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| D6:DN | greaterThanOrEqual 95 | Fill: compliant |
| D6:DN | between 90 | Fill: partial |
| D6:DN | lessThan 90 | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IF((B{row}+C{row})=0,0,B{row}/(B{row}+C{row})*100)` |  |
| DN | `=AVERAGE(D{approval_start}:D{approval_start+1})` |  |
| EN | `=IF(D{row}>=95,` |  |
| DN | `=AVERAGE(D{testing_start}:D{testing_start+2})` |  |
| DN | `=AVERAGE(D{rollback_start}:D{rollback_start+1})` |  |
| DN | `=AVERAGE(D{overall_row-3}:D{overall_row-1})` |  |

---

## Sheet 11: Evidence_Register

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 18 |
| B |  | 20 |
| C |  | 40 |
| D |  | 20 |
| E |  | 15 |
| F |  | 40 |
| G |  | 20 |
| H |  | 15 |
| I |  | 15 |
| J |  | 15 |
| K |  | 18 |
| L |  | 25 |
| M |  | 35 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| K3:KN | equal  | Fill: compliant |
| K3:KN | equal  | Fill: non_compliant |
| H3:HN | equal  |  |

---

## Sheet 12: Approval_Sign_Off

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| BN:BN | equal  | Fill: compliant |
| BN:BN | equal  | Fill: partial |
| BN:BN | equal  | Fill: non_compliant |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `APPROVAL_DECISION` | Approved, Approved with Conditions, Not Approved - Revisions Required |
| `APPROVAL_METHOD` | CAB Meeting, Email Approval, Emergency Verbal, Automated (Standard), Not Applicable |
| `APPROVAL_STATUS_TIER` | ⏳ Pending, ✅ Approved, ❌ Rejected, ➖ N/A |
| `APPROVAL_TIER` | Single-Tier, Two-Tier, Three-Tier, Emergency |
| `CAB_REVIEW_OUTCOME` | ✅ Approved, ⚠️ Approved with Remediation, ❌ Disapproved (requires reversal), ⏳ Not Yet Reviewed |
| `CHANGE_PRIORITY` | 🔴 P1-Critical, 🟡 P2-High, 🟢 P3-Medium, ⭕ P4-Low |
| `CHANGE_STATUS` | 📝 Draft, 📤 Submitted, ✅ Approved, 🧪 In Testing, 📅 Scheduled, ⏳ Implementing, ✅ Completed, ❌ Faile... |
| `CHANGE_TYPE` | Standard, Normal, Emergency, Hot Fix |
| `DATA_LOSS_RISK` | None, Minimal, Moderate, Significant |
| `EMERGENCY_APPROVAL_METHOD` | Verbal (CIO/CISO), Email (Expedited), CAB Chair Authorization |
| `EMERGENCY_TYPE` | Security Incident, Service Outage, Critical Bug, Vulnerability Remediation, Other |
| `EVIDENCE_CLASSIFICATION` | Public, Internal, Confidential, Restricted |
| `EVIDENCE_TYPE` | Approval Record, Test Results, Implementation Log, Rollback Test, CAB Minutes, Email Approval, Ch... |
| `EVIDENCE_VERIFICATION` | ✅ Verified, 🔍 Needs Verification, ❌ Missing, ⏰ Outdated |
| `GO_NOGO` | Go, No-Go, Go with Conditions, N/A |
| `IMPLEMENTATION_METHOD` | Manual, Automated Script, Semi-Automated, Assisted (Vendor) |
| `IMPLEMENTATION_STATUS` | ✅ Successful, ❌ Failed, 🔄 Rolled Back, ⏳ In Progress |
| `ISSUES_RESOLVED` | Yes, No, Partially, N/A |
| `JUSTIFICATION_VALID` | Yes, No, Questionable |
| `POST_IMPL_DOC` | Yes, No, In Progress |
| `RETENTION_PERIOD` | 1 Year, 3 Years, 5 Years, 7 Years, Indefinite |
| `RISK_LEVEL` | ⭕ Low, 🟢 Medium, 🟡 High, 🔴 Critical |
| `ROLLBACK_APPROVAL` | Yes (same as forward), Yes (expedited), No (automatic) |
| `ROLLBACK_TEST_RESULTS` | ✅ Successful, ❌ Failed, ⚠️ Partially Successful, ❓ Not Tested |
| `SERVICE_DOWNTIME` | None, <1 hour, 1-4 hours, 4-8 hours, >8 hours |
| `TESTING_STATUS` | 🔴 Not Started, ⏳ In Progress, ✅ Completed, ❌ Failed, ⚡ Abbreviated (Emergency) |
| `TEST_ENVIRONMENT` | Dev, Test, Staging, UAT, Production (Non-Critical), None |
| `USER_IMPACT` | None, Minimal, Moderate, Significant, Severe |
| `VERIFICATION_STATUS` | ✅ Successful, ⚠️ Partial Success, ❌ Failed, ❓ Not Verified |
| `YES_NO` | Yes, No |
| `YES_NO_NA` | Yes, No, N/A |
| `YES_NO_PARTIAL_NA` | Yes, No, Partially, N/A |

---

**END OF SPECIFICATION**

---

*"The process of analogy-making lies at the heart of intelligence."*
— Douglas Hofstadter

<!-- QA_VERIFIED: 2026-02-06 -->
