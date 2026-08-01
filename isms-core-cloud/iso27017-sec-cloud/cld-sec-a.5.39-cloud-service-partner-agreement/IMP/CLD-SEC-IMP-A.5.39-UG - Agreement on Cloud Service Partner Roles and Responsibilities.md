<!-- ISMS-CORE:IMP:CLD-SEC-IMP-A.5.39-UG:sec:UG:a.5.39 -->
**CLD-SEC-IMP-A.5.39-UG — Agreement on Cloud Service Partner Roles and Responsibilities — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Agreement on Cloud Service Partner Roles and Responsibilities — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-SEC-IMP-A.5.39-UG |
| **Related Policy** | CLD-SEC-POL-A.5.39 (Agreement on the Roles and Responsibilities of the Cloud Service Partner) |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Cloud Security Manager |
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

**Review Cycle**: Annual (or upon onboarding/change of a cloud service partner)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-SEC-POL-A.5.39 (Agreement on the Roles and Responsibilities of the Cloud Service Partner — the governing policy)
- CLD-SEC-IMP-A.5.39-TG (Agreement on Cloud Service Partner Roles and Responsibilities — Technical Guide)
- CLD-SEC-POL-A.5.38 (Shared Roles and Responsibilities within a Cloud Computing Environment)

---

## Purpose of This Guide

This guide explains how [Organisation] classifies, agrees with, and documents the information security roles and responsibilities of cloud service partners (CSNs) under ISO/IEC 27017:2026, Clause 5.39. It is intended for operational use by teams onboarding a new cloud service partner or reviewing an existing one.

**Who this guide is for**: CISO, Cloud Security Manager, Legal/Compliance, Cloud Service Delivery/Engineering.

**What counts as a CSN**: A cloud service partner is any third party whose activities support or are auxiliary to [Organisation]'s CSC role, CSP role, or both — most commonly a cloud service developer, a cloud auditor, or a cloud service broker (per ISO/IEC 22123-3). If a third party is instead delivering [Organisation] its own independent cloud service, treat that relationship under CLD-SEC-IMP-A.5.38-UG (CSP relationship) rather than this guide.

---

## Part 1 — Classifying a Prospective Cloud Service Partner

### 1.1 Determining Whether a Third Party Is a CSN

**Procedure — classifying a new third party:**

1. **Describe the third party's activity.** The Cloud Security Manager documents what the third party will actually do in relation to [Organisation]'s cloud service(s).
2. **Match against the sub-role definitions.** Compare the activity against the three ISO/IEC 22123-3 sub-roles:
   - **Developer** — designs, builds, tests, or maintains components used in the cloud service
   - **Auditor** — independently assesses the cloud service's operation, controls, or compliance
   - **Broker** — manages the use, performance, or delivery of the cloud service, or negotiates CSC/CSP relationships
3. **Record the classification.** If one or more sub-roles apply, the third party is a CSN in scope of CLD-SEC-POL-A.5.39. Record the classification in the CSN Role Register (schema in CLD-SEC-IMP-A.5.39-TG, Section 1).
4. **Check for a dual CSP role.** If the third party will also independently deliver a cloud service to [Organisation] (rather than only supporting an existing CSC/CSP relationship), also apply CLD-SEC-IMP-A.5.38-UG to that portion of the relationship.

### 1.2 Checking Consistency with the Existing Shared Responsibility Allocation

Before agreeing roles and responsibilities with the CSN, the Cloud Security Manager retrieves the Shared Responsibility Matrix (CLD-SEC-IMP-A.5.38-TG, Section 1) for the cloud service relationship the CSN will support, and confirms the proposed CSN responsibilities do not reassign a responsibility away from the CSC or CSP without that party's consent.

---

## Part 2 — Agreeing and Documenting the CSN's Roles

### 2.1 Defining the CSN's Responsibilities

**Procedure — defining and agreeing CSN roles and responsibilities:**

1. **Draft the responsibility statement.** The Cloud Security Manager drafts a specific statement of the information security responsibilities the CSN is expected to assume, tied to its classified sub-role(s).
2. **Route through supplier agreement process.** Legal/Compliance negotiates the agreement per ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements), incorporating the responsibility statement as contract text — not left as an informal understanding.
3. **Obtain sign-off.** The Cloud Security Manager confirms consistency with the Shared Responsibility Matrix (Part 1.2); the CISO approves engagements with information-security-relevant scope.
4. **Register the agreement.** Legal/Compliance adds the executed agreement to the CSN Role Register.

### 2.2 Handling a CSN Whose Scope Changes

**Procedure — material change to an existing CSN's activities:**

1. Cloud Service Delivery/Engineering identifies that a CSN's activity has changed materially from its agreed scope.
2. The Cloud Security Manager re-classifies the CSN's sub-role(s) if needed and reassesses consistency with the current Shared Responsibility Matrix.
3. Legal/Compliance amends the agreement to reflect the updated responsibility statement.
4. The CSN Role Register is updated with the amendment date and revised scope.

---

## Part 3 — Ongoing Oversight

### 3.1 Annual Review

The Cloud Security Manager reviews the CSN Role Register at least annually, confirming each active CSN's classification, agreed responsibilities, and continued consistency with the relevant Shared Responsibility Matrix remain accurate.

### 3.2 Escalation

Where a CSN's actual activity is found to exceed its agreed scope, or a conflict is identified between a CSN agreement and the CSC/CSP shared responsibility allocation, Cloud Service Delivery/Engineering escalates immediately to the Cloud Security Manager, who determines whether the CSN agreement must be amended, the CSN's access restricted, or the CISO engaged for a broader resolution.

---

## Evidence Checklist

- [ ] CSN Role Register maintained and current, with sub-role classification for every active cloud service partner
- [ ] Written agreements in place for all active CSNs, stating agreed information security responsibilities
- [ ] Consistency check against the relevant Shared Responsibility Matrix recorded for every CSN agreement
- [ ] Scope-change amendments recorded where a CSN's activity has materially changed
- [ ] Annual CSN Role Register review completed within the last 12 months

---

<!-- QA_VERIFIED: 2026-08-01 -->
