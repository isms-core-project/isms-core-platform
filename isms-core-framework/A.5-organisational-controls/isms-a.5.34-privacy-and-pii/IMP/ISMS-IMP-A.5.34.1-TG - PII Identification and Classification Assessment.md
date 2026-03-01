<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.1-TG:framework:TG:a.5.34.1 -->
**ISMS-IMP-A.5.34.1-TG - PII Identification and Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | PII Identification and Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.34.1-TG |
| **Related Policy** | ISMS-POL-A.5.34 (Privacy and Pii) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.34 (Privacy and Protection of PII) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.5.34 (Privacy and Pii)
- ISMS-IMP-A.5.34.2 (Legal Basis and Lawful Processing Assessment)
- ISMS-IMP-A.5.34.3 (Data Subject Rights Management Assessment)
- ISMS-IMP-A.5.34.4 (Technical and Organisational Measures (TOMs) Assessment)
- ISMS-IMP-A.5.34.5 (DPIA Assessment)
- ISMS-IMP-A.5.34.6 (Cross Border Transfer Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a5341_pii_identification_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.34.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | 2. PII System Inventory |
| 2 | 3. PII Data Flow Mapping |
| 3 | 4. ROPA (Record of Processing) |
| 4 | 5. PII Discovery Gaps |
| 5 | Evidence Register |
| 6 | Summary Dashboard |
| 7 | Approval Sign-Off |
| 8 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006400 | Custom |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #87CEEB | Custom |
| #8B0000 | Dark Red (Critical) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFA500 | Orange (High Priority) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | RowID |
| 2 | Status |
| 3 | System Name |
| 4 | System Owner |
| 5 | System Type |
| 6 | PII Processing Role |
| 7 | PII Data Subjects |
| 8 | PII Categories |
| 9 | PII Classification |
| 10 | Sensitive PII Types (if applicable) |
| 11 | Data Volume (approx. records) |
| 12 | Hosting Location |
| 13 | Access Level (who/how many) |
| 14 | Discovery Method |
| 15 | Discovery Date |
| 16 | Last Updated |
| 17 | Updated By |
| 18 | Notes |
| 19 | Evidence Reference |
| 20 | Review Comments |
| 21 | Source System |
| 22 | Destination System |
| 23 | PII Categories Transferred |
| 24 | Transfer Method |
| 25 | Transfer Frequency |
| 26 | Purpose of Transfer |
| 27 | Legal Basis (Art. 6) |
| 28 | Recipient Type |
| 29 | Recipient Name (if external) |
| 30 | Cross-Border Transfer? |
| 31 | Destination Country |
| 32 | Transfer Mechanism |
| 33 | SCC Date (if applicable) |
| 34 | TIA Completed? (if cross-border) |
| 35 | Security Measures |
| 36 | Processing Activity Name |
| 37 | Purpose of Processing |
| 38 | Legal Basis (Art. 9 if special category) |
| 39 | Legal Basis Justification |
| 40 | Categories of Data Subjects |
| 41 | Categories of Personal Data |
| 42 | Contains Special Category Data? |
| 43 | Specific Special Category Types |
| 44 | Categories of Recipients (Internal) |
| 45 | Categories of Recipients (Processors) |
| 46 | Categories of Recipients (Third Parties) |
| 47 | Categories of Recipients (Public Authorities) |
| 48 | Transfers to Third Countries? |
| 49 | Third Countries |
| 50 | Transfer Safeguards |
| 51 | Retention Period |
| 52 | Retention Justification |
| 53 | Deletion Method |
| 54 | Technical Security Measures |
| 55 | Organisational Security Measures |
| 56 | Data Sources |
| 57 | Data Subject Rights Supported |
| 58 | DPIA Completed? |
| 59 | DPIA Reference |
| 60 | LIA Completed? (if Leg. Interest) |
| 61 | LIA Reference |
| 62 | GapID |
| 63 | Gap Type |
| 64 | Gap Description |
| 65 | System/Activity Affected |
| 66 | Risk Level |
| 67 | Risk Justification |
| 68 | Remediation Action |
| 69 | Remediation Owner |
| 70 | Target Completion Date |
| 71 | Actual Completion Date |
| 72 | Date Identified |
| 73 | Identified By |
| 74 | Assessment Area |
| 75 | Total Items |
| 76 | Compliant |
| 77 | Partial |
| 78 | Non-Compliant |
| 79 | N/A |
| 80 | Compliance % |
| 81 | Metric |
| 82 | Value |
| 83 | Category |
| 84 | Finding |
| 85 | Count |
| 86 | Severity |
| 87 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Active, Archived, Superseded, Pending Review, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 8 sheets, 87 columns, 12 validation values, 14 colors

---

**END OF SPECIFICATION**


---

*"Privacy is not something that I'm merely entitled to, it's an absolute prerequisite."*
— Marlon Brando

<!-- QA_VERIFIED: 2026-02-06 -->
