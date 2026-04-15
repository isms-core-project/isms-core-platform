<!-- ISMS-CORE:IMP:AI-IMP-A.2.2-4-UG:ai:UG:a.2.2-4 -->
**AI-IMP-A.2.2-4-UG — AI Policy Framework — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Policy Framework — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.2.2-4-UG |
| **Related Policy** | AI-POL-A.2.2-4 (AI Policy Framework) |
| **Document Creator** | AI Governance Officer |
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

**Review Cycle**: Annual (or upon significant change to the AI governance framework)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.2.2-4 (AI Policy Framework — governing policy)
- AI-IMP-A.2.2-4-TG (AI Policy Framework — Technical Guide)
- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- ISO/IEC 42001:2023 Controls A.2.2, A.2.3, A.2.4

---

## Purpose of This Guide

This guide explains **how to implement and maintain [Organisation]'s AI policy framework** — including how to create AI policies, how to keep them current, how to communicate them, and how to measure compliance. It is the practical companion to AI-POL-A.2.2-4.

**Who this guide is for**: AI Governance Officer, AI System Owners, Legal/Compliance, HR (for staff communication), and any person responsible for drafting or maintaining AI governance documents.

---

## Part 1 — The AI Policy Hierarchy

### 1.1 Understanding the AIMS Policy Structure

[Organisation]'s AI management system uses a three-tier policy structure:

| Tier | Documents | Purpose | Audience |
|------|-----------|---------|---------|
| **Tier 1** | AI-POL-00 (Regulatory Applicability), AI-POL-01 (Governance Framework), AI-POL-A.2.2-4 (AI Policy Framework) | Set the framework: what we must comply with, how governance works, what our principles are | Executive Management, AI Governance Officer |
| **Tier 2** | AI-POL-A.2.x through A.10.x (Control-specific policies) | Define WHAT must be done for each control area | AI System Owners, Control owners, technical staff |
| **Tier 3** | IMP-UG (User Guides) and IMP-TG (Technical Guides) | Define HOW to implement — practical guidance, templates, checklists | Practitioners, technical staff, operators |

Tier 1 governs Tier 2; Tier 2 governs Tier 3. A Tier 3 implementation guide cannot contradict a Tier 2 policy, and a Tier 2 policy cannot contradict a Tier 1 framework document.

### 1.2 What "AI Policy" Means Here

In the AIMS, "AI policy" refers to [Organisation]'s internal governance instruments — not the EU AI Act or other external regulation. [Organisation]'s AI policies are the internal rules that operationalise compliance with external requirements. AI-POL-00 and AI-POL-01 set the boundary between external requirements and internal policy responses.

---

## Part 2 — Responsible AI Principles in Practice

### 2.1 The Five Principles

AI-POL-A.2.2-4 establishes five responsible AI principles that apply to all in-scope AI systems. Here is how each principle translates into daily practice:

**1. Human agency and oversight**

*In practice*:
- Every AI system with a consequential output shall have a documented human review step
- Staff using AI systems are trained that accountability for decisions remains with the human, not the AI
- AI System Owners document the oversight mechanism in the AISIA and the intended use specification
- If an AI system is operating without a human review step (automated), this must be specifically approved and recorded

**2. Fairness and non-discrimination**

*In practice*:
- Training data must be assessed for demographic coverage and bias before use (AI-POL-A.7.2-6)
- AI outputs must be monitored for disparate performance across demographic groups in operation
- Any AI system that informs consequential decisions must include a bias assessment in the AISIA
- Users must be trained to recognise and report outputs that appear inconsistent across groups

**3. Privacy by design**

*In practice*:
- No personal data enters an AI system without a documented legal basis (PRIV-POL-00)
- Privacy implications are assessed in the AISIA (Section 7.4) before deployment
- Minimisation: AI systems shall not collect more personal data than necessary for their documented purpose
- AI System Owners ensure DPO is involved where personal data is material

**4. Robustness, security, and safety**

*In practice*:
- AI systems undergo V&V before deployment (AI-POL-A.6.2)
- Performance is monitored against defined thresholds in operation
- Security testing includes AI-specific attack vectors (adversarial inputs, model extraction, prompt injection for generative AI)
- AI incidents are escalated per the incident communication process (AI-POL-A.8.2-5)

**5. Accountability and transparency**

*In practice*:
- Every AI system has an owner — the AI System Owner — who is accountable for the system's compliance
- AISIA records are maintained and available to auditors
- Users and affected individuals receive transparency information about AI use (AI-POL-A.8.2-5)
- No AI system is anonymous in the governance records — all in-scope systems are registered

### 2.2 Principle Conflicts

Where two principles appear to conflict (e.g., a highly explainable model is less accurate, reducing reliability), the conflict is escalated to the AI Governance Officer. The AI Governance Officer applies a proportionality test: given the impact classification of the AI system, which trade-off is acceptable? High-impact systems may require both principles to be satisfied through design solutions. The decision is documented in the AISIA.

---

## Part 3 — Creating and Updating AI Policies

### 3.1 Who Initiates a New Policy

| Scenario | Who initiates |
|---------|--------------|
| New AI control area identified (new ISO 42001 version, new regulation) | AI Governance Officer |
| Gap in existing policy coverage identified during audit or AISIA | AI Governance Officer |
| Significant change to a regulated area (e.g., EU AI Act implementing measure) | AI Governance Officer / Legal |
| Request from Executive Management | AI Governance Officer |

### 3.2 Policy Drafting Process

1. **Initiation**: AI Governance Officer confirms the need and scope of the new or updated policy
2. **Drafting**: Lead author drafts using the standard AIMS policy template (document control table, executive summary, scope, policy statements, roles, evidence requirements, audit considerations)
3. **Stakeholder review**: 2-week review window; required reviewers: Legal, CISO, relevant AI System Owners
4. **Approval**: Per the approval chain in the policy document control table
5. **Communication**: New or updated policies are communicated to all affected staff per Part 4 of this guide
6. **Version control**: Policies are version-controlled; old versions retained per evidence retention requirements

### 3.3 Policy Review Triggers

Existing policies must be reviewed:
- On their scheduled review date (minimum annual)
- When a relevant regulation changes materially (e.g., EU AI Act implementing acts)
- When an audit finding indicates a policy gap
- When an AI incident reveals a control deficiency not addressed by current policy
- When [Organisation]'s AI system portfolio changes significantly

### 3.4 Managing Conflicts Between Policies

Where a specific AI policy appears to conflict with another AIMS document, or with an ISMS policy:
1. The AI Governance Officer and CISO resolve the conflict bilaterally
2. If unresolved: escalate to Executive Management for decision
3. Interim: the more restrictive requirement applies until the conflict is resolved
4. Resolution is documented in both affected policies

---

## Part 4 — Communicating AI Policies to Staff

### 4.1 Awareness Requirements by Audience

Not all staff need equal depth of awareness. The following matrix guides minimum awareness:

| Audience | Minimum Awareness Required | Delivery Method |
|---------|--------------------------|----------------|
| All staff | [Organisation] uses AI systems; AI governance principles; how to report AI concerns | Annual all-staff communication; AIMS induction for new joiners |
| AI system users (operational) | Intended use and limitations of AI systems they use; responsible use rules; how to report concerns | Training before access; refresher when system changes |
| AI System Owners | Full AI-POL suite awareness; AISIA requirements; incident reporting obligations | Initial AIMS training; annual update |
| Executive Management | AIMS scope; key obligations; High-impact AI system approvals; risk posture | Annual management review |
| AI development team | AI governance policies for development (A.6.1, A.6.2, A.7.2-6); responsible AI principles | Technical training; AIMS induction |

### 4.2 Communication for New Policies

When a new policy or material update is issued:
1. AI Governance Officer drafts a plain-language summary (1 page maximum)
2. Summary is distributed to affected staff via [Organisation]'s standard internal communication channel
3. Affected staff acknowledge receipt where the policy imposes new obligations on them
4. Training is updated where the policy change requires it

### 4.3 Policy Availability

All current AI policies shall be accessible to all staff who need them. The AI Governance Officer maintains a document register with links to current policy versions. Staff must be able to find:
- The current version of any AI policy within 5 minutes
- Who to contact with questions about a policy

---

## Part 5 — Monitoring Policy Effectiveness

### 5.1 Indicators of Effective AI Policy

The AI Governance Officer monitors the following indicators annually:

| Indicator | How Measured | Target |
|---------|-------------|--------|
| AISIA completion rate | % of in-scope AI systems with current AISIA | 100% |
| Policy awareness | Training completion rates per audience category | ≥ 95% |
| Incidents potentially caused by policy non-compliance | Count from incident register | Trend down |
| Audit findings relating to AI policy gaps | Count from internal / external audit | Zero critical findings |
| Policy reviews on schedule | % of due reviews completed on time | 100% |

### 5.2 Annual AIMS Management Review Input

The AI Governance Officer prepares an AIMS governance report for the annual management review covering:
- Status of all AI policy documents (current / overdue for review)
- Policy effectiveness indicators
- Material policy changes made in the period
- Proposed policy additions or updates for the coming period

---

<!-- QA_VERIFIED: [2026-04-15] -->
