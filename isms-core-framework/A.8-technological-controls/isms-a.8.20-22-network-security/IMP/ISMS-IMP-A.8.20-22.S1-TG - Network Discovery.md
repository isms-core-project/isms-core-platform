<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-22.S1-TG:framework:TG:a.8.20-22 -->
**ISMS-IMP-A.8.20-22.S1-TG - Network Discovery Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Network Discovery |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-22.S1-TG |
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
- ISMS-IMP-A.8.20-22.S2 (Architecture Documentation)
- ISMS-IMP-A.8.20-22.S3 (Device Hardening)
- ISMS-IMP-A.8.20-22.S4 (Services Security)
- ISMS-IMP-A.8.20-22.S5 (Segmentation Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a820_1_infrastructure_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.20-22.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Evidence Register |
| 2 | Approval Sign-Off |
| 3 | Instructions & Legend |
| 4 | Device Inventory |
| 5 | Device Criticality Matrix |
| 6 | Device Type Summary |
| 7 | Discovery Metadata |
| 8 | Gap Analysis |
| 9 | Summary Dashboard |
| 10 | Validation Rules |

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
| 1 | Assessment Area |
| 2 | Total |
| 3 | Yes |
| 4 | Partial |
| 5 | N-A |
| 6 | Compliance % |
| 7 | IT Infrastructure Team |
| 8 | Network Scan |
| 9 | DEVICE CRITICALITY ASSESSMENT MATRIX |
| 10 | DEVICE TYPE SUMMARY & STATISTICS |
| 11 | NETWORK DISCOVERY PROCESS METADATA |
| 12 | NETWORK DISCOVERY GAP ANALYSIS |
| 13 | Missing Device |
| 14 | Network Team |
| 15 | What This Shows |
| 16 | Critical Finding Type |
| 17 | Filter Instructions |
| 18 | DATA VALIDATION RULES & QUALITY CHECKS |
| 19 | Device ID |
| 20 | Device Type |
| 21 | Make/Model |
| 22 | Hostname |
| 23 | Primary IP |
| 24 | Management IP |
| 25 | Location |
| 26 | Security Zone |
| 27 | Purpose |
| 28 | Criticality |
| 29 | Owner |
| 30 | Last Discovered |
| 31 | Discovery Method |
| 32 | Firmware Version |
| 33 | Serial Number |
| 34 | Compliance Status |
| 35 | Status |
| 36 | Notes |
| 37 | Service Impact |
| 38 | Recovery Time |
| 39 | User Impact |
| 40 | Revenue Impact |
| 41 | Redundancy |
| 42 | Total Count |
| 43 | Active |
| 44 | Offline |
| 45 | Critical Count |
| 46 | Compliant Count |
| 47 | Gap ID |
| 48 | Gap Type |
| 49 | Device/Location |
| 50 | Description |
| 51 | Severity |
| 52 | Impact |
| 53 | Remediation Plan |
| 54 | Target Date |
| 55 | Evidence ID |
| 56 | Evidence Type |
| 57 | Location/Path |
| 58 | Date Collected |
| 59 | Collected By |
| 60 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Router, Switch, Firewall, Wireless AP, Load Balancer, VPN Concentrator
IDS/IPS, Network Management, Other, Critical, High, Medium, Low, Active
Offline, Decommissioned, Planned, Internet/DMZ, Internal, Management, Guest
Datacenter, Branch, Cloud, Unknown, Nmap Scan, SNMP Walk, Cloud API
Manual Entry, Documentation Review, Compliant, Non-Compliant, ⚠️ Partial
❓ Not Assessed, ⭕ Open, In Progress, Resolved, ⚠️ Accepted Risk
Configuration Backup, Discovery Report, Network Diagram, Scan Results
Documentation, Screenshot, Collected, Pending, Missing, Not Applicable
Configuration file, Network scan, Vendor spec, Certificate inventory
Audit log, Compliance report, ✅ Verified, ⚠️ Pending, ❌ Not Verified, N/A
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 60 columns, 66 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"The idea behind digital computers may be explained by saying that these machines are intended to carry out any operations which could be done by a human computer."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
