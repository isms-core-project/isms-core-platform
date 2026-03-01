<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.1-7-18-19-S4-TG:framework:TG:a.8.1-7-18-19-s4 -->
**ISMS-IMP-A.8.1-7-18-19-S4-TG - Privileged Utility Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Privileged Utility Management |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S4-TG |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19-S4 (Endpoint Security) |
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

- ISMS-POL-A.8.1-7-18-19-S4 (Endpoint Security)
- ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process)
- ISMS-IMP-A.8.1-7-18-19-S2 (Malware Protection Deployment)
- ISMS-IMP-A.8.1-7-18-19-S3 (Software Control Process)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a81-7-18-19_4_privileged_utilities.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.1-7-18-19.4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Utility Inventory |
| 3 | Access Controls |
| 4 | Approval Workflow |
| 5 | Usage Audit |
| 6 | MFA Compliance |
| 7 | Quarterly Reviews |
| 8 | Capability Requirements |
| 9 | Gap Analysis |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

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
| 1 | PRIVILEGED UTILITY INVENTORY |
| 2 | Total Utilities: |
| 3 | ACCESS CONTROL CONFIGURATION |
| 4 | PRIVILEGED ACCESS APPROVAL WORKFLOW |
| 5 | PRIVILEGED UTILITY USAGE AUDIT LOG |
| 6 | MFA COMPLIANCE FOR PRIVILEGED ACCESS |
| 7 | QUARTERLY PRIVILEGED ACCESS REVIEWS |
| 8 | Total Critical/High Findings: |
| 9 | EVIDENCE REGISTER |
| 10 | Total Evidence Entries: |
| 11 | GAP ANALYSIS & REMEDIATION TRACKING |
| 12 | Utility ID |
| 13 | Utility Name |
| 14 | Platform |
| 15 | Category |
| 16 | Risk Level |
| 17 | Business Justification |
| 18 | Authorised Roles |
| 19 | Access Control Method |
| 20 | MFA Required |
| 21 | Logging Enabled |
| 22 | Notes |
| 23 | File Permissions Set |
| 24 | AD Group Restriction |
| 25 | AppLocker Rule |
| 26 | Control Status |
| 27 | Last Verified |
| 28 | Verified By |
| 29 | Issues |
| 30 | Request ID |
| 31 | Request Date |
| 32 | Requester |
| 33 | Utility |
| 34 | Access Type |
| 35 | Duration |
| 36 | Justification |
| 37 | Manager Approval |
| 38 | Security Approval |
| 39 | Status |
| 40 | Log ID |
| 41 | Timestamp |
| 42 | User |
| 43 | Device |
| 44 | Action |
| 45 | Authorised |
| 46 | Flagged |
| 47 | Role |
| 48 | Utility Access |
| 49 | MFA Technology |
| 50 | MFA Status |
| 51 | Last MFA Setup |
| 52 | Compliance |
| 53 | Review Quarter |
| 54 | Last Used |
| 55 | Manager Review |
| 56 | Decision |
| 57 | Action Taken |
| 58 | Completion Date |
| 59 | Reviewer |
| 60 | Req ID |
| 61 | Policy Requirement |
| 62 | Implemented |
| 63 | Evidence Reference |
| 64 | Assessment Area |
| 65 | Total Items |
| 66 | Compliant |
| 67 | Partial |
| 68 | Non-Compliant |
| 69 | N/A |
| 70 | Compliance % |
| 71 | KPI |
| 72 | Current Value |
| 73 | Target |
| 74 | Last Updated |
| 75 | Owner |
| 76 | Finding ID |
| 77 | Description |
| 78 | Affected Area |
| 79 | Severity |
| 80 | Due Date |
| 81 | Evidence ID |
| 82 | Evidence Type |
| 83 | Related Requirement |
| 84 | Related Worksheet/Device |
| 85 | File Location |
| 86 | Collection Date |
| 87 | Collected By |
| 88 | Gap ID |
| 89 | Affected Utilities |
| 90 | Requirement |
| 91 | Risk |
| 92 | Root Cause |
| 93 | Remediation |
| 94 | Budget Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, [TOOL] System Admin, [BUG] Debugging, [UNLOCK] Security Bypass
[WEB] Network Tools, [DISK] Disk/File, Third-Party Admin, Other, Critical
High, Medium, Low, Standing, Temporary, JIT High-Risk, JIT Critical, Emergency
Open, In Progress, Resolved, Closed, Config, Screenshot, Report, Policy, Log
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 94 columns, 36 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"It is perfectly obvious that the whole world is going to hell. The only possible chance that it might not is that we do not attempt to prevent it from doing so."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
