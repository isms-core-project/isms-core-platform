# Changelog — ISMS CORE Platform

All notable changes to the ISMS CORE Platform (backend, frontend, connectors, feeds,
threat-intel, SMTP bridge) will be documented here.

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
