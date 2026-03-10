<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.3.2-4-UG:privacy:UG:a.1.3.2-4 -->
**PRIV-IMP-A.1.3.2-4-UG — Transparency and Information Provision — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Transparency and Information Provision — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.3.2-4-UG |
| **Related Policy** | PRIV-POL-A.1.3.2-4 (Transparency and Information Provision) |
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

- PRIV-POL-A.1.3.2-4 (Transparency and Information Provision — the governing policy)
- PRIV-IMP-A.1.3.2-4-TG (Transparency and Information Provision — Technical Guide)
- PRIV-POL-A.1.3.5-10 (Data Subject Rights — rights referenced in privacy notices)
- PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent — lawful basis stated in notices)

---

## Purpose of This Guide

This guide explains **how to implement** the transparency and information provision requirements of PRIV-POL-A.1.3.2-4. It covers how to determine transparency obligations for each processing activity, how to draft privacy notices meeting GDPR Article 13/14 content requirements, and how to ensure notices are provided at the right time and in accessible formats.

**Who this guide is for**: DPO, Legal/Compliance, Marketing/Communications, HR, Development/Product Teams.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Determining Obligations to PII Principals (A.1.3.2)

### 1.1 Mapping Transparency Obligations per Processing Activity

For each processing activity in the RoPA, the DPO maps the applicable transparency obligations:

1. Is the PII collected **directly** from the data subject → Article 13 obligations apply
2. Is the PII collected **indirectly** (from a third party, from a public source, inferred) → Article 14 obligations apply
3. Are there jurisdiction-specific obligations? (CH FADP Articles 19/20; UK GDPR if applicable)
4. Is the processing consent-based? → Right to withdraw consent must be clearly communicated
5. Is automated decision-making involved? → Additional transparency elements required (Art. 22 information)
6. Is there legitimate interests processing? → Explicit notification of right to object required (Art. 21(4))

Document the mapped obligations in the PII Principal Obligations Register (template in PRIV-IMP-A.1.3.2-4-TG).

### 1.2 Triggering Notice Updates

When any of the following occur, the DPO must review and if necessary update the relevant privacy notice(s) within 30 days:

| Trigger | Notice Action |
|---------|--------------|
| New processing activity added to RoPA | Check if existing notice covers it; update or create new notice if not |
| Existing processing activity changes purpose, basis, recipients, or retention | Update the affected notice section |
| New regulatory requirement changes the information elements | Update all affected notices |
| New supervisory authority guidance materially changes expectations | Review all notices against new guidance; update as required |
| New product feature or service launch | Ensure collection point notice is published before launch |

---

## Part 2 — Drafting Privacy Notice Content (A.1.3.3)

### 2.1 Privacy Notice Content Checklist

Use this checklist to confirm a privacy notice is complete for GDPR Article 13 (direct collection):

| Element | Included? | Note |
|---------|-----------|------|
| Controller identity (legal name) and contact | Yes / No | Include address and DPO email |
| DPO contact details | Yes / No | Where DPO is appointed |
| Processing purposes (specific) | Yes / No | Per processing activity |
| Legal basis for each purpose | Yes / No | Art. 6 basis; Art. 9 for special category |
| Legitimate interests described | Yes / No | Where Art. 6(1)(f) is the basis |
| Categories of recipients | Yes / No | Internal teams, processors, public authorities |
| International transfers and safeguards | Yes / No | Countries + mechanism (adequacy / SCCs / BCRs) |
| Retention period or retention criteria | Yes / No | Per data category or purpose |
| Right to access (Art. 15) | Yes / No | How to exercise |
| Right to rectification (Art. 16) | Yes / No | How to exercise |
| Right to erasure (Art. 17) | Yes / No | How to exercise |
| Right to restriction (Art. 18) | Yes / No | How to exercise |
| Right to portability (Art. 20) | Yes / No | Where applicable |
| Right to object (Art. 21) | Yes / No | Must be explicit at legitimate interests basis |
| Right to withdraw consent (Art. 7(3)) | Yes / No | Where consent is the basis |
| Right to lodge complaint with supervisory authority | Yes / No | Include DPA name and contact |
| Whether provision of PII is obligatory and consequences | Yes / No | Where applicable (contracts, legal requirements) |
| Automated decision-making information (Art. 22) | Yes / No | Where applicable |

For **indirect collection** (Art. 14), also include: the source(s) of the PII and whether from publicly available sources.

### 2.2 Writing Quality Standards

Privacy notices must be:

- **Plain language**: No legal jargon without explanation; reading level appropriate to the intended audience
- **Layered**: Short contextual notices at collection points (3-5 sentences) + link to full notice; full notice accessible always
- **Specific**: Vague statements ("may share with partners") are inadequate — name or categorise recipients; specify purposes specifically
- **Accurate**: Matches the actual processing documented in the RoPA — do not include purposes that aren't documented; do not omit purposes that are

**DPO review is mandatory** before any privacy notice is published, updated, or provided to data subjects.

### 2.3 Employee Privacy Notices

Employee privacy notices have the same content requirements as consumer notices but tailored to the employment context. The HR Manager coordinates with the DPO to:

1. Document all categories of employee PII processed (payroll, attendance, performance, health, benefits)
2. Map each category to purposes and lawful basis (employment contract, legal obligation, consent where used)
3. Draft the employee privacy notice
4. Provide the notice to all new employees before or at commencement of employment
5. Update and re-issue the notice when processing changes

---

## Part 3 — Providing Information to PII Principals (A.1.3.4)

### 3.1 Publication and Access Points

The full privacy notice must be accessible at all times:

| Access Point | How to Publish |
|-------------|----------------|
| Website (external-facing) | Footer link "Privacy Notice" or "Privacy Policy" — present on every page |
| App (mobile or web) | Settings/profile section; accessible without requiring data subject to scroll through T&Cs |
| Physical collection (paper forms) | Either printed on the form or clearly referenced with a URL/QR code |
| Email data collection | Privacy statement or link in the collection email |
| Employee induction | Distributed as part of onboarding documentation; acknowledgment obtained |
| At each collection point | Short inline notice with link to full notice |

### 3.2 Timing of Provision — Practical Implementation

**Direct collection** (online form, app registration, physical form):
- Short privacy statement explaining the processing purpose and basis must be visible before or at the point of data entry
- "By clicking Submit / Sign, I acknowledge that I have read the privacy notice" language is acceptable where the notice link is immediately accessible
- Data collection must not occur before the notice has been presented (not buried after submission)

**Indirect collection** (buying a list, receiving referral data, inferred data):
1. DPO identifies the indirect collection situation and calculates the earliest notification deadline: within 1 month of obtaining the PII; OR at first communication; OR at first disclosure to another recipient — whichever is earliest
2. Communications team or DPO issues a notification to affected data subjects within the deadline
3. Notification includes the full Article 14 information or directs to where it can be accessed
4. Notifications are logged in the PII Principal Obligations Register (date sent, channel, population covered)

### 3.3 Right to Object — First Communication

Where processing relies on legitimate interests, the data subject must be explicitly and clearly informed of the right to object **at the latest at the time of first communication** with the data subject (GDPR Art. 21(4)). This means:

- The right to object and how to exercise it must appear in the first marketing email, the registration confirmation, or the employee onboarding notice — not buried in a full privacy notice that the data subject must go looking for
- For direct marketing: unsubscribe mechanism must be in every communication

### 3.4 Annual Privacy Notice Review Process

1. DPO schedules annual review (Q1 of each year or at certification renewal)
2. Cross-reference current privacy notices against the current RoPA — are all processing activities covered?
3. Compare notice content against current Article 13/14 requirements and any updated supervisory authority guidance
4. Update notices where gaps found; have DPO and Legal sign off
5. Republish updated notices with a new version date; where changes are material, consider notifying data subjects of the update

---

## Evidence Checklist

- [ ] PII Principal Obligations Register — obligations mapped per processing activity
- [ ] Privacy notice(s) — current, published, covering all processing activities; reviewed within 12 months
- [ ] Privacy notice version history — all prior versions retained with effective dates
- [ ] Collection point documentation — evidence of notice provision at each data collection point
- [ ] Indirect collection notification records — where applicable, notifications sent within Art. 14 timeframes
- [ ] Employee privacy notice — provided at onboarding; acknowledgment records
- [ ] Annual notice review record — DPO sign-off on currency and completeness

---

<!-- QA_VERIFIED: [Date] -->
