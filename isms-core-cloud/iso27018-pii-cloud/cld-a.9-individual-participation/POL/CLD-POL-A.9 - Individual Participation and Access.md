<!-- ISMS-CORE:POLICY:CLD-POL-A.9:cloud:POL:a.9 -->
**CLD-POL-A.9 — Individual Participation and Access**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Individual Participation and Access |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.9 |
| **Document Creator** | Data Protection Officer (DPO) |
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
| 1.0 | [Date to be set] | DPO | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant service capability change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: CISO / Cloud Security Manager
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- CLD-POL-A.2 (Consent and Choice — A.2.1 co-operation on rights)
- CLD-POL-A.7 (Accuracy and Quality — rectification capability)
- ISO/IEC 27018:2025 Annex A, Section A.9 (Individual Participation and Access — principle)
- ISO/IEC 27701:2025 Control A.2.3.2 (processor — comply with obligations to PII principals, including supporting the fulfilment of data subject rights)
- GDPR Articles 15–22 (data subject rights); Article 28(3)(e) (processor assists with rights)
- CH FADP Articles 25–32 (data subject rights); Article 9(2)(c) (processor assists controller)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to individual participation and access — specifically the obligation to provide PII controllers with technical mechanisms and operational support to enable fulfilment of data subject rights requests and other data subject rights within statutory timeframes — in accordance with ISO/IEC 27018:2025 Annex A, Section A.9.

**Scope**: All cloud services provided by [Organisation] that store or process PII on behalf of PII controllers.

**Role Clarification**: [Organisation] does not respond directly to data subjects. Data subjects direct their rights requests to the PII controller. [Organisation]'s obligation is to provide the controller with the tools and cooperation needed to fulfil those requests on time. The cooperation obligation under A.9 is the counterpart to A.2.1 at a higher level.

**Principle Note**: ISO/IEC 27018:2025 Annex A, Section A.9 is a principle-level section with no additional sub-controls beyond the main body of the standard. The operational mechanism for co-operation on data subject rights is addressed in CLD-POL-A.2.1.

---

# Scope and Applicability

## ISO/IEC 27018:2025 — Section A.9

**Section A.9 — Individual participation and access (principle)**

Section A.9 establishes the principle that a public cloud PII processor should provide PII controllers with mechanisms to support the fulfilment of data subject access and other rights requests, ensure those capabilities are tested and documented, and assist controllers in meeting their statutory response obligations.

## What This Policy Does NOT Cover

- Specific technical capabilities for individual rights (export, deletion, restriction, portability) — detailed in CLD-POL-A.2.1
- Correction and update mechanisms — addressed in CLD-POL-A.7

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Articles 15–22 (data subject rights: access, rectification, erasure, restriction, portability, objection, automated decision rights); Article 28(3)(e) (processor shall assist controller in ensuring compliance with data subject rights obligations)
- **CH FADP**: Articles 25–32 (data subject rights); Article 9(2)(c) (processor cooperation with controller on rights requests)
- **ISO/IEC 27018:2025**: Section A.9 principle

---

# Policy Statements: Individual Participation and Access (A.9)

## Processor Support Obligation

[Organisation] SHALL provide PII controllers with technical capabilities and operational procedures that enable controllers to fulfil data subject rights requests under applicable law. [Organisation]'s support obligation covers the following rights:

| Right | [Organisation]'s Support Obligation |
|-------|-------------------------------------|
| **Access (Art. 15 GDPR)** | Provide capability to export all PII associated with a data subject in structured, readable format |
| **Rectification (Art. 16)** | Provide capability to update or correct PII records including replication propagation |
| **Erasure (Art. 17)** | Provide deletion of PII from all active storage within 5 business days; backup and replicated copies purged within 15 business days |
| **Restriction (Art. 18)** | Isolate PII from active processing within 1 business day ("functional restriction"); full propagation to replicated data stores within 5 business days |
| **Portability (Art. 20)** | Provide PII export in machine-readable, commonly used format (JSON, CSV) |
| **Objection (Art. 21)** | Provide capability to suspend or restrict processing of specific PII records upon controller instruction |

## Capability Testing

[Organisation] SHALL test data subject rights fulfilment capabilities at least **annually** and upon any material change to service architecture — including changes to data storage infrastructure, backup architecture, replication topology, or API interfaces used for rights fulfilment. Testing SHALL:

- Cover each right listed in the table above for each service category
- Verify that data export, deletion, and restriction operations complete within the defined response timeframe
- Confirm that deletions propagate correctly to backup copies and replicated data stores
- Be documented with results retained for audit purposes

Material gaps identified during testing SHALL be tracked as remediation items and reported to affected PII controllers if capability is reduced below contracted service levels.

## Response Timeframes

[Organisation]'s service capabilities SHALL support controller fulfilment of DSAR responses within the following timeframes:

- **Acknowledge** controller DSAR-related request: within 1 business day
- **Complete** data access exports and rectification requests: within 5 business days
- **Complete** erasure requests (including propagation to backups): within 15 business days
- **Complete** restriction requests: within 1 business day (functional — PII isolated from active processing); full propagation to replicated data stores within 5 business days

Where a specific service agreement defines shorter timeframes, those timeframes prevail.

## Controller Documentation

[Organisation] SHALL provide PII controllers with documentation describing the data subject rights capabilities available within each cloud service, including:

- How to initiate each rights fulfilment operation via the service interface or API
- Expected completion times and confirmation mechanisms
- Any limitations on rights fulfilment (e.g., backup deletion timelines)
- The escalation path for requesting [Organisation] assistance where self-service is insufficient

This documentation SHALL be kept current and updated within 30 days of any material capability change — including changes to data storage infrastructure, backup architecture, replication topology, or API interfaces. Where a data subject rights capability is temporarily unavailable, [Organisation] SHALL notify affected controllers of the outage and the expected restoration timeframe, and shall provide manual assistance (e.g., staff-assisted export) where a controller faces a statutory deadline during the outage period. Manual fallback procedures are documented in [Organisation]'s incident response plan.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Monitors controller satisfaction with rights fulfilment capabilities; reviews annual capability test results; advises on emerging rights obligations |
| **CISO / Cloud Security Manager** | Owns rights capability design and maintenance; manages annual capability testing programme; reports gaps to DPO |
| **Cloud Engineering** | Implements and maintains rights fulfilment mechanisms; resolves technical capability gaps; confirms backup and replication propagation of rights operations |
| **Cloud Service Delivery** | Assists controllers in exercising rights capabilities; escalates complex requests to Cloud Engineering |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Rights Capability Documentation | Per-service documentation of data subject rights capabilities and usage instructions | Current + previous versions for 3 years |
| Annual Capability Test Results | Documented test outcomes for all rights types per service | 3 years |
| Remediation Tracking Records | Tracked items for capability gaps identified in testing | Until resolved + 3 years |
| Controller Assistance Records | Log of DSAR-related requests received from controllers and resolution outcomes | Duration of contract + 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.9 should expect to find:

- Up-to-date documentation of data subject rights capabilities per cloud service
- Annual capability test records covering all rights types with outcomes and any remediation
- No material unresolved capability gaps for data subject rights fulfilment
- Records of controller requests for DSAR assistance and timely resolution

---

<!-- QA_VERIFIED: [Date] -->
