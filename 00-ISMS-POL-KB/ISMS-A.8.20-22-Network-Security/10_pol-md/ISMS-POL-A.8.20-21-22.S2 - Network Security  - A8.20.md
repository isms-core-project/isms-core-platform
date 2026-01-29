# ISMS-POL-A.8.20-21-22-S2
## Network Security Requirements (A.8.20)

**Document ID**: ISMS-POL-A.8.20-21-22-S2  
**Title**: Network Security Requirements (ISO/IEC 27001:2022 Control A.8.20)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Network Security Manager | Initial network security requirements (A.8.20) |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Network Operations Manager
- Implementation Review: Network Administrators

**Distribution**: Network team, security team, IT operations, auditors  
**Related Documents**: ISMS-POL-A.8.20-21-22 (Master), ISMS-POL-A.8.20-21-22-S1 (Executive Summary)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.20

**Official Control Text**:

> *Networks and network devices should be secured, managed and controlled to protect information in systems and applications.*

**Control Purpose**: Ensure network infrastructure and devices are hardened, monitored, and configured to prevent unauthorized access, protect information in transit, and maintain network integrity and availability.

**Why This Matters**:

Network infrastructure forms the foundation for all information systems. Compromised network devices or insecure network configurations enable attackers to:
- Intercept sensitive data in transit (eavesdropping)
- Modify data in transit (man-in-the-middle attacks)
- Pivot between systems (lateral movement)
- Establish persistent access (backdoors in network devices)
- Disrupt operations (denial-of-service, routing attacks)
- Bypass application-layer security controls

Secure network infrastructure reduces these risks and provides defense in depth.

### 1.2 Scope of A.8.20 Requirements

This section defines mandatory requirements for:

1. **Network Topology Documentation** - Understanding network architecture
2. **Network Device Inventory** - Knowing what devices exist
3. **Network Device Hardening** - Securing device configurations
4. **Network Perimeter Controls** - Protecting the network boundary
5. **Network Access Controls** - Controlling who can access the network
6. **Network Monitoring and Logging** - Detecting threats and incidents
7. **Configuration Management** - Maintaining secure configurations
8. **Wireless Network Security** - Securing wireless networks
9. **Remote Access Security** - Securing VPN and remote access

### 1.3 Integration with A.8.21 and A.8.22

While A.8.20 focuses on network infrastructure and devices:
- **A.8.21** addresses security of services running on this infrastructure (DNS, DHCP, NTP, etc.)
- **A.8.22** addresses how this infrastructure is segmented (security zones, VLANs, firewalls)

All three controls share the same network topology and devices but have distinct requirements for audit purposes.

---

## 2. Network Topology Documentation

### 2.1 Requirement: Network Architecture Documentation

**REQ-A820-001**: [Organization] **MUST** maintain current network topology documentation covering all network infrastructure.

**Minimum Documentation Requirements**:

1. **Physical Topology**:
   - Physical network devices and their locations (data centers, offices, branches)
   - Physical connections between devices (fiber, copper, wireless links)
   - Rack diagrams for data center equipment
   - WAN connectivity (MPLS, internet circuits, point-to-point links)

2. **Logical Topology**:
   - IP addressing scheme (subnets, VLAN assignments)
   - Routing topology (OSPF, BGP, static routes)
   - Layer 2 topology (VLANs, trunks, spanning tree)
   - Security zones and trust boundaries (see A.8.22)

3. **Network Services Topology**:
   - DNS infrastructure (authoritative, recursive, forwarders)
   - DHCP infrastructure (servers, scopes, relay agents)
   - Load balancer placement and virtual IPs
   - VPN concentrator locations and remote access paths

4. **Data Flow Diagrams**:
   - Critical application traffic flows
   - Inter-zone traffic patterns
   - Internet ingress/egress paths
   - Backup/replication traffic flows

**Documentation Standards**:
- Diagrams created using standard tools (Visio, draw.io, Lucidchart, or equivalent)
- Standardized symbols and color coding
- Layer separation (physical, logical, security views)
- Version control and change tracking

**Update Frequency**:
- **Immediate**: After any major network change (new zones, new devices, topology changes)
- **Quarterly**: Routine verification and update
- **Post-incident**: After significant security incidents

**Audit Evidence**: Current network topology diagrams (physical, logical, security views)

### 2.2 Requirement: Network Discovery and Validation

**REQ-A820-002**: [Organization] **MUST** perform periodic network discovery to validate topology documentation accuracy.

**Discovery Methods**:
- Automated network scanning (nmap, network discovery tools)
- SNMP-based discovery
- NetFlow/sFlow traffic analysis
- Cloud API-based discovery (AWS, Azure, GCP)
- Configuration parsing (extract topology from device configs)

**Discovery Frequency**:
- **Quarterly**: Full network discovery across all segments
- **Monthly**: Discovery of critical segments (DMZ, management network)
- **Continuous**: Passive traffic analysis for anomaly detection

**Discovery Validation**:
- Compare discovery results to documentation
- Flag undocumented devices ("shadow devices")
- Update documentation to reflect reality
- Investigate and remediate unauthorized devices

**Audit Evidence**: Network discovery reports, documentation update logs

---

## 3. Network Device Inventory

### 3.1 Requirement: Comprehensive Device Inventory

**REQ-A820-003**: [Organization] **MUST** maintain a comprehensive inventory of all network devices.

**Devices In-Scope**:
- Routers (edge, core, distribution)
- Switches (core, distribution, access)
- Firewalls (perimeter, inter-zone, host-based)
- Wireless access points and controllers
- Load balancers (hardware, virtual, cloud)
- VPN concentrators (SSL VPN, IPsec VPN)
- Network security appliances (IPS/IDS, DLP, network sandboxes)
- Network management systems (NMS, SNMP managers)
- Cloud network devices (virtual routers, virtual firewalls, transit gateways)

**Inventory Attributes (Minimum)**:
- Device ID (unique identifier)
- Device type (router, switch, firewall, etc.)
- Make and model
- Hostname
- Primary IP address
- Management IP address (if different)
- Physical location (data center, building, rack)
- Logical location (network zone, VLAN)
- Device purpose/function
- Criticality classification (critical, high, medium, low)
- Owner/responsible party
- Firmware/software version
- Last discovery date
- Last security assessment date
- Compliance status

**Inventory Management**:
- Centralized inventory system (CMDB, spreadsheet, database)
- Inventory updated from network discovery (automated integration)
- Manual updates for devices not discoverable via network
- Decommissioned devices removed promptly

**Criticality Classification Criteria**:
- **Critical**: Single point of failure; compromise impacts entire network or critical services
- **High**: Compromise impacts multiple systems or sensitive data
- **Medium**: Compromise impacts specific segment or non-critical systems
- **Low**: Compromise has minimal impact

**Audit Evidence**: Network device inventory (Assessment Workbook 1)

### 3.2 Requirement: Asset Ownership and Accountability

**REQ-A820-004**: Every network device **MUST** have a designated owner and responsible party.

**Ownership Responsibilities**:
- **Device Owner**: Business accountability for device purpose and risk acceptance
- **Responsible Administrator**: Technical accountability for device security and operations

**Owner Obligations**:
- Approve device deployment and configuration
- Approve security exceptions (if any)
- Review device security assessments
- Accept residual risk for non-compliance

**Administrator Obligations**:
- Implement and maintain device hardening
- Perform configuration changes per change management
- Monitor device health and security
- Respond to device-related incidents
- Maintain device documentation

**Audit Evidence**: Ownership records in device inventory, responsibility matrix

---

## 4. Network Device Hardening

### 4.1 Requirement: Hardening Baselines

**REQ-A820-005**: [Organization] **MUST** establish and apply hardening baselines for all network device types.

**Baseline Sources**:
- CIS Benchmarks for network devices (Cisco, Juniper, Palo Alto, etc.)
- Vendor-specific hardening guides
- NIST guidelines (if applicable)
- Industry best practices
- [Organization]-specific customizations

**Baseline Development Process**:
1. Select authoritative hardening guide (CIS, vendor guide)
2. Customize for [Organization]'s environment (risk-based decisions)
3. Document customizations and justifications
4. Obtain CISO approval for baseline
5. Version control baseline documents
6. Review and update baselines annually

**Device-Specific Baselines**:
- Separate baselines per device type (routers, switches, firewalls, wireless APs)
- Separate baselines per device role (edge vs. core vs. access)
- Cloud-specific baselines (AWS security groups, Azure NSGs, GCP firewall rules)

**Audit Evidence**: Hardening baseline documents, baseline approval records

### 4.2 Requirement: Authentication and Access Control

**REQ-A820-006**: Network devices **MUST** enforce strong authentication for administrative access.

**Mandatory Authentication Requirements**:

1. **No Default Credentials**:
   - Default usernames and passwords **MUST** be changed immediately upon device deployment
   - Default accounts **MUST** be disabled if not needed
   - Vendor default accounts (e.g., "admin", "cisco", "root") **MUST** be renamed or disabled

2. **Strong Password Policies**:
   - Minimum 12 characters (15 characters recommended)
   - Complexity requirements (uppercase, lowercase, numbers, special characters)
   - Password expiration (90 days maximum for local accounts)
   - Password history (minimum 5 passwords remembered)
   - Account lockout after 5 failed attempts

3. **Multi-Factor Authentication (MFA)**:
   - MFA **MUST** be enabled for all administrative access to critical and high-criticality devices
   - MFA **SHOULD** be enabled for all devices where technically feasible
   - Acceptable MFA methods: Time-based OTP (TOTP), hardware tokens, smart cards
   - SMS-based MFA is discouraged (known vulnerabilities)

4. **Centralized Authentication**:
   - Network devices **SHOULD** authenticate against centralized AAA servers (RADIUS, TACACS+)
   - Local accounts **MUST** be restricted to emergency access only ("break-glass" accounts)
   - Local account usage **MUST** be logged and reviewed

5. **Privilege Levels**:
   - Least privilege principle: Users granted minimum necessary access
   - Role-based access control (RBAC) where supported
   - Separate accounts for read-only vs. configuration access
   - Audit trail of all privileged actions

**Audit Evidence**: Device authentication configurations, MFA implementation status, AAA server logs

### 4.3 Requirement: Secure Management Protocols

**REQ-A820-007**: Network devices **MUST** use secure protocols for management access.

**Mandatory Protocol Requirements**:

| Management Function | Required Protocol | Prohibited Protocol |
|---------------------|-------------------|---------------------|
| Command-line access | SSH (v2 minimum) | Telnet |
| Web management | HTTPS | HTTP |
| File transfer | SFTP, SCP | TFTP, FTP |
| SNMP | SNMPv3 | SNMPv1, SNMPv2c |
| Remote desktop | RDP over VPN (encrypted) | RDP over internet (unencrypted) |
| API access | HTTPS with API keys/tokens | HTTP |

**Protocol-Specific Requirements**:

1. **SSH**:
   - SSH version 2 minimum (SSH v1 disabled)
   - Strong ciphers only (AES-256, ChaCha20)
   - Key-based authentication preferred over passwords
   - Host key verification enabled

2. **HTTPS**:
   - TLS 1.2 minimum (TLS 1.3 preferred)
   - Strong cipher suites only
   - Valid certificates from trusted CA (no self-signed certificates in production)
   - Certificate expiration monitoring

3. **SNMPv3**:
   - Authentication and encryption enabled (authPriv mode)
   - Strong authentication (SHA-256) and encryption (AES-256)
   - SNMPv1 and SNMPv2c **MUST** be disabled

**Exceptions**:
- Legacy devices that cannot support secure protocols **MUST** be:
  - Risk-assessed and documented
  - Isolated on management VLAN accessible only from bastion hosts
  - Scheduled for replacement or decommissioning
  - Subject to compensating controls (network-level encryption, strict access controls)

**Audit Evidence**: Protocol configuration on devices, protocol usage logs, exception documentation

### 4.4 Requirement: Unnecessary Services Disabled

**REQ-A820-008**: Network devices **MUST** have unnecessary services and features disabled.

**Services to Disable (Minimum)**:

**Common Services (Disable Unless Required)**:
- HTTP server (use HTTPS only)
- Telnet server (use SSH only)
- FTP server (use SFTP/SCP only)
- TFTP server (unless required for specific functions like PXE boot)
- SNMPv1/v2c (use SNMPv3 only)
- Finger protocol
- Small services (echo, discard, chargen, daytime)
- CDP/LLDP on untrusted ports (information disclosure risk)
- IP source routing
- IP directed broadcast
- Proxy ARP (on most interfaces)
- ICMP redirects (on most interfaces)

**Router-Specific**:
- Disable unused interfaces (shutdown)
- Disable IP source routing
- Disable IP redirects
- Disable proxy ARP (unless required)

**Switch-Specific**:
- Disable unused ports (shutdown)
- Disable DTP (Dynamic Trunking Protocol)
- Disable VTP (VLAN Trunking Protocol) or use VTP transparent mode
- Disable CDP on untrusted ports

**Firewall-Specific**:
- Disable unused rule processing features
- Disable management access from untrusted zones
- Disable packet capture on production interfaces (unless troubleshooting)

**Service Justification**:
- Any enabled service **MUST** have documented business justification
- Regular review of enabled services (quarterly)
- Remove services when no longer needed

**Audit Evidence**: Device configuration audits, service inventory, justification documentation

### 4.5 Requirement: Network Device Logging

**REQ-A820-009**: Network devices **MUST** generate and forward security logs to centralized logging infrastructure.

**Mandatory Logging Requirements**:

**Events to Log (Minimum)**:
- Administrative access (successful and failed login attempts)
- Configuration changes (who, what, when)
- Privilege escalation (enable, su, sudo)
- Interface up/down events
- Routing protocol changes
- Access control violations (denied connections, ACL hits)
- Security policy violations (IPS/IDS alerts, firewall denies)
- System events (reboots, crashes, hardware failures)
- Time synchronization events (NTP changes)

**Logging Configuration**:
- Log level: Informational minimum (level 6), Warning recommended (level 4)
- Log destination: Centralized syslog server (see A.8.15 Logging policy)
- Log transport: Encrypted (syslog over TLS preferred)
- Local logging: Enabled as backup (log to device flash/disk)
- Log rotation: Automated to prevent disk full conditions

**Log Integrity**:
- Device clocks synchronized via NTP (see A.8.21)
- Accurate timestamps in all log entries
- Log forwarding reliability monitoring (alert if log flow stops)

**Integration with SIEM**:
- Network device logs ingested into SIEM (Splunk, ELK, commercial SIEM)
- Correlation rules for network security events
- Alerting on critical events (administrative access from unauthorized IPs, etc.)

**Audit Evidence**: Device logging configurations, syslog server records, SIEM ingestion status

### 4.6 Requirement: Session Timeouts and Banners

**REQ-A820-010**: Network devices **MUST** implement session timeouts and login banners.

**Session Timeout Requirements**:
- **Console sessions**: 10 minutes of inactivity maximum
- **SSH/Telnet sessions**: 15 minutes of inactivity maximum
- **Web management sessions**: 15 minutes of inactivity maximum
- **Absolute session timeout**: 8 hours maximum (forced logout)

**Login Banner Requirements**:
- **Pre-authentication banner**: Display before login prompt
- **Banner content**:
  - Warning that system is for authorized use only
  - Notification that activity is monitored and logged
  - Legal disclaimer per [Organization]'s legal counsel
  - No information disclosure (no hostname, OS version, etc.)

**Example Banner** (approved by legal):
```
AUTHORIZED ACCESS ONLY
Unauthorized access is prohibited and will be prosecuted.
All activity is monitored and logged.
By accessing this system, you consent to monitoring.
```

**Audit Evidence**: Session timeout configurations, login banners

### 4.6 Requirement: NTP Time Synchronization

**REQ-A820-011**: Network devices **MUST** synchronize time with authoritative NTP servers.

**Why Time Synchronization Matters**:
- Accurate log timestamps for forensic analysis
- Correlation of events across multiple devices
- Certificate validation (time-sensitive)
- Compliance with audit requirements

**NTP Configuration Requirements**:
- Synchronize with [Organization]'s internal NTP servers (see A.8.21)
- NTP authentication enabled (if supported by device)
- Multiple NTP servers configured for redundancy (minimum 3)
- Monitor time drift (alert if >1 second deviation)

**Audit Evidence**: NTP configurations on devices, time synchronization status

---

## 5. Network Perimeter Controls

### 5.1 Requirement: Defined Network Perimeter

**REQ-A820-012**: [Organization] **MUST** define and document the network perimeter (boundary between internal and external networks).

**Perimeter Definition**:
- **Internet-facing perimeter**: Where [Organization]'s network connects to the public internet
- **Partner/extranet perimeter**: Where [Organization]'s network connects to trusted third parties
- **Cloud perimeter**: Where [Organization]'s network connects to cloud providers (AWS, Azure, GCP)

**Perimeter Documentation**:
- Network diagrams showing perimeter locations
- List of perimeter devices (edge firewalls, routers)
- Internet circuits and IP address ranges
- DMZ architecture

**Audit Evidence**: Perimeter definition documentation, network diagrams

### 5.2 Requirement: Perimeter Firewall Protection

**REQ-A820-013**: All network perimeters **MUST** be protected by stateful firewalls.

**Firewall Requirements**:

1. **Stateful Inspection**:
   - Firewalls **MUST** perform stateful packet inspection
   - Stateless packet filtering is insufficient

2. **Default Deny Policy**:
   - Default action **MUST** be "deny" (block)
   - Explicit allow rules for permitted traffic only
   - No "permit any" rules

3. **Rule Documentation**:
   - Every firewall rule **MUST** have documented business justification
   - Rule owner identified
   - Rule review date documented
   - Disable or remove obsolete rules

4. **Rule Review**:
   - Firewall rules reviewed quarterly minimum
   - Remove unused rules (rules with zero hits in 90 days)
   - Simplify overly complex rulesets
   - Document rule review results

5. **Egress Filtering**:
   - Egress traffic **SHOULD** be filtered (not just ingress)
   - Prevent data exfiltration via unauthorized protocols
   - Allow only necessary outbound connections

6. **Firewall Redundancy**:
   - Critical firewalls **SHOULD** be deployed in high-availability pairs
   - Failover tested quarterly
   - Configuration synchronized between primary and standby

**Audit Evidence**: Firewall configurations, rule documentation, rule review reports

### 5.3 Requirement: Intrusion Prevention Systems (IPS)

**REQ-A820-014**: Internet-facing and high-risk perimeters **SHOULD** be protected by Intrusion Prevention Systems (IPS).

**IPS Requirements** (where deployed):
- IPS signatures updated daily minimum (automatic updates preferred)
- IPS in blocking mode (not just detection mode) for known threats
- IPS performance monitoring (ensure not causing network bottlenecks)
- IPS alert review and tuning (reduce false positives)

**IPS Placement**:
- Behind edge firewall (firewall first, then IPS)
- Before critical services (DMZ web servers, mail servers)
- Between security zones (see A.8.22)

**Alternative**: Next-generation firewalls (NGFW) with integrated IPS capabilities meet this requirement.

**Audit Evidence**: IPS deployment architecture, signature update logs, IPS alerts and response

### 5.4 Requirement: DDoS Protection

**REQ-A820-015**: Internet-facing infrastructure **SHOULD** have Distributed Denial-of-Service (DDoS) protection.

**DDoS Protection Methods**:
- **Cloud-based DDoS protection**: Services like Cloudflare, Akamai, AWS Shield
- **ISP-based DDoS mitigation**: Protection at ISP level before traffic reaches [Organization]
- **On-premises DDoS mitigation**: Hardware/software appliances (Arbor Networks, Radware, etc.)

**DDoS Protection Requirements** (where deployed):
- Volumetric attack mitigation (flooding attacks)
- Application-layer attack mitigation (HTTP floods, slowloris)
- Rate limiting and traffic shaping
- Automatic attack detection and mitigation
- DDoS mitigation testing (tabletop or live testing annually)

**Risk-Based Approach**:
- Critical internet-facing services (e.g., e-commerce, customer portals): DDoS protection mandatory
- Low-criticality services: DDoS protection risk-based decision

**Audit Evidence**: DDoS protection architecture, service agreements, testing results

---

## 6. Network Access Controls

### 6.1 Requirement: Network Access Control (NAC) or 802.1X

**REQ-A820-016**: [Organization] **SHOULD** implement Network Access Control (NAC) or 802.1X port authentication for wired networks.

**Purpose**: Prevent unauthorized devices from accessing the network.

**802.1X Authentication**:
- **EAP-TLS** (certificate-based authentication) preferred
- **PEAP-MSCHAPv2** (username/password with TLS) acceptable
- Integration with RADIUS server (see A.8.21)
- Integration with Active Directory or LDAP for user authentication

**NAC Capabilities** (if implemented):
- Device posture assessment (antivirus status, OS patches, etc.)
- Role-based network access (assign VLAN based on user/device role)
- Quarantine VLAN for non-compliant devices
- Guest access registration and provisioning

**Implementation Priorities**:
- **Critical/High**: Corporate office networks, data center access ports
- **Medium**: Branch offices, remote sites
- **Low**: Guest networks (different controls), IoT devices (device-specific controls)

**Alternatives for Devices Not Supporting 802.1X**:
- MAC address authentication (RADIUS-based)
- Static VLAN assignment
- Network segmentation (IoT devices on separate VLAN)

**Audit Evidence**: NAC/802.1X deployment status, authentication logs, compliance reports

### 6.2 Requirement: Port Security on Switches

**REQ-A820-017**: Switch ports **MUST** implement port security controls.

**Port Security Controls**:

1. **MAC Address Limits**:
   - Limit number of MAC addresses per port (typically 1-3)
   - Prevent MAC flooding attacks
   - Configure port to shutdown or restrict on violation

2. **DHCP Snooping**:
   - Enable DHCP snooping on access switches
   - Designate trusted ports (uplinks, ports to DHCP servers)
   - Drop DHCP server messages on untrusted ports (prevent rogue DHCP)

3. **ARP Inspection**:
   - Enable Dynamic ARP Inspection (DAI)
   - Validate ARP packets against DHCP snooping binding table
   - Drop invalid ARP packets (prevent ARP spoofing)

4. **IP Source Guard**:
   - Enable IP Source Guard on access ports
   - Validate source IP addresses against DHCP snooping binding table
   - Drop packets with spoofed source IPs

5. **Disable Unused Ports**:
   - Shutdown all unused switch ports
   - Assign unused ports to "black hole" VLAN (no connectivity)
   - Regularly review and reclaim unused ports

**Audit Evidence**: Switch port security configurations, violation logs

### 6.3 Requirement: Rogue Device Detection

**REQ-A820-018**: [Organization] **SHOULD** implement rogue device detection mechanisms.

**Rogue Device Definition**: Unauthorized device connected to [Organization]'s network without approval.

**Detection Methods**:
- **Network Access Control (NAC)**: Detect devices failing authentication
- **Network scanning**: Periodic scans to identify unknown devices
- **NetFlow/sFlow analysis**: Detect unusual traffic patterns
- **802.1X violations**: Devices attempting to bypass authentication
- **DHCP snooping violations**: Devices not in authorized DHCP table

**Response to Rogue Devices**:
1. Alert security team immediately
2. Isolate device (quarantine VLAN or port shutdown)
3. Investigate device purpose and owner
4. Remediate (remove if malicious, register if legitimate)

**Audit Evidence**: Rogue device detection logs, response actions

---

## 7. Wireless Network Security

### 7.1 Requirement: Wireless Encryption

**REQ-A820-019**: Wireless networks **MUST** use strong encryption.

**Encryption Requirements**:
- **WPA3** (Wi-Fi Protected Access 3): Preferred for new deployments
- **WPA2 with AES**: Acceptable for existing deployments (upgrade to WPA3 when feasible)
- **WEP** and **WPA with TKIP**: Prohibited (known vulnerabilities)

**Encryption Configuration**:
- Personal mode (PSK): Acceptable for guest networks with strong passphrase (20+ characters)
- Enterprise mode (802.1X): Mandatory for corporate wireless networks
- Open networks (no encryption): Prohibited except for guest networks with captive portal

**Audit Evidence**: Wireless network configurations, encryption settings

### 7.2 Requirement: Wireless Authentication

**REQ-A820-020**: Corporate wireless networks **MUST** use 802.1X authentication.

**802.1X Configuration**:
- EAP-TLS (certificate-based) preferred
- PEAP-MSCHAPv2 (username/password) acceptable
- Integration with RADIUS server (see A.8.21)
- User-based or device-based authentication
- Unique credentials per user/device (no shared credentials)

**Guest Wireless Networks**:
- Separate SSID from corporate network
- Captive portal authentication
- Acceptable use policy acceptance required
- Time-limited access (e.g., 24 hours, then re-authenticate)

**Audit Evidence**: Wireless authentication configurations, RADIUS logs

### 7.3 Requirement: Rogue Access Point Detection

**REQ-A820-021**: [Organization] **MUST** implement rogue wireless access point (AP) detection.

**Detection Methods**:
- **Wireless IDS/IPS**: Dedicated sensors to detect unauthorized APs
- **Wireless controller-based detection**: Enterprise wireless controllers with rogue AP detection
- **Network-based detection**: Detect rogue APs via wired network (MAC address analysis)

**Rogue AP Response**:
1. Alert security team immediately (critical alert)
2. Locate rogue AP (physical location)
3. Disable rogue AP (if possible via wireless controller containment)
4. Physically remove rogue AP
5. Investigate source (malicious vs. innocent user error)

**Audit Evidence**: Rogue AP detection logs, response actions, containment capabilities

### 7.4 Requirement: Wireless Network Segmentation

**REQ-A820-022**: Wireless networks **MUST** be segmented from wired networks.

**Segmentation Requirements**:
- Wireless traffic **MUST** traverse firewall before reaching wired network
- Corporate wireless on separate VLAN from wired network
- Guest wireless on isolated VLAN (see A.8.22)
- Wireless-to-wireless traffic blocked (client isolation) on guest networks

**Audit Evidence**: VLAN assignments, firewall rules between wireless and wired networks

---

## 8. Remote Access Security

### 8.1 Requirement: VPN for Remote Access

**REQ-A820-023**: Remote access to [Organization]'s internal network **MUST** use VPN with strong authentication.

**VPN Technologies**:
- **SSL VPN**: Acceptable (clientless or client-based)
- **IPsec VPN**: Acceptable
- **Hybrid**: Both SSL and IPsec VPN acceptable

**VPN Authentication Requirements**:
- **Multi-Factor Authentication (MFA)**: Mandatory for all VPN access
- Acceptable MFA methods: Time-based OTP (TOTP), push notifications, hardware tokens
- Username/password alone is insufficient

**VPN Encryption Requirements**:
- **SSL VPN**: TLS 1.2 minimum (TLS 1.3 preferred)
- **IPsec VPN**: AES-256 encryption, SHA-256 authentication minimum
- Weak ciphers disabled (DES, 3DES, MD5, etc.)

**VPN Configuration**:
- Certificate-based authentication for VPN endpoints (mutual authentication)
- Split-tunnel vs. full-tunnel policy defined (risk-based decision)
- VPN access logging (who connected, when, from where)
- VPN idle timeout (disconnect after 15 minutes inactivity)

**Audit Evidence**: VPN configurations, MFA enforcement, VPN access logs

### 8.2 Requirement: Split-Tunnel vs. Full-Tunnel

**REQ-A820-024**: [Organization] **MUST** define split-tunnel vs. full-tunnel VPN policy.

**Full-Tunnel (Forced-Tunnel)**:
- All traffic from remote device routed through VPN
- Advantages: Full visibility and control, all traffic subject to [Organization] security controls
- Disadvantages: Increased VPN bandwidth, latency for internet traffic

**Split-Tunnel**:
- Only traffic destined for [Organization] routed through VPN
- Internet traffic goes directly from remote device
- Advantages: Reduced VPN bandwidth, better internet performance
- Disadvantages: Internet traffic not subject to [Organization] security controls

**Policy Decision**:
- **Full-tunnel** preferred for high-security environments (financial, healthcare, etc.)
- **Split-tunnel** acceptable for lower-risk environments with endpoint security controls (EDR, web filtering on endpoints)
- Document policy decision and risk acceptance

**Audit Evidence**: VPN configuration (split-tunnel or full-tunnel), policy documentation

### 8.3 Requirement: VPN Access Logging and Monitoring

**REQ-A820-025**: VPN access **MUST** be logged and monitored.

**Events to Log**:
- VPN connection attempts (successful and failed)
- User identity, source IP address, timestamp
- MFA success/failure
- VPN session duration and data transferred
- VPN disconnection (user-initiated, timeout, error)

**Monitoring and Alerting**:
- Alert on VPN connections from unexpected geographic locations
- Alert on repeated failed VPN authentication attempts
- Alert on excessive data transfer (potential data exfiltration)
- Review VPN access logs weekly minimum

**Audit Evidence**: VPN logs, monitoring alerts, log review records

---

## 9. Configuration Management

### 9.1 Requirement: Configuration Baselines

**REQ-A820-026**: [Organization] **MUST** maintain configuration baselines ("golden configs") for network devices.

**Baseline Purpose**: Define known-good, secure configuration for each device type and role.

**Baseline Components**:
- Device hardening settings (authentication, services, protocols)
- Network-specific settings (interfaces, VLANs, routing)
- Security-specific settings (ACLs, logging, SNMP)
- Management settings (NTP, syslog, DNS)

**Baseline Development**:
- Based on hardening guides (CIS, vendor guides)
- Customized for [Organization]'s environment
- Approved by CISO
- Version-controlled

**Baseline Application**:
- New devices configured from baseline before deployment
- Configuration drift detected and remediated (see below)

**Audit Evidence**: Configuration baseline documents, baseline approval records

### 9.2 Requirement: Automated Configuration Backups

**REQ-A820-027**: Network device configurations **MUST** be backed up automatically.

**Backup Requirements**:
- **Frequency**: Daily minimum (nightly automated backup preferred)
- **Retention**: Minimum 30 days, 12 months recommended
- **Encryption**: Backups encrypted at rest and in transit
- **Storage**: Backups stored off-device (centralized backup server, cloud storage)
- **Versioning**: Multiple versions retained (able to roll back to previous configs)

**Backup Tools**:
- Configuration management platforms (Ansible, Puppet, Chef)
- Network management tools (SolarWinds, PRTG, commercial NMS)
- Open-source tools (RANCID, Oxidized)
- Vendor-specific tools (Cisco Prime, Juniper Junos Space)

**Backup Validation**:
- Test backup restoration quarterly (pick sample devices)
- Verify backup integrity (not corrupted)

**Audit Evidence**: Backup configurations, backup schedules, backup restoration test results

### 9.3 Requirement: Configuration Change Management

**REQ-A820-028**: Configuration changes to network devices **MUST** follow change management process.

**Change Management Requirements**:
1. **Change Request**:
   - Document change purpose and justification
   - Identify affected devices and services
   - Assess risk and impact
   - Define rollback plan

2. **Change Approval**:
   - Low-risk changes: Network administrator approval
   - Medium-risk changes: Network manager approval
   - High-risk changes: CISO and CIO approval
   - Emergency changes: Post-implementation approval (within 24 hours)

3. **Change Implementation**:
   - Pre-change backup (before making change)
   - Implement change during maintenance window (if possible)
   - Test change (verify functionality)
   - Update documentation (network diagrams, inventory)

4. **Change Verification**:
   - Post-change testing and validation
   - Monitor for issues (24-48 hours post-change)
   - Rollback if issues detected
   - Close change request (document outcome)

**Change Documentation**:
- All changes logged in change management system
- Change records retained for audit (minimum 3 years)

**Audit Evidence**: Change management records, change approvals, post-change validation

### 9.4 Requirement: Configuration Drift Detection

**REQ-A820-029**: [Organization] **SHOULD** implement automated configuration drift detection.

**Configuration Drift**: Unauthorized or unapproved changes to device configurations.

**Detection Methods**:
- Compare running config to baseline config (daily)
- Compare running config to startup config (detect unsaved changes)
- Alert on configuration changes not matching change records
- Automated tools: Configuration management platforms, network monitoring tools

**Response to Drift**:
1. Alert network and security teams
2. Investigate change (authorized or unauthorized?)
3. If unauthorized: Revert to last known good config, investigate root cause
4. If authorized but not documented: Update documentation, create retroactive change record
5. Remediate process gaps (prevent future drift)

**Audit Evidence**: Configuration drift reports, drift remediation actions

---

## 10. Compliance Verification

### 10.1 Requirement: Periodic Security Assessments

**REQ-A820-030**: Network security controls (A.8.20) **MUST** be assessed for compliance.

**Assessment Methods**:
- **Automated**: Configuration auditing tools, vulnerability scanners
- **Manual**: Configuration review, device inspections
- **Penetration Testing**: External and internal network penetration tests

**Assessment Frequency**:
- **Quarterly**: Automated assessments (configuration audits, vulnerability scans)
- **Annual**: Manual assessments, penetration testing
- **Ad-hoc**: Post-change validation, incident-driven assessments

**Assessment Outputs**:
- Network infrastructure inventory (Workbook 1)
- Device security assessment (Workbook 2)
- Compliance scoring (percentage of requirements met)
- Gap identification and prioritization
- Remediation tracking

**Audit Evidence**: Assessment reports (Workbooks 1-2), compliance scores, remediation plans

### 10.2 Requirement: Vulnerability Management Integration

**REQ-A820-031**: Network devices **MUST** be scanned for vulnerabilities per A.8.8 (Vulnerability Management).

**Scanning Requirements**:
- Monthly vulnerability scans minimum
- Authenticated scans (using device credentials) preferred
- Scan all network devices (routers, switches, firewalls, wireless APs, load balancers)
- Prioritize remediation by CVSS score (Critical and High first)

**Firmware/Software Patching**:
- Critical vulnerabilities patched within 30 days
- High vulnerabilities patched within 90 days
- Medium and Low vulnerabilities patched within 180 days or risk-accepted
- Patches tested in lab before production deployment

**Audit Evidence**: Vulnerability scan reports, patching records, risk acceptance documentation

### 10.3 Requirement: Non-Compliance Handling

**REQ-A820-032**: Network security non-compliance **MUST** be addressed through remediation or risk acceptance.

**Non-Compliance Response**:
1. **Identify Gap**: Assessment reveals non-compliance with requirement
2. **Risk Assessment**: Evaluate likelihood and impact of gap
3. **Remediation Plan**: Develop plan to close gap with timeline
4. **Implementation**: Execute remediation plan
5. **Validation**: Verify gap is closed (re-assessment)

**Risk Acceptance** (if remediation not feasible):
- Document gap and reason remediation is not feasible
- Assess residual risk
- Define compensating controls (if any)
- Obtain CISO approval for risk acceptance
- Time-limit risk acceptance (review annually)
- Track risk acceptance in risk register

**Escalation**:
- Critical gaps: Immediate escalation to CISO
- High gaps: Escalation to CISO if not remediated within 30 days
- Medium gaps: Escalation if not remediated within 90 days

**Audit Evidence**: Remediation plans, risk acceptance documentation, escalation records

---

## 11. Summary of Requirements

**Total Requirements**: 32 (REQ-A820-001 through REQ-A820-032)

**Requirement Breakdown by Category**:
- Network Topology Documentation: 2 requirements
- Network Device Inventory: 2 requirements
- Network Device Hardening: 6 requirements
- Network Perimeter Controls: 4 requirements
- Network Access Controls: 3 requirements
- Wireless Network Security: 4 requirements
- Remote Access Security: 3 requirements
- Configuration Management: 4 requirements
- Compliance Verification: 3 requirements

**Criticality Classification**:
- **MUST** requirements: 26 (mandatory, no exceptions without risk acceptance)
- **SHOULD** requirements: 6 (strongly recommended, risk-based decision)

---

**END OF SECTION 2 (A.8.20)**

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Network Security Manager | Initial network security requirements (A.8.20) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

**Next Document**: ISMS-POL-A.8.20-21-22-S3 (Network Services Security Requirements - A.8.21)
