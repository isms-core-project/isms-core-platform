**ISMS-OP-POL-A.5.9 — Asset Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Asset Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.9 |
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

- ISO/IEC 27001:2022 Control A.5.9 — Inventory of information and other associated assets

**Related Annex A Controls**:

| Control | Relationship to Asset Management |
|---------|----------------------------------|
| A.5.10 Acceptable use of information and other associated assets | Acceptable use rules reference inventoried assets |
| A.5.11 Return of assets | Asset return tracked in inventory; register updated on return/disposal |
| A.5.12–13 Information classification and labelling | Classification assigned to information assets in the register |
| A.5.14 Information transfer | Transfer controls based on asset classification |
| A.5.15–18 Access control and identity management | Access rights approved by asset owners |
| A.7.10 Storage media | Removable media registered as assets |
| A.7.14 Secure disposal or re-use of equipment | Disposal updates inventory status |
| A.8.1 User endpoint devices | Endpoint devices registered in asset inventory |
| A.8.8 Management of technical vulnerabilities | Patch management requires complete asset inventory |
| A.8.9 Configuration management | Configuration baselines linked to inventoried IT assets |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Access Control Policy
- Endpoint Security Policy
- Acceptable Use Policy
- Privacy and Protection of PII Policy

---

# Asset Management Policy

## Purpose

The purpose of this policy is the identification, registration, and management of organisation assets to ensure appropriate protection and accountability throughout their lifecycle.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk to protect personal data, including knowing what data exists, where it is stored, and who is accountable for it. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All organisation information, IT infrastructure, applications, physical assets, and cloud services deemed in scope by the ISO 27001 scope statement.

## Principle

Organisation assets are known, identified, classified, and managed with appropriate protection in place. You cannot protect what you do not know you have. Asset inventory is the foundation upon which all other security controls depend — risk assessment, access control, classification, vulnerability management, incident response, and business continuity planning.

### Asset Register

The organisation shall maintain the asset register in a centralised tool or platform (e.g., IT asset management system, CMDB, or structured spreadsheet with access controls). The register shall be accessible to asset owners, IT, and information security management team members, and protected against unauthorised modification.

---

## Asset Categories

The following categories of assets shall be inventoried:

| Category | Description | Examples |
|----------|-------------|----------|
| **Hardware** | Physical devices that process, store, or transmit information | Servers, workstations, laptops, mobile devices, network equipment (routers, switches, firewalls), printers |
| **Software and Licences** | Installed software and subscription services | Operating systems, business applications, development tools, security software, SaaS subscriptions |
| **Data and Information** | Digital and physical information with value to the organisation | Databases, file shares, backups, archives, contracts, intellectual property, configuration data |
| **Cloud Services** | Externally hosted services processing organisation data | IaaS (virtual machines, storage), PaaS (databases, platforms), SaaS (email, CRM, collaboration) |
| **Physical Assets** | Tangible resources supporting information security | Offices, server rooms, safes, removable media (USB drives, backup tapes) |
| **Personnel Competencies** | Key roles and specialist skills critical to operations | Critical roles (single points of failure), specialist certifications, institutional knowledge |

**Personnel competencies**: The register documents **roles and competencies**, not individual person records. Example: "Database Administrator competency (2 qualified staff)" — not individual names. Where a critical function is dependent on a single individual (single point of failure), this shall be flagged and a succession or knowledge transfer plan documented to mitigate the risk.

---

## Inventory of Hardware and IT Infrastructure

All hardware and IT infrastructure assets shall be registered in the asset inventory. For each asset, the following attributes shall be recorded:

**Mandatory Attributes**:

| Attribute | Description |
|-----------|-------------|
| **Asset ID** | Unique identifier (e.g., HW-0042) |
| **Asset Name** | Human-readable name |
| **Asset Type** | Category (server, laptop, network device, mobile, etc.) |
| **Description** | Purpose and function |
| **Owner** | Person accountable for the asset (name and role) |
| **Department** | Organisational unit |
| **Serial Number / Asset Tag** | Physical identifier |
| **Location** | Physical location (office, rack, site) |
| **Classification** | Per the Information Classification and Handling Policy |
| **Status** | Active / In Storage / Decommissioned / Disposed |
| **Last Reviewed** | Date the record was last verified |

**Recommended Additional Attributes**:

- Criticality (High / Medium / Low) — based on: **High** = loss would cause significant business disruption, regulatory breach, or data loss; **Medium** = loss would cause moderate impact, workaround available; **Low** = loss causes minimal impact, easily replaceable
- IP address or hostname (for network-connected assets)
- Manufacturer, model, and firmware/OS version
- Acquisition date and warranty expiry
- Encryption status

---

## Inventory of Software and Licence Assets

Software and software licences shall be registered in the asset inventory. For each software asset, the following attributes shall be recorded:

| Attribute | Description |
|-----------|-------------|
| **Software Name** | Product name and publisher |
| **Version** | Current version deployed |
| **Owner** | Person accountable |
| **Licence Type** | Perpetual, subscription, open-source, freeware |
| **Licence Count** | Number of licences purchased vs. deployed |
| **Renewal Date** | Subscription expiry or next renewal |
| **Deployment Location** | Where the software is installed or hosted |
| **Business Purpose** | Why the software is used |
| **Support Status** | Vendor-supported / End of Life (EOL) / End of Support (EOS) |

Only organisation-approved and licensed software shall be deployed. Unauthorised software discovered during inventory reviews shall be reported to the information security management team for assessment and removal.

Software that has reached end of life or end of support shall be flagged and prioritised for upgrade or replacement. Where unsupported software cannot be immediately replaced, the risk shall be documented in the risk register with compensating controls.

---

## Inventory of Cloud and SaaS Services

Cloud services (IaaS, PaaS, SaaS) shall be registered in the asset inventory alongside traditional software. For each cloud service, the following additional attributes shall be recorded:

| Attribute | Description |
|-----------|-------------|
| **Service Provider** | Vendor name |
| **Service Type** | IaaS / PaaS / SaaS |
| **Data Residency** | Country or region where data is stored |
| **Data Classification** | Classification of data processed by the service |
| **SSO Integration** | Whether the service is integrated with the organisation's identity provider |
| **Contract Owner** | Person responsible for the vendor relationship |
| **Renewal Date** | Contract or subscription expiry |

Cloud services shall be classified as:

- **Sanctioned**: Approved by IT and security for organisation use.
- **Tolerated**: Known but not formally approved; under review (maximum 90 days before sanctioned or prohibited).
- **Prohibited**: Not authorised; must be removed.

New cloud services shall be registered in the asset inventory **before** organisation data is processed in the service (or within 5 business days for emergency deployments with CISO approval).

Unsanctioned cloud services (shadow IT) shall be identified through periodic reviews of expense reports, SSO logs, and network traffic. Newly discovered services shall be assessed for security and data protection compliance before being sanctioned.

---

## Inventory of Data and Information Assets

Data and information assets shall be identified, and an inventory drawn up and maintained. For each data asset, the following attributes shall be recorded:

| Attribute | Description |
|-----------|-------------|
| **Asset Name** | Name of the dataset, database, or information store |
| **Owner** | Person accountable (the business party, not the technical custodian) |
| **Classification** | Per the Information Classification and Handling Policy |
| **Storage Location** | System or service where the data resides |
| **Data Residency** | Country where data is physically stored |
| **Retention Period** | How long the data is kept, per retention requirements |
| **Personal Data** | Whether the dataset contains personal data (Yes / No) |

Where data assets contain personal data, the register should capture additional fields to support Swiss nFADP compliance:

- Categories of data subjects
- Purpose of processing
- Categories of recipients
- Whether cross-border transfers occur (and applicable safeguards)

This information may be recorded in the data asset inventory or in a separate **Register of Processing Activities (ROPA)** per nFADP Art. 12, with a cross-reference between the two registers.

---

## Ownership of Assets

An owner shall be assigned to every inventoried asset. Ownership shall not be left blank.

**Owner** means the person accountable for the asset's security throughout its lifecycle. It does not mean legal property rights. The owner may delegate day-to-day management to a custodian (e.g., IT manages the server, but the business unit head owns the data on it), but accountability remains with the owner.

### Owner Responsibilities

Asset owners shall:

- Ensure their assets are inventoried and records are accurate.
- Classify assets according to business value and risk.
- Review inventory records for owned assets at least annually.
- Approve access requests to owned assets.
- Report security incidents affecting owned assets.
- Participate in asset lifecycle decisions (decommissioning, archival, disposal).

### Ownership Assignment

- New assets shall have an owner assigned at the time of registration.
- Where ownership is unclear, the information security management team shall escalate to the appropriate manager for determination within **30 calendar days**.
- Assets without an assigned owner beyond 30 days shall be escalated to the CISO with documented justification.
- Ownership changes (e.g., employee departure, role change) shall be updated in the register within **5 business days**.

### Orphaned Assets

**Discovered unregistered assets**: Assets found in use but not in the inventory shall be immediately registered with a temporary owner (the discoverer's manager or IT), investigated within **14 business days** to determine the business owner and purpose, and either formally assigned to a permanent owner or decommissioned.

**Owner departure**: When an asset owner leaves the organisation, ownership shall be reassigned to the departing employee's manager or designated successor within **10 business days** of departure. Assets without reassigned ownership after 30 days shall be escalated to the CISO.

---

## Asset Lifecycle

### Registration

All assets shall be registered in the asset inventory within **5 business days** of acquisition or deployment. Assets shall not be connected to the network or used to process organisation data until registered.

### Maintenance and Change

Any change to an asset's owner, location, classification, or status shall be reflected in the register within **5 business days** of the change.

### Decommissioning and Disposal

When an asset is decommissioned or disposed of:

- Data shall be securely erased or destroyed in line with the Information Classification and Handling Policy, using methods compliant with **NIST SP 800-88** (Guidelines for Media Sanitization): Clear (logical overwrite) for INTERNAL data, Purge (cryptographic erasure or degauss) for CONFIDENTIAL data, or Destroy (physical destruction) where required.
- Software licences shall be reclaimed or deactivated.
- The asset register shall be updated to reflect the disposal, including the date and method of disposal.
- For assets that stored confidential or personal data, evidence of data sanitisation shall be retained (e.g., certificate of destruction, wipe confirmation log).

### BYOD (Bring Your Own Device)

Where BYOD is permitted, personally-owned devices used to access organisation data shall be registered in the asset inventory with a flag indicating personal ownership. Minimum BYOD registration attributes:

- Device type and operating system
- Employee name
- Business use scope (email only, full access, etc.)
- MDM enrolment status
- BYOD agreement signed (date)

Upon termination or contract end, organisation data shall be wiped from the personal device, and the BYOD record shall be updated.

---

## Acceptable Use of Assets

Acceptable use of assets shall be in line with the Acceptable Use Policy.

Users shall not install unauthorised software, connect unapproved devices to the network, or use organisation assets for purposes outside the scope of their role.

---

## Return of Assets

All employees and third-party users shall return all organisation assets in their possession upon termination of their employment, contract, or agreement.

Where an employee or third-party user has used their own personal equipment (BYOD), procedures shall ensure that all organisation information is transferred to the organisation and securely erased from the personal device.

During notice periods, the organisation shall take reasonable measures to prevent unauthorised copying of organisation information by departing employees or third-party users.

The asset register shall be updated to reflect all returned, reassigned, or disposed assets.

---

## Asset Review

The asset inventory shall be reviewed at the following intervals:

| Review Type | Frequency | Responsible |
|-------------|-----------|-------------|
| **Event-driven updates** | Ongoing (within 5 business days of change) | Asset owners and IT |
| **Owner attestation** | Annually | Each asset owner confirms accuracy of their assigned assets |
| **Full inventory audit** | Annually (aligned with management review) | Information security management team |
| **Cloud/SaaS discovery review** | Quarterly | IT and information security management team |
| **Software licence compliance** | Semi-annually | IT |

Department heads shall confirm their asset lists are current during the annual review. Discrepancies shall be investigated and resolved within 30 days.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **Asset inventory register** (hardware, software, data, cloud services — with mandatory attributes populated) — *maintained in centralised tool; exported for audit evidence*
- **Asset owner assignment records** — *target: 100% of assets with assigned owners; measured quarterly*
- **Owner attestation records** (annual review confirmations) — *signed off by each asset owner; retained for 3 years*
- **Cloud/SaaS service register** with data residency and classification — *updated per event; reviewed quarterly*
- **Software licence compliance records** (licences purchased vs. deployed) — *audited semi-annually*
- **Asset disposal records** (date, method, NIST SP 800-88 sanitisation evidence, certificates of destruction) — *retained for 5 years*
- **BYOD registration records and agreement signatures** (if applicable) — *updated per event; reviewed annually*
- **Annual inventory audit report** with findings and remediation actions — *presented at management review*
- **Inventory completeness metric** — *target: ≥95% of known assets registered with complete mandatory attributes; measured annually*
- **Shadow IT discovery reports** — *quarterly reviews documented with assessment outcomes*

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, asset register audits, owner attestation reviews, licence compliance checks, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to asset management standards, organisational changes (acquisitions, restructuring), cloud service adoption, regulatory changes, and lessons learned from incidents and audits.

---

# Areas of the ISO 27001 Standard Addressed

Asset Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | **5.9 Inventory of information and other associated assets** |
| | 5.10 Acceptable use of information and other associated assets |
| | 5.11 Return of assets |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures (requires knowing what data exists and where); Art. 12 — Register of Processing Activities |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 5 — Accountability principle; Art. 30 — Records of processing activities; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 5.9 — Inventory of information and other associated assets |
| ISO/IEC 27002:2022 | Section 5.9 — Implementation guidance |
| NIST SP 800-53 Rev 5 | CM-8 (System Component Inventory), PM-5 (System Inventory) |
| CIS Controls v8 | Control 1 (Inventory and Control of Enterprise Assets), Control 2 (Inventory and Control of Software Assets) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
