# Gap Management

<!-- ISMS-CORE:USER-MANUAL:08-gap-management:v1.0:2026-04-16 -->

---

## What Is a Gap?

A gap is a documented deficiency — a control that is not implemented, partially implemented, or where evidence is missing. Gaps are the primary action items of your ISMS: they represent work that needs to be done before your controls are fully effective.

Gaps in ISMS CORE are scoped to your active project. Navigate to **Risk & Operations → Gaps** in the sidebar.

---

## Creating a Gap

Gaps can be created in two ways:

### From a Checklist Item

When assessing a control and marking an item as Non-compliant or Partial, click **Create Gap** directly from the checklist item. The gap is pre-populated with the control ID, item reference, and your comment.

### Manually

1. Navigate to **Risk & Operations → Gaps**
2. Click **New Gap**
3. Fill in the gap form:

| Field | Description |
|-------|-------------|
| **Title** | Short description of the gap (e.g. "MFA not enabled on admin accounts") |
| **Control group** | Which ISO control group this gap belongs to |
| **Severity** | Critical / High / Medium / Low |
| **Owner** | The user or team responsible for remediation |
| **Due date** | Target remediation date (SLA) |
| **Description** | Full gap description and context |
| **Source** | How the gap was identified (internal audit, penetration test, assessment, connector, etc.) |

---

## Gap Lifecycle

Each gap moves through a defined lifecycle:

```
Open → In Progress → Resolved → Closed
              ↓
         Risk Accepted (if not remediating)
```

| State | Meaning |
|-------|---------|
| **Open** | Gap identified, not yet being worked on |
| **In Progress** | Remediation action under way |
| **Resolved** | Remediation complete — awaiting verification |
| **Closed** | Verified and closed — evidence confirmed |
| **Risk Accepted** | Organisation has formally accepted this gap as a residual risk |

Update the state as work progresses. Only ISMS Manager and Admin roles can close or risk-accept a gap.

---

## BSI 200-3 Risk Calculator

For each gap, the platform includes an automatic risk calculator based on the BSI 200-3 risk model. When you select the control group and set the severity, the calculator pre-populates:

- **Threat code** — the relevant BSI threat category for this ISO control section
- **Likelihood** — pre-mapped from the control type and threat category
- **Impact** — pre-mapped from the severity you selected
- **Risk level** — likelihood × impact, shown as Low / Medium / High / Very High

You can override the pre-mapped values if your assessment differs.

---

## Remediation Tracking

For gaps that are being remediated, add an **Action Plan** from the gap detail view:

| Field | Description |
|-------|-------------|
| **Action** | What needs to be done |
| **Owner** | Who is responsible for this specific action |
| **ETA** | Target completion date |
| **Effort** | Estimated effort (days or story points) |
| **Cost** | Estimated cost (optional) |
| **Progress** | Percentage complete (0–100) |

Multiple action items can be added to a single gap to represent a phased remediation approach.

### ITSM Integration

If your organisation uses Jira or ServiceNow, action plan items can be pushed as tickets directly from the gap detail view. Click **Push to Jira** or **Push to ServiceNow** to create a ticket. The push is idempotent — clicking again updates the existing ticket rather than creating a duplicate.

Ticket status (open, in progress, done) syncs back to the platform automatically on a scheduled basis.

---

## SLA Monitoring

Gaps with a due date are monitored for SLA compliance. The gap list shows:

- **On track** — due date is in the future
- **Due soon** — due within 7 days
- **Overdue** — past due date without being resolved or closed

The KPI Dashboard metric `gap_closure_rate` and `remediation_overdue` are derived from your gap SLA data.

---

## Risk Acceptance

If your organisation decides not to remediate a gap (accepting the residual risk), change the gap state to **Risk Accepted** and document:

- The business justification
- Who approved the risk acceptance (sign-off owner)
- The review date (when this acceptance should be reconsidered)

Risk-accepted gaps are excluded from overdue SLA calculations but remain visible in the gap list and in audit exports.

---

## Gap Reporting

From the Gaps list:

- **Filter** by severity, state, owner, control group, or date range
- **Export** as CSV or XLSX
- **Group by** control group or owner for a summary view

The export includes all gap fields, action plan items, and current state — suitable for management reporting or audit evidence.

---

## Gaps and the Risk Register

Significant gaps can be escalated to the Risk Register as formal risk scenarios. From the gap detail view, click **Escalate to Risk Register** to create a linked risk scenario. The gap remains open and is linked to the risk record for full traceability.

See [Risk Register](11-risk-register.md) for how risk scenarios are managed.

<!-- QA_VERIFIED: 2026-04-16 -->
