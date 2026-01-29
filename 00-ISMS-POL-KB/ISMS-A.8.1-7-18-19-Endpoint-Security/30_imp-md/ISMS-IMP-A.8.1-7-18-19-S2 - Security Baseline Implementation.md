# ISMS-IMP-A.8.1-7-18-19-S2 - Security Baseline Implementation
## Practical Implementation Guidance for Endpoint Security Baselines
### ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19: Endpoint Security Framework

---

## Document Control

| Attribute | Details |
|-----------|---------|
| Document ID | ISMS-IMP-A.8.1-7-18-19-S2 |
| Document Title | Security Baseline Implementation |
| Version | 1.0 |
| Date | [Date] |
| Classification | Internal |
| Document Owner | [Organization] Endpoint Security Team |
| Status | Active |
| Review Cycle | Annual |
| Parent Document | ISMS-POL-A.8.1-7-18-19-S2 (Endpoint Devices Requirements - A.8.1) |
| Related Documents | ISMS-POL-A.8.1-7-18-19 (Master Framework)<br>ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process)<br>ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment) |

---

## 1. Purpose and Scope

### 1.1 Purpose
This document provides practical, step-by-step guidance for developing, deploying, and enforcing security baselines across all endpoint types in [Organization]'s environment. Security baselines are the foundation of endpoint security, ensuring consistent minimum security configurations that protect information stored on, processed by, or accessible via user endpoint devices (ISO 27001:2022 Control A.8.1).

**Critical Principle**: *Configuration is security. An unmanaged endpoint is an unprotected endpoint. Baselines must be enforced automatically, not manually.*

### 1.2 Scope
This guidance covers:
- **Baseline Development**: Creating risk-appropriate security baselines per OS and device type
- **Baseline Deployment**: Technical implementation using GPO, MDM, configuration management
- **Operating Systems**: Windows (10/11), macOS, Linux (RHEL/Ubuntu), iOS, Android, ChromeOS
- **Management Platforms**: Intune, Jamf Pro, SCCM, Google Workspace, Ansible, Puppet, Chef
- **Encryption Implementation**: BitLocker, FileVault, LUKS, mobile device encryption
- **Compliance Monitoring**: Automated compliance assessment and drift detection
- **Exception Handling**: Risk-based exceptions to baseline requirements

### 1.3 Target Audience
- Endpoint security architects and engineers
- MDM/UEM platform administrators
- Group Policy administrators (Windows)
- Configuration management engineers (Linux)
- ISMS implementation teams conducting A.8.1 compliance

### 1.4 Prerequisites
- **Access Requirements**:
  - Administrator access to Group Policy Management Console (GPO)
  - Administrator access to MDM/UEM platforms (Intune, Jamf, SCCM)
  - Root/sudo access to configuration management systems (Ansible, Puppet)
  - Access to CIS Benchmarks (free download from cisecurity.org)
- **Knowledge Requirements**:
  - Understanding of endpoint operating systems
  - Familiarity with Group Policy Objects (Windows)
  - Understanding of MDM concepts (configuration profiles, compliance policies)
  - Basic scripting (PowerShell, Bash, Python)
- **Completed Prerequisites**:
  - Endpoint inventory complete (IMP-S1)
  - Endpoint classification complete (device type, ownership, criticality)
  - Stakeholder alignment (IT ops, security, user representatives)

---

## 2. Overview and Prerequisites

### 2.1 Process Overview
Security baseline implementation follows a **six-phase approach**:

```
Phase 1: Baseline Development
   ↓ (Map CIS Benchmarks → [Organization] requirements)
Phase 2: Stakeholder Review & Approval
   ↓ (IT ops + Security + User reps)
Phase 3: Pilot Deployment
   ↓ (Test group: 50-100 devices)
Phase 4: Validation & Tuning
   ↓ (Address issues, adjust settings)
Phase 5: Production Rollout
   ↓ (Phased deployment to all devices)
Phase 6: Continuous Compliance Monitoring
   ↓ (Ongoing drift detection & remediation)
```

**Timeline Estimate**:
- Phase 1-2 (Development & Review): 2-3 weeks
- Phase 3-4 (Pilot & Tuning): 2-4 weeks
- Phase 5 (Production Rollout): 4-8 weeks (phased)
- Phase 6 (Monitoring): Ongoing

### 2.2 Baseline Development Approach

**CIS Benchmark Foundation**:
- Start with CIS (Center for Internet Security) Benchmarks as baseline template
- CIS Benchmarks = industry consensus baseline (free download)
- Customize based on [Organization] risk tolerance and operational requirements
- Document deviations from CIS recommendations with justification

**Risk-Based Customization**:

| Endpoint Criticality | Baseline Strictness | Example Adjustments |
|---------------------|---------------------|---------------------|
| **High (Executive, Critical Systems)** | Strictest | Screen lock timeout: 5 minutes<br>Require TPM + PIN for BitLocker<br>Block USB storage<br>MFA required for all access |
| **Medium (Standard Users)** | Balanced | Screen lock timeout: 15 minutes<br>BitLocker without PIN<br>USB storage allowed (scanned)<br>MFA for sensitive apps |
| **Low (Guest, Kiosks)** | Minimal | Network isolation<br>No local data storage<br>Session timeout: 30 minutes |
| **BYOD** | Privacy-Aware Minimum | Containerized data only<br>PIN/password required<br>Remote wipe capability<br>No device-level inspection |

### 2.3 Key Principles
- **Defense in Depth**: Multiple layers of security controls
- **Least Privilege**: Users run with minimal necessary permissions
- **Fail Secure**: If configuration fails to apply, device should not connect to network
- **Automated Enforcement**: Manual configuration checks don't scale - automate via GPO/MDM
- **User Experience Balance**: Security should not make devices unusable
- **Technology-Agnostic**: Principles apply regardless of tools used (GPO, Intune, Jamf, etc.)

### 2.4 CIS Benchmark Resources

**Download CIS Benchmarks** (Free):
- URL: https://www.cisecurity.org/cis-benchmarks/
- Required Benchmarks:
  - CIS Microsoft Windows 10 Enterprise Benchmark
  - CIS Microsoft Windows 11 Enterprise Benchmark
  - CIS Apple macOS Benchmark
  - CIS Red Hat Enterprise Linux Benchmark
  - CIS Ubuntu Linux Benchmark
  - CIS Google Chrome Benchmark (if using Chrome)

**CIS-CAT Lite** (Free Compliance Scanner):
- Download: https://www.cisecurity.org/cybersecurity-tools/cis-cat-lite/
- Use: Scan sample devices to verify baseline compliance

---

## 3. Baseline Development Process

### 3.1 Phase 1: CIS Benchmark Mapping

**Objective**: Map CIS Benchmark recommendations to [Organization] requirements

**Procedure**:

1. **Download Relevant CIS Benchmark** (e.g., Windows 11 Enterprise)

2. **Review Benchmark Sections**:
   - CIS Benchmarks organized by security area:
     - Account Policies (passwords, lockout)
     - Security Options (audit, user rights)
     - Windows Firewall
     - Windows Defender
     - AppLocker
     - User Account Control (UAC)
     - BitLocker

3. **Create Baseline Mapping Spreadsheet**:

   | CIS ID | CIS Setting | CIS Recommendation | [Org] Decision | Rationale | Implementation Method |
   |--------|-------------|-------------------|----------------|-----------|----------------------|
   | 1.1.1 | Enforce password history | 24 passwords | Accept | Standard | GPO |
   | 1.1.2 | Maximum password age | 60 days | Modify: 90 days | User feedback - 60 too frequent | GPO |
   | 2.3.1.1 | Administrator account status | Disabled | Accept | Security best practice | GPO |
   | 18.9.30.2 | BitLocker: Require TPM | Enabled | Modify: Optional | Older devices lack TPM | GPO + Intune |

4. **Categorize Decisions**:
   - **Accept**: Implement CIS recommendation as-is
   - **Modify**: Implement but with adjustments (document why)
   - **Reject**: Do not implement (document risk acceptance)
   - **N/A**: Not applicable to [Organization] environment

5. **Document Deviations**:
   - For each "Modify" or "Reject": Document business justification
   - Example: "CIS recommends disabling Windows Remote Assistance. We modify to 'Allow solicited remote assistance only' because IT support requires this for remote troubleshooting."

**Output**: `Baseline_Mapping_Windows11.xlsx` (or similar for each OS)

### 3.2 Phase 2: Baseline Document Creation

**Objective**: Formalize baseline into implementable configuration document

**Baseline Document Structure**:

```markdown
# [Organization] Windows 11 Security Baseline v1.0

## 1. Account Policies
### 1.1 Password Policy
- Enforce password history: 24 passwords
- Maximum password age: 90 days
- Minimum password age: 1 day
- Minimum password length: 14 characters
- Password must meet complexity requirements: Enabled
- Store passwords using reversible encryption: Disabled

### 1.2 Account Lockout Policy
- Account lockout threshold: 5 invalid attempts
- Account lockout duration: 15 minutes
- Reset account lockout counter after: 15 minutes

## 2. Local Policies
### 2.1 Audit Policy
- Audit logon events: Success, Failure
- Audit account logon events: Success, Failure
- Audit privilege use: Failure
[... etc ...]

## 10. BitLocker Encryption
### 10.1 Fixed Data Drives
- Require BitLocker: Yes
- Encryption method: XTS-AES 256-bit
- Require TPM: Preferred (not mandatory for devices without TPM)
- Allow password: Yes (for non-TPM devices)
- Save recovery key to: Azure AD / Active Directory
```

**Create Baseline Documents For**:
- Windows 10 Enterprise
- Windows 11 Enterprise
- macOS Sonoma / Ventura
- RHEL 8 / 9
- Ubuntu 22.04 / 24.04
- iOS 17
- Android 13 / 14 (Enterprise)
- BYOD Minimum Requirements (cross-platform)

### 3.3 Phase 3: Stakeholder Review

**Review Participants**:
- **Security Team**: Ensure baseline meets security requirements
- **IT Operations**: Ensure baseline is operationally viable (not breaking critical workflows)
- **Helpdesk**: Ensure baseline won't generate excessive support tickets
- **User Representatives**: Ensure baseline doesn't severely impact productivity
- **Compliance/Legal**: Ensure baseline meets regulatory requirements (if applicable)

**Review Process**:

1. **Distribute Baseline Documents** (2-week review period)
2. **Collect Feedback**:
   - Security concerns (settings too weak?)
   - Operational concerns (settings break required workflows?)
   - User experience concerns (settings too restrictive?)
3. **Review Meeting**: Discuss feedback, make adjustments
4. **Approval Sign-Off**:
   - IT Operations Manager
   - CISO
   - (If significant user impact) Business unit managers

**Common Feedback Themes**:
- **"Screen lock timeout too short"**: Users complain 5 minutes too frequent → Adjust to 15 minutes for medium criticality
- **"BitLocker PIN annoying"**: Users frustrated by TPM+PIN requirement → Make PIN optional (TPM-only acceptable)
- **"USB storage blocked"**: Developers need USB drives → Create exception for developer group
- **"Can't install software"**: AppLocker too restrictive → Create allow rules for approved software paths

### 3.4 Phase 4: Baseline Finalization

**Output**: Approved baseline configuration documents + implementation plans

**Baseline Versioning**:
- Version 1.0: Initial baseline
- Future updates: v1.1, v1.2 (minor changes), v2.0 (major revision)
- Track changes in version history table
- Annual re-approval required

---

## 4. Windows Baseline Implementation

### 4.1 Group Policy Implementation (On-Premises AD)

**Use Case**: Windows devices joined to on-premises Active Directory domain

#### 4.1.1 Create Baseline GPOs

**GPO Structure** (Recommended):
```
OU Structure:
- [Organization]
  └─ Computers
     ├─ Workstations
     │  ├─ High-Criticality
     │  ├─ Standard
     │  └─ Kiosks
     ├─ Laptops
     │  ├─ Executive
     │  └─ Standard
     └─ Servers (separate baseline - not covered here)

GPO Structure:
- [Org]-Security-Baseline-Windows11-Standard (linked to Standard Workstations/Laptops)
- [Org]-Security-Baseline-Windows11-High (linked to High-Criticality/Executive)
- [Org]-BitLocker-Enforcement (linked to all computer OUs)
- [Org]-AppLocker-Standard (linked to Standard OUs)
```

**Step-by-Step GPO Creation**:

1. **Open Group Policy Management Console (GPMC)**:
   - Run `gpmc.msc` on domain controller or management workstation
   - Connect to domain

2. **Create New GPO**:
   - Right-click on domain → Create a GPO in this domain, and link it here
   - Name: `[Org]-Security-Baseline-Windows11-Standard`
   - Description: "Security baseline for Windows 11 standard devices per [Org] policy v1.0"

3. **Configure Account Policies** (Computer Configuration → Policies → Windows Settings → Security Settings → Account Policies):
   
   **Password Policy**:
   ```
   Enforce password history: 24 passwords
   Maximum password age: 90 days
   Minimum password age: 1 day
   Minimum password length: 14 characters
   Password must meet complexity requirements: Enabled
   Store passwords using reversible encryption: Disabled
   ```

   **Account Lockout Policy**:
   ```
   Account lockout threshold: 5 invalid logon attempts
   Account lockout duration: 15 minutes
   Reset account lockout counter after: 15 minutes
   ```

4. **Configure Audit Policies** (Computer Configuration → Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration):
   
   **Logon/Logoff**:
   ```
   Audit Logon: Success and Failure
   Audit Logoff: Success
   Audit Account Lockout: Failure
   ```

   **Account Management**:
   ```
   Audit User Account Management: Success and Failure
   Audit Security Group Management: Success and Failure
   ```

   **Policy Change**:
   ```
   Audit Audit Policy Change: Success and Failure
   ```

5. **Configure User Rights Assignment** (Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → User Rights Assignment):
   
   **Critical Settings**:
   ```
   Access this computer from the network: Administrators, Authenticated Users
   Allow log on locally: Administrators, Users
   Allow log on through Remote Desktop Services: Administrators, Remote Desktop Users
   Back up files and directories: Administrators, Backup Operators
   Restore files and directories: Administrators, Backup Operators
   Shut down the system: Administrators, Users
   
   DENY settings:
   Deny access to this computer from the network: Guests
   Deny log on as a batch job: Guests
   Deny log on as a service: Guests
   Deny log on locally: Guests
   ```

6. **Configure Security Options** (Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → Security Options):
   
   **User Account Control (UAC)**:
   ```
   User Account Control: Admin Approval Mode for the Built-in Administrator account: Enabled
   User Account Control: Behavior of the elevation prompt for administrators: Prompt for credentials
   User Account Control: Behavior of the elevation prompt for standard users: Prompt for credentials
   User Account Control: Detect application installations and prompt for elevation: Enabled
   User Account Control: Run all administrators in Admin Approval Mode: Enabled
   ```

   **Network Security**:
   ```
   Network security: Do not store LAN Manager hash value on next password change: Enabled
   Network security: LAN Manager authentication level: Send NTLMv2 response only. Refuse LM & NTLM
   Network security: Minimum session security for NTLM SSP based clients: Require NTLMv2 session security, Require 128-bit encryption
   ```

7. **Configure Windows Firewall** (Computer Configuration → Policies → Windows Settings → Security Settings → Windows Defender Firewall with Advanced Security):
   
   **Domain Profile**:
   ```
   Firewall state: On
   Inbound connections: Block (default)
   Outbound connections: Allow (default)
   Protected network connections: All network connections
   ```

   **Private Profile**: Same as Domain

   **Public Profile**:
   ```
   Firewall state: On
   Inbound connections: Block all connections
   Outbound connections: Allow (default)
   ```

8. **Configure Windows Defender Antivirus** (Computer Configuration → Policies → Administrative Templates → Windows Components → Microsoft Defender Antivirus):
   
   ```
   Turn off Microsoft Defender Antivirus: Disabled (i.e., Defender is ON)
   
   Real-time Protection:
   - Turn on behavior monitoring: Enabled
   - Scan all downloaded files and attachments: Enabled
   - Monitor file and program activity on your computer: Enabled
   - Turn on process scanning whenever real-time protection is enabled: Enabled
   
   Signature Updates:
   - Allow real-time security intelligence updates: Enabled
   - Check for the latest virus and spyware security intelligence on startup: Enabled
   ```

9. **Configure Screen Saver / Lock Settings** (Computer Configuration → Policies → Administrative Templates → Control Panel → Personalization):
   
   ```
   Enable screen saver: Enabled
   Screen saver timeout: Enabled → 900 seconds (15 minutes for Standard, 300 for High)
   Password protect the screen saver: Enabled
   ```

10. **Configure PowerShell Logging** (Computer Configuration → Policies → Administrative Templates → Windows Components → Windows PowerShell):
    
    ```
    Turn on Module Logging: Enabled (log all modules: *)
    Turn on PowerShell Script Block Logging: Enabled
    Turn on PowerShell Transcription: Enabled
    ```

11. **Link GPO to Appropriate OUs**:
    - Right-click on OU (e.g., "Standard Workstations") → Link an Existing GPO
    - Select `[Org]-Security-Baseline-Windows11-Standard`
    - Verify GPO precedence (higher precedence GPOs override lower)

12. **Test GPO Application**:
    - Place test computer in target OU
    - Force Group Policy update: `gpupdate /force`
    - Verify settings applied: `gpresult /H gpresult.html` (review HTML report)

#### 4.1.2 Microsoft Security Compliance Toolkit

**Alternative Approach**: Use Microsoft's pre-built baseline GPOs

**Download Security Compliance Toolkit**:
- URL: https://www.microsoft.com/en-us/download/details.aspx?id=55319
- Includes: Baseline GPO templates for Windows 10/11, Office, Edge

**Import Microsoft Baseline**:

1. **Extract Toolkit**: Unzip to `C:\SecurityBaselines\`
2. **Open GPMC**: `gpmc.msc`
3. **Import Baseline GPO**:
   - Right-click on Group Policy Objects → New
   - Name: `Microsoft-Win11-Security-Baseline`
   - Right-click → Import Settings
   - Browse to `C:\SecurityBaselines\Windows 11 v23H2\GPOs\`
   - Select baseline backup folder
4. **Customize Microsoft Baseline**:
   - Review settings (Microsoft baselines are VERY strict)
   - Adjust settings that conflict with operational requirements
   - Example: Microsoft disables Remote Assistance → Re-enable if needed for IT support
5. **Link to OUs**: Link customized GPO to target OUs

### 4.2 Microsoft Intune Configuration Profiles (Cloud + Hybrid)

**Use Case**: Windows devices Azure AD joined or hybrid-joined, managed by Intune

#### 4.2.1 Create Device Configuration Profile

**Step-by-Step Procedure**:

1. **Access Microsoft Intune Admin Center**:
   - URL: https://endpoint.microsoft.com
   - Sign in with Intune Administrator credentials

2. **Create Configuration Profile**:
   - Navigate: **Devices** → **Configuration profiles** → **Create profile**
   - Platform: **Windows 10 and later**
   - Profile type: **Templates** → **Device restrictions** (or **Endpoint protection** for security-focused)

3. **Configure Device Restrictions**:
   
   **Password Settings**:
   ```
   Require password: Yes
   Required password type: Alphanumeric
   Minimum password length: 14 characters
   Number of sign-in failures before wiping device: 10
   Maximum minutes of inactivity until screen locks: 15 minutes
   Password expiration (days): 90
   Number of previous passwords to prevent reuse: 24
   ```

   **Device Security Settings**:
   ```
   Firewall: Require
   Antivirus: Require
   Anti-spyware: Require
   Microsoft Defender: Require
   Real-time protection: Require
   ```

4. **Create Endpoint Protection Profile** (for additional security settings):
   - Profile type: **Endpoint protection**
   
   **Microsoft Defender Antivirus**:
   ```
   Cloud-delivered protection: Enabled
   Block at first sight: Enabled
   File blocking level: High
   
   Scan settings:
   - Scan type: Quick scan
   - Scan day: Daily
   - Scan time: 2:00 AM
   ```

   **Windows Defender Firewall**:
   ```
   Domain network:
   - Firewall: Enable
   - Inbound connections: Block
   - Outbound connections: Allow
   
   Public network:
   - Firewall: Enable
   - Inbound connections: Block all
   ```

5. **Create AppLocker Profile** (Application Control):
   - Profile type: **Endpoint protection** → **Windows Defender Application Control**
   
   Or create custom OMA-URI settings for AppLocker:
   ```
   OMA-URI: ./Vendor/MSFT/AppLocker/ApplicationLaunchRestrictions/
   Data type: String (XML)
   Value: [AppLocker XML policy]
   ```

6. **Assign Profile to Device Groups**:
   - Click **Assignments**
   - Include groups: **All Windows 11 Devices** (or specific groups)
   - Exclude groups: **Pilot Devices** (initially, then remove exclusion after pilot)
   - Save

7. **Monitor Deployment**:
   - Navigate: **Devices** → **Configuration profiles** → Select profile
   - Click **Device status** or **User status**
   - View deployment success/failure/pending

#### 4.2.2 Intune Security Baselines

**Alternative**: Use Intune's built-in Security Baselines (recommended for simplicity)

**Procedure**:

1. **Access Security Baselines**:
   - Navigate: **Endpoint security** → **Security baselines**
   - Available baselines:
     - **Security Baseline for Windows 10 and later**
     - **Microsoft Defender for Endpoint baseline**
     - **Microsoft Edge baseline**

2. **Create Baseline Profile**:
   - Select **Security Baseline for Windows 10 and later**
   - Click **Create profile**
   - Name: `[Org] Windows 11 Security Baseline v1.0`

3. **Configure Settings** (or accept Microsoft defaults):
   - Review each category (Account Protection, Application Guard, BitLocker, etc.)
   - Adjust settings as needed
   - Microsoft baselines align with CIS Benchmarks (high compliance)

4. **Assign to Device Groups**:
   - Include: **All Corporate Windows Devices**
   - Pilot first with small group before production rollout

5. **Monitor Compliance**:
   - Navigate: **Endpoint security** → **Security baselines** → Select profile
   - View compliance summary (Compliant, Not compliant, In grace period, Not applicable)

### 4.3 BitLocker Encryption Deployment (Windows)

**Objective**: Encrypt all Windows laptops and desktops with BitLocker

#### 4.3.1 BitLocker via Group Policy

**GPO Configuration**:

1. **Create BitLocker GPO**:
   - Name: `[Org]-BitLocker-Enforcement`

2. **Configure BitLocker Policies** (Computer Configuration → Policies → Administrative Templates → Windows Components → BitLocker Drive Encryption):
   
   **Operating System Drives**:
   ```
   Require additional authentication at startup: Enabled
   - Allow BitLocker without a compatible TPM: Enabled (for non-TPM devices - password required)
   - Configure TPM startup: Allow TPM
   - Configure TPM startup PIN: Require startup PIN with TPM (for high-security devices)
   - Configure TPM startup key: Allow startup key with TPM
   
   Choose how BitLocker-protected operating system drives can be recovered: Enabled
   - Save BitLocker recovery information to AD DS: Enabled
   - Store recovery passwords and key packages: Enabled
   - Do not enable BitLocker until recovery information is stored: Enabled
   
   Choose drive encryption method and cipher strength: XTS-AES 256-bit
   ```

   **Fixed Data Drives**:
   ```
   Configure use of passwords for fixed data drives: Enabled (allow passwords)
   Choose drive encryption method: XTS-AES 256-bit
   ```

   **Removable Data Drives**:
   ```
   Control use of BitLocker on removable drives: Enabled
   Allow users to apply BitLocker protection on removable drives: Enabled
   Choose drive encryption method: XTS-AES 256-bit
   ```

3. **Link GPO** to all Windows computer OUs

4. **Enable BitLocker** (post-GPO deployment):
   - Option 1: Users enable BitLocker manually (Control Panel → System and Security → BitLocker Drive Encryption → Turn on BitLocker)
   - Option 2: Scripted enablement (PowerShell):
     ```powershell
     Enable-BitLocker -MountPoint "C:" -EncryptionMethod XtsAes256 -UsedSpaceOnly -TpmProtector
     ```
   - Option 3: SCCM/ConfigMgr task sequence (for automated deployment)

5. **Verify Recovery Key Escrow**:
   - Check Active Directory: BitLocker recovery passwords stored in computer object properties
   - PowerShell verification:
     ```powershell
     Get-ADComputer -Identity COMPUTERNAME -Properties "msTPM-OwnerInformation"
     ```

#### 4.3.2 BitLocker via Intune

**Procedure**:

1. **Create BitLocker Profile**:
   - Navigate: **Endpoint security** → **Disk encryption** → **Create Policy**
   - Platform: **Windows 10 and later**
   - Profile: **BitLocker**

2. **Configure BitLocker Settings**:
   
   **BitLocker – Base Settings**:
   ```
   Enable BitLocker: Yes
   Require storage cards to be encrypted (mobile only): Not configured
   Hide prompt about third-party encryption: Yes
   
   Allow standard users to enable encryption: Yes
   ```

   **BitLocker – OS Drive Settings**:
   ```
   BitLocker system drive policy: Enabled
   Startup authentication required: Yes
   Compatible TPM startup: Required
   Compatible TPM startup PIN: Allowed
   Compatible TPM startup key: Allowed
   Compatible TPM startup key and PIN: Allowed
   
   Minimum PIN length: 6
   Recovery options: Enabled
   - Allow certificate-based data recovery agent: Yes
   - User creation of recovery key: Allowed
   - Hide recovery options during BitLocker setup: No
   - Save BitLocker recovery information to Azure AD: Enabled
   - Storage of recovery information to Azure AD before enabling BitLocker: Required
   ```

   **Encryption Method**:
   ```
   Encryption method: XTS-AES 256-bit
   ```

3. **Assign Profile**:
   - Include groups: **All Corporate Windows Laptops**

4. **Monitor Deployment**:
   - Navigate: **Devices** → **Compliance policies** → **BitLocker compliance**
   - View per-device encryption status

5. **Retrieve Recovery Keys** (when needed):
   - Azure AD portal → Devices → All devices → Select device
   - Click **Recovery keys** → View BitLocker recovery key

---

## 5. macOS Baseline Implementation

### 5.1 Configuration Profiles (MDM)

**Use Case**: macOS devices managed by Jamf Pro or Intune

#### 5.1.1 Jamf Pro Configuration Profile

**Step-by-Step Procedure**:

1. **Access Jamf Pro Console**:
   - Navigate to: `https://[your-instance].jamfcloud.com`
   - Sign in with administrator credentials

2. **Create Configuration Profile**:
   - Navigate: **Computers** → **Configuration Profiles** → **New**
   - Name: `[Org] macOS Security Baseline v1.0`
   - Level: **Computer Level**

3. **Configure Passcode Policy** (Add payload: **Passcode**):
   ```
   Require passcode on device: Checked
   Allow simple passcode: Unchecked
   Require alphanumeric passcode: Checked
   Minimum passcode length: 14 characters
   Minimum number of complex characters: 1
   Maximum passcode age: 90 days
   Passcode history: 24 previous passcodes
   Maximum Auto-Lock: 15 minutes
   Maximum grace period for device lock: Immediately
   ```

4. **Configure FileVault Encryption** (Add payload: **Security & Privacy** → **FileVault**):
   ```
   Enable FileVault: Checked
   
   Recovery Key:
   - Escrow location: Jamf Pro (institutional recovery key)
   - Personal recovery key: Show recovery key to user
   
   Defer enablement: Allow user to defer (3 deferrals maximum, 24 hours between)
   ```

5. **Configure Firewall** (Add payload: **Security & Privacy** → **Firewall**):
   ```
   Enable Firewall: On
   Block all incoming connections: Unchecked (allow necessary services)
   Automatically allow built-in software to receive incoming connections: Checked
   Automatically allow downloaded signed software: Checked
   Enable stealth mode: Checked (don't respond to ICMP ping requests)
   ```

6. **Configure Gatekeeper** (Add payload: **Security & Privacy** → **Gatekeeper**):
   ```
   Gatekeeper: App Store and identified developers (default, good balance)
   
   For high-security:
   Gatekeeper: Mac App Store only
   ```

7. **Configure Restrictions** (Add payload: **Restrictions**):
   ```
   Functionality:
   - Allow Gatekeeper's Identified Developers option: Checked (unless ultra-high security)
   - Allow user to override Gatekeeper: Unchecked (prevent user bypasses)
   
   Applications:
   - Disallow "/Applications/Utilities/Terminal.app": Unchecked (allow for admins, restrict for standard users)
   
   Media:
   - Allow AirDrop: Checked (business use common)
   ```

8. **Configure System Preferences Restrictions** (Add payload: **Restrictions** → **Preferences**):
   ```
   Disable selected items:
   - Users & Groups (prevent local account creation)
   - Sharing (prevent unauthorized sharing services)
   ```

9. **Scope Configuration Profile**:
   - **Targets** tab:
     - **Computers**: All Computers (or specific Smart Group: "Corporate macOS Devices")
   - **Exclusions**: Test devices (initially)

10. **Save and Deploy**:
    - Click **Save**
    - Devices will receive profile on next check-in (usually within 15 minutes)

11. **Verify Deployment**:
    - Navigate: **Computers** → Select computer → **Configuration Profiles**
    - Verify "Installed" status

#### 5.1.2 Microsoft Intune Configuration Profile (macOS)

**Procedure**:

1. **Create Device Configuration Profile**:
   - Navigate: **Devices** → **Configuration profiles** → **Create profile**
   - Platform: **macOS**
   - Profile type: **Templates** → **Device restrictions**

2. **Configure Password Settings**:
   ```
   Required password type: Alphanumeric
   Minimum password length: 14 characters
   Number of sign-in failures before wiping device: 10
   Maximum minutes after screen lock before password is required: Immediately
   Maximum minutes of inactivity until screen locks: 15 minutes
   Password expiration (days): 90
   Number of previous passwords to prevent reuse: 24
   ```

3. **Configure Built-in Apps**:
   ```
   Block Siri: No (business use common)
   Block Safari autofill: No
   ```

4. **Assign Profile**:
   - Include groups: **All Corporate macOS Devices**

### 5.2 FileVault Encryption Deployment (macOS)

**Objective**: Encrypt all Mac laptops with FileVault

**Jamf Pro Method** (see 5.1.1 above - FileVault payload in configuration profile)

**Intune Method**:

1. **Create Encryption Profile**:
   - Navigate: **Endpoint security** → **Disk encryption** → **Create Policy**
   - Platform: **macOS**
   - Profile: **FileVault**

2. **Configure FileVault Settings**:
   ```
   Enable FileVault: Yes
   Recovery key type: Institutional recovery key
   Escrow location description: "[Organization] IT Department"
   Personal recovery key rotation: 12 months
   Disable prompt at sign out: No (allow user to enable later if they defer)
   Number of times allowed to bypass: 3
   ```

3. **Assign Profile**:
   - Include: **All Corporate Mac Laptops**

4. **Monitor Encryption Status**:
   - Navigate: **Devices** → **Monitor** → **Encryption report**
   - View per-device FileVault status

5. **Retrieve Recovery Keys**:
   - Intune portal → Devices → All devices → Select device
   - Click **Recovery keys** → View FileVault recovery key

---

## 6. Linux Baseline Implementation

### 6.1 Configuration Management Approach

**Use Case**: Linux endpoints (RHEL, Ubuntu, etc.) managed via configuration management

#### 6.1.1 Ansible Playbook Baseline

**Step-by-Step Procedure**:

1. **Create Ansible Inventory**:
   
   `inventory.ini`:
   ```ini
   [linux_workstations]
   workstation01.corp.local
   workstation02.corp.local
   workstation03.corp.local
   
   [linux_workstations:vars]
   ansible_user=ansible
   ansible_become=yes
   ansible_become_method=sudo
   ```

2. **Create Baseline Playbook**:
   
   `security_baseline.yml`:
   ```yaml
   ---
   - name: Linux Security Baseline Enforcement
     hosts: linux_workstations
     become: yes
     tasks:
       # === TASK 1: Password Policy Configuration ===
       - name: Configure password quality requirements
         lineinfile:
           path: /etc/security/pwquality.conf
           regexp: '^{{ item.key }}'
           line: '{{ item.key }} = {{ item.value }}'
         loop:
           - { key: 'minlen', value: '14' }
           - { key: 'dcredit', value: '-1' }  # At least 1 digit
           - { key: 'ucredit', value: '-1' }  # At least 1 uppercase
           - { key: 'lcredit', value: '-1' }  # At least 1 lowercase
           - { key: 'ocredit', value: '-1' }  # At least 1 special char
       
       - name: Configure password aging (login.defs)
         lineinfile:
           path: /etc/login.defs
           regexp: '^{{ item.key }}'
           line: '{{ item.key }}\t{{ item.value }}'
         loop:
           - { key: 'PASS_MAX_DAYS', value: '90' }
           - { key: 'PASS_MIN_DAYS', value: '1' }
           - { key: 'PASS_WARN_AGE', value: '7' }
       
       # === TASK 2: Account Lockout Policy ===
       - name: Configure account lockout (faillock)
         lineinfile:
           path: /etc/security/faillock.conf
           regexp: '^{{ item.key }}'
           line: '{{ item.key }} = {{ item.value }}'
         loop:
           - { key: 'deny', value: '5' }        # Lock after 5 failures
           - { key: 'unlock_time', value: '900' }  # 15 minutes lockout
           - { key: 'fail_interval', value: '900' } # 15 minute window
       
       # === TASK 3: SSH Hardening ===
       - name: Harden SSH configuration
         lineinfile:
           path: /etc/ssh/sshd_config
           regexp: '^#?{{ item.key }}'
           line: '{{ item.key }} {{ item.value }}'
         loop:
           - { key: 'PermitRootLogin', value: 'no' }
           - { key: 'PasswordAuthentication', value: 'yes' }  # Or 'no' if key-only
           - { key: 'PermitEmptyPasswords', value: 'no' }
           - { key: 'X11Forwarding', value: 'no' }
           - { key: 'MaxAuthTries', value: '3' }
           - { key: 'ClientAliveInterval', value: '300' }
           - { key: 'ClientAliveCountMax', value: '0' }
           - { key: 'Protocol', value: '2' }
         notify: Restart SSH
       
       # === TASK 4: Firewall Configuration (firewalld for RHEL/CentOS) ===
       - name: Ensure firewalld is installed
         package:
           name: firewalld
           state: present
       
       - name: Enable and start firewalld
         systemd:
           name: firewalld
           enabled: yes
           state: started
       
       - name: Set default zone to drop (restrictive)
         command: firewall-cmd --set-default-zone=drop
       
       - name: Allow SSH in public zone
         firewalld:
           service: ssh
           zone: public
           permanent: yes
           state: enabled
       
       # === TASK 5: Disable Unnecessary Services ===
       - name: Disable unnecessary services
         systemd:
           name: "{{ item }}"
           enabled: no
           state: stopped
         loop:
           - avahi-daemon
           - cups
         ignore_errors: yes  # Service may not exist on all systems
       
       # === TASK 6: Automatic Updates (Ubuntu) ===
       - name: Enable unattended upgrades (Ubuntu only)
         when: ansible_distribution == "Ubuntu"
         block:
           - name: Install unattended-upgrades
             apt:
               name: unattended-upgrades
               state: present
           
           - name: Configure automatic security updates
             lineinfile:
               path: /etc/apt/apt.conf.d/50unattended-upgrades
               regexp: '^//\s*"${distro_id}:${distro_codename}-security"'
               line: '  "${distro_id}:${distro_codename}-security";'
           
           - name: Enable automatic updates
             lineinfile:
               path: /etc/apt/apt.conf.d/20auto-upgrades
               create: yes
               line: |
                 APT::Periodic::Update-Package-Lists "1";
                 APT::Periodic::Unattended-Upgrade "1";
       
       # === TASK 7: Auditd Configuration ===
       - name: Ensure auditd is installed
         package:
           name: audit
           state: present
       
       - name: Enable and start auditd
         systemd:
           name: auditd
           enabled: yes
           state: started
       
       - name: Configure audit rules for privileged commands
         blockinfile:
           path: /etc/audit/rules.d/privileged.rules
           create: yes
           block: |
             # Monitor use of privileged commands (sudo)
             -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged
             -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged
         notify: Restart auditd
     
     handlers:
       - name: Restart SSH
         systemd:
           name: sshd
           state: restarted
       
       - name: Restart auditd
         command: service auditd restart
   ```

3. **Run Ansible Playbook**:
   ```bash
   ansible-playbook -i inventory.ini security_baseline.yml
   ```

4. **Verify Execution**:
   - Review Ansible output for failures
   - SSH to sample device and verify configurations:
     ```bash
     # Check password policy
     cat /etc/security/pwquality.conf | grep minlen
     
     # Check SSH hardening
     sshd -T | grep PermitRootLogin
     
     # Check firewalld status
     firewall-cmd --get-default-zone
     firewall-cmd --list-all
     ```

#### 6.1.2 Puppet Manifest Baseline

**Puppet Manifest Example** (`linux_baseline.pp`):

```puppet
# Linux Security Baseline Manifest

# Password quality
class { 'pam':
  password_quality => {
    'minlen'  => 14,
    'dcredit' => -1,
    'ucredit' => -1,
    'lcredit' => -1,
    'ocredit' => -1,
  },
}

# SSH hardening
class { 'ssh':
  server_options => {
    'PermitRootLogin'        => 'no',
    'PasswordAuthentication' => 'yes',
    'PermitEmptyPasswords'   => 'no',
    'X11Forwarding'          => 'no',
    'MaxAuthTries'           => '3',
  },
}

# Firewall (firewalld)
class { 'firewalld':
  default_zone => 'drop',
  services     => ['ssh'],
}

# Disable unnecessary services
service { 'avahi-daemon':
  ensure => 'stopped',
  enable => false,
}

# Auditd
class { 'auditd':
  ensure => 'present',
  enable => true,
  rules  => [
    '-a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -k privileged',
  ],
}
```

**Apply Manifest**:
```bash
puppet apply linux_baseline.pp
```

### 6.2 LUKS Encryption (Linux Full Disk Encryption)

**Objective**: Encrypt Linux laptops with LUKS

**LUKS Encryption During OS Installation**:
- Most Linux distributions (RHEL, Ubuntu) offer LUKS encryption during installation
- Check "Encrypt disk" or "Use LVM with encryption" option
- Set encryption passphrase
- Post-install: Passphrase required at boot

**Post-Installation LUKS Encryption** (complex - requires re-partitioning):
- Generally not recommended for existing systems (data loss risk high)
- Better approach: Provision new encrypted systems, migrate data

**LUKS Key Management**:
- Store LUKS passphrases securely (password manager, secure vault)
- No centralized escrow like BitLocker/FileVault (manual key management required)

---

## 7. Mobile Device Baselines

### 7.1 iOS Baseline (via MDM)

**Use Case**: Corporate-owned and BYOD iPhones/iPads

#### 7.1.1 iOS Configuration Profile (Jamf Pro)

**Procedure**:

1. **Create iOS Configuration Profile**:
   - Navigate: **Mobile Devices** → **Configuration Profiles** → **New**

2. **Configure Passcode** (Add payload: **Passcode**):
   ```
   Require passcode on device: Checked
   Allow simple passcode: Unchecked
   Require alphanumeric passcode: Checked
   Minimum passcode length: 8 characters (iOS 17 supports up to 16)
   Minimum number of complex characters: 1
   Maximum passcode age: 90 days
   Passcode history: 8 previous passcodes
   Maximum Auto-Lock: 5 minutes (corporate) / 15 minutes (BYOD)
   Maximum grace period: Immediately
   ```

3. **Configure Restrictions** (Add payload: **Restrictions**):
   ```
   Functionality:
   - Allow screenshots: Checked (unless ultra-high security)
   - Allow AirDrop: Checked (business collaboration)
   - Force encrypted backups: Checked (if backups allowed)
   
   Apps:
   - Allow installing apps: Checked (BYOD) / Unchecked (Corporate - deploy via VPP)
   - Allow removing apps: Checked (BYOD) / Unchecked (Corporate)
   
   iCloud:
   - Allow iCloud backup: Checked (BYOD) / Unchecked (Corporate - use Jamf backup)
   - Allow iCloud Keychain: Checked
   ```

4. **Configure Wi-Fi** (if corporate Wi-Fi access):
   - Add payload: **Wi-Fi**
   - Configure SSID, security type (WPA2 Enterprise), authentication

5. **Configure VPN** (if VPN access required):
   - Add payload: **VPN**
   - Configure VPN settings (IPSec, SSL VPN, etc.)

6. **Scope and Deploy**:
   - Scope to appropriate Smart Groups (Corporate iOS Devices, BYOD iOS Devices)
   - Save and deploy

#### 7.1.2 iOS Encryption

**Note**: iOS devices are encrypted by default once a passcode is set

**Verification**:
- Setting passcode automatically enables Data Protection (hardware encryption)
- No additional configuration needed for encryption
- MDM can enforce passcode via configuration profile → Encryption guaranteed

### 7.2 Android Baseline (via MDM)

**Use Case**: Corporate Android devices (Android Enterprise work profile)

#### 7.2.1 Android Configuration Profile (Intune)

**Procedure**:

1. **Create Device Configuration Profile**:
   - Navigate: **Devices** → **Configuration profiles** → **Create profile**
   - Platform: **Android Enterprise**
   - Profile type: **Device restrictions** (Work Profile)

2. **Configure Password Settings**:
   ```
   Required password type: At least alphanumeric
   Minimum password length: 8 characters
   Number of sign-in failures before wiping device: 10
   Maximum minutes of inactivity until screen locks: 15 minutes
   Password expiration (days): 90
   Number of previous passwords to prevent reuse: 8
   ```

3. **Configure Work Profile Settings**:
   ```
   Work profile password:
   - Require separate work profile password: Yes (BYOD - separate personal/work)
   - Minimum work profile password length: 8
   
   Work and personal profile data sharing:
   - Copy and paste between work and personal profiles: Block
   - Data sharing between work and personal profiles: Block
   
   Work profile notifications:
   - Work profile notifications while device locked: Show all notifications
   ```

4. **Configure Device Security**:
   ```
   Encryption: Require (Android 6.0+ encrypted by default)
   Google Play Protect: Require
   ```

5. **Assign Profile**:
   - Include: **All Corporate Android Devices** or **BYOD Android Devices**

#### 7.2.2 Android Encryption

**Note**: Android devices (6.0+) are encrypted by default

**Verification**:
- MDM configuration profile enforces encryption setting
- On device: Settings → Security → Encryption → Should show "Encrypted"

---

## 8. Baseline Compliance Monitoring

### 8.1 Automated Compliance Scanning

**Objective**: Continuously monitor endpoint compliance with baselines

#### 8.1.1 Windows Compliance (Intune)

**Create Compliance Policy**:

1. **Navigate**: **Devices** → **Compliance policies** → **Create Policy**
2. **Platform**: Windows 10 and later
3. **Configure Compliance Settings**:
   
   **Device Health**:
   ```
   Require BitLocker: Yes
   Require Secure Boot: Yes
   Require code integrity: Yes
   ```

   **Device Properties**:
   ```
   Minimum OS version: 10.0.19041 (Windows 10 20H1 or later)
   Maximum OS version: Not configured (allow latest)
   ```

   **System Security**:
   ```
   Require password to unlock mobile devices: Yes
   Simple passwords: Block
   Password type: Alphanumeric
   Minimum password length: 14
   Maximum minutes of inactivity before password is required: 15
   Password expiration (days): 90
   Number of previous passwords to prevent reuse: 24
   
   Firewall: Require
   Antivirus: Require
   Antispyware: Require
   Microsoft Defender Antimalware: Require
   ```

4. **Assign Policy**:
   - Include: **All Corporate Windows Devices**

5. **Configure Actions for Noncompliance**:
   - Immediately: Mark device as noncompliant
   - After 3 days: Send email to end user
   - After 7 days: Block device from corporate resources (conditional access)

#### 8.1.2 macOS Compliance (Jamf Pro)

**Extension Attribute** (custom compliance check):

1. **Create Extension Attribute**:
   - Navigate: **Settings** → **Computer Management** → **Extension Attributes** → **New**
   - Name: `Baseline Compliance Status`
   - Data Type: String
   - Input Type: Script

2. **Script Example**:
   ```bash
   #!/bin/bash
   
   # Check FileVault status
   fv_status=$(fdesetup status | grep "On")
   
   # Check firewall status
   fw_status=$(defaults read /Library/Preferences/com.apple.alf globalstate)
   
   # Check Gatekeeper
   gk_status=$(spctl --status | grep "enabled")
   
   if [[ -n "$fv_status" ]] && [[ "$fw_status" -eq 1 ]] && [[ -n "$gk_status" ]]; then
       echo "<result>Compliant</result>"
   else
       echo "<result>Non-Compliant</result>"
   fi
   ```

3. **Create Smart Group** (Non-Compliant Devices):
   - Criteria: Baseline Compliance Status **is not** Compliant
   - Use for reporting and remediation targeting

#### 8.1.3 Linux Compliance (Ansible)

**Compliance Check Playbook** (`compliance_check.yml`):

```yaml
---
- name: Linux Baseline Compliance Check
  hosts: linux_workstations
  become: yes
  tasks:
    - name: Check password minimum length
      shell: grep "^minlen" /etc/security/pwquality.conf | awk '{print $3}'
      register: minlen_check
      failed_when: minlen_check.stdout|int < 14
    
    - name: Check SSH PermitRootLogin
      shell: sshd -T | grep "^permitrootlogin" | awk '{print $2}'
      register: ssh_check
      failed_when: ssh_check.stdout != "no"
    
    - name: Check firewalld status
      shell: systemctl is-active firewalld
      register: firewalld_check
      failed_when: firewalld_check.stdout != "active"
    
    - name: Generate compliance report
      debug:
        msg: "Compliance checks passed"
```

**Run Compliance Check**:
```bash
ansible-playbook -i inventory.ini compliance_check.yml
```

**Failed checks** → Non-compliant devices → Remediate

### 8.2 Compliance Reporting and Dashboards

**Intune Compliance Reports**:
- Navigate: **Devices** → **Monitor** → **Noncompliant devices**
- Export report: CSV
- Schedule: Weekly compliance summary email to security team

**Jamf Pro Compliance Dashboard**:
- Create Advanced Search for non-compliant devices
- Export to CSV
- Schedule report via Jamf API

**Compliance Metrics** (track over time):
- **Overall Compliance Rate**: (Compliant Devices / Total Devices) × 100%
- **Target**: ≥95% compliance
- **Baseline Compliance by Control**:
  - Encryption compliance: X%
  - Firewall compliance: Y%
  - Password policy compliance: Z%
- **Trend Analysis**: Is compliance improving or degrading?

### 8.3 Configuration Drift Detection

**Objective**: Detect when baseline configurations are manually changed

**Windows Group Policy Results** (drift detection):
```powershell
# Run on endpoint
gpresult /H gpresult.html

# Compare to expected baseline GPO settings
# Manual review or scripted comparison
```

**Intune Configuration Drift**:
- Intune automatically re-applies configuration profiles
- If user changes setting → Intune reverts on next check-in (typically 8 hours)
- Monitor **Device status** for "Error" or "Conflict" status

**Jamf Pro Configuration Drift**:
- Similar to Intune: Configuration profiles automatically re-apply
- Monitor profile installation status

---

## 9. Exception Handling Process

### 9.1 Exception Scenarios

**Valid Exception Reasons**:
- **Business Requirement**: Critical business workflow requires exception (e.g., developers need local admin rights)
- **Technical Limitation**: Device lacks capability (e.g., no TPM for BitLocker)
- **Temporary Workaround**: Short-term exception during system migration
- **BYOD Privacy**: Personal device cannot enforce corporate baseline fully

**Invalid Exception Reasons**:
- "It's inconvenient"
- "User doesn't like it"
- "We've always done it this way"

### 9.2 Exception Request Workflow

**Procedure**:

1. **Submit Exception Request** (via IT ticket):
   - Required fields:
     - Device ID / User
     - Baseline requirement to be excepted (e.g., "BitLocker encryption")
     - Business justification
     - Proposed compensating controls (if any)
     - Exception duration (temporary or permanent)
     - Risk assessment (what risk does this exception introduce?)

2. **Security Review**:
   - Security team reviews request
   - Assess risk vs. business need
   - Recommend approval or denial

3. **Approval Authorities**:
   - **Low-risk exceptions** (e.g., screen lock timeout extension): IT Manager
   - **Medium-risk exceptions** (e.g., disable USB storage for specific user): Security Manager
   - **High-risk exceptions** (e.g., disable BitLocker, local admin rights): CISO approval required

4. **Exception Documentation**:
   - Approved exceptions logged in Exception Register
   - Columns: Device ID, User, Exception Type, Justification, Approver, Approval Date, Expiration Date, Compensating Controls

5. **Exception Implementation**:
   - **GPO**: Move device to exception OU (unlink baseline GPO)
   - **Intune**: Add device to exclusion group
   - **Jamf**: Add device to exclusion scope

6. **Periodic Review**:
   - **Quarterly**: Review all active exceptions
   - Verify exception still needed
   - Revoke if no longer necessary
   - Renew if still valid (annual re-approval required)

### 9.3 Compensating Controls

**Examples**:

- **Exception**: BitLocker disabled (no TPM on old laptop)
  - **Compensating Control**: Enhanced physical security (locked office), frequent backups (encrypted backup destination), device nearing end-of-life (replacement scheduled)

- **Exception**: Developer needs local admin rights
  - **Compensating Control**: Enhanced monitoring (privileged utility logging), regular security assessments, developer security training, least privilege admin account (separate from standard account)

- **Exception**: BYOD device cannot enforce full baseline
  - **Compensating Control**: Containerized app management (MAM), remote wipe capability, conditional access (require MFA), limited data access (no confidential data on BYOD)

---

## 10. Verification Procedures

### 10.1 Baseline Deployment Verification

**Post-Deployment Checklist**:

1. **Verify GPO Application** (Windows):
   - Sample device: Run `gpupdate /force`
   - Generate GPO report: `gpresult /H gpresult.html`
   - Review HTML report: Verify baseline GPO applied successfully
   - Check for conflicts: No "Access Denied" or "Empty" errors

2. **Verify Intune Profile Deployment**:
   - Intune portal → Devices → Configuration profiles → Select profile
   - Check **Device status**: View success vs. error count
   - Drill into errors: Identify devices with deployment failures
   - Remediate failures

3. **Verify Jamf Profile Installation**:
   - Jamf Pro → Computers → Select computer → Configuration Profiles tab
   - Verify profile shows "Installed"
   - If "Failed": Review logs, re-deploy

4. **Spot-Check Compliance** (manual verification):
   - Random sample: 20 devices
   - Remote desktop (RDP, VNC, SSH) to device
   - Verify settings:
     - Password policy: `net accounts` (Windows), `pwpolicy` (macOS), `chage -l username` (Linux)
     - Firewall: `netsh advfirewall show allprofiles` (Windows), `sudo ufw status` (Linux), System Preferences (macOS)
     - Encryption: BitLocker status, FileVault status, LUKS status
   - Document discrepancies

### 10.2 Encryption Deployment Verification

**Windows BitLocker**:
```powershell
# Check BitLocker status
Get-BitLockerVolume -MountPoint C:

# Expected output:
# EncryptionMethod: XtsAes256
# VolumeStatus: FullyEncrypted
# ProtectionStatus: On
```

**macOS FileVault**:
```bash
# Check FileVault status
fdesetup status

# Expected output: "FileVault is On."
```

**Linux LUKS**:
```bash
# Check LUKS status
lsblk -f | grep crypto_LUKS

# Should show encrypted partitions
```

### 10.3 Compliance Rate Monitoring

**Monthly Compliance Review**:
- Generate compliance report from MDM/Intune/Jamf
- Calculate compliance rate per baseline requirement:
  - Encryption: X% encrypted
  - Firewall: Y% firewall enabled
  - Password policy: Z% compliant
- Identify trends (improving or degrading)
- Escalate chronic non-compliance (devices repeatedly non-compliant)

---

## 11. Common Pitfalls and Troubleshooting

### 11.1 Common Mistakes

**Pitfall 1: Baseline Too Strict - Users Unable to Work**
- **Problem**: Security baseline breaks critical business workflows. Example: AppLocker blocks required software, screen lock timeout too short for users giving presentations.
- **Solution**: Pilot deployment FIRST with diverse user group. Collect feedback. Adjust baseline before production rollout. Balance security with usability.

**Pitfall 2: BitLocker Deployment Fails - No TPM**
- **Problem**: Older devices lack TPM 2.0, BitLocker GPO requires TPM, encryption fails.
- **Solution**: Adjust BitLocker GPO to allow "BitLocker without compatible TPM" (password-based). Accept risk for older devices (plan for hardware refresh).

**Pitfall 3: Jamf Configuration Profile Not Applying - Scope Issue**
- **Problem**: Created profile but devices not receiving it.
- **Solution**: Check **Scope** tab in Jamf Pro. Verify devices are in target Smart Group or included in "All Computers". Check for exclusions.

**Pitfall 4: GPO Conflicts - Multiple GPOs Setting Same Policy**
- **Problem**: Baseline GPO sets screen timeout to 15 minutes, another GPO sets it to 30 minutes. Unpredictable behavior.
- **Solution**: Review GPO precedence (GPMC → View GPO links). Higher precedence GPO wins. Consolidate settings into single baseline GPO where possible. Use GPO comments to document purpose.

**Pitfall 5: Intune Profile Deployment Error - Incorrect Setting**
- **Problem**: Profile deployment fails with error "Setting not applicable".
- **Solution**: Check OS version requirements. Some settings only apply to specific Windows versions (e.g., Windows 11 only). Adjust profile or create separate profiles per OS version.

**Pitfall 6: User Complaints About Password Complexity**
- **Problem**: Users frustrated by 14-character password requirement, frequent expiration.
- **Solution**: Educate users on password managers (corporate-approved tool). Consider passphrase approach (4 random words = long but memorable). Balance security with user acceptance.

**Pitfall 7: Baseline Deployment Breaks VPN or Other Critical Service**
- **Problem**: Firewall baseline blocks VPN traffic. Users unable to connect remotely.
- **Solution**: Pilot deployment exposes this. Before production, test all critical services (VPN, file shares, printers, etc.). Adjust firewall rules to allow necessary traffic.

### 11.2 Troubleshooting Guide

**Issue: Group Policy Not Applying to Device**
- **Symptoms**: `gpresult` shows baseline GPO not applied.
- **Diagnosis**:
  - Check device OU placement (is device in correct OU where GPO is linked?)
  - Check GPO link status (is GPO link enabled, not disabled?)
  - Check security filtering (does device have Read + Apply GPO permissions?)
  - Check WMI filtering (if WMI filter applied, does device meet filter criteria?)
- **Solution**:
  - Move device to correct OU
  - Enable GPO link
  - Adjust security filtering (add computer to security group with GPO apply permission)
  - Remove or adjust WMI filter

**Issue: BitLocker Not Encrypting - "Waiting for Activation"**
- **Symptoms**: BitLocker shows "Waiting for Activation" status indefinitely.
- **Diagnosis**:
  - Check TPM status: `tpm.msc` (is TPM enabled and initialized?)
  - Check recovery key escrow: Has recovery key been backed up to AD/Azure AD? (GPO may require escrow before enabling)
- **Solution**:
  - Initialize TPM (BIOS setting + `tpm.msc`)
  - Manually back up recovery key to AD: `manage-bde -protectors -adbackup C:`
  - Then enable BitLocker

**Issue: Intune Profile Shows "Error" Status**
- **Symptoms**: Configuration profile deployment shows "Error" for multiple devices.
- **Diagnosis**:
  - Click into error details: View error message
  - Common errors:
    - "Setting not supported on this OS version"
    - "Conflicting setting from another profile"
    - "Device not compliant with prerequisites"
- **Solution**:
  - Adjust profile to remove unsupported settings
  - Resolve conflicts (disable conflicting profile or adjust precedence)
  - Ensure device meets prerequisites (OS version, enrollment status)

**Issue: macOS Configuration Profile Installation Failed**
- **Symptoms**: Jamf shows profile "Failed" status.
- **Diagnosis**:
  - On Mac: System Preferences → Profiles → Check for error
  - Common issues:
    - User declined profile installation (if user-approved enrollment)
    - Profile signed with expired certificate
    - Conflicting profile already installed
- **Solution**:
  - Re-deploy profile
  - Update Jamf Pro certificate
  - Remove conflicting profile manually, then re-deploy

**Issue: Ansible Playbook Fails on Some Devices**
- **Symptoms**: Ansible playbook successful on 80% of devices, fails on 20%.
- **Diagnosis**:
  - Review Ansible output: Which tasks failed?
  - SSH to failed device, run failed command manually
  - Common issues:
    - Package name different on different distros (firewalld vs. ufw)
    - Service name different (sshd vs. ssh)
    - File paths different (/etc/ssh/sshd_config vs. /etc/sshd_config)
- **Solution**:
  - Add conditional tasks: `when: ansible_distribution == "Ubuntu"`
  - Use `ignore_errors: yes` for non-critical tasks
  - Standardize on single Linux distro if possible

---

## 12. Integration with Other Controls

### 12.1 A.8.7 (Protection Against Malware)

**Integration Point**: Security baseline includes anti-malware configuration

**How They Integrate**:
- Baseline enables Windows Defender / macOS XProtect / Linux ClamAV
- Baseline enforces real-time protection, automatic updates
- Malware protection assessment (A.8.7) verifies baseline-configured settings

**Implementation**:
- Windows baseline: GPO configures Windows Defender settings
- macOS baseline: Gatekeeper enforcement (baseline) + third-party AV if deployed
- Linux baseline: Install and enable ClamAV (Ansible playbook)

### 12.2 A.8.18 (Use of Privileged Utility Programs)

**Integration Point**: Baseline restricts privileged utility access

**How They Integrate**:
- Baseline configures UAC (Windows), sudo restrictions (Linux)
- Baseline may block administrative tools for standard users (AppLocker, Gatekeeper)
- Privileged utility management (A.8.18) monitors usage of tools allowed by baseline

**Implementation**:
- Windows: UAC prompts configured via baseline GPO
- Linux: `sudo` configuration (baseline playbook) restricts which users can elevate
- macOS: Gatekeeper blocks unapproved utilities

### 12.3 A.8.19 (Installation of Software on Operational Systems)

**Integration Point**: Baseline enforces software installation restrictions

**How They Integrate**:
- Baseline deploys AppLocker (Windows), Gatekeeper (macOS), package manager restrictions (Linux)
- Software installation controls (A.8.19) define approved software list
- Baseline enforces approved list via application control technologies

**Implementation**:
- Windows: AppLocker rules in baseline GPO
- macOS: Gatekeeper + MDM restrictions in baseline profile
- Linux: Package manager permissions (baseline playbook)

---

## 13. Maintenance and Updates

### 13.1 Regular Maintenance Tasks

**Daily** (automated):
- MDM compliance sync (Intune, Jamf auto-sync)
- Configuration drift detection and auto-remediation

**Weekly**:
- Review compliance reports
- Identify chronic non-compliant devices
- Initiate remediation for non-compliant devices

**Monthly**:
- Spot-check compliance (sample verification)
- Review exception register (are exceptions still valid?)
- Baseline compliance metrics dashboard update

**Quarterly**:
- Full baseline compliance assessment
- Exception register review (renew or revoke exceptions)
- Baseline effectiveness review (are baselines preventing incidents?)

**Annually**:
- CIS Benchmark update review (new benchmark versions released)
- Baseline revision (update to latest CIS recommendations)
- Stakeholder re-approval (IT ops, security, business)

### 13.2 Baseline Update Procedures

**When to Update Baseline**:
- New CIS Benchmark version released
- New OS version deployed (e.g., Windows 12, macOS 15)
- Security incident reveals baseline gap (e.g., attack exploited weak setting)
- Regulatory requirement changes (new compliance mandate)

**Update Procedure**:

1. **Review Change Trigger**:
   - New CIS Benchmark: Compare new vs. current baseline
   - Incident: Identify setting that needs strengthening
   - Compliance: Identify new requirement

2. **Draft Updated Baseline**:
   - Document proposed changes
   - Example: "Increase password minimum length from 14 to 16 characters"

3. **Impact Assessment**:
   - Will change break existing workflows?
   - How many users affected?
   - User training required?

4. **Stakeholder Review** (same as initial baseline development):
   - Security, IT ops, user representatives

5. **Pilot Updated Baseline**:
   - Deploy to test group (50-100 devices)
   - Monitor for issues (2-4 weeks)
   - Collect user feedback

6. **Production Rollout**:
   - Phased deployment
   - Monitor closely for first 2 weeks
   - Roll back if critical issues discovered

7. **Version Control**:
   - Update baseline document version (e.g., v1.0 → v2.0)
   - Document changes in version history table
   - Archive previous baseline version (for audit trail)

### 13.3 CIS Benchmark Refresh Cycle

**CIS Benchmark Release Cadence**:
- CIS updates benchmarks 1-2 times per year (varies by OS)
- Monitor CIS website for new releases: https://www.cisecurity.org/cis-benchmarks/

**Benchmark Update Procedure**:

1. **Download New Benchmark**: CIS releases new version
2. **Gap Analysis**: Compare new benchmark to current [Org] baseline
3. **Risk Assessment**: Are new recommendations addressing significant risks?
4. **Decide on Adoption**:
   - Adopt: Update baseline to include new recommendations
   - Defer: Risk is low, adopt in next annual review
   - Reject: Recommendation not applicable to [Org]
5. **If Adopting**: Follow baseline update procedures (section 13.2)

---

## 14. Conclusion

### 14.1 Success Criteria Summary

**Baseline implementation is successful when**:
- ✅ **Coverage**: ≥95% of endpoints have baseline applied (via GPO/MDM)
- ✅ **Compliance**: ≥90% of endpoints compliant with baseline requirements
- ✅ **Encryption**: ≥95% of laptops encrypted (BitLocker/FileVault/LUKS)
- ✅ **Monitoring**: Automated compliance monitoring in place (Intune/Jamf/Ansible)
- ✅ **Maintenance**: Quarterly compliance reviews conducted
- ✅ **Exceptions**: All exceptions documented, approved, reviewed quarterly
- ✅ **User Acceptance**: <5% of users report baseline causing significant productivity issues

### 14.2 Key Takeaways

1. **CIS Benchmarks = Starting Point**: Don't reinvent the wheel. Use CIS Benchmarks as foundation, customize based on risk tolerance.

2. **Pilot Before Production**: Never deploy baseline to entire organization without pilot testing. Baselines can break workflows if not properly validated.

3. **Balance Security and Usability**: Overly restrictive baselines lead to workarounds and shadow IT. Involve users in baseline development.

4. **Automate Enforcement**: Manual baseline enforcement doesn't scale. Use GPO, MDM, configuration management to automate.

5. **Continuous Monitoring**: Baseline deployment is not "set and forget". Monitor compliance continuously, remediate drift.

6. **Encryption is Non-Negotiable**: All laptops MUST be encrypted (BitLocker/FileVault/LUKS). Unencrypted laptops = critical risk.

7. **Exception Management is Critical**: Uncontrolled exceptions undermine entire baseline. Require justification, approval, periodic review.

8. **Integration with Other Controls**: Baselines enable A.8.7 (malware protection), A.8.18 (privileged utilities), A.8.19 (software controls). They work together.

---

**END OF DOCUMENT**

*This implementation guide provides the practical procedures to develop, deploy, and maintain endpoint security baselines across all device types. Use it as a step-by-step playbook for achieving A.8.1 compliance through systematic baseline enforcement.*
