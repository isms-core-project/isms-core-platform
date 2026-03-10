<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.2.2-5-UG:privacy:UG:a.1.2.2-5 -->
**PRIV-IMP-A.1.2.2-5-UG — Lawful Basis and Consent — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Lawful Basis and Consent — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.2.2-5-UG |
| **Related Policy** | PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent) |
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

- PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent — the governing policy)
- PRIV-IMP-A.1.2.2-5-TG (Lawful Basis and Consent — Technical Guide)
- PRIV-POL-A.1.2.6-9 (Privacy Governance and Records — RoPA maintained here)
- PRIV-POL-A.1.3.5-10 (Data Subject Rights — consent withdrawal handled here)

---

## Purpose of This Guide

This guide explains **how to implement** the purpose documentation, lawful basis determination, and consent management requirements of PRIV-POL-A.1.2.2-5. It covers how to document processing purposes in the RoPA, how to determine and evidence lawful basis, how to design and approve consent processes, and how to maintain consent records.

**Who this guide is for**: DPO, Legal/Compliance, Data Owners, Development/Product Teams, HR.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Documenting Processing Purposes (A.1.2.2)

### 1.1 When to Document a New Processing Purpose

A new processing purpose must be documented in the RoPA before any PII is collected or processing commences. Triggers:

- New product or service feature that involves PII collection or use
- New internal process that requires access to or use of existing PII for a new purpose
- New data category being added to an existing processing activity
- Change to the purpose of an existing processing activity

**Who is responsible**: The Data Owner for the relevant domain identifies the processing purpose and proposes it to the DPO. The DPO approves the RoPA entry before processing commences.

### 1.2 Writing Specific Processing Purposes

Purposes must be specific enough that a data subject can understand what their PII is used for. The test: could a reasonable person reading this purpose understand what will happen to their PII?

**Insufficient (too vague)**:
- "Improve our services"
- "Business purposes"
- "Marketing"

**Sufficient (specific)**:
- "Sending monthly newsletter emails with product updates to subscribers who have opted in"
- "Analysing user session data to identify and fix application errors in the checkout flow"
- "Processing payroll including calculating statutory deductions and issuing payslips to employees"

**Process for documenting a purpose**:
1. Describe the activity: what PII is collected/used; from whom; to do what; in what system
2. Confirm the purpose is specific, explicit, and legitimate — not vague or aspirational
3. DPO reviews and approves the purpose statement before it is added to the RoPA
4. Add the purpose to the RoPA (per PRIV-POL-A.1.2.6-9 RoPA management procedures)

### 1.3 Purpose Limitation and Compatibility Assessment

If an existing processing activity is proposed for a new purpose (secondary use):

1. DPO conducts a compatibility assessment — see PRIV-IMP-A.1.2.2-5-TG for the assessment template
2. Compatibility factors assessed: relationship between purposes; nature of PII; consequences for data subjects; context of collection; existence of safeguards
3. If compatible: document the assessment; secondary use may proceed without fresh consent
4. If not compatible: fresh consent is required for the new purpose, or processing cannot proceed

---

## Part 2 — Determining and Documenting Lawful Basis (A.1.2.3)

### 2.1 Lawful Basis Selection Process

For each processing purpose, the Data Owner and DPO work through the following selection process:

**Step 1**: Identify which Article 6 basis/bases could apply given the purpose and context.

**Step 2**: For each candidate basis, apply the selection test:

| Basis | Key Selection Question |
|-------|----------------------|
| **Contract** (Art. 6(1)(b)) | Is the processing genuinely necessary to perform a contract with the data subject? Would they be unable to receive the contracted service without it? |
| **Legal obligation** (Art. 6(1)(c)) | Does a specific, identifiable law impose this obligation? (Name the law and provision.) Is compliance actually required, not merely desirable? |
| **Legitimate interests** (Art. 6(1)(f)) | Is there a real, specific interest? Is processing necessary (not just useful)? Would data subjects reasonably expect it? Does it override their rights? (Requires LIA) |
| **Consent** (Art. 6(1)(a)) | Can you offer genuine free choice? If no, consent is not the right basis. |
| **Vital interests** (Art. 6(1)(d)) | Is there a genuine life-threatening situation? (Narrow — rarely applicable outside emergency contexts) |
| **Public task** (Art. 6(1)(e)) | Does [Organisation] exercise public authority or perform a public task? (Usually not applicable to private sector organisations) |

**Step 3**: For **special category PII**: identify the Article 9(2) condition in addition to the Article 6 basis.

**Step 4**: Document the chosen basis in the RoPA with the supporting rationale.

### 2.2 Legitimate Interests Assessment (LIA)

Where legitimate interests is the proposed basis:

1. DPO and Legal conduct a three-part balancing test (see PRIV-IMP-A.1.2.2-5-TG for LIA template):
   - **Purpose test**: Is the interest legitimate, real, and specific?
   - **Necessity test**: Is the processing necessary for that interest? Is there a less privacy-intrusive alternative?
   - **Balancing test**: Do the data subjects' interests, rights, or fundamental freedoms override the legitimate interest?
2. LIA must be completed before processing commences
3. LIA approved and signed by DPO
4. LIA retained as evidence of lawful basis determination; reviewed when processing activity changes
5. Data subjects must be informed of the legitimate interests basis (privacy notice requirement per PRIV-POL-A.1.3.2-4) and have a right to object (PRIV-POL-A.1.3.5-10)

### 2.3 Evidencing Lawful Basis

The DPO maintains evidence of each lawful basis determination:

| Basis | Evidence Required |
|-------|-----------------|
| Contract | Copy of contract type or template; explanation of why each processing purpose is necessary for contract performance |
| Legal obligation | Citation of the specific legal provision (Act, Article, Regulation number) |
| Legitimate interests | Completed and signed LIA |
| Consent | Consent process documentation + consent records (see Part 3 and 4) |
| Vital interests | Assessment documenting the life-threatening situation and lack of alternative basis |

Evidence is filed in the PIMS document repository linked to the RoPA entry.

---

## Part 3 — Designing the Consent Process (A.1.2.4)

### 3.1 When Consent is Appropriate as a Basis

Use consent as the lawful basis when:
- No other basis clearly applies, AND
- You can genuinely offer the data subject a free and unconstrained choice, AND
- Refusal to consent will not disadvantage the data subject in any meaningful way

Do **not** use consent when:
- The processing is necessary for contract performance (use contract basis)
- A legal obligation requires it (use legal obligation basis)
- You cannot offer genuine free choice (e.g., consent required to use the service)

### 3.2 Consent Process Design Approval

Before implementing any consent-based processing, the Product/Development team submits a consent process proposal to the DPO covering:

1. The purposes for which consent will be sought (list each distinctly)
2. The information that will be presented to the data subject before consent is requested
3. The mechanism by which consent will be expressed (checkbox, signature, click, etc.)
4. How consent will be recorded and linked to the data subject's identity
5. How withdrawal of consent will be enabled (and confirmed to be as easy as giving consent)
6. For child-oriented services: age verification mechanism and parental consent process

DPO reviews the proposal against the consent validity criteria in PRIV-POL-A.1.2.2-5. DPO may require changes before approval. No consent-based processing commences without DPO approval of the process.

### 3.3 Common Consent Design Pitfalls

| Problem | Why It Invalidates Consent | Required Fix |
|---------|--------------------------|--------------|
| Pre-ticked checkbox | Not unambiguous positive opt-in | Use un-ticked checkbox requiring active selection |
| Consent bundled with T&Cs | Not freely given or specific | Separate consent from T&Cs acceptance |
| Single consent for multiple purposes | Not specific | Separate checkbox or question per distinct purpose |
| No withdrawal mechanism | Not freely given | Provide withdrawal option as easy as consent (unsubscribe link, settings page) |
| Vague purpose description | Not informed | Specify exact purpose before requesting consent |
| Consent required to use service | Not freely given (unless strictly necessary) | Review whether consent is the right basis |

---

## Part 4 — Obtaining and Recording Consent (A.1.2.5)

### 4.1 Consent Record Requirements

Every consent-based processing activity must generate a consent record. IT confirms with DPO that consent collection systems generate records meeting the schema defined in PRIV-IMP-A.1.2.2-5-TG.

**Key principle**: The consent record is your evidence of lawful basis. If you cannot produce a consent record for a specific data subject showing when and for what they consented, you cannot rely on consent as your lawful basis.

### 4.2 Managing Consent Withdrawal

When a data subject withdraws consent:

1. The withdrawal is received and timestamped (channel: email to DPO, privacy settings page, written request)
2. Processing based on that consent must cease — the DPO/Privacy Champion confirms with the relevant Data Owner that processing has stopped within **[X] business days** (define in consent process documentation — typically 5 business days or less)
3. If no other lawful basis applies: PII must be deleted or anonymised
4. If PII was disclosed to third parties under that consent: notify those parties of the withdrawal
5. Update the consent record: status = Withdrawn; withdrawal date and channel recorded
6. Confirm to the data subject that consent has been withdrawn and processing has ceased

### 4.3 Consent Record Accuracy Reviews

Quarterly, the DPO confirms with Data Owners that:
- Consent records are being generated correctly for all consent-based activities
- Withdrawal mechanisms are functioning and withdrawal is being actioned promptly
- No consent records are missing, corrupted, or inaccessible

---

## Evidence Checklist

- [ ] RoPA — all processing activities with documented purposes, lawful basis, and basis evidence references
- [ ] Legitimate Interests Assessments (LIAs) — for all processing activities relying on legitimate interests basis
- [ ] Consent process documentation — DPO-approved process for each consent-based activity
- [ ] Consent records — generated, timestamped, linked to data subject identity
- [ ] Purpose compatibility assessments — for any secondary use of PII
- [ ] Consent withdrawal records — where withdrawals have occurred; processing cessation confirmed

---

<!-- QA_VERIFIED: [Date] -->
