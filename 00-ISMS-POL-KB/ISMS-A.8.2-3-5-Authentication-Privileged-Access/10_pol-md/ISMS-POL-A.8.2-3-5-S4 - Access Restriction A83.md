# ISMS-POL-A.8.2-3-5-S4
## Information Access Restriction Requirements (A.8.3)

**Document ID**: ISMS-POL-A.8.2-3-5-S4  
**Title**: Information Access Restriction Requirements (ISO/IEC 27001:2022 Control A.8.3)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial information access restriction requirements (A.8.3) |

**Review Cycle**: Annual  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Architect
- Systems Review: Systems Administration Manager
- Database Review: Database Administration Lead

**Distribution**: Security team, systems administrators, database administrators, application owners, developers, auditors  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 (Executive Summary)
- ISMS-POL-A.8.2-3-5-S2 (Authentication - A.8.5)
- ISMS-IMP-A.8.2-3-5-S4 (Access Enforcement Implementation)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.3

**Official Control Text**:

> *Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.*

**Control Purpose**: Ensure technical access controls (file permissions, database grants, API scopes, encryption) enforce the access control policy defined in A.5.15, implementing principle of least privilege at the technical layer.

**Why This Matters**:

Access restriction is the **last line of defense**. Even with perfect authentication (A.8.5) and privileged access controls (A.8.2), misconfigured permissions allow unauthorized access:

- **Misconfigured file permissions** = data exposed to unauthorized users
- **Overly permissive database grants** = applications can read/write unintended data
- **Missing default deny** = accidental access (everyone can access everything)
- **No encryption** = data readable if access controls bypassed

Proper access restriction provides:
- **Defense in depth** - multiple layers of access controls
- **Principle of least privilege** enforced technically (not just policy)
- **Audit trail** of access attempts (successful and denied)
- **Containment** - lateral movement blocked even if one system compromised

### 1.2 Scope of A.8.3 Requirements

This section defines mandatory requirements for:

1. **Operating System Access Controls** - File permissions (NTFS, ACLs)
2. **Database Access Controls** - SQL grants, row/column-level security
3. **Application Access Controls** - RBAC, ABAC within applications
4. **API Access Controls** - OAuth scopes, API keys, rate limiting
5. **Cloud Resource Access Controls** - IAM policies (AWS, Azure, GCP)
6. **Data Classification Enforcement** - Encryption based on sensitivity
7. **Network Segmentation** - Firewalls between zones
8. **Default Deny Principle** - Explicit allow required
9. **Access Control Testing** - Penetration testing, configuration audits

---

## 2. Operating System Access Controls

### 2.1 Requirement: File System Permissions

**REQ-A83-001**: File system permissions **MUST** implement principle of least privilege with default deny.

**File System Permission Requirements**:

**Windows (NTFS)**:
- **Default permissions**: Deny all, explicit allow required
- **Permission types**: Read, Write, Modify, Full Control
- **Permission inheritance**: Properly configured (child folders inherit parent permissions)
- **Special permissions**: Limited use (require justification and approval)
- **Auditing**: Log access to sensitive directories

**Linux (ext4, XFS, ZFS)**:
- **Default permissions**: 644 files (rw-r--r--), 755 directories (rwxr-xr-x)
- **Sensitive data**: 600 files (rw-------), 700 directories (rwx------)
- **ACLs**: Use Access Control Lists for complex permission requirements
- **SELinux/AppArmor**: Mandatory Access Control for high-security systems
- **sudo**: Logged and monitored (see A.8.2 privileged access)

**Permission Assignment**:
- **User permissions**: Individual users only when necessary (prefer groups)
- **Group permissions**: Use AD groups (finance-team, hr-team, engineering-team)
- **Everyone/Authenticated Users**: NEVER grant write access to these groups
- **Service accounts**: Grant only permissions required for application function

**Prohibited Practices**:
- ❌ Full Control granted to Users or Everyone groups
- ❌ Write permissions to system directories (C:\Windows, /etc, /usr/bin)
- ❌ Executable permissions on data directories
- ❌ Permission inheritance disabled without justification

**Audit Evidence**: Sample file permissions from critical systems, permission audit logs (Workbook 5)

### 2.2 Requirement: Permission Management

**REQ-A83-002**: File system permissions **MUST** be documented, reviewed, and audited.

**Permission Documentation**:
- **Permission matrix**: Document which groups have access to which shares/directories
- **Business justification**: Why does this group need access?
- **Permission templates**: Standard permission sets for common scenarios (department share, project share, etc.)

**Regular Permission Audits**:
- **Frequency**: Quarterly for sensitive data, annually for standard data
- **Automated scanning**: PowerShell scripts (Get-Acl), Linux scripts (getfacl)
- **Manual review**: Review permissions on high-value directories
- **Cleanup**: Remove permissions for users no longer needing access

**Permission Change Control**:
- **Approval required**: Manager approval for adding permissions to sensitive directories
- **Change logging**: All permission changes logged (Windows Event ID 4670, Linux auditd)
- **Review**: Quarterly review of permission changes

**Audit Evidence**: Permission matrix, audit reports (Workbook 5), permission change logs

---

## 3. Database Access Controls

### 3.1 Requirement: Database Permissions and Grants

**REQ-A83-003**: Database access **MUST** use principle of least privilege with specific grants.

**Database Permission Requirements**:

**SQL Databases** (SQL Server, PostgreSQL, MySQL, Oracle):
- **Grant specific privileges only**: SELECT, INSERT, UPDATE, DELETE (not ALL PRIVILEGES)
- **Schema-level grants**: Grant on specific schemas/databases, not server-wide
- **Table-level grants**: For sensitive tables, grant specific access (not entire schema)
- **Row-level security**: Implement where users should only see subset of data (e.g., sales reps see only their accounts)
- **Column-level security**: Hide sensitive columns from standard users (e.g., salary, SSN)

**NoSQL Databases** (MongoDB, Cassandra, DynamoDB):
- **Database-specific roles**: Create custom roles with minimal privileges
- **Collection/table-level permissions**: Not database-wide admin access
- **Read-only users**: Applications that only need read access get read-only credentials

**Database Account Types**:

1. **Application Service Accounts**:
   - Grant ONLY privileges required for application function
   - Typical: SELECT, INSERT, UPDATE on specific tables (NOT DELETE, DROP)
   - Never grant: CREATE, ALTER, DROP (DDL privileges)
   - Never grant: GRANT OPTION (ability to grant privileges to others)

2. **Database Administrators (DBAs)**:
   - Full privileges on database servers (covered in A.8.2 privileged access)
   - Named DBA accounts (john.dba), not shared "sa" or "root"
   - MFA required, session recorded

3. **Data Analysts / Read-Only Users**:
   - SELECT privilege only
   - Access only to non-sensitive tables or anonymized views
   - Connection from specific IP addresses only (if possible)

**Prohibited Practices**:
- ❌ Granting "db_owner" or "ALL PRIVILEGES" to application accounts
- ❌ Using "sa" or "SYSTEM" accounts for applications
- ❌ Granting "GRANT OPTION" to non-DBAs
- ❌ Shared database credentials across multiple applications

**Audit Evidence**: Database grant reports (SQL queries showing grants), permission reviews (Workbook 5)

### 3.2 Requirement: Database Permission Auditing

**REQ-A83-004**: Database permissions **MUST** be audited regularly.

**Database Audit Procedures**:

**Monthly Audits**:
- Query database for all grants: `SELECT * FROM information_schema.table_privileges` (PostgreSQL)
- Review users with excessive privileges (db_owner, ALL PRIVILEGES)
- Review users with DDL privileges (CREATE, ALTER, DROP)
- Review users with GRANT OPTION
- Alert on new privileged users

**Quarterly Audits**:
- Full permission review for all application accounts
- Verify permissions match application requirements documentation
- Remove unused accounts (accounts with no connections in 90 days)
- Review service account permissions (still need this access?)

**Database Audit Logging**:
- Enable database audit logging (SQL Server Audit, Oracle Audit, PostgreSQL pgaudit)
- Log: Privileged access (sa, SYSTEM), DDL changes (DROP TABLE), sensitive data access
- Forward logs to SIEM for monitoring

**Audit Evidence**: Database permission audit reports, unused account cleanup logs (Workbook 5)

---

## 4. Application Access Controls

### 4.1 Requirement: Role-Based Access Control (RBAC)

**REQ-A83-005**: Applications **MUST** implement role-based access control aligned with business roles.

**RBAC Requirements**:

**Role Definition**:
- Define application roles based on business functions (not technical roles)
- Examples: "Sales Manager", "Customer Service Rep", "Finance Analyst", "HR Admin"
- Each role has specific permissions within application (read, write, approve, delete)

**Permission Assignment**:
- Users assigned to roles (user → role → permissions)
- Roles assigned based on job function (documented in access request)
- Regular review: Quarterly review of user-role assignments

**RBAC Best Practices**:
- **Separation of duties**: High-risk transactions require multiple roles (maker-checker)
- **Least privilege**: Roles have minimum permissions for job function
- **Role hierarchy**: Senior roles inherit junior role permissions (if appropriate)
- **Default deny**: New roles start with no permissions, add as needed

**Application-Specific RBAC Examples**:

**ERP Systems** (SAP, Oracle EBS):
- Complex role structure (hundreds of roles)
- Segregation of Duties (SoD) rules enforced (e.g., cannot create vendor AND approve payment)
- Regular SoD audits

**CRM Systems** (Salesforce):
- Profiles and permission sets
- Record-level access (user sees only their accounts)
- Field-level security (hide sensitive fields from standard users)

**Custom Applications**:
- Application-defined roles
- Permission checks at business logic layer (not just UI layer)
- API endpoints enforce same permissions as web UI

**Audit Evidence**: Application role matrix, user-role assignments, RBAC configuration (Workbook 5)

### 4.2 Requirement: Attribute-Based Access Control (ABAC)

**REQ-A83-006**: Applications **MAY** implement attribute-based access control for complex requirements.

**ABAC Concept**:

Access decisions based on attributes:
- **User attributes**: Department, job title, clearance level, location
- **Resource attributes**: Data classification, owner, project
- **Environmental attributes**: Time of day, network location, device type

**ABAC Examples**:

Example 1 - Data Classification:
- **Rule**: Users can access "Confidential" data only if: (user.clearance == "Confidential" OR "Restricted") AND (user.department == data.owner_department OR user.role == "Executive")

Example 2 - Time-Based Access:
- **Rule**: Contractors can access systems only during business hours (8 AM - 6 PM, Monday-Friday)

Example 3 - Location-Based Access:
- **Rule**: Access to financial systems allowed only from corporate network or VPN (not public Wi-Fi)

**ABAC vs. RBAC**:
- **RBAC**: Simpler, easier to manage, suitable for most applications
- **ABAC**: More flexible, handles complex rules, suitable for high-security environments

**Audit Evidence**: ABAC policy documentation, attribute definitions, access decision logs

---

## 5. API Access Controls

### 5.1 Requirement: API Authentication and Authorization

**REQ-A83-007**: APIs **MUST** implement authentication and authorization with scoped access.

**API Access Control Requirements**:

**API Authentication Methods**:
1. **OAuth 2.0** (preferred for user-facing APIs):
   - Client credentials flow (machine-to-machine)
   - Authorization code flow (user authorization)
   - Access tokens (JWT tokens)

2. **API Keys**:
   - Unique API key per application/client
   - API key rotation (every 90 days)
   - API key revocation capability

3. **Certificate-Based** (mTLS):
   - Client certificates for high-security APIs
   - Mutual TLS authentication

**API Authorization** (OAuth Scopes):
- **Scope-based access**: Define scopes for API endpoints (read:users, write:orders, delete:accounts)
- **Least privilege**: Grant only scopes required for client application function
- **Scope validation**: API endpoints verify client has required scope

**API Rate Limiting**:
- **Purpose**: Prevent abuse, DoS attacks, brute force attempts
- **Limits**: Per API key or per user (e.g., 1000 requests/hour)
- **Response**: HTTP 429 Too Many Requests when limit exceeded

**API Security Controls**:
- **Input validation**: Validate all API inputs (prevent SQL injection, XSS)
- **Output encoding**: Encode API responses (prevent XSS)
- **HTTPS only**: APIs accessible only via HTTPS (not HTTP)
- **CORS policy**: Restrict cross-origin requests to authorized domains

**Prohibited Practices**:
- ❌ APIs without authentication ("public" APIs for sensitive data)
- ❌ API keys in client-side code (JavaScript, mobile apps)
- ❌ Long-lived API keys (no rotation)
- ❌ Broad scopes ("admin" scope for standard users)

**Audit Evidence**: API authentication configuration, OAuth scope definitions, API rate limiting logs (Workbook 5)

### 5.2 Requirement: API Access Logging and Monitoring

**REQ-A83-008**: API access **MUST** be logged and monitored for security incidents.

**API Logging Requirements**:
- **Successful API calls**: User/client, endpoint, timestamp, response code
- **Failed API calls**: User/client, endpoint, timestamp, failure reason (401, 403)
- **Rate limit violations**: Client exceeding rate limits
- **Suspicious patterns**: Brute force attempts, data scraping, unusual access patterns

**API Monitoring Alerts**:
- Alert on: 100+ failed API calls in 5 minutes (brute force)
- Alert on: API access from unusual locations
- Alert on: Spike in API calls (potential DoS or data exfiltration)

**Audit Evidence**: API access logs, monitoring alerts, API security incidents

---

## 6. Cloud Resource Access Controls

### 6.1 Requirement: Cloud IAM Policies

**REQ-A83-009**: Cloud resource access **MUST** use Identity and Access Management (IAM) policies with least privilege.

**Cloud IAM Best Practices**:

**AWS IAM**:
- **Policy structure**: User → Group → IAM Policy → AWS Resources
- **Least privilege**: Grant only actions required (ec2:DescribeInstances, not ec2:*)
- **Resource-level permissions**: Grant access to specific resources (specific S3 bucket, not all buckets)
- **Conditions**: Use conditions for additional security (MFA required, source IP restrictions)
- **Managed policies**: Use AWS Managed Policies where appropriate (reduces management overhead)
- **Service Control Policies (SCPs)**: Organization-level guardrails

**Azure RBAC**:
- **Role assignment**: User → Azure AD Group → Azure Role → Subscription/Resource Group
- **Built-in roles**: Use built-in roles (Reader, Contributor, Owner) where possible
- **Custom roles**: Create custom roles for specific needs (principle of least privilege)
- **Management groups**: Organize subscriptions into hierarchy with inherited policies
- **Privileged Identity Management (PIM)**: Just-in-time access for privileged roles

**GCP IAM**:
- **Policy structure**: User → Google Group → IAM Role → GCP Resources
- **Predefined roles**: Use predefined roles where possible
- **Custom roles**: Create custom roles with specific permissions
- **Resource hierarchy**: Organization → Folder → Project (permissions inherit down)
- **Service accounts**: Use service accounts for applications (not user accounts)

**Common Cloud IAM Principles** (all platforms):
- **No root/global admin usage**: Root/global admin accounts used only for account setup and break-glass
- **Service accounts for applications**: Applications use service accounts (AWS IAM roles, Azure Managed Identity, GCP service accounts)
- **Resource tagging**: Tag resources for access control (e.g., Environment=Production, Owner=FinanceTeam)
- **Cross-account access**: Use roles for cross-account access (not user keys)

**Audit Evidence**: Cloud IAM policy exports, role assignments, permission reviews (Workbook 5)

---

## 7. Data Classification and Access Enforcement

### 7.1 Requirement: Data Classification Alignment

**REQ-A83-010**: Access restrictions **MUST** align with data classification levels.

**Data Classification Levels** (typical):

| Classification | Access Restriction | Encryption | MFA | Example Data |
|----------------|-------------------|------------|-----|--------------|
| **Public** | No restriction | Optional | No | Marketing materials, public website content |
| **Internal** | Authenticated users only | Recommended | No | Internal memos, non-sensitive business documents |
| **Confidential** | Need-to-know, department access | Required (at rest) | Recommended | Customer data, financial reports, source code |
| **Restricted** | Need-to-know, executive approval | Required (at rest + in transit) | Required | PII, trade secrets, M&A documents, passwords |

**Access Enforcement by Classification**:

**Public Data**:
- Access: Anyone (may be published on public website)
- Encryption: Not required
- MFA: Not required

**Internal Data**:
- Access: Authenticated employees and contractors only
- Encryption: Recommended (encryption at rest)
- MFA: Not required (password sufficient)
- Storage: Corporate file shares, internal SharePoint sites

**Confidential Data**:
- Access: Need-to-know basis (specific departments or project teams)
- Encryption: Required (encryption at rest)
- MFA: Recommended (MFA for remote access to confidential data)
- Storage: Dedicated file shares with restricted access, encrypted databases
- Logging: Access logging enabled

**Restricted Data**:
- Access: Need-to-know basis with executive/security approval
- Encryption: Required (encryption at rest and in transit - TLS 1.2+)
- MFA: Required (mandatory MFA for access to restricted data)
- Storage: Dedicated secure storage with audit logging
- Logging: Full audit logging of all access
- DLP: Data Loss Prevention (DLP) policies prevent unauthorized exfiltration

**Audit Evidence**: Data classification policy, classification labels on files/systems, encryption status by classification (Workbook 5)

---

## 8. Network Segmentation for Access Restriction

### 8.1 Requirement: Firewall Rules for Access Enforcement

**REQ-A83-011**: Network segmentation **MUST** enforce access restrictions between security zones.

**Network Segmentation Integration** (see also A.8.22):

Access restriction (A.8.3) leverages network segmentation (A.8.22) for defense in depth:

**Security Zones** (typical):
- **Internet** (untrusted)
- **DMZ** (public-facing servers)
- **Internal Network** (employee workstations, internal servers)
- **Data Center** (production servers, databases)
- **Management Network** (network devices, infrastructure management)

**Inter-Zone Access Rules** (default deny, explicit allow):

| Source Zone | Destination Zone | Allowed Traffic | Rationale |
|-------------|------------------|-----------------|-----------|
| Internet | DMZ | HTTPS (443), HTTP (80) | Public access to web servers |
| Internet | Internal | DENY ALL | No direct access to internal network |
| DMZ | Internet | HTTPS (443) for updates | Web servers need to download updates |
| DMZ | Internal | DENY ALL | DMZ compromised should not reach internal |
| Internal | DMZ | HTTPS (443) | Employees access internal web apps in DMZ |
| Internal | Internet | HTTPS (443), DNS (53) | Employee internet access |
| Data Center | Internet | DENY ALL | Production servers no direct internet |
| Data Center | Internal | Application-specific | Servers serve internal applications |
| Management | All | SSH (22), RDP (3389), SNMP (161) | Infrastructure management |
| All | Management | DENY ALL | Nothing should connect TO management network |

**Firewall Rule Requirements**:
- **Default deny**: All traffic denied unless explicitly allowed
- **Rule documentation**: Each rule has business justification
- **Regular review**: Quarterly review of firewall rules (remove unused rules)
- **Change control**: Firewall rule changes require approval and documentation

**Audit Evidence**: Firewall rule exports, rule justification documentation, rule review logs (Workbook 5 can reference A.8.22 network segmentation assessment)

---

## 9. Encryption-Based Access Restriction

### 9.1 Requirement: Encryption for Access Control

**REQ-A83-012**: Encryption **MUST** be used to restrict access to sensitive data.

**Encryption as Access Control**:

Encryption provides access control: Only users with decryption keys can access data.

**Encryption at Rest**:

**Full Disk Encryption** (FDE):
- **Purpose**: Protect data if device lost/stolen
- **Technologies**: BitLocker (Windows), FileVault (macOS), LUKS (Linux)
- **Key management**: TPM-based or password-protected
- **Scope**: All laptops, mobile devices, removable media

**Database Encryption**:
- **Transparent Data Encryption (TDE)**: Encrypt entire database (SQL Server TDE, Oracle TDE)
- **Column encryption**: Encrypt specific sensitive columns (SSN, credit card numbers)
- **Application-layer encryption**: Application encrypts data before storing in database

**File Encryption**:
- **File system encryption**: Encrypted file systems (EFS on Windows, eCryptfs on Linux)
- **Application-level encryption**: Applications encrypt files before storage (S3 server-side encryption)

**Encryption in Transit**:

**TLS (Transport Layer Security)**:
- **Purpose**: Protect data transmitted over network
- **Requirements**: TLS 1.2 minimum (TLS 1.3 preferred)
- **Scope**: All data in transit (web traffic, API calls, database connections, file transfers)

**VPN (Virtual Private Network)**:
- **Purpose**: Encrypt remote access traffic
- **Technologies**: IPsec VPN, SSL VPN
- **Requirement**: All remote access via VPN

**Key Management**:
- **Key storage**: Keys stored in Hardware Security Module (HSM) or key management service (AWS KMS, Azure Key Vault)
- **Key rotation**: Keys rotated annually (or per policy)
- **Key access control**: Only authorized systems/users can access encryption keys
- **Key backup**: Encryption keys backed up securely (encrypted backup)

**Integration with A.8.24 (Use of Cryptography)**:
- Detailed cryptographic requirements defined in A.8.24
- A.8.3 focuses on access restriction aspect of encryption
- Both controls reference same key management system

**Audit Evidence**: Encryption status by system/data classification (Workbook 5), key management documentation

---

## 10. Default Deny Principle

### 10.1 Requirement: Explicit Allow Required

**REQ-A83-013**: Access controls **MUST** use default deny (whitelist approach).

**Default Deny Principle**:

**Access denied unless explicitly allowed**:
- File permissions: Deny all, grant specific read/write to specific users/groups
- Database permissions: No privileges by default, grant specific privileges
- Firewall rules: Deny all traffic, allow specific traffic flows
- API access: Deny all requests, allow authenticated requests with valid scopes

**Benefits of Default Deny**:
- **Security by default**: Misconfigurations result in denied access (safe failure)
- **Explicit permissions**: All access is intentional (not accidental)
- **Audit clarity**: All allowed access is documented and justified

**Default Deny Implementation**:

**File Systems**:
- Remove "Everyone" and "Authenticated Users" permissions
- Grant access only to specific users/groups who need it

**Databases**:
- Revoke "PUBLIC" permissions (PostgreSQL) or remove default grants
- Grant specific privileges to specific users/roles

**Firewalls**:
- Final rule in firewall ruleset: "DENY ALL"
- All allow rules above this (explicit allows)

**Applications**:
- Default user role: No permissions
- Permissions granted through role assignment

**Prohibited Practices**:
- ❌ "Allow all, deny specific" (blacklist approach) - always insecure
- ❌ Broad permissions first, then restrict (default allow)
- ✅ Deny all first, then grant specific (default deny)

**Audit Evidence**: Permission configurations showing default deny, firewall rule sets (Workbook 5)

---

## 11. Access Control Verification and Testing

### 11.1 Requirement: Configuration Audits

**REQ-A83-014**: Access control configurations **MUST** be audited regularly.

**Configuration Audit Procedures**:

**Quarterly Audits**:
- File system permissions audit (sample sensitive directories)
- Database permissions audit (review grants for all accounts)
- Application RBAC audit (user-role assignments)
- Firewall rule audit (review all rules, remove unused)
- Cloud IAM policy audit (review policies, identify overly permissive)

**Automated Scanning**:
- **CIS Benchmarks**: Automated scanning against CIS security benchmarks
- **Cloud Security Posture Management (CSPM)**: Automated scanning of cloud configurations (Prisma Cloud, Wiz, Orca Security)
- **Configuration management**: Ansible, PowerShell DSC, Terraform state validation

**Manual Reviews**:
- Review access to most sensitive systems (quarterly)
- Review recent permission changes (monthly)
- Spot check: Random sample of systems for permission compliance

**Audit Evidence**: Configuration audit reports, scanning results, remediation tracking (Workbook 5)

### 11.2 Requirement: Penetration Testing

**REQ-A83-015**: Access control effectiveness **MUST** be tested through penetration testing.

**Penetration Testing for Access Controls**:

**Testing Scope**:
- Attempt to bypass access controls (horizontal privilege escalation)
- Attempt to gain elevated privileges (vertical privilege escalation)
- Test API authorization (access data outside assigned scope)
- Test application RBAC (perform actions outside role)

**Testing Frequency**:
- **Annual**: External penetration test (third-party company)
- **Quarterly**: Internal testing (security team or authorized personnel)
- **Ad-hoc**: After major changes (new application, infrastructure changes)

**Test Scenarios**:
- **Horizontal escalation**: User A accesses User B's data
- **Vertical escalation**: Standard user gains admin privileges
- **API abuse**: Enumerate data by manipulating API parameters (IDOR - Insecure Direct Object Reference)
- **File traversal**: Access files outside permitted directories (../../../etc/passwd)
- **SQL injection**: Bypass database access controls via injection attacks

**Remediation**:
- High/critical findings: Remediate within 30 days
- Medium findings: Remediate within 90 days
- Low findings: Remediate within 180 days
- Re-test after remediation

**Audit Evidence**: Penetration test reports, finding remediation tracking (Workbook 5)

---

## 12. Measurable Requirements and Audit Verification

### 12.1 Access Control Security Metrics

**Measurable requirements for audit verification**:

| Requirement | Metric | Target | Verification Method |
|-------------|--------|--------|---------------------|
| **Systems with default deny** | % systems configured default deny | 95%+ | Workbook 5 |
| **Permission audit coverage** | % systems audited quarterly | 100% sensitive, 50% standard | Workbook 5 |
| **Encryption - restricted data** | % restricted data encrypted | 100% | Workbook 5 |
| **Encryption - confidential data** | % confidential data encrypted | 95%+ | Workbook 5 |
| **Access control testing** | Penetration tests per year | 1+ (external) | Pen test reports |
| **Database least privilege** | % DB accounts with specific grants (not ALL) | 90%+ | Workbook 5 |
| **API rate limiting** | % APIs with rate limiting | 95%+ | Workbook 5 |
| **Cloud IAM least privilege** | % cloud policies using specific actions | 85%+ | Workbook 5 |
| **Configuration compliance** | % systems compliant with baselines | 90%+ | Workbook 5 |
| **Access violation incidents** | Unauthorized access attempts per month | <10 | Security logs |

### 12.2 Audit Evidence Requirements

**For ISO 27001:2022 A.8.3 audit**:

1. **Policy and procedures**: This document (ISMS-POL-A.8.2-3-5-S4)
2. **Permission audits**: Workbook 5 (file system, database, application, API permissions)
3. **Configuration compliance**: Configuration scan results, CIS benchmark compliance
4. **Encryption status**: Encryption inventory aligned with data classification
5. **Penetration testing**: Penetration test reports, remediation evidence
6. **Network segmentation**: Firewall rules (reference A.8.22 assessment)
7. **Cloud IAM**: Cloud IAM policy exports, permission reviews
8. **Default deny evidence**: Sample configurations showing default deny implementation

---

**END OF SECTION 4 (INFORMATION ACCESS RESTRICTION REQUIREMENTS - A.8.3)**

**Next Section**: ISMS-POL-A.8.2-3-5-S5 (Assessment Methodology and Evidence Framework)

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial information access restriction requirements (A.8.3) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**
