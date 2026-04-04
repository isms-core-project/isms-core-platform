<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.30-DE:operational:OP-POL:a.8.30 -->
**ISMS-OP-POL-A.8.30 — Ausgelagerte Entwicklung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Ausgelagerte Entwicklung |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.30 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstfassung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.8.30 — Outsourced development
- ISO/IEC 27002:2022 Section 8.30 — Implementation guidance for outsourced development
- NIST SP 800-53 Rev 5 — SA-4 (Acquisition Process), SA-9 (External System Services)
- OWASP Secure Software Contract Annex
- OWASP Top 10:2025 — A03 Software Supply Chain Failures
- CIS Controls v8 — Safeguard 16.4 (Third-Party Software Component Inventory)

**Verwandte Annex-A-Controls**:

| Control | Bezug zur ausgelagerten Entwicklung |
|---------|-------------------------------------|
| A.5.19–23 Lieferanten- und Cloud-Sicherheit | Lieferantenbewertungsrahmen; cloudgehostete Entwicklungsplattformen |
| A.5.31 Rechtliche, gesetzliche, regulatorische und vertragliche Anforderungen | Regulatorische Pflichten in Auslagerungsverträgen |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | Datenschutzanforderungen beim Anbieterzugriff auf Personendaten |
| A.8.4 Zugriff auf Quellcode | Anbieterzugriff auf organisationseigene Repositories |
| A.8.25–26–29 Sicherer Entwicklungslebenszyklus | Sichere Programmierung, Tests und SDLC-Anforderungen für ausgelagerte Arbeit |
| A.8.28 Sicheres Coding | Programmierstandards, die auf Drittentwickler ausgedehnt werden |
| A.8.31 Trennung von Umgebungen | Umgebungstrennung für ausgelagerte Entwicklung |
| A.8.32 Change Management | Änderungskontrolle bei der Produktionseinführung ausgelagerten Codes |

**Verwandte interne Richtlinien**:

- Richtlinie für den sicheren Entwicklungslebenszyklus
- Richtlinie für Lieferanten- und Cloud-Dienste-Sicherheit
- Richtlinie für den Zugriff auf Quellcode
- Change-Management-Richtlinie
- Richtlinie zur Informationsklassifikation und -behandlung
- Datenschutz- und Personendaten-Richtlinie

---

# Richtlinie für die ausgelagerte Entwicklung

## Zweck

Zweck dieser Richtlinie ist es sicherzustellen, dass die Organisation alle Aktivitäten im Zusammenhang mit der ausgelagerten System- und Softwareentwicklung steuert, überwacht und überprüft, sodass extern entwickelter Code die Informationssicherheitsanforderungen der Organisation erfüllt, bevor er akzeptiert und eingesetzt wird.

Diese Richtlinie unterstützt den schweizerischen nDSG (revDSG) Art. 9, indem sie vertragliche Anforderungen an Auftragsbearbeiter festlegt, die an der Softwareentwicklung beteiligt sind, und sicherstellt, dass ausgelagerte Entwicklungsaktivitäten Personendaten nur auf die Weise verarbeiten, wie die Organisation selbst zur Verarbeitung berechtigt ist. Die Anforderungen des Art. 8 an technische und organisatorische Massnahmen gelten gleichermassen für ausgelagerte Komponenten. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, sind ausserdem die Anforderungen der DSGVO Art. 28 (Pflichten des Auftragsverarbeiters) und Art. 32 (Sicherheit der Verarbeitung) einzuhalten.

## Geltungsbereich

Alle System- und Softwareentwicklungsaktivitäten, die von externen Parteien im Auftrag der Organisation durchgeführt werden, einschliesslich:

- Individuelle Softwareentwicklung durch Auftragsentwicklungsunternehmen.
- Offshore- und Nearshore-Entwicklungsteams.
- Freiberufliche Einzelentwickler und Auftragnehmer.
- Entwicklungspartnerschaften und Co-Entwicklungsvereinbarungen.
- Anpassung und Erweiterung beschaffter Software durch Dritte.
- Wartung und Weiterentwicklung bestehender organisationseigener Systeme durch Dritte.

Alle Mitarbeitenden, die für die Beschaffung, das Management oder die Abnahme ausgelagerter Entwicklungsarbeit verantwortlich sind.

**Nicht im Geltungsbereich**: Kommerzielle Standardsoftware (COTS), die ohne Anpassungen erworben wird (abgedeckt durch A.5.19–23); interne Entwicklungsaktivitäten (abgedeckt durch A.8.25-26-29); Cloud-Plattformdienste, bei denen kein individueller Code entwickelt wird; quelloffene Software, die als Abhängigkeit verwendet wird (abgedeckt durch SCA-Anforderungen in der Richtlinie für den sicheren Entwicklungslebenszyklus).

## Grundsatz

Die Organisation trägt unabhängig davon, wo und von wem ausgelagerter Code entwickelt wird, die Verantwortung für dessen Sicherheit. Ausgelagerte Entwicklung muss Sicherheitsanforderungen, vertraglichen Kontrollen und Verifikationsaktivitäten unterliegen, die den für interne Entwicklung geltenden Anforderungen gleichwertig sind oder diese übertreffen.

Kein ausgelagerter Code darf ohne unabhängige Sicherheitsvalidierung und formale Abnahme durch die Organisation in die Produktion übernommen werden.

---

## Lieferantensicherheitsbewertung

Vor der Beauftragung eines externen Entwicklungspartners führt die Organisation eine Sicherheitsbewertung durch, um zu bestätigen, dass der Anbieter die Informationssicherheitsanforderungen erfüllen kann.

**Bewertungskriterien vor Vertragsabschluss**:

| Bewertungsbereich | Mindestanforderungen |
|-------------------|----------------------|
| **Sicherheitszertifizierungen** | Nachweis einer ISO 27001-Zertifizierung, eines SOC 2 Type II-Berichts oder Äquivalents; oder Ausfüllen des Lieferantensicherheitsfragebogens der Organisation |
| **Sichere Entwicklungspraktiken** | Dokumentierter SDLC mit Sicherheitsaktivitäten; Einsatz von SAST, SCA und Code-Review-Prozessen |
| **Personalsicherheit** | Hintergrundüberprüfungen für Entwickler mit Zugriff auf Organisationsdaten; von allen zugriffsberechtigten Personen unterzeichnete NDA |
| **Datenschutz** | Auftragsverarbeitungsvertrag (AVV) gemäss schweizerischem nDSG Art. 9; Beurteilung des Datenspeicherorts und Datentransfers abgeschlossen |
| **Incident Response** | Dokumentierte Reaktionsfähigkeit bei Sicherheitsvorfällen; Fähigkeit zur Benachrichtigung der Organisation innerhalb von 24 Stunden nach einem Sicherheitsereignis |
| **Business Continuity** | Nachweis der Business-Continuity-Planung; Quellcode-Hinterlegung (Escrow) oder gleichwertige Kontinuitätsvereinbarung, wo angemessen |
| **Referenzen** | Überprüfbare Referenzen aus vergleichbaren Aufträgen |

**Bewertungsstufen**:

| Anbieterstufe | Kriterien | Bewertungstiefe |
|---------------|-----------|-----------------|
| **Stufe 1 — Hohes Risiko** | Anbieter entwickelt High-Risk-Applikationen; hat Zugriff auf Produktionsdaten oder personenbezogene Daten; entwickelt internetfähige Systeme | Vollständige Sicherheitsbewertung + Vor-Ort- oder Remote-Audit + jährliche Neubewertung |
| **Stufe 2 — Mittleres Risiko** | Anbieter entwickelt interne Tools; eingeschränkter Datenzugriff; kein direkter Produktionszugriff | Sicherheitsfragebogen + Nachweisüberprüfung + Neubewertung alle zwei Jahre |
| **Stufe 3 — Niedriges Risiko** | Anbieter entwickelt unkritische Hilfsprogramme; kein Zugriff auf sensible Daten | Sicherheitsfragebogen + Selbstauskunft + Neubewertung bei Vertragsverlängerung |

**Bestimmung der Anbieterstufe**:

Anbieter werden auf der Grundlage des höchsten vorhandenen Risikofaktors eingestuft:

**Stufe-1-Auslöser** (einer genügt):
- Entwickelt Applikationen, die vertrauliche oder eingeschränkt zugängliche Daten verarbeiten
- Direkter Zugriff auf Produktionsumgebungen oder Datenbanken
- Entwickelt internetfähige Systeme mit Benutzerauthentifizierung
- Verarbeitet Personendaten von mehr als 1'000 Personen
- Anpassung von Zahlungsverarbeitungs- oder Finanzsystemen
- Zugriff auf Quellcode-Repositories mit proprietären Algorithmen

**Stufe-2-Auslöser** (keiner der Stufe-1-Auslöser, aber mindestens einer der folgenden):
- Entwickelt rein interne Applikationen
- Lesezugriff auf nicht-produktive Daten
- Verarbeitet Personendaten von weniger als 1'000 Personen
- Integrationsentwicklung mit Drittanbieter-APIs
- Entwicklung von Reporting- und Analyse-Tools

**Stufe 3** (Standard):
- Entwicklung von Hilfsprogrammen (Skripte, CLI-Tools, unkritische Automatisierung)
- Entwicklung statischer Websites ohne Erhebung von Benutzerdaten
- Dokumentation und UI/UX-Design (kein Code-Zugriff)
- Prototyp-/Proof-of-Concept-Arbeiten ausschliesslich mit synthetischen Daten

Die Stufenbestimmung ist im Lieferantensicherheitsbewertungsdokument festzuhalten und bei Änderungen des Auftragumfangs zu überprüfen.

Bewertungsergebnisse sind für die Dauer der Anbieterbeziehung zuzüglich 3 Jahre aufzubewahren.

Anbieter, die die Sicherheitsbewertung nicht bestehen, dürfen erst dann beauftragt werden, wenn festgestellte Mängel behoben und verifiziert wurden.

### Sicherheitswarnsignale beim Anbieter

Folgende Befunde während der Anbieterbewertung führen zur Disqualifikation, sofern sie nicht behoben werden:

| Warnsignal | Risiko | Erforderliche Massnahme |
|------------|--------|-------------------------|
| **Kein formaler SDLC** | Unstrukturierte Entwicklung; inkonsistente Sicherheitspraktiken | SDLC mit Sicherheits-Gates dokumentieren; mindestens 3 Monate konsistente Anwendung nachweisen |
| **Keine SAST/SCA-Werkzeuge** | Schwachstellen werden vor Lieferung nicht erkannt | Automatisierte Sicherheitsscans implementieren; ≥3 Scans mit Massnahmen nachweisen |
| **Anbieter verweigert Audit-Rechtsklausel** | Sicherheitsangaben können nicht verifiziert werden | Audit-Rechte akzeptieren oder SOC 2 Type II / ISO 27001-Zertifizierung vorlegen |
| **Auslagerung an nicht offengelegte Subunternehmer** | Unbekannte Sicherheitslage in der Lieferkette | Vollständige Transparenz über Subunternehmer; Weitergabe der Sicherheitsanforderungen; Bewertung jedes einzelnen |
| **Keine Incident-Response-Fähigkeit** | Kompromittierungen können nicht erkannt oder behoben werden | IR-Plan dokumentieren; Verpflichtung zur 24-Stunden-Meldung; IR-Tests nachweisen |
| **Früherer schwerwiegender Sicherheitsvorfall (unbehoben)** | Muster mangelhafter Sicherheit | Verbesserungen nach dem Vorfall nachweisen; Behebung durch Dritte validieren lassen |
| **Fehlende Hintergrundüberprüfungen** | Insider-Threat-Risiko | Hintergrundüberprüfungen für Personal mit Datenzugriff einführen |
| **Verwendung privater E-Mail-Konten für Arbeitsaufgaben** | Keine Trennung von Unternehmens- und Privatdaten | Unternehmens-E-Mail bereitstellen; Acceptable-Use-Policy dokumentieren |

**Während des Auftrags sind folgende Eskalationsauslöser zu beachten**:
- Anbieter macht falsche Angaben bei der Sicherheitsbewertung
- Unautorisierte Datenexfiltration erkannt
- Anbieter verweigert Schwachstellenbehebung
- Sicherheitstestergebnisse werden zurückgehalten oder gefälscht

---

## Vertragliche Sicherheitsanforderungen

Alle Verträge über ausgelagerte Entwicklung müssen Sicherheitsanforderungen als vertragliche Pflichten enthalten.

**Obligatorische Vertragsklauseln**:

| Klausel | Anforderung |
|---------|-------------|
| **Sichere Entwicklungsstandards** | Der Anbieter muss die sicheren Programmierstandards und die Richtlinie für den sicheren Entwicklungslebenszyklus der Organisation einhalten oder gleichwertige, vom ISB genehmigte Standards nachweisen |
| **Sicherheitstests** | Der Anbieter muss SAST und SCA für alle Liefergegenstände durchführen; DAST für Webapplikationen und APIs; Ergebnisse sind der Organisation vor der Abnahme vorzulegen |
| **Schwachstellenbehebung** | Kritische Schwachstellen: 7 Tage; Hoch: 30 Tage; Mittel: 90 Tage; Niedrig: 180 Tage — entsprechend den Behebungs-SLAs der Organisation |
| **Meldepflicht bei Sicherheitsvorfällen** | Der Anbieter muss die Organisation innerhalb von 24 Stunden nach Entdeckung eines Sicherheitsvorfalls benachrichtigen, der den Auftrag betrifft, einschliesslich vermuteter Datenpannen, Code-Kompromittierungen oder unberechtigter Zugriffe |
| **Audit-Rechte** | Die Organisation behält sich das Recht vor, die Sicherheitspraktiken, Entwicklungsumgebungen und Prozesse des Anbieters nach schriftlicher Vorankündigung von 30 Kalendertagen zu prüfen |
| **Code-Review-Rechte** | Die Organisation hat das Recht, alle im Rahmen des Vertrages gelieferten Quellcodes, Build-Skripte und Konfigurationsdateien zu überprüfen, zu testen und zu inspizieren |
| **Unterauftragsvergabe** | Der Anbieter darf Entwicklungsarbeiten nicht ohne vorherige schriftliche Genehmigung der Organisation an Subunternehmer vergeben; Subunternehmer müssen gleichwertige Sicherheitsanforderungen erfüllen |
| **Datenschutz** | Auftragsverarbeitungsvertrag gemäss schweizerischem nDSG Art. 9; Personendaten werden nur nach Weisung der Organisation verarbeitet; grenzüberschreitende Transfers unterliegen einer Transferbeurteilung |
| **Vertraulichkeit** | NDA für alle proprietären Informationen, Quellcodes, Systemarchitekturen und Daten, auf die während des Auftrags zugegriffen wird |
| **Vertragsbeendigungsregelungen** | Sichere Rückgabe oder Vernichtung aller Organisationsdaten, Quellcodes, Zugangsdaten und Zugriffsberechtigungen bei Vertragsende; Verifizierung innerhalb von 30 Tagen |

**Empfohlene Vertragsklauseln** (je nach Auftragsrisiko):

| Klausel | Anwendbarkeit |
|---------|---------------|
| **Penetrationstests** | Erforderlich für Stufe-1-Anbieter; die Organisation oder ein qualifizierter Dritter führt vor der Produktionsabnahme einen Penetrationstest durch |
| **Hintergrundüberprüfungen** | Erforderlich für Stufe-1-Anbieter-Personal mit Zugriff auf Personendaten, Finanzdaten oder Produktionsumgebungen |
| **Sicherheitsschulung** | Anbieterpersonal muss das Sicherheitsbewusstseinstraining der Organisation absolvieren oder eine gleichwertige Schulung nachweisen |
| **Haftung und Schadenersatz** | Anbieterhaftung für Sicherheitsverletzungen infolge von Nichteinhaltung vertraglicher Sicherheitsanforderungen |
| **Versicherung** | Berufshaftpflicht- und Cyber-Haftpflichtversicherung entsprechend dem Auftragswert und dem Risikoprofil |

**Genehmigungsverfahren für Unterauftragsvergaben**:

Wenn ein Anbieter eine Genehmigung zur Unterauftragsvergabe beantragt:
1. **Benachrichtigung**: Der Anbieter stellt mindestens 30 Tage vor Beauftragung des Subunternehmers eine schriftliche Anfrage ein, die Folgendes enthält:
   - Name und Standort des Subunternehmers
   - Umfang der zu vergebenden Arbeiten
   - Datenzugriff, den der Subunternehmer benötigt
   - Ergebnisse der Sicherheitsbewertung des Subunternehmers
   - Bestätigung der Weitergabe vertraglicher Sicherheitsanforderungen

2. **Bewertung**: Die Organisation prüft den Subunternehmer anhand derselben Sicherheitskriterien wie den Hauptanbieter (stufengerechte Bewertung)

3. **Genehmigung**:
   - Stufe-1-Anbieter: ISB-Genehmigung erforderlich
   - Stufe-2/3-Anbieter: Genehmigung durch den Development Manager mit Benachrichtigung des ISB

4. **Dokumentation**: Genehmigte Subunternehmer werden im Lieferantensicherheitsbewertungsdokument erfasst; dieselben Monitoring- und Zugriffsmanagementanforderungen gelten entsprechend

Nicht genehmigte Unterauftragsvergabe stellt einen wesentlichen Vertragsbruch dar und kann zur Kündigung des Vertrags führen.

---

## Anforderungen an sichere Entwicklung durch Anbieter

Die sicheren Entwicklungsstandards der Organisation sind Anbietern zu Beginn jedes Auftrags mitzuteilen.

**Paket mit Entwicklungsstandards für Anbieter**:

Die Organisation stellt jedem Anbieter folgende Unterlagen zur Verfügung:

- Sichere Programmierstandards für den eingesetzten Technologie-Stack.
- Sicherheitsanforderungsspezifikation für das Projekt.
- Bedrohungsmodell (sofern eines für die Applikation existiert).
- Genehmigte kryptografische Standards und Bibliotheken.
- Anforderungen an Protokollierung und Fehlerbehandlung.
- API-Sicherheitsstandards (sofern zutreffend).
- Anforderungen an Eingabevalidierung und Ausgabekodierung.

**Anforderungen an die Entwicklungsumgebung des Anbieters**:

| Anforderung | Details |
|-------------|---------|
| **Umgebungstrennung** | Entwicklungs-, Test- und Produktionsumgebungen sind zu trennen; Anbieter-Entwicklungsumgebungen dürfen keinen direkten Zugriff auf die Produktionssysteme der Organisation haben |
| **Zugangskontrolle** | Der Anbieterzugriff auf organisationseigene Repositories und Systeme muss dem Prinzip der minimalen Rechtevergabe folgen; der Zugriff muss zeitlich begrenzt und an die Vertragslaufzeit gebunden sein |
| **Verwaltung von Zugangsdaten** | Keine fest kodierten Zugangsdaten im Quellcode; Secrets werden über genehmigte Secrets-Management-Tools verwaltet |
| **Versionskontrolle** | Sämtlicher Code muss in einem genehmigten Versionskontrollsystem mit vollständiger Commit-Historie und Autorenzuordnung gepflegt werden |
| **Abhängigkeitsverwaltung** | Anbieter müssen ein Software-Stückliste (SBOM) für alle Liefergegenstände führen; Drittanbieter-Abhängigkeiten müssen aus genehmigten Registries bezogen und auf bekannte Schwachstellen geprüft werden |

**Supply-Chain-Sicherheit**:

Anbieter müssen Kontrollen implementieren, um Software-Supply-Chain-Risiken gemäss OWASP Top 10:2025 A03 (Software Supply Chain Failures) zu mitigieren:

- Alle Drittanbieter-Abhängigkeiten sind in einer SBOM (im Format CycloneDX oder SPDX) zu inventarisieren und zu verfolgen.
- Abhängigkeiten sind auf bestimmte Versionen festzuschreiben (Pinning) und aus vertrauenswürdigen Registries zu beziehen.
- Transitive Abhängigkeiten sind in die Schwachstellenprüfung einzubeziehen.
- Anbieter müssen Abhängigkeiten gegen Schwachstellendatenbanken (NVD, OSV, GitHub Advisory Database) überwachen und identifizierte Schwachstellen innerhalb der vereinbarten SLAs beheben.
- Der Einsatz nicht mehr gewarteter oder End-of-Life-Komponenten erfordert eine dokumentierte Risikoakzeptanz durch die Organisation.

**SBOM-Anforderungen im Detail**:
- **Format**: CycloneDX 1.4+ (bevorzugt) oder SPDX 2.3+
- **Tiefe**: Transitive Abhängigkeiten einschliessen (nicht nur direkte Abhängigkeiten)
- **Inhalt**: Komponentenname, Version, Lizenz, Lieferant, kryptografischer Hash
- **Übergabe**: SBOM wird mit jedem Release geliefert und bei Abhängigkeitsänderungen aktualisiert
- **Werkzeug**: Generiert mittels automatisiertem SBOM-Tool (CycloneDX CLI, Syft, SPDX-Tools oder Äquivalent) — keine manuell erstellten Tabellen
- **Validierung**: Die Organisation überprüft die SBOM-Vollständigkeit mittels SCA-Tool vor der Abnahme

## Typischer Entwicklungsablauf beim Anbieter

```
┌─────────────────────────────────────────────────────────────────┐
│ AUFTRAGSPHASE                                                    │
├─────────────────────────────────────────────────────────────────┤
│ 1. Lieferantensicherheitsbewertung (ISB) ─────────────────────┐│
│ 2. Vertrag mit Sicherheitsklauseln (Legal + ISB) ─────────────┐││
│ 3. AVV-Abschluss (DSB) ────────────────────────────────────────┘││
│ 4. Übergabe des Entwicklungsstandards-Pakets (Dev Manager) ────┘│
│ 5. Bereitstellung des Anbieterzugriffs (IT Operations) ─────────│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ ENTWICKLUNGSPHASE (iterativ)                                     │
├─────────────────────────────────────────────────────────────────┤
│ 6. Anbieterentwicklung + Sicherheitstests (Anbieter) ───────────│
│    - SAST/SCA pro Build                                          │
│    - Sicherheitsprüfergebnisse werden mit Org geteilt           │
│ 7. Meilensteinlieferung (Anbieter → Dev Manager) ───────────────│
│ 8. Code-Review durch die Organisation (Security Team) ──────────│
│ 9. Schwachstellenbehebung (Anbieter) ───────────────────────────│
│    ↺ Wiederholen bis Abnahmekriterien erfüllt sind             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ ABNAHMEPHASE                                                     │
├─────────────────────────────────────────────────────────────────┤
│ 10. Unabhängige Sicherheitstests (Org / Dritte) ────────────────│
│     - SAST/SCA/DAST                                              │
│     - Penetrationstest (Stufe 1)                                │
│ 11. SBOM-Übergabe und -Prüfung (Dev Manager) ───────────────────│
│ 12. Abnahme-Checkliste (Dev Manager) ───────────────────────────│
│ 13. Abnahmebestätigung (risikobasiert: ISB/Dev Manager/App Owner)│
│ 14. Code-Hinterlegung beim Escrow-Agenten (sofern zutreffend) ──│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE NACH DER PRODUKTIONSEINFÜHRUNG                             │
├─────────────────────────────────────────────────────────────────┤
│ 15. Entzug des Anbieterzugriffs (IT Operations) ────────────────│
│ 16. Verifizierung der Datenlöschung/-rückgabe (DSB) ────────────│
│ 17. Laufender Supportvertrag (sofern vorhanden) ────────────────│
│ 18. Jährliche Sicherheits-Neubewertung (Stufe 1) ───────────────│
└─────────────────────────────────────────────────────────────────┘
```

---

## Code-Review und Sicherheitstests

Sämtlicher ausgelagerter Code muss vor der Abnahme einer unabhängigen Sicherheitsvalidierung durch die Organisation unterzogen werden.

**Anbieterseitige Tests** (vom Anbieter durchgeführt, Ergebnisse werden der Organisation übermittelt):

| Testtyp | Anforderung | Zeitpunkt |
|---------|-------------|-----------|
| **SAST** | Scan des gesamten Quellcodes auf Sicherheitsschwachstellen mit [SAST-Tool] (Beispiele: SonarQube, Semgrep, Checkmarx, Veracode oder vom ISB genehmigtes Äquivalent) | Pro Build oder mindestens wöchentlich während der aktiven Entwicklung |
| **SCA** | Scan aller Abhängigkeiten auf bekannte Schwachstellen und Lizenzkonflikte | Pro Build oder mindestens wöchentlich während der aktiven Entwicklung |
| **Unit-/Integrationstests** | Nachweis der Wirksamkeit von Sicherheitskontrollen (Authentifizierung, Autorisierung, Eingabevalidierung) | Fortlaufend |
| **Secret Scanning** | Verifizierung, dass keine Zugangsdaten, API-Keys oder Tokens im Quellcode oder in Konfigurationsdateien vorhanden sind | Pre-Commit und pro Build |

Anbieterseitige Testergebnisse sind der Organisation in vereinbarten Abständen vorzulegen (mindestens: pro Meilenstein oder Sprint-Lieferung).

**Organisationsseitige Tests** (von der Organisation oder einem beauftragten Dritten durchgeführt):

| Testtyp | Anforderung | Zeitpunkt |
|---------|-------------|-----------|
| **Unabhängiger Code-Review** | Interner Entwickler oder Security Champion überprüft den Anbietercode anhand der sicheren Programmier-Checkliste | Vor Abnahme jedes Liefergegenstands |
| **Unabhängige SAST/SCA** | Die Organisation führt eigene SAST- und SCA-Scans am gelieferten Code durch | Vor Abnahme |
| **DAST** | Dynamische Tests der laufenden Applikation (z.B. OWASP ZAP, Burp Suite oder Äquivalent) | Vor Produktionseinführung |
| **Penetrationstest** | Externer Penetrationstest durch einen Spezialisten für High-Risk-Applikationen | Vor der initialen Produktionseinführung; danach jährlich |

**Mindest-Testgrundlage**: Alle Sicherheitstests müssen mindestens die OWASP Top 10:2025-Kategorien abdecken.

Alle Penetrationstests müssen von einem unabhängigen externen Spezialunternehmen durchgeführt werden, das mindestens eine der folgenden Voraussetzungen erfüllt:
- CREST-Zertifizierung (CREST Registered Penetration Tester oder höher)
- Teammitglieder mit OSCP-, GPEN- oder CEH-Zertifizierungen
- Nachgewiesene Erfahrung mit mindestens 5 vergleichbaren Penetrationstests in den letzten 2 Jahren mit nachprüfbaren Referenzen
- ISO 27001-zertifiziertes Penetrationstest-Unternehmen mit öffentlichem Kundenportfolio

Der Penetrationstest-Dienstleister darf nicht mit dem Entwicklungsanbieter identisch sein, um die Unabhängigkeit zu gewährleisten.

Schwachstellen, die beim Testen identifiziert werden, sind vom Anbieter auf Kosten des Anbieters zu beheben, bevor die Organisation den Liefergegenstand akzeptiert. Kritische und hohe Schwachstellen blockieren die Abnahme.

### Verwaltung der Schwachstellenbehebung

Alle in Anbieterlieferungen identifizierten Schwachstellen sind bis zur Behebung zu verfolgen:

**Verfolgungsprozess**:
1. **Entdeckung**: Schwachstelle mittels SAST/SCA/DAST/Penetrationstest identifiziert
2. **Zuweisung**: Schwachstelle dem Anbieter mit Behebungs-SLA zugewiesen
3. **Verifizierung**: Anbieter liefert Fix + Nachtestergebnisse
4. **Validierung**: Organisation validiert die Wirksamkeit des Fixes
5. **Abschluss**: Dokumentierter Abschluss mit Testnachweis

**SLA-Verfolgung für die Schwachstellenbehebung**:

| Schweregrad | SLA | Reaktion bei SLA-Überschreitung |
|-------------|-----|----------------------------------|
| **Kritisch** | 7 Tage | Sofortige ISB-Eskalation; Abnahme blockiert; Anbieter-Performance-Review |
| **Hoch** | 30 Tage | Eskalation an Development Manager; Abnahme bedingt durch Behebungsplan |
| **Mittel** | 90 Tage | Verfolgung in wöchentlichen Statusmeetings; Abnahme möglich mit dokumentierter Risikoakzeptanz und Behebungsverpflichtung |
| **Niedrig** | 180 Tage | Verfolgung im Projektbacklog; Abnahme möglich mit geplantem zukünftigem Sprint für die Behebung |

**SLA-Fristbeginn**:
- Beginnt mit der Offenlegung der Schwachstelle gegenüber dem Anbieter
- Pausiert bei sachlich begründeten Klärungsanfragen des Anbieters (<5 Werktage)
- Setzt sich nach Anbieterantrag auf SLA-Verlängerung mit Begründung neu (ISB-Genehmigung erforderlich)

**SLA-Compliance-Berichterstattung**:
Verfolgung pro Anbieter, pro Auftrag. Eine Compliance-Rate von <70% löst einen Anbieter-Performance-Review aus.

---

## Abnahmekriterien

Ausgelagerte Liefergegenstände dürfen erst dann akzeptiert oder in die Produktion überführt werden, wenn alle Abnahmekriterien erfüllt sind.

**Sicherheits-Abnahme-Checkliste**:

| # | Kriterium | Geprüft durch |
|---|-----------|---------------|
| 1 | Alle vertraglich geforderten Sicherheitstests abgeschlossen und Ergebnisse vorgelegt | Development Manager |
| 2 | Keine offenen kritischen oder hohen Schwachstellen in SAST-, SCA-, DAST- oder Penetrationstestergebnissen | ISB / Security Team |
| 3 | Unabhängiger Code-Review der Organisation abgeschlossen, keine blockierenden Befunde | Development Manager |
| 4 | SBOM im Format CycloneDX oder SPDX vorgelegt; keine Komponenten mit ungepatchten kritischen oder hohen Schwachstellen, sofern Patches verfügbar; nicht gepatchte Schwachstellen erfordern dokumentierte Risikoakzeptanz und kompensierende Kontrollen | Development Manager |
| 5 | Keine fest kodierten Secrets, Zugangsdaten oder Testdaten im gelieferten Code | Security Team |
| 6 | Code erfüllt die sicheren Programmierstandards der Organisation | Security Champion / Senior Developer |
| 7 | Gesamte Dokumentation geliefert (Architektur, API-Spezifikationen, Deployment-Leitfäden, Konfiguration) | Development Manager |
| 8 | Quellcode und alle Artefakte in das Repository oder an den Escrow-Agenten der Organisation übergeben | Development Manager |
| 9 | Datenschutzanforderungen erfüllt; keine unautorisierten Personendaten beim Anbieter verblieben | Datenschutzbeauftragter / ISB |
| 10 | Lizenz- und geistiges Eigentumsrecht gemäss Vertrag bestätigt | Legal / Procurement |

*Blockierende Befunde umfassen:*
- Fest kodierte Zugangsdaten, API-Keys oder Secrets
- SQL-Injection-Schwachstellen (jedes Schweregrades)
- Schwachstellen zur Umgehung der Authentifizierung
- Autorisierungsfehler, die eine Rechteerweiterung ermöglichen
- Verwendung kryptografisch unsicherer Algorithmen (MD5, SHA-1 für Sicherheitszwecke, DES, RC4)
- Offenlegung sensibler Daten in Logs oder Fehlermeldungen
- Fehlende Eingabevalidierung bei benutzerseitig übermittelten Daten
- Offene kritische oder hohe SAST/DAST-Befunde

**Abnahmebestätigung**:

| Applikationsrisiko | Erforderliche Unterzeichner |
|--------------------|-----------------------------|
| Hohes Risiko | ISB + Development Manager + Applikationsverantwortlicher |
| Mittleres Risiko | Development Manager + Applikationsverantwortlicher |
| Niedriges Risiko | Development Manager |

Abnahmedokumente sind für die gesamte Applikationslebenszeit zuzüglich 3 Jahre aufzubewahren.

---

## Geistiges Eigentum und Code-Hinterlegung (Escrow)

**Code-Eigentümerschaft**:

Der Entwicklungsvertrag muss die Eigentümerschaft an allen Arbeitsergebnissen klar festlegen, einschliesslich Quellcode, Dokumentation, Entwürfen und damit verbundenen geistigen Eigentumsrechten.

Wenn die Organisation eine Individualentwicklung in Auftrag gibt, ist die Standardposition, dass die Organisation alle Rechte des geistigen Eigentums an den Liefergegenständen mit vollständiger Zahlung oder — bei Zahlung bei Lieferung — mit der Lieferung erwirbt, je nachdem, was zuerst eintritt. Jede Abweichung von der vollständigen Eigentümerschaft ist zu dokumentieren, durch Legal und den ISB zu genehmigen und geschäftlich zu begründen.

**Lizenzen**:

Wo eine vollständige Eigentumsübertragung nicht möglich ist (z.B. wenn der Anbieter Rechte an vorbestehenden Komponenten oder Frameworks behält), muss der Vertrag Folgendes festlegen:

- Eine dauerhafte, unwiderrufliche Lizenz für die Organisation, die gelieferte Software zu nutzen, zu modifizieren und zu warten.
- Klare Abgrenzung zwischen Anbieter-eigenen und organisationseigenen Komponenten.
- Lizenzbedingungen für alle im Liefergegenstand enthaltenen Drittanbieter- und Open-Source-Komponenten.

**Code-Hinterlegung (Escrow)**:

Für Stufe-1-Anbieteraufträge, bei denen die Organisation den Quellcode nicht direkt in ihrem Besitz hat, schlichtet die Organisation eine Code-Hinterlegungsvereinbarung mit einem unabhängigen Escrow-Agenten (z.B. Escode, Codekeeper oder Äquivalent) ab.

**Anforderungen an die Hinterlegungsvereinbarung**:

| Anforderung | Details |
|-------------|---------|
| **Hinterlegungsfrequenz** | Quellcode wird bei jedem Major-Release hinterlegt, mindestens aber vierteljährlich |
| **Hinterlegungsinhalt** | Vollständiger Quellcode, Build-Skripte, Build-Umgebungsspezifikationen, Dokumentation, Abhängigkeiten und Deployment-Anweisungen, die ausreichen, um die Software unabhängig zu erstellen und einzusetzen |
| **Freigabebedingungen** | Insolvenz des Anbieters, Einstellung des Geschäftsbetriebs, wesentliche Verletzung von Wartungspflichten oder Nichterbringung vertraglich vereinbarter Leistungen |
| **Verifizierung** | Hinterlegungen werden jährlich vom Escrow-Agenten überprüft (Build-Verifizierung — Bestätigung, dass der hinterlegte Code kompiliert und einen funktionierenden Build erzeugt) |

**Verifizierungskriterien für Hinterlegungen**:
- Quellcode kompiliert ohne Fehler mit der dokumentierten Build-Anleitung
- Alle Abhängigkeiten aus öffentlichen oder dokumentierten privaten Repositories auflösbar
- Build-Umgebungsspezifikationen enthalten alle erforderlichen Tools, SDKs und Versionen
- Das resultierende Build-Artefakt (Executable, Container-Image, deploybare Pakete) kann in einer Testumgebung eingesetzt werden
- Basis-Smoke-Test bestanden (Applikation startet, Health-Check-Endpoint antwortet)
- Keine proprietären Anbieter-eigenen Tools für den Build-Prozess erforderlich

Verifizierung wird jährlich vom Escrow-Agenten durchgeführt. Bei fehlgeschlagener Verifizierung muss der Anbieter die Hinterlegung innerhalb von 30 Tagen korrigieren.

Wenn die Organisation den Quellcode direkt in ihren eigenen Repositories hält, ist keine Code-Hinterlegung erforderlich, jedoch muss die Organisation eigene, verifizierte Backups pflegen.

---

## Laufendes Monitoring

Die Organisation überwacht ausgelagerte Entwicklungsaktivitäten kontinuierlich während des gesamten Auftragslebenszyklus.

**Monitoringaktivitäten**:

| Aktivität | Häufigkeit | Verantwortlich |
|-----------|-----------|----------------|
| **Überprüfung der Sicherheitstest-Berichte** | Pro Meilenstein oder Sprint-Lieferung | Development Manager |
| **Fortschritts- und Qualitätsüberprüfung** | Alle 2 Wochen oder pro Sprint (bei agilen Aufträgen) | Development Manager / Project Manager |
| **Überprüfung des Anbieter-Sicherheitsstatus** | Jährlich (Stufe 1); alle zwei Jahre (Stufe 2); bei Verlängerung (Stufe 3) | ISB / Information Security Manager |
| **Zugriffsüberprüfung** | Vierteljährlich — Verifizierung, dass Anbieterpersonal mit aktivem Zugriff diesen noch benötigt | IT Operations / Development Manager |
| **Compliance-Stichprobenprüfung** | Halbjährlich — Verifizierung der Einhaltung der sicheren Programmierstandards durch den Anbieter | Security Team |
| **Vorfalls- und Beinahe-Unfall-Überprüfung** | Pro Vorfall | ISB |

Eine Anbieter-Performance-Scorecard ist vierteljährlich zu führen, die folgende Punkte verfolgt: Compliance mit Sicherheitstests, SLA-Einhaltung, Vorfallsanzahl und Auditbefunde. Ergebnisse sind jährlich an das Management zu berichten.

**Eskalationsauslöser**:

| Auslöser | Massnahme |
|----------|-----------|
| Anbieter liefert Sicherheitsprüfberichte nicht innerhalb der vereinbarten Frist | Eskalation an Development Manager; Abnahme zurückhalten |
| Kritische Schwachstelle in vom Anbieter geliefertem Code identifiziert | Eskalation an ISB; Anbieterbehebung innerhalb von 7 Tagen |
| Sicherheitsvorfall beim Anbieter betrifft Daten oder Systeme der Organisation | Incident-Management-Prozess aktivieren (A.5.24-28); ISB innerhalb von 1 Stunde benachrichtigen |
| Anbieter besteht jährliche Sicherheits-Neubewertung nicht | Keine neuen Auftragserteilungen; Behebungsplan innerhalb von 30 Tagen; Vertragsüberprüfung |
| Nachweis nicht genehmigter Unterauftragsvergabe | Eskalation an ISB und Legal; Vertragsüberprüfung |

---

## Sicherheitsvorfallsreaktion beim Anbieter

Wenn ein Anbieter einen Sicherheitsvorfall erlebt, der den Auftrag der Organisation betrifft:

**Meldepflichten des Anbieters**:
- **Innerhalb von 24 Stunden**: Erstmeldung über Vorfall, Art und potenziellen Auswirkungen
- **Innerhalb von 72 Stunden**: Detaillierter Vorfallsbericht einschliesslich Umfang, vorläufige Ursachenanalyse, betroffene Systeme/Daten und Behebungsmassnahmen

**Reaktion der Organisation**:

| Vorfallstyp | Reaktionsmassnahmen |
|-------------|---------------------|
| **Kompromittierung des Anbieter-Code-Repositories** | 1. Anbieterzugriff auf Organsysteme aussetzen 2. Forensische Überprüfung des gesamten vom Anbieter gelieferten Codes 3. Vollständige Sicherheits-Neustests vor weiterer Abnahme 4. Code-Neuentwicklung erwägen, wenn Schadcode vermutet wird |
| **Diebstahl von Anbieterpersonal-Zugangsdaten** | 1. Alle Anbieterzugangsdaten sofort widerrufen 2. Zugriffsprotokolle auf unberechtigte Aktivitäten prüfen 3. Zugangsdaten nach Bestätigung der Behebung der Kompromittierung durch den Anbieter neu ausstellen 4. MFA obligatorisch für erneuten Zugriff |
| **Datenpanne beim Anbieter (Organisationsdaten betroffen)** | 1. Organisationseigenen Incident-Response-Prozess aktivieren 2. Meldepflichten gegenüber Datenschutzbehörden prüfen 3. Gemeinsame Vorfallsuntersuchung 4. Vertragsüberprüfung hinsichtlich Haftung und Behebungskosten |
| **Supply-Chain-Kompromittierung beim Anbieter** | 1. Abnahme von Lieferungen mit betroffener Komponente aussetzen 2. SBOM auf betroffene Abhängigkeit in allen Anbieterarbeiten prüfen 3. Anbieter zur Entfernung/Ersetzung der kompromittierten Komponente auffordern 4. Unabhängige Sicherheits-Neustests |

Der ISB benachrichtigt das Geschäftsleitung innerhalb von 24 Stunden über jeden Anbietervorfall, der Organisationsdaten oder -systeme betrifft.

**Massnahmen nach dem Vorfall**:
- Der Anbieter muss innerhalb von 30 Tagen einen Post-Incident-Bericht vorlegen
- Die Organisation führt eine Sicherheits-Neubewertung des Anbieters durch
- Vertragsfortsetzung abhängig von zufriedenstellender Behebung
- Schwerwiegende Vorfälle können die Vertragskündigungsklausel auslösen

---

## Datenschutzanforderungen

Wenn ausgelagerte Entwicklung den Zugriff auf Personendaten oder auf Systeme, die Personendaten verarbeiten, umfasst, gelten zusätzliche Datenschutzanforderungen.

**Auftragsverarbeitungsvertrag (AVV)**:

Gemäss schweizerischem nDSG Art. 9 schliesst die Organisation einen AVV mit dem Entwicklungsanbieter ab, der Folgendes regelt:

- Kategorien und Arten der verarbeiteten Personendaten.
- Zweck und Dauer der Verarbeitung.
- Pflicht zur Verarbeitung von Daten nur nach Weisung der Organisation.
- Vertraulichkeitspflichten für Anbieterpersonal.
- Technische und organisatorische Sicherheitsmassnahmen des Anbieters.
- Melde- und Genehmigungspflichten bei der Hinzuziehung von Subauftragsverarbeitern.
- Unterstützungspflichten bei Betroffenenrechten.
- Datenrückgabe und -löschung bei Vertragsende.
- Audit- und Inspektionsrechte.

**Grenzüberschreitende Datentransfers**:

Wenn die Entwicklung beim Anbieter ausserhalb der Schweiz stattfindet:

- Ein Transfer-Impact-Assessment ist gemäss den Anforderungen des schweizerischen nDSG durchzuführen.
- Es müssen geeignete Garantien vorhanden sein (z.B. Standardvertragsklauseln, Angemessenheitsentscheide des Bundesrats oder verbindliche Unternehmensregeln).
- Wenn der Anbieter Daten von Personen in der EU/EWR verarbeitet, sind ausserdem die Transfer-Anforderungen gemäss DSGVO Kapitel V einzuhalten.

**Datensparsamkeit bei der Entwicklung**:

- Anbieter dürfen keine produktiven Personendaten für Entwicklungs- oder Testzwecke erhalten.
- Wenn realistische Daten erforderlich sind, sind bereinigt, anonymisierte oder pseudonymisierte Daten zu verwenden.
- Synthetische Daten (künstlich generiert) sind der bevorzugte Ansatz.
- Jede Verwendung transformierter Personendaten ist vom Datenschutzbeauftragten oder ISB zu dokumentieren und zu genehmigen.

**Ansätze zur Generierung synthetischer Daten**:
- **Faker-Bibliotheken**: Realistische, aber fiktive Daten (Namen, Adressen, E-Mails) — geeignet für UI-Tests, Reporting-Entwicklung
- **Data-Masking-Tools**: Beibehaltung der Datenstruktur und referentiellen Integrität bei gleichzeitiger Verschleierung der Werte — geeignet für komplexe Schematests
- **Regelbasierte Generierung**: Erzeugung von Daten, die den Mustern und Verteilungen der Produktion entsprechen — geeignet für Performance-Tests
- **KI-generierte Daten**: ML-Modelle, die mit Produktionsdaten trainiert wurden, um statistisch ähnliche synthetische Datensätze zu erzeugen — geeignet für die Analytikentwicklung

Tool-Beispiele: Faker (Python/JavaScript), Mockaroo (webbasiert), Tonic.ai, Gretel.ai (Enterprise)

Wenn die Verwendung von Produktionsdaten absolut notwendig ist (komplexe Datenbeziehungen, seltene Randfälle), sind die Daten:
1. Auf die minimal erforderlichen Datensätze zu begrenzen (kein vollständiger Produktionsdump)
2. Gemäss nDSG Art. 5 zu anonymisieren oder zu pseudonymisieren
3. Vom Datenschutzbeauftragten mit dokumentierter Begründung zu genehmigen
4. Im Ruhezustand und bei der Übertragung in die Anbieterumgebung zu verschlüsseln
5. Innerhalb von 30 Tagen nach Abschluss der Entwicklung aus den Anbietersystemen zu löschen

**Meldepflicht gegenüber dem Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB)**:

Wenn ein Anbietervorfall zu einem hohen Risiko für Betroffene führt (nDSG Art. 24), meldet die Organisation dies dem EDÖB unverzüglich. Indikatoren für hohes Risiko umfassen:
- Unbefugter Zugriff auf besondere Kategorien von Personendaten (Art. 5 Abs. 2)
- Datenpanne mit mehr als 500 Betroffenen in der Schweiz
- Kompromittierung sensibler Personendaten (Gesundheit, Finanzen, Biometrie)
- Vorfall mit Daten aus systematischem Profiling oder automatisierter Entscheidungsfindung

Der AVV muss den Anbieter verpflichten, alle für die EDÖB-Meldung notwendigen Informationen innerhalb von 48 Stunden nach Entdeckung des Vorfalls bereitzustellen.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Abnahmetests** | Formale Verifizierung, dass ein Liefergegenstand die spezifizierten Anforderungen vor dem Deployment erfüllt |
| **Code-Hinterlegung (Escrow)** | Vereinbarung, bei der Quellcode bei einem unabhängigen Dritten hinterlegt wird, damit er der Organisation unter bestimmten Bedingungen zur Verfügung gestellt werden kann |
| **DAST** | Dynamic Application Security Testing — Analyse laufender Applikationen auf Sicherheitsschwachstellen |
| **AVV** | Auftragsverarbeitungsvertrag — Vertrag, der regelt, wie ein Auftragsverarbeiter Personendaten im Auftrag eines Verantwortlichen verarbeitet |
| **SAST** | Static Application Security Testing — Analyse des Quellcodes auf Sicherheitsschwachstellen ohne Codeausführung |
| **SBOM** | Software-Stückliste (Software Bill of Materials) — Inventar aller Software-Komponenten, Abhängigkeiten und ihrer Versionen |
| **SCA** | Software Composition Analysis — Identifizierung von Schwachstellen und Lizenzproblemen in Drittanbieter- und Open-Source-Abhängigkeiten |
| **Subauftragsverarbeiter** | Dritte, die vom Auftragsverarbeiter (Anbieter) beauftragt werden, Personendaten im Auftrag des Verantwortlichen (Organisation) zu verarbeiten |
| **Supply-Chain-Angriff** | Kompromittierung einer Software-Komponente, einer Abhängigkeit oder eines Entwicklungswerkzeugs, um schädlichen Code oder Schwachstellen in nachgelagerte Systeme einzubringen |
| **Stufe-1/2/3-Anbieter** | Anbieterrisikoklassifikation basierend auf der Sensitivität der entwickelten Systeme und der zugänglichen Daten |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung der Stufe-1-Sicherheitsbewertungen; Abnahmefreigabe für High-Risk-Applikationen; Ausnahmegenehmigungen; Eskalationsinstanz; jährliche Richtlinienüberprüfung |
| **Development Manager** | Koordination der Anbieterbeauftragung; Kommunikation der Sicherheitsanforderungen; Management von Code-Review und Abnahme; Überwachung der Anbieterlieferungen; Compliance-Berichterstattung |
| **Information Security Manager** | Verwaltung des Anbieter-Sicherheitsfragebogens; Compliance-Stichprobenprüfungen; Überwachung des Anbieter-Sicherheitsstatus; Koordination der Vorfallsuntersuchung |
| **Project Manager** | Tagesgeschäftliche Anbieterbeziehungen; Verfolgung von Liefermeilensteinen; Eskalation von Sicherheitsbedenken an den Development Manager |
| **Datenschutzbeauftragter / ISB** | AVV-Überprüfung und -Genehmigung; Beurteilungen grenzüberschreitender Transfers; Verifizierung der Datensparsamkeit; Koordination von Betroffenenrechten |
| **Legal / Procurement** | Vertragserstellung und -überprüfung; IP- und Lizenzbedingungen; NDA-Verwaltung; Versicherungsverifizierung; Koordination der Escrow-Vereinbarungen |
| **Security Team** | Unabhängige Sicherheitstests von Anbieterlieferungen; Koordination von Penetrationstests; Durchführung von SAST/DAST/SCA; Schwachstellentriage |
| **IT Operations** | Bereitstellung und Entzug von Anbieterzugriffen; Unterstützung bei Zugriffsüberprüfungen; Umgebungstrennung für Anbieterzugriffe |
| **Applikationsverantwortlicher** | Initiierung von Sicherheitsanforderungen; Abnahmefreigabe; Ausnahmeanträge; Budget für Sicherheitstests |

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlich | Häufigkeit | Aufbewahrung |
|---|----------|----------------|-----------|--------------|
| 1 | **Lieferantensicherheitsbewertungen** (Fragebögen, Auditberichte, Zertifizierungsnachweise, Bewertungsentscheide) | ISB / Information Security Manager | Pro Auftrag + jährliche Neubewertung (Stufe 1) | Dauer der Anbieterbeziehung + 3 Jahre |
| 2 | **Entwicklungsverträge mit Sicherheitsklauseln** (unterzeichnete Vereinbarungen, AVV, NDA, Escrow-Vereinbarungen) | Legal / Procurement | Pro Auftrag | Vertragslaufzeit + 7 Jahre |
| 3 | **Sicherheitsprüfberichte des Anbieters** (SAST-, SCA-, DAST-Ergebnisse, die vom Anbieter pro Meilenstein geliefert werden) | Development Manager | Pro Meilenstein oder Sprint-Lieferung | Applikationslebenszyklus + 3 Jahre |
| 4 | **Organisationseigene unabhängige Testergebnisse** (interner Code-Review, unabhängige SAST/SCA/DAST, Penetrationstest-Berichte) | Security Team / ISB | Pro Abnahme | Applikationslebenszyklus + 3 Jahre |
| 5 | **Abnahmebestätigungen** (Sicherheits-Abnahme-Checkliste, Freigabe mit Datum, Genehmiger, Bedingungen) | Development Manager | Pro Liefergegenstand | Applikationslebenszyklus + 3 Jahre |
| 6 | **Anbieterzugriffsaufzeichnungen** (Zugriffsgenehmigungen, vierteljährliche Reviews, Deprovisioning-Bestätigungen) | IT Operations / Development Manager | Pro Zugriffsereignis; vierteljährliche Reviews | Dauer der Anbieterbeziehung + 3 Jahre |
| 7 | **SBOM-Aufzeichnungen** (Software-Stückliste für jeden akzeptierten Liefergegenstand) | Development Manager | Pro Liefergegenstand | Applikationslebenszyklus + 3 Jahre |
| 8 | **Code-Hinterlegungs- und Verifizierungsaufzeichnungen** (Hinterlegungsbestätigungen, jährliche Build-Verifizierungsergebnisse) | Legal / Development Manager | Pro Hinterlegung + jährliche Verifizierung | Vertragslaufzeit + 3 Jahre |
| 9 | **Schwachstellenbehebungs-Tracking** (Anbieterbehebungsaufzeichnungen, SLA-Compliance, Abschlussnachweise) | Development Manager / Security Team | Pro Schwachstelle | 3 Jahre |
| 10 | **Anbieter-Monitoring-Aufzeichnungen** (Fortschrittsüberprüfungen, Compliance-Stichprobenprüfungen, Eskalationsaufzeichnungen) | Development Manager / ISB | Pro Überprüfungszyklus | Dauer der Anbieterbeziehung + 3 Jahre |
| 11 | **Datenschutzaufzeichnungen** (AVV, Transfer-Impact-Assessments, Datensparsamkeitsgenehmigungen) | Datenschutzbeauftragter / ISB | Pro Auftrag | Vertragslaufzeit + 10 Jahre (nDSG) |
| 12 | **Ausnahmeregister** (Ausnahmeanträge, Genehmigungen, kompensierende Kontrollen, vierteljährliche Reviews) | Information Security Manager | Pro Ausnahme; vierteljährliche Überprüfung | Ausnahmedauer + 3 Jahre |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheitsmanagement-Team verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, darunter unter anderem Lieferantensicherheitsbewertungsaufzeichnungen, Vertragsklauselaudits, Sicherheitsprüfberichte, Abnahmedokumente, Zugriffsüberprüfungen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Compliance-Kennzahlen**:

| Kennzahl | Ziel | Messhäufigkeit |
|----------|------|----------------|
| Anbieteraufträge mit abgeschlossener Sicherheitsbewertung vor Vertragsunterzeichnung | 100% | Pro Auftrag |
| Entwicklungsverträge mit allen obligatorischen Sicherheitsklauseln | 100% | Pro Auftrag |
| Ausgelagerte Liefergegenstände mit organisationsseitigem unabhängigem Sicherheitstest vor Abnahme | 100% | Pro Liefergegenstand |
| Vom Anbieter gemeldete Schwachstellen innerhalb der SLA behoben | >= 90% | Vierteljährlich |
| Anbieterzugriffsüberprüfungen termingerecht abgeschlossen | 100% | Vierteljährlich |
| Stufe-1-Anbieter mit aktueller Sicherheits-Neubewertung (innerhalb von 12 Monaten) | 100% | Jährlich |
| Code-Hinterlegungen aktuell (innerhalb der vereinbarten Frequenz) | 100% | Gemäss Hinterlegungsplan |

**Umgang mit Nichteinhaltung**: Ein Wert unter 70% bei einer beliebigen Kennzahl erfordert sofortige ISB-Eskalation und einen Massnahmenplan. Ein Wert zwischen 70-89% erfordert die Aufsicht durch den Information Security Manager mit monatlichen Überprüfungen bis zur Wiederherstellung. Ein Wert von 90% und mehr folgt dem standardmässigen vierteljährlichen Monitoring.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Information Security Manager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen und einem definierten Überprüfungsdatum (maximal 12 Monate). Ausnahmen sind dem Management Review Team zu berichten.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarisch belangt werden, bis hin zur Kündigung des Arbeitsverhältnisses. Anbieterseitige Nichteinhaltung wird durch vertragliche Rechtsmittel angegangen, einschliesslich Vertragsaussetzung oder -kündigung bei wesentlichen Sicherheitsverstössen.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen in den Auslagerungspraktiken und der Supply-Chain-Bedrohungslandschaft, neue Software-Supply-Chain-Angriffstechniken (Dependency Confusion, Typosquatting, CI/CD-Pipeline-Kompromittierung), regulatorische Änderungen bei Auftragsverarbeitungsverträgen und grenzüberschreitenden Transfers, Aktualisierungen des Lieferantenmanagement-Rahmens, Auditbefunde sowie Erkenntnisse aus Sicherheitsvorfällen im Zusammenhang mit ausgelagerter Entwicklung.

---

## Implementierungs-Checkliste (für Organisationen, die erstmals auslagern)

**Vor der Beauftragung des ersten Anbieters**:
- [ ] Vorlage für den Anbieter-Sicherheitsfragebogen erstellt
- [ ] Standardmässige Vertragsvorlage für ausgelagerte Entwicklung mit Sicherheitsklauseln ausgearbeitet (Legal-Überprüfung)
- [ ] AVV-Vorlage gemäss nDSG Art. 9 vorbereitet (DSB-Überprüfung)
- [ ] Sichere Programmierstandards dokumentiert und veröffentlicht
- [ ] SAST/SCA/DAST-Tools ausgewählt und betriebsbereit
- [ ] Vorlage für die Sicherheits-Abnahme-Checkliste erstellt
- [ ] Anbieterzugriff-Bereitstellungsprozess dokumentiert
- [ ] Escrow-Agent ausgewählt (sofern für Stufe 1 anwendbar)

**Pro Auftrag**:
- [ ] Anbieterstufe bestimmt und dokumentiert
- [ ] Sicherheitsbewertung abgeschlossen und genehmigt
- [ ] Vertrag mit Sicherheitsklauseln unterzeichnet
- [ ] AVV abgeschlossen (wenn Anbieter auf Personendaten zugreift)
- [ ] Sicheres Entwicklungspaket an Anbieter übergeben
- [ ] Hintergrundüberprüfungen des Anbieterpersonals verifiziert (Stufe 1)
- [ ] Anbieterzugriff nach dem Prinzip der minimalen Rechtevergabe bereitgestellt
- [ ] Sicherheitstest-Kadenz geplant (Meilenstein-/Sprint-Reviews)
- [ ] Abnahmekriterien dem Anbieter mitgeteilt
- [ ] Code-Repository oder Escrow-Vereinbarung eingerichtet

---

# Adressierte Bereiche des ISO 27001-Standards

Richtlinie für ausgelagerte Entwicklung — ISO 27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.19 Informationssicherheit in Lieferantenbeziehungen |
| Klausel 7.3 Bewusstsein | 5.20 Berücksichtigung von Informationssicherheit in Lieferantenvereinbarungen |
| | 5.21 Management der Informationssicherheit in der IKT-Lieferkette |
| | 5.22 Überwachung, Überprüfung und Change Management von Lieferantendienstleistungen |
| | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| | 6.3 Sensibilisierung, Schulung und Training zur Informationssicherheit |
| | 6.4 Disziplinarverfahren |
| | 8.4 Zugriff auf Quellcode |
| | 8.25 Sicherer Entwicklungslebenszyklus |
| | 8.26 Applikationssicherheitsanforderungen |
| | 8.28 Sicheres Coding |
| | 8.29 Sicherheitstests in Entwicklung und Abnahme |
| | **8.30 Ausgelagerte Entwicklung** |
| | 8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|----------|
| Schweizerischer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen zum Datenschutz; Art. 9 — Datenverarbeitung durch Dritte (Auftragsverarbeitungsverträge) |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1-3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (sofern anwendbar) | Art. 28 — Pflichten des Auftragsverarbeiters; Art. 32 — Sicherheit der Verarbeitung; Kapitel V — Grenzüberschreitende Datentransfers |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.30 — Ausgelagerte Entwicklung |
| ISO/IEC 27002:2022 | Abschnitt 8.30 — Implementierungsleitfaden für ausgelagerte Entwicklung |
| NIST SP 800-53 Rev 5 | SA-4 (Acquisition Process), SA-9 (External System Services) |
| OWASP Top 10:2025 | A03 — Software Supply Chain Failures |
| CIS Controls v8 | 16.4 (Third-Party Software Component Inventory), 16.6 (Severity Rating for Application Vulnerabilities) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
