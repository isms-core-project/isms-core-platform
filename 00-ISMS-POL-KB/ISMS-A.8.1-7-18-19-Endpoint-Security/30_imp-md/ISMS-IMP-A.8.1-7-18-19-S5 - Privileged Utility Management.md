# ISMS-IMP-A.8.1-7-18-19-S5 - Privileged Utility Management
## Practical Implementation Guidance for Privileged Utility Controls
### ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19

---

## Document Control

| **Attribute** | **Details** |
|---------------|-------------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S5 |
| **Document Title** | Privileged Utility Management |
| **Version** | 1.0 |
| **Date** | [Date] |
| **Classification** | Internal |
| **Document Owner** | Information Security Manager / ISMS Implementation Lead |
| **Status** | Active |
| **Review Cycle** | Annual (or when privileged utility requirements change) |
| **Parent Document** | ISMS-POL-A.8.1-7-18-19 (Endpoint Security Framework) |
| **Related Documents** | ISMS-POL-A.8.1-7-18-19-S4 (Privileged Utilities Requirements - A.8.18)<br>ISMS-POL-A.8.2 (Privileged Access Rights)<br>ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process)<br>ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process)<br>ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment) |

---

## 1. Purpose and Scope

### 1.1 Purpose

This document provides **practical, step-by-step guidance** for implementing privileged utility management controls to implement **Control A.8.18 (Use of Privileged Utility Programs)** requirements.

**Privileged utility management** involves:
- Systematically discovering privileged utilities on all endpoints
- Classifying utilities by risk level (Critical, High, Medium, Low)
- Implementing strict access controls (RBAC, file permissions, application control)
- Establishing approval workflows (standing access, JIT access, emergency access)
- Configuring comprehensive logging and monitoring
- Integrating with SIEM for correlation and alerting
- Conducting quarterly access reviews
- Managing security bypass tools

### 1.2 Scope

This guidance covers implementation for:

- **Windows Endpoints**: PowerShell, CMD, Registry Editor, MMC snap-ins, Sysinternals tools
- **macOS Endpoints**: Terminal, System Preferences, launchctl, diskutil
- **Linux Endpoints**: bash/sh, sudo, systemctl, iptables
- **Cross-Platform**: Remote access tools, debuggers, packet sniffers
- **Security Bypass Tools**: Password recovery, encryption bypass, secure delete tools

### 1.3 Applicability

This guidance is **technology-agnostic** while providing specific examples for common platforms and tools. Implementers should adapt procedures to their environment.

**Key Principle**: Privileged utilities can bypass security controls - they require the strictest controls and comprehensive monitoring.

### 1.4 Who Should Use This Guidance

- Security managers implementing A.8.18 controls
- System administrators managing privileged access
- IT operations teams configuring access controls and logging
- ISMS implementers preparing for privileged utility assessments

---

## 2. Process Overview

### 2.1 Privileged Utility Management Workflow

```
┌────────────────────────────────────────────────────────────────────┐
│         PRIVILEGED UTILITY MANAGEMENT IMPLEMENTATION PROCESS       │
└────────────────────────────────────────────────────────────────────┘

Phase 1: Privileged Utility Discovery
├─ Automated discovery (software inventory scans)
├─ Manual discovery (administrator surveys)
├─ Categorize by type (system admin, debugging, security bypass, etc.)
├─ Classify by risk (Critical, High, Medium, Low)
└─ Document in inventory

Phase 2: Access Control Implementation
├─ Define authorized roles (IT Admins, Security Analysts, etc.)
├─ Implement RBAC (role-based access control)
├─ Configure file permissions (restrict execution)
├─ Deploy AppLocker/application control rules
├─ Test access controls (verify unauthorized users blocked)
└─ Document access control configuration

Phase 3: Approval Workflow Setup
├─ Define access types (standing, temporary, JIT, emergency)
├─ Create approval request form/workflow
├─ Configure approval routing (Security Manager, CISO)
├─ Implement JIT access (PAM solution or scripted)
├─ Document approval procedures
└─ Train administrators on approval process

Phase 4: MFA Implementation
├─ Assess MFA feasibility per utility type
├─ Configure MFA for privileged sessions
├─ Deploy hardware tokens or authenticator apps
├─ Test MFA enforcement
└─ Document MFA implementation and exceptions

Phase 5: Logging Configuration
├─ Enable privileged utility logging (Windows Event Log, auditd, etc.)
├─ Configure PowerShell logging (Windows)
├─ Configure sudo logging (Linux)
├─ Deploy Sysmon (Windows - enhanced logging)
├─ Test logging (execute utility, verify log generated)
└─ Document logging configuration

Phase 6: SIEM Integration
├─ Forward privileged utility logs to SIEM
├─ Create SIEM correlation rules (anomaly detection)
├─ Configure SIEM alerts (high-risk utility usage)
├─ Test SIEM integration (trigger alert, verify received)
└─ Document SIEM integration

Phase 7: Quarterly Access Review Setup
├─ Schedule quarterly access reviews
├─ Create access review report template
├─ Train managers on review process
├─ Execute first quarterly review
├─ Track access removals/changes
└─ Document review results

Phase 8: Continuous Monitoring
├─ Daily: SIEM alert review (unauthorized privileged utility usage)
├─ Weekly: Privileged utility usage log review
├─ Monthly: Access inventory verification (new utilities detected?)
├─ Quarterly: Access reviews (manager attestations)
└─ Annual: Comprehensive privileged utility audit
```

### 2.2 Key Principles

- **Least Privilege**: Only users who absolutely need privileged utilities should have access
- **Separation of Duties**: Users should not have access to privileged utilities that conflict with their role
- **Defense in Depth**: Multiple layers (access control + logging + monitoring + review)
- **Assume Breach**: Comprehensive logging because privileged utilities may be used maliciously
- **Transparency**: All privileged utility usage must be auditable
- **Just-in-Time Access**: High-risk utilities should use JIT access (temporary, auto-expire)

---

## 3. Prerequisites and Tools

### 3.1 Required Access and Permissions

**Endpoint Access**:
- **Administrative access** to endpoints for configuration (file permissions, AppLocker, logging)
- **Group Policy Management** (Windows AD environments)
- **MDM/Intune Admin** (cloud-managed endpoints)

**Identity and Access Management**:
- **Active Directory** or **Azure AD** admin access (for group management, RBAC)
- **PAM Solution Admin** (if implementing JIT access via PAM)

**Logging and Monitoring**:
- **SIEM Administrator** access (for log forwarding, correlation rules, alerts)
- **Endpoint Management** tools (SCCM, Intune, Jamf) for configuration deployment

### 3.2 Privileged Utility Inventory Tools

| Tool | Platform | Purpose | Type |
|------|----------|---------|------|
| **Software Inventory** | Windows, macOS, Linux | Detect installed utilities via inventory | Built-in (SCCM, Intune, Jamf) |
| **PowerShell Scripts** | Windows | Custom inventory scripts | Open-source |
| **Osquery** | Windows, macOS, Linux | SQL-based endpoint queries | Open-source |
| **File System Scanning** | All | Search for known privileged utility paths | Custom scripts |

### 3.3 Access Control Technologies

| Technology | Platform | Purpose | Type |
|------------|----------|---------|------|
| **RBAC (Role-Based Access Control)** | All | Group-based access management | Built-in (AD, Azure AD) |
| **File Permissions** | All | Restrict file execution | Built-in (NTFS, POSIX) |
| **AppLocker** | Windows | Application allowlist/denylist | Built-in |
| **WDAC** | Windows | Code integrity policies | Built-in |
| **sudo** | Linux | Privileged command execution control | Built-in |

### 3.4 Logging Technologies

| Technology | Platform | Purpose | Type |
|------------|----------|---------|------|
| **Windows Event Log** | Windows | Process creation, privilege use events | Built-in |
| **PowerShell Logging** | Windows | Script block logging, transcription | Built-in |
| **Sysmon** | Windows | Enhanced process/network/file logging | Microsoft (free) |
| **auditd** | Linux | System call auditing | Built-in |
| **Unified Logging** | macOS | System and application logging | Built-in |

### 3.5 Privileged Access Management (PAM) Solutions

**For JIT Access Implementation**:
- **CyberArk**: Enterprise PAM solution (full-featured, expensive)
- **BeyondTrust**: Privileged account and session management
- **Delinea (Thycotic)**: Secret Server, PAM solution
- **Azure AD PIM**: Cloud-native JIT for Azure AD (Microsoft environments)
- **HashiCorp Vault**: Secrets management with JIT access

**Minimum Requirements** (if PAM solution not available):
- Scripted JIT access (PowerShell, bash scripts with time-limited group membership)
- Manual approval process (ticketing system)
- Enhanced logging (compensating control)

---

## 4. Privileged Utility Discovery

### 4.1 Define Privileged Utility Categories

**Before discovery, define what constitutes a "privileged utility"** (per POL-S4 Section 2.1):

**Category 1: System Administration Tools**
- Windows: PowerShell (unrestricted), CMD (admin), Registry Editor, Group Policy Editor, MMC snap-ins, WMIC
- macOS: Terminal (root), System Preferences (privileged), launchctl, diskutil
- Linux: bash/sh (root), sudo, su, systemctl, iptables, useradd, passwd

**Category 2: Debugging and Development Tools**
- Debuggers: WinDbg, gdb, lldb, Visual Studio debugger
- Scripting interpreters with elevated privileges: Python (admin), Ruby, Perl
- Compilers on production endpoints: gcc, Visual Studio (should not be on production)

**Category 3: Security Bypass Tools**
- Password recovery: Ophcrack, John the Ripper, hashcat
- Encryption bypass: Elcomsoft tools
- Registry editors: regedit (can bypass security policies)

**Category 4: Network and Monitoring Tools**
- Packet sniffers: Wireshark, tcpdump, tshark
- Network scanners: nmap, Nessus, OpenVAS
- Remote access with admin rights: SSH (root), RDP (admin), VNC (admin)

**Category 5: Disk and File Utilities**
- Disk editors: HxD, WinHex (hex editors)
- Partition managers: DiskPart, GParted
- Secure delete tools: SDelete, shred

**Category 6: Third-Party Administrative Tools**
- Sysinternals Suite: PsExec, Process Explorer, Autoruns, AccessChk
- Remote admin tools: TeamViewer, AnyDesk (when used with admin privileges)

### 4.2 Automated Discovery via Software Inventory

**Using Intune** (Windows/macOS/mobile):

1. **Apps → Discovered apps → Export**
2. Filter exported CSV for known privileged utilities:
   ```python
   import pandas as pd
   
   # Load discovered apps
   df = pd.read_csv('discovered_apps.csv')
   
   # Define privileged utility keywords
   privileged_keywords = [
       'powershell', 'cmd', 'regedit', 'mmc', 'psexec', 'wireshark',
       'terminal', 'debugger', 'windbg', 'gdb', 'nmap', 'sdelete'
   ]
   
   # Filter for privileged utilities
   df_privileged = df[df['Application'].str.lower().str.contains('|'.join(privileged_keywords), na=False)]
   
   # Export
   df_privileged.to_csv('privileged_utilities_discovered.csv', index=False)
   ```

**Using SCCM**:

1. **Monitoring → Reporting → Reports → Software - Files**
2. Run report: "All inventoried files for a specific product"
3. Search for known privileged utilities (e.g., "powershell.exe", "regedit.exe")
4. Export results

**Using PowerShell** (Windows, direct endpoint query):

```powershell
# Discover privileged utilities on local endpoint
$privilegedPaths = @(
    "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
    "C:\Windows\System32\regedit.exe",
    "C:\Windows\System32\cmd.exe",
    "C:\Windows\System32\mmc.exe",
    "C:\Program Files\Sysinternals\*",
    "C:\Program Files\Wireshark\*"
)

$results = @()

foreach ($path in $privilegedPaths) {
    if (Test-Path $path) {
        $item = Get-Item $path
        $results += [PSCustomObject]@{
            Path = $item.FullName
            Name = $item.Name
            Version = $item.VersionInfo.FileVersion
            Exists = $true
        }
    }
}

$results | Export-Csv -Path "C:\Temp\PrivilegedUtilities.csv" -NoTypeInformation
```

**Using Osquery** (Linux/macOS):

```bash
# macOS: Find privileged utilities
osqueryi "SELECT name, path, bundle_identifier FROM apps WHERE path LIKE '%Terminal%' OR name LIKE '%Disk Utility%';"

# Linux: Find sudo configuration
osqueryi "SELECT * FROM sudoers;"

# Linux: Find installed debugging tools
osqueryi "SELECT name, version FROM deb_packages WHERE name IN ('gdb', 'strace', 'tcpdump');"
```

### 4.3 Manual Discovery via Administrator Survey

**Some privileged utilities may not be detected via automated inventory** (portable tools, custom scripts, cloud-based tools).

**Survey Template** (email to all administrators):

```
Subject: Privileged Utility Inventory Survey - Action Required

Dear Administrator,

We are conducting an inventory of privileged utilities across our endpoints. Please help us by completing this survey:

1. List all privileged utilities you use in your role (examples: PowerShell, PsExec, debuggers, packet sniffers, registry editors, remote admin tools):

   Utility 1: _______________
   Utility 2: _______________
   Utility 3: _______________
   [Add more as needed]

2. For each utility, indicate:
   - Frequency of use: Daily / Weekly / Monthly / Rarely
   - Purpose: Why do you need this utility? (brief description)
   - Platforms: Windows / macOS / Linux / Other

3. Are there any portable or cloud-based privileged tools not installed on your endpoint but used regularly (e.g., portable SSH clients, cloud-based admin consoles)?

   Tool: _______________
   Purpose: _______________

Please respond by [Date]. This information is confidential and used for security controls implementation only.

Thank you,
Information Security Team
```

**Survey Analysis**:
- Compile responses
- Identify utilities not discovered via automated inventory
- Cross-reference with known privileged utility lists
- Add to inventory

### 4.4 Risk Classification

**Classify each discovered privileged utility by risk level** (per POL-S4 REQ-A818-002):

**Risk Classification Criteria**:

| Risk Level | Capabilities | Access Controls Required |
|------------|--------------|--------------------------|
| **Critical** | Disable security controls, destroy evidence, bypass all access controls | JIT access only, MFA required, extensive logging, quarterly reviews, CISO approval |
| **High** | Modify system config, elevate privileges, access sensitive data | Approval required, MFA required, comprehensive logging, semi-annual reviews, Security Manager approval |
| **Medium** | Access files beyond normal permissions, limited system modifications | Approval required, logging enabled, annual reviews |
| **Low** | Limited bypass capability, well-controlled | Access restriction, basic logging |

**Example Risk Classifications**:

| Utility | Platform | Risk Level | Justification |
|---------|----------|------------|---------------|
| **PsExec** | Windows | Critical | Remote code execution, can bypass application control |
| **PowerShell (unrestricted)** | Windows | High | Can execute arbitrary code, modify system, access registry |
| **Wireshark** | Cross-platform | High | Packet capture, can capture credentials |
| **Registry Editor** | Windows | Medium | Can modify registry, bypass some security policies |
| **CMD (admin)** | Windows | Medium | Administrative command execution |
| **PowerShell (constrained)** | Windows | Low | Limited cmdlet access, restricted operations |

**Documentation**:

Create **Privileged Utility Inventory** spreadsheet:

| Utility | Platform | Category | Risk Level | Business Justification | Authorized Roles | Notes |
|---------|----------|----------|------------|------------------------|------------------|-------|
| PsExec | Windows | Third-Party Admin | Critical | Remote troubleshooting, incident response | IT Admins, Security Analysts | Sysinternals tool |
| PowerShell | Windows | System Admin | High | Automation, system management | IT Admins, DevOps | Unrestricted execution policy |
| Registry Editor | Windows | System Admin | Medium | Troubleshooting, configuration changes | IT Admins | Built-in Windows tool |

---

## 5. Access Control Implementation

### 5.1 Define Authorized Roles

**Step 1: Identify roles requiring privileged utility access**

**Example Roles**:
- **IT Administrators**: System management, troubleshooting
- **Security Analysts**: Security monitoring, incident response
- **DevOps Engineers**: Automation, deployment, infrastructure management
- **Database Administrators**: Database management (may need specialized utilities)
- **Network Administrators**: Network troubleshooting (packet sniffers, network tools)

**Step 2: Map utilities to roles**

| Role | Authorized Utilities | Business Justification |
|------|----------------------|------------------------|
| **IT Administrators** | PowerShell, CMD, Registry Editor, MMC, Remote Desktop (admin), PsExec | System administration and troubleshooting |
| **Security Analysts** | Wireshark, nmap, PsExec (for incident response), PowerShell | Security monitoring, incident response, forensics |
| **DevOps Engineers** | PowerShell, bash/ssh, git, Docker CLI, kubectl | Automation, CI/CD, infrastructure as code |
| **Database Administrators** | SQL Management Studio, database utilities | Database administration |
| **Network Administrators** | Wireshark, tcpdump, nmap, SSH | Network troubleshooting and monitoring |

**Step 3: Create Active Directory / Azure AD Security Groups**

**Windows (Active Directory)**:

```powershell
# Create security groups for privileged utility access
New-ADGroup -Name "PrivUtil-ITAdmins" -GroupScope Global -GroupCategory Security -Description "Access to IT administrative utilities"
New-ADGroup -Name "PrivUtil-SecurityAnalysts" -GroupScope Global -GroupCategory Security -Description "Access to security analysis utilities"
New-ADGroup -Name "PrivUtil-DevOps" -GroupScope Global -GroupCategory Security -Description "Access to DevOps automation utilities"

# Add users to groups
Add-ADGroupMember -Identity "PrivUtil-ITAdmins" -Members "john.smith-admin", "jane.doe-admin"
Add-ADGroupMember -Identity "PrivUtil-SecurityAnalysts" -Members "bob.jones-admin"
```

**Azure AD** (cloud-managed):

1. **Azure AD → Groups → New group**
2. **Group type**: Security
3. **Group name**: PrivUtil-ITAdmins
4. **Members**: Add admin accounts (john.smith-admin@organization.com)
5. **Create**

### 5.2 Implement File Permission Restrictions (Windows)

**Restrict execution of privileged utilities via NTFS permissions**.

**Example: Restrict PowerShell to IT Admins only**

1. **Navigate to PowerShell directory**:
   ```
   C:\Windows\System32\WindowsPowerShell\v1.0\
   ```

2. **Right-click powershell.exe → Properties → Security → Advanced**

3. **Disable inheritance**: "Disable inheritance" → "Convert inherited permissions into explicit permissions"

4. **Remove standard users**: Remove "Users" and "Authenticated Users" groups

5. **Add authorized group**:
   - **Add** → **Select a principal** → Enter: `PrivUtil-ITAdmins`
   - **Permissions**: Read & Execute
   - **Apply**

6. **Keep built-in admins**: Ensure "Administrators" and "SYSTEM" retain Full Control

**Verification**:
- Log in as standard user (non-admin)
- Attempt to run: `powershell.exe`
- **Expected**: Access denied (NTFS permission denied)

**Deployment at Scale** (via PowerShell script):

```powershell
# Script to restrict PowerShell access
$psPath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$authorizedGroup = "DOMAIN\PrivUtil-ITAdmins"

# Get current ACL
$acl = Get-Acl $psPath

# Disable inheritance
$acl.SetAccessRuleProtection($true, $true)

# Remove Users and Authenticated Users
$acl.Access | Where-Object { $_.IdentityReference -match "Users|Authenticated Users" } | ForEach-Object {
    $acl.RemoveAccessRule($_)
}

# Add authorized group
$permission = New-Object System.Security.AccessControl.FileSystemAccessRule(
    $authorizedGroup, "ReadAndExecute", "Allow"
)
$acl.AddAccessRule($permission)

# Apply ACL
Set-Acl -Path $psPath -AclObject $acl

Write-Host "PowerShell access restricted to $authorizedGroup"
```

**Deploy via GPO** (Startup Script):
- **Group Policy → Computer Configuration → Windows Settings → Scripts (Startup/Shutdown)**
- Add script: Restrict-PowerShellAccess.ps1
- Apply to all endpoints

### 5.3 Implement File Permission Restrictions (Linux)

**Restrict sudo and privileged utilities via file permissions and sudo configuration**.

**Example: Restrict sudo to IT Admins group**

1. **Create group**:
   ```bash
   sudo groupadd itadmins
   ```

2. **Add users to group**:
   ```bash
   sudo usermod -aG itadmins john.smith
   sudo usermod -aG itadmins jane.doe
   ```

3. **Configure sudo** (`/etc/sudoers` via `visudo`):
   ```bash
   sudo visudo
   ```

   **Add line**:
   ```
   %itadmins ALL=(ALL:ALL) ALL
   ```

   **Remove broad sudo access** (if present):
   ```
   # Comment out or remove lines like:
   # %sudo ALL=(ALL:ALL) ALL
   ```

4. **Restrict direct root access** (optional):
   ```bash
   # Lock root account (no direct root login)
   sudo passwd -l root
   ```

**Verification**:
- Log in as standard user (not in itadmins group)
- Attempt: `sudo ls`
- **Expected**: `user is not in the sudoers file. This incident will be reported.`

**Restrict Specific Commands** (advanced sudo configuration):

```bash
# Allow itadmins to run all commands
%itadmins ALL=(ALL:ALL) ALL

# Allow developers to run only specific commands (no full sudo)
%developers ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp, /usr/bin/tail -f /var/log/myapp/*
```

### 5.4 Implement AppLocker Rules (Windows)

**Restrict privileged utilities via AppLocker** (additional layer beyond file permissions).

**Example: Block PsExec except for IT Admins**

1. **Group Policy → Computer Configuration → Policies → Windows Settings → Security Settings → Application Control Policies → AppLocker**

2. **Executable Rules → Create New Rule**:
   - **Permissions**: Deny
   - **User or Group**: Everyone
   - **Conditions**: File Hash
   - **Browse**: Select PsExec.exe
   - **Create**

3. **Create Allow Rule for IT Admins**:
   - **Executable Rules → Create New Rule**
   - **Permissions**: Allow
   - **User or Group**: DOMAIN\PrivUtil-ITAdmins
   - **Conditions**: File Hash
   - **Browse**: Select PsExec.exe
   - **Create**

**Rule Evaluation Order**: AppLocker evaluates Deny rules before Allow rules. Configuration:
- Deny Everyone (PsExec.exe)
- Allow PrivUtil-ITAdmins (PsExec.exe)
- Result: Only IT Admins can execute PsExec

**Verification**:
- Log in as standard user
- Attempt to run PsExec.exe
- **Expected**: AppLocker blocks execution, event logged

---

## 6. Approval Workflow Implementation

### 6.1 Define Access Types and Approval Authorities

**Access Types** (per POL-S4 REQ-A818-006):

| Access Type | Description | Approval Authority | Duration | Recertification |
|-------------|-------------|--------------------|----------|-----------------|
| **Standing Access** | Permanent privileged access for job role | Security Manager + User's Manager | Permanent | Annual |
| **Temporary Access** | Time-limited for specific project | Security Manager | Max 90 days | N/A (auto-expire) |
| **JIT Access** (High-Risk) | On-demand access to high-risk utilities | Automated (within policy) or Security Manager | Hours | N/A (auto-expire) |
| **JIT Access** (Critical) | On-demand access to critical utilities | Security Manager (manual) | Hours | N/A (auto-expire) |
| **Emergency Access** | Break-glass for critical incidents | CISO or Deputy | 24 hours | N/A (emergency only) |

### 6.2 Create Access Request Form

**Minimum Information Required**:

1. **Requester Information**:
   - Name, employee ID, job role
   - Manager name and email
   - Department

2. **Privileged Utility Details**:
   - Which privileged utility(ies) needed
   - Risk level (from inventory)
   - Platform (Windows, macOS, Linux)

3. **Access Details**:
   - Access type: Standing / Temporary / JIT / Emergency
   - Duration (if temporary/JIT): Specific end date or hours
   - Business justification: Why do you need this privileged utility?
   - Alternative approaches considered: Can task be accomplished without privileged utility?

4. **Manager Approval** (for standing/temporary access):
   - Manager attests that access is required for job role
   - Manager signature/approval

**Form Implementation Options**:

**Option 1: Ticketing System** (ServiceNow, Jira):

1. Create custom ticket type: "Privileged Utility Access Request"
2. Add custom fields (requester info, utility, justification, duration)
3. Configure workflow:
   - Submit → Manager Approval (if standing/temporary)
   - Manager Approves → Security Manager Review
   - Security Manager Approves → IT Operations Implementation
   - Requester Notified

**Option 2: SharePoint + Power Automate**:

1. Create SharePoint list: "Privileged Utility Access Requests"
2. Add columns (requester, utility, risk, justification, access type, duration, manager approval, security approval, status)
3. Create Power Automate flow:
   - On item creation → Email manager for approval
   - Manager approves → Email Security Manager
   - Security Manager approves → Email IT Ops, update status
   - Notify requester

**Option 3: Simple Email Request** (small organizations):

Email template:
```
To: security-manager@organization.ch
CC: [Your Manager]
Subject: Privileged Utility Access Request - [Utility Name]

Requester: [Name, Role, Department]
Utility: [Name, e.g., PsExec]
Risk Level: [Critical/High/Medium/Low - from inventory]
Access Type: [Standing/Temporary/JIT/Emergency]
Duration: [If temporary: 90 days, If JIT: 2 hours]

Business Justification:
[Explain why you need this privileged utility - be specific]

Alternative Approaches Considered:
[Have you tried other methods? Why won't they work?]

Manager Approval:
[Manager name] - Approved / Not Yet Approved

[Requester sends email, manager replies with approval, Security Manager reviews]
```

### 6.3 Approval Decision Process

**Security Manager Reviews Request**:

**Approval Criteria** (Security Manager checklist):
- [ ] Business need is legitimate and clearly documented
- [ ] Privileged utility is necessary (alternatives not viable)
- [ ] Requester's role justifies access
- [ ] Risk level is appropriate for requester's experience/training
- [ ] Duration is reasonable (not excessive)
- [ ] Manager has approved (for standing/temporary access)

**Security Manager Actions**:
- **Approve**: Request meets all criteria
- **Approve with Conditions**: Approve but add restrictions (e.g., "Approve JIT only, not standing access")
- **Request More Information**: Insufficient justification or unclear need
- **Deny**: Business need not justified, excessive risk, alternatives available

**High-Risk and Critical Utilities** (additional step):
- Security Manager review → Escalate to CISO for final approval
- CISO reviews risk, business need, compensating controls
- CISO approves or denies

**Approval Notification**:

```
Subject: Privileged Utility Access Request Approved - [Utility]

Dear [Requester],

Your privileged utility access request has been approved:

Utility: [Name]
Access Type: [Standing/Temporary/JIT]
Duration: [Permanent/90 days/2 hours]
Approved By: [Security Manager name]
Conditions: [Any special conditions, e.g., "JIT access only, MFA required"]

Next Steps:
- IT Operations will implement access within [X] business days
- You will receive notification when access is active
- Review your responsibilities: [Link to privileged access policy]

Important Reminders:
- All privileged utility usage is logged and monitored
- Use separate administrative account (not your regular account)
- MFA is required for privileged access
- Your access will be reviewed [quarterly/annually]

Questions? Contact Information Security Team.
```

### 6.4 Just-in-Time (JIT) Access Implementation

**JIT Access Concept**: Temporary privileged access granted on-demand for specific duration (hours), then automatically revoked.

**Why JIT**:
- Reduces standing privilege (principle of least privilege)
- Limits exposure window (access only when needed)
- Reduces credential theft risk (no permanent credentials)
- Supports audit (clear business justification per access)

**JIT Implementation Options**:

**Option 1: PAM Solution** (CyberArk, BeyondTrust, Azure AD PIM)

**Azure AD Privileged Identity Management (PIM)** (example):

1. **Azure AD → Privileged Identity Management → Azure AD roles → Roles**
2. **Add assignments** → **Eligible assignments**
3. Select role: (e.g., "PrivUtil-ITAdmins-HighRisk")
4. **Select members**: Add users eligible for JIT access
5. **Assignment type**: Eligible (requires activation)
6. **Assignment settings**:
   - **Maximum activation duration**: 8 hours
   - **Require justification on activation**: Yes
   - **Require approval to activate**: Yes (for Critical-risk utilities)
   - **Approvers**: Security Manager

**User JIT Access Request** (Azure AD PIM):
1. User navigates: Azure AD → PIM → My roles
2. Select role: "PrivUtil-ITAdmins-HighRisk"
3. Click: **Activate**
4. Provide justification: "Troubleshooting server issue, ticket #12345"
5. Submit activation request
6. If approval required: Security Manager receives notification, approves/denies
7. Once approved: Role activated for specified duration (e.g., 8 hours)
8. After duration expires: Role automatically deactivated

**Option 2: PowerShell Script-Based JIT** (simple, no PAM solution)

**Concept**: PowerShell script adds user to privileged group, waits specified duration, then removes user.

**Script** (`Grant-JITAccess.ps1`):

```powershell
<#
.SYNOPSIS
Grants JIT access to privileged utility group for specified duration.

.PARAMETER Username
User to grant access (e.g., john.smith-admin)

.PARAMETER GroupName
Privileged group (e.g., PrivUtil-ITAdmins-HighRisk)

.PARAMETER DurationHours
Duration in hours (default: 4)

.PARAMETER Justification
Business justification for access
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$Username,
    
    [Parameter(Mandatory=$true)]
    [string]$GroupName,
    
    [Parameter(Mandatory=$false)]
    [int]$DurationHours = 4,
    
    [Parameter(Mandatory=$true)]
    [string]$Justification
)

# Log access request
$logEntry = @{
    Timestamp = Get-Date
    Username = $Username
    Group = $GroupName
    Duration = $DurationHours
    Justification = $Justification
    Action = "JIT Access Granted"
}
$logEntry | ConvertTo-Json | Out-File -Append -FilePath "C:\Logs\JIT-Access.log"

# Add user to group
Add-ADGroupMember -Identity $GroupName -Members $Username
Write-Host "JIT Access granted: $Username added to $GroupName for $DurationHours hours"

# Wait for duration
Start-Sleep -Seconds ($DurationHours * 3600)

# Remove user from group
Remove-ADGroupMember -Identity $GroupName -Members $Username -Confirm:$false
Write-Host "JIT Access expired: $Username removed from $GroupName"

# Log access expiration
$logEntry.Action = "JIT Access Expired"
$logEntry.Timestamp = Get-Date
$logEntry | ConvertTo-Json | Out-File -Append -FilePath "C:\Logs\JIT-Access.log"
```

**Usage**:
```powershell
.\Grant-JITAccess.ps1 -Username "john.smith-admin" -GroupName "PrivUtil-ITAdmins-HighRisk" -DurationHours 2 -Justification "Incident response ticket #12345"
```

**Automation**: Run script as scheduled task or via self-service portal.

**Limitation**: Script must run continuously for duration (if server reboots, access not revoked). Consider PAM solution for production.

---

## 7. MFA Implementation

### 7.1 MFA for Privileged Access (Windows)

**Requirement** (POL-S4 REQ-A818-008): MFA required for privileged utility usage where technically feasible.

**Windows MFA Options**:

**Option 1: Windows Hello for Business** (Smart Cards or Biometrics)

1. **Group Policy → Computer Configuration → Policies → Windows Settings → Security Settings → Public Key Policies → Certificate Services Client - Auto-Enrollment**
2. **Configuration Model**: Enabled
3. **Deploy smart cards or enable biometric devices** (fingerprint readers, facial recognition)
4. **Require smart card for interactive logon**:
   - **Group Policy → Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → Security Options**
   - **Interactive logon: Require smart card**: Enabled
5. **Scope**: Apply to administrative accounts only (not regular users)

**Option 2: Azure AD MFA** (for Azure AD-joined or hybrid-joined devices)

1. **Azure AD → Security → Conditional Access → New policy**
2. **Name**: Require MFA for Administrative Accounts
3. **Assignments**:
   - **Users and groups**: Include: PrivUtil-ITAdmins, PrivUtil-SecurityAnalysts (privileged groups)
   - **Cloud apps**: All cloud apps (or specific admin portals)
4. **Conditions**:
   - **Device platforms**: Windows
   - **Client apps**: Browser, mobile apps, desktop clients
5. **Access controls → Grant**: Grant access, Require multi-factor authentication
6. **Enable policy**: On

**User Experience**:
- User logs in with admin account → Prompted for MFA (push notification, authenticator app, hardware token)
- After MFA: Session established, privileged utilities accessible

**Option 3: Third-Party MFA** (Duo Security, Okta, etc.)

1. Install Duo Authentication for Windows Logon
2. Configure Duo policy: Require MFA for specific groups (PrivUtil-ITAdmins)
3. Users prompted for Duo push or hardware token at Windows login

**Verification**:
- Log in with administrative account
- Verify MFA prompt appears
- Complete MFA, verify access granted

### 7.2 MFA for Privileged Access (Linux)

**Linux MFA via PAM (Pluggable Authentication Modules)**

**Google Authenticator PAM Module** (TOTP-based MFA):

1. **Install Google Authenticator PAM module**:
   ```bash
   # Ubuntu/Debian
   sudo apt install libpam-google-authenticator
   
   # RHEL/CentOS
   sudo yum install google-authenticator
   ```

2. **Configure PAM** (`/etc/pam.d/sshd` or `/etc/pam.d/sudo`):
   ```bash
   sudo nano /etc/pam.d/sshd
   ```

   **Add line** (at top):
   ```
   auth required pam_google_authenticator.so
   ```

3. **Configure SSH** to use PAM (`/etc/ssh/sshd_config`):
   ```bash
   ChallengeResponseAuthentication yes
   UsePAM yes
   ```

4. **Restart SSH**:
   ```bash
   sudo systemctl restart sshd
   ```

5. **Setup TOTP for each user**:
   ```bash
   google-authenticator
   ```
   - Answer prompts (Y/N for various options)
   - Scan QR code with authenticator app (Google Authenticator, Authy, Microsoft Authenticator)
   - Save emergency codes

**User Experience**:
- User SSH to server: `ssh admin@server`
- Prompted for password: [Enter password]
- Prompted for verification code: [Enter TOTP code from authenticator app]
- Access granted

**Verification**:
- SSH as admin user
- Verify TOTP prompt appears
- Enter code, verify access

### 7.3 MFA for Privileged Access (macOS)

**macOS MFA Options**:

**Option 1: Touch ID / Secure Enclave** (built-in biometric)

1. **System Settings → Touch ID & Password**
2. **Enable Touch ID**: Enrolled fingerprints
3. **Use Touch ID for**: Unlocking Mac, Apple Pay, Password AutoFill, **sudo authentication**

**sudo with Touch ID**:
- Edit `/etc/pam.d/sudo`:
  ```bash
  sudo nano /etc/pam.d/sudo
  ```
- Add at top:
  ```
  auth       sufficient     pam_tid.so
  ```
- Save and exit

**User Experience**:
- User runs privileged command: `sudo systemctl restart service`
- Prompted: Touch ID sensor to authenticate
- After Touch ID verification: Command executes

**Option 2: Jamf Pro with MFA** (enterprise managed Macs)

1. **Jamf Pro → Computer Management → Security → User-Initiated Enrollment**
2. Configure MFA requirement for enrollment
3. **Policies** → Require MFA for privileged operations

**Option 3: Third-Party MFA** (Duo, Okta)

- Similar to Windows, install Duo for macOS
- Configure MFA for privileged actions

---

## 8. Logging Configuration

### 8.1 Windows Privileged Utility Logging

**Enable Comprehensive Logging** (per POL-S4 REQ-A818-010):

**1. Enable Process Creation Logging** (Event ID 4688):

**Group Policy → Computer Configuration → Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → System Audit Policies → Detailed Tracking**
- **Audit Process Creation**: Success

**GPO also configure command line inclusion**:
- **Administrative Templates → System → Audit Process Creation**
- **Include command line in process creation events**: Enabled

**Verification**:
- Run command: `powershell.exe -Command "Get-Process"`
- **Event Viewer → Security** → Event ID 4688
- Verify: Command line visible in event details

**2. Enable PowerShell Logging**:

**A. Script Block Logging** (logs all PowerShell code executed):

**Group Policy → Computer Configuration → Administrative Templates → Windows Components → Windows PowerShell**
- **Turn on PowerShell Script Block Logging**: Enabled
- **Log script block invocation start / stop events**: Enabled (optional, verbose)

**Logs**: Event Viewer → Applications and Services Logs → Microsoft → Windows → PowerShell → Operational → Event ID 4104

**B. Module Logging** (logs PowerShell module usage):

**Windows PowerShell → Turn on Module Logging**: Enabled
- **Module Names**: `*` (all modules)

**Logs**: Event ID 4103

**C. Transcription Logging** (logs all PowerShell input/output):

**Windows PowerShell → Turn on PowerShell Transcription**: Enabled
- **Transcript output directory**: `\\fileserver\logs\powershell-transcripts` (centralized)
- **Include invocation headers**: Enabled

**Logs**: Plaintext transcript files in specified directory

**3. Deploy Sysmon** (Enhanced Logging):

Sysmon provides detailed logging beyond Windows Event Log (process creation, network connections, file creation, registry modifications).

**Download Sysmon**: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

**Install Sysmon with Configuration**:

1. Download Sysmon configuration (e.g., SwiftOnSecurity config): https://github.com/SwiftOnSecurity/sysmon-config

2. Install Sysmon:
   ```cmd
   sysmon64.exe -accepteula -i sysmonconfig-export.xml
   ```

3. Deploy via GPO (Startup Script):
   ```batch
   \\fileserver\sysmon\sysmon64.exe -accepteula -i \\fileserver\sysmon\sysmonconfig-export.xml
   ```

**Sysmon Logs**: Event Viewer → Applications and Services Logs → Microsoft → Windows → Sysmon → Operational

**Key Sysmon Events**:
- **Event ID 1**: Process creation (includes parent process, command line, hash)
- **Event ID 3**: Network connection (destination IP, port)
- **Event ID 7**: Image loaded (DLL loading, detect malicious DLLs)
- **Event ID 11**: File creation (detect file creation by privileged utilities)
- **Event ID 13**: Registry modification (detect registry changes)

**Verification**:
- Run privileged utility (e.g., `powershell.exe`)
- Check Sysmon logs: Event ID 1 (process creation) should appear

### 8.2 Linux Privileged Utility Logging

**Enable auditd** (Linux Audit Daemon):

**1. Install auditd** (if not installed):
```bash
# Ubuntu/Debian
sudo apt install auditd

# RHEL/CentOS
sudo yum install audit
```

**2. Configure Audit Rules** (`/etc/audit/rules.d/audit.rules`):

**Monitor sudo usage**:
```bash
-a always,exit -F arch=b64 -S execve -F auid>=1000 -F auid!=-1 -F key=sudo-commands
```

**Monitor privileged utility execution** (specific utilities):
```bash
# Monitor /usr/bin/sudo
-w /usr/bin/sudo -p x -k sudo-exec

# Monitor /bin/su
-w /bin/su -p x -k su-exec

# Monitor systemctl
-w /usr/bin/systemctl -p x -k systemctl-exec

# Monitor iptables
-w /usr/sbin/iptables -p x -k iptables-exec
```

**Monitor file access by root**:
```bash
-a always,exit -F arch=b64 -S open -S openat -F auid=0 -F key=root-file-access
```

**3. Reload Audit Rules**:
```bash
sudo augenrules --load
sudo systemctl restart auditd
```

**4. View Audit Logs**:
```bash
# View real-time audit events
sudo ausearch -k sudo-commands

# View audit log file
sudo cat /var/log/audit/audit.log | grep sudo-commands
```

**Verification**:
- Execute sudo command: `sudo ls /root`
- Check audit log: `sudo ausearch -k sudo-commands`
- Verify: Event logged with user, command, timestamp

**3. sudo Logging** (built-in):

sudo automatically logs to `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL/CentOS).

**View sudo logs**:
```bash
# Ubuntu/Debian
sudo grep sudo /var/log/auth.log

# RHEL/CentOS
sudo grep sudo /var/log/secure
```

**Example log entry**:
```
Jan 11 10:23:45 server sudo: john.smith : TTY=pts/0 ; PWD=/home/john.smith ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx
```

### 8.3 macOS Privileged Utility Logging

**1. Unified Logging** (macOS built-in):

**View logs**:
```bash
# View sudo usage
log show --predicate 'process == "sudo"' --info --last 1h

# View Terminal usage (root)
log show --predicate 'process == "Terminal" AND eventMessage CONTAINS "root"' --info --last 1h
```

**2. File Monitoring** (OpenBSM Audit - macOS built-in):

**Enable auditing** (`/etc/security/audit_control`):
```bash
sudo nano /etc/security/audit_control
```

**Modify flags**:
```
flags:lo,aa,ad,fd,fm,-all
```
- `lo`: Login/logout
- `aa`: Authentication and authorization
- `ad`: Administrative actions
- `fd`: File deletion
- `fm`: File attribute modification

**Restart auditing**:
```bash
sudo audit -s
```

**View audit logs**:
```bash
sudo praudit /var/audit/* | grep sudo
```

**3. Third-Party Logging** (Jamf Pro, enterprise environments):

Jamf Pro can collect and centralize logs from managed Macs.

---

## 9. SIEM Integration

### 9.1 Log Forwarding to SIEM

**Forward privileged utility logs to SIEM** for centralized monitoring, correlation, and alerting.

**Windows → SIEM** (using NXLog or similar):

**NXLog Configuration** (`C:\Program Files\nxlog\conf\nxlog.conf`):

```xml
<Input eventlog>
    Module im_msvistalog
    <QueryXML>
        <QueryList>
            <Query Id="0">
                <Select Path="Security">*[System[(EventID=4688 or EventID=4673)]]</Select>
                <Select Path="Microsoft-Windows-PowerShell/Operational">*[System[(EventID=4103 or EventID=4104)]]</Select>
                <Select Path="Microsoft-Windows-Sysmon/Operational">*[System[(EventID=1 or EventID=3)]]</Select>
            </Query>
        </QueryList>
    </QueryXML>
</Input>

<Output siem>
    Module om_tcp
    Host siem.organization.ch
    Port 514
    Exec to_syslog_bsd();
</Output>

<Route eventlog_to_siem>
    Path eventlog => siem
</Route>
```

**Deploy NXLog via GPO or SCCM** (install on all endpoints).

**Linux → SIEM** (using rsyslog):

**rsyslog Configuration** (`/etc/rsyslog.d/60-auditd.conf`):

```bash
# Forward auditd logs to SIEM
$ModLoad imfile
$InputFileName /var/log/audit/audit.log
$InputFileTag audit:
$InputFileStateFile stat-audit
$InputFileSeverity info
$InputFileFacility local6
$InputRunFileMonitor

# Forward to SIEM
*.* @@siem.organization.ch:514
```

**Restart rsyslog**:
```bash
sudo systemctl restart rsyslog
```

**macOS → SIEM** (using syslog forwarding):

**Configure syslog forwarding** (`/etc/syslog.conf`):

```bash
# Forward all logs to SIEM
*.* @siem.organization.ch:514
```

**Restart syslog**:
```bash
sudo launchctl unload /System/Library/LaunchDaemons/com.apple.syslogd.plist
sudo launchctl load /System/Library/LaunchDaemons/com.apple.syslogd.plist
```

**Verification**:
- Execute privileged utility
- Check SIEM: Verify log appears in SIEM within 5 minutes

### 9.2 SIEM Correlation Rules

**Create SIEM correlation rules** to detect anomalous privileged utility usage.

**Rule 1: Unauthorized Privileged Utility Usage**

**Trigger**: Privileged utility executed by unauthorized user (user not in authorized groups).

**SIEM Logic** (example - adapt to your SIEM):
```
IF EventID == 4688 (Process Creation)
AND ProcessName IN (privileged_utility_list)
AND User NOT IN (authorized_users_list)
THEN ALERT "Unauthorized Privileged Utility Usage" (Severity: HIGH)
```

**Rule 2: High-Risk Privileged Utility Usage Outside Business Hours**

**Trigger**: Critical or high-risk privileged utility executed outside 8 AM - 6 PM Mon-Fri.

**SIEM Logic**:
```
IF EventID == 4688
AND ProcessName IN (high_risk_utilities)
AND (Time < 08:00 OR Time > 18:00 OR DayOfWeek IN (Saturday, Sunday))
THEN ALERT "High-Risk Privileged Utility - Outside Business Hours" (Severity: MEDIUM)
```

**Rule 3: Multiple Privileged Utilities in Sequence** (Possible Attack)

**Trigger**: Multiple high-risk utilities executed by same user within 10 minutes.

**SIEM Logic**:
```
IF COUNT(EventID == 4688 AND ProcessName IN (high_risk_utilities) AND User == X) >= 3
WITHIN 10 minutes
THEN ALERT "Multiple Privileged Utilities - Possible Attack" (Severity: CRITICAL)
```

**Rule 4: PsExec Lateral Movement Detection**

**Trigger**: PsExec executed to connect to multiple endpoints.

**SIEM Logic**:
```
IF ProcessName == "psexec.exe"
AND COUNT(DISTINCT DestinationIP) >= 5
WITHIN 30 minutes
THEN ALERT "PsExec Lateral Movement Detected" (Severity: CRITICAL)
```

**Rule 5: Security Bypass Tool Execution**

**Trigger**: Known security bypass tool executed (any user, any time).

**SIEM Logic**:
```
IF ProcessName IN (security_bypass_tools)
THEN ALERT "Security Bypass Tool Executed" (Severity: CRITICAL)
```

**Tune Alerts**:
- Monitor false positive rate
- Adjust thresholds and conditions
- Whitelist legitimate usage (e.g., scheduled maintenance during off-hours)

---

## 10. Quarterly Access Review

### 10.1 Access Review Process

**Requirement** (POL-S4 REQ-A818-016): Quarterly review of privileged utility access.

**Step 1: Generate Access Inventory Report**

**PowerShell Script** (generate report):

```powershell
# Generate Privileged Utility Access Report
$privilegedGroups = @("PrivUtil-ITAdmins", "PrivUtil-SecurityAnalysts", "PrivUtil-DevOps")

$report = @()

foreach ($group in $privilegedGroups) {
    $members = Get-ADGroupMember -Identity $group
    
    foreach ($member in $members) {
        $user = Get-ADUser -Identity $member.SamAccountName -Properties Department, Manager, LastLogonDate
        
        $report += [PSCustomObject]@{
            Username = $user.SamAccountName
            DisplayName = $user.Name
            Department = $user.Department
            Manager = (Get-ADUser -Identity $user.Manager).Name
            PrivilegedGroup = $group
            LastLogon = $user.LastLogonDate
            AccountEnabled = $user.Enabled
        }
    }
}

$report | Export-Csv -Path "C:\Reports\PrivilegedAccessReview-$(Get-Date -Format 'yyyy-MM-dd').csv" -NoTypeInformation
Write-Host "Access review report generated: C:\Reports\PrivilegedAccessReview-$(Get-Date -Format 'yyyy-MM-dd').csv"
```

**Step 2: Distribute Report to Managers**

**Email Template**:

```
Subject: Quarterly Privileged Utility Access Review - Action Required

Dear Manager,

Attached is the quarterly privileged utility access review report for your team members.

Please review and attest to the following for each team member with privileged access:

1. Is this access still required for their current job role?
2. Has the utility been used appropriately (no security violations)?
3. Should access be continued, modified, or revoked?

Please respond by [Date + 14 days] with:
- Continue Access: [List usernames]
- Revoke Access: [List usernames with reason]
- Modify Access: [List usernames with requested changes]

If we do not hear from you by [Date + 30 days], access will be automatically suspended pending your review.

Attachment: PrivilegedAccessReview-2026-01-11.csv

Questions? Contact Information Security Team.
```

**Step 3: Manager Review**

Manager reviews report and responds:
- **Continue Access**: User still needs privileged utility, access appropriate
- **Revoke Access**: User no longer needs access (role changed, no longer used)
- **Modify Access**: Downgrade access (e.g., High-Risk → Medium-Risk utilities only)

**Step 4: Security Manager Review**

Security Manager reviews manager attestations + usage logs:
- Cross-reference manager responses with actual usage logs (was utility actually used?)
- Identify unused access (access granted but not used in last 90 days)
- Review high-risk access (extra scrutiny for critical utilities)

**Step 5: Implement Access Changes**

IT Operations implements access changes within 7 days:
- Revoke access: Remove user from privileged group
- Modify access: Move user to different group (lower privilege)
- Continue access: No change (document recertification)

**Step 6: Document Review Results**

Create **Quarterly Access Review Report**:

| Review Date | Total Privileged Access | Reviewed | Continued | Revoked | Modified | Manager Response Rate |
|-------------|-------------------------|----------|-----------|---------|----------|-----------------------|
| [Date] | 45 | 45 (100%) | 40 | 3 | 2 | 100% |

**Store documentation** for audit purposes.

### 10.2 Automate Access Review (Optional)

**Using Azure AD Access Reviews** (for cloud environments):

1. **Azure AD → Identity Governance → Access reviews → New access review**
2. **Review name**: Quarterly Privileged Utility Access Review
3. **Scope**: Members of group → Select: PrivUtil-ITAdmins
4. **Reviewers**: Group owner(s) (managers)
5. **Recurrence**: Quarterly
6. **Duration**: 14 days
7. **Upon completion settings**:
   - Auto apply results to resource: Yes
   - If reviewers don't respond: Remove access
8. **Create**

**Automated process**:
- Quarterly: Access review starts automatically
- Managers receive email notification to review access
- Managers attest via Azure portal (Approve/Deny per user)
- After 14 days: Access automatically revoked for non-approved users

---

## 11. Security Bypass Tool Management

### 11.1 Identify Security Bypass Tools

**Security Bypass Tool Examples** (per POL-S4 Section 7):

| Category | Tool Examples | Risk |
|----------|---------------|------|
| **Password Recovery** | Ophcrack, John the Ripper, hashcat, Mimikatz | Critical |
| **Encryption Bypass** | Elcomsoft tools, BitLocker recovery tools | Critical |
| **Evidence Destruction** | SDelete, shred, BleachBit, CCleaner (secure wipe) | Critical |
| **Rootkit/Stealth Tools** | Rootkit detectors (can also be rootkits) | Critical |
| **Anti-Forensics** | Timestomp, log wipers | Critical |

**Detection Methods**:

1. **Software Inventory Scan**:
   - Cross-reference software inventory with known bypass tool list
   - Example: Search inventory for "Mimikatz", "Ophcrack", "SDelete"

2. **File Hash Database**:
   - Maintain database of known bypass tool hashes (SHA-256)
   - Scan endpoints for matching hashes
   - Example: Hash of `mimikatz.exe` = `<hash>` → Flag if found

3. **EDR Behavioral Detection**:
   - EDR detects tools attempting to disable security controls
   - Example: Tool attempting to disable Windows Defender → Alert

### 11.2 Remove from Non-Administrative Endpoints

**Automated Removal via SCCM/Intune**:

**PowerShell Script** (`Remove-BypassTools.ps1`):

```powershell
# Remove security bypass tools from endpoint
$bypassTools = @(
    "C:\Tools\Mimikatz\mimikatz.exe",
    "C:\Tools\Ophcrack\*",
    "C:\Program Files\SDelete\*"
)

foreach ($tool in $bypassTools) {
    if (Test-Path $tool) {
        Remove-Item -Path $tool -Recurse -Force
        Write-Host "Removed: $tool"
        
        # Log removal
        $logEntry = "$(Get-Date): Removed bypass tool: $tool"
        $logEntry | Out-File -Append -FilePath "C:\Logs\BypassToolRemoval.log"
    }
}
```

**Deploy via GPO** (Startup Script) or **SCCM** (deploy to all non-administrative endpoints).

**Verification**:
- After deployment, spot-check sample endpoints
- Verify bypass tools removed

### 11.3 Restrict on Administrative Endpoints

**If legitimate use case** (security testing, incident response):

1. **CISO Approval Required**:
   - Security team submits request
   - CISO reviews business justification
   - CISO approves or denies

2. **JIT Access Only**:
   - Tools deployed temporarily (for specific project)
   - Automatic removal after 30 days (max)

3. **Enhanced Monitoring**:
   - All usage logged and alerted
   - Real-time alerts to Security Manager
   - Session recording (PAM solution)

4. **Environment Isolation**:
   - Tools used in isolated environment (separate VLAN, no production access)
   - No access to production data/systems

**Example Approval Record**:

```
Security Bypass Tool Approval

Tool: Mimikatz
Requested by: Security Analyst (Bob Jones)
Business Justification: Incident response investigation (suspected credential theft, ticket #12345)
Duration: 7 days (until 2026-01-18)
Environment: Isolated forensics workstation (no production network access)
Monitoring: Session recorded, real-time alerts enabled
Approved by: CISO (Jane Smith)
Approval Date: 2026-01-11
```

---

## 12. Verification Procedures

### 12.1 Access Control Verification

**Test 1: Unauthorized User Blocked**

1. Log in as standard user (non-admin, not in privileged groups)
2. Attempt to execute privileged utility:
   - Windows: `powershell.exe`
   - Linux: `sudo ls /root`
   - macOS: `sudo diskutil list`
3. **Expected Result**: Access denied (file permission denied, AppLocker blocked, sudo not in sudoers file)
4. **If not blocked**: Access control misconfigured, review configuration

**Test 2: Authorized User Allowed**

1. Log in as authorized user (member of PrivUtil-ITAdmins)
2. Attempt to execute privileged utility
3. **Expected Result**: Access granted, utility executes successfully
4. **If blocked**: Access control misconfigured, verify group membership

**Sample Size**: Test on 5-10 endpoints (different OS types).

### 12.2 Logging Verification

**Test 1: Privileged Utility Execution Logged**

1. Execute privileged utility (e.g., PowerShell: `Get-Process`)
2. Check local logs:
   - Windows: Event Viewer → Security → Event ID 4688 (Process Creation)
   - Windows: PowerShell Operational → Event ID 4104 (Script Block Logging)
   - Linux: `/var/log/audit/audit.log` or `ausearch -k sudo-commands`
3. **Expected Result**: Event logged with user, command, timestamp
4. **If not logged**: Logging misconfigured, review configuration

**Test 2: Log Forwarded to SIEM**

1. Execute privileged utility
2. Wait 5-10 minutes (log forwarding delay)
3. Query SIEM for event (search by username, process name, EventID)
4. **Expected Result**: Event appears in SIEM
5. **If not in SIEM**: Log forwarding misconfigured, check NXLog/rsyslog configuration

**Sample Size**: Test on 5-10 endpoints.

### 12.3 SIEM Alert Verification

**Test: High-Risk Utility Usage Alert**

1. Execute high-risk privileged utility (e.g., PsExec, Wireshark)
2. Wait 5-10 minutes
3. Check SIEM alerts
4. **Expected Result**: SIEM alert generated ("High-Risk Privileged Utility Usage")
5. **If no alert**: SIEM correlation rule misconfigured, review rule logic

---

## 13. Common Pitfalls and Troubleshooting

### 13.1 Pitfall: Privileged Utilities Blocked for Legitimate Administrators

**Symptom**: IT administrators cannot execute privileged utilities needed for their job.

**Causes**:
1. Access control too restrictive (admin not in authorized group)
2. File permissions misconfigured (admin group not granted execute permission)
3. AppLocker rule blocking utility (no allow rule for admin group)

**Solution**:
1. **Verify Group Membership**: Check if admin is member of authorized group (e.g., PrivUtil-ITAdmins)
   ```powershell
   Get-ADGroupMember -Identity "PrivUtil-ITAdmins"
   ```
   - If admin not member: Add to group
2. **Verify File Permissions**: Check file permissions on privileged utility
   - Ensure admin group has Read & Execute permissions
3. **Review AppLocker Rules**: Check AppLocker logs for blocks
   - Event Viewer → AppLocker → EXE and DLL → Event ID 8004 (Blocked)
   - If admin legitimately blocked: Add allow rule for admin group
4. **Test Access**: After remediation, test admin can execute utility

### 13.2 Pitfall: Excessive SIEM Alerts (Alert Fatigue)

**Symptom**: SIEM generates too many privileged utility alerts, security team overwhelmed.

**Causes**:
1. Correlation rules too sensitive (alerting on all privileged utility usage)
2. Legitimate administrative activity triggering alerts
3. Baselines not established (normal usage patterns not defined)

**Solution**:
1. **Tune Correlation Rules**:
   - Reduce sensitivity (e.g., alert only on critical-risk utilities, not all)
   - Adjust thresholds (e.g., multiple utilities within 10 minutes, not 1 hour)
2. **Whitelist Legitimate Activity**:
   - Scheduled maintenance windows (disable alerts during maintenance)
   - Known administrative tasks (add exceptions to correlation rules)
3. **Establish Baselines**:
   - Analyze privileged utility usage over 30 days
   - Define "normal" usage patterns (who, when, which utilities)
   - Alert only on deviations from baseline
4. **Prioritize Alerts**:
   - Critical alerts: Security bypass tools, unauthorized users
   - Medium alerts: High-risk utilities outside business hours
   - Low alerts: Routine privileged utility usage (logged but not alerted)

### 13.3 Pitfall: JIT Access Expires During Active Work

**Symptom**: User's JIT access expires while actively using privileged utility, disrupting work.

**Causes**:
1. JIT access duration too short (e.g., 1 hour for task requiring 3 hours)
2. User did not plan access duration appropriately

**Solution**:
1. **Extend JIT Access Duration**:
   - Default: 4 hours (sufficient for most administrative tasks)
   - Allow users to request specific duration (up to 8 hours)
2. **Access Extension Capability**:
   - User can request extension if task takes longer than expected
   - Automated approval (if within policy) or manual approval (Security Manager)
3. **User Education**:
   - Train users to estimate task duration accurately
   - Request sufficient JIT access time upfront
4. **Fallback to Standing Access**:
   - For users requiring daily privileged utility usage (e.g., IT Ops): Grant standing access (not JIT)
   - JIT reserved for infrequent use cases

---

## 14. Integration with Other Controls

### 14.1 Integration with A.8.19 (Installation of Software)

**Connection**: Privileged utilities are software (subject to software control).

**Integration Points**:
- **Privileged Utilities in Approved Software List**: All authorized privileged utilities must be on approved software list (A.8.19)
- **Application Control for Privileged Utilities**: AppLocker/WDAC rules (A.8.19) restrict privileged utility execution (A.8.18)
- **Unauthorized Privileged Utilities**: Detected via software inventory (A.8.19), removed as unauthorized software

**Example**:
- PsExec: On approved software list (role-based: IT Admins only)
- AppLocker: Blocks PsExec for non-IT Admins (software control + privileged utility control)
- Unauthorized privileged utility (e.g., Mimikatz): Detected in software inventory → Removed

### 14.2 Integration with A.8.7 (Protection Against Malware)

**Connection**: Malware may use privileged utilities maliciously.

**Integration Points**:
- **Malware Detection**: Anti-malware detects malicious use of privileged utilities (e.g., malware using PowerShell for C2)
- **Behavioral Analysis**: EDR correlates privileged utility usage with malware indicators
- **Logging Integration**: Privileged utility logs + malware detection logs → SIEM correlation

**Example**:
- Malware executes: `powershell.exe -encodedcommand [base64]`
- Anti-malware: Detects PowerShell behavioral indicators (suspicious command)
- Privileged utility logging: Logs PowerShell execution
- SIEM: Correlates malware detection + PowerShell usage → Alert

### 14.3 Integration with A.8.2 (Privileged Access Rights)

**Connection**: A.8.2 governs privileged access broadly, A.8.18 focuses on privileged utilities specifically.

**Integration Points**:
- **Privileged Access Policy**: A.8.2 defines overall privileged access principles (least privilege, separation of duties)
- **Privileged Utility Access**: A.8.18 implements those principles for privileged utilities
- **Access Reviews**: Privileged utility access reviews (A.8.18) part of broader privileged access reviews (A.8.2)

---

## 15. Continuous Improvement

### 15.1 Metrics to Track

**Privileged Utility Metrics**:
- **Inventory Accuracy**: % of privileged utilities correctly inventoried (target: ≥90%)
- **Access Control Coverage**: % of utilities with access controls configured (target: 100%)
- **Approval Compliance**: % of access grants with documented approval (target: 100%)
- **MFA Coverage**: % of privileged access requiring MFA (target: ≥90%)
- **Logging Coverage**: % of endpoints with privileged utility logging enabled (target: ≥95%)
- **SIEM Integration**: % of endpoints forwarding logs to SIEM (target: ≥95%)
- **Access Review Completion**: % of privileged access reviewed quarterly (target: 100%)
- **Unauthorized Tool Detection**: # of security bypass tools detected and removed (target: 0 on non-admin endpoints)

### 15.2 Quarterly Review Process

1. **Collect Metrics** (automated, monthly)
2. **Analyze Trends** (quarterly):
   - Inventory accuracy improving or degrading?
   - Access control coverage improving?
   - SIEM alerts increasing (more threats) or decreasing (better controls)?
3. **Identify Improvement Opportunities**:
   - Inventory accuracy low → Improve discovery procedures
   - MFA coverage low → Deploy MFA to more endpoints
   - Access reviews incomplete → Automate review process
4. **Implement Improvements**: Action plan with owners and deadlines
5. **Measure Effectiveness**: Track metrics post-implementation

---

## 16. Documentation Requirements

**Mandatory Documentation**:
- [ ] **Privileged Utility Inventory**: Complete inventory with risk classifications
- [ ] **Access Control Configuration**: AppLocker policies, file permissions, RBAC groups
- [ ] **Approval Records**: All access approvals (standing, temporary, JIT, emergency)
- [ ] **MFA Configuration**: MFA implementation details and exceptions
- [ ] **Logging Configuration**: Windows Event Log, PowerShell logging, auditd, Sysmon
- [ ] **SIEM Integration**: Log forwarding configuration, correlation rules, alert definitions
- [ ] **Quarterly Access Reviews**: Review reports, manager attestations, access changes

---

## 17. Appendix

### 17.1 Glossary

**Privileged Utility**: Program that can bypass or override security controls (system admin tools, debuggers, security bypass tools).

**JIT Access**: Just-in-Time access - temporary privileged access granted on-demand for specific duration.

**PAM**: Privileged Access Management - solution for managing, monitoring, and controlling privileged access.

**Security Bypass Tool**: Tool that can disable security controls, destroy evidence, or bypass access controls.

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Team | Initial privileged utility management implementation guidance (A.8.18) |

---

**END OF DOCUMENT**