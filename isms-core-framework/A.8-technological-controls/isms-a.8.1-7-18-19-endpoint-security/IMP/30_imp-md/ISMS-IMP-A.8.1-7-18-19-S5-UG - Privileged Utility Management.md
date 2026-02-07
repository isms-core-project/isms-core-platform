**ISMS-IMP-A.8.1-7-18-19-S5-UG - Privileged Utility Management**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S5-UG |
| **Version** | 1.0 |
| **Assessment Area** | Privileged Utility Programs Access and Usage Control |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.3 (Privileged Utility Management) |
| **Purpose** | Document privileged utilities, assess access controls, verify usage monitoring, track approval workflows |
| **Target Audience** | Security Engineers, IT Operations, System Administrators, Privileged Access Management Team, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (usage monitoring), Quarterly (full assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for privileged utility assessment | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.1-7-18-19-S5-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.1-7-18-19-S5 - Privileged Utility Management Assessment

#### What This Assessment Covers

This assessment evaluates [Organization]'s controls over privileged utility programs - tools that can bypass or disable security controls. This answers:

- What privileged utilities are present on endpoints?
- Who has access to privileged utilities?
- Are access controls enforced (RBAC, AppLocker, PAM)?
- Is privileged utility usage logged and monitored?
- Are approval workflows in place for access requests?
- What security bypass tools exist (can disable antivirus, edit logs, etc.)?
- What gaps exist in privileged utility controls?

#### Key Principle

**Privileged utilities are HIGH-RISK tools that require strong controls:**

- ❌ Weak: "Admins can use any tools they need"
- ✅ Strong: "Registry Editor requires PAM approval, usage logged, reviewed monthly"

Privileged utilities can disable security controls, modify system configurations, access sensitive data, and cover tracks. They must be strictly controlled.

#### What You'll Document

**Privileged Utility Inventory:**

- System administration tools (Registry Editor, Services, Task Manager)
- Remote access tools (RDP, VNC, SSH, TeamViewer)
- Debugging tools (WinDbg, gdb, debuggers)
- Password tools (password resets, hash dumpers)
- Network tools (Wireshark, port scanners, protocol analyzers)
- Security bypass tools (anti-malware disablers, log editors, rootkit detectors)

**Access Controls:**

- Who can access each utility (RBAC groups)
- How access is enforced (AppLocker, PAM, sudo, MDM)
- Access approval workflows
- Standing vs. temporary vs. emergency access

**Usage Monitoring:**

- Logging mechanisms (event logs, SIEM, PAM logs)
- Usage review processes
- Anomaly detection
- Incident response for unauthorized usage

#### How This Relates to Other Assessments

| Assessment | Focus | Relationship to S5 |
|------------|-------|-------------------|
| S1 - Endpoint Discovery | Inventory | Provides endpoint list for S5 |
| S2 - Security Baselines | Configuration | Baseline includes privileged utility restrictions |
| S3 - Malware Protection | Protection | Privileged utilities can disable protection |
| S4 - Software Controls | Software Governance | Privileged utilities are subset of software |
| **S5 - Privileged Utilities** | **High-Risk Tool Control** | **Who can use dangerous tools, how controlled** |
| S6 - Compliance Assessment | Consolidated View | Overall compliance |

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Privileged Access Management (PAM) Team** - Tool access controls
2. **Security Operations Center (SOC)** - Usage monitoring
3. **System Administrators** - Tool usage and requirements
4. **Security Engineering** - Policy and control design
5. **Compliance** - Audit readiness

#### Time Commitment

- **Initial assessment:** 8-12 hours (inventory and access control review)
- **Monthly updates:** 2-3 hours (usage monitoring review)
- **Quarterly updates:** 4-6 hours (full assessment with recertification)

### Expected Outputs

Upon completion, you will have:

1. ✅ Complete privileged utility inventory
2. ✅ Access control matrix (who can use what)
3. ✅ Approval workflow documentation
4. ✅ Usage monitoring configuration
5. ✅ Security bypass tool identification
6. ✅ Usage audit logs and review records
7. ✅ Gap analysis with remediation plans
8. ✅ Evidence register for audit
9. ✅ Approved assessment

---

## Prerequisites

### Information You'll Need

#### 1. Endpoint Inventory

- **From S1:** Complete endpoint inventory
- Required: Device name, OS type, endpoint type (admin workstation, standard user, server)

#### 2. Privileged Utility Access

- Access to endpoint management platforms
- Access to PAM solution (if deployed)
- Access to Active Directory / identity management
- Access to SIEM for usage logs

#### 3. Documentation

- Privileged utility inventory (if exists)
- Access control policies
- Approval workflows for privileged access
- PAM solution documentation
- Audit/logging configurations

#### 4. Access Control Data

- RBAC group memberships (who's in admin groups)
- AppLocker / allowlisting policies
- PAM access grants and approvals
- sudo configurations (Linux)
- MDM restrictions (mobile)

### Tools You'll Use

**Access Control:**

- Privileged Access Management (CyberArk, BeyondTrust, Delinea, etc.)
- Active Directory / Entra ID
- AppLocker / Application Control
- sudo (Linux)
- MDM (Intune, Jamf, etc.)

**Monitoring:**

- SIEM platform
- Windows Event Logs
- Linux audit logs (auditd)
- PAM session recordings
- Endpoint detection and response (EDR)

### Access Requirements

- Read access to identity management systems
- Read access to PAM solution
- Read access to SIEM
- Read access to endpoint management consoles
- Access to approval workflow systems

---

## Assessment Workflow

### High-Level Process

```
1. IMPORT ENDPOINT INVENTORY (from S1)
2. IDENTIFY PRIVILEGED UTILITIES (Sheet 1)
3. DOCUMENT ACCESS CONTROLS (Sheet 2)
4. ASSESS APPROVAL WORKFLOWS (Sheet 3)
5. VERIFY USAGE MONITORING (Sheet 4)
6. IDENTIFY SECURITY BYPASS TOOLS (Sheet 5)
7. CONSOLIDATE GAPS (Sheet 6)
8. REGISTER EVIDENCE (Sheet 7)
9. CALCULATE DASHBOARD METRICS (Sheet 8)
10. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (1-2 hours)

**Steps:**
1. Read this entire User Guide
2. Gather all prerequisites
3. Review policy requirements (ISMS-POL-A.8.1-7-18-19, Section 2.3)
4. Export endpoint inventory from S1
5. Schedule time with SMEs (PAM team, sysadmins, SOC)
6. Create working folder for evidence

**Deliverable:** Prerequisites gathered, SME availability

#### Phase 2: Utility Inventory (2-3 hours)

**Objective:** Complete Sheet 1 - Utility Inventory

**Steps:**
1. Identify privileged utilities by category
2. Determine prevalence (which endpoints have which utilities)
3. Classify by risk level
4. Document business justification

**Deliverable:** Complete Sheet 1

#### Phase 3: Access Control Assessment (2-3 hours)

**Objective:** Complete Sheet 2 - Access Control

**Steps:**
1. Document access control mechanism per utility
2. Identify who has access (RBAC groups, individuals)
3. Verify enforcement (AppLocker, PAM, sudo)
4. Test access controls (can standard users access?)

**Deliverable:** Complete Sheet 2

#### Phase 4: Approval Workflow Verification (1-2 hours)

**Objective:** Complete Sheet 3 - Approval Workflow

**Steps:**
1. Document approval process for each utility
2. Review recent approval requests
3. Assess recertification process
4. Identify standing vs. temporary access

**Deliverable:** Complete Sheet 3

#### Phase 5: Usage Monitoring Assessment (2-3 hours)

**Objective:** Complete Sheet 4 - Usage Monitoring

**Steps:**
1. Verify logging configuration per utility
2. Check SIEM integration
3. Review recent usage (sample period)
4. Assess anomaly detection
5. Review incident response for unauthorized usage

**Deliverable:** Complete Sheet 4

#### Phase 6: Security Bypass Tool Identification (1-2 hours)

**Objective:** Complete Sheet 5 - Security Bypass Tools

**Steps:**
1. Identify tools that can disable security controls
2. Assess risk for each bypass tool
3. Document compensating controls
4. Verify access restrictions

**Deliverable:** Complete Sheet 5

#### Phase 7: Gap Identification (1 hour)

**Objective:** Complete Sheet 6 - Gaps

**Steps:**
1. Consolidate gaps from all sheets
2. Assess risk levels
3. Develop remediation plans

**Deliverable:** Complete Sheet 6

#### Phase 8: Evidence Registry (1 hour)

**Objective:** Complete Sheet 7 - Evidence

**Deliverable:** Complete Sheet 7

#### Phase 9: Dashboard Metrics (1 hour)

**Objective:** Complete Sheet 8 - Dashboard

**Deliverable:** Complete Sheet 8

#### Phase 10: Review & Approval (2-3 hours)

**Deliverable:** Approved assessment

---

## Sheet-by-Sheet Completion Guide

### Sheet 1: Utility_Inventory

#### Purpose
Document all privileged utilities present on endpoints.

#### What to Document

- Privileged utility inventory by category
- Endpoint prevalence (where utilities exist)
- Risk classification
- Business justification

#### How to Complete

**Step 1: Identify Privileged Utilities by Category**

**Category 1: System Administration Tools**

- Windows: Registry Editor (regedit), Services (services.msc), Task Manager, Computer Management, Group Policy Editor (gpedit.msc), PowerShell (admin), Command Prompt (admin)
- macOS: Terminal (sudo), System Preferences (privileged), Disk Utility, Activity Monitor
- Linux: sudoedit, visudo, systemctl, service management, package managers (apt, yum with sudo)

**Category 2: Remote Access Tools**

- RDP (Remote Desktop), VNC, SSH, TeamViewer, AnyDesk, LogMeIn, Remote Assistance
- Note: Distinguish authorized (corporate-approved) vs. unauthorized remote access

**Category 3: Debugging & Development Tools**

- Windows: WinDbg, Visual Studio Debugger, Process Explorer, Process Monitor
- macOS: Xcode debugger, lldb
- Linux: gdb, strace, ltrace
- Cross-platform: IDA Pro, Ghidra, OllyDbg

**Category 4: Password & Credential Tools**

- Password reset utilities (built-in OS tools)
- Credential editors
- Hash dumpers (Mimikatz, pwdump - should be prohibited except security team)
- Keychain/credential manager access

**Category 5: Network Analysis Tools**

- Wireshark, tcpdump, tshark
- Nmap, port scanners
- Network protocol analyzers
- Packet injection tools

**Category 6: Security Bypass Tools (HIGH RISK)**

- Anti-malware disablers (tools that stop AV/EDR)
- Audit log editors/clearers (EventLog utilities, log tampering tools)
- Rootkit detectors (GMER, RootkitRevealer - legitimate but powerful)
- Forensic tools (FTK, EnCase - authorized security use only)
- Boot manipulation tools (BCDEdit, bootloaders)

**Step 2: Determine Endpoint Prevalence**

For each utility:

- Which endpoints have it (count and percentage)
- Is it pre-installed (OS default) or added?
- Installation method (built-in, centrally deployed, user-installed)

**Example:**
```
Utility: Registry Editor (regedit.exe)
Endpoints with utility: 847 / 847 Windows endpoints (100%)
Installation: Pre-installed (Windows OS default)
```

**Step 3: Classify by Risk Level**

**Risk Factors:**

- Can bypass security controls? (High)
- Can modify system configuration? (High)
- Can access sensitive data? (Medium/High)
- Can cover tracks (delete logs)? (Critical)
- Commonly used legitimately? (Lower risk if yes)

**Risk Levels:**
```
CRITICAL: Security bypass tools (AV disablers, log editors, rootkits)
HIGH: Remote access (unauthorized), debugging tools, password tools
MEDIUM: System admin tools (Registry, Services), network analyzers
LOW: Standard admin utilities with limited scope
```

**Step 4: Document Business Justification**

For each utility:

- Why needed? (troubleshooting, system administration, development, security analysis)
- Who needs it? (IT admins, developers, security team)
- Frequency of use? (daily, weekly, rarely)
- Alternatives? (can task be done without this tool?)

#### Common Mistakes to Avoid

❌ **Forgetting built-in utilities** - Focusing only on installed tools, missing regedit, Task Manager  
❌ **Not categorizing** - Treating all privileged utilities the same  
❌ **No risk assessment** - Missing that some tools can disable security  
❌ **No prevalence data** - Not knowing which endpoints have which tools  
❌ **Ignoring unauthorized tools** - Remote access tools installed by users  

#### Quality Checklist

- [ ] All privileged utility categories covered
- [ ] Utilities identified per OS type (Windows, macOS, Linux)
- [ ] Endpoint prevalence documented
- [ ] Risk levels assigned with justification
- [ ] Business justification documented
- [ ] Security bypass tools specifically identified
- [ ] Pre-installed vs. added utilities distinguished

---

### Sheet 2: Access_Control

#### Purpose
Document access controls for privileged utilities - who can use them and how access is enforced.

#### What to Document

For each privileged utility:

- Access control mechanism (AppLocker, PAM, sudo, MDM)
- Who has access (RBAC groups, individuals)
- Enforcement verification
- Access testing results

#### How to Complete

**Step 1: Identify Access Control Mechanisms**

**By Operating System:**

**Windows:**

- AppLocker / Windows Defender Application Control (WDAC)
- Group Policy (restrict execution)
- Privileged Access Management (PAM) solution
- User Account Control (UAC)
- Local admin rights removal

**macOS:**

- Gatekeeper
- MDM restrictions (Jamf, Intune)
- Privilege escalation controls
- sudo restrictions

**Linux:**

- sudo configuration (/etc/sudoers)
- SELinux / AppArmor policies
- User/group permissions
- PAM (Pluggable Authentication Modules)

**Mobile:**

- MDM application restrictions
- Enterprise app catalog controls

**Step 2: Document Who Has Access**

**For EACH Utility:**

**Access Granted To:**

- RBAC groups (e.g., "Domain Admins", "IT Operations", "Security Team")
- Specific individuals (if not group-based)
- Count of users with access

**Access Type:**

- Standing access (permanent, ongoing)
- Temporary access (time-limited, expires)
- Emergency/break-glass (for critical incidents)

**Example:**
```
Utility: Registry Editor (regedit.exe)
Access Control: AppLocker allowlist rule
Access Granted To: 

  - RBAC Group: "IT-Admin-Tier1" (12 users)
  - RBAC Group: "IT-Admin-Tier2" (5 users)
  - Emergency Access: "Break-Glass-Admin" (3 accounts)

Total Users: 20 users
Access Type: Standing (Tier1/Tier2), Emergency (Break-Glass)
```

**Step 3: Verify Enforcement**

**For EACH Utility:**

**Test Access Control:**
1. Log in as standard user (non-admin)
2. Attempt to launch privileged utility
3. Expected: Access denied / blocked
4. Actual: Document result

**Test Results:**

- ✅ Pass: Standard user cannot access
- ⚠️ Partial: Can launch but limited functionality
- ❌ Fail: Standard user can access fully

**Step 4: Document Access Control Configuration**

**Configuration Details:**

- AppLocker rule details (allowlist entries, deny rules)
- PAM policy configuration
- sudo rules (/etc/sudoers entries)
- MDM profile settings

**Example AppLocker Rule:**
```
Rule: Allow "IT-Admin-Tier1" to run regedit.exe
Path: %WINDIR%\regedit.exe
Action: Allow
Conditions: User Group = IT-Admin-Tier1 OR IT-Admin-Tier2
Audit: Log all executions
```

**Step 5: Identify Gaps in Access Control**

**Common Gaps:**

- No access control (anyone can use utility)
- Access control not enforced (audit mode only)
- Too many users have access (over-privileged)
- No group-based control (individual grants)
- Inconsistent enforcement (some endpoints yes, some no)

#### Common Mistakes to Avoid

❌ **Assuming UAC is enough** - UAC is bypass-able, not real access control  
❌ **Not testing** - Assuming controls work without verification  
❌ **Ignoring local admin** - Local admins bypass AppLocker  
❌ **No PAM** - Managing privileged access manually  
❌ **Audit mode forever** - AppLocker in audit doesn't block  
❌ **No emergency access** - Break-glass needed for incidents  

#### Quality Checklist

- [ ] Access control mechanism identified per utility
- [ ] RBAC groups documented
- [ ] User counts documented
- [ ] Access control configuration detailed
- [ ] Enforcement verified (testing conducted)
- [ ] Test results documented (pass/fail)
- [ ] Gaps identified (no control, not enforced, over-privileged)
- [ ] Emergency access documented
- [ ] PAM integration (if applicable)

---

### Sheet 3: Approval_Workflow

#### Purpose
Document approval processes for privileged utility access.

#### What to Document

For access requests:

- Approval workflow (who approves, process)
- Recent approval requests (sample)
- Standing vs. temporary access policies
- Recertification process

#### How to Complete

**Step 1: Document Approval Workflow**

**Workflow Components:**

**1. Request Submission:**

- How does user request access? (Ticket, form, PAM self-service)
- What information required? (Business justification, utility needed, duration)

**2. Approval Chain:**

- **Level 1:** Manager approval (business need)
- **Level 2:** Security review (risk assessment)
- **Level 3:** Final approval (IT Director, CISO for high-risk)

**3. Access Grant:**

- How is access provisioned? (AD group add, PAM grant, sudo rule)
- Notification to user
- Documentation of approval

**4. Time Limits:**

- Standing access: Permanent, recertified quarterly/annually
- Temporary access: Time-limited (24 hours, 7 days, 30 days)
- Emergency access: Immediate grant, reviewed retrospectively

**Step 2: Review Recent Approvals**

**Sample Period:** Last 90 days

**For Each Approval:**

- Requestor
- Utility requested
- Business justification
- Approval chain (who approved at each level)
- Access type (standing/temporary/emergency)
- Grant date and expiration (if temporary)

**Metrics:**
```
Total Requests: [X]
Approved: [X] ([%])
Denied: [X] ([%])
Pending: [X]

Average Approval Time: [X] days
Requests by Type:

  - Standing: [X]
  - Temporary: [X]
  - Emergency: [X]

```

**Step 3: Assess Approval Quality**

**Review Criteria:**

**Well-Documented Approval:**

- ✅ Clear business justification
- ✅ Risk assessment documented
- ✅ All approval levels completed
- ✅ Time limit appropriate
- ✅ Recertification date set

**Poorly-Documented Approval:**

- ❌ Vague justification ("Need admin access")
- ❌ No security review
- ❌ Rubber-stamp approvals (approved in 5 minutes)
- ❌ Standing access when temporary appropriate
- ❌ No recertification

**Step 4: Document Recertification Process**

**Recertification:** Periodic review of standing access

**Process:**

- Frequency: Quarterly (high-risk utilities), Annually (standard utilities)
- Owner: Manager + Security
- Review questions:
  - Does user still need access?
  - Is access level appropriate?
  - Any security incidents involving this user?
- Actions: Approve continuation, reduce access, revoke access

**Recent Recertification:**

- Last recertification date
- Number of users recertified
- Access revoked (count and %)
- Access reduced (count and %)

**Step 5: Identify Process Gaps**

**Common Gaps:**

- No approval workflow (ad-hoc grants)
- Incomplete approvals (missing security review)
- No time limits (all access is standing)
- No recertification (access never reviewed)
- Approvals not documented (verbal approvals)

#### Common Mistakes to Avoid

❌ **Ad-hoc approvals** - Email/chat approvals, not tracked  
❌ **Rubber-stamp approvals** - Manager approves everything instantly  
❌ **No security review** - Only manager approves, no risk assessment  
❌ **Standing access by default** - Everything is permanent  
❌ **No recertification** - Access granted forever  
❌ **Emergency access abuse** - "Emergency" used for convenience  

#### Quality Checklist

- [ ] Approval workflow documented
- [ ] Approval levels defined (manager, security, final)
- [ ] Recent approvals reviewed (sample 90 days)
- [ ] Approval quality assessed
- [ ] Time limits documented (standing vs. temporary)
- [ ] Recertification process documented
- [ ] Recent recertification completed
- [ ] Emergency access process defined
- [ ] Gaps identified

---

### Sheet 4: Usage_Monitoring

#### Purpose
Verify privileged utility usage is logged, monitored, and reviewed.

#### What to Document

For each privileged utility:

- Logging configuration
- SIEM integration
- Recent usage (sample period)
- Anomaly detection
- Usage review process

#### How to Complete

**Step 1: Verify Logging Configuration**

**For EACH Utility:**

**Logging Mechanism:**

- Windows Event Logs (Application, Security, System)
- Linux audit logs (auditd)
- PAM session logs
- EDR process execution logs
- SIEM

**What's Logged:**

- User (who executed)
- Timestamp (when)
- Endpoint (where)
- Utility name (what)
- Command-line arguments (how - if applicable)
- Duration (session length for remote access)
- Exit status (success/failure)

**Example:**
```
Utility: Registry Editor (regedit.exe)
Logging: Windows Event Log (Security), EDR Process Execution
SIEM: Forwarded to Splunk
Events Logged:

  - Process creation (Event ID 4688)
  - User: DOMAIN\username
  - Timestamp: 2026-01-25 14:32:15
  - Endpoint: WKS-12345
  - Command: regedit.exe
  - Parent process: explorer.exe

```

**Step 2: Verify SIEM Integration**

**For Critical/High-Risk Utilities:**

**SIEM Requirements:**

- Logs forwarded to SIEM? (Yes/No)
- Forwarding verified? (Check SIEM for recent events)
- Retention period (how long stored)
- Alerting configured? (anomaly detection, unauthorized usage)

**Test SIEM Integration:**
1. Execute privileged utility on test endpoint
2. Wait 5-15 minutes (log forwarding delay)
3. Search SIEM for event
4. Verify event present with all details

**Step 3: Review Recent Usage**

**Sample Period:** Last 30 days

**For Each Utility:**

- Total execution count
- Unique users (who used it)
- Unique endpoints (where used)
- Usage frequency distribution (who's using it most)

**Example:**
```
Utility: Registry Editor
Period: Last 30 days
Total Executions: 147
Unique Users: 8
Unique Endpoints: 23

Top Users:
  1. admin.smith: 52 executions (35%)
  2. admin.jones: 38 executions (26%)
  3. admin.davis: 24 executions (16%)
  
Usage Pattern: Normal (consistent with IT workload)
```

**Step 4: Assess Anomaly Detection**

**Anomalies to Detect:**

- Unusual user (standard user accessing admin tool)
- Unusual time (3 AM execution)
- Unusual frequency (utility run 50 times in 10 minutes)
- Unusual endpoint (admin tool on non-admin workstation)
- Unusual sequence (multiple bypass tools in succession)

**Anomaly Detection:**

- Automated (SIEM rules, UEBA)
- Manual (periodic review)
- Combination

**Recent Anomalies:**

- Count of anomalies detected
- False positive rate
- True positives (actual incidents)
- Response actions taken

**Step 5: Document Usage Review Process**

**Review Frequency:**

- Real-time: SIEM alerts for high-risk utilities
- Daily: SOC review of suspicious activity
- Weekly: Summary report to security management
- Monthly: Detailed usage audit

**Review Responsibilities:**

- SOC: Real-time monitoring, alert triage
- Security Engineering: Weekly/monthly review
- Management: Monthly summary review

**Recent Review:**

- Last review date
- Findings (anomalies, policy violations, incidents)
- Actions taken (investigations, access revoked, training)

#### Common Mistakes to Avoid

❌ **Logging not configured** - Utilities run but not logged  
❌ **Logs not forwarded** - Logged locally but not to SIEM  
❌ **No review process** - Logs collected but never reviewed  
❌ **Alert fatigue** - Too many alerts, all ignored  
❌ **No retention** - Logs deleted after 7 days  
❌ **No anomaly detection** - Only manual review, infrequent  

#### Quality Checklist

- [ ] Logging configured per utility
- [ ] SIEM integration verified
- [ ] Recent usage data collected (30 days)
- [ ] Usage patterns analyzed
- [ ] Anomaly detection configured
- [ ] Recent anomalies documented
- [ ] Usage review process defined
- [ ] Recent review completed
- [ ] Review findings documented
- [ ] Log retention adequate (≥90 days)

---

### Sheet 5: Security_Bypass_Tools

#### Purpose
Specifically identify tools that can disable or bypass security controls - these are CRITICAL risk.

#### What to Document

Tools that can:

- Disable anti-malware/EDR
- Edit or clear audit logs
- Modify security configurations
- Install rootkits or bypass kernel protections
- Dump credentials or passwords

#### How to Complete

**Step 1: Identify Security Bypass Tools**

**Category 1: Anti-Malware Disablers**

- Tools that stop/disable AV/EDR services
- Tamper protection bypass tools
- Service control utilities used maliciously (sc.exe, net.exe)

**Category 2: Audit Log Manipulation**

- Event log editors/clearers (wevtutil, Clear-EventLog)
- Log file deletion tools
- Timestamp modification tools

**Category 3: Credential Access**

- Mimikatz, pwdump, fgdump (password hash dumpers)
- SAM database extractors
- Keyloggers
- Credential editors

**Category 4: Rootkits & Kernel Manipulation**

- Rootkit installers
- Driver signing bypass tools
- Kernel debuggers (if unauthorized)
- Boot manipulation (BCDEdit for malicious purposes)

**Category 5: Forensic Anti-Analysis**

- Anti-forensic tools (data wiping, secure delete)
- Counter-surveillance tools
- Encryption bypass tools

**Step 2: Assess Prevalence and Risk**

**For EACH Security Bypass Tool:**

**Presence:**

- Found on endpoints? (Yes/No, count)
- Authorized use? (Security team only, or prohibited)
- Access controlled? (Who can use)

**Risk Assessment:**
```
CRITICAL: Malicious use can completely compromise security

  - Examples: Mimikatz on non-security endpoints, AV disablers
  
HIGH: Legitimate use exists but very dangerous

  - Examples: Event log clearers (wevtutil), service control for AV services
  
MEDIUM: Can be used maliciously but has legitimate admin uses

  - Examples: BCDEdit, kernel debuggers on authorized admin workstations

```

**Step 3: Document Authorized Use Cases**

**Security Team Use:**

- Penetration testing (Mimikatz, exploitation frameworks)
- Incident response (forensic tools, memory dumpers)
- Security research (rootkit detectors, malware analysis tools)

**Requirements for Authorized Use:**

- Explicitly approved by CISO
- Used only on authorized endpoints (security lab, isolated networks)
- Usage heavily logged and monitored
- Users background-checked and trained
- Session recording (PAM)

**Step 4: Document Controls**

**For Authorized Security Tools:**

- Access restricted to security team only
- Cannot be executed on production endpoints
- PAM-controlled access
- Session recording mandatory
- Usage reviewed after each use

**For Prohibited Tools:**

- Blocklisted (cannot execute)
- Detection via EDR (alert if found)
- Immediate incident response (presence = incident)

**Step 5: Identify Gaps**

**Common Gaps:**

- Security bypass tools on standard endpoints
- No access control (any admin can use Mimikatz)
- No detection (EDR doesn't alert on bypass tools)
- Authorized use not restricted (security tools on production)
- No session recording (can't audit what was done)

#### Common Mistakes to Avoid

❌ **Allowing Mimikatz anywhere** - Should be isolated to security lab  
❌ **No detection** - Bypass tools present but not detected  
❌ **Service control unrestricted** - sc.exe, net.exe can disable AV  
❌ **Event log clearing allowed** - wevtutil should be restricted  
❌ **No session recording** - Can't prove what security team did  

#### Quality Checklist

- [ ] Security bypass tools identified
- [ ] Presence assessed (where found)
- [ ] Risk levels assigned
- [ ] Authorized use cases documented
- [ ] Authorization requirements defined
- [ ] Controls documented (access, monitoring, recording)
- [ ] Prohibited tools blocklisted
- [ ] Detection configured (EDR alerts)
- [ ] Gaps identified

---

### Sheet 6: Privileged_Utility_Gaps

#### Purpose
Consolidate all gaps in privileged utility controls.

#### Gap Categories

1. No Access Control
2. Access Control Not Enforced
3. Over-Privileged Access
4. No Approval Workflow
5. No Usage Monitoring
6. No Recertification
7. Security Bypass Tools Present

#### How to Complete

Similar to S3 and S4 gap sheets. Consolidate gaps from Sheets 1-5, assign risk, develop remediation plans.

---

### Sheet 7: Evidence_Register

#### Purpose
Evidence repository for audit.

#### Evidence Categories

- Privileged utility inventory
- Access control configurations
- Approval workflow records
- Usage logs and SIEM screenshots
- Recertification records
- Security bypass tool assessments

---

### Sheet 8: Privileged_Utility_Dashboard

#### Purpose
Executive summary dashboard.

#### What to Document

**Summary Metrics:**

- Total privileged utilities
- Access control deployment %
- Utilities with logging/monitoring
- Approval workflow compliance
- Recertification compliance
- Security bypass tools (count and control status)
- Critical gaps

**Thresholds:**

**Green:**

- Access control deployed ≥95%
- Logging/monitoring ≥95%
- Approval workflow 100%
- Recertification current (≤90 days)
- No uncontrolled security bypass tools

**Yellow:**

- Access control 85-94%
- Logging/monitoring 85-94%
- Approval workflow ≥90%
- Recertification 90-180 days
- Security bypass tools controlled but present

**Red:**

- Access control <85%
- Logging/monitoring <85%
- Approval workflow <90%
- Recertification >180 days
- Uncontrolled security bypass tools

---

### Sheet 9: MFA_Compliance

#### Purpose
Track multi-factor authentication (MFA) compliance for privileged accounts and sensitive utilities.

#### What to Document

**MFA Status:**

- Utility or privileged function
- MFA required (Yes/No)
- MFA enabled (Yes/No)
- MFA method (TOTP/Hardware/Push/SMS)
- Endpoints with enforcement
- Endpoints without enforcement
- Compliance %

**Risk Assessment:**

- Utilities with high-risk access
- Accounts without MFA
- MFA bypass capabilities
- Approved MFA exceptions

#### How to Complete

**Step 1: Identify High-Risk Utilities Requiring MFA**

- Remote access tools: [tool names]
- Privileged utility access: [tool names]
- Administrative functions: [descriptions]
- Database access: [systems]
- Network device access: [devices]

**Step 2: Verify MFA Deployment**

For each high-risk utility:

- MFA deployed? Yes/No
- MFA method: [TOTP/Hardware/Push/SMS]
- Enforcement point: [Where MFA is verified]
- Endpoints affected: [count]
- MFA compliance: [X%]

**Step 3: Identify Gaps**

- Utilities without MFA: [list]
- Endpoints with access but no MFA: [count]
- Approved exceptions: [list with justification]
- Remediation timeline: [date]

**Step 4: Assess MFA Bypass Risk**

- Method: [How could MFA be bypassed]
- Risk level: Critical/High/Medium/Low
- Mitigation: [Control or acceptance]

#### Common Mistakes to Avoid

❌ MFA not enforced at access point
❌ MFA bypass methods not assessed
❌ Too many approved exceptions
❌ MFA method not recovery-resistant
❌ No account recovery if MFA device lost

#### Quality Checklist

- [ ] High-risk utilities identified
- [ ] MFA status documented
- [ ] Enforcement verified
- [ ] Bypass risks assessed
- [ ] Exceptions justified
- [ ] Recovery procedures defined

---

### Sheet 10: Quarterly_Reviews

#### Purpose
Track quarterly access reviews and recertification activities for privileged utilities.

#### What to Document

**Review Schedule:**

- Review period: [Quarter date]
- Target completion date: [date]
- Actual completion date: [date]
- Reviewers: [names/teams]

**Access Certifications:**

- Total privileged accounts: [count]
- Accounts reviewed: [count] ([%])
- Accounts approved: [count]
- Accounts requested removal: [count]
- Accounts awaiting decision: [count]
- Review completion status: [%]

**Changes from Review:**

- Access added: [count]
- Access removed: [count]
- Access modified: [count]
- Access exceptions approved: [count]

#### How to Complete

**Step 1: Plan Quarterly Review**

- Review period: Q[1-4] 20[XX]
- Target completion: [date - typically 30 days after quarter end]
- Reviewers assigned: [list]
- Approval authority: [title]
- Scope: All privileged accounts

**Step 2: Execute Access Review**

For each active privileged account:

- Owner/reviewer: [name]
- Account holder: [user]
- Utility/role accessed: [description]
- Business justification: [current need]
- Certification: Approved/Remove/Modify

**Step 3: Process Review Results**

- Accounts approved to continue: [count]
- Accounts approved for removal: [count]
  - Removal date: [date]
  - Verification of removal: [how verified]
- Accounts requiring modification: [count]
  - Change needed: [description]
  - Modification date: [date]

**Step 4: Track Exceptions**

- Exception to review process: [description]
- Exception approver: [title]
- Exception end date: [date]
- Risk rating: Critical/High/Medium/Low

**Step 5: Document Review Completion**

- All accounts reviewed: Yes/No
- Review completion date: [date]
- Reviewer sign-off: [name/date]
- Approval authority sign-off: [name/date]
- Findings summary: [key results]

**Step 6: Plan Next Review**

- Lessons learned: [notes]
- Process improvements: [suggested changes]
- Next review period: [date]

#### Common Mistakes to Avoid

❌ Review process bypassed
❌ Accounts approved without verification
❌ Review lag (not completed within 30-45 days)
❌ No removal of unneeded access
❌ No documented justification
❌ No management sign-off

#### Quality Checklist

- [ ] Review period clearly defined
- [ ] All accounts included in scope
- [ ] Reviewers assigned and trained
- [ ] All accounts reviewed by deadline
- [ ] All decisions documented
- [ ] Approved changes implemented
- [ ] Removed access verified
- [ ] Management approval obtained
- [ ] Results communicated to stakeholders

---

## Evidence Collection

### Required Evidence Types

1. **Utility Inventory** - List of privileged utilities, prevalence
2. **Access Control** - AppLocker policies, PAM configurations, sudo rules
3. **Approvals** - Recent approval requests, approval workflow documentation
4. **Usage Logs** - SIEM screenshots, event log exports, usage reports
5. **Recertification** - Recertification records, access reviews
6. **Security Bypass** - Detection configurations, authorized use approvals

---

## Common Pitfalls

### Pitfall 1: Assuming UAC is Access Control

**Mistake:** "We have UAC enabled, privileged utilities are controlled"

**Why It Fails:** UAC is a prompt, not a control. Users with local admin bypass UAC easily.

**How to Avoid:** Use AppLocker, PAM, or true RBAC. Test with standard user.

### Pitfall 2: No Privileged Utility Inventory

**Mistake:** "We control admin access" but don't know what tools exist

**Why It Fails:** Can't control what you don't inventory

**How to Avoid:** Complete inventory (Sheet 1) before implementing controls

### Pitfall 3: Logging but Not Monitoring

**Mistake:** Usage logged but logs never reviewed

**Why It Fails:** Logging without review = no visibility

**How to Avoid:** Define review process, assign responsibility, track completion

### Pitfall 4: Standing Access for Everything

**Mistake:** All privileged access is permanent

**Why It Fails:** Accounts compromised = persistent privileged access

**How to Avoid:** Just-in-time access for high-risk utilities, temporary grants

### Pitfall 5: No Recertification

**Mistake:** Access granted 3 years ago, never reviewed

**Why It Fails:** Users change roles, leave company, access remains

**How to Avoid:** Quarterly/annual recertification with active revocation

### Pitfall 6: Security Bypass Tools Uncontrolled

**Mistake:** Mimikatz on production endpoints, no controls

**Why It Fails:** One compromised admin = lateral movement

**How to Avoid:** Isolate security tools to lab, PAM control, session recording

### Pitfall 7: No Testing

**Mistake:** Assuming controls work without verification

**Why It Fails:** Controls may be misconfigured or not applied

**How to Avoid:** Test access control (standard user attempt), verify blocking

### Pitfall 8: Audit Mode Forever

**Mistake:** AppLocker in audit mode for years

**Why It Fails:** Audit doesn't block, only logs

**How to Avoid:** Enforce mode after pilot period

### Pitfall 9: Emergency Access Abuse

**Mistake:** Break-glass accounts used daily for convenience

**Why It Fails:** Defeats purpose of emergency access

**How to Avoid:** Monitor emergency access usage, require justification, review

### Pitfall 10: Ignoring Built-In Tools

**Mistake:** Controlling installed tools, ignoring regedit, Task Manager

**Why It Fails:** Built-in tools are powerful, accessible to all admins

**How to Avoid:** Inventory includes built-in utilities, controls apply equally

---

## Quality Checklist

### Completeness (10 items)

- [ ] All sheets completed
- [ ] Privileged utility inventory comprehensive
- [ ] Access controls assessed
- [ ] Approval workflow documented
- [ ] Usage monitoring verified
- [ ] Security bypass tools identified
- [ ] Gaps consolidated
- [ ] Evidence registered
- [ ] Dashboard calculated

### Accuracy (10 items)

- [ ] Utility categorization correct
- [ ] Risk levels justified
- [ ] Access control mechanisms verified
- [ ] RBAC groups accurate
- [ ] Logging verified in SIEM
- [ ] Usage data current (≤30 days)
- [ ] Approval records authentic
- [ ] Recertification dates accurate
- [ ] Test results documented
- [ ] Metrics calculated correctly

### Honesty (6 items)

- [ ] Access control status accurate (not aspirational)
- [ ] Gaps documented honestly
- [ ] Over-privileged access admitted
- [ ] Security bypass tools not hidden
- [ ] Enforcement mode accurate (audit vs enforce)
- [ ] Recertification compliance honest

### Evidence (5 items)

- [ ] Access control configs
- [ ] Usage logs / SIEM screenshots
- [ ] Approval records
- [ ] Recertification evidence
- [ ] All evidence sanitized

### Remediation (5 items)

- [ ] All gaps have plans
- [ ] Plans specific
- [ ] Owners assigned
- [ ] Dates realistic
- [ ] Priority assigned

### Integration (4 items)

- [ ] PAM integrated (if deployed)
- [ ] SIEM integrated
- [ ] Identity management integrated
- [ ] EDR integrated

### Stakeholder Input (4 items)

- [ ] PAM team reviewed
- [ ] SOC reviewed
- [ ] Sysadmins reviewed
- [ ] Management reviewed

### Consistency (3 items)

- [ ] No contradictions
- [ ] Access control status matches tests
- [ ] Dashboard matches details

---

## Review & Approval

### Three-Level Approval Process

#### Level 1: Technical Review

**Reviewer:** PAM Lead or Senior System Administrator

**Focus:**

- Utility inventory completeness
- Access control accuracy
- Usage monitoring verification

**Checklist:**

- [ ] Privileged utilities identified
- [ ] Access controls verified
- [ ] Logging confirmed
- [ ] Technical evidence present

**Outcome:** Approve → Level 2 / Request Changes

#### Level 2: Compliance Review

**Reviewer:** Information Security Manager

**Focus:**

- Policy compliance
- Risk assessments
- Evidence quality

**Checklist:**

- [ ] All requirements addressed
- [ ] Risk levels justified
- [ ] Gaps documented
- [ ] Evidence audit-ready

**Outcome:** Approve → Level 3 / Request Changes

#### Level 3: Management Approval

**Reviewer:** CISO or IT Director

**Focus:**

- Strategic alignment
- Resource allocation
- Risk acceptance

**Checklist:**

- [ ] Gap priorities acceptable
- [ ] Remediation funded
- [ ] Accepted risks documented
- [ ] Timelines realistic

**Outcome:** Approve / Request Changes / Escalate

### Post-Approval Actions

1. Lock assessment
2. Store in ISMS repository
3. Notify auditors
4. Begin remediation
5. Schedule quarterly reassessment

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
