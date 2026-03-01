<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.1-2-3-S2-TG:framework:TG:a.7.1-2-3-s2 -->
**ISMS-IMP-A.7.1-2-3-S2-TG - Entry Control Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.2: Physical Entry

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Entry Control Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.1-2-3-S2-TG |
| **Related Policy** | ISMS-POL-A.7.1-2-3-S2 (Physical Access Control) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.2 (Physical Entry) |
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

- ISMS-POL-A.7.1-2-3-S2 (Physical Access Control)
- ISMS-IMP-A.7.1-2-3-S1 (Perimeter Security Assessment)
- ISMS-IMP-A.7.1-2-3-S3 (Secure Areas Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a71_2_entry_control.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.1.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Access Control Systems |
| 3 | Visitor Management |
| 4 | Contractor Access |
| 5 | After-Hours Access |
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
| 1 | Entry Point ID |
| 2 | Location |
| 3 | Security Zone |
| 4 | Access System Type |
| 5 | Authentication Method |
| 6 | Anti-Tailgating |
| 7 | Log Retention (Days) |
| 8 | Last Review Date |
| 9 | Status |
| 10 | Notes |
| 11 | Procedure Element |
| 12 | Location/Facility |
| 13 | Implemented |
| 14 | Sign-In Process |
| 15 | ID Verification |
| 16 | Badge Issued |
| 17 | Escort Required |
| 18 | Contractor Type |
| 19 | Facility/Area |
| 20 | Pre-Authorisation |
| 21 | Time-Limited Access |
| 22 | Access Logged |
| 23 | Supervision Level |
| 24 | Facility/Entry Point |
| 25 | After-Hours Period |
| 26 | Enhanced Auth |
| 27 | Alarm Integration |
| 28 | Security Response |
| 29 | Evidence ID |
| 30 | Assessment Area |
| 31 | Evidence Type |
| 32 | Description |
| 33 | Location/Path |
| 34 | Date Collected |
| 35 | Collected By |
| 36 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Controlled Zone, Restricted Zone, High-Security Zone
Card Reader, PIN Pad, Biometric, Card + PIN, Card + Biometric, Multi-Factor
Badge/Card Only, Badge + PIN, Badge + Biometric, PIN + Biometric
Dual-Person Control, Reception Sign-In, ID Check, Visitor Badge, Escort Policy
Sign-Out Process, Log Retention, After-Hours Visitors, N/A, IT Maintenance
Cleaning, Security Services, HVAC/Facilities, Delivery, Construction
Consultants, Other, Full Escort, Spot Checks, Self-Supervised, Not Required
Access log, Visitor log, Configuration screenshot, Policy document
Test report, Badge sample, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 8 sheets, 36 columns, 55 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Security is not just about locks and keys; it's about ensuring only the right people pass through at the right time."*
--- Security Operations Principle

<!-- QA_VERIFIED: 2026-03-01 -->
