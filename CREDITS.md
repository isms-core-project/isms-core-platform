# Credits & Acknowledgements

The connector architecture, asynchronous worker patterns (Celery beat/worker split),
service topology, and Docker Compose structure in ISMS CORE draw from production-grade
patterns established by [Filigran](https://filigran.io) and their open-source projects:

- **OpenCTI** — [https://github.com/OpenCTI-Platform/docker](https://github.com/OpenCTI-Platform/docker)
- **OpenAEV** — [https://github.com/OpenAEV-Platform/docker](https://github.com/OpenAEV-Platform/docker)

These implementations saved significant engineering time and provided a battle-tested
foundation for the ISMS CORE platform.

## Security tooling

The ISMS CORE Platform's security hardening passes (backend, frontend, and every
connector/feed/threat-intel/SMTP-bridge service — v1.1 and the v1.5.0 re-scan that landed
in v1.2) were carried out using [Visa's Vulnerability Agentic Harness
(VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness), an open-source,
Apache-2.0-licensed agentic SAST tool released by Visa's security engineering team. VVAH's
threat-modeling, call-graph decomposition, and adversarial verification pipeline has
surfaced 348 real, independently-verified findings across the platform to date (141 in
v1.1, 207 in v1.2) — see [CHANGELOG.md](isms-core-platform/CHANGELOG.md) for the summary
and the [v1.1](https://isms-core.com/blog/isms-core-vvah-security-sweep/) /
[v1.2](https://isms-core.com/blog/isms-core-vvah-v15-rescan/) write-ups for the full
detail. Full credit to Visa for building and open-sourcing it.
