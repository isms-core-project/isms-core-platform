# Contributing to ISMS CORE

## QA Philosophy

Not all documents require the same level of standardization. ISMS CORE applies appropriate rigor based on what matters for reliability, maintainability, and correctness.

---

## Document Types and Quality Standards

### POL (Policy Documents)

| Attribute | Requirement |
|-----------|-------------|
| Consistency | High |
| Change Frequency | Low (stable foundation) |
| Review Process | Formal approval required |
| QA Gate | `<!-- QA_VERIFIED: YYYY-MM-DD -->` comment |

Policies are foundation documents. They must be stable, consistent, and formally approved.

### IMP (Implementation Guides)

| Attribute | Requirement |
|-----------|-------------|
| Consistency | Moderate |
| Change Frequency | Medium (living documents) |
| Review Process | Subject to ongoing refinement |
| QA Gate | Bamboo tag at end of file |

Implementation guides adapt to context. Variations are acceptable when they serve the control's purpose.

**IMP QA Criteria (v3.2+):**
- Control quotes use "should" (not "shall") per ISO 27001:2022 Annex A
- British spelling (organisation, authorised, standardised)
- Document structure: PART I (User Guide) + PART II (Technical Specification)
- Standard ending: `**END OF SPECIFICATION**` + separator + quote with em-dash (—)
- QA tag: `<!-- QA_VERIFIED: YYYY-MM-DD -->` after bamboo tag

### SCR (Python Scripts)

| Attribute | Requirement |
|-----------|-------------|
| Consistency | High |
| Change Frequency | Medium (bug fixes and improvements) |
| Review Process | Code review and testing |
| QA Gate | `QA_VERIFIED:` marker in file |

Code must be reliable, maintainable, and error-free. Systematic standards are enforced.

### REF (Reference Materials)

| Attribute | Requirement |
|-----------|-------------|
| Consistency | Moderate |
| Change Frequency | Low |
| Review Process | Technical accuracy review |
| QA Gate | Bamboo tag at end of file |

### CTX (Context Documents)

| Attribute | Requirement |
|-----------|-------------|
| Consistency | Moderate |
| Change Frequency | Low |
| Review Process | Accuracy verification |
| QA Gate | Bamboo tag at end of file |

---

## QA Gates

Content is promoted to the main repository only when QA gates pass:

```bash
# Check QA status
./promote_control.sh --status

# Dry-run promotion
./promote_control.sh --dry-run isms-a.8.24-use-of-cryptography

# Promote verified content
./promote_control.sh isms-a.8.24-use-of-cryptography
```

---

## Python Script Standards

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

Use `logger.info()` / `logger.error()`, not `print()`:

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

## Folder Structure

```
isms-a.X.X-control-name/
├── 10_generator-master/  # Python generators
├── 11_normalize/         # Normalization scripts
├── 12_consolidator/      # Dashboard consolidation scripts
├── 13_presentation/      # Sample data population (CISO demos)
├── 50_sanity/            # Validation scripts
└── 90_workbooks/         # Generated Excel output (excluded from git)
```

---

## Presentation Mode (13_presentation)

Populate scripts fill workbooks with realistic sample data for CISO presentations.

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
- `isms-a.8.23-web-filtering/13_presentation/` - 4 scripts, 250+ data points
- `isms-a.8.24-use-of-cryptography/13_presentation/` - 4 scripts, 350+ data points

---

## Online Research Requirement

**All IMP and SCR development MUST include online research** to verify:
- Current best practices for the control
- Alignment with NIST, CIS, MITRE ATT&CK frameworks
- Technical accuracy of implementation guidance
- Latest tool capabilities and integration patterns

Key frameworks to reference:
- ISO/IEC 27001:2022 & 27002:2022
- NIST CSF 2.0 & SP 800-53 Rev 5
- CIS Controls v8
- MITRE ATT&CK Enterprise

---

## The Engineering Principle

> *"Standardization is good. Over-standardization is cargo cult. Apply rigor where it matters."*

**Feynman would ask:** "Does this variation serve a purpose?"

- If YES → Document why and keep it
- If NO → Standardize
- If forcing uniformity breaks functionality → Don't force it

---

## AI-Assisted Development

ISMS CORE is developed through collaborative AI-assisted engineering:

- **Gregory Griffin** - Methodology, architecture, domain expertise, IP ownership
- **Claude AI** - Policy framework, Python automation, documentation
- **Claude Code** - Script QA, pattern analysis, formula verification

**IP Ownership:** All intellectual property belongs to Gregory Griffin.

---

*Where bamboo antennas actually work.*
