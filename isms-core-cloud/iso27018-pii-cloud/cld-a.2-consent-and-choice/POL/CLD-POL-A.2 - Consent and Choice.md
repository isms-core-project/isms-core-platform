<!-- ISMS-CORE:POLICY:CLD-POL-A.2:cloud:POL:a.2 -->
**CLD-POL-A.2 — Consent and Choice**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Consent and Choice |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.2 |
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

**Review Cycle**: Annual (or upon significant regulatory or service model change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: CISO / Cloud Security Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- CLD-POL-A.1 (General)
- CLD-POL-A.3 (Purpose Legitimacy and Specification)
- CLD-POL-A.9 (Individual Participation and Access)
- ISO/IEC 27018:2025 Annex A, Section A.2 and Control A.2.1
- ISO/IEC 27701:2025 Controls A.2.3.3 (processor — no secondary use without consent)
- GDPR Article 28(3)(a) (instruction-only processing); Article 7 (conditions for consent)
- CH FADP Article 9 (processor obligations)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to consent and choice obligations — specifically the prohibition on processing PII beyond controller instructions and the obligation to cooperate with PII controllers in enabling data subject rights — in accordance with ISO/IEC 27018:2025 Annex A, Section A.2 and Control A.2.1.

**Scope**: All PII processing performed by [Organisation] on behalf of PII controllers under cloud service agreements.

**Combined Control Rationale**: Section A.2 establishes the foundational principle that [Organisation] does not independently determine the lawfulness of processing, including consent. That is the controller's responsibility. [Organisation]'s obligation under A.2 is twofold: (1) not to process PII beyond controller instructions without authority, and (2) to cooperate technically and operationally to enable controllers to fulfil data subject rights obligations.

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**Section A.2 — Consent and choice (principle)**
> *The public cloud PII processor shall not process PII for any purpose other than the documented instructions of the PII controller, unless required by applicable law. The processor shall not use PII for marketing, advertising, or profiling without explicit authorisation from the PII controller.*

**Control A.2.1 — Obligation to co-operate regarding PII principals' rights**
> *The public cloud PII processor shall co-operate with the PII controller to enable the controller to fulfil data subject rights requests, including access, rectification, erasure, restriction, portability, and objection. The processor shall implement technical capabilities to support these obligations and respond to controller requests within timeframes enabling statutory compliance.*

## What This Policy Does NOT Cover

- Determining the legal basis for PII processing — that is the PII controller's responsibility
- Managing data subject rights requests directly with data subjects — [Organisation] supports the controller; it does not act as the primary rights-fulfilment point unless contractually designated
- Consent collection and management on behalf of the controller — governed by the controller's own privacy policy

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 28(3)(a) (processor processes only on controller instructions); Article 28(3)(e) (processor assists with data subject rights); Articles 15–22 (data subject rights obligations of the controller, which the processor must technically support)
- **CH FADP**: Article 9(2)(b) (processor processes only as instructed); Article 9(2)(c) (duty to cooperate with controller on data subject requests)
- **ISO/IEC 27018:2025**: Controls A.2 (principle) and A.2.1 (cooperation obligation)

---

# Policy Statements: Consent and Choice (A.2)

## Prohibition on Unsanctioned Processing

[Organisation] SHALL NOT process PII for any purpose other than the documented instructions of the PII controller. This prohibition includes but is not limited to:

- Marketing, advertising, or audience profiling using controller-owned PII
- Data analytics or product improvement activities using PII beyond service delivery telemetry agreed with the controller
- Sale, licensing, or sharing of PII with third parties for commercial purposes
- Training machine learning models on PII without explicit written controller authorisation

Where [Organisation] wishes to use aggregated or anonymised data derived from PII for service improvement, [Organisation] SHALL document the anonymisation methodology and obtain confirmation from the DPO that the result is genuinely anonymised before proceeding.

## Legally Compelled Processing

Where applicable law requires [Organisation] to process PII beyond controller instructions (e.g., retention for law enforcement purposes), [Organisation] SHALL:

1. Inform the PII controller of the requirement before processing, unless legally prohibited
2. Process only the minimum PII required to comply with the legal obligation
3. Document the legal basis for the override processing
4. Notify the controller at the earliest opportunity when any prohibition on notification lapses

---

# Policy Statements: Co-operation on Data Subject Rights (A.2.1)

## Technical Capability Requirement

[Organisation] SHALL implement and maintain technical capabilities within its cloud services that enable PII controllers to fulfil data subject rights. These capabilities SHALL include, at minimum:

| Right | Required Technical Capability |
|-------|-------------------------------|
| **Access** | Export of all PII associated with a data subject in machine-readable format |
| **Rectification** | Mechanisms to update or correct specific PII fields |
| **Erasure** | Confirmed deletion of PII and all replicated or cached copies |
| **Restriction** | Ability to flag and isolate PII from active processing without deletion |
| **Portability** | Export of PII in structured, commonly used format (CSV, JSON) |
| **Objection** | Ability to suspend automated processing involving specific PII |

## Response Timeframes

[Organisation] SHALL respond to PII controller requests for data subject rights assistance within timeframes that enable the controller to meet its regulatory obligations. Unless the service agreement specifies shorter timeframes, [Organisation] SHALL:

- Acknowledge controller requests within **1 business day**
- Complete data subject rights fulfilment requests within **5 business days** for standard requests
- Notify the controller immediately of any technical constraint preventing fulfilment within this period

## Documentation of Cooperation

[Organisation] SHALL maintain records of all data subject rights assistance provided to PII controllers, including request receipt date, type of right exercised, controller identifier, and fulfilment date. These records SHALL be made available to the controller on request.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Monitors compliance with A.2 obligations; reviews requests for any commercial use of PII; advises on legally compelled processing; oversees data subject rights cooperation records |
| **CISO / Cloud Security Manager** | Ensures technical capabilities for data subject rights fulfilment are built and maintained within cloud services; includes cooperation capabilities in service design |
| **Cloud Service Delivery** | Processes data subject rights requests from controllers within defined timeframes; escalates complex or contested requests to DPO |
| **Legal/Compliance Officer** | Advises on legally compelled processing obligations; reviews any controller notifications regarding legal overrides |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Data Subject Rights Cooperation Records | Logs of all controller requests for rights fulfilment assistance with outcome and date | Duration of contract + 3 years |
| Technical Capability Documentation | Documented description of data subject rights technical features per service | Current + previous versions for 3 years |
| Legally Compelled Processing Records | Records of any processing beyond controller instructions required by law, with legal basis | Duration of processing + 3 years |
| Controller Agreement Clauses | Processor agreement terms addressing A.2.1 cooperation obligations | Duration of contract + 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.2 should expect to find:

- No evidence of PII being used for [Organisation]'s own marketing, analytics, or commercial purposes without documented controller authorisation
- Technical documentation confirming data subject rights fulfilment capabilities (export, deletion, restriction, portability) are operational within cloud services
- Records of data subject rights cooperation requests fulfilled for PII controllers
- Any legally compelled processing events documented with legal basis and controller notification records

---

<!-- QA_VERIFIED: [Date] -->
