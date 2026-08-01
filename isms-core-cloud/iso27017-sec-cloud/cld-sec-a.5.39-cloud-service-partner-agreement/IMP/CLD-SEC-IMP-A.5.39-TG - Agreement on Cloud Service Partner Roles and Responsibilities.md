<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.5.39-TG:sec:TG:a.5.39 -->
**CLD-SEC-IMP-A.5.39-TG — Agreement on Cloud Service Partner Roles and Responsibilities — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Agreement on Cloud Service Partner Roles and Responsibilities — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-SEC-IMP-A.5.39-TG |
| **Related Policy** | CLD-SEC-POL-A.5.39 (Agreement on the Roles and Responsibilities of the Cloud Service Partner) |
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

- CLD-SEC-POL-A.5.39 (Agreement on the Roles and Responsibilities of the Cloud Service Partner — the governing policy)
- CLD-SEC-IMP-A.5.39-UG (Agreement on Cloud Service Partner Roles and Responsibilities — User Guide)
- CLD-SEC-IMP-A.5.38-TG (Shared Responsibility Matrix schema — referenced for consistency checks)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for classifying and agreeing cloud service partner (CSN) roles and responsibilities under ISO/IEC 27017:2026, Clause 5.39. It covers:

- CSN Role Register schema
- CSN Responsibility Statement template
- Consistency Check Record schema

**Audience**: CISO, Cloud Security Manager, Legal/Compliance.

---

## 1. CSN Role Register Schema

Maintained by the Cloud Security Manager; reviewed annually.

| Field | Type | Description |
|-------|------|-------------|
| `csn_id` | String (unique) | Internal reference: `CSN-YYYY-NNN` |
| `csn_name` | String | Legal name of the cloud service partner |
| `sub_role_developer` | Boolean | Whether the CSN acts as a cloud service developer |
| `sub_role_auditor` | Boolean | Whether the CSN acts as a cloud auditor |
| `sub_role_broker` | Boolean | Whether the CSN acts as a cloud service broker |
| `related_service_id` | String | Reference to the Shared Responsibility Matrix entry (CLD-SEC-IMP-A.5.38-TG, Section 1) this CSN supports |
| `related_relationship_role` | Enum | Supports [Organisation]'s CSC role / Supports [Organisation]'s CSP role / Both |
| `agreement_ref` | String | Reference to the executed CSN agreement |
| `agreement_date` | Date | Date the agreement was executed |
| `responsibility_statement_ref` | String | Reference to the CSN Responsibility Statement (Section 2) |
| `also_delivers_cloud_service` | Boolean | Whether this CSN also independently delivers a cloud service to [Organisation] (triggers CLD-SEC-IMP-A.5.38-TG treatment for that portion) |
| `consistency_check_ref` | String | Reference to the Consistency Check Record (Section 3) |
| `last_reviewed_date` | Date | Date of last annual review |
| `next_review_date` | Date | Date of next scheduled review |
| `status` | Enum | Active / Terminated / Under Review |
| `notes` | Text | Scope-change history, exceptions, escalation references |

---

## 2. CSN Responsibility Statement Template

Incorporated into the CSN's written agreement per ISMS-POL-A.5.19-23-S2.

---

**CLOUD SERVICE PARTNER — RESPONSIBILITY STATEMENT**
**CSN ID**: [CSN-YYYY-NNN]
**Cloud Service Partner**: [Legal Name]
**Related Cloud Service**: [Service ID / Name]

### A. Classified Sub-Role(s)

| Sub-role | Applies |
|----------|---------|
| Cloud service developer | [Yes/No] |
| Cloud auditor | [Yes/No] |
| Cloud service broker | [Yes/No] |

### B. Assigned Information Security Responsibilities

| Responsibility | Description | Related Shared Responsibility Matrix Area |
|-----------------|-------------|--------------------------------------------|
| [e.g. Secure code review] | [Describe] | [e.g. "Application security"] |
| [e.g. Independent control assessment] | [Describe] | [e.g. "Compliance verification"] |
| [Add rows as needed] | | |

### C. Consistency Confirmation

| Field | Detail |
|-------|--------|
| Shared Responsibility Matrix reference checked | [Service ID] |
| Confirmed no unauthorised reassignment of CSC/CSP responsibility | Yes / No — if No, describe counterparty consent obtained |

**Cloud Security Manager Sign-off**: _________________________ Date: _____________

---

## 3. Consistency Check Record Schema

Records the check performed before a CSN agreement is signed, confirming it does not conflict with the CSC/CSP shared responsibility allocation.

| Field | Type | Description |
|-------|------|-------------|
| `check_id` | String (unique) | Internal reference: `CCR-YYYY-NNN` |
| `csn_id` | String | Reference to the CSN Role Register |
| `related_service_id` | String | Reference to the Shared Responsibility Matrix entry checked against |
| `check_date` | Date | Date the check was performed |
| `checked_by` | String | Name/role of the person performing the check |
| `conflict_identified` | Boolean | Whether a conflict with the existing allocation was identified |
| `conflict_description` | Text | Description of the conflict (if any) |
| `counterparty_consent_obtained` | Boolean | Whether CSC/CSP consent was obtained to resolve the conflict |
| `resolution_description` | Text | How the conflict was resolved |
| `outcome` | Enum | Cleared / Cleared with amendment / Escalated to CISO |

---

<!-- QA_VERIFIED: 2026-08-01 -->
