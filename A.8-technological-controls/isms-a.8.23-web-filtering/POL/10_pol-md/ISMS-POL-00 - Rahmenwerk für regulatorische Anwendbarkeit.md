**ISMS-POL-00 — Rahmenwerk für regulatorische Anwendbarkeit**
**Autoritative Referenz für ISMS Compliance-Verpflichtungen**

---

**Dokumentenlenkung**

| Feld | Wert |
|------|------|
| **Dokumenten Titel** | Rahmenwerk für regulatorische Anwendbarkeit |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-00 |
| **Ersteller/in** | Chief Information Security Officer (CISO) |
| **Dokumenteneigentümer/in** | Chief Executive Officer (CEO) |
| **Freigabe durch** | Geschäftsleitung (GL) |
| **Erstellt** | [Date] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versions-Verzeichnis**:

| Version | Datum | Autor | Änderungsvermerk |
|---------|-------|-------|------------------|
| 1.0 | [Date] | CISO | Initiale Richtlinie für ISO 27001:2022 Erstzertifizierung |

**Review Cycle**: Jährlich (oder bei wesentlichen regulatorischen Änderungen)  
**Nächstes Review-Datum**: [Freigabedatum + 12 Monate]  
**Genehmiger**: 

- Chief Information Security Officer (CISO)
- Legal/Compliance Officer
- Data Protection Officer (DPO)
- Executive Management


**Verteilung**: Alle ISMS Stakeholder, Policy Authors, System Owners, Auditoren  
**Referenziert durch**: Alle ISMS Policy-Dokumente (obligatorische Referenz)

**Language Strategy**: Wo technische oder regulatorische Begriffe international etabliert sind (z.B. GDPR, ISO/IEC, NIST), wird die englische Terminologie beibehalten, um Präzision zu gewährleisten und grenzüberschreitende regulatorische Referenzierung zu erleichtern.

---

## Executive Summary

Dieses Dokument bietet die **autoritative Referenz** für die Interpretation der Anwendbarkeit von Regulations und Frameworks im gesamten Information Security Management System (ISMS).

**Zweck**: Beseitigung von Unklarheiten und Inkonsistenzen bei der Referenzierung von Regulations und Frameworks in ISMS Policies, Procedures und Controls.

**Geltungsbereich**: Alle Verweise auf Gesetze, Regulations, Standards und Frameworks innerhalb der ISMS-Dokumentation.

**Kernprinzip**: **Die Anwendbarkeit von Regulations muss explizit sein, nicht impliziert.** Verweise auf Regulations und Frameworks fallen in drei Kategorien:

1. **Mandatory Compliance** - Gesetzliche Verpflichtungen, die für die Organisation gelten
2. **Conditional Applicability** - Anforderungen, die nur unter bestimmten Umständen gelten
3. **Informational Reference** - Best Practices und technische Leitlinien

**Verwendung**: Alle ISMS Policies MÜSSEN Abschnitt 1.3 mit Verweis auf dieses Framework enthalten, oder einen "Regulatory Framework"-Abschnitt, der diese Kategorien direkt einbindet.

---

## Policy Authority und Abgrenzungen

### Zweck und Geltungsbereich dieser Policy

Diese Policy definiert die **Identifikation und Anwendbarkeit** von gesetzlichen, statutory, regulatorischen und vertraglichen Anforderungen für das Information Security Management System der Organisation.

**Diese Policy etabliert:**

- Welche Regulations und Standards für die Organisation gelten
- Kategorisierung regulatorischer Verpflichtungen (Mandatory, Conditional, Informational)
- Assessment-Methodik zur Bestimmung der Anwendbarkeit
- Review- und Update-Prozesse für Änderungen in der Regulatory Landscape


**Diese Policy etabliert NICHT:**

- Risk Treatment-Entscheidungen (adressiert in Clause 6 - Risk Management)
- Control Implementation-Anforderungen (adressiert in Annex A Controls)
- Compliance-Status oder Verification (adressiert in Compliance Monitoring Processes)


Das Ergebnis des Regulatory Applicability Assessment dient als **Input** für:

- Control Scoping-Entscheidungen innerhalb Annex A
- Risk Assessment und Treatment Priorisierung
- Proportionality-Entscheidungen für Control Implementation
- Audit Planning und Compliance Verification


**Abgrenzungsprinzip**: Diese Policy etabliert die Anwendbarkeit von Regulations. Implementation, Enforcement und Verification werden durch separate ISMS-Prozesse behandelt.

---

# Regulatory Applicability-Kategorien

## Kategoriedefinitionen

**Mandatory Compliance**  
Gesetzliche oder vertragliche Verpflichtungen, die die Organisation ERFÜLLEN MUSS. Nichteinhaltung führt zu rechtlicher Haftung, Regulatory Fines, Vertragsbruch oder Zertifizierungsverlust.

**Merkmale**:

- Durchsetzbar durch Gesetz oder Vertrag
- Nichteinhaltung hat rechtliche/finanzielle Konsequenzen
- Erfordert dokumentierte Compliance-Nachweise
- Unterliegt Regulatory Audits und Inspektionen


**Informational Reference / Best Practice Alignment**  
Frameworks und Standards, die für technische Leitlinien, Benchmarking oder freiwillige Ausrichtung verwendet werden. Diese informieren Security Practices, stellen aber keine mandatory Compliance-Anforderungen dar, es sei denn, sie sind explizit durch Vertrag oder Regulation gefordert.

**Merkmale**:

- Freiwillige Übernahme für Best Practices
- Kein rechtlicher Enforcement-Mechanismus
- Verwendung für technische Implementation Guidance
- Können mandatory werden, wenn in Verträgen referenziert


**Conditional Applicability**  
Anforderungen, die nur gelten, wenn bestimmte Bedingungen erfüllt sind (z.B. Branche, geografische Lage, Service-Art, Kundenverträge, Regulatory Scope).

**Merkmale**:

- Anwendbarkeit hängt vom organisatorischen Kontext ab
- Können mandatory werden basierend auf Geschäftsaktivitäten
- Erfordern periodisches Re-Assessment bei Business-Entwicklung
- Beispiele: PCI DSS (nur bei Kreditkartenverarbeitung), HIPAA (nur bei US-Healthcare-Daten)


**Klarstellung zur Tier-Klassifizierung**: Die Tier-Klassifizierung (Mandatory, Conditional, Informational) bestimmt die **regulatorische Bindungskraft** und impliziert nicht per se Implementation-Verpflichtungen. Implementation-Entscheidungen werden durch den Risk Assessment und Treatment Process getroffen, unter Berücksichtigung regulatorischer Anforderungen zusammen mit anderen Faktoren wie Risk Appetite, Business Context und technischer Machbarkeit.

## Compliance Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPLIANCE HIERARCHY                         │
├─────────────────────────────────────────────────────────────────┤
│  TIER 1: MANDATORY (Legal/Contractual)                         │
│  • Swiss Federal Data Protection Act (FADP)                     │
│  • EU GDPR (bei Verarbeitung von EU-Personendaten)             │
│  • ISO/IEC 27001:2022 (für Zertifizierung)                      │
│  • Branchenspezifische Regulations (je nach Anwendbarkeit)      │
│  • Kundenverträge (explizite Security-Anforderungen)            │
│                                                                 │
│  TIER 2: CONDITIONAL (Context-Dependent)                        │
│  • DORA (falls EU Financial Services Entity)                    │
│  • NIS2 (falls Essential/Important Entity in EU)                │
│  • PCI DSS (bei Kreditkartenverarbeitung)                       │
│  • HIPAA (bei US-Healthcare-Daten)                              │
│  • Branchen-Regulations (sektorabhängig)                        │
│                                                                 │
│  TIER 3: INFORMATIONAL (Best Practice)                          │
│  • NIST SP 800-series (Technical Guidance)                      │
│  • CIS Controls (Security Benchmarks)                           │
│  • OWASP (Application Security)                                 │
│  • Industry Frameworks (nur Referenz)                           │
└─────────────────────────────────────────────────────────────────┘
```

---

# Mandatory Compliance (Tier 1)

## Swiss Federal Data Protection Act (FADP/nDSG)

**Anwendbarkeit**: Alle Aktivitäten der Organisation mit Sitz in oder Service für die Schweiz

**Kernbestimmungen**:

- Artikel 8: Angemessene technische und organisatorische Massnahmen
- Artikel 19: Recht auf Auskunft (Betroffenenrechte)
- Artikel 6: Grundsätze (Rechtmässigkeit, Verhältnismässigkeit, Zweckbindung)
- Artikel 7: Datensicherheit (angemessene technische und organisatorische Massnahmen)
- Artikel 328b OR (Obligationenrecht): Mitarbeiterüberwachung und Persönlichkeitsschutz


**ISMS-Impact**:

- Data Protection by Design und by Default
- Technische Sicherheitsmassnahmen (Encryption, Access Control)
- Transparenz und Verhältnismässigkeit bei Mitarbeiterüberwachung
- Bearbeitungsverzeichnis (Art. 12)
- Data Breach Notification (Art. 24)


**Referenz**: Bundesgesetz über den Datenschutz (SR 235.1), in Kraft seit 1. September 2023

## EU General Data Protection Regulation (GDPR)

**Anwendbarkeit**: Bei Verarbeitung von Personendaten von EU-Bürgern

**Kernbestimmungen**:

- Article 5: Grundsätze der Verarbeitung (Rechtmässigkeit, Fairness, Transparenz, Zweckbindung)
- Article 6: Rechtsgrundlage für Verarbeitung
- Article 24: Verantwortlichkeiten des Controllers (Accountability)
- Article 25: Data Protection by Design und by Default
- Article 28: Processor-Verpflichtungen (Verträge, Security-Massnahmen)
- Article 32: Security of Processing (Encryption, Pseudonymization, Resilience)
- Article 33: Breach Notification (72 Stunden an Supervisory Authority)
- Article 35: Data Protection Impact Assessment (DPIA) für High-Risk Processing


**ISMS-Impact**:

- Technical and Organizational Measures (TOMs)
- Encryption und Pseudonymization
- Access Controls und Authentication
- Data Breach Response Procedures
- Vendor Management (Processor Agreements)
- Privacy Impact Assessments


**Referenz**: Regulation (EU) 2016/679, in Kraft seit 25. Mai 2018

## ISO/IEC 27001:2022

**Anwendbarkeit**: Wenn die Organisation eine ISO 27001-Zertifizierung anstrebt

**Kernbestimmungen**:

- Annex A Controls (93 Controls in den Bereichen Organizational, People, Physical, Technological)
- Clause 4: Context der Organisation
- Clause 5: Leadership und Commitment
- Clause 6: Risk Assessment und Treatment
- Clause 7: Support (Resources, Competence, Awareness, Communication, Documented Information)
- Clause 8: Operation (Risk Treatment, Assessment)
- Clause 9: Performance Evaluation (Monitoring, Internal Audit, Management Review)
- Clause 10: Improvement (Nonconformity, Corrective Action, Continual Improvement)


**ISMS-Impact**:

- Policy Framework Implementation
- Risk Management Methodology
- Control Implementation und Evidence
- Internal Audit Program
- Management Review Process
- Continual Improvement


**Referenz**: ISO/IEC 27001:2022 Information Security Management Systems

## Weitere Mandatory Regulations

Organisationen sollten zusätzliche mandatory Regulations basierend auf ihrem spezifischen Kontext dokumentieren:

| Regulation | Trigger | Beispiele |
|-----------|---------|----------|
| **Arbeitsrecht** | Mitarbeiter in der Jurisdiktion | Betriebsratsmitbestimmung (Deutschland), Mitarbeiterüberwachungsgesetze |
| **Finanzregulierungen** | Financial Services | FINMA (Schweiz), BaFin (Deutschland), MiFID II (EU) |
| **Telekommunikation** | Telecom Services | Lawful Interception, Data Retention |
| **Exportkontrolle** | Grenzüberschreitende Operationen | Dual-Use-Güter, Kryptografie-Export |
| **Vertragsrecht** | Kundenvereinbarungen | Explizite Security-Anforderungen in Service Contracts |

---

# Conditional Applicability (Tier 2)

Diese Regulations gelten **nur, wenn bestimmte Geschäftsbedingungen erfüllt sind**:

## Swiss Financial Market Supervisory Authority (FINMA)

**Regulation**: Eidgenössische Finanzmarktaufsicht  
**Primäre Rundschreiben**: 

- FINMA-Rundschreiben 2023/1 (Operationelle Risiken und Resilienz - Banken, in Kraft seit 1. Januar 2024)
- FINMA-Rundschreiben 2008/7 (Outsourcing - Banken)
- FINMA-Rundschreiben 2018/3 (Outsourcing - Versicherer)


**Anwendbarkeits-Trigger**:

- Organisation ist ein **Schweizer Finanzinstitut**, das von der FINMA reguliert wird:
  - Banken (Banklizenz der FINMA)
  - Effektenhändler (Effektenhändlerlizenz)
  - Versicherungsgesellschaften (Versicherungslizenz)
  - Finanzinfrastrukturanbieter (Börsen, zentrale Wertpapierverwahrstellen)
  - Kollektive Kapitalanlagen (Fondsverwaltungslizenzen)
  

**Kernbestimmungen**:

- **Operational Resilience**: ICT Risk Management, Business Continuity Planning, Disaster Recovery
- **Outsourcing**: Third-Party Risk Management, Due Diligence, Verträge, Exit-Strategien
- **Data Protection**: Kundendatensicherheit, Vertraulichkeit, Verfügbarkeit
- **Incident Reporting**: Wesentliche operationelle Incidents an FINMA
- **Internal Controls**: Governance, Risk Management, Internal Audit


**ISMS-Impact**:

- Erweiterte Business Continuity und Disaster Recovery Controls
- Umfassendes Third-Party Risk Management (A.5.19-23)
- Incident Response und Reporting Procedures (A.5.24-28)
- Governance- und Oversight-Strukturen (A.5.1, 5.4)


**Assessment**: Falls Organisation FINMA-Lizenz oder -Registrierung hält → **Mandatory Compliance**

## Digital Operational Resilience Act (DORA)

**Regulation**: Regulation (EU) 2022/2554 zur digitalen operationellen Resilienz im Finanzsektor  
**Inkrafttretensdatum**: 17. Januar 2025

**Anwendbarkeits-Trigger**:

- Organisation ist ein **Finanzunternehmen in der EU**:
  - Kreditinstitute (Banken)
  - Zahlungsinstitute und E-Geld-Institute
  - Wertpapierfirmen
  - Krypto-Asset-Service-Provider
  - Versicherungs- und Rückversicherungsunternehmen
  - ICT-Drittdienstleister für Finanzunternehmen (Critical/Important-Designation)


**Kernbestimmungen**:

- **ICT Risk Management**: Umfassendes Framework für Identification, Protection, Detection, Response, Recovery
- **Incident Reporting**: Major ICT-bezogene Incidents an zuständige Behörden
- **Digital Operational Resilience Testing**: Regelmässige Tests einschliesslich Threat-Led Penetration Testing (TLPT)
- **Third-Party Risk**: ICT Service Provider Oversight, Verträge, Exit-Strategien
- **Information Sharing**: Threat Intelligence und Cybersecurity-Informationsaustausch


**ISMS-Impact**:

- Erweitertes ICT Risk Management Framework (über ISO 27001 hinaus)
- Erweiterte Incident Detection und Response (A.5.24-28)
- Mandatory Resilience Testing Programs
- Supplier Risk Management mit Regulatory Oversight (A.5.19-23)
- Information Sharing Arrangements


**Assessment**: Falls Organisation ein EU-Finanzunternehmen oder kritischer ICT Service Provider ist → **Mandatory Compliance**

## Network and Information Security Directive 2 (NIS2)

**Directive**: Directive (EU) 2022/2555 über Massnahmen für ein hohes gemeinsames Cybersecurity-Niveau  
**Umsetzungsfrist**: 17. Oktober 2024 (EU-Mitgliedstaaten müssen in nationales Recht umsetzen)

**Anwendbarkeits-Trigger**:

- Organisation ist ein **Essential oder Important Entity** in der EU in abgedeckten Sektoren:
  

**Essential Entities** (strengere Anforderungen):

- Energie (Elektrizität, Öl, Gas)
- Transport (Luft, Schiene, Wasser, Strasse)
- Banking und Financial Market Infrastructures
- Gesundheit (Healthcare Providers, EU Reference Laboratories, Pharmahersteller)
- Trinkwasser und Abwasser
- Digitale Infrastruktur (Internet Exchange Points, DNS Service Providers, Cloud Computing, Data Centers, CDNs, Trust Service Providers)
- ICT Service Management (Managed Service Providers, Managed Security Service Providers)
- Public Administration (zentrale Regierungsstellen)
- Raumfahrt (bodengestützte Infrastruktur für Weltraumsysteme)


**Important Entities** (weniger streng):

- Post- und Kurierdienste
- Abfallwirtschaft
- Chemieproduktion und -vertrieb
- Lebensmittelproduktion und -vertrieb
- Fertigung (Medizinprodukte, Elektronik, Maschinen, Kraftfahrzeuge, Luft- und Raumfahrt)
- Digitale Anbieter (Online-Marktplätze, Suchmaschinen, Social Networks)
- Forschungsorganisationen


**Kernbestimmungen**:

- **Risk Management**: Cybersecurity Risk Assessment und Security Policies
- **Incident Handling**: Detection-, Response-, Recovery-Fähigkeiten
- **Business Continuity**: Backup Management, Disaster Recovery
- **Supply Chain Security**: Third-Party Risk Management
- **Network Security**: Access Controls, Encryption, Multi-Factor Authentication
- **Incident Notification**: 24-Stunden-Frühwarnung, 72-Stunden-detaillierter Incident Report an nationales CSIRT/zuständige Behörde
- **Supervision**: Periodische Audits, Security Assessments, Ex-Post-Monitoring


**ISMS-Impact**:

- Umfassendes Cybersecurity Risk Management (Clause 6)
- Incident Response mit Regulatory Reporting Timelines (A.5.24-28)
- Supply Chain Security-Anforderungen (A.5.19-23)
- Technische Security Controls (Encryption, Access Control) (A.8.x-Serie)
- Business Continuity und Disaster Recovery (A.5.29-30)


**Strafen**: Bis zu €10 Millionen oder 2% des weltweiten Jahresumsatzes (Essential Entities), €7 Millionen oder 1,4% (Important Entities)

**Assessment**: Falls Organisation in abgedecktem Sektor in der EU tätig ist und Grössen-/Kritikalitätsschwellen erfüllt → **Mandatory Compliance**

## Payment Card Industry Data Security Standard (PCI DSS)

**Standard**: PCI DSS v4.0 (in Kraft seit 31. März 2024)  
**Governing Body**: PCI Security Standards Council

**Anwendbarkeits-Trigger**:

- Organisation **speichert, verarbeitet oder überträgt** Payment Cardholder Data:
  - Händler, die Kredit-/Debitkarten akzeptieren
  - Payment Processors und Gateways
  - Service Provider, die Cardholder Data handhaben
  - Jede Entität mit Zugang zur Cardholder Data Environment (CDE)


**Kernbestimmungen**:

- **12 Requirements über 6 Control Objectives**:

  1. Network Security Controls installieren und warten
  2. Secure Configurations auf alle System Components anwenden
  3. Gespeicherte Account Data schützen
  4. Cardholder Data mit starker Kryptografie während der Übertragung schützen
  5. Systeme und Networks vor Malicious Software schützen
  6. Secure Systems und Software entwickeln und warten
  7. Zugriff auf Cardholder Data nach Business Need-to-Know beschränken
  8. User identifizieren und Zugriff auf System Components authentifizieren
  9. Physical Access auf Cardholder Data beschränken
  10. Alle Zugriffe auf System Components und Cardholder Data loggen und überwachen
  11. Security von Systems und Networks regelmässig testen
  12. Information Security mit organisatorischen Policies und Programs unterstützen

**ISMS-Impact**:

- Network Segmentation und Firewall Controls (A.8.20-22)
- Encryption von Cardholder Data at Rest und in Transit (A.8.24)
- Starke Access Controls und Authentication (A.5.15-18, A.8.2-5)
- Vulnerability Management und Patching (A.8.8)
- Logging, Monitoring und Audit Trails (A.8.15-16)
- Penetration Testing und Vulnerability Scanning (A.8.8)


**Validation**: Jährliches On-Site-Audit (Level 1), Self-Assessment Questionnaire (SAQ) für kleinere Händler

**Assessment**: Falls Organisation Payment Cards handhabt → **Mandatory Compliance**

## Health Insurance Portability and Accountability Act (HIPAA)

**Regulation**: US-Bundesgesetz zum Schutz von Health Information  
**Inkrafttretensdatum**: 1996 (mit Updates durch HITECH Act 2009, Omnibus Rule 2013)

**Anwendbarkeits-Trigger**:

- Organisation ist ein **Covered Entity** oder **Business Associate**, der US Protected Health Information (PHI) handhabt:
  - Healthcare Providers (Ärzte, Krankenhäuser, Kliniken)
  - Health Plans (Versicherungsgesellschaften, HMOs, Medicare/Medicaid)
  - Healthcare Clearinghouses
  - Business Associates (Vendors, Contractors, die PHI im Namen von Covered Entities handhaben)


**Kernbestimmungen**:

- **HIPAA Security Rule** (45 CFR Part 164):
  - **Administrative Safeguards**: Security Management Process, Workforce Security, Information Access Management, Security Awareness Training, Contingency Planning
  - **Physical Safeguards**: Facility Access Controls, Workstation Security, Device and Media Controls
  - **Technical Safeguards**: Access Controls, Audit Controls, Integrity Controls, Transmission Security (Encryption)
- **HIPAA Privacy Rule**: Patient Rights, Minimum Necessary Access, Use and Disclosure Limitations
- **Breach Notification Rule**: Notification an Individuals (60 Tage), HHS, Media (falls >500 betroffen)
- **Business Associate Agreements (BAAs)**: Erforderliche Verträge mit allen Vendors, die PHI handhaben


**ISMS-Impact**:

- Risk Assessment und Risk Management (erforderlich unter Security Rule)
- Access Controls und Authentication (A.5.15-18, A.8.2-5)
- Encryption von PHI (A.8.24)
- Audit Logging und Monitoring (A.8.15-16)
- Incident Response und Breach Notification (A.5.24-28)
- Workforce Training und Awareness (A.6.3)
- Business Associate Management (A.5.19-23)


**Strafen**: $100-$50.000 pro Violation (bis zu $1,5 Millionen pro Jahr), strafrechtliche Strafen für Willful Neglect

**Assessment**: Falls Organisation US-Healthcare-Daten (PHI) handhabt → **Mandatory Compliance**

## Federal Information Security Management Act (FISMA)

**Regulation**: US-Bundesgesetz, das Cybersecurity für Regierungssysteme fordert  
**Inkrafttretensdatum**: 2002 (aktualisiert durch FISMA Reform Act 2014)

**Anwendbarkeits-Trigger**:

- Organisation betreibt **Federal Information Systems** oder bietet **Cloud Services für US Federal Agencies**:
  - Federal Agencies und Departments
  - Federal Contractors und Cloud Service Providers (FedRAMP Authorization)
  - Organisationen, die Federal Information verarbeiten


**Kernbestimmungen**:

- **Risikobasierter Ansatz für Cybersecurity**: Nach NIST SP 800-53 Controls
- **Categorization**: System Categorization (Low, Moderate, High) per FIPS 199
- **Control Implementation**: NIST SP 800-53 Security Controls basierend auf Impact Level
- **Continuous Monitoring**: Laufendes Security Assessment und Authorization (A&A)
- **FedRAMP (für Cloud)**: Federal Risk and Authorization Management Program
  - Third-Party Assessment durch akkreditierte Assessors (3PAO)
  - Authorization durch JAB (Joint Authorization Board) oder Agency ATO (Authority to Operate)


**ISMS-Impact**:

- NIST SP 800-53 Control Implementation (umfassende Security Controls)
- System Categorization und Impact Analysis (A.5.9)
- Continuous Monitoring und Assessment (A.8.15-16)
- Supply Chain Risk Management (A.5.19-23)
- Incident Response aligned mit NIST Frameworks (A.5.24-28)


**Assessment**: Falls Organisation US Federal Contracts oder FedRAMP Authorization hat → **Mandatory Compliance**

## Weitere Conditional Regulations

Organisationen sollten die Anwendbarkeit basierend auf dem Business Context bewerten:

| Regulation | Anwendbarkeits-Trigger | Region/Scope |
|-----------|---------------------|--------------|
| **Sarbanes-Oxley (SOX)** | US Publicly Traded Company | Vereinigte Staaten |
| **GLBA (Gramm-Leach-Bliley)** | US Financial Institution | Vereinigte Staaten |
| **CCPA/CPRA** | Verarbeitung von California Resident Data | Kalifornien, USA |
| **China PIPL** | Verarbeitung von Personal Information von China Residents | China |
| **Australia Privacy Act** | Verarbeitung von Australian Personal Information | Australien |
| **Singapore PDPA** | Verarbeitung von Singapore Personal Data | Singapur |
| **LGPD** | Verarbeitung von Brazilian Personal Data | Brasilien |
| **Branchenspezifisch** | Branchenabhängig (Telecom, Energy, Pharma) | Variiert |

---

# Informational Reference / Best Practice (Tier 3)

Diese Frameworks bieten **technische Leitlinien und Best Practices**, sind aber nicht rechtlich durchsetzbar:

## NIST Special Publications (SP 800-series)

**Beschreibung**: National Institute of Standards and Technology Cybersecurity Guidance  
**Anwendbarkeit**: Freiwillige Übernahme für Best Practices (es sei denn, erforderlich durch FISMA/FedRAMP-Vertrag)

**Kernpublikationen**:

- **NIST SP 800-53**: Security and Privacy Controls (umfassender Control-Katalog)
- **NIST SP 800-171**: Schutz von Controlled Unclassified Information (CUI) in non-federal Systems
- **NIST Cybersecurity Framework (CSF)**: Identify, Protect, Detect, Respond, Recover
- **NIST SP 800-61**: Computer Security Incident Handling Guide
- **NIST SP 800-63**: Digital Identity Guidelines (Authentication, Federation)


**Verwendung im ISMS**:

- Technische Implementation Guidance für ISO 27001 Controls
- Incident Response Playbook Development (800-61)
- Identity and Access Management (800-63)
- Risk Assessment Methodologies (800-30, 800-37)


## CIS Controls

**Beschreibung**: Center for Internet Security Critical Security Controls  
**Version**: CIS Controls v8 (18 Controls)  
**Anwendbarkeit**: Freiwillige Übernahme für Security Benchmarking

**Kern-Controls**:
1. Inventory and Control of Enterprise Assets
2. Inventory and Control of Software Assets
3. Data Protection
4. Secure Configuration of Enterprise Assets
5. Account Management
6. Access Control Management
7. Continuous Vulnerability Management
8. Audit Log Management
9-18. Weitere Controls zu Backup, Incident Response, Penetration Testing, Training

**Verwendung im ISMS**:

- Asset Management Practices (A.5.9)
- Configuration Management (A.8.9)
- Vulnerability Management (A.8.8)
- Benchmarking der organisatorischen Security Maturity


## OWASP (Open Web Application Security Project)

**Beschreibung**: Community-getriebene Web Application Security Standards  
**Anwendbarkeit**: Freiwillige Übernahme für Secure Software Development

**Kernressourcen**:

- **OWASP Top 10**: Kritischste Web Application Security Risks
- **OWASP ASVS**: Application Security Verification Standard
- **OWASP SAMM**: Software Assurance Maturity Model
- **OWASP Cheat Sheets**: Secure Coding Guidance


**Verwendung im ISMS**:

- Secure Software Development Lifecycle (A.8.25-28)
- Web Application Security Testing
- Developer Security Training (A.6.3)
- Code Review und Vulnerability Assessment


## ISO/IEC 27002:2022

**Beschreibung**: Code of Practice für Information Security Controls  
**Anwendbarkeit**: Supporting Guidance für ISO 27001 Implementation (nicht separat zertifizierbar)

**Verwendung im ISMS**:

- Detaillierte Implementation Guidance für Annex A Controls
- Control Selection und Tailoring
- Proportionality- und Scalability-Überlegungen


## Cloud Security Alliance (CSA)

**Beschreibung**: Cloud Computing Security Best Practices  
**Anwendbarkeit**: Freiwillige Übernahme für Cloud Security

**Kern-Frameworks**:

- **CSA Cloud Controls Matrix (CCM)**: Cloud Security Control Framework
- **CSA Security Trust Assurance and Risk (STAR)**: Cloud Provider Certification
- **CSA Consensus Assessments Initiative Questionnaire (CAIQ)**: Cloud Security Assessment


**Verwendung im ISMS**:

- Cloud Service Provider Evaluation (A.5.23)
- Cloud Security Architecture
- Vendor Security Assessments


## Weitere Best Practice Frameworks

Organisationen können zusätzliche Frameworks basierend auf dem Branchen-Kontext referenzieren:

| Framework | Beschreibung | Use Case |
|----------|-------------|----------|
| **COBIT** | IT Governance und Management | IT Governance Alignment |
| **ITIL** | IT Service Management | Service Delivery Processes |
| **ISO 22301** | Business Continuity Management | BCM Program Structure |
| **ISO 27017/27018** | Cloud Security und Privacy | Cloud-spezifische Controls |
| **ENISA Guidelines** | EU Cybersecurity Agency Guidance | EU Regulatory Context |

---

# United States Federal Requirements (Spezielle Kategorie)

**Prinzip**: US Federal Cybersecurity Requirements (FISMA, FIPS, FedRAMP, NIST CSF) gelten **nur, wenn die Organisation explizite US Federal Contractual Obligations hat**.

**Default-Status**: **Not Applicable**, es sei denn:

- Organisation hält US Federal Contracts
- Organisation bietet Services für US Federal Agencies
- Vertrag fordert explizit NIST Controls oder FedRAMP Authorization


**Begründung**: US Federal Requirements sind nicht extraterritorial und gelten nicht für Nicht-US-Organisationen, es sei denn, vertraglich gefordert.

**ISMS-Behandlung**:

- NIST Frameworks können als **Informational Reference** (Tier 3) verwendet werden
- FISMA/FedRAMP werden **Mandatory** (Tier 1) nur mit Federal Contracts
- NIST SP 800-series verwendet für Technical Guidance ohne Mandatory Compliance


---

# Bestimmung der Regulatory Applicability

## Assessment-Prozess

Organisationen MÜSSEN jährliche Regulatory Applicability Assessments durchführen:

**Schritt 1: Identifikation der Geschäftsaktivitäten**

- Geografische Standorte der Operationen
- Bediente Branchen und Sektoren
- Arten von verarbeiteten Daten (PII, Healthcare, Financial, etc.)
- Kundenbasis (B2B, B2C, Government)
- Erbrachte Services (Cloud, Consulting, Software, etc.)


**Schritt 2: Mapping von Regulations zu Aktivitäten**

| Geschäftsaktivität | Ausgelöste Regulations |
|-------------------|----------------------|
| Verarbeitung von EU Resident Data | GDPR (mandatory) |
| Betrieb in der Schweiz | Swiss FADP (mandatory) |
| ISO 27001-Zertifizierungsziel | ISO 27001 (mandatory) |
| Verarbeitung von Payment Cards | PCI DSS (conditional - falls ja, mandatory) |
| EU Financial Services | DORA (conditional - falls ja, mandatory) |
| US Federal Contracts | FISMA/FedRAMP (conditional - falls ja, mandatory) |

**Schritt 3: Dokumentation der Anwendbarkeitsbestimmung**

- Erstellung einer Regulatory Applicability Matrix
- Dokumentation der Rationale für Anwendbarkeitsbestimmung
- Zuweisung von Ownership (Legal, Compliance, CISO, DPO)
- Jährliche Updates oder bei Business-Änderungen


**Hinweis**: Dieser Assessment-Prozess identifiziert **welche Regulations gelten**, nicht wie Compliance implementiert oder verifiziert wird. Implementation und Verification werden durch separate ISMS-Prozesse behandelt (Risk Assessment, Control Implementation, Compliance Monitoring).

## Regulatory Applicability Matrix Template

Organisationen sollten eine Regulatory Applicability Matrix pflegen:

| Regulation | Tier | Status | Triggers | Owner | Letztes Review |
|-----------|------|--------|----------|-------|---------------|
| Swiss FADP | 1 - Mandatory | Applicable | Schweizer Operationen | DPO | [Datum] |
| EU GDPR | 1 - Mandatory | Applicable | EU Customer Data | DPO | [Datum] |
| ISO 27001 | 1 - Mandatory | Applicable | Certification Goal | CISO | [Datum] |
| DORA | 2 - Conditional | Not Applicable | Kein Financial Entity | N/A | [Datum] |
| PCI DSS | 2 - Conditional | Applicable | Card Processing | CISO | [Datum] |
| NIST SP 800-53 | 3 - Informational | Reference Only | Technical Guidance | CISO | [Datum] |

## Wann Re-Assessment durchführen

**Trigger-Events für Re-Assessment**:

- Neue Geschäftslinie oder Service-Angebot
- Expansion in neue geografische Märkte
- Acquisition oder Merger
- Neue Kundenverträge mit Regulatory Requirements
- Regulatory Changes (neue Gesetze, aktualisierte Standards)
- Certification Scope Changes (ISO 27001 Expansion)


**Häufigkeit**: Jährliches Minimum + getriggerte Reassessments

**Verantwortlichkeit**: CISO + Legal/Compliance + DPO (vierteljährliches Monitoring), Executive Management Approval (jährliches umfassendes Review)

---

# Verwendung in ISMS Policies

## Standard-Referenzsprache

Alle ISMS Policies MÜSSEN eines der folgenden beinhalten:

**Option A: Section 1.3 Referenz** (Empfohlen für die meisten Policies):

```markdown
## Anwendbarkeit von Regulatory Frameworks

Verweise auf Standards, Frameworks und Regulations in diesem ISMS 
sind kategorisiert gemäss ISMS-POL-00 (Regulatory Applicability Framework):

**Mandatory Compliance:**

- Swiss Federal Data Protection Act (FADP)
- EU GDPR (bei Verarbeitung von EU-Personendaten)
- ISO/IEC 27001:2022
- [Weitere mandatory Regulations gemäss ISMS-POL-00]


**Informational Reference / Best Practice Alignment:**

- NIST Special Publications (SP 800-series)
- [Weitere Frameworks gemäss ISMS-POL-00]


**United States Federal Requirements:**
Verweise auf US Federal Frameworks (FISMA, FIPS, FedRAMP, NIST Cybersecurity 
Requirements) gelten nur, wenn die Organisation explizite US Federal 
Contractual Obligations hat, wie in ISMS-POL-00 definiert.

Für vollständige Regulatory Categorization siehe ISMS-POL-00.
```

**Option B: Dedizierter Regulatory Framework-Abschnitt** (Für control-spezifische Regulations):

```markdown
# Regulatory Framework

Dieser Control implementiert Anforderungen aus Regulations, die gemäss 
ISMS-POL-00 (Regulatory Applicability Framework) kategorisiert sind.

## Mandatory Compliance
[Control-spezifische mandatory Requirements]

## Conditional Applicability
[Control-spezifische conditional Requirements]

## Informational Reference
[Control-spezifische Best Practices]

Für vollständige Regulatory Categorization siehe ISMS-POL-00.
```

## Audit-Referenzen

**Für Internal Audits**:

- Verifizierung, dass alle ISMS Policies ISMS-POL-00 referenzieren
- Bestätigung, dass Regulatory Applicability Matrix aktuell ist (jährlich reviewed)
- Validierung, dass Applicability Determinations dokumentierte Rationale haben


**Für External Audits**:

- Bereitstellung von ISMS-POL-00 als Foundation Document
- Referenzierung der Regulatory Applicability Matrix
- Demonstration des jährlichen Reassessment-Prozesses und Ownership


**Evidence für diese Policy**:
Evidence für diese Policy besteht aus:

- Regulatory Applicability Matrix (aktuelle und historische Versionen)
- Dokumentierte Ownership- und Approval-Records
- Review Records (jährliche und getriggerte Assessments)
- Rationale-Dokumentation für Applicability Determinations


Diese Policy erfordert NICHT:

- Compliance Dashboards oder KPIs
- Evidence von Control Implementation
- Compliance Status Tracking (adressiert in separaten Compliance Monitoring Processes)


---

# Maintenance & Updates

## Review Schedule

**Vierteljährliches Review** (CISO + Legal + DPO):

- Monitoring von Regulatory Changes (GDPR Guidance Updates, neue Directives)
- Tracking von organisatorischen Änderungen (neue Services, neue Märkte)
- Update der Applicability Matrix bei Trigger-Änderungen
- Dokumentation des Reviews im vierteljährlichen ISMS Review Meeting


**Jährliches Review** (Executive Management Approval):

- Umfassendes Regulatory Landscape Assessment
- Update von ISMS-POL-00 für neue Regulations
- Revision der Policy Reference Language bei Bedarf
- Executive Sign-Off zu Compliance Obligations
- Update von Version Control und Distribution


**Getriggertes Review**:

- Neue Regulation publiziert (DORA effective, AI Act published)
- Business Expansion (neues Land, neuer Service)
- Merger/Acquisition
- Major Contract mit neuen Regulatory Requirements


**Verantwortlichkeit**:

- **Regulatory Monitoring**: Legal/Compliance Officer (primär), CISO (unterstützend)
- **Applicability Assessment**: CISO + Legal/Compliance + DPO (gemeinsame Verantwortlichkeit)
- **Matrix Updates**: CISO (Owner), DPO (Data Protection Regulations)
- **Policy Updates**: CISO (Autor), Executive Management (Approval)


## Kommunikation

**Policy Updates werden kommuniziert via**:

- Policy Portal Update
- E-Mail an alle Policy Owners
- Legal/Compliance Briefing
- CISO Briefing an Executive Management
- Training Material Updates (bei wesentlichen Änderungen)


**Benachrichtigte Stakeholder**:

- Alle ISMS Policy Authors (sofortiger Impact)
- System Owners (Control Scoping Impact)
- Internal Audit (Audit Planning)
- External Auditors (Certification Scope)


## Version Control

**Major Version (X.0)**:

- Neue mandatory Regulations hinzugefügt (Tier 1 Changes)
- Tier Changes (informational → mandatory)
- Strukturelle Änderungen am Framework
- Entfernung von Regulations (nicht mehr applicable)


**Minor Version (X.Y)**:

- Klarstellungen zu bestehenden Regulations
- Zusätzliche informational Frameworks (Tier 3)
- Reference Updates (NIST Publication Versions, GDPR Guidance)
- Nicht-strukturelle Verbesserungen


---

# Verwandte Dokumente

**Interne Referenzen**:

- Alle ISMS Policies (ISMS-POL-A.X.XX-Serie)
- ISMS Risk Assessment Methodology (Clause 6)
- ISMS Statement of Applicability (Annex A Scoping)
- ISMS Compliance Monitoring Processes


**Externe Referenzen**:

- Swiss Federal Data Protection Act (SR 235.1)
- EU GDPR (Regulation 2016/679)
- ISO/IEC 27001:2022
- NIST Special Publications (nist.gov)
- PCI DSS (pcisecuritystandards.org)
- DORA (Regulation 2022/2554)
- NIS2 (Directive 2022/2555)


---

# Glossar

| Begriff | Definition |
|------|------------|
| **Applicable** | Regulation gilt für die Organisation basierend auf Geschäftsaktivitäten, muss eingehalten werden |
| **Conditional** | Regulation gilt nur, wenn spezifische Triggers erfüllt sind (Branche, Geografie, Datentyp) |
| **Mandatory** | Gesetzliche Verpflichtung, durchsetzbar durch Gesetz oder Vertrag, Nichteinhaltung hat Konsequenzen |
| **Informational** | Referenz für Best Practices, nicht rechtlich durchsetzbar, freiwillige Übernahme |
| **Tier 1** | Mandatory Compliance (gesetzlich, vertraglich) |
| **Tier 2** | Conditional Compliance (kontextabhängig) |
| **Tier 3** | Informational Reference (Best Practice, freiwillig) |
| **Binding Force** | Rechtliche oder vertragliche Durchsetzbarkeit einer Regulation |
| **Implementation Obligation** | Anforderung zur Implementierung spezifischer Controls (bestimmt durch Risk Assessment) |

---

# Abschluss-Statement

Diese Policy etabliert die Anwendbarkeit von Regulations für das Information Security Management System der Organisation.

**Was diese Policy etabliert:**

- Identifikation anwendbarer Regulations (mandatory, conditional, informational)
- Assessment-Methodik zur Bestimmung der Regulatory Applicability
- Review- und Update-Prozesse für Änderungen in der Regulatory Landscape


**Was diese Policy NICHT etabliert:**

- Risk Treatment-Entscheidungen (adressiert in Clause 6 - Risk Management)
- Control Implementation-Anforderungen (adressiert in Annex A Controls)
- Compliance-Status oder Verification (adressiert in Compliance Monitoring Processes)


**Separation of Concerns:**

- **Diese Policy (POL-00)**: Definiert WELCHE Regulations gelten
- **Risk Management (Clause 6)**: Bestimmt WIE auf Regulatory Requirements reagiert wird
- **Control Implementation (Annex A)**: Implementiert SPEZIFISCHE Controls
- **Compliance Monitoring**: Verifiziert und trackt COMPLIANCE-Status


---

**ENDE VON ISMS-POL-00**

*"Regulatory Applicability ist das Fundament. Implementation und Compliance sind die darauf aufbauende Struktur."*
<!-- QA_VERIFIED: 2026-02-01 -->
