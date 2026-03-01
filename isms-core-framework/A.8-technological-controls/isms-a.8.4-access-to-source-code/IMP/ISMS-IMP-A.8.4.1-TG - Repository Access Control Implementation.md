<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.4.1-TG:framework:TG:a.8.4.1 -->
**ISMS-IMP-A.8.4.1-TG - Repository Access Control Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Repository Access Control Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.4.1-TG |
| **Related Policy** | ISMS-POL-A.8.4 (Access to Source Code) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.4 (Access to Source Code) |
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

- ISMS-POL-A.8.4 (Access to Source Code)
- ISMS-IMP-A.8.4.2 (Branch Protection Configuration)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a84_1_repository_access.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.4.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Repository Inventory |
| 3 | User Access Matrix |
| 4 | Access Approval Records |
| 5 | Access Review Log |
| 6 | Deprovisioning Log |
| 7 | Third Party Access |
| 8 | Service Accounts |
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
| 1 | REPOSITORY INVENTORY |
| 2 | USER ACCESS MATRIX |
| 3 | ACCESS APPROVAL RECORDS |
| 4 | ACCESS REVIEW LOG |
| 5 | DEPROVISIONING LOG |
| 6 | THIRD PARTY SOURCE CODE ACCESS |
| 7 | SERVICE ACCOUNT AND BOT ACCESS INVENTORY |
| 8 | GAP ANALYSIS |
| 9 | Repository Name |
| 10 | Repository URL |
| 11 | Repository Platform |
| 12 | Repository Classification |
| 13 | Repository Owner |
| 14 | Repository Owner Email |
| 15 | Business Purpose |
| 16 | Primary Programming Language |
| 17 | Last Commit Date |
| 18 | Active/Inactive Status |
| 19 | Total Contributors |
| 20 | Total Commits (Lifetime) |
| 21 | Repository Creation Date |
| 22 | Criticality |
| 23 | Contains Production Code |
| 24 | Contains Sensitive Data |
| 25 | Branch Protection Enabled |
| 26 | Secret Scanning Enabled |
| 27 | Last Access Review Date |
| 28 | Notes |
| 29 | User Name |
| 30 | User Email |
| 31 | User Role |
| 32 | Employment Type |
| 33 | Department/Team |
| 34 | Access Level |
| 35 | Access Granted Date |
| 36 | Access Approved By |
| 37 | Business Justification |
| 38 | Contract End Date |
| 39 | Access Expiration Date |
| 40 | Last Access Date |
| 41 | Access Status |
| 42 | Last Review Date |
| 43 | Reviewer Comments |
| 44 | Remediation Required |
| 45 | Remediation Due Date |
| 46 | Request Date |
| 47 | Request ID |
| 48 | Requestor Name |
| 49 | Requestor Email |
| 50 | Access Level Requested |
| 51 | Expected Duration |
| 52 | Expected End Date |
| 53 | Owner Approval |
| 54 | Approval Date |
| 55 | Additional Approver |
| 56 | Additional Approval |
| 57 | Provisioning Date |
| 58 | Provisioned By |
| 59 | Denial Reason |
| 60 | Review Date |
| 61 | Review Quarter |
| 62 | Reviewer Name |
| 63 | Reviewer Role |
| 64 | Repositories Reviewed |
| 65 | Repository Names |
| 66 | Total Users Reviewed |
| 67 | Appropriate Access Found |
| 68 | Excessive Access Found |
| 69 | Unnecessary Access Found |
| 70 | Orphaned Accounts Found |
| 71 | Contractor Expired Found |
| 72 | Total Findings |
| 73 | Remediation Completed |
| 74 | Remediation Pending |
| 75 | Review Completion Date |
| 76 | Days to Complete |
| 77 | Next Review Due Date |
| 78 | Compliance Status |
| 79 | Deprovisioning Event |
| 80 | Event Date |
| 81 | Notification Received Date |
| 82 | Previous Access Level |
| 83 | Access Removed Date |
| 84 | Hours to Deprovision |
| 85 | Removed By |
| 86 | Removal Method |
| 87 | Verification Method |
| 88 | Verification Date |
| 89 | Compliant Timeline |
| 90 | Delay Reason |
| 91 | Third Party Name |
| 92 | Access Type |
| 93 | Repository/System |
| 94 | Approved By |
| 95 | Expiry Date |
| 96 | NDA Reference |
| 97 | Risk Rating |
| 98 | Account Name |
| 99 | Account Type |
| 100 | Purpose |
| 101 | Owner |
| 102 | Authentication Method |
| 103 | Secret Storage |
| 104 | Last Rotated |
| 105 | Rotation Frequency |
| 106 | Status |
| 107 | Gap ID |
| 108 | Gap Category |
| 109 | Gap Description |
| 110 | Policy Requirement |
| 111 | Current State |
| 112 | Desired State |
| 113 | Risk Level |
| 114 | Impact |
| 115 | Affected Repositories |
| 116 | Root Cause |
| 117 | Remediation Plan |
| 118 | Responsible Party |
| 119 | Target Completion Date |
| 120 | Estimated Effort |
| 121 | Actual Completion Date |
| 122 | Evidence ID |
| 123 | Assessment Area |
| 124 | Evidence Type |
| 125 | Description |
| 126 | Location/Path |
| 127 | Date Collected |
| 128 | Collected By |
| 129 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
GitHub, GitLab, Bitbucket, Azure DevOps, Self-Hosted Git, Perforce, SVN, Other
Production Code, Internal Tools, Open Source, Archived/Deprecated, Active
Archived, Deprecated, Planned, Critical, High, Medium, Low, Developer
Security Team, Auditor, External Contractor, Repository Admin, Service Account
Employee, Contractor, Automated System, Read, Write/Contribute, Admin
Permanent, Time-Bound, Termination, Role Change, Contract End, Access Review
Security Incident, Automated, Manual, Platform Check, Login Test, API Query
Consultant, Vendor, Partner, Suspended, Expired, Revoked, Pending
CI/CD Pipeline, Deployment Bot, Monitoring Agent, Integration Service, API Key
SSH Key, Personal Access Token, OAuth Token, Deploy Key, Certificate
Vault/HSM, CI/CD Secrets, Environment Variable, Key Management Service
30 days, 60 days, 90 days, 180 days, 365 days, On compromise only, N/A
Disabled, Pending Review, Access Control, Inventory, Reviews, Deprovisioning
Documentation, [CRIT] Critical, [HIGH] High, [MED] Medium, [LOW] Low
1-2 hours, 1 day, 1 week, 2-4 weeks, >1 month, [OPEN] Open, [PROG] In Progress
[DONE] Completed, [DEF] Deferred, Configuration file, Screenshot, Network scan
Vendor spec, Certificate inventory, Audit log, Compliance report, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 129 columns, 111 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Cryptanalysis is like solving a puzzle where the puzzle maker actively tries to stop you."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
