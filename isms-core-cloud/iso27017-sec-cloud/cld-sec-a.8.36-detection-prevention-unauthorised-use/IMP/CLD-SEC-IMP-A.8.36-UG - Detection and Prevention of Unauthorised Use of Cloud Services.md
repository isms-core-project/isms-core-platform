<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.8.36-UG:sec:UG:a.8.36 -->
**CLD-SEC-IMP-A.8.36-UG — Detection and Prevention of Unauthorised Use of Cloud Services — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Detection and Prevention of Unauthorised Use of Cloud Services — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-SEC-IMP-A.8.36-UG |
| **Related Policy** | CLD-SEC-POL-A.8.36 (Detection and Prevention of Unauthorised Use of Cloud Services) |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Security Operations Lead |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial user guide for ISO/IEC 27017:2026 Ed. 2 implementation |

**Review Cycle**: Annual (or upon significant change to cloud usage monitoring capability)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-SEC-POL-A.8.36 (Detection and Prevention of Unauthorised Use of Cloud Services — the governing policy)
- CLD-SEC-IMP-A.8.36-TG (Detection and Prevention of Unauthorised Use of Cloud Services — Technical Guide)
- CLD-SEC-POL-A.8.35 (Segregation in Virtual Computing Environments)

---

## Purpose of This Guide

This guide explains how [Organisation] monitors cloud service user (CSU) activity to detect and prevent unauthorised access, unintended data transfer, and other unauthorised cloud service activity under ISO/IEC 27017:2026, Clause 8.36. It is intended for operational use by Security Operations and Cloud Service Delivery teams.

**Who this guide is for**: CISO, Security Operations Lead, Cloud Security Manager, Cloud Service Delivery/Engineering.

---

## Part 1 — Scoping Monitoring by Risk (CSC Role)

### 1.1 Determining Mandatory vs Risk-Based Scope

**Procedure — scoping CSU activity monitoring for a cloud service:**

1. **Classify the service's data.** The Cloud Security Manager confirms the data classification (Public / Internal / Confidential / Restricted) of the cloud service, using the Segregation Requirements Statement (CLD-SEC-IMP-A.8.35-TG, Section 1) where one already exists for the service.
2. **Apply the baseline.** For Confidential or Restricted services, CSU activity monitoring is mandatory — proceed to Part 2.
3. **Assess risk for lower classifications.** For Public or Internal services, the Security Operations Lead prepares a risk-based recommendation (monitor / don't monitor, and why) for CISO approval. Record the decision in the Monitoring Scope Decision Log (CLD-SEC-IMP-A.8.36-TG, Section 1).

---

## Part 2 — Implementing CSU Activity Monitoring (CSC Role)

### 2.1 Monitoring CSU Activities

**Procedure — implementing CSU activity monitoring:**

1. **Identify monitoring sources.** The Security Operations Lead identifies available monitoring sources for the cloud service — CSP-native activity logs (e.g. cloud provider audit logs), cloud access security broker (CASB) tooling, or SIEM integration.
2. **Configure activity logging.** Ensure logging captures, at minimum: authentication events, resource provisioning/deprovisioning, data access, and configuration changes.
3. **Route to central monitoring.** Where feasible, route cloud service activity logs into [Organisation]'s central security monitoring capability per ISMS-POL-A.8.16 (Monitoring Activities).

### 2.2 Periodic Technical Compliance Review

**Procedure — technical compliance review:**

1. On a schedule set by service risk classification (at minimum annually for Confidential/Restricted services), the Security Operations Lead reviews CSU activity against:
   - [Organisation]'s information security policy
   - [Organisation]'s topic-specific policy on the use of cloud services
   - Relevant external rules and standards applicable to the service
2. Findings are recorded in the Technical Compliance Review Record (CLD-SEC-IMP-A.8.36-TG, Section 2).
3. Non-compliant findings are escalated to the Cloud Security Manager for remediation tracking.

### 2.3 Monitoring and Preventing Unintended Information Transfer

**Procedure — preventing unintended or unauthorised data transfer:**

1. Identify the data transfer paths available within the cloud service environment [Organisation] manages (uploads, downloads, API-based transfers, cross-service sharing).
2. Where technically available, implement controls to detect or prevent transfers outside authorized boundaries (e.g. data loss prevention integration, restricted sharing settings, egress monitoring).
3. Log detected unintended or unauthorised transfer attempts in the Anomaly Detection Log (CLD-SEC-IMP-A.8.36-TG, Section 3).

### 2.4 Detecting Anomalies

**Procedure — anomaly detection:**

1. Establish a baseline of normal cloud service usage (typical resource utilisation, typical service usage patterns) for each monitored service.
2. Configure alerting for deviations from baseline — for example, unexpected spikes in resource utilisation, or use of cloud services not previously authorized for the organisation ("unknown service usage" / shadow IT indicators).
3. Investigate and record each triggered alert in the Anomaly Detection Log, including disposition (false positive, confirmed unauthorised use, remediated).

---

## Part 3 — Providing Monitoring Guidance to CSCs (CSP Role)

### 3.1 Publishing Monitoring Guidance and Functions

Where [Organisation] delivers a cloud service to its own CSCs, the Cloud Security Manager ensures the service provides CSCs with guidance and functions to monitor and control their own CSUs' use of the service — for example, activity logs accessible to the CSC, configurable alerting, or documentation on how to interpret usage data.

**Procedure — publishing CSC-facing monitoring guidance:**

1. Identify what CSU activity data the service technically exposes to CSCs.
2. Document how CSCs can access and interpret this data.
3. Where the service provides configurable monitoring functions (e.g. CSC-defined alert thresholds), document how to configure them.
4. Publish the guidance in the CSC-Facing Monitoring Guidance document (CLD-SEC-IMP-A.8.36-TG, Section 4) and keep it current as the service evolves.

---

## Evidence Checklist

- [ ] Monitoring Scope Decision recorded and CISO-approved for every Public/Internal cloud service where monitoring is not implemented
- [ ] CSU activity monitoring implemented for every Confidential/Restricted cloud service
- [ ] Technical Compliance Review Records current, at minimum annually, for monitored services
- [ ] Anomaly Detection Log maintained with disposition recorded for every triggered alert
- [ ] CSC-Facing Monitoring Guidance published and current for every cloud service [Organisation] delivers as CSP

---

<!-- QA_VERIFIED: 2026-08-01 -->
