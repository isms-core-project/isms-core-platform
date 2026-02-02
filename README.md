<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Control_Oriented_Real_World_Engineering-2E8B57?style=for-the-badge" alt="ISMS CORE"/>
</p>

<h1 align="center">🎋 ISMS CORE</h1>

<p align="center">
  <strong>Control-Oriented Real-world Engineering for ISO 27001:2022</strong>
</p>

<p align="center">
  <a href="https://www.iso.org/standard/27001"><img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square&logo=iso&logoColor=white" alt="ISO 27001:2022"/></a>
  <a href="#-status"><img src="https://img.shields.io/badge/Progress-83%25-32CD32?style=flat-square" alt="Progress"/></a>
  <a href="#-status"><img src="https://img.shields.io/badge/Section_8-100%25_Complete-00AA00?style=flat-square" alt="Section 8"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL_3.0-9400D3?style=flat-square" alt="License"/></a>
</p>

<p align="center">
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/NIST_CSF-2.0-FF6600?style=flat-square" alt="NIST CSF"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/MITRE_ATT&CK-v18-DC143C?style=flat-square" alt="MITRE ATT&CK"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/GDPR-Compliant-FFD700?style=flat-square" alt="GDPR"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/Swiss_nDSG-Ready-FF0000?style=flat-square" alt="Swiss nDSG"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/EU_AI_Act-Mapped-0066CC?style=flat-square" alt="EU AI Act"/></a>
</p>

<p align="center">
  <em>Grows fast. Bends, doesn't break. Built to last.</em> 🎋
</p>

---

## 🎯 What is ISMS CORE?

A production-grade compliance management platform that treats ISMS implementation as an **engineering problem**, not a consulting exercise.

<table>
<tr>
<td align="center"><strong>📜 POL</strong><br/>Policy</td>
<td align="center"><strong>📋 IMP</strong><br/>Implementation</td>
<td align="center"><strong>🐍 SCR</strong><br/>Scripts</td>
<td align="center"><strong>📚 REF</strong><br/>Reference</td>
<td align="center"><strong>🏢 CTX</strong><br/>Context</td>
</tr>
<tr>
<td>Control requirements<br/>and governance</td>
<td>Technical procedures<br/>and assessments</td>
<td>Python workbook<br/>generators</td>
<td>Standards mapping<br/>and references</td>
<td>Organizational<br/>context</td>
</tr>
</table>

### 🏗️ Architecture

```
POL (Policy)         → Requirements and accountability
       ↓
IMP (Implementation) → Verification procedures and assessment guides
       ↓
SCR (Scripts)        → Assessment workbook generators
       ↓
Workbook (Output)    → Evidence and compliance metrics
```

---

## 📂 Repository Structure

```
isms-core-platform/
├── A.5-organizational-controls/     # 17 control groups
│   ├── isms-a.5.7-threat-intelligence/
│   │   ├── POL/    ├── IMP/    ├── SCR/    └── REF/
│   └── ...
├── A.6-people-controls/             # 3 control groups
├── A.7-physical-controls/           # 6 control groups
├── A.8-technological-controls/      # 23 control groups
├── CONTROLS.md                      # 📋 Control index (start here!)
├── STATUS.md                        # 📊 Current implementation progress
├── STACKING.md                      # 🔗 Control grouping approaches
├── PHILOSOPHY.md                    # ✈️ Anti-cargo-cult methodology
└── CONTRIBUTING.md                  # 🔧 QA process and standards
```

Controls are organized by ISO 27001:2022 Annex A section.

---

## 🚀 Quick Start

**Browse controls:** Start with [CONTROLS.md](CONTROLS.md) for a complete index.

Each control folder contains everything you need:

```
A.8-technological-controls/
└── isms-a.8.24-use-of-cryptography/
    ├── POL/10_pol-md/         # 📜 Policy documents
    ├── IMP/30_imp-md/         # 📋 Implementation guides
    └── SCR/                   # 🐍 Scripts & workbooks
        ├── 10_generator-master/
        ├── 13_presentation/
        └── 90_workbooks/
```

Generate a workbook:
```bash
cd A.8-technological-controls/isms-a.8.24-use-of-cryptography/SCR/10_generator-master
python3 generate_a824_1_data_transmission_assessment.py
```

---

## 🔗 Framework Integration

<table>
<tr>
<th>Framework</th>
<th>Coverage</th>
<th>Badge</th>
</tr>
<tr>
<td>ISO/IEC 27001:2022</td>
<td>Complete Annex A mapping</td>
<td><img src="https://img.shields.io/badge/Complete-0066CC?style=flat-square" alt="Complete"/></td>
</tr>
<tr>
<td>ISO/IEC 27002:2022</td>
<td>Implementation guidance</td>
<td><img src="https://img.shields.io/badge/Complete-0066CC?style=flat-square" alt="Complete"/></td>
</tr>
<tr>
<td>NIST CSF 2.0</td>
<td>Control mapping</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>NIST SP 800-53 Rev 5</td>
<td>Security controls</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>MITRE ATT&CK</td>
<td>Enterprise, ICS, Mobile</td>
<td><img src="https://img.shields.io/badge/v18-DC143C?style=flat-square" alt="v18"/></td>
</tr>
<tr>
<td>Swiss nDSG, FINMA</td>
<td>Regulatory compliance</td>
<td><img src="https://img.shields.io/badge/Ready-FF0000?style=flat-square" alt="Ready"/></td>
</tr>
<tr>
<td>EU GDPR, DORA, NIS2</td>
<td>Data protection</td>
<td><img src="https://img.shields.io/badge/Compliant-FFD700?style=flat-square" alt="Compliant"/></td>
</tr>
<tr>
<td>EU AI Act</td>
<td>AI risk management</td>
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

*If attackers are the "planes," cargo cult ISMS won't stop them. Only real controls will.* ✈️

See [PHILOSOPHY.md](PHILOSOPHY.md) for the full methodology.

---

## 📊 Status

<table>
<tr>
<th>Metric</th>
<th>Value</th>
<th>Status</th>
</tr>
<tr>
<td>Control Groups Complete</td>
<td><strong>44 of 53</strong></td>
<td><img src="https://img.shields.io/badge/83%25-32CD32?style=flat-square" alt="83%"/></td>
</tr>
<tr>
<td>Section 8 (Technological)</td>
<td><strong>22 of 22</strong></td>
<td><img src="https://img.shields.io/badge/100%25_🎉-00AA00?style=flat-square" alt="100%"/></td>
</tr>
<tr>
<td>Python Scripts</td>
<td><strong>360+</strong></td>
<td><img src="https://img.shields.io/badge/Validated-0066CC?style=flat-square" alt="Validated"/></td>
</tr>
<tr>
<td>IMP Documents</td>
<td><strong>158+</strong></td>
<td><img src="https://img.shields.io/badge/QA_Complete-9400D3?style=flat-square" alt="QA Complete"/></td>
</tr>
</table>

See [STATUS.md](STATUS.md) for detailed progress.

---

## 📜 License

**Dual-licensed:**

| License | Use Case |
|---------|----------|
| ![AGPL](https://img.shields.io/badge/AGPL_3.0-Open_Source-9400D3?style=flat-square) | Open source use |
| ![Commercial](https://img.shields.io/badge/Commercial-Proprietary-FFD700?style=flat-square) | Without AGPL obligations |

For commercial licensing: admin@gregorygriffin.org

---

## 📞 Contact

<p align="center">
  <strong>Gregory Griffin</strong>
</p>

<p align="center">
  <a href="https://isms-core.com"><img src="https://img.shields.io/badge/🌐_isms--core.com-Coming_Soon-2E8B57?style=for-the-badge" alt="Website"/></a>
</p>

<p align="center">
  <a href="mailto:admin@gregorygriffin.org"><img src="https://img.shields.io/badge/Email-admin@gregorygriffin.org-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/ggriffinorg"><img src="https://img.shields.io/badge/GitHub-ggriffinorg-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://www.linkedin.com/in/ggriffinorg/"><img src="https://img.shields.io/badge/LinkedIn-ggriffinorg-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
</p>

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CONTROLS.md](CONTROLS.md) | 📋 **Start here!** Index of all 49 control implementations |
| [STATUS.md](STATUS.md) | 📊 Current implementation progress and metrics |
| [STACKING.md](STACKING.md) | 🔗 Control grouping approaches (Domain vs NIST CSF) |
| [PHILOSOPHY.md](PHILOSOPHY.md) | ✈️ Anti-cargo-cult methodology and the Feynman principle |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 🔧 QA process, quality standards, development guidelines |

---

<p align="center">
  <strong>Copyright © 2025-2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
