<!-- ISMS-CORE:IMP:PRIV-IMP-A.2.5.2-6-UG:privacy:UG:a.2.5.2-6 -->
**PRIV-IMP-A.2.5.2-6-UG — Transfer and Disclosure (Processor) — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Transfer and Disclosure (Processor) — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.2.5.2-6-UG |
| **Related Policy** | PRIV-POL-A.2.5.2-6 (Transfer and Disclosure (Processor)) |
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

- PRIV-POL-A.2.5.2-6 (Transfer and Disclosure (Processor) — the governing policy)
- PRIV-IMP-A.2.5.2-6-TG (Transfer and Disclosure (Processor) — Technical Guide)
- PRIV-POL-A.2.5.7-9 (Sub-processor Management — sub-processor transfer documentation)

---

## Purpose of This Guide

This guide explains **how to implement** the transfer and disclosure obligations of PRIV-POL-A.2.5.2-6 from the processor perspective. It covers how to inform customers of transfer basis and changes, how to maintain the Transfer Destination Register, how to record disclosures, and how to handle legally binding and non-binding disclosure requests.

**Who this guide is for**: DPO, Legal/Compliance, Customer Success.

**Processor-only**: This guide applies to processing activities where [Organisation] acts as PII Processor on behalf of customer controllers.

---

## Part 1 — Transfer Basis and Customer Notification (A.2.5.2)

### 1.1 Documenting Transfer Basis in Processor Agreements

The legal basis for each cross-border transfer of customer PII must be documented before processing begins. For each processor engagement:

1. The DPO identifies all transfer destinations involved in delivering the service — data centre locations, sub-processor jurisdictions, support team locations with PII access
2. The transfer mechanism for each destination is determined (adequacy decision, SCCs, BCRs)
3. The transfer basis is documented in the processor agreement's data processing schedule or appendix — not just orally communicated

**Transfer mechanism selection for processors**:
- **Adequacy countries**: No additional mechanism needed — adequacy covers the transfer
- **Non-adequate countries via SCCs**: The appropriate SCC module must be incorporated:
  - Module 3: Processor-to-processor (from [Organisation] as processor to a sub-processor)
  - Module 2: Controller-to-processor (if needed for reference to the upstream customer-to-[Organisation] relationship)
- The DPO confirms the correct module and ensures the SCC wording is incorporated into the relevant agreement

### 1.2 Notifying Customers of Transfer Changes

When [Organisation] intends to change a transfer basis or add a new transfer destination, customers must be notified in advance:

1. The DPO identifies the planned change — new sub-processor in a different jurisdiction, data centre migration, adequacy status change affecting an existing destination
2. Customer notifications are drafted by the DPO and sent via Customer Success to each affected customer's data protection or legal contact
3. The notification includes:
   - Description of the change
   - New destination country / jurisdiction
   - Transfer mechanism to be used
   - Effective date of the change
   - How the customer can object or terminate if they do not accept the change
4. The notification period is per the processor agreement (minimum 30 days unless urgent)
5. If a customer objects, Customer Success and DPO assess whether alternative arrangements can accommodate the customer — if not, termination rights per the processor agreement apply
6. All notifications and responses are logged in the Transfer Change Notification Log (see TG)

---

## Part 2 — Transfer Destination Register (A.2.5.3)

### 2.1 What the Register Contains

The DPO maintains a Transfer Destination Register listing all countries and international organisations to which customer PII may possibly be transferred. This register is:

- Made available to customers as part of the processor agreement documentation
- Published or updated at minimum annually and on any change
- Disclosed proactively — customers do not need to ask separately

### 2.2 Maintaining the Register

Triggers for register updates:

| Trigger | Action |
|---------|--------|
| New sub-processor engagement in a new jurisdiction | Add destination; notify customers per A.2.5.2 |
| Sub-processor changes its data centre country | Update destination; notify customers |
| EU Commission withdraws adequacy decision for a destination | Update mechanism; notify customers; arrange SCCs |
| Service infrastructure migration to different region | Update destination; notify customers |
| Annual review | Confirm all entries are current and accurate |

The register must reflect all *possible* transfer destinations, not just those currently active — including DR/failover regions where PII might be processed in a contingency.

---

## Part 3 — Recording Disclosures (A.2.5.4)

### 3.1 What Constitutes a Disclosure by the Processor

A disclosure in the processor context is any communication of customer PII to a third party by [Organisation] in the course of processing. This includes:

- Transfers to sub-processors (routine — see PRIV-POL-A.2.5.7-9)
- Disclosures to regulators or law enforcement under legal obligation
- Disclosures to professional advisors engaged by [Organisation] (legal, audit) where they access customer PII
- Disclosures to the customer itself (data returns, reports)

Disclosures to sub-processors are recorded in the Sub-processor Register. All other disclosures are recorded in the Processor Disclosure Register.

### 3.2 Recording Procedure

When a disclosure of customer PII to a third party occurs:

1. The person making or arranging the disclosure notifies the DPO
2. DPO creates a Processor Disclosure Register entry (see TG for schema)
3. The entry records: date, recipient, PII categories, customer, basis, and whether the customer was notified
4. For legally mandated disclosures, the legal authority reference is recorded; for contractually authorised disclosures, the agreement reference is recorded

---

## Part 4 — Handling Disclosure Requests (A.2.5.5 and A.2.5.6)

### 4.1 Types of Disclosure Requests

[Organisation] may receive requests for customer PII from external parties. These fall into three categories:

| Category | Description | [Organisation]'s Response |
|----------|-------------|---------------------------|
| **Legally binding** | Court order, statutory access power, regulatory demand with legal force | Follow process in Section 4.2 |
| **Non-legally-binding** | Informal law enforcement request, speculative demand, request without legal authority | Reject (Section 4.3) |
| **Contractually authorised** | Customer has explicitly authorised [Organisation] to respond to certain requests (e.g., specific regulator) | Accept and act per authorisation (Section 4.4) |

### 4.2 Handling Legally Binding Requests

When a legally binding request for customer PII is received:

1. **Immediate escalation**: The request is forwarded to the DPO and Legal/Compliance within 1 business day
2. **Legal assessment**: Legal/Compliance confirms whether the request is genuinely legally binding — who issued it, what legal authority is cited, whether it covers [Organisation] as processor
3. **Customer notification**: The DPO notifies the affected customer(s) without undue delay, providing: the nature of the request, the legal authority cited, the PII categories requested, and the disclosure [Organisation] intends to make — unless notification is legally prohibited (non-disclosure order)
4. **Scope limitation**: Legal/Compliance and DPO assess whether the scope of the request can be challenged or limited — [Organisation] discloses only the minimum PII necessary to comply
5. **Execution**: Disclosure is made only after customer notification (or if legally prohibited notification, after confirming with Legal that disclosure cannot be deferred)
6. **Record**: Disclosure is recorded in the Processor Disclosure Register; notification to customer is recorded in the Legally Binding Disclosure Request Log (see TG)

**If notification is legally prohibited**: Legal/Compliance documents the legal basis for the prohibition. The DPO seeks legal advice on whether the prohibition can be challenged. The customer is notified as soon as the prohibition is lifted.

### 4.3 Rejecting Non-Legally-Binding Requests

If a request for customer PII does not have clear legal authority:

1. Do not provide any PII pending Legal/Compliance assessment
2. Legal/Compliance confirms the request is not legally binding
3. The DPO sends a written refusal to the requesting party, stating that [Organisation] processes PII on behalf of customer controllers and cannot disclose without legal obligation or customer authorisation
4. The refusal is documented in the Legally Binding Disclosure Request Log
5. The customer is informed that a request was received and refused

### 4.4 Contractually Authorised Disclosures

If the customer's processor agreement explicitly authorises [Organisation] to disclose PII to specific recipients (e.g., the customer's auditors, a named regulator):

1. Verify the request aligns with the specific authorisation in the processor agreement
2. Execute the disclosure per the contractual authorisation
3. Record in the Processor Disclosure Register
4. Notify the customer of the disclosure (unless the agreement specifies otherwise)

---

## Evidence Checklist

- [ ] Transfer Destination Register — current list of transfer destinations in all processor agreements
- [ ] Transfer Change Notification Log — advance notifications sent for all transfer changes; customer responses recorded
- [ ] Processor Disclosure Register — all third-party disclosures of customer PII recorded
- [ ] Legally Binding Disclosure Request Log — all requests received, assessments, customer notifications, disclosures
- [ ] Non-legally-binding refusals — refusal records for non-binding requests
- [ ] Legal/Compliance assessment records — confirmation of legally binding status for each request
- [ ] SCC documentation — correct module in place for all non-adequate country transfers

---

<!-- QA_VERIFIED: [Date] -->
