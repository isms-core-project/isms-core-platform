**ISMS-IMP-A.5.8.1-TG - Project Lifecycle Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.8: Information Security in Project Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.8.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Project Lifecycle Security Integration |
| **Related Policy** | ISMS-POL-A.5.8, Section 2.3 (Security Activities Across Project Lifecycle) |
| **Purpose** | Assess integration of information security activities across all project phases (Initiation → Planning → Execution → Monitoring → Closure) with phase-by-phase compliance verification and gate review documentation |
| **Target Audience** | Project Managers, Project Security Coordinators, PMO Staff, Information Security Officers, Project Steering Committees, Auditors |
| **Assessment Type** | Process & Procedural Compliance |
| **Review Cycle** | Per Project Phase (at each gate review) + Annual Post-Project Review for lessons learned |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Project Lifecycle Security Assessment workbook | ISMS Implementation Team |

---

# Technical Specification

**Audience:** Workbook Developers (Python/Excel script maintainers)

---

# Workbook Structure

## Overall Design Philosophy

This workbook implements a **phase-based progressive assessment model** where:
1. Each project phase has dedicated sheet
2. Sheets unlock/enable as project progresses
3. Compliance scores auto-calculate from checklist completion
4. Dashboard auto-aggregates from all phase sheets
5. Evidence centrally tracked but linked from phase activities

**Design Principles:**

- **Iterative:** Not a one-time completion, updated throughout project lifecycle
- **Automated:** Maximum use of formulas to reduce manual calculation
- **Evidence-centric:** Every activity has evidence link field
- **Audit-ready:** Clear traceability from requirement → implementation → test → evidence
- **Flexible:** Works with any project methodology (Waterfall, Agile, hybrid)

## Sheet Layout

| Sheet # | Sheet Name | Purpose | User Interaction | Dependencies |
|---------|------------|---------|------------------|--------------|
| 1 | Instructions | Guide, legend, methodology | Read-only | None |
| 2 | Project Classification | Risk level determination | Fill criteria, get approval | None |
| 3 | Initiation Phase | Stakeholder ID, initial risks, budget | Complete checklist, link evidence | Sheet 2 (classification) |
| 4 | Planning Phase | Requirements, threat model, test plan | Complete checklist, link evidence | Sheet 2 (classification) |
| 5 | Execution Phase | Testing, remediation, documentation | Complete checklist, link evidence | Sheet 2, 4 (test plan) |
| 6 | Monitoring Phase | Risk updates, change assessment, metrics | Update regularly | Sheet 2, 3 (risks) |
| 7 | Closure Phase | Handover, risk acceptance, lessons learned | Complete checklist, link evidence | Sheet 2, 5 (findings) |
| 8 | Compliance Dashboard | Executive summary, scoring, gaps | Auto-populated (read-only) | All phase sheets |
| 9 | Evidence Register | Centralized evidence tracking | Link evidence items | All phases |
| 10 | Sign-Off | Approval workflow | Signatures and approvals | Sheet 8 (summary) |

**Total Sheets:** 10

---

# Cell Styling Reference

## Standard Styling Conventions

| Element | Cell Format | Color Code | Font | Protection |
|---------|-------------|------------|------|------------|
| **Main Headers (Level 1)** | Dark blue fill, white text, bold | Fill: #003366, Font: #FFFFFF | Calibri 16pt bold | Protected |
| **Section Headers (Level 2)** | Medium blue fill, white text, bold | Fill: #305496, Font: #FFFFFF | Calibri 14pt bold | Protected |
| **Column Headers** | Light blue fill, dark text, bold | Fill: #B4C7E7, Font: #000000 | Calibri 11pt bold | Protected |
| **User Input Cells** | Yellow fill, black text | Fill: #FFEB9C, Font: #000000 | Calibri 11pt | Unprotected |
| **Protected Formula Cells** | White or light gray fill | Fill: #FFFFFF or #F2F2F2 | Calibri 11pt | Protected |
| **Example Cells** | Light gray, italic | Fill: #D9D9D9, Font: #595959 | Calibri 11pt italic | Protected |

## Status Color Coding

| Status | Symbol | Background Color | Use Case |
|--------|--------|------------------|----------|
| Complete | ✅ | Green #C6EFCE | Activity completed with evidence |
| In Progress | 🔄 | Blue #B4C7E7 | Activity started but not complete |
| Warning/Incomplete | ⚠️ | Yellow #FFEB9C | Activity required but missing |
| Not Done | ❌ | Red #FFC7CE | Activity not started |
| Not Applicable | N/A | Gray #D9D9D9 | Activity not required for this classification |

## Dropdown Styling

**Best Practices:**

- Use data validation with dropdown lists for consistency
- Include emoji symbols in options where appropriate (✅ ⚠️ ❌ 🔄)
- Provide "N/A" option where applicability varies by classification
- Error alerts: Show warning (not stop) if invalid entry
- Input message: Brief hint about what to select

**Example Dropdown Setup:**
```
Field: Status
List Source: ✅ Complete, 🔄 In Progress, ⚠️ Incomplete, ❌ Not Done, N/A
Allow: List
Error Alert: Warning style, "Please select from dropdown"
Input Message: "Select activity completion status"
```

## Conditional Formatting Rules

**1. Compliance Scores:**
```
Range: Compliance score cells
Rules:

- If ≥90: Dark green background (#00B050)
- If ≥75 AND <90: Light green background (#C6EFCE)
- If ≥60 AND <75: Yellow background (#FFEB9C)
- If ≥40 AND <60: Orange background (#FFC000)
- If <40: Red background (#FFC7CE)

```

**2. Status Cells:**
```
Range: Status dropdown cells
Rules:

- If "✅": Green background (#C6EFCE)
- If "🔄": Blue background (#B4C7E7)
- If "⚠️": Yellow background (#FFEB9C)
- If "❌": Red background (#FFC7CE)
- If "N/A": Gray background (#D9D9D9)

```

**3. Date Cells:**
```
Range: Target date cells
Rules:

- If < TODAY() AND status <> "✅": Red text (past due)
- If < TODAY()+7 AND status <> "✅": Orange text (due within 7 days)
- If > TODAY()+7: Black text (future)

```

**4. Finding Severity:**
```
Range: Severity cells
Rules:

- If "Critical": Red background (#FFC7CE), bold
- If "High": Orange background (#FFC000)
- If "Medium": Yellow background (#FFEB9C)
- If "Low": White background (default)

```

---

# Integration Points

## With ISMS-IMP-A.5.8.2 (Security Requirements Register)

**Data Flow:**

- **Sheet 2 (Classification)** → A.5.8.2 header (project name, classification, PM)
- **Sheet 4 (Planning Phase)** → A.5.8.2 requirements count
- **A.5.8.2 (Requirements status)** → Sheet 5 (Execution) implementation rate

**Integration Methods:**
1. **Manual:** Hyperlink from Sheet 4 to A.5.8.2 workbook
2. **Semi-automated:** Copy/paste requirement counts from A.5.8.2 to Sheet 4
3. **Fully automated:** If workbooks in same directory, use INDIRECT or external reference formulas

**Recommended:** Manual hyperlink for simplicity, avoiding external reference complexity

## With ISMS-IMP-A.5.8.3 (Portfolio Dashboard)

**Data Extraction (Read by A.5.8.3 script):**

A.5.8.3 consolidation script reads this workbook and extracts:

**From Sheet 2 (Classification):**

- Cell B5: Project Name
- Cell H58: Final Classification
- Cell B7: Project Manager
- Cell B8: Business Owner

**From Sheet 8 (Dashboard):**

- Overall Compliance Score cell
- Current Phase cell
- Critical gaps count
- Open Critical/High findings count

**From Sheet 7 (Closure):**

- Residual risk level cell
- Closure status cell

**Integration Method:** Python script (openpyxl) with read_only=True, data_only=True

**Cell References Must Be Stable:** Script expects specific cell addresses, don't move key cells

## With Project Management Tools

**Export Capabilities:**

- **Risk Register (Sheet 3, 6)** → Export to enterprise risk register (Jira Risk Register, ServiceNow, etc.)
- **Findings (Sheet 5)** → Export to issue tracker (Jira, Azure DevOps)
- **Evidence Register (Sheet 9)** → Index for project document repository

**Import Capabilities:**

- **Project Details** → Import from PMO system (project name, PM, dates, budget)
- **Risk Data** → Import from enterprise risk tool if organization uses centralized risk management

**Recommended:** Keep this assessment as single source of truth for project security status, sync to other tools but don't create circular dependencies

## With ISMS Asset Inventory (A.5.9)

**Data Flow:**

- **Sheet 7 (Closure, Section C)** lists assets created/modified by project
- These assets → registered in ISMS Asset Inventory
- Process: Manual (export asset list, import to inventory) or API integration if inventory system supports it

---

# Maintenance and Version Control

## Annual Template Review

**Review Checklist:**

- [ ] ISMS-POL-A.5.8 policy changes → update required activities
- [ ] New regulatory requirements → add compliance checks
- [ ] User feedback → improve usability, add clarifications
- [ ] Dropdown options → add new project types, methodologies, tools
- [ ] Scoring thresholds → calibrate based on organizational maturity
- [ ] Example content → update for relevance, add new examples

**Version Control:**

- Maintain template in version control (Git or document management system)
- Track changes: version number, date, change description, approver
- Test new template versions with pilot projects before rollout
- Provide migration guide if structure changes significantly

## Customization Guidance

**Organizations SHOULD customize:**

- **Project Type dropdown** (Sheet 2): Add organization-specific project categories
- **Stakeholder Roles** (Sheet 3): Add custom security roles (e.g., Cloud Security Engineer)
- **Evidence Types** (Sheet 9): Add organization-specific evidence systems
- **Approval Workflow** (Sheet 10): Match organization's approval hierarchy

**Organizations MUST NOT customize (breaks comparability/integration):**

- **Compliance scoring formulas:** Changing weights or calculation breaks cross-project comparison
- **Required activities list:** Must match ISMS-POL-A.5.8 requirements
- **Sheet structure for integration:** Changing key cell locations breaks Portfolio Dashboard (A.5.8.3)
- **Classification criteria:** Organizational standard, changes require CISO approval

---

**END OF SPECIFICATION**

---

*"Everything we call real is made of things that cannot be regarded as real."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
