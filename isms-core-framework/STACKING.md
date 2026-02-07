<h1 align="center">🎋 Control Stacking Approaches</h1>

<p align="center">
  <strong>ISO/IEC 27001:2022 Annex A Control Grouping Patterns</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square" alt="ISO 27001:2022"/>
  <img src="https://img.shields.io/badge/NIST_CSF-2.0-FF6600?style=flat-square" alt="NIST CSF 2.0"/>
  <img src="https://img.shields.io/badge/93_Annex_A_Controls-53_Control_Packs-32CD32?style=flat-square" alt="93 to 53"/>
</p>

---

## Why Group Controls?

<p align="center">
<img src="https://img.shields.io/badge/Industry_Practice-20--25_Policies-9400D3?style=for-the-badge" alt="Industry Practice"/>
</p>

Organizations commonly implement multiple Annex A controls through a single policy and supporting procedures, **as long as** responsibilities, evidence, and effectiveness can still be demonstrated.

In practice, many ISMS programmes maintain ~20–25 top-level policy documents, with procedures, standards, and technical evidence underneath.

---

## Why 53 Packs, Not 93 Folders?

Most ISMS implementations create one folder per Annex A control — 93 separate structures with massive duplication. Authentication guidance repeated in A.5.17, A.8.2, A.8.3, and A.8.5. Access control policies scattered across A.5.15, A.5.16, and A.5.18.

ISMS CORE applies the **DRY principle** (Don't Repeat Yourself) to compliance:

| Approach | Controls | Duplication | Maintenance |
|----------|----------|-------------|-------------|
| 93 separate folders | 93 | High — same guidance repeated across related controls | Change one → must update 3-5 others |
| **53 domain packs** | 93 (grouped) | **None** — shared resources, single source of truth | Change one → all related controls update |

Every pack maintains **full audit traceability** back to individual Annex A controls via [COVERAGE.md](COVERAGE.md). An auditor can trace any of the 93 controls to its primary pack and supporting packs.

### Implementation Priority: SSE Scoring

Controls were built in order of **SSE (Structured Security Engineering) score**, prioritizing high-automation controls first:

| SSE Score | Characteristics | Examples | Build Order |
|:---------:|-----------------|----------|:-----------:|
| **5** | Technical, inventory-based, highly automatable | A.8.24 Cryptography, A.8.8 Vulnerability Mgmt | First |
| **4** | Technical with organizational overlap | A.8.15 Logging, A.8.9 Configuration Mgmt | Second |
| **3** | Mixed technical and organizational | A.5.24-28 Incident Mgmt, A.5.29 Disruption | Third |
| **2** | Primarily organizational, some automation | A.5.7 Threat Intel, A.6.3 Awareness | Fourth |
| **1** | Governance, legal, largely manual | A.5.31 Legal Requirements, A.5.35-36 Compliance | Last |

This strategy means the hardest, most technically complex controls were built and validated first, creating a strong foundation for the simpler governance controls to layer on top.

---

## Our Approach: Domain-Based Stacking

<p>
<img src="https://img.shields.io/badge/Current-Domain_Based-00AA00?style=flat-square" alt="Domain Based"/>
<img src="https://img.shields.io/badge/53_Control_Packs-Active-0066CC?style=flat-square" alt="53 Packs"/>
</p>

ISMS CORE groups controls into **control packs** by functional similarity, while still tracking coverage against the full set of **93 Annex A controls**.

| Pack (example) | Annex A controls covered | Domain |
|---|---|---|
| Secure employment & roles | A.5.1, A.5.2, A.6.1, A.6.2 | HR security & roles |
| Identity & access management | A.5.15, A.5.16, A.5.18 | Identity & access |
| Cloud & suppliers | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 | Cloud & suppliers |
| Incident management lifecycle | A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 | Incident management |
| Endpoint security | A.8.1, A.8.7, A.8.18, A.8.19 | Endpoint security |
| Network security | A.8.20, A.8.21, A.8.22 | Network security |

<p>
<img src="https://img.shields.io/badge/✓-ISO_Audit_Friendly-00AA00?style=flat-square" alt="Audit Friendly"/>
<img src="https://img.shields.io/badge/✓-Operationally_Practical-00AA00?style=flat-square" alt="Practical"/>
<img src="https://img.shields.io/badge/✓-Granular_Tracking-00AA00?style=flat-square" alt="Granular"/>
</p>

---

## Alternative View: NIST CSF 2.0 Alignment

<p>
<img src="https://img.shields.io/badge/View-NIST_CSF_2.0-FF6600?style=flat-square" alt="NIST CSF"/>
<img src="https://img.shields.io/badge/6_Functions-Lifecycle-0066CC?style=flat-square" alt="6 Functions"/>
</p>

NIST CSF 2.0 groups cybersecurity outcomes by lifecycle function. ISMS CORE can present the same implementation content through a CSF lens for reporting and customer alignment.

| CSF Function | Code | Example ISO/IEC 27001 Annex A controls (not exhaustive) | Purpose |
|----------|------|-------------------|---------|
| GOVERN | GV | A.5.1–A.5.4, A.5.31, A.5.35–A.5.36 | Strategy & governance |
| IDENTIFY | ID | A.5.7–A.5.13 | Asset awareness & preparation |
| PROTECT | PR | A.5.15–A.5.18, A.6.x, A.7.x, A.8.1–A.8.12, A.8.24–A.8.32 | Safeguards |
| DETECT | DE | A.8.8, A.8.15–A.8.17 | Monitoring & detection |
| RESPOND | RS | A.5.24–A.5.28, A.6.8 | Incident response |
| RECOVER | RC | A.5.29–A.5.30, A.8.13–A.8.14 | Continuity & recovery |

---

## Framework Overlap (Important Note)

ISO/IEC 27001 and NIST CSF overlap significantly, but "coverage" depends on **scope**, **depth**, and the **mapping method** used. ISMS CORE uses NIST OLIR informative references where available and maintains internal mappings where needed.

---

## Comparison

| Aspect | Domain-Based Packs | NIST CSF View |
|---|:---:|:---:|
| Groups | ~53 | 6 functions |
| Logic | Functional | Lifecycle/outcomes |
| Typical use | Implementation + audit execution | Reporting + customer alignment |
| Granularity | Fine | Coarse |

---

## Recommendation

<table>
<tr>
<th>Approach</th>
<th>Use Case</th>
<th>Status</th>
</tr>
<tr>
<td><strong>Domain-Based Packs</strong></td>
<td>Primary implementation structure</td>
<td><img src="https://img.shields.io/badge/Active-00AA00?style=flat-square" alt="Active"/></td>
</tr>
<tr>
<td><strong>NIST CSF View</strong></td>
<td>US clients, exec dashboards, customer questionnaires</td>
<td><img src="https://img.shields.io/badge/Available-0066CC?style=flat-square" alt="Available"/></td>
</tr>
</table>

Both views can be generated from the same implementations via **Statement of Applicability (SoA)** mapping.

---

## References

- NIST OLIR / Informative References Catalog (ISO 27001 ↔ CSF mappings, where available): https://csrc.nist.gov/projects/olir
- ISO/IEC 27001:2022 (ISO): https://www.iso.org/standard/27001

---

<p align="center">
  <strong>ISMS CORE Framework v1.0</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
