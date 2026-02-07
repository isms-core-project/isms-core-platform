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
| 1.0 | [Date] | Initial Excel workbook specification (Technical Specification) | ISMS Implementation Team |

---


> Auto-generated from `generate_reg_a523_4_governance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.23.S4` |
| **Output Filename** | `ISMS-IMP-A.5.23.S4_Ongoing_Governance_&_Risk_Management_YYYYMMDD.xlsx` |
| **Workbook Title** | Ongoing Governance & Risk Management |
| **Total Sheets** | 18 (18 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #0000FF | 0000FF | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #808080 | 808080 | Gray (Disabled) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Assessment_ID | 14 |
| B | Cloud_Service_Name | 25 |
| C | Provider_Name | 22 |
| D | Provider_HQ_Country | 18 |
| E | Provider_HQ_Jurisdiction | 20 |
| F | US_Parent_Company | 14 |
| G | CLOUD_Act_Applicability | 20 |
| H | Data_Processing_Locations | 25 |
| I | EU_Data_Boundary_Available | 18 |
| J | Customer_Managed_Keys | 16 |
| K | Legal_Challenge_Commitment | 18 |
| L | Adequacy_Decision_Status | 18 |
| M | Transfer_Mechanism | 16 |
| N | Risk_Level | 14 |
| O | Risk_Accepted_By | 18 |
| P | Risk_Acceptance_Date | 16 |
| Q | Compensating_Controls | 28 |
| R | Review_Date | 14 |
| S | Evidence_Reference | 20 |
| T | Notes | 30 |

---

## Sheet 2: 2. Access Review

---

## Sheet 3: 3. Change Management

---

## Sheet 4: 4. Incident Management

---

## Sheet 5: 5. Business Continuity

---

## Sheet 6: 6. Vendor Risk Monitoring

---

## Sheet 7: 7. Exit Strategy Review

---

## Sheet 8: 8. Jurisdictional Risk

---

## Sheet 9: 9. Summary Dashboard

---

## Sheet 10: 10. Evidence Register

---

## Sheet 11: 11. Approval Sign-Of

---

## Sheet 12: Instructions

---

## Sheet 13: 7_Exit_Strategy_Review

**Purpose:** - POL-A.5.19-23-S5 Section 8: Annual exit strategy review

**Data Rows:** 97 (rows 4–100) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Service Name | 25 |
| B | Provider | 20 |
| C | Criticality | 15 |
| D | Exit Strategy Type (Current) | 22 |
| E | Last Review Date | 15 |
| F | Next Review Date | 15 |
| G | Review Status | 15 |
| H | PoC Testing Required? | 20 |
| I | PoC Test Date (Last) | 16 |
| J | PoC Test Result | 18 |
| K | PoC Test Next Due | 16 |
| L | Exit Strategy Changed? | 20 |
| M | Reviewer Name | 20 |
| N | Notes | 40 |

---

## Sheet 14: 7_Jurisdictional_Risk

**Data Rows:** 25 (rows 6–30) | **Frozen Panes:** A6

---

## Sheet 15: Summary_Dashboard

**Data Rows:** 25 (rows 6–30)

### Columns

| Col | Header |
|-----|--------|
| A | Assessment Area |
| B | Total Items |
| C | Compliant |
| D | Partial |
| E | Non-Compliant |
| F | N/A |
| G | Compliance % |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(` | US-HQ Providers (CLOUD Act Scope) |
| — | `=COUNTIFS(` | CLOUD Act Mitigated |
| BN | `=G10` |  |
| BN | `=IF(G10=` |  |

---

## Sheet 16: Evidence_Register

**Data Rows:** 120 (rows 5–124) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Assessment Area | 25 |
| C | Cloud Service | 25 |
| D | Evidence Type | 28 |
| E | Description | 40 |
| F | Location/Path | 45 |
| G | Date Collected | 16 |
| H | Collected By | 20 |
| I | Verification Status | 20 |

---

## Sheet 17: Approval_Signoff

---

## Sheet 18: Assessment

**Purpose:** Generic engine to create any assessment sheet.

**Frozen Panes:** A6

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| CN | `=IF(COUNTA(C{checklist_data_start}:C{checklist_data_end})=0,` |  |

---

**END OF SPECIFICATION**

---

*"Nature uses only the longest threads to weave her patterns, so that each small piece of her fabric reveals the organization of the entire tapestry."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
