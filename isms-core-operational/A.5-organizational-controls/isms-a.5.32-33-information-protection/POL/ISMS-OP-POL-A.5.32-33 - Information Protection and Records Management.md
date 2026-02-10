<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.32-33:operational:OP-POL:a.5.32-33 -->
**ISMS-OP-POL-A.5.32-33 — Information Protection and Records Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Protection and Records Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.32-33 |
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

- ISO/IEC 27001:2022 Control A.5.32 — Intellectual property rights
- ISO/IEC 27001:2022 Control A.5.33 — Protection of records
- ISO/IEC 27001:2022 Clause 7.5 — Documented information

**Related Annex A Controls**:

| Control | Relationship to Information Protection and Records Management |
|---------|--------------------------------------------------------------|
| A.5.9 Inventory of information and other associated assets | IP assets and records included in asset inventory |
| A.5.10 Acceptable use of information | Acceptable use rules govern IP and records handling |
| A.5.12–13 Information classification and labelling | Classification scheme applied to IP and records |
| A.5.34 Privacy and protection of PII | Personal data records subject to privacy requirements |
| A.6.5 Responsibilities after termination or change of employment | Exit procedures ensure IP return/deletion |
| A.6.6 Confidentiality or non-disclosure agreements | NDAs required for third-party IP access |
| A.8.10 Information deletion | Secure deletion procedures for records disposal |
| A.8.12 Data leakage prevention | DLP controls protect IP from exfiltration |
| A.8.13 Information backup | Backup protects records availability |

**Related Internal Policies**:

- Asset Management Policy
- Information Classification and Handling Policy
- Privacy and Protection of PII Policy
- Acceptable Use Policy
- Information Deletion Policy

---

# Information Protection and Records Management Policy

## Purpose

The purpose of this policy is to ensure that intellectual property rights are appropriately protected and that records are protected from loss, destruction, falsification, unauthorised access, and unauthorised release in accordance with legislative, regulatory, contractual, and business requirements.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk, ensuring that records containing personal data are retained, protected, and disposed of in compliance with data protection principles. Swiss Code of Obligations (CO) Art. 958f requires retention of bookkeeping records and supporting documentation for 10 years. Where the organisation processes data of individuals in the EU/EEA, GDPR storage limitation (Art. 5(1)(e)) and erasure requirements (Art. 17) also apply, subject to overriding legal retention obligations.

**Combined Control Approach**: Controls A.5.32 (Intellectual Property Rights) and A.5.33 (Protection of Records) are implemented together because they share common governance structures, protection mechanisms, and lifecycle management requirements.

## Scope

All employees and third-party users.

All intellectual property (patents, copyrights, trademarks, trade secrets, proprietary software, source code), all records (business, financial, personnel, technical, operational, security), and all formats (physical documents, electronic files, databases, emails).

All environments in which IP or records are created, processed, stored, or transmitted.

## Principle

Intellectual property shall be identified, classified, and protected in accordance with its value and applicable legal requirements. Records shall be retained for required periods, protected from loss and falsification, and disposed of securely when no longer needed. Compliance with software licensing and third-party IP rights shall be maintained at all times.

---

## Definitions

| Term | Definition |
|------|------------|
| **Intellectual Property (IP)** | Creations of the mind: inventions, literary and artistic works, symbols, names, designs, and proprietary business information |
| **Trade Secret** | Confidential business information that provides a competitive advantage and is subject to reasonable efforts to maintain secrecy |
| **Record** | Information created, received, and maintained as evidence of business activity or to fulfil legal obligations |
| **Retention Period** | The required duration for keeping a record before authorised disposal |
| **Legal Hold** | A preservation requirement due to litigation, investigation, or regulatory action that overrides normal disposal schedules |
| **Software Asset Management (SAM)** | Processes and tools for managing, controlling, and protecting software assets throughout their lifecycle |

---

## IP and Records Management Systems

The organisation shall use the following systems to manage intellectual property and records:

| Function | System/Tool | Owner | Access Control |
|----------|-------------|-------|----------------|
| **IP Register** | [e.g., Legal case management system, SharePoint, Excel register] | Legal Counsel | Restricted to Legal, CISO, Executive Management |
| **Software Asset Management (SAM)** | [e.g., Snow License Manager, ServiceNow SAM, Flexera, manual spreadsheet] | IT Operations | IT Managers, Procurement, CISO |
| **Retention Schedule** | [e.g., Documented in policy appendix, GRC platform, legal database] | Legal Counsel | All personnel (read-only); Legal Counsel (edit) |
| **Records Disposal Log** | [e.g., Spreadsheet, GRC platform, ticketing system] | Records Manager | Records Manager, Legal Counsel, Internal Audit |
| **Legal Hold Register** | [e.g., Legal case management system, spreadsheet] | Legal Counsel | Legal Counsel only |
| **Source Code Repository** | [e.g., GitHub Enterprise, GitLab, Bitbucket] | Development Manager | Developers (role-based); CISO (audit access) |
| **Version Control (documents)** | [e.g., SharePoint, Confluence, Git] | IT Operations | Document owners and authorised users |

**Integration**: Where feasible, IP and records registers should integrate with the asset management system (per Asset Management Policy) to ensure all IP and critical records are tracked as organisational assets.

---

## Intellectual Property Protection (A.5.32)

### IP Identification and Classification

The organisation shall identify and classify all intellectual property assets:

| Category | Examples | Protection Level |
|----------|----------|------------------|
| **Trade Secrets** | Algorithms, formulas, processes, client lists | Restricted (highest protection) |
| **Proprietary Software** | Source code, development tools, internal scripts | Confidential minimum |
| **Business Methods** | Unique processes, methodologies, business models | Confidential |
| **Technical Documentation** | Architecture diagrams, designs, specifications | Confidential |
| **Trademarks and Branding** | Logos, brand materials, domain names | Internal (usage controlled) |

### IP Register

An IP register shall be maintained recording all significant intellectual property assets. The register shall include, at minimum:

- IP asset name and description.
- Category (per table above).
- Business owner and custodian.
- Classification (per Information Classification and Handling Policy).
- Location or system where stored.
- Third-party sharing allowed (Yes/No).
- Legal protection status (patent, copyright, trademark, trade secret).
- Last review date and next review date.

The IP register shall be reviewed **annually** by Legal Counsel (or equivalent role) and the CISO.

### IP Protection Controls

Protection controls shall be implemented based on IP type and classification:

**Technical Protection**:

| IP Type | Required Controls |
|---------|-------------------|
| **Source Code** | Access control, version control (e.g., Git), code review, export restrictions |
| **Trade Secrets** | Need-to-know access, encryption at rest and in transit, DLP monitoring |
| **Designs and Specifications** | Access logging, sharing restrictions, watermarking where appropriate |
| **Research Data** | Encryption, access control, backup protection |

**Administrative Protection**:

- Confidentiality clauses in all employment contracts.
- Non-disclosure agreements (NDAs) for third-party access to IP.
- IP ownership clauses in vendor and contractor agreements.
- Exit procedures ensuring return or verified deletion of IP materials upon departure.

**Legal Protection**:

- Patent applications filed where commercially appropriate.
- Copyright notices applied to protected materials.
- Trademark registrations maintained.
- Trade secret documentation maintained to support legal defence.

### Third-Party Access to Intellectual Property

All third parties (vendors, consultants, contractors, partners) accessing organisation IP or confidential records shall sign a Non-Disclosure Agreement (NDA) **before** access is granted.

**NDA Approval Process**:

1. **Request**: Business owner requests third-party access via [ticketing system/contract request].
2. **NDA Selection**: Legal Counsel provides appropriate NDA template (unilateral, mutual, or custom).
3. **Negotiation**: Legal Counsel negotiates terms if third party proposes changes.
4. **Approval**: Legal Counsel approves final NDA.
5. **Execution**: Both parties sign (electronic signature acceptable).
6. **Registration**: Legal Counsel registers executed NDA in legal agreement register with: third-party name, NDA type, effective date, expiration date, scope of access, IP assets covered.
7. **Access Grant**: Only after executed NDA is registered may IT Operations or business owner grant system access.
8. **Renewal**: For ongoing relationships, NDAs shall be reviewed and renewed before expiration.

**IP Return/Deletion on Exit**:

- NDA shall require third party to return or certify deletion of all organisation IP upon contract termination.
- Business owner shall verify return/deletion and document verification in agreement register.
- If third party fails to return/delete IP within **30 days**, escalate to Legal Counsel.

**NDA Register Review**: Legal Counsel shall review NDA register **quarterly** to identify expiring NDAs requiring renewal and terminated relationships requiring IP return verification. Target: 100% of active third parties with valid NDAs.

### Software Licensing and Compliance

All software used by the organisation shall be properly licensed and compliant:

- Software shall be acquired through official channels only. Evidence of valid licences shall be retained.
- Software shall be used in accordance with licence terms.
- A **Software Asset Management (SAM) register** shall be maintained recording: software name and version, licence type (commercial, open-source, freeware), person responsible, number of licences purchased vs. in use, licence location (key, certificate, portal), deployment locations, and review dates.
- **Only software supported by the manufacturer** shall be used in production. End-of-life software shall be identified and migrated per the vulnerability management policy.
- Software shall be installed only by authorised personnel.

### Software Asset Management (SAM) Process

**SAM Register Maintenance**: Owner: IT Operations Manager. Update frequency: real-time for new software deployments; full reconciliation quarterly. Tool: [Specify SAM tool name].

**Quarterly Reconciliation Process**:

1. **Discovery** (Week 1): Run automated software inventory scans across all endpoints and servers using SAM tool or endpoint management agent.
2. **Procurement Reconciliation** (Week 2): Compare discovered software against procurement records and licence entitlements.
3. **Gap Analysis** (Week 2): Identify unlicensed software (deployed but no licence), over-deployed software (more installs than licences), and unused licences (paid licences not deployed).
4. **Remediation** (Week 3–4):
   - **Critical**: Unlicensed business-critical software — purchase licence within **5 business days** or uninstall.
   - **Standard**: Over-deployment — harvest/reallocate licences within **30 days** or purchase additional.
   - **Low**: Freeware/open-source compliance issues — review licence and document compliance within **90 days**.
5. **Management Review** (End of quarter): IT Operations Manager presents SAM report to CISO including total software assets, licence compliance rate, cost optimisation opportunities, and exception status.
6. **Sign-off**: CISO and CFO approve quarterly SAM report.

**Unlicensed Software Response**:

- Immediate suspension of access if licence violation creates legal risk.
- User notification and alternative approved software recommendation.
- Escalation to user's manager and CISO within 24 hours.

**SAM Metrics**:

| Metric | Target |
|--------|--------|
| Licence compliance rate | 100% |
| Unlicensed software remediation time (critical) | <5 business days |
| Unused licence identification | >80% of paid licences actively used |

Unlicensed software use is prohibited.

### Third-Party IP Compliance

The organisation shall comply with third-party intellectual property rights:

- **Copyright verification** before using third-party content.
- **Proper attribution** in accordance with licence terms.
- **Open-source licence compliance**: see Open-Source Software Licence Compliance below.
- **Creative Commons** and other content licence restrictions shall be honoured.

### Open-Source Software Licence Compliance

Before deploying any open-source software (OSS) or incorporating OSS components into organisation applications:

1. **Identification**: Developer identifies OSS component and its licence (from package manager metadata, LICENSE file, or repository).
2. **SBOM Generation**: Generate Software Bill of Materials (SBOM) listing all OSS dependencies and their licences using [tool name, e.g., Syft, Trivy, Snyk].
3. **Licence Review**: IT Security Analyst or Development Manager reviews SBOM for:
   - **Approved licences**: MIT, Apache 2.0, BSD (2-clause, 3-clause), ISC.
   - **Restricted licences** (require CISO approval): GPL v2/v3 (copyleft obligations), LGPL, AGPL, MPL.
   - **Prohibited licences**: Custom licences with unclear terms, licences incompatible with commercial use.
4. **Approval**:
   - **Approved licences**: Development Manager authorises deployment.
   - **Restricted licences**: CISO reviews and approves/denies based on copyleft risk, project scope, and legal consultation if needed.
   - **Prohibited licences**: Denied; alternative component required.
5. **Documentation**: Record approved OSS components in OSS register: component name/version, licence type, approval date, approver, project/system using component, last SBOM review date.
6. **Ongoing Monitoring**: Quarterly SBOM regeneration to detect new dependencies or licence changes.

**Copyleft Obligations**: If GPL-licensed code triggers copyleft obligations (e.g., distribution of modified binaries), Development Manager shall provide source code to recipients per GPL terms, document compliance in OSS register, and notify Legal Counsel.

**Licence Violation Response**: If a licence violation is discovered (OSS used outside licence terms), immediate remediation (remove component, stop distribution, or obtain proper licence), incident creation per Incident Management Policy, and Legal Counsel consultation within 24 hours for high-risk violations.

**OSS Register Review**: Development Manager shall review OSS register **quarterly** to verify all components are properly licensed and documented. Target: 100% OSS components with valid licence approval.

---

## Records Protection (A.5.33)

### Records Classification and Retention

The organisation shall classify records based on retention requirements and protection needs:

| Category | Retention Period | Protection Requirement | Examples |
|----------|-----------------|----------------------|----------|
| **Legal and Contracts** | Duration + 10 years | Confidential, integrity protected | Contracts, legal agreements, NDAs |
| **Financial** | 10 years (Swiss CO Art. 958f) | Confidential, tamper-evident | Invoices, ledgers, tax records, audit reports |
| **Personnel** | Employment + 10 years | Confidential, privacy protected | HR files, payroll records, performance reviews |
| **Regulatory and Compliance** | Per applicable regulation | Per classification | ISMS evidence, audit reports, certifications |
| **Technical** | System lifecycle + 3 years | Internal minimum | Configurations, change records, architecture docs |
| **Operational** | 3–7 years | Internal | Meeting minutes, project files, correspondence |
| **Security and Audit** | 2–7 years | Confidential, integrity protected | Access logs, incident records, investigation files |

### Retention Schedule

A documented retention schedule shall be maintained:

- **Owner**: Legal Counsel (or equivalent role).
- **Content**: Record category, retention period, retention basis (law, contract, business need), disposal method, and record owner.
- **Review**: Annually, with regulatory alignment verified.
- **Conflict resolution**: Where multiple regulations apply, the most stringent retention requirement shall prevail. Where a deletion or erasure request conflicts with legal retention obligations, retention takes precedence — the records shall be access-restricted, the decision documented with Legal Counsel approval, and DPO involvement obtained for personal data.

**Retention Schedule Example Format**:

| Record Category | Record Type | Retention Period | Legal Basis | Disposal Method | Record Owner |
|----------------|-------------|------------------|-------------|-----------------|--------------|
| Financial | Invoices and receipts | 10 years | Swiss CO Art. 958f | Secure deletion (NIST SP 800-88) | Finance Manager |
| Financial | General ledger | 10 years | Swiss CO Art. 958f | Secure deletion | Finance Manager |
| Personnel | Employment contracts | Employment + 10 years | Swiss CO Art. 958f | Secure shredding (P-4) | HR Manager |
| Personnel | Payroll records | Employment + 10 years | Swiss CO Art. 958f | Secure deletion | HR Manager |
| Personnel | Performance reviews | Employment + 5 years | Business need | Secure deletion | HR Manager |
| Legal | Contracts and NDAs | Contract end + 10 years | Swiss CO Art. 958f | Secure deletion | Legal Counsel |
| ISMS | ISO 27001 audit evidence | 3 audit cycles (9 years) | ISO 27001 Clause 9.2 | Secure deletion | CISO |
| ISMS | Risk assessments | Superseded + 3 years | ISO 27001 Clause 6.1 | Secure deletion | CISO |
| ISMS | Security logs | 12 months | DSV Art. 4 (where applicable) | Secure deletion | IT Security |
| Technical | System configuration records | System lifecycle + 3 years | Business need | Standard deletion | IT Operations |
| Operational | Meeting minutes | 3 years | Business need | Standard deletion | Meeting owner |

**Grace Period**: Records may be retained up to 12 months beyond the minimum retention period to allow for orderly disposal processes. Records shall not be retained indefinitely without documented justification.

**Annual Review**: Legal Counsel shall review the retention schedule annually and update for regulatory changes, new record types, or business needs.

### Retention Controls

| Control | Requirement |
|---------|-------------|
| **Minimum retention** | Records shall not be deleted before the retention period expires |
| **Maximum retention** | Records should be deleted after the retention period plus a grace period (maximum 12 months), supporting GDPR storage limitation and nFADP data minimisation |
| **Legal hold** | Litigation or investigation holds override normal deletion schedules; holds are indefinite until formally released by Legal Counsel |
| **Integrity protection** | Critical records shall have integrity verification (checksums, digital signatures, or tamper-evident storage) |

**Critical records** include: regulatory and audit evidence, financial ledgers and tax documentation, security and access logs, signed contracts and legal agreements, HR master records, and incident investigation records.

### Records Protection Controls

Records shall be protected throughout their lifecycle:

**Integrity**:

- Critical records stored with integrity verification (checksums, hash values, or digital signatures).
- Audit logs tamper-protected (write-once storage, append-only, or cryptographic chaining).
- Version control for records requiring change tracking.

**Integrity Verification Process**:

| Record Type | Verification Method | Tool |
|-------------|---------------------|------|
| Electronic records (files) | SHA-256 hash comparison | [e.g., PowerShell Get-FileHash, Linux sha256sum, GRC platform] |
| Databases | Database integrity checks | Database native tools (e.g., SQL Server DBCC CHECKDB) |
| Audit logs | Tamper-evident storage verification | SIEM native integrity verification or cryptographic log signing |
| Digital documents | Digital signature verification | Adobe Acrobat, DocuSign verification, or equivalent |

- **Frequency**: Annually (or more frequently for high-risk records).
- **Owner**: IT Operations (electronic); Records Manager (physical with digital signatures).
- **Process**: Generate current hash/checksum, compare to baseline hash stored at record creation or last verification.

**Verification Failure Response**:

1. **Immediate isolation**: Quarantine affected record to prevent further modification.
2. **Incident creation**: Create security incident per Incident Management Policy.
3. **Investigation**: Determine cause (corruption, unauthorised modification, system error).
4. **Restoration**: Restore from verified backup if available.
5. **Notification**: Notify Legal Counsel and CISO within 4 hours for critical records (financial, legal, regulatory).
6. **Root cause analysis**: Document cause and implement corrective action.

**Availability**:

- Backup according to criticality (per backup and recovery policy).
- Geographic redundancy for critical records where feasible.
- Media refresh and format migration before degradation renders records unreadable.

**Backup Requirements by Record Category**:

| Record Category | Backup Frequency | Backup Retention | RTO | RPO |
|----------------|------------------|------------------|-----|-----|
| Financial records | Daily | 10 years (online: 90 days; archive: 9+ years) | 24 hours | 24 hours |
| Legal contracts | Daily | Duration + 10 years | 24 hours | 24 hours |
| Personnel records | Daily | Employment + 10 years | 48 hours | 24 hours |
| ISMS audit evidence | Weekly | 9 years | 72 hours | 1 week |
| Security logs | Daily (continuous forwarding to SIEM) | 12 months (online: 90 days; archive: 9 months) | 4 hours | 1 hour |
| IP assets (source code) | Continuous (version control) + daily backup | Indefinite (version history retained) | 4 hours | Real-time (via version control) |

- Backup restoration testing shall be performed **quarterly** for critical records (select 3 sample records from each category, perform test restoration, verify integrity and completeness). Target: 100% successful restoration.
- Critical records shall have backups stored in a geographically separate location (minimum 100 km from primary site).
- Backups containing confidential records shall be encrypted (AES-256 or equivalent).
- Backup deletion requires dual approval (IT Operations Manager + CISO).

**Confidentiality**:

- Access control based on need-to-know and role.
- Encryption for confidential records at rest and in transit.
- Physical protection for paper records (locked storage, controlled access).

### Records Disposal

Records shall be disposed of securely when the retention period expires (and no legal hold applies):

| Record Type | Disposal Method |
|-------------|-----------------|
| **Paper (Confidential or above)** | Cross-cut shredding (DIN 66399 P-4 minimum) or witnessed incineration |
| **Paper (Internal)** | Standard shredding (P-3 minimum) |
| **Electronic (Confidential or above)** | Secure deletion per information deletion policy (NIST SP 800-88: Clear, Purge, or Destroy) |
| **Electronic (Internal)** | Standard deletion with verification |
| **Media (HDDs, SSDs, tapes)** | Degaussing, physical destruction, or certified third-party destruction |

**Disposal documentation**:

- Disposal records shall be maintained for the audit trail (minimum 3 years).
- Certificates of destruction shall be obtained for confidential and above records.
- Third-party destruction shall be verified through vendor certifications and chain-of-custody documentation.

### Records Disposal Process

**Automated Disposal** (for electronic records with system-managed retention):

1. **Expiry Identification**: Retention management system (or script) identifies records where retention period has expired.
2. **Pre-Disposal Hold Check**: System verifies no active legal holds apply to the record.
3. **Owner Notification** (30 days before disposal): Record owner receives notification with scheduled disposal date; owner may submit extension request with business justification.
4. **Extension Request** (if needed): Owner submits request to Legal Counsel with justification; Legal Counsel approves/denies within 5 business days.
5. **Disposal Execution**: System performs secure deletion per method defined in retention schedule.
6. **Disposal Logging**: System logs disposal event (record ID, disposal date, method, user/system initiating disposal).

**Manual Disposal** (for physical records or electronic records requiring manual review):

1. **Disposal Request**: Records Manager generates quarterly disposal list from retention schedule.
2. **Owner Review**: Record owners review list and confirm disposal authorisation within 10 business days.
3. **Legal Hold Verification**: Legal Counsel confirms no active holds apply.
4. **Disposal Authorisation**: Records Manager authorises disposal.
5. **Physical Disposal**: Confidential paper cross-cut shredded (DIN 66399 P-4) on-site or by certified vendor; media (HDDs, SSDs) physically destroyed or degaussed by certified vendor.
6. **Certificate of Destruction**: Obtain certificate from destruction vendor within 5 business days.
7. **Disposal Documentation**: Records Manager logs disposal in disposal register (disposal date, record description, method, certificate reference, authorising person).

**Disposal Verification**: Internal Audit shall sample disposal records annually to verify disposal occurred within timeframe, certificates of destruction obtained for confidential records, and legal holds were checked. Target: 100% compliance with disposal procedures.

### Legal Hold Process

**Legal Hold Triggers**: Actual or anticipated litigation, government investigation or subpoena, internal investigation (fraud, misconduct, data breach), or regulatory enforcement action.

**Legal Hold Issuance**:

1. **Hold Notification**: Legal Counsel issues formal legal hold notice documenting: case/matter name and number, scope (specific systems, date ranges, custodians, keywords), effective date, preservation obligations, and contact for questions.
2. **Custodian Notification** (within 24 hours): Legal Counsel sends hold notice to all identified custodians via email. Custodians acknowledge receipt and understanding within **2 business days**. Notice shall state: *"You are hereby instructed to preserve and not delete, modify, or destroy any records related to [matter]. This includes emails, documents, files, and any other information in your possession or control. Normal deletion activities must be suspended. This hold remains in effect until formally released by Legal Counsel."*
3. **IT System Suspension**: IT Operations suspends automated deletion for affected systems (email retention, log rotation, backup overwrites). Affected systems/data flagged with hold status. IT confirms suspension within **48 hours** and provides written confirmation to Legal Counsel.
4. **Hold Tracking**: Legal Counsel maintains Legal Hold Register recording: hold ID, matter name, issue date, scope, affected systems, custodians, acknowledgement status, monthly review date, release date (when lifted).
5. **Monthly Review**: Legal Counsel reviews all active holds monthly to verify hold is still necessary, update scope if case evolves, and confirm IT suspension remains active.
6. **Hold Release**: When matter concludes, Legal Counsel issues formal hold release notice. Custodians and IT Operations notified within **24 hours**. IT Operations re-enables normal deletion schedules. Records Manager may then dispose of records per normal retention schedule.

**Compliance Verification**: Internal Audit shall verify legal hold compliance annually (sample custodian acknowledgements, verify IT suspension was implemented).

---

## Privacy Protections for Records Containing Personal Data

Where records contain personal data (as defined by Swiss nFADP or GDPR):

**Access Control**:

- Personnel records (HR files, payroll, performance reviews): access restricted to HR team and employee's direct manager on need-to-know basis.
- Security logs containing user activity: access restricted to IT Security Team and Internal Audit; logs shall not be browsed by line managers for employee monitoring.
- Financial records with personal identifiers: access restricted to Finance team and authorised auditors.

**Pseudonymisation**: Where feasible, logs and records used for security analysis should pseudonymise personal identifiers (replace names/emails with anonymised IDs) while retaining ability to re-identify if needed for investigation.

**Data Subject Rights**: Employees and customers may exercise rights under nFADP/GDPR (access, rectification, erasure, restriction):

1. Data subject submits request to DPO or HR (for employee records).
2. DPO/HR verifies identity.
3. Records Manager identifies all records containing data subject's personal data.
4. If **access request**: provide copy within 30 days (nFADP Art. 25), free of charge for first request.
5. If **erasure request**: if retention obligation applies (e.g., Swiss CO Art. 958f), deny erasure but restrict access and document decision with Legal Counsel; if no retention obligation, perform secure deletion per disposal procedures.
6. Document all data subject requests and responses in data subject request register.

**Retention Minimisation**: Personal data in records shall not be retained longer than necessary. Annual review: Records Manager and DPO shall review retention schedule to verify personal data retention periods remain justified and comply with nFADP Art. 6 (proportionality).

**Breach Notification**: If integrity verification fails or unauthorised access to records containing personal data is detected, follow Data Breach Notification procedures per Privacy and Protection of PII Policy. Swiss nFADP Art. 24 requires notification to FDPIC "as soon as possible" for high-risk breaches.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|--------------------|
| **CISO** | Policy ownership; IP protection controls; records security requirements; exception authorisation for IP access |
| **Legal Counsel** | IP registration and legal protection; retention schedule ownership; legal hold management; disposal approval for uncertain cases |
| **Records Manager** | Retention schedule maintenance; disposal oversight; register management; compliance tracking |
| **IT Operations** | Technical controls implementation; backup and integrity verification; secure disposal execution |
| **Information Owners** | Classification and retention decisions for owned records and IP; review and approval of disposal |
| **All Personnel** | Handle IP and records per policy; report violations or concerns; do not use unlicensed software |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **IP register** with ownership, classification, and protection status | Legal Counsel / CISO | *Maintained continuously; reviewed annually; target: 100% of IP assets registered with designated owner* |
| 2 | **Software Asset Management (SAM) report** showing licence reconciliation and compliance | IT Operations | *Quarterly reconciliation; target: 100% licence compliance* |
| 3 | **Retention schedule** with regulatory alignment and approval records | Legal Counsel | *Reviewed annually; version-controlled; approved by Executive Management* |
| 4 | **Disposal records** and certificates of destruction | Records Manager | *Per event; retained 3 years; target: 100% of expired records disposed per schedule* |
| 5 | **Integrity verification results** for critical records (checksums, backup tests) | IT Operations | *Annually; target: 100% pass rate for critical records* |
| 6 | **Legal hold register** with active holds, scope, and review records | Legal Counsel | *Active holds reviewed monthly; release requires sign-off* |
| 7 | **NDA and IP agreement records** for third-party access | Legal Counsel / HR | *Per engagement; retained for agreement duration + 10 years* |
| 8 | **Open-source licence compliance records** (SBOM, licence review, approval) | IT Operations / Development | *Per adoption; reviewed quarterly where open-source is used* |
| 9 | **Training records** for IP and records handling awareness | Information Security / HR | *Per event; target: 100% of personnel with IP/records access trained* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, IP register reviews, software licence audits, retention schedule compliance checks, disposal record sampling, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Retention exceptions require Legal Counsel approval. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Unlicensed software use may additionally expose the organisation to legal liability.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to intellectual property law, records management regulations (including nFADP and GDPR developments), software licensing models, technology changes affecting records formats, audit findings, and lessons learned from IP incidents or disposal failures.

---

# Areas of the ISO 27001 Standard Addressed

Information Protection and Records Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.9 Inventory of information and other associated assets |
| Clause 7.3 Awareness | 5.36 Compliance with policies, rules, and standards |
| Clause 7.5.1 Documented information — General | **5.32 Intellectual property rights** |
| Clause 7.5.3 Control of documented information | **5.33 Protection of records** |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.10 Information deletion |
| | 8.19 Installation of software on operational systems |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss CO (Code of Obligations) | Art. 958f — Bookkeeping records retention (10 years); Art. 962 — Financial reporting obligations |
| Swiss nFADP (revDSG) | Art. 6 — Data minimisation and storage limitation; Art. 8 — Technical and organisational measures (records protection as organisational measure) |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security (protection of records containing personal data) |
| EU GDPR (where applicable) | Art. 5(1)(e) — Storage limitation; Art. 17 — Right to erasure (subject to legal retention); Art. 32 — Security of processing |
| Swiss Patent Act / Copyright Act | Protection of patent documentation and source code (where applicable) |
| ISO/IEC 27001:2022 | Annex A Controls 5.32, 5.33 |
| ISO/IEC 27002:2022 | Sections 5.32, 5.33 — Implementation guidance |
| NIST SP 800-53 Rev 5 | MP-6 (Media Sanitization), SI-12 (Information Management and Retention), PM-22 (Personally Identifiable Information Quality Management) |
| NIST SP 800-88 Rev 1 | Guidelines for Media Sanitization (Clear, Purge, Destroy) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
