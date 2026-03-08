<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Paradigm_Guide-2E8B57?style=for-the-badge" alt="ISMS CORE Paradigm Guide"/>
</p>

<h1 align="center">🧭 Understanding the Paradigm</h1>

<p align="center">
  <strong>Why ISMS CORE is engineered differently — and how to choose between its products</strong>
</p>

<p align="center">
  <a href="https://www.iso.org/standard/27001"><img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square&logo=iso&logoColor=white" alt="ISO 27001:2022"/></a>
  <a href="#framework-sse--secure-systems-engineering"><img src="https://img.shields.io/badge/🏗️_FRAMEWORK-SSE_Engineering-9400D3?style=flat-square" alt="FRAMEWORK SSE"/></a>
  <a href="#operational-foundation-isms-for-smes"><img src="https://img.shields.io/badge/⚡_OPERATIONAL-SME_Foundation-FF6600?style=flat-square" alt="OPERATIONAL"/></a>
  <a href="PHILOSOPHY.md"><img src="https://img.shields.io/badge/Anti--Cargo--Cult-Engineering-DC143C?style=flat-square" alt="Anti-Cargo-Cult"/></a>
</p>

<p align="center">
  <em>Grows fast. Bends, doesn't break. Built to last.</em> 🎋
</p>

---

> **TL;DR for people who skim:**
> - ISMS CORE moves compliance judgment from audit time to design time — policies state explicit, testable requirements; auditors verify documented decisions rather than making them for you
> - Two content products: **Framework** (full SSE engineering, regulated industries, multi-framework) and **Operational** (SME-focused, ISO 27001 + GDPR, practical checklists)
> - Both cover all 93 ISO 27001:2022 Annex A controls in 53 control packs
> - A **Platform** (WebUI + API) sits on top and turns the static files into a live compliance management system
> - Self-hosted, on-premises by design — your compliance evidence stays under your control and jurisdiction
> - This is not plug-and-play. You need a qualified CISO, Python execution capability, and willingness to make documented decisions

---

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
> — Richard Feynman

> *"A scientific revolution occurs when an old paradigm can no longer accommodate the anomalies that have accumulated within it."*
> — Thomas Kuhn, *The Structure of Scientific Revolutions*

---

## A Note on the Word "Paradigm"

Kuhn reserved "paradigm shift" for moments when an entire discipline restructures around a new framework — when accumulated anomalies make the old model untenable and a new one replaces it. This is not that.

ISO 27001 is not broken. Certification bodies still audit using the same Annex A criteria. The standard's language — "appropriate controls", "adequate measures" — has not changed. ISMS CORE works entirely within ISO 27001:2022, not outside it.

But within the domain of ISMS *implementation*, there is a genuine architectural choice about **where professional judgment is applied** — at design time or at audit time. That choice has real consequences for how evidence is produced, how audits unfold, and whether compliance represents actual security or compliance theater. That is what this document describes.

---

## 🎯 What Is ISMS CORE?

<p>
<img src="https://img.shields.io/badge/🏗️_FRAMEWORK-SSE_Engineering-9400D3?style=flat-square" alt="FRAMEWORK"/>
<img src="https://img.shields.io/badge/⚡_OPERATIONAL-SME_Foundation-FF6600?style=flat-square" alt="OPERATIONAL"/>
<img src="https://img.shields.io/badge/Controls-93_Annex_A-32CD32?style=flat-square" alt="93 Controls"/>
</p>

ISMS CORE provides **two distinct ISMS implementations** designed for different organisational needs:

- **FRAMEWORK (SSE — Secure Systems Engineering)**: Engineered compliance system for regulated industries with complex multi-regulatory requirements
- **OPERATIONAL**: Classical ISMS for SMEs seeking ISO 27001 certification with automation-assisted compliance

Both variants use code-driven, evidence-automated, engineer-designed approaches. If you are looking for Word document templates, generic guidance like "implement appropriate security measures", or annual compliance snapshots with manual evidence collection — this is not the right tool for you.

---

## 📊 Traditional ISMS vs. ISMS CORE

<p>
<img src="https://img.shields.io/badge/Judgment-At_Design_Time-00AA00?style=flat-square" alt="Design Time"/>
<img src="https://img.shields.io/badge/Evidence-Automated-0066CC?style=flat-square" alt="Automated"/>
<img src="https://img.shields.io/badge/Requirements-Testable-DC143C?style=flat-square" alt="Testable"/>
</p>

| Aspect | Traditional ISMS | ISMS CORE (Both Variants) |
|--------|-----------------|---------------------------|
| **Documentation Format** | Word/PDF documents, manual templates | Markdown policies + Python scripts + generated workbooks |
| **Evidence Collection** | Manual gathering (screenshots, logs, approvals) | Structured workbook generation (FRAMEWORK: control-derived assessment workbooks completed manually against system state; OPERATIONAL: policy-derived compliance checklists) |
| **Requirements Specificity** | "Regular backups", "Appropriate encryption" | "AES-256 encrypted backups, verified quarterly via assessment workbook" (testable, measurable) |
| **Professional Judgment Location** | Audit discussion (auditor interprets "adequate") | Model design (organisation documents interpretation, auditor verifies) |
| **Compliance Verification** | Annual snapshot (point-in-time assessment) | Periodic verification (workbooks regenerated on demand, completed by assessor on defined schedule) |
| **Policy Updates** | Manual document revision, version control in filenames | Version-controlled Markdown, regenerable workbooks that stay in sync with policy |
| **Exception Handling** | Ad-hoc discussions with auditors | Structured process (FRAMEWORK: POL-01 5-step; OPERATIONAL: embedded in control policies) |
| **Regulatory Applicability** | Ambiguous ("We comply with GDPR where applicable") | Explicit (FRAMEWORK: POL-00 Tier 1/2/3; OPERATIONAL: focused scope in control policies) |
| **Audit Preparation** | Weeks of effort gathering evidence that should already exist | Hours to assemble — provided assessments have been completed on schedule (workbooks pre-generated, evidence pre-documented) |
| **Control Implementation Evidence** | "We have a firewall" (trust us) | Assessment workbook showing compliance status per requirement, last assessed date, supporting documentation (verify yourself) |

---

## ⚙️ The Paradigm Shift: Where Does Professional Judgment Live?

This is the core idea behind ISMS CORE. In a traditional ISMS, professional judgment often happens during the audit — the auditor decides what's "adequate." In ISMS CORE, professional judgment happens during policy design — the organisation decides, documents it explicitly, and the auditor verifies the documented decision.

### ❌ Traditional ISMS (Judgment During Audit)

1. Write policy: "Backups shall be encrypted with appropriate algorithms"
2. Implement: Install backup system, enable encryption
3. Audit time:
   - Auditor: "What algorithm?"
   - You: "Whatever the vendor default is"
   - Auditor: "Is that appropriate?"
   - You: "We think so?"
   - Auditor: *[Writing finding]* "Encryption adequacy not documented"
4. Result: Finding raised, remediation required, policy rewrite, re-evidence

### ✅ ISMS CORE (Judgment During Model Design)

1. Write policy: "Backups shall be encrypted using AES-256 minimum, tested quarterly for restore capability"
2. Implement: Configure backup system, document configuration, record algorithm in use
3. Build assessment: Python script generates structured workbook with explicit requirements from policy scope — assessor marks each item Compliant / Partial / Non-Compliant / N/A and records supporting evidence (configuration extract, last test date, restore result)
4. Audit time:
   - Auditor: "Show me backup encryption compliance"
   - You: "Here's the completed assessment workbook, the policy it was assessed against, and the configuration evidence. Algorithm documented as AES-256 in both."
   - Auditor: *[Reviews workbook and evidence]* "...compliant."
5. Result: No finding raised on this control. Audit progresses.

**The difference:** The question "What algorithm? Is that appropriate?" was answered **during policy design** (CISO documented "AES-256 minimum") and verified **during assessment** (workbook confirms alignment). The auditor verifies the quality of that documented decision — they do not make the decision for you.

---

## 🔀 Two Variants: Choose Based on Your Needs

### ⚡ OPERATIONAL (Foundation ISMS for SMEs)

<p>
<img src="https://img.shields.io/badge/Target-SME_/_Startup-FF6600?style=flat-square" alt="SME"/>
<img src="https://img.shields.io/badge/Effort-3–6_months-FFD700?style=flat-square" alt="3-6 months"/>
<img src="https://img.shields.io/badge/Regulatory-ISO_27001_+_nFADP-0066CC?style=flat-square" alt="ISO 27001"/>
<img src="https://img.shields.io/badge/Python-Basic-32CD32?style=flat-square" alt="Basic Python"/>
</p>

**For whom:**
- Small to medium enterprises seeking ISO 27001 certification
- Organisations with focused regulatory scope (ISO 27001 + Swiss nFADP + GDPR conditionally)
- Teams wanting classical ISMS structure with automation benefits

**What you get:**
- **Architecture**: OP-POL (policy) → Python Script (workbook generator) → Assessment Workbook (compliance checklist)
- **Coverage**: 53 control packs covering all 93 Annex A controls
- **Automation**: Python-generated Excel compliance checklists reflecting requirements defined in OP-POL
- **Evidence**: Quarterly/annual compliance assessments via workbooks, completed manually by assessor
- **Methodology**: Classical ISMS structure with 1:1 policy stacking (related controls share policies)
- **Regulatory support**: ISO 27001:2022 + Swiss nFADP + GDPR (when applicable)
- **Governance**: Embedded in control policies (no separate POL-00/POL-01 meta-layer)

**How the workbook is built:**

Each OP-POL is written to address the control's objectives proportionate to SME context and scope. The Python script generates a structured assessment workbook whose requirements correspond to the OP-POL — because the script was authored to reflect those requirements, not because it parses the policy at runtime. The workbook is **policy-derived**: the OP-POL is the source of truth. The assessor completes the workbook manually, marking each requirement Compliant / Partial / Non-Compliant / N/A and recording supporting evidence.

**Statement of Applicability (SoA):** The SoA is a mandatory certification artefact under ISO 27001:2022 Clause 6.1.3(d). ISMS CORE does not generate the SoA automatically — it is an organisational decision document that maps control applicability to your context, exclusions, and justifications. The 53 control packs (covering 93 Annex A controls) provide the structured input for producing your SoA; the organisation is responsible for completing it. If you are new to ISMS, ensure your implementation includes SoA guidance from a qualified practitioner.

**Prerequisites:**
- Basic Python execution capability (run scripts to generate checklists)
- Understanding of ISO 27001 Annex A controls
- Willingness to document decisions explicitly (testable requirements, not vague statements)
- Quarterly assessment discipline (complete workbooks, track compliance)

**Best for:** "We need ISO 27001 certification, we want automation help with compliance tracking, but we don't need multi-regulatory governance complexity."

---

### 🏗️ FRAMEWORK (SSE — Secure Systems Engineering)

<p>
<img src="https://img.shields.io/badge/Target-Regulated_Industries-9400D3?style=flat-square" alt="Regulated"/>
<img src="https://img.shields.io/badge/Effort-6–12_months-FF4500?style=flat-square" alt="6-12 months"/>
<img src="https://img.shields.io/badge/Regulatory-Multi--Framework-DC143C?style=flat-square" alt="Multi-Framework"/>
<img src="https://img.shields.io/badge/Python-Intermediate-0066CC?style=flat-square" alt="Intermediate Python"/>
</p>

**For whom:**
- Regulated industries (financial services, healthcare, critical infrastructure)
- Organisations with complex multi-regulatory requirements (GDPR + DORA + NIS2 + PCI DSS + FINMA)
- Technical teams comfortable with comprehensive, evidence-driven compliance work and Python-generated assessment tooling

**What you get:**
- **Foundation Governance**:
  - **POL-00** (Regulatory Applicability Framework): Tier 1/2/3 categorisation, quarterly monitoring, triggered assessments
  - **POL-01** (ISMS Governance Framework): Authority boundaries, competence requirements, 5-step exception process, 6-step change control, internal Challenge Protocol
- **Architecture**: POL (policy) → IMP (implementation spec) → Python (workbook generator) → Workbook (evidence)
- **Per control pack**: POL + IMP (UG/TG) + SCR + WKBK + REF + FORM + INS + CTX
- **Coverage**: 53 control packs covering all 93 Annex A controls. Score 4–5 controls have the most structured, comprehensive workbooks with the most objective measurable criteria. Score 1–3 controls use workbooks scaled to the control's inherent measurability.
- **Evidence**: Structured assessment workbooks generated by Python scripts, completed periodically by the assessor. Score reflects workbook depth and evidence objectivity, not automation of infrastructure queries.
- **Methodology**: Score 1–5 system (see below)
- **Regulatory support**: Multi-framework (ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA)

**How the workbook is built:**

FRAMEWORK workbooks are **control-derived**: built directly and comprehensively against every area the control addresses, covering the full scope of what ISO 27001 requires. The POL itself is written to the same scope. Policy and workbook are co-designed against the control requirements, not filtered through SME proportionality. The result is a more exhaustive, structured assessment than the OPERATIONAL equivalent. The assessor completes each workbook manually, marking requirements Compliant / Partial / Non-Compliant / N/A and attaching supporting evidence (configurations, certificates, logs, approvals). Auditors verify the completed workbook and supporting documentation against the stated policy requirements.

**Prerequisites:**
- Python 3.11+ execution capability (run scripts to generate workbooks)
- Understanding of ISO 27001 Annex A controls and SSE methodology
- Technical team willing to complete structured assessments with supporting evidence
- Appetite for comprehensive, evidence-driven compliance (not checkbox compliance)

**The Score 1–5 System (FRAMEWORK only):**

<p>
<img src="https://img.shields.io/badge/Score_5-Highest_Objectivity-00AA00?style=flat-square" alt="Score 5"/>
<img src="https://img.shields.io/badge/Score_4-High_Objectivity-32CD32?style=flat-square" alt="Score 4"/>
<img src="https://img.shields.io/badge/Score_3-Moderate-FFD700?style=flat-square" alt="Score 3"/>
<img src="https://img.shields.io/badge/Score_2-Lower-FF6600?style=flat-square" alt="Score 2"/>
<img src="https://img.shields.io/badge/Score_1-Attestation--Based-DC143C?style=flat-square" alt="Score 1"/>
</p>

Each Annex A control is scored on **evidence objectivity** — the score reflects how directly and measurably a control's requirements can be verified, and therefore how comprehensive and objective the generated workbook can be. This is a scoring of evidence quality, not an organisational principle; both Framework and Operational use the same A.5/A.6/A.7/A.8 structure with 53 control packs.

- **Score 5**: Highest evidence objectivity (log retention, backup status, algorithm in use — requirements are directly measurable, pass/fail criteria are unambiguous)
- **Score 4**: High evidence objectivity (access review, patch compliance — most requirements are objectively verifiable, small proportion requires human judgment)
- **Score 3**: Moderate evidence objectivity (incident response — process and outcomes can be documented and tracked, but not fully reduced to pass/fail)
- **Score 2**: Lower evidence objectivity (security training, supplier reviews — human judgment is central, evidence is attestation-based)
- **Score 1**: Lowest evidence objectivity (physical security, HR processes — assessment relies primarily on observation and attestation)

FRAMEWORK prioritises rigour across all scores. Higher-score controls produce workbooks with more objective, measurable criteria. Lower-score controls produce workbooks that are still comprehensive and structured, but rely more on assessor judgment and supporting documentation. The score describes the **control's inherent measurability**, not the script's current capabilities.

**Best for:** "We're a financial institution, we need DORA + FINMA + ISO 27001 + GDPR compliance, we have technical capacity for structured evidence automation."

---

## 📋 Variant Comparison

| Feature | FRAMEWORK (SSE) | OPERATIONAL |
|---------|----------------|-------------|
| **Target Audience** | Regulated industries (financial, healthcare, critical infrastructure) | SMEs seeking ISO 27001 certification |
| **Regulatory Scope** | Multi-framework (ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA) | Single-framework focused (ISO 27001 + nFADP + GDPR conditionally) |
| **Foundation Governance** | POL-00 (Regulatory Applicability Tier 1/2/3) + POL-01 (Governance Framework with authority boundaries, exception handling, change control, internal Challenge Protocol) | Classical ISMS structure (governance embedded in control policies, no meta-layer) |
| **Automation Level** | Moderate — Python generates comprehensive assessment workbooks from control scope; assessor completes manually against system state | Moderate — Python generates assessment checklists from OP-POL requirements; assessor completes manually |
| **Control Coverage** | 53 control packs / 93 Annex A controls; Score 4–5 have most objective criteria, Score 1–3 use structured assessment workbooks | 53 control packs / 93 Annex A controls (100% checklist coverage) |
| **Evidence Type** | Control-derived assessment workbooks: built comprehensively against full control scope and ISO 27001 requirements; assessor marks Compliant/Partial/Non-Compliant/N/A with supporting documentation | Policy-derived compliance checklists: script built to reflect OP-POL requirements; assessor marks Compliant/Partial/Non-Compliant/N/A |
| **Python Skill Required** | Intermediate (run scripts to generate workbooks, light customisation to adapt to organisational context) | Basic (run scripts to generate checklists, minimal customisation) |
| **Implementation Effort** | High (6–12 months for full implementation) | Moderate (3–6 months for certification readiness) |
| **Maintenance Burden** | Moderate (scripts updated when control requirements evolve, workbook criteria reviewed annually) | Low (regenerate checklists quarterly, update policies annually) |
| **Compliance Verification** | Periodic (workbooks regenerated on demand, completed by assessor; frequency determined by control criticality and organisational policy) | Periodic (quarterly assessments, annual reviews) |
| **When You Need This** | Multi-regulatory compliance (DORA + FINMA + PCI DSS + ISO 27001), comprehensive evidence required | ISO 27001 certification, want automation help but not full DevOps-for-compliance |

**Can you use both?** Technically yes, but:
- If you need multi-regulatory (DORA, FINMA, etc.) → Use FRAMEWORK (SSE) with POL-00/POL-01
- If you only need ISO 27001 → Use OPERATIONAL (standalone, no POL-00/POL-01 needed)

**Do NOT mix:** OPERATIONAL is self-contained. Adding POL-00/POL-01 to OPERATIONAL over-complicates SME implementation.

---

## 🏛️ Foundation Governance Explained

### 🏗️ FRAMEWORK (SSE) Foundation

<p>
<img src="https://img.shields.io/badge/POL--00-Regulatory_Applicability-9400D3?style=flat-square" alt="POL-00"/>
<img src="https://img.shields.io/badge/POL--01-Governance_Framework-0066CC?style=flat-square" alt="POL-01"/>
</p>

When navigating **6+ regulatory frameworks** (ISO 27001, GDPR, DORA, NIS2, PCI DSS, FINMA):

**POL-00 solves:** "Which of these regulations actually apply to us?"
- **Tier 1 (Mandatory)**: Legal obligations (ISO 27001, Swiss nFADP, GDPR where applicable)
- **Tier 2 (Conditional)**: Triggered by business context (DORA if financial entity, PCI DSS if processing cards)
- **Tier 3 (Informational)**: Best practices (NIST, CIS, OWASP)
- Quarterly monitoring detects when Tier 2 becomes Tier 1 (business expansion, regulatory changes)

**POL-01 solves:** "Who decides how we comply internally, and how do we handle complexity?"
- **Authority boundaries**: CISO (technical), Legal/Compliance (regulatory), Executive Management (strategic)
- **Exception handling**: 5-step internal process when controls conflict across frameworks (e.g., GDPR deletion vs. FINMA retention requirements)
- **Change management**: 6-step process when regulatory requirements evolve
- **Challenge Protocol**: Structured internal disagreement resolution when ISMS stakeholders question multi-framework interpretations

> **Note:** The internal Challenge Protocol governs disagreements between your own CISO, Legal, and Executive team during ISMS design and operation. External audit disagreements follow the certification body's standard appeals and objection process — the Challenge Protocol does not constrain or apply to certification body auditors.

**Result:** Explicit governance for a complex regulatory landscape. Without POL-00/POL-01, reconciling 6 frameworks consistently is structurally difficult.

### ⚡ OPERATIONAL Foundation

<p>
<img src="https://img.shields.io/badge/Governance-Classical_ISMS-FF6600?style=flat-square" alt="Classical ISMS"/>
<img src="https://img.shields.io/badge/No_Meta--Layer-By_Design-32CD32?style=flat-square" alt="No Meta-Layer"/>
</p>

**Why POL-00/POL-01 do NOT exist in OPERATIONAL:**

When implementing **ISO 27001 only** (or ISO 27001 + GDPR conditionally):
- Regulatory scope is clear and limited (no Tier 1/2/3 complexity)
- Control applicability is documented in SoA (ISO 27001 Clause 6.1.3 process, standard ISMS approach)
- Exception handling is embedded in control policies (each OP-POL addresses "if control cannot be implemented" per ISO 27001 guidance)
- Governance is classical ISMS structure (CISO → Management Review → Internal Audit per Clauses 5, 9.2, 9.3)

**Result:** SMEs don't need a governance meta-layer. Classical ISMS structure handles ISO 27001 complexity without additional governance overhead.

**If an SME grows into a regulated industry** (becomes a financial entity subject to DORA, or accepts payment cards requiring PCI DSS):
- Transition from OPERATIONAL → FRAMEWORK (SSE)
- Add POL-00 (now need Tier 1/2/3 regulatory tracking)
- Add POL-01 (now need formal exception handling for multi-framework conflicts)

---

## 🔬 Key Innovations

### 1. Tier 1/2/3 Regulatory Framework (POL-00 — FRAMEWORK Only)

<p>
<img src="https://img.shields.io/badge/Tier_1-Mandatory-DC143C?style=flat-square" alt="Tier 1 Mandatory"/>
<img src="https://img.shields.io/badge/Tier_2-Conditional-FF6600?style=flat-square" alt="Tier 2 Conditional"/>
<img src="https://img.shields.io/badge/Tier_3-Informational-0066CC?style=flat-square" alt="Tier 3 Informational"/>
</p>

**Problem solved:** "Does GDPR apply? Does PCI DSS apply? What about DORA?"

**Traditional ISMS:** Ambiguous references, audit-time debates, scope confusion

**FRAMEWORK (SSE) Solution:**
- **Tier 1 (Mandatory)**: Legal obligations (ISO 27001, Swiss nFADP, GDPR where applicable)
- **Tier 2 (Conditional)**: Triggered by business context (DORA if financial entity, PCI DSS if processing cards)
- **Tier 3 (Informational)**: Best practices (NIST, CIS, OWASP)
- Quarterly monitoring, documented assessment, Executive Management approval

**OPERATIONAL:** Regulatory scope is simpler (ISO 27001 + nFADP + GDPR conditionally), documented directly in control policies without Tier framework.

**Result (FRAMEWORK):** Zero ambiguity. Auditor cannot argue "You should comply with X" if X is documented as Tier 2 — Not Applicable with quarterly monitoring demonstrating the trigger has not occurred.

---

### 2. Governance with Competence Requirements (POL-01 — FRAMEWORK Only)

<p>
<img src="https://img.shields.io/badge/FRAMEWORK-Only-9400D3?style=flat-square" alt="Framework Only"/>
<img src="https://img.shields.io/badge/Authority-Boundaries_Defined-0066CC?style=flat-square" alt="Authority Boundaries"/>
</p>

**Problem solved:** "Who decides what's adequate internally? What if stakeholders disagree on interpretation?"

**Traditional ISMS:** Undefined authority boundaries, subjective interpretations, stale decisions

**FRAMEWORK (SSE) Solution:**
- **Authority boundaries**: CISO (technical), Legal/Compliance (regulatory), Executive Management (strategic)
- **Competence requirements**: CISO = CISSP/CISM + 5 years + ISO 27001 knowledge (documented, verifiable)
- **Internal Challenge Protocol**: Structured process for internal disagreements (evidence-based, ISO 27001 clause references required)
- **Exception handling**: 5-step internal process (Document → Assess risk → Propose solution → Obtain approval → Document in SoA)

**OPERATIONAL:** Uses classical ISMS governance (CISO → Management Review → Internal Audit per ISO 27001 Clauses 5, 9.2, 9.3). Exception handling embedded in control policies.

**Result (FRAMEWORK):** Internal governance decisions are documented, traceable, and defensible. The auditor verifies the quality and traceability of those decisions — they do not replace them.

---

### 3. Structured Evidence Generation

<p>
<img src="https://img.shields.io/badge/Evidence-Control--Derived_(FW)-9400D3?style=flat-square" alt="Control Derived"/>
<img src="https://img.shields.io/badge/Evidence-Policy--Derived_(OP)-FF6600?style=flat-square" alt="Policy Derived"/>
<img src="https://img.shields.io/badge/Format-Python_+_Excel-32CD32?style=flat-square" alt="Python Excel"/>
</p>

**Problem solved:** "Prove your controls are implemented. Prove your configurations are compliant."

**Traditional ISMS:** Screenshots, manual logs, "here's a sample" — gathered in a rush before each audit

**FRAMEWORK (SSE):**
- Python script generates a comprehensive assessment workbook built against the full control scope
- Workbook covers every dimension the control addresses — not filtered by SME proportionality
- Assessor completes the assessment: marks Compliant/Partial/Non-Compliant/N/A per requirement area, attaches supporting documentation (configs, certificates, logs, approvals)
- Score 4–5 controls produce workbooks where most criteria are directly measurable — the assessor extracts the value from the system and records it (retention period configured, algorithm in use, last tested date)
- Score 1–3 controls produce workbooks that are still comprehensive, but rely more on assessor judgment and attestation-based evidence
- Evidence: Completed workbook + supporting documentation. Auditor can verify each line item against stated policy requirements.

**OPERATIONAL:**
- Python script generates a structured compliance checklist reflecting the requirements defined in the OP-POL
- Assessor completes quarterly: marks Compliant/Partial/Non-Compliant/N/A per requirement
- Evidence: Completed workbook + supporting documentation (certificates, configs, attestations)

**The distinction that matters:** OPERATIONAL workbooks are **policy-derived** — the checklist reflects what the OP-POL defines, scoped to SME context. FRAMEWORK workbooks are **control-derived** — built comprehensively against the full scope of what the control requires. Different starting points, different depth, different audit conversations.

**Result:** Evidence is structured, traceable, and regenerable on demand. Auditor verifies compliance objectively against explicit, testable requirements — not "trust me."

---

### 4. Control Pack Consolidation

<p>
<img src="https://img.shields.io/badge/53_Packs-93_Controls-0066CC?style=flat-square" alt="53 Packs"/>
<img src="https://img.shields.io/badge/DRY-Don't_Repeat_Yourself-FF6600?style=flat-square" alt="DRY"/>
</p>

**Problem solved:** "Why do we have 93 separate policies for 93 Annex A controls? This is document hell."

**Traditional ISMS:** 93 separate Word documents, or one massive 300-page policy (both bad)

**ISMS CORE Solution (both variants):**
- **53 control packs** cover **93 Annex A controls**
- Related controls share policies when they address common processes or technologies:
  - A.5.15-16-18: Identity Access Management (IAM spans multiple controls)
  - A.8.1-7-18-19: Endpoint Security (shared endpoint management)
  - A.5.30-8.13-14: Business Continuity & DR (BC/DR lifecycle crosses boundaries)
- Stacking rationale documented in each policy
- Each control's specific ISO 27001 requirements distinctly addressed (not lost in generic bundle)

**Result:** Logical grouping (not arbitrary). Easier maintenance (update one policy, affects related controls). Auditor can still verify each control individually (requirements are traceable).

---

### 5. Testable Requirements

<p>
<img src="https://img.shields.io/badge/Requirements-Explicit_Pass/Fail-00AA00?style=flat-square" alt="Pass Fail"/>
<img src="https://img.shields.io/badge/No_More-%22Appropriate_Measures%22-DC143C?style=flat-square" alt="No Vague"/>
</p>

**Problem solved:** "Our policy says 'appropriate security measures.' Auditor says that's inadequate."

**Traditional ISMS:** Vague requirements ("regular reviews", "sufficient encryption", "adequate monitoring")

**ISMS CORE:** Testable requirements with clear pass/fail criteria:

| Vague (Traditional) | Testable (ISMS CORE) |
|---------------------|---------------------|
| "Backups shall be performed regularly" | "Backups shall be performed daily, encrypted with AES-256, tested quarterly for restore capability" |
| "Access shall be reviewed periodically" | "Access rights shall be reviewed quarterly, documented in access review workbook, approved by system owner" |
| "Appropriate encryption shall be used" | "Encryption shall use AES-256 (symmetric), RSA-4096 (asymmetric), TLS 1.3 (transport). Prohibited: DES, 3DES, MD5, SHA-1, TLS 1.0/1.1" |
| "Security incidents shall be handled" | "Incidents classified within 4 hours (A.5.25), response initiated within 24 hours (A.5.26), post-incident review within 7 days (A.5.27)" |

**Result:** Auditor verifies objectively. No debate about "Is this appropriate?" — requirement is explicit, evidence demonstrates compliance or non-compliance.

---

## 🖥️ Deployment Model: On-Premises First

<p>
<img src="https://img.shields.io/badge/Deployment-On--Premises-2E8B57?style=flat-square" alt="On-Premises"/>
<img src="https://img.shields.io/badge/Data_Sovereignty-By_Design-0066CC?style=flat-square" alt="Data Sovereignty"/>
<img src="https://img.shields.io/badge/CLOUD_Act-Risk_Mitigated-DC143C?style=flat-square" alt="CLOUD Act"/>
</p>

ISMS CORE is designed as a **self-hosted, on-premises platform**. This is a deliberate architectural decision, not a roadmap limitation.

Your ISMS evidence reflects your infrastructure configurations, organisational decisions, and control implementations. This is sensitive operational data — and in 2025–2026, the question of where that data resides and under whose legal jurisdiction it operates has become a material security and compliance concern in its own right.

**The European data sovereignty context:**

Europe's dependence on US-based cloud infrastructure has become a boardroom-level concern driven by concrete legal risk. The US CLOUD Act of 2018 allows American authorities to compel US-based technology companies to provide requested data regardless of where that data is physically stored — including data held in EU data centres. As of 2026, there is no European law that repeals this extraterritorial effect. Major US hyperscalers operating European sovereign cloud offerings have confirmed they cannot give an absolute guarantee that EU-hosted data will never be requested by US authorities.

The EU responded with the Declaration for European Digital Sovereignty (November 2025), a joint commitment by EU member states to strengthen European control over digital infrastructure. European sovereign cloud investment is forecast to more than triple between 2025 and 2027. Cloud repatriation — moving workloads from public cloud back to on-premises or European-operated infrastructure — is an actively growing trend, particularly for regulated industries, government, and security-sensitive workloads.

An ISMS platform — which holds your organisation's security control evidence, compliance status, risk assessments, gap analyses, and audit artefacts — sits precisely in the category of data that should not be subject to foreign-jurisdiction legal access.

**What on-premises means for ISMS CORE:**
- Python scripts run in your environment, against your systems
- Generated workbooks stay in your infrastructure
- No data leaves your organisation to a third-party platform
- You control the assessment schedule, storage, and access
- No vendor dependency for your compliance evidence

**A note on future hosted offerings:**

A hosted or SaaS-accessible version of ISMS CORE is not excluded from the roadmap. However, data sovereignty is a design variable in any such architecture — not an afterthought. Any future hosted offering would need to address jurisdiction, residency, legal access risk, and operational control in a way that is architecturally verifiable, not commercially asserted. The on-premises model remains the default for organisations in regulated industries or jurisdictions where these concerns are material.

---

## ⚖️ What This Is NOT

<p>
<img src="https://img.shields.io/badge/NOT-Plug_and_Play-DC143C?style=flat-square" alt="Not Plug and Play"/>
<img src="https://img.shields.io/badge/NOT-Beginner_Friendly-DC143C?style=flat-square" alt="Not Beginner Friendly"/>
<img src="https://img.shields.io/badge/IS-Engineering_Driven-00AA00?style=flat-square" alt="Engineering Driven"/>
<img src="https://img.shields.io/badge/IS-Audit_Optimised-00AA00?style=flat-square" alt="Audit Optimised"/>
</p>

**This is NOT:**
- ❌ **Plug-and-play templates**: You must understand ISO 27001, adapt to your context, make documented decisions (not fill-in-the-blanks)
- ❌ **Consultant replacement**: You need competence (CISO with ISO 27001 knowledge, Legal/Compliance for regulatory interpretation). The platform accelerates implementation — it does not replace expertise.
- ❌ **Magic certification button**: You still implement controls, collect evidence, pass audits. This makes it systematic, not automatic.
- ❌ **Beginner-friendly**: If you don't understand risk assessment, control objectives, or basic Python, start with ISO 27001 training first.
- ❌ **Vendor-agnostic boilerplate**: Policies reference specific technologies (AES-256, TLS 1.3, MFA). You must adapt to your stack (AWS, Azure, on-premises, hybrid).
- ❌ **Zero-maintenance solution**: Scripts require updates when infrastructure changes, policies require annual review, evidence must be regenerated periodically.

**This IS:**
- ✅ **Engineering-driven compliance**: Systematic, code-based, evidence-automated approach to ISMS
- ✅ **Opinionated framework**: We made decisions (AES-256 minimum, TLS 1.3, quarterly reviews). You can change them, but they're explicit — not vague.
- ✅ **Audit-optimised**: Structured to reduce audit-time ambiguity by moving professional judgment to model design — auditors verify documented decisions rather than interpreting vague ones
- ✅ **Maintainable**: Version-controlled Markdown, regenerable workbooks, testable (not static Word docs rotting on SharePoint)
- ✅ **Continuous improvement**: Lessons learned registers, governance reviews, change control processes (ISMS evolves, not stagnates)
- ✅ **Data sovereign by design**: On-premises deployment keeps your compliance evidence under your control and your jurisdiction

---

## 👥 Who Should Use This?

<p>
<img src="https://img.shields.io/badge/✅_Good_Fit-See_Below-00AA00?style=flat-square" alt="Good Fit"/>
<img src="https://img.shields.io/badge/❌_Bad_Fit-See_Below-DC143C?style=flat-square" alt="Bad Fit"/>
</p>

### ✅ Good Fit

<p>
<img src="https://img.shields.io/badge/⚡_OPERATIONAL-SMEs_seeking_certification-FF6600?style=flat-square" alt="OPERATIONAL Good Fit"/>
<img src="https://img.shields.io/badge/🏗️_FRAMEWORK-Regulated_industries-9400D3?style=flat-square" alt="FRAMEWORK Good Fit"/>
</p>

**OPERATIONAL:**
- SMEs wanting ISO 27001 certification with clear, testable requirements
- Teams wanting automation help (checklist generation) without full DevOps commitment
- Organisations tired of vague policies ("appropriate", "regular", "sufficient")
- CISOs who want objective compliance evidence (not "trust me" statements)

**FRAMEWORK (SSE):**
- Regulated industries with multi-framework compliance (financial services: DORA + FINMA + ISO 27001)
- Organisations wanting comprehensive, control-derived assessments rather than SME-scoped checklists
- Teams wanting structured, exhaustive workbooks that cover the full depth of each control's requirements
- CISOs who want objective, traceable evidence with explicit pass/fail criteria per requirement

### ❌ Bad Fit (Both Variants)

- Organisations wanting zero-effort certification
- Teams without Python capability (scripts must be executable, even if not heavily customised)
- CISOs expecting consultant hand-holding (you make decisions, the platform provides structure)
- Organisations wanting subjective flexibility ("We'll decide what 'appropriate' means during audit" — no, decide now, document it)
- Teams that don't want to be told what to do (the platform is opinionated: AES-256, not "choose your encryption")

---

## ❓ Before You Open an Issue

**"Is there a SaaS or hosted version?"**

Not currently. ISMS CORE is a platform you deploy and run in your own environment. This is a deliberate design decision grounded in data sovereignty — your ISMS evidence is sensitive operational data, and in the current European regulatory environment, self-hosted deployment is the architecturally sound default. A hosted version is not excluded from the roadmap, but data sovereignty will be a design requirement, not an afterthought, in any such offering.

**"Why does a higher Score control have a more detailed workbook than a lower Score one?"**

Score reflects evidence objectivity — how directly and measurably a control's requirements can be verified. Score 4–5 controls address requirements that can be checked precisely (retention periods, algorithm specifications), so the workbook can be built with explicit pass/fail criteria per item. Score 1–3 controls address requirements that depend more on process, judgment, and attestation, so the workbook is comprehensive but relies more on assessor documentation. Both are complete assessments — the Score describes the nature of the evidence, not the effort required.

**"Can I use OPERATIONAL and add POL-00/POL-01 later?"**

You can, but it is not recommended. OPERATIONAL is designed as a self-contained classical ISMS. Adding POL-00/POL-01 mid-implementation creates a hybrid more complex than either pure variant. If you think you need POL-00/POL-01, start with FRAMEWORK. If you are an SME and genuinely only need ISO 27001 + GDPR, OPERATIONAL is sufficient without them.

**"The Python scripts don't work in my environment."**

The scripts require Python 3.11+ and the dependencies listed in `requirements.txt`. They are tested on Linux and macOS. Windows PowerShell environments may require adaptation. This is a prerequisite, not a support issue. Read the prerequisites section before running anything.

**"Can I use this for ISO 27001 certification without a consultant?"**

Technically yes, if you have a qualified CISO (ISO 27001 knowledge, relevant experience) and Legal/Compliance capability for regulatory determinations. The platform accelerates implementation — it does not replace the expertise required to make good security decisions. If you do not know what a Statement of Applicability is, hire a consultant first.

**"The policies reference Swiss law (nFADP). I'm not in Switzerland."**

The regulatory framework is Swiss-primary (nFADP, FINMA) because that is the design context. Tier 1 mandatory regulations will differ for your jurisdiction. POL-00 provides the framework for making those determinations — you substitute your mandatory regulations in Tier 1. The control policies (Annex A) are jurisdiction-neutral. The governance framework (POL-00/POL-01) is not jurisdiction-locked; it is jurisdiction-parameterised.

**"I found a mistake in a policy or a script error."**

Open an issue with: (1) the specific document or script, (2) the exact error or incorrect text, (3) the correct text or expected behaviour with a reference (ISO 27001 clause, regulation article, etc.). Issues without a specific reference will be closed. "This doesn't look right" is not actionable.

---

## 🖥️ The Third Layer: ISMS CORE Platform

Framework and Operational are **content products** — policies, workbooks, and guides that work perfectly as static files. You can clone this repository, run the Python generators, fill in the Excel workbooks, and have a fully functional, audit-ready ISMS without anything else.

The **ISMS CORE Platform** is the operational layer built on top. It ingests both products and turns them into a live compliance management system:

| Without Platform | With Platform |
|-----------------|---------------|
| Read policies as files | Search across all policies by keyword or control |
| Open individual Excel workbooks | See aggregated compliance scores per section and control group |
| Manually track gaps in a spreadsheet | Gap lifecycle management with severity, owner, SLA, and remediation tracking |
| No cross-framework visibility | ISO 27001 ↔ NIST CSF ↔ MITRE ATT&CK ↔ GDPR ↔ DORA mappings, live |
| Manual evidence collection | Evidence items with expiry tracking and freshness alerts |
| No audit trail | Full immutable log of who did what and when |

The Platform is a six-service Docker Compose stack (FastAPI + PostgreSQL + Redis + OpenSearch + Celery + React) deployed on-premises. Same data sovereignty principle applies — your compliance data does not leave your infrastructure.

**Platform is additive, never mandatory.** Framework and Operational are the product. Platform is the engine that makes it operational at scale.

See [PLATFORM.md](PLATFORM.md) for architecture details and [GETTING-STARTED.md](GETTING-STARTED.md) for setup instructions.

---

<p align="center">
<strong>Copyright © 2025–2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
<em>Where bamboo antennas actually work.</em> 🎋
</p>