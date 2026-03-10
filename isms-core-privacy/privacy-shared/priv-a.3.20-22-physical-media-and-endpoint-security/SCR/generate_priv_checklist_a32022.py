#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.20-22 — Physical Media and Endpoint Security Compliance Checklist

Controls A.3.20-22: Storage Media Lifecycle (PII), Secure Disposal and Re-use
                    of Equipment (PII), User Endpoint Devices (PII)
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Storage Media Lifecycle (A.3.20) — 5 reqs
4. Equipment Disposal and Re-use (A.3.21) — 5 reqs
5. User Endpoint Device Protection (A.3.22) — 4 reqs

Total: 14 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_PRIV_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_PRIV_ROOT / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "PRIV-CHK-A.3.20-22"
CONTROL_ID = "A.3.20-22"
CONTROL_NAME = "Physical Media and Endpoint Security"
SOURCE_POLICY = "PRIV-POL-A.3.20-22"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.20-22
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Storage Media Lifecycle", [
        ("A.3.20-01", "Media Registration",
         "All removable storage media that will or may contain PII shall be registered in the Media Register upon acquisition. Each registered media item shall have an assigned owner. Media classification shall be assigned at first use based on the PII content stored, consistent with the classification scheme in PRIV-POL-A.3.5-7."),
        ("A.3.20-02", "Media in Use — Encryption",
         "Media containing RESTRICTED PII (special category) shall be encrypted at all times. Media containing CONFIDENTIAL PII shall be encrypted when transported outside secure premises. Unattended media containing PII shall be physically secured (in locked storage or locked equipment), consistent with clear desk requirements in PRIV-POL-A.3.17-19."),
        ("A.3.20-03", "Media Transportation",
         "Transportation of media containing PII outside secure premises shall be logged, including destination, purpose, and return date. Media containing CONFIDENTIAL PII transported externally shall use approved encrypted media or approved secure courier. Loss of media during transport shall be reported immediately as a PII incident per PRIV-POL-A.3.11-12."),
        ("A.3.20-04", "Media Disposal",
         "Storage media containing PII shall not be disposed of through standard waste streams. Before disposal, PII shall be irreversibly removed by cryptographic erasure (for encrypted media), secure overwrite (DoD 5220.22-M or equivalent standard), or physical destruction. Disposal method shall be documented in the Media Register, including method used, date, and responsible person."),
        ("A.3.20-05", "Third-Party Destruction",
         "Third-party media destruction service disposal shall produce a certificate of destruction before media leaves the organisation's custody. Certificates of destruction shall be retained as evidence. For RESTRICTED PII, physical destruction of storage media is required (sale or donation of such media not permitted without confirmed destruction)."),
    ]),

    ("Equipment Disposal and Re-use", [
        ("A.3.21-01", "Pre-Disposal Verification",
         "Before any item of equipment containing storage media is disposed of or re-used (within or outside the organisation), the organisation shall verify that any PII has been removed or securely overwritten. Verification shall follow a documented procedure: inventory check, data erasure, verification scan, and documentation in the Disposal Register."),
        ("A.3.21-02", "Erasure Standards",
         "Approved erasure methods for equipment containing PII: software erasure using industry-standard overwrite (minimum DoD 5220.22-M single pass; NIST SP 800-88 is authoritative guidance); cryptographic erasure by destruction of encryption keys (acceptable where full-disk encryption is confirmed active throughout the media's life); physical destruction by shredding or degaussing (required for RESTRICTED PII or where software erasure is technically impractical)."),
        ("A.3.21-03", "Disposal Register",
         "A Disposal Register shall be maintained recording all equipment disposal and re-use events involving storage media where PII may have been present: device asset ID, PII status, erasure method used, verification outcome, date, and responsible person. Disposal Register records shall be retained for minimum 5 years."),
        ("A.3.21-04", "Re-use Within Organisation",
         "Before reassignment of equipment to another user within the organisation: all PII from the previous user's profile shall be removed; the device shall be imaged or reset to baseline configuration; and a new user access record shall be created with the previous user's access revoked per PRIV-POL-A.3.8-10."),
        ("A.3.21-05", "Third-Party Disposal",
         "Where equipment is disposed of through a third-party service, the third party shall provide a certificate of data destruction before equipment leaves the organisation's custody. For equipment containing RESTRICTED PII, physical destruction of storage media is required before disposal. Certificates of destruction shall be retained in the Disposal Register for minimum 5 years."),
    ]),

    ("User Endpoint Device Protection", [
        ("A.3.22-01", "Minimum Endpoint Controls",
         "All corporate endpoint devices that store, process, or access PII shall be configured with: full-disk encryption (active and enforced); automatic screen lock after maximum idle period; remote wipe capability (registered and tested at minimum annually); device management enrolment in corporate MDM or UEM where technically feasible; and current operating system and security patches applied within defined timeframes."),
        ("A.3.22-02", "PII Storage Restrictions",
         "Bulk download or storage of PII on endpoint devices shall be limited to what is necessary for the job function. Copying or storing large volumes of PII on local endpoints requires Data Owner approval. RESTRICTED PII shall not be stored locally on endpoints except where operationally necessary with DPO notification; where stored locally, it shall be in an encrypted container with access controls separate from general file system access."),
        ("A.3.22-03", "BYOD Controls",
         "Where personal devices are permitted to access PII, BYOD devices shall be enrolled in an MDM containerisation solution creating a managed PII workspace segregated from personal data. Minimum controls (encryption, screen lock, remote wipe) shall apply to the managed workspace. The organisation's right to remote wipe the managed workspace shall be agreed in writing before PII access is granted. PII shall not be stored outside the managed workspace on BYOD devices."),
        ("A.3.22-04", "Lost or Stolen Devices",
         "Loss or theft of an endpoint device containing or with access to PII shall be: reported immediately to the IT Security Team and DPO; treated as a suspected PII incident and managed per PRIV-POL-A.3.11-12; and subject to remote wipe initiated within 4 hours of confirmed loss. Device loss and remote wipe actions shall be documented."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27701:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Privacy product launch
# =============================================================================
