**ISMS-OP-POL-A.5.14 — Information Transfer**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Transfer |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.14 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.5.14 — Information transfer

**Related Annex A Controls**:

| Control | Relationship to Information Transfer |
|---------|--------------------------------------|
| A.5.10 Acceptable use of information | Acceptable use rules apply to all information transfers |
| A.5.12–13 Information classification and labelling | Classification determines transfer method and encryption requirements |
| A.5.19–23 Supplier relationships | Third-party transfer agreements and cloud service transfers |
| A.5.31 Legal, statutory, regulatory requirements | Cross-border transfer legal requirements (nFADP Art. 16–17) |
| A.5.34 Privacy and protection of PII | Personal data transfer requirements and DPIA triggers |
| A.7.10 Storage media | Removable media management and secure disposal |
| A.8.10 Information deletion | Secure erasure of transferred data from temporary storage and media |
| A.8.13 Information backup | Backup media transport and off-site transfer security |
| A.8.24 Use of cryptography | Encryption standards for data in transit |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Use of Cryptography Policy
- Access Control Policy
- Privacy and Protection of PII Policy
- Asset Management Policy
- Incident Management Policy

---

# Information Transfer Policy

## Purpose

The purpose of this policy is to ensure the correct treatment when transferring information internally and externally and to protect the transfer of information using all types of communication facilities.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) during transfer. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

Information that forms part of systems and applications deemed in scope by the ISO 27001 scope statement.

## Principles

Data transfer shall comply with all applicable legal and regulatory requirements, including Swiss nFADP (revDSG) and, where applicable, the EU GDPR.

Formal agreements that include non-disclosure and confidentiality clauses shall be in place for data sharing with third parties prior to the data transfer.

Personal data shall not be transferred outside Switzerland without a valid legal basis under nFADP Art. 16–17 (adequacy decision, Standard Contractual Clauses, or applicable exception). See the Cross-Border Transfer section below.

No personal or confidential information shall be transferred unencrypted.

All transfers shall be in line with the Information Classification and Handling Policy.

---

## Information Virus Checking

Information that is transferred shall be checked for malware before being sent or before being opened when received. This applies to all electronic transfers including email attachments, file transfers, and removable media.

## Information Encryption

Personal and confidential information shall always be encrypted before being transferred, in line with the Use of Cryptography Policy.

Encryption credentials for username and password, where used, shall be shared via two separate and distinct communication methods. The preferred method is to share the access link or username via email and the password or passphrase via a voice call or secure messaging channel.

## Transfer Agreements

Formal transfer agreements shall be established with all third-party recipients of personal or confidential data. Transfer agreements shall address:

- The parties involved and their data protection roles (controller, processor).
- Categories of data subjects and personal data to be transferred.
- Purpose and legal basis of the transfer.
- Technical and organisational security measures (encryption, access controls, logging).
- Data retention and deletion obligations.
- Breach notification timelines.
- Audit rights.
- Subprocessor controls (where applicable).

Transfer agreements shall be reviewed annually or upon material changes to the transfer arrangement.

---

## Data Transfer Methods

### Preferred Transfer Method

The preferred transfer method for confidential and personal data is an organisation-approved secure file sharing platform (e.g., [encrypted cloud service], secure portal, or managed file transfer solution).

All organisation-approved transfer methods shall support:

- Encryption in transit (TLS 1.2 minimum, TLS 1.3 preferred).
- Access controls and authentication.
- Audit logging of transfers.

### Electronic File Transfer

For automated or bulk file transfers, the following protocols shall be used:

| Protocol | Status |
|----------|--------|
| SFTP (SSH File Transfer Protocol) | Approved — preferred for automated transfers |
| HTTPS | Approved — for web-based file uploads and API transfers |
| FTPS (FTP over TLS) | Approved — where SFTP is not available |
| FTP (unencrypted) | Prohibited |
| SCP | Acceptable — but SFTP preferred |

### Data Transfer by Email

Email is not the preferred method for transferring personal or confidential information, as it is not inherently secure and does not guarantee delivery.

Consideration shall always be given to an alternative secure method of transferring sensitive data wherever possible and practicable.

Email communication shall not be used to transfer unencrypted personal or confidential information.

Where confidential data must be sent via email:

- An encrypted attachment shall be used with a key length that meets the Use of Cryptography Policy requirements (AES-256 minimum).
- The password or decryption key shall be shared via a separate communication channel (voice call, secure messaging).
- Filename or subject line shall not reveal the full contents of attachments or disclose any sensitive personal data.

Email messages containing sensitive transfers shall include clear instructions of the recipient's responsibilities and instructions on what to do if they are not the correct recipient.

The use of personal email accounts for transferring organisation data is prohibited. Where technically feasible, the organisation shall implement controls to prevent forwarding of organisation email to external personal accounts (e.g., mail flow rules, DLP policies, conditional access).

The organisation shall implement email domain authentication (SPF, DKIM, DMARC) to protect against email spoofing and interception. DMARC policy shall be set to **quarantine** or **reject** (not **none**) for production domains.

### Data Transfers by Post or Courier

Data transfers which occur via physical media such as paper reports, memory cards, or external drives shall only be dispatched via an organisation-approved secure courier (a courier service providing tracked, signed-for delivery with tamper-evident packaging and chain of custody documentation, e.g., Swiss Post registered mail, DHL Express with signature, or equivalent). Standard postal services shall not be used for confidential or personal data.

The recipient shall be clearly stated on the parcel and the physical media shall be securely packaged to prevent damage or tampering. Tamper-evident packaging shall be used for confidential material.

The recipient shall be advised in advance that the information is being sent so that they are aware when to expect it. The recipient shall confirm safe receipt as soon as the information arrives. The sender is responsible for confirming the data has arrived safely.

### Data Transfers on Removable Media

Only organisation-owned removable media shall be used for transferring information, in line with the Asset Management Policy. The device shall be approved, recorded in the asset register, assigned to a user, and encrypted (AES-256 full-disk or file-level encryption). Encryption shall be verified by IT before the device is approved for confidential data transfers.

Unencrypted USB drives, personal storage devices, and unapproved cloud storage shall not be used for organisation data transfers.

The removable media shall be returned to the owner on completion of the transfer and the transferred data shall be securely erased from the storage device after use. The asset register shall be updated.

Clear instructions of the recipient's responsibilities and instructions on what to do if they are not the intended recipient shall be given.

Any accompanying message or filename shall not reveal the contents of the media.

The process described for data transfers by post or courier shall be followed for physical dispatch of removable media.

### Telephones, Mobile Phones, and General Conversations

As phone calls may be monitored, overheard, or intercepted (either deliberately or accidentally), care shall be taken as follows:

- Be conscious of your surroundings, especially on public transport and in public places, when discussing personal, confidential, or otherwise sensitive information.
- Personal data shall not be transferred or discussed over the telephone unless you have confirmed the identity and authorisation of the recipient.
- When using voicemail, do not leave sensitive or confidential messages or include any personal data. Only provide a means of contact and wait for the recipient to speak to you personally.
- When listening to voicemail messages, ensure you do not play them in open-plan areas which risk others overhearing. Delete them immediately after listening.

### Data Transfers over Bluetooth

Bluetooth shall not be approved as a communication method for unencrypted confidential, personal, or otherwise sensitive data.

Where Bluetooth is used for approved purposes (e.g., peripherals such as keyboards, headsets):

- Device mutual authentication shall be performed for all connections.
- Encryption shall be enabled for all transmissions.
- Bluetooth Security Mode 4, Level 3 (authenticated encryption) or higher shall be used. Security Modes 1 and 2 are prohibited.
- Devices shall be set to non-discoverable mode when not actively pairing.
- Pairing shall be performed in a secure, non-public area.
- Users shall not accept transmissions of any kind from unknown or suspicious devices.
- Bluetooth file transfer (OBEX) shall be disabled unless specifically approved.
- Bluetooth profiles shall be limited to those required for the approved function.

---

## Cross-Border Data Transfers

Personal data shall not be transferred to a country outside Switzerland unless one of the following conditions is met:

| Safeguard | Description |
|-----------|-------------|
| Adequacy decision | The Swiss Federal Council has determined the destination country provides adequate data protection (Annex 1, DSV). This includes all EU/EEA states, the United Kingdom, and other listed countries. |
| Swiss-US Data Privacy Framework | For US recipients certified under the DPF (effective September 2024). Certification status shall be verified before each transfer. |
| Standard Contractual Clauses | EU SCCs adapted for Swiss nFADP, with Swiss FDPIC as supervisory authority. A Transfer Impact Assessment (TIA) shall be completed. |
| Binding Corporate Rules | Approved by the Swiss FDPIC for intra-group transfers. |
| Explicit consent | Data subject has given explicit, informed consent to the specific transfer after being informed of the risks. |
| Contractual necessity | The transfer is necessary for the performance of a contract with the data subject. |

A register of all cross-border data transfers shall be maintained in the organisation's GRC platform, document management system, or equivalent central location. The register shall document the recipient, destination country, legal basis, safeguards, and review date. The register shall be reviewed annually by the CISO or Data Protection Advisor.

### Transfer Impact Assessment (TIA)

For transfers to countries without an adequacy decision (relying on SCCs or other safeguards), a Transfer Impact Assessment shall be conducted before the transfer commences. The TIA shall evaluate:

- **Legal environment**: Laws in the destination country that may impact data protection (government access, surveillance laws).
- **Practical circumstances**: Whether the recipient is subject to conflicting legal obligations or government data access requests.
- **Technical measures**: Encryption, pseudonymisation, or other safeguards that render data unintelligible to unauthorised parties.
- **Contractual measures**: SCCs, additional contractual clauses, audit rights, data subject remedies.
- **Residual risk**: Whether supplementary measures reduce risk to acceptable levels.

TIA results shall be documented and approved by the CISO or Data Protection Advisor before the transfer is authorised. TIAs shall be reviewed annually or when circumstances change (legal changes in destination country, security incident).

---

## Lost or Missing Information

If it is discovered or suspected that information has been lost, is missing, did not arrive, or has gone to the wrong person, then the employee or third-party user shall immediately inform their line manager and the information security management team. The Incident Management process shall be followed.

Lost or misdirected information shall be classified as:

- **Critical**: Involves sensitive personal data, confidential commercial data, or creates high risk to data subjects (potential breach notification required under nFADP).
- **High**: Involves personal data or confidential information but limited data subjects or volume.
- **Medium**: Involves internal or non-confidential data with no personal data.

The individual who sent the data is responsible for initiating the incident report and cooperating with the investigation.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **Transfer agreement register** (third-party agreements with review dates) — *reviewed annually; updated upon new agreements*
- **Cross-border transfer register** (destinations, legal bases, safeguards) — *reviewed annually by CISO/DPA; updated upon new transfers*
- **Secure file transfer logs** (SFTP, HTTPS, cloud sharing platform) — *retained for 12 months; reviewed quarterly for anomalies*
- **Email domain authentication records** (SPF, DKIM, DMARC configuration and compliance reports) — *DMARC reports reviewed monthly*
- **Removable media inventory and assignment records** — *updated per event; reconciled semi-annually with asset register*
- **Courier dispatch and receipt confirmation logs** — *retained for 12 months*
- **Incident reports** related to lost or misdirected information — *retained per incident management policy*
- **Transfer Impact Assessments** (for non-adequate country transfers) — *reviewed annually or upon legal changes in destination country*
- **Data transfer log** (electronic transfers of confidential or personal data) — *retained for 12 months; accessible for audit*

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, transfer log audits, agreement reviews, incident reports, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to data transfer standards, emerging threats, regulatory changes (including Swiss adequacy list updates), and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Information Transfer Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | **5.14 Information transfer** |
| Clause 7.5.3 Control of documented information | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 7.10 Storage media |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures; Art. 16–17 — Cross-border transfers |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum data security requirements; Annex 1 — Adequacy list |
| EU GDPR (where applicable) | Art. 32 — Security of processing; Art. 44–49 — International transfers |
| ISO/IEC 27001:2022 | Annex A Control 5.14 — Information transfer |
| ISO/IEC 27002:2022 | Section 5.14 — Implementation guidance for information transfer |
| NIST SP 800-53 Rev 5 | SC-8 (Transmission Confidentiality and Integrity), MP-5 (Media Transport) |
| CIS Controls v8 | Control 3 (Data Protection — Safeguard 3.10: Encrypt Sensitive Data in Transit) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
