<!-- ISMS-CORE:POLICY:CLD-POL-A.1:cloud:POL:a.1 -->
**CLD-POL-A.1 — General**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — General Applicability and Obligations |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.1 |
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
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII — parent ISMS policy)
- CLD-POL-A.2 (Consent and Choice)
- CLD-POL-A.3 (Purpose Legitimacy and Specification)
- CLD-POL-A.10 (Accountability)
- CLD-POL-A.11 (Information Security)
- CLD-POL-A.12 (Privacy Compliance)
- ISO/IEC 27018:2025 Annex A, Section A.1 (General)
- ISO/IEC 27701:2025 (Privacy Information Management System)
- ISO/IEC 27002:2022 (Information security controls)
- GDPR Article 28 (Processor obligations)
- CH FADP Article 9 (Processor engagements)

---

## Executive Summary

This policy establishes the scope, applicability, and general obligations of [Organisation] acting as a **public cloud PII processor** in accordance with ISO/IEC 27018:2025 Annex A, Section A.1.

**Scope**: All cloud services provided by [Organisation] where [Organisation] processes personally identifiable information (PII) on behalf of, and under the instructions of, a PII controller. This applies regardless of the cloud service model (IaaS, PaaS, SaaS) or deployment model (public, hybrid).

**Role Clarification**: ISO/IEC 27018:2025 applies to [Organisation] in its capacity as a **PII processor** — an entity that processes PII on behalf of and under the authority of a PII controller. [Organisation] does not determine the purposes and means of such processing; that responsibility rests with the PII controller.

**Extended Controls Note**: ISO/IEC 27018:2025 Annex A controls are informative. [Organisation] implements them as part of its cloud privacy practice, independent of their normative status under the standard.

---

# Scope and Applicability

## ISO/IEC 27018:2025 — Section A.1

**Section A.1 — General**
> *These controls apply to public cloud service providers acting as PII processors. Processors shall implement all applicable controls and document how they address each requirement in their service agreements with PII controllers.*

## Applicability

This policy and the CLD-POL-A.X policy suite applies to:

- All [Organisation] public cloud services that process PII on behalf of customers (PII controllers)
- All personnel, systems, processes, and sub-processors involved in such PII processing
- All jurisdictions in which [Organisation] provides cloud services where PII of data subjects is processed

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 28 (processor obligations — written contract, instruction-only processing, security, sub-processors, assistance, return/deletion, audit rights); Article 32 (security of processing)
- **CH FADP**: Article 9 (processor engagement conditions); Article 8 (data security)
- **ISO/IEC 27018:2025**: Annex A extended control set — implemented as organisational commitment

---

# Policy Statements: General Applicability (A.1)

## PII Processor Role

[Organisation] SHALL operate as a PII processor only — processing PII solely on the documented instructions of PII controllers. [Organisation] SHALL NOT:

- Determine the purposes or means of PII processing beyond technical service delivery
- Process PII for its own commercial, analytical, or operational purposes without explicit controller authorisation
- Transfer, sell, or otherwise exploit PII processed on behalf of a controller

## Contract Requirement

[Organisation] SHALL process PII only where a written contract with the PII controller is in place. That contract SHALL address, at minimum, the scope of processing, security obligations, breach notification, sub-processor arrangements, data return/deletion, and audit rights — in accordance with CLD-POL-A.11.11.

## Documentation of Controls

[Organisation] SHALL document how each applicable control in ISO/IEC 27018:2025 Annex A is addressed within its services. This documentation SHALL be made available to PII controllers upon request and incorporated into service agreements where contractually required.

## Instruction Processing

[Organisation] SHALL process PII only in accordance with documented, current instructions from the PII controller. Where [Organisation] is legally required by applicable law to process PII beyond controller instructions, [Organisation] SHALL inform the PII controller of that requirement before processing, unless legally prohibited from doing so.

## Sub-Processor Management

[Organisation] SHALL engage sub-processors only with the prior written consent of the PII controller. All sub-processors SHALL be bound by equivalent data protection obligations. [Organisation] remains accountable to the controller for sub-processor compliance. Sub-processor arrangements are governed in detail by CLD-POL-A.11.12.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO / Cloud Security Manager** | Maintains the CLD-POL-A.X policy suite; ensures technical controls meet ISO 27018:2025 Annex A requirements; reports on cloud PII processor compliance |
| **Data Protection Officer (DPO)** | Advises on regulatory compliance of processor activities; reviews processor agreements; coordinates with controllers on PII matters |
| **Legal/Compliance Officer** | Reviews processor agreement terms; advises on applicable law obligations; assesses regulatory changes affecting processor obligations |
| **Cloud Service Delivery** | Operates services within documented controller instructions; escalates out-of-scope processing requests to CISO and DPO |
| **All Personnel** | Process PII only as authorised; report suspected policy breaches immediately to CISO and DPO |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Processor Agreement Register | List of all active PII controller agreements with scope, status, and review date | Current + 3 years |
| Control Implementation Documentation | Documentation of how each CLD-POL-A.X control is implemented per service | Current version + previous versions for 3 years |
| Sub-Processor Register | List of approved sub-processors with controller consent records | Current + 3 years |
| Instruction Records | Records of documented controller processing instructions and any deviations | Duration of contract + 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.1 should expect to find:

- Processor agreement register demonstrating written contracts with all PII controllers
- Documentation mapping each ISO/IEC 27018:2025 Annex A control to service implementation
- Sub-processor register with controller consent records for each sub-processor
- Evidence that processing is conducted only in accordance with documented controller instructions

---

<!-- QA_VERIFIED: [Date] -->
