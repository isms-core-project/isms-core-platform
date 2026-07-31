<!-- ISMS-CORE:IMP:AI-IMP-A.6.1-UG:ai:UG:a.6.1 -->
**AI-IMP-A.6.1-UG — AI Development Governance — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Development Governance — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.6.1-UG |
| **Related Policy** | AI-POL-A.6.1 (AI Development Governance) |
| **Document Creator** | AI Governance Officer / Chief Technology Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial user guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.6.1 (AI Development Governance — governing policy)
- AI-IMP-A.6.1-TG (AI Development Governance — Technical Guide)
- AI-POL-A.6.2 (AI System Lifecycle)
- AI-POL-A.7.2-6 (Data for AI Systems)
- ISO/IEC 42001:2023 Controls A.6.1.1–A.6.1.7

---

## Purpose of This Guide

This guide explains **how to apply [Organisation]'s AI development governance requirements in practice** — including responsible design, bias management, V&V, and the development-to-deployment transition. It is the practical companion to AI-POL-A.6.1.

**Who this guide is for**: ML Engineers, Data Scientists, AI product leads, AI System Owners, and anyone involved in designing, building, or validating AI systems.

---

## Part 1 — Responsible Design in Practice

### 1.1 Responsible AI by Design — Not an Afterthought

Responsible AI considerations must enter the development process at the **design stage**, not as a final review before deployment. The cost of addressing a bias, transparency, or safety issue is orders of magnitude lower during design than post-deployment.

The AI development team should ask these questions at the start of every project:

| Design Question | What to Decide |
|----------------|---------------|
| Who will be affected by this system's outputs? | Defines the AISIA scope — involve AI Governance Officer early |
| Could any affected population be discriminated against? | Define fairness constraints and required training data coverage |
| What does "human oversight" mean for this system? | Design the human review step into the architecture, not as a wrapper |
| Can this system's outputs be explained? | Choose explainability-compatible architectures where consequential decisions are involved |
| What are the failure modes? | Define fail-safe behaviours and fallback states |
| What data is needed and what are the risks? | Involve Data Governance Lead and DPO at data design stage |

### 1.2 The AISIA as a Development Input

The AISIA (AI-IMP-A.5.2-5-UG) is not just a deployment gate — for new AI system development, a **preliminary AISIA** should be conducted at the design stage to identify:
- Impact dimensions that must be addressed in the system design
- Data quality requirements driven by fairness and privacy
- Human oversight mechanisms that must be built in
- Transparency requirements for the intended deployment context

The preliminary AISIA is updated and finalised before deployment (the deployment gate AISIA).

---

## Part 2 — Managing Bias

### 2.1 Where Bias Enters the Development Process

Bias in AI systems can enter at multiple points. Development teams must address each:

| Stage | Bias Entry Point | Mitigation |
|-------|-----------------|-----------|
| **Data collection** | Training data does not represent all affected groups; historical data encodes past discrimination | Representative sampling; demographic coverage assessment |
| **Data labelling** | Annotators apply inconsistent or culturally biased labels | Annotator diversity; inter-annotator agreement testing; label audits |
| **Feature engineering** | Proxy variables correlated with protected characteristics included in features | Feature review against protected characteristic proxies |
| **Model selection** | Some model types are less robust to distribution shift across demographic groups | Stratified evaluation by demographic group |
| **Threshold setting** | A single decision threshold can produce disparate impact across groups | Group-specific threshold analysis; consider separate thresholds where justified |
| **Evaluation** | Test set not representative of deployment population | Stratified test sets; evaluation on held-out demographic sub-groups |
| **Deployment** | Operational population differs from training population (distribution shift) | Ongoing monitoring of output distributions by group |

### 2.2 Minimum Fairness Evaluation Requirements

Before deployment, all AI systems with consequential outputs affecting individuals must pass:

1. **Demographic parity analysis**: Does the system produce significantly different outcomes for different demographic groups?
2. **Equalised opportunity analysis**: For positive-outcome systems (e.g., loan approval), is the true positive rate consistent across groups?
3. **Individual fairness spot-check**: Do similar individuals receive similar outputs?
4. **Proxy variable audit**: Do any features serve as proxies for protected characteristics?

Results are documented in the V&V record and referenced in the AISIA (Section 7.3 — Fairness and discrimination).

For systems with Low impact classification, a lighter-touch fairness review may be acceptable — documented with rationale.

### 2.3 When Bias Is Found

If bias is identified during evaluation:
1. Document the finding in the V&V record
2. Assess severity: does it produce disparate impact in practice?
3. Options: remediate (re-collect data, re-train, adjust thresholds) or document as known limitation with mitigating controls
4. Do not deploy a system with known material bias without documented risk acceptance from the AI Risk Owner and AI Governance Officer review

---

## Part 3 — Transparency by Design

### 3.1 Designing for Explainability

Explainability requirements depend on the impact classification and deployment context:

| Context | Minimum Explainability Requirement |
|---------|----------------------------------|
| Internal advisory tool (Low impact) | System-level description sufficient; per-output explanation not required |
| System informing consequential decisions (Medium impact) | Feature importance or comparable explanation available per output; users trained to interpret it |
| System used for high-stakes decisions affecting individuals (High impact) | Per-output explanation available; explanation accessible to affected individual; human reviewer must be able to validate the explanation |
| System interacting directly with members of the public | Disclosure that AI is being used; accessible explanation of how AI affects the interaction |

### 3.2 Transparency of Intended Use

User documentation (AI-POL-A.8.2-5) must be prepared alongside the system — not as a post-deployment task. The AI System Owner should draft the user documentation during development and validate it with representative users before deployment.

---

## Part 4 — Verification and Validation (V&V)

### 4.1 V&V Requirements by Impact Classification

| Requirement | Low Impact | Medium Impact | High Impact |
|------------|-----------|--------------|------------|
| Held-out test set | ✓ | ✓ | ✓ |
| Stratified evaluation by demographic group | Recommended | ✓ | ✓ (mandatory) |
| Performance against defined KPI thresholds | ✓ | ✓ | ✓ |
| Adversarial / edge case testing | Recommended | ✓ | ✓ (mandatory) |
| Human evaluation (sample-based) | Optional | Recommended | ✓ |
| Independent V&V reviewer | Optional | Recommended | ✓ (mandatory) |
| V&V documented and version-controlled | ✓ | ✓ | ✓ |
| V&V report reviewed by AI Governance Officer | Optional | Recommended | ✓ |

### 4.2 Defining Pass/Fail Criteria

V&V criteria must be defined **before** evaluation commences — not after results are available. The AI System Owner and development team document:
- What metrics will be used
- What threshold values constitute a pass
- What remediation is required if a threshold is not met

Setting criteria after seeing results is not acceptable and constitutes a V&V process failure.

### 4.3 V&V Record Contents

The V&V record for each AI system version shall include:
- AI system name and version
- V&V date(s) and assessors
- Dataset used for evaluation (name, version — different from training data)
- Metrics evaluated and results against thresholds
- Fairness evaluation results
- Edge case / adversarial test results
- Known limitations and conditions
- Pass / Fail decision with rationale
- Sign-off by AI System Owner

---

## Part 5 — Deployment Gate

### 5.1 What the Deployment Gate Requires

An AI system version may not be deployed to an operational environment without all of the following:

| Gate Criterion | Evidence Required |
|---------------|------------------|
| AISIA approved | AISIA document ID and AI Governance Officer approval date |
| V&V passed | V&V record with pass decision |
| User documentation prepared | Document reference |
| User training completed | Training completion records |
| Access controls configured | Confirmation from system administrator |
| Logging active | Technical confirmation |
| AI System Resource Register updated | Confirmation from AI System Owner |
| AI Governance Officer deployment approval | Email / ticket / formal approval |

### 5.2 Deployment to Production Without Gate Clearance

Deploying an AI system to production without gate clearance is a policy violation. If discovered:
1. System is suspended from operational use pending gate completion
2. AI Governance Officer and CISO notified
3. Root cause analysis — was this accidental or intentional?
4. Preventive measures to avoid recurrence

Development teams should treat the gate as a quality milestone, not a bureaucratic obstacle.

---

<!-- QA_VERIFIED: 2026-07-31 -->
