<!-- ISMS-CORE:POLICY:CLD-POL-A.3:cloud:POL:a.3 -->
**CLD-POL-A.3 — Purpose Legitimacy and Specification**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Purpose Legitimacy and Specification |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.3 |
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
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- CLD-POL-A.1 (General)
- CLD-POL-A.2 (Consent and Choice)
- CLD-POL-A.4 (Collection Limitation)
- ISO/IEC 27018:2025 Annex A, Section A.3 and Controls A.3.1–A.3.2
- ISO/IEC 27701:2025 Controls A.2.2.3 (processor — organisation's purposes) and A.2.2.4 (processor — marketing and advertising use)
- GDPR Article 28(3)(a) (instruction-only processing); Article 5(1)(b) (purpose limitation)
- CH FADP Article 6(3) (purpose limitation); Article 9 (processor obligations)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to purpose legitimacy and specification — specifically the restriction to controller-defined processing purposes and the absolute prohibition on commercial use of controller-owned PII without explicit authorisation — in accordance with ISO/IEC 27018:2025 Annex A, Controls A.3.1 and A.3.2.

**Scope**: All PII processing performed by [Organisation] on behalf of PII controllers under cloud service agreements.

**Combined Control Rationale**: A.3.1 and A.3.2 together define the purpose boundary for [Organisation] as a processor. A.3.1 restricts processing to agreed purposes; A.3.2 explicitly prohibits the monetisation of PII for the processor's own benefit. These controls are the operational expression of the instruction-only processing principle established in CLD-POL-A.2.

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**Section A.3 — Purpose legitimacy and specification (principle)**

Section A.3 establishes the principle that a public cloud PII processor must restrict all processing to the purposes specified in its agreement with the PII controller, and must obtain controller approval before implementing any new processing purpose.

**Control A.3.1 — Public cloud PII processor's purpose**

Control A.3.1 requires the processor to process PII only for the documented purposes agreed with the controller, and prohibits processing for the processor's own purposes unless the controller has explicitly authorised it in writing.

**Control A.3.2 — Public cloud PII processor's commercial use**

Control A.3.2 prohibits the processor from using controller-owned PII for its own commercial benefit — including advertising, profiling, data sales, or product improvement — without documented written controller authorisation, and requires any such arrangement to be disclosed in the service agreement.

## What This Policy Does NOT Cover

- Determining or validating the legitimacy of the controller's processing purpose — that is the controller's responsibility
- [Organisation]'s own processing of data it collects directly (not on behalf of a controller) — governed by ISMS-POL-A.5.34

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 5(1)(b) (purpose limitation principle — applied to the controller; processor must not undermine it); Article 28(3)(a) (processor processes only on controller instructions and for no other purpose)
- **CH FADP**: Article 6(3) (purpose limitation); Article 9(2)(b) (processor bound by controller's purpose specification)
- **ISO/IEC 27018:2025**: Controls A.3.1 and A.3.2

---

# Policy Statements: Processor's Purpose (A.3.1)

## Purpose Restriction

[Organisation] SHALL process PII only for the purposes explicitly documented in the service agreement or written processing instructions received from the PII controller. Processing SHALL NOT be extended to new purposes without prior written controller authorisation.

## Documenting Processing Purposes

All cloud service agreements with PII controllers SHALL include a processing description that specifies:

- The categories of PII to be processed
- The purposes of processing
- The processing operations to be performed
- The duration of processing
- Any permitted sub-processing arrangements

## New Purpose Requests

Where [Organisation] identifies an operational need to process PII for a purpose not covered by the current agreement (e.g., incident investigation requiring access to PII beyond normal service delivery), [Organisation] SHALL:

1. Document the proposed new purpose in writing
2. Obtain written controller authorisation before processing begins
3. Record the authorisation in the Processor Agreement Register
4. Cease the additional processing if authorisation is withheld or withdrawn

Where a controller does not respond within 15 business days of receiving a written new purpose request, [Organisation] treats the request as denied and does not proceed with the additional processing.

## Operational Telemetry

[Organisation] may collect service telemetry and operational metadata (e.g., performance metrics, error logs) as necessary for service delivery. Where such telemetry incidentally contains PII:

- It SHALL be treated as PII subject to this policy
- Retention SHALL be limited to the minimum period necessary for operational purposes, not to exceed 90 days unless operationally justified and documented with CISO and DPO approval
- It SHALL NOT be used for analytics, product improvement, or commercial purposes without controller authorisation

---

# Policy Statements: Commercial Use Prohibition (A.3.2)

## Absolute Prohibition

[Organisation] SHALL NOT use PII processed on behalf of a PII controller for any of [Organisation]'s own commercial purposes, including but not limited to:

- Targeted advertising or ad profiling
- Sale or licensing of PII or derived data sets to third parties
- Training or improving machine learning models using PII
- Use of controller PII for competitive intelligence or market positioning purposes
- Market research or customer analytics not directly supporting the contracted service

This prohibition applies regardless of whether the PII has been aggregated, pseudonymised, or de-identified, unless [Organisation]'s DPO has confirmed in writing that the data is genuinely and irreversibly anonymised.

## Contractual Commitment

[Organisation]'s service agreements SHALL include an explicit clause confirming the commercial use prohibition. Any proposed commercial use arrangement (including those involving genuinely anonymised data) SHALL:

- Be proposed to and agreed by the PII controller in writing before implementation
- Be disclosed in the service agreement
- Be reviewed by the DPO and Legal/Compliance before execution

## Internal Safeguards

To enforce the commercial use prohibition, [Organisation] SHALL:

- Implement technical access controls separating controller PII from [Organisation]'s internal product and analytics systems
- Prohibit [Organisation]'s marketing and commercial teams from accessing controller PII without DPO authorisation
- Include the commercial use prohibition in the employee security awareness training programme (see ISMS-POL-A.6.3) and in standard confidentiality agreements used in employment and contractor contracts

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Reviews and approves any proposed new processing purpose or commercial use arrangement; maintains records of purpose authorisations; monitors compliance with purpose restriction |
| **Legal/Compliance Officer** | Reviews service agreement processing descriptions for completeness and compliance; advises on purpose limitation obligations under GDPR and FADP |
| **CISO / Cloud Security Manager** | Implements technical controls preventing cross-contamination of controller PII and [Organisation]'s internal systems; includes purpose controls in service architecture |
| **Product / Commercial Teams** | May not access controller PII for product development or commercial purposes without written DPO authorisation; must route any such requests through the DPO |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Processing Descriptions in Service Agreements | Documented processing purpose per service and per controller | Duration of contract + 3 years |
| New Purpose Authorisation Records | Written controller authorisations for any processing beyond original agreement | Duration of processing + 3 years |
| DPO Anonymisation Confirmations | Written DPO assessments confirming any derived data set is genuinely anonymised | Duration of use + 3 years |
| Access Control Documentation | Technical documentation demonstrating separation of controller PII from internal systems | Current + 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.3 should expect to find:

- Service agreements containing explicit processing purpose descriptions for all active controller relationships
- No evidence of controller PII being accessed by [Organisation]'s marketing, analytics, or product teams without documented authorisation
- Records of any new purpose authorisations obtained from controllers
- Technical architecture documentation demonstrating system-level separation between controller PII and [Organisation]'s internal data systems

---

<!-- QA_VERIFIED: [Date] -->
