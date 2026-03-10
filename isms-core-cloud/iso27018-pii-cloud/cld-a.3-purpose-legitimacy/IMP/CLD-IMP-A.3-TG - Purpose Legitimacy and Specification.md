<!-- ISMS-CORE:IMP:CLD-IMP-A.3-TG:cloud:TG:a.3 -->
**CLD-IMP-A.3-TG — Purpose Legitimacy and Specification — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Purpose Legitimacy and Specification — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.3-TG |
| **Related Policy** | CLD-POL-A.3 (Purpose Legitimacy and Specification) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.3 (Purpose Legitimacy and Specification — the governing policy)
- CLD-IMP-A.3-UG (Purpose Legitimacy and Specification — User Guide)
- CLD-POL-A.2 (Consent and Choice)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for managing purpose restriction and commercial use prohibition obligations under ISO/IEC 27018:2025 Annex A, Controls A.3.1 and A.3.2. It covers:

- Purpose Scope Review Checklist (pre-contract)
- Processing Instruction Change Log schema
- Unlawful Instruction Escalation Record template

**Audience**: CISO, DPO, Legal/Compliance, Cloud Engineering.

---

## 1. Purpose Scope Review Checklist (Pre-Contract)

This checklist is completed by Legal/Compliance (Part A) and the DPO (Part B) for every new cloud service engagement involving PII processing. It is filed with the processor agreement in the Processor Agreement Register.

---

**PURPOSE SCOPE REVIEW CHECKLIST**
**Agreement ID**: [PA-YYYY-NNN] (assigned from Processor Agreement Register)
**Controller**: [Controller Legal Name]
**Service**: [Service Name]
**Review Date**: [Date]
**Legal/Compliance Reviewer**: [Name]
**DPO Reviewer**: [Name]

### Part A — Factual Mapping (Legal/Compliance)

**A1. Proposed processing purposes as stated by controller:**

| # | Purpose as stated | Specific enough? (Y/N) | Notes |
|---|------------------|------------------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| [Add rows] | | | |

**A2. PII categories proposed:**

| PII Category | Operational justification provided by controller? (Y/N) | Special category under GDPR Art. 9? (Y/N) |
|--------------|--------------------------------------------------------|-------------------------------------------|
| | | |
| | | |
| [Add rows] | | | |

**A3. Service delivery scope assessment:**

| Assessment Item | Result | Notes |
|----------------|--------|-------|
| Can [Organisation] deliver the service within the proposed purpose boundaries? | Yes / No / Conditional | |
| Does service delivery require [Organisation] to make independent decisions about processing means? | Yes / No | |
| Does service architecture route PII through any component not covered by the proposed purposes? | Yes / No | |
| Does [Organisation]'s service telemetry collection fall within the proposed purposes? | Yes / No | |

### Part B — Purpose Assessment (DPO)

**B1. Processor vs. controller role assessment:**

| Question | Answer | Basis |
|----------|--------|-------|
| Do the proposed processing operations require [Organisation] to act as a controller for any part of the processing? | Yes / No | |
| Are the proposed purposes defined by the controller (not [Organisation])? | Yes / No | |

**B2. Facial lawfulness assessment (not a full legal opinion):**

| Question | Answer | Notes |
|----------|--------|-------|
| Do any proposed purposes involve special category PII without an indication of applicable exemption or controller legal basis? | Yes / No | |
| Do any proposed purposes require transfer of PII to a third country without an indicated transfer mechanism? | Yes / No | |
| Do any proposed purposes on their face require [Organisation] to participate in activity that would be unlawful in [Organisation]'s jurisdiction? | Yes / No | |

**B3. Commercial use check:**

| Question | Answer | Notes |
|----------|--------|-------|
| Does the proposed agreement include any clause permitting [Organisation] to use controller PII for [Organisation]'s own commercial purposes? | Yes / No | |
| If yes — has explicit controller written authorisation been obtained and DPO-reviewed? | Yes / No / N/A | |

**B4. DPO Determination:**

| Determination | Selected (✓) |
|---------------|:---:|
| Accept — processing purposes are specific, lawful on their face, and within [Organisation]'s processor role | |
| Accept with clarification — minor clarifications required; acceptable after response from controller | |
| Escalate — material concerns requiring further assessment before agreement execution | |
| Decline — proposed processing purposes cannot be accepted | |

**DPO Determination Notes**: _______________________________________________

**DPO Signature**: _________________________ Date: _____________

---

## 2. Processing Instruction Change Log Schema

The Processing Instruction Change Log records all changes to, or deviations from, the agreed processing purposes during service delivery. This log captures both formally agreed changes (via controller authorisation) and any purpose drift events identified and corrected by [Organisation]. Maintained by Cloud Service Delivery; reviewed by the DPO.

| Field | Type | Description |
|-------|------|-------------|
| `change_id` | String (unique) | Internal reference: `PCL-YYYY-NNN` |
| `agreement_id` | String | Reference to the Processor Agreement Register |
| `service_name` | String | Cloud service affected |
| `event_date` | Date | Date the change or drift event was identified or received |
| `event_type` | Enum | Controller instruction change / Purpose drift identified / Telemetry scope change / Architecture change |
| `event_description` | Text | Description of the change or drift |
| `pii_categories_affected` | Text | PII categories involved |
| `new_purpose_introduced` | Boolean | Whether the event introduces a new processing purpose |
| `within_existing_agreement` | Boolean | Whether the processing falls within existing agreed purposes on review |
| `technical_correction_required` | Boolean | Whether a technical correction was required to return to scope |
| `technical_correction_description` | Text | Description of correction implemented (if applicable) |
| `controller_authorisation_required` | Boolean | Whether formal controller authorisation for new purpose was required |
| `controller_authorisation_received` | Boolean | Whether controller authorisation was received |
| `controller_authorisation_date` | Date | Date written controller authorisation was received (if applicable) |
| `authorising_contact` | String | Controller contact name and role who provided authorisation |
| `dpo_assessment` | Text | DPO assessment and determination |
| `dpo_sign_off_date` | Date | Date DPO reviewed and signed off |
| `agreement_amendment_required` | Boolean | Whether a formal processor agreement amendment was required |
| `amendment_executed_date` | Date | Date amendment was executed (if applicable) |
| `recorded_by` | String | Name of team member recording the entry |

---

## 3. Unlawful Instruction Escalation Record Template

This record is completed whenever [Organisation] receives controller instructions that appear to require unlawful processing under CLD-POL-A.3 or CLD-IMP-A.3-UG, Part 3.

---

**UNLAWFUL INSTRUCTION ESCALATION RECORD**
**Record ID**: [UIE-YYYY-NNN]
**Date Identified**: [Date]
**Agreement ID**: [Reference to Processor Agreement Register]
**Service**: [Service Name]

**1. Description of the Instruction**

| Field | Detail |
|-------|--------|
| Instruction as received | [Verbatim or close paraphrase of the instruction] |
| Date instruction received | [Date] |
| Received from (controller contact) | [Name and role] |
| PII categories affected | [List] |
| Nature of concern | [Description — e.g., instruction requires transfer to non-adequate country without safeguard; instruction requires processing of special category PII without indicated basis] |
| Identified by | [Name and team] |

**2. Processing Suspension**

| Field | Detail |
|-------|--------|
| Processing of this instruction suspended pending assessment | Yes / No |
| If no — reason | [Explanation] |
| Suspension effective date | [Date] |

**3. Legal/Compliance and DPO Assessment**

| Field | Detail |
|-------|--------|
| Legal/Compliance reviewer | [Name] |
| DPO reviewer | [Name] |
| Assessment date | [Date] |
| Assessment outcome | Instruction lawful on further analysis / Instruction unlawful / Requires clarification from controller |
| Assessment basis | [Summary of legal reasoning] |

**4. Controller Engagement**

| Field | Detail |
|-------|--------|
| Controller notified of concern | Yes / No |
| Date notified | [Date] |
| Notification method | [Email / Call / Formal letter] |
| Controller response | [Description] |
| Revised instructions received | Yes / No |
| Date revised instructions received | [Date] |

**5. Resolution**

| Field | Detail |
|-------|--------|
| Resolution outcome | Instructions accepted (revised) / Instructions declined / Agreement suspended / Agreement terminated |
| Resolution date | [Date] |
| CISO notified | Yes / No — [Date] |
| Executive escalation required | Yes / No |
| Executive decision | [If applicable] |

**DPO sign-off**: _________________________ Date: _____________
**CISO sign-off**: _________________________ Date: _____________

---

<!-- QA_VERIFIED: [Date] -->
