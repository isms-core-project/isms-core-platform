# Changelog — ISMS CORE Platform

All notable changes to the ISMS CORE Platform (backend, frontend, connectors, feeds,
threat-intel, SMTP bridge) will be documented here.

## [1.3] - 2026-10-18 — the "Veridis Quo Release"

Write-ups: [release overview](https://isms-core.com/blog/isms-core-v1-3-veridis-quo-release/),
[roles](https://isms-core.com/blog/isms-core-auditors-should-not-edit-what-they-audit/),
[OpenSearch TLS](https://isms-core.com/blog/isms-core-opensearch-real-tls/).

v1.3 changes who is allowed to do what (roles and access rights), lets one person work in several organisations, adds real TLS to the supporting services, brings a new connector for Nessus and a working one for Greenbone / GVM, and moves the third-party API keys from `.env` into the web interface.

It is a minor release, not a patch: the role changes alter what existing users can do, so read the **upgrade notes** and the role table before you pull the images. The images are the release; update `docker-compose.yml` and `.env.example` together with them.

### Highlights

- **Roles that mean something.** Auditors are read-only plus findings, control owners work only on the control groups assigned to them, and library-wide operations belong to the platform operator. A new help tab, *Roles & permissions*, documents all six roles.
- **One login, several organisations.** A consultant can be given access to further organisations with a role of their own in each.
- **Connector certificates: Fetch Certificate and Trust on every connector.** Appliances with a self-signed or internal-CA certificate are trusted from the web interface, and plain `http://` addresses are no longer accepted.
- **Scanner connectors:** Greenbone / GVM rewritten (it could not connect before), Nessus added, Tenable fixed, and scanners can run on a schedule or on demand.
- **Third-party API keys in the web interface** (Admin → API keys), encrypted, with an on/off switch per key.
- **Sign-in lockout per address** with an admin unlock, instead of locking a whole account for everybody.
- **Feed schedules you can change without a restart** (Schedule button on every feed card), and feeds no longer all re-run at every container start.
- **Claude AI QA that grades the right thing:** fewer false failures, the configured model, and replies that are no longer lost to model thinking.
- **TLS for OpenSearch, Garage, and optionally Redis and mail.**
- **MITRE ATT&CK v20**, repaired EU AI Act and ISO 42001 data, and Assessment Collections back in the interface.


### Roles and access rights

#### Write routes any logged-in user could call now have a role
- **NIST CSF profiles, ratings, import and delete** require ISMS_MANAGER or above (like the regulatory modules); the NIST CSF page is read-only for VIEWER, AUDITOR and CONTROL_OWNER.
- **Remediation actions: create** requires ISMS_MANAGER or above (update and delete already did).
- **ITSM push / sync (Jira, ServiceNow) and the report generators** require ISMS_MANAGER or above, because they use the organisation's stored credentials or run subprocesses.
- **Promoting connector evidence to an evidence record** is no longer available to VIEWER or AUDITOR.
- **AI chat, Compass analysis, IP enrichment and metric snapshots** are no longer available to the read-only VIEWER role.

#### AUDITOR is an audit role
- An auditor is **read-only plus findings**: it can no longer create, edit or delete assessments, evidence, projects, BIA, EBIOS, CSRM, collections, risks or gaps. It can still read everything in its organisation, open documents in a read-only viewer, and **raise findings**. *Behaviour change: anyone using AUDITOR as a general editing role must be given CONTROL_OWNER or ISMS_MANAGER.*
- An auditor can **accept or flag evidence** (a flag needs a comment). The review is shown next to the item ("Audit: accepted / flagged"), recorded in the audit log, independent of the manager's approve / reject, and visible only to auditors and the platform operator for their own organisation.
- Fourteen pages now show each role only the controls it can use (no more buttons that answer 403), and the document editor has a read-only mode.

#### CONTROL_OWNER is scoped to assigned control groups
- A control owner creates and changes evidence, gaps, assessment items and remediation actions **only for the control groups assigned to them** (new picker in Admin → Users). Without an assignment the role is effectively read-only.
- Project structure, BIA, EBIOS, CSRM, collections, risk creation and creating or deleting assessments are ISMS_MANAGER-and-above work.
- Admin, QA and Generators pages redirect users whose role cannot use them instead of showing pages full of errors.

#### Platform-wide operations are for the platform operator (SUPER_ADMIN)
- Library-wide QA sweeps, QA synonym rules and keyword translations, the library "Full Sync", platform-wide diagnostics, and **editing generator definitions** (they are shared by every organisation). Organisation managers keep the per-project QA runs and can still list and run generators.
- Error text is no longer leaked to ordinary users: the health banner shows only "Feed 'x' failed"; administrators see a redacted reason; only the platform operator sees the raw upstream error.
- The SMTP test e-mail can only be sent to your own address and is rate limited.

#### One login, several organisations
- A person can be given access to additional organisations with a role of their own in each (and, for a control owner, their own control groups). An organisation switcher appears in the sidebar for people with more than one organisation; single-organisation installs see no change.
- Only a super administrator grants access (Admin → Users → "Access from other organisations"); the organisation's admin can change the role or remove the access, effective on the next request. Passwords, MFA and account status stay with the person's home organisation.
- New database table `organisation_memberships` (additive).
- **Fixed:** deleting a user or organisation failed with a server error once the user had ever signed in. Users can be deleted again; their audit entries remain, and the audit log stays otherwise unchangeable.

#### Tenant scoping and sessions
- An EBIOS measure can no longer point at another organisation's scenario, a NIST CSF profile can no longer be re-linked to another organisation's project, and evidence can only be linked to an assessment item of the same project. The status of a control group no longer mixes organisations. Dashboard counts are scoped to the caller's organisation.
- Resetting or deactivating a user also invalidates that user's already-issued access tokens. MFA backup-code regeneration is audit-logged. The "active project" can only be a project of the organisation you work in.


### Sign-in lockout per address, with admin unlock
- Failed sign-ins are counted per **account and source address**. Five wrong passwords from one address lock that address for that account only: five minutes, doubling up to fifteen (sixty for administrators). A locked address stops counting, so hammering it does not extend the lock.
- An account is locked **as a whole** only when failures arrive from many different addresses (eight or more within an hour), which is the pattern of credential stuffing. Before, anyone who knew an e-mail address could keep that person locked out for well over an hour.
- **Admin → Users → Locked sign-ins** lists current locks, with **Unlock** (one account and address), **Unblock IP** (that address for every account of the organisation) and **Unlock account**. Organisation admins see their own organisation, the platform operator sees all, only a super administrator can unlock a super administrator, and every unlock is written to the audit log.
- New database table `login_attempts` (automatic).


### Connectors

#### Certificates: Fetch Certificate and Trust, on every connector with an address
- Every connector that takes a URL or host has **Fetch Certificate** under the address field: it shows the certificate the target presents, you check the fingerprint and choose **Trust**, and from then on that one certificate is trusted for that connector (and the connector restarts). The same flow works for self-signed certificates and for certificates issued by an internal CA.
- A trusted certificate works **whatever name or address the host is reached by**, which matters for appliances normally reached by IP. A pinned single certificate is the only trust anchor and any other certificate is still refused; a pinned CA keeps the host-name check.
- **Pinned certificates issued by a CA now work on the connector image.** The image runs Python 3.12, which only accepts a pinned non-self-signed certificate as a trust anchor when asked to. HTTP clients, the Greenbone TLS context and the Active Directory / OpenLDAP clients all handle it now.
- The **Register** dialog trusts the fetched certificate straight away (checkbox, on by default). Before, only Configure could trust, so a freshly registered connector had no pin. Fetch Certificate probes the service's own port when none is typed (Nessus 8834, GVM 9390, LDAP 636).
- All 33 connectors that have Fetch Certificate carry the same **Verify SSL** switch in the same place. Trust comes only from a certificate trusted through Fetch Certificate, and verification can be disabled only by the operator's environment variable, never from the web interface.
- **Active Directory and OpenLDAP:** LDAPS certificate trust works as documented. A self-signed or internal-CA domain controller can be trusted with the certificate pinned in the web interface, the server box accepts `dc.corp.local:636` or `ldaps://dc.corp.local:636`, and the connector no longer accepts a CA file path from its remotely edited configuration. The LDAP connections are never sent in clear text (STARTTLS before the bind, or LDAPS).
- **Plain `http://` addresses are refused for every connector.** Credentials would travel unencrypted, and every appliance can serve HTTPS; keep `https://` and trust a self-signed certificate with Fetch Certificate. Nessus, Greenbone and Tenable.sc, which build the address from the host box, drop a typed `http://` and use https. *Behaviour change: a connector that still points at `http://` stops working until its address is changed.*

#### Scanner connectors
- **Greenbone / OpenVAS (GVM) is rewritten.** It used to call a REST interface that GVM does not have. It now speaks GMP (XML over TLS, port 9390) and reads each scan task's latest report: GVM's own per-class counts, the results with their CVEs, and the host count. A pasted web-interface address (`https://host:9392`) is mapped to 9390. The form's saved fields are read correctly. gvmd must listen on the network (see the connector notes).
- **Nessus connector added** (Professional, Expert and Essentials; port 8834; API keys): severity counts, the worst plugins with their CVEs and scores, the most affected hosts with their IP, scans and hosts reached. Evidence lands in the shared Tenable index. The scanner's licence data is never stored.
- **Tenable Vulnerability Management:** severity counts were always 0 (the API returns numbers, the connector compared words), so evidence always read "compliant". Fixed, plus an optional **Tenable URL** box (for example a government cloud).
- **Tenable Security Center:** the Host box accepts `host`, `host:port` or a pasted `https://` address; the row window is sent where the API reads it; optional username and password for versions before 5.13.
- Scanner names in the register picker say where they run: "Tenable Security Center (on-prem)", "Tenable Vulnerability Management (SaaS)", "Qualys VMDR (SaaS)".

#### Schedules
- **Scanner schedules:** Manual only (the default for scanners), or Daily, Weekly, Monthly, Quarterly or Bi-annual. **Sync now** wakes a manual connector, and a manual connector is no longer flagged as stale.
- **The interval chosen in the web interface is applied to every connector.** In worker mode it used to be ignored and each connector ran on its built-in default.
- **Feed schedules, changed from the web interface and live without a restart.** Every scheduled feed job (the threat-intelligence feeds and the vulnerability, MITRE, KEV, EPSS, EUVD and Exploit-DB feeds) has a **Schedule** button on its feed card. A Super Admin can set it to default, manual, an interval, daily at a chosen time, or weekly. A saved schedule is picked up by the feed scheduler at its daily re-check, or immediately through a resync, and the container is never restarted. Feeds that run several times a day (for example the MISP and ThreatFox feeds) are replaced by the one saved schedule, so no hidden extra run remains. Only the schedule is configurable here; switching a feed on or off stays an environment setting. New tables `feed_schedule_overrides` and `ti_schedule_overrides` (migration 096). Deleting an override that does not exist now answers 404 instead of a server error.
- **Feeds no longer all re-run at every container start.** `FEEDS_RUN_ON_START` now defaults to `false`: it forced every enabled feed to run again whenever the feeds container was recreated, which re-triggered the NVD full pull (about 400,000 records) on every redeploy. A feed that has never run is still seeded automatically. The weekly and daily feed times are documented in the user manual exactly as the scheduler runs them.

#### Other connector fixes
- **A connector that crashes while it is being created no longer restarts every few seconds forever.** A bad address (for example a Kubernetes Dashboard URL copied with its `#/…` part) used to crash on every refresh cycle, invisible in the admin interface because the connector did not exist yet to report it. The runner now reports such a crash to the platform, so it shows on the connector, and backs off exponentially (up to 30 minutes) while the same error repeats, retrying at once when the configuration changes.
- **Backend CPU spikes during connector polling are gone.** The key used to protect stored connector credentials was re-derived (a 600,000-iteration derivation) on every call; it is derived once per process now, with the same result and the same security.
- **PAN-OS, FortiGate and HashiCorp Vault connectors could never start from the worker** (the connector map named a class that did not exist). Fixed; a wrong name is now logged as an error. *Configured connectors of these three types start polling after the upgrade.*
- **A connector configured with an address but without its own credentials is refused** instead of silently using environment-held credentials against that address. An **empty** credential saved from the form counts as missing. The rule now covers 28 clients, including ServiceNow and Qualys.
- Credentials are no longer sent through HTTP redirects (a long list of clients and the keyed threat-intel feeds), and a target hostname that cannot be resolved is refused instead of being used unvalidated. Jira and ServiceNow requests go to exactly the addresses that were validated.
- **Form fields that were saved but never read** are fixed for Qualys, Zscaler, GLPI, Jira and SentinelOne.
- **Kubernetes connector:** the sample no longer tells you to use an admin service-account token; a read-only role sample is included.
- The GMP reply reader refuses an XML document type declaration before parsing.
- The SMTP bridge throttles wrong-password attempts per source and no longer freezes for other senders while a slow Microsoft Graph call runs.


### Third-party API keys in the web interface
- **Admin → API keys** (Super Admin only), in three tabs: **Vuln Feeds** (NIST NVD, VulnCheck), **TI Feeds** (AbuseIPDB, Shodan, IPinfo, MaxMind account id and licence key, ThreatFox, MalwareBazaar, AlienVault OTX, VirusTotal, GreyNoise) and **System** (Anthropic / Claude AI). One card per key with an **Enabled** switch, **Add / Replace key** and **Remove**.
- Saved values are write-only: never shown again, never in a response, log line or audit entry. The audit trail records which key changed and how.
- **Lookup order, per use, never cached:** a saved key whose switch is on wins; with the switch off, nothing saved, or the stored value unreadable, the matching `.env` variable is used. A rotated key applies on the next call, not the next restart. It is used by the AI assistant, Compass and Claude QA, the live IP look-ups, the NVD CVE / CPE and VulnCheck feeds, and the threat-intel feeds that take a key.
- **New secret `PLATFORM_KEY_ENCRYPTION_SECRET`** (backend, feeds and threat-intel only, never `SECRET_KEY`): at least 32 random characters, for example `openssl rand -hex 32`. It is required only to store keys in the web interface; without it the page says so and every `.env` key keeps working. Changing it makes saved keys unreadable (the `.env` fallback applies), so keep it with your backups.
- **New installations** enter keys on the page only. **Upgraded installations** have their `.env` keys imported **once**, at the first backend start with the secret set, as enabled rows marked "migrated from .env"; after that a key you remove is not brought back and a rotated key is not touched. Those `.env` lines can then be deleted.
- Not on the page on purpose: the session signing key, database, Redis and OpenSearch passwords and the trigger secrets (they protect the platform's own authentication and storage). Malpedia has no entry, because its feed needs no key.
- New database table `platform_api_keys` (automatic). Rebuild the feeds and threat-intel images (they gain the `cryptography` library).


### Transport security and hardening

#### OpenSearch with real TLS and a login (optional)
- With `OPENSEARCH_DISABLE_SECURITY=false` the platform brings its own certificate authority and one certificate per OpenSearch node and for Dashboards (the security plugin's public demo certificates are refused), encrypts REST and node-to-node traffic with host-name verification, lets only certified nodes join, and replaces the plugin's demo accounts with exactly two accounts, `admin` and `kibanaserver`, whose passwords come from `.env`. Dashboards is served over HTTPS with its own login.
- It is off by default (quick start), and the quick-start default is flagged loudly: a banner in `.env.example`, a warning from `bootstrap.sh`, and the install page say that no authentication and no TLS is for local evaluation only.
- OpenSearch TLS is always verified when TLS is on. To skip the check for an external OpenSearch you cannot validate, set `OPENSEARCH_ALLOW_UNVERIFIED_TLS=true` (logged).

#### Garage (S3 object store) is HTTPS-only
- Garage cannot do TLS itself, so a TLS proxy (`isms-core-garage-tls`) sits in front of its S3 and admin APIs, and Garage moved to a private network with no published ports. The OpenSearch snapshot plugin trusts the proxy's certificate. The Garage setup job also works on a brand-new install now.

#### Redis and mail over TLS (optional, both off by default)
- **`REDIS_TLS=true`:** the server certificate comes from the platform's own certificate authority, the plain port is closed, and the backend, worker and scheduler verify the certificate and still send the password.
- **`MAIL_REQUIRE_TLS=true`** (with `MAIL_CA_FILE` for a private CA): mail goes out only over verified TLS (STARTTLS, or implicit TLS on port 465). A relay that offers no TLS is refused, nothing is sent, and the credentials never leave in clear text. Leave it off for the bundled SMTP bridge and plain internal relays.

#### Containers and dependencies
- The application containers run with no Linux capabilities and no privilege escalation; PostgreSQL and Redis keep only the few capabilities their start-up needs. Own base images and the certificate-generation image are pinned by digest, and the optional Dashboards and Mailpit services no longer use `latest`.
- The Redis password is no longer visible in the process list; the OpenSearch URL can be set from `.env`. The frontend image installs dependencies with plain `npm ci`.
- The feeds and threat-intel containers can use their own trigger secrets (`FEEDS_TRIGGER_SECRET`, `TI_TRIGGER_SECRET`) instead of the connectors' shared secret.
- The background-task engine (Celery) is updated to 5.6.3. The semantic QA model is built into the backend image instead of being downloaded on first use (the image is about 450 MB larger).

#### Limits, validation and audit trail
- Rate limits and size caps on previously unbounded routes (model list, workbook generation, KPI metrics, QA result paging, connector ingest, the PDF parser); Compass and Claude QA runs are rate limited like the AI chat, and a rate-limited feature shows one readable message on every page.
- Out-of-range scores and unknown statuses answer 422 instead of a database error; PDF exports no longer fail on names containing `<` or `&`; invalid `project_id` values answer 422 instead of 500.
- The SSRF filter also rejects hostnames resolving into the carrier-grade-NAT range and Kubernetes cluster-local names.
- Audit trail for connector interval, rename and retention changes, platform-wide content loads, imports and re-indexing; a failed sign-in is recorded under the organisation of the account that was guessed.
- Generated spreadsheets can no longer be abused through names that start with `=`, `+`, `-` or `@`, and the workbook script runs with a minimal environment. Downloads of feeds and archives have size ceilings.


### AI features and Claude QA
- **The Claude semantic QA grades the control it is asked about.** The guidance for a whole product (for example the privacy or AI themes) was applied as a checklist to every single control group, so narrowly scoped controls failed for not reproducing content that correctly lives in another control group, and background ISO 22123 terminology was treated as a binding requirement. A full library sweep that produced 5 false failures and 32 warnings now ends with no failures and one real finding.
- **QA runs use the model selected in the admin interface**, not a fixed default. The library-wide sweep uses the newest model of the account, the project-scoped check uses the project's own organisation's selection.
- **Replies are no longer lost to model thinking.** Models that think before they answer put a thinking block first and used the same token budget as the answer; the reply was cut off before it started or could not be read. Text is now read by block type, these short structured tasks run with low reasoning effort, and the reply budget is larger; a response with no text block gives a readable error instead of a blank one.
- **A parse error is never stored as a result.** A failed reply used to be saved like a real score, and the "skip unchanged" shortcut then reused that failure forever.
- **"Full document text (no truncation)"** now also applies to the ISO requirement text, which was always cut to a few hundred characters.
- **Prompt caching** for the AI chat, Compass analysis and Claude QA: the static part of each prompt is cached, so multi-question sessions and sweeps read it again at a lower cost.

### Data and modules

- **MITRE ATT&CK updated to v20** (Enterprise): 706 active techniques (the 697 of v19 plus 9 new AI-related ones), 842 software entries, 178 groups and 57 campaigns, cross-checked against MITRE's release notes. A new ISO 27001 ↔ ATT&CK v20 axis has 45 mappings (the 36 existing direct mappings carried forward plus 9 new ones, each grounded in MITRE's own mitigation list); the v19 axis stays alongside. The weekly MITRE feed and the five MITRE pages (EN/DE/FR/IT) read v20, and the v19 data already stored is kept.
- **Threat Exposure keeps its NIST-based coverage with MITRE v20.** Its aggregation accepts both v19 and v20 crosswalk targets (the published NIST 800-53 ↔ ATT&CK mappings only exist for v19), so the 590 transitive mappings are not dropped and the 9 new v20 mappings are included. About 60 FINMA crosswalk mappings that had been missing were added, and duplicate FINMA rows from an earlier control-id change were removed.
- **EU AI Act crosswalk now loads.** The crosswalk pointed at control ids that the nine-article dataset no longer has, so every EU AI Act mapping was silently skipped. Mappings are re-pointed at the articles (30 from ISO 27001, 13 from ISO 42001, 7 from ISO 42005); mappings to articles outside the dataset were removed rather than guessed.
- **EU AI Act assessment** lists its 9 articles, and **CyberFundamentals (BE)** lists all 41 practices (it listed 12).
- **ISO 42001 control codes repaired:** the two life-cycle controls are `A.6.1.2-3` and `A.6.2.2-8` in every installation (an older edit was never picked up), which lets 47 more mappings load. The platform now holds **5,478 mappings on 86 axes** (4,632 on 60 axes in the core crosswalk, the ISO 42001 / ISO 42005 and country crosswalks, and 229 control dependencies); mappings that cited controls that do not exist were removed.
- **Updating a framework dataset keeps your assessments.** The loader used to delete every control of a framework whenever its content changed, and the ratings with them. It now updates in place and deletes only controls that left the standard. Thirteen framework datasets that were reloaded on every start now skip when unchanged, and dataset files that were removed from the image no longer linger in the data volume.
- **Assessment Collections are back in the interface:** Assessments → Collections lists, creates and deletes collections (open one to add assessments and export CSV, XLSX or PDF).
- **Cloud checklist generators run from the published repository**, internal folder names are gone from policy documents, and 44 broken links in the control lists are fixed. The public documentation was re-measured against the code (connectors 46, frameworks 42, 29 assessment modules).

### Content and dependencies
- **Documentation clean-up:** internal tooling references were removed from 203 implementation guides, the A.5.7 threat-intelligence assessment cites MITRE v20, a stale Sheet 5 formula description was corrected, and the A.8.35 guide now spells out its schema fields instead of pointing at a document auditors do not see.
- **Dependency updates:** the Angular packages were aligned to one version (this also clears two advisories in the development server's tooling, which never ship in the production build), `multidict` in the threat-intel image and the website's `source-map-js` and `sharp` were updated.

### Fixes
- Evidence: the **Approve** and **Reject** buttons did nothing (wrong HTTP method, answered 405). Fixed.
- **Help page:** the contents list stays in view and scrolls to sections, links inside the guide scroll instead of leaving the page, and the permission tables are real tables.
- An organisation Admin saw an endless spinner on the System page; now they get the cards they can use.
- **The browser refreshes an expired session again and keeps the selected organisation.** The refresh-and-replay after a 401 had never run (an injection-context error that the pages' own retry hid), and the replay dropped the organisation header. Organisation and project data is cleared from the browser when a session has expired.
- SIEM evidence no longer reports "compliant" when the alert fields could not be read; SIEM and threat-intel sync failures are reported to the platform.
- OpenSearch Dashboards: *Entra ID Entity Analytics* and *Microsoft Defender* count distinct objects instead of documents, and *Audit Logs — Top Users* no longer includes events with no user. Takes effect when `dashboards-setup` is rebuilt and re-run.


### What each role can do in v1.3

Measured on the running platform, route by route, against v1.2. "Changes" means the API routes that create, edit or delete something.

| Role | Reads | Changes | Compared with v1.2 |
|---|---|---|---|
| **VIEWER** | Everything in its organisation except administration, connector set-up and QA settings | Only its own account (password, MFA, notification settings) | **Loses 16 routes**: AI chat, Compass analysis, metric snapshots, report generators, NIST CSF edits, connector actions, remediation create, threat-intel actions — these were callable by any logged-in user |
| **AUDITOR** | As VIEWER | Raise findings, **accept / flag evidence**, AI chat, Compass analysis, IP enrichment, metric snapshots | **Loses 77 routes**: create / edit / delete of assessments, evidence, projects, BIA, EBIOS, CSRM, collections, risks, gaps, NIST, generators, connector actions. Gains the evidence review |
| **CONTROL_OWNER** | As VIEWER | Evidence, gaps, assessment items and remediation actions **of the control groups assigned to them**, plus AI chat / Compass / metric snapshots. Remediation actions: edit and (through the API) create within their groups; no deleting | **Loses 62 routes** (projects, BIA, EBIOS, CSRM, collections, risks, NIST, generators, connector actions, creating assessments). Anything outside the assigned groups is refused |
| **ISMS_MANAGER** | As VIEWER, plus per-project QA | Organisation content: projects, BIA, EBIOS, CSRM, collections, risks, vendors, assessments, evidence, gaps, remediation, regulatory modules, NIST CSF, per-project QA runs; may list and run generators | **Loses 7 routes** (library-wide QA sweeps and synonym rules, now SUPER_ADMIN) |
| **ADMIN** | Everything in its organisation, including administration | Everything a manager can, plus users and groups, connectors, organisation settings, custom frameworks, sign-in unlocks | **Loses 11 routes** (library-wide QA, the library "Full Sync", two platform-wide diagnostics, generator editing) |
| **SUPER_ADMIN** | Everything, all organisations | Everything, including platform-wide operations (feeds, library content, global QA, generator definitions, API keys, system) | Unchanged, plus API keys |

A person can additionally hold a role of their own in other organisations.


### Design choices that remain
- The SSRF filter allows private address ranges for Jira and ServiceNow URLs, because on-premises installations of both live there. Metadata addresses, cluster-local names and carrier-grade NAT ranges are refused.
- The `docker-socket-proxy` used by the backup tool runs with `POST=1` so backups can stop and start containers; it sits on an isolated network, in the `backup` profile only.


### Upgrade notes

**Before you upgrade**
- **Review who uses which role.** If anyone uses AUDITOR as a general editing role, give them CONTROL_OWNER or ISMS_MANAGER first. API clients or scripts that call write routes as VIEWER or AUDITOR will start receiving 403.
- **Every connector address must be `https://`.** Plain `http://` addresses are refused, including the SIEM and threat-intel (TAXII / MISP / JSON) connectors. A system with a self-signed certificate stays on `https://`; use **Fetch Certificate → Trust** once.
- **Copy the new `docker-compose.yml` and `.env.example`** and pull all images (rebuild feeds and threat-intel if you build yourself). The compose file carries the container hardening, the new secrets and a changed command for the scheduler (`beat`).

**Automatic at start-up**
- Database migrations: `096` (`feed_schedule_overrides`, `ti_schedule_overrides`), `097` (`organisation_memberships`), `098` (the audit log permits only the foreign-key detach when a user or organisation is deleted), `099` (`platform_api_keys`) and `100` (`login_attempts`). All are additive.
- Keys that are in `.env` are imported into Admin → API keys once, if `PLATFORM_KEY_ENCRYPTION_SECRET` is set.
- Dataset repairs (ISO 42001 codes, thirteen datasets get their first content hash, removed dataset files are cleaned up) are applied at the first start with the new data image.

**Behaviour change:** `FEEDS_RUN_ON_START` now defaults to `false` in `docker-compose.yml` and `.env.example`. If you relied on every feed running at each start, set it to `true` again (not recommended: it repeats the large NVD pull).

**New optional settings** (all documented in `.env.example`): `PLATFORM_KEY_ENCRYPTION_SECRET`, `REDIS_TLS`, `MAIL_REQUIRE_TLS`, `MAIL_CA_FILE`, `FEEDS_TRIGGER_SECRET`, `TI_TRIGGER_SECRET`, `OPENSEARCH_ALLOW_UNVERIFIED_TLS`, and the OpenSearch security block.

**Redis TLS (optional).** Set `REDIS_TLS=true` in `.env`, run `docker compose up -d isms-core-internal-certs-init` (adds the Redis certificate to the existing certificate authority), then recreate Redis, the backend, the worker and the scheduler together; the data is kept. Check that the worker logs `Connected to rediss://`.

**Garage (S3) moves to HTTPS** — read before upgrading an install that uses `--profile garage`. Existing snapshots and data are not touched. What changes: Garage is reachable only through the new HTTPS proxy `isms-core-garage-tls` (same host ports 3900 / 3903, now TLS), the OpenSearch nodes get a trust store and are recreated, and the snapshot repository is re-registered at the new address.
1. Copy the new `docker-compose.yml` **and the new file `garage/tls-proxy.conf`**.
2. In `.env` set `GARAGE_ENDPOINT=https://isms-core-garage-tls:3900` (or delete the line).
3. Pull the new `opensearch-setup` and `garage-setup` images.
4. Bring up the new pieces first: `docker compose up -d isms-core-internal-certs-init isms-core-garage isms-core-garage-tls`. Then recreate the OpenSearch nodes; on a 3-node cluster **one node at a time** (wait for `green` with 3 nodes between nodes), since a plain `docker compose up -d` recreates all three together and search is briefly unavailable. Finally `docker compose up -d` for everything else.
5. The `opensearch-setup` log must say "Snapshot repository registered" and "verified OK".
6. Check that `GET _cat/snapshots/garage-s3` still lists your earlier snapshots. Anything of yours that talked to Garage directly now has to use `https://…` and trust the certificate in the `isms-core-internal-certs` volume (`/certs/garage/server.crt`).
Rollback: put the old compose file and `.env` back and run the old `opensearch-setup` once; the snapshots in the bucket are unaffected.

**OpenSearch security (optional — only if you want TLS and a login)**
1. Copy the new `docker-compose.yml` and `.env.example`; pull the new `opensearch-setup` and `dashboards-setup` images.
2. In `.env`: `OPENSEARCH_DISABLE_SECURITY=false`, `OPENSEARCH_ADMIN_PASSWORD`, `OPENSEARCH_DASHBOARDS_PASSWORD`, `OPENSEARCH_URL=https://isms-core-opensearch:9200`, `OPENSEARCH_USERNAME=admin`, `OPENSEARCH_PASSWORD=<the admin password>`, `OPENSEARCH_USE_SSL=true`, `OPENSEARCH_VERIFY_CERTS=true`. Optional: `DASHBOARDS_TLS_EXTRA_SAN=DNS:your.name,IP:your.address`. **No dollar sign (`$`) in the passwords.**
3. `docker compose up -d isms-core-internal-certs-init`, then recreate **all OpenSearch nodes together** (turning security on is not possible one node at a time; expect a short outage, around half a minute), then the rest of the stack. Plain HTTP on port 9200 stops working at that moment.
4. Check that `https://localhost:9200/_cluster/health` with the admin account is green inside a node, that the demo accounts are refused, and that Dashboards opens on `https://<host>:5601`. The browser warns about the Dashboards certificate until the platform CA (`ca.crt`, folder `opensearch-ca` of the `isms-core-internal-certs` volume) is trusted.
5. The two passwords are read **once**, when the security plugin first initialises; change one later with the OpenSearch security API.
Rollback: set `OPENSEARCH_DISABLE_SECURITY=true`, put the plain `OPENSEARCH_URL` back and recreate all nodes together.

**After you upgrade**
- **The backend image is about 450 MB larger** (the semantic-QA model is inside it); nothing is downloaded at run time any more. To confirm the hardening: `docker exec isms-core-backend grep -E 'CapEff|NoNewPrivs' /proc/1/status` should show `CapEff: 0000000000000000` and `NoNewPrivs: 1`.
- **Recommended:** give the feeds and threat-intel containers their own secrets (`FEEDS_TRIGGER_SECRET` and `TI_TRIGGER_SECRET`, each a different random value) and recreate the stack. Until you do, they keep using `CONNECTORS_WORKER_SECRET`.
- **Assign control groups to every CONTROL_OWNER** (Admin → Users). Until then a control owner can read everything but cannot change anything.
- **PAN-OS, FortiGate and HashiCorp Vault connectors begin polling** if you had configured one. Check the credentials and the first run in Admin → Connectors. A scanner connector defaults to **Manual only**: choose a schedule or use Sync now.
- If an Active Directory connector relied on a `ca_cert_file` entry in its configuration, move that file to the connector container as `AD_CA_CERT_FILE` (or pin the certificate in the web interface).
- A connector configured with an address but without its own credentials is refused; re-enter the credentials in the connector settings if one stops syncing.
- The QA and Claude AI QA pages are visible to ISMS_MANAGER and above only; the library-wide QA sweeps, synonym rules, the library "Full Sync" and generator editing need SUPER_ADMIN.

### Verification
- **Roles and tenants:** every route's role gate was compared with what the running backend does, and cross-organisation access was attempted with real objects from a second organisation on every resource type: no gate mismatches and no cross-organisation leaks.
- **Browser:** both builds were built with `ng build --configuration=production` and clicked through as every role on every page: no failing calls and no script errors. The new pages were also driven against a mocked API.
- **Database:** every migration was rehearsed up, down and up on a copy before it ran on the production database.
- **Connectors:** certificate trust was tested on the connector image's own Python version with certificates issued by a CA and with self-signed ones, and a negative test proves an unrelated certificate is still refused on every path. The Greenbone and Nessus connectors were exercised against real scanners and produced real evidence.
- **Sign-in lockout, Redis TLS, mail TLS and the dataset loader** were tested against a real PostgreSQL, a real Redis and test mail relays, including the failure cases (wrong CA, wrong password, relay without TLS, a renamed control with ratings attached).
- **Images:** built from the final sources, deployed with all containers recreated, and the start-up logs of every container read.

## [1.2] - 2026-10-10
### Security & Hardening

VVAH shipped v1.5.0 — a rewrite of its detection backend around a code graph instead of
chunk-by-chunk reading — so we re-ran the full internal security review (backend, frontend,
and every connector/feed/threat-intel/SMTP-bridge service) against the new engine. See the
[blog write-up](https://isms-core.com/blog/isms-core-vvah-v15-rescan/) for the full breakdown.

**207 verified findings fixed, no exceptions:**
- Backend: 102 (0 Critical, 5 High, 77 Medium, 20 Low)
- Connectors / feeds / threat-intel / SMTP bridge: 99 (1 Critical, 13 High, 58 Medium, 27 Low)
- Frontend: 6 (0 Critical, 0 High, 4 Medium, 2 Low)

Highlights: 17 connectors where a config-supplied target host could pair with a secret still
held only in the environment, letting a config edit alone redirect real credentials to a
foreign host; 7 connectors still accepting cleartext `http://` despite otherwise-complete SSRF
target validation; 32 backend write routes with no role gate at all, now all running through
the same `require_not_viewer` dependency already proven everywhere else.

**Two older architectural gaps closed for real, not patched around:**
- Stateless JWT access tokens can now actually be revoked on logout (or admin force-revoke) via
  a per-user token-epoch counter checked on every request, at no added per-request database cost
- DNS-rebinding against connector targets is fully closed, not just narrowed: a validated
  hostname's resolved address is pinned for the life of the connector process, closing the gap
  between "we checked this host once" and "we're still talking to the same host now"

**Internal Postgres TLS and a connector-identity redesign**, both shipped the same evening after
being deliberately deferred mid-sweep rather than rushed:
- Postgres now runs real TLS by default — a self-signed certificate generated once on first boot,
  fail-closed client verification (refuses to connect rather than silently fall back to
  plaintext), with a logged, explicit opt-out for operators who genuinely need one
- The connectors runner previously authenticated every per-connector API call with one shared
  secret plus a client-supplied connector-ID header, trusted outright — any connector could
  impersonate any other connector to the backend. Every connector now gets its own bearer token;
  the shared secret's only remaining job is the one bootstrap call that hands those out. Verified
  against the real API: the old exploit path (shared secret + an arbitrary connector ID) now gets
  rejected where it used to succeed.

Also fixed along the way: a live middleware bug (a decorator had landed on the wrong function,
which would have 500'd every request in production — caught only because a real HTTP request was
dispatched against it, not just a build/syntax check); the backup volume image pinned to a real
version tag; the frontend container now runs non-root on an unprivileged port with security
headers and a working healthcheck; three deploy-time regressions found and fixed by watching real
production logs after redeploy rather than assuming a clean build meant a clean deploy; five freshly-
disclosed CVEs against pre-existing dependencies (`proxy-addr`, `@modelcontextprotocol/sdk`,
`source-map-js`, `sharp`, `multidict`) patched and re-verified with real builds and installs.

## [1.1] - 2026-08-30
### Security & Hardening

A full internal security review across the backend, frontend, and every connector/feed/
threat-intel/SMTP-bridge service, using [Visa's open-source Vulnerability Agentic Harness
(VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness) — an agentic SAST
pipeline that threat-models the codebase, decomposes the call graph, and runs every
finding through an independent adversarial-verification pass before it's reported. See
the [blog write-up](https://isms-core.com/blog/isms-core-vvah-security-sweep/) for the
full breakdown.

**141 verified findings fixed, no exceptions:**
- Backend: 50 (7 Critical, 17 High, 21 Medium, 5 Low)
- Frontend: 24 (1 Critical, 4 High, 11 Medium, 8 Low)
- Connectors / feeds / threat-intel / SMTP bridge: 67 (9 Critical, 26 High, 23 Medium, 9 Low)

Highlights: tenant-isolation authorisation gaps closed across multiple root causes;
template-injection and path-traversal remote-code-execution paths closed; MFA secrets
and backup codes moved to proper encryption/hashing at rest; every connector's TLS
verification setting now reads from the local environment only, never from remote
config; SSRF closed across every connector and feed that follows a server-supplied
pagination URL; both on-demand feed trigger servers now require the shared worker
secret they already had sitting unused; hash-pinned (`--require-hashes`) Python
dependencies across all connector images; non-root containers across the board.

Also fixed along the way, unrelated to the security review itself: a missing
`connectors/base/__init__.py` that was silently breaking connector startup in the
default deployment shape (see the [companion post](https://isms-core.com/blog/isms-core-connectors-init-py-bug/));
an Active Directory password-policy compliance check that silently passed domains
with unlimited password age; a threat-intel feed scheduler indentation bug that
disabled VirusTotal enrichment whenever AlienVault OTX was turned off; a cancel-flag
key mismatch that made the ENISA EUVD feed uncancellable from the trigger API.

### Full findings
See [SECURITY.md](../SECURITY.md) for the vulnerability disclosure policy this review
was run under internally, ahead of any external report.

---

## [1.0] - 2026-08-04
### Launch
- Ten-service Docker Compose stack: FastAPI backend, Angular frontend, PostgreSQL,
  Redis, OpenSearch, Celery worker/beat, nginx, vulnerability feeds, threat intelligence
- 44 native connectors across identity, cloud, network, and SIEM systems
- 29 compliance assessment modules, 4,671 crosswalk objects across 59 axes
- 8 country jurisdiction configurations
- 21+ live threat intelligence feed sources

---

*Where bamboo antennas actually work.* 🎋
