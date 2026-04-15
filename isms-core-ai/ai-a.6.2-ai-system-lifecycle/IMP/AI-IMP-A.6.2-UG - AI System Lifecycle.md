<!-- ISMS-CORE:IMP:AI-IMP-A.6.2-UG:ai:UG:a.6.2 -->
**AI-IMP-A.6.2-UG — AI System Lifecycle — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Lifecycle — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.6.2-UG |
| **Related Policy** | AI-POL-A.6.2 (AI System Lifecycle) |
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

- AI-POL-A.6.2 (AI System Lifecycle — governing policy)
- AI-IMP-A.6.2-TG (AI System Lifecycle — Technical Guide)
- AI-POL-A.6.1 (AI Development Governance)
- AI-IMP-A.5.2-5-UG (AISIA process — deployment gate)
- ISO/IEC 42001:2023 Controls A.6.2.1–A.6.2.9

---

## Purpose of This Guide

This guide explains **how to manage an AI system through its full lifecycle** — from specification through deployment, operation, change management, monitoring, and decommissioning. It is the practical companion to AI-POL-A.6.2.

**Who this guide is for**: AI System Owners, ML Engineers, operations teams, and AI development leads.

---

## Part 1 — The AI System Lifecycle at [Organisation]

### 1.1 Lifecycle Stages

[Organisation]'s AI systems pass through six lifecycle stages. Each stage has specific governance requirements.

| Stage | Description | Key Governance Requirement |
|-------|-------------|--------------------------|
| **1. Specification** | Define requirements, intended use, scope | Intended use specification documented; preliminary AISIA initiated |
| **2. Development** | Build, train, and iterate | Development governance (AI-IMP-A.6.1); data governance (AI-POL-A.7.2-6) |
| **3. V&V** | Validate the system meets its specification | V&V record completed per AI-IMP-A.6.1-TG |
| **4. Deployment** | Deploy to operational environment | Deployment gate clearance; AISIA approved |
| **5. Operation** | System in operational use | Operational monitoring; human oversight; incident response |
| **6. Decommissioning** | End of operational life | Data deletion; documentation retention; transition management |

An AI system may cycle through stages 2–4 multiple times as new versions are developed and deployed.

### 1.2 Lifecycle Governance Is the AI System Owner's Responsibility

The AI System Owner is responsible for governance at each lifecycle stage for their system. They are not responsible for doing everything themselves — but they are responsible for ensuring governance happens and escalating when it does not.

---

## Part 2 — Specification Stage (A.6.2.2)

### 2.1 What the Specification Must Cover

Before development commences, the AI System Owner documents the AI system specification. This is the starting point for all downstream governance — AISIA, V&V criteria, user documentation, and the intended use enforcement.

**Minimum specification content**:
- System name and purpose
- Intended use statement (who, what, where, to what end)
- Intended users and their competency requirements
- Intended operational context and deployment environment
- Output type and how outputs are used
- Sensitive use assessment (does this involve vulnerable populations, consequential decisions?)
- Performance requirements (what does "good enough" mean for this system?)
- Constraints (what the system must NOT do)
- Integration requirements (what systems does this connect to?)

### 2.2 Specification Approval

Before development commences, the specification is reviewed and approved by the AI Governance Officer. This approval confirms that:
- The intended use is within the AIMS scope
- A preliminary AISIA has been initiated
- Data governance has been notified (if personal data involved)
- Responsible AI considerations are reflected in the specification

---

## Part 3 — Operation Stage (A.6.2.4–A.6.2.8)

### 3.1 Pre-Operational Checklist

Before an AI system enters operational use, the AI System Owner confirms:

| Item | Status |
|------|--------|
| AISIA approved | ☐ |
| V&V completed and passed | ☐ |
| User documentation accessible | ☐ |
| Users trained | ☐ |
| Monitoring active (KPIs defined, alerts configured) | ☐ |
| Logging active | ☐ |
| Human oversight mechanism in place | ☐ |
| Access controls configured | ☐ |
| AI Governance Officer deployment approval received | ☐ |

### 3.2 Operational Monitoring

Once deployed, the AI System Owner maintains a monitoring regime:

**What to monitor**:
- Primary performance metric (against threshold defined in V&V criteria)
- Error rate or exception rate
- Distribution of inputs (detecting distribution shift — inputs diverging from training distribution)
- Distribution of outputs (detecting unexpected output patterns)
- Volume and access patterns (detecting use outside intended scope)
- Human oversight compliance (are humans doing their review?)

**Monitoring frequency**:
- High-impact systems: continuous automated monitoring + weekly human review
- Medium-impact systems: automated monitoring + monthly human review
- Low-impact systems: automated monitoring + quarterly human review

**When to escalate**:
| Condition | Action |
|-----------|--------|
| Performance metric breaches alert threshold | AI System Owner investigates and decides: continue (monitored), retrain, or suspend |
| Distribution shift detected | AI System Owner reviews — may require retraining or AISIA review |
| Unexpected output patterns that could affect individuals | AI System Owner escalates to AI Governance Officer; potential incident |
| Volume / access pattern outside expected range | AI System Owner investigates; potential misuse response |

### 3.3 Logging Requirements

Logs must be sufficient to support:
- Incident investigation (reconstruct what happened and when)
- Audit and compliance verification
- Regulatory requests (EU AI Act Article 12 logging for high-risk systems)

Minimum log retention:
- High-impact systems: 12 months operational logs + extended per regulatory requirement
- Medium-impact systems: 6 months
- Low-impact systems: 3 months

Logs must be stored where they cannot be modified by the AI system's operators (integrity-protected).

---

## Part 4 — Change Management (A.6.2.5)

### 4.1 What Counts as a Material Change

A material change requires the full deployment gate process before the changed version is deployed to production.

Material changes include:
- New version of the underlying model (re-trained or fine-tuned)
- New training dataset or significant change to existing dataset
- New use case or expanded intended use
- New user population or affected population
- New deployment environment or integration
- Significant change to human oversight mechanism

### 4.2 Minor Changes

Minor changes (bug fixes, UI changes, non-material configuration updates) may be deployed via the standard change management process without a full AISIA review, provided:
- The AI System Owner confirms in writing the change is non-material
- The change does not affect model outputs, training data, or deployment scope
- The AI System Resource Register is updated to reflect the new version

If there is doubt about whether a change is material: treat it as material and consult the AI Governance Officer.

### 4.3 Emergency Changes

If an urgent change is required (e.g., critical security patch to an AI system):
1. CISO and AI System Owner agree the emergency change is necessary
2. Change is deployed with the most expedient safe procedure
3. Full documentation and AISIA review completed within [5 business days] of emergency deployment
4. AI Governance Officer notified before or immediately after deployment

---

## Part 5 — Decommissioning (A.6.2.9)

### 5.1 Decommissioning Triggers

An AI system is decommissioned when:
- It is replaced by a new system
- Its business purpose is discontinued
- It can no longer be maintained in a compliant state
- The AI Governance Officer determines it poses unacceptable risk

### 5.2 Decommissioning Process

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Notify AI Governance Officer of planned decommissioning | AI System Owner |
| 2 | Notify all users with adequate lead time ([minimum X days]) | AI System Owner |
| 3 | If customers affected: notify per contractual obligations (AI-POL-A.10.2-4) | Account Management |
| 4 | Cease operational use on the agreed decommissioning date | AI System Owner |
| 5 | Securely delete training data per GDPR Article 17 obligations (where applicable) | DPO / Data Governance Lead |
| 6 | Retain AISIA, V&V records, model card per retention schedule (5 years post-decommission) | AI Governance Officer |
| 7 | Update AI System Resource Register: status = Decommissioned, date recorded | AI System Owner |
| 8 | Confirm access revocation from decommissioned system | IT / CISO |

### 5.3 What Happens to Data After Decommissioning

- Training data: deleted per AI-POL-A.7.2-6 data lifecycle requirements and GDPR Article 17 (if personal data)
- Operational logs: retained for the defined log retention period from the last operational use
- Model artefacts (weights, binaries): deleted or archived securely per AI Governance Officer decision
- AISIA, V&V records, model card: retained for 5 years post-decommission as audit evidence

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
