# ISMS CONTROL 8.32 - CHANGE MANAGEMENT
## Project Roadmap & Implementation Plan
### System Engineering Approach for ISO/IEC 27001:2022 Control A.8.32

---

**Project ID:** ISMS-A.8.32-SE  
**Control Name (DE):** Änderungssteuerung  
**Control Name (EN):** Change Management / Change Control  
**Approach:** System Engineering with Python-Generated Excel Workbooks  
**Reference Model:** ISMS Control A.8.23 (Web Filtering)  
**Created:** 05.01.2026  
**Status:** Planning Phase

---

## 1. CONTROL OVERVIEW

### 1.1 ISO/IEC 27002:2022 Definition

**Control Statement:**  
> *"Änderungen an Informationsverarbeitungseinrichtungen und Informationssystemen 
> sollten Gegenstand von Änderungsmanagementverfahren sein."*

**English Translation:**  
> *"Changes to information processing facilities and information systems should be 
> subject to change management procedures."*

**Purpose:**  
Maintaining information security when implementing changes to prevent:
- System failures
- Security vulnerabilities
- Data integrity issues
- Availability disruptions
- Compliance violations

### 1.2 Control Scope (ISO 27002:2022 Requirements)

Change management procedures SHALL address:

**a) Planning & Impact Assessment**  
   - Analysis of potential impacts
   - Consideration of all dependencies
   - Risk assessment

**b) Authorization**  
   - Formal approval process
   - Authority levels
   - Documentation requirements

**c) Communication**  
   - Notification to affected stakeholders
   - Timing of communications
   - Content requirements

**d) Testing & Acceptance**  
   - Pre-deployment testing
   - Acceptance criteria
   - Sign-off procedures
   - Reference to Control 8.29 (Security Testing)

**e) Implementation**  
   - Deployment plans
   - Rollout strategies
   - Timing considerations

**f) Emergency & Contingency**  
   - Rollback procedures
   - Fallback mechanisms
   - Emergency change process

**g) Record Keeping**  
   - Change logs
   - Audit trails
   - Documentation completeness

**h) Documentation Updates**  
   - Operational documentation (see 5.37)
   - User procedures
   - Configuration documentation

**i) Continuity Plan Updates**  
   - ICT continuity plans (see 5.30)
   - Response procedures
   - Recovery procedures

### 1.3 Key Challenge: Separation of Dev/Test/Prod

**ISO 27002:2022 Guidance:**
> *"Poor control over changes to information processing facilities and information 
> systems is a common cause of system or security failures."*

Special attention required for:
- Development → Production transitions
- Software changes affecting production
- Patches, service packs, updates
- Infrastructure changes (OS, DB, middleware)

---

## 2. SYSTEM ENGINEERING APPROACH

### 2.1 Philosophy: Implementation State Documentation

**Not This (Cargo Cult):**
- Generic "Change Management Policy" that nobody reads
- 50-page procedure document that gets outdated
- Theoretical process that doesn't match reality

**This (Engineering Approach):**
- Document ACTUAL change management practices
- Stakeholders fill Excel workbooks describing THEIR process
- Evidence-based assessment of current state
- Gap analysis against ISO 27002 requirements
- Continuous improvement tracking

### 2.2 Assessment Domains (5 Workbooks)
```
┌─────────────────────────────────────────────────────────┐
│            CONTROL 8.32 ARCHITECTURE                    │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  POLICY LAYER (Markdown Documents)               │  │
│  │  - Requirements definition                       │  │
│  │  - Roles & responsibilities                      │  │
│  │  - Governance framework                          │  │
│  └──────────────────────────────────────────────────┘  │
│                          ↓                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  IMPLEMENTATION LAYER (Excel Workbooks)          │  │
│  │                                                  │  │
│  │  1. Change Process Assessment                    │  │
│  │     → Workflow, approval, documentation          │  │
│  │                                                  │  │
│  │  2. Change Types & Categories                    │  │
│  │     → Standard, normal, emergency changes        │  │
│  │                                                  │  │
│  │  3. Environment Separation Assessment            │  │
│  │     → Dev, Test, Prod isolation                  │  │
│  │                                                  │  │
│  │  4. Testing & Validation Assessment              │  │
│  │     → Testing procedures, acceptance criteria    │  │
│  │                                                  │  │
│  │  5. Change Management Compliance Dashboard       │  │
│  │     → Aggregated metrics, KPIs, gaps             │  │
│  └──────────────────────────────────────────────────┘  │
│                          ↓                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  EVIDENCE LAYER                                  │  │
│  │  - Evidence registers in each workbook           │  │
│  │  - Links to change tickets, logs                 │  │
│  │  - Approval workflows                            │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### 2.3 Technology-Agnostic Principle

**Critical Rule:** NO vendor/tool names in policies or assessments!

Organizations use different tools:
- ITSM tools (ServiceNow, Jira Service Management, BMC Remedy, etc.)
- Version control (Git, SVN, etc.)
- CI/CD pipelines (Jenkins, GitLab CI, Azure DevOps, etc.)
- Configuration management (Ansible, Terraform, Puppet, etc.)

**Approach:**
- Define generic capabilities required
- Organizations document THEIR specific tools
- Assessment validates capabilities, not products

---

## 3. DOCUMENT STRUCTURE

### 3.1 Policy Layer (13 Markdown Files)
```
ISMS-POL-A.8.32_-_Change_Management_Policy.md
│
├─ ISMS-POL-A.8.32-S1_-_Purpose__Scope__Definitions.md
│  ├─ Control objective
│  ├─ Scope boundaries
│  ├─ Key definitions (change, CAB, emergency change, etc.)
│  ├─ Regulatory context
│  └─ Exclusions
│
├─ ISMS-POL-A.8.32-S2_-_Requirements_-_Overview.md
│  └─ Framework of 4 requirement domains
│
│  ├─ ISMS-POL-A.8.32-S2_1_-_Change_Process_Requirements.md
│  │  ├─ Planning & assessment requirements
│  │  ├─ Authorization requirements
│  │  ├─ Communication requirements
│  │  ├─ Implementation requirements
│  │  └─ Documentation requirements
│  │
│  ├─ ISMS-POL-A.8.32-S2_2_-_Change_Classification_Requirements.md
│  │  ├─ Standard changes (pre-approved)
│  │  ├─ Normal changes (CAB approval)
│  │  ├─ Emergency changes (fast-track)
│  │  └─ Risk-based categorization
│  │
│  ├─ ISMS-POL-A.8.32-S2_3_-_Testing___Validation_Requirements.md
│  │  ├─ Testing environments (Dev/Test/Prod separation)
│  │  ├─ Acceptance criteria
│  │  ├─ Rollback procedures
│  │  └─ Integration with 8.29 (Security Testing)
│  │
│  └─ ISMS-POL-A.8.32-S2_4_-_Emergency_Change_Requirements.md
│     ├─ Emergency change triggers
│     ├─ Fast-track approval process
│     ├─ Post-implementation review
│     └─ Risk acceptance

├─ ISMS-POL-A.8.32-S3_-_Roles_and_Responsibilities.md
│  ├─ Change Requester
│  ├─ Change Manager
│  ├─ Change Advisory Board (CAB)
│  ├─ Change Implementer
│  ├─ Change Approver
│  ├─ Technical Reviewer
│  ├─ Security Review (integration with CISO)
│  └─ RACI matrix

├─ ISMS-POL-A.8.32-S4_-_Policy_Governance.md
│  ├─ Policy lifecycle
│  ├─ Review cycles
│  ├─ Change management for the policy itself (meta!)
│  └─ Integration with ISMS

└─ ISMS-POL-A.8.32-S5_-_Annexes.md
   ├─ ISMS-POL-A.8.32-S5_A_-_Change_Management_Capability_Standards.md
   │  └─ Minimum capabilities required from change management systems
   │
   ├─ ISMS-POL-A.8.32-S5_B_-_Change_Request_Form_Template.md
   │  └─ Standard change request fields and template
   │
   ├─ ISMS-POL-A.8.32-S5_C_-_Risk_Assessment_Matrix.md
   │  └─ Change risk classification methodology
   │
   └─ ISMS-POL-A.8.32-S5_D_-_Quick_Reference_Guide.md
      └─ One-page summary for practitioners
```

**Document Constraints:**
- Each section: 300-400 lines maximum
- Modular structure for easy updates
- Cross-references between sections
- Date format: DD.MM.YYYY

### 3.2 Implementation Layer (5 Excel Workbooks)
```
┌────────────────────────────────────────────────────────┐
│ ISMS-IMP-A.8.32.1 - Change Process Assessment         │
├────────────────────────────────────────────────────────┤
│ Sheets:                                                │
│  1. Instructions & Legend                              │
│  2. Change Process Workflow                            │
│     - Initiation → Review → Approval → Implementation  │
│     - Roles involved at each stage                     │
│     - Timelines and SLAs                               │
│  3. Approval Authority Matrix                          │
│     - Who can approve what type of changes             │
│     - Escalation paths                                 │
│  4. Communication Procedures                           │
│     - Stakeholder notification                         │
│     - Communication templates                          │
│  5. Documentation Requirements                         │
│     - Mandatory fields in change records               │
│     - Audit trail requirements                         │
│  6. Change Management Tools                            │
│     - ITSM tool capabilities assessment                │
│     - Integration with other systems                   │
│  7. Summary Dashboard                                  │
│  8. Evidence Register                                  │
│  9. Approval Sign-Off                                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ ISMS-IMP-A.8.32.2 - Change Types & Categories         │
├────────────────────────────────────────────────────────┤
│ Sheets:                                                │
│  1. Instructions & Legend                              │
│  2. Standard Changes Catalog                           │
│     - Pre-approved, low-risk changes                   │
│     - Self-service changes                             │
│  3. Normal Changes Assessment                          │
│     - CAB-reviewed changes                             │
│     - Risk assessment requirements                     │
│  4. Emergency Changes                                  │
│     - Fast-track process                               │
│     - Post-implementation review                       │
│  5. Change Risk Classification                         │
│     - Risk matrix (Impact × Likelihood)                │
│     - Risk-based approval requirements                 │
│  6. Change Calendar Management                         │
│     - Freeze periods                                   │
│     - Blackout windows                                 │
│  7. Summary Dashboard                                  │
│  8. Evidence Register                                  │
│  9. Approval Sign-Off                                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ ISMS-IMP-A.8.32.3 - Environment Separation Assessment  │
├────────────────────────────────────────────────────────┤
│ Sheets:                                                │
│  1. Instructions & Legend                              │
│  2. Development Environment                            │
│     - Purpose, access controls, isolation              │
│  3. Test/QA Environment                                │
│     - Testing procedures, data protection              │
│  4. Production Environment                             │
│     - Protection controls, change restrictions         │
│  5. Environment Promotion Process                      │
│     - Dev → Test → Prod workflow                       │
│     - Approval gates between environments              │
│  6. Production Data in Non-Prod (8.33)                 │
│     - Data masking/anonymization                       │
│     - Protection requirements                          │
│  7. Summary Dashboard                                  │
│  8. Evidence Register                                  │
│  9. Approval Sign-Off                                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ ISMS-IMP-A.8.32.4 - Testing & Validation Assessment    │
├────────────────────────────────────────────────────────┤
│ Sheets:                                                │
│  1. Instructions & Legend                              │
│  2. Pre-Deployment Testing                             │
│     - Test plans and procedures                        │
│     - Integration with 8.29 (Security Testing)         │
│  3. Acceptance Criteria                                │
│     - Success criteria definition                      │
│     - Sign-off requirements                            │
│  4. Rollback Procedures                                │
│     - Backout plans                                    │
│     - Recovery procedures                              │
│  5. Post-Implementation Review                         │
│     - PIR process                                      │
│     - Lessons learned                                  │
│  6. Continuous Improvement                             │
│     - Failed change analysis                           │
│     - Process optimization                             │
│  7. Summary Dashboard                                  │
│  8. Evidence Register                                  │
│  9. Approval Sign-Off                                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ ISMS-IMP-A.8.32.5 - Compliance Dashboard               │
├────────────────────────────────────────────────────────┤
│ Sheets:                                                │
│  1. Instructions & Legend                              │
│  2. Overall Compliance Summary                         │
│     - Aggregated status from IMP 1-4                   │
│     - Red/Yellow/Green indicators                      │
│  3. Change Management KPIs                             │
│     - Change success rate                              │
│     - Emergency change ratio                           │
│     - Average implementation time                      │
│     - Failed change percentage                         │
│  4. Risk Exposure Dashboard                            │
│     - High-risk changes without proper review          │
│     - Unauthorized changes detected                    │
│     - Environment separation violations                │
│  5. Gap Analysis                                       │
│     - Requirements vs. actual state                    │
│     - Prioritized remediation actions                  │
│  6. Audit Readiness                                    │
│     - Evidence completeness check                      │
│     - Document currency status                         │
│  7. Executive Summary (One-Page)                       │
│  8. Evidence Register                                  │
│  9. Approval Sign-Off                                  │
└────────────────────────────────────────────────────────┘
```

### 3.3 Python Generator Scripts (5 Scripts)
```
generate_a832_1_change_process.py          (~800-1000 lines)
generate_a832_2_change_types.py            (~800-1000 lines)
generate_a832_3_environment_separation.py  (~800-1000 lines)
generate_a832_4_testing_validation.py      (~800-1000 lines)
generate_a832_5_compliance_dashboard.py    (~1000-1200 lines)
```

**Script Structure (following A.8.23 pattern):**
- Section 1: Workbook creation & styles
- Section 2: Column definitions
- Section 3: Data validations
- Section 4: Sheet creation functions
- Section 5: Assessment sheet builders
- Section 6-8: Instructions, Evidence, Approval sheets
- Section 9: Dashboard creation
- Section 10: Main execution
- Section 11: Utility functions
- Section 12: Constants and configuration

**If scripts exceed 1000 lines → split into sections:**
- `generate_a832_X_part1.py` (core logic)
- `generate_a832_X_part2.py` (extended features)

### 3.4 Sanity Check Script
```
excel_sanity_check_a832.py
```

**Functions:**
- Validate all 5 workbooks are present
- Check sheet structure consistency
- Verify dropdown validations
- Test formula integrity
- Validate evidence register structure
- Check approval sign-off workflow
- Generate compliance report

---

## 4. DETAILED ROADMAP

### Phase 1: Foundation (Week 1)

**Day 1-2: Policy Framework**
```
✓ ISMS-POL-A.8.32_-_Change_Management_Policy.md (Master Index)
✓ ISMS-POL-A.8.32-S1_-_Purpose__Scope__Definitions.md
  - Control objective and scope
  - Key definitions (change, CAB, emergency, etc.)
  - Regulatory applicability (Swiss/EU context)
  - Integration with ISO 27002:2022 requirements
```

**Day 3-4: Requirements Framework**
```
✓ ISMS-POL-A.8.32-S2_-_Requirements_-_Overview.md
✓ ISMS-POL-A.8.32-S2_1_-_Change_Process_Requirements.md
  - Planning & impact assessment (SHALL)
  - Authorization workflows (SHALL)
  - Communication requirements (SHALL)
  - Implementation controls (SHALL)
  - Documentation requirements (SHALL)
```

**Day 5: Change Classification**
```
✓ ISMS-POL-A.8.32-S2_2_-_Change_Classification_Requirements.md
  - Standard changes (pre-approved catalog)
  - Normal changes (CAB review)
  - Emergency changes (fast-track with post-review)
  - Risk-based categorization matrix
```

### Phase 2: Testing & Emergency Controls (Week 2)

**Day 6-7: Testing Requirements**
```
✓ ISMS-POL-A.8.32-S2_3_-_Testing___Validation_Requirements.md
  - Environment separation (Dev/Test/Prod)
  - Testing procedures
  - Acceptance criteria
  - Rollback requirements
  - Integration with Control 8.29 (Security Testing)
  - Integration with Control 8.33 (Production data in test)
```

**Day 8-9: Emergency Changes**
```
✓ ISMS-POL-A.8.32-S2_4_-_Emergency_Change_Requirements.md
  - Emergency triggers and criteria
  - Fast-track approval process
  - Risk acceptance procedures
  - Post-implementation review (mandatory)
  - Documentation catch-up requirements
```

### Phase 3: Governance (Week 2)

**Day 10: Roles & Responsibilities**
```
✓ ISMS-POL-A.8.32-S3_-_Roles_and_Responsibilities.md
  - Change Requester
  - Change Manager
  - Change Advisory Board (CAB)
  - Change Implementer
  - Technical Reviewer
  - Security Reviewer (CISO team)
  - Change Approver (by authority level)
  - RACI matrix for all activities
```

**Day 11: Policy Governance**
```
✓ ISMS-POL-A.8.32-S4_-_Policy_Governance.md
  - Policy lifecycle
  - Review and update process
  - Version control
  - Integration with ISMS
  - Compliance monitoring
```

### Phase 4: Annexes (Week 3)

**Day 12-13: Capability Standards & Templates**
```
✓ ISMS-POL-A.8.32-S5_-_Annexes.md (Index)
✓ ISMS-POL-A.8.32-S5_A_-_Change_Management_Capability_Standards.md
  - ITSM tool requirements
  - Workflow automation capabilities
  - Integration requirements
  - Audit trail capabilities
```
```
✓ ISMS-POL-A.8.32-S5_B_-_Change_Request_Form_Template.md
  - Standard change request fields
  - Risk assessment template
  - Approval workflow template
```

**Day 14: Risk & Reference**
```
✓ ISMS-POL-A.8.32-S5_C_-_Risk_Assessment_Matrix.md
  - Impact × Likelihood matrix
  - Risk-based approval requirements
  - Escalation criteria
```
```
✓ ISMS-POL-A.8.32-S5_D_-_Quick_Reference_Guide.md
  - One-page practitioner guide
  - Decision flowcharts
  - Quick checklists
```

### Phase 5: Implementation Specifications (Week 3-4)

**Day 15-16: IMP-1 Specification**
```
✓ ISMS-IMP-A_8_32_1_-_Change_Process_Assessment.md
  - Sheet structure (9 sheets)
  - Column definitions for each sheet
  - Validation rules
  - Compliance checklists
  - Reference tables
```

**Day 17: IMP-2 Specification**
```
✓ ISMS-IMP-A_8_32_2_-_Change_Types_Categories_Assessment.md
  - Change catalog documentation
  - Risk classification assessment
  - Calendar management
```

**Day 18: IMP-3 Specification**
```
✓ ISMS-IMP-A_8_32_3_-_Environment_Separation_Assessment.md
  - Dev/Test/Prod assessment
  - Promotion workflow documentation
  - Data protection in non-prod environments
```

**Day 19: IMP-4 Specification**
```
✓ ISMS-IMP-A_8_32_4_-_Testing_Validation_Assessment.md
  - Testing procedure documentation
  - Rollback capability assessment
  - PIR process documentation
```

**Day 20: IMP-5 Specification**
```
✓ ISMS-IMP-A_8_32_5_-_Compliance_Dashboard_Specification.md
  - Dashboard layout
  - KPI calculations
  - Gap analysis structure
  - Executive summary format
```

### Phase 6: Python Generators (Week 4-5)

**Day 21-22: Generator 1 - Change Process**
```
✓ generate_a832_1_change_process.py
  Testing:
  - Generate workbook
  - Verify sheet structure
  - Test all dropdowns
  - Validate formulas
  - Check evidence register
  - Verify approval workflow
```

**Day 23: Generator 2 - Change Types**
```
✓ generate_a832_2_change_types.py
  Testing: Same as above
```

**Day 24: Generator 3 - Environment Separation**
```
✓ generate_a832_3_environment_separation.py
  Testing: Same as above
```

**Day 25: Generator 4 - Testing & Validation**
```
✓ generate_a832_4_testing_validation.py
  Testing: Same as above
```

**Day 26-27: Generator 5 - Compliance Dashboard**
```
✓ generate_a832_5_compliance_dashboard.py
  Testing: Same as above
  Note: This is the most complex (aggregates data from IMP 1-4)
```

### Phase 7: Quality Assurance (Week 6)

**Day 28-29: Sanity Checks**
```
✓ excel_sanity_check_a832.py
  - Structural validation
  - Formula verification
  - Dropdown consistency
  - Evidence register checks
  - Approval workflow validation
```

**Day 30: Integration Testing**
```
✓ Generate all 5 workbooks
✓ Complete sample data in each
✓ Verify dashboard aggregation in IMP-5
✓ Test audit trail completeness
✓ Document known issues
```

### Phase 8: Documentation & Handover (Week 6)

**Day 31: User Documentation**
```
✓ README_A832.md
  - Quick start guide
  - How to generate workbooks
  - How to complete assessments
  - How to maintain evidence
  - FAQ section
```

**Day 32: Final Review**
```
✓ Policy completeness check
✓ IMP specification completeness
✓ Python script functionality
✓ Date format compliance (DD.MM.YYYY in docs/Excel)
✓ File naming conventions (YYYYMMDD in filenames)
✓ Code window formatting for all MD outputs
✓ Line count compliance (<400 per MD section)
```

---

## 5. KEY DELIVERABLES CHECKLIST

### 5.1 Policy Documents (13 MD Files)
```
[  ] ISMS-POL-A.8.32_-_Change_Management_Policy.md
[  ] ISMS-POL-A.8.32-S1_-_Purpose__Scope__Definitions.md
[  ] ISMS-POL-A.8.32-S2_-_Requirements_-_Overview.md
[  ] ISMS-POL-A.8.32-S2_1_-_Change_Process_Requirements.md
[  ] ISMS-POL-A.8.32-S2_2_-_Change_Classification_Requirements.md
[  ] ISMS-POL-A.8.32-S2_3_-_Testing___Validation_Requirements.md
[  ] ISMS-POL-A.8.32-S2_4_-_Emergency_Change_Requirements.md
[  ] ISMS-POL-A.8.32-S3_-_Roles_and_Responsibilities.md
[  ] ISMS-POL-A.8.32-S4_-_Policy_Governance.md
[  ] ISMS-POL-A.8.32-S5_-_Annexes.md
[  ] ISMS-POL-A.8.32-S5_A_-_Change_Management_Capability_Standards.md
[  ] ISMS-POL-A.8.32-S5_B_-_Change_Request_Form_Template.md
[  ] ISMS-POL-A.8.32-S5_C_-_Risk_Assessment_Matrix.md
[  ] ISMS-POL-A.8.32-S5_D_-_Quick_Reference_Guide.md
```

### 5.2 Implementation Specifications (5 MD Files)
```
[  ] ISMS-IMP-A_8_32_1_-_Change_Process_Assessment.md
[  ] ISMS-IMP-A_8_32_2_-_Change_Types_Categories_Assessment.md
[  ] ISMS-IMP-A_8_32_3_-_Environment_Separation_Assessment.md
[  ] ISMS-IMP-A_8_32_4_-_Testing_Validation_Assessment.md
[  ] ISMS-IMP-A_8_32_5_-_Compliance_Dashboard_Specification.md
```

### 5.3 Python Generators (5+1 Files)
```
[  ] generate_a832_1_change_process.py
[  ] generate_a832_2_change_types.py
[  ] generate_a832_3_environment_separation.py
[  ] generate_a832_4_testing_validation.py
[  ] generate_a832_5_compliance_dashboard.py
[  ] excel_sanity_check_a832.py
```

### 5.4 Generated Excel Workbooks (5 Files)
```
[  ] ISMS-IMP-A.8.32.1_Change_Process_YYYYMMDD.xlsx
[  ] ISMS-IMP-A.8.32.2_Change_Types_YYYYMMDD.xlsx
[  ] ISMS-IMP-A.8.32.3_Environment_Separation_YYYYMMDD.xlsx
[  ] ISMS-IMP-A.8.32.4_Testing_Validation_YYYYMMDD.xlsx
[  ] ISMS-IMP-A.8.32.5_Compliance_Dashboard_YYYYMMDD.xlsx
```

---

## 6. QUALITY STANDARDS

### 6.1 Document Standards

**Markdown Files:**
- [ ] Maximum 300-400 lines per section
- [ ] All MD content in code windows (```markdown blocks)
- [ ] Date format: DD.MM.YYYY
- [ ] Cross-references between documents
- [ ] Version control headers

**Python Scripts:**
- [ ] Maximum ~1000 lines (split if exceeding)
- [ ] Consistent style with A.8.23 pattern
- [ ] Section headers (SECTION 1-12)
- [ ] Comprehensive docstrings
- [ ] Error handling

**Excel Workbooks:**
- [ ] Date format: DD.MM.YYYY in all cells
- [ ] Filename format: YYYYMMDD
- [ ] Freeze panes configured
- [ ] 100 rows in Evidence Register
- [ ] 3-level Approval Sign-Off
- [ ] Consistent color scheme (003366 headers)

### 6.2 Technology Neutrality

- [ ] NO vendor/product names in policies
- [ ] NO vendor/product names in IMP specs
- [ ] Generic capability descriptions only
- [ ] Customer fills in THEIR specific tools
- [ ] Works for ANY change management system

### 6.3 Audit Trail

- [ ] Evidence Register in every workbook
- [ ] Approval Sign-Off in every workbook
- [ ] Traceability from requirements → implementation
- [ ] Gap analysis documentation
- [ ] Continuous improvement tracking

---

## 7. DEPENDENCIES & INTEGRATIONS

### 7.1 Related ISO 27002:2022 Controls
```
┌──────────────────────────────────────────────────────┐
│ Control 8.32 integrates with:                        │
│                                                      │
│ → 5.30: ICT continuity planning                     │
│    (change management affects continuity plans)     │
│                                                      │
│ → 5.37: Documented operating procedures             │
│    (documentation updates after changes)            │
│                                                      │
│ → 8.29: Security testing during development         │
│    (testing requirements before deployment)         │
│                                                      │
│ → 8.31: Separation of dev/test/production          │
│    (environment isolation for changes)              │
│                                                      │
│ → 8.33: Test information                            │
│    (production data in test environments)           │
│                                                      │
│ → 8.19: Installation of software on operational    │
│    (software deployment controls)                   │
└──────────────────────────────────────────────────────┘
```

### 7.2 ITIL 4 Alignment (Optional)

If organization uses ITIL 4:
- Map to ITIL Change Enablement practice
- Reference ITIL change models
- Integrate with ITIL service lifecycle

**Note:** ITIL is informational, not mandatory for ISO 27001.

### 7.3 Regulatory Context

**Swiss Federal Act on Data Protection (FADP):**
- Change management prevents data breaches
- Audit trail for data protection compliance

**EU GDPR (if applicable):**
- Article 32: Security of processing
- Change management as technical measure

**Industry-Specific:**
- Financial services: FINMA requirements
- Healthcare: Swiss medical device regulations
- Critical infrastructure: Specific change control requirements

---

## 8. RISK MITIGATION

### 8.1 Common Pitfalls

**Pitfall 1: "Nobody will fill out the Excel workbooks"**

*Mitigation:*
- Make workbooks intuitive with clear instructions
- Provide example rows in each sheet
- Auto-calculate compliance scores
- Executive dashboard shows value
- Integrate with existing ITSM tools (export/import)

**Pitfall 2: "Our change management is chaos"**

*Mitigation:*
- Document ACTUAL state (not ideal state)
- Gap analysis identifies improvements
- Prioritized roadmap in dashboard
- Start with high-risk changes first
- Incremental improvement approach

**Pitfall 3: "We don't have separate Dev/Test/Prod"**

*Mitigation:*
- Document current state honestly
- Assess risk exposure
- Compensating controls where separation isn't feasible
- Roadmap for environment separation
- Risk acceptance by management

**Pitfall 4: "Emergency changes are uncontrolled"**

*Mitigation:*
- Emergency change process with post-review
- Document all emergency changes in workbook
- Analyze emergency change patterns
- Identify process improvements
- Reduce emergency change ratio over time

### 8.2 Success Factors

✓ **Feynman Principle:** Keep it simple, avoid cargo cult compliance  
✓ **System Engineering:** Evidence-based, measurable, improvable  
✓ **Technology Agnostic:** Works with ANY change management tool  
✓ **Practical:** Document reality, not fiction  
✓ **Auditable:** Complete evidence trail  
✓ **Continuous:** Improvement tracking built-in  

---

## 9. TIMELINE SUMMARY
```
Week 1-2:    Policy Layer (13 MD files)
Week 3:      Annexes & IMP Specs preparation
Week 4:      IMP Specifications (5 MD files)
Week 4-5:    Python Generators (5 scripts)
Week 6:      QA, Testing, Documentation

Total: ~6 weeks for complete Control 8.32 implementation
```

**Effort Estimate:**
- Policy writing: ~60 hours
- IMP specifications: ~30 hours
- Python coding: ~80 hours
- Testing & QA: ~20 hours
- Documentation: ~10 hours

**Total: ~200 hours (~5 weeks full-time)**

---

## 10. NEXT STEPS

### Immediate Actions

1. **Confirm Approach**
   - Review roadmap with stakeholders
   - Adjust timeline if needed
   - Identify SMEs for change management

2. **Start Phase 1**
   - Begin with Master Policy (POL-A.8.32)
   - Draft S1 (Purpose, Scope, Definitions)
   - Review ISO 27002:2022 Control 8.32 in detail

3. **Prepare Development Environment**
   - Set up Python 3 with openpyxl
   - Create directory structure
   - Version control setup (Git recommended)

### Questions to Address

- [ ] Do we have existing change management procedures to reference?
- [ ] What ITSM tool(s) are currently in use?
- [ ] Do we have separate Dev/Test/Prod environments?
- [ ] What's the current change success rate?
- [ ] Are there known change management pain points?
- [ ] Who will be the Policy Owner for Control 8.32?
- [ ] Who are the key stakeholders (CAB members)?

---

## 11. HUMOR CORNER (Because Feynman Would Approve)

**Change Management Reality Check:**
```
                    THEORY vs. REALITY

Theory:
    Request → Risk Assessment → CAB Review → Testing → 
    Approval → Scheduled Deployment → PIR → Success!

Reality:
    "It's on fire!" → Emergency change → Deploy now → 
    "It's more on fire!" → Rollback → PIR: "Let's never 
    speak of this again"

Goal of Control 8.32:
    Move from Reality toward Theory (incrementally)
```

**Cargo Cult Warning:**

Don't write policies like this:
> "All changes shall be thoroughly reviewed by the Change 
> Advisory Board which meets weekly to assess risk and approve 
> changes following our comprehensive 47-step process..."

When reality is:
> "Changes happen when Bob isn't looking and we hope for the best."

**Instead:** Document how Bob actually works, assess the risk, 
and incrementally improve the process. That's real engineering.

---

## 12. DOCUMENT METADATA

**Project:** ISMS Control 8.32 - Change Management  
**Roadmap Version:** 1.0  
**Created:** 05.01.2026  
**Author:** ISMS Implementation Team  
**Status:** Planning - Ready for Phase 1  
**Next Review:** After Phase 1 completion  

**References:**
- ISO/IEC 27001:2022 Annex A.8.32
- ISO/IEC 27002:2022 Control 8.32
- ISMS Control A.8.23 (Web Filtering) - Reference Model
- ITIL 4 (Change Enablement) - Optional reference

---

**END OF ROADMAP**

*"The first principle is that you must not fool yourself — and you are 
the easiest person to fool." — Richard Feynman*

*Let's build a change management framework that actually helps people 
do their jobs better, not just check boxes for auditors.* 🎯