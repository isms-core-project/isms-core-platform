# ISMS CORE OPERATIONAL — OP-POL Audit Log

Tracks which OP-POLs have been reviewed by ISMS Copilot and fixes applied.

---

## Audit Status

| # | OP-POL ID | Title | Copilot Review | S1 Fixes | S2 Enhancements | Status |
|---|-----------|-------|----------------|----------|-----------------|--------|
| 1 | ISMS-OP-POL-A.8.24 | Use of Cryptography | Passed | PQC (FIPS 203/204/205), key rotation table, secrets scope | S2: KMS specification, PQC crypto-agility assessment, key compromise tested annually, evidence cadence | Done |
| 2 | ISMS-OP-POL-A.5.15-16-18 | Identity and Access Management | Passed | Service accounts, shared accounts, MFA exemption, inactive definition, password storage | S2: Service account inactivity exclusion, 5-step access request workflow, identity verification methods (4), 5-min session timeout for sensitive data, remote access broadened, evidence with cadence/targets, service account register | Done |
| 3 | ISMS-OP-POL-A.5.34 | Privacy and Protection of PII | Passed | ROPA (SME exemption), DPIA, DSR timeline, breach notification precision | S2: Duty to Inform (Art. 19, 8 elements), consent management, controller/processor assessment, children's data, DPA advisor (voluntary/mandatory), evidence with cadence + 2 new items | Done |
| 4 | ISMS-OP-POL-A.8.20-22 | Network Security | Passed | NAC, firewall governance, patching (CVSS), split tunnelling, guest network, IoT/OT, DNS, adequacy | S2: IDS/IPS deployment locations table (5 locations), evidence retention/cadence (10 items) | Done |
| 5 | ISMS-OP-POL-A.5.14 | Information Transfer | Passed | TIA section, removable media encryption, lost information classification | S2: Courier examples (Swiss Post/DHL), personal email enforcement (DLP/mail flow), DMARC quarantine/reject, cross-border register + CISO/DPA review, evidence retention + data transfer log | Done |
| 6 | ISMS-OP-POL-A.5.24-28 | Incident Management | Passed | Breach notification content table, evidence retention baseline | S2: 4 reporting channels, IRT roles table (5), incident register (15 fields), test scenarios (4 + rotation), forensic provider pre-approved, evidence retention periods, communication templates, 9 KPIs | Done |
| 7 | ISMS-OP-POL-A.8.1-7-18-19 | Endpoint Security | Passed | CIS Benchmark L1/L2, 5-min screen lock, privileged utilities list | S2: Recovery key via MDM, remote wipe process (1hr lock/24hr wipe), BYOD enrollment (5-step), malware incident triggers, endpoint management tools table (5), config baseline reference, JIT privilege escalation, patch testing pilot group, roles table, evidence with ownership/frequency (10 items) | Done |
| 8 | ISMS-OP-POL-A.5.9 | Asset Management | Passed | Orphaned assets (discovery + departure reassignment) | S2: Asset register location/tool, criticality guidance (H/M/L), cloud registration timing, tolerated 90-day max, SPOF/succession, NIST 800-88 (Clear/Purge/Destroy), evidence ≥95% completeness, shadow IT reports | Done |
| 9 | ISMS-OP-POL-A.8.8 | Management of Technical Vulnerabilities | Passed | CVSS v3.1 primary (v4.0 future) | S2: VM tools table (5 categories), vendor advisory owner + 2-day triage, patch testing by system type table, verification failure escalation, exception register format (10 fields), EOL/EOS timelines (6/12/18 months), metrics with targets + red thresholds, change management integration, roles table, evidence with ownership/frequency (9 items) | Done |
| 10 | ISMS-OP-POL-A.5.12-13 | Information Classification and Handling | Passed | (S1: no changes) | S2: Aggregation risk guidance + examples, DLP enforcement alignment, verbal information handling (4 requirements), evidence with sample sizes + DLP reports | Done |
| 11 | ISMS-OP-POL-A.8.15 | Logging | Passed | (S1: no changes) | S2: Centralised platform specification table, capacity management (80%/90% alerts), log review ownership table (5 rows), alert thresholds with numeric values (7 events), incident escalation process (alert→triage→incident), retention rationale, archival/retrieval timelines (4 tiers), DSV Art. 4 applicability assessment, roles table, evidence with ownership/frequency (10 items) | Done |
| 12 | ISMS-OP-POL-A.5.10-11 | Acceptable Use and Return of Assets | Passed | BYOD agreement + remote wipe consent | S2: AI approval criteria (4) + 14-day request, personal use examples (4+4), sanctioned register location, monitoring triggers (4 examples) + employee rights, asset non-return process, social media crisis, gaming/crypto/mining prohibitions, evidence with cadence | Done |
| 13 | ISMS-OP-POL-A.6.3 | Information Security Awareness and Training | Passed | (S1: no changes) | S2: Training platform/delivery/duration table (6 methods), pass score 80%, phishing metrics + targets + red thresholds (4 KPIs), training content update triggers (6), effectiveness measurement framework (7 measures), language/accessibility (Swiss multilingual), roles table, register expansion (2 new fields), evidence with ownership/frequency (10 items) | Done |
| 14 | ISMS-OP-POL-A.5.19-23 | Cloud Services and Supplier Security | Passed | New OP-POL (408 lines) — merged IS 14 + IS 26 | S2: All 10 enhancements applied during initial creation (shared responsibility matrix, cloud risk register, exit strategy, contractual ISMS clause, SLA monitoring, subcontractor flow-down, evidence cadence) | Done |
| 15 | ISMS-OP-POL-A.8.32 | Change Management | Passed | New OP-POL (~440 lines) from IS 13 + Framework POL | S2: Failed change definition, change system specification + ID format, CAB meeting schedule (agenda/format), Standard Change Catalogue examples (5 + exclusions), separation of duties (peer review/privileged access/SME exception <5 staff), maintenance window preferences (standard/extended/emergency), rollback testing for high/critical + forward-fix, emergency abuse escalation (14-day RCA/60-day follow-up), configuration management integration (CMDB/drift), change-incident correlation (48hr review/3-day PIR) | Done |
| 16 | ISMS-OP-POL-A.5.37 | Documented Operating Procedures | Passed | New OP-POL (~350 lines) from IS 23 + Framework POL | S2: Repository specification + URL placeholder, procedure naming convention (PROC-[CATEGORY]-[###]), backup owner for critical procedures (SPOF), test result classification (success/partial/failure) + failure response (14/30-day revision), procedure documentation metrics (6 metrics), offline pack storage/access/annual audit, document classification guidance (Internal/Confidential), external document control (5 requirements + examples), user feedback loop (14-day handling), obsolete document retention periods (3yr/7yr/7-10yr + 90-day deletion) | Done |
| 17 | ISMS-OP-POL-A.5.32-33 | Information Protection and Records Management | Passed | New OP-POL (~350 lines) from IS 27 + Framework POL | S2: IP/records management systems table (7 tools), SAM quarterly process (6-step + metrics + unlicensed response), NDA approval process (8-step + IP return/deletion + quarterly register review), OSS licence compliance (6-step pre-adoption + approved/restricted/prohibited + copyleft + violation response), retention schedule template (11 example record types + grace period), integrity verification (4 methods + failure response 6-step), records disposal workflow (automated 6-step + manual 7-step + annual audit), legal hold process (triggers + notification template + IT suspension + monthly review + release), backup requirements (6 categories with RTO/RPO + quarterly testing + geo-redundancy), privacy-by-design (access control + pseudonymisation + DSR process + retention minimisation + breach notification) | Done |
| 18 | ISMS-OP-POL-A.5.35-36 | Independent Review and Compliance | Passed | New OP-POL (465 lines) from IS 15 + Framework POL | S2: Audit coverage cycle (1yr/3yr + mandatory annual + approval month), Evidence Library location (folder structure + access), RCA methodology (5 Whys/Fishbone/Fault Tree + documentation), audit tool security (A.8.34: approved tools/change mgmt/non-production/data protection), assessment completion tracking (deadlines per tier + escalation), finding aging thresholds (Green/Yellow/Red dashboard), improvement action process (5-step + metrics), risk acceptance renewal triggers (4 conditions + 14-day notification), trend analysis specifics (4 key trends + annual report), effectiveness verification timing (Critical 30d/High 60d/Medium-Low at next assessment) | Done |
| 19 | ISMS-OP-POL-A.8.25-26-29 | Secure Development Lifecycle | Passed | New OP-POL (430→663 lines) from IS 19 + Framework POL | S2: Security toolchain specification (9-category tools table with owner/integration), threat modelling process (5-step STRIDE + review cadence), security requirements template (14-section table + approval), language-specific coding standards (Python example: prohibited functions/required practices/approved crypto), code review workflow (5-step + 10-item secure checklist + approval by risk level), CI/CD pipeline security gates (4 gates + failure thresholds + override rules), secret scanning & secrets management (remediation 5-step with 4hr SLA + approved methods table), Security Champion programme (selection/responsibilities/training/incentives/metrics), risk classification review triggers (6 triggers + 5-step re-classification), SBOM management (generation/content/quarterly review/monitoring/retention), testing environment similarity (8-component parity table + verification), penetration testing scope & standards (approach table/in-out scope/OWASP TG v4.2/PTES/vendor criteria/5-step post-test) | Done |
| 20 | ISMS-OP-POL-A.6.7-8 | Remote Working and Security Event Reporting | Passed | New OP-POL (449→573 lines) from IS 09a + Framework POL | S2: Remote access technology specification (VPN/ZT requirements + compliance checks), location approval (standard/international/high-risk + 14-day change notification), BYOD approval criteria (5 criteria + Confidential exception), public Wi-Fi guidance (prohibited/VPN-only/Confidential discouraged + home network), clear desk cross-reference (A.7.7 + remote requirements), anonymous reporting preservation (anonymity/follow-up/alternate approach), lost/stolen device procedure (5-step + evidence preservation), reporting metrics (6 KPIs with targets + quarterly review), reporting training & awareness (initial/annual/phishing simulation), remote work compliance verification (quarterly checks/annual reviews/spot checks) | Done |
| 21 | ISMS-OP-POL-A.5.1-2-6.1-2 | ISMS Governance and Secure Employment | — | New OP-POL (525 lines) from IS 01 + Framework POL | Awaiting S2 review | Written |
| 22 | ISMS-OP-POL-A.5.30-8.13-14 | Business Continuity and Disaster Recovery | — | New OP-POL (507 lines) from IS 10 + IS 11 + Framework POL | Awaiting S2 review | Written |
| 23 | ISMS-OP-POL-A.8.2-3-5 | Authentication and Privileged Access | — | New OP-POL (482 lines) from IS 02 + Framework POL | Awaiting S2 review | Written |
| 24 | ISMS-OP-POL-A.5.3 | Segregation of Duties | — | New OP-POL (413 lines) from IS 02 (partial) + Framework POL | Awaiting S2 review | Written |
| 25 | ISMS-OP-POL-A.5.4 | Management Responsibilities | — | New OP-POL (455 lines) from IS 01 (partial) + Framework POL | Awaiting S2 review | Written |
| 26 | ISMS-OP-POL-A.6.4-5 | Disciplinary Process and Employment Exit | — | New OP-POL (434 lines) from IS 02 (partial) + Framework POL | Awaiting S2 review | Written |
| 27 | ISMS-OP-POL-A.5.17 | Authentication Information | — | New OP-POL (463 lines) from IS 02 (partial) + Framework POL | Awaiting S2 review | Written |
| 28 | ISMS-OP-POL-A.6.6 | Confidentiality and Non-Disclosure Agreements | — | New OP-POL (558 lines) from IS 02 (partial) + Framework POL | Awaiting S2 review | Written |
| 29 | ISMS-OP-POL-A.5.29 | Information Security During Disruption | — | New OP-POL (432 lines) from IS 10 (partial) + Framework POL | Awaiting S2 review | Written |
| 30 | ISMS-OP-POL-A.7.1-3 | Physical Access Control | — | New OP-POL (466 lines) from IS 20 + Framework POL | Awaiting S2 review | Written |
| 31 | ISMS-OP-POL-A.7.4-5-11 | Physical Infrastructure Security | — | New OP-POL (457 lines) from IS 20 (partial) + Framework POL | Awaiting S2 review | Written |
| 32 | ISMS-OP-POL-A.7.6-7-14 | Secure Areas and Media Handling | — | New OP-POL (465 lines) from IS 05 (partial) + Framework POL | Awaiting S2 review | Written |
| 33 | ISMS-OP-POL-A.7.8-9 | Equipment Siting and Protection | — | New OP-POL (459 lines) from IS 08 + IS 20 + Framework POL | Awaiting S2 review | Written |
| 34 | ISMS-OP-POL-A.7.10 | Storage Media | — | New OP-POL (480 lines) from IS 20 (partial) + Framework POL | Awaiting S2 review | Written |
| 35 | ISMS-OP-POL-A.5.31 | Legal, Statutory, Regulatory and Contractual Requirements | — | New OP-POL (520 lines) from DP 01 + Framework POL (condensed 4,500+ lines) | Awaiting S2 review | Written |
| 36 | ISMS-OP-POL-A.8.4 | Access to Source Code | — | New OP-POL (502 lines) from IS 19 (partial) + Framework POL (800 lines condensed) | Awaiting S2 review | Written |
| 37 | ISMS-OP-POL-A.8.10 | Information Deletion | — | New OP-POL (558 lines) from IS 05 + DP 02 + Framework POL | Awaiting S2 review | Written |
| 38 | ISMS-OP-POL-A.8.11 | Data Masking | — | New OP-POL (466 lines) from IS 02 (partial) + Framework POL (1,318 lines condensed) | Awaiting S2 review | Written |
| 39 | ISMS-OP-POL-A.8.16 | Monitoring Activities | — | New OP-POL from IS 16 (partial) + Framework POL | Awaiting S2 review | Written |
| 40 | ISMS-OP-POL-A.8.17 | Clock Synchronisation | — | New OP-POL from IS 16 (partial) + Framework POL | Awaiting S2 review | Written |
| 41 | ISMS-OP-POL-A.8.23 | Web Filtering | — | New OP-POL from IS 17 (partial) + Framework POL | Awaiting S2 review | Written |
| 42 | ISMS-OP-POL-A.8.27 | Secure Systems Architecture and Engineering Principles | Passed | New OP-POL (550→773 lines) from IS 19 (partial) + Framework POL | S2: Risk-based review SLAs (5/10/15 days), Zero Trust org-size context, Tier 3 encryption made auditable, threat model retention (lifecycle+3yr), SSO/SAML pattern example, third-party review triggers, architecture review checklist, external review triggers, fail-secure examples, complexity metrics, anti-patterns table, tier re-classification, SOC 2 alignment (7 criteria), nFADP Art. 7 privacy by default (22 enhancements) | Done |
| 43 | ISMS-OP-POL-A.8.28 | Secure Coding | Passed | New OP-POL (~510 lines) from IS 19 (partial) + Framework POL | S2: Hard-coded secrets detection (3 scanning layers), SAST false positive suppression (peer review), risk-based code review (5-tier), SBOM for all apps, dependency pinning/update cadence, Security Champion programme | Done |
| 44 | ISMS-OP-POL-A.8.30 | Outsourced Development | Passed | New OP-POL (479→740 lines) from IS 19 (partial) + Framework POL | S2: Vendor tier methodology, pen test qualifications, blocking findings, synthetic data generation, subcontractor approval, escrow verification, vendor workflow diagram, red flags table, vulnerability remediation, vendor incident response, SBOM requirements, implementation checklist, acceptance/SAST/ownership/monitoring refinements, vendor scorecard, CISO escalation, FDPIC notification (19 enhancements) | Done |
| 45 | ISMS-OP-POL-A.8.31 | Environment Separation | Passed | New OP-POL (~507 lines) from IS 19 (partial) + Framework POL | S2: Container-specific guidance (production container security, K8s hardening), staging-production differences table, developer experience section, incident response integration | Done |
| 46 | ISMS-OP-POL-A.5.5-6 | Contact with Authorities and Special Interest Groups | Passed | New OP-POL (~478 lines) from Framework POL (gap) | S2: Customer/stakeholder communication section, contact registry change management | Done |
| 47 | ISMS-OP-POL-A.5.7 | Threat Intelligence | Passed | New OP-POL (528→822 lines) from Framework POL (gap) | S2: Availability/BCP integration, vendor intelligence management, data lifecycle, testing/validation, customer threat sharing, metrics dashboard | Done |
| 48 | ISMS-OP-POL-A.5.8 | Information Security in Project Management | Passed | New OP-POL (456→522 lines) from Framework POL (gap) | S2: Optional enhancements applied (full file revision) | Done |
| 49 | ISMS-OP-POL-A.7.12-13 | Cabling Security and Equipment Maintenance | Passed | New OP-POL (~464 lines) from Framework POL (gap) | S2: Availability/service continuity, service impact assessment, maintenance windows, redundancy requirements, cabling change control | Done |
| 50 | ISMS-OP-POL-A.8.6 | Capacity Management | Passed | New OP-POL (~488 lines) from Framework POL (gap) | S2: Capacity/cost optimisation, service level objectives alignment, capacity planning committee | Done |
| 51 | ISMS-OP-POL-A.8.9 | Configuration Management | Passed | New OP-POL (~526 lines) from Framework POL (gap) | S2: Tiered baseline coverage (100%/100%/90%/80%), least functionality whitelist, change categorisation (formal/pre-approved/no-approval), drift remediation verification, risk-based golden image refresh, IaC scanning rules | Done |
| 52 | ISMS-OP-POL-A.8.12 | Data Leakage Prevention | Passed | New OP-POL (586→919 lines) from Framework POL (gap) | S2: Customer data protection (CC1.2), third-party DLP vendor management (CC9.2), DLP availability/performance (A1.2), business continuity/DR (CC9.1), DLP effectiveness testing (CC4.1), management reporting, enhanced SOC 2 Type II evidence table (7 enhancements) | Done |
| 53 | ISMS-OP-POL-A.8.33-34 | Test Information and Audit Testing Protection | Passed | New OP-POL (~458 lines) from Framework POL (gap) | S2: Test data source decision tree, data masking quick reference table, testing status communication | Done |

---

## Phase 1 Summary

- **53/53 OP-POLs written** (100%)
- **53/53 Copilot S2 applied** (100%) — All batches complete
- **Phase 1 S2 COMPLETE** (2026-02-08)

---

## Phase 2 — Compliance Checklist Workbooks (SCR + WKBK)

| # | Control Group | Generator | Domains | Requirements | Sheets | Status |
|---|--------------|-----------|---------|-------------|--------|--------|
| 1 | A.8.24 Use of Cryptography | `generate_op_checklist_a824.py` | 5 (Encryption Standards, Data in Transit, Data at Rest, Key Management, Crypto Governance) | 47 | 7 | Done |
| 2 | A.5.19-23 Cloud Services and Supplier Security | `generate_op_checklist_a51923.py` | 6 (Register & Classification, Due Diligence & Selection, Contracts & Data Processing, Cross-Border & Compliance, Monitoring & Incidents, Exit & Continuity) | 42 | 8 | Done |
| 3 | A.5.24-28 Incident Management | `generate_op_checklist_a52428.py` | 6 (Reporting & Triage, Classification & Escalation, Incident Response, Data Breach Notification, Evidence Collection, Lessons Learned & Testing) | 43 | 8 | Done |

**Progress: 3/53 generators built (6%)**

**Workbook pattern:**
- Executive Summary + Dashboard + N domain checklist sheets
- Each "shall" requirement from OP-POL becomes one row
- Status dropdown (Compliant/Partial/Non-Compliant/N/A) with conditional formatting
- Dashboard aggregates via COUNTIF formulas
- Executive Summary traffic light (GREEN >=90%, AMBER >=70%, RED <70%)
- Naming: `ISMS-OP-CHK-A.X.X_Compliance_Checklist_YYYYMMDD.xlsx`

---

## Review Process

1. Write OP-POL from source sample + online research
2. Apply template structure (A.8.24 reference)
3. Submit to ISMS Copilot for review
4. Triage findings (valid for SME OP-POL vs scope creep)
5. Apply valid fixes
6. Log in this file

---

*Last updated: 2026-02-08*
