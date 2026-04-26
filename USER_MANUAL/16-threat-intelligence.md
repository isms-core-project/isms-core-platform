# Threat Intelligence

<!-- ISMS-CORE:USER-MANUAL:16-threat-intelligence:v1.1:2026-04-26 -->

---

## Overview

The Threat Intelligence section gives you live access to eleven threat and vulnerability intelligence sources integrated directly into the platform. This supports ISO 27001:2022 control A.5.7 (Threat intelligence) and provides the technical depth needed to assess your exposure to current adversary techniques, actively exploited vulnerabilities, and real-world IOC data from public OSINT feeds.

Navigate to **Intelligence** in the sidebar.

---

## Threat Intelligence Feeds

The platform pulls from two dedicated containers:

**`isms-core-feeds`** — vulnerability and adversary intelligence:

| Feed | Update Frequency | What it provides |
|------|-----------------|-----------------|
| **MITRE ATT&CK** | Weekly | Full ATT&CK framework — tactics, techniques, sub-techniques, mitigations, adversary groups, software, campaigns |
| **MITRE ATLAS** | Weekly | AI/ML-specific adversary techniques (adversarial machine learning threat landscape) |
| **CISA KEV** | Daily | CISA's Known Exploited Vulnerabilities catalogue — CVEs actively exploited in the wild |
| **FIRST EPSS** | Daily | Exploit Prediction Scoring System — probability score (0–1) for each CVE being exploited in the next 30 days |
| **NVD CVE** | Weekly (full) + Daily (delta) | ~250,000 CVEs from the NIST National Vulnerability Database, indexed into OpenSearch with CVSS 4.0 support |
| **NVD CPE** | Weekly | Software/hardware product identifiers — enables correlating CVEs to specific products |
| **ENISA EUVD** | Daily | EU Vulnerability Database — exploited-flag CVEs and high-severity (CVSS ≥ 4.0) EU-assigned entries; cross-enriched into NVD CVE docs with `in_euvd` flag |

**`isms-core-threat-intel`** — OSINT IOC feeds (optional profile):

| Feed | Update Frequency | What it provides |
|------|-----------------|-----------------|
| **CIRCL MISP** | Every 6 hours (delta) | Public OSINT feed from Luxembourg CIRCL — IOCs (IPs, domains, URLs, file hashes) with ATT&CK TIDs, Malpedia family + actor tags from MISP galaxy attributes |
| **Botvrij MISP** | Every 6 hours (delta) | Public OSINT feed (botvrij.eu) — same schema as CIRCL, deduplicated by IOC value + source |
| **AbuseIPDB** | Daily | Top 10,000 highest-confidence abusive IPs; on-demand single-IP enrichment (abuse score, reports, categories) with 24h cache |
| **Malpedia** | Weekly | Malware family knowledge base (aliases, descriptions, ATT&CK TIDs, associated actors) and threat actor directory (country, motivation) |

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
- **EUVD flag** — show only CVEs present in the EU Vulnerability Database
- **Year** — filter by CVE publication year

### CVE Detail Panel

Click any CVE to open the detail panel:

- CVSS v2, v3, and v4 scores and vector strings
- CWE (weakness type) categorisation
- CPE applicability list (which products are affected)
- EPSS score and percentile
- KEV status and date added to KEV list
- EUVD flag and EU-assigned identifier where available
- NVD reference links

### CPE Tab

The CPE tab allows you to search the software/hardware product catalogue. Useful for identifying all CVEs affecting a specific product in your environment.

---

## ENISA EUVD Explorer

Navigate to **Intelligence → EUVD Explorer**.

The EUVD Explorer provides access to ENISA's European Vulnerability Database — the EU's authoritative source for vulnerability information relevant to European operators under NIS2 and DORA obligations.

- Browse vulnerabilities marked as **exploited in the wild** (highest priority for patching)
- Filter by CVSS severity — focus on critical and high-severity entries
- See EU-assigned EUVD identifiers alongside CVE IDs
- Detail panel shows affected vendors, products, aliases, EPSS score, and CVSS data
- Export filtered sets as CSV for audit evidence under ISO 27001 A.8.8

The EUVD feed cross-enriches the NVD CVE index: each CVE that appears in EUVD gets an `in_euvd` flag and `euvd_id` field, visible in the CVE Explorer.

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

## IOC Explorer

Navigate to **Intelligence → IOC Explorer**.

The IOC Explorer provides a searchable table of all Indicators of Compromise collected from the OSINT feeds (CIRCL MISP, Botvrij MISP, AbuseIPDB). This requires the `isms-core-threat-intel` container to be running.

### Searching IOCs

Filter by:

- **Type** — IP address / domain / URL / file hash (MD5, SHA1, SHA256)
- **Source** — CIRCL MISP / Botvrij MISP / AbuseIPDB
- **MITRE technique** — filter IOCs tagged with a specific ATT&CK TID
- **Tag** — MISP event tags (e.g. `tlp:white`, `misp-galaxy:malpedia`)
- **Free text** — search IOC values directly

### IOC Detail

Each IOC row shows:

- IOC value and type
- Source feed and first/last seen timestamps
- Confidence score (AbuseIPDB) or feed confidence
- Associated ATT&CK techniques (from MISP galaxy tags)
- Associated malware family and threat actor (resolved from Malpedia slugs at ingest)

The correlation model stamps ATT&CK TIDs, Malpedia family slugs, and actor slugs onto IOCs at ingest time — no runtime joins are performed. This means an IP address can carry its abuse score, the malware family it was seen distributing, the threat actor group attributed to that family, and the ATT&CK techniques that actor uses, all in a single record.

---

## IP Enrichment

Navigate to **Intelligence → IP Enrichment**.

Enter any IP address to retrieve on-demand enrichment from two sources:

### AbuseIPDB Check

- **Abuse confidence score** (0–100): probability the IP is malicious
- **Total reports** in the AbuseIPDB database
- **Last reported at** timestamp
- **Usage type** (ISP / Data Centre / VPN / etc.)
- **Categories** of reported abuse (port scan, brute force, web spam, etc.)

### Shodan Data

If `SHODAN_API_KEY` is configured:

- Open ports and service banners
- Hostnames and reverse DNS
- ASN and organisation
- CVEs detected on the host (from Shodan scanning)
- Last scan date

If no Shodan API key is set, the **Shodan InternetDB** free service is used as a fallback — provides open ports, CPEs, tags, hostnames, and a CVE list without requiring an account.

If an IP is not indexed in Shodan (common for transit IPs and private ranges), the widget shows "IP not indexed" rather than an error.

Enrichment results are cached for 24 hours to respect API rate limits. The cache is per-IP and resets automatically.

---

## Malware Atlas

Navigate to **Intelligence → Malware Atlas**.

The Malware Atlas exposes the Malpedia knowledge base ingested by the threat-intel container. It requires the `isms-core-threat-intel` container to be running with `TI_MALPEDIA_ENABLED=true`.

### Malware Families

Browse the full Malpedia family catalogue:

- **Family name** and common aliases
- **Description** — origin, targets, first seen, capabilities
- **ATT&CK TIDs** — ATT&CK techniques associated with this family
- **Associated actors** — threat groups known to use this malware
- Link to Malpedia source page

### Threat Actors

Browse the threat actor directory:

- **Actor name** and aliases
- **Country attribution** (suspected state-sponsored origin)
- **Motivation** — espionage / financial / hacktivism / unknown
- **Description** — activity summary and known targets

> **Note:** Malware family and threat actor data is sourced from the MISP galaxy (open GitHub dataset) — no API key required.

### Correlation Use

The Malware Atlas is the lookup endpoint for IOC correlation. When MISP events contain galaxy tags like `misp-galaxy:malpedia="win.emotet"`, the ingest pipeline resolves the Malpedia slug to a family record and stamps it on the IOC. You can pivot from:

- IOC → Malware Family → ATT&CK Techniques
- IOC → Malware Family → Threat Actor → Country of origin
- Threat Actor → All associated malware families → All ATT&CK techniques used

---

## Intelligence and Evidence

Threat intelligence data integrates with the Evidence Tracker. The CISA KEV feed in particular is linked to evidence collection:

- When a new KEV entry matches a CVE relevant to your environment, a notification is generated
- KEV remediation status can be promoted to the Evidence Tracker as proof of active vulnerability management under A.8.8
- IOC Explorer results can be referenced in gap notes and remediation actions as evidence of active threat targeting

---

## Feed Configuration

Feed configuration is an administrator function. See your administrator if a feed is not running or if you need to change feed settings.

Key environment variables:

| Variable | Description |
|----------|-------------|
| `ABUSEIPDB_API_KEY` | Required for AbuseIPDB blacklist + enrichment |
| `SHODAN_API_KEY` | Optional — paid Shodan API; InternetDB (free) used if absent |
| `TI_MISP_IMPORT_FROM_DATE` | First-run date floor for MISP history (default: `2024-01-01`) |
| `TI_RUN_ON_START` | Force all OSINT feeds to run on every container start |

The **CPE Option B** toggle in **Intelligence → Threat Feeds** allows an administrator to switch the NVD CPE pull strategy between KEV-vendor CPEs (lightweight) and full CPE library (comprehensive) without restarting containers.

<!-- QA_VERIFIED: 2026-04-26 -->
