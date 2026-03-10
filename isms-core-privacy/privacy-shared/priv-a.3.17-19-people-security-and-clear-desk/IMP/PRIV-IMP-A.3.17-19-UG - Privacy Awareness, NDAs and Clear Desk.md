<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.17-19-UG:privacy:UG:a.3.17-19 -->
**PRIV-IMP-A.3.17-19-UG — Privacy Awareness, NDAs and Clear Desk — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Awareness, NDAs and Clear Desk — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.3.17-19-UG |
| **Related Policy** | PRIV-POL-A.3.17-19 (Privacy Awareness, NDAs and Clear Desk) |
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

- PRIV-POL-A.3.17-19 (Privacy Awareness, NDAs and Clear Desk — the governing policy)
- PRIV-IMP-A.3.17-19-TG (Privacy Awareness, NDAs and Clear Desk — Technical Guide)
- PRIV-POL-A.3.3-4 (Privacy Policy and Roles — role definitions including Privacy Champion)
- ISMS-POL-A.6.3 (Information Security Awareness and Training — ISMS parallel)

---

## Purpose of This Guide

This guide explains **how to implement** the privacy awareness, confidentiality agreement, and clear desk/screen requirements of PRIV-POL-A.3.17-19. It covers how to build and maintain the privacy training programme, how to manage the Confidentiality Agreement Register, and how to enforce clear desk and clear screen rules for PII processing environments.

**Who this guide is for**: DPO, HR Manager, CISO, Privacy Champions, Line Management.

---

## Part 1 — Privacy Awareness, Education and Training (A.3.17)

### 1.1 Building the Privacy Training Programme

The DPO owns the privacy training curriculum. The programme is separate from (and complementary to) the general information security awareness programme managed by the CISO.

**Initial programme build**:

1. Map personnel categories to training tiers per PRIV-POL-A.3.17-19 (all personnel → awareness; PII handlers → role training; elevated roles → specialist training; DPO → professional development)
2. Define the content required for each tier — see PRIV-IMP-A.3.17-19-TG for curriculum content requirements
3. Select delivery method per tier (e-learning module, workshop, briefing, self-study with acknowledgment)
4. Agree with HR on the induction integration point — privacy awareness must be completed before PII access is granted to new starters
5. Agree with CISO on integration points with the general security awareness programme (avoid duplicating identical content)
6. Build completion tracking into the Personnel Privacy Training and Acknowledgment Register (see PRIV-IMP-A.3.17-19-TG for register schema)

### 1.2 Delivering Training to New Starters

**Process for new employees and contractors**:

1. HR notifies DPO (or designated Privacy Champion) of new starter engagement — at minimum 3 business days before start date
2. DPO or Privacy Champion assigns the appropriate training tier based on the new starter's role and PII access scope
3. New starter completes required privacy training as part of induction — before any PII access is provisioned
4. Completion is recorded in the Personnel Privacy Training and Acknowledgment Register within 1 business day of completion
5. IT Security Team is informed that privacy training is complete before PII access is provisioned (IT does not grant PII access without DPO confirmation of training completion)

**For contractors and temporary workers**: minimum general privacy awareness is required. Where the contractor will handle elevated PII categories (special category data, financial PII, children's data), role-specific training is required before access is granted.

### 1.3 Annual Refresher Training

All personnel with PII access must complete privacy refresher training annually. The DPO coordinates with HR to run this as a coordinated campaign:

| Step | Action | Timing |
|------|--------|--------|
| 1 | DPO confirms training content is current — update if PIMS policies have changed materially | 8 weeks before refresher window |
| 2 | HR generates list of all personnel requiring refresher | 6 weeks before |
| 3 | Training assigned to all required personnel via LMS (or equivalent) | 4 weeks before |
| 4 | First reminder to those not yet completed | 2 weeks before deadline |
| 5 | Final reminder; escalation to line managers for non-completions | 1 week before deadline |
| 6 | DPO reviews completion report; escalates persistent non-completions to HR and line management | On deadline |
| 7 | 100% completion required; PII access suspension for any personnel not completing within 30 days of deadline | 30 days post-deadline |

### 1.4 Policy Update Notifications

When a PIMS policy is substantially revised or a new policy is issued:

1. DPO identifies which personnel are affected (which roles interact with the changed control group)
2. DPO prepares a summary communication explaining what changed and why
3. Communication is issued with a minimum 5 business days' notice before the policy's effective date
4. Affected personnel must acknowledge receipt and understanding (simple acknowledgment click in LMS or signed acknowledgment form)
5. Acknowledgment records are added to the Personnel Privacy Training and Acknowledgment Register

**Threshold for "substantial revision"**: Any change that affects what personnel are permitted or required to do in their handling of PII — a formatting change or minor clarification does not trigger a mandatory update notification.

### 1.5 Training Record Maintenance

The Personnel Privacy Training and Acknowledgment Register is maintained by DPO with HR support. Monthly, DPO reviews:

- Are all currently active personnel records up to date?
- Are any refresher dates upcoming within the next 60 days?
- Are there any personnel whose PII access was provisioned without confirmed training completion?

Records are retained for the duration of employment plus 3 years (per PRIV-POL-A.3.17-19).

---

## Part 2 — Confidentiality and Non-Disclosure Agreements (A.3.18)

### 2.1 Building the Confidentiality Agreement Register

The DPO maintains the Confidentiality Agreement Register — the authoritative record of all signed confidentiality or non-disclosure agreements covering PII protection. On initial setup:

1. Gather all existing employment contracts, contractor agreements, NDA templates from Legal and HR
2. Assess each contract type for PII-protective clause adequacy per PRIV-POL-A.3.17-19 (minimum content requirements)
3. For any contract type found to be inadequate: flag for amendment at next renewal or immediately for high-risk roles
4. Create a register entry per agreement type (or per individual agreement for standalone NDAs)
5. Record: party/category, mechanism type, execution date, review date, adequacy assessment

### 2.2 Executing Agreements for New Personnel and Parties

**Employees**: Privacy obligations should be embedded in the employment contract. Where an existing contract template does not meet the minimum PII content requirements:
- Legal updates the template for all new hires
- For existing staff: issue a supplementary privacy acknowledgment form to be signed

**Contractors**: All contractor agreements must include a privacy/confidentiality clause meeting minimum PII content before work commences. Procurement circulates the PRIV-IMP-A.3.17-19-TG clause checklist to Legal when reviewing new contractor agreements.

**Temporary workers**: If placed through a staffing agency, verify the agency agreement includes downstream NDA obligations. Where it does not, issue a standalone NDA before any PII access is granted.

**Processors**: Privacy confidentiality obligations are embedded in the Article 28 GDPR processor agreement — managed per PRIV-POL-A.2.2.2-7 and PRIV-POL-A.3.8-10.

### 2.3 Annual and Trigger-Based Agreement Review

**Annual review process**:

1. DPO reviews the Confidentiality Agreement Register for agreements approaching review date
2. For each agreement or agreement type due for review: confirm the obligations remain adequate given current regulatory requirements (any new GDPR/FADP guidance affecting confidentiality scope?)
3. For individual contracts materially changed (e.g., role changes resulting in access to new PII categories): initiate agreement refresh
4. Update register: new review date confirmed; amendments noted

**Trigger-based review** (in addition to annual):

| Trigger | Action |
|---------|--------|
| Material regulatory change affecting confidentiality obligations | Assess all agreement types; update templates; issue supplementary acknowledgment if substantive change |
| Personnel role change to elevated PII access (special category, large scale) | Confirm existing agreement scope covers new access; supplement if not |
| Party to agreement departs | Confirm post-termination obligations are recorded; retain signed agreement per retention schedule |
| Supplier/processor relationship ends | Confirm deletion/return obligations triggered; retain agreement per schedule |

### 2.4 Handling Gaps in Agreement Coverage

If the DPO discovers that a person or party with PII access does not have an adequate confidentiality agreement in place:

1. **Immediate**: Assess the risk — what PII did they access? Have obligations been communicated verbally or by policy?
2. **Urgent**: Issue an appropriate agreement for signature within 5 business days
3. **Suspend if necessary**: If the gap relates to ongoing PII access that cannot be adequately protected pending a signed agreement, suspend PII access until the agreement is executed
4. **Document**: Record the gap, the assessment, and the remediation action in the register

---

## Part 3 — Clear Desk and Clear Screen (A.3.19)

### 3.1 Establishing Clear Desk Rules

The DPO (working with CISO for technical controls) establishes clear desk rules for all PII processing environments. Privacy Champions are responsible for day-to-day enforcement in their business units.

**Initial setup**:

1. Identify all physical workspaces where PII is handled (offices, shared areas, home working environments)
2. Identify special risk areas (open-plan offices where screens may be visible to visitors; reception areas; meeting rooms with large display screens)
3. Issue clear desk rules as a short, practical workplace notice — see PRIV-IMP-A.3.17-19-TG for the recommended notice text
4. Communicate rules to all personnel as part of privacy awareness induction and annual refresher
5. Establish periodic workspace inspection schedule — minimum quarterly inspection in high-risk PII processing areas

### 3.2 Enforcing Clear Desk Rules

**Privacy Champions** perform clear desk inspections in their business unit:

| Inspection Frequency | Area Type | What to Check |
|---------------------|-----------|---------------|
| Quarterly (minimum) | Standard office — personnel with PII access | Desks clear of PII documents; shredding bins in place and not overflowing; removable media (USB, documents) not left unattended |
| Monthly (minimum) | High-risk areas (open plan, customer-facing, reception) | All above + screen visibility from visitor-accessible areas |
| After office hours (spot check) | All areas | PII documents on desks; unlocked cabinets |

Inspection results are recorded (see PRIV-IMP-A.3.17-19-TG for the Workspace Inspection Record template).

**Violation handling**:

| Severity | Example | Action |
|----------|---------|--------|
| Minor | PII document left on desk at end of day; screen not locked | Privacy Champion raises with individual; line manager notified; recorded informally |
| Moderate | Repeated minor violations; special category PII left unattended | Formal notice to individual; DPO notified; documented in inspection record |
| Serious | PII disclosure risk from unattended materials (e.g., visible to visitors, found in unsecured area) | DPO assesses as potential PII incident per PRIV-POL-A.3.11-12; line manager and HR notified |

### 3.3 Clear Screen Technical Controls

The CISO configures automatic screen locking for all workstations accessing PII systems. Minimum configuration standards are defined in PRIV-IMP-A.3.17-19-TG. DPO confirms annually with CISO that:

- Screen lock timeout settings meet or exceed the technical guide requirements
- Privacy screen filters are deployed in identified high-risk display environments
- Remote working device configurations match office standards

### 3.4 Remote Working Clear Desk and Screen

Personnel working remotely are subject to the same clear desk and clear screen rules as office-based workers. On commencement of remote working (permanent or habitual):

1. Personnel read and acknowledge the remote working annex of clear desk rules (see PRIV-IMP-A.3.17-19-TG)
2. Acknowledgment recorded in the Personnel Privacy Training and Acknowledgment Register
3. Privacy Champion may conduct remote working self-assessment where the DPO determines elevated risk (e.g., household members regularly present; role involves special category PII)

---

## Evidence Checklist

- [ ] Personnel Privacy Training and Acknowledgment Register — current, all active PII-handling personnel recorded
- [ ] Privacy training curriculum — version-controlled, reviewed within last 12 months
- [ ] New starter induction integration confirmed — training completed before PII access provisioned
- [ ] Annual refresher training completion — 100% completion recorded for current year
- [ ] Confidentiality Agreement Register — all agreement types assessed, review dates current
- [ ] Sample signed agreements — employment contracts, contractor NDAs, covering PII obligations
- [ ] Clear desk and clear screen rules — written and communicated to all personnel
- [ ] Workspace inspection records — quarterly (minimum) for standard areas; monthly for high-risk areas
- [ ] Screen lock configuration settings — documented, confirmed meeting TG specifications

---

<!-- QA_VERIFIED: [Date] -->
