# ISMS-INS-POL-01 — Implementation Guide
## POL-01: ISMS Governance and Decision-Making Framework

**Date:** 2026-02-17
**Purpose:** Practical implementation guide for organisations adopting POL-01
**Audience:** CISO, Implementation Lead, Consultant

---

## 1. What POL-01 Actually Does (Plain English)

POL-01 exists for one reason: **to shut down auditor scope creep.**

ISO 27001 certification involves two stages of professional judgment:
1. **Your judgment** — interpreting ISO 27001 for your context, selecting controls, defining evidence
2. **The auditor's judgment** — verifying your interpretation is reasonable and implemented

Without POL-01, the boundary between Stage 1 and Stage 2 is blurry. An OCD auditor can challenge your control design decisions during the audit, turning a verification exercise into a re-negotiation. POL-01 moves all of your professional judgment decisions into documented, signed, pre-audit artefacts. By the time the auditor arrives, every decision has a named authority, a competence record, and an approval signature. Their job shrinks to binary: did you follow your documented process? Yes or no.

**The complexity of POL-01 is the product. A simpler governance policy gives auditors more room to operate.**

---

## 2. What Needs to Change in Other Policies

### 2.1 Required Changes (Do These)

Only 4 policies need substantive updates. These are worth doing because they establish cross-references that auditors will expect to find when reviewing the governance framework.

#### POL-00 — Regulatory Applicability Framework
**Where:** Section 7 (Maintenance & Updates)
**What to add:** A subsection explaining that regulatory changes detected via POL-00 monitoring trigger the POL-01 change process (Section 5.2). Auditors will look for this link — without it, POL-00 monitoring and POL-01 change control look disconnected.

```markdown
### Change Management Integration

Regulatory changes detected through POL-00 monitoring trigger the compliance
criteria change process defined in ISMS-POL-01 (Section 5.2). Change impact
assessment, approval authority, and reassessment tracking follow the 6-step
process defined in POL-01 Section 5.2. Affected controls are reassessed within
90 days per POL-01 Section 5.4.
```

#### POL-A.5.1 — Policies for Information Security
**Where:** Section 1.3 or new Section 1.4
**What to add:** A governance boundaries reference. This is the umbrella policy for all Annex A controls — stating here that decision-making authority, exceptions, and change control are governed by POL-01 means you don't need to add it anywhere else.

```markdown
### Governance Framework

Decision-making authority for ISMS compliance interpretation, control exception
handling, and compliance criteria change control is governed by ISMS-POL-01
(ISMS Governance and Decision-Making Framework). All Annex A control policies
operate within the authority boundaries and processes defined in POL-01.
```

#### POL-A.5.31 — Legal, Statutory, Regulatory and Contractual Requirements
**Where:** Compliance Monitoring section
**What to add:** Governance authority reference linking compliance monitoring (POL-00) to exception handling and change control (POL-01). Auditors checking A.5.31 compliance will want to see how regulatory changes flow into the governance process.

#### POL-A.5.35-36 — Compliance Review / Independent Review
**Where:** Review process section
**What to add:** Reference to POL-01 Section 6.1 (annual governance review) as part of the independent review scope. This ensures governance effectiveness is explicitly within the audit scope.

---

### 2.2 Skip These (Not Worth Doing)

**Adding POL-01 to Related Documents in all 53 Annex A policies.**

The ISMS Copilot suggested this as Phase 3. Do not do it. Here is why:

- The relationship between POL-01 and all control policies is established by the ISMS structure, the SoA, and by POL-A.5.1 (the umbrella policy)
- Auditors do not verify governance by cross-checking 53 Related Documents lists
- 53 policy edits × maintenance overhead = perpetual debt whenever POL-01 changes
- Adding one line to each policy creates the illusion of integration without the substance

**If an auditor asks why POL-01 is not in the Related Documents of a specific control policy**, point them to POL-A.5.1 Section 1.X (the governance reference you added above). That is sufficient.

---

## 3. Operational Startup — What Must Exist Before Stage 2 Audit

This is where most organisations get caught. POL-01 defines processes. Processes need evidence. Here is the minimum viable evidence set for a first Stage 2 audit.

### 3.1 Must Have (Auditor will ask)

| Evidence | What it is | Who maintains it | Cadence |
|----------|-----------|-----------------|---------|
| **POL-00 monitoring logs** | Signed record that regulatory landscape was reviewed | Legal/Compliance + CISO | Quarterly (4 per year) |
| **Exception Register** | Log of controls that could not be implemented as written, with 5-step process documented | CISO | As exceptions arise |
| **Risk Acceptance Register** | Executive Management signatures on accepted risks | Executive Management | As decisions are made |
| **ISMS Change Log** | Record of compliance criteria changes with 6-step process | CISO | As changes occur |
| **Competence records** | Certifications / experience records for CISO, Legal/Compliance, DPO, Executive Management | HR / CISO | At role assignment |
| **Annual governance review minutes** | Meeting minutes showing 6 topics covered with Executive Management attendance | CISO | Annual |

### 3.2 Nice to Have (Strengthens position)

| Evidence | What it is |
|----------|-----------|
| Gap Register | Tracking reassessments after changes (POL-01 Section 5.4) |
| Lessons Learned Register | Governance improvement actions (POL-01 Section 6.2) |
| ISMS-CHK-POL-01 completed workbook | Quarterly governance self-assessment (20 requirements, GOV-01–GOV-20) |

### 3.3 What You Can Defer to Surveillance Audit

- Full ISMS-CHK-POL-01 quarterly assessment history (4 quarters)
- Complete Lessons Learned register with multiple entries
- Detailed Gap Register with >95% completion tracking

At the **initial certification audit**, auditors accept that processes are new. What they cannot accept is no evidence at all. Even one completed quarter of monitoring logs + an exception register with 0-3 entries beats nothing.

---

## 4. Implementation Observations

### 4.1 The Quarterly Monitoring Log is the Key Dependency

Everything in POL-01 ultimately connects to POL-00 quarterly monitoring. If the quarterly log exists and is signed by Legal/Compliance + CISO, it demonstrates:
- GOV-05 (Applicability Decisions domain) ✅
- That the organisation is actively maintaining regulatory awareness ✅
- That POL-01 Section 3 is operationally active ✅

Create a simple template for the monitoring log and complete it quarterly, even if the answer is "no changes detected." The signature is what matters.

### 4.2 The Exception Register is Your Safety Net

The 5-step exception process (POL-01 Section 4.2) is not bureaucracy — it is your documented justification for every control you could not or chose not to implement fully. Without it, an auditor can flag any gap as a nonconformity. With it, the same gap becomes a documented, risk-assessed, management-approved exception. That is the difference between a major nonconformity and an acceptable risk acceptance.

Start the register immediately, even if empty. An empty register with the right structure beats no register.

### 4.3 Executive Management Signatures Are Non-Negotiable

ISO 27001 Clause 6.1.3d explicitly requires management approval for risk acceptance decisions. POL-01 formalises this through the Risk Acceptance Register. If you cannot get Executive Management to sign the register, you cannot complete risk treatment, and you cannot get certified. This is the one process where there is no workaround — get the signatures.

### 4.4 The Change Log Is Easy to Forget

The 6-step change process (POL-01 Section 5.2) only activates when compliance criteria change — which may not happen often. The risk is forgetting to log a change when it does happen (new regulation, audit feedback, significant threat). Designate the CISO as the log owner and add "check change log" as a standing agenda item on the annual governance review.

### 4.5 Do Not Over-Engineer the Governance Review

POL-01 Section 6.1 requires an annual governance review covering 6 topics. This does not need to be a formal board meeting. A documented 2-hour session with the CISO and one Executive Management representative, with minutes covering the 6 topics, satisfies the requirement. A one-page set of minutes beats an elaborate process that never happens.

---

## 5. Minimum Viable Implementation Sequence

For an organisation implementing POL-01 from scratch, in order:

1. **Approve and sign POL-01** — CISO drafts, Legal/Compliance reviews, Executive Management approves
2. **Create competence records** — document that CISO, Legal/Compliance, DPO meet Section 2.3 criteria
3. **Create the Exception Register** — template only, even if empty
4. **Create the Risk Acceptance Register** — template only, even if empty
5. **Create the ISMS Change Log** — template only, even if empty
6. **Complete first POL-00 quarterly monitoring log** — even one quarter
7. **Update POL-00 Section 7** — add change management integration reference
8. **Update POL-A.5.1** — add governance framework reference
9. **Schedule annual governance review** — put it in the calendar now
10. **Generate ISMS-CHK-POL-01 workbook** — run script, complete one assessment cycle

Steps 1-6 are prerequisites for Stage 2 audit. Steps 7-10 strengthen the position.

---

## 6. File Locations

| Document | Location |
|----------|---------|
| POL-01 policy | `POL/ISMS-POL-01 - ISMS Governance and Decision-Making Framework.md` |
| Assessment workbook generator | `SCR/ISMS-SCR-CHK-POL-01.py` |
| Generated assessment workbook | `WKBK/ISMS-CHK-POL-01_...xlsx` |
| This implementation guide | `INS/ISMS-INS-POL-01-Implementation-Guide.md` |
| Copilot cross-reference analysis | `96-isms-core-audit-reports/.../isms-copilot-pol-01-referencing-instructions.md` |

---

<!-- QA_VERIFIED: 2026-02-17 -->
