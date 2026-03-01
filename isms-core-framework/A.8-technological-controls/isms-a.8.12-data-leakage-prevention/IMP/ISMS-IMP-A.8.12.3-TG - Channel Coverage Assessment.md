<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.12.3-TG:framework:TG:a.8.12.3 -->
**ISMS-IMP-A.8.12.3-TG - Channel Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Channel Coverage Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.12.3-TG |
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
- ISMS-IMP-A.8.12.1 (DLP Infrastructure Assessment)
- ISMS-IMP-A.8.12.2 (Data Classification Assessment)
- ISMS-IMP-A.8.12.4 (Monitoring & Response Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a812_3_channel_coverage.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.12.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Channel Overview |
| 3 | Email Channel |
| 4 | Web Cloud Channel |
| 5 | Endpoint Channel |
| 6 | Network Channel |
| 7 | Application Channel |
| 8 | Mobile Channel |
| 9 | Coverage Metrics |
| 10 | Gap Analysis |
| 11 | Evidence Register |
| 12 | Summary Dashboard |
| 13 | Approval Sign-Off |

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
| 1 | Channel Name |
| 2 | Priority Tier |
| 3 | DLP Deployed? |
| 4 | Coverage % |
| 5 | Users Protected |
| 6 | Total Users |
| 7 | Policy Action |
| 8 | Gap Status |
| 9 | Evidence ID |
| 10 | Email System |
| 11 | System Type |
| 12 | DLP Solution |
| 13 | Deployment Mode |
| 14 | Content Inspection |
| 15 | Attachment Scanning |
| 16 | Encrypted Email Handling |
| 17 | External Email Protected |
| 18 | Users Covered |
| 19 | SIEM Integration |
| 20 | Service/Application |
| 21 | Service Type |
| 22 | Protection Method |
| 23 | SSL/TLS Inspection |
| 24 | Upload Blocking |
| 25 | Download Monitoring |
| 26 | Endpoint Type |
| 27 | OS Version |
| 28 | DLP Agent Installed |
| 29 | USB Control |
| 30 | Print Control |
| 31 | Clipboard Control |
| 32 | Screen Capture Control |
| 33 | Bluetooth Control |
| 34 | Application Control |
| 35 | Devices Covered |
| 36 | Total Devices |
| 37 | Protocol |
| 38 | Business Use Case |
| 39 | Detection Method |
| 40 | Encryption Handling |
| 41 | Application Name |
| 42 | Application Type |
| 43 | Data Export Capability |
| 44 | DLP Control Method |
| 45 | Bulk Export Detection |
| 46 | Export Policy Action |
| 47 | Audit Logging |
| 48 | Device Ownership |
| 49 | Mobile Platform |
| 50 | MDM/MAM Solution |
| 51 | Work Profile Enabled |
| 52 | Copy-Paste Control |
| 53 | Screenshot Control |
| 54 | Camera Access Control |
| 55 | Personal Cloud Block |
| 56 | AirDrop/NFC Control |
| 57 | Devices Enrolled |
| 58 | Total Mobile Devices |
| 59 | Gap ID |
| 60 | Channel |
| 61 | Gap Description |
| 62 | Risk Level |
| 63 | Exfiltration Risk |
| 64 | Current Coverage % |
| 65 | Target Coverage % |
| 66 | Remediation Plan |
| 67 | Owner |
| 68 | Target Date |
| 69 | Status |
| 70 | Assessment Area |
| 71 | Evidence Type |
| 72 | Description |
| 73 | Location/Path |
| 74 | Date Collected |
| 75 | Collected By |
| 76 | Verification Status |
| 77 | Total Items |
| 78 | Compliant |
| 79 | Partial |
| 80 | Non-Compliant |
| 81 | N/A |
| 82 | Compliance % |
| 83 | Metric |
| 84 | Value |
| 85 | Target |
| 86 | Finding |
| 87 | Impact |
| 88 | Recommendation |
| 89 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Planned, N/A, Email, Web, Endpoint, Network, App, Mobile
Critical, High, Medium, Low, Very High, Very Low, Not Started, In Progress
Complete, Blocked, Approved, Pending, Rejected, SMTP, M365, Gmail, Webmail
Other, Inline, Monitor, Cloud-Native, CASB, Allow, Alert, Block, Quarantine
Encrypt, Decrypt, Cloud Storage, SaaS, Web Upload, Code Repo, Social Media
Proxy, Windows Desktop, macOS, Linux, VDI, Thin Client, Block All
Allow Approved, None, Watermark, Whitelist, Blacklist, SMB/CIFS, FTP, SFTP
NFS, SCP, WebDAV, Rsync, TAP, SPAN, Database, API, Reporting, CRM, ERP, BI
Limited, DAM, API Gateway, App Control, Approval Required, Corporate, BYOD
iOS, Android, Windows Mobile, Config, Screenshot, Log, Report, Policy
Verified, Configuration file, Network scan, Documentation, Vendor spec
Certificate inventory, Audit log, Compliance report, Pending verification
Not verified, Requires update, Draft, Final, Requires remediation
Re-assessment required, Approved with Conditions, Deferred
```

**Extracted:** 13 sheets, 89 columns, 103 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Life is like riding a bicycle. To keep your balance, you must keep moving."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
