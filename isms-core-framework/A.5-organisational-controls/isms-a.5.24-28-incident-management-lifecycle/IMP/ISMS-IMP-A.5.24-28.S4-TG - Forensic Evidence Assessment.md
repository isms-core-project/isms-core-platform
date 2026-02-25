<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.24-28.S4-TG:framework:TG:a.5.24-28 -->
**ISMS-IMP-A.5.24-28.S4-TG - Forensic Evidence Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.28: Collection of Evidence

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Forensic Evidence Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S4-TG |
| **Assessment Domain** | Domain 4 - Forensic Evidence Management (A.5.28 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide, Section 3) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Digital Forensics Lead / Incident Response Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Digital Forensics Lead | Initial forensic evidence assessment specification |

**Review Cycle**: Annual (or after major forensic investigation)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**:
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide, Section 3: Forensic Collection Techniques Library)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISO/IEC 27002:2022 Control A.5.28
- NIST SP 800-86 (Guide to Integrating Forensic Techniques into Incident Response)
- ISO/IEC 27037:2012 (Guidelines for the Identification, Collection, Acquisition and Preservation of Digital Evidence)

---


> Auto-generated from `generate_a524_28_s4_forensic_evidence.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.24-28.S4` |
| **Output Filename** | `ISMS-IMP-A.5.24-28.S4_Forensic_Evidence_YYYYMMDD.xlsx` |
| **Total Sheets** | 20 (20 visible) |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #C8F0C8 | C8F0C8 | Custom |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFD9B3 | FFD9B3 | Custom |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Evidence Collection

---

## Sheet 3: Chain of Custody

---

## Sheet 4: Forensic Analysis

---

## Sheet 5: Storage & Retention

---

## Sheet 6: Legal & Regulatory

---

## Sheet 7: Gap Analysis

---

## Sheet 8: Evidence Register

---

## Sheet 9: Dashboard

---

## Sheet 10: Approval Sign-Off

---

## Sheet 11: Instructions

**Frozen Panes:** A3

---

## Sheet 12: Evidence_Collection

**Purpose:** Evidence Collection — 25 questions.

---

## Sheet 13: Chain_Of_Custody

**Purpose:** Chain of Custody — 20 questions.

---

## Sheet 14: Forensic_Analysis

**Purpose:** Forensic Analysis — 20 questions.

---

## Sheet 15: Storage_Retention

**Purpose:** Storage & Retention — 15 questions.

---

## Sheet 16: Legal_Regulatory

**Purpose:** Legal & Regulatory Readiness — 15 questions.

---

## Sheet 17: Gap_Analysis

**Purpose:** Gap Analysis — 40 capacity.

**Data Rows:** 40 (rows 6–45) | **Frozen Panes:** A7

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Domain |
| C | Gap_Description |
| D | Risk_Level |
| E | Current_State |
| F | Target_State |
| G | Remediation_Action |
| H | Owner |
| I | Target_Date |
| J | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| B4 | `=COUNTA(C6:C45)-COUNTBLANK(C6:C45)` |  |
| D4 | `=COUNTIF(E6:E45,` |  |

---

## Sheet 18: Evidence_Register

**Purpose:** Evidence Register — 60 capacity.

**Data Rows:** 7 (rows 2–8) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Evidence_Type |
| C | Description |
| D | Related_Question |
| E | Storage_Location |
| F | Date_Collected |
| G | Collected_By |
| H | Verification_Status |

---

## Sheet 19: Approval_Signoff

**Purpose:** Approval Sign-Off sheet.

**Frozen Panes:** A3

---

## Sheet 20: Assessment

**Data Rows:** 7 (rows 1–7)

### Columns

| Col | Header |
|-----|--------|
| A | Question_ID |
| B | Section |
| C | Question |
| D | Answer |
| E | Evidence_Ref |
| F | Comments |
| G | Gap_Flag |

---

**END OF SPECIFICATION**

---

*"I would rather have questions that can't be answered than answers that can't be questioned."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
