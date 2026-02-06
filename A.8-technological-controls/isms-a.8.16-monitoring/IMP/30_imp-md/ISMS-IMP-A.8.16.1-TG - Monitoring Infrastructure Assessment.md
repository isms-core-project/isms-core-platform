**ISMS-IMP-A.8.16.1-TG - Monitoring Infrastructure Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.16.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Monitoring Infrastructure & Technology Capabilities |
| **Related Policy** | ISMS-POL-A.8.16, Section 2.1 (Monitoring Infrastructure Requirements) |
| **Purpose** | Document deployed monitoring technologies, assess capabilities against policy requirements, and identify infrastructure gaps in a vendor-agnostic manner |
| **Target Audience** | Security Engineers, SOC Analysts, IT Operations, System Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Semi-annual or After Major Infrastructure Changes |
| **Date** | 22.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.16.1-UG.

---

# Technical Specification

# Workbook Structure

**Filename:** `ISMS_A_8_16_1_Monitoring_Infrastructure_Assessment_YYYYMMDD.xlsx`
**Generator Script:** `generate_a816_1_monitoring_infrastructure.py`
**Total Sheets:** 9

## Sheet Overview

| Sheet # | Name | Purpose | Data Rows | Auto-Calc |
|---------|------|---------|-----------|-----------|
| 1 | Instructions & Legend | Workbook overview, color coding | 3 | Yes |
| 2 | 1. Monitoring Platform Capabilities | Monitoring technology inventory | 18 | Yes |
| 3 | 2. Log Source Coverage | System monitoring status | 100 | Yes |
| 4 | 3. Data Collection Architecture | Log flow mapping | 20 | No |
| 5 | 4. Integration & Enrichment | External integrations | 20 | No |
| 6 | 5. Performance & Scalability | Metrics and capacity | 10 | Yes |
| 7 | Summary Dashboard | Consolidated compliance view | 0 | Yes |
| 8 | Evidence Register | Evidence tracking | 50 | No |
| 9 | Approval Sign-Off | Approval workflow | 3 | No |

# Sheet 2: Monitoring Platform Capabilities - Technical Spec

**Column Definitions:**

| Col | Header | Width | Type | Validation | Formula |
|-----|--------|-------|------|------------|---------|
| A | Platform/Tool Name | 28 | Text | None | None |
| B | Platform Type | 20 | Dropdown | SIEM, IDS/IPS, EDR, NDR, UEBA, Log Management, Other | None |
| C | Vendor/Solution | 22 | Text | None | None |
| D | Deployment Model | 18 | Dropdown | On-Premises, Cloud, Hybrid | None |
| E | Log Collection Methods | 24 | Text | None | None |
| F | Parsing Capabilities | 20 | Dropdown | Excellent, Good, Limited, Poor | None |
| G | Storage & Indexing | 20 | Dropdown | Hot/Warm/Cold Tiers, Hot Only, Minimal | None |
| H | Search Performance | 18 | Dropdown | <10 sec, 10-60 sec, >60 sec | None |
| I | Real-Time Alerting | 18 | Dropdown | Yes, No, Limited | None |
| J | Correlation Engine | 18 | Dropdown | Advanced, Basic, None | None |
| K | Threat Intel Integration | 22 | Dropdown | Yes, No, Planned | None |
| L | SOAR Integration | 18 | Dropdown | Yes, No, Planned | None |
| M | Compliance Reporting | 20 | Dropdown | Built-in, Custom, None | None |
| N | Version | 20 | Text | None | None |
| O | Licensing Status | 18 | Dropdown | Licensed, Evaluation, Expired, Open Source | None |
| P | Support Contract | 18 | Dropdown | Active, Expired, None, Community | None |
| Q | Deployment Date | 15 | Date | DD.MM.YYYY | None |
| R | Administrator Contact | 25 | Text | Email format | None |
| S | Status | 18 | Dropdown | ✅ Operational, ⚠️ Degraded, 🔧 Maintenance, ❌ Failed, 📋 Planned, 🗑️ Decommissioned | None |
| T | Compliance Score | 12 | Percentage | Read-only | =CALCULATE_CAPABILITY_SCORE(F:M) |
| U | Notes | 30 | Text | None | None |

**Compliance Score Formula (Column T):**
```excel
=IF(ISBLANK(A8),"",
    LET(
        capabilities, COUNTIFS(F8:M8,"Excellent",F8:M8,"Yes",F8:M8,"Advanced",F8:M8,"Built-in",F8:M8,"Hot/Warm/Cold Tiers",F8:M8,"<10 sec"),
        partial_capabilities, COUNTIFS(F8:M8,"Good",F8:M8,"Limited",F8:M8,"Basic",F8:M8,"Custom",F8:M8,"Hot Only",F8:M8,"10-60 sec"),
        total_capabilities, 8,
        score, (capabilities + partial_capabilities*0.5) / total_capabilities,
        IF(score>=0.8,"✅ "&TEXT(score,"0%"),IF(score>=0.5,"⚠️ "&TEXT(score,"0%"),"❌ "&TEXT(score,"0%")))
    )
)
```

**Conditional Formatting:**

- Compliance Score ≥80%: Green fill (#C6EFCE), dark green text (#006100)
- Compliance Score 50-79%: Yellow fill (#FFEB9C), dark yellow text (#9C6500)
- Compliance Score <50%: Red fill (#FFC7CE), dark red text (#9C0006)

# Sheet 3: Log Source Coverage - Technical Spec

**Column Definitions:**

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | System Name | 30 | Text | None |
| B | System Type | 25 | Dropdown | Server - Domain Controller, Server - Database, Server - Application, Server - File, Server - Email, Server - Other, Network - Firewall, Network - Router, Network - Switch, Network - Load Balancer, Network - VPN, Network - Wireless, Network - Other, Security - IDS/IPS, Security - Proxy, Security - WAF, Security - DLP, Security - Email Gateway, Security - Other, Endpoint - Workstation, Endpoint - Mobile, Cloud - Infrastructure, Cloud - Application, Appliance - Backup, Appliance - Other |
| C | Criticality Tier | 18 | Dropdown | Tier 1 - Critical, Tier 2 - Standard, Tier 3 - Low |
| D | IP Address / Identifier | 20 | Text | None |
| E | Monitoring Status | 18 | Dropdown | ✅ Monitored, ⚠️ Partial, ❌ Not Monitored, 📋 Planned, N/A |
| F | Collection Method | 25 | Text | None |
| G | Log Types Collected | 30 | Text | None |
| H | Retention Period (Days) | 15 | Number | >0 |
| I | Last Log Received | 20 | DateTime | DD.MM.YYYY HH:MM |
| J | Log Volume (Events/Day) | 18 | Number | ≥0 |
| K | Data Classification | 18 | Dropdown | Public, Internal, Confidential, Restricted |
| L | Compliance Requirement | 18 | Dropdown | ISO 27001, GDPR, nDSG, PCI DSS, HIPAA, FINMA, DORA, NIS2, SOC 2, Multiple, None |
| M | Monitoring Platform | 25 | Text | Reference Sheet2 Column A |
| N | Coverage Gap? | 15 | Dropdown | No Gap, Partial Gap, Full Gap, Exception Approved |
| O | Remediation Target | 15 | Date | DD.MM.YYYY |
| P | Notes | 35 | Text | None |

**Coverage Calculation (Summary Section):**
```excel
Total Systems: =COUNTA(A8:A107)
Systems Monitored: =COUNTIF(E8:E107,"✅ Monitored")
Coverage %: =IF(Total>0, Monitored/Total*100, 0)
Tier 1 Coverage: =COUNTIFS(C8:C107,"Tier 1*",E8:E107,"✅ Monitored")/COUNTIF(C8:C107,"Tier 1*")*100
```

**Conditional Formatting:**

- Monitoring Status "✅ Monitored": Green
- Monitoring Status "⚠️ Partial": Yellow
- Monitoring Status "❌ Not Monitored": Red
- Coverage Gap "Full Gap" + Tier 1: Red bold (CRITICAL)

# Cell Styling Reference

**Standard Color Palette:**

- **Header Rows:** Dark Blue (#003366), White Text, Bold, 40px height
- **Data Entry Cells:** Yellow fill (#FFFF00), Black text
- **Read-Only Formula Cells:** Light Gray (#F2F2F2), Gray text
- **Example Rows:** Light Blue (#D9E2F3), Italic text
- **Compliance Status:**
  - ✅ Compliant: Green (#C6EFCE / #006100)
  - ⚠️ Partial: Yellow (#FFEB9C / #9C6500)
  - ❌ Non-Compliant: Red (#FFC7CE / #9C0006)

**Cell Protection:**

- All formula cells: Protected (locked)
- All data entry cells: Unprotected (editable)
- Header rows: Protected (locked)
- Sheet protection: Enabled with password (password in generator script)

---

# Implementation Complete

This specification enables Python script generation of the Excel workbook with all features:

- Data validation (dropdowns, date formats, number ranges)
- Conditional formatting (color-coded compliance status)
- Formula calculations (compliance scores, coverage percentages)
- Cell protection (prevent formula modification, allow data entry)
- Professional styling (colors, fonts, borders matching ISMS standards)

**Total Document Length:** ~2,500 lines (Part I: ~1,800 + Part II: ~700)

**Status:** ✅ COMPLETE - Ready for implementation and use

---

**END OF DOCUMENT**

---

# Evidence Collection

**Purpose:** Gather supporting documentation for audit trail and compliance verification

## Required Evidence Types

**1. Architecture Documentation**

- **What to Collect:**
  - Monitoring infrastructure topology diagrams
  - Log flow diagrams (source → collector → aggregator → SIEM)
  - Network architecture showing monitoring zones
  - Data center and cloud architecture with monitoring points
- **Format:** Visio, draw.io, PowerPoint, or any diagramming tool
- **Storage Location:** Evidence Register (Sheet 8), document management system
- **Frequency:** Update after any infrastructure changes

**2. Platform Configuration Evidence**

- **What to Collect:**
  - SIEM data source list export (all configured log sources)
  - Agent deployment reports (EDR, log forwarders showing installation status)
  - License records (screenshots showing license usage vs. available)
  - Version information (SIEM, IDS/IPS, EDR platforms with build numbers)
- **How to Collect:**
  - Splunk: Settings → Data Inputs → Export to CSV
  - Sentinel: Data Connectors → Export connector list
  - EDR consoles: Agent deployment status reports
- **Retention:** Keep current + previous 2 versions for change tracking

**3. Performance Metrics**

- **What to Collect:**
  - Dashboard screenshots (ingestion rate, search performance, storage)
  - Capacity planning reports (current utilization, growth projections)
  - Historical trend graphs (30-90 days of performance data)
  - Alert latency measurements (time from event to alert)
- **Frequency:** Monthly snapshots, quarterly trend analysis
- **Critical Metrics:**
  - Ingestion rate (events/sec or GB/day)
  - Search response time (average and 95th percentile)
  - Storage consumption and retention compliance
  - Alert latency (<60 sec for Tier 1 critical alerts)

**4. Integration Configuration**

- **What to Collect:**
  - Threat intelligence feed subscription records
  - SOAR playbook documentation (what actions are automated)
  - Ticketing integration configuration (how alerts create tickets)
  - Asset/identity enrichment lookup tables (sample data showing enrichment)
- **Verification Evidence:**
  - Test integration execution logs
  - Sample enriched log entries
  - Threat intel match examples (IOC detections)

**5. Coverage Evidence**

- **What to Collect:**
  - Asset inventory exports (systems that SHOULD be monitored)
  - SIEM data source inventory (systems that ARE monitored)
  - Gap analysis report (systems in inventory but not in SIEM)
  - Coverage by tier metrics (% Tier 1/2/3/4 monitored)
- **Cross-References:**
  - Sheet 3 (Log Source Coverage) is primary evidence
  - CMDB exports show authoritative asset list
  - SIEM queries showing last log received per system

**6. Compliance Documentation**

- **What to Collect:**
  - Policy excerpts defining monitoring requirements
  - Exception approval records (email, signed forms)
  - Remediation plans for identified gaps
  - Gap closure verification (before/after evidence)
- **Critical for Audit:**
  - Every exception must have written approval from CISO
  - Every gap must have documented remediation plan with owner and date
  - Closed gaps must show verification evidence (logs now flowing)

## Evidence Collection Best Practices

**Organize by Assessment Sheet:**

- Create folder structure matching workbook sheets
- Example:

  ```
  A.8.16.1_Evidence/
  ├── Sheet2_Platforms/
  │   ├── Platform_Capability_Assessments/
  │   └── License_Records/
  ├── Sheet3_Coverage/
  │   ├── Asset_Inventory_Exports/
  │   ├── SIEM_Data_Source_Lists/
  │   └── Gap_Analysis_Reports/
  ├── Sheet4_Architecture/
  │   ├── Diagrams/
  │   └── Test_Results/
  └── Sheet5_Integrations/
      ├── Integration_Configs/
      └── Test_Evidence/
  ```

**Use Consistent Naming:**

- Format: `[Evidence_Type]_[Date]_[Description].ext`
- Example: `SIEM_DataSources_20260122_Splunk_Export.csv`

**Maintain Evidence Register (Sheet 8):**

- Document every piece of evidence collected
- Include location, collection date, what it proves
- Enable quick retrieval during audits

**Version Control:**

- Keep current evidence + previous 2 assessment cycles
- Track changes over time (coverage improving? gaps closed?)

**Secure Storage:**

- Evidence may contain sensitive information (asset lists, IP addresses)
- Store in access-controlled document repository
- Follow data classification policy

---

# Common Pitfalls

## Pitfall #1: Confusing Monitoring TOOLS with Monitoring COVERAGE

**The Mistake:**
"We have a SIEM, so we have monitoring."

**Reality Check:**
Having a SIEM doesn't mean you're monitoring everything (or anything). Many organizations have expensive SIEM platforms receiving logs from <30% of critical systems.

**How to Avoid:**

- Complete Sheet 3 (Log Source Coverage) honestly
- For EVERY system marked "Monitored" - actually search SIEM for logs
- If last log received > 7 days ago, it's NOT monitored
- Calculate coverage % = (Systems Actually Monitored / Total Systems) × 100

**Red Flag:** Coverage % is a guess, not a measured number

---

## Pitfall #2: Treating All Monitoring Platforms as Equivalent

**The Mistake:**
"We have IDS, so we have visibility."

**Reality Check:**

- IDS sees network traffic (but not endpoint activity)
- EDR sees endpoints (but not network devices)
- SIEM correlates (but needs log sources feeding it)
- Each platform has DIFFERENT visibility

**How to Avoid:**

- Document platform TYPE in Sheet 2, Column B
- Understand what each platform CAN and CANNOT see
- Don't claim endpoint visibility if you only have network IDS
- Combine platforms for comprehensive coverage

**Example:**

- Firewall IDS detects network attack → but can't see if endpoint was compromised
- EDR detects malware on endpoint → but can't see lateral movement across network
- Need BOTH for complete picture

---

## Pitfall #3: Ignoring "Ghost" Log Sources

**The Mistake:**
Assessment documents systems that "send logs to SIEM" based on configuration, without verifying logs actually arrive.

**Reality Check:**
Many configured log sources stop working:

- Agent crashed and never restarted
- Firewall rule blocks log forwarding
- Certificate expired (encrypted transport)
- Disk full (can't write logs locally)
- SIEM license limit reached (silently dropping logs)

**How to Avoid:**

- For every "Monitored" system in Sheet 3:
  - Actually search SIEM for logs from that specific system
  - Verify timestamp is recent (<24 hours for Tier 1)
  - Document verification date in Column J
- If logs are stale (>30 days old), change status to "Partial" or investigate

**Best Practice:** 
Run automated query monthly: "Show all systems configured in SIEM but no logs received in 30 days"

---

## Pitfall #4: Single Points of Failure in Log Collection

**The Mistake:**
All logs flow through one collector with no redundancy. Collector fails → monitoring blind.

**Reality Check:**
During incidents (when monitoring is most critical), infrastructure often fails:

- Network segmentation cuts off log collector
- Log server runs out of disk space
- Collector overwhelmed by log volume during attack

**How to Avoid:**

- Document data collection architecture in Sheet 4
- Identify EVERY single point of failure (Column K)
- For Tier 1 systems: MUST have redundancy
  - Multiple collectors (active-active or failover)
  - Local buffering (if collector unreachable, queue locally)
  - Diverse network paths (primary WAN + backup Internet)

**Red Flag:** All Tier 1 logs flow through single collector with no failover

---

## Pitfall #5: Assuming Integration Works Without Testing

**The Mistake:**
"We have threat intel integration configured" → Never verify IOCs actually getting into SIEM.

**Reality Check:**
Integrations break silently:

- API key expired
- Threat feed URL changed
- Integration add-on incompatible with SIEM upgrade
- Rate limit exceeded (no error messages)

**How to Avoid:**

- Sheet 5, Column H: Document LAST SUCCESSFUL UPDATE timestamp
- Test each integration:
  - Threat Intel: Search SIEM for known malicious IP → Does it flag as malicious?
  - Asset Enrichment: Search for IP → Does SIEM show asset name, owner, criticality?
  - SOAR: Create test alert → Does playbook execute?
- If "Last Update" timestamp is >7 days old for threat intel → Integration may be broken

**Best Practice:**
Monitor your integrations (monitor the monitor):

- Alert if threat intel feed hasn't updated in 24 hours
- Alert if SOAR hasn't executed in 7 days (may indicate connection failure)

---

## Pitfall #6: Unencrypted Log Transport

**The Mistake:**
Logs sent via UDP syslog (unencrypted, no delivery guarantee) across untrusted networks.

**Reality Check:**
Unencrypted logs expose sensitive data:

- Authentication logs contain usernames
- Application logs may contain PII, API keys, session tokens
- Network sniffing reveals internal architecture

**How to Avoid:**

- Sheet 4, Column G: Document transport protocol for EVERY path
- Mandate encrypted transport for:
  - Any logs crossing security zones (DMZ → Internal)
  - Any logs containing PCI/PHI/PII data
  - Any logs traversing Internet or untrusted networks
- Acceptable: Unencrypted within trusted internal network segment
- Preferred: TLS-encrypted everywhere (TLS 1.2+)

**Compliance:**

- PCI DSS: Requires encryption for cardholder data logs
- GDPR: Requires encryption for personal data in transit
- HIPAA: Requires encryption for PHI

---

## Pitfall #7: No Performance Baseline

**The Mistake:**
"Our SIEM is slow" → but no metrics to quantify "slow" or prove degradation.

**Reality Check:**
Without baseline metrics, you can't:

- Detect performance degradation (is it slower than yesterday? last month?)
- Capacity plan (when will we run out of storage? When do we need to scale?)
- Compare platforms (is Solution A actually faster than Solution B?)

**How to Avoid:**

- Sheet 6: Document current performance metrics
- Establish baseline over 30+ days:
  - Average search time: ___ seconds
  - Ingestion rate: ___ events/sec or GB/day
  - Storage growth: ___ GB/day
  - Alert latency: ___ seconds
- Re-measure quarterly to detect trends

**Capacity Planning Formula:**
```
Time Until Capacity Reached = (Available Storage) / (Daily Growth Rate)

Example:
Available Storage: 5 TB
Daily Growth: 50 GB/day
Time Until Full: 5000 GB / 50 GB/day = 100 days

Action: Plan expansion in 60-90 days
```

---

## Pitfall #8: Exception Proliferation Without Compensating Controls

**The Mistake:**
Many "exceptions" for unmonitored Tier 1 systems, but no documented compensating controls or risk acceptance.

**Reality Check:**
Exception should be EXCEPTION (rare), not the norm.

- If >10% of Tier 1 systems have exceptions → Policy is wrong or exceptions are rubber-stamped
- Every exception creates a blind spot → must have CISO-approved risk acceptance
- Compensating controls MUST be documented (how do you mitigate the monitoring gap?)

**How to Avoid:**

- Sheet 3, Column N: Mark "Exception Approved" ONLY if:

  1. Formal exception request submitted
  2. CISO (or equivalent) approved in writing
  3. Compensating controls documented
  4. Annual review scheduled

- Document exception details in Column P:
  - Exception ID: EXE-A816-###
  - Approval Date: DD.MM.YYYY
  - Approver: [Name, Title]
  - Reason: [Technical limitation, business justification]
  - Compensating Controls: [Alternative security measures]
  - Review Date: [Annual re-approval required]

**Red Flag:** >20% exception rate without documented compensating controls

---

## Pitfall #9: Cloud Monitoring Gaps

**The Mistake:**
Comprehensive on-premises monitoring, but cloud resources (AWS, Azure, GCP) not monitored or only partially monitored.

**Reality Check:**
Cloud attack surface is GROWING, but many organizations:

- Don't monitor cloud resource logs (CloudTrail, Activity Logs, VPC Flow Logs)
- Don't integrate cloud logs into central SIEM
- Don't monitor cloud-native services (Lambda, S3, RDS)
- Treat cloud as "someone else's problem"

**How to Avoid:**

- Include cloud resources in Sheet 3 (Log Source Coverage)
- Document cloud log collection architecture in Sheet 4:
  - AWS: CloudWatch → Kinesis/Lambda → SIEM
  - Azure: Diagnostic Settings → Event Hub → SIEM
  - GCP: Cloud Logging → Pub/Sub → SIEM
- Monitor cloud-native services:
  - API calls (CloudTrail, Activity Logs)
  - Resource changes (Config, Resource Manager)
  - Network traffic (VPC Flow Logs, NSG Flows)
  - Authentication (IAM, Entra ID)

**Critical:** Cloud resources are Tier 1 if they process production data or are externally accessible

---

## Pitfall #10: Assessment as One-Time Exercise

**The Mistake:**
Complete assessment for ISO 27001 audit, then never update it. Assessment becomes stale documentation.

**Reality Check:**
Environment changes constantly:

- New servers deployed
- Old systems decommissioned
- Cloud infrastructure scales up/down
- Monitoring tools upgraded
- Integration feeds change

Stale assessment = Compliance theater (looks good on paper, doesn't reflect reality)

**How to Avoid:**

- Set review cycle in Sheet 1: Minimum semi-annual for A.8.16.1
- Trigger updates when:
  - Major infrastructure changes (datacenter migration, cloud adoption)
  - Monitoring platform upgrades (SIEM version changes)
  - Significant asset additions (>10% increase in monitored systems)
  - Security incidents exposing blind spots
- Automate where possible:
  - Asset inventory sync with CMDB
  - SIEM data source list refresh
  - Performance metrics collection

**Best Practice:**

- **Quarterly:** Update Sheet 3 (Log Source Coverage), Sheet 6 (Performance)
- **Semi-Annual:** Full review of all sheets, re-verify monitoring status
- **Annual:** Complete re-assessment with fresh evidence collection

---

# Quality Checklist

**Before submitting assessment for approval, verify:**

## Document Completeness

**Sheet 1: Instructions**

- [ ] Assessment Date filled in (DD.MM.YYYY)
- [ ] Completed By name entered
- [ ] Organization name entered
- [ ] Next Review Date auto-calculated correctly

**Sheet 2: Monitoring Platform Capabilities**

- [ ] All monitoring platforms documented (SIEM, IDS/IPS, EDR, NDR, Log Management)
- [ ] Platform types correctly categorized
- [ ] Vendor/solution with version numbers included
- [ ] Capability assessment complete (Columns F-M) for each platform
- [ ] Licensing status documented (active, expired, evaluation)
- [ ] Support contract status verified
- [ ] Administrator contacts provided
- [ ] Deployment dates documented
- [ ] Status current (Operational, Degraded, Failed)
- [ ] Compliance scores auto-calculated (no manual entry)

**Sheet 3: Log Source Coverage (CRITICAL SHEET)**

- [ ] All Tier 1 (Critical) systems documented
- [ ] All Tier 2 (High) systems documented
- [ ] Monitoring status VERIFIED (not assumed) - searched SIEM for actual logs
- [ ] "Last Log Verified" date within:
  - [ ] 7 days for Tier 1 systems
  - [ ] 30 days for Tier 2 systems
  - [ ] 90 days for Tier 3/4 systems
- [ ] Every "Monitored" system has specific log types listed (Column H)
- [ ] Every monitoring platform name matches Sheet 2 entries
- [ ] Coverage gaps documented with reasons (Column P)
- [ ] Full Gap + Tier 1 systems have remediation target ≤30 days
- [ ] All exceptions have approval documentation referenced
- [ ] Coverage summary metrics auto-calculated

**Sheet 4: Data Collection Architecture**

- [ ] All distinct log collection paths documented
- [ ] Source systems clearly identified (specific or grouped)
- [ ] Collectors and aggregators documented with hostnames/IPs
- [ ] Transport protocols specified (encryption status clear)
- [ ] Network paths documented (LAN, WAN, VPN, cloud)
- [ ] Redundancy mechanisms documented (or "None" explicitly stated)
- [ ] Buffering capacity calculated (GB or time duration)
- [ ] Single points of failure identified
- [ ] All paths tested with verification dates (Column L)
- [ ] Path status current (Operational, Degraded, Failed)

**Sheet 5: Integration & Enrichment**

- [ ] All SIEM integrations documented (threat intel, SOAR, ticketing, enrichment)
- [ ] Integration methods specified (API, webhook, file import, etc.)
- [ ] Data flow direction clarified (Inbound, Outbound, Bidirectional)
- [ ] Update frequency documented
- [ ] Last successful update timestamp verified (<7 days for active integrations)
- [ ] Authentication methods documented
- [ ] Enrichment value quantified (what benefit does it provide?)
- [ ] Coverage scope documented (what logs are enriched?)
- [ ] Limitations and known issues documented
- [ ] Integration status current (Active, Intermittent, Failed)

**Sheet 6: Performance & Scalability**

- [ ] Performance metrics documented for each platform
- [ ] Ingestion rates measured (events/sec or GB/day)
- [ ] Storage consumption documented (total size, growth rate)
- [ ] Search performance measured (average query time)
- [ ] Alert latency documented (event generation to alert delivery)
- [ ] Resource utilization measured (CPU, memory, disk I/O)
- [ ] Capacity headroom calculated (% available before scaling needed)
- [ ] Performance vs. policy requirements compared
- [ ] Bottlenecks identified
- [ ] Scalability plans documented

**Sheet 7: Summary Dashboard**

- [ ] All auto-calculated metrics display correctly
- [ ] No #REF or #VALUE errors in formulas
- [ ] Compliance percentages calculated accurately
- [ ] Critical gaps highlighted visually
- [ ] Overall health score makes sense (sanity check)

**Sheet 8: Evidence Register**

- [ ] All supporting evidence documented
- [ ] Evidence types categorized correctly
- [ ] Storage locations provided (file paths, URLs)
- [ ] Collection dates documented
- [ ] Evidence linked to relevant sheets
- [ ] Retention periods specified
- [ ] Evidence actually exists at documented locations (spot check)

**Sheet 9: Approval Sign-Off**

- [ ] All approval levels defined (Technical, Compliance, Executive)
- [ ] Approver names and titles specified
- [ ] Approval criteria documented
- [ ] Space for signatures/electronic approval
- [ ] Approval timeline realistic (15 business days total)

## Data Quality

**Accuracy Checks:**

- [ ] No placeholder text remaining (no "TBD", "[USER INPUT]", "SAMPLE")
- [ ] All dates in correct format (DD.MM.YYYY)
- [ ] No blank required fields (yellow-highlighted cells filled)
- [ ] Dropdown selections from valid lists only (no free-text in dropdown columns)
- [ ] Numerical data makes sense (no negative percentages, no >100% coverage unless multi-platform)

**Consistency Checks:**

- [ ] Platform names consistent across all sheets (Sheet 2 → Sheet 3 → Sheet 4)
- [ ] System IDs match between sheets (Sheet 3 → Sheet 4 if referenced)
- [ ] Integration names consistent (Sheet 5 → Evidence Register)
- [ ] Dates logical (Collection Date not in future, Last Log not before Deployment Date)

**Completeness Checks:**

- [ ] Every "Gap" has documented reason, owner, and target date
- [ ] Every "Exception Approved" has exception ID and approval details
- [ ] Every "Planned" item has target implementation date
- [ ] Every integration has last update timestamp
- [ ] Every log collection path has status and last verification date

## Policy Compliance

**Coverage Requirements:**

- [ ] Tier 1 (Critical) systems: 100% monitored OR approved exceptions
- [ ] Tier 2 (High) systems: >80% monitored
- [ ] Tier 3 (Medium) systems: >60% monitored
- [ ] If requirements not met: Remediation plans documented with timelines

**Capability Requirements:**

- [ ] At least one SIEM or equivalent correlation platform
- [ ] Real-time or near-real-time log collection
- [ ] Alerting capabilities documented
- [ ] Log retention meets policy (typically 90 days online, 1 year archive)
- [ ] If capabilities missing: Gap documented with remediation plan

**Infrastructure Resilience:**

- [ ] Tier 1 log collection paths have redundancy OR risk accepted
- [ ] Buffering capacity >24 hours for critical paths
- [ ] Single points of failure identified and assessed
- [ ] If resilience inadequate: Investment plan documented

**Integration Maturity:**

- [ ] Threat intelligence integration present (even if basic)
- [ ] Asset/identity enrichment present (AD, CMDB)
- [ ] Automated incident response evaluated (SOAR, ticketing)
- [ ] If integrations missing: Business justification or improvement plan

## Audit Readiness

**Traceability:**

- [ ] Can trace from policy requirement → implementation → evidence
- [ ] Example: Policy requires Tier 1 monitoring → Sheet 3 shows Tier 1 systems monitored → Sheet 8 points to verification evidence
- [ ] Every compliance claim supported by evidence
- [ ] Every gap documented with remediation plan

**Defensibility:**

- [ ] Assessment completed by qualified personnel (SOC, Security Engineering)
- [ ] Technical review completed and documented
- [ ] Compliance review completed and documented
- [ ] Executive approval obtained
- [ ] All approvals signed/dated

**Evidence Package:**

- [ ] Evidence Register (Sheet 8) complete
- [ ] All referenced evidence actually exists and is accessible
- [ ] Evidence organized logically (by sheet, by type)
- [ ] Sensitive evidence properly secured (access-controlled storage)
- [ ] Evidence retention aligned with audit cycles

## Red Flags to Investigate

**If ANY of these are true, re-review before submitting:**

- [ ] ⚠️ Tier 1 coverage <100% with no documented exceptions
- [ ] ⚠️ >20% of systems marked "Monitored" but Last Log Verified >30 days ago
- [ ] ⚠️ >50% of systems have "Partial Monitoring" status (should be either Monitored or Not Monitored)
- [ ] ⚠️ Many "Exception Approved" but no exception IDs documented
- [ ] ⚠️ All monitoring platforms have "Excellent" capabilities (be honest about limitations)
- [ ] ⚠️ No single points of failure identified (every environment has some)
- [ ] ⚠️ All integrations show "Active" status but Last Update timestamps are old
- [ ] ⚠️ Performance metrics are round numbers (100%, exactly 1000 EPS) - suggests estimates not measurements
- [ ] ⚠️ Evidence Register is empty or has <10 entries (insufficient evidence)
- [ ] ⚠️ No gaps, no remediation plans (unrealistic - every organization has gaps)

**If red flags found:** Investigate and correct before proceeding to approval.

---

# Review & Approval

## Three-Level Approval Workflow

This assessment requires approval at three levels to ensure technical accuracy, policy compliance, and strategic alignment.

### Level 1: Technical Review

**Reviewer:** SOC Lead / Security Engineering Manager  
**Timeline:** 2-3 business days  
**Focus:** Technical accuracy, operational feasibility

**Review Criteria:**

**Technical Accuracy:**

- [ ] All monitoring platforms documented with correct versions
- [ ] Platform capabilities accurately assessed (not overstated)
- [ ] Log source inventory complete and verified
- [ ] Monitoring status verified (not assumed) - logs actually flowing
- [ ] Data collection architecture accurately reflects actual implementation
- [ ] Integration configurations documented correctly

**Operational Feasibility:**

- [ ] Remediation plans are realistic (timelines achievable)
- [ ] Resource requirements identified (budget, staff, tools)
- [ ] Dependencies documented (network changes, approvals needed)
- [ ] Operational impact assessed (will remediation cause outages?)

**Completeness:**

- [ ] All monitoring technologies documented (not just primary SIEM)
- [ ] All Tier 1 and Tier 2 systems included
- [ ] Architecture includes all log collection paths
- [ ] Performance metrics from actual measurements

**Reviewer Actions:**
1. Review all sheets for technical accuracy
2. Spot-check monitoring status (verify 10-20 systems in SIEM)
3. Validate architecture against actual deployment
4. Confirm remediation plans are achievable
5. Document findings in approval sheet (Sheet 9)
6. **If Approved:** Sign off and forward to Level 2
7. **If Rejected:** Return to assessor with specific corrections needed

---

### Level 2: Compliance Review

**Reviewer:** Security Manager / Compliance Officer / CISO  
**Timeline:** 3-5 business days  
**Focus:** Policy compliance, risk assessment

**Review Criteria:**

**Policy Compliance:**

- [ ] Coverage meets policy thresholds:
  - Tier 1: 100% monitored or approved exceptions
  - Tier 2: >80% monitored
  - Tier 3: >60% monitored
- [ ] Platform capabilities meet policy requirements
- [ ] Log retention complies with policy (90 days online, 1 year archive)
- [ ] Infrastructure resilience adequate for Tier 1 systems
- [ ] Integration requirements met (threat intel, enrichment)

**Risk Assessment:**

- [ ] Unmonitored Tier 1 systems have risk acceptance documentation
- [ ] Single points of failure identified and risk assessed
- [ ] Coverage gaps have appropriate remediation timelines:
  - Critical (Tier 1 Full Gap): ≤30 days
  - High (Tier 2 Full Gap): ≤90 days
- [ ] Residual risk documented for approved exceptions

**Gap Remediation:**

- [ ] All gaps have documented remediation plans
- [ ] Remediation plans have assigned owners
- [ ] Remediation timelines are tracked
- [ ] Resource requirements identified (budget allocation needed?)
- [ ] Compensating controls documented for delayed remediations

**Exception Management:**

- [ ] All exceptions formally requested
- [ ] Exception justifications are valid (technical limitations, business requirements)
- [ ] Compensating controls documented and adequate
- [ ] Exception review dates set (annual re-approval)

**Reviewer Actions:**
1. Review compliance against ISMS-POL-A.8.16 requirements
2. Assess risk posture based on documented gaps
3. Validate exception approvals are properly documented
4. Confirm remediation plans align with risk prioritization
5. Document findings in approval sheet (Sheet 9)
6. **If Approved:** Sign off and forward to Level 3
7. **If Approved with Conditions:** Document required actions before next review
8. **If Rejected:** Return to assessor with compliance gaps to address

---

### Level 3: Executive Approval

**Reviewer:** CISO / CIO  
**Timeline:** 5-7 business days  
**Focus:** Strategic alignment, resource commitment, risk acceptance

**Review Criteria:**

**Strategic Alignment:**

- [ ] Monitoring strategy supports business objectives
- [ ] Monitoring coverage aligns with critical business systems
- [ ] Investment priorities align with organizational risk appetite
- [ ] Monitoring capabilities support regulatory compliance (ISO 27001, GDPR, etc.)

**Resource Commitment:**

- [ ] Budget requirements for remediation identified
- [ ] Staffing requirements assessed (SOC scaling, engineering effort)
- [ ] Technology investments justified (new platforms, capacity expansion)
- [ ] Remediation timeline realistic given competing priorities

**Risk Acceptance:**

- [ ] Residual risks from monitoring gaps understood
- [ ] Accepted risks documented formally
- [ ] Risk acceptance aligns with organizational risk appetite
- [ ] Board-level reporting adequate (if significant risks exist)

**Executive Decision Points:**
1. **Accept Assessment:** Monitoring posture adequate, no major concerns
2. **Accept with Investments:** Approve with commitment to fund identified gaps
3. **Accept with Risk:** Acknowledge gaps, formally accept residual risk
4. **Reject:** Monitoring posture inadequate, requires significant improvement before acceptance

**Reviewer Actions:**
1. Review executive summary (Sheet 7 - Summary Dashboard)
2. Review critical gaps and remediation plans
3. Assess resource requirements (budget, staff, technology)
4. Determine risk acceptance for documented gaps
5. Document decision in approval sheet (Sheet 9)
6. **If Approved:** Final sign-off, assessment complete
7. **If Approved with Conditions:** Document investment commitments or risk acceptances
8. **If Rejected:** Require re-assessment or escalate to Board if necessary

---

## Approval Timeline

**Total Duration:** 10-15 business days

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Assessment Completion | (Prerequisite) | Day 0 |
| Level 1: Technical Review | 2-3 days | Day 3 |
| Level 2: Compliance Review | 3-5 days | Day 8 |
| Level 3: Executive Approval | 5-7 days | Day 15 |

**Expedited Process:**

- If critical security gap discovered: Escalate directly to CISO (same-day review)
- If minimal findings: Levels 1-2 can be combined (5-7 days total)

---

## Post-Approval Actions

**Once all approvals obtained:**

1. **Finalize Documentation:**

   - Ensure all approval signatures collected
   - Archive completed assessment in document repository
   - Update ISMS documentation register

2. **Remediation Tracking:**

   - Extract gap remediation list from Sheet 3, 4, 5
   - Create project tickets for each remediation item
   - Assign owners and deadlines per assessment
   - Track progress in project management system

3. **Reporting:**

   - Present Summary Dashboard (Sheet 7) to management
   - Report critical gaps to Board/Executive Committee if required
   - Include monitoring posture in quarterly ISMS reporting

4. **Schedule Next Review:**

   - Set calendar reminder for next assessment (6 months)
   - Trigger ad-hoc reviews if major infrastructure changes occur

5. **Continuous Improvement:**

   - Incorporate lessons learned into next assessment cycle
   - Update assessment templates based on feedback
   - Automate data collection where possible

---

**END OF SPECIFICATION**

---

*"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
