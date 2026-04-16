# Risk Register

<!-- ISMS-CORE:USER-MANUAL:11-risk-register:v1.0:2026-04-16 -->

---

## Overview

The Risk Register implements ISO 27001:2022 Clause 6.1.2 — the information security risk assessment process. It provides a structured way to document, score, treat, and track information security risks scoped to your active project.

Navigate to **Risk & Operations → Risk Register** in the sidebar.

---

## Risk Scenarios

Each entry in the Risk Register is a **risk scenario** — a documented combination of a threat, a vulnerability, and a potential impact to the organisation.

### Creating a Risk Scenario

1. Click **New Risk**
2. Complete the risk form:

| Field | Description |
|-------|-------------|
| **Title** | Short description (e.g. "Ransomware attack on file servers") |
| **Control group** | The ISO 27001 control group this risk is most closely associated with |
| **Threat** | The threat event (e.g. malicious actor, system failure, human error) |
| **Vulnerability** | The weakness being exploited or the gap that enables the threat |
| **Asset** | The information asset(s) at risk |
| **Impact description** | What would happen if this risk materialised |
| **Probability** | Likelihood of occurrence: 1 (Very Low) to 5 (Critical) |
| **Impact** | Consequence if it occurs: 1 (Very Low) to 5 (Critical) |
| **Treatment** | Mitigate / Accept / Transfer / Avoid |
| **Owner** | Responsible person or team |

3. Click **Save**

The risk score is calculated automatically as **Probability × Impact**, mapping to a risk level:

| Score | Risk Level | Colour |
|-------|-----------|--------|
| 1–4 | Low | Green |
| 5–9 | Medium | Amber |
| 10–14 | High | Orange |
| 15–25 | Critical | Red |

---

## The 5×5 Risk Heatmap

Navigate to the **Heatmap** tab to see all risk scenarios plotted on the 5×5 probability × impact matrix. Each cell shows the number of risks that fall at that score combination. Click any cell to see the risks within it.

The heatmap gives you an at-a-glance picture of your overall risk distribution:

- Risks in the top-right corner (high probability, high impact) need immediate attention
- Risks that cluster in the lower-left are well-controlled residual risks
- The goal over time is to see risks migrate from high to low as controls are implemented

---

## Residual Risk

For each risk scenario, you can record both **inherent risk** (before controls) and **residual risk** (after controls are applied). This allows you to demonstrate that your controls are reducing risk to an acceptable level.

Set the **Residual Probability** and **Residual Impact** fields in the risk detail view. The residual risk score and level are shown alongside the inherent score.

---

## Risk Treatment Options

| Treatment | When to use |
|-----------|-------------|
| **Mitigate** | Implement or improve controls to reduce probability or impact |
| **Accept** | Risk is within tolerance — document the rationale and review date |
| **Transfer** | Transfer risk to a third party (insurance, outsourcing) |
| **Avoid** | Eliminate the activity or asset that introduces the risk |

For Mitigate treatment: link to specific gap records or action plans that are addressing the risk.

For Accept treatment: record the formal acceptance rationale, approver, and a review date.

---

## Risk Acceptance

When treatment is **Accept**, a formal risk acceptance workflow is triggered:

1. Provide the acceptance rationale
2. Select the approval owner (must have ISMS Manager or Admin role)
3. Set a review date (when this acceptance decision should be reconsidered)
4. Submit for sign-off

The approver receives a notification and can sign off or reject the acceptance. Signed-off risk acceptances are recorded with timestamp, approver identity, and rationale — fully auditable.

---

## Linking Risks to Gaps and EBIOS RM

**Gaps → Risks:** Gaps can be escalated to the Risk Register from the Gap Management view. The resulting risk is linked to the originating gap for full traceability.

**EBIOS RM → Risks:** Strategic scenarios from EBIOS RM workshops can be linked to Risk Register entries. See [EBIOS RM](14-ebios-rm.md).

---

## Risk Register Reporting

From the Risk Register:

- **Filter** by level (Low / Medium / High / Critical), treatment, owner, control group
- **Sort** by score, date created, review date
- **Export** as CSV or XLSX

The export includes all risk fields, treatment details, acceptance records, and linkages — suitable for management review and audit evidence under ISO 27001:2022 Clause 6.1.2.

---

## Risk Metrics

Two KPI Dashboard metrics are derived from the Risk Register:

- **`risk_score_avg`** — average risk score across all open risks in the active project
- **`risk_critical_count`** — count of risks at Critical level (score 15–25)

See [KPI Dashboard](19-kpi-dashboard.md) for detail.

<!-- QA_VERIFIED: 2026-04-16 -->
