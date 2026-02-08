#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.17 — Authentication Information Compliance Checklist

Control A.5.17: Authentication Information
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Authentication Info Allocation (10 reqs)
4. Password Requirements (5 reqs)
5. Multi-Factor Authentication (13 reqs)
6. Authentication Info Protection (10 reqs)
7. Password Reset and Recovery (13 reqs)
8. Compliance Measurement (2 reqs)

Total: 53 requirements across 6 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.5.17"
CONTROL_ID = "A.5.17"
CONTROL_NAME = "Authentication Information"
SOURCE_POLICY = "ISMS-OP-POL-A.5.17"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.17
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Authentication Info Allocation", [
        ("A.5.17-01", "Before Issuing New Or Replacement",
         "Before issuing new or replacement authentication credentials, the identity of the requesting person shall be verified through at least one of the following methods:."),
        ("A.5.17-02", "The Verification Method Used",
         "The verification method used shall be documented for audit purposes."),
        ("A.5.17-03", "Authentication Information",
         "Authentication information shall be distributed through secure channels. Insecure methods such as unencrypted email or plain-text messaging shall not be used for credential distribution."),
        ("A.5.17-04", "Shall Have A Maximum",
         "Shall have a maximum validity of 24 hours."),
        ("A.5.17-05", "Shall Require Change On",
         "Shall require change on first use."),
        ("A.5.17-06", "Shall Be Generated With",
         "Shall be generated with sufficient randomness and length to resist guessing."),
        ("A.5.17-07", "Shall Be Invalidated After",
         "Shall be invalidated after successful use."),
        ("A.5.17-08", "Vendor-Supplied And Default Passwords",
         "Vendor-supplied and default passwords shall be changed immediately upon installation, before any system is connected to the production network."),
        ("A.5.17-09", "Default Accounts",
         "Default accounts shall be disabled or renamed where technically feasible."),
        ("A.5.17-10", "System Limitation), The Following",
         "Where default credentials cannot be changed (vendor firmware dependency, system limitation), the following compensating controls shall be applied:."),
    ]),

    ("Password Requirements", [
        ("A.5.17-11", "Enforce The Following Password",
         "The organisation shall enforce the following password standards, aligned with NIST SP 800-63B-4:."),
        ("A.5.17-12", "Privileged Accounts (Administrator, Tier",
         "Privileged accounts (administrator, Tier 0/1 accounts) shall enforce:."),
        ("A.5.17-13", "Not",
         "Personnel shall not:."),
        ("A.5.17-14", "Store Passwords Using Approved One-Way",
         "Systems shall store passwords using approved one-way cryptographic hashing with unique per-password salt:."),
        ("A.5.17-15", "Password Databases",
         "Password databases shall be protected with encryption at rest and access restricted to authorised service accounts."),
    ]),

    ("Multi-Factor Authentication", [
        ("A.5.17-16", "Multi-Factor Authentication",
         "Multi-factor authentication shall be required for the following access types:."),
        ("A.5.17-17", "Acceptable Authentication Factors",
         "Acceptable authentication factors shall be drawn from at least two different categories:."),
        ("A.5.17-18", "Mfa Methods",
         "MFA methods shall be selected with preference for phishing resistance:."),
        ("A.5.17-19", "Sms-Based Otp",
         "SMS-based OTP shall be documented in the risk register with a migration plan to a stronger method. New system deployments shall not implement SMS-based MFA as the sole second factor."),
        ("A.5.17-20", "Plan And Execute Migration Toward",
         "The organisation shall plan and execute migration toward phishing-resistant authentication (FIDO2/WebAuthn passkeys) as the primary MFA method. FIDO2 uses public-key cryptography bound to the legitimate service origin, preventing credential phishing even if users are tricked by fraudulent sites."),
        ("A.5.17-21", "Backup Mfa Method: Users Are Encouraged",
         "Backup MFA method: Users are encouraged to register a backup MFA method (e.g., second hardware key stored securely, backup authenticator app). Privileged users shall register at least two independent MFA methods."),
        ("A.5.17-22", "Template Storage: Biometric Templates",
         "Template storage: Biometric templates shall be stored locally on the device (not centralised) where technically feasible. If centralised storage is required, templates shall be encrypted at rest with AES-256."),
        ("A.5.17-23", "Liveness Detection: Biometric Systems",
         "Liveness detection: Biometric systems shall implement liveness detection to prevent replay attacks (e.g., photographs, silicone fingerprints)."),
        ("A.5.17-24", "Fallback: A Non-Biometric Fallback",
         "Fallback: A non-biometric fallback authentication method shall always be available (biometrics shall not be the sole authentication factor)."),
        ("A.5.17-25", "Consent: Personnel",
         "Consent: Personnel shall provide informed consent before biometric enrolment, in compliance with Swiss nFADP requirements for sensitive personal data processing."),
        ("A.5.17-26", "Revocation: Biometric Templates",
         "Revocation: Biometric templates shall be deleted upon employment termination or when the individual withdraws consent."),
        ("A.5.17-27", "Accuracy: Biometric Systems",
         "Accuracy: Biometric systems shall be configured with a false acceptance rate (FAR) appropriate to the risk level (recommended: FAR <= 1:50'000 for standard access, FAR <= 1:1'000'000 for privileged access)."),
        ("A.5.17-28", "Systems That Cannot Support Mfa",
         "Systems that cannot support MFA shall be documented in the risk register with:."),
    ]),

    ("Authentication Info Protection", [
        ("A.5.17-29", "Personnel",
         "All personnel shall:."),
        ("A.5.17-30", "The Main Access Authentication System",
         "The main access authentication system shall:."),
        ("A.5.17-31", "Validate The Log-On Information Only On",
         "Validate the log-on information only on completion of all input data; if an error condition arises, the system shall not indicate which part of the data is correct or incorrect."),
        ("A.5.17-32", "Shared Authentication Information Is",
         "Shared authentication information is discouraged and shall be avoided wherever possible. Where shared credentials are required (legacy systems, vendor-mandated accounts):."),
        ("A.5.17-33", "Be Stored In The Approved Credential",
         "Credentials shall be stored in the approved credential vault [Password Manager], not in plaintext documents, email, or chat."),
        ("A.5.17-34", "A Named Custodian",
         "A named custodian shall be assigned for each shared credential."),
        ("A.5.17-35", "Check-Out Logging With User",
         "Check-out logging with user identification and timestamp shall be maintained."),
        ("A.5.17-36", "Individual Accountability",
         "Individual accountability shall be maintained through audit logging."),
        ("A.5.17-37", "Access And Usage",
         "Access and usage shall be reviewed quarterly; annual reauthorisation required."),
        ("A.5.17-38", "Shared Accounts",
         "Shared accounts shall be included in the privileged account register and access review process."),
    ]),

    ("Password Reset and Recovery", [
        ("A.5.17-39", "Mfa-Based Verification (Authenticator",
         "MFA-based verification (authenticator push, FIDO2, or hardware token) shall be required before a password reset is permitted."),
        ("A.5.17-40", "Knowledge-Based Security Questions",
         "Knowledge-based security questions shall not be used as the sole verification method due to their susceptibility to social engineering."),
        ("A.5.17-41", "Reset Tokens",
         "Reset tokens shall be time-limited (maximum 1 hour validity) and single-use."),
        ("A.5.17-42", "Reset Activities",
         "All reset activities shall be logged, including the verification method used."),
        ("A.5.17-43", "The User",
         "The user shall be notified of the password change via a registered secondary contact (email or mobile)."),
        ("A.5.17-44", "The Reset Process",
         "The reset process shall not reveal whether an account exists (prevent account enumeration)."),
        ("A.5.17-45", "Helpdesk-Assisted Password Resets",
         "Helpdesk-assisted password resets shall follow this procedure:."),
        ("A.5.17-46", "Verify Identity: The Helpdesk",
         "Verify identity: The helpdesk shall verify the caller's identity using at least one pre-registered verification method (secondary email, registered mobile number, manager confirmation, or in-person with photo ID)."),
        ("A.5.17-47", "Generate Temporary Password: A Random",
         "Generate temporary password: A random temporary password shall be generated meeting minimum length requirements."),
        ("A.5.17-48", "Communicate Securely: The Temporary",
         "Communicate securely: The temporary password shall be communicated via a secure channel (not unencrypted email); where possible, use the identity provider's secure reset link."),
        ("A.5.17-49", "Force Change: The Temporary Password",
         "Force change: The temporary password shall expire on first use, requiring the user to set a new password immediately."),
        ("A.5.17-50", "Document: The Reset Request,",
         "Document: The reset request, verification method used, and timestamp shall be recorded in the IT service management system."),
        ("A.5.17-51", "Helpdesk Personnel",
         "Helpdesk personnel shall not have access to view user passwords after issuance."),
    ]),

    ("Compliance Measurement", [
        ("A.5.17-52", "The Information Security Management Team",
         "The information security management team shall verify compliance with this policy through various methods, including but not limited to, identity provider configuration audits, MFA coverage reports, breach screening verification, authentication log analysis, penetration testing, internal and external audits, and feedback to the policy owner."),
        ("A.5.17-53", "Be Reported To The Ciso Quarterly",
         "Metrics shall be reported to the CISO quarterly. Metrics falling below target shall include a remediation plan with owner and target date."),
    ]),

])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS
    ))


# =============================================================================
# QA_VERIFIED: 2026-02-08
# QA_STATUS: PASSED - AUTO-GENERATED (Phase 2 Operational Checklist)
# QA_TOOL: meta_generate_op_checklists.py
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.17
# =============================================================================
