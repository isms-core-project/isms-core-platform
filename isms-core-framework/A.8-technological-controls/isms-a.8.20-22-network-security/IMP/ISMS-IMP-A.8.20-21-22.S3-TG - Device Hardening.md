<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S3-TG:framework:TG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S3-TG - Device Hardening Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Device Hardening |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-21-22.S3-TG |
| **Related Policy** | ISMS-POL-A.8.20-21-22 (Network Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.20 (Networks Security) |
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

- ISMS-POL-A.8.20-21-22 (Network Security)
- ISMS-IMP-A.8.20-21-22.S1 (Network Discovery)
- ISMS-IMP-A.8.20-21-22.S2 (Architecture Documentation)
- ISMS-IMP-A.8.20-21-22.S4 (Services Security)
- ISMS-IMP-A.8.20-21-22.S5 (Segmentation Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a820_3_services_catalog.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.20-21-22.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Evidence Register |
| 2 | Approval Sign-Off |
| 3 | Instructions & Legend |
| 4 | Services Catalog |
| 5 | DNS Security Assessment |
| 6 | DHCP Security Assessment |
| 7 | NTP Security Assessment |
| 8 | Proxy Security Assessment |
| 9 | Additional Services |
| 10 | Summary Dashboard |
| 11 | Gap Analysis |
| 12 | Service Dependencies |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #4472C4 | Medium Blue (Sub-headers) |
| #7F7F7F | Custom |
| #808080 | Gray (Disabled) |
| #9C0006 | Dark Red (Error) |
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
| 1 | Assessment Area |
| 2 | Total |
| 3 | Yes |
| 4 | Partial |
| 5 | N-A |
| 6 | Compliance % |
| 7 | DNS SECURITY ASSESSMENT |
| 8 | DHCP SECURITY ASSESSMENT |
| 9 | NTP SECURITY ASSESSMENT |
| 10 | PROXY/WEB FILTER SECURITY ASSESSMENT |
| 11 | ADDITIONAL NETWORK SERVICES ASSESSMENT |
| 12 | What This Shows |
| 13 | Critical Finding Type |
| 14 | Filter Instructions |
| 15 | SERVICE SECURITY GAPS - REMEDIATION TRACKING |
| 16 | Network Team |
| 17 | SERVICE DEPENDENCIES MAPPING |
| 18 | Service ID |
| 19 | Service Type |
| 20 | Service Name |
| 21 | Purpose |
| 22 | Hosting Location |
| 23 | IP Address |
| 24 | Port(s) |
| 25 | Criticality |
| 26 | Redundancy Level |
| 27 | Monitoring Status |
| 28 | SLA Uptime % |
| 29 | Owner |
| 30 | Last Security Review |
| 31 | Status |
| 32 | Notes |
| 33 | Assessment Link |
| 34 | DNS Type |
| 35 | DNSSEC Enabled |
| 36 | Split DNS |
| 37 | Rate Limiting |
| 38 | Query Logging |
| 39 | RPZ/Filtering |
| 40 | Recursion Control |
| 41 | Cache Poisoning Protection |
| 42 | Zone Transfer Controls |
| 43 | TSIG/SIG(0) |
| 44 | Compliance Score % |
| 45 | Last Assessed |
| 46 | DHCP Scope |
| 47 | DHCP Snooping |
| 48 | Rogue DHCP Detection |
| 49 | Server Hardening |
| 50 | Lease Time Appropriate |
| 51 | Utilization Monitoring |
| 52 | Reservation Management |
| 53 | Logging Enabled |
| 54 | NTP Role |
| 55 | Authentication |
| 56 | Access Control |
| 57 | Stratum Appropriate |
| 58 | Source Validation |
| 59 | Monitoring |
| 60 | Stratum Level |
| 61 | Proxy Type |
| 62 | SSL Inspection |
| 63 | Category Filtering |
| 64 | Malware Scanning |
| 65 | Logging |
| 66 | Bypass Prevention |
| 67 | Redundancy |
| 68 | Filter Categories |
| 69 | Encryption |
| 70 | Hardening Applied |
| 71 | Key Controls |
| 72 | Gap ID |
| 73 | Security Gap |
| 74 | Current State |
| 75 | Severity |
| 76 | Remediation Plan |
| 77 | Target Date |
| 78 | Depends On |
| 79 | Required By |
| 80 | Impact of Failure |
| 81 | Evidence ID |
| 82 | Evidence Type |
| 83 | Description |
| 84 | Location/Path |
| 85 | Date Collected |
| 86 | Collected By |
| 87 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Critical, High, Medium, Low, Active, Offline, Planned, Decommissioned, Yes, No
N/A, Active-Active, Active-Passive, Clustered, Single Point of Failure
Monitored, Not Monitored, Partially Monitored, Open, In Progress, Resolved
Accepted Risk, Configuration file, Screenshot, Network scan, Documentation
Vendor spec, Certificate inventory, Audit log, Compliance report, Other
✅ Verified, ⚠️ Pending, ❌ Not Verified, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 87 columns, 42 validation values, 13 colors

---

**END OF SPECIFICATION**


---

*"I would not dare to say that there is a direct relation between mathematics and madness, but there is no doubt that great mathematicians suffer from maniacal characteristics."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
