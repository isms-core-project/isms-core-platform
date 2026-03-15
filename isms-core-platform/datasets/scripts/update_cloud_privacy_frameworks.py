"""
update_cloud_privacy_frameworks.py

Populates controls arrays for:
  - iso27017_cloud.json      (ISO/IEC 27017:2015 — 7 new CLD + 5 CSP/CSC adapted)
  - iso27018_pii_cloud.json  (ISO/IEC 27018:2019 — 16 thematic controls)
  - iso27701_privacy.json    (ISO/IEC 27701:2025 — management clauses + Annex A/B/C)

Existing crosswalk UUIDs are preserved exactly.
Additional controls get deterministic UUIDs from uuid5(NAMESPACE_URL, stable_key).
"""

import json
import uuid
import hashlib
from datetime import timezone, datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
CROSSWALK_FILE = DATA_DIR / "crosswalk.json"

NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")  # NAMESPACE_URL

def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(NS, key))

def content_hash(controls: list) -> str:
    return hashlib.sha1(json.dumps(controls, sort_keys=True).encode()).hexdigest()

# Load crosswalk to extract existing UUIDs
crosswalk = json.load(open(CROSSWALK_FILE))
existing: dict[str, str] = {}  # "FRAMEWORK|control_id" → uuid
for obj in crosswalk["objects"]:
    fw = obj.get("target_framework", "")
    cid = obj.get("target_control_id") or obj.get("target_control")
    cuuid = obj.get("target_control_uuid", "")
    if fw and cid and cuuid:
        existing[f"{fw}|{cid}"] = cuuid

def get_uuid(framework: str, control_id: str) -> str:
    key = f"{framework}|{control_id}"
    return existing.get(key) or stable_uuid(f"isms-core-dataset-{framework}-{control_id}")

# ─────────────────────────────────────────────────────────────────────────────
# ISO/IEC 27017:2015
# 7 brand-new CLD controls + 5 CSP/CSC adapted controls from crosswalk
# ─────────────────────────────────────────────────────────────────────────────

ISO27017_CONTROLS = [
    # ── 7 New Cloud-Specific Controls (CLD prefix) ──────────────────────────
    {
        "control_id": "CLD.6.3.1",
        "category": "New Cloud Controls",
        "title": "Shared roles and responsibilities within a cloud computing environment",
        "description": (
            "Roles and responsibilities of cloud service providers and cloud service customers "
            "shall be defined, documented and communicated. Both parties must understand who is "
            "responsible for each security function within the shared responsibility model."
        ),
        "applicability": "CSP and Customer",
        "notes": "New control — not present in ISO 27002. Unique to cloud environments.",
    },
    {
        "control_id": "CLD.8.1.5",
        "category": "New Cloud Controls",
        "title": "Removal and return of assets upon contract termination",
        "description": (
            "When a cloud service contract ends, the cloud service provider shall return or "
            "securely destroy the cloud service customer's assets. Procedures for asset return, "
            "secure deletion, and data remanence prevention shall be agreed contractually."
        ),
        "applicability": "CSP and Customer",
        "notes": "New control — not present in ISO 27002.",
    },
    {
        "control_id": "CLD.9.5.1",
        "category": "New Cloud Controls",
        "title": "Segregation in virtual computing environments",
        "description": (
            "Virtual computing environments shall be protected and segregated to prevent "
            "unauthorised access between cloud service customers. Isolation mechanisms shall "
            "ensure one customer cannot access another customer's environment or data."
        ),
        "applicability": "CSP",
        "notes": "New control — not present in ISO 27002.",
    },
    {
        "control_id": "CLD.9.5.2",
        "category": "New Cloud Controls",
        "title": "Virtual machine hardening",
        "description": (
            "Virtual machine images shall be hardened in accordance with organisation policy "
            "before deployment. Hardening shall cover removal of unnecessary services, "
            "application of security baselines, and validation of configuration integrity."
        ),
        "applicability": "CSP and Customer",
        "notes": "New control — not present in ISO 27002.",
    },
    {
        "control_id": "CLD.12.1.5",
        "category": "New Cloud Controls",
        "title": "Administrator's operational security",
        "description": (
            "Administrative operations and procedures in cloud environments shall be documented "
            "and applied consistently. Privileged administrative access shall be controlled, "
            "logged and regularly reviewed to prevent unauthorised operations."
        ),
        "applicability": "CSP",
        "notes": "New control — not present in ISO 27002.",
    },
    {
        "control_id": "CLD.12.4.5",
        "category": "New Cloud Controls",
        "title": "Monitoring of cloud services",
        "description": (
            "Cloud service customers shall have the ability to monitor their use of cloud "
            "services. Providers shall make available sufficient logging and monitoring data "
            "to allow customers to verify security status and investigate incidents."
        ),
        "applicability": "CSP and Customer",
        "notes": "New control — not present in ISO 27002.",
    },
    {
        "control_id": "CLD.13.1.4",
        "category": "New Cloud Controls",
        "title": "Alignment of security management for virtual and physical networks",
        "description": (
            "Security management for virtual networks shall be aligned with physical network "
            "security policies and procedures. Network segregation, access control, and "
            "monitoring shall apply consistently across physical and virtual network boundaries."
        ),
        "applicability": "CSP",
        "notes": "New control — not present in ISO 27002.",
    },

    # ── Cloud-Adapted ISO 27002 Controls (CSP/CSC prefix) ───────────────────
    {
        "control_id": "CSP.6.1",
        "category": "Cloud-Adapted Controls",
        "title": "Information security roles and responsibilities in cloud environments",
        "description": (
            "Information security roles and responsibilities shall be defined and allocated "
            "with explicit consideration of cloud-specific functions, including responsibilities "
            "under the shared responsibility model for the cloud deployment type in use."
        ),
        "applicability": "CSP",
        "notes": "Cloud-specific implementation of ISO 27002 organisational controls.",
    },
    {
        "control_id": "CSC.9.1",
        "category": "Cloud-Adapted Controls",
        "title": "Access control policy for cloud service customers",
        "description": (
            "Cloud service customers shall implement access control policies appropriate "
            "for cloud environments, including identity and access management for cloud "
            "resources, privileged access management, and federated identity where applicable."
        ),
        "applicability": "Customer",
        "notes": "Cloud-specific implementation of ISO 27002 access control.",
    },
    {
        "control_id": "CSP.12.1",
        "category": "Cloud-Adapted Controls",
        "title": "Capacity and availability management for cloud services",
        "description": (
            "Cloud service providers shall manage capacity to ensure agreed service availability "
            "levels. Resource allocation, elasticity mechanisms, and availability monitoring "
            "shall be implemented and communicated to cloud service customers."
        ),
        "applicability": "CSP",
        "notes": "Cloud-specific implementation of ISO 27002 operations security.",
    },
    {
        "control_id": "CSP.16.1",
        "category": "Cloud-Adapted Controls",
        "title": "Notification of security incidents affecting cloud customers",
        "description": (
            "Cloud service providers shall notify affected cloud service customers of security "
            "incidents without undue delay. Notification shall include sufficient information "
            "for customers to assess impact and take protective action on their own systems."
        ),
        "applicability": "CSP",
        "notes": "Cloud-specific implementation of ISO 27002 incident management.",
    },
    {
        "control_id": "CSC.13.1",
        "category": "Cloud-Adapted Controls",
        "title": "Protection of data in cloud services",
        "description": (
            "Cloud service customers shall identify and implement appropriate controls to "
            "protect data stored in and transmitted to/from cloud services, including "
            "encryption, data residency controls, and secure deletion procedures."
        ),
        "applicability": "Customer",
        "notes": "Cloud-specific implementation of ISO 27002 communications security.",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# ISO/IEC 27018:2019
# 16 thematic control areas — PII in public cloud (PII processor focus)
# ─────────────────────────────────────────────────────────────────────────────

ISO27018_CONTROLS = [
    {
        "control_id": "A.1",
        "category": "Consent and Choice",
        "title": "Consent and choice",
        "description": (
            "PII processing shall only occur for purposes to which the PII principal has "
            "consented. PII shall not be used for direct marketing or advertising without "
            "explicit consent. Mechanisms shall exist for principals to withdraw consent."
        ),
    },
    {
        "control_id": "A.2",
        "category": "Purpose Legitimacy",
        "title": "Purpose legitimacy and specification",
        "description": (
            "The purposes for which PII is processed shall be specified and communicated "
            "to PII principals. PII shall be processed only for legitimate, specified "
            "purposes and not retained beyond the period necessary for those purposes."
        ),
    },
    {
        "control_id": "A.3",
        "category": "Collection Limitation",
        "title": "Collection limitation",
        "description": (
            "Collection of PII shall be limited to the minimum necessary for the specified "
            "purpose. PII shall be collected by lawful and fair means, and where appropriate, "
            "with the knowledge or consent of the PII principal."
        ),
    },
    {
        "control_id": "A.4",
        "category": "Data Minimisation",
        "title": "Data minimisation",
        "description": (
            "PII shall be minimised — only data adequate, relevant and limited to what "
            "is necessary in relation to the purposes for which it is processed shall be "
            "retained. Regular reviews of data holdings shall be conducted."
        ),
    },
    {
        "control_id": "A.5",
        "category": "Use, Retention and Disclosure",
        "title": "Use, retention and disclosure limitation",
        "description": (
            "PII shall not be disclosed, made available, or used for purposes other than "
            "those specified except with the consent of the PII principal or as required "
            "by applicable law. Retention periods shall be defined and enforced."
        ),
    },
    {
        "control_id": "A.6",
        "category": "Accuracy and Quality",
        "title": "Accuracy and quality",
        "description": (
            "PII shall be accurate, complete, and kept up to date as necessary for the "
            "purposes for which it is used. Procedures shall exist for PII principals to "
            "correct inaccurate personal data held by the organisation."
        ),
    },
    {
        "control_id": "A.7",
        "category": "Openness and Transparency",
        "title": "Openness, transparency and notice",
        "description": (
            "PII principals shall be informed about the collection and use of their PII, "
            "including identity of the controller, purposes of processing, sub-processors "
            "used, data residency locations, and applicable rights."
        ),
    },
    {
        "control_id": "A.8",
        "category": "Individual Participation",
        "title": "Individual participation and access",
        "description": (
            "PII principals shall have the right to access their personal data, request "
            "corrections, and request erasure where appropriate. Mechanisms shall be "
            "implemented to handle such requests within defined timeframes."
        ),
    },
    {
        "control_id": "A.9",
        "category": "Accountability",
        "title": "Accountability",
        "description": (
            "The cloud service provider (as PII processor) shall be accountable for "
            "compliance with applicable privacy obligations. Records of processing activities "
            "shall be maintained and made available to competent authorities on request."
        ),
    },
    {
        "control_id": "A.10.1",
        "category": "Sub-processor Obligations",
        "title": "Information security obligations for sub-processors",
        "description": (
            "Contractual obligations for PII protection shall flow down to all sub-processors. "
            "Cloud service providers shall ensure sub-processors provide sufficient guarantees "
            "and shall be accountable for their sub-processors' compliance."
        ),
    },
    {
        "control_id": "A.10.2",
        "category": "Business Continuity",
        "title": "Business continuity for PII",
        "description": (
            "Business continuity plans shall include provisions for the protection of PII "
            "during disruptive events. Recovery procedures shall ensure PII integrity and "
            "availability are restored in accordance with contractual obligations."
        ),
    },
    {
        "control_id": "A.10.3",
        "category": "Incident Response",
        "title": "Incident response for PII breaches",
        "description": (
            "Procedures shall exist for detecting, reporting, and responding to PII-related "
            "security incidents. Cloud service providers shall notify affected customers "
            "without undue delay to enable compliance with breach notification obligations."
        ),
    },
    {
        "control_id": "A.10.4",
        "category": "Encryption",
        "title": "Encryption and key management for PII",
        "description": (
            "PII shall be protected by encryption both in transit and at rest where "
            "appropriate to the risk. Key management procedures shall ensure encryption "
            "keys remain under the control of the appropriate party (customer or provider)."
        ),
    },
    {
        "control_id": "A.10.5",
        "category": "Access Control",
        "title": "Access control for PII",
        "description": (
            "Access to PII shall be restricted on a need-to-know basis. Privileged access "
            "to systems processing PII shall be controlled, logged, and regularly reviewed. "
            "Physical and logical access controls shall prevent unauthorised PII access."
        ),
    },
    {
        "control_id": "A.11.1",
        "category": "Compliance Monitoring",
        "title": "Privacy compliance monitoring",
        "description": (
            "Compliance with privacy obligations shall be regularly monitored and reviewed. "
            "Audits of PII processing activities shall be conducted and results reported "
            "to senior management. Non-conformities shall be addressed with corrective action."
        ),
    },
    {
        "control_id": "A.11.2",
        "category": "Cross-Border Transfers",
        "title": "Cross-border PII transfer controls",
        "description": (
            "Transfers of PII across national or jurisdictional boundaries shall only "
            "occur where adequate protections exist. The legal basis for each transfer "
            "shall be identified and documented, and data residency commitments honoured."
        ),
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# ISO/IEC 27701:2025
# Management clauses (4–10) + Annex A.1 Controller + Annex A.2 Processor
# + Annex A.3 Information Security Controls
# ─────────────────────────────────────────────────────────────────────────────

ISO27701_CONTROLS = [
    # ── Management System Clauses (cross-ref to crosswalk UUIDs) ────────────
    {
        "control_id": "5.2.1",
        "category": "Management System",
        "title": "Understanding the organisation and its context (privacy)",
        "description": "Extends ISO 27001 clause 4.1 with privacy-specific context requirements.",
        "applicability": "Controller, Processor",
        "clause_ref": "4.1",
    },
    {
        "control_id": "5.4.1",
        "category": "Management System",
        "title": "Privacy risk assessment",
        "description": "Extends ISO 27001 clause 6.1.2 with privacy risk identification and assessment.",
        "applicability": "Controller, Processor",
        "clause_ref": "6.1.2",
    },
    {
        "control_id": "6.2.1",
        "category": "Annex A — PII Controller",
        "title": "PII inventories",
        "description": "Maintain inventories of all categories of PII processed.",
        "applicability": "Controller",
        "clause_ref": "A.1.2",
    },
    {
        "control_id": "6.2.2",
        "category": "Annex A — PII Controller",
        "title": "Determining privacy roles and responsibilities",
        "description": "Define and document roles of PII controller and any joint controllers.",
        "applicability": "Controller",
        "clause_ref": "A.1.2.8",
    },
    {
        "control_id": "6.3.1",
        "category": "Annex A — PII Controller",
        "title": "Privacy by design and by default",
        "description": "Implement privacy by design principles and data minimisation by default.",
        "applicability": "Controller",
        "clause_ref": "A.1.4",
    },
    {
        "control_id": "6.4.1",
        "category": "Annex A — PII Controller",
        "title": "PII principal consent management",
        "description": "Implement mechanisms to obtain, record and manage PII principal consent.",
        "applicability": "Controller",
        "clause_ref": "A.1.2.4",
    },
    {
        "control_id": "6.5.1",
        "category": "Annex A — PII Controller",
        "title": "PII principal rights support",
        "description": "Implement mechanisms to support PII principals in exercising their rights.",
        "applicability": "Controller",
        "clause_ref": "A.1.3",
    },
    {
        "control_id": "7.11.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Supplier relationships for PII processing",
        "description": "Ensure PII protection obligations are addressed in supplier agreements.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.10",
    },
    {
        "control_id": "7.12.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Information security incident management for PII breaches",
        "description": "Manage PII-related incidents with appropriate notification procedures.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.11",
    },
    {
        "control_id": "7.14.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Privacy compliance and review",
        "description": "Regularly review compliance with privacy obligations and PIMS requirements.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.15",
    },
    {
        "control_id": "7.2.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Information security policies for PII",
        "description": "Establish and maintain information security policies covering PII protection.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.3",
    },
    {
        "control_id": "7.3.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Human resource security and privacy",
        "description": "Ensure personnel are aware of privacy obligations and PII handling requirements.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.17",
    },
    {
        "control_id": "7.4.1",
        "category": "Annex A — Controller IS Controls",
        "title": "PII asset management",
        "description": "Identify and manage assets containing PII including classification and labelling.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.5",
    },
    {
        "control_id": "7.5.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Access control for PII (controller)",
        "description": "Control access to PII based on need-to-know and least privilege principles.",
        "applicability": "Controller",
        "clause_ref": "A.3.9",
    },
    {
        "control_id": "7.8.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Operations security for PII",
        "description": "Implement operational controls including backup, logging and monitoring for PII.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.24",
    },
    {
        "control_id": "7.9.1",
        "category": "Annex A — Controller IS Controls",
        "title": "Communications security for PII",
        "description": "Protect PII in transfer through encryption and secure transmission controls.",
        "applicability": "Controller, Processor",
        "clause_ref": "A.3.7",
    },
    {
        "control_id": "8.2.1",
        "category": "Annex A.2 — PII Processor",
        "title": "Contractual obligations for PII processors",
        "description": "Process PII only on documented instructions from the controller.",
        "applicability": "Processor",
        "clause_ref": "A.2.2.2",
    },
    {
        "control_id": "8.4.1",
        "category": "Annex A.2 — PII Processor",
        "title": "Temporary files and copies of PII",
        "description": "Ensure temporary files containing PII are securely deleted after use.",
        "applicability": "Processor",
        "clause_ref": "A.2.4.2",
    },
    {
        "control_id": "8.5.1",
        "category": "Annex A.2 — PII Processor",
        "title": "Processor security obligations",
        "description": "Implement all security obligations agreed with the PII controller.",
        "applicability": "Processor",
        "clause_ref": "A.2.2.6",
    },

    # ── Additional PIMS Management Clauses (new UUIDs) ───────────────────────
    *[
        {
            "control_id": cid,
            "category": "Management System",
            "title": title,
            "description": desc,
            "applicability": "Controller, Processor",
        }
        for cid, title, desc in [
            ("4.2", "Understanding the needs and expectations of interested parties",
             "Identify interested parties relevant to the PIMS and their privacy-related requirements."),
            ("4.3", "Determining the scope of the PIMS",
             "Define the scope of the Privacy Information Management System in relation to the ISMS."),
            ("5.1", "Leadership and commitment to PIMS",
             "Top management shall demonstrate leadership and commitment with respect to the PIMS."),
            ("5.2", "Privacy Policy",
             "Top management shall establish a privacy policy aligned with the organisation's context."),
            ("5.3", "Roles, responsibilities and authorities for PIMS",
             "Define and communicate roles and responsibilities for privacy management."),
            ("6.1.1", "General actions to address privacy risks and opportunities",
             "Determine risks and opportunities relevant to privacy and plan actions to address them."),
            ("6.1.2", "Privacy risk assessment",
             "Perform privacy risk assessments at planned intervals and when significant changes occur."),
            ("6.1.3", "Privacy risk treatment",
             "Select and implement privacy risk treatment options including controls from Annex A."),
            ("6.2", "Privacy objectives and planning",
             "Establish privacy objectives consistent with the privacy policy and plan how to achieve them."),
            ("6.3", "Planning of changes to the PIMS",
             "Carry out changes to the PIMS in a planned manner, considering purpose and consequences."),
            ("7.1", "Resources for PIMS",
             "Determine and provide resources needed for establishment and continual improvement of the PIMS."),
            ("7.2", "Competence for PIMS",
             "Ensure personnel are competent on the basis of appropriate education, training and experience."),
            ("7.3", "Awareness of PIMS",
             "Ensure personnel are aware of the privacy policy and their contribution to PIMS effectiveness."),
            ("7.4", "Communication on PIMS",
             "Determine internal and external communications relevant to the PIMS."),
            ("8.1", "Operational planning and control",
             "Plan, implement and control processes needed to meet PIMS requirements."),
            ("8.2", "Privacy risk assessment (operational)",
             "Perform privacy risk assessments at planned intervals and when significant changes are proposed."),
            ("8.3", "Privacy risk treatment (operational)",
             "Implement the privacy risk treatment plan and retain documented information of results."),
            ("9.1", "Monitoring, measurement, analysis and evaluation",
             "Evaluate privacy performance and the effectiveness of the PIMS."),
            ("9.2.1", "Internal audit — General",
             "Conduct internal audits at planned intervals to determine PIMS conformance."),
            ("9.2.2", "Internal audit programme",
             "Plan, establish, implement and maintain audit programmes for the PIMS."),
            ("9.3.1", "Management review — General",
             "Top management shall review the PIMS at planned intervals."),
            ("9.3.2", "Management review inputs",
             "The management review shall consider status of actions from previous reviews and relevant changes."),
            ("9.3.3", "Management review results",
             "Management review results shall include decisions on continual improvement opportunities."),
            ("10.1", "Continual improvement",
             "Continually improve the suitability, adequacy and effectiveness of the PIMS."),
            ("10.2", "Nonconformity and corrective action",
             "React to nonconformity by taking action to control and correct it, and deal with consequences."),
        ]
    ],

    # ── Annex A.1 — PII Controller Controls ─────────────────────────────────
    *[
        {
            "control_id": cid,
            "category": "Annex A.1 — PII Controller",
            "title": title,
            "description": desc,
            "applicability": "Controller",
        }
        for cid, title, desc in [
            ("A.1.2.2", "Identify and document purpose",
             "Identify and document the specific purposes for which PII is to be processed."),
            ("A.1.2.3", "Identify lawful basis",
             "Identify and document the lawful basis for processing each category of PII."),
            ("A.1.2.4", "Determine when and how consent is to be obtained",
             "Determine the circumstances and method for obtaining PII principal consent."),
            ("A.1.2.5", "Obtain and record consent",
             "Obtain consent in a manner that is freely given, specific, informed and unambiguous."),
            ("A.1.2.6", "Privacy impact assessment",
             "Conduct a privacy impact assessment when processing is likely to result in high risk."),
            ("A.1.2.7", "Contracts with PII processors",
             "Ensure contracts with PII processors include all required data processing terms."),
            ("A.1.2.8", "Joint PII controller",
             "Where joint controllership exists, define respective responsibilities in an arrangement."),
            ("A.1.2.9", "Records related to processing PII",
             "Maintain records of processing activities as required by applicable law."),
            ("A.1.3.2", "Determining and fulfilling obligations to PII principals",
             "Identify and fulfil all obligations owed to PII principals under applicable law."),
            ("A.1.3.3", "Determining information for PII principals",
             "Determine what information must be provided to PII principals about processing."),
            ("A.1.3.4", "Providing information to PII principals",
             "Provide PII principals with required information in a concise, transparent manner."),
            ("A.1.3.5", "Providing mechanism to modify or withdraw consent",
             "Implement an easy mechanism for PII principals to modify or withdraw consent."),
            ("A.1.3.6", "Providing mechanism to object to PII processing",
             "Provide PII principals with a mechanism to object to certain types of processing."),
            ("A.1.3.7", "Access, correction or erasure",
             "Respond to requests for access, correction or erasure of PII within required timeframes."),
            ("A.1.3.8", "PII controllers' obligations to inform third parties",
             "Where PII has been disclosed to third parties, inform them of corrections or erasures."),
            ("A.1.3.9", "Providing copy of PII processed",
             "Provide PII principals with a copy of their PII upon request."),
            ("A.1.3.10", "Handling requests",
             "Establish procedures for handling PII principal rights requests efficiently."),
            ("A.1.3.11", "Automated decision making",
             "Provide safeguards for automated decision-making including right to human review."),
            ("A.1.4.2", "Limit collection",
             "Limit collection of PII to that which is adequate, relevant and not excessive."),
            ("A.1.4.3", "Limit processing",
             "Limit processing of PII to that necessary for the specified and lawful purposes."),
            ("A.1.4.4", "Accuracy and quality",
             "Ensure PII is accurate and kept up to date to the extent necessary for its purpose."),
            ("A.1.4.5", "PII minimization objectives",
             "Define and implement objectives for minimising the volume of PII processed."),
            ("A.1.4.6", "PII de-identification and deletion at end of processing",
             "De-identify or delete PII when the processing purpose has been fulfilled."),
            ("A.1.4.7", "Temporary files",
             "Ensure temporary files containing PII are identified and deleted when no longer needed."),
            ("A.1.4.8", "Retention",
             "Define and implement retention schedules for all categories of PII processed."),
            ("A.1.4.9", "Disposal",
             "Securely dispose of PII in accordance with retention schedules and applicable law."),
            ("A.1.4.10", "PII transmission controls",
             "Control transmission of PII including use of encryption and secure transmission channels."),
            ("A.1.5.2", "Identify basis for PII transfer between jurisdictions",
             "Identify and document the legal basis for each cross-border transfer of PII."),
            ("A.1.5.3", "Countries and international organizations to which PII can be transferred",
             "Document which countries/international organizations PII may be transferred to and why."),
            ("A.1.5.4", "Records of transfer of PII",
             "Maintain records of all PII transfers between jurisdictions."),
            ("A.1.5.5", "Records of PII disclosures to third parties",
             "Maintain records of all disclosures of PII to third parties."),
        ]
    ],

    # ── Annex A.2 — PII Processor Controls ──────────────────────────────────
    *[
        {
            "control_id": cid,
            "category": "Annex A.2 — PII Processor",
            "title": title,
            "description": desc,
            "applicability": "Processor",
        }
        for cid, title, desc in [
            ("A.2.2.2", "Customer agreement",
             "Process PII only in accordance with customer instructions documented in a contract."),
            ("A.2.2.3", "Organisation's purposes",
             "Do not use PII received from customers for the processor's own business purposes."),
            ("A.2.2.4", "Marketing and advertising use",
             "Do not use customer PII for marketing or advertising without explicit permission."),
            ("A.2.2.5", "Infringing instruction",
             "Inform the customer if a processing instruction is believed to infringe applicable law."),
            ("A.2.2.6", "Customer obligations",
             "Assist the customer in fulfilling their obligations to PII principals."),
            ("A.2.2.7", "Records related to processing PII",
             "Maintain records of processing activities on behalf of the controller."),
            ("A.2.3.2", "Comply with obligations to PII principals",
             "Assist the controller in responding to PII principal rights requests."),
            ("A.2.4.2", "Temporary files",
             "Ensure temporary files created during processing are securely deleted after use."),
            ("A.2.4.3", "Return, transfer or disposal of PII",
             "At contract end, return or securely delete all PII processed on behalf of the controller."),
            ("A.2.4.4", "PII transmission controls",
             "Protect PII in transit using appropriate encryption and secure transmission controls."),
            ("A.2.5.2", "Basis for PII transfer between jurisdictions",
             "Only transfer PII across jurisdictions where an adequate legal basis exists."),
            ("A.2.5.3", "Countries and international organizations to which PII can be transferred",
             "Process PII only in jurisdictions approved by the controller."),
            ("A.2.5.4", "Records of PII disclosures to third parties",
             "Maintain records of any PII disclosures made to third parties."),
            ("A.2.5.5", "Notification of PII disclosure requests",
             "Notify the controller of any requests to disclose PII from authorities."),
            ("A.2.5.6", "Legally binding PII disclosures",
             "Where legally required to disclose PII, notify the controller unless prohibited."),
            ("A.2.5.7", "Disclosure of subcontractors used to process PII",
             "Disclose to the controller all sub-processors used to process their PII."),
            ("A.2.5.8", "Engagement of a subcontractor to process PII",
             "Obtain controller authorisation before engaging a sub-processor."),
            ("A.2.5.9", "Change of subcontractor to process PII",
             "Notify the controller of intended changes to sub-processors and allow time to object."),
        ]
    ],

    # ── Annex A.3 — Information Security Controls (Controller + Processor) ───
    *[
        {
            "control_id": cid,
            "category": "Annex A.3 — Information Security",
            "title": title,
            "description": desc,
            "applicability": "Controller, Processor",
        }
        for cid, title, desc in [
            ("A.3.3", "Policies for information security",
             "Establish information security policies that include specific provisions for PII protection."),
            ("A.3.4", "Information security roles and responsibilities",
             "Assign and communicate information security roles with explicit PII responsibilities."),
            ("A.3.5", "Classification of information",
             "Classify information assets including PII according to legal protection requirements."),
            ("A.3.6", "Labelling of information",
             "Implement procedures for labelling information assets that contain PII."),
            ("A.3.7", "Information transfer",
             "Implement policies for information transfer that address PII transmission requirements."),
            ("A.3.8", "Identity management",
             "Manage identities of all users who have access to systems processing PII."),
            ("A.3.9", "Access rights",
             "Assign, review and revoke access rights to PII based on the principle of least privilege."),
            ("A.3.10", "Information security in supplier agreements",
             "Address PII protection requirements in all supplier and service provider agreements."),
            ("A.3.11", "Information security incident management planning",
             "Plan and prepare for information security incidents involving PII."),
            ("A.3.12", "Response to information security incidents",
             "Respond to incidents involving PII with appropriate notification and remediation."),
            ("A.3.13", "Legal, statutory, regulatory and contractual requirements",
             "Identify and address all legal and regulatory requirements relating to PII."),
            ("A.3.14", "Protection of records",
             "Protect records containing PII from loss, destruction, falsification and unauthorised access."),
            ("A.3.15", "Independent review of information security",
             "Undertake independent reviews of PII protection measures at planned intervals."),
            ("A.3.16", "Compliance with policies, rules and standards",
             "Regularly review compliance with PII-related information security policies."),
            ("A.3.17", "Information security awareness, education and training",
             "Provide privacy and PII-specific awareness training to all relevant personnel."),
            ("A.3.18", "Confidentiality or non-disclosure agreements",
             "Require confidentiality agreements covering PII from all personnel with access."),
            ("A.3.19", "Clear desk and clear screen",
             "Implement clear desk and screen policies that address PII protection requirements."),
            ("A.3.20", "Storage media",
             "Manage storage media containing PII through its lifecycle including secure disposal."),
            ("A.3.21", "Secure disposal or re-use of equipment",
             "Ensure PII is securely removed from equipment before disposal or re-use."),
            ("A.3.22", "User endpoint devices",
             "Protect PII on user endpoint devices through encryption and access controls."),
            ("A.3.23", "Secure authentication",
             "Implement secure authentication for systems that process PII."),
            ("A.3.24", "Information backup",
             "Back up PII in accordance with retention requirements and test restoration procedures."),
            ("A.3.25", "Logging",
             "Log access to PII and processing activities to support accountability and incident response."),
            ("A.3.26", "Use of cryptography",
             "Apply cryptographic controls to protect PII in accordance with applicable requirements."),
            ("A.3.27", "Secure development life cycle",
             "Integrate privacy requirements into the software development lifecycle."),
            ("A.3.28", "Application security requirements",
             "Define and implement application security requirements that protect PII."),
            ("A.3.29", "Secure system architecture and engineering principles",
             "Apply privacy by design principles in system architecture and engineering."),
            ("A.3.30", "Outsourced development",
             "Ensure outsourced development activities address PII protection requirements."),
            ("A.3.31", "Test information",
             "Protect PII used in testing environments with appropriate access and deletion controls."),
        ]
    ],
]


def build_controls(framework_code: str, raw_controls: list) -> list:
    """Add UUIDs (preserving existing crosswalk UUIDs) and return cleaned list."""
    out = []
    for c in raw_controls:
        cid = c["control_id"]
        entry = {
            "id": get_uuid(framework_code, cid),
            "control_id": cid,
            "title": c["title"],
            "category": c.get("category", ""),
            "description": c.get("description", ""),
        }
        if "applicability" in c:
            entry["applicability"] = c["applicability"]
        if "notes" in c:
            entry["notes"] = c["notes"]
        if "clause_ref" in c:
            entry["clause_ref"] = c["clause_ref"]
        out.append(entry)
    return out


def update_file(filename: str, framework_code: str, raw_controls: list, version_override: str | None = None):
    path = DATA_DIR / filename
    data = json.load(open(path))

    controls = build_controls(framework_code, raw_controls)
    data["controls"] = controls

    if version_override:
        data["framework"]["version"] = version_override
        data["framework"]["name"] = data["framework"]["name"].replace("2019", "2025")
        data["framework"]["source_url"] = "https://www.iso.org/standard/71670.html"

    data["content_hash"] = content_hash(controls)
    data["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data["objects_count"] = len(controls)

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓  {filename}: {len(controls)} controls written")


if __name__ == "__main__":
    update_file("iso27017_cloud.json",     "ISO27017", ISO27017_CONTROLS)
    update_file("iso27018_pii_cloud.json", "ISO27018", ISO27018_CONTROLS)
    update_file("iso27701_privacy.json",   "ISO27701", ISO27701_CONTROLS, version_override="2025")
    print("\nDone. Re-run 'Load Reference Frameworks' in the WebUI to push changes to the DB.")
