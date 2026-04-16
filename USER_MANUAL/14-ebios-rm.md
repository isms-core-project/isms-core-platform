# EBIOS RM

<!-- ISMS-CORE:USER-MANUAL:14-ebios-rm:v1.0:2026-04-16 -->

---

## What Is EBIOS RM?

EBIOS RM (Expression of Needs and Identification of Security Objectives — Risk Manager) is the French national risk analysis methodology published by ANSSI (Agence nationale de la sécurité des systèmes d'information). It is widely required in French public sector organisations and increasingly used across Europe as an alternative or complement to ISO 27001 risk assessment.

EBIOS RM structures risk analysis into five workshops that progressively build a picture of your risk landscape — from the assets you want to protect to the attack paths that could compromise them.

Navigate to **Risk & Operations → EBIOS RM** in the sidebar.

---

## The Five Workshops

### Workshop 1 — Scope and Security Baseline

Define what you are protecting and establish your security baseline.

**What you record:**
- The perimeter of the study (the systems, processes, and information in scope)
- Feared events — the high-level security events that could harm the organisation (e.g. "confidentiality breach of customer data")
- The security baseline — your current security measures mapped to the ISMS CORE control library

For each feared event, set:
- **Gravity** — the severity of the feared event: 1 (Very Low) to 4 (Critical)
- **Likelihood** — estimated frequency of occurrence

### Workshop 2 — Risk Sources

Identify who might attack you and what they want.

**What you record:**
- Risk sources — potential threat actors (cybercriminal, insider, state actor, competitor, opportunist)
- Target objectives — what each risk source is trying to achieve (financial gain, espionage, disruption, reputational damage)
- Risk source characterisation — motivation, capability, resources

For each risk source, rate their **pertinence** (relevance to your specific context) to focus your analysis on realistic threats.

### Workshop 3 — Strategic Scenarios

Map risk sources to feared events via strategic scenarios.

**What you record:**
- Strategic scenarios — which risk source could cause which feared event, and through what high-level attack approach
- Likelihood assessment for each strategic scenario
- The **likelihood × gravity matrix** — a 4×4 risk matrix showing which scenarios require priority treatment

The strategic scenario matrix is shown as a colour-coded grid on the Workshop 3 view — scenarios in the top-right quadrant (high likelihood, high gravity) are your priority risks.

### Workshop 4 — Operational Scenarios

Decompose strategic scenarios into concrete attack paths.

**What you record:**
- Attack paths — the step-by-step technical sequence by which a strategic scenario could be executed
- MITRE ATT&CK technique mapping — each attack step can be linked to a specific MITRE ATT&CK technique, providing the technical depth required for NIS2 and ANSSI reporting
- Existing security measures that block or detect each step
- Residual likelihood for each attack path given current measures

The MITRE ATT&CK integration here is direct: when you add a step to an attack path, you can search and select the specific technique from the full ATT&CK v18 library (14 tactics, 700+ techniques and sub-techniques).

### Workshop 5 — Risk Treatment

Define security measures to address your operational scenarios.

**What you record:**
- Security measures — the controls you will implement or improve to address residual risks
- Mapping to ISO 27001 controls — each security measure is mapped to the relevant Annex A control group(s)
- Risk treatment decision — Mitigate / Accept / Transfer / Avoid
- Residual risk after measures

Security measures from Workshop 5 can be linked to the Risk Register and Gap Management to create trackable work items.

---

## MITRE ATT&CK Integration in Attack Paths

When building Workshop 4 attack paths, each step links to the MITRE ATT&CK technique library. This integration:

- Ensures your attack scenarios are grounded in documented adversary behaviours
- Provides technique IDs (e.g. T1190, T1078) that satisfy ANSSI reporting requirements
- Connects your EBIOS RM attack paths to the Threat Intelligence section — you can see which techniques are in your attack paths and which adversary groups use them

---

## Linking EBIOS RM to Other Platform Modules

| EBIOS RM element | Links to |
|-----------------|---------|
| Feared events | Risk Register (escalate to formal risk scenarios) |
| Security measures (Workshop 5) | Gap Management (create gaps for unimplemented measures) |
| Attack path techniques | MITRE ATT&CK Heatmap (visualise coverage) |
| Risk treatment decisions | Risk Register (as treatment records) |

---

## Exporting EBIOS RM Results

The EBIOS RM section provides an export that covers all five workshops in a structured format suitable for ANSSI review or management reporting. Export as PDF from the EBIOS RM summary view.

<!-- QA_VERIFIED: 2026-04-16 -->
