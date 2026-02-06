**ISMS-IMP-A.5.23.S4-TG - Ongoing Governance & Risk Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Ongoing Governance & Risk Management |
| **Related Policy** | ISMS-POL-A.5.19-23-S4 (Supplier Monitoring & Change Management), ISMS-POL-A.5.19-23-S5 (Cloud Services Security - Section 6) |
| **Purpose** | Assess ongoing governance, access reviews, change management, incident response, business continuity, and vendor risk monitoring for all cloud services |
| **Target Audience** | IT Operations, Risk Management, Compliance Officers, Business Continuity Planners, Vendor Managers, Security Teams |
| **Assessment Type** | Operational Governance & Continuous Monitoring |
| **Review Cycle** | Quarterly (with continuous monitoring) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification (Part II only) | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.23.S4-UG.

---

# Technical Specification

---

**Document:** ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management  
**Part:** II - Technical Specification  
**Section:** 1 of 4 (Workbook Overview + Sheets 1-2)  
**Version:** 1.0 
**Date:** [Date]

---

## Table of Contents - Section 1

1. **Workbook Structure Overview**
2. **Cell Styling Reference**
3. **Base Column Definitions (A-Q)**
4. **Sheet 1: Instructions & Legend**
5. **Sheet 2: Access Review & Recertification**

---

# Workbook Structure Overview

## Sheet Architecture (11 Sheets)

```
┌─────────────────────────────────────────────────────────────────────┐
│              ISMS-IMP-A.5.23.S4 WORKBOOK STRUCTURE.                 │
│              (Ongoing Governance & Risk Management)                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LAYER 1: ORIENTATION                                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 1: Instructions & Legend                                │  │
│  │          Assessment purpose, regulatory guidance, legend      │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 2: GOVERNANCE ACTIVITIES (Quarterly/Ongoing)                 │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 2: Access Review & Recertification                      │  │
│  │          24 columns (A-X): Quarterly access reviews, admin    │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 3: Change Management                                    │  │
│  │          24 columns (A-X): Provider changes, config changes   │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 4: Incident Management                                  │  │
│  │          24 columns (A-X): Detection, response, lessons       │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 5: Business Continuity                                  │  │
│  │          24 columns (A-X): BC/DR testing, RTO/RPO validation  │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 6: Vendor Risk Monitoring                               │  │
│  │          24 columns (A-X): Ongoing vendor assessment          │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 3: ANNUAL REVIEWS (NEW v2.1 - DORA Article 28.6)             │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 7: Exit Strategy Review & PoC Testing                   │  │
│  │          14 columns (A-N): Annual exit plan review + testing  │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 4: REGULATORY COMPLIANCE                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 8: Jurisdictional Risk Assessment                       │  │
│  │          20 columns (A-T): CLOUD Act, data sovereignty        │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 5: CONSOLIDATION & APPROVAL                                  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 9: Summary Dashboard                                    │  │
│  │          3 tables: Governance + Jurisdictional + Regulatory   │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 10: Evidence Register                                   │  │
│  │          Centralized evidence tracking (all sheets)           │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 11: Approval Sign-Off                                   │  │
│  │          5-stage: IT Ops → Compliance → DPO → CRO → CISO      │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Version Control

| Version | Date | Changes | Sheets Affected |
|---------|------|---------|-----------------|
| **1.0** | [Date] | Initial release (10 sheets) | All (original) |

**Key v2.1 Enhancements:**

- **NEW Sheet 7:** Exit Strategy Annual Review + PoC Testing (DORA Art. 28.6 requirement)
- **Sheet 8:** Jurisdictional Risk
- **Sheet 9:** Dashboard +1 table for exit strategy readiness
- **Sheet 11:** +DPO and CRO approval sections

## Regulatory Compliance Coverage

| Regulation | Affected Sheets | Key Requirements |
|------------|----------------|------------------|
| **DORA (Digital Operational Resilience Act)** | Sheets 4, 6, 7, 9, 11 | Incident management, ICT risk monitoring, exit strategy testing (Art. 28.6) |
| **NIS2 (Network and Information Security Directive 2)** | Sheets 4, 9, 11 | Significant incident notification (≤24h), cybersecurity measures |
| **EU AI Act** | Sheets 6, 9, 11 | High-risk AI system monitoring, post-market surveillance |
| **US CLOUD Act** | Sheet 8 | Jurisdictional risk assessment, cross-border data access exposure |

---

# Cell Styling Reference

## Style Definitions

All styles use **NEW object creation per cell** to avoid Excel "shared object" repair warnings.

| Style Name | Font | Fill Color | Alignment | Usage |
|------------|------|------------|-----------|-------|
| **header** | Calibri 14, Bold, White | Dark Blue (003366) | Center, Wrap | Section headers (Row 1) |
| **subheader** | Calibri 11, Bold, White | Medium Blue (4472C4) | Center, Wrap | Policy references (Row 2) |
| **column_header** | Calibri 10, Bold, Black | Light Gray (D9D9D9) | Center, Wrap | Column headers (Row 4) |
| **input_cell** | Calibri 10, Black | Light Yellow (FFFFCC) | Left, Wrap | Editable data cells (Rows 5-30) |
| **warning** | Calibri 10, Bold, Red | Light Orange (FFEB9C) | Left, Wrap | Warning messages |

## Border Standards

- **All cells:** Thin borders (1px solid) on all sides
- **Merged cells:** Apply border to entire merged range
- **Data rows:** Consistent thin borders for professional appearance

## Row Heights

| Row Type | Height (points) | Rationale |
|----------|-----------------|-----------|
| Section Header (Row 1) | 50 | Accommodate 2-line title + subtitle |
| Policy Reference (Row 2) | 30 | Clear policy requirement visibility |
| Spacer (Row 3) | 15 (default) | Visual separation |
| Column Headers (Row 4) | 15 (default) | Standard header height |
| Data Rows (5-30) | 15 (default) | Auto-adjust based on content |

## Column Widths

**Base columns (A-Q)** - Standard across all governance sheets (Sheets 2-6):

- Column A (Assessment_ID): 14
- Column B (Cloud_Service_Name): 28
- Column C (Vendor_Name): 22
- Column D (Service_Type): 20
- Column E (Environment): 18
- Column F (Service_Criticality): 18
- Column G (Governance_Area_Specific): 18-20 (varies by sheet)
- Column H (Configuration_Item): 30
- Column I (Status): 15
- Column J (Evidence_Location): 30
- Column K (Gap_Description): 35
- Column L (Remediation_Needed): 16
- Column M (Exception_ID): 14
- Column N (Risk_ID): 14
- Column O (Compensating_Controls): 30
- Column P (Responsible_Team): 20
- Column Q (Target_Remediation_Date): 18

**Extended columns (R-X)** - Vary by sheet (see individual sheet specs)

---

# Base Column Definitions (A-Q)

## Standard Columns for ALL Governance Assessment Sheets

These 17 columns (A-Q) are **identical** across Sheets 2-6 to enable dashboard consolidation.

| Column | Field Name | Width | Data Type | Validation | Formula | Description |
|--------|-----------|-------|-----------|------------|---------|-------------|
| **A** | Assessment_ID | 14 | Formula | - | `=CONCATENATE("GOV-",TEXT(ROW()-4,"000"))` | Auto-generated unique ID (GOV-001, GOV-002, etc.) |
| **B** | Cloud_Service_Name | 28 | Text | - | - | Service name (import from IMP-5.23.1 Sheet 2 Column B) |
| **C** | Vendor_Name | 22 | Text | - | - | Vendor/provider name (import from IMP-5.23.1 Sheet 2 Column C) |
| **D** | Service_Type | 20 | Dropdown | SaaS, IaaS, PaaS, Security Service, Storage Service | - | Cloud service category |
| **E** | Environment | 18 | Dropdown | Production, Staging, Development, Test, All Environments | - | Where this service is deployed |
| **F** | Service_Criticality | 18 | Dropdown | Critical, High, Medium, Low | - | Business impact if unavailable (from IMP-5.23.1) |
| **G** | Governance_Area | 18-20 | Dropdown | **VARIES BY SHEET** (see sheet-specific specs) | - | Sheet-specific governance dimension |
| **H** | Configuration_Item | 30 | Text | - | - | Specific governance item being assessed |
| **I** | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | - | Governance compliance status |
| **J** | Evidence_Location | 30 | Text | - | - | Path/URL to evidence file |
| **K** | Gap_Description | 35 | Text | - | - | If not Compliant: describe the gap |
| **L** | Remediation_Needed | 16 | Dropdown | Yes, No, N/A | - | Does this gap require remediation? |
| **M** | Exception_ID | 14 | Text | - | - | If exception approved: reference exception document ID |
| **N** | Risk_ID | 14 | Text | - | - | If risk accepted: reference risk register entry |
| **O** | Compensating_Controls | 30 | Text | - | - | Alternative controls if governance item not fully compliant |
| **P** | Responsible_Team | 20 | Dropdown | IT Operations, Cloud Ops, Security, Compliance, Risk Management | - | Team responsible for remediation |
| **Q** | Target_Remediation_Date | 18 | Date | - | - | Target date to close gap (if remediation needed) |

## Data Validation Rules (Base Columns)

**Dropdowns implemented via `openpyxl.worksheet.datavalidation.DataValidation`:**

```python
# Service Type (Column D)
service_type_dv = DataValidation(
    type="list",
    formula1='"SaaS,IaaS,PaaS,Security Service,Storage Service"',
    allow_blank=False
)
ws.add_data_validation(service_type_dv)
service_type_dv.add("D5:D30")

# Environment (Column E)
environment_dv = DataValidation(
    type="list",
    formula1='"Production,Staging,Development,Test,All Environments"',
    allow_blank=False
)
ws.add_data_validation(environment_dv)
environment_dv.add("E5:E30")

# Service Criticality (Column F)
criticality_dv = DataValidation(
    type="list",
    formula1='"Critical,High,Medium,Low"',
    allow_blank=False
)
ws.add_data_validation(criticality_dv)
criticality_dv.add("F5:F30")

# Status (Column I) - with UTF-8 symbols
status_dv = DataValidation(
    type="list",
    formula1=f'"{CHECK} Compliant,{WARNING} Partial,{XMARK} Non-Compliant,N/A"',
    allow_blank=False
)
ws.add_data_validation(status_dv)
status_dv.add("I5:I30")

# Remediation Needed (Column L)
yes_no_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(yes_no_dv)
yes_no_dv.add("L5:L30")

# Responsible Team (Column P)
responsible_team_dv = DataValidation(
    type="list",
    formula1='"IT Operations,Cloud Ops,Security,Compliance,Risk Management"',
    allow_blank=False
)
ws.add_data_validation(responsible_team_dv)
responsible_team_dv.add("P5:P30")
```

## UTF-8 Symbol Encoding

**Status symbols used in dropdowns:**

```python
CHECK = '\u2705'      # ✅ Green checkmark (Compliant)
WARNING = '\u26A0'    # ⚠️ Warning sign (Partial)
XMARK = '\u274C'      # ❌ Red X (Non-Compliant)
```

---

# Sheet 1: Instructions & Legend

## Purpose & Layout

**Sheet Name:** `Instructions & Legend`

**Purpose:** Provide user orientation, governance assessment context, status legend, evidence requirements, and regulatory applicability guidance.

**Layout:** Free-form text layout with merged cells, no data validation (read-only reference).

## Sheet Structure

```
┌───────────────────────────────────────────────────────────────┐
│ Row 1:  ISMS-IMP-A.5.23.S4 – Ongoing Governance v2.1          │
│         (Header, merged A1:C1)                                │
├───────────────────────────────────────────────────────────────┤
│ Row 2:  ISO/IEC 27001:2022 - Control A.5.23                   │
│         (Subheader, merged A2:C2)                             │
├───────────────────────────────────────────────────────────────┤
│ Row 4+: DOCUMENT INFORMATION                                  │
│         - Document ID: ISMS-IMP-A.5.23.S4                     │
│         - Assessment Area: Ongoing Governance & Risk Mgmt     │
│         - Related Policy: ISMS-POL-A.5.19-23-S5 Section 6     │
│         - Version: 2.1 (DORA Exit Strategy Update)            │
│         - Assessment Date: [Input field]                      │
│         - Completed By: [Input field]                         │
│         - Organization: [Input field]                         │
│         - Review Cycle: Quarterly (+ Annual Exit Review)      │
├───────────────────────────────────────────────────────────────┤
│ HOW TO USE THIS WORKBOOK (Step-by-step instructions)          │
├───────────────────────────────────────────────────────────────┤
│ SHEET NAVIGATION GUIDE (11 sheets explained)                  │
├───────────────────────────────────────────────────────────────┤
│ STATUS LEGEND (✅ ⚠️ ❌ N/A definitions)                      │
├───────────────────────────────────────────────────────────────┤
│ EVIDENCE REQUIREMENTS (logs, reports, test results)           │
├───────────────────────────────────────────────────────────────┤
│ REGULATORY APPLICABILITY GUIDE (DORA/NIS2/AI Act/CLOUD Act)   │
├───────────────────────────────────────────────────────────────┤
│ VERSION HISTORY (1.0 → 2.0 → 2.1 updates)                     │
├───────────────────────────────────────────────────────────────┤
│ CONTACT INFORMATION (coordinator, IT ops, compliance, CISO)   │
└───────────────────────────────────────────────────────────────┘
```

## Key Content Sections

### Document Information

| Attribute | Value | Notes |
|-------|-------|-------|
| Document ID | ISMS-IMP-A.5.23.S4 | Fixed |
| Assessment Area | Ongoing Governance & Risk Management | Fixed |
| Related Policy | ISMS-POL-A.5.19-23-S5 Section 6 | Fixed |
| Version | 2.1 (DORA Exit Strategy Update) | Fixed |
| Assessment Date | [Input field] | Yellow fill, user-editable |
| Completed By | [Input field] | Yellow fill, user-editable |
| Organization | [Input field] | Yellow fill, user-editable |
| Review Cycle | Quarterly (+ Annual Exit Review) | Fixed |

### How to Use This Workbook

**Instructions (summary):**
1. Reference ISMS-IMP-A.5.23.S1 (Inventory) for service list
2. Complete Sheets 2-6 for quarterly governance activities
3. Complete Sheet 7 annually for exit strategy review (DORA requirement)
4. Complete Sheet 8 for jurisdictional risk (US-nexus providers only)
5. Use dropdown menus for standardized entries
6. Provide evidence links for all governance claims
7. Dashboard formulas automatically calculate compliance
8. Review evidence register for completeness
9. Obtain sequential approvals (IT Ops → Compliance → DPO → CRO → CISO)

### Sheet Navigation Guide

**11-Sheet Overview:**

| Sheet # | Sheet Name | Purpose | Review Frequency |
|---------|------------|---------|------------------|
| 1 | Instructions & Legend | Orientation | Read first |
| 2 | 2. Access Review | Quarterly access recertification | Quarterly |
| 3 | 3. Change Management | Provider/config change tracking | Quarterly + ongoing |
| 4 | 4. Incident Management | Security/availability incidents | Quarterly + ongoing |
| 5 | 5. Business Continuity | BC/DR testing, RTO/RPO validation | Quarterly + annual full test |
| 6 | 6. Vendor Risk Monitoring | Ongoing vendor assessment | Quarterly + triggered |
| 7 | 7. Exit Strategy Review | Annual exit plan + PoC testing (DORA) | **Annually** |
| 8 | 8. Jurisdictional Risk | CLOUD Act exposure (US vendors) | Quarterly + triggered |
| 9 | 9. Summary Dashboard | Compliance metrics, gaps | Auto-calculated |
| 10 | 10. Evidence Register | Evidence tracking | As evidence collected |
| 11 | 11. Approval Sign-Of | 5-stage approval workflow | After assessment complete |

### Status Legend

| Symbol | Status | Definition | Usage |
|--------|--------|------------|-------|
| ✅ | Compliant | Governance activity completed per requirements, evidence provided | Use when governance item verified compliant |
| ⚠️ | Partial | Governance activity partially compliant, minor gaps exist | Use when mostly compliant but improvements needed |
| ❌ | Non-Compliant | Governance activity fails requirements, remediation required | Use when governance item is missing/inadequate |
| N/A | Not Applicable | Governance item not relevant to this service/environment | Use when governance item doesn't apply |

### Evidence Requirements

**Acceptable Evidence Types by Governance Area:**

| Governance Area | Evidence Type | Example |
|--------------------|---------------|---------|
| Access Review | Access review report export | Quarterly access review report (CSV/PDF) from IAM system |
| Change Management | Change ticket log | ServiceNow change ticket screenshots/export |
| Incident Management | Incident management report | Incident log from SIEM, MTTR metrics report |
| Business Continuity | BC/DR test report | Annual BC test results, RTO/RPO achievement |
| Vendor Risk | Vendor risk assessment | Vendor risk scorecard, security incident notifications |
| Exit Strategy | Exit plan document + PoC test report | Exit strategy document + annual PoC test results (DORA) |
| Jurisdictional Risk | Legal assessment memo | DPO/Legal opinion on CLOUD Act exposure |

**Evidence Location Format:**

- **File share:** `\\fileserver\ISMS\Evidence\A.5.23.4\[Service_Name]\[Governance_Area]\[Filename]`
- **SharePoint:** `https://[org].sharepoint.com/sites/ISMS/Evidence/A.5.23.4/[Service]/[File]`
- **ITSM:** Ticket IDs (INC-###, CHG-###, RITM-###)

### Regulatory Applicability Guide (v2.1 UPDATE)

**When to Complete Regulatory Sheets/Columns:**

| Regulation | Applies If... | Required Sheets | Required Columns |
|------------|---------------|-----------------|------------------|
| **DORA** | [Organization] is EU financial institution or critical ICT provider | Sheet 4 (Incident Mgmt), Sheet 7 (Exit Strategy) | Sheet 7: ALL columns (A-N) - Annual exit plan review |
| **NIS2** | [Organization] is Essential/Important Entity under NIS2 | Sheet 4 (Incident Mgmt) | Sheet 4: Enhanced incident notification tracking |
| **EU AI Act** | Cloud service includes high-risk AI components | Sheet 6 (Vendor Risk) | Sheet 6: AI system monitoring requirements |
| **US CLOUD Act** | Cloud provider has US nexus (HQ, subsidiary, operations in US) | Sheet 8 (Jurisdictional Risk) | Sheet 8: ALL columns (A-T) |

**NEW in v2.1 - DORA Article 28.6 Exit Strategy Requirement:**

```
If [Organization] is subject to DORA (EU financial institutions):
  ├─ Complete Sheet 7 (Exit Strategy Annual Review) ANNUALLY
  ├─ Conduct Proof-of-Concept (PoC) testing of exit strategies ANNUALLY
  ├─ Document PoC test results (Column J-N)
  └─ Report results to management and supervisory authorities

Otherwise:
  └─ Sheet 7 is OPTIONAL (but recommended as best practice)
```

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial release (10 sheets, no regulatory) |

---

# Sheet 2: Access Review & Recertification

## Purpose & Layout

**Sheet Name:** `2. Access Review`

**Purpose:** Assess quarterly access reviews and admin access recertification for all cloud services.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.1 (Access Management)

**Assessment Question:** "Are access reviews conducted quarterly with admin/privileged access recertified and documented?"

## Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns (see Section 3)

**Column G Specialization:** `Review_Period` (Dropdown: Q1, Q2, Q3, Q4, Annual)

**Extended Columns (R-X):** Access review-specific

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **R** | Last_Review_Date | 18 | Date | - | Date of last access review |
| **S** | Admin_Count | 14 | Integer | Positive integer | Number of admin/privileged accounts |
| **T** | Admin_Recertified | 18 | Dropdown | Yes, No, Pending | Were admin accounts recertified by business owner? |
| **U** | Inactive_Accounts_Disabled | 20 | Dropdown | Yes, No, Partial | Were inactive accounts (>90 days) disabled? |
| **V** | Orphaned_Accounts_Removed | 20 | Dropdown | Yes, No, Partial | Were orphaned accounts (user left org) removed? |
| **W** | JIT_Access_Used | 16 | Dropdown | Yes, No, N/A | Is Just-In-Time (JIT) access used for admin privileges? |
| **X** | Next_Review_Due | 18 | Date | Formula: `=R+90` | Next quarterly review date (90 days from last) |

## Data Validation Rules (Extended Columns)

```python
# Admin Count (Column S)
admin_count_dv = DataValidation(
    type="whole",
    operator="greaterThanOrEqual",
    formula1="0",
    allow_blank=True
)
ws.add_data_validation(admin_count_dv)
admin_count_dv.add("S5:S30")

# Admin Recertified (Column T)
admin_recertified_dv = DataValidation(
    type="list",
    formula1='"Yes,No,Pending"',
    allow_blank=False
)
ws.add_data_validation(admin_recertified_dv)
admin_recertified_dv.add("T5:T30")

# Inactive Accounts Disabled (Column U)
inactive_accounts_dv = DataValidation(
    type="list",
    formula1='"Yes,No,Partial"',
    allow_blank=False
)
ws.add_data_validation(inactive_accounts_dv)
inactive_accounts_dv.add("U5:U30")

# Orphaned Accounts Removed (Column V)
orphaned_accounts_dv = DataValidation(
    type="list",
    formula1='"Yes,No,Partial"',
    allow_blank=False
)
ws.add_data_validation(orphaned_accounts_dv)
orphaned_accounts_dv.add("V5:V30")

# JIT Access Used (Column W)
jit_access_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(jit_access_dv)
jit_access_dv.add("W5:W30")
```

## Section Headers

```
Row 1 (merged A1:X1):
  "ACCESS REVIEW & RECERTIFICATION ASSESSMENT
   ISMS-POL-A.5.19-23-S5, Section 6.1: Quarterly Access Reviews"

Row 2 (merged A2:X2):
  "Assessment Question: Are access reviews conducted quarterly with 
   admin/privileged access recertified and documented?"
```

## Compliance Checklist (Rows 33+)

**Checklist Items (15 items):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | Access reviews conducted quarterly for ALL cloud services | Access review schedule/calendar |
| 2 | Admin/privileged accounts recertified by business owner | Admin recertification report |
| 3 | Inactive accounts (>90 days) disabled automatically | IAM lifecycle policy config |
| 4 | Orphaned accounts (user left org) removed within 24 hours | Offboarding process doc |
| 5 | Service accounts inventoried and reviewed | Service account inventory |
| 6 | Access rights aligned with current job roles | Access review delta report |
| 7 | Just-In-Time (JIT) access implemented for admin privileges | PAM tool configuration |
| 8 | Access review results documented with approvals | Signed review report |
| 9 | Privilege creep identified and remediated | Access rightsizing report |
| 10 | Emergency access (break-glass) accounts reviewed | Break-glass account log |
| 11 | MFA enforced for all admin accounts (minimum) | MFA enforcement report |
| 12 | Access review deviations escalated to management | Exception log |
| 13 | Federated identity used (no local cloud accounts) | IdP integration validation |
| 14 | Access review metrics reported to CISO quarterly | Access metrics dashboard |
| 15 | Automated reminders sent to service owners before due date | Reminder email logs |

## Example Data Row

**Row 7 (Example - AWS Production Account):**

| Col | Value | Notes |
|-----|-------|-------|
| A | GOV-003 | Auto-generated |
| B | AWS Production Account | Service name |
| C | Amazon Web Services | Vendor |
| D | IaaS | Service type |
| E | Production | Environment |
| F | Critical | Criticality |
| G | Q1 | Review period |
| H | IAM User Access Review | Config item |
| I | ✅ Compliant | Status |
| J | `s3://isms-evidence/A.5.23.4/AWS/Q1_Access_Review.pdf` | Evidence path |
| K | - | No gap |
| L | No | No remediation |
| M | - | No exception |
| N | - | No risk ID |
| O | - | No compensating controls |
| P | IT Operations | Responsible team |
| Q | - | No target date |
| R | 15.01.2026 | Last review date |
| S | 8 | Admin count |
| T | Yes | Admin recertified |
| U | Yes | Inactive accounts disabled (automated) |
| V | Yes | Orphaned accounts removed (HR integration) |
| W | Yes | JIT via AWS IAM Identity Center |
| X | 15.04.2026 | Next review due (90 days) |

## Integration Points

**Exports to Sheet 9 (Dashboard):**

- Column I (Status): Access review compliance metrics
- Column R (Last_Review_Date): Overdue review tracking
- Column T (Admin_Recertified): Admin recertification compliance

**Exports to Sheet 10 (Evidence Register):**

- Column J (Evidence_Location): Access review evidence tracking

---

---

**Document:** ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management  
**Part:** II - Technical Specification  
**Sections:** 2-4 (Complete remaining sheets + integration)  
**Version:** 1.0  
**Date:** [Date]

---

# SECTION 2: SHEETS 3-6 (GOVERNANCE ACTIVITIES)

## Sheet 3: Change Management

### Purpose & Layout

**Sheet Name:** `3. Change Management`

**Purpose:** Track all changes to cloud services (provider changes, configuration changes, integrations) and ensure proper approval/review.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.2 (Change Management)

**Assessment Question:** "Are all cloud service changes following change management process with proper approvals?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `Change_Type` (Dropdown: Provider Change, Config Change, Integration Change, Emergency Change, Scheduled Maintenance)

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Change_Count_Period | 18 | Integer | ≥0 |
| **S** | Impact_Level | 16 | Dropdown | Critical, High, Medium, Low |
| **T** | Approval_Status | 18 | Dropdown | Approved, Pending, Rejected, Emergency |
| **U** | Rollback_Plan_Documented | 20 | Dropdown | Yes, No, N/A |
| **V** | Rollback_Tested | 16 | Dropdown | Yes, No, N/A |
| **W** | Post_Change_Review_Done | 20 | Dropdown | Yes, No, Pending |
| **X** | Security_Impact_Assessed | 20 | Dropdown | Yes, No, N/A |

### Compliance Checklist (15 items)

```
☐ Change management process documented for cloud services
☐ Provider change notifications monitored and assessed
☐ Configuration changes require security review before approval
☐ Integration changes assessed for data flow impact
☐ Emergency change process defined with post-review requirement
☐ Emergency changes reviewed within 48 hours
☐ Rollback procedures documented for critical changes
☐ Rollback procedures tested before go-live (critical changes)
☐ Change calendar maintained and communicated
☐ Change conflicts identified and resolved
☐ Security impact assessment required for all changes
☐ Change audit trail maintained in ticketing system
☐ Failed changes documented with root cause
☐ Change success metrics tracked (success rate, rollback rate)
☐ Provider maintenance windows tracked and planned for
```

---

## Sheet 4: Incident Management

### Purpose & Layout

**Sheet Name:** `4. Incident Management`

**Purpose:** Track cloud service incidents (security, availability, performance) and lessons learned.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.3 (Incident Management)

**Assessment Question:** "Are cloud service incidents detected, responded to, and documented per incident management procedures?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `Incident_Severity` (Dropdown: P1-Critical, P2-High, P3-Medium, P4-Low)

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Incident_Count_Period | 18 | Integer | ≥0 |
| **S** | MTTR_Hours | 14 | Decimal | ≥0 |
| **T** | Root_Cause_Documented | 20 | Dropdown | Yes, No, Pending |
| **U** | Playbook_Updated | 16 | Dropdown | Yes, No, N/A |
| **V** | Vendor_Notified | 16 | Dropdown | Yes, No, N/A |
| **W** | Customer_Impact | 18 | Dropdown | Yes, No, Unknown |
| **X** | Lessons_Learned_Captured | 20 | Dropdown | Yes, No, Pending |

### Compliance Checklist (30 items - REGULATORY ENHANCED)

**Base Items (15):**
```
☐ Incident detection mechanisms in place for cloud services
☐ Alerting thresholds defined and tuned
☐ Incident classification aligned with org severity matrix
☐ Escalation paths defined for cloud service incidents
☐ Vendor notification procedures documented
☐ Vendor incident response SLAs tracked
☐ Internal incident response playbooks exist per service
☐ Playbooks reviewed/updated after incidents
☐ Root cause analysis performed for P1/P2 incidents
☐ Lessons learned documented and shared
☐ Problem management process identifies recurring issues
☐ Known error database maintained for cloud services
☐ Incident metrics reported to management
☐ MTTR/MTTD tracked per service
☐ Post-incident reviews conducted within defined timeframe
```

**DORA Items (+8):**
```
☐ ICT-related incidents classified per DORA Article 17
☐ Major incidents reported to senior management immediately
☐ Incident impact on critical operations documented
☐ Incident root cause traced to ICT dependency (vendor/config)
☐ Third-party incident monitoring activated
☐ Incident severity escalation to authorities (if major)
☐ ICT incident register maintained and reviewed quarterly
☐ Lessons learned integrated into ICT risk management
```

**NIS2 Items (+5):**
```
☐ Significant cybersecurity incidents identified per NIS2
☐ Incident notification to authorities within 24h (significant)
☐ Incident intermediate report within 72h (if applicable)
☐ Final incident report prepared within 1 month
☐ Cross-border incident coordination with other MS authorities
```

**AI Act Items (+6):**
```
☐ High-risk AI system incidents categorized separately
☐ AI system failure incidents logged with input/output data
☐ AI safety incident impact on human rights documented
☐ Post-market monitoring incident review conducted
☐ Serious AI incidents reported to market surveillance authority
☐ AI incident corrective actions implemented and verified
```

---

## Sheet 5: Business Continuity

### Purpose & Layout

**Sheet Name:** `5. Business Continuity`

**Purpose:** Track BC/DR testing, RTO/RPO validation, and failover capabilities for cloud services.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.4 (Business Continuity)

**Assessment Question:** "Are BC/DR plans tested annually with RTO/RPO achievement verified?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `BC_Tier` (Dropdown: Tier 1 (<4hr), Tier 2 (<24hr), Tier 3 (<72hr), Tier 4 (Best Effort))

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Last_Test_Date | 16 | Date | - |
| **S** | Test_Result | 16 | Dropdown | Passed, Failed, Partial, Not Tested |
| **T** | RTO_Target_Hours | 16 | Decimal | ≥0 |
| **U** | RTO_Achieved_Hours | 18 | Decimal | ≥0 |
| **V** | RPO_Target_Hours | 16 | Decimal | ≥0 |
| **W** | RPO_Achieved_Hours | 18 | Decimal | ≥0 |
| **X** | Next_Test_Due | 16 | Date | Formula: `=R5+365` |

### Compliance Checklist (15 items)

```
☐ BC/DR plan documented for Critical/High services
☐ Vendor BC/DR capabilities verified and documented
☐ RTO requirements defined per service criticality
☐ RPO requirements defined per data classification
☐ Failover procedures documented and accessible
☐ Failover tested annually (minimum)
☐ Test results documented with evidence
☐ RTO achievement verified during tests
☐ RPO achievement verified during tests
☐ Data backup restoration tested
☐ Multi-region/availability zone strategy documented
☐ Single points of failure identified and mitigated
☐ Communication plan exists for BC events
☐ Vendor dependency chain mapped for BC planning
☐ BC plan reviewed after significant changes
```

---

## Sheet 6: Vendor Risk Monitoring

### Purpose & Layout

**Sheet Name:** `6. Vendor Risk Monitoring`

**Purpose:** Ongoing monitoring of vendor security posture, certification expiry, incidents, financial health.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.5 (Vendor Risk Management)

**Assessment Question:** "Is cloud vendor risk monitored continuously with reassessment triggered by changes?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `Risk_Rating` (Dropdown: Critical, High, Medium, Low, Minimal)

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Risk_Score_Trend | 18 | Dropdown | Improving, Stable, Degrading, Unknown |
| **S** | Security_Incidents_YTD | 20 | Integer | ≥0 |
| **T** | Cert_Expiry_Tracked | 18 | Dropdown | Yes, No, N/A |
| **U** | Next_Cert_Expiry | 16 | Date | - |
| **V** | Financial_Health | 18 | Dropdown | Strong, Stable, Concerning, Unknown |
| **W** | Last_Assessment_Date | 18 | Date | - |
| **X** | Reassessment_Trigger_Met | 20 | Dropdown | Yes, No |

### Compliance Checklist (15 items)

```
☐ Vendor risk assessment performed at onboarding
☐ Annual vendor risk reassessment scheduled
☐ Risk scoring methodology documented and consistent
☐ Security certifications tracked (ISO 27001, SOC 2, etc.)
☐ Certification expiry dates monitored with alerts
☐ Vendor security incidents monitored via news/feeds
☐ Vendor breach notification process documented
☐ Financial health indicators monitored for critical vendors
☐ Vendor concentration risk assessed
☐ Sub-processor changes tracked and assessed
☐ Geopolitical risk factors considered
☐ Vendor security questionnaire refreshed periodically
☐ Risk rating changes trigger stakeholder notification
☐ High-risk vendors subject to enhanced monitoring
☐ Vendor risk dashboard available to stakeholders
```

---

# SECTION 3: SHEETS 7-9 (ANNUAL REVIEWS + DASHBOARD)

## Sheet 7: Exit Strategy Annual Review & PoC Testing (NEW v2.1)

### Purpose & Layout

**Sheet Name:** `7. Exit Strategy Review`

**Purpose:** Annual review of exit strategies + Proof-of-Concept (PoC) testing per DORA Article 28.6.

**Regulatory Driver:** DORA Article 28.6 requires financial institutions to annually review and test exit strategies for ICT services.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 8 (Exit Strategy)

**Assessment Question:** "Is the exit strategy reviewed annually with PoC testing demonstrating feasibility?"

### Column Structure (A-N, 14 columns)

| Column | Field Name | Width | Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Review_ID | 14 | Formula | - | `=CONCATENATE("EXIT-",TEXT(ROW()-4,"000"))` |
| **B** | Cloud_Service_Name | 28 | Text | - | Service name |
| **C** | Vendor_Name | 22 | Text | - | Vendor/provider |
| **D** | Exit_Strategy_Documented | 20 | Dropdown | Yes, No, Partial | Exit plan exists? |
| **E** | Last_Annual_Review_Date | 18 | Date | - | Last review date |
| **F** | Next_Review_Due | 18 | Date | Formula: `=E5+365` | Next annual review |
| **G** | Review_Outcome | 16 | Dropdown | Adequate, Needs Update, Critical Gaps | Review result |
| **H** | PoC_Test_Conducted | 18 | Dropdown | Yes, No, Planned | PoC test done? |
| **I** | PoC_Test_Date | 16 | Date | - | When PoC tested |
| **J** | PoC_Test_Result | 16 | Dropdown | Successful, Partial, Failed, Not Tested | PoC outcome |
| **K** | Data_Portability_Verified | 20 | Dropdown | Yes, No, Partial | Can export data? |
| **L** | Alternative_Provider_Identified | 22 | Dropdown | Yes, No, In Progress | Backup vendor? |
| **M** | Responsible_Team | 20 | Dropdown | IT Operations, Cloud Ops, Business Continuity | Who owns exit plan |
| **N** | Next_PoC_Test_Due | 18 | Date | Formula: `=I5+365` | Next PoC test |

### Compliance Checklist (12 items - DORA-specific)

```
☐ Exit strategy documented for all cloud services (DORA Art. 28.6)
☐ Exit plan includes data extraction procedures
☐ Exit plan includes service migration steps
☐ Exit plan includes contract termination process
☐ Annual review conducted by business and technical teams
☐ Proof-of-Concept (PoC) test conducted annually
☐ PoC test validates data portability (complete extraction)
☐ PoC test validates alternative provider feasibility
☐ PoC test results documented with evidence
☐ PoC failures documented with remediation plan
☐ Exit strategy reviewed after vendor M&A or major changes
☐ Exit readiness status reported to senior management/board
```

### Example Data Row

**Row 5 (Example - Salesforce CRM):**

| Col | Value | Notes |
|-----|-------|-------|
| A | EXIT-001 | Auto-generated |
| B | Salesforce Sales Cloud | Service name |
| C | Salesforce Inc. | Vendor |
| D | Yes | Exit strategy documented |
| E | 01.02.2026 | Last annual review |
| F | 01.02.2027 | Next review due |
| G | Adequate | Review outcome |
| H | Yes | PoC test conducted |
| I | 15.02.2026 | PoC test date |
| J | Successful | PoC test result (full data export via API successful) |
| K | Yes | Data portability verified (CRM data exported to CSV) |
| L | Yes | Alternative provider identified (HubSpot, Dynamics 365) |
| M | Business Continuity | Responsible team |
| N | 15.02.2027 | Next PoC test due |

---

## Sheet 8: Jurisdictional Risk Assessment (CLOUD Act)

### Purpose & Layout

**Sheet Name:** `8. Jurisdictional Risk`

**Purpose:** Assess CLOUD Act exposure for US-headquartered cloud providers and cross-border data access risks.

**Regulatory Driver:** US CLOUD Act allows US government to compel US companies to produce data stored anywhere.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 7 (Data Sovereignty & Jurisdictional Risk)

**Assessment Question:** "For US-nexus providers, what is the jurisdictional risk and what mitigations are in place?"

### Column Structure (A-T, 20 columns)

| Column | Field Name | Width | Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Assessment_ID | 14 | Formula | - | `=CONCATENATE("JUR-",TEXT(ROW()-4,"000"))` |
| **B** | Cloud_Service_Name | 28 | Text | - | Service name |
| **C** | Vendor_Name | 22 | Text | - | Vendor/provider |
| **D** | Provider_HQ_Jurisdiction | 20 | Dropdown | Switzerland, EU/EEA, UK, US, Other Adequate, Non-Adequate | Where HQ located |
| **E** | US_Parent_Company | 18 | Dropdown | Yes, No, Unknown | Is parent company US-based? |
| **F** | CLOUD_Act_Exposure | 18 | Dropdown | No Exposure, Potential (US HQ), Mitigated (EU Boundary), Mitigated (Encryption+Keys), Accepted Risk, Under Assessment | CLOUD Act risk |
| **G** | Data_Processing_Locations | 22 | Text | - | Where data stored/processed |
| **H** | EU_Data_Boundary_Available | 20 | Dropdown | Yes, No, Unknown | Vendor offers EU boundary? |
| **I** | EU_Data_Boundary_Enabled | 20 | Dropdown | Yes, No, N/A | Is EU boundary configured? |
| **J** | Customer_Managed_Keys | 18 | Dropdown | Yes, No, Partial | Customer controls encryption keys? |
| **K** | Legal_Challenge_Commitment | 20 | Dropdown | Yes, No, Unknown | Vendor commits to challenge requests? |
| **L** | Transfer_Mechanism | 18 | Dropdown | SCCs, BCRs, Adequacy Decision, None | Legal basis for data transfer |
| **M** | SCCs_In_DPA | 16 | Dropdown | Yes, No, N/A | SCCs included in DPA? |
| **N** | Residual_Risk_Level | 16 | Dropdown | Low, Medium, High, Critical | After mitigations, what's risk? |
| **O** | Risk_Owner | 18 | Dropdown | DPO, Legal, CISO, Business Unit | Who owns this risk? |
| **P** | Risk_Acceptance_Date | 18 | Date | - | When risk accepted |
| **Q** | Compensating_Controls | 30 | Text | - | Additional controls |
| **R** | Next_Review_Date | 18 | Date | Formula: `=P5+90` | Next quarterly review |
| **S** | Evidence_ID | 14 | Text | - | Link to evidence register |
| **T** | Notes | 35 | Text | - | Additional context |

### Applicability

**Complete this sheet ONLY IF:**

- Cloud provider has US nexus (HQ, subsidiary, or significant US operations)

**Examples of US-nexus providers:**

- Microsoft, AWS, Google Cloud, Oracle Cloud, Salesforce, Adobe, Snowflake, ServiceNow, Workday, Okta, Zoom, Slack, Box, Dropbox, etc.

**Skip this sheet if:**

- Provider is EU/EEA-only (OVH, Hetzner, IONOS)
- Provider is Swiss (Proton, Infomaniak)
- Provider is UK-only with no US parent

### Example Data Row

**Row 5 (Example - Microsoft 365 with EU Data Boundary):**

| Col | Value |
|-----|-------|
| A | JUR-001 |
| B | Microsoft 365 |
| C | Microsoft Corporation |
| D | US |
| E | Yes (Microsoft Corp is US-based) |
| F | Mitigated (EU Boundary) |
| G | EU Data Boundary: Germany, France, Netherlands |
| H | Yes |
| I | Yes (EU Data Boundary enabled for tenant) |
| J | Partial (Customer-managed keys for email, not SharePoint) |
| K | Yes (Microsoft committed to legal challenge in MS Cloud Act transparency report) |
| L | SCCs |
| M | Yes (EU SCCs in DPA) |
| N | Medium (residual risk due to CMK partial coverage) |
| O | DPO |
| P | 15.01.2026 |
| Q | Vendor commitment to legal challenge + Enhanced monitoring |
| R | 15.04.2026 |
| S | EV-GOV-045 |
| T | DPO reviewed, acceptable with compensating controls |

---

## Sheet 9: Summary Dashboard

### Purpose & Layout

**Sheet Name:** `9. Summary Dashboard`

**Purpose:** Auto-calculated compliance metrics, governance health score, jurisdictional risk summary, regulatory compliance status.

**Layout:** Read-only formulas, no user input (except references to other sheets).

### Dashboard Structure (3 Main Tables)

**TABLE 1: Governance Compliance Summary (Rows 4-10)**

| Assessment Area | Total Items | Compliant | Partial | Non-Compliant | N/A | Compliance % |
|-----------------|-------------|-----------|---------|---------------|-----|--------------|
| 2. Access Review | `=COUNTA('2. Access Review'!I5:I30)` | `=COUNTIF('2. Access Review'!I5:I30,CHECK&" Compliant")` | `=COUNTIF('2. Access Review'!I5:I30,WARNING&" Partial")` | `=COUNTIF('2. Access Review'!I5:I30,XMARK&" Non-Compliant")` | `=COUNTIF('2. Access Review'!I5:I30,"N/A")` | `=IF(B5>0,ROUND((C5/B5)*100,0),"N/A")` |
| 3. Change Mgmt | ... | ... | ... | ... | ... | ... |
| 4. Incident Mgmt | ... | ... | ... | ... | ... | ... |
| 5. Business Continuity | ... | ... | ... | ... | ... | ... |
| 6. Vendor Risk | ... | ... | ... | ... | ... | ... |
| **TOTAL** | `=SUM(B5:B9)` | `=SUM(C5:C9)` | `=SUM(D5:D9)` | `=SUM(E5:E9)` | `=SUM(F5:F9)` | `=ROUND(AVERAGE(G5:G9),0)` |

**TABLE 2: Key Governance Metrics (Rows 13-20)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Cloud Services Assessed | `=COUNTA('2. Access Review'!B5:B30)` | - | Info |
| Services Requiring Remediation | `=COUNTIF('2. Access Review'!L5:L30,"Yes")` | 0 | `=IF(B14>0,"❌ Action","✅ OK")` |
| Overdue Access Reviews | `=COUNTIFS('2. Access Review'!R5:R30,"<"&TODAY()-90,'2. Access Review'!I5:I30,"<>N/A")` | 0 | `=IF(B15>0,"❌ Action","✅ OK")` |
| Open P1/P2 Incidents | `=COUNTIF('4. Incident Management'!G5:G30,"P1*")+COUNTIF('4. Incident Management'!G5:G30,"P2*")` | 0 | `=IF(B16>0,"⚠️ Review","✅ OK")` |
| BC Tests Overdue | `=COUNTIFS('5. Business Continuity'!R5:R30,"<"&TODAY()-365,'5. Business Continuity'!I5:I30,"<>N/A")` | 0 | `=IF(B17>0,"❌ Action","✅ OK")` |
| High-Risk Vendors | `=COUNTIF('6. Vendor Risk Monitoring'!G5:G30,"High")+COUNTIF('6. Vendor Risk Monitoring'!G5:G30,"Critical")` | <3 | `=IF(B18>3,"⚠️ Review","✅ OK")` |
| Exit Strategies Not Reviewed (Annual) | `=COUNTIFS('7. Exit Strategy Review'!E5:E30,"<"&TODAY()-365,'7. Exit Strategy Review'!D5:D30,"Yes")` | 0 | `=IF(B19>0,"❌ Action","✅ OK")` |
| Jurisdictional Risks (High/Critical) | `=COUNTIF('8. Jurisdictional Risk'!N5:N30,"High")+COUNTIF('8. Jurisdictional Risk'!N5:N30,"Critical")` | 0 | `=IF(B20>0,"⚠️ Review","✅ OK")` |

**TABLE 3: Regulatory Compliance Status (NEW - Rows 23-30)**

| Regulation | Metric | Value | Status |
|------------|--------|-------|--------|
| **DORA** | Exit Strategies Not PoC Tested (Annual) | `=COUNTIFS('7. Exit Strategy Review'!I5:I30,"<"&TODAY()-365,'7. Exit Strategy Review'!D5:D30,"Yes")` | `=IF(C24>0,"❌ Action","✅ OK")` |
| **DORA** | ICT Incidents Not Monitored | `=COUNTIF('4. Incident Management'!I5:I30,"❌ Non-Compliant")` | `=IF(C25>0,"❌ Action","✅ OK")` |
| **NIS2** | Significant Incidents (Require ≤24h notification) | `=COUNTIF('4. Incident Management'!G5:G30,"P1*")` | `=IF(C26>0,"⚠️ Review","✅ OK")` |
| **AI Act** | AI Systems Requiring Active Monitoring | `=COUNTIF('6. Vendor Risk Monitoring'!I5:I30,"<>N/A")` | Info |
| **CLOUD Act** | US-Nexus Providers (High/Critical Risk) | `=COUNTIF('8. Jurisdictional Risk'!N5:N30,"High")+COUNTIF('8. Jurisdictional Risk'!N5:N30,"Critical")` | `=IF(C28>0,"⚠️ Review","✅ OK")` |

### Overall Governance Health Score

**Row 33 (Weighted Score):**
```
OVERALL GOVERNANCE HEALTH SCORE: =ROUND(G10,0)%

Legend:
  ≥95%: ✅ Excellent
  80-94%: ⚠️ Good
  60-79%: ❌ Needs Improvement
  <60%: ❌ Critical - Immediate Action Required
```

---

# SECTION 4: SHEETS 10-11 + INTEGRATION

## Sheet 10: Evidence Register

### Purpose & Layout

**Sheet Name:** `10. Evidence Register`

**Purpose:** Centralized tracking of all governance evidence across all assessment sheets.

**Evidence ID Prefix:** `EV-GOV-###`

### Column Structure (A-M, 13 columns)

| Column | Field Name | Width | Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Evidence_ID | 15 | Formula | - | `=CONCATENATE("EV-GOV-",TEXT(ROW()-4,"000"))` |
| **B** | Source_Sheet | 22 | Dropdown | 2. Access Review, 3. Change Mgmt, 4. Incident Mgmt, 5. Business Continuity, 6. Vendor Risk, 7. Exit Strategy, 8. Jurisdictional Risk | Which sheet is this evidence for? |
| **C** | Source_Row | 12 | Integer | 5-30 | Row number in source sheet |
| **D** | Service_Name | 28 | Text | - | Cloud service name |
| **E** | Governance_Item | 30 | Text | - | What governance activity is being evidenced |
| **F** | Evidence_Type | 22 | Dropdown | Access Review Report, Change Ticket, Incident Report, BC Test Result, Vendor Assessment, Exit Plan Document, PoC Test Results, DPO Opinion | Type of evidence |
| **G** | File_Location | 45 | Text | - | Full path or URL to evidence file |
| **H** | File_Format | 16 | Dropdown | PDF, DOCX, XLSX, CSV, PNG/JPG, Email (MSG/EML), ITSM Ticket | File type |
| **I** | Collection_Date | 16 | Date | - | When evidence collected |
| **J** | Collected_By | 20 | Text | - | Who collected evidence |
| **K** | Retention_Until | 16 | Date | Formula: `=I5+2555` | 7 years retention |
| **L** | Verification_Status | 20 | Dropdown | Verified, Pending, Invalid, Missing | Evidence quality status |
| **M** | Notes | 35 | Text | - | Additional context |

### Conditional Formatting

**Verification Status (Column L):**

- "Verified" → Green fill (C6EFCE)
- "Pending" → Yellow fill (FFEB9C)
- "Invalid" → Orange fill (FFC7CE)
- "Missing" → Red fill (FF0000), white text

### Data Rows

**Rows:** 5-124 (120 evidence entries capacity)

---

## Sheet 11: Approval Sign-Off

### Purpose & Layout

**Sheet Name:** `11. Approval Sign-Of`  *(Note: typo in sheet name matches Python generator)*

**Purpose:** 5-stage sequential approval workflow.

**Approval Stages:**
1. IT Operations Review (technical accuracy)
2. Compliance Officer Review (governance adequacy)
3. Data Protection Officer (DPO) Review
4. Chief Risk Officer (CRO) Review
5. CISO Approval (final authorization)

### Approval Workflow Structure

**Assessment Summary (Rows 4-12):**

- Document ID: ISMS-IMP-A.5.23.S4
- Assessment Period: [Input]
- Overall Compliance Rate: `='9. Summary Dashboard'!G10`
- Services Assessed: `='9. Summary Dashboard'!B13`
- Services Requiring Remediation: `='9. Summary Dashboard'!B14`
- Overdue Access Reviews: `='9. Summary Dashboard'!B15`
- Jurisdictional Risks Identified: `='9. Summary Dashboard'!B20`
- Exit Strategies Not Tested: `='9. Summary Dashboard'!B19` (NEW v2.1)
- Assessment Status: [Dropdown: Draft, Ready for Review, In Approval, Approved, Requires Remediation]

**Approval Sections (Rows 14+):**

**1. IT OPERATIONS REVIEW (Rows 14-22)**

- Reviewed By (IT Ops Manager): [Input]
- Review Date: [Date]
- Technical Accuracy: [Dropdown: Verified, Issues Found, Incomplete]
- Governance Activities Completed: [Dropdown: Yes, Partially, No]
- Evidence Adequate: [Dropdown: Yes, Partially, No]
- IT Ops Comments: [Long text]
- IT Ops Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**2. COMPLIANCE OFFICER REVIEW (Rows 24-32)**

- Reviewed By (Compliance Officer): [Input]
- Review Date: [Date]
- Governance Framework Compliance: [Dropdown: Compliant, Partially, Non-Compliant]
- Policy Alignment: [Dropdown: Yes, Needs Update, Gaps Identified]
- Remediation Plans Adequate: [Dropdown: Yes, No, N/A]
- Compliance Comments: [Long text]
- Compliance Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**3. DPO REVIEW (Rows 34-42)**

- Reviewed By (DPO): [Input]
- Review Date: [Date]
- Data Protection Compliance: [Dropdown: Compliant, Partially Compliant, Non-Compliant]
- Cross-Border Transfer Status: [Dropdown: Approved, Approved with SCCs, Requires TIA, Rejected]
- Jurisdictional Risk Acceptable: [Dropdown: Yes, With Mitigations, No]
- DPO Comments: [Long text]
- DPO Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**4. CRO REVIEW (Rows 44-52)**

- Reviewed By (CRO): [Input]
- Review Date: [Date]
- Enterprise Risk Acceptance: [Dropdown: Approved, Conditionally Approved, Rejected]
- Regulatory Risk Status: [Dropdown: Acceptable, Requires Mitigation, Unacceptable]
- Vendor Concentration Risk: [Dropdown: Acceptable, Requires Diversification, Critical]
- CRO Comments: [Long text]
- CRO Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**5. CISO APPROVAL (Rows 54-62)**

- Reviewed By (CISO): [Input]
- Review Date: [Date]
- Overall Security Posture: [Dropdown: Strong, Acceptable, Needs Improvement, Unacceptable]
- Cloud Governance Adequate: [Dropdown: Yes, With Improvements, No]
- Risk Appetite Alignment: [Dropdown: Yes, Partially, No]
- CISO Comments: [Long text]
- **FINAL DECISION**: [Dropdown: **Approved, Approved with Conditions, Rejected - Remediation Required, Deferred**]

**Next Review Details (Rows 64-68):**

- Next Review Date: `=B57+90` (90 days after CISO approval)
- Next Review Type: [Dropdown: Quarterly, Annual, Triggered]
- Review Owner: [Input]
- Calendar Invite Sent: [Dropdown: Yes, No]

---

## Integration Points

### Integration with Other ISMS Assessments

**Imports FROM:**

| Source | Data Element | Usage |
|--------|--------------|-------|
| IMP-A.5.23.1 (Inventory) | Cloud service list (Column B) | Populate service names in Sheets 2-6 |
| IMP-A.5.23.1 (Inventory) | Service criticality (Column F) | Determine governance frequency (Critical = quarterly, Low = annual) |
| IMP-A.5.23.2 (Vendor DD) | Vendor certifications | Inform vendor risk monitoring (Sheet 6) |
| IMP-A.5.23.3 (Secure Config) | Access control baseline | Reference for access reviews (Sheet 2) |

**Exports TO:**

| Target | Data Element | Usage |
|--------|--------------|-------|
| IMP-A.5.23.5 (Compliance) | Overall compliance % (Dashboard) | Executive compliance reporting |
| IMP-A.5.23.5 (Compliance) | Incident counts (Sheet 4) | Security incident trends |
| IMP-A.5.23.5 (Compliance) | High-risk vendors (Sheet 6) | Risk heatmap generation |
| IMP-A.5.23.5 (Compliance) | Exit strategy readiness (Sheet 7) | Exit planning dashboard |

### Integration with Organizational Systems

**CMDB (Configuration Management Database):**

- Export: Cloud service governance status → CMDB compliance field
- Import: Service owner changes → Update Sheet 2 responsible teams

**ITSM (IT Service Management):**

- Export: Non-compliant items → Auto-create ITSM remediation tickets
- Import: Change ticket IDs → Populate Sheet 3 change references
- Import: Incident ticket IDs → Populate Sheet 4 incident references

**Risk Management System:**

- Export: Vendor risk ratings (Sheet 6) → Enterprise risk register
- Export: Jurisdictional risks (Sheet 8) → Operational risk register
- Import: Risk IDs → Column N (Risk_ID) across all sheets

**IAM (Identity & Access Management):**

- Import: Access review reports → Evidence for Sheet 2
- Import: Admin account counts → Sheet 2 Column S

**Vendor Management Portal:**

- Import: Vendor cert expiry dates → Sheet 6 Column U
- Import: Vendor security incidents → Sheet 6 Column S
- Export: Vendor risk ratings → Vendor portal dashboards

---

## Quality Assurance Procedures

### Pre-Distribution QA Checklist

```
☐ Generator Script Validation
  ├─ Run generate_reg_a523_4_governance.py
  ├─ Verify 11 sheets created (correct names)
  ├─ Check all formulas calculate correctly (no #REF! errors)
  └─ Validate dropdown lists populated

☐ Data Validation Testing
  ├─ Test Status dropdown (✅ ⚠️ ❌ N/A) on each sheet
  ├─ Test sheet-specific dropdowns (Column G variations)
  ├─ Test date validations (no future dates allowed)
  └─ Test integer validations (no negative numbers)

☐ Formula Validation
  ├─ Sheet 2 Column X (Next_Review_Due = Last_Review + 90 days)
  ├─ Sheet 5 Column X (Next_Test_Due = Last_Test + 365 days)
  ├─ Sheet 7 Column F (Next_Review_Due = Last_Review + 365 days)
  ├─ Sheet 7 Column N (Next_PoC_Test = Last_PoC + 365 days)
  ├─ Sheet 8 Column R (Next_Review = Risk_Acceptance + 90 days)
  ├─ Sheet 9: ALL dashboard formulas (compliance %, metrics)
  └─ Sheet 10 Column K (Retention_Until = Collection + 2555 days)

☐ Dashboard Formula Testing
  ├─ Manually enter test data in Sheet 2
  ├─ Verify Dashboard Table 1 updates correctly
  ├─ Verify Dashboard Table 2 metrics calculate
  ├─ Verify Dashboard Table 3 regulatory metrics
  └─ Test with 0 entries (should show "N/A" not errors)

☐ Integration Testing
  ├─ Export sample data from IMP-5.23.1
  ├─ Import into IMP-5.23.4 Sheets 2-6 Column B
  ├─ Verify Dashboard consolidates data correctly
  ├─ Test CMDB/ITSM integration scripts (if automated)
  └─ Validate evidence register linkages

☐ Accessibility & Usability
  ├─ Column widths appropriate (no truncated headers)
  ├─ Row heights adequate (wrapped text visible)
  ├─ Print settings: Landscape, A4, fit-to-width
  ├─ Freeze panes: Row 5 frozen on assessment sheets
  ├─ Instructions sheet comprehensive and clear
  └─ Legend/help text accurate
```

### Post-Completion QA

**Before approval submission:**
```
☐ Completeness Check
  ├─ All 11 sheets populated (no empty sheets)
  ├─ All yellow input cells filled (no "[INPUT]" placeholders)
  ├─ All dropdowns selected (no empty validation cells)
  ├─ Evidence locations provided (Column J on all sheets)
  └─ Evidence register populated (Sheet 10)

☐ Accuracy Verification
  ├─ Spot-check 20% of "Compliant" entries (verify evidence)
  ├─ Verify Status-Evidence alignment (Compliant = evidence exists)
  ├─ Check remediation dates realistic (Column Q)
  ├─ Validate cross-sheet consistency (service names match)
  └─ Review Dashboard metrics (do they make sense?)

☐ Regulatory Compliance
  ├─ If DORA: Sheet 7 complete (exit strategy + PoC)
  ├─ If NIS2: Sheet 4 incidents classified correctly
  ├─ If AI Act: Sheet 6 AI monitoring documented
  ├─ If US vendors: Sheet 8 jurisdictional risk assessed
  └─ DPO/CRO approval sections complete (if applicable)

☐ Approval Readiness
  ├─ Self-assessment score ≥80/100 (Part I Section 7)
  ├─ All gaps documented with remediation plans
  ├─ Critical findings escalated to CISO
  ├─ Stakeholders pre-briefed (no surprises)
  └─ README.md created (for auditors)
```

---

## Workbook-Level Specifications

**File Naming Convention:**
```
ISMS-IMP-A.5.23.S4_Governance_YYYYMMDD.xlsx

Example: ISMS-IMP-A.5.23.S4_Governance_20260120.xlsx
```

**Metadata Properties (via `openpyxl.workbook.properties`):**
```python
wb.properties.title = "ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management"
wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.23 Governance Assessment"
wb.properties.creator = "[Organization] ISMS Team"
wb.properties.description = "Quarterly governance assessment for cloud services (v2.1 with DORA exit strategy)"
wb.properties.keywords = "ISMS, ISO27001, A.5.23, Cloud, Governance, Risk, DORA, NIS2, CLOUD Act"
wb.properties.category = "Information Security Management"
wb.properties.version = "2.1"
```

**Sheet Protection:**

- **Protected Sheets:** 2-8 (assessment sheets), 9 (dashboard), 10 (evidence register)
- **Locked Cells:** Column A (Assessment_ID formulas), Dashboard formulas
- **Unlocked Cells:** All yellow input cells, Column J (Evidence_Location)
- **Allow:** Select unlocked cells, Select locked cells, Format cells

**Print Settings (All Assessment Sheets):**

- Page orientation: Landscape
- Paper size: A4
- Scaling: Fit to 1 page wide × auto tall
- Repeat rows: 1:4 (headers)
- Print gridlines: Yes
- Print quality: High

**Freeze Panes:**

- **Assessment Sheets (2-8):** Row 5 frozen (headers rows 1-4 visible when scrolling)
- **Dashboard (9):** Row 4 frozen (table headers visible)
- **Evidence Register (10):** Row 5 frozen
- **Approval (11):** No freeze

**Expected File Size:**

- Empty workbook: ~200-250 KB
- Fully populated: ~1.5-2.5 MB (depends on evidence volume)
- With images: Up to 10 MB (if screenshots embedded)

---

**END OF SPECIFICATION**

---

*"Nature uses only the longest threads to weave her patterns, so that each small piece of her fabric reveals the organization of the entire tapestry."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
