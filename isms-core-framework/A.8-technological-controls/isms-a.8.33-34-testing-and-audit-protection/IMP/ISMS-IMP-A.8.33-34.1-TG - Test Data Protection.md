<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.33-34.1-TG:framework:TG:a.8.33-34.1 -->
**ISMS-IMP-A.8.33-34.1-TG - Test Data Protection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Test Data Protection |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.33-34.1-TG |
| **Related Policy** | ISMS-POL-A.8.33-34 (Testing and Audit Protection) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.33 (Test Information) & A.8.34 (Protection of Information Systems During Audit Testing) |
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

- ISMS-POL-A.8.33-34 (Testing and Audit Protection)
- ISMS-IMP-A.8.33-34.2 (Audit Activity Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a83334_1_test_data_protection.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.33-34.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Test Data Inventory |
| 3 | Data Masking Assessment |
| 4 | Test Environment Registry |
| 5 | Data Refresh Schedule |
| 6 | Compliance Verification |
| 7 | Summary Dashboard |
| 8 | Evidence Register |
| 9 | Approval Sign-Off |

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
| 1 | TEST DATA INVENTORY |
| 2 | SUMMARY STATISTICS |
| 3 | DATA MASKING ASSESSMENT |
| 4 | MASKING TECHNIQUE SUMMARY |
| 5 | EFFECTIVENESS SUMMARY |
| 6 | Average Effectiveness Score |
| 7 | High Re-identification Risk |
| 8 | Critical Masking Gaps |
| 9 | TEST ENVIRONMENT REGISTRY |
| 10 | ENVIRONMENT STATISTICS |
| 11 | DATA REFRESH SCHEDULE |
| 12 | REFRESH STATISTICS |
| 13 | COMPLIANCE VERIFICATION |
| 14 | COMPLIANCE STATISTICS |
| 15 | Data Set ID |
| 16 | Data Set Name |
| 17 | Source System |
| 18 | Target Environment |
| 19 | Data Classification |
| 20 | Contains PII |
| 21 | PII Categories |
| 22 | Data Volume |
| 23 | Authorisation Status |
| 24 | Data Owner |
| 25 | Authoriser |
| 26 | Authorisation Date |
| 27 | Last Copy Date |
| 28 | Refresh Frequency |
| 29 | Masking Required |
| 30 | Masking Status |
| 31 | Business Justification |
| 32 | Expiration Date |
| 33 | Evidence Reference |
| 34 | Notes |
| 35 | Deleted After Testing |
| 36 | Primary Masking Technique |
| 37 | Masking Tool |
| 38 | Masking Effectiveness Score |
| 39 | PII Fields Identified |
| 40 | PII Fields Masked |
| 41 | PII Fields Unmasked |
| 42 | Masking Verification Date |
| 43 | Verification Method |
| 44 | Re identification Risk |
| 45 | Masking Gap Severity |
| 46 | Remediation Owner |
| 47 | Remediation Target Date |
| 48 | Remediation Status |
| 49 | Exception Approved |
| 50 | Exception Justification |
| 51 | Environment ID |
| 52 | Environment Name |
| 53 | Environment Type |
| 54 | Infrastructure Type |
| 55 | Environment Owner |
| 56 | Business Unit |
| 57 | Highest Data Classification |
| 58 | Contains Production Data |
| 59 | Access Control Type |
| 60 | Network Isolation |
| 61 | Encryption at Rest |
| 62 | Encryption in Transit |
| 63 | Logging Enabled |
| 64 | Patch Management |
| 65 | Security Control Status |
| 66 | Last Security Review |
| 67 | Next Review Due |
| 68 | Data Masking Enforced |
| 69 | Environment URL Location |
| 70 | Support Contact |
| 71 | Refresh ID |
| 72 | Data Sources |
| 73 | Refresh Method |
| 74 | Last Refresh Date |
| 75 | Next Scheduled Refresh |
| 76 | Masking Applied at Refresh |
| 77 | Refresh Duration |
| 78 | Refresh Window |
| 79 | Retention Period |
| 80 | Auto Purge Enabled |
| 81 | Refresh Owner |
| 82 | Refresh Log Location |
| 83 | Requirement ID |
| 84 | Requirement Source |
| 85 | Requirement Reference |
| 86 | Requirement Description |
| 87 | Applicable Data Sets |
| 88 | Applicable Environments |
| 89 | Compliance Status |
| 90 | Last Verification Date |
| 91 | Verifier |
| 92 | Findings |
| 93 | Finding Severity |
| 94 | Remediation Required |
| 95 | Next Verification Due |
| 96 | Assessment Area |
| 97 | Total Items |
| 98 | Compliant |
| 99 | Partial |
| 100 | Non-Compliant |
| 101 | N/A |
| 102 | Compliance % |
| 103 | Metric |
| 104 | Value |
| 105 | Category |
| 106 | Finding |
| 107 | Count |
| 108 | Severity |
| 109 | Action Required |
| 110 | Evidence ID |
| 111 | Evidence Type |
| 112 | Description |
| 113 | Location/Path |
| 114 | Date Collected |
| 115 | Collected By |
| 116 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Public, Internal, Confidential, Restricted, Yes, No, Authorised, Pending
Unauthorised, N/A, Daily, Weekly, Monthly, Quarterly, Ad-Hoc, One-Time
Fully Masked, Partially Masked, Not Masked, Substitution, Shuffling
Tokenization, Encryption, Synthetic, Anonymization, None, 1, 2, 3, 4, 5
Automated, Manual Sampling, High, Medium, Low, Critical, Not Started
In Progress, Completed, Development, QA, Staging, UAT, Performance, Training
DR-Test, Sandbox, On-Premise, Cloud-AWS, Cloud-Azure, Cloud-GCP, Hybrid
Container, Local, RBAC, AD/LDAP, SSO, Local Accounts, Full, Partial
Manual-Current, Manual-Delayed, Compliant, Non-Compliant, Bi-Weekly, Full Copy
Incremental, Subset, Clone, Yes - Automated, Yes - Manual, GDPR, ISO 27001
FADP, Internal Policy, Industry Standard, Not Assessed, Automated Check
Manual Audit, Self-Assessment, Third-Party Audit, Configuration file
Screenshot, Network scan, Documentation, Vendor spec, Certificate inventory
Audit log, Compliance report, Other, Verified, Pending verification
Not verified, Requires update, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 116 columns, 103 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The best time to discover a data protection flaw is during testing, not after a breach."*

<!-- QA_VERIFIED: 2026-02-06 -->
