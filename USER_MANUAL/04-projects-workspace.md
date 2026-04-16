# Projects Workspace

<!-- ISMS-CORE:USER-MANUAL:04-projects-workspace:v1.0:2026-04-16 -->

---

## What Is a Project?

A **Project** is a named workspace that owns a curated set of policies, implementation guides, assessments, gaps, and evidence. It is the operational unit of your ISMS — everything you work on day to day happens inside a project.

Typical projects:

- Your main ISO 27001 certification scope
- A specific audit cycle (e.g. "Surveillance Audit 2026")
- An organisational unit or subsidiary with its own scope
- A privacy-specific project for ISO 27701 work

Navigate to **Projects** in the sidebar to see your project list and create new ones.

---

## Creating a Project

1. Click **New Project**
2. Enter a project name and optional description
3. Select the product family (ISMS, Privacy, Cloud, AI — or all)
4. Set document variables (see below) — these are applied automatically to all documents you add to the project
5. Click **Create**

The new project appears in your project list. Click it to open the project workspace and make it your active project.

---

## Document Variables

Document variables are organisation-specific tokens that get substituted into policy documents when you add them to a project. This is how a generic "Organisation Name shall..." becomes "Bamboo Tech AG shall..." automatically.

Common variables include:

| Variable | Example |
|----------|---------|
| Organisation name | Bamboo Tech AG |
| CISO / RSSI name | Jane Smith |
| DPO name | Marc Dupont |
| Effective date | 2026-05-01 |
| Review date | 2027-05-01 |
| Document owner | Information Security Team |

Variables are set when you create the project and can be updated in **Project Settings**. When updated, you can bulk re-apply them to all documents in the project.

---

## Adding Content to a Project

### Adding Policies

1. Open your project and go to the **Policies** tab
2. Click **Add from Library**
3. Browse or search for the policy documents you want
4. Select one or more documents and click **Add**

When a policy is added, document variable substitution is applied automatically — the platform replaces all variable tokens in the document with your project values.

### Adding Implementations

Navigate to the **Implementations** tab and use the same Add from Library flow. IMP-UG (user-facing) and IMP-TG (technical) documents are listed separately.

### Bulk Actions

From the Policies or Implementations tab, use the checkbox column to select multiple documents and perform bulk actions:

- **Apply variables** — re-substitute document variables (use this after updating project variables)
- **Change status** — move selected documents to draft, review, approved, or published
- **Move to bin** — soft-delete selected documents (they can be restored)

---

## Document Editor

Click any document in your project to open the **Document Editor**. The editor has two modes:

### WYSIWYG Mode (default)

A rich-text editor powered by TipTap v3. You can:

- Edit text directly — use the formatting toolbar for headings, bold, italic, lists, and tables
- Add and edit tables (grid tables are automatically converted to GitHub Flavored Markdown on save)
- Insert images (drag and drop or paste)

Your changes are auto-saved. The document retains its original structure — only the content you changed is modified.

### Source Mode

Click the **Source** toggle to switch to raw Markdown editing. This is useful for precise formatting or bulk text changes. Switch back to WYSIWYG at any time — the platform renders your Markdown correctly.

> Metadata comment blocks (watermarks) are automatically stripped from the editing view so they do not distract from the document content. They are preserved in the stored document.

---

## Document Lifecycle (Approval Workflow)

Each document in a project has a lifecycle state:

| State | Meaning |
|-------|---------|
| **Draft** | Work in progress — not yet approved |
| **Review** | Submitted for review by ISMS Manager or Admin |
| **Approved** | Reviewed and approved — ready to publish |
| **Published** | Active — the current version in use |

Auditors can see all states. Only published documents are considered "active" for compliance scoring purposes.

Change a document's state using the **Status** dropdown in the document editor or via bulk actions in the policy list.

---

## SCR Checklists

Each policy in your project has an associated **SCR (Self-Assessment Checklist)**. The SCR tab in the document view shows the checklist items for that control group.

For each item:

1. Set the **status** — Compliant, Partial, Non-compliant, Not applicable
2. Add a **comment** explaining your evidence or rationale
3. **Link evidence** items directly to the checklist item

Completeness scoring (what percentage of checklist items have a status set) is shown as a progress bar on the SCR tab and feeds into the project's overall compliance score.

---

## Project Completeness Score

The project overview page shows an overall completeness score — a weighted summary of:

- Policy document coverage (% of expected policies added)
- Assessment completion (% of SCR items with a status set)
- Evidence attachment rate (% of checklist items with at least one evidence item)

This is your primary "are we ready for audit?" indicator at a glance.

---

## Bin and Restore

Documents moved to the bin are soft-deleted — they do not appear in the project views but are not permanently removed. To restore:

1. Go to **Project Settings → Bin**
2. Select the documents to restore
3. Click **Restore**

Permanent deletion is available from the bin view and requires Admin or ISMS Manager role.

---

## Switching the Active Project

Only one project is active at a time. Risk scenarios, gaps, and evidence items are scoped to the active project — switching projects switches your working context.

To switch:

1. Click the active project chip in the sidebar
2. Select the project you want from the list

Or navigate to **Projects** and click **Set Active** on any project.

<!-- QA_VERIFIED: 2026-04-16 -->
