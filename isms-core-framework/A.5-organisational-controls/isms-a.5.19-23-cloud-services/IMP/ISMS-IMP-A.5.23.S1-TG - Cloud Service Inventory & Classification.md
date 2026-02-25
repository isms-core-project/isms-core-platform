<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.23.S1-TG:framework:TG:a.5.23 -->
**ISMS-IMP-A.5.23.S1-TG - Cloud Service Inventory & Classification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Cloud Service Inventory & Classification |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 (Cloud Services Security) |
| **Purpose** | Maintain authoritative inventory of all cloud services with data classification, criticality assessment, regulatory mapping, and exit feasibility analysis |
| **Target Audience** | IT Operations, Procurement, Finance, Security Teams, Compliance Officers, Auditors |
| **Assessment Type** | Inventory & Classification |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |

---


> Auto-generated from `generate_reg_a523_1_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.23.S1` |
| **Output Filename** | `ISMS-IMP-A.5.23.S1_Cloud_Service_Inventory_&_Classification_YYYYMMDD.xlsx` |
| **Workbook Title** | Cloud Service Inventory & Classification |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | end_color | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: 2. SaaS Services

---

## Sheet 3: 3. IaaS PaaS Services

---

## Sheet 4: 4. Cloud Security Services

---

## Sheet 5: 5. Cloud Storage Services

---

## Sheet 6: 6. Data Classification

---

## Sheet 7: 7. Service Criticality

---

## Sheet 8: 8. Summary Dashboard

---

## Sheet 9: 9. Evidence Register

---

## Sheet 10: 10. Approval Sign-Of

---

## Sheet 11: Instructions

---

## Sheet 12: Assessment

**Frozen Panes:** A7

### Columns

| Col | Header |
|-----|--------|
| A | Item |
| B | Requirement |
| C | Status |
| D | Evidence |

---

## Sheet 13: Exit_Strategy

**Purpose:** Implements POL-A.5.19-23-S5 Section 8.1.1 (Exit Strategy Framework)

**Data Rows:** 97 (rows 4–100) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Service Name | 25 |
| B | Provider | 20 |
| C | Service Type | 18 |
| D | Environment | 15 |
| E | Business Owner | 20 |
| F | Technical Owner | 20 |
| G | Data Classification | 18 |
| H | Criticality | 15 |
| I | Users | 12 |
| J | Cost (Annual CHF) | 18 |
| K | Contract End Date | 15 |
| L | Primary Region | 18 |
| M | Backup Region | 18 |
| N | Integration Count | 15 |
| O | API Dependency | 15 |
| P | Compliance Certs | 20 |
| Q | Current Status | 15 |
| R | Exit Strategy Type | 20 |
| S | Alternative Identified | 22 |
| T | Export Format Available | 22 |
| U | Export Tested | 16 |
| V | Data Volume (GB) | 16 |
| W | Migration Complexity | 24 |
| X | Lock-In Risk | 16 |
| Y | Hybrid: Workload Segmentation | 28 |
| Z | Hybrid: Data Sync Latency | 28 |
| AA | OnPrem: TCO Analysis Complete | 28 |
| AB | OnPrem: Infrastructure Available | 30 |
| AC | OnPrem: Staffing Plan Documented | 30 |

---

## Sheet 14: Data_Classification

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Data_ID | 12 |
| B | Data Category | 25 |
| C | Description | 35 |
| D | Classification Level | 18 |
| E | Primary Cloud Service | 22 |
| F | Storage Location | 22 |
| G | Data Owner | 18 |
| H | Retention Period | 16 |
| I | Personal Data (GDPR) | 18 |
| J | Cross-Border Transfer | 18 |

---

## Sheet 15: Service_Criticality

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Service_ID | 12 |
| B | Cloud Service Name | 28 |
| C | Service Category | 18 |
| D | Business Process Supported | 28 |
| E | Criticality Level | 16 |
| F | RTO (Hours) | 14 |
| G | RPO (Hours) | 14 |
| H | MTPD (Hours) | 14 |
| I | Single Point of Failure | 18 |
| J | Workaround Available | 18 |
| K | DORA Scope | 14 |
| L | Exit Priority | 14 |

---

## Sheet 16: Summary_Dashboard

**Data Rows:** 43 (rows 8–50)

### Columns

| Col | Header |
|-----|--------|
| A | Category |
| B | Total |
| C | {...} Compliant |
| D | {...} Partial |
| E | {...} Non-Compliant |
| F | N/A |
| G | Compliance % |

---

## Sheet 17: Evidence_Register

**Data Rows:** 100 (rows 4–103)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 15 |
| B | Cloud_Service | 30 |
| C | Evidence_Type | 25 |
| D | Description | 40 |
| E | File_Location | 40 |
| F | Collection_Date | 16 |
| G | Collected_By | 20 |
| H | Retention | 16 |
| I | Status | 15 |

---

## Sheet 18: Approval_Signoff

---

## Sheet 19: All_Validations

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `AI_RISK_CLASSIFICATION` | Not Applicable, Minimal Risk, Limited Risk (Transparency), High Risk, Unacceptable Risk (Prohibited) |
| `ALTERNATIVE_IDENTIFIED` | Cloud Provider (AWS), Cloud Provider (Azure), Cloud Provider (GCP), Cloud Provider (OVHcloud), Cl... |
| `CLOUD_ACT_EXPOSURE` | No Exposure, Potential Exposure (US HQ), Mitigated (EU Data Boundary), Mitigated (Encryption + Ke... |
| `CONCENTRATION_RISK_LEVEL` | Low (Multiple alternatives), Medium (Limited alternatives), High (Few alternatives), Critical (Si... |
| `EU_DATA_BOUNDARY_OPTIONS` | Yes, No, Partial, Unknown |
| `EXIT_STRATEGY_TYPE` | Cloud-to-Cloud, Hybrid, On-Premises, Not Yet Determined |
| `EXPORT_FORMAT` | Standard (CSV/JSON), Proprietary, API Only, None |
| `EXPORT_TESTED` | Yes, No, Partial |
| `HYBRID_DATA_SYNC_LATENCY` | Excellent (<100ms), Acceptable (100-500ms), Concern (>500ms), Not Tested, N/A |
| `HYBRID_WORKLOAD_SEGMENTATION` | Documented, In Progress, Not Applicable |
| `LOCK_IN_RISK` | Low, Medium, High, Critical |
| `MIGRATION_COMPLEXITY` | Cloud-to-Cloud (Low), Cloud-to-Cloud (Medium), Cloud-to-Cloud (High), Hybrid (Medium), Hybrid (Hi... |
| `ONPREM_INFRASTRUCTURE` | Yes (Sufficient), Partial (Upgrade Needed), No (Full Build), Not Assessed, N/A |
| `ONPREM_STAFFING_PLAN` | Yes, In Progress, Not Started, N/A |
| `ONPREM_TCO_ANALYSIS` | Yes (Favorable), Yes (Unfavorable), In Progress, Not Started, N/A |
| `PROVIDER_HQ_JURISDICTION` | Switzerland, EU/EEA, United Kingdom, United States, Other Adequate Country, Non-Adequate Country |
| `YES_NO_NOT_DETERMINED` | Yes, No, Not Determined |
| `YES_NO_PARTIAL` | Yes, No, Partial |

---

**END OF SPECIFICATION**

---

*"What I cannot create, I do not understand."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
