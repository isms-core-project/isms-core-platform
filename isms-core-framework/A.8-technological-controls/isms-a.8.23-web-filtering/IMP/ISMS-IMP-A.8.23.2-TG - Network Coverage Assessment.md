<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.23.2-TG:framework:TG:a.8.23.2 -->
**ISMS-IMP-A.8.23.2-TG - Network Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Network Coverage Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.23.2-TG |
| **Related Policy** | ISMS-POL-A.8.23 (Web Filtering) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.23 (Web Filtering) |
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

- ISMS-POL-A.8.23 (Web Filtering)
- ISMS-IMP-A.8.23.1 (Filtering Infrastructure Assessment)
- ISMS-IMP-A.8.23.3 (Policy Configuration Assessment)
- ISMS-IMP-A.8.23.4 (Monitoring & Response Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a823_2_network_coverage.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.23.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Network Segment Inventory |
| 3 | Coverage Matrix |
| 4 | Gap Analysis |
| 5 | Device Inventory |
| 6 | Exemption Register |
| 7 | Coverage Verification |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #0000FF | Custom |
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
| 1 | Segment ID |
| 2 | Segment Name |
| 3 | Segment Type |
| 4 | Location/Site |
| 5 | Subnet/VLAN |
| 6 | User Count |
| 7 | Device Count |
| 8 | Internet Access? |
| 9 | Filtering Required? |
| 10 | Filtering Status |
| 11 | Filtering Solution(s) |
| 12 | Coverage % |
| 13 | Bypass Methods |
| 14 | Exemption ID |
| 15 | Evidence |
| 16 | Device ID |
| 17 | Device Type |
| 18 | User/Owner |
| 19 | Primary Network |
| 20 | Filtering Solution |
| 21 | Agent-Based? |
| 22 | Status |
| 23 | Last Verified |
| 24 | Verification ID |
| 25 | Test Date |
| 26 | Tester |
| 27 | Test Method |
| 28 | Test Results |
| 29 | Issues Found |
| 30 | Next Test Date |
| 31 | Network Segment |
| 32 | Solution 1 |
| 33 | Solution 2 |
| 34 | Solution 3 |
| 35 | Solution 4 |
| 36 | Total Coverage |
| 37 | Gap ID |
| 38 | Current Coverage |
| 39 | Gap Description |
| 40 | Risk Level |
| 41 | Impact |
| 42 | Remediation Plan |
| 43 | Owner |
| 44 | Target Date |
| 45 | Segment/Device |
| 46 | Exemption Type |
| 47 | Business Justification |
| 48 | Risk Assessment |
| 49 | Compensating Controls |
| 50 | Approved By |
| 51 | Approval Date |
| 52 | Review Date |
| 53 | Evidence ID |
| 54 | Assessment Area |
| 55 | Evidence Type |
| 56 | Description |
| 57 | Location/Path |
| 58 | Date Collected |
| 59 | Collected By |
| 60 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Restricted, On-Premises LAN, WLAN, VPN, Cloud Endpoints, Guest
DMZ, Branch, Mobile, IoT/OT, Dev/Test, Other, \u2705 Protected
\u26A0\uFE0F Partial, \u274C Unprotected, \u27F3 Planned, \u2298 Exempt
Laptop, Desktop, Smartphone, Tablet, Virtual Desktop, Yes (endpoint agent)
No (network-based), Hybrid, Full Exemption, Partial Exemption
Temporary Exemption, Category Exemption, Technical Exemption, \u2705 Active
\u274c Expired, \u26d4 Revoked, \u23f3 Under Review, Manual Browse Test
Automated Scan, Curl/wget Test, Browser Extension, Vendor Tool
Penetration Test, Pass, Fail, Partial, Inconclusive, \u2705 Verified
\u274C Failed, \u26A0\uFE0F Needs Retest, Critical, High, Medium, Low, ○ Open
⟳ In Progress, ✅ Resolved, ⚠️ Accepted Risk, ⊘ Exempt, Network Diagram
VLAN Config, Firewall Policy, VPN Config, WiFi Config, Cloud Dashboard
NAC Policy, Exemption Approval, Test Results, Monitoring Report, Change Record
Verified, Pending, Not Verified, Draft, Final, Requires Remediation
Re-assessment Required, Approved, Approved with Conditions, Rejected, Approve
Approve with Conditions, Reject, Require Rework, Configuration file
Screenshot, Network scan, Documentation, '
                 'Vendor spec
Certificate inventory, Audit log, Compliance report, ✅ Verified, ⚠️ Pending
❌ Not Verified, Deferred
```

**Extracted:** 10 sheets, 60 columns, 96 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Rational behavior is just a small part of game theory. The interesting part is when people deviate from rationality."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
