# Control A.8.24: Use of Cryptography
## SECTION 3
## Roles & Responsibilities

---

**Document ID**: ISMS-POL-A.8.24-S3  
**Title**: Use of Cryptography - Roles & Responsibilities  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / HR Manager | Initial roles and accountability framework |

**Review Cycle**: Annual (or upon organizational restructuring)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Human Resources Officer (CHRO) or HR Director
- Business: Chief Information Officer (CIO) or IT Director
- Compliance: Legal/Compliance Officer (for accountability frameworks)

**Distribution**: All management levels, IT Security Team, HR Department, Internal Audit, Risk Management  
**Related Standards**: ISO/IEC 27001:2022 Controls A.5.1, A.5.3, A.8.24, RACI matrix best practices

---

## 3. Roles & Responsibilities

### Purpose
This section defines specific roles and their associated responsibilities for implementing, maintaining, and ensuring compliance with cryptographic controls as defined in this policy.

---

### 3.1 Responsibility Matrix

| Role | Responsibilities | Accountable Person |
|------|------------------|-------------------|
| **Chief Information Security Officer (CISO)** | • Overall accountability for cryptography policy and program<br>• Policy approval and annual review<br>• Risk acceptance for cryptographic exceptions<br>• Incident escalation point for cryptographic compromises<br>• Strategic cryptographic roadmap and budget approval<br>• Regulatory compliance oversight<br>• Authorization of deviations and exceptions | **[Name]** |
| **Information Security Officer (ISO) / Security Manager** | • Day-to-day policy enforcement and compliance monitoring<br>• Security team coordination and task assignment<br>• Exception request review and recommendation<br>• Security incident management for cryptographic events<br>• Key performance indicator (KPI) tracking and reporting<br>• Security awareness training coordination<br>• Audit liaison and evidence preparation | **[Name]** |
| **IT Manager / Infrastructure Manager** | • Overall implementation oversight and resource allocation<br>• Project management for cryptographic implementations<br>• Budget planning for cryptographic tools and systems<br>• Certificate management program ownership<br>• Coordination across IT teams (network, systems, database)<br>• Vendor management for cryptographic products<br>• Change management for cryptographic configurations | **[Name]** |
| **Network Team / Network Administrators** | • TLS/SSL configuration on network devices and load balancers<br>• VPN implementation and management (IPsec, WireGuard, OpenVPN)<br>• Certificate deployment on network infrastructure<br>• Wireless network encryption (WPA3/WPA2 Enterprise)<br>• Network-level encryption protocols<br>• Firewall rules for encrypted traffic<br>• Network security monitoring for cryptographic anomalies | **[Name]** |
| **Security Team / Security Engineers** | • Key management system administration<br>• HSM (Hardware Security Module) management<br>• Cryptographic monitoring and alerting configuration<br>• Security tool management (vulnerability scanners, SIEM)<br>• Certificate inventory maintenance<br>• Security assessments and penetration testing coordination<br>• Cryptographic vulnerability response<br>• Policy compliance verification and reporting | **[Name]** |
| **Database Administrators (DBAs)** | • Database encryption implementation (TDE, column-level)<br>• Database connection encryption configuration<br>• Database backup encryption<br>• Key rotation for database encryption keys<br>• Database key management and escrow<br>• Performance tuning for encrypted databases<br>• Database security monitoring and audit log review | **[Name]** |
| **System Administrators** | • Endpoint encryption deployment (BitLocker, FileVault, LUKS)<br>• Server encryption implementation<br>• Operating system cryptographic configuration<br>• Patch management for cryptographic updates<br>• Configuration compliance verification<br>• Recovery key escrow management<br>• System certificate management | **[Name]** |
| **Development Team / Application Developers** | • Secure coding practices with cryptography<br>• Application-level encryption implementation<br>• Cryptographic library integration and updates<br>• API security implementation (OAuth, API keys)<br>• Certificate integration in applications<br>• Secure credential storage in applications<br>• Code review for cryptographic implementations<br>• Security testing of cryptographic features | **[Name]** |
| **Cloud Architects / Cloud Engineers** | • Cloud encryption configuration (AWS, Azure, GCP)<br>• Customer-managed encryption key (CMEK) implementation<br>• Cloud KMS (Key Management Service) administration<br>• Cloud certificate management (ACM, Azure Key Vault, GCP Certificate Manager)<br>• Cloud security posture management for encryption<br>• Infrastructure-as-Code security for cryptographic resources<br>• Multi-cloud encryption strategy | **[Name]** |
| **Compliance / Audit Team** | • Regulatory compliance assessment<br>• Internal audit execution and reporting<br>• External audit coordination<br>• Compliance evidence collection and documentation<br>• Gap analysis and remediation tracking<br>• Regulatory monitoring (GDPR, PCI DSS, HIPAA, etc.)<br>• Audit finding remediation verification | **[Name]** |
| **Risk Management** | • Cryptographic risk assessments<br>• Risk treatment plan development<br>• Risk register maintenance for cryptographic risks<br>• Exception risk analysis<br>• Third-party cryptographic risk assessment<br>• Emerging threat monitoring (quantum computing, new attacks) | **[Name]** |
| **Training and Awareness Team / HR** | • Security awareness training program delivery<br>• Role-based cryptography training coordination<br>• Training completion tracking and reporting<br>• Training materials development<br>• New employee onboarding (cryptography awareness)<br>• Training effectiveness assessment | **[Name]** |
| **Procurement / Vendor Management** | • Vendor cryptographic capability assessment<br>• Cryptographic product evaluation<br>• Contract review for cryptographic requirements<br>• Vendor security questionnaire administration<br>• Third-party cryptographic audits coordination<br>• Vendor performance monitoring | **[Name]** |
| **Legal / Privacy Team** | • Regulatory interpretation and guidance<br>• Export control compliance for cryptography<br>• Privacy regulation compliance (GDPR, CCPA)<br>• Contract review for cryptographic clauses<br>• Breach notification assessment<br>• Legal risk assessment for cryptographic decisions | **[Name]** |
| **All Employees** | • Adherence to cryptography policy<br>• Use of strong passwords and MFA<br>• Protection of cryptographic credentials (passwords, keys, certificates)<br>• Reporting suspected cryptographic incidents<br>• Participation in security awareness training<br>• Secure handling of encrypted devices and media | **All Staff** |

---

### 3.2 RACI Matrix (Responsible, Accountable, Consulted, Informed)

**Key:**
- **R** = Responsible (does the work)
- **A** = Accountable (ultimate ownership, approves)
- **C** = Consulted (provides input)
- **I** = Informed (kept up to date)

| Activity | CISO | ISO/Security Manager | IT Manager | Network Team | Security Team | DBAs | SysAdmins | Developers | Compliance |
|----------|------|---------------------|------------|--------------|---------------|------|-----------|------------|------------|
| **Policy Development** | A | R | C | C | C | C | C | C | C |
| **Policy Approval** | A | I | I | I | I | I | I | I | I |
| **TLS/SSL Configuration** | I | C | A | R | C | - | - | - | I |
| **Certificate Management** | I | C | A | R | R | - | R | - | I |
| **Key Management** | C | A | C | - | R | R | - | - | I |
| **Database Encryption** | I | C | C | - | C | A/R | - | - | I |
| **Endpoint Encryption** | I | C | A | - | C | - | R | - | I |
| **Password Policy Enforcement** | C | A | R | - | R | - | R | - | I |
| **MFA Implementation** | I | C | A | R | R | - | R | C | I |
| **API Security** | I | C | C | C | C | - | - | A/R | I |
| **Security Monitoring** | I | A | C | C | R | - | - | - | I |
| **Incident Response** | A | R | C | C | R | C | C | C | I |
| **Exception Approval** | A | R | C | C | C | C | C | C | C |
| **Compliance Audits** | I | C | C | C | C | C | C | C | A/R |
| **Risk Assessment** | C | C | C | - | C | - | - | - | A/R |
| **Training Delivery** | I | C | C | - | C | - | - | - | I |
| **Vendor Assessment** | C | C | A | - | C | - | - | - | C |

---

### 3.3 Delegation of Authority

#### Authority Levels

**CISO Authority:**
- Final approval authority for all cryptographic policy decisions
- Risk acceptance for High and Critical severity exceptions
- Budget approval for cryptographic infrastructure
- Executive escalation for major cryptographic incidents

**ISO/Security Manager Authority:**
- Approval authority for Low and Medium severity exceptions (with CISO delegation)
- Day-to-day policy enforcement decisions
- Security tool procurement recommendations
- Security incident classification and response coordination

**IT Manager Authority:**
- Implementation decisions within policy boundaries
- Resource allocation for cryptographic projects
- Vendor selection (within approved product list)
- Change approval for standard cryptographic configurations

**Technical Team Authority:**
- Configuration and deployment within approved standards
- Tactical implementation decisions
- Tool and technology recommendations
- First-line troubleshooting and incident response

---

### 3.4 Escalation Paths

#### Cryptographic Incidents

**Severity-Based Escalation:**

| Severity | Initial Contact | Escalation (if unresolved) | Timeline |
|----------|----------------|---------------------------|----------|
| **Critical** | Security Team + CISO | Executive Management | Immediate |
| **High** | Security Team | ISO → CISO | Within 4 hours |
| **Medium** | Security Team | ISO | Within 24 hours |
| **Low** | Help Desk/IT | Security Team | Within 7 days |

**Critical Incident Examples:**
- Root CA private key compromise
- Widespread encryption key exposure
- Active exploitation of cryptographic vulnerability

**Escalation Triggers:**
- Incident unresolved within SLA
- Impact broader than initially assessed
- Regulatory notification required
- Customer data exposure
- Media/public attention

#### Policy Conflicts or Ambiguity

**Resolution Path:**
1. Technical team identifies conflict/ambiguity
2. Escalate to ISO/Security Manager
3. ISO convenes stakeholders (IT Manager, relevant technical leads)
4. ISO makes interpretation decision or escalates to CISO
5. CISO makes final determination
6. Policy clarification documented and communicated

---

### 3.5 Accountability Principles

**Clear Accountability:**
- Each cryptographic control MUST have a clearly assigned accountable person
- Accountability cannot be delegated (responsibility can be delegated)
- Accountable person answers for outcomes, not just effort

**Shared Responsibility:**
- Multiple people may be responsible for executing tasks
- Coordination required when responsibilities overlap
- Clear communication channels MUST be established

**Authority Commensurate with Responsibility:**
- Individuals assigned responsibilities MUST have appropriate authority
- Access rights, budget authority, and decision-making power MUST align with responsibilities
- Escalation paths available when authority is insufficient

**Consequences:**
- Non-performance of assigned responsibilities may result in disciplinary action
- Accountability reviews conducted during annual performance evaluations
- Persistent non-compliance escalated to management

---

### 3.6 Cross-Functional Collaboration

#### Security Champions Program (Optional)

**Concept:**
- Designate "Security Champions" within each technical team
- Champions serve as cryptography policy ambassadors
- Facilitate communication between security team and operational teams

**Champion Responsibilities:**
- Attend security working group meetings
- Provide feedback on policy practicality
- Assist with security awareness within their team
- First point of contact for policy questions

#### Working Groups and Committees

**Cryptography Working Group (Recommended):**
- **Membership:** ISO (chair), representatives from Network, Systems, Database, Development, Compliance
- **Frequency:** Quarterly (or as needed)
- **Purpose:**
  - Policy review and updates
  - Technology evaluation
  - Gap remediation planning
  - Incident lessons learned
  - Best practice sharing

**Security Steering Committee:**
- **Membership:** CISO (chair), IT Manager, ISO, Risk Manager, Compliance Manager, select business unit representatives
- **Frequency:** Monthly or Quarterly
- **Purpose:**
  - Strategic direction for security program (including cryptography)
  - Budget and resource allocation
  - Risk acceptance decisions
  - Major project approvals

---

### 3.7 Training Requirements by Role

| Role | Training Type | Frequency | Duration |
|------|---------------|-----------|----------|
| **All Employees** | General security awareness (including cryptography basics) | Annual | 30-60 minutes |
| **IT/Security Staff** | Cryptography fundamentals and policy training | Annual | 2-4 hours |
| **Developers** | Secure coding with cryptography | Annual | 4-8 hours |
| **System Admins** | Encryption implementation (BitLocker, FileVault, etc.) | Annual | 2-3 hours |
| **Network Admins** | TLS/SSL best practices and certificate management | Annual | 2-3 hours |
| **DBAs** | Database encryption (TDE, connection encryption) | Annual | 2-3 hours |
| **Security Team** | Advanced cryptography and key management | Annual | 8+ hours |
| **CISO/ISO** | Strategic cryptography and compliance | Annual | 4-8 hours |

**Training Delivery Methods:**
- Online learning modules
- Instructor-led training
- Vendor training (for specific products)
- Industry conferences and workshops
- Internal lunch-and-learn sessions

---

### 3.8 Performance Metrics by Role

#### Individual Performance Indicators

**Security Team:**
- Certificate expiration incidents (target: 0)
- Monitoring alert response time (target: <SLA)
- Vulnerability remediation time (target: <7 days for critical)
- Policy exception processing time (target: <10 business days)

**IT Operations Teams:**
- Encryption deployment compliance (target: >98%)
- Configuration compliance rate (target: >95%)
- Key rotation on-time percentage (target: >95%)
- Change success rate for cryptographic updates (target: >98%)

**Database Administrators:**
- Database encryption coverage (target: 100% for sensitive data)
- Backup encryption compliance (target: 100%)
- Database connection encryption rate (target: 100%)

**Developers:**
- Secure code review pass rate (cryptography) (target: 100%)
- Cryptographic library vulnerability remediation time (target: <30 days)

### 3.9 Key Ownership vs System Ownership

**Principle:** 
Encryption keys are organizational security assets managed independently from 
the systems they protect.

#### System Owner Accountability

**System Owners are accountable for:**
- Information security within their system/application domain
- Determining data classification and protection requirements
- Authorizing access to systems and data
- Ensuring cryptographic controls are implemented per policy

**System Owners do NOT:**
- Have automatic custody of encryption keys
- Control key lifecycle independently
- Access keys without Security Team authorization

#### Key Custodian Responsibility

**Security Team maintains custody of cryptographic keys:**
- Key generation, storage, rotation, and destruction
- Key access control and authorization
- Key backup and recovery procedures
- Key usage auditing and monitoring

**Key Access Requirements:**
- System owner authorization (business justification)
- AND Security Team approval (security validation)
- Documented in key access log

**Key Lifecycle Independence:**
- Keys MUST survive system owner departure
- Keys MUST survive system decommissioning
- Keys MUST survive organizational restructuring
- Key custodianship transfers via formal handover procedure

#### Separation of Duties

**For Restricted data classification:**
- System owner CANNOT be sole key custodian
- Key recovery requires dual control (Security Team + System Owner representative)
- Key generation and key usage MUST be separate roles (where technically feasible)
- HSM operations require split knowledge for master keys

**For Confidential data classification:**
- Security Team maintains key custody
- System owner authorized access with documented justification
- Single-person key access acceptable with audit logging

**For Internal data classification:**
- Standard key management procedures apply
- System owner may be delegated key management for low-sensitivity systems

#### Accountability Matrix

| Asset Type | Owner | Custodian | Lifecycle Authority |
|------------|-------|-----------|---------------------|
| **Information (data)** | Business Unit / Data Owner | System Owner | Business Unit |
| **System/Application** | IT Manager / System Owner | IT Operations Team | IT Governance |
| **Encryption Keys** | CISO / Security Team | Security Team + HSM | Security Governance |
| **Certificates** | IT Manager | Network/Security Team | Certificate Authority Policy |

#### Exception: User-Controlled Encryption

For endpoint encryption with user-managed passwords/PINs (BitLocker, FileVault):
- User is both system owner and key custodian
- Acceptable for personal workspace protection
- NOT acceptable for organizational Restricted data
- Recovery keys MUST be escrowed with Security Team or IT

**Related:** See Section 2.3.1 (Endpoint Encryption) for user responsibilities.

---

## Related Documents

- **ISMS-POL-A.8.24-S1** - Purpose, Scope, Definitions
- **ISMS-POL-A.8.24-S2.1 to S2.5** - Policy Requirements
- **ISMS-POL-A.8.24-S4** - Policy Governance (next section)
- **ISMS-IMP-A.8.24** - Implementation Status
- **ISMS Organizational Chart**
- **ISMS-POL-001** - Information Security Policy (defines overall ISMS roles)

---

**End of Section 3 - Roles & Responsibilities**

*"Responsibility without authority is frustration. Authority without responsibility is tyranny. This RACI matrix provides both."*  
*— The Wisdom of Organizational Design*