# ISMS-IMP-A.8.1-7-18-19-S6 - Endpoint Security Assessment
## Practical Assessment Execution Guidance
### ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19

---

## Document Control

| **Attribute** | **Details** |
|---------------|-------------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S6 |
| **Document Title** | Endpoint Security Assessment |
| **Version** | 1.0 |
| **Date** | [Date] |
| **Classification** | Internal |
| **Document Owner** | Information Security Manager / ISMS Implementation Lead |
| **Status** | Active |
| **Review Cycle** | Annual |
| **Parent Document** | ISMS-POL-A.8.1-7-18-19 (Endpoint Security Framework) |
| **Related Documents** | ISMS-POL-A.8.1-7-18-19-S6 (Assessment Methodology & Evidence Framework)<br>ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process)<br>ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation)<br>ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment)<br>ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process)<br>ISMS-IMP-A.8.1-7-18-19-S5 (Privileged Utility Management) |

---

## 1. Purpose and Scope

### 1.1 Purpose

This document provides **step-by-step execution guidance** for conducting endpoint security assessments to evaluate compliance with Controls A.8.1 (User Endpoint Devices), A.8.7 (Protection Against Malware), A.8.18 (Use of Privileged Utility Programs), and A.8.19 (Installation of Software on Operational Systems).

**Assessment execution** involves:
- Planning assessment scope and timeline
- Collecting data from endpoint management tools
- Executing control-specific assessments (A.8.1, A.8.7, A.8.18, A.8.19)
- Analyzing results and calculating compliance scores
- Identifying gaps and creating remediation plans
- Generating assessment workbooks and executive dashboard
- Presenting findings to stakeholders
- Managing remediation and continuous monitoring

### 1.2 Scope

This guidance covers practical execution for:

- **Initial Assessment**: Comprehensive baseline assessment (4-5 weeks)
- **Annual Assessment**: Full re-assessment (3-4 weeks)
- **Quarterly Assessment**: Targeted assessment (1-2 weeks)
- **Continuous Monitoring**: Ongoing automated assessment
- **Incident-Driven Assessment**: Ad-hoc assessment post-incident

### 1.3 Who Should Use This Guidance

- Information Security Manager leading assessment
- Security analysts executing assessments
- IT operations staff providing data and evidence
- ISMS coordinators preparing for certification audits

### 1.4 Prerequisites

**Before Starting Assessment**:
- [ ] Policy layer complete (POL-S1 through POL-S6)
- [ ] Implementation layer complete (IMP-S1 through IMP-S5)
- [ ] Endpoint management tools operational (MDM, SCCM, Jamf, etc.)
- [ ] Anti-malware console accessible
- [ ] Software inventory tools operational
- [ ] SIEM accessible (for privileged utility logs)
- [ ] Python 3.8+ installed (for workbook generation scripts)
- [ ] Assessment team identified and trained

---

## 2. Assessment Planning (Week 0)

### 2.1 Define Assessment Scope

**Step 1: Determine Assessment Type**

| Assessment Type | Scope | Timeline | Use Case |
|-----------------|-------|----------|----------|
| **Initial Assessment** | All endpoints, all controls | 4-5 weeks | First-time implementation |
| **Annual Assessment** | All endpoints, all controls | 3-4 weeks | Annual compliance review |
| **Quarterly Assessment** | Targeted (high-risk areas) | 1-2 weeks | Quarterly monitoring |
| **Incident-Driven** | Affected endpoints only | 1-3 days | Post-incident verification |

**Decision**: This execution guide focuses on **Initial Assessment** (most comprehensive). Adapt for other types.

**Step 2: Define Endpoint Scope**

**In-Scope Endpoints** (typically):
- Corporate laptops (Windows, macOS, Linux)
- Corporate desktops (Windows, Linux)
- Corporate mobile devices (iOS, Android)
- BYOD devices (if enrolled in MDM)
- Administrative workstations

**Out-of-Scope** (document exceptions):
- Server endpoints (covered under Server Security controls)
- Network infrastructure devices (covered under Network Security controls)
- IoT devices (unless endpoint-like: tablets, kiosks)

**Document Scope Decision**:
```
Assessment Scope Document

Assessment Type: Initial Comprehensive Assessment
Assessment Period: 2026-01-13 to 2026-02-14 (5 weeks)

Endpoints In-Scope:
- All corporate Windows 10/11 laptops/desktops (~1,800 devices)
- All corporate macOS devices (~200 devices)
- All corporate mobile devices (iOS/Android) (~500 devices)
- BYOD mobile devices enrolled in MDM (~150 devices)
Total: ~2,650 endpoints

Endpoints Out-of-Scope:
- Windows/Linux servers (~300 devices) - separate server security assessment
- Network infrastructure (~50 devices) - separate network security assessment

Controls Assessed:
- A.8.1: User Endpoint Devices
- A.8.7: Protection Against Malware
- A.8.18: Use of Privileged Utility Programs
- A.8.19: Installation of Software on Operational Systems
```

### 2.2 Identify Stakeholders and Responsibilities

**Assessment Roles**:

| Role | Responsibilities | Name/Team |
|------|------------------|-----------|
| **Assessment Lead** | Overall coordination, reporting to management | Information Security Manager |
| **Assessment Analysts** | Data collection, analysis, workbook generation | Security Analyst 1, Security Analyst 2 |
| **IT Operations** | Provide data exports, evidence, technical support | IT Operations Team |
| **Endpoint Administrators** | Access to MDM/SCCM/Jamf, configuration details | Endpoint Admin Team |
| **Security Engineers** | Technical review, gap remediation planning | Security Engineering Team |
| **Executive Sponsor** | Budget approval, executive escalation | CISO |

**RACI Matrix** (example):

| Task | Assessment Lead | Analysts | IT Ops | Endpoint Admins | Security Engineers |
|------|-----------------|----------|--------|-----------------|-------------------|
| Assessment Planning | **A** | C | I | I | C |
| Data Collection | **A** | **R** | S | S | I |
| Assessment Execution | **A** | **R** | I | I | C |
| Gap Analysis | **A** | **R** | I | I | **R** |
| Reporting | **A** | **R** | I | I | C |
| Remediation Planning | I | I | C | C | **A** |

**Legend**: A = Accountable, R = Responsible, C = Consulted, I = Informed, S = Supporting

### 2.3 Create Assessment Timeline

**Example Timeline** (5-week Initial Assessment):

```
Week 0 (Pre-Assessment): Planning
├─ Mon-Tue: Define scope, identify stakeholders
├─ Wed-Thu: Schedule kickoff meeting, notify stakeholders
└─ Fri: Kickoff meeting, finalize timeline

Week 1: Discovery and Data Collection
├─ Mon-Tue: Endpoint inventory collection (MDM/SCCM/Jamf exports)
├─ Wed-Thu: Software inventory collection, privileged utility discovery
└─ Fri: Data validation, preliminary analysis

Week 2: Control-Specific Data Collection
├─ Mon: A.8.1 data (baseline compliance, encryption status)
├─ Tue: A.8.7 data (malware protection coverage, scan logs)
├─ Wed: A.8.18 data (privileged utility access, logs)
├─ Thu: A.8.19 data (approved software, unauthorized software)
└─ Fri: Evidence collection, document evidence register

Week 3: Assessment Execution
├─ Mon-Tue: Execute A.8.1 assessment procedures
├─ Wed: Execute A.8.7 assessment procedures
├─ Thu: Execute A.8.18 and A.8.19 assessment procedures
└─ Fri: Compliance scoring, initial gap identification

Week 4: Gap Analysis and Remediation Planning
├─ Mon-Tue: Gap classification (severity, risk), root cause analysis
├─ Wed-Thu: Remediation planning with IT Ops and Security Engineers
└─ Fri: Workbook generation (run Python scripts)

Week 5: Reporting and Presentation
├─ Mon-Tue: Workbook review and validation
├─ Wed: Executive dashboard preparation
├─ Thu: Present findings to management
└─ Fri: Deliver assessment artifacts, archive evidence
```

**Adjust timeline** based on organization size and assessment type.

### 2.4 Stakeholder Communication

**Kickoff Meeting Agenda**:

```
Endpoint Security Assessment Kickoff
Date: [Week 0, Friday]
Duration: 1 hour
Attendees: Assessment team, IT Ops, Endpoint Admins, Executive Sponsor

Agenda:
1. Assessment Overview (10 min)
   - Purpose: Evaluate compliance with A.8.1, A.8.7, A.8.18, A.8.19
   - Scope: 2,650 endpoints (corporate + BYOD)
   - Timeline: 5 weeks

2. Roles and Responsibilities (10 min)
   - RACI matrix walkthrough
   - Contact information

3. Data Collection Requirements (20 min)
   - Endpoint inventory exports (IT Ops)
   - Anti-malware console access (Endpoint Admins)
   - SIEM log access (Security Engineers)
   - Evidence collection procedures

4. Timeline and Milestones (10 min)
   - Week-by-week schedule
   - Key deliverables and deadlines

5. Q&A and Next Steps (10 min)

Action Items:
- IT Ops: Provide endpoint inventory exports by [Date]
- Endpoint Admins: Provide MDM/SCCM access by [Date]
- All: Review POL-S6 and IMP-S6 before Week 1
```

**User Communication** (if applicable):

```
Subject: Endpoint Security Assessment - No Action Required

Dear Team,

We are conducting an endpoint security assessment from [Start Date] to [End Date] as part of our ongoing information security program.

What this means for you:
- Your endpoint will be included in automated inventory scans
- No action required from you
- No disruption to your work
- Your privacy is protected (we assess security configurations, not personal data)

Purpose: Ensure our endpoints are secure and compliant with security standards.

Questions? Contact Information Security Team.
```

---

## 3. Data Collection Procedures (Weeks 1-2)

### 3.1 Endpoint Inventory Collection (A.8.1 Foundation)

**Objective**: Collect complete endpoint inventory for all in-scope devices.

**Data Sources**:
- Microsoft Intune (cloud-managed Windows, macOS, iOS, Android)
- SCCM/Endpoint Manager (on-premises Windows, macOS)
- Jamf Pro (macOS, iOS)
- Lansweeper or other network discovery tools
- Manual discovery (air-gapped or unmanaged devices)

**Procedure**:

**Step 1: Export from Intune**

1. **Navigate**: Microsoft Endpoint Manager Admin Center (https://endpoint.microsoft.com)
2. **Devices → All devices**
3. **Export**: Click "Export" button
4. **Save**: `Intune_Inventory_[Date].csv`

**Columns Include**: Device name, User, OS, OS version, Compliance status, Last check-in, Serial number, Manufacturer, Model

**Step 2: Export from SCCM**

1. **SCCM Console → Assets and Compliance → Overview → Devices**
2. **Home → Export → Export List**
3. **Save**: `SCCM_Inventory_[Date].csv`

**Alternative**: SQL query direct from SCCM database:
```sql
SELECT 
    Name0 AS DeviceName,
    User_Name0 AS Username,
    Operating_System_Name_and0 AS OS,
    Build01 AS OSVersion,
    AD_Site_Name0 AS ADSite,
    Last_Logon_Timestamp0 AS LastLogon
FROM v_R_System
WHERE Operating_System_Name_and0 NOT LIKE '%Server%'
ORDER BY Name0;
```

**Step 3: Export from Jamf Pro**

1. **Jamf Pro Console → Computers → Advanced Computer Search**
2. **New Search**:
   - **Criteria**: All computers
   - **Display**: Computer Name, Username, Model, OS Version, Last Inventory Update
3. **Save** → **Export** → `Jamf_Inventory_[Date].csv`

**Step 4: Consolidate and Normalize**

**Python Script** (`consolidate_inventory.py`):

```python
import pandas as pd

# Load inventory from multiple sources
intune = pd.read_csv('Intune_Inventory_2026-01-13.csv')
sccm = pd.read_csv('SCCM_Inventory_2026-01-13.csv')
jamf = pd.read_csv('Jamf_Inventory_2026-01-13.csv')

# Normalize columns (create standard schema)
intune_norm = intune.rename(columns={
    'Device name': 'DeviceName',
    'User': 'Username',
    'OS': 'OperatingSystem',
    'Last check-in': 'LastSeen'
})
intune_norm['Source'] = 'Intune'

sccm_norm = sccm.rename(columns={
    'DeviceName': 'DeviceName',
    'Username': 'Username',
    'OS': 'OperatingSystem',
    'LastLogon': 'LastSeen'
})
sccm_norm['Source'] = 'SCCM'

jamf_norm = jamf.rename(columns={
    'Computer Name': 'DeviceName',
    'Username': 'Username',
    'OS Version': 'OperatingSystem',
    'Last Inventory Update': 'LastSeen'
})
jamf_norm['Source'] = 'Jamf'

# Merge all inventories
consolidated = pd.concat([intune_norm, sccm_norm, jamf_norm], ignore_index=True)

# Remove duplicates (device may appear in multiple sources)
consolidated = consolidated.drop_duplicates(subset='DeviceName', keep='first')

# Export consolidated inventory
consolidated.to_csv('Consolidated_Inventory_2026-01-13.csv', index=False)
print(f"Consolidated inventory: {len(consolidated)} endpoints")
```

**Output**: `Consolidated_Inventory_2026-01-13.csv` with standardized columns.

### 3.2 Baseline Compliance Data Collection (A.8.1)

**Objective**: Collect endpoint baseline compliance status (OS hardening, firewall, encryption).

**Data Sources**:
- Microsoft Defender for Endpoint compliance dashboard
- Intune compliance policies status
- SCCM compliance baselines
- Jamf compliance policies
- CIS-CAT Pro (if deployed)

**Procedure**:

**Step 1: Export Compliance Data from Intune**

1. **Devices → Monitor → Device compliance**
2. **Export compliance by device**
3. **Save**: `Intune_Compliance_[Date].csv`

**Columns Include**: Device name, Compliance status, OS configuration, Firewall status, Encryption status, Policy name

**Step 2: Export from SCCM Compliance Baselines**

1. **Monitoring → Deployments → [Baseline Name]**
2. **View Status → Export**
3. **Save**: `SCCM_Baseline_Compliance_[Date].csv`

**Step 3: Merge with Consolidated Inventory**

```python
# Load compliance data
compliance = pd.read_csv('Intune_Compliance_2026-01-13.csv')

# Load consolidated inventory
inventory = pd.read_csv('Consolidated_Inventory_2026-01-13.csv')

# Merge compliance with inventory
inventory_with_compliance = inventory.merge(
    compliance[['Device name', 'Compliance status', 'Encryption status', 'Firewall status']],
    left_on='DeviceName',
    right_on='Device name',
    how='left'
)

# Export
inventory_with_compliance.to_csv('Inventory_With_Compliance_2026-01-13.csv', index=False)
```

### 3.3 Malware Protection Data Collection (A.8.7)

**Objective**: Collect malware protection coverage, agent status, scan compliance, detections.

**Data Sources**:
- Microsoft Defender for Endpoint console
- CrowdStrike Falcon console
- Third-party anti-malware console

**Procedure**:

**Step 1: Export Protection Coverage**

**Microsoft Defender** (Intune):
1. **Endpoint security → Antivirus → Windows 10 and later → Reports**
2. **Antivirus agent status** → Export
3. **Save**: `Defender_Coverage_[Date].csv`

**CrowdStrike** (API or console):
1. **Host Management → Hosts**
2. Filter: All hosts
3. Export: Device name, Agent version, Last seen, Prevention policy
4. **Save**: `CrowdStrike_Coverage_[Date].csv`

**Step 2: Export Scan Compliance Data**

**Defender**:
1. **Reports → Antivirus → Scan report**
2. Export: Devices, Last full scan date, Last quick scan date
3. **Save**: `Defender_Scans_[Date].csv`

**Step 3: Export Detection Logs** (last 90 days)

**Defender**:
1. **Incidents & alerts → Alerts**
2. Filter: Last 90 days, Severity: All
3. Export: Alert time, Device, Threat, Severity, Status
4. **Save**: `Defender_Detections_[Date].csv`

**Step 4: Consolidate Protection Data**

```python
coverage = pd.read_csv('Defender_Coverage_2026-01-13.csv')
scans = pd.read_csv('Defender_Scans_2026-01-13.csv')
detections = pd.read_csv('Defender_Detections_2026-01-13.csv')

# Merge coverage + scans
protection = coverage.merge(scans, on='Device name', how='left')

# Count detections per device
detection_counts = detections.groupby('Device').size().reset_index(name='DetectionCount')
protection = protection.merge(detection_counts, left_on='Device name', right_on='Device', how='left')
protection['DetectionCount'].fillna(0, inplace=True)

# Export
protection.to_csv('Protection_Coverage_2026-01-13.csv', index=False)
```

### 3.4 Privileged Utility Data Collection (A.8.18)

**Objective**: Collect privileged utility inventory, access controls, usage logs.

**Data Sources**:
- Software inventory (from Section 3.1)
- Active Directory groups (privileged access groups)
- Windows Event Logs (Process Creation, PowerShell logs)
- SIEM (aggregated privileged utility usage logs)
- auditd logs (Linux)

**Procedure**:

**Step 1: Identify Privileged Utilities in Software Inventory**

```python
# Load consolidated software inventory
software = pd.read_csv('Software_Inventory_2026-01-13.csv')

# Define privileged utility keywords
priv_keywords = [
    'powershell', 'cmd', 'regedit', 'mmc', 'psexec', 'wireshark',
    'terminal', 'gdb', 'windbg', 'nmap', 'tcpdump', 'mimikatz'
]

# Filter for privileged utilities
privileged_utils = software[
    software['SoftwareName'].str.lower().str.contains('|'.join(priv_keywords), na=False)
]

# Group by utility (count endpoints)
priv_util_summary = privileged_utils.groupby('SoftwareName').agg({
    'DeviceName': 'nunique'
}).rename(columns={'DeviceName': 'EndpointCount'}).reset_index()

# Export
priv_util_summary.to_csv('Privileged_Utilities_Inventory_2026-01-13.csv', index=False)
```

**Step 2: Export Privileged Access Group Membership**

```powershell
# PowerShell: Export AD group membership
$groups = @("PrivUtil-ITAdmins", "PrivUtil-SecurityAnalysts", "PrivUtil-DevOps")
$members = @()

foreach ($group in $groups) {
    Get-ADGroupMember -Identity $group | ForEach-Object {
        $members += [PSCustomObject]@{
            Group = $group
            Username = $_.SamAccountName
            Name = $_.Name
        }
    }
}

$members | Export-Csv -Path "C:\Assessment\PrivilegedAccess_Groups_2026-01-13.csv" -NoTypeInformation
```

**Step 3: Export Privileged Utility Usage Logs from SIEM**

**SIEM Query** (example - adapt to your SIEM):
```
Query: EventID=4688 AND ProcessName IN (powershell.exe, psexec.exe, regedit.exe)
Time Range: Last 30 days
Export: Timestamp, Username, ProcessName, CommandLine, Endpoint
```

**Save**: `SIEM_PrivilegedUtility_Usage_[Date].csv`

### 3.5 Software Control Data Collection (A.8.19)

**Objective**: Collect approved software list, software inventory, unauthorized software, application control status.

**Data Sources**:
- Approved software list (from Software Control Process - IMP-S4)
- Software inventory (from Section 3.1)
- AppLocker/WDAC configuration exports
- Software approval records (ticketing system)

**Procedure**:

**Step 1: Load Approved Software List**

**File**: `Approved_Software_List.xlsx` (from IMP-S4 Section 5)

**Step 2: Compare Installed Software vs. Approved List**

```python
# Load approved software
approved = pd.read_excel('Approved_Software_List.xlsx', sheet_name='Approved_Software')

# Load installed software inventory
installed = pd.read_csv('Software_Inventory_2026-01-13.csv')

# Normalize for comparison
installed['SoftwareNormalized'] = installed['SoftwareName'].str.lower().str.strip()
approved['SoftwareNormalized'] = approved['Software Name'].str.lower().str.strip()

# Identify unauthorized (in installed but not in approved)
unauthorized = installed[~installed['SoftwareNormalized'].isin(approved['SoftwareNormalized'])]

# Group by software (count devices with unauthorized software)
unauthorized_summary = unauthorized.groupby('SoftwareName').agg({
    'DeviceName': 'nunique'
}).rename(columns={'DeviceName': 'DeviceCount'}).reset_index()

# Export
unauthorized_summary.to_csv('Unauthorized_Software_2026-01-13.csv', index=False)
print(f"Unauthorized software types: {len(unauthorized_summary)}")
print(f"Total unauthorized installations: {len(unauthorized)}")
```

**Step 3: Export AppLocker Configuration**

```powershell
# Export AppLocker policy
Get-AppLockerPolicy -Effective -Xml | Out-File -FilePath "C:\Assessment\AppLocker_Policy_2026-01-13.xml"

# Get enforcement status
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections | 
    Select-Object RuleCollectionType, EnforcementMode | 
    Export-Csv -Path "C:\Assessment\AppLocker_Enforcement_2026-01-13.csv" -NoTypeInformation
```

### 3.6 Evidence Register Documentation

**Create Evidence Register** (tracking all collected evidence):

| Evidence ID | Evidence Type | Description | Related Assessment | Collection Date | Collected By | File Path |
|-------------|---------------|-------------|-------------------|-----------------|--------------|-----------|
| EVD-001 | Automated Report | Intune endpoint inventory export | A.8.1 Inventory | 2026-01-13 | Analyst1 | /evidence/Intune_Inventory_2026-01-13.csv |
| EVD-002 | Automated Report | SCCM endpoint inventory export | A.8.1 Inventory | 2026-01-13 | Analyst1 | /evidence/SCCM_Inventory_2026-01-13.csv |
| EVD-003 | Automated Report | Defender coverage report | A.8.7 Coverage | 2026-01-14 | Analyst2 | /evidence/Defender_Coverage_2026-01-13.csv |
| EVD-004 | Configuration | AppLocker policy export | A.8.19 Application Control | 2026-01-15 | Analyst2 | /evidence/AppLocker_Policy_2026-01-13.xml |
| ... | ... | ... | ... | ... | ... | ... |

**Store Evidence Register** in Excel: `Evidence_Register_2026-01-13.xlsx`

---

## 4. Assessment Execution (Week 3)

### 4.1 A.8.1 - User Endpoint Devices Assessment

**Objective**: Evaluate endpoint inventory, classification, baseline compliance, encryption, management enrollment, disposal procedures.

**Assessment Procedures**:

**Procedure 1: Inventory Completeness Assessment**

**Method**:
1. **Load Consolidated Inventory**: `Consolidated_Inventory_2026-01-13.csv`
2. **Manual Spot-Check**: Physically verify 20 random endpoints exist and are correctly inventoried
   - Verify device name, OS, user matches inventory
   - Check for devices not in inventory (discovery gap)
3. **Calculate Inventory Accuracy**:
   ```
   Inventory Accuracy = (Correct Inventory Records / Total Spot-Checked) × 100
   Target: ≥95%
   ```

**Procedure 2: Baseline Compliance Assessment**

**Method**:
1. **Load Compliance Data**: `Inventory_With_Compliance_2026-01-13.csv`
2. **Calculate Compliance Rate**:
   ```python
   compliant = inventory_with_compliance[inventory_with_compliance['Compliance status'] == 'Compliant']
   compliance_rate = (len(compliant) / len(inventory_with_compliance)) * 100
   print(f"Baseline compliance rate: {compliance_rate:.1f}%")
   ```
3. **Identify Non-Compliant Endpoints**:
   - Filter: `Compliance status != 'Compliant'`
   - Categorize by failure reason (encryption missing, firewall disabled, outdated OS, etc.)

**Target**: ≥95% compliant

**Procedure 3: Encryption Coverage Assessment**

**Method**:
1. **Calculate Encryption Coverage**:
   ```python
   encrypted = inventory_with_compliance[inventory_with_compliance['Encryption status'] == 'Encrypted']
   encryption_rate = (len(encrypted) / len(inventory_with_compliance)) * 100
   print(f"Encryption coverage: {encryption_rate:.1f}%")
   ```
2. **Identify Unencrypted Endpoints**:
   - High-priority: Laptops (mobile risk)
   - Medium-priority: Desktops (physical access risk)
   - Low-priority: Mobile devices (usually encrypted by default)

**Target**: ≥95% for laptops/desktops, ≥90% for mobile

**Procedure 4: MDM Enrollment Assessment**

**Method**:
1. **Calculate Enrollment Rate**:
   ```python
   enrolled = inventory_with_compliance[inventory_with_compliance['MDM Enrolled'] == 'Yes']
   enrollment_rate = (len(enrolled) / len(inventory_with_compliance)) * 100
   ```

**Target**: ≥95% corporate devices, ≥80% BYOD (optional enrollment)

**Procedure 5: Lost/Stolen Incident Review**

**Method**:
1. **Retrieve Incident Reports**: Last 12 months lost/stolen device incidents
2. **Verify Response**:
   - [ ] Remote wipe initiated within 24 hours?
   - [ ] Incident documented?
   - [ ] Police report filed (if required)?
3. **Acceptance**: 100% incidents properly handled

**Procedure 6: Disposal Certificate Review**

**Method**:
1. **Retrieve Disposal Records**: Last 12 months
2. **Verify**:
   - [ ] 100% disposed devices have certificate of destruction?
   - [ ] Data sanitization method documented?

**Results**: Document findings in `A81_Assessment_Results.xlsx`

### 4.2 A.8.7 - Protection Against Malware Assessment

**Objective**: Evaluate malware protection coverage, signature currency, scan compliance, detection effectiveness.

**Assessment Procedures**:

**Procedure 1: Protection Coverage Assessment**

**Method**:
1. **Load Protection Data**: `Protection_Coverage_2026-01-13.csv`
2. **Calculate Coverage**:
   ```python
   protected = protection[protection['Agent Status'] == 'Active']
   coverage_rate = (len(protected) / len(protection)) * 100
   print(f"Malware protection coverage: {coverage_rate:.1f}%")
   ```
3. **Identify Coverage Gaps**:
   - Endpoints without agent installed
   - Endpoints with inactive/outdated agent
   - Root cause: Deployment failed? Endpoint offline? User removed agent?

**Target**: ≥98% corporate, ≥80% BYOD

**Procedure 2: Signature Currency Assessment**

**Method**:
1. **Calculate Signature Currency**:
   ```python
   from datetime import datetime, timedelta
   
   # Parse signature update dates
   protection['SignatureAge'] = (datetime.now() - pd.to_datetime(protection['Last Signature Update'])).dt.days
   
   # Current signatures (updated within 24 hours)
   current_sigs = protection[protection['SignatureAge'] <= 1]
   currency_rate = (len(current_sigs) / len(protection)) * 100
   print(f"Signature currency: {currency_rate:.1f}%")
   ```

**Target**: ≥98% updated within 24 hours

**Procedure 3: Scan Compliance Assessment**

**Method**:
1. **Full Scan Compliance**:
   ```python
   # Last full scan within 7 days
   protection['DaysSinceFullScan'] = (datetime.now() - pd.to_datetime(protection['Last Full Scan'])).dt.days
   compliant_full = protection[protection['DaysSinceFullScan'] <= 7]
   full_scan_rate = (len(compliant_full) / len(protection)) * 100
   ```
2. **Quick Scan Compliance**:
   ```python
   # Last quick scan within 1 day
   protection['DaysSinceQuickScan'] = (datetime.now() - pd.to_datetime(protection['Last Quick Scan'])).dt.days
   compliant_quick = protection[protection['DaysSinceQuickScan'] <= 1]
   quick_scan_rate = (len(compliant_quick) / len(protection)) * 100
   ```

**Target**: ≥95% full scan, ≥90% quick scan

**Procedure 4: Detection Effectiveness Assessment**

**Method**:
1. **Review Detections** (last 90 days):
   - Total detections: Count
   - Successful remediations: Count (Status = "Remediated")
   - Failed remediations: Count (Status = "Failed" or "Active")
   - Remediation success rate: (Successful / Total) × 100

**Target**: ≥95% remediation success rate

**Procedure 5: User Awareness Assessment**

**Method**:
1. **Training Completion**:
   - Retrieve training records (LMS export)
   - Calculate: (Users completed training / Total users) × 100
2. **Phishing Simulation Results**:
   - Retrieve quarterly phishing sim results
   - Click rate: (Users clicked / Total targeted) × 100

**Target**: ≥98% training completed, <10% phishing click rate

**Results**: Document findings in `A87_Assessment_Results.xlsx`

### 4.3 A.8.18 - Use of Privileged Utility Programs Assessment

**Objective**: Evaluate privileged utility inventory, access controls, approvals, MFA, logging, SIEM integration.

**Assessment Procedures**:

**Procedure 1: Inventory Completeness Assessment**

**Method**:
1. **Load Privileged Utility Inventory**: `Privileged_Utilities_Inventory_2026-01-13.csv`
2. **Manual Spot-Check**: Check 20 random endpoints for undiscovered privileged utilities
   - Common locations: `C:\Windows\System32\`, `/usr/bin/`, `/Applications/Utilities/`
3. **Calculate Inventory Accuracy**:
   ```
   Accuracy = (Correctly Inventoried / Total Found) × 100
   ```

**Target**: ≥90% accuracy

**Procedure 2: Access Control Assessment**

**Method**:
1. **Review Access Control Configuration**:
   - AppLocker policies: `AppLocker_Policy_2026-01-13.xml`
   - File permissions: Spot-check sample utilities
2. **Testing**: Attempt to execute privileged utility as unauthorized user
   - Expected: Access denied (blocked)
   - If not blocked: Access control gap

**Target**: 100% of privileged utilities have access controls configured

**Procedure 3: Approval Workflow Assessment**

**Method**:
1. **Review Access Approvals**: `PrivilegedAccess_Groups_2026-01-13.csv`
2. **Sample 20 users** with privileged access
3. **Verify**:
   - [ ] Documented approval exists?
   - [ ] Approver is appropriate authority (Security Manager, CISO)?
   - [ ] Business justification documented?

**Target**: 100% access grants have documented approval

**Procedure 4: MFA Enforcement Assessment**

**Method**:
1. **Review MFA Configuration**:
   - Azure AD Conditional Access policies
   - PAM solution MFA settings
2. **Test MFA Requirement**:
   - Attempt privileged access → MFA prompt should appear
3. **Review Authentication Logs**:
   - Sample 20 privileged sessions
   - Verify MFA used

**Target**: ≥90% of privileged access requires MFA

**Procedure 5: Logging Coverage Assessment**

**Method**:
1. **Verify Logging Configuration** (sample 20 endpoints):
   - Windows: Process creation logging (Event ID 4688), PowerShell logging (Event ID 4104)
   - Linux: auditd configured
2. **Test Logging**:
   - Execute privileged utility
   - Verify log generated

**Target**: ≥95% endpoints with logging enabled

**Procedure 6: SIEM Integration Assessment**

**Method**:
1. **Verify Log Forwarding** (sample 20 endpoints):
   - Execute privileged utility
   - Query SIEM for event (within 10 minutes)
   - Verify event appears in SIEM

**Target**: ≥95% endpoints forwarding to SIEM

**Procedure 7: Access Review Verification**

**Method**:
1. **Retrieve Quarterly Access Review Reports**: Last 4 quarters
2. **Verify**:
   - [ ] Reviews conducted quarterly?
   - [ ] Manager attestations documented?
   - [ ] Access removals implemented?

**Target**: 100% privileged access reviewed quarterly

**Results**: Document findings in `A818_Assessment_Results.xlsx`

### 4.4 A.8.19 - Installation of Software Assessment

**Objective**: Evaluate approved software list, approval process, unauthorized software detection, application control deployment.

**Assessment Procedures**:

**Procedure 1: Approved Software List Assessment**

**Method**:
1. **Review Approved Software List**: `Approved_Software_List.xlsx`
2. **Verify**:
   - [ ] List complete (includes all commonly used software)?
   - [ ] List current (reviewed within last 12 months)?
   - [ ] Obsolete software removed?

**Target**: Approved list exists and reviewed within 12 months

**Procedure 2: Approval Process Compliance Assessment**

**Method**:
1. **Sample 20 recent software approvals** (from ticketing system)
2. **Verify Each Approval**:
   - [ ] Security review documented?
   - [ ] Vulnerability assessment completed?
   - [ ] Business justification documented?
   - [ ] Approved by appropriate authority?

**Target**: 100% of new software has documented approval

**Procedure 3: Unauthorized Software Detection Assessment**

**Method**:
1. **Load Unauthorized Software Report**: `Unauthorized_Software_2026-01-13.csv`
2. **Calculate Unauthorized Software Rate**:
   ```python
   total_software_installations = len(installed)
   unauthorized_installations = len(unauthorized)
   unauthorized_rate = (unauthorized_installations / total_software_installations) * 100
   print(f"Unauthorized software rate: {unauthorized_rate:.2f}%")
   ```
3. **Verify Detection Process**:
   - [ ] Daily automated scans running?
   - [ ] Remediation within 24 hours (high-risk)?

**Target**: <1% unauthorized software, daily scans, 100% remediated within SLA

**Procedure 4: Application Control Deployment Assessment**

**Method**:
1. **Review AppLocker Configuration**: `AppLocker_Enforcement_2026-01-13.csv`
2. **Calculate Deployment Coverage**:
   ```python
   endpoints_with_applocker = inventory[inventory['AppLocker Enabled'] == 'Yes']
   deployment_rate = (len(endpoints_with_applocker) / len(inventory)) * 100
   ```
3. **Verify Enforcement Mode** (not just audit):
   - AppLocker policy: EnforcementMode = "Enabled" (not "AuditOnly")
4. **Test Application Control**:
   - Attempt to execute unauthorized software
   - Expected: Blocked

**Target**: ≥90% endpoints with application control in enforcement mode

**Procedure 5: Change Control Integration Assessment**

**Method**:
1. **Sample 20 recent software installations**
2. **Verify**:
   - [ ] Change ticket exists?
   - [ ] Testing documented?
   - [ ] Rollback plan documented?

**Target**: 100% software installations via change control

**Results**: Document findings in `A819_Assessment_Results.xlsx`

---

## 5. Gap Analysis and Remediation Planning (Week 4)

### 5.1 Gap Identification and Classification

**Step 1: Consolidate Assessment Findings**

**Create Master Gap List** (`Gaps_Master_List.xlsx`):

| Gap ID | Control | Gap Description | Affected Endpoints | Severity | Risk | Root Cause | Remediation Owner |
|--------|---------|-----------------|-------------------|----------|------|------------|-------------------|
| GAP-001 | A.8.1 | 120 endpoints unencrypted | 120 laptops (5%) | High | Data theft if lost/stolen | BitLocker not deployed to pilot group | IT Operations |
| GAP-002 | A.8.7 | 45 endpoints without malware protection | 45 desktops (2%) | Critical | Malware infection risk | Agent deployment failed, endpoints offline | Endpoint Admins |
| GAP-003 | A.8.18 | PsExec access not restricted | All endpoints with PsExec | High | Unauthorized remote execution | AppLocker rule missing | Security Engineers |
| GAP-004 | A.8.19 | 15 endpoints with unauthorized software | 15 workstations (<1%) | Medium | Policy violation, potential malware | User-installed software, detection delay | IT Operations |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Step 2: Classify Gap Severity**

**Severity Criteria** (per POL-S6 Section 6.1):

| Severity | Definition | Remediation SLA |
|----------|------------|-----------------|
| **Critical** | Complete control failure on high-criticality endpoint, multiple control failures creating critical risk | 7 days |
| **High** | Single critical control failure, widespread non-compliance | 30 days |
| **Medium** | Single control failure on standard endpoint, partial compliance | 60 days |
| **Low** | Minor deviation, low-risk non-compliance | 90 days |

**Example Classification**:
- GAP-002 (45 unprotected endpoints): **Critical** (complete malware protection failure, significant endpoint count)
- GAP-001 (120 unencrypted laptops): **High** (encryption failure, widespread)
- GAP-004 (15 unauthorized software): **Medium** (small count, limited risk)

**Step 3: Prioritize Gaps**

**Prioritization Factors**:
1. Severity (Critical > High > Medium > Low)
2. Affected endpoint count (more affected = higher priority)
3. Ease of remediation (quick wins prioritized for early progress)
4. Risk (likelihood × impact)

**Prioritized Gap List**:
1. GAP-002 (Critical, 45 endpoints, malware protection gap)
2. GAP-001 (High, 120 endpoints, encryption gap)
3. GAP-003 (High, all endpoints with PsExec, access control gap)
4. GAP-004 (Medium, 15 endpoints, unauthorized software)

### 5.2 Remediation Planning

**For Each Gap, Create Remediation Plan**:

**Example Remediation Plan** (GAP-002: Malware Protection Gap):

```
Gap ID: GAP-002
Gap Description: 45 endpoints without malware protection (agent not installed or inactive)
Severity: Critical
Remediation SLA: 7 days (by 2026-01-20)

Root Cause Analysis:
- 30 endpoints: Agent deployment failed (installation error)
- 15 endpoints: Endpoints offline during deployment (not reachable)

Remediation Approach:
1. Re-attempt agent deployment to 30 failed endpoints (via SCCM)
   - Verify prerequisites (disk space, permissions)
   - Use manual installation script if automated deployment fails
2. Identify 15 offline endpoints
   - Email users to power on and connect to network
   - Deploy agent on next network connection
3. Verify agent installation and activation

Timeline:
- Day 1-2: Re-attempt deployment to 30 endpoints
- Day 3-4: Contact users of 15 offline endpoints
- Day 5: Deploy to endpoints as they come online
- Day 6: Verify deployment (all 45 endpoints protected)
- Day 7: Close gap if verified

Resources Required:
- Endpoint Admins: 8 hours (deployment testing, troubleshooting)
- Help Desk: 2 hours (user communication)

Success Criteria:
- ≥43 of 45 endpoints protected (≥95% success rate)
- Remaining endpoints documented as exceptions (if offline for extended period)

Verification Method:
- Re-run A.8.7 coverage assessment
- Verify 43+ endpoints show "Agent Active" status

Remediation Owner: Endpoint Admin Team Lead
```

**Create Remediation Plan for All Gaps** (prioritized order).

### 5.3 Remediation Tracking

**Track Remediation Progress** (`Remediation_Tracking.xlsx`):

| Gap ID | Severity | Remediation Owner | SLA Date | Status | Progress % | Blockers | Last Updated |
|--------|----------|-------------------|----------|--------|------------|----------|--------------|
| GAP-002 | Critical | Endpoint Admins | 2026-01-20 | In Progress | 70% | 13 endpoints still offline | 2026-01-18 |
| GAP-001 | High | IT Operations | 2026-02-13 | Not Started | 0% | Awaiting BitLocker licenses | 2026-01-15 |
| GAP-003 | High | Security Engineers | 2026-02-13 | In Progress | 50% | AppLocker policy created, testing | 2026-01-17 |
| GAP-004 | Medium | IT Operations | 2026-03-15 | Planned | 0% | N/A | 2026-01-15 |

**Status Values**:
- Not Started: Remediation not yet begun
- Planned: Remediation plan created, scheduled
- In Progress: Remediation actively underway
- Blocked: Remediation stalled due to blocker
- Completed: Remediation complete, pending verification
- Verified: Gap closed, verified by security team
- Closed: Gap officially closed

**Weekly Status Updates**: Remediation owners provide weekly updates to Information Security Manager.

---

## 6. Workbook Generation and Reporting (Week 4-5)

### 6.1 Generate Assessment Workbooks

**Python Scripts** (located in `50_scripts-excel/`):

**Script 1**: `generate_assessment_1_endpoint_inventory.py`

**Run**:
```bash
python generate_assessment_1_endpoint_inventory.py
```

**Inputs**: `Inventory_With_Compliance_2026-01-13.csv`, assessment results

**Output**: `Endpoint_Inventory.xlsx` (9 worksheets)

**Script 2**: `generate_assessment_2_protection_coverage.py`

**Run**:
```bash
python generate_assessment_2_protection_coverage.py
```

**Inputs**: `Protection_Coverage_2026-01-13.csv`, detection data, scan data

**Output**: `Protection_Coverage.xlsx` (11 worksheets)

**Script 3**: `generate_assessment_3_software_controls.py`

**Run**:
```bash
python generate_assessment_3_software_controls.py
```

**Inputs**: `Approved_Software_List.xlsx`, `Unauthorized_Software_2026-01-13.csv`, AppLocker config

**Output**: `Software_Controls.xlsx` (10 worksheets)

**Script 4**: `generate_assessment_4_privileged_utilities.py`

**Run**:
```bash
python generate_assessment_4_privileged_utilities.py
```

**Inputs**: `Privileged_Utilities_Inventory_2026-01-13.csv`, access group membership, SIEM logs

**Output**: `Privileged_Utilities.xlsx` (9 worksheets)

**Script 5**: `generate_assessment_5_compliance_matrix.py`

**Run**:
```bash
python generate_assessment_5_compliance_matrix.py
```

**Inputs**: All assessment workbooks (1-4), gap analysis

**Output**: `Compliance_Matrix.xlsx` (master compliance matrix across all 4 controls)

**Script 6**: `generate_assessment_6_dashboard.py`

**Run**:
```bash
python generate_assessment_6_dashboard.py
```

**Inputs**: All assessment workbooks (1-5)

**Output**: `Executive_Dashboard.xlsx` (executive summary, charts, KPIs)

### 6.2 Workbook Review and Validation

**Quality Checks** (before presenting to management):

- [ ] **Data Accuracy**: Spot-check sample data in workbooks vs. source data
- [ ] **Formula Validation**: Verify calculated fields (compliance rates, coverage %) are correct
- [ ] **Conditional Formatting**: Verify color coding works (red/yellow/green thresholds)
- [ ] **Charts**: Verify charts display correctly, data labels accurate
- [ ] **Evidence Register**: Verify all evidence documented with correct file paths
- [ ] **UTF-8 Encoding**: Verify no broken characters (especially in workbook scripts)

**Review Session**: Assessment Lead + Analysts review all workbooks together (2-hour session).

### 6.3 Executive Dashboard Preparation

**Executive Dashboard Contents**:

**Page 1: Overall Compliance Summary**
- Overall Endpoint Security Score: X% (Green/Yellow/Red indicator)
- Per-Control Scores: A.8.1: X%, A.8.7: X%, A.8.18: X%, A.8.19: X%
- Compliance Status: Compliant / Partial / Non-Compliant
- Total Endpoints Assessed: X,XXX
- Assessment Period: YYYY-MM-DD to YYYY-MM-DD

**Page 2: Key Findings**
- Critical Gaps: Count, summary
- High Gaps: Count, summary
- Top 5 Risks: Prioritized list

**Page 3: Remediation Status**
- Gaps by Severity: Chart (Critical/High/Medium/Low counts)
- Remediation Progress: Chart (Not Started / In Progress / Completed)
- SLA Compliance: X% of gaps on track

**Page 4: Trend Analysis** (if historical data available)
- Compliance score trend (vs. previous assessment)
- Gap count trend (improving or degrading?)

**Page 5: Recommendations**
- Top 3 Immediate Actions
- Long-Term Improvements

---

## 7. Presentation to Management (Week 5)

### 7.1 Presentation Preparation

**Presentation Agenda** (45 minutes):

```
Endpoint Security Assessment Results Presentation
Date: [Week 5, Thursday]
Audience: CISO, IT Operations Manager, Endpoint Admins, Executive Sponsor

Agenda:
1. Assessment Overview (5 min)
   - Scope: 2,650 endpoints, 4 controls (A.8.1, A.8.7, A.8.18, A.8.19)
   - Timeline: 5 weeks
   - Assessment methodology

2. Overall Compliance Summary (10 min)
   - Endpoint Security Score: X%
   - Per-control breakdown (A.8.1: X%, A.8.7: X%, etc.)
   - Compliance status

3. Key Findings (15 min)
   - Critical gaps (detail)
   - High gaps (summary)
   - Positive findings (what's working well)

4. Remediation Plan (10 min)
   - Prioritized gaps
   - Remediation timelines
   - Resource requirements
   - Budget implications (if any)

5. Recommendations and Next Steps (5 min)
   - Immediate actions (next 30 days)
   - Long-term improvements
   - Continuous monitoring approach

6. Q&A (10 min)
```

**Presentation Slides** (PowerPoint):

**Slide 1**: Title
- Endpoint Security Assessment Results
- Assessment Period: [Dates]
- Presented by: [Information Security Manager]

**Slide 2**: Assessment Overview
- Scope: 2,650 endpoints across Windows, macOS, mobile
- Controls assessed: A.8.1, A.8.7, A.8.18, A.8.19
- Assessment duration: 5 weeks
- Assessment team: [Names]

**Slide 3**: Overall Compliance Score
- **Large Number**: 87% (example - Yellow status)
- Status: Partial Compliance (70-89%)
- Target: 90% (Compliant)
- Chart: Gauge chart showing 87% of 90% target

**Slide 4**: Per-Control Compliance
| Control | Score | Status |
|---------|-------|--------|
| A.8.1 - Endpoint Devices | 92% | 🟢 Compliant |
| A.8.7 - Malware Protection | 85% | 🟡 Partial |
| A.8.18 - Privileged Utilities | 78% | 🟡 Partial |
| A.8.19 - Software Controls | 93% | 🟢 Compliant |

**Slide 5**: Critical Gaps (Detail)
- **GAP-002**: 45 endpoints without malware protection
  - Impact: Critical malware infection risk
  - Root Cause: Agent deployment failures
  - Remediation: In progress, 70% complete, SLA: 7 days
- **GAP-XXX**: [Additional critical gaps]

**Slide 6**: High Gaps (Summary)
- GAP-001: 120 unencrypted laptops (data theft risk)
- GAP-003: PsExec access not restricted (unauthorized access risk)
- Total High Gaps: 3
- Remediation SLA: 30 days

**Slide 7**: Positive Findings
- ✅ Software control (A.8.19) at 93% compliance
- ✅ Endpoint inventory (A.8.1) complete and accurate
- ✅ Unauthorized software rate <1% (excellent)

**Slide 8**: Remediation Plan
- Critical gaps: 2 (target: 100% closed within 7 days)
- High gaps: 3 (target: 100% closed within 30 days)
- Medium gaps: 8 (target: 90% closed within 60 days)
- Resource requirements: Endpoint Admin team (40 hours), Budget: $XX,XXX (BitLocker licenses)

**Slide 9**: Recommendations
**Immediate Actions** (next 30 days):
1. Complete malware protection deployment (GAP-002)
2. Deploy BitLocker to 120 unencrypted laptops (GAP-001)
3. Implement AppLocker rule for PsExec restriction (GAP-003)

**Long-Term Improvements**:
1. Implement continuous monitoring (daily compliance scans)
2. Automate remediation workflows (auto-deploy agents to new endpoints)
3. Quarterly assessment cadence

**Slide 10**: Next Steps
- Week 6-12: Execute remediation plans
- Week 13: Verification assessment (confirm gaps closed)
- Ongoing: Continuous monitoring (monthly metrics reports)

### 7.2 Presentation Delivery

**Presenter Tips**:
- **Start with big picture**: Overall score, compliance status
- **Focus on business impact**: What does 87% compliance mean for the organization?
- **Be honest about gaps**: Don't downplay critical issues
- **Present solutions, not just problems**: Every gap has a remediation plan
- **Manage expectations**: Realistic timelines, resource requirements
- **Invite questions throughout**: Encourage engagement

**Handling Tough Questions**:

**Q**: "Why are we only at 87%? I thought we had good security?"
**A**: "87% is a solid baseline. The 13% gap is primarily due to 2 critical issues we've already identified and are actively remediating. With targeted efforts over the next 30 days, we expect to reach 90%+."

**Q**: "How much will remediation cost?"
**A**: "Most gaps can be remediated with existing resources. The main budget item is BitLocker licenses for 120 laptops, estimated at $X,XXX. All other remediation is operational effort."

**Q**: "How do we compare to industry standards?"
**A**: "87% compliance is above average for initial assessments. Industry benchmarks for mature programs are 90-95%. We're on track to reach that within 6 months."

---

## 8. Continuous Monitoring (Ongoing)

### 8.1 Daily Monitoring Activities

**Automated** (no manual intervention):
- [ ] Software inventory collection (Intune, SCCM, Jamf)
- [ ] Malware protection coverage scan (anti-malware console)
- [ ] Unauthorized software detection (compare inventory vs. approved list)
- [ ] SIEM alert monitoring (privileged utility usage anomalies)

**Manual Review** (10 minutes daily):
- [ ] Review SIEM alerts (unauthorized privileged utility usage)
- [ ] Review malware detection reports (new infections?)
- [ ] Review unauthorized software alerts (new detections?)

### 8.2 Weekly Monitoring Activities

**Every Monday** (30 minutes):
- [ ] Baseline compliance scan (Intune compliance policies)
- [ ] Malware signature currency check (% endpoints with current signatures)
- [ ] Remediation progress review (update `Remediation_Tracking.xlsx`)

**Outputs**:
- Weekly status email to CISO (compliance metrics, remediation progress)

### 8.3 Monthly Monitoring Activities

**First Week of Month** (2 hours):
- [ ] Generate comprehensive metrics report:
  - A.8.1: Inventory completeness, baseline compliance, encryption coverage
  - A.8.7: Malware protection coverage, scan compliance, detection metrics
  - A.8.18: Privileged utility access reviews, logging coverage
  - A.8.19: Unauthorized software rate, application control coverage
- [ ] Analyze trends (improving or degrading vs. last month?)
- [ ] Update assessment workbooks (refresh data)

**Outputs**:
- Monthly Endpoint Security Metrics Report (PDF)
- Updated assessment workbooks (Endpoint_Inventory.xlsx, Protection_Coverage.xlsx, etc.)

### 8.4 Quarterly Re-Assessment

**Every Quarter** (1-2 weeks):
- [ ] Targeted re-assessment (high-risk areas)
- [ ] Re-run assessment procedures for controls with previous gaps
- [ ] Verify gap remediation (gaps marked "Closed" truly closed?)
- [ ] Update compliance scores
- [ ] Present quarterly results to management

**Outputs**:
- Quarterly Assessment Report
- Updated Executive Dashboard
- Gap remediation verification

---

## 9. Verification Procedures

### 9.1 Workbook Verification

**Before Delivering Workbooks to Management**:

- [ ] **Spot-Check Data Accuracy**: Sample 20 rows from each workbook, verify against source data
- [ ] **Formula Validation**: Manually calculate 5 compliance rates, verify formulas correct
- [ ] **Conditional Formatting**: Change sample data values, verify colors update correctly
- [ ] **Chart Verification**: Check charts display correct data, labels accurate
- [ ] **Evidence Register Completeness**: All evidence rows have file paths, collection dates
- [ ] **UTF-8 Encoding**: Open workbooks, visually scan for broken characters (✅❌ vs. garbled)

### 9.2 Assessment Results Verification

**Verification Method**: Independent review by second analyst.

**Procedure**:
1. **Select 20 random endpoints**
2. **Manually verify assessment results**:
   - A.8.1: Is endpoint inventory correct? Is baseline compliance accurate?
   - A.8.7: Is malware protection status correct? Signatures current?
   - A.8.18: Does endpoint have privileged utilities? Are access controls configured?
   - A.8.19: Is software inventory accurate? Unauthorized software detected?
3. **Compare manual verification to assessment workbook data**
4. **Acceptance**: ≥95% accuracy (19 of 20 correct)

---

## 10. Common Pitfalls and Troubleshooting

### 10.1 Pitfall: Assessment Data Collection Incomplete

**Symptom**: Assessment cannot proceed due to missing data (inventory exports unavailable, console access denied).

**Causes**:
1. IT Ops or Endpoint Admins not engaged early enough
2. Access permissions not granted to assessment team
3. Tools not operational (MDM offline, SIEM not collecting logs)

**Solution**:
1. **Engage Stakeholders Early**: Kickoff meeting Week 0, confirm data access
2. **Pre-Assessment Access Verification**: Test access to all tools before Week 1
3. **Escalation Path**: If access not granted, escalate to CISO immediately (don't wait)

**Prevention**: Include data access checklist in kickoff meeting agenda.

### 10.2 Pitfall: Assessment Timeline Slips

**Symptom**: Assessment exceeds planned 5-week timeline.

**Causes**:
1. Data collection delays (waiting for IT Ops to provide exports)
2. Scope creep (additional controls added mid-assessment)
3. Assessment team capacity (analysts pulled to other priorities)

**Solution**:
1. **Strict Scope Management**: Define scope in Week 0, no changes mid-assessment
2. **Weekly Status Meetings**: Track progress, identify delays early, escalate blockers
3. **Buffer Time**: Build 1-week buffer into timeline for unexpected delays

**Prevention**: Executive sponsor approval of scope and timeline before starting.

### 10.3 Pitfall: Gap Remediation Not Prioritized

**Symptom**: Critical gaps remain open past SLA, remediation progress stalls.

**Causes**:
1. Remediation owners (IT Ops, Endpoint Admins) have other priorities
2. Executive sponsor not engaged in remediation tracking
3. No consequences for missing SLAs

**Solution**:
1. **Executive Accountability**: CISO tracks critical gaps weekly, escalates overdue gaps to CIO
2. **Remediation SLA Tracking**: Automated alerts when gap approaches SLA (48 hours before deadline)
3. **Resource Allocation**: Executive sponsor ensures remediation owners have capacity

**Prevention**: Include remediation commitment in assessment presentation to management.

---

## 11. Documentation Requirements

**Mandatory Documentation** (archive after assessment):

- [ ] **Assessment Scope Document**: Scope, timeline, stakeholders
- [ ] **Evidence Register**: All evidence with file paths (`Evidence_Register_2026-01-13.xlsx`)
- [ ] **Raw Data Exports**: Inventory, compliance, protection, software, logs (all CSV/JSON files)
- [ ] **Assessment Workbooks**: Endpoint_Inventory.xlsx, Protection_Coverage.xlsx, Software_Controls.xlsx, Privileged_Utilities.xlsx, Compliance_Matrix.xlsx
- [ ] **Executive Dashboard**: Executive_Dashboard.xlsx
- [ ] **Gap Analysis**: Gaps_Master_List.xlsx, Remediation_Tracking.xlsx
- [ ] **Presentation Materials**: PowerPoint slides, presentation notes
- [ ] **Assessment Report**: Written report summarizing findings (PDF)

**Storage**:
- Evidence Folder: `\\fileserver\ISMS\Assessments\2026-01_Endpoint_Security\`
- Retention: 3 years (for trend analysis, audit purposes)

---

## 12. Appendix

### 12.1 Glossary

**Assessment**: Systematic evaluation of endpoint security controls against policy requirements.

**Gap**: Deviation from policy requirement, control failure, non-compliance.

**Remediation**: Actions taken to close gaps, achieve compliance.

**Continuous Monitoring**: Ongoing automated assessment to detect configuration drift, new gaps.

**Compliance Score**: Quantitative measure of control implementation effectiveness (0-100%).

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Team | Initial endpoint security assessment execution guidance |

---

**END OF DOCUMENT**