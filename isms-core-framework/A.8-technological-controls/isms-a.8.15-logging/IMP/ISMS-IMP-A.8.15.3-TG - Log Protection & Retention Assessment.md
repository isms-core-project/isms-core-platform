<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.3-TG:framework:TG:a.8.15.3 -->
**ISMS-IMP-A.8.15.3-TG - Log Protection & Retention Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Log Protection & Retention Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.15.3-TG |
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
- ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment)
- ISMS-IMP-A.8.15.2 (Log Collection & Centralization Assessment)
- ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a815_3_log_protection_retention.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.15.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Access Control Assessment |
| 3 | Integrity Protection |
| 4 | Secure Transmission |
| 5 | Retention Period Compliance |
| 6 | Storage Tier Implementation |
| 7 | Log Backup & Recovery |
| 8 | Disposal Procedures |
| 9 | Separation of Duties |
| 10 | Legal Hold Management |
| 11 | Privacy Impact Assessment |
| 12 | Gap Analysis |
| 13 | Evidence Register |
| 14 | Summary Dashboard |
| 15 | Approval Sign-Off |

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
| 1 | Log Source / SIEM Component |
| 2 | Access Control Type |
| 3 | Authentication Required |
| 4 | Authorisation Model |
| 5 | Read Access Controlled |
| 6 | Write Access Prevented |
| 7 | Delete Access Controlled |
| 8 | Admin Separation |
| 9 | Access Logged (Meta) |
| 10 | MFA Required for Admin |
| 11 | Last Access Review |
| 12 | Review Frequency |
| 13 | Non-Compliance Issues |
| 14 | Compliance Score |
| 15 | Remediation Required |
| 16 | Notes |
| 17 | Log Source / Storage |
| 18 | Log Criticality |
| 19 | Write-Once Storage (WORM) |
| 20 | WORM Technology |
| 21 | Cryptographic Hashing |
| 22 | Hash Algorithm |
| 23 | Hash Storage Location |
| 24 | Digital Signatures |
| 25 | File Sealing |
| 26 | Integrity Check Frequency |
| 27 | Last Integrity Check |
| 28 | Tampering Detected |
| 29 | Backup Protected |
| 30 | Compliance with Policy |
| 31 | Gap Description |
| 32 | Remediation Plan |
| 33 | Source System |
| 34 | Destination (SIEM) |
| 35 | Transport Protocol |
| 36 | Encryption in Transit |
| 37 | TLS Version |
| 38 | Certificate Validation |
| 39 | Network Segment |
| 40 | Firewall Protection |
| 41 | Source Authentication |
| 42 | Vulnerability Risk |
| 43 | Compliance Status |
| 44 | Target Date |
| 45 | Log Source / Type |
| 46 | Log Category |
| 47 | Regulatory Requirement |
| 48 | Policy Retention (months) |
| 49 | Hot Storage Period (months) |
| 50 | Warm Storage Period (months) |
| 51 | Cold Storage Period (years) |
| 52 | Total Retention (months) |
| 53 | Meets Policy Requirement |
| 54 | Retention Gap (months) |
| 55 | Over-Retention (months) |
| 56 | Automated Disposal |
| 57 | Last Disposal Date |
| 58 | Legal Hold Capability |
| 59 | Remediation Action |
| 60 | Storage Tier |
| 61 | Technology |
| 62 | Capacity (TB) |
| 63 | Used (TB) |
| 64 | % Used |
| 65 | Retention Period |
| 66 | Access Performance |
| 67 | Encryption at Rest |
| 68 | Encryption Method |
| 69 | Geographic Location |
| 70 | Redundancy |
| 71 | Backup Implemented |
| 72 | Meets Policy Requirements |
| 73 | Issues |
| 74 | Backup Scope |
| 75 | Backup Frequency |
| 76 | Backup Technology |
| 77 | Backup Location |
| 78 | Backup Encrypted |
| 79 | Encryption Algorithm |
| 80 | Backup Integrity Verified |
| 81 | Last Backup Date |
| 82 | Last Restore Test Date |
| 83 | Restore Test Frequency |
| 84 | Last Restore Success |
| 85 | RTO (Recovery Time) |
| 86 | RPO (Recovery Point) |
| 87 | Backup Retention Period |
| 88 | Log Type / Source |
| 89 | Retention Period Expired |
| 90 | Disposal Method |
| 91 | Disposal Approval Required |
| 92 | Legal Hold Check |
| 93 | Disposal Logged |
| 94 | Volume Disposed (GB) |
| 95 | Disposal Verification |
| 96 | Remediation |
| 97 | System / Component |
| 98 | System Administrator(s) |
| 99 | Log Administrator(s) |
| 100 | Roles Separated |
| 101 | Sys Admin Can Modify Logs |
| 102 | Compensating Controls |
| 103 | Break-Glass Procedure |
| 104 | Break-Glass Usage Logged |
| 105 | Independent Review |
| 106 | Last Review Date |
| 107 | Violations Detected |
| 108 | Hold ID |
| 109 | Hold Name / Matter |
| 110 | Initiation Date |
| 111 | Initiated By |
| 112 | Scope Description |
| 113 | Systems/Sources Affected |
| 114 | Date Range |
| 115 | Hold Status |
| 116 | Review Date |
| 117 | Disposal Prevented |
| 118 | Release Date |
| 119 | Release Authorised By |
| 120 | Gap ID |
| 121 | Gap Category |
| 122 | Description |
| 123 | Affected Systems |
| 124 | Policy Requirement |
| 125 | Risk Level |
| 126 | Owner |
| 127 | Budget Required |
| 128 | Status |
| 129 | Evidence ID |
| 130 | Assessment Area |
| 131 | Evidence Type |
| 132 | Location/Path |
| 133 | Date Collected |
| 134 | Collected By |
| 135 | Verification Status |
| 136 | Minimum Retention |
| 137 | Regulatory Notes |
| 138 | PII/Sensitive Data Present |
| 139 | Data Types |
| 140 | Minimization Applied |
| 141 | Justification |
| 142 | GDPR Article |
| 143 | Data Type |
| 144 | Logs Checked |
| 145 | Found? |
| 146 | Location |
| 147 | Completion Date |
| 148 | Verified By |
| 149 | Right |
| 150 | Applicable to Logs? |
| 151 | Process Documented |
| 152 | Can Be Fulfilled |
| 153 | Response Time |
| 154 | Evidence Ref |
| 155 | Total Items |
| 156 | Compliant |
| 157 | Partial |
| 158 | Non-Compliant |
| 159 | N/A |
| 160 | Compliance % |
| 161 | Metric |
| 162 | Value |
| 163 | Target |
| 164 | Finding Type |
| 165 | Associated Sheet |
| 166 | Recommended Action |
| 167 | ISO Clause |

### Data Validation Values

All dropdown/list values used across sheets:

```
RBAC, ACL, None, Other, Yes, No, Role-Based, User-Based, Group-Based, Partial
Yes (read-only), Yes (restricted), Yes (separated), N/A, \u2705 Yes, \u274C No
\u2796 N/A, Quarterly, Semi-annual, Annual, Critical, High, Medium, Low
Hardware WORM, Software WORM, Cloud Object Lock, SHA-256, SHA-512, SHA-3
MD5 (weak), Daily, Weekly, Monthly, Never, Historical, Recent, TLS, TCP, UDP
HTTPS, Yes (TLS), TLS 1.3, TLS 1.2, TLS 1.1 (weak), TLS 1.0 (weak)
Isolated Mgmt Network, Internal Network, Internet, DMZ, Yes (mutual TLS/certs)
Security, Authentication, Admin, Application, System, Network, Database
PCI DSS v4.0.1, HIPAA, SOX, GDPR, FADP, ISO 27001, Hot, Warm, Cold
Local Disk/SSD, SAN, NAS, Object Storage, Tape, Real-time (<1 min)
Fast (<15 min), Slow (hours), Very Slow (days), AES-256, AES-128, Local (RAID)
Remote (Replication), Both, All Logs, Hot Storage Only, Critical Logs Only
Same Site, Offsite, Cloud, Multiple, Yes (periodic), Yes (always)
Cryptographic Erasure, Multi-pass Overwrite, Physical Destruction, Deletion
Yes (manual), No (automated), Yes (checked), Verified, Not Verified
Yes (different people), No (same people), No (compliant), Yes (violation)
Limited, Yes (documented), Active, Released, Suspended, Yes (verified)
Access Control, Integrity Protection, Transmission Security
Retention Non-Compliance, Backup, Disposal, Separation of Duties, Open
In Progress, Resolved, Deferred, Configuration file, Screenshot
Policy document, Audit log, Access control report, Retention schedule
Disposal certificate, Compliance report, Pending verification, Requires update
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected
```

**Extracted:** 15 sheets, 167 columns, 137 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Information is not knowledge. The only source of knowledge is experience."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
