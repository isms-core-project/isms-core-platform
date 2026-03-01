<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.4.2-TG:framework:TG:a.8.4.2 -->
**ISMS-IMP-A.8.4.2-TG - Branch Protection Configuration**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Branch Protection Configuration |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.4.2-TG |
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
- ISMS-IMP-A.8.4.1 (Repository Access Control Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a84_2_branch_protection.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.4.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Repository Branch Inventory |
| 3 | Branch Protection Details |
| 4 | Pull Request Configuration |
| 5 | Status Check Verification |
| 6 | Signed Commits Audit |
| 7 | Exception Management |
| 8 | Gap Analysis |
| 9 | Evidence Register |
| 10 | Summary Dashboard |
| 11 | Approval Sign-Off |

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
| 1 | REPOSITORY BRANCH INVENTORY |
| 2 | BRANCH PROTECTION DETAILS |
| 3 | PULL REQUEST CONFIGURATION |
| 4 | STATUS CHECK VERIFICATION |
| 5 | SIGNED COMMITS AUDIT |
| 6 | EXCEPTION MANAGEMENT |
| 7 | GAP ANALYSIS |
| 8 | Repository Name |
| 9 | Repository Platform |
| 10 | Repository Classification |
| 11 | Branch Name |
| 12 | Branch Type |
| 13 | Protection Required |
| 14 | Protection Configured |
| 15 | Status |
| 16 | Direct Commits Blocked |
| 17 | Pull Request Required |
| 18 | Required Approvals |
| 19 | Dismiss Stale Reviews |
| 20 | Code Owner Review |
| 21 | Status Checks Required |
| 22 | Status Check List |
| 23 | Signed Commits Required |
| 24 | Linear History |
| 25 | Compliance Score (%) |
| 26 | Minimum Reviewers |
| 27 | Dismiss Stale Approvals |
| 28 | Restrict Dismiss |
| 29 | Conversation Resolution |
| 30 | Self-Approval Blocked |
| 31 | Compliance Status |
| 32 | Status Checks Configured |
| 33 | Build Check |
| 34 | Test Check |
| 35 | Lint Check |
| 36 | Security Check |
| 37 | All Checks Must Pass |
| 38 | Up-to-Date Before Merge |
| 39 | % Commits Signed (30 days) |
| 40 | GPG Infrastructure |
| 41 | Developer Training |
| 42 | Exception ID |
| 43 | Repository/Branch |
| 44 | Exception Reason |
| 45 | Granted By |
| 46 | Grant Date |
| 47 | Expiration Date |
| 48 | Review Date |
| 49 | Gap ID |
| 50 | Gap Description |
| 51 | Affected Repositories |
| 52 | Remediation Plan |
| 53 | Responsible Party |
| 54 | Target Date |
| 55 | Notes |
| 56 | Evidence ID |
| 57 | Assessment Area |
| 58 | Evidence Type |
| 59 | Description |
| 60 | Location/Path |
| 61 | Date Collected |
| 62 | Collected By |
| 63 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
GitHub, GitLab, Bitbucket, Azure DevOps, Self-Hosted, Other, Production Code
Internal Tools, Open Source, Archived, Main, Release, Development, Feature
Hotfix, Active, Expired, Revoked, Open, In Progress, Closed, Deferred
Configuration file, Screenshot, Network scan, Documentation, Vendor spec
Certificate inventory, Audit log, Compliance report, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected
```

**Extracted:** 11 sheets, 63 columns, 41 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Secret sharing allows us to distribute trust among multiple parties, eliminating single points of failure."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
