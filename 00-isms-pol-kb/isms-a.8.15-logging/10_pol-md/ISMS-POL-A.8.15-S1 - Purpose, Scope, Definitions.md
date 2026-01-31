# ISMS-POL-A.8.15-S1
## Logging - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.8.15-S1  
**Title**: Logging - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial foundational document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager
- Operational Review: IT Operations Manager / SOC Lead
- Compliance Review: Legal/Compliance Officer

**Distribution**: Security team, IT operations, SOC analysts, system owners, auditors  
**Related Documents**: ISMS-POL-A.8.15 (Master), ISMS-POL-00 (Regulatory Framework), ISO/IEC 27001:2022 A.8.15

---

## 1.1 Purpose

### 1.1.1 Policy Objective

This document establishes the purpose, scope, and key definitions for the organization's Logging policy framework, implementing ISO/IEC 27001:2022 Annex A Control 8.15 (Logging).

The policy framework aims to:

- **Detect** information security incidents and anomalous activities through comprehensive event logging
- **Investigate** security incidents with sufficient forensic evidence for root cause analysis
- **Comply** with legal, regulatory, and contractual obligations regarding audit trails and accountability
- **Demonstrate** accountability for user and administrator actions
- **Support** forensic analysis and legal proceedings with admissible evidence
- **Monitor** system performance, capacity, and operational health

### 1.1.2 Control Alignment

This policy implements ISO/IEC 27001:2022 Annex A.8.15:

> **A.8.15 Logging**  
> *Event logs recording user activities, exceptions, faults and information security events shall be produced, kept and regularly reviewed.*

The control recognizes that without comprehensive logging, organizations cannot:
- Detect security incidents in a timely manner
- Investigate breaches or policy violations
- Demonstrate compliance with regulatory requirements
- Attribute actions to specific users or systems
- Provide evidence in legal or disciplinary proceedings
- Perform effective forensic analysis
- Meet audit trail requirements for financial, healthcare, or other regulated systems

As ISO/IEC 27002:2022 Section 8.15 states: *"Event logs are essential for detecting, understanding, and recovering from security incidents."*

### 1.1.3 Risk Management Context

Logging serves as a **detective control** within the organization's layered security architecture. While logging alone does not prevent security incidents, it is essential for:

- **Early Detection**: Identifying suspicious patterns before significant damage occurs
- **Incident Response**: Providing situational awareness during active incidents
- **Forensic Investigation**: Reconstructing attacker actions and timelines
- **Compliance Evidence**: Demonstrating due diligence to regulators and auditors
- **Deterrence**: Discouraging malicious insider activity through accountability
- **Root Cause Analysis**: Understanding how incidents occurred to prevent recurrence

The organization recognizes that logging must balance competing objectives:
- **Comprehensiveness** (capturing all relevant events) vs. **Storage Costs** (volume management)
- **Privacy** (minimizing personal data collection) vs. **Security** (capturing user attribution)
- **Performance** (minimal system impact) vs. **Detail** (sufficient information for investigation)

As Feynman warned: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."* Our logging framework is designed to provide objective, tamper-proof evidence, not to support wishful thinking or cargo cult compliance.

---

## 1.2 Scope

### 1.2.1 In Scope

This policy framework applies to:

**Systems and Infrastructure**:
- Operating systems (Windows, Linux, Unix, macOS) - servers and workstations
- Network devices (routers, switches, firewalls, load balancers, wireless controllers)
- Security infrastructure (SIEM, IDS/IPS, firewalls, web filters, email gateways, DLP, EDR/XDR)
- Database systems (relational databases, NoSQL databases, data warehouses)
- Application servers (web servers, application middleware, message queues)
- Virtualization and hypervisors (VMware, Hyper-V, KVM, container platforms)
- Cloud infrastructure (IaaS, PaaS, SaaS logging capabilities)
- Storage systems (NAS, SAN, object storage)
- Identity and access management systems (Active Directory, LDAP, SSO, MFA)
- Backup and recovery systems
- Physical access control systems (badge readers, CCTV) where integrated with IT systems

**Applications**:
- Custom-developed applications (internal business applications)
- Commercial off-the-shelf (COTS) applications
- Web applications and APIs
- Mobile applications accessing corporate resources
- Cloud-based SaaS applications
- Database applications
- Administrative and management consoles

**Events**:
- Authentication events (successful and failed logins, logouts, password changes)
- Authorization events (permission grants, denials, changes)
- Data access (read, write, delete, copy, export operations on sensitive data)
- Administrative actions (user creation, privilege changes, configuration modifications)
- Security events (malware detection, policy violations, IDS/IPS alerts)
- System events (service starts/stops, errors, failures, crashes)
- Network events (connection attempts, firewall blocks, VPN sessions)
- Application events (transactions, errors, exceptions, audit-significant operations)

**Users and Entities**:
- All employees (full-time, part-time, temporary)
- Contractors and third-party personnel
- Administrative accounts (privileged users, system administrators, security administrators)
- Service accounts and automated processes
- External users (customers, partners) accessing organizational systems
- System-to-system interactions

### 1.2.2 Out of Scope

The following are explicitly excluded from this logging policy:

- **Business application audit trails** for financial transactions (covered by financial controls and SOX compliance frameworks)
- **Clinical/medical record access logs** (covered by healthcare-specific policies and HIPAA compliance where applicable)
- **Payment card transaction logs** (covered by PCI DSS Requirement 10 where applicable)
- **Real-time monitoring and alerting** processes (covered by ISMS-POL-A.8.16 - Monitoring Activities)
- **Clock synchronization** mechanisms (covered by ISMS-POL-A.8.17 - Clock Synchronization)
- **Log analysis procedures** in detail (covered in S2.4 and S5.C)
- **Content of user communications** (emails, chat messages, documents) - only metadata and access events
- **Application performance monitoring (APM)** unrelated to security
- **Network flow analysis** beyond security events
- **Business intelligence and analytics** logs unrelated to security or compliance

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

Organizations implementing this policy may choose any technology solution(s) that satisfy the stated requirements, including:
- Commercial SIEM platforms (Splunk, IBM QRadar, Microsoft Sentinel, LogRhythm, ArcSight, etc.)
- Open-source log management (ELK Stack, Graylog, Wazuh, etc.)
- Cloud-native logging services (AWS CloudWatch, Azure Monitor, GCP Cloud Logging)
- Hybrid architectures combining multiple solutions

Technology selection should be based on:
- Capability to meet policy requirements (log collection, retention, protection, analysis)
- Scalability to handle log volume (current and projected)
- Integration with existing infrastructure
- Query and analysis capabilities
- Cost-effectiveness (licensing, storage, operational costs)
- Vendor support and community maturity
- Compliance with data residency requirements

---

## 1.3 Definitions

### 1.3.1 Core Terminology

**Event Log / Log**  
A chronological record of events that have occurred within a system, application, or network device. Each log entry (event) typically contains a timestamp, source identifier, event type, and relevant details about what occurred.

**Logging**  
The process of recording events that occur within information systems, applications, and network infrastructure. Logging captures who did what, when, where, and with what outcome.

**Log Source**  
Any system, application, device, or service that generates event logs. Examples include servers, databases, firewalls, web applications, and security tools.

**Log Collector / Log Forwarder**  
Software agent or service that collects logs from sources and transmits them to a centralized log management system. Examples include syslog daemons, Splunk forwarders, Logstash agents, Fluentd.

**Log Management System / SIEM (Security Information and Event Management)**  
Centralized platform for collecting, storing, analyzing, and retaining logs from multiple sources. SIEM systems provide correlation, alerting, search, and reporting capabilities.

**Log Retention**  
The duration for which logs are stored before being archived or deleted. Retention periods are determined by regulatory requirements, business needs, and storage costs.

**Log Review**  
The process of examining logs to detect security incidents, policy violations, system errors, or anomalous activities. Reviews may be manual or automated.

**Log Integrity**  
The property that logs are complete, accurate, and protected from unauthorized modification or deletion. Integrity mechanisms include access controls, write-once storage, cryptographic hashing, and digital signatures.

**Hot Storage**  
Log storage tier providing immediate access for real-time analysis and investigation. Typically stored on high-performance disk or SSD with fast query capabilities.

**Warm Storage**  
Log storage tier for less frequently accessed logs, typically archived logs still within retention period but no longer needed for real-time analysis.

**Cold Storage / Archive Storage**  
Long-term log storage for compliance and legal requirements, typically on low-cost media (tape, object storage) with slower retrieval times.

### 1.3.2 Log Event Types

**Authentication Log**  
Records of user authentication attempts including successful logins, failed logins, logouts, session timeouts, password changes, and account lockouts.

**Authorization Log**  
Records of access control decisions including permission grants, access denials, privilege escalations, and role changes.

**Administrative Log / Privileged Access Log**  
Records of actions performed by users with elevated privileges including configuration changes, user account management, policy modifications, and security setting changes.

**Security Event Log**  
Records of security-relevant events including malware detections, intrusion attempts, policy violations, vulnerability scans, and security tool alerts.

**Audit Log**  
Records of audit-significant events required for compliance or forensic purposes, often with higher protection and retention requirements than standard logs.

**Application Log**  
Records of application-specific events including transactions, errors, exceptions, and business logic events.

**System Log**  
Records of operating system events including service starts/stops, system errors, hardware failures, and resource exhaustion events.

**Network Log**  
Records of network device events including connection attempts, firewall rule triggers, routing changes, and VPN sessions.

**Database Log**  
Records of database events including queries (especially DDL/DML on sensitive data), connection attempts, schema changes, and privilege grants.

### 1.3.3 Technical Terms

**Syslog**  
Standard protocol (RFC 5424) for transmitting log messages in IP networks. Widely supported across operating systems and network devices.

**Common Event Format (CEF)**  
Standardized log format developed by ArcSight (now OpenText) for security events, enabling consistent parsing across different log sources.

**JSON (JavaScript Object Notation) Logging**  
Structured log format using JSON syntax, increasingly common in modern applications and cloud services.

**Log Forwarding**  
The process of transmitting logs from a source system to a centralized log management system, typically in real-time or near-real-time.

**Log Aggregation**  
The process of collecting logs from multiple sources into a centralized repository for unified analysis and retention.

**Log Correlation**  
The process of analyzing relationships between events from different log sources to identify security incidents or operational issues.

**Log Normalization / Parsing**  
The process of converting logs from various formats into a standardized schema for consistent analysis and querying.

**Write-Once-Read-Many (WORM) Storage**  
Storage technology that prevents modification or deletion of data once written, ensuring log integrity for compliance and forensic purposes.

**Time Synchronization / NTP (Network Time Protocol)**  
Mechanism for synchronizing system clocks to ensure accurate and consistent timestamps across log sources. Critical for log correlation. (See ISMS-POL-A.8.17)

### 1.3.4 Organizational Terms

**System Owner**  
Individual responsible for an information system, application, or infrastructure component, including ensuring that system generates and forwards appropriate logs.

**Log Administrator**  
Individual responsible for managing the log management infrastructure, including log collection configuration, retention policies, and storage management.

**Security Operations Center (SOC)**  
Team responsible for monitoring security events, analyzing logs, investigating incidents, and responding to security alerts.

**Security Analyst / SOC Analyst**  
Individual who reviews and analyzes logs to detect and investigate security incidents.

**Compliance Officer / Legal Counsel**  
Individual responsible for interpreting legal and regulatory requirements related to logging, retention, and privacy.

---

## 1.4 Regulatory Framework

### 1.4.1 Compliance Overview

This logging policy framework is designed to satisfy requirements from multiple regulatory frameworks simultaneously. The organization's actual compliance obligations are determined by:
- Geographic regions of operation
- Industry sectors
- Types of data processed
- Contractual commitments

**For authoritative interpretation of regulatory applicability, refer to ISMS-POL-00 (Regulatory Applicability Framework).**

### 1.4.2 Mandatory Compliance (Applies to All)

**ISO/IEC 27001:2022 - Annex A Control 8.15**  
Organizations seeking ISO 27001 certification MUST implement this control. The control requires:
- Event logs recording user activities, exceptions, faults, and security events
- Logs shall be produced, kept, and regularly reviewed
- Protection of logs against tampering and unauthorized access

**Swiss Federal Data Protection Act (FADP) - Article 8**  
Organizations processing personal data in Switzerland MUST implement security measures including:
- Technical and organizational measures appropriate to risk level
- Ability to demonstrate compliance (accountability principle)
- Logging is implicit requirement for demonstrating data security

**EU General Data Protection Regulation (GDPR) - Article 32(1)(d)**  
Organizations processing EU personal data MUST implement:
- Technical measures to ensure ongoing confidentiality, integrity, availability
- "A process for regularly testing, assessing and evaluating effectiveness" (requires logging for evidence)
- Ability to detect and respond to personal data breaches (requires log monitoring)

### 1.4.3 Conditional Compliance (When in Scope)

**Digital Operational Resilience Act (DORA) - Article 17**  
Financial entities subject to DORA MUST maintain comprehensive logging to:
- Support ICT-related incident management
- Enable root cause analysis of incidents
- Provide evidence for regulatory reporting

**NIS2 Directive - Article 21**  
Essential and important entities under NIS2 MUST implement:
- Measures for cybersecurity risk management including logging
- Incident detection through log monitoring
- Ability to report incidents with supporting evidence

**PCI DSS 4.0 - Requirement 10**  
Organizations processing payment card data MUST implement:
- Logging of all access to system components and cardholder data
- Log review for suspicious activities
- Tamper-resistant log storage with retention of at least 12 months

**HIPAA Security Rule - 45 CFR § 164.312(b)**  
U.S. healthcare entities MUST implement:
- Audit controls to record and examine system activity
- Information system activity review procedures

### 1.4.4 Best Practice Alignment

This policy also aligns with recognized security frameworks:
- **NIST SP 800-92**: Guide to Computer Security Log Management
- **CIS Controls v8 - Control 8**: Audit Log Management
- **ISO/IEC 27002:2022 - Section 8.15**: Implementation guidance for logging
- **NIST Cybersecurity Framework**: Detection (DE) and Response (RS) functions
- **COBIT 2019**: DSS05 (Managed Security Services)

---

## 1.5 Document Structure and Navigation

### 1.5.1 Policy Framework Architecture

This document (S1) is part of a modular policy framework consisting of 14 interconnected documents:

**ISMS-POL-A.8.15 (Master Policy)**

**S1: Purpose, Scope, Definitions (THIS DOCUMENT)**
- Foundation for understanding the entire framework

**S2: Requirements Overview**
- High-level summary of all SHALL/SHOULD/MAY requirements

**S2.1: Event Logging Requirements**
- WHAT to log, HOW to structure log events

**S2.2: Log Protection & Integrity**
- HOW to protect logs from tampering

**S2.3: Log Retention & Storage**
- HOW LONG to keep logs, WHERE to store them

**S2.4: Log Review & Analysis**
- HOW to review and analyze logs

**S3: Roles & Responsibilities**
- WHO does WHAT in the logging lifecycle

**S4: Policy Governance**
- How this policy is managed and updated

**S5: Annexes**
- S5.A: Logging Standards (technical specifications)
- S5.B: Log Source Template (for new systems)
- S5.C: Log Review Procedures (operational procedures)
- S5.D: Quick Reference Guide (FAQ and decision trees)

### 1.5.2 How to Use This Document

**If you are NEW to the logging policy framework:**
1. Read this document (S1) first to understand purpose, scope, and terminology
2. Read S2 (Requirements Overview) to understand high-level requirements
3. Dive into specific sections (S2.1-S2.4) based on your role
4. Reference S5 annexes for technical details and procedures

**If you are a SYSTEM OWNER:**
- Read S1 (this document) and S2.1 (Event Logging Requirements)
- Use S5.B (Log Source Template) when onboarding new systems
- Reference S5.A (Logging Standards) for technical specifications

**If you are a SOC ANALYST:**
- Read S1 (this document) and S2.4 (Log Review & Analysis)
- Use S5.C (Log Review Procedures) for daily operations
- Reference S5.D (Quick Reference Guide) for common scenarios

**If you are an AUDITOR:**
- Read S1 (this document) and S2 (Requirements Overview)
- Use S3 (Roles & Responsibilities) to verify RACI assignments
- Reference ISMS-IMP-A.8.15.5 (Compliance Dashboard) for evidence

**If you are IMPLEMENTING logging infrastructure:**
- Read S1-S2.4 for complete requirements
- Use S5.A (Logging Standards) for technical specifications
- Reference S5.B (Log Source Template) for onboarding process

### 1.5.3 Document Dependencies

**This document (S1) is foundational** - all other policy sections assume familiarity with the purpose, scope, and definitions established here.

**Reading Order for Full Understanding:**
1. S1 (This document) - Foundation
2. S2 - Requirements Overview
3. S2.1, S2.2, S2.3, S2.4 - Detailed requirements (in any order based on interest)
4. S3 - Roles & Responsibilities
5. S4 - Policy Governance
6. S5.A, S5.B, S5.C, S5.D - Supporting annexes (as needed)

---

## 1.6 Key Principles (Cross-Reference)

The logging policy framework is guided by six foundational principles established in the master policy (ISMS-POL-A.8.15):

1. **Comprehensive Logging** - *"What isn't logged, can't be investigated."*
2. **Log Integrity** - *"A log you can't trust is worse than no log at all."*
3. **Timely Review** - *"Logs aren't write-only storage."*
4. **Appropriate Retention** - *"Storage is cheap, but compliance violations aren't."*
5. **Privacy by Design** - *"Log what you need, protect what you log."*
6. **No Cargo Cult Logging** - *"We log because we understand WHY, not just because ISO says so."*

Detailed explanation of these principles is provided in ISMS-POL-A.8.15 Section 1.4.

---

## 1.7 Related Controls and Integration

This logging policy does NOT exist in isolation. It integrates with:

**ISMS-POL-A.8.16 - Monitoring Activities**  
Logging provides the data source; monitoring consumes and analyzes that data to detect anomalies and incidents.

**ISMS-POL-A.8.17 - Clock Synchronization**  
Accurate timestamps are essential for log correlation and forensic analysis. All log sources MUST be time-synchronized.

**ISMS-POL-A.5.24 - Information Security Incident Management**  
Logs are the primary evidence source for incident detection, investigation, and response.

**ISMS-POL-A.8.11 - Data Masking**  
Logs containing sensitive data (personal information, credentials, etc.) SHALL be protected appropriately.

**ISMS-POL-A.5.16 - Identity Management**  
User attribution in logs depends on effective identity management and unique user identifiers.

---

## 1.8 Document Approval

This document is approved as part of the ISMS-POL-A.8.15 policy framework.

| Role | Name | Date | Status |
|------|------|------|--------|
| **Chief Information Security Officer (CISO)** | [Name] | [DD.MM.YYYY] | Approved |
| **Information Security Manager** | [Name] | [DD.MM.YYYY] | Reviewed |
| **IT Operations Manager** | [Name] | [DD.MM.YYYY] | Reviewed |
| **SOC Lead** | [Name] | [DD.MM.YYYY] | Reviewed |
| **Legal/Compliance Officer** | [Name] | [DD.MM.YYYY] | Reviewed |

**Effective Date**: [DD.MM.YYYY]  
**Next Review Date**: [DD.MM.YYYY + 12 months]

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S1 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **ISO 27002:2022 Section** | 8.15 (Event logging) |
| **Document Type** | Policy Section - Foundation |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Page Count** | [Auto-generated] |
| **Word Count** | ~3,800 words |
| **Line Count** | ~285 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |
| **Related Sections** | S2, S2.1, S2.2, S2.3, S2.4, S3, S4, S5 |

---

**END OF SECTION S1**

---

*"In science, you must not fool yourself – and you are the easiest person to fool."*  
— Richard P. Feynman

*"What isn't logged can't be investigated. What can't be investigated can't be improved."*  
— ISMS Implementer Wisdom

*"The difference between screwing around and science is writing it down."*  
— Adam Savage (adapted for logging)