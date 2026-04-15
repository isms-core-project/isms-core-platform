<!-- ISMS-CORE:IMP:AI-IMP-A.9.2-4-UG:ai:UG:a.9.2-4 -->
**AI-IMP-A.9.2-4-UG — Responsible Use of AI Systems — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Responsible Use of AI Systems — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.9.2-4-UG |
| **Related Policy** | AI-POL-A.9.2-4 (Responsible Use of AI Systems) |
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

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.9.2-4 (Responsible Use of AI Systems — governing policy)
- AI-IMP-A.9.2-4-TG (Responsible Use of AI Systems — Technical Guide)
- AI-IMP-A.5.2-5-UG (AISIA — intended use basis)
- AI-POL-A.8.2-5 (Information for Interested Parties — user documentation and transparency)
- ISO/IEC 42001:2023 Controls A.9.2–A.9.4

---

## Purpose of This Guide

This guide explains **how to implement responsible AI use processes** — including how to configure and run the pre-use verification process, how to run the ongoing operational oversight process, and how to respond to misuse or out-of-scope use. It is the practical companion to AI-POL-A.9.2-4.

**Who this guide is for**: AI System Owners, operations/business function leads, and anyone responsible for managing AI systems in operation.

---

## Part 1 — Pre-Use Verification (A.9.2 Process 1)

### 1.1 Before Any Operational Use Commences

For every AI system being put into operational use for the first time, the AI System Owner completes a Pre-Use Verification Record confirming:

| Verification Item | Evidence Required |
|-----------------|-----------------|
| Current approved AISIA exists | AISIA document ID and approval date |
| Intended use for this context is within AISIA scope | Confirm the operational context matches the intended use specification |
| All users have completed required training | Training completion records per user category |
| Human oversight mechanisms are in place and tested | Technical confirmation; runbook reference |
| Logging is active | Technical confirmation from IT/DevOps |
| User documentation is available and accessible | Document reference; link confirmed |

This record is held by the AI System Owner and available to the AI Governance Officer on request.

### 1.2 When a New User Category Begins Using an Existing System

If a new category of users (e.g., a different business unit, or external partners) begins using an AI system that is already in operation:
1. AI System Owner confirms the new use falls within the existing intended use specification
2. New users receive training before access is granted
3. Access controls are updated
4. Pre-Use Verification is updated to record the new user category

If the new use is outside the existing intended use: treat it as a material change requiring AISIA review (AI-IMP-A.6.2-UG Part 4).

---

## Part 2 — Operational Oversight (A.9.2 Process 2)

### 2.1 Human Review in Practice

For AI systems where human review is required (per the intended use specification and AISIA), the AI System Owner must ensure the review actually happens — not just that a review step exists in theory.

**What "meaningful human review" means**:
- The reviewer understands what the AI output means and what it is based on
- The reviewer has sufficient information to make an independent judgment
- The reviewer's decision is recorded (not just the AI output)
- The reviewer has the authority and realistic ability to override the AI output
- The reviewer is not so time-pressured that review is perfunctory

**What it does NOT mean**:
- A rubber-stamp that happens in two seconds
- A reviewer who lacks the domain knowledge to evaluate AI outputs
- A checkbox that records "reviewed" without any actual scrutiny

If the AI System Owner observes that human review is not being conducted meaningfully, this is a compliance issue that must be escalated to the AI Governance Officer.

### 2.2 Monitoring for Intended Use Compliance

Beyond performance monitoring (AI-IMP-A.6.2-UG Part 3), the AI System Owner monitors operational use against the intended use specification:

| Monitoring Question | How to Monitor |
|--------------------|---------------|
| Are users using the system only for its intended purpose? | Review use logs; user-reported issues; audit samples |
| Are users exercising the required human oversight? | Review human review logs; sample quality checks |
| Are any outputs raising fairness or discrimination concerns? | Sample-based output review; user feedback channel |
| Is the volume and type of use consistent with what was assessed in the AISIA? | Compare operational metrics against AISIA scope assumptions |

---

## Part 3 — Intended Use Enforcement (A.9.4)

### 3.1 What AI System Owners Must Do

For each AI system, maintain and enforce the intended use specification:

1. **Keep it current**: The intended use specification must accurately reflect how the system is deployed. If operations have evolved beyond the specification, update it (with AI Governance Officer review) — do not leave a gap between reality and documentation.

2. **Communicate it to users**: Users must know what the system is for, what it is not for, and what is prohibited. This is covered in user documentation (AI-POL-A.8.2-5), but the AI System Owner must verify users have read and understood it.

3. **Enforce it through access controls**: Access rights should match authorised use. Staff who have no legitimate reason to access an AI system should not have access.

4. **Monitor for boundary violations**: Use logs to identify access or use patterns outside the intended scope.

### 3.2 Scope Creep

Scope creep is one of the most common intended use violations — the system gradually gets used for more things than it was originally designed for. Signs of scope creep:
- Users asking "can the AI also do X?" where X was not in the original scope
- Outputs from the AI system being used in workflows that were not assessed in the AISIA
- A growing list of "unofficial" uses that staff have discovered the system can do

Scope creep is not always malicious — it is often well-intentioned. But undocumented expanded use creates compliance exposure. When the AI System Owner identifies scope creep:
1. Document the observed out-of-scope use
2. Escalate to AI Governance Officer
3. Decision: cease out-of-scope use, OR initiate AISIA update to formally expand the intended use

---

## Part 4 — Responding to Misuse

### 4.1 Misuse Detection

Misuse is use of an AI system in a way that violates the intended use specification, including prohibited uses. Detection methods:
- User reporting through the A.3.3 concerns channel
- AI System Owner monitoring of use logs
- Automated alerting where use patterns trigger thresholds
- Outputs review identifying content inconsistent with intended use

### 4.2 Misuse Response Process

When misuse is detected or reported:

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Log the misuse event with date, description, and evidence | AI System Owner |
| 2 | Notify AI Governance Officer within [24 hours] | AI System Owner |
| 3 | Assess severity: is there potential harm to individuals? | AI Governance Officer + AI System Owner |
| 4 | If potential harm: initiate AI incident process (AI-POL-A.8.2-5 A.8.4) | AI Governance Officer |
| 5 | Identify the misuse actor: individual, team, or systemic pattern? | AI System Owner |
| 6 | Response options: user guidance and retraining / access restriction / system suspension | AI Governance Officer decides |
| 7 | Root cause analysis: why did the misuse occur? Gap in training? Unclear guidance? | AI System Owner + AI Governance Officer |
| 8 | Preventive measure: update training, documentation, or access controls | AI System Owner |
| 9 | Log outcome and close event | AI Governance Officer |

### 4.3 Serious Misuse

Where misuse has caused or could cause harm to individuals or constitutes a material violation of [Organisation]'s responsible AI principles:
- AI Governance Officer notifies Executive Management
- Legal is involved
- Incident communication process activated if external notification required
- HR involved if the misuse actor is an employee

---

<!-- QA_VERIFIED: [2026-04-15] -->
