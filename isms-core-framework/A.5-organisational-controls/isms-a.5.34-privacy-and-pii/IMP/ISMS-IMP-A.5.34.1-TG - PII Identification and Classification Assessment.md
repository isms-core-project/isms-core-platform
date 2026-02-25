<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.1-TG:framework:TG:a.5.34.1 -->
**ISMS-IMP-A.5.34.1-TG - PII Identification and Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | PII Identification, Classification, Data Flow Mapping, and ROPA Maintenance |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.1 (PII Classification and Identification) |
| **Purpose** | Guide users through systematic PII discovery, classification, data mapping, and GDPR Article 30 compliant Record of Processing Activities (ROPA) maintenance |
| **Target Audience** | DPO/Privacy Officers, Data Owners, System Owners, IT Teams, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major System Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for PII Identification assessment workbook | ISMS Implementation Team |

---


---
# Technical Specification
**Audience:** Workbook developers (Python/Excel script maintainers), Technical implementation teams


> Auto-generated from `generate_a5341_pii_identification_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.34.1` |
| **Output Filename** | `ISMS-IMP-A.5.34.1_PII_Identification_and_Classification_YYYYMMDD.xlsx` |
| **Workbook Title** | PII Identification and Classification |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | COLOR_HEADER | Dark Blue (Headers) |
| #006400 | COLOR_VALIDATED | Custom |
| #87CEEB | COLOR_LOW | Custom |
| #8B0000 | COLOR_CRITICAL | Dark Red (Critical) |
| #90EE90 | COLOR_COMPLETE | Custom |
| #D3D3D3 | COLOR_NOT_STARTED | Custom |
| #FFA500 | COLOR_HIGH | Orange (High Priority) |
| #FFFF00 | COLOR_IN_PROGRESS | Yellow (Warning) |

## Sheet 1: 1. Instructions & Legend

---

## Sheet 2: 2. PII System Inventory

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | RowID |
| B | Status |
| C | System Name |
| D | System Owner |
| E | System Type |
| F | PII Processing Role |
| G | PII Data Subjects |
| H | PII Categories |
| I | PII Classification |
| J | Sensitive PII Types (if applicable) |
| K | Data Volume (approx. records) |
| L | Hosting Location |
| M | Access Level (who/how many) |
| N | Discovery Method |
| O | Discovery Date |
| P | Last Updated |
| Q | Updated By |
| R | Notes |
| S | Evidence Reference |
| T | Review Comments |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| I2:I1000 | containsText  |  |
| I2:I1000 | containsText  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |
| O2 | `=TODAY()` |  |

---

## Sheet 3: 3. PII Data Flow Mapping

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | RowID |
| B | Status |
| C | Source System |
| D | Destination System |
| E | PII Categories Transferred |
| F | Transfer Method |
| G | Transfer Frequency |
| H | Purpose of Transfer |
| I | Legal Basis (Art. 6) |
| J | Recipient Type |
| K | Recipient Name (if external) |
| L | Cross-Border Transfer? |
| M | Destination Country |
| N | Transfer Mechanism |
| O | SCC Date (if applicable) |
| P | TIA Completed? (if cross-border) |
| Q | Security Measures |
| R | Last Updated |
| S | Updated By |
| T | Notes |
| U | Evidence Reference |
| V | Review Comments |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |
| R2 | `=TODAY()` |  |

---

## Sheet 4: 4. ROPA (Record of Processing)

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | RowID |
| B | Status |
| C | Processing Activity Name |
| D | Purpose of Processing |
| E | Legal Basis (Art. 6) |
| F | Legal Basis (Art. 9 if special category) |
| G | Legal Basis Justification |
| H | Categories of Data Subjects |
| I | Categories of Personal Data |
| J | Contains Special Category Data? |
| K | Specific Special Category Types |
| L | Categories of Recipients (Internal) |
| M | Categories of Recipients (Processors) |
| N | Categories of Recipients (Third Parties) |
| O | Categories of Recipients (Public Authorities) |
| P | Transfers to Third Countries? |
| Q | Third Countries |
| R | Transfer Safeguards |
| S | Retention Period |
| T | Retention Justification |
| U | Deletion Method |
| V | Technical Security Measures |
| W | Organizational Security Measures |
| X | Data Sources |
| Y | Data Subject Rights Supported |
| Z | DPIA Completed? |
| AA | DPIA Reference |
| AB | LIA Completed? (if Leg. Interest) |
| AC | LIA Reference |
| AD | Last Updated |
| AE | Updated By |
| AF | Notes |
| AG | Evidence Reference |
| AH | Review Comments |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |
| AD2 | `=TODAY()` |  |

---

## Sheet 5: 5. PII Discovery Gaps

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | GapID |
| B | Status |
| C | Gap Type |
| D | Gap Description |
| E | System/Activity Affected |
| F | Risk Level |
| G | Risk Justification |
| H | Remediation Action |
| I | Remediation Owner |
| J | Target Completion Date |
| K | Actual Completion Date |
| L | Date Identified |
| M | Identified By |
| N | Last Updated |
| O | Updated By |
| P | Notes |
| Q | Evidence Reference |
| R | Review Comments |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| B2:B1000 | equal  |  |
| B2:B1000 | equal  |  |
| B2:B1000 | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(YEAR(TODAY()),` |  |
| L2 | `=TODAY()` |  |

---

## Sheet 6: 6. Evidence Register

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | EvidenceID |
| B | Evidence Type |
| C | Evidence Description |
| D | Related System/Activity |
| E | Related Sheet Reference |
| F | Date Collected |
| G | Collected By |
| H | File Location/URL |
| I | File Name |
| J | Retention Period |
| K | Confidentiality Level |
| L | Last Updated |
| M | Updated By |
| N | Notes |
| O | Review Comments |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| K2:K1000 | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| F2 | `=TODAY()` |  |

---

## Sheet 7: 7. Dashboard

**Data Rows:** 999 (rows 2–1000)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Systems Assessed: |
| — | `=COUNTIF(` | Systems with Basic PII: |
| — | `=SUMPRODUCT((` | Flows Missing Transfer Mechanism: |
| — | `=IFERROR(TEXT(COUNTIF(` | Assessment Completion Rate: |

---

## Sheet 8: 8. Approval & Sign-Off

**Data Rows:** 997 (rows 4–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Signatory Role |
| B | Signatory Name |
| C | Signature / Electronic Approval |
| D | Signature Date |
| E | Approval Scope |
| F | Comments |
| G | Contact Email |

---

## Sheet 9: Header_Row

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `DISCOVERY_METHODS` | Automated Scan (DLP), Manual Survey, Interview (System Owner), Documentation Review, Database Sch... |
| `EVIDENCE_TYPES` | System Documentation, Interview Notes, DLP Scan Results, Contract (Processor Agreement, SCCs), Co... |
| `GAP_TYPES` | Unknown System (Not in inventory), Undocumented Data Flow, Missing Legal Basis, Unclear Retention... |
| `LEGAL_BASIS_ART6` | Consent (Art. 6(1)(a)), Contract (Art. 6(1)(b)), Legal Obligation (Art. 6(1)(c)), Vital Interests... |
| `LEGAL_BASIS_ART9` | N/A (No special category data), Explicit Consent (Art. 9(2)(a)), Employment / Social Security (Ar... |
| `PII_CLASSIFICATIONS` | Basic PII, Sensitive PII (GDPR Art. 9 / FADP Art. 5(c)), Criminal Offense Data (GDPR Art. 10 / FA... |
| `PII_DATA_SUBJECTS` | Customers, Employees, Contractors, Vendors/Suppliers, Job Applicants, Website Visitors, Other |
| `RECIPIENT_TYPES` | Internal (within organization), Processor (processes on our behalf per Art. 28), Third Party (sep... |
| `RISK_LEVELS` | Critical, High, Medium, Low |
| `SENSITIVE_PII_TYPES` | Health Data, Genetic Data, Biometric Data (for unique identification), Racial or Ethnic Origin, P... |
| `SIGNATORY_ROLES` | Assessment Lead (DPO / Privacy Officer), Chief Information Security Officer (CISO), Legal / Compl... |
| `STATUS_OPTIONS` | Not Started, In Progress, Complete, Validated |
| `SYSTEM_TYPES` | Customer Relationship Management (CRM), Human Resources Information System (HRIS), Payroll System... |
| `TRANSFER_MECHANISMS` | No cross-border transfer, Adequacy Decision (EU/CH recognizes country), Standard Contractual Clau... |

---

**END OF SPECIFICATION**

---

*"Privacy is not something that I'm merely entitled to, it's an absolute prerequisite."*
— Marlon Brando

<!-- QA_VERIFIED: 2026-02-06 -->
