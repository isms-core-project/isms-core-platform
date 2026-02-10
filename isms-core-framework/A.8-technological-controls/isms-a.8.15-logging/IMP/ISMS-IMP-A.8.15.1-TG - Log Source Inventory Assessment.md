<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.1-TG:framework:TG:a.8.15.1 -->
**ISMS-IMP-A.8.15.1-TG - Log Source Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Log Source Inventory & Event Logging Completeness |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.1 (Event Logging Requirements) |
| **Purpose** | Catalog all systems generating logs, verify logging completeness against policy requirements, and identify gaps in event logging coverage |
| **Target Audience** | IT Operations, System Owners, Application Owners, Security Team, Compliance Officers, Auditors, Workbook Developers (Python/Excel script maintainers) |
| **Assessment Type** | Inventory & Compliance Verification |
| **Review Cycle** | Annual (full inventory), Quarterly (new systems update) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification for Log Source Inventory assessment workbook | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook Developers (Python/Excel Script Maintainers)


> Auto-generated from `generate_a815_1_log_source_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.15.1` |
| **Output Filename** | `ISMS-IMP-A.8.15.1_Log_Source_Inventory_YYYYMMDD.xlsx` |
| **Total Sheets** | 27 (27 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.15: Logging |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | end_color | Light Gray (Example Rows) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: System Inventory

---

## Sheet 3: Log Event Types by System

---

## Sheet 4: Authentication Logging

---

## Sheet 5: Authorization & Access

---

## Sheet 6: Administrative Activity

---

## Sheet 7: Security Event Logging

---

## Sheet 8: Application & Database

---

## Sheet 9: Network Device Logging

---

## Sheet 10: Gap Analysis

---

## Sheet 11: Evidence Register

---

## Sheet 12: Summary Dashboard

---

## Sheet 13: Approval & Sign-Off

---

## Sheet 14: Instructions

**Purpose:** "If you can't explain it simply, you don't understand it well enough"

**Frozen Panes:** A3

---

## Sheet 15: System_Inventory

**Purpose:** "You can't improve what you don't measure, and you can't measure

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | System ID | 15 |
| B | System Name | 30 |
| C | System Type | 20 |
| D | Operating System / Platform | 25 |
| E | Environment | 15 |
| F | Data Classification | 18 |
| G | Business Criticality | 18 |
| H | Regulatory Scope | 20 |
| I | Logging Priority | 15 |
| J | System Owner | 25 |
| K | Owner Email | 30 |
| L | Hostname / FQDN | 30 |
| M | Primary IP | 15 |
| N | Location | 20 |
| O | Logging Enabled | 15 |
| P | Forwarding to SIEM | 18 |
| Q | Compliance Status | 18 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |
| QN | `=IF(B{data_row}=` |  |

---

## Sheet 16: Log_Event_Types

**Purpose:** "The devil is in the details, but so is salvation." - Hyman Rickover

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** C8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | System ID | 15 |
| B | System Name | 30 |
| C | Authentication Events | 15 |
| D | Authorization Events | 15 |
| E | Administrative Actions | 15 |
| F | Security Events | 15 |
| G | Application Events | 15 |
| H | System Events | 15 |
| I | Network Events | 15 |
| J | Database Events | 15 |
| K | Log Format | 15 |
| L | Timestamp Format | 18 |
| M | Timezone | 15 |
| N | Est. Daily Volume (MB) | 20 |
| O | Retention Period (months) | 20 |
| P | Storage Tier | 15 |
| Q | Protection Mechanisms | 20 |
| R | Event Types Completeness | 20 |
| S | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C9:J100 | `yes_no_dv` |
| K | K9:K100 | `log_format_dv` |
| L | L9:L100 | `timestamp_format_dv` |
| M | M9:M100 | `timezone_dv` |
| P | P9:P100 | `storage_tier_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=IF(A{data_row}=` |  |

---

## Sheet 17: Authentication_Logging

**Purpose:** Per ISMS-POL-A.8.15-S2.1.2 - Authentication events.

---

## Sheet 18: Authorization_Logging

**Purpose:** Per ISMS-POL-A.8.15-S2.1.3 - Authorization and access control events.

---

## Sheet 19: Administrative_Activity

**Purpose:** Per ISMS-POL-A.8.15-S2.1.4 - Administrative actions.

---

## Sheet 20: Security_Event_Logging

**Purpose:** Per ISMS-POL-A.8.15-S2.1.5 - Security tool and event logging.

---

## Sheet 21: Application_Database_Logging

**Purpose:** Per ISMS-POL-A.8.15-S2.1.7 - Application and database events.

---

## Sheet 22: Network_Device_Logging

**Purpose:** Per ISMS-POL-A.8.15-S2.1.8 - Network infrastructure logging.

---

## Sheet 23: Gap_Analysis

**Purpose:** "The gap between where you are and where you want to be is called a plan."

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | System ID | 15 |
| C | System Name | 30 |
| D | Gap Category | 25 |
| E | Gap Description | 50 |
| F | Policy Requirement | 30 |
| G | Impact / Risk | 20 |
| H | Remediation Action | 50 |
| I | Responsible Party | 25 |
| J | Target Date | 15 |
| K | Status | 15 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D9:D100 | `gap_category_dv` |
| G | G9:G100 | `risk_dv` |
| K | K9:K100 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |
| CN | `=IF(B{data_row}=` |  |

---

## Sheet 24: Evidence_Register

**Purpose:** "In God we trust. All others must bring data." - W. Edwards Deming

**Data Rows:** 100 (rows 9–108) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Type | 25 |
| C | Description | 40 |
| D | Related System(s) | 30 |
| E | Related Policy Req | 25 |
| F | File Name / Location | 40 |
| G | Collected By | 25 |
| H | Collection Date | 15 |
| I | Retention Period | 20 |
| J | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B108 | `evidence_type_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 25: Summary_Dashboard

**Purpose:** "What gets measured gets managed." - Peter Drucker

**Data Rows:** 92 (rows 9–100)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Systems Assessed |
| — | `=COUNTIF(` | Systems with Logging Enabled |
| — | `=COUNTIFS(` | Critical Systems Compliant (P1) |
| DN | `=IF(B{row}>={target[1:]},` |  |
| DN | `=IF(B{row}>0,` |  |
| CN | `=B{row}/COUNTA(\` |  |
| EN | `=IF(C{row}>={target[1:]},` |  |

---

## Sheet 26: Approval_Signoff

**Purpose:** "Trust, but verify. And get signatures." - Modified Russian proverb

---

## Sheet 27: Assessment

**Data Rows:** 92 (rows 9–100)

---

**END OF SPECIFICATION**

---

*"Once you stop learning, you start dying."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
