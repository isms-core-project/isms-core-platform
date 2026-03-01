<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.33-34.2-TG:framework:TG:a.8.33-34.2 -->
**ISMS-IMP-A.8.33-34.2-TG - Audit Activity Management Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Audit Activity Management |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.33-34.2-TG |
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
- ISMS-IMP-A.8.33-34.1 (Test Data Protection)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a83334_2_audit_activity_management.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.33-34.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Audit Activity Register |
| 3 | Audit Tool Authorisation |
| 4 | Audit Access Tracking |
| 5 | Disruption Mitigation Plans |
| 6 | Audit Evidence Protection |
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
| 1 | AUDIT ACTIVITY REGISTER |
| 2 | AUDIT STATISTICS |
| 3 | AUDIT TOOL AUTHORISATION |
| 4 | TOOL RISK SUMMARY |
| 5 | AUDIT ACCESS TRACKING |
| 6 | ACCESS STATISTICS |
| 7 | DISRUPTION MITIGATION PLANS |
| 8 | MITIGATION STRATEGY SUMMARY |
| 9 | SYSTEM COVERAGE STATISTICS |
| 10 | AUDIT EVIDENCE PROTECTION |
| 11 | PROTECTION STATISTICS |
| 12 | Audit ID |
| 13 | Audit Name |
| 14 | Audit Type |
| 15 | Audit Scope |
| 16 | Audit Firm Team |
| 17 | Lead Auditor |
| 18 | Planned Start |
| 19 | Planned End |
| 20 | Actual Start |
| 21 | Actual End |
| 22 | Audit Status |
| 23 | Management Approval |
| 24 | Approver |
| 25 | Approval Date |
| 26 | Systems in Scope |
| 27 | Data Access Required |
| 28 | Testing Type |
| 29 | Findings Count |
| 30 | Critical Findings |
| 31 | Report Location |
| 32 | Follow up Status |
| 33 | Notes |
| 34 | Tool ID |
| 35 | Tool Name |
| 36 | Tool Version |
| 37 | Tool Category |
| 38 | Vendor Source |
| 39 | Tool Owner |
| 40 | Authorisation Status |
| 41 | Authorisation Date |
| 42 | Authorised By |
| 43 | Risk Level |
| 44 | Authorised Use Cases |
| 45 | Restrictions |
| 46 | Required Approvals |
| 47 | Storage Location |
| 48 | Access Restricted To |
| 49 | Last Security Review |
| 50 | Next Review Due |
| 51 | Usage Logging Required |
| 52 | License Status |
| 53 | License Expiry |
| 54 | Evidence Reference |
| 55 | Access ID |
| 56 | Auditor Name |
| 57 | Auditor Organisation |
| 58 | Associated Audit |
| 59 | Access Type |
| 60 | Systems Accessed |
| 61 | Data Classification Accessed |
| 62 | Access Requested Date |
| 63 | Access Start Date |
| 64 | Access End Date |
| 65 | Actual Revocation Date |
| 66 | Access Status |
| 67 | Approval Status |
| 68 | Access Logging Enabled |
| 69 | NDA Signed |
| 70 | NDA Reference |
| 71 | Supervision Required |
| 72 | Supervisor |
| 73 | Multi Factor Auth Required |
| 74 | Revocation Confirmation |
| 75 | Device Security Verified |
| 76 | System ID |
| 77 | System Name |
| 78 | System Criticality |
| 79 | Business Owner |
| 80 | Technical Owner |
| 81 | Associated Audits |
| 82 | Primary Mitigation Strategy |
| 83 | Testing Restrictions |
| 84 | Permitted Testing Window |
| 85 | Maximum Test Duration |
| 86 | Backup Required Before Test |
| 87 | Recovery Point Objective |
| 88 | Recovery Time Objective |
| 89 | Rollback Procedure Location |
| 90 | Rollback Last Tested |
| 91 | Escalation Contact |
| 92 | Escalation Phone |
| 93 | Secondary Contact |
| 94 | Monitoring Enhancement |
| 95 | Incident Response Plan |
| 96 | Last Mitigation Review |
| 97 | Review Due Date |
| 98 | Evidence Category ID |
| 99 | Evidence Category |
| 100 | Evidence Description |
| 101 | Sensitivity Classification |
| 102 | Example Documents |
| 103 | Primary Storage Location |
| 104 | Backup Location |
| 105 | Encryption at Rest |
| 106 | Encryption in Transit |
| 107 | Access Control Type |
| 108 | Authorised Accessors |
| 109 | Retention Period |
| 110 | Retention Start Event |
| 111 | Destruction Method |
| 112 | Destruction Approval |
| 113 | Chain of Custody Required |
| 114 | Chain of Custody Process |
| 115 | Legal Hold Applicable |
| 116 | Legal Hold Contact |
| 117 | Integrity Verification |
| 118 | Last Access Review |
| 119 | Evidence Owner |
| 120 | Assessment Area |
| 121 | Total Items |
| 122 | Compliant |
| 123 | Partial |
| 124 | Non-Compliant |
| 125 | N/A |
| 126 | Compliance % |
| 127 | Metric |
| 128 | Value |
| 129 | Category |
| 130 | Finding |
| 131 | Count |
| 132 | Severity |
| 133 | Action Required |
| 134 | Evidence ID |
| 135 | Evidence Type |
| 136 | Description |
| 137 | Location/Path |
| 138 | Date Collected |
| 139 | Collected By |
| 140 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Internal, External-Financial, External-SOC2, Penetration Test
Vulnerability Assessment, Red Team, Regulatory, Compliance, Planned
In Progress, Completed, Cancelled, On Hold, Approved, Pending, Not Required
N/A, Non-Invasive, Read-Only, Active Testing, Exploitation, Open, Closed
Vulnerability Scanner, Penetration Tool, Network Analyser, Web App Scanner
Forensic Tool, Credential Tester, Exploitation Framework, Other, Authorised
Unauthorised, Prohibited, High, Medium, Low, Yes, No, Valid, Expired
Read-Write, Admin, Physical, Remote-VPN, Public, Confidential, Restricted
Active, Revoked, Denied, Partial, Critical, Staging First, Off-Hours
Rate Limiting, Scope Exclusion, Enhanced Monitoring, Standby Recovery
Read-Only Only, Multi-Strategy, Already Scheduled, AES-256, AES-128, BitLocker
None, TLS 1.3, TLS 1.2, VPN, RBAC, ACL, Individual Permissions, 1 Year
2 Years, 3 Years, 5 Years, 7 Years, Permanent, Legal Hold, Secure Delete
Shredding, Degaussing, Certified Destruction, Potentially, Hashing
Digital Signatures, Checksums, Configuration file, Screenshot, Network scan
Documentation, Vendor spec, Certificate inventory, Audit log
Compliance report, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 140 columns, 106 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The purpose of an audit is to improve, not to prove."*

<!-- QA_VERIFIED: 2026-02-06 -->
