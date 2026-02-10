<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.10:operational:OP-POL:a.8.10 -->
**ISMS-OP-POL-A.8.10 — Information Deletion**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Deletion |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.10 |
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

- ISO/IEC 27001:2022 Control A.8.10 — Information deletion

**Related Annex A Controls**:

| Control | Relationship to Information Deletion |
|---------|--------------------------------------|
| A.5.9 Inventory of information and other associated assets | Asset inventory defines deletion scope and data ownership |
| A.5.10 Acceptable use of information and other associated assets | Acceptable use lifecycle includes end-of-life deletion |
| A.5.12–13 Information classification and labelling | Classification determines deletion method and verification level |
| A.5.14 Information transfer | Deletion obligations after transfer completion |
| A.5.33 Protection of records | Records retention schedules trigger deletion at expiry |
| A.5.34 Privacy and protection of PII | Data subject erasure rights; PII deletion obligations |
| A.7.10 Storage media | Physical media sanitisation and disposal |
| A.7.14 Secure disposal or re-use of equipment | Equipment decommissioning requires data deletion |
| A.8.13 Information backup | Backup copies included in deletion scope |
| A.8.24 Use of cryptography | Cryptographic erasure as a deletion method |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Privacy and Protection of PII Policy
- Information Protection and Records Management Policy
- Backup Policy
- Asset Management Policy
- Use of Cryptography Policy

---

# Information Deletion Policy

## Purpose

The purpose of this policy is to ensure that information stored in information systems, devices, or any other storage media is deleted when no longer required, using methods appropriate to the sensitivity of the data and the media type, to prevent unnecessary exposure and to comply with legal, regulatory, and contractual requirements.

This policy supports Swiss nFADP (revDSG) Art. 6(4) (proportionality and data minimisation — personal data shall be destroyed or anonymised as soon as it is no longer required for the purpose of processing) and Art. 8 (technical and organisational measures for data security). Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 5(1)(e) (storage limitation) and Art. 17 (right to erasure) also apply.

## Scope

All employees and third-party users.

All information processed, stored, or transmitted on or in organisation-owned, managed, and controlled systems, devices, and media deemed in scope by the ISO 27001 scope statement.

This includes:

- All data categories (personal data, confidential business information, financial records, technical data, communications, logs)
- All storage locations (on-premises, cloud, third-party, backup, disaster recovery)
- All media types (magnetic, solid-state, optical, paper, removable media, mobile devices)
- All lifecycle stages (active use, archival, backup, development/test, end-of-life)

## Principle

Information shall not be retained longer than is required for its stated business, legal, or regulatory purpose. When retention periods expire, or when a valid deletion trigger occurs, information shall be deleted using a method appropriate to the data sensitivity and media type, with verifiable evidence that deletion has been performed.

Only organisation-approved deletion methods shall be used. Standard operating system deletion (e.g., "delete" or "empty recycle bin") is insufficient for confidential or personal data, as such methods are typically recoverable.

---

## Retention Schedules and Deletion Triggers

### Retention Schedule

The organisation shall maintain a retention schedule defining retention periods for all data categories. Retention periods shall be based on the longest applicable requirement from:

- Legal and statutory obligations (Swiss CO, nFADP, tax law)
- Regulatory requirements (industry-specific regulations)
- Contractual obligations (customer, supplier, partner agreements)
- Documented business need (with owner approval)

Where multiple requirements apply to the same data, the longest applicable retention period shall govern unless Legal Counsel determines otherwise.

**Reference Retention Periods for Swiss SMEs**:

| Data Category | Minimum Retention | Legal Basis | Notes |
|---------------|-------------------|-------------|-------|
| **Accounting records** (annual reports, audit reports, financial statements) | 10 years from end of financial year | Swiss CO Art. 958f | Must be retained in written and signed form (annual/audit reports) or electronically with integrity guarantee |
| **Accounting vouchers** (invoices, receipts, bank statements, VAT documents) | 10 years from end of financial year | Swiss CO Art. 958f | May be retained electronically per Olico requirements |
| **Employment contracts and HR files** | 10 years from end of employment | Swiss CO Art. 127–128 (limitation periods); cantonal requirements | Salary claims: 5-year limitation (CO Art. 128); work certificates: 10-year limitation (CO Art. 127) |
| **Payroll and social insurance records** | 10 years from end of financial year | Swiss CO Art. 958f; AHV/IV requirements | Includes salary statements, social security contributions |
| **Tax records** | 10 years from end of financial year | Swiss CO Art. 958f; cantonal tax law | Includes corporate and VAT records |
| **Customer contracts** | Duration + 10 years | Swiss CO Art. 127 (general limitation) | 10-year limitation period for contractual claims |
| **Supplier and vendor contracts** | Duration + 10 years | Swiss CO Art. 127 | Retain for limitation period after contract end |
| **Personal data (general)** | Only as long as required for processing purpose | nFADP Art. 6(4) | Must be deleted or anonymised when purpose fulfilled |
| **Data subject consent records** | Duration of processing + 3 years | nFADP Art. 6; best practice | Evidence of lawful basis for processing |
| **Security logs and audit trails** | 12 months (online), up to 3 years (archive) | Organisational policy; DSV Art. 4 | Longer retention for sensitive data processing logs |
| **ISMS audit evidence** | 3 years minimum | ISO 27001 certification cycle | Retain across full certification cycle |
| **Incident investigation records** | 3 years from closure | Organisational policy | Longer if litigation anticipated |

This table provides minimum reference periods. The Records Manager shall maintain the authoritative retention schedule, which shall be reviewed annually by Legal Counsel and approved by Executive Management.

### Deletion Triggers

Deletion shall be initiated when any of the following events occurs:

| # | Trigger Event | Responsible Party | Timeline |
|---|---------------|-------------------|----------|
| 1 | **Retention period expiry** | Records Manager / System Owner | Within 90 days of expiry (automated where feasible) |
| 2 | **Data subject erasure request** (nFADP / GDPR Art. 17) | DPO / Privacy Advisor | Within 30 days of validated request |
| 3 | **Contract or service agreement termination** | System Owner | Per contractual terms (default: 90 days) |
| 4 | **Processing purpose completion** | Data Owner | Within 90 days of purpose fulfilment |
| 5 | **Legal hold release** | Legal Counsel | Within 90 days of hold release |
| 6 | **Asset decommissioning** | IT Operations | Before asset leaves organisational control |
| 7 | **Consent withdrawal** | DPO / Privacy Advisor | Within 30 days (unless other legal basis applies) |

Where automated deletion is technically feasible, it should be implemented with safeguards against premature deletion (legal hold checks, business owner notification). Where automation is not feasible, manual deletion procedures shall be documented with defined verification checkpoints.

---

## Deletion Methods

### Sanitisation Standards

Deletion methods shall align with NIST SP 800-88 Rev. 2 (Guidelines for Media Sanitization, September 2025), which defines three sanitisation levels, and IEEE 2883 for media-specific sanitisation techniques.

| Sanitisation Level | Description | When to Use | Example Methods |
|--------------------|-------------|-------------|-----------------|
| **Clear** | Logical techniques rendering data inaccessible through standard interfaces; recovery possible with specialised tools | Media remaining under organisational control; lower-sensitivity data (Public, Internal) | Standard overwrite, manufacturer reset, operating system secure erase |
| **Purge** | Physical or logical techniques rendering data inaccessible even with laboratory-grade tools | Media leaving organisational control; sensitive data (Confidential); media reuse by third parties | Cryptographic erasure, block erasure (flash/SSD), degaussing (magnetic media) |
| **Destroy** | Physical destruction rendering media unusable and data recovery infeasible | End-of-life media; highest-sensitivity data; media with no future value | Disintegration, pulverisation, incineration, melting, shredding |

### Deletion Method by Classification and Media

| Data Classification | Media Remaining In-House | Media Leaving Organisation | Media End-of-Life |
|---------------------|--------------------------|-----------------------------|---------------------|
| **Public** | Clear | Clear | Destroy (or recycle if verified clear) |
| **Internal** | Clear | Purge | Destroy |
| **Confidential** | Purge | Purge | Destroy |
| **Strictly Confidential** | Purge | Destroy | Destroy |

### Paper Records

| Data Classification | Disposal Method |
|---------------------|--------------------|
| **Public** | General waste or recycling |
| **Internal** | Cross-cut shredding (DIN 66399 P-3 minimum) |
| **Confidential** | Cross-cut shredding (DIN 66399 P-4 minimum) or witnessed incineration |
| **Strictly Confidential** | DIN 66399 P-5 minimum or certified third-party destruction with certificate |

### Cryptographic Erasure

Cryptographic erasure may be used as a valid Purge-level method where data has been encrypted at rest and the encryption meets organisational standards (per Use of Cryptography Policy). For cryptographic erasure to constitute deletion under this policy:

- All target data shall have been encrypted before storage (encryption applied retroactively does not qualify).
- The encryption algorithm shall meet approved minimum standards (AES-256 or equivalent).
- A documented data-to-key mapping shall exist, enabling identification of which encryption keys protect which data.
- Key destruction shall be performed through a verified process (HSM key zeroisation, KMS key deletion with audit log, or equivalent).
- Key destruction evidence shall be retained (audit logs, HSM certificates) for a minimum of 3 years.
- Backup copies of the encryption key shall also be destroyed — if key backup, escrow, or external storage exists and cannot be verified as destroyed, cryptographic erasure shall not be accepted as the sole deletion method.

### Backup Deletion

Deletion in production systems shall extend to all backup copies containing the deleted data, including:

- Full, incremental, and differential backups
- Snapshots and point-in-time copies
- Disaster recovery replicas
- Application-level backups (database exports, VM exports)
- Cloud-native backup services with independent retention policies

Where immediate deletion from backups is not technically feasible (e.g., immutable backup tapes, retention-locked cloud backups), the organisation shall:

1. Document the backup retention schedule showing when the data will be naturally overwritten or expired.
2. Obtain CISO and Data Owner approval for the extended retention period.
3. Apply access controls to prevent restoration of the data from backup.
4. Track the pending deletion in the deletion register until confirmed complete.

---

## Third-Party and Cloud Deletion

### Contractual Requirements

All contracts with third parties that process organisational data shall include deletion obligations specifying:

- Maximum deletion timeline after contract termination or upon written request (default: 30 days)
- Sanitisation standard appropriate for data sensitivity (referencing NIST SP 800-88 levels)
- Deletion scope covering all copies, including backups, caches, logs, and disaster recovery replicas
- Requirement to provide deletion verification (certificate of destruction or equivalent attestation)
- Flow-down of deletion requirements to sub-processors
- Right to audit deletion compliance

### Cloud Service Provider Assessment

Before engaging a cloud service provider, the organisation shall assess deletion capabilities including:

- API support for data deletion and deletion verification
- Deletion propagation to all regions, availability zones, and replicas
- Multi-tenant isolation assurance (deletion does not affect other tenants; other tenants cannot access residual data)
- Backup and snapshot deletion capabilities and timelines
- Data remanence controls after deletion
- Certification or attestation of deletion practices (SOC 2 Type II, ISO 27001 with A.8.10 in scope)

### Third-Party Deletion Verification

The organisation shall obtain verification of deletion from third parties through one or more of the following methods:

**Physical media destruction** — Certificates of destruction including:
- Media serial numbers or asset identifiers
- Destruction method (referencing NIST SP 800-88 level or DIN 66399 security level)
- Destruction date and location
- Certificate issuer name and accreditation (e.g., NAID AAA, ISO 21964)

**Service provider logical deletion** — One of:
- SOC 2 Type II report with deletion control testing
- Independent audit report verifying deletion procedures
- ISO 27001 certification with A.8.10 in scope

**Cloud/SaaS API deletion** — Logged evidence including:
- API call timestamp and authenticated user
- Resource identifier(s) deleted
- HTTP success response (200/204)
- Confirmation of backup/snapshot deletion where the provider supports this

For Confidential and Strictly Confidential data: certificates from accredited destruction vendors or independent audit reports are required. API logs alone are insufficient.

### Third-Party Deletion Failure Escalation

| Timeline | Action | Responsible |
|----------|--------|-------------|
| T+0 days | Log failure in gap register; initiate follow-up with third-party contact | IT Operations |
| T+15 days | Escalate to third-party account manager; copy CISO and DPO | System Owner |
| T+30 days | Escalate to third-party executive contact; initiate contract review with Legal Counsel | CISO |
| T+45 days | Review contractual remedies (service credits, termination for material breach); consider data migration to compliant provider | Executive Management |

For Confidential/Strictly Confidential data, escalation timelines are accelerated: T+7, T+15, T+21 days.

---

## Data Subject Erasure Requests

### Accepting and Processing Requests

The organisation shall accept and process data subject erasure requests in compliance with Swiss nFADP Art. 6(4) and, where applicable, GDPR Art. 17 (right to erasure / right to be forgotten).

**Request Handling Process**:

| Step | Action | Timeline | Responsible |
|------|--------|----------|-------------|
| 1 | Receive request (email, web form, post, in person) | — | DPO / Privacy Advisor |
| 2 | Log request in data subject request register | Within 24 hours | DPO / Privacy Advisor |
| 3 | Verify data subject identity | Within 5 business days | DPO / Privacy Advisor |
| 4 | Identify all systems, databases, and backups containing the data subject's personal data | Within 10 business days | IT Operations / System Owners |
| 5 | Assess whether erasure obligation applies or a legal exception exists | Within 15 business days | DPO + Legal Counsel |
| 6 | Execute deletion or issue reasoned denial | Within 25 business days | IT Operations / DPO |
| 7 | Confirm completion to data subject in writing | Within 30 days of request | DPO / Privacy Advisor |

### Legal Exceptions to Erasure

Erasure may be refused where processing is necessary for:

- Compliance with a legal retention obligation (e.g., Swiss CO Art. 958f accounting records, tax obligations)
- Establishment, exercise, or defence of legal claims
- Archiving purposes in the public interest, scientific or historical research
- Reasons of public interest in the area of public health
- Exercise of freedom of expression and information

Where erasure is denied based on a legal exception:

1. Document the specific legal basis relied upon.
2. Provide written explanation to the data subject including the exception relied upon and complaint rights (right to lodge complaint with FDPIC or competent supervisory authority).
3. Apply restriction of processing where possible (data retained but not actively processed).
4. Set review date to reassess whether the exception still applies.

### Third-Party Notification

Where personal data subject to an erasure request was disclosed to third parties, the organisation shall notify those third parties of the erasure request per GDPR Art. 19 and nFADP obligations, unless doing so proves impossible or involves disproportionate effort.

---

## Legal Hold Management

### Legal Hold Triggers

Deletion shall be suspended when data is subject to a legal hold for any of the following reasons:

- Litigation (filed, threatened, or reasonably anticipated)
- Government investigation or regulatory examination
- Internal investigation requiring forensic preservation (fraud, misconduct, data breach)
- External audit requiring specific data preservation

### Initiation and Release

Only Legal Counsel (or designated Legal/Compliance Officer) may initiate or release a legal hold.

**Issuance Process**:

1. Legal Counsel issues formal hold notice documenting: matter name/number, scope (systems, date ranges, custodians, data categories), effective date, preservation obligations.
2. Affected custodians are notified within 24 hours and shall acknowledge receipt within 2 business days.
3. IT Operations suspends automated deletion for affected systems within 48 hours and confirms suspension in writing.
4. Legal Counsel maintains Legal Hold Register recording: hold ID, matter name, issue date, scope, affected systems, custodians, acknowledgement status, review dates.

### Quarterly Review

Legal holds shall be reviewed at least quarterly by Legal Counsel. Each review shall produce a documented assessment including:

- Hold identifier and initiation date
- Current litigation/investigation status
- Continued necessity determination with legal basis
- Scope adjustment if applicable (narrowing to specific data categories)
- Anticipated hold release date or trigger condition
- Reviewer name and review date

### Hold Release and Post-Hold Deletion

Upon hold release:

1. Legal Counsel issues formal hold release notice.
2. Custodians and IT Operations are notified within 24 hours.
3. IT Operations re-enables normal deletion schedules.
4. Data held beyond normal retention solely due to the legal hold shall be deleted within 90 days of hold release, unless an approved business justification exists.

### Conflict with Erasure Requests

When a data subject erasure request conflicts with an active legal hold:

- The legal hold takes precedence.
- Restriction of processing shall be applied (data preserved but not actively used).
- Deletion shall execute within 30 days of hold release.
- The data subject shall be informed that the request has been noted but cannot currently be fulfilled, citing the applicable legal exception, without disclosing details that could prejudice legal proceedings.

---

## Verification and Evidence

### Deletion Audit Trail

The organisation shall maintain deletion audit trails including:

| Field | Description |
|-------|-------------|
| **Deletion timestamp** | Date and time deletion was executed |
| **Data category** | Type and classification of data deleted |
| **Deletion method** | Sanitisation method applied (Clear / Purge / Destroy / Cryptographic Erasure) |
| **Media identifier** | System name, device serial number, or storage location |
| **Deletion trigger** | Event that initiated deletion (retention expiry, DSR, decommission, etc.) |
| **Responsible party** | Person or system that performed the deletion |
| **Verification result** | Confirmation that deletion was successful |

### Deletion Log Retention

Deletion logs shall be retained for a minimum of 3 years or the applicable regulatory requirement, whichever is longer. Deletion logs shall not contain the deleted data itself — only metadata about the deletion event.

### Verification Methods

Deletion effectiveness shall be verified through:

- **Automated verification**: System-generated confirmation of successful deletion (API response, tool output, log entry)
- **Periodic sampling**: Quarterly sampling of deletion records to verify completeness and accuracy (minimum 10% sample of deletions per quarter)
- **Third-party attestation**: Certificates of destruction for physical media and external service providers
- **Spot checks**: Annual spot-check of randomly selected systems to confirm no data exists beyond its retention period

---

## Exception Management

### Exception Requests

Exceptions to standard deletion procedures require a documented request including:

- Data category and classification
- Business justification for exception
- Risk assessment (what is the risk of retaining the data beyond its normal period?)
- Compensating controls to mitigate the retention risk
- Proposed expiry date (exceptions shall not be indefinite)

### Approval Authority

| Data Classification | Exception Duration | Approvers |
|---------------------|-------------------|-----------|
| Internal | Up to 12 months | System Owner + CISO |
| Confidential | Up to 6 months | CISO + DPO |
| Strictly Confidential | Any duration | CISO + DPO + Legal Counsel + Executive Management |

### Prohibited Exceptions

The following exceptions shall not be granted:

- Indefinite retention without a specific end date or review trigger
- Exceptions to circumvent legitimate data subject erasure requests
- Exceptions to bypass regulatory retention limitations
- Blanket exceptions for entire data categories without specific, documented justification

### Exception Register

All approved exceptions shall be recorded in the exception register with owner, approval date, expiry date, compensating controls, and review schedule. Exceptions shall be reviewed quarterly and auto-expire unless renewed through the approval process.

---

## Definitions

| Term | Definition |
|------|------------|
| **Information Deletion** | The process of removing data from storage media such that it cannot be recovered through normal or, depending on sanitisation level, specialised means |
| **Data Sanitisation** | All methods of rendering data inaccessible, including clearing, purging, and destroying |
| **Clear** | Logical sanitisation protecting against data recovery using standard operating system tools or simple non-invasive techniques |
| **Purge** | Physical or logical sanitisation protecting against data recovery using laboratory-grade attack techniques |
| **Destroy** | Physical destruction rendering media unusable and data recovery infeasible through any known technique |
| **Cryptographic Erasure** | Deletion method rendering encrypted data irrecoverable by securely destroying the encryption keys |
| **Retention Period** | Defined timeframe during which data must be kept before deletion is permitted or required |
| **Deletion Trigger** | Event or condition that initiates the deletion process (e.g., retention expiry, erasure request) |
| **Legal Hold** | Suspension of deletion to preserve data for litigation, investigation, regulatory examination, or audit |
| **Data Subject Erasure Request** | A request from a data subject exercising their right to erasure under nFADP or GDPR Art. 17 |
| **Certificate of Destruction** | Third-party attestation that physical media was destroyed according to a specified standard |
| **Data Remanence** | Residual data remaining on storage media after deletion attempts; the risk that sanitisation methods seek to eliminate |
| **Data Owner** | Individual or role accountable for defining business purpose, retention period, and deletion requirements for a data category |
| **Records Manager** | Role responsible for maintaining the organisational retention schedule and overseeing disposal processes |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; deletion method approval; exception approval; compliance monitoring and metrics; escalation point for deletion failures |
| **DPO / Privacy Advisor** | Data subject erasure request handling; privacy compliance; retention schedule review for personal data; exception approval (Confidential+) |
| **Legal Counsel** | Legal hold management (initiation, review, release); third-party contract terms (deletion clauses); regulatory interpretation; erasure exception assessment |
| **Records Manager** | Retention schedule maintenance and annual review; disposal oversight; deletion register management; compliance tracking and reporting |
| **IT Operations** | Deletion execution; deletion tool management and maintenance; backup deletion; logging and verification; third-party deletion coordination |
| **System Owners** | System-specific deletion implementation; coordination with IT Operations; exception requests; automated deletion feasibility assessment |
| **Data Owners** | Retention period definition for owned data categories; approval of business-critical data deletion; classification decisions |
| **All Personnel** | Handle data per classification and retention requirements; do not retain data beyond authorised periods; report suspected deletion failures |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Retention schedule** (current version, approved by Legal Counsel and Executive Management) | Records Manager | *Reviewed annually; version-controlled* | Current + superseded versions (7 years) |
| 2 | **Deletion execution logs** (timestamps, data categories, methods, verification results) | IT Operations | *Continuous; reviewed quarterly* | 3 years |
| 3 | **Third-party certificates of destruction** (physical media, accredited vendor certificates) | IT Operations | *Per destruction event* | 3 years from destruction date |
| 4 | **Data subject erasure request register** (requests received, assessment, outcome, completion date) | DPO / Privacy Advisor | *Per request; register reviewed quarterly* | 3 years from request closure |
| 5 | **Legal hold register** (active holds, scope, quarterly reviews, release records) | Legal Counsel | *Active holds reviewed quarterly; register maintained continuously* | 3 years from hold release |
| 6 | **Exception register** (approved exceptions with justification, compensating controls, expiry dates) | CISO | *Reviewed quarterly; presented at management review* | Life of exception + 3 years |
| 7 | **Data inventory** with retention periods and deletion scope per data category | Records Manager | *Reviewed annually; quarterly snapshots* | Current + quarterly snapshots (3 years) |
| 8 | **Quarterly compliance report** (deletion metrics: on-time deletion rate, overdue items, exceptions, DSR response times) | CISO / Records Manager | *Quarterly; presented at management review* | 3 years |
| 9 | **Cloud/SaaS API deletion logs** (API call records, resource identifiers, success confirmations) | IT Operations | *Per deletion event* | 3 years |
| 10 | **Third-party contract review records** (deletion clauses, vendor deletion capability assessments) | Legal Counsel / CISO | *Per contract; reviewed at contract renewal* | Contract duration + 3 years |
| 11 | **Automated deletion configuration records** (retention policies configured in systems, legal hold integration status) | IT Operations | *Reviewed semi-annually* | Current configuration + 3 years |
| 12 | **Deletion verification sampling results** (quarterly sampling records, spot-check findings) | Information Security | *Quarterly sampling; annual spot-check* | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, deletion log audits, retention schedule compliance reviews, data subject request response tracking, third-party deletion verification reviews, exception register reviews, internal and external audits, and feedback to the policy owner.

**Key Compliance Metrics**:

| # | Metric | Target | Measurement Frequency |
|---|--------|--------|----------------------|
| 1 | On-time deletion rate (deletions executed within 90 days of retention expiry) | ≥ 95% | Quarterly |
| 2 | Data subject erasure requests completed within 30 days | 100% | Per request; reported quarterly |
| 3 | Third-party deletion certificates obtained for Confidential+ data | 100% | Per event; reported quarterly |
| 4 | Legal holds reviewed within quarterly cycle | 100% | Quarterly |
| 5 | Exception register reviewed and current (no expired, unreviewed exceptions) | 100% | Quarterly |
| 6 | Retention schedule coverage (percentage of data categories with defined retention) | 100% | Annually |
| 7 | Backup deletion completion (data deleted from all backup copies within documented timeline) | ≥ 90% | Quarterly |

Metrics breaching targets shall be escalated to the CISO for immediate attention and reported at the next Management Review.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team. Retention-related exceptions require Legal Counsel approval.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Failure to delete personal data in accordance with legal requirements may additionally expose the organisation to regulatory sanctions (nFADP Art. 60–66; GDPR Art. 83 where applicable).

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to data protection regulations (nFADP, GDPR, cantonal requirements), media sanitisation standards (NIST SP 800-88, IEEE 2883), cloud service provider deletion capabilities, emerging storage technologies, audit findings, and lessons learned from deletion failures or data subject complaints.

---

# Areas of the ISO 27001 Standard Addressed

Information Deletion Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.9 Inventory of information and other associated assets |
| Clause 7.3 Awareness | 5.12 Classification of information |
| Clause 7.5.3 Control of documented information | 5.33 Protection of records |
| | 5.34 Privacy and protection of PII |
| | 5.36 Compliance with policies, rules, and standards |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 7.10 Storage media |
| | 7.14 Secure disposal or re-use of equipment |
| | **8.10 Information deletion** |
| | 8.13 Information backup |
| | 8.24 Use of cryptography |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 6 — Principles (proportionality, purpose limitation, storage limitation); Art. 8 — Data security (technical and organisational measures); Art. 25 — Right of access (includes deletion rights); Art. 24 — Breach notification |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| Swiss CO (Code of Obligations) | Art. 957–958f — Bookkeeping and record retention obligations (10 years); Art. 127–128 — Limitation periods for claims |
| EU GDPR (where applicable) | Art. 5(1)(e) — Storage limitation; Art. 17 — Right to erasure; Art. 19 — Notification obligation regarding erasure; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 8.10 — Information deletion |
| ISO/IEC 27002:2022 | Section 8.10 — Implementation guidance for information deletion |
| NIST SP 800-88 Rev. 2 | Guidelines for Media Sanitization (Clear, Purge, Destroy; cryptographic erasure) |
| IEEE 2883 | Standard for Sanitizing Storage (media-specific sanitisation techniques) |
| NIST SP 800-53 Rev 5 | MP-6 (Media Sanitization), SI-12 (Information Management and Retention) |
| DIN 66399 | Classification of paper and media destruction security levels |

**Conditional Frameworks** (apply where business activities trigger applicability):

| Framework | Condition |
|-----------|-----------|
| PCI DSS v4.0 | Applicable if payment card data is processed; requires secure deletion of cardholder data when no longer needed |
| FINMA circulars | Applicable if organisation is a supervised Swiss financial institution |
| HIPAA Security Rule | Applicable if US protected health information is processed |

---

<!-- QA_VERIFIED: 2026-02-07 -->
