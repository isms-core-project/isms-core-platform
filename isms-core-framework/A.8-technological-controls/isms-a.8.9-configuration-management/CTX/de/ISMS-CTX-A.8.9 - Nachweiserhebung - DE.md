<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.9-nachweiserhebung-DE:framework:CTX:a.8.9 -->
**ISMS-CTX-A.8.9 — Nachweiserhebung**

**Dokumentenkontrolle**

| Attribut | Wert |
|----------|------|
| **Dokument-ID** | ISMS-CTX-A.8.9-evidence-collection |
| **Version** | 1.0 |
| **Dokumenttyp** | Technische Referenz (NICHT ISMS) |
| **Verwandte Richtlinie** | ISMS-POL-A.8.9 (alle Abschnitte) |
| **Zweck** | Standardisierte Nachweisrepository-Struktur für den Nachweis der Compliance mit ISO 27001:2022 Control A.8.9 und die Vorbereitung von Audits bereitstellen |
| **Zielgruppe** | Configuration Manager, Systemadministratoren, Prüfer, Compliance Officers, Nachweis-Custodians |
| **Überprüfungszyklus** | Jährlich (oder bei Änderungen der Prüfanforderungen) |
| **Datum** | [Date] |

### Versionshistorie

| Version | Datum | Änderungen | Autor |
|---------|-------|------------|-------|
| 1.0 | [Date] | Erstversion der Nachweiserhebungsanleitung (NICHT ISMS) | ISMS-Implementierungsteam |

### Genehmiger

- Primär: Configuration Manager
- Technische Überprüfung: Security Architect
- KEINE Genehmigung der Geschäftsleitung erforderlich (NICHT ISMS)

### Verteilung

Konfigurationsmanagement-Team, Systemadministratoren, IT-Betrieb, Security-Ingenieure, Compliance Officers, interne Prüfer, externe Prüfer

### Verwandte Dokumente

- ISMS-POL-A.8.9: Konfigurationsmanagement-Richtlinie (konsolidiert)
- ISMS-CTX-A.8.9: Konfigurationsmanagement Referenz (NICHT ISMS)
- ISMS-IMP-A.8.9-UG: Implementierungsanleitung Konfigurationsmanagement (Benutzer)
- ISMS-IMP-A.8.9-TG: Implementierungsanleitung Konfigurationsmanagement (Technisch)

---

## ⚠️ KRITISCH: Dokumentenstatus

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

**DIESES DOKUMENT DEFINIERT KEINE VERBINDLICHEN ANFORDERUNGEN.**

**DIESES DOKUMENT BEGRÜNDET KEINE BINDENDEN VERPFLICHTUNGEN.**

**ALLE BINDENDEN ANFORDERUNGEN SIND IN ISMS-POL-A.8.9 DEFINIERT.**

**Dies ist ausschliesslich technische Referenz und operative Anleitung für die Nachweiserhebung, -organisation und Auditvorbereitung.**

**Zweck**: Praktische Anleitung für die Organisation von Nachweisen zur Demonstration der Compliance mit Control A.8.9 bei ISO 27001:2022-Audits bereitstellen. Dieses Dokument ergänzt ISMS-POL-A.8.9 und ISMS-IMP-A.8.9, ersetzt jedoch NICHT die Richtlinienanforderungen.

**Zielgruppe**: Nachweis-Custodians, Audit-Koordinatoren, Configuration Manager, die für die Vorbereitung von Audit-Nachweispaketen verantwortlich sind.

**Verwendung**: Referenz für die Einrichtung der Nachweisrepository-Struktur, Namenskonventionen, Aufbewahrungsrichtlinien und Audit-Vorbereitungsworkflows. Organisationen passen diesen Inhalt an ihre spezifischen Dokumentenverwaltungssysteme und Prüfanforderungen an.

**Aktualisierungen**: Dieses Dokument kann häufiger als ISMS-Richtlinien aktualisiert werden, um sich entwickelnde Prüfpraktiken, Dokumentenverwaltungs-Tools und Compliance-Anforderungen widerzuspiegeln. Aktualisierungen erfordern keine Genehmigung der Geschäftsleitung, müssen jedoch an betroffene Mitarbeitende kommuniziert werden.

---

## Übersicht

Diese Anleitung definiert die standardisierte Nachweisrepository-Struktur für ISO 27001:2022 Control A.8.9 (Konfigurationsmanagement). Eine ordnungsgemässe Nachweisorganisation ermöglicht effiziente Audits, demonstriert die Wirksamkeit der Controls und unterstützt die Compliance-Verifizierung.

**Repository-Speicherort**: [Von der Organisation zu definieren — z. B. SharePoint/Netzlaufwerk/Dokumentenverwaltungssystem]

**Zugangskontrolle**: Das Nachweisrepository muss zugangskontrolliert sein: Lesezugang für Prüfer und Compliance Officers, Schreibzugang auf das Konfigurationsmanagement-Team beschränkt.

**Aufbewahrungsfrist**: Mindestens 3 Jahre gemäss ISO 27001:2022-Anforderungen; länger, wenn branchenspezifische Regulierungen dies vorschreiben.

---

## Root-Nachweisstruktur

```
Nachweise/
  ISMS-A.8.9-Basiskonfiguration/
  ISMS-A.8.9-Change-Control/
  ISMS-A.8.9-Konfigurationsüberwachung/
  ISMS-A.8.9-Security-Hardening/
```

---

## Nachweis Basiskonfiguration

**Assessment-Datei**: ISMS-IMP-A.8.9.xlsx (generiert aus Python-Skript)

### Verzeichnisstruktur

**Nachweise/ISMS-A.8.9-Basiskonfiguration/**

#### 1. Asset-Inventar/
Enthält vollständiges Asset-Inventar zur Demonstration der Baseline-Abdeckung.

**Erforderliche Dateien**:

- `CMDB-Export-JJJJMMTT.xlsx` — Vollständiger Export der Configuration Management Database
- `Netzwerk-Scan-Ergebnisse-JJJJMMTT.pdf` — Ergebnisse des Netzwerkentdeckungs-Scans
- `Asset-Kritikalitaets-Klassifizierungen.pdf` — Asset-Tier-Klassifizierungen (Tier 1–4)
- `Cloud-Asset-Inventar-AWS-JJJJMMTT.csv` — AWS-Asset-Inventar
- `Cloud-Asset-Inventar-Azure-JJJJMMTT.csv` — Azure-Asset-Inventar
- `Asset-Inventar-Abgleich-Bericht.xlsx` — Vergleich mehrerer Quellen

**Nachweiszweck**: Belegt, dass ein vollständiges Asset-Inventar vorhanden und die Baseline-Abdeckungsziele messbar sind.

#### 2. Baseline-Dokumentation/
Enthält genehmigte Basiskonfigurationen nach Asset-Typ organisiert.

**Unterverzeichnisse**:

**Windows-Server/**

- `BL-WIN2022-DC-v2.1.docx` — Windows Server 2022 Domain Controller Baseline
- `BL-WIN2022-FS-v1.5.docx` — Windows Server 2022 File Server Baseline
- `BL-WIN2022-APP-v1.8.docx` — Windows Server 2022 Application Server Baseline
- `CIS-Windows-Server-2022-Zuordnung.xlsx` — CIS Benchmark-Zuordnung

**Linux-Unix/**

- `BL-RHEL9-STD-v1.3.pdf` — Red Hat Enterprise Linux 9 Baseline
- `BL-UBUNTU2204-WEB-v2.0.pdf` — Ubuntu 22.04 Webserver Baseline
- `BL-SUSE15-DB-v1.2.pdf` — SUSE Linux 15 Datenbankserver Baseline
- `CIS-Linux-Benchmark-Zuordnung.xlsx` — CIS Benchmark-Zuordnung

**Netzwerkgeraete/**

- `BL-Cisco-ASA-FW-v3.1.pdf` — Cisco ASA Firewall Baseline
- `BL-Palo-Alto-NGFW-v2.5.pdf` — Palo Alto Next-Gen Firewall Baseline
- `BL-Cisco-Switch-IOS-v1.9.pdf` — Cisco Switch IOS Baseline
- `BL-F5-LoadBalancer-v1.4.pdf` — F5 Load Balancer Baseline

**Cloud-Plattformen/**

- `BL-AWS-EC2-Linux-v2.2.pdf` — AWS EC2 Linux-Instanz Baseline
- `BL-AWS-RDS-MySQL-v1.6.pdf` — AWS RDS MySQL Baseline
- `BL-Azure-VM-Windows-v1.8.pdf` — Azure Windows VM Baseline
- `CIS-AWS-Foundations-Benchmark-Zuordnung.xlsx` — CIS AWS-Zuordnung

**Datenbanken/**

- `BL-SQLServer2022-v1.7.pdf` — SQL Server 2022 Baseline
- `BL-PostgreSQL15-v1.4.pdf` — PostgreSQL 15 Baseline
- `BL-Oracle19c-v2.1.pdf` — Oracle 19c Baseline
- `DISA-STIG-Datenbank-Zuordnung.xlsx` — DISA STIG-Zuordnung

**Container/**

- `BL-Docker-v1.5.pdf` — Docker Baseline
- `BL-Kubernetes-v2.0.pdf` — Kubernetes Baseline
- `CIS-Kubernetes-Benchmark-Zuordnung.xlsx` — CIS Kubernetes-Zuordnung

**Namenskonvention**: `BL-[Technologie]-[Rolle]-v[Version].pdf`

- BL = Baseline
- Technologie = Produkt/Plattform (WIN2022, RHEL9 usw.)
- Rolle = Zweck (DC, WEB, APP, DB usw.)
- Version = Semantische Versionierung (Major.Minor)

**Nachweiszweck**: Belegt, dass Baselines vorhanden, dokumentiert sind und auf anerkannte Standards verweisen.

#### 3. Golden-Images/
Enthält Golden-Image-Inventar und Genehmigungsunterlagen.

**Erforderliche Dateien**:

- `Image-Inventar-Register.xlsx` — Hauptliste aller Golden Images
- `WIN2022-STD-v2.1-20240115-Genehmigungsnachweis.pdf` — Image-Genehmigung mit Unterschriften
- `RHEL9-SEC-v1.3-20240120-Genehmigungsnachweis.pdf` — Image-Genehmigung mit Unterschriften

**Image-Build-Manifeste/** (IaC-Code für reproduzierbare Builds):

- `WIN2022-STD-v2.1-BuildManifest.yaml` — Automatisierte Build-Definition
- `RHEL9-SEC-v1.3-BuildManifest.yaml` — Automatisierte Build-Definition

**Schwachstellen-Scans/** (Sicherheitsvalidierung vor Genehmigung):

- `WIN2022-STD-v2.1-SchwachstellenScan-JJJJMMTT.pdf` — Schwachstellen-Scan-Bericht
- `RHEL9-SEC-v1.3-SchwachstellenScan-JJJJMMTT.pdf` — Schwachstellen-Scan-Bericht

**Nachweiszweck**: Belegt, dass Golden Images Baselines implementieren und vor dem Produktiveinsatz sicherheitsvalidiert wurden.

#### 4. Genehmigungsnachweise/
Enthält formelle Genehmigungen für Baselines.

**Erforderliche Dateien**:

- `Baseline-Genehmigungsmatrix.xlsx` — Hauptübersicht aller Baseline-Genehmigungen
- `CAB-Sitzungsprotokoll-JJJJMMTT.pdf` — CAB-Sitzungen, in denen Baselines genehmigt wurden
- `E-Mail-Genehmigung-BL-WIN2022-DC-v2.1.pdf` — E-Mail-Genehmigungsketten
- `ISB-Genehmigung-Baseline-Sicherheitsstandards.pdf` — Genehmigung durch Geschäftsleitung

**Nachweiszweck**: Belegt, dass Baselines über ordnungsgemässe Autorisierung und Governance-Aufsicht verfügen.

#### 5. Konfigurations-Snapshots/
Enthält tatsächliche Konfigurationsexporte zur Demonstration der Baseline-Compliance.

**Erforderliche Dateien**:

- `Server-Konfig-WebServer01-JJJJMMTT.txt` — Tatsächliche Serverkonfiguration
- `Firewall-Regeln-Export-JJJJMMTT.xml` — Firewall-Konfigurationsexport
- `Datenbank-Konfig-DBSERVER01-JJJJMMTT.sql` — Datenbankkonfiguration
- `Kubernetes-Manifest-Export-JJJJMMTT.yaml` — K8s-Konfiguration

**Nachweiszweck**: Belegt, dass eingesetzte Konfigurationen den genehmigten Baselines entsprechen.

#### 6. Abweichungsdokumentation/
Enthält genehmigte Ausnahmen von Baselines.

**Erforderliche Dateien**:

- `Abweichungsregister.xlsx` — Hauptliste aller genehmigten Abweichungen
- `Abweichungsantrag-ABW-2024-001.pdf` — Abweichungsantrag mit geschäftlicher Begründung
- `Risikobewertung-ABW-2024-001.pdf` — Risikoanalyse für Abweichung
- `Kompensierende-Controls-ABW-2024-001.pdf` — Dokumentation der Mitigationsmassnahmen
- `ISB-Genehmigung-ABW-2024-001.pdf` — Genehmigung der Geschäftsleitung

**Namenskonvention**: `ABW-JJJJ-###`, wobei ### eine fortlaufende Nummer ist.

**Nachweiszweck**: Belegt, dass Abweichungen formell mit Risikobewertung und Genehmigung verwaltet werden.

#### 7. Assessment-Berichte/
Enthält abgeschlossene Assessment-Workbooks und Zusammenfassungsberichte.

**Erforderliche Dateien**:

- `Basiskonfigurations-Assessment-JJJJMMTT.xlsx` — Abgeschlossenes ISMS-IMP-A.8.9-Workbook
- `Assessment-Zusammenfassung-Präsentation.pptx` — Management-Zusammenfassung
- `Nachweisregister-Index.pdf` — Index aller erhobenen Nachweise
- `Lücken-Behebungsplan.xlsx` — Massnahmenplan für identifizierte Lücken

**Nachweiszweck**: Belegt, dass regelmässige Bewertung der Baseline-Compliance und Lückenbehebung stattfinden.

---

## Nachweis Change Control

**Assessment-Datei**: ISMS-IMP-A.8.9.xlsx (generiert aus Python-Skript)

### Verzeichnisstruktur

**Nachweise/ISMS-A.8.9-Change-Control/**

#### 1. Änderungsanträge/
Enthält alle Änderungsantragsunterlagen.

**Unterverzeichnisse nach Jahr-Quartal**:

- `2024-Q1/` — Alle Änderungen Q1 2024
- `2024-Q2/` — Alle Änderungen Q2 2024
- usw.

**Pro Änderung**:

- `CR-2024-001-Änderungsantragsformular.pdf` — Ausgefüllter Änderungsantrag
- `CR-2024-001-Risikobewertung.pdf` — Risikoanalyse
- `CR-2024-001-Testergebnisse.pdf` — Testvalidierung
- `CR-2024-001-Implementierungsprotokoll.pdf` — Tatsächliche Implementierungsschritte
- `CR-2024-001-Nachimplementierungs-Review.pdf` — PIR innerhalb von 5 Tagen

**Namenskonvention**: `CR-JJJJ-###`, wobei ### eine fortlaufende Nummer ist.

#### 2. CAB-Unterlagen/
Enthält Change Advisory Board-Sitzungsdokumentation.

**Erforderliche Dateien**:

- `CAB-Sitzungsplan-2024.pdf` — Veröffentlichter CAB-Plan
- `CAB-Mitgliederliste.pdf` — Aktuelle CAB-Mitglieder und Rollen
- `CAB-Charta.pdf` — CAB-Befugnisse und -Verantwortlichkeiten
- `CAB-Sitzungsprotokoll-20240115.pdf` — Sitzungsprotokoll mit Entscheidungen
- `CAB-Sitzungsprotokoll-20240122.pdf` — Sitzungsprotokoll mit Entscheidungen
- `CAB-Anwesenheitsprotokoll-2024.xlsx` — Anwesenheitsverfolgung zur Quorumverifizierung

**Nachweiszweck**: Belegt, dass das CAB regelmässig mit ordnungsgemässer Governance arbeitet.

#### 3. Genehmigungsworkflows/
Enthält Genehmigungsketten für verschiedene Änderungstypen.

**Erforderliche Dateien**:

- `Genehmigungsworkflow-Diagramm.pdf` — Visuelle Darstellung der Genehmigungsstufen
- `Standard-Änderungskatalog.xlsx` — Vorab genehmigte Standard-Änderungen
- `Notfalländerungs-Protokoll.xlsx` — Alle Notfalländerungen mit retrospektiven Überprüfungen
- `Genehmigungsbefugnismatrix.pdf` — Wer was genehmigen kann

#### 4. Testing-Validierung/
Enthält Testpläne und -ergebnisse.

**Pro Hochrisiko-Änderung**:

- `TEST-CR-2024-001-Testplan.pdf` — Formeller Testplan
- `TEST-CR-2024-001-Testergebnisse.xlsx` — Detaillierte Testergebnisse
- `TEST-CR-2024-001-Screenshots.pdf` — Visueller Nachweis
- `TEST-CR-2024-001-RollbackTest.pdf` — Validierung des Rollback-Verfahrens

#### 5. Änderungserfolgs-Kennzahlen/
Enthält KPI-Berichte zum Änderungsmanagement.

**Erforderliche Dateien** (monatlich/vierteljährlich):

- `Änderungs-Kennzahlen-Dashboard-202401.pdf` — Monatlicher Kennzahlenbericht
- `Änderungserfolgsrate-Trendanalyse.xlsx` — Historische Nachverfolgung
- `Notfalländerungs-Analyse-Q1-2024.pdf` — Überprüfung der Notfalländerungsbegründungen
- `Fehlgeschlagene-Änderungen-Grundursachenanalyse.pdf` — Analyse von Rollbacks

**Nachweiszweck**: Belegt die Wirksamkeit des Änderungsmanagements und kontinuierliche Verbesserung.

#### 6. Assessment-Berichte/

- `Change-Control-Assessment-JJJJMMTT.xlsx` — Abgeschlossenes ISMS-IMP-A.8.9-Workbook
- `Assessment-Zusammenfassung-Präsentation.pptx` — Management-Zusammenfassung
- `Nachweisregister-Index.pdf` — Erhobene Nachweise

---

## Nachweis Konfigurationsüberwachung

**Assessment-Datei**: ISMS-IMP-A.8.9.xlsx (generiert aus Python-Skript)

### Verzeichnisstruktur

**Nachweise/ISMS-A.8.9-Konfigurationsüberwachung/**

#### 1. Überwachungsinfrastruktur/
Enthält Nachweise zur Bereitstellung von Überwachungs-Tools.

**Erforderliche Dateien**:

- `Überwachungs-Tool-Inventar.xlsx` — Alle eingesetzten Überwachungs-Tools
- `Überwachungsarchitektur-Diagramm.pdf` — Wie Überwachung eingesetzt wird
- `Überwachungsabdeckungs-Bericht.xlsx` — Asset-Abdeckung nach Tier
- `Überwachungsagent-Bereitstellungsstatus.xlsx` — Agenten-Installationsverfolgung

#### 2. Konfigurationsabweichungs-Alarme/
Enthält Konfigurationsabweichungsalarme und Behebungsmassnahmen.

**Unterverzeichnisse nach Schweregrad**:

- `Kritische-Abweichungen/` — Änderungen an kritischen Sicherheitscontrols
- `Hohe-Abweichungen/` — Änderungen mit hohem Schweregrad
- `Mittlere-Abweichungen/` — Änderungen mit mittlerem Schweregrad
- `Niedrige-Abweichungen/` — Informative Änderungen mit niedrigem Schweregrad

**Pro Konfigurationsabweichungs-Vorfall**:

- `ABW-2024-001-Alarm.pdf` — Ursprünglicher Alarm mit Details
- `ABW-2024-001-Untersuchung.pdf` — Grundursachenuntersuchung
- `ABW-2024-001-Behebung.pdf` — Ergriffene Behebungsmassnahmen
- `ABW-2024-001-Abschluss.pdf` — Vorfallsabschluss mit Verifizierung

**Namenskonvention**: `ABW-JJJJ-###`

#### 3. Baseline-Vergleichsberichte/
Enthält regelmässige Baseline-Compliance-Scans.

**Erforderliche Dateien** (mindestens monatlich für Tier 1, vierteljährlich für Tier 2):

- `Baseline-Compliance-Scan-202401-Tier1.pdf` — Compliance der Tier-1-Assets
- `Baseline-Compliance-Scan-202401-Tier2.pdf` — Compliance der Tier-2-Assets
- `Abweichungs-Trendanalyse-Q1-2024.xlsx` — Trendanalyse

#### 4. Behebungs-Nachverfolgung/
Enthält Nachverfolgung von Konfigurationsabweichungs-Behebungsaktionen.

**Erforderliche Dateien**:

- `Konfigurationsabweichungs-Behebungsregister.xlsx` — Alle offenen/geschlossenen Konfigurationsabweichungs-Vorfälle
- `SLA-Compliance-Bericht.xlsx` — Einhaltung des Behebungs-SLA
- `Wiederkehrende-Abweichungen-Analyse.pdf` — Grundursachenanalyse für wiederkehrende Abweichungen

#### 5. Überwachungsleistung/
Enthält Nachweise zur Gesundheit und Zuverlässigkeit des Überwachungs-Tools.

**Erforderliche Dateien**:

- `Überwachungs-Tool-Verfügbarkeitsbericht.xlsx` — Verfügbarkeitskennzahlen der Tools
- `Alarm-False-Positive-Rate.xlsx` — Wirksamkeit der Alarmkalibrierung
- `Überwachungs-Vorfallsprotokoll.xlsx` — Ausfälle des Überwachungssystems

#### 6. Assessment-Berichte/

- `Überwachungs-Assessment-JJJJMMTT.xlsx` — Abgeschlossenes ISMS-IMP-A.8.9-Workbook
- `Assessment-Zusammenfassung-Präsentation.pptx` — Management-Zusammenfassung
- `Nachweisregister-Index.pdf` — Erhobene Nachweise

---

## Nachweis Security Hardening

**Assessment-Datei**: ISMS-IMP-A.8.9.xlsx (generiert aus Python-Skript)

### Verzeichnisstruktur

**Nachweise/ISMS-A.8.9-Security-Hardening/**

#### 1. Hardening-Standards/
Enthält Dokumentation der Hardening-Standards.

**Erforderliche Dateien**:

- `Hardening-Standards-Register.xlsx` — Alle anwendbaren Standards auf Assets abgebildet
- `CIS-Benchmarks-Bibliothek/` — Heruntergeladene CIS Benchmark PDFs
- `DISA-STIG-Bibliothek/` — Heruntergeladene STIG-Dateien
- `Hersteller-Sicherheitsleitfäden/` — Herstellerspezifische Hardening-Dokumentation
- `Standard-Auswahlbegründung.pdf` — Warum jeder Standard gewählt wurde

#### 2. Compliance-Scans/
Enthält automatisierte Hardening-Compliance-Scans.

**Unterverzeichnisse nach Asset-Typ**:

- `Windows-Server/`
- `Linux-Server/`
- `Netzwerkgeraete/`
- `Datenbanken/`
- `Cloud-Plattformen/`

**Pro Asset-Typ (mindestens vierteljährlich)**:

- `CIS-Scan-WIN2022-202401.pdf` — Compliance-Scan-Ergebnisse
- `CIS-Scan-RHEL9-202401.pdf` — Compliance-Scan-Ergebnisse
- `Compliance-Trendanalyse-Q1-2024.xlsx` — Historische Nachverfolgung

#### 3. Lückenanalyse/
Enthält identifizierte Hardening-Lücken und Behebungspläne.

**Erforderliche Dateien**:

- `Hardening-Lückenregister.xlsx` — Alle identifizierten Lücken
- `Kritische-Lücken-Behebungsplan.xlsx` — Massnahmenplan für kritische Lücken
- `Lücken-Risikobewertung.pdf` — Risikoanalyse für Lücken
- `Behebungsstatus-Dashboard.xlsx` — Fortschrittsverfolgung

#### 4. Hardening-Ausnahmen/
Enthält genehmigte Ausnahmen von Hardening-Standards.

**Pro Ausnahme**:

- `HARD-EX-2024-001-Ausnahmeantrag.pdf` — Formeller Ausnahmeantrag
- `HARD-EX-2024-001-Risikobewertung.pdf` — Risikoanalyse
- `HARD-EX-2024-001-Kompensierende-Controls.pdf` — Mitigationsmassnahmen
- `HARD-EX-2024-001-Genehmigung.pdf` — ISB/Security Architect-Genehmigung

**Namenskonvention**: `HARD-EX-JJJJ-###`

#### 5. Hardening-Implementierung/
Enthält Nachweise der Hardening-Implementierung.

**Erforderliche Dateien**:

- `Pre-Hardening-Scans/` — Baseline vor Hardening
- `Post-Hardening-Scans/` — Validierung nach Hardening
- `Hardening-Skripte/` — Automatisierte Hardening-Skripte
- `Implementierungs-Protokolle/` — Prüfpfad der Hardening-Änderungen

#### 6. Compliance-Berichte/
Enthält reguläre Compliance-Berichterstattung.

**Erforderliche Dateien** (vierteljährlich):

- `Hardening-Compliance-Dashboard-Q1-2024.pdf` — Management-Dashboard
- `Compliance-nach-Asset-Tier-Q1-2024.xlsx` — Tier-basierte Compliance
- `Kritische-Controls-Compliance-Bericht.xlsx` — Fokus auf kritische Controls
- `Jahr-zu-Jahr-Verbesserungsanalyse.pdf` — Reifegradentwicklung

#### 7. Assessment-Berichte/

- `Hardening-Assessment-JJJJMMTT.xlsx` — Abgeschlossenes ISMS-IMP-A.8.9-Workbook
- `Assessment-Zusammenfassung-Präsentation.pptx` — Management-Zusammenfassung
- `Nachweisregister-Index.pdf` — Erhobene Nachweise

---

## Best Practices für die Nachweiserhebung

### Zusammenfassung der Namenskonventionen

**Allgemeines Format**: `[Typ]-[Datum/ID]-[Beschreibung].[Erw]`

**Beispiele**:

- Assessment-Workbooks: `Basiskonfigurations-Assessment-20240315.xlsx`
- Änderungsanträge: `CR-2024-042-Firewall-Regel-Aktualisierung.pdf`
- Konfigurationsabweichungs-Vorfälle: `ABW-2024-018-Nicht-autorisierter-Dienst-Start.pdf`
- Ausnahmen: `HARD-EX-2024-005-Legacy-App-Ausnahme.pdf`
- CAB-Protokolle: `CAB-Sitzungsprotokoll-20240315.pdf`

### Datumformat-Standards

**Alle Datumsangaben in Dateinamen**: Format JJJJMMTT (ISO 8601)

- Korrekt: `20240315`
- Inkorrekt: `03-15-2024`, `15.03.2024`

**Begründung**: Gewährleistet, dass alphabetische Sortierung = chronologische Sortierung

### Dateiformat-Standards

**Bevorzugte Formate**:

- **Formale Dokumente**: PDF/A (Archivformat)
- **Tabellen**: XLSX (Excel) oder CSV (für Datenaustausch)
- **Konfigurationsexporte**: Natives Format (XML, JSON, YAML, TXT)
- **Diagramme**: PDF (aus Visio/draw.io), PNG (wenn keine Interaktivität erforderlich)

**Zu vermeiden**:

- Proprietäre Formate ohne freie Viewer
- Passwortgeschützte Dateien (stattdessen Repository-Zugangskontrolle verwenden)
- Komprimierte Archive (unkomprimiert speichern für Indexierung)

### Nachweisaufbewahrungsregeln

| Nachweistyp | Aufbewahrungsfrist | Begründung |
|-------------|-------------------|------------|
| Assessment-Workbooks | Mindestens 3 Jahre | ISO 27001-Anforderung |
| Änderungsanträge | Mindestens 3 Jahre | Prüfpfad-Anforderung |
| Konfigurationsabweichungs-Vorfälle | Mindestens 3 Jahre | Sicherheitsvorfalls-Nachverfolgung |
| Genehmigungsnachweise | 7 Jahre | Rechtliche/Compliance-Anforderung |
| Konfigurations-Snapshots | 1 Jahr rollierend | Nur operativer Bedarf |
| CAB-Protokolle | Dauerhaft | Governance-Dokumentation |
| Hardening-Scans | 1 Jahr rollierend | Nur operativer Bedarf |

**Branchenspezifische Verlängerungen**:

- Finanzdienstleistungen (FINMA): 10 Jahre
- Gesundheitswesen (HIPAA): 6 Jahre
- Öffentliche Aufträge: Gemäss Vertragsbedingungen

### Qualitätscheckliste für Nachweise

Vor der Ablage von Nachweisen prüfen:

- [ ] Dateiname entspricht der Namenskonvention
- [ ] Datum ist korrekt und im Format JJJJMMTT
- [ ] Datei ist im bevorzugten Format (PDF/XLSX)
- [ ] Dokument ist vollständig (kein Entwurf/unvollständig)
- [ ] Sensible Daten sind angemessen klassifiziert
- [ ] Datei ist nicht beschädigt (zum Prüfen öffnen)
- [ ] Querverweise zu anderen Nachweisen sind korrekt
- [ ] Im korrekten Verzeichnis gemäss dieser Anleitung abgelegt

### Zugangskontrolle für Nachweise

**Lesezugang**:

- Konfigurationsmanagement-Team
- Internes Audit-Team
- Externe Prüfer (während Prüfungszeiträumen)
- Compliance Officers
- ISB und direkte Berichte

**Schreibzugang**:

- Configuration Manager
- Designated Nachweis-Custodians
- Automatisierte Sammelsysteme (Dienstkonten)

**Kein Zugang**:

- Allgemeines IT-Personal (Anfrage über Configuration Manager)
- Externe Parteien ohne NDA
- Ausgeschiedene Mitarbeitende (sofortige Sperrung)

### Automatisierung der Nachweiserhebung

**Empfohlene Automatisierung**:

- **CMDB-Exporte**: Wöchentlicher automatisierter Export
- **Compliance-Scans**: Automatisierte vierteljährliche Scans
- **Konfigurations-Snapshots**: Nächtliches Backup kritischer Konfigurationen
- **Konfigurationsabweichungs-Alarme**: Echtzeit-Export in Nachweisrepository
- **Änderungsantrags-Archivierung**: Automatisch bei Abschluss der Änderung

**Manuelle Erhebung**:

- Genehmigungsunterschriften (Unterschriften erforderlich)
- Risikobewertungen (menschliches Urteilsvermögen erforderlich)
- CAB-Sitzungsprotokolle (menschlich erstellt)
- Vorfallsuntersuchungen (menschliche Analyse erforderlich)

---

## Anhang: Downloads für Nachweisvorlagen

[Organisation sollte Vorlagen bereitstellen für]:

- Änderungsantragsformular (CR-Vorlage.docx)
- Abweichungsantragsformular (ABW-Vorlage.docx)
- Ausnahmeantragsformular (HARD-EX-Vorlage.docx)
- Risikobewertungsvorlage (Risikobewertungs-Vorlage.xlsx)
- CAB-Sitzungsprotokoll-Vorlage (CAB-Protokoll-Vorlage.docx)

**Vorlagen-Speicherort**: [Von der Organisation zu definieren — z. B. SharePoint/Intranet]

---

## Pflege des Nachweisrepository

**Vierteljährliche Überprüfung** (Aufgaben des Configuration Manager):

- Vollständigkeit der Nachweise für das vergangene Quartal prüfen
- Nachweise, die älter als 1 Jahr sind, gemäss Aufbewahrungsplan archivieren
- `Nachweisregister-Hauptindex.pdf` aktualisieren
- Zugangskontrollliste überprüfen (neue/ausgeschiedene Mitarbeitende)
- Backup/Disaster Recovery des Nachweisrepository prüfen

**Jährliche Überprüfung** (Aufgaben des ISB):

- Nachweisrepository-Struktur auf Compliance mit dieser Anleitung prüfen
- Compliance der Aufbewahrungsrichtlinie prüfen
- Qualität und Vollständigkeit der Nachweise bewerten
- Diese Anleitung bei identifizierten Prozessverbesserungen aktualisieren

---

**ENDE DES TECHNISCHEN REFERENZDOKUMENTS**

*Für verbindliche Richtlinienanforderungen siehe ISMS-POL-A.8.9 Konfigurationsmanagement-Richtlinie.*

<!-- QA_VERIFIED: 2026-03-28 -->
