# ISMS Control A.8.15 - Logging
## Implementation Roadmap & Project Plan
### System Engineering Approach

**Project ID**: ISMS-A.8.15-SE  
**Control**: ISO/IEC 27001:2022 Annex A Control 8.15 - Logging  
**Approach**: System Engineering (SE) - Policy-driven with Python-generated Excel assessments  
**Reference Project**: ISMS Control 8.23 (Web Filtering)  
**Date**: 05.01.2026  
**Status**: Planning Phase

---

## 1. Executive Summary

### 1.1 Control Overview
**Control 8.15 - Logging** (ISO/IEC 27002:2022 Section 8.15)

**Purpose**: Event logs recording user activities, exceptions, faults and information security events shall be produced, kept, and regularly reviewed.

**Scope**: 
- All systems, applications, and network devices requiring audit trails
- Security-relevant events across infrastructure and applications
- Administrative and operator activities
- Exception and error conditions
- Information security events and incidents

**Key Attributes**:
- Maßnahmenart: #Detektiv (Detective)
- Informationssicherheitseigenschaften: #Vertraulichkeit, #Integrität, #Verfügbarkeit
- Konzepte zur Cybersicherheit: #Erkennen (Detect), #Verteidigung (Defend)
- Sicherheitsdomänen: #Handhabung_von_Informationssicherheitsereignissen, #Schutz

### 1.2 System Engineering Approach

**Philosophy**: As Feynman said, "What I cannot create, I do not understand." 

We implement through:
1. **Policy Definition** → Clear, auditable requirements (MD documents)
2. **Assessment Tooling** → Python-generated Excel workbooks for stakeholder input
3. **Evidence Collection** → Structured data gathering with validation
4. **Compliance Dashboard** → Aggregated view from all assessments
5. **Continuous Improvement** → Gap-driven remediation

**No Cargo Cult**: We document what we ACTUALLY do, not what we THINK we should do.

---

## 2. Document Structure

### 2.1 Policy Documents (POL)
```
ISMS-POL-A_8_15_-_Logging_Policy.md (Main - max 400 lines)
│
├── ISMS-POL-A_8_15-S1_-_Purpose_Scope_Definitions.md (~300 lines)
│   ├── 1.1 Purpose
│   ├── 1.2 Scope
│   ├── 1.3 Regulatory Framework
│   ├── 1.4 Definitions
│   └── 1.5 Document Structure
│
├── ISMS-POL-A_8_15-S2_-_Requirements_Overview.md (~300 lines)
│   └── Overview of all logging requirements
│
├── ISMS-POL-A_8_15-S2_1_-_Event_Logging_Requirements.md (~350 lines)
│   ├── 2.1.1 Mandatory Log Events
│   ├── 2.1.2 Log Event Categories
│   ├── 2.1.3 Log Content Requirements
│   ├── 2.1.4 System-Specific Logging
│   ├── 2.1.5 Application Logging
│   └── 2.1.6 Network Device Logging
│
├── ISMS-POL-A_8_15-S2_2_-_Log_Protection_Integrity.md (~350 lines)
│   ├── 2.2.1 Log Integrity Protection
│   ├── 2.2.2 Access Controls
│   ├── 2.2.3 Tamper Detection
│   ├── 2.2.4 Secure Transport
│   ├── 2.2.5 Write-Once Storage
│   └── 2.2.6 Cryptographic Protection
│
├── ISMS-POL-A_8_15-S2_3_-_Log_Retention_Storage.md (~350 lines)
│   ├── 2.3.1 Retention Periods
│   ├── 2.3.2 Storage Tiers
│   ├── 2.3.3 Archival Requirements
│   ├── 2.3.4 Disposal Procedures
│   ├── 2.3.5 Legal Hold
│   └── 2.3.6 Storage Capacity Planning
│
├── ISMS-POL-A_8_15-S2_4_-_Log_Review_Analysis.md (~350 lines)
│   ├── 2.4.1 Review Frequency
│   ├── 2.4.2 Automated Analysis
│   ├── 2.4.3 Anomaly Detection
│   ├── 2.4.4 Correlation Rules
│   ├── 2.4.5 Alerting Thresholds
│   ├── 2.4.6 Investigation Procedures
│   └── 2.4.7 Reporting Requirements
│
├── ISMS-POL-A_8_15-S3_-_Roles_Responsibilities.md (~300 lines)
│   ├── 3.1 Governance Model
│   ├── 3.2 RACI Matrix
│   ├── 3.3 Role Definitions
│   ├── 3.4 Escalation Paths
│   └── 3.5 Competency Requirements
│
├── ISMS-POL-A_8_15-S4_-_Policy_Governance.md (~300 lines)
│   ├── 4.1 Policy Lifecycle
│   ├── 4.2 Version Control
│   ├── 4.3 Development Process
│   ├── 4.4 Approval Workflow
│   ├── 4.5 Publication & Distribution
│   ├── 4.6 Training Requirements
│   ├── 4.7 Periodic Review
│   ├── 4.8 Change Management
│   └── 4.9 ISMS Integration
│
└── ISMS-POL-A_8_15-S5_-_Annexes.md (~250 lines)
    ├── ISMS-POL-A_8_15-S5_A_-_Logging_Standards.md (~350 lines)
    │   ├── A.1 Log Format Standards
    │   ├── A.2 Syslog Configuration
    │   ├── A.3 Common Event Format (CEF)
    │   ├── A.4 JSON Logging Standards
    │   └── A.5 Timestamp Standards
    │
    ├── ISMS-POL-A_8_15-S5_B_-_Log_Source_Template.md (~300 lines)
    │   └── Template for documenting new log sources
    │
    ├── ISMS-POL-A_8_15-S5_C_-_Log_Review_Procedures.md (~350 lines)
    │   ├── C.1 Daily Review Procedures
    │   ├── C.2 Weekly Review Procedures
    │   ├── C.3 Monthly Review Procedures
    │   ├── C.4 Incident Response Procedures
    │   └── C.5 Forensic Investigation Procedures
    │
    └── ISMS-POL-A_8_15-S5_D_-_Quick_Reference_Guide.md (~300 lines)
        ├── D.1 Decision Trees
        ├── D.2 Common Scenarios
        ├── D.3 Troubleshooting Guide
        └── D.4 FAQ
```

**Total Policy Documents**: 16 files (~5,000 lines total)

### 2.2 Implementation Assessment Documents (IMP)
```
├── ISMS-IMP-A_8_15_1_-_Log_Source_Inventory.md (~300 lines)
│   └── Excel workbook specification for cataloging all log sources
│
├── ISMS-IMP-A_8_15_2_-_Log_Collection_Centralization.md (~300 lines)
│   └── Assessment of centralized logging infrastructure (SIEM/Log Management)
│
├── ISMS-IMP-A_8_15_3_-_Log_Protection_Retention.md (~300 lines)
│   └── Assessment of log integrity, access controls, and retention compliance
│
├── ISMS-IMP-A_8_15_4_-_Log_Analysis_Review.md (~300 lines)
│   └── Assessment of log review processes, automation, and effectiveness
│
└── ISMS-IMP-A_8_15_5_-_Compliance_Dashboard.md (~300 lines)
    └── Consolidated compliance view aggregating data from IMP-1 through IMP-4
```

**Total IMP Documents**: 5 files (~1,500 lines total)

### 2.3 Python Scripts
```
├── generate_a815_1_log_source_inventory.py (~800-1000 lines)
│   └── Generates Excel for comprehensive log source catalog
│
├── generate_a815_2_log_collection_centralization.py (~800-1000 lines)
│   └── Generates Excel for SIEM/log management assessment
│
├── generate_a815_3_log_protection_retention.py (~800-1000 lines)
│   └── Generates Excel for log protection and retention assessment
│
├── generate_a815_4_log_analysis_review.py (~800-1000 lines)
│   └── Generates Excel for log analysis and review assessment
│
├── generate_a815_5_compliance_dashboard.py (~1000-1200 lines)
│   └── Generates master Excel dashboard consolidating all assessments
│
└── excel_sanity_check_a815.py (~200-300 lines)
    └── Validation script to verify Excel workbook generation
```

**Total Python Scripts**: 6 files (~5,000-6,000 lines total)

---

## 3. Detailed Implementation Plan

### Phase 1: Policy Development (Weeks 1-4)

#### Week 1: Foundation Documents
- [ ] **ISMS-POL-A_8_15-S1** - Purpose, Scope, Definitions
- [ ] **ISMS-POL-A_8_15-S2** - Requirements Overview
- [ ] Review ISO 27002:2022 Section 8.15 guidance
- [ ] Analyze regulatory requirements (FADP, GDPR, DORA, NIS2)

#### Week 2: Core Requirements (S2.1 - S2.2)
- [ ] **ISMS-POL-A_8_15-S2_1** - Event Logging Requirements
  - Mandatory log events
  - System, application, network logging requirements
  - Log content standards
- [ ] **ISMS-POL-A_8_15-S2_2** - Log Protection & Integrity
  - Access controls and integrity protection
  - Tamper detection mechanisms
  - Secure transport and storage

#### Week 3: Advanced Requirements (S2.3 - S2.4)
- [ ] **ISMS-POL-A_8_15-S2_3** - Log Retention & Storage
  - Retention periods by log type
  - Storage tier architecture (hot/warm/cold)
  - Archival and disposal procedures
- [ ] **ISMS-POL-A_8_15-S2_4** - Log Review & Analysis
  - Review frequency and procedures
  - Automated analysis and correlation
  - Alerting and investigation

#### Week 4: Governance & Annexes
- [ ] **ISMS-POL-A_8_15-S3** - Roles & Responsibilities
- [ ] **ISMS-POL-A_8_15-S4** - Policy Governance
- [ ] **ISMS-POL-A_8_15-S5** - Annexes Overview
- [ ] **ISMS-POL-A_8_15-S5_A** - Logging Standards (syslog, CEF, JSON)
- [ ] **ISMS-POL-A_8_15-S5_B** - Log Source Template
- [ ] **ISMS-POL-A_8_15-S5_C** - Log Review Procedures
- [ ] **ISMS-POL-A_8_15-S5_D** - Quick Reference Guide
- [ ] **ISMS-POL-A_8_15** - Main Policy (consolidation)

---

### Phase 2: Implementation Assessment Specifications (Weeks 5-6)

#### Week 5: Assessment Specs (IMP-1 and IMP-2)
- [ ] **ISMS-IMP-A_8_15_1** - Log Source Inventory Specification
  - Sheet structure for cataloging all log sources
  - Fields: System, Log Type, Format, Volume, Retention, Owner
  - Evidence requirements
  
- [ ] **ISMS-IMP-A_8_15_2** - Log Collection & Centralization Specification
  - SIEM/Log Management platform assessment
  - Log forwarding mechanisms
  - Collection reliability metrics

#### Week 6: Assessment Specs (IMP-3, IMP-4, IMP-5)
- [ ] **ISMS-IMP-A_8_15_3** - Log Protection & Retention Specification
  - Access control assessment
  - Integrity protection mechanisms
  - Retention compliance tracking
  
- [ ] **ISMS-IMP-A_8_15_4** - Log Analysis & Review Specification
  - Review process assessment
  - Automation maturity
  - KPI tracking
  
- [ ] **ISMS-IMP-A_8_15_5** - Compliance Dashboard Specification
  - Consolidated scoring methodology
  - Gap aggregation
  - Executive reporting structure

---

### Phase 3: Python Script Development (Weeks 7-10)

#### Week 7: Core Generators (Scripts 1-2)
- [ ] **generate_a815_1_log_source_inventory.py**
  - Workbook: ~12 sheets, ~800 rows
  - Sheets: Instructions, Log_Sources, Systems_Inventory, Applications, Network_Devices, Security_Tools, Database_Logs, Cloud_Services, Gaps, Evidence, Approval
  - Dynamic dropdowns, conditional formatting, formulas
  
- [ ] **generate_a815_2_log_collection_centralization.py**
  - Workbook: ~11 sheets, ~700 rows
  - Sheets: Instructions, SIEM_Platform, Log_Forwarders, Collection_Coverage, Reliability_Metrics, Integration_Status, Data_Flows, Gaps, Evidence, Approval

#### Week 8: Protection & Analysis Generators (Scripts 3-4)
- [ ] **generate_a815_3_log_protection_retention.py**
  - Workbook: ~11 sheets, ~700 rows
  - Sheets: Instructions, Access_Controls, Integrity_Protection, Encryption_Transit, Retention_Compliance, Storage_Tiers, Archival_Process, Gaps, Evidence, Approval
  
- [ ] **generate_a815_4_log_analysis_review.py**
  - Workbook: ~11 sheets, ~700 rows
  - Sheets: Instructions, Review_Schedule, Automated_Analysis, Correlation_Rules, Alerting_Config, Investigation_Process, KPI_Tracking, Gaps, Evidence, Approval

#### Week 9: Dashboard Generator (Script 5)
- [ ] **generate_a815_5_compliance_dashboard.py**
  - Master workbook: ~12 sheets, ~800 rows
  - Sheets: Executive_Summary, Domain_1_Summary, Domain_2_Summary, Domain_3_Summary, Domain_4_Summary, Compliance_Score, Gap_Consolidation, Action_Plan, Evidence_Index, KPI_Dashboard, Trends, Approval
  - Aggregation formulas from IMP-1 through IMP-4
  - Maturity model calculation
  - Gap prioritization

#### Week 10: Validation & Testing
- [ ] **excel_sanity_check_a815.py**
  - Generate all 5 workbooks
  - Validate structure (sheet count, column headers)
  - Test formulas and dropdowns
  - Verify conditional formatting
  - Check file size and performance
  
- [ ] Integration testing
  - Test data flow from IMP-1→IMP-5
  - Validate aggregation formulas
  - Test edge cases (empty data, max data)
  - Performance testing with large datasets

---

### Phase 4: Documentation & Rollout (Weeks 11-12)

#### Week 11: Documentation Finalization
- [ ] Review all policy documents for consistency
- [ ] Cross-reference verification (all links valid)
- [ ] Generate PDF versions of policies
- [ ] Create training materials
- [ ] Develop implementation guide

#### Week 12: Stakeholder Rollout
- [ ] CISO approval of policy framework
- [ ] Present to Security Steering Committee
- [ ] Train system owners on Excel workbooks
- [ ] Distribute IMP workbooks to stakeholders
- [ ] Schedule initial assessment period (30-60 days)
- [ ] Plan follow-up workshops for gap remediation

---

## 4. Excel Workbook Design

### 4.1 Domain Structure

**Domain 1: Log Source Inventory** (ISMS-IMP-A_8_15_1)
- Comprehensive catalog of all systems generating logs
- Completeness assessment (are we logging everything?)
- Classification by system type, criticality, data sensitivity

**Domain 2: Log Collection & Centralization** (ISMS-IMP-A_8_15_2)
- SIEM/Log Management platform capabilities
- Log forwarding infrastructure
- Collection reliability and coverage
- Integration with IT service management

**Domain 3: Log Protection & Retention** (ISMS-IMP-A_8_15_3)
- Access control implementation
- Integrity protection mechanisms (WORM, signatures, blockchain)
- Retention compliance by log type
- Archival and disposal procedures

**Domain 4: Log Analysis & Review** (ISMS-IMP-A_8_15_4)
- Manual review schedules and procedures
- Automated analysis (SIEM rules, ML/AI)
- Correlation and enrichment
- Alerting and incident response integration
- KPI tracking and effectiveness measurement

**Domain 5: Compliance Dashboard** (ISMS-IMP-A_8_15_5)
- Executive summary with traffic light status
- Aggregated compliance score calculation
- Gap consolidation with prioritization
- Remediation action plan tracking
- Evidence index referencing Domains 1-4

### 4.2 Workbook Sheet Structure (Standard Pattern)

Each Domain workbook follows consistent structure:
```
Sheet 1:  Instructions_Legend (~50 rows)
Sheet 2:  [Domain-Specific Assessment] (~100-150 rows)
Sheet 3:  [Domain-Specific Detail] (~100-150 rows)
Sheet 4:  [Domain-Specific Metrics] (~80-120 rows)
Sheet 5:  [Domain-Specific Configuration] (~80-120 rows)
Sheet 6:  [Domain-Specific Analysis] (~80-100 rows)
Sheet 7:  Gap_Analysis (~70-90 rows)
Sheet 8:  Evidence_Register (~110 rows - 100 evidence items)
Sheet 9:  KPI_Metrics (~60-80 rows)
Sheet 10: Approval_Sign_Off (~30 rows - 3-level approval)
Sheet 11: [Domain-Specific Summary] (~50 rows - optional)
```

**Compliance Dashboard** has different structure:
- Executive summaries from each domain
- Consolidated scoring
- Master gap register
- Master evidence index
- Action plan with timeline
- Trend analysis

### 4.3 Color Coding Standard
```python
COLORS = {
    "header_dark": "003366",      # Dark blue - main headers
    "header_medium": "4472C4",    # Medium blue - subheaders
    "header_light": "8FAADC",     # Light blue - section headers
    "input_yellow": "FFFFCC",     # Yellow - user input cells
    "status_green": "C6EFCE",     # Green - Implemented/Compliant
    "status_yellow": "FFEB9C",    # Yellow/Amber - Partial
    "status_red": "FFC7CE",       # Red - Not Implemented/Non-Compliant
    "status_blue": "BDD7EE",      # Blue - Planned
    "status_gray": "D9D9D9",      # Gray - N/A
    "white": "FFFFFF",
    "black": "000000",
    "light_gray": "F2F2F2",
}
```

### 4.4 Status Values (Data Validation)

**Implementation Status:**
- Implemented
- Partial
- Planned
- Not Implemented
- N/A

**Compliance Status:**
- Compliant
- Partial Compliance
- Non-Compliant
- Under Review
- N/A

**Priority (for Gaps):**
- Critical (30 days)
- High (90 days)
- Medium (180 days)
- Low (365 days)

---

## 5. Key Deliverables

### 5.1 Policy Documents
- [ ] 16 MD files (main + sections + annexes)
- [ ] All in code blocks for easy copy/paste
- [ ] Date format: DD.MM.YYYY
- [ ] Max 300-400 lines per file

### 5.2 Implementation Specifications
- [ ] 5 IMP MD files specifying Excel layouts
- [ ] Column definitions, formulas, validations
- [ ] Evidence requirements per domain

### 5.3 Python Scripts
- [ ] 5 generator scripts (one per domain)
- [ ] 1 sanity check script
- [ ] Output filename format: ISMS-IMP-A_8_15_X_Description_YYYYMMDD.xlsx
- [ ] Date in Excel: DD.MM.YYYY

### 5.4 Generated Excel Workbooks
- [ ] ISMS-IMP-A_8_15_1_Log_Source_Inventory_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A_8_15_2_Log_Collection_Centralization_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A_8_15_3_Log_Protection_Retention_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A_8_15_4_Log_Analysis_Review_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A_8_15_5_Compliance_Dashboard_YYYYMMDD.xlsx

### 5.5 Documentation
- [ ] Implementation guide for system owners
- [ ] Training materials
- [ ] FAQ document
- [ ] This roadmap (project plan)

---

## 6. Success Criteria

### 6.1 Policy Framework
- ✅ Complete policy framework covering all ISO 27002:2022 8.15 requirements
- ✅ Clear, auditable requirements with SHALL/SHOULD/MAY
- ✅ Integration with ISMS-POL-00 (Regulatory Applicability Framework)
- ✅ CISO approval obtained

### 6.2 Implementation Tools
- ✅ All 5 Python scripts execute without errors
- ✅ Generated Excel workbooks are functional and user-friendly
- ✅ Formulas calculate correctly
- ✅ Data validation prevents invalid input
- ✅ Conditional formatting provides visual feedback

### 6.3 Assessment Execution
- ✅ Stakeholders complete workbooks within assessment period
- ✅ Evidence artifacts referenced and validated
- ✅ Gaps identified with realistic remediation plans
- ✅ Compliance dashboard provides meaningful insights

### 6.4 Audit Readiness
- ✅ Policy documentation complete and approved
- ✅ Implementation evidence available in workbooks
- ✅ Gap remediation tracking in place
- ✅ Auditors can independently verify compliance

---

## 7. Risk & Mitigation

### 7.1 Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Scope creep (too many log sources) | High | Medium | Focus on critical systems first, phase approach |
| Stakeholder availability | Medium | High | Provide clear deadlines, executive sponsorship |
| Technical complexity (SIEM integration) | Medium | Medium | Engage vendor support, pilot testing |
| Policy-practice mismatch | High | Medium | Iterate based on assessment findings |
| Resource constraints | Medium | Medium | Prioritize critical domains, extend timeline |

### 7.2 Dependencies

- SIEM/Log Management platform operational
- System owners identified and available
- ISMS-POL-00 (Regulatory Framework) approved
- Control 8.16 (Monitoring) alignment (related control)
- Control 8.17 (Clock Synchronization) implemented

---

## 8. Assumptions

1. Organization has existing logging infrastructure (systems generate logs)
2. Central log collection capability exists (SIEM or equivalent)
3. System owners can dedicate 4-8 hours for assessment completion
4. Python 3.8+ and openpyxl library available for script execution
5. Excel 2016+ or compatible spreadsheet software available
6. ISO 27001:2022 certification scope includes Control 8.15

---

## 9. Out of Scope

The following are **NOT** included in this project:

- ❌ Procurement of SIEM or log management platforms
- ❌ Implementation of missing logging capabilities
- ❌ Development of custom log parsers or collectors
- ❌ Gap remediation execution (covered by separate projects)
- ❌ Control 8.16 (Monitoring Activities) - separate control
- ❌ Control 8.17 (Clock Synchronization) - separate control
- ❌ SOC procedure development (covered in S5_C)

---

## 10. Approval & Sign-Off

### 10.1 Project Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project Sponsor (CISO) | [Name] | [DD.MM.YYYY] | __________ |
| Information Security Manager | [Name] | [DD.MM.YYYY] | __________ |
| IT Operations Manager | [Name] | [DD.MM.YYYY] | __________ |
| Project Lead | [Name] | [DD.MM.YYYY] | __________ |

### 10.2 Milestone Acceptance

| Milestone | Planned Date | Actual Date | Status |
|-----------|--------------|-------------|--------|
| Phase 1: Policy Development | Week 4 | | ⏳ |
| Phase 2: Assessment Specs | Week 6 | | ⏳ |
| Phase 3: Script Development | Week 10 | | ⏳ |
| Phase 4: Rollout | Week 12 | | ⏳ |

---

## 11. Next Steps

### Immediate Actions (This Week)
1. [ ] Obtain executive sponsorship and project approval
2. [ ] Confirm resource availability (policy author, Python developer)
3. [ ] Review and finalize this roadmap with stakeholders
4. [ ] Set up project workspace (Git repository, document repository)
5. [ ] Schedule kickoff meeting with Security Steering Committee

### Week 1 Actions
1. [ ] Begin ISMS-POL-A_8_15-S1 (Purpose, Scope, Definitions)
2. [ ] Review ISO 27002:2022 Section 8.15 in detail
3. [ ] Analyze logging requirements from FADP, GDPR, DORA, NIS2
4. [ ] Inventory existing organizational logging policies
5. [ ] Identify key stakeholders for each domain

---

## 12. References

### 12.1 Standards & Frameworks
- ISO/IEC 27001:2022 - Clause 8.15 (Logging)
- ISO/IEC 27002:2022 - Section 8.15 (Event logging)
- NIST SP 800-92 - Guide to Computer Security Log Management
- CIS Controls v8 - Control 8 (Audit Log Management)
- PCI DSS 4.0 - Requirement 10 (Log and Monitor All Access)

### 12.2 Regulatory
- FADP (Swiss Federal Data Protection Act) - Audit trail requirements
- GDPR - Article 32(1)(d) - Logging for security of processing
- DORA (Digital Operational Resilience Act) - ICT-related incident management and logging
- NIS2 - Security monitoring and incident detection

### 12.3 Technical References
- RFC 5424 - The Syslog Protocol
- RFC 3195 - Reliable Delivery for Syslog
- Common Event Format (CEF) - ArcSight
- OWASP Logging Cheat Sheet

### 12.4 Project References
- ISMS-POL-00 - Regulatory Applicability Framework
- ISMS Control A.8.23 - Web Filtering (reference implementation)
- ISMS-IMP-A_8_23_4 - Monitoring & Response (related control)

---

## 13. Appendix: Quick Decision Matrix

### When to Log (Decision Tree)
```
                    Is it a system/application/network device?
                                    │
                        ┌───────────┴───────────┐
                       YES                     NO
                        │                       │
            Does it process sensitive data  [Out of scope]
            or perform security functions?
                        │
                ┌───────┴────────┐
               YES              NO
                │                │
          [MUST LOG]      [SHOULD LOG if
                          business-critical]
```

### Log Retention (Quick Reference)
```
Security Event Logs:    12 months minimum (hot), 7 years archive
Authentication Logs:    12 months minimum (hot), 7 years archive
Administrative Logs:    12 months minimum (hot), 3 years archive
Application Logs:       6 months minimum (hot), 1 year archive
System Logs:            6 months minimum (hot), 1 year archive
Network Device Logs:    6 months minimum (hot), 1 year archive

Note: Adjust based on regulatory requirements and legal hold obligations
```

---

## 14. Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-A.8.15-ROADMAP |
| **Version** | 1.0 |
| **Date** | 05.01.2026 |
| **Author** | [Project Lead] |
| **Reviewers** | CISO, Information Security Manager, IT Operations |
| **Status** | Draft → Pending Approval |
| **Classification** | Internal |
| **Next Review** | Upon Phase 1 completion |

---

**END OF ROADMAP**

---

*"The first principle is that you must not fool yourself—and you are the easiest person to fool."*  
— Richard Feynman

*"Cargo cult science: We're not just copying forms, we're understanding the substance."*  
— Adapted from Feynman's Caltech commencement address

*"Event logs that nobody reads are just expensive write-only memory."*  
— Ancient ISMS Proverb