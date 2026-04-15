<!-- ISMS-CORE:IMP:AI-IMP-A.9.2-4-TG:ai:TG:a.9.2-4 -->
**AI-IMP-A.9.2-4-TG — Responsible Use of AI Systems — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Responsible Use of AI Systems — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.9.2-4-TG |
| **Related Policy** | AI-POL-A.9.2-4 (Responsible Use of AI Systems) |
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

- AI-POL-A.9.2-4 (Responsible Use of AI Systems — governing policy)
- AI-IMP-A.9.2-4-UG (Responsible Use of AI Systems — User Guide)

---

## Purpose of This Guide

This guide provides the **schemas, templates, and reference structures** for responsible AI use — including the intended use specification schema, the AI System Responsible Use Record template, the Pre-Use Verification Record schema, and the misuse event register schema.

**Audience**: AI System Owners, AI Governance Officer, compliance.

---

## 1. Intended Use Specification Schema (A.9.4)

One intended use specification per AI system. Maintained by AI System Owner; reviewed by AI Governance Officer when the system changes.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| AI System ID | Text | M | Reference to Resource Register |
| AI System Name | Text | M | |
| Specification Version | Text | M | Version of this intended use specification |
| Date | Date | M | |
| **Intended Use Statement** | Text | M | Clear, specific description: what for, by whom, in what context, to what end |
| **Intended User Categories** | Text | M | Who is authorised to use the system; any competency or qualification requirements |
| **Intended Operational Context** | Text | M | Environments, conditions, and populations for which the system was designed |
| **Conditions for Valid Use** | Text | M | Prerequisites for outputs to be reliable (input data requirements, operator actions, etc.) |
| **Out-of-Scope Uses** | Text | M | Uses not designed or validated for — authorisation required before proceeding |
| **Prohibited Uses** | Text | M | Uses explicitly forbidden; uses that could cause harm, violate rights, or breach law |
| **Material Change Triggers** | Text | M | What changes to the system or context require a specification update |
| Approved By | Text | M | AI Governance Officer name and date |
| Version History | Text | R | Track updates |

---

## 2. AI System Responsible Use Record Template (A.9.3)

One record per AI system documenting responsible use objectives. Maintained by AI System Owner.

---

```
AI SYSTEM RESPONSIBLE USE RECORD
System: [AI System Name] | Version: [X.X] | Date: [YYYY-MM-DD]
Document ID: RUR-[System-ID]-v[X.X]
AI System Owner: [Name]
Approved By: [AI Governance Officer] | Date: [YYYY-MM-DD]

1. RESPONSIBLE USE OBJECTIVES FOR THIS SYSTEM

For each of the six responsible use properties, document the specific 
objective as it applies to this AI system, how it is operationalised, and 
how it is monitored.

PROPERTY 1: USE WITHIN INTENDED PURPOSE
Objective: [Specific statement for this system]
How operationalised: [Specific measures in place for this system]
Monitoring approach: [How compliance with the objective is monitored]
Responsible party: [Role]

PROPERTY 2: PRESERVATION OF HUMAN AGENCY
Objective: [Specific human oversight objective for this system]
Human review mechanism: [Description of how human review works]
Override mechanism: [How users can and must override AI outputs when required]
Monitoring approach: [How oversight compliance is monitored]
Responsible party: [Role]

PROPERTY 3: FAIRNESS AND NON-DISCRIMINATION
Objective: [Specific fairness objective for this system]
Affected demographic groups: [Which groups are monitored]
Monitoring approach: [How output distributions are monitored for disparities]
Reporting threshold: [What triggers escalation]
Responsible party: [Role]

PROPERTY 4: PRIVACY COMPLIANCE IN USE
Objective: [Specific privacy objective for this system]
Personal data scope: [What personal data is processed; for what purpose]
Prohibited personal data inputs: [What personal data must not be fed into this system]
Monitoring approach: [How privacy compliance is monitored]
Responsible party: DPO / AI System Owner

PROPERTY 5: AVOIDANCE OF HARMFUL USE
Objective: [Specific harm avoidance objective for this system]
Known harmful use risks: [What harmful uses are possible and must be prevented]
Control measures: [What prevents harmful use]
Monitoring approach: [How use patterns are monitored for harm indicators]
Responsible party: [Role]

PROPERTY 6: TRANSPARENCY TO AFFECTED PARTIES
Objective: [Specific transparency objective for this system]
Transparency measures in place: [User documentation / notices / disclosures]
Completeness assessment: [Are all affected parties appropriately informed?]
Monitoring approach: [How transparency compliance is verified]
Responsible party: [Role]

2. PRE-USE VERIFICATION STATUS
Date of last pre-use verification: [YYYY-MM-DD]
Verification outcome: [Pass / Pass with conditions / Fail]
Open items: [Any conditions or outstanding actions]

3. TRAINING STATUS
[Summary of training completion by user category and date]

4. REVIEW LOG
| Date | Reviewed By | Changes | Next Review |
|------|-------------|---------|-------------|
| | | | |
```

---

## 3. Pre-Use Verification Record Schema (A.9.2)

One record per AI system per initial deployment (and per material expansion of user scope).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Record ID | Text | M | e.g., PUV-AI-SYS-001-v1.0 |
| AI System ID | Text | M | |
| AI System Version | Text | M | |
| Verification Date | Date | M | |
| Conducted By | Text | M | AI System Owner |
| **Verification Items** | | | |
| Current AISIA — Document ID | Text | M | |
| Current AISIA — Approval Date | Date | M | |
| Current AISIA — Status | Enum | M | Approved / Needs update |
| Operational context within AISIA scope? | Boolean | M | Confirmation that this use is within the assessed scope |
| User Training — All required users trained? | Boolean | M | |
| User Training — Completion evidence reference | Text | M | |
| Human oversight mechanism — Configured? | Boolean | M | |
| Human oversight mechanism — Tested? | Boolean | C | Required for Medium/High impact |
| Human oversight mechanism — Description | Text | M | Brief description of mechanism |
| Logging — Active? | Boolean | M | |
| Logging — Technical confirmation reference | Text | M | |
| User documentation — Available? | Boolean | M | |
| User documentation — Location/link | Text | M | |
| Access controls — Configured? | Boolean | M | |
| Access controls — Reviewed? | Boolean | M | |
| **Overall Verification Outcome** | Enum | M | Approved for use / Conditional / Not approved |
| Conditions (if conditional) | Text | C | |
| AI System Owner Sign-off | Text | M | Name and date |

---

## 4. Misuse Event Register Schema (A.9.2 — Misuse Detection and Response)

| Field | Type | Description |
|-------|------|-------------|
| Event ID | Text | Unique reference (e.g., MISUSE-2026-001) |
| Date Detected | Date | |
| Detection Method | Enum | User report / Log review / Automated alert / Management observation / Other |
| AI System | Text | Which system |
| Description | Text | Description of the misuse event |
| Actor (if known) | Text | Anonymised or "systemic" if pattern |
| Prohibited Use Category | Text | Which prohibited or out-of-scope use was violated |
| Potential Harm | Text | Assessment of whether harm to individuals occurred or could have occurred |
| Harm to Individuals? | Boolean | |
| Incident Process Triggered? | Boolean | If harm: AI incident process initiated |
| AI Governance Officer Notified | Date | |
| Response Applied | Text | Guidance / Retraining / Access restriction / System suspension / Other |
| Root Cause | Text | Why did misuse occur? |
| Preventive Measure | Text | What was done to prevent recurrence |
| Date Closed | Date | |
| Outcome | Text | Summary |

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
