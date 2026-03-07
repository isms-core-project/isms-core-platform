<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-22.S5-UG:framework:UG:a.8.20-22 -->
**ISMS-IMP-A.8.20-22.S5-UG - Network Segmentation Implementation**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Segmentation Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.20-22.S5-UG |
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
- ISMS-IMP-A.8.20-22.S1 (Network Discovery)
- ISMS-IMP-A.8.20-22.S2 (Architecture Documentation)
- ISMS-IMP-A.8.20-22.S3 (Device Hardening)
- ISMS-IMP-A.8.20-22.S4 (Services Security)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Controls Coverage Matrix | Map security controls across network zones and assets |
| 3 | Zone Control Assessment | Assess security controls per network zone |
| 4 | Device Control Mapping | Map controls to specific network devices |
| 5 | Service Control Mapping | Map controls to network services |
| 6 | Control Effectiveness | Assess effectiveness of network security controls |
| 7 | Gap Analysis | Identify network controls coverage gaps |
| 8 | Defense In Depth | Assess defence-in-depth strategy implementation |
| 9 | Executive Summary | High-level summary of network security posture |
| 10 | Evidence Register | Store and reference evidence supporting assessments |
| 11 | Summary Dashboard | Compliance status and key metrics overview |
| 12 | Approval Sign-Off | Management review sign-off and certification |

---

# Purpose and Scope

## Purpose

This document provides **practical, step-by-step guidance** for implementing network segmentation to enforce security boundaries, limit lateral movement, and comply with **Control A.8.22 (Segregation of Networks)** requirements.

**Network segmentation** involves:

- Designing security zones based on trust levels and data classification
- Implementing VLANs to logically separate network traffic
- Configuring firewall rules to control inter-zone traffic
- Deploying access control lists (ACLs) on routers and switches
- Implementing cloud network segmentation (VPCs, security groups, NSGs)
- Testing segmentation effectiveness to validate isolation

## Scope

This guidance covers:

- **Segmentation Architecture Design** - Defining security zones, trust boundaries, traffic policies
- **VLAN Implementation** - VLAN design, configuration, security best practices
- **Subnet Design** - IP addressing schemes, subnet allocation, CIDR planning
- **Firewall Rule Development** - Rule creation methodology, documentation, testing
- **ACL Implementation** - Router and switch ACLs for traffic filtering
- **Cloud Network Segmentation** - AWS VPC, Azure VNet, GCP VPC segmentation
- **Segmentation Migration** - Phased approach for moving from flat to segmented networks

## Applicability

This guidance is **technology-agnostic** with specific examples for:

- Traditional networks (Cisco, Juniper, HP/Aruba, etc.)
- Software-defined networking (SDN) environments
- Cloud platforms (AWS, Azure, GCP)
- Hybrid and multi-cloud architectures
- Virtual networks (VMware NSX, Hyper-V, KVM)

## Who Should Use This Guidance

- Network architects designing segmentation architecture
- Network engineers implementing VLANs, firewalls, ACLs
- Security teams defining inter-zone traffic policies
- Cloud engineers implementing VPC/VNet segmentation
- ISMS implementers preparing for A.8.22 assessments

---

# Process Overview

## Segmentation Implementation Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│        NETWORK SEGMENTATION IMPLEMENTATION PROCESS               │
└─────────────────────────────────────────────────────────────────┘

Phase 1: Segmentation Planning and Design
├─ Identify assets and classify by sensitivity
├─ Define security zones (DMZ, internal, management, etc.)
├─ Map trust relationships between zones
├─ Design inter-zone traffic policies (allow/deny matrix)
└─ Document segmentation architecture

Phase 2: IP Address Planning
├─ Design hierarchical IP addressing scheme
├─ Allocate IP subnets to security zones
├─ Plan VLAN-to-subnet mapping
└─ Document IP address management (IPAM) plan

Phase 3: VLAN Implementation
├─ Create VLANs on switches
├─ Configure switchport access and trunk ports
├─ Implement VLAN security (native VLAN, DTP, etc.)
└─ Verify VLAN connectivity

Phase 4: Firewall Rule Development and Deployment
├─ Develop firewall rules based on traffic policies
├─ Document rule justifications
├─ Test rules in staging environment
├─ Deploy rules to production firewalls
└─ Verify rule effectiveness

Phase 5: ACL Implementation (Optional, for additional filtering)
├─ Develop router/switch ACLs for zone boundaries
├─ Apply ACLs to interfaces (inbound/outbound)
├─ Test ACL effectiveness
└─ Document ACL configurations

Phase 6: Cloud Network Segmentation (If Applicable)
├─ Create VPCs/VNets per security zone
├─ Configure security groups (instance-level firewalls)
├─ Configure network ACLs (subnet-level firewalls)
├─ Implement peering/transit gateway for inter-zone traffic
└─ Verify cloud segmentation

Phase 7: Segmentation Testing and Validation
├─ Test inter-zone traffic (verify allow/deny policies)
├─ Attempt lateral movement (penetration testing)
├─ Verify VLAN isolation (VLAN hopping prevention)
└─ Document test results

Phase 8: Migration to Segmented Network (For Existing Flat Networks)
├─ Assess current network (identify flat networks)
├─ Develop phased migration plan (high-value assets first)
├─ Migrate assets zone-by-zone
├─ Update firewall rules incrementally
└─ Validate segmentation after each phase
```

## Key Principles

**Defense in Depth**: Segmentation is one layer; combine with device hardening, monitoring, and access control.

**Default Deny**: Inter-zone traffic is denied by default; only explicitly authorised traffic is allowed.

**Least Privilege**: Systems and users have network access only to resources they require.

**Trust Boundaries**: Every zone boundary enforces security controls (firewall rules, ACLs).

**Continuous Validation**: Segmentation effectiveness is tested regularly.

---

# Prerequisites and Tools

## Required Access and Permissions

- Administrative access to network devices (switches, routers, firewalls)
- Configuration change authority (change management approval)
- Access to network documentation (topology diagrams, IPAM)
- Cloud platform administrative access (if implementing cloud segmentation)

## Required Tools

**Network Management**:

- Network device CLI access (SSH)
- Configuration management tools (Ansible, Terraform, vendor-specific tools)

**IPAM (IP Address Management)**:

- NetBox (open-source IPAM)
- phpIPAM (open-source IPAM)
- Infoblox (commercial IPAM)
- Excel/spreadsheets (for small networks)

**Firewall Management**:

- Firewall vendor management interfaces (Panorama for Palo Alto, FortiManager for Fortinet, etc.)
- Firewall policy analysis tools (AlgoSec, Tufin, FireMon)
- Open-source tools (Capirca for multi-vendor firewall rule generation)

**Cloud Tools**:

- AWS CLI / boto3 (for AWS VPC)
- Azure CLI / PowerShell (for Azure VNet)
- GCP SDK / gcloud (for GCP VPC)
- Terraform (infrastructure-as-code for multi-cloud)

**Testing Tools**:

- nmap (port scanning, connectivity testing)
- tcpdump / Wireshark (packet capture, traffic analysis)
- telnet / nc (netcat - connectivity testing)
- hping3 (packet crafting for testing ACLs)

## Required Skills and Knowledge

- Understanding of IP addressing, subnetting (CIDR notation)
- VLAN concepts and configuration
- Firewall rule syntax (vendor-specific)
- ACL syntax (router/switch-specific)
- Cloud networking concepts (VPC, security groups, NSGs)
- Network security principles (defense in depth, least privilege)

---

# Step-by-Step Procedures

## Phase 1: Segmentation Planning and Design

### Identify and Classify Assets

**Objective**: Understand what needs to be segmented and why.

**Steps**:

1. **Inventory all network-connected assets** (from ISMS-IMP-A.8.20-21-22-S1: Network Discovery)

   - Servers, workstations, IoT devices, network devices, cloud resources

2. **Classify assets by data sensitivity** (align with data classification policy):

   - Public data (can be exposed externally)
   - Internal data (internal use only)
   - Confidential data (restricted access)
   - Restricted data (highly sensitive, regulatory requirements)

3. **Classify assets by function**:

   - Internet-facing (web servers, email gateways, VPN concentrators)
   - Internal business systems (ERP, CRM, databases)
   - Management systems (monitoring, backup, network management)
   - User endpoints (workstations, laptops, mobile devices)
   - Guest systems (guest Wi-Fi, visitor workstations)
   - Development/test systems (non-production environments)
   - IoT/OT (operational technology, industrial control systems)

### Define Security Zones

**Objective**: Create logical groupings of assets with similar security requirements.

**Common Security Zones**:

| Zone Name | Trust Level | Purpose | Example Assets |
|-----------|-------------|---------|----------------|
| **Internet** | Untrusted | External networks | - |
| **DMZ (Demilitarized Zone)** | Semi-Trusted | Internet-facing services | Web servers, mail relays, DNS (external) |
| **Internal** | Trusted | Business systems and user workstations | ERP, CRM, file servers, workstations |
| **Management** | Highly Trusted | Network/system management | Monitoring, backup, patch servers, jump hosts |
| **Guest** | Untrusted | Guest user access | Guest Wi-Fi, visitor workstations |
| **Development** | Isolated | Development/test environments | Dev servers, test systems |
| **IoT/OT** | Isolated | IoT and operational technology | Building automation, industrial control systems |
| **Remote Access** | Conditional Trust | VPN users, remote workers | VPN gateway, remote access systems |

**Zone Design Principles**:

- **Trust boundaries**: Each zone has defined trust level; stricter controls for lower-trust zones
- **Data classification alignment**: Zones map to data classification (e.g., restricted data → management zone)
- **Functional separation**: Similar functions grouped together (all web servers in DMZ)
- **Regulatory compliance**: Isolate regulated data (PCI DSS v4.0.1 → payment card zone, HIPAA → healthcare zone)

**Example Zone Architecture** (for mid-size organisation):

```
Internet (Untrusted)
    ↓ (Firewall)
DMZ (Semi-Trusted) - Web servers, mail relays
    ↓ (Firewall)
Internal (Trusted) - Business systems, user workstations
    ↓ (Firewall)
Management (Highly Trusted) - Monitoring, backup
    ↓ (Isolated)
Development (Isolated) - Test systems
    ↓ (Isolated)
IoT/OT (Isolated) - Building automation
    ↓
Guest (Untrusted) - Guest Wi-Fi
```

### Map Trust Relationships and Traffic Flows

**Objective**: Determine which zones need to communicate and what traffic is allowed.

**Steps**:

1. **Identify required inter-zone traffic**:

   - What services in DMZ need to access Internal zone? (e.g., web server → database)
   - What services in Internal need to access Management? (e.g., servers → backup server)
   - What services need Internet access? (e.g., servers → software updates)

2. **Create traffic flow matrix** (allow/deny matrix):

Example matrix:

|  | Internet | DMZ | Internal | Management | Guest | Dev | IoT/OT |
|---|---|---|---|---|---|---|---|
| **Internet** | - | ALLOW (HTTP/HTTPS inbound) | DENY | DENY | DENY | DENY | DENY |
| **DMZ** | ALLOW (HTTP/HTTPS outbound) | - | ALLOW (DB ports to app servers) | DENY | DENY | DENY | DENY |
| **Internal** | ALLOW (HTTP/HTTPS, DNS, NTP) | ALLOW (HTTP/HTTPS to web servers) | - | ALLOW (backup, monitoring) | DENY | DENY | DENY |
| **Management** | ALLOW (software updates) | ALLOW (management protocols) | ALLOW (management protocols) | - | DENY | ALLOW (monitoring) | ALLOW (monitoring) |
| **Guest** | ALLOW (HTTP/HTTPS, DNS) | DENY | DENY | DENY | - | DENY | DENY |
| **Dev** | ALLOW (software repos) | DENY | DENY | ALLOW (monitoring) | DENY | - | DENY |
| **IoT/OT** | DENY (unless required) | DENY | DENY | ALLOW (monitoring) | DENY | DENY | - |

**Matrix Notation**:

- **ALLOW**: Traffic explicitly permitted (with specific protocols/ports)
- **DENY**: Traffic explicitly blocked
- **-**: Intra-zone traffic (typically allowed, but may have micro-segmentation)

3. **Document justification for each ALLOW rule**:

   - **Business justification**: Why is this traffic needed?
   - **Technical justification**: What protocols/ports are required?
   - **Risk assessment**: What risks does this access introduce? How are they mitigated?

Example:
```
Allow: DMZ → Internal (TCP/3306 - MySQL)
Justification: Web servers in DMZ need to query application database in Internal zone
Risk: Database compromise from DMZ. Mitigation: DB access limited to web server IPs, 
      strong authentication, read-only DB user for web queries, SQL injection prevention.
```

### Document Segmentation Architecture

**Objective**: Create comprehensive segmentation documentation.

**Documentation Requirements**:

1. **Segmentation Architecture Diagram** (from ISMS-IMP-A.8.20-21-22-S2):

   - Visual representation of security zones
   - Trust boundaries and firewalls
   - Traffic flows between zones

2. **Zone Definition Document**:

   - Zone name, purpose, trust level
   - Assets in each zone
   - Data classification of data in zone
   - Zone owner (responsible team)

3. **Inter-Zone Traffic Policy**:

   - Traffic flow matrix (allow/deny)
   - Detailed justification for each allow rule
   - Protocols/ports required for each allow rule

4. **IP Address Allocation** (IPAM):

   - Subnet allocations per zone
   - VLAN-to-subnet mapping
   - IP address ranges

**Template**: See Annex A for Zone Definition Template

---

## Phase 2: IP Address Planning

### Design Hierarchical IP Addressing Scheme

**Objective**: Allocate IP addresses in a structured, scalable manner.

**IP Addressing Principles**:

- **Use RFC 1918 private IP space**: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- **Hierarchical allocation**: Allocate large blocks to regions/sites, then subdivide
- **CIDR notation**: Use CIDR (Classless Inter-Domain Routing) for efficient allocation
- **Contiguous allocation**: Keep related subnets contiguous for summarisation
- **Growth planning**: Leave room for future expansion

**Example IP Allocation** (for mid-size organisation):

```
10.0.0.0/8 - [Organisation] Private IP Space

10.1.0.0/16 - Headquarters Site
  ├─ 10.1.10.0/24 - DMZ (VLAN 10)
  ├─ 10.1.20.0/24 - Internal - Servers (VLAN 20)
  ├─ 10.1.30.0/22 - Internal - User Workstations (VLAN 30-33, 1024 IPs)
  ├─ 10.1.40.0/24 - Management (VLAN 40)
  ├─ 10.1.50.0/24 - Guest Wi-Fi (VLAN 50)
  ├─ 10.1.60.0/24 - Development (VLAN 60)
  └─ 10.1.70.0/24 - IoT/OT (VLAN 70)

10.2.0.0/16 - Branch Office Site
  ├─ 10.2.20.0/24 - Internal - Servers (VLAN 20)
  ├─ 10.2.30.0/23 - Internal - User Workstations (VLAN 30-31, 512 IPs)
  └─ 10.2.50.0/24 - Guest Wi-Fi (VLAN 50)

10.100.0.0/16 - Cloud Resources (AWS VPC)
  ├─ 10.100.10.0/24 - DMZ Subnet (Public-facing instances)
  ├─ 10.100.20.0/24 - Internal Subnet (Private instances)
  └─ 10.100.40.0/24 - Management Subnet (Bastion hosts)
```

**CIDR Subnet Sizing Reference**:

- /24 = 256 IPs (254 usable)
- /23 = 512 IPs (510 usable)
- /22 = 1024 IPs (1022 usable)
- /21 = 2048 IPs (2046 usable)

**CIDR Calculator**: Use online tools (e.g., subnet-calculator.com) or ipcalc command:
```bash
# Calculate subnet details
ipcalc 10.1.20.0/24

# Output:
# Address:   10.1.20.0
# Netmask:   255.255.255.0 = 24
# Network:   10.1.20.0/24
# Broadcast: 10.1.20.255
# HostMin:   10.1.20.1
# HostMax:   10.1.20.254
# Hosts/Net: 254
```

### Allocate Subnets to Security Zones

**Steps**:

1. **List all security zones** (from Phase 1)
2. **Estimate IP address requirements per zone**:

   - Count current assets
   - Estimate growth (3-5 years)
   - Add 20-30% overhead

3. **Allocate subnets using CIDR**:

   - Choose appropriate subnet size (/24, /23, /22, etc.)
   - Document subnet allocation in IPAM

**Example Subnet Allocation**:

| Security Zone | VLAN ID | Subnet | Usable IPs | Current Usage | Growth Capacity |
|---------------|---------|--------|------------|---------------|-----------------|
| DMZ | 10 | 10.1.10.0/24 | 254 | 15 | 239 |
| Internal - Servers | 20 | 10.1.20.0/24 | 254 | 45 | 209 |
| Internal - Workstations | 30-33 | 10.1.30.0/22 | 1022 | 350 | 672 |
| Management | 40 | 10.1.40.0/24 | 254 | 12 | 242 |
| Guest | 50 | 10.1.50.0/24 | 254 | Variable | N/A |
| Development | 60 | 10.1.60.0/24 | 254 | 20 | 234 |
| IoT/OT | 70 | 10.1.70.0/24 | 254 | 30 | 224 |

### VLAN-to-Subnet Mapping

**Principle**: Each VLAN typically maps to one IP subnet (1:1 mapping simplifies routing).

**Mapping Table**:

| VLAN ID | VLAN Name | Security Zone | IP Subnet | Default Gateway |
|---------|-----------|---------------|-----------|-----------------|
| 10 | DMZ | DMZ | 10.1.10.0/24 | 10.1.10.1 |
| 20 | Servers | Internal | 10.1.20.0/24 | 10.1.20.1 |
| 30 | Workstations | Internal | 10.1.30.0/22 | 10.1.30.1 |
| 40 | Management | Management | 10.1.40.0/24 | 10.1.40.1 |
| 50 | Guest | Guest | 10.1.50.0/24 | 10.1.50.1 |
| 60 | Development | Development | 10.1.60.0/24 | 10.1.60.1 |
| 70 | IoT | IoT/OT | 10.1.70.0/24 | 10.1.70.1 |

**Default Gateway**: Typically the first usable IP in the subnet (router interface or firewall interface).

---

## Phase 3: VLAN Implementation

### VLAN Design Principles

**VLAN Purpose**: Virtual LANs logically separate network traffic at Layer 2 (data link layer).

**VLAN Benefits**:

- **Traffic isolation**: Devices in different VLANs cannot communicate without routing
- **Broadcast domain reduction**: Limits broadcast traffic to VLAN boundaries
- **Flexibility**: Devices in different physical locations can be in same VLAN

**VLAN Numbering**:

- **1**: Default VLAN (do NOT use for production traffic)
- **2-1005**: Normal range VLANs (stored in vlan.dat on switches)
- **1006-4094**: Extended range VLANs (requires VTP transparent or off)
- **Reserved**: 1002-1005 (legacy token ring, FDDI)

**VLAN Naming Convention**:

- Use descriptive names: `VLAN10-DMZ`, `VLAN20-Servers`, `VLAN30-Workstations`
- Include function and/or subnet: `VLAN10-DMZ-10.1.10.0`

### Create VLANs on Switches

**Cisco IOS Switch Example**:

```cisco
! Enter global configuration mode
configure terminal

! Create VLAN 10 (DMZ)
vlan 10
 name DMZ
 exit

! Create VLAN 20 (Servers)
vlan 20
 name Servers
 exit

! Create VLAN 30 (Workstations)
vlan 30
 name Workstations
 exit

! Create VLAN 40 (Management)
vlan 40
 name Management
 exit

! Create VLAN 50 (Guest)
vlan 50
 name Guest
 exit

! Save configuration
end
write memory
```

**Verification**:
```cisco
show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------

1    default                          active    

10   DMZ                              active    
20   Servers                          active    
30   Workstations                     active    
40   Management                       active    
50   Guest                            active    
```

**Generic Steps** (for non-Cisco switches):
1. Access switch management interface (CLI or web GUI)
2. Create VLAN with ID and name
3. Verify VLAN created successfully

### Configure Switchport Access Ports

**Access Port**: Connects to end devices (workstations, servers, printers) - carries traffic for single VLAN.

**Cisco IOS Configuration**:

```cisco
! Configure access port for VLAN 20 (Servers)
interface GigabitEthernet0/1
 description Server-DB01
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast        ! Enable if connecting to end device (not another switch)
 no shutdown
 exit

! Configure access port for VLAN 30 (Workstations)
interface GigabitEthernet0/2
 description Workstation-WS01
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast
 no shutdown
 exit
```

**Port Security** (optional, recommended):
```cisco
interface GigabitEthernet0/1
 switchport port-security
 switchport port-security maximum 1
 switchport port-security violation restrict
 switchport port-security mac-address sticky
```

**Verification**:
```cisco
show interfaces GigabitEthernet0/1 switchport

Name: Gi0/1
Switchport: Enabled
Administrative Mode: access
Operational Mode: access
Access Mode VLAN: 20 (Servers)
```

### Configure Switchport Trunk Ports

**Trunk Port**: Connects to other switches or routers - carries traffic for multiple VLANs (tagged with 802.1Q).

**Cisco IOS Configuration**:

```cisco
! Configure trunk port to another switch
interface GigabitEthernet0/24
 description Trunk-to-Switch2
 switchport mode trunk
 switchport trunk native vlan 999   ! Change native VLAN from default (security)
 switchport trunk allowed vlan 10,20,30,40,50,60,70   ! Explicitly list allowed VLANs
 no shutdown
 exit

! Configure trunk port to router (router-on-a-stick for inter-VLAN routing)
interface GigabitEthernet0/23
 description Trunk-to-Router
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,40,50,60,70
 no shutdown
 exit
```

**Verification**:
```cisco
show interfaces trunk

Port        Mode         Encapsulation  Status        Native vlan
Gi0/23      on           802.1q         trunking      999
Gi0/24      on           802.1q         trunking      999

Port        Vlans allowed on trunk
Gi0/23      10,20,30,40,50,60,70
Gi0/24      10,20,30,40,50,60,70
```

### VLAN Security Best Practices

**CRITICAL Security Configurations**:

1. **Change Native VLAN** (prevent VLAN hopping via double tagging):
```cisco
switchport trunk native vlan 999   ! Use unused VLAN
```

2. **Disable Dynamic Trunking Protocol (DTP)** (prevent trunk negotiation attacks):
```cisco
interface GigabitEthernet0/24
 switchport mode trunk          ! Hardcode trunk mode
 switchport nonegotiate         ! Disable DTP
```

3. **Explicitly Allow VLANs on Trunk** (prevent unauthorised VLAN traffic):
```cisco
switchport trunk allowed vlan 10,20,30,40   ! Only list required VLANs
```

4. **Disable Unused Ports** (prevent rogue devices):
```cisco
interface range GigabitEthernet0/10-20
 shutdown
 switchport mode access
 switchport access vlan 999     ! Move to unused VLAN
```

5. **Implement Private VLANs** (for isolation within same subnet):
```cisco
! Useful for guest Wi-Fi (clients cannot talk to each other)
vlan 50
 private-vlan isolated
```

---

## Phase 4: Firewall Rule Development and Deployment

### Firewall Rule Development Methodology

**Objective**: Create explicit allow rules based on inter-zone traffic policy (default deny).

**Rule Development Process**:

1. **Identify required traffic** (from traffic flow matrix in Phase 1)
2. **Determine source/destination zones and IPs**
3. **Identify protocols and ports required**
4. **Document business justification for rule**
5. **Write firewall rule**
6. **Test rule in staging/lab environment**
7. **Deploy rule to production**
8. **Verify rule effectiveness**

### Firewall Rule Components

**Standard Firewall Rule Format**:

```
Rule ID: [Unique identifier]
Source Zone: [DMZ, Internal, Management, etc.]
Source Address: [IP address or subnet or "any"]
Destination Zone: [DMZ, Internal, Management, etc.]
Destination Address: [IP address or subnet or "any"]
Protocol: [TCP, UDP, ICMP, or "any"]
Destination Port: [Port number or range]
Action: [Allow, Deny]
Logging: [Enabled, Disabled]
Schedule: [Always, or time-based]
Description/Justification: [Business reason for rule]
```

### Example Firewall Rules

**Example 1: Allow Web Servers in DMZ to Access Database in Internal Zone**

```
Rule ID: FW-001
Source Zone: DMZ
Source Address: 10.1.10.10 (web-server-01)
Destination Zone: Internal
Destination Address: 10.1.20.50 (db-server-01)
Protocol: TCP
Destination Port: 3306 (MySQL)
Action: Allow
Logging: Enabled
Schedule: Always
Description: Allow web server to query application database
Justification: Web application requires database access for dynamic content.
             Risk mitigated by: DB user with read-only permissions, 
             SQL injection prevention, source IP restriction.
```

**Example 2: Allow Internal Users to Access Internet (HTTP/HTTPS)**

```
Rule ID: FW-002
Source Zone: Internal
Source Address: 10.1.30.0/22 (workstations)
Destination Zone: Internet
Destination Address: Any
Protocol: TCP
Destination Port: 80, 443
Action: Allow
Logging: Enabled (connections)
Schedule: Always
Description: Allow internal users web browsing
Justification: Business requirement for web access. 
             Risk mitigated by: Web filtering (A.8.23), proxy server, 
             user authentication, content filtering.
```

**Example 3: Deny All Other Traffic (Default Deny)**

```
Rule ID: FW-999
Source Zone: Any
Source Address: Any
Destination Zone: Any
Destination Address: Any
Protocol: Any
Destination Port: Any
Action: Deny
Logging: Enabled (all denied traffic)
Schedule: Always
Description: Default deny rule - block all traffic not explicitly allowed
Justification: Security best practice - default deny policy.
```

### Firewall Rule Ordering

**Critical**: Firewall rules are processed **top-to-bottom**. First matching rule wins.

**Rule Ordering Best Practices**:
1. **Specific rules first** (e.g., allow specific IP → specific IP)
2. **Broader rules next** (e.g., allow subnet → subnet)
3. **Deny rules before allow** (if you want to explicitly deny something that would be caught by broader allow)
4. **Default deny LAST** (catch-all rule)

**Example Rule Order**:
```
1. Deny 10.1.30.100 → Any (malicious workstation quarantine)
2. Allow 10.1.10.10 → 10.1.20.50 TCP/3306 (web → database)
3. Allow 10.1.30.0/22 → Internet TCP/80,443 (workstations → web)
4. Allow 10.1.20.0/24 → 10.1.40.5 TCP/3389 (servers → backup server RDP)
...
999. Deny Any → Any (default deny)
```

### Firewall Rule Documentation

**Template**: See Annex B for Firewall Rule Documentation Template

**Documentation Requirements**:

- Maintain firewall rule inventory (spreadsheet or firewall management tool)
- Each rule must have:
  - Rule ID, source, destination, protocol/port, action
  - Business justification
  - Rule owner (who requested rule)
  - Approval date and approver
  - Last review date
  - Next review date (rules reviewed annually)

### Firewall Configuration Examples

**Cisco ASA Firewall Example**:

```cisco
! Define security zones (interfaces with security levels)
interface GigabitEthernet0/0
 nameif outside
 security-level 0    ! Internet (least trusted)
 ip address 203.0.113.1 255.255.255.0
 
interface GigabitEthernet0/1
 nameif dmz
 security-level 50   ! DMZ (semi-trusted)
 ip address 10.1.10.1 255.255.255.0

interface GigabitEthernet0/2
 nameif inside
 security-level 100  ! Internal (most trusted)
 ip address 10.1.20.1 255.255.255.0

! Define network objects
object network web-server
 host 10.1.10.10
object network db-server
 host 10.1.20.50

! Create ACL to allow DMZ → Internal (web → database)
access-list dmz_in extended permit tcp object web-server object db-server eq 3306

! Apply ACL to DMZ interface
access-group dmz_in in interface dmz

! Enable logging for denied traffic
logging enable
logging trap informational
logging host inside 10.1.40.10
```

**pfSense Firewall Example** (open-source firewall):

1. Navigate to **Firewall > Rules > DMZ**
2. Click **Add** to create new rule:

   - **Action**: Pass
   - **Interface**: DMZ
   - **Protocol**: TCP
   - **Source**: DMZ subnet → 10.1.10.10 (web server)
   - **Destination**: Internal subnet → 10.1.20.50 (database)
   - **Destination Port**: 3306 (MySQL)
   - **Description**: Allow web server to access database
   - **Log**: Enabled

3. Click **Save** and **Apply Changes**

**Generic Firewall Steps**:
1. Access firewall management interface
2. Create security zones (if not already defined)
3. Create network objects (IPs, subnets)
4. Create firewall rules (access lists / security policies)
5. Apply rules to interfaces
6. Enable logging
7. Test rule effectiveness
8. Document rules

---

## Phase 5: ACL Implementation (Optional)

**Access Control Lists (ACLs)** provide additional traffic filtering at router/switch interfaces.

**When to Use ACLs**:

- **Router-based filtering**: Control traffic entering/leaving routers
- **Switch-based filtering**: Control traffic between VLANs (if not using dedicated firewall)
- **Defense in depth**: Additional layer beyond firewall rules

**ACL Types**:

- **Standard ACLs**: Filter based on source IP only (numbered 1-99, 1300-1999)
- **Extended ACLs**: Filter based on source IP, dest IP, protocol, port (numbered 100-199, 2000-2699)

### Standard ACL Example

**Use Case**: Restrict management access to router (only allow management subnet).

**Cisco IOS Configuration**:

```cisco
! Create standard ACL (allow management subnet, deny all else)
access-list 10 permit 10.1.40.0 0.0.0.255
access-list 10 deny any log

! Apply ACL to VTY lines (Telnet/SSH access)
line vty 0 4
 access-class 10 in   ! Only allow IPs from ACL 10
```

### Extended ACL Example

**Use Case**: Control inter-VLAN traffic at router (between Internal and DMZ).

**Cisco IOS Configuration**:

```cisco
! Create extended ACL
ip access-list extended INTERNAL-TO-DMZ
 ! Allow HTTP/HTTPS from internal workstations to DMZ web servers
 permit tcp 10.1.30.0 0.0.3.255 10.1.10.0 0.0.0.255 eq 80
 permit tcp 10.1.30.0 0.0.3.255 10.1.10.0 0.0.0.255 eq 443
 ! Deny all other traffic
 deny ip any any log

! Apply ACL to router interface (outbound on DMZ interface)
interface GigabitEthernet0/0.10   ! Sub-interface for VLAN 10 (DMZ)
 encapsulation dot1Q 10
 ip address 10.1.10.1 255.255.255.0
 ip access-group INTERNAL-TO-DMZ out
```

**Verification**:
```cisco
show ip access-lists INTERNAL-TO-DMZ

Extended IP access list INTERNAL-TO-DMZ
    10 permit tcp 10.1.30.0 0.0.3.255 10.1.10.0 0.0.0.255 eq www (15 matches)
    20 permit tcp 10.1.30.0 0.0.3.255 10.1.10.0 0.0.0.255 eq 443 (8 matches)
    30 deny ip any any log (3 matches)
```

### ACL Best Practices

- **Named ACLs**: Use named ACLs (easier to manage than numbered)
- **ACL placement**: 
  - Standard ACLs: Close to destination
  - Extended ACLs: Close to source
- **Implicit deny**: ACLs have implicit `deny any` at end (explicit deny with log is better)
- **Testing**: Test ACLs in lab before production deployment

---

## Phase 6: Cloud Network Segmentation

### AWS VPC Segmentation

**AWS VPC (Virtual Private Cloud)**: Logically isolated network in AWS cloud.

**Segmentation Components**:

- **VPC**: Top-level container (e.g., 10.100.0.0/16)
- **Subnets**: Segments within VPC (e.g., 10.100.10.0/24 for DMZ subnet)
- **Security Groups**: Instance-level firewall (stateful)
- **Network ACLs (NACLs)**: Subnet-level firewall (stateless)
- **Route Tables**: Control traffic routing between subnets

**Example VPC Architecture**:

```
AWS VPC: 10.100.0.0/16

├─ Public Subnet (DMZ): 10.100.10.0/24
│  ├─ Internet Gateway attached (for internet access)
│  ├─ Web servers (EC2 instances)
│  └─ Security Group: Allow TCP/80,443 from 0.0.0.0/0

├─ Private Subnet (Internal): 10.100.20.0/24
│  ├─ No Internet Gateway (no direct internet access)
│  ├─ Application servers (EC2 instances)
│  └─ Security Group: Allow TCP/3306 from Public Subnet

└─ Management Subnet: 10.100.40.0/24
   ├─ Bastion host (jump server)
   └─ Security Group: Allow SSH from corporate IP only
```

**AWS CLI Example** (create VPC and subnets):

```bash
# Create VPC
aws ec2 create-vpc --cidr-block 10.100.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Prod-VPC}]'

# Create Public Subnet (DMZ)
aws ec2 create-subnet --vpc-id vpc-xxxxx --cidr-block 10.100.10.0/24 --availability-zone us-east-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-DMZ}]'

# Create Private Subnet (Internal)
aws ec2 create-subnet --vpc-id vpc-xxxxx --cidr-block 10.100.20.0/24 --availability-zone us-east-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Private-Internal}]'

# Create Internet Gateway (for public subnet)
aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=Prod-IGW}]'
aws ec2 attach-internet-gateway --vpc-id vpc-xxxxx --internet-gateway-id igw-xxxxx
```

**Security Group Example** (allow web traffic to web servers):

```bash
# Create security group
aws ec2 create-security-group --group-name web-sg --description "Web server security group" --vpc-id vpc-xxxxx

# Allow HTTP from anywhere
aws ec2 authorise-security-group-ingress --group-id sg-xxxxx --protocol tcp --port 80 --cidr 0.0.0.0/0

# Allow HTTPS from anywhere
aws ec2 authorise-security-group-ingress --group-id sg-xxxxx --protocol tcp --port 443 --cidr 0.0.0.0/0

# Allow SSH from management subnet only
aws ec2 authorise-security-group-ingress --group-id sg-xxxxx --protocol tcp --port 22 --cidr 10.100.40.0/24
```

**Terraform Example** (infrastructure-as-code):

```hcl
# VPC
resource "aws_vpc" "prod" {
  cidr_block = "10.100.0.0/16"
  tags = {
    Name = "Prod-VPC"
  }
}

# Public Subnet (DMZ)
resource "aws_subnet" "dmz" {
  vpc_id            = aws_vpc.prod.id
  cidr_block        = "10.100.10.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "Public-DMZ"
  }
}

# Security Group for Web Servers
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Web server security group"
  vpc_id      = aws_vpc.prod.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

### Azure VNet Segmentation

**Azure VNet (Virtual Network)**: Logically isolated network in Azure cloud.

**Segmentation Components**:

- **VNet**: Top-level container (e.g., 10.200.0.0/16)
- **Subnets**: Segments within VNet (e.g., 10.200.10.0/24)
- **Network Security Groups (NSGs)**: Firewall rules (can apply to subnet or NIC)
- **Application Security Groups (ASGs)**: Group instances for easier rule management

**Azure CLI Example**:

```bash
# Create VNet
az network vnet create --name Prod-VNet --resource-group Prod-RG --location eastus --address-prefix 10.200.0.0/16

# Create DMZ Subnet
az network vnet subnet create --name DMZ-Subnet --resource-group Prod-RG --vnet-name Prod-VNet --address-prefix 10.200.10.0/24

# Create Internal Subnet
az network vnet subnet create --name Internal-Subnet --resource-group Prod-RG --vnet-name Prod-VNet --address-prefix 10.200.20.0/24

# Create NSG for DMZ
az network nsg create --name DMZ-NSG --resource-group Prod-RG --location eastus

# Add rule to allow HTTP
az network nsg rule create --name Allow-HTTP --nsg-name DMZ-NSG --resource-group Prod-RG --priority 100 --source-address-prefixes '*' --destination-port-ranges 80 --access Allow --protocol Tcp

# Associate NSG with subnet
az network vnet subnet update --name DMZ-Subnet --resource-group Prod-RG --vnet-name Prod-VNet --network-security-group DMZ-NSG
```

### GCP VPC Segmentation

**GCP VPC (Virtual Private Cloud)**: Global network resource in GCP.

**Segmentation Components**:

- **VPC Network**: Global (not regional)
- **Subnets**: Regional (e.g., 10.300.10.0/24 in us-east1)
- **Firewall Rules**: Applied to VPC (tag-based or IP-based)

**GCP CLI Example**:

```bash
# Create VPC
gcloud compute networks create prod-vpc --subnet-mode=custom

# Create DMZ Subnet
gcloud compute networks subnets create dmz-subnet --network=prod-vpc --region=us-east1 --range=10.300.10.0/24

# Create Internal Subnet
gcloud compute networks subnets create internal-subnet --network=prod-vpc --region=us-east1 --range=10.300.20.0/24

# Create firewall rule to allow HTTP
gcloud compute firewall-rules create allow-http --network=prod-vpc --allow=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=web-server

# Create firewall rule to deny all else (implicit in GCP, but explicit rule for logging)
gcloud compute firewall-rules create deny-all --network=prod-vpc --action=deny --rules=all --source-ranges=0.0.0.0/0 --priority=65534 --enable-logging
```

---

## Phase 7: Segmentation Testing and Validation

**Objective**: Verify that segmentation controls are working as intended.

### Inter-Zone Traffic Testing

**Test Allowed Traffic**:

```bash
# From workstation in Internal zone (10.1.30.50) to web server in DMZ (10.1.10.10)
# This should be ALLOWED per firewall rules

# Test HTTP connectivity
curl http://10.1.10.10
# Expected: HTTP response (success)

# Test HTTPS connectivity
curl https://10.1.10.10
# Expected: HTTPS response (success)
```

**Test Denied Traffic**:

```bash
# From workstation in Internal zone (10.1.30.50) to management server in Mgmt zone (10.1.40.10)
# This should be DENIED per firewall rules (workstations should not access management)

# Test SSH connectivity
telnet 10.1.40.10 22
# Expected: Connection timeout or connection refused (denied by firewall)

# Verify firewall log shows denied traffic
# Check firewall logs for deny entries
```

### Lateral Movement Simulation

**Objective**: Simulate attacker lateral movement to test segmentation effectiveness.

**Scenario**: Assume workstation in Internal zone (10.1.30.50) is compromised. Can attacker move to other zones?

**Test Procedure**:

1. **From compromised workstation, attempt to access other zones**:
```bash
# Attempt SSH to management zone
ssh admin@10.1.40.10
# Expected: Connection denied by firewall

# Attempt RDP to DMZ server
rdesktop 10.1.10.10
# Expected: Connection denied by firewall

# Attempt database connection to Internal server (should be allowed if workstation is authorised)
mysql -h 10.1.20.50 -u user -p
# Expected: Connection allowed if workstation is authorised; denied otherwise
```

2. **Verify firewall logs**:

   - Check firewall logs for denied connection attempts
   - Alert security team if unexpected denials occur (may indicate attack)

### VLAN Hopping Prevention Testing

**VLAN Hopping Attacks**:

- **Double Tagging**: Attacker sends double-tagged 802.1Q frame to access other VLANs
- **Switch Spoofing**: Attacker negotiates trunk with switch (via DTP) to access all VLANs

**Prevention Measures** (implemented in Phase 3):

- Change native VLAN to unused VLAN (not VLAN 1)
- Disable DTP (`switchport nonegotiate`)
- Explicitly allow VLANs on trunk ports

**Testing**:

1. **Attempt DTP negotiation** (using Yersinia tool):
```bash
# From attacker machine connected to access port
sudo yersinia -G   # Launch GUI
# Select DTP attack → Attempt to negotiate trunk
# Expected: Attack fails (DTP disabled)
```

2. **Attempt double tagging**:
```bash
# Use Scapy to craft double-tagged frame
sudo scapy
>>> sendp(Ether()/Dot1Q(vlan=1)/Dot1Q(vlan=20)/IP(dst="10.1.20.50")/ICMP())
# Expected: Frame dropped by switch (native VLAN != 1, double tagging fails)
```

**Verification**: Monitor switch logs for suspicious activity.

### Packet Capture Verification

**Objective**: Verify that only authorised traffic flows between zones.

**Procedure**:

1. **Capture traffic at zone boundary** (firewall or router):
```bash
# On firewall/router, capture traffic between DMZ and Internal
tcpdump -i eth0 -n host 10.1.10.10 and host 10.1.20.50 -w dmz-internal.pcap
```

2. **Analyze capture** (using Wireshark or tcpdump):
```bash
# View captured traffic
tcpdump -r dmz-internal.pcap -n
# Expected: Only authorised traffic (e.g., TCP/3306 from web server to database)
#           No unauthorised traffic (e.g., SSH, RDP, ICMP)
```

3. **Verify traffic matches firewall rules**:

   - All captured traffic should match ALLOW rules
   - No traffic should match DENY rules (would be dropped before capture)

---

## Phase 8: Migration to Segmented Network

**Objective**: Migrate from flat network to segmented network with minimal disruption.

### Assess Current Network (Flat Network Identification)

**Steps**:

1. **Document current network topology**:

   - Single subnet or multiple subnets?
   - Any existing VLANs?
   - Any existing firewall rules?

2. **Identify flat networks** (no segmentation):

   - All devices in single subnet (e.g., 192.168.1.0/24)
   - No VLANs or all devices in default VLAN (VLAN 1)
   - No firewall rules (or overly permissive rules)

3. **Risk assessment**:

   - High-value assets in flat network? (servers, databases)
   - Regulatory data in flat network? (PII, PCI, PHI)
   - External exposure risk? (internet-facing systems in same flat network as internal)

### Develop Phased Migration Plan

**Phased Approach** (minimise disruption):

**Phase 1: High-Value Assets First**

- Segment critical servers (databases, domain controllers, financial systems)
- Create Management zone and move management systems (monitoring, backup)

**Phase 2: External-Facing Assets**

- Create DMZ zone and move internet-facing systems (web servers, mail relays)
- Implement strict firewall rules between DMZ and Internal

**Phase 3: User Workstations**

- Create Internal zone and segment workstations
- Implement firewall rules for workstation access

**Phase 4: Specialized Zones**

- Create Guest, Development, IoT/OT zones as needed
- Migrate respective assets

**Phase 5: Finalize and Harden**

- Review all firewall rules
- Remove overly permissive rules
- Implement default deny policy
- Conduct penetration testing

### Migration Execution

**For Each Phase**:

1. **Pre-migration**:

   - Document current state (IP addresses, connectivity)
   - Create VLANs and subnets for new zone
   - Develop firewall rules for new zone
   - Test firewall rules in staging environment
   - Schedule migration window (off-hours, low-usage period)

2. **Migration**:

   - Change switchport VLAN assignment (move device to new VLAN)
   - Update device IP address (if changing subnet)
   - Update default gateway (if changing gateway)
   - Deploy firewall rules
   - Test connectivity (verify device can access required resources)

3. **Post-migration**:

   - Verify device connectivity (ping, application testing)
   - Monitor firewall logs (look for denied traffic that should be allowed)
   - Document migration completion
   - Adjust firewall rules if needed (based on legitimate traffic denied)

**Example Migration** (moving database server from flat network to Internal zone):

**Before**:

- Server: `db-server-01`, IP: `192.168.1.50`, VLAN: 1 (default), Subnet: 192.168.1.0/24

**After**:

- Server: `db-server-01`, IP: `10.1.20.50`, VLAN: 20 (Servers), Subnet: 10.1.20.0/24

**Migration Steps**:

1. Create VLAN 20 (Servers) on switches
2. Configure router sub-interface for VLAN 20 (gateway: 10.1.20.1)
3. Create firewall rules:

   - Allow web servers (10.1.10.0/24) → database (10.1.20.50) TCP/3306
   - Allow workstations (10.1.30.0/22) → database (10.1.20.50) TCP/3306 (if needed)
   - Deny all other traffic to database

4. During maintenance window:

   - Change switchport VLAN to 20
   - Change server IP to 10.1.20.50, gateway to 10.1.20.1
   - Test connectivity (web server can connect to database)
   - Monitor application logs for errors

5. Document migration completion

### Rollback Plan

**If migration fails**:

1. **Revert switchport VLAN** (move back to original VLAN)
2. **Revert IP address** (change back to original IP)
3. **Remove firewall rules** (if causing issues)
4. **Investigate failure** (what went wrong?)
5. **Revise migration plan** (adjust approach)
6. **Retry migration** (after resolving issues)

---

# Automation Opportunities

## Infrastructure-as-Code (IaC)

**Terraform**: Manage network infrastructure across cloud providers (AWS, Azure, GCP) and on-premise (vSphere).

**Example**: Define VPC, subnets, security groups in Terraform config:

```hcl
# terraform/main.tf
provider "aws" {
  region = "us-east-1"
}

# Import network segmentation module
module "network_segmentation" {
  source = "./modules/network_segmentation"
  
  vpc_cidr    = "10.100.0.0/16"
  dmz_subnet  = "10.100.10.0/24"
  int_subnet  = "10.100.20.0/24"
  mgmt_subnet = "10.100.40.0/24"
}
```

**Benefits**:

- Version control for network configs (Git)
- Repeatable deployments (dev, staging, prod environments)
- Automated testing (terraform plan before apply)

## Configuration Management (Ansible)

**Ansible**: Automate network device configurations (VLANs, ACLs, firewall rules).

**Example Playbook**: Create VLANs on Cisco switches:

```yaml
# ansible/create_vlans.yml

- name: Configure VLANs on Cisco switches

  hosts: cisco_switches
  gather_facts: no
  tasks:

    - name: Create VLAN 10 (DMZ)

      cisco.ios.ios_vlans:
        config:

          - vlan_id: 10

            name: DMZ
        state: merged

    - name: Create VLAN 20 (Servers)

      cisco.ios.ios_vlans:
        config:

          - vlan_id: 20

            name: Servers
        state: merged

    - name: Save configuration

      cisco.ios.ios_command:
        commands:

          - write memory

```

**Run Playbook**:
```bash
ansible-playbook -i inventory create_vlans.yml
```

## Firewall Rule Automation

**Capirca**: Generate firewall rules from high-level policies (supports multiple vendors: Cisco ASA, pfSense, iptables, AWS, GCP).

**Example Policy File** (Capirca format):

```
# policies/dmz_to_internal.pol
term allow-web-to-db {
  comment:: "Allow web servers to access database"
  source-address:: WEB_SERVERS
  destination-address:: DB_SERVER
  protocol:: tcp
  destination-port:: 3306
  action:: accept
}

term default-deny {
  comment:: "Default deny"
  action:: deny
}
```

**Generate Firewall Config**:
```bash
# Generate Cisco ASA config
aclgen --definitions=definitions.yaml --policy=dmz_to_internal.pol --output=cisco_asa

# Generate iptables config
aclgen --definitions=definitions.yaml --policy=dmz_to_internal.pol --output=iptables
```

---

# Integration with Other Processes

## Network Discovery (ISMS-IMP-A.8.20-21-22-S1)

**Integration**: Segmentation planning requires accurate network inventory.

- Use network discovery data to identify assets for segmentation
- IPAM data informs subnet design
- Device inventory informs zone assignment

## Device Hardening (ISMS-IMP-A.8.20-21-22-S3)

**Integration**: Segmentation devices (switches, routers, firewalls) must be hardened.

- Hardening baselines include segmentation security (VLAN security, ACLs)
- Configuration management ensures segmentation configs are maintained

## Network Security Testing (ISMS-IMP-A.8.20-21-22-S6)

**Integration**: Segmentation effectiveness is validated through testing.

- Vulnerability scanning tests segmentation controls
- Penetration testing simulates lateral movement
- Segmentation testing (Phase 7) is part of overall security testing process

## Logging and Monitoring (A.8.15, A.8.16)

**Integration**: Firewall logs and network traffic monitoring detect segmentation violations.

- Firewall logs capture denied traffic (attempted segmentation violations)
- SIEM alerts on suspicious inter-zone traffic
- Network traffic analysis (NetFlow/sFlow) monitors traffic patterns

---

# Quality Assurance

## Verification Checklist

**After implementing segmentation**:

- [ ] Security zones defined and documented
- [ ] Inter-zone traffic policies documented (traffic flow matrix)
- [ ] IP address allocation documented (IPAM)
- [ ] VLANs created on all switches
- [ ] Switchports configured (access and trunk ports)
- [ ] VLAN security implemented (native VLAN changed, DTP disabled)
- [ ] Firewall rules created and tested
- [ ] ACLs implemented (if applicable)
- [ ] Cloud segmentation implemented (if applicable)
- [ ] Segmentation testing completed (inter-zone traffic, lateral movement, VLAN hopping)
- [ ] Packet captures verified (only authorised traffic flows)
- [ ] Segmentation architecture documented (diagrams, zone definitions)
- [ ] Firewall rule documentation complete (justifications, approvals)
- [ ] Configuration backups completed (switches, routers, firewalls)

## Validation Procedures

**Post-Implementation Validation**:

1. **Connectivity Testing**: Verify all authorised traffic flows (applications work as expected)
2. **Security Testing**: Verify unauthorised traffic is blocked (attempt lateral movement)
3. **Performance Testing**: Verify segmentation does not degrade network performance (latency, throughput)
4. **Documentation Review**: Verify all segmentation documentation is complete and accurate
5. **Configuration Audit**: Verify configurations match design (no configuration drift)

---

# Common Pitfalls and Solutions

## Common Mistakes

**Mistake 1: Overly Complex Segmentation**

- **Problem**: Too many zones, overly granular segmentation → difficult to manage
- **Solution**: Start with high-level zones (DMZ, Internal, Management); add more zones as needed

**Mistake 2: Firewall Rule Explosion**

- **Problem**: Too many firewall rules → difficult to manage, performance impact
- **Solution**: Use network objects, service groups, rule consolidation

**Mistake 3: Undocumented Firewall Rules**

- **Problem**: "What does this rule do? Why is it here?" → cannot remove obsolete rules
- **Solution**: Mandatory rule documentation (justification, owner, approval)

**Mistake 4: No Default Deny**

- **Problem**: Implicit allow-all → segmentation ineffective
- **Solution**: Always implement default deny rule (explicit deny-all at end of ruleset)

**Mistake 5: Not Testing Segmentation**

- **Problem**: Assume segmentation works → actually has gaps
- **Solution**: Regular segmentation effectiveness testing (penetration testing, lateral movement simulation)

**Mistake 6: Flat Network in Cloud**

- **Problem**: All cloud resources in single VPC/VNet with no security groups → flat network
- **Solution**: Implement cloud segmentation (security groups, NACLs, VPC design)

**Mistake 7: Forgetting Management Traffic**

- **Problem**: Segmentation blocks legitimate management traffic (monitoring, backups, patching)
- **Solution**: Design Management zone with appropriate access rules

**Mistake 8: No Segmentation for Development/Test**

- **Problem**: Development systems in production network → lateral movement risk
- **Solution**: Separate Development zone, isolated from production

## Troubleshooting Guide

**Issue 1: Application Breaks After Segmentation**

- **Symptoms**: Application stops working after migration to segmented network
- **Diagnosis**:
  - Check firewall logs for denied traffic
  - Identify missing firewall rules (application requires additional ports)
- **Solution**:
  - Add firewall rules for legitimate traffic
  - Test rule before deploying to production
  - Document rule justification

**Issue 2: Firewall Performance Degradation**

- **Symptoms**: Network slow after implementing firewall rules
- **Diagnosis**:
  - Check firewall CPU/memory utilization
  - Count number of firewall rules (too many?)
  - Identify complex rules (regex patterns, deep packet inspection)
- **Solution**:
  - Optimize firewall rules (consolidate, use rule groups)
  - Upgrade firewall hardware/software (if needed)
  - Implement rule cleanup (remove obsolete rules)

**Issue 3: VLAN Hopping Successful**

- **Symptoms**: Attacker can access other VLANs from compromised device
- **Diagnosis**:
  - Check if native VLAN = VLAN 1 (vulnerable to double tagging)
  - Check if DTP enabled (vulnerable to switch spoofing)
- **Solution**:
  - Change native VLAN to unused VLAN (e.g., 999)
  - Disable DTP (`switchport nonegotiate`)
  - Re-test VLAN hopping (should now fail)

**Issue 4: Segmentation Testing Finds Gaps**

- **Symptoms**: Penetration testing reveals lateral movement is still possible
- **Diagnosis**:
  - Identify path used for lateral movement
  - Check firewall rules and ACLs for overly permissive rules
- **Solution**:
  - Tighten firewall rules (remove broad allow rules)
  - Implement additional ACLs
  - Re-test segmentation (should now block lateral movement)

---

# Documentation Requirements

## Segmentation Architecture Documentation

**Required Documentation**:

1. **Security Zone Definition Document**:

   - Zone name, purpose, trust level
   - Assets in each zone
   - Data classification of data in zone
   - Zone owner

2. **Network Segmentation Diagram**:

   - Visual representation of zones
   - Trust boundaries and firewalls
   - Traffic flows between zones

3. **Inter-Zone Traffic Policy**:

   - Traffic flow matrix (allow/deny)
   - Detailed justification for each allow rule
   - Protocols/ports required

4. **IP Address Management (IPAM) Documentation**:

   - Subnet allocations per zone
   - VLAN-to-subnet mapping
   - IP address ranges

5. **Firewall Rule Inventory**:

   - All firewall rules documented
   - Rule ID, source, destination, protocol/port, action
   - Business justification, rule owner, approval date

6. **VLAN Configuration Documentation**:

   - VLAN list (ID, name, purpose)
   - Switchport configurations
   - Trunk configurations

## Change Management Documentation

**For each segmentation change**:

- Change request (what is being changed, why)
- Impact assessment (what systems/users affected)
- Rollback plan (how to revert if change fails)
- Approval (who approved change, when)
- Implementation log (what was done, when, by whom)
- Post-implementation validation (was change successful?)

## Documentation Storage

**Centralized Documentation Repository**:

- SharePoint, Confluence, or similar documentation platform
- Version control (track changes over time)
- Access control (restrict access to authorised personnel)

---

# Continuous Improvement

## Periodic Review

**Quarterly Review**:

- Review firewall rules (identify obsolete rules)
- Review security zones (do they still align with business needs?)
- Review IPAM (is IP allocation still appropriate?)

**Annual Review**:

- Full segmentation architecture review
- Penetration testing to validate segmentation effectiveness
- Update documentation (reflect current state)

## Metrics to Track

- **Segmentation Coverage**: Percentage of network that is segmented (goal: 100%)
- **Flat Networks**: Count of flat networks (goal: 0)
- **Firewall Rule Count**: Total firewall rules (track growth, consolidate if excessive)
- **Firewall Rule Age**: Age of oldest firewall rule (identify obsolete rules)
- **Denied Traffic**: Count of denied firewall events (high count may indicate legitimate traffic being blocked)
- **Segmentation Testing**: Date of last segmentation effectiveness test (goal: annual minimum)

## Lessons Learned

**After Each Segmentation Project**:

- Document lessons learned (what went well, what didn't)
- Update segmentation procedures based on lessons learned
- Share knowledge with team (training, documentation updates)

---

# Annexes

## Annex A: Zone Definition Template

```
Security Zone Definition: [Zone Name]

Zone ID: [Unique identifier, e.g., ZONE-001]
Zone Name: [Descriptive name, e.g., DMZ]
Trust Level: [Untrusted, Semi-Trusted, Trusted, Highly Trusted]
Purpose: [Brief description of zone purpose]

Assets in Zone:

- [List of assets, e.g., web-server-01, web-server-02]
- [Asset types: servers, workstations, network devices, etc.]

Data Classification:

- Primary: [Public, Internal, Confidential, Restricted]
- Secondary: [If zone contains mixed classifications]

Network Details:

- VLAN ID: [VLAN number]
- Subnet: [IP subnet in CIDR notation]
- Default Gateway: [Gateway IP address]

Inter-Zone Traffic Policies:

- Allowed Inbound: [Zones that can send traffic to this zone]
  - [Zone Name]: [Protocols/ports allowed]
- Allowed Outbound: [Zones that this zone can send traffic to]
  - [Zone Name]: [Protocols/ports allowed]

Zone Owner:

- Business Owner: [Name, title]
- Technical Owner: [Name, title]

Last Review Date: [Date]
Next Review Date: [Date + 12 months]
```

## Annex B: Firewall Rule Documentation Template

```
Firewall Rule: [Rule ID]

Rule ID: [Unique identifier, e.g., FW-001]
Firewall Device: [Device name/IP]
Rule Position: [Rule order in ruleset, e.g., #5]

Traffic Details:

- Source Zone: [Zone name]
- Source Address: [IP/subnet or "any"]
- Destination Zone: [Zone name]
- Destination Address: [IP/subnet or "any"]
- Protocol: [TCP, UDP, ICMP, or "any"]
- Destination Port: [Port number/range]
- Action: [Allow, Deny]

Logging:

- Logging Enabled: [Yes/No]
- Log Level: [Informational, Warning, etc.]

Schedule:

- Always Active: [Yes/No]
- Time-Based: [If applicable, specify schedule]

Justification:

- Business Justification: [Why is this rule needed?]
- Technical Justification: [What traffic does this enable?]
- Risk Assessment: [What risks does this introduce? How mitigated?]

Ownership and Approval:

- Rule Requester: [Name, title]
- Rule Owner: [Name, title]
- Approved By: [Name, title]
- Approval Date: [Date]

Review Cycle:

- Last Review Date: [Date]
- Next Review Date: [Date + 12 months]

Status:

- Active: [Yes/No]
- Obsolete: [Yes/No - if Yes, explain why and removal date]

```

## Annex C: Segmentation Testing Checklist

```
Segmentation Effectiveness Testing Checklist

Test Date: [Date]
Tester: [Name]
Test Scope: [Zones tested]

1. Inter-Zone Traffic Testing

   - [ ] Test allowed traffic flows (verify applications work)
   - [ ] Test denied traffic (verify unauthorised traffic blocked)
   - [ ] Review firewall logs (verify denials logged)

2. Lateral Movement Simulation

   - [ ] Simulate compromised workstation (attempt to access other zones)
   - [ ] Verify segmentation blocks lateral movement
   - [ ] Document findings

3. VLAN Hopping Prevention

   - [ ] Test double tagging attack (should fail)
   - [ ] Test switch spoofing attack (should fail)
   - [ ] Verify native VLAN != VLAN 1
   - [ ] Verify DTP disabled on all ports

4. Packet Capture Verification

   - [ ] Capture traffic at zone boundaries
   - [ ] Analyze traffic (verify only authorised traffic flows)
   - [ ] Document findings

5. Configuration Audit

   - [ ] Verify firewall rules match documentation
   - [ ] Verify VLAN configs match documentation
   - [ ] Verify no configuration drift

6. Documentation Review

   - [ ] Verify segmentation architecture documentation up-to-date
   - [ ] Verify firewall rule documentation up-to-date
   - [ ] Verify IPAM documentation up-to-date

Test Results:

- Pass/Fail: [Overall result]
- Gaps Identified: [List any gaps found]
- Remediation Plan: [How to address gaps]

Next Test Date: [Date + 12 months]
```

---

# Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Implementation Team | Initial release |

---

**END OF DOCUMENT**

---

**END OF USER GUIDE**

---

*"Divide and isolate: the first principle of network defence."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
