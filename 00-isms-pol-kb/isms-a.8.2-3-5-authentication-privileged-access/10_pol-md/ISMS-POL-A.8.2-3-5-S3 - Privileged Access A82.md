# ISMS-POL-A.8.2-3-5-S3
## Privileged Access Requirements (A.8.2)

**Document ID**: ISMS-POL-A.8.2-3-5-S3  
**Title**: Privileged Access Requirements (ISO/IEC 27001:2022 Control A.8.2)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architecture Lead | Initial privileged access requirements (A.8.2) |

**Review Cycle**: Annual (aligned with privileged access review cycle)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Architect
- Operational Review: Systems Administration Manager
- PAM Review: Privileged Access Management Lead

**Distribution**: Security team, systems administrators, database administrators, security administrators, cloud administrators, auditors  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 (Executive Summary)
- ISMS-POL-A.8.2-3-5-S2 (Authentication Requirements - A.8.5)
- ISMS-IMP-A.8.2-3-5-S3 (PAM Implementation)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.2

**Official Control Text**:

> *The allocation and use of privileged access rights should be restricted and managed.*

**Control Purpose**: Ensure privileged accounts (administrators, root, elevated access) are tightly controlled, monitored, and audited to prevent misuse, detect compromise, and limit blast radius of security incidents.

**Why This Matters**:

Privileged access is the **"keys to the kingdom"**. Privileged accounts can:
- Access ANY system in the environment
- Modify ANY data (including audit logs)
- Disable ANY security control
- Create backdoor accounts for persistence
- Delete evidence of compromise

**The Privileged Access Reality**:
- **80% of security breaches involve privileged access abuse** (CyberArk)
- **Domain Admin compromise = complete organizational breach**
- **Unmonitored privileged access = attacker dwell time measured in MONTHS**
- **Shared admin passwords = zero accountability** (who did what?)

Proper privileged access controls provide:
- **Blast radius limitation** through admin tiering (Tier 0 compromise doesn't reach everything)
- **Accountability** through session recording (know exactly what admin did)
- **Credential protection** through PAM vaulting (passwords never seen by humans)
- **Temporary access** through Just-in-Time (admin rights only when needed, auto-revoked)
- **Lateral movement prevention** through tier isolation (attacker cannot hop between tiers)

### 1.2 Scope of A.8.2 Requirements

This section defines mandatory requirements for:

1. **Privileged User Identification** - Who has admin access and why
2. **Privileged Account Types** - Named, shared, service, break-glass accounts
3. **Privileged Access Management (PAM)** - Vaulting, JIT, approval workflows, session recording
4. **Privileged Account Separation** - Separate admin accounts from user accounts
5. **Admin Tiering Model** - Tier 0/1/2 isolation to prevent lateral movement
6. **MFA for Privileged Access** - Multi-factor authentication MANDATORY
7. **Privileged Access Monitoring** - Real-time monitoring and alerting
8. **Privileged Credential Rotation** - Automated password changes
9. **Privileged Access Reviews** - Quarterly verification of need

---

## 2. Privileged User Identification Requirements

### 2.1 Requirement: Definition of Privileged Access

**REQ-A82-001**: [Organization] **MUST** clearly define what constitutes privileged access.

**Privileged Access Definition**:

Privileged access is any access that allows a user to:
- Perform administrative functions (install software, change configurations)
- Access systems or data beyond normal business need
- Modify security controls (disable firewall, change permissions)
- Bypass normal access controls
- Access audit logs or security monitoring systems

**Privileged Access Types**:

1. **System Administrators**:
   - Windows Server administrators (Domain Admin, Enterprise Admin, local Administrator)
   - Linux/Unix administrators (root, sudo access)
   - Network device administrators (network routers, switches, firewalls)
   - Virtual infrastructure administrators (VMware, Hyper-V admins)

2. **Database Administrators (DBAs)**:
   - Database server administrators (SQL Server sa, Oracle SYS/SYSTEM, PostgreSQL superuser)
   - Database backup/restore privileges
   - Schema modification privileges

3. **Security Administrators**:
   - Firewall administrators
   - SIEM administrators
   - Antivirus/EDR administrators
   - PAM administrators
   - IAM administrators

4. **Cloud Administrators**:
   - Cloud global administrators (Azure Global Admin, AWS root, GCP Owner)
   - Cloud subscription/account administrators
   - Cloud resource administrators (EC2, VM management)

5. **Application Administrators**:
   - ERP administrators (SAP, Oracle EBS)
   - CRM administrators (Salesforce admin)
   - Application-specific admin roles

6. **Backup/Recovery Administrators**:
   - Backup system administrators
   - Disaster recovery administrators

**Non-Privileged Access** (for clarity):
- Standard user access to email, productivity tools
- Application users with read/write access to business data (within their role)
- End-user device local user accounts (not local admin)

**Audit Evidence**: Privileged access definition documentation, role catalog

### 2.2 Requirement: Privileged User Inventory

**REQ-A82-002**: [Organization] **MUST** maintain a complete inventory of all privileged users and accounts.

**Privileged User Inventory Requirements**:

For EACH privileged user, document:
- **User identity** (name, employee ID)
- **Privileged accounts owned** (john.admin, john.tier0, john.dba, etc.)
- **Privileged role** (Windows admin, Linux admin, DBA, security admin, cloud admin)
- **Admin tier classification** (Tier 0, Tier 1, Tier 2 - see Section 5)
- **Systems/platforms** (Windows servers, Linux servers, network devices, AWS, Azure, databases)
- **Business justification** (why does this user need privileged access?)
- **Approval date and approver** (who approved this privileged access grant?)
- **Last access review date** (quarterly reviews required)
- **MFA status** (MFA MUST be enabled for all privileged users)

**Privileged User Discovery**:
- Query Active Directory for privileged groups (Domain Admins, Enterprise Admins, Administrators)
- Query Azure AD for privileged roles (Global Administrator, Security Administrator)
- Query AWS for privileged IAM users/roles
- Query database servers for DBA accounts (sa, SYSTEM, postgres)
- Query PAM solution for vaulted accounts
- Query network devices for admin accounts

**Inventory Maintenance**:
- **Update frequency**: Monthly (detect new privileged grants)
- **Verification**: Quarterly full inventory review
- **Automation**: Automated discovery where possible (AD queries, cloud APIs)

**Audit Evidence**: Privileged user inventory (Workbook 3), discovery automation

---

## 3. Privileged Account Types and Management

### 3.1 Requirement: Named Privileged Accounts

**REQ-A82-003**: Privileged access **MUST** use named privileged accounts separate from standard user accounts.

**Named Privileged Account Principle**:

Each user requiring privileged access has **two accounts**:
1. **Standard user account**: For daily work (email, documents, web browsing)
   - Example: `john.doe`
   - Rights: Standard user, no admin rights
   - Usage: 95% of the time

2. **Privileged account**: For administrative tasks ONLY
   - Example: `john.doe.admin` or `john.admin` or `adm-john.doe`
   - Rights: Administrative access
   - Usage: 5% of the time, only when performing admin tasks
   - Requires: MFA MANDATORY

**Why Separate Accounts?**
- **Reduces attack surface**: Standard account compromise doesn't grant admin access
- **Accountability**: Clear audit trail (admin account used = administrative action)
- **Least privilege**: Users operate with minimum necessary privileges most of the time
- **Malware protection**: Malware running under standard account cannot install itself system-wide

**Account Naming Conventions**:

Standardized naming helps identification and automation:
- **Windows**: `adm-firstname.lastname` or `firstname.lastname.admin`
- **Linux**: `firstname.lastname-admin` or `root-firstname.lastname`
- **Database**: `firstname.lastname.dba`
- **Cloud**: `firstname.lastname@admin.domain.com` or `admin-firstname.lastname`

[Organization] chooses naming convention and applies consistently.

**Prohibited Practices**:
- ❌ Using standard account for administrative tasks (elevate via UAC/sudo)
- ❌ Using privileged account for daily work (email, web browsing as admin)
- ❌ Shared privileged accounts without PAM vaulting (see Section 3.2)

**Audit Evidence**: Named privileged account inventory, account naming compliance

### 3.2 Requirement: Shared Privileged Accounts

**REQ-A82-004**: Shared privileged accounts **MUST** be secured in PAM vault with session recording.

**Shared Privileged Account Definition**:

Accounts used by multiple administrators or required for system functions:
- **Windows**: Local Administrator, Domain Administrator account
- **Linux**: root account
- **Network devices**: admin, enable
- **Databases**: sa (SQL Server), SYSTEM (Oracle), postgres (PostgreSQL)
- **Applications**: Application admin accounts

**Why Shared Accounts Are High Risk**:
- **No accountability**: Multiple people know password, cannot determine who acted
- **Password sharing**: Passwords shared via email, written down, never changed
- **No audit trail**: All actions logged under same account name (e.g., "root")
- **Permanent access**: Shared passwords don't expire when person leaves

**Shared Account Management Requirements**:

1. **PAM Vaulting** (MANDATORY):
   - All shared privileged passwords stored in PAM vault
   - Passwords never known to administrators (check-out/check-in)
   - Automated password rotation (passwords changed after each use or daily)

2. **Check-Out/Check-In Workflow**:
   - Administrator requests access via PAM solution
   - PAM provides temporary password (or launches session)
   - Administrator uses account for approved task
   - PAM rotates password after check-in (or after time limit)

3. **Session Recording** (MANDATORY):
   - All sessions using shared accounts recorded (keystroke or video)
   - Recordings retained for audit (90 days minimum, 1 year recommended)
   - Recordings reviewable by security team

4. **Approval Workflow** (for high-risk accounts):
   - Shared account access requires approval (manager or security team)
   - Approval includes justification (what task requires shared account?)
   - Emergency access: Approve after-the-fact (with review)

5. **Minimize Shared Account Usage**:
   - **Preferred**: Named privileged accounts with PAM
   - **Acceptable**: Shared accounts in PAM vault with recording
   - **Goal**: Eliminate shared accounts where possible (use named accounts + JIT)

**Shared Accounts by Platform**:

| Platform | Shared Account | PAM Requirement | Session Recording |
|----------|----------------|-----------------|-------------------|
| Windows | Local Administrator | Mandatory | Mandatory |
| Windows | Domain Administrator | Mandatory | Mandatory |
| Linux | root | Mandatory | Mandatory |
| Network | admin, enable | Mandatory | Mandatory |
| Database | sa, SYSTEM, postgres | Mandatory | Mandatory |
| Cloud | AWS root, Azure global admin | Mandatory | Mandatory |

**Audit Evidence**: Shared account inventory, PAM vault configuration, session recordings

### 3.3 Requirement: Service Accounts with Privileges

**REQ-A82-005**: Service accounts with privileged access **MUST** be managed and monitored.

**Service Account Definition**:

Non-human accounts used by applications, services, or automation:
- Windows services running as specific account
- Application service accounts (SharePoint farm account, SQL Server service account)
- Automation/scripting accounts (Ansible service account, scheduled task accounts)
- API service accounts (application-to-application authentication)

**Service Account Challenges**:
- **No interactive login**: Cannot use MFA (service cannot approve push notification)
- **Long-lived credentials**: Passwords rarely changed (breaks service if changed)
- **Broad access**: Often granted excessive privileges (easy shortcut)
- **Forgotten accounts**: Created for project, never removed

**Service Account Management Requirements**:

1. **Inventory and Ownership**:
   - Complete inventory of all service accounts with privileges
   - Owner assigned (who is responsible for this service account?)
   - Purpose documented (what service/application uses this account?)

2. **Credential Management**:
   - **Preferred**: Certificate-based authentication (no passwords)
   - **Acceptable**: Passwords in PAM vault with automated rotation
   - **Prohibited**: Hard-coded passwords in scripts or configuration files

3. **Least Privilege**:
   - Service accounts granted ONLY privileges required for function
   - No "Domain Admin" service accounts (unless absolutely necessary)
   - Regular privilege review (quarterly)

4. **Monitoring**:
   - Service account login monitoring (alert on interactive login - suspicious)
   - Service account privilege usage logging
   - Failed authentication monitoring (detect compromise attempts)

5. **Credential Rotation**:
   - Automated rotation where possible (PAM solution or Group Managed Service Accounts in AD)
   - Manual rotation if automated not possible (minimum: annually)
   - Immediate rotation if compromise suspected

6. **Alternatives to Service Accounts**:
   - **Managed identities** (Azure Managed Identity, AWS IAM Roles for EC2)
   - **Group Managed Service Accounts** (Windows gMSA - automatic password rotation)
   - **Certificate-based authentication** (no password needed)

**Audit Evidence**: Service account inventory, credential rotation logs, privilege reviews

### 3.4 Requirement: Break-Glass / Emergency Accounts

**REQ-A82-006**: Break-glass accounts **MUST** be secured with sealed credentials and monitored usage.

**Break-Glass Account Definition**:

Emergency privileged accounts for use when normal authentication systems fail:
- Primary identity provider down (Azure AD outage, Okta outage)
- MFA system unavailable
- PAM system down
- Critical incident requiring immediate access

**Break-Glass Account Requirements**:

1. **Account Creation**:
   - Minimum 2 break-glass accounts (redundancy)
   - Accounts excluded from normal policies (no password expiration, no MFA requirement)
   - Highest privilege level (Domain Admin, Global Admin, root)

2. **Credential Storage**:
   - **Physical security**: Passwords written down, sealed in envelope, stored in safe
   - **Dual custody**: Requires two authorized persons to open (CEO + CISO, or equivalent)
   - **Digital backup**: Encrypted password in secure offline storage (not in PAM - PAM might be down)

3. **Access Procedures**:
   - **Use triggers**: Only use when normal access methods unavailable
   - **Authorization**: Executive approval required (CISO or CIO)
   - **Documentation**: Reason for use, who used, what actions performed
   - **Immediate password change**: After use, change password and re-seal

4. **Monitoring and Alerting**:
   - **Alert on any use**: Critical alert to security team when break-glass account logs in
   - **Audit logging**: All actions performed with break-glass account logged
   - **Post-incident review**: Full investigation of why break-glass was needed

5. **Regular Verification**:
   - **Quarterly test**: Verify break-glass accounts work (in controlled test environment)
   - **Password verification**: Confirm sealed password matches actual password
   - **Envelope integrity**: Verify seals not broken

**Break-Glass Account Examples**:
- **Windows**: Emergency-Admin1, Emergency-Admin2 (local Administrator rights on all servers)
- **Azure AD**: breakglass1@domain.onmicrosoft.com, breakglass2@domain.onmicrosoft.com
- **AWS**: emergency-root-access-1, emergency-root-access-2

**Audit Evidence**: Break-glass account documentation, sealed credentials inventory, usage logs, test logs

---

## 4. Privileged Access Management (PAM) Requirements

### 4.1 Requirement: PAM Solution Deployment

**REQ-A82-007**: [Organization] **MUST** deploy Privileged Access Management (PAM) solution or equivalent controls.

**PAM Solution Purpose**:

Centralized system for managing, monitoring, and securing privileged access:
- **Password vaulting**: Secure storage of privileged credentials
- **Check-out/check-in**: Temporary access to privileged accounts
- **Session recording**: Record all privileged sessions for audit
- **Just-in-time (JIT) access**: Temporary privilege elevation
- **Automated credential rotation**: Change passwords automatically
- **Approval workflows**: Require approval for privileged access
- **Audit logging**: Complete audit trail of privileged access

**PAM Solution Options** (technology-agnostic):

**Enterprise PAM Solutions**:
- CyberArk Privileged Access Manager
- BeyondTrust Privilege Management
- Delinea Secret Server (formerly Thycotic)
- One Identity Safeguard

**Cloud-Native PAM**:
- Azure Privileged Identity Management (PIM)
- AWS Systems Manager Session Manager
- GCP Privileged Access Manager

**Open-Source / Alternative**:
- HashiCorp Vault
- Teleport (open-source PAM)

**Native OS Controls** (if no PAM solution):
- Windows: Local Admin Password Solution (LAPS) + sudo logging
- Linux: sudo with centralized logging (rsyslog to SIEM)
- Limitation: No session recording, limited workflow, manual password rotation

**PAM Deployment Requirements**:

1. **Coverage**: All shared privileged accounts in PAM vault
2. **High Availability**: PAM solution deployed redundantly (no single point of failure)
3. **Secure Storage**: PAM database encrypted at rest
4. **Access Control**: Only authorized admins can access PAM
5. **Backup**: PAM configuration and vault backed up securely (encrypted backups)
6. **Monitoring**: PAM solution logs forwarded to SIEM

**Audit Evidence**: PAM solution documentation, vaulted accounts inventory, PAM logs

### 4.2 Requirement: Password Vaulting

**REQ-A82-008**: Shared privileged passwords **MUST** be vaulted in PAM solution.

**Password Vaulting Requirements**:

1. **Credential Onboarding**:
   - Discover privileged accounts across all systems
   - Import credentials into PAM vault
   - Verify credentials work (test login)
   - Rotate credentials after import (previous password no longer valid)

2. **Secure Storage**:
   - Passwords encrypted at rest in PAM vault
   - Passwords encrypted in transit (TLS)
   - Passwords never displayed in plain text (copy-paste to application)

3. **Check-Out/Check-In Workflow**:
   - **Check-out**: Administrator requests access, PAM provides temporary credential
   - **Session**: Administrator uses credential for approved task
   - **Check-in**: Administrator returns credential or session expires
   - **Rotation**: PAM changes password after check-in (or after defined interval)

4. **Access Policies**:
   - Who can check out which credentials? (role-based access to vault)
   - Approval required for high-risk accounts? (Domain Admin, root, production DB)
   - Time limits on check-out? (automatic check-in after X hours)
   - Exclusive access? (only one person can check out account at a time)

5. **Credential Types in Vault**:
   - Shared administrative passwords (root, Administrator, sa)
   - Service account passwords
   - API keys and tokens
   - SSH private keys
   - Cloud access keys (AWS access keys, Azure service principal secrets)
   - Encryption keys (for specific use cases, not primary key management)

**Automated Password Rotation**:
- **Frequency**: After each check-in, or daily/weekly for inactive accounts
- **Rotation mechanism**: PAM connects to system and changes password programmatically
- **Verification**: PAM verifies new password works (test login)
- **Notification**: Alert if rotation fails

**Audit Evidence**: PAM vault inventory, check-out/check-in logs, rotation logs

### 4.3 Requirement: Just-in-Time (JIT) Privileged Access

**REQ-A82-009**: Just-in-time privileged access **SHOULD** be implemented to minimize standing privileges.

**JIT Privileged Access Concept**:

Instead of permanent admin rights, grant temporary privilege elevation:
- **Normal state**: User has NO admin rights
- **When needed**: User requests admin rights for specific task
- **Temporary grant**: Admin rights granted for limited time (e.g., 4 hours)
- **Automatic revocation**: Admin rights automatically removed after time expires
- **Audit**: Full audit trail of when admin rights granted and what was done

**JIT Benefits**:
- **Reduced attack surface**: Most of the time, accounts have no elevated privileges
- **Lateral movement prevention**: Attacker compromises account when NO admin rights
- **Accountability**: Clear justification required for each admin rights grant
- **Compliance**: Demonstrates least privilege principle

**JIT Implementation Options**:

1. **Azure Privileged Identity Management (PIM)**:
   - JIT for Azure AD admin roles (Global Admin, Security Admin, etc.)
   - Time-bound role activation (user activates role for 1-8 hours)
   - Approval workflow (require manager approval for role activation)
   - MFA on activation (require MFA to activate privileged role)

2. **AWS IAM Temporary Credentials**:
   - AssumeRole for temporary AWS access
   - Time-limited sessions (configurable duration)
   - Federated access with temporary tokens

3. **PAM Solution JIT**:
   - CyberArk Dual Control
   - BeyondTrust Temporary Privilege Elevation
   - Delinea Just-in-Time access

4. **Native OS JIT** (less sophisticated):
   - Windows: Admin Approval Mode (UAC prompts)
   - Linux: sudo with time limits (sudo timeout)
   - Limitation: No centralized management, limited workflow

**JIT Access Workflow**:

1. User requests privileged access (via PAM portal or PIM)
2. User provides justification ("Need to restart production DB server")
3. Approval (automatic for low-risk, manual for high-risk)
4. Privileged access granted for defined time (e.g., 4 hours)
5. User performs administrative task
6. Access automatically revoked after time expires
7. Session recorded and audited

**JIT vs. Standing Privileges**:

| Scenario | Standing Privileges | JIT Access |
|----------|---------------------|------------|
| **Daily state** | User always has admin rights | User has no admin rights |
| **When compromise occurs** | Attacker gets admin access | Attacker gets standard access only |
| **Audit complexity** | All admin actions always possible | Admin actions only during grant period |
| **User experience** | Seamless (always admin) | Request-and-approve (extra step) |
| **Security** | Higher risk | Lower risk (time-bounded) |

**JIT Adoption Strategy**:
- **Start**: High-risk privileged accounts (Domain Admin, Global Admin)
- **Expand**: Server administrators, database administrators
- **Goal**: 50%+ of privileged access via JIT within 24 months

**Audit Evidence**: JIT access requests, approval logs, time-bounded grants

### 4.4 Requirement: Approval Workflows for Privileged Access

**REQ-A82-010**: High-risk privileged access **MUST** require approval workflows.

**Approval Workflow Requirements**:

**Tier 0 Privileged Access** (Domain Admin, Global Admin, root on critical systems):
- **Approval required**: Yes, mandatory
- **Approver**: Security team lead or CISO
- **Approval timeframe**: 15 minutes for emergencies, 4 hours for planned work
- **Justification**: Business reason required ("Disaster recovery test", "Security incident response")

**Tier 1 Privileged Access** (Server admin, DBA):
- **Approval required**: For production systems
- **Approver**: Manager or senior admin
- **Approval timeframe**: 1 hour
- **Justification**: Change ticket number or incident number

**Tier 2 Privileged Access** (Workstation admin):
- **Approval required**: No (automatic)
- **Logging**: Yes (all access logged)
- **Justification**: Recorded for audit

**Emergency Access**:
- **Break-glass process**: Access granted immediately, approval after-the-fact
- **Review**: Within 24 hours of emergency access
- **Verification**: Was emergency legitimate? What was done?

**Approval Workflow Integration**:
- PAM solution approval workflows
- Azure PIM approval workflows
- Integration with ticketing system (ServiceNow, Jira) - link access to change ticket

**Audit Evidence**: Approval logs, justification records, emergency access reviews

### 4.5 Requirement: Privileged Session Recording

**REQ-A82-011**: Privileged sessions **MUST** be recorded for security audit and forensics.

**Session Recording Requirements**:

**What to Record**:
- All sessions using shared privileged accounts (root, Administrator, sa, admin)
- All Tier 0 privileged sessions (Domain Admin, Global Admin)
- Tier 1 sessions on production systems (server admin, DBA on production)

**Recording Methods**:

1. **Keystroke Logging** (text-based):
   - Record all commands typed and output displayed
   - Lower storage requirements (text-only)
   - Searchable (can search for specific commands)
   - Works well for: SSH sessions, database queries, command-line admin

2. **Video Recording** (graphical):
   - Record full video of session (screen capture)
   - Higher storage requirements (video files)
   - Shows GUI interactions
   - Works well for: RDP sessions, web-based admin consoles, GUI applications

3. **Hybrid Approach**:
   - Keystroke logging for SSH/CLI sessions
   - Video recording for RDP/GUI sessions

**Session Recording Platforms**:
- PAM solutions (CyberArk, BeyondTrust - built-in session recording)
- Dedicated session recording (Ekran System, ObserveIT)
- SSH session recording (tlog, asciinema)
- RDP session recording (Windows RDS session recording, third-party tools)

**Recording Retention**:
- **Minimum retention**: 90 days online (searchable)
- **Extended retention**: 1 year archived (compliance requirement)
- **High-risk sessions**: 7 years (financial systems, regulated environments)

**Recording Access Control**:
- **Who can view recordings**: Security team, audit team, authorized investigators
- **Recording search**: Searchable by user, timestamp, system, commands
- **Playback**: Ability to play back session at 1x, 2x, 4x speed
- **Export**: Export recordings for incident investigation

**Privacy Considerations**:
- Users notified that privileged sessions are recorded (login banner)
- Recordings used ONLY for security audit and incident investigation
- Access to recordings logged (who viewed which recording)

**Session Recording Benefits**:
- **Accountability**: Know exactly what admin did during session
- **Forensics**: Investigate what happened during security incident
- **Training**: Use recordings to train junior admins (with permission)
- **Compliance**: Demonstrate privileged access oversight to auditors

**Audit Evidence**: Session recording configuration, sample recordings, recording access logs

---

## 5. Admin Tiering / Tiered Administration Model

### 5.1 Requirement: Privileged Access Tier Classification

**REQ-A82-012**: [Organization] **MUST** implement Admin Tiering Model to prevent lateral movement and limit blast radius.

**Admin Tiering Concept**:

Segregate privileged access into **three tiers** to prevent credential theft and lateral movement:

**Problem without tiering**:
- Attacker compromises workstation → steals Domain Admin credential cached on workstation → compromises entire domain

**Solution with tiering**:
- Tier 0 accounts NEVER log into workstations → attacker compromises workstation → finds NO Tier 0 credentials → cannot reach Tier 0 systems

**Admin Tiering Model Overview**:

```
Tier 0 (Domain/Enterprise Assets)    ← HIGHEST PRIVILEGE, HIGHEST PROTECTION
   ↑ NO DOWNWARD ACCESS
   
Tier 1 (Server/Application Assets)    ← MEDIUM PRIVILEGE, MEDIUM PROTECTION
   ↑ NO DOWNWARD ACCESS
   
Tier 2 (Workstation/Endpoint Assets)  ← LIMITED PRIVILEGE, STANDARD PROTECTION
```

**Tier 0 accounts NEVER access Tier 1 or Tier 2 systems**  
**Tier 1 accounts NEVER access Tier 2 systems**

### 5.2 Requirement: Tier 0 - Domain/Enterprise/Critical Infrastructure

**REQ-A82-013**: Tier 0 systems and accounts **MUST** have the strongest security controls.

**Tier 0 Definition**:

Systems and accounts that control the **entire environment** - compromise of Tier 0 = complete organizational breach.

**Tier 0 Systems** (can access ANY system in organization):

1. **Active Directory Domain Controllers**:
   - Domain controllers (Windows AD)
   - AD replication infrastructure
   - DNS servers (if integrated with AD)
   - Read-only domain controllers (RODCs)

2. **Cloud Identity Tenants**:
   - Azure AD tenant (entire tenant = Tier 0)
   - AWS root account and Organization root
   - GCP Organization node

3. **Security Infrastructure**:
   - SIEM systems (Splunk, Datadog, etc.)
   - PAM solution (CyberArk, BeyondTrust)
   - Backup infrastructure (can restore ANY system)
   - Certificate Authority (PKI root and issuing CAs)

4. **Critical Management Systems**:
   - ITSM admin (ServiceNow admins - control IT processes)
   - Identity governance platforms (SailPoint, One Identity)
   - Network management systems (with credentials to all network devices)

**Tier 0 Accounts**:
- Domain Admins, Enterprise Admins, Schema Admins (Windows AD)
- Azure Global Administrator, Security Administrator (Azure AD)
- AWS root user, Organization admin (AWS)
- GCP Organization Admin, Security Admin (GCP)
- Backup Administrators (Veeam admins, backup server admins)
- SIEM Administrators
- PAM Administrators
- PKI Administrators (Certificate Authority admins)

**Tier 0 Security Requirements** (STRONGEST controls):

1. **Separate Accounts per Tier**:
   - User has: `john.doe` (standard), `john.doe.tier1` (Tier 1 admin), `john.doe.tier0` (Tier 0 admin)
   - Tier 0 account used ONLY for Tier 0 administrative tasks
   - Tier 0 account NEVER used for email, web browsing, or non-Tier 0 tasks

2. **Dedicated Privileged Access Workstations (PAWs)**:
   - Tier 0 admins use **dedicated hardened workstations** (PAWs) for Tier 0 access
   - PAWs are clean, locked-down, monitored systems
   - PAWs cannot browse internet, cannot check email (air-gapped from user activity)
   - PAWs only RDP to Tier 0 systems

3. **Hardware MFA Tokens** (FIDO2):
   - Tier 0 accounts REQUIRE hardware MFA tokens (not authenticator apps)
   - Phishing-resistant authentication
   - YubiKey, Titan Security Key, or equivalent

4. **Session Recording MANDATORY**:
   - ALL Tier 0 sessions recorded (100% coverage)
   - Real-time monitoring of Tier 0 activities
   - Alerts on any Tier 0 account activity

5. **Just-in-Time Access** (where possible):
   - Tier 0 rights granted temporarily (not standing privileges)
   - Azure PIM for Azure AD Global Admin (activate role for 4 hours, then auto-revoke)

6. **Network Isolation**:
   - Tier 0 systems on separate VLAN/network segment
   - Firewall rules: ONLY PAWs can connect to Tier 0 systems
   - Jump servers for Tier 0 access (bastion hosts)

7. **No Internet Access**:
   - Tier 0 accounts cannot browse internet (no phishing risk)
   - Tier 0 accounts cannot check email

8. **Quarterly Access Reviews**:
   - Every quarter: Review who has Tier 0 access
   - Justification required for each Tier 0 account
   - Remove access if no longer needed

**Tier 0 Isolation Benefits**:
- Attacker compromises user workstation → NO Tier 0 credentials found → cannot escalate to Tier 0
- Limits blast radius: Even if Tier 1 or Tier 2 compromised, Tier 0 remains secure

**Audit Evidence**: Tier 0 system inventory, Tier 0 account inventory, PAW deployment, hardware token assignment

### 5.3 Requirement: Tier 1 - Server/Application Infrastructure

**REQ-A82-014**: Tier 1 systems and accounts **MUST** have strong security controls and NOT access Tier 0.

**Tier 1 Definition**:

Systems and accounts that manage **servers and applications** - compromise of Tier 1 affects production systems but not entire environment.

**Tier 1 Systems**:

1. **Server Infrastructure**:
   - Windows servers (not domain controllers)
   - Linux servers (web, app, database servers)
   - Virtualization hosts (VMware ESXi, Hyper-V hosts)

2. **Application Infrastructure**:
   - ERP systems (SAP, Oracle EBS)
   - CRM systems (Salesforce)
   - Database servers (SQL Server, Oracle, PostgreSQL, MySQL)
   - Web applications (production web apps)

3. **Cloud Infrastructure** (non-global):
   - AWS EC2 instances, RDS databases
   - Azure virtual machines, SQL databases
   - GCP Compute Engine instances

**Tier 1 Accounts**:
- Server administrators (Windows server admin, Linux admin)
- Application administrators (SAP admin, Salesforce admin)
- Database administrators (SQL Server DBA, Oracle DBA)
- Virtualization administrators (VMware admin, Hyper-V admin)
- Cloud infrastructure administrators (AWS EC2 admin, Azure VM admin - NOT Global Admin)

**Tier 1 Security Requirements**:

1. **Separate Admin Accounts**:
   - User has: `john.doe` (standard), `john.doe.tier1` (Tier 1 admin)
   - Tier 1 account used ONLY for server/application administration
   - Tier 1 account NEVER logs into Tier 0 systems (prevented via firewall/GPO)

2. **MFA MANDATORY**:
   - Tier 1 accounts REQUIRE MFA (authenticator app minimum, hardware token preferred)

3. **Separate Admin Workstations** (recommended but not mandatory like Tier 0):
   - Dedicated workstations for Tier 1 administration (separate from daily-use laptop)
   - Alternatively: Jump servers/bastion hosts for Tier 1 access

4. **Session Recording** (Tier 1 production systems):
   - Record sessions on production Tier 1 systems
   - Development/test Tier 1 systems: Recording recommended but not mandatory

5. **Quarterly Access Reviews**:
   - Review Tier 1 access quarterly
   - Remove access if no longer needed

6. **Tier Isolation Enforcement**:
   - Tier 1 accounts CANNOT log into Tier 0 systems (GPO, Azure conditional access)
   - Tier 1 accounts CANNOT log into Tier 2 systems (prevents credential theft if Tier 2 compromised)

**Tier 1 Isolation Benefits**:
- Attacker compromises Tier 1 server → finds Tier 1 credentials → can access other Tier 1 servers
- BUT: Cannot escalate to Tier 0 (no Tier 0 credentials on Tier 1 systems)
- AND: Cannot pivot to Tier 2 workstations (Tier 1 accounts restricted)

**Audit Evidence**: Tier 1 system inventory, Tier 1 account inventory, tier isolation policies

### 5.4 Requirement: Tier 2 - Workstation/Endpoint

**REQ-A82-015**: Tier 2 systems and accounts **MUST NOT** have access to Tier 0 or Tier 1 systems.

**Tier 2 Definition**:

Systems and accounts that manage **end-user workstations and devices** - lowest privilege tier.

**Tier 2 Systems**:
- End-user workstations (desktops, laptops)
- Mobile devices (smartphones, tablets)
- Printers, scanners, peripheral devices

**Tier 2 Accounts**:
- Desktop support / Help desk (local admin on workstations)
- MDM administrators (Intune admin, Jamf admin - device management only)
- Endpoint management (patch management for workstations)

**Tier 2 Security Requirements**:

1. **Limited Privilege**:
   - Tier 2 admins have local admin on workstations ONLY
   - Cannot access servers (Tier 1) or domain controllers (Tier 0)

2. **MFA MANDATORY**:
   - Tier 2 accounts REQUIRE MFA

3. **Tier Isolation Enforcement**:
   - Tier 2 accounts CANNOT log into Tier 0 or Tier 1 systems (firewall rules, access denied)

4. **Quarterly Access Reviews**:
   - Review Tier 2 access quarterly

**Tier 2 Why It Matters**:
- Workstations are MOST frequently compromised (phishing, malware, drive-by downloads)
- If Tier 0 or Tier 1 accounts log into workstations → credentials cached → attacker steals credentials
- Tier isolation prevents this: No Tier 0/1 credentials on workstations = attacker stuck at Tier 2

**Audit Evidence**: Tier 2 account inventory, tier isolation enforcement

### 5.5 Requirement: Tier Isolation Enforcement

**REQ-A82-016**: Tier isolation **MUST** be technically enforced to prevent cross-tier access.

**Tier Isolation Enforcement Methods**:

1. **Group Policy Objects (GPO)** - Windows AD:
   - Deny logon policies: Tier 0 accounts denied logon to Tier 1/2 systems
   - Logon restrictions configured via GPO applied to OUs (Organizational Units)

2. **Azure AD Conditional Access Policies**:
   - Tier 0 users can only access Tier 0 devices (PAWs)
   - Block Tier 0 users from accessing Tier 1/2 devices

3. **Firewall Rules**:
   - Network segmentation: Tier 0 network isolated from Tier 1/2 networks
   - Only PAWs can connect to Tier 0 systems (firewall rules)

4. **PAM Solution Tier Enforcement**:
   - CyberArk, BeyondTrust: Configure access policies based on tier
   - Tier 0 accounts can only check out Tier 0 credentials
   - Attempting to use Tier 0 account on Tier 1 system: DENIED

5. **Authentication Policies** (Windows AD):
   - Authentication Policies and Silos (Windows Server 2012 R2+)
   - Restrict which accounts can authenticate to which systems

**Tier Isolation Monitoring**:
- **Alert on tier violations**: Tier 0 account attempting to log into Tier 1/2 system = CRITICAL ALERT
- **Weekly tier violation reports**: Report showing any tier isolation violations
- **Investigation**: Any tier violation investigated immediately (legitimate need or attack?)

**Audit Evidence**: Tier isolation policies (GPOs, conditional access), tier violation logs, monitoring alerts

### 5.6 Requirement: Admin Tiering Implementation Roadmap

**REQ-A82-017**: Admin tiering implementation **MUST** follow phased approach.

**Admin Tiering Adoption Phases**:

**Phase 1 - Foundation** (Months 1-3):
- Classify all systems into Tier 0/1/2
- Identify all privileged accounts and classify by tier
- Create separate admin accounts per tier (john.doe.tier0, john.doe.tier1, john.doe.tier2)
- Document tier isolation requirements

**Phase 2 - Tier 0 Protection** (Months 4-6):
- Deploy Privileged Access Workstations (PAWs) for Tier 0 admins
- Enforce Tier 0 account restrictions (can only log into PAWs and Tier 0 systems)
- Deploy hardware MFA tokens for Tier 0 accounts
- Enable session recording for all Tier 0 access

**Phase 3 - Tier 1 Isolation** (Months 7-9):
- Enforce Tier 1 account restrictions (cannot log into Tier 0 or Tier 2 systems)
- Deploy jump servers / bastion hosts for Tier 1 access
- Enable session recording for Tier 1 production access

**Phase 4 - Monitoring and Compliance** (Months 10-12):
- Deploy tier violation monitoring and alerting
- Generate tier compliance reports
- Train administrators on tier model
- Quarterly tier compliance reviews

**Adoption Metrics**:
- Tier classification completion: 100% of systems classified
- Tier 0 PAW deployment: 100% of Tier 0 admins using PAWs
- Tier 0 hardware MFA: 100% of Tier 0 accounts using hardware tokens
- Tier isolation enforcement: 95%+ compliance (minimal tier violations)
- Tier violation response time: <15 minutes for critical alerts

**Audit Evidence**: Tiering implementation roadmap, phase completion status, adoption metrics

---

## 6. Multi-Factor Authentication for Privileged Access

### 6.1 Requirement: MFA Mandatory for All Privileged Access

**REQ-A82-018**: Multi-factor authentication **MUST** be enabled for ALL privileged accounts.

**MFA for Privileged Access Requirements**:

**Non-Negotiable**:
- **100% of privileged users MUST have MFA** - no exceptions
- **Password-only privileged access is PROHIBITED**

**MFA Methods by Tier**:

| Tier | MFA Requirement | Acceptable Methods |
|------|-----------------|-------------------|
| **Tier 0** | Hardware tokens REQUIRED | FIDO2, YubiKey, Titan Security Key |
| **Tier 1** | MFA REQUIRED | Hardware token (preferred), authenticator app (acceptable) |
| **Tier 2** | MFA REQUIRED | Authenticator app, push notifications |

**Privileged Account MFA Enrollment**:
- **Deadline**: Within 7 days of privileged access grant
- **Verification**: IT Security verifies MFA before activating privileged rights
- **Non-compliance**: Privileged access revoked if MFA not enrolled within deadline

**MFA Bypass Prohibited**:
- ❌ No privileged access without MFA (even temporarily)
- ❌ No "MFA bypass" exceptions for convenience
- ✅ Break-glass accounts only exception (sealed, monitored, executive approval)

**Audit Evidence**: Privileged user MFA enrollment status (100% target), MFA method by tier

---

## 7. Privileged Access Monitoring and Logging

### 7.1 Requirement: Privileged Command Logging

**REQ-A82-019**: All privileged commands **MUST** be logged for audit and forensics.

**Privileged Command Logging Requirements**:

**Windows**:
- PowerShell script block logging (capture all PowerShell commands)
- Windows Event Logs for privileged access (Event ID 4672 - Special Logon, 4688 - Process Creation)
- Sysmon for detailed process monitoring

**Linux**:
- sudo logging (all sudo commands logged to syslog)
- aureport / auditd for command auditing
- Centralized logging (rsyslog forwarding to SIEM)

**Network Devices**:
- Command logging on routers, switches, firewalls (syslog)
- Enable highest logging level (informational or debug)

**Databases**:
- Database audit logging (SQL Server Audit, Oracle Audit, PostgreSQL pgaudit)
- Log DDL (Data Definition Language) commands (CREATE, ALTER, DROP)
- Log privileged access (sa, SYSTEM, postgres usage)

**Cloud Platforms**:
- AWS CloudTrail (logs all API calls, including privileged actions)
- Azure Activity Log (logs Azure resource changes)
- GCP Cloud Audit Logs

**Log Centralization**:
- Forward all privileged access logs to SIEM (Security Information and Event Management)
- Real-time analysis and correlation
- Long-term retention (minimum 90 days online, 1 year archived)

**Audit Evidence**: Privileged command logs, SIEM integration, log retention configuration

### 7.2 Requirement: Privileged Access Monitoring and Alerting

**REQ-A82-020**: Privileged access **MUST** be monitored for anomalies and security incidents.

**Privileged Access Alerts**:

| Alert | Threshold | Priority | Response Time |
|-------|-----------|----------|---------------|
| **Privileged account login outside business hours** | 10 PM - 6 AM weekdays, weekends | Medium | 1 hour |
| **Privileged account from unusual location** | New country/city never seen before | High | 30 minutes |
| **Tier 0 account activity** | ANY Tier 0 account activity | High | 15 minutes |
| **Tier isolation violation** | Tier 0 account logging into Tier 1/2 system | Critical | 5 minutes |
| **Privileged account failed logins** | 3 failed attempts in 5 minutes | High | 15 minutes |
| **Privileged session > 4 hours** | Session exceeds maximum duration | Medium | 1 hour |
| **Privileged account accessing unusual systems** | System never accessed before | Medium | 1 hour |
| **Break-glass account usage** | ANY break-glass account login | Critical | Immediate |

**Automated Response Actions**:
- Alert security team (email, SMS, Slack notification)
- Create incident ticket automatically (ServiceNow, Jira)
- Require additional MFA challenge (risk-based MFA)
- Terminate session if critical violation detected

**Privileged Access Dashboards**:
- Real-time dashboard showing active privileged sessions
- Privileged account usage statistics (most active accounts, systems accessed)
- Tier isolation compliance status
- Alert summary (open alerts, resolved alerts, response times)

**Audit Evidence**: Privileged access alert logs, response actions, incident tickets

---

## 8. Privileged Credential Rotation

### 8.1 Requirement: Automated Credential Rotation

**REQ-A82-021**: Shared privileged credentials **MUST** be rotated automatically.

**Credential Rotation Requirements**:

**Rotation Frequency**:

| Account Type | Rotation Frequency | Trigger |
|--------------|-------------------|---------|
| **Shared admin accounts** (root, Administrator, sa) | After each check-in from PAM | After use |
| **Service accounts** (if in PAM) | Daily | Automated schedule |
| **Break-glass accounts** | After each use | Manual after use |
| **Tier 0 accounts** | After each session | After use |
| **API keys/tokens** | 90 days | Scheduled |

**Rotation Mechanism**:
- **PAM solution**: CyberArk, BeyondTrust automatically rotate passwords after check-in
- **Group Managed Service Accounts (gMSA)**: Windows automatically rotates passwords (30 days)
- **Native scripts**: PowerShell / Python scripts for systems without PAM

**Rotation Verification**:
- After rotation, PAM verifies new password works (test login)
- If rotation fails, alert security team immediately
- Retry rotation automatically (up to 3 attempts)

**Rotation Exceptions**:
- Service accounts with application dependencies (coordinate rotation with application team)
- Accounts requiring manual rotation (legacy systems without API support)
- Document exceptions and remediation plans

**Audit Evidence**: Credential rotation logs, rotation frequency compliance, failed rotation alerts

---

## 9. Privileged Access Reviews

### 9.1 Requirement: Quarterly Privileged Access Reviews

**REQ-A82-022**: Privileged access **MUST** be reviewed quarterly to verify continued need.

**Quarterly Review Requirements**:

**Review Scope**:
- ALL privileged users (every person with privileged accounts)
- ALL privileged accounts (named, shared, service, break-glass)
- ALL admin tier assignments (Tier 0/1/2 classification)

**Review Questions**:
1. Does this user still require privileged access? (Still in role requiring admin access?)
2. Is the level of privilege appropriate? (Should Tier 1 be downgraded to Tier 2?)
3. Has the user used privileged access in last 90 days? (Unused access = remove)
4. Is business justification still valid?
5. Is MFA enabled and functional?

**Review Workflow**:
1. **Generate review report**: List all privileged users and accounts (from Workbook 3)
2. **Send to managers**: Each manager reviews their team's privileged access
3. **Manager attestation**: Manager confirms each user still needs access (or marks for removal)
4. **Security review**: Security team verifies attestations and performs spot checks
5. **Access removal**: Remove privileged access for users no longer needing it
6. **Documentation**: Document review results, approvals, and removals

**Review Metrics**:
- **Review completion rate**: 100% (all privileged users reviewed quarterly)
- **Access removal rate**: 5-10% (continuous cleanup of unneeded access)
- **Review timeliness**: Completed within 30 days of quarter end

**Annual Deep Review** (in addition to quarterly):
- Review ALL service accounts (are they still needed?)
- Review ALL break-glass accounts (do they work? Seals intact?)
- Review admin tier classifications (are systems/accounts correctly classified?)
- Review PAM solution configuration (are policies still appropriate?)

**Audit Evidence**: Quarterly review reports, manager attestations, access removal logs

---

## 10. Measurable Requirements and Audit Verification

### 10.1 Privileged Access Security Metrics

**Measurable requirements for audit verification**:

| Requirement | Metric | Target | Verification Method |
|-------------|--------|--------|---------------------|
| **Privileged accounts - named** | % named accounts (vs. shared) | 70%+ | Workbook 3 |
| **Privileged accounts in PAM** | % shared accounts vaulted | 100% | Workbook 3 |
| **Privileged MFA coverage** | % privileged users with MFA | 100% | Workbook 2 + 3 |
| **Tier 0 hardware MFA** | % Tier 0 with hardware tokens | 100% | Workbook 3 |
| **Tier 0 PAW deployment** | % Tier 0 admins with PAWs | 100% | Workbook 3 |
| **Session recording coverage** | % privileged sessions recorded | 90%+ | Workbook 4 |
| **Credential rotation** | % accounts with recent rotation | 95%+ | Workbook 3 |
| **Tier isolation compliance** | Cross-tier violations per month | <5 | Workbook 4 |
| **Quarterly review completion** | % privileged users reviewed | 100% | Workbook 4 |
| **Privileged access response time** | Avg. alert response time | <30 min | Workbook 4 |

### 10.2 Audit Evidence Requirements

**For ISO 27001:2022 A.8.2 audit**:

1. **Policy and procedures**: This document (ISMS-POL-A.8.2-3-5-S3)
2. **Privileged account inventory**: Workbook 3 (complete inventory with tier classification)
3. **PAM deployment**: PAM solution documentation, vaulted accounts list
4. **Session recordings**: Sample session recordings, recording retention policy
5. **MFA for privileged**: Privileged user MFA enrollment status (target 100%)
6. **Admin tiering**: Tier classification documentation, PAW deployment, tier isolation policies
7. **Privileged access monitoring**: Workbook 4 (activity logs, alerts, reviews)
8. **Credential rotation**: Rotation logs, frequency compliance
9. **Quarterly reviews**: Review reports, attestations, access removal documentation

---

**END OF SECTION 3 (PRIVILEGED ACCESS REQUIREMENTS - A.8.2)**

**Next Section**: ISMS-POL-A.8.2-3-5-S4 (Information Access Restriction Requirements - A.8.3)

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architecture Lead | Initial privileged access requirements (A.8.2) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**
