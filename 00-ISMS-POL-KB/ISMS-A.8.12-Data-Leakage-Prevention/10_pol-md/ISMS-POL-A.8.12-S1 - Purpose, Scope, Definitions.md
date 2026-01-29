# ISMS-POL-A.8.12-S1
## Data Leakage Prevention - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.8.12-S1  
**Title**: Data Leakage Prevention - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: 2025-01-03  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-03 | Information Security Manager | Initial foundational document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: 2026-01-03  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager
- Compliance Review: Data Protection Officer (DPO) / Legal/Compliance Officer

**Distribution**: Security team, IT operations, policy administrators, data owners  
**Related Documents**: ISMS-POL-A.8.12 (Master), ISO/IEC 27001:2022 A.8.12, ISO/IEC 27002:2022 Control 8.12

---

## 1. Purpose

### 1.1 Policy Objective

This document establishes the purpose, scope, and key definitions for the organization's Data Leakage Prevention (DLP) policy framework, implementing ISO/IEC 27001:2022 Annex A Control 8.12 (Data Leakage Prevention).

The policy framework aims to:

- **Protect** the organization from unauthorized disclosure of sensitive information through all egress channels
- **Prevent** data exfiltration by insiders (malicious or negligent) and external attackers
- **Detect** data leakage attempts through monitoring and alerting mechanisms
- **Comply** with legal, regulatory, and contractual obligations regarding data protection (Swiss FADP, EU GDPR)
- **Enable** legitimate business operations while safeguarding confidential information

### 1.2 Control Alignment

This policy implements ISO/IEC 27001:2022 Annex A.8.12:

> **A.8.12 Data Leakage Prevention**  
> *Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information.*

The control recognizes that uncontrolled data egress exposes organizations to:
- Regulatory violations and fines (FADP: CHF 250K, GDPR: 4% global revenue or €20M)
- Loss of competitive advantage (intellectual property theft, trade secrets disclosure)
- Customer trust erosion (brand damage, customer churn)
- Legal liability (civil lawsuits, contractual penalties)
- Operational disruption (incident response, remediation costs)

### 1.3 Risk Management Context

Data leakage prevention serves as a **preventive and detective control** within the organization's layered security architecture.

**Threat Landscape:**
- **Insider Threats:** Employees exfiltrating data intentionally (e.g., departing employees stealing IP) or unintentionally (e.g., sending customer lists to personal email)
- **External Attackers:** APT groups exfiltrating data via command-and-control channels, malware, or compromised accounts
- **Accidental Disclosure:** Users misconfiguring cloud storage permissions, misdirecting emails, or uploading to unauthorized services
- **Shadow IT:** Unapproved cloud services and file-sharing tools bypassing organizational controls

**Risk Treatment:**
DLP addresses the risk of **unauthorized data disclosure** by implementing technical controls (DLP solutions), policy enforcement (acceptable use), and monitoring (alert generation and incident response).

### 1.4 Philosophy: Intelligence Over Theater

> *"The first principle is that you must not fool yourself about your data protection—and you are the easiest person to fool."*  
*— Richard Feynman (adapted for DLP context)

This framework rejects "checkbox compliance" in favor of **evidence-based effectiveness**:

- **DLP is 20% technology and 80% process:** Technology alone does not prevent data leakage; continuous tuning, user education, and incident response are critical
- **False positives are inevitable:** Accept 60-80% false positive rate initially, target <10% after 6 months of tuning
- **Monitor-only mode first:** Deploy in alert-only mode for 30-90 days to establish baseline before blocking
- **User education is essential:** Every DLP block is either a prevented breach or a teachable moment
- **Legal compliance is mandatory:** Employee monitoring requires transparency, proportionality, and works council consultation (Swiss FADP, EU GDPR)

**DLP implementations fail due to stupidity (lazy deployment, cargo cult copying, inadequate tuning) far more often than malice. This framework chooses intelligence and organization.**

> *"En matière de grande catastrophe publique, toujours privilégier la connerie au complot. La connerie est à la portée de tous, c'est donc assez largement répandu. Le complot nécessite beaucoup d'intelligence et d'organisation, c'est très rare."*  
> — Michel Rocard, Former Prime Minister of France

**Translation:** When it comes to disasters, favor stupidity over conspiracy. Stupidity is common; intelligence and organization are rare. This framework chooses the latter.

---

## 2. Scope

### 2.1 Scope Inclusions

This policy framework applies to:

**Information Assets:**
- All information classified as **Internal, Confidential, or Restricted** per organizational data classification policy (ISMS-POL-A.5.12)
- Personally Identifiable Information (PII) subject to FADP/GDPR
- Financial data (payment card data, bank accounts, financial records)
- Intellectual property (source code, designs, trade secrets, patents)
- Credentials and authentication secrets (passwords, API keys, certificates)
- Business confidential information (contracts, strategies, M&A, pricing)

**Systems and Devices:**
- All organizational endpoints (laptops, desktops, workstations, servers)
- All mobile devices accessing organizational data (BYOD, corporate-owned)
- All network segments (LAN, WAN, DMZ, wireless, VPN)
- All cloud services processing organizational data (SaaS, IaaS, PaaS)
- All applications with data export capabilities (databases, reporting tools, collaboration platforms)

**Data Egress Channels:**
- **Email** (SMTP, webmail, Exchange Online, O365, Google Workspace)
- **Web/Cloud** (HTTP uploads, file sharing, cloud storage, SaaS applications)
- **Endpoint** (USB drives, external media, optical drives, Bluetooth, clipboard, screenshots)
- **Network** (FTP, SMB file shares, unauthorized protocols)
- **Print** (physical printers, print-to-PDF, virtual printers)
- **Applications** (database exports, API calls, reporting exports)
- **Mobile** (camera, screenshots, app data sharing, mobile email)

**Personnel:**
- All employees (full-time, part-time, temporary, contractors)
- All third-party service providers with access to organizational data
- All privileged users (administrators, developers, database admins)
- All executives and management with access to confidential information

**Locations:**
- All organizational facilities (headquarters, branch offices, data centers)
- All remote work locations (home offices, co-working spaces, public networks)
- All geographic jurisdictions where organizational data is processed

### 2.2 Scope Exclusions

The following are explicitly **excluded** from this policy framework:

**Out-of-Scope Information:**
- Public information (press releases, marketing materials, public websites)
- Information already in the public domain
- Personal employee data unrelated to organizational information (personal photos, personal documents on personal devices outside working hours)

**Out-of-Scope Systems:**
- Personal devices not accessing organizational data
- Test/development environments with no production data (sanitized test data only)
- Isolated networks with no connection to organizational systems

**Out-of-Scope Activities:**
- Information security controls unrelated to data exfiltration (access control, authentication, patching) → covered by other ISO 27001 controls
- Physical security of paper documents → covered by ISMS-POL-A.7.X (Physical Security)
- Backup and archival processes → covered by ISMS-POL-A.8.13 (Information Backup)
- Data retention and deletion → covered by ISMS-POL-A.8.10 (Information Deletion)

**Jurisdictional Exclusions:**
- **US Federal requirements** (FISMA, FedRAMP, FIPS) apply **only** where the organization acts as contractor to US federal agencies or has explicit contractual obligations. Otherwise, these references are informational only.

### 2.3 Scope Boundaries

**Temporal Scope:**
- This policy applies during business hours AND outside business hours if organizational data is accessed
- DLP monitoring operates 24/7/365 where technically deployed

**Geographic Scope:**
- This policy applies globally wherever organizational data is processed
- Jurisdiction-specific requirements (Swiss FADP, EU GDPR) apply based on data processing location and data subject location

**Technology Scope:**
- This policy is **vendor-agnostic** and technology-independent
- Organizations may implement DLP using any combination of technologies (network-based DLP, endpoint agents, cloud-based DLP, email gateways, application-level controls)
- Specific technology implementations are documented in assessment workbooks (ISMS-IMP-A.8.12.1-5), not in policy documents

---

## 3. Definitions

### 3.1 Core Terminology

**Data Leakage Prevention (DLP):**  
A set of technologies, processes, and policies designed to detect, prevent, and respond to unauthorized disclosure, transfer, or exfiltration of sensitive information from organizational systems, networks, and endpoints.

**Data Leakage:**  
The unintentional or unauthorized disclosure of sensitive information to external parties or unauthorized internal parties. Includes accidental disclosure (user error, misconfiguration) and malicious exfiltration (insider threats, malware, APT).

**Data Loss:**  
The permanent destruction or unavailability of information due to hardware failure, corruption, deletion, or disaster. Data loss is addressed by backup and disaster recovery controls (ISMS-POL-A.8.13, ISMS-POL-A.7.14), **not** by DLP.

**Distinction - Data Leakage vs. Data Loss:**
- **Data Leakage** = Information is disclosed to unauthorized parties (confidentiality breach)
- **Data Loss** = Information is destroyed or unavailable (availability breach)
- **DLP controls address leakage, not loss**

**Sensitive Data / Confidential Information:**  
Information classified as Internal, Confidential, or Restricted per organizational data classification policy (ISMS-POL-A.5.12). Includes PII, financial data, intellectual property, credentials, and business confidential information.

**Egress Channel / Data Exfiltration Path:**  
Any mechanism by which data can leave organizational control, including email, web uploads, removable media, network file transfers, print, mobile devices, and applications.

**False Positive:**  
A DLP alert triggered by legitimate business activity (e.g., Finance sending invoices with account numbers to known banks). False positives require tuning to reduce operational burden and prevent alert fatigue.

**False Negative:**  
A data leakage event that was NOT detected by DLP controls (e.g., sensitive data exfiltrated via an unmonitored channel or bypassing DLP rules). False negatives represent control gaps and security risk.

### 3.2 DLP Operational Modes

**Monitor Mode (Alert-Only):**  
DLP solution logs and alerts on policy violations but does NOT block data transfer. Used during initial deployment and tuning phase (typically 30-90 days) to establish baseline and reduce false positives before enforcement.

**Block Mode (Enforce):**  
DLP solution prevents data transfer that violates policy (blocks email, denies upload, quarantines file). Used after tuning phase when false positive rate is acceptable (<10% target).

**Warn Mode (User Notification):**  
DLP solution notifies user of policy violation and allows user to proceed with justification or cancel action. Used for low-risk scenarios or user education purposes.

**Quarantine Mode:**  
DLP solution holds suspicious content for manual review by security team before allowing or blocking. Used for high-value data or ambiguous scenarios requiring human judgment.

**Encrypt Mode:**  
DLP solution forces encryption of sensitive data before allowing transfer. Used for approved data sharing with external parties (e.g., encrypted email to customers, encrypted file uploads).

### 3.3 Detection Methods

**Content Inspection:**  
Analysis of data content (file content, email body, web upload) using pattern matching, keywords, regular expressions, or machine learning to identify sensitive information.

**Contextual Analysis:**  
Analysis of data context (sender, recipient, destination, time, user role) to determine if transfer is authorized.  
*Example:* SSN sent to internal HR = low risk; SSN sent to external Gmail = high risk.

**Data Fingerprinting:**  
Creation of unique signatures (hashes, patterns) for sensitive documents or databases to detect unauthorized copying or transfer.

**Keyword Matching:**  
Search for specific words or phrases (e.g., "Confidential," "SSN," "Credit Card") in content.

**Pattern Matching (Regular Expressions):**  
Search for structured data patterns:
- SSN format: `\d{3}-\d{2}-\d{4}`
- Credit card: `\d{4}-\d{4}-\d{4}-\d{4}`
- IBAN: `[A-Z]{2}\d{2}[A-Z0-9]{1,30}`

**Machine Learning / AI:**  
Use of trained models to identify sensitive data based on statistical patterns, classification, or anomaly detection.

### 3.4 Roles and Responsibilities (Summary)

**Chief Information Security Officer (CISO):**  
Overall accountability for DLP program effectiveness and regulatory compliance.

**Information Security Officer (ISO):**  
Operational ownership of DLP policy framework, assessment coordination, and compliance monitoring.

**Security Engineering:**  
DLP technology deployment, configuration, rule tuning, and integration.

**IT Operations / SOC:**  
DLP solution maintenance, monitoring, alert triage, incident escalation, and user support.

**Data Owners:**  
Responsible for data classification decisions and DLP policy exceptions for their data domains.

**System Owners:**  
Responsible for DLP implementation within their systems and completion of quarterly assessments.

**Employees / Users:**  
Must comply with DLP policies, report incidents, and complete DLP awareness training annually.

**Data Protection Officer (DPO):**  
Legal compliance for employee monitoring (FADP/GDPR), proportionality assessment, transparency requirements.

**Works Council / Employee Representatives:**  
Co-determination rights for DLP monitoring deployment (jurisdiction-dependent: Switzerland, Germany, France, etc.).

*Detailed RACI matrix provided in ISMS-POL-A.8.12-S3 (Roles & Responsibilities).*

---

## 4. Regulatory Framework

### 4.1 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this ISMS are categorized as follows:

**Mandatory Compliance:**
- Swiss Federal Data Protection Act (FADP / nDSG)
- EU General Data Protection Regulation (GDPR) where applicable
- ISO/IEC 27001:2022
- ISO/IEC 27002:2022

**Informational Reference / Best Practice Alignment:**
- NIST Special Publications (SP 800-series)
- CIS Controls v8
- SANS Institute guidance

**United States Federal Requirements:**  
References to United States federal frameworks and regulations (including but not limited to FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply **only** where the organization:
- Acts as contractor, subcontractor, or service provider to US federal agencies
- Provides services to customers subject to such regulations
- Has explicit contractual obligations requiring such compliance

In all other cases, these references are provided for **informational or technical alignment purposes only** and do not constitute mandatory compliance requirements.

### 4.2 Key Regulatory Obligations

**Swiss FADP (Federal Data Protection Act):**
- **Article 26:** Transparency in data processing (employees must be informed of DLP monitoring)
- **Article 328b CO (Code of Obligations):** Employee monitoring restrictions (proportionality, legitimate interest, works council consultation where required)
- **Proportionality principle:** Monitoring must be necessary, appropriate, and minimal to achieve security objective
- **Employee rights:** Right to information, right to object (under certain conditions)

**EU GDPR (General Data Protection Regulation):**
- **Article 5:** Lawful processing (legitimate interest, necessity, transparency, purpose limitation)
- **Article 32:** Security measures (DLP as technical and organizational measure to ensure data security)
- **Article 13/14:** Information obligations (employees/data subjects must be informed of monitoring)
- **Article 35:** Data Protection Impact Assessment (DPIA may be required for systematic monitoring)
- **Recital 39:** Employee monitoring context (balance between employer interest and employee rights)

**ISO/IEC 27001:2022:**
- **Annex A Control 8.12:** Data leakage prevention measures SHALL be applied to systems, networks, and devices processing sensitive information

---

## 5. Legal and Privacy Considerations

### 5.1 Employee Monitoring and DLP

**Critical Legal Requirement:**  
DLP inherently involves employee monitoring (inspection of emails, file transfers, web activity, endpoint behavior). Organizations **MUST** comply with jurisdiction-specific employee monitoring laws.

**Swiss Law (FADP + Code of Obligations Art. 328b):**
- Employees MUST be informed of DLP monitoring (transparency requirement)
- Monitoring MUST be proportionate (security need vs. privacy intrusion)
- Monitoring MUST be limited to what is necessary (minimize scope and retention)
- Works council consultation MAY be required (jurisdiction-dependent, consult Legal/HR)
- Failure to comply = Potential CHF 50,000+ damages per violation, deployment injunction, works council challenge

**EU Law (GDPR):**
- Legal basis for monitoring MUST be established (legitimate interest, contractual necessity, or consent)
- Data Protection Impact Assessment (DPIA) SHOULD be conducted for systematic DLP monitoring
- Employees MUST be informed via privacy notice and employment contracts
- Monitoring data MUST be limited to security purposes (purpose limitation principle)
- Retention periods MUST be defined and documented (storage limitation principle)
- Employee rights MUST be respected (right of access, right to erasure under certain conditions)

**Organizational Requirements Before DLP Deployment:**
1. **Consult Legal/DPO** (mandatory before deployment)
2. **Conduct proportionality assessment** (document why DLP is necessary and proportionate)
3. **Draft employee notification** (clear, specific, transparent language in privacy notice)
4. **Update employment contracts** (monitoring clause, acceptable use policy acknowledgment)
5. **Consult works council if required** (jurisdiction-dependent: Switzerland, Germany, France, Belgium, Netherlands)
6. **Document all of the above** (audit evidence for compliance verification)

**Failure to comply with legal requirements = DLP deployment may be illegal, employees may refuse to work under unlawful monitoring, significant legal and financial liability.**

### 5.2 Proportionality Principle

DLP monitoring MUST be **proportionate** to the security risk:

**Proportionate Monitoring (Compliant):**
- Monitor egress channels for sensitive data only (email, web, endpoint, network)
- Focus on high-risk data (PII, financial, IP, credentials)
- Log DLP alerts with limited retention (e.g., 90 days for routine logs, 1 year for incident evidence)
- Limit access to DLP alerts to security team on need-to-know basis
- Deploy in monitor-only mode initially (observe before blocking)

**Disproportionate Monitoring (Non-Compliant):**
- Recording all email content indefinitely (excessive scope and retention)
- Monitoring all web browsing regardless of risk (excessive breadth)
- Allowing HR to browse DLP alerts for performance management (purpose creep, unauthorized access)
- Keystroke logging or screen recording without specific, documented justification (invasive)
- Monitoring personal devices for non-work activity (overreach)

**Proportionality Test:** Would a reasonable person consider this monitoring excessive given the security objective? If yes, it's disproportionate and likely non-compliant.

---

## 6. Integration with ISMS

### 6.1 Related ISO 27001 Controls

This DLP policy framework integrates with multiple ISO 27001 controls:

- **A.5.12 Classification of Information** - DLP protects data based on classification labels
- **A.5.15 Access Control** - DLP enforces access boundaries at egress points
- **A.5.24-28 Incident Management** - DLP alerts trigger security incident response process
- **A.5.34 Privacy and PII Protection** - DLP prevents unauthorized PII disclosure
- **A.8.10 Information Deletion** - DLP prevents unauthorized data retention on removable media
- **A.8.11 Data Masking** - Complementary data protection technique (mask before egress)
- **A.8.16 Monitoring Activities** - DLP generates security event logs for SIEM integration
- **A.8.23 Web Filtering** - Overlap on web channel data protection and exfiltration prevention
- **A.8.24 Cryptography** - Encryption complements DLP (encrypted channels may require special DLP handling)

### 6.2 Policy Framework Structure

This document (ISMS-POL-A.8.12-S1) is part of a modular policy framework for Data Leakage Prevention. The complete framework consists of:
```
ISMS-POL-A.8.12 (Master Policy Framework)
└── ISMS-POL-A.8.12-S1 (Purpose, Scope & Definitions) ← YOU ARE HERE
    ├── ISMS-POL-A.8.12-S2 (DLP Requirements Overview)
    │   ├── ISMS-POL-A.8.12-S2.1 (Data Classification & Identification)
    │   ├── ISMS-POL-A.8.12-S2.2 (Channel Protection Requirements)
    │   ├── ISMS-POL-A.8.12-S2.3 (Monitoring & Detection)
    │   └── ISMS-POL-A.8.12-S2.4 (Incident Response & Remediation)
    ├── ISMS-POL-A.8.12-S3 (Roles & Responsibilities)
    ├── ISMS-POL-A.8.12-S4 (Policy Governance)
    └── ISMS-POL-A.8.12-S5 (Annexes)
        ├── ISMS-POL-A.8.12-S5.A (DLP Channel Standards)
        ├── ISMS-POL-A.8.12-S5.B (Exception Request Template)
        ├── ISMS-POL-A.8.12-S5.C (Incident Response Procedures)
        └── ISMS-POL-A.8.12-S5.D (Quick Reference Guide)
```

Each section is independently versionable to support granular change management and targeted stakeholder reviews.

---

## 7. Document Maintenance

### 7.1 Review and Updates

This document shall be reviewed:
- **Annually** as part of the ISMS policy review cycle
- **Upon significant changes** to organizational risk profile, DLP technology, or regulatory requirements
- **Following security incidents** where data leakage gaps are identified
- **When new egress channels or data types** require policy adjustments

### 7.2 Change Management

Changes to this document require:
- Proposal with business/security justification
- Risk assessment of proposed changes
- Review by affected stakeholders (Legal/DPO, Security, IT Operations)
- Approval by Policy Owner (CISO)
- Communication to relevant personnel
- Update to related implementation documentation

### 7.3 Version Control

This document uses semantic versioning:
- **Major version (X.0):** Significant structural changes or scope modifications
- **Minor version (X.Y):** Content updates, clarifications, or additions without scope change

All versions are retained in the organization's document management system with full change history.

---

## 8. References

### 8.1 Normative References (Mandatory)

- ISO/IEC 27001:2022 - Information Security Management Systems (Requirements)
- ISO/IEC 27002:2022 - Information Security Controls (Control 8.12 implementation guidance)
- Swiss Federal Data Protection Act (FADP / nDSG) - Data protection and employee monitoring
- Swiss Code of Obligations (OR) Article 328b - Employee monitoring restrictions
- EU General Data Protection Regulation (GDPR) - Data protection and privacy

### 8.2 Informative References

- NIST SP 800-53 Rev. 5 - Security and Privacy Controls (SC-7 Boundary Protection, AC-4 Information Flow Enforcement, SI-4 System Monitoring)
- NIST SP 800-171 - Protecting Controlled Unclassified Information
- CIS Controls v8 - Control 13 (Network Monitoring and Defense)

### 8.3 Internal References

- ISMS-POL-A.5.12 - Classification of Information (data classification schema)
- ISMS-POL-A.5.15 - Access Control (authorization framework)
- ISMS-POL-A.8.16 - Monitoring Activities (logging and SIEM integration)
- ISMS-POL-A.8.23 - Web Filtering (overlap on web channel protection)
- ISMS-IMP-A.8.12.1-5 - DLP Assessment Workbooks (implementation evidence)

---

**END OF DOCUMENT**

*"The purpose of DLP is not to stop all data transfer - it's to prevent unauthorized data transfer while enabling legitimate business operations. Intelligence, not theater."*