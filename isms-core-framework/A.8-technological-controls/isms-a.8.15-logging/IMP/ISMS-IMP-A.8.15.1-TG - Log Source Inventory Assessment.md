<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.1-TG:framework:TG:a.8.15.1 -->
**ISMS-IMP-A.8.15.1-TG - Log Source Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Log Source Inventory Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.15.1-TG |
| **Related Policy** | ISMS-POL-A.8.15 (Logging) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.15 (Logging) |
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

- ISMS-POL-A.8.15 (Logging)
- ISMS-IMP-A.8.15.2 (Log Collection & Centralization Assessment)
- ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)
- ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a815_1_log_source_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.15.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | System Inventory |
| 3 | Log Event Types by System |
| 4 | Authentication Logging |
| 5 | Authorisation & Access |
| 6 | Administrative Activity |
| 7 | Security Event Logging |
| 8 | Application & Database |
| 9 | Network Device Logging |
| 10 | Gap Analysis |
| 11 | Evidence Register |
| 12 | Summary Dashboard |
| 13 | Approval Sign-Off |

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
| 1 | System ID |
| 2 | System Name |
| 3 | System Type |
| 4 | Operating System / Platform |
| 5 | Environment |
| 6 | Data Classification |
| 7 | Business Criticality |
| 8 | Regulatory Scope |
| 9 | Logging Priority |
| 10 | System Owner |
| 11 | Owner Email |
| 12 | Hostname / FQDN |
| 13 | Primary IP |
| 14 | Location |
| 15 | Logging Enabled |
| 16 | Forwarding to SIEM |
| 17 | Compliance Status |
| 18 | Authentication Events |
| 19 | Authorisation Events |
| 20 | Administrative Actions |
| 21 | Security Events |
| 22 | Application Events |
| 23 | System Events |
| 24 | Network Events |
| 25 | Database Events |
| 26 | Log Format |
| 27 | Timestamp Format |
| 28 | Timezone |
| 29 | Est. Daily Volume (MB) |
| 30 | Retention Period (months) |
| 31 | Storage Tier |
| 32 | Protection Mechanisms |
| 33 | Event Types Completeness |
| 34 | Notes |
| 35 | Logs Successful Logins |
| 36 | Logs Failed Logins |
| 37 | Logs Account Lockouts |
| 38 | Logs Password Changes |
| 39 | Logs Session Start/End |
| 40 | Includes User ID |
| 41 | Includes Timestamp |
| 42 | Includes Source IP |
| 43 | Includes Auth Method |
| 44 | MFA Events Logged |
| 45 | SSO Events Logged |
| 46 | Service Account Auth |
| 47 | Privileged Auth Logged |
| 48 | Compliance Score |
| 49 | Gap Description |
| 50 | Remediation Plan |
| 51 | Logs Access Grants |
| 52 | Logs Access Denials |
| 53 | Logs Permission Changes |
| 54 | Logs Privilege Escalation |
| 55 | Logs Data Access (Sensitive) |
| 56 | Includes Resource Accessed |
| 57 | Includes Action Type |
| 58 | Includes Outcome |
| 59 | Includes Reason (denied) |
| 60 | Includes Before/After State |
| 61 | Logs Group Membership |
| 62 | Logs Role Assignment |
| 63 | User Account Management |
| 64 | Group/Role Management |
| 65 | Configuration Changes |
| 66 | Security Policy Changes |
| 67 | Software Install/Uninstall |
| 68 | Service Start/Stop |
| 69 | Patch Application |
| 70 | Bulk Data Operations |
| 71 | Privileged Session Logging |
| 72 | Includes Administrator ID |
| 73 | Includes Before/After Values |
| 74 | Includes Change Reason |
| 75 | Firewall Events |
| 76 | IDS/IPS Alerts |
| 77 | Anti-malware Events |
| 78 | DLP Events |
| 79 | Web Filtering Events |
| 80 | Email Gateway Events |
| 81 | EDR Events |
| 82 | Vulnerability Scan Results |
| 83 | Security Incident Events |
| 84 | Includes Severity Level |
| 85 | Includes Threat Indicators |
| 86 | Includes Response Actions |
| 87 | Automated Response Logged |
| 88 | Web App Access Logging |
| 89 | API Call Logging |
| 90 | Transaction Logging |
| 91 | Application Errors |
| 92 | Database Connections |
| 93 | Database Queries (Sensitive) |
| 94 | Schema Changes (DDL) |
| 95 | Permission Grants |
| 96 | Backup/Restore Operations |
| 97 | Includes User/App Identity |
| 98 | Includes Data Modified |
| 99 | Includes Query Text |
| 100 | Includes Row Count |
| 101 | Device ID |
| 102 | Device Name |
| 103 | Connection Logging |
| 104 | Rule Match Logging |
| 105 | Interface Up/Down Events |
| 106 | Routing Changes |
| 107 | VPN Session Logging |
| 108 | DHCP/DNS Events |
| 109 | Wireless Events |
| 110 | NAT Translations |
| 111 | Includes Source/Dest IP |
| 112 | Includes Ports/Protocols |
| 113 | Includes Action (allow/deny) |
| 114 | Includes Bytes Transferred |
| 115 | Gap ID |
| 116 | Gap Category |
| 117 | Policy Requirement |
| 118 | Impact / Risk |
| 119 | Remediation Action |
| 120 | Responsible Party |
| 121 | Target Date |
| 122 | Status |
| 123 | Evidence ID |
| 124 | Assessment Area |
| 125 | Evidence Type |
| 126 | Description |
| 127 | Location/Path |
| 128 | Date Collected |
| 129 | Collected By |
| 130 | Verification Status |
| 131 | Total Items |
| 132 | Compliant |
| 133 | Partial |
| 134 | Non-Compliant |
| 135 | N/A |
| 136 | Compliance % |
| 137 | Metric |
| 138 | Value |
| 139 | Target |
| 140 | Finding Type |
| 141 | Risk Level |
| 142 | Associated Sheet |
| 143 | Recommended Action |
| 144 | ISO Clause |

### Data Validation Values

All dropdown/list values used across sheets:

```
Server, Network Device, Security Appliance, Application, Cloud Service
Database, Other, Windows, Linux, Unix, Network OS, Cloud, Application Platform
Production, Staging, Development, Test, Public, Internal, Confidential
Restricted, Critical (T1), High (T2), Medium (T3), Low (T4), P1-Critical
P2-High, P3-Medium, P4-Low, \u2705 Yes, \u274C No, \u26A0\uFE0F Partial
\u2753 Unknown, \u231B Planned, \u2796 N/A, Syslog, CEF, JSON, EVTX, Custom
Unknown, ISO 8601, RFC 3339, Unix Epoch, UTC, Local, Hot, Warm, Cold
Log Source Missing, Event Type Not Logged, Incomplete Fields
Format Non-Standard, Protection Inadequate, Critical, High, Medium, Low
\u274C Open, \u231B In Progress, \u2705 Resolved, \u2B55 Deferred, Log sample
Configuration file, Screenshot, SIEM query result, Documentation
Policy document, Audit log, Compliance report, Verified, Pending verification
Not verified, Requires update, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 13 sheets, 144 columns, 82 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Once you stop learning, you start dying."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
