<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.28-DE:operational:OP-POL:a.8.28 -->
**ISMS-OP-POL-A.8.28 — Sicheres Coding**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Sicheres Coding |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.28 |
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

- ISO/IEC 27001:2022 Massnahme A.8.28 — Sicheres Coding
- ISO/IEC 27002:2022 Abschnitt 8.28 — Implementierungsleitfaden für sicheres Coding
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1
- NIST SP 800-53 Rev 5 — SA-15 (Entwicklungsprozess, Standards und Tools), SA-16 (Entwicklerbereitgestellte Schulung), SA-17 (Entwickler-Sicherheitsarchitektur und -design)
- OWASP Secure Coding Practices — Quick Reference Guide
- OWASP Top 10 (2021) — Web Application Security Risks
- CWE/SANS Top 25 — Most Dangerous Software Weaknesses (2025 edition)
- CIS Controls v8 — Safeguards 16.1–16.14 (Sicherheit von Anwendungssoftware)
- CERT Secure Coding Standards (SEI/Carnegie Mellon)

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zum sicheren Coding |
|-----------|--------------------------|
| A.5.8 Informationssicherheit im Projektmanagement | Sicherheitsanforderungen werden zu Projektbeginn definiert |
| A.5.23 Informationssicherheit bei der Nutzung von Cloud-Diensten | Sicheres Coding für Cloud-bereitgestellte Anwendungen |
| A.8.4 Zugriff auf Quellcode | Repository-Zugriffssteuerung und Branch-Schutz |
| A.8.8 Management technischer Schwachstellen | Schwachstellenbehebung für bereitgestellten Code |
| A.8.9 Konfigurationsmanagement | Sichere Konfiguration von Entwicklungstools und -umgebungen |
| A.8.15 Protokollierung | Protokollierungsanforderungen auf Anwendungsebene |
| A.8.24 Einsatz von Kryptographie | Kryptographische Implementierung im Anwendungscode |
| A.8.25–26–29 Sicherer Entwicklungslebenszyklus | Übergreifendes SDLC-Rahmenwerk; Sicherheitsanforderungen, Tests |
| A.8.31 Trennung von Umgebungen | Isolation von Entwicklungs-, Test- und Produktionsumgebungen |
| A.8.32 Änderungsmanagement | Gesteuerte Bereitstellung von Codeänderungen in die Produktion |

**Verwandte interne Richtlinien**:

- Richtlinie zum sicheren Entwicklungslebenszyklus
- Richtlinie zum Zugriff auf Quellcode
- Richtlinie zum Schwachstellenmanagement
- Richtlinie zum Einsatz von Kryptographie
- Richtlinie zum Änderungsmanagement
- Protokollierungsrichtlinie

---

# Richtlinie zum sicheren Coding

## Zweck

Zweck dieser Richtlinie ist es, verbindliche Prinzipien für sicheres Coding festzulegen, die im gesamten Softwareentwicklungslebenszyklus angewendet werden sollen. Sicheres Coding verhindert, dass Schwachstellen in die Codebasis gelangen, reduziert die Angriffsfläche und schützt die Informationswerte, Kunden und den Ruf der Organisation. Schlechte Coding-Praktiken — unzureichende Eingabevalidierung, schwache Schlüsselgenerierung, hart kodierte Anmeldedaten, unzureichende Fehlerbehandlung — schaffen ausnutzbare Schwachstellen, auf die Angreifer routinemässig abzielen.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 7 (Datenschutz durch Technik und Voreinstellung) und Art. 8 (technische und organisatorische Massnahmen), indem sie vorschreibt, dass Sicherheit von der Designphase an in den Anwendungscode integriert wird. Sofern die Organisation Daten von Personen im EU/EWR-Raum bearbeitet, gelten auch die DSGVO-Anforderungen Art. 25 (Datenschutz durch Technik und Voreinstellung) und Art. 32 (Sicherheit der Verarbeitung). Sicheres Coding ist eine grundlegende technische Massnahme zum Nachweis, dass Systeme, die Personendaten verarbeiten, so konstruiert sind, dass unbefugter Zugriff, Datenpannen und Integritätsverletzungen verhindert werden.

## Geltungsbereich

Alle Softwareentwicklungsaktivitäten, bei denen die Organisation Quellcode schreibt, modifiziert oder pflegt. Dies umfasst:

- Alle intern entwickelten Anwendungen (Web, Mobile, Desktop, API, Microservices).
- Infrastructure-as-Code (IaC), Konfigurationsmanagement-Skripte und CI/CD-Pipeline-Definitionen.
- Individuelle Integrationen, Plugins und Erweiterungen für Drittanbieterplattformen.
- Open-Source-Beiträge, die im Namen der Organisation geleistet werden.
- Code, der von Auftragnehmern, ausgelagerten Entwicklungsteams und Offshore-Entwicklern im Auftrag der Organisation geschrieben wird.

Alle Entwickler, Sicherheitsingenieure, QA-Ingenieure, DevOps-Ingenieure, Auftragnehmer und Drittanbieter-Entwicklungsteams, die Code für die Organisation schreiben.

**Nicht im Geltungsbereich**: Kommerzielle Standardsoftware (COTS) ohne Anpassung (geregelt durch Lieferantensicherheitsbewertung); Laufzeit-Schwachstellenmanagement in der Produktion nach dem Deployment (geregelt durch A.8.8); Governance des sicheren Entwicklungslebenszyklus (geregelt durch A.8.25-26-29); Zugriffssteuerung für Quellcode (geregelt durch A.8.4).

## Grundsatz

Sämtlicher für oder im Auftrag der Organisation erstellter Quellcode soll dokumentierten Standards für sicheres Coding folgen. Sicherheit soll vor Beginn des Codings berücksichtigt, während des Codings angewendet und nach Abschluss des Codings verifiziert werden. Entwickler sollen sich nicht allein auf Sicherheitstests verlassen, um Mängel zu finden — sicheres Coding verhindert, dass Mängel von vornherein eingebracht werden.

Die Organisation soll explizit festlegen, welchen Coding-Standards sie folgt, unter Bezugnahme auf anerkannte Branchenrahmen (OWASP, CWE/SANS Top 25, CERT oder sprachspezifische Richtlinien). Allgemeine Behauptungen über «sicheres Coding» ohne Angabe eines Rahmens sind für Audit-Zwecke unzureichend.

---

## Standards für sicheres Coding

Die Organisation soll dokumentierte Standards für sicheres Coding einrichten und pflegen, die für jede aktiv genutzte Programmiersprache und jedes Framework anwendbar sind.

**Basis-Rahmenwerke**:

| Rahmenwerk | Umfang | Anwendung |
|-----------|--------|-----------|
| OWASP Top 10 (2021) | Schwachstellen in Webanwendungen | Pflichtliche Referenz für allen webfähigen Code |
| CWE/SANS Top 25 | Gefährlichste Softwareschwachstellen | Pflichtliche Referenz für allen Code |
| OWASP Secure Coding Practices | Technologieunahängige Coding-Checkliste | Pflichtliche Referenz für die gesamte Entwicklung |
| CERT Secure Coding Standards | Sprachspezifisches sicheres Coding (C, C++, Java, Perl) | Pflicht, wo sprachspezifische Standards vorhanden |

**Sprachspezifische Standards**:

Der Entwicklungsleiter soll ein Register genehmigter Sprachen und der damit verbundenen Referenzen für sicheres Coding pflegen. Mindestens:

| Sprache / Framework | Referenz für sicheres Coding |
|--------------------|------------------------------|
| Python | PEP 8 + OWASP Python Security + Bandit-Regelwerk |
| JavaScript / TypeScript | ESLint-Sicherheits-Plugin-Regeln + OWASP NodeGoat-Referenz |
| Java | CERT Oracle Secure Coding Standard für Java + SpotBugs/FindSecBugs-Regeln |
| C / C++ | CERT C/C++ Secure Coding Standards + Compiler-Warnungsdurchsetzung |
| Go | Go-Sicherheits-Best-Practices + govulncheck |
| .NET / C# | Microsoft Secure Coding Guidelines + Roslyn-Analyser |
| PHP | OWASP PHP Security Cheat Sheet + Psalm/PHPStan-Regeln |

Wenn eine Sprache verwendet wird, die keinen Eintrag in diesem Register hat, soll der Entwicklungsleiter die anwendbare Referenz für sicheres Coding dokumentieren, bevor die Sprache in die Produktion eingeführt wird.

**Überprüfung der Coding-Standards**: Standards für sicheres Coding sollen jährlich überprüft werden, oder wenn eine neue Sprache oder ein neues Framework übernommen wird, oder wenn eine wesentliche Schwachstellenklasse entsteht, die zusätzliche Leitlinien erfordert.

---

## Prävention häufiger Schwachstellen

Entwickler sollen Code schreiben, der die durch OWASP Top 10 und CWE/SANS Top 25 identifizierten Schwachstellenklassen verhindert. Die folgenden Abschnitte definieren verbindliche Coding-Praktiken für die häufigsten Schwachstellenkategorien.

### Eingabevalidierung

Alle Eingaben aus externen Quellen sollen als nicht vertrauenswürdig behandelt und vor der Verarbeitung validiert werden.

**Anforderungen**:

- Alle Eingaben serverseitig validieren, unabhängig von der clientseitigen Validierung. Clientseitige Validierung verbessert die Benutzererfahrung, bietet aber keine Sicherheit.
- Allowlist-Validierung (positiv) verwenden: definieren, was erlaubt ist, alles andere ablehnen. Denylist-Validierung (negativ) ist als alleinige Massnahme unzureichend.
- Datentyp, Länge, Wertebereich und Format validieren. Fehlerhafte Eingaben vor der Verarbeitung ablehnen.
- Alle Eingaben aus Formularen, URL-Parametern, HTTP-Headern, Cookies, API-Payloads, Dateiuploads und Daten aus vorgelagerten Systemen validieren und bereinigen.
- Parametrisierte Abfragen oder Prepared Statements für alle Datenbankinteraktionen verwenden. Die Konkatenation von Benutzereingaben in SQL-Statements ist verboten.
- Dateiuploads validieren: erlaubte Dateitypen einschränken, Grösseneinschränkungen durchsetzen, auf Malware scannen, hochgeladene Dateien ausserhalb des Web-Roots speichern und hochgeladene Dateien niemals ausführen.

### Ausgabekodierung

Alle für Benutzer oder externe Systeme gerenderten Ausgaben sollen kodiert werden, um Injection-Angriffe zu verhindern.

**Anforderungen**:

- Kontextgeeignete Ausgabekodierung (HTML, JavaScript, URL, CSS, XML) beim Rendering dynamischer Inhalte anwenden.
- Vom Framework bereitgestellte Kodierungsfunktionen anstelle von individuellen Implementierungen verwenden.
- Ausgabe am Rendering-Punkt kodieren, nicht am Speicher-Punkt.
- Content-Type- und Charset-Header bei allen HTTP-Antworten korrekt setzen.
- Content Security Policy (CSP)-Header implementieren, um Cross-Site-Scripting (XSS)-Risiken zu mindern.

### Authentifizierung und Session-Management

Anwendungscode, der Authentifizierung und Session-Verwaltung implementiert, soll etablierten sicheren Mustern folgen.

**Anforderungen**:

- Keine individuellen Authentifizierungsschemata implementieren. Das genehmigte Authentifizierungsframework oder den Identitätsanbieter der Organisation verwenden.
- Passwörter mit genehmigten adaptiven Hashing-Algorithmen (bcrypt, scrypt oder Argon2id) mit eindeutigen Salts speichern. MD5, SHA-1 und ungesalzene Hashes sind verboten.
- Kontosperrung oder progressive Verzögerungen nach wiederholten fehlgeschlagenen Authentifizierungsversuchen implementieren.
- Session-Kennzeichner mit kryptographisch sicheren Zufallsgeneratoren generieren. Session-IDs sollen ausreichende Länge haben (mindestens 128 Bit Entropie).
- Sichere Cookie-Attribute setzen: `Secure`, `HttpOnly`, `SameSite`. Session-Cookies nur über TLS übertragen.
- Sessions bei Abmeldung, Passwortänderung und Privilegieneskalation invalidieren. Geeignete Session-Timeout-Werte setzen.
- Session-Kennzeichner nicht in URLs, Fehlermeldungen oder Protokollen preisgeben.

### Fehlerbehandlung und Protokollierung

Die Fehlerbehandlung von Anwendungen soll die Preisgabe von Informationen verhindern und die Sicherheitsüberwachung unterstützen.

**Anforderungen**:

- Generische Fehlermeldungen für Benutzer anzeigen. Keine Stack Traces, Datenbankfehlermeldungen, interne Dateipfade, Framework-Versionsnummern oder Server-Konfigurationsdetails preisgeben.
- Alle sicherheitsrelevanten Ereignisse protokollieren: Authentifizierungserfolge und -fehler, Autorisierungsfehler, Eingabevalidierungsfehler, Anwendungsfehler und administrative Aktionen.
- Ausreichenden Kontext für Untersuchungen protokollieren: Zeitstempel (UTC), Benutzeridentität, Quell-IP-Adresse, versuchte Aktion, betroffene Ressource und Erfolgs- oder Fehlerstatus.
- Keine sensiblen Daten protokollieren: Passwörter, Session-Tokens, Personendaten, Kreditkartennummern oder Verschlüsselungsschlüssel.
- Ein zentrales Protokollierungsframework verwenden. Keine individuellen Protokollierungsmechanismen schreiben, die die Protokollierungsinfrastruktur der Organisation umgehen.
- Sicherstellen, dass Protokolleinträge, die nicht vertrauenswürdige Daten enthalten, in der Protokollansicht nicht als Code ausgeführt werden können (Prävention von Log-Injection).

### Kryptographische Praktiken

Anwendungscode, der Kryptographie implementiert oder nutzt, soll der kryptographischen Richtlinie der Organisation folgen.

**Anforderungen**:

- Von der Plattform bereitgestellte oder genehmigte Drittanbieter-Kryptobibliotheken verwenden. Keine individuellen kryptographischen Algorithmen implementieren.
- Aktuelle, genehmigte Algorithmen verwenden: AES-256 für symmetrische Verschlüsselung, RSA-2048+ oder ECDSA P-256+ für asymmetrische Operationen, SHA-256+ für Hashing. MD5 und SHA-1 sind für Sicherheitszwecke verboten.
- Mindestens TLS 1.2 (TLS 1.3 bevorzugt) für alle Daten bei der Übertragung. SSL, TLS 1.0 und TLS 1.1 sind verboten.
- Kryptographische Schlüssel mit kryptographisch sicheren Zufallsgeneratoren generieren. Keine vorhersehbaren Seeds verwenden.
- Keine kryptographischen Schlüssel, API-Schlüssel oder Geheimnisse im Quellcode hart kodieren. Die genehmigte Secrets-Management-Lösung der Organisation verwenden.
- Vollständige kryptographische Anforderungen in ISMS-OP-POL-A.8.24 (Einsatz von Kryptographie) einsehen.

### Zugriffssteuerung im Code

Anwendungscode soll Autorisierung konsistent durchsetzen.

**Anforderungen**:

- Zugriffssteuerung für jede Anfrage serverseitig durchsetzen. Nicht ausschliesslich auf das Ausblenden von UI-Elementen vertrauen.
- Standard-Deny anwenden: wenn das Berechtigungsniveau eines Benutzers nicht ermittelt werden kann, Zugriff verweigern.
- Prinzip der minimalen Rechtevergabe im Code anwenden: minimale Berechtigungen für jede Funktion gewähren.
- Autorisierung für jeden API-Endpunkt validieren, einschliesslich indirekter Objektreferenzen.
- Client-seitig bereitgestellte Rollen- oder Berechtigungsansprüche nicht ohne serverseitige Verifizierung vertrauen.

---

## Abhängigkeits- und Bibliotheksverwaltung

Drittanbieterbibliotheken, Frameworks und Open-Source-Komponenten bringen Supply-Chain-Risiken mit sich und sollen über ihren gesamten Lebenszyklus verwaltet werden.

**Anforderungen**:

- Ein Abhängigkeitsinventar für jede Anwendung pflegen. Alle Produktionsanwendungen sollen eine Software Bill of Materials (SBOM) im CycloneDX- oder SPDX-Format pflegen, die automatisch über die Build-Pipeline generiert wird.
- Software Composition Analysis (SCA)-Tools ([SCA-Tool] — z. B. Dependabot, Snyk, OWASP Dependency-Check oder gleichwertig) einsetzen, um Abhängigkeiten auf bekannte Schwachstellen zu scannen.
- SCA-Scans sollen bei jedem Build ausgeführt werden (CI/CD-Pipeline-Integration). Builds sollen fehlschlagen, wenn kritische oder hochgradige Schwachstellen in Abhängigkeiten erkannt und unbehoben sind.
- Abhängigkeitsversionen in Lock-Dateien pinnen. Keine variablen Versionsbereiche (z. B. `*` oder `>=`) für Produktionsabhängigkeiten verwenden.
- Neue Abhängigkeiten vor der Übernahme bewerten: Pflegestatus, bekannte Schwachstellen, Lizenzkompatibilität und Community-Aktivität prüfen. Aufgegebene oder nicht gepflegte Bibliotheken sollen nicht eingeführt werden.
- Ungenutzte Abhängigkeiten entfernen. Mindestens jährlich ein Abhängigkeitsaudit durchführen, um Bibliotheken, die nicht mehr verwendet werden, zu identifizieren und zu entfernen.

**Anforderungen an die Software Bill of Materials (SBOM)**:

SBOM-Generierung soll für alle Anwendungen zur Standardpraxis werden, nicht nur für Hochrisikoanwendungen.

- **Format**: CycloneDX oder SPDX (JSON oder XML).
- **Generierung**: Automatisiert über Build-Pipeline (jeder Build generiert eine aktualisierte SBOM). Tools: [SBOM-Tool — z. B. syft, cdxgen, cyclonedx-maven-plugin oder sprachspezifisches Äquivalent].
- **Inhalt**: Alle direkten und transitiven Abhängigkeiten, Versionen, Lizenzen, Lieferanten, bekannte Schwachstellen.
- **Abdeckung**: Produktionsanwendungen — SBOM erforderlich (100 % Abdeckung). Interne Tools — SBOM erforderlich. Proof-of-Concepts / Experimente — SBOM empfohlen (wenn Code >30 Tage bestehen bleibt).
- **Speicherung und Zugriff**: SBOMs werden in [Artefakt-Repository / Dependency Track / SBOM-Plattform] gespeichert, zugänglich für das Entwicklungsteam, das Sicherheitsteam, Legal (für Lizenzkonformität) und das Incident-Response-Team. Jede SBOM soll mit der entsprechenden Anwendungsversion markiert sein (1:1-Beziehung).
- **Verwendung**: Schwachstellenmanagement (SCA-Tool nimmt SBOM auf, gleicht gegen CVE-Datenbanken ab, identifiziert betroffene Anwendungen); Lizenzkonformität (Rechtsteam prüft SBOM auf Lizenzkonflikte); Incident Response (wenn neue Schwachstelle bekannt wird, SBOM-Repository innerhalb von Stunden auf betroffene Anwendungen abfragen); Supply-Chain-Transparenz (Drittanbieter-Audit oder Kunden-Due-Diligence-Anfragen).
- **Genauigkeitsvalidierung**: Vierteljährliches Audit — 10 % der Anwendungen stichprobenartig prüfen, SBOM mit tatsächlichen bereitgestellten Abhängigkeiten vergleichen (binäre Analyse). Wenn SBOM nicht mit der Realität übereinstimmt, Ursache untersuchen (Build-Prozessfehler, manuelle Abhängigkeitsinstallation).
- **Ausnahmen**: Legacy-Anwendungen ohne Build-Pipeline — manuelle vierteljährliche SBOM-Generierung (Übergang bis zur Migration oder Ausserbetriebnahme der Legacy-Anwendung). COTS-Software von Drittanbietern — SBOM vom Anbieter anfordern (wenn Anbieter keine bereitstellt, Lücke im Risikoregister dokumentieren).
- **Zeitplan**: Alle Produktionsanwendungen sollen bis [Datum — 6 Monate nach Richtlinien-Inkrafttreten empfohlen] SBOMs generieren. Schrittweiser Rollout: kritische Anwendungen zuerst (Monat 1–3), dann alle Produktionsanwendungen (Monat 4–6).

**Verwaltung von Abhängigkeitsversionen (Pinning und Aktualisierung)**:

Das Pinnen von Abhängigkeitsversionen gewährleistet reproduzierbare Builds, schafft aber ein Veralterungsrisiko, wenn Versionen nie aktualisiert werden. Die Organisation soll einen Aktualisierungsrhythmus für Abhängigkeiten pflegen, um Stabilität mit Sicherheit in Einklang zu bringen.

- **Lock-Dateien**: Erforderlich (package-lock.json, Gemfile.lock, poetry.lock, go.sum usw.).
- **Variable Bereiche**: Verboten für Produktion (`*`, `>=`, `^` nur in Nicht-Produktion erlaubt).
- **Exakte Versionen**: Im Lock-File gepinnt (z. B. `lodash@4.17.21` statt `lodash@^4.0.0`).

**Abhängigkeitsaktualisierungsrhythmus**:

| Aktualisierungstyp | Häufigkeit | Auslöser | Prüfumfang |
|-------------------|-----------|---------|-----------|
| **Sicherheits-Patches** (Schwachstellenbehebungen) | Sofort | SCA-Alarm (kritischer/hoher CVE) | Zielgerichtet (nur betroffene Abhängigkeit) |
| **Kleine Updates** (rückwärtskompatibel) | Monatlich | Geplantes Wartungsfenster | Batch-Update (mehrere Abhängigkeiten gleichzeitig) |
| **Grosse Updates** (breaking changes) | Vierteljährlich oder pro Abhängigkeit | Geplante Wartung oder geplante Feature-Arbeit | Individuelle Bewertung pro Abhängigkeit |

**Aktualisierungsverfahren**:
1. **Updates identifizieren**: SCA-Tool markiert veraltete Abhängigkeiten oder Dependabot/Renovate generiert PR.
2. **Changelog prüfen**: Release Notes auf breaking changes, Sicherheitsfixes, neue Features prüfen.
3. **Aktualisieren und testen**: Lock-Datei aktualisieren, vollständige Testsuite ausführen (Unit, Integration, E2E).
4. **Sicherheitsscan**: SAST und SCA auf aktualisierte Abhängigkeiten ausführen.
5. **Deployment**: Änderungsmanagementprozess folgen (Staging, dann Produktion).
6. **Überwachen**: Post-Deployment-Überwachung auf Regressionen (Fehlerquoten, Leistung).

**Automatisierte Abhängigkeitsupdates** (empfohlen):
- Tool: Dependabot, Renovate oder gleichwertig.
- Konfiguration: Automatisch PRs für Sicherheits-Patches erstellen (Auto-Merge wenn Tests bestehen), manuelle Prüfung für kleine/grosse Updates.
- Prüfungs-SLA: Sicherheits-Patches innerhalb von 2 Werktagen geprüft, kleine Updates innerhalb von 1 Woche.

**Veraltungsgrenzen für Abhängigkeiten**:
- Kritische Abhängigkeiten (Authentifizierung, Kryptographie, Web-Frameworks): Keine Version älter als 12 Monate.
- Standard-Abhängigkeiten: Keine Version älter als 24 Monate.
- Ausnahme: Wenn eine neuere Version bekannte Probleme hat, dokumentieren, warum die ältere Version beibehalten wird (mit kompensierenden Massnahmen — verstärkte Überwachung).

**Metriken zur Abhängigkeitsverwaltung**:
- Durchschnittliches Abhängigkeitsalter (Tage seit Versionsveröffentlichung).
- Prozentsatz der Abhängigkeiten mit bekannten Schwachstellen.
- Abhängigkeitsaktualisierungsfrequenz (Aktualisierungen pro Monat).
- Zeit von der CVE-Offenlegung bis zum Patch-Deployment.
- Ziel: Durchschnittliches Abhängigkeitsalter <180 Tage; <1 % der Abhängigkeiten mit bekannten kritischen/hohen CVEs.

**Behebungs-SLAs für Abhängigkeitsschwachstellen**:

| Schweregrad | CVSS-Score | Behebungs-SLA |
|-------------|-----------|---------------|
| Kritisch | 9,0–10,0 | 7 Tage |
| Hoch | 7,0–8,9 | 30 Tage |
| Mittel | 4,0–6,9 | 90 Tage |
| Niedrig | 0,1–3,9 | Nächste geplante Version |

---

## Code-Review-Anforderungen

Alle Codeänderungen sollen vor dem Merge in geschützte Branches überprüft werden.

**Review-Typen**:

| Review-Typ | Wann erforderlich | Prüfer |
|------------|------------------|--------|
| Peer-Code-Review | Alle Codeänderungen | Mindestens ein Entwickler ausser dem Autor |
| Sicherheitsorientiertes Code-Review | Änderungen an Authentifizierungs-, Autorisierungs-, Kryptographie-, Eingabevalidierungs-, Session-Verwaltungs- oder Datenschutzcode | Entwickler mit Sicherheitsschulung oder Security Champion |
| Automatisiertes Code-Review | Alle Codeänderungen | [SAST-Tool] in CI/CD-Pipeline integriert |

**Risikobasierte Code-Review-Anforderungen**:

Die Anzahl der Prüfer und ihre Qualifikationen sollen durch die Risikoklassifizierung der Codeänderung bestimmt werden:

**Standard-Code** (nicht sicherheitskritisch):
- Prüfer: Mindestens 1 Peer-Entwickler (nicht der Autor).
- Qualifikationen: Jeder Entwickler im Team mit >3 Monaten Erfahrung.
- Genehmigung: 1 Genehmigung für Merge erforderlich.

**Sicherheitskritischer Code** (Authentifizierung, Autorisierung, Session-Management, Eingabevalidierung, Kryptographie, Datenschutz):
- Prüfer: Mindestens 2 Prüfer: (1) Peer-Entwickler (jeder im Team), UND (2) Security Champion ODER Mitglied des Sicherheitsteams (obligatorisch).
- Qualifikationen: Security Champion soll Security-Champion-Schulung absolviert haben.
- Genehmigung: Beide Prüfer sollen vor dem Merge genehmigen.

**Infrastruktur-/Deployment-Code** (IaC, CI/CD-Pipeline-Änderungen, Konfigurationsmanagement):
- Prüfer: Mindestens 1 Peer + DevOps-Lead-Genehmigung.
- Qualifikationen: Prüfer soll Infrastrukturimplikationen verstehen.
- Genehmigung: 2 Genehmigungen erforderlich.

**Hochrisikoänderungen** (extern zugängliche APIs, Zahlungsverarbeitung, Admin-Funktionen):
- Prüfer: 2 Peers + Mitglied des Sicherheitsteams (3 insgesamt).
- Tests: Muss automatisierte Sicherheitstests umfassen (SAST bestanden, Integrationstests bestanden).
- Genehmigung: Alle 3 Prüfer genehmigen + automatisierte Tests bestanden.

**Zwei-Personen-Integrität** (Secrets-Rotationsskripte, Privilegieneskalations-Code, Umgehung von Sicherheitsmassnahmen):
- Prüfer: 2 Senior-Entwickler ODER 1 Senior + Mitglied des Sicherheitsteams.
- Genehmigung: Beide genehmigen + ISB benachrichtigt (Bewusstsein, keine Genehmigung erforderlich, es sei denn Produktionsänderung).

**Verfügbarkeit von Security Champions**:
- Mindestens 1 Security Champion pro Entwicklungsteam (Verhältnis 1:8 Entwickler).
- Security Champions sollen dedizierte Zeit für Sicherheitsreviews haben (10 % der Arbeitszeit).
- Wenn Security Champion nicht verfügbar: Sicherheitsteam soll innerhalb von 48 Stunden eine Prüfung bereitstellen.

Dokumentation: PR-Beschreibung soll den erforderlichen Review-Typ basierend auf der Code-Klassifizierung angeben (Standard, sicherheitskritisch, Hochrisiko). CI/CD-Prüfungen sollen verifizieren, dass die Genehmigungsanzahl den Anforderungen entspricht.

**Peer-Code-Review-Anforderungen**:

- Der Code-Autor soll seinen eigenen Code nicht genehmigen (Funktionstrennung).
- Prüfer sollen die Einhaltung der Standards für sicheres Coding der Organisation verifizieren.
- Prüfer sollen prüfen auf: hart kodierte Geheimnisse, unsichere Coding-Muster, fehlende Eingabevalidierung, fehlende Ausgabekodierung, übermässige Berechtigungen, unzureichende Fehlerbehandlung und fehlende Protokollierung.
- Pull Requests sollen eine Beschreibung der Änderungen, einen Link zum zugehörigen Issue oder Ticket und Testnachweise enthalten.
- Reviews sollen abgeschlossen werden, bevor der Code in einen geschützten Branch gemergt wird.

**Checkliste für sicherheitsorientiertes Code-Review**:

- [ ] Eingabevalidierung auf alle externen Eingaben angewendet
- [ ] Ausgabekodierung an Rendering-Punkten angewendet
- [ ] Keine hart kodierten Geheimnisse, Schlüssel oder Anmeldedaten
- [ ] Parametrisierte Abfragen für Datenbankinteraktionen verwendet
- [ ] Authentifizierung und Session-Verwaltung verwenden genehmigte Bibliotheken
- [ ] Fehlermeldungen geben keine internen Details preis
- [ ] Sicherheitsrelevante Ereignisse werden protokolliert
- [ ] Sensible Daten werden nicht protokolliert
- [ ] Kryptographische Operationen verwenden genehmigte Algorithmen und Bibliotheken
- [ ] Zugriffskontrollprüfungen sind serverseitig und pro Anfrage angewendet
- [ ] Abhängigkeiten sind gepinnt und frei von bekannten kritischen Schwachstellen

---

## Static Application Security Testing (SAST)

Automatisierte statische Analyse soll in den Entwicklungsworkflow integriert werden, um Sicherheitsmängel vor dem Deployment zu erkennen.

**Anforderungen**:

- Die Organisation soll ein SAST-Tool ([SAST-Tool] — z. B. SonarQube, Semgrep, CodeQL, Checkmarx oder gleichwertig) in die CI/CD-Pipeline integriert einsetzen.
- SAST-Scans sollen bei jedem Pull Request oder Merge Request in einen geschützten Branch ausgeführt werden.
- SAST-Ergebnisse sollen vor dem Merge überprüft werden. Kritische und hochgradige Befunde sollen den Merge blockieren, bis sie behoben oder explizit als False Positives mit dokumentierter Begründung akzeptiert werden.
- SAST-Regelwerke sollen mindestens die OWASP-Top-10 und CWE/SANS-Top-25-Schwachstellenklassen abdecken.
- False Positives sollen nach dem folgenden Unterdrückungsverfahren dokumentiert und unterdrückt werden. Unterdrückung ohne Begründung und Peer-Review ist verboten.
- SAST-Tool-Konfiguration und Regelwerke sollen jährlich vom Entwicklungsleiter und dem Sicherheitsteam überprüft werden.

**SAST-False-Positive-Unterdrückungsverfahren**:

Die Unterdrückung eines SAST-Befunds als False Positive ohne Peer-Review ist verboten. Entwickler können versehentlich echte Schwachstellen unterdrücken.

**Unterdrückungsantragsprozess**:
1. Entwickler identifiziert SAST-Befund, der für ein False Positive gehalten wird.
2. Entwickler dokumentiert im Unterdrückungsantrag: Befund-ID, warum der Befund ein False Positive ist (technische Begründung), Code-Snippet, das zeigt, warum die Regel nicht zutrifft, und vorgeschlagene Unterdrückungsmethode (Inline-Kommentar, Konfigurationsdatei).
3. **Peer-Review erforderlich**: Ein anderer Entwickler ODER ein Security Champion soll den Unterdrückungsantrag prüfen.
4. **Genehmigung des Sicherheitsteams** (für kritische/hohe Befunde): Das Sicherheitsteam soll die Unterdrückung kritischer/hoher Schweregradbefunde genehmigen. Mittel/Niedrig-Befunde können von einem Peer-Prüfer genehmigt werden.
5. Unterdrückung angewendet: Inline-Kommentar + Tool-Konfigurationsaktualisierung (doppelte Dokumentation).

**Vorlage für Unterdrückungsbegründung** (Inline-Kommentar):
```
// SAST-SUPPRESS: [Tool Name] [Rule ID] - [Date]
// Reason: [Brief explanation why this is a false positive]
// Reviewed by: [Reviewer Name]
// Approved by: [Security Team Member] (if Critical/High)
```

**Unterdrückungsaudit**:
- Vierteljährliche Überprüfung: Sicherheitsteam soll 20 % der unterdrückten Befunde stichprobenartig prüfen.
- Neuvalidierung: Sind Unterdrückungen noch gültig? (Code geändert, Regel aktualisiert, neuer Kontext?)
- Widerruf: Wenn Unterdrückung nicht mehr gerechtfertigt, Unterdrückung aufheben und Befund beheben.

**Verfolgte Unterdrückungsmetriken**:
- Gesamtzahl aktiver Unterdrückungen nach Schweregrad.
- Unterdrückungsrate (Prozentsatz der unterdrückten SAST-Befunde gegenüber behobenen).
- Durchschnittliches Alter der Unterdrückungen (alte Unterdrückungen auf weiterhin gültige Aktualität prüfen).
- Widerrufene Unterdrückungen (wie viele Unterdrückungen sich später als falsch herausgestellt haben).

**Warnsignale** (lösen Sicherheitsteam-Prüfung aus):
- Entwickler unterdrückt >5 Befunde in einem einzelnen PR (ungewöhnlich — deutet auf Missbrauch hin).
- Team unterdrückt >20 % der kritischen/hohen Befunde (deutet auf Bedarf an Regelabstimmung hin oder dass das Team das Tool nicht versteht).
- Unterdrückung ohne ausreichende Begründung (generisches «nicht anwendbar» — unzureichend).

Ziel: <5 % der SAST-Befunde unterdrückt (95 %+ behoben oder als bestätigte False Positives mit dokumentierter Begründung).

**SAST-Abdeckungsanforderungen**:

| Anwendungsklassifizierung | Scanfrequenz | Befundprüfung |
|--------------------------|--------------|---------------|
| Produktionsanwendungen | Pro Commit / Pull Request | Vor Merge |
| Interne Tools | Pro Commit / Pull Request | Vor Merge |
| Proof of Concepts | Wöchentlich (wenn in organisatorischen Repositories gespeichert) | Wöchentliche Triage |

---

## Schulung für sicheres Coding

Entwickler sollen eine Schulung erhalten, um sicheren Code effektiv schreiben zu können.

**Schulungsanforderungen**:

| Schulungsart | Zielgruppe | Häufigkeit | Mindestdauer |
|--------------|-----------|-----------|--------------|
| Grundlagen des sicheren Codings | Alle Entwickler (einschliesslich Auftragnehmer) | Vor dem Schreiben von Produktionscode | 4 Stunden |
| Jährliche Auffrischung | Alle Entwickler | Jährlich | 2 Stunden |
| Security-Champion-Schulung | Designierte Security Champions | Initial + jährlich | 8 Stunden initial; 4 Stunden Auffrischung |
| Sprachspezifisches sicheres Coding | Entwickler, die eine neue Sprache übernehmen | Vor der Produktionsnutzung der Sprache | 2 Stunden |

**Schulungsinhalte** sollen mindestens abdecken:

- OWASP-Top-10 und CWE/SANS-Top-25-Schwachstellenklassen.
- Standards für sicheres Coding, die für die primäre Sprache des Entwicklers anwendbar sind.
- Eingabevalidierung, Ausgabekodierung und Injection-Prävention.
- Authentifizierung, Session-Management und Zugriffskontrollmuster.
- Secrets-Management und das Verbot hart kodierter Anmeldedaten.
- Sicherer Einsatz von Kryptobibliotheken.
- Abhängigkeitsverwaltung und Supply-Chain-Sicherheit.
- Verwendung der SAST- und SCA-Tools der Organisation.

**Schulungsnachweise**: Abschlussunterlagen sollen in [HR-System / LMS] gepflegt und vierteljährlich vom Entwicklungsleiter überprüft werden.

**Durchsetzung der Schulungsanforderungen für sicheres Coding**:

Schulungsanforderungen sollen durch eskalierte Konsequenzen bei Nichteinhaltung durchgesetzt werden:

**Abschlussanforderungen** (gemäss Schulungsanforderungstabelle):
- Grundlagen des sicheren Codings: Vor dem Schreiben von Produktionscode (neue Mitarbeitende, Auftragnehmer).
- Jährliche Auffrischung: Innerhalb von 30 Tagen nach dem Jahrestag (alle Entwickler).
- Sprachspezifisch: Vor der Produktionsnutzung einer neuen Sprache.
- Security-Champion-Schulung: Innerhalb von 30 Tagen nach der Ernennung.

**Konsequenzen bei Nichteinhaltung** (eskalierend):

| Tage überfällig | Massnahme | Behörde |
|-----------------|---------|---------|
| **0–14 Tage** | Erinnerungs-E-Mail (automatisch) | System |
| **15–30 Tage** | Manager-Benachrichtigung + zweite Erinnerung | Entwicklungsleiter |
| **31–60 Tage** | Produktions-Deployment-Genehmigung blockiert (Entwickler kann keine PRs in Produktionsbranches genehmigen) | Entwicklungsleiter |
| **61–90 Tage** | Code-Review-Privilegien gesperrt (Entwickler kann den Code anderer nicht überprüfen) | Entwicklungsleiter + ISB |
| **>90 Tage** | Zugriff auf Produktionssysteme gesperrt (kein Deployment, kein Zugriff auf Produktionsumgebungen) | ISB |

**Vorübergehende Ausnahmen**:
- Langzeiturlaub (Eltern-, Krankenurlaub): Schulungsfälligkeitsdatum auf 30 Tage nach Rückkehr verlängert.
- Dringender Geschäftsbedarf (kritischer Incident, Kundennotfall): ISB gewährt 30-tägige Verlängerung mit dokumentierter Begründung.

**Verifizierung des Schulungsabschlusses**:
- Automatisiert: LMS/HR-System sendet Abschlussstatus an [Deployment-Tool] oder [Code-Review-Plattform].
- Vor-Deployment-Prüfung: CI/CD-Pipeline prüft Schulungsstatus vor Genehmigung des Produktions-Deployments (wenn nicht konformer Entwickler, Deployment blockiert mit Grund «Schulung überfällig — [Schulungsname] abschliessen»).

**Metriken zur Schulungsdurchsetzung**:
- Prozentsatz der Entwickler mit aktueller Schulung (Ziel: 95 %+ innerhalb von 30 Tagen nach Fälligkeitsdatum).
- Durchschnittliche Schulungsabschlusszeit (Tage vom Fälligkeitsdatum bis zum Abschluss).
- Anzahl der Entwickler mit gesperrten Privilegien (Ziel: 0).

**Kommunikation**:
- 30 Tage vor Fälligkeit: «Schulung bald fällig»-Erinnerung.
- 7 Tage vor Fälligkeit: «Schulung diese Woche fällig»-Erinnerung.
- Am Fälligkeitsdatum: «Schulung überfällig»-Benachrichtigung an Entwickler + Manager.
- Automatisierte Erinnerungen: Wöchentlich bis Schulung abgeschlossen.

Durchsetzung aktiv ab [Datum — 3 Monate nach Richtlinien-Inkrafttreten empfohlen, um bestehenden Entwicklern Zeit zu geben].

---

## Verbotene Coding-Praktiken

Die folgenden Coding-Praktiken sind verboten:

| Verbotene Praxis | Begründung | Erforderliche Alternative |
|-----------------|-----------|--------------------------|
| Hart kodierte Passwörter, API-Schlüssel oder Geheimnisse im Quellcode | Geheimnisse durch Repository-Zugriff oder Code-Lecks exponiert | Umgebungsvariablen oder genehmigten Secrets-Manager ([Secrets Manager]) verwenden |
| SQL-Statement-Konstruktion durch String-Konkatenation mit Benutzereingaben | SQL-Injection-Schwachstelle | Parametrisierte Abfragen oder Prepared Statements verwenden |
| Deserialisierung nicht vertrauenswürdiger Daten ohne Validierung | Remote-Code-Execution-Risiko | Validieren und bereinigen vor der Deserialisierung; sichere Deserialisierungsbibliotheken verwenden |
| Verwendung veralteter oder unsicherer kryptographischer Algorithmen (MD5, SHA-1, DES, RC4) | Bekannte Schwächen; Brute-Force- oder Kollisionsangriffe | Genehmigte Algorithmen gemäss kryptographischer Richtlinie verwenden |
| Deaktivierte oder umgangene TLS-Zertifikatsvalidierung | Man-in-the-Middle-Angriffs-Exposition | Zertifikatsvalidierung in allen Umgebungen ausser isoliertem Test durchsetzen |
| Ungepüfte Code-Beispiele aus öffentlichen Quellen kopiert | Können Schwachstellen, Backdoors oder Lizenzverletzungen enthalten | Prüfen und anpassen; Lizenzkompatibilität verifizieren; mit SAST scannen |
| Protokollierung sensibler Daten (Passwörter, Tokens, Personendaten) | Datenexposition durch Protokolldateien | Datenmaskierung verwenden oder sensible Felder von der Protokollierung ausschliessen |
| Verwendung von `eval()` oder gleichwertige dynamische Code-Ausführung mit Benutzereingaben | Code-Injection-Schwachstelle | Sichere Alternativen verwenden; Eingaben validieren und bereinigen |

### Erkennung hart kodierter Geheimnisse (verbindliche Tools)

Das Verbot hart kodierter Geheimnisse in der obigen Tabelle soll durch automatisierte Erkennung auf mehreren Ebenen durchgesetzt werden.

**Pre-Commit-Scanning** (empfohlen, Entwickler-Workstation):
- Tool: [git-secrets / Talisman / detect-secrets] auf Entwicklermaschinen installiert.
- Scannt Commits auf Regex-Muster (API-Schlüssel, private Schlüssel, Passwörter, Tokens).
- Blockiert Commit wenn Geheimnisse erkannt (Entwickler muss vor erneuter Übertragung entfernen).
- Onboarding: Alle Entwickler sollen während des Onboardings angewiesen werden, den Pre-Commit-Hook zu installieren.

**CI/CD-Pipeline-Scanning** (obligatorisch, Durchsetzungsebene):
- Tool: [GitGuardian / TruffleHog / Gitleaks] in CI/CD-Pipeline integriert.
- Scannt jeden Commit/PR auf Geheimnis-Muster.
- Builds sollen fehlschlagen, wenn Geheimnisse erkannt werden (kein Merge bis beheben).
- Alarm: Sicherheitsteam sofort über erkannte Geheimnisse benachrichtigt (kritischer Schweregrad).

**Repository-Scanning** (regelmässig, historische Erkennung):
- Tool: GitHub Advanced Security / GitLab Secret Detection / dedizierter Scanner.
- Scannt gesamte Repository-Historie (nicht nur neue Commits — erfasst historische Geheimnisse).
- Häufigkeit: Wöchentlicher vollständiger Repository-Scan.
- Behebung: Im Verlauf gefundene Geheimnisse erfordern: Entfernung aus dem Verlauf (git filter-repo), Rotation des kompromittierten Geheimnisses (als kompromittiert annehmen) und Dokumentation des Incidents im Geheimnisbruch-Protokoll.

**Mindestens erkannte Geheimnis-Muster**:
- AWS-Schlüssel (AKIA..., AWS Secret Access Key-Muster).
- API-Schlüssel (generische API-Key-Muster, anbieterspezifische Formate).
- Private Schlüssel (RSA-, SSH-, PGP-Key-Header).
- Datenbankpasswörter (Verbindungsstrings mit eingebetteten Anmeldedaten).
- OAuth-Tokens, JWT-Geheimnisse, Verschlüsselungsschlüssel.

**Verfahren zur Geheimnis-Behebung**:
1. **Sofort**: Entwickler entfernt Geheimnis aus Code, committed Fix.
2. **Innerhalb von 1 Stunde**: Geheimnis rotiert (als kompromittiert annehmen, auch wenn nur in Entwicklungs-Branch).
3. **Innerhalb von 24 Stunden**: Repository-Verlauf bereinigt (wenn Geheimnis committed wurde — git filter-repo oder BFG Repo-Cleaner verwenden).
4. **Innerhalb von 48 Stunden**: Incident-Bericht beim ISB eingereicht (wie Geheimnis committed wurde, Auswirkungsbeurteilung, präventive Massnahmen).

**Ausnahmen** (selten):
- Test-Fixtures mit Dummy-Geheimnissen (klar als unecht und nicht funktional markiert).
- Code-Beispiele in der Dokumentation (klar als Beispiele markiert, Platzhalterwerte wie `your-api-key-here` verwenden).

Dokumentation: Konfiguration des Geheimniserkennungstools soll in [CI/CD-Config-Repository] gepflegt und vierteljährlich vom Sicherheitsteam überprüft werden.

---

## Ausgelagerte Entwicklung

Von externen Auftragnehmern und ausgelagerten Entwicklungsteams produzierter Code soll denselben Standards für sicheres Coding wie intern entwickelter Code entsprechen.

**Vertragliche Anforderungen**:

- Verträge sollen die Einhaltung der Standards für sicheres Coding der Organisation und dieser Richtlinie erfordern.
- Auftragnehmer sollen Nachweise über Schulungen für sicheres Coding für ihre Entwickler vorlegen.
- Sämtlicher von Auftragnehmern produzierter Code soll dem gleichen Code-Review und SAST-Scanning unterzogen werden wie interner Code.
- Auftragnehmer sollen Sicherheitsbefunde innerhalb der definierten SLAs der Organisation beheben.
- Die Organisation behält das Recht, die Praktiken für sicheres Coding der Auftragnehmer zu auditieren.

**Verifizierung**:

- Auftragnehmer-Code soll vor dem Merge von einem internen Entwickler geprüft werden.
- SAST- und SCA-Ergebnisse für von Auftragnehmern produzierten Code sollen für das Sicherheitsteam der Organisation sichtbar sein.
- Hochrisikocode, der von Auftragnehmern produziert wird (Authentifizierung, Autorisierung, Kryptographie, Datenschutz), soll ein sicherheitsorientiertes Code-Review durch einen Security Champion oder Sicherheitsarchitekten erhalten.

**Qualitätssicherung für ausgelagerte Entwicklung**:

Zusätzlich zu laufendem Code-Review und Scanning soll die Organisation periodische Audits des von Auftragnehmern produzierten Codes durchführen, um nachhaltige Qualität und Konformität zu verifizieren.

**Vierteljährliches Auftragnehmer-Audit** (pro aktivem Auftragnehmer-Engagement):
- Stichprobengrösse: 10 % des vom Auftragnehmer produzierten Codes (mindestens 5 PRs/MRs) aus dem vorangegangenen Quartal.
- Audit-Umfang:
  - Sicherheitskonformität: Folgt Code den Standards für sicheres Coding? (Eingabevalidierung, Ausgabekodierung, keine hart kodierten Geheimnisse usw.)
  - Code-Qualität: Lesbarkeit, Wartbarkeit, Testabdeckung.
  - Dokumentation: Sind Code-Kommentare ausreichend? Architekturentscheidungen dokumentiert?
- Auditor: Interner Senior-Entwickler ODER Mitglied des Sicherheitsteams (nicht dieselbe Person, die das ursprüngliche Review durchgeführt hat — unabhängige Prüfung).
- Befunde: Im Auftragnehmer-Auditbericht mit Schweregrad (Kritisch/Hoch/Mittel/Niedrig) dokumentiert.

**Behandlung von Auditbefunden**:
- Kritisch/Hoch: Sofort an Auftragnehmer-Management eskalieren, innerhalb von 14 Tagen beheben, Vertragsüberprüfung erwägen wenn Muster entsteht.
- Mittel/Niedrig: Feedback an Auftragnehmer, im nächsten Sprint/Release beheben.

**Auftragnehmer-Leistungsbewertung**:
- Metriken: SAST/SCA-Befundsrate (Befunde pro KLOC), Code-Review-Ablehnungsrate, Audit-Befundsrate, Sicherheitsincident-Rate (durch Auftragnehmer-Code verursachte Incidents).
- Vierteljährlicher Scorecard: Mit Auftragnehmer-Management geteilt.
- Schlechte Leistung: 3 aufeinanderfolgende Quartale unter Schwellenwert soll Vertragsüberprüfung und mögliche Kündigung auslösen.

**Jährliche Auftragnehmer-Sicherheitsbewertung** (umfassend):
- Umfang: Sicheren Entwicklungsprozess, Schulungsprogramm, Tooling und Codequalität des vergangenen Jahres des Auftragnehmers überprüfen.
- Methode: Fragebogen + Interview + vertiefte Prüfung von Code-Beispielen.
- Ausgabe: Auftragnehmer-Sicherheitsbewertungsbericht mit Empfehlungen.
- Massnahme: Auftragnehmer sollen kritische/hohe Empfehlungen innerhalb von 90 Tagen adressieren.

Dokumentation: Auftragnehmer-Auditberichte sollen für Vertragsdauer + 3 Jahre aufbewahrt werden.

---

## Security-Champion-Programmrahmen

Security Champions sind entscheidend für die Verankerung von Sicherheit in Entwicklungsteams. Der folgende Rahmen formalisiert die Security-Champion-Rolle mit klarer Rechenschaftspflicht, Zeitallokation und Unterstützung.

**Auswahl und Ernennung**:
- Verhältnis: 1 Security Champion pro Entwicklungsteam (oder pro 8 Entwickler bei grösseren Teams).
- Auswahl: Freiwillige bevorzugt, vom Entwicklungsleiter ernannt wenn kein Freiwilliger.
- Qualifikationen: Mittlerer oder Senior-Entwickler, Interesse an Sicherheit, guter Kommunikator.
- Amtszeit: 12-monatige Amtszeit (verlängerbar), mit 6-monatigem Mentoring für neue Champions.

**Verantwortlichkeiten** (formal, in der Rollenbeschreibung dokumentiert):
- Sicherheitsorientierte Code-Reviews (sämtlicher sicherheitskritischer Code im Team).
- Mentoring für sicheres Coding (Teammitglieder bei Sicherheitsproblemen unterstützen).
- SAST/SCA-Triage (Erstlinienbewertung von Scan-Befunden, Eskalation an Sicherheitsteam wenn nötig).
- Teilnahme an Bedrohungsmodellierung (für neue Features/wesentliche Änderungen).
- Sicherheitsteam-Liaison (monatlichen Security-Champion-Meetings beiwohnen, Sicherheitsupdates an Team weitergeben).
- Incident-Unterstützung für Sicherheit (Sicherheitsteam bei Incidents, die den Code des Teams betreffen, unterstützen).

**Zeitallokation**:
- 10 % der Arbeitszeit für Security-Champion-Aufgaben (~4 Stunden/Woche).
- Code-Review-Zeit auf 10%-Allokation angerechnet.
- Vom Entwicklungsleiter verwaltet (sicherstellen, dass Champion Zeit hat und nicht mit Feature-Arbeit überlastet ist).

**Schulung und Entwicklung**:
- Erstschulung: 8 Stunden (Bedrohungsmodellierung, sicheres Code-Review, OWASP Top 10 vertieft, SAST/SCA-Tools).
- Jährliche Auffrischung: 4 Stunden (neue Schwachstellen, Tool-Updates, Fallstudien).
- Optional: Konferenzbesuche (OWASP AppSec, sicherheitsfokussierte Konferenzen), Online-Kurse.

**Unterstützung und Ressourcen**:
- Monatliches Security-Champion-Community-Meeting (Peer-Learning, Fallstudien, Q&A mit Sicherheitsteam).
- Dedizierter Kommunikationskanal (asynchrone Unterstützung, Wissensaustausch).
- Zugang zum Sicherheitsteam für Eskalation (innerhalb 24-Stunden-Antwort-SLA).
- Anerkennung: Öffentliche Würdigung (All-Hands, Newsletter), mögliche Bonus-/Beförderungserwägung.

**Leistungsmetriken** (vierteljährlich gemessen):
- Abgeschlossene sicherheitsorientierte Code-Reviews (Ziel: 100 % des sicherheitskritischen Codes).
- Innerhalb SLA triagierte SAST-Befunde (Ziel: 95 % innerhalb von 48 Stunden).
- Sicherheitsincidents mit Beteiligung des Team-Codes (Trend im Laufe der Zeit abnehmend).
- Sicherheitsschulungsabschluss der Teamentwickler (Champion fördert Team-Schulung).

**Nachfolgeplanung**:
- Shadow-Programm: Nachfolger 3 Monate vor Amtszeitende identifizieren, aktuellen Champion shadowing.
- Wissenstransfer: Im Security-Champion-Handbuch dokumentiert.

**Programm-Governance**:
- Programmeigentümer: ISB oder Sicherheitsteam-Lead.
- Vierteljährliche Programmüberprüfung: Metriken, Champion-Feedback, Programmverbesserungen.
- Jährliche Programmreifebewertung: Abdeckung (alle Teams haben Champions?), Engagement (Champions aktiv?), Wirksamkeit (Sicherheitsergebnisse verbessern sich?).

Dokumentation: Security-Champion-Register soll in [HR-System / Wiki] mit Namen, Teams, Ernennungsdaten und Schulungsabschluss gepflegt werden.

---

## Ausnahmenmanagement

Ausnahmen von dieser Richtlinie sollen schriftlich beantragt werden und enthalten:

- Spezifische Anforderung(en), für die eine Ausnahme beantragt wird.
- Geschäftliche Begründung.
- Kompensierende Massnahmen.
- Beantragte Ausnahmedauer (maximal 12 Monate).
- Risikobeurteilung und -akzeptanz.

Ausnahmen sollen vom Entwicklungsleiter und dem Information Security Manager (obligatorisch) genehmigt werden, plus dem ISB für Ausnahmen in Produktionsanwendungen. Alle aktiven Ausnahmen sollen vierteljährlich überprüft werden.

Wenn eine Anforderung technisch nicht erfüllbar ist (z. B. Legacy-Codebasis, die nicht sofort refaktoriert werden kann), sollen kompensierende Massnahmen implementiert, dokumentiert, vom Information Security Manager verifiziert und jährlich überprüft werden.

---

## Begriffsbestimmungen

| Begriff | Definition |
|---------|-----------|
| **CSP** | Content Security Policy — HTTP-Antwort-Header, der einschränkt, welche Ressourcen ein Browser für eine Seite laden darf, und XSS mindert |
| **CWE** | Common Weakness Enumeration — gemeinschaftlich entwickelte Liste von Software- und Hardware-Schwachstellentypen |
| **Abhängigkeit** | Eine Drittanbieterbibliothek, ein Framework oder eine Komponente, die vom Anwendungscode verwendet wird |
| **Injection** | Eine Klasse von Schwachstellen, bei der nicht vertrauenswürdige Daten als Teil eines Befehls oder einer Abfrage an einen Interpreter gesendet werden (z. B. SQL-Injection, XSS, Command Injection) |
| **OWASP** | Open Worldwide Application Security Project — gemeinnützige Stiftung, die Standards, Tools und Leitfäden für Anwendungssicherheit erstellt |
| **Parametrisierte Abfrage** | Eine Datenbankabfragetechnik, die SQL-Logik von benutzerseitig bereitgestellten Daten trennt und SQL-Injection verhindert |
| **SAST** | Static Application Security Testing — automatisierte Analyse von Quellcode zur Identifizierung von Sicherheitsmängeln ohne Ausführung der Anwendung |
| **SBOM** | Software Bill of Materials — maschinenlesbare Inventarliste aller Komponenten, Bibliotheken und Abhängigkeiten in einer Softwareanwendung |
| **SCA** | Software Composition Analysis — automatisiertes Scannen von Drittanbieterabhängigkeiten auf bekannte Schwachstellen und Lizenzrisiken |
| **Security Champion** | Ein Entwickler mit spezialisierter Sicherheitsschulung, der als Sicherheitskontakt innerhalb eines Entwicklungsteams fungiert |
| **TLS** | Transport Layer Security — kryptographisches Protokoll zur Sicherung von Daten bei der Übertragung |
| **XSS** | Cross-Site Scripting — eine Schwachstelle, die es Angreifern ermöglicht, bösartige Skripte in von anderen Benutzern angezeigte Webseiten einzuschleusen |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Ausnahmengenehmigung für Produktionsanwendungen; Aufsicht über die Konformität mit sicherem Coding; jährliche Richtlinienüberprüfung; Berichterstattung an Geschäftsleitung; Governance des Security-Champion-Programms |
| **Entwicklungsleiter** | Pflege der Standards für sicheres Coding (pro Sprache); Code-Review-Durchsetzung; SAST/SCA-Tool-Auswahl und -Konfiguration; Koordination der Entwicklerschulung; Konformitätsberichterstattung an ISB; Sicherstellung der Zeitallokation für Security Champions |
| **Information Security Manager** | Richtlinienpflege; Ausnahmenüberprüfung; Sicherheitsüberwachung und Incident-Untersuchung; Audit-Koordination; vierteljährliche Konformitätsberichterstattung an ISB |
| **Security Champions** | Sicherheitsorientierte Code-Reviews; Mentoring für sicheres Coding in Entwicklungsteams; Advocacy für Standards für sicheres Coding; SAST/SCA-Befunds-Triage; Teilnahme an Bedrohungsmodellierung; Eskalation von Sicherheitsbedenken an Sicherheitsteam |
| **Sicherheitsteam** | SAST/SCA-Tool-Management und Regelwerk-Updates; sicherheitsorientiertes Code-Review für hochrisikoäre Änderungen; Sicherheitstestkoordination; Incident Response für Schwachstellen auf Code-Ebene; SAST-Unterdrückungsgenehmigung für kritische/hohe Befunde; Teilnahme an Auftragnehmer-Audits |
| **DevOps-Ingenieure** | CI/CD-Pipeline-Integration von SAST- und SCA-Tools; Build-Pipeline-Durchsetzung von Sicherheitsgates; Secrets-Management-Infrastruktur; Integration von Geheimniserkennungstools |
| **Einzelne Entwickler und Auftragnehmer** | Einhaltung der Standards für sicheres Coding; Teilnahme am Code-Review; zeitnahe Behebung von Sicherheitsbefunden; Abschluss der Schulung für sicheres Coding; Incident-Meldung für Sicherheitsmängel; Installation des Pre-Commit-Hooks |

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Verantwortlicher | Häufigkeit | Aufbewahrung |
|---|----------|-----------------|------------|--------------|
| 1 | **Register der Standards für sicheres Coding** (genehmigte Sprachen, Frameworks und zugehörige Coding-Referenzen) | Entwicklungsleiter | Kontinuierlich gepflegt; jährlich überprüft | Aktuelle Version + 3 Jahre |
| 2 | **SAST-Scan-Ergebnisse** (Tool-Ausführungsprotokolle, Befunde, False-Positive-Begründungen) | Entwicklungsleiter / DevOps | Pro Pull Request; monatlich überprüft | 2 Jahre |
| 3 | **SCA-Abhängigkeitsscan-Ergebnisse** (Schwachstellenbefunde, SBOM-Ausgaben, Behebungsunterlagen) | Entwicklungsleiter / DevOps | Pro Build; monatlich überprüft | 2 Jahre |
| 4 | **Code-Review-Unterlagen** (Pull-Request-Reviews, Sicherheitsreview-Checklisten, Genehmigungsunterlagen) | Entwicklungsleiter | Pro Codeänderung | 3 Jahre |
| 5 | **Sicherheitsorientierte Code-Review-Unterlagen** für hochrisikoäre Änderungen (Authentifizierung, Autorisierung, Kryptographie) | Security Champions / Sicherheitsteam | Pro anwendbarer Änderung | 3 Jahre |
| 6 | **Schulungsabschlussunterlagen für sicheres Coding** (Grundlagen, Auffrischung, sprachspezifisch, Security Champion) | Entwicklungsleiter / HR | Jährlich; pro Onboarding | Beschäftigungsdauer + 3 Jahre |
| 7 | **Abhängigkeitsschwachstellen-Behebungsunterlagen** (Befundschiessungs-Tracking mit SLA-Konformität) | Entwicklungsleiter | Pro Befund | 3 Jahre |
| 8 | **SAST/SCA-Tool-Konfigurationsunterlagen** (Regelwerke, aktivierte Prüfungen, Unterdrückungsbegründungen) | Sicherheitsteam / DevOps | Jährlich überprüft | Aktuelle Version + 1 Jahr |
| 9 | **Unterlagen zu Verstössen gegen verbotene Praktiken** (Incidents mit hart kodierten Geheimnissen, erkannte und behobene unsichere Muster) | Sicherheitsteam | Pro Incident | 3 Jahre |
| 10 | **Ausnahmenregister** (Anträge, Genehmigungen, kompensierende Massnahmen, vierteljährliche Überprüfungen) | Information Security Manager | Kontinuierlich gepflegt; vierteljährlich überprüft | Ausnahmedauer + 3 Jahre |
| 11 | **Nachweise für sicheres Coding bei ausgelagerter Entwicklung** (Auftragnehmer-Schulungsunterlagen, Code-Review-Unterlagen, SLA-Konformität, vierteljährliche Auditberichte, jährliche Sicherheitsbewertungen) | Entwicklungsleiter / Beschaffung | Pro Auftragnehmer-Engagement; vierteljährliche Audits | Vertragsdauer + 3 Jahre |
| 12 | **Unterlagen zur jährlichen Überprüfung der Standards für sicheres Coding** (Prüfdatum, vorgenommene Änderungen, Genehmigung) | Entwicklungsleiter | Jährlich | 3 Jahre |
| 13 | **SAST/SCA-Befundtrends** — Monatliche Berichte mit Befundraten, Behebungszeiten, offenen Befunden nach Schweregrad für SOC-2-Audit-Stichproben | Sicherheitsteam | Monatlich | 2 Jahre |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team überprüft die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf SAST/SCA-Tool-Berichte, Code-Review-Abschlussunterlagen, Schulungsabschlussunterlagen, Abhängigkeitsaudit-Ergebnisse, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

**Konformitätsmetriken**:

| Kennzahl | Zielwert | Messhäufigkeit |
|----------|----------|----------------|
| Codeänderungen mit abgeschlossenem Peer-Review vor Merge | 100 % | Monatlich |
| SAST-Scans pro Pull Request ausgeführt (Produktionsanwendungen) | ≥95 % | Monatlich |
| Kritische/hohe SAST-Befunde vor Merge behoben oder als False Positive dokumentiert | ≥95 % | Monatlich |
| Kritische/hohe Abhängigkeitsschwachstellen innerhalb SLA behoben | ≥90 % | Monatlich |
| Entwickler mit aktueller Schulung für sicheres Coding | ≥95 % | Vierteljährlich |
| Hart kodierte Geheimnisse erkannt und innerhalb von 24 Stunden behoben | 100 % | Pro Incident |

**Konformitätsbewertung**:

| Komponente | Gewicht | Berechnung |
|------------|---------|-----------|
| Code-Review-Konformität | 30 % | (Codeänderungen mit abgeschlossenem Review) / Gesamte Codeänderungen × 100 |
| SAST-Abdeckung | 25 % | (Pull Requests mit bestandenem SAST-Scan) / Gesamte Pull Requests × 100 |
| Abhängigkeitssicherheit | 25 % | (Kritische/hohe Abhängigkeitsschwachstellen innerhalb SLA behoben) / Gesamte kritische/hohe Befunde × 100 |
| Schulungskonformität | 20 % | (Entwickler mit aktueller Schulung) / Gesamte Entwickler × 100 |

**Behandlung von Nichteinhaltung**: Unter 70 % erfordert sofortige ISB-Eskalation und Behebungsplan. 70–89 % erfordert Information-Security-Manager-Aufsicht mit monatlichen Überprüfungen. 90 % und darüber folgt der vierteljährlichen Standardüberwachung.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll vorab durch den Information Security Manager genehmigt und mit dokumentierter Risikoakzeptanz, kompensierenden Massnahmen und einem definierten Prüfdatum (maximal 12 Monate) erfasst werden. Ausnahmen sollen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses. Richtlinienverstösse sollen dokumentiert, vom Information Security Manager untersucht und dem ISB gemeldet werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen neue Schwachstellenklassen, Änderungen des OWASP Top 10 und CWE/SANS Top 25, neue von der Organisation übernommene Programmiersprachen oder Frameworks, die Weiterentwicklung von SAST/SCA-Tools, Auditbefunde sowie Erkenntnisse aus Sicherheitsincidents mit Schwachstellen auf Anwendungsebene berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zum sicheren Coding — Zuordnung zu ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Leitlinien für Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortung |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Normen |
| Abschnitt 7.3 Bewusstsein | 6.3 Bewusstsein, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 8.4 Zugriff auf Quellcode |
| | 8.25 Sicherer Entwicklungslebenszyklus |
| | 8.26 Sicherheitsanforderungen an Anwendungen |
| | **8.28 Sicheres Coding** |
| | 8.29 Sicherheitstests in Entwicklung und Abnahme |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 7 — Datenschutz durch Technik und Voreinstellung; Art. 8 — Technische und organisatorische Massnahmen; sicheres Coding als präventive technische Massnahme |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit, einschliesslich Massnahmen auf Anwendungsebene |
| EU DSGVO (sofern anwendbar) | Art. 25 — Datenschutz durch Technik und Voreinstellung; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.28 — Sicheres Coding |
| ISO/IEC 27002:2022 | Abschnitt 8.28 — Implementierungsleitfaden für sicheres Coding |
| NIST SP 800-218 (SSDF) v1.1 | PW.4 — Quellcode gemäss sicheren Coding-Praktiken erstellen; PW.5 — Build-Prozess sicher konfigurieren; PW.6 — Code prüfen und testen |
| NIST SP 800-53 Rev 5 | SA-15 (Entwicklungsprozess, Standards und Tools), SA-16 (Entwicklerbereitgestellte Schulung), SA-17 (Entwickler-Sicherheitsarchitektur und -design) |
| CIS Controls v8 | 16.1 (Sicherer Anwendungsentwicklungsprozess), 16.2 (Softwarearchitektur verwalten), 16.4 (Individuell entwickelte Software sichern), 16.12 (Sicherheitsprüfungen auf Code-Ebene implementieren) |
| OWASP Top 10 (2021) | A01–A10 — Sicherheitsrisikokategorien für Webanwendungen, die durch sichere Coding-Praktiken adressiert werden |
| CWE/SANS Top 25 (2025) | Gefährlichste Softwareschwachstellen, die durch Eingabevalidierung, Ausgabekodierung und Standards für sicheres Coding adressiert werden |

---

<!-- QA_VERIFIED: 2026-03-29 -->
