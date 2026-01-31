# ISMS-POL-A.8.17 — Zeitsynchronisation

---

## Dokumentenlenkung

| Feld | Wert |
|------|------|
| **Dokumenten Titel** | Zeitsynchronisation |
| **Dokumententyp** | Konzept |
| **Dokument-ID** | ISMS-POL-A.8.17 |
| **Dokumenteneigentümer/in** | Chief Information Security Officer (CISO) |
| **Freigabe durch** | Geschäftsleitung (GL) |
| **Erstellt** | [Date] |
| **Version** | 1.0 |
| **Versionsdatum** | [Date] |
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
- ISMS-IMP-A.8.17 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Control A.8.17
- ISMS-POL-A.8.21 (Network Services Security)
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)

---

## Management Summary

Diese Richtlinie definiert die Anforderungen von [Organisation] für Zeitsynchronisation über alle informationsverarbeitenden Systeme hinweg, um Log-Korrelation, forensische Analysen und zuverlässige Audit Trails gemäss ISO/IEC 27001:2022 Control A.8.17 zu ermöglichen.

**Geltungsbereich**: Diese Richtlinie gilt für alle informationsverarbeitenden Systeme, die Logs generieren oder an sicherheitsrelevanten Operationen teilnehmen, einschliesslich Servern, Netzwerkgeräten, Security-Systemen und Cloud-Instanzen.

**Zweck**: Definition organisatorischer Anforderungen für Implementierung und Governance von Zeitsynchronisations-Kontrollen. Diese Richtlinie definiert WAS Zeitsynchronisation erforderlich ist und WER verantwortlich ist. Implementierungsprozeduren (WIE) sind separat in ISMS-IMP-A.8.17 dokumentiert.

**Regulatorisches Alignment**: Diese Richtlinie adressiert obligatorische Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatory Applicability Framework), einschliesslich Schweizer nDSG, EU DSGVO und ISO/IEC 27001:2022. Konditionale branchenspezifische Anforderungen (PCI DSS, FINMA, DORA, NIS2) gelten, wo Geschäftsaktivitäten der [Organisation] Anwendbarkeit auslösen.

---

## 1. Control Alignment & Geltungsbereich

### 1.1 ISO/IEC 27001:2022 Control A.8.17

**ISO/IEC 27001:2022 Annex A.8.17 - Zeitsynchronisation**

> *Die Uhren informationsverarbeitender Systeme, die von der Organisation verwendet werden, sollen mit genehmigten Zeitquellen synchronisiert werden.*

**Control-Zielsetzung**: Etablierung organisatorischer Richtlinie für Zeitsynchronisation um sicherzustellen, dass alle Systeme akkurate, synchronisierte Zeitstempel für Log-Korrelation, forensische Analysen, Authentifizierung und Compliance-Zwecke bereitstellen.

**Diese Richtlinie adressiert**:
- Anforderungen an autoritative Zeitquellen und interne NTP-Infrastruktur
- Systemkonfigurationsanforderungen für Zeitsynchronisation
- Akzeptable Zeitabweichungs-Schwellenwerte (Time Drift Thresholds)
- Monitoring und Berichterstattung für Synchronisationsstatus
- Organisatorische Rollen und Verantwortlichkeiten für NTP-Governance
- Frameworks für Exception Management und Incident Management
- Integration mit Logging, Monitoring und Security Operations

### 1.2 Was diese Richtlinie tut

Diese Richtlinie:
- **Definiert** Anforderungen an Zeitquellen und NTP-Infrastruktur
- **Etabliert** akzeptable Zeitabweichungs-Schwellenwerte basierend auf System-Kritikalität
- **Spezifiziert** Monitoring-Anforderungen für Zeitsynchronisationsstatus
- **Etabliert** Governance-Framework für Zeitsynchronisations-Management
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

### 1.3 Was diese Richtlinie NICHT tut

Diese Richtlinie tut NICHT:
- **Spezifizieren technischer NTP-Server-Konfigurationen** (siehe ISMS-IMP-A.8.17-S1 Time Source Configuration)
- **Bereitstellen plattformspezifischer Synchronisations-Prozeduren** (siehe ISMS-IMP-A.8.17-S2 Synchronization Verification)
- **Definieren spezifischer NTP-Technologien** (chrony, ntpd, W32Time, Cloud Time Services)
- **Auswählen von Zeitquellen-Anbietern** (NIST, Cloudflare, NTP Pool, GPS - basierend auf organisatorischem Assessment)
- **Ersetzen von Risk Assessment** (Zeitabweichungs-Schwellenwerte basierend auf System-Kritikalität und Risk Treatment)

**Rationale**: Trennung von Richtlinienanforderungen und Implementierungsleitlinien ermöglicht:
- Richtlinienstabilität trotz sich entwickelnder NTP-Technologien
- Technische Agilität für Plattform-Updates ohne Richtlinienrevision
- Klare Unterscheidung zwischen Governance (Richtlinie) und Execution (Implementierung)

### 1.4 Geltungsbereich

**Diese Richtlinie gilt für**:
- Alle Server (physisch, virtuell, Cloud) die sicherheitsrelevante Logs generieren
- Alle Netzwerkgeräte (Router, Switches, Firewalls, Load Balancers)
- Alle Security-Systeme (SIEM, IDS/IPS, Authentifizierungsserver, Zertifikatsautoritäten)
- Alle Datenbanksysteme mit Audit-Anforderungen
- Alle Systeme in Security Operations Center (SOC) Scope
- Cloud-Instanzen und Container-Hosts mit Logging-Anforderungen

**Ausschlüsse**:
- Nicht-vernetzte Standalone-Systeme ohne Logging-Anforderungen
- IoT-Geräte ohne Audit-Trail-Anforderungen (sofern durch Risk Assessment ausgeschlossen)
- Systeme in vollständig isolierten Air-Gapped-Umgebungen (unterliegen speziellen Zeitquellen-Anforderungen)

### 1.5 Regulatorisches Applicability Framework

Gemäss ISMS-POL-00 (Regulatory Applicability Framework) sind regulatorische Anforderungen in drei Kategorien unterteilt:

**Tier 1 - Mandatory Compliance** (alle gelten):
- **Schweizer nDSG Art. 8** - Anforderungen an Datensicherheit, Logging und Audit Trails
- **EU DSGVO Art. 32** - Anforderungen an Logging und Monitoring zur Gewährleistung von Security of Processing
- **ISO/IEC 27001:2022 A.8.17** - Kontrolle für Clock Synchronization

**Tier 2 - Conditional Applicability** (gelten, wo ausgelöst):
- **PCI DSS Req. 10.4** - Time-Synchronization Technology (gilt, wenn Kartenzahlungen verarbeitet werden)
- **FINMA Rundschreiben 2023/1** - Logging-Anforderungen für Finanzinstitute (gilt bei Finanzdienstleistungen)
- **DORA Art. 21** - Logging und ICT-Risikomonitoring für Finanzentitäten (gilt bei Finanzdienstleistungen)
- **NIS2 Art. 21** - Anforderungen an Incident Logging für wesentliche/wichtige Entitäten (gilt bei kritischer Infrastruktur)

**Tier 3 - Informational Reference / Best Practice**:
- **NIST SP 800-53 (AU-8)** - Time Stamps für Audit Records
- **CIS Controls v8 (Control 8)** - Audit Log Management
- **RFC 5905** - Network Time Protocol Version 4 Spezifikation
- **NIST Time Services** - time.nist.gov technische Leitlinien

**Compliance-Bestimmung**: [Organisation] bestimmt anwendbare Tier-2-Regulations durch periodisches Business Activity Assessment. Die strengsten Anforderungen gelten, wo mehrere Regulations überlappen.

---

## 2. Clock Synchronization Requirements Framework

### 2.1 Anforderungen an Autoritative Zeitquellen (Obligatorisch)

[Organisation] unterhält Zugang zu autoritativen Zeitquellen um akkurate Referenzzeit für alle Informationssysteme bereitzustellen.

**Erforderliche Zeitquellen**:

| Anforderungs-Kategorie | Spezifikation | Implementierungs-Priorität |
|------------------------|---------------|---------------------------|
| **Redundanz** | Minimum ZWEI (2) autoritative Zeitquellen | **Obligatorisch** |
| **Stratum-Level** | Stratum 0 oder Stratum 1 Quellen | **Obligatorisch** |
| **Verfügbarkeit** | >99.9% Uptime für jede Quelle | **Obligatorisch** |
| **Geografische Diversität** | Quellen aus verschiedenen Standorten wo praktikabel | Empfohlen |
| **Vertrauenswürdige Anbieter** | Regierungs-, akademische oder renommierte kommerzielle Services | **Obligatorisch** |

**Primäre Zeitquellen (Stratum 0/1 erforderlich)**:
- GPS-basierte Zeitserver (Stratum 0/1)
- NIST-Zeitserver (time.nist.gov)
- Nationale/regionale Regierungs-Zeitservices
- Organisations-eigene Atomuhr oder GPS-Empfänger

**Ergänzende/Backup-Quellen (Stratum 2+ akzeptabel)**:
- NTP Pool Project Server (pool.ntp.org)
- Cloud-Provider-Zeitservices (AWS Time Sync, Azure NTP, GCP NTP)

**Hinweis**: Interne NTP-Infrastruktur MUSS mit mindestens zwei primären (Stratum 0/1) Quellen synchronisieren. NTP Pool und Cloud-Provider-Services können als ergänzende Quellen für Redundanz dienen, SOLLEN aber NICHT die einzige autoritative Referenz sein.

**Implementierungs-Hinweis**: Spezifische Zeitquellen-Auswahl, -Konfiguration und Verfügbarkeitsmonitoring-Prozeduren sind in ISMS-IMP-A.8.17-S1 (Time Source Configuration) definiert.

### 2.2 Interne Zeitsynchronisations-Infrastruktur (Obligatorisch)

[Organisation] deployed interne NTP-Infrastruktur um Zeitsynchronisations-Services für alle Client-Systeme bereitzustellen.

**Interne NTP-Infrastruktur-Anforderungen**:

| Anforderungs-Kategorie | Spezifikation | Implementierungs-Priorität |
|------------------------|---------------|---------------------------|
| **Redundanz** | Minimum ZWEI (2) interne NTP-Server | **Obligatorisch** |
| **Stratum-Level** | Stratum 2 (synchronisiert zu externen Stratum 1 Quellen) | **Obligatorisch** |
| **Geografische Verteilung** | NTP-Server über Rechenzentren/Standorte verteilt wo anwendbar | Empfohlen |
| **High Availability** | Automatisches Failover zwischen NTP-Servern | **Obligatorisch** |
| **Monitoring** | Kontinuierliches Monitoring mit automatisiertem Alerting | **Obligatorisch** |
| **Alerting-Konfiguration** | Automatische Benachrichtigung bei NTP-Infrastruktur-Ausfall oder Synchronisationsfehlern | **Obligatorisch** |

**NTP-Server-Anforderungen**:
- Synchronisation mit mindestens zwei externen autoritativen Zeitquellen
- Peer-Konfiguration mit anderen internen NTP-Servern für Konsistenz
- Zeitsynchronisations-Service per ISMS-POL-A.8.21 (Network Services Security) gesichert
- UDP Port 123 Traffic-Filterung und Access Control konfiguriert

**Implementierungs-Hinweis**: Spezifische NTP-Server-Deployment, -Konfiguration und -Management-Prozeduren sind in ISMS-IMP-A.8.17-S1 (Time Source Configuration) definiert.

### 2.3 Systemsynchronisations-Anforderungen (Obligatorisch)

Alle in-scope Systeme MÜSSEN für Zeitsynchronisation zu genehmigten internen NTP-Servern konfiguriert sein.

**Systemkonfigurations-Anforderungen**:

| Anforderungs-Kategorie | Spezifikation | Implementierungs-Priorität |
|------------------------|---------------|---------------------------|
| **NTP-Server-Zuweisung** | Primärer und sekundärer NTP-Server konfiguriert | **Obligatorisch** |
| **Automatische Korrektur** | Automatische Zeitkorrektur aktiviert (keine manuellen Eingriffe) | **Obligatorisch** |
| **Maximale Zeitabweichung** | Siehe Schwellenwert-Tabelle unten | **Obligatorisch** |
| **Synchronisationsstatus-Logging** | Zeit-Synchronisationsstatus und -änderungen geloggt | **Obligatorisch** |
| **Verifizierung** | Synchronisationsstatus verifiziert innerhalb von 7 Tagen für Compliance-Metriken, 30 Tage Maximum für Policy-Compliance | **Obligatorisch** |

**Maximale Akzeptable Zeitabweichung (Time Drift Thresholds)**:

| System-Kategorie | Target (Operational) | Compliance Threshold (Maximum) | Anwendbar auf |
|------------------|---------------------|--------------------------------|---------------|
| **Allgemeine Systeme** | <500 Millisekunden | ±1 Sekunde | Standard-Server, Workstations, nicht-kritische Netzwerkgeräte |
| **Kritische Security-Systeme** | <50 Millisekunden | ±100 Millisekunden | SIEM, Authentifizierungsserver, Zertifikatsautoritäten, IDS/IPS |
| **High-Precision-Anforderungen** | <5 Millisekunden | ±10 Millisekunden | Finanztransaktionssysteme, regulatorische Compliance-Systeme |

**Definitionen**:
- **Target**: Operationales Ziel, das gesunden Zustand indiziert
- **Compliance Threshold**: Maximal akzeptabler Wert per Section 2.3; Überschreitungen erfordern Remediation

**Spezialfälle**:

**Cloud-Systeme**:
- Cloud-Provider-Zeitservices (AWS Time Sync, Azure NTP, GCP NTP) sind akzeptabel wo von vertrauenswürdigem Provider bereitgestellt
- Zeitabweichungs-Monitoring bleibt verpflichtend
- Verifizierung der Cloud-Time-Service-Konfiguration erforderlich

**Air-Gapped Systeme**:
- Erfordern GPS-basierte Zeitquelle oder organisations-eigene Stratum 1 Zeitquelle
- Exception-Prozess erforderlich, falls kein GPS-Zugang verfügbar

**IoT/Embedded Devices**:
- Können SNTP (Simplified Network Time Protocol) verwenden
- Unterliegen denselben Zeitabweichungs-Anforderungen basierend auf Funktionalität

**Implementierungs-Hinweis**: Plattformspezifische NTP-Client-Konfigurationsprozeduren (Linux, Windows, Netzwerkgeräte, Cloud-Plattformen) sind in ISMS-IMP-A.8.17-S1 (Time Source Configuration) definiert.

### 2.4 Synchronisationsverifizierungs-Anforderungen (Obligatorisch)

[Organisation] verifiziert dass alle Systeme aktiv mit genehmigten Zeitquellen synchronisieren.

**Verifizierungs-Anforderungen**:

| Anforderungs-Kategorie | Spezifikation | Frequenz |
|------------------------|---------------|----------|
| **Synchronisationsstatus-Prüfung** | Verifizierung dass System mit genehmigtem NTP-Server synchronisiert | Monatlich (minimum) |
| **Zeitabweichungs-Messung** | Messung aktueller Zeitabweichung vs. autoritative Quelle | Monatlich (minimum) |
| **Synchronisationsausfall-Erkennung** | Automatisiertes Monitoring mit Alerting für Synchronisationsausfälle | Kontinuierlich |
| **Compliance-Assessment** | Dokumentiertes Assessment von systemweitem Synchronisationsstatus | Monatlich |
| **Verifizierungs-Zeitrahmen** | Sync-Status verifiziert innerhalb 7 Tage für Compliance-Metriken, 30 Tage Maximum für Policy-Compliance | Gemäss Kategorie |

**Verifizierungs-Methodik**:
- Plattformspezifische Verifizierungs-Commands (chronyc tracking, ntpq -p, w32tm /query /status)
- Automatisierte Sync-Status-Collection via Configuration Management oder Monitoring-Systeme
- Regelmässige System-Inventar-Abgleiche mit Asset Management (ISMS-POL-A.5.9)

**Implementierungs-Hinweis**: Detaillierte Verifizierungsprozeduren, plattformspezifische Commands und Assessment-Templates sind in ISMS-IMP-A.8.17-S2 (Synchronization Verification Process) definiert.

---

## 3. Governance & Operations

### 3.1 Rollen & Verantwortlichkeiten

**Chief Information Security Officer (CISO)**:
- Rechenschaftlichkeit für diese Policy und Clock Synchronization Compliance
- Genehmigung technischer Exceptions (alternative NTP-Server, spezifische Systemkonfigurationen)
- Quartalsweise Review von Exception Status und Compliance-Metriken
- Eskalation von Compliance-Ausfällen an Executive Management

**Network Operations Manager**:
- Deployment und Maintenance der internen NTP-Server-Infrastruktur
- Auswahl und Konfiguration externer autoritativer Zeitquellen
- NTP-Infrastruktur-Monitoring und Performance-Tuning
- Koordination mit Anbietern für GPS/Atomuhr-Zeitquellen wo anwendbar

**IT Operations / System Administrators**:
- Konfiguration von Client-Systemen für Zeitsynchronisation
- Verifizierung von Synchronisationsstatus per Verifizierungs-Schedule
- Investigation und Remediation von Synchronisationsausfällen
- Dokumentation von Systemkonfigurationen in Asset Management

**Cloud Platform Teams**:
- Konfiguration von Cloud-Instanzen für Zeitservices (AWS Time Sync, Azure NTP, GCP NTP)
- Verifizierung Cloud-Platform-Zeitsynchronisation funktioniert korrekt
- Integration Cloud-Zeitservices mit organisatorischem NTP-Monitoring

**Security Operations Center (SOC)**:
- Monitoring Zeitsynchronisationsstatus für security-kritische Systeme
- Investigation Synchronisationsausfälle die Security Operations beeinträchtigen
- Eskalation infrastrukturweiter Sync-Ausfälle
- Validierung Timestamp-Konsistenz während Security Investigations und Incident Response

**Information Security / ISMS Officer**:
- Maintenance dieser Policy und zugehöriger Implementation Guidance
- Durchführung monatlicher Systemsynchronisationsstatus-Assessments
- Generierung Compliance-Dashboards und Reports
- Tracking Remediation identifizierter Gaps und Non-Compliance
- Präsentation Compliance-Status an CISO und Management
- Koordination mit Auditoren für Evidence Provision

**System Owners**:
- Definition spezifischer Drift-Schwellenwerte für eigene Systeme (innerhalb Policy-Limits)
- Akzeptanz dokumentierter Risiken für Systeme ausgeschlossen von Zeitsynchronisations-Anforderungen
- Genehmigung Remediation Plans für Synchronisationsausfälle eigene Systeme betreffend
- Review Assessment Findings und Compliance-Status für eigene Systeme

**Verantwortlichkeits-Matrix**:

| Aktivität | CISO | Network Ops | IT Ops | System Owners | ISMS Officer | SOC |
|-----------|------|-------------|--------|---------------|--------------|-----|
| Policy-Genehmigung | A | C | I | I | R | I |
| NTP-Infrastruktur-Deployment | I | A/R | C | I | I | I |
| Client-Systemkonfiguration | I | C | A/R | C | I | I |
| Synchronisations-Monitoring | I | R | R | I | C | A |
| Compliance-Assessment | R | C | C | I | A | C |
| Exception-Genehmigung | A | I | I | R | C | I |
| Incident Response | C | R | R | I | C | A |

Legende: A = Accountable (Rechenschaftspflichtig), R = Responsible (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### 3.2 Monitoring & Reporting

**Monitoring-Anforderungen**:

[Organisation] monitored Zeitsynchronisation um sicherzustellen:
- Alle in-scope Systeme unterhalten aktive Synchronisation zu genehmigten Zeitquellen
- Zeitabweichung bleibt innerhalb akzeptabler Schwellenwerte definiert in Section 2.3
- NTP-Infrastruktur-Verfügbarkeit und -Performance erfüllt Service-Anforderungen
- Synchronisationsausfälle werden prompt erkannt und darauf reagiert

**Key Metrics**:

| Metrik | Target | Compliance Threshold | Anwendbar auf |
|--------|--------|---------------------|---------------|
| **Synchronizations-Compliance** | ≥98% | ≥95% | Alle in-scope Systeme |
| **Average Time Drift** | <500ms | <1 Sekunde | Allgemeine Systeme |
| **Critical System Drift** | <50ms | <100ms | Security-kritische Systeme |
| **Critical System Compliance** | 100% | 100% | SIEM, Authentifizierung, Zertifikatssysteme |
| **Infrastruktur-Verfügbarkeit** | >99.9% | >99.5% | Interne NTP-Server |

**Definitionen**:
- **Target**: Operationales Ziel, das gesunden Zustand indiziert
- **Compliance Threshold**: Maximal akzeptabler Wert per Section 2.3; Überschreitungen erfordern Remediation
- **Synchronizations-Compliance**: Prozentsatz in-scope Systeme mit verifiziertem Synchronisationsstatus innerhalb letzter 7 Tage zeigend Drift innerhalb anwendbarem Schwellenwert für System-Kategorie

**Rationale für 95% Compliance Threshold**: Dieser Schwellenwert berücksichtigt dass transiente Synchronisationsausfälle während Wartungsfenstern, System-Reboots und Netzwerkstörungen auftreten. Systeme unter Schwellenwert werden für Remediation getrackt. Persistente Non-Compliance (>30 Tage) triggert Eskalation unabhängig vom Gesamt-Prozentsatz.

**Reporting**:
- **Frequenz**: Monatliche Compliance-Reports, quartalsweise Executive Summaries
- **Publikum**: CISO (monatlich), Executive Management (quartalsweise), IT Operations (kontinuierliches Monitoring)
- **Format**: Compliance-Dashboard zeigend Sync-Status, Drift-Metriken, Gaps und Remediation Tracking
- **Eskalation**: Sofortige Benachrichtigung für critical System Sync Failures, Infrastruktur-Ausfälle oder Compliance fallend unter 90%

**Detaillierte Prozeduren**: ISMS-IMP-A.8.17-S2 (Synchronization Verification Process) bietet Monitoring-Konfiguration, Verifizierungsprozeduren, Metrik-Berechnungen und Reporting-Templates.

### 3.3 Exception Management

**Exception Request Anforderungen**:

Exceptions von Clock Synchronization Policy Anforderungen erfordern:
- Dokumentierte Business- oder technische Justifikation (z.B. air-gapped System ohne GPS, Vendor-Limitation)
- Risk Assessment (Likelihood und Impact inakkurater Zeit, Residual Risk)
- Kompensierende Kontrollen wo machbar (manuelle Zeitverifizierung, Log-Isolation, reduziertes Logging)
- Timeline für Erreichen voller Compliance (falls temporäre Exception)
- Formale Genehmigung per Authority Matrix

**Genehmigungsautorität**:
- **Technische Exceptions** (spezifische Systemkonfigurationen, alternative Zeitquellen): CISO-Genehmigung
- **Policy-Level-Exceptions** (Requirement Waiver, permanenter Ausschluss): Executive Management Genehmigung
- **Maximale Dauer**: 12 Monate für temporäre Exceptions
- **Renewal**: Erfordert aktualisiertes Risk Assessment und Justifikation

**Exception Reassessment**: Exception Renewals erfordern Reassessment gegen aktuelle Policy-Anforderungen, nicht nur fortgesetzte Justifikation ursprünglicher Umstände. Falls Policy-Anforderungen, Risk Landscape oder technische Capabilities sich seit Original-Genehmigung geändert haben, muss Exception re-evaluiert werden für fortgesetzte Angemessenheit. Exceptions granted innerhalb 90 Tagen des jährlichen Policy Review SOLLEN für explizites Reassessment während dieses Review Cycle geflaggt werden.

**Kompensierende Kontrollen** für excepted Systeme können einschliessen:
- Manuelle Zeitverifizierungs-Prozeduren mit dokumentierter Frequenz
- Log-Isolation (nicht korreliert mit anderen Systemen für forensische Analyse)
- Reduzierte Log-Retention oder keine Logging-Anforderung
- Risk Acceptance Dokumentation Limitations bestätigend

**Monitoring**: Aktive Exceptions reviewed quartalsweise durch CISO. Kompensierende Control Effectiveness verifiziert. Exceptions widerrufen falls Risk Profile sich ändert, kompensierende Controls fehlschlagen oder Compliance machbar wird.

**Exception Template**: ISMS-IMP-A.8.17 Exception Request Form bietet standardisiertes Dokumentationsformat und Workflow.

### 3.4 Incident Response

**Clock Synchronization Security Incidents** einschliessen:
- Weitverbreitete Synchronisationsausfälle mehrere Systeme oder kritische Infrastruktur betreffend
- Excessive Time Drift auf security-kritischen Systemen (SIEM, Authentifizierungsserver, Zertifikatsautoritäten)
- NTP-Infrastruktur-Kompromittierung oder verdächtige böswillige Zeitmanipulation
- Zeitquellen-Unerreichbarkeit oder Redundanzverlust
- Systeme persistent ausfallend zu synchronisieren trotz Remediation Efforts

**Response Prozess**:
1. **Erkennung & Reporting**: Monitoring-Systeme generieren Alerts; SOC oder IT Operations sofort benachrichtigt
2. **Assessment**: Incident Severity Classification (Critical, High, Medium, Low) basierend auf betroffenen Systemen und Security Impact
3. **Investigation**: Root Cause Analysis (NTP-Server-Ausfall, Network Connectivity, Misconfiguration, Infrastruktur-Issue)
4. **Containment**: Sofortmassnahmen basierend auf Incident Type (Failover zu Backup NTP, Service Restore, isolate betroffene Systeme)
5. **Recovery**: Systemwiederherstellung, Konfigurationskorrektur und Verifizierung Synchronisationsstatus
6. **Post-Incident**: Lessons Learned, Control Improvements und preventive Massnahmen

**Critical Incidents**: 
- Synchronisationsausfälle auf security-kritischen Systemen (SIEM, Authentifizierung) behandelt als **High-Priority Incidents** erfordern sofortige Response
- Infrastrukturweite Ausfälle eskaliert zu IT Management und CISO innerhalb 1 Stunde
- Verdächtige Zeitmanipulation eskaliert zu SOC für Security Investigation

**Response Timeframes**:
- **Critical Systems**: Investigation innerhalb 1 Stunde, Remediation Plan innerhalb 4 Stunden, Resolution innerhalb 24 Stunden
- **Standard Systems**: Investigation innerhalb 4 Business Hours, Remediation Plan innerhalb 1 Business Day, Resolution innerhalb 3 Business Days

**NTP-Infrastruktur-Klassifizierung**: Interne NTP-Server und autoritative Zeitquellen-Konnektivität sind klassifiziert als kritische Infrastruktur. Ausfälle NTP-Infrastruktur betreffend folgen Critical System Response Timeframes:
- Investigation innerhalb 1 Stunde
- Remediation Plan innerhalb 4 Stunden
- Resolution innerhalb 24 Stunden

Infrastruktur-Ausfälle werden eskaliert zu IT Management und CISO sofort bei Erkennung due zu kaskadierendem Impact auf alle abhängigen Systeme.

**Detaillierte Prozeduren**: ISMS-IMP-A.8.17-S2 (Synchronization Verification Process) bietet Incident Classification Criteria, Response Workflows, Eskalationsprozeduren und Koordination mit Endpoint Security und Infrastructure Teams.

### 3.5 Policy Governance

**Policy Review**:
- **Frequenz**: Jährlich (oder bei signifikanten Änderungen in NTP-Technologie, Threat Landscape oder regulatorischen Anforderungen)
- **Owner**: Chief Information Security Officer (CISO)
- **Prozess**: Formaler Review einschliesslich Stakeholder Input, Regulatory Update Assessment, Technology Evolution Review

**Policy Maintenance**:
- Minor Updates (klarifizierende Language, Contact Updates): CISO-Genehmigung
- Major Updates (neue Requirements, Scope Changes): Executive Management Genehmigung
- Emergency Updates (kritische Security Issues): CISO mit nachfolgender Executive Ratification

**Training & Awareness**:
- Neues Personal: Policy Awareness im Rahmen von Security Onboarding
- Technisches Personal (Network Ops, System Admins): Detailliertes Training auf Implementation Guidance
- Jährliche Awareness-Kampagne für alle Mitarbeiter betonend Importance akkurater Zeitstempel

---

## 4. Implementierung & Referenzen

### 4.1 Integration mit ISMS

Diese Policy integriert mit folgenden ISMS Komponenten:

**ISO/IEC 27001:2022 Clause 5 (Leadership)**:
- Clause 5.3 - CISO accountable für Policy und Compliance per Verantwortlichkeits-Matrix

**ISO/IEC 27001:2022 Clause 6 (Planning)**:
- Clause 6.1 - Risk Assessment informiert Zeitabweichungs-Schwellenwerte und Exception Decisions
- Clause 6.2 - Security Objectives einschliessen Zeitsynchronisations-Compliance-Ziele

**ISO/IEC 27001:2022 Clause 8 (Operation)**:
- Clause 8.1 - Operationelle Prozesse definiert in ISMS-IMP-A.8.17 Implementation Guidance

**ISO/IEC 27001:2022 Clause 9 (Performance Evaluation)**:
- Clause 9.1 - Monitoring-Requirements definiert in Section 3.2

**Related Annex A Controls**:
- **A.8.21 (Network Services Security)**: Sichert NTP-Infrastruktur und Zeit-Services gegen Attacks
- **A.8.15 (Logging)**: Ermöglicht durch synchronisierte Zeitstempel über Systeme hinweg
- **A.8.16 (Monitoring Activities)**: Einschliessen Zeitsynchronisations-Status-Monitoring
- **A.5.9 (Inventory of Assets)**: Bietet System-Liste für Zeitsynchronisations-Assessment
- **A.8.9 (Configuration Management)**: Verwaltet NTP-Client-Konfigurationen
- **A.5.28 (Collection of Evidence)**: Erfordert zeitlich synchronisierte Logs für forensische Analysen

### 4.2 Implementation Resources

**Implementation Guidance verfügbar in**:
- **ISMS-IMP-A.8.17-S1** (Time Source Configuration):
  - Auswahl externer autoritativer Zeitquellen (NIST, NTP Pool, Cloudflare, GPS)
  - Deployment interner NTP-Server (Redundanz, High Availability, Geographic Distribution)
  - NTP-Server-Konfiguration (chrony, ntpd, W32Time)
  - Client-Systemkonfigurationen (Linux, Windows, Netzwerkgeräte, Cloud-Plattformen)
  - Cloud-Zeitservices (AWS Time Sync, Azure NTP, GCP NTP)
  - Spezialfälle (Container, IoT, air-gapped Systeme)

- **ISMS-IMP-A.8.17-S2** (Synchronization Verification Process):
  - Plattformspezifische Verifizierungs-Commands (chronyc, ntpq, w32tm)
  - Zeitabweichungs-Messmethodik
  - Automatisierte Sync-Status-Collection-Ansätze
  - Alert-Konfiguration für Synchronisationsausfälle
  - Periodische Verifizierungs-Schedules
  - Gap Identification und Remediation Tracking

### 4.3 Regulatory Mapping

Diese Policy adressiert folgende regulatorische Anforderungen:

| Regulation | Requirement | Wie adressiert |
|------------|-------------|----------------|
| **Schweizer nDSG Art. 8** | Datensicherheit, Logging und Audit Trails | Synchronisierte Zeitstempel ermöglichen akkurate Logs und Audit Trails |
| **EU DSGVO Art. 32** | Logging und Monitoring | Zeitsynchronisation ermöglicht konsistente Logging und Security Monitoring |
| **ISO 27001:2022 A.8.17** | Clock Synchronization | Direkt implementiert durch diese Policy |
| **PCI DSS Req. 10.4** | Time-Synchronization Technology | NTP-Infrastruktur-Anforderungen und Zeitabweichungs-Schwellenwerte |
| **FINMA/DORA/NIS2** | Audit Trail Integrity, Logging Capability | Zeitstempel-Konsistenz für regulatorisches Logging |

**Compliance-Posture**: Diese Policy etabliert Framework für Clock Synchronization Compliance. Tatsächlicher Compliance-Status gemessen durch:
- System Synchronization Status Assessment (monatlich via ISMS-IMP-A.8.17-S2)
- NTP-Infrastruktur-Compliance-Review (quartalsweise)
- Audit Findings und Corrective Actions
- Regulatory Assessment Results

### 4.4 Training & Awareness

**Zielgruppen**:
- **Neues Personal**: Policy Awareness als Teil von Security Onboarding
- **Network Operations**: Detailliertes Training auf NTP-Server-Management
- **System Administrators**: Training auf Client-Systemkonfiguration und Verifizierung
- **Security Operations**: Awareness auf Importance Zeitsynchronisation für Incident Response
- **ISMS Officers**: Training auf Assessment-Prozeduren und Compliance-Reporting

**Training-Materialien**:
- Policy Overview-Präsentation
- Implementation Guidance Workshops
- Platform-spezifische How-To-Guides
- Troubleshooting Playbooks

---

## 5. Definitionen

**Autoritative Zeitquelle**: Stratum 0 oder Stratum 1 Zeitquelle (GPS, Atomuhr, NIST-Server), die primäre Zeitreferenz bereitstellt.

**Compliance Threshold**: Maximal akzeptabler Wert für Metrik; Überschreitung erfordert Remediation.

**NTP (Network Time Protocol)**: Protokoll verwendet für Uhren-Synchronisation zwischen Computer-Systemen über paket-geschaltete, variable-latency Datennetzwerke.

**Stratum**: Distanz von Referenzuhr in NTP-Hierarchie. Stratum 0 = direkte Physik-Referenz (GPS, Atomuhr), Stratum 1 = Computer synchronisiert zu Stratum 0, Stratum 2 = Computer synchronisiert zu Stratum 1, etc.

**Stratum 16**: Unsynchronisierter Zustand - indiziert NTP Sync Failure.

**Target**: Operationales Ziel indizierende gesunden Zustand.

**Zeitabweichung (Time Drift)**: Differenz zwischen System Clock und autoritativer Zeitquelle.

**Zeitsynchronisation**: Prozess koordinierender System-Clocks zu gemeinsamer Zeitreferenz.

---

## Approval Record

| Rolle | Name | Unterschrift | Datum |
|-------|------|--------------|-------|
| **CISO** (Primary Approver) | [Name] | [Unterschrift] | [Datum] |
| **CIO** (Secondary Approver) | [Name] | [Unterschrift] | [Datum] |
| **Legal/Compliance** | [Name] | [Unterschrift] | [Datum] |
| **Executive Management** (Finale Autorität) | [Name] | [Unterschrift] | [Datum] |

**Freigabedatum**: [Datum]  
**Inkrafttretungsdatum**: [Datum]  
**Nächstes Review-Datum**: [Freigabedatum + 12 Monate]

---

**END OF DOCUMENT**
