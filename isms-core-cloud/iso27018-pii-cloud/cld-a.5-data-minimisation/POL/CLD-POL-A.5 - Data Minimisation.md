<!-- ISMS-CORE:POLICY:CLD-POL-A.5:cloud:POL:a.5 -->
**CLD-POL-A.5 — Data Minimisation**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Data Minimisation |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.5 |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / Cloud Security Manager | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant service architecture change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: CISO / Cloud Security Manager
- Secondary: Data Protection Officer (DPO)
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- ISMS-POL-A.8.10 (Information Deletion)
- CLD-POL-A.4 (Collection Limitation)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation)
- CLD-POL-A.11 (Information Security — covers portable media, encryption, disposal)
- ISO/IEC 27018:2025 Annex A, Section A.5 and Control A.5.1
- ISO/IEC 27701:2025 Controls A.2.4.2 (processor — temporary files) and A.2.4.3 (processor — return, transfer or disposal of PII)
- GDPR Article 5(1)(c) (data minimisation); Article 5(1)(e) (storage limitation)
- CH FADP Article 6(2) (proportionality)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to data minimisation — specifically the secure erasure of temporary files containing PII generated during cloud processing operations — in accordance with ISO/IEC 27018:2025 Annex A, Section A.5 and Control A.5.1.

**Scope**: All ephemeral, temporary, and working storage created by [Organisation]'s cloud services during PII processing, including cache, swap, working files, and logs.

**Combined Control Rationale**: Section A.5 establishes the principle that full identification is unnecessary where processing can be performed on anonymised or pseudonymised data. Control A.5.1 addresses the specific cloud risk of PII persisting in temporary storage after processing completes — a particularly significant risk in multi-tenant cloud environments where storage may be reallocated.

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**Section A.5 — Data minimisation (principle)**

Section A.5 establishes the principle that full identification of data subjects should be avoided where processing can be performed using anonymised, pseudonymised, or aggregated data, and that the techniques used should be documented and reviewed.

**Control A.5.1 — Secure erasure of temporary files**

Control A.5.1 addresses the specific risk of PII persisting in temporary storage after processing completes. It requires the processor to implement secure erasure of temporary files — including cache, swap, work files, and logs — using methods that prevent recovery, covering both persistent and ephemeral storage.

## What This Policy Does NOT Cover

- Retention periods for primary PII data stores — addressed in CLD-POL-A.6
- Secure disposal of physical storage media — addressed in CLD-POL-A.11

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 5(1)(c) (data minimisation); Article 5(1)(e) (storage limitation — no longer than necessary); Article 32(1)(a) (pseudonymisation and encryption as appropriate security measures)
- **CH FADP**: Article 6(2) (proportionality); Article 9 (processor obligations — appropriate technical measures)
- **ISO/IEC 27018:2025**: Controls A.5 (principle) and A.5.1

---

# Policy Statements: Data Minimisation Principle (A.5)

## Pseudonymisation and Anonymisation

Where the processing purpose can be fulfilled without direct identification of data subjects, [Organisation] SHALL implement pseudonymisation or anonymisation as part of service design. Specifically:

- Analytics and reporting functions SHALL use pseudonymised or aggregated data where technically feasible
- Logging and telemetry systems SHALL minimise PII capture to the operationally necessary minimum
- Test and development environments SHALL use synthetic data or anonymised data sets wherever possible

Anonymisation techniques applied to controller PII SHALL be documented and subject to DPO review prior to implementation to confirm the result is genuinely and irreversibly anonymised. The DPO assessment SHALL be conducted in accordance with applicable supervisory authority guidance (including EDPB Opinion 05/2014 on anonymisation techniques, or its successor).

---

# Policy Statements: Secure Erasure of Temporary Files (A.5.1)

## Temporary File Types in Scope

[Organisation]'s cloud services generate the following categories of temporary storage that may contain PII and are subject to this policy:

- **Cache files**: Data temporarily stored by application layers during active processing
- **Swap files / paging files**: Operating system memory overflow stored to disk
- **Work files / scratch space**: Intermediate processing files created during batch or stream operations
- **Application log files**: Service logs generated during processing that may capture PII in payloads, error traces, or debugging output
- **Ephemeral compute storage**: Block storage attached to compute instances during job execution

## Erasure Requirement

[Organisation] SHALL implement secure erasure of all temporary storage categories listed above once the processing operation for which they were created is complete. Erasure SHALL be performed using methods that prevent data recovery, in accordance with NIST SP 800-88 (Guidelines for Media Sanitization) or equivalent, including:

- Cryptographic erasure (encryption key deletion for encrypted volumes) — only effective where the data was encrypted with a dedicated key not replicated or backed up outside the deletion scope
- Multi-pass overwrite for persistent storage where cryptographic erasure is not applicable
- Secure memory zeroing for in-memory PII after use

The erasing mechanism SHALL be automated within the service pipeline wherever technically feasible to eliminate reliance on manual procedures.

## Log Minimisation

Application and infrastructure logs that capture PII SHALL be subject to:

- **Minimum capture**: Log configurations SHALL be reviewed to ensure PII in payloads, headers, or parameters is masked or excluded unless operationally essential
- **Retention limits**: Logs containing PII SHALL be retained for no longer than the operational period required, and in any case no longer than 30 days unless operationally justified and documented — or the maximum defined in service agreements with the PII controller if shorter
- **Automated deletion**: Log retention policies SHALL be implemented as automated deletion rules, not manual processes

## Multi-Tenant Storage Isolation

In multi-tenant environments, [Organisation] SHALL ensure that temporary storage allocated to a PII controller's processing is:

- Isolated from other tenants during active processing
- Securely erased before reallocation to any other tenant or workload
- Auditable — reallocation events SHALL be logged and available for inspection

This is addressed in detail in CLD-POL-A.11 (§11.13 — Access to data on pre-used data storage space). Multi-tenant isolation tests SHALL be performed at minimum annually and following any material change to storage infrastructure.

## Procedure Coverage

Temporary file erasure procedures SHALL explicitly cover:

- Both persistent storage (SSD, HDD, NVMe) and ephemeral storage (instance store, container ephemeral)
- All compute layers: bare metal, virtual machine, container, serverless function (serverless-specific erasure considerations, including /tmp storage and layer caching, are addressed in the service-level erasure procedures)
- All geographic regions in which [Organisation] operates cloud infrastructure

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO / Cloud Security Manager** | Owns temporary file erasure standards; reviews implementation annually; escalates unresolved gaps to DPO and Executive Management |
| **Cloud Engineering** | Implements automated erasure mechanisms in service pipelines; ensures log minimisation configurations are applied; tests erasure effectiveness |
| **Data Protection Officer (DPO)** | Reviews anonymisation/pseudonymisation assessments; confirms log minimisation configurations are adequate; advises on storage limitation obligations |
| **Security Operations** | Monitors for anomalous data remanence events; responds to incidents where PII may have persisted in temporary storage |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Temporary File Erasure Procedures | Documented procedures per service and storage type, with erasure method specified | Current + previous versions for 3 years |
| Automated Erasure Configuration Records | Technical configuration records demonstrating automated erasure is implemented | Current + 3 years |
| Log Minimisation Configuration Records | Documented log configurations confirming PII capture is minimised | Current + previous versions for 3 years |
| Multi-Tenant Isolation Test Records | Results of periodic testing confirming no cross-tenant data remanence | 3 years |
| DPO Anonymisation Reviews | Signed DPO assessments of anonymisation techniques applied to controller PII | Duration of use + 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.5 should expect to find:

- Documented temporary file erasure procedures covering all relevant storage types and compute layers
- Technical evidence that erasure is automated within service pipelines rather than reliant on manual steps
- Log minimisation configurations reviewed and confirmed to exclude unnecessary PII
- Test results confirming that storage reallocated between tenants contains no residual PII from prior tenant processing

---

<!-- QA_VERIFIED: [Date] -->
