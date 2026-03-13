<!-- ISMS-CORE:POLICY:CLD-POL-A.8:cloud:POL:a.8 -->
**CLD-POL-A.8 — Openness, Transparency and Notice**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Openness, Transparency and Notice |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.8 |
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

**Review Cycle**: Annual (or upon sub-processor changes or service model changes)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: CISO / Cloud Security Manager
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- CLD-POL-A.1 (General)
- CLD-POL-A.11 (Information Security — §11.12: Sub-contracted PII processing)
- CLD-POL-A.12 (Privacy Compliance — geographical disclosure)
- ISO/IEC 27018:2025 Annex A, Section A.8 and Control A.8.1
- ISO/IEC 27701:2025 Controls A.2.5.7 (disclosure of subcontractors used to process PII), A.2.5.8 (engagement of a subcontractor to process PII) and A.2.5.9 (change of subcontractor to process PII)
- GDPR Article 28(2) (sub-processor authorisation and flow-down); Article 28(3)(d) (processor informs controller of sub-processors)
- CH FADP Article 9(3) (sub-processor disclosure obligations)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to openness, transparency, and notice — specifically the obligation to disclose sub-processors engaged to process PII on [Organisation]'s behalf and to provide advance notice of any changes to sub-processor arrangements — in accordance with ISO/IEC 27018:2025 Annex A, Section A.8 and Control A.8.1.

**Scope**: All sub-processors engaged by [Organisation] to perform PII processing operations as part of cloud service delivery.

**Combined Control Rationale**: Transparency about sub-processors is central to the trust relationship between cloud processors and their customers. PII controllers need to know who has access to their PII to fulfil their own accountability obligations, conduct due diligence, and exercise contractual rights (including objection to sub-processor changes under GDPR Article 28(2)).

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**Section A.8 — Openness, transparency and notice (principle)**

Section A.8 establishes the principle that a public cloud PII processor should make available to PII controllers information about where PII is processed, which sub-processors are engaged, and any changes to processing arrangements, and should keep its privacy notices current.

**Control A.8.1 — Disclosure of sub-contracted PII processing**

Control A.8.1 requires the processor to disclose to PII controllers the identity of all sub-processors handling PII on its behalf, and to give advance notice of any intended additions or replacements, providing the controller with an opportunity to object.

## What This Policy Does NOT Cover

- Sub-processor contract content and security flow-down — addressed in CLD-POL-A.11 (§11.12)
- Geographic location of PII processing — addressed in CLD-POL-A.12.1
- Legally compelled disclosure notifications — addressed in CLD-POL-A.6.1

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 28(2) (sub-processor engagement requires prior written controller consent — general or specific); Article 28(3)(d) (processor shall not engage sub-processor without prior written controller authorisation); Article 28(4) (sub-processor obligations must mirror processor obligations)
- **CH FADP**: Article 9(3) (processor must inform controller of sub-processors and obtain consent; equivalent security must be contractually required)
- **ISO/IEC 27018:2025**: Controls A.8 (principle) and A.8.1

---

# Policy Statements: Sub-Processor Disclosure (A.8.1)

## Sub-Processor Register

[Organisation] SHALL maintain a **Sub-Processor Register** listing all sub-processors engaged to process PII on [Organisation]'s behalf. The register SHALL include for each sub-processor:

| Field | Description |
|-------|-------------|
| **Sub-processor name** | Legal entity name |
| **Services provided** | Specific processing operations performed |
| **PII categories accessed** | Categories of PII the sub-processor may access |
| **Processing location(s)** | Countries or regions where processing occurs |
| **Contract reference** | Reference to the binding sub-processor agreement |
| **Controller consent status** | Date controller general/specific consent was obtained |
| **Date added / last reviewed** | Onboarding date and most recent review date |

The Sub-Processor Register SHALL be maintained by the DPO and made available to all PII controllers upon request. [Organisation] SHALL also publish a current Sub-Processor List on its website or trust portal for controllers operating under general authorisation. Controllers operating under specific sub-processor authorisation shall receive direct notification rather than relying on the public list. Existing Sub-Processor Register entries SHALL be reviewed at minimum annually, and upon any material change to a sub-processor's operations, to ensure the register remains current.

[Organisation] SHALL conduct a documented security and privacy due diligence assessment of each sub-processor before engagement. The results SHALL be referenced in the Sub-Processor Register and the assessment methodology is addressed in CLD-POL-A.11 (§11.12).

## Advance Notice of Changes

[Organisation] SHALL provide advance notice to PII controllers before implementing any intended changes to sub-processor arrangements, including:

- Engagement of a new sub-processor
- Replacement of an existing sub-processor
- Material change to the scope or location of an existing sub-processor's processing

**Notice period**: Unless a service agreement specifies a longer period, [Organisation] SHALL provide a minimum of **30 days' advance notice** of intended sub-processor changes.

Notices SHALL be delivered via the notification channel specified in the service agreement (e.g., email to the controller's designated data protection contact, trust portal notification, or published change log with subscriber alerts).

## Controller Objection Right

PII controllers operating under general sub-processor authorisation (GDPR Article 28(2)) SHALL have the right to object to any intended sub-processor change during the advance notice period. [Organisation]'s procedure for handling objections is:

1. Acknowledge the objection in writing within 3 business days
2. Engage with the controller to understand the grounds for objection
3. If the objection is upheld: identify and implement an alternative processing arrangement before the change
4. If the objection cannot be accommodated: notify the controller and allow contract termination on reasonable terms without penalty

Controllers who do not object within the notice period are deemed to have accepted the change, where general sub-processor authorisation applies. This deemed acceptance mechanism applies only under the general authorisation model; controllers operating under specific sub-processor authorisation may require a positive confirmation rather than silence as acceptance — Legal/Compliance Officer SHALL confirm which model applies to each controller relationship.

## Emergency Sub-Processor Changes

Where [Organisation] must engage a replacement sub-processor urgently (e.g., due to sub-processor insolvency or security incident), [Organisation] SHALL:

- Notify affected PII controllers within 72 hours of the decision to engage the replacement sub-processor
- Provide the controller with written justification for the emergency change
- Implement equivalent security and privacy controls on the replacement sub-processor before PII transfer. Where full security verification cannot be completed before an emergency transfer, a risk acceptance document signed by the CISO and DPO is required, with a defined remediation timeframe for any gaps identified post-transfer
- Formally close the emergency notification and update the Sub-Processor Register within 5 business days

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Owns the Sub-Processor Register; manages controller notification and objection process; authorises new sub-processor engagements |
| **Legal/Compliance Officer** | Reviews sub-processor agreements for GDPR Article 28(4) compliance; advises on controller objection handling; maintains contract references in Sub-Processor Register |
| **CISO / Cloud Security Manager** | Assesses security posture of proposed sub-processors; ensures security controls are flowed down contractually; manages emergency sub-processor changes |
| **Procurement** | Triggers DPO and Legal review before engaging any new sub-processor with PII access; ensures Sub-Processor Register is updated upon new engagements |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Sub-Processor Register | Complete and current register with mandatory fields | Current + previous versions for 5 years from engagement end — 5-year retention reflects the standard contractual limitation period under EU and Swiss law |
| Controller Advance Notices | Records of sub-processor change notifications sent to each controller | 5 years |
| Controller Objection Records | Any controller objections received, [Organisation]'s response, and resolution | 5 years |
| Published Sub-Processor List | Timestamped copies of the publicly available sub-processor list at each version | 5 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.8 should expect to find:

- A current, complete Sub-Processor Register with controller consent status for each sub-processor
- Evidence that PII controllers were given advance notice of all sub-processor changes in the audit period, within the required notice period
- Records of any controller objections received and how they were resolved
- A publicly accessible sub-processor list consistent with the internal Sub-Processor Register

---

<!-- QA_VERIFIED: [Date] -->
