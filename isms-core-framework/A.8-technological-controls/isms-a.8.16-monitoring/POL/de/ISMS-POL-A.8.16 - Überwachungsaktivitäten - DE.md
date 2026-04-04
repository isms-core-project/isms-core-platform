<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.16-DE:framework:POL:a.8.16 -->
**ISMS-POL-A.8.16 — Richtlinie zu Überwachungsaktivitäten**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Überwachungsaktivitäten |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.16 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstrichtlinie für ISO 27001:2022-Erstzertifizierung |

**Überprüfungsturnus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Operative Überprüfung: Security Operations Center (SOC) Lead
- Compliance: Legal/Compliance Officer
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.8.15 (Protokollierung)
- ISMS-POL-A.5.24-5.28 (Vorfallsmanagement)
- ISMS-IMP-A.8.16.1-UG/TG (Überwachungsinfrastruktur-Assessment)
- ISMS-IMP-A.8.16.2-UG/TG (Basis- und Erkennungs-Assessment)
- ISMS-IMP-A.8.16.3-UG/TG (Abdeckungs-Assessment)
- ISMS-IMP-A.8.16.4-UG/TG (Alarmverwaltungs- und Reaktions-Assessment)
- ISO/IEC 27001:2022 Control A.8.16
- ISO/IEC 27002:2022 Control 8.16

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an Überwachungsaktivitäten zur Erkennung anomalen Verhaltens und potenzieller Informationssicherheitsvorfälle gemäss ISO/IEC 27001:2022 Control A.8.16 fest.

**Anwendungsbereich**: Diese Richtlinie gilt für alle Netzwerke, Systeme und Anwendungen, bei denen Überwachung technisch möglich ist; für alle Nutzer (Mitarbeitende, Auftragnehmer, Dienstkonten); sowie für alle Überwachungstechnologien unabhängig von Anbieter oder Bereitstellungsmodell.

**Zweck**: Definition der organisatorischen Anforderungen an die Implementierung und Steuerung von Überwachungsaktivitäten. Diese Richtlinie legt fest, WAS überwacht werden muss, WO die Überwachung implementiert werden muss und WER verantwortlich ist. Implementierungsverfahren (WIE) sind separat in ISMS-IMP-A.8.16 (UG/TG-Varianten) dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich Swiss nDSG, EU DSGVO und ISO/IEC 27001:2022. Bedingte sektorspezifische Anforderungen (FINMA, DORA, NIS2) gelten, wenn die Geschäftsaktivitäten von [Organisation] deren Anwendbarkeit auslösen.

**Grundsatz**: Wie Richard Feynman weise bemerkte: *„Das erste Prinzip ist, dass man sich selbst nicht täuschen darf – und man selbst ist die Person, die man am leichtesten täuscht."* Dieses Rahmenwerk verhindert **Cargo-Cult-Überwachung** – SIEM-Dashboards, die niemand liest, Alarme, die alle ignorieren, und „Baselines", die reine Schätzungen sind. Echte Überwachung erfordert dokumentierte Baselines, messbare Schwellenwerte, belegte Reaktionsverfahren und quantifizierbare Wirksamkeitskennzahlen.

---

# Steuerungsausrichtung und Anwendungsbereich

## ISO/IEC 27001:2022 Control A.8.16

**ISO/IEC 27001:2022 Anhang A.8.16 – Überwachungsaktivitäten**

> *Netzwerke, Systeme und Anwendungen sollten auf anomales Verhalten überwacht werden, und es sollten geeignete Massnahmen ergriffen werden, um potenzielle Informationssicherheitsvorfälle zu bewerten.*

**Kontrollziel**: Festlegung der organisatorischen Richtlinie für Überwachungsaktivitäten zur Erkennung anormalen Verhaltens und potenzieller Informationssicherheitsvorfälle durch systematische Beobachtung, Baseline-Etablierung, Anomalieerkennung und Integration in Vorfallsmanagementprozesse.

**Diese Richtlinie adressiert**:

- Bestimmung des Überwachungsumfangs (welche Systeme, Netzwerke, Anwendungen zu überwachen sind)
- Baseline-Etablierung für normale Verhaltensmuster
- Anomalieerkennungsfähigkeiten und -methoden
- Anforderungen an Alarmgenerierung, -klassifizierung und -reaktion
- Anforderungen an die Überwachungsinfrastruktur (Tools, Fähigkeiten, Integration)
- Aufbewahrung und Archivierung von Protokolldaten für Compliance und Forensik
- Organisatorische Rollen und Verantwortlichkeiten für die Überwachungssteuerung
- Ausnahme- und Vorfallsmanagement-Rahmenwerke
- Integration mit den Risikobeurteilungs- und Vorfallsreaktionsprozessen von [Organisation]

## Was diese Richtlinie tut

Diese Richtlinie:

- **Definiert** Überwachungskontrollanforderungen ausgerichtet an Datenklassifizierung, Systemkritikalität und regulatorischen Pflichten
- **Etabliert** einen Governance-Rahmen für Überwachungsentscheidungen und Verantwortlichkeit
- **Legt fest** den verbindlichen Überwachungsumfang basierend auf Risikobeurteilung und Geschäftsanforderungen
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00
- **Identifiziert** organisatorische Rollen und Verantwortlichkeiten für Überwachungskontrollen
- **Bietet** einen Rahmen für das Management von Ausnahmen und Überwachungslücken

## Was diese Richtlinie NICHT tut

Diese Richtlinie legt NICHT fest:

- **Technische Überwachungsverfahren** (siehe ISMS-IMP-A.8.16 Implementierungsleitfäden)
- **Spezifische SIEM-Konfigurationen oder Erkennungsregeln** (siehe ISMS-IMP-A.8.16.2 Basis- und Erkennungs-Assessment)
- **Genehmigte Überwachungstools oder Anbieter** (Technologieauswahl basierend auf Risikobeurteilung und technischer Umgebung von [Organisation])
- **Detaillierte Alarm-Reaktions-Playbooks** (siehe ISMS-IMP-A.8.16 Alarm-Reaktionsverfahren)
- **Spezifische Überwachungstechnologien** (Auswahl basierend auf Architektur, Risikoprofil und operativen Bedürfnissen von [Organisation])
- **Risikobeurteilung** (Überwachungskontrollen werden auf Basis der Risikobehandlungsentscheide von [Organisation] ausgewählt)
- **Detaillierte Vorfallsreaktionsverfahren** (siehe ISMS-POL-A.5.24-5.28 Vorfallsmanagement)

**Begründung**: Die Trennung von Richtlinienanforderungen und Implementierungsleitfaden ermöglicht:

- Richtlinienstabilität trotz sich entwickelnder Bedrohungslandschaft und Technologieänderungen
- Technische Agilität für Tool-Updates und Verfeinerung von Erkennungsregeln ohne Richtlinienrevision
- Klare Trennung zwischen Steuerung (Richtlinie) und Ausführung (Implementierung)
- Fokussierter Prüfungsumfang (Prüfer auditieren Richtlinienkonformität, nicht technische Implementierungsdetails)

## Anwendungsbereich

**Diese Richtlinie gilt für**:

- Alle Netzwerksegmente, bei denen Überwachung technisch möglich ist (On-Premises, Cloud, Hybrid, Fernzugang)
- Alle Systeme, die gemäss Risikobeurteilung überwachungspflichtig sind (Server, Workstations, Netzwerkgeräte, Sicherheitsgeräte)
- Alle Anwendungen, die als geschäftskritisch oder sicherheitsrelevant eingestuft sind
- Alle Nutzer mit Zugang zu organisatorischen Ressourcen (Mitarbeitende, Auftragnehmer, Dienstkonten, automatisierte Systeme)
- Alle Überwachungstechnologien unabhängig von Anbieter oder Bereitstellungsmodell (SIEM, IDS/IPS, NDR, EDR, UEBA, Log-Management)
- Alle Drittanbieter mit Zugang zu organisatorischen Systemen oder Daten

**Nicht im Geltungsbereich**:

- Anwendungsleistungsüberwachung für nicht sicherheitsbezogene Zwecke (geregelt durch IT-Betriebsrichtlinien)
- Business Intelligence und Analysen ohne Sicherheitsbezug (geregelt durch Datenanalyserichtlinien)
- Netzwerk-Traffic-Optimierung und Kapazitätsplanung (geregelt durch Netzwerkverwaltungsrichtlinien)
- Überwachung der Mitarbeiterproduktivität (geregelt durch HR-Richtlinien, getrennt von Sicherheitsüberwachung)

**Kritische Systeme mit verbindlicher Überwachungspflicht**:

- Domain Controller und Authentifizierungsinfrastruktur
- Firewalls, VPN-Gateways und Netzwerksicherheitsgeräte
- Datenbankserver mit vertraulichen oder eingeschränkt zugänglichen Daten
- Internetexponierte Webserver und Anwendungen
- E-Mail-Server und Messaging-Infrastruktur
- Dateiserver mit geschäftskritischen oder sensiblen Daten
- Sicherheitsüberwachungsinfrastruktur selbst (SIEM, IDS/IPS, EDR)
- Cloud-Infrastruktur und Plattformdienste (wo [Organisation] Überwachungssichtbarkeit hat)

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Tier 1: Verbindliche Compliance**

| Regulation | Anwendbarkeit | Wesentliche Überwachungsanforderungen |
|------------|---------------|--------------------------------------|
| **Swiss nDSG** | Alle Schweizer Operationen | Art. 8 – Technische und organisatorische Massnahmen einschliesslich Überwachung zum Datenschutz |
| **EU DSGVO** | Bei Verarbeitung personenbezogener EU-Daten | Art. 32 – Sicherheitsmassnahmen einschliesslich Überwachungs- und Erkennungsfähigkeiten |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Control A.8.16 – Dokumentierte Richtlinie, implementierte Kontrollen, Wirksamkeitsnachweise |

**Tier 2: Bedingte Anwendbarkeit**

Nur anwendbar, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulation | Auslösebedingung | Überwachungsanforderungen |
|-----------|------------------|--------------------------|
| **FINMA Circular 2023/1** | Schweizer reguliertes Finanzinstitut | Margin 63–72: Protokollierung, Überwachung und Vorfallserkennung für operative Resilienz |
| **DORA** | EU-Finanzdienstleistungsunternehmen | Art. 17: Erkennung von IKT-bezogenen Vorfällen, Protokollierungs- und Überwachungsfähigkeiten |
| **NIS2** | Wesentliche/wichtige Einrichtung (EU) | Art. 21: Sicherheitsüberwachung, Vorfallserkennung und Reaktionsfähigkeiten |
| **PCI DSS v4.0.1** | Verarbeitung von Zahlungskartendaten | Req. 10: Protokollierung und Überwachung des Zugangs zu Karteninhaberdatenumgebungen |
| **HIPAA** | Verarbeitung von US-Gesundheitsdaten | §164.312(b): Audit-Kontrollen und Überwachung des ePHI-Zugangs |

**Tier 3: Orientierungsleitfäden**

Diese Rahmenwerke informieren die Implementierung, begründen jedoch keine verbindliche Compliance, sofern nicht vertraglich gefordert:

- NIST SP 800-92 (Guide to Computer Security Log Management)
- NIST SP 800-137 (Information Security Continuous Monitoring)
- CIS Controls v8.1 (Control 8: Audit Log Management, Control 13: Network Monitoring and Defense)
- MITRE ATT&CK Framework (Erkennungstaktiken und -techniken)
- SANS Critical Security Controls

**Compliance-Bestimmung**: [Organisation] bestimmt anwendbare Tier-2-Regulierungen durch periodische Geschäftsaktivitätsbeurteilungen, dokumentiert in ISMS-POL-00. Bei Überlappung mehrerer Regulierungen gelten die strengsten Anforderungen.

## Integration ins ISMS

**Integration Risikomanagement (ISO 27001 Abschnitt 6)**:

- Überwachungskontrollen als erkennende Massnahmen in der Defense-in-Depth-Strategie implementiert
- Überwachungslücken durch Risikobeurteilung identifiziert und im Risikoregister dokumentiert
- Risikobehandlungsentscheide bestimmen Überwachungsumfang und Priorität
- Restrisiken aus Überwachungsbeschränkungen verfolgt und von der Leitung akzeptiert

**Verwandte ISMS-Kontrollen**:

| Kontrolle | Integrationspunkt | Überwachungsrolle |
|-----------|-------------------|-------------------|
| **A.5.7** | Threat Intelligence | Überwachung erzeugt Intelligence aus beobachteten Angriffen; Threat Intel informiert Erkennungsregeln |
| **A.5.16** | Identitätsmanagement | User and Entity Behavior Analytics analysiert identitätsbasierte Zugriffsmuster |
| **A.5.24-5.28** | Vorfallsmanagement | Überwachungsalarme lösen Vorfallsreaktionsworkflow aus; Vorfälle informieren Überwachungsverbesserungen |
| **A.8.7** | Malware-Schutz | Malware-Erkennungsalarme fliessen in Überwachung; Überwachung erkennt Malware-Verhaltensmuster |
| **A.8.8** | Schwachstellenmanagement | Überwachung identifiziert Ausnutzungsversuche; priorisiert Patches basierend auf beobachteten Angriffen |
| **A.8.12** | Verhinderung von Datenlecks | Überwachung erkennt Datenexfiltrationsmuster und unerlaubte Datentransfers |
| **A.8.15** | Protokollierung | Überwachung analysiert durch Protokollierungskontrollen erzeugte Protokolldaten |
| **A.8.17** | Zeitsynchronisation | Genaue Zeitstempel sind für Ereigniskorrelation und Zeitlinienrekonstruktion unerlässlich |
| **A.8.20** | Netzwerksicherheit | Netzwerksicherheitskontrollen erzeugen überwachte Ereignisse; Überwachung validiert Kontrollwirksamkeit |
| **A.8.23** | Web-Filterung | Web-Filterprotokolle fliessen als Protokollquelle in Überwachung; Überwachung erkennt webbasierte Bedrohungen |

---

# Überwachungsanforderungsrahmen

## Anforderungen an die Überwachungsinfrastruktur

[Organisation] MUSS eine Überwachungsinfrastruktur mit ausreichenden Fähigkeiten zur Erfassung, Analyse, Speicherung und Massnahmenableitung aus sicherheitsrelevanten Ereignissen implementieren.

### Überwachungsplattform-Fähigkeiten

Überwachungsplattformen (SIEM, IDS/IPS, EDR, NDR, UEBA oder gleichwertig) MÜSSEN bereitstellen:

**Erfassungsfähigkeiten**:

- Mehrquellen-Protokollingest (Syslog, Agenten, APIs, dateibasiert, cloud-nativ)
- Protokollunterstützung für gängige Protokollformate (CEF, LEEF, JSON, XML, Syslog RFC)
- Echtzeit- und Batch-Protokollerfassungsmethoden
- Sichere Protokollübertragung (verschlüsselte Kanäle, authentifizierte Quellen)
- Skalierbare Erfassung zur Unterstützung des Organisationswachstums

**Analysefähigkeiten**:

- Echtzeit-Ereigniskorrelation über mehrere Protokollquellen
- Mustererkennung und signaturbasierte Erkennung
- Statistische Anomalieerkennung (Abweichung von Baselines)
- User and Entity Behavior Analytics (UEBA)
- Integration und Anreicherung mit Threat Intelligence
- Erstellung und Anpassung benutzerdefinierter Erkennungsregeln

**Speicherung und Aufbewahrung**:

- Hot Storage für aktive Überwachung (mindestens 90 Tage Betriebsprotokolle, 12 Monate Sicherheitsalarme)
- Warm/Cold Storage für Compliance und Forensik (Aufbewahrung gemäss regulatorischen Anforderungen)
- Indizierte Suchfähigkeiten für schnelle Untersuchung
- Datenschutz und Integritätsschutz (manipulationssichere Protokollierung)
- Backup und Disaster Recovery für Überwachungsdaten

**Alarmierung und Benachrichtigung**:

- Konfigurierbare Alarmregeln mit Schweregradklassifizierung
- Mehrkanal-Benachrichtigung (E-Mail, SMS, Ticketsystem-Integration, SOAR)
- Alarm-Deduplizierung und -korrelation
- Eskalations-Workflows basierend auf Schweregrad und Reaktionszeit
- Integration mit Vorfallsmanagementsystemen

**Berichterstattung und Dashboards**:

- Echtzeit-Security-Operations-Dashboards
- Executive-Zusammenfassungsberichte (Compliance, KPIs, Trends)
- Compliance-Berichte ausgerichtet auf regulatorische Anforderungen
- Forensische Untersuchungsfähigkeiten (Zeitlinienrekonstruktion, Beweiserfassung)
- Anpassbare Berichte für Stakeholder-Bedürfnisse

### Protokollquellen-Abdeckung

[Organisation] MUSS Protokollquellen überwachen aus:

**Netzwerkinfrastruktur**:

- Firewalls (erlaubter/verweigerter Traffic, Regeländerungen, VPN-Verbindungen)
- Router und Switches (Konfigurationsänderungen, Access Control Lists, Netzwerktopologieänderungen)
- Load Balancer (Trafficzuteilung, Health Checks, SSL-Terminierung)
- VPN-Gateways (Verbindungsversuche, Authentifizierung, Datenübertragung)
- WLAN-Access Points (Client-Assoziierungen, Authentifizierungsfehler, Rogue-AP-Erkennung)
- Intrusion Detection/Prevention Systems (IDS/IPS-Signaturen, blockierte Angriffe)

**Sicherheitsgeräte**:

- Web Application Firewalls (WAF) – HTTP/HTTPS-Traffic, Angriffsversuche, Regelverstösse
- Web-Filter – zugegriffene URL-Kategorien, blockierte Versuche, Richtlinienverstösse
- Data Loss Prevention (DLP) – Datenübertragungsversuche, Richtlinienverstösse, Inhaltsinspektion
- E-Mail-Sicherheitsgateways – Spam, Phishing, Malware, Datenleckage-Versuche
- Endpoint Protection Platforms (EPP/EDR) – Malware-Erkennung, Verhaltensanalyse, Behebungsmassnahmen
- Network Detection and Response (NDR) – Lateral Movement, anomaler Traffic, C2-Kommunikation

**Systeme und Server**:

- Betriebssystemprotokolle (Authentifizierung, Privilege Escalation, Systemfehler, Konfigurationsänderungen)
- Anwendungsprotokolle (Zugang, Fehler, Transaktionen, Sicherheitsereignisse)
- Datenbankprotokolle (Abfragen, Authentifizierung, Schema-Änderungen, sensibler Datenzugang)
- Webserverprotokolle (Zugriffsprotokolle, Fehlerprotokolle, HTTP-Methoden, Antwortcodes)
- Verzeichnisdienste (Active Directory, LDAP) – Authentifizierung, Gruppenänderungen, Richtlinienanpassungen
- Virtualisierungsplattformen (VM-Erstellung/-Löschung, Ressourcenzuweisung, Migrationsereignisse)

**Cloud-Infrastruktur**:

- Cloud-Plattformprotokolle (AWS CloudTrail, Azure Monitor, GCP Cloud Logging)
- Container-Orchestrierung (Kubernetes-Prüfprotokolle, Pod-Ereignisse, RBAC-Änderungen)
- Serverlose Funktionsausführungen (Aufrufe, Fehler, Ressourcenverbrauch)
- Cloud-Speicherzugriff (Bucket-Zugriff, Objekt-Downloads, Berechtigungsänderungen)
- Identity and Access Management (IAM-Richtlinienänderungen, Rollenzuweisungen, Authentifizierungsereignisse)

### Überwachungsabdeckungs-Assessment

[Organisation] MUSS:

- Alle kritischen Systeme und ihren Überwachungsstatus dokumentieren (ISMS-IMP-A.8.16.3 Abdeckungs-Assessment)
- Überwachungsabdeckungsprozentsatz berechnen: (Überwachte kritische Systeme / Gesamte kritische Systeme) × 100
- Zielabdeckung: 100 % der Tier-1-Systeme (Kritisch), >80 % der Tier-2-Systeme (Standard)
- Überwachungslücken mit Risikobeurteilung und Behebungszeitplänen identifizieren und dokumentieren
- Abdeckung vierteljährlich und nach wesentlichen Infrastrukturänderungen überprüfen

### Resilienz der Überwachungsinfrastruktur

Überwachungsinfrastruktur MUSS sein:

- **Redundant**: Kein Single Point of Failure bei Protokollerfassung, -speicherung oder -alarmierung
- **Isoliert**: Überwachungssysteme in separaten Netzwerksegmenten, geschützt von überwachten Systemen
- **Gesichert**: Gehärtete Konfigurationen, eingeschränkter Zugang, Multi-Faktor-Authentifizierung erforderlich
- **Überwacht**: Überwachungsinfrastruktur selbst unterliegt Health Checks und Alarmierung
- **Getestet**: Regelmässige Tests von Erkennungsfähigkeiten, Failover-Verfahren, Backup-Wiederherstellung

## Baseline- und Anomalieerkennungsanforderungen

[Organisation] MUSS Baselines für normales Verhalten etablieren und Anomalieerkennungsfähigkeiten konfigurieren.

### Baseline-Grundsatz

**Das Feynman-Prinzip angewendet auf Baselines:**
> *„Wenn man es nicht mit Zahlen messen kann, hat man keine Baseline – sondern eine Meinung."*

**Akzeptable Baseline**:

- ✅ „Benutzerauthentifizierungsrate während der Geschäftszeiten (08:00–18:00 CET): Mittelwert 145 Anmeldungen/Stunde, Std. Abw. 23, 95. Perzentil 189"
- ✅ „Datenbankabfragerate: Baseline 450 Abfragen/Minute ±50, Alarmschwelle 600 Abfragen/Minute (95. Perzentil × 1,3)"

**Nicht akzeptable „Baseline"**:

- ❌ „Normale Authentifizierungsaktivität liegt bei etwa 100–200 Anmeldungen pro Stunde" (ungenau)
- ❌ „Die Datenbank scheint tagsüber ausgelastet zu sein" (subjektiv, nicht messbar)

### Baseline-Etablierungsanforderungen

Baselines MÜSSEN etabliert werden für:

**System-Auslastungs-Baselines**:

- CPU-Auslastung (Mittelwert, Median, Standardabweichung, 95. Perzentil) während Normalzeiten und Spitzenzeiten
- Arbeitsspeicher-Verbrauchsmuster
- Festplatten-E/A und Speicherauslastung
- Netzwerkbandbreitenverbrauch (Eingang/Ausgang)
- Prozess- und Dienst-Ressourcenverbrauch

**Zugriffsmuster-Baselines**:

- Zeitpunkt der Benutzerauthentifizierung (Tageszeit-, Wochentagsmuster)
- Geografische Zugriffsmuster (normale Standorte, Fernzugriffsmuster)
- Zugriffshäufigkeit pro Nutzer/System (tägliche Anmeldungen, Anwendungszugriffsraten)
- Privilegiertezugriffsmuster (Administrator-Anmeldungen, Sudo-Nutzung, Eskalationsanfragen)
- Fehlgeschlagene Authentifizierungsversuche-Baseline (normale Fehlerrate vs. Angriffsindikatoren)

**Anwendungsverhalten-Baselines**:

- Transaktionsvolumen und -zeitpunkte
- API-Aufrufmengen und -muster
- Datenbankabfragemuster
- Dateizugriffs- und -änderungsmuster
- Netzwerkverbindungsmuster (intern, extern, verwendete Protokolle)

### Baseline-Dokumentation

Jede Baseline MUSS dokumentiert werden mit:

- **Identifiziertes System/Asset**: Spezifisches System, Benutzergruppe oder Anwendung
- **Metrik-Definition**: Genaue Beschreibung des Gemessenen
- **Beobachtungszeitraum**: Dauer der Baseline-Etablierung (mindestens 30 Tage, einschliesslich Geschäftszyklen)
- **Statistisches Profil**: Mittelwert, Median, Standardabweichung, 95./99. Perzentil
- **Zeitbewusste Baselines**: Separate Baselines für Geschäftszeiten, Ausserhalb der Geschäftszeiten, Wochenenden, Feiertage bei unterschiedlichen Mustern
- **Ausschlüsse**: Dokumentierte Ausschlüsse (bekannte Wartungsfenster, Vorfälle, Anomalien)
- **Baseline-Gültigkeit**: Wirksamkeitsdatum, Überprüfungsturnus (mindestens vierteljährlich), nächstes Überprüfungsdatum
- **Peer Review** (verbindlich für Tier-1-Kritisch-System-Baselines): Unabhängige Validierung durch SOC Lead oder Security Manager
- **Schwellenwertableitung**: Methodik zur Ableitung von Alarmschwellenwerten aus der Baseline
- **Eigentümer**: Verantwortliche Person für Baseline-Genauigkeit und -Updates

**Hinweis**: Für Nicht-Tier-1-Systeme ist Peer Review empfohlen, aber optional, um den Verwaltungsaufwand zu reduzieren.

Baseline-Dokumentationsvorlage in **Anhang B**.

### Anomalieerkennungsumfang

Überwachungssysteme MÜSSEN konfiguriert werden, um anomales Verhalten zu erkennen, einschliesslich:

**Ungeplantes Systemverhalten**:

- Unerwartete Prozessbeendigung oder Dienstausfälle
- Ungewöhnlicher Ressourcenverbrauch (CPU-Spitzen, Arbeitsspeichererschöpfung, Festplattenspeichererschöpfung)
- Konfigurationsänderungen ausserhalb genehmigter Änderungsfenster
- Nicht autorisierte Software-Installation oder -Ausführung
- Ungewöhnliche Netzwerkverbindungen (neue Ziele, Protokolle, Ports)

**Indikatoren für böswillige Aktivitäten**:

- Bekannte Malware-Signaturen und Verhaltensmuster
- Traffic zu/von bekannten schädlichen IPs, Domains oder Botnetzen (C2-Infrastruktur)
- Exploit-Versuch-Signaturen (Buffer Overflows, Injection-Angriffe, Privilege Escalation)
- Lateral-Movement-Muster (interne Aufklärung, Credential Dumping, Pass-the-Hash)
- Datenexfiltrationsindikatoren (grosse ausgehende Transfers, unerlaubte Cloud-Uploads, DNS-Tunneling)

**Angriffssignaturen**:

- Denial-of-Service-Angriffsmuster (SYN-Floods, UDP-Floods, Anwendungsschichtangriffe)
- Webanwendungsangriffe (SQL-Injection, XSS, CSRF, Directory Traversal)
- Netzwerkscan und -aufklärung (Port-Scans, Schwachstellen-Scans, Ping-Sweeps)
- Brute-Force-Authentifizierungsversuche
- Protokollanomalien und fehlerhafte Anfragen

**Ungewöhnliches Nutzer-/Entitätsverhalten**:

- Zugriffsversuche auf Ressourcen ausserhalb des normalen Umfangs (Privilege-Creep-Erkennung)
- Ungewöhnliche Zugriffszeiten (Anmeldungen um 03:00 Uhr, wenn Benutzer normalerweise 09:00–17:00 arbeitet)
- Geografische Anomalien (Anmeldung aus der Schweiz um 10:00 Uhr, Anmeldung aus China um 10:05 Uhr)
- Gleichzeitige Sitzungen von verschiedenen Standorten (unmögliche Reise)
- Ungewöhnliche Datenzugriffsmuster (Massen-Datei-Downloads, Datenbank-Dumps, Abfragen sensibler Daten)
- Privilege Escalation ausserhalb normaler Arbeitsabläufe
- Deaktivierung von Protokollierung oder Überwachung auf Systemen (Anti-Forensik-Indikatoren)

**Nicht autorisierter Zugriff**:

- Erfolgreiche Authentifizierung mit kompromittierten Zugangsdaten
- Nicht autorisierte Zugriffsversuche auf geschützte Ressourcen
- Privilege Escalation ohne Genehmigung
- Zugriff auf Systeme/Daten ausserhalb der Jobfunktion des Benutzers
- Ausserhalb der Geschäftszeiten auf geschäftskritische Systeme ohne Genehmigung

### Erkennungswirksamkeitsanforderungen

[Organisation] MUSS:

- Erkennungsregeln vierteljährlich mit simulierten Angriffen oder Purple-Team-Übungen testen
- Erkennungswirksamkeitskennzahlen verfolgen: True Positives, False Positives, False Negatives
- Erkennungsraten anstreben: >90 % True-Positive-Rate bei hochschweren Bedrohungen
- False-Positive-Raten anstreben: <20 % bei kritischen Alarmen, <30 % bei hochschweren Alarmen
- Erkennungslücken dokumentieren und kompensierende Kontrollen implementieren
- Erkennungsregeln kontinuierlich zur Verbesserung der Genauigkeit anpassen

## Alarmverwaltungs- und Reaktionsanforderungen

[Organisation] MUSS Alarmverwaltungs- und Reaktionsfähigkeiten implementieren, die eine zeitnahe und wirksame Reaktion auf Sicherheitsereignisse gewährleisten.

### Alarmklassifizierung

Alarme MÜSSEN nach Schweregrad klassifiziert werden:

| Schweregrad | Definition | Reaktionszeit-SLA | Beispiele |
|-------------|------------|-------------------|-----------|
| **Kritisch** | Aktiver Angriff im Gange, unmittelbarer Datenverlust oder vollständige Dienstunterbrechung | 15 Minuten | Ransomware erkannt, aktive Datenexfiltration, Root-Kompromittierung, kritischer Infrastrukturausfall |
| **Hoch** | Erheblicher Sicherheitsvorfall mit Potenzial für grosse Auswirkungen | 1 Stunde | Malware-Infektion, erfolgreiche Privilege Escalation, Zugriff auf sensible Daten durch nicht autorisierten Nutzer, erfolgreicher Brute-Force-Angriff |
| **Mittel** | Sicherheitsbedenken, die Untersuchung erfordern, potenzieller Vorfall | 4 Stunden | Fehlgeschlagene Privilege-Escalation-Versuche, anomale Verhaltensmuster, Richtlinienverstösse, verdächtige Authentifizierungsaktivitäten |
| **Niedrig** | Informationales Ereignis, geringfügiger Richtlinienverstos oder Anomalie mit geringer Auswirkung | 24 Stunden | Geringfügige Konfigurationsabweichungen, Richtlinienverstösse mit niedrigem Schweregrad, informative Sicherheitsereignisse |
| **Informational** | Zur Kenntnis genommen, keine sofortige Massnahme erforderlich | Überprüfung während der Geschäftszeiten | Routinemässige administrative Aktionen, erwartete Sicherheitsereignisse, Compliance-Protokollierung |

### Alarm-Reaktions-SLAs

Für jeden Schweregrad definiert [Organisation]:

- **Bestätigungs-SLA**: Maximale Zeit bis zur Bestätigung des Alarmpempfangs (Bestätigung der SOC-Analyst-Kenntnis)
- **Triage-SLA**: Maximale Zeit für initiale Bewertung (Feststellen, ob Vorfall)
- **Untersuchungs-SLA**: Maximale Zeit für abgeschlossene Untersuchung und Ursachenbestimmung
- **Eindämmungs-SLA**: Maximale Zeit zur Eindämmung aktiver Bedrohungen (bei Kritisch/Hoch)
- **Lösungs-SLA**: Maximale Zeit zur vollständigen Vorfallsauflösung

**Mindest-SLA-Anforderungen**:

| Schweregrad | Bestätigung | Triage | Untersuchung | Eindämmung | Lösung |
|-------------|-------------|--------|--------------|-----------|--------|
| **Kritisch** | 5 Min. | 15 Min. | 2 Stunden | 1 Stunde | 24 Stunden |
| **Hoch** | 15 Min. | 1 Stunde | 8 Stunden | 4 Stunden | 5 Arbeitstage |
| **Mittel** | 1 Stunde | 4 Stunden | 24 Stunden | 24 Stunden | 10 Arbeitstage |
| **Niedrig** | 4 Stunden | 24 Stunden | 5 Arbeitstage | n/a | 20 Arbeitstage |

[Organisation] DARF strengere SLAs basierend auf Risikobereitschaft und operativen Fähigkeiten definieren.

### Alarmbehandlungsverfahren

**Alarm-Triage**:
1. **Validieren**: Feststellen, ob Alarm True Positive oder False Positive ist
2. **Klassifizieren**: Richtigen Schweregrad basierend auf tatsächlichem Risiko zuweisen
3. **Korrelieren**: Verwandte Ereignisse prüfen (gleicher Nutzer, System, Angriffsmuster)
4. **Dokumentieren**: Triage-Ergebnisse, gesammelte Beweise, initiale Beurteilung festhalten
5. **Eskalieren**: An Incident Response eskalieren bei bestätigtem Sicherheitsvorfall

**Eskalationskriterien**:

- Alarm erfüllt Klassifizierung Kritisch oder Hoch
- Mehrere korrelierte Alarme deuten auf koordinierten Angriff hin
- Bestätigte Datenschutzverletzung oder -exfiltration
- Ransomware oder destruktive Malware erkannt
- Kompromittierung kritischer Infrastruktur (Domain Controller, Firewall, SIEM)
- Rechtliche oder regulatorische Meldepflichten ausgelöst
- Benachrichtigung der Geschäftsleitung gemäss Vorfallsmanagementrichtlinie erforderlich

**Behandlung von False Positives**:

- Grund für False Positive dokumentieren (Baseline-Problem, zu sensitive Erkennungsregel, legitime Aktivität falsch kategorisiert)
- Anfrage zur Anpassung der Erkennungsregel an Security Engineering einreichen
- False-Positive-Raten pro Regel und gesamt verfolgen
- Regeln mit hoher FP-Rate vierteljährlich für Anpassung oder Deaktivierung überprüfen

### Alarmoptimierung und -anpassung

[Organisation] MUSS:

- Alarmvolumen und False-Positive-Raten monatlich überprüfen
- Erkennungsregeln anpassen, um False Positives zu reduzieren und gleichzeitig Erkennungsabdeckung beizubehalten
- Regeln mit >40 % False-Positive-Rate nach Untersuchung deaktivieren oder ändern
- Anpassungsentscheide mit Begründung und Genehmigung dokumentieren
- Wirksamkeit von Anpassungen durch Überwachung nach Änderungen validieren
- Balance zwischen Erkennungsabdeckung (Recall) und Alarmrauschen (Precision) herstellen

**Anpassungsmethodik**:
1. Laute Alarme identifizieren (>10 Vorkommnisse/Tag mit <50 % True-Positive-Rate)
2. Grundursache analysieren (schlechte Baseline, zu sensitive Schwelle, normales Aktivitätsmuster)
3. Anpassung vorschlagen (Schwelle anpassen, Erkennungslogik verfeinern, Whitelist-Ausnahmen hinzufügen)
4. Anpassung im Überwachungsmodus testen (FP-Reduzierung ohne Erhöhung der FNs validieren)
5. Anpassung mit Dokumentation implementieren
6. Post-Anpassungs-Wirksamkeit überwachen (FP-Reduzierung validieren, keine Erhöhung verpasster Erkennungen)

## Aufbewahrungs- und Archivierungsanforderungen

[Organisation] MUSS Überwachungsdaten für Compliance, Forensik und operative Anforderungen aufbewahren.

### Aufbewahrungsfristen

**Betriebsprotokolle** (routinemässige Systemaktivitäten, keine Sicherheitsvorfälle):

- **Hot Storage** (indiziert, durchsuchbar, Echtzeitzugang): Mindestens 90 Tage
- **Warm/Cold Storage** (archiviert, langsamerer Abruf): Gesamtaufbewahrung 12 Monate

**Sicherheitsalarme und Vorfälle**:

- **Hot Storage**: Mindestens 12 Monate
- **Langzeitarchiv**: Ausgerichtet an gesetzlichen und regulatorischen Anforderungen

**Compliance-gesteuerte Aufbewahrung**:

- **DSGVO/nDSG**: Aufbewahrung durch berechtigtes Interesse gerechtfertigt, gelöscht wenn nicht mehr benötigt (typischerweise 12–24 Monate)
- **FINMA Circular 2023/1** (falls anwendbar): 10 Jahre für kritische operative Ereignisse
- **PCI DSS v4.0.1** (falls anwendbar): 12 Monate Hot Storage, 3 Monate sofort verfügbar
- **HIPAA** (falls anwendbar): Mindestens 6 Jahre
- **Legal Hold**: Unbegrenzte Aufbewahrung bis Hold aufgehoben

### Archivierungsprozess

Die Archivierung von Überwachungsdaten MUSS:

- Protokolle nach Ablauf der Aufbewahrungsfrist automatisch von Hot in Warm/Cold Storage übertragen
- Datenintegrität während der Übertragung aufrechterhalten (Prüfsummen, manipulationssichere Protokollierung)
- Archivierte Daten zur Speicherkostenoptimierung komprimieren
- Archivierte Daten im Ruhezustand verschlüsseln
- Archiv-Wiederherstellung vierteljährlich testen, um Wiederherstellbarkeit zu validieren
- Archivierungsstandorte, -formate und Abrufverfahren dokumentieren

### Datenschutz und Privatsphäre

Überwachungsdaten MÜSSEN sein:

- **Zugangskontrolliert**: Nur autorisiertes SOC, Security-Team, ISB und DSB haben Zugang
- **Verschlüsselt**: Im Ruhezustand und bei der Übertragung
- **Anonymisiert/Pseudonymisiert**: Wo machbar zum Schutz der Privatsphäre (unter Wahrung des forensischen Werts)
- **Vor Manipulation geschützt**: WORM-Speicher (Write Once Read Many) oder gleichwertiger Integritätsschutz
- **Segregiert**: Überwachungsprotokolle auf separater Infrastruktur von überwachten Systemen

**Mitarbeiter-Datenschutzüberlegungen** (Swiss nDSG Art. 328b OR, DSGVO Art. 88):

- Überwachungsumfang auf Sicherheits- und Compliance-Ziele beschränkt (keine Leistungskontrolle, keine Überwachung persönlicher Aktivitäten)
- Mitarbeitende über Überwachung durch Arbeitsverträge, Datenschutzhinweise, Richtlinien zur akzeptierten Nutzung informiert
- Verhältnismässigkeit bewertet: Überwachungsbreite und -tiefe durch Sicherheitsbedürfnisse gerechtfertigt
- Datensparsamkeit: Nur sicherheitsrelevante Ereignisse erfassen, Protokollausführlichkeit auf notwendige Felder beschränken
- Zweckbindung: Überwachungsdaten nicht für HR-Leistungsbeurteilungen ohne separate Rechtsgrundlage verwendet

---

# Governance und Compliance

## Rollen und Verantwortlichkeiten

Überwachungsaktivitäten erfordern klare Verantwortlichkeit über alle organisatorischen Rollen hinweg.

**Verantwortlichkeitsmatrix (RACI)**:

| Rolle | Verantwortung | Accountability |
|-------|---------------|----------------|
| **Informationssicherheitsbeauftragter (ISB)** | Strategische Aufsicht, Richtlinieneigentümerschaft, Budgetzuweisung, Risikoakzeptanz | Accountable für Wirksamkeit und Compliance des Überwachungsprogramms |
| **Security Operations Center (SOC) Lead** | Tägliche Überwachungsoperationen, Alarm-Triage, Eskalation, Teammanagement | Verantwortlich für 24/7-Überwachung, initiale Vorfallsreaktion, SLA-Einhaltung |
| **Security Team** | Baseline-Definition, Erkennungsregelgestaltung, Tool-Management, Optimierung | Verantwortlich für Überwachungsinfrastruktur, Erkennungswirksamkeit, Integration |
| **Systemeigentümer** | Sicherstellung, dass Systeme an Überwachungsplattformen protokollieren, Fachwissen bereitstellen | Verantwortlich für systemseitige Überwachungskonfiguration und Beweiserfassung |
| **IT-Betrieb** | Infrastrukturunterstützung für Überwachungsplattformen, Protokollquellen-Einbindung | Verantwortlich für operativen Support, Kapazitätsmanagement, Verfügbarkeit |
| **Netzwerk-Team** | Netzwerküberwachungsinfrastruktur, Traffic-Analyse, Firewall/IDS-Protokollerfassung | Verantwortlich für Überwachung auf Netzwerkebene und Traffic-Analyse |
| **Incident Response Team** | Eskalierte Vorfallsuntersuchung, Forensik, Behebung, Lessons Learned | Verantwortlich für Vorfallsbehandlung nach SOC-Eskalation |
| **Datenschutzbeauftragter (DSB)** | Datenschutzaufsicht, Compliance mit Datenschutzregulierungen | Beratend zu Überwachungsumfang, Datenaufbewahrung, Mitarbeiter-Datenschutz |
| **Legal/Compliance** | Regulatorische Auslegung, Legal-Hold-Management, Beweissicherung | Beratend zu gesetzlichen Anforderungen, Informiert über Compliance-Pflichten |
| **Geschäftsleitung** | Ressourcenzuweisung, strategische Ausrichtung, Risikoakzeptanz | Informiert durch vierteljährliche Compliance-Berichte, genehmigt Überwachungsbudget |

## Richtliniensteuerung

### Richtlinienüberprüfung und -aktualisierungen

Diese Richtlinie MUSS überprüft werden:

- **Jährlich** als Teil des ISMS-Richtlinienüberprüfungszyklus
- **Bei wesentlichen Änderungen** des organisatorischen Risikoprofils, der IT-Infrastruktur oder der Bedrohungslandschaft
- **Nach grossen Sicherheitsvorfällen**, bei denen Überwachungslücken identifiziert wurden
- **Wenn neue Überwachungstechnologien** eingesetzt oder bestehende Tools wesentlich aktualisiert werden
- **Bei regulatorischen Änderungen**, die Überwachungsanforderungen betreffen

Richtlinienaktualisierungen erfordern:

- Antrag mit geschäftlicher/sicherheitsbezogener Begründung
- Risikobeurteilung der vorgeschlagenen Änderungen
- Überprüfung durch betroffene Stakeholder (SOC, Security Team, Systemeigentümer, Legal/Compliance)
- Genehmigung durch ISB
- Kommunikation an relevante Mitarbeitende
- Aktualisierung der verwandten Implementierungsdokumentation (ISMS-IMP-A.8.16)

### Ausnahmemanagement

Ausnahmen zu Überwachungsanforderungen MÜSSEN:

- **Dokumentiert** werden mit geschäftlicher/technischer Begründung
- **Risikobewertet** werden, um Auswirkungen der Überwachungslücke zu quantifizieren
- **Kompensierende Kontrollen** identifiziert und implementiert haben, wo machbar
- **Genehmigt** werden durch SOC Lead (operative Ausnahmen) oder ISB (Richtlinienausnahmen)
- **Zeitlich begrenzt** sein: Maximal 12 Monate, kürzer für hochschwere Lücken
- **Vierteljährlich überprüft** werden, um fortgesetzte Notwendigkeit und Wirksamkeit kompensierender Kontrollen zu validieren
- **Verfolgt** werden im Ausnahmeregister mit Status, Behebungsplan und verantwortlicher Partei

**Gültige Ausnahmebeispiele**:

- Legacy-System ohne Protokollierungsfähigkeit, geplant zur Ausserdienststellung in 6 Monaten (Kompensierende Kontrolle: Netzwerküberwachung des gesamten Traffics zu/vom System)
- Cloud-Dienst mit eingeschränkter Protokollierungssichtbarkeit (Kompensierende Kontrolle: API-Aktivität überwachen, maximal verfügbare Protokollierung konfigurieren)
- Hochvolumen-Niedrigwert-Alarme temporär für Optimierung deaktiviert (Kompensierende Kontrolle: erweiterte manuelle Überprüfung verwandter Metriken)

**Ungültige Ausnahmebeispiele**:

- „Überwachung ist zu teuer" (Kosten sind kein gültiger Grund für Ausnahme von Sicherheitsanforderungen)
- „Wir haben keine Zeit, Protokollierung zu konfigurieren" (Ressourcenbeschränkungen erfordern Eskalation, keine Ausnahme)
- „Dieses System ist nicht wichtig" (Kritikalitätsbeurteilung erforderlich, keine Annahmenbasierte Ausnahme)

### Compliance-Verifizierung

Die Compliance mit Überwachungsanforderungen MUSS verifiziert werden durch:

- **Vierteljährliche Selbstbeurteilungen**: ISMS-IMP-A.8.16-Assessment-Arbeitsmappen von verantwortlichen Teams ausgefüllt
- **Jährliche interne Prüfung**: Verifikation der Richtlinienkonformität, Beweisüberprüfung, Kontrollwirksamkeitstests
- **Externe Prüfungen**: ISO-27001-Zertifizierungsprüfungen, regulatorische Inspektionen (FINMA, EDÖB usw.)
- **Erkennungstests**: Vierteljährliche Purple-Team-Übungen oder simulierte Angriffe zur Validierung von Erkennungsfähigkeiten
- **Kennzahlenüberprüfung**: Monatliche Überprüfung von MTTD, MTTR, False-Positive-Raten, Abdeckungsprozentsätzen, SLA-Einhaltung

**Compliance-Nachweise**:

- Ausgefüllte Assessment-Arbeitsmappen mit unterstützenden Nachweisen
- Architekturdiagramme der Überwachungsinfrastruktur
- Baseline-Dokumentation gemäss Anhang-B-Vorlage
- Erkennungsregel-Inventar mit Wirksamkeitskennzahlen
- Alarm-Reaktionsprotokolle, die SLA-Einhaltung belegen
- Ausnahmeregister mit Genehmigungen und kompensierenden Kontrollen
- Vorfallsreaktions-Tickets, die durch Überwachung ausgelöste Untersuchungen zeigen

## Integration ins Risikomanagement

**Risikobeurteilung**:

- Überwachungsumfang durch Risikobeurteilung bestimmt (kritische Assets priorisiert für Überwachung)
- Überwachungslücken als Risiken im Risikoregister identifiziert
- Risikobehandlungsentscheide bestimmen Überwachungsinvestitionen und -prioritäten

**Risikoregister**:

- Überwachungsrisiken dokumentiert: blinde Flecken, Alarm-Erschöpfung, unzureichende Abdeckung, Erkennungslücken
- Risikobewertungen treiben Behebungsdringlichkeit (Kritische Lücken innerhalb 30 Tage, Hohe innerhalb 90 Tage)
- Vierteljährliche Neubewertung basierend auf Überwachungswirksamkeitskennzahlen und Vorfallstrends

**Risikobehandlung**:

- Akzeptieren: Überwachungsbeschränkungen mit Risikoakzeptanz der Geschäftsleitung dokumentieren (z.B. Legacy-Systeme nicht überwachbar)
- Mindern: Überwachungskontrollen implementieren, Erkennungsabdeckung erweitern, Alarmrauschen reduzieren
- Übertragen: Drittanbieter-SOC-Dienste, Managed Detection and Response (MDR)
- Vermeiden: Nicht überwachbare Hochrisiko-Systeme ausser Betrieb nehmen

---

# Implementierung und Referenzen

## Implementierungsressourcen

**Implementierungsleitfaden (ISMS-IMP-A.8.16-Suite)**:

| Dokument | Zweck | Zielgruppe | Überprüfungsturnus |
|----------|-------|------------|-------------------|
| **ISMS-IMP-A.8.16.1** | Überwachungsinfrastruktur-Assessment | Security Engineering, IT-Betrieb | Halbjährlich |
| **ISMS-IMP-A.8.16.2** | Basis- und Erkennungs-Assessment | SOC, Security Team, Threat Intelligence | Vierteljährlich |
| **ISMS-IMP-A.8.16.3** | Abdeckungs-Assessment | Systemeigentümer, Netzwerk-Team, Security Team | Vierteljährlich |
| **ISMS-IMP-A.8.16.4** | Alarmverwaltungs- und Reaktions-Assessment | SOC, Incident Response, Security Team | Vierteljährlich |

## Verwandte ISMS-Richtlinien

Diese Richtlinie ist integriert mit:

| Richtlinie | Beziehung |
|------------|-----------|
| **ISMS-POL-00** | Regulatorischer Anwendbarkeitsrahmen – definiert anwendbare Regulierungen |
| **ISMS-POL-A.8.15** | Protokollierung – liefert Protokolldaten für Überwachungsanalyse |
| **ISMS-POL-A.5.24-5.28** | Vorfallsmanagement – konsumiert Überwachungsalarme, Vorfallsreaktions-Workflow |
| **ISMS-POL-A.5.7** | Threat Intelligence – Threat Intel informiert Erkennungsregeln, Überwachung erzeugt Intelligence |
| **ISMS-POL-A.8.8** | Schwachstellenmanagement – Überwachung identifiziert Ausnutzung, priorisiert Patches |
| **ISMS-POL-A.8.20** | Netzwerksicherheit – Netzwerkkontrollen erzeugen überwachte Ereignisse |
| **ISMS-POL-A.8.23** | Web-Filterung – Web-Filterprotokolle fliessen als Protokollquelle in Überwachung |
| **ISMS-POL-A.8.12** | Verhinderung von Datenlecks – Überwachung erkennt Datenexfiltrationsmuster |

## Externe Standards und Regulierungen

**Internationale Standards**:

- ISO/IEC 27001:2022 – Informationssicherheits-Managementsysteme
- ISO/IEC 27002:2022 – Informationssicherheitskontrollen (Control 8.16 Leitfaden)
- ISO/IEC 27035 – Vorfallsmanagement (Integration mit Überwachung)

**Technische Standards**:

- NIST SP 800-92 – Guide to Computer Security Log Management
- NIST SP 800-137 – Information Security Continuous Monitoring (ISCM)
- CIS Controls v8.1 – Control 8 (Audit Log Management), Control 13 (Network Monitoring)

**Regulatorisch**:

- Schweizerisches Bundesgesetz über den Datenschutz (DSG/nDSG)
- EU-Datenschutz-Grundverordnung (DSGVO) – wo anwendbar
- FINMA Circular 2023/1 (Operative Risiken und Resilienz) – falls anwendbar
- DORA (Digital Operational Resilience Act) – falls anwendbar
- NIS2-Richtlinie – falls anwendbar
- Branchenspezifische Regulierungen (PCI DSS v4.0.1, HIPAA usw.) – soweit anwendbar

**Rahmenwerk-Ausrichtung**:

- NIST Cybersecurity Framework (CSF) – Detect-Funktion
- MITRE ATT&CK Framework – Erkennungstaktiken und -techniken
- SANS Critical Security Controls

---

# Definitionen

**Überwachung (Monitoring)**
Die kontinuierliche oder periodische Beobachtung und Analyse von Netzwerken, Systemen und Anwendungen zur Identifizierung anomalen Verhaltens, Sicherheitsvorfällen, Richtlinienverstössen oder operativer Probleme, die Massnahmen erfordern.

**Baseline**
Ein dokumentiertes, messbares Profil des Normalverhaltens für ein System, Netzwerksegment, eine Anwendung oder Benutzergruppe, erstellt in bekannt-guten Betriebsperioden. Baselines umfassen statistische Kennzahlen (Mittelwert, Median, Standardabweichung, Perzentile) und sind zeitbewusst (Geschäftszeiten, ausserhalb der Geschäftszeiten, Wochenenden).

**Anomales Verhalten**
Aktivität, die erheblich von etablierten Baselines oder erwarteten Mustern abweicht. Anomalien können auf Sicherheitsvorfälle, Fehlkonfigurationen, Richtlinienverstösse oder legitime, aber ungewöhnliche Geschäftsaktivitäten hinweisen, die Untersuchung erfordern.

**Alarm**
Eine Benachrichtigung, die von Überwachungssystemen generiert wird, wenn vordefinierte Schwellenwerte überschritten oder spezifische Sicherheitsereignisse auftreten. Alarme werden nach Schweregrad klassifiziert und lösen Reaktionsverfahren gemäss SLA-Anforderungen aus.

**False Positive**
Ein Alarm, der durch legitime Aktivität ausgelöst wird, die fälschlicherweise als anomal oder böswillig identifiziert wurde. Hohe False-Positive-Raten führen zu Alarm-Erschöpfung und erfordern Anpassung der Erkennungsregeln.

**False Negative**
Ein Sicherheitsvorfall oder anomales Verhalten, das einen Alarm hätte auslösen sollen, aber nicht erkannt wurde. False Negatives stellen Erkennungslücken dar, die Regelverbesserung oder Baseline-Anpassung erfordern.

**Mean Time to Detect (MTTD)**
Durchschnittliche Zeitspanne zwischen dem Auftreten eines Vorfalls und seiner Erkennung durch Überwachungssysteme. Niedrigere MTTD zeigt effektivere Überwachung an.

**Mean Time to Respond (MTTR)**
Durchschnittliche Zeitspanne zwischen Alarmgenerierung und Vorfallseindämmung/-lösung. Niedrigere MTTR zeigt effektivere Vorfallsreaktion an.

**Security Information and Event Management (SIEM)**
Zentralisierte Plattform zur Erfassung, Korrelation, Analyse und Speicherung sicherheitsrelevanter Protokolle und Ereignisse aus mehreren Quellen. SIEM bietet Echtzeit-Alarmierung, forensische Untersuchung und Compliance-Berichterstattung.

**Intrusion Detection System (IDS) / Intrusion Prevention System (IPS)**
Netzwerksicherheitstechnologie, die Traffic auf böswillige Aktivitäten oder Richtlinienverstösse überwacht. IDS alarmiert bei Erkennung, IPS blockiert aktiv Bedrohungen.

**Endpoint Detection and Response (EDR)**
Auf Endpunkten (Workstations, Servern) eingesetzte Sicherheitslösung, die Systemverhalten überwacht, Bedrohungen erkennt und Reaktionsmassnahmen ermöglicht (Isolierung, Behebung).

**Network Detection and Response (NDR)**
Sicherheitslösung, die Netzwerktraffic analysiert, um Bedrohungen, Lateral Movement und anomale Kommunikationsmuster zu erkennen.

**User and Entity Behavior Analytics (UEBA)**
Analysetechnologie, die Verhaltensbaselines für Benutzer und Entitäten (Systeme, Anwendungen) erstellt und Abweichungen erkennt, die auf kompromittierte Konten oder Insider-Bedrohungen hinweisen können.

**Protokollquelle (Log Source)**
Jedes System, jede Anwendung, jedes Netzwerkgerät oder jede Sicherheitskontrolle, das/die Protokolle erzeugt, die von Überwachungsplattformen ingestiert werden.

**Korrelation**
Der Prozess der Analyse mehrerer Ereignisse aus verschiedenen Protokollquellen zur Identifizierung von Beziehungen und Erkennung komplexer Angriffsmuster, die aus einzelnen Ereignissen nicht ersichtlich sind.

**Threat Intelligence**
Kuratierte Informationen über aktuelle und aufkommende Bedrohungen, Angriffstechniken und Bedrohungsakteur-Verhalten. Threat Intelligence informiert Erkennungsregeln und reichert Alarmkontext an.

**Vorfall (Incident)**
Ein bestätigtes Sicherheitsereignis, das Untersuchung und Reaktion erfordert. Vorfälle werden nach Schweregrad klassifiziert und gemäss Vorfallsmanagementverfahren behandelt.

**Abdeckung (Coverage)**
Der Prozentsatz der Systeme, Netzwerke und Anwendungen im Überwachungsumfang, die aktiv überwacht werden und Protokolle an Überwachungsplattformen senden. Abdeckungslücken stellen blinde Flecken dar.

**Aufbewahrung (Retention)**
Die Dauer, für die Überwachungsdaten (Protokolle, Alarme, forensische Beweise) gespeichert werden. Aufbewahrungsfristen werden durch operative Bedürfnisse, regulatorische Anforderungen und rechtliche Pflichten bestimmt.

**Hot Storage**
Hochleistungsfähiger, indizierter Speicher für aktuelle Protokolle, der Echtzeit-Suche, Korrelation und Alarmierung ermöglicht. Typischerweise 90 Tage bis 12 Monate.

**Warm/Cold Storage**
Kostengünstigerer Archivierungsspeicher für ältere Protokolle mit langsameren Abrufzeiten. Verwendet für Compliance-Aufbewahrung und forensische Untersuchung historischer Vorfälle.

**Eskalation**
Der Prozess der Weitergabe eines Alarms oder Vorfalls an höherstufige Analysten, das Incident-Response-Team oder die Leitung, wenn die initiale Reaktion unzureichend ist oder der Schweregrad des Vorfalls zusätzliches Fachwissen erfordert.

**Anpassung (Tuning)**
Der Prozess der Anpassung von Erkennungsregeln, Baselines und Alarmschwellenwerten zur Reduzierung von False Positives unter Beibehaltung der Erkennungsabdeckung. Anpassung ist ein kontinuierlicher Prozess basierend auf operativem Feedback.

---

# Anhang A: Überwachungs-Fähigkeitsstandards (Entscheidungsrahmen)

**Zweck**: Dieser Anhang definiert Fähigkeitsanforderungen und Auswahlkriterien für Überwachungstechnologien. Organisationen nutzen dieses Rahmenwerk zur Bewertung von Überwachungslösungen bei der Beschaffung und Validierung bestehender Tool-Fähigkeiten.

## A.1 Überwachungstechnologie-Kategorien

| Technologie-Kategorie | Primärfunktion | Schlüsselfähigkeiten | Typische Bereitstellung |
|-----------------------|----------------|---------------------|------------------------|
| **SIEM** | Zentralisiertes Protokollmanagement, Korrelation, Alarmierung | Mehrquellen-Ingest, Echtzeit-Korrelation, Compliance-Berichterstattung, Forensik | Unternehmensweite, zentralisierte Bereitstellung |
| **IDS/IPS** | Erkennung und Abwehr von Netzwerkbedrohungen | Signaturbasierte Erkennung, Protokollanalyse, Paketinspektion | Netzwerkperimeter, kritische Segmente |
| **EDR** | Erkennung und Reaktion auf Endpoint-Bedrohungen | Verhaltensanalyse, Malware-Erkennung, forensische Untersuchung, Behebung | Workstations, Server |
| **NDR** | Netzwerkverhalten-Analyse und Lateral-Movement-Erkennung | Traffic-Analyse, Anomalieerkennung, Ost-West-Traffic-Überwachung | Rechenzentrum, Cloud-Umgebungen |
| **UEBA** | User and Entity Behavior Analytics | Machine-Learning-Baselines, Anomalieerkennung, Insider-Bedrohungserkennung | Überlagert SIEM/EDR-Daten |
| **Log Management** | Protokollerfassung, -speicherung, -suche | Skalierbare Ingest, Langzeitaufbewahrung, Suchfähigkeiten | Eigenständig oder SIEM-Komponente |

## A.2 Verbindliche Fähigkeiten (Alle Überwachungslösungen)

Unabhängig von der Technologie-Kategorie MÜSSEN Überwachungslösungen bereitstellen:

**Erfassung**:

- Mehrprotokoll-Protokollingest (Syslog, agentenbasiert, API, dateibasiert)
- Sichere Protokollübertragung (TLS-Verschlüsselung, authentifizierte Quellen)
- Skalierbare Erfassung (unterstützt Organisationswachstum ohne Architektur-Redesign)
- Zuverlässige Zustellung (Bestätigung, Wiederholungsmechanismen, Warteschlangenverwaltung)

**Analyse**:

- Echtzeit-Ereignisverarbeitung (Sub-Sekunden-Latenz für kritische Ereignisse)
- Suchfähigkeiten (indizierte Suche über alle gesammelten Protokolle)
- Filterung und Abfragen (flexible Abfragesprache für Untersuchungen)
- Korrelation (Fähigkeit, verwandte Ereignisse über Zeit und Quellen zu verknüpfen)

**Speicherung**:

- Datenschutz und Integritätsschutz (manipulationssichere Protokollierung, Prüfsummen)
- Angemessene Aufbewahrung (Hot Storage ≥90 Tage, Archivierung gemäss Compliance-Anforderungen)
- Backup und Recovery (Überwachungsdaten in Backup-Strategie einbezogen)

**Alarmierung**:

- Konfigurierbare Regeln (benutzerdefinierte Alarmerstellung basierend auf organisatorischen Bedürfnissen)
- Schweregradklassifizierung (Kritisch, Hoch, Mittel, Niedrig, Informational)
- Mehrkanal-Benachrichtigung (E-Mail, SMS, Ticketsystem, SOAR-Integration)
- Alarm-Deduplizierung (Alarmstürme aus einem einzelnen Ereignis verhindern)

**Berichterstattung**:

- Compliance-Berichterstattung (vorgefertigte oder anpassbare Berichte für regulatorische Anforderungen)
- Executive-Dashboards (übergeordnete KPIs für Management-Sichtbarkeit)
- Forensische Fähigkeiten (Zeitlinienrekonstruktion, Beweisexport)

## A.3 Empfohlene Fähigkeiten (Erweiterte Überwachung)

Organisationen SOLLTEN Lösungen mit folgenden Fähigkeiten in Betracht ziehen:

**Erweiterte Korrelation**:

- Mehrstufige Angriffserkennung (Aufklärung → Ausnutzung → Persistenz → Exfiltration verknüpfen)
- Verhaltensanalyse (UEBA für Benutzer- und Entitätsanomalien)
- Machine Learning (adaptive Baselines, automatische Anomalieerkennung)

**Threat-Intelligence-Integration**:

- Automatische Anreicherung (Ereignisse mit Threat-Intel-Feeds korrelieren)
- IOC-Abgleich (Protokolle gegen Indicators of Compromise abgleichen)
- Threat Hunting (proaktive Suche nach Adversary-TTPs)

**Orchestrierung und Automatisierung**:

- Automatisierte Reaktionsmassnahmen (Kontosperrung, Netzwerkisolierung, Malware-Quarantäne)
- Workflow-Automatisierung (Ticket-Erstellung, Benachrichtigung, Eskalation)
- Playbook-Ausführung (standardisierte Reaktionsverfahren)

**Cloud-native Fähigkeiten**:

- Cloud-Plattform-Integration (AWS-, Azure-, GCP-native Protokollerfassung)
- Container-Überwachung (Kubernetes-Prüfprotokolle, Pod-Ereignisse)
- Serverlose Überwachung (Lambda, Azure Functions, Cloud Functions)

## A.4 Technologieauswahlkriterien

Bei der Bewertung von Überwachungstechnologien MUSS [Organisation] beurteilen:

**Technische Eignung**:

- Kompatibilität mit bestehender Infrastruktur (On-Premises, Cloud, Hybrid)
- Protokollquellen-Abdeckung (unterstützt organisatorische Systeme und Anwendungen)
- Skalierbarkeit (verarbeitet aktuelle und prognostizierte Protokollvolumen)
- Integrationsfähigkeiten (APIs, SIEM-Konnektoren, Drittanbieter-Tools)

**Operative Wirksamkeit**:

- Erkennungsgenauigkeit (niedrige False-Positive-Raten, hohe True-Positive-Raten)
- Leistung (Echtzeit-Verarbeitung, akzeptable Suchlatenz)
- Benutzerfreundlichkeit (intuitive Benutzeroberfläche, effiziente Workflows, minimaler Schulungsaufwand)
- Zuverlässigkeit (Hochverfügbarkeit, Disaster-Recovery-Fähigkeiten)

**Sicherheit**:

- Zugriffskontrollen (RBAC, MFA, Prüfprotokollierung administrativer Aktionen)
- Datenschutz (Verschlüsselung im Ruhezustand und bei der Übertragung, Datenmaskierung)
- Isolierung (Härtung der Überwachungsinfrastruktur-Sicherheit)

**Kosten**:

- Gesamtbetriebskosten (Lizenzierung, Infrastruktur, Personal, Schulung)
- Lizenzierungsmodell (pro GB, pro Asset, pro Nutzer, unbegrenzt)
- Skalierungskosten (inkrementelle Kosten bei steigenden Protokollvolumen)

**Anbieter-Faktoren**:

- Anbieterreputation und Marktpräsenz
- Produktreife und Roadmap
- Support-Qualität und Reaktionsfähigkeit
- Community und Dokumentation
- Strategische Ausrichtung mit organisatorischer Technologierichtung

## A.5 Fähigkeitsreifebewertung

Organisationen SOLLTEN die Überwachungs-Fähigkeitsreife bewerten:

**Stufe 1 – Initial (Ad hoc)**:

- Grundlegende Protokollierung aktiviert, eingeschränkte Zentralisierung
- Manuelle Protokollüberprüfung, reaktive Vorfallserkennung
- Keine Baselines, Erkennungsregeln oder Alarmierung
- Minimale Überwachungsinfrastruktur

**Stufe 2 – Entwicklung (Wiederholbar)**:

- Zentralisierte Protokollerfassung (SIEM oder gleichwertig)
- Grundlegende Alarmierungsregeln konfiguriert
- Einige Baselines dokumentiert
- Vorfallsreaktion durch Alarme ausgelöst (manchmal)

**Stufe 3 – Definiert (Standardisiert)**:

- Umfassende Protokollquellen-Abdeckung (>80 % kritische Systeme)
- Dokumentierte Baselines für kritische Systeme
- Angepasste Erkennungsregeln mit akzeptablen False-Positive-Raten (<30 %)
- Definierte Reaktionsverfahren und SLAs
- Vierteljährliche Erkennungstests

**Stufe 4 – Managed (Quantitativ gesteuert)**:

- Nahezu vollständige Abdeckung (>95 % kritische Systeme, >80 % Standard-Systeme)
- Baselines für alle überwachten Systeme
- Niedrige False-Positive-Raten (<20 % kritische Alarme)
- Kennzahlengetriebene Optimierung (MTTD, MTTR, Erkennungsraten verfolgt)
- Monatliche Anpassung und kontinuierliche Verbesserung

**Stufe 5 – Optimierung (Kontinuierliche Verbesserung)**:

- Vollständige Abdeckung mit minimalen blinden Flecken
- Automatisierte Baseline-Wartung und Anomalieerkennung
- Erweiterte Korrelation und Threat-Intelligence-Integration
- Orchestrierte Reaktion (SOAR)
- Proaktives Threat Hunting
- Branchenführende Kennzahlen (MTTD <1 Stunde, MTTR <4 Stunden bei kritischen Vorfällen)

---

# Anhang B: Baseline-Definitionsvorlage

**Zweck**: Standardisierte Vorlage für die Dokumentation von System-, Benutzer- und Anwendungs-Baselines gemäss Richtlinienabschnitt 2.2.

## B.1 Baseline-Dokumentationsvorlage

**Baseline-ID**: [AUTO-GENERIERT: BL-JJJJMMTT-NNN]
**Erstellungsdatum**: [TT.MM.JJJJ]
**Erstellt von**: [Name, Rolle]
**Genehmigt von**: [SOC Lead / Security Manager]
**Überprüfungsdatum**: [Vierteljährlich – Nächste Überprüfung: TT.MM.JJJJ]

---

## Baseline-Umfang

**System/Asset/Benutzergruppe**:
[Spezifischer System-Hostname, IP, Anwendungsname oder Benutzergruppe (z.B. „dc01.example.com", „Finanzabteilungs-Benutzer", „Kundenportal-API")]

**Baseline-Kategorie**:

- [ ] Systemauslastung (CPU, Arbeitsspeicher, Festplatte, Netzwerk)
- [ ] Zugriffsmuster (Authentifizierung, Anmeldungen, Zugriffshäufigkeit)
- [ ] Anwendungsverhalten (Transaktionen, API-Aufrufe, Datenbankabfragen)
- [ ] Netzwerktraffic (Protokolle, Ziele, Bandbreite)
- [ ] Sonstiges: [Angeben]

**Umgebung**:

- [ ] Produktion
- [ ] Staging/QA
- [ ] Entwicklung
- [ ] Sonstiges: [Angeben]

---

## Baseline-Metrik-Definition

**Metrikname**: [Beschreibender Name – z.B. „SQL-Abfragerate", „Benutzerauthentifizierungsanzahl", „Ausgehende HTTPS-Verbindungen"]

**Metrikbeschreibung**: [Genaue Definition des Gemessenen – z.B. „Anzahl der SQL-SELECT-Abfragen pro Minute gegen Kundendatenbank", „Erfolgreiche Authentifizierungsversuche durch Finanzabteilungs-Benutzer pro Stunde"]

**Datenquelle**: [Wo Metrik erfasst wird – z.B. „SQL Server-Prüfprotokolle", „Active Directory-Sicherheitsprotokolle", „Firewall-Verbindungsprotokolle"]

**Erfassungsmethode**: [Wie Metrik berechnet wird – z.B. „SIEM-Aggregation von Ereignis-ID 4624", „Datenbankabfrage: SELECT COUNT(*) FROM sys.dm_exec_requests WHERE statement_type='SELECT'"]

---

## Beobachtungszeitraum

**Startdatum**: [TT.MM.JJJJ]
**Enddatum**: [TT.MM.JJJJ]
**Dauer**: [X Tage – mindestens 30 Tage empfohlen, vollständige Geschäftszyklen einschliessen]

**Geschäftszyklus-Abdeckung**:

- [ ] Umfasst Monatsabschluss-Verarbeitung (falls zutreffend)
- [ ] Umfasst Quartalsabschluss-Verarbeitung (falls zutreffend)
- [ ] Umfasst Jahresabschluss-Verarbeitung (falls zutreffend)
- [ ] Umfasst Geschäftsspitzenzeiten (z.B. Steuersaison, Weihnachtsgeschäft)
- [ ] Umfasst typische Wartungsfenster

**Ausschlüsse**: [Dokumentation aller vom Baseline-Berechnung ausgeschlossenen Zeiträume]

- Geplante Wartungsfenster: [Daten/Zeiten auflisten]
- Bekannte Vorfälle oder Anomalien: [Beschreiben und Ausschluss begründen]
- Systemausfallzeiten: [Daten/Zeiten auflisten]

---

## Statistisches Profil

**Zeitaggregation**: [Stichprobenintervall – z.B. „pro Minute", „pro Stunde", „pro Tag"]

**Gesamtstatistik**:

| Kennzahl | Wert | Anmerkungen |
|----------|------|-------------|
| **Mittelwert (Durchschnitt)** | [X,XX] | Durchschnittswert über Beobachtungszeitraum |
| **Median** | [X,XX] | 50. Perzentil (Mittelwert) |
| **Standardabweichung (σ)** | [X,XX] | Variabilitätsmass |
| **Minimum** | [X,XX] | Niedrigster beobachteter Wert (Ausreisser ausgeschlossen) |
| **Maximum** | [X,XX] | Höchster beobachteter Wert (Ausreisser ausgeschlossen) |
| **95. Perzentil** | [X,XX] | 95 % der Beobachtungen liegen darunter |
| **99. Perzentil** | [X,XX] | 99 % der Beobachtungen liegen darunter |

**Stichprobengrösse**: [N Beobachtungen – z.B. „43.200 Minuten (30 Tage × 24 Stunden × 60 Minuten)"]

---

## Zeitbewusste Baselines (falls zutreffend)

Falls das Verhalten sich je nach Zeitraum wesentlich unterscheidet, separate Baselines dokumentieren:

**Geschäftszeiten** (Montag–Freitag, 08:00–18:00 CET):

| Kennzahl | Mittelwert | Median | Std. Abw. | 95. %il |
|----------|-----------|--------|-----------|---------|
| [Metrikname] | [Wert] | [Wert] | [Wert] | [Wert] |

**Ausserhalb der Geschäftszeiten** (Montag–Freitag, 18:00–08:00 CET):

| Kennzahl | Mittelwert | Median | Std. Abw. | 95. %il |
|----------|-----------|--------|-----------|---------|
| [Metrikname] | [Wert] | [Wert] | [Wert] | [Wert] |

**Wochenenden** (Samstag–Sonntag, alle Zeiten):

| Kennzahl | Mittelwert | Median | Std. Abw. | 95. %il |
|----------|-----------|--------|-----------|---------|
| [Metrikname] | [Wert] | [Wert] | [Wert] | [Wert] |

---

## Schwellenwertableitung

**Alarmschwellenwert-Methodik**: [Beschreibung der Ableitung von Alarmschwellenwerten aus der Baseline]

**Beispiel-Methodiken**:

- **95. Perzentil-Multiplikator**: Alarmschwelle = 95. Perzentil × [Multiplikator – z.B. 1,5]
- **Standardabweichungen**: Alarmschwelle = Mittelwert + [N] × Standardabweichung
- **Absolutwert**: Alarmschwelle = [Fester Wert] basierend auf Kapazitätsgrenzen oder Geschäftsregeln
- **Änderungsrate**: Alarm wenn Wert innerhalb [Y Minuten] um [X] % steigt/fällt

**Berechnete Schwellenwerte**:

| Schwellenwertstufe | Methodik | Berechneter Wert | Begründung |
|--------------------|----------|-----------------|------------|
| **Warnung** | [Methode] | [Wert] | [Warum diese Stufe Warnung auslöst] |
| **Kritisch** | [Methode] | [Wert] | [Warum diese Stufe kritischen Alarm auslöst] |

---

## Baseline-Validierung

**Verifikation des bekannt-guten Zeitraums**:

- [ ] Beobachtungszeitraum als frei von Sicherheitsvorfällen bestätigt
- [ ] Keine wesentlichen Konfigurationsänderungen während Beobachtungszeitraum
- [ ] Keine wesentlichen Geschäftsprozessänderungen während Beobachtungszeitraum
- [ ] Systemleistung innerhalb normaler Betriebsparameter

**Ausreisseranalyse**: [Beschreibung identifizierter Ausreisser und deren Behandlung]

**Peer Review**: [Name und Rolle des Prüfers, der die Baseline-Genauigkeit validiert hat]

---

## Baseline-Wartung

**Überprüfungsturnus**: Vierteljährlich (oder häufiger bei Geschäfts-/Technikänderungen)

**Aktualisierungsauslöser**:

- [ ] Systemkonfigurationsänderungen (Hardware-, Software-, Kapazitätserweiterungen)
- [ ] Geschäftsprozessänderungen (neue Workflows, organisatorische Umstrukturierungen)
- [ ] Anhaltende Abweichungen von der Baseline (anhaltende Verschiebung des Normalverhaltens)
- [ ] Saisonale Schwankungen (Baselines für bekannte saisonale Muster anpassen)

**Nächstes Überprüfungsdatum**: [TT.MM.JJJJ]

**Eigentümer**: [Name und Rolle der für die Baseline-Genauigkeit verantwortlichen Person]

**Kontakt**: [E-Mail/Telefon für Fragen zu dieser Baseline]

---

## Erkennungsregeln, die diese Baseline verwenden

**Konfigurierte Alarmregeln**:

| Regel-ID | Regelname | Schweregrad | Schwellenwert | Status |
|----------|-----------|-------------|---------------|--------|
| [REGEL-001] | [Beschreibender Name] | [Kritisch/Hoch/Mittel] | [Wert aus Abschnitt 6] | [Aktiv/Test/Deaktiviert] |

---

## Baseline-Verwendungshinweise

[Zusätzlicher Kontext, Einschränkungen oder operative Hinweise für SOC-Analysten und Security-Team]

**Beispielhinweise**:

- „Diese Baseline schliesst Monatsabschluss-Batch-Verarbeitung aus (typischerweise 28.–3.). Separate Baseline BL-20260115-002 deckt Monatsabschluss-Zeitraum ab."
- „Baseline spiegelt aktuelle 100-Benutzer-Organisation wider. Neu-Baselining erforderlich, wenn Benutzeranzahl um >20 % steigt."
- „Anwendungsversion 2.5 während Beobachtungszeitraum bereitgestellt. Baseline kann Anpassung erfordern, wenn sich Leistungsmerkmale in zukünftigen Versionen ändern."

---

**ENDE DER BASELINE-VORLAGE**

**Baseline-Status**: [ ] Entwurf [ ] Genehmigt [ ] Aktiv [ ] Abgelaufen [ ] Ersetzt

---

# Anhang C: Kurzreferenz

**Zweck**: Einseitige Zusammenfassung der Überwachungsaktivitäten für SOC-Analysten, Systemeigentümer und Stakeholder.

## Was ist Überwachung?

Überwachung ist die kontinuierliche Beobachtung von Netzwerken, Systemen und Anwendungen zur Erkennung anomalen Verhaltens und potenzieller Sicherheitsvorfälle. Effektive Überwachung erfordert dokumentierte Baselines, angepasste Erkennungsregeln und zeitnahe Reaktion auf Alarme.

## Schlüsselverantwortlichkeiten

**Wenn Sie ... sind**

**SOC-Analyst**:

- ✅ Alarme 24/7 überwachen, Triage innerhalb SLA (5 Min. Kritisch, 15 Min. Hoch)
- ✅ Alarme untersuchen, Ergebnisse dokumentieren, bestätigte Vorfälle eskalieren
- ✅ False Positives für Anpassung melden

**Systemeigentümer**:

- ✅ Sicherstellen, dass Systeme an Überwachungsplattformen protokollieren
- ✅ Fachwissen bei Vorfallsuntersuchungen bereitstellen
- ✅ Baseline-Etablierung für eigene Systeme koordinieren

**Security Engineer**:

- ✅ Baselines etablieren, Erkennungsregeln erstellen, Alarme anpassen
- ✅ Überwachungsinfrastruktur verwalten, Protokollquellen integrieren
- ✅ Erkennungswirksamkeit vierteljährlich testen

**Executive/Leitung**:

- ✅ Vierteljährliche Summary-Dashboards überprüfen
- ✅ Ressourcen für das Überwachungsprogramm zuweisen
- ✅ Restrisiken aus Überwachungslücken akzeptieren

## Alarmschweregrade und Reaktionszeiten

| Schweregrad | Reaktionszeit | Beispiele |
|-------------|---------------|-----------|
| **Kritisch** | 15 Minuten | Ransomware, aktive Datenexfiltration, Root-Kompromittierung |
| **Hoch** | 1 Stunde | Malware-Infektion, erfolgreiche Privilege Escalation |
| **Mittel** | 4 Stunden | Anomales Verhalten, Richtlinienverstösse |
| **Niedrig** | 24 Stunden | Geringfügige Abweichungen, informative Ereignisse |

## Überwachungsabdeckungsziele

- ✅ **100 %** der Tier-1-Systeme (Kritisch) überwacht
- ✅ **>80 %** der Tier-2-Systeme (Standard) überwacht
- ✅ **<20 %** False-Positive-Rate bei kritischen Alarmen
- ✅ **>90 %** True-Positive-Rate bei hochschweren Bedrohungen

## Häufige Überwachungslücken (Worauf zu achten ist)

❌ **Blinde Flecken**: Legacy-Systeme, Cloud-Dienste mit eingeschränkter Protokollierung
❌ **Alarm-Erschöpfung**: Zu viele False Positives, Analysten ignorieren Alarme
❌ **Baseline-Drift**: Baselines nicht aktualisiert, normales Verhalten löst Alarme aus
❌ **Abdeckungslücken**: Kritische Systeme senden keine Protokolle an SIEM
❌ **Aufbewahrungsprobleme**: Protokolle zu schnell gelöscht für forensische Untersuchung

## Problemberichterstattung

**False Positive**: Anpassungsanfrage an Security-Team einreichen (Alarm-ID, Grund für FP, vorgeschlagene Lösung)

**Überwachungslücke**: Im vierteljährlichen Abdeckungs-Assessment dokumentieren, bei kritischen Lücken an ISB eskalieren

**Vorfall**: An Incident Response gemäss ISMS-POL-A.5.24-5.28 eskalieren

**Fragen**: SOC Lead oder Security Manager kontaktieren

## Schlüsselkennzahlen (Monatlich verfolgen)

- **MTTD** (Mean Time to Detect): Wie schnell werden Vorfälle erkannt?
- **MTTR** (Mean Time to Respond): Wie schnell werden Vorfälle eingedämmt?
- **Abdeckung %**: Welcher Prozentsatz kritischer Systeme wird überwacht?
- **False-Positive-Rate**: Welcher Prozentsatz der Alarme sind False Positives?
- **Erkennungsrate**: Welcher Prozentsatz der Angriffe wird erkannt? (Vierteljährlich testen)

## Vierteljährliche Assessments

Alle Stakeholder MÜSSEN vierteljährliche Überwachungsassessments durchführen:

- **ISMS-IMP-A.8.16.1-UG/TG**: Überwachungsinfrastruktur (Security Engineering)
- **ISMS-IMP-A.8.16.2-UG/TG**: Baselines & Erkennung (SOC, Security Team)
- **ISMS-IMP-A.8.16.3-UG/TG**: Abdeckung (Systemeigentümer, Netzwerk-Team)
- **ISMS-IMP-A.8.16.4-UG/TG**: Alarmverwaltung & Reaktion (SOC, Incident Response)

## Merken Sie sich

> *„Man kann nicht managen, was man nicht misst. Man kann nicht messen, was man nicht überwacht. Man kann nicht überwachen, was man nicht als Baseline definiert hat."*
> *— Security Operations Wisdom*

**Überwachung ohne Baselines ist Raten. Alarme ohne Reaktion sind Rauschen. Erkennung ohne Tests ist Hoffnung.**

---

**Für detaillierte Informationen wird auf ISMS-POL-A.8.16 (Richtlinie zu Überwachungsaktivitäten) und ISMS-IMP-A.8.16 (Implementierungsleitfaden-Suite) verwiesen.**

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Security Operations Center (SOC) Lead** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen an Überwachungsaktivitäten fest. Implementierungsverfahren, technische Standards und Assessment-Arbeitsmappen sind in ISMS-IMP-A.8.16 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-29 -->
