#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.24 — Use of Cryptography Compliance Checklist

Control A.8.24: Use of Cryptography
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Cryptographic Controls (22 reqs)
4. Cryptographic Key Management (22 reqs)
5. Optional Payment Card Data (2 reqs)

Total: 46 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/SCR/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'SCR'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.8.24"
CONTROL_ID = "A.8.24"
CONTROL_NAME = "Use of Cryptography"
SOURCE_POLICY = "ISMS-OP-POL-A.8.24"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.24
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Cryptographic Controls", [
        ("A.8.24-01", "Use The Following Minimum Cryptographic",
         "The organisation shall use the following minimum cryptographic standards:."),
        ("A.8.24-02", "Prohibited Algorithms:* Md5, Sha-1, Des,",
         "Prohibited algorithms:* MD5, SHA-1, DES, 3DES, RC4, RSA below 2048-bit. These shall not be used for any purpose."),
        ("A.8.24-03", "Monitor Nist Post-Quantum Cryptography",
         "The organisation shall monitor NIST post-quantum cryptography standards (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA) and plan migration as adoption timelines are established. A crypto-agility assessment shall be conducted to identify systems and data stores requiring PQC migration planning, prioritising long-lived keys and data with retention periods exceeding 10 years."),
        ("A.8.24-04", "Network Communications Carrying",
         "All network communications carrying confidential or personal data shall use encrypted transport:."),
        ("A.8.24-05", "Tls 1.3 Is Preferred And",
         "TLS 1.3 is preferred and shall be used where supported."),
        ("A.8.24-06", "Tls 1.0 And Tls 1.1",
         "TLS 1.0 and TLS 1.1 shall be disabled on all systems."),
        ("A.8.24-07", "Ssl (All Versions)",
         "SSL (all versions) shall be disabled on all systems."),
        ("A.8.24-08", "Only Cipher Suites Using Aead (E.G",
         "Only cipher suites using AEAD (e.g., AES-GCM) shall be enabled where feasible."),
        ("A.8.24-09", "Mobile Devices, Laptops, And Removable",
         "Mobile devices, laptops, and removable media shall have full-disk encryption enabled at the hardware or operating system level."),
        ("A.8.24-10", "Device Encryption",
         "Device encryption shall not be disabled."),
        ("A.8.24-11", "Access To Encrypted Storage",
         "Access to encrypted storage shall be protected by a password, passphrase, PIN, or biometric authentication."),
        ("A.8.24-12", "Not Be Used To Transfer Confidential",
         "Email shall not be used to transfer confidential or personal data in an unencrypted format, in line with the Information Transfer Policy."),
        ("A.8.24-13", "An Encrypted Attachment",
         "Where confidential data must be sent via email, an encrypted attachment shall be used with a key length that meets the approved algorithm requirements above."),
        ("A.8.24-14", "Evaluate And Approve An Email Encryption",
         "The organisation shall evaluate and approve an email encryption solution appropriate to its needs. Until a solution is deployed, encrypted file attachments with out-of-band key exchange shall be used as an interim measure."),
        ("A.8.24-15", "Web And Cloud Services That Process",
         "Web and cloud services that process, store, or transmit confidential or personal data shall implement TLS 1.2 at a minimum to protect data in transit."),
        ("A.8.24-16", "Have A Valid Certificate Issued By",
         "All servers shall have a valid certificate issued by a recognised Certificate Authority. System owners are responsible for certificate renewal and ensuring systems are updated before expiry."),
        ("A.8.24-17", "Not Be Used",
         "WEP shall not be used."),
        ("A.8.24-18", "Backups",
         "Backups containing confidential or personal data shall be encrypted using organisation-approved encryption technology meeting the minimum algorithm requirements above."),
        ("A.8.24-19", "Backup Encryption",
         "Backup encryption shall not rely solely on vendor-proprietary mechanisms without documented assurance of the encryption standard used."),
        ("A.8.24-20", "Databases",
         "Databases containing confidential information or personal data shall be encrypted at rest at either the database application layer or the disk/volume layer."),
        ("A.8.24-21", "The Transfer Of Confidential And",
         "The transfer of confidential and personal information shall use encrypted channels. Encryption is required for:."),
        ("A.8.24-22", "Not Be Used As A Communication",
         "Bluetooth shall not be used as a communication method for unencrypted confidential, personal, or otherwise sensitive data. See the Information Transfer Policy."),
    ]),

    ("Cryptographic Key Management", [
        ("A.8.24-23", "Cryptographic Keys",
         "Cryptographic keys shall be generated within cryptographic modules with at least FIPS 140-2 or FIPS 140-3 compliance, or equivalent validated assurance."),
        ("A.8.24-24", "Any Random Values Required For Key",
         "Any random values required for key generation shall be generated within the cryptographic module using a validated random bit generator."),
        ("A.8.24-25", "Be Transported Using Secure Channels.",
         "Keys shall be transported using secure channels. Key material shall not be transmitted in plaintext over any network."),
        ("A.8.24-26", "Never Be Stored In Plaintext Format",
         "Keys shall never be stored in plaintext format."),
        ("A.8.24-27", "Be Stored In A Cryptographic Vault",
         "Keys shall be stored in a cryptographic vault, HSM, or cloud key management service (KMS)."),
        ("A.8.24-28", "Not Be Hard-Coded In Source Code",
         "Keys shall not be hard-coded in source code, stored in configuration files in plaintext, or shared via email or messaging. This extends to API keys, tokens, service credentials, and other secrets — these shall be managed through a dedicated secrets management solution (e.g., AWS KMS, Azure Key Vault, HashiCorp Vault, or equivalent). Secrets do not require the same encryption-at-rest standards as data encryption keys but shall never be stored in plaintext and shall be rotated according to the key rotation periods above."),
        ("A.8.24-29", "Key Encryption Keys (Keks) Used To",
         "Key encryption keys (KEKs) used to wrap stored keys shall be at least as strong as the keys they protect."),
        ("A.8.24-30", "Have Integrity Protections Applied While",
         "Keys shall have integrity protections applied while in storage."),
        ("A.8.24-31", "Access To Cryptographic Keys",
         "Access to cryptographic keys shall follow the principle of least privilege."),
        ("A.8.24-32", "Administrative And Operational Access To",
         "Administrative and operational access to keys shall be separated where possible."),
        ("A.8.24-33", "Multi-Factor Authentication",
         "Multi-factor authentication shall be required for key custodians."),
        ("A.8.24-34", "A Register Of Individuals With Access",
         "A register of individuals with access to key material shall be maintained."),
        ("A.8.24-35", "Key Rotation Periods",
         "Key rotation periods shall be defined based on key type, risk, and regulatory requirements."),
        ("A.8.24-36", "Be Rotated Immediately Upon Suspected Or",
         "Keys shall be rotated immediately upon suspected or confirmed compromise, regardless of scheduled rotation."),
        ("A.8.24-37", "Key Material",
         "Key material shall be backed up to enable recovery of encrypted data."),
        ("A.8.24-38", "Backup Key Storage",
         "Backup key storage shall be encrypted using at least the same assurance level as the operational keys."),
        ("A.8.24-39", "Signing Keys",
         "Signing keys shall not be escrowed."),
        ("A.8.24-40", "A Key Compromise Recovery Plan",
         "A key compromise recovery plan shall be documented, tested annually, and maintained as a referenced procedure. The plan shall include:."),
        ("A.8.24-41", "Trust Stores",
         "Trust stores shall be protected against injection of unauthorised root certificates. Access controls shall be managed and enforced per entity and application."),
        ("A.8.24-42", "A Secure Process For Updating The",
         "A secure process for updating the trust store shall be implemented."),
        ("A.8.24-43", "Only Reputable Cryptographic Libraries",
         "Only reputable cryptographic libraries shall be used that are actively maintained, regularly updated, and validated by third-party organisations (e.g., NIST/FIPS, Common Criteria)."),
        ("A.8.24-44", "Custom Cryptographic Implementations",
         "Custom cryptographic implementations shall not be developed unless specifically approved by the CISO with documented justification."),
    ]),

    ("Optional Payment Card Data", [
        ("A.8.24-45", "Secret And Private Keys Used To",
         "Secret and private keys used to encrypt/decrypt cardholder data shall be stored encrypted with a key-encrypting key at least as strong as the data-encrypting key, stored separately from the data-encrypting key, or within a PTS-approved device or HSM."),
        ("A.8.24-46", "Cardholder Data Environment Encryption",
         "Cardholder data environment encryption shall meet PCI DSS requirements in addition to this policy."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.24
# =============================================================================
