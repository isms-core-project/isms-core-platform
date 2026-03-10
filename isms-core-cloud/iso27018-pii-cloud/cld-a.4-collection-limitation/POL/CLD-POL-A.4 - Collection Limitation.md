<!-- ISMS-CORE:POLICY:CLD-POL-A.4:cloud:POL:a.4 -->
**CLD-POL-A.4 — Collection Limitation**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Collection Limitation |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.4 |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
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
| 1.0 | [Date to be set] | CISO / DPO | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory or service model change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: CISO / Cloud Security Manager
- Secondary: Data Protection Officer (DPO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- CLD-POL-A.3 (Purpose Legitimacy and Specification)
- CLD-POL-A.5 (Data Minimisation)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation)
- ISO/IEC 27018:2025 Annex A, Section A.4 (Collection Limitation — principle)
- ISO/IEC 27701:2025 Controls A.2.3.4–A.2.3.5 (processor — collection limitation)
- GDPR Article 5(1)(c) (data minimisation principle); Article 28(3)(a) (instruction-only)
- CH FADP Article 6(2) (proportionality); Article 9 (processor obligations)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to collection limitation — specifically the obligation to process only the minimum PII necessary to fulfil the contracted service, and to handle any excess PII collected during service provision — in accordance with ISO/IEC 27018:2025 Annex A, Section A.4.

**Scope**: All PII collected, received, or otherwise obtained by [Organisation] in the course of providing cloud services to PII controllers.

**Principle Note**: ISO/IEC 27018:2025 Annex A, Section A.4 is a principle-level section with no additional sub-controls beyond the main body of the standard. This policy implements the principle as an organisational commitment. Practical data minimisation at the technical level is addressed in CLD-POL-A.5.

---

# Scope and Applicability

## ISO/IEC 27018:2025 — Section A.4

**Section A.4 — Collection limitation (principle)**
> *The cloud service provider shall collect only the minimum PII necessary to fulfil the contracted service. Collection practices shall be documented and reviewed. Excess PII collected during service provision shall be promptly deleted or returned to the PII controller.*

## What This Policy Does NOT Cover

- Determining what PII a controller may lawfully collect from data subjects — that is the controller's responsibility
- Technical anonymisation and erasure methods for temporary files — addressed in CLD-POL-A.5

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 5(1)(c) (data minimisation — adequate, relevant, and limited to what is necessary); Article 28(3)(a) (processor processes only as instructed — no excess collection)
- **CH FADP**: Article 6(2) (proportionality — personal data processing must be proportionate to the purpose)
- **ISO/IEC 27018:2025**: Section A.4 principle

---

# Policy Statements: Collection Limitation (A.4)

## Minimum Necessary Collection

[Organisation] SHALL collect, retain, or otherwise process only the minimum PII necessary to deliver the contracted cloud service. [Organisation] SHALL NOT:

- Request or accept PII categories from the PII controller beyond what is required for service delivery
- Store PII in system components, logs, or operational databases beyond the operational necessity of the processing
- Replicate PII across environments (development, test, staging, production) without explicit controller authorisation

## Documentation of Collection Practices

[Organisation] SHALL document PII collection practices for each cloud service, including:

- Categories of PII collected or received during service delivery
- The operational justification for each PII category
- The system components, logs, and storage locations where PII may be present
- Retention periods applicable to each collection type

This documentation SHALL be reviewed annually and upon material changes to service architecture.

## Excess PII

Where [Organisation] determines that PII has been collected that exceeds the scope of the contracted service (e.g., a controller uploads a data set containing PII categories beyond the service scope), [Organisation] SHALL:

1. Notify the PII controller of the excess PII without undue delay
2. Agree with the controller whether the excess PII is to be returned or securely deleted
3. Complete the agreed action within the timeframe agreed with the controller
4. Document the event and outcome

## Development and Test Environments

PII from production environments SHALL NOT be used in development, testing, or staging environments without explicit written authorisation from the PII controller. Where controller authorisation is obtained, the minimum necessary PII SHALL be used and the same security controls applicable in production SHALL apply.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO / Cloud Security Manager** | Ensures service architecture collects minimum necessary PII; maintains collection documentation; reviews collection scope during service design and changes |
| **Data Protection Officer (DPO)** | Reviews collection documentation annually; advises on proportionality assessments; monitors for excess collection events |
| **Cloud Service Delivery / Engineering** | Implements minimum-collection architecture; reports excess collection events to CISO and DPO promptly |
| **Legal/Compliance Officer** | Advises on proportionality and minimisation obligations under GDPR and FADP |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Collection Practice Documentation | Documented PII categories, justifications, and locations per service | Current + previous versions for 3 years |
| Annual Review Records | Signed records of annual collection practice reviews | 3 years |
| Excess PII Event Records | Documentation of any excess PII events, controller notifications, and resolution | Duration of contract + 3 years |
| Development/Test Authorisation Records | Written controller authorisations for any use of production PII in non-production environments | Duration of use + 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.4 should expect to find:

- Documented collection practice records for each cloud service with PII categories and justifications
- Evidence of annual collection practice reviews
- No PII categories in operational systems that exceed contracted service scope
- Any excess PII events documented with controller notification and resolution records
- No production PII in development or test environments without documented controller authorisation

---

<!-- QA_VERIFIED: [Date] -->
