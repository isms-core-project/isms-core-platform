<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.7-8.S2-TG:framework:TG:a.6.7-8 -->
**ISMS-IMP-A.6.7-8.S2-TG - Technical Controls Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Technical Controls Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.7-8.S2-TG |
| **Related Policy** | ISMS-POL-A.6.7-8 (Remote Working and Reporting) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting) |
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

- ISMS-POL-A.6.7-8 (Remote Working and Reporting)
- ISMS-IMP-A.6.7-8.S1 (Remote Work Authorisation Assessment)
- ISMS-IMP-A.6.7-8.S3 (Endpoint and Physical Security Assessment)
- ISMS-IMP-A.6.7-8.S4 (Event Reporting Mechanisms Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a678_s2_technical_controls.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.6.7-8.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | VPN Assessment |
| 3 | MFA Assessment |
| 4 | Encryption Assessment |
| 5 | Logging Assessment |
| 6 | Compliance Summary |
| 7 | Gap Analysis |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

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
| 1 | Requirement |
| 2 | Description |
| 3 | Level |
| 4 | Implemented |
| 5 | Evidence |
| 6 | Compliance |
| 7 | Notes |
| 8 | Control Area |
| 9 | Total Requirements |
| 10 | Compliant |
| 11 | Non-Compliant |
| 12 | Compliance % |
| 13 | Gap ID |
| 14 | Gap Description |
| 15 | Impact |
| 16 | Risk Level |
| 17 | Remediation |
| 18 | Owner |
| 19 | Target Date |
| 20 | Status |
| 21 | Evidence ID |
| 22 | Evidence Type |
| 23 | Source / Owner |
| 24 | Date Collected |
| 25 | Retention Period |
| 26 | Storage Location |
| 27 | Assessment Area |
| 28 | Total Items |
| 29 | Partial |
| 30 | N/A |
| 31 | Category |
| 32 | Finding |
| 33 | Count |
| 34 | Severity |
| 35 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, N/A, Compliant, Non-Compliant, VPN, MFA, Encryption, Logging
Critical, High, Medium, Low, Open, In Progress, Resolved, Accepted, Collected
Pending, Not Available, Superseded, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 35 columns, 30 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Complexity is the enemy of security."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-03-01 -->
