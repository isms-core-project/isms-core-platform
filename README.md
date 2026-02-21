<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Platform-2E8B57?style=for-the-badge" alt="ISMS CORE Platform"/>
</p>

<h1 align="center">🎋 ISMS CORE Platform</h1>

<p align="center">
  <strong>Control-Oriented Real-world Engineering for ISO/IEC 27001:2022</strong>
</p>

<p align="center">
  <a href="https://www.iso.org/standard/27001"><img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square&logo=iso&logoColor=white" alt="ISO 27001:2022"/></a>
  <a href="isms-core-framework/STATUS.md"><img src="https://img.shields.io/badge/Control_Packs-53_of_53-00AA00?style=flat-square" alt="Control Packs"/></a>
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

ISMS CORE is a production-grade **control engineering** platform for building and operating an ISO/IEC 27001:2022-aligned ISMS. It treats ISMS implementation as an **engineering problem** — not a consulting exercise.

The platform provides **two products** at different levels of depth:

<table>
<tr>
<th></th>
<th>🏗️ <a href="isms-core-framework/">ISMS CORE Framework</a></th>
<th>⚡ <a href="isms-core-operational/">ISMS CORE Operational</a></th>
</tr>
<tr>
<td><strong>What</strong></td>
<td>Full engineering product — governance policies with implementation guides, assessment scripts, and generated workbooks</td>
<td>Lightweight SME product — operational policies with compliance checklists per control group</td>
</tr>
<tr>
<td><strong>For</strong></td>
<td>Mature security teams, consultants, auditors</td>
<td>SMEs and startups</td>
</tr>
<tr>
<td><strong>Per control</strong></td>
<td>POL + IMP (UG/TG) + SCR + WKBK + REF + FORM + INS + CTX</td>
<td>OP-POL + SCR + WKBK</td>
</tr>
<tr>
<td><strong>Coverage</strong></td>
<td>53 control packs / 93 Annex A controls</td>
<td>53 control groups / 93 Annex A controls</td>
</tr>
<tr>
<td><strong>Artifacts</strong></td>
<td>504 IMP docs, 454 Python scripts, Excel workbooks</td>
<td>53 operational policies, compliance checklist scripts and workbooks</td>
</tr>
</table>

Both products cover **all 93 ISO 27001:2022 Annex A controls** organised into the same 53 control groups.

### 🧭 Who this is for (and not for)

**This is for:**
- Security teams building an ISMS and wanting **repeatable evidence**
- Engineers who prefer **automation + tests** over "security theater"
- SMEs that need **practical, audit-ready policies** without over-engineering
- Consultants/auditors who need **structured control packs**

**This is not for:**
- "One-click compliance" expectations
- Legal interpretations of GDPR/DORA/NIS2 (use counsel)
- Running scripts you haven't reviewed (treat this like code)

---

## 📂 Repository Structure

```
isms-core-platform/
├── README.md                           # This file
├── CONTRIBUTING.md                     # QA process and standards
├── PHILOSOPHY.md                       # Anti-cargo-cult methodology
├── CODE_OF_CONDUCT.md                  # Community standards
├── SECURITY.md                         # Vulnerability reporting
├── LICENSE                             # AGPL-3.0
├── COPYRIGHT
│
├── isms-core-framework/                # 🏗️ Full Engineering Product
│   ├── README.md                       # Framework overview
│   ├── CONTROLS.md                     # 53 control pack index
│   ├── COVERAGE.md                     # 93 Annex A → 53 pack mapping
│   ├── STATUS.md                       # Implementation metrics
│   ├── STACKING.md                     # Control grouping methodology
│   ├── CHANGELOG.md                    # Version history
│   ├── 00-foundation-policies/         # Regulatory framework
│   ├── A.5-organizational-controls/    # 21 control packs
│   ├── A.6-people-controls/            # 4 control packs
│   ├── A.7-physical-controls/          # 6 control packs
│   └── A.8-technological-controls/     # 22 control packs
│
└── isms-core-operational/              # ⚡ Lightweight SME Product
    ├── README.md                       # Operational overview
    ├── CONTROLS.md                     # 53 control group index
    ├── STATUS.md                       # Implementation metrics
    ├── CHANGELOG.md                    # Version history
    ├── OP-POL-AUDIT-LOG.md             # Per-policy review log
    ├── 00-checklist-engine/            # Shared checklist generator engine
    │   └── op_checklist_engine.py      # Common engine (642 lines)
    ├── A.5-organizational-controls/    # 21 control groups
    │   └── isms-a.X.X-control-name/
    │       ├── POL/                    # Operational policy (1 OP-POL)
    │       ├── SCR/                    # Checklist generator script
    │       └── WKBK/                   # Generated Excel checklist
    ├── A.6-people-controls/            # 4 control groups
    ├── A.7-physical-controls/          # 6 control groups
    └── A.8-technological-controls/     # 22 control groups
```

---

## 🚀 Quick Start

### Framework (full engineering product)

1. Browse [isms-core-framework/CONTROLS.md](isms-core-framework/CONTROLS.md) for the control pack index
2. Navigate to a control folder and read POL → IMP-UG → IMP-TG
3. Run generators to produce assessment workbooks:

```bash
cd isms-core-framework/A.8-technological-controls/isms-a.8.24-use-of-cryptography/SCR
python3 generate_a824_1_data_transmission_assessment.py
```

**Prerequisites:** Python 3.11+, `pip install openpyxl`

### Operational (lightweight SME product)

1. Browse [isms-core-operational/CONTROLS.md](isms-core-operational/CONTROLS.md) for the control pack index
2. Navigate to a control folder and read POL
3. Generate the compliance checklist and work through each requirement
4. Record status, evidence, and owners — that's your audit evidence

---

## 🔗 Framework Integration

Both products provide mappings to support multiple frameworks:

<table>
<tr>
<th>Framework</th>
<th>What ISMS CORE provides</th>
<th>Status</th>
</tr>
<tr>
<td>ISO/IEC 27001:2022</td>
<td>Annex A control packs (policy + implementation + assessment)</td>
<td><img src="https://img.shields.io/badge/Mapped-0066CC?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>ISO/IEC 27002:2022</td>
<td>Implementation-oriented guidance</td>
<td><img src="https://img.shields.io/badge/Coverage-0066CC?style=flat-square" alt="Coverage"/></td>
</tr>
<tr>
<td>NIST CSF 2.0</td>
<td>Control mapping and grouping options</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>NIST SP 800-53 Rev. 5</td>
<td>Security control mapping</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>MITRE ATT&CK</td>
<td>Threat technique mapping (Enterprise / ICS / Mobile)</td>
<td><img src="https://img.shields.io/badge/v18-Mapped-DC143C?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>GDPR / Swiss nDSG</td>
<td>Security/privacy control mapping and operational checklists</td>
<td><img src="https://img.shields.io/badge/Toolkit-FFD700?style=flat-square" alt="Toolkit"/></td>
</tr>
<tr>
<td>DORA / NIS2</td>
<td>Operational resilience mapping</td>
<td><img src="https://img.shields.io/badge/Mapped-FFD700?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>EU AI Act</td>
<td>AI risk management mapping</td>
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
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────────┐
│  Claude Code     │────▶│  ISMS Copilot X  │────▶│  GPT-5.x Red Team    │
│  (Build + QA)    │     │ (Blue Team Audit)│     │  (Attack Surface)    │
└──────────────────┘     └──────────────────┘     └──────────────────────┘
         │                        │                         │
         ▼                        ▼                         ▼
   Implementation           Stage 1: Docs             Stage 2: Gaps
   + Code Review            adequacy review            + adversarial test
                                  │                         │
                                  └────────────┬────────────┘
                                               ▼
                                  ┌──────────────────────┐
                                  │   Gregory Griffin    │
                                  │   (Final Approval)   │
                                  └──────────────────────┘
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed QA standards.

---

## 📊 Status

| Metric | Value | Status |
|--------|-------|--------|
| Framework control packs | **53 of 53** | ![100%](https://img.shields.io/badge/100%25-00AA00?style=flat-square) |
| Operational policies | **53 of 53** | ![100%](https://img.shields.io/badge/100%25-00AA00?style=flat-square) |
| Annex A controls mapped | **93 of 93** | ![Mapped](https://img.shields.io/badge/Mapped-32CD32?style=flat-square) |
| Python scripts (Framework) | **454** (410K+ lines) | ![Validated](https://img.shields.io/badge/Validated-0066CC?style=flat-square) |
| IMP documents (Framework) | **504** (252 UG + 252 TG) | ![Split](https://img.shields.io/badge/UG%2FTG-9400D3?style=flat-square) |

See [isms-core-framework/STATUS.md](isms-core-framework/STATUS.md) for detailed Framework metrics.

---

## 🔒 Security

- **Vulnerability reporting:** Please report security issues to **info@isms-core.com** (include "ISMS CORE Security" in the subject).
- **Safe usage:** Review scripts before execution. Run in a virtual environment. Treat generated artifacts as sensitive until proven otherwise.
- **No secrets:** Do not commit credentials, tokens, private keys, or customer data to this repo or to generated workbooks.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [isms-core-framework/CONTROLS.md](isms-core-framework/CONTROLS.md) | 📋 Control pack index (Framework) |
| [isms-core-framework/COVERAGE.md](isms-core-framework/COVERAGE.md) | 🗺️ 93 Annex A → 53 pack mapping |
| [isms-core-framework/STATUS.md](isms-core-framework/STATUS.md) | 📊 Framework metrics |
| [isms-core-framework/STACKING.md](isms-core-framework/STACKING.md) | 🔗 Control grouping approaches |
| [isms-core-operational/CONTROLS.md](isms-core-operational/CONTROLS.md) | 📋 Control group index (Operational) |
| [isms-core-operational/STATUS.md](isms-core-operational/STATUS.md) | 📊 Operational metrics |
| [PHILOSOPHY.md](PHILOSOPHY.md) | ✈️ Anti-cargo-cult methodology |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 🔧 QA process and standards |
| [SECURITY.md](SECURITY.md) | 🔒 Vulnerability reporting policy |
| [isms-core-framework/CHANGELOG.md](isms-core-framework/CHANGELOG.md) | 📝 Version history |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 🤝 Community standards |

---

## 📜 License

**Dual-licensed:**
- **AGPL-3.0** for open-source use (see [LICENSE](LICENSE))
- **Commercial license** available for organizations that cannot (or do not want to) comply with AGPL obligations

Commercial licensing: **info@isms-core.com**

---

## 📞 Contact

<p align="center">
  <strong>The ISMS Core Project</strong>
</p>

<p align="center">
  <a href="mailto:info@isms-core.com"><img src="https://img.shields.io/badge/Email-infor@isms--core.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/isms-core-project"><img src="https://img.shields.io/badge/GitHub-isms--core--project-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://www.linkedin.com/in/ggriffinorg/"><img src="https://img.shields.io/badge/LinkedIn-ggriffinorg-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
</p>

---

<p align="center">
  <strong>Copyright © 2025–2026 Gregory Griffin. All rights reserved.</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>