# ISMS-IMP-A.8.1-7-18-19-S4 - Software Control Process
## Practical Implementation Guidance for Software Installation Controls
### ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19

---

## Document Control

| **Attribute** | **Details** |
|---------------|-------------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S4 |
| **Document Title** | Software Control Process |
| **Version** | 1.0 |
| **Date** | [Date] |
| **Classification** | Internal |
| **Document Owner** | IT Operations Manager / ISMS Implementation Lead |
| **Status** | Active |
| **Review Cycle** | Annual (or when software control requirements change) |
| **Parent Document** | ISMS-POL-A.8.1-7-18-19 (Endpoint Security Framework) |
| **Related Documents** | ISMS-POL-A.8.1-7-18-19-S5 (Software Installation Requirements - A.8.19)<br>ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process)<br>ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment)<br>ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment)<br>ISMS-IMP-A.8.8 (Vulnerability Management Process) |

---

## 1. Purpose and Scope

### 1.1 Purpose

This document provides **practical, step-by-step guidance** for implementing software installation controls to implement **Control A.8.19 (Installation of Software on Operational Systems)** requirements.

**Software control implementation** involves:
- Developing and maintaining an approved software list (whitelist)
- Implementing software approval workflow (request → security review → approval)
- Deploying application control technologies (AppLocker, Gatekeeper, etc.)
- Collecting software inventory from all endpoints
- Detecting and remediating unauthorized software
- Integrating with change management processes
- Managing software vulnerabilities and end-of-life software

### 1.2 Scope

This guidance covers implementation for:

- **Windows Endpoints**: AppLocker, Windows Defender Application Control (WDAC), Software Restriction Policies
- **macOS Endpoints**: Gatekeeper, application restrictions via MDM
- **Linux Endpoints**: AppArmor, SELinux, package manager restrictions
- **Mobile Devices**: MDM app management (approved app lists, installation restrictions)
- **BYOD Devices**: Containerized app management (MAM), privacy-respecting controls

### 1.3 Applicability

This guidance is **technology-agnostic** while providing specific examples for common platforms. Implementers should adapt procedures to their environment and chosen tools.

**Key Principle**: The goal is to prevent unauthorized software installation while maintaining user productivity and respecting privacy (especially BYOD).

### 1.4 Who Should Use This Guidance

- IT operations teams implementing software controls
- Endpoint administrators deploying application control
- Security teams enforcing software policies
- Change managers integrating software installation with change control
- ISMS implementers preparing for A.8.19 assessments

---

## 2. Process Overview

### 2.1 Software Control Workflow

```
┌────────────────────────────────────────────────────────────────────┐
│              SOFTWARE CONTROL IMPLEMENTATION PROCESS               │
└────────────────────────────────────────────────────────────────────┘

Phase 1: Initial Software Inventory
├─ Collect current software inventory from all endpoints
├─ Analyze installed software (what users currently use)
├─ Identify business-critical software
├─ Categorize by business purpose and risk level
└─ Document initial baseline

Phase 2: Approved Software List Development
├─ Define software categories (universal, role-based, exceptions)
├─ Conduct security reviews for all software
├─ Create initial approved software list
├─ Obtain stakeholder approval (IT Ops, Security, Business)
└─ Publish approved software list

Phase 3: Software Approval Workflow Setup
├─ Design approval workflow (request → review → approval)
├─ Create software request form template
├─ Define approval authorities (IT Manager, Security Manager, CISO)
├─ Configure ticketing system workflow
├─ Document approval process
└─ Train staff on approval process

Phase 4: Application Control Deployment
├─ Select application control technology per platform
├─ Develop application control policies (allowlist rules)
├─ Deploy in audit mode (log violations, don't block) - initial phase
├─ Monitor and refine policies (reduce false positives)
├─ Switch to enforcement mode (block violations)
└─ Ongoing policy maintenance

Phase 5: Software Inventory Automation
├─ Configure endpoint management tools for inventory collection
├─ Schedule automated inventory (daily or weekly)
├─ Normalize inventory data (standardize software names/versions)
├─ Export inventory for analysis
└─ Track inventory trends

Phase 6: Unauthorized Software Detection
├─ Compare inventory to approved software list
├─ Identify unauthorized software (in inventory but not approved)
├─ Classify by risk (high-risk, medium-risk, low-risk)
├─ Generate unauthorized software report
├─ Notify users and remediate
└─ Track remediation progress

Phase 7: Change Control Integration
├─ Software installations require change requests (RFCs)
├─ Link software approvals to change control
├─ Track deployment through change management
└─ Post-implementation verification

Phase 8: Continuous Monitoring and Improvement
├─ Daily unauthorized software scans
├─ Weekly application control policy review
├─ Monthly metrics reporting (unauthorized software rate, remediation time)
├─ Quarterly approved software list review
└─ Annual process effectiveness review
```

### 2.2 Key Principles

- **Least Privilege**: Users should only have access to software needed for their role
- **Defense in Depth**: Multiple layers (approved list + application control + malware protection)
- **User Productivity Balance**: Controls should not excessively hinder legitimate work
- **Privacy Protection**: BYOD controls respect personal device privacy
- **Continuous Validation**: Regular scans detect unauthorized software, prompt remediation
- **Documented Exceptions**: All deviations from policy must be justified and approved

---

## 3. Prerequisites and Tools

### 3.1 Required Access and Permissions

**Endpoint Management Tools**:
- **Administrative access** to MDM/SCCM/Jamf (for inventory and policy deployment)
- **Application control policy management** permissions
- **Software inventory export** permissions

**Approval Workflow**:
- **Ticketing system** access (for software request workflow)
- **Approval authority** designation (who can approve software?)

**Change Management**:
- **Change request creation** permissions
- **Change Advisory Board (CAB)** membership or liaison

### 3.2 Software Inventory Tools

| Tool | Platform | Purpose | Type |
|------|----------|---------|------|
| **Microsoft Intune** | Windows, macOS, iOS, Android | Cloud-based inventory, MDM | Cloud Service |
| **SCCM (Endpoint Manager)** | Windows, macOS | On-premises inventory, deployment | Microsoft |
| **Jamf Pro** | macOS, iOS | Apple device management | Commercial |
| **Lansweeper** | Windows, macOS, Linux | Network-wide inventory scanning | Commercial |
| **GLPI** | Windows, macOS, Linux | Open-source IT asset management | Open-source |
| **Osquery** | Windows, macOS, Linux | SQL-based endpoint queries | Open-source |

### 3.3 Application Control Technologies

| Technology | Platform | Capabilities | Type |
|------------|----------|--------------|------|
| **AppLocker** | Windows 10/11, Server 2016+ | File-based allowlist/denylist, publisher rules | Built-in |
| **Windows Defender Application Control (WDAC)** | Windows 10/11 | Code integrity policies, stronger than AppLocker | Built-in |
| **Gatekeeper** | macOS | Code signing verification, notarization | Built-in |
| **MDM Restrictions** | macOS, iOS, Android | App installation restrictions via MDM | Built-in (MDM) |
| **AppArmor** | Linux (Ubuntu, Debian, SUSE) | Mandatory Access Control (MAC) | Built-in |
| **SELinux** | Linux (RHEL, CentOS, Fedora) | Security-Enhanced Linux, MAC | Built-in |

### 3.4 Software Approval Workflow Tools

**Options**:
- **ServiceNow**: Enterprise ITSM platform with workflow automation
- **Jira Service Management**: IT service desk with customizable workflows
- **SharePoint + Power Automate**: Microsoft ecosystem workflow automation
- **Custom Web Form + Email**: Simple approval workflow for small organizations

**Minimum Requirements**:
- Request submission capability
- Routing to appropriate approvers
- Approval tracking (audit trail)
- Notification to requester

---

## 4. Initial Software Inventory Collection

### 4.1 Purpose of Initial Inventory

**Before implementing controls**, understand current state:
- What software is currently installed across all endpoints?
- Which software is business-critical (must be approved)?
- Which software is unauthorized or unnecessary (candidates for removal)?

**Initial Inventory Informs**:
- Approved software list development (commonly used software = likely approved)
- Application control policy design (existing software needs allowlist rules)
- User communication (users need to know which software will be restricted)

### 4.2 Automated Inventory Collection

**Using Microsoft Intune**:

1. **Navigate to Intune Portal**: https://endpoint.microsoft.com
2. **Apps → Discovered apps** (or **Devices → All devices → [Device] → Discovered apps**)
3. **Export** inventory:
   - Click **Export** → Downloads CSV file
   - Columns: Application name, Version, Publisher, Device count

4. **Data Analysis**:
   - Load CSV into Excel or database
   - Aggregate: `SELECT Application, COUNT(DISTINCT Device) as DeviceCount FROM Inventory GROUP BY Application ORDER BY DeviceCount DESC`
   - Identify top applications (most widely deployed = business-critical)

**Using SCCM**:

1. **SCCM Console → Assets and Compliance → Overview → Devices**
2. **Reports → Software → Software Inventory**
3. Select report: **"All software titles"** or **"Installed software for a specific collection"**
4. Run report, export to CSV

5. **Data Extraction via SQL** (direct database query):
   ```sql
   SELECT DISTINCT 
       v_GS_INSTALLED_SOFTWARE.ProductName0 AS Software,
       v_GS_INSTALLED_SOFTWARE.Publisher0 AS Publisher,
       COUNT(DISTINCT v_GS_INSTALLED_SOFTWARE.ResourceID) AS DeviceCount
   FROM v_GS_INSTALLED_SOFTWARE
   GROUP BY v_GS_INSTALLED_SOFTWARE.ProductName0, v_GS_INSTALLED_SOFTWARE.Publisher0
   ORDER BY DeviceCount DESC;
   ```

**Using Jamf Pro** (macOS):

1. **Jamf Pro Console → Computers → Search Inventory**
2. **Advanced → Add Criteria → Applications**
3. Run search, export results
4. Alternatively: **Reports → Computer Reports → Application Usage** → Export

**Using Lansweeper**:

1. **Lansweeper Console → Reports → Software**
2. Select: **"Software: Installed software"**
3. Export to Excel
4. Aggregate by software name (Lansweeper may have duplicates due to version variations)

**Using PowerShell** (Windows, ad-hoc):

```powershell
# Collect installed software from local machine
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Where-Object {$_.DisplayName -ne $null} |
    Sort-Object DisplayName |
    Export-Csv -Path "C:\Temp\InstalledSoftware.csv" -NoTypeInformation

# Collect from remote machines (requires WinRM)
Invoke-Command -ComputerName (Get-Content C:\Temp\computers.txt) -ScriptBlock {
    Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
        Select-Object PSComputerName, DisplayName, DisplayVersion, Publisher
} | Export-Csv -Path "C:\Temp\NetworkInstalledSoftware.csv" -NoTypeInformation
```

**Using Osquery** (Linux/macOS):

```bash
# List installed packages (Debian/Ubuntu)
osqueryi "SELECT name, version, source FROM deb_packages;"

# List installed packages (RHEL/CentOS)
osqueryi "SELECT name, version, vendor FROM rpm_packages;"

# macOS applications
osqueryi "SELECT name, bundle_identifier, bundle_version FROM apps;"
```

### 4.3 Data Normalization

**Problem**: Software inventory from different sources uses inconsistent naming:
- "Microsoft Office Professional Plus 2021" vs. "Microsoft Office 2021" vs. "Office 2021"
- "Google Chrome" vs. "Chrome" vs. "Google Chrome Browser"

**Solution**: Normalize software names for analysis.

**Normalization Process**:

1. **Export raw inventory** to CSV
2. **Remove version numbers** from software names (for grouping):
   ```python
   # Python script example
   import pandas as pd
   import re
   
   df = pd.read_csv('raw_inventory.csv')
   
   # Remove version numbers (digits and dots)
   df['SoftwareNormalized'] = df['Software'].apply(
       lambda x: re.sub(r'\d+(\.\d+)*', '', x).strip()
   )
   
   # Remove common suffixes
   df['SoftwareNormalized'] = df['SoftwareNormalized'].str.replace(' (x64)', '', regex=False)
   df['SoftwareNormalized'] = df['SoftwareNormalized'].str.replace(' (x86)', '', regex=False)
   
   # Group and count
   summary = df.groupby('SoftwareNormalized').agg({
       'Device': 'nunique',
       'Software': 'first'  # Keep original name as example
   }).reset_index()
   
   summary.columns = ['Software (Normalized)', 'Device Count', 'Example Original']
   summary = summary.sort_values('Device Count', ascending=False)
   
   summary.to_csv('normalized_inventory.csv', index=False)
   ```

3. **Manual Review**: Some names still need manual correction (e.g., "Adobe Acrobat" vs. "Adobe Reader" → both are PDF readers, similar purpose)

### 4.4 Categorization and Analysis

**Step 1: Identify Top Applications** (by device count)

Most widely deployed software is likely business-critical:
- Microsoft Office: 2,200 devices (98% of endpoints) → **Universal Approval**
- Google Chrome: 2,100 devices (94%) → **Universal Approval**
- Zoom: 1,800 devices (81%) → **Universal Approval**
- Adobe Acrobat Reader: 1,500 devices (67%) → **Universal Approval**
- VPN Client: 1,400 devices (63%) → **Universal Approval** (corporate VPN)
- Visual Studio Code: 250 devices (11%) → **Role-Based Approval** (Developers)
- AutoCAD: 50 devices (2%) → **Role-Based Approval** (Engineers)
- WinRAR: 30 devices (1.3%) → **Review** (Do we need this? 7-Zip alternative?)

**Step 2: Identify Unauthorized/Unnecessary Software**

Software with low deployment or security concerns:
- Potentially Unwanted Programs (PUPs): Toolbars, adware, browser hijackers
- Pirated software: Unlicensed applications (legal and security risk)
- Personal software: Games, media players (non-business purpose)
- Outdated software: Deprecated versions with security vulnerabilities

**Example Findings**:
- "PC Optimizer Pro": 5 devices → **Unauthorized** (PUP, remove)
- "KMSPico": 2 devices → **Unauthorized** (piracy tool, remove + investigate)
- "Candy Crush": 15 devices → **Unauthorized** (personal software, remove)
- "Java Runtime Environment 1.8.0_151": 20 devices → **Unauthorized** (outdated, vulnerable, update or remove)

**Step 3: Categorize by Business Purpose**

| Category | Examples | Count | Action |
|----------|----------|-------|--------|
| **Productivity** | Office, PDF Reader, Notepad++ | 10 | Approve (universal) |
| **Communication** | Outlook, Teams, Zoom, Slack | 5 | Approve (universal) |
| **Development** | Visual Studio, Git, Docker | 8 | Approve (role-based: Developers) |
| **Security** | VPN Client, Anti-malware, MFA app | 4 | Approve (universal) |
| **Creative** | Adobe Creative Suite, AutoCAD | 3 | Approve (role-based: Designers, Engineers) |
| **Unauthorized** | Games, PUPs, pirated software | 15 | Remove |

### 4.5 Stakeholder Communication

**Before finalizing approved list**, communicate with stakeholders:

**Email to Department Managers**:
```
Subject: Software Standardization - Review Attached List

Dear Managers,

As part of our endpoint security initiative, we are implementing software installation 
controls. Attached is a draft list of approved software based on current usage.

Please review and provide feedback by [Date]:
- Are there critical tools missing for your team?
- Are there software alternatives you'd prefer?
- Are there unnecessary items we should remove?

Software not on the approved list will require individual approval. Users will be 
notified before any software is restricted.

Questions? Contact IT Operations.

Attachment: Approved_Software_Draft.xlsx
```

**Incorporate Feedback** → Finalize approved software list.

---

## 5. Approved Software List Development

### 5.1 Create Approved Software List Structure

**Recommended Format**: Excel workbook or database table

**Columns**:
- **Software Name**: Standardized name (e.g., "Microsoft Office 365")
- **Publisher**: Vendor name (e.g., "Microsoft Corporation")
- **Approved Versions**: Specific versions or "Latest" (e.g., "2021, 2024" or "Latest")
- **Category**: Universal, Role-Based, Exception
- **Business Purpose**: Productivity, Communication, Development, etc.
- **Risk Level**: High, Medium, Low (from POL-S5 Section 2.2)
- **Approval Date**: Date approved
- **Approved By**: IT Operations Manager, Security Manager (names or roles)
- **Review Date**: Next review date (quarterly)
- **Applicable Roles**: If role-based, which roles? (e.g., "Developers, IT Staff")
- **License Info**: License type (per-user, per-device, site license), count available
- **Notes**: Special considerations (e.g., "Requires admin approval for installation")

**Example Entries**:

| Software Name | Publisher | Approved Versions | Category | Business Purpose | Risk Level | Approval Date | Approved By | Review Date | Applicable Roles | Notes |
|---------------|-----------|-------------------|----------|------------------|------------|---------------|-------------|-------------|------------------|-------|
| Microsoft Office 365 | Microsoft | 2021, 2024 | Universal | Productivity | Medium | 2026-01-11 | IT Manager | 2026-04-11 | All Users | Auto-update enabled |
| Google Chrome | Google | Latest | Universal | Web Browser | High | 2026-01-11 | Security Manager | 2026-04-11 | All Users | Auto-update required |
| Visual Studio Code | Microsoft | Latest | Role-Based | Development | Medium | 2026-01-11 | IT Manager | 2026-04-11 | Developers, IT Staff | Extensions require review |
| AutoCAD 2024 | Autodesk | 2024 | Role-Based | Creative | Medium | 2026-01-11 | IT Manager | 2026-04-11 | Engineers, Designers | 50 licenses available |

### 5.2 Risk Classification Criteria

**From POL-S5 Section 2.2**, classify software by risk:

**High Risk** (Requires Security Manager + IT Ops Manager approval):
- Internet-facing applications (web browsers, email clients, chat apps)
- Applications processing untrusted data (PDF readers, media players)
- Applications requiring admin privileges (system utilities, installers)
- Applications with frequent CVEs (Adobe Flash historically, Java JRE)

**Medium Risk** (Requires IT Ops Manager approval):
- Business applications with local processing (Office, CAD, development tools)
- Applications with network access but limited attack surface
- Standard productivity tools

**Low Risk** (Automated approval for pre-approved list):
- No network access applications (calculators, basic utilities)
- OS components and drivers (from trusted vendors)
- Minimal privilege requirements

**Example Risk Assessments**:
- **Google Chrome**: High (internet-facing, processes untrusted web content, frequent updates due to vulnerabilities)
- **Microsoft Word**: Medium (processes documents, macro risks, but primarily local processing)
- **Windows Calculator**: Low (no network, no data processing, minimal privileges)

### 5.3 Version Management Strategy

**Options for Version Approval**:

**Option 1: Specific Versions Only**
- Example: "Adobe Acrobat Reader DC 2023.008.20421, 2024.001.20642"
- **Pros**: Tight control, known tested versions
- **Cons**: High maintenance (approve each new version)

**Option 2: Latest Version (Auto-Approve Updates)**
- Example: "Google Chrome: Latest"
- **Pros**: Low maintenance, automatic security updates
- **Cons**: Less control, untested versions may introduce issues

**Option 3: Version Range**
- Example: "Microsoft Office 2021, 2024" (major versions, auto-approve minor updates)
- **Pros**: Balance of control and flexibility
- **Cons**: Requires periodic major version approval

**Recommendation**:
- **Security-critical software** (browsers, anti-malware): Latest (auto-update)
- **Productivity software** (Office, business apps): Version range (major versions)
- **Specialty software** (CAD, development tools): Specific versions (test before approval)

### 5.4 License Tracking Integration

**Why Track Licenses in Approved List**:
- Prevent over-deployment (license compliance)
- Cost management (know license utilization)
- Renewal planning (track expiring licenses)

**License Information to Track**:
- License type: Per-user, per-device, concurrent, site license
- Total licenses owned
- Licenses currently deployed (from inventory)
- Available licenses (owned - deployed)
- License expiration date
- Cost per license (for budgeting)

**Example**:
- Software: AutoCAD 2024
- License Type: Per-device
- Licenses Owned: 50
- Licenses Deployed: 48 (from inventory)
- Available: 2
- Expiration: 2027-01-15
- Cost: $1,800/license/year
- **Action**: Alert when deployed approaches owned (48/50 = 96% utilized)

**Integration with SAM (Software Asset Management)** tools:
- ServiceNow SAM, Flexera, Snow License Manager
- Sync approved list with SAM tool for compliance tracking

### 5.5 Approval and Publication

**Step 1: Draft Approved Software List**

Create Excel file: `Approved_Software_List_v1.0.xlsx`
- Include all columns defined in Section 5.1
- Populate with software identified in initial inventory + stakeholder feedback

**Step 2: Approval Workflow**

Submit for approval:
1. **IT Operations Manager** (first approver):
   - Reviews for operational feasibility (supportability, compatibility)
   - Approves operational readiness
2. **Security Manager** (second approver):
   - Reviews risk classifications
   - Approves security posture
3. **CISO** (final approver for high-risk or organization-wide impact):
   - Reviews overall strategy
   - Approves for publication

**Document Approvals**: Add signature/approval records to document control section.

**Step 3: Publish Approved Software List**

Make list accessible to relevant stakeholders:
- **Internal SharePoint/Intranet**: Publish read-only version
- **IT Service Desk**: Provide copy for reference during user requests
- **Endpoint Administrators**: Access to list for application control policy creation

**User Communication**:
```
Subject: Approved Software List Published

Dear Team,

Our approved software list is now available on the intranet:
[Link to SharePoint/Intranet page]

This list includes all software permitted on [Organization] endpoints. If you need 
software not on this list, please submit a software request via the IT Service Desk.

Questions? Contact IT Operations.
```

---

## 6. Software Approval Workflow Implementation

### 6.1 Define Approval Workflow

**Workflow Diagram**:

```
User submits software request (IT Service Desk ticket)
    ↓
IT Service Desk logs request → Assigns to IT Operations
    ↓
IT Operations: Initial Review
    ├─ Already approved? → Route to Change Management (for deployment)
    ├─ Clearly inappropriate? → Reject with explanation
    └─ New software? → Continue to Security Review
         ↓
Security Review (Security Manager or delegate)
    ├─ Security assessment (vendor reputation, vulnerability history, privacy)
    ├─ Risk classification (High, Medium, Low)
    └─ Recommendation (Approve, Approve with conditions, Reject)
         ↓
IT Operations Review
    ├─ Compatibility testing (install in test environment)
    ├─ Performance impact assessment
    ├─ Support capability review (can we support this?)
    └─ Licensing review (cost, license availability)
         ↓
Approval Decision
    ├─ Low/Medium risk + IT Ops + Security approve → Approved
    ├─ High risk → Requires CISO approval
    ├─ Conditions not met → Conditional approval (requester addresses conditions)
    └─ Rejected → Notify requester with reason, suggest alternatives
         ↓
Approved → Add to Approved Software List → Route to Deployment (Change Management)
```

**Approval Authorities** (from POL-S5 Section 3.1):
- **IT Operations Manager**: All software (operational approval)
- **Security Manager**: High-risk software (security approval)
- **CISO**: Exception-based approvals, high-risk with significant organizational impact

**SLA**: 
- Standard requests (low/medium risk): 5 business days
- High-risk or complex requests: 10 business days
- Urgent requests (business-critical): 2 business days (requires justification)

### 6.2 Create Software Request Form

**Minimum Information Required**:

1. **Requester Information**:
   - Name, email, department, role
   - Manager name (for approval)

2. **Software Details**:
   - Software name and publisher
   - Version (specific or latest)
   - Download URL or source
   - Business justification (why do you need this?)
   - How many users need this? (1 person, department, organization-wide)
   - Urgency (standard, urgent - with justification)

3. **Technical Details** (optional, helpful for review):
   - OS compatibility (Windows, macOS, Linux)
   - Licensing (free, paid, trial)
   - Network requirements (internet access, specific ports)
   - Admin privileges required (yes/no)

4. **Alternatives Considered**:
   - Have you checked if approved software meets your needs?
   - Alternatives considered (if any)

**Form Implementation Options**:

**Option 1: IT Service Desk Ticket** (e.g., ServiceNow, Jira Service Management)

1. Create custom ticket type: "Software Request"
2. Add custom fields (requester info, software details, justification)
3. Configure workflow routing (IT Ops → Security → Approval)

**Option 2: SharePoint/Microsoft Forms + Power Automate**

1. Create Microsoft Form with fields above
2. Form submission triggers Power Automate workflow:
   - Create SharePoint list item (tracking)
   - Email to IT Operations Manager (for review)
   - Track approval status
   - Notify requester when approved/rejected

**Option 3: Simple Email Request** (small organizations)

Email template:
```
To: it-operations@organization.ch
Subject: Software Request - [Software Name]

Requester: [Name, Department, Role]
Software Name: [Name]
Publisher: [Vendor]
Business Justification: [Why you need this]
Users Affected: [1 person / Department / Organization]

[Requester fills in template and emails]
```

IT Ops manually tracks in spreadsheet.

### 6.3 Security Review Procedures

**Security Manager conducts security review for all new software requests.**

**Security Review Checklist**:

**1. Vendor Reputation Assessment** (10 minutes):
- [ ] Search vendor name + "security breach" (Google, news)
- [ ] Check vendor website for security practices (https://vendor.com/security)
- [ ] Vendor track record (established company or unknown startup?)
- [ ] **Red Flags**: Recent breach, unknown vendor, suspicious website

**2. Vulnerability Assessment** (15 minutes):
- [ ] Search NIST NVD (National Vulnerability Database): https://nvd.nist.gov/
   - Search software name
   - Review known CVEs (vulnerabilities)
   - Recent critical CVEs? (within last 12 months)
- [ ] Check vendor security advisories (https://vendor.com/security-advisories)
- [ ] Patch availability (does vendor release timely patches?)
- [ ] **Red Flags**: Multiple critical CVEs, slow patch releases, abandoned software

**3. Privacy Assessment** (10 minutes):
- [ ] Review software privacy policy (what data does it collect?)
- [ ] Telemetry and data sharing (does software send data to vendor?)
- [ ] GDPR/FADP compliance (for Swiss organization: data residency concerns?)
- [ ] Personal data handling (if software processes personal data)
- [ ] **Red Flags**: Excessive data collection, no privacy policy, data sent to unknown countries

**4. Installation Requirements** (5 minutes):
- [ ] Admin privileges required? (elevates risk if yes)
- [ ] Network access required? (internet-facing = higher risk)
- [ ] Firewall rules needed? (document for IT Ops)
- [ ] Dependencies (requires other software to be installed?)

**5. Risk Classification**:
- Based on assessment above, classify: **High, Medium, Low** (per POL-S5 Section 2.2)
- High-risk software requires CISO approval

**6. Recommendation**:
- **Approve**: Software passes security review, acceptable risk
- **Approve with Conditions**: Approve if conditions met (e.g., "Approve if network access restricted to corporate network only")
- **Reject**: Security concerns outweigh business need, suggest alternative

**Security Review Documentation** (record in ticket or database):
- Reviewer name and date
- Risk classification
- Findings (vulnerabilities, privacy concerns)
- Recommendation and justification

**Example Security Review**:
```
Software: Slack Desktop App
Publisher: Slack Technologies (Salesforce)
Requested by: Marketing Team

Security Review (2026-01-11, Security Manager):
1. Vendor Reputation: ✓ Salesforce-owned, established, good track record
2. Vulnerability Assessment: ✓ Few CVEs, timely patches, actively maintained
3. Privacy: ⚠ Collects usage data, processes messages (encrypted in transit/rest), GDPR compliant
4. Installation: Internet access required, no admin privileges
5. Risk Classification: Medium (internet-facing communication tool)
6. Recommendation: Approve
   - Rationale: Established vendor, good security practices, business-critical for marketing
   - Condition: Remind users not to share sensitive data in Slack (use encrypted email for confidential)
```

### 6.4 Compatibility Testing Procedures

**IT Operations conducts compatibility testing** (in parallel with security review or after security approval).

**Testing Scope**:
- Install software in test environment
- Verify functionality on representative OS versions (Windows 10, 11, macOS Sonoma, etc.)
- Test interaction with existing software (conflicts?)
- Performance impact (CPU, memory, disk usage)

**Test Environment**:
- Dedicated test machines (not production)
- Virtual machines (VMware, Hyper-V) for rapid testing
- Ideally: Match production OS versions and configurations

**Testing Procedure**:

**Step 1: Install Software**
- Download installer from official source (vendor website, software request link)
- Verify file hash (if provided by vendor) - integrity check
- Install on test machine (follow vendor instructions)
- Document installation steps (for future deployments)

**Step 2: Functionality Testing**
- Launch software, verify basic functionality
- Test key features (based on requester's use case)
- Test integration with other applications (if applicable)
  - Example: If software is a plugin for Office, test with Office

**Step 3: Conflict Testing**
- Check for conflicts with existing approved software:
  - Anti-malware (does anti-malware flag software as suspicious?)
  - Application control (will AppLocker/Gatekeeper block this software?)
  - Other productivity tools (any interference?)

**Step 4: Performance Testing**
- Monitor CPU and memory usage (Task Manager or Activity Monitor)
- Acceptable thresholds:
  - Idle CPU usage: <5%
  - Idle memory usage: <500 MB (desktop apps)
  - No excessive disk I/O
- Performance issues? → Document, may require optimization or rejection

**Step 5: Uninstall Testing**
- Uninstall software (Control Panel → Programs or vendor uninstaller)
- Verify clean uninstall (no residual files, registry entries)
- Uninstall issues? → Document for future reference

**Compatibility Test Report**:
```
Software: Adobe Acrobat Pro DC 2024
Test Date: 2026-01-11
Tested by: IT Operations Technician

Test Environment: Windows 11 23H2, 8 GB RAM
Installation: ✓ Successful, no issues
Functionality: ✓ PDF viewing, editing, signing tested - works as expected
Conflicts: ✓ No conflicts detected with Office, Chrome, anti-malware
Performance: ✓ Idle CPU: 0%, Memory: 250 MB (acceptable)
Uninstall: ✓ Clean uninstall, no residual files

Recommendation: Approve for deployment
```

### 6.5 Approval Decision and Notification

**After Security Review + Compatibility Testing**, approval decision is made.

**Decision Matrix**:

| Security Review | IT Ops Review | Required Approval | Decision |
|-----------------|---------------|-------------------|----------|
| Approve (Low/Medium risk) | Approve | IT Operations Manager | **Approved** |
| Approve (High risk) | Approve | IT Operations Manager + CISO | **Approved** (after CISO sign-off) |
| Approve with Conditions | Approve (conditions met) | IT Operations Manager | **Conditional Approval** (monitor conditions) |
| Reject | N/A | N/A | **Rejected** |
| Approve | Reject (compatibility issues) | N/A | **Rejected** (suggest alternative or wait for fix) |

**Approval Notification** (to requester):
```
Subject: Software Request Approved - [Software Name]

Dear [Requester],

Your software request has been approved:

Software: [Software Name]
Approval Date: [Date]
Approved By: IT Operations Manager, Security Manager

Next Steps:
1. Software has been added to the approved software list
2. IT will deploy software to your endpoint within [X] business days
3. You will receive notification when installation is complete

Conditions (if any): [List any usage conditions or restrictions]

Questions? Contact IT Service Desk.
```

**Rejection Notification**:
```
Subject: Software Request Not Approved - [Software Name]

Dear [Requester],

Unfortunately, we cannot approve your software request at this time.

Software: [Software Name]
Reason: [Security concerns, compatibility issues, license cost, etc.]

Alternative Solutions:
- [Alternative 1]: [Approved software with similar functionality]
- [Alternative 2]: [Web-based solution, SaaS alternative]

If you have questions or would like to discuss alternatives, please contact IT Operations.
```

**Conditional Approval Notification**:
```
Subject: Software Request - Conditional Approval - [Software Name]

Dear [Requester],

Your software request is conditionally approved, pending:
- [Condition 1, e.g., "Approval for budget allocation ($500)"]
- [Condition 2, e.g., "Completion of vendor security questionnaire"]

Please address the conditions above and reply to this email. Once conditions are met, 
we will proceed with deployment.

Questions? Contact IT Operations.
```

---

## 7. Application Control Implementation - Windows

### 7.1 AppLocker Overview

**AppLocker** is Windows' built-in application control feature (Windows 10/11 Enterprise, Windows Server).

**AppLocker Capabilities**:
- Allow or deny applications based on rules
- Rule types: Publisher, Path, Hash
- Enforcement per user or group
- Audit mode (log violations without blocking)

**When to Use AppLocker**:
- Standard Windows deployments (10/11 Enterprise)
- Balance of security and usability
- Easier configuration than WDAC

**Limitations**:
- Not as strong as WDAC (can be bypassed with admin rights)
- Requires Windows Enterprise or Education edition (not available in Pro)

### 7.2 AppLocker Rule Types

**Three Rule Types**:

**1. Publisher Rules** (Recommended - Most Flexible):
- Based on digital signature (code signing certificate)
- Example: "Allow all files signed by Microsoft Corporation"
- **Pros**: Survives software updates (signature remains same), flexible
- **Cons**: Requires software to be digitally signed

**2. Path Rules**:
- Based on file or folder path
- Example: "Allow all files in C:\Program Files\Adobe\"
- **Pros**: Simple, works for unsigned software
- **Cons**: Can be bypassed (copy file to allowed location), breaks if path changes

**3. Hash Rules**:
- Based on file hash (SHA-256)
- Example: "Allow only this specific chrome.exe with hash ABC123..."
- **Pros**: Most specific, exact file match
- **Cons**: Breaks with every software update (hash changes), high maintenance

**Recommendation**:
- **Preferred**: Publisher rules (for signed software)
- **Fallback**: Path rules (for unsigned or internal software)
- **Avoid**: Hash rules (unless very specific security requirement)

### 7.3 AppLocker Deployment via GPO

**Scenario**: Deploy AppLocker to all Windows 10/11 corporate endpoints via Group Policy.

**Prerequisites**:
- Active Directory domain
- Windows 10/11 Enterprise or Education (target endpoints)
- Approved software list completed (Section 5)

**Step 1: Enable AppLocker Service**

AppLocker requires "Application Identity" service to run.

1. **Group Policy Management** → Create/edit GPO: "AppLocker Policy"
2. **Computer Configuration → Preferences → Control Panel Settings → Services**
3. **New → Service**:
   - Service name: `AppIDSvc`
   - Startup: **Automatic**
   - Service action: **Start service**
4. **OK**

**Step 2: Create Default Allow Rules** (Important!)

AppLocker defaults to "deny all" - must create allow rules for Windows to function.

1. **Computer Configuration → Policies → Windows Settings → Security Settings → Application Control Policies → AppLocker**
2. **Executable Rules** → **Create Default Rules**
   - This creates rules to allow Windows system files (Windows folder, Program Files)
   - Without default rules, Windows won't boot!

**Step 3: Create Publisher Rules for Approved Software**

For each approved software with digital signature:

1. **AppLocker → Executable Rules → Create New Rule → Next**
2. **Permissions**: Allow
3. **User or Group**: **Everyone** (or specific group, e.g., "Domain Users")
4. **Conditions**: **Publisher**
5. **Browse**: Select example .exe file from approved software (e.g., `C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe`)
6. **Slider**: Adjust to appropriate level:
   - **Publisher only**: Allow all files from this publisher (broad)
   - **Product name**: Allow all versions of this product (recommended)
   - **File version**: Allow only specific version (restrictive)
7. **Create** → Rule created

**Example: Allow Adobe Acrobat DC (all versions)**:
- Publisher: `O=ADOBE INC., L=SAN JOSE, S=CALIFORNIA, C=US`
- Product name: `ADOBE ACROBAT`
- Slider: **Product name** (allows all Acrobat versions)

**Step 4: Create Path Rules for Unsigned Software**

For software without digital signature (rare, or internal tools):

1. **Executable Rules → Create New Rule → Publisher**
2. **Conditions**: **Path**
3. **Path**: `C:\Program Files\InternalTool\*` (wildcard allows all files in folder)
4. **Create**

**Step 5: Test in Audit Mode First**

Before enforcing, test in audit mode (log violations without blocking):

1. **AppLocker → Executable Rules → Properties**
2. **Enforcement**: **Audit only** (for all rule collections)
3. **Apply** → **OK**

4. Link GPO to pilot OU
5. Wait 24-48 hours, review logs:
   - **Event Viewer → Applications and Services Logs → Microsoft → Windows → AppLocker → EXE and DLL**
   - Event ID 8004: Would have been blocked (audit mode)
6. Identify false positives (legitimate software being blocked):
   - Add allow rules for missed software
7. Refine rules

**Step 6: Switch to Enforcement Mode**

After audit mode testing:

1. **AppLocker → Properties → Enforcement**: **Enforce rules**
2. **Apply**

**Step 7: Monitor and Maintain**

- Weekly review of Event Viewer logs (blocked applications)
- Users report issues → Investigate → Add allow rules if legitimate
- New software approvals → Add to AppLocker rules

### 7.4 AppLocker Deployment via Intune

**Scenario**: Cloud-managed Windows 10/11 devices (Azure AD joined).

**Step 1: Create Configuration Profile**

1. **Microsoft Endpoint Manager → Devices → Configuration profiles → Create profile**
2. **Platform**: Windows 10 and later
3. **Profile type**: **Templates → Device restrictions**
4. **Settings → App Store → Block all apps from Microsoft Store not installed by Intune**: Enable (if restricting Store apps)

**Note**: Intune does not have native AppLocker UI, use Custom OMA-URI policy.

**Step 2: Create Custom OMA-URI Policy for AppLocker**

1. **Create profile → Custom**
2. **OMA-URI Settings → Add**:
   - **Name**: AppLocker Executable Rules
   - **OMA-URI**: `./Vendor/MSFT/AppLocker/ApplicationLaunchRestrictions/EXE/Policy`
   - **Data type**: String (XML)
   - **Value**: AppLocker XML policy

**AppLocker XML Policy** (export from GPO or manually create):

```xml
<AppLockerPolicy Version="1">
  <RuleCollection Type="Exe" EnforcementMode="Enabled">
    <!-- Default Windows Rules -->
    <FilePublisherRule Id="..." Name="All signed files from Windows" Description="" UserOrGroupSid="S-1-1-0" Action="Allow">
      <Conditions>
        <FilePublisherCondition PublisherName="O=MICROSOFT CORPORATION*" ProductName="*" BinaryName="*">
          <BinaryVersionRange LowSection="*" HighSection="*" />
        </FilePublisherCondition>
      </Conditions>
    </FilePublisherRule>
    
    <!-- Approved Software: Adobe Acrobat -->
    <FilePublisherRule Id="..." Name="Adobe Acrobat DC" Description="" UserOrGroupSid="S-1-1-0" Action="Allow">
      <Conditions>
        <FilePublisherCondition PublisherName="O=ADOBE INC.*" ProductName="ADOBE ACROBAT" BinaryName="*">
          <BinaryVersionRange LowSection="*" HighSection="*" />
        </FilePublisherCondition>
      </Conditions>
    </FilePublisherRule>
    
    <!-- Add more rules for each approved software -->
  </RuleCollection>
</AppLockerPolicy>
```

3. **Assignments**: Assign to device group (e.g., "Corporate-Windows-Devices")
4. **Create**

**Verification**:
- Devices receive policy during check-in
- Test on pilot device: Attempt to run unapproved software → Should be blocked
- Event Viewer logs block events

### 7.5 Windows Defender Application Control (WDAC)

**WDAC** is a stronger alternative to AppLocker (code integrity policies, kernel-level enforcement).

**When to Use WDAC**:
- High-security environments (government, critical infrastructure)
- Require kernel-level protection (cannot be bypassed even with admin rights)
- Windows 10/11 (all editions support WDAC)

**Complexity**: WDAC is more complex than AppLocker (requires careful planning and testing).

**WDAC Policy Creation** (Overview):

1. **Create base policy**:
   ```powershell
   New-CIPolicy -Level Publisher -FilePath "BasePolicy.xml" -UserPEs -Fallback Hash
   ```

2. **Merge with Microsoft recommended policies**:
   ```powershell
   Merge-CIPolicy -PolicyPaths "BasePolicy.xml", "C:\Windows\schemas\CodeIntegrity\ExamplePolicies\AllowMicrosoft.xml" -OutputFilePath "MergedPolicy.xml"
   ```

3. **Convert to binary**:
   ```powershell
   ConvertFrom-CIPolicy "MergedPolicy.xml" "SIPolicy.p7b"
   ```

4. **Deploy via GPO or Intune** (copy to `C:\Windows\System32\CodeIntegrity\SIPolicy.p7b`)

**Recommendation**: Use AppLocker for most organizations; WDAC for high-security needs. WDAC requires specialized expertise.

---

## 8. Application Control Implementation - macOS

### 8.1 Gatekeeper Overview

**Gatekeeper** is macOS's built-in application control (verifies app signatures before allowing execution).

**Gatekeeper Levels**:
- **App Store**: Only apps from Mac App Store allowed
- **App Store and Identified Developers**: Apps from App Store + apps signed by Apple-registered developers (default)
- **Anywhere**: No restrictions (not recommended, requires disabling via terminal)

**Default Setting**: "App Store and Identified Developers" (reasonable for most organizations).

**Limitation**: Gatekeeper does not provide granular control (cannot allowlist specific apps). For granular control, use MDM restrictions.

### 8.2 Gatekeeper Configuration via MDM

**Scenario**: Enforce Gatekeeper via Jamf Pro or Intune.

**Jamf Pro Configuration**:

1. **Computers → Configuration Profiles → New**
2. **Security & Privacy**:
   - **Gatekeeper**: 
     - **Allow apps downloaded from**: Mac App Store and identified developers
     - **Do not allow user to override**: **Enabled** (prevent user from changing setting)
3. **Scope**: All managed Macs
4. **Save**

**Intune Configuration**:

1. **Devices → macOS → Configuration profiles → Create profile**
2. **Profile type**: **Templates → Device restrictions**
3. **Settings → Built-in Apps**:
   - **Block App Store**: No (allow App Store)
4. **Settings → General**:
   - **Allow Gatekeeper to be disabled**: **No** (enforce Gatekeeper)
5. **Assignments**: All macOS devices
6. **Create**

**Verification**:
- On Mac: **System Settings → Privacy & Security → Security**
- Verify: "Allow applications downloaded from: App Store and identified developers"
- Setting is grayed out (cannot be changed by user)

### 8.3 Application Restrictions via MDM

**For granular control** (allow only specific apps), use MDM restrictions.

**Jamf Pro - Restricted Software**:

1. **Computers → Restricted Software → New**
2. **General**:
   - **Display Name**: Unauthorized Games
   - **Process Name**: `candycrush.app` (example)
   - **Match Exact Process Name**: Checked
3. **Options**:
   - **Send Notification**: Enabled
   - **Kill Process**: Enabled (terminate if running)
4. **Scope**: All Macs
5. **Save**

When user attempts to run `candycrush.app`:
- Jamf detects process
- Terminates process
- Displays notification: "This application is restricted by your organization."

**Allowlist Approach** (more complex, use MDM configuration profile):

1. Create configuration profile with allowed bundle IDs
2. Block all apps except those on allowlist

**Note**: macOS app control is more limited than Windows. For strict control, consider VDI or restricted user accounts.

### 8.4 macOS User Account Restrictions

**Alternative to Application Control**: Use standard user accounts (not admin).

**Standard Users Cannot**:
- Install applications to `/Applications` folder (requires admin password)
- Modify system settings
- Install system extensions

**Organizational Approach**:
1. All user accounts are **Standard** (not Administrator)
2. IT maintains separate **Administrator** account (for installations)
3. Users request IT to install approved software (IT logs in with admin account, installs)

**Pros**: Simple, effective for small organizations
**Cons**: Requires IT intervention for every installation (not scalable)

**Configuration via MDM** (prevent admin account creation):

1. **Jamf Pro → Configuration Profiles → Accounts**:
   - **Prevent Mac users from being administrators**: **Enabled**
2. **Scope**: All Macs

---

## 9. Application Control Implementation - Linux

### 9.1 Linux Application Control Options

**Linux Application Control Technologies**:

1. **AppArmor**: Mandatory Access Control (MAC) framework (Ubuntu, Debian, SUSE)
2. **SELinux**: Security-Enhanced Linux (RHEL, CentOS, Fedora)
3. **Package Manager Restrictions**: Restrict apt, yum, dnf to sudoers only
4. **Custom Scripts**: Allowlist-based execution control (custom solution)

**Recommendation**:
- **RHEL/CentOS**: Use SELinux (built-in, well-integrated)
- **Ubuntu/Debian**: Use AppArmor (default, easier than SELinux)
- **All**: Restrict package manager access (minimum baseline)

### 9.2 Package Manager Restrictions

**Purpose**: Prevent non-admin users from installing software.

**By default**, Linux requires `sudo` (root privileges) for package installation:
- `sudo apt install [package]` (Debian/Ubuntu)
- `sudo yum install [package]` (RHEL/CentOS)

**Ensure sudo is properly configured**:

1. **Review `/etc/sudoers` file**:
   ```bash
   sudo visudo
   ```

2. **Verify only authorized users have sudo access**:
   ```
   # User privilege specification
   root    ALL=(ALL:ALL) ALL
   admin   ALL=(ALL:ALL) ALL
   
   # Group privilege specification
   %sudo   ALL=(ALL:ALL) ALL  # Users in sudo group can use sudo
   ```

3. **Do NOT grant broad sudo access**:
   - Avoid: `user ALL=(ALL:ALL) NOPASSWD: ALL` (no password, dangerous)
   - Avoid: Adding all users to `sudo` group

4. **Restrict to specific users or groups**:
   - IT admins only have sudo access
   - Standard users: NO sudo access (cannot install software)

**Verification**:
- Log in as standard user (non-sudo)
- Attempt: `sudo apt install htop`
- Expected: `user is not in the sudoers file. This incident will be reported.`

**Enforcement**: With sudo properly restricted, users cannot install software via package managers (apt, yum).

### 9.3 AppArmor Implementation (Ubuntu/Debian)

**AppArmor** confines applications to a set of allowed actions (files, network, etc.).

**AppArmor Modes**:
- **Enforce**: Block violations
- **Complain**: Log violations, allow (for testing)

**Use Case**: Restrict specific applications (e.g., web browser can only access certain directories).

**Example: Restrict Firefox** (prevent access to /home except downloads):

1. **Install AppArmor utilities** (if not installed):
   ```bash
   sudo apt install apparmor-utils
   ```

2. **Create AppArmor profile** for Firefox:
   ```bash
   sudo aa-genprof firefox
   ```
   - Run Firefox, perform typical actions (browse, download)
   - aa-genprof watches Firefox, creates profile based on observed behavior

3. **Edit profile**: `/etc/apparmor.d/usr.bin.firefox` (or similar path)
   ```
   #include <tunables/global>
   
   /usr/bin/firefox {
     #include <abstractions/base>
     #include <abstractions/fonts>
     
     # Allow read/write to downloads folder only
     owner /home/*/Downloads/** rw,
     
     # Deny access to other home folders
     deny /home/*/Documents/** rw,
     deny /home/*/Pictures/** rw,
     
     # Allow network access
     network inet stream,
     network inet6 stream,
   }
   ```

4. **Load profile**:
   ```bash
   sudo apparmor_parser -r /etc/apparmor.d/usr.bin.firefox
   ```

5. **Enable enforce mode**:
   ```bash
   sudo aa-enforce /usr/bin/firefox
   ```

**Verification**:
- Run Firefox as user
- Attempt to save file to `/home/user/Documents/` → Should be denied (AppArmor blocks)
- Save to `/home/user/Downloads/` → Allowed

**Limitation**: AppArmor is per-application, not per-executable allowlist (different use case than AppLocker).

### 9.4 SELinux Implementation (RHEL/CentOS)

**SELinux** provides mandatory access control (MAC) at kernel level.

**SELinux Modes**:
- **Enforcing**: Block policy violations
- **Permissive**: Log violations, allow (testing)
- **Disabled**: SELinux off (not recommended)

**Default**: Most RHEL/CentOS systems have SELinux in **Enforcing** mode by default.

**Verify SELinux Status**:
```bash
sestatus
```

Expected output:
```
SELinux status:                 enabled
Current mode:                   enforcing
```

**SELinux Use Case**: Confine system services, prevent privilege escalation.

**Example: Ensure user cannot execute binaries from /tmp** (common attack vector):

1. **Check current context**:
   ```bash
   ls -Z /tmp
   ```

2. **SELinux prevents execution from /tmp by default** (if policy configured correctly).

3. **Test**:
   ```bash
   echo '#!/bin/bash' > /tmp/test.sh
   echo 'echo "Hello"' >> /tmp/test.sh
   chmod +x /tmp/test.sh
   /tmp/test.sh
   ```
   Expected (if SELinux enforcing): `Permission denied` (SELinux blocks execution from tmp_t context)

**SELinux Management**:
- Modifying SELinux policies requires deep expertise (beyond scope of basic application control)
- For most organizations: Keep SELinux in **Enforcing** mode with default policies (provides baseline protection)

**Recommendation**: Use package manager restrictions as primary control, SELinux as defense-in-depth.

---

## 10. Application Control Implementation - Mobile

### 10.1 iOS Application Management via MDM

**Scenario**: Control app installations on corporate iOS devices (iPhones, iPads).

**MDM Capabilities**:
- Deploy approved apps (VPP - Volume Purchase Program)
- Prevent App Store access (supervised devices only)
- Remove apps remotely
- Create allowlist (supervised devices)

**Deployment via Intune**:

**Step 1: Configure App Restrictions**

1. **Devices → iOS/iPadOS → Configuration profiles → Create profile**
2. **Profile type**: **Device restrictions**
3. **Settings → App Store, Doc Viewing, Gaming**:
   - **Block App Store**: Yes (prevents user from installing apps)
   - **Require App Store password for all purchases**: Yes
4. **Settings → Built-in Apps**:
   - **Block Safari**: No (allow browser)
   - **Block Camera**: No (allow camera, unless high-security environment)
5. **Assignments**: Corporate iOS devices
6. **Create**

**Step 2: Deploy Approved Apps**

1. **Apps → iOS/iPadOS → Add**
2. **App type**: **iOS store app** (for free apps) or **iOS VPP app** (for purchased apps)
3. **Search App Store**: Find approved app (e.g., "Microsoft Outlook")
4. **Select app** → **Add**
5. **Assignments**:
   - **Required**: App automatically installs
   - **Available**: App available in Company Portal for user to install
6. **Create**

**Verification**:
- User's iPhone: Approved apps appear automatically (if Required) or in Company Portal (if Available)
- App Store icon: Hidden (if blocked in restrictions)
- User cannot install unapproved apps

**Limitation**: Blocking App Store entirely may frustrate users (cannot install personal apps on BYOD). See Section 10.4 for BYOD approach.

### 10.2 Android Application Management via MDM

**Scenario**: Control app installations on corporate Android devices (managed via Android Enterprise).

**Android Enterprise Work Profile** (Recommended for BYOD):
- Separate work profile (corporate apps and data)
- Personal profile (user's personal apps and data)
- Organization controls work profile only (privacy-respecting)

**Deployment via Intune**:

**Step 1: Enable Managed Google Play**

1. **Devices → Android → Managed Google Play** (one-time setup)
2. **Agree** to terms → Links Intune to Managed Google Play

**Step 2: Approve Apps**

1. **Apps → Android → Managed Google Play**
2. **Search**: Find approved app (e.g., "Microsoft Teams")
3. **Approve** → **Approval settings**: Keep approved when app requests new permissions
4. **Approve**

**Step 3: Assign Apps**

1. **Apps → Android** → App appears after sync
2. **Select app** → **Assignments**
3. **Required**: Work profile (auto-installs in work profile)
4. **Save**

**Step 4: Restrict Personal App Sideloading** (work profile only)

1. **Devices → Android → Configuration profiles → Create profile**
2. **Profile type**: **Device restrictions**
3. **Settings → Work Profile Settings**:
   - **Allow installing apps from unknown sources in personal profile**: **Not configured** (user can install personal apps)
   - **Require work profile password**: **Yes**
4. **Assignments**: All managed Android devices
5. **Create**

**Verification**:
- User's Android device: Work profile badge (briefcase icon) on work apps
- Work apps: Only approved apps installable
- Personal profile: User can install any app (organization does not control)

### 10.3 Mobile App Allowlisting (Supervised Devices)

**iOS Supervised Devices** (corporate-owned only, not BYOD):

Supervision allows stricter control (app allowlisting).

**Create App Allowlist**:

1. **Intune → Devices → iOS/iPadOS → Configuration profiles → Create profile**
2. **Profile type**: **Device restrictions → Restricted apps**
3. **Settings**:
   - **Type of restricted apps list**: **Allowed apps** (allowlist)
   - **Add**: List of allowed app bundle IDs
     - Example: `com.microsoft.Office.Outlook` (Outlook)
     - Example: `com.apple.mobilesafari` (Safari)
4. **Assignments**: Supervised iOS devices
5. **Create**

**Effect**: Only apps in allowlist can be installed/run. All other apps are blocked.

**Limitation**: Requires device supervision (corporate-owned devices enrolled via DEP/ABM).

### 10.4 BYOD Mobile Application Control

**BYOD Privacy Considerations**:

Users will not accept full device management on personal devices (privacy violation).

**Solution: Mobile Application Management (MAM)**:
- Manage corporate apps only (containerized)
- Do not manage personal apps or data

**MAM Implementation via Intune**:

**Step 1: Create App Protection Policy**

1. **Apps → App protection policies → Create policy → iOS/iPadOS** (or Android)
2. **Apps**: Select corporate apps to protect (Outlook, OneDrive, Teams, etc.)
3. **Data protection**:
   - **Prevent iTunes and iCloud backups**: **Yes** (prevent corporate data backup to personal iCloud)
   - **Send org data to other apps**: **Policy managed apps** (only to other corporate apps)
   - **Receive data from other apps**: **All apps** (allow receiving from personal apps, e.g., attaching photo)
4. **Access requirements**:
   - **PIN for access**: **Yes** (require PIN to access corporate apps)
   - **Biometrics instead of PIN**: **Yes** (allow Touch ID/Face ID)
5. **Conditional launch**:
   - **Max OS version**: **Not configured** (or Latest -1, allow updates)
   - **Min app version**: **Latest - 1** (require recent app version)
6. **Assignments**: All BYOD users
7. **Create**

**Effect**:
- User installs corporate apps (Outlook, Teams) on personal iPhone
- Apps require PIN to access (corporate data protected)
- Corporate data cannot be copied to personal apps (cut/paste blocked)
- Personal apps and data: Not managed, user has full control

**Verification**:
- User opens Outlook (corporate app) → Prompted for PIN
- User attempts to copy email text to personal Notes app → Blocked
- User's personal apps (Photos, Games, etc.): Not affected by policy

---

## 11. Software Inventory Collection

### 11.1 Purpose of Continuous Inventory

**After initial inventory** (Section 4), maintain continuous software inventory:
- Detect new software installations (authorized or unauthorized)
- Track software version changes (upgrades, patches)
- Monitor license utilization
- Provide data for compliance reporting

**Inventory Frequency**:
- **Daily**: Ideal (detect unauthorized software within 24 hours)
- **Weekly**: Acceptable for smaller deployments
- **Monthly**: Minimum (compliance requirement, not optimal for security)

**Target**: Inventory all corporate endpoints (≥95% coverage).

### 11.2 Automated Inventory via Intune

**Configuration**:

Intune automatically collects inventory (no additional configuration needed):

1. **Devices → All devices → [Select device] → Discovered apps**
2. View: List of installed apps on selected device

**Exporting Inventory**:

1. **Apps → Discovered apps**
2. **Export**: Download CSV file with all discovered apps across all devices

**Columns in Export**:
- Application name
- Version
- Publisher
- Number of devices with app installed

**Scheduling**: Intune collects inventory during device check-in (default: every 8 hours).

**Increasing Inventory Frequency**:
- Intune: Cannot manually adjust (cloud-managed schedule)
- Devices check in automatically when online

### 11.3 Automated Inventory via SCCM

**Configuration**:

1. **SCCM Console → Administration → Client Settings → Default Client Settings**
2. **Software Inventory**:
   - **Enable software inventory on clients**: **Yes**
   - **Schedule software inventory**: **Every 7 days** (or daily if needed)
   - **Inventory file types**: (default includes .exe, .dll, etc.)
3. **OK**

**Collecting Inventory**:

1. **Assets and Compliance → Device Collections → [Collection Name]**
2. Right-click → **Update Membership** (forces inventory collection)

**Exporting Inventory**:

1. **Monitoring → Reporting → Reports → Software - Files**
2. Run report: **"All inventoried files for a specific product"** or **"All software"**
3. Export to CSV or Excel

**SQL Query** (direct database access for automation):

```sql
SELECT 
    v_GS_INSTALLED_SOFTWARE.ProductName0 AS Software,
    v_GS_INSTALLED_SOFTWARE.ProductVersion0 AS Version,
    v_GS_INSTALLED_SOFTWARE.Publisher0 AS Publisher,
    v_R_System.Name0 AS DeviceName,
    v_R_System.Resource_Domain_OR_Workgr0 AS Domain
FROM v_GS_INSTALLED_SOFTWARE
INNER JOIN v_R_System ON v_GS_INSTALLED_SOFTWARE.ResourceID = v_R_System.ResourceID
ORDER BY Software, DeviceName;
```

### 11.4 Automated Inventory via Jamf Pro

**Configuration**:

1. **Jamf Pro → Settings → Computer Management → Inventory Collection**
2. **Collect installed applications**: **Enabled**
3. **Inventory collection frequency**: **Once per day** (or custom interval)

**Viewing Inventory**:

1. **Computers → Search Inventory**
2. **Advanced → Applications → [Application Name]**
3. Results: List of devices with application installed

**Exporting Inventory**:

1. **Computers → Advanced Computer Search → New**
2. **Criteria**: Applications → [Application Name] → is installed
3. **Display**: Name, Application Name, Application Version
4. **Save**
5. **View → Export** → CSV

**API Export** (for automation):

```bash
# Jamf Pro API: Get all computers with applications
curl -X GET "https://jamf.example.com/JSSResource/computers/subset/basic" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json" | jq '.computers'
```

### 11.5 Inventory Normalization Script

**Problem**: Inventory from different sources needs normalization (see Section 4.3).

**Automated Normalization Script** (Python):

```python
#!/usr/bin/env python3
"""
Software Inventory Normalization Script

Reads raw inventory CSV, normalizes software names, exports normalized inventory.
"""

import pandas as pd
import re

def normalize_software_name(name):
    """Normalize software name (remove version, architecture)."""
    if pd.isna(name):
        return ""
    
    # Remove version numbers
    name = re.sub(r'\d+(\.\d+)*', '', name)
    
    # Remove architecture indicators
    name = name.replace('(x64)', '').replace('(x86)', '')
    name = name.replace('64-bit', '').replace('32-bit', '')
    
    # Remove extra spaces
    name = re.sub(r'\s+', ' ', name).strip()
    
    return name

def main():
    # Load raw inventory
    df = pd.read_csv('raw_inventory.csv')
    
    # Normalize software names
    df['SoftwareNormalized'] = df['Software'].apply(normalize_software_name)
    
    # Group by normalized name
    summary = df.groupby('SoftwareNormalized').agg({
        'Device': 'nunique',  # Count unique devices
        'Software': 'first',  # Keep original name as example
        'Publisher': 'first'  # Keep publisher
    }).reset_index()
    
    summary.columns = ['Software (Normalized)', 'Device Count', 'Original Name', 'Publisher']
    summary = summary.sort_values('Device Count', ascending=False)
    
    # Export normalized inventory
    summary.to_csv('normalized_inventory.csv', index=False)
    print(f"Normalized inventory saved: normalized_inventory.csv")
    print(f"Total unique software: {len(summary)}")

if __name__ == "__main__":
    main()
```

**Usage**:
```bash
python normalize_inventory.py
```

**Output**: `normalized_inventory.csv` with clean, normalized software names.

---

## 12. Unauthorized Software Detection and Remediation

### 12.1 Detection Methodology

**Compare Inventory to Approved List**:

**Step 1: Export Current Inventory** (from Section 11)
- File: `current_inventory.csv`
- Columns: Device, Software, Version, Publisher

**Step 2: Load Approved Software List** (from Section 5)
- File: `approved_software.xlsx`
- Worksheet: Approved_Software
- Columns: Software Name, Publisher, Approved Versions

**Step 3: Compare** (identify software in inventory but NOT in approved list)

**Excel Method**:

1. Load both files into Excel (separate sheets)
2. Sheet 1: Current Inventory (column A: Software)
3. Sheet 2: Approved Software (column A: Software Name)
4. Sheet 3: Unauthorized Software (create formula):
   ```excel
   =IF(ISNA(VLOOKUP(Sheet1!A2, Sheet2!A:A, 1, FALSE)), Sheet1!A2, "")
   ```
5. Copy down → Lists all software in inventory but NOT approved
6. Filter blanks → Unauthorized software list

**Python Script** (automated):

```python
import pandas as pd

# Load data
inventory = pd.read_csv('current_inventory.csv')
approved = pd.read_excel('approved_software.xlsx', sheet_name='Approved_Software')

# Normalize for comparison (lowercase, strip spaces)
inventory['Software_Lower'] = inventory['Software'].str.lower().str.strip()
approved['Software_Lower'] = approved['Software Name'].str.lower().str.strip()

# Identify unauthorized (in inventory but not in approved)
unauthorized = inventory[~inventory['Software_Lower'].isin(approved['Software_Lower'])]

# Classify by risk (manual or automated based on keywords)
def classify_risk(software_name):
    high_risk_keywords = ['crack', 'keygen', 'torrent', 'game', 'casino']
    medium_risk_keywords = ['utility', 'tool', 'player']
    
    name_lower = software_name.lower()
    
    if any(keyword in name_lower for keyword in high_risk_keywords):
        return 'High'
    elif any(keyword in name_lower for keyword in medium_risk_keywords):
        return 'Medium'
    else:
        return 'Low'

unauthorized['Risk'] = unauthorized['Software'].apply(classify_risk)

# Group by software (count devices)
unauthorized_summary = unauthorized.groupby(['Software', 'Risk']).agg({
    'Device': 'nunique'
}).reset_index()

unauthorized_summary.columns = ['Software', 'Risk', 'Device Count']
unauthorized_summary = unauthorized_summary.sort_values(['Risk', 'Device Count'], ascending=[False, False])

# Export
unauthorized_summary.to_csv('unauthorized_software.csv', index=False)

print(f"Unauthorized software detected: {len(unauthorized_summary)}")
print(f"High-risk: {len(unauthorized_summary[unauthorized_summary['Risk'] == 'High'])}")
print(f"Devices affected: {unauthorized['Device'].nunique()}")
```

**Output**: `unauthorized_software.csv` with:
- Software name
- Risk level (High, Medium, Low)
- Device count (how many devices have this software)

### 12.2 User Notification

**For each unauthorized software detection**, notify affected user(s).

**Email Template**:
```
Subject: Unauthorized Software Detected on Your Endpoint - Action Required

Dear [User Name],

Our automated security scan has detected unauthorized software on your endpoint:

Device: [Device Name]
Software: [Software Name]
Risk Level: [High/Medium/Low]

REQUIRED ACTION:
Please uninstall this software within [5] business days. 

To uninstall:
- Windows: Control Panel → Programs and Features → Uninstall
- macOS: Drag application to Trash
- If you need this software for work, submit a software request: [Link to request form]

CONSEQUENCES OF NON-COMPLIANCE:
- Day 5: Reminder email
- Day 7: Manager notification
- Day 10: Endpoint isolation (network access blocked until software removed)

Questions? Contact IT Service Desk.

IT Security Team
```

**Automated Notification** (integrate with inventory script):

```python
# After detecting unauthorized software
for index, row in unauthorized.iterrows():
    user_email = get_user_email(row['Device'])  # Function to get user email from device
    
    send_email(
        to=user_email,
        subject="Unauthorized Software Detected - Action Required",
        body=f"Device: {row['Device']}\nSoftware: {row['Software']}\n\nPlease uninstall within 5 business days."
    )
```

### 12.3 Remediation Tracking

**Track remediation progress** (from notification to resolution).

**Tracking Spreadsheet** (or ticketing system):

| Detection ID | Device | User | Software | Risk | Notification Date | Deadline | Status | Remediation Date | Notes |
|--------------|--------|------|----------|------|-------------------|----------|--------|------------------|-------|
| UA-001 | LAPTOP-123 | john.doe | WinRAR | Low | 2026-01-11 | 2026-01-18 | Open | | |
| UA-002 | LAPTOP-456 | jane.smith | KMSPico | High | 2026-01-11 | 2026-01-18 | Resolved | 2026-01-13 | User uninstalled, case closed |

**Status Values**:
- **Open**: Notification sent, awaiting user action
- **Resolved**: Software uninstalled (verified in next inventory scan)
- **Approved**: User submitted request, software approved (move to approved list)
- **Escalated**: Past deadline, manager notified or network isolated

**Remediation SLA** (from POL-S5 REQ-A819-007):
- High-risk unauthorized software: 24 hours
- Medium/low-risk: 5 business days

### 12.4 Automated Removal (If Supported)

**Some MDM/management tools support remote application uninstallation**:

**Intune**:
- Limited capability (can remove apps deployed via Intune, cannot remove user-installed apps)

**SCCM**:
- Can uninstall applications if uninstaller package available
- Create uninstall task sequence, deploy to affected devices

**Jamf Pro**:
- Can remove apps via policy (if app is in Applications folder)
- **Policies → New → Packages**:
  - Script to remove app: `rm -rf /Applications/UnauthorizedApp.app`

**Manual Removal** (most common):
- User removes software themselves (per notification)
- IT manually removes if user cannot (remote desktop session)

### 12.5 Escalation Procedures

**If user does not remediate within deadline**:

**Day 5** (deadline passed):
- Reminder email to user: "This is your final reminder. Software must be removed by end of day."

**Day 7** (2 days overdue):
- Manager notification:
  ```
  Subject: Employee Non-Compliance - Unauthorized Software
  
  Dear [Manager Name],
  
  Your team member [User Name] has not removed unauthorized software from their endpoint 
  despite notifications. This creates security risk for [Organization].
  
  Software: [Software Name]
  Risk Level: [High/Medium/Low]
  Original Deadline: [Date]
  
  Please address with [User Name] immediately. If not resolved by [Day 10], endpoint 
  will be isolated from network.
  
  IT Security Team
  ```

**Day 10** (5 days overdue, or immediate for High-risk):
- **Network Isolation** (if supported):
  - Intune: Compliance policy marks device non-compliant → Conditional Access blocks network
  - SCCM: Move device to quarantine collection, firewall blocks access
  - Manual: Disable network port or block MAC address on switch

- **User Notification**:
  ```
  Subject: Endpoint Isolated - Unauthorized Software Not Removed
  
  Your endpoint has been isolated from the network due to unauthorized software.
  
  To regain access:
  1. Remove software: [Software Name]
  2. Contact IT Service Desk to verify removal and restore access
  
  IT Security Team
  ```

**Restoration**: After verification (manual check or next inventory scan shows software removed), restore network access.

---

## 13. Change Control Integration

### 13.1 Software Installation as Change

**Requirement** (POL-S5 REQ-A819-005): Software installations MUST follow change management process.

**Rationale**:
- Software changes system state (potential impact on stability, security)
- Change management provides approval, documentation, rollback plan
- Audit trail for compliance

**When Change Control Required**:
- **Deploying approved software to users** (initial deployment or version upgrade)
- **Adding new software to approved list** (organizational impact)
- **Updating application control policies** (affects all endpoints)

**When Change Control May Be Waived**:
- Security patches (expedited process, not full change control)
- Individual user software installation (if already approved and low-impact)

### 13.2 Change Request Template for Software Deployment

**RFC (Request for Change) Template**:

```
RFC-XXXX: Deploy Adobe Acrobat Pro DC to Marketing Department

SUMMARY:
Deploy Adobe Acrobat Pro DC 2024 to 50 users in Marketing Department.

BUSINESS JUSTIFICATION:
Marketing team requires PDF editing capabilities for brochure creation. Currently using 
free Adobe Reader (view-only). Acrobat Pro provides editing, form creation, e-signature.

SCOPE:
- Software: Adobe Acrobat Pro DC 2024
- Target: Marketing Department (50 users, 50 devices)
- Deployment method: SCCM
- Deployment window: After-hours (2026-01-20, 6:00 PM - 10:00 PM)

APPROVALS:
- Software Approval: Completed (approved 2026-01-11, IT Ops Manager + Security Manager)
- Change Advisory Board: Pending

RISK ASSESSMENT:
- Risk Level: Low (standard productivity software, widely used)
- Impact: Low (does not affect critical systems)
- Likelihood of issues: Low (tested in pilot successfully)

ROLLBACK PLAN:
- If deployment fails: Re-attempt deployment
- If software causes issues: Uninstall via SCCM (uninstall package prepared)

TESTING:
- Pilot deployment: 5 users, completed 2026-01-15, no issues
- Compatibility testing: Tested with Windows 10/11, Office 2021, no conflicts

DEPLOYMENT PLAN:
1. Deploy SCCM package to Marketing device collection
2. Install during maintenance window (devices online will install immediately, offline devices on next startup)
3. Verify installation: Check SCCM deployment report
4. User notification: Email users on 2026-01-21 (software available)

POST-IMPLEMENTATION VERIFICATION:
- Verify 50 devices have Acrobat Pro installed (SCCM report)
- User acceptance: Survey 10 random users (functionality meets needs?)
- Incident monitoring: Check for any Acrobat-related incidents within 7 days

SCHEDULE:
- CAB Review: 2026-01-18 (Friday)
- Deployment: 2026-01-20 (Sunday, 6:00 PM)
- Verification: 2026-01-21 (Monday)
```

**CAB Review**:
- Change Advisory Board meets weekly (or as needed)
- Reviews RFCs, approves/rejects/defers
- CAB composition: IT Manager, Security Manager, representatives from operations teams

**Approval**: CAB approves → RFC moves to "Scheduled" → Deployment proceeds.

### 13.3 Linking Software Approval to Change Control

**Workflow Integration**:

1. **Software Approval** (Section 6) → Software added to approved list
2. **Deployment Trigger**: User request or department-wide deployment
3. **Create RFC**: IT Operations creates change request
4. **CAB Approval**: Change Advisory Board reviews and approves
5. **Deployment**: Execute deployment per RFC schedule
6. **Post-Implementation Review**: Verify deployment success, close RFC

**Automation** (if using ITSM tool like ServiceNow):
- Software approval ticket → Automatically creates RFC (draft)
- IT Ops reviews/modifies RFC → Submits to CAB
- CAB approves → RFC status: Approved
- Deployment task → References RFC number

---

## 14. Verification Procedures

### 14.1 Application Control Verification

**Verify application control is functioning** (blocking unauthorized software).

**Test Procedure**:

**Windows (AppLocker)**:

1. Log in to test endpoint as **standard user** (not admin)
2. Attempt to run unapproved software (download portable .exe, e.g., PuTTY portable)
3. Double-click .exe
4. **Expected**: 
   - AppLocker blocks execution
   - Error message: "This app has been blocked by your system administrator."
   - Event logged: Event Viewer → AppLocker → EXE and DLL → Event ID 8004 (blocked)
5. **If not blocked**: AppLocker not configured correctly or not in enforce mode

**macOS (Gatekeeper)**:

1. Download unsigned app (or app from unidentified developer)
2. Attempt to open
3. **Expected**:
   - Gatekeeper blocks: "App cannot be opened because it is from an unidentified developer."
   - User cannot override (if MDM profile prevents override)
4. **If app opens**: Gatekeeper not enforced or app is signed

**Linux (Package Manager Restriction)**:

1. Log in as standard user (non-sudo)
2. Attempt: `sudo apt install htop`
3. **Expected**: `user is not in the sudoers file.`

**Sample Size**: Test on 5-10 devices (random sample, different OS/device types).

### 14.2 Unauthorized Software Detection Verification

**Verify detection process identifies unauthorized software**.

**Test Procedure**:

1. **Install test unauthorized software** on pilot endpoint:
   - Example: Install WinRAR (if not approved) on test laptop
2. **Wait for inventory cycle** (24 hours or trigger manual inventory)
3. **Run unauthorized software detection script** (Section 12.1)
4. **Expected**: Test software appears in unauthorized software report
5. **Remediate** (remove test software, verify removed in next inventory)

**Verification Schedule**: Monthly spot-check (install test software, verify detection).

### 14.3 Approval Workflow Verification

**Verify approval workflow functions correctly**.

**Test Procedure**:

1. **Submit test software request** (request low-risk, legitimate software)
2. **Track workflow**:
   - Request logged in ticketing system?
   - Routed to IT Operations?
   - Security review completed within SLA (5 days)?
   - Approval decision recorded?
   - Requester notified?
3. **Expected**: Workflow completes end-to-end, request approved (if legitimate)

**Verification Schedule**: Quarterly (test workflow, identify bottlenecks).

---

## 15. Common Pitfalls and Troubleshooting

### 15.1 Pitfall: AppLocker Blocks Legitimate Software (False Positive)

**Symptom**: Users report software they need for work is blocked by AppLocker.

**Causes**:
1. Legitimate software not in approved list (oversight)
2. Legitimate software not covered by publisher rule (unsigned software or different publisher)
3. AppLocker rule too restrictive (specific version hash rule, software updated)

**Solution**:

1. **Investigate**: Verify software is legitimate and business-justified
   - Ask user: "What do you use this software for?"
   - Search software name (is it reputable?)
2. **Add to Approved List** (if legitimate):
   - Follow approval process (Section 6)
   - Add AppLocker rule:
     - If signed: Publisher rule (recommended)
     - If unsigned: Path rule (if software installed in standard location)
3. **Communicate with User**:
   - "We've added [Software] to the approved list. You should be able to use it within [timeframe]."

**Prevention**:
- Thorough approved list development (Section 5) before deploying AppLocker
- Run AppLocker in **Audit Mode** for 2-4 weeks before enforcement (identify false positives proactively)

### 15.2 Pitfall: Unauthorized Software Not Detected (Detection Gap)

**Symptom**: Unauthorized software on endpoints but not detected by automated scan.

**Causes**:
1. Inventory not collecting software (inventory disabled or failing)
2. Software installed after last inventory cycle (timing gap)
3. Portable software not inventoried (runs from USB, not installed in registry)
4. Software name mismatch (normalized name differs between inventory and approved list)

**Solution**:

1. **Verify Inventory Collection**:
   - Check endpoint management tool: Inventory enabled? Last successful inventory date?
   - Force manual inventory on suspect device
   - Review inventory data: Is software appearing in raw inventory?
2. **Increase Inventory Frequency** (if timing gap):
   - Daily inventory instead of weekly (Section 11.1)
3. **Portable Software Detection** (advanced):
   - Use endpoint detection tools (EDR) to monitor process execution (detects portable apps)
   - Educate users: Portable apps violate policy (same as installed apps)
4. **Name Matching Review**:
   - Review normalization script (Section 11.5)
   - Manually check: Software in inventory with slightly different name than approved list?
   - Update approved list or normalization logic

**Prevention**:
- Daily inventory (detect unauthorized software within 24 hours)
- Regular inventory verification (spot-check: install test software, verify detected)

### 15.3 Pitfall: Users Frustrated by Software Restrictions

**Symptom**: Users complain software controls are too restrictive, hindering productivity.

**Causes**:
1. Approved list too narrow (common business tools missing)
2. Approval process too slow (users waiting weeks for software they need)
3. Lack of communication (users don't understand why restrictions exist)

**Solution**:

1. **Review Approved List**:
   - Gather feedback: "What software do you need that's not approved?"
   - Add commonly requested software to approved list (if security review passes)
2. **Streamline Approval Process**:
   - Meet SLA (5 business days for standard requests)
   - Expedite process for low-risk software (pre-approved categories)
   - Provide status updates to users (don't leave them in the dark)
3. **User Communication and Education**:
   - Explain rationale: "Software controls protect against malware and data breaches."
   - Provide alternatives: "Can't approve [Software]? Try [Approved Alternative]."
   - Transparent process: Publish approved software list (users can self-check)
4. **Balanced Approach**:
   - **Not too restrictive**: Allow productivity tools users need
   - **Not too permissive**: Block high-risk software (games, PUPs, pirated software)
   - **Role-based**: Developers get dev tools, everyone doesn't need AutoCAD

**Prevention**:
- Stakeholder engagement during approved list development (Section 5.5)
- Regular approved list review (quarterly) - add requested software if appropriate
- Clear communication (intranet page: "Approved Software List and Request Process")

### 15.4 Pitfall: Change Control Delays Software Deployment

**Symptom**: Approved software takes weeks to deploy due to change control bottleneck.

**Causes**:
1. CAB meets infrequently (monthly), creates delays
2. RFCs lack detail (CAB defers for more information)
3. Change control process too bureaucratic (unnecessary steps)

**Solution**:

1. **Expedited Change Process for Low-Risk Software**:
   - Standard software (Office, Chrome, approved productivity tools): Expedited approval (no CAB meeting, IT Manager approval only)
   - High-risk or organization-wide deployments: Full CAB review
2. **CAB Meeting Frequency**:
   - Weekly CAB meetings (or bi-weekly minimum)
   - Emergency CAB for urgent changes (next business day)
3. **RFC Quality**:
   - Provide RFC template (Section 13.2) - ensures all details included
   - Pre-CAB review (IT Ops reviews RFC, requests missing info before CAB meeting)
4. **Automation**:
   - For approved software already in list: Auto-generate RFC (minimal manual work)
   - Approval routing automation (ITSM workflow)

**Balance**: Change control should provide governance without excessive bureaucracy.

---

## 16. Integration with Other Controls

### 16.1 Integration with A.8.7 (Protection Against Malware)

**Connection**: Software controls prevent malware installation (malicious software is unauthorized software).

**Integration Points**:
- **Application Control**: Blocks execution of unsigned/untrusted software (malware often unsigned)
- **Approved Software List**: Only approved software allowed (malware not on list = blocked)
- **Unauthorized Software Detection**: Malware may appear as unauthorized software in inventory
  - Detection script identifies → Malware remediation (remove + investigate)

**Combined Defense**:
1. **Application Control**: Blocks malware execution (first line of defense)
2. **Anti-Malware (A.8.7)**: Detects malware signature/behavior (second line of defense)
3. **Unauthorized Software Detection**: Identifies malware in inventory (third line of defense)

**Example**:
- User downloads malware.exe
- AppLocker blocks execution (not signed by approved publisher)
- If bypassed: Anti-malware detects and quarantines
- If still bypassed: Unauthorized software scan detects malware.exe in inventory → Remediate

### 16.2 Integration with A.8.8 (Vulnerability Management)

**Connection**: Outdated/vulnerable software = security risk.

**Integration Points**:
- **Approved Software List**: Track approved versions
- **Software Inventory**: Identify software versions across endpoints
- **Vulnerability Scanning**: Identify software with known CVEs
- **Patch Management**: Update software to address vulnerabilities

**Workflow**:
1. Vulnerability scan identifies: "Adobe Acrobat Reader DC 2020.001 has CVE-2023-12345 (Critical)"
2. Check approved list: Latest approved version is 2024.001
3. Inventory scan: 150 endpoints have 2020.001 (outdated, vulnerable)
4. **Action**: Deploy patch (update to 2024.001) via change control
5. **Verification**: Next inventory scan shows endpoints updated

**POL-S5 Requirement**: EOL software (REQ-A819-012) must be replaced or isolated.

### 16.3 Integration with A.8.18 (Use of Privileged Utility Programs)

**Connection**: Privileged utilities are software (subject to software control).

**Integration Points**:
- **Privileged Utilities in Approved List**: PowerShell, administrative tools must be approved
- **Application Control for Privileged Utilities**: Restrict access (only IT admins can execute)
- **Inventory Tracking**: Track privileged utility installation and usage

**Example**:
- PowerShell: Approved software (universal for IT admins, role-based for developers)
- AppLocker rule: PowerShell.exe allowed only for "IT Admins" security group
- Unauthorized privileged utility (e.g., Mimikatz): Blocked by AppLocker, detected in inventory → Remove

**Combined Controls**: A.8.18 focuses on *usage monitoring* of privileged utilities, A.8.19 focuses on *installation control*.

### 16.4 Integration with A.8.15 (Logging)

**Connection**: Software control events must be logged.

**Integration Points**:
- **Application Control Logs**: AppLocker logs blocked executions (Event Viewer)
- **Software Approval Logs**: Ticketing system logs approval workflow
- **Unauthorized Software Logs**: Detection script logs findings
- **SIEM Integration**: Forward logs to SIEM for centralized monitoring

**Log Forwarding**:
- Windows: Forward AppLocker events (Event ID 8004 - blocked) to SIEM
- Ticketing System: Export software approval records for audit trail
- Script Logs: Unauthorized software detection results logged to file or database → SIEM

**Correlation Rules** (SIEM):
- **Rule 1**: Multiple AppLocker blocks from same user → Alert (user attempting to bypass controls)
- **Rule 2**: Unauthorized software detected on critical server → High-priority alert
- **Rule 3**: Software approval bypassed (software deployed without approval record) → Investigate

---

## 17. Maintenance and Updates

### 17.1 Daily Maintenance Tasks

**Automated (No Manual Intervention)**:
- [ ] Software inventory collection (endpoint management tools)
- [ ] Unauthorized software detection (automated script)
- [ ] User notifications (automated email for new detections)

**Manual Review (10-15 minutes daily)**:
- [ ] Review unauthorized software report (any critical findings?)
  - High-risk unauthorized software? → Immediate remediation
- [ ] Review software approval requests (new requests to process?)
  - Assign to security reviewer if new request
- [ ] Review application control logs (any unusual blocking patterns?)
  - Multiple blocks from same software? → Investigate (false positive or policy issue)

### 17.2 Weekly Maintenance Tasks

**Every Monday** (or designated day):
- [ ] Application Control Policy Review:
  - Review AppLocker logs (Event Viewer or SIEM)
  - Identify frequently blocked software (false positives?)
  - Adjust policies if needed (add allow rules)
- [ ] Unauthorized Software Remediation Tracking:
  - Review open remediation cases (Section 12.3)
  - Follow up on overdue cases (send reminders, escalate)
  - Close resolved cases (verify software removed in inventory)
- [ ] Software Approval Workflow SLA Review:
  - Are approvals meeting 5-day SLA?
  - Bottlenecks? (security review delays, CAB backlog)
  - Expedite overdue requests

### 17.3 Monthly Maintenance Tasks

**First Week of Month**:
- [ ] Generate Software Control Metrics Report:
  - Unauthorized software detection rate (# detections / # endpoints)
  - Remediation success rate (% resolved within SLA)
  - Application control coverage (% endpoints with AppLocker enforced)
  - Software approval SLA compliance (% approved within 5 days)
  - New software approvals count
- [ ] Distribute Report: Email to stakeholders (IT Ops Manager, Security Manager)
- [ ] Review Trends:
  - Unauthorized software increasing? → Investigate (user education needed?)
  - Application control blocks increasing? → Policy too restrictive?
- [ ] Approved Software List Review:
  - Add newly approved software (from last month's approvals)
  - Remove deprecated software (no longer used, EOL)

### 17.4 Quarterly Maintenance Tasks

**Every Quarter**:
- [ ] Comprehensive Approved Software List Review:
  - Review entire list (all software still relevant?)
  - Remove unused software (inventory shows zero installs)
  - Update version approvals (new versions available?)
  - License review (utilization vs. owned licenses)
- [ ] Application Control Policy Audit:
  - Review all AppLocker/Gatekeeper/MDM policies
  - Ensure policies align with approved software list
  - Remove obsolete rules
- [ ] User Feedback Collection:
  - Survey users: "Are software controls too restrictive? Missing needed software?"
  - Incorporate feedback into approved list
- [ ] Vulnerability Review:
  - Cross-reference approved software with vulnerability databases
  - Identify high-risk software (frequent CVEs)
  - Consider alternatives or enhanced monitoring

### 17.5 Annual Maintenance Tasks

**Every Year**:
- [ ] Policy Review: Review POL-S5 (Software Installation Requirements)
  - Requirements still appropriate?
  - Update based on lessons learned
- [ ] Process Effectiveness Review:
  - Is approval workflow effective? (SLA compliance, user satisfaction)
  - Is application control reducing unauthorized software? (metrics analysis)
  - Continuous improvement opportunities
- [ ] Technology Refresh:
  - Are current tools (AppLocker, inventory tools) still optimal?
  - New technologies available? (e.g., WDAC, next-gen inventory tools)
- [ ] Comprehensive Assessment: Full A.8.19 compliance assessment (using Assessment_3 workbook)
  - Evidence collection
  - Gap analysis
  - Remediation planning

---

## 18. Documentation Requirements

### 18.1 Software Control Documentation

**Mandatory Documentation**:
- [ ] **Approved Software List**: Excel/database with all approved software (Section 5)
- [ ] **Software Approval Records**: Ticketing system records for all approvals (Section 6)
- [ ] **Application Control Policies**: AppLocker/Gatekeeper/MDM policy configurations (Section 7-10)
- [ ] **Unauthorized Software Reports**: Weekly/monthly reports (Section 12)
- [ ] **Remediation Tracking**: Open/closed remediation cases (Section 12.3)
- [ ] **Change Requests**: RFCs for software deployments (Section 13)
- [ ] **Monthly Metrics Reports**: Software control KPIs (Section 17.3)

### 18.2 Operational Documentation

**Runbooks**:
- Software approval workflow (step-by-step for IT staff)
- AppLocker policy creation/update procedure
- Unauthorized software remediation procedure
- Emergency software approval process (bypass for urgent needs)

### 18.3 Audit Documentation

**For ISO 27001 Audits**:
- [ ] Evidence: Software_Controls.xlsx (from Assessment Script 3)
- [ ] Policy: POL-S5 (Software Installation Requirements)
- [ ] Procedures: This document (IMP-S4)
- [ ] Sample verification: Manual testing of 20 endpoints (application control functional, only approved software)

---

## 19. Continuous Improvement

### 19.1 Metrics to Track

**Software Control Metrics**:
- **Approval Compliance**: % of software installations that are approved (target: ≥95%)
- **Unauthorized Software Rate**: # unauthorized software detections / # endpoints (target: <5%)
- **Remediation Time**: Average days from detection to removal (target: <5 days)
- **Application Control Coverage**: % of endpoints with application control enforced (target: ≥90%)
- **Approval SLA Compliance**: % of software requests approved within SLA (target: ≥90%)
- **User Satisfaction**: User survey rating of software control process (target: ≥7/10)

### 19.2 Improvement Cycle

**Quarterly Improvement Process**:

1. **Collect Metrics** (automated, monthly)
2. **Analyze Trends** (quarterly review):
   - What's improving?
   - What's declining?
3. **Identify Opportunities**:
   - Unauthorized software rate increasing → Enhanced user training needed
   - Approval SLA compliance low → Streamline workflow or add approvers
   - User satisfaction low → Review approved list, add commonly requested software
4. **Implement Improvements**: Action plan with owners and deadlines
5. **Measure Effectiveness**: Track metrics post-implementation
6. **Repeat**: Continuous improvement

---

## 20. Appendix

### 20.1 Glossary

**Approved Software List**: Catalog of software permitted for installation on organizational endpoints.

**Application Control**: Technology that allows or denies applications based on rules (AppLocker, Gatekeeper, etc.).

**Unauthorized Software**: Software installed on endpoints but not on approved software list.

**Publisher Rule**: AppLocker rule based on digital signature (code signing certificate).

**MAM (Mobile Application Management)**: Management of corporate apps on mobile devices without managing entire device (BYOD-friendly).

**Software Asset Management (SAM)**: Tracking software licenses and utilization.

### 20.2 Reference Resources

**AppLocker**:
- Microsoft Documentation: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/applocker/

**Gatekeeper (macOS)**:
- Apple Documentation: https://support.apple.com/guide/security/gatekeeper-sec5599b66df/web

**Intune**:
- Microsoft Endpoint Manager: https://endpoint.microsoft.com

**General**:
- CIS Benchmarks (application control guidance): https://www.cisecurity.org/cis-benchmarks/

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IT Operations Team | Initial software control process implementation guidance (A.8.19) |

---

**END OF DOCUMENT**
