<!-- ISMS-CORE:IMP:CLD-IMP-A.4-UG:cloud:UG:a.4 -->
**CLD-IMP-A.4-UG — Collection Limitation — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Collection Limitation — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.4-UG |
| **Related Policy** | CLD-POL-A.4 (Collection Limitation) |
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

- CLD-POL-A.4 (Collection Limitation — the governing policy)
- CLD-IMP-A.4-TG (Collection Limitation — Technical Guide)
- CLD-POL-A.3 (Purpose Legitimacy and Specification)
- CLD-POL-A.5 (Data Minimisation)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation)

---

## Purpose of This Guide

This guide explains how [Organisation] implements its obligations as a public cloud PII processor under ISO/IEC 27018:2025 Annex A, Section A.4. It covers three operational areas: how to configure data collection scopes per controller instructions and service design principles, how to review and reduce the collection footprint of existing services, and how to handle situations where service design or controller submissions result in more PII being collected than instructed or necessary. It is intended for teams that design, operate, and govern cloud services.

**Who this guide is for**: CISO, DPO, Cloud Service Delivery, Cloud Engineering, Legal/Compliance.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. Collection limitation obligations here concern the PII that [Organisation] collects, receives, or processes during service delivery — not the PII that the controller collects from data subjects (which is the controller's responsibility).

---

## Part 1 — Configuring Data Collection Scopes Per Controller Instructions

### 1.1 Establishing the Collection Scope at Service Commencement

Before a cloud service commences processing PII, the CISO and Cloud Service Delivery establish the permitted collection scope for that service. The collection scope is the authoritative definition of which PII categories [Organisation] may collect or receive in the course of delivering the service.

**Procedure — establishing collection scope:**

1. **Review the processing description schedule.** Cloud Service Delivery reviews the processing description schedule (from the processor agreement, see CLD-IMP-A.1-TG, Section 2). The PII categories listed in Section A of the schedule define the maximum permitted collection scope.
2. **Map collection scope to service components.** Cloud Engineering completes the Collection Scope Configuration Checklist (see CLD-IMP-A.4-TG, Section 1) for the service, identifying which system components, APIs, log streams, and storage locations will receive or hold each PII category.
3. **Minimise collection in service configuration.** Cloud Engineering reviews each collection point and confirms that collection is limited to what is technically necessary to deliver the contracted service. Any collection point that cannot be justified operationally is disabled or reconfigured before service commencement.
4. **DPO confirmation.** The DPO reviews the completed Collection Scope Configuration Checklist and confirms that the documented collection scope aligns with the processing description schedule. The DPO's confirmation is recorded in the checklist.
5. **Baseline the collection scope.** The signed-off checklist is filed with the processor agreement as the baseline collection scope record. Any subsequent changes to collection scope require a new checklist to be completed and DPO-reviewed.

### 1.2 Log and Telemetry Collection

Operational logs and service telemetry frequently contain PII incidentally (e.g., user identifiers, IP addresses, session tokens in application logs). Cloud Engineering configures log collection to minimise PII content:

- Application logs SHALL NOT include free-form PII fields (e.g., names, email addresses) unless operationally necessary for support or incident response within the contracted service scope.
- Where log fields contain PII, log retention SHALL be limited to the minimum period operationally necessary (documented in the collection scope checklist).
- Log aggregation pipelines SHALL NOT route PII-containing log streams to [Organisation]'s internal analytics, product monitoring, or commercial intelligence systems.

The CISO reviews log configuration at least annually and upon any material change to the log pipeline.

### 1.3 Development, Test, and Staging Environment Controls

PII from production environments SHALL NOT be used in development, testing, or staging environments without explicit written controller authorisation. Cloud Engineering enforces this through:

1. **Environment separation controls.** Production PII databases are access-controlled separately from non-production environments. Non-production database instances are provisioned with synthetic or anonymised data by default.
2. **Code review gate.** Any deployment pipeline that moves data from production to non-production environments requires CISO and DPO approval before execution.
3. **Authorisation record.** Where a controller provides written authorisation for production PII to be used in a non-production environment, Cloud Service Delivery records the authorisation in the Development/Test Authorisation Register (see CLD-IMP-A.4-TG, Section 3) and confirms with Cloud Engineering that equivalent security controls are applied.

---

## Part 2 — Reviewing and Reducing the Collection Footprint

### 2.1 Annual Collection Footprint Review

The CISO initiates an annual collection footprint review for each active cloud service. The purpose is to identify opportunities to reduce PII collection without impacting service delivery.

**Review procedure:**

1. **Refresh the Collection Scope Configuration Checklist.** Cloud Engineering updates the checklist to reflect the current service state, including any architecture changes made during the year.
2. **Data flow mapping.** Cloud Engineering produces or updates the data flow map for the service (see CLD-IMP-A.4-TG, Section 2), tracing the path of each PII category from collection point through processing to storage and deletion.
3. **Collection reduction assessment.** For each PII collection point, Cloud Engineering assesses: (a) Is this collection still operationally necessary? (b) Can the collection be replaced with a pseudonym or anonymous identifier? (c) Can the retention period be reduced?
4. **Identify reduction opportunities.** Cloud Engineering and the CISO agree a list of actionable collection reduction measures, with implementation timelines.
5. **DPO review.** The DPO reviews the updated checklist and data flow map, and signs off the annual review.
6. **File the review record.** The completed annual review (including DPO sign-off) is filed as an Annual Review Record (see CLD-IMP-A.4-TG, Section 1, Annual Review tab).

### 2.2 Collection Review Triggered by Architecture Changes

When a service architecture change is proposed (new feature, infrastructure migration, third-party integration), Cloud Engineering completes a collection impact assessment before implementation:

1. Does the change introduce any new PII collection points?
2. Does the change increase the volume or categories of PII collected beyond the current collection scope?
3. Does the change route PII to new system components, including sub-processors?

If the answer to any of these questions is yes, Cloud Engineering escalates to the CISO and DPO before the change is implemented. The DPO confirms whether the change requires a processing description schedule update and controller notification.

---

## Part 3 — Handling Excess PII

### 3.1 What Constitutes Excess PII

Excess PII is any PII that [Organisation] receives, stores, or otherwise obtains during service delivery that falls outside the collection scope defined in the processing description schedule. Typical causes:

- A controller uploads a data set containing PII categories that exceed the agreed service scope (e.g., uploading a file that includes financial data when the service is scoped for contact information only)
- A system integration or API call returns more PII fields than the service requires
- A service configuration change inadvertently captures additional PII categories in logs or telemetry

### 3.2 Identifying Excess PII

Cloud Service Delivery and Cloud Engineering are responsible for identifying excess PII through:

- Reviewing data ingestion points against the collection scope baseline when new controller data loads are received
- Automated data classification tooling (where deployed) that flags PII categories not on the approved list
- Periodic data flow reviews (see Part 2)

Any team member who identifies potential excess PII SHALL notify the CISO and DPO on the same business day.

### 3.3 Excess PII Response Procedure

When excess PII is identified:

1. **Isolate the excess PII.** Cloud Engineering isolates the excess PII from active processing where technically feasible (e.g., moving it to a restricted quarantine area). Processing of the excess PII SHALL stop until the DPO has assessed the situation.
2. **Notify the CISO and DPO.** Notification is made on the day of identification. The notification describes: the nature of the excess PII, the volume affected, the system components involved, and how the excess PII entered the service.
3. **DPO assessment.** The DPO assesses within 1 business day whether the excess PII constitutes a personal data breach requiring notification under CLD-POL-A.11. If it does, the breach notification procedure takes priority.
4. **Notify the PII controller.** Within 2 business days of identification (or as soon as the DPO confirms no breach notification is needed), Cloud Service Delivery notifies the relevant PII controller of the excess PII event.
5. **Agree action with the controller.** Cloud Service Delivery and the controller agree whether the excess PII will be: (a) returned to the controller securely; or (b) securely deleted by [Organisation]. Agreement is recorded in writing.
6. **Execute the agreed action.** Cloud Engineering implements the return or deletion within the timeframe agreed with the controller.
7. **Document the event.** The event, controller notification, agreed action, and completion are recorded in the Excess PII Event Record (see CLD-IMP-A.4-TG, Section 3).
8. **Root cause review.** The CISO and Cloud Engineering conduct a root cause review to identify how the excess collection occurred and implement preventive measures.

---

## Evidence Checklist

- [ ] Collection Scope Configuration Checklists completed, DPO-reviewed, and current for all active cloud services
- [ ] Annual collection footprint reviews completed and signed off by DPO within the last 12 months
- [ ] Data flow maps maintained and current for all active cloud services, reflecting current architecture
- [ ] No PII categories in production systems that exceed the documented collection scope
- [ ] Excess PII Event Records complete (if applicable), including controller notification and resolution documentation
- [ ] Development/Test Authorisation Records in place for any use of production PII in non-production environments
- [ ] Log configuration review completed, confirming PII-containing logs are not routed to internal analytics or commercial systems

---

<!-- QA_VERIFIED: [Date] -->
