<!-- ISMS-CORE:POLICY:CLD-POL-A.6:cloud:POL:a.6 -->
**CLD-POL-A.6 — Use, Retention and Disclosure Limitation**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Use, Retention and Disclosure Limitation |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.6 |
| **Document Creator** | Data Protection Officer (DPO) / CISO |
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
| 1.0 | [Date to be set] | DPO / CISO | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory or service model change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: CISO / Cloud Security Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- ISMS-POL-A.5.33 (Protection of Records)
- CLD-POL-A.3 (Purpose Legitimacy and Specification)
- CLD-POL-A.5 (Data Minimisation)
- CLD-POL-A.10 (Accountability — breach notification, return/disposal)
- ISO/IEC 27018:2025 Annex A, Section A.6 and Controls A.6.1–A.6.2
- ISO/IEC 27701:2025 Controls A.2.3.7–A.2.3.9 (processor — use, retention, disclosure)
- GDPR Article 5(1)(b) and (e) (purpose limitation, storage limitation); Article 28(3)(a) (instruction-only); Article 28(3)(f) (assist with regulatory obligations)
- CH FADP Article 6(3) (purpose limitation); Article 9(2)(d) (processor duty to assist)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to use, retention, and disclosure limitation — specifically the obligation to notify PII controllers of legally compelled PII disclosures to third parties, and to maintain records of all such disclosures — in accordance with ISO/IEC 27018:2025 Annex A, Section A.6 and Controls A.6.1 and A.6.2.

**Scope**: All PII retained by [Organisation] on behalf of PII controllers, and all disclosures of such PII to third parties including law enforcement, regulatory authorities, and other entities.

**Combined Control Rationale**: A.6.1 and A.6.2 address the critical scenario in public cloud where government or regulatory bodies compel the processor to disclose PII without controller knowledge. Together they require transparency (notify the controller) and accountability (record all disclosures), ensuring the controller can fulfil its own regulatory notification obligations.

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**Section A.6 — Use, retention and disclosure limitation (principle)**
> *PII shall be retained only for as long as necessary for the specified purpose. Retention schedules shall be documented and enforced. PII shall be disclosed only to authorised parties. Third-party disclosures shall be documented and restricted to the minimum necessary.*

**Control A.6.1 — PII disclosure notification**
> *Where the public cloud PII processor is legally compelled to disclose PII to a third party (e.g. law enforcement, regulatory authority), the processor shall notify the PII controller of this requirement prior to disclosure unless prohibited by law. Where prior notification is prohibited, the processor shall notify the controller at the earliest opportunity after the legal prohibition lapses.*

**Control A.6.2 — Recording of PII disclosures**
> *The public cloud PII processor shall maintain records of all disclosures of PII to third parties, including: the recipient, date, categories of PII disclosed, legal basis for disclosure, and whether the PII controller was notified. These records shall be made available to the PII controller on request and retained for a period sufficient to demonstrate compliance.*

## What This Policy Does NOT Cover

- Primary data retention periods for PII at rest — these are set by the PII controller's instructions and included in service agreements
- Return or disposal of PII upon contract termination — addressed in CLD-POL-A.10.3

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 5(1)(b) (purpose limitation); Article 5(1)(e) (storage limitation); Article 28(3)(a) (instruction-only processing); Article 28(3)(f) (processor assists with controller's regulatory obligations, including breach notification)
- **CH FADP**: Article 6(3) (purpose limitation); Article 9(2)(d) (processor assists controller)
- **ISO/IEC 27018:2025**: Controls A.6.1 and A.6.2

---

# Policy Statements: Retention Limitation (A.6 principle)

## Retention Schedule Adherence

[Organisation] SHALL retain PII on behalf of controllers only for the duration specified in the service agreement. Where the service agreement does not specify a retention period, [Organisation] SHALL request explicit written instructions from the PII controller before implementing any retention configuration.

[Organisation] SHALL implement automated retention enforcement (automated deletion or archival) wherever technically feasible. Reliance on manual deletion is acceptable only where automated enforcement is technically not possible, in which case manual deletion SHALL be documented and reviewed quarterly.

---

# Policy Statements: PII Disclosure Notification (A.6.1)

## Prior Notification Requirement

Where [Organisation] receives a legally binding request from a law enforcement agency, regulatory authority, court, or other governmental body requiring disclosure of PII belonging to a PII controller, [Organisation] SHALL:

1. Notify the relevant PII controller of the disclosure request **prior to disclosure**, including:
   - The identity of the requesting authority (to the extent legally permissible)
   - The categories and scope of PII requested
   - The legal basis cited for the request
   - The requested disclosure deadline

2. Allow the PII controller a reasonable opportunity to seek legal challenge or injunctive relief before disclosure, where the disclosure deadline permits

3. Process the disclosure only after:
   - Controller notification has been given and the response period has lapsed, or
   - The disclosure deadline requires immediate action, in which case the controller SHALL be notified simultaneously with disclosure

## Notification Prohibited by Law

Where applicable law prohibits [Organisation] from notifying the PII controller of a disclosure request (e.g., a legally imposed gag order), [Organisation] SHALL:

- Document the legal prohibition and the date from which notification is restricted
- Notify the PII controller at the **earliest opportunity** after the legal prohibition lapses
- If [Organisation] is permanently prohibited from notifying the controller (e.g., ongoing national security order), [Organisation] SHALL publish a transparency report or warrant canary to the maximum extent legally permissible

## Minimum Disclosure

All legally compelled disclosures SHALL be limited to the minimum PII required to satisfy the legal obligation. [Organisation] SHALL not provide broader access or data sets than specifically required by the legal order.

---

# Policy Statements: Recording of PII Disclosures (A.6.2)

## Disclosure Register

[Organisation] SHALL maintain a **PII Disclosure Register** recording every disclosure of PII to a third party, including legally compelled disclosures. Each entry SHALL record:

| Field | Description |
|-------|-------------|
| **Date of disclosure** | Date PII was disclosed or transferred |
| **Recipient** | Identity of the receiving party (authority, entity, or individual) |
| **Categories of PII disclosed** | Types of PII transferred (e.g., identity data, contact data, processing logs) |
| **Volume** | Approximate number of data subjects affected |
| **Legal basis** | Legal authority or controller instruction authorising the disclosure |
| **Controller notified** | Yes / No — and if No, reason and date of subsequent notification |
| **Authorised by** | [Organisation] officer who authorised the disclosure |

## Access and Retention

The PII Disclosure Register SHALL be:

- Maintained by the DPO and protected against unauthorised modification
- Made available to any PII controller upon request (for records pertaining to their PII)
- Retained for a minimum of **5 years** from the date of each recorded disclosure
- Subject to quarterly review by the DPO

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Owns the PII Disclosure Register; reviews and authorises all third-party PII disclosures; manages controller notification process; monitors for prohibited notification lapses |
| **Legal/Compliance Officer** | Assesses the legal validity of disclosure requests; advises on legal challenge options; interprets notification prohibition orders; manages warrant canary updates |
| **CISO / Cloud Security Manager** | Implements technical retention enforcement; ensures disclosure is technically limited to the minimum required scope |
| **Executive Management** | Approves disclosures in ambiguous or high-risk scenarios; authorises transparency reporting |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| PII Disclosure Register | Complete log of all third-party PII disclosures with mandatory fields | 5 years from each disclosure date |
| Retention Configuration Records | Technical documentation of automated retention enforcement per service | Current + 3 years |
| Controller Notification Records | Records of all notifications sent to controllers regarding compelled disclosures | 5 years |
| Legal Prohibition Documentation | Records of notification prohibition orders and dates of subsequent notification | 5 years |
| Transparency Reports / Warrant Canary | Published statements regarding absence of undisclosed legal orders | 5 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.6 should expect to find:

- A maintained PII Disclosure Register covering all third-party disclosures with complete mandatory fields
- Evidence that PII controllers were notified of all legally compelled disclosures (or documentation of why notification was legally prohibited)
- Automated retention enforcement configurations aligned with service agreement retention periods
- Legal/compliance records documenting how legally compelled disclosure requests were assessed and handled

---

<!-- QA_VERIFIED: [Date] -->
