<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.1-3.S3-TG:framework:TG:a.7.1-3 -->
**ISMS-IMP-A.7.1-3.S3-TG - Secure Areas Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.3: Securing Offices, Rooms and Facilities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Areas Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.1-3.S3-TG |
| **Related Policy** | ISMS-POL-A.7.1-3-S3 (Physical Access Control) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.3 (Securing Offices, Rooms and Facilities) |
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

- ISMS-POL-A.7.1-3-S3 (Physical Access Control)
- ISMS-IMP-A.7.1-3-S1 (Perimeter Security Assessment)
- ISMS-IMP-A.7.1-3-S2 (Entry Control Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a71_3_secure_areas.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.1.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Office Security |
| 3 | Server Rooms |
| 4 | Meeting Rooms |
| 5 | Shared Facilities |
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
| 1 | Office/Area ID |
| 2 | Location |
| 3 | Security Zone |
| 4 | Classification |
| 5 | Lock When Unoccupied |
| 6 | Clean Desk Enforced |
| 7 | Screen Privacy |
| 8 | Secure Storage |
| 9 | Status |
| 10 | Notes |
| 11 | Room ID |
| 12 | Room Type |
| 13 | MFA Access |
| 14 | No Windows |
| 15 | Reinforced Walls |
| 16 | CCTV Coverage |
| 17 | Access Logging |
| 18 | Env. Monitoring |
| 19 | Room Classification |
| 20 | Recording Check |
| 21 | Whiteboard Clear |
| 22 | Document Clear |
| 23 | VC Equipment Secured |
| 24 | Facility/Building |
| 25 | Sharing Arrangement |
| 26 | Perimeter Defined |
| 27 | Own Access Control |
| 28 | Building Mgmt Access |
| 29 | Shared Infrastructure |
| 30 | Key Management |
| 31 | Evidence ID |
| 32 | Assessment Area |
| 33 | Evidence Type |
| 34 | Description |
| 35 | Location/Path |
| 36 | Date Collected |
| 37 | Collected By |
| 38 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Controlled Zone, Restricted Zone, High-Security Zone, Public
Internal, Confidential, Highly Confidential, N/A, Server Room, Datacenter
Network Closet, Comms Room, UPS Room, Generator Room, Standard Meeting Room
Boardroom, Secure Meeting Room, Interview Room, N/A - Sole Occupant
Multi-Tenant Building, Co-Working Space, Shared Floor, Colocation Facility
Sole Occupant, Controlled and Logged, Controlled Only, Uncontrolled
Floor plan, Photograph, Access log, Configuration screenshot
Inspection report, Policy document, Other, Verified, Pending verification
Not verified, Requires update, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 8 sheets, 38 columns, 49 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The security of a place lies not just in its walls, but in the practices of those within."*
--- Physical Security Principle

<!-- QA_VERIFIED: 2026-03-01 -->
