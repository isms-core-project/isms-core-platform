# Threat Intelligence

<!-- ISMS-CORE:USER-MANUAL:16-threat-intelligence:v1.2:2026-05-02 -->

---

## Overview

The Threat Intelligence section gives you live access to 17+ threat and vulnerability intelligence sources integrated directly into the platform. This supports ISO 27001:2022 control A.5.7 (Threat intelligence) and provides the technical depth needed to assess your exposure to current adversary techniques, actively exploited vulnerabilities, and real-world IOC data from public OSINT feeds.

Navigate to **Intelligence** in the sidebar.

> When the `isms-core-threat-intel` optional profile is not active, all Intelligence sidebar items remain visible but are greyed out.

---

## Feed Containers

The platform runs two dedicated feed containers:

- **`isms-core-feeds`** — vulnerability and adversary intelligence (always active with the standard stack)
- **`isms-core-threat-intel`** — OSINT IOC feeds (optional; enabled with `--profile threat-intel` + `VITE_THREAT_INTEL_ENABLED=true`)

---

## Feed Schedules — Vulnerability & Adversary Intelligence

These feeds run in the `isms-core-feeds` container and are always active.

| Feed | Schedule (UTC) | What it provides |
|------|----------------|-----------------|
| **MITRE ATT&CK v19** | Weekly, Sun 00:00 | Full ATT&CK framework — tactics, techniques, sub-techniques, mitigations, adversary groups, software, campaigns |
| **MITRE ATLAS** | Weekly, Sun 00:30 | AI/ML-specific adversary techniques (adversarial machine learning threat landscape) |
| **CISA KEV** | Daily 02:00 | CISA's Known Exploited Vulnerabilities catalogue — CVEs actively exploited in the wild |
| **FIRST EPSS** | Daily 02:30 | Exploit Prediction Scoring System — probability score (0–1) for each CVE being exploited in the next 30 days |
| **NVD CVE** | Daily delta 03:00 / Full weekly Sun 01:00 | ~250,000 CVEs from the NIST NVD with CVSS v2/v3/v4 scores, CWEs, and CPE applicability |
| **NVD CPE** | Weekly, Sun 01:30 | Software/hardware product identifiers — enables correlating CVEs to specific products |
| **ENISA EUVD** | Daily | EU Vulnerability Database — exploited-flag CVEs and high-severity (CVSS ≥ 4.0) EU-assigned entries; cross-enriched into NVD CVE docs with `in_euvd` flag |
| **Exploit-DB** | Daily | ~52,000 public exploits; cross-enriches CVEs with `edb_id`, `edb_verified` (Metasploit flag), and `edb_description` |
| **MaxMind GeoLite2** | Weekly, Tue 01:00 | GeoIP database used for IP-to-country resolution across all feeds |

---

## Feed Schedules — OSINT IOC Feeds

These feeds run in the `isms-core-threat-intel` container. All feeds run automatically on first boot if no previous successful run exists.

| Feed | Schedule (UTC) | API key | What it provides |
|------|----------------|---------|-----------------|
| **CIRCL MISP** | Every 6h: 00:00, 06:00, 12:00, 18:00 | None | Public OSINT MISP feed from Luxembourg CIRCL — IOCs (IPs, domains, URLs, hashes) with ATT&CK TIDs, Malpedia family + actor tags |
| **Botvrij MISP** | Every 6h: 01:00, 07:00, 13:00, 19:00 (staggered) | None | Public OSINT feed (botvrij.eu) — same schema as CIRCL, deduplicated by IOC value + source |
| **AbuseIPDB** | Daily 02:00 | `ABUSEIPDB_API_KEY` | Top 10,000 highest-confidence abusive IPs; on-demand single-IP enrichment with 24h cache |
| **URLhaus** | Daily 03:00 | None | Malicious URLs hosting malware payloads, from abuse.ch |
| **ThreatFox** | Every 6h: 03:00, 09:00, 15:00, 21:00 | `THREATFOX_API_KEY` (optional) | IOCs (IPs, domains, URLs, hashes) linked to named malware families with confidence scores |
| **SSLBL** | Daily 04:00 | None | SSL certificate blacklist — SHA1 fingerprints of certificates used by malware C2 infrastructure |
| **AlienVault OTX** | Daily 04:30 | `OTX_API_KEY` | Open Threat Exchange pulses — IOCs with TLP labels, ATT&CK TIDs, and confidence scores derived from pulse subscriber count |
| **Feodo Tracker** | Every 6h: 04:30, 10:30, 16:30, 22:30 | None | C2 IP blocklist for Emotet, QakBot, TrickBot, and Dridex botnets (confidence 85) |
| **Red Flag Domains** | Daily 05:00 | None | Newly registered suspicious domains flagged for phishing, malware, and C2 |
| **Stopforumspam** | Daily 05:30 | None | ~140,000 IPs reported for spam, botnet activity, and forum abuse |
| **MalwareBazaar** | Every 6h: 02:00, 08:00, 14:00, 20:00 | `MALWAREBAZAAR_API_KEY` | Recent malware sample hashes (MD5/SHA1/SHA256) with family attribution |
| **Malpedia** | Weekly, Sun 03:00 | None | Malware family knowledge base (aliases, ATT&CK TIDs, associated actors) and threat actor directory |
| **VirusTotal** (enrichment) | Daily 07:00 | `VT_API_KEY` (optional) | Enriches existing IOCs with VT detection ratios — updates `confidence` field only; does not add new IOCs |
| **IPInfo** (enrichment) | After AbuseIPDB | `IPINFO_API_KEY` (optional) | Geo-enriches AbuseIPDB IPs with city, country, and ASN; 120s time budget per run |

> **First-boot note:** All OSINT feeds run once immediately on startup to seed the database. Large feeds (CIRCL MISP ~133K IOCs, Stopforumspam ~140K IPs, AlienVault OTX ~90K IOCs) take several minutes each. The scheduler handles subsequent delta updates automatically.

---

## Feed Status

Feed run history and status is visible on:

- **Dashboard** — Intelligence Cards panel (CVE count, KEV count, IOC count, MITRE sync status, overall feed health)
- **Intelligence → Threat Feeds** — full feed run history with last-run timestamps, status, and record counts for all feeds
- **Header banner** — if any feed or connector reports an error in the last 24 hours, a dismissible warning banner appears at the top of every page

If a feed shows an error badge (red dot on the Intelligence sidebar group), go to **Intelligence → Threat Feeds** to see the error details. Admins can trigger any feed on demand using the **RUN** button, or abort a running feed using **CANCEL**.

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

## Threat Exposure

Navigate to **Intelligence → Threat Exposure**.

> Requires the `isms-core-threat-intel` container to be active and populated.

The Threat Exposure page shows which of your ISO 27001 controls are exposed to active threat techniques observed in the live OSINT feeds. It joins ATT&CK technique IDs attached to IOCs in `ti_iocs` against the ATT&CK → ISO 27001 crosswalk, then cross-references your framework assessment scores.

### Summary bar

| Metric | Meaning |
|--------|---------|
| **Active techniques** | Distinct ATT&CK TIDs seen in live IOC feeds |
| **Affected controls** | ISO 27001 controls mapped to those techniques |
| **Gaps identified** | Affected controls with a low assessment score or status "non_compliant" / "not_assessed" |

### Technique → Control table

| Column | Meaning |
|--------|---------|
| Technique | ATT&CK TID (e.g. T1190) |
| IOC count | Number of active IOCs tagged with this technique |
| Sources | Feed sources contributing IOCs for this technique |
| ISO 27001 controls | Controls mapped to this technique, colour-coded by assessment score (green ≥ 70%, orange 40–69%, red < 40%, grey = not assessed) |
| Gaps | Count of controls in the gap state for this technique |

Use the Threat Exposure page to prioritise remediation: techniques with high IOC counts and red/grey controls represent your highest-risk exposure.

---

## CVE / CPE Explorer

Navigate to **Intelligence → CVE Explorer**.

### CVE Search

Search and filter the NVD CVE index (~250,000 entries):

| Filter | Options |
|--------|---------|
| Keyword | CVE ID or keyword in description |
| Severity | Critical / High / Medium / Low (CVSS v3 base score) |
| EPSS score | Slider (0.00–1.00) — filter by exploitation probability |
| KEV only | Show only CVEs on the CISA KEV list |
| EUVD flag | Show only CVEs present in the EU Vulnerability Database |
| EDB only | Show only CVEs with a known public exploit in Exploit-DB |
| Year | CVE publication year |

### CVE Detail Panel

Click any CVE to open the detail panel:

- CVSS v2, v3, and v4 scores and vector strings
- CWE (weakness type) categorisation
- CPE applicability list (which products are affected)
- EPSS score and percentile
- KEV status and date added to the KEV list
- EUVD flag and EU-assigned identifier where available
- EDB chip — `EDB` if a public exploit exists, `EDB✓` if a Metasploit module exists
- NVD reference links

### CPE Tab

The CPE tab allows you to search the software/hardware product catalogue. Useful for identifying all CVEs affecting a specific product in your environment.

---

## ENISA EUVD Explorer

Navigate to **Intelligence → EUVD Explorer**.

The EUVD Explorer provides access to ENISA's European Vulnerability Database — the EU's authoritative source for vulnerability information relevant to European operators under NIS2 and DORA obligations.

- Browse vulnerabilities marked as **exploited in the wild** (highest priority for patching)
- Filter by CVSS severity — focus on critical and high-severity entries
- Toggle **Exploited only** or **Critical only** to surface the highest-risk subsets
- See EU-assigned EUVD identifiers alongside CVE IDs
- Detail panel shows affected vendors, products, aliases, EPSS score, and CVSS data
- Export filtered sets as CSV for audit evidence under ISO 27001 A.8.8

The EUVD feed cross-enriches the NVD CVE index: each CVE that appears in EUVD gets an `in_euvd` flag and `euvd_id` field, visible in the CVE Explorer.

---

## KEV Audit Report (A.8.8)

Navigate to **Intelligence → Threat Feeds → A.8.8 KEV Audit Report**.

The KEV Audit Report is a purpose-built evidence artefact for ISO 27001:2022 A.8.8 (Management of technical vulnerabilities). It shows:

- All CISA KEV entries by status — open, patched, in progress, not applicable
- Remediation status breakdown by CVE
- Per-vendor summary (how many KEVs affect each vendor's products)
- Time-to-remediate statistics

Select the review window (3 / 6 / 12 months). Export the report as CSV for inclusion in your audit evidence pack. The report provides an auditor with a defensible view of how your organisation tracks and remediates actively exploited vulnerabilities.

---

## MITRE ATLAS (AI/ML Threats)

Navigate to **Intelligence → ATLAS** for the AI/ML-specific threat framework. ATLAS documents techniques used to attack machine learning systems — training data poisoning, adversarial examples, model extraction, and more.

ATLAS is relevant to the AI Extension Pack (ISO 42001:2023) — specifically controls covering AI risk assessment, robustness, and incident management.

---

## IOC Explorer

Navigate to **Intelligence → IOC Explorer**.

The IOC Explorer provides a searchable table of all Indicators of Compromise collected from the 12 OSINT feeds. This requires the `isms-core-threat-intel` container to be running.

### Filters

| Filter | Options |
|--------|---------|
| Search | Free-text IOC value search (substring match) |
| Type | IP / Domain / URL / MD5 / SHA1 / SHA256 |
| Source | CIRCL MISP / Botvrij MISP / AbuseIPDB / URLhaus / ThreatFox / SSL Blacklist / AlienVault OTX / Feodo Tracker / Red Flag Domains / Stopforumspam / MalwareBazaar / Malpedia |

### Table columns

| Column | Description |
|--------|-------------|
| Type | IOC type chip |
| Value | The indicator value (truncated — expand row for full value) |
| Source | Feed that contributed this IOC |
| Confidence | Detection ratio (0–100%); from feed metadata or VirusTotal enrichment |
| TLP | Traffic Light Protocol label (WHITE / GREEN / AMBER / RED) — sourced from MISP events and AlienVault OTX pulses |
| Last seen | Most recent date this IOC was observed in the feed |
| Attribution | Malware family, threat actor, and ATT&CK TID chips (up to 2 each shown inline) |

Click any row to expand the full detail view — shows the complete IOC value, first seen date, all family/actor/TID associations, and full tag list from the source feed.

The correlation model stamps ATT&CK TIDs, Malpedia family slugs, and actor slugs onto IOCs at ingest time — no runtime joins are performed. This means an IP address can carry its abuse score, the malware family it was seen distributing, the threat actor group attributed to that family, and the ATT&CK techniques that actor uses, all in a single record.

> **Malpedia note:** Malpedia does not contribute rows to the IOC Explorer — it populates the Malware Atlas (families, actors, tools) instead. A Malpedia IOC count of 0 is correct.

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

Enrichment results are cached for 24 hours to respect API rate limits.

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

> **Note:** Malware family and threat actor data is sourced from the MISP galaxy open GitHub dataset — no API key required.

### Correlation Use

The Malware Atlas is the lookup endpoint for IOC correlation. When MISP events contain galaxy tags like `misp-galaxy:malpedia="win.emotet"`, the ingest pipeline resolves the Malpedia slug to a family record and stamps it on the IOC. You can pivot from:

- IOC → Malware Family → ATT&CK Techniques
- IOC → Malware Family → Threat Actor → Country of origin
- Threat Actor → All associated malware families → All ATT&CK techniques used

---

## Intelligence and Evidence

Threat intelligence data integrates with the Evidence Tracker:

- When a new KEV entry matches a CVE relevant to your environment, a notification is generated
- KEV remediation status can be promoted to the Evidence Tracker as proof of active vulnerability management under A.8.8
- IOC Explorer results can be referenced in gap notes and remediation actions as evidence of active threat targeting
- The Threat Exposure page provides direct linkage between live IOC feeds and your ISO 27001 control assessment scores

---

## Feed Configuration

Feed configuration is an administrator function. See your administrator if a feed is not running or if you need to change feed settings.

| Variable | Required for | Free registration |
|----------|-------------|-------------------|
| `NIST_API_KEY` | Faster NVD seeding (raises rate limit from 5→50 req/30s) | nvd.nist.gov |
| `ABUSEIPDB_API_KEY` | AbuseIPDB blacklist + IP enrichment | abuseipdb.com |
| `SHODAN_API_KEY` | Shodan paid enrichment (InternetDB free fallback used if absent) | shodan.io |
| `OTX_API_KEY` | AlienVault OTX feed | otx.alienvault.com |
| `OTX_IMPORT_DAYS` | OTX history depth on first run (default: `90` days) | — |
| `THREATFOX_API_KEY` | Higher rate limits for ThreatFox (works at lower limits without key) | threatfox.abuse.ch |
| `MALWAREBAZAAR_API_KEY` | MalwareBazaar sample feed | bazaar.abuse.ch |
| `VT_API_KEY` | VirusTotal IOC enrichment (free tier: ~500 req/day) | virustotal.com |
| `VT_DAILY_LIMIT` | Max IOCs enriched per VT run (default: `450`, free-tier safe cap) | — |
| `MAXMIND_ACCOUNT_ID` / `MAXMIND_LICENSE_KEY` | GeoLite2 database for IP geolocation | maxmind.com |
| `IPINFO_API_KEY` | Enhanced geo + ASN enrichment for AbuseIPDB IPs | ipinfo.io |
| `TI_MISP_IMPORT_FROM_DATE` | MISP first-run date floor (default `2024-01-01`) | — |
| `TI_RUN_ON_START` | Force all OSINT feeds to run on every container start | — |

> **VirusTotal enrichment:** VT does not add new IOCs — it queries IOCs already in the database (NULL confidence first, then oldest check) and updates their `confidence` field only when the VT score is higher than the existing value. IOCs are re-checked every 30 days. The free tier allows ~500 requests/day; the default cap of 450 stays safely under that limit.

The **CPE Option B** toggle in **Intelligence → Threat Feeds** allows an administrator to switch the NVD CPE pull strategy between KEV-vendor CPEs (lightweight) and full CPE library (comprehensive) without restarting containers. The setting is stored in the platform database and overrides the `FEEDS_CPE_FULL` environment variable.

<!-- QA_VERIFIED: 2026-05-02 -->
