# Policies & Documents

<!-- ISMS-CORE:USER-MANUAL:05-policies-documents:v1.0:2026-04-16 -->

---

## The Policy Library

Navigate to **ISMS → Policies** to browse the full policy library. This is the global view of all policy and reference documents imported into the platform — across all products, languages, and control groups.

This is different from your project's policy list. Here you can browse the full catalogue, search, and preview documents before adding them to a project.

---

## Document Types

The platform handles several document types, each with a specific role in the ISMS:

| Type | Code | Description |
|------|------|-------------|
| Policy | POL / OP-POL / PRIV-POL / CLD-POL / AI-POL | The "what, who, and with what" document for a control group |
| Instruction | INS | Foundation platform instructions and orientation docs |
| Reference | REF | Technical reference material supporting a control (hardening guides, configuration baselines) |
| Context | CTX | Regulatory and legal context document for a control |
| Form | FORM | Templates and forms used in operating the control |
| Implementation Guide (User) | IMP-UG | How to implement the control — written for ISMS Managers and process owners |
| Implementation Guide (Technical) | IMP-TG | How to implement the control — written for engineers and system administrators |

---

## Filtering the Policy Library

Use the filter bar at the top of the policy library to narrow the list:

- **Product** — ISMS / Privacy / Cloud / AI
- **Type** — POL, REF, CTX, FORM, INS, IMP-UG, IMP-TG
- **Language** — EN, FR, DE, IT
- **Control group** — filter to a specific Annex A section
- **Status** — draft, review, approved, published

Multiple filters can be combined.

---

## Full-Text Search

The search bar at the top of the policy library searches across the full content of all policy and implementation documents — not just titles and IDs. This is powered by OpenSearch and returns results ranked by relevance.

Type any keyword, regulatory term, or control concept to find relevant documents. Examples:

- `encryption at rest` — finds all policies and IMPs covering data-at-rest encryption
- `TOTP MFA` — finds implementation guides covering multi-factor authentication
- `GDPR Article 32` — finds policies that reference this article
- `vulnerability scanning` — finds all documents discussing vulnerability management

Use the product filter alongside search to narrow results to a specific product family.

---

## Previewing a Document

Click any document in the list to open the preview panel. The preview shows the rendered Markdown — formatted as the auditor or end-user would see it.

From the preview panel you can:

- **Copy document ID** — for referencing in gaps or evidence
- **Add to project** — add the document to your active project
- **View raw source** — see the underlying Markdown

---

## Document States

Documents imported from the content library start in **imported** state. Once added to a project, they enter the project's approval lifecycle (Draft → Review → Approved → Published).

The global library view shows documents in their library state. The project view shows documents in their project-specific state. The same document can be in different states across different projects.

---

## Languages and Localisation

The library contains documents in up to four languages. Use the **Language** filter to view documents in a specific language.

When your organisation has a country configured (see [Organisations & Users](20-organisations-users.md)), policy documents are rendered with jurisdiction-specific regulatory references automatically substituted. This happens transparently — the underlying document is unchanged; the display adapts to your organisation's jurisdiction.

---

## Foundation Documents

Two foundation document types sit above the standard control groups:

- **INS-POL-00** — ISMS CORE Platform Introduction: an orientation document for all users
- **INS-POL-01** — ISMS CORE Framework Introduction: an overview of the ISO 27001:2022 control structure

These are always available regardless of which product families are active, and are typically the first documents added to a new project.

<!-- QA_VERIFIED: 2026-04-16 -->
