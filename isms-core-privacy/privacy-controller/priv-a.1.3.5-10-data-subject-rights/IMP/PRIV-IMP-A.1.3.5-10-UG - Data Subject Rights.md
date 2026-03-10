<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.3.5-10-UG:privacy:UG:a.1.3.5-10 -->
**PRIV-IMP-A.1.3.5-10-UG — Data Subject Rights — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Subject Rights — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.3.5-10-UG |
| **Related Policy** | PRIV-POL-A.1.3.5-10 (Data Subject Rights) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.3.5-10 (Data Subject Rights — the governing policy)
- PRIV-IMP-A.1.3.5-10-TG (Data Subject Rights — Technical Guide)
- PRIV-POL-A.1.3.2-4 (Transparency and Information Provision — rights communicated in notices)
- PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent — consent withdrawal)

---

## Purpose of This Guide

This guide explains **how to implement** the data subject rights requirements of PRIV-POL-A.1.3.5-10. It covers how to receive, validate, process, and respond to rights requests, how to manage consent withdrawal, and how to notify third parties of changes to shared PII.

**Who this guide is for**: DPO, Privacy Champions, Legal/Compliance, IT Security Team, all personnel who may receive a rights request.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Receiving and Logging a Rights Request (A.1.3.10)

### 1.1 How Rights Requests May Arrive

Data subjects can submit rights requests through any of the following channels:

- Email to the DPO's privacy contact address
- Written request by post
- Via a web form or privacy portal (where provided)
- Verbally (in person or by phone — must be converted to a written record immediately)
- Via a Privacy Champion in their business unit

**All personnel must forward any rights request received to the DPO immediately** — do not attempt to fulfil it independently or respond without DPO involvement.

### 1.2 Logging the Request

Within 1 business day of receiving a rights request, the DPO logs it in the Data Subject Rights Register (see PRIV-IMP-A.1.3.5-10-TG for the register schema). The one-month response clock starts from the **date of receipt** — not from the date the DPO becomes aware of it.

**Sending acknowledgment**: An acknowledgment must be sent to the data subject within 3 business days confirming receipt and providing an estimated response date (within one month of receipt). The acknowledgment does not confirm whether the request will be fulfilled — it simply confirms receipt.

### 1.3 Identifying the Type of Request

Classify the request in the register by right type. A single request may invoke multiple rights:

| Request Type | Trigger Phrases | Applicable Policy |
|-------------|----------------|-------------------|
| Access (SAR) | "What data do you hold on me?", "Send me a copy of my personal data" | Art. 15 |
| Rectification | "Correct my data", "Your records are wrong" | Art. 16 |
| Erasure | "Delete my account", "Remove my data", "Forget me" | Art. 17 |
| Restriction | "Stop using my data", "Freeze my data" | Art. 18 |
| Portability | "Transfer my data", "Send my data to [another controller]" | Art. 20 |
| Objection | "Stop processing my data", "Opt me out of profiling" | Art. 21 |
| Consent withdrawal | "I withdraw my consent", "Unsubscribe" (if consent-based) | Art. 7(3) |

---

## Part 2 — Identity Verification

### 2.1 Verifying the Requester's Identity

Before disclosing any PII or confirming erasure, verify the requester's identity. The level of verification is proportionate to the sensitivity of the PII:

| PII Sensitivity | Verification Method |
|----------------|---------------------|
| INTERNAL PII | Confirmation of name and account identifier (email, account number, employee ID) |
| CONFIDENTIAL PII | Name + account identifier + one additional identifier (date of birth, postcode, last transaction reference) |
| RESTRICTED PII (special category) | Strong verification: name + account identifier + two additional identifiers OR identity document reference |

**Do not request more information than necessary for verification.** Do not require a data subject to provide their data protection number, national insurance number, or sensitive identifiers as routine verification.

**If identity cannot be verified**: Contact the requester to request additional information. If verification fails after reasonable effort, explain why the request cannot be fulfilled in the current form and offer alternative verification paths.

### 2.2 Requests from Representatives

A data subject may have a request submitted on their behalf by a legal representative, parent (for children), or other authorised person. Verify:
- That the representative is authorised by the data subject (signed authorisation or power of attorney)
- The identity of both the representative and the data subject

---

## Part 3 — Processing Each Right

### 3.1 Subject Access Requests (Art. 15)

**What to provide**:
1. Confirmation that PII is (or is not) being processed about the data subject
2. A copy of all PII held — across all systems identified by Data Owners (check: CRM, HR system, marketing platform, support tickets, email if indexed, logs if accessible)
3. Supplementary information per Art. 15(1)(a)-(h): purposes, categories, recipients, transfers, retention, rights, right to complain, source (if not direct), automated decision-making

**Process**:
1. DPO contacts relevant Data Owners and IT Security Team to collate all PII held for the individual
2. Review the collated PII for any content that should be withheld (e.g., third party data, legally privileged information, information relating to another individual where disclosure would be unfair)
3. Prepare the response package — the PII copy plus the supplementary information
4. Send securely (encrypted email, password-protected document, or portal download)
5. Record in Data Subject Rights Register: response date, method, any withheld information and reason

**Response format**: Commonly used file format; PDF acceptable for most requests. Portability (Art. 20) requires machine-readable format (see 3.5 below).

### 3.2 Rectification Requests (Art. 16)

1. Assess whether the PII is inaccurate — may require verification from the data subject
2. Correct the inaccurate data in all relevant systems (coordinate with Data Owners and IT)
3. If accuracy is disputed: consider whether restriction of processing is appropriate pending resolution
4. Notify any third parties who were provided the inaccurate PII (per A.1.3.8 — see Part 4)
5. Confirm correction to data subject; record in register

### 3.3 Erasure Requests (Art. 17)

**Assessment — does the right to erasure apply?**

Work through the erasure grounds (any one of the following must apply):
- PII no longer necessary for the original purpose
- Consent withdrawn and no other basis applies
- Data subject objects and no overriding legitimate grounds
- PII unlawfully processed
- Erasure required by legal obligation

**Also check for exemptions** that would prevent erasure:
- Processing necessary for legal claims
- Processing necessary for archiving in public interest / scientific / historical research
- Legal obligation to retain

**If erasure applies**:
1. Identify all systems where the PII is stored (Data Owners confirm)
2. Execute erasure in production systems — confirm deletion with IT Security Team
3. Schedule erasure from backups (may not be immediate — document the approach and expected timeline)
4. Notify third parties who received the PII (per A.1.3.8)
5. Confirm erasure to data subject; document method and completeness in register

**If erasure does not apply** (exemption applies):
- Notify the data subject in writing explaining which exemption applies and why
- Inform of right to complain to supervisory authority
- Document the refusal reasoning in the register

### 3.4 Restriction and Objection Requests (Art. 18 / Art. 21)

**Restriction**: Flag the affected PII records in all relevant systems with a "restricted — processing suspended" marker. Confirm to IT Security Team which records/accounts are restricted. Processing limited to storage only until restriction is lifted.

**Objection (legitimate interests)**: DPO assesses whether compelling legitimate grounds exist. If not: cease processing and inform the data subject. If yes: inform the data subject of the grounds and their right to complain. Document the assessment.

**Objection (direct marketing)**: Immediate cessation — no assessment required. Remove from all marketing lists across all channels. Confirm cessation to data subject.

### 3.5 Portability Requests (Art. 20)

Right to portability applies only to:
- PII provided by the data subject (not inferred/derived)
- Processing based on consent or contract
- Processing carried out by automated means

Provide the PII in a machine-readable format (JSON, CSV, XML — agree with the data subject which format is preferred). Coordinate with IT Security Team to generate the export. If the data subject requests direct transfer to another controller, assess technical feasibility and proceed where reasonably practicable.

---

## Part 4 — Notifying Third Parties of Changes (A.1.3.8)

When a data subject's request leads to a change in PII (rectification, erasure, restriction, consent withdrawal), and that PII was shared with third parties:

1. Identify which third parties received the PII in question (from Processor Agreement Register, RoPA, transfer logs)
2. Notify each third party of the change — the same correction, erasure, or restriction must be applied at their end
3. Record the notifications sent (third party name, date notified, change communicated)
4. If notification proves impossible or disproportionate (e.g., PII was broadcast widely): document why; inform the data subject of the limitation

**On data subject request**: Provide the data subject with a list of which third parties were notified.

---

## Part 5 — Response Timeframe Management

| Milestone | Timeline |
|-----------|---------|
| Log request in register | Day 1 (date of receipt) |
| Send acknowledgment to data subject | Within 3 business days |
| Identity verification completed | Within 5 business days |
| Data collation from Data Owners / IT complete | Within 15 business days |
| DPO review and response preparation | Days 16–25 |
| Response sent | By Day 30 (one month from receipt) |
| If extension required: notify data subject of extension and reason | Before Day 30 |
| Extended response deadline (if extended) | Day 90 from receipt |

**Extensions**: Only for complex or numerous requests. Document the reason. Notify the data subject in writing before the first month expires.

---

## Evidence Checklist

- [ ] Data Subject Rights Register — all requests logged, response dates, outcomes
- [ ] Acknowledgment records — sent within 3 business days of request receipt
- [ ] Identity verification records — documented per request
- [ ] Response records — copies of responses sent; PII copies provided securely
- [ ] Refusal documentation — reasoning and right to complain communicated
- [ ] Erasure confirmation records — technical confirmation from IT/Data Owner
- [ ] Third party notification records — per A.1.3.8 where applicable
- [ ] Consent withdrawal records — processing cessation confirmed
- [ ] Extension notifications — sent before one-month deadline where applicable

---

<!-- QA_VERIFIED: [Date] -->
