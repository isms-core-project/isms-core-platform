# ISMS-POL-A.8.16-S1
## Monitoring Activities - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.8.16-S1
**Title**: Monitoring Activities - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | Information Security Manager | Initial foundational document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Operations Center (SOC) Lead
- Compliance Review: Legal/Compliance Officer

**Distribution**: Security team, SOC analysts, system owners, IT operations, network team  
**Related Documents**: ISMS-POL-A.8.16 (Master), ISO/IEC 27001:2022 A.8.16, ISO/IEC 27002:2022 Section 8.16

---

## 1.1 Purpose

### 1.1.1 Policy Objective

This document establishes the purpose, scope, and key definitions for the organization's Monitoring Activities policy framework, implementing ISO/IEC 27001:2022 Annex A Control 8.16 (Monitoring Activities).

The policy framework aims to:

- **Detect** anomalous behavior in networks, systems, and applications that may indicate information security incidents
- **Establish** measurable baselines for normal behavior across all monitored assets
- **Respond** to security events and deviations from established baselines in a timely and effective manner
- **Integrate** monitoring outputs with incident response and threat intelligence processes
- **Comply** with legal, regulatory, and contractual obligations regarding security monitoring and incident detection
- **Support** continuous improvement of security posture through trend analysis and lessons learned

### 1.1.2 Control Alignment

This policy implements ISO/IEC 27001:2022 Annex A.8.16:

> **A.8.16 Monitoring Activities**  
> *Networks, systems and applications shall be monitored for anomalous behaviour and appropriate actions taken to evaluate potential information security incidents.*

The control recognizes that **detection is as critical as prevention**. No security control is perfect, and monitoring serves as the essential detective layer that identifies:
- Security incidents that bypassed preventive controls
- Insider threats and unauthorized activities
- Misconfigurations that create security exposures
- Policy violations requiring corrective action
- Attack patterns requiring defensive adjustments
- Compliance deviations requiring remediation

**Control Type**: #Detective #Corrective  
**Information Security Properties**: #Confidentiality #Integrity #Availability  
**Cybersecurity Concepts**: #Detect #Respond  
**Operational Capabilities**: #Information_Security_Incident_Handling  
**Security Domains**: #Defense

### 1.1.3 Risk Management Context

Monitoring activities serve as a **detective control** within the organization's layered security architecture. While preventive controls reduce the likelihood of security incidents, monitoring provides the critical capability to detect incidents that do occur.

**Without monitoring, the organization operates blind:**
- Incidents go undetected until significant damage occurs
- Attack dwell time increases, allowing adversaries more time to achieve objectives
- Root cause analysis becomes impossible without forensic evidence
- Compliance violations go unnoticed until external audit or breach
- Insider threats operate undetected
- System compromises remain hidden

**With effective monitoring, the organization gains:**
- Early warning of security incidents (reduced mean time to detect - MTTD)
- Evidence-based incident response (logs, baselines, alerts)
- Visibility into attack patterns and threat actor behaviors
- Compliance evidence demonstrating due diligence
- Ability to measure security control effectiveness
- Foundation for continuous security improvement

### 1.1.4 The Feynman Principle Applied to Monitoring

As Richard Feynman famously said: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*

**Applied to Control 8.16:**
- If you cannot explain what "normal behavior" looks like with measurable metrics, you do not have a baseline—you have a guess
- If you cannot explain why an alert fires, you cannot tune it—you have noise, not signal
- If you cannot explain what monitoring tool X actually monitors, you have cargo cult security—the appearance of monitoring without the substance

**Cargo Cult Monitoring Warning Signs:**
- ✅ "We have a SIEM!" (but no one reads the dashboards)
- ✅ "We get alerts!" (but everyone ignores them because of false positives)
- ✅ "We monitor everything!" (but have no documented baselines or thresholds)
- ✅ "Our monitoring is compliant!" (but cannot demonstrate detection effectiveness)

This policy framework prevents cargo cult monitoring by requiring:
- **Documented baselines** - Not opinions, but measured behavioral patterns
- **Measurable thresholds** - Not "looks suspicious," but "exceeds X by Y%"
- **Evidenced responses** - Not "we'll investigate," but "incident tickets created within Z minutes"
- **Regular validation** - Not "it's working," but "tested monthly with detection rate >N%"

---

## 1.2 Scope

### 1.2.1 In Scope

This policy framework applies to:

**Network Segments**:
- On-premises local area networks (LANs)
- Wide area networks (WANs) and inter-site connectivity
- Wireless networks (corporate WLANs, guest networks)
- Remote access infrastructure (VPN, RDP, SSH)
- Cloud network environments (VPC, virtual networks)
- Branch office networks
- Partner/extranet connections
- DMZ and perimeter networks
- IoT and OT networks (where technically feasible)

**Systems**:
- All production servers (physical, virtual, cloud-based)
- Database systems (production, staging)
- Application servers (web, API, middleware)
- Network infrastructure devices (routers, switches, firewalls, load balancers)
- Security appliances (SIEM, IDS/IPS, proxy, web filters, DLP)
- Endpoint systems (workstations, laptops, mobile devices - where technically feasible)
- Cloud infrastructure (IaaS, PaaS control planes)
- Directory services (Active Directory, LDAP, identity providers)
- Backup and disaster recovery systems

**Applications**:
- Business-critical applications (ERP, CRM, financial systems, etc.)
- Customer-facing applications (web portals, mobile apps, APIs)
- Security-sensitive applications (privileged access management, secrets vaults, etc.)
- Collaboration and productivity applications (email, file sharing, document management)
- Development and deployment platforms (CI/CD, source code repositories)

**Users and Entities**:
- All employees (full-time, part-time, temporary)
- Contractors and third-party personnel with system access
- Service accounts and non-human identities
- Privileged users (administrators, operators)
- Automated systems and API integrations

**Monitoring Data Sources**:
- Event logs (operating systems, applications, databases)
- Network traffic (flow data, packet captures where appropriate)
- Authentication and authorization events (logins, access attempts, privilege escalations)
- Configuration changes (system, application, security control)
- File integrity events (creation, modification, deletion of critical files)
- Resource utilization metrics (CPU, memory, disk, network)
- Security tool outputs (antivirus alerts, IDS signatures, vulnerability scanner findings)
- Cloud platform logs (AWS CloudTrail, Azure Monitor, GCP Cloud Logging)

### 1.2.2 Out of Scope

The following are explicitly excluded from this policy (covered under separate policies/controls):

- **Log generation and retention** (covered under ISMS-POL-A.8.15 - Logging)
- **Incident response procedures** (covered under ISMS-POL-A.5.24-28 - Incident Management)
- **Threat intelligence collection** (covered under ISMS-POL-A.5.7 - Threat Intelligence)
- **Vulnerability scanning and assessment** (covered under ISMS-POL-A.8.8 - Vulnerability Management)
- **Physical security monitoring** (covered under physical security policies)
- **Business continuity monitoring** (covered under BC/DR policies)
- **Performance monitoring** for non-security purposes (covered under IT operations policies)
- **Personal devices** (BYOD) not managed by the organization, unless accessing corporate resources through monitored channels

**NOTE**: While these topics are out of scope for THIS policy, monitoring activities often consume data from and integrate with these related controls. Integration points are documented in Section 1.4.2.

### 1.2.3 Geographic and Regulatory Scope

This policy applies to:
- All organizational locations worldwide
- All cloud regions where organizational data is processed
- All users regardless of physical location when accessing organizational resources
- All applicable legal and regulatory jurisdictions

Where local data protection regulations (e.g., GDPR, FADP, regional privacy laws) impose specific requirements or restrictions on logging, those requirements shall be documented and implemented as policy extensions.

**Key Regional Considerations**:
- **European Union**: GDPR Article 32(1)(d) requirements for logging in data processing
- **Switzerland**: FADP Article 8 security obligations including audit trails
- **Switzerland (Financial Sector)**: FINMA Circular 2023/1 Margin 63-72 logging requirements
- **United States**: State breach notification laws requiring log evidence
- **Sector-Specific**: DORA, NIS2, PCI DSS, HIPAA where applicable

Refer to **ISMS-POL-00 (Regulatory Applicability Framework)** for authoritative interpretation of regulatory requirements.

### 1.2.4 Technology Neutrality

This policy framework is **vendor-agnostic** and **technology-independent**. Requirements are expressed in terms of capabilities and outcomes rather than specific products or implementation methods.

Organizations implementing this policy may choose any technology solution(s) that satisfy the stated requirements. Technology selection should be based on:
- Fit with organizational architecture and existing infrastructure
- Capability to meet monitoring requirements (baseline establishment, anomaly detection, alerting)
- Integration with existing security controls (SIEM, SOAR, ticketing systems)
- Total cost of ownership (licensing, staffing, training, maintenance)
- Vendor support and product maturity
- Scalability and performance requirements
- Log source coverage and parsing capabilities

**Examples of monitoring technologies** (non-exhaustive):
- Security Information and Event Management (SIEM)
- Intrusion Detection/Prevention Systems (IDS/IPS)
- Network Detection and Response (NDR)
- Endpoint Detection and Response (EDR)
- User and Entity Behavior Analytics (UEBA)
- Security Orchestration, Automation and Response (SOAR)
- Cloud Security Posture Management (CSPM)
- Database Activity Monitoring (DAM)

---

## 1.3 Definitions

### 1.3.1 Core Monitoring Terminology

**Monitoring**  
The continuous or periodic observation and analysis of networks, systems, and applications to identify anomalous behavior, security incidents, policy violations, or operational issues requiring attention.

**Anomalous Behavior**  
Activity that deviates significantly from established baselines or expected patterns. Anomalies may indicate security incidents, misconfigurations, policy violations, or legitimate but unusual business activities requiring investigation.

**Baseline**  
A documented, measurable profile of normal behavior for a system, application, network segment, or user. Baselines are established through observation during known-good operational periods and serve as the reference point for anomaly detection. Baselines must be periodically reviewed and updated to remain accurate as business operations evolve.

**Threshold**  
A specific, quantifiable limit that, when exceeded, triggers an alert or action. Thresholds are derived from baselines (e.g., "login failures >5 within 10 minutes" or "network traffic volume >200% of baseline").

**Security Event**  
Any observable occurrence in a system or network that has relevance to security. Events are recorded in logs (e.g., "user logged in," "file modified," "network connection established").

**Security Alert**  
A notification generated when monitoring tools detect a condition that may indicate a security incident. Alerts are generated based on rules, thresholds, signatures, or anomaly detection algorithms.

**Security Incident**  
A security event or series of events that has been analyzed and determined to violate security policy, acceptable use policy, or standard security practice, or that represents an imminent threat to information assets.

**False Positive**  
An alert that triggers on legitimate, authorized activity rather than an actual security incident. High false positive rates reduce monitoring effectiveness by overwhelming analysts with noise.

**False Negative**  
A failure of monitoring systems to detect an actual security incident. False negatives are more dangerous than false positives because they allow attacks to proceed undetected.

### 1.3.2 Detection Terminology

**Signature-Based Detection**  
Monitoring approach that uses known patterns of malicious activity (signatures, rules, indicators of compromise) to identify threats. Effective against known threats but cannot detect novel attacks (zero-days).

**Anomaly-Based Detection**  
Monitoring approach that identifies deviations from established baselines of normal behavior. Can detect novel attacks but typically generates higher false positive rates requiring tuning.

**Behavior-Based Detection**  
Monitoring approach that analyzes sequences of actions or patterns of behavior to identify malicious activity. Example: Detecting lateral movement by correlating multiple network connections from the same source.

**Heuristic Detection**  
Monitoring approach using rules of thumb or algorithms to identify suspicious activity without requiring exact signatures. Example: Flagging any PowerShell execution from unusual parent processes.

**Correlation**  
The process of analyzing multiple security events from different sources to identify patterns that indicate security incidents. Example: Correlating failed login attempts with subsequent successful login from unusual location.

### 1.3.3 Monitoring Types

**Real-Time Monitoring**  
Continuous analysis of security events as they occur, with near-instant alert generation. Used for critical systems or high-severity threats requiring immediate response.

**Near-Real-Time Monitoring**  
Analysis of security events with slight delay (seconds to minutes) to allow for event aggregation and correlation. Balances timeliness with accuracy.

**Batch Monitoring**  
Periodic analysis of security events at scheduled intervals (hourly, daily). Suitable for non-critical systems or analysis requiring larger datasets (trend analysis, compliance reporting).

**Active Monitoring**  
Monitoring that actively queries or probes systems to verify their status or detect issues. Example: Sending test authentication attempts to verify login monitoring is working.

**Passive Monitoring**  
Monitoring that only observes existing traffic or events without generating additional network/system activity. Example: Network packet capture for intrusion detection.

### 1.3.4 Performance Metrics

**MTTD (Mean Time To Detect)**  
Average time from when a security incident occurs to when it is detected by monitoring systems. Lower MTTD indicates more effective monitoring.

**MTTR (Mean Time To Respond)**  
Average time from incident detection to initial response action (containment, investigation). While response is covered under incident management, monitoring capabilities (alert quality, context) significantly impact MTTR.

**Detection Rate**  
Percentage of actual security incidents successfully detected by monitoring systems. Measured through testing (red team exercises, attack simulations, injected test events).

**False Positive Rate**  
Percentage of alerts that do not represent actual security incidents. Target: <10% false positives for critical alerts, <25% for all alerts.

**Alert Volume**  
Total number of alerts generated per time period. Must be balanced—too few suggests gaps in detection, too many overwhelms analysts.

**Coverage**  
Percentage of assets, systems, or network segments actively monitored. Target: 100% of critical assets, >90% of all assets.

### 1.3.5 Roles and Entities

**Security Operations Center (SOC)**  
Team or function responsible for 24/7 monitoring of security events, alert triage, initial incident investigation, and escalation to incident response teams.

**SOC Analyst (Tier 1)**  
Personnel responsible for monitoring dashboards, triaging alerts, performing initial investigation, and escalating confirmed incidents to higher tiers or incident response.

**SOC Analyst (Tier 2/3)**  
Senior analysts responsible for complex investigations, threat hunting, monitoring tool tuning, and developing detection content (rules, signatures, correlation logic).

**Security Engineer**  
Personnel responsible for deploying, configuring, and maintaining monitoring infrastructure (SIEM, IDS/IPS, log collectors, etc.).

**System Owner**  
Person or role accountable for a system or application, including ensuring it is monitored per policy requirements and responding to monitoring alerts affecting their system.

**Threat Intelligence Analyst**  
Personnel responsible for incorporating external threat intelligence into monitoring capabilities (IOCs, TTP signatures, emerging threat patterns).

**Incident Response Team**  
Personnel responsible for investigating and remediating confirmed security incidents escalated from monitoring/SOC.

---

## 1.4 References

### 1.4.1 ISO/IEC Standards

- **ISO/IEC 27001:2022** - Information Security Management Systems - Requirements
- **ISO/IEC 27002:2022** - Information Security Controls, specifically:
  - Control 8.16: Monitoring Activities (this policy)
  - Control 8.15: Logging (data source for monitoring)
  - Control 5.24-5.28: Incident Management (consumes monitoring outputs)
  - Control 5.7: Threat Intelligence (informs monitoring)
  - Control 8.8: Management of Technical Vulnerabilities (monitoring detects exploitation)
- **ISO/IEC 27035** - Information Security Incident Management

### 1.4.2 Related Organizational Policies

This policy framework should be read in conjunction with:

- **ISMS-POL-A.8.15** - Logging Policy (monitoring analyzes logged data)
- **ISMS-POL-A.5.24-28** - Incident Management Policy (monitoring detects incidents)
- **ISMS-POL-A.5.7** - Threat Intelligence Policy (informs monitoring rules)
- **ISMS-POL-A.8.8** - Vulnerability Management Policy (monitoring detects exploitation)
- **ISMS-POL-A.8.23** - Web Filtering Policy (web filtering logs feed into monitoring)
- **Privacy Policy** - Considerations for monitoring user activity and data privacy
- **Acceptable Use Policy** - Monitoring enforces acceptable use

### 1.4.3 External References

- **NIST SP 800-92** - Guide to Computer Security Log Management
- **NIST SP 800-137** - Information Security Continuous Monitoring (ISCM)
- **NIST SP 800-61** - Computer Security Incident Handling Guide
- **CIS Controls v8**:
  - Control 8: Audit Log Management
  - Control 13: Network Monitoring and Defense
  - Control 17: Incident Response Management
- **MITRE ATT&CK Framework** - Adversary tactics and techniques (informs detection logic)
- **SANS Internet Storm Center** - Threat intelligence for monitoring
- **OWASP** - Web application attack patterns

### 1.4.4 Industry-Specific Frameworks

Where applicable to the organization's industry or regulatory environment:

- **PCI-DSS** - Payment Card Industry Data Security Standard (Requirement 10: Logging and Monitoring)
- **HIPAA** - Health Insurance Portability and Accountability Act (Security Rule § 164.308(a)(1)(ii)(D) - Information System Activity Review)
- **Financial Services Regulations** - Industry-specific requirements (FINMA, BaFin, etc.)
- **NIS2 Directive** - EU Network and Information Security Directive (for applicable organizations)
- **Swiss Financial Market Supervisory Authority (FINMA)** - For Swiss financial institutions

### 1.4.5 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this monitoring activities policy are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Mandatory Compliance:**
* Swiss Federal Data Protection Act (FADP)
* EU GDPR (where processing EU personal data)
* ISO/IEC 27001:2022 (Control A.8.16)
* [Additional mandatory regulations per ISMS-POL-00]

**Informational Reference / Best Practice Alignment:**
* NIST SP 800-92, 800-137 (Monitoring guidance)
* CIS Controls v8
* MITRE ATT&CK Framework
* [Other frameworks per ISMS-POL-00]

**United States Federal Requirements:**
References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where the organization has explicit US federal contractual obligations, as defined in **ISMS-POL-00**.

For complete regulatory categorization and applicability criteria, refer to **ISMS-POL-00 - Regulatory Applicability Framework**.

---

## 1.5 Policy Framework Structure

This document (S1) is part of a modular policy framework for Monitoring Activities. The complete framework consists of:

**ISMS-POL-A.8.16-S1** - Purpose, Scope, Definitions (this document)  
**ISMS-POL-A.8.16-S2** - Requirements Overview  
**ISMS-POL-A.8.16-S2.1** - Monitoring Infrastructure Requirements  
**ISMS-POL-A.8.16-S2.2** - Baseline & Anomaly Detection Requirements  
**ISMS-POL-A.8.16-S2.3** - Alert Management & Response Requirements  
**ISMS-POL-A.8.16-S2.4** - Retention & Archival Requirements  
**ISMS-POL-A.8.16-S3** - Roles and Responsibilities  
**ISMS-POL-A.8.16-S4** - Policy Governance  
**ISMS-POL-A.8.16-S5** - Annexes  
**ISMS-POL-A.8.16-S5.A** - Monitoring Capability Standards  
**ISMS-POL-A.8.16-S5.B** - Baseline Definition Template  
**ISMS-POL-A.8.16-S5.C** - Alert Response Procedures  
**ISMS-POL-A.8.16-S5.D** - Quick Reference Guide

Each section is independently versionable to support granular change management and targeted stakeholder reviews.

---

## 1.6 Document Maintenance

### 1.6.1 Review and Updates

This document shall be reviewed:
- **Annually** as part of the ISMS policy review cycle
- **Upon significant changes** to organizational risk profile, IT infrastructure, or threat landscape
- **Following security incidents** where monitoring gaps are identified
- **When new monitoring technologies** are deployed or existing tools are upgraded
- **Upon regulatory changes** affecting monitoring requirements

### 1.6.2 Change Management

Changes to this document require:
- Proposal with business/security justification
- Risk assessment of proposed changes
- Review by affected stakeholders (SOC, Security Engineering, System Owners)
- Approval by Policy Owner (CISO)
- Communication to relevant personnel
- Update to related implementation documentation

### 1.6.3 Version Control

This document uses semantic versioning:
- **Major version** (X.0): Significant structural changes or scope modifications
- **Minor version** (X.Y): Content updates, clarifications, or additions without scope change

All versions are retained in the organization's document management system with full change history.

---

## 1.7 Compliance and Enforcement

### 1.7.1 Policy Violations

Violations of monitoring policies may include:
- Unauthorized attempts to disable or tamper with monitoring systems
- Failure to configure systems for monitoring per requirements
- Ignoring or suppressing security alerts without proper justification/escalation
- Failure to investigate security alerts within defined timeframes
- Unauthorized access to or disclosure of monitoring data/logs
- Failure to report security incidents detected through monitoring

Violations are subject to disciplinary action in accordance with organizational policies and may include:
- Verbal or written warnings
- Mandatory security training
- Temporary restriction of system access privileges
- Suspension or termination of employment/contract
- Legal action where violations involve criminal activity or significant damage

### 1.7.2 Monitoring and Auditing

The organization reserves the right to:
- Monitor all activity on organizational networks, systems, and applications
- Review monitoring logs and alerts to investigate policy violations or security incidents
- Audit monitoring configurations to verify policy compliance
- Test monitoring effectiveness through red team exercises or simulated attacks
- Generate reports on monitoring coverage, detection effectiveness, and incident trends

Users should have **no expectation of privacy** when accessing organizational resources. Monitoring activities will be conducted in compliance with applicable laws and organizational privacy policies. Where required by law or regulation, users will be notified of monitoring activities.

### 1.7.3 Privacy Considerations

While this policy establishes monitoring for security purposes, the organization recognizes the need to balance security with privacy:
- Monitoring shall focus on security-relevant activities, not general user behavior
- Personal data collected through monitoring shall be handled per GDPR/FADP requirements
- Access to monitoring data shall be restricted to authorized personnel with legitimate need
- Monitoring data retention shall comply with data protection regulations
- Users shall be informed of monitoring activities where required by law
- Monitoring shall not be used for performance management or general employee surveillance (unless explicitly allowed by employment law and contracts)

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16** (Master Policy) - Overview and framework introduction
- **ISMS-POL-A.8.16-S2** (Requirements) - Detailed technical and operational requirements
- **ISMS-POL-A.8.16-S3** (Roles) - RACI matrix and accountability
- **ISMS-POL-A.8.16-S4** (Governance) - Policy lifecycle and updates
- **ISMS-POL-A.8.16-S5** (Annexes) - Templates and procedures

---

*"If you can't measure it, you can't detect it. If you can't detect it, you can't defend it."*  
*—Adapted from Lord Kelvin (probably)*