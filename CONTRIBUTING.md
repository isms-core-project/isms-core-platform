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
</table>

---

### 📋 IMP QA Criteria (v3.2+)

| Requirement | Description |
|-------------|-------------|
| ✅ Control quotes | Use "should" (not "shall") per ISO 27001:2022 Annex A |
| ✅ British spelling | organisation, authorised, standardised |
| ✅ Document structure | PART I (User Guide) + PART II (Technical Specification) |
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
│   └── 10_pol-md/
├── IMP/                      # 📋 Implementation guides
│   └── 30_imp-md/
├── SCR/                      # 🐍 Scripts & workbooks
│   ├── 10_generator-master/  # Python generators
│   ├── 11_normalize/         # Normalization scripts
│   ├── 12_consolidator/      # Dashboard consolidation
│   ├── 13_presentation/      # CISO demo data
│   ├── 50_sanity/            # Validation scripts
│   └── 90_workbooks/         # Excel output
├── REF/                      # 📚 Reference materials (if applicable)
│   └── 70_ref-md/
└── CTX/                      # 🏢 Context documents (if applicable)
    └── 80_ctx-md/
```

---

## 🎬 Presentation Mode (13_presentation)

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
<td><strong>Claude AI</strong></td>
<td>Policy framework, Python automation, documentation</td>
</tr>
<tr>
<td><strong>Claude Code</strong></td>
<td>Script QA, pattern analysis, formula verification</td>
</tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/IP_Ownership-Gregory_Griffin-FFD700?style=flat-square" alt="IP Ownership"/>
</p>

---

<p align="center">
  <strong>Copyright © 2025-2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
