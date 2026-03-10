<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.8-10-TG:privacy:TG:a.3.8-10 -->
**PRIV-IMP-A.3.8-10-TG — Identity, Access and Supplier Controls — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Identity, Access and Supplier Controls — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.8-10-TG |
| **Related Policy** | PRIV-POL-A.3.8-10 (Identity, Access and Supplier Controls) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant technical or regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.8-10 (Identity, Access and Supplier Controls — the governing policy)
- PRIV-IMP-A.3.8-10-UG (Identity, Access and Supplier Controls — User Guide)
- PRIV-IMP-A.3.23-31-TG (Technical Security Controls — authentication and session standards)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management — ISMS framework)

---

## Purpose of This Guide

This guide specifies the **technical structures, register schemas, timelines, and configuration standards** required to implement PRIV-POL-A.3.8-10. It covers:

- Identity Register schema
- Access Rights Register schema
- Privileged session audit logging requirements
- Action timelines for lifecycle events
- Supplier Agreement Inventory schema
- PII supplier agreement clause checklist template

**Audience**: CISO, IT Security Team, DPO, Procurement, Legal/Compliance.

---

## 1. Identity Register

The Identity Register is the authoritative record of all identities with access to PII or PII processing systems. It is maintained by the IT Security Team with DPO oversight.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Identity ID | Text | Unique identifier (matches IAM system user ID) |
| Identity Type | Enum | Human — Employee / Human — Contractor / Human — Temporary / Non-human — Service Account / Non-human — Application |
| Full Name / Account Name | Text | Full name (human) or descriptive account name (non-human) |
| Department / System | Text | Business unit (human) or owning system (non-human) |
| Line Manager / Account Owner | Text | Responsible person for this identity |
| PII Access Scope | Text | PII datasets and systems accessible |
| Access Level | Enum | Standard / Elevated / Privileged |
| Provisioning Date | Date | Date identity was granted PII access |
| Provisioning Approval Ref | Text | Reference to Data Owner approval record |
| Last Access Rights Review | Date | Date of most recent access certification |
| Status | Enum | Active / Suspended / Decommissioned |
| Suspension Date | Date | If suspended: date of suspension |
| Suspension Reason | Text | If suspended: reason (role change / departure / investigation / other) |
| Decommissioning Date | Date | If decommissioned: date |
| Decommissioning Method | Text | Account deleted / disabled / archived |
| Notes | Text | Outstanding actions, audit flags |

### Identity Lifecycle Action Timelines

| Event | Required Action | Maximum Timeline |
|-------|----------------|-----------------|
| Role change notification received | Modify access scope | 3 business days |
| Planned departure notified | Remove access | On or before last working day |
| Immediate termination | Suspend access | Within 1 hour of HR notification |
| Termination — decommissioning | Complete decommissioning | Within 3 business days of suspension |
| Service account purpose discontinued | Suspend and decommission | Within 5 business days |
| Technical delay to decommissioning | Suspension must precede delay | Immediate suspension; decommission when resolved |

---

## 2. Access Rights Register

The Access Rights Register records what access each identity has to which PII datasets and systems. It is maintained by the IT Security Team with Data Owner oversight.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Access Record ID | Text | Unique reference for this access grant |
| Identity ID | Text | Reference to Identity Register |
| Identity Name | Text | Full name / account name |
| System / Dataset | Text | PII system or dataset the access applies to |
| Access Type | Enum | Read / Read-Write / Admin / Bulk Export / Full Privileged |
| Access Scope | Text | Specific tables, fields, or functions accessible |
| Granted By | Text | Role and name of approving Data Owner |
| Approval Reference | Text | Approval request document or ticket reference |
| Grant Date | Date | Date access was provisioned |
| Expiry Date | Date | If time-limited: expiry date; blank if permanent |
| Last Review Date | Date | Date of last access rights certification |
| Last Review Outcome | Enum | Confirmed / Modified / Removed |
| Removal Date | Date | If removed: date of removal |
| Removal Reason | Text | Role change / departure / certification / no longer required |
| Status | Enum | Active / Expired / Removed |
| Notes | Text | Changes, outstanding reviews |

### Access Rights Review Schedule

| Review Type | Frequency | Owner | Output |
|-------------|-----------|-------|--------|
| Full certification — standard access | Annual | Data Owner (per dataset) | Signed certification record |
| Full certification — privileged access | Every 6 months | Data Owner + CISO | Signed certification record |
| Role change review | Within 3 business days | Data Owner | Updated access scope |
| Post-incident review | Within 5 business days of incident closure | Data Owner + DPO | Review report + remediation actions |

### Access Rights Removal Timelines

| Trigger | Maximum Timeline for Removal |
|---------|------------------------------|
| Annual certification — access flagged for removal | 5 business days |
| Role change — access no longer required | 3 business days |
| Departure — planned | On or before last working day |
| Departure — immediate termination | Within 1 hour (suspension); removal within 3 business days |
| Time-limited access expiry | On expiry date |

---

## 3. Privileged Access — Audit Logging Requirements

All privileged identity sessions involving PII processing systems must generate audit logs with the following minimum fields:

| Log Field | Description |
|-----------|-------------|
| Timestamp | ISO 8601 with timezone |
| Identity ID | The privileged account used |
| Session ID | Unique session reference |
| Source IP / terminal | Network source of the privileged session |
| Systems accessed | PII systems and databases accessed during session |
| Actions performed | Commands executed, queries run, data accessed (at least at category level) |
| Data volume | Approximate volume of PII records accessed or exported |
| Session duration | Start and end timestamp |
| Outcome | Normal / Anomalous / Flagged for review |

**Retention**: Privileged access logs involving PII are retained for minimum 3 years.

**Review**: IT Security Team reviews privileged access logs for anomalies at minimum monthly. Anomalies are reported to the CISO and DPO.

**Tooling**: Where privileged access management (PAM) tooling is in use, configure session recording for PII system access. Minimum: command/query logging. Preferred: full session recording where technically feasible and legally permissible.

---

## 4. Supplier Agreement Inventory

The Supplier Agreement Inventory is the authoritative record of all supplier relationships and their PII categorisation. It is maintained by Procurement with DPO oversight.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Supplier ID | Text | Unique supplier reference |
| Supplier Name | Text | Legal entity name |
| Supplier Type | Text | SaaS / Managed Service / Professional Services / Infrastructure / Other |
| PII Category | Enum | PII Processor / PII-Adjacent Supplier / No PII Access |
| Categorisation Date | Date | Date PII categorisation was determined |
| Categorisation Confirmed By | Text | DPO name |
| PII Datasets Accessed | Text | List of PII datasets or systems the supplier accesses |
| PII Categories Involved | Multi-select | Ordinary / Financial / Special Category / Sensitive |
| Agreement Type | Enum | DPA (Art. 28) / PII Security Schedule / Standard Terms / None required |
| Agreement Reference | Text | Contract reference or document location |
| Agreement Status | Enum | In force / Expired / Under Negotiation / Not yet executed |
| Agreement Signed Date | Date | Date of execution |
| Agreement Expiry / Renewal Date | Date | Renewal or review date |
| Last DPO Review Date | Date | Date DPO last reviewed PII clause adequacy |
| Next Review Date | Date | Scheduled next review |
| Subcontractors / Sub-processors | Text | Known sub-processors or subcontractors (with PII access) |
| Security Certifications | Text | ISO 27001, SOC 2, etc. held by supplier |
| Incident History | Text | Reference to any security incidents involving this supplier |
| Notes | Text | Ongoing negotiations, open items, flags |

---

## 5. PII Supplier Agreement Clause Checklist Template

Use this checklist when reviewing a supplier agreement for PII adequacy. Record the clause reference (section number) in the agreement where each obligation is addressed.

**For PII Processor and PII-Adjacent Supplier categories:**

| Clause | Required For | Agreement Section | Adequate? |
|--------|-------------|------------------|-----------|
| Security obligation (TOMs equivalent to ours) | Both | | Yes / No / Partial |
| Prohibition on own-purpose PII use | Both | | Yes / No / Partial |
| Personnel confidentiality obligation | Both | | Yes / No / Partial |
| Confidentiality obligation survives termination | Both | | Yes / No / Partial |
| PII incident notification ≤ 24 hours (for breach risk) | Both | | Yes / No / Partial |
| Incident investigation cooperation | Both | | Yes / No / Partial |
| Return or secure deletion of PII on termination | Both | | Yes / No / Partial |
| Written deletion confirmation | Both | | Yes / No / Partial |
| Regulatory compliance acknowledgment (GDPR / FADP) | Both | | Yes / No / Partial |
| Process PII only on our instruction | PII Processor only | | Yes / No / Partial |
| Sub-processor prior written consent required | PII Processor only | | Yes / No / Partial |
| Flow-down of equivalent obligations to sub-processors | PII Processor only | | Yes / No / Partial |
| Audit rights or third-party audit report provision | PII Processor only | | Yes / No / Partial |
| GDPR Article 28(3) mandatory elements complete | PII Processor only | | Yes / No / N/A |

**Overall assessment:**
- [ ] Agreement is adequate for PII processing — approved for signature
- [ ] Agreement requires amendment before signature — items: [list]
- [ ] DPO sign-off: _________________ Date: _________

---

<!-- QA_VERIFIED: [Date] -->
