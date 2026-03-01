<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.12.1-TG:framework:TG:a.8.12.1 -->
**ISMS-IMP-A.8.12.1-TG - DLP Infrastructure Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | DLP Infrastructure Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.12.1-TG |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.12 (Data Leakage Prevention) |
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

- ISMS-POL-A.8.12 (Data Leakage Prevention)
- ISMS-IMP-A.8.12.2 (Data Classification Assessment)
- ISMS-IMP-A.8.12.3 (Channel Coverage Assessment)
- ISMS-IMP-A.8.12.4 (Monitoring & Response Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a812_1_dlp_infrastructure.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.12.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | DLP Technology Inventory |
| 3 | Network DLP |
| 4 | Endpoint DLP |
| 5 | Email DLP |
| 6 | Cloud CASB DLP |
| 7 | Web DLP |
| 8 | Database DAM |
| 9 | Gap Analysis |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

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
| 1 | Technology ID |
| 2 | Technology Name |
| 3 | Deployment Type |
| 4 | Vendor |
| 5 | Version |
| 6 | Deployment Architecture |
| 7 | Deployment Status |
| 8 | License Type |
| 9 | License Expiry |
| 10 | Support Contract |
| 11 | EOL Date |
| 12 | Primary Use Case |
| 13 | Integration Status |
| 14 | SIEM Integration |
| 15 | SOC Integration |
| 16 | Evidence ID |
| 17 | Appliance Name |
| 18 | Deployment Mode |
| 19 | Network Segments Covered |
| 20 | Protocols Inspected |
| 21 | SSL/TLS Inspection |
| 22 | Throughput Capacity |
| 23 | Current Utilization % |
| 24 | Content Inspection |
| 25 | Pattern Matching (Regex) |
| 26 | Fingerprinting |
| 27 | Machine Learning/AI |
| 28 | Blocking Capability |
| 29 | High Availability |
| 30 | Operating System |
| 31 | OS Version |
| 32 | Agent Name |
| 33 | Agent Version |
| 34 | Deployment Method |
| 35 | Total Endpoints |
| 36 | Agents Deployed |
| 37 | Deployment Coverage % |
| 38 | USB Blocking |
| 39 | Clipboard Monitoring |
| 40 | Print Blocking |
| 41 | Screen Capture Detection |
| 42 | Bluetooth Blocking |
| 43 | Cloud Sync App Monitoring |
| 44 | Email System |
| 45 | DLP Solution |
| 46 | SMTP Gateway Protection |
| 47 | Webmail Protection |
| 48 | Attachment Scanning |
| 49 | Encrypted Email Handling |
| 50 | Internal Email Monitoring |
| 51 | External Email Monitoring |
| 52 | Quarantine Capability |
| 53 | Auto-Encryption |
| 54 | Cloud Service |
| 55 | CASB Solution |
| 56 | Integration Type |
| 57 | Upload Monitoring |
| 58 | Download Monitoring |
| 59 | Sharing Controls |
| 60 | Real-Time Blocking |
| 61 | Shadow IT Discovery |
| 62 | Proxy Solution |
| 63 | Proxy Type |
| 64 | SSL Inspection |
| 65 | HTTP/HTTPS Coverage |
| 66 | Cloud Storage Detection |
| 67 | Webmail Monitoring |
| 68 | URL Filtering Integration |
| 69 | Database System |
| 70 | DAM Solution |
| 71 | Monitoring Scope |
| 72 | SELECT Query Monitoring |
| 73 | Bulk Export Detection |
| 74 | Privileged User Monitoring |
| 75 | DLP Policy Integration |
| 76 | Alert Triggering |
| 77 | Gap ID |
| 78 | Gap Description |
| 79 | Affected Technology |
| 80 | Risk Level |
| 81 | Business Impact |
| 82 | Root Cause |
| 83 | Remediation Plan |
| 84 | Owner |
| 85 | Target Date |
| 86 | Status |
| 87 | Assessment Area |
| 88 | Evidence Type |
| 89 | Description |
| 90 | Location/Path |
| 91 | Date Collected |
| 92 | Collected By |
| 93 | Verification Status |
| 94 | Total Items |
| 95 | Compliant |
| 96 | Partial |
| 97 | Non-Compliant |
| 98 | N/A |
| 99 | Compliance % |
| 100 | Metric |
| 101 | Value |
| 102 | Target |
| 103 | Finding |
| 104 | Impact |
| 105 | Recommendation |
| 106 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Planned, N/A, Network, Endpoint, Cloud, Email, Web, Database
Inline, Monitor, Hybrid, Cloud-based, TAP, SPAN, Production, Staging, Test
Decommissioned, Perpetual, Subscription, Open Source, Active, Expired
Integrated, Standalone, Cloud Gateway, GPO, SCCM, Jamf, Manual, Cloud MDM
Ansible, Puppet, On-Premise, API, Log Analysis, Forward, Reverse, All, None
Critical, High, Medium, Low, Open, In Progress, Resolved, Accepted, Closed
Screenshot, Configuration File, Policy Document, Log Export, Report
Certificate, Meeting Minutes, Other, Verified, Pending, Rejected, Approved
Network scan, Documentation, Vendor spec, Certificate inventory, Audit log
Compliance report, Pending verification, Not verified, Requires update, Draft
Final, Requires remediation, Re-assessment required, Approved with Conditions
Deferred
```

**Extracted:** 12 sheets, 106 columns, 79 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"You cannot prevent what you cannot see."*
— Security monitoring principle

<!-- QA_VERIFIED: 2026-03-01 -->
