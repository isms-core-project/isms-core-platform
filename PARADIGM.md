# ISMS CORE — Understanding the Paradigm Shift

## What Is ISMS CORE?

ISMS CORE provides **two distinct ISMS implementations** designed for different organisational needs:

- **FRAMEWORK (SSE — Secure Systems Engineering)**: Engineered compliance system for regulated industries with complex multi-regulatory requirements
- **OPERATIONAL**: Classical ISMS for SMEs seeking ISO 27001 certification with automation-assisted compliance

Both variants use code-driven, evidence-automated, engineer-designed approaches. If you are looking for Word document templates, generic guidance like "implement appropriate security measures", or annual compliance snapshots with manual evidence collection — this is not the right tool for you.

## Traditional ISMS vs. ISMS CORE

| Aspect | Traditional ISMS | ISMS CORE (Both Variants) |
|--------|-----------------|---------------------------|
| **Documentation Format** | Word/PDF documents, manual templates | Markdown policies + Python scripts + generated workbooks |
| **Evidence Collection** | Manual gathering (screenshots, logs, approvals) | Automated workbook generation (FRAMEWORK: live queries; OPERATIONAL: compliance checklists) |
| **Requirements Specificity** | "Regular backups", "Appropriate encryption" | "AES-256 encrypted backups, verified daily via automated script" (testable, measurable) |
| **Professional Judgment Location** | Audit discussion (auditor interprets "adequate") | Model design (organisation documents interpretation, auditor verifies) |
| **Compliance Verification** | Annual snapshot (point-in-time assessment) | Continuous/periodic verification (workbooks regenerated on demand) |
| **Policy Updates** | Manual document revision, version control in filenames | Version-controlled Markdown, automated regeneration of dependent workbooks |
| **Exception Handling** | Ad-hoc discussions with auditors | Structured process (FRAMEWORK: POL-01 5-step; OPERATIONAL: embedded in control policies) |
| **Regulatory Applicability** | Ambiguous ("We comply with GDPR where applicable") | Explicit (FRAMEWORK: POL-00 Tier 1/2/3; OPERATIONAL: focused scope in control policies) |
| **Audit Preparation** | Weeks of scrambling to gather evidence | Hours to assemble (workbooks already generated, evidence already exists) |
| **Control Implementation Evidence** | "We have a firewall" (trust us) | Python workbook showing firewall rules, last verified date, compliance status (verify yourself) |

## The Paradigm Shift: Where Does Professional Judgment Live?

This is the core idea behind ISMS CORE. In a traditional ISMS, professional judgment happens during the audit — the auditor decides what's "adequate." In ISMS CORE, professional judgment happens during policy design — the organisation decides, documents it, and the auditor verifies.

### Traditional ISMS (Judgment During Audit)

1. Write policy: "Backups shall be encrypted with appropriate algorithms"
2. Implement: Install backup system, enable encryption (probably)
3. Audit time:
   - Auditor: "What algorithm?"
   - You: "Um... whatever the vendor default is?"
   - Auditor: "Is that appropriate?"
   - You: "We think so?"
   - Auditor: [Writing finding] "Encryption adequacy unclear"
4. Result: 3 months remediation, policy rewrite, re-audit

### ISMS CORE (Judgment During Model Design)

1. Write policy: "Backups shall be encrypted using AES-256 minimum (POL-A.8.24 cryptography standard)"
2. Implement: Configure backup system for AES-256, document in IMP (FRAMEWORK) or policy (OPERATIONAL)
3. Build verification: Python script generates assessment workbook from policy requirements (OPERATIONAL) or queries backup API (FRAMEWORK Score 4–5)
4. Generate evidence: Workbook shows compliance status per requirement, last assessed date, Compliant/Non-Compliant per item
5. Audit time:
   - Auditor: "Show me backup encryption compliance"
   - You: "Here's the workbook. Generated from policy. 100% AES-256."
   - Auditor: "Can I verify this?"
   - You: "Run the Python script yourself. Code is documented."
   - Auditor: [Reviews output] "...compliant."
6. Result: No discussion. No finding. Audit moves on.

**The difference:** Professional judgment (What algorithm? What's "appropriate"?) was exercised **during policy design** (CISO documented "AES-256 minimum"), not during audit (no room for interpretation).

## Two Variants: Choose Based on Your Needs

### OPERATIONAL (Foundation ISMS for SMEs)

**For whom:**
- Small to medium enterprises seeking ISO 27001 certification
- Organisations with focused regulatory scope (ISO 27001 + Swiss nFADP + GDPR conditionally)
- Teams wanting classical ISMS structure with automation benefits

**What you get:**
- **Architecture**: OP-POL (policy) → Python Script (requirement extractor) → Assessment Workbook (compliance checklist)
- **Coverage**: 53 control packs covering all 93 Annex A controls (100% coverage)
- **Automation**: Python-generated Excel compliance checklists (script built to reflect requirements defined in OP-POL)
- **Evidence**: Quarterly/annual compliance assessments via workbooks
- **Methodology**: Classical ISMS structure with 1:1 policy stacking (related controls share policies)
- **Regulatory support**: ISO 27001:2022 + Swiss nFADP + GDPR (when applicable)
- **Governance**: Embedded in control policies (no separate POL-00/POL-01 meta-layer)

**How the workbook is built:**

Each OP-POL is written to address the control's objectives in a way that is proportionate to SME context and scope. The Python script was built to reflect those requirements — the checklist items in the workbook correspond to the OP-POL because the script was authored that way, not because it parses the policy at runtime. The workbook is **policy-derived** — the OP-POL is the source of truth, and the script is a hand-crafted artefact that embodies it. The assessor then completes the workbook manually, marking each requirement Compliant / Partial / Non-Compliant / N/A and attaching supporting evidence.

**Prerequisites:**
- Basic Python execution capability (run scripts to generate checklists)
- Understanding of ISO 27001 Annex A controls
- Willingness to document decisions explicitly (testable requirements, not vague statements)
- Quarterly assessment discipline (complete workbooks, track compliance)

**Best for:** "We need ISO 27001 certification, we want automation help with compliance tracking, but we don't need multi-regulatory governance complexity."

### FRAMEWORK (SSE — Secure Systems Engineering)

**For whom:**
- Regulated industries (financial services, healthcare, critical infrastructure)
- Organisations with complex multi-regulatory requirements (GDPR + DORA + NIS2 + PCI DSS + FINMA)
- Technical teams comfortable with heavy automation and API integration

**What you get:**
- **Foundation Governance**:
  - **POL-00** (Regulatory Applicability Framework): Tier 1/2/3 categorisation, quarterly monitoring, triggered assessments
  - **POL-01** (ISMS Governance Framework): Authority boundaries, competence requirements, 5-step exception process, 6-step change control, Challenge Protocol
- **Architecture**: POL (policy) → IMP (implementation spec) → Python (automation) → Workbook (evidence)
- **Per control pack**: POL + IMP (UG/TG) + SCR + WKBK + REF + FORM + INS + CTX
- **Coverage**: 53 control packs covering all 93 Annex A controls (100% coverage). Score 4–5 controls have full automation scripts generating live evidence from infrastructure APIs. Score 1–3 controls use comprehensive assessment workbooks (see below).
- **Evidence**: Score 4–5: continuous compliance verification from live system queries. Score 1–3: structured assessment workbooks completed periodically.
- **Methodology**: Score 1–5 system (see below)
- **Regulatory support**: Multi-framework (ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA)

**How the workbook is built (Score 1–3 controls):**

For controls where full automation is not yet feasible or meaningful, FRAMEWORK uses comprehensive assessment workbooks. Unlike OPERATIONAL workbooks — which are derived from what the OP-POL defines — FRAMEWORK workbooks are **control-derived**: built directly and comprehensively against every area the control addresses, covering the full scope of what ISO 27001 requires. The POL itself is written to the same scope. Policy and workbook are co-designed against the control requirements, not filtered through SME proportionality. The result is a more exhaustive, structured assessment than the OPERATIONAL equivalent, reflecting the control's full depth rather than an SME-appropriate subset of it.

**Prerequisites:**
- Python development capability (scripts must be maintained, customised, integrated with infrastructure)
- Infrastructure APIs accessible (automation requires programmatic access: cloud platforms, firewalls, IAM, backup systems)
- Technical team willing to learn SSE methodology
- Appetite for building custom automation (not plug-and-play)

**The Score 1–5 System (FRAMEWORK only):**

Each Annex A control is scored on automation potential:
- **Score 5**: Fully automatable (firewall rules, log retention, backup status — query an API, get a result)
- **Score 4**: Mostly automatable (access review, patch compliance — automation covers 80%+)
- **Score 3**: Partially automatable (incident response — process can be tracked, not automated end-to-end)
- **Score 2**: Mostly manual (security training, supplier reviews — human judgment required)
- **Score 1**: Fully manual (physical security, HR processes — no meaningful automation possible)

FRAMEWORK prioritises Score 4–5 controls because these deliver the highest evidence quality through automation. Score 1–3 controls use comprehensive assessment workbooks built against the full control scope.

**Best for:** "We're a financial institution, we need DORA + FINMA + ISO 27001 + GDPR compliance, we have technical capacity for heavy automation."

## Variant Comparison

| Feature | FRAMEWORK (SSE) | OPERATIONAL |
|---------|----------------|-------------|
| **Target Audience** | Regulated industries (financial, healthcare, critical infrastructure) | SMEs seeking ISO 27001 certification |
| **Regulatory Scope** | Multi-framework (ISO 27001 + GDPR + DORA + NIS2 + PCI DSS + FINMA) | Single-framework focused (ISO 27001 + nFADP + GDPR conditionally) |
| **Foundation Governance** | **POL-00** (Regulatory Applicability Tier 1/2/3) + **POL-01** (Governance Framework with authority boundaries, exception handling, change control) | Classical ISMS structure (governance embedded in control policies, no meta-layer) |
| **Automation Level** | Heavy (Python queries infrastructure APIs, generates real-time evidence from live systems) | Moderate (Python generates assessment checklists from OP-POL requirements, manual completion) |
| **Control Coverage** | 53 control packs / 93 Annex A controls (Score 4–5 have live automation; Score 1–3 use comprehensive assessment workbooks) | 53 control packs / 93 Annex A controls (100% checklist coverage) |
| **Evidence Type** | Score 4–5: live system queries (firewall rules, backup status, log retention, IAM permissions). Score 1–3: comprehensive structured assessments | Policy-derived compliance checklists (script built to reflect OP-POL requirements; assessor marks Compliant/Partial/Non-Compliant) |
| **Workbook Design** | Control-derived: built comprehensively against full control scope; policy and workbook co-designed | Policy-derived: Python extracts requirements from OP-POL; workbook reflects what policy defines |
| **Python Skill Required** | Advanced (build/maintain automation, API integration, infrastructure queries) | Basic (run scripts to generate checklists, light customisation) |
| **Implementation Effort** | High (6–12 months for full implementation with automation) | Moderate (3–6 months for certification readiness) |
| **Maintenance Burden** | Moderate (scripts must be updated when infrastructure changes, API endpoints evolve) | Low (regenerate checklists quarterly, update policies annually) |
| **Compliance Verification** | Continuous (Score 4–5: regenerate workbooks daily/weekly from live infrastructure; Score 1–3: periodic structured assessment) | Periodic (quarterly assessments, annual reviews) |
| **When You Need This** | Multi-regulatory compliance (DORA + FINMA + PCI DSS + ISO 27001), highly automated evidence required | ISO 27001 certification, want automation help but not full DevOps-for-compliance |

**Can you use both?** Technically yes, but:
- If you need multi-regulatory (DORA, FINMA, etc.) → Use FRAMEWORK (SSE) with POL-00/POL-01
- If you only need ISO 27001 → Use OPERATIONAL (standalone, no POL-00/POL-01 needed)

**Do NOT mix:** OPERATIONAL is self-contained. Adding POL-00/POL-01 to OPERATIONAL over-complicates SME implementation.

## Foundation Governance Explained

### FRAMEWORK (SSE) Foundation

**Why POL-00/POL-01 exist in FRAMEWORK:**

When you are navigating **6+ regulatory frameworks** (ISO 27001, GDPR, DORA, NIS2, PCI DSS, FINMA):

**POL-00 solves:** "Which of these regulations actually apply to us?"
- **Tier 1 (Mandatory)**: Legal obligations (ISO 27001, Swiss nFADP, GDPR where applicable)
- **Tier 2 (Conditional)**: Triggered by business context (DORA if financial entity, PCI DSS if processing cards)
- **Tier 3 (Informational)**: Best practices (NIST, CIS, OWASP)
- Quarterly monitoring detects when Tier 2 becomes Tier 1 (business expansion, regulatory changes)

**POL-01 solves:** "Who decides how we comply, and how do we handle the complexity?"
- **Authority boundaries**: CISO (technical), Legal/Compliance (regulatory), Executive Management (strategic)
- **Exception handling**: 5-step process when controls conflict across frameworks (e.g., GDPR deletion vs. FINMA retention)
- **Change management**: 6-step process when regulatory requirements evolve (GDPR guidance updates, DORA technical standards)
- **Challenge Protocol**: Structured disagreement resolution when auditors question multi-framework interpretations

**Result:** Explicit governance for complex regulatory landscape. Without POL-00/POL-01, you'd have chaos trying to reconcile 6 frameworks.

### OPERATIONAL Foundation

**Why POL-00/POL-01 do NOT exist in OPERATIONAL:**

When you are implementing **ISO 27001 only** (or ISO 27001 + GDPR conditionally):
- Regulatory scope is **clear and limited** (no Tier 1/2/3 complexity — ISO 27001 is mandatory, GDPR applies if processing EU data)
- Control applicability is **documented in SoA** (ISO 27001 Clause 6.1.3 process, standard ISMS approach)
- Exception handling is **embedded in control policies** (each OP-POL addresses "if control cannot be implemented" per ISO 27001 guidance)
- Governance is **classical ISMS structure** (CISO → Management Review → Internal Audit per Clauses 5, 9.2, 9.3)

**Result:** SMEs don't need a governance meta-layer. Classical ISMS structure handles ISO 27001 complexity without additional governance framework.

**If an SME grows into a regulated industry** (becomes financial entity subject to DORA, or accepts payment cards requiring PCI DSS):
- Transition from OPERATIONAL → FRAMEWORK (SSE)
- Add POL-00 (now need Tier 1/2/3 regulatory tracking)
- Add POL-01 (now need formal exception handling for multi-framework conflicts)

## Key Innovations

### 1. Tier 1/2/3 Regulatory Framework (POL-00 — FRAMEWORK Only)

**Problem solved:** "Does GDPR apply? Does PCI DSS apply? What about DORA?"

**Traditional ISMS:** Ambiguous references, audit-time debates, scope confusion

**FRAMEWORK (SSE) Solution:**
- **Tier 1 (Mandatory)**: Legal obligations (ISO 27001, Swiss nFADP, GDPR where applicable)
- **Tier 2 (Conditional)**: Triggered by business context (DORA if financial entity, PCI DSS if processing cards)
- **Tier 3 (Informational)**: Best practices (NIST, CIS, OWASP)
- Quarterly monitoring, documented assessment, Executive Management approval

**OPERATIONAL:** Regulatory scope is simpler (ISO 27001 + nFADP + GDPR conditionally), documented directly in control policies without Tier framework.

**Result (FRAMEWORK):** Zero ambiguity. Auditor can't argue "You should comply with X" if X is documented Tier 2 — Not Applicable with quarterly monitoring proving trigger hasn't occurred.

### 2. Governance with Competence Requirements (POL-01 — FRAMEWORK Only)

**Problem solved:** "Who decides what's adequate? What if auditor disagrees?"

**Traditional ISMS:** Auditor interpretation is final, endless discussions, subjective findings

**FRAMEWORK (SSE) Solution:**
- **Authority boundaries**: CISO (technical), Legal/Compliance (regulatory), Executive Management (strategic)
- **Competence requirements**: CISO = CISSP/CISM + 5 years + ISO 27001 knowledge (documented, verifiable)
- **Challenge Protocol**: Structured process for disagreements (evidence-based, ISO 27001 clause references required)
- **Exception handling**: 5-step process (Document → Assess risk → Propose solution → Obtain approval → Document in SoA)

**OPERATIONAL:** Uses classical ISMS governance (CISO → Management Review → Internal Audit per ISO 27001 Clauses 5, 9.2, 9.3). Exception handling embedded in control policies.

**Result (FRAMEWORK):** Auditor verifies **quality of organisational decisions**, doesn't replace them. Disagreements resolved through documented reasoning, not authority contest.

### 3. Evidence Automation

**Problem solved:** "Prove your backups are encrypted. Prove logs are retained. Prove access is reviewed."

**Traditional ISMS:** Screenshots, manual logs, "here's a sample"

**FRAMEWORK (SSE) — Score 4–5 controls:**
- Python script queries log retention settings across 47 servers via API
- Verifies: retention >= 12 months, integrity protection enabled, log forwarding configured
- Generates: Workbook showing compliant/non-compliant per server
- Result: 47/47 compliant (100%)
- Evidence: Workbook + Python script (auditor can re-run to verify)

**FRAMEWORK (SSE) — Score 1–3 controls:**
- Python script generates a comprehensive assessment workbook built against the full control scope
- Assessor completes the assessment: marks Compliant/Partial/Non-Compliant/N/A per requirement area
- Workbook covers every dimension the control addresses — not filtered by SME proportionality
- Evidence: Completed workbook + supporting documentation

**OPERATIONAL:**
- Python script was built to reflect the requirements defined in the OP-POL (written to address the control's objectives proportionate to SME scope)
- Generates: Assessment workbook as a policy-derived compliance checklist
- Assessor completes quarterly: marks Compliant/Partial/Non-Compliant/N/A per OP-POL requirement
- Evidence: Completed workbook + supporting documentation (certificates, configs, attestations)

**The distinction that matters:** OPERATIONAL workbooks are **policy-derived** — the checklist reflects what the OP-POL defines, scoped to SME context. FRAMEWORK Score 1–3 workbooks are **control-derived** — built comprehensively against the full scope of what the control requires, independent of SME scope filtering. Different starting points, different depth, different audit conversations.

**Result:** Evidence is current, traceable, regenerable. Auditor verifies compliance objectively (not "trust me").

### 4. Control Pack Consolidation (OPERATIONAL)

**Problem solved:** "Why do we have 93 separate policies for 93 Annex A controls? This is document hell."

**Traditional ISMS:** 93 separate Word documents, or one massive 300-page policy (both bad)

**OPERATIONAL Solution:**
- **53 control packs** cover **93 Annex A controls**
- Related controls share policies when they address common processes/technologies:
  - A.5.15-16-18: Identity Access Management (IAM spans multiple controls)
  - A.8.1-7-18-19: Endpoint Security (shared endpoint management)
  - A.5.30-8.13-14: Business Continuity & DR (BC/DR lifecycle crosses boundaries)
- Stacking rationale documented in each policy
- Each control's specific ISO 27001 requirements distinctly addressed (not lost in generic bundle)

**FRAMEWORK (SSE):** Organises controls by Score 1–5 automation potential rather than by process similarity. High-score controls get full automation scripts; low-score controls use comprehensive assessment workbooks built against full control scope.

**Result:** Logical grouping (not arbitrary). Easier maintenance (update one policy, affects related controls). Auditor can still verify each control individually (requirements are traceable).

### 5. Testable Requirements (Both Variants)

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

## What This Is NOT

**This is NOT:**
- ❌ **Plug-and-play templates**: You must understand ISO 27001, adapt to your context, make documented decisions (not fill-in-the-blanks)
- ❌ **Consultant replacement**: You need competence (CISO with ISO 27001 knowledge, Legal/Compliance for regulatory interpretation). The platform accelerates, it doesn't replace expertise.
- ❌ **Magic certification button**: You still implement controls, collect evidence, pass audits. This makes it systematic, not automatic.
- ❌ **Beginner-friendly**: If you don't understand risk assessment, control objectives, or basic Python, start with ISO 27001 training first.
- ❌ **Vendor-agnostic boilerplate**: Policies reference specific technologies (AES-256, TLS 1.3, MFA). You must adapt to your stack (AWS, Azure, on-premises, hybrid).
- ❌ **Zero-maintenance solution**: Scripts require updates when infrastructure changes, policies require annual review, evidence must be regenerated periodically.

**This IS:**
- ✅ **Engineering-driven compliance**: Systematic, code-based, evidence-automated approach to ISMS
- ✅ **Opinionated framework**: We made decisions (AES-256 minimum, TLS 1.3, quarterly reviews). You can change them, but they're explicit (not vague).
- ✅ **Audit-optimised**: Designed to pass Stage 1 + Stage 2 with minimal findings by moving judgment to model design
- ✅ **Maintainable**: Version-controlled Markdown, regenerable workbooks, testable (not static Word docs rotting on SharePoint)
- ✅ **Production-grade**: Built by a CISSP/CCSP/Azure Cybersecurity Architect Expert who has implemented this in real organisations and passed real audits
- ✅ **Continuous improvement**: Lessons learned registers, governance reviews, change control processes (ISMS evolves, not stagnates)

## Who Should Use This?

### ✅ Good Fit

**OPERATIONAL:**
- SMEs wanting ISO 27001 certification with **clear, testable requirements**
- Teams wanting **automation help** (checklist generation) without full DevOps commitment
- Organisations tired of **vague policies** ("appropriate", "regular", "sufficient")
- CISOs who want **objective compliance evidence** (not "trust me" statements)

**FRAMEWORK (SSE):**
- Regulated industries with **multi-framework compliance** (financial services: DORA + FINMA + ISO 27001)
- Organisations with **technical capacity** for heavy automation (Python development, API integration)
- Environments requiring **continuous compliance verification** (daily/weekly evidence regeneration from live systems)
- Teams wanting to **eliminate manual evidence gathering** (automate everything that can be automated)

### ❌ Bad Fit (Both Variants)

- Organisations wanting **zero-effort certification** (doesn't exist — this is systematic, not magical)
- Teams without **Python capability** (scripts must be executable, even if not heavily customised)
- CISOs expecting **consultant hand-holding** (you make decisions, the platform provides structure)
- Organisations wanting **subjective flexibility** ("We'll decide what 'appropriate' means during audit" — no, decide now, document it)
- Teams that **don't want to be told what to do** (the platform is opinionated: AES-256, not "choose your encryption")

## Before You Open an Issue

These questions come up regularly. Read this first.

**"Is there a SaaS or hosted version?"**
No. ISMS CORE is a platform you implement in your environment. Your ISMS evidence touches your infrastructure — it cannot and should not live in a third-party SaaS. The Python scripts run in your environment, against your systems, generating your evidence. That is by design.

**"Why isn't control A.X.XX fully automated in FRAMEWORK?"**
FRAMEWORK prioritises Score 4–5 controls — those where automation delivers high-quality, real-time evidence. Score 1–3 controls use comprehensive assessment workbooks built against the full control scope rather than live API queries. Check the Score assigned to the control before asking.

**"Can I use OPERATIONAL and add POL-00/POL-01 later?"**
You can, but it is not recommended. OPERATIONAL is designed as a self-contained classical ISMS. Adding POL-00/POL-01 mid-implementation creates a hybrid that is more complex than either pure variant. If you think you need POL-00/POL-01, start with FRAMEWORK. If you are an SME and genuinely only need ISO 27001 + GDPR, OPERATIONAL is sufficient without them.

**"The Python scripts don't work in my environment."**
The scripts require Python 3.10+ and the dependencies listed in `requirements.txt`. They are tested on Linux and macOS. Windows PowerShell environments may require adaptation. This is not a support issue — it is a prerequisite. Read the prerequisites section before running anything.

**"Can I use this for ISO 27001 certification without a consultant?"**
Technically yes, if you have a qualified CISO (ISO 27001 knowledge, relevant experience) and Legal/Compliance capability for regulatory determinations. The platform accelerates implementation — it does not replace the expertise required to make good security decisions. If you do not know what a Statement of Applicability is, hire a consultant first.

**"The policies reference Swiss law (nFADP). I'm not in Switzerland."**
The regulatory framework is Swiss-primary (nFADP, FINMA) because that is the design context. Tier 1 mandatory regulations will differ for your jurisdiction. POL-00 provides the framework for making those determinations — you substitute your mandatory regulations in Tier 1. The control policies (Annex A) are jurisdiction-neutral. The governance framework (POL-00/POL-01) is not jurisdiction-locked; it is jurisdiction-parameterised.

**"I found a mistake in a policy / the script generates an error."**
Open an issue with: (1) the specific document or script, (2) the exact error or incorrect text, (3) the correct text or expected behaviour with a reference (ISO 27001 clause, regulation article, etc.). Issues without a specific reference will be closed. "This doesn't look right" is not actionable.

---

<p align="center">
<strong>Copyright © 2025–2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
<em>Where bamboo antennas actually work.</em> 🎋
</p>