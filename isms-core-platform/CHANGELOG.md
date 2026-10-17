# Changelog — ISMS CORE Platform

All notable changes to the ISMS CORE Platform (backend, frontend, connectors, feeds,
threat-intel, SMTP bridge) will be documented here.

## [1.3] - 2026-10-16 — the "Veridis Quo Release"

Why a minor release: v1.3 changes who is allowed to do what, and adds one data-model table (organisation
memberships). Read the upgrade notes before pulling the new images. Write-ups:
[release overview](https://isms-core.com/blog/isms-core-v1-3-veridis-quo-release/),
[roles](https://isms-core.com/blog/isms-core-auditors-should-not-edit-what-they-audit/),
[OpenSearch TLS](https://isms-core.com/blog/isms-core-opensearch-real-tls/).

### Roles and access rights
- **Auditor is an audit role: read-only plus findings.** It can raise gaps and **accept or flag evidence** (a flag needs a comment; recorded in the
  audit log, independent of the manager's approve / reject), and can no longer create, edit or delete the records it audits.
- **Control Owner is scoped to the control groups assigned to them** (new picker in Admin → Users). Without an assignment the role is read-only.
- **Viewer is read-only** (16 routes any logged-in user could call are now refused); **library-wide operations** (global QA sweeps, synonym rules,
  "Full Sync", platform diagnostics) are for the Super Admin. The interface shows each role only what it can use.
- Measured on the running platform, route by route (405 routes), with a cross-organisation test (142 routes, 0 leaks). Help → "Roles & permissions"
  lists what each role can do.

### One login, several organisations
- A Super Admin can give an existing account access to further organisations, each with its own role and control groups. A switcher appears in the
  sidebar. Password, MFA and account status stay with the home organisation. Single-organisation installs see no change.
- Fixed: deleting a user (or organisation) who had ever logged in failed with a server error; the Approve / Reject buttons on evidence did nothing.

### Transport security and hardening
- **OpenSearch with real TLS and a login (optional, off in the quick-start default).** The platform creates its own certificate authority and one
  certificate per node, encrypts REST and node-to-node traffic with hostname checking, lets only certified nodes join, replaces the security plugin's
  public demo accounts with exactly two (`admin`, `kibanaserver`) whose passwords come from `.env`, and serves OpenSearch Dashboards over HTTPS with a login.
- **Garage (S3) is HTTPS-only** behind a TLS proxy, on a private network with no published ports.
- Application containers drop all Linux capabilities and cannot gain new ones; base images are pinned by digest; LDAPS connectors honour the
  certificate pinned in the WebUI; Jira / ServiceNow requests are bound to the validated address; Celery 5.6.3.
- The semantic-QA model is now inside the backend image (about 450 MB larger; nothing is downloaded at first use).

### Threat intelligence — MITRE ATT&CK v20
- **MITRE ATT&CK updated to v20** (Enterprise matrix, released by MITRE 2026-10-13): 706 active techniques (the 697 of v19 plus 9 new AI-related ones), 842 software entries, 178 groups, 57 campaigns, checked against MITRE's own release notes. The weekly feed and the MITRE pages now read v20; the stored v19 data is kept.
- **Crosswalk:** a new ISO 27001 ↔ ATT&CK v20 axis with 45 mappings (the 36 existing direct mappings carried forward plus 9 new ones taken from each new technique's official MITRE mitigations). The v19 axis stays alongside, unchanged. The NIST 800-53 ↔ ATT&CK route is not extended to the 9 new techniques yet: the Center for Threat-Informed Defense has not published v20-aligned mappings.

### Upgrade notes
- **Before:** anyone using Auditor as a general editing role must be given Control Owner or ISMS Manager. API clients that call write routes as
  Viewer or Auditor will receive 403. SIEM and TAXII / MISP / JSON threat-intel sources must use `https://`.
- **Automatic:** database migration 097 (new table `organisation_memberships`, additive) and 098 (audit-log trigger permits only the
  foreign-key detach when a user is deleted).
- **Garage:** copy the new `docker-compose.yml` and `garage/tls-proxy.conf`, set `GARAGE_ENDPOINT=https://isms-core-garage-tls:3900` (or delete the line),
  pull the new `opensearch-setup` and `garage-setup` images; existing data and snapshots are untouched.
- **OpenSearch security (optional):** follow the OpenSearch block in `.env.example` (`OPENSEARCH_DISABLE_SECURITY=false`, admin and Dashboards passwords,
  `OPENSEARCH_URL=https://isms-core-opensearch:9200`, TLS and certificate checking on; no `$` in the passwords). Turning it on or off needs a full restart
  of all OpenSearch nodes together (about half a minute in testing); existing data is kept. The browser warns about the Dashboards certificate until the
  platform CA is trusted.
- Update `docker-compose.yml` along with the images and recreate the stack.

## Also in v1.3 — added on 2026-10-17, before the public release

Scanner connectors, certificate trust, third-party API keys in the WebUI, and the fixes from the final security re-scan of v1.3.

#### Third-party API keys in the WebUI
- **Admin → API keys** (Super Admin only), in three tabs — *Vuln Feeds* (NIST NVD, VulnCheck), *TI Feeds* (AbuseIPDB, Shodan, IPinfo, MaxMind, ThreatFox, MalwareBazaar, AlienVault OTX, VirusTotal, GreyNoise) and *System* (Anthropic / Claude AI). Each key has an **Enabled** switch; saved values are stored encrypted and never shown again. A key saved there takes effect at the next feed run or request, no restart.
- **New installations** enter their keys on the page; nothing needs to go into `.env`. **Upgraded installations** have the keys already in `.env` imported into the page once, automatically (enabled; shown as *Migrated from .env*); those lines can then be deleted. Until they are, a key that is switched off or removed on the page still falls back to its `.env` value.
- **New secret `PLATFORM_KEY_ENCRYPTION_SECRET`** (at least 32 random characters; only the backend, feeds and threat-intel containers get it, never `SECRET_KEY`). Without it the page refuses to save and keys in `.env` keep working. Changing it later makes stored keys unreadable (the `.env` value then applies) — keep it with your backups.
- Database migration 099 (new table `platform_api_keys`, automatic). The feeds and threat-intel images now include the `cryptography` library. Malpedia has no key (its feed uses the public API).

#### Connectors
- **OpenVAS / Greenbone is rewritten** for GVM's own management protocol (GMP, port 9390): scan tasks, results with CVEs, host count; tested against a real GVM 22.7. The previous connector called a REST API that GVM does not have and never produced data. gvmd must be set to listen on the network.
- **Nessus connector added** (Professional / Expert / Essentials, API keys): severity counts, worst plugins with CVEs and scores, most affected hosts, scans. Tested against a real Nessus Essentials. The platform now has **46 connectors**.
- **Tenable Vulnerability Management:** every severity count read 0 (the API returns numbers, the connector compared words); fixed, plus an optional Tenable URL for other Tenable clouds. **Tenable Security Center:** host box accepts `host`, `host:port` or a pasted URL.
- **Scanner schedules:** vulnerability scanners default to **Manual only** (run with *Sync now*) and can be scheduled Daily, Weekly, Monthly, Quarterly or Bi-annual. Fixed for all connectors: the interval chosen in the WebUI was ignored by the connector runner.
- **Certificate trust:** every connector with a URL or host has **Fetch Certificate** (review the fingerprint, then Trust) and the same **Verify SSL** switch; the Register dialog can trust the fetched certificate straight away. A pinned certificate now works for self-signed *and* CA-issued appliance certificates (Nessus, GVM, domain controllers) whatever name or IP the host is reached by; a different certificate is still refused. Fetch Certificate reads the service's own port when none is typed (Nessus 8834, GVM 9390, LDAPS 636). Fixed: SIEM ignored a pinned certificate.
- Form fields that were saved but never read are fixed for Qualys, Zscaler, GLPI, Jira and SentinelOne. Scanner names in the picker: *Tenable Security Center (on-prem)*, *Tenable Vulnerability Management (SaaS)*, *Qualys VMDR (SaaS)*.

#### Data and module fixes
- **EU AI Act crosswalk now loads** (30 ISO 27001, 13 ISO 42001 and 7 ISO 42005 mappings to the nine articles). Before, the crosswalk pointed at control ids the EU AI Act dataset no longer has, so every EU AI Act mapping was silently skipped. 85 further mappings that cited ISO 27701 clauses or an ISO 42001 control that does not exist were removed — they never loaded. The four crosswalk files now hold **5,249** mappings on 85 axes, all of which load.
- **Removed datasets no longer linger after an upgrade:** the data job now deletes dataset files that are not in the new image before copying, instead of loading an old and a new file for the same framework on every start.
- **Updating a framework dataset keeps your assessments:** the loader used to delete all controls of a framework when its content changed, taking the ratings with them; it now updates in place and removes only controls that left the standard.
- **ISO 42001 control codes repaired:** the two life-cycle controls are now `A.6.1.2-3` and `A.6.2.2-8` in every installation (an older edit was never picked up), which lets 47 more crosswalk mappings load — 5,478 mappings on 86 axes in total, including 229 control dependencies.
- **EU AI Act assessment** lists its 9 articles; **CyberFundamentals (BE)** lists all 41 practices (it showed 12).
- **Assessment Collections** can be listed, created and deleted again (*Assessments → Collections*).
- The **Cloud checklist generators** run from the published repository.

#### Security and behaviour changes
- **Generator definitions are edited by the Super Admin only** (they are shared by every organisation); listing and generating stay with ISMS Manager and above.
- **OpenSearch TLS is always verified when TLS is on.** For an external OpenSearch you cannot validate, `OPENSEARCH_ALLOW_UNVERIFIED_TLS=true` skips the check (logged).
- A control group's status no longer mixes organisations; Compass and Claude QA runs are rate limited; connector, feed and threat-intel calls that carry credentials no longer follow redirects; a configured host can no longer be paired with credentials held in the environment (cisco-ise, netbox, openvas); sheet names written into generated workbooks cannot act as formulas; audit-trail entries for failed logins and cross-organisation admin actions are recorded under the right organisation.
- Dashboards: *Entra ID Entity Analytics* and *Microsoft Defender* count distinct objects instead of documents; *Audit Logs — Top Users* no longer counts system events.
- **Final security round (2026-10-17):** an empty credential saved from the WebUI form can no longer pair a configured host with credentials held in the environment (28 connector clients now treat an empty value as missing; ServiceNow and Qualys gained the guard); the OpenVAS/GVM reply reader refuses an XML document type declaration before parsing and parses each reply once; the browser now really refreshes an expired sign-in and replays the request **in the organisation you selected** (the refresh step never ran before — the pages' own retry hid it — and the replay would have dropped the organisation header).
- **Sign-in lockout is per (account, address)** (migration 100): five wrong passwords from one address lock that address for that account only (5 minutes, doubling to 15; 60 for administrators). An account is locked as a whole only when wrong passwords arrive from many different addresses. Admins see and clear locks on **Admin → Users → Locked sign-ins** (Unlock, Unblock IP, Unlock account); every unlock is audited. Before, anyone who knew an e-mail address could keep that account locked for 40–80 minutes.
- **Optional TLS for Redis (`REDIS_TLS=true`) and for mail (`MAIL_REQUIRE_TLS=true`)**, both off by default — see PLATFORM.md, *Encrypted Redis and mail*.
- **Connectors refuse plain `http://` addresses.** A system with a self-signed certificate stays on `https://`: use Fetch Certificate → Trust. A connector that still points at `http://` stops working until its address is changed.

#### Upgrade notes for these additions
- Migration 100 (table `login_attempts`) runs automatically. `REDIS_TLS`, `MAIL_REQUIRE_TLS` and `MAIL_CA_FILE` are new optional `.env` keys (see `.env.example`); copy the new `docker-compose.yml` with the images.
- Check connectors that use `http://` addresses before upgrading: change them to `https://` (trust a self-signed certificate once with Fetch Certificate → Trust).
- Add `PLATFORM_KEY_ENCRYPTION_SECRET` to `.env`, copy the new `docker-compose.yml`, pull the images and recreate the stack. Migration 099 runs automatically; keys already in `.env` are imported once on the first start.
- Scanner connectors you configured before this release: re-open them, use **Fetch Certificate → Trust** once, and pick a schedule (scanners now default to Manual only).

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
