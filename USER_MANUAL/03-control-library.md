# Control Library

<!-- ISMS-CORE:USER-MANUAL:03-control-library:v1.0:2026-04-16 -->

---

## Overview

The **Control Library** is the authoritative list of all control groups in the platform. It is the starting point for understanding your compliance posture — every policy, assessment, gap, and piece of evidence traces back to a control group.

Navigate to **ISMS → Control Library** in the sidebar.

---

## Control Groups

Each row in the Control Library represents one control group — a cluster of related ISO controls addressed by a common set of documentation and evidence.

The platform contains 99 control groups across the five product families:

| Product | Count | Scope |
|---------|-------|-------|
| ISMS Framework | 54 | ISO 27001:2022 Annex A (A.5–A.8) |
| Privacy | 21 | ISO 27701:2025 (controller, processor, shared) |
| Cloud | 12 | ISO 27018:2025 |
| AI | 10 | ISO 42001:2023 Annex A |
| Foundation | 2 | Foundation policies (INS-POL-00/01) |

Use the **product switcher** to filter the library to a specific product, or view all control groups together.

---

## Reading the Control Library

Each control group card or row shows:

- **Control ID** — e.g. `A.8.24`, `PRIV-A.1.2`, `AI-A.5`
- **Title** — the control group name
- **Section** — the ISO Annex section (e.g. A.8 Technological Controls)
- **Compliance score** — percentage of checklist items marked compliant
- **Policy status** — whether a policy document is imported and in what state
- **Assessment status** — whether the assessment workbook has been completed
- **Evidence status** — count of evidence items attached and their freshness
- **Open gaps** — count of unresolved gaps linked to this control

### Compliance Score Colours

| Colour | Range | Meaning |
|--------|-------|---------|
| Green | 80–100% | On track |
| Amber | 50–79% | Needs attention |
| Red | 0–49% | Significant gaps |
| Grey | — | Not yet assessed |

---

## Drilling Into a Control Group

Click any control group to open its detail view. The detail view has several tabs:

### Overview Tab

Summary of the control group — ISO reference, clause text, applicable controls, and links to documentation.

### Policy Tab

Shows all policy documents linked to this control group (POL, OP-POL, REF, CTX, FORM). Click any document to preview it in the document viewer.

If a control group has no policy yet, this tab will show a placeholder. Policies are imported by the administrator — contact them if expected documents are missing.

### Implementations Tab

Shows all implementation guides (IMP-UG user-facing, IMP-TG technical) for this control group. These are indexed into OpenSearch and available for full-text search.

### Assessments Tab

Shows the compliance checklist for this control group — the individual items from the assessment workbook, each with a compliance status:

| Status | Meaning |
|--------|---------|
| Compliant | Control is implemented and evidenced |
| Partial | Control is partially implemented |
| Non-compliant | Control is not implemented |
| Not applicable | Control is formally scoped out |
| Not assessed | Not yet evaluated |

Click any item to update its status, add a comment, or link evidence.

### Evidence Tab

Shows all evidence items — both manual uploads and automated connector evidence — linked to this control group. See [Evidence Management](09-evidence-management.md) for detail.

### Automated Evidence Tab

Shows the most recent automated evidence from connectors for this control group. Each item shows the source connector, timestamp, classification, and a summary of what was collected. Use the **Promote** button to move a connector evidence item into your formal evidence tracker.

### Gaps Tab

Lists all open gaps linked to this control group. See [Gap Management](08-gap-management.md).

### BIA Tab

Available on continuity-related control groups (A.5.29, A.5.30). Shows linked Business Impact Analysis records. See [Business Impact Analysis](12-bia.md).

---

## Coverage Heatmap

Navigate to **ISMS → Coverage** for a visual heatmap of policy and assessment coverage across all control groups.

The heatmap shows two dimensions:

- **Policy coverage** — is a policy document present for this control group?
- **Assessment coverage** — is there a completed assessment checklist?

Cells are coloured by coverage percentage. Use the heatmap to identify which control groups need immediate attention.

---

## Control Dependency Graph

Navigate to **ISMS → Graph** to see the control dependency visualisation. This shows 229 documented relationships between ISO 27001:2022 controls — which controls support others, which are prerequisites, and which are commonly co-implemented.

Use the graph to understand implementation sequencing when building your ISMS from scratch, or to identify blast-radius when a control group falls behind.

---

## Searching Controls

Use the search bar at the top of the Control Library to filter by:

- Control ID (e.g. `A.8.8`, `AI-A.3`)
- Title keyword
- Section

Full-text search across policy and implementation document content is available via **ISMS → Policies** (see [Policies & Documents](05-policies-documents.md)).

<!-- QA_VERIFIED: 2026-04-16 -->
