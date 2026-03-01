<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.1-7-18-19-S3-TG:framework:TG:a.8.1-7-18-19-s3 -->
**ISMS-IMP-A.8.1-7-18-19-S3-TG - Software Control Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Software Control Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S3-TG |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19-S3 (Endpoint Security) |
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

- ISMS-POL-A.8.1-7-18-19-S3 (Endpoint Security)
- ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process)
- ISMS-IMP-A.8.1-7-18-19-S2 (Malware Protection Deployment)
- ISMS-IMP-A.8.1-7-18-19-S4 (Privileged Utility Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a81-7-18-19_3_software_controls.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.1-7-18-19.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Approved Software |
| 3 | Software Inventory |
| 4 | Unauthorised Software |
| 5 | Application Control |
| 6 | Change Control |
| 7 | Vulnerability Management |
| 8 | Licensing Compliance |
| 9 | Capability Requirements |
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
| 1 | APPROVED SOFTWARE CATALOG |
| 2 | Total Approved Software: |
| 3 | Last List Review Date: |
| 4 | By Category: |
| 5 | INSTALLED SOFTWARE INVENTORY |
| 6 | Total Software Entries: |
| 7 | Unique Software Titles: |
| 8 | Unique Groups: |
| 9 | UNAUTHORIZED SOFTWARE DETECTION & REMEDIATION |
| 10 | Total Unauthorised Detections: |
| 11 | Remediation Rate: |
| 12 | By Risk Level: |
| 13 | APPLICATION CONTROL DEPLOYMENT |
| 14 | Total Endpoints Assessed: |
| 15 | Deployment Rate: |
| 16 | SOFTWARE INSTALLATION CHANGE CONTROL |
| 17 | Total Changes: |
| 18 | Testing Compliance: |
| 19 | SOFTWARE VULNERABILITY & PATCH MANAGEMENT |
| 20 | Total Vulnerabilities: |
| 21 | SLA Compliance Rate: |
| 22 | SOFTWARE LICENSING COMPLIANCE |
| 23 | Total Software Tracked: |
| 24 | Total Annual Cost: |
| 25 | CAPABILITY REQUIREMENTS MAPPING |
| 26 | EVIDENCE REGISTER |
| 27 | Total Evidence Entries: |
| 28 | GAP ANALYSIS & REMEDIATION TRACKING |
| 29 | TOTAL Critical/High Findings: |
| 30 | Software ID |
| 31 | Software Name |
| 32 | Vendor |
| 33 | Version |
| 34 | Category |
| 35 | Type |
| 36 | Business Justification |
| 37 | Approval Date |
| 38 | Approved By |
| 39 | Review Date |
| 40 | Risk Level |
| 41 | Deployment Method |
| 42 | Notes |
| 43 | Group ID |
| 44 | Device Group Name |
| 45 | Installation Date |
| 46 | Installation Method |
| 47 | Approved |
| 48 | Approval Reference |
| 49 | Detection ID |
| 50 | Detection Date |
| 51 | Device ID |
| 52 | Hostname |
| 53 | Risk Assessment |
| 54 | Remediation Action |
| 55 | Remediation Date |
| 56 | Remediation Status |
| 57 | Device Type |
| 58 | Control Technology |
| 59 | Policy Name |
| 60 | Enforcement Mode |
| 61 | Last Policy Update |
| 62 | Blocked Executions (30d) |
| 63 | Status |
| 64 | Change ID |
| 65 | Change Date |
| 66 | Affected Devices |
| 67 | Change Type |
| 68 | Testing Completed |
| 69 | Rollback Plan |
| 70 | Implementer |
| 71 | Change Status |
| 72 | Vulnerability ID |
| 73 | Version Affected |
| 74 | CVE ID |
| 75 | Severity |
| 76 | Discovery Date |
| 77 | Patch Available |
| 78 | Patch Status |
| 79 | Patch Date |
| 80 | SLA Compliance |
| 81 | License Type |
| 82 | Licenses Purchased |
| 83 | Licenses Deployed |
| 84 | Licenses Available |
| 85 | Compliance Status |
| 86 | Annual Cost |
| 87 | License Expiration |
| 88 | Req ID |
| 89 | Policy Requirement |
| 90 | Implemented |
| 91 | Evidence Reference |
| 92 | Evidence ID |
| 93 | Evidence Type |
| 94 | Description |
| 95 | Related Requirement |
| 96 | Related Worksheet/Device |
| 97 | File Location |
| 98 | Collection Date |
| 99 | Collected By |
| 100 | Gap ID |
| 101 | Gap Description |
| 102 | Affected Software/Devices |
| 103 | Risk |
| 104 | Root Cause |
| 105 | Remediation Plan |
| 106 | Owner |
| 107 | Due Date |
| 108 | Budget |
| 109 | Assessment Area |
| 110 | Total Items |
| 111 | Compliant |
| 112 | Partial |
| 113 | Non-Compliant |
| 114 | N/A |
| 115 | Compliance % |
| 116 | KPI |
| 117 | Current Value |
| 118 | Target |
| 119 | Last Updated |
| 120 | Finding ID |
| 121 | Affected Area |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, [BIZ] Business Application, [TOOL] Development Tool
Security Software, Analytics/BI, [CHAT] Communication, [CLOUD] Cloud Service
STATUS LEGEND Creative/Design, [DB] Database, Other, Desktop Application
Web Application, SaaS, Mobile App, Browser Extension, Command-Line Tool
Library/Framework, Plugin, SCCM/Intune, [WEB] Self-Service Portal
User Installation, [DISK] Manual Install, [CLOUD] Cloud Deployment, Critical
High, Medium, Low, Automatic, Weekly, Monthly, Quarterly, As Needed, Never
ℹ️ Informational, Commercial, Subscription, Open Source, Freeware, Trial
Custom, Unknown, Open, In Progress, Resolved, Closed, On Hold, Approval Record
Screenshot, Inventory Report, License, Policy, Change Ticket
\u1f50d Scan Result, Pending, Removed, Approved Retroactively, Unresolved
AppLocker, WDAC, Gatekeeper (macOS), Application Whitelist, None
New Installation, Upgrade, Patch, Removal, Configuration Change, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 13 sheets, 121 columns, 77 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"There are children playing in the streets who could solve some of my top problems in physics, because they have modes of sensory perception that I lost long ago."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
