<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.4.2-5-UG:privacy:UG:a.1.4.2-5 -->
**PRIV-IMP-A.1.4.2-5-UG — Data Minimisation — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Minimisation — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.4.2-5-UG |
| **Related Policy** | PRIV-POL-A.1.4.2-5 (Data Minimisation) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.4.2-5 (Data Minimisation — the governing policy)
- PRIV-IMP-A.1.4.2-5-TG (Data Minimisation — Technical Guide)
- PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent — purpose limitation and compatibility)
- PRIV-POL-A.1.4.6-10 (PII Lifecycle, Retention and Disposal — retention minimisation)
- PRIV-POL-A.3.23-31 (Technical Controls for PII — pseudonymisation and anonymisation mechanisms)

---

## Purpose of This Guide

This guide explains **how to implement** the data minimisation obligations of PRIV-POL-A.1.4.2-5. It covers how to review and justify PII fields before collection, how to control processing scope, how to maintain accuracy across the PII lifecycle, and how to apply de-identification mechanisms for secondary use.

**Who this guide is for**: DPO, Development/Product Teams, Data Owners, Privacy Champions.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Collection Minimisation (A.1.4.2)

### 1.1 Triggering a Collection Minimisation Review

A DPO collection minimisation review is required **before** any of the following:

- Deploying a new data collection form, API endpoint, or integration that gathers PII
- Adding a new field to an existing collection point
- Importing PII from a third-party source for the first time
- Re-using a collection mechanism for a new purpose

Development and product teams are responsible for raising a review request with the DPO. PII collection SHALL NOT commence until the DPO has confirmed field justification.

### 1.2 Field Justification Process

For each proposed PII field, the requesting team submits the following information to the DPO:

1. **Field name and data type** — what the field contains (e.g., "date of birth — date", "mobile number — text")
2. **Processing purpose** — the specific documented purpose this field serves (must correspond to a RoPA entry)
3. **Necessity argument** — why this field is necessary (not merely useful) for the stated purpose
4. **System or form** — where the field will be collected
5. **Collection frequency** — one-time, recurring, continuously updated

The DPO reviews each field against the necessity test: can the processing purpose be achieved without this field, or with a less identifying substitute? Fields that fail this test are rejected.

**Approved fields** are documented in the RoPA for the relevant processing activity. **Rejected fields** are communicated in writing with the reasoning, and the development team revises the design accordingly.

### 1.3 Privacy by Default at the Design Stage

The privacy-by-default obligation (GDPR Article 25) means that data minimisation must be the starting assumption, not an afterthought. Practical defaults:

- Optional fields in forms must be genuinely optional — not pre-populated or required by UX flow
- Profile completion prompts must not pressure data subjects to provide optional PII
- Analytics instrumentation must be scoped to the minimum identifiers needed — full identifiers should not be sent to analytics platforms unless necessary
- API responses must not return PII fields beyond what the consuming system requires

Where privacy-by-default settings are technically enforced (e.g., most-restrictive sharing setting, minimum-scope API tokens), these are documented in PRIV-IMP-A.1.4.2-5-TG.

---

## Part 2 — Processing Minimisation (A.1.4.3)

### 2.1 Access Restriction as a Processing Minimisation Control

The minimum necessary principle applies to access. PII must only be accessible to systems and personnel that have a documented processing purpose for it:

- Role-based access controls must restrict PII system access to roles with a legitimate processing need
- Privileged access to PII databases (e.g., direct DB query access, DBA roles) must be approved by the DPO and Data Owner; access must be logged
- API integrations must use minimum-scope service accounts — a service account used for sending transactional email must not have read access to payment data

Data Owners are responsible for reviewing access to PII systems in their domain at minimum annually and confirming the access list is still appropriate.

### 2.2 Purpose Limitation in Ongoing Operations

Once PII has been collected for a stated purpose, it must not be used for a materially different purpose without prior assessment:

- Teams proposing to use existing PII data for a new analytical, marketing, or operational purpose must notify the DPO before commencing
- The DPO conducts a purpose compatibility assessment (per PRIV-IMP-A.1.2.2-5-UG) to determine whether the new use is compatible with the original purpose and whether the existing lawful basis covers it
- Where a new lawful basis is required, this must be obtained before processing for the new purpose begins

**Common secondary use scenarios requiring assessment**:

| Proposed Secondary Use | Why Assessment Is Needed |
|------------------------|--------------------------|
| Using customer PII for staff training or demos | Training/demo is not within the original processing purpose |
| Sharing CRM data with a new analytics platform | New processor; potential purpose extension |
| Using operational PII in product research | Research purpose may require separate basis or anonymisation |
| Exporting PII to a reporting tool | New system access; confirm scope of data exported |

### 2.3 De-identified Alternatives for Secondary Processing

Where the processing purpose can be fulfilled using pseudonymised or anonymised data, the de-identified version must be used in preference to identifiable PII:

- Analytics and reporting: use aggregated or pseudonymised datasets where the insight does not require individual re-identification
- Software testing: use synthetic or anonymised test data — see PRIV-POL-A.3.23-31 and PRIV-IMP-A.3.23-31-UG for the test data standard
- Internal training and demonstrations: use anonymised examples or fabricated data, not live PII

When a team is unsure whether de-identified data is sufficient for their use case, they should consult the DPO before proceeding with identifiable PII.

---

## Part 3 — Accuracy and Quality (A.1.4.4)

### 3.1 Accuracy Controls at the Point of Collection

Collection processes must include reasonable validation to prevent entry of obviously inaccurate data:

- **Format validation**: date fields validate date format; email fields validate structure; phone fields validate number format
- **Range validation**: numeric fields have reasonable min/max constraints
- **Logical validation**: dates of birth must be plausible; postcode/city combinations must match where feasible
- **Mandatory field prompts**: required fields prompt completion before submission

Validation rules must not substitute for PII quality — they catch format errors, not substantive inaccuracies. Data Owners are responsible for downstream accuracy.

### 3.2 Keeping PII Current Over the Lifecycle

For PII that is known to change over time (addresses, contact details, employment status, preferences), Data Owners must define and operate a review or update mechanism:

| PII Type | Review/Update Mechanism | Frequency |
|----------|------------------------|-----------|
| Customer contact details (email, address) | Data subject self-service update via account portal; email bounce monitoring | Ongoing; prompt if bounce detected |
| Employee HR records | Annual HR review cycle + event-triggered updates (role change, address change) | Annual + event-triggered |
| Supplier/processor contacts | Processor agreement renewal and annual review process | Annual |
| Consent preferences | Real-time update via preference centre | Ongoing |

Where PII is used for significant decisions (financial assessments, health-related processing, legal proceedings), enhanced accuracy controls apply — the Data Owner must verify currency of the PII before it is used in the decision, and document the verification.

### 3.3 Correcting Inaccurate PII

When inaccurate PII is identified — through a data subject rectification request, an internal discovery, or a third-party notification — it must be corrected without undue delay:

1. The Data Owner (or DPO via the DSR process) identifies the inaccurate field(s) and the correct value
2. The correction is applied in the primary system of record and propagated to linked systems
3. If the inaccurate PII was shared with third parties, they are notified (per PRIV-POL-A.1.3.5-10 and the third party notification process in PRIV-IMP-A.1.3.5-10-UG)
4. The correction is documented; if arising from a DSR, it is logged in the Data Subject Rights Register

Where inaccuracy cannot be corrected and the PII is used for a purpose where accuracy is necessary, the DPO must assess whether the PII can continue to be used for that purpose or must be suppressed.

---

## Part 4 — De-identification for Minimisation (A.1.4.5)

### 4.1 When to Apply De-identification

De-identification transforms identifiable PII into a less identifying form. The decision between pseudonymisation, anonymisation, and retention of identifiable PII is made by the DPO based on the processing purpose:

| Scenario | Recommended Approach |
|----------|---------------------|
| Secondary analytics — individual re-identification not needed | Anonymisation or aggregation |
| Software testing — realistic data needed but individuals must not be identifiable | Anonymisation or synthetic data |
| Development environment — testing specific user flows | Pseudonymisation (key held separately by DPO) |
| Research with follow-up capability needed (e.g., clinical follow-up) | Pseudonymisation |
| Operational processing requiring individual identity | Retain identifiable PII — minimise fields |

### 4.2 Pseudonymisation Process

Pseudonymisation replaces direct identifiers (name, email, national ID) with pseudonyms (tokens or codes). The resulting dataset is still PII — re-identification is possible with the pseudonymisation key.

**Process for creating a pseudonymised dataset**:

1. Data Owner submits a request to the DPO identifying: the source dataset, the intended secondary purpose, the proposed pseudonymisation method
2. DPO reviews and approves the approach; confirms the dataset scope
3. IT Security / Development implements the pseudonymisation — direct identifiers replaced with tokens; key stored separately (not in the same system as the pseudonymised data)
4. Pseudonymised dataset deployed to secondary use environment; key remains with DPO or in a secured key management system
5. DPO records the pseudonymised dataset in the Data Minimisation Objectives register (see TG)
6. Access to the pseudonymisation key is controlled and logged

**Important**: a pseudonymised dataset is still subject to GDPR — it must have a lawful basis, be within the scope of the purpose, and be deleted when no longer needed.

### 4.3 Anonymisation Process and DPO Confirmation

Anonymisation is an irreversible process. If successful, the output is no longer PII and GDPR does not apply to it. However, anonymisation is technically demanding — many attempts at anonymisation are reversible through re-identification techniques, and therefore do not meet the legal standard.

**Process for anonymising a dataset**:

1. Data Owner requests anonymisation of a dataset; submits to DPO with dataset description and intended use
2. DPO (with technical assistance from IT Security if needed) assesses the re-identification risk using the three-part test:
   - **Singling out**: Can an individual be identified from the dataset alone?
   - **Linkability**: Can records be linked to other available datasets to re-identify individuals?
   - **Inference**: Can attributes of an individual be inferred even without direct identification?
3. If all three risks are adequately mitigated, the DPO issues an Anonymisation Confirmation Record (see PRIV-IMP-A.1.4.2-5-TG)
4. The confirmed anonymised dataset is released for use; it is no longer subject to GDPR data subject rights
5. If re-identification risk cannot be adequately mitigated, pseudonymisation is used instead

**DPO confirmation is mandatory** before any dataset is treated as anonymised. Development teams must not self-certify anonymisation.

---

## Evidence Checklist

- [ ] RoPA — PII fields documented with purpose justification per collection activity
- [ ] DPO collection review records — sign-off on new collection points before deployment
- [ ] Purpose compatibility assessments — documented for any secondary use of existing PII
- [ ] Access review records — Data Owner confirmation of access lists annually
- [ ] Accuracy mechanisms — validation rules in collection; update procedures for time-varying PII
- [ ] Correction records — inaccurate PII corrected without undue delay; third parties notified
- [ ] Pseudonymisation records — datasets, key management, purpose documented
- [ ] Anonymisation Confirmation Records — DPO sign-off before any dataset treated as anonymised
- [ ] Minimisation Objectives document — current and reviewed annually

---

<!-- QA_VERIFIED: [Date] -->
