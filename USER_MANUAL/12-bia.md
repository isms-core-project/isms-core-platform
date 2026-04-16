# Business Impact Analysis

<!-- ISMS-CORE:USER-MANUAL:12-bia:v1.0:2026-04-16 -->

---

## Overview

The **Business Impact Analysis (BIA)** module supports ISO 27001:2022 controls A.5.29 (Information security during disruption) and A.5.30 (ICT readiness for business continuity). It provides a structured way to assess the impact of disruption on business activities and establish recovery time objectives.

Navigate to **Risk & Operations → BIA** in the sidebar, or access it via the BIA tab on control groups A.5.29 and A.5.30 in the Control Library.

---

## BIA Concepts

### Business Activity

The unit of BIA is a **business activity** — a process, service, or function that the organisation performs. Examples:

- Customer order processing
- Payroll processing
- Financial reporting
- Incident response

Each business activity depends on assets (systems, data, staff) and has a maximum tolerable disruption period.

### Key Recovery Time Metrics

| Metric | Definition |
|--------|-----------|
| **RTO** (Recovery Time Objective) | Maximum acceptable time to restore a business activity after disruption |
| **RPO** (Recovery Point Objective) | Maximum acceptable data loss expressed as time (e.g. "no more than 4 hours of data") |
| **MTPD** (Maximum Tolerable Period of Disruption) | Absolute maximum time the activity can be unavailable before causing irreversible harm |

The relationship: **RTO ≤ MTPD** always. If your RTO exceeds MTPD, your recovery capability is insufficient and a gap should be raised.

---

## Creating a BIA Record

1. Navigate to **Risk & Operations → BIA**
2. Click **New Business Activity**
3. Complete the record:

| Field | Description |
|-------|-------------|
| **Activity name** | Name of the business process or service |
| **Owner** | Process owner or team responsible |
| **Description** | What the activity does and why it matters |
| **Dependencies** | Key systems, data stores, or staff required |
| **RTO (hours)** | Recovery time objective |
| **RPO (hours)** | Recovery point objective |
| **MTPD (hours)** | Maximum tolerable disruption period |
| **Financial impact** | Estimated financial loss per hour of disruption (optional) |
| **Operational impact** | Operational consequences score: 1 (Minor) to 5 (Catastrophic) |
| **Reputational impact** | Reputational consequences score: 1 (Minor) to 5 (Catastrophic) |
| **Regulatory impact** | Regulatory consequences score: 1 (Minor) to 5 (Catastrophic) |
| **Recovery strategy** | How the activity is recovered (failover, manual workaround, etc.) |

4. Click **Save**

---

## Impact Scoring

The platform calculates an overall **impact score** from the four impact dimensions (financial, operational, reputational, regulatory). Activities with higher impact scores represent higher business continuity priority — they should have tighter RTOs and more robust recovery arrangements.

Impact scores are shown on the BIA list view and can be used to prioritise which activities get tested first.

---

## Recovery Testing

For each business activity, record recovery test results:

1. Open the BIA record and navigate to the **Recovery Tests** tab
2. Click **New Test**
3. Record:
   - Test date
   - Test type (tabletop exercise / partial failover / full failover)
   - Actual RTO achieved
   - Actual RPO achieved
   - Result (Pass / Fail / Partial)
   - Findings and actions

Comparing actual RTO/RPO against objectives over time demonstrates that your business continuity controls are effective — important evidence for A.5.29 and A.5.30 audits.

---

## BIA and the Control Library

The BIA tab is embedded in the control group detail views for A.5.29 and A.5.30. From the control group view, you can see all BIA records linked to that control and add new ones without navigating away.

---

## BIA Export

Export the BIA register from the BIA list view as:

- **CSV** — all records with all fields, suitable for spreadsheet analysis
- **XLSX** — formatted spreadsheet with impact scoring and recovery test history

<!-- QA_VERIFIED: 2026-04-16 -->
