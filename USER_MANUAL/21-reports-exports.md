# Reports & Exports

<!-- ISMS-CORE:USER-MANUAL:21-reports-exports:v1.0:2026-04-16 -->

---

## Overview

ISMS CORE Platform provides export and reporting capabilities throughout the application. This chapter is a reference guide to what can be exported from each section and in what format.

---

## Export Formats

| Format | Description | Best for |
|--------|-------------|---------|
| **CSV** | Comma-separated values — all fields, raw data | Data analysis, importing into other tools |
| **XLSX** | Colour-coded Excel spreadsheet | Management review, visual reporting, auditor evidence |
| **PDF** | Formatted A4 report | Formal reports, audit submission, printing |

---

## Exports by Section

### Compliance Assessments

| What | Format | Where |
|------|--------|-------|
| Checklist results (single assessment) | CSV, XLSX | Assessment detail view → Export |
| Assessment collection results | CSV, colour XLSX, PDF (A4) | Assessment Collections → Export |
| NIST CSF 2.0 scores | XLSX (NIST template format), CSV | NIST CSF 2.0 page → Export |

### Gap Management

| What | Format | Where |
|------|--------|-------|
| Gap register | CSV, XLSX | Gaps list → Export |
| Gap detail with action plan | CSV | Gap detail view → Export |

### Evidence Tracker

| What | Format | Where |
|------|--------|-------|
| Evidence register | CSV, XLSX | Evidence Tracker → Export |

### Risk Register

| What | Format | Where |
|------|--------|-------|
| Risk register | CSV, XLSX | Risk Register → Export |
| Risk heatmap | PNG image | Heatmap tab → Download image |

### TPRM

| What | Format | Where |
|------|--------|-------|
| Vendor register | CSV, XLSX | TPRM list → Export |
| DORA ICT register | XLSX | TPRM → DORA Register → Export |

### EBIOS RM

| What | Format | Where |
|------|--------|-------|
| Full EBIOS RM study (all 5 workshops) | PDF (A4) | EBIOS RM summary view → Export PDF |

### BIA

| What | Format | Where |
|------|--------|-------|
| BIA register | CSV, XLSX | BIA list → Export |

### KPI Dashboard

| What | Format | Where |
|------|--------|-------|
| KPI trends (selected date range) | XLSX, PDF | KPI Dashboard → Export |

### Threat Intelligence

| What | Format | Where |
|------|--------|-------|
| KEV Audit Report (A.8.8 evidence) | CSV | Intelligence → KEV Audit → Export |
| CVE search results | CSV | CVE Explorer → Export results |

### System Event Log

| What | Format | Where |
|------|--------|-------|
| Full event log (date range) | CSV | Admin → System → Event Log → Export |

### Cross-Framework Mapping

| What | Format | Where |
|------|--------|-------|
| Crosswalk mapping table | CSV | Crosswalk Viewer → Export |
| Inferred coverage report | CSV, PDF | Inferred Coverage tab → Export |

---

## Audit Evidence Pack — Recommended Exports

When preparing for an ISO 27001 Stage 2 or surveillance audit, the following exports provide a comprehensive evidence pack:

| Document | Export | Section |
|----------|--------|---------|
| Assessment checklist results | Colour XLSX | Compliance Assessments |
| Assessment collection summary | PDF | Assessment Collections |
| Gap register (closed + open) | XLSX | Gap Management |
| Risk register | XLSX | Risk Register |
| Evidence register | XLSX | Evidence Tracker |
| KEV audit report | CSV | Threat Intelligence |
| QA Engine results | Screenshot / on-screen | QA Engine |
| NIST CSF 2.0 profile | XLSX | NIST CSF 2.0 |
| KPI trend report | PDF | KPI Dashboard |
| Event log (audit period) | CSV | Admin → System |

---

## PDF Generation Notes

PDF exports use A4 format. They are generated server-side and formatted for printing — they do not require the browser's print function.

For EBIOS RM and Assessment Collection PDFs, the platform uses a structured template that includes:
- Cover page (document title, organisation name, date)
- Table of contents
- Section content
- Appendix with raw data

Large collections (>100 items) may take 15–30 seconds to generate.

---

## Pandoc Export (Advanced)

The policy and implementation documents in your project are stored as Markdown and can be exported for Pandoc processing if you need a custom PDF format. Download the raw Markdown from the document detail view (Source mode → Copy / Download).

To generate a formatted PDF with Pandoc:
```bash
pandoc policy.md \
  -o Policy_Document.pdf \
  --pdf-engine=xelatex \
  --toc \
  --number-sections \
  -V geometry:margin=2cm \
  -V fontsize=11pt
```

This produces numbered sections, a table of contents, and professional typesetting — useful for producing customer-ready policy documents from the platform content.

<!-- QA_VERIFIED: 2026-04-16 -->
