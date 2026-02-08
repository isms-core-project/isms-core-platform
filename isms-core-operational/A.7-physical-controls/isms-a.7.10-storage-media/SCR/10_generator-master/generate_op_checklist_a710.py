#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.7.10 — Storage Media Compliance Checklist

Control A.7.10: Storage Media
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Removable Media Management (14 reqs)
4. Media Use Requirements (10 reqs)
5. Transportation of Storage Media (10 reqs)
6. Storage Requirements (8 reqs)
7. Disposal of Storage Media (18 reqs)
8. Paper Documents & Physical (10 reqs)
9. Optional Payment Card Data (5 reqs)

Total: 75 requirements across 7 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.7.10"
CONTROL_ID = "A.7.10"
CONTROL_NAME = "Storage Media"
SOURCE_POLICY = "ISMS-OP-POL-A.7.10"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.7.10
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Removable Media Management", [
        ("A.7.10-01", "Use Of Removable Storage Media",
         "Use of removable storage media shall be authorised before deployment:."),
        ("A.7.10-02", "Obtain Authorisation From Their Line",
         "Employees shall obtain authorisation from their line manager before using any removable storage media for organisation data. Authorisation shall specify the permitted use case, data classification, and duration (default 12 months, maximum 24 months)."),
        ("A.7.10-03", "Removable Media",
         "All removable media shall be registered in [Asset Management System] with the following details: media type, capacity, serial number or asset tag, assigned user, purpose, maximum classification level of data to be stored, and authorisation expiration date."),
        ("A.7.10-04", "Only Organisation-Issued Or",
         "Only organisation-issued or organisation-approved removable media shall be used for organisation data. Personal USB drives, external hard drives, or other personal storage devices shall not be used for CONFIDENTIAL or INTERNAL data under any circumstances."),
        ("A.7.10-05", "Organisation-Issued Removable Media",
         "Organisation-issued removable media shall be procured through approved suppliers from the organisation's procurement process. Unapproved or unknown-origin media shall not be connected to organisation systems."),
        ("A.7.10-06", "Maintain A List Of Approved Removable",
         "The organisation shall maintain a list of approved removable media types. As a minimum:."),
        ("A.7.10-07", "Be Encrypted Before First Use (Not",
         "Media shall be encrypted before first use (not encrypted after data is already written — residual unencrypted data risk)."),
        ("A.7.10-08", "Migration To Hardware Encryption:",
         "Migration to hardware encryption: Software-encrypted exceptions shall be phased out as hardware-encrypted media becomes available (target: all INTERNAL data on hardware encryption within 12 months)."),
        ("A.7.10-09", "Sd/Microsd Cards: Permitted Only For",
         "SD/microSD cards: Permitted only for specific approved purposes (e.g., cameras, embedded systems). Shall be encrypted where the device supports it."),
        ("A.7.10-10", "Unencrypted Removable Media",
         "Unencrypted removable media shall not be used for CONFIDENTIAL data. Exceptions require documented CISO approval with compensating controls and a time limit not exceeding 6 months."),
        ("A.7.10-11", "The Approved Media List",
         "The approved media list shall be reviewed and maintained on a regular cycle:."),
        ("A.7.10-12", "Approval Process: It Operations Proposes",
         "Approval process: IT Operations proposes additions or removals with technical assessment; CISO approves changes; Procurement updates preferred supplier list; approved media list published on intranet and communicated to all staff. List shall include version date and next review date."),
        ("A.7.10-13", "A Risk-Based Audit Of Registered",
         "A risk-based audit of registered removable media shall be conducted quarterly:."),
        ("A.7.10-14", "Audit Results",
         "Audit results shall be documented and retained for 12 months."),
    ]),

    ("Media Use Requirements", [
        ("A.7.10-15", "Transfer Of Confidential Data To",
         "Transfer of CONFIDENTIAL data to removable media requires documented management approval prior to transfer. The approval record shall state the business justification, recipient, and expected return date."),
        ("A.7.10-16", "Data Transferred To Removable Media",
         "All data transferred to removable media shall be encrypted. For CONFIDENTIAL data, AES-256 encryption (hardware or software) is mandatory. For INTERNAL data, AES-128 or stronger is required."),
        ("A.7.10-17", "Transfer Logs",
         "Transfer logs shall be maintained for CONFIDENTIAL data, recording: date, user, media identifier, data description, and recipient."),
        ("A.7.10-18", "Be Removed From Removable Media As",
         "Data shall be removed from removable media as soon as it is no longer needed for the approved purpose."),
        ("A.7.10-19", "Media",
         "Media containing CONFIDENTIAL data shall be password-protected or encrypted with strong authentication (PIN, passphrase, or biometric unlock on the device)."),
        ("A.7.10-20", "Not Be Left Unattended At Any",
         "Media shall not be left unattended at any time. When not in active use, media shall be secured in locked storage appropriate to the classification level."),
        ("A.7.10-21", "Removable Media",
         "Removable media shall not be connected to untrusted or public systems."),
        ("A.7.10-22", "Media Contents",
         "Media contents shall be scanned for malware by [Endpoint Protection Tool] before data is opened or transferred to organisation systems. Auto-run and auto-play shall be disabled on all endpoints via [Endpoint Management Tool] policy."),
        ("A.7.10-23", "Usb Ports And Removable Media Access",
         "USB ports and removable media access shall be managed centrally via [Endpoint Management Tool] (e.g., Group Policy, MDM, or endpoint protection platform)."),
        ("A.7.10-24", "Usb Connection Events",
         "All USB connection events shall be logged by the endpoint protection platform. Logs shall be retained for a minimum of 12 months."),
    ]),

    ("Transportation of Storage Media", [
        ("A.7.10-25", "Confidential Media",
         "CONFIDENTIAL media shall be transported only by approved secure courier services with tracking and signature on delivery. Standard postal services shall not be used for CONFIDENTIAL data."),
        ("A.7.10-26", "Tamper-Evident Packaging",
         "Tamper-evident packaging shall be used for all media containing CONFIDENTIAL data. The recipient shall inspect packaging for evidence of tampering and report any anomalies immediately."),
        ("A.7.10-27", "Chain Of Custody Documentation",
         "Chain of custody documentation shall accompany all shipments of CONFIDENTIAL media (see Chain of Custody section below)."),
        ("A.7.10-28", "Be Carried In Hand Luggage During",
         "Media shall be carried in hand luggage during travel (never in checked baggage)."),
        ("A.7.10-29", "Be Encrypted And",
         "Media shall be encrypted and shall not be left unattended at any time during transport."),
        ("A.7.10-30", "Transport Through High-Risk Areas",
         "Transport through high-risk areas (public transport hubs, conferences, foreign jurisdictions without adequate data protection) should be avoided where alternatives exist. Where unavoidable, additional encryption and access controls shall be applied."),
        ("A.7.10-31", "Courier Instructions For Confidential",
         "Courier instructions for CONFIDENTIAL media: Provide handling instructions to courier; require signature on delivery (no 'leave at door'); track shipment in real time; investigate if delivery delayed >24 hours. Recipient shall inspect packaging for damage upon receipt and report any physical damage immediately."),
        ("A.7.10-32", "Transfers Of Media",
         "All transfers of media containing CONFIDENTIAL data between individuals, locations, or organisations shall be documented with:."),
        ("A.7.10-33", "Chain Of Custody Records",
         "Chain of custody records shall be retained for 7 years."),
        ("A.7.10-34", "Logical Data Transfer Chain Of Custody*",
         "Logical data transfer chain of custody*: Where data is transferred electronically rather than via physical media, chain of custody shall also be documented:."),
    ]),

    ("Storage Requirements", [
        ("A.7.10-35", "Storage Media",
         "Storage media shall be stored in conditions appropriate to both the sensitivity of the information and the physical integrity of the medium:."),
        ("A.7.10-36", "Backup Tapes And Cartridges",
         "Backup tapes and cartridges shall be stored in a separate physical location from the systems they back up (off-site or in a separate fire zone)."),
        ("A.7.10-37", "Backup Media",
         "Backup media shall be encrypted using strong vendor encryption or an organisation-approved encryption tool."),
        ("A.7.10-38", "Backup Media",
         "Backup media shall be included in the media inventory and subject to the same quarterly audit as removable media."),
        ("A.7.10-39", "Be Retained In Accordance With The",
         "Media shall be retained in accordance with the organisation's data retention schedule. Retention periods are defined by data type, regulatory requirement, and business need."),
        ("A.7.10-40", "The Medium",
         "When the retention period for data on a medium expires, the medium shall be sanitised or destroyed per the Disposal section of this policy."),
        ("A.7.10-41", "Backup Tapes And Cloud Snapshots",
         "Backup tapes and cloud snapshots shall have documented disposal or deletion triggers aligned with the retention schedule. 'Indefinite' retention is not permitted without documented CISO approval and annual review."),
        ("A.7.10-42", "Legal Hold Exception*: If Data Subject",
         "Legal hold exception*: If data subject to legal hold (litigation, investigation, audit), backup deletion shall be suspended for affected data. Legal hold documented in [Asset Management System] with hold reason, start date, and review date. Resumption of deletion requires Legal/Compliance approval."),
    ]),

    ("Disposal of Storage Media", [
        ("A.7.10-43", "Disposal And Sanitisation",
         "Disposal and sanitisation shall ensure that information cannot be recovered, using organisation-approved methods appropriate to the media type and the highest classification of data ever stored on the medium."),
        ("A.7.10-44", "Hdd Overwrite — Nist Sp 800-88",
         "HDD overwrite — NIST SP 800-88 Rev. 2 guidance*: NIST SP 800-88 Rev. 2 (September 2025) confirms that a single-pass overwrite is sufficient for modern HDDs (post-2001 manufacturing). Multi-pass overwrite (e.g., legacy DoD 5220.22-M 3-pass or 7-pass methods) is no longer required and provides no additional security benefit on modern drives. Approved Purge methods for HDDs: manufacturer secure erase command (ATA Secure Erase, NVMe Sanitize), or single-pass overwrite with verification using an approved tool (e.g., DBAN, nwipe, shred, or dd). Verification shall include tool completion report with serial number, timestamp, and pass/fail status."),
        ("A.7.10-45", "Degaussing Requirements For Magnetic",
         "Degaussing requirements for magnetic media*: Degaussing effectiveness depends on the magnetic field strength of the degausser relative to the coercivity of the media. The degausser shall be rated for the media type being sanitised:."),
        ("A.7.10-46", "Degausser Validation: Degaussing",
         "Degausser validation: Degaussing equipment shall be tested annually (or per manufacturer recommendations) to verify field strength remains within specification. Testing records shall be retained. SSDs and flash media cannot be degaussed — degaussing has no effect on solid-state storage."),
        ("A.7.10-47", "Cloud And Virtual Storage Disposal*:",
         "Cloud and virtual storage disposal*: Major cloud providers (AWS, Azure, GCP) do not provide individual destruction certificates for virtual storage. For cloud disposal, the organisation shall:."),
        ("A.7.10-48", "Executive Management",
         "Executive Management shall acknowledge reliance on provider-certified deletion processes annually in the Management Review."),
        ("A.7.10-49", "Be Securely Erased Using An Approved",
         "All data shall be securely erased using an approved method appropriate to the previous data classification."),
        ("A.7.10-50", "Be Verified Using [Secure Wipe Tool]",
         "Erasure shall be verified using [Secure Wipe Tool] and the verification log retained."),
        ("A.7.10-51", "Be Inspected For Physical Integrity.",
         "Media shall be inspected for physical integrity. Damaged media shall not be re-used but destroyed."),
        ("A.7.10-52", "[Asset Management System] Records",
         "[Asset Management System] records shall be updated with the new assignment, date, and sanitisation evidence."),
        ("A.7.10-53", "Licensed Software",
         "Licensed software shall be transferred or removed per licensing terms."),
        ("A.7.10-54", "Media Being Disposed Of Externally",
         "Media being disposed of externally shall:."),
        ("A.7.10-55", "Equipment That Has Stored Confidential",
         "Equipment that has stored CONFIDENTIAL data shall not be re-used externally. Storage media shall be physically destroyed before any external transfer."),
        ("A.7.10-56", "A Certificate Of Destruction",
         "A certificate of destruction shall be obtained for every batch or individual item destroyed."),
        ("A.7.10-57", "Reference Individual Serial Numbers Or",
         "Certificates shall reference individual serial numbers or asset tags, not only batch identifiers."),
        ("A.7.10-58", "The Destruction Method And Compliance",
         "The destruction method and compliance standard (e.g., NIST SP 800-88 Destroy, DIN 66399 level) shall be stated."),
        ("A.7.10-59", "Be Matched Against The Handover Record",
         "Certificates shall be matched against the handover record to ensure all items are accounted for. Discrepancies shall be escalated immediately and logged as a security event."),
        ("A.7.10-60", "Be Filed With The Disposal Record",
         "Certificates shall be filed with the disposal record and retained for 7 years."),
    ]),

    ("Paper Documents & Physical", [
        ("A.7.10-61", "Paper Documents",
         "Paper documents shall be classified and handled per the Information Classification and Handling Policy."),
        ("A.7.10-62", "Confidential Documents",
         "CONFIDENTIAL documents shall be stored in locked cabinets or safes when not in immediate active use:."),
        ("A.7.10-63", "Be Collected Immediately From Printers,",
         "Documents shall be collected immediately from printers, copiers, and fax machines. Secure print release (pull printing) should be implemented where available."),
        ("A.7.10-64", "Clean Desk Policy",
         "Clean desk policy shall be followed at all times (see Secure Areas and Media Handling Policy, A.7.6–7–14)."),
        ("A.7.10-65", "Paper Destruction",
         "Paper destruction shall comply with DIN 66399 standards. DIN 66399 defines security levels using a letter prefix for the media category (P = paper) and a number for the security level (1–7, higher = smaller particles):."),
        ("A.7.10-66", "Be Performed On-Site Using",
         "Shredding shall be performed on-site using organisation-owned shredders where possible. For bulk destruction, approved external providers may be used with collection in locked confidential waste bins and certificates of destruction."),
        ("A.7.10-67", "Confidential Waste Bins",
         "Confidential waste bins shall be provided at accessible locations throughout the office. Bins shall be locked and emptied on a scheduled basis by authorised personnel or [Destruction Vendor]."),
        ("A.7.10-68", "Mass Destruction Events (Office Moves,",
         "Mass destruction events (office moves, archive purges) shall be witnessed or certified."),
        ("A.7.10-69", "Follow Din 66399 Media Category F",
         "Destruction shall follow DIN 66399 media category F (film) at security levels corresponding to the classification of the information."),
        ("A.7.10-70", "An Approved External Vendor",
         "Where on-site shredding of film media is not possible, an approved external vendor shall be used."),
    ]),

    ("Optional Payment Card Data", [
        ("A.7.10-71", "The Following Additional Requirements",
         "If PCI DSS scope applies, the following additional requirements shall be met:."),
        ("A.7.10-72", "Media",
         "Media containing cardholder data shall be physically destroyed when no longer needed for business or legal reasons (PCI DSS Requirement 9.4)."),
        ("A.7.10-73", "An Inventory Of Media",
         "An inventory of media containing cardholder data shall be maintained and reconciled at least annually (PCI DSS Requirement 9.4.1)."),
        ("A.7.10-74", "Secure Disposal Of Cardholder Data Media",
         "Secure disposal of cardholder data media shall be documented with destruction certificates (PCI DSS Requirement 9.4.7)."),
        ("A.7.10-75", "Internal And External Transport Of Media",
         "Internal and external transport of media containing cardholder data shall use secure courier and be logged (PCI DSS Requirement 9.4.3–9.4.4)."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.7.10
# =============================================================================
