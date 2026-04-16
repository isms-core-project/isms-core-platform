# Getting Started

<!-- ISMS-CORE:USER-MANUAL:02-getting-started:v1.0:2026-04-16 -->

---

## Logging In

Navigate to your platform URL in a browser. If you see a certificate warning ("Your connection is not private"), this is expected on internal deployments using a self-signed certificate. Accept the warning to proceed — the connection is still encrypted.

Enter your email address and password. If you have Multi-Factor Authentication (MFA) enabled, you will be prompted for your 6-digit TOTP code after entering your password.

> Your administrator sets your initial password and role. Contact them if you cannot log in or have forgotten your credentials.

---

## The Dashboard

After logging in, you land on the **Home dashboard**. This is your operational overview for the active product.

### Intelligence Cards

At the top of the dashboard, four intelligence cards show the current state of your threat feed data:

- **CVE Index** — total CVEs indexed from the NVD feed
- **CISA KEV** — total Known Exploited Vulnerabilities tracked
- **MITRE ATT&CK** — last feed update timestamp
- **Feed Health** — overall status of all threat intelligence feeds

Click any card to navigate to the **Threat Intelligence** section.

### Compliance Metrics

Below the intelligence cards, the dashboard shows compliance metrics for the active product family:

- Total control groups and coverage percentage
- Policy status summary (imported, draft, approved, published)
- Assessment completeness
- Open gaps count
- Evidence freshness indicator
- Audit readiness score

### Health Alert Banner

If any feed run, connector sync, or OpenSearch check has reported an error in the last 24 hours, a dismissible amber banner appears at the top of the page. This is purely informational — the platform continues to function. Click the banner or navigate to **Intelligence** to investigate.

---

## Navigation

### Sidebar

The left sidebar is your primary navigation. It collapses to a narrow icon-only strip — click the chevron at the bottom to toggle. Hover over any icon in collapsed mode to see a tooltip with the section name.

The sidebar is organised into groups:

| Group | What it contains |
|-------|-----------------|
| **ISMS** | Control Library, Overview, Policies, Coverage, Generator Workbooks |
| **Projects** | Projects Workspace |
| **Compliance** | Assessment Checklists, all 23 Framework Assessment pages |
| **Risk & Operations** | Risk Register, Gap Management, EBIOS RM, BIA, TPRM |
| **Evidence** | Evidence Tracker, Connectors |
| **Intelligence** | MITRE ATT&CK, CVE/CPE Explorer, KEV Audit |
| **Analytics** | KPI Dashboard, Cross-Framework Mapping |
| **Tools** | QA Engine, ISMS Compass, Custom Frameworks |
| **Global** | All framework assessment pages (NIS2, DORA, NIST CSF 2.0, etc.) |
| **Admin** | User management, system config, import panel (Admin role only) |

### Product Switcher

The product switcher appears at the top of the ISMS group in the sidebar (or as a tab selector on product-aware pages). Use it to switch between:

- **ISMS** — Framework and Operational content
- **Privacy** — ISO 27701:2025 content
- **Cloud** — ISO 27018:2025 content
- **AI** — ISO 42001:2023 content

Switching products changes the context shown in the Control Library, Policies, Coverage, and Assessment pages. Framework-level tools (Risk Register, Gap Management, Evidence, etc.) are not product-specific — they cover your full ISMS scope.

---

## Your Active Project

Most compliance work in the platform happens inside a **Project**. A project is a named workspace that owns a curated subset of the content library — the policies, implementations, assessments, gaps, and evidence relevant to a specific scope, audit cycle, or organisational unit.

The **active project** is shown in the sidebar as a coloured chip below the product switcher. You can switch your active project at any time from the Projects Workspace.

If no project is active, you are working in the global library view — you can browse all content but cannot edit or track items.

> **Recommended first step:** Ask your administrator to create a project for your organisation, or create one yourself if you have the ISMS Manager role (see [Projects Workspace](04-projects-workspace.md)).

---

## User Roles and What You Can Do

Your role determines what you can see and do in the platform.

| Role | Capabilities |
|------|-------------|
| **Super Admin** | Cross-organisation access — manages orgs and users, views portfolio metrics |
| **Admin** | Full access within the organisation — user management, imports, system config |
| **ISMS Manager** | All compliance work: controls, assessments, gaps, evidence, projects, risk |
| **Auditor** | Read-only access to everything. Can run exports and QA checks. |
| **Control Owner** | Read/write on assigned control groups only |
| **Viewer** | Read-only on non-confidential content |

Contact your administrator if you need access to a capability not available under your current role.

---

## Profile and MFA

Access your profile by clicking your name or avatar at the top right of the screen (or navigate to **System → MFA Setup**).

### Changing Your Password

Go to **Admin → Users**, find your account, and use the Edit action to update your password.

### Setting Up MFA

Two-factor authentication is strongly recommended for all users, required for Admin and above.

1. Navigate to **System → MFA Setup**
2. Scan the QR code with Google Authenticator, Authy, or any TOTP app
3. Enter the 6-digit code to confirm setup
4. Save the 8 backup codes shown — these are single-use recovery codes for when you do not have your authenticator device

Once enabled, you will be prompted for your TOTP code on every login.

---

## Next Steps

- Browse your controls: [Control Library](03-control-library.md)
- Start working on documents: [Projects Workspace](04-projects-workspace.md)
- Understand your compliance posture: [Compliance Assessments](06-compliance-assessments.md)

<!-- QA_VERIFIED: 2026-04-16 -->
