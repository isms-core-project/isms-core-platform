<!-- ISMS-CORE:IMP:CLD-IMP-A.3-UG:cloud:UG:a.3 -->
**CLD-IMP-A.3-UG — Purpose Legitimacy and Specification — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Purpose Legitimacy and Specification — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.3-UG |
| **Related Policy** | CLD-POL-A.3 (Purpose Legitimacy and Specification) |
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

- CLD-POL-A.3 (Purpose Legitimacy and Specification — the governing policy)
- CLD-IMP-A.3-TG (Purpose Legitimacy and Specification — Technical Guide)
- CLD-POL-A.2 (Consent and Choice)
- CLD-POL-A.4 (Collection Limitation)
- CLD-POL-A.1 (General)

---

## Purpose of This Guide

This guide explains how [Organisation] implements its obligations as a public cloud PII processor under ISO/IEC 27018:2025 Annex A, Controls A.3.1 and A.3.2. It covers three operational areas: how to review controller-specified processing purposes before accepting them in service agreements, how to identify and flag scope creep or purpose drift during service delivery, and what to do when controller instructions appear to be unlawful or cannot be fulfilled within agreed purpose boundaries. It is intended for teams that negotiate, operate, and govern cloud service relationships.

**Who this guide is for**: CISO, DPO, Legal/Compliance, Cloud Service Delivery, Product and Commercial Teams.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. [Organisation] does not determine the legitimacy of the controller's processing purposes — that is the controller's legal responsibility. [Organisation]'s obligation is to ensure it does not process beyond those documented purposes and does not exploit controller PII for its own benefit.

---

## Part 1 — Reviewing Controller-Specified Processing Purposes Before Accepting Service Agreements

### 1.1 Why Pre-Contract Purpose Review Matters

Before [Organisation] accepts a new cloud service engagement involving PII processing, Legal/Compliance and the DPO review the proposed processing purposes. This review is not about judging the controller's legal basis — it is about confirming:

- That [Organisation] can technically deliver the service within the described purposes
- That the proposed processing does not require [Organisation] to act as a data controller (which would trigger entirely different obligations)
- That the proposed processing purposes do not on their face involve [Organisation] in unlawful activity

### 1.2 Pre-Contract Purpose Review Procedure

The pre-contract purpose review is completed using the Purpose Scope Review Checklist (see CLD-IMP-A.3-TG, Section 1). Legal/Compliance initiates the review; the DPO makes the final determination.

**Procedure:**

1. **Receive proposed processing description.** Legal/Compliance receives the controller's proposed processing description — either as a completed schedule or as a description in the draft service agreement.
2. **Complete the Purpose Scope Review Checklist.** Legal/Compliance completes Part A of the checklist (factual mapping). The DPO completes Part B (purpose assessment).
3. **Assess each proposed processing purpose against four criteria:**
   - Is the purpose specific and documented? (A vague purpose such as "data analytics" is insufficient; the specific operations must be described.)
   - Does the purpose require [Organisation] to act as a controller? (If [Organisation] would be making decisions about the means or purposes of processing, this is not a permissible processor arrangement.)
   - Is the purpose facially lawful? (Legal/Compliance flags any purpose that appears to involve processing that would be unlawful in the controller's or [Organisation]'s jurisdiction — e.g., processing of special categories of PII without clear indication of a legal basis.)
   - Can [Organisation] technically deliver within the purpose boundaries? (Cloud Service Delivery confirms that service architecture does not require processing beyond the proposed scope.)
4. **DPO makes determination.** The DPO records the determination in the checklist: Accept / Accept with clarification / Escalate / Decline.
5. **If clarification is required.** Legal/Compliance requests clarification from the controller before the agreement is executed. The clarified processing description is re-reviewed.
6. **If escalation is required.** The DPO and Legal/Compliance escalate to the CISO and, if applicable, external legal counsel. The service agreement is not executed until the concern is resolved.
7. **File the completed checklist.** The completed Purpose Scope Review Checklist is filed with the processor agreement in the Processor Agreement Register.

### 1.3 Operational Telemetry — Purpose Boundary Confirmation

Service telemetry and operational metadata (performance metrics, error logs, access logs) collected during service delivery may incidentally contain PII. Before service commencement, Cloud Service Delivery confirms with the DPO that:

- The telemetry collection is necessary for service delivery within the contracted purpose
- Telemetry retention periods are documented and limited to operational necessity
- Telemetry is not routed to [Organisation]'s internal analytics, product, or commercial systems

This confirmation is recorded in the processing description schedule (see CLD-IMP-A.1-TG, Section 2).

---

## Part 2 — Identifying and Flagging Purpose Drift During Service Delivery

### 2.1 What Is Purpose Drift

Purpose drift occurs when the actual processing of controller PII during service delivery begins to exceed or deviate from the purposes documented in the processor agreement. It may arise from:

- Service architecture changes that introduce new processing operations not covered by the agreement
- Feature development that inadvertently routes controller PII through new system components
- Requests from internal [Organisation] teams to use controller PII for purposes beyond service delivery
- Changes to the controller's use of the service that result in new PII categories being submitted without a corresponding agreement update

### 2.2 Responsibility for Identifying Purpose Drift

Cloud Service Delivery is responsible for identifying purpose drift during day-to-day service operations. Cloud Engineering is responsible for identifying purpose drift during architecture changes and feature development. The CISO is responsible for identifying purpose drift during periodic reviews of service data flows.

Any team member who identifies actual or potential purpose drift SHALL report it to Cloud Service Delivery and the CISO on the same day.

### 2.3 Purpose Drift Escalation Procedure

When potential purpose drift is identified:

1. **Notify the CISO and DPO.** Cloud Service Delivery or Cloud Engineering notifies the CISO and DPO in writing (same business day), describing: the nature of the drift, the PII categories potentially affected, the service component involved, and whether the drift is current or anticipated.
2. **CISO and DPO assess.** Within 2 business days, the CISO and DPO assess whether: (a) the processing falls within existing agreed purposes on a reasonable interpretation; (b) a technical correction is required to bring processing back within scope; or (c) a formal new purpose authorisation is required from the controller.
3. **Technical correction.** If the drift is due to a misconfiguration or unintended routing, Cloud Engineering implements a technical correction. The event is recorded in the Processing Instruction Change Log (see CLD-IMP-A.3-TG, Section 2).
4. **New purpose authorisation.** If the proposed processing genuinely requires a new purpose, Legal/Compliance obtains written controller authorisation before processing continues. See CLD-POL-A.3 for the new purpose authorisation requirements.
5. **Commercial use proposals.** If the purpose drift involves a request from an internal team to use controller PII for [Organisation]'s own commercial benefit, Legal/Compliance and the DPO assess whether this can be proposed to the controller as a contractual amendment. Processing SHALL NOT proceed until explicit written controller authorisation is obtained.

---

## Part 3 — Escalation When Controller Instructions Appear Unlawful

### 3.1 When to Escalate

[Organisation] does not assess the legality of the controller's processing purposes as a routine matter — that is the controller's responsibility. However, [Organisation] must escalate when:

- Controller instructions explicitly require [Organisation] to process PII in a manner that would constitute a breach of applicable law in [Organisation]'s jurisdiction (e.g., instructions to process special categories of PII in a jurisdiction where this is prohibited without explicit consent)
- Instructions require [Organisation] to transfer PII to a jurisdiction without adequate data protection safeguards, in breach of GDPR Chapter V or CH FADP transfer requirements, and without the safeguards required by CLD-POL-A.12
- Instructions appear to require [Organisation] to actively destroy, conceal, or falsify PII in a manner that would constitute an offence

### 3.2 Unlawful Instruction Escalation Procedure

1. **Cloud Service Delivery or Cloud Engineering identifies the concern** and immediately notifies the DPO and Legal/Compliance in writing. Processing of the potentially unlawful instruction is suspended pending assessment.
2. **Legal/Compliance and DPO assess the instructions** within 2 business days. They confirm whether the instruction is: (a) lawful on further analysis; (b) unlawful and incapable of being made lawful; or (c) requires clarification from the controller.
3. **If clarification is sought.** Legal/Compliance contacts the controller, describing the concern without disclosing confidential legal analysis, and requests clarification or revised instructions. Processing of the specific instruction is suspended during this period.
4. **If instructions are confirmed unlawful.** Legal/Compliance and the DPO escalate to the CISO and, if necessary, to executive management. [Organisation] does not comply with the unlawful instruction. Legal/Compliance advises on whether the service agreement must be suspended or terminated.
5. **Record the escalation.** All unlawful instruction escalation events are recorded in the Unlawful Instruction Escalation Record (see CLD-IMP-A.3-TG, Section 3) regardless of outcome.

---

## Evidence Checklist

- [ ] Purpose Scope Review Checklists completed and filed for all active processor agreements
- [ ] Processing description schedules contain specific purpose descriptions — not vague or catch-all purpose statements
- [ ] Processing Instruction Change Log maintained and current, with all purpose drift events recorded
- [ ] No evidence of controller PII routed through [Organisation]'s internal analytics, product, or commercial systems without documented controller authorisation
- [ ] Unlawful Instruction Escalation Records (if applicable) complete with legal basis assessment and resolution
- [ ] DPO sign-off recorded on all new purpose authorisations
- [ ] Service telemetry scope confirmed as within agreed processing purposes for all active services

---

<!-- QA_VERIFIED: [Date] -->
