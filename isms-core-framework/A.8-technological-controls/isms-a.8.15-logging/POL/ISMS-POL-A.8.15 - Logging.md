<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.15:framework:POL:a.8.15 -->
**ISMS-POL-A.8.15 – Logging Policy**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Logging Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.15 |
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
| 1.0 | [Date] | CISO | Initial policy framework |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager
- Operational Review: Security Operations Center (SOC) Lead / IT Operations Manager
- Privacy Review: Data Protection Officer (DPO)
- Compliance Review: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.15.1-UG/TG (Log Source Inventory Assessment)
- ISMS-IMP-A.8.15.2-UG/TG (Log Collection & Centralization Assessment)
- ISMS-IMP-A.8.15.3-UG/TG (Log Protection & Retention Assessment)
- ISMS-IMP-A.8.15.4-UG/TG (Log Analysis & Review Assessment)
- ISMS-IMP-A.8.15.5-UG/TG (Logging Compliance Dashboard)
- ISMS-REF-A.8.15 (Logging Standards Reference)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.8.17 (Clock Synchronization)
- ISMS-POL-A.5.24 (Information Security Incident Management)

---

# Executive Summary

This policy establishes [Organization]'s requirements for event logging to support incident detection, forensic investigation, compliance obligations, and accountability in accordance with ISO/IEC 27001:2022 Control A.8.15.

**Purpose**: Define organizational requirements for event logging control implementation and governance. This policy establishes:

- WHAT events must be logged
- HOW LONG logs must be retained
- WHO is accountable for log management
- WHEN logs must be reviewed

Implementation procedures (HOW logs are technically configured) are documented separately in ISMS-IMP-A.8.15 (UG/TG variants).

**ISO/IEC 27001:2022 Control A.8.15 - Logging**:
> *Event logs recording user activities, exceptions, faults and information security events shall be produced, kept and regularly reviewed.*

---

# Scope

## In-Scope Systems and Activities

**This policy applies to**:

- All information systems, applications, and infrastructure components
- Network devices (routers, switches, firewalls, VPN gateways, load balancers)
- Security tools (SIEM, IDS/IPS, anti-malware, endpoint protection, DLP)
- Database systems and data storage platforms
- Cloud services and SaaS applications
- Authentication and identity management systems
- Administrative access infrastructure (jump hosts, bastion hosts, PAM)

**Deployment models covered**:

- On-premises infrastructure
- Cloud environments (public, private, hybrid)
- Third-party hosted services

## Out of Scope

- Business application audit trails not related to security
- Financial transaction logs for accounting purposes (covered by financial control policies)
- Real-time monitoring and alerting (covered by ISMS-POL-A.8.16)

---

# Policy Statements

## Event Logging Requirements

[Organization] SHALL log security-relevant events across all in-scope systems.

**Mandatory event categories**:

- **Authentication events**: Login attempts (success and failure), logout, account lockouts, password changes, MFA events
- **Authorization events**: Access to sensitive data, privilege escalation, access control changes
- **Administrative actions**: Configuration changes, user account management, privilege grants, security policy changes
- **Security events**: Malware detection, intrusion alerts, firewall blocks, DLP alerts
- **System events**: Startup/shutdown, service status changes, errors, resource exhaustion
- **Network events**: Firewall matches, VPN connections, segmentation boundary traversals
- **Application events**: Errors, exceptions, API authentication, privileged function execution

**Log content requirements**: Each log entry SHALL include timestamp, user identity, source system, event type, outcome, and relevant context. Detailed field specifications are documented in ISMS-REF-A.8.15.

## Log Protection Requirements

[Organization] SHALL protect logs from unauthorized access, modification, and deletion.

**Access control principles**:

- Read access limited to authorized personnel with legitimate need
- Write access restricted to logging services only
- Administrative access requires elevated privileges with separation of duties
- Log administrator actions SHALL be logged separately

**Integrity protection**:

- Logs SHALL be forwarded to centralized collection within 5 minutes for security events
- Centralized collection prevents local tampering
- Cryptographic or write-once protection SHOULD be implemented for compliance-critical logs

**Secure transmission**:

- Logs SHALL be transmitted encrypted using TLS 1.2 or higher

## Log Retention Requirements

[Organization] SHALL retain logs for periods sufficient to support investigation and compliance.

| Log Category | Online Storage | Archive Storage | Total Retention |
|--------------|----------------|-----------------|-----------------|
| Security events, authentication, administrative actions | 12 months | 7 years | 8 years |
| Database logs (sensitive data access) | 12 months | 7 years | 8 years |
| Application, network, and system logs | 6 months | 1 year | 1.5 years |

**Regulatory-specific minimums** (when applicable per ISMS-POL-00):

- PCI DSS v4.0.1: 12 months online
- HIPAA: 6 years total
- SOX: 7 years total

**Conflict Resolution**: When multiple regulations apply to the same system, the **most stringent requirement** SHALL govern. Example: System processing both payment cards and health data → 12 months online (PCI DSS v4.0.1) + 7 years archive (SOX/nDSG) = 8 years total retention.

**Storage and disposal**:

- Tiered storage architecture (hot, warm, cold) SHALL optimize cost and accessibility
- Logs SHALL be securely deleted after retention expiry using approved methods
- Legal hold procedures SHALL suspend deletion during litigation or investigation

## Log Review Requirements

[Organization] SHALL regularly review and analyze logs to detect security incidents.

| Review Type | Frequency | Responsibility |
|-------------|-----------|----------------|
| Automated analysis | Continuous (24/7) | SIEM / SOC |
| Daily review | Every business day | SOC Analysts |
| Weekly review | Weekly | Security Team |
| Monthly review | Monthly | Information Security Manager |
| Quarterly review | Quarterly | CISO |

**Automated detection** SHALL be implemented for:

- Brute force attacks
- Privilege escalation
- Data exfiltration indicators
- Malware indicators
- Policy violations

**Review Continuity Requirements**:

- SOC SHALL maintain 24/7 coverage via shift rotation or on-call roster
- Secondary reviewers SHALL be designated for each role (documented in SOC Roster)
- Absences exceeding 5 business days require formal delegation documented in access management system
- If scheduled review cannot be completed on time, Information Security Manager SHALL be notified within 24 hours
- SOC roster and backup assignments SHALL be reviewed monthly

## Privacy and Data Protection

[Organization] SHALL implement logging in compliance with privacy regulations.

**Prohibited data in logs**:

- Passwords (cleartext or encrypted)
- Full credit card numbers (truncated PANs permitted: first 6, last 4)
- Card verification codes (CVV/CVC)
- National identification numbers (full SSN, passport number)
- Full contents of personal communications (subject lines/metadata permitted)
- Biometric templates (raw biometric data prohibited; pseudonymized identifiers permitted)
- Other regulated special categories as identified by DPO per GDPR Art. 9 or nDSG Art. 5

**DPO Authoritative List**: DPO SHALL maintain authoritative list of prohibited data types, reviewed quarterly and updated when new data categories are processed.

**Privacy principles**:

- Minimize personal data collection in logs
- Use pseudonymization where feasible
- Inform users of monitoring through acceptable use policy
- DPO SHALL review logging implementations affecting personal data

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Accountability |
|------|----------------|
| **Executive Management** | Approve policy; ensure adequate resources; accept residual risks |
| **CISO** | Overall policy effectiveness; approve exceptions; define logging requirements based on risk |
| **Information Security Manager** | Implement policy requirements; coordinate logging enablement; manage exceptions |
| **SOC Team** | Daily log review; alert investigation; incident escalation; 24/7 coverage |
| **IT Operations** | Configure system logging; ensure log forwarding; maintain time synchronization |
| **System/Application Owners** | Enable appropriate logging; document log events; coordinate onboarding |
| **Log Administrators** | Manage SIEM platform; configure collection and retention; maintain separation of duties |
| **DPO** | Review privacy compliance; advise on personal data handling; respond to data subject requests |
| **All Personnel** | Comply with acceptable use policy; understand activities are logged |

---

# Regulatory Compliance

## Mandatory Compliance (Tier 1)

| Regulation | Requirement | Reference |
|-----------|-------------|-----------|
| **ISO/IEC 27001:2022** | Event logs SHALL be produced, kept, and regularly reviewed | Annex A.8.15 |
| **Swiss nDSG** | Appropriate technical measures including logging for data security | Art. 8 |
| **EU GDPR** | Logging as security measure for personal data protection | Art. 32 |

## Conditional Compliance (Tier 2)

Applies when triggered per ISMS-POL-00:

| Regulation | Trigger | Key Logging Requirements |
|-----------|---------|-------------------------|
| **DORA** | EU financial services | ICT incident detection and management |
| **NIS2** | Essential/important entity (EU) | Cybersecurity risk management logging |
| **PCI DSS v4.0.1** | Payment card processing | Req. 10: Comprehensive audit trails, 12-month online retention |
| **HIPAA** | US healthcare data | §164.312(b): Audit controls, 6-year retention |
| **SOX** | Public company financial reporting | Financial system audit trails, 7-year retention |

---

# Exception Management

## Exception Process

**Requirements**:

- Formal exception request with business justification
- Risk assessment required
- Compensating controls SHALL be implemented
- Maximum duration: 12 months (renewable)
- CISO approval required; Executive Management approval for high-risk exceptions

**Valid exception scenarios**:

- Legacy systems unable to forward logs
- Performance-sensitive systems where logging impacts operations
- Third-party systems without logging capabilities
- Cost-prohibitive implementations

## Exception Documentation

Each exception SHALL document:

- Affected system and requirement
- Business justification
- Risk assessment
- Compensating controls
- Duration and renewal conditions
- Approval signatures

---

# Incident Response

## Logging-Related Incidents

The following SHALL be classified as security incidents:

- Log tampering detected
- Log collection failure exceeding 15 minutes for critical systems
- Unauthorized log access
- Log storage capacity exhaustion
- SIEM platform compromise

## Incident Classification and Escalation

| Incident Type | Severity | Initial Response Time | Escalation Path |
|---------------|----------|----------------------|-----------------|
| Log tampering detected | Critical | Immediate (5 min) | SOC → Info Sec Manager → CISO → Exec Mgmt |
| Log collection failure (critical systems) | High | 15 minutes | SOC → Info Sec Manager → CISO (if >1 hour) |
| Unauthorized log access | High | 30 minutes | SOC → Info Sec Manager |
| SIEM platform compromise | Critical | Immediate (5 min) | SOC → CISO → Exec Mgmt |
| Log storage 90% full | Medium | 4 hours | Log Administrators → IT Ops Manager |

## Response Requirements

- CISO notification within 15 minutes for Critical incidents
- Forensic preservation: Immediate for all Critical and High incidents
- Root cause analysis: Within 48 hours for Critical, 5 days for High
- Integration with ISMS-POL-A.5.24 incident response framework
- Post-incident review for all Critical incidents within 7 days

---

# Policy Governance

## Review Schedule

| Review Type | Frequency | Authority |
|-------------|-----------|-----------|
| Policy review | Annual minimum | CISO + Executive Management |
| Implementation standards | Quarterly | Security Team, CISO approval |

**Review triggers**:

- Regulatory changes
- Major logging incidents
- Organizational changes
- Audit findings
- Technology changes

## Update Classification

| Type | Examples | Approval |
|------|----------|----------|
| **Minor** | Clarifications, references, corrections | CISO |
| **Major** | New requirements, scope changes, retention changes | CISO + Executive Management |
| **Emergency** | Critical security issues, urgent regulatory | CISO with Executive notification |

---

# Implementation Resources

## Supporting Documents

| Document | Purpose |
|----------|---------|
| **ISMS-IMP-A.8.15.1-UG/TG** | Log Source Inventory Assessment |
| **ISMS-IMP-A.8.15.2-UG/TG** | Log Collection & Centralization Assessment |
| **ISMS-IMP-A.8.15.3-UG/TG** | Log Protection & Retention Assessment |
| **ISMS-IMP-A.8.15.4-UG/TG** | Log Analysis & Review Assessment |
| **ISMS-IMP-A.8.15.5-UG/TG** | Compliance Dashboard |
| **ISMS-REF-A.8.15** | Logging Standards Reference (formats, schemas, technical specifications) |

## Related Controls

| Control | Integration |
|---------|-------------|
| **A.8.16 (Monitoring)** | Real-time monitoring consumes logs for alerting |
| **A.8.17 (Clock Synchronization)** | Accurate timestamps for log correlation |
| **A.5.24 (Incident Management)** | Logs provide incident detection and investigation evidence |
| **A.5.17-18 (Authentication/Access)** | Authentication and authorization events logged |

---

# Compliance Verification

## Assessment Schedule

| Domain | Frequency | Procedure | Evidence Output |
|--------|-----------|-----------|-----------------|
| Log Source Inventory | Annual (quarterly updates) | ISMS-IMP-A.8.15.1-UG/TG | Inventory workbook with coverage % |
| Collection & Centralization | Annual (quarterly metrics) | ISMS-IMP-A.8.15.2-UG/TG | Forwarding compliance report |
| Protection & Retention | Semi-annual | ISMS-IMP-A.8.15.3-UG/TG | Retention compliance workbook |
| Analysis & Review | Quarterly | ISMS-IMP-A.8.15.4-UG/TG | Review completion records |
| Compliance Dashboard | Quarterly | ISMS-IMP-A.8.15.5-UG/TG | Executive dashboard report |

## Evidence Location and Access

**Evidence Repository Structure**:
- **Assessment workbooks**: [GRC Platform / SharePoint] → ISMS → Controls → A.8.15 → [Assessment Name]
- **SIEM configuration records**: Configuration Management Database (CMDB) → Logging → [System Name]
- **Log retention reports**: SIEM → Reports → Compliance → Log_Retention_Monthly
- **Review completion records**: SIEM → Cases → [Review Period] OR SOC Ticketing System → A.8.15 Reviews
- **Exception register**: [GRC Platform / SharePoint] → ISMS → Exceptions → A.8.15
- **Gap register**: [GRC Platform] → ISMS → Gap Register (filter: Control = A.8.15)

**Access Procedure**:
- Internal auditors: Self-service access via GRC Platform role "Auditor"
- External auditors: Request evidence package via CISO or Information Security Manager
- Evidence custodian: Information Security Manager (primary), CISO (backup)
- Response timeline: Evidence provided within 2 business days of request

**Evidence Retention**: Assessment evidence SHALL be retained for 3 years minimum (aligns with ISO 27001 certification cycle).

## Gap and Finding Management

**Gap Identification and Recording**:
- Findings from log assessments (IMP-A.8.15.1-5) SHALL be recorded in organizational Gap Register (ISMS-REG-GAPS or GRC Platform equivalent)
- Each finding SHALL include:
  - Control ID: A.8.15
  - Finding description (specific requirement not met)
  - Severity: Critical / High / Medium / Low
  - Affected systems/scope
  - Root cause (if identified)
  - Responsible party (owner for remediation)
  - Target closure date
  - Current status (Open / In Progress / Closed)

**Gap Closure Requirements**:
- Gap closure requires evidence verification by Information Security Manager
- Evidence types accepted: Updated assessment workbook, SIEM configuration change log, review records
- High/Critical gaps require CISO approval for closure
- Closed gaps remain in register for audit trail (minimum 3 years)

**Escalation and Reporting**:
- Open gaps SHALL be reported monthly to CISO (part of security metrics)
- High-severity gaps open >30 days SHALL be escalated to Executive Management
- Critical gaps open >14 days require executive decision: accept risk OR allocate emergency resources

**Integration with Exception Process**:
- If gap cannot be remediated within target date, formal exception request (Section 7) MAY be submitted
- Exception approval does NOT close gap; gap remains open with status "Exception Granted"
- Exception expiry triggers gap remediation requirement

---

# Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Chief Information Security Officer (CISO)** | [Name] | | [Date] |
| **Information Security Manager** | [Name] | | [Date] |
| **Security Operations Center (SOC) Lead** | [Name] | | [Date] |
| **IT Operations Manager** | [Name] | | [Date] |
| **Data Protection Officer (DPO)** | [Name] | | [Date] |
| **Legal/Compliance Officer** | [Name] | | [Date] |
| **Executive Management (GL)** | [Name] | | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for event logging controls. Implementation procedures are documented in ISMS-IMP-A.8.15 (UG/TG). Technical standards are documented in ISMS-REF-A.8.15.*

<!-- QA_VERIFIED: 2026-02-02 -->
