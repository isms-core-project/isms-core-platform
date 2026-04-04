<!-- ISMS-CORE:REF:ISMS-REF-A.8.32-aenderungsmanagement-referenz-DE:framework:REF:a.8.32 -->
**ISMS-REF-A.8.32 – Änderungsmanagement-Referenz**
**Umsetzungstools und Vorlagen (Nicht-ISMS Technische Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Änderungsmanagement-Referenz |
| **Dokumententyp** | Intern – Technische Referenz (Kein ISMS) |
| **Dokument-ID** | ISMS-REF-A.8.32 |
| **Dokumentenersteller** | Change Manager |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Change Manager (Technische Referenz – Keine Executive-Genehmigung erforderlich) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | INTERN |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | Change Manager / IT-Betrieb | Erste technische Referenz für ISO 27001:2022 Erstzertifizierung |

**Überprüfungszyklus**: Nach Bedarf (technologische und Tool-Evolution)
**Nächstes Überprüfungsdatum**: [Date + 12 months]
**Genehmiger**: Change Manager / IT-Betriebsleiter (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verteiler**: Change Manager, CAB-Mitglieder, IT-Betrieb, Änderungsumsetzer (zur technischen Umsetzungskenntnis)

---

⚠️ **WICHTIG – NICHT-ISMS TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschliesslich Informations- und Bewusstseinszwecken.

- Dieses Dokument ist KEIN Bestandteil des Informationssicherheits-Managementsystems (ISMS).
- Dieses Dokument definiert KEINE verbindlichen Änderungsmanagement-Kontrollen oder Anforderungen.
- Dieses Dokument legt KEINE bindenden Anforderungen, Fristen, KPIs oder SLAs fest.
- Dieses Dokument macht die Verwendung, das Verbot oder die Konfiguration spezifischer Änderungsmanagement-Tools, Anbieter oder Plattformen NICHT verbindlich.
- Dieses Dokument hebt KEINE ISMS-Richtlinie auf oder erweitert diese nicht.

Alle bindenden Anforderungen, Verpflichtungen und Governance-Entscheidungen im Änderungsmanagement sind ausschliesslich in **ISMS-POL-A.8.32 (Änderungsmanagement-Richtlinie)** und anderen genehmigten ISMS-Dokumenten definiert.

Dieses Dokument dient ausschliesslich als technische Referenz für:

- Beschreibung von Tool-Fähigkeiten und Anforderungen an Änderungsmanagementsysteme
- Bereitstellung von Vorlagen und Formularen für Änderungsmanagementaktivitäten
- Darstellung von Risikobewertungsmethoden und Entscheidungsmatrizen
- Unterstützung der Implementierungsplanung des Änderungsmanagements
- Kurzanleitungen für Praktiker
- **Dieses Dokument darf nicht als Audit-Nachweis der Umsetzung verwendet werden**

Die Nutzung dieses Dokuments impliziert keine Umsetzung, Compliance oder betriebliche Reife.

**Kritische Positionierungsaussage**:
Dieses Dokument liefert bewusst technische Details und Umsetzungsleitlinien, die über das für die ISO/IEC 27001 Richtliniendokumentation erforderliche Masse hinausgehen. Sein Zweck ist ausschliesslich technisches Bewusstsein und Praktiker-Unterstützung. Aus dem Vorhandensein, dem Fehlen oder der Klassifizierung eines Tools, einer Vorlage oder Methodik in diesem Dokument dürfen keine Audit-Schlussfolgerungen gezogen werden.

---

**Dokumentzweck und Geltungsbereich**

**Zweck**

Dieses Dokument stellt technisches Referenzmaterial für die Umsetzung des Änderungsmanagements bereit und konsolidiert:

- Tool-Fähigkeitsanforderungen (ehemals ISMS-POL-A.8.32-S5.A)
- Vorlagen für Änderungsantragsformulare (ehemals ISMS-POL-A.8.32-S5.B)
- Risikobewertungsmethodik (ehemals ISMS-POL-A.8.32-S5.C)
- Kurzanleitungen (ehemals ISMS-POL-A.8.32-S5.D)

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Definiert NICHT die bindenden Änderungsmanagement-Anforderungen von [Organisation] (siehe ISMS-POL-A.8.32)
- Legt KEINE obligatorischen Tool-Anforderungen fest
- Schafft KEINE Compliance-Verpflichtungen oder Audit-Kriterien
- Ersetzt NICHT die Richtlinienanforderungen aus ISMS-POL-A.8.32
- Macht KEINE spezifische Tool-Auswahl oder Anbieterbeziehungen verbindlich
- Legt KEINE Genehmigungsabläufe oder -kompetenzen fest

## Beziehung zum ISMS

Dieses Dokument ist eine **unverbindliche technische Referenz**. Alle Änderungsmanagement-Anforderungen sind ausschliesslich in ISMS-POL-A.8.32 (Änderungsmanagement-Richtlinie) definiert.

Umsetzungsentscheidungen werden über ISMS-IMP-A.8.32-Bewertungsarbeitsmappen dokumentiert, basierend auf Risikobewertung, Betriebskontext und Organisationsanforderungen.

## Inhaltsorganisation

Diese Referenz gliedert den Inhalt in vier Abschnitte:

1. **Abschnitt 2**: Tool-Fähigkeitsanforderungen – Mindestfähigkeiten für Änderungsmanagementsysteme
2. **Abschnitt 3**: Vorlage für Änderungsantragsformulare – Standardvorlage für einheitliche Informationserfassung
3. **Abschnitt 4**: Risikobewertungsmethodik – Detaillierte Auswirkungs-/Wahrscheinlichkeitsbewertung und Risikomatrix
4. **Abschnitt 5**: Kurzanleitung – Einseitige Praktiker-Anleitung für häufige Szenarien

---

# Tool-Fähigkeitsanforderungen

## Zweck

Mindestfähigkeiten definieren, die von Änderungsmanagementsystemen (ITSM-Tools, Ticketing-Systeme, Workflow-Plattformen) erwartet werden. Organisationen dürfen jedes System verwenden, das diese Fähigkeitsanforderungen erfüllt.

**Wichtig:** Dieses Dokument spezifiziert FÄHIGKEITEN, keine spezifischen Produkte oder Anbieter.

## Kernfähigkeiten des Änderungsmanagements

### CAP-001: Verwaltung von Änderungsanträgen

**Fähigkeit:** Das System MUSS die Erstellung und Verwaltung von Änderungsanträgen ermöglichen.

**Anforderungen:**

- Änderungsanträge mit eindeutigen Kennungen erstellen
- Alle Pflichtfelder gemäss Abschnitt 3 (Formularvorlage) erfassen
- Rich-Text-Beschreibungen und Dateianhänge unterstützen
- Verwandte Änderungen, Vorfälle und Probleme verknüpfen
- Änderungen taggen/kategorisieren (nach Typ, betroffenen Systemen, Priorität)

**Bewertung:** Können Benutzer vollständige Änderungsanträge einreichen? Werden alle Pflichtfelder erfasst?

---

### CAP-002: Verwaltung des Änderungsstatus

**Fähigkeit:** Das System MUSS den Änderungsstatus durch einen definierten Lebenszyklus verfolgen.

**Erforderliche Zustände (Minimum):**

- Beantragt / Entwurf
- In Bewertung / Überprüfung
- Geplant / Genehmigt
- In Umsetzung
- Überprüfung (PIR)
- Abgeschlossen
- Abgelehnt
- Storniert

**Anforderungen:**

- Zustandsübergänge mit Zeitstempel und Benutzer verfolgt
- Zustandsbasierte Workflows (bestimmte Aktionen nur in bestimmten Zuständen möglich)
- Zustandsverlauf im Änderungsnachweis sichtbar

---

### CAP-003: Genehmigungsworkflow

**Fähigkeit:** Das System MUSS konfigurierbare Genehmigungsworkflows unterstützen.

**Anforderungen:**

- Mehrstufige Genehmigungen (Change Manager, CAB, E-CAB, Management)
- Rollenbasierte Genehmigungsweiterleitung
- Genehmigungsbenachrichtigungen an Genehmiger
- Verfolgung von Genehmigungsfristen
- Genehmigung mit Kommentaren/Bedingungen
- Genehmigungsverlauf mit Genehmigeridentität und Zeitstempel
- E-Mail-Integration für Genehmigungsbenachrichtigungen

---

### CAP-004: Änderungskalender

**Fähigkeit:** Das System MUSS einen Änderungskalender mit geplanten Änderungen bereitstellen.

**Anforderungen:**

- Visuelle Kalenderansicht (täglich, wöchentlich, monatlich)
- Konflikte zwischen Änderungen hervorheben
- Änderungssperrzeiten und Sperrfenster identifizieren
- Filtern nach System, Änderungstyp, Risikoniveau, Team
- Export im iCalendar-Format

---

### CAP-005: Berichterstattung und Analytik

**Fähigkeit:** Das System MUSS Berichtsfähigkeiten für das Metriken-Tracking bereitstellen.

**Erforderliche Berichte:**

- Änderungsvolumen (nach Typ, Zeitraum, Risikoniveau)
- Änderungserfolgsquote
- Prozentsatz der Notfalländerungen
- Durchschnittliche Änderungsdauer
- Änderungsbedingte Vorfälle
- PIR-Abschlussquote
- Nutzung von Standard-Änderungen
- Trendanalyse

---

### CAP-006: Audit-Trail

**Fähigkeit:** Das System MUSS einen vollständigen Audit-Trail führen.

**Anforderungen:**

- Alle Feldänderungen protokolliert (wer, was, wann)
- Zustandsübergänge protokolliert
- Genehmigungen mit Zeitstempel protokolliert
- Systemzugriff protokolliert
- Unveränderliches Audit-Protokoll (nach Erstellung nicht änderbar)
- Aufbewahrung des Audit-Protokolls gemäss Richtlinienanforderungen

---

### CAP-007: Integration

**Fähigkeit:** Das System SOLLTE sich mit verwandten Systemen integrieren.

**Integrationspunkte:**

- Configuration Management Database (CMDB) – Änderungen mit CIs verknüpfen
- Incident-Management – Änderungen mit Vorfällen verknüpfen
- Problem-Management – Änderungen mit Problemen verknüpfen
- Service-Katalog – Standard-Änderungen als Katalogelemente
- Benachrichtigungssysteme – E-Mail, Slack, MS Teams
- API-Verfügbarkeit für Automatisierung

---

## Tool-Bewertungs-Checkliste

Organisationen, die Änderungsmanagement-Tools evaluieren, können diese Checkliste verwenden:

- [ ] CAP-001: Fähigkeiten zur Verwaltung von Änderungsanträgen vorhanden
- [ ] CAP-002: Zustandsverwaltung mit Lebenszyklus-Tracking
- [ ] CAP-003: Konfigurierbare Genehmigungsworkflows
- [ ] CAP-004: Änderungskalender mit Konflikterkennung
- [ ] CAP-005: Berichterstattungs- und Analysefähigkeiten
- [ ] CAP-006: Vollständige Audit-Trail-Fähigkeiten
- [ ] CAP-007: Integrationsfähigkeiten mit CMDB/Vorfall-/Problemsystemen
- [ ] Benutzerfreundliche Oberfläche für Änderungsantragsteller
- [ ] Mobiler Zugriff möglich
- [ ] Verwaltung des Standard-Änderungskatalogs
- [ ] Massenänderungsoperationen unterstützt
- [ ] Rollenbasierte Zugriffskontrolle
- [ ] Anpassbare Felder und Workflows
- [ ] Mandantenfähigkeit (bei Bedarf)
- [ ] Cloud-basiertes oder On-Premises-Deployment (gemäss Anforderungen)

---

# Vorlage für Änderungsantragsformulare

## Zweck

Standardvorlage für Änderungsanträge bereitstellen, die eine einheitliche Informationserfassung gewährleistet. Diese Vorlage zur Konfiguration von ITSM-Tool-Formularen oder als eigenständiges Änderungsantragsdokument verwenden.

## Änderungsantragsformular

**Abschnitt 1: Grundinformationen**

- **Änderungsantrags-ID:** [Automatisch vom System generiert]
- **Einreichungsdatum:** [Automatisch ausgefüllt]
- **Beantragt von:** [Name, E-Mail, Abteilung]
- **Kontakttelefon:** [Für Umsetzungskoordination]

**Abschnitt 2: Änderungsklassifizierung**

- **Änderungstyp:** [Dropdown: Standard / Normal / Notfall]
- **Bei Standard-Änderung – Eintrag im Standard-Änderungskatalog:** [Dropdown: Aus Katalog auswählen]
- **Bei Notfalländerung – Notfallbegründung:** [Text: Warum die Notfallklassifizierung gilt]
- **Priorität:** [Dropdown: Kritisch / Hoch / Mittel / Niedrig]
- **Risikoniveau:** [Automatisch berechnet oder manuell: Kritisch / Hoch / Mittel / Niedrig]

**Abschnitt 3: Änderungsbeschreibung**

- **Änderungstitel:** [Kurzer, beschreibender Titel – max. 80 Zeichen]
- **Änderungsbeschreibung:** [Was wird geändert? Was ist der Umfang? Was sind die spezifischen Modifikationen?]
- **Geschäftliche Begründung:** [Warum ist diese Änderung notwendig? Geschäftstreiber, erwarteter Nutzen, Konsequenzen bei Nichtdurchführung]

**Abschnitt 4: Folgenabschätzung**

- **Betroffene Systeme/Komponenten:** [Liste der Configuration Items aus der CMDB]
- **Betroffene Benutzer/Interessengruppen:** [Benutzergruppen, ungefähre Anzahl, geografische Standorte]
- **Dienstauswirkung:** [Dropdown: Keine Auswirkung / Eingeschränkt / Teilausfall / Vollständiger Ausfall]
- **Ausfallzeit erforderlich:** [Ja / Nein] **Bei Ja, Dauer:** [Geschätzte Minuten/Stunden]

**Abschnitt 5: Risikobewertung**

- **Auswirkungsgrad:** [Dropdown: Niedrig / Mittel / Hoch / Kritisch] + Begründung
- **Wahrscheinlichkeitsgrad:** [Dropdown: Niedrig / Mittel / Hoch] + Begründung
- **Gesamtrisiko:** [Automatisch aus Auswirkung × Wahrscheinlichkeitsmatrix berechnet]
- **Risikominderungsmassnahmen:** [Wie werden Risiken reduziert?]

**Abschnitt 6: Abhängigkeiten und Voraussetzungen**

- **Abhängigkeiten:** [Andere Änderungen, Systeme oder Aktivitäten, von denen diese Änderung abhängt]
- **Voraussetzungen:** [Was muss vor dieser Änderung abgeschlossen sein – technisch, geschäftlich, genehmigungstechnisch]
- **Konflikte:** [Bekannte Konflikte mit anderen Änderungen oder Aktivitäten?]

**Abschnitt 7: Umsetzungsplan**

- **Vorgeschlagenes Umsetzungsdatum/-uhrzeit:** [Datumsauswahl, Zeitauswahl – Zeitzone angeben]
- **Umsetzungsfenster:** [Geschätzte Dauer]
- **Umsetzungsschritte:** [Übergeordnete Verfahren als nummerierte Liste]
- **Umsetzungsteam:** [Hauptumsetzer, weitere Umsetzer, Verifikationspersonal]
- **Ressourcenanforderungen:** [Personal, Tools/Software, Budget]

**Abschnitt 8: Tests und Validierung**

- **Testumgebung:** [Wo wird die Änderung getestet?]
- **Durchgeführte Tests:** [Unit-Tests, Integrationstests, Sicherheitstests, UAT – J/N und Ergebnisse]
- **Testergebnisse:** [Testdokumentation anhängen]
- **Abnahmekriterien:** [Wie wird Erfolg gemessen?]

**Abschnitt 9: Rollback-Plan**

- **Rollback-Verfahren:** [Schritt-für-Schritt-Rollback bei Änderungsscheitern]
- **Rollback-Dauer:** [Für Rollback erforderliche Zeit]
- **Rollback-Entscheidungskriterien:** [Wann soll der Rollback eingeleitet werden?]
- **Datenüberlegungen:** [Verursacht Rollback Datenverlust? Wie wird das gemindert?]

**Abschnitt 10: Kommunikationsplan**

- **Stakeholder-Benachrichtigung erforderlich:** [Ja / Nein]
- **Bei Ja:** Wer muss benachrichtigt werden, Benachrichtigungsmethode, Zeitpunkt, Kommunikationsverantwortlicher
- **Benutzerkommunikation:** [Benötigen Endbenutzer eine Vorankündigung?]

**Abschnitt 11: Dokumentation**

- **Dokumentationsaktualisierungen erforderlich:** [Ja / Nein]
- **Bei Ja:** Systemdokumentation, Betriebsverfahren, Benutzerhandbücher, Netzwerkdiagramme, Sonstiges
- **Dokumentationsverantwortlicher:** [Wer aktualisiert die Dokumentation?]

**Abschnitt 12: Nach der Umsetzung**

- **PIR erforderlich:** [Automatisch basierend auf Änderungstyp/Risiko ermittelt]
- **Erfolgskriterien:** [Wie wird der Änderungserfolg gemessen?]
- **Überwachungsdauer:** [Wie lange wird die Änderung nach der Umsetzung überwacht?]

---

# Risikobewertungsmethodik

## Zweck

Detaillierte Methodik für die Bewertung des Änderungsrisikos basierend auf Auswirkung und Wahrscheinlichkeit bereitstellen, die angemessene Genehmigungskompetenz bestimmt und Risikominderungsstrategien identifiziert.

## Folgenabschätzung

### Definitionen der Auswirkungsgrade

| Auswirkungsgrad | Definition | Umfang |
|----------------|------------|--------|
| **Niedrig** | Minimale Auswirkung, leicht reversibel | Einzelbenutzer, einzelnes nicht-kritisches System, Wiederherstellung <15 Min. |
| **Mittel** | Moderate Auswirkung, Rollback machbar | Team/mehrere Benutzer, nicht-kritische Systeme, Wiederherstellung <2 Std. |
| **Hoch** | Bedeutende Auswirkung, komplexer Rollback | Abteilung, Hauptsystem, Geschäftsprozessunterbrechung, Wiederherstellung <8 Std. |
| **Kritisch** | Schwerwiegende Auswirkung, schwierige Wiederherstellung | Organisationsweit, geschäftskritisches System, kundenseitig, Wiederherstellung >8 Std. oder irreversibel |

### Dimensionen der Folgenabschätzung

**Betroffene Benutzer:** Niedrig: <10 / Mittel: 10–100 / Hoch: 100–1.000 / Kritisch: >1.000

**Geschäftsprozesse:** Niedrig: Optional / Mittel: Wichtig / Hoch: Kritisch mit Workarounds / Kritisch: Geschäftskritisch

**Finanzielle Auswirkung:** Niedrig: <CHF 10 K / Mittel: CHF 10 K–100 K / Hoch: CHF 100 K–1 Mio. / Kritisch: >CHF 1 Mio.

**Regulatorisch/Compliance:** Niedrig: Keine / Mittel: Berichterstattung betroffen / Hoch: Fristrisiko / Kritisch: Potenzielle Verletzung

**Reputation:** Niedrig: Nur intern / Mittel: Benutzerunannehmlichkeit / Hoch: Öffentliche Sichtbarkeit / Kritisch: Grosse Auswirkung

**Wiederherstellungskomplexität:** Niedrig: <15 Min. / Mittel: <2 Std. / Hoch: <8 Std. / Kritisch: Sehr komplex oder irreversibel

**Gesamtauswirkung:** Höchster Grad über alle Dimensionen (konservativste Bewertung)

## Wahrscheinlichkeitsbewertung

### Definitionen der Wahrscheinlichkeitsgrade

| Wahrscheinlichkeit | Definition | Typische Erfolgsquote |
|-------------------|------------|----------------------|
| **Niedrig** | Sehr unwahrscheinlich zu scheitern | >95% Erfolg |
| **Mittel** | Moderate Problemchance | 75–95% Erfolg |
| **Hoch** | Erhebliche Problemchance | <75% Erfolg |

### Faktoren der Wahrscheinlichkeitsbewertung

**Änderungskomplexität:** Niedrig: Einfach / Mittel: Moderat / Hoch: Komplex

**Umgebungsstabilität:** Niedrig: Stabil / Mittel: Gelegentliche Probleme / Hoch: Häufige Probleme

**Team-Erfahrung:** Niedrig: Erfahren / Mittel: Einige Erfahrung / Hoch: Neues Verfahren/Team

**Testvollständigkeit:** Niedrig: Ausgiebig getestet / Mittel: Gut getestet / Hoch: Eingeschränkt/Ungetestet

**Abhängigkeiten:** Niedrig: Keine / Mittel: Wenige / Hoch: Viele komplexe Abhängigkeiten

## Risikomatrix

**Gesamtrisiko = Auswirkung × Wahrscheinlichkeit**

| Auswirkung ↓ / Wahrscheinlichkeit → | Niedrig | Mittel | Hoch |
|------------------------------------|---------|--------|------|
| **Niedrig** | Niedrig | Niedrig | Mittel |
| **Mittel** | Niedrig | Mittel | Hoch |
| **Hoch** | Mittel | Hoch | Kritisch |
| **Kritisch** | Hoch | Kritisch | Kritisch |

## Genehmigungskompetenz nach Risikoniveau

| Risikoniveau | Genehmigungskompetenz | Zusätzliche Anforderungen |
|-------------|----------------------|--------------------------|
| **Niedrig** | Change Manager | Standarddokumentation |
| **Mittel** | CAB | Standarddokumentation |
| **Hoch** | CAB + IT-Senior-Management | Umfassende Dokumentation |
| **Kritisch** | CAB + ISB + Geschäftsleitung | Umfassende Dokumentation + Executive-Briefing |
| **Notfall** | E-CAB (IT-Betriebsleiter + ISB) | Retrospektive CAB-Überprüfung innerhalb von 48 Stunden |

---

# Kurzanleitung

## Entscheidungsbaum für Änderungstypen

**HIER STARTEN → Ist diese Änderung notwendig?**

```
├─ Ist die Änderung bereits im Standard-Änderungskatalog?
│   ├─ JA → Standard-Änderung
│   │        ▼
│   │   • Änderungsantrag einreichen (Self-Service möglich)
│   │   • Keine CAB-Genehmigung notwendig
│   │   • Katalogverfahren befolgen
│   │   • Im Änderungssystem protokollieren
│   │
│   └─ NEIN → Weiter...
│
├─ Handelt es sich um eine Notfallsituation?
│   ├─ JA → Erfüllt sie ALLE Notfallkriterien?
│   │        • Sofortiges Handeln erforderlich?
│   │        • Kritischer Vorfall/Sicherheit/Ausfall?
│   │        • Risiko der Untätigkeit > Risiko des Handelns?
│   │        ▼
│   │   ├─ JA → Notfalländerung
│   │   │        • E-CAB sofort kontaktieren
│   │   │        • Begründung dokumentieren
│   │   │        • Beschleunigter Genehmigungsprozess
│   │   │        • PIR obligatorisch innerhalb von 2 Tagen
│   │   │
│   │   └─ NEIN → Dringende normale Änderung
│   │              • Sonder-CAB-Sitzung einberufen
│   │              • Beschleunigen, aber vollständigen Prozess einhalten
│   │
│   └─ NEIN → Normale Änderung
│              ▼
│         • Änderungsantrag einreichen
│         • Risikobewertung
│         • CAB-Überprüfung
│         • Vollständiger Prozess
```

## Kurzreferenz zur Genehmigungskompetenz

| Risikoniveau | Wer genehmigt | Typischer Zeitrahmen |
|-------------|---------------|---------------------|
| **Niedrig** (Standard) | Change Manager | Sofort – 1 Tag |
| **Mittel** (Normal) | CAB | Wöchentliche CAB-Sitzung |
| **Hoch** (Normal) | CAB + IT-Senior-Management | 1–2 Wochen |
| **Kritisch** (Normal) | CAB + ISB + Geschäftsleitung | 2–4 Wochen |
| **Notfall** | E-CAB | <4 Stunden |

## Checkliste für Pflichtangaben

**Jeder Änderungsantrag benötigt:**

- [ ] Klare Beschreibung (was wird geändert?)
- [ ] Geschäftliche Begründung (warum?)
- [ ] Risikobewertung (Auswirkung + Wahrscheinlichkeit)
- [ ] Betroffene Systeme (aus CMDB)
- [ ] Umsetzungsplan (schrittweise)
- [ ] Tests abgeschlossen (oder Plan bei Notfall)
- [ ] Rollback-Plan (wie rückgängig machen)
- [ ] Kommunikationsplan (wer wird informiert)

## Checkliste für Notfalländerungen

**Vor der Notfallerklärung:**

- [ ] Kritischer Vorfall oder Sicherheitslücke?
- [ ] Sofortiges Handeln notwendig, um wesentliche Auswirkungen zu verhindern?
- [ ] Risiko der NICHT-Änderung > Risiko der Änderung?
- [ ] Keine Zeit für normale CAB-Überprüfung?

**Bei JA zu allen Punkten oben → Notfalländerung:**
1. E-CAB kontaktieren (IT-Betriebsleiter + ISB)
2. Notfallbegründung dokumentieren
3. Beschleunigten Genehmigungsprozess einleiten
4. Mit Monitoring umsetzen
5. PIR innerhalb von 48 Stunden durchführen
6. Retrospektiv dem CAB präsentieren

## Schlüsselkontakte

**Change Manager:** [Name, E-Mail, Telefon]
**CAB-Vorsitz:** [Name, E-Mail, Telefon]
**E-CAB (Notfall):** [Namen, E-Mails, Telefone]
**IT-Betriebsleiter:** [Name, E-Mail, Telefon]
**ISB:** [Name, E-Mail, Telefon]

**Eskalationspfad:**
1. Change Manager
2. IT-Betriebsleiter
3. ISB
4. ITL

## Häufige Fehler, die vermieden werden sollten

1. ❌ **Unvollständige Änderungsanträge einreichen** → Fehlende Genehmigungen verzögern
2. ❌ **Tests "wegen Dringlichkeit" überspringen** → Produktionsvorfälle
3. ❌ **Kein Rollback-Plan** → Verlängerte Ausfälle bei Änderungsscheitern
4. ❌ **Vergessen zu kommunizieren** → Verärgerte Benutzer und Führungskräfte
5. ❌ **Fehlklassifizierung als Notfall** → Prozesserosion
6. ❌ **Keine Dokumentationsaktualisierungen** → Betriebliche Verwirrung
7. ❌ **PIR überspringen** → Erfahrungen nicht gelernt, Fehler wiederholt
8. ❌ **Umsetzung ohne Genehmigung** → Compliance-Verletzung, karrierebeschädigend

## Erfolgstipps

✅ **Änderungsantrag früh starten** – Nicht bis zur letzten Minute warten
✅ **Bei der Risikobewertung gründlich sein** – Besser sicher als nachher leid
✅ **Zuerst in Nicht-Produktion testen** – Probleme vor Produktion erkennen
✅ **Rollback-Plan bereithalten** – Auf das Beste hoffen, auf das Schlimmste vorbereiten
✅ **Proaktiv kommunizieren** – Interessengruppen schätzen Vorankündigung
✅ **Alles dokumentieren** – Ihr zukünftiges Ich wird Ihr heutiges Ich dafür danken
✅ **Aus Fehlern lernen** – PIR dient der Verbesserung, nicht der Schuldzuweisung

---

# Leitlinien zur Tool-Auswahl

## Bewertung von ITSM-Plattformen

**Schlüsselkriterien:**

- Mindest-Fähigkeitsanforderungen erfüllt (Abschnitt 2)
- Benutzerfreundlich für Änderungsantragsteller
- Integration mit bestehenden Tools (CMDB, Ticketing)
- Berichterstattungs- und Analysefähigkeiten
- Total Cost of Ownership (Lizenzierung, Wartung, Schulung)
- Anbieter-Stabilität und Supportqualität
- Cloud- oder On-Premises-Deployment-Modell

**Verbreitete ITSM-Plattformen** (Beispiele, keine Empfehlungen):

- ServiceNow
- Jira Service Management
- BMC Remedy
- Cherwell
- Freshservice
- ManageEngine
- Open-Source-Optionen (OTRS, iTop, osTicket)

## Best Practices zur Konfiguration

**Bei der Konfiguration von Änderungsmanagement-Tools:**
1. Mit Out-of-Box-Workflows starten, nur bei Bedarf anpassen
2. Pflichtfelder implementieren, um Vollständigkeit durchzusetzen
3. Genehmigungsworkflows basierend auf Risikomatrix konfigurieren
4. E-Mail-Benachrichtigungen für alle Interessengruppen einrichten
5. Änderungskalender mit Sperrzeiten konfigurieren
6. Integration mit CMDB für genaue Folgenabschätzung aktivieren
7. Dashboards für Change Manager und CAB einrichten
8. Berichtsvorlagen für erforderliche Metriken konfigurieren
9. Benutzer vor Go-Live schulen
10. Laufende Wartung und Updates planen

---

# Anhang: Formularvorlagen

## A.1 Änderungsantragsformular (Leer)

[Vollständiges Leerformular entsprechend der Struktur aus Abschnitt 3.2]

## A.2 Vorlage für Notfalländerungsbegründung

**Notfall-Änderungsantrag**

- **Änderungs-ID:** ___________
- **Eingereicht von:** ___________
- **Datum/Uhrzeit:** ___________

**Erfüllte Notfallkriterien:**

- [ ] Kritischer Vorfall, der sofortige Behebung erfordert
- [ ] Sicherheitslücke, die sofortige Behebung erfordert
- [ ] Systemausfall, der sofortige Wiederherstellung erfordert
- [ ] Prävention eines drohenden Systemausfalls
- [ ] Dringende regulatorische Anforderung

**Situationsbeschreibung:**
[Kritische Situation beschreiben, die die Notfalländerung erfordert]

**Auswirkung bei NICHT sofortiger Umsetzung:**
[Konsequenzen einer Verzögerung beschreiben]

**Risiko bei Umsetzung ohne vollständige Tests:**
[Risiken einer beschleunigten Umsetzung anerkennen]

**Minderungsmassnahmen:**
[Beschreiben, wie Risiken trotz Dringlichkeit minimiert werden]

**E-CAB-Genehmigung:**

- IT-Betriebsleiter: ___________ Datum: ___________
- ISB: ___________ Datum: ___________

---

**ENDE DER TECHNISCHEN REFERENZ**

---

*Diese technische Referenz unterstützt die Umsetzung von ISMS-POL-A.8.32. Alle bindenden Anforderungen sind im Richtliniendokument definiert.*

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-29 -->
