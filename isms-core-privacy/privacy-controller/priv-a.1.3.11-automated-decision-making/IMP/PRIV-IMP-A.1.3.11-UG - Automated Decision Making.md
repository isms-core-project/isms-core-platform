<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.3.11-UG:privacy:UG:a.1.3.11 -->
**PRIV-IMP-A.1.3.11-UG — Automated Decision Making — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Automated Decision Making — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.3.11-UG |
| **Related Policy** | PRIV-POL-A.1.3.11 (Automated Decision Making) |
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

- PRIV-POL-A.1.3.11 (Automated Decision Making — the governing policy)
- PRIV-IMP-A.1.3.11-TG (Automated Decision Making — Technical Guide)
- PRIV-POL-A.1.3.5-10 (Data Subject Rights — human review right handled via DSR process)
- PRIV-POL-A.1.2.6-9 (Privacy Governance and Records — DPIA required for high-risk ADM)

---

## Purpose of This Guide

This guide explains **how to implement** the automated decision-making obligations of PRIV-POL-A.1.3.11. It covers how to identify in-scope ADM activities, how to document obligations and safeguards, and how to operate the human review mechanism.

**Who this guide is for**: DPO, Legal/Compliance, Development/Data Science Teams, Product Management.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Identifying In-Scope ADM (A.1.3.11)

### 1.1 What Is and Is Not In Scope

**In scope** (GDPR Article 22 applies): A decision that:
- Is based solely on automated processing (no meaningful human involvement in the decision)
- Produces a legal effect on the data subject (e.g., denial of a right, contract, or benefit), OR
- Produces a similarly significant effect (e.g., automatic denial of credit, automatic rejection of an employment application, insurance rate automatically set based on a model)

**Not in scope for Article 22** (though transparency still applies):
- A human reviews an automated output before a final decision is made — this is "decision support"
- Automation that filters or ranks results but leaves the final selection to a human
- Analytics or profiling that does not result in an automated decision affecting individuals

**Test to apply**: Remove the human from the process. Does the system make a decision on its own that directly affects the data subject in a legal or significant way? If yes → in scope.

### 1.2 Discovering In-Scope ADM Activities

At PIMS initial implementation and annually thereafter, the DPO surveys development/data science and product teams:

1. Do any systems make automatic decisions about individuals (credit scoring, eligibility checking, pricing, access control) without a human making the final call?
2. Are there any AI/ML models that classify, rank, or recommend actions relating to individuals, and are those recommendations automatically acted upon?
3. Are any application processing or filtering steps applied automatically that determine whether an individual proceeds, qualifies, or is rejected?

All identified ADM activities are added to the ADM Register (see PRIV-IMP-A.1.3.11-TG for schema). Development teams must notify the DPO **before deploying** any new ADM functionality.

---

## Part 2 — Documenting Obligations and Exceptions

### 2.1 Obligations for Each ADM Activity

For each ADM activity in the register, the DPO documents:

1. **The default restriction**: Data subjects have the right not to be subject to solely automated decisions with significant effects (Art. 22(1))
2. **The exception invoked** (one must apply for ADM to be lawful):
   - **Contract necessity**: The automated decision is necessary for entering into or performing a contract with the data subject — e.g., automated credit assessment required to process a loan application
   - **Authorised by law**: The processing is authorised by EU or Member State law with appropriate safeguards — e.g., fraud detection mandated by AML regulation
   - **Explicit consent**: The data subject has given explicit consent for the automated decision — note: explicit consent (not standard consent)
3. **Safeguards implemented** (required for all three exceptions):
   - Right to obtain human intervention
   - Right to express point of view
   - Right to contest the decision
4. **Transparency information**: What data subjects are told in the privacy notice about this ADM activity

### 2.2 Special Category PII in ADM

If the ADM system processes special category PII (health, biometric, genetic, racial origin, etc.):
- An Article 22(4) exception is additionally required: either explicit consent or substantial public interest under Union/Member State law
- This must also be assessed against Article 9(2) conditions
- A DPIA is almost always required — DPO must conduct a DPIA before any special category ADM is deployed
- Explicit DPO approval is required before special category ADM goes live

---

## Part 3 — Operating the Human Review Mechanism

### 3.1 How the Human Review Mechanism Must Work

The human review mechanism allows a data subject to request that a human reviews an automated decision that significantly affects them. This is not an appeal mechanism — it is a first-instance human review. Requirements:

- The mechanism must be **accessible**: data subjects are told how to request human review (in the privacy notice and when the automated decision is communicated to them)
- The mechanism must be **genuinely human**: the reviewer must be a person with the authority to override or modify the automated decision, and must actually review the case — not simply confirm the automated output
- The mechanism must be **timely**: the human review response should be provided within the standard one-month rights response timeframe
- The mechanism must allow the data subject to **express their point of view**: give the data subject the opportunity to provide additional information before the human review conclusion

**Reviewer competence**: The human reviewer must understand the ADM system's logic (what factors influence the decision) and have access to the data subject's specific inputs and outputs. A reviewer who cannot explain the decision or has no ability to override it is not adequate.

### 3.2 When a Human Review Request Is Received

Human review requests are logged in the Data Subject Rights Register (per PRIV-POL-A.1.3.5-10) and handled as a data subject rights request:

1. DPO receives the request; logs it; acknowledges within 3 business days
2. DPO identifies the relevant ADM system and the data subject's specific decision output
3. DPO coordinates with the designated human reviewer for the ADM system
4. Data subject is given the opportunity to provide additional information or context
5. Human reviewer reviews: the automated output, the data subject's inputs, and any additional context provided
6. Human reviewer makes a determination: confirm / modify / reverse the automated decision
7. DPO communicates the outcome to the data subject within one month
8. Document the outcome in the DSR Register and the ADM Register

---

## Part 4 — Transparency for ADM

### 4.1 Privacy Notice Requirements for ADM

For each in-scope ADM activity, the privacy notice must include:

- **Existence**: That automated decision-making (including profiling) takes place
- **Logic**: Meaningful information about the logic involved — what factors are considered; how they influence the outcome. Not a technical specification, but enough for the data subject to understand the process. Example: "We assess loan applications using a credit scoring model that takes into account your payment history, outstanding debts, credit history length, and income."
- **Significance and consequences**: What the decision means for the data subject. Example: "If our model assesses your creditworthiness as below threshold, your loan application will be automatically declined."
- **Right to human review**: How to request a human review, express your point of view, or contest the decision.

### 4.2 Communication of an Automated Decision to the Data Subject

When an automated decision is communicated to a data subject, the communication must include:

- Clear statement that the decision was automated
- Summary of the key factors that influenced the decision (at a level the data subject can understand)
- Instructions on how to request human review or contest the decision
- Contact details for the DPO or privacy team

---

## Evidence Checklist

- [ ] ADM Register — all in-scope automated decision-making activities documented
- [ ] Exception documentation — Article 22(2) exception identified and evidenced for each ADM activity
- [ ] Safeguards implementation — human review, point-of-view, and contestation mechanisms operational
- [ ] DPIA for high-risk ADM — completed before deployment
- [ ] Privacy notice ADM section — existence, logic, significance, and human review right communicated
- [ ] ADM decision communications — contain required information and human review instructions
- [ ] Human review records — DSR register entries for review requests; outcomes documented

---

<!-- QA_VERIFIED: [Date] -->
