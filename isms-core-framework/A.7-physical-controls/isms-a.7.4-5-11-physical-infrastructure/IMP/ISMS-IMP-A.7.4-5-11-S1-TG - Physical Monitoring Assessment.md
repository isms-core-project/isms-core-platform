<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.4-5-11-S1-TG:framework:TG:a.7.4-5-11 -->
**ISMS-IMP-A.7.4-5-11-S1-TG - Physical Monitoring Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.4: Physical Security Monitoring

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Physical Monitoring Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.4-5-11-S1-TG |
| **Related Policy** | ISMS-POL-A.7.4-5-11 (Physical Infrastructure) |
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

- ISMS-POL-A.7.4-5-11 (Physical Infrastructure)
- ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection Implementation)
- ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a74_1_access_monitoring.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.4-5-11-S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Access Control |
| 3 | CCTV |
| 4 | Intrusion Detection |
| 5 | Incidents |
| 6 | Evidence Register |
| 7 | Summary Dashboard |
| 8 | Approval Sign-Off |

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
| 1 | Door ID |
| 2 | Location/Building |
| 3 | Reader Type |
| 4 | Last Tested |
| 5 | Status |
| 6 | Notes |
| 7 | Evidence Location |
| 8 | Camera ID |
| 9 | Location |
| 10 | Coverage Area |
| 11 | Recording |
| 12 | Retention (Days) |
| 13 | Sensor ID |
| 14 | Type |
| 15 | Armed |
| 16 | Incident ID |
| 17 | Date |
| 18 | Severity |
| 19 | Response Time (min) |
| 20 | Resolved |
| 21 | Assessment Area |
| 22 | Total Items |
| 23 | Compliant |
| 24 | Partial |
| 25 | Non-Compliant |
| 26 | N/A |
| 27 | Compliance % |
| 28 | Evidence ID |
| 29 | Evidence Type |
| 30 | Description |
| 31 | Location/Path |
| 32 | Date Collected |
| 33 | Collected By |
| 34 | Verification Status |

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

**Extracted:** 8 sheets, 34 columns, 31 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"There must be no barriers to freedom of inquiry. There is no place for dogma in science."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-03-01 -->
