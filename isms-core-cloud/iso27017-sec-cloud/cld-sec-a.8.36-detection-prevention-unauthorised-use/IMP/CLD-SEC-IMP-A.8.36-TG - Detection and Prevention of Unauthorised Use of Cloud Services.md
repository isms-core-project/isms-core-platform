<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.8.36-TG:sec:TG:a.8.36 -->
**CLD-SEC-IMP-A.8.36-TG — Detection and Prevention of Unauthorised Use of Cloud Services — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Detection and Prevention of Unauthorised Use of Cloud Services — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-SEC-IMP-A.8.36-TG |
| **Related Policy** | CLD-SEC-POL-A.8.36 (Detection and Prevention of Unauthorised Use of Cloud Services) |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Security Operations Lead |
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

- CLD-SEC-POL-A.8.36 (Detection and Prevention of Unauthorised Use of Cloud Services — the governing policy)
- CLD-SEC-IMP-A.8.36-UG (Detection and Prevention of Unauthorised Use of Cloud Services — User Guide)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for monitoring cloud service user (CSU) activity and detecting unauthorised cloud service use under ISO/IEC 27017:2026, Clause 8.36. It covers:

- Monitoring Scope Decision Log schema
- Technical Compliance Review Record schema
- Anomaly Detection Log schema
- CSC-Facing Monitoring Guidance template

**Audience**: CISO, Security Operations Lead, Cloud Security Manager.

---

## 1. Monitoring Scope Decision Log Schema

Records the CISO-approved decision for cloud services where CSU activity monitoring is not mandatory (Public/Internal classification).

| Field | Type | Description |
|-------|------|-------------|
| `decision_id` | String (unique) | Internal reference: `MSD-YYYY-NNN` |
| `service_id` | String | Reference to the cloud service |
| `data_classification` | Enum | Public / Internal |
| `monitoring_implemented` | Boolean | Whether monitoring was implemented despite not being mandatory |
| `rationale` | Text | Rationale for the risk-based decision |
| `recommended_by` | String | Name/role of the Security Operations Lead making the recommendation |
| `approved_by` | String | Name/role of the CISO approving the decision |
| `decision_date` | Date | Date of decision |
| `review_date` | Date | Date of next scheduled review |

---

## 2. Technical Compliance Review Record Schema

Completed by the Security Operations Lead per the schedule set by service risk classification.

| Field | Type | Description |
|-------|------|-------------|
| `review_id` | String (unique) | Internal reference: `TCR-YYYY-NNN` |
| `service_id` | String | Reference to the cloud service |
| `review_date` | Date | Date of the review |
| `policies_checked` | Text | List of policies/standards checked against (information security policy, cloud usage policy, external standards) |
| `findings` | Text | Description of findings |
| `non_compliant_items` | Text | List of non-compliant items identified |
| `escalated_to` | String | Name/role the finding was escalated to (if non-compliant items found) |
| `remediation_due_date` | Date | Date remediation is due (if applicable) |
| `reviewed_by` | String | Name/role of the reviewer |

---

## 3. Anomaly Detection Log Schema

Records detected anomalies and their disposition.

| Field | Type | Description |
|-------|------|-------------|
| `anomaly_id` | String (unique) | Internal reference: `AND-YYYY-NNN` |
| `service_id` | String | Reference to the cloud service |
| `detected_date` | Date | Date/time the anomaly was detected |
| `anomaly_type` | Enum | Unexpected resource utilisation / Unknown service usage / Unauthorised data transfer / Unauthorised access / Other |
| `description` | Text | Description of the anomaly |
| `baseline_deviation` | Text | Description of how the observed activity deviates from the established baseline |
| `investigated_by` | String | Name/role of the investigator |
| `disposition` | Enum | False positive / Confirmed unauthorised use / Remediated / Escalated to incident response |
| `disposition_date` | Date | Date the anomaly was closed |
| `notes` | Text | Additional detail, including links to incident records if escalated |

---

## 4. CSC-Facing Monitoring Guidance Template

Used when [Organisation] delivers a cloud service to its own CSCs.

---

**CLOUD SERVICE MONITORING GUIDANCE FOR CSCs — [Service Name]**
**Version**: [Version] **Effective Date**: [Date]

### A. Available Activity Data

| Data Type | Description | Access Method |
|-----------|-------------|----------------|
| [e.g. Authentication events] | [Describe] | [e.g. Admin console, API, exportable log] |
| [e.g. Resource provisioning events] | [Describe] | [Describe] |
| [e.g. Data access events] | [Describe] | [Describe] |

### B. Configurable Monitoring Functions

| Function | Description | Configuration Method |
|----------|-------------|------------------------|
| [e.g. Custom alert thresholds] | [Describe] | [Describe] |
| [e.g. Anomaly notifications] | [Describe] | [Describe] |

### C. Recommended CSC Monitoring Practices

- [Recommendation 1, e.g. "Review authentication logs weekly for anomalous login patterns"]
- [Recommendation 2, e.g. "Configure alerts for resource provisioning outside business hours"]
- [Add as applicable to the service]

---

<!-- QA_VERIFIED: 2026-08-01 -->
