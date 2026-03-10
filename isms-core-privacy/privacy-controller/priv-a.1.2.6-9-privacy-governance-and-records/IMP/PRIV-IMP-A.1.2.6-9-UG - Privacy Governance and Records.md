<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.2.6-9-UG:privacy:UG:a.1.2.6-9 -->
**PRIV-IMP-A.1.2.6-9-UG — Privacy Governance and Records — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Governance and Records — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.2.6-9-UG |
| **Related Policy** | PRIV-POL-A.1.2.6-9 (Privacy Governance and Records) |
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

- PRIV-POL-A.1.2.6-9 (Privacy Governance and Records — the governing policy)
- PRIV-IMP-A.1.2.6-9-TG (Privacy Governance and Records — Technical Guide)
- PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent — lawful basis documentation in RoPA)
- PRIV-POL-A.3.13-16 (Compliance, Audit and Review — records protection requirements)

---

## Purpose of This Guide

This guide explains **how to implement** the DPIA, processor contract, joint controller, and records management requirements of PRIV-POL-A.1.2.6-9. It covers how to conduct DPIA screenings and full DPIAs, how to commission and review processor agreements, how to establish joint controller arrangements, and how to build and maintain the RoPA.

**Who this guide is for**: DPO, Legal/Compliance, Data Owners, Procurement.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Privacy Impact Assessment / DPIA (A.1.2.6)

### 1.1 When to Trigger DPIA Screening

A DPIA screening must be triggered before commencing any new PII processing or materially changing existing processing. **Responsibility**: Data Owner identifies the need and notifies the DPO. The DPO conducts the screening.

**Triggers for DPIA screening**:
- Any new product feature, service, or business process that involves PII
- A significant change to how existing PII is processed (new purposes, new data categories, new technology, new recipient categories)
- Engagement of a new processor or change to processor scope
- Changes to international transfer mechanisms or destinations
- Response to a supervisory authority guidance that identifies new risk

### 1.2 DPIA Screening Process

The DPO conducts a screening within 5 business days of being notified of a new or changed processing activity:

1. Review the proposed processing description from the Data Owner
2. Apply the mandatory DPIA criteria: is the processing "likely to result in a high risk"?
3. Check whether the processing type appears on the national supervisory authority's DPIA-required list
4. Document the screening outcome: DPIA required / not required + rationale
5. If DPIA not required: record in DPIA Register and proceed
6. If DPIA required: initiate full DPIA process (see 1.3)

### 1.3 Conducting a Full DPIA

A DPIA must be completed before the processing commences (not after). The DPO leads the DPIA with the Data Owner and relevant technical stakeholders:

**Phase 1 — Describe the processing**:
- What PII is collected? From whom? How? To what purpose?
- Who has access to the PII? Who is it shared with?
- What are the retention periods?

**Phase 2 — Assess necessity and proportionality**:
- Is the processing necessary for the stated purpose? Could less PII achieve the same result?
- Is the lawful basis appropriate?
- Are data subject rights protected?

**Phase 3 — Identify and assess risks**:
- What could go wrong? What is the likelihood and severity of harm to data subjects?
- Consider: unauthorised access, data breach, wrong data, excessive processing, discrimination, profiling effects
- Rate each risk (Low / Medium / High) before mitigation measures

**Phase 4 — Identify risk reduction measures**:
- What controls will reduce each risk?
- After controls: what is the residual risk level?

**Phase 5 — Outcome**:
- If residual risk is acceptable: DPIA approved; processing may proceed
- If residual high risk remains: **prior consultation with supervisory authority required** before processing commences (GDPR Art. 36 / FADP Art. 23)

**Phase 6 — Document and approve**:
- DPO signs off completed DPIA with Data Owner
- DPIA reference added to DPIA Register and linked to RoPA entry
- Executive Management notified of any unmitigatable residual high risk

### 1.4 Reviewing Existing DPIAs

DPIAs must be reviewed when:
- The processing activity changes materially (purpose, scope, technology, volume)
- A privacy incident occurs involving the processing activity
- A supervisory authority or DPA guidance indicates increased risk for the processing type
- At minimum every 3 years for ongoing high-risk processing

---

## Part 2 — Processor Contracts (A.1.2.7)

### 2.1 Engaging a New PII Processor

No PII shall be transferred to a supplier or third party without a signed processor agreement in place. **Procurement triggers this process** when a new supplier with PII access is identified.

**Process**:

1. Procurement identifies supplier as a PII Processor (using categorisation per PRIV-POL-A.3.8-10)
2. Legal prepares or reviews the processor agreement — must include all GDPR Article 28(3) mandatory clauses (see PRIV-IMP-A.1.2.6-9-TG for clause checklist)
3. DPO reviews the privacy clauses for adequacy
4. Agreement signed by both parties before any PII access is granted
5. Processor Agreement Register updated with: supplier name, agreement reference, execution date, review date, PII scope
6. If the supplier cannot or will not sign an adequate processor agreement: **PII access cannot be granted**; escalate to DPO and Legal for alternative sourcing

### 2.2 Annual Processor Agreement Review

The DPO reviews the Processor Agreement Register annually:

| Check | Action if Gap Found |
|-------|-------------------|
| Agreement is current and in force | No action |
| Agreement not reviewed in 12 months (high-risk processor) | Schedule review/renewal |
| Agreement not reviewed in 3 years (standard processor) | Schedule review/renewal |
| Processor's processing activities have changed | Update agreement clauses to reflect new scope |
| New regulatory requirements affect agreement content | Update agreement; obtain fresh signatures |

### 2.3 Processor Agreement Template (Article 28 Compliance)

The DPO maintains an approved processor agreement template. Key components checked per the Article 28 checklist in PRIV-IMP-A.1.2.6-9-TG. For novel or complex processor relationships (joint ventures, cloud infrastructure providers), Legal and DPO agree on bespoke terms.

---

## Part 3 — Joint Controller Arrangements (A.1.2.8)

### 3.1 Identifying Joint Controller Situations

A joint controller situation arises when two or more organisations **jointly determine the purposes and means** of a processing activity. Examples:
- [Organisation] and a partner organisation jointly design a product feature that processes user PII for a shared purpose
- [Organisation] and a marketing partner jointly determine how customer data is used for a shared campaign
- [Organisation] and a research institution jointly conduct a study using identifiable PII

**Not a joint controller situation**: [Organisation] instructs a supplier to process PII according to [Organisation]'s instructions alone — that is a processor relationship.

**When in doubt**: DPO and Legal assess the relationship and document the determination.

### 3.2 Establishing a Joint Controller Arrangement

1. DPO and Legal identify the joint controller situation and contact the other controller's privacy team
2. Negotiate the arrangement — the arrangement must determine:
   - Who is responsible for which GDPR obligations (privacy notice, rights requests, breach notification, DPIAs)
   - The primary contact for data subjects
   - Security responsibilities for shared processing
3. Execute the arrangement in writing (signed by both organisations)
4. Make the **essence of the arrangement** available to data subjects — at minimum, which controller to contact and for what purpose
5. Add to Joint Controller Arrangement Register

### 3.3 Joint Controller Register Maintenance

The DPO reviews the Joint Controller Arrangement Register annually:
- Are all joint processing arrangements documented?
- Has the processing activity or the parties' roles changed since the arrangement was executed?
- Is the essence of the arrangement still being communicated to data subjects (in the relevant privacy notice)?

---

## Part 4 — Records of Processing Activities (A.1.2.9)

### 4.1 Building the RoPA

The RoPA is the DPO's primary accountability record. Every processing activity conducted by [Organisation] as PII Controller must have a RoPA entry.

**Initial RoPA build process**:

1. DPO circulates a RoPA data collection template to all Data Owners and department heads
2. Each department maps its processing activities: what PII, from whom, for what purpose, in what system, shared with whom, retained how long
3. DPO reviews submissions for completeness and lawful basis alignment
4. DPO drafts RoPA entries from submissions, confirms with Data Owners
5. DPO publishes the initial RoPA with Executive Management approval

### 4.2 Maintaining the RoPA

**Quarterly review**: DPO circulates the RoPA to Data Owners asking: are any processing activities missing, discontinued, or changed? Changes actioned within 10 business days of confirmation.

**Trigger-based update**: RoPA is updated when:
- A new processing activity is identified (before processing commences)
- An existing activity is discontinued
- The purpose, lawful basis, categories, recipients, retention period, or transfer arrangements change
- A new processor or joint controller relationship is established

### 4.3 RoPA Accuracy Responsibility

Data Owners are responsible for providing accurate processing information for their domain. The DPO is responsible for the overall accuracy and completeness of the RoPA. Annual formal review: DPO confirms all entries with Data Owners and signs off on the RoPA currency.

---

## Evidence Checklist

- [ ] DPIA Register — all DPIA screenings (with outcome) and full DPIAs documented
- [ ] Full DPIAs for all high-risk processing, with risk treatment and residual risk documented
- [ ] Prior consultation records — where residual high risk was identified and DPA consulted
- [ ] Processor Agreement Register — all active processors listed with agreement status and review date
- [ ] Signed processor agreements — for all active processors, including Article 28(3) mandatory clauses
- [ ] Joint Controller Arrangement Register — all active joint controller relationships
- [ ] RoPA — current, accurate, covers all processing activities; quarterly reviews documented
- [ ] Annual formal RoPA review record — DPO sign-off

---

<!-- QA_VERIFIED: [Date] -->
