<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Framework-2E8B57?style=for-the-badge" alt="ISMS CORE Framework"/>
</p>

<h1 align="center">🎋 ISMS CORE Framework</h1>

<p align="center">
  <strong>Governance Policies — Full Engineering Product</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Control_Packs-53-0066CC?style=flat-square" alt="53 Control Packs"/>
  <img src="https://img.shields.io/badge/Annex_A_Controls-93-32CD32?style=flat-square" alt="93 Annex A Controls"/>
  <img src="https://img.shields.io/badge/IMP_Documents-504-9400D3?style=flat-square" alt="504 IMP Documents"/>
  <img src="https://img.shields.io/badge/Python_Scripts-454-3776AB?style=flat-square" alt="454 Scripts"/>
</p>

---

## What is ISMS CORE Framework?

ISMS CORE Framework is the **full engineering product** for building and operating an ISO/IEC 27001:2022-aligned ISMS. Each of the 53 control packs contains a complete six-layer control stack:

<table>
<tr>
<td align="center"><strong>📜 POL</strong><br/>Policy</td>
<td align="center"><strong>📋 IMP</strong><br/>Implementation<br/><em>(UG + TG)</em></td>
<td align="center"><strong>🐍 SCR</strong><br/>Scripts</td>
<td align="center"><strong>📊 WKBK</strong><br/>Workbooks</td>
<td align="center"><strong>📚 REF</strong><br/>Reference</td>
<td align="center"><strong>🏢 CTX</strong><br/>Context</td>
</tr>
<tr>
<td>Requirements<br/>and governance</td>
<td>User Guides (UG)<br/>+ Technical Specs (TG)</td>
<td>Python generators<br/>and automation</td>
<td>Generated Excel<br/>assessment workbooks</td>
<td>Mappings and notes<br/>to support implementation</td>
<td>Organisational<br/>assumptions & scope</td>
</tr>
</table>

**Target audience:** Security teams, consultants, and engineers who need structured, auditable control packs with automated evidence generation.

---

## Directory Structure

```
isms-core-framework/
├── A.0-regulatory-control/             # 1 regulatory framework pack
├── A.5-organizational-controls/        # 21 control packs (covers 37 Annex A controls)
│   └── isms-a.5.X-control-name/
│       ├── POL/10_pol-md/              # Governance policies
│       ├── IMP/30_imp-md/              # UG (User Guide) + TG (Technical Spec)
│       ├── SCR/10_generator-master/    # Python generators
│       ├── WKBK/90_workbooks/          # Generated Excel workbooks
│       ├── REF/70_ref-md/              # Reference materials
│       └── CTX/80_ctx-md/              # Context documents
├── A.6-people-controls/                # 4 control packs (covers 8 Annex A controls)
├── A.7-physical-controls/              # 6 control packs (covers 14 Annex A controls)
├── A.8-technological-controls/         # 22 control packs (covers 34 Annex A controls)
├── CONTROLS.md                         # Control pack index
├── COVERAGE.md                         # 93 Annex A → 53 pack mapping
├── STATUS.md                           # Implementation status
├── STACKING.md                         # Control grouping methodology
└── CHANGELOG.md                        # Version history
```

---

## Quick Start

1. Browse [CONTROLS.md](CONTROLS.md) for the control pack index
2. Navigate to a control folder (e.g., `A.8-technological-controls/isms-a.8.24-use-of-cryptography/`)
3. Read the **POL** for requirements, **IMP-UG** for completion guidance, **IMP-TG** for technical specs
4. Run generators to produce assessment workbooks:

```bash
cd A.8-technological-controls/isms-a.8.24-use-of-cryptography/SCR/10_generator-master
python3 generate_a824_1_data_transmission_assessment.py
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [CONTROLS.md](CONTROLS.md) | Control pack index with all 53 packs |
| [COVERAGE.md](COVERAGE.md) | Canonical mapping: 93 Annex A controls → 53 packs |
| [STATUS.md](STATUS.md) | Current progress and metrics |
| [STACKING.md](STACKING.md) | Control grouping approaches |
| [CHANGELOG.md](CHANGELOG.md) | Version history and release notes |

---

## Relationship to ISMS CORE Operational

ISMS CORE Framework is the **full engineering product**. For organisations that need a lighter approach, see [ISMS CORE Operational](../isms-core-operational/) — a single operational policy per control group, designed for SMEs.

| | Framework | Operational |
|---|---|---|
| **Audience** | Mature security teams | SMEs and startups |
| **Per control group** | GOV-POL + IMP (UG/TG) + SCR + WKBK + REF + CTX | OP-POL + SCR + WKBK |
| **Depth** | Full assessment workbooks with automated scoring | Compliance checklists with evidence tracking |
| **Effort** | Comprehensive implementation | Practical minimum for audit readiness |

---

<p align="center">
  <em>Part of <a href="../README.md">ISMS CORE Platform</a></em> 🎋
</p>
