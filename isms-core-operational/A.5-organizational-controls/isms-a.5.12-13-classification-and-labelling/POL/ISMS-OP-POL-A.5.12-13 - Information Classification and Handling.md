<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.12-13:operational:OP-POL:a.5.12-13 -->
**ISMS-OP-POL-A.5.12-13 — Information Classification and Handling**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Classification and Handling |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.12-13 |
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

- ISO/IEC 27001:2022 Controls A.5.12, A.5.13 — Classification of information, labelling of information

**Related Annex A Controls**:

| Control | Relationship to Information Classification |
|---------|-------------------------------------------|
| A.5.9 Inventory of information and other associated assets | Classification assigned to inventoried information assets |
| A.5.10 Acceptable use of information | Acceptable use rules enforce handling requirements per classification |
| A.5.14 Information transfer | Transfer method determined by classification level |
| A.5.15–18 Access control and identity management | Access rights granted based on classification and need-to-know |
| A.5.33 Protection of records | Records retention and protection aligned with classification |
| A.5.34 Privacy and protection of PII | Personal data classification and handling requirements |
| A.7.10 Storage media | Media handling and disposal per classification |
| A.7.14 Secure disposal or re-use of equipment | Disposal standards determined by classification |
| A.8.10 Information deletion | Secure deletion standards per classification level |
| A.8.11 Data masking | Masking of classified data in non-production environments |
| A.8.12 Data leakage prevention | DLP controls enforce classification handling rules |
| A.8.24 Use of cryptography | Encryption requirements determined by classification |

**Related Internal Policies**:

- Asset Management Policy
- Access Control Policy
- Information Transfer Policy
- Use of Cryptography Policy
- Privacy and Protection of PII Policy
- Acceptable Use Policy

---

# Information Classification and Handling Policy

## Purpose

The purpose of this policy is to ensure the correct classification and handling of information based on its sensitivity, value, and legal requirements, so that information receives an appropriate level of protection throughout its lifecycle.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) through classification-based controls. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All information in any format (digital, physical, verbal) that forms part of systems and applications deemed in scope by the ISO 27001 scope statement.

## Principle

Information shall be classified in terms of legal requirements, value, criticality, and sensitivity to unauthorised disclosure or modification. Classification determines the handling controls applied throughout the information lifecycle — from creation through storage, transmission, and destruction.

---

## Classification Scheme

Information shall be classified into one of three levels:

| Level | Description | Impact of Unauthorised Disclosure |
|-------|-------------|-----------------------------------|
| **CONFIDENTIAL** | Information whose disclosure would cause significant harm to the organisation, its customers, or data subjects. Includes legally protected data. | Severe financial loss, regulatory penalties, legal action, significant reputational damage, high risk to data subjects |
| **INTERNAL** | Information intended for use within the organisation. Not intended for public disclosure. | Minor operational inconvenience, minor embarrassment, limited reputational impact |
| **PUBLIC** | Information approved for public release. Disclosure causes no harm. | No adverse impact |

**Default classification**: Information that has not been explicitly classified shall be treated as **INTERNAL** until classified by its owner.

### Classification by Information Type

| Information Type | Minimum Classification |
|------------------|----------------------|
| **Sensitive personal data** (nFADP Art. 5: health, racial/ethnic origin, religious/political beliefs, criminal records, genetic data, biometric data) | **CONFIDENTIAL** |
| **Personal data** (names, email addresses, phone numbers, employee records) | **INTERNAL** (minimum); **CONFIDENTIAL** if volume >1,000 records or combined with sensitive categories |
| **Financial records** (accounts, transactions, salary information, bank details) | **CONFIDENTIAL** |
| **Trade secrets and intellectual property** (proprietary methods, source code, designs, formulas) | **CONFIDENTIAL** |
| **Passwords, cryptographic keys, credentials** | **CONFIDENTIAL** |
| **Contracts and legal agreements** | **CONFIDENTIAL** |
| **Internal policies, procedures, meeting minutes** | **INTERNAL** |
| **Organisation charts, internal communications** | **INTERNAL** |
| **Marketing materials, press releases, published content** | **PUBLIC** |
| **Information already in the public domain** | **PUBLIC** |

### Classification Responsibilities

- **Information owners** (as defined in the Asset Management Policy) are responsible for classifying their information assets.
- Classification shall be assigned when information is created or received.
- Classification shall be reviewed when information is significantly modified, shared with new parties, or when business circumstances change.
- Over-classification shall be avoided — classifying everything as CONFIDENTIAL dilutes the meaning and wastes resources.
- **Aggregation risk**: Information that is individually classified as INTERNAL may require reclassification to CONFIDENTIAL when combined with other datasets, if the aggregation creates a materially higher risk of harm (e.g., combining names with health conditions, or combining individual salary records into a department-wide compensation report). Information owners shall consider aggregation risk when classifying datasets.

---

## Information Labelling

### Labelling Requirements

All information shall be labelled according to its classification level:

| Format | Labelling Method |
|--------|-----------------|
| **Digital documents** (Word, PDF, Excel) | Classification in the document header or footer on every page (e.g., "CONFIDENTIAL") |
| **Email** | Classification prefix in the subject line (e.g., "[CONFIDENTIAL] Subject") |
| **Physical documents** | Classification on the cover page; header or footer on subsequent pages |
| **Physical media** (USB drives, backup tapes) | Physical label affixed to the device or container |
| **File metadata** | Classification recorded in file properties or document management system metadata |
| **Database records** | Classification column or metadata tag per dataset |

**PUBLIC** information does not require a classification label unless published on internal platforms where its public status may be unclear.

**Unmarked information** shall be treated as **INTERNAL** by default.

Where the organisation uses Microsoft 365 or equivalent platforms, sensitivity labels should be configured to automate classification enforcement, including encryption, access restrictions, and visual markings.

---

## Information Handling

### Handling Matrix

| Handling Aspect | PUBLIC | INTERNAL | CONFIDENTIAL |
|-----------------|--------|----------|--------------|
| **Digital storage** | No restrictions | Organisation-managed systems only; not on personal devices without MDM | Encrypted at rest (AES-256); access-controlled folders; no removable media without encryption |
| **Physical storage** | No restrictions | Office premises; standard filing | Locked cabinets or restricted-access rooms; clean desk enforced |
| **Email transmission** | No restrictions | Internal email or encrypted external | Encrypted email mandatory; password/decryption key via separate channel |
| **File transfer** | No restrictions | Approved file sharing platforms only | Encrypted transfer only (SFTP, HTTPS); no unapproved cloud services |
| **Physical transfer** | No restrictions | Sealed envelope; internal mail | Tamper-evident packaging; approved courier with tracking; recipient confirmation |
| **Sharing — internal** | Unrestricted | Within the organisation | Need-to-know basis with documented approval from information owner |
| **Sharing — external** | Unrestricted | NDA required; approved channels | NDA + specific authorisation from information owner; transfer agreement where required |
| **Printing** | No restrictions | Collect promptly; no abandoned printouts | Secure print release (badge/PIN); collect immediately |
| **Cloud storage** | Approved services | Approved services; data in Switzerland or adequate country | Approved services; data in Switzerland preferred; encryption with organisation-managed keys |
| **Mobile devices** | No restrictions | Organisation MDM-enrolled devices only | MDM-enrolled; device encryption; remote wipe capability |
| **Backup** | Standard backup | Encrypted backup | Encrypted backup; restricted restore access |

### Information Storage

Organisation information shall not be stored on personal equipment, personal email accounts, or personal cloud storage unless approved by the CISO and recorded in an approved register.

Organisation information shall be protected by access controls as defined in the Access Control Policy.

Confidential information shall be encrypted at rest and in transit when stored on or transmitted through any system, in line with the Use of Cryptography Policy.

Confidential and internal information shall not be stored or processed in development or test environments unless the data has been masked, anonymised, or pseudonymised. Where production data must be used in non-production environments, approval from the information owner and the CISO is required, and the data shall be handled at the same classification level as in production.

Where the organisation deploys Data Leakage Prevention (DLP) tools, DLP policies shall be aligned with the classification scheme to detect and prevent unauthorised transfer or disclosure of CONFIDENTIAL information (e.g., blocking external email of files labelled CONFIDENTIAL, preventing upload to unsanctioned cloud services).

### Verbal Information Handling

Confidential information discussed verbally (in meetings, phone calls, or conversations) shall be handled with appropriate care:

- Discussions of confidential information shall take place in private settings (closed offices, meeting rooms with closed doors) — not in open-plan areas, public spaces, or on public transport.
- Virtual meetings discussing confidential information shall use encrypted platforms with access restricted to authorised participants.
- Participants shall be reminded of the confidential nature of the discussion at the start of the meeting.
- Notes or minutes of confidential discussions shall be classified and handled accordingly.

### Control of Devices and Media

All electronic and paper media containing confidential information shall be physically secured from unauthorised access by securing in locked drawers, cabinets, or restricted rooms.

Removable media (USB drives, external drives, backup tapes) containing confidential data shall be encrypted and registered in the asset inventory, in line with the Asset Management Policy.

### Information Backup

Organisation information shall be backed up, retained, and tested in line with the backup schedule. Backups shall be encrypted using strong encryption. All backups shall be stored in secure locations with access restricted to authorised personnel.

---

## Information Destruction

When information is no longer required and its retention period has expired, it shall be destroyed securely according to its classification level.

### Destruction of Hard Copy Paper Records

| Classification | Destruction Standard |
|---------------|---------------------|
| **CONFIDENTIAL** | Cross-cut shredding to DIN 66399 Security Level P-4 or higher, or placement in approved confidential waste bins serviced by a certified destruction provider |
| **INTERNAL** | Cross-cut shredding to DIN 66399 Security Level P-3 or higher, or approved confidential waste bins |
| **PUBLIC** | Standard recycling or general waste |

### Destruction of Electronic Information

| Classification | Destruction Standard |
|---------------|---------------------|
| **CONFIDENTIAL** | Cryptographic erasure (destroy encryption key) or NIST SP 800-88 compliant overwrite; verification of erasure documented |
| **INTERNAL** | Secure deletion (overwrite); standard media sanitisation |
| **PUBLIC** | Standard deletion |

Logs of the wipe shall be maintained where the sanitisation tool supports it.

### Destruction of Electronic Media and Devices

Electronic media and devices that have stored confidential or internal information shall be destroyed by approved methods when no longer required:

- **SSDs and flash storage**: Cryptographic erasure (ATA Secure Erase) or physical destruction.
- **Hard disk drives**: NIST SP 800-88 compliant overwrite or physical destruction (degaussing, shredding).
- **Backup tapes**: Degaussing or physical destruction.
- **Optical media**: Physical shredding.

Destruction of confidential media shall be performed by approved specialist third-party suppliers where in-house destruction is not feasible. Certificates of destruction shall be obtained and retained as evidence.

An inventory of devices, including those destroyed, shall be maintained in line with the Asset Management Policy.

---

## Reclassification

Information classification is not permanent. Information shall be reclassified when:

- The sensitivity or value of the information changes.
- Legal or regulatory requirements change.
- A contractual obligation expires (e.g., NDA period ends).
- Information is approved for public release.
- The information owner determines the current classification is no longer appropriate.

Reclassification shall be performed by the information owner and the labelling updated accordingly.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **Information classification scheme documentation** (this policy) — *reviewed annually*
- **Sample classified documents** showing correct labelling (headers, footers, email prefixes) — *sample of 5–10 documents per classification level collected during annual audit*
- **Handling matrix implementation evidence** (access controls, encryption settings, sharing restrictions) — *system configuration screenshots or audit exports; reviewed annually*
- **Confidential media destruction records** (certificates of destruction, wipe logs) — *retained for 5 years; reconciled annually with asset disposal records*
- **Information asset register** showing classification assignments (per Asset Management Policy) — *target: 100% of information assets classified; measured annually*
- **Training records** showing employees trained on classification and handling requirements — *annual awareness training; completion tracked*
- **Exception records** for any deviation from handling rules — *reviewed quarterly; presented at management review*
- **DLP policy configuration and incident reports** (where DLP deployed) — *reviewed quarterly*

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, document sampling for correct labelling, access control audits, media destruction records, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to classification standards, regulatory requirements (including Swiss nFADP and GDPR developments), emerging data protection risks, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Information Classification and Handling Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | **5.12 Classification of information** |
| Clause 7.5.2 Creating and updating documentation | **5.13 Labelling of information** |
| Clause 7.5.3 Control of documented information | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 7.10 Storage media |
| | 7.14 Secure disposal or re-use of equipment |
| | 8.10 Information deletion |
| | 8.11 Data masking |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 5 — Sensitive personal data definition (maps to CONFIDENTIAL); Art. 8 — Technical and organisational measures |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 5 — Data protection principles; Art. 9 — Special categories of personal data; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Controls 5.12, 5.13 |
| ISO/IEC 27002:2022 | Sections 5.12, 5.13 — Implementation guidance |
| NIST SP 800-53 Rev 5 | RA-2 (Security Categorisation), AC-16 (Security and Privacy Attributes), MP-3 (Media Marking), MP-6 (Media Sanitisation) |
| CIS Controls v8 | Control 3 (Data Protection — including classification, encryption, disposal) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
