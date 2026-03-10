<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.11-12-UG:privacy:UG:a.3.11-12 -->
**PRIV-IMP-A.3.11-12-UG — Privacy Incident Management — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Incident Management — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.3.11-12-UG |
| **Related Policy** | PRIV-POL-A.3.11-12 (Privacy Incident Management) |
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
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.11-12 (Privacy Incident Management — the governing policy)
- PRIV-IMP-A.3.11-12-TG (Privacy Incident Management — Technical Guide)
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle — ISMS framework)
- PRIV-POL-A.2.5.2-6 (Transfer and Disclosure Processor — customer breach notification)

---

## Purpose of This Guide

This guide explains **how to implement** the privacy incident management requirements of PRIV-POL-A.3.11-12, including how to build and maintain the Privacy Incident Response Plan (PIRP), how to detect and escalate PII incidents, how to assess breaches, and how to execute notifications. It also contains the Privacy Incident Response Plan template.

**Who this guide is for**: DPO, CISO, Privacy Champions, Legal/Compliance, IT Security Team, and all personnel who may encounter or report a potential PII incident.

---

## Part 1 — Building and Maintaining the PIRP (A.3.11)

### 1.1 Privacy Incident Response Plan Structure

The PIRP is a controlled document owned by the DPO. It must be reviewed annually and updated after any incident that reveals a gap in the plan. The PIRP must contain:

| Section | Content |
|---------|---------|
| **Purpose and scope** | Types of incidents covered; relationship to ISMS incident management plan |
| **Incident classification** | Severity tiers (Critical / High / Medium / Low) with criteria and examples |
| **Roles and responsibilities** | Named persons for each privacy incident role; deputies; out-of-hours contacts |
| **Escalation paths** | Who contacts whom at each severity level; time triggers for escalation |
| **Detection and reporting** | How all personnel report suspected PII incidents; initial triage process |
| **Breach assessment process** | Step-by-step assessment of whether an incident is a personal data breach |
| **Regulatory notification decision tree** | When to notify EDPB/DPA (72-hour clock), FDPIC, customers (processor role) |
| **Data subject notification process** | When and how to notify data subjects; approval workflow |
| **Evidence preservation** | Coordination with CISO; log preservation; chain of custody |
| **Communication management** | Internal communications; external/media management |
| **Recovery criteria** | What constitutes incident resolution; sign-off authority |
| **Post-incident review** | Process, timeline, and output requirements |
| **Notification templates** | Pre-approved draft templates (see PRIV-IMP-A.3.11-12-TG) |
| **Supervisory authority contacts** | GDPR: Lead DPA contact; FDPIC: contact and online notification portal URL |

### 1.2 Annual PIRP Test (Tabletop Exercise)

The PIRP must be tested annually. A tabletop exercise is the minimum requirement.

**Exercise format**:
1. DPO selects a realistic scenario (e.g., ransomware affecting a PII database; accidental email disclosure of customer PII; supplier reports a breach)
2. Invite privacy incident roles: DPO, CISO, Legal, Privacy Champions, Communications representative
3. Walk through the scenario step-by-step against the PIRP: who does what, when, how
4. Identify gaps, decision points that were unclear, and timeline issues
5. Document findings in an exercise report
6. Update PIRP to address identified gaps within 30 days of the exercise

Retain exercise reports as evidence of A.3.11 compliance.

### 1.3 Maintaining Contact Information

The DPO maintains current supervisory authority contact information. Review quarterly:

| Authority | Contact | Notification Method |
|-----------|---------|---------------------|
| GDPR — Lead DPA (confirm based on main establishment) | [Contact URL from DPA website] | Online portal (most DPAs) |
| FDPIC (Swiss) | https://www.edoeb.admin.ch | Online form |
| ICO (UK — if applicable) | https://ico.org.uk | Online portal |
| DPO direct contact email | [DPO email] | Internal escalation |

---

## Part 2 — Detecting and Reporting a PII Incident

### 2.1 What to Report

Any of the following should be reported immediately as a potential PII incident:

- You find PII data sent to the wrong recipient (email, post, message)
- A device, paper document, or media containing PII is lost or stolen
- You suspect someone has accessed PII they should not have
- A system containing PII has been compromised, hacked, or infected with malware
- PII has been accidentally deleted or corrupted
- A supplier or processor contacts you about a security incident affecting your PII
- You notice PII appearing somewhere it should not be (shared drive, public site, etc.)

**When in doubt: report.** An over-reported near-miss is far better than an under-reported breach.

### 2.2 How to Report

**Any personnel**: Report to your Privacy Champion immediately — do not wait. If your Privacy Champion is unavailable: report directly to the DPO.

**Privacy Champions**: Perform initial triage (see 2.3), then escalate to DPO.

**IT Security Team**: Log the incident in the incident management system (per ISMS-POL-A.5.24-28); simultaneously notify DPO.

**Do not**:
- Attempt to resolve a PII incident on your own without notifying the DPO
- Delete or alter evidence related to the incident
- Communicate externally about the incident without DPO/Legal approval

### 2.3 Initial Triage by Privacy Champion

On receiving a report, the Privacy Champion performs a quick triage to determine whether escalation to DPO is required immediately or within 24 hours:

| Indicators | Action |
|-----------|--------|
| Confirmed or likely access by unauthorised party to significant PII | Escalate to DPO **immediately** |
| Special category PII involved | Escalate to DPO **immediately** |
| Large number of data subjects potentially affected (>100) | Escalate to DPO **immediately** |
| Ransomware or system compromise affecting PII systems | Escalate to DPO and CISO **immediately** |
| Supplier has reported an incident | Escalate to DPO **immediately** |
| Small-scale potential incident under investigation | Escalate to DPO **within 24 hours** |
| Apparent near-miss — no confirmed PII exposure | Log and escalate to DPO **within 5 business days** |

---

## Part 3 — Responding to a PII Incident (A.3.12)

### 3.1 Step 1 — Contain

The CISO leads technical containment. Priority actions on incident confirmation:
- Isolate affected systems from the network where appropriate (without destroying evidence)
- Revoke compromised credentials or access tokens
- Block unauthorised exfiltration channels
- Preserve system state before remediation (snapshot, log extraction)

The DPO is notified simultaneously and begins the breach assessment.

### 3.2 Step 2 — Assess: Is This a Personal Data Breach?

The DPO leads the personal data breach assessment. Complete the Breach Assessment Form (see PRIV-IMP-A.3.11-12-TG):

| Assessment Question | Answer |
|--------------------|--------|
| Was PII accessed, disclosed, altered, lost, or destroyed without authorisation? | Yes / No / Unknown |
| What categories of PII were affected? | List |
| How many data subjects are approximately affected? | Number / estimate / unknown |
| What is the likely impact on affected data subjects? | Describe: harm, risk of identity theft, financial loss, distress, etc. |
| Is a risk to the rights and freedoms of natural persons likely? | Yes / No / Under assessment |
| Is a HIGH risk to the rights and freedoms of natural persons likely? | Yes / No / Under assessment |

**Outcome determines notification obligations** (see Step 4).

The clock for the 72-hour GDPR notification window starts when the organisation **becomes aware** of the breach — not when the assessment is complete. If in doubt: start the clock.

### 3.3 Step 3 — Preserve Evidence

Coordinate with CISO to preserve:
- System and application logs from the affected period (before and after)
- Access logs for the affected PII systems
- Email, file, or communication records relevant to the incident
- Third-party communications (supplier notifications, customer complaints)

Chain of custody must be maintained. Do not destroy or alter any evidence before Legal/CISO sign-off.

### 3.4 Step 4 — Notify

**Notification decision matrix**:

| Scenario | Who to Notify | When |
|----------|--------------|------|
| Controller role: breach likely to result in risk to data subjects | Competent supervisory authority (GDPR Art. 33) | Within 72 hours of awareness |
| Controller role: FADP high-risk breach | FDPIC (FADP Art. 24) | As soon as possible |
| Controller role: breach likely to result in HIGH risk to data subjects | Affected data subjects (GDPR Art. 34) | Without undue delay |
| Processor role: breach (or potential breach) affecting customer PII | Customer (PII Controller) | Without undue delay; per agreement; max 24 hours |
| Processor role: do NOT notify regulators or data subjects | — | Not your obligation unless controller authorises |

**72-hour clock management**:
- DPO tracks time from awareness to notification submission
- If 72 hours cannot be met: notify the supervisory authority within 72 hours with the information available, and supplement later — a partial notification within 72 hours is better than a complete notification after the deadline
- Document the reason for any delay

### 3.5 Step 5 — Recover

The CISO leads recovery, confirmed with DPO and Data Owner sign-off:
- Restore affected PII systems with appropriate safeguards in place
- Verify data integrity — confirm no corruption or further unauthorised access
- Confirm that the root cause has been addressed before returning to normal operation
- DPO confirms it is safe to resume normal PII processing on the affected systems

### 3.6 Step 6 — Post-Incident Review

Within 10 business days of incident closure, DPO leads a post-incident review:

**Required outputs**:
- Root cause analysis: why did this breach occur?
- Impact assessment: actual harm or risk realised vs. assessed
- Process gaps identified: what failed in detection, response, or prevention?
- Control improvements: what changes are needed to prevent recurrence?
- PIRP update: does the PIRP need updating based on lessons learned?

The post-incident review report is retained for 3 years. Control improvement actions are tracked to completion.

### 3.7 Privacy Breach Register — Completing the Entry

Every incident, including those where no regulatory notification was required, must have a completed entry in the Privacy Breach Register (see PRIV-IMP-A.3.11-12-TG for the register schema). The entry must be completed within 3 business days of incident closure.

Key principle: if a supervisory authority later asks why you did not notify, the breach register entry is your defence. An undocumented "no risk" determination is not a defence.

---

## Evidence Checklist

- [ ] Privacy Incident Response Plan (PIRP) — current, approved version
- [ ] Annual PIRP test record — exercise report with findings and updates
- [ ] Supervisory authority contacts — current, tested (portal access verified)
- [ ] Notification templates — pre-approved by DPO and Legal
- [ ] Privacy Breach Register — all incidents recorded, including no-notification determinations
- [ ] Breach assessment records for all High/Critical incidents
- [ ] Regulatory notifications (Art. 33 / FADP Art. 24) within required windows, with timeline evidence
- [ ] Data subject communications where Article 34 applied
- [ ] Post-incident review reports with improvement tracking

---

<!-- QA_VERIFIED: [Date] -->
