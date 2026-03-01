<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S4-TG:framework:TG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S4-TG - Network Services Security Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Services Security |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-21-22.S4-TG |
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
- ISMS-IMP-A.8.20-21-22.S3 (Device Hardening)
- ISMS-IMP-A.8.20-21-22.S5 (Segmentation Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a820_4_segmentation_matrix.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.20-21-22.S4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Evidence Register |
| 2 | Approval Sign-Off |
| 3 | Instructions & Legend |
| 4 | Security Zones Inventory |
| 5 | Segmentation Matrix |
| 6 | VLAN Inventory |
| 7 | Firewall Rules Assessment |
| 8 | ACL Assessment |
| 9 | Segmentation Testing |
| 10 | Gap Analysis |
| 11 | Summary Dashboard |
| 12 | Remediation Roadmap |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #4472C4 | Medium Blue (Sub-headers) |
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
| 7 | NETWORK SEGMENTATION MATRIX - ZONE-TO-ZONE TRAFFIC RULES |
| 8 | VLAN INVENTORY & DESIGN ASSESSMENT |
| 9 | FIREWALL RULES ASSESSMENT |
| 10 | TCP/80, TCP/443 |
| 11 | Network Security Team |
| 12 | SEGMENTATION EFFECTIVENESS TESTING |
| 13 | Internet DMZ to Corporate LAN |
| 14 | Internet DMZ |
| 15 | Corporate LAN |
| 16 | SEGMENTATION GAPS - REMEDIATION TRACKING |
| 17 | Flat Network |
| 18 | Network Architecture Team |
| 19 | What This Shows |
| 20 | Critical Finding Type |
| 21 | Filter Instructions |
| 22 | SEGMENTATION REMEDIATION ROADMAP |
| 23 | Zone ID |
| 24 | Zone Name |
| 25 | Purpose |
| 26 | Trust Level |
| 27 | Networks/Subnets |
| 28 | VLANs |
| 29 | Segmentation Type |
| 30 | Devices Count |
| 31 | Critical Assets |
| 32 | Internet Access |
| 33 | Owner |
| 34 | Notes |
| 35 | Rule ID |
| 36 | Source Zone |
| 37 | Destination Zone |
| 38 | Traffic Action |
| 39 | Protocols/Ports |
| 40 | Justification |
| 41 | Firewall Enforced |
| 42 | ACL Enforced |
| 43 | Monitoring |
| 44 | Last Reviewed |
| 45 | VLAN ID |
| 46 | VLAN Name |
| 47 | Security Zone |
| 48 | IP Subnet |
| 49 | Devices/Ports |
| 50 | Trunk Allowed |
| 51 | Native VLAN |
| 52 | Firewall |
| 53 | Rule Number |
| 54 | Source IP/Network |
| 55 | Destination IP/Network |
| 56 | Service/Port |
| 57 | Action |
| 58 | Review Status |
| 59 | Last Modified |
| 60 | Reviewed By |
| 61 | ACL ID |
| 62 | Device |
| 63 | ACL Name/Number |
| 64 | Interface |
| 65 | Direction |
| 66 | Zones Protected |
| 67 | Effectiveness |
| 68 | Test ID |
| 69 | Test Name |
| 70 | Expected Result |
| 71 | Actual Result |
| 72 | Test Result |
| 73 | Test Method |
| 74 | Test Date |
| 75 | Tested By |
| 76 | Gap ID |
| 77 | Gap Type |
| 78 | Location/Zone |
| 79 | Description |
| 80 | Risk |
| 81 | Severity |
| 82 | Remediation Plan |
| 83 | Status |
| 84 | Target Date |
| 85 | Priority |
| 86 | Improvement |
| 87 | Affected Zones |
| 88 | Remediation Action |
| 89 | Evidence ID |
| 90 | Evidence Type |
| 91 | Location/Path |
| 92 | Date Collected |
| 93 | Collected By |
| 94 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Untrusted, Low Trust, Medium Trust, High Trust, Trusted, Allow, Deny, Inspect
VLAN, Physical, VRF, Virtual Network, Cloud Security Group, Drop, Reject
Current, Outdated, Unused, Requires Review, Pass, Fail, Partial, Not Tested
Critical, High, Medium, Low, Open, In Progress, Resolved, Accepted Risk
Configuration file, Screenshot, Network scan, Documentation, Vendor spec
Certificate inventory, Audit log, Compliance report, Other, ✅ Verified
⚠️ Pending, ❌ Not Verified, N/A, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 94 columns, 52 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"People are always selling the idea that people with mental illness are suffering. I think madness can be an escape."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
