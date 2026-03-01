<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.5-TG:framework:TG:a.5.34.5 -->
**ISMS-IMP-A.5.34.5-TG - Data Protection Impact Assessment (DPIA)**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | DPIA Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.34.5-TG |
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
- ISMS-IMP-A.5.34.6 (Cross Border Transfer Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a5345_dpia_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.34.5`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Summary Dashboard |
| 2 | Instructions |
| 3 | Trigger Assessment |
| 4 | DPIA Register |
| 5 | Risk Assessment |
| 6 | Mitigation Measures |
| 7 | Stakeholder Consultation |
| 8 | Gap Analysis |
| 9 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
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
| 1 | Processing Activity ID |
| 2 | Processing Activity Name |
| 3 | System/Application |
| 4 | Trigger 1: Systematic Profiling |
| 5 | Trigger 2: Large-Scale Special Categories |
| 6 | Trigger 3: Systematic Monitoring |
| 7 | Trigger 4: Innovative Technology |
| 8 | Trigger 5: Denial of Service |
| 9 | Trigger 6: Large Scale |
| 10 | Trigger 7: Matching Datasets |
| 11 | Trigger 8: Vulnerable Subjects |
| 12 | Trigger 9: Cross-Border Transfer |
| 13 | Total Triggers |
| 14 | DPIA Required? |
| 15 | Notes |
| 16 | DPIA ID |
| 17 | Business Owner |
| 18 | DPO Assigned |
| 19 | DPIA Start Date |
| 20 | Target Completion Date |
| 21 | Actual Completion Date |
| 22 | DPIA Status |
| 23 | Initial Risk Rating |
| 24 | Residual Risk Rating |
| 25 | Supervisory Authority Consulted? |
| 26 | Authority Consultation Date |
| 27 | Authority Reference Number |
| 28 | Next Review Date |
| 29 | DPIA Document Location |
| 30 | Risk ID |
| 31 | Risk Category |
| 32 | Risk Description |
| 33 | Data Subject Impact |
| 34 | Likelihood (Before Mitigation) |
| 35 | Impact (Before Mitigation) |
| 36 | Inherent Risk Score |
| 37 | Inherent Risk Level |
| 38 | Necessity Justified? |
| 39 | Necessity Justification |
| 40 | Proportionality Justified? |
| 41 | Proportionality Justification |
| 42 | Legal Basis |
| 43 | Special Category Legal Basis |
| 44 | Data Subject Rights Respected? |
| 45 | Rights Restrictions Documented |
| 46 | Third-Party Recipients |
| 47 | Cross-Border Transfers |
| 48 | Transfer Safeguards |
| 49 | Risk Description (Reference) |
| 50 | Mitigation Control ID |
| 51 | Control Type |
| 52 | Mitigation Description |
| 53 | Implementation Status |
| 54 | Owner |
| 55 | Target Date |
| 56 | Actual Date |
| 57 | Effectiveness Rating |
| 58 | Evidence Location |
| 59 | Stakeholder Type |
| 60 | Stakeholder Name/Title |
| 61 | Consultation Date |
| 62 | Consultation Method |
| 63 | Key Concerns Raised |
| 64 | Recommendations |
| 65 | Action Taken |
| 66 | Inherent Risk Score (Reference) |
| 67 | Mitigation Implemented? |
| 68 | Mitigation Effectiveness |
| 69 | Risk Reduction Factor |
| 70 | Residual Likelihood |
| 71 | Residual Risk Score |
| 72 | Residual Risk Level |
| 73 | Gap Identified? |
| 74 | Gap Description |
| 75 | Remediation Plan |
| 76 | Assessment Area |
| 77 | Total Items |
| 78 | Compliant |
| 79 | Partial |
| 80 | Non-Compliant |
| 81 | N/A |
| 82 | Compliance % |
| 83 | Metric |
| 84 | Value |
| 85 | Category |
| 86 | Finding |
| 87 | Count |
| 88 | Severity |
| 89 | Action Required |

**Extracted:** 9 sheets, 89 columns, 0 validation values, 8 colors

---

**END OF SPECIFICATION**


---

*"Whenever we proceed from the known into the unknown we may hope to understand, but we may have to learn at the same time a new meaning of the word understanding."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
