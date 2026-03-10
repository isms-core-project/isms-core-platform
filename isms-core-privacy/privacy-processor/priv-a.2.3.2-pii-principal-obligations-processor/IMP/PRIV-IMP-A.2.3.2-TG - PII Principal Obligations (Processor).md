<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.3.2-TG:privacy:TG:a.2.3.2 -->
**PRIV-IMP-A.2.3.2-TG — PII Principal Obligations (Processor) — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | PII Principal Obligations (Processor) — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.2.3.2-TG |
| **Related Policy** | PRIV-POL-A.2.3.2 (PII Principal Obligations (Processor)) |
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

- PRIV-POL-A.2.3.2 (PII Principal Obligations (Processor) — the governing policy)
- PRIV-IMP-A.2.3.2-UG (PII Principal Obligations (Processor) — User Guide)
- PRIV-IMP-A.2.2.2-7-TG (Processor Agreements — DPA schema and templates)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and reference specifications** for [Organisation]'s processor-side data subject rights fulfilment capabilities. It covers:

- Rights Fulfilment Capability Register schema
- Customer Data Subject Request Log schema
- Technical capability specification for each right
- Direct Request Forward Record template

**Audience**: DPO, IT Security Team, Customer Success.

---

## 1. Rights Fulfilment Capability Register

Documents [Organisation]'s technical capability for each data subject right, per service or platform. Reviewed annually and when services change. Maintained by IT Security Team in coordination with DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Capability ID | Text | Unique reference (e.g., RFC-001) |
| Service / Platform | Text | [Organisation] service to which this capability applies |
| Right | Enum | Access / Rectification / Erasure / Restriction / Portability / Objection |
| Capability Available | Enum | Fully Implemented / Partially Implemented / Manual Process / Not Yet Implemented |
| Implementation Method | Text | How the capability is executed (API, admin console, database procedure, manual) |
| Customer Instruction Channel | Text | How customers submit instructions (API endpoint, support portal, email to DPO) |
| Scope | Text | Systems covered by this capability (primary DB, backups, logs, caches) |
| Limitations | Text | Any known limitations (e.g., "Backup erasure delayed to next overwrite cycle — max 30 days") |
| Response Time Target | Text | [Organisation]'s target fulfilment time |
| Tested | Boolean | Yes / No |
| Last Test Date | Date | Date the capability was last tested |
| Test Result | Enum | Pass / Fail / Partial |
| Owner | Text | Technical owner role |
| Notes | Text | Outstanding gaps, planned improvements |

### Reference: Minimum Capability Requirements by Right

| Right | Minimum Technical Capability |
|-------|------------------------------|
| Access | Extract all PII for a given data subject identifier from all processing systems; export in structured format |
| Portability | Same as Access, but specifically in machine-readable format (JSON, CSV) |
| Rectification | Update specific PII fields for a given data subject across all primary systems |
| Erasure | Delete all PII for a given data subject from primary systems; schedule backup erasure; confirm scope and timeline |
| Restriction | Apply a processing restriction flag preventing active processing while permitting storage; reversible on instruction |
| Objection | Cease specified processing for a given data subject; reversible if grounds resolved |

---

## 2. Customer Data Subject Request Log

Records all customer instructions for data subject rights fulfilment, and [Organisation]'s fulfilment actions. Maintained by Customer Success / DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Log ID | Text | Unique reference (e.g., CSRQ-2026-001) |
| Customer Name | Text | Customer (controller) who issued the instruction |
| DPA Reference | Text | Linked Processor Agreement Register entry |
| Instruction Type | Enum | Access / Rectification / Erasure / Restriction / Portability / Objection / Direct Request Forward |
| Instruction Received Date | Date | Date instruction was received from customer |
| Data Subject Identifier | Text | Customer-provided identifier for the data subject (anonymised in log if possible) |
| Instruction Detail | Text | Description of what the customer has instructed |
| Customer Regulatory Deadline | Date | Date by which the customer needs [Organisation]'s fulfilment to meet their own deadline |
| Systems Affected | Text | Systems where fulfilment action is required |
| Fulfilment Actions Taken | Text | Description of what was done |
| Primary System Fulfilment Date | Date | Date fulfilment completed in primary systems |
| Backup Handling | Text | Approach and expected timeline for backup (if applicable) |
| Confirmation Sent to Customer | Boolean | Yes / No |
| Confirmation Date | Date | Date confirmation was sent to customer |
| Status | Enum | Open / Completed / Partial / Escalated |
| Notes | Text | Partial fulfilment reasons, escalations, limitations |

---

## 3. Direct Request Forward Record

Used when a data subject contacts [Organisation] directly with a rights request.

```
DIRECT DATA SUBJECT REQUEST FORWARD RECORD

Record ID: DRF-[YYYY]-[NNN]
Date Received: _____________
Received Via: [ ] Support ticket  [ ] Email  [ ] Phone  [ ] Other: _____________

DATA SUBJECT DETAILS
Name (if provided): _____________________________________________
Contact details (email / phone): _____________________________________________
Request type (as stated by data subject): _____________________________________________
Description of request: _____________________________________________

CUSTOMER IDENTIFICATION
Customer identified: [ ] Yes — Customer: _____________________________________________
                    [ ] No — identification steps taken: _____________________________________________

FORWARD ACTION
Forwarded to: _____________________________________________  (customer data protection contact)
Forwarded date: _____________________________________________
Forward method: [ ] Email  [ ] Portal  [ ] Other: _____________

ACKNOWLEDGMENT TO DATA SUBJECT
[ ] Acknowledgment sent to data subject
    Date sent: _____________
    Text: "Thank you for your request. [Organisation] processes data on behalf of service
    providers. We have forwarded your request to the relevant service provider. They will
    respond to you directly within the applicable timeframe."

DPO Notified: [ ] Yes  Date: _____________
Notes: _____________________________________________
```

---

## 4. Annual Rights Capability Review Checklist

Completed annually by IT Security Team and DPO.

```
ANNUAL DATA SUBJECT RIGHTS CAPABILITY REVIEW

Review Date: _____________
IT Security Lead: _____________
DPO: _____________

SERVICE: _____________________________________________

FOR EACH RIGHT — CONFIRM:

ACCESS / PORTABILITY
[ ] Export capability operational and tested in last 12 months
[ ] Output format is structured and machine-readable (JSON / CSV)
[ ] All relevant systems in scope (DB, logs, profile store, etc.) confirmed
[ ] Test date: _____________  Result: Pass / Fail

RECTIFICATION
[ ] Update capability operational across all primary systems
[ ] Test date: _____________  Result: Pass / Fail

ERASURE
[ ] Primary system deletion confirmed operational
[ ] Backup erasure approach documented and consistent with DPA commitments
[ ] Test date: _____________  Result: Pass / Fail

RESTRICTION
[ ] Restriction flag mechanism operational
[ ] Restriction correctly prevents active processing while permitting storage
[ ] Test date: _____________  Result: Pass / Fail

OBJECTION
[ ] Processing cessation for specified purpose operational
[ ] Test date: _____________  Result: Pass / Fail

CONTRACTUAL ALIGNMENT
[ ] Current DPA commitments match actual technical capability
[ ] Any capability gaps identified:
    _____________________________________________
[ ] Customer Success team briefed on updated capabilities

CONCLUSION
[ ] All capabilities operational — no gaps
[ ] Gaps identified — remediation plan: _____________________________________________
    Target remediation date: _____________

IT Security Lead: _________________________ Date: _____________
DPO: _________________________ Date: _____________
```

---

<!-- QA_VERIFIED: [Date] -->
