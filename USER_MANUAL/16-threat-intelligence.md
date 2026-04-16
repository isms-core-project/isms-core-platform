# Threat Intelligence

<!-- ISMS-CORE:USER-MANUAL:16-threat-intelligence:v1.0:2026-04-16 -->

---

## Overview

The Threat Intelligence section gives you live access to four threat and vulnerability intelligence feeds integrated directly into the platform. This supports ISO 27001:2022 control A.5.7 (Threat intelligence) and provides the technical depth needed to assess your exposure to current adversary techniques.

Navigate to **Intelligence** in the sidebar.

---

## Threat Intelligence Feeds

The platform continuously pulls from six sources via the `isms-core-feeds` container:

| Feed | Update Frequency | What it provides |
|------|-----------------|-----------------|
| **MITRE ATT&CK** | Weekly | Full ATT&CK framework — tactics, techniques, sub-techniques, mitigations, adversary groups, software, campaigns |
| **MITRE ATLAS** | Weekly | AI/ML-specific adversary techniques (adversarial machine learning threat landscape) |
| **CISA KEV** | Daily | CISA's Known Exploited Vulnerabilities catalogue — CVEs actively exploited in the wild |
| **FIRST EPSS** | Daily | Exploit Prediction Scoring System — probability score (0–1) for each CVE being exploited in the next 30 days |
| **NVD CVE** | Weekly (full) + Daily (delta) | ~250,000 CVEs from the NIST National Vulnerability Database, indexed into OpenSearch |
| **NVD CPE** | Weekly | Software/hardware product identifiers (CPE) — enables correlating CVEs to specific products |

Feed run history and status is visible in **Intelligence → Threat Feeds**. The health of all feeds is also reflected in the Health Alert Banner and Dashboard Intelligence Cards.

---

## MITRE ATT&CK

Navigate to **Intelligence → MITRE ATT&CK**.

### Technique Browser

Browse the full ATT&CK framework organised by tactic. Each technique shows:

- Technique ID and name (e.g. T1190 — Exploit Public-Facing Application)
- Tactic (Initial Access, Execution, Persistence, etc.)
- Sub-techniques list
- Description and detection guidance
- Mitigations — ISO 27001 controls that address this technique

### Actor Intelligence

Navigate to the **Groups** tab to browse adversary groups. Each group shows:

- Attribution and aliases
- Target sectors and geographies
- Techniques used by this group
- Associated software and campaigns
- Link to MITRE ATT&CK official page

Use actor intelligence to contextualise your EBIOS RM Workshop 2 risk sources — if you operate in a sector targeted by a known group, their technique set tells you which of your controls are most tested.

### Heatmap

Navigate to the **Heatmap** tab for a MITRE ATT&CK Navigator-style technique heatmap. The heatmap shows:

- Which techniques are used by groups that target your sector
- Which techniques are referenced in your EBIOS RM attack paths
- Coverage overlay — which techniques are addressed by your ISO 27001 controls

---

## CVE / CPE Explorer

Navigate to **Intelligence → CVE Explorer**.

### CVE Search

Search and filter the NVD CVE index (~250,000 entries):

- **Keyword** — search CVE descriptions for specific products, vendors, or vulnerability types
- **Severity** — Critical / High / Medium / Low (based on CVSS v3 base score)
- **EPSS score** — filter for CVEs with a high exploitation probability
- **KEV only** — show only CVEs that appear in the CISA KEV list
- **Year** — filter by CVE publication year

### CVE Detail Panel

Click any CVE to open the detail panel:

- CVSS v2 and v3 scores and vector
- CWE (weakness type) categorisation
- CPE applicability list (which products are affected)
- EPSS score and percentile
- KEV status and date added to KEV list
- NVD reference links

### CPE Tab

The CPE tab allows you to search the software/hardware product catalogue. Useful for identifying all CVEs affecting a specific product in your environment.

---

## KEV Audit Report (A.8.8)

Navigate to **Intelligence → KEV Audit**.

The KEV Audit Report is a purpose-built evidence artefact for ISO 27001:2022 A.8.8 (Management of technical vulnerabilities). It shows:

- All CISA KEV entries by status — open, patched, in progress, not applicable
- Remediation status breakdown by CVE
- Per-vendor summary (how many KEVs affect each vendor's products)
- Time-to-remediate statistics

Export the report as CSV for inclusion in your audit evidence pack. The report provides an auditor with a defensible view of how your organisation tracks and remediates actively exploited vulnerabilities.

---

## MITRE ATLAS (AI/ML Threats)

Navigate to **Intelligence → ATLAS** for the AI/ML-specific threat framework. ATLAS documents techniques used to attack machine learning systems — training data poisoning, adversarial examples, model extraction, and more.

ATLAS is relevant to the AI Extension Pack (ISO 42001:2023) — specifically controls covering AI risk assessment, robustness, and incident management.

---

## Intelligence and Evidence

Threat intelligence data integrates with the Evidence Tracker. The CISA KEV feed in particular is linked to evidence collection:

- When a new KEV entry matches a CVE relevant to your environment, a notification is generated
- KEV remediation status can be promoted to the Evidence Tracker as proof of active vulnerability management under A.8.8

---

## Feed Configuration

Feed configuration is an administrator function (enabling/disabling feeds, setting the `NIST_API_KEY` for NVD access, toggling CPE Option B). See your administrator if a feed is not running or if you need to change feed settings.

The **CPE Option B** toggle in **Intelligence → Threat Feeds** allows an administrator to switch the NVD CPE pull strategy between KEV-vendor CPEs (lightweight) and full CPE library (comprehensive) without restarting containers.

<!-- QA_VERIFIED: 2026-04-16 -->
