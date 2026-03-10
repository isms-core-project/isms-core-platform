<!-- ISMS-CORE:IMP:CLD-IMP-A.4-TG:cloud:TG:a.4 -->
**CLD-IMP-A.4-TG — Collection Limitation — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Collection Limitation — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.4-TG |
| **Related Policy** | CLD-POL-A.4 (Collection Limitation) |
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

- CLD-POL-A.4 (Collection Limitation — the governing policy)
- CLD-IMP-A.4-UG (Collection Limitation — User Guide)
- CLD-POL-A.5 (Data Minimisation)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for implementing collection limitation controls under ISO/IEC 27018:2025 Annex A, Section A.4. It covers:

- Collection Scope Configuration Checklist per service tier
- Data flow mapping template for collection limitation review
- Excess PII Event Record and Development/Test Authorisation Register schemas

**Audience**: CISO, DPO, Cloud Engineering, Legal/Compliance.

---

## 1. Collection Scope Configuration Checklist

This checklist is completed by Cloud Engineering at service commencement and refreshed annually (or upon material architecture change). The DPO reviews and signs off each completed checklist. One checklist is maintained per active cloud service.

---

**COLLECTION SCOPE CONFIGURATION CHECKLIST**
**Service Name**: [Service Name]
**Agreement ID(s)**: [References to relevant Processor Agreement Register entries]
**Checklist Version**: [e.g., 1.0, 1.1 — increment on each refresh]
**Completed by (Cloud Engineering)**: [Name] Date: [Date]
**DPO Reviewed by**: [Name] Date: [Date]
**CISO Reviewed by**: [Name] Date: [Date]

### Part A — Approved PII Collection Scope

Derived from the processing description schedule. Only PII categories listed here may be collected.

| # | PII Category | Examples of Data Fields | Operational Justification | Collection Points (system components) | Retention Period | Deletion Method |
|---|-------------|------------------------|--------------------------|---------------------------------------|-----------------|-----------------|
| 1 | [e.g., User identity data] | [e.g., User ID, email address, display name] | [e.g., Required for user authentication and account management] | [e.g., User DB (prod), auth service logs] | [e.g., Duration of account + 30 days post-termination] | [e.g., Hard delete from DB; log purge on rotation] |
| 2 | [e.g., Usage telemetry] | [e.g., Session ID, timestamp, feature interaction events] | [e.g., Required for service performance monitoring and support] | [e.g., Application logs, APM tool] | [e.g., 90 days] | [e.g., Log rotation with secure overwrite] |
| 3 | [Add rows as needed] | | | | | |

### Part B — Collection Point Configuration Assessment

For each collection point identified above, Cloud Engineering confirms the following:

| Collection Point | PII categories received | Minimised to necessity? | Routed to internal analytics? | Routed to sub-processors? | Notes / Remediation Required |
|-----------------|------------------------|------------------------|------------------------------|--------------------------|------------------------------|
| [e.g., User DB (prod)] | [Identity data] | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| [e.g., Auth service logs] | [Identity data — partial: user ID only] | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| [e.g., APM tool] | [Usage telemetry] | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No | |
| [Add rows] | | | | | |

### Part C — Log and Telemetry Minimisation Confirmation

| Question | Answer | Notes |
|----------|--------|-------|
| Do application logs contain free-form PII fields (names, email addresses, postal addresses)? | Yes / No | |
| If yes — is this collection operationally justified within the service scope? | Yes / No / Partial | |
| Are log PII fields masked, tokenised, or redacted where technically feasible? | Yes / No | |
| Are log streams routed to any [Organisation] internal analytics or commercial intelligence system? | Yes / No | |
| Log retention period documented and compliant with collection scope? | Yes / No | |

### Part D — Non-Production Environment Assessment

| Question | Answer | Notes |
|----------|--------|-------|
| Is production PII used in any development, test, or staging environment? | Yes / No | |
| If yes — written controller authorisation obtained and filed? | Yes / No / N/A | [Ref: Dev/Test Authorisation Register ID] |
| Are equivalent security controls applied in non-production environments where production PII is used? | Yes / No / N/A | |

### Part E — Annual Review Record

| Review Date | Reviewed by (Engineering) | Reviewed by (CISO) | DPO Sign-off | Changes Since Last Review | Reduction Opportunities Identified |
|-------------|--------------------------|--------------------|--------------|--------------------------|------------------------------------|
| [Date] | [Name] | [Name] | [Name / Date] | [Description or "None"] | [Description or "None"] |
| [Date] | | | | | |

---

## 2. Data Flow Mapping Template for Collection Limitation Review

The data flow map is a structured record of how each PII category moves through the service from collection to deletion. Cloud Engineering produces and maintains one data flow map per active cloud service. The map is used during annual collection footprint reviews (CLD-IMP-A.4-UG, Part 2) and upon architecture changes.

### 2.1 Data Flow Map — Header

| Field | Value |
|-------|-------|
| Service Name | [Name] |
| Map Version | [e.g., 1.0] |
| Last Updated | [Date] |
| Updated by | [Name — Cloud Engineering] |
| DPO Reviewed | [Name / Date] |

### 2.2 PII Flow Table

Complete one row per PII category per distinct flow segment.

| Flow # | PII Category | Source / Entry Point | Processing Operation | Destination Component | Transfer Method | Encrypted in Transit? | Encrypted at Rest? | Retention at Destination | Deletion Trigger | Deletion Method | Sub-processor Involved? | Sub-processor Name (if yes) |
|--------|-------------|---------------------|---------------------|-----------------------|-----------------|----------------------|--------------------|--------------------------|-----------------|-----------------|------------------------|------------------------------|
| 1.1 | [e.g., User identity] | [e.g., Client API call] | [e.g., Write to user record] | [e.g., PostgreSQL prod DB] | [e.g., TLS 1.3] | ☐ Yes ☐ No | ☐ Yes ☐ No | [Duration of account] | [Account deletion] | [Hard delete] | ☐ Yes ☐ No | |
| 1.2 | [e.g., User identity] | [e.g., PostgreSQL prod DB] | [e.g., Replication] | [e.g., PostgreSQL read replica] | [e.g., Encrypted replication stream] | ☐ Yes ☐ No | ☐ Yes ☐ No | [Same as primary] | [Cascade from primary deletion] | [Cascade delete] | ☐ Yes ☐ No | |
| 2.1 | [e.g., Usage telemetry] | [e.g., Application server] | [e.g., Log write] | [e.g., Application log files] | [e.g., Local write] | N/A | ☐ Yes ☐ No | [90 days] | [Log rotation] | [Secure overwrite] | ☐ Yes ☐ No | |
| [Add rows] | | | | | | | | | | | | |

### 2.3 Collection Reduction Assessment Table

Completed during the annual collection footprint review.

| PII Category | Collection Point | Collection Currently Necessary? | Pseudonymisation Feasible? | Anonymisation Feasible? | Retention Reduction Feasible? | Recommended Action | Priority | Assigned To | Target Date | Completed Date |
|-------------|-----------------|--------------------------------|---------------------------|------------------------|------------------------------|-------------------|----------|-------------|-------------|----------------|
| [e.g., Email address in logs] | [Application logs] | Partial | Yes — replace with user ID hash | No | Yes — reduce to 30 days | Replace email with hashed user ID in log format | High | [Cloud Engineering Lead] | [Date] | |
| [Add rows] | | | | | | | | | | |

---

## 3. Excess PII Event Record and Development/Test Authorisation Register

### 3.1 Excess PII Event Record Schema

One record is created per excess PII event. Maintained by Cloud Service Delivery; reviewed by the CISO and DPO.

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | String (unique) | Internal reference: `XPE-YYYY-NNN` |
| `agreement_id` | String | Reference to the Processor Agreement Register |
| `service_name` | String | Cloud service where excess PII was identified |
| `date_identified` | Date | Date excess PII was identified |
| `identified_by` | String | Name and role of the team member who identified the excess |
| `excess_pii_description` | Text | Description of the excess PII: categories, estimated volume, data fields |
| `entry_point` | Text | How the excess PII entered the service (e.g., controller data upload, API response, configuration error) |
| `components_affected` | Text | System components, logs, or storage locations where excess PII is present |
| `isolated_from_processing` | Boolean | Whether excess PII was isolated from active processing |
| `isolation_date` | Date | Date isolation was completed (if applicable) |
| `breach_assessment_required` | Boolean | Whether DPO assessed this event against breach notification obligations |
| `breach_assessment_outcome` | Text | DPO's breach assessment outcome (if applicable) |
| `controller_notified` | Boolean | Whether the PII controller was notified |
| `controller_notification_date` | Date | Date of controller notification |
| `agreed_action` | Enum | Return to controller / Secure deletion |
| `action_completion_deadline` | Date | Date agreed with controller for action completion |
| `action_completed_date` | Date | Actual date action was completed |
| `action_confirmed_by` | String | Name confirming completion |
| `root_cause` | Text | Root cause of the excess collection event |
| `preventive_measure_implemented` | Text | Preventive measure implemented to prevent recurrence |
| `dpo_sign_off_date` | Date | Date DPO reviewed and closed the event |

### 3.2 Development/Test Authorisation Register Schema

Records all instances where production PII has been authorised for use in non-production environments.

| Field | Type | Description |
|-------|------|-------------|
| `authorisation_id` | String (unique) | Internal reference: `DTA-YYYY-NNN` |
| `agreement_id` | String | Reference to the Processor Agreement Register |
| `service_name` | String | Cloud service affected |
| `environment` | Enum | Development / Test / Staging / UAT |
| `pii_categories` | Text | PII categories authorised for use in non-production environment |
| `volume_scope` | Text | Description of volume and scope (e.g., subset of records, full dataset, specific date range) |
| `justification` | Text | Business justification provided by requesting team |
| `controller_written_authorisation` | Boolean | Whether written controller authorisation was obtained |
| `controller_authorisation_date` | Date | Date written authorisation was received |
| `controller_authorising_contact` | String | Controller contact name and role |
| `dpo_approved` | Boolean | Whether DPO approved the use |
| `dpo_approval_date` | Date | Date DPO approved |
| `ciso_approved` | Boolean | Whether CISO approved the use |
| `ciso_approval_date` | Date | Date CISO approved |
| `security_controls_equivalent` | Boolean | Whether equivalent security controls to production are confirmed |
| `security_controls_confirmation` | Text | Description of security controls applied in non-production environment |
| `start_date` | Date | Date non-production use commenced |
| `end_date` | Date | Date non-production use ended (PII deleted from non-production) |
| `deletion_confirmed` | Boolean | Whether deletion from non-production environment was confirmed |
| `deletion_confirmation_date` | Date | Date deletion was confirmed |

---

<!-- QA_VERIFIED: [Date] -->
