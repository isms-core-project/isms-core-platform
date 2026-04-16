# QA Engine

<!-- ISMS-CORE:USER-MANUAL:18-qa-engine:v1.0:2026-04-16 -->

---

## Overview

The QA Engine validates that all expected policy and implementation artefacts are present and contain the minimum required content. It is an internal quality control tool — useful before audits, after content imports, or when onboarding new users who need to verify their project is complete.

Navigate to **Tools → QA Engine** in the sidebar.

---

## What the QA Engine Checks

The QA Engine runs two types of checks:

### Existence Check

Verifies that all expected documents are present in the platform for the selected product family and control groups.

For each expected document (POL, IMP-UG, IMP-TG, SCR, REF, CTX, FORM), the check returns:

| Result | Meaning |
|--------|---------|
| **Present** | Document is in the platform and indexed |
| **Missing** | Expected document has not been imported |

Missing documents are flagged with the document ID and type for easy follow-up with the administrator.

### Keyword / Content Check

Verifies that each document contains the minimum expected content — key terms, required sections, and structural markers that indicate the document is substantively complete rather than a placeholder.

For each document, the content check returns:

| Result | Meaning |
|--------|---------|
| **Pass** | Document contains all expected keywords and structural elements |
| **Warn** | Document is present but missing some expected content — review recommended |
| **Fail** | Document is missing significant required content |

---

## Running the QA Engine

1. Navigate to **Tools → QA Engine**
2. Select the **scope**:
   - **Product family** — ISMS / Privacy / Cloud / AI
   - **Control groups** — all, or select specific groups from the list
3. Select the **reference mode**:
   - **Internal** — check against the ISMS CORE Gold Standard corpus only
   - **External** — check against imported external documents (your own policies)
   - **Both** — cross-reference against both corpora
4. Click **Run QA Check**

Results appear within 15–60 seconds depending on scope.

---

## Reading QA Results

The results page shows a summary score (% of documents passing) and a detailed item list.

### Summary View

- Total documents checked
- Pass / Warn / Fail / Missing counts
- Coverage percentage (documents present / documents expected)

### Detail View

Each document is listed with its QA result. Click any document to see:

- Which keyword checks passed
- Which keyword checks failed (with the missing terms listed)
- The relevant section from the Gold Standard corpus for comparison (if reference mode includes corpus)

---

## Project-Scoped QA

By default, the QA Engine checks the global content library. To check the documents in your active project specifically:

1. Select **Project scope** from the scope dropdown
2. The QA Engine will check only the documents present in your active project

This is useful for verifying that a project is fully populated before an audit — you want to confirm that every expected control has a policy and SCR in your project, not just in the library.

---

## Organisation-Level QA (ISMS Manager and above)

Navigate to the **Org Aggregate** tab to see a QA summary rolled up across all projects in your organisation. This gives the ISMS Manager a portfolio view of content completeness across multiple audit scopes or organisational units.

---

## Multilingual Support

The QA Engine supports keyword checks in EN, FR, DE, and IT. When checking a non-English document, the engine uses the appropriate language keyword set automatically — you do not need to configure this.

The keyword translation sets are seeded during the bootstrap process and can be refreshed by the administrator.

---

## QA Engine vs ISMS Compass

| Tool | What it checks | When to use |
|------|---------------|-------------|
| **QA Engine** | Existence and structural completeness — are the right documents present and do they contain the expected sections? | Pre-audit inventory check; after content imports |
| **ISMS Compass** | Semantic quality — does the document say the right things? | Drafting and review; evaluating existing policies against the Gold Standard |

Use the QA Engine first (quick inventory), then ISMS Compass for detailed gap analysis on flagged documents.

<!-- QA_VERIFIED: 2026-04-16 -->
