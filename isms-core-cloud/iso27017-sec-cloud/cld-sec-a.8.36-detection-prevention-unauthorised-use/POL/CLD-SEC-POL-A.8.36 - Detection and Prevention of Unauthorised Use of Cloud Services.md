<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.36:sec:POL:a.8.36 -->
**CLD-SEC-POL-A.8.36 — Detection and Prevention of Unauthorised Use of Cloud Services**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Detection and Prevention of Unauthorised Use of Cloud Services |
| **Document Type** | Policy |
| **Document ID** | CLD-SEC-POL-A.8.36 |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO/IEC 27017:2026 Ed. 2 implementation |

**Review Cycle**: Annual (or upon significant change to cloud usage monitoring capability, or following a confirmed unauthorised use incident)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Cloud Security Manager
- Technical: Security Operations Lead
- Final Authority: Executive Management

**Related Documents**:

- ISMS-POL-A.8.16 (Monitoring Activities — parent ISMS policy)
- CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities within a Cloud Computing Environment)
- CLD-SEC-POL-A.8.35 (Segregation in Virtual Computing Environments)
- CLD-SEC-IMP-A.8.36-TG (Detection and Prevention of Unauthorised Use of Cloud Services — Technical Guide, holds the full monitoring schemas)
- CLD-SEC-REF-A.5-A.8 (Cloud Security Guidance Addendum)
- ISO/IEC 27017:2026, Clause 8.36 (CLD — Detection and prevention of unauthorised use of cloud services)
- ISO/IEC 19086 (all parts) (Cloud computing — Service level agreement framework)

---

## Executive Summary

This policy establishes how [Organisation] monitors cloud service users' (CSUs') activity to detect and prevent unauthorised access, unintended data transfer, and other unauthorised activity on cloud services, in accordance with ISO/IEC 27017:2026, Clause 8.36.

**Scope**: All cloud services [Organisation] manages as a cloud service customer (CSC), including monitoring of [Organisation]'s own cloud service users; and all cloud services [Organisation] delivers as a cloud service provider (CSP), including the monitoring guidance and functions provided to CSCs.

**Extended Control Note**: ISO/IEC 27017:2026, Clause 8.36 is one of four cloud-specific "CLD" extended controls introduced by the standard's second edition (alongside 5.38, 5.39, and 8.35). It is entirely new — it has no equivalent in the 2015 first edition of ISO/IEC 27017 and no direct equivalent in ISO/IEC 27002:2022. [Organisation] implements it as an informative extension to its ISO/IEC 27001:2022-based ISMS, alongside Annex A control 8.16 (Monitoring activities).

**Core Risk**: Cloud services are easy to provision and easy to misuse — a single CSU can create shadow infrastructure, exfiltrate data through an authorised service in an unauthorised way, or exceed their intended access without triggering conventional network-perimeter controls. Detection depends on monitoring usage patterns, not just monitoring for external attack. A confirmed instance of unauthorised cloud service use is treated as an information security incident, escalated and investigated per [Organisation]'s incident management process — not simply logged and closed.

---

# Scope and Applicability

## ISO/IEC 27017:2026 — Clause 8.36

**Control statement (ISO/IEC 27017:2026, 8.36):**
> "The CSUs' use of cloud services should be monitored to prevent unauthorized access, data transfer and other activities on cloud services."

**Purpose (ISO/IEC 27017:2026, 8.36):**
> "To enable monitoring and prevention of unintended use of cloud services and unintended data transfer to and from cloud services."

## Applicability

This policy applies to:

- All cloud service users (CSUs) within [Organisation] who access cloud services on [Organisation]'s behalf, as CSC
- All cloud services [Organisation] delivers to its own CSCs, as CSP, with respect to the monitoring guidance and functions [Organisation] must provide
- All information security event management processes that ingest cloud service usage data

## Regulatory and Standards Framework

ISO/IEC 27017:2026 is an informative extension to ISO/IEC 27002:2022. Clause 8.36 does not correspond to a numbered ISO/IEC 27002:2022 control; it is new in the 2026 second edition, with no equivalent even in the 2015 first edition of ISO/IEC 27017. It is implemented alongside ISO/IEC 27001:2022 Annex A control 8.16 (Monitoring activities), and draws on the SLA guidance in the ISO/IEC 19086 series where cloud SLA terms govern the monitoring data available to [Organisation].

---

# Policy Statements: Detection and Prevention of Unauthorised Cloud Use (8.36)

## Risk-Based Scoping

Before implementing monitoring for a given cloud service, [Organisation] SHALL:

- Confirm the service's data classification (Public / Internal / Confidential / Restricted), using the Segregation Requirements Statement (CLD-SEC-IMP-A.8.35-TG, Section 1) where one already exists for the service
- Apply CSU activity monitoring as a mandatory baseline for cloud services classified Confidential or Restricted
- For services classified Public or Internal, prepare a risk-based recommendation (monitor or not, and why) for CISO approval, and record the decision — monitoring is not skipped by default, it is a documented decision

## Obligations as Cloud Service Customer (CSC)

Where [Organisation] acts as a cloud service customer, [Organisation] SHALL, for every in-scope cloud service:

- Implement monitoring of CSUs' activities, capturing at minimum authentication events, resource provisioning/deprovisioning, data access, and configuration changes, routed to [Organisation]'s central security monitoring capability per ISMS-POL-A.8.16 where feasible
- Perform periodic technical compliance review against [Organisation]'s information security policy, its topic-specific policy on the use of cloud services, and relevant rules and standards — at minimum annually for Confidential or Restricted services — with non-compliant findings escalated to the Cloud Security Manager for remediation tracking
- Monitor and prevent unintended or unauthorised information transfer to and from the cloud service environment [Organisation] manages, using available technical controls (e.g. data loss prevention integration, restricted sharing settings, egress monitoring)
- Establish a baseline of normal cloud service usage per monitored service, and detect anomalies — such as increasing resource utilisation or unknown service usage — by identifying deviations from that baseline
- Investigate every triggered anomaly alert and record its disposition (false positive, confirmed unauthorised use, remediated, escalated to incident response); treat a confirmed unauthorised use finding as an information security incident

## Obligations as Cloud Service Provider (CSP)

Where [Organisation] acts as a cloud service provider, [Organisation] SHALL:

- Provide CSCs with guidance and functions enabling them to monitor and control their CSUs' use of the cloud service [Organisation] delivers — documenting what activity data is exposed, how CSCs can access it, and how any configurable monitoring functions (e.g. custom alert thresholds) are set up
- Keep this CSC-facing monitoring guidance current as the service evolves, reviewing it alongside the annual policy review at minimum

## Communication and Awareness

[Organisation] SHALL communicate monitoring scope, CSU responsibilities, acceptable-use rules, and how to report suspected unauthorised use to internal CSUs and relevant teams, through the organisation's information security awareness programme (see ISMS-POL-A.6.3) and service-specific onboarding materials. Where [Organisation] acts as CSP, the equivalent information SHALL be communicated to customer CSUs through the published CSC-facing monitoring guidance.

## Monitoring Scope Decision Log — Minimum Content

The Monitoring Scope Decision Log (full schema in CLD-SEC-IMP-A.8.36-TG, Section 1) SHALL record, per cloud service: the service identifier; its data classification; the monitoring decision (mandatory, risk-based-implemented, or risk-based-not-implemented); the rationale and, where applicable, the CISO's approval; and the date of last review.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Owns CLD-SEC-POL-A.8.36; approves the risk-based scoping of monitoring for lower-classification cloud services; reviews anomaly escalations with organisation-wide impact; owns confirmed unauthorised-use incidents through [Organisation]'s incident management process |
| **Security Operations Lead** | Implements and operates CSU activity monitoring, technical compliance review, and anomaly detection (CSC role); reports monitoring coverage and anomaly metrics to the CISO |
| **Cloud Security Manager** | Ensures the CSC-facing monitoring guidance and functions are documented and made available where [Organisation] is a CSP; records risk-based scoping decisions |
| **Cloud Service Delivery / Engineering** | Configures cloud service monitoring capabilities; responds to detected unintended or unauthorised information transfer |
| **All Personnel (as CSUs)** | Use cloud services only within authorised scope; report suspected unauthorised use they observe |

---

# Evidence Requirements

| Evidence | Description | Owner | Retention |
|---------|-------------|-------|-----------|
| Monitoring Scope Decision Log | CISO-approved risk-based decisions for Public/Internal services where monitoring is not implemented | Cloud Security Manager | Current + 3 years |
| CSU Activity Monitoring Configuration | Documentation of monitoring scope and mechanisms per cloud service (CSC role) | Security Operations Lead | Current version + previous versions for 3 years |
| Technical Compliance Review Records | Records of periodic reviews against information security policy, cloud usage policy, and standards | Security Operations Lead | Current + 3 years |
| Anomaly Detection Log | Log of detected anomalies (unexpected resource utilisation, unknown service usage) and their disposition | Security Operations Lead | Current + 3 years |
| Confirmed Unauthorised Use / Incident Records | Records of anomalies confirmed as unauthorised use, cross-referenced to the incident management process | CISO | Current + 3 years |
| CSC-Facing Monitoring Guidance (CSP role) | Documentation and functions provided to CSCs to monitor and control their own CSUs' use | Cloud Security Manager | Current version + previous versions for 3 years |

---

# Monitoring and Metrics

The Security Operations Lead reports the following to the CISO at least quarterly:

- Proportion of Confidential/Restricted cloud services with active CSU monitoring
- Number of anomalies detected, and their disposition breakdown (false positive / confirmed unauthorised use / remediated / escalated)
- Number of technical compliance review findings and remediation status
- Time from anomaly detection to disposition, for anomalies confirmed as unauthorised use

---

# Audit Considerations

Auditors verifying compliance with CLD-SEC-POL-A.8.36 should expect to find:

- Documented CSU activity monitoring scope for every cloud service classified as Confidential or Restricted
- Evidence of periodic technical compliance review against information security policy and the cloud usage policy
- An Anomaly Detection Log demonstrating active review and disposition tracking, not just passive log collection
- For services where [Organisation] is a CSP, published monitoring guidance and functions made available to CSCs
- Documented CISO approval where monitoring has been risk-scoped down for lower-classification services
- Evidence that confirmed unauthorised-use findings were handled through [Organisation]'s incident management process, with a record of time-to-disposition

---

<!-- QA_VERIFIED: 2026-08-01 -->
