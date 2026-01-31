# ISMS-REF-PCI-DSS — Payment Card Industry Data Security Standard Requirements Reference
## Payment Card Data Security Requirements (Non-ISMS Technical Reference)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | PCI DSS Requirements Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-PCI-DSS |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | CISO (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Payment Security Team | Initial technical reference for PCI DSS v4.0.1 |

**Review Cycle**: Annual (or upon PCI DSS version updates)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: CISO / Payment Security Lead (technical reference, no ISMS approval required)

**Distribution**: Payment processing team, CISO, Compliance, IT Operations (for organizations handling payment cards)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory requirements unless [Organization] processes payment cards.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs for non-card-processing entities.
- This document does NOT mandate the adoption of PCI DSS requirements for organizations not handling payment cards.
- This document does NOT override or extend any ISMS policy.

**Applicability Determination**:
PCI DSS requirements apply ONLY IF [Organization]:
- Stores, processes, or transmits payment cardholder data (CHD)
- Has access to the Cardholder Data Environment (CDE)
- Is a merchant accepting credit/debit card payments
- Is a payment service provider or processor
- Is designated by payment brands (Visa, Mastercard, etc.) as requiring compliance

For all other organizations, this document serves solely as:
- Technical reference for potential PCI DSS requirements
- Context for business expansion into payment processing
- Awareness of payment card security standards
- **This document must not be used as audit evidence unless [Organization] is PCI DSS-compliant**

Use of this document does not imply PCI DSS applicability, compliance obligations, or payment card processing status.

**Critical Positioning Statement**:
This document intentionally provides regulatory detail beyond what applies to most organizations. Its purpose is awareness only for organizations that MAY become subject to PCI DSS, or that provide services to merchants or payment processors. No auditor conclusions shall be drawn from the presence, absence, or implementation status of any PCI DSS requirement listed herein unless [Organization] explicitly processes payment cards.

---

## 1. Document Purpose and Scope

### 1.1 Purpose

This document provides a technical overview of the Payment Card Industry Data Security Standard (PCI DSS) v4.0.1 requirements. It is intended to support:

- Awareness of PCI DSS requirements for entities handling payment cards
- Understanding of the 12 PCI DSS requirements across 6 control objectives
- Context for organizations considering payment card acceptance
- Potential future applicability assessment
- Mapping PCI DSS requirements to ISO 27001:2022 controls

### 1.2 What This Document Is NOT

This document does NOT:
- Establish mandatory requirements for non-payment-card-processing organizations
- Define [Organization]'s compliance obligations (see POL-00 for regulatory applicability)
- Create audit criteria unless [Organization] processes payment cards
- Replace Qualified Security Assessor (QSA) guidance
- Constitute legal or compliance advice on PCI DSS
- Cover all Self-Assessment Questionnaire (SAQ) variations
- Establish implementation procedures or validation processes

### 1.3 Relationship to ISMS

This document is a **non-binding technical reference** UNLESS [Organization] processes payment cards (as determined in ISMS-POL-00 Section 3.4).

**If [Organization] DOES process payment cards:**
- PCI DSS requirements become Tier 1 (Mandatory Compliance) per POL-00
- This document provides implementation guidance
- ISMS controls must demonstrate PCI DSS compliance
- Annual validation required (Report on Compliance or Self-Assessment Questionnaire)

**If [Organization] DOES NOT process payment cards:**
- PCI DSS remains Tier 3 (Informational Reference) per POL-00
- This document is for awareness only
- No PCI DSS compliance obligations exist
- ISMS controls follow ISO 27001:2022 only

### 1.4 Content Organization

This reference organizes PCI DSS requirements by:
- Applicability and merchant levels
- 12 requirements across 6 control objectives
- Cardholder Data Environment (CDE) scope definition
- Validation methods (ROC vs. SAQ)
- Mapping to ISO 27001:2022 Annex A controls
- PCI DSS v4.0.1 new requirements and timelines

---

## 2. PCI DSS Overview and Applicability

### 2.1 What is PCI DSS?

**Payment Card Industry Data Security Standard (PCI DSS)** is a global information security standard designed to protect payment card data.

**Governing Body**: PCI Security Standards Council (PCI SSC)
- Founded by major payment brands (Visa, Mastercard, American Express, Discover, JCB)
- Develops and maintains PCI DSS
- Certifies Qualified Security Assessors (QSAs)

**Current Version**: **PCI DSS v4.0.1** (released March 2024)
- Effective: March 31, 2024
- Transition period from v3.2.1 ended: March 31, 2024
- New requirements phased in through March 31, 2025

**Purpose**:
- Protect cardholder data from theft and fraud
- Establish minimum security requirements
- Standardize security controls across payment ecosystem
- Reduce risk of data breaches

### 2.2 Who Must Comply with PCI DSS?

**Any organization that stores, processes, or transmits cardholder data**:

| Entity Type | Description | Examples |
|-------------|-------------|----------|
| **Merchants** | Accept payment cards as payment | Retailers, e-commerce, restaurants, hotels |
| **Service Providers** | Process, store, or transmit CHD on behalf of merchants | Payment gateways, processors, hosting providers, managed security services |
| **Financial Institutions** | Issue payment cards or acquire transactions | Banks, credit unions, payment networks |
| **Point-of-Sale (POS) Vendors** | Provide POS systems or applications | POS software vendors, terminal manufacturers |

**Key Principle**: If you touch cardholder data, PCI DSS applies.

### 2.3 Merchant Levels

Payment brands (Visa, Mastercard, etc.) classify merchants into levels based on transaction volume:

**Visa Merchant Levels**:

| Level | Transaction Volume (Annual) | Validation Requirement |
|-------|----------------------------|------------------------|
| **Level 1** | > 6 million Visa transactions | Annual Report on Compliance (ROC) by QSA + Quarterly network scans |
| **Level 2** | 1-6 million Visa transactions | Annual Self-Assessment Questionnaire (SAQ) + Quarterly network scans |
| **Level 3** | 20,000 - 1 million Visa e-commerce transactions | Annual SAQ + Quarterly network scans |
| **Level 4** | < 20,000 Visa e-commerce OR < 1 million total Visa transactions | Annual SAQ + Quarterly network scans (may vary by acquirer) |

**Note**: Other payment brands (Mastercard, Amex, Discover) have similar but slightly different level definitions. Organizations should check requirements with their acquiring bank.

### 2.4 Cardholder Data (CHD) and Sensitive Authentication Data (SAD)

**Cardholder Data (CHD)**:
- **Primary Account Number (PAN)**: The 13-19 digit payment card number
- **Cardholder Name**: Name on the card
- **Expiration Date**: Card expiration date
- **Service Code**: 3-digit code on magnetic stripe

**Sensitive Authentication Data (SAD)** - MUST NOT be stored after authorization:
- **Full Magnetic Stripe Data** (Track 1, Track 2, or equivalent chip data)
- **Card Verification Code/Value** (CVV/CVC/CVV2/CID - 3 or 4 digit code)
- **PIN / PIN Block**: Personal Identification Number

**Critical Rule**: SAD must NEVER be stored after transaction authorization completes, even if encrypted.

### 2.5 Cardholder Data Environment (CDE)

**Definition**: The people, processes, and technologies that store, process, or transmit cardholder data or SAD, including connected systems.

**CDE Components**:
- **In-scope systems**: Systems that store, process, or transmit CHD
- **Connected systems**: Systems that provide security services to in-scope systems or could impact CDE security
- **Out-of-scope systems**: Properly segmented systems with no impact on CDE

**Scope Reduction Strategies**:
- **Tokenization**: Replace PAN with non-sensitive token
- **Point-to-point encryption (P2PE)**: Encrypt at point of entry, decrypt outside merchant environment
- **Network segmentation**: Isolate CDE from rest of network
- **Reduce data storage**: Don't store CHD if not needed
- **Outsourcing**: Use validated payment processors (reduces merchant scope)

### 2.6 Applicability Determination

**PCI DSS applies to [Organization] IF**:

| Criteria | Status | Evidence |
|----------|--------|----------|
| Stores cardholder data (PAN) | ⬜ Yes ⬜ No | [Description of storage] |
| Processes cardholder data (PAN) | ⬜ Yes ⬜ No | [Description of processing] |
| Transmits cardholder data (PAN) | ⬜ Yes ⬜ No | [Description of transmission] |
| Has systems connected to CDE | ⬜ Yes ⬜ No | [Description of connections] |
| Provides services to entities that handle CHD | ⬜ Yes ⬜ No | [Service provider type] |

**If ANY "Yes"**: PCI DSS requirements are **Tier 1 (Mandatory Compliance)** per POL-00 Section 3.4

**If ALL "No"**: PCI DSS requirements remain **Tier 3 (Informational Reference)** per POL-00

**Transaction Volume** (if applicable): [Annual volume] → Merchant Level: [1/2/3/4]

---

## 3. PCI DSS Structure - 6 Control Objectives and 12 Requirements

```
┌─────────────────────────────────────────────────────────────────┐
│              PCI DSS v4.0.1 STRUCTURE                           │
├─────────────────────────────────────────────────────────────────┤
│  BUILD AND MAINTAIN A SECURE NETWORK AND SYSTEMS                │
│    1. Install and maintain network security controls            │
│    2. Apply secure configurations to all system components      │
├─────────────────────────────────────────────────────────────────┤
│  PROTECT CARDHOLDER DATA                                        │
│    3. Protect stored account data                               │
│    4. Protect cardholder data with strong cryptography during   │
│       transmission over open, public networks                   │
├─────────────────────────────────────────────────────────────────┤
│  MAINTAIN A VULNERABILITY MANAGEMENT PROGRAM                    │
│    5. Protect all systems and networks from malicious software  │
│    6. Develop and maintain secure systems and software          │
├─────────────────────────────────────────────────────────────────┤
│  IMPLEMENT STRONG ACCESS CONTROL MEASURES                       │
│    7. Restrict access to cardholder data by business need to    │
│       know                                                      │
│    8. Identify users and authenticate access to system          │
│       components                                                │
│    9. Restrict physical access to cardholder data               │
├─────────────────────────────────────────────────────────────────┤
│  REGULARLY MONITOR AND TEST NETWORKS                            │
│   10. Log and monitor all access to system components and       │
│       cardholder data                                           │
│   11. Test security of systems and networks regularly           │
├─────────────────────────────────────────────────────────────────┤
│  MAINTAIN AN INFORMATION SECURITY POLICY                        │
│   12. Support information security with organizational policies │
│       and programs                                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Detailed Requirements

### 4.1 Requirement 1: Install and Maintain Network Security Controls

**Objective**: Firewalls and routers are critical for network security, controlling traffic between untrusted networks and the CDE.

**Key Sub-Requirements**:

**1.1 Processes and mechanisms for installing and maintaining network security controls**
- Documented network security control processes
- Roles and responsibilities assigned
- Annual review and update

**1.2 Network security controls (NSCs) configured and maintained**
- **1.2.1**: Configuration standards for NSCs defined and implemented
- **1.2.2**: Deny-all, permit-by-exception firewall rule sets
- **1.2.3**: Inbound and outbound traffic restricted to necessary
- **1.2.4**: Rules documented and justified (business need)
- **1.2.5**: Firewall rules reviewed at least every 6 months
- **1.2.6**: Changes to NSC rulesets approved
- **1.2.7**: Configurations reviewed for security parameter configurations

**1.3 Network access to and from the CDE restricted**
- **1.3.1**: Inbound traffic to CDE restricted
- **1.3.2**: Outbound traffic from CDE authorized
- **1.3.3**: NSCs installed between wireless networks and CDE

**1.4 Network connections between trusted and untrusted networks controlled**
- **1.4.1**: NSCs implemented to control traffic
- **1.4.2**: Configurations align with "deny all" principle
- **1.4.3**: Anti-spoofing measures implemented
- **1.4.4**: System components do not leak internal IP addresses
- **1.4.5**: Internet-facing web applications protected (WAF or equivalent) - **[New v4.0.1, Best Practice until March 31, 2025]**

**1.5 Risks to the CDE from computing devices able to connect to both untrusted networks and the CDE managed**
- **1.5.1**: Personal firewall software or equivalent controls deployed

**ISO 27001:2022 Mapping**:
- A.8.20: Networks security
- A.8.21: Security of network services
- A.8.22: Segregation of networks
- A.8.23: Web filtering

---

### 4.2 Requirement 2: Apply Secure Configurations to All System Components

**Objective**: Malicious actors target default accounts and settings. Secure configurations must be applied.

**Key Sub-Requirements**:

**2.1 Processes and mechanisms for applying secure configurations**
- Configuration standards documented
- Regular reviews of configurations

**2.2 System components configured and managed securely**
- **2.2.1**: Vendor default settings changed before production
- **2.2.2**: Vendor-supplied default passwords changed (or disabled)
- **2.2.3**: Primary functions requiring different security levels are managed by separate components (e.g., web servers, database servers separated)
- **2.2.4**: Insecure services, protocols, daemons removed or disabled
- **2.2.5**: Security services and parameters configured
- **2.2.6**: System security parameters configured to prevent misuse
- **2.2.7**: Non-console administrative access encrypted using strong cryptography

**2.3 Wireless environments configured and managed securely**
- **2.3.1**: Wireless vendor defaults changed
- **2.3.2**: Wireless networks secured with strong cryptography (WPA2/WPA3)

**ISO 27001:2022 Mapping**:
- A.8.9: Configuration management
- A.8.19: Installation of software on operational systems
- A.8.1: User endpoint devices

---

### 4.3 Requirement 3: Protect Stored Account Data

**Objective**: Stored cardholder data is a prime target. Protection methods must be in place.

**Key Sub-Requirements**:

**3.1 Processes and mechanisms for protecting stored account data**
- Data retention and disposal policies
- Documentation of CHD storage locations

**3.2 Storage of account data is kept to a minimum**
- **3.2.1**: Account data storage minimized
- Data retention policies limit storage amount and retention time

**3.3 Sensitive authentication data (SAD) is not stored after authorization**
- **3.3.1**: SAD not retained after authorization - **CRITICAL RULE**
- **3.3.2**: SAD rendered unrecoverable if stored before authorization
- **3.3.3**: PANs not displayed when not needed (masking)

**3.4 Access to displays of full PAN is restricted**
- **3.4.1**: PAN masked when displayed (first 6 and last 4 digits max)
- **3.4.2**: Technical controls enforce masking - **[New v4.0.1, Best Practice until March 31, 2025]**

**3.5 Primary Account Number (PAN) secured wherever stored**
- **3.5.1**: PAN rendered unreadable (encryption, truncation, hashing, tokenization)
- **3.5.1.1**: Hashes use keyed hash (HMAC) and key secured - **[New v4.0.1, Best Practice until March 31, 2025]**
- **3.5.1.2**: PANs secured with disk-level or partition-level encryption - **[New v4.0.1, Best Practice until March 31, 2025]**
- **3.5.1.3**: Cryptoperiods defined and implemented

**3.6 Cryptographic keys used to protect stored account data are secured**
- **3.6.1**: Procedures for key management defined and implemented
- **3.6.2**: Keys stored securely (fewest locations, encrypted storage)
- **3.6.3**: Key management restricted to few custodians
- **3.6.4**: Key management for cryptographic keys that have reached end of cryptoperiod
- **3.6.5**: Key custodian acknowledgment
- **3.6.6**: Secure cryptographic key distribution
- **3.6.7**: Prevention of unauthorized substitution of keys
- **3.6.8**: Requirement for key custodians to formally acknowledge understanding of responsibilities

**3.7 Where cryptography is used to protect stored account data, key management processes and procedures are implemented**
- **3.7.1**: Key-management policies and procedures maintained
- **3.7.2**: Cryptographic key management
- **3.7.3**: Key revocation process
- **3.7.4**: Removal or destruction of keys
- **3.7.5**: Change of keys when integrity compromised
- **3.7.6**: Key splits stored securely (for manual key management)
- **3.7.7**: Prevention of unauthorized substitution
- **3.7.8**: Key custodians formally acknowledge responsibilities
- **3.7.9**: Hardware and software inventory of cryptographic devices - **[New v4.0.1, Best Practice until March 31, 2025]**

**ISO 27001:2022 Mapping**:
- A.8.24: Use of cryptography
- A.8.10: Information deletion
- A.8.11: Data masking

---

### 4.4 Requirement 4: Protect Cardholder Data with Strong Cryptography During Transmission

**Objective**: Cardholder data transmitted over public networks must be encrypted.

**Key Sub-Requirements**:

**4.1 Processes and mechanisms for protecting cardholder data with strong cryptography during transmission**
- Inventory of CHD transmission points
- Cryptography policies and procedures

**4.2 PAN protected with strong cryptography during transmission**
- **4.2.1**: Strong cryptography and security protocols protect PAN during transmission over open, public networks
- **4.2.1.1**: Inventory of trusted keys and certificates - **[New v4.0.1, Best Practice until March 31, 2025]**
- **4.2.2**: PAN not sent via end-user messaging technologies

**ISO 27001:2022 Mapping**:
- A.8.24: Use of cryptography
- A.5.14: Information transfer

**Encryption Standards**:
- TLS 1.2 minimum (TLS 1.3 preferred)
- Strong cipher suites (no deprecated algorithms)
- No SSL, early TLS versions

---

### 4.5 Requirement 5: Protect All Systems and Networks from Malicious Software

**Objective**: Malware exploits vulnerabilities. Anti-malware protections must be deployed.

**Key Sub-Requirements**:

**5.1 Processes and mechanisms for protecting all systems and networks from malicious software**
- Anti-malware solution deployment plan
- Regular updates and reviews

**5.2 Malicious software (malware) prevented, detected, and addressed**
- **5.2.1**: Anti-malware solutions deployed on all systems (commonly affected by malware)
- **5.2.2**: Anti-malware mechanisms maintained (current, running, logging)
- **5.2.3**: Anti-malware mechanisms cannot be disabled or altered

**5.3 Anti-phishing mechanisms protect users against phishing attacks**
- **5.3.1**: Processes implemented to detect and protect personnel against phishing attacks
- **5.3.2**: Anti-phishing mechanisms are maintained and periodically evaluated - **[New v4.0.1, Best Practice until March 31, 2025]**
- **5.3.3**: Anti-phishing mechanisms protect against threats (controls/technical solutions) - **[New v4.0.1, Best Practice until March 31, 2025]**

**5.4 Anti-malware mechanisms and processes are active and maintained**
- **5.4.1**: Anti-malware logs retained and reviewed

**ISO 27001:2022 Mapping**:
- A.8.7: Protection against malware
- A.5.7: Threat intelligence

---

### 4.6 Requirement 6: Develop and Maintain Secure Systems and Software

**Objective**: Vulnerabilities in systems and software allow attackers to compromise CHD.

**Key Sub-Requirements**:

**6.1 Processes and mechanisms for developing and maintaining secure systems and software**
- Secure development lifecycle
- Change control procedures

**6.2 Bespoke and custom software are developed securely**
- **6.2.1**: Bespoke and custom software developed securely
- **6.2.2**: Software development personnel trained in secure coding
- **6.2.3**: Code reviews for bespoke and custom software before production - **[Updated v4.0.1]**
- **6.2.4**: Software engineering techniques in development to prevent common vulnerabilities

**6.3 Security vulnerabilities identified and addressed**
- **6.3.1**: Security vulnerabilities identified and assessed using industry-accepted methodologies
- **6.3.2**: Inventory of bespoke and custom software and third-party components
- **6.3.3**: All system components and software protected from known vulnerabilities (patches applied)
- **6.3.4**: Relevant patches/security updates reviewed and deployed within defined time periods

**Patch Timelines** (6.3.4):
- **Critical vulnerabilities**: 30 days maximum
- **High vulnerabilities**: Per organizational risk ranking (typically 30-90 days)
- **Other vulnerabilities**: Per risk-based approach

**6.4 Public-facing web applications protected from attacks**
- **6.4.1**: Public-facing web applications protected (automated technical solution, manual review, WAF)
- **6.4.2**: Payment page script integrity techniques - **[New v4.0.1, Best Practice until March 31, 2025]**
- **6.4.3**: HTTP headers included that instruct browser to protect from attacks

**6.5 Changes to all system components managed securely**
- **6.5.1**: Changes managed according to change control procedures
- **6.5.2**: Changes to systems reviewed for security impact
- **6.5.3**: Bespoke and custom software changes reviewed before deployment
- **6.5.4**: Test data and accounts removed before production
- **6.5.5**: Change control procedures documented
- **6.5.6**: Production data not used for testing/development

**ISO 27001:2022 Mapping**:
- A.8.8: Management of technical vulnerabilities
- A.8.25: Secure development life cycle
- A.8.26: Application security requirements
- A.8.27: Secure system architecture and engineering principles
- A.8.28: Secure coding
- A.8.29: Security testing in development and acceptance
- A.8.30: Outsourced development
- A.8.31: Separation of development, test and production environments
- A.8.32: Change management
- A.8.33: Test information

---

### 4.7 Requirement 7: Restrict Access to Cardholder Data by Business Need to Know

**Objective**: Access to CHD must be restricted to those who need it for their job.

**Key Sub-Requirements**:

**7.1 Processes and mechanisms for restricting access to system components and cardholder data**
- Access control policies defined
- Roles and responsibilities

**7.2 Access to system components and data is appropriately defined and assigned**
- **7.2.1**: Access granted based on job classification and function (need-to-know)
- **7.2.2**: Access assigned based on least privilege
- **7.2.3**: Required privileges approved by authorized personnel
- **7.2.4**: Access rights reviewed at least once every 6 months
- **7.2.5**: Privileged accounts assigned to specific user - **[Updated v4.0.1]**
- **7.2.6**: All user access to query repositories of stored CHD restricted

**7.3 Access to system components and data is managed via access control systems**
- **7.3.1**: Access control systems in place for system components
- **7.3.2**: Access control systems configured to enforce permissions (deny-all principle)
- **7.3.3**: Access control systems configured to prevent elevation of privilege

**ISO 27001:2022 Mapping**:
- A.5.15: Access control
- A.5.18: Access rights
- A.8.2: Privileged access rights
- A.8.3: Information access restriction

---

### 4.8 Requirement 8: Identify Users and Authenticate Access to System Components

**Objective**: Authentication ensures users are who they claim to be before accessing systems.

**Key Sub-Requirements**:

**8.1 Processes and mechanisms for identifying users and authenticating access**
- User identification and authentication policies

**8.2 User identification and related accounts are strictly managed**
- **8.2.1**: Unique ID assigned before access granted
- **8.2.2**: Shared IDs prohibited (except explicitly approved)
- **8.2.3**: Generic accounts only used when necessary (approved, controlled)
- **8.2.4**: Service provider personnel with remote access have unique credential
- **8.2.5**: Shared service provider accounts use MFA - **[New v4.0.1, Best Practice until March 31, 2025]**
- **8.2.6**: Application and system accounts managed to prevent misuse
- **8.2.7**: User accounts added, deleted, or modified in timely manner
- **8.2.8**: Invalid authentication attempts result in account lockout (after 10 attempts maximum)

**8.3 Strong authentication for users and administrators is established and managed**
- **8.3.1**: Multi-factor authentication (MFA) for all access into CDE
- **8.3.2**: MFA for all access to entity's network (remote and internal)
- **8.3.3**: MFA systems configured to prevent misuse
- **8.3.4**: MFA required for all administrative access
- **8.3.5**: MFA for all access to CDE uses factors in two different categories - **[New v4.0.1, Best Practice until March 31, 2025]**
- **8.3.6**: Phishing-resistant MFA used for personnel with administrative access - **[New v4.0.1, Best Practice until March 31, 2025]**
- **8.3.7**: MFA for application and system accounts used to execute privileged commands - **[New v4.0.1, Best Practice until March 31, 2025]**
- **8.3.8**: MFA for service providers with remote access to entity's systems - **[New v4.0.1, Best Practice until March 31, 2025]**
- **8.3.9**: Strong cryptographic authentication used for non-console administrative access
- **8.3.10**: User authentication methods appropriate to entity's environment

**8.4 Multi-factor authentication (MFA) is implemented to secure access into the CDE**
- **[New v4.0.1 consolidated from various 8.3 requirements]**

**8.5 Passwords and passphrases meet minimum strength requirements**
- **8.5.1**: Passwords/passphrases minimum 12 characters (or 8 if system doesn't support 12) - **[Updated v4.0.1]**

**8.6 Use of application and system accounts and associated authentication factors is strictly managed**
- **8.6.1**: Application and system accounts secured (no interactive login, can't be used for interactive login)
- **8.6.2**: Passwords/passphrases changed when suspected or known compromise
- **8.6.3**: Passwords/passphrases managed to prevent misuse

**ISO 27001:2022 Mapping**:
- A.5.16: Identity management
- A.5.17: Authentication information
- A.8.5: Secure authentication

---

### 4.9 Requirement 9: Restrict Physical Access to Cardholder Data

**Objective**: Physical access to systems and media containing CHD must be controlled.

**Key Sub-Requirements**:

**9.1 Processes and mechanisms for restricting physical access to cardholder data**
- Physical security policies and procedures

**9.2 Physical access controls manage entry into facilities and systems containing cardholder data**
- **9.2.1**: Physical access controls in place to restrict access to systems in CDE
- **9.2.2**: Logical and physical access controls ensure only authorized personnel have access
- **9.2.3**: Physical access for personnel revoked immediately upon termination
- **9.2.4**: Visitor access procedures and visitor badge system
- **9.2.5**: Physical access controls for wireless access points
- **9.2.6**: Physical access logs reviewed at least once every 3 months
- **9.2.7**: Video cameras or access control mechanisms monitor sensitive areas

**9.3 Physical access for personnel and visitors is authorized and managed**
- **9.3.1**: Visitors authorized and escorted in areas containing CHD
- **9.3.2**: Visitor badge system distinguishes visitors from personnel
- **9.3.3**: Visitor badges surrendered or deactivated before leaving

**9.4 Media with cardholder data is securely stored, accessed, distributed, and destroyed**
- **9.4.1**: Media containing CHD stored in secure location (offsite backups secured)
- **9.4.2**: Media classified for sensitivity
- **9.4.3**: Media sent by secure courier (tracking used)
- **9.4.4**: Management approval for media leaving secured area
- **9.4.5**: Media inventoried at least annually
- **9.4.6**: Media destroyed when no longer needed (crosscut shred, incinerate, purge/degauss magnetic media)
- **9.4.7**: Media with CHD destroyed when no longer needed for business/legal reasons

**9.5 Point of Interaction (POI) devices are protected from tampering and unauthorized substitution**
- **9.5.1**: POI devices protected from tampering (tamper-evident seals, etc.)
- **9.5.2**: Procedures to detect and report tampering/substitution
- **9.5.3**: Training for personnel to be aware of tampering/substitution attempts

**ISO 27001:2022 Mapping**:
- A.7.1: Physical security perimeters
- A.7.2: Physical entry
- A.7.3: Securing offices, rooms and facilities
- A.7.4: Physical security monitoring
- A.7.7: Clear desk and clear screen
- A.7.8: Equipment siting and protection
- A.7.10: Storage media
- A.7.14: Secure disposal or re-use of equipment

---

### 4.10 Requirement 10: Log and Monitor All Access to System Components and Cardholder Data

**Objective**: Logging mechanisms and the ability to track user activities are critical for prevention, detection, or minimizing impact of a data compromise.

**Key Sub-Requirements**:

**10.1 Processes and mechanisms for logging and monitoring all access to system components and cardholder data**
- Logging and monitoring policies defined

**10.2 Audit logs are implemented to support detection of anomalies and suspicious activity**
- **10.2.1**: Audit logs enabled and active for system components
- **10.2.2**: Audit logs capture: user ID, event type, date/time, success/failure, origination, identity/name of affected data/system component

**10.3 Audit logs are protected from destruction and unauthorized modifications**
- **10.3.1**: Read access to audit log files limited to those with job-related need
- **10.3.2**: Audit log files protected from unauthorized modification
- **10.3.3**: Audit log files promptly backed up to secure centralized log server
- **10.3.4**: File integrity monitoring or change detection software used on audit logs

**10.4 Audit logs are reviewed to identify anomalies or suspicious activity**
- **10.4.1**: Security policies and procedures identify anomalies and suspicious activity
- **10.4.1.1**: Automated mechanisms alert personnel for anomalies or suspicious activity - **[New v4.0.1, Best Practice until March 31, 2025]**
- **10.4.2**: Audit logs reviewed at least once daily
- **10.4.3**: Exceptions and anomalies identified during review process are addressed

**10.5 Audit log history is retained and available for analysis**
- **10.5.1**: Audit log history retained for at least 12 months (minimum 3 months immediately available)

**10.6 Time-synchronization mechanisms support consistent time settings across all systems**
- **10.6.1**: System clocks are synchronized using time synchronization technology
- **10.6.2**: Time synchronization technologies configured consistently
- **10.6.3**: Critical time servers accept time from external sources (Stratum 0 or 1)

**10.7 Failures of critical security control systems are detected, reported, and responded to promptly**
- **10.7.1**: Additional requirement for service providers only - Failures of critical security control systems detected and reported - **[New v4.0.1]**
- **10.7.2**: Additional requirement for service providers only - Failures of critical security control systems responded to promptly - **[New v4.0.1]**
- **10.7.3**: Additional requirement for service providers only - Failures of critical security control systems include restoration of security functions - **[New v4.0.1]**

**ISO 27001:2022 Mapping**:
- A.8.15: Logging
- A.8.16: Monitoring activities

---

### 4.11 Requirement 11: Test Security of Systems and Networks Regularly

**Objective**: Vulnerabilities are discovered continuously. Regular testing identifies and verifies controls are in place.

**Key Sub-Requirements**:

**11.1 Processes and mechanisms for regularly testing security of systems and networks**
- Testing policies and procedures defined

**11.2 Wireless access points are identified and monitored**
- **11.2.1**: Authorized and unauthorized wireless access points detected
- **11.2.2**: Wireless IDS/IPS or equivalent deployed

**11.3 External and internal vulnerabilities are regularly identified, prioritized, and addressed**
- **11.3.1**: Internal vulnerability scans performed at least once every 3 months
- **11.3.2**: External vulnerability scans performed at least once every 3 months (by Approved Scanning Vendor - ASV)
- **11.3.3**: External and internal penetration testing performed

**Penetration Testing (11.4)**:
- **11.4.1**: Penetration testing methodology defined and implemented
- **11.4.2**: Internal penetration testing performed at least once every 12 months
- **11.4.3**: External penetration testing performed at least once every 12 months
- **11.4.4**: Exploitable vulnerabilities found during penetration testing corrected
- **11.4.5**: Segmentation controls tested (if network segmentation used for scoping)
- **11.4.6**: Additional requirement for service providers - penetration testing performed after significant infrastructure/application upgrade
- **11.4.7**: Multi-tenant service providers support customer penetration testing or provide testing evidence - **[New v4.0.1, Best Practice until March 31, 2025]**

**11.5 Network security controls are in place and effective**
- **11.5.1**: Change detection mechanisms deployed
- **11.5.2**: Change detection mechanisms configured to alert personnel

**11.6 Unauthorized changes on payment pages are detected and responded to**
- **11.6.1**: Change and tamper detection mechanism deployed on payment pages - **[Updated v4.0.1]**

**ISO 27001:2022 Mapping**:
- A.8.8: Management of technical vulnerabilities
- A.5.7: Threat intelligence
- A.8.34: Protection of information systems during audit testing

---

### 4.12 Requirement 12: Support Information Security with Organizational Policies and Programs

**Objective**: Security policies and procedures establish expectations and guide personnel in their day-to-day duties.

**Key Sub-Requirements**:

**12.1 An overall information security policy is established and published**
- **12.1.1**: Security policy established, documented, communicated
- **12.1.2**: Security policy reviewed at least annually and updated as needed
- **12.1.3**: Roles and responsibilities for security assigned
- **12.1.4**: Executive management ultimate responsibility for protection of CHD

**12.2 Acceptable use policies for end-user technologies are defined and implemented**
- **12.2.1**: Acceptable use policy for end-user technologies defined

**12.3 Risks to the cardholder data environment are formally identified, evaluated, and managed**
- **12.3.1**: Targeted risk analysis performed at least once every 12 months
- **12.3.2**: Targeted risk analysis performed upon significant changes
- **12.3.3**: Risk assessment results reviewed and documented
- **12.3.4**: PCI DSS compliance program confirmed operational at least quarterly

**12.4 PCI DSS compliance is managed**
- **12.4.1**: Responsibilities for management of PCI DSS assigned
- **12.4.2**: Executive management maintains awareness and oversight

**12.5 PCI DSS scope is documented and validated**
- **12.5.1**: Inventory of all system components in scope for PCI DSS
- **12.5.2**: Scope determination at least once every 12 months
- **12.5.2.1**: Impact of changes on PCI DSS scope determined - **[New v4.0.1, Best Practice until March 31, 2025]**
- **12.5.3**: Security impact of changes to system components determined

**12.6 Security awareness education is an ongoing activity**
- **12.6.1**: Security awareness program implemented
- **12.6.2**: Personnel complete awareness training upon hire and at least once every 12 months
- **12.6.3**: Personnel training materials reference correct security policies and procedures
- **12.6.3.1**: Personnel receive training on phishing and social engineering - **[New v4.0.1, Best Practice until March 31, 2025]**

**12.7 Personnel are screened to reduce risks from insider threats**
- **12.7.1**: Potential personnel screened before hire (background checks per local law)

**12.8 Risk to information assets associated with third-party service provider (TPSP) relationships is managed**
- **12.8.1**: List of TPSPs maintained (including services provided)
- **12.8.2**: Written agreements with TPSPs include acknowledgment of responsibility
- **12.8.3**: Processes in place to engage TPSPs (due diligence before engagement)
- **12.8.4**: Program to monitor TPSP PCI DSS compliance status
- **12.8.5**: Information maintained about PCI DSS requirements managed by each TPSP

**12.9 Third-party service providers (TPSPs) support their customers' PCI DSS compliance**
- **12.9.1**: TPSPs acknowledge responsibility for security of CHD
- **12.9.2**: TPSPs provide information to customers upon request

**12.10 Suspected and confirmed security incidents are responded to immediately**
- **12.10.1**: Incident response plan created and maintained
- **12.10.2**: Incident response plan tested at least annually
- **12.10.3**: Personnel designated and trained for incident response
- **12.10.4**: Alerting and monitoring systems in place
- **12.10.5**: Intrusion detection/prevention systems monitor all traffic in CDE
- **12.10.6**: Change detection mechanisms monitor audit logs
- **12.10.7**: Incident response procedures include: (i) roles/responsibilities, (ii) communication strategy, (iii) specific procedures, (iv) business recovery procedures, (v) data backup processes, (vi) legal requirements, (vii) forensics

**ISO 27001:2022 Mapping**:
- A.5.1: Policies for information security
- A.5.36: Compliance with policies, rules and standards for information security
- A.6.3: Information security awareness, education and training
- A.5.24-5.28: Incident management
- A.5.19-5.23: Supplier relationships
- Clause 6.1.2-6.1.3: Risk assessment and treatment

---

## 5. PCI DSS v4.0.1 New and Updated Requirements

### 5.1 Phased Implementation Timeline

**PCI DSS v4.0** introduced new requirements phased in over time:

| Requirement Category | Effective Date | Status |
|---------------------|----------------|--------|
| **All existing v3.2.1 requirements** | March 31, 2024 | Mandatory |
| **New requirements - Future Dated** | March 31, 2024 - March 31, 2025 | Best Practice |
| **All v4.0.1 requirements** | March 31, 2025 | Mandatory |

### 5.2 Key New Requirements (Effective March 31, 2025)

**Multi-Factor Authentication Expansion**:
- 8.3.5: MFA must use factors from two different categories (something you know, have, are)
- 8.3.6: Phishing-resistant MFA for administrative access
- 8.3.7: MFA for privileged application/system accounts
- 8.3.8: MFA for service provider remote access

**Enhanced Authentication**:
- 8.5.1: Passwords minimum 12 characters (previously 7)

**Cryptographic Enhancements**:
- 3.5.1.1: Keyed hashes (HMAC) required for PAN hashing
- 3.5.1.2: Disk/partition-level encryption with key management separation
- 3.7.9: Hardware/software inventory of cryptographic devices
- 4.2.1.1: Inventory of trusted keys and certificates

**Web Application Security**:
- 1.4.5: NSCs between internet and web applications (WAF or equivalent)
- 6.4.2: Payment page script integrity techniques (CSP, SRI, etc.)
- 11.6.1: Tamper detection for payment pages enhanced

**Anti-Phishing**:
- 5.3.2: Anti-phishing mechanisms maintained and evaluated
- 5.3.3: Technical anti-phishing controls implemented
- 12.6.3.1: Personnel training on phishing and social engineering

**Logging and Monitoring**:
- 10.4.1.1: Automated alerting for anomalies/suspicious activity
- 10.7.1-10.7.3: Critical security control failure detection and response (service providers)

**Scope and Risk Management**:
- 12.3.4: PCI DSS compliance program operational confirmation (quarterly)
- 12.5.2.1: Impact of changes on PCI DSS scope determination

**Service Provider Requirements**:
- 11.4.7: Multi-tenant service providers support customer penetration testing

---

## 6. Validation and Compliance

### 6.1 Validation Methods

**Report on Compliance (ROC)**:
- Required for: Level 1 merchants, service providers
- Performed by: Qualified Security Assessor (QSA)
- Frequency: Annual
- Deliverable: Detailed compliance report (300+ pages)

**Self-Assessment Questionnaire (SAQ)**:
- Required for: Level 2-4 merchants (depending on payment channels)
- Performed by: Internal assessment (or QSA optional)
- Frequency: Annual
- Deliverable: Completed SAQ + Attestation of Compliance (AOC)

**SAQ Types**:

| SAQ Type | Applicability | Requirements |
|----------|---------------|--------------|
| **SAQ A** | Card-not-present, fully outsourced (no electronic storage, processing, transmission) | 22 requirements |
| **SAQ A-EP** | E-commerce, partially outsourced | 169 requirements |
| **SAQ B** | Imprint machines only OR standalone dial-out terminals | 41 requirements |
| **SAQ B-IP** | Standalone IP-connected terminals, no electronic storage | 79 requirements |
| **SAQ C** | Payment application systems connected to internet, no electronic storage | 158 requirements |
| **SAQ C-VT** | Web-based virtual terminal, no electronic storage | 80 requirements |
| **SAQ P2PE** | Hardware payment terminals using validated P2PE solution | 32 requirements |
| **SAQ D - Merchant** | All other merchants not fitting above categories | 337 requirements |
| **SAQ D - Service Provider** | Service providers eligible for SAQ | 337 requirements |

**Quarterly Network Scans**:
- Required for: All entities with internet-facing systems in CDE
- Performed by: Approved Scanning Vendor (ASV)
- Frequency: Quarterly minimum (also after significant network changes)
- Pass criteria: No vulnerabilities rated 4.0 or higher (CVSS)

### 6.2 Attestation of Compliance (AOC)

Required documentation submitted to acquirer/payment brand:
- Completed ROC or SAQ
- Attestation of Compliance (AOC) - signed document
- ASV scan results (4 passing quarterly scans)
- Segmentation testing (if network segmentation used for scoping)

---

## 7. ISO 27001:2022 to PCI DSS Mapping

### 7.1 Control Mapping Matrix

| PCI DSS Requirement | ISO 27001:2022 Control | Gap Analysis |
|---------------------|------------------------|--------------|
| 1. Network Security Controls | A.8.20-8.23 | PCI DSS: More prescriptive firewall rules |
| 2. Secure Configurations | A.8.9, A.8.19, A.8.1 | Aligned |
| 3. Protect Stored CHD | A.8.24, A.8.10, A.8.11 | **PCI DSS-specific**: SAD storage prohibited, strict encryption requirements |
| 4. Protect CHD in Transmission | A.8.24, A.5.14 | PCI DSS: Mandates TLS 1.2+, prohibits end-user messaging |
| 5. Protect from Malware | A.8.7, A.5.7 | PCI DSS: Adds anti-phishing requirements (v4.0) |
| 6. Secure Development | A.8.8, A.8.25-8.33 | PCI DSS: Prescriptive patch timelines (30 days critical) |
| 7. Restrict Access by Need-to-Know | A.5.15, A.5.18, A.8.2-8.3 | Aligned |
| 8. Identify and Authenticate | A.5.16-5.17, A.8.5 | **PCI DSS-specific**: MFA mandatory, 12-char passwords |
| 9. Restrict Physical Access | A.7.1-7.4, A.7.7-7.8, A.7.10, A.7.14 | PCI DSS: Adds POI device protection |
| 10. Log and Monitor | A.8.15-8.16 | PCI DSS: Prescriptive 12-month retention, daily review |
| 11. Test Security | A.8.8, A.5.7, A.8.34 | **PCI DSS-specific**: Quarterly ASV scans, annual pentests |
| 12. Security Policy and Program | A.5.1, A.5.36, A.6.3, A.5.24-5.28, A.5.19-5.23 | PCI DSS: Adds targeted risk analysis, executive accountability |

### 7.2 Key Gaps Between ISO 27001:2022 and PCI DSS

**Gap 1: Cardholder Data Specific Requirements**
- ISO 27001: General data protection
- PCI DSS: Explicit CHD handling, SAD storage prohibition, PAN masking

**Gap 2: Prescriptive Technical Controls**
- ISO 27001: Risk-based control selection
- PCI DSS: Mandatory controls (firewalls, encryption, MFA, anti-malware)

**Gap 3: Testing and Validation Frequency**
- ISO 27001: No mandated testing frequency
- PCI DSS: Quarterly ASV scans, annual pentests, annual compliance validation

**Gap 4: Merchant/Service Provider Specific Requirements**
- ISO 27001: No merchant-specific guidance
- PCI DSS: Explicit merchant levels, SAQ types, service provider obligations

**Gap 5: Executive Accountability**
- ISO 27001: Management commitment
- PCI DSS: Executive management ultimate responsibility (12.1.4)

### 7.3 PCI DSS Compliance with ISO 27001 Foundation

**Key Insight**:
ISO 27001:2022 certification provides foundational security controls. However, PCI DSS requires:
1. **CDE scoping** and cardholder data flow documentation
2. **Prescriptive technical controls** (MFA, encryption standards, patch timelines)
3. **Regular validation** (ASV scans, pentests, annual compliance attestation)
4. **Specific logging/monitoring** requirements (12-month retention, daily review)
5. **Merchant-specific requirements** based on transaction volume

Organizations with ISO 27001 typically require **30-50% additional effort** to achieve PCI DSS compliance, primarily in CDE scoping, prescriptive controls, and validation processes.

---

## 8. Implementation Considerations

### 8.1 PCI DSS Compliance Roadmap

**If [Organization] processes payment cards**:

**Phase 1: Scoping (Months 1-2)**
- Document cardholder data flows
- Define Cardholder Data Environment (CDE)
- Identify in-scope systems and connected systems
- Network segmentation if applicable
- Determine merchant level and validation requirements

**Phase 2: Gap Assessment (Months 2-3)**
- Assess current controls against PCI DSS requirements
- Identify gaps and remediation priorities
- Document compensating controls if needed
- Estimate remediation timeline and budget

**Phase 3: Remediation (Months 3-9)**
- **Critical gaps first**: Req 3 (protect stored CHD), Req 4 (protect CHD transmission), Req 8 (MFA)
- **High priority**: Req 1-2 (network security, configurations), Req 6 (patching), Req 10 (logging)
- **Medium priority**: Req 5 (anti-malware), Req 7 (access controls), Req 9 (physical security)
- **Administrative**: Req 11 (testing), Req 12 (policies and procedures)

**Phase 4: Validation Preparation (Months 9-11)**
- Internal readiness assessment
- ASV quarterly scans (4 passing scans required)
- Internal penetration testing
- Documentation compilation
- QSA engagement (if ROC required)

**Phase 5: Compliance Validation (Month 12)**
- QSA audit (if Level 1) or SAQ completion
- Final ASV scan
- Attestation of Compliance (AOC) completion
- Submission to acquirer/payment brands

**Ongoing (Post-Compliance)**:
- Quarterly ASV scans
- Annual compliance revalidation
- Continuous monitoring and logging review
- Change management with PCI impact assessment
- Annual penetration testing and vulnerability management

### 8.2 Resource Requirements

**Personnel**:
- PCI Compliance Manager/Coordinator
- QSA (external, for Level 1 merchants)
- ASV (external, for quarterly scans)
- Internal security team (firewall, encryption, logging, patching)
- Application development team (secure coding, payment page protection)
- Physical security team (if applicable)

**Technology**:
- Network security controls (firewalls, IDS/IPS)
- Encryption solutions (TLS for transmission, disk/database encryption)
- Multi-factor authentication platform
- SIEM or centralized logging
- Vulnerability scanning tools
- Anti-malware solutions
- File integrity monitoring (FIM)
- Time synchronization (NTP)
- Payment tokenization or P2PE (optional, for scope reduction)

**External Services**:
- QSA for annual audit (Level 1)
- ASV for quarterly vulnerability scans
- Penetration testing services (annual)
- Secure disposal/destruction vendor (media)
- Forensic investigation retainer (incident response)

### 8.3 Cost Implications

PCI DSS compliance costs vary significantly by merchant level and environment complexity:

**Level 1 Merchant (> 6M transactions/year)**:
- QSA audit: $30,000 - $100,000 (annual)
- ASV scans: $3,000 - $10,000 (annual)
- Penetration testing: $15,000 - $50,000 (annual)
- Technology investments: $100,000 - $500,000 (initial)
- Personnel: 1-3 FTE dedicated to PCI compliance
- **Total annual cost**: $200,000 - $1,000,000+

**Level 2-4 Merchant (< 6M transactions/year)**:
- SAQ + AOC: $0 - $20,000 (if QSA assistance)
- ASV scans: $2,000 - $5,000 (annual)
- Penetration testing: $10,000 - $30,000 (annual)
- Technology investments: $50,000 - $200,000 (initial)
- Personnel: 0.5-1 FTE dedicated to PCI compliance
- **Total annual cost**: $50,000 - $250,000

**Non-Compliance Penalties**:
- Card brand fines: $5,000 - $100,000 per month (escalating)
- Acquirer fines and fees
- Potential loss of ability to accept cards
- Breach costs: $200+ per compromised record
- Reputational damage

---

## 9. Common Pitfalls and Lessons Learned

### 9.1 Common PCI DSS Compliance Challenges

**Challenge 1: Scope Creep**
- CDE not properly segmented from rest of network
- "Flat" networks result in entire environment in scope
- Lack of network diagrams and data flow documentation

**Challenge 2: Sensitive Authentication Data (SAD) Storage**
- Accidentally storing CVV/CVV2, full track data, PIN
- Even encrypted storage of SAD is prohibited post-authorization
- Legacy applications may have hidden SAD storage

**Challenge 3: Multi-Factor Authentication Implementation**
- Underestimating MFA deployment complexity (v4.0 expansion)
- Legacy systems not supporting MFA
- Exceptions for "service accounts" not properly managed

**Challenge 4: Logging and Monitoring Gaps**
- Logs not retained for 12 months
- Daily log review not performed consistently
- SIEM not properly configured for CDE
- Time synchronization issues (clocks out of sync)

**Challenge 5: Quarterly ASV Scan Failures**
- Unpatched vulnerabilities discovered during scans
- False positive management
- Scan windows not aligned with compliance submission deadlines

**Challenge 6: Change Management**
- Changes to CDE not assessed for PCI impact
- Network segmentation breaks due to changes
- Firewall rules added without documentation/justification

**Challenge 7: Vendor Management**
- Third-party service providers not validated for PCI compliance
- Payment applications not PA-DSS or PCI SSC validated
- Hosting providers not PCI DSS compliant

### 9.2 Best Practices

**Practice 1**: Reduce scope through tokenization, P2PE, or outsourcing
**Practice 2**: Implement strong network segmentation (reduce CDE scope)
**Practice 3**: Use QSA for pre-assessment gap analysis (before formal audit)
**Practice 4**: Automate compliance monitoring (continuous compliance)
**Practice 5**: Integrate PCI DSS into SDLC for payment applications
**Practice 6**: Conduct quarterly internal PCI readiness reviews
**Practice 7**: Train all personnel on PCI DSS basics (not just IT)
**Practice 8**: Use compensating controls documentation when technical controls infeasible
**Practice 9**: Maintain comprehensive documentation (diagrams, policies, evidence)
**Practice 10**: Plan ASV scans early (allow time for remediation before deadlines)

---

## 10. References and Resources

### 10.1 PCI DSS Official Resources

**PCI Security Standards Council (PCI SSC)**:
- Website: https://www.pcisecuritystandards.org/
- PCI DSS v4.0.1: https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf
- PCI DSS Quick Reference Guide
- Self-Assessment Questionnaires (SAQs)
- Prioritized Approach for PCI DSS v4.0

**Payment Brand Resources**:
- **Visa**: https://usa.visa.com/support/small-business/security-compliance.html
- **Mastercard**: https://www.mastercard.us/en-us/business/overview/safety-and-security/security-recommendations.html
- **American Express**: https://www.americanexpress.com/us/merchant/data-security-operating-policy.html
- **Discover**: https://www.discoverglobalnetwork.com/en-us/resources/compliance

### 10.2 Qualified Service Providers

**Find a QSA (Qualified Security Assessor)**:
- PCI SSC QSA Directory: https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors

**Find an ASV (Approved Scanning Vendor)**:
- PCI SSC ASV Directory: https://www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors

**Validated Payment Applications**:
- PCI SSC Validated Applications: https://www.pcisecuritystandards.org/assessors_and_solutions/payment_applications

### 10.3 Related Standards and Frameworks

**ISO Standards**:
- ISO/IEC 27001:2022: Information Security Management
- ISO/IEC 27002:2022: Information Security Controls

**NIST Publications** (informational reference):
- NIST SP 800-53: Security and Privacy Controls
- NIST Cybersecurity Framework

**Industry Guidance**:
- OWASP Application Security: https://owasp.org/
- CIS Controls: https://www.cisecurity.org/controls

### 10.4 Training and Certification

**PCI SSC Training**:
- PCI Professional (PCIP): Entry-level certification
- Internal Security Assessor (ISA): Internal audit certification
- Qualified Security Assessor (QSA): External auditor certification

**Online Resources**:
- PCI Guru: https://pciguru.wordpress.com/ (unofficial blog)
- PCI Compliance Guide: https://www.pcicomplianceguide.org/

---

## Appendix A: PCI DSS Compliance Self-Assessment Checklist

This checklist provides high-level coverage. Organizations should use official SAQs for complete assessment.

### Build and Maintain Secure Network (Req 1-2)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Firewall rules documented and justified | ⬜ Yes ⬜ No ⬜ Partial | | |
| Firewall rules reviewed every 6 months | ⬜ Yes ⬜ No | | |
| Network segmentation between CDE and other networks | ⬜ Yes ⬜ No ⬜ N/A | | |
| Vendor default passwords changed | ⬜ Yes ⬜ No | | |
| Unnecessary services disabled | ⬜ Yes ⬜ No ⬜ Partial | | |
| Wireless networks secured (WPA2/WPA3) | ⬜ Yes ⬜ No ⬜ N/A | | |

### Protect Cardholder Data (Req 3-4)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| CHD storage minimized (only if needed) | ⬜ Yes ⬜ No | | |
| Sensitive Authentication Data (SAD) NOT stored after authorization | ⬜ Yes ⬜ No | | |
| PAN masked when displayed (first 6, last 4 max) | ⬜ Yes ⬜ No | | |
| PAN encrypted or tokenized when stored | ⬜ Yes ⬜ No | | |
| Encryption keys secured and managed | ⬜ Yes ⬜ No ⬜ Partial | | |
| TLS 1.2+ used for CHD transmission over open networks | ⬜ Yes ⬜ No | | |
| PAN not sent via end-user messaging (email, chat, SMS) | ⬜ Yes ⬜ No | | |

### Maintain Vulnerability Management (Req 5-6)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Anti-malware deployed on all systems (commonly affected) | ⬜ Yes ⬜ No ⬜ Partial | | |
| Anti-malware current, running, and logging | ⬜ Yes ⬜ No | | |
| Anti-phishing mechanisms deployed | ⬜ Yes ⬜ No ⬜ Partial | | |
| Security patches applied within 30 days (critical vulnerabilities) | ⬜ Yes ⬜ No | | |
| Vulnerability management process in place | ⬜ Yes ⬜ No ⬜ Partial | | |
| Secure coding practices for custom software | ⬜ Yes ⬜ No ⬜ N/A | | |
| Public-facing web applications protected (WAF or equivalent) | ⬜ Yes ⬜ No ⬜ N/A | | |

### Implement Strong Access Controls (Req 7-9)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Access granted based on need-to-know | ⬜ Yes ⬜ No ⬜ Partial | | |
| Access rights reviewed at least every 6 months | ⬜ Yes ⬜ No | | |
| Unique user IDs assigned to each person | ⬜ Yes ⬜ No | | |
| Shared accounts prohibited (except approved) | ⬜ Yes ⬜ No | | |
| Multi-factor authentication (MFA) for all CDE access | ⬜ Yes ⬜ No | | |
| MFA for remote access to entity's network | ⬜ Yes ⬜ No | | |
| Passwords minimum 12 characters | ⬜ Yes ⬜ No | | |
| Account lockout after 10 failed login attempts | ⬜ Yes ⬜ No | | |
| Physical access controls for CDE systems | ⬜ Yes ⬜ No ⬜ Partial | | |
| Visitor access controlled and logged | ⬜ Yes ⬜ No ⬜ N/A | | |
| Media with CHD securely destroyed when no longer needed | ⬜ Yes ⬜ No | | |

### Monitor and Test Networks (Req 10-11)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Audit logs enabled for all system components | ⬜ Yes ⬜ No ⬜ Partial | | |
| Audit logs reviewed at least once daily | ⬜ Yes ⬜ No | | |
| Audit logs retained for at least 12 months | ⬜ Yes ⬜ No | | |
| Time synchronization implemented (NTP) | ⬜ Yes ⬜ No | | |
| Wireless access points detected (authorized/unauthorized) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Internal vulnerability scans every 3 months | ⬜ Yes ⬜ No | | |
| External vulnerability scans (ASV) every 3 months - 4 passing scans | ⬜ Yes ⬜ No | | |
| Internal penetration testing at least annually | ⬜ Yes ⬜ No | | |
| External penetration testing at least annually | ⬜ Yes ⬜ No | | |
| Change detection mechanisms deployed (FIM) | ⬜ Yes ⬜ No | | |

### Information Security Policy (Req 12)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Information security policy established and published | ⬜ Yes ⬜ No | | |
| Security policy reviewed at least annually | ⬜ Yes ⬜ No | | |
| Acceptable use policy for end-user technologies | ⬜ Yes ⬜ No | | |
| Targeted risk analysis performed at least annually | ⬜ Yes ⬜ No | | |
| PCI DSS scope documented and validated annually | ⬜ Yes ⬜ No | | |
| Security awareness training completed by all personnel (annual) | ⬜ Yes ⬜ No | | |
| Phishing and social engineering training provided | ⬜ Yes ⬜ No | | |
| Background checks for personnel before hire | ⬜ Yes ⬜ No ⬜ Partial | | |
| Third-party service providers validated for PCI compliance | ⬜ Yes ⬜ No ⬜ N/A | | |
| Incident response plan created and tested annually | ⬜ Yes ⬜ No | | |

---

## Appendix B: Cardholder Data Flow Diagram Template

Organizations should create a detailed data flow diagram showing how CHD enters, flows through, and exits the environment.

**Template Elements**:

```
[Customer] 
    â†"
[Payment Channel: POS / Web / Mobile / Phone]
    â†"
[Entry Point: Payment Terminal / Web Form / Payment Gateway]
    â†"
[Processing: Payment Application / Server]
    â†"
[Storage: Database / File System] ← (if stored)
    â†"
[Transmission: Processor / Acquirer / Payment Brand]
    â†"
[Exit: Authorization Response / Settlement]
```

**Required Documentation**:
- All systems that store, process, or transmit CHD
- Network zones and segmentation
- Data encryption points (in transit and at rest)
- Data retention policies and deletion procedures
- Third-party connections to CDE

---

**END OF TECHNICAL REFERENCE**

---

*This technical reference supports potential PCI DSS compliance requirements as determined in ISMS-POL-00. All regulatory applicability determinations and binding requirements are defined in ISMS-POL-00 and approved ISMS policy documents.*

*For organizations NOT processing payment cards, this document is for informational awareness only and does NOT create compliance obligations.*