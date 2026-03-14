<h1 align="center">🎋 Contributing to ISMS CORE</h1>

<p align="center">
  <img src="https://img.shields.io/badge/QA-Engineering_First-2E8B57?style=for-the-badge" alt="QA Engineering First"/>
</p>

<p align="center">
  <a href="#-qa-gates"><img src="https://img.shields.io/badge/QA_Gates-Enforced-00AA00?style=flat-square" alt="QA Gates"/></a>
  <a href="#-python-script-standards"><img src="https://img.shields.io/badge/Python-Standardized-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/></a>
  <a href="#-online-research-requirement"><img src="https://img.shields.io/badge/Research-Required-FF6600?style=flat-square" alt="Research Required"/></a>
  <a href="#-the-engineering-principle"><img src="https://img.shields.io/badge/Feynman-Approved-0066CC?style=flat-square" alt="Feynman Approved"/></a>
</p>

<p align="center">
  <em>Not all documents require the same level of standardization. Apply rigor where it matters.</em>
</p>

---

## 🎯 QA Philosophy

ISMS CORE applies appropriate rigor based on what matters for **reliability**, **maintainability**, and **correctness**.

> *"Standardization is good. Over-standardization is cargo cult. Apply rigor where it matters."*

---

## 📋 Document Types and Quality Standards

<table>
<tr>
<th>Type</th>
<th>Consistency</th>
<th>Change Freq</th>
<th>QA Gate</th>
<th>Badge</th>
</tr>
<tr>
<td><strong>📜 POL</strong> (Policy)</td>
<td>🔴 High</td>
<td>Low</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Formal_Approval-9400D3?style=flat-square" alt="Formal"/></td>
</tr>
<tr>
<td><strong>📋 IMP</strong> (Implementation)</td>
<td>🟡 Moderate</td>
<td>Medium</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Living_Document-32CD32?style=flat-square" alt="Living"/></td>
</tr>
<tr>
<td><strong>🐍 SCR</strong> (Scripts)</td>
<td>🔴 High</td>
<td>Medium</td>
<td><code># QA_VERIFIED:</code></td>
<td><img src="https://img.shields.io/badge/Code_Review-3776AB?style=flat-square" alt="Code Review"/></td>
</tr>
<tr>
<td><strong>📚 REF</strong> (Reference)</td>
<td>🟡 Moderate</td>
<td>Low</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Technical_Accuracy-FF6600?style=flat-square" alt="Technical"/></td>
</tr>
<tr>
<td><strong>🏢 CTX</strong> (Context)</td>
<td>🟡 Moderate</td>
<td>Low</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Accuracy_Verified-0066CC?style=flat-square" alt="Verified"/></td>
</tr>
<tr>
<td><strong>📝 FORM</strong> (Forms)</td>
<td>🟡 Moderate</td>
<td>Low</td>
<td><code>&lt;!-- QA_VERIFIED --&gt;</code></td>
<td><img src="https://img.shields.io/badge/Template_Verified-32CD32?style=flat-square" alt="Template"/></td>
</tr>
</table>

---

### 📋 IMP Document Structure (UG / TG)

Every IMP (Implementation) document exists as a **paired set** of two files — a User Guide and a Technical Specification. This separation gives auditors, implementers, and developers each a purpose-built document without cross-contamination.

```
IMP/
├── ISMS-IMP-A.8.9.1-UG - Baseline Configuration Assessment.md    ← For implementers
└── ISMS-IMP-A.8.9.1-TG - Baseline Configuration Assessment.md    ← For developers/auditors
```

#### UG — User Completion Guide

**Audience:** Security analysts, control owners, assessors, compliance officers

The UG is the **human-written** document that guides someone through completing an assessment workbook. It answers: *"I have this Excel file — what do I do with it?"*

| Section | Purpose |
|---------|---------|
| Assessment Overview | What this assessment covers, why it matters, scope boundaries |
| Prerequisites | What must be in place before starting (access, data, approvals) |
| Workbook Structure | Sheet-by-sheet overview of the Excel workbook |
| Completion Walkthrough | Step-by-step instructions for filling in each sheet |
| Evidence Collection | What evidence to gather, where to store it, naming conventions |
| Common Pitfalls | 8-10 `MISTAKE:` examples with corrections |
| Quality Checklist | Verification items before submission |
| Review & Approval | Who reviews, approval workflow, escalation |

#### TG — Technical Specification

**Audience:** Python developers, Excel workbook developers, QA engineers

The TG is **auto-generated** from the Python generator script (`SCR/generate_*.py`). It is a human-readable translation of the generator's code — every sheet, column, data validation dropdown, color style, and formula documented in structured tables.

| Section | Purpose |
|---------|---------|
| Workbook Overview | Document ID, output filename, total sheets, control reference |
| Color Palette | All hex codes, style names, and usage descriptions |
| Sheet N: *Name* | Per-sheet specification with columns, widths, validations, formulas |
| Data Validation Lists | All dropdown value lists defined in the generator |

**Regenerating TGs:** TG content is regenerated by the factory script whenever generators change:

```bash
python3 generate_tg_from_scr.py --apply          # All 252 TGs
python3 generate_tg_from_scr.py --control a.8.9   # Single control group
```

The top of each TG's technical content shows its source:

```
> Auto-generated from `generate_a89_1_baseline_configuration.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`
```

#### IMP QA Criteria (v4.5+)

| Requirement | Description |
|-------------|-------------|
| ✅ UG/TG split | Each IMP exists as `-UG` and `-TG` file pair |
| ✅ Standard header | 3-line format: bold title, subtitle (UG/TG), ISO control reference |
| ✅ Control quotes | Use "should" (not "shall") per ISO 27001:2022 Annex A |
| ✅ British spelling | organisation, authorised, standardised |
| ✅ Standard ending | `**END OF SPECIFICATION**` + separator + quote with em-dash (—) |
| ✅ QA tag | `<!-- QA_VERIFIED: YYYY-MM-DD -->` after bamboo tag |

---

## 🚦 QA Gates

<p align="center">
  <img src="https://img.shields.io/badge/Gate-Pass_Required-00AA00?style=for-the-badge" alt="Gate Pass Required"/>
</p>

Content is promoted to this repository **only when QA gates pass**. Each document type carries a QA marker that must be present before promotion:

| Document | QA marker required |
|----------|--------------------|
| POL / IMP / REF / CTX / FORM | `<!-- QA_VERIFIED: YYYY-MM-DD -->` at end of file |
| SCR (Python scripts) | `# QA_VERIFIED: YYYY-MM-DD` footer block |

> **Note for maintainers:** Promotion is handled by the internal development tooling in the private `factory_claude_ai` repository (`95-isms-core-factory/promote_control.sh`). Content in this repository has already passed all QA gates before being published here.

---

## 🐍 Python Script Standards

### Required Structure

```python
# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.X.X.X"
WORKBOOK_NAME = "Assessment Name"
CONTROL_ID = "A.X.X"
CONTROL_NAME = "Control Name"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"
```

### Logging

| ❌ Don't | ✅ Do |
|----------|-------|
| `print("message")` | `logger.info("message")` |

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)
```

### QA Footer

```python
# =============================================================================
# QA_VERIFIED: YYYY-MM-DD
# QA_STATUS: PASSED
# QA_TOOL: Claude Code
# CHANGES: Description of changes
# =============================================================================
```

---

## 📂 Folder Structure

Each control is self-contained with all artifact types:

```
isms-a.X.X-control-name/
├── POL/                      # 📜 Policy documents
├── IMP/                      # 📋 Implementation guides (UG + TG pairs)
├── SCR/                      # 🐍 Scripts (generators, normalizers, consolidators)
├── WKBK/                     # 📊 Generated Excel workbooks
├── REF/                      # 📚 Reference materials (if applicable)
├── CTX/                      # 🏢 Context documents (if applicable)
└── FORM/                     # 📝 Forms and templates (if applicable)
```

---

## 🔍 Online Research Requirement

<p align="center">
  <img src="https://img.shields.io/badge/⚠️_Research-MANDATORY-FF0000?style=for-the-badge" alt="Research Mandatory"/>
</p>

**All IMP and SCR development MUST include online research** to verify:

- ✅ Current best practices for the control
- ✅ Alignment with NIST, CIS, MITRE ATT&CK frameworks
- ✅ Technical accuracy of implementation guidance
- ✅ Latest tool capabilities and integration patterns

**Key frameworks to reference:**

<p align="center">
  <img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square" alt="ISO"/>
  <img src="https://img.shields.io/badge/NIST_CSF-2.0-FF6600?style=flat-square" alt="NIST"/>
  <img src="https://img.shields.io/badge/CIS_Controls-v8-00AA00?style=flat-square" alt="CIS"/>
  <img src="https://img.shields.io/badge/MITRE_ATT&CK-Enterprise-DC143C?style=flat-square" alt="MITRE"/>
</p>

---

## ⚖️ The Engineering Principle

> *"Standardization is good. Over-standardization is cargo cult. Apply rigor where it matters."*

**Feynman would ask:** *"Does this variation serve a purpose?"*

| Answer | Action |
|--------|--------|
| ✅ YES | Document why and keep it |
| ❌ NO | Standardize |
| ⚠️ Breaks functionality | Don't force uniformity |

---

## 🔬 Validation Process

<p align="center">
  <img src="https://img.shields.io/badge/Multi--Stage-QA_Process-DC143C?style=for-the-badge" alt="Multi-Stage QA Process"/>
</p>

Every control pack undergoes a structured multi-stage validation process to ensure quality and correctness.

```
  ┌─────────────────────────┐
  │     The ISMS Core Project     │
  │   (Architect / Owner)   │
  └────────────┬────────────┘
               │ Requirements + Domain Expertise
               ▼
  ┌─────────────────────────┐
  │   Claude Code (Sonnet)    │──── Implementation
  │   Build + Code Review   │     POL, IMP, SCR, REF, CTX
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │    ISMS Copilot X       │──── Audit Review
  │  (Documentation + QA)   │     Stage 1: adequacy, Stage 2: effectiveness
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │     The ISMS Core Project     │
  │   Final Approval Gate   │
  └─────────────────────────┘
```

| Contributor | Role | Focus |
|-------------|------|-------|
| **Claude Code (Sonnet)** | Implementation + QA | Policy writing, Python generators, code review, pattern analysis |
| **ISMS Copilot X** | Documentation Audit | Stage 1 documentation adequacy, Stage 2 implementation effectiveness |
| **The ISMS Core Project** | Architect + Final Gate | Methodology, domain expertise, IP ownership, approval authority |

Each stage operates under **purpose-built instruction sets** authored by The ISMS Core Project — structured prompts defining scope, constraints, output format, and audit criteria. These are controlled operational documents specifying exactly what must be checked, what to ignore (e.g., placeholder dates), and how to classify findings.

### Finding Classification

| Severity | Criteria | Action |
|----------|----------|--------|
| **Critical** | Missing control implementation, audit blocker | Must resolve before promotion |
| **High** | Significant gap in evidence or coverage | Must resolve before promotion |
| **Medium** | Incomplete guidance, minor inconsistency | Resolve during QA pass |
| **Low** | Style, formatting, enhancement opportunity | Track for future iteration |

---

## 🤖 AI-Assisted Development

<table>
<tr>
<th>Contributor</th>
<th>Role</th>
</tr>
<tr>
<td><strong>The ISMS Core Project</strong></td>
<td>Methodology, architecture, domain expertise, IP ownership</td>
</tr>
<tr>
<td><strong>Claude Code (Sonnet)</strong></td>
<td>Primary implementation partner — see detailed contribution below</td>
</tr>
<tr>
<td><strong>ISMS Copilot X</strong></td>
<td>Documentation audit, adequacy review, implementation effectiveness</td>
</tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/IP_Ownership-Gregory_Griffin-FFD700?style=flat-square" alt="IP Ownership"/>
</p>

---

## 🧠 Claude Code — Implementation Contribution

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Sonnet_4.6-CC785C?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code Sonnet"/>
  <img src="https://img.shields.io/badge/Dec_2025–Feb_2026-6_Weeks-2E8B57?style=for-the-badge" alt="6 Weeks"/>
</p>

Claude Code (Anthropic, Sonnet model family) has been the primary implementation partner on ISMS CORE since December 31, 2025. Working in continuous pairing sessions directed by The ISMS Core Project — who authored all methodology, architectural decisions, prompt instruction sets, and multi-model orchestration — Claude Code delivered the full automation layer, wrote and refined all documentation, and built the factory infrastructure that makes this project maintainable.

### What was built

<table>
<tr>
<th>Category</th>
<th>Deliverable</th>
<th>Scale</th>
</tr>
<tr>
<td><strong>Python Scripts</strong></td>
<td>Workbook Generators</td>
<td><strong>274</strong> scripts total — 188 (FW) + 53 (OP) + 21 (PRIV) + 12 (CLD)</td>
</tr>
<tr>
<td><strong>IMP Documents</strong></td>
<td>User Guides (UG) + Technical Specifications (TG) for every assessment</td>
<td><strong>442</strong> files — 376 FW (188 UG + 188 TG) + 42 PRIV + 24 CLD</td>
</tr>
<tr>
<td><strong>POL Documents</strong></td>
<td>Policy framework with "WITH WHAT" verification methodology</td>
<td><strong>53</strong> framework POLs + <strong>53</strong> operational OP-POLs</td>
</tr>
<tr>
<td><strong>Excel Workbooks</strong></td>
<td>Assessment workbooks with data validation, formulas, conditional formatting</td>
<td><strong>188</strong> (FRAMEWORK) + <strong>53</strong> (OPERATIONAL)</td>
</tr>
<tr>
<td><strong>Factory Automation</strong></td>
<td>Assembly, promotion, backup, sync, splitting, normalization scripts</td>
<td>10+ major tools</td>
</tr>
<tr>
<td><strong>QA Infrastructure</strong></td>
<td>QA gates, status dashboards, verification pipeline</td>
<td><strong>53/53</strong> controls passing</td>
</tr>
</table>

### The journey

```
December 31st 2025: Pilot Control Creation -> A.8.24
January 31st 2026: ISMS CORE Framework -> 93 Controls Completed in 53 Control Packs
February 7th 2026: ISMS CORE Operational -> 93 Controls Completed in 53 Control Packs
February 8th 2026: Python Scripts QA (Ongoing)
```

### Platform

The **ISMS CORE Platform** (`isms-core-platform/`) is live — a FastAPI backend with PostgreSQL, Docker Compose deployment, nginx TLS, and framework correlation engine. It transforms the file-based framework into a live compliance platform: DB-driven, WebUI-editable, with evidence tracking, gap management, crosswalk mapping across 18+ regulatory frameworks, and 44 automated evidence connectors.

<p align="center">
  <em>Built with the conviction that security compliance should be engineering discipline, not checkbox theater.</em>
</p>

---

<p align="center">
  <strong>Copyright © 2025-2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
