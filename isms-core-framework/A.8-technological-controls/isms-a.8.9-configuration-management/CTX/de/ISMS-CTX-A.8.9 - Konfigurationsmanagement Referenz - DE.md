<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.9-konfigurationsmanagement-referenz-DE:framework:CTX:a.8.9 -->
**ISMS-CTX-A.8.9 — Konfigurationsmanagement Referenz**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Konfigurationsmanagement Referenz |
| **Dokumenttyp** | Technische Referenz (NICHT ISMS) |
| **Dokument-ID** | ISMS-CTX-A.8.9 |
| **Dokumentersteller** | Configuration Manager |
| **Dokumenteigentümer** | Security Architect |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Date] |
| **Klassifizierung** | INTERN |
| **Status** | Referenz |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | Configuration Manager / Security Architect | Erstversion der technischen Referenz |

**Überprüfungszyklus**: Halbjährlich oder bei Änderungen der Standards/Technologien
**Nächstes Überprüfungsdatum**: [Date + 6 months]

**Überprüfungsbefugnis**:

- Technische Überprüfung: Configuration Manager
- Sicherheitsüberprüfung: Security Architect
- KEINE Genehmigung der Geschäftsleitung erforderlich (NICHT ISMS)

---

## ⚠️ KRITISCH: Dokumentenstatus

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

**DIESES DOKUMENT DEFINIERT KEINE VERBINDLICHEN ANFORDERUNGEN.**

**DIESES DOKUMENT BEGRÜNDET KEINE BINDENDEN VERPFLICHTUNGEN.**

**ALLE BINDENDEN ANFORDERUNGEN SIND IN ISMS-POL-A.8.9 DEFINIERT.**

**Dies ist ausschliesslich technische Referenz und operative Anleitung zur Unterstützung bei der Umsetzung.**

**Zweck**: Technische Standardsreferenz, Implementierungsverfahren und operative Anleitung zur Unterstützung der Umsetzung der Konfigurationsmanagement-Richtlinie bereitstellen. Dieses Dokument ergänzt ISMS-POL-A.8.9, ersetzt jedoch NICHT die Richtlinienanforderungen.

**Zielgruppe**: Configuration Manager, Systemadministratoren, DevOps-Ingenieure, Security-Ingenieure, Betriebspersonal

**Verwendung**: Referenz für Baseline-Definitionen, Änderungsverfahren, Reaktion auf Konfigurationsabweichungen und schnelle operative Anleitung. Organisationen passen diesen Inhalt an ihren spezifischen Technologie-Stack, ihre Tools und operativen Prozesse an.

**Aktualisierungen**: Dieses Dokument kann häufiger als ISMS-Richtlinien aktualisiert werden, um sich entwickelnde Technologien, neue Tools und aktualisierte Standards widerzuspiegeln. Aktualisierungen erfordern keine Genehmigung der Geschäftsleitung, müssen jedoch an betroffene Mitarbeitende kommuniziert werden.

---

## Teil 1: Standards-Referenz für Konfigurationen

### Übersicht Hardening-Standards

Konfigurations-Hardening wendet sicherheitsorientierte Konfigurationen auf Basis anerkannter Branchenstandards an. [Organisation] wählt anwendbare Standards auf Basis von Asset-Typ, regulatorischen Anforderungen und Risikobewertung aus.

**1.1.1 CIS Benchmarks** (Center for Internet Security)

**Abdeckung**: Über 100 Benchmarks für mehr als 25 Technologiefamilien

- Betriebssysteme: Windows, Linux (RHEL, Ubuntu, SUSE), macOS, Unix-Varianten
- Cloud-Plattformen: AWS, Azure, GCP, Oracle Cloud
- Netzwerkgeräte: Cisco, Palo Alto, Fortinet
- Datenbanken: Oracle, SQL Server, PostgreSQL, MongoDB, MySQL
- Anwendungen: Webserver, Container-Plattformen, Kubernetes

**Stufen**:

- **Level 1**: Praktisches Baseline-Hardening (minimale operative Auswirkung)
- **Level 2**: Defense-in-Depth (kann Funktionalität einschränken)

**Bezug**: Kostenloser Download von cisecurity.org (Registrierung erforderlich)

**1.1.2 DISA STIGs** (Defense Information Systems Agency)

**Abdeckung**: Sicherheitsanforderungen des US-Verteidigungsministeriums

- Betriebssysteme: Windows, Linux, Unix
- Anwendungen: Datenbanken, Webserver, Applikationsserver
- Netzwerkgeräte: Router, Switches, Firewalls

**Klassifizierung**: CAT I (Kritisch), CAT II (Hoch), CAT III (Mittel)

**Bezug**: Kostenloser Download von public.cyber.mil/stigs

**Verwendung**: Behörden/Verteidigungsauftragnehmer, Hochsicherheitsumgebungen

**1.1.3 Herstellerspezifische Sicherheitsleitfäden**

**Microsoft**:

- Windows Server Security Baseline
- Microsoft 365 Security Baseline
- Azure Security Baseline
- Security Compliance Toolkit

**Cloud-Anbieter**:

- AWS Security Best Practices
- Azure Security Benchmarks
- Google Cloud Security Foundations
- Oracle Cloud Security Posture Management

**Netzwerkhersteller**: Cisco, Palo Alto, Fortinet, Check Point Sicherheitsleitfäden

**1.1.4 NIST-Publikationen**

- **NIST SP 800-53 Rev. 5**: Sicherheits- und Datenschutzcontrols (CM-Familie)
- **NIST SP 800-128**: Sicherheitsorientiertes Konfigurationsmanagement
- **NIST SP 800-70**: National Checklist Program
- **NIST Cybersecurity Framework**: Konfigurationsmanagement in der PROTECT-Funktion

**1.1.5 Weitere Standards**

- **BSI Grundschutz**: Bundesamt für Sicherheit in der Informationstechnik
- **Essential Eight**: Australian Cyber Security Centre
- **CMMC**: Cybersecurity Maturity Model Certification (Verteidigungsauftragnehmer)
- **SWIFT CSC**: Sicherheitscontrols für Finanznachrichten

### Konfigurationsstandards nach Asset-Typ

**1.2.1 Betriebssysteme**

**Windows Server**:

- **Primärer Standard**: CIS Windows Server Benchmark (versionsspezifisch)
- **Ergänzend**: Microsoft Security Baselines, DISA STIG (Hochsicherheit)
- **Schlüsselcontrols**:
  - User Account Control (UAC) aktiviert
  - Windows-Firewall mit restriktiven Regeln aktiviert
  - Audit-Logging für Authentifizierung, Privilegiennutzung, Objektzugriff
  - Passwortrichtlinie: Mindestens 14 Zeichen, Komplexität, Sperrung nach 5 Fehlversuchen
  - Deaktivierte Dienste: Print Spooler (sofern nicht benötigt), Remote Desktop (sofern nicht benötigt)
  - Sicherheitspatches: Monatliche Installation innerhalb von 30 Tagen

**Linux/Unix**:

- **Primärer Standard**: CIS Distributions-spezifischer Benchmark (RHEL, Ubuntu, SUSE usw.)
- **Ergänzend**: DISA STIG (Hochsicherheit)
- **Schlüsselcontrols**:
  - Root-Login deaktiviert (sudo verwenden)
  - SSH-Hardening (schlüsselbasierte Authentifizierung, Root-Login deaktivieren, Protokoll 1 deaktivieren)
  - iptables/firewalld mit Default-Deny konfiguriert
  - SELinux/AppArmor aktiviert (Enforcing-Modus)
  - Audit-Daemon (auditd) aktiviert und konfiguriert
  - Dateiberechtigungen: /etc/passwd 644, /etc/shadow 000, /boot 700

**1.2.2 Netzwerkgeräte**

**Firewalls** (Palo Alto, Fortinet, Cisco ASA):

- **Primärer Standard**: Herstellerspezifischer Sicherheitsleitfaden + CIS Benchmark
- **Schlüsselcontrols**:
  - Default-Deny-Regeln
  - Regelwerke mit minimalen Rechten
  - Logging für alle Allow/Deny-Entscheidungen aktiviert
  - Admin-Zugang auf Management-VLAN beschränkt
  - Multi-Faktor-Authentifizierung für Admin-Zugang
  - Regelmässige Überprüfung und Bereinigung der Regeln

**Router/Switches** (Cisco, Juniper, Arista):

- **Primärer Standard**: CIS Network Device Benchmark
- **Schlüsselcontrols**:
  - Konsolen- und VTY-Zugangscontrol (nur SSH, kein Telnet)
  - SNMP v3 oder deaktiviert
  - AAA-Authentifizierung
  - Logging an zentralen Syslog
  - NTP-Synchronisation
  - Ungenutzte Ports deaktiviert

**Load Balancer**:

- **Primärer Standard**: Herstellersicherheitsleitfaden
- **Schlüsselcontrols**:
  - Ausschliesslich TLS 1.2+
  - Starke Cipher Suites
  - Zertifikatsvalidierung
  - Session-Timeout-Konfiguration
  - Admin-Interface im Management-Netzwerk

**1.2.3 Cloud-Plattformen**

**AWS**:

- **Primärer Standard**: CIS AWS Foundations Benchmark
- **Schlüsselcontrols**:
  - IAM: MFA für alle Benutzer, Prinzip der minimalen Rechte, regelmässige Rotation der Access Keys
  - Logging: CloudTrail in allen Regionen aktiviert, S3-Bucket-Logging, VPC Flow Logs
  - Überwachung: CloudWatch-Alarme für nicht autorisierte API-Aufrufe
  - Netzwerk: VPC Security Groups Default-Deny, keine öffentlichen S3-Buckets (ausser wenn explizit erforderlich)
  - Verschlüsselung: EBS-Verschlüsselung, S3-Verschlüsselung im Ruhezustand

**Azure**:

- **Primärer Standard**: CIS Microsoft Azure Foundations Benchmark
- **Schlüsselcontrols**:
  - Identität: MFA aktiviert, Richtlinien für bedingten Zugang, PIM für privilegierte Rollen
  - Logging: Activity Log Retention ≥ 365 Tage, Diagnostic Settings aktiviert
  - Netzwerk: NSG Default-Deny, kein RDP/SSH aus dem Internet
  - Verschlüsselung: Azure Disk Encryption, Storage Service Encryption

**Google Cloud Platform (GCP)**:

- **Primärer Standard**: CIS Google Cloud Platform Foundation Benchmark
- **Schlüsselcontrols**:
  - IAM: Rotation von Service-Account-Keys, Prinzip der minimalen Rechte
  - Logging: Cloud Audit Logs aktiviert, Log Sinks konfiguriert
  - Netzwerk: VPC-Firewall-Regeln restriktiv, Private Google Access
  - Verschlüsselung: CMEK wo erforderlich, verschlüsselte persistente Festplatten

**1.2.4 Datenbanken**

**SQL Server**:

- **Primärer Standard**: CIS Microsoft SQL Server Benchmark, DISA STIG
- **Schlüsselcontrols**:
  - Windows-Authentifizierungsmodus (kein Mixed Mode)
  - sa-Konto deaktiviert/umbenannt
  - Unnötige Features deaktiviert (xp_cmdshell, OLE Automation usw.)
  - SQL Server Audit aktiviert
  - Verschlüsselung: TDE (Transparent Data Encryption), Always Encrypted für sensible Spalten

**Oracle Database**:

- **Primärer Standard**: CIS Oracle Database Benchmark, DISA STIG
- **Schlüsselcontrols**:
  - Starke Passwortrichtlinie
  - Standardkonten gesperrt
  - Auditing aktiviert
  - Verschlüsselung: TDE, Netzwerkverschlüsselung (Native Network Encryption)

**PostgreSQL/MySQL/MongoDB**:

- **Primärer Standard**: CIS Benchmark für jedes System
- **Schlüsselcontrols**:
  - Authentifizierung erforderlich (kein anonymer Zugang)
  - SSL/TLS-Verbindungen erzwungen
  - Benutzerberechtigungen mit minimalen Rechten
  - Audit-Logging aktiviert

**1.2.5 Container und Orchestrierung**

**Docker**:

- **Primärer Standard**: CIS Docker Benchmark
- **Schlüsselcontrols**:
  - Container als Nicht-Root-Benutzer ausführen
  - Schreibgeschütztes Root-Dateisystem soweit möglich
  - Ressourcenlimits (CPU, Arbeitsspeicher)
  - AppArmor/SELinux-Profile
  - Regelmässiges Image-Scanning auf Schwachstellen

**Kubernetes**:

- **Primärer Standard**: CIS Kubernetes Benchmark
- **Schlüsselcontrols**:
  - RBAC aktiviert und konfiguriert
  - Pod Security Standards durchgesetzt
  - Netzwerkrichtlinien definiert
  - Secrets-Management (externer Secrets-Store)
  - API-Server-Authentifizierung und -Autorisierung
  - etcd-Verschlüsselung im Ruhezustand

**1.2.6 Anwendungen**

**Webserver** (Apache, Nginx, IIS):

- **Primärer Standard**: CIS Benchmark für jedes System
- **Schlüsselcontrols**:
  - Als nicht-privilegierter Benutzer ausführen
  - Unnötige Module deaktiviert
  - Zugriffsprotokollierung aktiviert
  - Ausschliesslich TLS 1.2+, starke Cipher Suites
  - Security-Header (HSTS, X-Frame-Options, CSP)

**Applikationsserver** (JBoss, WebLogic, Tomcat):

- **Primärer Standard**: Herstellersicherheitsleitfaden + CIS Benchmark
- **Schlüsselcontrols**:
  - Standardkonten entfernt
  - Management-Interface in separatem Netzwerk
  - Audit-Logging aktiviert
  - Unnötige Dienste deaktiviert

### Entscheidungsbaum zur Standard-Auswahl

```
START: Welchen Hardening-Standard soll ich verwenden?

├─ Verarbeitet der Asset regulierte Daten (PCI, HIPAA usw.)?
│  ├─ JA → Regulatorisch vorgeschriebenen Standard zuerst verwenden
│  └─ NEIN → Weiter

├─ Gibt es einen CIS Benchmark für diesen Asset-Typ?
│  ├─ JA → CIS Benchmark verwenden (Level 1 Baseline, Level 2 Hochsicherheit)
│  └─ NEIN → Weiter

├─ Gibt es einen herstellerspezifischen Sicherheitsleitfaden?
│  ├─ JA → Herstellerleitfaden verwenden
│  └─ NEIN → Weiter

├─ Ist der Asset-Typ durch NIST-Leitlinien abgedeckt?
│  ├─ JA → NIST-Controls als Referenz verwenden
│  └─ NEIN → Eigene Baseline mit Genehmigung des Security Architects entwickeln

IMMER: Standard-Auswahl in der Baseline-Dokumentation festhalten
```

### Verifizierungsmethoden

**Automatisiertes Scanning**:

- **OpenSCAP**: CIS- und STIG-Compliance-Scanning (Linux/Windows)
- **Nessus/Tenable**: Schwachstellen- und Compliance-Scanning
- **Qualys**: Cloudbasiertes Compliance-Scanning
- **AWS Security Hub**: AWS-spezifische Compliance (CIS AWS Benchmark)
- **Azure Security Center**: Azure-spezifische Compliance
- **GCP Security Command Center**: GCP-spezifische Compliance

**Manuelle Verifizierung**:

- Konfigurationsdateien gegen Baseline prüfen
- Compliance-Check-Skripte ausführen
- Sicherheitscontrols durch Tests validieren
- Befunde und Ausnahmen dokumentieren

**Kontinuierliche Compliance**:

- Scanning in CI/CD-Pipelines integrieren
- Automatisierte Summary-Dashboard-Berichterstattung
- Alarm bei Compliance-Abweichung
- Regelmässige Neubewertung (mindestens vierteljährlich)

---

## Teil 2: Implementierungsleitfaden für das Änderungsmanagement

### Vorlage für das Änderungsantragsformular

**Felder des Änderungsantragsformulars**:

**Abschnitt 1: Änderungsidentifikation**

- Änderungsantrags-ID: [Automatisch generiert oder CR-YYYY-####]
- Einreichungsdatum: [TT.MM.JJJJ]
- Eingereicht von: [Name, Abteilung, Kontakt]
- Änderungstitel: [Kurzer beschreibender Titel, max. 100 Zeichen]
- Änderungsklassifizierung: [Standard / Normal / Notfall]
- Wenn Notfall, Begründung: [Warum kann nicht der normale Prozess abgewartet werden]

**Abschnitt 2: Änderungsbeschreibung**

- Geschäftliche Begründung: [Warum erforderlich? Welches Problem wird gelöst?]
- Technische Beschreibung: [Was genau wird geändert?]
- Betroffene Systeme/Dienste: [Alle betroffenen Assets auflisten]
- Configuration Items (CIs): [CMDB-CI-Nummern sofern vorhanden]

**Abschnitt 3: Auswirkungsbewertung**

- Benutzerauswirkung: [Keine / Minimal / Moderat / Erheblich / Schwerwiegend]
- Erforderliche Dienstunterbrechung: [Keine / < 1 Std. / 1–4 Std. / 4–8 Std. / > 8 Std.]
- Risikoniveau: [Niedrig / Mittel / Hoch / Kritisch]
- Abhängigkeiten: [Andere betroffene Systeme, Dienste, Teams]

**Abschnitt 4: Implementierungsplan**

- Implementierungsschritte: [Detailliertes schrittweises Verfahren]
- Implementierungsdatum/-uhrzeit: [TT.MM.JJJJ HH:MM]
- Implementierungsdauer: [Geschätzte Zeit]
- Implementierungsteam: [Namen und Rollen]
- Benötigte Ressourcen: [Tools, Zugang, Herstellersupport]

**Abschnitt 5: Testing und Validierung**

- Testumgebung: [Dev / Test / Staging / UAT]
- Testdatum: [TT.MM.JJJJ]
- Testergebnisse: [Bestanden / Fehlgeschlagen / Teilweise]
- Testnachweise: [Link zur Testdokumentation]
- Erfolgskriterien: [Wie wird festgestellt, ob die Änderung erfolgreich war]

**Abschnitt 6: Rollback-Plan**

- Rollback-Auslösekriterien: [Wann Rollback durchzuführen]
- Rollback-Verfahren: [Schrittweise Anweisungen]
- Rollback-Dauer: [Geschätzte Zeit]
- Daten-Backup verifiziert: [Ja / Nein / Nicht zutreffend]
- Rollback getestet: [Ja / Nein / Nicht zutreffend — Datum wenn getestet]

**Abschnitt 7: Kommunikation**

- Zu informierende Benutzer: [Verteilerliste]
- Kommunikationsmethode: [E-Mail / Portal / Ankündigung]
- Benachrichtigungszeitpunkt: [Vor / Während / Nach der Änderung]

**Abschnitt 8: Genehmigungen**

- Technische Überprüfung: [Name, Rolle, Entscheidung, Datum, Kommentare]
- Sicherheitsüberprüfung: [Name, Rolle, Entscheidung, Datum, Kommentare]
- CAB-Entscheidung: [Genehmigt / Genehmigt mit Bedingungen / Abgelehnt / Aufgeschoben]
- CAB-Datum: [TT.MM.JJJJ]
- Bedingungen: [Etwaige Genehmigungsbedingungen]

**Abschnitt 9: Nachimplementierungsüberprüfung**

- Tatsächliches Implementierungsdatum/-uhrzeit: [TT.MM.JJJJ HH:MM]
- Implementierungsstatus: [Erfolgreich / Erfolgreich mit Problemen / Fehlgeschlagen / Zurückgerollt]
- Aufgetretene Probleme: [Beschreibung]
- Lösung: [Wie Probleme behoben wurden]
- Gelernte Lektionen: [Was verbessert werden könnte]

### CAB-Sitzungsverfahren

**Vorbereitung der Sitzung (Aufgaben des CAB-Vorsitzes)**:

- Änderungsanträge 48 Stunden vor der Sitzung verteilen
- Sicherstellen, dass alle erforderlichen Genehmigungen eingeholt wurden
- Vollständigkeit vorab prüfen (unvollständige Anträge zurückweisen)
- Sitzungsagenda veröffentlichen

**Während der Sitzung**:

- Jeden Normalen Änderungsantrag prüfen
- Risiko und Auswirkung bewerten
- Testing- und Rollback-Pläne prüfen
- Prioritäten setzen bei Ressourcenkonflikten
- Genehmigungsentscheidung treffen (Genehmigt / Genehmigt mit Bedingungen / Abgelehnt / Aufgeschoben)
- Entscheidung und Begründung dokumentieren

**Nach der Sitzung**:

- Sitzungsprotokoll innerhalb von 24 Stunden veröffentlichen
- Änderungsanforderer über Entscheidungen informieren
- Change-Management-System aktualisieren
- Nächste Sitzung planen

**CAB-Sitzungshäufigkeit**: Wöchentlich oder zweiwöchentlich je nach Änderungsvolumen

### Katalog Standard-Änderungen

Standard-Änderungen sind durch das CAB vorab genehmigt und können ohne individuelle Überprüfung ausgeführt werden. Beispiele:

**Passwort-Resets**:

- Verfahren: Identifikationsverfahren befolgen, Reset in AD/IAM durchführen
- Risiko: Niedrig
- Testing: Nicht erforderlich
- Rollback: Benutzer kann bei Bedarf erneut zurücksetzen

**Zertifikatserneuerungen**:

- Verfahren: CSR generieren, bei CA einreichen, neues Zertifikat installieren
- Risiko: Niedrig (bei gleichen Parametern wie auslaufendes Zertifikat)
- Testing: Zertifikatskette und Ablaufdatum prüfen
- Rollback: Zum vorherigen Zertifikat zurückkehren (falls noch gültig)

**Standard-Software-Patches**:

- Verfahren: Aus genehmigter Patch-Liste in Test, dann Produktion installieren
- Risiko: Niedrig (Patches von genehmigter Herstellerliste)
- Testing: In Testumgebung erforderlich
- Rollback: Patch deinstallieren oder aus Backup wiederherstellen

**Benutzerkontenerstellung/-löschung**:

- Verfahren: Onboarding-/Offboarding-Prozess befolgen
- Risiko: Niedrig
- Testing: Zugang und Berechtigungen prüfen
- Rollback: Konto deaktivieren (Löschung), Konto löschen (Erstellung)

Organisationen pflegen ihren eigenen Katalog für Standard-Änderungen entsprechend ihren operativen Anforderungen und ihrem Risikoappetit.

### Notfalländerungsverfahren

**Wann der Notfalländerungsprozess angewendet wird**:

- Aktiver Sicherheits-Exploit (Schwachstelle wird aktiv ausgenutzt)
- Kritischer Dienstausfall mit Auswirkung auf den Geschäftsbetrieb
- Eindämmung eines Datenlecks
- Kritischer Compliance-Verstoss mit sofortigem Handlungsbedarf

**Wann NICHT anzuwenden**:

- Schlechte Planung („vergessen, Änderungsantrag einzureichen")
- Bequemlichkeit („möchte nicht auf CAB warten")
- Herstellerdruck („Hersteller sagt, muss sofort erledigt werden")

**Notfalländerungs-Workflow**:
1. **Sofortige mündliche Genehmigung**: ITL, ISB oder CAB-Vorsitz telefonisch kontaktieren
2. **Begründung dokumentieren**: Innerhalb von 1 Stunde E-Mail mit Notfallbegründung senden
3. **Änderung implementieren**: Änderung unter Aufsicht ausführen (Vier-Augen-Prinzip wenn möglich)
4. **Implementierung dokumentieren**: Innerhalb von 24 Stunden Änderungsantragsformular mit tatsächlich durchgeführten Schritten ausfüllen
5. **Retrospektive CAB-Überprüfung**: Innerhalb von 5 Arbeitstagen dem CAB zur Überprüfung vorlegen

**Ergebnisse der CAB-Retrospektivüberprüfung**:

- **Genehmigt**: Notfall gerechtfertigt, Änderung angemessen
- **Genehmigt mit Abhilfemassnahmen**: Notfall gerechtfertigt, aber Prozessverbesserungen erforderlich
- **Nicht genehmigt**: Notfall nicht gerechtfertigt, Rückgängigmachung erforderlich oder Disziplinarmassnahmen

---

## Teil 3: Reaktionsverfahren bei Konfigurationsabweichungen

### Erkennung und Triage von Konfigurationsabweichungen

**Schritt 1: Alarmempfang**

- Konfigurationsüberwachungs-Tool erzeugt Konfigurationsabweichungs-Alarm
- Alarm wird an Configuration Manager und System Owner weitergeleitet
- Alarm enthält: Asset-ID, erkannte Änderung, erwarteter Baseline-Wert, tatsächlicher Wert, Erkennungszeitstempel

**Schritt 2: Erste Triage** (innerhalb von 1–4 Stunden je nach Schweregrad)

- Configuration Manager überprüft Alarmdetails
- Prüft das Change-Management-System auf autorisierte Änderungen
- Klassifiziert Konfigurationsabweichung: Autorisiert, Nicht autorisiert oder False Positive

**Schritt 3: Klassifizierungsentscheidung**

**Autorisierte Konfigurationsabweichung**: Änderung war genehmigt, Baseline noch nicht aktualisiert

- Massnahme: Baseline-Dokumentation aktualisieren
- CMDB mit neuer Konfiguration aktualisieren
- Vorfall-Ticket schliessen
- Keine weitere Massnahme

**Nicht autorisierte Konfigurationsabweichung**: Änderung nicht genehmigt oder unbekannt

- Massnahme: Zur Untersuchung übergehen (Schritt 4)

**False Positive**: Fehlkonfiguration des Überwachungs-Tools oder Fehler in der Baseline

- Massnahme: Überwachungsregel anpassen
- Baseline aktualisieren, wenn Baseline fehlerhaft war
- Vorfall-Ticket schliessen

**Schritt 4: Untersuchung nicht autorisierter Konfigurationsabweichungen**

- Systemlogs prüfen, um festzustellen, wer/was die Änderung vorgenommen hat
- Änderungszeitstempel bestimmen
- Beurteilen, ob Änderung böswillig oder Betriebsfehler ist
- Schweregrad klassifizieren (Kritisch / Hoch / Mittel / Niedrig)

**Schritt 5: Incident Response** (bei böswilliger Handlung)

- An Security Operations Center (SOC) eskalieren
- Incident-Response-Verfahren befolgen (ISMS-POL-A.5.24)
- Beweise sichern
- Bedrohung eindämmen

**Schritt 6: Behebung** (bei Betriebsfehler)

- Konfiguration auf Baseline zurücksetzen
- Behebungsmassnahmen dokumentieren
- Grundursachenanalyse durchführen
- Präventive Massnahmen implementieren
- Vorfall-Ticket schliessen

### Ausnahmeantragsprozess

**Wann eine Ausnahme beantragt wird**:

- Baseline-Hardening-Control technisch nicht machbar
- Geschäftsanforderung steht im Widerspruch zur Sicherheits-Baseline
- Herstellerproduktbeschränkung verhindert vollständige Compliance
- Temporäre Ausnahme während Migration/Projekt erforderlich

**Ausnahmeantragsverfahren**:

**Schritt 1: Ausnahmeantragsformular ausfüllen**

- System/Asset, das die Ausnahme benötigt
- Baseline-Control(s), für die Ausnahme benötigt wird
- Geschäftliche Begründung (warum Ausnahme erforderlich)
- Risikobewertung (welches Risiko die Ausnahme einführt)
- Kompensierende Controls (wie das Risiko gemindert wird)
- Beantragter Zeitraum (maximal 12 Monate)
- Plan zur Erreichung vollständiger Compliance (wenn temporär)

**Schritt 2: Sicherheitsüberprüfung**

- Security Architect prüft den Antrag
- Validiert die Risikobewertung
- Prüft, ob kompensierende Controls ausreichend sind
- Empfiehlt Genehmigung/Ablehnung

**Schritt 3: Genehmigungsentscheidung**

- Ausnahmegenehmigungsbefugnis je nach Risikoniveau (gemäss ISMS-POL-A.8.9 Abschnitt 2.5.4)
- Kritisch: Nur ISB
- Hoch: Configuration Manager + Security Architect
- Mittel/Niedrig: Configuration Manager

**Schritt 4: Ausnahmenerfassung**

- Zum Ausnahmenregister hinzufügen
- Ablaufdatum festlegen
- Überprüfung vor Ablauf einplanen
- Kompensierende Controls überwachen

**Schritt 5: Ausnahmenüberprüfung**

- 30 Tage vor Ablauf wird System Owner benachrichtigt
- Optionen: Ausnahme verlängern, vollständige Compliance erreichen, Risiko akzeptieren und dokumentieren
- Verlängerung erfordert denselben Genehmigungsprozess

### Behebungsworkflows

**Behebung kritischer Konfigurationsabweichungen** (< 4 Stunden):
1. SOC und Configuration Manager sofort alarmiert
2. System Owner untersucht innerhalb von 1 Stunde
3. Wenn nicht autorisiert, sofort auf Baseline zurücksetzen
4. Wenn sicheres Zurücksetzen nicht möglich, kompensierende Controls implementieren
5. Massnahmen im Vorfall-Ticket dokumentieren
6. An ISB eskalieren, wenn nach 4 Stunden nicht behoben
7. Post-Incident-Überprüfung innerhalb von 48 Stunden

**Behebung hoher Konfigurationsabweichungen** (< 24 Stunden):
1. Configuration Manager und System Owner benachrichtigt
2. Innerhalb von 4 Stunden untersuchen
3. Behebungsplan entwickeln
4. Behebung innerhalb von 24 Stunden ausführen
5. Konfigurationscompliance verifizieren
6. Im Vorfall-Ticket dokumentieren
7. An Configuration Manager eskalieren, wenn nach 24 Stunden nicht behoben

**Behebung mittlerer Konfigurationsabweichungen** (< 5 Arbeitstage):
1. Configuration Manager weist an System Owner zu
2. System Owner entwickelt Behebungsplan
3. Behebung im Wartungsfenster einplanen
4. Ausführen und verifizieren
5. Baseline aktualisieren, wenn autorisiert
6. Vorfall-Ticket schliessen

**Behebung niedriger Konfigurationsabweichungen** (< 30 Tage):
1. Zum Behebungsrückstand hinzufügen
2. Mit anderen Aufgaben priorisieren
3. Bei verfügbaren Ressourcen beheben
4. Im Vorfall-Ticket dokumentieren

---

## Teil 4: Kurzreferenz

### Wann muss ein Änderungsantrag gestellt werden?

**JA — Änderungsantrag erforderlich**:

- Firewall-Regeln ändern
- Systemkonfigurationen ändern (Betriebssystem, Anwendung, Netzwerk)
- Neue Software installieren
- Software-Versionen upgraden
- Sicherheitseinstellungen ändern
- Dienste hinzufügen/entfernen
- Netzwerkänderungen (Routing, VLANs, ACLs)
- Baseline-Aktualisierungen

**NEIN — Kein Änderungsantrag erforderlich**:

- Passwort-Resets (Standard-Änderung)
- Zertifikatserneuerungen (Standard-Änderung — bei gleichen Parametern)
- Routines Patching aus genehmigter Liste (Standard-Änderung)
- Überwachungsalarme/-benachrichtigungen
- Konfigurationsdateien lesen

**Bei Unsicherheit**: Configuration Manager kontaktieren

### Entscheidungsbaum zur Änderungsklassifizierung

```
START: Welcher Änderungstyp ist das?

├─ Handelt es sich um ein wiederholbares, vorab genehmigtes Verfahren mit niedrigem Risiko?
│  └─ JA → STANDARD-ÄNDERUNG (vorab genehmigt, SOP befolgen)

├─ Handelt es sich um einen dringenden Sicherheitsvorfall oder kritischen Ausfall?
│  └─ JA → NOTFALLÄNDERUNG (beschleunigte Genehmigung)

├─ Alles andere
   └─ NORMALE ÄNDERUNG (CAB-Genehmigung erforderlich)

Wenn NORMALE ÄNDERUNG, wie hoch ist das Risikoniveau?

├─ Begrenzter Umfang, einzelnes System, einfacher Rollback
│  └─ NIEDRIGES RISIKO → Einstufige Genehmigung

├─ Mehrere Systeme, moderate Auswirkung, Standardverfahren
│  └─ MITTLERES RISIKO → Zweistufige Genehmigung

├─ Organisationsweit, kritische Systeme, komplex/ungetestet
   └─ HOHES RISIKO → Dreistufige Genehmigung (CAB)
```

### Wer genehmigt was?

| Änderungsrisiko | Genehmiger | Frist |
|----------------|-----------|-------|
| **Standard** | Vorab genehmigt (SOP befolgen) | Sofort |
| **Normal — Niedrig** | Technical Lead / System Owner | 1–2 Tage |
| **Normal — Mittel** | Technical Lead + Service Owner | 3–5 Tage |
| **Normal — Hoch** | CAB (3-stufig) | 5–10 Tage |
| **Notfall** | ITL oder ISB (mündlich) | < 4 Stunden |

### Häufige Konfigurationsaufgaben

**Baseline für Asset-Typ anzeigen**:

- Zugang: Konfigurations-Repository (SharePoint/CMDB)
- Navigieren zu: Baselines → [Asset-Typ]
- Beispiel: Baselines → Windows Server 2022 → Domain Controller

**Prüfen, ob Baseline vorhanden**:

- Konfigurations-Repository nach Asset-Typ durchsuchen
- Wenn nicht gefunden, Configuration Manager kontaktieren, um Baseline-Erstellung einzuleiten

**Baseline-Ausnahme beantragen**:

- Ausnahmeantragsformular herunterladen
- Alle Felder ausfüllen (geschäftliche Begründung, Risikobewertung, kompensierende Controls)
- Zur Überprüfung an Security Architect einreichen
- Genehmigungsfrist: 5–10 Arbeitstage

**Konfigurationsabweichung melden**:

- Wenn nicht automatisch erkannt, Vorfall-Ticket erstellen
- Angeben: Asset-ID, geänderter Konfigurationsparameter, erwarteter Wert, tatsächlicher Wert
- An Configuration Manager weiterleiten

**Zugang zu Golden Images**:

- Speicherort: [Organisationsspezifisches Image-Repository]
- Erfordert: Berechtigungen des Bereitstellungsteams
- Immer Image-Version und Genehmigungsstatus vor der Verwendung prüfen

### Kontaktinformationen

**Configuration Manager**: [Name], [E-Mail], [Telefon]
**CAB-Vorsitz**: [Name], [E-Mail], [Telefon]
**Security Architect**: [Name], [E-Mail], [Telefon]
**Security Operations Center (SOC)**: [E-Mail], [Telefon], [Bereitschaftsdienst]

**CAB-Sitzungsplan**: [Tag/Uhrzeit], [Meeting-Link/Ort]
**Notfallkontakt**: [24/7-Hotline]

### Häufig gestellte Fragen

**F: Mein Änderungsantrag wurde abgelehnt. Wie geht es weiter?**
A: Ablehnungsgrund prüfen, CAB-Bedenken ausräumen, mit Aktualisierungen erneut einreichen.

**F: Kann ich den Change Control für dringende geschäftliche Anforderungen umgehen?**
A: Nein. Den Notfalländerungsprozess mit ordnungsgemässer Begründung und retrospektiver Überprüfung verwenden.

**F: Wie finde ich die richtige Baseline für mein System?**
A: Konfigurations-Repository nach Betriebssystem und Rolle durchsuchen. Wenn nicht gefunden, Configuration Manager kontaktieren.

**F: Ich habe einen Konfigurationsabweichungs-Alarm für eine autorisierte Änderung erhalten. Was tue ich?**
A: Prüfen, ob Änderung autorisiert war, Baseline-Dokumentation aktualisieren, Vorfall schliessen.

**F: Mein System kann die Baseline aufgrund von Herstellerbeschränkungen nicht erfüllen. Welche Optionen habe ich?**
A: Formelle Ausnahme mit kompensierenden Controls beantragen oder Hersteller wegen Workaround/Upgrade kontaktieren.

**F: Wie oft soll ich meine Systeme gegen Baselines prüfen?**
A: Automatisierte Überwachung prüft kontinuierlich. Manuelle Überprüfungen: Tier 1 (monatlich), Tier 2 (vierteljährlich), Tier 3 (halbjährlich), Tier 4 (jährlich).

---

## Anhang: Dokumentenaktualisierungen

Diese technische Referenz kann häufiger als ISMS-Richtlinien aktualisiert werden, um folgendes widerzuspiegeln:

- Neue Hardening-Standards (CIS Benchmark-Aktualisierungen, neue DISA STIGs)
- Technologieänderungen (neue Cloud-Dienste, Container-Plattformen)
- Entwicklung der Tool-Landschaft (neue Überwachungs-/Scanning-Tools)
- Verfahrensverbesserungen (gelernte Lektionen aus operativer Erfahrung)

Aktualisierungen werden über [Kommunikationskanäle der Organisation] mitgeteilt und erfordern keine Genehmigung der Geschäftsleitung.

**Zuletzt aktualisiert**: [Datum]
**Nächste geplante Überprüfung**: [Datum + 6 Monate]

---

**ENDE DES TECHNISCHEN REFERENZDOKUMENTS**

*Für verbindliche Richtlinienanforderungen siehe ISMS-POL-A.8.9 Konfigurationsmanagement-Richtlinie.*

<!-- QA_VERIFIED: 2026-03-28 -->
