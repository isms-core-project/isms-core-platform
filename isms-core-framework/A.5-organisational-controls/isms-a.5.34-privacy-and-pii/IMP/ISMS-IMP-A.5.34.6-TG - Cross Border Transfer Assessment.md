<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.6-TG:framework:TG:a.5.34.6 -->
**ISMS-IMP-A.5.34.6-TG - Cross-Border Data Transfer Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Cross Border Transfer Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.34.6-TG |
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
- ISMS-IMP-A.5.34.1 (PII Identification and Classification Assessment)
- ISMS-IMP-A.5.34.2 (Legal Basis and Lawful Processing Assessment)
- ISMS-IMP-A.5.34.3 (Data Subject Rights Management Assessment)
- ISMS-IMP-A.5.34.4 (Technical and Organisational Measures (TOMs) Assessment)
- ISMS-IMP-A.5.34.5 (DPIA Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a5346_cross_border_transfer_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.34.6`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Transfer Register |
| 2 | TIA Register |
| 3 | Processor Tracker |
| 4 | Evidence Repository |
| 5 | Gap Analysis |
| 6 | Summary Dashboard |
| 7 | Approval Sign-Off |
| 8 | Instructions & Legend |

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
| 1 | Transfer ID |
| 2 | Status |
| 3 | Transfer Name |
| 4 | Source System |
| 5 | Destination System |
| 6 | Destination Country |
| 7 | Adequacy Status |
| 8 | Transfer Mechanism |
| 9 | SCC Version |
| 10 | SCC Date |
| 11 | DPF Cert? |
| 12 | TIA Required? |
| 13 | TIA ID |
| 14 | PII Categories |
| 15 | Transfer Volume |
| 16 | Transfer Frequency |
| 17 | Purpose |
| 18 | Legal Basis (Art.6) |
| 19 | Last Updated |
| 20 | Notes |
| 21 | Assessment Date |
| 22 | Assessor |
| 23 | Surveillance Laws |
| 24 | Gov Access Risk |
| 25 | Risk Justification |
| 26 | Supplementary Measures |
| 27 | Residual Risk |
| 28 | TIA Conclusion |
| 29 | DPO Approval |
| 30 | Next Review Date |
| 31 | Processor ID |
| 32 | Processor Name |
| 33 | Processor Location |
| 34 | DPA Exists? |
| 35 | DPA Date |
| 36 | SCCs Included? |
| 37 | Subprocessors? |
| 38 | Compliance Status |
| 39 | Gap Description |
| 40 | Remediation Action |
| 41 | Owner |
| 42 | Deadline |
| 43 | Evidence ID |
| 44 | Evidence Type |
| 45 | Description |
| 46 | Document Name |
| 47 | File Location |
| 48 | Upload Date |
| 49 | Gap ID |
| 50 | Gap Type |
| 51 | Risk Level |
| 52 | Affected Data Subjects |
| 53 | Discovery Date |
| 54 | Target Date |
| 55 | Assessment Area |
| 56 | Total Items |
| 57 | Compliant |
| 58 | Partial |
| 59 | Non-Compliant |
| 60 | N/A |
| 61 | Compliance % |
| 62 | Metric |
| 63 | Value |
| 64 | Category |
| 65 | Finding |
| 66 | Count |
| 67 | Severity |
| 68 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 8 sheets, 68 columns, 8 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The problems of language here are really serious. We wish to speak in some way about the structure of the atoms. But we cannot speak about atoms in ordinary language."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
