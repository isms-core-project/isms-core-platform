<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.17-19-TG:privacy:TG:a.3.17-19 -->
**PRIV-IMP-A.3.17-19-TG — Privacy Awareness, NDAs and Clear Desk — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Awareness, NDAs and Clear Desk — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.17-19-TG |
| **Related Policy** | PRIV-POL-A.3.17-19 (Privacy Awareness, NDAs and Clear Desk) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or technical change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.17-19 (Privacy Awareness, NDAs and Clear Desk — the governing policy)
- PRIV-IMP-A.3.17-19-UG (Privacy Awareness, NDAs and Clear Desk — User Guide)
- PRIV-IMP-A.3.23-31-TG (Technical Security Controls — screen lock and endpoint configuration standards)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, curriculum content, and configuration standards** for privacy awareness, confidentiality agreements, and clear desk/screen controls. It covers:

- Personnel Privacy Training and Acknowledgment Register schema
- Privacy training curriculum content requirements by tier
- Confidentiality Agreement Register schema
- Minimum PII NDA clause checklist
- Screen lock and privacy screen configuration standards
- Workspace Inspection Record template
- Remote Working Clear Desk Acknowledgment template

**Audience**: DPO, HR Manager, CISO, IT Security Team, Legal.

---

## 1. Personnel Privacy Training and Acknowledgment Register

The register is maintained by the DPO with HR support. It records all privacy training completions and policy acknowledgments.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Record ID | Text | Unique reference (e.g., TRAIN-2026-001) |
| Personnel ID | Text | Employee/contractor ID — linked to Identity Register |
| Full Name | Text | Name of individual |
| Role / Department | Text | Current role and business unit |
| Personnel Category | Enum | Employee / Contractor / Temporary / External Advisor |
| Training Tier | Enum | Tier 1 (All Personnel) / Tier 2 (PII Handler) / Tier 3 (Elevated Role) / Tier 4 (DPO/Privacy Function) |
| Training Module | Text | Module name and version (e.g., "Privacy Awareness v2.1") |
| Training Type | Enum | Annual Refresher / Induction / Policy Update Acknowledgment / Role Change / Supplementary |
| Completion Date | Date | Date training or acknowledgment completed |
| Delivery Method | Enum | E-learning / Workshop / Briefing / Self-study with Acknowledgment |
| Outcome | Enum | Completed / Pass (where assessed) / Fail / Pending |
| Next Required Date | Date | Date by which next refresher or acknowledgment is due |
| Recorded By | Text | Name of person recording completion |
| Notes | Text | Exceptional circumstances, extensions granted, escalations |

### Minimum Records at First Certification

All active personnel with PII access must have:
- At minimum one Tier 1 (general privacy awareness) completion record dated within the past 12 months
- Tier 2 or Tier 3 records as applicable to their role, within the past 12 months
- Policy acknowledgment record for all major PIMS policies relevant to their role

---

## 2. Privacy Training Curriculum Content Requirements

### Tier 1 — All Personnel (General Privacy Awareness)

Minimum content requirements for annual general privacy awareness:

| Topic | Minimum Content |
|-------|----------------|
| What is PII? | Definition; examples of ordinary, special category, and sensitive PII; why it matters |
| [Organisation]'s legal obligations | Overview of GDPR and FADP obligations (not exhaustive — headline duties) |
| Individual responsibility | Handling rules: classification, transfer restrictions, clean desk/screen |
| Recognising PII incidents | What to report; how to report; escalation to Privacy Champion / DPO |
| Data subject rights | Overview of rights; how to escalate requests to DPO |
| Consequences | Regulatory penalties; disciplinary consequences of PII mishandling |

Delivery: E-learning module with completion tracking. Assessment: minimum pass rate where assessment is included (recommended). Duration: 20–30 minutes.

### Tier 2 — Personnel with PII Access (Role-Appropriate Training)

In addition to Tier 1, personnel with direct PII access receive:

| Topic | Minimum Content |
|-------|----------------|
| PII handling in their role | Specific handling rules relevant to the PII datasets they access |
| Lawful basis and purpose limitation | Applicable lawful bases for their processing activities; no secondary use |
| Data minimisation | Only collect/access what is necessary; do not retain beyond purpose |
| Access control obligations | Not sharing credentials; reporting unexpected access |
| Transfer and disclosure | When they may share PII; permitted recipients; prohibited disclosures |
| Incident response | Their specific escalation steps if they suspect a breach |

Delivery: Role-specific briefing or e-learning module (can be combined with Tier 1). Duration: additional 15–20 minutes.

### Tier 3 — Elevated PII Roles (Data Owners, Privacy Champions, System Owners)

In addition to Tiers 1 and 2, elevated roles receive training covering:

| Topic | Minimum Content |
|-------|----------------|
| PIMS control group responsibilities | The specific control groups relevant to their role (policy + implementation obligations) |
| Access rights certification | How to conduct access rights reviews for their datasets |
| DPIA obligations | When to trigger a DPIA; their role in the DPIA process |
| Data subject rights handling | Their role in responding to rights requests |
| Incident management | Their role in the Privacy Incident Response Plan |

Delivery: Structured workshop or guided self-study with acknowledgment sign-off. Frequency: on appointment to role + annual refresher. Duration: minimum 60 minutes.

### Tier 4 — DPO and Privacy Function (Ongoing Professional Development)

The DPO maintains currency through:
- EDPB and FDPIC guidance monitoring (ongoing)
- External privacy conferences, webinars, and publications (at least 2 per year)
- Formal CPD towards CIPP/E or equivalent (annual hours target set by DPO)

---

## 3. Confidentiality Agreement Register

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Agreement ID | Text | Unique reference (e.g., CDA-2026-001) |
| Agreement Type | Enum | Employment Contract Clause / Contractor Agreement Clause / Standalone NDA / Staffing Agency Agreement / Processor Agreement / Professional Advisor NDA |
| Party / Category | Text | Individual name or category (e.g., "All permanent employees — [Division]") |
| Governing Document | Text | Reference to the contract or agreement document |
| PII Scope | Text | What PII categories or processing activities are covered |
| Execution Date | Date | Date agreement was signed or policy acknowledged |
| Review Date | Date | Next scheduled review date |
| Adequacy Assessment | Enum | Adequate / Requires Amendment / Under Review |
| Assessed By | Text | DPO name |
| Assessment Date | Date | Date adequacy was last confirmed |
| Post-Termination Obligation | Boolean | Yes / No — does agreement survive termination? |
| Status | Enum | Active / Lapsed / Superseded / Archived |
| Notes | Text | Amendments, gaps, follow-up actions |

---

## 4. Minimum PII NDA Clause Checklist

Use when reviewing employment contracts, contractor agreements, or standalone NDAs for PII adequacy:

| Required Clause | Present? | Document Section | Notes |
|----------------|----------|-----------------|-------|
| Process PII only for authorised purposes and under instruction | Yes / No / Partial | | |
| Prohibition on unauthorised disclosure of PII to third parties | Yes / No / Partial | | |
| Obligation to protect PII using at least [Organisation]'s required security measures | Yes / No / Partial | | |
| Obligation to report suspected PII incidents without undue delay | Yes / No / Partial | | |
| Confidentiality obligation survives termination of engagement | Yes / No / Partial | | |
| Return or secure deletion of PII on termination of engagement | Yes / No / Partial | | |
| Consequences of breach stated (disciplinary, contractual, and regulatory) | Yes / No / Partial | | |

**Overall adequacy**:
- [ ] Agreement is adequate for PII purposes — no amendment required
- [ ] Agreement requires amendment before continued PII access — items: [list gaps]
- [ ] DPO sign-off: _________________ Date: _________

---

## 5. Screen Lock and Privacy Screen Configuration Standards

### Screen Lock Minimum Settings

All workstations with access to PII processing systems must be configured to the following minimum standards. The CISO confirms annually that deployed configurations meet or exceed these values:

| Setting | Minimum Requirement | Recommended |
|---------|--------------------|----|
| Automatic screen lock timeout (general office) | ≤ 5 minutes of inactivity | 3 minutes |
| Automatic screen lock timeout (unattended sessions with PII open) | ≤ 3 minutes | 1 minute |
| Screen lock authentication | Password or MFA (biometric acceptable) | MFA |
| Remote working device auto-lock | Same as office — ≤ 5 minutes | 3 minutes |
| Kiosk / shared terminal auto-lock | ≤ 2 minutes | 1 minute |

### Privacy Screen Requirements

| Environment | Requirement |
|-------------|-------------|
| Open-plan offices with regular visitor access | Privacy filter screens on all workstations displaying PII routinely |
| Customer-facing or reception positions | Privacy filter screens mandatory |
| Meeting rooms with large displays | No PII to be projected unless all present are authorised; confirm before display |
| Remote working — risk assessment | Self-assessment required; privacy screen required where others regularly present |

---

## 6. Workspace Inspection Record Template

```
WORKSPACE PRIVACY INSPECTION RECORD

Inspection Reference: INS-[YYYY]-[NNN]
Area Inspected: [Department / Floor / Room]
Inspection Date: [Date]
Conducted By (Privacy Champion / DPO): [Name]
Inspection Type: [ ] Routine Quarterly  [ ] Routine Monthly  [ ] Spot Check

FINDINGS

A. PII Documents — Desks and Surfaces
[ ] Pass — No PII documents left unattended at occupied or unoccupied desks
[ ] Finding — Description: ___________________________________________________

B. PII Documents — Storage
[ ] Pass — PII documents not in use are in locked/secured storage
[ ] Finding — Description: ___________________________________________________

C. Removable Media
[ ] Pass — No unattended removable media (USB drives, printed reports, portable drives)
[ ] Finding — Description: ___________________________________________________

D. Secure Disposal
[ ] Pass — Secure shredding bins present and in use; no PII in open waste bins
[ ] Finding — Description: ___________________________________________________

E. Screen Visibility
[ ] Pass — No PII visible on unattended screens; screens facing away from unauthorised view
[ ] Finding — Description: ___________________________________________________

SUMMARY

Total Findings: [Number]
Severity Assessment: [ ] No issues  [ ] Minor  [ ] Moderate  [ ] Serious

ACTIONS

| Finding | Action Required | Owner | Target Date | Closed Date |
|---------|----------------|-------|-------------|-------------|
| | | | | |

Privacy Champion Sign-off: _________________________ Date: _____________
DPO Notification: [ ] Not required  [ ] Notified (Date: _____________)
```

---

## 7. Remote Working Clear Desk Acknowledgment

```
REMOTE WORKING PRIVACY — CLEAR DESK AND CLEAR SCREEN ACKNOWLEDGMENT

Personnel Name: _____________________________________________
Role: _____________________________________________
Remote Working Arrangement: [ ] Permanent  [ ] Hybrid  [ ] Occasional

I acknowledge that I have read and understood the following obligations when
working remotely or from home:

1. PII documents in use during remote working will be stored securely when
   not in active use and will not be left visible to household members or
   others not authorised to access the PII.

2. PII documents are not to be printed in remote environments unless
   specifically authorised for the task. Printed PII documents must be
   securely disposed of (shredded) after use and must not be placed in
   household recycling or waste.

3. My workstation screen will lock automatically after [X] minutes of
   inactivity and I will lock my screen manually before leaving my
   workstation unattended.

4. I will not display PII on-screen in shared spaces (cafes, co-working
   spaces, public transport) without a privacy screen filter in place.

5. I confirm that my home or remote working workspace meets the requirements
   above. I will notify my Privacy Champion if my working environment changes
   in a way that affects these obligations.

Signed: _________________________ Date: _____________
Recorded in Privacy Training Register: [ ] Yes  Record ID: _____________
```

---

<!-- QA_VERIFIED: [Date] -->
