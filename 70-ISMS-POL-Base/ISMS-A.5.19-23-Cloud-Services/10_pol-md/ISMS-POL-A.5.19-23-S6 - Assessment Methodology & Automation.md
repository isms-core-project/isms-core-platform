# ISMS-POL-A.5.19-23-S6 — Assessment Methodology & Automation
## Cloud Services Security - Systems Engineering Approach

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Assessment Methodology & Automation |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S6 |
| **Document Creator** | Information Security Officer (ISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISO | Initial section covering Python-based assessment framework |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Technical: System Engineering Team Lead
- Quality: Quality Assurance Manager
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- All ISMS-IMP-A.5.23 implementation guidance documents
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- Python generator scripts in 50_scripts-excel/
- ISO/IEC 27001:2022 Clause 9.2 (Internal audit)

---

## 1. Executive Summary

### 1.1 Purpose

This document defines the **Systems Engineering (SE) approach** for assessing cloud service security compliance. Instead of traditional checkbox audits, we use **Python-generated Excel workbooks** that enforce:

- **Repeatable** assessments (identical structure quarterly)
- **Quantitative** compliance metrics (87.3% compliant vs. "mostly compliant")
- **Evidence-based** verification (screenshots, configs, contracts)
- **Traceable** audit trails (normalized files + manifest)
- **Transparent** dashboards (auto-calculated from assessments)

### 1.2 Critical Principle

**"If You Can't Generate It, You Can't Maintain It"**: Manual spreadsheets decay over time - formulas break, validations disappear, and inconsistencies emerge across assessment cycles. Copy-pasted templates drift as different stakeholders modify local versions without version control. Assessment tools must be generated programmatically to ensure consistency, repeatability, and systematic updates when requirements change. This policy uses Python generators to create Excel assessment workbooks, enabling rapid deployment, controlled modifications, and evidence-based compliance measurement with full audit trails.

**Systems Engineering Approach:**
```
1. Run Python generator → ISMS_REG_A523_1_Inventory.xlsx
2. Procurement completes service list with evidence
3. Normalize and validate completed files
4. Dashboard auto-calculates: "45/78 services compliant (57.7%)"
5. Gap report identifies: "33 services missing MFA"
```

**Result:** Objective, quantitative assessment of actual compliance state, not subjective self-assessment.

---

## 2. Framework Architecture

### 2.1 Five-Layer Design

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: POLICY LAYER                                       │
│ • ISMS-POL-A.5.19-23 (Master Index)                         │
│ • ISMS-POL-A.5.19-23-S5 (Cloud Services Requirements)       │
│ • ISMS-POL-A.5.19-23-S6 (This document - Methodology)       │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: ASSESSMENT SPECIFICATIONS (Markdown)               │
│ • ISMS-IMP-A.5.23.1.md - Inventory & Classification         │
│ • ISMS-IMP-A.5.23.2.md - Vendor Due Diligence               │
│ • ISMS-IMP-A.5.23.3.md - Secure Configuration               │
│ • ISMS-IMP-A.5.23.4.md - Ongoing Governance                 │
│ • ISMS-IMP-A.5.23.5.md - Compliance Dashboard               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: IMPLEMENTATION (Python Scripts)                    │
│ • generate_reg_a523_1_inventory.py                          │
│ • generate_reg_a523_2_vendor_dd.py                          │
│ • generate_reg_a523_3_secure_config.py                      │
│ • generate_reg_a523_4_governance.py                         │
│ • generate_reg_a523_5_compliance_dashboard.py               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 4: VALIDATION (Quality Assurance)                     │
│ • normalize_assessment_files_a523.py (audit trail creator)  │
│ • consolidate_reg_a523_dashboard.py (dashboard aggregation) │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 5: INTEGRATION (Executive Dashboard)                  │
│ • Auto-aggregated compliance metrics                        │
│ • Risk heatmap (vendor lock-in, data sovereignty)           │
│ • Gap analysis with remediation roadmap                     │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Assessment Workbook Structure

Each workbook follows this proven pattern:

| Sheet | Purpose | Filled By | Review Cycle |
|-------|---------|-----------|--------------|
| **Instructions & Legend** | How to use + status codes | Auto-generated | N/A |
| **Assessment Sheets (2-6)** | Domain-specific checklists | Stakeholders | Quarterly |
| **Summary Dashboard** | Compliance % per domain | Formula-driven | Auto |
| **Evidence Register** | Links to proof documents | Stakeholders | Quarterly |
| **Approval Sign-Off** | CISO approval + review dates | Management | Quarterly |

---

## 3. Assessment Workbooks Specification

### 3.1 Workbook 1: Cloud Service Inventory & Classification

**Document ID:** ISMS-IMP-A.5.23.1  
**Filename:** `ISMS_REG_A523_1_Inventory_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_1_inventory.py`  
**Stakeholder:** IT Operations, Procurement, Finance  
**Sheet Count:** 10 sheets

**Purpose:** Maintain authoritative inventory of all cloud services with criticality classification.

**Sheet Structure:**
1. Instructions & Legend
2. SaaS Services (Office 365, Salesforce, Zoom, etc.)
3. IaaS/PaaS Services (AWS, Azure, GCP, etc.)
4. Cloud Security Services (CrowdStrike, Zscaler, etc.)
5. Cloud Storage Services (Dropbox, Box, etc.)
6. Data Classification Mapping
7. Service Criticality Assessment
8. Summary Dashboard
9. Evidence Register
10. Approval Sign-Off

**Base Columns (17 standard A-Q):**
- A: Cloud Service Name
- B: Service Type (SaaS/IaaS/PaaS/Security/Storage)
- C: Vendor Name
- D: Service Criticality (Critical/High/Medium/Low)
- E: Data Classification (Restricted/Confidential/Internal/Public)
- F: Data Residency Region (Switzerland/EU/USA/Global)
- G: Contract Status (Active/Renewal Due/Expired)
- H: Status (✅ Compliant / ⚠️ Partial / ❌ Non-Compliant)
- I: Evidence Location
- J: Gap Description
- K: Remediation Needed (Yes/No)
- L: Exception ID
- M: Risk ID
- N: Compensating Controls
- O: Service Owner
- P: Target Remediation Date
- Q: Budget Impact (High/Medium/Low/None)

**Extended Columns (R-X for inventory-specific):**
- R: Monthly Cost (formula: validates numeric)
- S: Annual Contract Value
- T: Number of Licensed Users
- U: Integration Count (# of connected systems)
- V: Backup Service Available (Yes/No)
- W: Exit Feasibility (Easy/Medium/Hard/Unknown)
- X: Last Inventory Review Date

### 3.2 Workbook 2: Vendor Due Diligence & Contracts

**Document ID:** ISMS-IMP-A.5.23.2  
**Filename:** `ISMS_REG_A523_2_DueDiligence_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_2_vendor_dd.py`  
**Stakeholder:** Legal, Procurement, Compliance, ISO  
**Sheet Count:** 10 sheets

**Purpose:** Track vendor security certifications, contract terms, SLAs, and audit rights.

**Sheets:**
1. Instructions & Legend
2. Vendor Security Certifications
3. Contract Terms Analysis
4. SLA Requirements & Performance
5. Data Sovereignty Compliance
6. Forensics & Incident Support
7. Right to Audit & Penetration Testing
8. Summary Dashboard
9. Evidence Register
10. Approval Sign-Off

**Extended Columns (R-X):**
- R: ISO 27001 Certified (Yes/No/Unknown + Cert #)
- S: SOC 2 Type II Report Available (Yes/No/Unknown)
- T: Contract Renewal Date
- U: SLA Availability % (99.9%, 99.95%, etc.)
- V: Right to Audit Clause (Yes/No)
- W: Data Portability Clause (Yes/No)
- X: Forensics/IR Support (Yes/No/Limited)

### 3.3 Workbook 3: Secure Configuration & Deployment

**Document ID:** ISMS-IMP-A.5.23.3  
**Filename:** `ISMS_REG_A523_3_Configuration_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_3_secure_config.py`  
**Stakeholder:** IT Security, DevOps, System Administrators  
**Sheet Count:** 11 sheets

**Purpose:** Assess security configuration baseline compliance for deployed cloud services.

**Sheets:**
1. Instructions & Legend
2. Identity & Access Management
3. Data Encryption (At Rest & In Transit)
4. Network Security & Segmentation
5. Logging & Monitoring Configuration
6. Backup & Disaster Recovery
7. Data Classification Labeling
8. API Security & Integration
9. Summary Dashboard
10. Evidence Register
11. Approval Sign-Off

**Extended Columns (R-X):**
- R: MFA Enabled (Yes/No/Partial)
- S: Encryption at Rest (Yes/No/Unknown)
- T: Encryption in Transit (TLS 1.3/TLS 1.2/Weak)
- U: Centralized Logging (Yes/No/Partial)
- V: SSO Integration (Yes/No/Planned)
- W: Data Classification Labels Applied (Yes/No/Partial)
- X: Configuration Baseline Documented (Yes/No)

### 3.4 Workbook 4: Ongoing Governance & Risk Management

**Document ID:** ISMS-IMP-A.5.23.4  
**Filename:** `ISMS_REG_A523_4_Governance_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_4_governance.py`  
**Stakeholder:** IT Management, Risk Management, ISO  
**Sheet Count:** 11 sheets

**Purpose:** Monitor ongoing governance, vendor risk, business continuity, and change management.

**Sheets:**
1. Instructions & Legend
2. Security Awareness & Training
3. Incident Response Procedures
4. Security Update Management
5. Vendor Lock-in Assessment
6. Vendor Lock-out Evaluation
7. Business Continuity Planning
8. Change Management Tracking
9. Summary Dashboard
10. Evidence Register
11. Approval Sign-Off

**Extended Columns (R-X):**
- R: Security Training Completed (Yes/No + Date)
- S: Last Security Review Date
- T: Incident Response Plan Tested (Yes/No/Planned)
- U: Vendor Lock-in Risk (High/Medium/Low)
- V: BC/DR Plan Exists (Yes/No)
- W: BC/DR Last Test Date
- X: Change Management Process (Yes/No)

### 3.5 Workbook 5: Compliance Monitoring & Exit Planning

**Document ID:** ISMS-IMP-A.5.23.5  
**Filename:** `ISMS_REG_A523_5_Dashboard_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_5_compliance_dashboard.py`  
**Stakeholder:** Compliance, Legal, IT Operations  
**Sheet Count:** 9 sheets (Dashboard-focused)

**Purpose:** Aggregate compliance metrics, SLA performance, and exit readiness from all workbooks.

**Sheets:**
1. Instructions & Legend
2. Compliance Summary (pulls from Workbooks 1-4)
3. SLA Performance Tracking
4. Security Incident Log
5. Exit Strategy & Data Migration
6. Risk Heatmap (Lock-in/Sovereignty/Availability)
7. Gap Analysis Report
8. Evidence Register
9. Approval Sign-Off

**Dashboard Formulas:**
- Pulls data from `ISMS_REG_A523_1` through `ISMS_REG_A523_4`
- Auto-calculates compliance % per domain
- Generates risk scores based on criteria
- Produces remediation priority matrix

---

## 4. Python Generator Architecture

### 4.1 Script Structure (Standard Pattern)

All generator scripts follow this modular architecture:

```python
# ============================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================
def create_workbook() -> Workbook:
    """Create all sheets matching specification."""
    
def setup_styles() -> dict:
    """Define colors, fonts, borders (NEW objects per cell!)."""

# ============================================================================
# SECTION 2: COLUMN DEFINITIONS (BASE + EXTENDED)
# ============================================================================
def get_base_cloud_columns() -> dict:
    """Returns 17 standard columns (A-Q) for ALL cloud assessments."""
    
def get_extended_columns_inventory() -> dict:
    """Returns domain-specific columns R-X for inventory."""

# ============================================================================
# SECTION 3: VALIDATION DEFINITIONS
# ============================================================================
def create_base_validations(ws) -> dict:
    """Create dropdown validations for standard fields."""
    
def create_extended_validations(ws, sheet_type) -> dict:
    """Create domain-specific dropdowns."""

# ============================================================================
# SECTION 4: CHECKLIST ITEM DEFINITIONS
# ============================================================================
def get_checklist_items(sheet_type) -> list:
    """Return domain-specific compliance checklist."""

# ============================================================================
# SECTION 5: REFERENCE TABLE DEFINITIONS
# ============================================================================
def get_reference_tables(sheet_type) -> dict:
    """Return lookup tables (vendors, regions, standards)."""

# ============================================================================
# SECTION 6: GENERIC ASSESSMENT SHEET BUILDER
# ============================================================================
def create_assessment_sheet(ws, styles, section_title, policy_ref, 
                           question, sheet_type):
    """Universal builder - ONE function creates ALL assessment sheets."""

# ============================================================================
# SECTION 7: SPECIALIZED SHEET CREATORS
# ============================================================================
def create_instructions_sheet(ws, styles):
def create_summary_dashboard(ws, styles):
def create_evidence_register(ws, styles):
def create_approval_signoff(ws, styles):

# ============================================================================
# SECTION 8: DOMAIN-SPECIFIC ASSESSMENT SHEETS
# ============================================================================
def create_1_saas_services(ws, styles):
def create_2_iaas_paas_services(ws, styles):
# ... etc

# ============================================================================
# SECTION 9: MAIN EXECUTION
# ============================================================================
def main():
    """Orchestrate workbook generation."""
```

### 4.2 Critical Implementation Notes

**Style Object Best Practice:**
```python
# ❌ AVOID - Shared objects can cause Excel compatibility issues
border = Border(left=Side(style="thin"), ...)
cell1.border = border  # Reference 1
cell2.border = border  # Reference 2

# ✅ RECOMMENDED - New object per cell ensures compatibility
def apply_border(cell):
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )
```

**Implementation rationale:** Creating fresh style objects for each cell prevents potential Excel compatibility warnings and ensures clean workbook generation.

---

## 5. Validation & Integration

### 5.1 Processing Scripts

| Script | Purpose | When to Run |
|--------|---------|-------------|
| **normalize_assessment_files_a523.py** | Standardizes filenames and creates audit trail manifest | After stakeholder completion |
| **consolidate_reg_a523_dashboard.py** | Aggregates data from assessment workbooks into unified dashboard | After normalization, before executive review |

### 5.2 Processing Workflow

```
┌────────────────────────────────────────────────────────────┐
│ 1. Generate Workbook                                        │
│    $ python3 generate_reg_a523_1_inventory.py               │
│    Output: ISMS_REG_A523_1_Inventory_20260115.xlsx          │
└────────────────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────┐
│ 2. Distribute to Stakeholders                               │
│    - Email to IT Ops, Procurement, Legal                    │
│    - Deadline: 2 weeks for completion                       │
└────────────────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────┐
│ 3. Normalize Completed Files                                │
│    $ python3 normalize_assessment_files_a523.py             │
│    Creates: assessment_manifest_20260129.json               │
└────────────────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────┐
│ 4. Consolidate Dashboard                                    │
│    $ python3 consolidate_reg_a523_dashboard.py              │
│    Aggregates all assessment data into dashboard            │
└────────────────────────────────────────────────────────────┘
```

---

## 6. Dashboard Integration

### 6.1 Formula-Driven Aggregation

The Compliance Dashboard (Workbook 5) uses Excel formulas to pull data from Workbooks 1-4:

```excel
# Example: Count compliant services from Inventory workbook
=COUNTIF('[ISMS_REG_A523_1_Inventory_20260115.xlsx]2. SaaS Services'!$H$8:$H$50,"✅*")

# Example: Calculate compliance percentage
=IF((B4-F4)=0,"0%",ROUND(C4/(B4-F4)*100,1)&"%")
```

**Benefits:**
- **No manual updates** - change assessment → dashboard refreshes
- **Real-time metrics** - stakeholders see live compliance %
- **Audit trail** - formulas show exactly where data comes from

### 6.2 Dashboard Visualizations

**Compliance Summary Table:**
| Assessment Area | Total | Compliant | Partial | Non-Compliant | N/A | Compliance % |
|-----------------|-------|-----------|---------|---------------|-----|--------------|
| Inventory       | 78    | 45        | 18      | 15            | 0   | 57.7%        |
| Vendor DD       | 78    | 62        | 10      | 6             | 0   | 79.5%        |
| Configuration   | 156   | 98        | 35      | 23            | 0   | 63.2%        |
| Governance      | 78    | 51        | 20      | 7             | 0   | 65.4%        |
| **TOTAL**       | **390** | **256** | **83** | **51**      | **0** | **65.6%** |

**Risk Heatmap:**
- High vendor lock-in + Low exit feasibility = 🔴 Critical risk
- Restricted data + Non-EU residency = 🔴 Sovereignty violation
- Critical service + No BC/DR test = 🟡 High risk

---

## 7. Assessment Cycle & Workflow

### 7.1 Quarterly Assessment Cycle

```
Week 1: GENERATION
├─ Security Engineering runs Python generators
├─ Quality review of generated workbooks
└─ Distribute to stakeholders with instructions

Weeks 2-3: ASSESSMENT
├─ IT Ops completes inventory & configuration
├─ Procurement updates vendor & contract data
├─ Legal reviews compliance & exit clauses
└─ Evidence collected (contracts, certs, screenshots)

Week 4: REVIEW
├─ ISO reviews completed assessments
├─ Gap analysis performed
├─ Remediation priorities assigned
└─ CISO approval obtained

Week 5: INTEGRATION
├─ Normalize files (audit trail created)
├─ Consolidate dashboard data
├─ Executive summary generated
└─ Board reporting package prepared
```

### 7.2 Ad-Hoc Assessment Triggers

Run assessments outside quarterly cycle when:
- **New cloud service onboarding** (use Workbook 1 + 2)
- **Major configuration changes** (use Workbook 3)
- **Security incidents** (use Workbook 4 + 5)
- **Contract renewals** (use Workbook 2)
- **Audit preparation** (use all 5 workbooks)

---

## 8. Stakeholder Guide

### 8.1 Who Fills What

| Workbook | Primary | Secondary | Tertiary |
|----------|---------|-----------|----------|
| 1. Inventory | IT Operations | Procurement | Finance |
| 2. Vendor DD | Procurement | Legal | Compliance |
| 3. Configuration | IT Security | DevOps | Sys Admins |
| 4. Governance | Risk Mgmt | ISO | IT Mgmt |
| 5. Dashboard | ISO | (Auto-generated) | CISO |

### 8.2 Completion Instructions

**For Each Assessment Sheet:**
1. Fill **yellow cells** with your data
2. Use **dropdown menus** (don't type freeform)
3. Provide **evidence location** (file path, link, doc ID)
4. If Status = Partial/Non-Compliant:
   - Complete **Gap Description**
   - Fill **Remediation Needed** = Yes
   - Assign **Responsible Person**
   - Set **Target Date**
5. Update **Evidence Register** with supporting docs

**Evidence Requirements:**
- ✅ Contract PDFs (vendor agreements, SLAs)
- ✅ Security certifications (ISO 27001, SOC 2 reports)
- ✅ Configuration screenshots (MFA settings, encryption)
- ✅ Audit reports (penetration tests, vulnerability scans)
- ✅ Training records (security awareness completion)
- ✅ BC/DR test results (last recovery drill report)
- ❌ "We have a process" (not acceptable without proof!)

---

## 9. Continuous Improvement

### 9.1 Framework Enhancement Process

**Improvement triggers:**
- Audit findings
- Stakeholder feedback
- New cloud service types
- Regulatory changes
- Technology evolution

**Process:**
1. Document issue in GitHub/Jira
2. Update markdown specification
3. Regenerate Python script
4. Test generated workbooks
5. Update this S6 document
6. Communicate changes to stakeholders

### 9.2 Quality Metrics

**Framework health indicators:**
- ✅ <2 hours generation time (all 5 workbooks)
- ✅ >80% stakeholder completion rate (within 2 weeks)
- ✅ <5% error rate in completed assessments
- ✅ Zero critical findings in audit reviews
- ✅ Quarterly framework updates completed on schedule

---

## 10. Reference Information

### 10.1 Related Documents

**Policy Layer:**
- ISMS-POL-A.5.19-23 (Master Index)
- ISMS-POL-A.5.19-23-S5 (Cloud Services Security Requirements)

**Assessment Specifications:**
- ISMS-IMP-A.5.23.1 - Inventory & Classification Spec
- ISMS-IMP-A.5.23.2 - Vendor Due Diligence Spec
- ISMS-IMP-A.5.23.3 - Secure Configuration Spec
- ISMS-IMP-A.5.23.4 - Ongoing Governance Spec
- ISMS-IMP-A.5.23.5 - Compliance Dashboard Spec

**Generator Scripts:**
- generate_reg_a523_1_inventory.py
- generate_reg_a523_2_vendor_dd.py
- generate_reg_a523_3_secure_config.py
- generate_reg_a523_4_governance.py
- generate_reg_a523_5_compliance_dashboard.py

**Processing Scripts:**
- normalize_assessment_files_a523.py
- consolidate_reg_a523_dashboard.py

### 10.2 External Standards

- ISO/IEC 27001:2022 - Control A.5.23
- ISO/IEC 27002:2022 - Cloud security guidance
- ISO/IEC 27017:2015 - Cloud-specific controls
- ISO/IEC 27018:2019 - PII in public clouds
- NIST SP 800-144 - Guidelines on Security and Privacy in Public Cloud
- CSA Cloud Controls Matrix (CCM) v4

---

## Appendix A: Quick Reference

### Script Execution Cheat Sheet

```bash
# Generate all assessment workbooks
python3 generate_reg_a523_1_inventory.py
python3 generate_reg_a523_2_vendor_dd.py
python3 generate_reg_a523_3_secure_config.py
python3 generate_reg_a523_4_governance.py
python3 generate_reg_a523_5_compliance_dashboard.py

# After stakeholder completion
python3 normalize_assessment_files_a523.py

# Consolidate dashboard
python3 consolidate_reg_a523_dashboard.py
```

---

**END OF DOCUMENT**

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
*— Richard Feynman*

**Translation for ISMS:** Evidence-based compliance prevents cloud washing! ☁️🔍