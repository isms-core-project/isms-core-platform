# ISMS-IMP-A.8.2-3-5-S3
## Privileged Access Management (PAM) Implementation Guide

**Document ID**: ISMS-IMP-A.8.2-3-5-S3  
**Title**: PAM and Admin Tiering Implementation  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Security Architecture Lead  
**Status**: Draft

---

## 1. PAM Implementation Overview

**Purpose**: Deploy Privileged Access Management solution and implement admin tiering model.

**Scope**:
- PAM solution selection and deployment
- Password vaulting for shared privileged accounts
- Just-in-time (JIT) access implementation
- Session recording deployment
- Admin Tiering Model (Tier 0/1/2) implementation
- Privileged Access Workstations (PAWs) deployment

---

## 2. PAM Solution Selection

### 2.1 Solution Comparison

| Solution | Best For | Strengths | Cost | Deployment |
|----------|----------|-----------|------|------------|
| **CyberArk** | Enterprise (1000+ users) | Most comprehensive, market leader | $$$$$ | Complex (3-6 months) |
| **BeyondTrust** | Mid-Enterprise (500-5000) | Good feature set, strong remote access | $$$$ | Moderate (2-4 months) |
| **Delinea Secret Server** | SMB-Mid (100-1000) | Easy to deploy, good value | $$$ | Fast (1-2 months) |
| **Azure PIM** | Microsoft shops | Native Azure AD integration, included in P2 | $$ (incl in license) | Fast (weeks) |
| **HashiCorp Vault** | Cloud-native, DevOps | Secrets management, API-driven | $ (open-source) / $$ (enterprise) | Moderate (2-3 months) |
| **Native Controls** | Budget-constrained | Free, minimal features | Free | Fast (weeks) |

### 2.2 Selection Criteria

**Choose CyberArk if**:
- Enterprise organization (Fortune 500)
- Highly regulated (finance, healthcare, government)
- Budget available ($$$$)
- Comprehensive PAM features required

**Choose BeyondTrust if**:
- Mid-large enterprise
- Need remote access management (vendor/contractor access)
- Good balance of features and cost

**Choose Delinea Secret Server if**:
- Small-medium business
- Need quick deployment
- Budget-conscious but want commercial PAM

**Choose Azure PIM if**:
- Already using Azure AD P2
- Cloud-first organization
- Need JIT for Azure AD roles specifically
- Limited budget (included in P2 license)

**Choose HashiCorp Vault if**:
- Cloud-native infrastructure (AWS, Azure, GCP, Kubernetes)
- DevOps/API-first approach
- Need secrets management for applications

**Choose Native Controls if**:
- Very small organization (<50 users)
- Budget constraints (no PAM budget)
- Use OS-level controls (Windows LAPS, sudo logging, etc.)

---

## 3. PAM Platform Deployment

### 3.1 CyberArk Deployment (Example)

**Architecture Components**:
```
CyberArk Vault (Database)
  ↓
CyberArk PVWA (Web Portal) ← Users request access
  ↓
CyberArk CPM (Central Policy Manager) → Rotates passwords
  ↓
CyberArk PSM (Privileged Session Manager) → Records sessions
```

**Deployment Steps**:
1. **Infrastructure Preparation** (Week 1):
   - Provision servers (Vault, PVWA, CPM, PSM)
   - Windows Server 2019/2022 for all components
   - SQL Server for Vault database
   - Network connectivity (dedicated management VLAN preferred)

2. **Vault Installation** (Week 2):
   - Install CyberArk Vault (primary)
   - Install CyberArk Vault DR (disaster recovery)
   - Configure Vault replication
   - Secure Vault server (hardening, firewall rules)

3. **PVWA Installation** (Week 2):
   - Install CyberArk Password Vault Web Access
   - Configure HTTPS (SSL certificate)
   - Integrate with Azure AD/AD for authentication
   - Configure MFA (RADIUS integration or Azure MFA)

4. **CPM Installation** (Week 3):
   - Install Central Policy Manager
   - Configure CPM plugins (Windows, Linux, databases, cloud)
   - Test password rotation on test accounts

5. **PSM Installation** (Week 3):
   - Install Privileged Session Manager
   - Configure session recording (video + keystroke)
   - Test RDP and SSH session proxying

6. **Account Onboarding** (Weeks 4-8):
   - Discover privileged accounts (scanning tools)
   - Import accounts into Vault
   - Verify credentials work
   - Rotate passwords immediately (old passwords invalid)

### 3.2 Azure PIM Deployment (Simpler Alternative)

**Enable Azure PIM**:
```
Azure AD → Privileged Identity Management → Azure AD roles

Steps:
1. Discover privileged roles (Global Admin, Security Admin, etc.)
2. Convert permanent assignments → eligible assignments
3. Configure activation requirements (MFA, justification, approval)
4. Set activation duration (max 8 hours, recommend 4 hours)
5. Configure alerts (activate alerts for privileged role activations)
```

**Activation Workflow**:
```
User needs Global Admin:
1. User → Azure PIM → "Activate Global Admin role"
2. User provides justification: "Need to configure Conditional Access policy"
3. User completes MFA
4. (Optional) Manager approves activation
5. Role activated for 4 hours
6. After 4 hours, role automatically deactivated
```

---

## 4. Privileged Account Onboarding

### 4.1 Account Discovery

**Discovery Methods**:

**Windows Active Directory**:
```powershell
# Find Domain Admins
Get-ADGroupMember "Domain Admins"

# Find Enterprise Admins
Get-ADGroupMember "Enterprise Admins"

# Find local Administrators on servers
$servers = Get-ADComputer -Filter 'OperatingSystem -like "*Server*"'
foreach ($server in $servers) {
  Get-LocalGroupMember -ComputerName $server.Name -Group "Administrators"
}
```

**Linux Servers**:
```bash
# Find users with sudo access
grep -r "sudo" /etc/sudoers /etc/sudoers.d/

# Find users with UID 0 (root privileges)
awk -F: '$3 == 0 { print $1 }' /etc/passwd
```

**Databases**:
```sql
-- SQL Server: Find sysadmin users
SELECT name FROM sys.server_principals 
WHERE IS_SRVROLEMEMBER('sysadmin', name) = 1

-- PostgreSQL: Find superusers
SELECT usename FROM pg_user WHERE usesuper = true
```

**Cloud Platforms**:
- AWS: `aws iam list-users --query 'Users[?PasswordLastUsed!=null]'`
- Azure: `Get-AzRoleAssignment -RoleDefinitionName "Owner"`
- GCP: `gcloud projects get-iam-policy [PROJECT_ID]`

### 4.2 Account Onboarding to PAM Vault

**Onboarding Process**:
1. **Identify account**: root on linux-server-01
2. **Create safe in PAM**: "Linux-Production-Servers"
3. **Add account to safe**: 
   - Account name: root@linux-server-01
   - Password: [current password - manually entered]
   - Platform: Unix SSH
4. **Test credential**: PAM connects to server and verifies password works
5. **Rotate password**: PAM changes password to random 32-character string
6. **Verify rotation**: PAM confirms new password works
7. **Old password invalid**: Previous password no longer works (security improvement)

**Onboarding Priority**:
1. **Tier 0 accounts first** (Domain Admin, Enterprise Admin, root on DCs)
2. **Tier 1 production** (sa, SYSTEM, admin on production servers)
3. **Tier 1 non-production** (dev/test servers)
4. **Tier 2 accounts** (workstation local admin)

---

## 5. Password Vaulting and Check-Out

### 5.1 Check-Out Workflow

**Standard Workflow**:
```
Admin needs access:
1. Admin logs into PAM portal (PVWA, CyberArk, etc.)
2. Admin searches for account (e.g., "root@linux-server-01")
3. Admin clicks "Check Out" or "Connect"
4. PAM provides password (copy-paste) OR launches session (PSM)
5. Admin performs task
6. Admin clicks "Check In" or session ends
7. PAM rotates password (new password generated, admin doesn't know it)
```

**Exclusive Check-Out**:
- Only ONE admin can check out account at a time
- Prevents conflicts (two admins making changes simultaneously)
- Other admins see "Account in use by John Doe"

**Time-Limited Check-Out**:
- Check-out valid for X hours (e.g., 4 hours)
- After time limit, account auto-checks in
- Password rotated after check-in

### 5.2 Automated Password Rotation

**Rotation Frequency**:
- After each check-in (most secure - password changes after each use)
- Daily (scheduled rotation)
- Weekly (for accounts used frequently)

**Rotation Process**:
```
CyberArk CPM:
1. Connects to system (Linux server, Windows server, database)
2. Changes password using API or CLI (passwd command, ALTER USER, etc.)
3. Verifies new password works (test login)
4. Updates password in Vault
5. Logs rotation event
```

**Rotation Verification**:
```
# Linux password change (CyberArk CPM)
ssh root@linux-server-01 'echo "root:NEW_PASSWORD" | chpasswd'

# Windows password change (PowerShell)
Set-ADAccountPassword -Identity Administrator -NewPassword (ConvertTo-SecureString "NEW_PASSWORD" -AsPlainText -Force)

# SQL Server password change
ALTER LOGIN sa WITH PASSWORD = 'NEW_PASSWORD'
```

---

## 6. Session Recording Implementation

### 6.1 Session Recording Architecture

**Recording Methods**:
1. **Proxy-based** (CyberArk PSM, BeyondTrust):
   - User connects to PAM server → PAM proxies connection to target
   - PAM records all session activity
   - Works for: RDP, SSH, database, web-based admin

2. **Agent-based** (Ekran System, ObserveIT):
   - Agent installed on target system
   - Agent records local sessions
   - Works for: Local console access

### 6.2 Session Recording Configuration

**What to Record**:
- **Mandatory**: All Tier 0 sessions (100% coverage)
- **Highly Recommended**: All Tier 1 production sessions
- **Recommended**: Tier 2 sessions on sensitive systems

**Recording Type**:
- **RDP sessions**: Video recording (screen capture)
- **SSH sessions**: Keystroke logging (text-based, searchable)
- **Database sessions**: Query logging (SQL commands executed)

**Recording Storage**:
- Retention: 90 days online, 1 year archived
- Storage location: Dedicated storage (not on PAM server - avoid resource contention)
- Encryption: Recordings encrypted at rest
- Access control: Only security team can view recordings

**Playback Features**:
- Fast-forward/rewind
- Search by command (SSH sessions)
- Export recording (for incident investigation)

---

## 7. Admin Tiering Model Implementation

### 7.1 Tier Classification

**Step 1: Classify All Systems**:
```
Tier 0 Systems:
- Domain controllers (ad-dc-01, ad-dc-02)
- Azure AD tenant (entire tenant)
- AWS Organization root
- SIEM (Splunk, Datadog)
- PAM vault (CyberArk, BeyondTrust)
- Backup infrastructure (Veeam servers)
- Certificate Authority (PKI CA servers)

Tier 1 Systems:
- Production servers (web-prod-01, db-prod-01)
- Application servers (sap-app-01, crm-app-01)
- Database servers (sql-prod-01, oracle-prod-01)
- Cloud VMs (AWS EC2, Azure VMs)

Tier 2 Systems:
- End-user workstations (laptops, desktops)
- Mobile devices (smartphones, tablets)
```

**Step 2: Classify All Privileged Accounts**:
```
Tier 0 Accounts:
- Domain Admins, Enterprise Admins
- Azure Global Administrator
- AWS root user
- SIEM administrators
- PAM administrators

Tier 1 Accounts:
- Server administrators
- Database administrators (DBAs)
- Application administrators
- Cloud infrastructure admins (not global admin)

Tier 2 Accounts:
- Workstation local admins
- MDM administrators (Intune, Jamf)
```

### 7.2 Create Separate Admin Accounts per Tier

**Account Naming Convention**:
```
Standard user account: john.doe
Tier 2 admin account: john.doe.tier2 (or adm2-john.doe)
Tier 1 admin account: john.doe.tier1 (or adm1-john.doe)
Tier 0 admin account: john.doe.tier0 (or adm0-john.doe)
```

**Account Creation**:
```powershell
# Create Tier 0 account (Active Directory)
New-ADUser -Name "john.doe.tier0" `
  -UserPrincipalName "john.doe.tier0@domain.com" `
  -Enabled $true `
  -ChangePasswordAtLogon $true `
  -Description "Tier 0 Admin - John Doe"

# Add to Domain Admins (Tier 0 group)
Add-ADGroupMember -Identity "Domain Admins" -Members "john.doe.tier0"
```

**User Training**:
- John has 3 accounts now: john.doe, john.doe.tier1, john.doe.tier0
- Use john.doe for email, documents, daily work (95% of time)
- Use john.doe.tier1 for server administration
- Use john.doe.tier0 ONLY for domain controller/critical infrastructure tasks
- NEVER use john.doe.tier0 for email or web browsing

### 7.3 Tier Isolation Enforcement

**Group Policy Objects (GPO) - Windows**:
```
GPO: "Deny Tier 0 Accounts on Tier 1/2 Systems"
Linked to: Tier 1 Servers OU, Tier 2 Workstations OU

Computer Configuration → Policies → Windows Settings → 
Security Settings → Local Policies → User Rights Assignment

Deny log on locally: Domain\Tier0-Admins
Deny log on through Remote Desktop Services: Domain\Tier0-Admins

Result: Tier 0 accounts CANNOT log into Tier 1/2 systems
```

**Azure Conditional Access**:
```
Policy: "Tier 0 - PAWs Only"
Assignments:
  Users: Tier 0 admin group
  Cloud apps: All apps
  Conditions: 
    Locations: Any
    Device platforms: Windows, macOS, Linux
Access controls:
  Grant: Require device to be marked as compliant (only PAWs are compliant)
  OR: Require specific device (allowlist of PAW devices)
```

**Monitoring Tier Violations**:
```
Alert: "Tier 0 Account on Non-PAW Device"
Query: 
  Event: User login
  User: Member of Tier0-Admins group
  Device: NOT in PAW device list
Action: 
  - Terminate session immediately
  - Alert security team (critical priority)
  - Investigate (legitimate need or compromise?)
```

---

## 8. Privileged Access Workstations (PAWs)

### 8.1 PAW Purpose and Architecture

**Why PAWs?**:
- Tier 0 accounts have access to EVERYTHING
- If Tier 0 credential cached on user's laptop → laptop compromised → attacker gets Tier 0
- PAW = dedicated hardened workstation for Tier 0 administration ONLY

**PAW Restrictions**:
- NO email (Outlook, Gmail, etc.)
- NO web browsing (except admin portals)
- NO USB drives (disabled)
- NO internet access (except whitelisted admin portals)
- ONLY remote desktop to Tier 0 systems

### 8.2 PAW Deployment

**Hardware**:
- Dedicated laptop or desktop (one PAW per Tier 0 admin)
- Moderate specs (8GB RAM, SSD sufficient - not heavy workload)
- Physical security (locked in office when not in use)

**Software Configuration**:
```
Operating System: Windows 11 Enterprise (most recent)
Security Baseline: Microsoft Security Compliance Toolkit
Hardening:
- AppLocker (only approved admin tools can run)
- Windows Firewall (block all except RDP, HTTPS to admin portals)
- Credential Guard (protect credentials in memory)
- BitLocker (full disk encryption)
- LAPS (local admin password managed)
- No local admin (user cannot install software)

Applications Allowed:
- Remote Desktop Connection (RDP to Tier 0 systems)
- Privileged Access Management portal (PVWA, etc.)
- PowerShell (for admin scripts)
- Azure/AWS/GCP admin portals (web-based)
- Nothing else (no email, no browser for general use)
```

**PAW User Experience**:
```
John needs to perform Tier 0 task:
1. John uses his PAW laptop (dedicated device)
2. John logs in with john.doe.tier0@domain.com + hardware MFA
3. John RDPs to domain controller from PAW
4. John performs admin task
5. John logs out

John NEVER uses PAW for email, web browsing, or daily work
John uses his standard laptop for daily work (john.doe account)
```

### 8.3 PAW Alternatives (If Budget Constrained)

**Jump Servers** (less secure than PAWs but better than nothing):
- Dedicated VM for Tier 0 administration
- Admins RDP to jump server → then RDP to Tier 0 systems
- Jump server hardened (no email, no web browsing)
- Cheaper than dedicated laptops (one VM vs. many laptops)

**Azure Bastion** (cloud jump service):
- Managed jump service for Azure VMs
- No need to deploy and manage jump servers
- Access via Azure portal (HTTPS)
- Session recording built-in

---

## 9. Just-in-Time (JIT) Access

### 9.1 Azure PIM JIT Implementation

**JIT Workflow**:
```
User needs Global Admin temporarily:
1. User → Azure PIM → "Activate Global Admin"
2. User provides justification: "Need to configure Conditional Access"
3. User completes MFA
4. (Optional) Manager/Security approves
5. Role activated for 4 hours (configurable 1-8 hours)
6. User performs administrative task
7. After 4 hours, role auto-deactivated (user is no longer Global Admin)
```

**Configuration**:
```
Azure AD → PIM → Azure AD roles → Settings → Global Administrator

Activation:
- Maximum duration: 4 hours
- Require MFA: Yes
- Require justification: Yes
- Require approval: Yes (for high-risk roles like Global Admin)

Assignment:
- Allow permanent eligible assignment: Yes
- Allow permanent active assignment: No (force JIT)
```

### 9.2 AWS IAM Temporary Credentials

**AssumeRole for JIT**:
```python
# Admin assumes privileged role temporarily
import boto3

sts = boto3.client('sts')
response = sts.assume_role(
    RoleArn='arn:aws:iam::123456789012:role/AdminRole',
    RoleSessionName='john-admin-session',
    DurationSeconds=14400  # 4 hours
)

credentials = response['Credentials']
# Use temporary credentials for 4 hours
# After 4 hours, credentials automatically expire
```

---

## 10. Implementation Checklist

**Phase 1: PAM Platform Deployment** (Months 1-3):
- [ ] PAM solution selected
- [ ] PAM infrastructure deployed (Vault, PVWA, CPM, PSM)
- [ ] Test environment configured
- [ ] Pilot account onboarded and tested

**Phase 2: Account Onboarding** (Months 4-6):
- [ ] Tier 0 accounts discovered and documented
- [ ] Tier 0 accounts onboarded to PAM vault
- [ ] Password rotation configured and tested
- [ ] Tier 1 production accounts onboarded
- [ ] Session recording enabled for Tier 0 accounts

**Phase 3: Admin Tiering** (Months 7-9):
- [ ] All systems classified into tiers (Tier 0/1/2)
- [ ] All accounts classified into tiers
- [ ] Separate admin accounts created per tier (john.tier0, john.tier1)
- [ ] Tier isolation GPOs deployed
- [ ] Tier violation monitoring enabled

**Phase 4: PAWs Deployment** (Months 10-12):
- [ ] PAW hardware procured (one per Tier 0 admin)
- [ ] PAW image created (hardened Windows 11)
- [ ] PAWs deployed to Tier 0 admins
- [ ] Conditional Access policies enforce PAW usage
- [ ] Tier 0 admins trained on PAW usage

**Phase 5: JIT Implementation** (Month 12+):
- [ ] Azure PIM configured for Azure AD roles
- [ ] Permanent Tier 0 assignments converted to eligible
- [ ] JIT activation workflows tested
- [ ] JIT adoption measured

---

**END OF IMPLEMENTATION GUIDE S3**

**Next**: IMP-S4 (Access Enforcement), IMP-S5 (Security Assessment), then scripts
