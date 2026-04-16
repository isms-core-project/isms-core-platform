# Organisations & Users

<!-- ISMS-CORE:USER-MANUAL:20-organisations-users:v1.0:2026-04-16 -->

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

| Role | What they can do |
|------|-----------------|
| **Super Admin** | Cross-organisation access — creates and manages organisations, views Metrics Portfolio. Assigned at the platform level. |
| **Admin** | Full access within their organisation — user management, system config, content import, admin panel |
| **ISMS Manager** | All compliance work: controls, assessments, gaps, evidence, projects, risk, TPRM, EBIOS RM, BIA |
| **Auditor** | Read-only access to everything in their organisation. Can run QA checks and exports. |
| **Control Owner** | Read/write on control groups assigned to them. Can update checklist items and upload evidence for their controls. |
| **Viewer** | Read-only access to non-confidential content |

### Managing Users (Admin only)

Navigate to **Admin → Users** to:

- **Add a user** — enter email, name, and role; an invitation email is sent if email is configured
- **Edit a user** — change role, name, or assigned organisation (Super Admin only)
- **Disable a user** — revokes access without deleting the account
- **Reset password** — sends a password reset email

### Role Assignment

Each user has exactly one role. To give a user access to a specific control group as a Control Owner, assign them the Control Owner role and then assign specific control groups to them from the Control Library (each control group has an **Assign Owner** option in its detail view).

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

## Admin Panel — Content Management

The Admin panel (**Admin → First-Run Setup**) is where platform content is imported and re-synced. This is typically a one-time operation at deployment time, repeated when content is updated.

As a non-admin user, you do not need to use this panel — it is documented in [PLATFORM.md](../PLATFORM.md) for administrators.

<!-- QA_VERIFIED: 2026-04-16 -->
