<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.8-9-S1-TG:framework:TG:a.7.8-9-s1 -->
**ISMS-IMP-A.7.8-9-S1-TG - Equipment Siting Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.8: Equipment Siting and Protection

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Equipment Siting Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.8-9-S1-TG |
| **Related Policy** | ISMS-POL-A.7.8-9-S1 (Equipment Location Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.8 (Equipment Siting and Protection) |
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

- ISMS-POL-A.7.8-9-S1 (Equipment Location Security)
- ISMS-IMP-A.7.8-9-S2 (Off-Premises Asset Security)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a78_1_equipment_siting.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.8.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Equipment Locations |
| 3 | Environmental |
| 4 | Physical Security |
| 5 | Power Infrastructure |
| 6 | Workstation Security |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
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
| 1 | Location ID |
| 2 | Location Name |
| 3 | Location Type |
| 4 | Building/Address |
| 5 | Equipment Types |
| 6 | Criticality Tier |
| 7 | Access Control Type |
| 8 | Environmental Monitoring |
| 9 | CCTV Coverage |
| 10 | UPS Protected |
| 11 | Last Inspection |
| 12 | Compliance Status |
| 13 | Notes |
| 14 | Temperature Range |
| 15 | Humidity Range |
| 16 | Temperature Monitoring |
| 17 | Flood Risk |
| 18 | Fire Suppression |
| 19 | Dust/Contamination |
| 20 | Vibration Exposure |
| 21 | Food/Drink Prohibited |
| 22 | Incidents (12 months) |
| 23 | Access Control System |
| 24 | Access Levels Defined |
| 25 | Log Retention (Days) |
| 26 | CCTV System |
| 27 | CCTV Retention (Days) |
| 28 | Equipment Locking |
| 29 | Cable Protection |
| 30 | Asset Labels |
| 31 | Segregation |
| 32 | Last Security Review |
| 33 | UPS Coverage |
| 34 | UPS Runtime (min) |
| 35 | Generator Backup |
| 36 | Surge Protection |
| 37 | Lightning Protection |
| 38 | EPO Switch |
| 39 | Power Redundancy |
| 40 | Last UPS Test |
| 41 | Last Generator Test |
| 42 | Power Incidents (12m) |
| 43 | Area ID |
| 44 | Area Name |
| 45 | Workstation Count |
| 46 | Data Sensitivity |
| 47 | Screen Positioning |
| 48 | Privacy Screens |
| 49 | Automatic Lock |
| 50 | Clear Desk Policy |
| 51 | Visitor Access |
| 52 | Shoulder Surfing Risk |
| 53 | Last Review |
| 54 | Evidence ID |
| 55 | Evidence Type |
| 56 | Description |
| 57 | Related Sheet/Item |
| 58 | Collection Date |
| 59 | Collected By |
| 60 | Retention Period |
| 61 | Assessment Area |
| 62 | Total Items |
| 63 | Compliant |
| 64 | Partial |
| 65 | Non-Compliant |
| 66 | N/A |
| 67 | Compliance % |
| 68 | Metric |
| 69 | Value |
| 70 | Category |
| 71 | Finding |
| 72 | Count |
| 73 | Severity |
| 74 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Data Centre, Server Room, Network Closet, Office Area, Co-location
Remote Office, Other, Tier 1 - Critical, Tier 2 - Standard
Tier 3 - Non-Critical, Biometric + Badge, Badge Only, Key Lock
Combination Lock, No Access Control, Yes - Real-time alerts
Yes - Periodic checks, No monitoring, Yes - 24/7 recording
Yes - Motion triggered, No CCTV, Yes - Full coverage, Partial coverage, No UPS
Yes - Daily checks, High (below grade), Medium (ground floor)
Low (upper floor), Protected (raised floor), Gas suppression
Pre-action sprinkler, Wet sprinkler, Extinguishers only, None, Clean room
Filtered HVAC, Standard office, Industrial/Dusty, Low (isolated)
Medium (standard building), High (near machinery), Yes - Enforced
Yes - Policy only, No restriction, Rack locks + Cable locks, Rack locks only
Cable locks only, Enclosed conduit, Cable trays, Exposed cabling
Yes - All labelled, Partial, No labels, Yes - Physical separation
Partial - Logical only, No - Shared space, 100% (all equipment)
Partial (critical only), Yes - Auto-transfer, Yes - Manual transfer
No generator, Yes - All circuits, Yes - Building grounded, Unknown, No
Yes - Near room, Yes - Remote only, No EPO, Dual feed (A+B), Single feed + UPS
Single feed only, High (PII, Financial), Medium (Internal), Low (Public)
Optimal (away from windows/traffic), Acceptable, At risk (visible to public)
Yes - All workstations, Yes - <5 min timeout, Yes - >5 min timeout
Not configured, No policy, Escorted only, Badge required, Open access, Low
Medium, High, Screenshot, Configuration Export, Log Sample, Report, Document
Photo, Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 74 columns, 103 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Security is mostly a superstition. Life is either a daring adventure or nothing."*
-- Helen Keller

<!-- QA_VERIFIED: 2026-03-01 -->
