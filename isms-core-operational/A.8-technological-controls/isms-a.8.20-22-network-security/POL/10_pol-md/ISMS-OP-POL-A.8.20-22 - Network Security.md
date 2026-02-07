**ISMS-OP-POL-A.8.20-22 — Network Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Network Security |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.20-22 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Controls A.8.20, A.8.21, A.8.22 — Network security, security of network services, segregation of networks

**Related Annex A Controls**:

| Control | Relationship to Network Security |
|---------|----------------------------------|
| A.5.14 Information transfer | Encryption and secure channel requirements for data in transit |
| A.5.15 Access control | Network access control aligned with identity and access policy |
| A.5.23 Information security for cloud services | Cloud network connectivity and segmentation |
| A.8.1 User endpoint devices | Endpoint compliance before network admission |
| A.8.5 Secure authentication | Authentication for network access (802.1X, VPN) |
| A.8.9 Configuration management | Network device configuration baselines and hardening |
| A.8.15 Logging | Network event and traffic logging |
| A.8.16 Monitoring activities | Network monitoring, IDS/IPS, anomaly detection |
| A.8.23 Web filtering | URL/DNS filtering as network-layer control |
| A.8.24 Use of cryptography | TLS/IPsec for encrypted network transport |

**Related Internal Policies**:

- Access Control Policy
- Use of Cryptography Policy
- Information Transfer Policy
- Physical and Environmental Security Policy
- Asset Management Policy
- Logging and Monitoring Policy

---

# Network Security Management Policy

## Purpose

The purpose of this policy is to ensure the protection of information in networks and its supporting information processing facilities.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) through network security controls. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All organisation networks, network services, network administration and management solutions, and network devices deemed in scope by the ISO 27001 scope statement.

## Principle

The network is managed on the principle of least privilege with security by design and default. Network access is denied by default and granted only with documented approval. All network architecture decisions shall be risk-based, considering the classification of information and the criticality of systems.

---

## Network Controls

- Responsibilities and procedures for the management of networking equipment shall be established and documented.
- Operational responsibility for networks shall be separated from computer operations where appropriate.
- Special controls shall be established to safeguard the confidentiality and integrity of data passing over public networks or over wireless networks and to protect the connected systems and applications.
- Appropriate logging and monitoring shall be applied to enable recording and detection of actions that may affect, or are relevant to, information security.
- Management activities shall be closely coordinated both to optimise the service to the organisation and to ensure that controls are consistently applied across the information processing infrastructure.
- Systems on the network shall be authenticated before being granted access.
- System connections to the network shall be restricted to authorised and compliant devices.
- Network device default passwords and accounts shall be changed or disabled before deployment.
- Administrative access to network devices shall use encrypted management protocols (SSH, HTTPS). Telnet and unencrypted SNMP (v1/v2c) shall not be used.
- Network device firmware and software shall be maintained at current, vendor-supported versions. Security patches shall be applied according to the following timelines:

| Severity | Timeframe |
|----------|-----------|
| Critical vulnerabilities (CVSS 9.0+, active exploitation) | Within 14 days |
| High vulnerabilities (CVSS 7.0–8.9) | Within 30 days |
| Medium vulnerabilities (CVSS 4.0–6.9) | Within 90 days |
| Low vulnerabilities (CVSS 0.1–3.9) | Next scheduled maintenance window |

Emergency patches for actively exploited vulnerabilities may be deployed without non-production testing with CISO approval and documented risk acceptance.

## Security of Network Services

Security mechanisms, service levels, and management requirements of all network services shall be identified and included in network services agreements, whether these services are provided in-house or outsourced.

The ability of the network service provider to manage agreed services in a secure way shall be determined and regularly monitored, and the right to audit shall be agreed.

The security arrangements necessary for particular services, such as security features, service levels, and management requirements, shall be identified. The organisation shall ensure that network service providers implement these measures.

Network services include but are not limited to:

- DNS, DHCP, and NTP services.
- Email, file sharing, and web application services.
- Firewall, intrusion detection/prevention, and gateway security services.
- Remote access and VPN services.

## Segregation in Networks

Large networks shall be divided into separate network domains. The domains shall be chosen based on trust levels, data classification, and business function.

Segregation may be achieved using physically different networks or by using different logical networks (e.g., VLANs, software-defined networking).

The perimeter of each domain shall be well defined. Access between network domains shall be controlled at the perimeter using a gateway (e.g., firewall, filtering router) with a default-deny posture.

The criteria for segregation of networks into domains, and the access allowed through the gateways, shall be based on an assessment of the security requirements of each domain. The assessment shall be in accordance with the access control policy, access requirements, value and classification of information processed, and shall take account of the relative cost and performance impact of incorporating suitable gateway technology.

**Firewall rule governance:**

- All firewall rule changes shall follow a documented change management process with business justification and approval.
- Firewall rule sets shall be reviewed at least **annually** to remove obsolete rules and verify continued business justification.
- Reviews shall be documented with sign-off from the network administrator and CISO.
- Default-deny policy shall be verified during each review (all traffic blocked unless explicitly permitted).

Minimum network segments shall include:

| Segment | Purpose |
|---------|---------|
| Corporate / user network | Standard employee workstations and devices |
| Server / application network | Business applications and databases |
| Management network | Network device administration (out-of-band where feasible) |
| Guest network | Visitor and non-corporate device access (isolated from corporate) |
| IoT / OT network | Internet of Things and operational technology devices (isolated) |

Additional segments (e.g., DMZ for public-facing services, development/test environments) shall be created based on risk assessment.

### Guest Network Requirements

Guest networks shall be configured with the following security controls:

- **Isolation**: No access to corporate network segments (firewall rules shall enforce separation).
- **Internet-only access**: Guests shall access only the Internet, not internal resources.
- **Encryption**: WPA2-Personal minimum with a strong passphrase, or WPA2-Enterprise with guest credentials.
- **Time-limited access**: Guest credentials shall expire after a defined period (e.g., 24 hours) and be reissued as needed.
- **Monitoring**: Guest network traffic shall be logged for security investigation if needed.

The guest network passphrase shall be changed at least **quarterly** or immediately if compromise is suspected.

### IoT and OT Device Security

IoT (Internet of Things) and OT (Operational Technology) devices shall be placed on an isolated network segment with the following controls:

- IoT/OT devices shall not have direct, uncontrolled Internet access. Internet communication shall be routed via a proxy or gateway with whitelisted destinations.
- IoT/OT devices shall not be accessible from the Internet without VPN and explicit authorisation.
- Access from the corporate network to the IoT/OT segment shall be restricted to authorised personnel via firewall rules.
- Third-party vendor remote access to IoT/OT devices shall require approval, VPN, and time-limited credentials.
- All IoT/OT device default passwords shall be changed before deployment.
- All IoT/OT devices shall be registered in the asset register with owner, purpose, and network location.

### Wireless Network Segregation

Wireless networks require special treatment due to the poorly defined network perimeter. For sensitive environments, all wireless access shall be treated as external connections and segregated from internal networks until the access has passed through a gateway before granting access to internal systems.

Wireless network access for personnel and guests shall be segregated on separate SSIDs with distinct security controls.

### Wireless Security Standards

The following wireless security standards shall apply:

- WPA3 is preferred for all wireless networks.
- WPA2 Enterprise mode with 802.1X authentication and AES encryption is the minimum acceptable standard for corporate networks.
- WPA2 Personal mode may be used for non-production networks (e.g., guest access) with a minimum 16-character random passphrase and AES encryption.
- WEP shall not be used under any circumstances.
- WPA (original) and TKIP encryption shall not be used.

## Access to Networks and Network Services

Users shall only be provided with access to the network and network services that they have been specifically authorised to use.

Access to networks and network services shall be in line with the Access Control Policy.

Before connecting to the network, devices shall have:

- Been registered in the asset register.
- Been patched to the latest security patch levels.
- Appropriate malware protection installed and current.
- Default passwords and accounts changed or disabled.
- Been included where possible in the network management and monitoring system.
- Ports, services, applications, and guest accounts removed or disabled that are not required.

The organisation shall implement technical controls to enforce device compliance before granting network access. Enforcement mechanisms include network access control (NAC) solutions, 802.1X certificate or credential-based authentication, VPN gateway posture assessment, or manual registration and approval by IT. Non-compliant devices shall be placed in a quarantine or restricted segment until compliance is achieved.

## Remote Access

Remote access to the organisation network shall be secured using encrypted tunnels (VPN or equivalent) with multi-factor authentication.

VPN connections shall use current, secure protocols:

- WireGuard or IKEv2/IPsec are preferred.
- OpenVPN is acceptable where WireGuard or IKEv2 are not supported.
- PPTP and L2TP without IPsec shall not be used.

Remote connections shall be set to disconnect after a defined period of inactivity.

A list of users with remote access shall be maintained and reviewed quarterly.

Split tunnelling (allowing some traffic to bypass the VPN) may be permitted only when:

- A documented risk assessment demonstrates acceptable residual risk.
- All organisation resources (file shares, databases, applications, email) are accessed only via the encrypted tunnel.
- Split-tunnelled traffic is limited to non-sensitive, Internet-only destinations.
- The user's endpoint meets all security baseline requirements (current patches, antivirus/EDR, encryption).
- Split tunnelling is disabled for privileged and administrator accounts.

## Network Locations

Network infrastructure and data processing locations shall be selected based on risk assessment, data classification, and applicable data protection requirements.

The following hierarchy of preference shall apply for the location of network infrastructure, data centres, and cloud services processing personal or confidential data:

1. Within Switzerland.
2. Within countries recognised by the Swiss Federal Council as providing adequate data protection per **Annex 1 of the Data Protection Ordinance (DSV)**. The current adequacy list is published by the Federal Data Protection and Information Commissioner (FDPIC) and shall be verified before deploying infrastructure or services in a new jurisdiction.
3. Within countries where Standard Contractual Clauses (SCCs) or other appropriate safeguards under nFADP Art. 16–17 are in place.

Cross-border data transfers shall comply with the Information Transfer Policy and nFADP requirements. Legal counsel shall verify the adequacy status of any country before deployment.

## Physical Network Devices

Physical network devices shall be managed in line with the Physical and Environmental Security Policy, specifically the sections on cabling security, equipment siting and protection, and access control.

Physical network devices shall be destroyed in line with the Information Classification and Handling Policy, specifically the section on the destruction of electronic media and devices.

Physical network devices shall be managed in line with the Asset Management Policy and subject to the asset management process.

## Web Filtering

Access to websites containing illegal information or known to contain malicious content shall be restricted.

Access to the following types of websites shall be blocked where practicable:

- Websites with an information upload function, unless permitted for valid business reasons.
- Known or suspected malicious websites (phishing, malware distribution).
- Command and control servers.
- Malicious websites identified in threat intelligence feeds.
- Websites sharing illegal content.
- Proxy and anonymiser services (unless required for approved business purposes).

Web filtering shall be implemented using DNS-based filtering, web proxy, or equivalent technology. Filter categories and exceptions shall be reviewed quarterly.

### DNS Security

- DNS resolvers should validate DNSSEC signatures where available to protect against DNS spoofing.
- Internal DNS zones shall not be exposed to the Internet. Split-horizon DNS is recommended for organisations with internal and external name resolution.
- DNS queries should be logged for security investigation and threat detection.

## Host Intrusion, Network Intrusion, Malware, and Antivirus

Network services and devices shall be managed in line with the Malware and Antivirus Policy.

Host intrusion detection and network intrusion detection/prevention shall be deployed based on risk, business need, and where practical to do so.

**Minimum IDS/IPS deployment locations:**

| Location | Type | Purpose |
|----------|------|---------|
| Internet perimeter (firewall/gateway) | Network IDS/IPS | Detect/prevent external attacks and malicious inbound traffic |
| Between network segments (inter-VLAN) | Network IDS/IPS | Detect lateral movement between trust zones |
| Server/application network | Network IDS or host-based IDS | Detect anomalous access to critical systems |
| Endpoints (workstations, servers) | Host-based IDS (EDR/XDR) | Detect endpoint-level threats, fileless malware, suspicious processes |
| Cloud workloads (IaaS/PaaS) | Cloud-native IDS or CASB | Detect threats targeting cloud infrastructure |

Additional deployment locations shall be determined by risk assessment. Where dedicated IDS/IPS appliances are not feasible, equivalent detection capabilities (e.g., EDR with network visibility, cloud-native security tools) are acceptable.

Network traffic shall be monitored for anomalous behaviour. Security alerts shall be triaged and escalated per the Incident Management process.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **Network architecture diagram** (current, showing segments, trust zones, gateways) — *updated upon change; reviewed annually*
- **Firewall and gateway rule sets** with documented change history and annual review sign-off — *rule changes retained for 3 years; annual review documented with CISO sign-off*
- **Network device inventory and configuration baselines** — *updated within 5 business days of change; audited annually*
- **Wireless security configuration records** (WPA3/WPA2-Enterprise) — *reviewed semi-annually*
- **VPN access list and quarterly review records** — *reviewed quarterly; inactive accounts disabled*
- **Web filtering configuration and exception logs** — *exceptions reviewed quarterly; filter categories updated monthly*
- **Network monitoring and IDS/IPS alert reports** — *retained for 12 months minimum; critical alerts reviewed daily*
- **Network access review and device compliance records** — *reviewed quarterly for privileged access; annually for standard*
- **Patching compliance reports** (network devices per CVSS timeline table) — *reviewed monthly*
- **Guest network passphrase rotation records** — *quarterly rotation documented*

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, network configuration audits, penetration testing, vulnerability scanning, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to network security standards, emerging threats, regulatory changes, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Network Security Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.20 Network security** |
| | **8.21 Security of network services** |
| | **8.22 Segregation of networks** |
| | 8.23 Web filtering |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security; Annex 1 — Adequacy list |
| EU GDPR (where applicable) | Art. 32 — Security of processing (network controls as appropriate measure) |
| ISO/IEC 27001:2022 | Annex A Controls 8.20, 8.21, 8.22 |
| ISO/IEC 27002:2022 | Sections 8.20, 8.21, 8.22 — Implementation guidance |
| NIST SP 800-53 Rev 5 | SC-7 (Boundary Protection), SC-8 (Transmission Confidentiality) |
| CIS Controls v8 | Control 12 (Network Infrastructure Management), Control 13 (Network Monitoring and Defense) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
