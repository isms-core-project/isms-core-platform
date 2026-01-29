# ISMS-POL-A.8.20-21-22-S5 – Assessment Methodology & Evidence Framework
## Network Security Assessment and Compliance Verification

---

**Document ID**: ISMS-POL-A.8.20-21-22-S5  
**Title**: Assessment Methodology & Evidence Framework  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / CISO | Initial assessment methodology framework |

**Review Cycle**: Annual  
**Parent Document**: ISMS-POL-A.8.20-21-22 (Master Framework)  
**Related Documents**: S2 (A.8.20 Requirements), S3 (A.8.21 Requirements), S4 (A.8.22 Requirements)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document defines the **unified assessment methodology** for evaluating compliance with ISO/IEC 27001:2022 Controls A.8.20 (Networks Security), A.8.21 (Security of Network Services), and A.8.22 (Segregation of Networks).

The assessment methodology provides:
- Systematic approach to network security evaluation
- Standardized evidence collection procedures
- Consistent compliance scoring methodology
- Clear audit trail for certification/compliance verification
- Continuous improvement framework

### 1.2 Scope

This assessment framework covers:
- **Network Discovery**: Systematic identification of all network assets (devices, services, segments)
- **Network Security Assessment**: Evaluation of network infrastructure security (A.8.20)
- **Network Services Assessment**: Evaluation of network services security (A.8.21)
- **Network Segmentation Assessment**: Evaluation of network segregation effectiveness (A.8.22)
- **Evidence Collection**: Documentation and artifact gathering for audit purposes
- **Compliance Scoring**: Quantitative measurement of control implementation
- **Gap Management**: Identification, prioritization, and remediation tracking

### 1.3 Systems Engineering Approach

This framework employs a **Systems Engineering methodology**:

```
Discovery → Documentation → Evaluation → Gap Identification → Remediation → Verification
    ↑                                                                            ↓
    └────────────────────────── Continuous Improvement ─────────────────────────┘
```

**Key Principles**:
1. **Systematic**: Structured, repeatable processes
2. **Evidence-Based**: Objective verification over subjective claims
3. **Technology-Agnostic**: Works across any network architecture
4. **Automation-First**: Python-generated workbooks for consistency
5. **Continuous**: Not just point-in-time, but ongoing assessment

---

## 2. Assessment Methodology Overview

### 2.1 Assessment Lifecycle

**Phase 1: Planning**
- Define assessment scope (which networks, devices, services, segments)
- Identify stakeholders and responsibilities
- Schedule assessment activities
- Prepare assessment tools and workbooks

**Phase 2: Discovery**
- Execute automated network discovery (nmap, SNMP, cloud APIs)
- Execute manual discovery (documentation review, interviews)
- Map network topology (physical, logical, security zones)
- Inventory network devices
- Identify network services
- Document network segmentation

**Phase 3: Data Collection**
- Gather network device configurations
- Collect service configurations
- Document firewall rules and ACLs
- Collect logs (network devices, services)
- Gather vulnerability scan reports
- Collect penetration test reports

**Phase 4: Evaluation**
- Assess network device hardening (against baselines)
- Assess network services security (service-specific requirements)
- Assess network segmentation effectiveness
- Calculate compliance scores per control
- Identify gaps and deviations

**Phase 5: Gap Analysis**
- Classify gaps by severity (Critical, High, Medium, Low)
- Prioritize remediation based on risk
- Document compensating controls (if applicable)
- Create remediation plans with timelines

**Phase 6: Reporting**
- Generate assessment workbooks (WB1-WB5)
- Generate executive dashboard
- Present findings to management
- Present evidence to auditors (if audit cycle)

**Phase 7: Remediation**
- Execute remediation plans
- Track remediation progress
- Verify remediation effectiveness
- Update assessment workbooks

**Phase 8: Continuous Monitoring**
- Automated configuration drift detection
- Real-time log analysis (SIEM integration)
- Continuous vulnerability scanning
- Periodic re-assessment (quarterly)

### 2.2 Assessment Types

**Initial Assessment (Comprehensive)**:
- Full network discovery across all segments
- Complete evaluation of all requirements (A.8.20, A.8.21, A.8.22)
- Baseline establishment for future comparisons
- Executed: Upon framework implementation
- Duration: 4-6 weeks (depending on network size/complexity)

**Annual Assessment (Full Re-Assessment)**:
- Scheduled comprehensive re-assessment
- Full re-discovery and re-evaluation
- Trend analysis (compare to previous assessments)
- Executed: Annually (scheduled)
- Duration: 3-4 weeks

**Quarterly Assessment (Targeted)**:
- Focused assessment on high-risk areas
- Update assessment workbooks
- Verify remediation of previous gaps
- Executed: Quarterly
- Duration: 1-2 weeks

**Triggered Assessment (As-Needed)**:
- Triggered by: Major network changes, security incidents, regulatory changes
- Scope: Focused on changed areas
- Executed: As needed
- Duration: 1-3 weeks (depending on trigger)

**Continuous Assessment (Ongoing)**:
- Automated configuration monitoring
- Real-time log analysis
- Continuous vulnerability scanning
- Dashboard updates
- Executed: Continuously (automated)
- No specific duration (ongoing)

### 2.3 Assessment Frequency Summary

| Assessment Type | Frequency | Scope | Duration | Trigger |
|-----------------|-----------|-------|----------|---------|
| Initial | Once | Full | 4-6 weeks | Framework implementation |
| Annual | Yearly | Full | 3-4 weeks | Scheduled |
| Quarterly | Quarterly | Targeted | 1-2 weeks | Scheduled |
| Triggered | As needed | Focused | 1-3 weeks | Changes, incidents, regulatory |
| Continuous | Ongoing | Automated | N/A | Real-time monitoring |

---

## 3. Network Discovery Methodology

### 3.1 Discovery Objectives

Network discovery aims to achieve **100% visibility** of:
- All network devices (routers, switches, firewalls, wireless APs, VPN concentrators, load balancers)
- All network services (DNS, DHCP, NTP, proxy, load balancers, authentication, monitoring, logging)
- All network segments (security zones, VLANs, subnets, cloud networks)
- Network topology (physical, logical, security architecture)

### 3.2 Automated Discovery Methods

**Network Scanning (nmap, commercial scanners)**:
- **Purpose**: Identify all reachable network devices and services
- **Tools**: nmap, Nessus Discovery, Qualys Asset Inventory, commercial IPAM tools
- **Execution**: 
  - Network sweep scans (ICMP ping sweep, TCP SYN scan)
  - Service detection scans (port scanning, service fingerprinting)
  - OS detection
- **Output**: List of IP addresses, open ports, services, OS versions
- **Frequency**: Quarterly (or after major network changes)

**SNMP-Based Discovery**:
- **Purpose**: Inventory managed network devices via SNMP
- **Tools**: SNMPwalk, commercial network management systems
- **Execution**: Query network devices via SNMP (preferably SNMPv3)
- **Output**: Device details (make, model, firmware version, interfaces, neighbors)
- **Frequency**: Monthly (automated)

**NetFlow/sFlow Analysis**:
- **Purpose**: Discover devices and services via traffic analysis
- **Tools**: NetFlow collectors, sFlow analyzers
- **Execution**: Analyze network traffic flows
- **Output**: Device communications, service usage patterns, traffic volumes
- **Frequency**: Continuous (real-time traffic analysis)

**Configuration Management Database (CMDB) Integration**:
- **Purpose**: Leverage existing asset management data
- **Tools**: ServiceNow, CMDB tools, asset management systems
- **Execution**: Query CMDB for network asset inventory
- **Output**: Device inventory with ownership, criticality, lifecycle data
- **Frequency**: Weekly (automated sync)

**Cloud API-Based Discovery**:
- **Purpose**: Discover cloud network resources (AWS VPC, Azure VNet, GCP VPC)
- **Tools**: AWS CLI, Azure CLI, GCP SDK, Terraform state, cloud-native inventory tools
- **Execution**: API queries for network resources (VPCs, subnets, security groups, load balancers, etc.)
- **Output**: Cloud network inventory
- **Frequency**: Daily (automated)

### 3.3 Manual Discovery Methods

**Documentation Review**:
- Review existing network diagrams
- Review IP address management (IPAM) documentation
- Review VLAN/subnet allocation records
- Review firewall ruleset documentation
- Review network architecture documents

**Interviews with Network Administrators**:
- Identify undocumented network segments
- Identify shadow IT / unauthorized devices
- Clarify network architecture decisions
- Identify planned network changes

**Physical Site Surveys**:
- Data center walk-throughs (rack diagrams, cabling)
- Wiring closet inspections
- Identify rogue devices (unauthorized wireless APs, switches)

**Log Analysis**:
- Review DHCP logs (identify devices obtaining IP addresses)
- Review DNS logs (identify device hostname resolutions)
- Review firewall logs (identify connection attempts)
- Review authentication logs (identify devices authenticating to network services)

### 3.4 Discovery Data Consolidation

**Data Sources**:
- Automated scans (nmap, SNMP, NetFlow, cloud APIs)
- Manual discovery (documentation, interviews, surveys, logs)
- Existing databases (CMDB, IPAM, asset management)

**Data Normalization**:
- Deduplicate devices (same device from multiple sources)
- Resolve conflicts (discrepancies between sources)
- Validate data (IP address format, reachability verification)
- Enrich data (add ownership, criticality, lifecycle info)

**Output: Network Inventory**:
- Device inventory → feeds **WB1: Network Infrastructure Inventory**
- Service inventory → feeds **WB3: Network Services Catalog**
- Segment inventory → feeds **WB4: Network Segmentation Matrix**

### 3.5 Discovery Challenges and Mitigation

| Challenge | Mitigation Strategy |
|-----------|---------------------|
| **Hidden/Dark Devices** (not responding to scans) | Passive network monitoring (NetFlow/sFlow), MAC address table review on switches, DHCP log analysis |
| **Cloud/Hybrid Environments** (distributed resources) | Multi-tool approach (cloud APIs + network scans), cloud-native discovery tools |
| **Large/Complex Networks** (scale) | Phased discovery (segment-by-segment), distributed scanning, parallelization |
| **Discovery Impact** (network load, service disruption) | Rate limiting, scheduled scans during maintenance windows, pilot testing |
| **Incomplete Data** (missing ownership, purpose) | Follow-up with network administrators, document assumptions, iterative refinement |

---

## 4. Network Security Assessment Process (A.8.20)

### 4.1 Assessment Objectives

Evaluate compliance with **A.8.20 (Networks Security)** requirements defined in Section 2 (S2).

**Assessment Scope**:
- Network infrastructure security
- Network device security (hardening)
- Network perimeter controls
- Network access controls
- Network monitoring and logging
- Wireless network security
- Remote access network security
- Configuration management

### 4.2 Assessment Methodology

**Step 1: Device Inventory Validation**
- Verify all network devices are inventoried in **WB1: Network Infrastructure Inventory**
- Confirm device criticality classifications
- Validate device ownership/responsibility assignments

**Step 2: Device Hardening Assessment**
- Compare device configurations to hardening baselines (CIS benchmarks, vendor hardening guides)
- Assess each hardening requirement in **WB2: Network Device Security Assessment**:
  - Default credentials disabled (Yes/No/N/A)
  - Strong password policy enforced (Yes/No/N/A)
  - MFA for administrative access (Yes/No/N/A)
  - Unnecessary services disabled (Yes/No/N/A)
  - Secure management protocols (SSH/HTTPS only) (Yes/No/N/A)
  - Logging enabled (Yes/No/N/A)
  - NTP configured (Yes/No/N/A)
  - SNMP v3 only (Yes/No/N/A)
  - Session timeouts configured (Yes/No/N/A)
  - Banner messages configured (Yes/No/N/A)
  - Configuration backups (automated) (Yes/No/N/A)
  - Firmware up-to-date (Yes/No/N/A)
- Calculate compliance score per device: (# Yes / # applicable) × 100%
- Identify gaps (requirements marked "No")

**Step 3: Perimeter Controls Assessment**
- Verify firewall rules for internet-facing perimeter
- Assess IPS/IDS deployment and configuration
- Verify DDoS protection mechanisms
- Review perimeter logging and monitoring

**Step 4: Access Controls Assessment**
- Assess 802.1X deployment (if applicable for wired networks)
- Assess NAC deployment and effectiveness
- Review MAC address management policies
- Verify guest network isolation

**Step 5: Monitoring and Logging Assessment**
- Verify network device logging is enabled and functional
- Verify logs are centralized (syslog server, SIEM)
- Assess NetFlow/sFlow collection (if applicable)
- Verify integration with A.8.15 (Logging) and A.8.16 (Monitoring)

**Step 6: Wireless Network Security Assessment**
- Verify wireless encryption (WPA3 preferred, WPA2 minimum)
- Assess wireless authentication (802.1X EAP-TLS preferred)
- Verify rogue AP detection is functional
- Verify wireless segmentation (guest isolation)

**Step 7: Remote Access Security Assessment**
- Verify VPN security (IPsec or SSL/TLS VPN)
- Verify MFA for remote access
- Review split-tunnel vs. full-tunnel policies
- Verify remote access logging

**Step 8: Configuration Management Assessment**
- Verify configuration backups are automated and encrypted
- Verify configuration change management process (approval, documentation)
- Assess configuration baseline compliance
- Review configuration audit trails

### 4.3 Compliance Scoring (A.8.20)

**Overall A.8.20 Compliance Score** = (# compliant requirements / # total applicable requirements) × 100%

**Requirements Breakdown** (from S2):
- Infrastructure Security: 8 requirements
- Device Security: 12 requirements
- Perimeter Controls: 6 requirements
- Access Controls: 6 requirements
- Monitoring & Logging: 5 requirements
- Wireless Security: 5 requirements
- Remote Access Security: 4 requirements
- Configuration Management: 4 requirements
- **Total: 50 requirements** (some marked as MUST, some as SHOULD - weight accordingly)

**Weighting**:
- MUST requirements: 100% weight (mandatory)
- SHOULD requirements: 50% weight (risk-based, strongly recommended)

**Example Calculation**:
- 40 MUST requirements: 35 compliant → 35/40 = 87.5%
- 10 SHOULD requirements: 7 compliant → 7/10 = 70%
- Weighted Score = (87.5% × 0.8) + (70% × 0.2) = 70% + 14% = 84%

### 4.4 Evidence Collection (A.8.20)

**Required Evidence**:
- Network topology diagrams (logical, physical, security zones) - **WB1**
- Network device inventory - **WB1**
- Device configurations (routers, switches, firewalls, wireless APs) - redacted for sensitive info
- Device hardening assessment results - **WB2**
- Vulnerability scan reports (network devices)
- Penetration test reports (network perimeter, internal)
- Network monitoring logs (sample)
- Firewall logs (sample)
- Configuration backup logs (automated backup verification)
- Wireless rogue AP detection logs/reports

---

## 5. Network Services Assessment Process (A.8.21)

### 5.1 Assessment Objectives

Evaluate compliance with **A.8.21 (Security of Network Services)** requirements defined in Section 3 (S3).

**Assessment Scope**:
- Network services inventory
- Service-specific security (DNS, DHCP, NTP, proxy, load balancers, authentication, SNMP, syslog)
- Service availability and performance
- Service monitoring and alerting
- Service redundancy and failover
- Service hardening and patching

### 5.2 Assessment Methodology

**Step 1: Services Inventory Validation**
- Verify all network services are inventoried in **WB3: Network Services Catalog**
- Confirm service criticality classifications
- Validate service ownership/responsibility assignments

**Step 2: Service-Specific Security Assessment**

For each service type, assess service-specific requirements:

**DNS (6 requirements)**:
- DNSSEC enabled (Yes/No)
- Split DNS configured (Yes/No)
- DNS filtering enabled (Yes/No)
- Query logging enabled (Yes/No)
- Rate limiting configured (Yes/No)
- DNS server hardened (Yes/No)

**DHCP (4 requirements)**:
- DHCP snooping enabled (Yes/No)
- Rogue DHCP detection functional (Yes/No)
- Scope management documented (Yes/No)
- DHCP logging enabled (Yes/No)

**NTP (4 requirements)**:
- NTP authentication enabled (Yes/No)
- Stratum hierarchy documented (Yes/No)
- Access controls configured (Yes/No)
- Rate limiting configured (Yes/No)

**Proxy (5 requirements)**:
- Authentication enabled (Yes/No)
- SSL/TLS interception configured (Yes/No, with privacy considerations)
- Logging enabled (Yes/No)
- Bypass prevention configured (Yes/No)
- Content filtering enabled (Yes/No)

**Load Balancer (6 requirements)**:
- SSL/TLS termination secured (Yes/No)
- Session persistence configured (Yes/No)
- Health checks configured (Yes/No)
- DDoS protection enabled (Yes/No)
- Logging enabled (Yes/No)
- Redundancy configured (Yes/No)

**Authentication Services (4 requirements - RADIUS/TACACS+)**:
- Centralized authentication for network devices (Yes/No)
- Secure key management (Yes/No)
- Command authorization (TACACS+ - Yes/No/N/A)
- Redundancy configured (Yes/No)

**SNMP (3 requirements)**:
- SNMPv3 only (v1/v2 disabled) (Yes/No)
- Authentication and encryption (Yes/No)
- Access controls configured (Yes/No)

**Syslog (4 requirements)**:
- Centralized logging (Yes/No)
- Encrypted transport (TLS) (Yes/No)
- Log retention policy (Yes/No)
- Redundancy configured (Yes/No)

**Step 3: Service Availability Assessment**
- Verify service SLA definitions
- Assess actual uptime vs. SLA requirements
- Review service performance monitoring data
- Identify availability gaps

**Step 4: Service Monitoring Assessment**
- Verify service health monitoring (uptime, performance)
- Verify service security monitoring (log collection, alerting)
- Assess integration with A.8.16 (Monitoring Activities)
- Review alerting thresholds and escalation

**Step 5: Service Redundancy Assessment**
- Verify high availability configuration (where required based on criticality)
- Review failover testing results
- Assess geographic distribution (if applicable)
- Verify backup service configurations

**Step 6: Service Hardening and Patching Assessment**
- Assess service hardening compliance (CIS benchmarks where applicable)
- Verify service vulnerability scanning
- Review service patching status
- Assess integration with A.8.8 (Vulnerability Management)

### 5.3 Compliance Scoring (A.8.21)

**Overall A.8.21 Compliance Score** = (# compliant requirements / # total applicable requirements) × 100%

**Requirements Breakdown** (from S3):
- Services Inventory: 5 requirements
- DNS Security: 6 requirements
- DHCP Security: 4 requirements
- NTP Security: 4 requirements
- Proxy Security: 5 requirements
- Load Balancer Security: 6 requirements
- Authentication Services: 4 requirements
- SNMP Security: 3 requirements
- Syslog Security: 4 requirements
- Service Availability: 4 requirements
- Service Monitoring: 4 requirements
- Service Redundancy: 3 requirements
- Service Hardening & Patching: 2 requirements
- **Total: 54 requirements** (31 MUST, 23 SHOULD)

**Weighting**: Same as A.8.20 (MUST = 100% weight, SHOULD = 50% weight)

### 5.4 Evidence Collection (A.8.21)

**Required Evidence**:
- Network services catalog - **WB3**
- Service configurations (DNS, DHCP, NTP, proxy, load balancers, etc.)
- Service security assessment results - **WB3** (service-specific tabs)
- Service availability reports (SLA compliance data)
- Service monitoring logs (sample)
- Service failover test results
- Service vulnerability scan reports
- Service patching/update logs

---

## 6. Network Segmentation Assessment Process (A.8.22)

### 6.1 Assessment Objectives

Evaluate compliance with **A.8.22 (Segregation of Networks)** requirements defined in Section 4 (S4).

**Assessment Scope**:
- Network segmentation architecture
- Security zones definition and implementation
- VLAN segregation
- Subnet design
- Inter-zone traffic controls (firewall rules, ACLs)
- Segmentation effectiveness testing
- Flat network identification
- Cloud network segmentation

### 6.2 Assessment Methodology

**Step 1: Security Zones Inventory Validation**
- Verify all security zones are inventoried in **WB4: Network Segmentation Matrix**
- Confirm zone trust levels and data classifications
- Validate zone ownership/responsibility assignments

**Step 2: Segmentation Architecture Assessment**
- Review network segmentation architecture against requirements
- Verify security zones are properly defined (DMZ, Internal, Management, Guest, Server, etc.)
- Assess trust boundaries and trust relationships
- Verify segmentation technology (VLANs, physical separation, VRF, cloud security groups)

**Step 3: VLAN Segregation Assessment**
- Verify VLAN usage and design
- Assess VLAN security (native VLAN changes, DTP disabled, trunk security)
- Review VLAN-to-subnet mapping
- Verify VLAN documentation

**Step 4: Inter-Zone Traffic Controls Assessment**
- Review firewall rules between zones in **WB4: Inter-Zone Traffic Matrix**
- Verify default deny policies
- Assess rule justifications and documentation
- Verify rule review and approval process
- Identify excessive permissive rules or rule sprawl

**Step 5: Segmentation Effectiveness Testing**
- Review segmentation test results in **WB4: Segmentation Effectiveness Testing**
- Verify traffic flow validation (tcpdump, Wireshark)
- Review firewall rule testing results
- Assess lateral movement testing (penetration test results)
- Review VLAN hopping test results

**Step 6: Flat Network Identification**
- Identify flat network segments (single broadcast domain, no segmentation)
- Assess flat network risks
- Review flat network remediation plans
- Track flat network remediation progress

**Step 7: Cloud Network Segmentation Assessment** (if applicable)
- Assess AWS VPC segmentation (VPCs, subnets, security groups, NACLs)
- Assess Azure VNet segmentation (VNets, subnets, NSGs, ASGs)
- Assess GCP VPC segmentation (VPCs, subnets, firewall rules)
- Verify cloud-to-on-premise segmentation (hybrid)

### 6.3 Compliance Scoring (A.8.22)

**Overall A.8.22 Compliance Score** = (# compliant requirements / # total applicable requirements) × 100%

**Requirements Breakdown** (from S4):
- Segmentation Principles: 4 requirements
- Security Zones: 5 requirements
- VLAN Segregation: 5 requirements
- Subnet Design: 3 requirements
- Inter-Zone Traffic Controls: 5 requirements
- Microsegmentation: 2 requirements (SHOULD)
- Segmentation Testing: 4 requirements
- Flat Network Remediation: 3 requirements
- Cloud Network Segmentation: 3 requirements (if applicable)
- **Total: 34 requirements** (28 MUST, 6 SHOULD)

**Weighting**: Same as A.8.20/A.8.21 (MUST = 100% weight, SHOULD = 50% weight)

### 6.4 Evidence Collection (A.8.22)

**Required Evidence**:
- Network segmentation diagrams (security zones, trust boundaries) - **WB4**
- Security zones inventory - **WB4**
- VLAN configurations and documentation
- Firewall rulesets (inter-zone traffic policies) - **WB4**
- Inter-zone traffic matrix - **WB4**
- Segmentation effectiveness test results - **WB4**
- Traffic flow analysis (NetFlow/sFlow data)
- Penetration test reports (lateral movement testing)
- Flat network remediation plans/status

---

## 7. Unified Compliance Scoring Methodology

### 7.1 Overall Network Security Compliance

**Formula**:
```
Overall Compliance = (A.8.20 Score × 0.40) + (A.8.21 Score × 0.30) + (A.8.22 Score × 0.30)
```

**Weighting Rationale**:
- A.8.20 (40%): Foundation - network infrastructure security is most critical
- A.8.21 (30%): Services - critical but builds on A.8.20
- A.8.22 (30%): Segmentation - critical defense-in-depth but builds on A.8.20

**Example Calculation**:
- A.8.20 Score: 85%
- A.8.21 Score: 90%
- A.8.22 Score: 80%
- Overall = (85% × 0.40) + (90% × 0.30) + (80% × 0.30) = 34% + 27% + 24% = 85%

### 7.2 Compliance Thresholds

| Score Range | Status | Color | Action Required |
|-------------|--------|-------|-----------------|
| **≥ 95%** | Fully Compliant | 🟢 Green | Maintain, continuous improvement |
| **90-94%** | Substantially Compliant | 🟡 Yellow | Address minor gaps within 1 quarter |
| **80-89%** | Partially Compliant | 🟠 Orange | Remediation plan required, executive attention |
| **< 80%** | Non-Compliant | 🔴 Red | Immediate remediation, escalate to CISO/CIO |

### 7.3 Compliance by Network Segment

Compliance can also be calculated **per network segment** (zone) to identify weak areas:

```
DMZ Compliance = (DMZ devices compliance + DMZ services compliance + DMZ segmentation compliance) / 3
Internal Compliance = (Internal devices + Internal services + Internal segmentation) / 3
Management Compliance = (Management devices + Management services + Management segmentation) / 3
...
```

This identifies which zones need prioritized attention.

### 7.4 Trend Analysis

For organizations with historical assessment data, track compliance trends:

```
Trend = (Current Assessment Score - Previous Assessment Score) / Previous Assessment Score × 100%
```

**Example**:
- Previous Quarter: 80%
- Current Quarter: 85%
- Trend = (85% - 80%) / 80% × 100% = +6.25% improvement

**Dashboard Visualization**: Line chart showing compliance over time (monthly/quarterly).

---

## 8. Gap Management Framework

### 8.1 Gap Identification

Gaps are identified during assessment as requirements marked **"No"** or **"Partially Implemented"** in workbooks WB1-WB5.

**Gap Sources**:
- Device hardening gaps (WB2)
- Service security gaps (WB3)
- Segmentation gaps (WB4)
- Coverage gaps (WB5)

### 8.2 Gap Severity Classification

**Critical**:
- **Definition**: Exploitable vulnerability, immediate risk to confidentiality/integrity/availability
- **Examples**: Default credentials on internet-facing firewall, no network segmentation (flat network), critical service (DNS) unmonitored and unsecured
- **Remediation SLA**: < 1 week
- **Escalation**: Immediate escalation to CISO and CIO

**High**:
- **Definition**: Significant security weakness, high risk if exploited
- **Examples**: Wireless network using WPA2 instead of WPA3, missing DNSSEC, firewall rules allowing excessive traffic
- **Remediation SLA**: < 1 month
- **Escalation**: Report to CISO if not remediated within SLA

**Medium**:
- **Definition**: Moderate security weakness, moderate risk
- **Examples**: SNMP v2 still enabled (but not primary), missing NTP authentication, some devices not in NAC
- **Remediation SLA**: < 3 months
- **Escalation**: Track in quarterly review

**Low**:
- **Definition**: Minor security weakness, low risk or best practice
- **Examples**: Missing session timeouts on low-criticality devices, incomplete documentation, SHOULD requirements not implemented
- **Remediation SLA**: < 6 months
- **Escalation**: Track in annual review

### 8.3 Gap Prioritization

**Prioritization Factors**:
1. **Severity** (Critical > High > Medium > Low)
2. **Device/Service Criticality** (Critical assets prioritized)
3. **Exploitability** (Internet-facing > Internal)
4. **Remediation Effort** (Quick wins prioritized for morale/momentum)

**Prioritization Matrix**:

| Severity | Critical Asset | Non-Critical Asset |
|----------|----------------|---------------------|
| Critical | Priority 1 (Immediate) | Priority 2 (< 1 week) |
| High | Priority 2 (< 1 week) | Priority 3 (< 1 month) |
| Medium | Priority 3 (< 1 month) | Priority 4 (< 3 months) |
| Low | Priority 4 (< 3 months) | Priority 5 (< 6 months) |

### 8.4 Remediation Planning

**Remediation Plan Components**:
- Gap description (what is missing/non-compliant)
- Severity and priority
- Affected devices/services/segments
- Remediation action (what needs to be done)
- Responsible party (who will fix it)
- Target completion date (based on SLA)
- Estimated effort (hours/days)
- Dependencies (other work that must complete first)
- Verification method (how to confirm fixed)

**Remediation Tracking**:
- Document in **WB5: Gap Summary** tab
- Track status: Open → In Progress → Closed
- Update workbooks after remediation
- Re-assess to verify effectiveness

### 8.5 Compensating Controls

If remediation is not immediately feasible (technical constraints, business impact), **compensating controls** may be implemented:

**Compensating Control Requirements**:
- Must provide equivalent risk reduction
- Must be documented and approved (exception process - see Master Framework Section 8.2)
- Must be temporary (with defined end date)
- Must be reviewed quarterly

**Examples**:
- **Gap**: Legacy device cannot meet hardening requirement (no SSH support, only Telnet)
  - **Compensating Control**: Isolate device on management VLAN with strict firewall rules, enhanced logging and monitoring
- **Gap**: Flat network cannot be segmented immediately (major project required)
  - **Compensating Control**: Enhanced endpoint security (EDR on all systems), network anomaly detection (IDS/IPS), strict access controls

---

## 9. Evidence Collection and Documentation

### 9.1 Evidence Requirements Summary

**Per Control**:

| Control | Evidence Type | Storage Location |
|---------|---------------|------------------|
| **A.8.20** | Network topology diagrams, device inventory, device configs, hardening assessment, vulnerability scans, penetration tests, monitoring logs | WB1, WB2, file attachments |
| **A.8.21** | Services catalog, service configs, service assessments, availability reports, monitoring logs, failover tests, vulnerability scans | WB3, file attachments |
| **A.8.22** | Segmentation diagrams, zones inventory, firewall rules, inter-zone matrix, segmentation tests, traffic analysis, penetration tests | WB4, file attachments |
| **All** | Unified controls coverage, gap summary, compliance dashboard | WB5, Dashboard |

### 9.2 Evidence Organization

**Recommended Structure**:
```
Network_Security_Evidence/
├── Assessments/
│   ├── 2026-Q1/
│   │   ├── WB1_Infrastructure_Inventory_2026Q1.xlsx
│   │   ├── WB2_Device_Security_2026Q1.xlsx
│   │   ├── WB3_Services_Catalog_2026Q1.xlsx
│   │   ├── WB4_Segmentation_Matrix_2026Q1.xlsx
│   │   ├── WB5_Controls_Coverage_2026Q1.xlsx
│   │   └── Dashboard_Network_Security_2026Q1.xlsx
│   ├── 2026-Q2/
│   └── ...
├── Network_Diagrams/
│   ├── Logical_Topology_v2.5.pdf
│   ├── Physical_Topology_v2.5.pdf
│   ├── Security_Zones_v2.5.pdf
│   └── ...
├── Device_Configurations/
│   ├── Firewalls/
│   ├── Routers/
│   ├── Switches/
│   └── ...
├── Service_Configurations/
│   ├── DNS/
│   ├── DHCP/
│   ├── Proxy/
│   └── ...
├── Vulnerability_Scans/
│   ├── Network_Devices_Scan_2026-01.pdf
│   └── ...
├── Penetration_Tests/
│   ├── Network_Pentest_2025_Annual.pdf
│   └── ...
├── Logs_Samples/
│   ├── Firewall_Logs_Sample_2026-01.log
│   ├── DNS_Logs_Sample_2026-01.log
│   └── ...
└── Remediation_Plans/
    ├── Gap_Remediation_Plan_2026Q1.xlsx
    └── ...
```

### 9.3 Evidence Retention

**Retention Policy**:
- **Current Assessment**: Keep indefinitely (or until superseded by next assessment)
- **Historical Assessments**: Keep for 3 years (for trend analysis and audit trail)
- **Configurations**: Keep current + previous 2 versions
- **Logs**: Per logging policy (ISMS-POL-A.8.15) - typically 1 year minimum
- **Vulnerability Scans**: Keep for 1 year (for trend analysis)
- **Penetration Tests**: Keep for 3 years

### 9.4 Evidence Security

**Confidentiality**:
- Network topology diagrams, device configurations, firewall rules are **Confidential**
- Restrict access to authorized personnel only (network operations, security operations, auditors)
- Redact sensitive information (passwords, cryptographic keys) from configurations before archiving

**Integrity**:
- Store evidence in version-controlled repository (Git, SharePoint with version control)
- Generate checksums/hashes for critical evidence files
- Maintain audit trail of evidence access and modifications

**Availability**:
- Backup evidence repository
- Ensure evidence is accessible during audit cycles
- Maintain evidence index for quick retrieval

---

## 10. Assessment Tools and Automation

### 10.1 Assessment Workbook Generation Scripts

**Purpose**: Automate generation of Excel workbooks for consistent, repeatable assessments.

**Scripts**:
1. **`generate_network_1_infrastructure_inventory.py`** → WB1: Network Infrastructure Inventory
2. **`generate_network_2_device_security_assessment.py`** → WB2: Network Device Security Assessment
3. **`generate_network_3_services_catalog.py`** → WB3: Network Services Catalog
4. **`generate_network_4_segmentation_matrix.py`** → WB4: Network Segmentation Matrix
5. **`generate_network_5_controls_coverage.py`** → WB5: Security Controls Coverage
6. **`generate_network_dashboard.py`** → Dashboard: Network Security Compliance Overview
7. **`normalize_network_assessment_data.py`** → Data validation and normalization utility

**Script Capabilities**:
- Generate structured Excel workbooks with pre-defined sheets, headers, formulas
- Import data from network discovery tools (nmap XML, SNMP walks, cloud APIs)
- Auto-populate device types, service types, security zones
- Calculate compliance scores automatically
- Generate charts and visualizations
- Validate data formats (IP addresses, VLAN IDs, subnet CIDR)
- Flag missing or inconsistent data

### 10.2 Discovery and Assessment Tools

**Network Discovery**:
- **nmap**: Network scanning and service detection
- **Nessus / Qualys**: Vulnerability scanning and asset discovery
- **SNMP tools**: SNMPwalk, commercial SNMP management tools
- **NetFlow/sFlow collectors**: SolarWinds, PRTG, open-source collectors
- **Cloud CLIs**: AWS CLI (boto3), Azure CLI, GCP SDK

**Configuration Management**:
- **Ansible / Puppet / Chef**: Configuration automation and compliance checking
- **NAPALM**: Network Automation and Programmability Abstraction Layer (Python library)
- **Vendor-specific tools**: Cisco DNA Center, Juniper Junos Space, Palo Alto Panorama

**Compliance Scanning**:
- **Nessus Policy Compliance**: Network device configuration auditing
- **Nipper**: Configuration analysis for routers, switches, firewalls
- **OpenSCAP**: Security compliance scanning (where applicable)

**Traffic Analysis**:
- **Wireshark / tcpdump**: Packet capture and analysis
- **NetFlow/sFlow analyzers**: Traffic flow analysis
- **SIEM**: Splunk, ELK Stack, commercial SIEM platforms (log analysis)

**Penetration Testing**:
- **Metasploit**: Exploitation framework
- **nmap NSE scripts**: Network service testing
- **Custom scripts**: Segmentation testing, VLAN hopping, lateral movement simulation

### 10.3 Integration with Other ISMS Tools

**SIEM Integration** (A.8.16):
- Network device logs → SIEM (real-time analysis)
- Network service logs → SIEM
- Compliance alerts → SIEM dashboards

**Vulnerability Management Integration** (A.8.8):
- Network device vulnerability scans → vulnerability management system
- Remediation tracking → vulnerability management system
- Patch status → vulnerability management system

**CMDB Integration**:
- Network asset inventory → CMDB (asset management)
- Network device lifecycle data ← CMDB
- Ownership and responsibility data ← CMDB

---

## 11. Continuous Assessment and Monitoring

### 11.1 Continuous Monitoring Approach

**Real-Time Monitoring**:
- Network device log analysis (SIEM)
- Network traffic anomaly detection (IDS/IPS, NetFlow analysis)
- Configuration drift detection (compare running config to baseline)
- Service availability monitoring (uptime, performance)

**Automated Compliance Checking**:
- Daily/weekly configuration compliance scans (Ansible, Puppet, commercial tools)
- Continuous vulnerability scanning (Nessus, Qualys continuous monitoring)
- Automated policy compliance checks (firewall rule reviews, VLAN configurations)

**Dashboard Updates**:
- Monthly dashboard refresh (or more frequently for real-time dashboards)
- Compliance trend visualization
- Gap remediation progress tracking

### 11.2 Continuous Improvement

**Quarterly Review Cycle**:
1. Execute quarterly assessment (targeted)
2. Update workbooks (WB1-WB5)
3. Refresh dashboard
4. Review with CISO and Network Operations Manager
5. Adjust priorities based on new risks or business changes

**Annual Review Cycle**:
1. Execute annual assessment (comprehensive, full re-discovery)
2. Compare to previous year (trend analysis)
3. Update baselines and requirements (if needed)
4. Present to executive management
5. Plan major improvements for next year

**Lessons Learned**:
- After security incidents: What network security gaps contributed? How to prevent recurrence?
- After assessments: What worked well? What didn't? How to improve assessment process?
- After remediation: Were timelines realistic? Were resources adequate?

---

## 12. Reporting and Communication

### 12.1 Assessment Reporting

**Audience**: CISO, CIO, Network Operations Manager, Security Operations Manager, Executive Management, Auditors

**Report Contents**:
1. **Executive Summary**:
   - Overall network security compliance (single percentage)
   - Compliance per control (A.8.20, A.8.21, A.8.22)
   - Top 5 critical gaps
   - Remediation status summary
   - Trend (if historical data available)

2. **Detailed Findings**:
   - Compliance by network segment (DMZ, Internal, Management, etc.)
   - Gap analysis (severity, priority, affected assets)
   - Remediation plans and timelines
   - Evidence summary

3. **Recommendations**:
   - Prioritized remediation actions
   - Quick wins (low effort, high impact)
   - Strategic improvements (major projects)
   - Resource requirements

**Report Formats**:
- **Executive Dashboard** (Excel): For management review, high-level overview
- **Detailed Workbooks** (Excel): For technical teams, gap remediation
- **PowerPoint Presentation**: For executive briefings, board meetings
- **Formal Report** (PDF/Word): For auditors, compliance evidence

### 12.2 Stakeholder Communication

**Monthly**: 
- Email update to CISO with compliance status and critical gap status
- Dashboard refresh and distribution to Network Operations, Security Operations

**Quarterly**:
- Formal assessment report to CISO, CIO, Executive Management
- Presentation to security steering committee (if exists)
- Review with network operations and security operations teams

**Annually**:
- Comprehensive assessment report to executive management
- Board presentation (if applicable)
- Audit evidence package preparation

**Ad-Hoc** (Triggered Events):
- After major network changes (architecture redesign, cloud migration): Triggered assessment report
- After security incidents: Incident post-mortem with network security component analysis
- Audit requests: Evidence package delivery to auditors

---

## 13. Integration with Audit Processes

### 13.1 Internal Audit Support

**Internal Audit Objectives**:
- Verify network security controls are implemented as documented
- Assess effectiveness of network security controls
- Identify gaps and recommend improvements

**Assessment Framework Support for Internal Audit**:
- Workbooks WB1-WB5 provide structured evidence
- Dashboard provides compliance overview
- Gap summaries identify areas for audit focus
- Evidence repository provides audit trail

**Internal Audit Frequency**: Typically annual or semi-annual (per ISMS internal audit schedule)

### 13.2 External Audit / Certification Audit Support

**External Audit Objectives**:
- Verify ISO 27001:2022 Controls A.8.20, A.8.21, A.8.22 are implemented
- Assess compliance with Statement of Applicability (SoA)
- Verify continuous improvement

**Assessment Framework Support for External Audit**:
- Master Framework and S1-S4 demonstrate policy compliance
- Workbooks WB1-WB5 demonstrate implementation evidence
- Dashboard demonstrates ongoing assessment and monitoring
- Gap remediation tracking demonstrates continuous improvement

**Audit Evidence Package**:
1. Policy documents (Master Framework, S1-S5)
2. Most recent assessment workbooks (WB1-WB5)
3. Dashboard showing compliance trends
4. Sample evidence (network diagrams, configurations, logs)
5. Gap remediation plans and status
6. Exception register (if applicable)

**Audit Frequency**: Typically annual (ISO 27001 surveillance audit) or tri-annual (re-certification audit)

### 13.3 Regulatory Compliance Audit Support

For organizations subject to specific regulations (financial services, healthcare, critical infrastructure):

**Regulatory Audit Objectives**:
- Verify compliance with industry-specific network security requirements
- Assess adequacy of network controls for regulatory compliance

**Examples**:
- **PCI-DSS**: Network segmentation (Requirement 1), cardholder data environment isolation
- **HIPAA**: Network security for ePHI transmission, encryption, access controls
- **NIS2 / DORA**: Network resilience, incident response, supply chain security

**Assessment Framework Adaptation**:
- Map regulatory requirements to A.8.20/8.21/8.22 framework
- Add regulatory-specific requirements to workbooks (if needed)
- Generate regulatory compliance reports from dashboard data

---

## 14. Conclusion

This Assessment Methodology & Evidence Framework provides a **comprehensive, systematic, and auditable approach** to evaluating network security compliance with ISO 27001:2022 Controls A.8.20, A.8.21, and A.8.22.

**Key Features**:
1. ✅ **Systems Engineering Approach**: Discovery → Documentation → Evaluation → Remediation
2. ✅ **Unified Assessment**: Single framework covers all three controls efficiently
3. ✅ **Automation-First**: Python-generated workbooks ensure consistency
4. ✅ **Evidence-Based**: Objective verification, clear audit trail
5. ✅ **Continuous Improvement**: Quarterly/annual cycles + continuous monitoring
6. ✅ **Audit-Ready**: Structured evidence for internal, external, and regulatory audits
7. ✅ **Gap Management**: Systematic identification, prioritization, and remediation

**Success Metrics**:
- **100% network visibility**: All devices, services, segments inventoried
- **≥ 95% compliance**: Across all three controls (A.8.20, A.8.21, A.8.22)
- **Zero critical gaps**: All critical gaps remediated within SLA (< 1 week)
- **Positive trend**: Compliance improving or maintained quarter-over-quarter
- **Audit success**: Pass internal, external, and regulatory audits on first attempt

**Next Steps**:
1. Review and approve this assessment framework
2. Develop Python scripts for workbook generation (Phase 3 of implementation roadmap)
3. Execute pilot assessment on selected network segment
4. Refine framework based on pilot results
5. Execute full network-wide assessment

---

**END OF SECTION 5 (ASSESSMENT METHODOLOGY & EVIDENCE FRAMEWORK)**

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / CISO | Initial assessment methodology framework |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

**Next Document**: ISMS-POL-A.8.20-21-22-S6 (Network Security Architecture Guidance) [Optional]
