<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.9.1-TG:framework:TG:a.8.9.1 -->
**ISMS-IMP-A.8.9.1-TG - Baseline Configuration Assessment Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

**Document ID**: ISMS-IMP-A.8.9.1-TG  
**Title**: Baseline Configuration Assessment Specification  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Configuration Manager  
**Status**: Draft  

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Baseline Configuration Management - Asset Inventory, Baseline Documentation, Golden Images, Approvals |
| **Related Policy** | ISMS-POL-A.8.9, Section 2.2 (Baseline Configuration Management) |
| **Purpose** | Assess establishment, documentation, approval, and maintenance of configuration baselines across all asset types to demonstrate ISO 27001:2022 Control A.8.9 compliance |
| **Target Audience** | Configuration Manager, System Administrators, Asset Managers, Security Engineers, IT Operations, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Baseline Configuration assessment workbook | ISMS Implementation Team |

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


> Auto-generated from `generate_a89_1_baseline_configuration.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.9.1` |
| **Output Filename** | `ISMS-IMP-A.8.9.1_Baseline_Configuration_YYYYMMDD.xlsx` |
| **Workbook Title** | Baseline Configuration Assessment |
| **Total Sheets** | 12 (11 visible + 1 hidden) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.9: Configuration Management |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | header_main | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | header_sub | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #999999 | 999999 | Medium Gray |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #9C6500 | 9C6500 | Dark Yellow (Caution) |
| #C00000 | critical | Dark Red (Blocked) |
| #C65911 | C65911 | Brown/Orange (Overdue) |
| #C6EFCE | compliant | Light Green (Compliant/Pass) |
| #D9D9D9 | column_header | Light Gray (Column Headers) |
| #E7E6E6 | info_bg | Light Gray (Example Rows) |
| #F2F2F2 | protected_cell | Very Light Gray (Protected/Alternating) |
| #FFC7CE | non_compliant | Light Red (Non-Compliant/Fail) |
| #FFEB9C | partial | Light Yellow/Amber (Partial) |

## Sheet 1: Lookup_Tables (Hidden)

---

## Sheet 2: Instructions

**Data Rows:** 2 (rows 1–2)

---

## Sheet 3: Asset_Inventory

**Purpose:** Comprehensive list of all information assets requiring baseline management.

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset ID | 15 |
| B | Asset Name | 30 |
| C | Asset Type | 35 |
| D | Asset Category | 20 |
| E | Criticality | 12 |
| F | Owner | 20 |
| G | Location | 25 |
| H | Baseline Status | 15 |
| I | Baseline Reference | 25 |
| J | Last Reviewed Date | 15 |
| K | Next Review Due | 15 |
| L | Compliance Status | 15 |
| M | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| H3:HN | equal  | Fill: compliant |
| H3:HN | equal  | Fill: partial |
| H3:HN | equal  | Fill: non_compliant |
| H3:HN | equal  | Fill: excluded |
| L3:LN | containsText  | Fill: compliant |
| L3:LN | containsText  | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IF(C{row}=` |  |
| KN | `=IF(J{row}=` |  |
| LN | `=IF(H{row}=` |  |

---

## Sheet 4: Baseline_Repository

**Purpose:** Catalog of all configuration baselines maintained by [Organization].

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Baseline ID | 20 |
| B | Baseline Name | 35 |
| C | Version | 12 |
| D | Applicable Asset Types | 30 |
| E | Description | 50 |
| F | Approval Status | 18 |
| G | Approved By | 20 |
| H | Approval Date | 15 |
| I | Last Updated | 15 |
| J | Documentation Location | 40 |
| K | Config Elements Count | 12 |
| L | Applied to Assets Count | 12 |
| M | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| F3:FN | equal  | Fill: compliant |
| F3:FN | equal  | Fill: partial |
| F3:FN | equal  | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| LN | `=COUNTIF(Asset_Inventory!$I$3:$I$102,A{row})` |  |

---

## Sheet 5: Baseline_Coverage_Matrix

**Purpose:** Statistical analysis of baseline coverage by asset type (formula-driven).

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Type | 40 |
| B | Asset Category | 20 |
| C | Total Assets | 12 |
| D | Assets with Baselines | 15 |
| E | Assets In Progress | 15 |
| F | Assets Not Started | 15 |
| G | Assets N/A | 12 |
| H | Coverage % | 12 |
| I | Critical Assets Count | 12 |
| J | Critical Coverage % | 15 |
| K | Status | 15 |
| L | Gap Analysis | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| H3:HN | greaterThanOrEqual 90 | Fill: compliant |
| H3:HN | between 60 | Fill: partial |
| H3:HN | lessThan 60 | Fill: non_compliant |
| J3:JN | greaterThanOrEqual 95 | Fill: compliant |
| J3:JN | between 80 | Fill: partial |
| J3:JN | lessThan 80 | Fill: non_compliant |
| K3:KN | containsText  |  |
| K3:KN | containsText  |  |
| K3:KN | containsText  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| CN | `=COUNTIF(Asset_Inventory!$C$3:$C$102,A{row})` |  |
| DN | `=COUNTIFS(Asset_Inventory!$C$3:$C$102,A{row},Asset_Inventory!$H$3:$H$102,` |  |
| HN | `=IF((C{row}-G{row})=0,0,D{row}/(C{row}-G{row})*100)` |  |
| JN | `=IF(I{row}=0,0,COUNTIFS(Asset_Inventory!$C$3:$C$102,A{row},Asset_Inventory!$E$3:` |  |
| KN | `=IF(H{row}>=90,` |  |
| LN | `=IF(ISNUMBER(SEARCH(` |  |
| CN | `=SUM(C3:C{row-1})` |  |
| DN | `=SUM(D3:D{row-1})` |  |
| EN | `=SUM(E3:E{row-1})` |  |
| FN | `=SUM(F3:F{row-1})` |  |
| GN | `=SUM(G3:G{row-1})` |  |
| HN | `=IF((C{summary_row}-G{summary_row})=0,0,D{summary_row}/(C{summary_row}-G{summary` |  |
| IN | `=SUM(I3:I{row-1})` |  |
| JN | `=IF(I{summary_row}=0,0,COUNTIFS(Asset_Inventory!$E$3:$E$102,` |  |
| KN | `=IF(H{summary_row}>=85,` |  |

---

## Sheet 6: Approval_Tracking

**Purpose:** Track approval workflow status for each configuration baseline.

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Baseline ID | 20 |
| B | Baseline Name | 30 |
| C | Submission Date | 15 |
| D | Approver Name | 20 |
| E | Approval Status | 20 |
| F | Approval Date | 15 |
| G | Approval Method | 25 |
| H | Approval Reference | 30 |
| I | Business Justification | 40 |
| J | Risk Assessment | 15 |
| K | Days Pending | 12 |
| L | SLA Status | 15 |
| M | Next Action | 30 |
| N | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E3:EN | equal  | Fill: compliant |
| E3:EN | equal  | Fill: partial |
| E3:EN | equal  | Fill: non_compliant |
| L3:LN | equal  |  |
| L3:LN | equal  |  |
| L3:LN | equal  |  |
| K3:KN | greaterThan 21 | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| KN | `=IF(C{row}=` |  |
| LN | `=IF(K{row}=` |  |

---

## Sheet 7: Documentation_Assessment

**Purpose:** Evaluate quality of baseline documentation against defined criteria.

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Baseline ID | 20 |
| B | Baseline Name | 30 |
| C | Documentation Completeness | 18 |
| D | Completeness Score | 12 |
| E | Documentation Accuracy | 18 |
| F | Accuracy Score | 12 |
| G | Maintainability | 18 |
| H | Maintainability Score | 12 |
| I | Accessibility | 18 |
| J | Accessibility Score | 12 |
| K | Overall Quality Score | 15 |
| L | Quality Rating | 15 |
| M | Gaps Identified | 40 |
| N | Remediation Priority | 15 |
| O | Target Completion Date | 15 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| K3:KN | greaterThanOrEqual 90 | Fill: compliant |
| K3:KN | between 75 | Fill: #C6EFCE (Light Green (Compliant/Pass)) |
| K3:KN | between 50 | Fill: partial |
| K3:KN | lessThan 50 | Fill: non_compliant |
| L3:LN | equal  |  |
| L3:LN | equal  |  |
| L3:LN | equal  |  |
| L3:LN | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IF(C{row}=` |  |
| FN | `=IF(E{row}=` |  |
| HN | `=IF(G{row}=` |  |
| JN | `=IF(I{row}=` |  |
| KN | `=IF(AND(D{row}=` |  |
| LN | `=IF(K{row}=` |  |

---

## Sheet 8: Version_Control

**Purpose:** Track version history of configuration baselines over time.

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Baseline ID | 20 |
| B | Baseline Name | 30 |
| C | Version Number | 15 |
| D | Version Date | 15 |
| E | Previous Version | 15 |
| F | Change Type | 18 |
| G | Change Summary | 40 |
| H | Change Request Reference | 25 |
| I | Changed By | 20 |
| J | Approved By | 20 |
| K | Superseded Date | 15 |
| L | Status | 12 |
| M | Assets Affected Count | 12 |
| N | Documentation Location | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| L3:LN | equal  | Fill: compliant |
| L3:LN | equal  | Fill: excluded |
| F3:FN | equal  |  |
| F3:FN | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| LN | `=IF(K{row}=` |  |

---

## Sheet 9: Deviation_Register

**Purpose:** Document authorized deviations from standard configuration baselines.

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Deviation ID | 18 |
| B | Asset ID | 15 |
| C | Asset Name | 25 |
| D | Baseline ID | 20 |
| E | Deviation Type | 25 |
| F | Configuration Element | 30 |
| G | Standard Value | 25 |
| H | Actual Value | 25 |
| I | Business Justification | 40 |
| J | Risk Assessment | 12 |
| K | Compensating Controls | 35 |
| L | Approved By | 20 |
| M | Approval Date | 15 |
| N | Review Frequency | 15 |
| O | Next Review Date | 15 |
| P | Deviation Status | 15 |
| Q | Expiration Date | 15 |
| R | Notes | 35 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| J3:JN | equal  | Fill: critical |
| J3:JN | equal  | Fill: non_compliant |
| J3:JN | equal  | Fill: partial |
| J3:JN | equal  | Fill: #C6EFCE (Light Green (Compliant/Pass)) |
| P3:PN | equal  | Fill: compliant |
| P3:PN | equal  | Fill: non_compliant |
| P3:PN | equal  | Fill: partial |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| ON | `=IF(M{row}=` |  |

---

## Sheet 10: Metrics_Summary

**Purpose:** Auto-calculate key compliance metrics and executive summary (formula-driven dashboard).

**Data Rows:** 100 (rows 3–102)

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| DN:DN | greaterThanOrEqual 85 | Fill: compliant |
| DN:DN | between 70 | Fill: partial |
| DN:DN | lessThan 70 | Fill: non_compliant |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Asset_Inventory!A3:A102)-COUNTBLANK(Asset_Inventory!A3:A102)` | Total Assets in Scope |
| — | `=COUNTIF(Asset_Inventory!H3:H102,` | Assets with Defined Baselines |
| — | `=IF(B5=0,0,B6/B5*100)` | Overall Baseline Coverage % |
| — | `=COUNTIF(Asset_Inventory!E3:E102,` | Critical Asset Count |
| — | `=COUNTIFS(Asset_Inventory!E3:E102,` | Critical Assets with Baselines |
| — | `=IF(B8=0,0,B9/B8*100)` | Critical Asset Coverage % |
| — | `=IF(B11=0,0,B12/B11*100)` | High Asset Coverage % |
| — | `=COUNTIF(Approval_Tracking!E3:E52,` | Baselines Pending Approval |
| — | `=COUNTIF(Documentation_Assessment!L3:L32,` | Baselines with Excellent Documentation |
| — | `=COUNTIFS(Deviation_Register!J3:J52,` | Active High/Critical Risk Deviations |
| BN | `=COUNTIF(Asset_Inventory!$D$3:$D$102,` |  |
| CN | `=COUNTIFS(Asset_Inventory!$D$3:$D$102,` |  |
| DN | `=IF(B{row}=0,0,C{row}/B{row}*100)` |  |
| — | `=IFERROR(AVERAGE(Approval_Tracking!K3:K52),0)` | Average Approval Time (Days) |
| — | `=COUNTIF(Approval_Tracking!L3:L52,` | Baselines Exceeding SLA (>21 days) |
| — | `=IF((B{row_approved}+B{row_rejected})=0,0,B{row_approved}/(B{row_approved}+B{row` | Approval Success Rate % |

---

## Sheet 11: Evidence_Register

**Purpose:** Central register of supporting evidence and documentation.

**Frozen Panes:** B3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 18 |
| B | Evidence Type | 20 |
| C | Evidence Description | 40 |
| D | Related Asset(s) | 20 |
| E | Related Baseline(s) | 20 |
| F | Evidence Date | 15 |
| G | Evidence Location | 40 |
| H | Evidence Owner | 20 |
| I | Evidence Classification | 15 |
| J | Retention Period | 15 |
| K | Last Verified Date | 15 |
| L | Verification Status | 18 |
| M | Linked Control Requirement | 25 |
| N | Notes | 35 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| L3:LN | equal  | Fill: compliant |
| L3:LN | equal  | Fill: partial |
| L3:LN | equal  | Fill: non_compliant |
| I3:IN | equal  |  |
| I3:IN | equal  |  |

---

## Sheet 12: Approval_Sign_Off

**Purpose:** Three-tier approval signatures for the assessment.

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
| `APPROVAL_METHOD` | Change Advisory Board, Email Approval, Manager Sign-Off, Governance Committee, Automated Process |
| `APPROVAL_STATUS_BASELINE` | ✅ Approved, 🔍 Pending Review, ❌ Rejected, 📝 Draft |
| `APPROVAL_STATUS_TRACKING` | 📝 Pending Submission, 📤 Submitted, 🔍 Under Review, ✅ Approved, ❌ Rejected, ὌB Revisions Requested |
| `ASSET_CRITICALITY` | 🔴 Critical, 🟡 High, 🟢 Medium, ⭕ Low |
| `BASELINE_STATUS` | ✅ Defined, ⏳ In Progress, 🔴 Not Started, ➖ N/A |
| `CHANGE_TYPE` | Initial Release, Minor Update, Major Update, Security Patch, Emergency Change, Rollback |
| `DEVIATION_STATUS` | ✅ Active, 🔍 Under Review, ⏰ Expired, ❌ Revoked, ➖ No Longer Needed |
| `DEVIATION_TYPE` | Configuration Exception, Exclusion from Baseline, Temporary Deviation, Permanent Exception |
| `DOC_ACCESSIBILITY` | Highly Accessible, Accessible, Limited Access, Not Accessible |
| `DOC_ACCURACY` | Verified Accurate, Mostly Accurate, Contains Errors, Not Verified |
| `DOC_COMPLETENESS` | Comprehensive, Adequate, Insufficient, Missing |
| `DOC_MAINTAINABILITY` | Easy to Update, Moderate Effort, Difficult, Not Maintainable |
| `EVIDENCE_CLASSIFICATION` | Public, Internal, Confidential, Restricted |
| `EVIDENCE_TYPE` | Screenshot, Configuration File, Scan Report, Approval Record, Meeting Minutes, Email, Document, S... |
| `REMEDIATION_PRIORITY` | 🔴 Critical, 🟡 High, 🟢 Medium, ⭕ Low |
| `RETENTION_PERIOD` | 1 Year, 3 Years, 5 Years, 7 Years, Indefinite |
| `REVIEW_FREQUENCY` | Monthly, Quarterly, Semi-Annual, Annual |
| `RISK_ASSESSMENT` | ⭕ Low, 🟢 Medium, 🟡 High |
| `RISK_ASSESSMENT_DEVIATION` | ⭕ Low, 🟢 Medium, 🟡 High, 🔴 Critical |
| `VERIFICATION_STATUS` | ✅ Verified, 🔍 Needs Verification, ❌ Missing, ⏰ Outdated |

---

**END OF SPECIFICATION**

---

*"I seem to have been only like a boy playing on the seashore, and diverting myself in now and then finding a smoother pebble or a prettier shell than ordinary, whilst the great ocean of truth lay all undiscovered before me."*
— Isaac Newton

<!-- QA_VERIFIED: 2026-02-06 -->
