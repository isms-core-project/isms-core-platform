<!-- ISMS-CORE:IMP:CLD-IMP-A.2-UG:cloud:UG:a.2 -->
**CLD-IMP-A.2-UG — Consent and Choice — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Consent and Choice — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.2-UG |
| **Related Policy** | CLD-POL-A.2 (Consent and Choice) |
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

**Review Cycle**: Annual (or upon significant regulatory or service model change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.2 (Consent and Choice — the governing policy)
- CLD-IMP-A.2-TG (Consent and Choice — Technical Guide)
- CLD-POL-A.1 (General)
- CLD-POL-A.3 (Purpose Legitimacy and Specification)
- CLD-POL-A.9 (Individual Participation and Access)

---

## Purpose of This Guide

This guide explains how [Organisation] implements its obligations as a public cloud PII processor under ISO/IEC 27018:2025 Annex A, Section A.2 and Control A.2.1. It covers three operational areas: how to handle requests to process beyond controller instructions (including the escalation procedure), how to manage situations where processing is legally compelled, and how to handle data subject rights cooperation requests from PII controllers. It is intended for teams that operate cloud services and respond to controller and data subject queries.

**Who this guide is for**: CISO, DPO, Cloud Service Delivery, Legal/Compliance.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. [Organisation] does not determine the legal basis for processing; it processes only on documented controller instructions. Consent and choice obligations in this guide concern [Organisation]'s own conduct as a processor, not the controller's consent management with data subjects.

---

## Part 1 — Handling Requests to Process Beyond Controller Instructions

### 1.1 What Constitutes Out-of-Scope Processing

Out-of-scope processing is any processing of controller PII that is not covered by the current processing description schedule or written controller instructions. Examples include:

- A request from [Organisation]'s product team to use controller PII for product analytics or testing
- A proposal to share controller PII with a new third party not listed as a sub-processor
- A request from [Organisation]'s marketing team to use controller PII for audience profiling or campaign targeting
- Processing controller PII through a machine learning pipeline or model training workload without explicit controller authorisation

CLD-POL-A.2 and CLD-POL-A.3 together prohibit all such processing without explicit written controller authorisation.

### 1.2 Escalation Procedure — Requests for Out-of-Scope Processing

When any [Organisation] team member identifies a request, proposal, or technical configuration that would involve processing controller PII beyond the documented instructions, they SHALL follow this procedure:

1. **Stop.** Do not proceed with the out-of-scope processing. If a system or pipeline is already operating in a way that may exceed instructions, suspend the relevant component if technically feasible.
2. **Notify the DPO immediately.** The DPO must be informed on the same business day. Notification is via the DPO's designated escalation channel (defined in the DPO's contact record). Include: a description of the proposed or actual processing, the PII categories involved, the identity of the requesting party, and the business rationale.
3. **DPO assessment.** The DPO assesses whether the processing is permissible under the current processor agreement. The DPO has 2 business days to complete the initial assessment.
4. **If permissible with controller authorisation.** The DPO or Legal/Compliance contacts the relevant controller to obtain explicit written authorisation. Processing SHALL NOT proceed until authorisation is received and recorded.
5. **If not permissible.** The DPO notifies the requesting party that the processing cannot proceed. If a commercial arrangement is being proposed (e.g., use of controller PII for product improvement), this is escalated to the CISO and Legal/Compliance, who advise on whether a contractual amendment with the controller is feasible.
6. **Record the event.** All out-of-scope processing requests and their outcomes are recorded in the Cooperation Request Log (see CLD-IMP-A.2-TG, Section 2), regardless of outcome.

### 1.3 Anonymisation Requests

Where [Organisation] proposes to use aggregated or anonymised data derived from controller PII for service improvement, [Organisation] SHALL:

1. Submit the proposed anonymisation methodology to the DPO in writing.
2. The DPO confirms in writing whether the result constitutes genuine, irreversible anonymisation.
3. If confirmed as genuinely anonymised, the DPO documents the assessment. The derived data set is no longer PII and may be used within the scope confirmed by the DPO.
4. If not confirmed as genuinely anonymised, the data is treated as PII and the out-of-scope processing escalation procedure (above) applies.

---

## Part 2 — Technically Compelled Processing Workflow

### 2.1 Triggers for Legally Compelled Processing

Legally compelled processing occurs when [Organisation] is required by applicable law to process PII in a manner that is not covered by, or conflicts with, the controller's processing instructions. Typical triggers:

- A law enforcement authority presents a lawful order or warrant requiring disclosure of PII
- A regulatory body requires retention of PII beyond the agreed retention period
- A court order requires production of PII as evidence

### 2.2 Procedure — Legally Compelled Processing

When any [Organisation] employee receives a legal demand that may require processing controller PII beyond instructions:

1. **Do not comply immediately.** Route the demand to Legal/Compliance without delay. Do not disclose PII or take any action to comply until Legal/Compliance has reviewed the demand.
2. **Legal/Compliance verifies the demand.** Legal/Compliance confirms the legal basis, jurisdiction, and scope of the demand. If the demand appears procedurally defective, Legal/Compliance challenges it through appropriate legal channels before any processing occurs.
3. **DPO notification.** Legal/Compliance notifies the DPO on the same day the demand is received.
4. **Controller notification assessment.** Legal/Compliance determines whether applicable law permits notification of the PII controller before processing. If permitted:
   - Notify the controller in writing, describing the nature of the legal demand and the PII scope, without disclosing information that would prejudice the legal process.
   - Allow the controller reasonable time (and legal opportunity) to object, if applicable.
5. **If notification is prohibited.** Legal/Compliance documents the legal basis for the prohibition and records the expected date on which the prohibition lapses.
6. **Process minimum necessary PII.** If the legal obligation is confirmed, processing is limited to the minimum PII required by the demand.
7. **Complete the Legally Compelled Processing Record** (see CLD-IMP-A.2-TG, Section 3) covering: demand reference, legal basis, PII categories, controller notification status, and processing outcome.
8. **Post-lapse notification.** When any prohibition on controller notification lapses, the DPO notifies the controller at the earliest opportunity.

---

## Part 3 — Data Subject Rights Cooperation Request Handling

### 3.1 How Controller Cooperation Requests Are Received

PII controllers may submit cooperation requests to [Organisation] when they receive data subject rights requests from their data subjects. Controllers submit these requests through the designated service channel (defined in the processor agreement — typically a secure support ticket system or designated email address).

[Organisation] does not receive data subject rights requests directly from data subjects, unless the service agreement specifically designates [Organisation] as the rights fulfilment point. In all other cases, Cloud Service Delivery redirects any data subjects who contact [Organisation] directly to the relevant PII controller.

### 3.2 Procedure — Handling a Controller Cooperation Request

When a controller cooperation request is received:

1. **Log the request.** Cloud Service Delivery logs the request in the Cooperation Request Log (see CLD-IMP-A.2-TG, Section 2) on receipt, recording: controller identity, data subject right type, date received, PII categories potentially affected, and the controller's required response deadline.
2. **Acknowledge within 1 business day.** Cloud Service Delivery sends a written acknowledgement to the controller confirming receipt and providing an expected completion date.
3. **Determine technical feasibility.** Cloud Service Delivery assesses whether the requested technical action (export, deletion, restriction, portability export, etc.) can be completed within the 5 business day standard timeframe. If a technical constraint prevents this, the controller is notified immediately with a revised timeline.
4. **Execute the request.** Cloud Service Delivery performs the required action using the technical capabilities described in CLD-IMP-A.2-TG, Section 1.
5. **Confirm completion.** Cloud Service Delivery sends written confirmation to the controller confirming the action taken, the date completed, and any relevant technical details (e.g., deletion confirmation, export file reference).
6. **Update the log.** The Cooperation Request Log is updated with the completion date and outcome.

### 3.3 Response Timeframes Summary

| Request Type | Acknowledgement | Standard Completion |
|--------------|-----------------|---------------------|
| Access / Portability export | 1 business day | 5 business days |
| Rectification | 1 business day | 5 business days |
| Erasure | 1 business day | 5 business days |
| Restriction / Objection flag | 1 business day | 2 business days |
| Complex / large-scale requests | 1 business day | Agreed with controller — document in log |

Where the service agreement specifies shorter timeframes, those contractual timeframes take precedence.

### 3.4 Contested or Complex Requests

If Cloud Service Delivery is uncertain whether a cooperation request can be fulfilled (e.g., the requested erasure would conflict with a legal retention obligation), it escalates to the DPO on the same day. The DPO assesses the conflict and provides instruction within 1 business day. Cloud Service Delivery notifies the controller of the outcome and the reason for any limitation on fulfilment.

---

## Evidence Checklist

- [ ] Out-of-scope processing escalation events recorded in the Cooperation Request Log with DPO assessment and outcome
- [ ] No evidence of controller PII processed for [Organisation]'s own marketing, analytics, or commercial purposes without documented controller authorisation
- [ ] Cooperation Request Log in place and current, with all data subject rights requests logged, acknowledged, and completed within timeframes
- [ ] Legally Compelled Processing Records complete for any legally compelled processing events, including controller notification status
- [ ] Technical capability documentation confirming access, erasure, rectification, restriction, portability, and objection capabilities are operational
- [ ] DPO anonymisation assessment records in place for any anonymised data use
- [ ] Processor agreements include A.2.1 cooperation obligation clauses

---

<!-- QA_VERIFIED: [Date] -->
