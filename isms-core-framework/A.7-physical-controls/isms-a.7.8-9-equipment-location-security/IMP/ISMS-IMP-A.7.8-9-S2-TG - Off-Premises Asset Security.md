<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.8-9-S2-TG:framework:TG:a.7.8-9-s2 -->
**ISMS-IMP-A.7.8-9-S2-TG - Off-Premises Asset Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.9: Security of Assets Off-Premises

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Off-Premises Asset Security |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.8-9-S2-TG |
| **Related Policy** | ISMS-POL-A.7.8-9-S2 (Equipment Location Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.9 (Security of Assets Off-Premises) |
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

- ISMS-POL-A.7.8-9-S2 (Equipment Location Security)
- ISMS-IMP-A.7.8-9-S1 (Equipment Siting Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a78_2_offpremises_assets.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.9.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Equipment Inventory |
| 3 | Authorisation |
| 4 | Protection Measures |
| 5 | Remote Working |
| 6 | Permanent Off-Site |
| 7 | Incidents |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

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
| 1 | Category ID |
| 2 | Equipment Category |
| 3 | Equipment Type |
| 4 | Total Count |
| 5 | Off-Premises Count |
| 6 | Primary Use Case |
| 7 | MDM Managed |
| 8 | Encryption Enabled |
| 9 | Remote Wipe Capable |
| 10 | GPS Tracking |
| 11 | Last Compliance Check |
| 12 | Compliance Status |
| 13 | Notes |
| 14 | Authorisation Required |
| 15 | Authorisation Method |
| 16 | Tracking System |
| 17 | Chain of Custody |
| 18 | Return Verification |
| 19 | Overdue Alert |
| 20 | Current Overdue |
| 21 | Last Process Review |
| 22 | Physical Security |
| 23 | Transport Guidelines |
| 24 | Public Place Rules |
| 25 | Storage When Not In Use |
| 26 | Environmental Protection |
| 27 | Privacy Screen Required |
| 28 | VPN Required |
| 29 | Screen Lock Timeout |
| 30 | Scenario ID |
| 31 | Work Scenario |
| 32 | Data Sensitivity |
| 33 | VPN Requirement |
| 34 | Privacy Screen |
| 35 | WiFi Security |
| 36 | Visitor Access |
| 37 | Bluetooth/Wireless |
| 38 | Worker Count |
| 39 | Last Review |
| 40 | Installation ID |
| 41 | Installation Name |
| 42 | Installation Type |
| 43 | Location Count |
| 44 | Environmental Monitoring |
| 45 | Remote Management |
| 46 | Inspection Schedule |
| 47 | Last Inspection |
| 48 | Incident Response |
| 49 | Incident ID |
| 50 | Incident Date |
| 51 | Incident Type |
| 52 | Location |
| 53 | Data at Risk |
| 54 | Remote Wipe Executed |
| 55 | Time to Report (hrs) |
| 56 | Recovery Status |
| 57 | Root Cause |
| 58 | Corrective Action |
| 59 | Evidence ID |
| 60 | Evidence Type |
| 61 | Description |
| 62 | Related Sheet/Item |
| 63 | Collection Date |
| 64 | Collected By |
| 65 | Retention Period |
| 66 | Assessment Area |
| 67 | Total Items |
| 68 | Compliant |
| 69 | Partial |
| 70 | Non-Compliant |
| 71 | N/A |
| 72 | Compliance % |
| 73 | Metric |
| 74 | Value |
| 75 | Category |
| 76 | Finding |
| 77 | Count |
| 78 | Severity |
| 79 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Laptop, Mobile Phone, Tablet, Storage Media, Edge Device, Other
Yes - All devices, Partial, No, Yes - 100%, Partial (>80%), Low (<80%)
Yes - Tested, Yes - Not tested, Yes - Enabled, Available - Not enabled
Not available, Yes - Manager approval, Yes - IT approval, Yes - Auto-approved
No approval required, Yes - Full tracking, Yes - Physical check
Yes - System check, No verification, Yes - Automated, Yes - Manual review
Cable lock required, Secure bag required, No requirement, Yes - Documented
No guidelines, Yes - Never unattended, Yes - Partial rules, No rules
Locked storage required, Secure location recommended
Yes - Guidelines provided, Yes - Always, Yes - For sensitive data
Yes - All connections, Yes - Untrusted networks, High (PII, Financial)
Medium (Internal), Low (Public), Required - Always, Required - Sensitive only
Recommended, Not required, Required, Encrypted only, VPN for public WiFi
Locked when away, Not visible to others, No access allowed
Supervised access only, N/A, Disable when not needed, ATM/Kiosk, Sensor/IoT
Edge Computing, Signage, Antenna/Telecom, Tamper detection, Locked enclosure
Public exposure, Yes - Continuous, Yes - Periodic, Yes - Full control, Monthly
Quarterly, Annual, None, No procedure, Lost, Stolen, Damaged, Compromised
Near Miss, None (encrypted), Yes - Successful, Yes - Failed, No - Not needed
No - Not possible, Recovered, Not recovered, Insurance claim, Replaced
Screenshot, Configuration Export, Log Sample, Report, Document, Photo, Draft
Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 79 columns, 103 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"The price of freedom is eternal vigilance."*
-- Thomas Jefferson

<!-- QA_VERIFIED: 2026-03-01 -->
