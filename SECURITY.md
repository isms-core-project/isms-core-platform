# Security Policy

ISMS CORE takes security seriously. If you discover a vulnerability in this repository (including scripts, workbook generators, templates, or documentation that could cause unsafe outcomes), please report it responsibly.

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
- Python scripts and generators in `SCR/`
- Workbook templates and outputs where repository-provided logic may be unsafe
- Promotion/QA scripts and automation
- Supply-chain risks introduced by dependencies (when applicable)

**Out of scope:**
- Vulnerabilities in third-party tools or services not distributed with ISMS CORE
- Social engineering, spam, or physical attacks

## Safe Handling

- Do not include secrets, tokens, private keys, or customer data in vulnerability reports.
- Treat generated artifacts as potentially sensitive until reviewed.

Thank you for helping improve ISMS CORE.
