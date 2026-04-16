# KPI Dashboard

<!-- ISMS-CORE:USER-MANUAL:19-kpi-dashboard:v1.0:2026-04-16 -->

---

## Overview

The KPI Dashboard tracks nine named metrics that collectively represent the health of your ISMS programme. It is the primary tool for CISO-level reporting and management review under ISO 27001:2022 Clause 9.1 (Monitoring, measurement, analysis, and evaluation).

Navigate to **Analytics → KPI Dashboard** in the sidebar.

---

## The Audit Readiness Score

The **Audit Readiness Score** is the hero metric at the top of the KPI Dashboard. It is a composite score (0–100) derived from all nine KPI metrics, weighted to reflect overall programme health.

A score above 80 indicates strong audit readiness. Below 60 indicates significant work required before an audit.

The score updates automatically as your underlying metrics change — there is no manual input required.

---

## The Nine KPI Metrics

### 1. Compliance Score (`compliance_score`)

The average compliance score across all assessed control groups in the active project. Calculated from assessment checklist data.

**Target:** ≥ 80%

### 2. Policy Coverage (`policy_coverage`)

The percentage of expected control groups that have at least one approved or published policy document in the active project.

**Target:** 100%

### 3. Average Risk Score (`risk_score_avg`)

The average inherent risk score (probability × impact) across all open risk scenarios in the active project.

**Target:** As low as reasonable — no single absolute threshold, but declining trend indicates effective risk treatment.

### 4. Critical Risk Count (`risk_critical_count`)

The number of open risk scenarios with a score of 15–25 (Critical).

**Target:** 0 open critical risks, or all with documented risk acceptance.

### 5. Evidence Freshness (`evidence_freshness`)

The percentage of evidence items in the active project that are verified and not expired.

**Target:** ≥ 90%

### 6. Open Gap Count (`gap_open_count`)

The total number of open gaps (status: Open or In Progress) in the active project.

**Target:** Declining trend — absolute number depends on programme maturity.

### 7. Gap Closure Rate (`gap_closure_rate`)

The percentage of gaps created in the last 90 days that have been closed or resolved.

**Target:** ≥ 70%

### 8. Overdue Remediation Items (`remediation_overdue`)

The number of gap action plan items that are past their target ETA and not yet complete.

**Target:** 0 overdue items.

### 9. Audit Readiness Score (`audit_readiness`)

The composite metric (described above). Shown separately on the dashboard card and as a trend line.

---

## Sparkline Trends

Each metric card shows a **sparkline** — a small inline chart showing the metric's movement over the last 30 days. This lets you see at a glance whether a metric is improving, stable, or degrading.

KPI snapshots are taken daily at 06:00 UTC by the Celery Beat scheduler. If the platform was not running on a particular day, that day's snapshot is missing from the sparkline — this is normal.

---

## Metrics Portfolio (Super Admin)

If you have the Super Admin role, navigate to **Analytics → Metrics Portfolio** for a cross-organisation view of all nine KPIs across every organisation in the platform.

This is the board-level CISO view for organisations running multiple entities — group companies, subsidiaries, or separate organisational scopes — on a single platform instance.

---

## Using KPI Data for Management Review

The KPI Dashboard is designed to support ISO 27001:2022 Clause 9.3 (Management review). The recommended cadence:

- **Monthly:** Review Audit Readiness Score trend, gap closure rate, and overdue remediations
- **Quarterly:** Full nine-metric review, compare against targets, update risk treatment plan
- **Annual:** Baseline reset for the new audit cycle

Export the KPI summary from the dashboard for inclusion in your management review pack:

1. Click **Export** on the KPI Dashboard
2. Select the date range
3. Download as XLSX (nine metrics, daily values, trend data) or PDF (formatted report)

<!-- QA_VERIFIED: 2026-04-16 -->
