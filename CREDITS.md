# Credits & Acknowledgements

The connector architecture, asynchronous worker patterns (Celery beat/worker split),
service topology, and Docker Compose structure in ISMS CORE draw from production-grade
patterns established by [Filigran](https://filigran.io) and their open-source projects:

- **OpenCTI** — [https://github.com/OpenCTI-Platform/docker](https://github.com/OpenCTI-Platform/docker)
- **OpenAEV** — [https://github.com/OpenAEV-Platform/docker](https://github.com/OpenAEV-Platform/docker)

These implementations saved significant engineering time and provided a battle-tested
foundation for the ISMS CORE platform.

## Security tooling

The ISMS CORE Platform's v1.1 security hardening pass (backend, frontend, and every
connector/feed/threat-intel/SMTP-bridge service) was carried out using [Visa's
Vulnerability Agentic Harness (VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness),
an open-source, Apache-2.0-licensed agentic SAST tool released by Visa's security
engineering team. VVAH's threat-modeling, call-graph decomposition, and adversarial
verification pipeline surfaced 141 real, independently-verified findings across the
platform — see [CHANGELOG.md](isms-core-platform/CHANGELOG.md) for the summary and the
[blog post](https://isms-core.com/blog/isms-core-vvah-security-sweep/) for the full
write-up. Full credit to Visa for building and open-sourcing it.
