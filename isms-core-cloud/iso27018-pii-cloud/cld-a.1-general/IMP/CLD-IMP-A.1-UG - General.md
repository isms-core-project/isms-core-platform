<!-- ISMS-CORE:IMP:CLD-IMP-A.1-UG:cloud:UG:a.1 -->
**CLD-IMP-A.1-UG — General — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | General — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.1-UG |
| **Related Policy** | CLD-POL-A.1 (General) |
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

- CLD-POL-A.1 (General — the governing policy)
- CLD-IMP-A.1-TG (General — Technical Guide)
- CLD-POL-A.10 (Accountability)
- CLD-POL-A.11 (Information Security)
- CLD-POL-A.12 (Privacy Compliance)

---

## Purpose of This Guide

This guide explains how [Organisation] implements its obligations as a public cloud PII processor under ISO/IEC 27018:2025 Annex A, Section A.1. It covers how the processor role is documented in contracts, how controller processing instructions are captured and maintained, and how sub-processor consent is managed. It is intended for operational use by teams responsible for establishing and maintaining cloud service relationships with PII controllers.

**Who this guide is for**: CISO, DPO, Legal/Compliance, Cloud Service Delivery, Contract Management.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. [Organisation] processes PII solely under documented controller instructions and does not determine processing purposes or means.

---

## Part 1 — Documenting the Processor Role in Contracts

### 1.1 Establishing the Written Processor Agreement

Every cloud service engagement where [Organisation] will process PII on behalf of a customer (PII controller) SHALL be governed by a written processor agreement before processing commences. The CISO and Legal/Compliance Officer are jointly responsible for ensuring this requirement is met.

**Procedure — establishing a new processor agreement:**

1. **Identify the processing relationship.** When a new customer onboarding request is received, Cloud Service Delivery confirms with the DPO whether the engagement involves PII processing. If yes, a processor agreement is mandatory.
2. **Use the standard processor agreement template.** Legal/Compliance uses the template maintained in the Processor Agreement Register (see CLD-IMP-A.1-TG, Section 1). Custom terms requested by the controller must be reviewed by Legal/Compliance and approved by the DPO before acceptance.
3. **Complete the processing description schedule.** The agreement must include a completed schedule specifying: categories of PII, processing purposes, processing operations, processing duration, and sub-processor arrangements. See CLD-IMP-A.1-TG, Section 2 for the schedule template.
4. **Obtain DPO sign-off.** The DPO reviews the completed processing description schedule for compliance with CLD-POL-A.3 (purpose restriction) and CLD-POL-A.4 (collection limitation) before the agreement is executed.
5. **Register the agreement.** Legal/Compliance adds the executed agreement to the Processor Agreement Register with status, effective date, and next review date.
6. **Distribute to Cloud Service Delivery.** Cloud Service Delivery receives a copy of the processing description schedule and confirms they can deliver the service within the documented scope.

### 1.2 Maintaining the Processor Agreement Register

The Processor Agreement Register is the authoritative record of all active PII controller relationships. Legal/Compliance maintains it; the DPO has oversight.

**Register maintenance obligations:**

- All agreements are reviewed no less than annually, or upon material change to the service or applicable regulatory requirements.
- When a controller notifies [Organisation] of a change to processing requirements, Legal/Compliance assesses whether a formal agreement amendment is required. If yes, the DPO approves before implementation.
- When an agreement expires or terminates, Legal/Compliance records the termination date and confirms with Cloud Service Delivery that PII return or deletion has been completed per CLD-POL-A.11.11.
- The register is made available to the DPO and CISO on demand and to controllers upon written request.

### 1.3 Documenting ISO/IEC 27018:2025 Annex A Control Implementation

CLD-POL-A.1 requires [Organisation] to document how each applicable Annex A control is addressed within its services. This documentation (the Control Implementation Documentation) is the artefact that demonstrates ISO/IEC 27018:2025 compliance to controllers and auditors.

**Procedure — producing and maintaining the Control Implementation Documentation:**

1. The CISO maintains a control mapping document that links each CLD-POL-A.X policy to the service feature, process, or technical control that implements it.
2. The control mapping is reviewed annually by the CISO and DPO and updated to reflect any service architecture changes.
3. On request from a PII controller (typically at contract negotiation or audit time), the CISO produces a controller-facing summary of control implementation. This summary does not expose internal system architecture; it confirms that each control is addressed and describes the method at a level appropriate for contractual assurance.
4. Where a controller requires inclusion of control implementation commitments in the service agreement, Legal/Compliance incorporates the relevant statements as a schedule or annex.

---

## Part 2 — Receiving and Maintaining Controller Processing Instructions

### 2.1 Initial Instructions — Service Commencement

At service commencement, Cloud Service Delivery confirms with the DPO that documented processing instructions have been received from the PII controller. Instructions are defined as:

- The completed processing description schedule (from the processor agreement)
- Any supplementary written instructions provided by the controller (e.g., data handling addenda, configuration specifications)

Processing SHALL NOT commence until the DPO confirms that instructions have been received and are adequate.

### 2.2 Ongoing Instruction Management

Processing instructions may change during the service lifecycle. Cloud Service Delivery is responsible for identifying and escalating changes.

**Procedure — handling a change to controller processing instructions:**

1. **Identify the change.** Cloud Service Delivery identifies a change request — either received in writing from the controller or identified through a proposed service configuration change.
2. **Assess scope.** If the change is within the existing processing description (e.g., a technical parameter change with no new PII categories or purposes), Cloud Service Delivery documents the change in the Instruction Change Log and proceeds.
3. **Escalate if out of scope.** If the change involves new PII categories, new processing purposes, or new sub-processor arrangements, Cloud Service Delivery escalates to the DPO. The DPO determines whether a formal agreement amendment is required (see Part 1).
4. **Record the instruction.** All instruction changes are recorded in the Instruction Change Log (see CLD-IMP-A.1-TG, Section 3) with the date received, the change description, the authorising contact at the controller, and the DPO assessment outcome.

### 2.3 Where Processing is Legally Required Beyond Instructions

Where [Organisation] is legally required to process PII beyond controller instructions (for example, under a law enforcement request or regulatory obligation):

1. Legal/Compliance confirms the legal basis for the requirement.
2. The DPO is notified immediately.
3. Legal/Compliance notifies the PII controller before processing, unless applicable law prohibits notification.
4. Processing is limited to the minimum PII required by the legal obligation.
5. The event is recorded in the Legally Compelled Processing Record (see CLD-IMP-A.1-TG, Section 4).
6. When any prohibition on notification lapses, the DPO ensures the controller is notified at the earliest opportunity.

---

## Part 3 — Sub-Processor Consent and Management

### 3.1 Sub-Processor Approval Requirement

[Organisation] SHALL NOT engage a sub-processor to process controller PII without the prior written consent of the relevant PII controller. This applies to new sub-processor engagements and to material changes to existing sub-processor arrangements.

### 3.2 Requesting Sub-Processor Consent

**Procedure — obtaining sub-processor consent:**

1. **Identify the need.** CISO or Cloud Service Delivery identifies a need to engage a new sub-processor (e.g., a cloud infrastructure provider, backup service, or specialist processing vendor).
2. **Complete sub-processor due diligence.** The DPO and CISO conduct due diligence on the proposed sub-processor, assessing: data protection capability, applicable jurisdiction, certifications (ISO 27001, ISO 27018, SOC 2), and contractual data protection obligations.
3. **Prepare the consent request.** Legal/Compliance prepares a written consent request for the relevant PII controllers, describing the sub-processor's name, location, role, and PII categories it will access.
4. **Obtain written consent.** Consent must be received in writing (email confirmation is acceptable). Controllers are given a reasonable period (typically 30 days) to object. If a controller objects, [Organisation] works with the controller to resolve the concern before proceeding.
5. **Execute sub-processor agreement.** Legal/Compliance executes a sub-processor data processing agreement imposing equivalent data protection obligations on the sub-processor as those [Organisation] owes the controller.
6. **Update the Sub-Processor Register.** Legal/Compliance adds the sub-processor to the register with controller consent records, agreement details, and review date.

### 3.3 Ongoing Sub-Processor Oversight

The CISO reviews sub-processor compliance at least annually. If a sub-processor suffers a security incident or fails to meet its obligations, the CISO notifies the DPO and Legal/Compliance, who assess the impact on controller obligations and initiate appropriate remedial action. Controllers are notified in accordance with CLD-POL-A.11 (Information Security) incident notification obligations.

---

## Evidence Checklist

- [ ] Processor Agreement Register maintained and current, with all active PII controller agreements recorded
- [ ] Processing description schedule completed and DPO-reviewed for each active service agreement
- [ ] Control Implementation Documentation produced and reviewed within the last 12 months
- [ ] Instruction Change Log in place and current, with all instruction change events recorded
- [ ] Sub-Processor Register maintained with controller consent records for each sub-processor
- [ ] Sub-processor data processing agreements executed for all active sub-processors
- [ ] Legally Compelled Processing Records (if applicable) complete with legal basis and controller notification status

---

<!-- QA_VERIFIED: [Date] -->
