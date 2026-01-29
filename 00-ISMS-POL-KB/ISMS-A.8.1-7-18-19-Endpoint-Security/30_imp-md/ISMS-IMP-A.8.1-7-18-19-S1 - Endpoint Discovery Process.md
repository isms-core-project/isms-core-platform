# ISMS-IMP-A.8.1-7-18-19-S1 - Endpoint Discovery Process
## Practical Implementation Guidance for Comprehensive Endpoint Inventory
### ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19: Endpoint Security Framework

---

## Document Control

| Attribute | Details |
|-----------|---------|
| Document ID | ISMS-IMP-A.8.1-7-18-19-S1 |
| Document Title | Endpoint Discovery Process |
| Version | 1.0 |
| Date | [Date] |
| Classification | Internal |
| Document Owner | [Organization] Endpoint Security Team |
| Status | Active |
| Review Cycle | Annual |
| Parent Document | ISMS-POL-A.8.1-7-18-19-S6 (Assessment Framework) |
| Related Documents | ISMS-POL-A.8.1-7-18-19-S2 (Endpoint Devices Requirements - A.8.1)<br>ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation)<br>ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment) |

---

## 1. Purpose and Scope

### 1.1 Purpose
This document provides practical, step-by-step guidance for discovering and inventorying ALL endpoint devices across [Organization]'s environment. Complete endpoint inventory is the foundational requirement for ISO 27001:2022 Control A.8.1 (User Endpoint Devices) and enables assessment of Controls A.8.7 (Malware Protection), A.8.18 (Privileged Utilities), and A.8.19 (Software Installation).

**Critical Principle**: *You cannot protect what you cannot see. Endpoint discovery must achieve ≥95% coverage to support effective security controls.*

### 1.2 Scope
This guidance covers discovery of:
- **User Endpoints**: Laptops, desktops, tablets, smartphones, thin clients
- **Operating Systems**: Windows, macOS, Linux, iOS, Android, ChromeOS
- **Ownership Models**: Corporate-owned, BYOD (Bring Your Own Device), contractor devices, guest devices
- **Network Locations**: On-premises, remote/home, mobile, branch offices
- **Special Cases**: Air-gapped devices, IoT endpoints, kiosks, lab/test devices

### 1.3 Target Audience
- Endpoint administrators and security engineers
- MDM/UEM platform administrators
- ISMS assessment teams
- Security assessors and auditors
- IT asset management teams

### 1.4 Prerequisites
- **Access Requirements**:
  - Administrator access to MDM/UEM platforms (Intune, Jamf, SCCM, etc.)
  - Network administrator access (for network-based discovery)
  - Active Directory/Azure AD read access
  - Cloud platform access (Azure, AWS, GCP if endpoints hosted in cloud)
- **Authorization**:
  - Documented approval for network scanning activities
  - Authorization to access endpoint management systems
  - Privacy approval for BYOD device discovery (where applicable)
- **Knowledge**:
  - Understanding of endpoint management technologies
  - Familiarity with PowerShell, Bash, or Python for scripting
  - Basic networking knowledge (IP addressing, DNS, DHCP)

---

## 2. Overview and Prerequisites

### 2.1 Process Overview
Endpoint discovery follows a **five-phase approach**:

```
Phase 1: Planning & Scoping
   ↓
Phase 2: Automated Discovery (MDM, AD, network scanning)
   ↓
Phase 3: Manual Discovery (surveys, documentation review)
   ↓
Phase 4: Data Consolidation & Deduplication
   ↓
Phase 5: Classification & Validation
```

**Key Success Metrics**:
- **Coverage Rate**: ≥95% of expected endpoints discovered
- **Data Quality**: <5% duplicate records after deduplication
- **Currency**: Inventory updated within 24 hours of device changes

### 2.2 Discovery Methods Matrix

| Method | Coverage | Accuracy | Effort | Recommended For |
|--------|----------|----------|--------|-----------------|
| **MDM/UEM Export** | High (managed devices only) | Very High | Low | Primary discovery method |
| **Active Directory Query** | High (domain-joined only) | High | Low | Windows endpoints |
| **Network Scanning** | Very High (all networked devices) | Medium | Medium | Gap coverage, validation |
| **DHCP Lease Analysis** | High (DHCP clients) | Medium | Low | Quick discovery |
| **User Surveys** | Medium (self-reporting) | Low | High | BYOD, unmanaged devices |
| **Cloud Platform APIs** | High (cloud VMs) | Very High | Low | Cloud-hosted endpoints |

### 2.3 Key Principles
- **Multi-Method Approach**: No single discovery method achieves 100% coverage - combine multiple approaches
- **Continuous Discovery**: Inventory is never "complete" - implement ongoing discovery processes
- **Privacy-Aware**: BYOD discovery must respect employee privacy and comply with regulations (GDPR, etc.)
- **Technology-Agnostic**: Process works regardless of MDM platform, OS mix, or environment
- **Validate, Don't Trust**: Cross-reference multiple sources to ensure accuracy

### 2.4 Timeline
- **Initial Discovery** (comprehensive, first time): 3-4 weeks
- **Periodic Discovery** (quarterly full scan): 1 week
- **Continuous Discovery** (automated daily updates): Ongoing

---

## 3. Automated Discovery Methods

### 3.1 MDM/UEM Platform Discovery

#### 3.1.1 Microsoft Intune Discovery

**Use Case**: Discover all devices enrolled in Microsoft Intune (Windows, macOS, iOS, Android)

**Step-by-Step Procedure**:

1. **Access Intune Portal**:
   - Navigate to https://endpoint.microsoft.com
   - Sign in with Global Administrator or Intune Administrator credentials

2. **Export All Devices**:
   - Go to: **Devices** → **All devices**
   - Click **Export** (top toolbar)
   - Wait for export to complete (may take several minutes for large environments)
   - Download CSV file

3. **Export Data Fields** (verify your export includes):
   - Device name
   - Operating system
   - OS version
   - Last check-in date
   - Compliance status
   - Ownership (Corporate, Personal)
   - Serial number
   - IMEI/MEID (mobile devices)
   - Primary user (UPN)
   - Enrollment date
   - Management state (Managed, Retired, etc.)

4. **Platform-Specific Exports** (if needed):
   - **Windows**: Devices → Windows → Windows devices → Export
   - **macOS**: Devices → macOS → Export
   - **iOS**: Devices → iOS → Export
   - **Android**: Devices → Android → Export

5. **Save Export**:
   - Filename convention: `Intune_All_Devices_YYYYMMDD.csv`
   - Store in evidence repository: `[EvidencePath]/Endpoint_Discovery/`

**Common Issues**:
- **Export timeout**: Large environments (>10,000 devices) may timeout → Export by platform separately
- **Stale devices**: Include devices not checked in for 90+ days → Filter later during validation
- **Duplicate entries**: Same device may appear if re-enrolled → Deduplicate using serial number

#### 3.1.2 Jamf Pro Discovery (macOS/iOS)

**Use Case**: Discover all Apple devices managed by Jamf Pro

**Step-by-Step Procedure**:

1. **Access Jamf Pro Console**:
   - Navigate to your Jamf Pro URL: `https://[your-instance].jamfcloud.com`
   - Sign in with administrator credentials

2. **Computer Inventory Export** (macOS):
   - Go to: **Computers** → **Search Inventory**
   - Create Advanced Search:
     - Display: All Computers
     - Criteria: None (or "Last Check-in: less than 365 days ago")
   - Click **Search**
   - Click **Export** (CSV or XML)

3. **Mobile Device Inventory Export** (iOS/iPadOS):
   - Go to: **Mobile Devices** → **Search Mobile Devices**
   - Create Advanced Search (similar to computers)
   - Export results

4. **Export Data Fields** (verify inclusion):
   - Computer Name / Device Name
   - Serial Number
   - MAC Address
   - IP Address
   - Operating System
   - OS Version
   - Last Check-in
   - Username
   - Department
   - Building
   - FileVault Enabled (macOS)
   - Managed Status

5. **API-Based Export** (for automation):
   ```bash
   # Jamf Pro API example (Classic API)
   curl -X GET \
     -H "Accept: application/json" \
     -u "username:password" \
     "https://[instance].jamfcloud.com/JSSResource/computers" \
     -o jamf_computers.json
   ```

6. **Save Export**:
   - Filename: `Jamf_Computers_YYYYMMDD.csv`, `Jamf_MobileDevices_YYYYMMDD.csv`
   - Store in evidence repository

#### 3.1.3 SCCM/ConfigMgr Discovery (Windows)

**Use Case**: Discover all Windows devices managed by Microsoft Endpoint Configuration Manager

**Step-by-Step Procedure**:

1. **Access SCCM Console**:
   - Launch Configuration Manager Console
   - Connect to site server

2. **Run Built-In Inventory Report**:
   - Navigate to: **Monitoring** → **Reporting** → **Reports**
   - Search for: "All Systems" or "Hardware Inventory"
   - Common reports:
     - "Computers in a specific collection" (select "All Systems")
     - "Hardware inventory by computer"

3. **Create Custom SQL Query** (for detailed export):
   ```sql
   SELECT 
       sys.Name0 AS ComputerName,
       sys.Operating_System_Name_and0 AS OS,
       sys.Resource_Domain_OR_Workgr0 AS Domain,
       sys.User_Name0 AS UserName,
       sys.Client_Version0 AS ClientVersion,
       hw.SerialNumber0 AS SerialNumber,
       hw.Manufacturer0 AS Manufacturer,
       hw.Model0 AS Model,
       net.MACAddress0 AS MACAddress,
       net.IPAddress0 AS IPAddress,
       sys.Last_Logon_Timestamp0 AS LastLogon,
       sys.Client0 AS ClientInstalled
   FROM v_R_System sys
   LEFT JOIN v_GS_COMPUTER_SYSTEM hw ON sys.ResourceID = hw.ResourceID
   LEFT JOIN v_GS_NETWORK_ADAPTER_CONFIGURATION net ON sys.ResourceID = net.ResourceID
   WHERE net.IPEnabled0 = 1
   ORDER BY sys.Name0
   ```

4. **Export Query Results**:
   - Right-click on query results → **Export** → **CSV**
   - Filename: `SCCM_All_Systems_YYYYMMDD.csv`

5. **PowerShell Alternative**:
   ```powershell
   # Connect to SCCM
   Import-Module ConfigurationManager
   Set-Location "SITECODE:\"
   
   # Get all devices
   $devices = Get-CMDevice -CollectionName "All Systems"
   
   # Export to CSV
   $devices | Select-Object Name, DeviceOS, LastActiveTime, SerialNumber, MACAddress | 
       Export-Csv -Path "SCCM_Devices.csv" -NoTypeInformation
   ```

#### 3.1.4 Google Workspace (ChromeOS, Mobile)

**Use Case**: Discover ChromeOS devices and mobile devices managed by Google Workspace

**Step-by-Step Procedure**:

1. **Access Admin Console**:
   - Navigate to: https://admin.google.com
   - Sign in with Super Admin credentials

2. **ChromeOS Devices**:
   - Go to: **Devices** → **Chrome devices**
   - Click **Download all** (top right)
   - Export format: CSV
   - Data includes: Device ID, Serial Number, OS Version, Last Sync, User, Location, Notes

3. **Mobile Devices**:
   - Go to: **Devices** → **Mobile devices**
   - Click **Download all**
   - Data includes: Device Name, Type (iOS/Android), IMEI, Phone Number, Email, Last Sync

4. **Save Exports**:
   - Filenames: `Google_ChromeOS_YYYYMMDD.csv`, `Google_Mobile_YYYYMMDD.csv`

### 3.2 Active Directory / Azure AD Query

#### 3.2.1 Active Directory Computer Objects (Windows Domain)

**Use Case**: Discover all domain-joined Windows devices

**PowerShell Procedure**:

```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Get all computer objects
$computers = Get-ADComputer -Filter * -Properties Name, OperatingSystem, 
    OperatingSystemVersion, Created, LastLogonDate, DistinguishedName, 
    Description, IPv4Address

# Export to CSV
$computers | Select-Object Name, OperatingSystem, OperatingSystemVersion, 
    Created, LastLogonDate, DistinguishedName, Description, IPv4Address |
    Export-Csv -Path "AD_Computers_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

Write-Host "Exported $($computers.Count) computer objects"
```

**Filtering Stale Objects** (not logged in for 90+ days):
```powershell
$cutoffDate = (Get-Date).AddDays(-90)
$activeComputers = Get-ADComputer -Filter {LastLogonDate -gt $cutoffDate} -Properties *
```

**Important Notes**:
- **LastLogonDate** is replicated, but may be up to 14 days old
- **Stale objects**: AD may contain decommissioned devices not yet cleaned up
- **Workstations vs. Servers**: Filter by OS if needed (`OperatingSystem -notlike "*Server*"`)

#### 3.2.2 Azure AD Device Query

**Use Case**: Discover all devices registered/joined to Azure AD (cloud + hybrid)

**PowerShell Procedure**:

```powershell
# Install Azure AD module if not present
# Install-Module AzureAD

# Connect to Azure AD
Connect-AzureAD

# Get all devices
$azureDevices = Get-AzureADDevice -All $true

# Export to CSV
$azureDevices | Select-Object DisplayName, DeviceId, DeviceOSType, 
    DeviceOSVersion, IsCompliant, IsManaged, ApproximateLastLogonTimeStamp, 
    AccountEnabled, DeviceTrustType |
    Export-Csv -Path "AzureAD_Devices_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

Write-Host "Exported $($azureDevices.Count) Azure AD devices"
```

**Device Trust Types**:
- **Azure AD Joined**: Cloud-only devices
- **Azure AD Registered**: BYOD devices
- **Hybrid Azure AD Joined**: On-premises AD + Azure AD

### 3.3 Network Scanning Discovery

#### 3.3.1 Nmap Network Scan

**Use Case**: Discover active devices on corporate networks (gap coverage, validation)

**Prerequisites**:
- Nmap installed (`sudo apt install nmap` or download from nmap.org)
- Authorization to scan networks (notify security team to whitelist scanner IP)
- Target network ranges (CIDR notation)

**Basic Scan Procedure**:

```bash
# Ping scan (discover live hosts without port scanning - least intrusive)
sudo nmap -sn 10.0.0.0/24 -oA network_scan_10.0.0

# OS detection scan (more intrusive, requires sudo)
sudo nmap -O 10.0.0.0/24 -oA network_scan_10.0.0_OS

# Aggressive scan (OS, version, script scanning - most intrusive)
sudo nmap -A 10.0.0.0/24 -oA network_scan_10.0.0_aggressive
```

**Output Formats**:
- `-oA filename`: Outputs in all formats (XML, nmap, grepable)
- Use XML output for parsing: `filename.xml`

**Parse Nmap XML to CSV** (Python example):

```python
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('network_scan.xml')
root = tree.getroot()

with open('nmap_results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['IP Address', 'Hostname', 'OS', 'MAC Address', 'Status'])
    
    for host in root.findall('host'):
        ip = host.find('address[@addrtype="ipv4"]').get('addr')
        mac = host.find('address[@addrtype="mac"]')
        mac_addr = mac.get('addr') if mac is not None else 'Unknown'
        hostname_elem = host.find('hostnames/hostname')
        hostname = hostname_elem.get('name') if hostname_elem is not None else 'Unknown'
        os_elem = host.find('os/osmatch')
        os_name = os_elem.get('name') if os_elem is not None else 'Unknown'
        status = host.find('status').get('state')
        
        writer.writerow([ip, hostname, os_name, mac_addr, status])
```

**Best Practices**:
- **Scan during off-hours**: Minimize impact on production
- **Use throttling**: `--max-rate 100` to limit packet rate
- **Scan in phases**: Don't scan entire network at once
- **Coordinate with security team**: Avoid triggering IDS/IPS alerts

#### 3.3.2 DHCP Lease Analysis

**Use Case**: Quick discovery of devices with DHCP leases (active on network recently)

**Windows DHCP Server**:

```powershell
# Export DHCP leases from Windows DHCP Server
Get-DhcpServerv4Scope | ForEach-Object {
    Get-DhcpServerv4Lease -ScopeId $_.ScopeId
} | Export-Csv -Path "DHCP_Leases_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

**Linux DHCP Server** (dhcpd):

```bash
# Parse dhcpd.leases file
grep -E "lease|hostname|hardware" /var/lib/dhcp/dhcpd.leases | 
    awk '/lease/ {ip=$2} /hostname/ {host=$2} /hardware/ {mac=$3; print ip,host,mac}'
```

**Advantages**:
- Low-effort, high-coverage for DHCP clients
- Captures recently active devices
- Includes devices that may not respond to pings

**Limitations**:
- Misses devices with static IPs
- Lease data may be stale (devices no longer on network)

### 3.4 Cloud Platform API Discovery

#### 3.4.1 Azure Virtual Machines (Cloud Endpoints)

**Use Case**: Discover Azure-hosted virtual machines that function as endpoints

**PowerShell (Azure Az Module)**:

```powershell
# Connect to Azure
Connect-AzAccount

# Get all VMs across all subscriptions
$vms = Get-AzVM -Status

# Export to CSV
$vms | Select-Object Name, ResourceGroupName, Location, 
    @{N='OS';E={$_.StorageProfile.OsDisk.OsType}}, 
    @{N='VMSize';E={$_.HardwareProfile.VmSize}}, 
    PowerState, 
    @{N='PrivateIP';E={$_.NetworkProfile.NetworkInterfaces[0].IpConfigurations[0].PrivateIpAddress}} |
    Export-Csv -Path "Azure_VMs_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

#### 3.4.2 AWS EC2 Instances (Cloud Endpoints)

**Use Case**: Discover AWS EC2 instances

**AWS CLI**:

```bash
# Get all EC2 instances across all regions
for region in $(aws ec2 describe-regions --query 'Regions[].RegionName' --output text); do
    echo "Scanning region: $region"
    aws ec2 describe-instances --region $region \
        --query 'Reservations[].Instances[].[InstanceId, InstanceType, State.Name, 
                 Platform, PrivateIpAddress, PublicIpAddress, Tags[?Key==`Name`].Value | [0]]' \
        --output text >> aws_ec2_instances.txt
done
```

**Python (boto3)**:

```python
import boto3
import csv

ec2 = boto3.client('ec2')
instances = []

# Get all regions
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

for region in regions:
    ec2_regional = boto3.client('ec2', region_name=region)
    response = ec2_regional.describe_instances()
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'Platform': instance.get('Platform', 'Linux'),
                'PrivateIP': instance.get('PrivateIpAddress', 'N/A'),
                'PublicIP': instance.get('PublicIpAddress', 'N/A'),
                'Region': region
            })

# Export to CSV
with open('aws_ec2_instances.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=instances[0].keys())
    writer.writeheader()
    writer.writerows(instances)
```

---

## 4. Manual Discovery Methods

### 4.1 User Surveys for BYOD and Unmanaged Devices

**Use Case**: Discover BYOD and personal devices used for work (email on personal phone, etc.)

**Survey Approach**:

1. **Email Survey Template**:

```
Subject: [Action Required] IT Asset Inventory - Personal Device Usage

Dear [Organization] Staff,

As part of our ongoing information security assessment, we need to understand 
all devices used to access [Organization] resources (email, files, applications).

Please complete this brief survey (5 minutes):
[Survey Link]

Survey Questions:
1. Do you use any personal devices for work purposes? (Yes/No)
2. If yes, which devices? (Check all that apply)
   - [ ] Personal smartphone (accessing work email)
   - [ ] Personal tablet
   - [ ] Personal laptop/desktop
   - [ ] Other: ___________
3. Which [Organization] resources do you access from personal devices?
   - [ ] Email (Outlook, Gmail)
   - [ ] File sharing (SharePoint, OneDrive)
   - [ ] Company applications
   - [ ] VPN
4. Device details (if comfortable sharing):
   - Device type: ___________
   - Operating system (e.g., iOS 17, Android 13, Windows 11): ___________
   - Is device enrolled in MDM/Company Portal? (Yes/No/Unsure)

Your responses are confidential and used solely for security inventory purposes.

Thank you,
[Organization] IT Team
```

2. **Survey Tools**:
   - Microsoft Forms (if using M365)
   - Google Forms (if using Google Workspace)
   - SurveyMonkey, Typeform (third-party)

3. **Follow-Up**:
   - Send reminder email after 1 week
   - Track response rate (target: >70% response rate)
   - Personal outreach to non-responders in critical roles

**Limitations**:
- Self-reporting is unreliable (users may forget or not disclose devices)
- Privacy concerns may reduce response rate
- Data quality depends on user knowledge

### 4.2 Documentation Review

**Use Case**: Discover devices documented in existing asset management systems, procurement records, or network diagrams

**Sources to Review**:

1. **Asset Management Systems (CMDB)**:
   - ServiceNow asset inventory
   - BMC Remedy CMDB
   - Jira Service Management assets
   - Extract all endpoint assets

2. **Procurement Records**:
   - Purchase orders for laptops, desktops, mobile devices
   - Leasing agreements (if devices leased)
   - Expected count vs. discovered count discrepancy analysis

3. **Network Diagrams**:
   - Visio diagrams showing endpoint distribution
   - Office floor plans with device locations
   - Data center rack diagrams (if physical endpoints in DC)

4. **IT Service Desk Tickets**:
   - Device provisioning tickets (new hires)
   - Device repair/replacement tickets
   - Device decommissioning tickets
   - Analyze trends: Are all provisioned devices in inventory?

### 4.3 Physical Site Surveys (For Special Cases)

**Use Case**: Discover air-gapped devices, kiosks, lab equipment, IoT endpoints not connected to network

**Procedure**:

1. **Schedule Site Visits**:
   - Coordinate with facility managers
   - Visit all [Organization] locations (HQ, branch offices, data centers, labs)

2. **Inventory Checklist**:
   - Device type (laptop, desktop, kiosk, etc.)
   - Serial number / asset tag
   - Location (building, floor, room)
   - Purpose (receptionist kiosk, lab workstation, etc.)
   - Network connectivity (networked, air-gapped, intermittent)
   - Ownership (corporate, contractor, research)

3. **Photo Documentation**:
   - Take photos of device asset tags
   - Photograph device configuration (if relevant for security)

4. **Common Air-Gapped Devices**:
   - Industrial control systems (SCADA endpoints)
   - Research lab workstations
   - Secure rooms / classified networks
   - Kiosks in lobbies

---

## 5. Data Consolidation and Deduplication

### 5.1 Data Normalization

**Challenge**: Different discovery sources provide data in different formats. Normalize before consolidating.

**Normalization Procedures**:

1. **Device Name Standardization**:
   - Convert to uppercase: `LAPTOP-001` (not `laptop-001` or `Laptop-001`)
   - Remove domain suffixes: `DEVICE.corp.local` → `DEVICE`
   - Trim whitespace

   **PowerShell Example**:
   ```powershell
   $normalizedName = $deviceName.ToUpper().Trim().Split('.')[0]
   ```

2. **Operating System Standardization**:
   - Map variations to standard names:
     - `Windows 10 Pro`, `Windows 10 Enterprise` → `Windows 10`
     - `macOS 14.1`, `macOS Sonoma` → `macOS Sonoma`
     - `Ubuntu 22.04.3 LTS` → `Ubuntu 22.04`
   
   **Mapping Table**:
   ```csv
   SourceOS,NormalizedOS
   "Windows 10 Pro","Windows 10"
   "Windows 10 Enterprise","Windows 10"
   "Microsoft Windows 11 Pro","Windows 11"
   "macOS 14.1","macOS Sonoma"
   "macOS 14.2","macOS Sonoma"
   ```

3. **Date Standardization**:
   - Convert all dates to ISO 8601: `YYYY-MM-DD`
   - Handle different formats from different sources:
     - `12/31/2025` → `2025-12-31`
     - `31.12.2025` → `2025-12-31`

4. **Boolean Standardization**:
   - `Yes/No`, `True/False`, `Enabled/Disabled`, `1/0` → Standardize to `Yes/No`

### 5.2 Data Consolidation

**Procedure**:

1. **Import All Discovery Exports**:
   - Intune_All_Devices.csv
   - Jamf_Computers.csv
   - SCCM_All_Systems.csv
   - AD_Computers.csv
   - Network_Scan.csv
   - DHCP_Leases.csv
   - Azure_VMs.csv
   - Survey_Responses.csv

2. **Merge into Master Inventory**:

   **Python Example** (using pandas):
   ```python
   import pandas as pd
   
   # Load all sources
   intune = pd.read_csv('Intune_All_Devices.csv')
   jamf = pd.read_csv('Jamf_Computers.csv')
   sccm = pd.read_csv('SCCM_All_Systems.csv')
   ad = pd.read_csv('AD_Computers.csv')
   
   # Normalize column names
   intune.rename(columns={'DeviceName': 'Hostname', 'OS': 'OperatingSystem'}, inplace=True)
   jamf.rename(columns={'ComputerName': 'Hostname', 'OperatingSystem': 'OperatingSystem'}, inplace=True)
   
   # Concatenate all sources
   master_inventory = pd.concat([intune, jamf, sccm, ad], ignore_index=True)
   
   # Save consolidated inventory
   master_inventory.to_csv('Master_Endpoint_Inventory_Consolidated.csv', index=False)
   ```

3. **Handle Missing Data**:
   - Not all sources provide all fields
   - Fill in gaps from multiple sources:
     - Hostname from Intune, Serial Number from Jamf, IP Address from DHCP

### 5.3 Deduplication

**Challenge**: Same device may appear multiple times from different sources

**Deduplication Strategy**:

1. **Unique Identifiers** (in order of reliability):
   - **Serial Number** (most reliable - hardware identifier)
   - **MAC Address** (reliable for networked devices)
   - **Device ID / GUID** (MDM-assigned, unique)
   - **Hostname** (least reliable - can be changed or duplicated)

2. **Deduplication Procedure**:

   **Python Example**:
   ```python
   import pandas as pd
   
   # Load consolidated inventory
   df = pd.read_csv('Master_Endpoint_Inventory_Consolidated.csv')
   
   # Remove exact duplicates
   df.drop_duplicates(inplace=True)
   
   # Deduplicate by serial number (keep first occurrence)
   df_dedup = df.drop_duplicates(subset=['SerialNumber'], keep='first')
   
   # For devices without serial number, deduplicate by hostname
   df_no_serial = df[df['SerialNumber'].isna()]
   df_no_serial_dedup = df_no_serial.drop_duplicates(subset=['Hostname'], keep='first')
   
   # Combine
   final_inventory = pd.concat([df_dedup, df_no_serial_dedup], ignore_index=True)
   
   # Save
   final_inventory.to_csv('Master_Endpoint_Inventory_Deduplicated.csv', index=False)
   
   print(f"Original records: {len(df)}")
   print(f"After deduplication: {len(final_inventory)}")
   print(f"Duplicates removed: {len(df) - len(final_inventory)}")
   ```

3. **Manual Review of Duplicates**:
   - Flag near-duplicates for manual review (e.g., similar hostname but different serial)
   - Review devices appearing in some sources but not others

---

## 6. Endpoint Classification

### 6.1 Device Type Classification

**Categories**:
- 💻 **Laptop**: Portable computer with integrated keyboard and screen
- 🖥️ **Desktop**: Stationary computer (tower, all-in-one)
- 📱 **Smartphone**: Mobile phone (iOS, Android)
- 📲 **Tablet**: Touchscreen tablet (iPad, Android tablet, Surface)
- 💿 **Thin Client**: Lightweight endpoint connecting to remote desktop
- ⚙️ **IoT Device**: Internet of Things endpoint (smart displays, sensors)
- 🖨️ **Other**: Kiosks, specialized endpoints

**Automated Classification** (based on OS and form factor):

```python
def classify_device_type(os, model):
    if 'iOS' in os or 'iPhone' in model:
        return 'Smartphone'
    elif 'iPadOS' in os or 'iPad' in model:
        return 'Tablet'
    elif 'Android' in os:
        if 'Phone' in model or 'SM-' in model:  # Samsung phone model prefix
            return 'Smartphone'
        else:
            return 'Tablet'
    elif 'Windows' in os or 'macOS' in os or 'Linux' in os:
        if 'Laptop' in model or 'ThinkPad' in model or 'MacBook' in model:
            return 'Laptop'
        elif 'Desktop' in model or 'iMac' in model or 'OptiPlex' in model:
            return 'Desktop'
        elif 'Thin' in model or 'Zero Client' in model:
            return 'Thin Client'
        else:
            return 'Unknown'  # Manual classification required
    else:
        return 'Unknown'
```

### 6.2 Ownership Model Classification

**Categories**:
- 🏢 **Corporate-Owned**: Company-purchased and owned devices
- 📱 **BYOD (Bring Your Own Device)**: Employee personal devices used for work
- 👷 **Contractor**: Devices owned by contractors/consultants
- 👤 **Guest**: Temporary devices (visitors, temporary workers)
- 🧪 **Lab/Test**: Devices for testing, development, research (not production)

**Classification Procedure**:

1. **MDM Enrollment Data**:
   - Intune: Check `Ownership` field (Corporate/Personal)
   - Jamf: Check `User Approved Enrollment` (supervised vs. user-enrolled)

2. **Asset Management Data**:
   - Cross-reference with procurement records
   - If asset tag exists in procurement → Corporate
   - If no asset tag and user survey indicates personal → BYOD

3. **User Attributes**:
   - If username domain is external contractor domain → Contractor
   - If temporary account (e.g., `guest-*`) → Guest

4. **Default Assignment**:
   - If managed by corporate MDM → Corporate (unless specified otherwise)
   - If unmanaged → Flag for manual classification

### 6.3 Criticality Classification

**Categories**:
- 🔴 **High Criticality**: Executive devices, devices accessing critical systems, devices with sensitive data
- 🟡 **Medium Criticality**: Standard employee devices
- 🟢 **Low Criticality**: Guest devices, temporary devices, lab/test devices

**Classification Criteria**:

1. **User Role-Based**:
   - Executive (C-level, VP) → High
   - Finance, HR, Legal, IT Admin → High
   - Engineering, Sales, Marketing → Medium
   - Guest, Contractor (non-privileged) → Low

2. **Data Sensitivity**:
   - Device accesses classified/confidential data → High
   - Device accesses internal data → Medium
   - Device accesses only public data → Low

3. **System Access**:
   - Device has administrative access to critical systems → High
   - Device accesses production systems → Medium
   - Device isolated from production → Low

**Automated Classification** (based on user role):

```python
def classify_criticality(user_email, user_department):
    high_risk_roles = ['CEO', 'CFO', 'CTO', 'CISO', 'VP', 'Finance', 'Legal', 'IT Admin']
    
    if any(role in user_email or role in user_department for role in high_risk_roles):
        return 'High'
    elif user_department in ['Guest', 'Contractor', 'Lab']:
        return 'Low'
    else:
        return 'Medium'
```

---

## 7. Inventory Maintenance

### 7.1 Continuous Discovery Automation

**Goal**: Keep inventory up-to-date without manual effort

**Automation Approaches**:

1. **Scheduled MDM Exports**:
   - **Daily**: Export Intune/Jamf/SCCM data (scheduled task or cron job)
   - **API-Based**: Use MDM APIs to pull inventory programmatically
   - **Diff Detection**: Compare today's export with yesterday's → Identify new/removed devices

   **PowerShell Example** (Intune daily export):
   ```powershell
   # Schedule this script to run daily (Task Scheduler)
   Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"
   
   $today = Get-Date -Format 'yyyyMMdd'
   $exportPath = "C:\EndpointInventory\Intune_$today.csv"
   
   $devices = Get-MgDeviceManagementManagedDevice -All
   $devices | Export-Csv -Path $exportPath -NoTypeInformation
   
   # Compare with previous day
   $yesterday = (Get-Date).AddDays(-1).ToString('yyyyMMdd')
   $previousExport = "C:\EndpointInventory\Intune_$yesterday.csv"
   
   if (Test-Path $previousExport) {
       $previousDevices = Import-Csv $previousExport
       $currentDevices = Import-Csv $exportPath
       
       # New devices
       $newDevices = Compare-Object $previousDevices $currentDevices -Property DeviceId -PassThru | 
           Where-Object { $_.SideIndicator -eq '=>' }
       
       # Removed devices
       $removedDevices = Compare-Object $previousDevices $currentDevices -Property DeviceId -PassThru | 
           Where-Object { $_.SideIndicator -eq '<=' }
       
       # Alert if changes detected
       if ($newDevices.Count -gt 0) {
           Write-Host "New devices detected: $($newDevices.Count)"
           # Send email notification
       }
       if ($removedDevices.Count -gt 0) {
           Write-Host "Devices removed: $($removedDevices.Count)"
           # Send email notification
       }
   }
   ```

2. **Integration with Asset Management**:
   - **ServiceNow Integration**: MDM → ServiceNow CMDB (real-time sync)
   - **Custom API**: Build API endpoint that MDM pushes changes to
   - **Webhook Notifications**: MDM platforms support webhooks for device enrollment/retirement events

3. **Network Monitoring Integration**:
   - **NAC (Network Access Control)**: Discover new devices as they connect to network
   - **DHCP Server Logs**: Monitor DHCP lease logs for new MAC addresses
   - **Flow Analysis**: Analyze NetFlow/sFlow data to identify previously unknown endpoints

### 7.2 Stale Device Identification

**Goal**: Identify devices no longer in use (decommissioned, lost, stolen)

**Procedure**:

1. **Define "Stale" Criteria**:
   - Device has not checked in to MDM for >90 days
   - Device has not logged into AD for >90 days
   - Device has not been seen on network for >90 days

2. **Automated Stale Detection**:

   ```python
   import pandas as pd
   from datetime import datetime, timedelta
   
   # Load inventory
   df = pd.read_csv('Master_Endpoint_Inventory.csv')
   
   # Convert LastCheckIn to datetime
   df['LastCheckIn'] = pd.to_datetime(df['LastCheckIn'])
   
   # Define stale threshold
   stale_threshold = datetime.now() - timedelta(days=90)
   
   # Identify stale devices
   df['IsStale'] = df['LastCheckIn'] < stale_threshold
   
   # Export stale devices
   stale_devices = df[df['IsStale'] == True]
   stale_devices.to_csv('Stale_Devices_Report.csv', index=False)
   
   print(f"Stale devices identified: {len(stale_devices)}")
   ```

3. **Stale Device Workflow**:
   - **Weekly Report**: Generate stale device list
   - **Manager Notification**: Email device owner's manager for confirmation
   - **Grace Period**: 30 days to respond
   - **Retirement**: If no response, retire device from inventory (update status to "Decommissioned")

### 7.3 Exception Handling

**Challenge**: Some devices legitimately cannot be discovered via automated methods

**Exception Categories**:

1. **Air-Gapped Devices**:
   - Industrial control systems
   - Classified networks
   - **Solution**: Manual inventory, physical site surveys

2. **Intermittently Connected Devices**:
   - Field technician laptops (rarely online)
   - Remote workers with inconsistent connectivity
   - **Solution**: Longer "stale" threshold (180 days), periodic check-ins via email

3. **BYOD Devices with Limited Management**:
   - Employees refuse MDM enrollment (privacy concerns)
   - **Solution**: MAM (Mobile Application Management) instead of MDM, or accept as "unmanaged" with documented risk

**Exception Documentation**:
- Maintain exception register
- Columns: Device ID, Exception Type, Justification, Approval Date, Approver, Review Date
- Annual review of all exceptions

---

## 8. Verification Procedures

### 8.1 Coverage Verification

**Goal**: Ensure discovery achieved ≥95% coverage

**Verification Methods**:

1. **Expected Count Validation**:
   - Procurement records: 500 laptops purchased in last 3 years
   - Discovery results: 485 laptops found
   - Coverage: 485/500 = 97% ✅

2. **Sample Testing**:
   - Randomly select 20 devices from inventory
   - Physically verify or remote-verify existence
   - If 19/20 verified → 95% accuracy ✅

3. **Cross-Source Validation**:
   - Compare device counts across sources:
     - Intune: 450 devices
     - AD: 460 computers
     - Network scan: 470 active IPs
   - Investigate discrepancies (why does AD have 10 more?)

### 8.2 Data Quality Checks

**Validation Checks**:

1. **Required Fields Populated**:
   - No blank Device IDs
   - No blank Hostnames (or minimal blanks)
   - Operating System populated for ≥95% of devices

   **SQL Example** (if using database):
   ```sql
   SELECT COUNT(*) AS MissingHostname
   FROM EndpointInventory
   WHERE Hostname IS NULL OR Hostname = '';
   ```

2. **Valid Values**:
   - Operating System from approved list (not freeform text)
   - Device Type from approved list
   - Criticality from approved list (High, Medium, Low)

3. **Date Validity**:
   - LastCheckIn date is not in the future
   - LastCheckIn date is within reasonable range (not 1970-01-01)

4. **Duplicate Detection**:
   - No duplicate serial numbers
   - Minimal duplicate hostnames (investigate if found)

### 8.3 Accuracy Spot-Checks

**Procedure**:

1. **Sample Selection**:
   - Random sample of 20 devices (stratified by device type)

2. **Physical Verification**:
   - **Laptops/Desktops**: Remote desktop connection or physical inspection
     - Verify hostname matches inventory
     - Verify OS matches inventory
     - Verify user matches inventory
   - **Mobile Devices**: Contact user to confirm device details
   - **Cloud VMs**: Verify in cloud console

3. **Documentation**:
   - Verification log: Device ID, Verified Date, Verifier, Result (Match/Mismatch), Discrepancies

4. **Discrepancy Resolution**:
   - If mismatch found → Update inventory
   - If pattern of mismatches → Review discovery process for issues

---

## 9. Common Pitfalls and Troubleshooting

### 9.1 Common Mistakes

**Pitfall 1: Relying on a Single Discovery Method**
- **Problem**: No single method discovers all devices. MDM only finds managed devices, AD only finds domain-joined devices, network scan misses offline devices.
- **Solution**: Use multiple methods (MDM + AD + network scan + surveys) and consolidate.

**Pitfall 2: Ignoring BYOD Devices**
- **Problem**: BYOD devices access corporate email/data but aren't inventoried, creating security blind spot.
- **Solution**: User surveys, MAM enrollment tracking, conditional access policies (require registration for access).

**Pitfall 3: Stale AD Computer Objects Skewing Count**
- **Problem**: Active Directory contains hundreds of stale computer objects (devices decommissioned years ago), making AD counts unreliable.
- **Solution**: Filter AD query by LastLogonDate (exclude devices not logged in for 90+ days).

**Pitfall 4: Network Scanning Triggering IDS/IPS Alerts**
- **Problem**: Aggressive nmap scans trigger security alerts, causing security team to investigate or block scanner.
- **Solution**: Coordinate with security team before scanning, whitelist scanner IP in IDS/IPS, use throttled scans (`--max-rate 100`).

**Pitfall 5: Duplicate Devices After Consolidation**
- **Problem**: Same device appears multiple times from different sources (Intune + AD + network scan), inflating counts.
- **Solution**: Deduplicate using serial number or MAC address before counting.

**Pitfall 6: Incomplete Data from API Exports**
- **Problem**: MDM API export missing critical fields (e.g., no serial numbers returned).
- **Solution**: Verify API export includes all required fields. If not, supplement with additional API calls or manual data entry.

**Pitfall 7: Privacy Violations with BYOD Discovery**
- **Problem**: Aggressive BYOD discovery (e.g., scanning personal devices) violates privacy regulations (GDPR).
- **Solution**: Obtain user consent for BYOD discovery, limit discovery to work-related data (email access, app usage), avoid collecting personal data.

### 9.2 Troubleshooting Guide

**Issue: MDM Export Shows Fewer Devices Than Expected**
- **Symptoms**: Intune export shows 300 devices, but procurement records indicate 500 devices purchased.
- **Diagnosis**:
  - Check MDM enrollment status: Are devices enrolled?
  - Check filter settings: Is export filtered (e.g., only "Compliant" devices)?
  - Check device retirement: Were devices retired in MDM but not in procurement records?
- **Solution**:
  - Review enrollment process: Why aren't devices enrolling?
  - Export ALL devices (remove filters)
  - Cross-reference with network scan to find unenrolled devices

**Issue: Network Scan Returns No Results**
- **Symptoms**: Nmap scan returns 0 hosts, but network is active.
- **Diagnosis**:
  - Firewall blocking ICMP: Network devices configured to not respond to pings.
  - Wrong subnet: Scanning wrong IP range.
  - Permissions: Nmap requires sudo for some scans (OS detection, SYN scan).
- **Solution**:
  - Use TCP SYN scan instead of ping scan: `nmap -sS 10.0.0.0/24`
  - Verify correct subnet (check DHCP scope, routing tables)
  - Run with sudo: `sudo nmap -sS 10.0.0.0/24`

**Issue: Duplicate Devices in Consolidated Inventory**
- **Symptoms**: Same device appears 3 times (from Intune, AD, network scan).
- **Diagnosis**: Deduplication not applied or unique identifier missing.
- **Solution**:
  - Ensure all sources provide serial number or MAC address
  - Run deduplication script based on serial number
  - Manual review of remaining duplicates (different hostnames but same serial)

**Issue: Stale Devices Not Being Identified**
- **Symptoms**: Inventory shows devices that were decommissioned months ago.
- **Diagnosis**: LastCheckIn date not being updated or threshold too long.
- **Solution**:
  - Verify MDM is recording LastCheckIn accurately
  - Reduce stale threshold from 90 days to 60 days
  - Implement automated stale device retirement workflow

**Issue: High Number of "Unknown" Device Types**
- **Symptoms**: 20% of devices classified as "Unknown" device type.
- **Diagnosis**: Automated classification logic incomplete (new device models not in mapping table).
- **Solution**:
  - Expand device type classification logic (add more model keywords)
  - Manual classification for "Unknown" devices
  - Update classification script with new patterns

---

## 10. Integration with Other Controls

### 10.1 A.5.9 (Asset Inventory)

**Integration Point**: Endpoint inventory feeds into overall IT asset inventory.

**How They Integrate**:
- Endpoint discovery produces endpoint asset list
- Asset inventory (A.5.9) aggregates endpoints + servers + network devices + applications
- Endpoint data includes: Device ID, Owner, Location, Criticality, Value

**Implementation**:
- Export endpoint inventory to CMDB (ServiceNow, BMC Remedy, etc.)
- Tag endpoints as "Asset Type: Endpoint" in CMDB
- Link endpoint asset to user asset (who owns the device)

### 10.2 A.8.7 (Protection Against Malware)

**Integration Point**: Endpoint inventory defines scope for malware protection.

**How They Integrate**:
- Endpoint discovery identifies ALL endpoints
- Malware protection assessment (A.8.7) compares inventory to anti-malware console
- Gap = Devices in inventory NOT in anti-malware console → Unprotected devices

**Implementation**:
- Use endpoint inventory as master list
- Cross-reference with anti-malware/EDR console device list
- Generate gap report: `Inventory - AntiMalware = Unprotected`

### 10.3 A.8.8 (Vulnerability Management)

**Integration Point**: Endpoint inventory defines scan scope for vulnerability assessments.

**How They Integrate**:
- Vulnerability scanners (Nessus, Qualys) scan endpoints
- Endpoint inventory ensures ALL endpoints are in scan scope
- Unscanned endpoints = security blind spot

**Implementation**:
- Import endpoint inventory into vulnerability scanner
- Create scan targets from inventory (IP addresses, hostnames)
- Compare scanned devices to inventory → Identify missed devices

### 10.4 A.8.9 (Configuration Management)

**Integration Point**: Endpoint inventory is the foundation for configuration baselines.

**How They Integrate**:
- Configuration management requires knowing WHAT to manage (inventory)
- Endpoint baselines (A.8.1) apply to devices in inventory
- Configuration drift detection requires current device list

**Implementation**:
- Endpoint inventory → Configuration management database
- Baseline configurations applied per device type (from inventory classification)
- Configuration compliance assessment references inventory

### 10.5 A.8.15 (Logging)

**Integration Point**: All endpoints should be logging events to SIEM.

**How They Integrate**:
- Endpoint inventory lists devices that SHOULD be logging
- SIEM receives logs from subset of devices
- Gap = Devices in inventory NOT sending logs to SIEM

**Implementation**:
- Compare endpoint inventory to SIEM log sources
- Identify devices not logging (configuration issue or connectivity issue)
- Remediate logging gaps

---

## 11. Maintenance and Updates

### 11.1 Regular Maintenance Tasks

**Daily** (automated):
- MDM inventory export
- Diff detection (new/removed devices)
- Automated alerting for significant changes (>10 devices added/removed)

**Weekly**:
- Stale device report generation
- Manual review of "Unknown" device types
- Classification updates (new devices classified)

**Monthly**:
- Accuracy spot-checks (sample verification)
- Exception register review
- Deduplication and data quality checks

**Quarterly**:
- Full discovery cycle (network scan + user surveys)
- Coverage verification (expected count vs. actual count)
- Manager attestation (department managers confirm their users' devices)

**Annually**:
- Full process review and update
- Discovery tool evaluation (are tools still effective?)
- Compliance audit (external auditor reviews inventory)

### 11.2 Update Procedures

**When to Update Discovery Process**:
- New endpoint types introduced (e.g., ChromeOS devices, AR/VR headsets)
- New MDM platform deployed
- Organizational changes (acquisition, divestiture)
- Regulatory changes (new privacy laws affecting BYOD discovery)

**Update Procedure**:
1. Document change request (what's changing, why)
2. Update discovery scripts/procedures
3. Test in pilot environment
4. Update documentation (this IMP document)
5. Train discovery team
6. Implement change
7. Monitor for issues

### 11.3 Discovery Tool Refresh

**Tool Evaluation Cycle**: Every 2 years

**Evaluation Criteria**:
- Coverage: Does tool discover all device types?
- Accuracy: How accurate is the data?
- Automation: Can it run unattended?
- Integration: Does it integrate with CMDB/SIEM?
- Cost: Is there a more cost-effective alternative?

**Tool Replacement Process**:
- Evaluate alternatives (RFP process if needed)
- Pilot new tool alongside existing
- Compare results (coverage, accuracy)
- Migrate if new tool superior
- Retire old tool

---

## 12. Conclusion

### 12.1 Success Criteria Summary

**Endpoint discovery is successful when**:
- ✅ **Coverage**: ≥95% of expected endpoints discovered
- ✅ **Accuracy**: <5% error rate on spot-checks
- ✅ **Currency**: Inventory updated within 24 hours of device changes
- ✅ **Completeness**: All required fields populated for ≥95% of devices
- ✅ **Classification**: All devices classified (type, ownership, criticality)
- ✅ **Deduplication**: No significant duplicate records (<1% duplicates)
- ✅ **Automation**: Daily automated discovery running reliably

### 12.2 Key Takeaways

1. **Multi-Method Discovery**: No single method achieves 100% coverage. Combine MDM exports, AD queries, network scanning, and user surveys.

2. **Continuous Process**: Endpoint discovery is not a one-time project. Implement automated daily discovery and periodic validation.

3. **BYOD Complexity**: BYOD devices are the hardest to discover. Use surveys and privacy-respecting methods. Accept that some BYOD devices will remain unmanaged.

4. **Data Quality**: Garbage in, garbage out. Invest time in normalization, deduplication, and validation.

5. **Cross-Functional Collaboration**: Endpoint discovery requires input from IT, security, procurement, facilities, and end users.

6. **Foundation for Everything**: Endpoint inventory is the foundation for A.8.7 (malware protection), A.8.18 (privileged utilities), A.8.19 (software controls), and many other controls.

---

**END OF DOCUMENT**

*This implementation guide provides the practical procedures to achieve comprehensive endpoint discovery. Use it as a step-by-step playbook for building and maintaining your endpoint inventory.*
