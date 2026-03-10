<!-- ISMS-CORE:IMP:CLD-IMP-A.6-TG:cloud:TG:a.6 -->
**CLD-IMP-A.6-TG — Use, Retention and Disclosure Limitation — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Use, Retention and Disclosure Limitation — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.6-TG |
| **Related Policy** | CLD-POL-A.6 (Use, Retention and Disclosure Limitation) |
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

- CLD-POL-A.6 (Use, Retention and Disclosure Limitation — the governing policy)
- CLD-IMP-A.6-UG (Use, Retention and Disclosure Limitation — User Guide)
- CLD-POL-A.10 (Accountability — PII return and disposal)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for use, retention, and disclosure limitation. It covers:

- PII Disclosure Register schema (mandatory fields per CLD-POL-A.6.2)
- Controller notification template for legally compelled disclosures
- Automated retention enforcement configuration checklist
- Warrant canary template and update process

**Audience**: CISO, DPO, Legal/Compliance, Cloud Engineering.

---

## 1. PII Disclosure Register Schema

Maintained by the DPO. Classified RESTRICTED. Minimum retention: 5 years from date of each disclosure.

| Field | Type | Description |
|-------|------|-------------|
| Disclosure ID | Text | Unique reference (e.g., DISC-2026-001) |
| Status | Enum | Under Assessment / Authorised / Disclosed / Closed |
| Date of Disclosure | Date | Date PII was disclosed to the requesting party |
| Requesting Authority | Text | Name and jurisdiction of the requesting authority |
| Authority Type | Enum | Law Enforcement / Regulatory Authority / Court Order / National Security / Other |
| Legal Basis Cited | Text | Specific legal provision cited in the order |
| PII Categories Disclosed | Text | Categories of PII transferred (e.g., identity data, contact data, usage logs) |
| Volume (approx.) | Text | Approximate number of data subjects affected |
| Controller(s) Affected | Text | Name(s) of PII controller(s) whose data is affected |
| Controller Notified | Enum | Yes — prior / Yes — simultaneous / No — legally prohibited / No — other |
| Controller Notification Date | Date | Date notification was sent to controller |
| Notification Prohibition | Boolean | Yes / No |
| Prohibition Legal Basis | Text | Legal provision prohibiting notification (if applicable) |
| Prohibition Lapse Date | Date | Date prohibition expired (if known) |
| Post-Prohibition Notification Date | Date | Date controller was notified after prohibition lapsed |
| Disclosure Scope Minimum Confirmed | Boolean | Yes / No — DPO confirmation that minimum scope applied |
| Authorised By (DPO) | Text | DPO name and date of authorisation |
| Legal/Compliance Assessment Ref | Text | Reference to Legal/Compliance validity assessment document |
| Transfer Method | Text | Method of transfer to requesting authority |
| Notes | Text | Challenge status, appeals, follow-up actions |

---

## 2. Controller Notification Template — Legally Compelled Disclosure

Used by the DPO to notify PII controllers of legally compelled disclosure requests. Send via the controller's designated data protection contact.

```
SUBJECT: [CONFIDENTIAL] Legally Compelled PII Disclosure Notification — [Disclosure ID]

Dear [Controller Data Protection Contact Name],

[Organisation] is writing to notify you of a legally compelled disclosure
request received in connection with PII processed by [Organisation] on
your behalf.

DISCLOSURE DETAILS

Requesting Authority: [Name and jurisdiction, to the extent legally permissible]
Authority Type: [Law enforcement / Regulatory authority / Court]
Legal Basis Cited: [Specific statutory provision cited in the order]
PII Categories Requested: [Categories of PII identified in the order]
Approximate Scope: [Number of data subjects or description of records]
Disclosure Deadline: [Date specified in the order, or "Not specified"]

NEXT STEPS

[Organisation] intends to process this disclosure on [date] unless:

- You provide written instructions to [Organisation] not to proceed by [date], or
- You obtain an injunction or other legal relief prior to the disclosure deadline

If you intend to seek legal challenge, please notify [Organisation]
immediately at [legal@organisation.example].

[Organisation] is limiting the disclosure to the minimum PII necessary
to satisfy the legal obligation. No broader access will be provided.

[Insert if prior notification prohibited: NOTE — This notification has been
delayed due to a legal prohibition that has now lapsed. The disclosure
was processed on [date]. We are now informing you at the earliest
opportunity following lapse of the prohibition.]

If you have any questions, please contact the DPO: [dpo@organisation.example]

Yours sincerely,
[DPO Name]
Data Protection Officer
[Organisation]
Date: _____________
Disclosure Reference: [Disclosure ID]
```

---

## 3. Automated Retention Enforcement Configuration Checklist

Completed by Cloud Engineering per controller during onboarding and at each annual service review.

| Check | Requirement | Status |
|-------|-------------|--------|
| Retention period documented | Controller retention period recorded in service configuration and DPA schedule | [ ] Pass / [ ] Fail |
| Automated deletion rule configured | Deletion or archival rule implemented in storage layer (e.g., object lifecycle policy, database TTL, log retention policy) | [ ] Pass / [ ] Fail |
| Rule tested | Automated deletion confirmed to trigger correctly in test environment | [ ] Pass / [ ] Fail |
| Retention period matches DPA | Configured period does not exceed the controller's DPA maximum | [ ] Pass / [ ] Fail |
| Manual override procedure documented | If automation not feasible: manual deletion procedure exists, documented, and reviewed quarterly | [ ] Pass / [ ] Fail |
| Controller confirmation sent | Cloud Service Delivery confirmed retention configuration to controller in writing | [ ] Pass / [ ] Fail |
| Configuration last reviewed | Date of most recent review | _______________ |

**Controller name**: _________________________
**Service**: _________________________
**Configured retention period**: _________________________
**Cloud Engineering sign-off**: _________________________ Date: _____________
**DPO confirmation**: _________________________ Date: _____________

---

## 4. Warrant Canary Template and Update Process

### 4.1 Warrant Canary Statement

Published on [Organisation]'s trust portal and updated at minimum annually. Removal or non-renewal constitutes an implicit signal that an undisclosed legal order has been received.

```
WARRANT CANARY — [Organisation]

Publication Date: [Date]
Next Review Date: [Date + 3 months]

[Organisation] affirms that, as of the date of this statement:

1. [Organisation] has NOT received any order, warrant, subpoena, or
   national security letter requiring disclosure of customer PII that
   [Organisation] is prohibited from disclosing.

2. [Organisation] has NOT been required by any court, authority, or
   government body to implement any backdoor, interception capability,
   or covert access mechanism in its cloud services.

3. [Organisation] has NOT been subject to any gag order that would
   prevent [Organisation] from notifying affected customers of a
   legally compelled disclosure.

This statement is reviewed and re-published quarterly. If this
statement is removed or not renewed on schedule, customers should
treat this as an implicit notification that one or more of the above
conditions may no longer hold.

Signed: [DPO Name], Data Protection Officer
Countersigned: [CEO / Legal Counsel Name]
Date: _____________
```

### 4.2 Warrant Canary Update Process

| Step | Responsible | Action |
|------|------------|--------|
| 1 | DPO | Confirms with Legal/Compliance that no new prohibited orders have been received |
| 2 | DPO | Drafts updated statement with new publication date |
| 3 | Legal/Compliance | Reviews and countersigns |
| 4 | DPO | Publishes to trust portal; archives previous version with timestamp |
| 5 | DPO | Records publication in PII Disclosure Register maintenance log |

If a prohibited order is received and the canary cannot be renewed honestly, the DPO escalates immediately to Executive Management and Legal/Compliance. The canary is allowed to lapse (not renewed) rather than published falsely. No false statement is to be published.

---

<!-- QA_VERIFIED: [Date] -->
