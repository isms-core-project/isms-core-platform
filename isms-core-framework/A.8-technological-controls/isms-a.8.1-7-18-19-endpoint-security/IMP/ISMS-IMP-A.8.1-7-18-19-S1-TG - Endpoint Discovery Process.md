<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.1-7-18-19-S1-TG:framework:TG:a.8.1-7-18-19-s1 -->
**ISMS-IMP-A.8.1-7-18-19-S1-TG - Endpoint Discovery Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Endpoint Discovery Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S1-TG |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19-S1 (Endpoint Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.1 (User Endpoint Devices) |
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

- ISMS-POL-A.8.1-7-18-19-S1 (Endpoint Security)
- ISMS-IMP-A.8.1-7-18-19-S2 (Malware Protection Deployment)
- ISMS-IMP-A.8.1-7-18-19-S3 (Software Control Process)
- ISMS-IMP-A.8.1-7-18-19-S4 (Privileged Utility Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a81-7-18-19_1_endpoint_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.1-7-18-19.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Inventory |
| 3 | Baseline Compliance |
| 4 | Encryption Status |
| 5 | Management Enrollment |
| 6 | Capability Requirements |
| 7 | Gap Analysis |
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
| 1 | ENDPOINT DEVICE GROUP INVENTORY |
| 2 | Total Device Groups: |
| 3 | ENDPOINT BASELINE COMPLIANCE ASSESSMENT |
| 4 | Compliance Rate: |
| 5 | ENDPOINT ENCRYPTION STATUS |
| 6 | Encryption Coverage Rate: |
| 7 | ENDPOINT MANAGEMENT ENROLLMENT |
| 8 | Enrollment Rate: |
| 9 | By MDM Platform: |
| 10 | Microsoft Intune: |
| 11 | Jamf Pro: |
| 12 | CAPABILITY REQUIREMENTS MAPPING |
| 13 | Total Requirements: |
| 14 | Not Implemented: |
| 15 | Total Critical/High Findings: |
| 16 | EVIDENCE REGISTER |
| 17 | Total Evidence Entries: |
| 18 | GAP ANALYSIS & REMEDIATION TRACKING |
| 19 | In Progress: |
| 20 | Group ID |
| 21 | Device Group Name |
| 22 | Group Type |
| 23 | Device Type |
| 24 | OS Platform |
| 25 | Device Count |
| 26 | Department |
| 27 | Ownership Model |
| 28 | Location |
| 29 | Management Platform |
| 30 | Compliance Status |
| 31 | Last Assessed |
| 32 | Criticality |
| 33 | Notes |
| 34 | OS Hardening |
| 35 | Firewall Status |
| 36 | Antivirus / EDR |
| 37 | Screen Lock |
| 38 | Patch Compliance |
| 39 | Password Policy |
| 40 | Baseline Profile |
| 41 | Device ID |
| 42 | Hostname |
| 43 | Encryption Technology |
| 44 | Encryption Status |
| 45 | Full Disk Encryption |
| 46 | Key Escrow/Recovery |
| 47 | Recovery Key Location |
| 48 | Last Verified Date |
| 49 | MDM Platform |
| 50 | Enrollment Status |
| 51 | Remote Wipe Capable |
| 52 | Policy Enforcement |
| 53 | Compliance Policy Applied |
| 54 | Last Check-In |
| 55 | MDM Compliance Status |
| 56 | Req ID |
| 57 | Policy Requirement |
| 58 | Implemented |
| 59 | Evidence Reference |
| 60 | Status |
| 61 | Assessment Area |
| 62 | Total Items |
| 63 | Compliant |
| 64 | Partial |
| 65 | Non-Compliant |
| 66 | N/A |
| 67 | Compliance % |
| 68 | KPI |
| 69 | Current Value |
| 70 | Target |
| 71 | Last Updated |
| 72 | Owner |
| 73 | Finding ID |
| 74 | Description |
| 75 | Affected Area |
| 76 | Severity |
| 77 | Due Date |
| 78 | Evidence ID |
| 79 | Evidence Type |
| 80 | Related Requirement |
| 81 | Related Worksheet/Device |
| 82 | File Location |
| 83 | Collection Date |
| 84 | Collected By |
| 85 | Gap ID |
| 86 | Gap Description |
| 87 | Affected Devices/Count |
| 88 | Risk |
| 89 | Root Cause |
| 90 | Remediation Plan |
| 91 | Budget Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Unknown, Compliant, Partial, Non-Compliant, Laptop, Desktop
Mobile (iOS), Mobile (Android), Tablet, Workstation, Other, Windows 11
Windows 10, macOS 14 (Sonoma), macOS 13 (Ventura), iOS 17, iOS 16, Android 14
Android 13, Linux (Ubuntu), Linux (RHEL/CentOS), Corporate-Owned, BYOD
Contractor, Shared Device, Critical, High, Medium, Low, Encrypted
Not Encrypted, BitLocker, FileVault, LUKS, Built-in (iOS/Android), Third-Party
None, Microsoft Intune, Jamf Pro, SCCM, VMware Workspace ONE, MobileIron
Citrix Endpoint Management, Kandji, Google Workspace, Enrolled, Not Enrolled
Pending, Remediation in Progress, Enabled, Disabled, Active, Outdated
Not Installed, Inactive, Office, Remote, Mobile, International, Retired
Storage, Pending Setup, Lost/Stolen, Open, In Progress, Resolved, Closed
On Hold, Config Export, Screenshot, Report, Certificate, Policy, Log File
Encryption Key Backup, Verified, Not Verified, Needs Review, Approved
Approved with Conditions, Rejected, Pending Review, AD OU, Entra ID Group
Department Group, Location Group, Windows, macOS, Linux, iOS, Android, Mixed
Azure AD, On-premise AD, HashiCorp Vault, Manual, Draft, Final
Requires remediation, Re-assessment required, Deferred
```

**Extracted:** 10 sheets, 91 columns, 104 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Access to the Vedas is the greatest privilege this century may claim over all previous centuries."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
