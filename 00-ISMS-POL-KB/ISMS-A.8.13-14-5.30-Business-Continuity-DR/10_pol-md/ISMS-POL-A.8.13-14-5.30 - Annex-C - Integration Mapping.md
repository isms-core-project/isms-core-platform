# ISMS-POL-A.8.13-14-5.30-Annex-C: Integration Mapping

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Chief Information Security Officer (CISO)  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / CISO | Initial integration mapping for BC/DR controls |

---

## Table of Contents

1. [Purpose of Integration Mapping](#1-purpose-of-integration-mapping)
2. [BC/DR Controls Integration with Asset Management](#2-bcdr-controls-integration-with-asset-management)
3. [BC/DR Controls Integration with Operations Management](#3-bcdr-controls-integration-with-operations-management)
4. [BC/DR Controls Integration with Supplier Management](#4-bcdr-controls-integration-with-supplier-management)
5. [BC/DR Controls Integration with Incident Management](#5-bcdr-controls-integration-with-incident-management)
6. [BC/DR Controls Integration with Configuration Management](#6-bcdr-controls-integration-with-configuration-management)
7. [Evidence Flow Between Controls](#7-evidence-flow-between-controls)
8. [Unified Compliance Approach](#8-unified-compliance-approach)

---

## 1. Purpose of Integration Mapping

### 1.1 Why Integration Matters

ISO 27001:2022 controls are not independent silos—they form an integrated Information Security Management System. BC/DR controls (A.8.13, A.8.14, A.5.30) have particularly strong integration points with other controls.

**Benefits of Understanding Integration:**
- **Avoid Duplication:** Don't duplicate work already done for other controls
- **Leverage Existing Data:** Use asset inventory, configuration data, monitoring data for BC/DR
- **Holistic Compliance:** Integrated controls provide better overall security posture
- **Efficient Auditing:** Single evidence can support multiple controls

### 1.2 Scope of This Annex

This annex documents integration points between BC/DR controls and other ISMS controls:
- What data/evidence flows between controls
- How controls depend on each other
- Where joint testing makes sense
- Where single evidence supports multiple controls

---

## 2. BC/DR Controls Integration with Asset Management

### 2.1 Control A.5.9 - Inventory of Information and Other Associated Assets

**Integration Points:**

**A.5.9 → BC/DR (Dependency):**
- BC/DR requires **complete and accurate asset inventory**
- Cannot backup or protect systems not in inventory
- Asset criticality classification in A.5.9 drives BC/DR requirements

**Data Flow:**
- Asset inventory (from A.5.9) → Systems requiring backup/redundancy (in BC/DR)
- Asset criticality (from A.5.9) → RPO/RTO requirements (in BC/DR)
- Asset owners (from A.5.9) → BIA stakeholders (in BC/DR)

**Practical Integration:**
- Assessment Workbook 1 (Backup Inventory) references asset inventory from A.5.9
- Assessment Workbook 2 (Redundancy Analysis) references asset inventory
- BIA process (A.5.30) uses asset inventory as starting point

**Evidence Sharing:**
- Asset inventory spreadsheet supports both A.5.9 and BC/DR compliance
- Asset criticality documentation supports A.5.9 and BC/DR requirements determination

**Testing Integration:**
- Asset inventory updates trigger BC/DR review (new assets need backup/redundancy)
- BC/DR testing may identify assets missing from inventory (update A.5.9)

### 2.2 Control A.5.10 - Acceptable Use of Information and Other Associated Assets

**Integration Points:**

**A.5.10 → BC/DR:**
- Acceptable use policy may restrict what can be backed up or where (data residency, privacy)
- Acceptable use defines who can restore data (access controls during recovery)

**BC/DR → A.5.10:**
- BC/DR procedures must comply with acceptable use (can't restore data to unauthorized locations)

---

## 3. BC/DR Controls Integration with Operations Management

### 3.1 Control A.8.6 - Capacity Management

**Integration Points:**

**Bidirectional Dependency:**

**A.8.6 → BC/DR:**
- Capacity management must account for backup storage requirements
- Capacity planning must include redundant capacity (for A.8.14)
- Capacity monitoring detects when backup storage is running out

**BC/DR → A.8.6:**
- BC/DR requirements drive capacity needs (e.g., 3× capacity for 3-2-1 backups)
- Redundancy doubles infrastructure capacity requirements

**Data Flow:**
- Backup storage utilization (from BC/DR monitoring) → Capacity planning (A.8.6)
- Backup growth trends (from BC/DR) → Storage capacity forecasting (A.8.6)
- Redundancy requirements (from BC/DR) → Infrastructure capacity planning (A.8.6)

**Practical Integration:**
- Capacity management dashboard includes backup storage metrics
- BC/DR gap analysis identifies capacity constraints
- Annual capacity planning includes BC/DR requirements

**Evidence Sharing:**
- Storage utilization reports support both A.8.6 and BC/DR monitoring
- Capacity planning documents reference BC/DR requirements

### 3.2 Control A.8.7 - Protection Against Malware

**Integration Points:**

**A.8.7 → BC/DR:**
- Malware protection critical for backup integrity (prevent ransomware from encrypting backups)
- Antimalware on backup servers and backup storage

**BC/DR → A.8.7:**
- Offline/immutable backups are last defense against ransomware (if malware protection fails)
- Recovery procedures may include malware scanning of restored systems

**Practical Integration:**
- Backup servers included in antimalware deployment (A.8.7)
- Backup storage scanned for malware
- Recovery procedures include malware verification before production restore

### 3.3 Control A.8.15 - Logging

**Integration Points:**

**Strong Bidirectional Integration:**

**A.8.15 → BC/DR:**
- Logs must be backed up (log retention requirements)
- Log backup enables forensic analysis after incidents

**BC/DR → A.8.15:**
- BC/DR events must be logged:
  - Backup job start/completion
  - Backup failures
  - Restore operations (who, what, when)
  - Failover events
  - BC/DR plan activation
  - DR test execution

**Data Flow:**
- Backup/restore logs (from BC/DR) → SIEM (A.8.15)
- Failover events (from BC/DR) → Security monitoring (A.8.15)
- DR test logs (from BC/DR) → Compliance evidence (A.8.15)

**Practical Integration:**
- Backup solution integrated with centralized logging (syslog, SIEM)
- Failover events trigger SIEM alerts
- Restore operations logged for audit trail

**Evidence Sharing:**
- Backup job logs support both BC/DR testing compliance and A.8.15 logging compliance
- Restore operation logs support BC/DR audit and security audit (who accessed what data)

### 3.4 Control A.8.16 - Monitoring Activities

**Integration Points:**

**Strong Bidirectional Integration:**

**A.8.16 → BC/DR:**
- Monitoring detects backup failures (enables rapid response)
- Monitoring detects redundancy failures (health checks, failover triggers)
- Monitoring provides early warning of capacity issues

**BC/DR → A.8.16:**
- BC/DR requires specific monitoring:
  - Backup success/failure monitoring
  - Backup storage utilization monitoring
  - Redundancy health monitoring (uptime, failover capability)
  - RPO/RTO compliance monitoring

**Data Flow:**
- Backup monitoring alerts (from BC/DR) → SOC dashboard (A.8.16)
- Redundancy health checks (from BC/DR) → Infrastructure monitoring (A.8.16)
- BC/DR compliance metrics (from BC/DR) → Management dashboards (A.8.16)

**Practical Integration:**
- Backup monitoring integrated with overall infrastructure monitoring
- BC/DR metrics included in executive dashboards
- Automated alerts for backup/failover failures

**Evidence Sharing:**
- Monitoring dashboards support both A.8.16 and BC/DR compliance
- Alert logs support both controls

### 3.5 Control A.8.19 - Installation of Software on Operational Systems

**Integration Points:**

**A.8.19 → BC/DR:**
- Backup agents must be installed per A.8.19 change control
- Redundancy software (clustering, replication) follows change control

**BC/DR → A.8.19:**
- Recovery may require software installation (restore to bare metal)
- Software installation procedures must be documented in recovery plans

---

## 4. BC/DR Controls Integration with Supplier Management

### 4.1 Control A.5.19 - Information Security in Supplier Relationships

**Integration Points:**

**A.5.19 → BC/DR:**
- Supplier contracts must include BC/DR requirements (covered in A.5.30 S4 Section 9)
- Supplier security assessment includes BC/DR capability assessment

**BC/DR → A.5.19:**
- BC/DR requirements drive supplier selection criteria
- Supplier BC/DR failures impact [Organization] BC/DR capability

**Practical Integration:**
- Supplier due diligence includes BC/DR assessment
- Supplier contracts include BC/DR SLA requirements
- Supplier incidents tracked in BC/DR risk register

### 4.2 Controls A.5.20-23 - Supplier-Specific Controls

**Integration Points:**

**Particularly A.5.21 (Managing Information Security in the ICT Supply Chain):**
- Cloud provider BC/DR capabilities critical to [Organization] BC/DR
- SaaS provider backup/redundancy impacts [Organization] data protection
- Managed service provider BC/DR impacts [Organization] operations

**BC/DR Supplier Requirements:**
- Suppliers must demonstrate BC/DR capability (testing evidence)
- Suppliers must notify [Organization] of incidents affecting BC/DR
- [Organization] may audit supplier BC/DR controls

**Evidence Sharing:**
- Supplier BC/DR assessment supports A.5.20-23 and BC/DR supplier management (A.5.30)
- Supplier SLA reviews support both controls

---

## 5. BC/DR Controls Integration with Incident Management

### 5.1 Controls A.5.24-27 - Incident Management

**Strong Integration - BC/DR Often Activated During Incidents:**

**A.5.24 (Information Security Incident Management Planning) → BC/DR:**
- Incident severity criteria may trigger BC/DR activation
- Incident response plan references BC/DR plan for major incidents

**A.5.25 (Assessment and Decision on Information Security Events) → BC/DR:**
- Incident assessment determines if BC/DR activation required
- Critical incidents (ransomware, system failures) often require BC/DR response

**A.5.26 (Response to Information Security Incidents) → BC/DR:**
- Incident response may include BC/DR procedures:
  - Restore from clean backups (ransomware response)
  - Failover to unaffected systems
  - Geographic failover (if site compromised)

**BC/DR → A.5.27 (Learning from Information Security Incidents):**
- BC/DR activation provides lessons learned
- Incident reviews identify BC/DR gaps
- Post-incident analysis improves BC/DR plans

**Data Flow:**
- Incident severity assessment → BC/DR activation decision
- BC/DR activation → Incident response actions
- Incident lessons learned → BC/DR plan updates

**Practical Integration:**
- Incident response playbooks reference BC/DR procedures
- Major incident triggers BC/DR team activation
- Post-incident reviews include BC/DR performance assessment
- BC/DR tests may simulate incident scenarios

**Evidence Sharing:**
- Incident reports document BC/DR activations
- BC/DR test results inform incident response planning
- Lessons learned from incidents improve BC/DR plans

---

## 6. BC/DR Controls Integration with Configuration Management

### 6.1 Control A.8.9 - Configuration Management

**Integration Points:**

**A.8.9 → BC/DR:**
- Configuration management provides baseline for backup
- Configuration backups critical for system restore
- Configuration management tracks what needs to be backed up

**BC/DR → A.8.9:**
- Backup includes configurations (infrastructure-as-code, system configs)
- Redundancy configurations must be managed (failover configs, cluster configs)
- Configuration changes may impact BC/DR (trigger re-testing)

**Data Flow:**
- System configurations (from A.8.9) → Backup scope (BC/DR)
- Configuration baselines (from A.8.9) → Restore verification (BC/DR)
- Configuration changes (from A.8.9) → BC/DR change impact assessment

**Practical Integration:**
- Configuration management system includes backup configurations
- Configuration changes trigger BC/DR review (does backup include new configs?)
- Restore procedures reference configuration management for baseline
- Infrastructure-as-code (IaC) configurations backed up

**Evidence Sharing:**
- Configuration documentation supports A.8.9 and BC/DR recovery procedures
- Configuration backup reports support both controls

### 6.2 Control A.8.32 - Change Management

**Integration Points:**

**A.8.32 → BC/DR:**
- Changes must be assessed for BC/DR impact
- Major changes may require BC/DR testing before production
- Change management ensures BC/DR plans updated after infrastructure changes

**BC/DR → A.8.32:**
- BC/DR plan updates follow change management process
- BC/DR infrastructure changes (backup solutions, DR site) managed as changes

**Practical Integration:**
- Change request template includes BC/DR impact assessment
- Change approval criteria include BC/DR verification
- Post-change testing includes BC/DR testing where relevant

---

## 7. Evidence Flow Between Controls

### 7.1 Single Evidence Supporting Multiple Controls

**Example 1: Asset Inventory**
- **Primary Control:** A.5.9 (Asset Inventory)
- **Also Supports:**
  - BC/DR: Systems requiring backup/redundancy
  - A.8.9: Systems requiring configuration management
  - A.8.16: Systems requiring monitoring
  - A.8.7: Systems requiring malware protection

**Evidence:** Asset inventory spreadsheet with criticality classification

**Example 2: Backup Job Logs**
- **Primary Control:** A.8.13 (Backup)
- **Also Supports:**
  - A.8.15: Logging (backup events logged)
  - A.8.16: Monitoring (backup job monitoring)
  - A.8.6: Capacity management (storage utilization)

**Evidence:** Backup solution logs and reports

**Example 3: Monitoring Dashboards**
- **Primary Control:** A.8.16 (Monitoring)
- **Also Supports:**
  - A.8.13: Backup monitoring
  - A.8.14: Redundancy health monitoring
  - A.8.6: Capacity utilization monitoring
  - A.8.15: Event monitoring

**Evidence:** Centralized monitoring dashboard screenshots

**Example 4: Supplier BC Assessment**
- **Primary Control:** A.5.19-23 (Supplier Management)
- **Also Supports:**
  - A.5.30: Supplier BC requirements (BC/DR)
  - A.8.13: Cloud backup provider assessment
  - A.8.14: Hosting provider redundancy assessment

**Evidence:** Supplier BC/DR assessment questionnaire and results

### 7.2 Evidence Consolidation Strategy

**Centralized Evidence Repository:**
- Single repository for all ISMS evidence
- Evidence tagged with applicable controls
- Reduces duplication, improves audit efficiency

**Evidence Mapping Table:**

| Evidence Type | Primary Control | Also Supports |
|---------------|----------------|---------------|
| Asset Inventory | A.5.9 | BC/DR, A.8.9, A.8.16, A.8.7 |
| Backup Logs | A.8.13 | A.8.15, A.8.16, A.8.6 |
| Failover Logs | A.8.14 | A.8.15, A.8.16 |
| Monitoring Dashboard | A.8.16 | A.8.13, A.8.14, A.8.6, A.8.15 |
| Configuration Backups | A.8.9 | A.8.13 |
| Change Records | A.8.32 | BC/DR (plan updates) |
| Incident Reports | A.5.24-27 | BC/DR (activation records) |
| Supplier Assessments | A.5.19-23 | A.5.30 (supplier BC) |
| Capacity Reports | A.8.6 | A.8.13 (backup storage) |
| BIA Documentation | A.5.30 | A.8.13 (RPO), A.8.14 (RTO) |

**Audit Efficiency:**
- Auditor asks for "backup evidence" → Provide backup logs, which also satisfy logging and monitoring controls
- Single walkthrough demonstrates integration (e.g., change management → BC/DR impact → testing)

---

## 8. Unified Compliance Approach

### 8.1 Integrated Testing

**Testing Multiple Controls Simultaneously:**

**Example: Infrastructure Failover Test**
- **Tests A.8.14:** Redundancy works (failover successful)
- **Tests A.8.15:** Failover event logged correctly
- **Tests A.8.16:** Monitoring detected failure and triggered alert
- **Tests A.5.26:** Incident response procedures worked (if framed as incident)
- **Tests A.8.32:** Change management (if failover config recently changed)

**Single test provides evidence for 4-5 controls.**

**Example: Backup Restore Test**
- **Tests A.8.13:** Backup restore works
- **Tests A.8.9:** Restored configurations match baseline
- **Tests A.8.15:** Restore operation logged
- **Tests A.8.16:** Monitoring tracked restore process

**Example: DR Simulation**
- **Tests A.5.30:** Full BC/DR plan execution
- **Tests A.8.13:** Restore from backups
- **Tests A.8.14:** Failover to DR site
- **Tests A.5.24-27:** Incident management integration
- **Tests A.8.15/16:** Logging and monitoring during crisis

**Benefits:**
- More efficient testing (single test, multiple controls verified)
- More realistic testing (controls work together in real scenarios)
- Better evidence (integrated evidence shows holistic capability)

### 8.2 Integrated Reporting

**Management Dashboard:**
- Single dashboard showing compliance across all controls
- BC/DR metrics alongside other ISMS metrics
- Holistic view of ISMS maturity

**Audit Presentation:**
- Integrated narrative: "Here's how our ISMS works end-to-end"
- Show control integration, not isolated controls
- Demonstrate mature ISMS, not checkbox compliance

### 8.3 Integrated Governance

**ISMS Steering Committee:**
- Oversees all controls, including BC/DR
- Makes integrated decisions (BC/DR investment also supports capacity management, monitoring, etc.)
- Reviews cross-control risks

**Integrated Risk Management:**
- BC/DR risks in enterprise risk register
- Risk treatment considers multiple controls
- Risk acceptance at enterprise level, not individual control level

### 8.4 Benefits of Integration

**For [Organization]:**
- More efficient ISMS implementation (less duplication)
- Better overall security posture (controls reinforce each other)
- Easier maintenance (updates propagate across controls)
- Clearer accountability (integrated governance)

**For Audits:**
- Faster audits (integrated evidence)
- Better audit results (demonstrates maturity)
- Easier audit preparation (organized evidence)

---

## Conclusion

BC/DR controls (A.8.13, A.8.14, A.5.30) are deeply integrated with other ISMS controls. Understanding and leveraging these integration points:
- Reduces implementation effort (reuse existing data and processes)
- Improves compliance (integrated controls work better)
- Streamlines audits (single evidence for multiple controls)
- Demonstrates ISMS maturity (holistic, not siloed approach)

**Key Integration Points:**
✅ **Asset Management (A.5.9):** Provides foundation for BC/DR (what to protect)  
✅ **Capacity Management (A.8.6):** BC/DR drives capacity requirements  
✅ **Logging (A.8.15):** BC/DR events must be logged  
✅ **Monitoring (A.8.16):** BC/DR capabilities must be monitored  
✅ **Supplier Management (A.5.19-23):** Supplier BC/DR critical to [Organization]  
✅ **Incident Management (A.5.24-27):** BC/DR activated during incidents  
✅ **Configuration Management (A.8.9/A.8.32):** BC/DR requires config backups and change control  

**Recommended Approach:**
- Implement controls in integrated manner (not isolation)
- Consolidate evidence (single repository, tagged with applicable controls)
- Integrate testing (test multiple controls simultaneously)
- Unified governance (integrated oversight and decision-making)

**Next Steps:**
1. Map existing evidence to multiple controls (complete evidence mapping table)
2. Plan integrated testing (combine BC/DR tests with other control testing)
3. Consolidate evidence repository (centralized, tagged evidence)
4. Integrate reporting (unified dashboards and reports)

---

**Document End**

*Integration is efficiency. Integration is maturity.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| ISMS Program Manager | | | |
| Compliance Officer | | | |
| Internal Audit Manager | | | |

**Next Review Date:** [One year from approval date]