<!-- ISMS-CORE:IMP:AI-IMP-A.8.2-5-UG:ai:UG:a.8.2-5 -->
**AI-IMP-A.8.2-5-UG — Information for Interested Parties — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Information for Interested Parties — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.8.2-5-UG |
| **Related Policy** | AI-POL-A.8.2-5 (Information for Interested Parties) |
| **Document Creator** | AI Governance Officer / Communications Officer |
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

- AI-POL-A.8.2-5 (Information for Interested Parties — governing policy)
- AI-IMP-A.8.2-5-TG (Information for Interested Parties — Technical Guide)
- AI-POL-A.9.2-4 (Responsible Use — A.9.4 intended use specification)
- ISO/IEC 42001:2023 Controls A.8.2–A.8.5

---

## Purpose of This Guide

This guide explains **how to prepare, communicate, and manage AI system information for different audiences** — from user documentation and transparency notices to external reporting and incident communication. It is the practical companion to AI-POL-A.8.2-5.

**Who this guide is for**: AI System Owners, Communications/Legal, Account Management, Customer Success, and anyone responsible for communicating about AI systems to internal or external audiences.

---

## Part 1 — User Documentation

### 1.1 Who Produces User Documentation

The AI System Owner is responsible for ensuring user documentation exists and is current. In practice, the AI System Owner may coordinate with technical writers, product teams, or Legal to produce the documentation — but the AI System Owner approves it and is accountable for its accuracy.

### 1.2 When Documentation Must Be Available

User documentation must be available **before or at the point of deployment**. It is not an optional post-launch task. At the deployment gate (AI-IMP-A.6.2-UG), confirmed documentation availability is a gate criterion.

### 1.3 Writing Effective User Documentation

User documentation must be **accessible** — not a technical manual or legal disclaimer. Test: can a typical user of this system read the documentation and answer these questions within five minutes?

- What does this AI system do?
- What should I use it for? What should I NOT use it for?
- What are its limitations? When should I NOT rely on its outputs?
- What do I need to do to use it responsibly?
- Who do I contact if something goes wrong or I have a concern?

If the answer to any of these is "no, the documentation doesn't help with that" — revise it.

**Avoid**:
- Technical jargon that users of the system will not understand
- Generic disclaimers copied from legal templates
- Phrases like "use at your own risk" without substantive guidance
- Documentation buried in terms and conditions

**Include**:
- Plain language description of how AI works in this system
- Concrete examples of appropriate and inappropriate use
- Specific guidance on the human oversight required
- How to report concerns (link to the A.3.3 channel)

### 1.4 Language and Accessibility

If the intended user audience includes non-English speakers, documentation must be available in their language(s). For customer-facing AI systems in Switzerland, France, Germany, or Italy: French, German, or Italian versions are required per the country deployment scope (AI-POL-00).

---

## Part 2 — Transparency Notices for Affected Individuals

### 2.1 When a Transparency Notice Is Required

A transparency notice is required wherever an AI system:
- Interacts directly with members of the public or customers (EU AI Act Article 50)
- Makes or significantly influences decisions that affect individuals who are not direct users
- Generates content that could be mistaken for human-generated content
- Uses emotion recognition, biometric categorisation, or deep fake technology

If uncertain: consult the AI Governance Officer. The default is to provide a transparency notice.

### 2.2 What the Notice Must Say

Transparency notices must be written in plain language. They must include:
- That an AI system is being used (unless obvious from context)
- What the AI system does in this context
- Whether AI output influences decisions about the individual
- What rights or recourse the individual has
- Who to contact with questions

The notice must be displayed **before or at the time of interaction** — not in a privacy policy that nobody reads.

### 2.3 EU AI Act Specific Disclosures

For AI systems subject to EU AI Act Article 50 obligations:

| System Type | Required Disclosure |
|------------|---------------------|
| AI chatbot / virtual assistant | Inform users they are interacting with an AI — unless clearly evident |
| Emotion recognition system | Inform individuals before and during exposure |
| Biometric categorisation | Inform individuals exposed to the system |
| AI-generated content that could be mistaken for human | Label the content as AI-generated |
| Deep synthetic audio/video | Mark as artificially generated or manipulated |

---

## Part 3 — External Reporting Process

### 3.1 Responding to Information Requests

Any external request for information about [Organisation]'s AI systems (from a regulator, customer, civil society body, journalist, or member of the public) is routed as follows:

1. Request received by the point of contact or whoever first receives it
2. Forwarded to AI Governance Officer within [1 business day]
3. AI Governance Officer assesses: what is being asked? Who is asking? What is the applicable obligation?
4. Response drafted by AI Governance Officer with Legal support
5. Approved by AI Governance Officer (and Legal for regulatory requests)
6. Response sent within the required timeframe:
   - Regulatory requests: per applicable regulatory deadline
   - Standard requests: within 10 business days
7. Request and response logged in the external reporting register

### 3.2 Proactive External Reporting

Do not wait for requests. Proactively publish or provide:
- Customer-facing AI documentation for all AI-enabled products (AI-POL-A.10.2-4)
- Website transparency statement (where [Organisation] uses AI publicly)
- EU AI Act technical documentation for high-risk systems — available to market surveillance authorities on request

---

## Part 4 — AI Incident Communication

### 4.1 Internal Communication — First Steps

When an AI incident or near-miss is detected:
1. Person detecting the incident notifies the AI System Owner immediately
2. AI System Owner logs the incident and notifies the AI Governance Officer within:
   - **Serious incident** (death, serious injury, significant harm, fundamental rights breach): within [2] hours
   - **Material incident** (harm to individuals, significant malfunction): within [24] hours
   - **Near-miss**: within [3] business days
3. AI Governance Officer notifies CISO (if information security dimension) and DPO (if personal data involved)

### 4.2 External Communication — When to Notify

| Party | Trigger | Timeframe | Who Manages |
|-------|---------|-----------|-------------|
| **Regulatory authority** | Serious incident involving high-risk AI (EU AI Act Article 73); personal data breach (GDPR Article 33) | Per applicable deadline (GDPR: 72 hours; EU AI Act: without undue delay) | Legal / AI Governance Officer |
| **Affected individuals** | AI incident causing harm to identified individuals; GDPR Article 34 high-risk data breach | Without undue delay | DPO / Communications |
| **Customers** | AI incident materially affecting services or involving customer data | Per contractual obligation | Account Management / Legal |
| **Public** | Where incident has significant public interest impact | Coordinated with Legal; no unilateral public statements | AI Governance Officer / Communications |

### 4.3 What Not to Do

- Do not make public statements about an AI incident without AI Governance Officer and Legal approval
- Do not downplay a serious incident to avoid regulatory notification — this creates greater liability
- Do not delay notifying affected individuals where their safety or rights are at immediate risk
- Do not notify customers or the public before the AI Governance Officer and Legal have assessed the situation

---

<!-- QA_VERIFIED: [2026-04-15] -->
