# ISMS-INS-POL-00 — Implementation Guide
## POL-00: Regulatory Applicability Framework

**Date:** 2026-02-17
**Purpose:** Practical implementation guide for organisations adopting POL-00
**Audience:** CISO, Legal/Compliance Officer, DPO, Implementation Lead

---

## 1. What POL-00 Actually Does (Plain English)

POL-00 answers one question: **which regulations apply to this organisation, and with what force?**

Without it, every ISMS policy author decides independently whether to reference GDPR, DORA, FINMA, or NIST. The result is inconsistency — some policies cite regulations that don't apply, others miss regulations that do, and auditors spend Stage 1 untangling the mess.

POL-00 solves this by establishing three tiers once, centrally:

- **Tier 1 (Mandatory)** — applies regardless of business activity. Non-negotiable.
- **Tier 2 (Conditional)** — applies only if specific business triggers are met. Requires a deliberate determination.
- **Tier 3 (Informational)** — best practice reference only. No compliance obligation.

All 53 Annex A control policies then inherit this categorisation by reference to POL-00. The Tier determination is made once, by Legal/Compliance, and all policies use that determination consistently.

**The operational value**: when a new regulation emerges, you update POL-00 (one document), and the change propagates logically to all control policies. You do not touch 53 policies individually.

---

## 2. The Hard Part: Making the Tier 2 Determinations

Tier 1 is straightforward for a Swiss organisation — nFADP and ISO 27001 are effectively mandatory if you are pursuing certification and operating in Switzerland. GDPR is mandatory if you process personal data of EU residents (for most Swiss organisations, the answer is yes).

**Tier 2 is where the real work is.** These determinations require judgment, legal knowledge, and honest assessment of the organisation's business model. Getting them wrong has consequences in both directions:

- **Over-applying** (applying Tier 2 when trigger not met): unnecessary compliance overhead, gold-plating, cost without benefit
- **Under-applying** (missing a trigger that is met): regulatory exposure, potential enforcement action, audit nonconformity

### Tier 2 Decision Checklist

Work through each regulation in order. For each, answer the trigger question honestly. If uncertain, Legal/Compliance makes the determination and documents the reasoning.

---

#### FINMA (Swiss Financial Market Supervisory Authority)

**Trigger question:** Is the organisation a FINMA-supervised entity?

FINMA-supervised entities include: banks, insurance companies, securities firms, stock exchanges, fund management companies, collective investment schemes, financial market infrastructures, payment service providers regulated under FinSA/FinIA.

| Answer | Tier | Action |
|--------|------|--------|
| Yes — directly supervised by FINMA | Tier 2 Active | Apply FINMA Circular 2023/1 requirements; document in SoA |
| Yes — ICT service provider to FINMA entity | Tier 2 Active | FINMA outsourcing rules apply; assess sub-outsourcing requirements |
| No | Tier 2 Not Active | Document "not a FINMA-supervised entity" in Regulatory Applicability Matrix |

**Common mistake:** SMEs that provide IT services to banks assume FINMA does not apply. If the bank classifies your service as material outsourcing under FINMA Circular 2023/1, FINMA requirements flow through contractually. Check the master services agreement.

---

#### DORA (Digital Operational Resilience Act)

**Trigger question:** Is the organisation a financial entity or ICT third-party service provider (ITSP) to EU financial entities?

EU financial entities under DORA include: banks, insurance companies, investment firms, payment institutions, electronic money institutions, crypto-asset service providers, and others. DORA's ITSP provisions apply to providers of critical or important ICT services to these entities.

| Answer | Tier | Action |
|--------|------|--------|
| EU financial entity | Tier 2 Active | Full DORA applicability including TLPT testing |
| ICT service provider designated as critical/important by financial entity | Tier 2 Active | DORA Chapter V (oversight framework) applies |
| ICT service provider — not yet designated | Tier 2 Watch | Monitor; determine if contractual DORA requirements flow through client agreements |
| No connection to EU financial entities | Tier 2 Not Active | Document determination; review annually |

**DORA effective date:** 17 January 2025. If Tier 2 Active, requirements should already be in place or being implemented.

**Common mistake:** Swiss ICT providers to EU banks assume DORA does not apply because they are not EU-based. DORA's extraterritorial reach covers non-EU ICT providers serving EU financial entities. Check your client list.

---

#### NIS2 (Network and Information Security Directive 2)

**Trigger question:** Does the organisation operate in a sector listed in NIS2 Annex I or II, and meet the size threshold?

NIS2 applies to **Essential Entities** (Annex I: energy, transport, banking, health, water, digital infrastructure, public administration, space) and **Important Entities** (Annex II: postal services, waste management, food, manufacturing, digital providers, research).

Size threshold: medium enterprises (50+ employees OR €10M+ annual turnover) in covered sectors. Smaller entities only if specifically designated by Member State.

| Answer | Tier | Action |
|--------|------|--------|
| In-scope sector + meets size threshold | Tier 2 Active | NIS2 cybersecurity risk measures (Article 21) and incident reporting (Article 23) apply |
| In-scope sector + below threshold | Tier 2 Watch | Monitor; Member States may extend scope |
| Out-of-scope sector | Tier 2 Not Active | Document determination |

**For Swiss organisations:** NIS2 is EU law. It applies directly only if the organisation has EU operations or provides services to EU in-scope entities. Switzerland has its own revision of ISSG (Informationssicherheitsgesetz) — assess both.

---

#### PCI DSS v4.0.1

**Trigger question:** Does the organisation store, process, or transmit cardholder data (payment card numbers, CVV, PINs)?

This is binary. There is no threshold — any organisation that touches card data is in scope.

| Answer | Tier | Action |
|--------|------|--------|
| Yes — any card data handled | Tier 2 Active | Determine SAQ level; apply relevant requirements to cardholder data environment (CDE) |
| No — outsourced entirely to PSP (e.g., Stripe, PayPal), no card data touches own systems | Tier 2 Reduced | SAQ-A scope only; verify tokenisation/redirect approach |
| No card processing at all | Tier 2 Not Active | Document determination |

**Common mistake:** Assuming that using a payment processor removes all PCI DSS obligation. If your systems redirect to a hosted payment page and never see card data, SAQ-A applies (simplified). If your systems ever see card data in transit, full scope applies.

---

#### EU AI Act

**Trigger question:** Does the organisation develop, deploy, or use AI systems within the EU?

| Answer | Tier | Action |
|--------|------|--------|
| Develops or deploys prohibited AI systems | Not permitted | Full stop |
| Develops or deploys high-risk AI (Annex III) | Tier 2 Active | Conformity assessment, registration, technical documentation required |
| Deploys general-purpose AI in high-risk context | Tier 2 Active | Obligations under Article 50 (transparency) and use-case assessment |
| Uses AI tools (e.g., Microsoft Copilot, ChatGPT) as deployer | Tier 2 Watch | Monitor; transparency and human oversight obligations apply |
| No AI development or deployment | Tier 2 Not Active | Document; review annually — AI adoption changes rapidly |

**Timeline note:** High-risk AI obligations phased in from August 2025. Prohibited AI provisions active from February 2025. Compliance dates are moving targets — check delegated acts publication schedule.

---

#### HIPAA / FISMA / CCPA (US Federal / State)

These apply only if the organisation:
- Processes protected health information of US persons (HIPAA)
- Is a US federal agency or federal contractor (FISMA)
- Collects personal data of California residents and meets revenue/data volume thresholds (CCPA)

For most Swiss-based organisations without US operations, these are **Tier 3 (Informational)**. Document the determination. Review if US market expansion is planned.

---

## 3. First-Time Setup — Completing the Regulatory Applicability Matrix

The Regulatory Applicability Matrix (POL-00 Section 8.2) is the formal record of Tier determinations. Before completing it, answer these organisation-level questions:

**About the organisation:**
1. Registered in Switzerland? (nFADP = Tier 1)
2. Processes personal data of EU residents? (GDPR = Tier 1 or Tier 2 depending on volume/nature)
3. FINMA-supervised entity or material IT service provider to one? (FINMA Tier 2)
4. Provides ICT services to EU financial entities? (DORA Tier 2)
5. Operates in NIS2 Annex I/II sector with 50+ employees or €10M+ turnover? (NIS2 Tier 2)
6. Stores, processes, or transmits payment card data? (PCI DSS Tier 2)
7. Develops, deploys, or uses AI systems in EU? (EU AI Act Tier 2 Watch/Active)
8. Any US health data, federal contracts, or California customer base? (HIPAA/FISMA/CCPA Tier 2 or 3)

**Sequence:**
1. CISO and Legal/Compliance work through the checklist above together
2. Legal/Compliance makes the Tier 2 determinations and documents reasoning
3. DPO validates privacy-related determinations (GDPR, nFADP, EU AI Act)
4. Matrix is completed with Tier + determination rationale for each regulation
5. Executive Management approves the completed matrix
6. Matrix is dated and signed — this becomes the audit evidence for Stage 1

**The matrix does not need to be perfect.** It needs to be deliberate. An auditor will accept a reasoned determination that DORA does not apply, supported by a documented assessment of the client base. They will not accept "we didn't think about it."

---

## 4. The Quarterly Monitoring Log (In Practice)

POL-00 Section 4.3 requires quarterly monitoring of the regulatory landscape. This is the evidence that the Tier determinations are being kept current.

**What monitoring actually means:**

It does not mean hiring a legal team to conduct regulatory research every quarter. It means:

1. Reviewing a curated set of regulatory monitoring sources (POL-00 Appendix — Regulatory Monitoring Sources)
2. Confirming whether any material regulatory developments occurred in the quarter
3. Assessing whether any developments affect current Tier determinations
4. Documenting the review and signing off

**Template for a typical quarterly log entry (nothing changed):**

```
REGULATORY MONITORING LOG — Q[X] [YEAR]
Period: [DD.MM.YYYY] to [DD.MM.YYYY]

Monitoring Sources Reviewed:
☑ EDÖB (Federal Data Protection Commissioner) — news and guidance
☑ FINMA — circulars and guidance updates
☑ EUR-Lex / Official Journal EU — DORA/NIS2/AI Act implementation acts
☑ PCI Security Standards Council — DSS updates
☑ ENISA — NIS2 implementation guidance

Findings:
No material regulatory developments affecting current Tier 1/2/3 determinations
were identified in this quarter.

Triggered Assessment Required: No

Reviewed by: [Legal/Compliance Officer name]          Date: [DD.MM.YYYY]
Confirmed by: [CISO name]                              Date: [DD.MM.YYYY]
```

**If something changed:** Document the change, assess which Tier determinations or control policies are affected, trigger the POL-01 Section 5.2 change process, and record the triggered assessment reference.

**The most important thing about the log:** Do it on the same date each quarter. Set a calendar recurring appointment. A log that is consistently dated (end of March, June, September, December) looks deliberate. A log with irregular dates looks retrofitted.

---

## 5. Triggered Assessments — When to Reassess Mid-Quarter

The following business events should trigger an immediate reassessment outside the quarterly cycle (POL-00 Section 5):

| Event | What to Assess |
|-------|---------------|
| Entering a new market (EU, US, etc.) | New regulatory obligations in that jurisdiction |
| Acquiring or merging with another entity | Target entity's regulatory obligations carry over |
| Launching a new product handling personal data | GDPR/nFADP scope, AI Act if AI-enabled |
| Starting to process payment card data | PCI DSS trigger |
| Winning a contract with an EU financial entity | DORA ITSP provisions |
| Reaching 50 employees or €10M turnover | NIS2 size threshold crossed |
| Material regulatory update (enforcement action, new guidance) | Affected Tier determination |

Triggered assessments use the same assessment methodology as the quarterly review but are documented separately. Reference the trigger event, the assessment outcome, and whether a POL-01 change process was initiated.

---

## 6. Connections to Other Documents

**→ POL-01 (ISMS Governance and Decision-Making Framework)**
POL-00 generates the *what* (which regulations apply). POL-01 governs the *process* for changing that determination. When a quarterly monitoring log identifies a material regulatory change, the POL-01 Section 5.2 six-step change process is triggered. The two policies work as a pair.

**→ Statement of Applicability (SoA)**
Tier 1 and Tier 2 Active determinations directly influence SoA control selections. DORA active → resilience controls (A.5.29, A.5.30, A.8.13, A.8.14) are likely mandatory. PCI DSS active → encryption and access controls (A.8.24, A.8.2, A.5.15) get additional justification. The SoA should reference POL-00 as a source of control inclusion rationale.

**→ Annex A Control Policies**
Control policies do not need to individually enumerate every applicable regulation. They reference POL-00 for the regulatory framework and cite specific regulations only where the regulation drives a specific control requirement (e.g., GDPR Article 32 in A.8.24 encryption policy).

**→ ISMS-CHK-POL-00 (if created)**
A compliance assessment workbook for POL-00 would verify GOV-05 through GOV-08 in the ISMS-CHK-POL-01 workbook — specifically that quarterly monitoring is done, triggered assessments are documented, and SoA justifications are complete. POL-00 does not currently have its own assessment workbook; these requirements are assessed via ISMS-CHK-POL-01.

---

## 7. Evidence for Auditors

### Stage 1 (Documentation Review)

The auditor wants to see that regulatory obligations are explicitly identified and categorised. Evidence:

- [X] POL-00 v1.0 — approved, signed, dated
- [X] Regulatory Applicability Matrix (Section 8.2) — completed with Tier determinations and rationale for each regulation
- [X] Tier 2 determination documentation — written justification for Active/Not Active decisions for each conditional regulation
- [X] Approval signatures — CISO, Legal/Compliance, DPO, Executive Management

**What Stage 1 auditors catch:** Missing or vague Tier 2 determinations ("DORA — under review"), unsigned matrices, inconsistency between POL-00 Tier determinations and SoA control selections.

### Stage 2 (Operational Effectiveness)

The auditor wants to see that POL-00 is actually being maintained. Evidence:

- [X] Quarterly monitoring logs — minimum 4 quarters (or since ISMS inception if less than a year)
- [X] Each log signed by Legal/Compliance + CISO
- [X] At least one triggered assessment record (if a relevant business event occurred)
- [X] Evidence that SoA was updated following any Tier determination change

**What Stage 2 auditors catch:** Quarterly logs that look templated but not genuinely reviewed (identical text across all 4 quarters with no variation), missing signatures, no response to known regulatory developments (e.g., DORA effective date passes but no log entry acknowledges it).

---

## 8. Implementation Observations

### 8.1 The "Nothing Changed" Quarter Is Fine — But Vary the Language

Four identical quarterly log entries with copy-pasted text looks like a checkbox exercise. Auditors notice. Even when nothing substantive changed, vary what was reviewed, note specific guidance documents checked, and call out any developments that were assessed and deemed immaterial.

### 8.2 GDPR and nFADP Overlap — Handle Once, Not Twice

For Swiss organisations processing EU personal data, both GDPR and nFADP apply. They have overlapping but not identical requirements. The safest approach: implement to the stricter standard for each specific requirement (usually GDPR). Document this in the Regulatory Applicability Matrix. Do not write two separate compliance programmes — that creates inconsistency and confusion.

### 8.3 Tier 2 "Watch" Is a Legitimate Status

Not every Tier 2 regulation is binary Active/Not Active. "Watch" (monitoring the situation without full compliance obligations) is appropriate for:
- DORA when serving financial entities through intermediaries (unclear exposure)
- EU AI Act where AI tools are used but the full risk classification is being assessed
- NIS2 where you are close to but not clearly over the size threshold

Document the Watch rationale. Set a review trigger. Do not leave Watch entries indefinitely — they should resolve to Active or Not Active within 12 months.

### 8.4 The Regulatory Landscape Is Moving Fast (2025-2026)

Three major Tier 2 regulations are in active implementation phase:
- **DORA** — effective 17 January 2025, enforcement beginning
- **EU AI Act** — prohibited AI February 2025, high-risk AI from August 2025
- **NIS2** — transposition deadline October 2024, enforcement varying by Member State

The quarterly monitoring log will likely have genuine content for the next 2-3 years just from these three. Do not treat monitoring as a formality during this period.

### 8.5 The Regulatory Applicability Matrix Is an Audit Anchor

Auditors at Stage 1 will spend significant time on POL-00 because it underpins every other policy's regulatory references. A well-completed matrix — with explicit determinations, signed rationale, and clear Tier assignments — creates a strong first impression and pre-empts detailed questioning on individual control policies.

Invest time in getting the matrix right. It pays dividends across the entire audit.

---

## 9. Minimum Viable Implementation Sequence

1. **Answer the 8 organisation-level questions** (Section 3) — CISO + Legal/Compliance together
2. **Complete the Regulatory Applicability Matrix** — Tier 1 first, then Tier 2 determinations with written rationale
3. **DPO validates privacy determinations** — GDPR, nFADP, EU AI Act sections
4. **Executive Management approves and signs the matrix**
5. **Approve and sign POL-00 itself** — full approval chain (CISO → Legal/Compliance → DPO → Executive Management)
6. **Complete first quarterly monitoring log** — even one quarter before Stage 1 audit
7. **Cross-reference SoA** — confirm control selections reflect Tier 1/2 Active determinations
8. **Update POL-00 Section 7** — add POL-01 change management integration text (see POL-01 INS guide)
9. **Schedule quarterly monitoring** — recurring calendar appointment, same dates each quarter

Steps 1-6 are the minimum for Stage 1 audit readiness. Steps 7-9 complete the integration.

---

## 10. File Locations

| Document | Location |
|----------|---------|
| POL-00 policy | `POL/ISMS-POL-00 - Regulatory Applicability Framework.md` |
| This implementation guide | `INS/ISMS-INS-POL-00-Implementation-Guide.md` |
| POL-01 implementation guide | `../isms-pol-01-.../INS/ISMS-INS-POL-01-Implementation-Guide.md` |
| Copilot cross-reference analysis | `96-isms-core-audit-reports/.../isms-copilot-pol-01-referencing-instructions.md` |
| Regulatory reference documents | `isms-ref-dora/`, `isms-ref-eu-ai-act/`, etc. |

---

<!-- QA_VERIFIED: 2026-02-17 -->
