# Organisations & Users

<!-- ISMS-CORE:USER-MANUAL:20-organisations-users:v1.3:2026-10-17 -->

---

## Overview

ISMS CORE Platform supports multi-tenant operation — multiple organisations can run on a single platform instance with full data isolation. Within each organisation, role-based access control determines what each user can see and do.

User and organisation management is an **Admin** function. This chapter covers the settings relevant to all roles.

---

## Organisations

Each organisation in the platform represents an independent tenant — a company, subsidiary, or separate organisational scope. Organisations do not share data.

### Organisation Settings

Administrators can configure the following per-organisation in **Admin → Organisation**:

| Setting | Description |
|---------|-------------|
| **Organisation name** | Legal or operating name |
| **Country** | Jurisdiction for policy localisation (CH, AT, BE, DE, FR, GB, IT, LU) |
| **Industry sector** | Used for framework relevance recommendations |
| **Active projects** | Which project is the default active project per product family |

**Country setting and policy localisation:** When the country is set, policy documents are rendered with jurisdiction-specific regulatory references. For example, setting the country to `DE` causes GDPR references to appear alongside relevant BDSG references, and the Datenschutzbehörde (DSB) to appear in place of the generic "supervisory authority" token. See [Introduction](01-introduction.md) for the full list of supported jurisdictions.

---

## Users

### Roles

There are six roles. A person has **one role in each organisation** they belong to.

| Role | What they can do |
|------|-----------------|
| **Viewer** | Reads everything in the organisation (controls, policies, assessments, evidence, gaps, risks, reports, dashboards) and manages their own account. Cannot change anything else. |
| **Auditor** | Everything a Viewer can, plus **raises findings** (creates gaps), **accepts or flags evidence**, and uses the AI assistant, ISMS Compass, IP look-up and KPI snapshots. Cannot create, edit or delete the records being audited — by design, an auditor is independent of what is audited. |
| **Control Owner** | For the **control groups assigned to them**: uploads, edits, submits and deletes evidence; raises and updates gaps; fills in assessment items; edits remediation actions. Reads everything else. Cannot approve evidence, create assessments or projects, or delete remediation actions. |
| **ISMS Manager** | All compliance work on **all** control groups: projects (policies, implementations, checklists), assessments, risk register, BIA, EBIOS RM, CSRM, collections, third-party risk, regulatory modules, NIST CSF, report generators, approving or rejecting evidence, QA checks of a project, and pushing gaps to Jira / ServiceNow. |
| **Admin** | ISMS Manager rights plus users and groups, organisation settings, connectors, custom frameworks, notification settings and the event and audit logs. |
| **Super Admin** | Everything in every organisation, plus platform-wide operations: creating and archiving organisations, giving access to other organisations, library content, feeds and threat-intelligence sources, library-wide QA, the System page. Assigned at the platform level. |

The **Roles & permissions** tab of the in-app Help (**Help → Roles & permissions**) has the complete tables, area by area, with a short description of every role.

### Managing Users (Admin only)

Navigate to **Admin → Users** to:

- **Add a user** — click **Add User**, enter email, username, full name, an initial password and the role. For a Control Owner, also choose the assigned control groups.
- **Edit a user** — change role, name, assigned control groups, or (Super Admin only) the organisation
- **Disable a user** — revokes access without deleting the account
- **Delete a user** — removes the account; their entries in the audit log stay, with the email address they acted under
- **Reset MFA** — for a person who lost their authenticator and backup codes
- **Locked sign-ins** — when a card **Locked sign-ins** appears above the user list, someone is currently locked out. Five wrong passwords from one address lock **that address for that account only** (5 minutes, doubling up to 15 minutes; 60 for administrators), so a stranger who knows an e-mail address cannot lock the real user out from their own address. An account is locked **as a whole** only when wrong passwords arrive from many different addresses (credential guessing from rotating addresses). Use **Unlock** (that account and address), **Unblock IP** (that address for every account of your organisation) or **Unlock account**; the user can sign in again immediately. Every unlock is written to the audit log. Super Admins see the locks of all organisations; an Admin sees their own.

A role or control-group change applies at the person's next action.

### Control groups for a Control Owner

A **control group** is a group of related controls (for example *A.5.15 Access control*). A Control Owner works **only on the control groups assigned to them**:

1. Open **Admin → Users** and click **Add User** (or **Edit** next to an existing Control Owner).
2. Choose the role **Control Owner**; the field **Assigned control groups** appears.
3. Pick the control groups and save.

Outside their groups a Control Owner can only read. A Control Owner **with no assigned group can read everything but cannot change anything** — assign at least one when you create the account.

### Groups of people

**Admin → Users → Groups** lets an Admin create named groups of users (for example *Internal audit team*) and add or remove members. Groups are an organising tool only: **they grant no permission and cannot restrict a role**. Permissions always come from the role and, for Control Owners, from the assigned control groups.

### Working in several organisations

Consultants and implementers often work for several clients. A **Super Admin** can give an existing account access to another organisation, with its **own role** there: **Admin → Users → Access from other organisations → Give access**.

- Anyone who belongs to more than one organisation sees an **organisation switcher** at the top of the sidebar. Choosing another organisation changes the role, the control groups and all data to that organisation's.
- The password, MFA and account status stay with the person's **home organisation**.
- An Admin of an organisation can change or remove the access of its members; the change applies at the person's next action.
- Nobody can give themselves access, and the Super Admin role cannot be given this way.

---

## Multi-Factor Authentication (MFA)

MFA is TOTP-based (Time-based One-Time Password) — compatible with Google Authenticator, Authy, Microsoft Authenticator, and any RFC 6238-compliant TOTP app.

### Setting Up MFA

1. Navigate to **System → MFA Setup**
2. Scan the QR code with your authenticator app
3. Enter the 6-digit code displayed in the app to confirm
4. **Save the 8 backup codes** — these are one-time-use codes for recovery when your device is unavailable

### Logging In with MFA

After entering your email and password, you are prompted for your 6-digit TOTP code. The code auto-submits when 6 digits are entered — you do not need to click a button.

If you have lost access to your authenticator app and your backup codes:
- Contact your organisation's Admin to reset your MFA
- Admins can reset MFA from **Admin → Users → Edit user**

### MFA Policy

MFA enforcement is configured by the administrator. When enforced:
- Users without MFA set up are prompted to complete setup at next login
- Users cannot bypass the MFA step

---

## System Event Log

Navigate to **Admin → System → Event Log** for an immutable audit trail of all platform actions. Every create, update, delete, import, and login event is recorded with:

- Timestamp
- User identity
- Action type
- Resource affected (document ID, user ID, etc.)
- IP address

The event log cannot be modified or deleted. It is the authoritative record of who did what and when — essential for ISO 27001:2022 Annex A.8.15 (Logging) and Annex A.5.26 (Response to information security incidents) audit requirements.

Export the event log as CSV from the log view.

---

## Third-Party API Keys (Super Admin)

The platform uses outside services — the NVD and VulnCheck vulnerability feeds, the threat-intelligence feeds and IP look-ups, and Anthropic (Claude AI) for the AI assistant, ISMS Compass and Claude QA. Their keys are managed by the **Super Admin** under **Admin → API keys** (the page is not shown to any other role). The keys are platform-wide: one key serves every organisation.

- Three tabs: **Vuln Feeds**, **TI Feeds** and **System**; one card per key.
- **Add key / Replace key** stores the key encrypted. A saved value is never shown again.
- The **Enabled** switch turns a saved key on or off without retyping it; **Remove** deletes it.
- A key takes effect at the next feed run or request — no restart.
- New installations enter their keys here. Installations upgraded from an earlier version had the keys already in the `.env` file imported once (they show as *Migrated from .env*); those `.env` lines can then be deleted. Until they are, a key that is switched off or removed here still falls back to its `.env` value.
- If the page warns that `PLATFORM_KEY_ENCRYPTION_SECRET` is not set, keys cannot be saved yet; the operator adds that secret to `.env` and recreates the backend, feeds and threat-intel containers.

---

## Admin Panel — Content Management

The Admin panel (**Admin → First-Run Setup**) is where platform content is imported and re-synced. This is typically a one-time operation at deployment time, repeated when content is updated.

As a non-admin user, you do not need to use this panel — it is documented in [PLATFORM.md](../PLATFORM.md) for administrators.

<!-- QA_VERIFIED: 2026-10-17 -->
