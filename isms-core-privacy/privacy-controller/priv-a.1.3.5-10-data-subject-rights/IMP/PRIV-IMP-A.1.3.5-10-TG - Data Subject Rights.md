<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.3.5-10-TG:privacy:TG:a.1.3.5-10 -->
**PRIV-IMP-A.1.3.5-10-TG — Data Subject Rights — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Subject Rights — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.3.5-10-TG |
| **Related Policy** | PRIV-POL-A.1.3.5-10 (Data Subject Rights) |
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

- PRIV-POL-A.1.3.5-10 (Data Subject Rights — the governing policy)
- PRIV-IMP-A.1.3.5-10-UG (Data Subject Rights — User Guide)
- PRIV-POL-A.1.3.2-4 (Transparency and Information Provision — notice templates)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for data subject rights management. It covers:

- Data Subject Rights Register schema
- Request Acknowledgment template
- Rights Response Decision Tree
- Third Party Notification Record schema
- Erasure Verification template
- Consent Withdrawal Register schema

**Audience**: DPO, Legal/Compliance, IT Security Team.

---

## 1. Data Subject Rights Register

The primary log of all data subject rights requests. Owned by the DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Request ID | Text | Unique reference (e.g., DSR-2026-001) |
| Receipt Date | Date | Date request was received — day 1 of one-month clock |
| Receipt Channel | Enum | Email / Post / Web Form / Verbal (converted) / Portal |
| Requester Name | Text | Name of the data subject (or representative) |
| Representative | Text | If via representative: name and authority |
| Requester Contact | Text | Email or postal address for response |
| Right(s) Invoked | Multi-select | Access (15) / Rectification (16) / Erasure (17) / Restriction (18) / Portability (20) / Objection (21) / Consent Withdrawal (7(3)) |
| PII Scope | Text | What PII the request relates to (where known) |
| Identity Verification Method | Text | Method used to verify requester identity |
| Identity Verification Date | Date | Date identity was confirmed |
| Identity Verified | Enum | Confirmed / Pending / Failed |
| Data Collation Status | Enum | Not Started / In Progress / Complete |
| DPO Assessment Date | Date | Date DPO completed assessment |
| Response Type | Enum | Fulfilled / Partially Fulfilled / Refused / Extended |
| Exemption Applied (if refused/partial) | Text | Which exemption and rationale |
| Response Date | Date | Date response was sent to data subject |
| Response Method | Text | Email / Post / Portal |
| Extension Notified | Boolean | Yes / No |
| Extension Deadline | Date | If extended: new deadline date |
| Erasure Confirmed | Boolean | Yes / No / Not Applicable |
| Third Parties Notified | Boolean | Yes / No / Not Applicable |
| Supervisory Authority Complaint Raised | Boolean | Yes / No |
| Status | Enum | Open / Responded / Closed |
| Notes | Text | Complex decisions, exceptional circumstances |

---

## 2. Request Acknowledgment Template

```
Subject: Acknowledgment of Your Data Subject Rights Request [DSR-XXXX-XXX]

Dear [Name],

Thank you for your request received on [Date].

We are writing to confirm that we have received your request to exercise
your right to [access / rectification / erasure / restriction / portability /
object to processing / withdraw consent].

YOUR REQUEST REFERENCE: [DSR-XXXX-XXX]
Please quote this reference in any further correspondence about this request.

WHAT HAPPENS NEXT
We will review your request and respond within one month of the date of receipt
([Date + 1 month]).

In some cases, we may need to verify your identity before we can process your
request. If so, we will contact you separately with details of what is required.

If you have questions about your request or this process:
[DPO Name] | privacy@[domain] | [Phone if applicable]

You also have the right to contact [Supervisory Authority Name] if you have concerns:
[Supervisory Authority URL and contact]

[Organisation Legal Name]
```

---

## 3. Rights Response Decision Tree

Use this reference when assessing each right invoked:

### Access (Art. 15) — Key Questions
1. Is the request valid (is it actually a right of access request)?
2. Identity verified?
3. Does any exemption apply? (e.g., other individuals' data in the same records; legal professional privilege; crime prevention)
4. If no exemption: provide copy + supplementary Art. 15(1) information
5. If partial exemption: redact third-party information; provide the rest with explanation

### Erasure (Art. 17) — Assessment Checklist
At least ONE erasure ground must apply:
- [ ] PII no longer necessary for original purpose
- [ ] Consent withdrawn + no other basis
- [ ] Object upheld + no overriding legitimate grounds
- [ ] Unlawful processing confirmed
- [ ] Legal obligation to erase

At least ONE exemption must NOT apply:
- [ ] Legal claims (retention needed)
- [ ] Legal obligation to retain
- [ ] Public interest archiving / research
- [ ] Public health (Art. 9(2)(h)/(i))

If grounds met, no exemption: proceed with erasure. If exemption applies: document and refuse.

### Objection (Art. 21) — Direct Marketing
- Direct marketing objection: absolute right — cease immediately, no assessment.

### Objection (Art. 21) — Other Legitimate Interests
- DPO assesses: do compelling legitimate grounds exist that override the data subject's interests?
- If yes: continue processing + inform data subject + log assessment
- If no: cease processing + inform data subject + log outcome

---

## 4. Third Party Notification Record

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Notification ID | Text | Unique reference (e.g., TPN-2026-001) |
| DSR Request Reference | Text | Linked Data Subject Rights Register entry |
| Third Party | Text | Name of third party notified |
| PII Shared | Text | What PII was originally shared |
| Change Type | Enum | Rectification / Erasure / Restriction / Consent Withdrawal |
| Notification Method | Text | Email / API integration / Written |
| Notification Date | Date | Date third party was notified |
| Third Party Response | Text | Confirmation received / pending / not responded |
| Response Date | Date | Date confirmation received |
| Notified to Data Subject | Boolean | Yes / No |
| Notes | Text | Where notification was impossible/disproportionate — document reason |

---

## 5. Erasure Verification Template

```
ERASURE VERIFICATION RECORD

DSR Reference: DSR-[YYYY]-[NNN]
Data Subject Name: [Name]
Erasure Authorised By (DPO): [Name]
Date Erasure Authorised: [Date]

SYSTEMS TO ERASE FROM
(Complete for each system where data subject PII was held)

| System | Data Owner | PII Categories | Erasure Method | Confirmed By | Confirmation Date |
|--------|------------|----------------|----------------|--------------|-------------------|
| | | | Delete / Anonymise / Pseudonymise | | |

BACKUP ERASURE
Backup systems containing this PII: [List]
Backup erasure approach: [ ] On next backup overwrite (date: [___])
                          [ ] Manual extract and delete (date: [___])
                          [ ] Not applicable (backup already outside retention window)

THIRD PARTY ERASURE NOTIFICATIONS
(Complete if PII was shared externally)
[ ] Notification to third parties sent — see Third Party Notification Record [TPN-XXXX-XXX]
[ ] Not applicable — PII was not shared externally

CONFIRMATION
[ ] Erasure complete across all in-scope systems
[ ] Partial erasure — exceptions: [describe; document basis for retention]

IT Security Team Lead: _________________________ Date: _____________
DPO: _________________________ Date: _____________
Data Subject Notified: _________________________ Date: _____________
```

---

## 6. Consent Withdrawal Register

Tracks consent withdrawals separately from the main DSR register (consent withdrawal may occur outside a formal DSR process — e.g., via unsubscribe link or privacy settings).

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Withdrawal ID | Text | Unique reference (e.g., CW-2026-001) |
| Data Subject ID | Text | Internal identity reference |
| Processing Activity | Text | RoPA activity ID affected by the withdrawal |
| Withdrawal Date | Date | Date withdrawal was received |
| Withdrawal Channel | Enum | Email / Unsubscribe Link / Privacy Settings / Portal / Written Request |
| Consent Purpose(s) Withdrawn | Text | Specific purposes for which consent withdrawn |
| Processing Ceased Date | Date | Date on which processing based on consent stopped |
| Cessation Confirmed By | Text | DPO or Data Owner confirmation |
| Alternative Basis Applicable | Boolean | Yes / No |
| Alternative Basis Details | Text | If yes: basis and RoPA reference |
| PII Deleted / Anonymised | Enum | Deleted / Anonymised / Retained on Alternative Basis / Pending |
| Deletion Date | Date | If deleted: date confirmed |
| Third Parties Notified | Boolean | Yes / No / Not Applicable |
| Notification Record Reference | Text | TPN reference if applicable |
| Data Subject Confirmed | Boolean | Yes / No — confirmation sent to data subject |
| Status | Enum | Open / Completed |
| Notes | Text | Exceptional circumstances |

---

<!-- QA_VERIFIED: [Date] -->
