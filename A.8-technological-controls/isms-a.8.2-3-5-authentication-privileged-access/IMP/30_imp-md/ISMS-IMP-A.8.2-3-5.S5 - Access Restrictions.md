**ISMS-IMP-A.8.2-3-5.5 - Access Restrictions Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S5 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Column Definitions
  - Formulas & Calculations
  - Python Script Integration

---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.2-3-5.5 - Access Restrictions Assessment

**What This Assessment Does:**

- Audits technical access control implementation across all layers
- Verifies operating system access controls (NTFS, ACLs, file permissions)
- Validates database access controls (SQL grants, roles, row-level security)
- Assesses application access controls (RBAC, ABAC, permission models)
- Tests API access controls (OAuth scopes, API keys, rate limiting)
- Evaluates network segmentation for access restriction
- Verifies default deny principle implementation
- Validates encryption-based access restriction (encryption at rest, in transit)
- Tests access control effectiveness (penetration testing, configuration scanning)

**What This Assessment Does NOT Do:**

- Manage user identities (see ISMS-POL-A.5.15-16-18 - IAM Foundation)
- Authenticate users (see IMP.1 - Authentication Inventory, IMP.2 - MFA Coverage)
- Track privileged accounts (see IMP.3 - Privileged Account Inventory)

**Primary ISO 27001 Control:** A.8.3 - Information Access Restriction

**Related Controls:**

- A.8.5 - Secure Authentication (authentication enables access)
- A.8.2 - Privileged Access Rights (privileged access restrictions)
- A.8.24 - Use of Cryptography (encryption-based access restriction)
- A.8.20 - Networks Security (network segmentation)

**Why Access Restrictions Matter:**
Authentication proves WHO you are. Access restrictions enforce WHAT you can access. Without effective access restrictions:

- Users access data outside their role (data breach risk)
- Applications access databases with excessive permissions (SQL injection = full database compromise)
- APIs allow unauthorized operations (business logic bypass)
- Network segmentation failures allow lateral movement

## When to Use This Assessment

**Use this assessment when:**

- Conducting quarterly access control reviews (compliance requirement)
- After major system deployments (new servers, applications, databases)
- After configuration changes (permission changes, firewall rules)
- Preparing for ISO 27001 certification audits
- After security incidents (access control bypass, unauthorized access)
- Demonstrating GDPR Article 32 compliance (security of processing)

**Assessment Frequency:**

- **Continuous**: Configuration monitoring via vulnerability scanners, CSPM tools
- **Quarterly**: Comprehensive access control audit, permission review
- **Annual**: Penetration testing (access control bypass testing), full compliance validation

## Who Completes This Assessment

**Primary Responsibility:** Security Team (security engineer, access control specialist)

**Supporting Roles:**

- **IT Operations**: System-level access controls (file permissions, OS hardening)
- **Database Administrators**: Database access controls (grants, roles)
- **Application Teams**: Application-level access controls (RBAC, permission models)
- **Network Team**: Network segmentation, firewall rules
- **Cloud Team**: Cloud IAM policies, resource access controls
- **System Owners**: Validate access controls for owned systems

**Approval Authority:** Chief Information Security Officer (CISO)

## Expected Time Investment

**Initial Assessment** (establishing baseline):

- System inventory and access control discovery: 6-8 hours
- OS permission audits: 4-6 hours
- Database grant audits: 3-4 hours
- Application access control review: 4-6 hours
- Network segmentation review: 2-3 hours
- Workbook completion: 2-3 hours
- Evidence collection: 2-3 hours
- **Total**: 23-33 hours (spread over 2-3 weeks)

**Quarterly Assessment**:

- Configuration audit updates: 3-4 hours
- Permission changes review: 2-3 hours
- Access control testing: 2-3 hours
- Workbook updates: 1-2 hours
- Evidence updates: 1-2 hours
- **Total**: 9-14 hours per quarter

**Continuous Monitoring** (ongoing):

- Automated configuration scanning (daily/weekly)
- Alert on permission changes (real-time)
- Quarterly manual validation

---

# Prerequisites

## Required Information

Before starting the assessment, gather the following information:

**System Inventory:**

- [ ] Complete list of systems requiring access controls (servers, databases, applications, APIs, network devices)
- [ ] Data classification per system (Public, Internal, Confidential, Restricted)
- [ ] System owners and responsible teams

**Access Control Configuration:**

- [ ] OS-level access controls (NTFS permissions, Linux ACLs)
- [ ] Database grants and roles (SQL Server, Oracle, PostgreSQL, MySQL, MongoDB)
- [ ] Application permission models (RBAC roles, permissions matrix)
- [ ] API access controls (OAuth scopes, API key policies)
- [ ] Network segmentation (firewall rules, VLANs, security groups)

**Encryption Configuration:**

- [ ] Encryption at rest status (BitLocker, LUKS, TDE, S3 encryption)
- [ ] Encryption in transit status (TLS, IPsec, VPN)
- [ ] Key management integration (which systems use encryption-based access)

**Baseline Expectations:**

- [ ] Expected access patterns (who should access what)
- [ ] Default deny configuration (explicit allow required)
- [ ] Least privilege implementation (minimal permissions)

## Required Access

**System Access Needed:**

- [ ] Read access to file systems (audit NTFS/ACL permissions)
- [ ] Read access to database catalogs (audit grants, roles)
- [ ] Read access to application configuration (permission models, RBAC)
- [ ] Read access to API gateway configuration (OAuth, API keys, rate limits)
- [ ] Read access to network configuration (firewall rules, security groups)
- [ ] Read access to encryption configuration (BitLocker, TDE status)

**People Access Needed:**

- [ ] System owners (validate access control intent)
- [ ] DBAs (database permission review)
- [ ] Application teams (application access control review)
- [ ] Network team (firewall rule review)

## Required Tools

**Software:**

- [ ] Microsoft Excel 2016 or later
- [ ] Python 3.8+ (if using automated workbook generation)
- [ ] Configuration audit tools (Nessus, Qualys, Microsoft Defender for Cloud, AWS Config)
- [ ] Permission analysis tools (AccessChk, PowerShell, SQL scripts)

**Optional Tools:**

- [ ] Penetration testing tools (for access control bypass testing)
- [ ] CSPM (Cloud Security Posture Management) tools
- [ ] Database audit tools (DBDefence, Imperva)

---

# Assessment Workflow

## Assessment Process Overview

```
1. PREPARE
   → Inventory systems requiring access controls
   → Classify data per system (determines required controls)
   → Generate workbook (Python script or Excel template)

2. AUDIT OPERATING SYSTEM ACCESS CONTROLS
   → Sheet 1: OS Access Controls

      - NTFS permissions (Windows)
      - File system ACLs (Linux: ext4, XFS, ZFS)
      - Default permissions (umask, default ACLs)
      - Permission inheritance

3. AUDIT DATABASE ACCESS CONTROLS
   → Sheet 2: Database Access Controls

      - SQL grants (SELECT, INSERT, UPDATE, DELETE)
      - Database roles and privileges
      - Row-level security (if applicable)
      - Column-level security (if applicable)

4. AUDIT APPLICATION ACCESS CONTROLS
   → Sheet 3: Application Access Controls

      - RBAC implementation (roles, permissions)
      - Application-level permissions (read, write, delete, admin)
      - Permission enforcement (backend + frontend)

5. AUDIT API ACCESS CONTROLS
   → Sheet 4: API Access Controls

      - OAuth scope enforcement
      - API key management
      - Rate limiting and throttling
      - API authentication requirements

6. VERIFY NETWORK SEGMENTATION
   → Sheet 5: Network Segmentation

      - Network zones (DMZ, Internal, Management, Database)
      - Firewall rules enforcing restrictions
      - VLAN segmentation

7. VERIFY ENCRYPTION-BASED RESTRICTION
   → Sheet 6: Encryption-Based Access

      - Encryption at rest (who has keys = who has access)
      - Encryption in transit (TLS enforcement)
      - Key-based access control

8. TEST ACCESS CONTROL EFFECTIVENESS
   → Penetration testing (access control bypass attempts)
   → Configuration compliance scanning

9. COLLECT EVIDENCE
   → Permission audit exports
   → Firewall rule exports
   → Penetration test reports

10. REVIEW & APPROVE
   → Security Team review
   → System Owner validation
   → CISO approval
```

## Step-by-Step Completion Guide

**Step 1: Generate Workbook**

Option A - Automated (Recommended):
```bash
python3 generate_a8235_5_access_restrictions.py
```
This creates: `ISMS-IMP-A.8.2-3-5.5_Access_Restrictions_YYYYMMDD.xlsx`

Option B - Manual:

- Use Excel template
- Save as: `ISMS-IMP-A.8.2-3-5.5_Access_Restrictions_[DATE].xlsx`

**Step 2: Complete Sheet 1 - OS Access Controls**

For each system with OS-level access controls:

1. **System Identification** (Columns A-D):

   - System ID: Unique identifier
   - System Name: Full name
   - Operating System: Windows Server, Linux (distro), macOS
   - Data Classification: Public, Internal, Confidential, Restricted

2. **Access Control Type** (Columns E-G):

   - Access Control Type: NTFS, ext4 ACL, XFS ACL, ZFS ACL, NFS ACL
   - Default Deny Configured: Yes, No (requires explicit allow?)
   - Permission Inheritance: Yes, No (do subfolders inherit?)

3. **Permission Audit** (Columns H-K):

   - Last Audit Date: When permissions reviewed
   - Excessive Permissions Found: Yes, No (users with broader access than needed)
   - Permission Cleanup Completed: Yes, No, N/A
   - Compliance Status: Compliant, Non-Compliant

4. **Evidence** (Column L):

   - Evidence Location: Link to permission audit export

**Example - Windows File Server:**
```
System: FILE-SRV-01
OS: Windows Server 2022
Data Classification: Confidential
Access Control: NTFS
Default Deny: Yes (no Everyone group permissions)
Excessive Permissions: No
Compliance: Compliant
```

**Step 3: Complete Sheet 2 - Database Access Controls**

For each database:

1. **Database Identification** (Columns A-D):

   - Database ID
   - Database Name
   - Database Type: SQL Server, Oracle, PostgreSQL, MySQL, MongoDB, other
   - Data Classification

2. **Access Control Implementation** (Columns E-H):

   - Role-Based Access: Yes, No (database roles used?)
   - Least Privilege: Yes, No (minimal grants?)
   - Row-Level Security: Yes, No, N/A
   - Column-Level Security: Yes, No, N/A

3. **Grant Audit** (Columns I-L):

   - Last Grant Audit Date
   - Excessive Grants Found: Yes, No (users with more than SELECT on sensitive tables?)
   - Public Role Grants: Yes - Review, No (dangerous: grants to PUBLIC)
   - Compliance Status: Compliant, Non-Compliant

**Example - SQL Server Database:**
```
Database: SALES-DB
Type: SQL Server 2022
Data Classification: Confidential
Role-Based Access: Yes (db_datareader, db_datawriter, custom roles)
Least Privilege: Yes
Excessive Grants: No
Public Role Grants: No
Compliance: Compliant
```

**Step 4: Complete Sheet 3 - Application Access Controls**

For each application:

1. **Application Identification** (Columns A-D):

   - Application ID
   - Application Name
   - Application Type: Web App, Desktop App, Mobile App, API
   - Data Classification

2. **Access Control Model** (Columns E-H):

   - Access Control Model: RBAC, ABAC, ACL, Custom
   - Roles Defined: Yes, No (are roles documented?)
   - Permissions Matrix: Yes, No (is permission model documented?)
   - Enforcement: Backend Only, Frontend Only, Both (where is access checked?)

3. **Access Control Testing** (Columns I-K):

   - Last Access Control Test: Date of last test (pen test, security test)
   - Access Control Bypass Found: Yes, No (vulnerabilities discovered?)
   - Remediation Completed: Yes, No, N/A
   - Compliance Status: Compliant, Non-Compliant

**Example - Web Application:**
```
Application: INTRANET-PORTAL
Type: Web Application
Access Control Model: RBAC
Roles: Yes (Admin, Manager, User)
Enforcement: Both (backend API + frontend UI)
Last Test: 15.12.2025 (penetration test)
Bypass Found: No
Compliance: Compliant
```

**Step 5: Complete Sheet 4 - API Access Controls**

For each API:

1. **API Identification** (Columns A-D):

   - API ID
   - API Name
   - API Type: REST, GraphQL, SOAP, gRPC
   - Data Classification

2. **Authentication & Authorization** (Columns E-H):

   - Authentication Method: OAuth 2.0, API Key, JWT, mTLS, None
   - Authorization Model: OAuth Scopes, API Key Permissions, Role-Based
   - Rate Limiting: Yes, No (requests per minute/hour limited?)
   - Rate Limit Value: [requests/minute]

3. **Access Control Testing** (Columns I-K):

   - Last API Security Test
   - IDOR Vulnerability: Yes, No (Insecure Direct Object Reference - can users access other users' data?)
   - Broken Access Control: Yes, No (OWASP Top 10 A01:2021)
   - Compliance Status: Compliant, Non-Compliant

**Example - REST API:**
```
API: CUSTOMER-API
Type: REST API
Authentication: OAuth 2.0
Authorization: OAuth Scopes (read:customers, write:customers)
Rate Limiting: Yes (100 req/min per API key)
Last Test: 10.01.2026
IDOR: No
Compliance: Compliant
```

**Step 6: Complete Sheet 5 - Network Segmentation**

For each network zone:

1. **Network Zone** (Columns A-C):

   - Zone Name: DMZ, Internal, Management, Database, Guest
   - Zone Purpose: Purpose of this network segment
   - Data Classification: What sensitivity of data resides here?

2. **Segmentation Implementation** (Columns D-G):

   - Segmentation Method: Firewall, VLAN, Security Group, Subnet
   - Firewall Rules: Yes, No (firewall rules enforcing restrictions?)
   - Default Deny: Yes, No (deny all, allow specific?)
   - VLAN Segmentation: Yes, No, N/A

3. **Segmentation Effectiveness** (Columns H-J):

   - Last Rule Review Date
   - Unnecessary Rules Found: Yes, No (overly permissive rules?)
   - Segmentation Tested: Yes, No (penetration tested?)
   - Compliance Status: Compliant, Non-Compliant

**Example - Database Network Zone:**
```
Zone: DATABASE-ZONE
Purpose: Database servers
Data Classification: Confidential
Segmentation: VLAN + Security Group
Firewall: Yes (only application servers allowed to connect)
Default Deny: Yes
Last Review: 05.01.2026
Unnecessary Rules: No
Compliance: Compliant
```

**Step 7: Complete Sheet 6 - Cloud IAM Policies**

For cloud platforms (AWS, Azure, GCP) access control policies:

1. **Cloud Service Identification** (Columns A-D):

   - Cloud Platform: AWS, Azure, GCP
   - Service Name: EC2, RDS, S3, Entra ID, KeyVault, Compute Engine, Storage
   - Resource Count: Number of resources with IAM policies
   - Data Classification: Data sensitivity in service

2. **IAM Policy Implementation** (Columns E-H):

   - Least Privilege Enforced: Yes, No (minimal permissions?)
   - Service Principal Grants: Documented? (who/what has access?)
   - Default Deny: Yes, No (deny all, allow specific?)
   - MFA on API Access: Yes, No, N/A

3. **Compliance** (Columns I-J):

   - Last Policy Audit Date
   - Compliance Status: Compliant, Non-Compliant

**Example - Azure Storage Account:**
```
Platform: Azure
Service: Storage Account
Least Privilege: Yes (specific roles per application)
Default Deny: Yes (private endpoints only)
MFA on Access: Yes (Conditional Access enforced)
Compliance: Compliant
```

**Step 8: Complete Sheet 7 - Encryption-Based Access**

For systems using encryption as access control:

1. **System Identification** (Columns A-D):

   - System ID
   - System Name
   - System Type
   - Data Classification

2. **Encryption at Rest** (Columns E-H):

   - Encryption at Rest: Yes, No
   - Encryption Type: BitLocker, LUKS, TDE, AWS KMS, Azure SSE, Other
   - Key Management: Who has keys? (defines access)
   - Encryption Required: Yes, No (per data classification policy)

3. **Encryption in Transit** (Columns I-K):

   - Encryption in Transit: Yes, No
   - Protocol: TLS 1.2, TLS 1.3, IPsec, VPN
   - TLS Enforcement: Mandatory, Optional, None

4. **Compliance** (Column L):

   - Compliance Status: Compliant, Non-Compliant

**Example - File Server with Encryption:**
```
System: FILE-SRV-01
Data Classification: Confidential
Encryption at Rest: Yes (BitLocker)
Key Management: IT Operations (only authorized admins have recovery keys)
Encryption in Transit: Yes (SMB3 encryption)
TLS Enforcement: Mandatory
Compliance: Compliant
```

**Step 9: Complete Sheet 8 - Network Segmentation**

For network zone configuration and verification (detailed guidance in Part I Assessment Workflow, Step 5).

**Step 10: Complete Sheet 9 - Penetration Test Results**

For access control security testing findings:

1. **Test Information** (Columns A-D):

   - Test Date: When penetration test was performed
   - Test Scope: OS Permissions, Database Grants, Application RBAC, API Security, Network Segmentation, All
   - Tester: Security firm or internal team
   - Systems Tested: Count

2. **Finding Results** (Columns E-H):

   - Access Control Bypass: Yes, No (vulnerabilities found?)
   - IDOR Vulnerabilities: Yes, No (insecure direct object reference)
   - Privilege Escalation: Yes, No (ability to escalate privileges?)
   - Finding Count: Total vulnerabilities

3. **Remediation** (Columns I-K):

   - Critical Findings: Count (immediate action)
   - High Findings: Count (within 30 days)
   - Remediation Status: Not Started, In Progress, Completed
   - Follow-up Test Date: Scheduled retest

**Example - Web Application Penetration Test:**
```
Test Date: 15.01.2026
Scope: Application RBAC and API Security
Tester: External Security Firm
Access Bypass: No
IDOR Found: No
Privilege Escalation: No
Findings: 0
Remediation: Completed
Compliance: Passed
```

**Step 11: Review Calculated Metrics**

The workbook automatically calculates:

- **OS Access Control Compliance**: % of systems with compliant OS permissions
- **Database Access Control Compliance**: % of databases with least privilege
- **Application Access Control Compliance**: % of applications with tested access controls
- **API Security Compliance**: % of APIs with authentication + rate limiting
- **Network Segmentation Compliance**: % of zones with firewall rules + default deny
- **Encryption Compliance**: % of systems with required encryption
- **Cloud IAM Compliance**: % of cloud services with least privilege policies
- **Penetration Test Compliance**: Access control vulnerabilities identified and remediated

**Step 12: Collect Evidence**

Required evidence:

- **OS Permission Audits**: PowerShell `Get-Acl` exports, Linux `getfacl` exports
- **Database Grant Audits**: SQL query results showing grants per user/role
- **Application Access Control Documentation**: RBAC role definitions, permission matrix
- **API Security Configuration**: OAuth scope definitions, rate limit configuration
- **Firewall Rules**: Export of firewall rules per zone
- **Encryption Configuration**: BitLocker/LUKS status reports, TDE configuration

Store evidence in: `/evidence/access-restrictions/[date]/`

**Step 13: Complete Evidence Register (Sheet 11)**

Document all collected evidence with links.

**Step 14: Approval & Sign-Off (Sheet 12)**

Three-level approval process.

---

# Evidence Collection Guidelines

## Required Evidence Types

**For OS Access Controls:**

1. **Windows NTFS Permissions**:
```powershell
# Export NTFS permissions for sensitive folders
Get-ChildItem "D:\Data" -Recurse | 
  Get-Acl | 
  Select Path, Owner, @{N='Access';E={$_.Access | Out-String}} | 
  Export-Csv "ntfs-permissions.csv"
```

2. **Linux ACLs**:
```bash
# Export ACLs for sensitive directories
getfacl -R /data > acl-permissions.txt
```

**For Database Access Controls:**

```sql
-- SQL Server: Export database grants
SELECT 
  dp.name AS Principal,
  dp.type_desc,
  o.name AS ObjectName,
  p.permission_name,
  p.state_desc
FROM sys.database_permissions p
JOIN sys.database_principals dp ON p.grantee_principal_id = dp.principal_id
LEFT JOIN sys.objects o ON p.major_id = o.object_id
ORDER BY dp.name;
```

**For Firewall Rules:**

```bash
# Export iptables rules (Linux)
iptables-save > firewall-rules.txt

# Export Azure NSG rules
az network nsg rule list --resource-group RG --nsg-name NSG --output table

# Export AWS Security Group rules
aws ec2 describe-security-groups --group-ids sg-12345 --output json
```

## Evidence Storage

**Structure:**
```
/evidence/access-restrictions/
├── 2026-01-22/
│   ├── os-permissions/
│   │   ├── file-srv-01-ntfs-permissions.csv
│   │   └── web-srv-01-acl-permissions.txt
│   ├── database-grants/
│   │   ├── sales-db-grants.csv
│   │   └── customer-db-roles.csv
│   ├── application-access/
│   │   ├── intranet-rbac-roles.pdf
│   │   └── customer-portal-permissions-matrix.xlsx
│   ├── api-security/
│   │   ├── customer-api-oauth-scopes.json
│   │   └── partner-api-rate-limits.png
│   ├── network-segmentation/
│   │   ├── firewall-rules-database-zone.txt
│   │   └── azure-nsg-rules.json
│   └── encryption/
│       ├── bitlocker-status-report.csv
│       └── sql-tde-configuration.png
└── penetration-tests/
    └── 2025-Q4-pentest-access-control-findings.pdf
```

## Evidence Quality Checklist

For each piece of evidence:

- [ ] Timestamp visible
- [ ] System identified
- [ ] Data matches workbook
- [ ] Sensitive data redacted (passwords, keys)
- [ ] Linked in Evidence Register

---

# Common Pitfalls & How to Avoid Them

## Pitfall 1: Focusing Only on Authentication, Ignoring Authorization

**Problem**: MFA is deployed (authentication), but users can access any data (authorization failure)

**Solution**:

- Authentication ≠ Authorization
- Authentication = WHO are you?
- Authorization = WHAT can you access?
- Both are required

## Pitfall 2: "Everyone" Group with Permissions

**Problem**: Windows file server has "Everyone" group with Read access (any authenticated user can read)

**Solution**:

- Remove "Everyone" group
- Use specific security groups
- Default deny: No permissions by default, explicitly grant to specific groups

## Pitfall 3: Database "PUBLIC" Role with Grants

**Problem**: SQL Server PUBLIC role has SELECT on sensitive tables (all database users can read)

**Solution**:

- Review PUBLIC role grants
- PUBLIC should have minimal permissions (CONNECT only)
- Grant specific permissions to specific roles

## Pitfall 4: Application Frontend-Only Access Controls

**Problem**: Application UI hides "Delete" button from non-admins, but API endpoint allows delete (Insecure Direct Object Reference)

**Solution**:

- Enforce access controls in BACKEND (API, database)
- Frontend controls are convenience, NOT security
- Test: Can user call API directly and bypass UI?

## Pitfall 5: API Authentication Without Authorization

**Problem**: API requires authentication (API key), but all API keys have same permissions

**Solution**:

- OAuth scopes (read-only API key vs. read-write)
- API key permissions (per-key access control)
- Rate limiting per API key

## Pitfall 6: Overly Permissive Firewall Rules

**Problem**: Firewall rule "Allow Any → Database Server:3306" (anyone can connect to database)

**Solution**:

- Specify source: "Allow Application Servers → Database Server:3306"
- Default deny: Deny all, allow specific
- Review quarterly: Are all rules still necessary?

## Pitfall 7: Not Testing Access Controls

**Problem**: Assuming access controls work without testing

**Solution**:

- Penetration testing: Can attacker bypass access controls?
- Functional testing: Can user access data outside their role?
- Automated testing: Configuration scanning (excessive permissions)

## Pitfall 8: Encryption Without Key Management

**Problem**: Database encrypted with TDE, but database service account has access to keys (encryption doesn't restrict access)

**Solution**:

- Encryption protects data AT REST (disk theft, backup theft)
- Encryption does NOT restrict application access (if app has key)
- Use encryption + access controls (both required)

## Pitfall 9: Not Documenting Access Control Model

**Problem**: Application has RBAC, but roles and permissions not documented (how do we audit?)

**Solution**:

- Document roles: Admin, Manager, User (what can each do?)
- Document permissions matrix: Role → Permission mapping
- Keep documentation updated

## Pitfall 10: Legacy Systems with Weak Access Controls

**Problem**: Old application doesn't support RBAC (all users are admins or users, nothing in between)

**Solution**:

- Compensating controls: Network segmentation (limit who can access), enhanced monitoring
- Migration plan: Migrate to modern application with proper RBAC
- Risk acceptance: Document risk, CISO approval

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All systems with access controls inventoried
- [ ] OS permissions audited (file servers, application servers)
- [ ] Database grants audited (all production databases)
- [ ] Application access controls reviewed
- [ ] API security assessed
- [ ] Network segmentation verified
- [ ] Encryption-based access documented

## Accuracy

- [ ] Permission audit data validated (spot-check actual permissions)
- [ ] Data classification correct per system
- [ ] Access control models accurately documented
- [ ] Firewall rules reviewed with network team
- [ ] Encryption status verified (not assumed)

## Evidence Quality

- [ ] Permission audit exports collected
- [ ] Database grant queries executed and exported
- [ ] Firewall rule exports collected
- [ ] Penetration test reports linked (if available)
- [ ] Evidence dated and linked

## Compliance

- [ ] Systems with excessive permissions flagged
- [ ] Databases with PUBLIC role grants flagged
- [ ] Applications with untested access controls flagged
- [ ] APIs without rate limiting flagged
- [ ] Unencrypted confidential data flagged

## Professional Presentation

- [ ] No spelling errors
- [ ] Consistent formatting
- [ ] Clear and concise notes
- [ ] Evidence clearly linked

---

# Interpreting Results

## Understanding Access Control Metrics

**OS Access Control Compliance:**

- **90-100%**: Excellent - Proper OS permissions across systems
- **75-89%**: Good - Most systems compliant, some cleanup needed
- **<75%**: POOR - Widespread permission issues

**Database Access Control Compliance:**

- **100%**: Ideal - Least privilege everywhere
- **90-99%**: Good - Minor excessive grants
- **<90%**: CONCERN - Significant excessive grants (data breach risk)

**Application Access Control Effectiveness:**

- **100% tested, 0% bypass**: Excellent
- **80-99% tested, low bypass**: Good
- **<80% tested or high bypass rate**: CRITICAL - Major access control gaps

**API Security Score:**

- **100%**: All APIs with auth + authz + rate limiting
- **80-99%**: Most APIs secure
- **<80%**: HIGH RISK - API security gaps

**Network Segmentation Effectiveness:**

- **100%**: All zones segmented with firewall rules
- **80-99%**: Minor segmentation gaps
- **<80%**: POOR - Network segmentation not enforced

## Gap Prioritization

**Priority 1 - CRITICAL (Immediate Action - Within 7 Days):**

- Database PUBLIC role with SELECT on sensitive tables
- Application access control bypass vulnerability
- API without authentication (public API unintentionally)
- Confidential data unencrypted on disk
- Firewall rule allowing ANY → sensitive system

**Priority 2 - HIGH (Within 30 Days):**

- Excessive OS permissions (too many users with write access)
- Database user with more grants than needed (DBA privileges for application account)
- Application without RBAC (all users have same permissions)
- API without rate limiting (DoS risk)
- Network zone without segmentation

**Priority 3 - MEDIUM (Within 90 Days):**

- Permission cleanup (remove orphaned permissions)
- Application access controls not tested recently (>1 year)
- API with weak authentication (API key only, no OAuth)

**Priority 4 - LOW (Ongoing Improvement):**

- Documentation improvements (RBAC model documentation)
- Permission audit automation
- Enhanced monitoring

---

# Review & Approval Process

## Approval Workflow

**Level 1 - Preparer (Security Team)**:

- Audit access controls across all layers
- Collect permission audit data
- Test access control effectiveness
- Complete assessment workbook
- Collect evidence
- Submit for review

**Level 2 - Reviewer (Senior Security Engineer / System Owner)**:

- Validate access control configurations
- Verify permission audit accuracy
- Review gap prioritization
- Confirm evidence completeness
- Approve and forward to CISO

**Level 3 - Approver (CISO)**:

- Review access control metrics
- Validate critical gaps identified
- Approve remediation priorities
- Sign off on assessment
- Present to Executive Management (if required)

## Approval Criteria

Assessment is approved when:

- [ ] All systems with access controls audited
- [ ] Permission audits completed
- [ ] Access control effectiveness tested (or test planned)
- [ ] Critical gaps identified and prioritized
- [ ] Evidence collected and linked
- [ ] Remediation timeline defined

## Post-Approval Actions

After CISO approval:
1. **Communicate Gaps**: Notify system owners of access control issues
2. **Escalate Critical**: PUBLIC role grants, access control bypasses escalated immediately
3. **Track Remediation**: Move gaps to Dashboard (IMP.6)
4. **Schedule Next Review**: Quarterly access control audit

---

# PART II: TECHNICAL SPECIFICATION

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

<!-- QA_VERIFIED: 2026-01-31 -->
