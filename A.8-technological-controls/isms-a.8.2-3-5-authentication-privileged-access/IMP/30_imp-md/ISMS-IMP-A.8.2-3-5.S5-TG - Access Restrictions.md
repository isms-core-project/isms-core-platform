**ISMS-IMP-A.8.2-3-5.S5-TG - Access Restrictions Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Technical Access Control Implementation & Effectiveness |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Section 2.3 - Information Access Restriction) |
| **Purpose** | Verify technical implementation of access controls across operating systems, databases, applications, APIs, and networks; validate default deny principle and encryption-based access restriction |
| **Target Audience** | Security Team, IT Operations, System Owners, Database Administrators, Application Teams, Network Team |
| **Assessment Type** | Configuration Audit & Access Control Effectiveness Testing |
| **Review Cycle** | Quarterly comprehensive assessment, Continuous configuration monitoring |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for access restriction verification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.2-3-5.S5-UG.

---

# Technical Specification

# Excel Workbook Structure

## Workbook Overview

**Filename:** `ISMS-IMP-A.8.2-3-5.5_Access_Restrictions_YYYYMMDD.xlsx`

**Sheet Structure:**

| Sheet # | Sheet Name | Purpose | Rows | Completion Method |
|---------|-----------|---------|------|-------------------|
| 1 | Instructions_Legend | User guide and access control reference | ~60 | Pre-populated |
| 2 | File_System_Permissions | File system permission audits and compliance | 253 | User completes |
| 3 | Database_Access_Controls | Database grant and role audits | 253 | User completes |
| 4 | Application_RBAC | Application RBAC and permission audits | 253 | User completes |
| 5 | API_Access_Controls | API authentication and authorization controls | 253 | User completes |
| 6 | Cloud_IAM_Policies | Cloud service IAM policies and role assignments | 153 | User completes |
| 7 | Encryption_Status | Encryption key access and management controls | 153 | User completes |
| 8 | Network_Segmentation | Network zone segmentation and isolation verification | 103 | User completes |
| 9 | Penetration_Test_Results | Access control security testing results | ~50 | User completes |
| 10 | Gap_Analysis | Access control gaps and remediation priority | ~100 | Auto-calculated |
| 11 | Evidence_Register | Evidence tracking | 53 | User completes |
| 12 | Approval_Sign_Off | Three-level approval workflow | ~25 | User completes |

**Total Workbook:** 12 sheets, ~1,600 rows of structured data collection

## Color Coding & Conditional Formatting

**Compliance Status Colors:**

- 🟢 **Green (Compliant)**: RGB(198, 239, 206) - Meets all access control requirements
- 🟡 **Yellow (Partial)**: RGB(255, 235, 156) - Meets some requirements, gaps exist
- 🔴 **Red (Non-Compliant)**: RGB(255, 199, 206) - Does not meet requirements

**Gap Priority Colors:**

- 🔴 **Critical**: RGB(255, 0, 0) - Immediate action
- 🟠 **High**: RGB(255, 153, 0) - Within 30 days
- 🟡 **Medium**: RGB(255, 255, 0) - Within 90 days
- 🟢 **Low**: RGB(146, 208, 80) - Ongoing improvement

---

# Sheet 2: OS Access Controls

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | System ID | 15 | Text | Free text | Unique identifier |
| B | System Name | 22 | Text | Free text | System name |
| C | Operating System | 20 | Dropdown | Windows Server, Linux (Ubuntu), Linux (RHEL), Linux (Other), macOS, Other | OS type |
| D | Data Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Data sensitivity |
| E | Access Control Type | 15 | Dropdown | NTFS, ext4 ACL, XFS ACL, ZFS ACL, NFS ACL, Other | Permission system |
| F | Default Deny | 12 | Dropdown | Yes, No | Explicit allow required? |
| G | Permission Inheritance | 15 | Dropdown | Yes, No, N/A | Subfolder inheritance? |
| H | Last Audit Date | 15 | Date | DD.MM.YYYY | Last permission review |
| I | Excessive Permissions | 15 | Dropdown | Yes, No | Overly broad permissions? |
| J | Cleanup Completed | 15 | Dropdown | Yes, No, N/A | Permissions cleaned up? |
| K | Compliance Status | 15 | Formula | Auto: Compliant, Non-Compliant | Meets policy? |
| L | Evidence Location | 25 | Text | Free text | Link to audit export |

**Total Columns:** 12 (A-L)

## Compliance Calculation (Column K)

```excel
=IF(AND(F5="Yes", I5="No"), "Compliant", "Non-Compliant")
```

---

# Sheet 3: Database Access Controls

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Database ID | 15 | Text | Free text | Unique identifier |
| B | Database Name | 22 | Text | Free text | Database name |
| C | Database Type | 18 | Dropdown | SQL Server, Oracle, PostgreSQL, MySQL, MongoDB, DynamoDB, Cosmos DB, Other | DB platform |
| D | Data Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Data sensitivity |
| E | Role-Based Access | 15 | Dropdown | Yes, No | Database roles used? |
| F | Least Privilege | 12 | Dropdown | Yes, No | Minimal grants? |
| G | Row-Level Security | 15 | Dropdown | Yes, No, N/A | RLS implemented? |
| H | Column-Level Security | 18 | Dropdown | Yes, No, N/A | CLS implemented? |
| I | Last Grant Audit | 15 | Date | DD.MM.YYYY | Last grant review |
| J | Excessive Grants | 15 | Dropdown | Yes, No | Overly broad grants? |
| K | PUBLIC Role Grants | 15 | Dropdown | Yes - Review, No | Dangerous public grants? |
| L | Compliance Status | 15 | Formula | Auto: Compliant, Non-Compliant | Meets policy? |

**Total Columns:** 12 (A-L)

## Compliance Calculation (Column L)

```excel
=IF(AND(F5="Yes", J5="No", K5="No"), "Compliant", "Non-Compliant")
```

---

# Sheet 4: Application Access Controls

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Application ID | 15 | Text | Free text | Unique identifier |
| B | Application Name | 22 | Text | Free text | Application name |
| C | Application Type | 15 | Dropdown | Web App, Desktop App, Mobile App, API, Other | App category |
| D | Data Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Data sensitivity |
| E | Access Control Model | 18 | Dropdown | RBAC, ABAC, ACL, Custom, None | Model type |
| F | Roles Defined | 12 | Dropdown | Yes, No | Documented roles? |
| G | Permissions Matrix | 15 | Dropdown | Yes, No | Permission mapping documented? |
| H | Enforcement Location | 18 | Dropdown | Backend Only, Frontend Only, Both, None | Where checked? |
| I | Last Access Test | 15 | Date | DD.MM.YYYY | Last security test |
| J | Bypass Found | 15 | Dropdown | Yes, No | Vulnerabilities? |
| K | Remediation Complete | 15 | Dropdown | Yes, No, N/A | Fixed? |
| L | Compliance Status | 15 | Formula | Auto: Compliant, Non-Compliant | Meets policy? |

**Total Columns:** 12 (A-L)

## Compliance Calculation (Column L)

```excel
=IF(AND(E5<>"None", H5<>"None", H5<>"Frontend Only", J5="No"), 
    "Compliant", "Non-Compliant")
```

---

# Sheet 5: API Access Controls

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | API ID | 15 | Text | Free text | Unique identifier |
| B | API Name | 22 | Text | Free text | API name |
| C | API Type | 12 | Dropdown | REST, GraphQL, SOAP, gRPC, Other | API protocol |
| D | Data Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Data sensitivity |
| E | Authentication | 18 | Dropdown | OAuth 2.0, API Key, JWT, mTLS, Basic Auth, None | Auth method |
| F | Authorization Model | 18 | Dropdown | OAuth Scopes, API Key Permissions, Role-Based, None | Authz model |
| G | Rate Limiting | 12 | Dropdown | Yes, No | Rate limited? |
| H | Rate Limit (req/min) | 15 | Number | ≥0 | Limit value |
| I | Last Security Test | 15 | Date | DD.MM.YYYY | Last API test |
| J | IDOR Vulnerability | 15 | Dropdown | Yes, No | IDOR found? |
| K | Broken Access Control | 18 | Dropdown | Yes, No | OWASP A01:2021? |
| L | Compliance Status | 15 | Formula | Auto: Compliant, Non-Compliant | Meets policy? |

**Total Columns:** 12 (A-L)

## Compliance Calculation (Column L)

```excel
=IF(AND(E5<>"None", F5<>"None", G5="Yes", J5="No", K5="No"), 
    "Compliant", "Non-Compliant")
```

---

# Sheet 6: Network Segmentation

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Zone Name | 18 | Text | Free text | Network zone |
| B | Zone Purpose | 25 | Text | Free text | Purpose |
| C | Data Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Data in zone |
| D | Segmentation Method | 18 | Dropdown | Firewall, VLAN, Security Group, Subnet, None | Method |
| E | Firewall Rules | 12 | Dropdown | Yes, No | Rules configured? |
| F | Default Deny | 12 | Dropdown | Yes, No | Deny all, allow specific? |
| G | VLAN Segmentation | 15 | Dropdown | Yes, No, N/A | VLANs used? |
| H | Last Rule Review | 15 | Date | DD.MM.YYYY | Last review |
| I | Unnecessary Rules | 15 | Dropdown | Yes, No | Overly permissive? |
| J | Segmentation Tested | 15 | Dropdown | Yes, No | Pen tested? |
| K | Compliance Status | 15 | Formula | Auto: Compliant, Non-Compliant | Meets policy? |

**Total Columns:** 11 (A-K)

## Compliance Calculation (Column K)

```excel
=IF(AND(E5="Yes", F5="Yes", I5="No"), "Compliant", "Non-Compliant")
```

---

# Sheet 7: Encryption-Based Access

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | System ID | 15 | Text | Free text | Unique identifier |
| B | System Name | 22 | Text | Free text | System name |
| C | System Type | 15 | Text | Free text | Type |
| D | Data Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Data sensitivity |
| E | Encryption at Rest | 15 | Dropdown | Yes, No | Encrypted? |
| F | Encryption Type | 18 | Dropdown | BitLocker, LUKS, TDE, AWS KMS, Azure SSE, Other | Encryption method |
| G | Key Management | 22 | Text | Free text | Who has keys? |
| H | Encryption Required | 15 | Formula | Auto: Yes, No | Per policy? |
| I | Encryption in Transit | 15 | Dropdown | Yes, No | TLS enforced? |
| J | Protocol | 12 | Dropdown | TLS 1.2, TLS 1.3, IPsec, VPN, None | Protocol |
| K | TLS Enforcement | 15 | Dropdown | Mandatory, Optional, None | Enforcement |
| L | Compliance Status | 15 | Formula | Auto: Compliant, Non-Compliant | Meets policy? |

**Total Columns:** 12 (A-L)

## Encryption Required (Column H)

```excel
=IF(OR(D5="Confidential", D5="Restricted"), "Yes", "No")
```

## Compliance Calculation (Column L)

```excel
=IF(H5="Yes", 
    IF(AND(E5="Yes", I5="Yes"), "Compliant", "Non-Compliant"),
    "N/A")
```

---

# Sheet 8: Compliance Summary (Dashboard)

## Metrics Calculated

```excel
OS Access Control Compliance %: 
  =COUNTIF('OS Access Controls'!K:K, "Compliant") / 
   COUNTA('OS Access Controls'!K5:K253) * 100

Database Access Control Compliance %: 
  =COUNTIF('Database Access Controls'!L:L, "Compliant") / 
   COUNTA('Database Access Controls'!L5:L253) * 100

Application Access Control Compliance %: 
  =COUNTIF('Application Access Controls'!L:L, "Compliant") / 
   COUNTA('Application Access Controls'!L5:L253) * 100

API Security Compliance %: 
  =COUNTIF('API Access Controls'!L:L, "Compliant") / 
   COUNTA('API Access Controls'!L5:L253) * 100

Network Segmentation Compliance %: 
  =COUNTIF('Network Segmentation'!K:K, "Compliant") / 
   COUNTA('Network Segmentation'!K5:K103) * 100

Encryption Compliance %: 
  =COUNTIF('Encryption-Based Access'!L:L, "Compliant") / 
   COUNTA('Encryption-Based Access'!L5:L253) * 100

Overall Access Control Score: 
  =AVERAGE(OS%, DB%, App%, API%, Network%, Encryption%)
```

---

# Sheet 9: Evidence Register

Standard evidence tracking sheet.

---

# Sheet 10: Approval & Sign-Off

Three-level approval process.

---

# Python Script Integration

## Script Purpose

**Script:** `generate_a8235_5_access_restrictions.py`

## Running the Script

```bash
python3 generate_a8235_5_access_restrictions.py
```

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**END OF ISMS-IMP-A.8.2-3-5.5**

*Access restrictions are your last line of defense. Test them. Validate them. Trust, but verify.*

*Default deny is the way. Explicit allow is the rule.*

---

**END OF SPECIFICATION**

---

*"If a machine is expected to be infallible, it cannot also be intelligent."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
