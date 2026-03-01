<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.6-7-14-S2-TG:framework:TG:a.7.6-7-14-s2 -->
**ISMS-IMP-A.7.6-7-14-S2-TG - Clear Desk and Clear Screen Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.7: Clear Desk and Clear Screen

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Clear Desk Screen Compliance |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.6-7-14-S2-TG |
| **Related Policy** | ISMS-POL-A.7.6-7-14-S2 (Information Media Handling) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.7 (Clear Desk and Clear Screen) |
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

- ISMS-POL-A.7.6-7-14-S2 (Information Media Handling)
- ISMS-IMP-A.7.6-7-14-S1 (Secure Areas Working Assessment)
- ISMS-IMP-A.7.6-7-14-S3 (Equipment Disposal Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a76_2_clear_desk_screen.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.7.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Requirements Matrix |
| 3 | Screen Lock Configuration |
| 4 | Audit Results |
| 5 | Workspace Assessment |
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
| 1 | Classification |
| 2 | Clear Desk - Work Hours |
| 3 | Clear Desk - End of Day |
| 4 | Storage Requirement |
| 5 | Screen Lock Timeout (min) |
| 6 | Privacy Screen Required |
| 7 | Implementation Status |
| 8 | Notes |
| 9 | Device Type |
| 10 | Policy/GPO Name |
| 11 | Configured Timeout (min) |
| 12 | Required Timeout (min) |
| 13 | Compliant |
| 14 | Enforcement Method |
| 15 | Device Count |
| 16 | Last Verified |
| 17 | Evidence |
| 18 | Audit Date |
| 19 | Audit Type |
| 20 | Location/Area |
| 21 | Workstations Audited |
| 22 | Non-Compliant |
| 23 | Compliance Rate |
| 24 | Common Issues |
| 25 | Follow-Up Actions |
| 26 | Auditor |
| 27 | Area ID |
| 28 | Location |
| 29 | Workspace Type |
| 30 | Workstation Count |
| 31 | Lockable Storage |
| 32 | Shredder Access |
| 33 | Confidential Bins |
| 34 | Privacy Screens |
| 35 | Avg Audit Compliance |
| 36 | Status |
| 37 | Workspace Assessment |
| 38 | Requirements Matrix |
| 39 | Assessment Area |
| 40 | Total Items |
| 41 | Partial |
| 42 | N/A |
| 43 | Compliance % |
| 44 | Evidence ID |
| 45 | Evidence Type |
| 46 | Description |
| 47 | Location/Path |
| 48 | Date Collected |
| 49 | Collected By |
| 50 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Implemented, Partial, Not Implemented, Required, Recommended, Not Required
Group Policy, MDM (Intune), MDM (JAMF), MDM (Other), Manual, Not Enforced, Yes
No, Scheduled Monthly, Random Spot Check, Post-Incident, Annual Comprehensive
Open Plan Office, Private Office, Meeting Room, Shared Space, Home Office
Reception, Yes - All, Yes - Partial, Yes - On Floor, Yes - Central, N/A
Approved, Approved with Conditions, Rejected, Deferred, Policy document
Procedure document, Screenshot, Photograph, Audit report, Training record
Configuration file, Other, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
```

**Extracted:** 8 sheets, 50 columns, 49 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The best defence against data leakage is a culture of security, not just a policy document."*
— Unknown

<!-- QA_VERIFIED: 2026-03-01 -->
