<!-- ISMS-CORE:IMP:CLD-IMP-A.6-UG:cloud:UG:a.6 -->
**CLD-IMP-A.6-UG — Use, Retention and Disclosure Limitation — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Use, Retention and Disclosure Limitation — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.6-UG |
| **Related Policy** | CLD-POL-A.6 (Use, Retention and Disclosure Limitation) |
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

- CLD-POL-A.6 (Use, Retention and Disclosure Limitation — the governing policy)
- CLD-IMP-A.6-TG (Use, Retention and Disclosure Limitation — Technical Guide)
- CLD-POL-A.3 (Purpose Legitimacy — authorised processing purposes per service agreement)
- CLD-POL-A.10 (Accountability — return and disposal of PII on contract termination)
- CLD-POL-A.5 (Data Minimisation — retention limits for temporary files)

---

## Purpose of This Guide

This guide explains how [Organisation] manages use limitation, retention enforcement, and legally compelled disclosure of PII held on behalf of PII controllers. It covers the step-by-step procedure for handling legally compelled disclosure requests, how to manage notification prohibitions (gag orders), and how to maintain and review the PII Disclosure Register.

**Who this guide is for**: DPO, Legal/Compliance Officer, CISO, Cloud Service Delivery.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. [Organisation] processes PII only on documented controller instruction. Legally compelled disclosures represent a direct conflict between processor obligations and regulatory demands; the procedures in this guide ensure both compliance with legal orders and maximum transparency to controllers.

---

## Part 1 — Retention Enforcement

### 1.1 Establishing Retention Periods

Retention periods for controller PII are set by the PII controller's instructions, documented in the service agreement or data processing agreement (DPA). Cloud Service Delivery is responsible for confirming the agreed retention period with each controller during onboarding and recording it in the service configuration.

Where a service agreement does not specify a retention period, Cloud Service Delivery SHALL request explicit written instruction from the controller before any retention configuration is applied. [Organisation] SHALL NOT apply a default retention period without controller instruction.

### 1.2 Implementing Automated Retention

Cloud Engineering implements automated retention enforcement as the standard mechanism. Manual deletion is only permitted where automation is technically not feasible, in which case the manual process is documented, and Cloud Engineering reviews it quarterly.

Automated retention configuration settings per controller are recorded in the Retention Configuration Record (see CLD-IMP-A.6-TG). Cloud Service Delivery confirms configuration to the controller in writing following onboarding.

---

## Part 2 — Legally Compelled Disclosure: Step-by-Step Procedure

### 2.1 Step 1 — Receive and Acknowledge the Order

When [Organisation] receives a disclosure request from a law enforcement agency, regulatory authority, court, or other governmental body:

1. The recipient (any [Organisation] employee or officer) immediately forwards the order to the **DPO** and the **Legal/Compliance Officer** without responding
2. The DPO opens a disclosure assessment record in the PII Disclosure Register (status: Under Assessment)
3. Legal/Compliance acknowledges receipt to the requesting authority within the timeframe specified in the order (or within 1 business day if no timeframe is specified)

### 2.2 Step 2 — Assess the Legal Validity of the Order

Legal/Compliance assesses whether the order is:

- Issued by an authority with jurisdiction over [Organisation]
- Legally binding (not a voluntary request disguised as mandatory)
- Specific in scope — identifies the PII categories and controller(s) affected
- Within applicable legal authority (e.g., not broader than the stated statutory power permits)

If the order is assessed as invalid or excessively broad, Legal/Compliance advises the DPO on grounds for challenge and drafts a response to the requesting authority. Orders assessed as invalid are not processed until legal challenge is resolved or the order is confirmed by a court.

### 2.3 Step 3 — Notify the PII Controller (Prior Notification)

Before processing any disclosure, the DPO SHALL notify the affected PII controller(s). Notification includes:

1. The identity of the requesting authority (to the extent legally permissible)
2. The categories and scope of PII requested
3. The legal basis cited in the order
4. The deadline by which disclosure is required

Notification is sent via the controller's designated data protection contact (as recorded in the service agreement). Cloud Service Delivery confirms receipt of notification.

The controller is given reasonable time to seek legal challenge or injunctive relief. Where the disclosure deadline does not permit a response window, the controller is notified simultaneously with disclosure (see step 5).

### 2.4 Step 4 — Determine Scope of Minimum Disclosure

Legal/Compliance and the CISO determine the minimum PII required to satisfy the legal order. [Organisation] SHALL NOT provide broader access or additional data sets than specifically required by the order.

Cloud Engineering prepares the disclosure dataset scoped to the minimum required. The DPO confirms the scope before extraction.

### 2.5 Step 5 — Process the Disclosure

The DPO authorises the disclosure after confirming:

- Prior notification to the controller has been given (or simultaneous notification is in progress)
- Scope has been limited to the minimum required
- Legal/Compliance has confirmed the order is valid

Cloud Engineering or Cloud Service Delivery executes the disclosure to the requesting authority. The method of transfer is documented (e.g., secure portal, encrypted email, physical media with chain of custody).

### 2.6 Step 6 — Complete the Disclosure Register Entry

The DPO completes the PII Disclosure Register entry (see CLD-IMP-A.6-TG for schema), recording all mandatory fields. The register entry is closed as complete once all post-disclosure notifications to the controller are confirmed.

---

## Part 3 — Notification Prohibitions (Gag Orders)

### 3.1 When Notification Is Prohibited by Law

Where the legal order prohibits [Organisation] from notifying the PII controller (e.g., a gag order accompanying a law enforcement demand):

1. Legal/Compliance confirms the prohibition in writing, citing the specific legal provision
2. The DPO documents the prohibition in the PII Disclosure Register with the date from which notification is restricted
3. [Organisation] processes the disclosure without prior controller notification
4. The DPO monitors the legal prohibition for lapse — either a defined expiry date in the order, or a court ruling lifting the prohibition

### 3.2 Notification at the Earliest Opportunity

When the legal prohibition lapses, the DPO SHALL notify the affected PII controller without undue delay. Notification follows the same content requirements as prior notification (authority identity, PII scope, legal basis, date of disclosure).

The lapse date and date of subsequent controller notification are recorded in the PII Disclosure Register.

### 3.3 Ongoing or Permanent Prohibitions and Warrant Canary

Where [Organisation] is permanently prohibited from notifying a controller (e.g., an ongoing national security order with no expiry), the DPO escalates to Executive Management. [Organisation] publishes a transparency report or maintains a **warrant canary** to the maximum extent legally permissible.

The warrant canary is a published statement affirming that [Organisation] has not received any orders of a type that would be prohibited from disclosure. Removal or non-renewal of the canary serves as an indirect signal. The warrant canary process and template are maintained in CLD-IMP-A.6-TG.

### 3.4 Quarterly DPO Review

The DPO reviews the PII Disclosure Register quarterly. Open entries with active notification prohibitions are reviewed to determine whether the prohibition has lapsed and notification to the controller is now due.

---

## Evidence Checklist

- [ ] PII Disclosure Register — complete, current, all mandatory fields populated
- [ ] Controller notification records — evidence of prior notification (or prohibited notification documentation) for each disclosure
- [ ] Legal Prohibition Documentation — records of gag orders, dates, and lapse tracking
- [ ] Retention Configuration Records — automated retention settings per controller, confirmed in writing
- [ ] Warrant canary publication — timestamped copies at each version
- [ ] Legal validity assessment records — Legal/Compliance assessment for each disclosure order received
- [ ] Quarterly DPO review sign-off — documented quarterly review of open disclosure register entries

---

<!-- QA_VERIFIED: [Date] -->
