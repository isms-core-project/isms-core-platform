<!-- ISMS-CORE:IMP:CLD-IMP-A.1-TG:cloud:TG:a.1 -->
**CLD-IMP-A.1-TG — General — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | General — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.1-TG |
| **Related Policy** | CLD-POL-A.1 (General) |
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

- CLD-POL-A.1 (General — the governing policy)
- CLD-IMP-A.1-UG (General — User Guide)
- CLD-POL-A.11 (Information Security)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for managing [Organisation]'s obligations as a public cloud PII processor under ISO/IEC 27018:2025 Annex A, Section A.1. It covers:

- Processor Agreement Register schema
- Processing description schedule template
- Instruction Change Log schema
- Legally Compelled Processing Record template
- Sub-Processor Register schema

**Audience**: CISO, DPO, Legal/Compliance, Cloud Engineering.

---

## 1. Processor Agreement Register Schema

The Processor Agreement Register is the master record of all active and historical PII controller relationships. It is maintained by Legal/Compliance and reviewed quarterly by the DPO.

**Register fields:**

| Field | Type | Description |
|-------|------|-------------|
| `agreement_id` | String (unique) | Internal reference: `PA-YYYY-NNN` |
| `controller_name` | String | Legal name of the PII controller |
| `controller_jurisdiction` | String | Primary jurisdiction of the controller (e.g., EU, CH, UK) |
| `service_name` | String | Name of the cloud service provided |
| `service_tier` | Enum | IaaS / PaaS / SaaS |
| `agreement_type` | Enum | DPA / DPA + Schedule / MSA with DPA Annex |
| `effective_date` | Date | Date agreement entered into force |
| `expiry_date` | Date | Scheduled expiry date (or "Ongoing" for evergreen agreements) |
| `next_review_date` | Date | Date of next scheduled review |
| `processing_schedule_ref` | String | Reference to the completed processing description schedule |
| `sub_processors_approved` | Boolean | Whether controller has confirmed sub-processor list |
| `status` | Enum | Active / Expired / Terminated / Under Review |
| `dpo_sign_off_date` | Date | Date DPO reviewed and approved the processing schedule |
| `termination_date` | Date | Actual termination date (if applicable) |
| `pii_return_deletion_confirmed` | Boolean | Whether PII return/deletion confirmed at termination |
| `notes` | Text | Free-text field for exceptions, amendments, or escalation notes |

---

## 2. Processing Description Schedule Template

Each processor agreement must include a completed processing description schedule. The schedule below is the mandatory template.

---

**PROCESSING DESCRIPTION SCHEDULE**
**Agreement ID**: [PA-YYYY-NNN]
**Controller**: [Controller Legal Name]
**Service**: [Service Name]
**Effective Date**: [Date]

### A. Categories of PII Processed

| PII Category | Examples | Processing Justification |
|--------------|----------|--------------------------|
| [e.g., Identity data] | [Name, email, user ID] | [Required for user account management] |
| [e.g., Usage data] | [Logs, session data] | [Required for service delivery and support] |
| [Add rows as needed] | | |

### B. Processing Purposes

| Purpose | Description | Lawful Basis (Controller's) |
|---------|-------------|------------------------------|
| [e.g., Service delivery] | [Hosting and serving the controller's application] | [Contractual necessity — controller's assessment] |
| [Add rows as needed] | | |

### C. Processing Operations

| Operation | System Component | Frequency |
|-----------|------------------|-----------|
| [e.g., Storage] | [Production database] | [Continuous] |
| [e.g., Transmission] | [API endpoints] | [On-demand] |
| [Add rows as needed] | | |

### D. Processing Duration

| Phase | Duration |
|-------|----------|
| Active processing | Duration of service agreement |
| Post-termination retention | [As specified in agreement, typically 30 days] |
| Deletion/return deadline | [Date or "Within 30 days of termination"] |

### E. Sub-Processor Arrangements

| Sub-Processor | Role | Location | Controller Consent Date |
|---------------|------|----------|-------------------------|
| [Name] | [e.g., Cloud infrastructure] | [Country] | [Date] |
| [Add rows as needed] | | | |

**DPO Approval**: _________________________ Date: _____________

---

## 3. Instruction Change Log Schema

The Instruction Change Log records all changes to controller processing instructions during the service lifecycle. Maintained by Cloud Service Delivery; reviewed by the DPO.

| Field | Type | Description |
|-------|------|-------------|
| `log_id` | String (unique) | Internal reference: `ICL-YYYY-NNN` |
| `agreement_id` | String | Reference to the Processor Agreement Register |
| `change_date` | Date | Date instruction change was received or identified |
| `change_source` | Enum | Controller request / Service change / Regulatory update |
| `change_description` | Text | Description of the instruction change |
| `pii_categories_affected` | Text | PII categories affected by the change (if any) |
| `new_purpose_involved` | Boolean | Whether the change involves a new processing purpose |
| `new_sub_processor_involved` | Boolean | Whether the change involves a new sub-processor |
| `escalation_required` | Boolean | Whether escalation to DPO was required |
| `dpo_assessment` | Text | DPO's assessment and decision (if escalated) |
| `agreement_amendment_required` | Boolean | Whether formal agreement amendment was required |
| `amendment_completed_date` | Date | Date amendment was executed (if applicable) |
| `controller_authorising_contact` | String | Name and role of the controller contact who authorised the change |
| `recorded_by` | String | Name of Cloud Service Delivery team member recording the entry |

---

## 4. Legally Compelled Processing Record Template

This record must be completed whenever [Organisation] processes PII beyond controller instructions due to a legal obligation (e.g., law enforcement request, regulatory order).

---

**LEGALLY COMPELLED PROCESSING RECORD**
**Record ID**: [LCP-YYYY-NNN]
**Date of Event**: [Date]
**Agreement ID**: [Reference to affected processor agreement]

**1. Nature of Legal Requirement**

| Field | Detail |
|-------|--------|
| Requiring authority / legislation | [e.g., Law enforcement request under [Statute]; Regulatory order] |
| Jurisdiction | [Country / regulatory body] |
| Legal reference | [Statute, article, order number where known] |
| PII categories required | [List PII categories the legal obligation requires access to] |
| Processing required | [Describe the processing — e.g., disclosure, retention, restriction] |

**2. Controller Notification Assessment**

| Field | Detail |
|-------|--------|
| Is pre-processing notification to controller legally permitted? | Yes / No |
| If yes — controller notification date | [Date] |
| If no — reason notification is prohibited | [Legal basis for prohibition] |
| Date prohibition lapses (if known) | [Date or "Unknown"] |
| Post-lapse notification date | [Date — complete when notification is made] |

**3. DPO and Legal/Compliance Review**

| Reviewer | Name | Date | Assessment |
|----------|------|------|------------|
| Legal/Compliance | | | |
| DPO | | | |

**4. Processing Executed**

| Field | Detail |
|-------|--------|
| Processing start date | [Date] |
| Processing end date | [Date] |
| PII actually disclosed / processed | [Describe] |
| Minimum necessary principle applied | Yes / No / Partial — [Notes] |

---

## 5. Sub-Processor Register Schema

The Sub-Processor Register records all approved sub-processors and the controller consents obtained for each. Maintained by Legal/Compliance; reviewed annually by the DPO and CISO.

| Field | Type | Description |
|-------|------|-------------|
| `sub_processor_id` | String (unique) | Internal reference: `SP-NNN` |
| `sub_processor_name` | String | Legal name of the sub-processor organisation |
| `sub_processor_country` | String | Country of establishment / primary processing location |
| `service_role` | String | Description of processing role (e.g., cloud infrastructure, backup) |
| `pii_categories_accessed` | Text | PII categories accessible by sub-processor |
| `agreement_type` | Enum | DPA / DPA Annex / Standard Contractual Clauses |
| `agreement_date` | Date | Date sub-processor DPA was executed |
| `agreement_review_date` | Date | Date sub-processor agreement is next due for review |
| `iso27001_certified` | Boolean | Whether sub-processor holds ISO 27001 certification |
| `iso27018_certified` | Boolean | Whether sub-processor holds ISO 27018 certification |
| `soc2_type2` | Boolean | Whether sub-processor holds SOC 2 Type II report |
| `controllers_consented` | Text | List of controller agreement IDs where consent for this sub-processor has been obtained |
| `consent_notification_method` | Enum | General authorisation in agreement / Specific written consent |
| `last_audit_review_date` | Date | Date of most recent compliance review of this sub-processor |
| `status` | Enum | Active / Terminated / Under Review |
| `notes` | Text | Exceptions, objections received, or remediation notes |

---

<!-- QA_VERIFIED: [Date] -->
