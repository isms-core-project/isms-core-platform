<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.28-DE:framework:POL:a.8.28 -->
**ISMS-POL-A.8.28 — Richtlinie zur sicheren Codierung**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zur sicheren Codierung |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.28 |
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
- Sekundär: Technischer Leiter (TL)
- Compliance: Legal/Compliance Officer
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.8.28.1-UG/TG (SDLC-Assessment-Spezifikation)
- ISMS-IMP-A.8.28.2-UG/TG (Standards- und Tools-Assessment-Spezifikation)
- ISMS-IMP-A.8.28.3-UG/TG (Code-Review- und Test-Assessment-Spezifikation)
- ISMS-IMP-A.8.28.4-UG/TG (Drittanbieter- und Open-Source-Software-Assessment-Spezifikation)
- ISMS-CTX-A.8.28 (Sprachspezifische Richtlinien zur sicheren Codierung)
- ISMS-REF-A.8.28 (Technische Referenz für Code Reviews)
- ISO/IEC 27001:2022 Control A.8.28
- ISO/IEC 27002:2022 Control 8.28

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an sichere Softwareentwicklung gemäss ISO/IEC 27001:2022 Control A.8.28 (Sichere Codierung) fest.

**Zweck**: Definition, WAS an Kontrollen für sichere Codierung erforderlich ist und WER verantwortlich ist. Technische Implementierungsdetails (WIE) sind in den ISMS-IMP-A.8.28-Spezifikationen dokumentiert.

**Anwendungsbereich**: Alle Softwareentwicklungsaktivitäten einschliesslich interner Entwicklung, ausgelagerter Entwicklung und Anpassung beschaffter Software. Gilt für alle Anwendungstypen, Entwicklungsphasen und Programmiersprachen.

**Adressiertes Geschäftsrisiko**: Softwareschwachstellen, die zu Datenschutzverletzungen, Dienstunterbrechungen, finanziellen Verlusten, Reputationsschäden und regulatorischen Sanktionen führen.

**Regulatorische Ausrichtung**: Gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen):

- **Verbindlich**: Swiss DSG, EU DSGVO (Art. 32), ISO 27001:2022
- **Orientierend**: OWASP Top 10, NIST SP 800-218 SSDF, CWE Top 25

---

# Steuerungsausrichtung und Anwendungsbereich

## ISO/IEC 27001:2022 Control A.8.28

**Kontrollanforderung**:
> *Prinzipien der sicheren Codierung müssen auf die Softwareentwicklung angewendet werden.*

**Kontrollziel**: Reduzierung der Anzahl von Sicherheitsschwachstellen in Software durch Anwendung von Prinzipien der sicheren Codierung über den gesamten Entwicklungslebenszyklus.

**Diese Kontrolle adressiert**:

- Prävention von Schwachstellen während der Entwicklung (Shift-Left Security)
- Prävention gängiger Schwachstellen (Injection, XSS, Authentifizierungsfehler usw.)
- Sichere Design- und Architekturprinzipien
- Entwicklerschulung und Kompetenz
- Code Review und Sicherheitstests
- Sicherheit von Drittanbieter-Komponenten

## Anwendungsbereichs-Definition

**Im Geltungsbereich**:

- Alle Softwareentwicklung (Neuentwicklung, Wartung, Erweiterungen, Patches)
- Alle Entwicklungstypen (intern, ausgelagert, vertraglich, beschafft)
- Alle Anwendungstypen (Web, Mobile, API, Desktop, Eingebettet, Serverlos)
- Alle von [Organisation] verwendeten Sprachen und Rahmenwerke
- Entwicklungs-, Staging- und Produktionsumgebungen

**Nicht im Geltungsbereich**:

- Infrastrukturkonfiguration (siehe A.8.9 Konfigurationsmanagement)
- Netzwerksicherheit (siehe A.8.20-22 Netzwerksicherheit)
- Kryptografisches Schlüsselmanagement (siehe A.8.24 Kryptographie)

## Dokumentenhierarchie

| Dokumententyp | Inhalt | Aktualisierungsturnus |
|---------------|--------|----------------------|
| **Diese Richtlinie (POL)** | Anforderungen, Governance, Verantwortlichkeit | Jährlich |
| **Implementierung (IMP)** | Bewertungsverfahren, Arbeitsmappenspezifikationen | Vierteljährlich |
| **Kontext (CTX)** | Sprachspezifische Muster, Technologie-Leitfaden | Halbjährlich |
| **Referenz (REF)** | Checklisten, technische Methoden | Nach Bedarf |

---

# Anforderungen an sichere Entwicklung

## Sicherheit vor der Entwicklung

**Definition von Sicherheitsanforderungen**:

- Sicherheitsanforderungen MÜSSEN für alle Projekte definiert werden, die sensible Daten verarbeiten
- Anforderungen abgeleitet aus Datenklassifizierung, regulatorischen Bedürfnissen und Bedrohungslandschaft
- Sicherheitsabnahmekriterien definiert vor Entwicklungsbeginn

**Threat-Modelling-Anforderungen**:

| Projekttyp | Anforderung |
|------------|-------------|
| Neue Anwendungen mit sensiblen Daten | Verbindlich |
| Wesentliche Architekturänderungen | Verbindlich |
| Öffentlich zugängliche Anwendungen/APIs | Verbindlich |
| Finanzielle/PII-Verarbeitung | Verbindlich |
| Interne Tools (begrenzte Exposition) | Empfohlen |

**Threat-Model-Dokumentation**:

- Systemarchitektur und Datenflüsse
- Vertrauensgrenzen und Angriffsfläche
- Identifizierte Bedrohungen mit Risikobewertungen
- Auf Bedrohungen abgebildete Minderungskontrollen
- Validierungsansatz

**Threat-Modelling-Methodik**: [Organisation] MUSS eine anerkannte Methodik verwenden (STRIDE, PASTA, DREAD oder OWASP Threat Dragon). Methodikauswahl pro Anwendung dokumentiert; Konsistenz innerhalb von Anwendungsfamilien empfohlen.

**Verifizierung**: Threat Models vom Application-Security-Team überprüft; Genehmigung in Arbeitsmappe 1 dokumentiert. Kritische Anwendungen erfordern ISB-Freigabe.

**Sicherheitsarchitektur-Review**:

- Erforderlich vor Entwicklungs-Sprint 1 für neue Anwendungen
- Erforderlich bei wesentlichen Architekturänderungen
- Genehmigung durch Security Architect oder Application-Security-Team erforderlich
- Kritische Anwendungen erfordern ISB-Genehmigung

## Entwickler-Sicherheitsschulung

**Schulungsanforderungen**:

| Schulungstyp | Zielgruppe | Turnus |
|--------------|------------|--------|
| Grundlagen sicherer Codierung | Alle Entwickler | Initial + Jährlich |
| Sprachspezifische Sicherheit | Entwickler der betreffenden Sprache | Initial |
| Security Champions fortgeschritten | Security Champions | Vierteljährlich |
| OWASP-Top-10-Updates | Alle Entwickler | Bei Aktualisierung |

**Schulungsverifizierung**:

- Abschluss im Enterprise-Learning-Management-System verfolgt (z.B. Workday Learning, SAP SuccessFactors oder gleichwertig)
- Wissensbewertungen erforderlich mit Mindestbestehensquote: 85 % für Grundlagen sicherer Codierung und sprachspezifisches Training; 80 % für Sensibilisierungsschulung. Begründung der Bestehensquote: Sicherheitskritische Kompetenzen erfordern tieferes Verständnis als allgemeine Sensibilisierung.
- Abschlusszertifikate als Nachweis aufbewahrt
- Nicht-Compliance nach 30 Tagen an Entwicklungsmanager eskaliert; ISB-Benachrichtigung nach 60 Tagen

**Schulungsinhalt-Eigentümerschaft**:

- Application-Security-Team pflegt Schulungsinhalte
- Inhalte jährlich oder bei OWASP-Top-10-/CWE-Top-25-Updates überprüft und aktualisiert
- Sprachspezifisches Training ausgerichtet auf ISMS-CTX-A.8.28

**Verifizierung**: Schulungsabschlussberichte vierteljährlich aus LMS generiert; Abschlussraten als KPI verfolgt (Ziel: 100 %). Musterzertifikate für Prüfungen aufbewahrt.

## Standards zur sicheren Codierung

**Universelle Anforderungen** (alle Sprachen):

**Eingabevalidierung**:

- ALLE Eingaben validieren (Nutzer, API, Datei, Umgebung, Datenbank)
- Whitelist-Validierung gegenüber Blacklist bevorzugen
- Serverseitige Validierung verbindlich (clientseitig ist nur UX)
- Ungültige Eingaben ablehnen; keine Bereinigungsversuche

**Ausgabe-Encoding**:

- Kontextangemessenes Encoding (HTML, JavaScript, URL, SQL)
- Framework-bereitgestellte Encoding-Funktionen verwenden
- XSS durch ordnungsgemässes Ausgabe-Encoding verhindern

**Authentifizierung und Session-Management**:

- Starkes Passwort-Hashing (bcrypt, Argon2, scrypt)
- Passwörter niemals im Klartext speichern
- Kryptografisch zufällige Session-Tokens
- Session-Timeout und -Ungültigkeitserklärung bei Abmeldung
- MFA-Unterstützung für sensible Anwendungen

**Autorisierung**:

- Serverseitige Durchsetzung für jede Anfrage
- Least-Privilege-Prinzip
- IDOR-Schwachstellen verhindern
- RBAC- oder ABAC-Implementierung

**Kryptographie**:

- Nur Industrie-Standardalgorithmen (AES-256, RSA-2048+)
- Niemals eigene Kryptographie implementieren
- Ordnungsgemässes Schlüsselmanagement (Schlüssel vom Code getrennt)
- TLS 1.2+ für Daten in Transit (TLS 1.3 bevorzugt)

**Fehlerbehandlung**:

- Generische Fehlermeldungen an Nutzer
- Detaillierte serverseitige Protokollierung (keine sensiblen Daten in Protokollen)
- Sicherheitsereignisse zur Überwachung protokollieren

**Sprachspezifische Richtlinien**: Siehe ISMS-CTX-A.8.28 für Python-, JavaScript-, Java-, C#-, Go-, SQL-Muster.

## Verbotene Praktiken

Folgendes ist **VERBOTEN**:

- Im Quellcode fest hinterlegte Geheimnisse (API-Schlüssel, Passwörter, Tokens)
- Veraltete/unsichere Funktionen (gets(), strcpy(), MD5 für Passwörter, eval() mit Nutzereingaben)
- SQL-Abfragenkonstruktion über String-Verkettung
- Deaktivierte Sicherheitskontrollen in der Produktion
- Geheimnisse in Versionskontrolle einspeichern (auch in der Historie)
- Sicherheitstools-Befunde ohne dokumentierte Ausnahme ignorieren

## Geheimnisverwaltung

- KEINE fest hinterlegten Geheimnisse im Quellcode
- Geheimnisse in genehmigten Geheimnisverwaltungssystemen gespeichert (z.B. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault)
- Secret Scanning in CI/CD-Pipeline integriert (z.B. GitLeaks, TruffleHog, GitHub Secret Scanning)
- Pre-Commit-Hooks konfiguriert, um Commits mit erkannten Geheimnissen zu blockieren
- Geheimnisse regelmässig und bei Mitarbeiteraustritt rotiert

**Reaktion auf Geheimniserkennung**:

- Pre-Commit-Blockierung: Entwickler muss Geheimnis vor Commit-Fortführung entfernen
- CI/CD-Erkennung: Build schlägt fehl; Geheimnis muss vor Merge entfernt und rotiert werden
- Erkennung nach Commit: Sofortige Rotation erforderlich; Vorfall protokolliert

**Verifizierung**: Secret-Scanning-Tool-Konfiguration in Arbeitsmappe 2 dokumentiert; Erkennungsereignisse protokolliert und wöchentlich vom Application-Security-Team überprüft.

## Drittanbieter- und Open-Source-Komponenten

**Komponentenauswahl**:

- Sicherheitsposition vor Übernahme bewerten
- Gut gepflegte, weitverbreitete Bibliotheken bevorzugen
- Vor Einbindung auf bekannte Schwachstellen prüfen
- Lizenzkompatibilität verifizieren

**Laufendes Management**:

- Komponenteninventar pflegen (Software Bill of Materials)
- Schwachstellen über SCA-Tools überwachen
- Innerhalb definierter SLAs patchen/aktualisieren
- Ungenutzte Abhängigkeiten entfernen

---

# Code Review und Sicherheitstests

## Code-Review-Anforderungen

**Peer Review**:

- Alle Produktionscode-Änderungen erfordern Peer Review
- Sicherheitsorientiertes Review für Änderungen, die Authentifizierung, Autorisierung, Kryptographie, Eingabebehandlung betreffen
- Branch-Schutz verhindert Merge ohne Genehmigung

**Sicherheits-Review-Kriterien**: Siehe ISMS-REF-A.8.28 für detaillierte Checkliste.

## Sicherheitstestanforderungen

**Static Application Security Testing (SAST)**:

- In CI/CD-Pipeline integriert (z.B. SonarQube, Checkmarx, Snyk Code, Semgrep)
- Bei jedem Build/Commit ausgeführt; Build schlägt bei Kritisch/Hoch-Befunden fehl
- Befunde triagiert und gemäss SLA behoben
- False Positives dokumentiert und angepasst (Ziel: <20 % False-Positive-Rate)

**Dynamic Application Security Testing (DAST)**:

- Gegen Staging/QA-Umgebungen ausgeführt (z.B. OWASP ZAP, Burp Suite, Qualys WAS)
- Vor Produktions-Release für Webanwendungen erforderlich
- API-Sicherheitstests für alle APIs (z.B. Postman-Sicherheitstests, OWASP API Security)

**Software Composition Analysis (SCA)**:

- In CI/CD-Pipeline integriert (z.B. Snyk, Dependabot, OWASP Dependency-Check)
- Überwacht alle Drittanbieter-Abhängigkeiten
- Alarmiert bei neuen Schwachstellen in Abhängigkeiten; Build schlägt bei Kritisch/Hoch fehl

**Tool-Integrations-Verifizierung**:

- CI/CD-Pipeline-Konfiguration in Arbeitsmappe 2 dokumentiert
- Tool-Auswahl und Deployment-Status verfolgt
- Scan-Berichte der letzten 90 Tage auf Anfrage verfügbar
- Pipeline-Protokolle belegen automatisierte Ausführung

**Verifizierung**: Sicherheitstools-Dashboards wöchentlich überprüft; Tool-Abdeckung und Scan-Erfolgsraten als KPIs verfolgt.

**Penetrationstests**:

| Anwendungstyp | Turnus | Umfang |
|---------------|--------|--------|
| Kritisch/Hochrisiko | Jährlich mindestens | Vollständige Anwendung (alle OWASP-Top-10-Kategorien) |
| Internetzugang | Jährlich mindestens | Externe Angriffsfläche (Authentifizierung, APIs, Eingabebehandlung) |
| Nach wesentlichen Änderungen | Nach Bedarf | Geänderte Komponenten + Integrationspunkte |

**Umfangskriterien**:

- Kritische Anwendungen: Authentifizierungsumgehung, Privilege Escalation, Datenexfiltrations-Szenarien einschliessen
- API-Tests: Alle öffentlichen Endpunkte, Authentifizierungsmechanismen, Rate Limiting einschliessen
- Nach dem Test: Befunde gemäss SLA behoben; Nachtest für Kritisch/Hoch-Befunde

**Nachtest-Anforderungen**:

- Kritische und Hoch-Befunde MÜSSEN nach Behebung nachgetestet werden, um Wirksamkeit zu verifizieren
- Nachtest kann auf betroffene Komponenten eingegrenzt werden (kein vollständiger Anwendungs-Nachtest erforderlich)
- Mittel- und Niedrig-Befunde durch interne Sicherheitstests verifiziert (DAST oder manuelle Tests), sofern nicht Kunden- oder regulatorische Anforderungen externen Nachtest vorschreiben
- Nachtest-Nachweise in Arbeitsmappe 3 dokumentiert

**Verifizierung**: Penetrationstest-Berichte gemäss Abschnitt 7.3 aufbewahrt; Behebungsnachweise in Arbeitsmappe 3 dokumentiert.

## SLAs zur Schwachstellenbehebung

| Schweregrad | CVSS-Score | Behebungs-SLA |
|-------------|------------|---------------|
| **Kritisch** | 9,0–10,0 | 7 Tage |
| **Hoch** | 7,0–8,9 | 30 Tage |
| **Mittel** | 4,0–6,9 | 90 Tage |
| **Niedrig** | 0,1–3,9 | Best Effort / nächstes Release |

**SLA-Verfolgungsmechanismus**:

- Schwachstellen im Issue-Tracking-System verfolgt (z.B. Jira, Azure DevOps) mit Schweregrad und Entdeckungsdatum
- Überfälligkeit automatisch berechnet; überfällige Punkte markiert
- Wöchentliche SLA-Compliance-Überprüfung durch Application-Security-Team
- Monatlicher SLA-Bericht an Entwicklungsmanagement und ISB

**Ausnahmeprozess**:

- Dokumentierte Geschäftsbegründung erforderlich
- Risikobeurteilung und kompensierende Kontrollen (z.B. WAF-Regel, Netzwerkisolierung, erweiterte Überwachung)
- Genehmigung: Mittel durch Security Lead, Hoch/Kritisch durch ISB
- Maximale Ausnahmedauer: 90 Tage (erneuerbar)
- Ausnahmen im zentralen Ausnahmeregister verfolgt (Arbeitsmappe 3)

**Verifizierung**: Schwachstellen-Altersüberprüfungs-Dashboard wöchentlich überprüft; SLA-Compliance-Raten als KPI verfolgt (Kritisch ≥95 %, Hoch ≥90 %).

---

# Rollen und Verantwortlichkeiten

## Geschäftsleitung

- Richtlinie zur sicheren Codierung genehmigen
- Budget für Sicherheitstools und Schulungen zuweisen
- Sicherheitskennzahlen vierteljährlich überprüfen
- Eskalationspunkt für kritische Schwachstellen

## Informationssicherheitsbeauftragter (ISB)

- Gesamtverantwortung für das sichere Entwicklungsprogramm
- Auswahl von Sicherheitstools genehmigen
- Hochrisiko-Ausnahmen genehmigen
- Schwachstellentrends und Behebungsstatus überprüfen

## Application-Security-Team

- Standards zur sicheren Codierung pflegen
- Threat-Model-Reviews durchführen
- Sicherheitstesttools verwalten (SAST, DAST, SCA)
- Schwachstellen triagieren und verfolgen
- Sicherheitsschulungen durchführen
- Vorfallsreaktion bei Code-Schwachstellen unterstützen

## Entwicklungsmanagement

- Sicherstellen, dass Entwickler Sicherheitsschulungen abschliessen
- Zeit für Sicherheitsaktivitäten in Sprints einplanen
- Code-Review-Anforderungen durchsetzen
- Ungelöste Sicherheitsbefunde eskalieren

## Security Champions

- Eingebettete Sicherheitsfürsprecher in Entwicklungsteams
- Erster Ansprechpartner für Sicherheitsfragen
- Am Threat Modelling teilnehmen
- Sichere Codierungspraktiken fördern

**Programmstruktur**:

- Abdeckungsziel: Mindestens 1 Security Champion pro Entwicklungsteam (oder pro 10 Entwickler)
- Auswahl: Vom Entwicklungsmanager nominiert, vom Application-Security-Team genehmigt
- Designation: Formelle Rolle im HR-System dokumentiert; 10–20 % Zeitzuweisung für Sicherheitsaktivitäten
- Schulung: Vierteljährliche fortgeschrittene Sicherheitsschulung (über Standard-Entwicklerschulung hinaus)
- Anerkennung: Security-Champion-Beiträge in Leistungsbeurteilungen einbezogen

**Verifizierung**: Security-Champions-Roster vom Application-Security-Team gepflegt; Abdeckung in Arbeitsmappe 1 verfolgt.

## Entwickler

- Erforderliche Sicherheitsschulungen abschliessen
- Standards zur sicheren Codierung einhalten
- Sicherheitsbefunde im eigenen Code beheben
- An Code Reviews teilnehmen
- Sicherheitsbedenken melden
- Keine Geheimnisse in Repositories einspeichern

## Drittentwickler

- Compliance mit den Standards zur sicheren Codierung von [Organisation]
- Sicherheitsschulungen nach Bedarf abschliessen
- Code Reviews und Sicherheitstests akzeptieren
- Schwachstellen innerhalb der SLAs beheben

**Compliance-Durchsetzung**:

- Vertragliche Verpflichtung: Anforderungen zur sicheren Codierung in Lieferantenvereinbarungen eingeschlossen (gemäss A.5.20)
- Einführung: Drittentwickler schliessen Schulung zur sicheren Codierung vor Zugangsgewährung ab
- Code Review: Gesamter Drittanbieter-Code unterliegt denselben Review-Standards wie interner Code
- Sicherheitstests: Drittanbieter-Lieferungen vor Abnahme mit SAST/SCA gescannt
- Attestierung: Jährliche Compliance-Bestätigung durch Lieferantenmanagement unterzeichnet

**Verifizierung**: Drittentwickler-Compliance in Arbeitsmappe 4 verfolgt; Attestierungen für Prüfungen aufbewahrt.

---

# Governance und Compliance

## Richtlinien-Compliance-Überwachung

**Kontinuierliche Überwachung**:

- SAST/DAST/SCA-Ergebnisse im Sicherheits-Dashboard verfolgt
- Schwachstellen-Alterung überwacht
- Schulungsabschluss verfolgt

**Periodische Beurteilung**:

- Vierteljährlich: Schwachstellen-Kennzahlen, Schulungs-Compliance, Ausnahmen-Review
- Jährlich: Vollständige Beurteilung des sicheren Codierungsprogramms (ISMS-IMP-A.8.28)

## Behandlung von Nicht-Compliance

**Progressiver Reaktionsplan**:
1. Erstes Vorkommen: Schulung und dokumentierte Verwarnung
2. Wiederholung: Manager-Eskalation
3. Anhaltende Nicht-Compliance: Entwicklerrechte eingeschränkt
4. Vorsätzlicher Verstoss: Disziplinarmassnahmen gemäss HR-Richtlinien

## Ausnahmemanagement

- Alle Ausnahmen erfordern dokumentierte Geschäftsbegründung
- Risikobeurteilung und kompensierende Kontrollen verbindlich
- Genehmigungsbehörde basierend auf Risikograd
- Ausnahmen im zentralen Ausnahmeregister verfolgt (Arbeitsmappe 3)
- Maximale Dauer: 90 Tage (erneuerbar mit erneuter Genehmigung)

**Leitfaden für kompensierende Kontrollen**:

- WAF-Regeln, die bekannte Angriffsmuster für nicht gepatchte Schwachstellen blockieren
- Netzwerksegmentierung, die Exposition vulnerabler Komponenten einschränkt
- Erweiterte Überwachung/Alarmierung für Ausnutzungsversuche
- Rate Limiting, das Angriffsdurchführbarkeit reduziert
- Eingabevalidierung am Netzwerkrand (Reverse Proxy)

**Kriterien zur Angemessenheit kompensierender Kontrollen**: Kompensierende Kontrollen MÜSSEN gleichwertiges Risikoreduktion nachweisen durch:

- **Wirksamkeit**: Kontrolle mindert den spezifischen Ausnutzungspfad (nicht generische Sicherheit)
- **Zuverlässigkeit**: Kontrolle arbeitet kontinuierlich mit Alarmierung bei Ausfall
- **Verifizierbarkeit**: Kontrollbetrieb kann getestet und überwacht werden
- **Umfang**: Kontrolle deckt alle betroffenen Systeme/Datenflüsse ab

Application-Security-Team bewertet Angemessenheit; ISB-Genehmigung für Hoch/Kritisch-Ausnahmen schliesst Kompensationskontroll-Validierung ein.

**Verifizierung**: Ausnahmeregister vierteljährlich überprüft; abgelaufene Ausnahmen für Schliessung oder Erneuerung eskaliert.

## Kennzahlen und Berichterstattung

**Schlüssel-Leistungsindikatoren**:

| Kennzahl | Ziel | Turnus | Datenquelle |
|----------|------|--------|-------------|
| Entwickler-Schulungsabschluss | 100 % | Vierteljährlich | LMS-Abschlussberichte |
| Code-Review-Abdeckung | ≥95 % | Monatlich | Git/PR-Merge-Statistiken |
| Kritische Schwachstellen innerhalb SLA | ≥95 % | Monatlich | Schwachstellenverfolger-Alterungsbericht |
| Hohe Schwachstellen innerhalb SLA | ≥90 % | Monatlich | Schwachstellenverfolger-Alterungsbericht |
| Threat-Model-Abdeckung (Hochrisiko-Apps) | ≥90 % | Vierteljährlich | Arbeitsmappe 1 Anwendungsinventar |

**Kennzahlen-Dashboard**: Sicherheitskennzahlen in einzelnen Assessment-Summary-Dashboards (Arbeitsmappen 1–4) oder Sicherheitsoperationsplattform verfolgt; monatlich vom ISB überprüft.

---

# Integration mit anderen Kontrollen

## Verwandte ISMS-Kontrollen

| Kontrolle | Integration |
|-----------|-------------|
| **A.5.7 Threat Intelligence** | Informiert Prioritäten der sicheren Codierung |
| **A.5.24-28 Vorfallsmanagement** | Code-Schwachstellen lösen Vorfallsreaktion aus |
| **A.8.2-3-5 Authentifizierung und Zugang** | Sichere Codierung implementiert Auth/Authz-Logik |
| **A.8.9 Konfigurationsmanagement** | Sichere Konfiguration im Code |
| **A.8.15-16 Protokollierung und Überwachung** | Sichere Protokollierungsimplementierung |
| **A.8.24 Kryptographie** | Kryptographische Implementierung im Code |
| **A.8.25-27 Sichere Entwicklung** | Komplementäre SDLC-Kontrollen |
| **A.8.29 Sicherheitstests** | Testanforderungen abgestimmt |
| **A.8.30 Ausgelagerte Entwicklung** | Drittanbieter-Anforderungen |
| **A.8.32 Änderungsmanagement** | Sicherheits-Gates im Deployment |

## Regulatorische Zuordnung

| Anforderung | Swiss DSG | EU DSGVO | ISO 27001 |
|-------------|-----------|----------|-----------|
| Sichere Entwicklung | Art. 8 | Art. 32 | A.8.28 |
| Sicherheitstests | Art. 8 | Art. 32 | A.8.29 |
| Schwachstellenmanagement | Art. 8 | Art. 32 | A.8.8 |

---

# Nachweise zu dieser Richtlinie

**Stufe 1 (Dokumentationsüberprüfung) Nachweise:**

Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.8.28 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL, Geschäftsleitung
- ✅ Standards zur sicheren Codierung dokumentiert
- ✅ Entwickler-Schulungsanforderungen festgelegt
- ✅ Code-Review-Anforderungen definiert
- ✅ Sicherheitstestanforderungen dokumentiert
- ✅ Rollen und Verantwortlichkeiten zugewiesen
- ✅ Assessment-Arbeitsmappe-Referenzen dokumentiert (ISMS-IMP-A.8.28)

**Stufe 2 (Operative Wirksamkeit) Nachweise:**

Nachweise, die die operative Wirksamkeit dieser Richtlinie belegen:

- Dokumentation zu Standards der sicheren Codierung
- Entwickler-Schulungsaufzeichnungen und Abschlussraten
- Threat-Model-Beispiele für Hochrisiko-Anwendungen
- Code-Review-Aufzeichnungen (PR-Genehmigungen, Kommentare)
- SAST/DAST/SCA-Scan-Berichte und Trenddaten
- Schwachstellenbehebungsnachweise
- Penetrationstest-Berichte
- Ausnahmeregister mit Genehmigungen
- Compliance-Attestierungen von Drittentwicklern

**Assessment-Arbeitsmappen** (ISMS-IMP-A.8.28-Suite):
- ISMS-IMP-A.8.28.1: SDLC-Assessment
- ISMS-IMP-A.8.28.2: Standards- und Tools-Assessment
- ISMS-IMP-A.8.28.3: Code-Review- und Test-Assessment
- ISMS-IMP-A.8.28.4: Drittanbieter- und OSS-Assessment

**Nachweis-Aufbewahrung**:
- Schulungsaufzeichnungen: Beschäftigungsdauer + 2 Jahre
- Code-Review-Aufzeichnungen: Anwendungslebensdauer + 2 Jahre
- Sicherheitsscan-Ergebnisse: 3 Jahre
- Penetrationstest-Berichte: 5 Jahre
- Schwachstellenbehebungsnachweise: 3 Jahre

---

# Implementierungsressourcen

## Unterstützende Dokumentation

| Dokument | Zweck |
|----------|-------|
| **ISMS-IMP-A.8.28.1-5-UG/TG** | Assessment-Spezifikationen und Arbeitsmappen |
| **ISMS-CTX-A.8.28** | Sprachspezifische Richtlinien (Python, Java, JS, C#, Go, SQL) |
| **ISMS-REF-A.8.28** | Code-Review-Checklisten und technische Referenz |

## Externe Referenzen

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
- CWE Top 25: https://cwe.mitre.org/top25/
- NIST SP 800-218 SSDF: Secure Software Development Framework

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **Technischer Leiter (TL)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen an sichere Softwareentwicklung fest. Implementierungsverfahren, Bewertungsmethoden und Arbeitsmappe-Spezifikationen sind in ISMS-IMP-A.8.28 (UG/TG) dokumentiert. Sprachspezifische Richtlinien befinden sich in ISMS-CTX-A.8.28. Code-Review-Checklisten befinden sich in ISMS-REF-A.8.28.*

<!-- QA_VERIFIED: 2026-03-29 -->
