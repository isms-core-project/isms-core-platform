<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.29.2-TG:framework:TG:a.5.29.2 -->
**ISMS-IMP-A.5.29.2-TG - Degraded Mode Security Requirements**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Degraded Mode Security Requirements |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.29.2-TG |
| **Related Policy** | ISMS-POL-A.5.29 (Security During Disruption) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.29) |
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

- ISMS-POL-A.5.29 (Security During Disruption)
- ISMS-IMP-A.5.29.1 (Security Controls During Disruption Assessment)
- ISMS-IMP-A.5.29.3 (Recovery Security Verification)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a529_2_degraded_mode.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.29.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Degradation Scenarios |
| 3 | BreakGlass Accounts |
| 4 | BreakGlass Activation |
| 5 | Elevated Monitoring |
| 6 | Personnel Availability |
| 7 | Security Debt Register |
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
| 1 | Role / Function |
| 2 | Name |
| 3 | Signature / Initials |
| 4 | Date (DD.MM.YYYY) |
| 5 | Comments |
| 6 | Assessment Area |
| 7 | Total |
| 8 | Compliant |
| 9 | Partial |
| 10 | Non-Compliant |
| 11 | N/A |
| 12 | Compliance % |
| 13 | Metric |
| 14 | Value |
| 15 | Category |
| 16 | Finding |
| 17 | Count |
| 18 | Severity |
| 19 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Temporary Bypass, Reduced Capability, Postponed, Alternative Method, Elevated
Degraded, Emergency, Domain Admin, System Admin, Database Admin, Network Admin
Application Admin, Other, Yes, No, Verified, Disabled, Enabled, Unknown
Complete, Partial, None, Deferred Patch, Skipped Review, Delayed Scan
Config Exception, Access Exception, Open, In Progress, Closed, Policy Document
Process Record, System Screenshot, Configuration Export, Audit Log
Training Record, Test Result, Risk Assessment, Meeting Minutes, ✅ Verified
⚠️ Pending, ❌ Not Verified, N/A, Draft, Final, Requires remediation
Re-assessment required
```

**Extracted:** 10 sheets, 19 columns, 47 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"In preparing for battle I have always found that plans are useless, but planning is indispensable."*
— Dwight D. Eisenhower

<!-- QA_VERIFIED: 2026-02-06 -->
