<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.1-3.S1-TG:framework:TG:a.7.1-3 -->
**ISMS-IMP-A.7.1-3.S1-TG - Perimeter Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.1: Physical Security Perimeters

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Perimeter Security Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.1-3.S1-TG |
| **Related Policy** | ISMS-POL-A.7.1-3-S1 (Physical Access Control) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.1 (Physical Security Perimeters) |
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

- ISMS-POL-A.7.1-3-S1 (Physical Access Control)
- ISMS-IMP-A.7.1-3-S2 (Entry Control Assessment)
- ISMS-IMP-A.7.1-3-S3 (Secure Areas Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a71_1_perimeter_security.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.1.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Security Zones |
| 3 | Building Perimeter |
| 4 | Internal Perimeters |
| 5 | Perimeter Monitoring |
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
| 1 | Zone ID |
| 2 | Zone Name |
| 3 | Zone Type |
| 4 | Location/Building |
| 5 | Classification |
| 6 | Access Requirements |
| 7 | Perimeter Defined |
| 8 | Status |
| 9 | Notes |
| 10 | Building/Facility |
| 11 | Perimeter Element |
| 12 | Construction Type |
| 13 | Solid Construction |
| 14 | Gap/Breach Points |
| 15 | Security Controls |
| 16 | Last Inspection |
| 17 | Inspector |
| 18 | From Zone |
| 19 | To Zone |
| 20 | Barrier Type |
| 21 | Floor-to-Ceiling |
| 22 | Above Ceiling Check |
| 23 | Below Floor Check |
| 24 | Access Control |
| 25 | Entry Point ID |
| 26 | Location |
| 27 | Entry Type |
| 28 | CCTV Coverage |
| 29 | Intrusion Detection |
| 30 | Alert Response |
| 31 | Last Tested |
| 32 | Evidence ID |
| 33 | Assessment Area |
| 34 | Evidence Type |
| 35 | Description |
| 36 | Location/Path |
| 37 | Date Collected |
| 38 | Collected By |
| 39 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Public Zone, Controlled Zone, Restricted Zone
High-Security Zone, Tier 1 - Critical, Tier 2 - Important, Tier 3 - Standard
External Wall, Roof, Floor, Window, External Door, Emergency Exit
Loading Dock, Other, Solid Wall, Glass Partition, Demountable Partition
Security Cage, N/A, Main Entrance, Side Door, Roof Access, Vent/Service Point
Floor plan, Photograph, Inspection report, Configuration file, Test report
Policy document, Verified, Pending verification, Not verified, Requires update
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 8 sheets, 39 columns, 45 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The strength of a chain is determined by its weakest link; the security of a perimeter, by its least protected point."*
--- Bruce Schneier

<!-- QA_VERIFIED: 2026-03-01 -->
