<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.3.2-UG:privacy:UG:a.2.3.2 -->
**PRIV-IMP-A.2.3.2-UG — PII Principal Obligations (Processor) — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | PII Principal Obligations (Processor) — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.2.3.2-UG |
| **Related Policy** | PRIV-POL-A.2.3.2 (PII Principal Obligations (Processor)) |
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

- PRIV-POL-A.2.3.2 (PII Principal Obligations (Processor) — the governing policy)
- PRIV-IMP-A.2.3.2-TG (PII Principal Obligations (Processor) — Technical Guide)
- PRIV-POL-A.2.2.2-7 (Processor Agreements and Obligations — foundational processor policy)

---

## Purpose of This Guide

This guide explains **how to implement** the PII principal obligations of PRIV-POL-A.2.3.2 — specifically, how [Organisation] as processor provides customers with the means to fulfil their data subject rights obligations. It covers the capabilities [Organisation] must make available, how to handle direct data subject contact, and how to respond to customer instructions for individual rights.

**Who this guide is for**: DPO, IT Security Team, Customer Success / Account Management.

**Processor-only**: This guide applies to processing activities where [Organisation] acts as PII Processor on behalf of customer controllers.

---

## Part 1 — Understanding the Processor's Role in Data Subject Rights

### 1.1 The Processor Does Not Own the Data Subject Relationship

Data subjects (PII principals) are the controller's data subjects — they have a legal relationship with the customer controller, not with [Organisation]. This means:

- Data subjects do not have rights against [Organisation] in [Organisation]'s capacity as processor
- [Organisation] does not decide how to respond to data subject rights requests — the customer controller decides
- [Organisation]'s obligation is to provide the **means** that enable the customer to respond correctly and within the required timeframe

### 1.2 What "Providing the Means" Requires

Providing the means for customer compliance means:

1. **Technical capabilities**: [Organisation]'s platform or service must be able to retrieve, correct, delete, or restrict individual data subjects' PII upon instruction
2. **Operational responsiveness**: [Organisation] must execute customer instructions for individual rights within timeframes that allow the customer to meet their regulatory deadline (typically one month from the data subject's request)
3. **Contractual commitment**: The processor agreement must document [Organisation]'s obligation to assist with these rights (per Article 28(3)(e))
4. **Direct request forwarding**: If a data subject contacts [Organisation] directly, [Organisation] must forward the request to the customer without delay

---

## Part 2 — Capabilities for Each Data Subject Right

### 2.1 Access (Article 15) and Portability (Article 20)

**Customer instruction**: "Provide all PII you hold for data subject [X] so we can respond to their access/portability request."

**[Organisation]'s response**:
1. Customer Success or DPO receives the instruction with the data subject identifier (customer-assigned ID, email, or equivalent)
2. IT Security Team or relevant technical team runs the data extraction for that individual across all systems where [Organisation] processes the customer's PII
3. The extracted data is provided to the customer in a structured, commonly used format — JSON, CSV, or as agreed in the processor agreement — within the agreed response time
4. For portability: machine-readable format (JSON preferred) is used
5. The response is logged in the Customer Data Subject Request Log

### 2.2 Rectification (Article 16)

**Customer instruction**: "Update field [Y] for data subject [X] from [old value] to [new value]."

**[Organisation]'s response**:
1. IT Security Team or relevant team implements the correction in all systems holding that individual's PII
2. Correction is confirmed to the customer with the date completed
3. Logged in the Customer Data Subject Request Log

### 2.3 Erasure (Article 17)

**Customer instruction**: "Delete all PII you hold for data subject [X]."

**[Organisation]'s response**:
1. IT Security Team identifies all systems (including backups within the scope agreed in the processor agreement) where the data subject's PII exists
2. Erasure is executed in primary systems immediately
3. For backup systems: erasure is scheduled per the backup cycle, and the expected deletion date is confirmed to the customer
4. Erasure is confirmed to the customer with the scope (primary systems: date; backups: expected date)
5. Logged in the Customer Data Subject Request Log

**Partial erasure**: If [Organisation] is under a legal obligation that requires retaining some PII (e.g., financial records, audit trails), this is communicated to the customer so they can manage the data subject's expectations accordingly. [Organisation] does not decide unilaterally whether the legal obligation overrides the erasure — that determination rests with the customer as controller.

### 2.4 Restriction (Article 18)

**Customer instruction**: "Apply a restriction flag to data subject [X] — processing to be limited to storage only."

**[Organisation]'s response**:
1. IT Security Team or relevant team applies a processing restriction marker to that data subject's records in applicable systems
2. The restriction marker prevents any active processing of those records while permitting storage
3. Restriction confirmed to customer; logged in the Customer Data Subject Request Log
4. When the customer instructs that the restriction is lifted, the restriction marker is removed

### 2.5 Objection (Article 21)

**Customer instruction**: "Cease processing for [specific purpose] for data subject [X]."

**[Organisation]'s response**:
1. IT Security Team or relevant team implements the cessation for the specified purpose for that data subject
2. Cessation confirmed to customer; logged in the Customer Data Subject Request Log

### 2.6 Response Timeframe Target

Customer instructions for data subject rights fulfilment are treated as priority requests. [Organisation]'s target response times:

| Right | Target Response to Customer |
|-------|-----------------------------|
| Access / Portability (data extraction) | Within 5 business days of instruction |
| Rectification | Within 2 business days of instruction |
| Erasure (primary systems) | Within 3 business days of instruction |
| Restriction | Within 2 business days of instruction |
| Objection | Within 2 business days of instruction |

These targets allow the customer to meet their one-month regulatory deadline even where the customer receives the data subject request close to the deadline.

---

## Part 3 — Handling Direct Data Subject Contact

### 3.1 When a Data Subject Contacts [Organisation] Directly

Data subjects sometimes contact [Organisation] directly with rights requests — for example, a user of a SaaS product contacts [Organisation]'s support team to request deletion of their account data.

**[Organisation] must NOT respond directly to the rights request** — the decision on how to respond belongs to the customer controller. Instead:

1. Acknowledge receipt to the data subject courteously: "Thank you for your request. Please be aware that [Organisation] processes data on behalf of your service provider. We have forwarded your request to them. They will respond to you directly."
2. Forward the request to the relevant customer's data protection contact within 1 business day
3. Log the forward in the Customer Data Subject Request Log, noting the date received and the date forwarded
4. Record in [Organisation]'s own log that the request was forwarded — do not action it without customer instruction

**[Organisation] does not decide** whether the data subject's right applies, whether an exemption exists, or how to respond — all of that is the customer's responsibility.

### 3.2 Identifying the Relevant Customer

If a data subject contacts [Organisation] and it is not immediately clear which customer's processing is involved (for example, if [Organisation] serves multiple customers with the same platform):

1. [Organisation]'s support team attempts to identify the relevant customer from the data subject's information (email domain, account reference, service name)
2. If the customer cannot be identified, [Organisation]'s DPO is notified; the DPO coordinates internally to identify the correct customer
3. If the customer truly cannot be identified, [Organisation] informs the data subject that it cannot identify the controlling organisation without more information, and requests clarifying details

---

## Evidence Checklist

- [ ] Rights fulfilment capability documentation — technical procedures for each right (access, rectification, erasure, restriction, objection) documented in TG
- [ ] Customer Data Subject Request Log — all customer instructions and [Organisation]'s fulfilment outcomes recorded
- [ ] Direct request forward records — data subjects contacting [Organisation] directly forwarded to customer within 1 business day
- [ ] Processor agreements — Article 28(3)(e) assistance commitment confirmed in all active DPAs
- [ ] Response timeframe targets — [Organisation] consistently meets 5-business-day (access) and 2-business-day (other) targets
- [ ] Annual capability review — DPO confirms rights fulfilment capabilities are operational and contractually committed

---

<!-- QA_VERIFIED: [Date] -->
