**ISMS-POL-A.5.14 — Information Transfer**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Transfer |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.14 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling)
- ISMS-POL-A.8.24 (Use of Cryptography)
- ISMS-POL-A.5.19-23 (Cloud Services)
- ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements)
- ISMS-IMP-A.5.14.1-UG/TG (Transfer Rules and Procedures)
- ISMS-IMP-A.5.14.2-UG/TG (Channel Security Assessment)
- ISMS-IMP-A.5.14.3-UG/TG (Transfer Agreements Register)
- ISMS-IMP-A.5.14.4-UG/TG (Compliance Monitoring Dashboard)
- ISMS-IMP-A.5.14.5-UG/TG (Consolidation Dashboard)
- ISO/IEC 27001:2022 Control A.5.14

---

## Executive Summary

This policy establishes [Organization]'s requirements for secure information transfer to protect information during transmission through all types of communication channels and facilities.

**Scope**: This policy applies to all information transfers, whether electronic, physical, or verbal, including transfers within [Organization] and with external parties.

**Purpose**: Define organizational requirements for information transfer security. This policy establishes WHAT transfer methods are approved and WHO is authorized. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.14 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, PCI DSS) apply where [Organization]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Control A.5.14**

**ISO/IEC 27001:2022 Annex A.5.14 - Information Transfer**

> *Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties.*

**Control Objectives**:

- Protect information confidentiality, integrity, and availability during transfer
- Ensure appropriate transfer methods based on information sensitivity
- Establish transfer agreements with external parties
- Maintain accountability and audit trails for transfers

**Control Type**: Preventive
**Control Category**: Organizational

**This Policy Addresses**:

- Approved transfer methods and channels
- Transfer requirements per information classification
- External transfer agreements and requirements
- Transfer authorization and accountability
- Incident handling for transfer failures

## What This Policy Does

This policy:

- **Defines** approved transfer methods for each classification level
- **Establishes** requirements for external and cross-border transfers
- **Specifies** authorization requirements for different transfer types
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Specify encryption tool configurations** (see ISMS-IMP-A.5.14 and ISMS-POL-A.8.24)
- **Define file transfer platform procedures** (see ISMS-IMP-A.5.14)
- **Provide secure email gateway administration** (operational documentation)
- **Detail physical courier engagement** (see ISMS-IMP-A.5.14)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite technology or platform changes
- Flexibility for different transfer solutions
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All information transfers (electronic, physical, verbal)
- All transfer methods (email, file sharing, courier, in-person)
- All personnel (employees, contractors, third parties) transferring organizational information
- All external transfers to customers, partners, vendors, and regulatory bodies

**Out of Scope**:

- Personal communications unrelated to organizational information
- Public information already freely available
- Real-time database replication (covered by system architecture)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG Art. 16-17** | All personal data transfers | Cross-border transfer requirements |
| **ISO/IEC 27001:2022** | Certification scope | Control A.5.14 - Information transfer |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Transfer Requirements |
|-----------|-------------------|----------------------|
| **EU GDPR Art. 44-49** | Processing EU personal data | International data transfer safeguards, SCCs |
| **FINMA** | Swiss regulated financial institution | Enhanced security for financial data transfers |
| **Swiss Banking Secrecy** | Bank client data | Strict transfer controls |
| **PCI DSS** | Payment card data | Encryption requirements for cardholder data |
| **HIPAA** | US health data | Business Associate Agreements |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ISO 27002:2022 Implementation Guidance for A.5.14
- NIST SP 800-53 (System and Communications Protection)
- CIS Controls v8 (Data Protection)
- ENISA Guidelines on Data Transfer Security

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent transfer requirements apply where multiple regulations overlap.

---

# Policy Statements

## Transfer Method Requirements

### Electronic Transfer

**Email Communications**:

| Classification | Requirement |
|----------------|-------------|
| PUBLIC | Standard corporate email permitted |
| INTERNAL | Corporate email only, external recipients require recorded business justification (purpose, recipient, classification, access expiry) |
| CONFIDENTIAL | Encrypted email (TLS enforced) or secure file sharing platform |
| RESTRICTED | End-to-end encrypted platform, recipient verification required |

**Email Security Controls**:

- Transport Layer Security (TLS) mandatory for all outbound email
- S/MIME or equivalent for CONFIDENTIAL/RESTRICTED attachments
- Email size limits enforced (attachments >25MB via secure file sharing)
- DLP policies active for sensitive data pattern detection
- External recipient warnings displayed before sending

**File Transfer**:

| Method | Permitted Use | Classification Limit |
|--------|--------------|---------------------|
| Corporate file sharing (SharePoint/OneDrive) | Internal transfers | Up to RESTRICTED |
| Secure file transfer platform | External transfers | Up to RESTRICTED |
| SFTP/SCP | System integrations | Up to CONFIDENTIAL |
| USB drives (encrypted) | Exception only | Up to CONFIDENTIAL |
| Public file sharing (Dropbox, Google Drive) | Never for corporate data | PUBLIC only (personal use) |

**Web-Based Transfer**:

- HTTPS required for all web transfers
- Certificate validation mandatory
- CONFIDENTIAL and RESTRICTED information SHALL only be transferred via approved web-based services listed in the Approved Transfer Tools Register; other destinations require an approved exception (ISMS-REG-EXCEPTIONS)
- Secure upload portals for customer data submission

### Physical Transfer

**Document Transfer**:

| Classification | Transfer Method |
|----------------|-----------------|
| PUBLIC | Standard mail or courier |
| INTERNAL | Internal mail or standard courier |
| CONFIDENTIAL | Sealed envelope, tracked courier, recipient signature |
| RESTRICTED | Double-sealed package, bonded courier, chain of custody documentation |

**Media Transfer** (USB, hard drives, backup tapes):

- All removable media encrypted before transfer
- Media inventory logged with tracking number
- Secure courier with chain of custody for CONFIDENTIAL+
- RESTRICTED media: dedicated secure courier, tamper-evident packaging

**In-Person Transfer**:

- Verify recipient identity before handover
- Document transfer with receipt acknowledgment
- RESTRICTED information: witness presence required

### Verbal Transfer

**Telephone/Video Communications**:

| Classification | Requirement |
|----------------|-------------|
| PUBLIC/INTERNAL | Standard corporate systems |
| CONFIDENTIAL | Verified participants, no recording without consent |
| RESTRICTED | Secure/encrypted channels only, participant verification |

**In-Person Discussions**:

- CONFIDENTIAL: Private location, no unauthorized listeners
- RESTRICTED: Secure room, no electronic devices, need-to-know participants only

## External Transfer Requirements

### Transfer Agreements

External transfers of INTERNAL or higher classification SHALL require:

**Minimum Agreement Elements**:

- Information handling obligations for recipient
- Permitted use and disclosure restrictions
- Return/destruction requirements
- Breach notification obligations
- Audit rights where appropriate

**Agreement Types**:

| Transfer Type | Required Agreement |
|--------------|-------------------|
| One-time transfer | Confidentiality acknowledgment |
| Ongoing relationship | NDA (per ISMS-POL-A.6.6) |
| Supplier/vendor | Data Processing Agreement (where personal data involved) |
| Customer data | Service agreement with security terms |

### Cross-Border Transfers

Transfers outside Switzerland/EEA SHALL comply with:

**Legal Requirements**:

- Adequacy decision verification (country assessment)
- Standard Contractual Clauses (SCCs) where required
- Supplementary measures for high-risk jurisdictions; for cross-border transfers of personal data, an International Transfer Assessment record SHALL be completed and stored in the Evidence Register (including adequacy/SCC basis, supplementary measures decision, and DPO approval reference)
- DPO approval for personal data transfers

**Technical Requirements**:

- Encryption in transit mandatory
- Data residency compliance verification
- Transfer logging and monitoring

**Prohibited Destinations**:

- Countries subject to sanctions
- Jurisdictions without adequate legal protections (without appropriate safeguards)

### Customer and Third-Party Data

Special handling for data belonging to external parties:

- Classification: Minimum CONFIDENTIAL for all customer data
- Transfer: Per customer contract requirements
- Documentation: Transfer logs retained per contractual/regulatory requirements
- Notification: Inform data owners of transfers where required by contract

## Transfer Controls

### Authorization

**Transfer Authorization Matrix**:

| Classification | Internal Transfer | External Transfer |
|----------------|-------------------|-------------------|
| PUBLIC | Self-authorized | Self-authorized |
| INTERNAL | Self-authorized | Manager approval |
| CONFIDENTIAL | Manager approval | Information Owner + Manager |
| RESTRICTED | Department Head | Department Head + CISO |

### Logging and Accountability

All CONFIDENTIAL and RESTRICTED transfers SHALL be logged:

**Log Contents**:

- Date/time of transfer
- Sender and recipient identification
- Information description (not content)
- Transfer method used
- Authorization reference

**Retention**: Transfer logs retained for minimum 2 years.

### Incident Response

Transfer failures or suspected compromises:

- Immediate notification to CISO for CONFIDENTIAL+
- Investigation per ISMS-POL-A.5.24-28 (Incident Management)
- Notification to data owner/Information Owner
- Regulatory and contractual notifications for personal data breaches SHALL be handled through the incident management process (ISMS-POL-A.5.24-28) and the organisation's privacy breach notification procedure, based on ISMS-POL-00 applicability decisions

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Transfer Responsibilities |
|------|--------------------------|
| **Executive Management** | Approve transfer policy, authorize RESTRICTED external transfers |
| **CISO** | Define transfer requirements, approve transfer platforms, incident oversight |
| **IT Operations** | Implement secure transfer infrastructure, manage platforms |
| **Information Owners** | Authorize transfers of owned information, verify recipient appropriateness |
| **Department Heads** | Approve departmental transfers, ensure compliance |
| **All Personnel** | Use approved transfer methods, protect information during transfer |

## Escalation Path

- Transfer method uncertainty: Personnel → Manager → CISO
- External transfer approval: Information Owner → Department Head → CISO (RESTRICTED)
- Transfer incident: Personnel → CISO → Executive Management (significant incidents)

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Transfer platform security review | Quarterly | IT Operations | Platform reports |
| DLP policy effectiveness | Monthly | CISO | DLP reports |
| Cross-border transfer compliance | Quarterly | DPO | Compliance records |
| Transfer agreement inventory | Annual | Legal Counsel | Agreement register |

**Governance Metrics**:

- Approved transfer method usage (target: 100%)
- DLP incident remediation time (target: <24 hours)
- Cross-border transfer compliance (target: 100%)
- Transfer agreement coverage (target: 100% for ongoing relationships)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: New transfer technologies, regulatory changes, security incidents
- **Reviewers**: CISO, DPO, IT Operations, Legal Counsel
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Alternative transfer method when approved method unavailable (with compensating controls)
- Emergency transfers with post-facto documentation within 24 hours
- Legacy system transfers with documented mitigation plan

**Exception Process**:

1. Request exception with business justification
2. Risk assessment of alternative method
3. Document compensating controls
4. CISO approval required for CONFIDENTIAL+
5. Time-limited approval (maximum 90 days)

**Not Permissible**:

- Transfer of RESTRICTED information via unapproved channels
- Cross-border transfers without legal basis
- Persistent use of insecure transfer methods

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., unapproved transfer methods, missing agreements, cross-border violations) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Transfer controls selected based on [Organization]'s risk assessment
- Information classification determines minimum transfer security requirements
- Risk treatment plans document transfer control implementation

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.5.14 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

- A.5.12-13 (Information Classification and Labelling): Determines transfer security requirements
- A.5.19-23 (Cloud Services): Cloud-based transfer platform requirements
- A.6.6 (Confidentiality and Non-Disclosure Agreements): External transfer agreements
- A.8.24 (Use of Cryptography): Encryption standards for transfers
- A.8.12 (Data Leakage Prevention): DLP controls for transfer monitoring
- A.8.15 (Logging): Transfer activity logging requirements

**Stacked Control Integration**:

A.5.14 (Information Transfer) stacks with related controls to provide comprehensive protection:

| Stacked Control | Integration Point | A.5.14 Contribution |
|-----------------|-------------------|---------------------|
| **A.5.12-13** (Classification) | Classification-based handling | A.5.14 specifies transfer methods per classification level |
| **A.8.24** (Cryptography) | Encryption in transit | A.5.14 mandates encryption; A.8.24 specifies algorithms |
| **A.8.12** (DLP) | Content inspection | A.5.14 defines transfer channels; A.8.12 monitors for policy violations |

Assessment of A.5.14 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Document Structure** (ISMS-IMP-A.5.14 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.14-UG/TG** | Information Transfer Implementation Guide | Detailed procedures for secure information transfer |

**Cross-References**:

- ISMS-POL-A.8.24 for cryptographic requirements
- ISMS-POL-A.5.12-13 for classification requirements
- ISMS-IMP-A.5.14 for detailed transfer procedures

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- ✅ This policy document (ISMS-POL-A.5.14 v1.0)
- ✅ Recorded approval by CISO, CIO, Executive Management
- ✅ Evidence of communication to relevant roles
- ✅ Approved transfer methods defined (Transfer Method Requirements)
- ✅ External transfer requirements documented (External Transfer Requirements)
- ✅ Cross-border transfer requirements specified (Cross-Border Transfers)
- ✅ Transfer authorization matrix defined (Transfer Controls)
- ✅ Roles and responsibilities assigned (Roles and Responsibilities)

Evidence status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Transfer logs for CONFIDENTIAL/RESTRICTED transfers
- Sample external transfer agreements (redacted)
- DLP incident reports and remediation
- Secure file sharing platform access logs
- Email security gateway reports (TLS enforcement)
- Cross-border transfer documentation (SCCs, adequacy assessments)
- Training records for transfer procedures
- Exception register with approvals

---

# Definitions

| Term | Definition |
|------|------------|
| **Information Transfer** | The movement of information from one location, system, or person to another through any means |
| **Transfer Facility** | Any technology, equipment, or service used to transmit information (email systems, file sharing, couriers, etc.) |
| **Cross-Border Transfer** | Transfer of information to a recipient in a different country/jurisdiction |
| **Standard Contractual Clauses (SCCs)** | EU Commission-approved contract terms for international data transfers |
| **Chain of Custody** | Documented record of all individuals who handled information during physical transfer |
| **End-to-End Encryption** | Encryption where only the sender and intended recipient can decrypt the information |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for information transfer. Implementation procedures are documented in ISMS-IMP-A.5.14 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->
