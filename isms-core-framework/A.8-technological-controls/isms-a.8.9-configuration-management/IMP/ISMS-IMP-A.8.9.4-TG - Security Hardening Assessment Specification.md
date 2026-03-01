<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.9.4-TG:framework:TG:a.8.9.4 -->
**ISMS-IMP-A.8.9.4-TG - Security Hardening Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Hardening Assessment Specification |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.9.4-TG |
| **Related Policy** | ISMS-POL-A.8.9 (Configuration Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.9 (Configuration Management) |
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

- ISMS-POL-A.8.9 (Configuration Management)
- ISMS-IMP-A.8.9.1 (Baseline Configuration Assessment Specification)
- ISMS-IMP-A.8.9.2 (Change Control Assessment Specification)
- ISMS-IMP-A.8.9.3 (Configuration Monitoring Assessment Specification)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a89_4_hardening.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.9.4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Hardening Standard Register |
| 2 | Asset Type Hardening Matrix |
| 3 | Asset Hardening Assessment |
| 4 | Control Compliance Detail |
| 5 | Exception Management |
| 6 | Remediation Tracking |
| 7 | Summary Dashboard |
| 8 | Gap Prioritization |
| 9 | Evidence Register |
| 10 | Approval Sign-Off |
| 11 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #0000FF | Custom |
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
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
| 1 | Critical |
| 2 | High |
| 3 | Medium |
| 4 | Low |
| 5 | Very High |
| 6 | Very Low |
| 7 | Not Started |
| 8 | Pending Review |
| 9 | Standard ID |
| 10 | Standard Name |
| 11 | Standard Category |
| 12 | Standard Version |
| 13 | Issuing Authority |
| 14 | Applicability Scope |
| 15 | Compliance Level |
| 16 | Mandatory Optional |
| 17 | Regulatory Driver |
| 18 | Control Count |
| 19 | Implementation Target |
| 20 | Review Frequency |
| 21 | Last Review Date |
| 22 | Next Review Date |
| 23 | Standard Owner |
| 24 | Documentation Location |
| 25 | Notes |
| 26 | Status |
| 27 | Required Standards Count |
| 28 | Recommended Standards Count |
| 29 | Total Applicable Standards |
| 30 | High Hardening Burden |
| 31 | Asset ID |
| 32 | Asset Name |
| 33 | Asset Type |
| 34 | Asset Tier |
| 35 | Asset Owner |
| 36 | Location |
| 37 | Operating System |
| 38 | Applicable Standards |
| 39 | Standards Count |
| 40 | Total Controls |
| 41 | Implemented Controls |
| 42 | Partial Controls |
| 43 | Not Implemented Controls |
| 44 | Not Applicable Controls |
| 45 | Compliance Percentage |
| 46 | High Risk Gaps |
| 47 | Medium Risk Gaps |
| 48 | Low Risk Gaps |
| 49 | Active Exceptions |
| 50 | Compensating Controls |
| 51 | Compliance Status |
| 52 | Last Assessment Date |
| 53 | Next Assessment Date |
| 54 | Assessor |
| 55 | Evidence Reference |
| 56 | Remediation Status |
| 57 | Target Compliance Date |
| 58 | Control ID |
| 59 | Control Number |
| 60 | Control Title |
| 61 | Control Description |
| 62 | Control Category |
| 63 | Control Severity |
| 64 | Implementation Status |
| 65 | Implementation Method |
| 66 | Implementation Evidence |
| 67 | Configuration Setting |
| 68 | Expected Value |
| 69 | Actual Value |
| 70 | Gap Description |
| 71 | Gap Risk Rating |
| 72 | Remediation Required |
| 73 | Remediation Plan |
| 74 | Remediation Owner |
| 75 | Target Remediation Date |
| 76 | Exception Status |
| 77 | Exception ID |
| 78 | Compensating Control |
| 79 | Last Verified Date |
| 80 | Verified By |
| 81 | Verification Method |
| 82 | Next Verification Date |
| 83 | Exception Type |
| 84 | Exception Reason |
| 85 | Business Justification |
| 86 | Risk Assessment |
| 87 | Residual Risk Rating |
| 88 | Compensating Control Required |
| 89 | Compensating Control Description |
| 90 | Compensating Control Effectiveness |
| 91 | Requested By |
| 92 | Request Date |
| 93 | Reviewed By |
| 94 | Review Date |
| 95 | Approved By |
| 96 | Approval Date |
| 97 | Exception Duration |
| 98 | Valid From Date |
| 99 | Valid Until Date |
| 100 | Days Until Expiry |
| 101 | Review Required |
| 102 | Audit Trail |
| 103 | Monitoring Required |
| 104 | Monitoring Description |
| 105 | Re Assessment Trigger |
| 106 | Exception Closure Plan |
| 107 | Documentation Reference |
| 108 | Remediation ID |
| 109 | Gap Type |
| 110 | Impact Assessment |
| 111 | Discovery Date |
| 112 | Discovery Method |
| 113 | Remediation Strategy |
| 114 | Remediation Description |
| 115 | Remediation Team |
| 116 | Estimated Effort |
| 117 | Estimated Cost |
| 118 | Dependencies |
| 119 | Remediation Priority |
| 120 | Target Start Date |
| 121 | Target Completion Date |
| 122 | Actual Start Date |
| 123 | Actual Completion Date |
| 124 | Days To Remediate |
| 125 | Days Overdue |
| 126 | Status Notes |
| 127 | Completion Percentage |
| 128 | Blocker Description |
| 129 | Verification Required |
| 130 | Verification Date |
| 131 | Verification Result |
| 132 | Re Test Required |
| 133 | Change Request ID |
| 134 | Risk Acceptance ID |
| 135 | Lessons Learned |
| 136 | Preventive Action |
| 137 | Closure Date |
| 138 | Assessment Area |
| 139 | Total Items |
| 140 | Compliant |
| 141 | Partial |
| 142 | Non-Compliant |
| 143 | N/A |
| 144 | Compliance % |
| 145 | Priority Rank |
| 146 | Exploitation Likelihood |
| 147 | Risk Score |
| 148 | Priority Category |
| 149 | Days Until Target |
| 150 | Quick Win |
| 151 | Related Gaps |
| 152 | Batch Opportunity |
| 153 | Evidence ID |
| 154 | Evidence Type |
| 155 | Description |
| 156 | Location/Path |
| 157 | Date Collected |
| 158 | Collected By |
| 159 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Configuration file, Screenshot, Network scan, Documentation, Vendor spec
Certificate inventory, Audit log, Compliance report, Other, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred, Critical, High, Medium, Low
Industry Benchmark, Government Standard, Regulatory Requirement
Vendor Baseline, Framework Control, Custom Organisational Standard, Level 1
Level 2, Custom, Mandatory, Optional, Monthly, Quarterly, Semi-Annual, Annual
\u2705 Active, \u26A0\uFE0F Deprecated, Planned, Required, Recommended
Not Applicable, \u2705 Fully Compliant, \u2705 Compliant
\u26A0\uFE0F Substantially Compliant, \u26A0\uFE0F Partially Compliant
\u274C Non-Compliant, ❌ Not Started, Planning, ⏳ In Progress, \u274C Blocked
\u2705 Completed, \u26A0\uFE0F Accepted as Exception, \u2705 Implemented
\u26A0\uFE0F Partial, \u274C Not Implemented, ➖ Not Applicable, Automated Tool
Manual Configuration, Native Feature, Third-Party Tool, Compensating Control
Not Implemented, Access Control, Audit & Logging, Authentication
Network Security, Data Protection, System Hardening, Patch Management
Secure Configuration, Service Minimization, Physical Security, Cryptography
Backup & Recovery, \u2705 Pass, \u274C Fail, ➖ N/A, Configuration Export
Security Tool Report, Manual Inspection, Audit Log Review, Test/Validation
Documentation Review, Yes, No, Technical Limitation, Business Requirement
Legacy System, Performance Impact, Vendor Limitation, Cost Prohibitive
Temporary Transition, Regulatory Conflict, ⏳ Pending Review, ⏳ Under Review
\u2705 Approved, \u26A0\uFE0F Conditionally Approved, \u274C Rejected
⏰ Expired, \u2705 Closed, 3 Months, 6 Months, 12 Months, 24 Months, Indefinite
Full, Partial, None, Hardening Gap, Configuration Drift, Vulnerability
Audit Finding, Threat Response, Security Assessment, Vulnerability Scan
Configuration Monitoring, Penetration Test, Incident Response, Audit
Threat Intelligence, Configuration Change, Software Update, Policy Change
Accept as Exception, Asset Decommission, Defer, <1 hour, 1-4 hours, 1 day
2-5 days, 1-2 weeks, 2-4 weeks, >1 month, Identified, ⏳ Verification
\u26A0\uFE0F Deferred, \u2705 Closed - Fixed, \u26A0\uFE0F Closed - Exception
➖ Closed - Not Required, Security Scan Report, Audit Log Extract
Policy/Procedure Document, Test Results, Attestation, Change Record
Exception Approval, Vendor Documentation, Manual Collection, System Export
Security Tool, Change Management System, Documentation Repository, Email
Meeting Minutes, API/Script, Command Line, GUI Screenshot, File Export
Report Generation, Manual Documentation, Copy/Paste, Point-in-Time, 1 Month
Continuous, Until Changed, \u26A0\uFE0F Superseded, Very High, Very Low
```

**Extracted:** 11 sheets, 159 columns, 173 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"The more we study the major problems of our time, the more we come to realise that they cannot be understood in isolation."*
— Fritjof Capra

<!-- QA_VERIFIED: 2026-02-06 -->
