<!-- ISMS-CORE:IMP:AI-IMP-A.3.2-3-TG:ai:TG:a.3.2-3 -->
**AI-IMP-A.3.2-3-TG — AI Roles and Responsibilities — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Roles and Responsibilities — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.3.2-3-TG |
| **Related Policy** | AI-POL-A.3.2-3 (AI Roles and Responsibilities) |
| **Document Creator** | AI Governance Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial technical guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.3.2-3 (AI Roles and Responsibilities — governing policy)
- AI-IMP-A.3.2-3-UG (AI Roles and Responsibilities — User Guide)

---

## Purpose of This Guide

This guide provides the **schemas, templates, and reference structures** for implementing AI governance roles — including the AI Role Assignment Register schema, the AI concerns register schema, role appointment letter template, and competency requirements by role.

**Audience**: AI Governance Officer, HR, compliance.

---

## 1. AI Role Assignment Register Schema

The AI Governance Officer maintains an AI Role Assignment Register documenting all named role holders. Minimum schema:

| Field | Type | Description |
|-------|------|-------------|
| Role | Enum | AI Governance Officer / AI Risk Owner / AI System Owner / CISO / DPO / Other |
| Role Holder Name | Text | Full name |
| Role Holder Title / Position | Text | Current job title |
| Business Unit | Text | Organisational unit |
| Appointed Date | Date | Date role formally assigned |
| AI System(s) | Text | For AI System Owner / AI Risk Owner: list of assigned AI systems |
| Backup / Deputy | Text | Named backup if role holder unavailable |
| Training Completed | Date | Date of role-specific training completion |
| Next Training Refresh | Date | Date of next required training |
| Status | Enum | Active / Pending onboarding / Transitioning / Vacant |
| Notes | Text | Any relevant notes |

**Key constraints**:
- Every in-scope AI system must have exactly one AI System Owner with Status = Active
- AI Governance Officer: exactly one named individual (or named acting) at all times
- Vacant status triggers immediate escalation to Executive Management

---

## 2. AI Concerns Register Schema

The AI Governance Officer maintains an AI Concerns Register to log all concerns raised through the A.3.3 channel.

| Field | Type | Description |
|-------|------|-------------|
| Concern ID | Text | Unique ID (e.g., CONCERN-2026-001) |
| Date Received | Date | |
| Received Via | Enum | Email / Form / Portal / Verbal (documented) / Anonymous |
| Raiser Identity | Text | Name or "Anonymous" |
| Concern Category | Enum | Potential incident / Misuse / Policy concern / Discriminatory output / Privacy concern / Safety concern / Other |
| AI System Affected | Text | Which AI system, if identified |
| Concern Description | Text | Summary of the concern |
| Date Acknowledged | Date | Date raiser notified of receipt |
| Assigned To | Text | AI Governance Officer / AI System Owner |
| Date AI System Owner Notified | Date | If applicable |
| Investigation Status | Enum | Open / Under investigation / Escalated to incident / Closed — no action / Closed — action taken |
| Outcome Summary | Text | Summary of investigation outcome and action taken |
| Date Closed | Date | |
| Escalated to Regulatory Authority? | Boolean | Yes / No |
| Follow-up Required? | Boolean | Yes / No |

---

## 3. Competency Requirements by Role

### 3.1 AI Governance Officer

| Competency Area | Minimum Level | Assessment Method |
|----------------|---------------|------------------|
| ISO/IEC 42001:2023 — full standard | Comprehensive knowledge | Formal training + certification (ISO 42001 Lead Implementer or equivalent) |
| EU AI Act — provider/deployer obligations | Working knowledge | Training (internal or external) |
| AI/ML technology fundamentals | Awareness (non-technical) | Completed awareness training |
| Risk management (ISO 31000 or equivalent) | Working knowledge | Experience or training |
| GDPR / data protection | Awareness | Training |
| ISMS governance (ISO 27001) | Working knowledge | Preferred: CISM / CISSP / ISO 27001 Lead Auditor |
| Stakeholder management | Demonstrated | Experience |

### 3.2 AI System Owner

| Competency Area | Minimum Level | Assessment Method |
|----------------|---------------|------------------|
| ISO/IEC 42001:2023 — relevant controls for owned system | Working knowledge | Completed AIMS AI System Owner training |
| AI system functionality (owned system) | Subject matter expert | Demonstrated in role |
| AISIA process | Working knowledge | Completed AI-IMP-A.5.2-5-UG training |
| AI incident response | Awareness | Completed AIMS incident awareness training |
| Data governance basics | Awareness | Completed awareness training |
| EU AI Act — system classification | Awareness | Completed AIMS training |

### 3.3 AI Risk Owner

| Competency Area | Minimum Level | Assessment Method |
|----------------|---------------|------------------|
| ISO/IEC 42001:2023 — risk and impact concepts | Awareness | AIMS management briefing |
| Organisational risk appetite | Expert | Executive experience |
| AI system capabilities and limitations | Awareness | Completed AIMS management briefing |
| AISIA output interpretation | Working knowledge | Completed briefing |

---

## 4. Role Appointment Letter Template

Use this template when formally appointing an AI System Owner or AI Risk Owner:

---

```
[Organisation Letterhead / Internal Communication]

SUBJECT: Appointment as [AI System Owner / AI Risk Owner] — [AI System Name]

To: [Name]
From: AI Governance Officer / [Senior Sponsor]
Date: [YYYY-MM-DD]

Dear [Name],

I am pleased to confirm your appointment as [AI System Owner / AI Risk Owner]
for [AI System Name] within [Organisation]'s AI Management System (AIMS), 
effective [Date].

YOUR ROLE AND RESPONSIBILITIES:

As [AI System Owner / AI Risk Owner], you are responsible for:

[AI System Owner:
- Maintaining the AI System Resource Register entry for [AI System Name]
- Initiating and maintaining the AI System Impact Assessment (AISIA)
- Monitoring system performance and escalating incidents
- Maintaining user documentation and access controls
- Implementing measures identified in the AISIA
- Attending AISIA review cycles per the review schedule]

[AI Risk Owner:
- Commissioning the AISIA for AI systems in your portfolio
- Accepting residual AI risks following AISIA assessment
- Approving deployment of AI systems in your portfolio (with AI Governance Officer)
- Receiving AI incident notifications and management reports]

OBLIGATIONS:

You are required to:
- Complete AI System Owner / AI Risk Owner onboarding training within 30 days
- Read and acknowledge the relevant AIMS policies (AI-POL-A.3.2-3 and related)
- Notify the AI Governance Officer of any issues with the AI system that 
  may require AISIA review or incident response

SUPPORT:

Your primary point of contact for AIMS governance matters is the AI Governance 
Officer: [Name, Email, Extension].

Please acknowledge receipt and acceptance of this appointment by [Date].

[Signature]
AI Governance Officer
```

---

## 5. AIMS Governance Escalation Matrix

The following matrix defines who is notified and who approves decisions at each level of AI governance.

| Situation | First Contact | Escalation 1 | Escalation 2 | Final Authority |
|-----------|--------------|-------------|-------------|----------------|
| AISIA completed — Low-impact | AI System Owner → AI Governance Officer for approval | — | — | AI Governance Officer |
| AISIA completed — Medium-impact | AI System Owner → AI Governance Officer for approval | — | — | AI Governance Officer |
| AISIA completed — High-impact | AI System Owner → Legal/DPO review → AI Governance Officer | Executive Management notification | — | AI Governance Officer (+ Executive notification) |
| Deployment without approved AISIA detected | AI System Owner | AI Governance Officer | CISO | Executive Management |
| AI concern received | AI Governance Officer | AI System Owner (if system-specific) | — | — |
| AI concern escalated to incident | AI Governance Officer | CISO | DPO (if personal data) | Executive Management (if serious) |
| AI concern raised to regulator | Legal | AI Governance Officer | Executive Management | CEO |
| AI System Owner vacancy | AI Governance Officer (interim) | Executive Management | — | — |
| Material misuse detected | AI System Owner | AI Governance Officer | CISO | Executive Management |

---

<!-- QA_VERIFIED: 2026-04-15 -->
