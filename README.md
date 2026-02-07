<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Control_Oriented_Real_World_Engineering-2E8B57?style=for-the-badge" alt="ISMS CORE"/>
</p>

<h1 align="center">🎋 ISMS CORE</h1>

<p align="center">
  <strong>Control-Oriented Real-world Engineering for ISO/IEC 27001:2022</strong>
</p>

<p align="center">
  <a href="https://www.iso.org/standard/27001"><img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square&logo=iso&logoColor=white" alt="ISO 27001:2022"/></a>
  <a href="#-status"><img src="https://img.shields.io/badge/Progress-100%25-00AA00?style=flat-square" alt="Progress"/></a>
  <a href="#-status"><img src="https://img.shields.io/badge/Control_Packs-53_of_53-00AA00?style=flat-square" alt="Control Packs"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL_3.0-9400D3?style=flat-square" alt="License"/></a>
</p>

<p align="center">
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/NIST_CSF_2.0-Mapped-FF6600?style=flat-square" alt="NIST CSF"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/MITRE_ATT&CK_v18-Mapped-DC143C?style=flat-square" alt="MITRE ATT&CK"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/GDPR-Mapped-FFD700?style=flat-square" alt="GDPR"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/Swiss_nDSG-Toolkit-FF0000?style=flat-square" alt="Swiss nDSG"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/EU_AI_Act-Mapped-0066CC?style=flat-square" alt="EU AI Act"/></a>
</p>

<p align="center">
  <em>Grows fast. Bends, doesn't break. Built to last.</em> 🎋
</p>

---

## 🎯 What is ISMS CORE?

ISMS CORE is a production-grade **control engineering** repository for building and operating an ISO/IEC 27001:2022-aligned ISMS. It treats ISMS implementation as an **engineering problem** — not a consulting exercise.

It is organized into a consistent control "stack":

<table>
<tr>
<td align="center"><strong>📜 POL</strong><br/>Policy</td>
<td align="center"><strong>📋 IMP</strong><br/>Implementation<br/><em>(UG + TG)</em></td>
<td align="center"><strong>🐍 SCR</strong><br/>Scripts</td>
<td align="center"><strong>📚 REF</strong><br/>Reference</td>
<td align="center"><strong>🏢 CTX</strong><br/>Context</td>
<td align="center"><strong>📝 FORM</strong><br/>Forms</td>
</tr>
<tr>
<td>Requirements<br/>and governance</td>
<td>User Guides (UG)<br/>+ Technical Specs (TG)</td>
<td>Python generators<br/>and automation</td>
<td>Mappings and notes<br/>to support implementation</td>
<td>Organizational<br/>assumptions & scope context</td>
<td>Templates, checklists<br/>and operational forms</td>
</tr>
</table>

### 🧭 Who this is for (and not for)

**This is for:**
- Security teams building an ISMS and wanting **repeatable evidence**
- Engineers who prefer **automation + tests** over "security theater"
- Consultants/auditors who need **structured control packs** (policy + implementation + assessment artifacts)

**This is not for:**
- "One-click compliance" expectations
- Legal interpretations of GDPR/DORA/NIS2 (use counsel)
- Running scripts you haven't reviewed (treat this like code)

---

## 🏗️ Architecture

```
POL (Policy)         → Requirements and accountability
       ↓
IMP (Implementation) → User Guides (UG) + Technical Specifications (TG)
       ↓
SCR (Scripts)        → Assessment workbook generators
       ↓
WKBK (Workbooks)     → Evidence and compliance metrics
```

---

## 📂 Repository Structure

```
isms-core-platform/
├── A.5-organizational-controls/     # 21 control packs (covers 37 Annex A controls)
│   ├── isms-a.5.7-threat-intelligence/
│   │   ├── POL/    ├── IMP/    ├── SCR/    ├── WKBK/    └── REF/    └── FORM/
│   └── ...
├── A.6-people-controls/             # 4 control packs (covers 8 Annex A controls)
├── A.7-physical-controls/           # 6 control packs (covers 14 Annex A controls)
├── A.8-technological-controls/      # 22 control packs (covers 34 Annex A controls)
├── CONTROLS.md
├── COVERAGE.md
├── STATUS.md
├── STACKING.md
├── PHILOSOPHY.md
└── CONTRIBUTING.md
```

Controls are organized by ISO/IEC 27001:2022 Annex A section (A.5–A.8).

---

## 🚀 Quick Start

### 1) Browse controls
Start with [CONTROLS.md](CONTROLS.md) for the index and navigate to a control folder.

Each control folder contains everything needed:

```
A.8-technological-controls/
└── isms-a.8.24-use-of-cryptography/
    ├── POL/10_pol-md/
    ├── IMP/30_imp-md/
    ├── SCR/
    │   ├── 10_generator-master/
    │   └── 13_presentation/
    └── WKBK/
        └── 90_workbooks/
```

### 2) Understand IMP documents (UG / TG)

Each assessment has two companion documents in `IMP/30_imp-md/`:

| File | Type | Purpose |
|------|------|---------|
| `ISMS-IMP-A.X.X.N-UG - Title.md` | **User Guide** | How to complete the assessment — walkthrough, evidence, pitfalls |
| `ISMS-IMP-A.X.X.N-TG - Title.md` | **Technical Spec** | What the Excel workbook contains — sheets, columns, validations (auto-generated from Python) |

Start with the **UG** if you're completing an assessment. Refer to the **TG** if you're developing or modifying a generator script. See [CONTRIBUTING.md](CONTRIBUTING.md#-imp-document-structure-ug--tg) for full details.

### 3) Prerequisites
- Python 3.11+ recommended (3.10+ may work depending on dependencies)
- A virtual environment (`python -m venv .venv`)
- `pip install openpyxl` (primary dependency)

### 4) Generate a workbook (example)
```bash
cd A.8-technological-controls/isms-a.8.24-use-of-cryptography/SCR/10_generator-master
python3 generate_a824_1_data_transmission_assessment.py
```

**Tip:** Treat generated workbooks as potential evidence. Don't commit workbooks containing secrets, production identifiers, or personal data.

---

## 🔗 Framework Integration

This repo provides **mappings and implementation material** to support multiple frameworks. Your compliance outcome depends on how you implement, operate, and evidence controls in your own environment.

<table>
<tr>
<th>Framework</th>
<th>What ISMS CORE provides</th>
<th>Status</th>
</tr>
<tr>
<td>ISO/IEC 27001:2022</td>
<td>Annex A control packs (policy + implementation + assessment structure)</td>
<td><img src="https://img.shields.io/badge/Mapped-0066CC?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>ISO/IEC 27002:2022</td>
<td>Implementation-oriented guidance (original wording, not a copy of the standard)</td>
<td><img src="https://img.shields.io/badge/Coverage-0066CC?style=flat-square" alt="Coverage"/></td>
</tr>
<tr>
<td>NIST CSF 2.0</td>
<td>Control mapping and grouping options</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>NIST SP 800-53 Rev. 5</td>
<td>Security control mapping (where applicable)</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>MITRE ATT&CK</td>
<td>Threat technique mapping (Enterprise / ICS / Mobile as used)</td>
<td><img src="https://img.shields.io/badge/v18-Mapped-DC143C?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>GDPR / Swiss nDSG</td>
<td>Security/privacy control mapping and operational checklists</td>
<td><img src="https://img.shields.io/badge/Toolkit-FFD700?style=flat-square" alt="Toolkit"/></td>
</tr>
<tr>
<td>DORA / NIS2</td>
<td>Operational resilience mapping (risk mgmt, incident handling, continuity)</td>
<td><img src="https://img.shields.io/badge/Mapped-FFD700?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>EU AI Act</td>
<td>AI risk management mapping (where relevant)</td>
<td><img src="https://img.shields.io/badge/Mapped-0066CC?style=flat-square" alt="Mapped"/></td>
</tr>
</table>

---

## ✈️ Philosophy: Not Cargo Cult

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
> — Richard Feynman

ISMS CORE avoids **cargo-cult security** where formal structures exist without verifiable effectiveness:

| | Cargo Cult | ISMS CORE |
|---|---|---|
| ❌ | Impressive policies nobody reads | ✅ Controls that **actually work** |
| ❌ | Made-up compliance numbers | ✅ Evidence that **proves effectiveness** |
| ❌ | Security theater for audits | ✅ Metrics that **measure real security** |
| ❌ | PowerPoints instead of controls | ✅ Automation that **enforces compliance** |

See [PHILOSOPHY.md](PHILOSOPHY.md) for the full methodology.

---

## 🔬 Quality Assurance

Every control pack undergoes **adversarial multi-model validation** — controls are reviewed by competing AI models to ensure no single model's blind spots compromise quality.

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Claude Code     │────▶│  ISMS Copilot X   │────▶│  GPT-4 Red Team  │
│  (Build + QA)    │     │  (Blue Team Audit) │     │  (Attack Surface) │
└─────────────────┘     └──────────────────┘     └──────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
   Implementation          Stage 1: Docs            Stage 2: Gaps
   + Code Review           adequacy review          + adversarial test
                                  │                        │
                                  └──────────┬─────────────┘
                                             ▼
                                  ┌──────────────────┐
                                  │  Gregory Griffin   │
                                  │  (Final Approval)  │
                                  └──────────────────┘
```

<table>
<tr>
<th>Stage</th>
<th>Method</th>
<th>Focus</th>
</tr>
<tr>
<td><strong>Stage 1</strong></td>
<td>Documentation adequacy</td>
<td>Policy completeness, control coverage, artifact consistency</td>
</tr>
<tr>
<td><strong>Stage 2</strong></td>
<td>Implementation effectiveness</td>
<td>Gap analysis, evidence sufficiency, audit readiness</td>
</tr>
<tr>
<td><strong>Findings</strong></td>
<td>Classified: Critical / High / Medium / Low</td>
<td>Iterated until all Critical and High findings resolved</td>
</tr>
</table>

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed QA standards.

---

## 📊 Status

To avoid ambiguity, ISMS CORE tracks three different things:
- **Controls:** ISO/IEC 27001:2022 Annex A controls (93 total in A.5–A.8)
- **Control packs:** our implementation bundles (53 packs covering all 93 controls)
- **Artifacts:** POL/IMP/SCR per pack

<table>
<tr>
<th>Metric</th>
<th>Value</th>
<th>Status</th>
</tr>
<tr>
<td>Control packs complete</td>
<td><strong>53 of 53</strong></td>
<td><img src="https://img.shields.io/badge/100%25_🎉-00AA00?style=flat-square" alt="100%"/></td>
</tr>
<tr>
<td>Annex A controls mapped</td>
<td><strong>93 of 93</strong></td>
<td><img src="https://img.shields.io/badge/Mapped-32CD32?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>Python scripts</td>
<td><strong>454</strong> (410K+ lines)</td>
<td><img src="https://img.shields.io/badge/Validated-0066CC?style=flat-square" alt="Validated"/></td>
</tr>
<tr>
<td>IMP documents</td>
<td><strong>504</strong> (252 UG + 252 TG)</td>
<td><img src="https://img.shields.io/badge/UG%2FTG_Split-9400D3?style=flat-square" alt="UG/TG Split"/></td>
</tr>
</table>

See [STATUS.md](STATUS.md) for detailed progress.

---

## 🔒 Security

- **Vulnerability reporting:** Please report security issues to **admin@gregorygriffin.org** (include "ISMS CORE Security" in the subject).
- **Safe usage:** Review scripts before execution. Run in a virtual environment. Treat generated artifacts as sensitive until proven otherwise.
- **No secrets:** Do not commit credentials, tokens, private keys, or customer data to this repo or to generated workbooks.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CONTROLS.md](CONTROLS.md) | 📋 **Start here.** Index of control packs and implementations |
| [COVERAGE.md](COVERAGE.md) | 🗺️ Canonical mapping: 93 Annex A controls → 53 control packs |
| [STATUS.md](STATUS.md) | 📊 Current progress and metrics |
| [STACKING.md](STACKING.md) | 🔗 Control grouping approaches (e.g., Domain vs NIST CSF) |
| [PHILOSOPHY.md](PHILOSOPHY.md) | ✈️ Anti-cargo-cult methodology |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 🔧 QA process and standards |
| [SECURITY.md](SECURITY.md) | 🔒 Vulnerability reporting policy |
| [CHANGELOG.md](CHANGELOG.md) | 📝 Version history and release notes |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 🤝 Community standards |

---

## 📜 License

**Dual-licensed:**
- **AGPL-3.0** for open-source use (see [LICENSE](LICENSE))
- **Commercial license** available for organizations that cannot (or do not want to) comply with AGPL obligations

Commercial licensing: **admin@gregorygriffin.org**

---

## 📞 Contact

<p align="center">
  <strong>Gregory Griffin</strong>
</p>

<p align="center">
  <a href="mailto:admin@gregorygriffin.org"><img src="https://img.shields.io/badge/Email-admin@gregorygriffin.org-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/ggriffinorg"><img src="https://img.shields.io/badge/GitHub-ggriffinorg-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://www.linkedin.com/in/ggriffinorg/"><img src="https://img.shields.io/badge/LinkedIn-ggriffinorg-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
</p>

---

<p align="center">
  <strong>Copyright © 2025–2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
