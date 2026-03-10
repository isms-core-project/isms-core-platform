<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.5.2-6-TG:privacy:TG:a.2.5.2-6 -->
**PRIV-IMP-A.2.5.2-6-TG — Transfer and Disclosure (Processor) — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Transfer and Disclosure (Processor) — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.2.5.2-6-TG |
| **Related Policy** | PRIV-POL-A.2.5.2-6 (Transfer and Disclosure (Processor)) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.2.5.2-6 (Transfer and Disclosure (Processor) — the governing policy)
- PRIV-IMP-A.2.5.2-6-UG (Transfer and Disclosure (Processor) — User Guide)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for processor-side transfer and disclosure management. It covers:

- Transfer Destination Register schema (processor-side)
- Transfer Change Notification Log schema
- Processor Disclosure Register schema
- Legally Binding Disclosure Request Log schema

**Audience**: DPO, Legal/Compliance.

---

## 1. Transfer Destination Register (Processor-Side)

Lists all countries and international organisations to which customer PII may be transferred in the course of [Organisation]'s service delivery. Made available to customers. Maintained by DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Destination ID | Text | Unique reference (e.g., PTDR-001) |
| Country / Territory | Text | Destination country or international organisation name |
| Transfer Mechanism | Enum | Adequacy (EU) / Adequacy (CH) / SCCs Module 2 / SCCs Module 3 / BCRs / Other |
| SCC Reference (if applicable) | Text | Reference to the SCC appendix or agreement incorporating the SCCs |
| Processing Context | Text | Why PII is transferred here (e.g., "Cloud hosting — AWS eu-west-1 DR failover to us-east-1", "Sub-processor X — email delivery") |
| Sub-processor Name (if applicable) | Text | Name of the sub-processor if this destination is driven by a sub-processor |
| PII Categories Affected | Text | Categories of customer PII that may be transferred here |
| Applicable Services | Text | [Organisation] services that involve this transfer destination |
| Applicable Customers | Text | Customer agreements covering this destination (or "All customers" for universal infrastructure) |
| First Documented | Date | Date this destination was first added to the register |
| Last Reviewed | Date | Date this entry was last confirmed as current |
| Status | Enum | Active / Planned / Decommissioned |
| Notes | Text | Adequacy status history, pending changes, risk flags |

---

## 2. Transfer Change Notification Log

Records all advance notifications sent to customers about transfer basis changes or new transfer destinations. Maintained by DPO / Customer Success.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Notification ID | Text | Unique reference (e.g., TCN-2026-001) |
| Change Description | Text | Nature of the change (e.g., "New sub-processor in India", "Data centre migrating from US to EU") |
| Affected Destination | Text | Country/destination involved |
| New Transfer Mechanism | Text | Mechanism after the change |
| Planned Effective Date | Date | When the change will take effect |
| Notification Sent Date | Date | Date customers were notified |
| Customers Notified | Text | List or category of customers notified |
| Notification Method | Enum | Email / Portal / Contractual notice |
| Objection Deadline | Date | Deadline for customers to object |
| Objections Received | Boolean | Yes / No |
| Objection Details | Text | If yes: customer name and nature of objection |
| Resolution | Text | How objection was handled (alternative arrangement, termination, etc.) |
| Change Proceeded | Boolean | Yes / No |
| Notes | Text | Urgent changes, legal drivers, exceptional circumstances |

---

## 3. Processor Disclosure Register

Records all disclosures of customer PII to third parties made by [Organisation] in the course of processing. Maintained by DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Disclosure ID | Text | Unique reference (e.g., PDISC-2026-001) |
| Date | Date | Date of disclosure |
| Customer | Text | Customer whose PII was disclosed |
| Recipient | Text | Name of the receiving third party |
| Recipient Type | Enum | Sub-processor / Professional Advisor / Regulatory Authority / Law Enforcement / Other |
| PII Categories Disclosed | Text | Categories of customer PII in the disclosure |
| Volume (approx.) | Text | Approximate record count or data scope |
| Basis for Disclosure | Enum | Customer Instruction / Contractual Authorisation / Legal Obligation / Sub-processor Engagement |
| Legal / Agreement Reference | Text | Court order reference, contractual clause, or sub-processor agreement reference |
| Customer Notified | Enum | Yes / No / Legally Prohibited |
| Customer Notification Date | Date | Date customer was notified (if applicable) |
| Transfer Mechanism (if cross-border) | Text | SCCs module, adequacy, or other mechanism |
| DPO Authorised | Boolean | Yes / No |
| Notes | Text | Restrictions on customer notification, scope limitations, follow-up actions |

---

## 4. Legally Binding Disclosure Request Log

Records all requests for customer PII from external parties (legal authorities, regulators, courts). Maintained by DPO with Legal/Compliance input. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Request ID | Text | Unique reference (e.g., LBDR-2026-001) |
| Date Received | Date | Date request was received |
| Requesting Authority | Text | Name of the requesting body |
| Authority Type | Enum | Law Enforcement / Court Order / Regulatory Authority / Other |
| Request Description | Text | Brief description of what was requested |
| Legal Authority Cited | Text | Specific law or legal instrument cited in the request |
| Customer(s) Affected | Text | Which customer's PII is involved |
| Legal/Compliance Assessment Date | Date | Date Legal/Compliance assessed the request |
| Binding Determination | Enum | Legally Binding / Non-Binding / Uncertain — escalated |
| Customer Notified | Enum | Yes / No — legally prohibited / No — not yet |
| Customer Notification Date | Date | Date customer was notified |
| Notification Prohibition | Text | If notification prohibited: legal basis for prohibition |
| Scope Limitation Applied | Boolean | Yes / No |
| Scope Limitation Description | Text | How the disclosure scope was narrowed |
| Disclosure Made | Boolean | Yes / No |
| Disclosure Date | Date | Date disclosure was executed |
| PII Categories Disclosed | Text | Scope of actual disclosure |
| Processor Disclosure Register Ref | Text | Linked PDISC entry |
| Notes | Text | Legal advice obtained, challenge attempts, prohibition lifting date |

---

<!-- QA_VERIFIED: [Date] -->
