<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.4-5-11-S3-TG:framework:TG:a.7.4-5-11 -->
**ISMS-IMP-A.7.4-5-11-S3-TG - Utility Resilience Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.11: Supporting Utilities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Utility Resilience Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.4-5-11-S3-TG |
| **Related Policy** | ISMS-POL-A.7.4-5-11-S3 (Physical Infrastructure) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.4 (Physical Security Monitoring) |
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

- ISMS-POL-A.7.4-5-11-S3 (Physical Infrastructure)
- ISMS-IMP-A.7.4-5-11-S1 (Physical Monitoring Assessment)
- ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a74_3_utility_resilience.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.4.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Power Infrastructure |
| 3 | HVAC |
| 4 | Telecommunications |
| 5 | Evidence Register |
| 6 | Summary Dashboard |
| 7 | Approval Sign-Off |

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
| 1 | UPS ID |
| 2 | Capacity (kVA) |
| 3 | Load (%) |
| 4 | Battery (%) |
| 5 | Runtime (min) |
| 6 | Status |
| 7 | Evidence Location |
| 8 | HVAC ID |
| 9 | Capacity (Tons) |
| 10 | Redundancy |
| 11 | Last Service |
| 12 | ISP ID |
| 13 | Provider |
| 14 | Bandwidth (Mbps) |
| 15 | SLA (%) |
| 16 | Actual (%) |
| 17 | Incident ID |
| 18 | Date |
| 19 | Type |
| 20 | Severity |
| 21 | Location |
| 22 | Response Time (min) |
| 23 | Resolved |
| 24 | Notes |
| 25 | Assessment Area |
| 26 | Total Items |
| 27 | Compliant |
| 28 | Partial |
| 29 | Non-Compliant |
| 30 | N/A |
| 31 | Compliance % |
| 32 | Evidence ID |
| 33 | Evidence Type |
| 34 | Description |
| 35 | Location/Path |
| 36 | Date Collected |
| 37 | Collected By |
| 38 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Not Applicable, Tailgating, Unauthorised Access, Alarm Trigger
Lost Badge, Forced Entry, Other, Critical, High, Medium, Low, Floor plan
Photograph, Inspection report, Configuration file, Test report
Policy document, Verified, Pending verification, Not verified, Requires update
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 7 sheets, 38 columns, 31 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The best way to send information is to wrap it up in a person."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-03-01 -->
