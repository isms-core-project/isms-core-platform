<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.5.38-TG:sec:TG:a.5.38 -->
**CLD-SEC-IMP-A.5.38-TG — Shared Roles and Responsibilities — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Shared Roles and Responsibilities — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-SEC-IMP-A.5.38-TG |
| **Related Policy** | CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities within a Cloud Computing Environment) |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Cloud Security Manager |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial technical guide for ISO/IEC 27017:2026 Ed. 2 implementation |

**Review Cycle**: Annual (or upon significant change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities — the governing policy)
- CLD-SEC-IMP-A.5.38-UG (Shared Roles and Responsibilities — User Guide)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for documenting shared information security roles and responsibilities under ISO/IEC 27017:2026, Clause 5.38. It covers:

- Shared Responsibility Matrix schema (used in both the CSC and CSP roles)
- CSC-facing Capability Documentation template (CSP role)
- Allocation Gap Log schema

**Audience**: CISO, Cloud Security Manager, Cloud Engineering.

---

## 1. Shared Responsibility Matrix Schema

One matrix instance per cloud service relationship. Maintained by the Cloud Security Manager.

| Field | Type | Description |
|-------|------|-------------|
| `service_id` | String (unique) | Internal reference: `CSV-YYYY-NNN` |
| `service_name` | String | Name of the cloud service |
| `counterparty_name` | String | Name of the CSP (if [Organisation] is CSC) or CSC (if [Organisation] is CSP) |
| `organisation_role` | Enum | CSC / CSP / Both |
| `service_model` | Enum | IaaS / PaaS / SaaS |
| `shared_responsibility_model_ref` | String | Reference/version of the published shared responsibility model relied upon |
| `responsibility_area` | String | e.g. "Authentication", "Cryptography", "Backup", "Logging", "Patching", "Network segmentation" |
| `allocated_to` | Enum | CSC / CSP / Shared |
| `csc_action_required` | Text | What the CSC must do to fulfil its portion (if shared or CSC-allocated) |
| `csp_action_required` | Text | What the CSP must do to fulfil its portion (if shared or CSP-allocated) |
| `fulfilment_confirmed` | Boolean | Whether [Organisation] has confirmed it can/does fulfil its allocated portion |
| `last_reviewed_date` | Date | Date this responsibility area was last reviewed |
| `next_review_date` | Date | Date of next scheduled review |
| `notes` | Text | Exceptions, compensating controls, or escalation references |

---

## 2. CSC-Facing Capability Documentation Template

Used when [Organisation] acts as CSP and must publish capability information to its CSCs.

---

**CLOUD SERVICE SECURITY CAPABILITIES — [Service Name]**
**Version**: [Version] **Effective Date**: [Date]

### A. Authentication

| Capability | Description |
|-----------|-------------|
| Supported authentication methods | [e.g. password + MFA, SSO/SAML, OAuth 2.0] |
| Privileged access authentication | [e.g. mandatory MFA for administrative roles] |

### B. Cryptography

| Capability | Description |
|-----------|-------------|
| Encryption in transit | [e.g. TLS 1.2+] |
| Encryption at rest | [e.g. AES-256, provider-managed or customer-managed keys] |
| Key management options | [Describe available key management models] |

### C. Backup

| Capability | Description |
|-----------|-------------|
| Backup scope and schedule | [Describe] |
| Retention periods | [Describe] |
| Restoration process | [Describe] |

### D. Logging

| Capability | Description |
|-----------|-------------|
| Events logged | [Describe] |
| Log access for CSC | [Describe how the CSC can access relevant logs] |
| Log retention | [Describe] |

### E. Shared Responsibility Statement

| Responsibility Area | CSC | [Organisation] (CSP) |
|---------------------|-----|------------------------|
| [e.g. Application-level access control] | ✅ | |
| [e.g. Platform patching] | | ✅ |
| [e.g. Incident detection and notification] | | ✅ (notification) / ✅ (CSC-side response) |
| [Add rows per service] | | |

### F. Independent Assurance

| Framework / Certification | Status | Reference |
|---------------------------|--------|-----------|
| [e.g. ISO/IEC 27001] | [Certified / In progress] | [Certificate reference] |
| [e.g. SOC 2 Type II] | [Available on request] | [Report reference] |

---

## 3. Allocation Gap Log Schema

Records any gap identified in a Shared Responsibility Matrix and its resolution.

| Field | Type | Description |
|-------|------|-------------|
| `gap_id` | String (unique) | Internal reference: `ARG-YYYY-NNN` |
| `service_id` | String | Reference to the Shared Responsibility Matrix entry |
| `identified_date` | Date | Date the gap was identified |
| `identified_by` | String | Name/role of the person who identified the gap |
| `gap_description` | Text | Description of the unassigned or unfulfillable responsibility |
| `identification_source` | Enum | Onboarding review / Annual review / Incident / CSP or CSC notification |
| `escalated_to_ciso` | Boolean | Whether escalated to the CISO |
| `resolution_type` | Enum | Compensating control / Contractual amendment / Service reconsidered / Accepted risk |
| `resolution_description` | Text | Description of how the gap was resolved |
| `resolution_date` | Date | Date the gap was closed |
| `signed_off_by` | String | Name/role of the approver closing the gap |

---

<!-- QA_VERIFIED: 2026-08-01 -->
