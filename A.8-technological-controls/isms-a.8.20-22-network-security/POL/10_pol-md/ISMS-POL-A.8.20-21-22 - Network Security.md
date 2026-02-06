**ISMS-POL-A.8.20-21-22 — Network Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Network Security |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.20-21-22 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Technical: Network Operations Manager
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.20-21-22.S1-UG/TG (Network Discovery)
- ISMS-IMP-A.8.20-21-22.S2-UG/TG (Architecture Documentation)
- ISMS-IMP-A.8.20-21-22.S3-UG/TG (Device Hardening)
- ISMS-IMP-A.8.20-21-22.S4-UG/TG (Services Security)
- ISMS-IMP-A.8.20-21-22.S5-UG/TG (Segmentation Implementation)
- ISMS-IMP-A.8.20-21-22.S6-UG/TG (Security Testing)
- ISO/IEC 27001:2022 Controls A.8.20, A.8.21, A.8.22
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.5.23 (Cloud Services)

---

## Executive Summary

This policy establishes [Organization]'s requirements for network security controls to protect information assets through secure network infrastructure, services, and segmentation in accordance with ISO/IEC 27001:2022 Controls A.8.20, A.8.21, and A.8.22.

**Scope**: This policy applies to all network infrastructure, network devices, network services, and network segments regardless of deployment model (on-premises, cloud, hybrid) or technology (traditional networking, software-defined networking).

**Purpose**: Define organizational requirements for network security control implementation and governance. This policy establishes WHAT network security protection is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.20-21-22 (UG/TG variants). Technical standards and configurations are intentionally defined outside this policy to preserve technological agility.

**Combined Control Approach**: These three controls are implemented as a unified framework because they operate on the same network infrastructure and share common discovery, assessment, and evidence collection processes. Despite unified implementation, each control maintains distinct requirements for Statement of Applicability (SoA) purposes.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Controls A.8.20, A.8.21, A.8.22

**ISO/IEC 27001:2022 Annex A.8.20 - Networks Security**

> *Networks and network devices should be secured, managed and controlled to protect information in systems and applications.*

**Control Objective**: Ensure network infrastructure and devices are hardened, monitored, and configured to prevent unauthorized access and protect information in transit.

**ISO/IEC 27001:2022 Annex A.8.21 - Security of Network Services**

> *Security mechanisms, service levels and service requirements of network services should be identified, implemented and monitored.*

**Control Objective**: Ensure network services are secured, available, and monitored to support business operations while protecting against service-based attacks.

**ISO/IEC 27001:2022 Annex A.8.22 - Segregation of Networks**

> *Groups of information services, users and information systems should be segregated in the organization's networks.*

**Control Objective**: Implement network segmentation to limit blast radius, enforce least privilege network access, and comply with regulatory requirements for data isolation.

**Statement of Applicability Independence**: Despite unified implementation and documentation, Controls A.8.20, A.8.21, and A.8.22 are assessed independently in the Statement of Applicability. Each control maintains distinct requirements, evidence collection, and compliance scoring for audit purposes.

**This Policy Addresses**:

- Network infrastructure security requirements (A.8.20)
- Network services security requirements (A.8.21)
- Network segmentation requirements (A.8.22)
- Organizational roles and responsibilities for network security governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

## What This Policy Does

This policy:

- **Defines** network security control requirements aligned with organizational risk assessment
- **Establishes** governance framework for network security decision-making
- **Specifies** accountability for network security control implementation
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** three related controls into unified framework for implementation efficiency

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical implementation details** (see ISMS-IMP-A.8.20-21-22 Implementation Guides)
- **Define network topology or architecture** (see ISMS-IMP-A.8.20-21-22-S2 Architecture Documentation)
- **Provide device-specific configuration procedures** (see ISMS-IMP-A.8.20-21-22-S3 Device Hardening)
- **Define firewall rules or ACLs** (see ISMS-IMP-A.8.20-21-22-S5 Segmentation Implementation)
- **Select network technologies or vendors** (technology selection based on [Organization]'s risk assessment)
- **Replace risk assessment** (network security controls selected based on [Organization]'s risk treatment)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving network technologies (SDN, cloud networking, etc.)
- Technical agility for technology updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Technology-agnostic approach applicable to any network architecture

## Scope

**This policy applies to**:

**Network Infrastructure** (A.8.20):

- On-premises networks (data centers, offices, branches)
- Cloud networks (AWS VPC, Azure VNet, GCP VPC, other cloud providers)
- Hybrid networks (on-premises + cloud integration)
- Software-defined networks (SDN, SD-WAN)
- Traditional networks (routers, switches, firewalls)
- Wireless networks (corporate WLANs, guest networks)
- Remote access networks (VPN, remote desktop)

**Network Devices** (A.8.20):

- Routers, switches, firewalls, wireless access points
- Load balancers, VPN concentrators
- Network security appliances (IPS/IDS, DLP)
- Network management systems
- Cloud virtual network devices

**Network Services** (A.8.21):

- DNS, DHCP, NTP
- Proxy services, load balancing services
- Authentication services (RADIUS, TACACS+)
- SNMP, syslog, other critical network services

**Network Segments** (A.8.22):

- Security zones (DMZ, Internal, Management, Guest, Server, etc.)
- VLANs and subnets
- Trust boundaries and inter-zone controls
- Cloud security groups and network ACLs

**Personnel**:

- Network administrators, security team, IT operations
- Cloud administrators, system owners
- All employees (network access policies)

**This policy does NOT apply to**:

- Application-layer security (covered under other controls)
- Endpoint security (covered under A.8.1 User Endpoint Devices)
- Physical security of network equipment (covered under physical security controls)

**Cloud Environment Scope**:

References to specific cloud providers (AWS, Azure, GCP) throughout this policy are illustrative of cloud networking concepts. Applicable cloud environments are documented in the network infrastructure inventory (Workbook 1).

**Cloud Environment Documentation**: The authoritative list of in-scope cloud environments is maintained in:
- **Workbook 1 - Network Infrastructure Inventory** (cloud devices and VPCs/VNets)
- **ISMS-POL-A.5.9 Asset Inventory** (cloud service instances)

Before initial policy approval, the following SHALL be documented in Workbook 1:
- **Primary cloud provider(s)**: Provider name, regions, VPCs/VNets in scope
- **Secondary cloud provider(s)**: If applicable, same detail level
- **SaaS with network integration**: Services requiring VPN or private connectivity (e.g., IPsec tunnels, VPC peering, private endpoints)

Cloud provider additions or changes are reflected in the network infrastructure inventory and do not require policy revision. New cloud environments must implement equivalent controls per this policy before production deployment.

## Regulatory Applicability

This policy implements network security requirements to comply with regulations per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1: Mandatory Compliance**

| Regulation | Requirement | Applicability |
|------------|-------------|---------------|
| **Swiss nDSG (Federal Data Protection Act)** | Technical and organizational measures to protect personal data | All [Organization] processing of personal data |
| **EU GDPR** | Technical and organizational measures (Art. 32) | When processing EU personal data |
| **ISO/IEC 27001:2022** | Controls A.8.20, A.8.21, A.8.22 | Certification scope |

**Tier 2: Conditional Applicability**

| Regulation | Requirement | Trigger Condition |
|------------|-------------|-------------------|
| **PCI DSS** | Network segmentation (Req. 1), secure network services | Processing payment card data |
| **FINMA** | Network security controls for financial institutions | Swiss financial services operations |
| **DORA** | ICT network security and resilience | EU financial services operations |
| **NIS2** | Network security for essential/important entities | Critical infrastructure designation |

**Tier 3: Informational Guidance**

Best practice frameworks referenced but not mandatory compliance requirements:

- ISO/IEC 27033 (Network Security)
- NIST CSF (Cybersecurity Framework)
- CIS Controls (network device hardening benchmarks)

**United States Federal Requirements**: References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where [Organization] has explicit US federal contractual obligations, as defined in ISMS-POL-00.

**Compliance Determination**: Legal/Compliance Officer determines applicability of Tier 2 regulations based on [Organization]'s business activities and regulatory status.

---

# Requirements Framework

## Network Infrastructure Security (A.8.20)

[Organization] **MUST** implement the following network infrastructure security controls:

| Requirement Category | Mandatory Controls | Implementation Reference |
|---------------------|-------------------|-------------------------|
| **Network Topology Documentation** | Maintain current network diagrams (physical, logical, security views); Update documentation based on organizational change management | ISMS-IMP-A.8.20-21-22-S2 |
| **Network Device Inventory** | Comprehensive inventory of all network devices with ownership, criticality, compliance status; Updated from automated discovery | ISMS-IMP-A.8.20-21-22-S1 |
| **Device Hardening** | Disable default credentials; Remove unnecessary services; Implement secure configurations per CIS benchmarks or vendor hardening guides | ISMS-IMP-A.8.20-21-22-S3 |
| **Perimeter Controls** | Firewalls at network perimeter; IPS/IDS for threat detection; DDoS protection for internet-facing services | ISMS-IMP-A.8.20-21-22-S3 |
| **Network Access Controls** | Industry-standard network access control mechanisms **(e.g., 802.1X for wired/wireless networks, NAC appliances, clientless network access control)**; Port security on switches; Authentication-based access control | ISMS-IMP-A.8.20-21-22-S3 |
| **Monitoring & Logging** | All network devices log to centralized system; Network traffic analysis; SIEM integration for correlation | ISMS-IMP-A.8.20-21-22-S6 |
| **Configuration Management** | Configuration baselines; Change control for configuration changes; Automated backups per implementation guidance | ISMS-IMP-A.8.20-21-22-S3 |
| **Wireless Security** | Strong encryption and authentication; Rogue AP detection; Guest network isolation | ISMS-IMP-A.8.20-21-22-S3 |
| **Remote Access Security** | VPN with MFA; Split-tunnel policies; Session logging and monitoring | ISMS-IMP-A.8.20-21-22-S3 |

**Implementation Note**: Specific technical standards (cipher suites, protocol versions, configuration parameters) are defined in ISMS-IMP-A.8.20-21-22 implementation guides and may be updated without policy revision.

**Cloud Applicability**: Cloud network security (AWS VPC, Azure VNet, GCP VPC) **MUST** implement equivalent controls using cloud-native capabilities (security groups, network ACLs, virtual firewalls, cloud monitoring). See ISMS-IMP-A.8.20-21-22-S3 for cloud-specific guidance.

## Network Services Security (A.8.21)

[Organization] **MUST** implement the following network services security controls:

| Service Type | Mandatory Security Mechanisms | Implementation Reference |
|-------------|------------------------------|-------------------------|
| **DNS** | Industry-standard DNS security mechanisms **(specific mechanisms defined in ISMS-IMP-A.8.20-21-22-S4)**; Split DNS architecture; DNS query logging; DNS filtering for malicious domains; DDoS protection for public DNS | ISMS-IMP-A.8.20-21-22-S4 |
| **DHCP** | DHCP security mechanisms on switches **(specific mechanisms defined in ISMS-IMP-A.8.20-21-22-S4)**; Rogue DHCP detection; Documented scopes with periodic review; High availability for critical DHCP services | ISMS-IMP-A.8.20-21-22-S4 |
| **NTP** | NTP authentication mechanisms **(specific mechanisms defined in ISMS-IMP-A.8.20-21-22-S4)**; Documented time source hierarchy; Access control restrictions; Time synchronization monitoring | ISMS-IMP-A.8.20-21-22-S4 |
| **Proxy Services** | Authentication required; SSL/TLS interception (if applicable); Comprehensive logging; Bypass prevention | ISMS-IMP-A.8.20-21-22-S4 |
| **Load Balancers** | SSL/TLS termination with strong ciphers; Session management; DDoS protection; Health check monitoring | ISMS-IMP-A.8.20-21-22-S4 |
| **Authentication Services** | RADIUS/TACACS+ with MFA support; AAA logging; Encrypted communication; Redundancy for critical authentication | ISMS-IMP-A.8.20-21-22-S4 |
| **All Network Services** | Services catalog maintained; Service-specific monitoring; Availability SLA defined; Hardening per vendor guidelines; Regular patching | ISMS-IMP-A.8.20-21-22-S1, S4 |

**Service Availability Requirements**: Critical network services **MUST** define availability SLA (Service Level Agreement) based on business requirements and operational context.

**SLA Target Guidance**: Typical availability SLA targets based on service criticality and infrastructure redundancy:
- **Critical services with redundancy**: ≥99.9% (≤8.76 hours downtime/year)
- **Critical services without redundancy**: ≥99.5% (≤43.8 hours downtime/year)
- **Non-critical services**: ≥99.0% (≤87.6 hours downtime/year)

Service-specific SLA determination guidance is provided in ISMS-IMP-A.8.20-21-22-S4.

**Implementation Note**: Service-specific security configurations are documented in ISMS-IMP-A.8.20-21-22-S4 and may be updated based on threat intelligence without policy revision.

**Cloud Applicability**: Cloud-provided network services (Route 53, Azure DNS, Cloud Load Balancing) **MUST** implement equivalent security mechanisms using cloud-native capabilities. **Equivalency means comparable security outcomes, not identical implementation** (e.g., AWS Route 53 DNSSEC, query logging, and DNS Firewall achieve equivalent outcomes to on-premises DNS security). See ISMS-IMP-A.8.20-21-22-S4 for cloud-specific guidance and equivalency mapping.

## Network Segmentation (A.8.22)

[Organization] **MUST** implement the following network segmentation controls:

| Requirement Category | Mandatory Controls | Implementation Reference |
|---------------------|-------------------|-------------------------|
| **Security Zones** | Define and document security zones; Assign trust levels (Untrusted, Semi-Trusted, Trusted); Document zone purpose, networks, VLANs, allowed traffic flows | ISMS-IMP-A.8.20-21-22-S5 |
| **Segmentation Architecture** | Minimum zones: DMZ, Internal, Management, Guest; Additional zones based on data classification and regulatory requirements (Server, Development, OT/ICS, Cloud) | ISMS-IMP-A.8.20-21-22-S5 |
| **VLAN Segregation** | VLANs for logical segmentation; VLAN security mechanisms; VLAN-to-zone mapping documented | ISMS-IMP-A.8.20-21-22-S5 |
| **Inter-Zone Traffic Controls** | Firewalls or ACLs at trust boundaries; Default deny policy (explicit allow only); Stateful inspection for all inter-zone traffic; Traffic flow documentation | ISMS-IMP-A.8.20-21-22-S5 |
| **Trust Boundaries** | Define trust boundaries between zones; Enforce controls at every boundary; Log denied traffic; Regular firewall rule review | ISMS-IMP-A.8.20-21-22-S5 |
| **Segmentation Testing** | Periodic segmentation effectiveness testing; VLAN security testing; Traffic flow verification; Penetration testing of inter-zone controls | ISMS-IMP-A.8.20-21-22-S6 |
| **Flat Network Remediation** | Identify flat networks (no segmentation); Risk assessment of flat networks; Remediation plan based on risk prioritization | ISMS-IMP-A.8.20-21-22-S5 |
| **Microsegmentation** | Application-level segmentation for high-security requirements (SHOULD); Zero Trust network approaches where applicable | ISMS-IMP-A.8.20-21-22-S5 |

**Default Deny Principle**: All inter-zone traffic **MUST** be blocked by default. Only explicitly approved traffic flows permitted. Every permit rule **MUST** have documented business justification.

**Firewall Rule Justification Documentation**:

Business justification for all inter-zone permit rules is documented using the following mechanisms:

- **New rules**: Firewall rule change request (template in ISMS-IMP-A.8.20-21-22-S5) completed and approved before implementation
- **Existing rules**: Business justification recorded in network segmentation matrix (Workbook 4) during periodic firewall rule review
- **Emergency rules**: Documented within 48 hours of implementation per incident response procedures

Rules lacking documented business justification identified during review must be either justified and documented, or removed within a timeframe proportionate to the trust boundary criticality. For critical trust boundaries, resolution should not exceed 7 days; for other boundaries, 30 days.

**Implementation Note**: Specific VLAN assignments, subnet designs, and firewall rule templates are documented in ISMS-IMP-A.8.20-21-22-S5 and may be updated based on architecture changes without policy revision.

**Cloud Applicability**: Cloud network segmentation (VPCs, VNets, subnets, security groups, network ACLs) **MUST** implement equivalent controls. Public cloud flat networks (single VPC with no internal segmentation) **MUST** be remediated per risk assessment. See ISMS-IMP-A.8.20-21-22-S5 for cloud-specific guidance.

---

# Governance & Operations

## Roles & Responsibilities

**Chief Information Security Officer (CISO)**:

- Policy owner and ultimate accountability for network security controls
- Approve network security requirements and risk treatment decisions
- Approve exceptions to network security requirements
- Report network security posture to executive management
- Ensure adequate resources for network security implementation

**Chief Information Officer (CIO) / IT Director**:

- Operational accountability for network infrastructure and services
- Allocate resources for network security implementation
- Ensure network changes follow security requirements
- Approve network architecture and design changes

**Network Operations Manager**:

- Technical accountability for network security implementation
- Manage network security configurations and changes
- Coordinate with security team on security requirements
- Ensure network team training and competency
- Maintain network documentation and topology diagrams

**Network Administrators**:

- Implement network security controls on devices and services
- Follow device hardening procedures and secure configurations
- Implement firewall rules and ACLs per approved requirements
- Monitor network devices and respond to alerts
- Document network changes and maintain configuration backups

**Security Team / Information Security Manager**:

- Define network security requirements based on risk assessment
- Perform network security assessments (using assessment workbooks)
- Review and approve firewall rule changes
- Monitor network security events via SIEM
- Conduct segmentation effectiveness testing
- Report compliance status and gaps

**Cloud Administrators** (if applicable):

- Implement cloud network security controls (security groups, NACLs, etc.)
- Ensure cloud networks meet equivalent security requirements
- Coordinate with network team on hybrid network integration
- Document cloud network architecture

**System Owners**:

- Define network access requirements for their systems
- Ensure systems comply with network security policies
- Coordinate with network team on segmentation requirements
- Participate in incident response for their systems

**Legal/Compliance Officer**:

- Determine regulatory applicability (Tier 2 requirements)
- Ensure network security controls meet regulatory requirements
- Review network security for compliance with data protection laws

**Responsibility Matrix**:

| Activity | CISO | CIO/IT Director | Network Ops Mgr | Network Admins | Security Team | Cloud Admins |
|----------|------|-----------------|-----------------|----------------|---------------|--------------|
| Policy Approval | A | C | C | I | C | I |
| Requirements Definition | A | C | C | I | R | I |
| Network Architecture | A | A | R | C | C | C |
| Device Hardening | A | A | R | R | C | R |
| Segmentation Implementation | A | A | R | R | C | R |
| Firewall Rule Changes | C | C | R | R | A | R |
| Security Assessments | A | I | C | I | R | C |
| Exception Approval | A | C | C | I | C | I |
| Incident Response | A | A | R | R | R | R |

*R=Responsible, A=Accountable, C=Consulted, I=Informed*

## Monitoring & Reporting

**Continuous Monitoring**:

- Network security controls monitored through automated and manual mechanisms
- Network device logs monitored via centralized logging system
- Network traffic analyzed for security anomalies
- Security events trigger alerts and incident response procedures

**Periodic Reporting**:

- Network security compliance assessed periodically
- Network discovery and inventory maintained current
- Firewall rules and ACLs reviewed regularly
- Comprehensive network security assessments conducted
- Segmentation effectiveness validated through testing
- Network architecture documentation reviewed and updated

**Metrics and Performance Indicators**:

- Network security compliance metrics defined in assessment framework
- Key performance indicators (KPIs) documented in implementation guidance
- Targets and thresholds established based on organizational risk tolerance
- Gap remediation prioritized based on risk assessment
- Trend analysis conducted to identify security improvements

**Network Security Performance Targets**:

| Metric | Target | Measurement Frequency | Escalation Threshold | Collection Method |
|--------|--------|----------------------|---------------------|
| Network device hardening compliance | ≥95% | Quarterly | <90% triggers remediation plan | **Workbook 2 auto-generated from device config audits** |
| Network device inventory accuracy | ≥98% | Quarterly | <95% triggers discovery review | **Workbook 1 reconciliation with network discovery** |
| Firewall rule review completion | 100% within review cycle | Per defined review cycle | Any overdue review escalated to CISO | **Workbook 4 review date stamps** |
| Segmentation effectiveness test pass rate | 100% critical zones | Annually minimum | Any critical zone failure triggers immediate remediation | **Workbook 4 + pen test reports** |
| Network services availability (critical) | ≥99.9% | Monthly | <99.5% triggers incident review | **Workbook 3 + monitoring platform data** |
| Mean time to patch critical vulnerabilities (network devices) | ≤14 days | Monthly | >30 days triggers exception request | **Vulnerability scanner reports + patch logs** |
| Exception backlog | ≤5 active exceptions | Quarterly | >10 triggers executive review | **Exception register in GRC platform** |

**Metric Governance**: Detailed metric definitions, collection methods, and trending analysis documented in ISMS-IMP-A.8.20-21-22-S6. Targets reviewed annually and adjusted based on organizational risk tolerance and operational maturity.

**Reporting Audience**:

- **Executive Management**: Executive summary of network security posture, critical risks, strategic initiatives
- **CISO**: Detailed compliance reports, security event summaries, gap analysis
- **IT Management**: Operational metrics, service availability, infrastructure status
- **Auditors**: Access to assessment workbooks, evidence, and compliance documentation

## Exception Management

**Exception Request Process**:

When network security requirements cannot be met due to technical, operational, or business constraints, formal exception process applies:

1. **Exception Request**: Submitted by System Owner or Network Operations Manager
2. **Risk Assessment**: Security team evaluates security risk of exception
3. **Compensating Controls**: Identify alternative controls to mitigate risk (if possible)
4. **Business Justification**: Document business need and impact of non-exception
5. **Approval**: CISO approves/rejects exception based on risk tolerance
6. **Time Limit**: Exceptions granted for maximum 12 months (renewable)
7. **Monitoring**: Exceptions reviewed quarterly; compensating controls verified
8. **Remediation Plan**: Required for all exceptions (timeline to achieve compliance)

**Exception Approval Authority**:

- **Low Risk**: Information Security Manager
- **Medium Risk**: CISO
- **High Risk**: CISO + CIO (joint approval)
- **Critical Risk**: CISO + Executive Management

**Exception Documentation**:

- Exception ID and date
- Requirement(s) not met
- Risk assessment results
- Compensating controls implemented
- Business justification
- Approval chain
- Expiration date
- Remediation plan and timeline

**Common Exception Scenarios**:

- Legacy systems unable to support modern authentication (e.g., 802.1X)
- Cloud provider limitations preventing specific control implementation
- Temporary exception during migration or major project
- Operational impact outweighs security benefit (with compensating controls)

**Exception Denial**: If exception request denied, system/network **MUST** be brought into compliance or decommissioned based on risk assessment.

**Reference**: Detailed exception procedures in ISMS-IMP-A.8.20-21-22-S6.

## Incident Response

**Network Security Incidents** (triggering this policy):

- Unauthorized access to network devices or management interfaces
- Network device compromise (malware, backdoor, unauthorized changes)
- Network-based attacks (DDoS, ARP poisoning, VLAN hopping, man-in-the-middle)
- Network service compromise (DNS poisoning, rogue DHCP, NTP attacks)
- Segmentation bypass or flat network exploitation
- Configuration tampering or unauthorized firewall rule changes
- Network traffic anomalies indicating data exfiltration or lateral movement

**Incident Severity Classification**:

| Severity | Definition | Scope Indicators | Data Impact | Service Impact |
|----------|------------|-----------------|-------------|----------------|
| **Low** | Contained issue with minimal security impact | Single device or user affected | No data exposure confirmed | No service degradation |
| **Medium** | Potential for spread or escalation; requires prompt attention | Multiple devices or single network segment affected | Potential data exposure; no confirmation | Minor service degradation (<10% users) |
| **High** | Active threat or confirmed unauthorized access requiring urgent response | Multiple segments affected or critical systems targeted | Confirmed data exposure (limited scope) or access to sensitive systems | Significant service degradation (10-50% users) |
| **Critical** | Severe incident with organization-wide impact or active data exfiltration | Network-wide impact or management infrastructure compromised | Active data exfiltration or exposure of high-sensitivity data | Major service disruption (>50% users) |

**Severity Examples (Network Security)**:

| Severity | Example Scenarios |
|----------|-------------------|
| **Low** | Failed authentication attempts on single network device; minor configuration drift detected; single rogue AP detected and contained |
| **Medium** | Misconfigured firewall rule allowing unintended traffic (no exploitation confirmed); VLAN misconfiguration affecting non-critical segment; network service degradation from capacity issue |
| **High** | Compromised network device with evidence of reconnaissance; successful VLAN hopping attempt; unauthorized access to network management interface; segmentation bypass confirmed |
| **Critical** | Network device compromise affecting critical infrastructure; active lateral movement across segments; compromise of centralized authentication (RADIUS/TACACS+); network-wide DDoS with sustained impact; evidence of data exfiltration via network channels |

**Incident Response Process**:

1. **Detection**: Incident detected via monitoring, alerts, or user report
2. **Triage**: Security team assesses severity and impact
3. **Containment**: Immediate actions to limit damage (isolate compromised device/segment, block traffic, disable compromised accounts)
4. **Investigation**: Determine root cause, scope, and impact using logs and network forensics
5. **Eradication**: Remove threat (patch vulnerabilities, restore configurations, rebuild compromised devices)
6. **Recovery**: Return to normal operations with enhanced monitoring
7. **Post-Incident**: Lessons learned, update security controls, improve detection

**Escalation Requirements**:

| Severity | Initial Response | Notification Timeline | Notification Recipients |
|----------|-----------------|---------------------|------------------------|
| **Low** | Network/security team handles | Within 24 hours | Network Operations Manager |
| **Medium** | Network/security team handles with management awareness | Within 4 hours | Network Operations Manager, Information Security Manager |
| **High** | Incident response team engaged | Within 1 hour | CISO, CIO, Network Operations Manager |
| **Critical** | Full incident response activation | Immediate | CISO, CIO, Executive Management, Legal/Compliance (if data breach) |

**Severity Escalation**: Incidents may be escalated to higher severity if:

- Scope expands beyond initial assessment
- Data impact confirmed or increased
- Containment measures prove ineffective
- Duration exceeds expected resolution time

**Incident Logging**: All network security incidents logged in incident management system with timeline, actions taken, root cause, and remediation.

**Reference**: Detailed incident response procedures in organizational incident response plan and ISMS-IMP-A.8.20-21-22-S6.

## Policy Governance

**Policy Review**:

- **Frequency**: Annual review cycle
- **Triggers**: Regulatory changes, significant security incidents, technology changes, organizational changes, audit findings
- **Reviewers**: CISO (primary), CIO, Network Operations Manager, Legal/Compliance Officer
- **Approval**: Executive Management (final authority)

**Implementation Standards Review** (separate lifecycle from policy):

- **Frequency**: Quarterly or as needed for technology updates
- **Scope**: ISMS-IMP-A.8.20-21-22 implementation guides (technical standards, procedures, configurations)
- **Authority**: CISO approves implementation standard updates without requiring policy revision
- **Rationale**: Separates stable governance (policy) from evolving technical details (implementation standards)

**Policy Updates**:

**Minor Updates** (no material change to requirements):

- Typographical corrections, formatting, clarifications
- Updated references to other documents
- Updated regulatory references (no new requirements)
- Approval: CISO
- Notification: Update version number (e.g., 1.0 → 1.1)

**Major Updates** (material change to requirements):

- New security requirements or controls
- Changes to roles/responsibilities
- Changes to exception approval authority
- Scope changes
- Approval: Executive Management (full approval chain)
- Notification: Update version number (e.g., 1.0 → 2.0)
- Communication: Notification to all stakeholders, training if needed

**Emergency Updates** (urgent security risk):

- Critical vulnerability or threat requiring immediate policy change
- Regulatory mandate requiring immediate compliance
- Approval: CISO (with Executive Management notification within 24 hours)
- Notification: Immediate communication to affected parties
- Formalization: Retroactive approval at next policy review

**Communication**:

- Policy updates communicated via email to all affected stakeholders
- Updated policy published on internal policy portal
- Training provided if policy changes affect operational procedures
- Obsolete versions clearly marked and removed from circulation

---

# Implementation & References

## Integration with ISMS

**ISO/IEC 27001:2022 Clause 6.1 - Risk Assessment**:

Network security controls implemented based on [Organization]'s risk assessment:

- Network infrastructure risks (A.8.20) identified and assessed
- Network services risks (A.8.21) identified and assessed
- Network segmentation risks (A.8.22) identified and assessed
- Risk treatment decisions document which controls are implemented and to what level

**ISO/IEC 27001:2022 Clause 6.1.3 - Statement of Applicability**:

This policy supports the following SoA entries:

| Control | Status | Justification | Implementation |
|---------|--------|---------------|----------------|
| **A.8.20 - Networks Security** | ☑ Applicable | [Organization] operates network infrastructure requiring security controls | Section 2.1, ISMS-IMP-A.8.20-21-22-UG/TG |
| **A.8.21 - Security of Network Services** | ☑ Applicable | [Organization] operates critical network services requiring security controls | Section 2.2, ISMS-IMP-A.8.20-21-22-UG/TG |
| **A.8.22 - Segregation of Networks** | ☑ Applicable | [Organization] requires network segmentation to limit risk and meet regulatory requirements | Section 2.3, ISMS-IMP-A.8.20-21-22-UG/TG |

**Related Controls** (integration points):

**A.8.15 - Logging**:

- Network devices generate security logs
- Network services log critical events
- Logs centralized in SIEM for correlation
- Integration: Network devices configured to log per A.8.15 requirements

**A.8.16 - Monitoring Activities**:

- Network traffic monitored for anomalies (NetFlow/sFlow, IDS/IPS)
- Network services monitored for availability and performance
- Security events trigger alerts
- Integration: Network monitoring integrated with organizational monitoring framework per A.8.16

**A.8.8 - Technical Vulnerability Management**:

- Network devices scanned for vulnerabilities
- Firmware/software patched based on vulnerability severity
- Integration: Network devices included in vulnerability management scope per A.8.8

**A.8.9 - Configuration Management**:

- Network device configurations baselined
- Configuration changes controlled via change management
- Configuration backups automated and tested
- Integration: Network configurations managed per A.8.9 requirements

**A.5.23 - Cloud Services**:

- Cloud network security assessed (AWS VPC, Azure VNet, GCP VPC)
- Hybrid network integration evaluated
- Integration: Cloud networking subject to this policy and assessed per A.5.23

**A.8.23 - Web Filtering**:

- Web filtering implemented using network controls (proxy, DNS filtering)
- Integration: Web filtering infrastructure secured per this policy

**A.8.1 - User Endpoint Devices**:

- Endpoint network access controlled via 802.1X or NAC
- Integration: Endpoint network access policies enforced by network controls

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.20-21-22):

| Document | Purpose | Scope |
|----------|---------|-------|
| **ISMS-IMP-A.8.20-21-22-S1** | Network Discovery Process | Automated and manual network discovery procedures; Tools and methodologies; Discovery validation |
| **ISMS-IMP-A.8.20-21-22-S2** | Network Architecture Documentation | Topology diagram requirements; Documentation standards; Update procedures |
| **ISMS-IMP-A.8.20-21-22-S3** | Device Hardening Process | Device-specific hardening procedures; CIS benchmark application; Configuration templates; Wireless and VPN security |
| **ISMS-IMP-A.8.20-21-22-S4** | Network Services Security Process | Service-by-service security implementation (DNS, DHCP, NTP, proxy, load balancers); Monitoring and availability |
| **ISMS-IMP-A.8.20-21-22-S5** | Segmentation Implementation | Zone design process; VLAN configuration; Firewall rule development; ACL implementation; Cloud segmentation |
| **ISMS-IMP-A.8.20-21-22-S6** | Network Security Testing | Segmentation effectiveness testing; Penetration testing; VLAN hopping tests; Service security testing |

**Assessment Tools** (Python-generated Excel workbooks):

| Workbook | Purpose | Update Frequency |
|----------|---------|-----------------|
| **Workbook 1 - Network Infrastructure Inventory** | Device inventory with location, ownership, criticality, compliance status | Per implementation guidance |
| **Workbook 2 - Network Device Security Assessment** | Device-by-device hardening compliance, gap identification | Per implementation guidance |
| **Workbook 3 - Network Services Catalog** | Services inventory with security mechanisms, availability, monitoring status | Per implementation guidance |
| **Workbook 4 - Network Segmentation Matrix** | Security zones, trust relationships, inter-zone policies, effectiveness tests | Per implementation guidance |
| **Workbook 5 - Security Controls Coverage** | Master controls matrix showing which controls protect which segments | Per implementation guidance |
| **Dashboard - Network Security Compliance** | Consolidated compliance view with metrics and trends | Per implementation guidance |

**Supporting Materials**:

- Network topology diagram templates
- CIS benchmarks for network devices
- Vendor hardening guides (Cisco, Juniper, Palo Alto, AWS, Azure, etc.)
- Firewall rule change request templates
- Segmentation effectiveness test procedures

## Regulatory Mapping

**Regulatory Requirements Matrix**:

| Regulation | Specific Requirements | Implementation Section | Evidence |
|------------|---------------------|----------------------|----------|
| **Swiss nDSG** | Technical measures to protect personal data; Access controls; Logging | Section 2.1, 2.2, 2.3 | Network security assessments, logs, segmentation documentation |
| **EU GDPR (Art. 32)** | Technical measures including network security; Access controls; Encryption of data in transit | Section 2.1, 2.2, 2.3 | Network security assessments, encryption configs |
| **ISO 27001:2022** | A.8.20 network device security; A.8.21 network services security; A.8.22 network segmentation | Section 2.1, 2.2, 2.3 | All assessment workbooks |
| **PCI DSS (Req. 1)** | Firewall and router configuration standards; Network segmentation for cardholder data | Section 2.3 | Segmentation matrix (Workbook 4), firewall configs |
| **FINMA** | Network security controls; Segregation of environments; Monitoring | Section 2.1, 2.2, 2.3 | Network security assessments, monitoring logs |
| **DORA** | Network and information systems security; Network segmentation | Section 2.1, 2.3 | Network security assessments, segmentation documentation |
| **NIS2** | Network security measures; Network segmentation; Security monitoring | Section 2.1, 2.2, 2.3 | All assessment workbooks, monitoring evidence |

**Compliance Verification**: Regulatory compliance verified through:

- Quarterly network security assessments
- Annual internal audits
- External certification audits (ISO 27001, sector-specific)
- Regulatory examinations (FINMA, NIS2 authorities as applicable)

## Training & Awareness

**Security Awareness** (all personnel):

- **Audience**: All employees, contractors, temporary staff
- **Content**: Network access policies; Acceptable use; Incident reporting; Social engineering awareness
- **Frequency**: Annual security awareness training
- **Delivery**: E-learning modules, mandatory completion
- **Verification**: Training completion tracked in HR system

**Technical Training** (IT/security staff):

**Network Administrators**:

- **Content**: Device hardening procedures; Secure configurations; Firewall rule management; VLAN configuration; Wireless security; VPN security
- **Frequency**: Annual, plus ad-hoc for new technologies or policy updates
- **Delivery**: Hands-on workshops, vendor training, internal knowledge transfer
- **Verification**: Competency assessment, certification programs (e.g., CCNA Security, network vendor certifications)

**Security Team**:

- **Content**: Network security assessment methodologies; Segmentation effectiveness testing; Penetration testing techniques; Cloud network security; Security monitoring and SIEM
- **Frequency**: Annual, plus continuous learning for emerging threats
- **Delivery**: Security conferences, specialized training courses, certification programs
- **Verification**: Security certifications (CISSP, GIAC, vendor security certifications)

**Cloud Administrators**:

- **Content**: Cloud network security (AWS, Azure, GCP); Security groups and NACLs; Cloud monitoring; Hybrid network security
- **Frequency**: Annual, plus updates for new cloud services
- **Delivery**: Cloud vendor training, certification programs (AWS Certified Security, Azure Security Engineer, etc.)
- **Verification**: Cloud security certifications

**Operational Training** (IT operations, help desk):

- **Content**: Network security basics; Recognizing security incidents; Escalation procedures; Change management procedures
- **Frequency**: Annual
- **Delivery**: Internal training sessions, documentation review
- **Verification**: Training completion and knowledge checks

**Specialized Training** (as needed):

- Software-defined networking (SDN) security
- Zero Trust network architecture
- Advanced threat detection and response
- Network forensics and incident investigation

---

# Definitions

**Periodic Activity Frequency Standards**:

Unless explicitly stated otherwise in this policy or referenced implementation guidance, the following minimum frequencies apply:

| Term | Minimum Frequency | Applicable Activities |
|------|-------------------|----------------------|
| **Continuous** | Real-time or near-real-time automated monitoring | Network device monitoring, traffic analysis, security event logging |
| **Regular** | Monthly | Patching review, configuration backup verification, service availability review |
| **Periodic** | Quarterly | Security assessments, inventory validation, firewall rule review, metrics reporting |
| **Annual** | Once per calendar year (within 12 months of previous) | Segmentation effectiveness testing, policy review, comprehensive architecture review, penetration testing |

**Frequency Adjustments**: Activity frequencies may be increased based on:

- Risk assessment findings indicating elevated threat levels
- Regulatory requirements mandating specific frequencies
- Audit findings requiring enhanced monitoring
- Significant changes to network infrastructure or threat landscape

Frequency reductions require CISO approval and documented risk acceptance.

**Key Terms**:

**Critical Network Services**: Network services whose failure would cause significant business disruption or security impact. Criticality determination is documented in the network services catalog (Workbook 3) based on business impact assessment. Examples: DNS (business-wide impact), DHCP for server VLANs (critical infrastructure dependency), NTP for authentication systems (security dependency), RADIUS/TACACS+ (authentication infrastructure).

**Defense in Depth**: Layered security approach using multiple security controls at different levels to protect information assets. In network security context: perimeter controls + segmentation + device hardening + monitoring.

**DMZ (Demilitarized Zone)**: Network segment isolated from both internal networks and the internet, typically hosting internet-facing services (web servers, mail relays, VPN concentrators).

**Flat Network**: Network with no segmentation - all systems can communicate with all other systems without firewall or ACL controls. Considered high-risk architecture.

**Microsegmentation**: Fine-grained network segmentation at the application or workload level, often implemented using software-defined networking or host-based firewalls.

**NAC (Network Access Control)**: Technology that enforces security policies on devices seeking network access, typically checking device compliance before allowing network connectivity.

**SDN (Software-Defined Networking)**: Network architecture approach that enables programmatic network control by separating the control plane from the data plane.

**Security Zone**: Logical or physical network segment with common security requirements, trust level, and data classification. Examples: DMZ, Internal, Management, Guest.

**Trust Boundary**: Network perimeter where trust level changes, requiring security controls (firewall, ACLs) to enforce access policies between zones.

**VLAN (Virtual Local Area Network)**: Logical network segment created on physical network infrastructure using IEEE 802.1Q standard, enabling network segregation without separate physical networks.

**Zero Trust Network**: Security model that assumes no implicit trust based on network location. All access requests verified regardless of source, emphasizing "never trust, always verify."

---

# Approval Record

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Document Owner (CISO)** | [Name] | [Date] | [Signature] |
| **Technical Review (CIO)** | [Name] | [Date] | [Signature] |
| **Technical Review (Network Ops Mgr)** | [Name] | [Date] | [Signature] |
| **Compliance Review (Legal/Compliance)** | [Name] | [Date] | [Signature] |
| **Final Approval (Executive Management)** | [Name] | [Date] | [Signature] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for network security controls covering network infrastructure (A.8.20), network services (A.8.21), and network segmentation (A.8.22). Implementation procedures are documented in ISMS-IMP-A.8.20-21-22 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-02 -->