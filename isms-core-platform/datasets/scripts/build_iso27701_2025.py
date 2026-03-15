"""
build_iso27701_2025.py

Generates iso27701_privacy.json with the complete ISO/IEC 27701:2025 (Ed. 2)
control structure from Annex A (normative):
  - Table A.1 — 31 controls for PII controllers
  - Table A.2 — 18 controls for PII processors
  - Table A.3 — 29 security controls for both

Preserves existing framework UUID and bundle ID. Replaces all 2019 controls
(7.x, A.x.x, B.x.x) with the 2025 three-table structure.

Usage:
    python3 datasets/scripts/build_iso27701_2025.py [--dry-run]

Source: ISO/IEC 27701:2025(en), Annex A (normative), pp. 15–20.
"""

import argparse
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "datasets" / "data"
OUT_FILE = DATA_DIR / "iso27701_privacy.json"

# Same namespace as update_cloud_privacy_frameworks.py
NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

FRAMEWORK_ID = "50aabf3b-a713-525a-b7f7-2e4a6a06b3f0"
BUNDLE_ID = "bundle--10986a78-f676-5b60-a946-26fe327d78d1"
FRAMEWORK_CODE = "ISO27701"


def uid(control_id: str) -> str:
    return str(uuid.uuid5(NS, f"isms-core-dataset-{FRAMEWORK_CODE}-{control_id}"))


# ─────────────────────────────────────────────────────────────────────────────
# TABLE A.1 — PII CONTROLLERS
# ─────────────────────────────────────────────────────────────────────────────

TABLE_A1_GROUPS = [
    {
        "control_id": "A.1.2",
        "title": "Conditions for collection and processing",
        "objective": (
            "To demonstrate that processing is lawful, with legal basis as per applicable "
            "jurisdictions, with clearly defined and legitimate purposes."
        ),
    },
    {
        "control_id": "A.1.3",
        "title": "Obligations to PII principals",
        "objective": (
            "To ensure that PII principals are provided with appropriate information about the "
            "processing of their PII, and to meet any other applicable obligations to PII "
            "principals related to the processing of their PII."
        ),
    },
    {
        "control_id": "A.1.4",
        "title": "Privacy by design and privacy by default",
        "objective": (
            "To ensure that processes and systems are designed such that the collection and "
            "processing of PII (including use, disclosure, retention, transmission and disposal) "
            "are limited to what is necessary for the identified purpose."
        ),
    },
    {
        "control_id": "A.1.5",
        "title": "PII sharing, transfer and disclosure",
        "objective": (
            "To determine whether, and document when, PII is shared, transferred to other "
            "jurisdictions or third parties or disclosed in accordance with applicable obligations."
        ),
    },
]

TABLE_A1_CONTROLS = [
    # ── A.1.2 Conditions for collection and processing ───────────────────────
    {
        "control_id": "A.1.2.2",
        "group": "A.1.2",
        "title": "Identify and document purpose",
        "description": (
            "The organisation shall identify and document the specific purposes for which the "
            "PII will be processed."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.2.3",
        "group": "A.1.2",
        "title": "Identify lawful basis",
        "description": (
            "The organisation shall determine, document and be able to demonstrate compliance "
            "with the relevant lawful basis for the processing of PII for the identified purposes."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.2.4",
        "group": "A.1.2",
        "title": "Determine when and how consent is to be obtained",
        "description": (
            "The organisation shall determine and document a process by which it can demonstrate "
            "if, when and how consent for the processing of PII was obtained from PII principals."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.2.5",
        "group": "A.1.2",
        "title": "Obtain and record consent",
        "description": (
            "The organisation shall obtain and record consent from PII principals according to "
            "the documented processes."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.2.6",
        "group": "A.1.2",
        "title": "Privacy impact assessment",
        "description": (
            "The organisation shall assess the need for, and implement where appropriate, a "
            "privacy impact assessment whenever new processing of PII or changes to existing "
            "processing of PII is planned."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.2.7",
        "group": "A.1.2",
        "title": "Contracts with PII processors",
        "description": (
            "The organisation shall have a written contract with any PII processor that it uses, "
            "and shall ensure that their contracts with PII processors address the implementation "
            "of the appropriate controls in Annex A (Table A.2)."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.2.8",
        "group": "A.1.2",
        "title": "Joint PII controller",
        "description": (
            "The organisation shall determine respective roles and responsibilities for the "
            "processing of PII (including PII protection and security requirements) with any "
            "joint PII controller."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.2.9",
        "group": "A.1.2",
        "title": "Records related to processing PII",
        "description": (
            "The organisation shall determine and securely maintain the necessary records in "
            "support of its obligations for the processing of PII."
        ),
        "applies_to": "controller",
    },
    # ── A.1.3 Obligations to PII principals ──────────────────────────────────
    {
        "control_id": "A.1.3.2",
        "group": "A.1.3",
        "title": "Determining and fulfilling obligations to PII principals",
        "description": (
            "The organisation shall determine and document its legal, regulatory and business "
            "obligations to PII principals related to the processing of their PII and provide "
            "the means to meet these obligations."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.3",
        "group": "A.1.3",
        "title": "Determining information for PII principals",
        "description": (
            "The organisation shall determine and document the information to be provided to PII "
            "principals regarding the processing of their PII and the timing of such a provision."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.4",
        "group": "A.1.3",
        "title": "Providing information to PII principals",
        "description": (
            "The organisation shall provide PII principals with clear and easily accessible "
            "information identifying the PII controller and describing the processing of their PII."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.5",
        "group": "A.1.3",
        "title": "Providing mechanism to modify or withdraw consent",
        "description": (
            "The organisation shall provide a mechanism for PII principals to modify or withdraw "
            "their consent."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.6",
        "group": "A.1.3",
        "title": "Providing mechanism to object to PII processing",
        "description": (
            "The organisation shall provide a mechanism for PII principals to object to the "
            "processing of their PII."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.7",
        "group": "A.1.3",
        "title": "Access, correction or erasure",
        "description": (
            "The organisation shall implement policies, procedures or mechanisms to meet its "
            "obligations to PII principals to access, correct or erase their PII."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.8",
        "group": "A.1.3",
        "title": "PII controllers' obligations to inform third parties",
        "description": (
            "The organisation shall inform third parties with whom PII has been shared of any "
            "modification, withdrawal or objections pertaining to the shared PII, and implement "
            "appropriate policies, procedures or mechanisms to do so."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.9",
        "group": "A.1.3",
        "title": "Providing copy of PII processed",
        "description": (
            "The organisation shall be able to provide a copy of the PII that is processed, "
            "when requested by the PII principal."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.10",
        "group": "A.1.3",
        "title": "Handling requests",
        "description": (
            "The organisation shall define and document policies and procedures for handling "
            "and responding to legitimate requests from PII principals."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.3.11",
        "group": "A.1.3",
        "title": "Automated decision making",
        "description": (
            "The organisation shall identify obligations, including legal obligations, to the "
            "PII principals resulting from decisions made by the organisation which are related "
            "to the PII principal based solely on automated processing of PII, and be able to "
            "demonstrate how it addresses these obligations."
        ),
        "applies_to": "controller",
    },
    # ── A.1.4 Privacy by design and privacy by default ───────────────────────
    {
        "control_id": "A.1.4.2",
        "group": "A.1.4",
        "title": "Limit collection",
        "description": (
            "The organisation shall limit the collection of PII to the minimum that is relevant, "
            "proportional and necessary for the identified purposes."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.3",
        "group": "A.1.4",
        "title": "Limit processing",
        "description": (
            "The organisation shall limit the processing of PII to that which is adequate, "
            "relevant and necessary for the identified purposes."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.4",
        "group": "A.1.4",
        "title": "Accuracy and quality",
        "description": (
            "The organisation shall ensure and document that PII is as accurate, complete and "
            "up to date as necessary for the purposes for which it is processed, throughout the "
            "life cycle of the PII."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.5",
        "group": "A.1.4",
        "title": "PII minimisation objectives",
        "description": (
            "The organisation shall define and document data minimisation objectives and what "
            "mechanisms (such as de-identification) are used to meet those objectives."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.6",
        "group": "A.1.4",
        "title": "PII de-identification and deletion at the end of processing",
        "description": (
            "The organisation shall either delete PII or render it in a form which does not "
            "permit identification or re-identification of PII principals, as soon as the "
            "original PII is no longer necessary for the identified purpose(s)."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.7",
        "group": "A.1.4",
        "title": "Temporary files",
        "description": (
            "The organisation shall ensure that temporary files created as a result of the "
            "processing of PII are disposed of (e.g. erased or destroyed) following documented "
            "procedures within a specified, documented period."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.8",
        "group": "A.1.4",
        "title": "Retention",
        "description": (
            "The organisation shall not retain PII for longer than is necessary for the purposes "
            "for which the PII is processed."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.9",
        "group": "A.1.4",
        "title": "Disposal",
        "description": (
            "The organisation shall have documented policies, procedures or mechanisms for the "
            "disposal of PII."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.4.10",
        "group": "A.1.4",
        "title": "PII transmission controls",
        "description": (
            "The organisation shall subject PII transmitted (e.g. sent to another organisation) "
            "over a data-transmission network to appropriate controls designed to ensure that "
            "the data reaches its intended destination."
        ),
        "applies_to": "controller",
    },
    # ── A.1.5 PII sharing, transfer and disclosure ───────────────────────────
    {
        "control_id": "A.1.5.2",
        "group": "A.1.5",
        "title": "Identify basis for PII transfer between jurisdictions",
        "description": (
            "The organisation shall identify and document the relevant basis for transfers of "
            "PII between jurisdictions."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.5.3",
        "group": "A.1.5",
        "title": "Countries and international organisations to which PII can be transferred",
        "description": (
            "The organisation shall specify and document the countries and international "
            "organisations to which PII can possibly be transferred."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.5.4",
        "group": "A.1.5",
        "title": "Records of transfer of PII",
        "description": (
            "The organisation shall record transfers of PII to or from third parties and ensure "
            "cooperation with those parties to support future requests related to obligations "
            "to the PII principals."
        ),
        "applies_to": "controller",
    },
    {
        "control_id": "A.1.5.5",
        "group": "A.1.5",
        "title": "Records of PII disclosures to third parties",
        "description": (
            "The organisation shall record disclosures of PII to third parties, including which "
            "PII has been disclosed, to whom and at what time."
        ),
        "applies_to": "controller",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# TABLE A.2 — PII PROCESSORS
# ─────────────────────────────────────────────────────────────────────────────

TABLE_A2_GROUPS = [
    {
        "control_id": "A.2.2",
        "title": "Conditions for collection and processing",
        "objective": (
            "To demonstrate that processing is lawful, with legal basis as per applicable "
            "jurisdictions, and with clearly defined and legitimate purposes."
        ),
    },
    {
        "control_id": "A.2.3",
        "title": "Obligations to PII principals",
        "objective": (
            "To ensure that PII principals are provided with the appropriate information about "
            "the processing of their PII, and to meet any other applicable obligations to PII "
            "principals related to the processing of their PII."
        ),
    },
    {
        "control_id": "A.2.4",
        "title": "Privacy by design and privacy by default",
        "objective": (
            "To ensure that processes and systems are designed such that the collection and "
            "processing of PII are limited to what is necessary for the identified purpose."
        ),
    },
    {
        "control_id": "A.2.5",
        "title": "PII sharing, transfer and disclosure",
        "objective": (
            "To determine whether, and document when, PII is shared, transferred to other "
            "jurisdictions or third parties, or disclosed according to applicable obligations."
        ),
    },
]

TABLE_A2_CONTROLS = [
    # ── A.2.2 Conditions for collection and processing ───────────────────────
    {
        "control_id": "A.2.2.2",
        "group": "A.2.2",
        "title": "Customer agreement",
        "description": (
            "The organisation shall ensure, where relevant, that the contract to process PII "
            "addresses the organisation's role in providing assistance with the customer's "
            "obligations (taking into account the nature of processing and the information "
            "available to the organisation)."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.2.3",
        "group": "A.2.2",
        "title": "Organisation's purposes",
        "description": (
            "The organisation shall ensure that PII processed on behalf of a customer are only "
            "processed for the purposes expressed in the documented instructions of the customer."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.2.4",
        "group": "A.2.2",
        "title": "Marketing and advertising use",
        "description": (
            "The organisation shall not use PII processed under a contract for the purposes of "
            "marketing and advertising without establishing that prior consent was obtained from "
            "the appropriate PII principal. The organisation shall not make providing such "
            "consent a condition for receiving the service."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.2.5",
        "group": "A.2.2",
        "title": "Infringing instruction",
        "description": (
            "The organisation shall inform the customer if, in its opinion, a processing "
            "instruction infringes applicable legal requirements."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.2.6",
        "group": "A.2.2",
        "title": "Customer obligations",
        "description": (
            "The organisation shall provide the customer with the appropriate information such "
            "that the customer can demonstrate compliance with their obligations."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.2.7",
        "group": "A.2.2",
        "title": "Records related to processing PII",
        "description": (
            "The organisation shall determine and maintain the necessary records in support of "
            "demonstrating compliance with its obligations (as specified in the applicable "
            "contract) for the processing of PII carried out on behalf of a customer."
        ),
        "applies_to": "processor",
    },
    # ── A.2.3 Obligations to PII principals ──────────────────────────────────
    {
        "control_id": "A.2.3.2",
        "group": "A.2.3",
        "title": "Comply with obligations to PII principals",
        "description": (
            "The organisation shall provide the customer with the means to comply with its "
            "obligations related to PII principals."
        ),
        "applies_to": "processor",
    },
    # ── A.2.4 Privacy by design and privacy by default ───────────────────────
    {
        "control_id": "A.2.4.2",
        "group": "A.2.4",
        "title": "Temporary files",
        "description": (
            "The organisation shall ensure that temporary files created as a result of the "
            "processing of PII are disposed of (e.g. erased or destroyed) following documented "
            "procedures within a specified, documented period."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.4.3",
        "group": "A.2.4",
        "title": "Return, transfer or disposal of PII",
        "description": (
            "The organisation shall be able to return, transfer or dispose of PII in a secure "
            "manner. It shall also make its policy available to the customer."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.4.4",
        "group": "A.2.4",
        "title": "PII transmission controls",
        "description": (
            "The organisation shall subject PII transmitted over a data-transmission network "
            "to appropriate controls, which are designed to ensure that the data reaches its "
            "intended destination."
        ),
        "applies_to": "processor",
    },
    # ── A.2.5 PII sharing, transfer and disclosure ───────────────────────────
    {
        "control_id": "A.2.5.2",
        "group": "A.2.5",
        "title": "Basis for PII transfer between jurisdictions",
        "description": (
            "The organisation shall inform the customer in a timely manner of the basis for PII "
            "transfers between jurisdictions and of any intended changes in this regard, so that "
            "the customer can object to such changes or terminate the contract."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.5.3",
        "group": "A.2.5",
        "title": "Countries and international organisations to which PII can be transferred",
        "description": (
            "The organisation shall specify and document the countries and international "
            "organisations to which PII can possibly be transferred."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.5.4",
        "group": "A.2.5",
        "title": "Records of PII disclosures to third parties",
        "description": (
            "The organisation shall record disclosures of PII to third parties, including which "
            "PII has been disclosed, to whom and when."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.5.5",
        "group": "A.2.5",
        "title": "Notification of PII disclosure requests",
        "description": (
            "The organisation shall notify the customer of any legally binding requests for "
            "disclosure of PII."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.5.6",
        "group": "A.2.5",
        "title": "Legally binding PII disclosures",
        "description": (
            "The organisation shall reject any requests for PII disclosures that are not legally "
            "binding, consult the corresponding customer before making any PII disclosures and "
            "accept any contractually agreed requests for PII disclosures that are authorised "
            "by the corresponding customer."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.5.7",
        "group": "A.2.5",
        "title": "Disclosure of subcontractors used to process PII",
        "description": (
            "Before use, the organisation shall disclose whether any subcontractors are used "
            "to process PII to the customer."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.5.8",
        "group": "A.2.5",
        "title": "Engagement of a subcontractor to process PII",
        "description": (
            "The organisation shall only engage a subcontractor to process PII according to "
            "the customer contract."
        ),
        "applies_to": "processor",
    },
    {
        "control_id": "A.2.5.9",
        "group": "A.2.5",
        "title": "Change of subcontractor to process PII",
        "description": (
            "The organisation shall, in the case of having general written authorisation, inform "
            "the customer of any intended changes concerning the addition or replacement of "
            "subcontractors to process PII, thereby giving the customer the opportunity to "
            "object to such changes."
        ),
        "applies_to": "processor",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# TABLE A.3 — SECURITY CONTROLS (BOTH PII CONTROLLERS AND PII PROCESSORS)
# Maps to ISO/IEC 27002:2022 controls via Annex B cross-reference
# ─────────────────────────────────────────────────────────────────────────────

TABLE_A3_CONTROLS = [
    {
        "control_id": "A.3.3",
        "title": "Policies for information security",
        "description": (
            "Information security policies related to PII processing shall be defined, approved "
            "by management, published, communicated to and acknowledged by relevant personnel "
            "and relevant interested parties, and reviewed at planned intervals and if "
            "significant changes occur."
        ),
        "maps_to_iso27002": ["5.1"],
    },
    {
        "control_id": "A.3.4",
        "title": "Information security roles and responsibilities",
        "description": (
            "Information security roles and responsibilities related to PII processing shall be "
            "defined and allocated according to the organisational needs."
        ),
        "maps_to_iso27002": ["5.2", "5.4"],
    },
    {
        "control_id": "A.3.5",
        "title": "Classification of information",
        "description": (
            "Information shall be classified according to the information security needs of the "
            "organisation, taking into consideration PII, based on confidentiality, integrity, "
            "availability and relevant interested party requirements."
        ),
        "maps_to_iso27002": ["5.12"],
    },
    {
        "control_id": "A.3.6",
        "title": "Labelling of information",
        "description": (
            "An appropriate set of procedures for information labelling that considers PII shall "
            "be developed and implemented in accordance with the information classification "
            "scheme adopted by the organisation."
        ),
        "maps_to_iso27002": ["5.13"],
    },
    {
        "control_id": "A.3.7",
        "title": "Information transfer",
        "description": (
            "Information transfer rules, procedures, or agreements related to processing PII "
            "shall be in place for all types of transfer facilities within the organisation "
            "and between the organisation and other parties."
        ),
        "maps_to_iso27002": ["5.14"],
    },
    {
        "control_id": "A.3.8",
        "title": "Identity management",
        "description": (
            "The full life cycle of identities related to PII processing shall be managed."
        ),
        "maps_to_iso27002": ["5.16"],
    },
    {
        "control_id": "A.3.9",
        "title": "Access rights",
        "description": (
            "Access rights to PII and other associated assets related to PII processing shall "
            "be provisioned, reviewed, modified and removed in accordance with the organisation's "
            "topic-specific policy on and rules for access control."
        ),
        "maps_to_iso27002": ["5.18"],
    },
    {
        "control_id": "A.3.10",
        "title": "Addressing information security within supplier agreements",
        "description": (
            "Relevant information security requirements related to PII processing shall be "
            "established and agreed with each supplier based on the type of supplier relationship."
        ),
        "maps_to_iso27002": ["5.20"],
    },
    {
        "control_id": "A.3.11",
        "title": "Information security incident management planning and preparation",
        "description": (
            "The organisation shall plan and prepare for managing information security incidents "
            "related to PII processing by defining, establishing and communicating incident "
            "management processes, roles and responsibilities."
        ),
        "maps_to_iso27002": ["5.24"],
    },
    {
        "control_id": "A.3.12",
        "title": "Response to information security incidents",
        "description": (
            "Responses to information security incidents related to PII processing shall be "
            "according to the documented procedures."
        ),
        "maps_to_iso27002": ["5.26"],
    },
    {
        "control_id": "A.3.13",
        "title": "Legal, statutory, regulatory and contractual requirements",
        "description": (
            "Legal, statutory, regulatory and contractual requirements relevant to information "
            "security related to PII processing and the organisation's approach to meet these "
            "requirements shall be documented and this documentation kept up to date."
        ),
        "maps_to_iso27002": ["5.31"],
    },
    {
        "control_id": "A.3.14",
        "title": "Protection of records",
        "description": (
            "Records related to PII processing shall be protected from loss, destruction, "
            "falsification, unauthorised access and unauthorised release."
        ),
        "maps_to_iso27002": ["5.33"],
    },
    {
        "control_id": "A.3.15",
        "title": "Independent review of information security",
        "description": (
            "The organisation's approach to managing information security related to PII "
            "processing and its implementation including people, processes and technologies "
            "shall be reviewed independently at planned intervals, or when significant "
            "changes occur."
        ),
        "maps_to_iso27002": ["5.35"],
    },
    {
        "control_id": "A.3.16",
        "title": "Compliance with policies, rules and standards for information security",
        "description": (
            "Compliance with the organisation's information security policy, topic-specific "
            "policies, rules and standards related to PII processing shall be regularly reviewed."
        ),
        "maps_to_iso27002": ["5.36"],
    },
    {
        "control_id": "A.3.17",
        "title": "Information security awareness, education and training",
        "description": (
            "Personnel of the organisation and relevant interested parties shall receive "
            "appropriate information security awareness education and training, and regular "
            "updates of the organisation's information security policy, topic-specific policies "
            "and procedures, as relevant for their job function, as they relate to PII processing."
        ),
        "maps_to_iso27002": ["6.3"],
    },
    {
        "control_id": "A.3.18",
        "title": "Confidentiality or non-disclosure agreements",
        "description": (
            "Confidentiality or non-disclosure agreements reflecting the organisation's needs "
            "for the protection of PII shall be identified, documented, regularly reviewed and "
            "signed by personnel and other relevant interested parties."
        ),
        "maps_to_iso27002": ["6.6"],
    },
    {
        "control_id": "A.3.19",
        "title": "Clear desk and clear screen",
        "description": (
            "Clear desk rules for papers and removable storage media and clear screen rules for "
            "information processing facilities shall be defined and appropriately enforced."
        ),
        "maps_to_iso27002": ["7.7"],
    },
    {
        "control_id": "A.3.20",
        "title": "Storage media",
        "description": (
            "Storage media with PII shall be managed through its life cycle of acquisition, "
            "use, transportation and disposal in accordance with the organisation's "
            "classification scheme and handling requirements."
        ),
        "maps_to_iso27002": ["7.10"],
    },
    {
        "control_id": "A.3.21",
        "title": "Secure disposal or re-use of equipment",
        "description": (
            "Items of equipment containing storage media with PII shall be verified to ensure "
            "that any sensitive data and licensed software has been removed or securely "
            "overwritten prior to disposal or re-use."
        ),
        "maps_to_iso27002": ["7.14"],
    },
    {
        "control_id": "A.3.22",
        "title": "User endpoint devices",
        "description": (
            "PII stored on, processed by or accessible via user endpoint devices shall be "
            "protected."
        ),
        "maps_to_iso27002": ["8.1"],
    },
    {
        "control_id": "A.3.23",
        "title": "Secure authentication",
        "description": (
            "Secure authentication technologies and procedures related to PII processing shall "
            "be implemented based on information access restrictions."
        ),
        "maps_to_iso27002": ["8.5"],
    },
    {
        "control_id": "A.3.24",
        "title": "Information backup",
        "description": (
            "Backup copies of PII, and software and systems related to PII processing shall be "
            "maintained and regularly tested."
        ),
        "maps_to_iso27002": ["8.13"],
    },
    {
        "control_id": "A.3.25",
        "title": "Logging",
        "description": (
            "Logs that record activities, exceptions, faults and other relevant events related "
            "to PII processing shall be produced, stored, protected and analysed."
        ),
        "maps_to_iso27002": ["8.15"],
    },
    {
        "control_id": "A.3.26",
        "title": "Use of cryptography",
        "description": (
            "Rules for the effective use of cryptography related to PII processing, including "
            "cryptographic key management, shall be defined and implemented."
        ),
        "maps_to_iso27002": ["8.24"],
    },
    {
        "control_id": "A.3.27",
        "title": "Secure development life cycle",
        "description": (
            "Rules for the secure development of software and systems related to PII processing "
            "shall be established and applied."
        ),
        "maps_to_iso27002": ["8.25"],
    },
    {
        "control_id": "A.3.28",
        "title": "Application security requirements",
        "description": (
            "Information security requirements related to PII processing shall be identified, "
            "specified and approved when developing or acquiring applications."
        ),
        "maps_to_iso27002": ["8.26"],
    },
    {
        "control_id": "A.3.29",
        "title": "Secure system architecture and engineering principles",
        "description": (
            "Principles for engineering secure systems related to processing PII shall be "
            "established, documented, maintained and applied to any information system "
            "development activities."
        ),
        "maps_to_iso27002": ["8.27"],
    },
    {
        "control_id": "A.3.30",
        "title": "Outsourced development",
        "description": (
            "The organisation shall direct, monitor and review the activities related to "
            "outsourced PII processing system development."
        ),
        "maps_to_iso27002": ["8.30"],
    },
    {
        "control_id": "A.3.31",
        "title": "Test information",
        "description": (
            "Test information related to PII processing shall be appropriately selected, "
            "protected and managed."
        ),
        "maps_to_iso27002": ["8.33"],
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# BUILD OBJECTS ARRAY
# ─────────────────────────────────────────────────────────────────────────────

def build_objects() -> list:
    objects = []
    sort = 1000

    def next_sort():
        nonlocal sort
        v = sort
        sort += 100
        return v

    # Top-level table sections (level 0)
    tables = [
        ("A.1", "Table A.1 — Controls for PII controllers",
         "Normative control objectives and controls applicable to organisations acting as "
         "PII controllers. Contains 31 controls across four groups: conditions for collection "
         "and processing, obligations to PII principals, privacy by design, and PII sharing."),
        ("A.2", "Table A.2 — Controls for PII processors",
         "Normative control objectives and controls applicable to organisations acting as "
         "PII processors on behalf of a customer. Contains 18 controls across four groups: "
         "conditions for processing, obligations to PII principals, privacy by design, and "
         "PII sharing and disclosure."),
        ("A.3", "Table A.3 — Security controls for PII controllers and PII processors",
         "Normative information security controls applicable to all organisations processing "
         "PII, whether as controllers or processors. Contains 29 controls aligned with "
         "ISO/IEC 27002:2022 controls, adapted for PII processing contexts."),
    ]
    for cid, title, desc in tables:
        objects.append({
            "type": "framework_control",
            "id": uid(cid),
            "framework_id": FRAMEWORK_ID,
            "control_id": cid,
            "title": title,
            "description": desc,
            "level": 0,
            "sort_order": next_sort(),
        })

    # Table A.1 groups (level 1) + controls (level 2)
    a1_group_sort = {g["control_id"]: i for i, g in enumerate(TABLE_A1_GROUPS)}
    for g in TABLE_A1_GROUPS:
        objects.append({
            "type": "framework_control",
            "id": uid(g["control_id"]),
            "framework_id": FRAMEWORK_ID,
            "control_id": g["control_id"],
            "title": g["title"],
            "description": g["objective"],
            "level": 1,
            "parent_id": "A.1",
            "sort_order": next_sort(),
            "metadata": {"role": "objective_group"},
        })
    for ctrl in TABLE_A1_CONTROLS:
        meta = {"applies_to": ctrl["applies_to"]}
        objects.append({
            "type": "framework_control",
            "id": uid(ctrl["control_id"]),
            "framework_id": FRAMEWORK_ID,
            "control_id": ctrl["control_id"],
            "title": ctrl["title"],
            "description": ctrl["description"],
            "level": 2,
            "parent_id": ctrl["group"],
            "sort_order": next_sort(),
            "metadata": meta,
        })

    # Table A.2 groups (level 1) + controls (level 2)
    for g in TABLE_A2_GROUPS:
        objects.append({
            "type": "framework_control",
            "id": uid(g["control_id"]),
            "framework_id": FRAMEWORK_ID,
            "control_id": g["control_id"],
            "title": g["title"],
            "description": g["objective"],
            "level": 1,
            "parent_id": "A.2",
            "sort_order": next_sort(),
            "metadata": {"role": "objective_group"},
        })
    for ctrl in TABLE_A2_CONTROLS:
        meta = {"applies_to": ctrl["applies_to"]}
        objects.append({
            "type": "framework_control",
            "id": uid(ctrl["control_id"]),
            "framework_id": FRAMEWORK_ID,
            "control_id": ctrl["control_id"],
            "title": ctrl["title"],
            "description": ctrl["description"],
            "level": 2,
            "parent_id": ctrl["group"],
            "sort_order": next_sort(),
            "metadata": meta,
        })

    # Table A.3 controls (level 1 — flat, single group)
    for ctrl in TABLE_A3_CONTROLS:
        meta = {
            "applies_to": "both",
            "maps_to_iso27002_2022": ctrl.get("maps_to_iso27002", []),
        }
        objects.append({
            "type": "framework_control",
            "id": uid(ctrl["control_id"]),
            "framework_id": FRAMEWORK_ID,
            "control_id": ctrl["control_id"],
            "title": ctrl["title"],
            "description": ctrl["description"],
            "level": 1,
            "parent_id": "A.3",
            "sort_order": next_sort(),
            "metadata": meta,
        })

    return objects


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    objects = build_objects()

    # Counts
    controllers = [o for o in objects if o.get("metadata", {}).get("applies_to") == "controller"]
    processors = [o for o in objects if o.get("metadata", {}).get("applies_to") == "processor"]
    both = [o for o in objects if o.get("metadata", {}).get("applies_to") == "both"]
    groups = [o for o in objects if o.get("metadata", {}).get("role") == "objective_group"]
    tables = [o for o in objects if o.get("level") == 0]

    print(f"Tables:  {len(tables)}")
    print(f"Groups:  {len(groups)}")
    print(f"Controls — A.1 (controllers): {len(controllers)}")
    print(f"Controls — A.2 (processors):  {len(processors)}")
    print(f"Controls — A.3 (both):        {len(both)}")
    print(f"Total objects: {len(objects)}")

    ch = hashlib.sha1(json.dumps(objects, sort_keys=True).encode()).hexdigest()

    bundle = {
        "bundle_id": "bundle--10986a78-f676-5b60-a946-26fe327d78d1",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "2.0",
        "framework": {
            "id": FRAMEWORK_ID,
            "code": FRAMEWORK_CODE,
            "name": "ISO/IEC 27701:2025 — Privacy Information Management",
            "version": "2025",
            "publisher": "ISO/IEC",
            "source_url": "https://www.iso.org/standard/71670.html",
            "jurisdiction": None,
            "description": (
                "Standalone Privacy Information Management System (PIMS) standard. "
                "Second edition (published 2025-10-14) is a complete structural rewrite "
                "from the 2019 first edition (which was an extension to ISO/IEC 27001/27002). "
                "2025 edition defines PIMS as an independent management system with three "
                "normative annexes: Annex A (control objectives and controls — 31 for PII "
                "controllers, 18 for PII processors, 29 security controls for both), "
                "Annex B (implementation guidance), plus informative annexes mapping to "
                "ISO/IEC 29100 (C), GDPR (D), ISO/IEC 27018+29151 (E), and 2019 "
                "correspondence (F)."
            ),
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "build_iso27701_2025.py",
        "content_hash": ch,
        "objects_count": len(objects),
        "relationships_count": 0,
        "objects": objects,
        "relationships": [],
    }

    print(f"\nContent hash: {ch}")

    if args.dry_run:
        print("\n--dry-run: no file written.")
        return

    OUT_FILE.write_text(json.dumps(bundle, indent=2, ensure_ascii=False))
    print(f"\nWritten: {OUT_FILE}")
    print(f"Size: {OUT_FILE.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
