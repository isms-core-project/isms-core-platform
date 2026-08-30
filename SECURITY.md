# Security Policy

ISMS CORE takes security seriously. If you discover a vulnerability in this repository — including scripts, workbook generators, templates, or documentation that could cause unsafe outcomes — or in the running ISMS CORE platform itself (the backend API and services distributed as the Docker images referenced by this repo's `docker-compose.yml`), please report it responsibly.

## Reporting a Vulnerability

Please email: **info@isms-core.com**
Subject: **ISMS CORE Security — Vulnerability Report**

Include:
- A clear description of the issue and potential impact
- Reproduction steps (proof-of-concept if available)
- Affected files/folders (control pack name if relevant)
- Any suggested remediation

If you prefer encrypted reporting, request a PGP key via email and we will provide one.

## What to Expect

We will:
- Acknowledge receipt within **3 business days**
- Provide a status update within **10 business days**
- Work with you on a coordinated disclosure timeline when appropriate

## Scope

**In scope:**
- The ISMS CORE platform itself — the backend API and services shipped in the Docker images this
  repo's `docker-compose.yml` pulls, including authentication, authorisation, and multi-tenant
  (organisation-level) data isolation
- Python scripts and generators in `SCR/`
- Workbook templates and outputs where repository-provided logic may be unsafe
- Promotion/QA scripts and automation
- Supply-chain risks introduced by dependencies (when applicable)

**Out of scope:**
- Vulnerabilities in third-party tools or services not distributed with ISMS CORE
- Social engineering, spam, or physical attacks

## Authentication Security

ISMS CORE supports TOTP-based MFA (RFC 6238) for all user accounts. We recommend:
- Enabling MFA on all admin and super_admin accounts before production use
- Rotating the `SECRET_KEY` environment variable when deploying to a new environment
- Using strong, unique values for `POSTGRES_PASSWORD` and `SECRET_KEY` (minimum 32 characters, randomly generated)

## Proactive Security Reviews

Beyond responding to external reports, we periodically run the platform's own codebase
through [Visa's Vulnerability Agentic Harness (VVAH)](https://github.com/visa/visa-vulnerability-agentic-harness),
an open-source agentic SAST tool, and fix every independently-verified finding before
it ships. The most recent full pass (backend, frontend, and every connector/feed/
threat-intel/SMTP-bridge service) landed in v1.1 — see
[isms-core-platform/CHANGELOG.md](isms-core-platform/CHANGELOG.md) for the summary.

## Safe Handling

- Do not include secrets, tokens, private keys, or customer data in vulnerability reports.
- Treat generated artifacts as potentially sensitive until reviewed.

Thank you for helping improve ISMS CORE.
