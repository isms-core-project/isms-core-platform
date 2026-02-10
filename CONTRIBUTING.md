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

Content is promoted to the main repository **only when QA gates pass**:

```bash
# Check QA status
./promote_control.sh --status

# Dry-run promotion
./promote_control.sh --dry-run isms-a.8.24-use-of-cryptography

# Promote verified content
./promote_control.sh isms-a.8.24-use-of-cryptography
```

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

## 🎬 Presentation Mode

<p align="center">
  <img src="https://img.shields.io/badge/CISO_Demo-Ready-DC143C?style=for-the-badge" alt="CISO Demo Ready"/>
</p>

Populate scripts fill workbooks with realistic sample data for presentations.

**Pattern for MergedCell handling:**

```python
from openpyxl.cell.cell import MergedCell

def safe_cell_write(ws, cell_ref, value):
    """Safely write to a cell, handling merged cells."""
    try:
        cell = ws[cell_ref]
        if not isinstance(cell, MergedCell):
            cell.value = value
    except Exception as e:
        pass
```

**Reference implementations:**

| Control | Scripts | Data Points |
|---------|:-------:|:-----------:|
| A.8.23 Web Filtering | 4 | 250+ |
| A.8.24 Use of Cryptography | 4 | 350+ |

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

## 🔬 Triple-Validation Process

<p align="center">
  <img src="https://img.shields.io/badge/Adversarial-Multi--Model_QA-DC143C?style=for-the-badge" alt="Adversarial Multi-Model QA"/>
</p>

Every control pack undergoes adversarial multi-model validation. Controls are reviewed by competing AI models to ensure no single model's blind spots compromise quality.

```
  ┌─────────────────────────┐
  │     Gregory Griffin     │
  │   (Architect / Owner)   │
  └────────────┬────────────┘
               │ Requirements + Domain Expertise
               ▼
  ┌─────────────────────────┐
  │   Claude Code (Opus)    │──── Implementation
  │   Build + Code Review   │     POL, IMP, SCR, REF, CTX
  └────────────┬────────────┘
               │
       ┌───────┴───────┐
       ▼               ▼
 ┌───────────┐   ┌───────────┐
 │ Copilot X │   │   GPT-5   │
 │ Blue Team │   │ Red Team  │
 │  (Audit)  │   │ (Attack)  │
 └─────┬─────┘   └─────┬─────┘
       │               │
       └───────┬───────┘
               ▼
  ┌─────────────────────────┐
  │     Gregory Griffin     │
  │   Final Approval Gate   │
  └─────────────────────────┘
```

| Model | Role | Focus |
|-------|------|-------|
| **Claude Code (Opus)** | Implementation + QA | Policy writing, Python generators, code review, pattern analysis |
| **ISMS Copilot X** | Blue Team Audit | Stage 1 documentation adequacy, Stage 2 implementation effectiveness |
| **ChatGPT GPT-5** | Red Team Auditor | Attack surface review, gap identification, adversarial testing |
| **Gregory Griffin** | Architect + Final Gate | Methodology, domain expertise, IP ownership, approval authority |

Each model operates under **purpose-built instruction sets** authored by Gregory Griffin — structured prompts defining scope, constraints, output format, and audit criteria. These aren't casual prompts; they are controlled operational documents specifying exactly what each model must check, what to ignore (e.g., placeholder dates), and how to classify findings. The instruction sets themselves represent a reusable methodology for AI-governed compliance engineering.

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
<td><strong>Gregory Griffin</strong></td>
<td>Methodology, architecture, domain expertise, IP ownership</td>
</tr>
<tr>
<td><strong>Claude Code (Opus)</strong></td>
<td>Primary implementation partner — see detailed contribution below</td>
</tr>
<tr>
<td><strong>ISMS Copilot X</strong></td>
<td>Blue team audit, documentation adequacy, implementation review</td>
</tr>
<tr>
<td><strong>ChatGPT GPT-5</strong></td>
<td>Red team audit, adversarial testing, gap identification</td>
</tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/IP_Ownership-Gregory_Griffin-FFD700?style=flat-square" alt="IP Ownership"/>
</p>

---

## 🧠 Claude Code — Implementation Contribution

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Opus_4-CC785C?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code Opus"/>
  <img src="https://img.shields.io/badge/Dec_2025–Feb_2026-6_Weeks-2E8B57?style=for-the-badge" alt="6 Weeks"/>
</p>

Claude Code (Anthropic, Opus model family) has been the primary implementation partner on ISMS CORE since December 31, 2025. Working in continuous pairing sessions directed by Gregory Griffin — who authored all methodology, architectural decisions, prompt instruction sets, and multi-model orchestration — Claude Code delivered the full automation layer, wrote and refined all documentation, and built the factory infrastructure that makes this project maintainable.

### What was built

<table>
<tr>
<th>Category</th>
<th>Deliverable</th>
<th>Scale</th>
</tr>
<tr>
<td><strong>Python Scripts</strong></td>
<td>Generators, normalizers, consolidators, sanity checks, population scripts</td>
<td><strong>454</strong> scripts, <strong>410K+</strong> lines</td>
</tr>
<tr>
<td><strong>IMP Documents</strong></td>
<td>User Guides (UG) + Technical Specifications (TG) for every assessment</td>
<td><strong>504</strong> files (252 UG + 252 TG)</td>
</tr>
<tr>
<td><strong>POL Documents</strong></td>
<td>Policy framework with "WITH WHAT" verification methodology</td>
<td><strong>68</strong> policies, all audited</td>
</tr>
<tr>
<td><strong>Excel Workbooks</strong></td>
<td>Assessment workbooks with data validation, formulas, conditional formatting</td>
<td><strong>299+</strong> generated</td>
</tr>
<tr>
<td><strong>Factory Automation</strong></td>
<td>Assembly, promotion, backup, sync, splitting, normalization scripts</td>
<td><strong>9</strong> major tools</td>
</tr>
<tr>
<td><strong>QA Infrastructure</strong></td>
<td>QA gates, status dashboards, verification pipeline</td>
<td><strong>53/53</strong> controls passing</td>
</tr>
</table>

### The journey (6 weeks)

```
Week 1 (Dec 31–Jan 6)    Foundation — first generators, script patterns, pilot controls
Week 2 (Jan 7–13)        Scale — Section 8 technological controls, workbook generation
Week 3 (Jan 14–20)       Depth — IMP specifications, formula validation (180K+ formulas)
Week 4 (Jan 21–27)       Standardization — Phase 1-3 Python QA (322 scripts), SPDX licensing
Week 5 (Jan 28–Feb 3)    Completion — final 9 controls, POL promotion, production sync
Week 6 (Feb 4–6)         Architecture — UG/TG split (504 files), POL updates, full GitHub sync
```

### Key engineering decisions

| Decision | Rationale |
|----------|-----------|
| **UG/TG split** | Separated user-facing guidance from technical specs — cleaner consumption, independent update cycles |
| **QA-gated promotion** | `promote_control.sh` enforces QA markers before any content reaches GitHub |
| **Logger over print** | Structured logging across 454 scripts for production traceability |
| **Factory scripts** | Repeatable automation for assembly, normalization, and sync — not manual file copying |
| **Consolidation dashboards** | Cross-workbook aggregation with automatic gap identification |

### What's next

The **ISMS CORE Platform** (`60-isms-core-api/`) is architected and ready for implementation — a FastAPI backend with PostgreSQL, Docker Compose deployment, and framework correlation engine inspired by [OpenCTI](https://github.com/OpenCTI-Platform/opencti). This will transform the current file-based framework into a live compliance platform with knowledge graph capabilities.

<p align="center">
  <em>Built with the conviction that security compliance should be engineering discipline, not checkbox theater.</em>
</p>

---

<p align="center">
  <strong>Copyright © 2025-2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
