<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.4-5-11-S2-TG:framework:TG:a.7.4-5-11 -->
**ISMS-IMP-A.7.4-5-11-S2-TG - Environmental Protection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.5: Protecting Against Physical and Environmental Threats

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Environmental Protection Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.4-5-11-S2-TG |
| **Related Policy** | ISMS-POL-A.7.4-5-11-S2 (Physical Infrastructure) |
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

- ISMS-POL-A.7.4-5-11-S2 (Physical Infrastructure)
- ISMS-IMP-A.7.4-5-11-S1 (Physical Monitoring Assessment)
- ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a74_2_environmental_protection.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.4.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Fire Detection |
| 3 | Water Detection |
| 4 | Temperature & Humidity |
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
| 1 | Detector ID |
| 2 | Type |
| 3 | Location |
| 4 | Last Tested |
| 5 | Status |
| 6 | Evidence Location |
| 7 | Sensor ID |
| 8 | Temp Range (°C) |
| 9 | Humidity Range (%) |
| 10 | Incident ID |
| 11 | Date |
| 12 | Severity |
| 13 | Response Time (min) |
| 14 | Resolved |
| 15 | Notes |
| 16 | Assessment Area |
| 17 | Total Items |
| 18 | Compliant |
| 19 | Partial |
| 20 | Non-Compliant |
| 21 | N/A |
| 22 | Compliance % |
| 23 | Evidence ID |
| 24 | Evidence Type |
| 25 | Description |
| 26 | Location/Path |
| 27 | Date Collected |
| 28 | Collected By |
| 29 | Verification Status |

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

**Extracted:** 7 sheets, 29 columns, 31 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Both the man of science and the man of action live always at the edge of mystery, surrounded by it."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-03-01 -->
