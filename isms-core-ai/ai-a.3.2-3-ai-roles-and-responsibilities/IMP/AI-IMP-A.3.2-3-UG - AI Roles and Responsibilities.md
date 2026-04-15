<!-- ISMS-CORE:IMP:AI-IMP-A.3.2-3-UG:ai:UG:a.3.2-3 -->
**AI-IMP-A.3.2-3-UG — AI Roles and Responsibilities — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Roles and Responsibilities — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.3.2-3-UG |
| **Related Policy** | AI-POL-A.3.2-3 (AI Roles and Responsibilities) |
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

- AI-POL-A.3.2-3 (AI Roles and Responsibilities — governing policy)
- AI-IMP-A.3.2-3-TG (AI Roles and Responsibilities — Technical Guide)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- ISO/IEC 42001:2023 Controls A.3.2, A.3.3

---

## Purpose of This Guide

This guide explains **how to assign, communicate, and maintain AI governance roles** at [Organisation] — including onboarding new role holders, handling the concerns reporting channel, and managing role transitions. It is the practical companion to AI-POL-A.3.2-3.

**Who this guide is for**: AI Governance Officer, HR, Managers nominating staff for AI governance roles, and any individual taking on an AI governance responsibility for the first time.

---

## Part 1 — Understanding AI Governance Roles

### 1.1 Role Overview

[Organisation]'s AIMS assigns responsibilities across six role categories. Understanding which role applies to you determines what policies you must follow and what obligations you carry.

| Role | What it means in practice |
|------|--------------------------|
| **AI Governance Officer** | The person accountable for the AIMS as a system. Approves all AISIAs, owns the policy suite, chairs governance reviews. Typically one individual, named. |
| **AI Risk Owner** | Business executive accountable for the risk profile of specific AI systems. Commissions AISIAs, accepts residual risk. May be the same person for multiple systems; typically a senior leader in the business function using AI. |
| **AI System Owner** | The person responsible for a specific AI system day-to-day. Maintains documentation, monitors performance, manages incidents for that system. Every in-scope AI system must have exactly one named AI System Owner. |
| **CISO** | The ISMS and security lead. Reviews security dimensions of AI systems; coordinates AI security incidents; manages supplier security monitoring. |
| **DPO / Privacy Officer** | Reviews AI systems involving personal data; ensures GDPR compliance for AI training data and AI-driven processing. |
| **AI system users** | All staff who use AI systems in their work. Obligated to use AI systems within their intended purpose and report concerns. |

### 1.2 Multiple Role Holders

In a smaller organisation, one person may hold multiple AI governance roles. Acceptable combinations:
- AI Governance Officer + DPO: acceptable provided there is no conflict between AI governance and privacy obligations
- AI Risk Owner for multiple systems: acceptable
- AI System Owner for multiple systems: acceptable provided review obligations for each system can be met

Not acceptable (conflict of interest):
- AI Governance Officer + AI System Owner for a High-impact AI system (the approver cannot also be the assessed)
- AI Risk Owner + AI Governance Officer: the risk acceptor and the governance approver should be distinct

### 1.3 The AI System Owner Role in Detail

The AI System Owner is the most common AI governance role. Every person who becomes an AI System Owner should understand the following obligations:

| Obligation | What it means |
|-----------|--------------|
| Maintain AISIA currency | The AISIA for your system must be current. When the system changes materially, you initiate a new or updated AISIA. |
| Maintain intended use documentation | The documented intended use must accurately reflect how the system is deployed. If use has drifted, you notify the AI Governance Officer. |
| Monitor system performance | You are responsible for monitoring against KPIs. If KPIs breach thresholds, you escalate. |
| Report AI incidents | If an AI incident occurs involving your system, you are the first responder — notify the AI Governance Officer within the required timeframe. |
| Maintain user documentation | Users of your system must have current documentation on what the system does, its limitations, and how to report concerns. |
| Manage access | You control who has access to your AI system and review that access when people change roles or leave. |
| Attend AISIA reviews | You participate in scheduled AISIA reviews for your system and implement measures identified in the AISIA. |

---

## Part 2 — Assigning AI Governance Roles

### 2.1 Appointing an AI System Owner

When a new AI system enters the AIMS scope:

1. **AI Governance Officer** identifies the appropriate AI System Owner (typically the business function lead responsible for the system's use)
2. **AI Governance Officer** formally notifies the nominee and their line manager in writing
3. **AI System Owner** receives an onboarding briefing (Part 3 of this guide)
4. **AI System Owner** is formally recorded in the AI System Resource Register (AI-POL-A.4.2-6) against the system
5. Role is confirmed in any relevant HR records or job description where [Organisation]'s HR practices require it

### 2.2 Appointing an AI Risk Owner

1. **AI Governance Officer** proposes an AI Risk Owner to Executive Management for each in-scope AI system
2. **Executive Management** confirms the AI Risk Owner appointment
3. **AI Risk Owner** is recorded in the AI System Resource Register and the AISIA for the relevant system
4. AI Risk Owner receives a briefing on their obligations (see AI-POL-A.3.2-3 and this guide)

### 2.3 Role Transitions

When an AI governance role holder leaves their role (resignation, role change, organisational restructure):

1. Outgoing role holder notifies AI Governance Officer at least 4 weeks before departure
2. AI Governance Officer identifies replacement
3. Handover documentation prepared — covering: current AISIA status; open incidents; system monitoring status; any ongoing issues
4. Replacement formally recorded in AI System Resource Register
5. AI Governance Officer confirms continuity — no AI system may be without a named AI System Owner at any time

If a replacement cannot be found before departure: AI Governance Officer acts as interim AI System Owner.

---

## Part 3 — AI System Owner Onboarding

### 3.1 Onboarding Checklist

New AI System Owners should complete the following within their first [30] days:

| Step | Description | Completed |
|------|-------------|-----------|
| 1 | Read AI-POL-A.3.2-3 (Roles and Responsibilities) | ☐ |
| 2 | Read AI-POL-A.5.2-5 (AISIA) and AI-IMP-A.5.2-5-UG | ☐ |
| 3 | Read the current AISIA for your AI system(s) | ☐ |
| 4 | Review the AI System Resource Register entry for your system(s) | ☐ |
| 5 | Review the intended use specification for your system(s) | ☐ |
| 6 | Confirm user documentation is current and accessible | ☐ |
| 7 | Confirm monitoring KPIs are active and documented | ☐ |
| 8 | Confirm the AI concerns reporting channel is known to users of your system | ☐ |
| 9 | Meet with the AI Governance Officer for a briefing on AIMS governance | ☐ |
| 10 | Confirm your contact details are recorded in the AI System Resource Register | ☐ |

### 3.2 When Your System Has No Current AISIA

If you become AI System Owner for a system that has no completed AISIA, or where the AISIA is materially out of date:

1. Notify the AI Governance Officer immediately
2. Determine whether the system should be considered deployed without an approved AISIA
3. If yes: the system may need to be suspended pending AISIA completion — this is a governance risk to escalate, not ignore
4. Initiate AISIA process per AI-IMP-A.5.2-5-UG

---

## Part 4 — The AI Concerns Reporting Channel (A.3.3)

### 4.1 What the Channel Is For

[Organisation]'s AI concerns reporting channel allows any person — staff, contractors, third parties — to raise concerns about:
- An AI system behaving in an unexpected or potentially harmful way
- Potential misuse of an AI system
- A possible breach of [Organisation]'s responsible AI principles
- A concern about an AI-driven decision affecting an individual

The channel is not a general IT helpdesk. It is a governance escalation path for AI-related concerns.

### 4.2 How the Channel Works

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Person raises concern via [designated channel — email / form / portal / hotline] | Concern raiser |
| 2 | AI Governance Officer receives and logs the concern within [1 business day] | AI Governance Officer |
| 3 | Concern is categorised: incident / potential misuse / policy question / other | AI Governance Officer |
| 4 | If incident: AI incident process initiated (AI-POL-A.8.2-5) | AI Governance Officer |
| 5 | If potential misuse: AI System Owner notified; investigation initiated | AI Governance Officer + AI System Owner |
| 6 | If policy question: AI Governance Officer responds within [5 business days] | AI Governance Officer |
| 7 | Concern raiser receives acknowledgment within [2 business days] and outcome within [15 business days] | AI Governance Officer |
| 8 | All concerns and outcomes logged in AI concerns register | AI Governance Officer |

### 4.3 Non-Retaliation Guarantee

Any person who raises a concern in good faith through the AI concerns channel — including where the concern later proves unfounded — shall not face any negative consequence for doing so. This protection applies equally to concerns raised internally and concerns reported to regulatory authorities.

The AI Governance Officer shall monitor for any indication of retaliation against concern raisers and escalate any such indication to Executive Management.

### 4.4 Training Staff on the Channel

All staff who use AI systems shall be informed:
- That the concerns channel exists
- How to access it (link / contact details)
- That there is no retaliation for good-faith concerns
- What types of concerns to raise

This awareness is delivered as part of AI system user training (AI-POL-A.9.2-4) and reinforced annually.

---

## Part 5 — Common Questions

**Q: I'm an AI System Owner — what if I notice my system is being used outside its intended purpose?**

A: Escalate immediately to the AI Governance Officer. Document what you observed and when. The AI Governance Officer will determine whether use should be suspended, whether user retraining is sufficient, or whether a formal misuse response is required (per AI-POL-A.9.2-4 A.9.2 Misuse Detection Process).

**Q: I've noticed the AI system I use seems to produce unfair outputs for certain groups. Should I report it?**

A: Yes — this is exactly what the AI concerns channel is for. Report the concern with as much specific detail as possible (which system, what outputs, which groups, when observed). You will not face any negative consequence for raising this in good faith.

**Q: I'm a new AI System Owner and I think the previous owner missed some AISIA reviews. What do I do?**

A: Notify the AI Governance Officer. They will determine whether the overdue reviews are a material governance gap and prioritise the work. This is not your personal liability — it is a governance issue to address, not conceal.

**Q: My AI system is a small internal tool that barely qualifies as "AI". Does it still need an AI System Owner?**

A: If it is in the AIMS scope, yes. If you believe the system should be out of scope, request a scope review from the AI Governance Officer. The AI Governance Officer applies the scoping criteria in the AIMS Scope Statement and makes a documented decision.

---

<!-- QA_VERIFIED: 2026-04-15 -->
