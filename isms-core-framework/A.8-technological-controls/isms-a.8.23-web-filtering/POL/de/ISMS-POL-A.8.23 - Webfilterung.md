<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.23-DE:framework:POL:a.8.23-de -->
**ISMS-POL-A.8.23 — Webfilterung**

---

**Dokumentenlenkung**

| Feld | Wert |
|------|------|
| **Dokumenten Titel** | Webfilterung |
| **Dokumententyp** | Konzept |
| **Dokument-ID** | ISMS-POL-A.8.23 |
| **Dokumenteneigentümer/in** | Chief Information Security Officer (CISO) |
| **Freigabe durch** | Geschäftsleitung (GL) |
| **Erstellt** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versions-Verzeichnis**:

| Version | Datum | Autor | Änderungsvermerk |
|---------|-------|-------|------------------|
| 1.0 | [Date] | CISO | Initiale Richtlinie für ISO 27001:2022 Erstzertifizierung |

**Review-Zyklus**: Jährlich  
**Nächstes Review-Datum**: [Inkraftsetzungsdatum + 12 Monate]  

**Freigabekette**:

- Primär: Chief Information Security Officer (CISO)
- Sekundär: Chief Information Officer (CIO)
- Compliance: Legal/Compliance Officer
- Finale Autorität: Geschäftsleitung (GL)

**Zugehörige Dokumente**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.23 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Control A.8.23

---

## Management Summary

Diese Richtlinie definiert die Anforderungen von [Organisation] für Web-Filtering-Kontrollen zum Schutz von Benutzern und organisatorischen Informationen vor webbasierten Bedrohungen gemäss ISO/IEC 27001:2022 Control A.8.23.

**Geltungsbereich**: Diese Richtlinie gilt für alle Netzwerksegmente, wo Benutzer auf Internetressourcen zugreifen, alle organisatorischen Mitarbeiter und alle Web-Filtering-Technologien unabhängig vom Deployment-Modell.

**Zweck**: Definition organisatorischer Anforderungen für Implementierung und Governance von Web-Filtering-Kontrollen. Diese Richtlinie definiert WAS Web-Filtering-Schutz erforderlich ist und WER verantwortlich ist. Implementierungsprozeduren (WIE) sind separat in ISMS-IMP-A.8.23 dokumentiert.

**Regulatorisches Alignment**: Diese Richtlinie adressiert obligatorische Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatory Applicability Framework), einschliesslich Schweizer nDSG, EU DSGVO und ISO/IEC 27001:2022. Konditionale branchenspezifische Anforderungen (PCI DSS v4.0.1, FINMA, DORA, NIS2) gelten, wo Geschäftsaktivitäten der [Organisation] Anwendbarkeit auslösen.

---

# Control Alignment & Geltungsbereich

## ISO/IEC 27001:2022 Control A.8.23

**ISO/IEC 27001:2022 Annex A.8.23 - Web Filtering**

> *Access to external websites shall be managed to reduce exposure to malicious content.*

**Control-Zielsetzung**: Etablierung organisatorischer Richtlinie für Web-Filtering-Kontrollen zum Schutz von Benutzern und Informationen vor webbasierten Bedrohungen durch die gesamte Netzwerkinfrastruktur der Organisation.

**Diese Richtlinie adressiert**:

- Anforderungen an Web-Filtering-Kontrollen basierend auf Bedrohungslandschaft und organisatorischer Risikoakzeptanz
- Anforderungen an Netzwerk-Coverage zur Sicherstellung umfassenden Schutzes
- Organisatorische Rollen und Verantwortlichkeiten für Web-Filtering-Governance
- Frameworks für Exception Management und Incident Management
- Integration mit Risk Assessment und Treatment Prozessen der [Organisation]

## Was diese Richtlinie tut

Diese Richtlinie:

- **Definiert** Anforderungen an Web-Filtering-Kontrollen ausgerichtet auf organisatorisches Risk Assessment
- **Etabliert** Governance-Framework für Web-Filtering-Entscheidungsfindung
- **Spezifiziert** Verantwortlichkeit für Implementierung von Web-Filtering-Kontrollen
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

## Was diese Richtlinie NICHT tut

Diese Richtlinie tut NICHT:

- **Spezifizieren technischer Implementierungsdetails** (siehe ISMS-IMP-A.8.23 Implementation Guides)
- **Definieren spezifischer Filtering-Kategorien oder URL-Listen** (siehe ISMS-IMP-A.8.23 Policy Configuration Assessment)
- **Bereitstellen systemspezifischer Konfigurationsprozeduren** (siehe ISMS-IMP-A.8.23 Assessment Guides)
- **Auswählen von Filtering-Technologien oder Anbietern** (Technologieauswahl basierend auf Risk Assessment der [Organisation])
- **Ersetzen von Risk Assessment** (Web-Filtering-Kontrollen werden basierend auf Risk Treatment der [Organisation] ausgewählt)

**Rationale**: Trennung von Richtlinienanforderungen und Implementierungsleitlinien ermöglicht:

- Richtlinienstabilität trotz sich entwickelnder Bedrohungslandschaft
- Technische Agilität für Technologie-Updates ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Execution (Implementierung)

## Geltungsbereich

**Diese Richtlinie gilt für**:

- Alle Netzwerksegmente, die Internet-Konnektivität bereitstellen (On-Premises, Wireless, Remote Access, Cloud)
- Alle Benutzer (Angestellte, Auftragnehmer, Temporäres Personal, Gäste wo anwendbar)
- Alle Geräte, die auf organisatorische Netzwerkressourcen zugreifen
- Alle Web-Filtering-Implementierungen unabhängig vom Deployment-Modell (Gateway, Cloud-basiert, Endpoint, DNS-basiert)
- Alle Drittanbieter-Services, die Netzwerkzugang bereitstellen

**Nicht im Geltungsbereich**:

- E-Mail-Filtering (durch separate E-Mail-Sicherheitsrichtlinien abgedeckt)
- Network Intrusion Prevention jenseits webbasierter Bedrohungen (durch Netzwerksicherheitsrichtlinien abgedeckt)
- Endpoint Antivirus/Anti-Malware (durch Endpoint-Schutzrichtlinien abgedeckt)
- Data Loss Prevention (durch DLP-Richtlinien abgedeckt, obwohl Web Filtering DLP-Ziele unterstützen kann)

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen sind gemäss **ISMS-POL-00 (Regulatory Applicability Framework)** kategorisiert.

**Tier 1: Obligatorische Compliance**

| Regulierung | Anwendbarkeit | Hauptanforderungen |
|-------------|---------------|-------------------|
| **Schweizer nDSG** | Alle Schweizer Operationen | Art. 8 - Angemessene technische und organisatorische Massnahmen |
| **EU DSGVO** | Bei Verarbeitung personenbezogener Daten von EU-Bürgern | Art. 32 - Sicherheitsmassnahmen inkl. Zugangskontrollen |
| **ISO/IEC 27001:2022** | Zertifizierungsbereich | Control A.8.23 - Dokumentierte Richtlinie und Implementierung |

**Tier 2: Konditionale Anwendbarkeit**

Gelten nur, wenn spezifische Geschäftsbedingungen Anwendbarkeit auslösen:

| Regulierung | Auslöse-Bedingung | Web-Filtering-Anforderungen |
|-------------|-------------------|------------------------------|
| **PCI DSS v4.0.1** | Verarbeitung von Zahlungskartendaten | Netzwerksicherheitskontrollen, Malware-Schutz |
| **FINMA** | Schweizer regulierte Finanzinstitution | Technische und organisatorische Massnahmen gemäss Risk Assessment |
| **DORA** | EU-Finanzdienstleistungs-Entität | Netzwerksicherheitskontrollen, Cyber-Resilienz |
| **NIS2** | Essenzielle/wichtige Entität (EU) | Sicherheitsmassnahmen für Netzwerk- und Informationssysteme |

**Tier 3: Informationsleitlinien**

Diese Frameworks informieren Implementierung, stellen aber keine obligatorische Compliance dar, sofern nicht vertraglich gefordert:

- NIST Cybersecurity Framework (Protect Function)
- CIS Controls v8.1 (Control 9: Email and Web Browser Protections)
- MITRE ATT&CK Framework (Defense Techniques)
- OWASP (Web Security Testing Guide)

**Compliance-Bestimmung**: [Organisation] bestimmt anwendbare Tier 2 Regulierungen durch periodische Geschäftsaktivitäts-Assessments. Die strengsten Anforderungen gelten bei Überschneidung mehrerer Regulierungen.

---

# Framework für Web-Filtering-Anforderungen

## Threat Protection Anforderungen (Obligatorisch)

[Organisation] implementiert Web-Filtering-Fähigkeiten zum Schutz vor webbasierten Bedrohungen.

**Erforderliche Schutzkategorien**:

| Bedrohungs-Kategorie | Schutzanforderung | Implementierungs-Priorität |
|----------------------|-------------------|---------------------------|
| **Malicious Content** | Blockieren bekannter Malware-Verteilungs-Sites | **Obligatorisch** |
| **Phishing** | Blockieren von Credential Harvesting und Brand Impersonation | **Obligatorisch** |
| **Command & Control** | Blockieren von C2-Infrastruktur und Botnet-Kommunikation | **Obligatorisch** |
| **Exploit Delivery** | Blockieren von Sites mit Exploit Kits und Vulnerability Exploitation | **Obligatorisch** |

**Implementierungs-Hinweis**: Spezifische Threat Intelligence Feeds, Update-Frequenzen und Blockierungs-Mechanismen sind in ISMS-IMP-A.8.23-1 (Filtering Infrastructure Assessment) und ISMS-IMP-A.8.23-3 (Policy Configuration Assessment) definiert.

**Threat Intelligence**: [Organisation] SOLL Threat Intelligence von renommierten Quellen nutzen, um aktuellen Schutz vor neu aufkommenden Bedrohungen aufrechtzuerhalten. Threat Intelligence Integration Prozeduren dokumentiert in ISMS-IMP-A.8.23-3.

## Category Filtering Ansatz (Risikobasiert)

[Organisation] definiert Web-Filtering-Category-Ansatz basierend auf organisatorischer Risikoakzeptanz und Compliance-Anforderungen.

**Organisatorische Ansatz-Optionen**:

[Organisation] SOLL einen der folgenden Ansätze dokumentieren:

1. **Restriktives Blocking**: Spezifische Website-Kategorien blockiert basierend auf Risk Assessment und Compliance-Anforderungen
2. **Trust-basiertes Monitoring**: Meiste Kategorien erlaubt mit Aktivitäts-Monitoring und Acceptable Use Policy Enforcement
3. **Hybrid Risikobasiert**: Hochrisiko-Kategorien blockiert, Mittelrisiko-Kategorien überwacht, Niedrigrisiko-Kategorien erlaubt basierend auf Risikoklassifizierung

**Implementierungs-Hinweis**: Ausgewählter Ansatz, spezifische blockierte/überwachte Kategorien und Risikoklassifizierungs-Kriterien sind in ISMS-IMP-A.8.23-3 (Policy Configuration Assessment) dokumentiert. Category-Entscheidungen überprüft basierend auf Risk Assessment und allen Benutzern kommuniziert.

**Gewählter Organisatorischer Ansatz:** [Organisation] implementiert einen **Hybrid Risikobasierten** Ansatz:

- **Blockiert (Hochrisiko):** Malware-Verteilung, Phishing, C2/Botnets, Exploit Kits, illegale Inhalte, Anonymisierer/offene Proxies
- **Überwacht (Mittelrisiko):** File Sharing, Streaming Media, Social Networking, persönliche Webmail
- **Erlaubt (Niedrigrisiko):** Business, News, Bildung, Technologie, Regierung, Finanzdienstleistungen

Kategorie-Klassifizierungen und Blocking-Regeln sind dokumentiert in ISMS-IMP-A.8.23-3 (Policy Configuration Assessment) und werden quartalsweise überprüft. Änderungen an Kategorie-Klassifizierungen erfordern Security Team Review und CISO-Genehmigung.

## Netzwerk-Coverage-Anforderungen

[Organisation] implementiert Web-Filtering-Kontrollen zur Erreichung umfassender Coverage.

**Coverage-Prinzip**: Alle Pfade zum Internet von organisatorischen Geräten SOLLEN Web-Filtering-Kontrollen durchlaufen.

**Erforderliche Coverage**:

- Primäre Internet-Verbindungspunkte
- Wireless-Netzwerke (Corporate Access)
- Remote Access Infrastruktur
- Cloud-gehostete Ressourcen mit Internetzugang
- Branch Office Verbindungen

**Implementierungs-Hinweis**: Netzwerk-Topologie-Dokumentation, Coverage-Verifizierungs-Prozeduren und Gap-Identifikations-Methoden sind in ISMS-IMP-A.8.23-2 (Network Coverage Assessment) definiert.

**Coverage-Verifizierung**: [Organisation] SOLL Filtering-Coverage durch technisches Testing verifizieren. Testing-Methodologie und Frequenz definiert in ISMS-IMP-A.8.23-2.

**Akzeptable Coverage-Exceptions**:

- Gast-Netzwerke (Anforderungen definiert in Annex A: Guest Network Filtering Requirements)
- Dedizierte B2B-Partner-Verbindungen (dokumentiert, risikobewertet, durch CISO genehmigt)
- Air-gapped Netzwerke ohne Internet-Konnektivität
- Spezifische Benutzergruppen mit dokumentierten und genehmigten Exceptions

## Logging und Monitoring

[Organisation] implementiert Logging von Web-Filtering-Events zur Unterstützung von Security-Monitoring und Incident-Investigation.

**Logging-Anforderungen**:

- Web-Access-Events (erlaubt und blockiert)
- Security-Events (Threat-Blocks, Policy-Violations)
- Benutzer-Attribution (wo technisch verfügbar und Privacy-compliant)
- Ausreichendes Detail für Incident-Investigation und forensische Analyse

**Log-Retention:**

- Security-Events (Threat-Blocks, C2-Versuche, Umgehungs-Versuche, Policy-Violations): Minimum **12 Monate**
- Allgemeine Web-Access-Logs (erlaubte Anfragen): Minimum **90 Tage**
- Erweiterte Retention gilt, wo regulatorische Anforderungen längere Perioden vorschreiben (gemäss ISMS-POL-00 Abschnitt 4.2)
- Logs geschützt mit angemessenen Integritäts- und Vertraulichkeits-Kontrollen gemäss A.8.15
- Log-Löschung erfordert dokumentierte Genehmigung und folgt Data Retention Policy Prozeduren

**Implementierungs-Hinweis**: Spezifische Logging-Felder, Retention-Perioden, Storage-Anforderungen und Monitoring-Prozeduren sind in ISMS-IMP-A.8.23-4 (Monitoring & Response Assessment) definiert.

**Privacy-Compliance**: Logging SOLL mit anwendbaren Privacy-Regulierungen gemäss ISMS-POL-00 konform sein. Benutzer informiert über Monitoring durch Acceptable Use Policy. Zugang zu Logs beschränkt auf autorisiertes Personal mit legitimer Notwendigkeit.

---

# Rollen, Governance & Incident Response

## Rollen und Verantwortlichkeiten

**Geschäftsleitung / Verwaltungsrat**:

- Verantwortlich für Genehmigung von Web-Filtering-Richtlinie und -Strategie
- Sicherstellung adäquater Ressourcen und Budget
- Akzeptanz von Restrisiken
- Unterstützung des Sicherheitsprogramms

**Chief Information Security Officer (CISO)**:

- Verantwortlich für gesamte Web-Filtering-Richtlinien- und Programm-Effektivität
- Genehmigung von Hochrisiko-Exceptions und Richtlinien-Änderungen
- Definition organisatorischer Risikoakzeptanz für Web Filtering
- Eskalation kritischer Issues an Geschäftsleitung
- Jährlicher Richtlinien-Review und Genehmigung

**Security Team**:

- Verantwortlich für Implementierung der Web-Filtering-Richtlinien-Anforderungen
- Konfiguration und Wartung von Filtering-Lösungen
- Monitoring von Events und Response auf Security-Incidents
- Verarbeitung von Exception-Requests und Durchführung von Risk Assessments
- Integration von Threat Intelligence Feeds
- Durchführung periodischer Coverage-Assessments

**IT Operations / Network Team**:

- Verantwortlich für Deployment und Wartung der Web-Filtering-Infrastruktur
- Sicherstellung, dass Netzwerk-Topologie Filtering-Coverage unterstützt
- Bereitstellung technischen Supports für Filtering-Systeme
- Koordination von Changes mit Security Team

**Benutzer (Alle Mitarbeiter)**:

- Verantwortlich für Compliance mit Web-Filtering-Richtlinien und Acceptable Use Policy
- Reporting von False Positives und Security-Concerns
- Verwendung von Exception-Prozess für legitime Geschäfts-Needs
- Verboten, Versuche zu unternehmen, Web-Filtering-Kontrollen zu umgehen

**Detaillierte RACI-Matrix**: Vollständige Rollen- und Verantwortlichkeits-Matrix dokumentiert in ISMS-IMP-A.8.23 Implementation Guides.

## Assessment und Verifizierung

[Organisation] verifiziert Web-Filtering-Kontroll-Effektivität durch strukturiertes Assessment.

**Assessment-Domänen**:
1. Filtering Infrastructure: Deployierte Technologien und Fähigkeiten
2. Network Coverage: Topologie-Mapping und Coverage-Verifizierung
3. Policy Configuration: Filtering-Regeln, Kategorien und Threat Feeds
4. Monitoring & Response: Logging, Alerting und Incident Response Fähigkeiten
5. Compliance Summary: Konsolidierte Metriken und Gap-Analyse

**Implementierungs-Hinweis**: Assessment-Methodologie, Evidence-Anforderungen, Workbooks und Compliance-Berechnungs-Prozeduren sind in ISMS-IMP-A.8.23 (Implementation Guidance Suite) definiert. Assessment-Tools separat von Richtlinie gepflegt zur Ermöglichung häufiger Updates.

**Assessment-Frequenz:**

- Umfassendes Assessment: **Jährlich** (ausgerichtet auf internes Audit-Programm, typischerweise Q4)
- Periodische Verifizierung: **Quartalsweise** (Coverage-Testing, Threat Feed Aktualität, Policy-Effektivität)
- Getriggertes Assessment: **Innerhalb 30 Tagen** nach:
  - Signifikanten Security-Incidents mit webbasierten Bedrohungen
  - Grösseren Infrastruktur-Änderungen, die Filtering-Coverage beeinflussen
  - Deployment neuer Filtering-Lösungen oder Major Version Upgrades
  - Audit-Findings, die Remediation-Verifizierung erfordern

## Exception Management

**Exception-Request-Anforderungen**:

Exceptions zu Web-Filtering-Richtlinien-Anforderungen benötigen:

- Dokumentierte geschäftliche oder technische Begründung
- Risk Assessment (Wahrscheinlichkeit, Impact, Restrisiko)
- Kompensierende Kontrollen (wo machbar)
- Timeline für Erreichung vollständiger Compliance (wo anwendbar)
- Formale Genehmigung gemäss Autoritäts-Matrix

**Genehmigungs-Autorität**:

- **Einzelne URL/Domain-Exceptions**: Security Team Lead Genehmigung
- **Category-Exceptions (individuell)**: Security Team Lead + Manager Genehmigung
- **Category-Exceptions (Gruppe/Abteilung)**: CISO + Abteilungsleiter Genehmigung
- **Hochrisiko-Exceptions**: CISO + Geschäftsleitung Genehmigung
- **Threat Protection Exceptions**: NICHT ERLAUBT (Malware, Phishing, C2 Blocks können nicht umgangen werden)

**Monitoring**: Aktive Exceptions überprüft basierend auf Risiko-Level. Exception-Aktivität überwacht für Policy-Compliance. Exceptions widerrufen, falls Risikoprofil sich ändert oder geschäftliche Begründung nicht länger gültig.

**Exception Template**: ISMS-IMP-A.8.23 Exception Request Prozeduren stellen standardisiertes Dokumentations-Format und Workflow bereit.

## Incident Response

**Web-Filtering Security Incidents** beinhalten:

- Command and Control (C2) Kommunikations-Versuche (indiziert potenzielle Kompromittierung)
- Wiederholte Malware- oder Phishing-Versuche von spezifischen Benutzern/Systemen
- Umgehungs-Versuche (Proxy-Verwendung, VPN zur Umgehung von Filtering)
- Web-Filtering-System-Ausfälle oder Coverage-Gaps
- False Positive Patterns, die Fehlkonfiguration indizieren

**Response-Prozess**:
1. **Detection & Reporting**: Security-Events triggern Alerts gemäss Schweregrad
2. **Assessment**: Incident-Klassifikation basierend auf Bedrohungs-Level
3. **Investigation**: Root Cause Analysis und Scope-Bestimmung
4. **Containment**: Sofortige Aktionen basierend auf Incident-Typ
5. **Recovery**: System-Wiederherstellung und präventive Massnahmen
6. **Post-Incident**: Lessons Learned und Kontroll-Verbesserungen

**Kritische Incidents**: C2-Kommunikations-Versuche behandelt als hochpriorisierte Security-Incidents, die sofortige Investigation potenziell kompromittierter Systeme erfordern.

**Detaillierte Prozeduren**: ISMS-IMP-A.8.23-4 (Monitoring & Response Assessment) stellt Incident-Klassifikations-Kriterien, Response-Workflows, Eskalations-Prozeduren und Koordination mit Endpoint-Security-Teams bereit.

## Richtlinien-Governance

**Richtlinien-Review**:

- **Frequenz**: Jährlich Minimum
- **Trigger**: Regulatorische Änderungen, Major Incidents, signifikante Bedrohungslandschafts-Änderungen, organisatorische Änderungen, Audit-Findings
- **Reviewer**: CISO, IT Security Team, Legal/Compliance, IT Operations
- **Genehmigung**: CISO (technisch), Geschäftsleitung (strategisch)

**Implementation Standards Review**:

- **Frequenz**: Basierend auf Bedrohungslandschafts-Evolution (mindestens halbjährlich)
- **Autorität**: Security Team schlägt Updates vor, CISO genehmigt
- **Hinweis**: Implementation Standard Updates (ISMS-IMP-A.8.23) erfordern keine Richtlinien-Revision

**Richtlinien-Updates**:

- **Minor** (Klarstellungen, Referenzen): CISO-Genehmigung, Kommunikation innerhalb 30 Tagen
- **Major** (Scope-Änderungen, neue Anforderungen): Vollständige Freigabekette, Implementierungs-Timeline gemäss Change Management
- **Emergency** (kritische Bedrohungen): CISO-Genehmigung, sofortige Kommunikation und Implementierung

**Kommunikation**: Richtlinie publiziert in ISMS-Dokumenten-Repository. Änderungen organisationsweit kommuniziert. Training für signifikante Änderungen bereitgestellt, die Benutzerverhalten oder Verantwortlichkeiten beeinflussen.

---

# Implementierung & Referenzen

## Integration mit ISMS

Diese Richtlinie integriert mit dem Informationssicherheits-Managementsystem der [Organisation]:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Web-Filtering-Kontrollen ausgewählt basierend auf Risk Assessment der [Organisation]
- Bedrohungslandschafts-Assessment bestimmt Schutzanforderungen
- Risk Treatment Plans dokumentieren Web-Filtering-Kontroll-Implementierung

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.8.23 Anwendbarkeit in SoA der [Organisation] begründet
- Implementierungs-Status getrackt und berichtet

**Zugehörige Controls**:

- A.5.10 (Acceptable Use of Information): Definiert akzeptable Internet-Nutzung
- A.8.7 (Protection against malware): Malware-Schutz-Kontrollen inkl. webbasierter Bedrohungen
- A.8.16 (Monitoring Activities): Integriert mit Security-Monitoring-Programm
- A.8.20 (Networks Security): Netzwerk-Level-Sicherheitskontrollen
- A.8.22 (Segregation of Networks): Netzwerk-Segmentierungs-Strategie
- A.5.24 (Information Security Incident Management): Incident Response Framework

## Implementierungs-Ressourcen

**Implementation Guidance** (ISMS-IMP-A.8.23 Suite):

- ISMS-IMP-A.8.23-1: Filtering Infrastructure Assessment (Technologien, Fähigkeiten, Threat Intelligence)
- ISMS-IMP-A.8.23-2: Network Coverage Assessment (Topologie-Mapping, Coverage-Verifizierung)
- ISMS-IMP-A.8.23-3: Policy Configuration Assessment (Kategorien, Regeln, Blocking-Policies)
- ISMS-IMP-A.8.23-4: Monitoring & Response Assessment (Logging, Alerting, Incident-Prozeduren)

**Assessment-Tools**:

- Excel-basierte Assessment Workbooks mit automatisierten Compliance-Berechnungen
- Evidence-Register
- Gap Analysis Templates
- Remediation-Tracking

**Unterstützende Materialien**:

- Exception Request Prozeduren
- Benutzer-Kommunikations-Templates
- Quick Reference Guides
- Incident Response Playbooks

## Regulatorisches Mapping

Diese Richtlinie adressiert Web-Filtering-Anforderungen von:

| Anforderungs-Kategorie | Schweizer nDSG | EU DSGVO | ISO 27001 | PCI DSS v4.0.1* | FINMA* | DORA/NIS2* |
|------------------------|----------------|----------|-----------|---------|---------|------------|
| Web-Threat-Protection | Art. 8 | Art. 32 | A.8.23 | Req. 1, 2, 5 | Risikobasiert | Network Security |
| Zugangskontrollen | Art. 8 | Art. 32 | A.8.23 | Req. 7 | Risikobasiert | Access Controls |
| Logging & Monitoring | Art. 8 | Art. 32 | A.8.23, A.8.15 | Req. 10 | Risikobasiert | Monitoring |
| Incident Response | Art. 8 | Art. 33 | A.8.23, A.5.24 | Req. 12.10 | Incident Mgmt | Incident Response |

*Konditionale Anwendbarkeit gemäss ISMS-POL-00

**Hinweis**: Spezifische regulatorische Interpretation und Compliance-Verifizierungs-Prozeduren sind dokumentiert in ISMS-IMP-A.8.23 (Implementation Guidance Suite).

## Training & Awareness

**Security Awareness** (Alle Mitarbeiter):

- Jährliches Training-Modul zu Web Filtering und Acceptable Use
- Benutzer-Verantwortlichkeiten und Reporting-Prozeduren
- Erkennung von Phishing und verdächtigen Websites

**Technisches Training** (IT/Security-Personal):

- Web-Filtering-Technologie-Konfiguration und Wartung
- Threat Intelligence Integration
- Incident Response Prozeduren
- Exception Request Evaluation

**Operatives Training** (IT Operations, Help Desk):

- False Positive Handling und Eskalation
- Benutzer-Support-Prozeduren
- Häufige Blocking-Szenarien und Resolution

---

# Definitionen

**Web Filtering**: Technologiebasierte Kontrollen, die Zugang zu Web-Ressourcen überwachen, einschränken oder blockieren basierend auf definierten Sicherheitsrichtlinien. Web Filtering analysiert URLs, Domains, Content und Protokolle, um Zugangsversuche zu erlauben, zu verweigern oder zu loggen.

**Threat Protection**: Fähigkeiten zum Blockieren des Zugangs zu bekannten bösartigen Websites inkl. Malware-Verteilungs-Sites, Phishing-Pages, Command-and-Control-Infrastruktur und Exploit-Delivery-Mechanismen.

**Category Filtering**: Fähigkeit, Zugang zu Website-Kategorien (z.B. Social Media, Glücksspiel, Streaming) zu blockieren oder zu überwachen basierend auf organisatorischen Acceptable Use Policies und Risikoakzeptanz.

**Netzwerk-Coverage**: Das Ausmass, in dem Web-Filtering-Kontrollen über alle Netzwerksegmente und Zugriffsmethoden deployed sind, wo Benutzer das Internet erreichen können.

**Exception**: Temporäre oder permanente Abweichung von Standard-Filtering-Policies, gewährt durch formalen Genehmigungs-Prozess mit dokumentierter geschäftlicher Begründung und Risikoakzeptanz.

**C2 (Command and Control)**: Infrastruktur, die von Malware verwendet wird, um mit Angreifern zu kommunizieren und Remote-Kontrolle sowie Daten-Exfiltration zu ermöglichen.

**False Positive**: Legitime Website fälschlicherweise blockiert durch Web-Filtering-System, erfordert Review und Policy-Anpassung.

**Threat Intelligence**: Kuratierte Information über aktuelle und aufkommende webbasierte Bedrohungen, verwendet zur Aktualisierung von Filtering-Policies und Schutz vor neuen Angriffsvektoren.

**Threat Intelligence Feed**: Automatisierter, kontinuierlich aktualisierter Datenstrom von Threat-Intelligence-Anbietern, der aktuelle Indicators of Compromise (IOCs), bösartige URLs, IP-Adressen, Domains und Threat-Actor-Infrastruktur liefert. Feeds integrieren sich mit Web-Filtering-Lösungen, um Echtzeit-Schutz gegen neu identifizierte Bedrohungen zu ermöglichen.

---

# Anhang A: Guest Network Filtering Anforderungen

**Geltungsbereich:** Dieser Anhang definiert Web-Filtering-Anforderungen für Gast-Netzwerksegmente, die Internetzugang für nicht-organisatorische Benutzer bereitstellen (Besucher, Auftragnehmer ohne Corporate Credentials, BYOD auf Gast-SSID).

**Filtering-Ansatz:** Gast-Netzwerke implementieren einen **Restriktiven Blocking-Ansatz**:

- **Blockiert**: Alle Threat Protection Kategorien (Malware, Phishing, C2, Exploits) — keine Ausnahmen erlaubt
- **Blockiert**: Hochrisiko-Inhaltskategorien (Erwachseneninhalte, illegale Inhalte, Anonymisierer/Proxies)
- **Erlaubt**: Allgemeiner Webzugang für legitime geschäftliche Nutzung

**Coverage**: Alle Gast-Netzwerk-Egress-Punkte SOLLEN Web-Filtering-Kontrollen durchlaufen, bevor sie das Internet erreichen.

**Logging**: Gast-Netzwerk Web-Access-Logging ist aktiviert für Security-Event-Erkennung. Benutzer-Attribution ist beschränkt auf IP/MAC-Adresse (keine persönliche Identifikation) in Übereinstimmung mit Privacy-Anforderungen.

**Exceptions**: Keine Kategorie-Exceptions sind für Gast-Netzwerke erlaubt. Benutzer, die breiteren Zugang benötigen, müssen sich über das Corporate-Netzwerk mit entsprechenden Credentials verbinden.

**Governance**: Gast-Netzwerk-Filtering-Konfiguration wird durch das Security Team verwaltet und quartalsweise überprüft als Teil des Standard Web-Filtering Assessment-Zyklus (ISMS-IMP-A.8.23-3).

---

# Freigabe-Protokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Chief Information Security Officer (CISO)** | [Name] | [Datum] |
| **Chief Information Officer (CIO)** | [Name] | [Datum] |
| **Legal/Compliance Officer** | [Name] | [Datum] |
| **Geschäftsleitung (GL)** | [Name] | [Datum] |

---

**ENDE DES RICHTLINIEN-DOKUMENTS**

---

*Diese Richtlinie definiert Anforderungen. Implementierungs-Prozeduren sind dokumentiert in ISMS-IMP-A.8.23.*
<!-- QA_VERIFIED: 2026-03-01 -->
