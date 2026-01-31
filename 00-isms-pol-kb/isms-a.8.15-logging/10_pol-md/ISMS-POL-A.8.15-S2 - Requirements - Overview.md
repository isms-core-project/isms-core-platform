# ISMS-POL-A.8.15-S2
## Logging Requirements - Overview

**Document ID**: ISMS-POL-A.8.15-S2  
**Title**: Logging Requirements - Overview  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial requirements framework |

**Review Cycle**: Semi-annual (or upon significant infrastructure or regulatory changes)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager / Security Architect
- Operational Review: IT Operations Manager / SOC Lead
- Compliance Review: Legal/Compliance Officer

**Distribution**: Security team, IT operations, SOC analysts, system administrators, auditors  
**Related Documents**: ISMS-POL-A.8.15-S2.1 through S2.4 (specific requirements)

---

## 2.1 Introduction

This document provides an overview of logging requirements established to implement ISO/IEC 27001:2022 Control A.8.15. Detailed requirements are organized into four functional domains, each documented in separate policy sections to support granular change management and stakeholder accountability.

Logging requirements balance multiple organizational objectives:

- **Security**: Detection and investigation of security incidents through comprehensive event capture
- **Compliance**: Adherence to legal, regulatory, and contractual audit trail obligations
- **Privacy**: Respect for data protection requirements while maintaining necessary accountability
- **Forensics**: Preservation of evidence for incident response and legal proceedings
- **Operational Efficiency**: Maintainable, scalable logging solutions that don't overwhelm storage or analysis capacity
- **Performance**: Minimal impact on system performance and user experience

As the policy principles state: *"We log because we understand WHY, not just because ISO says so."* Every requirement in this framework has a clear security or compliance justification.

---

## 2.2 Requirements Framework

Logging requirements are organized into four domains corresponding to the logging lifecycle:

### 2.2.1 Event Logging Requirements (S2.1)

**Objective**: Define WHAT events must be logged, WHERE they are logged, and HOW log events should be structured.

**Scope**: Requirements for:
- Mandatory log event categories (authentication, authorization, administrative actions, security events)
- System-specific logging (operating systems, databases, applications)
- Network device logging (firewalls, switches, routers, VPN concentrators)
- Security tool logging (SIEM, IDS/IPS, EDR, web filters, email gateways)
- Log content standards (timestamp, user ID, action, outcome, source IP)
- Log format specifications (syslog, CEF, JSON)
- Time synchronization requirements (cross-reference to ISMS-POL-A.8.17)

**Primary Stakeholders**: System Owners, Application Developers, Network Administrators, Security Engineers  
**Detailed Requirements**: ISMS-POL-A.8.15-S2.1

**Implementation Evidence**: ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment)

### 2.2.2 Log Protection & Integrity Requirements (S2.2)

**Objective**: Ensure logs are protected from unauthorized access, modification, and deletion to maintain their evidentiary value.

**Scope**: Requirements for:
- Access control to log data (who can read, search, export logs)
- Administrative access to log infrastructure (separation of duties)
- Integrity protection mechanisms (write-once storage, cryptographic hashing, digital signatures)
- Tamper detection and alerting (detecting unauthorized log modifications or deletions)
- Secure log transmission (encryption in transit from source to log management system)
- Protection from malicious insiders (preventing administrators from covering their tracks)
- Backup and disaster recovery for log data

**Primary Stakeholders**: Security Team, IT Operations, Log Administrators, Compliance Officers  
**Detailed Requirements**: ISMS-POL-A.8.15-S2.2

**Implementation Evidence**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)

### 2.2.3 Log Retention & Storage Requirements (S2.3)

**Objective**: Define HOW LONG logs must be retained and WHERE/HOW they should be stored to meet regulatory and business requirements.

**Scope**: Requirements for:
- Retention periods by log type (security logs, authentication, administrative, application logs)
- Regulatory retention requirements (GDPR, FADP, DORA, NIS2, PCI DSS, HIPAA where applicable)
- Storage tier architecture (hot storage for recent logs, warm storage for archives, cold storage for long-term compliance)
- Archival procedures and format standards (ensuring long-term readability)
- Disposal procedures (secure deletion after retention period expires)
- Legal hold procedures (suspension of disposal for investigations or litigation)
- Storage capacity planning and scalability
- Cost optimization strategies

**Primary Stakeholders**: IT Operations, Storage Administrators, Legal/Compliance, Finance  
**Detailed Requirements**: ISMS-POL-A.8.15-S2.3

**Implementation Evidence**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)

### 2.2.4 Log Review & Analysis Requirements (S2.4)

**Objective**: Ensure logs are regularly reviewed and analyzed to detect security incidents, policy violations, and operational issues.

**Scope**: Requirements for:
- Review frequency by log type (daily, weekly, monthly)
- Automated analysis capabilities (SIEM correlation rules, anomaly detection)
- Alert configuration and escalation procedures
- Investigation procedures (incident response playbooks)
- Reporting requirements (to management, regulators, auditors)
- Key Performance Indicators (KPIs) for logging effectiveness
- Integration with incident response processes (ISMS-POL-A.5.24)
- Use case development (what to look for, what patterns indicate compromise)

**Primary Stakeholders**: Security Operations Center (SOC), Security Analysts, Incident Responders  
**Detailed Requirements**: ISMS-POL-A.8.15-S2.4

**Implementation Evidence**: ISMS-IMP-A.8.15.2 (Log Collection & Centralization), ISMS-IMP-A.8.15.4 (Log Analysis & Review)

---

## 2.3 Risk-Based Approach

Logging requirements follow a risk-based methodology:

1. **Identify Critical Assets**: Systems and data requiring the most comprehensive logging
2. **Identify Threat Scenarios**: Attack patterns and incident types logs must help detect
3. **Assess Detection Gaps**: Current logging capabilities vs. required visibility
4. **Define Requirements**: Specific log events and analysis capabilities needed
5. **Implement Solutions**: Deploy log management infrastructure meeting requirements
6. **Monitor Effectiveness**: Measure detection capabilities and adjust as needed
7. **Review Periodically**: Reassess threats and logging adequacy as environment evolves

Requirements are **not one-size-fits-all**. Organizations must:
- Consider their specific threat profile and regulatory obligations
- Balance logging comprehensiveness with storage costs and performance impact
- Prioritize logging for high-risk systems and sensitive data
- Document risk-based decisions and trade-offs
- Accept residual risk where comprehensive logging is not feasible

**Key Risk Considerations**:
- **Over-logging Risk**: Excessive logs overwhelm analysis capacity, increasing detection time
- **Under-logging Risk**: Insufficient logs prevent incident detection and investigation
- **Storage Risk**: Inadequate retention may violate compliance requirements or limit forensic analysis
- **Performance Risk**: Inefficient logging can degrade system performance
- **Privacy Risk**: Excessive personal data in logs may violate data protection regulations

---

## 2.4 Technology Neutrality

All requirements in this framework are **vendor-agnostic** and **technology-independent**. Requirements specify:

- **Capabilities** that must be achieved (WHAT must be logged, protected, retained, analyzed)
- **Outcomes** that must be demonstrated (WHY each requirement exists)

Requirements do **NOT** specify:
- Specific SIEM or log management vendor products
- Implementation architectures or technologies
- Configuration parameters or technical settings

Organizations may satisfy requirements using any technology solution(s) appropriate to their environment, including:
- Commercial SIEM platforms (Splunk, QRadar, Sentinel, LogRhythm, etc.)
- Open-source solutions (ELK Stack, Graylog, Wazuh)
- Cloud-native services (AWS CloudWatch, Azure Monitor, GCP Cloud Logging)
- Hybrid architectures combining multiple tools

The solution must demonstrably meet stated requirements regardless of implementation approach.

---

## 2.5 Relationship to Implementation

Policy requirements (this document and S2.1-S2.4) define **WHAT** must be achieved. Implementation specifications (ISMS-IMP-A.8.15.x) define **HOW** compliance is assessed and demonstrated.

**Mapping**:

| Policy Section | Implementation Assessment | Purpose |
|----------------|--------------------------|---------|
| S2.1 (Event Logging) | IMP-A.8.15.1 | Catalog all log sources and verify completeness |
| S2.1 (Event Logging) | IMP-A.8.15.2 | Verify log collection and centralization |
| S2.2 (Log Protection) | IMP-A.8.15.3 | Document integrity protection mechanisms and access controls |
| S2.3 (Log Retention) | IMP-A.8.15.3 | Verify retention compliance and storage architecture |
| S2.4 (Log Review & Analysis) | IMP-A.8.15.2 | Document SIEM/analysis capabilities |
| S2.4 (Log Review & Analysis) | IMP-A.8.15.4 | Verify review processes and effectiveness metrics |
| All Sections | IMP-A.8.15.5 | Consolidated compliance dashboard and gap analysis |

Implementation assessments provide evidence that policy requirements are met, using quantifiable metrics and documented artifacts.

---

## 2.6 Compliance Verification

Compliance with logging requirements shall be verified through:

**Technical Assessments**:
- Evaluation of log management infrastructure capabilities
- Verification that all in-scope systems generate and forward logs
- Testing of integrity protection mechanisms
- Validation of retention periods and disposal processes

**Operational Reviews**:
- Examination of log review procedures and documentation
- Review of SOC playbooks and investigation workflows
- Assessment of alert tuning and false positive rates
- Verification of incident response log utilization

**Audit Evidence**:
- Log source inventory completeness (IMP-A.8.15.1)
- Log collection reliability metrics (IMP-A.8.15.2)
- Retention compliance reports (IMP-A.8.15.3)
- Log review effectiveness metrics (IMP-A.8.15.4)
- Sample log extracts demonstrating content standards

**Continuous Monitoring**:
- Automated checks for log forwarding failures
- Storage capacity monitoring and alerting
- Detection of gaps in log collection
- Regular validation of timestamp accuracy

**Third-Party Audits**:
- External validation during ISO 27001 certification audits
- Regulatory examinations (DORA, NIS2, PCI DSS audits where applicable)
- Penetration testing verification of logging effectiveness

Evidence of compliance shall be documented in implementation assessment workbooks (ISMS-IMP-A.8.15.x) and retained per organizational record retention policies.

---

## 2.7 Requirement Prioritization

Where resource constraints prevent simultaneous implementation of all requirements, organizations should prioritize:

### Critical (Must Implement):
- Authentication and authorization event logging (S2.1) - Essential for accountability
- Administrative action logging (S2.1) - Required to detect insider threats
- Security event logging (S2.1) - Core incident detection capability
- Basic log integrity protection (S2.2) - Prevents evidence tampering
- Minimum regulatory retention (S2.3) - Mandatory compliance requirement
- Log collection for critical systems (S2.1, S2.2) - Focus on crown jewels first

### Important (Should Implement):
- Comprehensive system and application logging (S2.1) - Broader visibility
- Advanced integrity protection (S2.2) - Enhanced tamper resistance
- Extended retention for security logs (S2.3) - Better forensic capability
- Automated log review and correlation (S2.4) - Scalable detection
- Coverage of all managed systems (S2.1) - Complete visibility

### Beneficial (May Implement):
- Logging of low-risk systems (S2.1) - Comprehensive coverage
- Advanced analytics and machine learning (S2.4) - Enhanced detection
- Long-term cold storage beyond regulatory minimum (S2.3) - Extended forensic window
- Integration with advanced threat intelligence (S2.4) - Proactive detection

Prioritization decisions must be documented with risk justification and approved by the CISO. Organizations SHALL NOT skip Critical requirements without documented risk acceptance.

---

## 2.8 SHALL / SHOULD / MAY Requirement Summary

This framework uses RFC 2119 terminology:

**SHALL** = Mandatory requirement (non-compliance requires risk acceptance)  
**SHOULD** = Strongly recommended (non-compliance requires justification)  
**MAY** = Optional (implementation at organization's discretion)

### Quick Reference by Domain:

**S2.1 (Event Logging)**:
- SHALL: Authentication events, administrative actions, security events, access to sensitive data
- SHOULD: Application errors, system events, network connections
- MAY: Non-security operational events, verbose debugging logs

**S2.2 (Log Protection)**:
- SHALL: Access controls, separation of duties, secure transmission
- SHOULD: Cryptographic integrity protection, write-once storage
- MAY: Hardware security modules (HSM) for log signing

**S2.3 (Log Retention)**:
- SHALL: Meet regulatory minimum retention periods, secure disposal after retention
- SHOULD: Tiered storage architecture, capacity planning
- MAY: Extended retention beyond regulatory requirements

**S2.4 (Log Review)**:
- SHALL: Regular review of security logs, documented investigation procedures
- SHOULD: Automated correlation and alerting, integration with SIEM
- MAY: Advanced analytics, machine learning anomaly detection

Detailed requirements with specific SHALL/SHOULD/MAY statements are in sections S2.1-S2.4.

---

## 2.9 Integration with Related Controls

This logging policy does not exist in isolation. Requirements must be implemented in coordination with:

**ISMS-POL-A.8.16 (Monitoring Activities)**:
- Logging provides data; monitoring analyzes and acts on that data
- Requirements must be coordinated to ensure monitoring has necessary log inputs

**ISMS-POL-A.8.17 (Clock Synchronization)**:
- Accurate timestamps are prerequisite for effective log correlation
- All log sources SHALL be time-synchronized per A.8.17 requirements

**ISMS-POL-A.5.24 (Incident Management)**:
- Logs are primary evidence source for incident detection and investigation
- Logging requirements must support incident response procedures

**ISMS-POL-A.5.16 (Identity Management)**:
- User attribution in logs depends on unique user identifiers
- Service accounts must be individually identifiable in logs

**ISMS-POL-A.8.11 (Data Masking)**:
- Sensitive data in logs (PII, credentials, payment data) must be protected
- Consider data minimization in log design

---

## 2.10 Privacy Considerations

Logging requirements must balance security needs with privacy obligations:

**Data Minimization**:
- Log only what is necessary for security and compliance purposes
- Avoid logging message content, document bodies, or full payloads where possible
- Log metadata (who, what, when, where) rather than content (details of what was said/written)

**Personal Data Protection**:
- Logs containing personal data are subject to GDPR/FADP requirements
- Apply appropriate retention limits (don't store forever "just in case")
- Implement access controls (not everyone needs access to all logs)
- Consider pseudonymization where user attribution isn't required

**Transparency**:
- Inform users that their activities are logged (acceptable use policy, privacy notice)
- Don't conduct covert monitoring without legal justification

**Purpose Limitation**:
- Use logs only for stated purposes (security, compliance, operations)
- Don't repurpose security logs for performance management or employee surveillance

Detailed privacy guidance is provided in S2.1 (what to log) and S2.2 (log access controls).

---

## 2.11 Document Structure

The complete Logging Requirements framework consists of:

- **ISMS-POL-A.8.15-S2** - This overview document
- **ISMS-POL-A.8.15-S2.1** - Event Logging Requirements (WHAT to log)
- **ISMS-POL-A.8.15-S2.2** - Log Protection & Integrity Requirements (HOW to protect)
- **ISMS-POL-A.8.15-S2.3** - Log Retention & Storage Requirements (HOW LONG to keep)
- **ISMS-POL-A.8.15-S2.4** - Log Review & Analysis Requirements (HOW to analyze)

Each section is independently versionable. Changes to one section do not require re-approval of other sections unless dependencies exist.

**Recommended Reading Order**:
1. Read this overview (S2) to understand the framework structure
2. Read S2.1 to understand what must be logged
3. Read S2.2 to understand log protection requirements
4. Read S2.3 to understand retention and storage requirements
5. Read S2.4 to understand review and analysis requirements

---

## 2.12 Document Approval

This document is approved as part of the ISMS-POL-A.8.15 policy framework.

| Role | Name | Date | Status |
|------|------|------|--------|
| **Chief Information Security Officer (CISO)** | [Name] | [DD.MM.YYYY] | Approved |
| **Information Security Manager** | [Name] | [DD.MM.YYYY] | Reviewed |
| **IT Operations Manager** | [Name] | [DD.MM.YYYY] | Reviewed |
| **SOC Lead** | [Name] | [DD.MM.YYYY] | Reviewed |
| **Legal/Compliance Officer** | [Name] | [DD.MM.YYYY] | Reviewed |

**Effective Date**: [DD.MM.YYYY]  
**Next Review Date**: [DD.MM.YYYY + 6 months]

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S2 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **ISO 27002:2022 Section** | 8.15 (Event logging) |
| **Document Type** | Policy Section - Requirements Overview |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Page Count** | [Auto-generated] |
| **Word Count** | ~2,800 words |
| **Line Count** | ~300 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |
| **Related Sections** | S2.1, S2.2, S2.3, S2.4 |
| **Subsections** | 4 detailed requirement documents |

---

**END OF SECTION S2**

---

*"The first principle is that you must not fool yourself—and you are the easiest person to fool."*  
— Richard P. Feynman

*"If you can't measure it, you can't manage it. If you can't log it, you can't investigate it."*  
— ISMS Wisdom (adapted from Drucker)

*"Logs are the difference between 'we got hacked' and 'here's exactly what the attacker did.'"*  
— Ancient SOC Proverb