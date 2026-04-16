# Compliance Assessments

<!-- ISMS-CORE:USER-MANUAL:06-compliance-assessments:v1.0:2026-04-16 -->

---

## Overview

The **Compliance Assessments** section contains per-product checklists — the control-by-control self-assessment for your ISMS. These are distinct from the 23 framework assessment modules (NIS2, DORA, NIST CSF 2.0, etc.) covered in the next chapter.

Navigate to **Compliance → Assessments** in the sidebar.

---

## Product Assessment Checklists

Each product family has its own set of assessment checklists derived from the control documentation:

| Product | Checklists | Scope |
|---------|-----------|-------|
| **ISMS Framework** | 188 workbooks | One per generator — detailed technical and process checks per control group |
| **ISMS Operational** | 53 checklists | Lightweight checklist per Annex A group |
| **Privacy** | 21 checklists | One per ISO 27701:2025 control group |
| **Cloud** | 12 checklists | One per ISO 27018:2025 control group |
| **AI** | 10 checklists | One per ISO 42001:2023 control group |

Use the product switcher to navigate between assessment sets.

---

## Opening an Assessment

Click any checklist in the assessment list to open it. The checklist shows all items derived from the control's SCR (Self-Assessment Scorecard) generator.

Each item has:

- **Item ID** — unique reference (e.g. `A.8.24-GS-CS-001`)
- **Control statement** — what is being assessed
- **Status selector** — Compliant / Partial / Non-compliant / Not applicable / Not assessed
- **Comment field** — your assessment rationale or evidence pointer
- **Evidence links** — attach specific evidence items to this checklist item

---

## Scoring and Status

### Per-Item Status

| Status | Score weight | When to use |
|--------|-------------|-------------|
| **Compliant** | Full | Control is implemented, documented, and evidenced |
| **Partial** | Half | Control is partly implemented or evidence is incomplete |
| **Non-compliant** | Zero | Control is not implemented |
| **Not applicable** | Excluded | Control is formally scoped out (document the reason in the comment) |
| **Not assessed** | Neutral | Not yet evaluated — does not drag down the score but shows as incomplete |

### Checklist Score

The checklist score is the percentage of assessed items (excluding "Not applicable" and "Not assessed") that are Compliant or Partial, weighted by their status. It is shown on the checklist card in the assessment list and in the Control Library.

### Aggregated Compliance Score

The Overview page for each product shows an aggregated compliance score across all control groups — the average of all individual checklist scores for assessed groups. This is your ISO 27001 (or extension standard) coverage indicator.

---

## Assessment Collections

Group multiple assessments into a named collection for reporting. Use collections to represent:

- An audit cycle (e.g. "Stage 2 Audit Preparation Q2 2026")
- A management review package
- A specific scope boundary (e.g. only cloud controls)

### Creating a Collection

1. Navigate to **Compliance → Assessment Collections**
2. Click **New Collection**
3. Give it a name and description
4. Add assessments to the collection from the checklist library

### Collection Reporting

A collection shows:

- Completion percentage (% of items with a status set)
- Compliance percentage (% of assessed items that are Compliant or Partial)
- Status rollup by product family
- Export options: CSV (raw item data), colour-coded XLSX (one row per item with traffic-light formatting), PDF (A4, suitable for management review)

---

## Framework Workbooks (ISMS Framework)

The ISMS Framework product includes 188 assessment workbooks — one per generator, derived from the Excel workbooks produced by the ISMS CORE control engineering process. Each workbook corresponds to a specific technical or process topic within a control group and contains:

- Summary dashboard with scoring
- Domain-specific assessment items (General Security, Implementation, Formula-based scoring)
- Maturity level indicators

These are the most granular assessment artefacts in the platform. Use them for technical deep-dives and when preparing for stage 2 audits.

---

## Exporting Assessment Results

From any assessment list or collection:

- **CSV** — all items with status, comments, and evidence counts
- **XLSX** — colour-coded spreadsheet (green/amber/red per status)
- **PDF** — formatted A4 report suitable for audit evidence or management reporting

All exports include the assessment name, date, and assessor information for audit traceability.

<!-- QA_VERIFIED: 2026-04-16 -->
