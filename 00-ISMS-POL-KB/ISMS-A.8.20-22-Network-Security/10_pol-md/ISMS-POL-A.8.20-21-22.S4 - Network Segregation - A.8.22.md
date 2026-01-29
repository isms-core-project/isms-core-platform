# ISMS-POL-A.8.20-21-22-S4
## Network Segregation Requirements (A.8.22)

**Document ID**: ISMS-POL-A.8.20-21-22-S4  
**Title**: Network Segregation Requirements (ISO/IEC 27001:2022 Control A.8.22)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Network Security Manager | Initial network segregation requirements (A.8.22) |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Network Operations Manager
- Architecture Review: Network Architect

**Distribution**: Network team, security team, IT operations, auditors  
**Related Documents**: ISMS-POL-A.8.20-21-22 (Master), ISMS-POL-A.8.20-21-22-S2 (A.8.20), ISMS-POL-A.8.20-21-22-S3 (A.8.21)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.22

**Official Control Text**:

> *Groups of information services, users and information systems should be segregated in the organization's networks.*

**Control Purpose**: Implement network segmentation to limit blast radius, enforce least privilege network access, and comply with regulatory requirements for data isolation.

**Why This Matters**:

Flat networks (no segmentation) enable attackers to:
- **Lateral movement**: Freely move between systems after initial compromise
- **Data exfiltration**: Access sensitive data from compromised low-security systems
- **Privilege escalation**: Exploit trust relationships between network segments
- **Ransomware propagation**: Encrypt entire network from single entry point
- **Regulatory non-compliance**: Fail to isolate regulated data (PII, payment card data, healthcare data)

Network segmentation reduces these risks by creating security boundaries, limiting communication between zones, and enforcing defense in depth.

**The "Flat Network" Problem**:

Without segmentation, a network is like a building with no internal walls or doors - once an attacker is inside, they have free access to everything. Segmentation creates "rooms" with locked doors, limiting an attacker's ability to move freely.

### 1.2 Scope of A.8.22 Requirements

This section defines mandatory requirements for:

1. **Network Segmentation Architecture** - Defining security zones
2. **Security Zones Design** - Zone purpose, trust levels, boundaries
3. **VLAN Segregation** - Virtual LAN implementation
4. **Subnet Design** - IP address segmentation
5. **Inter-Zone Traffic Controls** - Firewall rules, ACLs
6. **Trust Boundaries** - Defining and enforcing trust relationships
7. **Segmentation Effectiveness Testing** - Validating segmentation
8. **Flat Network Remediation** - Identifying and fixing flat networks
9. **Microsegmentation** - Advanced segmentation techniques
10. **Cloud Network Segmentation** - Cloud-specific segmentation

### 1.3 Integration with A.8.20 and A.8.21

While A.8.22 focuses on network segmentation:
- **A.8.20** provides the infrastructure for segmentation (routers, switches, firewalls)
- **A.8.21** provides services that may be zone-specific (DNS, DHCP per zone)

All three controls work together to create a secure, well-architected network.

---

## 2. Network Segmentation Principles

### 2.1 Requirement: Defense in Depth Through Segmentation

**REQ-A822-001**: [Organization] **MUST** implement network segmentation as part of defense-in-depth strategy.

**Segmentation Purpose**:
- **Containment**: Limit blast radius of security incidents
- **Least Privilege**: Enforce minimum necessary network access
- **Compliance**: Isolate regulated data (PII, PCI, PHI)
- **Performance**: Reduce broadcast traffic, improve network efficiency
- **Operational**: Separate production from development/test

**Segmentation Principle**: "Need to know" and "need to access" - users and systems only have network access to resources they require for their function.

### 2.2 Requirement: Default Deny Policy

**REQ-A822-002**: Inter-zone traffic **MUST** follow default deny policy (explicit allow only).

**Default Deny Principle**:
- All traffic between zones blocked by default
- Only specifically approved traffic flows permitted
- Every permit rule requires business justification
- Regular review and removal of unused rules

---

## 3. Security Zones Architecture

### 3.1 Requirement: Defined Security Zones

**REQ-A822-003**: [Organization] **MUST** define and document security zones.

**Security Zone Definition**: Logical or physical network segment with common security requirements, trust level, and data classification.

**Minimum Security Zones** (typical organization):

| Zone Name | Purpose | Trust Level | Example Systems |
|-----------|---------|-------------|-----------------|
| **DMZ** | Internet-facing services | Untrusted | Web servers, mail relays, VPN concentrators |
| **Internal** | Corporate users and resources | Semi-Trusted | Workstations, file servers, print servers |
| **Management** | Network device management | Trusted | Jump servers, network management systems |
| **Guest** | Visitor internet access | Untrusted | Guest wireless, conference room networks |
| **Server** | Internal application servers | Semi-Trusted | Database servers, application servers |
| **Voice/Data** | VoIP/UC infrastructure | Trusted | IP phones, voice gateways, call managers |
| **OT/ICS** | Operational technology | Highly Trusted | SCADA, industrial controllers (if applicable) |
| **Development** | Non-production systems | Low Trust | Development servers, test environments |
| **Cloud** | Cloud-hosted resources | Varies | AWS VPC, Azure VNet, GCP VPC |

**Zone Documentation Requirements**:
- Zone name and identifier
- Zone purpose and description
- Trust level classification
- Data classification (what data resides in zone)
- Networks/subnets in zone
- VLANs assigned to zone
- Allowed traffic flows (to/from other zones)
- Zone owner/responsible party

**Audit Evidence**: Security zones inventory (Workbook 4), network architecture diagrams

### 3.2 Requirement: Zone Trust Levels

**REQ-A822-004**: Every security zone **MUST** have a defined trust level.

**Trust Level Definitions**:

**Untrusted (Internet-facing)**:
- Assumes compromise is likely
- No trust in traffic from this zone
- Strict inbound and outbound filtering
- Enhanced monitoring and logging
- Examples: DMZ, Guest network

**Semi-Trusted (Internal networks)**:
- Some trust in users/systems
- Moderate filtering between zones
- Standard monitoring and logging
- Examples: Internal corporate network, Server network

**Trusted (Highly controlled)**:
- High trust in users/systems
- Critical infrastructure components
- Strict access controls (authentication required)
- Comprehensive monitoring and alerting
- Examples: Management network, OT/ICS network

**Trust Relationships**: Traffic from lower-trust zones to higher-trust zones **MUST** be strictly controlled or denied.

### 3.3 Requirement: Trust Boundaries

**REQ-A822-005**: [Organization] **MUST** define and enforce trust boundaries between zones.

**Trust Boundary Definition**: Network perimeter where trust level changes, requiring security controls (firewall, ACLs).

**Trust Boundary Enforcement**:
- Firewall or ACL at every trust boundary
- Stateful inspection for all inter-zone traffic
- Explicit allow rules only (default deny)
- Logging of all denied traffic
- Regular review of trust boundary configurations

**Trust Boundary Examples**:
- DMZ → Internal: Firewall required (untrusted to semi-trusted)
- Internal → Management: Firewall required (semi-trusted to trusted)
- Guest → Internal: Firewall required (untrusted to semi-trusted, strict deny)

**Audit Evidence**: Trust boundary documentation, firewall placement diagrams

---

## 4. VLAN Segregation

### 4.1 Requirement: VLAN Implementation

**REQ-A822-006**: [Organization] **MUST** use VLANs for logical network segmentation.

**VLAN Purpose**: Create logical separation on physical network infrastructure without requiring separate physical networks.

**VLAN Assignment**:
- One VLAN per security zone (minimum)
- VLANs assigned based on function, not physical location
- VLAN assignments documented and reviewed quarterly

**VLAN Naming Convention**:
- VLAN ID and descriptive name
- Example: VLAN 10 - DMZ-Public-Services, VLAN 20 - Internal-Corporate, VLAN 30 - Management

### 4.2 Requirement: VLAN Tagging and Trunking Security

**REQ-A822-007**: VLAN trunks **MUST** be secured to prevent VLAN hopping attacks.

**VLAN Trunk Security Requirements**:

1. **Disable Dynamic Trunking Protocol (DTP)**:
   - All trunk ports configured manually (not auto-negotiate)
   - DTP disabled on all ports
   - Prevents VLAN hopping via switch spoofing

2. **Native VLAN Security**:
   - Change native VLAN from default (VLAN 1)
   - Use unused VLAN as native VLAN (e.g., VLAN 999)
   - Prune native VLAN from trunk (where possible)
   - Prevents VLAN hopping via double tagging

3. **Allowed VLANs on Trunks**:
   - Explicitly define allowed VLANs on each trunk
   - Remove unused VLANs from trunk allowed list
   - Reduces attack surface

**VLAN Hopping Prevention**: VLAN hopping attacks (double tagging, switch spoofing) **MUST** be mitigated through trunk security configuration.

**Audit Evidence**: Switch trunk configurations, VLAN assignments, security audit results

### 4.3 Requirement: VLAN Access Port Security

**REQ-A822-008**: VLAN access ports **MUST** be configured with proper VLAN assignment and security controls (see A.8.20 port security).

**Access Port Requirements**:
- Statically assigned to single VLAN (no dynamic VLAN assignment unless via 802.1X)
- Port security enabled (MAC address limits)
- Unused ports disabled and assigned to black hole VLAN

---

## 5. Subnet Design and IP Address Management

### 5.1 Requirement: Subnet Segregation

**REQ-A822-009**: [Organization] **MUST** use subnets to segment IP address space.

**Subnet Design Principles**:
- One subnet per security zone (minimum)
- Subnets sized appropriately for expected device count
- Private IP address ranges (RFC 1918) for internal networks
- Hierarchical IP addressing scheme for scalability

**RFC 1918 Private IP Ranges**:
- 10.0.0.0/8 (10.0.0.0 - 10.255.255.255) - Large networks
- 172.16.0.0/12 (172.16.0.0 - 172.31.255.255) - Medium networks
- 192.168.0.0/16 (192.168.0.0 - 192.168.255.255) - Small networks

### 5.2 Requirement: IP Address Management (IPAM)

**REQ-A822-010**: [Organization] **MUST** maintain IP address management (IPAM) documentation.

**IPAM Documentation**:
- Subnet allocation (which subnets are used, which are free)
- VLAN-to-subnet mapping
- IP address assignments (static allocations)
- DHCP scope definitions
- IPv4 and IPv6 addressing (where applicable)

**IPAM Tools**: Commercial IPAM systems, spreadsheets, DNS/DHCP integration, cloud-native IPAM

**Audit Evidence**: IPAM documentation, subnet allocation records

---

## 6. Inter-Zone Traffic Controls

### 6.1 Requirement: Firewall Between Zones

**REQ-A822-011**: Traffic between security zones **MUST** traverse firewalls or ACLs.

**Firewall Placement**:
- Internet → DMZ: Perimeter firewall
- DMZ → Internal: Internal firewall
- Internal → Management: Internal firewall
- Guest → Internal: Firewall (deny all)
- Server → Internal: Firewall (controlled access)

**Firewall Types**:
- **Hardware firewalls**: Dedicated firewall appliances (Palo Alto, Fortinet, Cisco ASA, etc.)
- **Virtual firewalls**: VM-based firewalls (cloud or on-prem)
- **Next-generation firewalls (NGFW)**: Advanced features (IPS, application awareness, SSL inspection)
- **Cloud-native firewalls**: AWS security groups, Azure NSGs, GCP firewall rules

### 6.2 Requirement: Firewall Rule Documentation

**REQ-A822-012**: Every inter-zone firewall rule **MUST** be documented with business justification.

**Rule Documentation Requirements**:
- Rule ID or number
- Source zone and IP/subnet
- Destination zone and IP/subnet
- Protocol and port(s)
- Action (Allow or Deny)
- Business justification (why this traffic is needed)
- Rule owner (who approved/requested)
- Creation date and last review date

**Rule Review**: Firewall rules **MUST** be reviewed quarterly (minimum):
- Identify unused rules (zero hits in 90 days)
- Remove obsolete rules
- Consolidate overlapping rules
- Update documentation

**Audit Evidence**: Firewall rule inventory (Workbook 4), rule documentation, rule review reports

### 6.3 Requirement: Inter-Zone Traffic Matrix

**REQ-A822-013**: [Organization] **MUST** maintain an inter-zone traffic matrix showing allowed/denied traffic flows.

**Traffic Matrix Purpose**: Visual representation of which zones can communicate, enabling security architecture review and gap identification.

**Matrix Example**:
```
              | DMZ    | Internal | Management | Guest  |
------------- |--------|----------|------------|--------|
DMZ           |   -    | ALLOW*   | DENY       | DENY   |
Internal      | DENY   |    -     | ALLOW*     | DENY   |
Management    | ALLOW* | ALLOW*   |     -      | DENY   |
Guest         | DENY   | DENY     | DENY       |   -    |

* = Allowed with specific firewall rules and logging
```

**Matrix Documentation**: For each "ALLOW" cell:
- Protocols/ports allowed (HTTP/443, SSH/22, etc.)
- Business justification
- Firewall rule ID reference

**Audit Evidence**: Inter-zone traffic matrix (Workbook 4)

### 6.4 Requirement: Deny-by-Default Policy

**REQ-A822-014**: Firewalls between zones **MUST** implement deny-by-default (implicit deny).

**Default Deny Configuration**:
- Final rule in firewall ruleset: Deny all
- No "permit any" rules
- Explicit allow rules for necessary traffic only
- Log all denied traffic (for anomaly detection)

### 6.5 Requirement: Egress Filtering

**REQ-A822-015**: [Organization] **SHOULD** implement egress filtering (outbound traffic control) between zones.

**Egress Filtering Purpose**: Prevent data exfiltration, command-and-control traffic, lateral movement.

**Egress Filtering Examples**:
- Internal → Internet: Allow only HTTP/HTTPS, DNS, specific protocols
- Server → Internet: Deny all (no direct internet access) or highly restricted
- Management → Internet: Deny all (management isolated)

---

## 7. Segmentation Effectiveness Testing

### 7.1 Requirement: Segmentation Testing

**REQ-A822-016**: Network segmentation **MUST** be tested for effectiveness.

**Testing Methods**:

1. **Traffic Flow Verification**:
   - Use packet capture (tcpdump, Wireshark) to verify only authorized traffic flows between zones
   - Attempt unauthorized connections, verify denial
   - Test from multiple zones to validate rules

2. **Firewall Rule Testing**:
   - Test each firewall rule individually (source, destination, port)
   - Verify allow rules permit traffic
   - Verify deny rules block traffic
   - Tools: telnet, netcat, nmap

3. **Lateral Movement Simulation**:
   - Simulate attacker moving between zones
   - Attempt to pivot from compromised system in one zone to another
   - Verify segmentation prevents or detects lateral movement
   - Penetration testing (red team exercises)

4. **VLAN Hopping Testing**:
   - Attempt double-tagging VLAN hopping (tools: Scapy, Yersinia)
   - Attempt switch spoofing (DTP exploitation)
   - Verify VLAN hopping prevention controls work

**Testing Frequency**:
- **Initial**: After segmentation implementation
- **Periodic**: Annual minimum (as part of penetration testing)
- **Post-Change**: After any segmentation architecture changes

**Audit Evidence**: Segmentation effectiveness test results (Workbook 4), penetration test reports

### 7.2 Requirement: Penetration Testing

**REQ-A822-017**: Network segmentation **SHOULD** be included in annual penetration testing scope.

**Penetration Test Objectives**:
- Validate firewall rules between zones
- Attempt lateral movement between zones
- Test VLAN segmentation effectiveness
- Identify segmentation gaps or misconfigurations

**Audit Evidence**: Penetration test reports (segmentation findings)

---

## 8. Flat Network Identification and Remediation

### 8.1 Requirement: Flat Network Assessment

**REQ-A822-018**: [Organization] **MUST** identify flat networks (no segmentation) and assess risk.

**Flat Network Definition**: Network segment where all devices can communicate freely without firewalls or ACLs (single broadcast domain, no segmentation).

**Flat Network Risks**:
- No containment: Compromise of one device compromises all
- Unrestricted lateral movement
- Regulatory non-compliance (PCI, HIPAA, etc.)
- Performance issues (large broadcast domains)

**Flat Network Identification**:
- Review VLAN assignments (single VLAN for entire network = flat)
- Review firewall rules (lack of inter-zone firewalls = flat)
- Traffic analysis (NetFlow/sFlow shows unrestricted east-west traffic)

**Audit Evidence**: Flat network identification assessment (Workbook 4)

### 8.2 Requirement: Flat Network Remediation

**REQ-A822-019**: Identified flat networks **MUST** be remediated or risk-accepted.

**Remediation Approach**:
1. **Prioritize**: High-risk, high-impact flat networks first
2. **Design**: Define security zones and segmentation architecture
3. **Implement**: Phased rollout (pilot, then production)
   - Create VLANs for security zones
   - Deploy firewalls between zones
   - Configure firewall rules
   - Test segmentation effectiveness
4. **Validate**: Post-implementation testing
5. **Document**: Updated network diagrams, configuration documentation

**Phased Remediation** (if immediate remediation not feasible):
- Phase 1: Segment critical zones (DMZ, management, OT/ICS)
- Phase 2: Segment server zones (database, application tiers)
- Phase 3: Segment user zones (departments, functions)

**Risk Acceptance** (if remediation not feasible):
- Document flat network and risk
- Implement compensating controls (enhanced monitoring, endpoint security)
- CISO approval required
- Time-limited (annual review and re-approval)

**Audit Evidence**: Flat network remediation plans, implementation records, risk acceptance documentation

---

## 9. Microsegmentation and Advanced Segmentation

### 9.1 Requirement: Microsegmentation Consideration

**REQ-A822-020**: [Organization] **SHOULD** consider microsegmentation for high-security environments.

**Microsegmentation Definition**: Fine-grained segmentation at the application, workload, or host level (beyond traditional VLAN/subnet segmentation).

**Microsegmentation Technologies**:
- **Host-based firewalls**: Firewall on every server/workload (Windows Firewall, iptables/nftables, cloud security groups)
- **Software-defined segmentation**: Centralized policy enforcement via SDN controllers
- **Service mesh**: Application-layer segmentation for microservices (Istio, Linkerd)
- **Container network policies**: Kubernetes network policies, Docker network segmentation

**Use Cases for Microsegmentation**:
- **Zero Trust architecture**: Segment even within "trusted" zones
- **Cloud-native applications**: Container and microservice segmentation
- **High-security workloads**: Payment processing, PHI, PII handling
- **Compliance requirements**: PCI DSS Level 1, HIPAA compliance

**Microsegmentation Benefits**:
- Extreme containment (breach limited to single workload)
- Application-aware segmentation (beyond IP/port)
- Dynamic policy enforcement (adapt to workload changes)
- Support for modern cloud-native architectures

**Microsegmentation Challenges**:
- Complexity (many more policies to manage)
- Performance overhead (packet inspection at every host)
- Operational maturity (requires automation, policy orchestration)

**Implementation Approach**: Start with traditional segmentation (VLANs, zones), then add microsegmentation for critical workloads.

**Audit Evidence**: Microsegmentation architecture documentation (if implemented)

### 9.2 Requirement: Zero Trust Network Access (ZTNA)

**REQ-A822-021**: [Organization] **MAY** implement Zero Trust Network Access (ZTNA) principles for advanced segmentation.

**ZTNA Principles**:
- "Never trust, always verify" - no implicit trust based on network location
- Verify identity, device posture, and context for every access request
- Least privilege access (grant minimum necessary access dynamically)
- Micro-perimeters around every resource (not just network perimeter)

**ZTNA Technologies**:
- Software-Defined Perimeter (SDP)
- Identity-based network access (BeyondCorp, Perimeter 81, Zscaler Private Access)
- Policy enforcement points at application layer

**ZTNA Benefits**: Eliminates implicit trust in network location, supports remote workforce, reduces lateral movement risk

**Audit Evidence**: ZTNA architecture documentation (if implemented)

---

## 10. Cloud Network Segmentation

### 10.1 Requirement: Cloud Network Segmentation

**REQ-A822-022**: Cloud networks **MUST** be segmented using cloud-native tools.

**Cloud Segmentation Technologies**:

**AWS (Amazon Web Services)**:
- **VPCs (Virtual Private Clouds)**: Isolated virtual networks
- **Subnets**: Public, private, database subnets within VPC
- **Security Groups**: Stateful firewalls for EC2 instances
- **Network ACLs**: Stateless firewalls for subnets
- **VPC Peering, Transit Gateway**: Controlled inter-VPC connectivity

**Azure**:
- **VNets (Virtual Networks)**: Isolated virtual networks
- **Subnets**: Segment within VNet
- **Network Security Groups (NSGs)**: Firewalls for subnets and NICs
- **Application Security Groups (ASGs)**: Group-based security
- **VNet Peering, VPN Gateway**: Inter-VNet connectivity

**GCP (Google Cloud Platform)**:
- **VPCs**: Global virtual networks
- **Subnets**: Regional subnets within VPC
- **Firewall Rules**: Stateful firewalls
- **VPC Peering, Cloud VPN**: Inter-VPC connectivity

**Cloud Segmentation Principles**:
- Separate VPCs/VNets per environment (production, development, test)
- Separate subnets per tier (web, app, database)
- Security groups/NSGs for micro-segmentation
- Default deny policy (no 0.0.0.0/0 allow rules)
- Logging and monitoring (VPC Flow Logs, NSG logs, GCP firewall logs)

**Audit Evidence**: Cloud network architecture diagrams, security group/NSG configurations (Workbook 4)

### 10.2 Requirement: Hybrid Network Segmentation

**REQ-A822-023**: Hybrid networks (on-premises + cloud) **MUST** maintain segmentation boundaries.

**Hybrid Segmentation Challenges**:
- Segmentation must span on-premises and cloud
- Different technologies (VLANs on-prem, security groups in cloud)
- VPN or Direct Connect / ExpressRoute connectivity

**Hybrid Segmentation Approach**:
- Extend security zones to cloud (DMZ in AWS VPC, Internal zone in Azure VNet)
- Firewall at hybrid connection point (VPN gateway, Direct Connect gateway)
- Consistent segmentation policy across on-prem and cloud
- Centralized policy management (where possible)

**Audit Evidence**: Hybrid network architecture diagrams, segmentation consistency assessment

---

## 11. Compliance Verification

### 11.1 Requirement: Segmentation Compliance Assessment

**REQ-A822-024**: Network segmentation (A.8.22) **MUST** be assessed for compliance.

**Assessment Methods**:
- Security zones inventory validation (quarterly)
- Inter-zone traffic matrix review (annual)
- Firewall rule review (quarterly)
- Segmentation effectiveness testing (annual)
- Flat network identification (annual)

**Assessment Outputs**:
- Security zones inventory (Workbook 4)
- Inter-zone traffic matrix (Workbook 4)
- Firewall rules inventory (Workbook 4)
- Segmentation effectiveness test results (Workbook 4)
- Flat network remediation status (Workbook 4)
- Compliance scoring (percentage of requirements met)
- Gap identification and remediation tracking

**Audit Evidence**: Assessment reports (Workbook 4), compliance scores, remediation plans

### 11.2 Requirement: Non-Compliance Handling

**REQ-A822-025**: Network segmentation non-compliance **MUST** be addressed through remediation or risk acceptance.

**Non-Compliance Response**: Same process as A.8.20 and A.8.21 (risk assessment, remediation plan, risk acceptance if needed, CISO approval)

**Priority Remediation**:
- Flat networks in high-security zones (management, OT/ICS): Critical priority
- Missing firewalls between trust boundaries: Critical priority
- Unauthorized inter-zone traffic: High priority
- Obsolete firewall rules: Medium priority

---

## 12. Summary of Requirements

**Total Requirements**: 25 (REQ-A822-001 through REQ-A822-025)

**Requirement Breakdown by Category**:
- Segmentation Principles: 2 requirements
- Security Zones Architecture: 3 requirements
- VLAN Segregation: 3 requirements
- Subnet Design: 2 requirements
- Inter-Zone Traffic Controls: 5 requirements
- Segmentation Testing: 2 requirements
- Flat Network Remediation: 2 requirements
- Microsegmentation: 2 requirements
- Cloud Segmentation: 2 requirements
- Compliance Verification: 2 requirements

**Criticality Classification**:
- **MUST** requirements: 18 (mandatory)
- **SHOULD** requirements: 6 (strongly recommended)
- **MAY** requirements: 1 (optional, advanced)

---

**END OF SECTION 4 (A.8.22)**

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Network Security Manager | Initial network segregation requirements (A.8.22) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

**Next Document**: ISMS-POL-A.8.20-21-22-S5 (Assessment & Evidence Framework)

**Note**: We've now completed requirements for all three controls (A.8.20, A.8.21, A.8.22). Section 5 will define the unified assessment methodology and evidence framework.
