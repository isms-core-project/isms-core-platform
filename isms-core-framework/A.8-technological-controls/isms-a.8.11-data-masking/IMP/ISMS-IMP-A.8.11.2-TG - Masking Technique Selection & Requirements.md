<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.11.2-TG:framework:TG:a.8.11.2 -->
**ISMS-IMP-A.8.11.2-TG - Masking Technique Selection & Requirements**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Masking Technique Selection & Requirements |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.11.2-TG |
| **Related Policy** | ISMS-POL-A.8.11 (Data Masking) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.11 (Data Masking) |
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

- ISMS-POL-A.8.11 (Data Masking)
- ISMS-IMP-A.8.11.1 (Data Inventory & Classification Assessment)
- ISMS-IMP-A.8.11.3 (Environment Coverage Assessment)
- ISMS-IMP-A.8.11.4 (Testing & Validation Framework)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a811_2_masking_techniques.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.11.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Approved Techniques |
| 3 | Technique Selection Matrix |
| 4 | Static Masking SDM |
| 5 | Dynamic Masking DDM |
| 6 | Tokenisation Implementation |
| 7 | Encryption for Masking |
| 8 | Masking Tool Inventory |
| 9 | Configuration Standards |
| 10 | Gap Analysis |
| 11 | Evidence Register |
| 12 | Summary Dashboard |
| 13 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Technique ID |
| 2 | Technique Name |
| 3 | Description |
| 4 | Reversible? |
| 5 | Format-Preserving? |
| 6 | Primary Use Cases |
| 7 | Approved for Use? |
| 8 | Policy Reference |
| 9 | Implementation Status |
| 10 | Data Category |
| 11 | Data Type Example |
| 12 | Sensitivity Level |
| 13 | Primary Technique |
| 14 | Secondary Technique |
| 15 | Format Must Preserve? |
| 16 | Reversibility Required? |
| 17 | Environment(s) |
| 18 | Selection Rationale |
| 19 | Regulatory Driver |
| 20 | Notes |
| 21 | System/Database |
| 22 | Technique/Method |
| 23 | Configuration |
| 24 | Automated? |
| 25 | Frequency/Trigger |
| 26 | Last Update |
| 27 | Format Preserved? |
| 28 | Validated? |
| 29 | Performance Impact |
| 30 | Status |
| 31 | Evidence Ref |
| 32 | Responsible |
| 33 | Gap ID |
| 34 | Gap Category |
| 35 | Affected System |
| 36 | Gap Description |
| 37 | Risk Level |
| 38 | Impact |
| 39 | Root Cause |
| 40 | Remediation Action |
| 41 | Owner |
| 42 | Target Date |
| 43 | Completion Date |
| 44 | Verification |
| 45 | =SUM(B6:B11) |
| 46 | =SUM(C6:C11) |
| 47 | =SUM(D6:D11) |
| 48 | =SUM(E6:E11) |
| 49 | =SUM(F6:F11) |
| 50 | APPROVED MASKING TECHNIQUES |
| 51 | TECHNIQUE SELECTION MATRIX |
| 52 | MASKING TECHNIQUE IMPLEMENTATION GAP ANALYSIS |
| 53 | Evidence ID |
| 54 | Category |
| 55 | Source/Location |
| 56 | Date Collected |
| 57 | Collected By |
| 58 | Assessment Area |
| 59 | Total Items |
| 60 | Compliant |
| 61 | Partial |
| 62 | Non-Compliant |
| 63 | N/A |
| 64 | Compliance % |
| 65 | Finding |
| 66 | Recommendation |
| 67 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Planned, N/A, \u2705 Implemented, \u26A0\uFE0F Partial
\u274C Not Implemented, TECH-SDM, TECH-DDM, TECH-RED, TECH-TOK, TECH-SUB
TECH-ENC, TECH-SHF, TECH-HSH, Critical, High, Medium, Low, Development
Test/QA, UAT, Training, Analytics, Production, Substitution, Redaction
Shuffling, Hashing, Tokenisation, Encryption, Other, On-Demand, Weekly
Monthly, Quarterly, Open, In Progress, Complete, Accepted Risk
Configuration file, Screenshot, Masking rule export, Documentation
Vendor spec, Test results, Audit log, Compliance report, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 13 sheets, 67 columns, 61 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Insanity is doing the same thing over and over and expecting different results."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
