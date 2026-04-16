# Evidence Management

<!-- ISMS-CORE:USER-MANUAL:09-evidence-management:v1.0:2026-04-16 -->

---

## Why Evidence Matters

Evidence is the proof that a control is operating effectively. Without evidence, a compliant assessment score is an assertion — with it, it becomes an auditable fact. ISMS CORE Platform manages two types of evidence: evidence you upload manually and evidence collected automatically by connectors.

---

## The Evidence Tracker

Navigate to **Evidence → Evidence Tracker** in the sidebar.

The tracker shows all evidence items in your active project, with:

- **Control group** — which control this evidence supports
- **Title** — what the evidence is
- **Source** — where it came from (manual upload, specific connector, external system)
- **Date collected** — when the evidence was gathered
- **Expiry date** — when the evidence needs to be renewed
- **Verification status** — Verified / Pending verification / Expired
- **Freshness indicator** — colour-coded based on age and expiry

---

## Adding Evidence Manually

1. Navigate to **Evidence → Evidence Tracker**
2. Click **New Evidence**
3. Fill in the evidence form:

| Field | Description |
|-------|-------------|
| **Title** | Descriptive name (e.g. "Annual penetration test report 2026") |
| **Control group** | Which control this evidence supports |
| **Type** | Document / Screenshot / Configuration export / Log / Report / Certificate / Other |
| **Description** | What the evidence demonstrates |
| **Collection date** | When the evidence was gathered |
| **Expiry date** | When it needs to be renewed (leave blank if it does not expire) |
| **Attachment** | Upload a file (PDF, PNG, XLSX, etc.) |

4. Click **Save**

The evidence item appears in the tracker and is linked to the control group you specified.

---

## Linking Evidence to Checklist Items

Evidence can be attached to specific checklist items for precise audit traceability:

1. Open a compliance assessment or SCR checklist
2. Click the evidence icon on any checklist item
3. Select existing evidence items from the tracker, or create a new one

When an evidence item is linked to a checklist item, it appears in the item detail and in audit exports — auditors can see exactly which evidence supports which control statement.

---

## Expiry and Freshness

Evidence items with an expiry date are monitored automatically:

| Status | Meaning |
|--------|---------|
| **Current** | Expiry date is in the future (green) |
| **Expiring soon** | Expiry within 30 days (amber) |
| **Expired** | Past expiry date (red) |
| **No expiry** | Evergreen evidence — typically configuration exports or certificates with defined validity |

The `evidence_freshness` KPI metric on the dashboard reflects the percentage of evidence items that are current. Expired evidence is flagged and triggers the health notification if above a threshold.

---

## Automated Evidence (Connector Evidence)

The platform collects evidence automatically from 44 integrated systems via the connector layer. This evidence appears in two places:

### Automated Evidence Tab (per control group)

Each control group detail view has an **Automated Evidence** tab showing the most recent connector evidence for that group — updated every 60 seconds. Items show:

- Source connector (e.g. "Microsoft Entra ID", "CrowdStrike Falcon")
- Collection timestamp
- Classification (Access Control, Vulnerability, Configuration, etc.)
- Summary text of what was collected

### Promoting Connector Evidence

To move a connector evidence item into your formal Evidence Tracker:

1. Open the Automated Evidence tab on the relevant control group
2. Click **Promote** on the evidence item
3. The item appears in your Evidence Tracker with source, timestamp, and classification pre-filled

Promotion creates a permanent record in your tracker — the promoted item is no longer just a transient feed entry.

---

## Evidence for Audit Packs

When preparing for an audit, use the Evidence Tracker filter to:

1. Filter by control group to see all evidence for a specific control
2. Check for gaps — control groups with no evidence are flagged
3. Check for expiry — ensure no evidence has lapsed before the audit date
4. Export the evidence list as CSV or XLSX for the auditor pack

The export includes file attachment references, dates, and all metadata — auditors can request specific attachments based on the export.

---

## Verification Workflow

Evidence items can be marked as:

- **Pending verification** — collected but not yet reviewed
- **Verified** — reviewed and confirmed as valid by an ISMS Manager or Admin
- **Expired** — past expiry date (set automatically)

Only verified evidence counts fully towards the `evidence_freshness` KPI metric. Mark connector-promoted evidence as verified once you have confirmed it is accurate and relevant.

<!-- QA_VERIFIED: 2026-04-16 -->
