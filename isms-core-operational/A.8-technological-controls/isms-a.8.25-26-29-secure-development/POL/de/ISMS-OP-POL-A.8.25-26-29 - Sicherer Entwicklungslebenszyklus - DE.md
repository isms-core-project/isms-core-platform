<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.25-26-29-DE:operational:OP-POL:a.8.25-26-29 -->
**ISMS-OP-POL-A.8.25-26-29 — Sicherer Entwicklungslebenszyklus**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Sicherer Entwicklungslebenszyklus |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.25-26-29 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Initiale operative Richtlinie für ISO 27001:2022 |

**Prüfzyklus**: Jährlich
**Nächstes Prüfdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.8.25 — Sicherer Entwicklungslebenszyklus
- ISO/IEC 27001:2022 Massnahme A.8.26 — Sicherheitsanforderungen an Anwendungen
- ISO/IEC 27001:2022 Massnahme A.8.29 — Sicherheitstests in Entwicklung und Abnahme
- OWASP Application Security Verification Standard (ASVS) 4.0
- OWASP Top 10:2025
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zum sicheren Entwicklungslebenszyklus |
|-----------|---------------------------------------------|
| A.5.8 Informationssicherheit im Projektmanagement | Sicherheitsanforderungen in den Projektlebenszyklus integriert |
| A.5.15–16–18 Identitäts- und Zugriffsmanagement | Zugriffssteuerung für Repositories, Umgebungen und Deployment-Tools |
| A.8.4 Zugriff auf Quellcode | Einschränkung und Schutz des Zugriffs auf Quellcode |
| A.8.8 Management technischer Schwachstellen | Behebung von Schwachstellen in eingesetzten Anwendungen |
| A.8.28 Sicheres Coding | Standards und Praktiken für sicheres Coding |
| A.8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen | Anforderungen an die Umgebungssegregation |
| A.8.32 Änderungsmanagement | Änderungssteuerung für Code-Promotion und Deployment |
| A.8.33 Testinformationen | Schutz von Testdaten |

**Verwandte interne Richtlinien**:

- Richtlinie zur Zugriffskontrolle
- Richtlinie zum Schwachstellenmanagement
- Richtlinie zum Änderungsmanagement
- Richtlinie zur Informationsklassifizierung und -handhabung
- Endgerätesicherheitsrichtlinie

---

# Richtlinie zum sicheren Entwicklungslebenszyklus

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass Informationssicherheit im Entwicklungslebenszyklus von Software und Systemen konzipiert und implementiert wird, dass Sicherheitsanforderungen bei der Entwicklung oder dem Erwerb von Anwendungen identifiziert und spezifiziert werden und dass Sicherheitstests vor der Inbetriebnahme definiert und durchgeführt werden.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG), indem technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz von Personendaten implementiert werden, gemäss Art. 7 (Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen) und Art. 8 (technische und organisatorische Sicherheitsmassnahmen). Sofern die Organisation Daten von Personen im EU/EWR-Raum bearbeitet, gelten auch die DSGVO-Anforderungen (Art. 25 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 32 — Sicherheit der Verarbeitung).

## Geltungsbereich

Systementwicklung massgeschneiderter Softwarelösungen der Organisation, einschliesslich Webanwendungen, APIs, mobiler Anwendungen und Infrastructure-as-Code.

Alle intern entwickelten und ausgelagerten Entwicklungsaktivitäten, die gemäss der ISO-27001-Scope-Erklärung im Geltungsbereich sind.

Alle Mitarbeitenden und Drittnutzer, die an Softwareentwicklung, Tests und Deployment beteiligt sind.

## Grundsatz

Sichere Software- und Systemtechnikprinzipien und -standards werden im gesamten Softwareentwicklungslebenszyklus implementiert und getestet.

Informationssicherheit und Datenschutz sind durch Technik und Voreinstellung verankert, gemäss den NIST SP 800-218 (SSDF) Praxisgruppen: Prepare the Organisation (PO), Protect the Software (PS), Produce Well-Secured Software (PW) und Respond to Vulnerabilities (RV).

Sicherheitsmassnahmen werden proportional zum Anwendungsrisiko angewendet, wobei Anwendungen mit höherem Risiko strengeren Anforderungen unterliegen.

---

## Sicherheits-Toolchain für die Entwicklung

Die Organisation soll eine genehmigte Sicherheits-Toolchain pflegen, die in den Entwicklungslebenszyklus integriert ist.

**Genehmigte Sicherheits-Toolchain**:

| Kategorie | Zweck | Verantwortlicher | Integrationspunkt |
|-----------|-------|-----------------|------------------|
| **Quellcode-Repository** | Versionskontrolle, Branch-Schutz, Zugriffssteuerung | DevOps / Plattformteam | Entwicklungsphase |
| **SAST** (Static Application Security Testing) | Erkennung von Schwachstellen im Quellcode (z. B. SonarQube, Semgrep, Checkmarx oder gleichwertig) | DevOps / Entwicklungsleiter | CI/CD-Pipeline — Build-Phase |
| **SCA** (Software Composition Analysis) | Erkennung von Schwachstellen in Open-Source-Abhängigkeiten (z. B. Snyk, OWASP Dependency-Check oder gleichwertig) | DevOps / Entwicklungsleiter | CI/CD-Pipeline — Build-Phase |
| **DAST** (Dynamic Application Security Testing) | Erkennung von Laufzeitschwachstellen (z. B. OWASP ZAP, Burp Suite oder gleichwertig) | QA / Sicherheitsteam | Vor-Deployment-Phase |
| **Secret Scanning** | Erkennung von Anmeldedaten, API-Schlüsseln und Tokens im Code (z. B. GitLeaks, TruffleHog oder gleichwertig) | DevOps / Plattformteam | Pre-Commit-Hook + CI/CD-Pipeline |
| **Abhängigkeitsdatenbank** | Schwachstellenintelligenz für Drittkomponenten (z. B. NVD, OSV, GitHub Advisory Database) | Entwicklungsleiter | Kontinuierliche Überwachung |
| **SBOM-Generator** | Erstellung einer Software Bill of Materials (z. B. Syft, CycloneDX CLI oder gleichwertig) | DevOps / Plattformteam | CI/CD-Pipeline — Build-Phase |
| **Code-Review-Plattform** | Peer-Review, Genehmigungsworkflow, Audit-Trail (z. B. GitHub, GitLab, Bitbucket oder gleichwertig) | Entwicklungsleiter | Vor-Merge-Phase |
| **Penetrationstest** | Manuelle Sicherheitsbeurteilung durch qualifizierte externe Spezialisten | ISB | Vor Release (Hochrisiko) / regelmässig |

Die Toolchain soll jährlich vom Entwicklungsleiter und ISB überprüft werden. Tooländerungen sollen dem Änderungsmanagementprozess folgen. Alle Tools sollen auf aktuellen, unterstützten Versionen gepflegt werden.

---

## Umgebungssegregation

Entwicklungs-, Test- und Produktionsumgebungen sollen getrennt werden und dürfen keine gemeinsamen Komponenten, Datenbanken oder Speicher teilen.

Entwicklungs-, Test- und Produktionsumgebungen sollen in separaten Netzwerken oder Netzwerksegmenten betrieben werden.

Es soll eine Trennung der administrativen Aufgaben zwischen Entwicklungs-/Testumgebungen und Produktionsumgebungen bestehen. Personal mit Schreibzugriff auf Entwicklungs-Repositories soll ohne separate Autorisierung keinen direkten administrativen Zugriff auf Produktionssysteme haben.

Daten sollen ohne explizite Genehmigung und angemessene Bereinigung nicht von der Produktions- in Entwicklungs- oder Testumgebungen fliessen (siehe Abschnitt Testdatenschutz).

Die Konfiguration der Umgebungssegregation soll dokumentiert werden, und die Einhaltung soll mindestens jährlich überprüft werden.

---

## Anwendungsrisikoklassifizierung

Alle Anwendungen sollen nach Risikoniveau klassifiziert werden, um die geeigneten Sicherheitsanforderungen zu bestimmen.

**Risikoklassifizierungskriterien**:

| Risikoniveau | Kriterien |
|--------------|-----------|
| **Hochrisiko** | Erfüllt EINES DER FOLGENDEN: verarbeitet vertrauliche oder eingeschränkte Daten; verarbeitet Personendaten gemäss nDSG/DSGVO; internetfähig oder für externe Parteien zugänglich; kritische Geschäftsfunktion oder Verarbeitung von Finanztransaktionen; Zahlungskarteninformationen (sofern PCI-Geltungsbereich besteht) |
| **Mittleres Risiko** | Erfüllt EINES DER FOLGENDEN: verarbeitet interne Daten; begrenzte Personendatenexposition (nur Namen, E-Mail-Adressen); nur intern zugänglich; wichtige, aber nicht kritische Geschäftsfunktion |
| **Niedrigrisiko** | Erfüllt ALLE: verarbeitet nur öffentliche Daten; keine Personendaten, keine sensiblen Geschäftsdaten; nicht kritische Geschäftsfunktion |

Anwendungsrisikoklassifizierungen sollen jährlich vom Entwicklungsleiter und ISB überprüft werden.

**Auslöser für Neuklassifizierung** (zusätzlich zur jährlichen Überprüfung):

| Auslöseereignis | Massnahme |
|-----------------|-----------|
| Neuer verarbeiteter Datentyp (z. B. Personendaten, Finanzdaten, Gesundheitsdaten) | Neuklassifizierung innerhalb von 14 Tagen |
| Änderung der Netzwerkexposition (intern → internetfähig) | Neuklassifizierung vor Deployment |
| Wesentliche Architekturänderung (neue API, neue Integration) | Neuklassifizierung in der Designphase |
| Regulatorische Änderung, die die Anwendung betrifft | Neuklassifizierung innerhalb von 30 Tagen |
| Sicherheitsincident mit Beteiligung der Anwendung | Neuklassifizierung innerhalb von 14 Tagen nach Incident-Abschluss |
| Übernahme oder Fusion, die den Anwendungsumfang betrifft | Neuklassifizierung innerhalb von 60 Tagen |

**Neuklassifizierungsprozess**: (1) Anwendungseigentümer stellt Änderungsantrag mit Begründung → (2) Entwicklungsleiter bewertet anhand der Klassifizierungskriterien → (3) ISB genehmigt bei Erhöhung der Klassifizierung → (4) Aktualisierte Sicherheitsanforderungen innerhalb von 60 Tagen angewendet, wenn Klassifizierung steigt → (5) Aktualisierte Klassifizierung im Register erfasst.

Die Klassifizierung soll im Anwendungsrisikoklassifizierungsregister erfasst werden.

---

## Sicherheitsanforderungen

Sicherheitsanforderungen sollen für alle Anwendungen auf der Grundlage der Risikoklassifizierung spezifiziert werden.

**Pflichtanforderungen nach Risikoniveau**:

| Anforderung | Hochrisiko | Mittleres Risiko | Niedrigrisiko |
|-------------|-----------|-----------------|--------------|
| Spezifikation der Sicherheitsanforderungen | Pflicht | Pflicht | Grundlegende Checkliste |
| Bedrohungsmodellierung (z. B. STRIDE, PASTA oder Attack Trees) | Pflicht | Empfohlen | Optional |
| Sicherheitsarchitekturprüfung | Pflicht | Empfohlen | Optional |
| Rückverfolgbarkeit der Anforderungen | Pflicht | Empfohlen | Optional |

**Prozess zur Bedrohungsmodellierung**:

Wo eine Bedrohungsmodellierung erforderlich ist (Pflicht für Hochrisiko, empfohlen für mittleres Risiko), soll folgender Prozess angewendet werden:

| Schritt | Aktivität | Ergebnis |
|---------|-----------|---------|
| 1. **Vorbereitung** | Team zusammenstellen (Entwickler, Architekt, Security Champion/ISB); Systemdokumentation, Datenflussdagramme, Architekturdiagramme zusammenstellen | Scope-Definition und Materialienpaket |
| 2. **Bedrohungsidentifikation** | STRIDE-Methodik anwenden (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) auf jede Komponente und jeden Datenfluss | Bedrohungskatalog |
| 3. **Risikobewertung** | Wahrscheinlichkeit und Auswirkung jeder identifizierten Bedrohung anhand der Risikokriterien der Organisation bewerten | Priorisierte Bedrohungsliste |
| 4. **Massnahmenplanung** | Sicherheitsmassnahmen und -anforderungen zur Behandlung jeder Bedrohung definieren; Implementierungsaufgaben zuordnen | Massnahmenplan mit Verantwortlichen und Fristen |
| 5. **Dokumentation** | Bedrohungsmodell im genehmigten Format erfassen; mit Sicherheitsanforderungsspezifikation verknüpfen | Abgeschlossenes Bedrohungsmodelldokument |

Bedrohungsmodelle sollen überprüft und aktualisiert werden: bei jedem Major Release; bei wesentlichen Änderungen der Anwendungsarchitektur; wenn neue relevante Bedrohungsintelligenz identifiziert wird; und mindestens jährlich für Hochrisikoanwendungen.

**Sicherheitsanforderungen sollen mindestens folgende Bereiche abdecken**:

- **Authentifizierung und Autorisierung** — Identitätsverifizierung, rollenbasierter Zugriff, Session-Verwaltung.
- **Eingabevalidierung und Ausgabekodierung** — Abwehr von Injection-Angriffen (OWASP Top 10 A05:2025).
- **Kryptographie** — Verschlüsselung von Daten bei der Übertragung (mindestens TLS 1.2) und im Ruhezustand gemäss der Richtlinie zum Einsatz von Kryptographie.
- **Session-Management** — sichere Session-Tokens, Timeouts, Invalidierung bei Abmeldung.
- **Fehlerbehandlung und Protokollierung** — keine sensiblen Daten in Fehlermeldungen; Sicherheitsereignisse gemäss der Protokollierungsrichtlinie protokollieren.
- **API-Sicherheit** — Authentifizierung, Rate Limiting, Eingabevalidierung für alle API-Endpunkte.
- **Datenschutz** — Handhabung von Personendaten gemäss nDSG Art. 7 (Datenschutz durch Technik und Voreinstellung); Datensparsamkeit; sichere Löschung.

Für Anwendungen, die Transaktionsdienste zwischen der Organisation und externen Parteien erbringen, sollen zusätzliche Anforderungen Identitäts-Vertrauensstufen, Integrität ausgetauschter Informationen, Nicht-Abstreitbarkeit und Vertraulichkeit von Transaktionen adressieren.

**Vorlage für Sicherheitsanforderungen**:

Sicherheitsanforderungsspezifikationen sollen einer standardisierten Vorlage folgen, die folgende Abschnitte umfasst:

| # | Abschnitt | Beschreibung |
|---|-----------|-------------|
| 1 | Anwendungsübersicht | Name, Zweck, Risikoklassifizierung, Datenklassifizierung |
| 2 | Datenflussdagramm | Systemkontextdiagramm mit Datenflüssen, Vertrauensgrenzen, externen Schnittstellen |
| 3 | Authentifizierungsanforderungen | Authentifizierungsmethoden, MFA-Anforderungen, Session-Management |
| 4 | Autorisierungsanforderungen | Zugriffskontrollmodell (RBAC/ABAC), Privilegstufen, Funktionstrennung |
| 5 | Eingabevalidierung | Validierungsregeln nach Eingabetyp, Kodierungsanforderungen, Dateiupload-Einschränkungen |
| 6 | Kryptographieanforderungen | Verschlüsselungsstandards (gemäss Richtlinie zum Einsatz von Kryptographie), Schlüsselmanagement |
| 7 | API-Sicherheit | Authentifizierung, Rate Limiting, Eingabevalidierung, Versionierung, Fehlerbehandlung |
| 8 | Datenschutz | Handhabung von Personendaten, Datensparsamkeit, Aufbewahrung, Löschung, nDSG-Art.-7-Konformität |
| 9 | Protokollierung und Überwachung | Zu protokollierende Sicherheitsereignisse, Protokollformat, Aufbewahrung, Alarmschwellen |
| 10 | Fehlerbehandlung | Inhaltsbeschränkungen für Fehlermeldungen, Fallback-Verhalten, graceful degradation |
| 11 | Drittanbieterintegration | Vertrauensbewertung, Datenaustausch, API-Sicherheit, SLA-Anforderungen |
| 12 | Konformitätsanforderungen | Regulatorische Anforderungen (nDSG, DSGVO sofern anwendbar), Branchenstandards |
| 13 | Zusammenfassung des Bedrohungsmodells | Identifizierte Hauptbedrohungen, erforderliche Massnahmen (für Hochrisikoanwendungen) |
| 14 | Sicherheitstestplan | Erforderliche Testarten, Umfang, Zeitplan, Akzeptanzkriterien |

Sicherheitsanforderungen sollen vom ISB (Hochrisiko) oder Entwicklungsleiter (mittleres/niedriges Risiko) genehmigt werden, bevor die Entwicklung beginnt.

---

## Richtlinien für sicheres Coding

Software soll auf der Grundlage branchenweit anerkannter Richtlinien für sicheres Coding konzipiert und entwickelt werden, darunter:

- **OWASP** — OWASP Top 10:2025, OWASP Application Security Verification Standard (ASVS) und OWASP Secure Coding Practices.
- **NIST SP 800-218 (SSDF)** — Secure Software Development Framework zur Minderung des Risikos von Softwareschwachstellen.
- **CWE/SANS Top 25** — Gefährlichste Softwareschwachstellen, die Kategorien wie Injection, Speicherbeschädigung und Authentifizierungsfehler abdecken.

Sprachspezifische Standards für sicheres Coding sollen für jede aktiv genutzte Programmiersprache dokumentiert und gepflegt werden. Diese sollen mindestens abdecken:

- Verbotene Funktionen und unsichere Muster.
- Erforderliche Eingabevalidierungs- und Ausgabekodierungstechniken.
- Genehmigte kryptographische Bibliotheken und Verwendungsmuster.
- Sichere Fehlerbehandlungs- und Protokollierungspraktiken.
- Abhängigkeitsverwaltung und Versions-Pinning.

**Beispiel — Python Secure Coding Standard** (illustrativ; für jede Sprache soll eine gleichwertige Dokumentation erstellt werden):

| Kategorie | Anforderung |
|-----------|-------------|
| **Verbotene Funktionen** | `eval()`, `exec()`, `pickle.loads()` bei nicht vertrauenswürdiger Eingabe, `os.system()` (stattdessen `subprocess.run()` mit shell=False verwenden), `yaml.load()` ohne SafeLoader |
| **Erforderliche Praktiken** | Parametrisierte Abfragen (keine String-Konkatenation für SQL), `secrets`-Modul zur Zufallsgenerierung (nicht `random`), Typhinweise für sicherheitskritische Funktionen, Eingabevalidierung mit Allowlists |
| **Genehmigte Kryptobibliotheken** | `cryptography`-Bibliothek (bevorzugt), `hashlib` (nur Hashing); verboten: `pycrypto` (nicht mehr gepflegt), individuelle Krypto-Implementierungen |
| **Fehlerbehandlung** | Keine sensiblen Daten in Exception-Nachrichten; strukturiertes Logging verwenden; spezifische Exceptions abfangen (kein nacktes `except:`) |
| **Abhängigkeiten** | Versionen in `requirements.txt` oder `pyproject.toml` pinnen; Changelogs vor grossen Versions-Upgrades prüfen; keine Abhängigkeiten mit bekannten kritischen CVEs |

Sprachspezifische Standards sollen im Code-Repository gespeichert (z. B. `docs/secure-coding/` oder gleichwertig), jährlich überprüft und bei neuen Schwachstellen oder Mustern aktualisiert werden.

Alle Entwickler sollen eine Schulung für sicheres Coding absolvieren, bevor ihnen Schreibzugriff auf Produktionscode gewährt wird (siehe Abschnitt Sicherheitsschulung für Entwickler).

---

## Code-Repositories und Versionskontrolle

Entwicklungscode soll in einem sicheren Code-Repository gespeichert werden, das die Anforderungen der Zugriffskontrollrichtlinie und die Funktionstrennung durchsetzt.

Repository-Zugriff soll dem Prinzip der minimalen Rechtevergabe folgen:

- Zugriff soll auf der Grundlage von Projektzuweisung und Rolle gewährt werden.
- Repository-Zugriff soll mindestens jährlich überprüft werden, in Übereinstimmung mit Identitäts- und Zugriffsmanagement-Überprüfungen.
- Ehemaligen Teammitgliedern soll der Zugriff noch am selben Werktag des Ausscheidens widerrufen werden.

Code-Repositories sollen Folgendes durchsetzen:

- **Versionskontrolle** mit angemessener Versionsarchivierung und Branching-Strategie.
- **Branch-Schutz** für Haupt-/Produktionsbranches — direkte Commits sind verboten; Änderungen erfordern Pull/Merge-Request-Genehmigung.
- **Commit-Signierung** empfohlen für Hochrisikoanwendungen.
- **Secret Scanning** zur Verhinderung der versehentlichen Übertragung von Anmeldedaten, API-Schlüsseln oder Tokens.

**Secret Scanning und Secrets-Management**:

Secret Scanning soll mindestens folgendes erkennen: API-Schlüssel, Zugriffstoken, private Schlüssel, Datenbankverbindungsstrings, Cloud-Anbieter-Anmeldedaten und Webhook-URLs.

**Prozess zur Behebung erkannter Geheimnisse**:

| Schritt | Massnahme | Zeitrahmen |
|---------|-----------|------------|
| 1 | **Commit blockieren** (Pre-Commit-Hook) oder in der CI/CD-Pipeline markieren | Sofort |
| 2 | **Kompromittierte Anmeldedaten widerrufen und rotieren** | Innerhalb von 4 Stunden für Produktionsgeheimnisse; innerhalb von 24 Stunden für Nicht-Produktionsgeheimnisse |
| 3 | **Aus der Repository-Historie entfernen** (falls committed) mit genehmigten Tools (z. B. git filter-branch, BFG Repo-Cleaner) | Innerhalb von 24 Stunden |
| 4 | **Exposition untersuchen** — feststellen, ob auf das Geheimnis durch nicht autorisierte Parteien zugegriffen wurde | Innerhalb von 48 Stunden |
| 5 | **Incident dokumentieren** — im Incident-Protokoll erfassen; an ISB eskalieren, wenn Produktionsgeheimnis gegenüber externen Parteien exponiert wurde | Gemäss Incident-Management-Richtlinie |

**Genehmigte Secrets-Verwaltung**:

| Umgebung | Genehmigte Methode |
|----------|-------------------|
| Entwicklung | Umgebungsvariablen, `.env`-Dateien (über `.gitignore` von der Versionskontrolle ausgeschlossen) |
| Test | Secrets Manager oder verschlüsselte Umgebungsvariablen |
| Produktion | Dedizierter Secrets Manager (z. B. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault oder gleichwertig) |
| CI/CD-Pipelines | Pipeline-Secrets-Store (z. B. GitHub Secrets, GitLab CI/CD Variables oder gleichwertig); keine hart kodierten Geheimnisse in Pipeline-Definitionen |

Hart kodierte Geheimnisse im Quellcode sind verboten. Secret-Scanning-Ergebnisse sollen wöchentlich vom Entwicklungsleiter überprüft werden.

---

## Code-Review

Sämtlicher Code soll vor der Freigabe durch qualifiziertes Personal überprüft werden, das nicht der Code-Autor oder Entwickler ist.

Code soll anhand der von der Organisation dokumentierten Richtlinien für sicheres Coding geprüft werden.

Code-Reviews sollen sowohl manuelle als auch automatisierte Techniken einsetzen:

- **Manuelles Peer-Review** — für alle Codeänderungen vor dem Merge in geschützte Branches erforderlich.
- **Sicherheitsorientiertes Review** — für Hochrisikoanwendungen erforderlich, durchgeführt von einem Security Champion oder einem sicherheitsgeschulten Prüfer.
- **Automatisiertes Review** — SAST-Tools (Static Application Security Testing) in die CI/CD-Pipeline integriert (z. B. SonarQube, Semgrep, Checkmarx oder gleichwertig).

**Code-Review-Workflow**:

| Schritt | Aktivität | Verantwortlicher |
|---------|-----------|-----------------|
| 1. **Einreichung** | Entwickler erstellt Pull/Merge Request mit Beschreibung, verknüpften Anforderungen und Selbstprüfungs-Checkliste | Entwickler |
| 2. **Automatisierte Prüfungen** | CI/CD-Pipeline führt SAST, SCA, Secret Scanning, Linting und Unit-Tests aus | Automatisiert (DevOps) |
| 3. **Manuelles Peer-Review** | Prüfer kontrolliert Logik, Lesbarkeit, Einhaltung der Coding-Standards, Testabdeckung | Peer-Prüfer |
| 4. **Sicherheitsreview** | Sicherheitsorientiertes Review anhand der Checkliste für sicheres Coding (Hochrisiko: Pflicht; mittleres Risiko: empfohlen) | Security Champion oder sicherheitsgeschulter Prüfer |
| 5. **Genehmigung und Merge** | Prüfer genehmigen; Merge in geschützten Branch | Prüfer / Entwicklungsleiter |

**Checkliste für sicheres Code-Review** (Mindestpunkte für sicherheitsorientiertes Review):

1. Eingabevalidierung auf alle externen Eingaben angewendet (Benutzereingaben, API-Parameter, Dateiuploads)
2. Ausgabekodierung angewendet, wo Daten gerendert werden (HTML, JSON, SQL, LDAP)
3. Authentifizierungs- und Autorisierungsprüfungen vorhanden und korrekt
4. Keine hart kodierten Geheimnisse, Anmeldedaten oder API-Schlüssel
5. Kryptographische Funktionen verwenden genehmigte Bibliotheken und Algorithmen
6. Fehlerbehandlung legt keine sensiblen Informationen offen
7. Protokollierung enthält sicherheitsrelevante Ereignisse ohne Protokollierung sensibler Daten
8. SQL-Abfragen verwenden parametrisierte Statements (keine String-Konkatenation)
9. Dateioperationen validieren Pfade (kein Path Traversal)
10. Drittanbieterabhängigkeiten auf geprüfte Versionen gepinnt

**Genehmigungsanforderungen nach Risikoniveau**:

| Risikoniveau | Mindestanzahl Genehmiger | Sicherheitsreview erforderlich |
|--------------|--------------------------|-------------------------------|
| Hochrisiko | 2 (einschliesslich Security Champion oder ISB-beauftragter Prüfer) | Pflicht |
| Mittleres Risiko | 1 | Empfohlen |
| Niedrigrisiko | 1 | Optional |

Befunde aus Code-Reviews sollen dokumentiert und bis zur Auflösung nachverfolgt werden, bevor Code für die Promotion genehmigt wird.

Code soll genehmigt werden, bevor er in Test- oder Produktionsumgebungen befördert wird.

---

## Sicherheitsgates in der CI/CD-Pipeline

Sicherheitsprüfungen sollen in der CI/CD-Pipeline an definierten Gates automatisiert werden.

**Pipeline-Sicherheitsgates**:

| Gate | Phase | Prüfungen | Massnahme bei Fehler |
|------|-------|-----------|---------------------|
| **Gate 1: Pre-Commit** | Entwickler-Workstation | Secret Scanning (Pre-Commit-Hook) | Commit blockieren; Entwickler muss Geheimnis entfernen |
| **Gate 2: Build** | CI-Pipeline — Build-Phase | SAST-Scan, SCA-Abhängigkeitsscan, Lizenzkompatiblitätsprüfung, Unit-Tests | Merge blockieren; Entwickler muss beheben |
| **Gate 3: Vor Deployment** | CI-Pipeline — Vor-Deployment | DAST-Scan (Hochrisiko/mittleres Risiko), Integrationstests, Sicherheitsregressionstests | Deployment blockieren; beheben oder eskalieren |
| **Gate 4: Produktionsdeployment** | Deployment-Pipeline | Genehmigungsprüfung (erforderliche Genehmiger), Change-Ticket-Verifizierung, Umgebungsvalidierung | Deployment blockieren bis Genehmigungen vorliegen |

**Fehlerschwellen** (automatische Gate-Blockierung):

| Befundschweregrad | SAST/SCA Gate 2 | DAST Gate 3 |
|-------------------|-----------------|-------------|
| Kritisch | Blockieren | Blockieren |
| Hoch | Blockieren | Blockieren |
| Mittel | Warnung (als technische Schuld erfassen) | Warnung (als technische Schuld erfassen) |
| Niedrig | Nur protokollieren | Nur protokollieren |

**Override-Regeln**: Pipeline-Gate-Overrides erfordern die Genehmigung des ISB (im Change-Ticket mit Risikoakzeptanz und kompensierenden Massnahmen dokumentiert). Notfalldeployments können Gate-3-DAST mit ISB-Genehmigung umgehen, mit obligatorischem nachträglichem Scan innerhalb von 72 Stunden.

Ergebnisse der Pipeline-Sicherheitsgates sollen dem Entwicklungsleiter wöchentlich und dem ISB monatlich gemeldet werden.

---

## Sicherheitstestanforderungen

Sicherheitstestprozesse sollen im Entwicklungslebenszyklus definiert und implementiert werden. Tests sollen vor dem Deployment in die Produktion validieren, dass die Sicherheitsanforderungen erfüllt wurden.

**Erforderliche Tests nach Risikoniveau**:

| Testart | Hochrisiko | Mittleres Risiko | Niedrigrisiko |
|---------|-----------|-----------------|--------------|
| **SAST** | Pro Commit oder täglich | Pro Commit oder täglich | Wöchentlich |
| **SCA** (Abhängigkeitsscan) | Täglich oder kontinuierlich | Täglich oder kontinuierlich | Wöchentlich |
| **DAST** | Pro Deployment oder wöchentlich | Monatlich | Optional |
| **Penetrationstest** | Jährlich + vor erstem Release + nach wesentlicher Änderung | Alle 2 Jahre | Optional |

**Grundlegende Testanforderungen**:

- Alle Anwendungssicherheitstests sollen mindestens die **OWASP-Top-10:2025**-Kategorien testen: Fehlerhafte Zugriffskontrolle, Sicherheitsfehlkonfiguration, Fehler in der Software-Lieferkette, kryptographische Fehler, Injection, unsicheres Design, Authentifizierungsfehler, Software- oder Datenintegritätsfehler, Fehler bei der Sicherheitsprotokollierung und -alarmierung sowie fehlerhafte Behandlung von Ausnahmezuständen.
- Alle Vor-Produktionstests sollen in einer Testumgebung stattfinden, die der Produktionsumgebung so weit wie möglich entspricht.

**Anforderungen an die Gleichwertigkeit der Testumgebung**:

| Komponente | Anforderung an Produktionsparität |
|------------|----------------------------------|
| Betriebssystem | Gleiche OS und Version |
| Laufzeit / Framework-Versionen | Gleiche Haupt- und Nebenversionen |
| Datenbank-Engine | Gleiche Engine und Hauptversion |
| Netzwerkarchitektur | Gleiche Segmentierungsmodell und Firewall-Regeln (IP-Bereiche können abweichen) |
| TLS/SSL-Konfiguration | Gleiche Cipher Suites und Protokollversionen |
| Authentifizierung | Gleicher Authentifizierungsmechanismus und MFA-Konfiguration |
| Load Balancer / Reverse Proxy | Gleicher Typ und Konfiguration |
| Containerisierung / Orchestrierung | Gleiche Plattform und Version (sofern anwendbar) |

**Zulässige Abweichungen**: IP-Adressen, Hostnamen, Skalierung (weniger Instanzen in Test zulässig), Überwachungs-Volumenschwellen und synthetische/anonymisierte Daten anstelle von Produktionsdaten.

**Umgebungsverifizierung**: Umgebungsparität soll vor grossen Sicherheitstests (Penetrationstests, DAST) verifiziert werden. Die Verifizierung soll dokumentiert und vom DevOps-/Plattformteam abgezeichnet werden.

**Sicherheit der Testumgebung**: Testumgebungen sollen denselben Zugriffskontrollen unterliegen wie Produktionsumgebungen. Testumgebungen sollen nicht über das Internet erreichbar sein, sofern nicht für DAST-Tests erforderlich (mit zeitlich begrenzten Firewall-Regeln).

- Alle Penetrationstests sollen von einem externen Spezialunternehmen durchgeführt werden.
- Alle öffentlich zugänglichen Webanwendungen sollen mindestens jährlich oder nach einer wesentlichen Änderung mit manuellen oder automatisierten Schwachstellensicherheitstools getestet werden.

**Standards und Umfang von Penetrationstests**:

| Anwendungstyp | Testansatz | Häufigkeit |
|---------------|-----------|-----------|
| Internetfähige Webanwendung (Hochrisiko) | Vollständige OWASP-Testing-Guide-Bewertung + Geschäftslogiktests | Jährlich + vor erstem Release + nach wesentlicher Änderung |
| Internetfähige Webanwendung (mittleres Risiko) | OWASP-Top-10-fokussierte Bewertung | Alle 2 Jahre |
| Interne Anwendung (Hochrisiko) | Authentifizierter Test mit Geschäftslogiküberprüfung | Jährlich |
| API-only-Dienst (Hochrisiko) | API-Sicherheitstest (OWASP API Security Top 10) | Jährlich |
| Mobile Anwendung | Mobilspezifischer Test (OWASP MASTG) | Jährlich für Hochrisiko |

**Im Umfang** (Minimum): Authentifizierung und Session-Management, Autorisierung und Zugriffssteuerung, Eingabevalidierung (Injection, XSS, SSRF), Geschäftslogik, API-Sicherheit, kryptographische Implementierung, Konfiguration und Deployment, Fehlerbehandlung und Informationspreisgabe.

**Ausserhalb des Umfangs** (sofern nicht explizit einbezogen): Denial-of-Service-Tests, Social Engineering, Tests der physischen Sicherheit, von Dritten gehostete Komponenten (werden separat durch den Anbieter getestet).

**Teststandards**: Penetrationstests sollen dem OWASP Testing Guide v4.2 und/oder PTES (Penetration Testing Execution Standard) folgen. Testberichte sollen enthalten: Management-Zusammenfassung, Methodik, Befunde mit CVSS-Bewertung, Belege (Screenshots, Request/Response), Massnahmenempfehlungen und Verifizierung nach Behebung.

**Anbieterauswahlkriterien**: Penetrationstest-Anbieter sollen relevante Zertifizierungen besitzen (z. B. CREST, OSCP, CEH) und Nachweise über Berufshaftpflichtversicherung vorlegen. Anbieterverträge sollen unterzeichnete Rules of Engagement und NDA umfassen.

**Massnahmen nach dem Test**: (1) Befunde gemäss Schwachstellenbehebungs-SLAs beheben → (2) Anbieter testet kritische/hohe Befunde nach der Behebung erneut → (3) Abschlussbericht mit Nachtestergebnissen dem ISB und dem Management-Review-Team präsentiert → (4) Erkenntnisse in Standards für sicheres Coding eingearbeitet → (5) Bericht 5 Jahre aufbewahrt.

**Software Bill of Materials (SBOM)**:

- Hochrisikoanwendungen sollen eine SBOM im CycloneDX- oder SPDX-Format führen.
- SBOMs sollen automatisch während des Build-Prozesses generiert werden (bei jedem Build für Hochrisiko; wöchentlich für mittleres Risiko).
- SBOMs sollen bei Änderungen an Abhängigkeiten aktualisiert und vierteljährlich auf bekannte Schwachstellen überprüft werden.

**SBOM-Inhaltsanforderungen**: Jede SBOM soll enthalten: Komponentenname und -version, Lieferant/Autor, Lizenztyp, Abhängigkeitsbeziehungen (direkt und transitiv) sowie bekannten Schwachstellenstatus (CVE-Referenzen sofern anwendbar).

**Vierteljährlicher SBOM-Überprüfungsprozess**: (1) Aktuelle SBOM erstellen → (2) Alle Komponenten gegen Schwachstellendatenbanken (NVD, OSV, GitHub Advisory Database) abgleichen → (3) Komponenten mit bekannten Schwachstellen, End-of-Life-Status oder Lizenzänderungen identifizieren → (4) Behebungsplan für identifizierte Probleme erstellen (gemäss Schwachstellenbehebungs-SLAs).

**SBOM-Schwachstellenüberwachung**: SCA-Tools sollen SBOM-Komponenten kontinuierlich gegen Schwachstellendatenbanken überwachen. Neue kritische/hohe Schwachstellen, die SBOM-Komponenten betreffen, sollen innerhalb von 24 Stunden Alarme an den Entwicklungsleiter auslösen.

**SBOM-Aufbewahrung**: SBOMs sollen für den Lebenszyklus der Anwendung plus 3 Jahre aufbewahrt werden.

Testergebnisse, einschliesslich Penetrationstestberichte, sollen dem Management-Review-Team gemeldet werden.

---

## Schwachstellenbehebung

Im Rahmen der Entwicklung und des Testens identifizierte Sicherheitsschwachstellen sollen innerhalb definierter Zeitrahmen entsprechend dem Schweregrad behoben werden.

**Service Level Agreements für die Schwachstellenbehebung**:

| Schweregrad | CVSS-Score | Behebungs-SLA | Auswirkung auf Deployment |
|-------------|-----------|---------------|--------------------------|
| **Kritisch** | 9,0–10,0 | 7 Tage | Deployment blockiert, wenn unbehoben |
| **Hoch** | 7,0–8,9 | 30 Tage | Deployment blockiert, wenn überfällig |
| **Mittel** | 4,0–6,9 | 90 Tage | Als technische Schuld erfassen |
| **Niedrig** | 0,1–3,9 | 180 Tage | Für nächsten Major Release einplanen |

Alle im Rahmen der Testphase identifizierten Schwachstellen, einschliesslich Penetrationstests, sollen vor der Promotion in die Produktion behoben oder über den Risikomanagement- und Ausnahmenprozess behandelt werden.

**Eskalationsprozess**:

- Schwachstellen, die das Behebungs-SLA überschreiten, sollen an den ISB und den Anwendungseigentümer eskaliert werden.
- Kritische und hohe Schwachstellen, die nach dem SLA überfällig sind, sollen nachfolgende Deployments blockieren bis zur Behebung oder Genehmigung einer Ausnahme mit kompensierenden Massnahmen.
- Der Behebungsstatus von Schwachstellen soll monatlich überprüft und vierteljährlich dem Management-Review-Team gemeldet werden.

---

## Testdatenschutz

Produktionsdaten sollen nicht für Tests oder die Entwicklung verwendet werden.

Personendaten (gemäss nDSG Art. 5) sollen nicht für Tests oder die Entwicklung verwendet werden.

Wenn für den Testprozess sensible Informationen erforderlich sind, sollen diese:

- **bereinigt** (sensible Felder entfernt oder ersetzt),
- **anonymisiert** (irreversible Entfernung identifizierender Merkmale) oder
- **pseudonymisiert** (identifizierende Daten durch künstliche Kennungen ersetzt) werden.

**Synthetische Daten** (künstlich generierte Daten ohne Bezug zu realen Personen) sind der bevorzugte Ansatz und sollen verwendet werden, wo machbar.

Die Erstellung und Verwendung von Testdatensätzen soll dokumentiert und vom Dateneigentümer genehmigt werden. Testdatensätze mit transformierten Personendaten sollen mindestens als INTERN klassifiziert werden.

Testdaten sollen sicher gelöscht werden, wenn sie nicht mehr benötigt werden.

---

## Beförderung von Code in die Produktion

Code soll nur von genehmigtem Personal in die Produktion befördert werden und soll dem dokumentierten Änderungsmanagementprozess unterliegen.

Vor der Beförderung in die Produktion:

- Alle erforderlichen Sicherheitsgates sollen bestanden worden sein (Sicherheitstests, Code-Review, Schwachstellenbehebung).
- Die Produktionsumgebung soll gesichert werden, um im Falle einer fehlgeschlagenen Änderung einen Rollback zu ermöglichen.
- Testdaten sollen aus der Anwendung entfernt werden.
- Keine Entwicklungsdateien, Debug-Konfigurationen, Testkonten oder Testdaten sollen in der Produktionsumgebung vorhanden sein.
- Für Hochrisikoanwendungen soll der ISB oder eine designierte Sicherheitsbehörde eine explizite Abzeichnung geben.

Promotionsnachweise sollen den Change-Ticket-Verweis, den Genehmiger, den Sicherheitsgate-Status und den Deployment-Zeitstempel enthalten.

---

## Ausgelagerte Entwicklung

Wenn Softwareentwicklung an Drittauftragnehmer oder Entwicklungspartner ausgelagert wird, sollen die sicheren Entwicklungsanforderungen der Organisation Anwendung finden.

**Vertragliche Anforderungen sollen umfassen**:

- Einhaltung der Standards für sicheres Coding und der Sicherheitsanforderungen der Organisation.
- Sicherheitstestpflichten (SAST, DAST, SCA) mit Berichterstattung an die Organisation.
- Behebungs-SLAs für Schwachstellen, die mit dieser Richtlinie abgestimmt sind.
- Benachrichtigung bei Sicherheitsincidents innerhalb von 24 Stunden nach Entdeckung.
- Recht der Organisation auf Audit der Sicherheitspraktiken des Auftragnehmers mit 30 Tagen Vorankündigung.
- Teilnahmerechte bei Code-Review und Sicherheitsarchitekturprüfung.

**Verifizierung der Auftragnehmer-Konformität**:

- Auftragnehmer sollen Sicherheitstestberichte (SAST/DAST/SCA-Ergebnisse, Behebungsstatus) in vereinbarten Abständen einreichen.
- Hochrisiko-Outsourcing-Projekte sollen bei grossen Meilensteinen (Designfreigabe, Vor-Produktion) einer Sicherheitsprüfung durch das sicherheitsqualifizierte Personal der Organisation unterzogen werden.
- Von Auftragnehmern gelieferter Code soll vor der Abnahme demselben Code-Review- und Sicherheitstestprozess unterzogen werden wie intern entwickelter Code.

---

## Sicherheitsschulung für Entwickler

Alle Entwickler sollen eine ihrer Rolle und Verantwortung angemessene Sicherheitsschulung absolvieren.

**Schulungsanforderungen**:

| Schulungsart | Zielgruppe | Häufigkeit | Mindestdauer |
|--------------|-----------|-----------|--------------|
| **Initiale Sicherheitsschulung** | Alle Entwickler | Vor Produktionscode-Zugriff | 4 Stunden |
| **Jährliche Auffrischung** | Alle Entwickler | Jährlich | 2 Stunden |
| **Security-Champion-Schulung** (optional für KMU) | Nominierte Security Champions | Initial + jährlich | 8 Stunden + 4 Stunden |

Die Schulung soll mindestens abdecken:

- OWASP-Top-10-Schwachstellen und Abhilfetechniken.
- Sichere Coding-Praktiken relevant für den Technologie-Stack des Entwicklers.
- Die Richtlinie zur sicheren Entwicklung und die Coding-Standards der Organisation.
- Häufige Softwareschwachstellen (CWE/SANS Top 25).

Der Abschluss der Schulung soll vor der Gewährung des Produktionscode-Zugriffs erfasst und verifiziert werden. Schulungsunterlagen sollen für die Dauer der Beschäftigung plus 3 Jahre aufbewahrt werden.

Sofern Ressourcen vorhanden sind, sollte die Organisation ein **Security-Champion-Programm** einrichten — nominierte Entwickler innerhalb jedes Teams, die eine fortgeschrittene Sicherheitsschulung erhalten und als erste Anlaufstelle für Sicherheitsfragen innerhalb ihres Teams dienen.

**Security-Champion-Programm** (sofern etabliert):

**Auswahlkriterien**: Security Champions sollen aus Entwicklungsteams nominiert werden auf der Grundlage von: nachgewiesenem Interesse an Sicherheit, mindestens 2 Jahren Entwicklungserfahrung, Bereitschaft, ca. 10 % der Arbeitszeit für Sicherheitsaktivitäten aufzuwenden, und Empfehlung des Teamleiters.

**Verantwortlichkeiten**:
- Sicherheitsorientierte Code-Reviews für Hochrisikoänderungen im Team durchführen.
- Sichere Coding-Anleitungen und Mentoring für Teammitglieder bereitstellen.
- An Bedrohungsmodellierungssitzungen als Sicherheitsvertreter des Teams teilnehmen.
- Sicherheitsbedenken an den ISB oder das Sicherheitsteam eskalieren.
- Aktuelle Bedrohungen und Schwachstellen relevant für den Technologie-Stack des Teams im Blick behalten.
- Sicherheitskultur und -bewusstsein im Team fördern.

**Schulung**: Erstschulung: 8 Stunden (OWASP Top 10 vertieft, sichere Architekturmuster, Bedrohungsmodellierung, Sicherheitstesttools). Jährliche Auffrischung: 4 Stunden (neue Bedrohungen, neue Angriffstechniken, aktualisierte Standards).

**Anreize**: Security-Champion-Beiträge sollen in Leistungsbeurteilungen anerkannt werden. Die Organisation sollte Konferenzbesuche, Zertifizierungsförderung oder ähnliche berufliche Entwicklungsmöglichkeiten in Betracht ziehen.

**Programm-Kennzahlen**: Anzahl aktiver Security Champions (Ziel: mindestens 1 pro Entwicklungsteam), Teilnahmequote an Sicherheitsreviews, im Code-Review identifizierte Sicherheitsbefunde, Schulungsabschlussrate.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Sicherheitsgate-Genehmigung für Hochrisikoanwendungen; Ausnahmengenehmigung; Eskalationsbehörde; Aufsicht über das Schulungsprogramm |
| **Entwicklungsleiter** | SDLC-Sicherheitsintegration; Code-Review-Durchsetzung; Pflege der Standards für sicheres Coding; Aufsicht über Schwachstellenbehebung; Anwendungsrisikoklassifizierung |
| **Security Champion** (sofern etabliert) | Sicherheitsfürsprache im Entwicklungsteam; sicherheitsorientiertes Code-Review; Mentoring für sicheres Coding |
| **Entwickler** | Einhaltung der Standards für sicheres Coding; Schwachstellenbehebung; Abschluss der Sicherheitsschulung; Teilnahme am Code-Review |
| **QA / Testleiter** | Durchführung von Sicherheitstests; Testumgebungsmanagement; Testdatenschutz; Sicherheitstestberichterstattung |
| **DevOps / Plattformteam** | CI/CD-Sicherheitstools-Integration; Umgebungssegregation; Deployment-Automatisierung; Secret Scanning |
| **Anwendungseigentümer** | Eingabe zur Anwendungsrisikoklassifizierung; Ausnahmenanträge; Genehmigung von Sicherheitsanforderungen |

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Verantwortlicher | Häufigkeit |
|---|----------|-----------------|------------|
| 1 | **Anwendungsrisikoklassifizierungsregister** (alle Anwendungen nach Risikoniveau klassifiziert) | Entwicklungsleiter / ISB | *Kontinuierlich gepflegt; jährlich überprüft; Ziel: 100 % der Anwendungen klassifiziert* |
| 2 | **Sicherheitsanforderungsdokumentation** (Anforderungsspezifikationen, Bedrohungsmodelle für Hochrisiko) | Entwicklungsleiter | *Pro Projekt; für den Lebenszyklus der Anwendung aufbewahrt* |
| 3 | **SAST/SCA-Scan-Berichte** (Tool-Ausführungsprotokolle, Befunde, Behebungsstatus) | DevOps / Entwicklungsleiter | *Gemäss Richtlinienhäufigkeit nach Risikoniveau; 2 Jahre aufbewahrt* |
| 4 | **Penetrationstestberichte** (Umfang, Befunde, Behebungsverifizierung) | ISB | *Jährlich für Hochrisiko; alle 2 Jahre für mittleres Risiko; 5 Jahre aufbewahrt* |
| 5 | **Code-Review-Unterlagen** (Review-Kommentare, Genehmigungsunterlagen, Merge-Request-Historie) | Entwicklungsleiter | *Pro Codeänderung; 2 Jahre aufbewahrt* |
| 6 | **Schwachstellenbehebungsunterlagen** (Tickets mit SLA-Tracking, Abschlussnachweise) | Entwicklungsleiter | *Pro Schwachstelle; monatlich überprüft; 3 Jahre aufbewahrt* |
| 7 | **Dokumentation zur Umgebungssegregation** (Netzwerkdiagramme, Zugriffskontrollunterlagen) | DevOps / IT Operations | *Jährlich überprüft; bei Änderungen aktualisiert* |
| 8 | **Sicherheitsschulungsunterlagen für Entwickler** (Abschlussdaten, behandelte Schulungsinhalte) | ISB / HR | *Pro Entwickler verfolgt; jährlich überprüft; Ziel: 100 % Abschluss* |
| 9 | **Sicherheitsberichte für ausgelagerte Entwicklung** (Auftragnehmer-SAST/DAST/SCA-Ergebnisse, Audit-Unterlagen) | Entwicklungsleiter / ISB | *Gemäss Vertragsbedingungen; für Vertragsdauer + 3 Jahre aufbewahrt* |
| 10 | **Produktionsdeployment-Unterlagen** (Change-Tickets, Sicherheitsgate-Abzeichnung, Rollback-Pläne) | Änderungsmanagement / DevOps | *Pro Deployment; 3 Jahre aufbewahrt* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team überprüft die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf SAST/DAST/SCA-Scan-Berichte, Code-Review-Unterlagen, Penetrationstestberichte, Entwickler-Schulungsunterlagen, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll vorab durch den Information Security Manager genehmigt und mit dokumentierter Risikoakzeptanz, kompensierenden Massnahmen und einem definierten Prüfdatum erfasst werden. Ausnahmen sollen dem Management-Review-Team gemeldet werden. Notfalldeployments, die Sicherheitsgates umgehen, erfordern die Genehmigung des ISB und eine nachträgliche Sicherheitsvalidierung innerhalb von 72 Stunden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der Standards für sichere Entwicklung (OWASP, NIST SSDF, CWE/SANS Top 25), neue Bedrohungen und Angriffstechniken, regulatorische Änderungen, Änderungen der Entwicklungstools und -methoden sowie Erkenntnisse aus Sicherheitsincidents und Penetrationstests berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zum sicheren Entwicklungslebenszyklus — Zuordnung zu ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Leitlinien für Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortung |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Normen |
| Abschnitt 7.3 Bewusstsein | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 8.4 Zugriff auf Quellcode |
| | **8.25 Sicherer Entwicklungslebenszyklus** |
| | **8.26 Sicherheitsanforderungen an Anwendungen** |
| | 8.27 Sichere Systemarchitektur und Ingenieursprinzipien |
| | 8.28 Sicheres Coding |
| | **8.29 Sicherheitstests in Entwicklung und Abnahme** |
| | 8.30 Ausgelagerte Entwicklung |
| | 8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen |
| | 8.33 Testinformationen |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 7 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 8 — Technische und organisatorische Massnahmen zum Datenschutz |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (sofern anwendbar) | Art. 25 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex-A-Massnahmen 8.25, 8.26, 8.29 — Sichere Entwicklung, Sicherheitsanforderungen an Anwendungen, Sicherheitstests |
| ISO/IEC 27002:2022 | Abschnitte 8.25–8.31, 8.33 — Implementierungsleitfaden für sichere Entwicklungsmassnahmen |
| NIST SP 800-218 (SSDF) | Secure Software Development Framework — Praxisgruppen PO, PS, PW, RV |
| OWASP Top 10:2025 | Grundlegende Testbasis — enthält Fehler in der Software-Lieferkette und fehlerhafte Behandlung von Ausnahmezuständen |
| CWE/SANS Top 25 | Gefährlichste Softwareschwachstellen — Referenz für sicheres Coding |

---

<!-- QA_VERIFIED: 2026-03-29 -->
