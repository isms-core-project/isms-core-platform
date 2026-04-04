<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.4-DE:framework:POL:a.8.4 -->
**ISMS-POL-A.8.4 — Zugang zu Quellcode**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Zugang zu Quellcode |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.4 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB | Erstfassung für die ISO 27001:2022-Erstzertifizierung |

**Überprüfungsrhythmus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Technischer Leiter (TL) oder VP Engineering
- Compliance: Rechts-/Compliance-Officer
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.8.4.1-UG/TG (Implementierung der Repository-Zugangskontrolle)
- ISMS-IMP-A.8.4.2-UG/TG (Konfiguration des Branch-Schutzes)
- ISMS-IMP-A.8.4.3-UG/TG (Bewertung des Quellcode-Zugangs)
- ISO/IEC 27001:2022 Massnahme A.8.4
- ISMS-POL-A.8.25-26-29 (Sicherer Entwicklungslebenszyklus)
- ISMS-POL-A.5.15-16-18 (Zugangskontrolle / Identitäts- und Zugriffsmanagement)

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für die Zugangssteuerung zu Quellcode fest, um geistiges Eigentum zu schützen und sichere Softwareentwicklungspraktiken gemäss ISO/IEC 27001:2022 Massnahme A.8.4 aufrechtzuerhalten.

**Geltungsbereich**: Diese Richtlinie gilt für alle Quellcode-Repositories (Produktion, interne Werkzeuge, Infrastructure-as-Code, Open-Source-Beiträge, archiviert); alle Entwicklungsartefakte (Bibliotheken, Build-Skripte, Test-Code); alle Repository-Plattformen (GitHub, GitLab, Bitbucket, Azure DevOps, selbst gehostet); und alle Mitarbeitenden, Auftragnehmer und Dritte der Organisation mit Quellcode-Zugang.

**Zweck**: Organisatorische Anforderungen für die Implementierung und Governance der Quellcode-Zugangssteuerung festlegen. Diese Richtlinie legt fest, WAS für Zugangsmassnahmen erforderlich sind und WER dafür verantwortlich ist. Implementierungsverfahren (WIE) sind separat in der ISMS-IMP-A.8.4-Suite dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00, darunter das schweizerische nDSG, die EU DSGVO und ISO/IEC 27001:2022. Bedingt anwendbare sektorspezifische Anforderungen (FINMA, DORA, NIS2) gelten, wenn die Geschäftstätigkeit von [Organisation] deren Anwendbarkeit auslöst.

---

# Massnahmenausrichtung und Geltungsbereich

## ISO/IEC 27001:2022 Massnahme A.8.4

**ISO/IEC 27001:2022 Anhang A.8.4 — Zugang zu Quellcode**

> *Der Zugang zu Quellcode, Entwicklungswerkzeugen und Softwarebibliotheken muss angemessen verwaltet werden.*

**Massnahmenziel**: Organisatorische Richtlinie für Quellcode-Zugangsmassnahmen festlegen, um geistiges Eigentum zu schützen und sichere Softwareentwicklung durch geeignetes Zugangsmanagement zu Quellcode-Repositories und verwandten Entwicklungsartefakten sicherzustellen.

**Diese Richtlinie adressiert**:

- Anforderungen für die Quellcode-Zugangssteuerung basierend auf Repository-Klassifikation und Risikobereitschaft
- Rollenbasierte Zugangskontrolle für Repositories und Entwicklungsartefakte
- Branch-Schutz und Code-Review-Anforderungen
- Anforderungen für das Management und die Verhinderung von Secrets
- Anforderungen an Backup, Wiederherstellung und Prüfprotokollierung
- Management von Drittpartei-Zugängen
- Organisatorische Rollen und Verantwortlichkeiten für die Governance der Quellcode-Zugangssteuerung
- Rahmen für Ausnahmen- und Vorfallmanagement

## Was diese Richtlinie regelt

Diese Richtlinie:

- **Definiert** Anforderungen für die Quellcode-Zugangssteuerung ausgerichtet an Datenklassifikation und regulatorischen Verpflichtungen
- **Legt fest** den Governance-Rahmen für Repository-Zugangsentscheidungen und Verantwortlichkeit
- **Spezifiziert** verbindliche Zugangsmassnahmen für Quellcode-Repositories und Entwicklungsartefakte
- **Verweist** auf anwendbare regulatorische Anforderungen gemäss ISMS-POL-00
- **Identifiziert** organisatorische Rollen und Verantwortlichkeiten für die Quellcode-Zugangssteuerung

## Was diese Richtlinie NICHT regelt

Diese Richtlinie regelt NICHT:

- **Technische Implementierungsdetails** (siehe ISMS-IMP-A.8.4 Implementierungsleitfäden)
- **Plattformspezifische Konfigurationsverfahren** (siehe ISMS-IMP-A.8.4.1 und ISMS-IMP-A.8.4.2)
- **Bewertungsmethoden oder Nachweiserhebungsverfahren** (siehe ISMS-IMP-A.8.4.3)
- **Auswahl von Repository-Plattformen oder -Technologien** (basiert auf Risikobeurteilung von [Organisation])
- **Detaillierte Incident-Response-Verfahren** (integriert mit organisatorischer Incident-Response gemäss A.5.24-27)
- **Sichere Coding-Standards** (abgedeckt durch ISMS-POL-A.8.25-26-29)

**Dokumentenstruktur**:

- **ISMS-POL-A.8.4** (DIESES DOKUMENT): Richtlinienanforderungen (WAS und WER)
- **ISMS-IMP-A.8.4.1**: Implementierungsverfahren für Repository-Zugangskontrolle (WIE)
- **ISMS-IMP-A.8.4.2**: Branch-Schutz-Konfigurationsleitfaden (WIE)
- **ISMS-IMP-A.8.4.3**: Verfahren zur Bewertung des Quellcode-Zugangs (WIE)

## Geltungsbereich

**Diese Richtlinie gilt für**:

- Alle Quellcode-Repositories mit Produktionsanwendungscode, internen Werkzeugen, Infrastructure-as-Code, Konfigurationsmanagement oder Entwicklungsartefakten
- Alle Repository-Plattformen (cloud-gehostete Git-Plattformen, selbst gehostete Git-Plattformen, alternative Versionskontrollsysteme)
- Alle Entwicklungsartefakte (Quellcode, Bibliotheken, Build-Skripte, Test-Code, Dokumentation, Container-Definitionen, CI/CD-Pipelines)
- Alle Mitarbeitenden (Angestellte, Auftragnehmer, Zeitarbeitskräfte) mit Quellcode-Zugangsbedarf
- Alle Drittentwicklungspartner, Offshore-Entwicklungsteams und Sicherheitsprüfer
- Alle Deployment-Modelle (On-Premises, hybride Umgebungen, cloud-gehostete Repositories)

**Nicht im Geltungsbereich**:

- Kompilierte Binärdateien und ausführbare Dateien (abgedeckt durch A.8.1 — Benutzer-Endgeräte)
- Produktionslaufzeit-Konfigurationen (abgedeckt durch A.8.9 — Konfigurationsmanagement)
- Sichere Coding-Standards und -Praktiken (abgedeckt durch ISMS-POL-A.8.25-26-29)
- Änderungsmanagement für Produktions-Deployments (abgedeckt durch A.8.32)
- Kommerzielle Software von Drittparteien ohne Quellcode-Zugang
- Open-Source-Software, die von [Organisation] genutzt aber nicht verändert wird

## Regulatorische Anwendbarkeit

### Stufe 1: Verbindliche Compliance

| Regulierung | Anwendbarkeit | Wesentliche Anforderungen |
|-------------|---------------|--------------------------|
| **ISO/IEC 27001:2022** | Alle Betriebe | A.8.4 — Zugang zu Quellcode muss angemessen verwaltet werden |
| **Schweizerisches nDSG** | Alle Schweizer Betriebe | Art. 8 — Technische und organisatorische Massnahmen zum Schutz von Personendaten umfassen Quellcode-Zugangskontrolle |
| **EU DSGVO** | EU-Datenverarbeitung | Art. 32 — Geeignete technische Massnahmen umfassen Zugangskontrolle zu Systemen mit Personendaten |

### Stufe 2: Bedingte Anwendbarkeit

| Regulierung | Auslösebedingung | Wesentliche Anforderungen |
|------------|-----------------|--------------------------|
| **FINMA** | Schweizer Finanzinstitut | Circular 2023/1 Marginal 50-62 — Informationssicherheit umfasst Quellcode-Schutz |
| **DORA** | EU-Finanzunternehmen | Art. 9 — IKT-Asset-Management umfasst Quellcode; Art. 15 — Incident-Reporting umfasst Quellcode-Kompromittierung |
| **NIS2** | Wesentliche/wichtige Einrichtung | Art. 21(2) — Asset-Management umfasst Quellcode; Art. 23 — Incident-Reporting umfasst Quellcode-Sicherheitsvorfälle |

### Stufe 3: Informationsleitlinien

- NIST SP 800-218: Secure Software Development Framework (Quellcode-Sicherheit)
- CIS Control 16: Anwendungssoftwaresicherheit
- OWASP Code Repository Security Guide

## Integration verwandter Massnahmen

| Massnahme | Beziehung |
|-----------|-----------|
| **A.5.15-16-18 (IAM-Grundlage)** | Liefert grundlegenden IAM-Rahmen; Quellcode-Zugangskontrolle erbt Authentifizierungs- und Identitätsmanagement-Anforderungen |
| **A.8.2-3-5 (Authentifizierung und privilegierter Zugang)** | Repository-Admin-Zugang wird als privilegierter Zugang behandelt |
| **A.8.25-26-29 (Sicherer Entwicklungslebenszyklus)** | A.8.4 ermöglicht sichere Entwicklungsmassnahmen, indem nur autorisiertes Personal Code ändern kann |
| **A.8.32 (Änderungsmanagement)** | Adressiert Änderungsmanagement durch Umgebungen; A.8.4 fokussiert auf Zugangskontrolle vor Deployment |
| **A.5.24-27 (Vorfallmanagement)** | A.8.4 hilft bei der Erkennung von Quellcode-Zugangsvorfällen durch Überwachung |

---

# Zugangskontrollanforderungen

## Repository-Zugangsverwaltung

[Organisation] implementiert rollenbasierte Zugangskontrolle für alle Quellcode-Repositories nach dem Minimalprinzip.

**Zugangskontrollgrundsätze**:

Alle Quellcode-Repositories müssen rollenbasierte Zugangskontrolle (RBAC) implementieren. Standard-Repository-Berechtigungen müssen "kein Zugang" sein — für jede Zugangsstufe ist eine explizite Gewährung erforderlich. Zugang zu Quellcode-Repositories darf nur auf Basis eines dokumentierten geschäftlichen Bedarfs und mit Genehmigung des Repository-Eigentümers gewährt werden. Repository-Zugang muss vierteljährlich auf fortbestehende geschäftliche Begründung überprüft werden. Repository-Zugang muss automatisch widerrufen werden bei Kündigung, Rollenwechsel oder Vertragsablauf.

**Vierteljährlicher Zugangsüberprüfungsprozess**:

- Überprüfungen über standardisiertes Zugriffsüberprüfungsformular (Vorlage in ISMS-IMP-A.8.4.3) durchgeführt
- Repository-Eigentümer überprüft jeden Benutzerzugang und bestätigt: Zugang noch erforderlich (ja/nein), Zugangsstufe angemessen (ja/nein), Massnahme (behalten/ändern/widerrufen)
- Überprüfungsabschluss mit Unterschrift des Repository-Eigentümers und Datum dokumentiert
- Überprüfungsnachweise in Nachweis-Repository aufbewahrt (SharePoint/Confluence ISMS-Nachweisbibliothek oder gleichwertig)
- Keine Reaktion wird nach 10 Arbeitstagen an Entwicklungsmanager eskaliert; nach 15 Arbeitstagen an ISB

**Zugriffsanfrage und -genehmigung**:

Alle Repository-Zugriffsanfragen müssen umfassen: Name und Rolle des Antragstellers, Repository-Name und -Klassifikation, angefragte Zugangsstufe (Lesen/Schreiben/Admin), geschäftliche Begründung und erwartete Dauer bei befristetem Zugang. Genehmigt werden muss durch: Repository-Eigentümer (verbindlich), Entwicklungsteamleiter bei Schreibzugang oder höher, und ISB oder Vertreter bei Admin-Zugang zu Produktions-Repositories. Zugang wird innerhalb von 24 Stunden nach Genehmigung während der Geschäftszeiten bereitgestellt. Alle Zugriffsanfragen und -genehmigungen werden dokumentiert und für Prüfzwecke aufbewahrt (mindestens 3 Jahre). Notfall-Zugriffsanfragen folgen einem beschleunigten Genehmigungsprozess mit nachträglicher Überprüfung innerhalb von 48 Stunden.

**Zugangsprovisionierung und -entzug**:

Repository-Zugang wird wo technisch möglich über zentralisierte Identitätsverwaltungssysteme bereitgestellt. Zugang wird für spezifische Repositories gewährt, nicht pauschal für alle Repositories. Das HR-System löst einen automatisierten Entzugs-Workflow innerhalb von 1 Stunde nach der Verarbeitung einer Kündigung aus. Der Entzug wird innerhalb von 24 Stunden nach dem auslösenden Ereignis über automatisierte Berichte verifiziert.

**Implementierungshinweis**: Zugriffsanfrage-Workflows, Provisionierungsverfahren und Entzugs-Automatisierung sind in ISMS-IMP-A.8.4.1 dokumentiert.

## Repository-Klassifikation und Massnahmen

[Organisation] klassifiziert alle Quellcode-Repositories, um geeignete Schutzstufen zu bestimmen.

**Klassifikationsrahmen**:

- **Produktionscode-Repositories**: Code, der direkt in kundengerichtete oder geschäftskritische Produktionssysteme deployed wird (höchster Schutz)
  - *Beispiele*: Kunden-Webanwendung, Zahlungsverarbeitungsdienst, API-Gateway, Mobile-App-Backend
- **Repositories für interne Werkzeuge**: Code für interne Automatisierung, Dienstprogramme und Betriebswerkzeuge (hoher Schutz)
  - *Beispiele*: CI/CD-Pipeline-Skripte, Monitoring-Dashboards, interne Admin-Werkzeuge, Deployment-Automatisierung
- **Open-Source-Beitrags-Repositories**: Öffentliche oder Open-Source-Projektcode-Repositories mit Beiträgen der Organisation (mittlerer Schutz — kontrollierter öffentlicher Zugang)
  - *Beispiele*: Geforkte Open-Source-Bibliotheken, Community-Beiträge, öffentliche Dokumentation
- **Archivierte/Veraltete Repositories**: Historischer Code, der nicht mehr aktiv entwickelt wird (nur Lesen)
  - *Beispiele*: Legacy-Anwendungscode (eingestellt), frühere Produktversionen, abgeschlossene Proof-of-Concepts

Repository-Klassifikation wird vom Repository-Eigentümer bei der Repository-Erstellung zugewiesen. Repository-Klassifikation wird jährlich überprüft und bei Änderung des Repository-Zwecks aktualisiert.

**Massnahmen basierend auf Klassifikation**:

Produktionscode-Repositories erfordern: mindestens Zwei-Personen-Review für alle Code-Merges, Branch-Schutz auf Haupt- und Release-Branches, signierte Commits wo technisch möglich, tägliches Secret Scanning und vierteljährliche Zugriffsüberprüfungen. Repositories für interne Werkzeuge erfordern: mindestens Ein-Personen-Review für Code-Merges, Branch-Schutz auf Haupt-Branch, wöchentliches Secret Scanning und vierteljährliche Zugriffsüberprüfungen. Open-Source-Beitrags-Repositories erfordern: Zugangskontrolle (nicht öffentlich beschreibbar), Überprüfungsprozess für Beiträge, Secret Scanning vor öffentlichem Push, keine internen Secrets oder Zugangsdaten in öffentlichen Repositories. Archivierte/veraltete Repositories müssen: in den Nur-Lesen-Modus versetzt werden, Schreibzugang von allen Benutzern entfernt haben, Zugriffsprotokolle aufbewahren und als archiviert mit Veraltungsdatum dokumentiert sein.

**Implementierungshinweis**: Repository-Klassifikations-Zuteilungsverfahren und -überprüfungsprozesse sind in ISMS-IMP-A.8.4.1 dokumentiert.

## Rollenbasierte Zugangskontrolle

[Organisation] gewährt Repository-Zugang basierend auf definierten Rollen mit geeigneten Berechtigungen.

**Zugriffsrollen und Berechtigungen**:

**Entwickler** haben Schreibzugang zum Klonen/Pullen von Repositories, Erstellen von Branches/Commits, Pushen auf nicht geschützte Branches, Einreichen von Pull Requests und Zuweisen von Reviewern. Entwickler können nicht auf geschützte Branches pushen, eigene Pull Requests genehmigen oder Repository-Einstellungen ändern.

**Sicherheitsteam** hat Lesezugang zu allen Repositories für Sicherheitsüberprüfungen und Prüfungen, kann Repositories klonen/pullen und Quellcode sowie Commit-Historie lesen. Das Sicherheitsteam kann keine Änderungen einreichen oder Repository-Einstellungen ändern, es sei denn, dies ist ausdrücklich gewährt.

**Prüfer** erhalten befristeten Nur-Lesen-Zugang während des Prüfungszeitraums und Zugang zu Prüfprotokollen und Berechtigungsberichten. Zugang läuft nach Abschluss der Prüfung automatisch ab.

**Externe Auftragnehmer** erhalten befristeten, repository-spezifischen Schreibzugang, der auf die vertragliche Arbeit beschränkt ist. Zugang endet am Vertragsablaufdatum, kein Zugang zu Repositories ausserhalb des Projektumfangs, alle Commits unterliegen verstärkter Überprüfung.

**Repository-Administratoren** verwalten Repository-Einstellungen, konfigurieren Branch-Schutz und verwalten Mitarbeiterzugang. Admin-Zugang gewährt nicht automatisch Code-Schreibzugang (Funktionstrennung), Admin-Aktionen werden protokolliert.

**Repository-Eigentümer** tragen die letztendliche Verantwortung für das Repository, genehmigen Zugriffsanfragen, führen Zugriffsüberprüfungen durch und legen Repository-Klassifikation fest.

**Dienstkonten** (CI/CD, Deployment-Automatisierung, Sicherheitsscanner) werden erstellt mit: beschreibenden Namen, die den Zweck angeben, Zugang beschränkt auf spezifische für die Automatisierung erforderliche Repositories, Token-basierter Authentifizierung mit Ablaufzeit, vierteljährlicher Überprüfung auf fortbestehenden Bedarf und Dokumentation mit Eigentümer und Zweck.

**Vierteljährliche Überprüfungskriterien für Dienstkonten**:

- Ist die Automatisierung/Pipeline noch aktiv? (Letzte Aktivität prüfen; inaktiv > 90 Tage markiert für Entfernung)
- Ist der dokumentierte Eigentümer noch verantwortlich? (Bestätigen, dass Eigentümer noch in der Organisation und noch für die Automatisierung zuständig)
- Ist die Zugangsstufe noch angemessen? (Berechtigungen überprüfen; reduzieren wenn breiter als erforderlich)
- Ist die Token-Ablaufzeit angemessen gesetzt? (Maximal 1 Jahr; 90 Tage für hochprivilegierte Konten empfohlen)
- Massnahme: Behalten (mit Bestätigung), Ändern (Zugang reduzieren) oder Widerrufen (nicht mehr benötigt)

**Durchsetzung des Minimalprinzips**:

Benutzer erhalten die für ihre Rolle minimal erforderliche Zugangsstufe. Admin-Zugang wird sparsam gewährt und auf Personal mit Repository-Verwaltungsverantwortung beschränkt. Externen Auftragnehmern wird ausser in dokumentierten Ausnahmefällen mit ISB-Genehmigung kein "Admin"- oder "Eigentümer"-Zugang gewährt.

**Implementierungshinweis**: Rollenzuweisungsverfahren, Berechtigungsmatrizen und Zugangsbegründungsvorlagen sind in ISMS-IMP-A.8.4.1 dokumentiert.

## Branch-Schutz und Code-Review

[Organisation] implementiert Branch-Schutz, um nicht autorisierte Code-Änderungen zu verhindern und Code-Reviews durchzusetzen.

**Hauptbranch-Schutz**:

Der Hauptbranch (master/main/trunk) von Produktions- und internen Tool-Repositories muss geschützt sein: direkte Commits gesperrt, Pull Request vor Merge erforderlich, Mindestanzahl Reviewer (2 für Produktion, 1 für interne Werkzeuge), veraltete Pull-Request-Genehmigungen bei neuen Commits verworfen, Status-Checks müssen vor Merge bestanden werden (CI/CD-Tests, Linter, Sicherheitsscans), signierte Commits wo technisch möglich, lineare Historie wo technisch möglich. Nur Repository-Administratoren dürfen Branch-Schutzregeln ändern. Temporäre Aufhebung von Branch-Schutzregeln erfordert dokumentierte Begründung, ISB-Genehmigung und automatische Wiederherstellung nach einem bestimmten Zeitraum.

**Release-Branch-Schutz**:

Release-Branches (release/*, hotfix/*) müssen dieselben Schutzanforderungen wie der Hauptbranch haben. Die Erstellung von Release-Branches folgt einer dokumentierten Branching-Strategie und ist der Release-Planung nachvollziehbar zugeordnet.

**Pull-Request-Anforderungen**:

Alle Code-Änderungen an geschützten Branches müssen über Pull Requests eingereicht werden. Pull Requests dürfen nicht vom Code-Autor genehmigt werden (Funktionstrennung). Pull Requests umfassen: klare Beschreibung der Änderungen und des Zwecks, Link zu verwandten Issues/Tickets wo anwendbar, Testnachweis (Testergebnisse, Testabdeckung) und Sicherheitsfolgenabschätzung für sicherheitsrelevante Änderungen. Pull Requests bleiben für einen Mindestüberprüfungszeitraum offen: 4 Stunden für Produktionscode-Änderungen, 1 Stunde für interne Tool-Änderungen, mit Ausnahme für Notfall-Fixes mit nachträglicher Überprüfung.

**Schnellüberprüfung** (reduzierter Überprüfungszeitraum): Risikoarme Änderungen (Dokumentationsupdates, Tippfehler-Korrekturen, reine Konfigurationsänderungen ohne Code-Logik) können eine 1-Stunden-Überprüfungszeit für Produktions-Repositories verwenden, wenn: als "risikoarm" oder "nur-Doku" gekennzeichnet, auf Dokumentations-/Konfigurationsdateien beschränkt, keine ausführbaren Code-Änderungen und vom Code-Eigentümer genehmigt.

**Implementierungshinweis**: Branch-Schutzkonfigurationsverfahren, Pull-Request-Workflows und Code-Review-Standards sind in ISMS-IMP-A.8.4.2 dokumentiert.

## Secret Management

[Organisation] untersagt Secrets in Quellcode-Repositories und implementiert automatisiertes Secret Scanning.

**Verbot von Secrets**:

Quellcode-Repositories dürfen NICHT enthalten: Passwörter/Passphrases/Zugangsdaten, API-Schlüssel/Token/Access Keys, private kryptografische Schlüssel/Zertifikate, Datenbankverbindungsstrings mit eingebetteten Zugangsdaten, SSH-Private-Keys/OAuth-Secrets, Verschlüsselungsschlüssel/Initialisierungsvektoren oder andere sensible Authentifizierungsmaterialien. Konfigurationsdateien, die Secrets erfordern, verwenden Umgebungsvariablen, Secrets-Management-Systeme, verschlüsselte Konfiguration mit externem Schlüsselmanagement oder Konfigurationsvorlagen mit Platzhalterwerten.

**Secret Scanning**:

Alle Repositories müssen automatisiertes Secret Scanning aktiviert haben: Pre-Commit-Scanning (verhindert, dass Secrets in das Repository gelangen), serverseitiges Scanning (erkennt bereits im Repository vorhandene Secrets), Scanfrequenz: Echtzeit für neue Commits und täglich für vollständige Repository-Scans. Secret-Scanning-Befunde lösen aus: sofortige Benachrichtigung an Repository-Eigentümer und Sicherheitsteam, automatische Erstellung eines Behebungstickets und Blockierung des Commits bei aktiviertem Pre-Commit-Scanning. Produktions-Repositories müssen Pre-Commit-Secret-Scanning aktiviert haben.

**Secret-Behebung**:

Entdeckte Secrets müssen behoben werden innerhalb von: 1 Stunde für Secrets in Produktions-Repositories und 24 Stunden für Secrets in Repositories für interne Werkzeuge, mit sofortiger Rotation wenn das Secret bestätigt exponiert oder verwendet wurde. Die Behebung umfasst: sofortige Rotation des exponierten Secrets, Entfernung aus dem Repository (einschliesslich Git-Historie falls notwendig), Folgenabschätzung (wurde das Secret von unbefugten Parteien abgerufen?) und Incident-Reporting gemäss A.5.24-27 falls erforderlich.

**Umgang mit Ausnahmen bei Behebungszeitrahmen**:

- Entdeckung ausserhalb der Geschäftszeiten: Bereitschaftsingenieur über PagerDuty/gleichwertig kontaktiert; 1-Stunden-Frist beginnt ab Bestätigung; bei keiner Bestätigung innerhalb von 30 Minuten Eskalation an sekundären Bereitschaftsdienst
- Falls 1-Stunden-Behebung nicht erreichbar: Sofortige kompensierende Massnahme erforderlich (Secret beim Anbieter deaktivieren, API-Schlüssel widerrufen, betroffenen Dienst sperren); vollständige Behebung innerhalb von 4 Stunden; Ausnahme mit Begründung dokumentiert

**Implementierungshinweis**: Secret-Scanning-Konfiguration, Behebungsverfahren und Entwicklungsschulungsmaterialien sind in ISMS-IMP-A.8.4.1 und ISMS-IMP-A.8.4.2 dokumentiert.

## Authentifizierung und Multi-Faktor-Authentifizierung

[Organisation] erfordert starke Authentifizierung für den Repository-Zugang mit MFA für Produktions-Repositories.

**Authentifizierungsmethoden**:

Zugang zu Quellcode-Repositories muss authentifiziert werden über: Benutzername/Passwort (mit MFA erforderlich), SSH-Public-Key-Authentifizierung, persönliche Zugriffstoken (mit Ablaufzeit), zertifikatsbasierte Authentifizierung oder Single Sign-On (SSO) über den organisatorischen Identity Provider.

**Multi-Faktor-Authentifizierung**:

MFA ist verbindlich für: alle menschlichen Benutzerkonten mit Schreib- oder Admin-Zugang zu Produktions-Repositories, alle menschlichen Benutzerkonten mit Admin-Zugang zu beliebigen Repositories und webbasierten Repository-Zugang für alle Nutzer. Akzeptierte MFA-Methoden: Authenticator-Anwendungen, Hardware-Sicherheitsschlüssel (YubiKey), Push-Benachrichtigung an registriertes Mobilgerät, SMS-basierte Codes (am wenigsten bevorzugt). Dienstkonten und Automatisierungswerkzeuge verwenden Token-basierte Authentifizierung mit eingeschränkten Geltungsbereichen anstelle von MFA.

**Begründung der MFA-Ausnahme für Dienstkonten**: Dienstkonten können keine interaktive MFA durchführen; kompensierende Massnahmen angewendet: Tokens mit minimal erforderlichen Geltungsbereichen ausgestellt, Token-Ablaufzeit durchgesetzt, Dienstkonto-Aktivität protokolliert und auf Anomalien überwacht, vierteljährliche Überprüfung auf fortbestehenden Bedarf und angemessenen Zugang.

**Implementierungshinweis**: Authentifizierungskonfiguration, MFA-Registrierungsverfahren und SSH-Schlüsselverwaltung sind in ISMS-IMP-A.8.4.1 dokumentiert.

## Prüfprotokollierung und Überwachung

[Organisation] implementiert umfassende Protokollierung und Überwachung von Repository-Zugang und -Aktivitäten.

**Protokollierungsanforderungen**:

Repository-Plattformen müssen protokollieren: Zugangsereignisse (Anmeldeversuche, Abmeldeereignisse), Repository-Zugang (Klonen, Pull-Operationen), Code-Änderungen (Commits mit Autor/Zeitstempel/Nachricht/Dateien, Pushes, Force-Pushes), Branch-Operationen, Pull-Request-Aktivitäten, Berechtigungsänderungen, administrative Aktionen und Sicherheitsereignisse (Secret-Scanning-Alarme, fehlgeschlagene Authentifizierung). Protokolle umfassen Mindest-Metadaten: Zeitstempel (UTC), Nutzeridentität, Quell-IP-Adresse, durchgeführte Aktion, betroffenes Repository und Erfolg/Misserfolg.

**Protokollaufbewahrung**:

Repository-Zugriffsprotokolle müssen aufbewahrt werden für: Zugangsereignisse 1 Jahr, Code-Änderungsereignisse 3 Jahre, Berechtigungsänderungen 3 Jahre, Sicherheitsereignisse 3 Jahre und administrative Aktionen 3 Jahre.

**Protokollüberwachung und Alarmierung**:

Repository-Zugriffsprotokolle werden überwacht auf: mehrfache fehlgeschlagene Authentifizierungsversuche, Zugang aus ungewöhnlichen geografischen Standorten, Zugang ausserhalb der normalen Geschäftszeiten, Massenhervorgabe-Operationen, Versuche zur Berechtigungserweiterung, Force-Pushes auf geschützte Branches und Secret-Scanning-Alarme. Sicherheitsalarme werden innerhalb von 15 Minuten nach Erkennung an das Security-Operations-Team gesendet.

**Implementierungshinweis**: Protokollierungskonfiguration, Überwachungsregeln und Alarmierungsverfahren sind in ISMS-IMP-A.8.4.3 dokumentiert.

## Backup und Wiederherstellung

[Organisation] implementiert regelmässige Backups von Quellcode-Repositories mit getesteten Wiederherstellungsverfahren.

**Backup-Anforderungen**:

Alle Quellcode-Repositories müssen gesichert werden mit: Häufigkeit tägliche inkrementelle Backups und wöchentliche vollständige Backups, Aufbewahrung mindestens 90 Tage für aktive Repositories und 7 Jahre für Produktions-Repositories, und geografischer Redundanz (Backups an einem anderen geografischen Standort als das primäre Repository). Backups umfassen: Quellcode (alle Branches, alle Commits, vollständige Historie), Repository-Metadaten, Pull-Request-Historie und Diskussionen, Issue-Tracking-Daten falls integriert sowie Wikis und Dokumentation.

**Wiederherstellungstests**:

Repository-Wiederherstellungsverfahren werden getestet: vierteljährlich für Produktions-Repositories, jährlich für Repositories interner Werkzeuge und nach grösseren Plattform-Upgrades oder Konfigurationsänderungen. Wiederherstellungstests verifizieren: Repository-Wiederherstellung innerhalb des Recovery Time Objective (RTO: 4 Stunden für Produktion, 24 Stunden für Nicht-Produktion), Datenintegrität (alle Commits, Branches, Historie intakt) und Funktionsfähigkeit des wiederhergestellten Repositories.

**Wiederherstellungstest-Methodik**:

- Tests in isolierter Testumgebung durchgeführt (nicht Produktion)
- Repräsentatives Stichproben-Testen akzeptabel: mindestens 3 Produktions-Repositories pro Quartal
- Simulierte Wiederherstellung (in Testumgebung wiederherstellen, Integrität verifizieren, RTO messen) ist akzeptabel
- Jährlicher Gesamttest umfasst mindestens eine vollständige Produktions-Repository-Wiederherstellung mit Berechtigungsvalidierung

**Implementierungshinweis**: Backup-Konfigurationsverfahren, Wiederherstellungstest-Methodik und RTO-Ziele sind in ISMS-IMP-A.8.4.1 dokumentiert.

## Management von Drittpartei-Zugängen

[Organisation] implementiert zusätzliche Massnahmen für Drittpartei-Entwicklerzugang zu Quellcode-Repositories.

**Anforderungen für Drittpartei-Zugang**:

Drittpartei-Entwickler, Auftragnehmer und Offshore-Entwicklungsteams müssen: Geheimhaltungsvereinbarungen (NDAs) vor Gewährung des Repository-Zugangs unterzeichnen, Zugang auf spezifische für die vertragliche Arbeit erforderliche Repositories beschränkt haben, befristeten Zugang entsprechend der Vertragsdauer haben, Zugang automatisch widerrufen bei Vertragsablauf und verstärkten Code-Review-Anforderungen unterliegen. Alle Code-Beiträge von Drittparteien erfordern Code-Review durch einen internen Entwickler (mindestens ein Reviewer) und Sicherheitsüberprüfung für sicherheitsrelevante Änderungen.

**Implementierungshinweis**: Drittpartei-Zugriffsverfahren, Überwachungsanforderungen und Code-Review-Standards sind in ISMS-IMP-A.8.4.1 und ISMS-IMP-A.8.4.2 dokumentiert.

## Ausnahmenmanagement

**Ausnahmeanfrageprozess**:

Ausnahmen zu dieser Richtlinie werden beantragt mit: spezifischen Anforderungen, die eine Ausnahme erfordern, geschäftlicher Begründung, kompensierenden Massnahmen (falls anwendbar), beantragter Ausnahmedauer und Risikobewertung und -akzeptanz. Genehmigt werden muss durch: Repository-Eigentümer (verbindlich), Informationssicherheitsmanager (verbindlich) und ISB (für Produktions-Repository-Ausnahmen). Ausnahmen werden für begrenzte Zeiträume gewährt (maximal 12 Monate) und erfordern Erneuerung.

**Implementierungshinweis**: Ausnahmeanfrageverfahren, Genehmigungsworkflows und Bewertungsmethodik für kompensierende Massnahmen sind in ISMS-IMP-A.8.4.3 dokumentiert.

---

# Rollen, Governance und Compliance

## Rollen und Verantwortlichkeiten

**Informationssicherheitsbeauftragter (ISB)**:

- Gesamtverantwortung für Richtlinie und Implementierung der Quellcode-Zugangskontrolle
- Genehmigung von Ausnahmen zu Richtlinienanforderungen
- Genehmigung von Admin-Zugang zu Produktions-Repositories
- Aufsicht über Sicherheitsvorfälle mit Quellcode-Zugang
- Jährliche Richtlinienüberprüfung und -aktualisierungen

**Technischer Leiter (TL) / VP Engineering**:

- Verantwortung für Auswahl und Konfiguration der Entwicklungsplattform
- Genehmigung von Repository-Klassifikationen
- Eskalationsstelle bei Zugriffsstreitigkeiten
- Compliance des Entwicklungsteams mit Richtlinienanforderungen

**Informationssicherheitsmanager**:

- Pflege und Aktualisierungskoordination der Richtlinie
- Ausnahmenüberprüfung und -genehmigung (Nicht-Produktions-Repositories)
- Sicherheitsüberwachung und Vorfalluntersuchung
- Koordination und Nachweis für Prüfungen

**Repository-Eigentümer**:

- Zuweisung der Repository-Klassifikation
- Genehmigung von Zugriffsanfragen
- Vierteljährliche Zugriffsüberprüfungen
- Pflege der Repository-Sicherheitskonfiguration

**Entwicklungsteamleiter**:

- Zugriffsanfragenüberprüfung für Teammitglieder
- Durchsetzung des Code-Review-Prozesses
- Entwicklerschulung zu sicheren Repository-Praktiken

**Sicherheitsteam**:

- Konfiguration von Sicherheitsüberwachung und Alarmierung
- Management von Secret-Scanning-Werkzeugen
- Sicherheitsprüfungen und -bewertungen
- Incident-Response für Quellcode-Sicherheitsvorfälle

**IT-Betrieb**:

- Pflege und Verfügbarkeit der Repository-Plattform
- Implementierung von Backup und Wiederherstellung
- Automatisierung der Zugangsprovisionierung/-entzug

**Einzelne Entwickler und Auftragnehmer**:

- Einhaltung von Zugangsmassnahmen und Authentifizierungsanforderungen
- Schutz von Zugangsdaten (Passwörter, SSH-Schlüssel, Token)
- Keine Speicherung von Secrets in Repositories
- Teilnahme an Code-Reviews

## Compliance-Überwachung und Reporting

Der Informationssicherheitsmanager überwacht die Richtlinien-Compliance durch vierteljährliche Zugangskontrollbewertungen, kontinuierliche Secret-Scanning-Überwachung, Protokollanalyse und Anomalieerkennung sowie Prüfung der Branch-Schutzkonfigurationen. Compliance-Status wird berichtet: monatlich an ISB (Zusammenfassungs-Dashboard), vierteljährlich an Geschäftsleitung (detaillierter Bericht) und jährlich an den Vorstand (strategischer Überblick).

## Nichteinhaltungskonsequenzen

Richtlinienverletzungen führen zu: geringfügigen Verletzungen (schriftliche Verwarnung, verbindliche Nachschulung), moderaten Verletzungen (Zugangssperrung, formelles Disziplinarverfahren) oder schwerwiegenden Verletzungen (Zugangsentzug, mögliche Kündigung, rechtliche Schritte).

---

# Nachweise für diese Richtlinie

**Stage 1 (Dokumentationsüberprüfung) Nachweise:**

- Dieses Richtliniendokument (ISMS-POL-A.8.4 v1.0)
- Genehmigungsunterschriften von ISB, TL, Geschäftsleitung
- Anforderungen für Repository-Zugangskontrolle definiert
- Branch-Schutzanforderungen dokumentiert
- Secret-Management-Anforderungen spezifiziert
- Authentifizierungsanforderungen dokumentiert
- Rollen und Verantwortlichkeiten zugewiesen

**Stage 2 (Operationale Wirksamkeit) Nachweise:**

- Inventar der Repositories mit Klassifikation/Eigentümer/Metadaten
- Benutzer-zu-Repository-Zugriffsmatrix
- Zugriffsanfrage-Genehmigungsunterlagen
- Vierteljährliche Zugriffsüberprüfungs-Abschlussunterlagen
- NDA-Unterschriftsnachweise
- Konfigurationen des Branch-Schutzes
- Secret-Scanning-Konfiguration und Protokolle
- MFA-Registrierungsberichte (100 % Abdeckung)
- Backup-Ausführungsprotokolle und Wiederherstellungstestergebnisse

## Compliance-Bewertung

**Gesamtpunktzahl Quellcode-Sicherheit** (0–100 %): Repository-Zugangscompliance 35 %, Branch-Schutz-Compliance 35 %, Secret-Management-Compliance 20 %, Drittpartei-Zugangscompliance 10 %

**Compliance-Ziele**: Reifes ISMS ≥ 90 % Gesamtcompliance, Neues ISMS ≥ 70 % Compliance innerhalb von 180 Tagen

---

# Inkrafttreten und Übergang

## Inkrafttreten

**Inkrafttretungsdatum**: [30 Tage nach Genehmigung durch Geschäftsleitung]

Diese Richtlinie tritt 30 Tage nach Genehmigung durch das Geschäftsleitung in Kraft.

## Übergangszeitplan

**Sofort (0–30 Tage)** — Kritische Massnahmen: Zugriffsüberprüfungen für Produktions-Repositories, Aktivierung des Secret Scannings, Notfall-Zugangsentzugsverfahren, MFA-Durchsetzung für Produktions-Repositories

**Kurzfristig (30–90 Tage)** — Kernimplementierungen: Branch-Schutz-Implementierung, Zugangsdokumentation und Inventar, Abschluss der Repository-Klassifikation, vierteljährlicher Zugriffsüberprüfungsprozess

**Mittelfristig (90–180 Tage)** — Vollständige Compliance: Vollständige Compliance über alle Repositories, Deployment der automatisierten Überwachung, Backup- und Wiederherstellungstests, Schulungsabschluss für alle Mitarbeitenden

**Langfristig (180–365 Tage)** — Optimierung: Automatisierungsverbesserung, Prozessoptimierung, erweiterte Überwachung und Analytik

---

# Genehmigungsnachweis

| Rolle | Name | Unterschrift | Datum |
|-------|------|-------------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | _________________ | [Date to be set] |
| **Technischer Leiter (TL)** | [Name] | _________________ | [Date to be set] |
| **Rechts-/Compliance-Officer** | [Name] | _________________ | [Date to be set] |
| **Geschäftsführer (GF)** | [Name] | _________________ | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen für die Quellcode-Zugangskontrolle fest. Implementierungsverfahren sind in ISMS-IMP-A.8.4.1 (Repository-Zugangskontrolle), ISMS-IMP-A.8.4.2 (Branch-Schutz) und ISMS-IMP-A.8.4.3 (Bewertung des Quellcode-Zugangs) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
