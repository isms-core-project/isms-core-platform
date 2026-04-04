<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.8-DE:operational:OP-POL:a.5.8 -->
**ISMS-OP-POL-A.5.8 — Informationssicherheit im Projektmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationssicherheit im Projektmanagement |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.8 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
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

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.5.8 — Information security in project management
- ISO/IEC 27002:2022 Section 5.8 — Umsetzungshinweise
- ISO 21500:2021 — Projekt-, Programm- und Portfoliomanagement
- Swiss nFADP (revDSG) Art. 22 — Datenschutz-Folgenabschätzung
- NIST SP 800-53 Rev 5 SA-3 — System Development Life Cycle
- NIST SP 800-53 Rev 5 PL-2 — System Security and Privacy Plans

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zur Informationssicherheit im Projektmanagement |
|-----------|-------------------------------------------------------|
| A.5.1 Richtlinien für Informationssicherheit | Übergeordneter Richtlinienrahmen als Baseline für Sicherheitsanforderungen in Projekten |
| A.5.7 Bedrohungsintelligenz | Bedrohungsintelligenz informiert projektspezifische Risikobeurteilung und Bedrohungsmodellierung |
| A.5.9 Inventar von Informationen und anderen Assets | Projekte erstellen neue Assets, die bei der Übergabe zu registrieren sind |
| A.5.12 Informationsklassifizierung | Datenklassifizierung bestimmt Projektsicherheitsklassifizierung und Kontrollauswahl |
| A.5.19 Informationssicherheit in Lieferantenbeziehungen | Anbieter-Sicherheitsanforderungen gelten für Projekte mit externen Anbietern |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | DSFA-Anforderungen für Projekte, die personenbezogene Daten verarbeiten |
| A.8.25 Sicherer Entwicklungslebenszyklus | Anforderungen an die sichere Entwicklung für Softwareprojekte |
| A.8.26 Anwendungssicherheitsanforderungen | Identifizierung von Sicherheitsanforderungen für Anwendungsprojekte |
| A.8.27 Sichere Systemarchitektur und Engineering-Prinzipien | Architektursicherheit für Infrastruktur- und Systemprojekte |
| A.8.29 Sicherheitstests in Entwicklung und Abnahme | In Phasentore integrierte Sicherheitstestanforderungen |
| A.8.32 Änderungsmanagement | Änderungskontrollprozess für projektinitiierte Änderungen in der Produktion |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Richtlinie zur Sicherheit in Lieferantenbeziehungen
- Richtlinie zum sicheren Entwicklungslebenszyklus
- Änderungsmanagement-Richtlinie
- Datenschutz- und PII-Schutz-Richtlinie
- Risikomanagement-Richtlinie

---

# Richtlinie zur Informationssicherheit im Projektmanagement

## Zweck

Der Zweck dieser Richtlinie ist es, sicherzustellen, dass Informationssicherheitsrisiken im Zusammenhang mit Projekten und Projektliefergegenständen systematisch über den gesamten Projektlebenszyklus hinweg identifiziert, bewertet und behandelt werden. Informationssicherheit muss in das Projektmanagement integriert werden, damit sie Teil jedes Projekts ist — kein nachträglicher Gedanke am Ende.

Projekte führen Veränderungen ein. Veränderungen führen Risiken ein. Ob es sich um eine neue Softwareanwendung, ein Infrastruktur-Upgrade, eine Anbieterbeschaffung oder ein Business-Process-Redesign handelt — jedes Projekt schafft Möglichkeiten, dass Sicherheitskontrollen geschwächt, umgangen oder weggelassen werden, es sei denn, Sicherheit wird in jeder Phase explizit adressiert.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG), indem sie organisatorische Massnahmen proportional zum Risiko zum Schutz personenbezogener Daten während Projektaktivitäten umsetzt, einschliesslich der Anforderung für Datenschutz-Folgenabschätzungen (DSFA) nach Art. 22, wo die Verarbeitung wahrscheinlich zu hohem Risiko für Persönlichkeit oder Grundrechte von Personen führt. Wo die Organisation Daten natürlicher Personen im EU/EWR-Raum verarbeitet, gelten auch DSGVO Art. 25 (Datenschutz durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen) und Art. 35 (DSFA).

## Geltungsbereich

Alle von der Organisation durchgeführten Projekte, unabhängig von Typ, Methodik, Grösse oder Dauer. Dies umfasst:

- Softwareentwicklungsprojekte (intern und ausgelagert).
- System-Implementierungs- und Integrationsprojekte.
- Infrastruktur-Bereitstellungs- und Migrationsprojekte (On-Premises und Cloud).
- IT-Beschaffungsprojekte (Hardware, Software, SaaS-Dienste).
- Business-Process-Redesign-Projekte mit Informationssicherheitsimplikationen.
- Compliance- und regulatorische Umsetzungsprojekte.
- Fusions-, Akquisitions- oder Veräusserungsprojekte mit IT-Assets oder Daten.

**Nicht im Geltungsbereich**: Routinemässige operative Tätigkeiten, die kein Projekt darstellen (betrieblicher Unterhalt und Support); Notfall-Reaktionsaktivitäten (abgedeckt unter der Vorfallsmanagement-Richtlinie); geringfügige Änderungen, die über den Standard-Änderungskontrollprozess verwaltet werden (abgedeckt unter der Änderungsmanagement-Richtlinie). Wo Unklarheit besteht, ob eine Aktivität ein Projekt darstellt, berät der ISB oder der Informationssicherheitsbeauftragte.

## Grundsatz

Informationssicherheit sollte in das Projektmanagement integriert werden. Sicherheitsanforderungen müssen früh — bei der Projektinitiierung — identifiziert und proportional über den gesamten Projektlebenszyklus hinweg entsprechend der Sicherheitsrisikoklassifizierung des Projekts adressiert werden. Kein Projekt darf ohne angemessene Sicherheitsvalidierung für seine Klassifizierungsstufe in die Produktionsbereitstellung übergehen.

Alle Projektsicherheitsentscheidungen müssen risikobasiert sein und die Sensitivität und Klassifizierung der beteiligten Daten, die Kritikalität der betroffenen Systeme, das regulatorische Umfeld und das Potenzial für geschäftliche Auswirkungen bei unzureichender Sicherheit berücksichtigen.

---

## Projektklassifizierung

Alle Projekte müssen nach Informationssicherheitsrisiken klassifiziert werden, um proportionale Sicherheitsanforderungen zu bestimmen. Die Klassifizierung muss bei der Projektinitiierung erfolgen und im Projektauftrag oder einem gleichwertigen Initiierungsdokument dokumentiert werden.

### Klassifizierungsfaktoren

Projekte müssen basierend auf dem **höchsten anwendbaren Faktor** über folgende Dimensionen hinweg klassifiziert werden:

| Faktor | Hohes Risiko | Mittleres Risiko | Niedriges Risiko |
|--------|-------------|-----------------|-----------------|
| **Datensensitivität** | Vertrauliche oder eingeschränkte Daten (PII, Finanzdaten, geistiges Eigentum, Geschäftsgeheimnisse) | Interne Daten (nicht öffentliche Geschäftsinformationen, Mitarbeiterdaten) | Öffentliche Daten (Marketinginhalt, veröffentlichte Dokumentation) |
| **Systemkritikalität** | Geschäftskritisches System (RTO < 4 Stunden); umsatzgenerierend oder kundenorientiert | Geschäftswichtiges System (RTO 4-24 Stunden); interner Betrieb | Unterstützungssystem (RTO > 24 Stunden); nicht kritische Tools |
| **Regulatorischer Geltungsbereich** | nDSG Hochrisikoverarbeitung, DSGVO Art. 35 DSFA erforderlich, PCI DSS anwendbar | nDSG Standardverarbeitung anwendbar | Keine regulierte Datenverarbeitung |
| **Externe Exposition** | Internetzugang oder für externe Parteien zugänglich (Kunden, Partner, Öffentlichkeit) | Kontrollierter externer Zugriff (VPN, dedizierte Verbindung) | Nur interner Zugriff |
| **Beteiligung Dritter** | Kritische Funktion ausgelagert (Hosting, Authentifizierung, Zahlungsverarbeitung) | Von Anbieter verwaltete Komponenten (SaaS-Integration, Managed Services) | Vollständig interne Lieferung |

**Klassifizierungsregel**: Wenn **ein einziger Faktor** die Kriterien für hohes Risiko erfüllt, muss das Projekt als **Hohes Risiko** klassifiziert werden. Wenn ein Faktor mittleres Risiko erfüllt (und kein Faktor hohes Risiko ist), als **Mittleres Risiko** klassifizieren. Nur wenn **alle Faktoren** niedriges Risiko aufweisen, darf das Projekt als **Niedriges Risiko** klassifiziert werden.

### Klassifizierungsbeispiele

Zur Unterstützung konsistenter Klassifizierungsentscheidungen illustrieren folgende Beispiele typische Projektszenarien nach Klassifizierungsstufe:

| Faktor | Beispiel Hohes Risiko | Beispiel Mittleres Risiko | Beispiel Niedriges Risiko |
|--------|----------------------|--------------------------|--------------------------|
| **Datensensitivität** | Kreditkartendaten von Kunden, Gesundheitsdaten von Mitarbeitenden | E-Mail-Adressen von Mitarbeitenden, interne Finanzberichte | Marketingbroschüren, öffentliche Dokumentation |
| **Systemkritikalität** | Zahlungsabwicklungssystem (RTO < 1 Stunde) | Internes CRM (RTO 8 Stunden) | Testumgebung, Proof-of-Concept-System |
| **Regulatorischer Geltungsbereich** | DSGVO Art. 35 DSFA erforderlich (Profiling), PCI DSS Level 1 | Schweizerisches nDSG anwendbar (Standard-Personendaten) | Keine regulierten Daten |
| **Externe Exposition** | Öffentliche Website, kundenorientierte API | Partner-Extranet, nur VPN-Zugriff | Nur internes LAN |
| **Beteiligung Dritter** | Cloud-gehosteter Zahlungsabwickler, Authentifizierungs-SaaS | AWS-gehostet mit Organisationsverwaltung, Office 365 | Vollständig intern, On-Premises |

### Klassifizierungsgenehmigung

| Klassifizierung | Genehmigungsbefugnis |
|----------------|---------------------|
| **Hohes Risiko** | ISB-Genehmigung erforderlich |
| **Mittleres Risiko** | Genehmigung des Informationssicherheitsbeauftragten |
| **Niedriges Risiko** | Projektleiter klassifiziert selbst; Informationssicherheitsbeauftragter bestätigt |

Die Klassifizierung muss an jedem Phasentor überprüft werden. Wenn sich Projektumfang, Datensensitivität oder externe Exposition wesentlich ändert, muss die Klassifizierung aktualisiert und neu genehmigt werden.

### Sicherheitsbudget-Hinweise

Projektleiter müssen Sicherheitskosten basierend auf der Projektklassifizierung bei der Budgeterstellung schätzen:

| Klassifizierung | Typische Sicherheitskosten | Enthaltene Aktivitäten |
|----------------|---------------------------|------------------------|
| **Hohes Risiko** | 8–12% der Gesamtprojektkosten | Bedrohungsmodellierung, Sicherheitsarchitektur-Review, Penetrationstesting, Sicherheits-Code-Review, Zeit des Informationssicherheitsbeauftragten |
| **Mittleres Risiko** | 4–6% der Gesamtprojektkosten | Sicherheitsanforderungsanalyse, Schwachstellen-Scanning, funktionale Sicherheitstests, Zeit des Informationssicherheitsbeauftragten |
| **Niedriges Risiko** | 1–2% der Gesamtprojektkosten | Sicherheitschecklisten-Review, grundlegendes Schwachstellen-Scanning |

Sicherheitsbudgetschätzungen müssen in die Projektinitiierungsdokumentation aufgenommen und als Teil des Projektbudgets genehmigt werden. Wo tatsächliche Sicherheitskosten voraussichtlich den geschätzten Bereich überschreiten, muss der Projektleiter den Informationssicherheitsbeauftragten benachrichtigen und das Projektbudget entsprechend anpassen.

---

## Identifizierung von Sicherheitsanforderungen

Sicherheitsanforderungen für Projektliefergegenstände müssen systematisch während der Planungsphase identifiziert werden, basierend auf der Klassifizierung des Projekts und den Kategorien der beteiligten Assets und Daten.

### Anforderungskategorien

Der Projektleiter muss mit Unterstützung des Informationssicherheitsbeauftragten jede der folgenden Anforderungskategorien gegen den Projektumfang bewerten:

| Anforderungskategorie | Anwendbar wenn | Quelle |
|----------------------|----------------|--------|
| **Zugangskontrolle** | Alle Projekte (Mindest-Baseline) | Identity- und Zugangsverwaltungs-Richtlinie |
| **Datenschutz und Verschlüsselung** | Projekt umfasst vertrauliche oder eingeschränkte Daten | Kryptographie-Richtlinie, nDSG Art. 8 |
| **Anwendungssicherheit** | Projekt umfasst Softwareentwicklung oder benutzerdefinierten Code | Richtlinie zum sicheren Entwicklungslebenszyklus |
| **Infrastruktursicherheit** | Projekt setzt Netzwerkinfrastruktur ein oder ändert diese | Netzwerksicherheits-Richtlinie |
| **Anbieter-Sicherheit** | Projekt umfasst externe Anbieter oder Cloud-Dienste | Richtlinie zur Sicherheit in Lieferantenbeziehungen |
| **Datenschutz und PII** | Projekt verarbeitet personenbezogene Daten | Datenschutz- und PII-Richtlinie, nDSG Art. 22 |
| **Geschäftskontinuität** | Projekt betrifft geschäftskritische Systeme | Richtlinie zur Geschäftskontinuität und Notfallwiederherstellung |
| **Protokollierung und Überwachung** | Projekt setzt Systeme ein, die Sicherheitsüberwachung erfordern | Protokollierungs-Richtlinie |

### Quellzuordnung der Anforderungen

Die folgende Referenztabelle zeigt, welche Richtlinienbereiche typischerweise auf häufige Projekttypen anwendbar sind, um Projektleitern bei der Identifizierung anwendbarer Anforderungen zu helfen:

| Projekttyp | Immer anwendbar | Häufig anwendbar | Bedingt anwendbar |
|------------|-----------------|------------------|-------------------|
| **Softwareentwicklung** | Sicherer Entwicklungslebenszyklus, Zugangskontrolle, Protokollierung | Anwendungssicherheit, Datenschutz, Änderungsmanagement | Datenschutz und PII (bei Personendaten), Anbieter-Sicherheit (bei Auslagerung) |
| **Infrastrukturbereitstellung** | Zugangskontrolle, Netzwerksicherheit, Protokollierung | Konfigurationsmanagement, Geschäftskontinuität | Anbieter-Sicherheit (bei vom Anbieter verwalteten Diensten) |
| **SaaS-Beschaffung** | Anbieter-Sicherheit, Zugangskontrolle | Datenschutz, Datenschutz und PII | Anwendungssicherheit (bei benutzerdefinierter Integration) |

### Dokumentation

- **Hochrisiko- und Mittelrisiko-Projekte**: Sicherheitsanforderungen müssen in einem Sicherheitsanforderungsregister (oder einem entsprechenden Abschnitt in [Projektmanagement-Tool]) dokumentiert und bis zur Umsetzung und zum Test verfolgt werden.
- **Niedrigrisiko-Projekte**: Sicherheitsanforderungen müssen als Risikominderungsposten im Projektrisikoregister mit Bestätigung der anwendbaren Richtlinienkonformität dokumentiert werden.

### Genehmigung

- **Hohes Risiko**: ISB genehmigt Sicherheitsanforderungen vor der Ausführungsphase.
- **Mittleres Risiko**: Informationssicherheitsbeauftragter genehmigt vor der Ausführungsphase.
- **Niedriges Risiko**: Informationssicherheitsbeauftragter bestätigt Vollständigkeit der Anforderungen.

---

## Phasentor-Sicherheitsreviews

Sicherheitsreviews müssen in die Projektsteuerung an folgenden Phasentoren integriert werden. Projekte dürfen nicht zur nächsten Phase übergehen, bis Sicherheitskriterien für das aktuelle Phasentor erfüllt oder formal von der zuständigen Behörde akzeptiert wurden.

### Phasentor-Anforderungen

| Phasentor | Erforderliche Sicherheitsaktivitäten |
|-----------|--------------------------------------|
| **Initiierung / Projektgenehmigung** | Sicherheitsrisikoklassifizierung bestimmt und genehmigt; erste Sicherheitsrisiken im Projektrisikoregister identifiziert; Sicherheitsbudget und Ressourcenanforderungen geschätzt; DSFA-Screening abgeschlossen (siehe DSFA-Integration) |
| **Planung / Design-Genehmigung** | Sicherheitsanforderungen dokumentiert, überprüft und genehmigt; Bedrohungsmodell für Hochrisikoprojekte abgeschlossen (empfohlen für mittleres Risiko); Sicherheitsarchitektur für Hochrisikoprojekte überprüft; DSFA abgeschlossen wo Screening hohes Risiko angezeigt hat |
| **Ausführung / Build-Checkpoint** | Sicherheitstests gemäss Klassifizierungsanforderungen durchgeführt; Sicherheitsbefunde gemäss Schweregrad-Zielen verfolgt und behoben; Sicherheitsanforderungen zu Umsetzungsnachweisen rückverfolgt |
| **Bereitstellung / Go-Live-Genehmigung** | Alle Kritisch-Befunde behoben; Hoch-Befunde gemäss Klassifizierungszielen behoben (siehe Abschnitt Sicherheitstests); Sicherheitsübergabedokumentation vollständig und von Betrieb akzeptiert; Restrisiken formal dokumentiert und von zuständiger Behörde akzeptiert |
| **Abschluss** | Lessons Learned erfasst (obligatorisch für hohes/mittleres Risiko); neue Assets im Asset-Inventar registriert; Restrisiken in operatives Risikoregister übertragen; Projektsicherheitsdokumentation gemäss Records-Management-Anforderungen archiviert |

### Eskalationsfristen

Sicherheitsbedenken an Phasentoren müssen innerhalb folgender Fristen eskaliert werden:

- **2 Arbeitstage** für Hochrisikoprojekte.
- **5 Arbeitstage** für Mittelrisikoprojekte.

**Eskalationspfad**: Projektleiter -> Informationssicherheitsbeauftragter -> ISB -> Geschäftsleitung.

Projekte dürfen nicht ohne Lösung kritischer Sicherheitsbedenken zur nächsten Phase übergehen. Hohe Sicherheitsbedenken können mit formaler Risikoakzeptanz durch die zuständige Behörde voranschreiten. Mittlere und niedrige Bedenken können mit einem dokumentierten Massnahmenplan voranschreiten.

---

## Sicherheitstests nach Klassifizierung

Alle Projekte müssen Sicherheitstests proportional zu ihrer Klassifizierungsstufe einschliessen. Tests müssen vor der Bereitstellung abgeschlossen und die Ergebnisse dokumentiert werden.

### Testanforderungen

| Anforderung | Hohes Risiko | Mittleres Risiko | Niedriges Risiko |
|-------------|-------------|-----------------|-----------------|
| **Externer Penetrationstest** | Obligatorisch (unabhängige Drittpartei, OWASP-Methodik oder gleichwertig) | Erforderlich bei Internetexposition oder regulierten Daten; sonst empfohlen | Nicht erforderlich |
| **Automatisiertes Schwachstellen-Scanning** | Obligatorisch (wöchentlich während Entwicklung + abschliessend vor Bereitstellung) | Obligatorisch (abschliessendes Scan vor Bereitstellung) | Empfohlen |
| **Sicherheits-Code-Review** | Obligatorisch für benutzerdefinierten Code (mindestens: Authentifizierung, Autorisierung, Datenschutz, kryptographische Funktionen) | Empfohlen für benutzerdefinierten Code | Nicht erforderlich |
| **Funktionale Sicherheitstests** | Obligatorisch (Authentifizierung, Autorisierung, Eingabevalidierung, Fehlerbehandlung, Session-Management) | Obligatorisch (Authentifizierung, Autorisierung, Datenvalidierung, Fehlerbehandlung) | Sicherheitsvalidierung gegen Anforderungs-Checkliste |

### Behebungsziele vor der Bereitstellung

| Befundschweregrad | Hochrisikoprojekte | Mittelrisikoprojekte | Niedrigrisikoprojekte |
|-------------------|-------------------|---------------------|----------------------|
| **Kritisch** | 100% behoben | 100% behoben | 100% behoben |
| **Hoch** | >=80% behoben | >=70% behoben | Best Effort; risikoakzeptiert |
| **Mittel** | Verfolgt; Massnahmenplan | Verfolgt; Massnahmenplan | Verfolgt |
| **Niedrig** | Dokumentiert | Dokumentiert | Dokumentiert |

Wenn Behebungsziele nicht vor dem Bereitstellungstermin erreicht werden können, muss Restrisiko gemäss dem Abschnitt Ausnahmemanagement dieser Richtlinie formal akzeptiert werden.

Testnachweise (Scan-Berichte, Penetrationstest-Berichte, Code-Review-Befunde) müssen gemäss Records-Management-Anforderungen archiviert werden.

---

## Sicherheitsübergabe und -abnahme

Bei Projektabschluss muss Sicherheitsübergabedokumentation dem Betriebsteam bereitgestellt und als vollständig validiert werden, bevor das Projekt formal abgeschlossen wird. Unvollständige Sicherheitsübergabe blockiert den Projektabschluss.

### Übergabedokumentation

Das Sicherheitsübergabepaket muss folgendes umfassen:

1. **Sicherheitsarchitektur-Dokumentation** — Systemsicherheitsdesign, Vertrauensgrenzen, Authentifizierungs- und Autorisierungsmodell, Verschlüsselungsimplementierung, Datenflussdiagramme mit Klassifizierung, Netzwerkarchitektur und Segmentierung.

2. **Operative Sicherheitsverfahren** — Überwachungsanforderungen (Protokollquellen, Warnschwellenwerte, [SIEM]-Integration), Sicherungs- und Wiederherstellungsverfahren, Ansatz zum Sicherheits-Patch-Management, Eskalationspfade für die Vorfallsreaktion.

3. **Akzeptierte Restrisiken** — formale Risikoakzeptanzunterlagen mit Genehmigungsunterschriften, Ausgleichskontrollen wo anwendbar, Zeitplan zur erneuten Risikobewertung für zeitlich begrenzte Akzeptanzen.

4. **Sicherheitstest-Nachweise** — abschliessender Schwachstellen-Scan-Bericht (datiert innerhalb von 7 Tagen nach Bereitstellung), Penetrationstest-Bericht (falls anwendbar), Behebungsnachweise für Kritisch- und Hoch-Befunde.

### Übergabeabnahme

Der operative Eigentümer muss die Vollständigkeit der Übergabe über eine unterzeichnete Sicherheitsübergabe-Checkliste bestätigen, bevor der Projektleiter die Projektabschlussgenehmigung beantragt. Für Hochrisikoprojekte muss der ISB die Übergabe zusätzlich genehmigen.

Nach Übergabeabnahme muss der Projektleiter sicherstellen:
- Neue Assets werden im Asset-Inventar registriert.
- Restrisiken werden in das operative Risikoregister übertragen.
- Sicherheitsdokumentation wird gemäss Records-Management-Anforderungen archiviert.

---

## Projektsicherheitsrollen

### RACI-Matrix

| Aktivität | Projektleiter | InfoSec-Beauftragter | ISB | Business Owner | Technical Lead |
|-----------|:-:|:-:|:-:|:-:|:-:|
| Projektsicherheitsklassifizierung | V | A | I | B | B |
| Identifizierung von Sicherheitsanforderungen | V | A | I | B | B |
| Sicherheitsarchitektur-Design | B | B | I | I | V/A |
| Sicherheitstest-Durchführung | V | B | I | I | V |
| Risikoakzeptanz für Restrisiken | I | B | A (Hoch) | A (Mittel/Niedrig) | I |
| Sicherheitsübergabe an Betrieb | V | A | I | B | B |
| Lessons Learned | V | B | I | B | B |

V = Verantwortlich (erledigt die Arbeit), A = Accountable (letzte Entscheidung), B = Beratend (Input erforderlich), I = Informiert (auf dem Laufenden gehalten).

### Rollenbeschreibungen

| Rolle | Hauptverantwortlichkeiten |
|-------|--------------------------|
| **Geschäftsleitung** | Diese Richtlinie genehmigen; Restrisiken für kritische Projekte akzeptieren; Ressourcen für Projektsicherheit sicherstellen |
| **ISB** | Hochrisiko-Klassifizierungen genehmigen; Restrisiken für Hochrisikoprojekte akzeptieren; Projekte mit inakzeptablem Sicherheitsrisiko stoppen; Projektsicherheitsmetriken überwachen |
| **Informationssicherheitsbeauftragter** | Projektteams bei Risikobeurteilung und Anforderungen unterstützen; Mittelrisiko-Klassifizierungen genehmigen; Angemessenheit von Sicherheitstests überprüfen; Sicherheitsanforderungsvorlagen pflegen |
| **Projektleiter** | Projektsicherheitsrisiko klassifizieren; Sicherheitsaktivitäten planen und budgetieren; Sicherheitsaktivitäten an jedem Phasentor durchführen; Projektsicherheitsrisikoregister pflegen; Sicherheitsübergabedokumentation erstellen |
| **Business Owner / Product Owner** | Geschäftliche Sicherheitsanforderungen definieren; an Risikobeurteilung teilnehmen; Restrisiken für eigene Systeme akzeptieren (Mittel/Niedrig) |
| **Technical Lead / Solution Architect** | Sicherheitskontrollen in Lösungsarchitektur einbauen; Sicherheitsanforderungen umsetzen; Bedrohungsmodellierung unterstützen; Sicherheitsbefunde adressieren |
| **Drittanbieter** | Vertragliche Sicherheitsanforderungen einhalten; an Sicherheitsbewertungen teilnehmen; Sicherheitsvorfälle oder Schwachstellen melden |

### Security Champions (Optional)

Organisationen mit 50 oder mehr Mitarbeitenden sollten die Ernennung von Security Champions in Projektteams erwägen, um die Sicherheitsintegration zu verbessern und Engpässe beim Informationssicherheitsbeauftragten zu reduzieren:

| Aspekt | Beschreibung |
|--------|-------------|
| **Auswahl** | Ausgebildetes Teammitglied (Entwickler, Business Analyst oder Projektleiter), das als Sicherheits-Liaison im Projektteam fungiert |
| **Schulung** | Security Champions müssen Sicherheitsschulungen absolvieren (mindestens 8 Stunden pro Jahr) zu sicheren Entwicklungspraktiken, Bedrohungsidentifikation und organisatorischen Sicherheitsrichtlinien |
| **Verantwortlichkeiten** | Sicherheitsanforderungen während der Planung identifizieren; für Sicherheit im Projektteam eintreten; Sicherheitsbedenken an den Informationssicherheitsbeauftragten eskalieren; Sicherheitstestkoordination unterstützen |
| **Vorteile** | Reduziert Engpass beim Informationssicherheitsbeauftragten; baut Sicherheitsbewusstsein in der Organisation auf; schafft in Projektteams eingebettete Sicherheitsfürsprecher |

Der Informationssicherheitsbeauftragte koordiniert das Security-Champion-Programm einschliesslich Auswahlkriterien, Schulungsinhalt und laufender Unterstützung.

---

## DSFA-Integration

Wo ein Projekt die Verarbeitung personenbezogener Daten umfasst, muss eine Datenschutz-Folgenabschätzungs (DSFA)-Prüfung bei der Projektinitiierung durchgeführt werden, um zu bestimmen, ob eine vollständige DSFA erforderlich ist.

### DSFA-Screening

Ein DSFA-Screening muss für jedes Projekt durchgeführt werden, das personenbezogene Daten verarbeitet. Das Screening muss bewerten, ob die geplante Verarbeitung wahrscheinlich zu einem hohen Risiko für die Persönlichkeit oder Grundrechte von Personen führt, wie es das schweizerische nDSG Art. 22 verlangt.

**Eine DSFA ist obligatorisch, wenn das Projekt folgendes umfasst:**

- Umfassende Verarbeitung sensibler Personendaten (Gesundheitsdaten, biometrische Daten, politische Meinungen, religiöse Überzeugungen, Strafregistereinträge oder Sozialhilfemassnahmen gemäss nDSG Art. 5).
- Systematische und umfassende Überwachung von Personen (einschliesslich Profiling gemäss nDSG Art. 5 lit. f).
- Einsatz neuer Technologie, wo die Datenschutzauswirkungen ungewiss sind.
- Grossmassstäbliche automatisierte Entscheidungsfindung mit erheblichen Auswirkungen auf Personen.
- Kombination oder Zusammenführung von Datensätzen aus verschiedenen Quellen auf eine Weise, die Personen vernünftigerweise nicht erwarten würden.

### DSFA-Zeitplanung

- **Screening**: Bei Projektinitiierung abgeschlossen (vor dem Planungsphasentor).
- **Vollständige DSFA** (wo erforderlich): Während der Planungsphase abgeschlossen, vor dem Ausführungsphasentor.
- **DSFA-Aktualisierung**: Erforderlich, wenn sich Projektumfang, Datenverarbeitung oder Technologie während der Ausführung wesentlich ändert.

### DSFA-Genehmigung

Die abgeschlossene DSFA muss vom Datenschutzbeauftragten (oder ISB, wo kein DSB ernannt ist) überprüft und genehmigt werden, bevor das Projekt zur Ausführung übergeht. Wo die DSFA verbleibende hohe Risiken identifiziert, die nicht gemindert werden können, muss die Organisation vor dem Voranschreiten den Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB) konsultieren, wie es nDSG Art. 23 verlangt.

---

## Agile und iterative Projektintegration

Für Projekte, die Agile, Scrum oder andere iterative Methoden verwenden, muss Sicherheit in den iterativen Prozess integriert werden, anstatt bis zum Ende aufgeschoben zu werden.

### Sicherheit in der iterativen Entwicklung

| Agile-Aktivität | Sicherheitsintegration |
|----------------|------------------------|
| **Backlog-Pflege** | Sicherheits-Stories und Sicherheits-Abnahmekriterien werden zu User Stories hinzugefügt, die sensible Daten, Authentifizierung, Autorisierung oder externe Schnittstellen betreffen |
| **Sprint-Planung** | Sicherheitsaufgaben werden geschätzt und in die Sprint-Kapazität aufgenommen; Sicherheits-Stories werden neben Geschäftsfunktionen priorisiert |
| **Sprint-Ausführung** | Automatisierte Sicherheitstests (SAST, Abhängigkeits-Scanning) in CI/CD-Pipeline integriert; Sicherheitsbefunde werden als Fehler behandelt und im Sprint-Backlog verfolgt |
| **Sprint-Review** | Sicherheitsstatus wird zusammen mit dem Funktionsfortschritt gemeldet; Sicherheitsschulden werden verfolgt und priorisiert |
| **Release-Planung** | Sicherheitstestanforderungen (Penetrationstesting, Schwachstellen-Scanning) werden vor dem Produktions-Release gemäss Klassifizierungsanforderungen geplant |

### Sicherheits-Checkpoints für iterative Projekte

Statt einzelner Phasentore müssen iterative Projekte Sicherheits-Checkpoints an folgenden Punkten implementieren:

- **Projektinitiierung**: Sicherheitsklassifizierung, DSFA-Screening und erstes Bedrohungsmodell (gleich wie traditionelle Projekte).
- **Architektur-Sprint / Sprint 0**: Sicherheitsarchitektur-Review; Sicherheitsanforderungs-Baseline festgelegt.
- **Jeder Release-Kandidat**: Ergebnisse automatisierter Sicherheitsscans überprüft; manuelle Sicherheitstests für Produktions-Releases.
- **Produktions-Release**: Vollständige Sicherheitstests gemäss Klassifizierungsanforderungen; Sicherheitsübergabe aktualisiert.
- **Projektabschluss**: Abschliessende Lessons Learned; Restrisiken an Betrieb übertragen.

---

## Sicherheit bei Beschaffungsprojekten

Projekte, die die Beschaffung von IT-Systemen, Software oder Dienstleistungen umfassen, müssen Informationssicherheitsanforderungen in den Beschaffungsprozess einbeziehen.

### Beschaffungs-Sicherheitsanforderungen

- **Anbieter-Sicherheitsbewertung**: Anbieter müssen gegen die Anbieter-Sicherheitsanforderungen der Organisation (gemäss der Richtlinie zur Sicherheit in Lieferantenbeziehungen) vor der Auftragsvergabe bewertet werden.
- **Sicherheitsanforderungen in Verträgen**: Verträge müssen Informationssicherheitsanforderungen einschliessen, einschliesslich Datenschutzverpflichtungen, Vorfallsbenachrichtigungsanforderungen, Prüfungsrechte und Unterauftragnehmer-Kontrollen.
- **Sicherheits-Abnahmekriterien**: Beschaffungs-Abnahmekriterien müssen Sicherheitsvalidierung einschliessen (z. B. Schwachstellen-Scan des gelieferten Systems, Sicherheitskonfigurations-Review, Zugangskontrollverifikation).
- **Datenverarbeitungsverträge**: Wo der Anbieter personenbezogene Daten im Auftrag der Organisation verarbeitet, muss ein Datenverarbeitungsvertrag gemäss nDSG Art. 9 (und DSGVO Art. 28, wo anwendbar) vor Beginn der Datenverarbeitung abgeschlossen werden.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Projekt** | Ein vorübergehendes Vorhaben mit definierten Start- und Enddaten, das durchgeführt wird, um ein einzigartiges Produkt, einen Dienst oder ein Ergebnis zu schaffen, das Informationsassets oder Informationssysteme umfasst |
| **Phasentor** | Ein formaler Überprüfungspunkt zwischen Projektphasen, an dem Sicherheitskriterien erfüllt sein müssen, bevor das Projekt voranschreitet |
| **Sicherheitsklassifizierung** | Die Kategorisierung eines Projekts als hohes, mittleres oder niedriges Risiko basierend auf Informationssicherheits-Auswirkungsfaktoren |
| **Sicherheitsanforderungsregister** | Eine dokumentierte Liste von Sicherheitsanforderungen für ein Projekt, verfolgt bis zur Umsetzung und zum Test |
| **DSFA (Datenschutz-Folgenabschätzung)** | Eine strukturierte Bewertung der Auswirkungen der geplanten Datenverarbeitung auf den Schutz personenbezogener Daten, erforderlich durch nDSG Art. 22, wo die Verarbeitung wahrscheinlich zu hohem Risiko führt |
| **Bedrohungsmodell** | Eine strukturierte Analyse potenzieller Bedrohungen für ein System oder eine Anwendung, die Angriffsvektoren, Bedrohungsakteure und erforderliche Gegenmassnahmen identifiziert |
| **Restrisiko** | Das nach der Implementierung von Sicherheitskontrollen verbleibende Risiko, das von der zuständigen Behörde formal akzeptiert werden muss |
| **Sicherheitsübergabe** | Die formale Übertragung von Sicherheitsdokumentation, Verantwortlichkeiten und operativen Verfahren vom Projektteam an das Betriebsteam bei Projektabschluss |
| **Security Champion** | Ein ausgebildetes Teammitglied, das in ein Projektteam eingebettet ist und als Sicherheits-Liaison fungiert und dabei hilft, Sicherheitsanforderungen zu identifizieren und für Best Practices einzutreten |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten für Informationssicherheit im Projektmanagement |
|-------|----------------------------------------------------------------------|
| **Geschäftsleitung** | Diese Richtlinie genehmigen; organisatorische Ressourcen für Projektsicherheit sicherstellen; Restrisiken für kritische Projekte akzeptieren; Sicherheitsstatus von Hochrisikoprojekten in Management-Reviews überprüfen |
| **ISB** | Hochrisiko-Klassifizierungen und Risikoakzeptanz genehmigen; Projekte mit inakzeptablem Sicherheitsrisiko stoppen oder verzögern; Projektsicherheitsmetriken überwachen; Ausnahmen von Sicherheitsanforderungen genehmigen |
| **Informationssicherheitsbeauftragter** | Projektteams bei Sicherheitsrisikobeurteilung und Anforderungsidentifizierung unterstützen; Mittelrisiko-Klassifizierungen genehmigen; Angemessenheit von Sicherheitstests überprüfen; Sicherheitsvorlagen und Checklisten pflegen |
| **Projektleiter** | Projektsicherheitsrisiko klassifizieren (mit InfoSec-Unterstützung); Sicherheitsaktivitäten planen und budgetieren; Sicherheitsaktivitäten an jedem Phasentor durchführen; Projektsicherheitsrisikoregister pflegen; Sicherheitsübergabedokumentation erstellen |
| **Business Owner** | Geschäftliche Sicherheitsanforderungen definieren; an Sicherheitsrisikobeurteilung teilnehmen; Restrisiken für Mittel/Niedrigrisiko-Projekte akzeptieren; Sicherheitsanforderungen als Teil des Projektumfangs genehmigen |
| **Technical Lead** | Sicherheitskontrollen in Lösungen einbauen; Sicherheitsanforderungen umsetzen; Bedrohungsmodellierung unterstützen; Sicherheitsbefunde aus Tests adressieren |
| **Datenschutzbeauftragter** | DSFAs überprüfen und genehmigen; über Datenschutzanforderungen für Projekte beraten; mit EDÖB in Verbindung treten, wo nDSG Art. 23 dies verlangt |

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlicher | Frequenz |
|---|---------|-----------------|----------|
| 1 | **Projektklassifizierungsunterlagen** mit Bestimmung und Genehmigung der Sicherheitsrisikoklassifizierung für jedes Projekt | Projektleiter | *Pro Projektinitiierung; bei Projektabschluss archiviert* |
| 2 | **Sicherheitsanforderungsregister** (oder Risikoregistereinträge für niedriges Risiko) mit identifizierten Sicherheitsanforderungen und Umsetzungsstatus | Projektleiter | *Pro Projekt; während des gesamten Lebenszyklus aktualisiert* |
| 3 | **Phasentor-Genehmigungsunterlagen** mit Sicherheitskriterien-Verifikation und Freigabe | Projektleiter | *Pro Phasentor; bei Projektabschluss archiviert* |
| 4 | **Sicherheitstest-Berichte** (Penetrationstests, Schwachstellen-Scans, Code-Reviews) gemäss Klassifizierungsanforderungen | InfoSec-Beauftragter | *Pro Projekt; abschliessender Bericht innerhalb von 7 Tagen nach Bereitstellung* |
| 5 | **Befundbehebungs-Unterlagen** zur Verfolgung von Befunden bis zum Abschluss oder zur Risikoakzeptanz | Projektleiter | *Pro Projekt; bis Abschluss aktualisiert* |
| 6 | **Sicherheitsübergabe-Dokumentationspakete** vom Betriebsteam akzeptiert | Projektleiter | *Pro Projektabschluss* |
| 7 | **Risikoakzeptanzunterlagen für Restrisiken** mit angemessenen Genehmigungen nach Klassifizierung | ISB / Business Owner | *Pro Projekt, wo Restrisiken bestehen* |
| 8 | **DSFA-Screening-Unterlagen** (und vollständige DSFA, wo anwendbar) für Projekte, die Personendaten verarbeiten | DSB / ISB | *Pro Projekt mit Personendaten* |
| 9 | **Lessons-Learned-Dokumentation** für mittlere und hochrisikoreiche Projekte | Projektleiter | *Pro Projektabschluss* |
| 10 | **Sicherheitsausnahmenregister** mit Genehmigungen, Ausgleichskontrollen und Fristen | ISB | *Pro Ausnahme; vierteljährlich überprüft* |
| 11 | **Projektsicherheits-Metrik-Dashboard** mit Klassifizierungsverteilung, Testabschluss und Befundtrends | ISB | *Monatlich; vierteljährlich an Geschäftsleitung gemeldet* |
| 12 | **Schulungsunterlagen** für Projektleiter zur Sicherheitsanforderungsintegration | HR / InfoSec-Beauftragter | *Jährlich; Abschluss verfolgt* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden überprüfen, einschliesslich, aber nicht beschränkt auf, Projektklassifizierungs-Audits, Phasentor-Konformitätsprüfungen, Verifikation des Sicherheitstest-Abschlusses, Reviews der Übergabedokumentation, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

Die folgenden Metriken müssen dem ISB vierteljährlich gemeldet werden:

| Metrik | Ziel | Roter Schwellenwert |
|--------|------|---------------------|
| Innerhalb von 5 Arbeitstagen nach Initiierung klassifizierte Projekte | 100% | <80% |
| Hoch/Mittelrisiko-Projekte mit abgeschlossenem Sicherheitsanforderungsregister | 100% | <90% |
| Vor der Bereitstellung abgeschlossene Sicherheitstests | 100% | <90% |
| Vor der Bereitstellung behobene kritische Sicherheitsbefunde | 100% | <100% (jeder bereitgestellte Kritisch-Befund = rot) |
| Vor Projektabschluss akzeptierte Sicherheitsübergabedokumentation | 100% | <80% |
| DSFA-Screening für Projekte mit Personendaten abgeschlossen | 100% | <90% |
| Lessons Learned für Hoch/Mittelrisiko-Projekte erfasst | 100% | <80% |

### Metrik-Dashboard

Der ISB muss ein Projektsicherheits-Metrik-Dashboard pflegen, das einen schnellen Überblick über die Programmgesundheit bietet. Das Dashboard muss folgendes enthalten:

- **Gesamtprogramm-Konformitätswert** — Aggregat der sieben oben genannten Metriken, berechnet als gewichteter Durchschnitt der Zielerreichung.
- **Konformitätsbalken pro Metrik** — jede Metrik mit aktuellem Prozentsatz und Statusindikator (grün >= Ziel, gelb >= roter Schwellenwert, rot < roter Schwellenwert).
- **Aktive Projekte nach Klassifizierung** — Anzahl aktiver Hoch-, Mittel- und Niedrigrisiko-Projekte.
- **Aufmerksamkeitspunkte** — Projekte mit überfälligen Sicherheitsaktivitäten oder Metriken, die gelbe/rote Schwellenwerte überschreiten.

Das Dashboard muss beim monatlichen ISB-Review überprüft und in den vierteljährlichen Bericht an die Geschäftsleitung aufgenommen werden.

**Berichtsanforderungen**:
- **Monatliches ISB-Dashboard**: Projekte nach Klassifizierung und Sicherheitsstatus (im Plan / gefährdet / überfällig); offene Sicherheitsbefunde nach Schweregrad und Alter; gewährte Sicherheitsausnahmen.
- **Vierteljährlicher Bericht an die Geschäftsleitung**: Gesamtzahl der Projekte und Anzahl der Hochrisikoprojekte; kritische Sicherheitsbefunde und Behebungsstatus; DSFA-Abschlussraten; wesentliche Sicherheitsvorfälle, die Projekte betreffen.
- **Jährliche Management-Überprüfung**: Vollständige Programm-Effektivitätsbewertung; Metrikktrends; wesentliche Befunde; Verbesserungsempfehlungen.

Metriken, die rote Schwellenwerte überschreiten, müssen an den ISB zur sofortigen Beachtung eskaliert und beim nächsten Management-Review gemeldet werden.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss im Voraus vom ISB genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen von Sicherheitstest- oder Phasentor-Anforderungen für Hochrisikoprojekte erfordern eine gemeinsame Genehmigung von ISB und Geschäftsleitung. Ausnahmen dürfen 90 Kalendertage ohne Neubewertung und Neugenehmigung nicht überschreiten.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Beendigung des Arbeitsverhältnisses. Projekte, die ohne erforderliche Sicherheitstests oder Klassifizierung bereitgestellt wurden, können sofort ausgesetzt werden, bis Sicherheitsanforderungen erfüllt sind. Nichteinhaltung muss dem ISB gemeldet und im ISMS-Nichtkonformitätsregister aufgezeichnet werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen müssen Änderungen der Projektmanagementmethodik, Audit-Befunde, regulatorische Änderungen (einschliesslich nDSG-Änderungen), sicherheitsbezogene Projektvorfälle, Ausnahmetrends, Lessons Learned aus Projektsicherheitsreviews und die Entwicklung der Bedrohungslandschaft berücksichtigen. Nichtkonformitäten im Zusammenhang mit dieser Richtlinie müssen im ISMS-Korrekturmassnahmenprozess (Klausel 10.2) mit Ursachenanalyse und nachverfolgter Behebung aufgezeichnet und verwaltet werden.

---

# Bereiche des ISO 27001-Standards, die adressiert werden

Informationssicherheit im Projektmanagement — ISO 27001-Kontrollzuordnung

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.3 Organisatorische Rollen, Verantwortlichkeiten und Befugnisse | **5.8 Informationssicherheit im Projektmanagement** |
| Klausel 6.1 Massnahmen zum Umgang mit Risiken und Chancen | 5.7 Bedrohungsintelligenz |
| Klausel 6.2 Informationssicherheitsziele und Planung | 5.9 Inventar von Informationen und anderen Assets |
| Klausel 7.4 Kommunikation | 5.12 Informationsklassifizierung |
| Klausel 8.1 Operative Planung und Steuerung | 5.19 Informationssicherheit in Lieferantenbeziehungen |
| Klausel 9.1 Überwachung, Messung, Analyse und Bewertung | 5.34 Datenschutz und Schutz personenbezogener Daten |
| Klausel 10.2 Nichtkonformität und Korrekturmassnahmen | 8.25 Sicherer Entwicklungslebenszyklus |
| | 8.26 Anwendungssicherheitsanforderungen |
| | 8.29 Sicherheitstests in Entwicklung und Abnahme |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 7 — Datenschutz durch Technikgestaltung und Voreinstellungen; Art. 8 — Technische und organisatorische Massnahmen; Art. 22 — DSFA für Hochrisikoverarbeitung; Art. 23 — Konsultation des EDÖB |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1-3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 25 — Datenschutz durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen; Art. 32 — Sicherheit der Verarbeitung; Art. 35 — Datenschutz-Folgenabschätzung |
| ISO/IEC 27001:2022 | Annex A Kontrolle 5.8 — Informationssicherheit im Projektmanagement |
| ISO/IEC 27002:2022 | Abschnitt 5.8 — Umsetzungshinweise für Informationssicherheit im Projektmanagement |
| ISO 21500:2021 | Projekt-, Programm- und Portfoliomanagement — Kontext und Konzepte |
| NIST SP 800-53 Rev 5 | SA-3 (System Development Life Cycle) — Sicherheitsintegration im gesamten Systemlebenszyklus; PL-2 (System Security and Privacy Plans) — Sicherheitsplanung für Systeme |
| NIST CSF 2.0 | GV.RR — Rollen, Verantwortlichkeiten und Befugnisse; ID.RA — Risikobeurteilung; PR.IP — Informationsschutzprozesse und -verfahren |
| CIS Controls v8 | Kontrolle 16 (Application Software Security) — Massnahmen zum sicheren Entwicklungslebenszyklus; Governance-Funktion — Richtlinien und Verfahren für den Asset-Schutz |

---

<!-- QA_VERIFIED: 2026-03-29 -->
