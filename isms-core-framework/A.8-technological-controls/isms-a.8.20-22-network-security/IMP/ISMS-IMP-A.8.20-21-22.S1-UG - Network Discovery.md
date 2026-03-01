<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S1-UG:framework:UG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S1-UG - Network Discovery Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Network Discovery |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-21-22.S1-UG |
| **Related Policy** | ISMS-POL-A.8.20-21-22 (Network Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.20 (Networks Security) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.20-21-22 (Network Security)
- ISMS-IMP-A.8.20-21-22.S2 (Architecture Documentation)
- ISMS-IMP-A.8.20-21-22.S3 (Device Hardening)
- ISMS-IMP-A.8.20-21-22.S4 (Services Security)
- ISMS-IMP-A.8.20-21-22.S5 (Segmentation Implementation)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Device Inventory | Inventory of all network devices |
| 3 | Device Criticality Matrix | Assess criticality of each network device |
| 4 | Device Type Summary | Summary of network device types |
| 5 | Discovery Metadata | Record network discovery process metadata |
| 6 | Gap Analysis | Identify network inventory coverage gaps |
| 7 | Validation Rules | Define and track inventory validation rules |
| 8 | Evidence Register | Store and reference evidence supporting assessments |
| 9 | Summary Dashboard | Compliance status and key metrics overview |
| 10 | Approval Sign-Off | Management review sign-off and certification |

---

# Purpose and Scope

## Purpose
This document provides practical, step-by-step guidance for discovering and inventorying all network assets, services, and infrastructure components required for assessing compliance with ISO 27001:2022 Controls A.8.20, A.8.21, and A.8.22.

## Scope
This guidance covers:

- **Network Infrastructure Discovery** (A.8.20): Routers, switches, firewalls, wireless access points, VPN concentrators, load balancers, network appliances
- **Network Services Discovery** (A.8.21): DNS, DHCP, NTP, proxy services, authentication services (RADIUS/TACACS+), monitoring services
- **Network Segmentation Discovery** (A.8.22): VLANs, subnets, security zones, trust boundaries, firewall rulesets

## Target Audience

- Network administrators and engineers
- Security assessors and auditors
- ISMS implementation teams
- Infrastructure teams responsible for network documentation

## Prerequisites

- Administrative access to network management systems
- Access to network documentation (if available)
- Understanding of [Organisation]'s network topology (high-level)
- Authorisation to perform network scanning activities

---

# Process Overview

## Discovery Methodology
Network discovery follows a **four-phase approach**:

```
Phase 1: Planning & Scoping
   ↓
Phase 2: Automated Discovery (technical scanning)
   ↓
Phase 3: Manual Discovery (documentation review, interviews)
   ↓
Phase 4: Data Consolidation & Validation
```

## Key Principles

- **Comprehensive Coverage**: Discover ALL network assets, not just managed devices
- **Multi-Method Approach**: Combine automated scanning with manual documentation review
- **Non-Disruptive**: Discovery activities must not impact production services
- **Validated Data**: Cross-reference multiple sources to ensure accuracy
- **Technology-Agnostic**: Works for any network architecture (traditional, SDN, cloud, hybrid)

## Timeline

- **Initial Discovery** (comprehensive): 2-4 weeks
- **Periodic Discovery** (quarterly updates): 1-3 days
- **Continuous Discovery** (automated): Ongoing

---

# Prerequisites and Tools

## Required Access and Permissions

- **Network Administrator Access**: Read-only minimum; write access if deploying agents
- **SNMP Community Strings / SNMPv3 Credentials**: For SNMP-based discovery
- **Cloud Console Access**: AWS/Azure/GCP console access (if using cloud infrastructure)
- **Network Documentation Access**: Access to existing diagrams, IP address management (IPAM) systems
- **Scanning Authorisation**: Documented approval to perform network scans (avoid triggering IDS/IPS)

## Recommended Tools

### Automated Discovery Tools
| Tool | Type | Use Case | Cost |
|------|------|----------|------|
| **nmap** | Port scanner | Network scanning, OS detection, service enumeration | Open-source (free) |
| **Nessus / Qualys** | Vulnerability scanner | Device discovery + vulnerability assessment | Commercial |
| **SNMPwalk / snmpget** | SNMP utility | Device inventory via SNMP | Open-source (free) |
| **NetBox** | IPAM/DCIM | IP address management, device inventory | Open-source (free) |
| **phpIPAM** | IPAM | IP address management | Open-source (free) |
| **AWS CLI / boto3** | Cloud API | AWS infrastructure discovery | Free (AWS SDK) |
| **Azure CLI** | Cloud API | Azure infrastructure discovery | Free (Azure SDK) |
| **GCP SDK** | Cloud API | GCP infrastructure discovery | Free (GCP SDK) |
| **NetFlow/sFlow Collectors** | Traffic analysis | Discover active hosts via traffic flow | Open-source/commercial |
| **Zabbix / PRTG / Nagios** | Monitoring | Leverage existing monitoring for inventory | Open-source/commercial |

### Manual Discovery Tools
| Tool | Type | Use Case |
|------|------|----------|
| **Visio / draw.io** | Diagramming | Document discovered topology |
| **Spreadsheets** | Data management | Track discovery results |
| **Interview templates** | Documentation | Capture knowledge from network admins |
| **Configuration management systems** | CMDB | Extract existing asset data |

## Required Skills and Knowledge

- Basic networking (TCP/IP, subnetting, routing)
- Command-line proficiency (Bash/PowerShell)
- Understanding of SNMP (v2c and v3)
- Familiarity with cloud platforms (if applicable)
- Data analysis skills (tracking results from multiple sources)

---

# Step-by-Step Procedures

## Phase 1: Planning & Scoping

### Define Discovery Scope
Identify the network boundaries to be discovered:

- **Corporate networks**: Data center, campus LAN, branch offices
- **Remote access**: VPN endpoints, remote workers
- **Cloud environments**: AWS VPCs, Azure VNets, GCP networks
- **Wireless networks**: Guest Wi-Fi, corporate Wi-Fi, IoT networks
- **Out-of-band management**: Management VLANs, console servers

**Deliverable**: Discovery scope document listing all network segments

### Identify Discovery Constraints
Document constraints that may affect discovery:

- **Production impact**: Scanning schedules to avoid business hours
- **Access limitations**: Networks inaccessible from scanning location (air-gapped, DMZ)
- **Security controls**: IDS/IPS that may block scans
- **Regulatory compliance**: Networks with special compliance requirements (PCI DSS v4.0.1, HIPAA)

**Deliverable**: Discovery constraints matrix

### Obtain Scanning Authorisation
Obtain written approval for scanning activities:

- **Change ticket** (if required by change management process)
- **Security team notification** (to whitelist scanning source IPs)
- **Stakeholder communication** (notify network admins, service owners)

**Deliverable**: Scanning authorisation document

---

## Phase 2: Automated Discovery

### Network Scanning with nmap

**Overview**: nmap is the industry-standard network scanner for discovering live hosts, open ports, and running services.

**Basic Host Discovery** (ping scan):
```bash
# Discover live hosts in a subnet (no port scan)
nmap -sn 10.1.0.0/24

# Discover multiple subnets
nmap -sn 10.1.0.0/24 10.2.0.0/24 10.3.0.0/24

# Discover entire RFC 1918 private address space (large scan - be cautious)
nmap -sn 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16
```

**Expected Output**:
```
Starting Nmap 7.92 ( https://nmap.org )
Nmap scan report for 10.1.0.1
Host is up (0.0012s latency).
Nmap scan report for 10.1.0.10
Host is up (0.0008s latency).
...
Nmap done: 256 IP addresses (42 hosts up) scanned in 5.32 seconds
```

**Service Detection** (identify running services):
```bash
# Service version detection
nmap -sV 10.1.0.1

# OS detection (requires root/sudo)
sudo nmap -O 10.1.0.1

# Comprehensive scan: service + OS detection
sudo nmap -sV -O 10.1.0.1

# Scan multiple hosts with service detection
nmap -sV 10.1.0.1,10,20,30
```

**Expected Output**:
```
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.3
80/tcp    open  http        nginx 1.18.0
443/tcp   open  ssl/http    nginx 1.18.0
3306/tcp  open  mysql       MySQL 8.0.27
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.6
```

**Network Device Detection** (identify routers, switches, firewalls):
```bash
# Detect network devices (common management ports)
nmap -p 22,23,80,443,161,8443 10.1.0.0/24

# Script scan for device identification
nmap --script snmp-info,http-title,ssh-hostkey 10.1.0.1
```

**Output Formats** (for automated processing):
```bash
# XML output (best for parsing)
nmap -sn 10.1.0.0/24 -oX scan_results.xml

# Greppable output
nmap -sn 10.1.0.0/24 -oG scan_results.gnmap

# All formats
nmap -sn 10.1.0.0/24 -oA scan_results
```

**Troubleshooting Tips**:

- If nmap returns "Host seems down", try `-Pn` to skip host discovery
- If scans are slow, use `-T4` (faster timing) or `-T5` (fastest, aggressive)
- If results are incomplete, ensure firewall rules allow scanning traffic
- If nmap is blocked by IDS/IPS, coordinate with security team to whitelist scan source

---

### SNMP-Based Discovery

**Overview**: SNMP (Simple Network Management Protocol) is excellent for discovering managed network devices (routers, switches) and extracting detailed inventory data.

**SNMPv2c Walk** (community-string based):
```bash
# Walk entire MIB tree
snmpwalk -v2c -c public 10.1.0.1

# System information
snmpwalk -v2c -c public 10.1.0.1 system

# Interface information
snmpwalk -v2c -c public 10.1.0.1 interfaces

# IP address table
snmpwalk -v2c -c public 10.1.0.1 ipAddrTable

# ARP table (discover connected devices)
snmpwalk -v2c -c public 10.1.0.1 ipNetToMediaTable
```

**SNMPv3 Walk** (secure, recommended):
```bash
# SNMPv3 with authentication and privacy
snmpwalk -v3 -l authPriv \
  -u snmpuser \
  -a SHA -A authPassword \
  -x AES -X privPassword \
  10.1.0.1 system
```

**Common OIDs for Network Discovery**:
| OID | Description |
|-----|-------------|
| `1.3.6.1.2.1.1.1.0` | System description (sysDescr) |
| `1.3.6.1.2.1.1.5.0` | System name (sysName) |
| `1.3.6.1.2.1.1.6.0` | System location (sysLocation) |
| `1.3.6.1.2.1.2.2.1.2` | Interface descriptions (ifDescr) |
| `1.3.6.1.2.1.4.20.1.1` | IP addresses configured on device (ipAdEntAddr) |
| `1.3.6.1.2.1.4.22.1.2` | ARP table / MAC address table (ipNetToMediaPhysAddress) |

**Extract Specific Information**:
```bash
# Get system name
snmpget -v2c -c public 10.1.0.1 1.3.6.1.2.1.1.5.0

# Get all IP addresses on device
snmpwalk -v2c -c public 10.1.0.1 1.3.6.1.2.1.4.20.1.1

# Get interface list
snmpwalk -v2c -c public 10.1.0.1 1.3.6.1.2.1.2.2.1.2
```

**Parse SNMP Output** (extract useful data):
```bash
# Extract IP addresses from ARP table
snmpwalk -v2c -c public 10.1.0.1 ipNetToMediaNetAddress | \
  awk '{print $NF}' | \
  sort -u > discovered_ips.txt
```

**Troubleshooting Tips**:

- If SNMP queries fail, verify SNMP is enabled on target device
- Check SNMP community string (default "public" is often changed for security)
- Ensure SNMP ACLs allow queries from your scanning host
- If SNMPv3 fails, verify username and authentication credentials

---

### Cloud Infrastructure Discovery

**AWS Discovery** (using AWS CLI):
```bash
# List all EC2 instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,PrivateIpAddress,InstanceType,State.Name]' --output table

# List all VPCs
aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,CidrBlock,Tags[?Key==`Name`].Value|[0]]' --output table

# List all subnets
aws ec2 describe-subnets --query 'Subnets[*].[SubnetId,VpcId,CidrBlock,AvailabilityZone]' --output table

# List all security groups (firewall rules)
aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupId,GroupName,VpcId]' --output table

# List all network interfaces
aws ec2 describe-network-interfaces --query 'NetworkInterfaces[*].[NetworkInterfaceId,PrivateIpAddress,SubnetId,Status]' --output table

# List all load balancers (ELB/ALB/NLB)
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,DNSName,Type,Scheme]' --output table
```

**AWS Discovery** (using boto3 Python script):
```python
import boto3
import csv

# Create EC2 client
ec2 = boto3.client('ec2')

# Discover all instances
instances = ec2.describe_instances()

# Extract instance details
inventory = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        inventory.append({
            'InstanceId': instance['InstanceId'],
            'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
            'InstanceType': instance['InstanceType'],
            'State': instance['State']['Name'],
            'VpcId': instance.get('VpcId', 'N/A'),
            'SubnetId': instance.get('SubnetId', 'N/A')
        })

# Write to CSV
with open('aws_ec2_inventory.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=inventory[0].keys())
    writer.writeheader()
    writer.writerows(inventory)

print(f"Discovered {len(inventory)} EC2 instances")
```

**Azure Discovery** (using Azure CLI):
```bash
# List all virtual networks
az network vnet list --query '[*].[name,resourceGroup,location,addressSpace.addressPrefixes[0]]' --output table

# List all subnets
az network vnet subnet list --resource-group MyResourceGroup --vnet-name MyVNet --query '[*].[name,addressPrefix]' --output table

# List all VMs
az vm list --query '[*].[name,location,hardwareProfile.vmSize,provisioningState]' --output table

# List all network security groups (NSGs)
az network nsg list --query '[*].[name,resourceGroup,location]' --output table

# List all network interfaces
az network nic list --query '[*].[name,ipConfigurations[0].privateIpAddress,networkSecurityGroup.id]' --output table

# List all load balancers
az network lb list --query '[*].[name,resourceGroup,frontendIpConfigurations[0].privateIpAddress]' --output table
```

**GCP Discovery** (using gcloud CLI):
```bash
# List all VPCs
gcloud compute networks list

# List all subnets
gcloud compute networks subnets list

# List all VM instances
gcloud compute instances list --format="table(name,zone,machineType,networkInterfaces[0].networkIP,status)"

# List all firewall rules
gcloud compute firewall-rules list --format="table(name,network,direction,priority,sourceRanges.list():label=SRC_RANGES,allowed[].map().firewall_rule().list():label=ALLOW)"

# List all load balancers
gcloud compute forwarding-rules list
```

**Troubleshooting Tips**:

- Ensure AWS/Azure/GCP CLI is authenticated (`aws configure`, `az login`, `gcloud auth login`)
- Verify IAM permissions (read access to EC2, VPC, networking resources)
- For multi-region deployments, loop through all regions:

  ```bash
  for region in $(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text); do
    echo "Scanning $region..."
    aws ec2 describe-instances --region $region --query 'Reservations[*].Instances[*].[InstanceId,PrivateIpAddress]' --output table
  done
  ```

---

### NetFlow/sFlow Traffic Analysis

**Overview**: NetFlow/sFlow collectors passively capture traffic metadata to identify active hosts and services without active scanning.

**Setup NetFlow Collector** (using nfdump):
```bash
# Install nfdump
sudo apt-get install nfdump

# Create directory for NetFlow data
mkdir -p /var/cache/nfdump/flows

# Start nfcapd collector (listens on port 9995)
nfcapd -w -D -l /var/cache/nfdump/flows -p 9995
```

**Configure Network Devices** to export NetFlow/sFlow:
```cisco
! Cisco IOS NetFlow configuration (example)
interface GigabitEthernet0/1
 ip flow ingress
 ip flow egress
!
ip flow-export version 9
ip flow-export destination 10.1.100.50 9995
```

**Analyze NetFlow Data** (discover active hosts):
```bash
# List all flows
nfdump -R /var/cache/nfdump/flows -c 100

# Extract unique source IPs
nfdump -R /var/cache/nfdump/flows -o "fmt:%sa" | sort -u > source_ips.txt

# Extract unique destination IPs
nfdump -R /var/cache/nfdump/flows -o "fmt:%da" | sort -u > dest_ips.txt

# Identify top talkers (most active hosts)
nfdump -R /var/cache/nfdump/flows -s srcip/bytes -n 20

# Identify services used (destination ports)
nfdump -R /var/cache/nfdump/flows -s dstport/bytes -n 20
```

**Troubleshooting Tips**:

- Ensure network devices are configured to export flows to collector IP
- Verify UDP port 9995 (or configured port) is open on firewall
- NetFlow data is sampled (1:100 or 1:1000) - full traffic isn't captured
- Use NetFlow as supplementary discovery method, not primary

---

## Phase 3: Manual Discovery

### Documentation Review

**Collect Existing Documentation**:

- Network topology diagrams (physical and logical)
- IP address management (IPAM) spreadsheets or systems
- Asset inventory (CMDB / configuration management database)
- VLAN assignments and subnet allocations
- Firewall rule documentation
- Service catalogs (DNS, DHCP, NTP servers, etc.)
- Vendor contracts (for managed services)

**Extract Asset Data from Documentation**:

- Device hostnames and IP addresses
- Device types (router, switch, firewall, etc.)
- Device locations (data center, building, floor)
- Management interfaces (how to access devices)
- Service dependencies (what depends on what)

**Validate Documentation Accuracy**:

- Compare documented assets against discovered assets
- Flag discrepancies (documented but not discovered = potentially offline or decommissioned)
- Flag discoveries not documented (shadow IT, undocumented changes)

**Deliverable**: Asset list from documentation sources

---

### Network Administrator Interviews

**Purpose**: Capture tacit knowledge not documented elsewhere

**Interview Template**:

**General Questions**:
1. Can you describe the high-level network architecture?
2. What are the primary network segments (data center, office, DMZ, guest, etc.)?
3. Are there any air-gapped or isolated networks?
4. What network monitoring tools are currently deployed?

**Device Inventory Questions**:
5. What types of network devices do we have? (routers, switches, firewalls, load balancers, etc.)
6. Are there any network devices not managed centrally?
7. Are there any end-of-life devices scheduled for replacement?
8. Do we have redundant/failover devices?

**Network Services Questions**:
9. What DNS servers are in use? (authoritative, recursive, caching)
10. How is DHCP deployed? (centralized, distributed, per-VLAN)
11. What NTP servers do devices synchronize with?
12. Are there proxy servers or web gateways?
13. What authentication services are used? (RADIUS, TACACS+, LDAP)

**Network Segmentation Questions**:
14. How is the network segmented? (VLANs, physical separation, VRFs, cloud security groups)
15. What are the security zones? (DMZ, internal, management, guest)
16. Are there firewall rules between zones?
17. Are there any flat networks (unsegmented)?

**Access and Credentials Questions**:
18. How do we access network devices remotely? (SSH, console, jump host)
19. Are credentials centrally managed or local to each device?
20. Is there a network configuration backup system?

**Deliverable**: Interview notes document

---

### Physical Site Survey (if applicable)

**Purpose**: Discover devices not accessible via network scanning (offline, out-of-band management, isolated)

**Site Survey Checklist**:

- [ ] Data center equipment racks (label devices, note IP addresses)
- [ ] IDF/MDF closets (identify switches, patch panels)
- [ ] Wireless access point locations
- [ ] Network monitoring appliances (IDS/IPS sensors, packet capture devices)
- [ ] Out-of-band management network (console servers, IPMI/iLO)
- [ ] Legacy equipment (old switches still in rack but powered off)

**Document with Photos**:

- Rack layout photos (label device positions)
- Cable management (identify uplink connections)
- Serial numbers and model numbers (for warranty tracking)

**Deliverable**: Site survey report with photos and notes

---

## Phase 4: Data Consolidation & Validation

### Compile Discovery Results

**Combine Data from All Sources**:

- Automated scans (nmap, SNMP, cloud APIs)
- Documentation review
- Administrator interviews
- Physical site surveys

**Deduplication Strategy**:
1. **Normalize IP addresses**: Ensure consistent format (remove leading zeros, standardize notation)
2. **Normalize hostnames**: Convert to lowercase, remove domain suffixes if inconsistent
3. **Match by multiple attributes**: IP address + MAC address + hostname
4. **Resolve conflicts**: If same IP has different hostnames in different sources, investigate

**Tools for Consolidation**:

- **Spreadsheets** (Excel, Google Sheets): Simple, manual deduplication
- **Database** (SQLite, PostgreSQL): Import all sources, use SQL to deduplicate
- **Python scripts**: Automate deduplication logic

**Example Deduplication Python Script**:
```python
import csv
from collections import defaultdict

# Load discovery data from multiple sources
nmap_data = csv.DictReader(open('nmap_scan.csv'))
snmp_data = csv.DictReader(open('snmp_walk.csv'))
docs_data = csv.DictReader(open('documentation.csv'))

# Compile by IP address
inventory = defaultdict(dict)

for row in nmap_data:
    ip = row['IP Address']
    inventory[ip].update({'nmap_hostname': row['Hostname'], 'nmap_os': row['OS']})

for row in snmp_data:
    ip = row['IP Address']
    inventory[ip].update({'snmp_sysname': row['sysName'], 'snmp_location': row['sysLocation']})

for row in docs_data:
    ip = row['IP Address']
    inventory[ip].update({'doc_hostname': row['Hostname'], 'doc_location': row['Location']})

# Deduplicate hostnames (prefer SNMP sysName, fallback to nmap, fallback to documentation)
for ip, data in inventory.items():
    hostname = data.get('snmp_sysname') or data.get('nmap_hostname') or data.get('doc_hostname') or 'Unknown'
    location = data.get('snmp_location') or data.get('doc_location') or 'Unknown'
    inventory[ip]['hostname'] = hostname
    inventory[ip]['location'] = location

# Write compiled inventory
with open('consolidated_inventory.csv', 'w', newline='') as f:
    fieldnames = ['IP Address', 'Hostname', 'Location', 'OS', 'Discovery Source']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for ip, data in inventory.items():
        writer.writerow({
            'IP Address': ip,
            'Hostname': data.get('hostname', 'Unknown'),
            'Location': data.get('location', 'Unknown'),
            'OS': data.get('nmap_os', 'Unknown'),
            'Discovery Source': 'Multiple sources'
        })

print(f"Compiled {len(inventory)} unique devices")
```

---

### Data Validation

**Validate IP Addresses**:
```bash
# Check for invalid IP formats
grep -vE '^([0-9]{1,3}\.){3}[0-9]{1,3}$' consolidated_inventory.csv
```

**Validate VLAN IDs**:

- Ensure VLAN IDs are in valid range (1-4094)
- Flag reserved VLANs (1 = default, 1002-1005 = reserved)

**Validate Subnet CIDR Notation**:
```bash
# Check for valid CIDR notation
grep -vE '^([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$' subnets.csv
```

**Cross-Reference Consistency**:

- Device IDs referenced in multiple sheets must exist in master inventory
- Zone IDs must be consistent across segmentation documentation
- Service IDs must link to valid services

**Reachability Testing**:
```bash
# Ping discovered hosts to verify they're still online
while IFS=, read -r ip hostname; do
  if ping -c 1 -W 1 "$ip" > /dev/null 2>&1; then
    echo "$ip,$hostname,REACHABLE"
  else
    echo "$ip,$hostname,UNREACHABLE"
  fi
done < <(tail -n +2 consolidated_inventory.csv | cut -d',' -f1,2)
```

**Deliverable**: Validated compiled inventory (CSV/Excel)

---

### Identify and Investigate Gaps

**Identify Discovered-But-Not-Documented Assets**:

- Devices found by scanning but not in documentation (shadow IT risk)
- Investigate ownership and purpose
- Add to official inventory if legitimate

**Identify Documented-But-Not-Discovered Assets**:

- Devices in documentation but not found by scanning (possibly offline, decommissioned, or unreachable)
- Investigate status (powered off, network issue, scheduled for decommissioning)
- Update documentation if decommissioned

**Identify Missing Critical Information**:

- Devices without hostname (assign naming convention)
- Devices without location (physical or logical location unknown)
- Devices without owner (assign responsibility)

**Deliverable**: Gap analysis report

---

# Automation Opportunities

## Scheduled Automated Discovery

**Cron Job for Periodic nmap Scans**:
```bash
# /etc/cron.d/network-discovery
# Run nmap scan every Sunday at 2 AM

0 2 * * 0 root /usr/bin/nmap -sn 10.0.0.0/8 -oX /var/log/nmap/scan_$(date +\%Y\%m\%d).xml

```

**SNMP Polling Script** (Python):
```python
#!/usr/bin/env python3
import subprocess
import csv
from datetime import datetime

# List of network devices (IP addresses)
devices = ['10.1.0.1', '10.1.0.2', '10.1.0.3']

# SNMP community string
community = 'public'

# Output CSV
output_file = f'snmp_inventory_{datetime.now().strftime("%Y%m%d")}.csv'

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['IP Address', 'sysName', 'sysDescr', 'sysLocation'])
    
    for ip in devices:
        try:
            # Query SNMP
            sysname = subprocess.check_output(['snmpget', '-v2c', '-c', community, ip, '1.3.6.1.2.1.1.5.0'], text=True).split()[-1]
            sysdescr = subprocess.check_output(['snmpget', '-v2c', '-c', community, ip, '1.3.6.1.2.1.1.1.0'], text=True).split('=')[-1].strip()
            syslocation = subprocess.check_output(['snmpget', '-v2c', '-c', community, ip, '1.3.6.1.2.1.1.6.0'], text=True).split()[-1]
            
            writer.writerow([ip, sysname, sysdescr, syslocation])
        except Exception as e:
            print(f"Error querying {ip}: {e}")

print(f"SNMP inventory saved to {output_file}")
```

**Cloud Inventory Sync** (AWS example):
```bash
#!/bin/bash
# Sync AWS EC2 inventory daily

aws ec2 describe-instances \
  --query 'Reservations[*].Instances[*].[InstanceId,PrivateIpAddress,InstanceType,State.Name]' \
  --output text > /var/log/aws_inventory_$(date +%Y%m%d).txt

echo "AWS inventory updated"
```

---

## Integration with Configuration Management

**Ansible Dynamic Inventory**:
```yaml
# ansible.cfg
[defaults]
inventory = /etc/ansible/inventory/ec2.py
```

**Terraform State as Inventory Source**:
```bash
# Extract infrastructure from Terraform state
terraform show -json | jq '.values.root_module.resources[] | select(.type=="aws_instance") | {name: .values.tags.Name, private_ip: .values.private_ip}'
```

---

## Continuous Discovery with Monitoring Tools

**Leverage Existing Monitoring**:

- **Zabbix**: Export host inventory from Zabbix monitoring system
- **Nagios**: Parse Nagios configuration for monitored hosts
- **PRTG**: Export device list from PRTG sensor tree

**Example: Export from Zabbix**:
```bash
# Zabbix API call to get all hosts
curl -X POST https://zabbix.example.com/api_jsonrpc.php \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
      "output": ["hostid", "host", "name", "status"],
      "selectInterfaces": ["ip"]
    },
    "auth": "YOUR_AUTH_TOKEN",
    "id": 1
  }'
```

---

# Integration with Other Processes

## Integration with A.8.20 (Network Security)

- Discovered devices feed into **Device Hardening Assessment** (IMP-S3)
- Device inventory populates **WB1: Infrastructure Inventory** workbook
- Discovery identifies unmanaged/rogue devices requiring security review

## Integration with A.8.21 (Network Services)

- Discovered services feed into **Network Services Catalog** (WB3)
- Service enumeration (DNS, DHCP, NTP) from automated scans
- Port scanning identifies unexpected services requiring investigation

## Integration with A.8.22 (Network Segregation)

- Discovered subnets and VLANs feed into **Segmentation Matrix** (WB4)
- Network topology discovery informs segmentation architecture review
- ARP tables and traffic flow reveal inter-zone communication patterns

## Integration with Other ISMS Controls

- **A.8.8 (Vulnerability Management)**: Discovery feeds into vulnerability scanning scope
- **A.8.9 (Configuration Management)**: Discovered devices must have baseline configurations
- **A.8.15 (Logging)**: Discovered devices should be checked for logging capability
- **A.8.16 (Monitoring)**: Discovered devices should be enrolled in monitoring systems

---

# Quality Assurance

## Completeness Checks

- [ ] All known network segments have been scanned
- [ ] All cloud environments have been queried (if applicable)
- [ ] Documentation review is complete
- [ ] Administrator interviews conducted
- [ ] Physical site surveys completed (if applicable)

## Accuracy Checks

- [ ] IP address format validation passed
- [ ] Hostname resolution verified (DNS forward/reverse lookup)
- [ ] Reachability testing completed (ping test or equivalent)
- [ ] Cross-reference consistency validated (no orphaned references)
- [ ] Deduplication completed (no duplicate IP addresses or hostnames)

## Coverage Metrics
Calculate discovery coverage:
```
Coverage % = (Discovered Devices / Expected Devices) * 100
```

- If Coverage < 90%, investigate gaps
- If Coverage > 110%, investigate false positives or scope creep

---

# Common Pitfalls and Solutions

## Pitfall: Incomplete Scanning Due to Firewall Blocks
**Problem**: Network scanning blocked by IDS/IPS or firewalls  
**Solution**:

- Coordinate with security team to whitelist scanning source IP
- Use trusted internal scanning hosts (not external)
- Perform scans during maintenance windows if blocking cannot be avoided
- Use passive discovery methods (NetFlow, SNMP polling) as alternative

---

## Pitfall: SNMP Access Denied
**Problem**: SNMP queries fail due to incorrect community strings or ACLs  
**Solution**:

- Obtain correct SNMP community strings from network admins
- Verify SNMP ACLs allow queries from scanning host
- If SNMPv2c is disabled, use SNMPv3 with proper authentication
- Test SNMP access with simple query first (sysName) before full walk

---

## Pitfall: Cloud Discovery Misses Resources
**Problem**: Cloud resources not discovered due to multi-region or multi-account deployments  
**Solution**:

- Loop through all regions (AWS: `aws ec2 describe-regions`, Azure: `az account list-locations`)
- Loop through all accounts (AWS Organisations, Azure Management Groups)
- Use cloud-native discovery tools (AWS Config, Azure Resource Graph)

---

## Pitfall: Duplicate Devices in Compiled Inventory
**Problem**: Same device appears multiple times due to multiple IP addresses or hostnames  
**Solution**:

- Use MAC address as unique identifier (if available)
- Cross-reference multiple attributes (IP + MAC + hostname)
- Manually review devices with similar names (e.g., router1, router01, router-1)

---

## Pitfall: Discovery Disrupts Production
**Problem**: Network scanning causes performance issues or triggers security alerts  
**Solution**:

- Use slower scan timing (`nmap -T2` instead of `-T4`)
- Scan outside business hours
- Coordinate with operations team before scanning
- Use passive discovery methods where possible

---

# Documentation Requirements

## Discovery Report
Document the following:

- **Discovery Date Range**: Start and end dates of discovery activities
- **Discovery Scope**: Network segments covered
- **Discovery Methods Used**: Automated scanning, SNMP, cloud APIs, documentation review, interviews
- **Tools Used**: nmap version, SNMP utilities, cloud CLIs, etc.
- **Discovery Results Summary**:
  - Total devices discovered
  - Total services discovered
  - Total subnets/VLANs identified
  - Gaps identified (undocumented devices, unreachable documented devices)
- **Next Discovery Date**: Scheduled date for next periodic discovery

**Template**: See `/templates/network_discovery_report_template.docx`

---

## Compiled Inventory
The consolidated inventory should be stored in a structured format (CSV or database) with the following fields:

**Minimum Required Fields**:

- Device ID (unique identifier, e.g., NET-DEV-001)
- IP Address (primary IP)
- Hostname
- Device Type (router, switch, firewall, etc.)
- Location (physical or logical)
- Discovery Date
- Discovery Method

**Recommended Additional Fields**:

- MAC Address
- Vendor/Manufacturer
- Model/Part Number
- Serial Number
- Firmware/OS Version
- Management IP (if different from primary IP)
- Device Owner/Responsible Team
- Criticality (Critical, High, Medium, Low)
- Status (Active, Offline, Decommissioned)

**Storage Location**: [Organisation] CMDB / Network Documentation Repository

---

## Gap Analysis Report
Document all gaps identified during discovery:

- **Gap ID**: Unique identifier (e.g., DISC-GAP-001)
- **Gap Type**: Undocumented device, unreachable device, missing information
- **Description**: Details of the gap
- **Impact**: Risk or compliance impact
- **Remediation Plan**: How gap will be addressed
- **Responsible Person**: Who will remediate
- **Target Date**: When gap will be closed

**Template**: See `/templates/network_discovery_gap_analysis_template.xlsx`

---

# Continuous Improvement

## Metrics to Track

- **Discovery Completeness**: % of known network covered by discovery
- **Discovery Accuracy**: % of discovered devices that are accurate (not false positives)
- **Documentation Drift**: Number of devices discovered but not documented (shadow IT indicator)
- **Discovery Cycle Time**: Time required to complete discovery (target: reduce over time)

## Lessons Learned Capture
After each discovery cycle, document:

- What worked well (efficient discovery methods)
- What didn't work (blocked scans, access issues)
- Improvements for next cycle (better tools, refined scope)

## Process Refinement

- Review discovery process annually
- Incorporate feedback from network admins and security team
- Update tool recommendations based on new technologies
- Automate repetitive tasks (scheduled scans, data consolidation)

---

# Appendix

## nmap Command Reference

| Command | Purpose |
|---------|---------|
| `nmap -sn <target>` | Ping scan (host discovery only, no port scan) |
| `nmap -sS <target>` | TCP SYN scan (stealthy, requires root) |
| `nmap -sT <target>` | TCP connect scan (non-privileged) |
| `nmap -sU <target>` | UDP scan |
| `nmap -sV <target>` | Service version detection |
| `nmap -O <target>` | OS detection (requires root) |
| `nmap -A <target>` | Aggressive scan (OS detection, version, script, traceroute) |
| `nmap -p 1-65535 <target>` | Scan all 65535 ports |
| `nmap -p 22,80,443 <target>` | Scan specific ports |
| `nmap --script <script> <target>` | Run NSE script |
| `nmap -Pn <target>` | Skip host discovery (assume host is up) |
| `nmap -T0` through `-T5` | Timing templates (0=paranoid, 5=insane) |
| `nmap -oX <file>` | XML output |
| `nmap -oG <file>` | Greppable output |
| `nmap -oA <basename>` | Output in all formats |

---

## SNMP OID Quick Reference

| OID | Description |
|-----|-------------|
| `1.3.6.1.2.1.1.1.0` | sysDescr (system description) |
| `1.3.6.1.2.1.1.5.0` | sysName (hostname) |
| `1.3.6.1.2.1.1.6.0` | sysLocation (physical location) |
| `1.3.6.1.2.1.1.7.0` | sysServices (services offered) |
| `1.3.6.1.2.1.2.1.0` | ifNumber (number of interfaces) |
| `1.3.6.1.2.1.2.2.1.2` | ifDescr (interface descriptions) |
| `1.3.6.1.2.1.4.20.1.1` | ipAdEntAddr (IP addresses on device) |
| `1.3.6.1.2.1.4.22.1.2` | ipNetToMediaPhysAddress (ARP table MAC addresses) |
| `1.3.6.1.2.1.4.22.1.3` | ipNetToMediaNetAddress (ARP table IP addresses) |

---

## Cloud CLI Command Reference

**AWS CLI**:
```bash
aws ec2 describe-instances                    # List EC2 instances
aws ec2 describe-vpcs                         # List VPCs
aws ec2 describe-subnets                      # List subnets
aws ec2 describe-security-groups              # List security groups
aws ec2 describe-network-interfaces           # List network interfaces
aws elbv2 describe-load-balancers             # List load balancers
aws route53 list-hosted-zones                 # List DNS hosted zones
```

**Azure CLI**:
```bash
az network vnet list                          # List virtual networks
az network vnet subnet list                   # List subnets
az vm list                                    # List VMs
az network nsg list                           # List network security groups
az network nic list                           # List network interfaces
az network lb list                            # List load balancers
az network dns zone list                      # List DNS zones
```

**GCP gcloud**:
```bash
gcloud compute networks list                  # List VPCs
gcloud compute networks subnets list          # List subnets
gcloud compute instances list                 # List VM instances
gcloud compute firewall-rules list            # List firewall rules
gcloud compute forwarding-rules list          # List load balancers
gcloud dns managed-zones list                 # List DNS zones
```

---

## Sample Discovery Timeline

**Week 1: Planning & Preparation**

- Day 1-2: Define scope, identify constraints
- Day 3: Obtain scanning authorisation
- Day 4-5: Prepare tools, test scanning in lab environment

**Week 2: Automated Discovery**

- Day 1-2: nmap scans (host discovery, service enumeration)
- Day 3: SNMP walks (managed devices)
- Day 4: Cloud infrastructure discovery (AWS/Azure/GCP)
- Day 5: NetFlow analysis (if applicable)

**Week 3: Manual Discovery**

- Day 1-2: Documentation review (diagrams, IPAM, CMDB)
- Day 3: Administrator interviews
- Day 4: Physical site surveys (if applicable)
- Day 5: Begin data consolidation

**Week 4: Consolidation & Validation**

- Day 1-2: Compile data from all sources
- Day 3: Deduplication and validation
- Day 4: Gap analysis
- Day 5: Generate discovery report, update inventory

---

**END OF DOCUMENT**

**Related Documents:**

- ISMS-IMP-A.8.20-21-22-S2 (Architecture Documentation) → Next process
- ISMS-IMP-A.8.20-21-22-S3 (Device Hardening) → Uses inventory from this process
- ISMS-POL-A.8.20-21-22, Section 3 (Governance & Operations) → Parent policy document

**Revision History:**
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial release | [Organisation] ISMS Team |

---

**END OF USER GUIDE**

---

*"You cannot secure a network you have not mapped."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
