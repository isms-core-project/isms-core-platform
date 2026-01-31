# ISMS CORE

**Control-Oriented Real-world Engineering for ISO 27001:2022**

A production-grade compliance management platform that treats ISMS implementation as an engineering problem, not a consulting exercise.

---

## What is ISMS CORE?

ISMS CORE automates ISO 27001:2022 compliance through:

- **Policy Framework** (POL) - Control requirements and governance
- **Implementation Guides** (IMP) - Technical procedures and assessments
- **Python Automation** (SCR) - Excel workbook generators for evidence collection
- **Reference Materials** (REF) - Standards mapping and technical references
- **Context Documents** (CTX) - Organizational context and landscape analysis

### Architecture

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

## Repository Structure

```
isms-core/
├── 10-isms-scr-base/    # Python generator scripts
├── 30-isms-imp-base/    # Implementation guides
├── 40-isms-ref-base/    # Reference materials
├── 50-isms-ctx-base/    # Context documents
├── 70-isms-pol-base/    # Policy documents
├── PHILOSOPHY.md        # Anti-cargo-cult methodology
├── CONTRIBUTING.md      # QA process and standards
└── STATUS.md            # Current implementation progress
```

---

## Quick Start

Controls are organized by document type across bases:

```
70-isms-pol-base/isms-a.X.X-control/10_pol-md/      # Policies
30-isms-imp-base/isms-a.X.X-control/30_imp-md/      # Implementation guides
10-isms-scr-base/isms-a.X.X-control/
├── 10_generator-master/   # Python generators
└── 90_workbooks/          # Generated Excel output
```

Generate a workbook:
```bash
cd 10-isms-scr-base/isms-a.8.24-use-of-cryptography/10_generator-master
python3 generate_a824_1_data_transmission_assessment.py
```

---

## Framework Integration

- ISO/IEC 27001:2022 (complete Annex A mapping)
- ISO/IEC 27002:2022 (implementation guidance)
- NIST Cybersecurity Framework 2.0
- NIST SP 800-53 Rev 5
- MITRE ATT&CK (Enterprise, ICS, Mobile)
- Swiss nDSG, FINMA
- EU GDPR, DORA, NIS2

---

## License

**Dual-licensed:**

- **AGPL 3.0** - Open source use ([LICENSE](LICENSE))
- **Commercial** - Proprietary use without AGPL obligations

For commercial licensing: admin@gregorygriffin.org

---

## Contact

**Gregory Griffin**

- Email: admin@gregorygriffin.org
- GitHub: https://github.com/ggriffinorg
- LinkedIn: https://www.linkedin.com/in/ggriffinorg/

---

## Documentation

- [PHILOSOPHY.md](PHILOSOPHY.md) - Anti-cargo-cult methodology and the Feynman principle
- [CONTRIBUTING.md](CONTRIBUTING.md) - QA process, quality standards, development guidelines
- [STATUS.md](STATUS.md) - Current implementation progress and metrics

---

**Copyright © 2025-2026 Gregory Griffin. All rights reserved.**
