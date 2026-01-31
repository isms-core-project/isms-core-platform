# ISMS CONTROL 8.28 - SECURE CODING
## Implementation Roadmap & Project Plan
### System Engineering Approach

**Project ID:** ISMS-A.8.28-IMPL  
**Control:** ISO/IEC 27001:2022 Annex A.8.28 (Secure Coding)  
**Reference Pattern:** ISMS Control 8.23 (Web Filtering) - Proven SE Approach  
**Prepared:** 05.01.2026  
**Status:** Planning Phase

---

## 1. EXECUTIVE SUMMARY

### 1.1 Control Overview

**ISO/IEC 27002:2022 Control A.8.28: Secure Coding**

> *Principles for secure coding should be applied in software development.*

**Purpose:** Ensure software is written securely to reduce potential security 
vulnerabilities throughout the software development lifecycle.

**Key Aspects:**
- Pre-development planning and governance
- Secure coding practices during development
- Code review and testing procedures
- Third-party and open-source component management
- Continuous improvement through threat monitoring

### 1.2 Implementation Approach

Following the **proven three-layer architecture** from Control 8.23:
```
Layer 1: POLICY (POL)
â†' Modular Markdown documents defining WHAT must be done
â†' Vendor-agnostic requirements
â†' Auditor-friendly structure

Layer 2: IMPLEMENTATION (IMP)
â†' Combined MD specs + Python-generated Excel workbooks
â†' Stakeholder-specific assessment tools
â†' Evidence collection frameworks

Layer 3: AUTOMATION (Scripts)
â†' Python generators for Excel workbooks
â†' Sanity check utilities
â†' Data aggregation capabilities
```

### 1.3 Key Success Factors

✅ **No Vendor Lock-In:** All policies and assessments are tool-agnostic  
✅ **Maintainability:** Documents capped at 300-400 lines  
✅ **Dual Perspective:** Implementer pragmatism + Auditor evidence requirements  
✅ **Real-World Focus:** Practical assessment tools, not theoretical frameworks  
✅ **Aggregation Ready:** Main workbook consolidates all assessment data

---

## 2. CONTROL 8.28 DOMAIN ANALYSIS

### 2.1 Core Requirements (from ISO 27002:2022)

**A. Planning and Pre-Coding:**
1. Organization-specific secure coding principles
2. Common coding practices and historical vulnerability patterns
3. Development tool configuration (IDEs)
4. Vendor guideline compliance
5. Current development tool maintenance
6. Developer qualification in secure coding
7. Secure design and architecture (threat modeling)
8. Secure programming standards
9. Controlled development environments

**B. During Coding:**
1. Language-specific secure coding practices
2. Secure programming techniques (pair programming, peer review, refactoring)
3. Structured programming techniques
4. Code documentation and error elimination
5. Prohibition of insecure patterns (hardcoded credentials, etc.)

**C. Governance & Continuous Improvement:**
1. Organization-wide secure coding governance
2. Minimum security baseline establishment
3. Extension to third-party and open-source components
4. Real threat and vulnerability monitoring
5. Continuous improvement processes

### 2.2 Stakeholder Mapping

| Stakeholder Group | Primary Interest | Assessment Tool Needed |
|-------------------|------------------|------------------------|
| **Development Teams** | Coding standards, tooling, training | SDLC & Standards Assessment |
| **Security Champions** | Code review, vulnerability mgmt | Code Review Assessment |
| **Architecture Review Board** | Design patterns, threat modeling | SDLC Assessment |
| **DevOps/Platform Teams** | Tool integration, automation | Tools & Testing Assessment |
| **Third-Party Vendors** | Supplier requirements | Third-Party Assessment |
| **CISO/Security Leadership** | Compliance dashboard, metrics | Compliance Dashboard |
| **Auditors** | Evidence, traceability | All assessments + Evidence Register |

### 2.3 Assessment Domain Breakdown

Following 8.23's 5-domain model:

| Domain | Focus Area | Primary Output |
|--------|-----------|----------------|
| **Domain 1** | Secure Development Lifecycle (SDLC) | SDLC maturity assessment |
| **Domain 2** | Coding Standards & Development Tools | Standards compliance assessment |
| **Domain 3** | Code Review & Security Testing | Review/test coverage assessment |
| **Domain 4** | Third-Party & Open Source Management | Component risk assessment |
| **Domain 5** | Compliance Dashboard & Metrics | Executive summary & KPIs |

---

## 3. LAYER 1 - POLICY DOCUMENTS (POL)

### 3.1 Document Structure
```
ISMS-POL-A.8.28/
â"œâ"€â"€ ISMS-POL-A.8.28_-_Secure_Coding_Policy.md           [Master - 300-400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S1_-_Purpose_Scope_Definitions.md   [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S2_-_Requirements_Overview.md        [~300 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S2_1_-_Pre_Development_Requirements.md [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S2_2_-_Secure_Coding_Standards.md    [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S2_3_-_Code_Review_Testing_Requirements.md [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S2_4_-_Third_Party_OSS_Management.md [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S3_-_Roles_Responsibilities.md       [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S4_-_Policy_Governance.md            [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S5_-_Annexes.md                       [~300 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S5_A_-_Language_Specific_Guidelines.md [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S5_B_-_Code_Review_Checklist_Template.md [~400 lines]
â"œâ"€â"€ ISMS-POL-A.8.28-S5_C_-_Vulnerability_Response_Procedures.md [~400 lines]
â""â"€â"€ ISMS-POL-A.8.28-S5_D_-_Quick_Reference_Guide.md      [~300 lines]
```

**Total:** 14 documents (~5,000 lines total, ~350 lines average)

### 3.2 Policy Content Outline

#### 3.2.1 Master Policy (ISMS-POL-A.8.28)
- Executive summary
- Control objective and scope
- High-level requirements summary
- Document structure navigation
- Approval and review cycle
- Cross-references to sections

#### 3.2.2 S1 - Purpose, Scope, Definitions
**Content:**
- Policy objective and ISO 27001:2022 alignment
- Risk management context for secure coding
- Scope (in-scope/out-of-scope)
  - Development types (internal, outsourced, acquired)
  - Development phases (design, coding, testing)
  - Programming languages and frameworks
  - Application types (web, mobile, desktop, embedded)
- Key definitions
  - Secure coding terminology
  - SDLC terminology
  - Testing and review terminology
  - Compliance terminology

#### 3.2.3 S2 - Requirements Overview
**Content:**
- Requirements framework structure
- Requirement categorization
- Applicability matrix by development type
- Compliance expectations overview

#### 3.2.4 S2.1 - Pre-Development Requirements
**Content:**
- Threat modeling requirements
- Secure design principles
- Security requirements specification
- Development environment security
- Tool configuration standards
- Developer training and qualification
- Secure architecture review gates

#### 3.2.5 S2.2 - Secure Coding Standards
**Content:**
- General secure coding principles (OWASP, CWE references)
- Input validation requirements
- Output encoding requirements
- Authentication and session management
- Access control implementation
- Cryptographic requirements
- Error handling and logging
- Secure configuration management
- Language-specific standards (reference to S5.A)

#### 3.2.6 S2.3 - Code Review & Testing Requirements
**Content:**
- Peer code review requirements
- Static Application Security Testing (SAST) requirements
- Dynamic Application Security Testing (DAST) requirements
- Software Composition Analysis (SCA) requirements
- Penetration testing requirements
- Security regression testing
- Vulnerability remediation SLAs
- Testing evidence requirements

#### 3.2.7 S2.4 - Third-Party & Open Source Management
**Content:**
- Third-party component approval process
- Open source license compliance
- Vulnerability scanning for dependencies
- Component inventory maintenance
- Supply chain security requirements
- Vendor security assessment (for outsourced development)
- Contractual security requirements

#### 3.2.8 S3 - Roles and Responsibilities
**Content:**
- CISO / Security Leadership
- Application Security Team
- Development Team Lead
- Individual Developers
- Security Champions
- Code Reviewers
- Quality Assurance Team
- DevOps / Platform Team
- Architecture Review Board
- RACI matrix for key activities

#### 3.2.9 S4 - Policy Governance
**Content:**
- Policy ownership and approval
- Review and update cycle
- Exception management process
- Compliance monitoring
- Metrics and reporting
- Policy violation consequences
- Continuous improvement process

#### 3.2.10 S5 - Annexes Overview
**Content:**
- Purpose of annexes
- How to use annexes
- Navigation to specific annexes
- Update cycle for annexes

#### 3.2.11 S5.A - Language-Specific Guidelines
**Content:**
- Guidelines for common languages:
  - Java / Kotlin
  - C# / .NET
  - Python
  - JavaScript / TypeScript / Node.js
  - C / C++
  - Go
  - Ruby
  - PHP
  - Swift / Objective-C
- Language-specific vulnerability patterns
- Recommended secure libraries/frameworks per language

#### 3.2.12 S5.B - Code Review Checklist Template
**Content:**
- Pre-review checklist
- Security-focused review checklist
- Common vulnerability patterns to check
- Review outcome categories
- Review documentation template
- Escalation procedures

#### 3.2.13 S5.C - Vulnerability Response Procedures
**Content:**
- Vulnerability discovery process
- Severity classification (CVSS-based)
- Remediation SLAs by severity
- Remediation verification process
- Communication procedures
- Post-remediation analysis
- Integration with incident management

#### 3.2.14 S5.D - Quick Reference Guide
**Content:**
- One-page overview for developers
- Top 10 secure coding rules
- Common vulnerability cheat sheet
- Quick links to resources
- Contact information for security team
- Tool access instructions

---

## 4. LAYER 2 - IMPLEMENTATION SPECIFICATIONS (IMP)

### 4.1 Document Structure
```
ISMS-IMP-A.8.28/
â"œâ"€â"€ ISMS-IMP-A_8_28_1_-_SDLC_Assessment.md                [MD Spec ~400 lines]
â"œâ"€â"€ ISMS-IMP-A_8_28_2_-_Standards_Tools_Assessment.md     [MD Spec ~400 lines]
â"œâ"€â"€ ISMS-IMP-A_8_28_3_-_Code_Review_Testing_Assessment.md [MD Spec ~400 lines]
â"œâ"€â"€ ISMS-IMP-A_8_28_4_-_Third_Party_OSS_Assessment.md     [MD Spec ~400 lines]
â""â"€â"€ ISMS-IMP-A_8_28_5_-_Compliance_Dashboard_Specification.md [MD Spec ~400 lines]
```

**Total:** 5 Markdown specifications (~2,000 lines total)

### 4.2 Implementation Document Content

Each IMP document follows this structure:
```markdown
# ISMS-IMP-A.8.28.X - [Assessment Name]
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

## Document Overview
- Document ID, Assessment Area, Related Policy
- Purpose statement
- Key principle (vendor-agnostic approach)

## Workbook Structure
### Sheet 1: Instructions & Legend
- Header section design
- Document information block
- How to use this workbook (9 steps)
- Status legend
- Acceptable evidence examples

### Sheet 2-6: Assessment Sheets
- Sheet-specific header and policy reference
- Column structure (17 base columns A-Q)
- Extended columns as needed (R-X)
- Data entry rows (8-20 with yellow highlighting)
- Compliance checklist (15-20 items with status dropdowns)
- Reference tables (2-3 per sheet)
- Exception/deviation management block

### Sheet 7: Summary Dashboard
- Compliance summary table
- Critical gaps section
- KPI sections (4-6 domain-specific metrics)
- Overall security score

### Sheet 8: Evidence Register
- 100 rows for evidence tracking
- Standard evidence columns

### Sheet 9: Approval Sign-Off
- Three-level approval workflow
- Signature blocks
- Date tracking

## Column Definitions
- Base columns (A-Q): Standard across all sheets
- Extended columns (R-X): Sheet-specific

## Data Validation
- Dropdown options for each validated field
- Validation rules

## Cell Styling Reference
- Header styles
- Input cell styles
- Status color fills
- Border specifications

## Freeze Panes Configuration
- Assessment sheets: A7
- Dashboard: A4
- Evidence: A5
- Approval: A3

## Sheet-by-Sheet Detailed Specification
[Detailed specification for each sheet including:
 - Exact headers and titles
 - Policy requirement references
 - Assessment questions
 - Checklist items (15-20 per sheet)
 - Reference table content (2-3 per sheet)
 - Exception management fields]
```

### 4.3 Assessment Domain Details

#### 4.3.1 IMP-1: SDLC Assessment
**Excel Filename:** `ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx`

**Assessment Sheets (2-6):**
1. **Development Lifecycle Phases**
   - Requirements gathering security integration
   - Design phase security activities
   - Implementation phase controls
   - Testing phase security verification
   - Deployment security checks
   
2. **Threat Modeling & Risk Assessment**
   - Threat modeling process maturity
   - Risk assessment integration
   - Security architecture review
   - Attack surface analysis
   - Security requirements traceability

3. **Development Environment Security**
   - Development environment segregation
   - Access controls
   - Tool security configuration
   - Build pipeline security
   - Secret management

4. **Training & Competency**
   - Secure coding training programs
   - Developer security awareness
   - Security champion program
   - Training effectiveness metrics
   - Competency assessment

5. **SDLC Documentation & Governance**
   - SDLC policy documentation
   - Process maturity assessment
   - Governance structure
   - Metrics and KPIs
   - Continuous improvement

#### 4.3.2 IMP-2: Standards & Tools Assessment
**Excel Filename:** `ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx`

**Assessment Sheets (2-6):**
1. **Coding Standards Documentation**
   - Language-specific standards
   - Framework security guidelines
   - Coding style guides
   - Security pattern libraries
   - Anti-pattern documentation

2. **Development Tools & IDE Configuration**
   - IDE security plugins
   - Linter configurations
   - Code quality tools
   - Security analysis tools
   - Tool update management

3. **Version Control & Configuration Management**
   - Source code repository security
   - Branch protection rules
   - Commit signing
   - Code review integration
   - Configuration as code

4. **Build & CI/CD Pipeline Security**
   - Build automation security
   - Pipeline security controls
   - Artifact integrity verification
   - Deployment automation
   - Pipeline security testing

5. **Documentation & Knowledge Management**
   - Security documentation availability
   - Knowledge base maintenance
   - Developer onboarding materials
   - Lessons learned database
   - Documentation accessibility

#### 4.3.3 IMP-3: Code Review & Testing Assessment
**Excel Filename:** `ISMS-IMP-A.8.28.3_Code_Review_Testing_Assessment_YYYYMMDD.xlsx`

**Assessment Sheets (2-6):**
1. **Peer Code Review Process**
   - Review workflow and tools
   - Review criteria and checklists
   - Security-focused review
   - Review coverage metrics
   - Review documentation

2. **Static Analysis (SAST)**
   - SAST tool deployment
   - Scan frequency and coverage
   - Rule configuration
   - False positive management
   - Remediation tracking

3. **Dynamic Analysis (DAST)**
   - DAST tool deployment
   - Test environment setup
   - Scan scheduling
   - Vulnerability validation
   - Remediation verification

4. **Penetration Testing**
   - Pentesting frequency
   - Scope definition
   - Internal vs external testing
   - Finding remediation
   - Retest verification

5. **Security Testing Metrics**
   - Test coverage metrics
   - Vulnerability trending
   - Remediation SLA compliance
   - False positive rates
   - Tool effectiveness

#### 4.3.4 IMP-4: Third-Party & OSS Assessment
**Excel Filename:** `ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_YYYYMMDD.xlsx`

**Assessment Sheets (2-6):**
1. **Component Inventory Management**
   - SBOM (Software Bill of Materials) generation
   - Component tracking tools
   - Inventory completeness
   - Update tracking
   - License tracking

2. **Vulnerability Scanning (SCA)**
   - SCA tool deployment
   - Scan frequency
   - Vulnerability database updates
   - Critical vulnerability alerting
   - Remediation prioritization

3. **License Compliance**
   - License inventory
   - License compatibility checking
   - Compliance verification
   - Legal review integration
   - Violation remediation

4. **Vendor Security Assessment**
   - Vendor selection criteria
   - Security questionnaires
   - Vendor security reviews
   - Contract security clauses
   - Ongoing vendor monitoring

5. **Supply Chain Security**
   - Source verification
   - Package integrity checking
   - Private repository security
   - Dependency pinning
   - Supply chain attack mitigation

#### 4.3.5 IMP-5: Compliance Dashboard
**Excel Filename:** `ISMS-IMP-A.8.28.5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Dashboard Sheets (2-6):**
1. **Overall Compliance Summary**
   - Compliance by domain (IMP 1-4)
   - Trend analysis
   - Critical gap summary
   - Remediation roadmap
   - Executive summary

2. **SDLC Maturity Metrics**
   - Maturity level by phase
   - Process compliance
   - Training completion rates
   - Threat modeling coverage
   - Environment security posture

3. **Code Quality & Security Metrics**
   - Code review coverage
   - SAST/DAST findings trends
   - Vulnerability density
   - Remediation velocity
   - Technical debt tracking

4. **Third-Party Risk Metrics**
   - Component vulnerability exposure
   - License compliance rate
   - Critical dependency updates
   - Vendor security scores
   - Supply chain risk indicators

5. **KPIs & Reporting**
   - Security KPIs dashboard
   - Board-level reporting
   - Regulatory compliance view
   - Budget and resource tracking
   - Improvement initiatives

---

## 5. LAYER 3 - AUTOMATION SCRIPTS

### 5.1 Script Structure
```
scripts/
â"œâ"€â"€ excel_sanity_check_a828.py                    [~300 lines]
â"œâ"€â"€ generate_a828_1_sdlc_assessment.py            [~800-1000 lines, may split]
â"œâ"€â"€ generate_a828_2_standards_tools.py            [~800-1000 lines, may split]
â"œâ"€â"€ generate_a828_3_code_review_testing.py       [~800-1000 lines, may split]
â"œâ"€â"€ generate_a828_4_third_party_oss.py           [~800-1000 lines, may split]
â""â"€â"€ generate_a828_5_compliance_dashboard.py      [~800-1000 lines, may split]
```

### 5.2 Script Architecture (Common Pattern)

Each generator script follows this 10-section structure:
```python
#!/usr/bin/env python3
"""
ISMS-IMP-A.8.28.X - [Assessment Name] Excel Generator
ISO/IEC 27001:2022 Control A.8.28: Secure Coding

Requirements:
    sudo apt install python3-openpyxl
    
Usage:
    python3 generate_a828_X_assessment.py
    
Output:
    ISMS-IMP-A.8.28.X_[Name]_YYYYMMDD.xlsx
"""

from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# ==========================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ==========================================================================

def create_workbook() -> Workbook:
    """Create workbook with all required sheets."""
    pass

def setup_styles():
    """Define all cell styles used throughout the workbook."""
    pass

# ==========================================================================
# SECTION 2: COLUMN DEFINITIONS
# ==========================================================================

def get_base_columns():
    """Return base column structure (A-Q, 17 columns)."""
    pass

def get_extended_columns(sheet_type):
    """Return extended columns (R-X) based on sheet type."""
    pass

# ==========================================================================
# SECTION 3: DATA VALIDATION
# ==========================================================================

def create_base_validations(ws):
    """Create data validation objects for standard columns."""
    pass

# ==========================================================================
# SECTION 4: ASSESSMENT SHEET CREATOR (Generic Template)
# ==========================================================================

def create_assessment_sheet(ws, styles, section_title, policy_ref, 
                           question, checklist_items, reference_tables,
                           sheet_type="standard"):
    """Create a standardized assessment sheet with all components."""
    pass

# ==========================================================================
# SECTION 5: DOMAIN-SPECIFIC ASSESSMENT SHEETS (5 sheets)
# ==========================================================================

def create_sheet_2(wb, styles):
    """Create Sheet 2: [Domain-specific sheet 1]"""
    pass

def create_sheet_3(wb, styles):
    """Create Sheet 3: [Domain-specific sheet 2]"""
    pass

# ... (sheets 4-6)

# ==========================================================================
# SECTION 6: INSTRUCTIONS & LEGEND SHEET
# ==========================================================================

def create_instructions_sheet(ws, styles):
    """Create Instructions & Legend sheet."""
    pass

# ==========================================================================
# SECTION 7: SUMMARY DASHBOARD
# ==========================================================================

def create_summary_dashboard(ws, styles):
    """Create comprehensive summary dashboard with KPIs."""
    pass

# ==========================================================================
# SECTION 8: EVIDENCE REGISTER
# ==========================================================================

def create_evidence_register(ws, styles):
    """Create Evidence Register with 100 rows."""
    pass

# ==========================================================================
# SECTION 9: APPROVAL SIGN-OFF
# ==========================================================================

def create_approval_signoff(ws, styles):
    """Create Approval Sign-Off workflow sheet."""
    pass

# ==========================================================================
# SECTION 10: MAIN EXECUTION
# ==========================================================================

def main():
    """Main execution function - orchestrates workbook creation."""
    print("=" * 78)
    print(f"ISMS-IMP-A.8.28.X - [Assessment Name] Generator")
    print("ISO/IEC 27001:2022 Control A.8.28: Secure Coding")
    print("=" * 78)

    wb = create_workbook()
    styles = setup_styles()

    print("\n[1/9] Creating Instructions & Legend...")
    create_instructions_sheet(wb["Instructions & Legend"], styles)

    print("[2/9] Creating Assessment Sheet 1...")
    create_sheet_2(wb["1. [Sheet Name]"], styles)

    # ... [sheets 3-6]

    print("[7/9] Creating Summary Dashboard...")
    create_summary_dashboard(wb["Summary Dashboard"], styles)

    print("[8/9] Creating Evidence Register...")
    create_evidence_register(wb["Evidence Register"], styles)

    print("[9/9] Creating Approval Sign-Off...")
    create_approval_signoff(wb["Approval Sign-Off"], styles)

    filename = f"ISMS-IMP-A.8.28.X_[Name]_{datetime.now().strftime('%Y%m%d')}.xlsx"
    wb.save(filename)

    print(f"\n✅ SUCCESS: {filename}")
    print("\nWorkbook Structure:")
    print("  • Instructions & Legend")
    print("  • 5 Assessment Sheets (with checklists + reference tables)")
    print("  • Summary Dashboard (KPIs + gap analysis)")
    print("  • Evidence Register (100 rows)")
    print("  • Approval Sign-Off (3-level workflow)")
    print("\n" + "=" * 78)

if __name__ == "__main__":
    main()
```

### 5.3 Sanity Check Script

**Purpose:** Validate generated Excel files for structural integrity
```python
#!/usr/bin/env python3
"""
ISMS Control A.8.28 - Excel Workbook Sanity Check
Validates structure, formulas, and data validations

Usage:
    python3 excel_sanity_check_a828.py ISMS-IMP-A.8.28.1_*.xlsx
"""

def check_workbook_structure(filename):
    """Verify all required sheets exist"""
    pass

def check_data_validations(filename):
    """Verify dropdown validations are properly configured"""
    pass

def check_formulas(filename):
    """Verify formula integrity in dashboard"""
    pass

def check_styling(filename):
    """Verify consistent styling across sheets"""
    pass

def generate_report(results):
    """Generate sanity check report"""
    pass
```

---

## 6. PROJECT DELIVERABLES SUMMARY

### 6.1 Deliverables Checklist

**LAYER 1: POLICY DOCUMENTS (14 Documents)**
- [ ] ISMS-POL-A.8.28 - Master Policy
- [ ] ISMS-POL-A.8.28-S1 - Purpose, Scope, Definitions
- [ ] ISMS-POL-A.8.28-S2 - Requirements Overview
- [ ] ISMS-POL-A.8.28-S2.1 - Pre-Development Requirements
- [ ] ISMS-POL-A.8.28-S2.2 - Secure Coding Standards
- [ ] ISMS-POL-A.8.28-S2.3 - Code Review & Testing Requirements
- [ ] ISMS-POL-A.8.28-S2.4 - Third-Party & OSS Management
- [ ] ISMS-POL-A.8.28-S3 - Roles and Responsibilities
- [ ] ISMS-POL-A.8.28-S4 - Policy Governance
- [ ] ISMS-POL-A.8.28-S5 - Annexes
- [ ] ISMS-POL-A.8.28-S5.A - Language-Specific Guidelines
- [ ] ISMS-POL-A.8.28-S5.B - Code Review Checklist Template
- [ ] ISMS-POL-A.8.28-S5.C - Vulnerability Response Procedures
- [ ] ISMS-POL-A.8.28-S5.D - Quick Reference Guide

**LAYER 2: IMPLEMENTATION SPECS (5 Documents)**
- [ ] ISMS-IMP-A.8.28.1 - SDLC Assessment Specification
- [ ] ISMS-IMP-A.8.28.2 - Standards & Tools Assessment Specification
- [ ] ISMS-IMP-A.8.28.3 - Code Review & Testing Assessment Specification
- [ ] ISMS-IMP-A.8.28.4 - Third-Party & OSS Assessment Specification
- [ ] ISMS-IMP-A.8.28.5 - Compliance Dashboard Specification

**LAYER 3: AUTOMATION SCRIPTS (6 Scripts)**
- [ ] excel_sanity_check_a828.py
- [ ] generate_a828_1_sdlc_assessment.py
- [ ] generate_a828_2_standards_tools.py
- [ ] generate_a828_3_code_review_testing.py
- [ ] generate_a828_4_third_party_oss.py
- [ ] generate_a828_5_compliance_dashboard.py

**GENERATED ARTIFACTS (5 Excel Workbooks)**
- [ ] ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A.8.28.3_Code_Review_Testing_Assessment_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_YYYYMMDD.xlsx
- [ ] ISMS-IMP-A.8.28.5_Compliance_Dashboard_YYYYMMDD.xlsx

**Total:** 25 deliverables (14 POL + 5 IMP + 6 scripts) + 5 generated Excel files

### 6.2 Size Estimates

| Layer | Documents | Est. Lines | Est. Size |
|-------|-----------|------------|-----------|
| **POL** | 14 docs | ~5,000 lines | ~150 KB MD |
| **IMP** | 5 docs | ~2,000 lines | ~100 KB MD |
| **Scripts** | 6 scripts | ~5,000 lines | ~200 KB PY |
| **Excel** | 5 workbooks | N/A | ~2-5 MB each |
| **TOTAL** | 30 files | ~12,000 lines | ~400 KB + Excel |

---

## 7. IMPLEMENTATION ROADMAP

### 7.1 Phase-Based Approach
```
PHASE 1: FOUNDATION (Week 1-2)
â"œâ"€ Setup project structure
â"œâ"€ Review ISO 27002:2022 Control 8.28 in detail
â"œâ"€ Analyze reference frameworks (OWASP, NIST, CWE)
â"œâ"€ Create Master Policy (POL-A.8.28)
â""â"€ Create S1 (Purpose, Scope, Definitions)

PHASE 2: REQUIREMENTS (Week 3-4)
â"œâ"€ Create S2 (Requirements Overview)
â"œâ"€ Create S2.1 (Pre-Development Requirements)
â"œâ"€ Create S2.2 (Secure Coding Standards)
â"œâ"€ Create S2.3 (Code Review & Testing Requirements)
â""â"€ Create S2.4 (Third-Party & OSS Management)

PHASE 3: GOVERNANCE (Week 5)
â"œâ"€ Create S3 (Roles and Responsibilities)
â"œâ"€ Create S4 (Policy Governance)
â""â"€ Create S5 (Annexes Overview)

PHASE 4: ANNEXES (Week 6)
â"œâ"€ Create S5.A (Language-Specific Guidelines)
â"œâ"€ Create S5.B (Code Review Checklist Template)
â"œâ"€ Create S5.C (Vulnerability Response Procedures)
â""â"€ Create S5.D (Quick Reference Guide)

PHASE 5: IMPLEMENTATION SPECS (Week 7-9)
â"œâ"€ Create IMP-A.8.28.1 (SDLC Assessment Spec)
â"œâ"€ Create IMP-A.8.28.2 (Standards & Tools Spec)
â"œâ"€ Create IMP-A.8.28.3 (Code Review & Testing Spec)
â"œâ"€ Create IMP-A.8.28.4 (Third-Party & OSS Spec)
â""â"€ Create IMP-A.8.28.5 (Compliance Dashboard Spec)

PHASE 6: AUTOMATION (Week 10-12)
â"œâ"€ Create excel_sanity_check_a828.py
â"œâ"€ Create generate_a828_1_sdlc_assessment.py
â"œâ"€ Create generate_a828_2_standards_tools.py
â"œâ"€ Create generate_a828_3_code_review_testing.py
â"œâ"€ Create generate_a828_4_third_party_oss.py
â""â"€ Create generate_a828_5_compliance_dashboard.py

PHASE 7: VALIDATION & REFINEMENT (Week 13)
â"œâ"€ Generate all Excel workbooks
â"œâ"€ Run sanity checks
â"œâ"€ Conduct internal review
â"œâ"€ Refine based on feedback
â""â"€ Final quality assurance

PHASE 8: DOCUMENTATION & HANDOVER (Week 14)
â"œâ"€ Create implementation guide
â"œâ"€ Create user training materials
â"œâ"€ Document maintenance procedures
â""â"€ Prepare handover package
```

### 7.2 Iteration Strategy

Following Feynman's principle: "The first principle is that you must not fool 
yourself â€" and you are the easiest person to fool."

**Anti-Cargo-Cult Approach:**
1. Test each POL section with a "why does this exist?" challenge
2. Every IMP assessment must have a clear "what evidence?" answer
3. No checkbox compliance theater â€" focus on actual security improvement
4. Scripts must be maintainable by someone who didn't write them
5. Excel workbooks must be usable without a 50-page manual

**Iteration Checkpoints:**
- After each POL section: "Can an auditor understand this?"
- After each IMP spec: "Would a developer use this?"
- After each script: "Does this save time or create busywork?"

---

## 8. TECHNICAL SPECIFICATIONS

### 8.1 Document Format Standards

**Markdown Documents (POL & IMP):**
- Encoding: UTF-8
- Line endings: LF (Unix-style)
- Max line length: 120 characters (soft limit)
- Max document size: 400 lines (hard limit)
- Heading structure: # for title, ## for major sections, ### for subsections
- Date format in content: DD.MM.YYYY (e.g., 05.01.2026)

**Python Scripts:**
- Python version: 3.8+
- Style guide: PEP 8 compliant
- Max function length: 50 lines (split if longer)
- Max script length: 1000 lines (split into sections if longer)
- Required dependency: openpyxl (installable via apt or pip)
- Shebang: `#!/usr/bin/env python3`

**Excel Workbooks:**
- Format: .xlsx (OpenXML)
- Max sheets: 10-12
- Max rows per sheet: 1000 (practical limit for performance)
- Filename date format: YYYYMMDD (e.g., 20260105)
- Internal date format: DD.MM.YYYY

### 8.2 Naming Conventions

**Policy Documents:**
```
ISMS-POL-A_8_28_-_Secure_Coding_Policy.md
ISMS-POL-A_8_28-S[N]_-_[Section_Name].md
ISMS-POL-A_8_28-S[N]_[L]_-_[Subsection_Name].md
```

**Implementation Specifications:**
```
ISMS-IMP-A_8_28_[N]_-_[Assessment_Name].md
```

**Python Scripts:**
```
generate_a828_[N]_[assessment_name].py
excel_sanity_check_a828.py
```

**Generated Excel Files:**
```
ISMS-IMP-A_8_28_[N]_[Assessment_Name]_YYYYMMDD.xlsx
```

### 8.3 Excel Workbook Standards

**Color Palette (Consistent across all workbooks):**
- Header Blue: #003366
- Subheader Blue: #4472C4
- Column Header Gray: #D9D9D9
- Input Yellow: #FFFFCC
- Status Green (Compliant): #C6EFCE
- Status Yellow (Partial): #FFEB9C
- Status Red (Non-Compliant): #FFC7CE
- Planned Blue: #B4C7E7
- Border: Thin black (#000000)

**Font Standards:**
- Primary: Calibri
- Header: 14pt bold white
- Subheader: 11pt bold white
- Column headers: 10pt bold black
- Body text: 10pt regular black
- Input fields: 10pt regular black

**Sheet Structure:**
- Instructions & Legend: Always Sheet 1
- Assessment Sheets: Sheets 2-6 (5 assessment domains)
- Summary Dashboard: Sheet 7
- Evidence Register: Sheet 8
- Approval Sign-Off: Sheet 9

**Data Entry Standards:**
- User input cells: Yellow fill (#FFFFCC)
- Dropdown validations: Where applicable
- Date fields: DD.MM.YYYY format
- Freeze panes: Row 7 for assessments, Row 4 for dashboard

---

## 9. QUALITY ASSURANCE

### 9.1 Document Quality Checklist

**Before completing any POL or IMP document:**
- [ ] Document < 400 lines
- [ ] All dates in DD.MM.YYYY format
- [ ] No vendor/product names (vendor-agnostic)
- [ ] Clear policy references
- [ ] Logical section flow
- [ ] Spell-checked and grammar-checked
- [ ] Internal cross-references valid
- [ ] ISO 27001:2022 control alignment verified
- [ ] RACI responsibilities clear (for POL)
- [ ] Evidence requirements clear (for IMP)

### 9.2 Script Quality Checklist

**Before completing any Python script:**
- [ ] Script < 1000 lines (split if needed)
- [ ] PEP 8 compliant
- [ ] All functions documented
- [ ] Error handling implemented
- [ ] File paths use pathlib
- [ ] Dates in correct format (YYYYMMDD for filenames)
- [ ] Excel generation successful
- [ ] Sanity check passes
- [ ] Console output clear and helpful
- [ ] No hardcoded paths

### 9.3 Excel Quality Checklist

**Before finalizing any generated Excel workbook:**
- [ ] All required sheets present
- [ ] Instructions sheet complete and clear
- [ ] Assessment sheets have 5 domains
- [ ] Column headers match specification
- [ ] Data validations working
- [ ] Freeze panes configured
- [ ] Color scheme consistent
- [ ] Formulas calculate correctly
- [ ] Evidence Register has 100 rows
- [ ] Approval Sign-Off workflow complete
- [ ] File size reasonable (< 10 MB)

---

## 10. RISK MANAGEMENT

### 10.1 Project Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **Scope Creep** | Medium | High | Strict adherence to 400-line limit per document |
| **AI Timeout** | High | Medium | Split documents/scripts into sections |
| **Inconsistency** | Medium | High | Use Control 8.23 as reference template |
| **Over-Engineering** | Medium | High | Regular "anti-cargo-cult" reviews |
| **Unclear Requirements** | Low | High | Refer to ISO 27002:2022 text for clarity |
| **Tool Dependencies** | Low | Medium | Use widely available tools (openpyxl) |

### 10.2 Success Criteria

✅ **Completeness:** All 25 deliverables created  
✅ **Consistency:** All documents follow established patterns  
✅ **Usability:** Excel workbooks are intuitive without extensive training  
✅ **Maintainability:** Documents are modular and updatable  
✅ **Vendor-Agnosticism:** No vendor lock-in in policies or assessments  
✅ **Audit-Readiness:** Clear evidence requirements and traceability  
✅ **Practical Value:** Assessments provide actionable insights

---

## 11. NEXT STEPS

### 11.1 Immediate Actions

1. **Confirm Roadmap Approval**
   - Review and approve this roadmap
   - Confirm any adjustments needed
   - Lock down deliverables list

2. **Setup Project Structure**
```
   ISMS-Control-8.28/
   â"œâ"€â"€ docs/
   â"'   â"œâ"€â"€ policies/      (POL documents)
   â"'   â""â"€â"€ implementation/ (IMP documents)
   â"œâ"€â"€ scripts/          (Python generators)
   â"œâ"€â"€ generated/        (Excel outputs)
   â"œâ"€â"€ reference/        (ISO docs, OWASP, etc.)
   â""â"€â"€ README.md         (Project overview)
```

3. **Begin Phase 1 Implementation**
   - Start with ISMS-POL-A.8.28 (Master Policy)
   - Follow with ISMS-POL-A.8.28-S1 (Purpose, Scope, Definitions)

### 11.2 Questions for Clarification

Before we begin implementation, please confirm:

1. **Scope Confirmation:**
   - Are there specific programming languages to prioritize in S5.A?
   - Are there specific third-party/OSS tools already in use?
   - Any specific regulatory requirements (GDPR, SOC2, etc.)?

2. **Stakeholder Preferences:**
   - Any specific assessment format preferences?
   - Preferred evidence collection methods?
   - Any existing secure coding standards to integrate?

3. **Technical Constraints:**
   - Any restrictions on Python dependencies?
   - Any specific Excel version compatibility requirements?
   - Any corporate Excel templates to follow?

---

## 12. REFERENCES

### 12.1 Standards & Frameworks

- **ISO/IEC 27001:2022** - Information Security Management Systems
- **ISO/IEC 27002:2022** - Information Security Controls (Control A.8.28)
- **OWASP Top 10** - Web Application Security Risks
- **OWASP ASVS** - Application Security Verification Standard
- **OWASP SAMM** - Software Assurance Maturity Model
- **CWE Top 25** - Most Dangerous Software Weaknesses
- **NIST SP 800-218** - Secure Software Development Framework (SSDF)
- **SANS Top 25** - Most Dangerous Software Errors

### 12.2 Project References

- **Control 8.23 Implementation** - Reference pattern for this project
- **IMP Template** - Implementation document structure
- **Regulatory Applicability Framework** - ISMS-POL-00

### 12.3 Cargo Cult Warning

> "The first principle is that you must not fool yourself â€" and you are the 
> easiest person to fool." â€" Richard Feynman

This project aims for **substance over ceremony**. Every requirement, every 
checklist item, every assessment question should have a clear "why" that traces 
back to actual security improvement, not just compliance theater.

---

## DOCUMENT CONTROL

**Document ID:** ISMS-A.8.28-ROADMAP  
**Version:** 1.0  
**Date:** 05.01.2026  
**Status:** Awaiting Approval  
**Prepared By:** ISMS Implementation Team  
**Next Action:** Begin Phase 1 - Foundation

---

**END OF ROADMAP**

*"If you can't explain it simply, you don't understand it well enough."*  
*â€" Often attributed to Einstein, probably apocryphal, but good advice nonetheless.*

Ready to proceed with implementation?