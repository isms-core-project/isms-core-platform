# ISMS CORE Platform — User Guide

**Version:** 1.0  
**Audience:** ISMS Managers · Auditors · Control Owners  
**Platform:** ISMS CORE v1.0

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Dashboard](#dashboard)
4. [Projects Workspace](#projects-workspace)
5. [Controls Library](#controls-library)
6. [Compliance Assessments](#compliance-assessments)
7. [Gap Tracking](#gap-tracking)
8. [QA Engine](#qa-engine)
9. [Evidence & Connectors](#evidence-connectors)
10. [Threat Intelligence & Vulnerability Feeds](#threat-intelligence)
11. [Risk Register](#risk-register)
12. [EBIOS RM](#ebios-rm)
13. [Business Impact Analysis](#business-impact-analysis)
14. [Third-Party Risk Management](#third-party-risk-management)
15. [Crosswalk & Framework Mapping](#crosswalk-framework-mapping)
16. [Metrics & KPI Dashboard](#metrics-kpi-dashboard)
17. [Country Localisation](#country-localisation)
18. [AI Extension Pack](#ai-extension-pack)
19. [Custom Frameworks](#custom-frameworks)
20. [Organisation & User Management](#organisation-user-management)
21. [MFA & Account Security](#mfa-account-security)

---

## Introduction {#introduction}

ISMS CORE is a compliance management platform covering ISO 27001:2022 and four extension standards. It turns your static policy documents, implementation guides, and control workbooks into a live compliance system — with gap tracking, risk management, evidence collection, and cross-framework mapping.

Five product families are available:

| Product | Standard | Control groups |
|---------|----------|---------------|
| **ISMS Framework** | ISO 27001:2022 | 54 Annex A groups |
| **ISMS Operational** | ISO 27001:2022 | 53 lightweight policies |
| **Privacy Extension** | ISO 27701:2025 | 21 privacy groups |
| **Cloud Extension** | ISO 27018:2025 | 12 cloud PII groups |
| **AI Extension** | ISO 42001:2023 + ISO 42005:2025 | 10 AI management groups |

### What you can do with ISMS CORE

- Manage your ISMS across 99 control groups covering ISO 27001, ISO 27701, ISO 27018, and ISO 42001
- Track control implementation status, gaps, and evidence
- Run compliance assessments across 24 regulatory frameworks (NIS2, DORA, NIST CSF 2.0, NIST AI RMF 1.0, CSA CCM, NIST SP 800-53, NCSC CAF v4.0, and more)
- Collect evidence automatically via 44 integrations (Microsoft, CrowdStrike, Jira, ServiceNow, and more)
- Monitor live threat intelligence — MITRE ATT&CK, CISA KEV, NVD CVE/CPE feeds, EPSS scores
- Manage risks with a full 5×5 risk register and treatment workflow
- Run EBIOS RM workshops (French public sector methodology)
- Assess business impact (BIA) for continuity planning
- Track third-party and supplier risk
- Map your controls across multiple frameworks automatically
- Generate localised policies for 8 jurisdictions (CH default, AT, BE, DE, FR, GB, IT, LU)

### Personas

| Role | Primary use |
|------|-------------|
| **ISMS Manager** | Day-to-day management — projects, gaps, risk register, evidence |
| **Auditor** | Read-only review — assessments, gap status, evidence, reports |
| **Control Owner** | Update control implementation status, attach evidence |
| **Admin** | User management, organisation settings, connectors |
| **Super Admin** | Multi-org management, platform-level oversight |

---

## Getting Started {#getting-started}

### First login

1. Open the platform URL in your browser.
2. Enter your email address and password.
3. If your account has MFA enabled, enter the 6-digit code from your authenticator app.
4. You land on the Dashboard.

> **Default admin credentials** are set by your administrator during deployment. Contact your admin if you do not have credentials.

### Changing your password

1. Click your user avatar or name in the sidebar (bottom-left).
2. Select **Profile & Settings**.
3. Enter your current password and the new password.
4. Click **Save**.

Passwords must be at least 12 characters. Use a mix of letters, numbers, and symbols.

### Organisation setup (Admin)

When you first access the platform as an Admin:

1. Go to **Admin → Organisation Settings**.
2. Set your organisation name, country/jurisdiction, and contact details.
3. Assign a country — this controls which jurisdiction-specific tokens appear in your rendered policies (e.g., Swiss nLPD, UK GDPR, German DSGVO).
4. Invite users via **Admin → Users → Invite User**.

---

## Dashboard {#dashboard}

The Dashboard gives a live snapshot of your ISMS posture.

### Panels

| Panel | What it shows |
|-------|---------------|
| **Audit Readiness Score** | Composite score (0–100%) based on gap closure, evidence currency, and control implementation |
| **Control Coverage** | % of ISO 27001 controls with at least one mapped implementation |
| **Open Gaps** | Count of gaps by severity (Critical / High / Medium / Low) |
| **Recent Activity** | Last 10 actions across the platform |
| **Framework Coverage** | How your ISO 27001 controls map to other frameworks (NIS2, DORA, etc.) |
| **Risk Summary** | Open risks by treatment status |
| **Intelligence Cards** | Live feed status for CVE index, CISA KEV, MITRE ATT&CK, and feed health — click any card to navigate to the relevant Intelligence page |

### Interpreting the Audit Readiness Score

- **80–100%** — Audit-ready. All critical controls implemented, evidence current, no critical gaps.
- **60–79%** — Partially ready. Some critical gaps remain open or evidence is expiring.
- **Below 60%** — Significant gaps. Review the Gap Tracker and prioritise remediation.

The score recalculates automatically as you close gaps and attach evidence.

---

## Projects Workspace {#projects-workspace}

A **Project** is the container for your ISMS work. Each project holds policies, implementation documents, SCR checklists, and tracks completeness.

### Creating a project

1. Go to **Projects** in the sidebar.
2. Click **New Project**.
3. Enter a name, select the framework (ISO 27001:2022), and assign owners.
4. Click **Create**.

### Working with documents

Each project contains three document types:

| Type | Description |
|------|-------------|
| **Policies (POL)** | What your organisation does and who is responsible |
| **Implementations (IMP)** | How controls are implemented — User Guide (UG) and Technical Guide (TG) variants |
| **SCR Checklists** | Self-assessment checklists for each control |

Click any document to open it in the editor.

### WYSIWYG editor

The editor supports:
- Rich text formatting (headings, bold, italic, lists, tables)
- **Document variables** — tokens like `{{org_name}}`, `{{ciso_name}}`, `{{review_date}}` are substituted automatically with your organisation settings. Never edit these tokens directly.
- **Version history** — every save creates a version you can compare or restore.

### Document variables

Variables are populated from **Admin → Organisation Settings**. Common variables:

| Token | Value |
|-------|-------|
| `{{org_name}}` | Your organisation name |
| `{{ciso_name}}` | Name of your CISO/RSSI |
| `{{dpo_name}}` | Name of your DPO |
| `{{review_date}}` | Annual review date |
| `{{country}}` | Jurisdiction (e.g., Switzerland, Germany) |

### Completeness scoring

Each project shows a completeness percentage based on how many documents have been reviewed and approved. To advance a document:

1. Open the document.
2. Set its status to **Reviewed** or **Approved** using the status selector at the top.
3. The project score updates immediately.

### Bulk actions

From the project document list, select multiple documents with the checkboxes and use **Bulk Actions** to:
- Change status (Draft → Reviewed → Approved)
- Export to PDF
- Archive

---

## Controls Library {#controls-library}

The Controls Library is the reference layer — all 93 ISO 27001:2022 Annex A controls, organised into 53 control groups across 4 domains.

### Browsing controls

1. Go to **Controls** in the sidebar.
2. Browse by domain (Organisational / People / Physical / Technological) or search by control ID or keyword.
3. Click a control to see its full description, linked policies, implementation guides, and compliance status.

### Control detail view

Each control shows:
- **ISO 27001:2022 description** — normative text
- **Linked policies** — your POL documents mapped to this control
- **Implementation status** — Not Started / In Progress / Implemented / Under Review
- **Gap status** — whether a gap exists and its severity
- **Evidence** — attached evidence items
- **Crosswalk** — which other frameworks this control maps to

### Updating implementation status

1. Open a control.
2. Click **Edit Status**.
3. Select the implementation status and add an optional note.
4. Click **Save**.

Control Owners can update status for controls assigned to them. ISMS Managers can update any control.

---

## Compliance Assessments {#compliance-assessments}

ISMS CORE includes 24 built-in compliance assessment modules. Each module maps your ISO 27001 control posture to a specific regulatory framework.

### Available frameworks

| Framework | Scope |
|-----------|-------|
| NIST CSF 2.0 | US cybersecurity framework (tiered profiles, radar report, XLSX import/export) |
| NIST AI RMF 1.0 | US AI risk management framework (AI 100-1) — 72 subcategories, 0–4 maturity |
| NIST SP 800-53 Rev 5 | US federal security controls — 324 base controls across 20 families |
| NIS2 | EU network and information security directive |
| DORA | EU digital operational resilience (financial sector) |
| CIS Controls v8 | Center for Internet Security controls |
| CSA CCM v4.1 | Cloud Security Alliance Cloud Controls Matrix — 207 controls, 17 domains |
| CSA AICM v1.0.3 | Cloud Security Alliance AI Controls Matrix — 243 controls, 18 domains |
| BSI IT-Grundschutz | German federal security baseline |
| TISAX | Automotive sector information security |
| Swiss ISG (SR 128) | Swiss Federal Act on Information Security |
| Swiss nDSG | Swiss revised data protection act |
| EU Cyber Resilience Act | EU product security requirements |
| EU AI Act | EU artificial intelligence regulation |
| EU Cloud Sovereignty | EU cloud data sovereignty framework |
| CSRM | Swiss NCSC cyber security risk management |
| COBIT 2019 | ISACA IT governance and management framework |
| FINMA | Swiss financial market supervisory authority |
| BaFin BAIT | German banking IT supervision |
| CSSF LU | Luxembourg financial sector regulator |
| ACN IT | Italian national cybersecurity agency |
| UK NIS | UK network and information systems regulations |
| UK Operational Resilience | UK FCA/PRA operational resilience |
| NCSC CAF v4.0 | UK National Cyber Security Centre Cyber Assessment Framework — outcome-based assessment, 4 Objectives, 14 Principles, 41 Contributing Outcomes |

### Running an assessment

1. Go to **Assessments** in the sidebar.
2. Click **New Assessment**.
3. Select the framework and the project to assess.
4. Work through each control item — set status (Compliant / Partially Compliant / Non-Compliant / Not Applicable) and add evidence links.
5. Save at any time. Assessments auto-save on navigation.

### Assessment results

Once all items are scored, the assessment shows:
- **Overall compliance %**
- **Items by status** — breakdown chart
- **Critical gaps** — non-compliant items requiring action
- **Exportable report** — PDF summary for auditors

---

## Gap Tracking {#gap-tracking}

Gaps represent controls that are missing, partially implemented, or have insufficient evidence.

### Gap lifecycle

```
Identified → In Remediation → Resolved → Closed
```

Gaps can also be **Accepted** (formally acknowledged as a residual risk with sign-off).

### Creating a gap

Gaps can be created:
- **Automatically** — from a compliance assessment (non-compliant items generate gaps)
- **Manually** — from **Gaps → New Gap**

Manual gap fields:
- Control reference (ISO 27001 control ID)
- Severity (Critical / High / Medium / Low)
- Description
- Assigned owner
- Target remediation date

### Tracking remediation

1. Open a gap.
2. Click **Start Remediation**.
3. Log remediation actions — each action records the date, description, and who performed it.
4. Attach evidence when remediation is complete.
5. Set status to **Resolved**.

An ISMS Manager or Auditor can then **Close** the gap after reviewing evidence.

### Gap acceptance

If a gap cannot be remediated and the risk is formally accepted:

1. Open the gap.
2. Click **Accept Risk**.
3. Enter the justification and the name of the authorising manager.
4. Set an acceptance expiry date (mandatory — accepted risks must be reviewed periodically).

---

## QA Engine {#qa-engine}

The QA Engine validates your policy and implementation documents against normative ISO standards and cross-framework references.

### What it checks

The engine runs three types of checks:

| Check type | Description |
|-----------|-------------|
| **Keyword** | Detects required terms, mandatory clauses, and prohibited language |
| **Semantic** | Compares document sections against the reference corpus using AI similarity scoring |
| **Crosswalk** | Validates that control text meets requirements of mapped frameworks (NIS2, DORA, etc.) |

### Running a QA check

1. Go to a project and open the **QA** tab.
2. Select the documents to check.
3. Optionally filter by:
   - **Framework codes** — focus validation on specific frameworks (e.g., NIS2, DORA)
   - **Reference mode** — ISO only, crosswalk only, or both
4. Click **Run QA**.
5. Results appear per document — PASS / WARN / FAIL per check.

### Interpreting results

| Status | Meaning |
|--------|---------|
| **PASS** | Document meets the normative requirement |
| **WARN** | Document partially meets the requirement — review recommended |
| **FAIL** | Document does not meet the requirement — action required |

Click any result to see the exact text that triggered the finding and the reference it was checked against.

### Reference library

The QA engine validates against one of three reference libraries — selectable per run:

| Library | Contents |
|---------|---------|
| **ISO Standards** | ~12,987 indexed chunks from 50 standards and frameworks (default) |
| **Crosswalk** | Cross-framework mappings for the target frameworks selected |
| **CISA KEV Corpus** | CISA Known Exploited Vulnerabilities feed — use when validating vulnerability management controls (e.g. A.8.8) to check that your policies address actively exploited CVEs |

The ISO corpus loads automatically on platform startup. To reload it after a framework update, go to **Admin → System → Reload QA Corpus**.

---

## Evidence & Connectors {#evidence-connectors}

Evidence is the documentation that proves a control is implemented. ISMS CORE supports 44 connectors to pull evidence automatically from your tools.

### Evidence types

| Type | Examples |
|------|---------|
| **Policy** | Approved policy documents |
| **Configuration** | System configuration exports |
| **Log** | Access logs, audit trails |
| **Report** | Vulnerability scan reports, penetration test results |
| **Certificate** | ISO certificates, training records |
| **Screenshot** | UI evidence for manual controls |

### Attaching evidence manually

1. Open a control or gap.
2. Click **Attach Evidence**.
3. Upload a file or paste a URL.
4. Set the evidence type and expiry date.
5. Click **Save**.

Evidence with an expiry date generates a notification when it is approaching expiry (default: 30 days in advance).

### Connectors (automated evidence)

Connectors pull evidence automatically on a schedule. Supported connectors include:

**Identity & Access**
- Microsoft Entra ID, Active Directory, LDAP, FreeIPA, Authentik, Keycloak, Cisco ISE

**Endpoint & Detection**
- CrowdStrike Falcon, SentinelOne, Wazuh, Microsoft Defender

**Vulnerability Management**
- Tenable.sc, Tenable.io, Qualys, OpenVAS

**Cloud Security**
- AWS Security Hub, Azure CSPM (Defender for Cloud), GCP Security Command Center

**ITSM**
- Jira, ServiceNow

**Network & Firewall**
- FortiGate, FortiAnalyzer, Palo Alto PAN-OS, Cisco ASA, Zscaler

**Monitoring & SIEM**
- Microsoft Sentinel, PRTG, Zabbix, Graylog

**PAM**
- CyberArk, Devolutions Hub, HashiCorp Vault

**Asset Management**
- GLPI, NetBox

**DevSecOps**
- GitHub Advanced Security, GitLab

**Threat Intelligence**
- Filigran XTM (OpenCTI, OpenAEV), Generic Threat Intel feed

### Configuring a connector

1. Go to **Connectors** in the sidebar.
2. Click **New Connector**.
3. Select the connector type.
4. Enter the connection details (API URL, token or credentials).
5. Set the sync schedule (hourly / daily / weekly).
6. Click **Test Connection** — a green checkmark confirms the connector is working.
7. Click **Save**.

The connector runs on its schedule and attaches new evidence items to the mapped controls automatically.

---

## Threat Intelligence & Vulnerability Feeds {#threat-intelligence}

The **Intelligence** section aggregates live threat and vulnerability data from two dedicated feed containers. All feeds run on schedule — no external subscription required for the core feeds; some OSINT feeds require free API keys.

### Available feeds

**Vulnerability & adversary intelligence** (`isms-core-feeds` container):

| Feed | Source | Schedule | Description |
|------|--------|----------|-------------|
| **MITRE ATT&CK** | MITRE | Weekly (Sunday 00:00) | Full adversary TTP matrix — tactics, techniques, sub-techniques, mitigations, groups, software |
| **MITRE ATLAS** | MITRE | Weekly (Sunday 00:30) | AI/ML-targeted attack techniques |
| **CISA KEV** | CISA | Daily (02:00) | Known Exploited Vulnerabilities — CVEs with confirmed exploitation in the wild |
| **EPSS** | FIRST | Daily (02:30) | Exploit Prediction Scoring System — probability of exploitation in the next 30 days |
| **NVD CVE** | NIST | Daily delta (03:00) / Full weekly (Sunday 01:00) | Full NVD CVE database (~250,000 CVEs) with CVSS v2/v3/v4 scores, CWEs, and CPE applicability |
| **NVD CPE** | NIST | Weekly (Sunday 01:30) | Common Platform Enumeration entries for vendor/product resolution |
| **ENISA EUVD** | ENISA | Daily | EU Vulnerability Database — exploited-flag CVEs and high-severity (CVSS ≥ 4.0) EU-assigned entries |

**OSINT IOC feeds** (`isms-core-threat-intel` container — optional profile):

| Feed | Source | Schedule | Description |
|------|--------|----------|-------------|
| **CIRCL MISP** | CIRCL Luxembourg | Every 6h (delta) | Public OSINT MISP feed — IOCs (IPs, domains, URLs, hashes) with ATT&CK TIDs and Malpedia family/actor tags |
| **Botvrij MISP** | Botvrij.eu | Every 6h (delta, staggered) | Public OSINT MISP feed — same schema, deduplicated against CIRCL by IOC value + source |
| **AbuseIPDB** | AbuseIPDB | Daily (02:00) | Top 10,000 confidence=100 abusive IPs; on-demand single-IP enrichment cached 24h |
| **Malpedia** | Fraunhofer FKIE | Weekly (Sunday 03:00) | Malware family knowledge base (aliases, ATT&CK TIDs) and threat actor directory (country, motivation) |

### Feed status

The feed status is visible on:
- **Dashboard** — Intelligence Cards panel (CVE count, KEV count, IOC count, MITRE sync status, overall feed health)
- **Intelligence → Threat Feeds** — full feed run history with last-run timestamps, status, and record counts for all feeds
- **Header banner** — if any feed or connector reports an error in the last 24 hours, a dismissible warning banner appears at the top of every page

If a feed shows an error badge (red dot on the Intelligence sidebar group), go to **Intelligence → Threat Feeds** to see the error details.

### Threat Feeds page

Go to **Intelligence → Threat Feeds** to see:
- Live status cards for all configured feeds
- Last successful run and record count per feed
- Error details for any failed run
- On-demand trigger button to run a feed outside its schedule (admin only)

### CVE / CPE Explorer {#cve-explorer}

Go to **Intelligence → CVE / CPE** to search and explore the NVD CVE and CPE index.

**Stats bar** — always visible at the top:
- Total CVEs indexed, total CPEs indexed, total CISA KEV entries
- Last sync timestamp
- API key warning if `NIST_API_KEY` is not set (rate-limited to 5 req/30s without a key)

**CVE tab**

| Filter | Options |
|--------|---------|
| Search | CVE ID or keyword in description |
| Severity | Critical / High / Medium / Low / None |
| Min EPSS | Slider (0.00–1.00) — filter by exploitation probability |
| Year | Calendar year of publication |
| KEV only | Show only CVEs on the CISA KEV list |
| EUVD flag | Show only CVEs present in the EU Vulnerability Database |

Click a CVE row to open the detail panel — shows CVSS v2/v3/v4 scores and vectors, CWEs, CPE applicability statements, EPSS score, KEV status, EUVD badge, and NVD reference links.

**CPE tab** — search by keyword, filter by type (Application / Operating System / Hardware), source, and KEV-only.

### EUVD Explorer

Go to **Intelligence → EUVD Explorer** for the ENISA European Vulnerability Database view.

- Browse vulnerabilities marked as **exploited in the wild** — highest priority for patching under NIS2 and DORA
- Filter by CVSS severity (Critical / High / Medium / Low)
- Toggle **Exploited only** to surface the highest-risk subset
- Detail panel: affected vendors/products, EPSS score, CVSS data, EU-assigned EUVD identifier, aliases
- Export filtered results as CSV for audit evidence (A.8.8)

The EUVD feed cross-enriches the NVD CVE index: every CVE that appears in EUVD gets an `in_euvd` flag and `euvd_id` field visible in the CVE Explorer.

### IOC Explorer

Go to **Intelligence → IOC Explorer** to search Indicators of Compromise from the OSINT feeds.

> Requires the `isms-core-threat-intel` container running with `VITE_THREAT_INTEL_ENABLED=true`.

**Filters:**

| Filter | Options |
|--------|---------|
| Type | IP / Domain / URL / MD5 / SHA1 / SHA256 |
| Source | CIRCL MISP / Botvrij MISP / AbuseIPDB |
| MITRE Technique | ATT&CK TID (e.g. T1190) |
| Tag | MISP event tag (e.g. `tlp:white`) |
| Search | Free-text IOC value search |

Each IOC row shows source, type, confidence, first/last seen, and associated ATT&CK techniques, malware family, and threat actor — all resolved at ingest time from MISP galaxy tags and Malpedia slugs.

### IP Enrichment

Go to **Intelligence → IP Enrichment** to look up any single IP address on demand.

Enter an IP address and the platform queries two sources in parallel:

**AbuseIPDB** (requires `ABUSEIPDB_API_KEY`):
- Abuse confidence score (0–100)
- Total report count and last reported timestamp
- Usage type and abuse categories

**Shodan** — if `SHODAN_API_KEY` is set:
- Open ports and service banners
- Hostnames and ASN/organisation
- CVEs detected on the host
- Last scan date

If no Shodan API key is configured, the free **Shodan InternetDB** fallback is used (open ports, CPEs, tags, CVE list — no account needed). If the IP is not indexed in Shodan (transit IPs, RFC1918 ranges), the widget shows "IP not indexed" rather than an error.

Enrichment results are cached for 24 hours. The cache resets automatically per IP.

### Malware Atlas

Go to **Intelligence → Malware Atlas** for the Malpedia-sourced malware and threat actor knowledge base.

> Requires the `isms-core-threat-intel` container. No API key needed — data sourced from the MISP galaxy open dataset.

**Malware Families tab:**
- Family name, aliases, description
- ATT&CK techniques associated with this malware
- Threat actor groups known to use it

**Threat Actors tab:**
- Actor name and aliases
- Country attribution (suspected state-sponsored origin)
- Motivation (espionage / financial / hacktivism / unknown)

Use the Malware Atlas to pivot from an IOC → malware family → actor → ATT&CK techniques, providing the "who and how" context for any indicator seen in your environment.

### KEV Audit Report (A.8.8)

The KEV Audit Report supports compliance evidence for ISO 27001:2022 **A.8.8 — Management of technical vulnerabilities**.

1. Go to **Intelligence → Threat Feeds**.
2. Scroll to the **A.8.8 KEV Audit Report** section.
3. Select the review window (3 / 6 / 12 months).
4. The report shows:
   - Total KEV entries in the window
   - Breakdown by remediation status (Patched / Overdue / Unscored)
   - Per-vendor summary
   - Full CVE list with CVSS score, EPSS score, exploitation notes, and due date
5. Click **Export CSV** to download the report for audit evidence.

### Enabling CPE Option B (admin toggle)

CPE Option B queries the NVD CPE API for KEV vendor/product names and indexes ~3-5K additional CPE entries. It can be toggled without editing `.env` or restarting containers:

1. Go to **Intelligence → Threat Feeds**.
2. Scroll to the **Feed Settings** panel (visible to Admins only).
3. Toggle **NVD CPE Option B (KEV-vendor)** on or off.
4. The change takes effect on the next scheduled CPE run (Sunday 01:30 UTC).

> The toggle stores the setting in the platform database and overrides the `FEEDS_CPE_FULL` environment variable.

### Configuring feeds

| Variable | Required for |
|----------|-------------|
| `NIST_API_KEY` | Faster NVD seeding (free key at nvd.nist.gov) |
| `ABUSEIPDB_API_KEY` | AbuseIPDB blacklist + IP enrichment |
| `SHODAN_API_KEY` | Shodan paid enrichment (InternetDB free fallback used if absent) |
| `TI_MISP_IMPORT_FROM_DATE` | MISP first-run date floor (default `2024-01-01`) |

The first NVD full run indexes ~250,000 CVEs into OpenSearch — this takes several hours without an API key.

---

## Risk Register {#risk-register}

The Risk Register implements ISO 27001:2022 Clause 6.1.2 — risk identification, analysis, evaluation, and treatment.

### Risk model

Each risk has:
- **Scenario** — description of the threat and asset
- **Probability** (1–5) — likelihood of occurrence
- **Impact** (1–5) — potential damage if it occurs
- **Risk Score** — Probability × Impact (1–25)
- **Risk Level** — Critical (20–25) / High (12–19) / Medium (6–11) / Low (1–5)
- **Treatment** — Mitigate / Accept / Transfer / Avoid
- **Linked controls** — ISO 27001 controls that address this risk
- **Residual score** — score after controls are applied

### Risk heatmap

The 5×5 heatmap gives a visual portfolio view. Risks are plotted by probability (Y-axis) and impact (X-axis). Click any cell to see the risks in that zone.

### Creating a risk

1. Go to **Risk Register** in the sidebar.
2. Click **New Risk**.
3. Fill in the scenario, asset, threat actor, and probability/impact scores.
4. Link relevant ISO 27001 controls.
5. Select a treatment and assign an owner.
6. Click **Save**.

### Risk treatment workflow

| Treatment | Meaning |
|-----------|---------|
| **Mitigate** | Implement or strengthen controls to reduce the score |
| **Accept** | Formally accept the risk (requires sign-off) |
| **Transfer** | Transfer to a third party (insurance, contract) |
| **Avoid** | Eliminate the activity that creates the risk |

For **Mitigate** — link a remediation plan (see Gap Tracking).  
For **Accept** — enter the authorising manager name and acceptance expiry date.  
For **Transfer** — document the transfer mechanism (insurer name, contract reference).

### ITSM push

Risks with treatment **Mitigate** can be pushed as tickets to Jira or ServiceNow:

1. Open a risk.
2. Click **Push to ITSM**.
3. Select the connector (Jira project or ServiceNow queue).
4. A ticket is created and linked back to the risk record.

---

## EBIOS RM {#ebios-rm}

EBIOS RM (Expression des Besoins et Identification des Objectifs de Sécurité — Risk Manager) is the French national risk methodology (ANSSI). ISMS CORE implements the full 5-workshop structure.

### When to use EBIOS RM

EBIOS RM is required for French public sector organisations and recommended for any organisation seeking ANSSI certification or operating in critical infrastructure sectors in France.

### The 5 workshops

| Workshop | Purpose |
|----------|---------|
| **1 — Scope & Security Baseline** | Define the study perimeter, supporting assets, feared events |
| **2 — Risk Sources** | Identify threat actors, their motivation and capability |
| **3 — Strategic Scenarios** | Map risk sources to feared events via attack paths |
| **4 — Operational Scenarios** | Detail technical attack paths (kill chains) |
| **5 — Risk Treatment** | Define security measures and residual risk |

### Running an EBIOS RM study

1. Go to **EBIOS RM** in the sidebar.
2. Click **New Study**.
3. Enter the study name, scope, and organisation context.
4. Work through workshops 1–5 sequentially — each workshop builds on the previous.
5. Workshop 5 generates a set of security measures that link back to your ISO 27001 controls and Risk Register.

> Each workshop auto-saves. You can pause and resume at any time.

---

## Business Impact Analysis {#business-impact-analysis}

The BIA module supports ISO 27001:2022 controls A.5.29 (Business continuity planning) and A.5.30 (ICT readiness for business continuity).

### Key concepts

| Term | Definition |
|------|-----------|
| **RTO** | Recovery Time Objective — maximum tolerable downtime |
| **RPO** | Recovery Point Objective — maximum tolerable data loss |
| **MTPD** | Maximum Tolerable Period of Disruption |
| **Business Function** | A critical process or service the organisation depends on |

### Creating a BIA

1. Go to **BIA** in the sidebar.
2. Click **New BIA**.
3. Define the scope (specific system, department, or organisation-wide).
4. Add business functions — for each, set:
   - Criticality (Critical / Important / Normal)
   - RTO target
   - RPO target
   - Supporting IT assets
   - Dependencies on other functions
5. Analyse impact over time horizons (1h, 4h, 24h, 72h, 7 days).
6. Generate the BIA report.

---

## Third-Party Risk Management {#third-party-risk-management}

The TPRM module tracks vendor and supplier risk, aligned with ISO 27001:2022 A.5.19–A.5.22 and DORA ICT third-party requirements.

### Vendor risk tiers

| Tier | Definition |
|------|-----------|
| **Critical** | Has direct access to your systems or processes critical data |
| **High** | Provides important services; breach would cause significant disruption |
| **Medium** | Standard supplier; limited access |
| **Low** | No access to systems or data |

### Adding a vendor

1. Go to **TPRM** in the sidebar.
2. Click **New Vendor**.
3. Enter the vendor name, service description, and tier.
4. Complete the DORA ICT fields if applicable (contract reference, sub-outsourcing details, exit plan).
5. Set the next review date.
6. Click **Save**.

### Vendor assessments

For each vendor you can attach:
- Due diligence questionnaires
- Security certifications (ISO 27001, SOC 2, etc.)
- Penetration test results
- Contractual clauses

Set a review frequency — the platform notifies you when a vendor review is due.

---

## Crosswalk & Framework Mapping {#crosswalk-framework-mapping}

The Crosswalk engine automatically maps your ISO 27001:2022 controls to other frameworks using a database of 3,980 pre-built mappings.

### How it works

When you implement an ISO 27001 control, the crosswalk engine infers coverage in mapped frameworks. For example:

- Implementing **A.8.8** (Management of technical vulnerabilities) automatically infers partial coverage of **NIS2 Article 21(e)**, **DORA Article 9**, and **CIS Control 7**.

### Viewing the coverage map

1. Go to **Crosswalk** in the sidebar.
2. Select the source framework (ISO 27001:2022) and the target framework.
3. The coverage matrix shows which target controls are covered, partially covered, or not covered by your current implementation.

### Using crosswalk in assessments

When running a compliance assessment for a framework like NIS2:

- Controls already covered by your ISO 27001 implementation are pre-populated.
- You only need to review and confirm the inferred coverage.
- Gaps in the target framework that are not covered by ISO 27001 are flagged separately.

### Control Dependency Graph

The **Dependency Graph** (available under **Analytics → Control Graph**) shows the 229 intra-ISO-27001 relationships — which controls depend on, enable, or feed into others.

Use this to:
- Understand the order of implementation (implement dependencies first)
- Assess the blast radius of a gap (which controls are blocked by this gap)
- Plan your implementation roadmap

---

## Metrics & KPI Dashboard {#metrics-kpi-dashboard}

The Metrics module tracks 9 security KPIs with trend history.

### Available KPIs

| KPI | Description |
|-----|-------------|
| **Audit Readiness Score** | Composite readiness score (0–100%) |
| **Control Coverage** | % of controls with implemented status |
| **Mean Time to Remediate** | Average days from gap creation to closure |
| **Open Critical Gaps** | Count of critical-severity open gaps |
| **Evidence Currency** | % of evidence items not expired |
| **Risk Score Average** | Mean residual risk score across all open risks |
| **Critical Risk Count** | Count of open risks at critical level |
| **Vendor Review Compliance** | % of vendors reviewed on schedule |
| **Assessment Completion** | % of active assessments fully scored |

### Sparkline trends

Each KPI shows a sparkline chart for the last 90 days. Trends are calculated from daily snapshots taken automatically at midnight.

### Portfolio view (Super Admin)

Super Admins can access **Metrics → Portfolio** to compare KPIs across all organisations on the platform. Useful for MSSP and multi-entity groups.

---

## Country Localisation {#country-localisation}

ISMS CORE generates jurisdiction-specific policies for 8 jurisdictions. When you set your organisation's country, all policy documents render with localised legal references, regulatory contacts, and terminology. Switzerland (CH) is the default — all source documents use Swiss references unless a country is set.

### Supported jurisdictions

| Code | Country | Key localised references |
|------|---------|--------------------------|
| **CH** | Switzerland (default) | nLPD, OPDo, PFPDT, FINMA, NCSC/BACS |
| **AT** | Austria | DSGVO, DSG, DSB, FMA |
| **BE** | Belgium | GDPR, RGPD, APD/GBA, CCB, CyberFundamentals |
| **DE** | Germany | DSGVO, BDSG, BSI, BaFin, LfDI |
| **FR** | France | RGPD, CNIL, ANSSI, LPM |
| **GB** | United Kingdom | UK GDPR, DPA 2018, ICO, FCA/PRA, NIS Regs 2018 |
| **IT** | Italy | GDPR, Garante, ACN |
| **LU** | Luxembourg | RGPD, CNPD, CSSF, CIRCABC |

### Setting your jurisdiction

1. Go to **Admin → Organisation Settings**.
2. Select your country from the **Jurisdiction** dropdown.
3. Click **Save**.

All policy documents immediately reflect the jurisdiction-specific tokens (regulatory body names, law references, terminology).

> **Note:** Changing jurisdiction does not alter the base control text — only the jurisdiction-specific tokens are replaced.

---

## AI Extension Pack {#ai-extension-pack}

The AI Extension Pack brings ISO 42001:2023 (AI Management System) and ISO 42005:2025 (AI Risk Assessment) into the platform as a fifth product family. It is designed for organisations that develop, deploy, or procure AI systems and need to demonstrate governance and risk management beyond their ISO 27001 ISMS.

### What It Covers

10 control groups across the ISO 42001:2023 Annex A domains:

| Group | Domain |
|-------|--------|
| AI-A.2 | AI Policy |
| AI-A.3 | Internal Organisation |
| AI-A.4 | Resources for AI Systems |
| AI-A.5 | Assessing Impacts of AI Systems |
| AI-A.6 | AI System Life Cycle |
| AI-A.7 | Data for AI Systems |
| AI-A.8 | Information for Interested Parties |
| AI-A.9 | Use of AI Systems |
| AI-A.10 | Third-Party and Customer Relationships |
| AI Foundation | AI-POL-00 + AI-POL-01 foundation policies |

Each group has: AI-POL policy, IMP-UG user implementation guide, IMP-TG technical implementation guide, SCR self-assessment checklist.

### AI Product Switcher

Switch to the AI product using the product switcher in the sidebar. The Control Library, Policies, Coverage, and Assessment pages update to show AI content.

### Crosswalk Coverage

ISO 42001 controls are crosswalked to:

| Target framework | Mappings |
|-----------------|---------|
| NIST AI RMF 1.0 | 32 mappings |
| EU AI Act | 31 mappings |
| OECD AI Principles | 14 mappings |
| ISO 42005:2025 | 5 mappings |

### ISO 42005:2025 Integration

ISO 42005:2025 (AI Risk Assessment) content is integrated into the AI implementation guides — the IMP-TG documents for AI-A.5 (Assessing Impacts) and AI-A.6 (Life Cycle) include ISO 42005 methodology and AISIA (AI System Impact Assessment) guidance.

### NIST AI RMF and EU AI Act Assessments

The AI Extension Pack activates two dedicated compliance assessment modules:

- **NIST AI RMF 1.0** — assess your AI governance against GOVERN, MAP, MEASURE, and MANAGE functions
- **EU AI Act** — assess compliance with high-risk AI system requirements across 6 groups

Both are available in the Compliance Assessments section when the AI product is active.

---

## Custom Frameworks {#custom-frameworks}

You can import your own control frameworks using a YAML template. This is useful for sector-specific requirements, internal control frameworks, or client-specific standards.

### YAML format

```yaml
framework:
  code: MY_FRAMEWORK
  name: My Internal Framework
  version: "1.0"
  controls:
    - id: MF-1.1
      title: Access Control Policy
      description: The organisation shall maintain a documented access control policy.
      iso_mappings:
        - A.5.15
        - A.8.2
    - id: MF-1.2
      title: Privileged Access Management
      description: Privileged accounts shall be reviewed quarterly.
      iso_mappings:
        - A.8.2
```

### Importing a framework

1. Go to **Frameworks → Custom Frameworks**.
2. Click **Import Framework**.
3. Upload your YAML file.
4. The platform validates the file and shows a preview.
5. Click **Confirm Import**.

The framework is now available in:
- Compliance Assessments (as a new assessment module)
- Crosswalk (as a target framework)
- QA Engine (as a reference option)

---

## Organisation & User Management {#organisation-user-management}

### User roles

| Role | Permissions |
|------|-------------|
| **Super Admin** | Full access to all organisations; platform administration |
| **Admin** | Manage users, connectors, org settings within their organisation |
| **ISMS Manager** | Full access to all projects, controls, gaps, risks, assessments |
| **Auditor** | Read-only access to all content; can export reports |
| **Control Owner** | Can update status and attach evidence for assigned controls |
| **Viewer** | Read-only access |

### Inviting a user (Admin)

1. Go to **Admin → Users**.
2. Click **Invite User**.
3. Enter the email address and select the role.
4. Click **Send Invitation**.

The user receives an email with a link to set their password. Invitation links expire after 48 hours.

### Deactivating a user

1. Go to **Admin → Users**.
2. Find the user and click **Edit**.
3. Toggle **Active** to off.
4. Click **Save**.

Deactivated users cannot log in. Their data and activity history are preserved.

### Notification preferences

Each user controls which email notifications they receive:

1. Click your name in the sidebar (bottom-left).
2. Go to **Profile & Settings → Notifications**.
3. Toggle each event type on or off.

| Event | Default | Description |
|-------|---------|-------------|
| **Gap assigned to me** | On | Email when a gap is assigned to you |
| **Evidence expiry alerts** | On | Warning when evidence items are approaching or past expiry |
| **QA check failures** | On | Summary email when a QA check finds failures |
| **Import completed** | On | Email when a data import finishes |
| **Feed pull failures** | On | Alert when a threat intelligence feed (MITRE, KEV, NVD) fails to pull |
| **Connector sync failures** | On | Alert when an evidence connector reports a sync error |

> **Note:** Email delivery requires `MAIL_HOST` to be configured in the deployment environment. If email is disabled, notifications are suppressed regardless of preferences.

### Multi-organisation (Super Admin)

Super Admins can manage multiple organisations from a single login:

1. Go to **Admin → Organisations**.
2. Click **New Organisation** to create a new tenant.
3. Assign an Admin to the organisation.
4. Switch between organisations using the org selector in the top bar.

Each organisation is fully isolated — users, data, connectors, and settings do not cross organisation boundaries.

---

## MFA & Account Security {#mfa-account-security}

### Enabling MFA

1. Go to your profile (click your name in the sidebar).
2. Click **Security → Enable Two-Factor Authentication**.
3. Scan the QR code with your authenticator app (Google Authenticator, Authy, 1Password, etc.).
4. Enter the 6-digit code to confirm setup.
5. **Save your backup codes** — displayed once. Store them securely. These are needed if you lose access to your authenticator.

### Logging in with MFA

1. Enter your email and password as normal.
2. On the MFA screen, enter the 6-digit code from your authenticator app.
3. The code is valid for 30 seconds — enter it promptly.

### Using a backup code

If you do not have access to your authenticator:

1. On the MFA screen, enter one of your 8-character backup codes (format: `XXXX-XXXX`).
2. Each backup code can only be used once.
3. After using a backup code, go to Security settings and generate a new set.

### Disabling MFA (Admin override)

If a user is locked out and has no backup codes:

1. Admin goes to **Admin → Users**.
2. Opens the user record.
3. Clicks **Reset MFA** — this clears their MFA configuration.
4. The user can then log in with password only and re-enrol MFA.

### Session security

- Sessions expire after 8 hours of inactivity.
- You can sign out from all devices via **Profile → Security → Sign Out Everywhere**.
- Admins can review active sessions in **Admin → Audit Log**.

### Audit log

All significant actions are recorded in the Audit Log (**Admin → Audit Log**):

- User logins and logouts
- Permission changes
- Data exports
- Configuration changes
- Failed authentication attempts

The audit log is read-only and cannot be modified. Entries are retained for 12 months.

---

*ISMS CORE User Guide — v1.0 · © 2026 ISMS CORE*  
*For technical documentation, see ARCHITECTURE.md. For deployment instructions, see the Administrator Guide.*
