<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.3.11-TG:privacy:TG:a.1.3.11 -->
**PRIV-IMP-A.1.3.11-TG — Automated Decision Making — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Automated Decision Making — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.3.11-TG |
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
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or technical change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.3.11 (Automated Decision Making — the governing policy)
- PRIV-IMP-A.1.3.11-UG (Automated Decision Making — User Guide)
- PRIV-IMP-A.1.2.6-9-TG (Privacy Governance and Records — DPIA template for ADM)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for automated decision-making compliance. It covers:

- ADM Register schema
- ADM Obligation Assessment template
- ADM Decision Communication template
- Human Review Request Response template

**Audience**: DPO, Legal/Compliance, Development/Data Science Teams.

---

## 1. ADM Register

The ADM Register is the DPO's authoritative list of all in-scope automated decision-making activities. Classified CONFIDENTIAL.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| ADM ID | Text | Unique reference (e.g., ADM-001) |
| Activity Name | Text | Descriptive name of the ADM activity |
| System / Application | Text | System or platform where ADM is implemented |
| RoPA Reference | Text | Linked processing activity in the RoPA |
| Decision Type | Text | What decision the system makes (e.g., loan eligibility, insurance pricing, job application screening) |
| Significant Effects | Text | Legal or significant effects on data subjects |
| Special Category PII Involved | Boolean | Yes / No |
| Special Category Types | Text | If yes: types of special category PII used |
| Art. 22(2) Exception Invoked | Enum | Contract necessity / Authorised by law / Explicit consent |
| Exception Evidence Reference | Text | Reference to contract terms, legal provision, or consent record |
| Safeguard: Human Review | Enum | Implemented / Not Implemented / Planned |
| Safeguard: Point of View Mechanism | Enum | Implemented / Not Implemented / Planned |
| Safeguard: Contestation Mechanism | Enum | Implemented / Not Implemented / Planned |
| Human Reviewer Role | Text | Named role responsible for human reviews |
| Transparency in Privacy Notice | Enum | Included / Pending / Not Included |
| Privacy Notice Section Reference | Text | Where ADM is covered in the privacy notice |
| DPIA Required | Boolean | Yes / No |
| DPIA Reference | Text | Linked DPIA Register entry |
| DPO Approved | Boolean | Yes / No |
| Approval Date | Date | Date DPO approved the ADM activity |
| Last Reviewed | Date | Date register entry was last reviewed |
| Status | Enum | Active / Suspended / Decommissioned |
| Notes | Text | Open items, regulatory developments, model changes |

---

## 2. ADM Obligation Assessment Template

Complete for each ADM activity before deployment and when materially changed.

```
ADM OBLIGATION ASSESSMENT

ADM ID: ADM-[NNN]
Activity Name: _____________________________________________
System / Application: _____________________________________________
Date: _____________________________________________
DPO: _____________________________________________

SECTION 1 — IN-SCOPE DETERMINATION

1.1 Does this system make decisions based solely on automated processing?
    (No meaningful human involvement in the decision)
    [ ] Yes  [ ] No — human in the loop (transparency still applies; Art. 22 does not)

1.2 Do those decisions produce legal or significantly significant effects?
    [ ] Yes — describe: _______________________________________________
    [ ] No — this activity is not in scope for Art. 22

If both 1.1 and 1.2 = Yes: this activity is in scope. Continue.

SECTION 2 — EXCEPTION TO ART. 22(1)

One of the following must apply:
[ ] Contract necessity — ADM is necessary for the performance of a contract with the data subject
    Describe: _______________________________________________
[ ] Authorised by law — ADM is authorised by EU/Member State law
    Cite specific law and provision: _______________________________________________
[ ] Explicit consent — data subject has given explicit consent
    Consent mechanism reference: _______________________________________________

Is special category PII used in the ADM?
[ ] No  [ ] Yes — Art. 22(4) condition additionally required:
         [ ] Explicit consent  [ ] Substantial public interest (specify: _______________)
         Art. 9(2) condition also required: _______________________________________________

SECTION 3 — SAFEGUARDS

3.1 Human review mechanism:
    Description of mechanism: _______________________________________________
    Reviewer role: _______________________________________________
    [ ] Mechanism is genuinely human (reviewer can override automated output)
    [ ] Data subject is informed how to request human review

3.2 Right to express point of view:
    Mechanism: _______________________________________________
    [ ] Data subject can provide additional context before human review concludes

3.3 Right to contest the decision:
    Mechanism: _______________________________________________
    [ ] Contestation leads to genuine reconsideration, not auto-confirmation

SECTION 4 — TRANSPARENCY

4.1 Privacy notice coverage:
    [ ] Existence of ADM disclosed
    [ ] Logic (key factors) described at accessible level
    [ ] Significance and consequences described
    [ ] Human review right and how to exercise explained
    Notice section: _______________________________________________

4.2 Decision communication:
    When the automated decision is communicated to the data subject, does it include:
    [ ] Statement that the decision was automated
    [ ] Key factors influencing the decision
    [ ] Instructions on how to request human review
    [ ] Contact details for DPO / privacy team

SECTION 5 — DPIA

DPIA required? [ ] Yes — DPIA reference: _______________   [ ] No
DPIA rationale (if not required): _______________________________________________

ASSESSMENT CONCLUSION
[ ] ADM activity is compliant — exception invoked, safeguards implemented, transparency provided
[ ] ADM activity requires remediation before deployment — items: _______________
[ ] ADM activity should not proceed — no valid exception available

DPO Approval: _________________________ Date: _____________
```

---

## 3. ADM Decision Communication Template

Use when communicating an automated decision to the data subject:

```
Subject: Automated Decision Notice — [Decision Type]

Dear [Name],

We are writing to inform you of an automated decision made in relation to
your [application / account / request].

DECISION OUTCOME
[Clear statement of the decision, e.g., "Your application for [X] has been
automatically declined."]

This decision was made using an automated system without individual human review.

WHY THIS DECISION WAS MADE
Our automated system considered the following factors in making this decision:
[List the key factors relevant to the data subject's case — at an accessible level.
Example: your [credit score / account history / eligibility criteria / application data].]

[If applicable: This decision was made based on information provided by [source].]

YOUR RIGHTS

You have the right to:
1. **Request human review**: Ask a member of our team to review this automated decision.
   A person will review your case and the factors considered, and may confirm, modify,
   or reverse the automated decision.

2. **Express your point of view**: Provide additional information or context you believe
   is relevant before or during the human review.

3. **Contest this decision**: Challenge the outcome if you believe the decision is incorrect
   or was made on the basis of inaccurate information.

HOW TO EXERCISE YOUR RIGHTS
Contact: privacy@[domain] | Subject: "Human Review Request — [Decision Type]"
Reference: [ADM-REF-XXXXXX]
Deadline to request review: [Date — typically 30 days from this letter]
We will respond within one month of receiving your request.

DATA PROTECTION CONTACT
[DPO Name] | privacy@[domain]

Right to complain: [Supervisory Authority Name] — [URL]

[Organisation Legal Name]
[Date]
```

---

## 4. Human Review Response Template

```
Subject: Human Review Outcome — [Decision Type] — [Reference]

Dear [Name],

Thank you for requesting a human review of the automated decision dated [Date].

REVIEW OUTCOME
[ ] Decision confirmed: Following human review, the original decision is maintained.
    Reason: [Explain basis for maintaining decision]

[ ] Decision modified: The original decision has been updated as follows:
    New outcome: [Describe modified decision]
    Reason: [Explain what changed and why]

[ ] Decision reversed: The original decision has been overturned.
    New outcome: [Describe reversed decision and next steps]
    Reason: [Explain why the decision was reversed]

REVIEW PROCESS
Your case was reviewed by [reviewer role] who:
- Reviewed the factors considered in the automated decision
- Considered the information you provided
- Assessed your case against the applicable criteria

[Where additional information was provided: We specifically considered the additional
information you provided: [summary of what was considered].]

FURTHER OPTIONS
If you are not satisfied with the outcome of this review, you have the right to:
- Contact us for further explanation: privacy@[domain]
- Lodge a complaint with [Supervisory Authority Name]: [URL]

[Organisation Legal Name] | [DPO Name] | [Date]
```

---

<!-- QA_VERIFIED: [Date] -->
