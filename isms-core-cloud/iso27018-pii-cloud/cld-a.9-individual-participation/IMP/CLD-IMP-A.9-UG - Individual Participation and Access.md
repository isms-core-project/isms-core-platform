<!-- ISMS-CORE:IMP:CLD-IMP-A.9-UG:cloud:UG:a.9 -->
**CLD-IMP-A.9-UG — Individual Participation and Access — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Individual Participation and Access — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.9-UG |
| **Related Policy** | CLD-POL-A.9 (Individual Participation and Access) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial user guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory or service capability change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.9 (Individual Participation and Access — the governing policy)
- CLD-IMP-A.9-TG (Individual Participation and Access — Technical Guide)
- CLD-POL-A.2 (Consent and Choice — co-operation on data subject rights)
- CLD-POL-A.7 (Accuracy and Quality — rectification capability)
- CLD-POL-A.10 (Accountability — breach notification and end-of-contract obligations)

---

## Purpose of This Guide

This guide explains how [Organisation]'s Cloud Service Delivery and DPO teams manage incoming requests from PII controllers to assist with data subject rights fulfilment. It covers the end-to-end workflow from receiving a controller request to confirming completion, and addresses edge cases that require escalation or special handling.

**Who this guide is for**: Cloud Service Delivery, Data Protection Officer (DPO), Cloud Engineering (escalation), Legal/Compliance (dispute handling).

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. [Organisation] does not respond directly to data subjects. All rights requests are directed by data subjects to their controller; [Organisation]'s obligation is to provide the controller with the tools and co-operation needed to fulfil those requests within statutory timeframes.

---

## Part 1 — Receiving and Logging Controller Requests

### 1.1 How Controllers Submit Rights-Related Requests

PII controllers contact [Organisation] to request assistance with a data subject rights fulfilment operation. Requests may arrive via:

- The designated **Cloud Service Delivery inbox** or customer portal (preferred channel)
- A direct email to the DPO where the controller's DPA specifies that channel
- Escalation through an account manager for complex or urgent requests

All incoming requests SHALL be logged in the **Data Subject Rights Request Log** (see CLD-IMP-A.9-TG for the log schema) within **1 business hour** of receipt.

### 1.2 Acknowledging the Request

Acknowledge the controller's request **within 1 business day** of receipt. The acknowledgement SHALL:

1. Confirm receipt of the request and assign an internal reference number
2. State the expected completion timeframe (per CLD-POL-A.9 response timeframes)
3. Identify the Cloud Service Delivery contact responsible for the request
4. Note any information required from the controller to proceed (e.g., a unique data subject identifier)

Use the standard acknowledgement template maintained by the DPO. Do not commit to a completion date shorter than the policy timeframes without CISO approval.

---

## Part 2 — Processing Rights Fulfilment Operations

### 2.1 Access and Portability Requests (GDPR Art. 15 and 20)

When a controller requests an export of all PII associated with a specific data subject:

1. Obtain the data subject identifier from the controller (e.g., account ID, email address, or unique key used within the service)
2. Raise a service export task in the internal ticketing system, tagged as "DSR — Access/Portability"
3. Cloud Engineering executes the export covering all PII stores (primary database, backups, replicated copies, object storage) associated with that identifier
4. Deliver the export to the controller in the agreed format (JSON or CSV; see CLD-IMP-A.9-TG for the access response package format)
5. Complete within **5 business days** of receiving sufficient information from the controller

### 2.2 Erasure Requests (GDPR Art. 17)

When a controller requests deletion of all PII for a specific data subject:

1. Confirm with the controller that no legal hold or processing restriction applies that would defer the deletion
2. Raise an erasure task in the ticketing system, tagged "DSR — Erasure"
3. Cloud Engineering executes deletion across all primary stores and raises a backup purge job
4. Confirm propagation of deletion to backup copies (per the backup rotation cycle documented in the service agreement)
5. Issue a **written erasure confirmation** to the controller within **15 business days**, confirming scope, completion date, and backup purge status
6. Log the completion in the Data Subject Rights Request Log

### 2.3 Restriction Requests (GDPR Art. 18)

When a controller requests restriction of processing for a specific data subject:

1. Apply a restriction flag to the data subject's PII in the primary data store within **1 business day** (functional restriction)
2. Ensure restricted records are excluded from active processing pipelines, analytics, and downstream integrations
3. Confirm to the controller that functional restriction is in place and state the expected date for full propagation to replicated stores (within 5 business days)
4. Do not delete restricted records — restriction isolates PII from processing without deletion; the controller determines when to lift or convert the restriction to erasure

### 2.4 Rectification Requests (GDPR Art. 16)

When a controller provides corrected PII to be updated in [Organisation]'s systems:

1. Validate that the correction request includes sufficient identifying information to locate the correct record
2. Apply the correction to the primary data store and confirm propagation to replicated copies
3. Confirm completion to the controller within **5 business days**, including confirmation of replication propagation

### 2.5 Objection to Automated Processing (GDPR Art. 21)

When a controller requests suspension of automated processing involving a specific data subject's PII:

1. Apply a processing suspension flag to prevent the data subject's PII from being included in automated profiling, scoring, or decision-making pipelines
2. Confirm to the controller within **1 business day** that automated processing has been suspended
3. Document the suspension flag in the Data Subject Rights Request Log, including the scope of processing suspended

---

## Part 3 — Confirming Completion and Closing the Request

### 3.1 Completion Confirmation

For every rights fulfilment operation, issue a **written completion confirmation** to the controller. The confirmation SHALL include:

- The internal reference number and controller reference (if provided)
- The type of right exercised and the data subject identifier used
- Confirmation of completion, including the date the operation was finalised
- For erasure: confirmation that backup copies have been purged or the expected purge date
- The name of the Cloud Service Delivery contact responsible for the operation

### 3.2 Updating the Log

Close the request in the Data Subject Rights Request Log with:

- Actual completion date
- Outcome (completed, partially completed, or escalated with reason)
- Whether completion fell within the policy timeframe

---

## Part 4 — Edge Cases and Escalation

### 4.1 Deceased Data Subjects

Rights requests concerning deceased individuals require Legal/Compliance review before processing. Some jurisdictions extend data subject rights to next of kin or estate representatives; others do not. Escalate to the DPO and Legal/Compliance upon receipt and suspend processing until guidance is received.

### 4.2 Disputed or Ambiguous Identifiers

If the data subject identifier provided by the controller does not return a unique match in [Organisation]'s systems, do not proceed without clarification. Return to the controller within **1 business day** with a request for additional identifying information. Document the query in the log and pause the response timer pending controller response.

### 4.3 Capability Gaps

If [Organisation] is unable to fulfil a rights operation within the contracted timeframe due to a technical limitation:

1. Notify the DPO and CISO immediately
2. Issue a **partial notification** to the controller within the standard acknowledgement window, stating the limitation and the revised expected completion date
3. Log the gap as a remediation item for the annual capability testing programme (per CLD-POL-A.9)

### 4.4 Requests Conflicting with Legal Holds

Where [Organisation] is subject to a legal obligation that prevents erasure or return of specific PII (e.g., a court order, regulatory preservation requirement), escalate to Legal/Compliance before processing the request. Notify the controller of the hold and the basis for deferral within **1 business day**.

---

## Evidence Checklist

- [ ] Data Subject Rights Request Log is current, with all active and closed requests recorded
- [ ] All acknowledgements issued within 1 business day of request receipt
- [ ] Access/rectification/restriction requests completed within 5 business days
- [ ] Erasure requests completed (including backup confirmation) within 15 business days
- [ ] Written completion confirmations issued for all closed requests
- [ ] Edge cases (deceased subjects, disputes, legal holds) logged and escalated appropriately
- [ ] Annual capability test results on file for all rights types (per CLD-POL-A.9)

---

<!-- QA_VERIFIED: [Date] -->
