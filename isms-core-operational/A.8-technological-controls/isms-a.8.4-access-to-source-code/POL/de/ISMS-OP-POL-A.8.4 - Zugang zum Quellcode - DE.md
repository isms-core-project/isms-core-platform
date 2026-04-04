<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.4-DE:operational:OP-POL:a.8.4 -->
**ISMS-OP-POL-A.8.4 — Zugang zum Quellcode**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Zugang zum Quellcode |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.4 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.8.4 — Access to source code
- ISO/IEC 27002:2022 Section 8.4 — Implementation guidance for source code access control
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1
- CIS Controls v8 — Safeguard 16.1–16.14 (Application Software Security)

**Verwandte Annex-A-Controls**:

| Control | Bezug zum Quellcode-Zugang |
|---------|---------------------------|
| A.5.9 Inventar von Informationen und anderen zugehörigen Assets | Quellcode-Repositories im Asset-Inventar enthalten |
| A.5.15–16–18 Identitäts- und Zugangsverwaltung | Grundlegendes IAM-Framework; Authentifizierung und Autorisierung für Repositories |
| A.5.19–23 Lieferanten- und Cloud-Dienste-Sicherheit | Zugang für Drittentwickler und Cloud-Repository-Kontrollen |
| A.8.2–3–5 Authentifizierung und privilegierter Zugang | MFA-Anforderungen; Admin-Zugang wird als privilegiert behandelt |
| A.8.9 Konfigurationsmanagement | Konfigurationsbaselines für Repository-Plattformen |
| A.8.15 Protokollierung | Audit-Protokollierung für Repository-Zugang und Code-Änderungen |
| A.8.25–26–29 Sicherer Entwicklungslebenszyklus | Sicheres Kodieren, Branch-Schutz, Code-Review-Integration |
| A.8.32 Änderungsmanagement | Änderungskontrolle für Code-Bereitstellungen in Produktion |

**Verwandte interne Richtlinien**:

- Identitäts- und Zugangsverwaltungsrichtlinie
- Richtlinie für den sicheren Entwicklungslebenszyklus
- Protokollierungsrichtlinie
- Änderungsmanagementrichtlinie
- Richtlinie zur Informationsklassifizierung und -handhabung

---

# Richtlinie zum Zugang zum Quellcode

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass Lese- und Schreibzugang zu Quellcode, Entwicklungstools und Softwarebibliotheken angemessen verwaltet wird, um geistiges Eigentum zu schützen, die Einführung nicht autorisierter Funktionalität zu verhindern, unbeabsichtigte oder böswillige Änderungen zu vermeiden und die Vertraulichkeit organisationaler Software-Assets zu wahren.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem technische und organisatorische Massnahmen dem Risiko entsprechend implementiert werden, um personenbezogene Daten zu schützen, die in Quellcode-Systemen eingebettet oder durch diese verarbeitet werden. Soweit die Organisation Daten von Personen in der EU/im EWR verarbeitet, gelten auch die Anforderungen der DSGVO Art. 32. Die Quellcode-Zugangskontrolle ist eine wichtige technische Massnahme, um nachzuweisen, dass Systeme, die personenbezogene Daten verarbeiten, angemessenen Zugangsrestriktionen unterliegen.

## Geltungsbereich

Quellcode-Repositories, Entwicklungstools und Softwarebibliotheken, die der Organisation gehören, von ihr verwaltet oder kontrolliert werden und gemäss ISO-27001-Geltungsbereichserklärung als in den Geltungsbereich fallend eingestuft sind. Dies umfasst:

- Alle Quellcode-Repositories (Produktionsanwendungen, interne Tools, Infrastructure-as-Code, Konfigurationsmanagement, Open-Source-Beiträge, archivierter Code).
- Alle Repository-Plattformen ([Repository Platform] — z. B. GitHub Enterprise, GitLab, Bitbucket, Azure DevOps oder selbst gehosteter Git-Server). Die Organisation soll ihre primären Repository-Plattform(en) im Asset-Inventar dokumentieren, einschliesslich: Hosting-Modell (Cloud-Hosting vs. selbst gehostet), Datenspeicherort, Backup-Vereinbarungen und administrative Zugangskontrolle. Wenn mehrere Plattformen verwendet werden, gilt diese Richtlinie gleichermassen für alle Plattformen.
- Alle Entwicklungs-Artefakte (Quellcode, Bibliotheken, Build-Skripte, Testcode, Container-Definitionen, CI/CD-Pipeline-Definitionen).

Alle Mitarbeitenden, Auftragnehmer und Drittnutzer mit Quellcode-Zugang.

**Nicht im Geltungsbereich**: Kompilierte Binärdateien und ausführbare Dateien; Produktionslaufzeit-Konfigurationen (abgedeckt durch A.8.9); sichere Kodierungsstandards (abgedeckt durch A.8.25-26-29); kommerzielle Drittanbietersoftware, auf deren Quellcode die Organisation keinen Zugang hat.

## Grundsatz

Der Quellcode-Zugang soll dem Prinzip der minimalen Rechtevergabe folgen. Zugang wird nur auf Basis eines dokumentierten Geschäftsbedarfs und mit Genehmigung des Repository-Eigentümers gewährt.

Die Organisation soll den Zugang zu Quellcode-Repositories zentral über ein Quellcode-Managementsystem verwalten. Standardmässige Repository-Berechtigungen sollen „kein Zugang" sein — für jede Zugangsstufe ist eine explizite Gewährung erforderlich.

Quellcode wird als kritisches organisationales Asset eingestuft. Nicht autorisierter Zugang, Modifikation oder Offenlegung von Quellcode kann zu Verlust von geistigem Eigentum, Einführung von Schwachstellen, regulatorischer Nichtkonformität oder Reputationsschäden führen.

---

## Repository-Klassifizierung

Alle Quellcode-Repositories sollen klassifiziert werden, um angemessene Schutzniveaus zu bestimmen.

**Klassifizierungskategorien**:

| Klassifizierung | Beschreibung | Beispiele |
|-----------------|--------------|-----------|
| **Produktion** | Code, der in kundenseitigen oder geschäftskritischen Produktionssystemen eingesetzt wird | Kunden-Webanwendung, Zahlungsverarbeitungsdienst, API-Gateway, mobile App-Backend |
| **Interne Tools** | Code für interne Automatisierung, Hilfsprogramme und Betriebstools | CI/CD-Pipeline-Skripte, Monitoring-Dashboards, interne Admin-Tools, Deployment-Automatisierung |
| **Open Source** | Öffentlicher oder Open-Source-Projektcode, zu dem die Organisation beiträgt | Geforkte Open-Source-Bibliotheken, Community-Beiträge, öffentliche Dokumentation |
| **Archiviert** | Historischer Code, der sich nicht mehr in aktiver Entwicklung befindet | Legacy-Anwendungscode (eingestellt), frühere Produktversionen, abgeschlossene Machbarkeitsstudien |

Die Repository-Klassifizierung soll vom Repository-Eigentümer bei der Erstellung zugewiesen und jährlich überprüft werden. Die Klassifizierung soll aktualisiert werden, wenn sich der Repository-Zweck ändert.

**Übernommene und ruhende Repositories**: Repositories, die übernommen wurden (z. B. durch Akquisition, Umstrukturierung des Teams oder Weggang von Entwicklern) oder ruhend sind (keine Commits seit >12 Monaten), sollen wie folgt behandelt werden:

- **Übernommene Repositories**: Der aufnehmende Team-Lead soll innerhalb von 5 Arbeitstagen als interimistischer Repository-Eigentümer zugewiesen werden. Das Repository soll innerhalb von 30 Tagen auf Klassifizierungsgenauigkeit, Zugangsberechtigung und Secret-Scanning-Konformität überprüft werden.
- **Ruhende Repositories**: Repositories ohne Commit-Aktivität seit 12 Monaten sollen zur Überprüfung markiert werden. Der Repository-Eigentümer soll bestätigen: (a) das Repository wird noch benötigt (behalten mit aktueller Klassifizierung), (b) das Repository soll archiviert werden (in die Klassifizierung „Archiviert" verschieben, auf Lesezugang beschränken), oder (c) das Repository soll gelöscht werden (Datenaufbewahrungsrichtlinie befolgen). Keine Reaktion nach 30 Tagen führt zur automatischen Archivierung mit Benachrichtigung an den Entwicklungsmanager.

---

## Rollenbasierte Zugriffskontrolle

Repository-Zugang soll auf Basis definierter Rollen mit den minimal erforderlichen Berechtigungen gewährt werden.

**Zugangsstufen**:

| Rolle | Berechtigungen | Einschränkungen |
|-------|----------------|-----------------|
| **Entwickler** | Klonen, Pullen, Branches erstellen, in nicht geschützte Branches pushen, Pull Requests einreichen | Kann nicht in geschützte Branches pushen, eigene Pull Requests genehmigen oder Repository-Einstellungen ändern |
| **Sicherheitsreviewer** | Lesezugang auf alle Repositories für Sicherheitsreviews und Audits | Kann keine Änderungen committen oder Einstellungen ändern, sofern nicht explizit gewährt |
| **Auditor** | Zeitlich begrenzter, schreibgeschützter Zugang während des Auditszeitraums; Zugang zu Audit-Protokollen und Berechtigungsberichten | Zugang läuft nach Abschluss des Audits automatisch ab |
| **Externer Auftragnehmer** | Zeitlich begrenzter, repository-spezifischer Schreibzugang, begrenzt auf vertraglich vereinbarte Arbeiten | Kein Zugang zu Repositories ausserhalb des Projektumfangs; alle Commits unterliegen erweiterter Überprüfung; Zugang läuft am Vertragsende ab |
| **Repository-Administrator** | Verwaltung von Repository-Einstellungen, Branch-Schutz und Mitarbeiter-Zugang | Admin-Zugang gewährt nicht automatisch Code-Schreibzugang (Funktionstrennung); Admin-Aktionen werden protokolliert |
| **Repository-Eigentümer** | Zugriffsanfragen genehmigen, Zugriffsüberprüfungen durchführen, Klassifizierung festlegen | Kann je nach Rolle Code-Schreibzugang haben oder nicht |
| **Dienstkonto** | Automatisierter Zugang für CI/CD, Deployment und Sicherheits-Scanning-Tools | Beschreibende Benennung; tokenbasierte Authentifizierung mit Ablauf; Zugang auf spezifische Repositories beschränkt; dokumentierter Eigentümer und Zweck. Token-Scopes sollen minimiert werden — z. B. CI-Build: `repo:read`, `actions:write`; Deployment: `repo:read`, `packages:write`; Sicherheits-Scanner: `repo:read`, `security_events:write` |

Admin- oder Eigentümerzugang soll externen Auftragnehmern nur in dokumentierten Ausnahmefällen mit ISB-Genehmigung gewährt werden.

---

## Zugriffsanforderung und -genehmigung

Alle Repository-Zugriffsanfragen sollen Folgendes enthalten:

- Name und Rolle des Antragstellers.
- Repository-Name und Klassifizierung.
- Beantragte Zugangsstufe (Lesen/Schreiben/Admin).
- Geschäftliche Begründung.
- Erwartete Dauer (bei zeitlich begrenztem Zugang).

**Genehmigungsanforderungen**:

| Zugangsstufe | Erforderliche Genehmiger |
|--------------|--------------------------|
| Lesezugang | Repository-Eigentümer |
| Schreibzugang | Repository-Eigentümer + Entwicklungs-Team-Lead |
| Admin-Zugang (jedes Repository) | Repository-Eigentümer + Entwicklungs-Team-Lead |
| Admin-Zugang (Produktions-Repository) | Repository-Eigentümer + ISB oder Stellvertreter |

Zugang soll innerhalb von 24 Stunden nach Genehmigung während der Geschäftszeiten bereitgestellt werden. Notfall-Zugriffsanfragen sollen einem beschleunigten Genehmigungsverfahren mit nachträglicher Überprüfung innerhalb von 48 Stunden folgen.

Alle Zugriffsanfragen und Genehmigungen sollen dokumentiert und mindestens 3 Jahre aufbewahrt werden.

---

## Zugriffsüberprüfung und Entzug

Repository-Zugang soll vierteljährlich überprüft werden, um die fortbestehende geschäftliche Begründung zu bestätigen.

**Vierteljährlicher Zugriffsüberprüfungsprozess**:

1. Repository-Eigentümer überprüft den Zugang jedes Nutzers und bestätigt: Zugang noch erforderlich (ja/nein), Zugangsstufe angemessen (ja/nein), Massnahme (behalten/ändern/entziehen).
2. Überprüfung dokumentiert mit Bestätigung des Repository-Eigentümers und Datum.
3. Keine Reaktion wird nach 10 Arbeitstagen an den Entwicklungsmanager und nach 15 Arbeitstagen an den ISB eskaliert.

**Dienstkonto-Überprüfung** (vierteljährlich):

- Ist die Automatisierung oder Pipeline noch aktiv? (Zur Entfernung markieren, wenn inaktiv >90 Tage.)
- Ist der dokumentierte Eigentümer noch verantwortlich?
- Ist die Zugangsstufe noch angemessen?
- Ist der Token-Ablauf angemessen gesetzt? (Maximum 1 Jahr; 90 Tage empfohlen für hochprivilegierte Konten.)

**Entzug des Zugangs**:

- Repository-Zugang soll am gleichen Geschäftstag entzogen werden, an dem die Beschäftigung endet, eine Rollenänderung den Zugangsbedarf entfällt oder der Vertrag ausläuft.
- Automatischer Zugangsentzug über das Identitätsmanagementsystem ist bevorzugt.
- Der Zugangsentzug soll innerhalb von 24 Stunden nach dem auslösenden Ereignis verifiziert werden.

---

## Branch-Schutz und Code-Review

Der Hauptbranch (main/master/trunk) von Produktions- und internen Tool-Repositories soll geschützt werden.

**Branch-Schutz-Anforderungen**:

| Anforderung | Produktion | Interne Tools |
|-------------|------------|---------------|
| Direkte Commits blockiert | Ja | Ja |
| Pull Request vor Merge erforderlich | Ja | Ja |
| Minimale Reviewer-Anzahl | 2 | 1 |
| Veraltete Genehmigungen bei neuen Commits verwerfen | Ja | Empfohlen |
| Statusprüfungen müssen bestehen (CI/CD-Tests, Linter, Sicherheits-Scans) | Ja | Ja |
| Signierte Commits | Empfohlen | Optional |

Release-Branches (release/*, hotfix/*) sollen den gleichen Schutz wie der Hauptbranch haben.

Nur Repository-Administratoren sollen Branch-Schutzregeln ändern dürfen. Eine vorübergehende Aufhebung des Branch-Schutzes erfordert dokumentierte Begründung, ISB-Genehmigung und automatische Wiederherstellung nach dem festgelegten Zeitraum.

**Pull-Request-Anforderungen**:

- Alle Code-Änderungen an geschützten Branches sollen über Pull Requests eingereicht werden.
- Pull Requests sollen nicht vom Code-Autor genehmigt werden (Funktionstrennung).
- Pull Requests sollen eine klare Beschreibung der Änderungen, einen Link zum zugehörigen Issue oder Ticket (wo zutreffend) und Nachweise über Tests enthalten.
- Sicherheitsrelevante Änderungen sollen eine Bewertung der Sicherheitsauswirkungen enthalten.

**Schnell-Review**: Risikoarme Änderungen (Dokumentationsaktualisierungen, Tippfehler-Korrekturen, reine Konfigurationsänderungen ohne Code-Logik) können eine 1-Stunden-Review-Periode für Produktions-Repositories verwenden, sofern sie als „risikoarm" oder „docs-only" gekennzeichnet sind, auf Dokumentations- oder Konfigurationsdateien beschränkt sind und von einem Code-Owner genehmigt werden. Standard-Review-Zeitraum für Produktionscode-Änderungen: 4 Stunden.

---

## Secret-Management

Quellcode-Repositories sollen keine Passwörter, API-Keys, Tokens, Private Keys, Datenbankverbindungsstrings mit eingebetteten Anmeldedaten, SSH-Private-Keys, Verschlüsselungskeys oder andere sensible Authentifizierungsmaterialien enthalten.

**Secret-Scanning**:

Alle Repositories sollen automatisches Secret-Scanning mit [Secret Scanning Tool] aktiviert haben (z. B. GitLeaks, TruffleHog, GitHub Secret Scanning oder gleichwertig).

| Scan-Typ | Umfang | Häufigkeit |
|----------|--------|------------|
| Pre-Commit-Scanning | Verhindert, dass Secrets in das Repository gelangen | Echtzeit (jeder Commit) |
| Serverseitiges Scanning | Erkennt bereits im Repository vorhandene Secrets | Täglicher Vollscan |

Produktions-Repositories sollen Pre-Commit-Secret-Scanning im Blocking-Modus aktiviert haben.

Secret-Scanning soll generische Secrets (regex-basierte Muster), anbieterspezifische Secrets (AWS-Keys, GitHub-Tokens, Azure-Anmeldedaten) und vom Sicherheitsteam definierte benutzerdefinierte Muster erkennen.

**Secret-Behebung**:

| Repository-Klassifizierung | Behebungs-SLA |
|---------------------------|---------------|
| Produktion | 1 Stunde (sofortige Rotation bei bestätigter Exposition) |
| Interne Tools | 24 Stunden |

Die Behebung soll umfassen: (1) sofortige Rotation des exponierten Secrets, (2) Entfernung aus der Repository-Historie falls committed, (3) Folgenabschätzung (wurde das Secret von nicht autorisierten Parteien abgerufen?), und (4) Incident-Meldung sofern erforderlich.

**Genehmigte Secret-Management-Methoden**:

| Umgebung | Genehmigte Methode |
|----------|-------------------|
| Entwicklung | Umgebungsvariablen; `.env`-Dateien über `.gitignore` aus der Versionskontrolle ausgeschlossen |
| CI/CD-Pipelines | Pipeline-Secrets-Store ([CI/CD Platform] Secrets oder gleichwertig); keine hartcodierten Secrets in Pipeline-Definitionen |
| Produktion | Dedizierter Secrets-Manager (z. B. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault oder gleichwertig) |

Entwickler sollen in Best Practices für Secret-Management geschult werden, einschliesslich der Verwendung von Umgebungsvariablen, Secrets-Management-Systemen und Pre-Commit-Hooks.

---

## Authentifizierung und Multi-Faktor-Authentifizierung

Der Zugang zu Quellcode-Repositories soll mit genehmigten Methoden authentifiziert werden: Benutzername/Passwort (mit MFA), SSH-Public-Key-Authentifizierung, Personal Access Tokens (mit Ablaufzeit), zertifikatsbasierte Authentifizierung oder Single Sign-On (SSO) über den organisationalen Identity Provider.

**MFA-Anforderungen**:

Multi-Faktor-Authentifizierung soll erforderlich sein für:

- Alle menschlichen Nutzerkonten mit Schreib- oder Admin-Zugang zu Produktions-Repositories.
- Alle menschlichen Nutzerkonten mit Admin-Zugang zu jedem Repository.
- Webbasierter Repository-Zugang für alle Nutzer.

Akzeptierte MFA-Methoden: Authenticator-Anwendungen (z. B. Google Authenticator, Microsoft Authenticator, Authy), Hardware-Sicherheitsschlüssel (z. B. YubiKey) oder Push-Benachrichtigung auf registriertes Gerät. SMS-basierte Codes sind die am wenigsten bevorzugte Methode und sollen nur verwendet werden, wenn andere Methoden nicht verfügbar sind.

**SSH-Keys und Personal Access Tokens**:

- Eindeutig pro Nutzer und Gerät.
- Mit Passphrase oder sicherer Speicherung geschützt.
- Jährlich oder sofort bei Verdacht auf Kompromittierung rotiert.
- Bei Geräteverlust oder -ausserdienststellung widerrufen.

**Dienstkonten**: Dienstkonten können keine interaktive MFA durchführen. Kompensierende Kontrollen sollen umfassen: Tokens mit minimalen erforderlichen Scopes ausgestellt, Token-Ablauf durchgesetzt (Maximum 1 Jahr; 90 Tage empfohlen für hochprivilegierte Konten), Aktivität protokolliert und auf Anomalien überwacht sowie vierteljährliche Überprüfung auf fortbestehenden Bedarf.

---

## Audit-Protokollierung und Monitoring

Repository-Plattformen sollen folgende Ereignisse protokollieren:

| Ereigniskategorie | Protokollierte Ereignisse |
|-------------------|--------------------------|
| **Zugang** | Anmeldeversuche, Abmeldeereignisse, Sitzungsdauer |
| **Repository-Zugang** | Klonen, Pullen, Browse-Operationen |
| **Code-Änderungen** | Commits (Autor, Zeitstempel, Nachricht, Dateien), Pushes, Force-Pushes |
| **Branch-Operationen** | Erstellung, Löschung, Schutzänderungen |
| **Pull Requests** | Erstellung, Review, Genehmigung, Merge, Ablehnung |
| **Berechtigungsänderungen** | Zugang gewährt, entzogen, Rollenänderungen |
| **Administrative Aktionen** | Repository-Einstellungsänderungen, Mitarbeiterverwaltung |
| **Sicherheitsereignisse** | Secret-Scanning-Warnungen, fehlgeschlagene Authentifizierung, verdächtige Zugriffsmuster |

Protokolle sollen enthalten: Zeitstempel (UTC), Nutzeridentität, Quell-IP-Adresse, durchgeführte Aktion, betroffenes Repository sowie Erfolgs- oder Fehlerstatus.

**Protokollaufbewahrung**:

| Ereignistyp | Mindestaufbewahrung |
|-------------|---------------------|
| Zugriffsereignisse | 1 Jahr |
| Code-Änderungsereignisse | 3 Jahre |
| Berechtigungsänderungen | 3 Jahre |
| Sicherheitsereignisse | 3 Jahre |
| Administrative Aktionen | 3 Jahre |

Protokolle sollen manipulationssicher und vor nicht autorisierter Änderung oder Löschung geschützt sein.

**Monitoring und Alarmierung**:

Repository-Zugriffsprotokolle sollen überwacht werden auf: mehrere fehlgeschlagene Authentifizierungsversuche, Zugang von ungewöhnlichen geografischen Standorten, Zugang ausserhalb normaler Geschäftszeiten, Massen-Download-Operationen, Versuche zur Berechtigungserhöhung, Force-Pushes auf geschützte Branches und Secret-Scanning-Warnungen.

Sicherheitswarnungen sollen erzeugt und innerhalb von 15 Minuten nach Erkennung an das Security-Operations-Team übermittelt werden. Kritische Ereignisse (bestätigter nicht autorisierter Zugang, massenhafte Berechtigungsänderungen) sollen eine sofortige Incident-Response gemäss dem Incident-Management-Prozess der Organisation auslösen. Bestätigte Sicherheitsvorfälle mit Quellcode-Beteiligung (nicht autorisierter Zugang, Code-Manipulation, Diebstahl geistigen Eigentums) sollen innerhalb von 1 Stunde nach Bestätigung an den ISB eskaliert werden. Wenn der Vorfall Kundendaten oder Produktionssysteme betrifft, soll der Incident-Management-Prozess (A.5.24-28) sofort aktiviert werden.

---

## Backup und Wiederherstellung

Alle Quellcode-Repositories sollen gesichert werden, um die Wiederherstellung nach Datenverlust, Beschädigung oder Plattformausfall zu ermöglichen.

**Backup-Anforderungen**:

| Anforderung | Standard |
|-------------|----------|
| Häufigkeit | Täglich inkrementell; wöchentlich vollständig |
| Aufbewahrung | 90 Tage (aktive Repositories); 7 Jahre (Produktions-Repositories) |
| Geografische Redundanz | Backups an einem anderen geografischen Standort als das primäre Repository gespeichert |
| Verschlüsselung | Im Ruhezustand mit organisationsgenehmigter Verschlüsselung verschlüsselt |
| Zugangskontrolle | Auf autorisierte Backup-Administratoren beschränkt; MFA erforderlich |

Backups sollen umfassen: Quellcode (alle Branches, Commits, vollständige Historie), Repository-Metadaten (Berechtigungen, Einstellungen, Konfigurationen), Pull-Request-Historie und Issue-Tracking-Daten soweit integriert.

**Wiederherstellungstests**:

| Repository-Klassifizierung | Testhäufigkeit | Recovery Time Objective (RTO) |
|---------------------------|----------------|-------------------------------|
| Produktion | Vierteljährlich | 4 Stunden |
| Interne Tools | Jährlich | 24 Stunden |

Wiederherstellungstests sollen verifizieren: Repository-Wiederherstellung innerhalb des RTO, Datenintegrität (alle Commits, Branches, Historie intakt), Berechtigungswiederherstellung und Funktionsfähigkeit des wiederhergestellten Repositories. Tests sollen eine repräsentative Auswahl von Repositories verwenden (mindestens 3 Produktions-Repositories pro Quartal, rotierend um alle jährlich abzudecken). Ergebnisse sollen dokumentiert werden.

---

## Drittanbieter-Zugangsverwaltung

Drittentwickler, Auftragnehmer und Offshore-Entwicklungsteams sollen folgende Anforderungen erfüllen, bevor sie Repository-Zugang erhalten:

- Unterzeichnetes Geheimhaltungsabkommen (NDA), verifiziert durch Beschaffung oder Rechtsabteilung.
- Zugang auf spezifische Repositories beschränkt, die für die vertraglich vereinbarte Arbeit erforderlich sind.
- Zeitlich begrenzter Zugang, an die Vertragsdauer gebunden mit automatischem Ablauf.
- Zugang genehmigt vom Repository-Eigentümer (obligatorisch) und ISB oder Stellvertreter (für Produktions-Repositories).

**Drittanbieter-Monitoring**:

- Drittanbieter-Zugang monatlich auf fortbestehenden Bedarf überprüft.
- Alle Code-Beiträge von Drittanbietern sollen eine Überprüfung durch einen internen Entwickler erfordern (mindestens ein Reviewer) sowie eine Sicherheitsüberprüfung bei sicherheitsrelevanten Änderungen.
- Drittanbieter-Zugang soll sofort entzogen werden bei Vertragsablauf, Vertragskündigung, Sicherheitsvorfall mit Beteiligung des Drittanbieters oder auf Anfrage des Repository-Eigentümers.

Drittanbieter-Zugang soll in einem Drittanbieter-Zugriffsregister dokumentiert werden mit: Vertragsunternehmen, Einzelpersonen, zugegriffenen Repositories, Vertragsdaten und Verantwortlichkeit des Projektmanagers.

---

## Ausnahmeverwaltung

Ausnahmen von dieser Richtlinie sollen schriftlich beantragt werden und Folgendes enthalten:

- Spezifische Anforderung(en), die eine Ausnahme erfordern.
- Geschäftliche Begründung.
- Kompensierende Kontrollen.
- Beantragte Ausnahmedauer (Maximum 12 Monate).
- Risikobewertung und -akzeptanz.

Ausnahmen sollen vom Repository-Eigentümer und Information Security Manager (obligatorisch) genehmigt werden, sowie vom ISB für Produktions-Repository-Ausnahmen. Alle aktiven Ausnahmen sollen vierteljährlich überprüft werden.

Wo es technisch nicht machbar ist, eine Anforderung zu erfüllen, sollen kompensierende Kontrollen implementiert werden, um eine gleichwertige Risikominderung zu erzielen, dokumentiert, vom Information Security Manager verifiziert und jährlich überprüft werden.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Branch-Schutz** | Konfigurationsregeln, die direkte Commits an bestimmte Branches verhindern und Pull Requests, Reviews und bestandene Statusprüfungen erfordern |
| **Code-Owner** | Einzelperson oder Team, die/das für die Überprüfung von Änderungen an bestimmten Teilen der Codebasis verantwortlich ist |
| **Force-Push** | Eine Git-Operation, die die Remote-Branch-Historie überschreibt; auf geschützten Branches eingeschränkt |
| **MFA** | Multi-Faktor-Authentifizierung — Erfordernis von zwei oder mehr Verifizierungsfaktoren für den Zugang |
| **Pre-Commit-Hook** | Ein Skript, das vor der Erstellung eines Commits ausgeführt wird, um zu verhindern, dass Secrets oder Richtlinienverletzungen in das Repository gelangen |
| **Pull Request (Merge Request)** | Eine Anfrage, Code-Änderungen von einem Branch in einen anderen zu mergen, die eine Überprüfung vor der Integration ermöglicht |
| **RBAC** | Rollenbasierte Zugriffskontrolle — Zuweisung von Berechtigungen auf Basis definierter organisationaler Rollen |
| **Repository** | Ein Speicherort für Quellcode, verwaltet durch ein Versionskontrollsystem (z. B. Git) |
| **Secret** | Jede Anmeldeinformation, jeder API-Key, Token, Private Key oder jedes Authentifizierungsmaterial, das nicht im Quellcode gespeichert werden darf |
| **Dienstkonto** | Ein nicht menschliches Konto für Automatisierung, CI/CD und System-zu-System-Integration |
| **SSO** | Single Sign-On — Authentifizierung, die Nutzern ermöglicht, mit einem Satz von Anmeldedaten auf mehrere Systeme zuzugreifen |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung von Admin-Zugang zu Produktions-Repositories; Ausnahmegenehmigung; Überwachung von Sicherheitsvorfällen mit Quellcode; jährliche Richtlinienüberprüfung; Berichterstattung an die Geschäftsleitung |
| **TL / Entwicklungsmanager** | Auswahl und Konfiguration der Entwicklungsplattform; Genehmigung der Repository-Klassifizierung; Compliance des Entwicklungsteams; Ressourcenzuweisung für die Richtlinienumsetzung |
| **Information Security Manager** | Richtlinienpflege; Ausnahmenüberprüfung (Nicht-Produktions-Repositories); Sicherheitsmonitoring und Vorfalluntersuchung; Audit-Koordination; vierteljährliche Compliance-Berichterstattung an ISB |
| **Repository-Eigentümer** | Zuweisung der Repository-Klassifizierung; Genehmigung von Zugriffsanfragen; vierteljährliche Zugriffsüberprüfungen; Repository-Sicherheitskonfiguration; Vorfallmeldung an das Sicherheitsteam |
| **Entwicklungs-Team-Leads** | Überprüfung von Zugriffsanfragen für Teammitglieder; Durchsetzung des Code-Review-Prozesses; Schulung der Entwickler in sicheren Repository-Praktiken; Durchsetzung des Secret-Managements im Team |
| **Sicherheitsteam** | Konfiguration von Sicherheitsmonitoring und -alarmierung; Verwaltung von Secret-Scanning-Tools; Sicherheitsaudits und -bewertungen; Incident-Response für Quellcode-Sicherheitsereignisse |
| **IT-Betrieb** | Repository-Plattformwartung und -verfügbarkeit; Backup- und Wiederherstellungsimplementierung; Automatisierung der Zugangsvergabe und des Zugangsentzugs; Protokollsammlung und -aufbewahrung |
| **Einzelne Entwickler und Auftragnehmer** | Einhaltung der Zugangskontroll- und Authentifizierungsanforderungen; Schutz von Anmeldedaten; kein Speichern von Secrets in Repositories; Teilnahme an Code-Reviews; Vorfallmeldung; Abschluss der erforderlichen Sicherheitsschulungen |

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit | Aufbewahrung |
|---|---------|-----------|------------|--------------|
| 1 | **Repository-Inventar** mit Klassifizierung, Eigentümer und Plattform-Metadaten | TL / Entwicklungsmanager | Kontinuierlich gepflegt; jährlich überprüft | Lebensdauer des Repositories + 3 Jahre |
| 2 | **Zugriffsanforderungs- und Genehmigungsaufzeichnungen** (Anfragen, Begründungen, Genehmigungen) | Repository-Eigentümer | Pro Anfrage | 3 Jahre |
| 3 | **Vierteljährliche Zugriffsüberprüfungsaufzeichnungen** (nutzerweise Bestätigung, ergriffene Massnahmen) | Repository-Eigentümer | Vierteljährlich | 3 Jahre |
| 4 | **Dienstkonto-Inventar** mit Eigentümer, Zweck und vierteljährlichen Überprüfungsaufzeichnungen | IT-Betrieb / Entwicklungsmanager | Kontinuierlich gepflegt; vierteljährlich überprüft | Lebensdauer des Kontos + 1 Jahr |
| 5 | **Branch-Schutz-Konfigurationsexporte** von der Repository-Plattform | Entwicklungsmanager / DevOps | Vierteljährlich | 2 Jahre |
| 6 | **Pull-Request- und Code-Review-Aufzeichnungen** (Review-Kommentare, Genehmigungen, Merge-Historie) | Entwicklungsmanager | Pro Code-Änderung | 3 Jahre |
| 7 | **Secret-Scanning-Konfiguration und Befundprotokoll** (Tool-Einstellungen, Warnungen, Behebungsaufzeichnungen) | Sicherheitsteam / DevOps | Kontinuierlich; Befunde wöchentlich überprüft | 3 Jahre |
| 8 | **MFA-Registrierungsberichte** mit Abdeckung für alle Repository-Nutzer | IT-Betrieb / Sicherheitsteam | Vierteljährlich | 1 Jahr |
| 9 | **Authentifizierungs- und Zugriffsprotokolle** von der Repository-Plattform | IT-Betrieb | Kontinuierlich | Gemäss Aufbewahrungstabelle (1–3 Jahre je Ereignistyp) |
| 10 | **Backup-Ausführungs- und Wiederherstellungstestaufzeichnungen** (Backup-Protokolle, Testberichte, RTO-Messungen) | IT-Betrieb | Backup: täglich; Wiederherstellungstests: vierteljährlich (Produktion) / jährlich (andere) | 3 Jahre |
| 11 | **Drittanbieter-Zugriffsregister** (Auftragnehmerdetails, NDA-Aufzeichnungen, Vertragsdaten, Zugangsablauf) | Repository-Eigentümer / Beschaffung | Kontinuierlich gepflegt; monatlich überprüft | Vertragsdauer + 3 Jahre |
| 12 | **Ausnahmeregister** (Anfragen, Genehmigungen, kompensierende Kontrollen, vierteljährliche Überprüfungen) | Information Security Manager | Kontinuierlich gepflegt; vierteljährlich überprüft | Ausnahmedauer + 3 Jahre |
| 13 | **Entwickler-Sicherheitsschulungsaufzeichnungen** (Secret-Management, Repository-Sicherheitspraktiken) | ISB / HR | Jährlich | Beschäftigungsdauer + 3 Jahre |
| 14 | **Aufzeichnungen zur Verifizierung des Zugangsentzugs** (durch Kündigung ausgelöste Widerrufbestätigungen) | IT-Betrieb / HR | Pro Kündigungsereignis | 3 Jahre |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Managementteam verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich unter anderem Repository-Plattform-Zugriffsberichte, Audits der Branch-Schutz-Konfiguration, Secret-Scanning-Tool-Berichte, Aufzeichnungen zur Zugriffsüberprüfungsabschlüsse, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Konformitätskennzahlen**:

| Kennzahl | Ziel | Messhäufigkeit |
|----------|------|----------------|
| Repositories mit konformem RBAC und abgeschlossenen vierteljährlichen Überprüfungen | >= 90% | Vierteljährlich |
| Repositories mit erforderlichem Branch-Schutz aktiviert | >= 95% | Vierteljährlich |
| Repositories mit Secret-Scanning aktiviert und Secrets innerhalb SLA behoben | >= 90% | Monatlich |
| Drittanbieter-Konten mit gültigem NDA und aktuellem Vertrag | 100% | Monatlich |
| MFA-Registrierung für Nutzer mit Schreib- oder Admin-Zugang | 100% | Vierteljährlich |
| Zugang am gleichen Geschäftstag der Kündigung entzogen | 100% | Pro Ereignis |

**Konformitätsbewertung**:

| Komponente | Gewichtung | Berechnung |
|------------|-----------|------------|
| Repository-Zugangs-Compliance | 35% | (Repositories mit konformem RBAC + abgeschlossenen vierteljährlichen Überprüfungen) / Gesamte Repositories x 100 |
| Branch-Schutz-Compliance | 35% | (Repositories mit erforderlichem Branch-Schutz aktiviert) / Anwendbare Repositories x 100 |
| Secret-Management-Compliance | 20% | (Repositories mit Scanning aktiviert + Secrets innerhalb SLA behoben) / Gesamt x 100 |
| Drittanbieter-Zugangs-Compliance | 10% | (Drittanbieter-Konten mit gültigem NDA + aktuellem Vertrag) / Gesamte Drittanbieter-Konten x 100 |

**Handhabung von Nichtkonformität**: Unter 70% erfordert sofortige ISB-Eskalation und Sanierungsplan. 70–89% erfordert Information-Security-Manager-Aufsicht mit monatlichen Überprüfungen. 90% und darüber folgt dem standardmässigen vierteljährlichen Monitoring.

**Sanierungsverantwortung nach Score-Komponente**:

| Komponente | Unter Ziel | Sanierungsverantwortlicher | Eskalation |
|------------|-----------|---------------------------|------------|
| Repository-Zugangs-Compliance | <90% | Repository-Eigentümer + Entwicklungsmanager | ISB nach 30 Tagen überfällig |
| Branch-Schutz-Compliance | <95% | DevOps / Entwicklungsmanager | ISB nach 15 Tagen überfällig |
| Secret-Management-Compliance | <90% | Sicherheitsteam + DevOps | ISB sofort bei aktiv exponierten Secrets |
| Drittanbieter-Zugangs-Compliance | <100% | Beschaffung + Repository-Eigentümer | ISB nach 5 Tagen überfällig (rechtliches/vertragliches Risiko) |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Information Security Manager genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen und einem definierten Überprüfungsdatum (Maximum 12 Monate). Ausnahmen sollen dem Management-Review-Team gemeldet werden.

## Nichtkonformität

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterzogen werden, bis hin zur Beendigung des Arbeitsverhältnisses. Richtlinienverstösse sollen dokumentiert, vom Information Security Manager untersucht und dem ISB gemeldet werden.

## SOC-2-Implementierungsphasen

Für Organisationen, die eine SOC-2-Typ-II-Zertifizierung anstreben, wird die folgende stufenweise Implementierung empfohlen:

| Phase | Fokus | Hauptmassnahmen |
|-------|-------|-----------------|
| 1 | **Asset-Inventar** | Vollständiges Repository-Inventar mit Klassifizierung und Eigentümer |
| 2 | **RBAC-Implementierung** | Rollenbasierte Zugriffskontrolle mit minimaler Rechtevergabe |
| 3 | **MFA-Durchsetzung** | MFA für alle Schreib-/Admin-Zugänge |
| 4 | **Branch-Schutz** | Geschützte Branches mit erforderlichen Reviews |
| 5 | **Secret-Scanning** | Automatisches Pre-Commit- und serverseitiges Scanning |
| 6 | **Protokollierung und Monitoring** | Umfassende Audit-Protokollierung an SIEM weitergeleitet |
| 7 | **Zugriffsüberprüfungen** | Vierteljährliche Überprüfungen mit dokumentierten Nachweisen |
| 8 | **Backup und Wiederherstellung** | Backup-Strategie mit getesteter Wiederherstellung |
| 9 | **Drittanbieter-Kontrollen** | NDA, zeitlich begrenzter Zugang, erweiterte Überprüfung |
| 10 | **Kontinuierliche Verbesserung** | Kennzahlen, Konformitätsbewertung, vierteljährliche Berichterstattung |

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen an Repository-Plattformfähigkeiten, neu entstehende Bedrohungen für die Quellcode-Sicherheit (Supply-Chain-Angriffe, Dependency Confusion, CI/CD-Pipeline-Kompromittierung), regulatorische Änderungen, Audit-Befunde und Erkenntnisse aus Sicherheitsvorfällen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Quellcode-Zugriffsrichtlinie — ISO-27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | **8.4 Zugang zum Quellcode** |
| | 8.5 Sichere Authentifizierung |
| | 8.25 Sicherer Entwicklungslebenszyklus |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen zum Datenschutz; Quellcode-Zugangskontrolle als technische Massnahme |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Zugangskontrolle als angemessene technische Massnahme) |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.4 — Zugang zum Quellcode |
| ISO/IEC 27002:2022 | Abschnitt 8.4 — Implementierungsleitfaden für die Zugangskontrolle zum Quellcode |
| NIST SP 800-218 (SSDF) | PS.1 — Protect all forms of code from unauthorised access and tampering |
| NIST SP 800-53 Rev 5 | AC-3 (Access Enforcement), AC-6 (Least Privilege), CM-5 (Access Restrictions for Change), AU-2 (Audit Events) |
| CIS Controls v8 | 6.1–6.2 (Access Granting/Revoking), 6.7 (Centralised Access Control), 6.8 (Role-Based Access), 16.1–16.4 (Application Software Security) |
| FINMA (soweit anwendbar) | Rundschreiben 2023/1 Rz. 50–62 — Informationssicherheit umfasst Quellcode-Schutz |
| DORA (soweit anwendbar) | Art. 9 — IKT-Asset-Management umfasst Quellcode; Art. 15 — Vorfallmeldung umfasst Quellcode-Kompromittierung |
| NIS2 (soweit anwendbar) | Art. 21(2) — Asset-Management umfasst Quellcode; Art. 23 — Vorfallmeldung bei Quellcode-Sicherheitsvorfällen |

---

<!-- QA_VERIFIED: 2026-03-29 -->
