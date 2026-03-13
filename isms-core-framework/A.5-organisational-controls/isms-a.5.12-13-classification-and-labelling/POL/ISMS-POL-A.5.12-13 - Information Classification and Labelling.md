<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.12-13:framework:POL:a.5.12-13 -->
**ISMS-POL-A.5.12-13 — Information Classification and Labelling**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Classification and Labelling |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.12-13 |
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
- Secondary: Data Protection Officer (DPO)
- Final Authority: Executive Management

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.9 (Inventory of Information and Assets)
- ISMS-POL-A.5.14 (Information Transfer)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- ISMS-POL-A.8.10 (Information Deletion)
- ISMS-POL-A.8.12 (Data Leakage Prevention)
- ISMS-IMP-A.5.12-13.S1-UG/TG (Classification Scheme Definition)
- ISMS-IMP-A.5.12-13.S2-UG/TG (Labelling Procedures and Standards)
- ISMS-IMP-A.5.12-13.S3-UG/TG (Asset Classification Inventory)
- ISO/IEC 27001:2022 Controls A.5.12, A.5.13

---

## Executive Summary

This policy establishes [Organisation]'s information classification scheme and labelling requirements to ensure that information receives an appropriate level of protection according to its sensitivity, value, and legal requirements.

**Scope**: This policy applies to all information created, received, processed, stored, or transmitted by [Organisation], regardless of format (electronic, physical, verbal).

**Purpose**: Define organisational requirements for information classification and labelling. This policy establishes WHAT classification levels apply and WHO is responsible. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.12-13 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, Swiss Banking Secrecy) apply where [Organisation]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Controls A.5.12 and A.5.13**

**ISO/IEC 27001:2022 Annex A.5.12 - Classification of Information**

> *Information should be classified according to the information security needs of the organisation based on confidentiality, integrity, availability and relevant interested party requirements.*

**ISO/IEC 27001:2022 Annex A.5.13 - Labelling of Information**

> *An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organisation.*

**Control Objectives**:

- Establish consistent classification across all information types
- Enable appropriate handling based on sensitivity
- Meet regulatory requirements for data protection
- Support access control and data protection decisions

**Control Type**: Preventive
**Control Category**: Organisational

**This Policy Addresses**:

- Classification scheme and level definitions
- Classification responsibility assignments
- Labelling requirements for all information formats
- Handling requirements per classification level
- Reclassification and declassification procedures

## What This Policy Does

This policy:

- **Defines** the four-tier classification scheme for all organisational information
- **Establishes** criteria for classification decisions based on impact analysis
- **Specifies** labelling requirements for electronic and physical formats
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Specify labelling templates and tools** (see ISMS-IMP-A.5.12-13 Implementation Guidance)
- **Define classification workflow procedures** (see ISMS-IMP-A.5.12-13 Procedures)
- **Provide training materials** (see ISMS-IMP-A.5.12-13 Training)
- **Replace data protection impact assessments** (see ISMS-POL-A.5.34)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite tool or process changes
- Flexibility for different labelling technologies
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All information created, received, processed, stored, or transmitted by [Organisation]
- All formats: electronic documents, physical documents, databases, verbal communications
- All personnel (employees, contractors, third parties) handling organisational information
- All systems and applications processing organisational data

**Out of Scope**:

- Personal information held by employees for personal purposes
- Public information already in the public domain with no sensitivity
- Third-party information classified by external parties (follow their classification)

Where an external party's classification scheme differs from [Organisation]'s four-tier scheme, the Information Owner SHALL map it to the nearest higher [Organisation] classification level and document the mapping.

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All personal data processing | Appropriate technical and organisational measures |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.5.12, A.5.13 - Classification and labelling |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Classification Requirements |
|-----------|-------------------|---------------------------|
| **EU GDPR Art. 32** | Processing EU personal data | Security appropriate to sensitivity of personal data |
| **FINMA** | Swiss regulated financial institution | Client data classification requirements |
| **Swiss Banking Secrecy** | Bank client data | Strict confidentiality classification |
| **Government contracts** | Public sector work | May require additional classification levels |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ISO 27002:2022 Implementation Guidance for A.5.12-13
- NIST SP 800-53 (Security Categorization)
- CIS Controls v8.1 (Data Classification and Protection)
- Government classification schemes (for reference in public sector work)

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent classification requirements apply where multiple regulations overlap.

---

# Policy Statements

## Classification Scheme

### Classification Levels

[Organisation] adopts a four-tier classification scheme:

| Level | Label | Description | Examples |
|-------|-------|-------------|----------|
| **Public** | PUBLIC | Information approved for unrestricted disclosure | Marketing materials, press releases, public website content |
| **Internal** | INTERNAL | Information for internal use only, not for external distribution | Internal procedures, org charts, general business communications |
| **Confidential** | CONFIDENTIAL | Sensitive information requiring protection, limited distribution | Customer data, contracts, financial reports, HR records |
| **Restricted** | RESTRICTED | Highly sensitive information, strict access control | Trade secrets, M&A data, security configurations, cryptographic keys |

### Classification Criteria

Information SHALL be classified based on:

**Confidentiality Impact** (if disclosed):

| Impact Level | Criteria | Minimum Classification |
|--------------|----------|------------------------|
| None | No adverse impact | Public |
| Low | Minor inconvenience | Internal |
| Moderate | Significant harm to operations or reputation | Confidential |
| High | Severe damage, regulatory penalties, existential threat | Restricted |

**Regulatory Requirements**:

| Data Type | Minimum Classification |
|-----------|------------------------|
| Personal data (non-sensitive) | Confidential |
| Special category personal data | Restricted |
| Financial records (customer) | Confidential |
| Health information | Restricted |
| Cryptographic materials | Restricted |

**Integrity and Availability Requirements**:

- Information requiring high integrity (financial, legal) → minimum Confidential
- Information requiring high availability (critical operations) → consider availability protection measures

### Default Classification

- **Unclassified information**: Treated as INTERNAL until formally classified
- **External information**: Classified upon receipt based on content and sender's classification
- **Aggregated information**: Classified at highest level of component data

## Classification Responsibilities

### Information Owners

Information Owners SHALL:

- Classify information upon creation or receipt
- Review classification when information content changes
- Authorise access appropriate to classification level
- Ensure subordinates understand classification responsibilities
- Review and update classification annually or upon trigger event

### Classification Authority

| Classification Level | Who May Classify | Who May Declassify |
|---------------------|------------------|---------------------|
| Public | Information Owner | Information Owner |
| Internal | Information Owner | Information Owner |
| Confidential | Information Owner, Department Head | Information Owner, Department Head |
| Restricted | Department Head, Executive Management | Executive Management only |

### Reclassification

Information SHALL be reclassified when:

- Business value or sensitivity changes
- Legal/regulatory requirements change
- Time-based declassification applies (e.g., after public announcement)
- Information Owner determines different classification appropriate

**Declassification Process**:

- Document reason for declassification
- Obtain required approval per classification authority
- Update labels on all instances
- Notify recipients of reclassified information

Classification and declassification decisions for RESTRICTED information SHALL be recorded (owner, approver, date, rationale, affected locations) in the Evidence Register or designated workflow system.

## Labelling Requirements

### Mandatory Labelling

All information classified CONFIDENTIAL or RESTRICTED SHALL be clearly labelled.

**Electronic Documents**:

- Header and/or footer on each page: "CONFIDENTIAL" or "RESTRICTED"
- Document properties/metadata including classification
- Email subject line prefix for sensitive emails: [CONFIDENTIAL] or [RESTRICTED]
- File naming convention to include classification where practical

**Physical Documents**:

- Classification label on cover page
- Classification marking on each page (header or footer)
- Sealed containers labelled with highest classification of contents
- Archive boxes marked with classification level

**Other Formats**:

| Format | Labelling Method |
|--------|------------------|
| Removable media | Physical label + encrypted with classification metadata |
| Databases | Classification field per record or table-level designation |
| Verbal communications | Verbal statement of classification before discussing |
| Presentations | Classification on title slide and each subsequent slide |

### Labelling Exceptions

PUBLIC and INTERNAL information:

- Labelling recommended but not mandatory
- Unlabelled information is treated as INTERNAL only within approved internal systems with access controls
- Any information shared externally or stored in shared collaboration repositories SHALL have an explicit classification applied when CONFIDENTIAL or RESTRICTED
- Unlabelled sensitive content detected by DLP monitoring or periodic scans SHALL be handled as a nonconformity or recorded as an exception with compensating controls

### Automated Labelling

Where technically feasible, [Organisation] SHALL implement:

- Auto-classification based on content patterns (DLP rules)
- Inheritance of classification from parent folders/systems
- Mandatory classification prompts before saving/sending
- Integration with Microsoft Information Protection or equivalent

## Handling Requirements

### Per-Classification Handling Matrix

| Requirement | PUBLIC | INTERNAL | CONFIDENTIAL | RESTRICTED |
|-------------|--------|----------|--------------|------------|
| **Storage** | Any | Corporate systems | Encrypted storage | Encrypted, access-logged |
| **Transmission** | Any | Corporate email | Encrypted | Encrypted, secure channel |
| **Printing** | Unrestricted | Standard | Secure print queue | Authorised printer only |
| **Disposal** | Standard | Shredding (P-3) | Cross-cut shredding (P-4) | Cross-cut (P-5) + witness |
| **Access** | Anyone | Employees | Need-to-know | Named individuals |
| **Copying** | Unrestricted | Permitted | Owner approval | Not permitted (exceptions require GL) |
| **External sharing** | Permitted | Not without approval | NDA required | Prohibited (exceptions require GL) |

### Physical Security

| Classification | Physical Control |
|----------------|------------------|
| Public | No special requirements |
| Internal | Secured premises |
| Confidential | Locked storage when unattended |
| Restricted | Secure container (safe/vault), access log |

### Digital Security

| Classification | Technical Control |
|----------------|------------------|
| Public | Standard backup |
| Internal | Access control, backup |
| Confidential | Encryption at rest, access control, audit logging |
| Restricted | Strong encryption, MFA access, comprehensive audit, DLP |

Encryption and logging requirements SHALL meet the minimum standards defined in ISMS-POL-A.8.24 (cryptography) and ISMS-POL-A.8.15/A.8.16 (logging/monitoring). For CONFIDENTIAL and RESTRICTED information, encryption at rest SHALL be verifiable via platform encryption status reports or configuration baselines. Access logs SHALL be forwarded to the central logging platform with retention per ISMS-POL-A.8.15 and quarterly review evidence.

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Classification Responsibilities |
|------|--------------------------------|
| **Executive Management** | Approve classification scheme, authorise Restricted declassification |
| **CISO** | Define classification requirements, monitor compliance, manage labelling tools |
| **DPO** | Ensure personal data classification meets regulatory requirements |
| **Information Owners** | Classify and label information, authorise access, review classifications |
| **Department Heads** | Ensure departmental compliance, Confidential/Restricted classification authority |
| **All Personnel** | Handle information per classification, report misclassified information |

## Escalation Path

- Classification disputes: Information Owner → Department Head → CISO
- Uncertain classification: Classify at higher level, seek clarification from CISO
- Suspected misclassification: Report to Information Owner and CISO

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Classification compliance audit | Annual | Internal Audit | Audit reports |
| Labelling tool effectiveness review | Quarterly | CISO | Tool reports |
| Classification scheme review | Annual | CISO | Scheme documentation |
| Information Owner training completion | Annual | HR | Training records |

**Governance Metrics**:

- Information assets with assigned classification (target: ≥95% classified with documented exceptions; 100% for systems in certification scope)
- Labelling compliance for Confidential/Restricted (target: ≥95%, exceptions must be time-bound with compensating controls)
- Classification audit findings (target: decreasing trend quarter-over-quarter)
- Training completion rate (target: 100%)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, business model changes, audit findings
- **Reviewers**: CISO, DPO, Legal Counsel, Department Heads
- **Approval**: Executive Management

## Exception Management

**Labelling Exceptions**:

- Legacy systems where labelling technically infeasible: Document in exception register, implement compensating controls
- High-volume automated data: Classification rules applied at system/dataset level

**Handling Exceptions**:

- Emergency situations may permit deviation with immediate documentation and post-event review
- Requires CISO approval and compensating controls

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., missing labels, misclassified information, handling violations) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organisation]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Classification levels aligned with [Organisation]'s risk assessment and impact analysis
- Handling requirements determined by confidentiality, integrity, and availability impacts
- Risk treatment plans document classification scheme implementation

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.5.12 and A.5.13 applicability justified in [Organisation]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Integration Point |
|---------|-------------------|
| **A.5.9** | Inventory of Information and Assets - Assets classified according to this scheme |
| **A.5.14** | Information Transfer - Transfer methods determined by classification |
| **A.5.34** | Privacy and PII Protection - Personal data classification requirements |
| **A.8.10** | Information Deletion - Deletion methods per classification level |
| **A.8.12** | Data Leakage Prevention - DLP rules enforce classification boundaries |
| **A.8.24** | Use of Cryptography - Encryption requirements per classification |

**Bidirectional Data Flows**:

**Classification → Other Controls**:

- Classification decisions → Access control (A.5.15): Need-to-know requirements based on sensitivity
- Classification labels → DLP (A.8.12): Automated policy enforcement
- Classification level → Transfer methods (A.5.14): Approved channels per sensitivity

**Other Controls → Classification**:

- Asset inventory (A.5.9) → Classification coverage: All assets require classification
- Incident lessons learned → Classification review: Post-incident reclassification where needed
- Regulatory changes → Classification updates: New requirements for personal data categories

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.12-13 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.12-13-UG/TG** | Classification and Labelling Implementation Guide | Detailed procedures, templates, and tools |

**Cross-References**:

- ISMS-POL-A.5.9 for asset inventory requirements
- ISMS-POL-A.5.14 for transfer handling per classification
- ISMS-POL-A.8.12 for DLP enforcement

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- ✅ This policy document (ISMS-POL-A.5.12-13 v1.0)
- ✅ Recorded approval by CISO, DPO, Executive Management
- ✅ Evidence of communication to relevant roles
- ✅ Classification scheme with level definitions documented (Classification Scheme)
- ✅ Labelling requirements specified (Labelling Requirements)
- ✅ Handling requirements per classification level defined (Handling Requirements)
- ✅ Information Owner responsibilities documented (Classification Responsibilities)
- ✅ Roles and responsibilities assigned (Roles and Responsibilities)

Evidence status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Sample classified documents with appropriate labels
- Classification tool reports (e.g., Microsoft Information Protection)
- Information asset inventory with classification assignments
- Training completion records for classification responsibilities
- Audit reports on classification compliance
- Reclassification/declassification records
- Exception register for labelling/handling exceptions
- Incident reports involving misclassified information (if any)

---

# Definitions

| Term | Definition |
|------|------------|
| **Classification** | The process of categorizing information based on its sensitivity and the potential impact of unauthorised disclosure, modification, or unavailability |
| **Labelling** | The application of visible or metadata markers to information indicating its classification level |
| **Information Owner** | The individual or role accountable for the classification, handling, and protection of specific information assets |
| **Need-to-Know** | A principle that restricts access to information to those who require it to perform their job functions |
| **Declassification** | The reduction of a classification level when information no longer requires the higher level of protection |
| **Aggregation** | The combination of multiple pieces of information that, together, may require higher classification than individual components |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Data Protection Officer (DPO)** | [Name] | [Date to be set] |
| **Executive Management** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for information classification and labelling. Implementation procedures are documented in ISMS-IMP-A.5.12-13 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-01 -->
