# ISMS Compass

<!-- ISMS-CORE:USER-MANUAL:17-isms-compass:v1.0:2026-04-16 -->

---

## What Is ISMS Compass?

ISMS Compass is an AI-powered gap analysis tool. Paste or upload any policy, procedure, or security document, and Compass compares it against the ISMS CORE Gold Standard — the curated corpus of ISO 27001:2022 policy and implementation content. It returns a structured gap analysis identifying what is present, what is missing, and what does not align.

Navigate to **Tools → ISMS Compass** in the sidebar.

> ISMS Compass requires the `ANTHROPIC_API_KEY` environment variable to be set by your administrator. If Compass shows a "not available" message, contact your administrator.

---

## What Compass Is For

Compass is designed for three use cases:

**Evaluating existing documentation:** You have policies written before adopting ISMS CORE. Paste them into Compass to understand how they compare against the Gold Standard before deciding whether to adopt ISMS CORE policies or adapt your existing ones.

**Reviewing drafts:** You have written a new policy or procedure. Compass identifies gaps, missing clauses, and non-aligned wording before it goes to review.

**Pre-audit health check:** Paste any auditor-facing document into Compass to get a second opinion on its coverage before the audit.

---

## Using ISMS Compass

1. Navigate to **Tools → ISMS Compass**
2. Select the **product family** the document belongs to (ISMS / Privacy / Cloud / AI)
3. Optionally select the specific **control group** — narrowing the context produces more precise results
4. Paste the document text into the input area, or upload a file (plain text, Markdown, or PDF)
5. Click **Analyse**

Compass processes the document against the indexed corpus of ISMS CORE policies and implementation guides. This takes 10–30 seconds depending on document length.

---

## Reading the Compass Report

The Compass report is structured in three sections:

### Alignment Summary

A brief assessment of how well the document aligns with the Gold Standard overall — strong alignment, partial coverage, or significant gaps. This is the executive summary.

### Present and Aligned

A list of clauses, topics, or requirements that are present in your document and align with the ISMS CORE Gold Standard. These are items the auditor will find satisfactory.

### Missing or Misaligned

The gap list — items that are expected by the Gold Standard but absent or insufficiently addressed in your document. Each gap item shows:

- What is missing or misaligned
- Why it matters (the ISO control it supports)
- A suggested improvement

### Suggested Additions

Specific language additions or structural changes that would bring the document closer to the Gold Standard. These are suggestions, not mandates — your professional judgement takes precedence.

---

## What Compass Is Not

**Compass is not a compliance certification tool.** A green Compass report does not mean your ISMS is certified. It means your document aligns well with the ISMS CORE content baseline.

**Compass does not have access to your environment.** It analyses the text you provide. It cannot know whether your stated policies are actually implemented.

**Compass is a drafting aid, not an auditor.** Use it to improve document quality and catch gaps early — not as a substitute for proper audit preparation.

---

## The Reference Corpus

Compass compares your document against a curated corpus of ~12,987 indexed chunks derived from the ISMS CORE policy and implementation guide library. The corpus is organised by product family and control group.

The corpus is updated whenever your administrator reloads it with updated content (via **Admin → System → Reload QA Corpus**).

<!-- QA_VERIFIED: 2026-04-16 -->
