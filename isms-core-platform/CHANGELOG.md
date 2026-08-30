# Changelog — ISMS CORE Platform

All notable changes to the ISMS CORE Platform (backend, frontend, connectors, feeds,
threat-intel, SMTP bridge) will be documented here.

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
