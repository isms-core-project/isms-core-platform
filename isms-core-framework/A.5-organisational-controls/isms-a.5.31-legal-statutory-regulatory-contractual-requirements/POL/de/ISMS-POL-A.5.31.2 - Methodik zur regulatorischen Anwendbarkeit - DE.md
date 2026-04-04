<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.2-DE:framework:POL:a.5.31.2 -->
**ISMS-POL-A.5.31.2 — Methodik zur regulatorischen Anwendbarkeit**
**Gesetzliche, gesetzlich vorgeschriebene, regulatorische und vertragliche Anforderungen**

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Gesetzliche, gesetzlich vorgeschriebene, regulatorische und vertragliche Anforderungen: Methodik zur regulatorischen Anwendbarkeit |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.31.2 |
| **Erstellt von** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Festzulegen] |
| **Klassifizierung** | INTERN |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB/ISO | Erstversion des Richtlinienrahmens für ISO 27001:2022 Erstzertifizierung |

---

# Einführung und Framework-Kontext

## Zweck dieses Richtlinienabschnitts

Dieser Richtlinienabschnitt legt die systematische Methodik fest, mit der [Organisation] gesetzliche, gesetzlich vorgeschriebene, regulatorische und vertragliche Anforderungen, die für ihr Informationssicherheitsprogramm relevant sind, identifiziert, bewertet und kategorisiert.

Die hier definierte Methodik verwandelt die Einhaltung von Vorschriften von einer reaktiven, ad-hoc Aktivität in einen systematischen, wiederholbaren Prozess, der konsistente, nachvollziehbare Bestimmungen der regulatorischen Anwendbarkeit erzeugt.

## Beziehung zum Compliance-Framework

ISMS-POL-A.5.31.1 (Zusammenfassung & Massnahmenausrichtung) hat den übergeordneten Compliance-Rahmen und die Governance-Struktur festgelegt. Dieser Richtlinienabschnitt (5.31.2) stellt die **erste operative Methodik** innerhalb dieses Rahmens bereit: den Prozess zur Bestimmung, **welche Vorschriften für [Organisation] gelten**.

Die Ergebnisse dieser Methodik befüllen und pflegen direkt **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** – das verbindliche Register anwendbarer Vorschriften.

**Framework-Fluss:**
```
ISO 27001:2022 Massnahme A.5.31
         ↓
POL-5.31.1: Framework-Grundlage & Governance
         ↓
POL-5.31.2: Anwendbarkeits-Methodik ← SIE BEFINDEN SICH HIER
         ↓ (erzeugt Einträge für)
ISMS-POL-00: Regulatorisches Register
         ↓ (fliesst ein in)
POL-5.31.3: Anforderungsextraktion & Massnahmenzuordnung
         ↓
POL-5.31.4: Änderungsmanagement & Nachweise
```

## Systematischer vs. Ad-hoc-Ansatz

**Traditioneller Ad-hoc-Ansatz:**

- „Wir sind in Land X tätig, also müssen wir wahrscheinlich dem Datenschutzgesetz von Land X entsprechen"
- „Kunde Y erwähnte Vorschrift Z in seiner Ausschreibung, also gilt die wohl"
- „Ich habe auf einer Konferenz gehört, dass Vorschrift ABC wichtig ist"
- Keine dokumentierte Begründung für Bestimmungen
- Inkonsistente Kriterien für verschiedene Vorschriften
- Kein systematischer Überprüfungsprozess

**Systematischer Ansatz dieses Frameworks:**

- Definierte Auslöseereignisse initiieren Anwendbarkeitsbewertungen
- Mehrere Quellen systematisch auf potenziell anwendbare Vorschriften geprüft
- Strukturierte Bewertung mit konsistenten dreidimensionalen Kriterien
- Dokumentierte Begründung mit unterstützenden Nachweisen
- Formeller Genehmigungsworkflow
- Periodische Überprüfung und Validierung
- Vollständiger Prüfpfad

Der systematische Ansatz stellt sicher, dass:

- Verschiedene Auswerter zu denselben Schlussfolgerungen gelangen (Wiederholbarkeit)
- Entscheidungen gegenüber Prüfern und Regulatoren verteidigbar sind
- Anwendbarkeitsbestimmungen rückverfolgbar und umkehrbar sind
- Änderungen der Umstände eine Neubewertung auslösen
- Nichts durch die Maschen fällt

## Integration mit ISMS-POL-00

ISMS-POL-00 dient als **verbindliches regulatorisches Register** für [Organisation]. Diese Richtlinie definiert die **Prozesse, durch die Vorschriften in POL-00 eintreten, dort kategorisiert werden und es verlassen**.

**Schlüsselbeziehung:**

- **Diese Richtlinie (POL-5.31.2)** definiert die Methodik für die Anwendbarkeitsbewertung
- **POL-00** enthält die Ergebnisse der Anwendung dieser Methodik (die Liste anwendbarer Vorschriften)
- **IMP-5.31.1** (Anwendbarkeitsbewertungsprozess) stellt schrittweise operative Verfahren zur Ausführung dieser Methodik bereit
- **Bewertungsarbeitsbuch 2** (Anwendbarkeitsmatrix) stellt strukturierte Werkzeuge zur Dokumentation bereit

## Dokumentenumfang

Dieser Richtlinienabschnitt behandelt:

- **Auslöseereignisse**, die Anwendbarkeitsbewertungen initiieren (Abschnitt 2.1)
- **Quellen** zur Identifikation potenziell anwendbarer Vorschriften (Abschnitt 2.2)
- **Erstscreening** zur Filterung von Kandidaten (Abschnitt 2.3)
- **Dreidimensionale Anwendbarkeitsbewertungs-Methodik** (Abschnitt 3)
- **Drei-Tier-Kategorisierungs-Framework** (Abschnitt 4)
- **Dokumentations- und Genehmigungsanforderungen** (Abschnitt 5)
- **Überprüfungshäufigkeit und -auslöser** für Neubewertung (Abschnitt 6)

Dieser Richtlinienabschnitt deckt NICHT ab:

- Extraktion von Anforderungen aus anwendbaren Vorschriften (behandelt in POL-5.31.3)
- Zuordnung von Anforderungen zu Massnahmen (behandelt in POL-5.31.3)
- Überwachung auf regulatorische Änderungen (behandelt in POL-5.31.4)
- Nachweismanagement (behandelt in POL-5.31.4)

---

# Regulatorischer Identifikationsprozess

## Auslöseereignisse für die regulatorische Identifikation

[Organisation] leitet die Identifikation von Vorschriften und Anwendbarkeitsbewertungen ein, wenn folgende Ereignisse eintreten:

### Periodische Überprüfungsauslöser

**Jährliche umfassende Überprüfung** (Obligatorisch):

- Vollständige Prüfung der regulatorischen Landschaft
- Überprüfung aller Einträge in ISMS-POL-00 auf fortbestehende Anwendbarkeit
- Validierung, dass keine anwendbaren Vorschriften übersehen wurden
- Im Q4 jeden Kalenderjahres durchgeführt (oder gemäss ISMS-Kalender)
- Verantwortung: Compliance-Beauftragter in Koordination mit der Rechtsfunktion

**Quartalsweiser Umfeldüberblick** (Empfohlen):

- Fokussierte Prüfung regulatorischer Entwicklungen in Schlüsseljurisdiktionen
- Überprüfung im Quartal aufgelaufener regulatorischer Überwachungsalarme
- Identifikation neuer oder vorgeschlagener Vorschriften, die Aufmerksamkeit erfordern
- Am Ende jedes Quartals durchgeführt
- Verantwortung: Compliance-Beauftragter

### Expansionsauslöser

Eine Anwendbarkeitsbewertung wird eingeleitet, wenn [Organisation]:

**Neue geografische Märkte erschliesst:**

- Rechtliche Einheit in neuer Jurisdiktion gründet
- Büro oder Betriebsstätte an neuem Standort eröffnet
- Beginnt, Dienstleistungen in neuem Land oder neuer Region zu vermarkten oder anzubieten
- Daten von Personen in neuer Jurisdiktion verarbeitet

**Neue Dienstleistungen oder Produkte anbietet:**

- Neues Dienstleistungsangebot startet (z.B. Cloud-Dienste, Managed Security, Beratung)
- In neuen vertikalen Markt eintritt (z.B. Gesundheitswesen, Finanzdienstleistungen, öffentlicher Sektor)
- Neue Datenkategorien verarbeitet (z.B. Gesundheitsdaten, Finanzdaten, biometrische Daten)
- Neue Technologien mit regulatorischen Implikationen einführt (z.B. KI, Blockchain)

**Kunden in regulierten Branchen gewinnt:**

- Vertrag mit Kunden in stark reguliertem Sektor abschliesst (Finanzen, Gesundheit, Energie etc.)
- Beziehung umfasst Zugang zu regulierten Daten oder Systemen des Kunden
- Kunde in für [Organisation] neuer Jurisdiktion tätig ist

**Fusionen und Übernahmen:**

- [Organisation] erwirbt eine andere Einheit (übernimmt deren regulatorische Verpflichtungen)
- [Organisation] wird erworben (kann neue Verpflichtungen des Mutterkonzerns auslösen)
- Löst umfassende Überprüfung der kombinierten regulatorischen Landschaft aus

### Vertragliche Auslöser

**Neue Kundenverträge:**

- Kundenvertrag enthält spezifische Compliance-Anforderungen
- Kunde führt Compliance-Due-Diligence-Fragebogen durch
- Ausschreibung enthält regulatorische oder Zertifizierungsanforderungen
- Rahmendienstleistungsvertrag enthält regulatorische Compliance-Klauseln

**Neue Lieferantenvereinbarungen:**

- Lieferantenvereinbarung schafft Durchleitungs-Compliance-Verpflichtungen
- [Organisation] wird als Unterauftragsverarbeiter oder Dienstleister mit übernommenen Verpflichtungen designiert
- Lieferantenzertifizierungen erfordern, dass [Organisation] bestimmte Standards erfüllt

**Partner- und Händlervereinbarungen:**

- Gemeinsames Angebot mit Compliance-Anforderungen aus den Verpflichtungen des Partners
- Technologiepartner erfordert spezifische Compliance-Position
- Händlervereinbarung enthält Compliance-Zusagen

### Zertifizierungs- und Akkreditierungsauslöser

**Verfolgung neuer Zertifizierungen:**

- Entscheidung, ISO 27001, SOC 2, PCI DSS v4.0.1 oder andere Zertifizierung anzustreben
- Zertifizierungsstelle spezifiziert regulatorische Anforderungen als Teil der Zertifizierung
- Branchenspezifische Akkreditierungen mit Compliance-Komponenten

**Zertifizierungspflege:**

- Überwachungsaudit identifiziert neue regulatorische Anforderungen
- Zertifizierungsstandard mit neuen Compliance-Referenzen aktualisiert
- Zertifizierungsstelle gibt neue Leitlinien zu regulatorischen Erwartungen heraus

### Interne Auslöser

**Strategische Initiativen:**

- Geschäftsstrategie sieht Eintritt in regulierte Märkte vor
- Digitale Transformationsinitiative umfasst regulierte Technologien
- Neue Produktentwicklung mit regulatorischen Implikationen

**Risikobewertungsfeststellungen:**

- Informationssicherheits-Risikobewertung identifiziert regulatorische Exponierung
- Datenschutz-Folgenabschätzung zeigt potenzielle regulatorische Anwendbarkeit
- Bedrohungsintelligenz deutet auf regulatorische Durchsetzung im Domäne von [Organisation] hin

**Identifikation von Compliance-Gaps:**

- Internes Audit identifiziert potenziell anwendbare Vorschrift, die nicht in POL-00 enthalten ist
- Mitarbeitender macht auf potenziell anwendbare Vorschrift aufmerksam
- Compliance-Selbstbewertung zeigt Wissenslücke auf

### Externe Auslöser

**Verabschiedung von Vorschriften:**

- Neues Gesetz oder neue Vorschrift in Jurisdiktion, in der [Organisation] tätig ist, verabschiedet
- Regulierungsbehörde gibt neue Regeln oder Leitlinien heraus
- Internationaler Vertrag oder Abkommen mit Compliance-Implikationen

**Branchenentwicklungen:**

- Branchenverband veröffentlicht neue Standards oder Leitlinien
- Vergleichbare Organisationen erhalten regulatorische Durchsetzungsmassnahmen
- Branchen-Arbeitsgruppe empfiehlt Übernahme eines bestimmten Frameworks

**Regulatorische Anfragen:**

- Regulierungsbehörde kontaktiert [Organisation] direkt
- Branchenumfrage einer Regulierungsbehörde
- Regulatorische Untersuchung oder Durchsetzungsmassnahme im Sektor von [Organisation]

## Quellen für regulatorische Intelligence

[Organisation] nutzt folgende Quellen zur Identifikation potenziell anwendbarer Vorschriften:

### Rechtsdatenbanken und Recherchedienste

**Kommerzielle rechtliche Rechercheplattformen:**

- Abonnementbasierte Dienste (z.B. LexisNexis, Westlaw, Bloomberg Law)
- Zugang zu Gesetzen, Vorschriften und Verwaltungsregelungen über Jurisdiktionen hinweg
- Alarmierungsfunktionalität für regulatorische Änderungen
- Durchsuchbar nach Jurisdiktion, Thema, Branche, Inkrafttreten

**Staatliche Rechtsdatenbanken:**

- Offizielle staatliche Repositorys (z.B. EUR-Lex für EU, Bundesblatt für die Schweiz)
- Nationale Gesetzgebungsdatenbanken
- Websites der Regulierungsbehörden
- Kostenlos, aber ggf. ohne erweiterte Suche und Alarmierung

**Regulatory-Technology-(RegTech-)Plattformen:**

- Spezialisierte Compliance-Überwachungsdienste (z.B. Compliance.ai, RegHub)
- KI-gestützte regulatorische Änderungserkennung
- Branchenspezifische regulatorische Verfolgung
- Oft mit Auslegungs- und Auswirkungsanalyse

**Nutzungsleitlinien:**

- Aktuelle Abonnements für primäre rechtliche Rechercheplattform pflegen
- Alarme für Schlüsseljurisdiktionen und -themen konfigurieren
- Regelmässige Schulung des Compliance-Personals zur effektiven Datenbanknutzung
- Suchanfragen und -ergebnisse für Prüfpfad dokumentieren

### Branchenverbände und Normungsgremien

**Sektorspezifische Verbände:**

- Branchenverbände in Sektoren, die [Organisation] bedient
- Verbände veröffentlichen regulatorische Aktualisierungen, Compliance-Leitfäden und Best Practices
- Beispiele: Finanzdienstleistungsverbände, Gesundheitsbranchengruppen, Technologiekonsortien

**Branchenübergreifende Organisationen:**

- Fach- und Berufsverbände für Informationssicherheit und Datenschutz (z.B. IAPP, (ISC)², ISACA)
- Qualitäts- und Compliance-Organisationen (z.B. nationale ISO-Stellen)
- Regionale Unternehmensorganisationen

**Normungsentwicklungsorganisationen:**

- ISO (Internationale Organisation für Normung)
- NIST (National Institute of Standards and Technology)
- CIS (Center for Internet Security)
- Branchenspezifische Normungsgremien

**Nutzungsleitlinien:**

- Mitgliedschaften in relevanten Verbänden pflegen
- Regulatory-Update-Newsletter und Alarme abonnieren
- An Branchen-Arbeitsgruppen zu regulatorischen Themen teilnehmen
- Konferenzen und Webinare zu regulatorischen Entwicklungen besuchen

### Rechtsberater

**Interne Rechtsabteilung:**

- Primäre Quelle für rechtliche Auslegung von Vorschriften
- Überwacht für [Organisation] relevante rechtliche Entwicklungen
- Bietet laufende Rechtsberatung in Compliance-Angelegenheiten
- Koordiniert nach Bedarf mit externen Beratern

**Externe Rechtsberater:**

- Jurisdiktionsspezifische Berater (für internationalen Betrieb)
- Spezialisierte Regulatoren-Berater (z.B. Datenschutz, Finanzregulierung)
- Für spezifische Angelegenheiten oder laufende regulatorische Überwachung mandatiert

**Spezialisierte Regulatoren-Berater:**

- Tiefgehende Expertise in spezifischen regulatorischen Domänen
- Für komplexe Compliance-Fragen mandatiert
- Liefern Stellungnahmen zu regulatorischer Anwendbarkeit und Auslegung

**Nutzungsleitlinien:**

- Regelmässige (mindestens vierteljährliche) rechtliche Kurzinformationen zur regulatorischen Landschaft
- Ständiger Tagesordnungspunkt in Rechts-/Compliance-Besprechungen
- Rechtliche Überprüfung aller Tier-1-Anwendbarkeitsbestimmungen
- Externer Berater für Jurisdiktionen eingebunden, wo [Organisation] keine interne Expertise hat

### Peer-Netzwerke und Berufsgemeinschaften

**Branchenforen:**

- Compliance- und Rechtsforen innerhalb der Branche
- Information Sharing and Analysis Centers (ISACs)
- Peer-Diskussionsgruppen zu regulatorischen Themen

**Berufsverbände:**

- Netzwerke von Compliance-Beauftragten
- Gemeinschaften von Datenschutzbeauftragten
- Berufsgruppen für Informationssicherheit

**Communities of Practice für Compliance:**

- Unternehmensübergreifende Compliance-Zusammenarbeit
- Benchmarking und Austausch bewährter Verfahren
- Diskussionen zur regulatorischen Auslegung

**Nutzungsleitlinien:**

- Aktive Teilnahme an mindestens einem relevanten Peer-Netzwerk
- Designierte Vertreter nehmen an regelmässigen Besprechungen teil
- Erkenntnisse teilen unter Wahrung der Vertraulichkeit
- Peer-Informationen durch verbindliche Quellen verifizieren, bevor gehandelt wird

### Professionelle Dienstleistungsunternehmen

**Wirtschaftsprüfungsgesellschaften:**

- Big-4- und regionale Prüfungsgesellschaften veröffentlichen regulatorische Aktualisierungen
- Branchenspezifische regulatorische Alarme
- Compliance-Beratungsdienstleistungen
- Bieten Mandanten oft kostenlose regulatorische Kurzinformationen

**Compliance-Berater:**

- Spezialisierte regulatorische Compliance-Beratung
- Bewertungen regulatorischer Programme
- Gap-Analyse-Dienstleistungen für Compliance

**Regulatorische Überwachungsdienste:**

- Drittanbieter für regulatorische Änderungsüberwachung
- Kuratierte Alarme und Zusammenfassungen
- Auswirkungsbewertungen und Empfehlungen

**Nutzungsleitlinien:**

- Regulatory-Update-Dienste von Prüfungsgesellschaft oder Berater abonnieren
- Client-Briefings und Webinare besuchen
- Professionelle Dienstleister für komplexe Bewertungen nutzen
- Beziehungen für ad-hoc Konsultationen pflegen

### Kunden- und Lieferantenkanäle

**Kundenanforderungen:**

- Compliance-Klauseln in Rahmendienstleistungsverträgen
- Sicherheits- und Compliance-Fragebögen (z.B. SIG, CAIQ)
- Compliance-Anforderungen in Ausschreibungen
- Compliance-Audits und -Bewertungen durch Kunden

**Lieferantenverpflichtungen:**

- Datenverarbeitungsvereinbarungen (DVAs) mit übernommenen Verpflichtungen
- Unterauftragsverarbeitungsvereinbarungen
- Compliance-Anforderungen in der Lieferkette
- Lieferantenbewertungsfragebögen

**Nutzungsleitlinien:**

- Systematische Überprüfung aller Kundenverträge auf Compliance-Klauseln
- Rechtliche Überprüfung von Lieferantenvereinbarungen auf Durchleitungsverpflichtungen
- Datenbank der vertraglichen Compliance-Anforderungen pflegen
- Vertragliche Anforderungen in den Anwendbarkeitsbewertungsprozess einspeisen

## Erstscreening-Kriterien

Vor der vollständigen Anwendbarkeitsbewertung wendet [Organisation] ein Erstscreening an, um das Universum der Vorschriften auf eine handhabbare Kandidatenmenge zu filtern:

### Relevanzscreening

**Frage**: Betrifft diese Vorschrift Informationssicherheit, Datenschutz, IT-Dienste oder die Informationswerte von [Organisation]?

**Anwenden auf**:

- Vorschriften zur Datensicherheit, zum Datenschutz, zur Cybersicherheit
- Vorschriften zu IT-Diensten, Cloud-Diensten, Managed Services
- Vorschriften zu spezifischen Datentypen, die [Organisation] verarbeitet
- Vorschriften zu Informationssystemen und Technologieinfrastruktur
- Vorschriften mit Informationssicherheitsbestimmungen (auch wenn breiterer Geltungsbereich)

**Ausschliessen**:

- Rein operative Vorschriften ohne Bezug zu Informationen/IT (z.B. Arbeitssicherheit, Umwelt)
- Finanzberichterstattungsvorschriften ohne Informationssicherheitskomponenten
- Produktsicherheitsvorschriften für physische Produkte, die [Organisation] nicht herstellt
- Vorschriften eindeutig ausserhalb des Domäne von [Organisation]

**Ergebnis**: Wenn die Vorschrift NICHT relevant für Informationssicherheit oder IT ist, **STOPP** – keine vollständige Bewertung durchführen. Begründung dokumentieren und in Kategorie „Ausgesiebt – Nicht relevant" ablegen.

### Jurisdiktionsscreening

**Frage**: Hat [Organisation] irgendeinen Bezug zur Jurisdiktion, in der diese Vorschrift gilt?

**Bezüge umfassen**:

- Physische Präsenz (Büro, Einrichtung, Mitarbeitende) in der Jurisdiktion
- In der Jurisdiktion eingetragene juristische Person
- In der Jurisdiktion ansässige Kunden oder betroffene Personen
- Erbringung von Dienstleistungen in die Jurisdiktion (auch ohne physische Präsenz)
- Verarbeitung von Daten, die dem Recht der Jurisdiktion unterliegen
- Vorschrift beansprucht extraterritoriale Reichweite, die [Organisation] betrifft

**Ergebnis**: Wenn [Organisation] KEINERLEI Bezug zur Jurisdiktion hat und die Vorschrift keinen extraterritorialen Anspruch stellt, wahrscheinlich nicht anwendbar. Dennoch vollständige Bewertung durchführen, wenn:

- Unsicherheit über extraterritoriale Reichweite besteht
- Potenzielle künftige Expansion in die Jurisdiktion geplant ist
- Indirekter Bezug über Kunden oder Lieferanten besteht

### Operatives Screening

**Frage**: Fallen die aktuellen oder geplanten Betriebsaktivitäten von [Organisation] in den Geltungsbereich dieser Vorschrift?

**Prüfen**:

- Arten der von [Organisation] erbrachten Dienstleistungen gegenüber dem Geltungsbereich der Vorschrift
- Von [Organisation] bediente Branchen gegenüber den Anwendbarkeitskriterien der Vorschrift
- Von [Organisation] verarbeitete Datentypen gegenüber dem Geltungsbereich der Vorschrift
- Grösse, Umsatz oder andere Schwellenwerte von [Organisation] gegenüber den Anwendbarkeitskriterien der Vorschrift

**Ergebnis**: Wenn die Vorschrift eindeutig NICHT auf den Betrieb von [Organisation] anwendbar ist (z.B. Gesundheitsvorschrift, wenn [Organisation] keine Gesundheitsdienstleistungen erbringt oder Gesundheitsdaten verarbeitet), wahrscheinlich nicht anwendbar. Vollständige Bewertung durchführen, wenn:

- Unsicherheit über den Geltungsbereich besteht
- Potenzielle künftige Aktivitäten eine Anwendbarkeit auslösen könnten
- Partielle Überschneidung mit aktuellen Aktivitäten vorliegt

### Screening-Entscheidungsmatrix

| Relevanz | Jurisdiktion | Betrieb | Entscheidung |
|---------|-------------|---------|--------------|
| NICHT relevant | Beliebig | Beliebig | **STOPP** – Ausgesiebt |
| Relevant | KEIN Bezug | NICHT anwendbar | **STOPP** – Wahrscheinlich nicht anwendbar (dokumentieren) |
| Relevant | KEIN Bezug | Potenziell anwendbar | **FORTFAHREN** – Vollständige Bewertung (potenzielle Zukunft) |
| Relevant | Bezug vorhanden | NICHT anwendbar | **FORTFAHREN** – Vollständige Bewertung (Nichtanwendbarkeit verifizieren) |
| Relevant | Bezug vorhanden | Potenziell anwendbar | **FORTFAHREN** – Vollständige Bewertung |
| Relevant | Bezug vorhanden | Eindeutig anwendbar | **FORTFAHREN** – Vollständige Bewertung (wahrscheinlich anwendbar) |

### Screening-Dokumentation

Für jede gescreente Vorschrift:

- Vorschriftsname, Jurisdiktion, kurze Beschreibung dokumentieren
- Screening-Entscheidung erfassen (Vollständige Bewertung durchführen / Ausgesiebt)
- Begründung für die Entscheidung liefern
- Quelle, wo identifiziert, referenzieren
- Datum und Name des Bewerters

Ausgesiebte Vorschriften werden in einer Datei „Geprüft, aber nicht anwendbar" für eine mögliche künftige Referenz aufbewahrt, falls sich die Umstände ändern.

---

# Anwendbarkeitskriterien-Framework

Für Vorschriften, die das Erstscreening bestehen, führt [Organisation] eine strukturierte Anwendbarkeitsbewertung mit einem **dreidimensionalen Framework** durch:

1. **Geografischer Geltungsbereich**: Anwendbarkeit basierend auf WO [Organisation] tätig ist
2. **Operativer Geltungsbereich**: Anwendbarkeit basierend auf WAS [Organisation] tut
3. **Vertraglicher Geltungsbereich**: Anwendbarkeit basierend auf VEREINBARUNGEN, die [Organisation] eingegangen ist

Jede Dimension wird unabhängig bewertet, dann für eine Gesamtanwendbarkeitsbestimmung kombiniert.

## Bewertung des geografischen Geltungsbereichs

### Kriterien für geografische Anwendbarkeit

**Kriterium G1: Betrieb in der Jurisdiktion**

Frage: Übt [Organisation] Betriebstätigkeiten in der Jurisdiktion aus, in der diese Vorschrift gilt?

Berücksichtigen:

- Physische Büros, Einrichtungen oder Rechenzentren in der Jurisdiktion
- Mitarbeitende, die von der Jurisdiktion aus arbeiten
- In der Jurisdiktion gegründete oder eingetragene juristische Personen
- Geschäftslizenzen oder -genehmigungen in der Jurisdiktion

Nachweis: Handelsregisterunterlagen, Büromietverträge, Beschäftigungsunterlagen, Geschäftslizenzregistrierungen

**Kriterium G2: Kunden oder betroffene Personen in der Jurisdiktion**

Frage: Bedient [Organisation] in der Jurisdiktion ansässige Kunden oder verarbeitet Daten von in der Jurisdiktion ansässigen Personen?

Berücksichtigen:

- Kundenverträge mit in der Jurisdiktion ansässigen Parteien
- Endnutzer, die von der Jurisdiktion aus auf Dienste von [Organisation] zugreifen
- Betroffene Personen, deren Personendaten durch das Recht der Jurisdiktion geschützt sind
- Marketing- oder Vertriebsaktivitäten, die auf die Jurisdiktion ausgerichtet sind

Nachweis: Kundenverträge, Verkaufsdaten, Website-Analysen, Datenverarbeitungsunterlagen

**Kriterium G3: Ausrichtung auf die Jurisdiktion**

Frage: Richtet [Organisation] Aktivitäten aktiv auf Personen oder Einheiten in der Jurisdiktion aus?

Berücksichtigen:

- Website in der Sprache(n) der Jurisdiktion verfügbar
- Preise in der Währung der Jurisdiktion angezeigt
- Marketingkampagnen auf die Jurisdiktion ausgerichtet
- Lokale Zahlungsmethoden akzeptiert
- Compliance mit Verbraucherschutzgesetzen der Jurisdiktion

Nachweis: Website-Inhalte, Marketingmaterialien, Zahlungsgateway-Konfigurationen

**Kriterium G4: Datenverarbeitung in der Jurisdiktion**

Frage: Verarbeitet [Organisation] Daten in der Jurisdiktion, auch wenn [Organisation] keine andere Präsenz hat?

Berücksichtigen:

- Server oder Infrastruktur in der Jurisdiktion
- Drittanbieter-Dienstleister in der Jurisdiktion, die Daten im Auftrag von [Organisation] verarbeiten
- Daten im Transit durch die Jurisdiktion
- Backup- oder Notfallwiederherstellungsstandorte in der Jurisdiktion

Nachweis: Infrastrukturdiagramme, Lieferantenvereinbarungen, Datenfluss-Dokumentation

**Kriterium G5: Extraterritoriale Anwendung**

Frage: Beansprucht die Vorschrift explizit, über die Grenzen der Jurisdiktion hinaus zu gelten?

Berücksichtigen:

- Vorschrift gilt für Organisationen ausserhalb der Jurisdiktion, wenn sie dort ansässige Personen bedienen
- Vorschrift gilt basierend auf dem Aufenthaltsort der betroffenen Person unabhängig vom Standort der Organisation
- Beispiele: DSGVO (EU), CCPA (Kalifornien), LGPD (Brasilien) haben alle extraterritoriale Bestimmungen

Nachweis: Regulatorischer Text, rechtliche Analyse extraterritorialer Bestimmungen

### Bewertung des geografischen Geltungsbereichs – Punktevergabe

Für jedes Kriterium G1–G5:

- **JA** = 1 Punkt
- **NEIN** = 0 Punkte
- **UNGEWISS** = 0,5 Punkte (löst rechtliche Überprüfung aus)

**Punktzahl geografische Anwendbarkeit** = Summe G1 bis G5 (Bereich: 0 bis 5)

**Interpretation**:

- 0–1 Punkte: Geringe geografische Anwendbarkeit
- 2–3 Punkte: Mässige geografische Anwendbarkeit
- 4–5 Punkte: Hohe geografische Anwendbarkeit

Hohe Punktzahl deutet auf starken geografischen Bezug hin, der auf Anwendbarkeit hindeutet. Die Punktzahl allein bestimmt jedoch NICHT die endgültige Anwendbarkeit – alle drei Dimensionen müssen berücksichtigt werden.

## Bewertung des operativen Geltungsbereichs

### Kriterien für operative Anwendbarkeit

**Kriterium O1: Ausrichtung des Dienstleistungstyps**

Frage: Bietet [Organisation] Dienstleistungstypen an, die in den Geltungsbereich der Vorschrift fallen?

Berücksichtigen:

- Cloud-Dienste, Hosting, SaaS (können Cloud-/IT-Dienstleistungsvorschriften auslösen)
- Zahlungsabwicklung (kann Finanzdienstleistungsvorschriften auslösen)
- Gesundheitsdienstleistungen oder Gesundheitsdatenverarbeitung (kann Gesundheitsvorschriften auslösen)
- Telekommunikationsdienste (können Telekommunikationsvorschriften auslösen)
- Kritische Infrastrukturdienste (können Schutzvorschriften für kritische Infrastruktur auslösen)

Nachweis: Dienstleistungskatalog, Dienstleistungsbeschreibungen, Leistungsverzeichnisse, Marketingmaterialien

**Kriterium O2: Ausrichtung des Branchensektors**

Frage: Bedient [Organisation] Branchensektoren, die durch diese Vorschrift reguliert werden?

Berücksichtigen:

- Finanzdienstleistungssektor (Banken, Investmentgesellschaften, Versicherungen)
- Gesundheitssektor (Leistungserbringer, Zahler, Health-Tech)
- Regierungssektor (öffentlicher Sektor, Verteidigung)
- Sektoren kritischer Infrastruktur (Energie, Wasser, Verkehr)
- Vorschrift kann auch für Dienstleister AN diesen Sektoren gelten, auch wenn nicht direkt im Sektor tätig

Nachweis: Kundenliste, Vertikalmarktanalyse, branchenspezifische Verträge

**Kriterium O3: Ausrichtung des Datentyps**

Frage: Verarbeitet [Organisation] Datentypen, die durch diese Vorschrift geschützt oder reguliert werden?

Berücksichtigen:

- Personendaten / Persönlich identifizierbare Informationen (PII)
- Besondere Kategorien von Personendaten (Gesundheit, biometrische, genetische, Rasse/Ethnizität etc.)
- Finanzdaten (Zahlungskartendaten, Bankdaten, Finanzkontoinformationen)
- Staatliche Daten (klassifiziert, kontrolliert unklassifiziert, Strafverfolgungsdaten)
- Geschäftsgeheimnisse oder vertrauliche Geschäftsinformationen
- Daten von Kindern

Nachweis: Dateninventar, Datenklassifizierungsregister, Datenflussdiagramme, Datenverarbeitungsunterlagen

**Kriterium O4: Organisatorische Merkmale**

Frage: Erfüllt [Organisation] die Anwendbarkeitsschwellenwerte der Vorschrift basierend auf Grösse, Umsatz oder anderen Merkmalen?

Berücksichtigen:

- Anzahl der Mitarbeitenden (manche Vorschriften gelten nur ab einem Schwellenwert)
- Jahresumsatz oder -einkommen (finanzielle Schwellenwerte)
- Volumen der verarbeiteten Daten (z.B. Anzahl der betroffenen Personen)
- Öffentliche vs. private Einheit
- Gewinn- vs. Non-Profit-Orientierung
- Organisatorische Struktur (Tochtergesellschaft eines regulierten Mutterunternehmens)

Nachweis: Jahresabschlüsse, Mitarbeiterzahlberichte, Datenverarbeitungsvolumen-Metriken, Unternehmensstruktur-Dokumente

**Kriterium O5: Spezifisch abgedeckte Aktivitäten**

Frage: Führt [Organisation] spezifische Aktivitäten durch, die explizit durch die Vorschrift abgedeckt werden?

Berücksichtigen:

- E-Commerce-Betrieb (kann Verbraucherschutz-/E-Commerce-Vorschriften auslösen)
- Grenzüberschreitende Datenübermittlungen (können Datenübermittlungsvorschriften auslösen)
- Automatisierte Entscheidungsfindung oder Profiling (können KI-/Algorithmus-Vorschriften auslösen)
- Marketing/Werbung mit Personendaten (kann Marketingvorschriften auslösen)
- Biometrische Authentifizierung/Identifikation (können biometrische Vorschriften auslösen)

Nachweis: Operative Dokumentation, technologische Dokumentation, Prozessbeschreibungen

### Bewertung des operativen Geltungsbereichs – Punktevergabe

Für jedes Kriterium O1–O5:

- **JA** = 1 Punkt
- **NEIN** = 0 Punkte
- **UNGEWISS** = 0,5 Punkte (löst weitere Analyse aus)

**Punktzahl operative Anwendbarkeit** = Summe O1 bis O5 (Bereich: 0 bis 5)

**Interpretation**:

- 0–1 Punkte: Geringe operative Anwendbarkeit
- 2–3 Punkte: Mässige operative Anwendbarkeit
- 4–5 Punkte: Hohe operative Anwendbarkeit

## Bewertung des vertraglichen Geltungsbereichs

### Kriterien für vertragliche Anwendbarkeit

**Kriterium V1: Vertragliche Kundenanforderungen**

Frage: Erfordern die Kundenverträge von [Organisation] explizit die Einhaltung dieser Vorschrift?

Berücksichtigen:

- Rahmendienstleistungsverträge mit Compliance-Klauseln
- Datenverarbeitungsvereinbarungen mit Auftragsverarbeitungs-Compliance-Anforderungen
- Leistungsverzeichnisse mit spezifischen regulatorischen Anforderungen
- Compliance-Fragebögen von Kunden mit Konformitätserwartungen
- Auditrechtsklauseln zur regulatorischen Compliance

Nachweis: Ausgeführte Kundenverträge, Compliance-Anforderungsmatrizen, Kundenauditberichte

**Kriterium V2: Lieferanten-Durchleitungsverpflichtungen**

Frage: Schaffen die Vereinbarungen von [Organisation] mit Lieferanten Verpflichtungen für [Organisation], diese Vorschrift einzuhalten?

Berücksichtigen:

- [Organisation] als Unterauftragsverarbeiter mit Verpflichtungen aus dem primären Auftragsverarbeiter
- Compliance-Anforderungen in der Lieferkette
- Lieferant, der von [Organisation] verlangt, die Standards einzuhalten, die der Lieferant einhalten muss
- Weiterleitungsklauseln aus Hauptverträgen

Nachweis: Lieferantenvereinbarungen, Unterauftragsverarbeitungsvereinbarungen, Lieferkettenverträge

**Kriterium V3: Zertifizierungsanforderungen**

Frage: Ist die Einhaltung dieser Vorschrift für Zertifizierungen erforderlich, die [Organisation] hält oder anstrebt?

Berücksichtigen:

- ISO 27001 kann auf spezifische regulatorische Anforderungen verweisen
- SOC 2 Typ II kann regulatorische Compliance in Kriterien einschliessen
- Branchenspezifische Zertifizierungen mit regulatorischer Compliance-Anforderung
- Zertifizierungsstelle erfordert explizit Konformität mit Vorschrift

Nachweis: Zertifizierungsstandards, Zertifizierungsstellenanforderungen, Auditberichte, Bewerter-Leitlinien

**Kriterium V4: Freiwillige Verpflichtungen**

Frage: Hat [Organisation] öffentliche Zusagen oder freiwillige Verpflichtungen zur Einhaltung dieser Vorschrift oder dieses Frameworks gemacht?

Berücksichtigen:

- Datenschutzrichtlinien, die Compliance mit spezifischen Vorschriften erklären
- Marketingmaterialien, die Zertifizierungen oder Compliance behaupten
- Öffentliche Verpflichtungen zu Frameworks
- Verhaltenskodizes oder Branchenerklärungen

Nachweis: Veröffentlichte Datenschutzrichtlinien, Website-Erklärungen, Marketingmaterialien, Pressemitteilungen

### Bewertung des vertraglichen Geltungsbereichs – Punktevergabe

Für jedes Kriterium V1–V4:

- **JA** = 1 Punkt
- **NEIN** = 0 Punkte
- **UNGEWISS** = 0,5 Punkte

**Punktzahl vertragliche Anwendbarkeit** = Summe V1 bis V4 (Bereich: 0 bis 4)

**Interpretation**:

- 0 Punkte: Keine vertragliche Anwendbarkeit
- 1–2 Punkte: Mässige vertragliche Anwendbarkeit
- 3–4 Punkte: Hohe vertragliche Anwendbarkeit

## Kombinierte Anwendbarkeitsbestimmung

### Dimensionsgewichtung

Alle drei Dimensionen haben gleiches Gewicht bei der Bestimmung. Eine Vorschrift kann anwendbar sein aufgrund eines starken Ergebnisses in einer Dimension ODER mässiger Ergebnisse über mehrere Dimensionen.

### Anwendbarkeits-Entscheidungslogik

**ANWENDBAR** (In ISMS-POL-00 aufnehmen):

- Hohe Punktzahl (4–5) in EINER Dimension, ODER
- Mässige Punktzahlen (2–3) in ZWEI ODER MEHR Dimensionen, ODER
- Explizite vertragliche Anforderung (V1 oder V2 = JA), ODER
- Rechtsgutachten bestätigt Anwendbarkeit

**BEDINGT ANWENDBAR** (In ISMS-POL-00 als Tier 2 aufnehmen):

- Mässige Punktzahl (2–3) in NUR EINER Dimension
- Potenzielle künftige Anwendbarkeit (Expansionspläne)
- Freiwillige Übernahme für Wettbewerbsvorteil

**NICHT ANWENDBAR** (Nicht in ISMS-POL-00 aufnehmen):

- Geringe Punktzahlen (0–1) über ALLE Dimensionen
- Vorschrift schliesst Betriebsaktivitäten von [Organisation] explizit aus
- Rechtsgutachten bestätigt Nichtanwendbarkeit

### Sonderfälle

**Ungewisse Bestimmungen:**
Wenn Anwendbarkeit nach Bewertung ungewiss ist:

- An Rechtsberater zur Auslegung eskalieren
- Einschaltung externer Regulatoren-Berater erwägen
- Unsicherheit und Entscheidung zur Aufnahme/zum Ausschluss dokumentieren
- Auf klärende Leitlinien der Regulierungsbehörde überwachen
- Standard: „Bedingt anwendbar" (Tier 2), wenn Zweifel bestehen bleibt

**Widersprüchliche Indikatoren:**
Wenn manche Kriterien auf Anwendbarkeit und andere auf Nichtanwendbarkeit hindeuten:

- Rechtsberater trifft endgültige Bestimmung
- Vertragliche Anforderungen (V1, V2) werden besonders gewichtet, da sie Verpflichtungen unabhängig von rechtlicher Anwendbarkeit begründen
- Konflikt und Begründung für endgültige Entscheidung dokumentieren

---

# Drei-Tier-Kategorisierungs-Framework

Als anwendbar bestimmte Vorschriften werden in ISMS-POL-00 in einen von drei Tiers eingeordnet:

## Tier 1: Obligatorische Compliance

### Definition

Vorschriften in Tier 1 sind solche mit **RECHTLICHER VERPFLICHTUNG** oder **DURCHSETZBARER VERTRAGLICHER ANFORDERUNG**.

Nichteinhaltung führt zu konkreten rechtlichen oder vertraglichen Konsequenzen: regulatorische Bussen, Sanktionen, Lizenzentzug, Vertragsstrafen oder Verlust von Geschäftsbeziehungen.

### Zuordnungskriterien

Eine Vorschrift MUSS als Tier 1 eingestuft werden, wenn sie EINES der folgenden Kriterien erfüllt:

**Rechtliche Verpflichtung:**

- Gesetz oder Vorschrift, das/die in den Jurisdiktionen, in denen [Organisation] tätig ist, rechtlich bindend ist
- Hohe Punktzahl für geografische Anwendbarkeit (4–5) UND Vorschrift enthält verbindliche Anforderungen („muss", „ist verpflichtend")
- Regulierungsbehörde hat Zuständigkeit für [Organisation] und Durchsetzungsbefugnis
- Nichtkonformität kann zu Bussen, Sanktionen oder anderen rechtlichen Strafen führen

**Vertragliche Durchsetzbarkeit:**

- Kundenvertrag erfordert explizit Compliance und enthält Durchsetzungsmechanismen (Strafen, Kündigungsrechte)
- Lieferantenvereinbarung schafft durchsetzbare Durchleitungsverpflichtung
- Vertragliche Verpflichtung mit wesentlichen finanziellen oder geschäftlichen Konsequenzen bei Verletzung

**Zertifizierungsanforderung:**

- Konformität erforderlich für Zertifizierung, die [Organisation] hält (z.B. ISO 27001, SOC 2)
- Zertifizierungsstelle prüft Compliance mit Vorschrift
- Verlust der Zertifizierung hätte wesentliche Geschäftsauswirkungen

### Behandlung von Tier-1-Vorschriften

Tier-1-Vorschriften erhalten höchste Priorität:

- **Vollständige Compliance erforderlich** – keine Ausnahmen ohne dokumentierte Risikoakzeptanz
- **Genehmigung der Geschäftsleitung erforderlich** zur Aufnahme in Tier 1 (Ressourcenverpflichtung)
- **Obligatorische Anforderungsextraktion** (POL-5.31.3, IMP-5.31.2)
- **Obligatorische Massnahmenzuordnung** (POL-5.31.3, IMP-5.31.3)
- **Hochprioritäre Gap-Behebung** – Gaps müssen adressiert oder formal akzeptiert werden
- **Regelmässige Compliance-Audits** (intern und potenziell extern)
- **Kontinuierliche Nachweis-Erhebung** und -Pflege
- **Mindestens jährliche Überprüfung** – häufiger bei aktiv sich ändernden Vorschriften

### Beispiele für Tier-1-Klassifizierungen (Generisch)

- Datenschutzgesetz in Jurisdiktion, in der [Organisation] Betrieb unterhält und Personendaten verarbeitet
- Finanzdienstleistungsvorschrift, bei der [Organisation] IT-Dienste für Finanzinstitute erbringt und als Dienstleister designiert ist
- Kundenvertrag mit Fortune-500-Kunden, der SOC-2-Compliance mit Vertragsstrafen bei Nichtkonformität erfordert
- ISO-27001-Standard (wenn [Organisation] zertifiziert ist)

## Tier 2: Bedingte Anwendbarkeit

### Definition

Vorschriften in Tier 2 sind solche, die **IN ZUKUNFT ANWENDBAR WERDEN KÖNNTEN** oder aus strategischen Gründen **FREIWILLIG ÜBERNOMMEN** werden.

Diese sind derzeit rechtlich nicht bindend, werden aber von [Organisation] überwacht aufgrund potenzieller künftiger Anwendbarkeit oder weil eine freiwillige Übernahme einen Wettbewerbs- oder strategischen Vorteil bietet.

### Zuordnungskriterien

Eine Vorschrift MUSS als Tier 2 eingestuft werden, wenn sie EINES der folgenden Kriterien erfüllt:

**Potenzielle künftige Anwendbarkeit:**

- [Organisation] erwägt Expansion in Jurisdiktion, in der Vorschrift gilt
- [Organisation] plant, Dienstleistungen anzubieten, die Anwendbarkeit auslösen würden
- [Organisation] könnte in durch Vorschrift abgedeckten Branchensektor eintreten
- Vorgeschlagene oder geplante Vorschrift, die wahrscheinlich verabschiedet wird und [Organisation] betrifft
- Schwellenwerte aktuell nicht erfüllt, könnten aber mit Wachstum erfüllt werden

**Freiwillige Übernahme:**

- Framework für branchenbeste Praxis, das [Organisation] zu übernehmen wählt
- Wettbewerbsdifferenzierung (Compliance überschreitet Anforderungen)
- Kundenerwartungen oder Marktanforderungen (auch ohne vertragliche Verpflichtung)
- Regulatorischer Safe Harbor oder bevorzugter Ansatz
- Strategische Positionierung für künftige Chancen

**Regulatorische Unsicherheit:**

- Anwendbarkeitsbewertung ist ungewiss (mässige Punktzahlen, unklarer Geltungsbereich)
- Extraterritoriale Reichweite ist mehrdeutig
- Rechtliche Klärung oder regulatorische Leitlinien werden erwartet
- Standard: Tier 2, bis Klarheit besteht

### Behandlung von Tier-2-Vorschriften

Tier-2-Vorschriften erhalten mässige Priorität:

- **Überwachung und Bereitschaft** – über Änderungen auf dem Laufenden bleiben
- **Gap-Analyse** zum Verständnis des Compliance-Aufwands bei/nach Auslösung
- **Teilweise Implementierung** kann erfolgen, wenn strategisch wertvoll
- **Anforderungsextraktion** optional (empfohlen bei hoher Wahrscheinlichkeit künftiger Anwendbarkeit)
- **Jährliche oder zweijährliche Überprüfung** – beurteilen, ob sich Umstände geändert haben, die einen Wechsel zu Tier 1 auslösen
- **Strategische Begründung dokumentieren** für freiwillige Übernahme, falls zutreffend

### Beispiele für Tier-2-Klassifizierungen (Generisch)

- Datenschutzvorschrift in Jurisdiktion, in die [Organisation] zu expandieren erwägt
- Branchenspezifische Vorschrift für vertikalen Markt, in den [Organisation] eintreten könnte
- Aufkommende Vorschrift (Entwurf/Vorschlag), die [Organisation] nach Verabschiedung voraussichtlich betrifft
- NIST Cybersecurity Framework (CSF) 2.0, freiwillig für Reifegradbeurteilung übernommen

## Tier 3: Informativer Verweis

### Definition

Vorschriften und Frameworks in Tier 3 werden nur zur **ORIENTIERUNG**, zum **BENCHMARKING** oder als **BEST PRACTICES** genutzt.

Es besteht KEINE Compliance-Verpflichtung (rechtlich oder vertraglich), aber diese Frameworks informieren das Massnahmendesign von [Organisation] und bieten Referenzpunkte für die Reifegradbeurteilung.

### Zuordnungskriterien

Eine Vorschrift oder ein Framework MUSS als Tier 3 eingestuft werden, wenn:

**Keine Compliance-Verpflichtung:**

- Geringe Anwendbarkeitspunktzahlen über alle drei Dimensionen
- Keine rechtliche Compliance-Anforderung
- Keine vertragliche Compliance-Anforderung
- Für keine Zertifizierung, die [Organisation] hält, erforderlich

**Wertvoll als Referenz:**

- Branchenweit anerkannte Best Practice
- Von Vergleichsorganisationen zum Benchmarking genutzt
- Bietet nützliche Orientierung für das Massnahmendesign
- Von anderen anwendbaren Vorschriften referenziert
- Unterstützt Reifegradbeurteilung und Verbesserungsbemühungen

### Behandlung von Tier-3-Vorschriften

Tier-3-Vorschriften erhalten minimale formelle Behandlung:

- **Referenz für Massnahmendesign** – bei Implementierung oder Verbesserung von Massnahmen konsultiert
- **Benchmarking** gegen Branchenstandards
- **Keine Nachweisanforderungen** – keine Verpflichtung zur Konformitätsdemonstration
- **Periodische Überprüfung** (zweijährlich oder nach Bedarf) – beurteilen, ob weiterhin nützliche Referenz
- **Kann informieren, erfordert aber nicht** – Massnahmen können von Tier-3-Frameworks inspiriert sein, aber keine Verpflichtung

### Beispiele für Tier-3-Klassifizierungen (Generisch)

- CIS Controls (Critical Security Controls des Center for Internet Security)
- NIST Cybersecurity Framework (wenn nicht freiwillig gemäss Tier 2 übernommen)
- OWASP-Leitlinien (Open Web Application Security Project)
- Branchenspezifische Best-Practice-Leitfäden ohne regulatorische Kraft

## Tier-Zuordnungs-Entscheidungsbaum

```
START: Vorschrift hat Erstscreening bestanden
    ↓
Besteht eine RECHTLICHE Verpflichtung?
(Vorschrift ist Gesetz in Jurisdiktion, in der [Org] tätig ist
 UND gilt für Betriebsaktivitäten von [Org])
    ├─ JA → TIER 1 (Obligatorische Compliance)
    └─ NEIN → Weiter
        ↓
Besteht eine DURCHSETZBARE vertragliche Anforderung?
(Kunden-/Lieferantenvertrag erfordert Compliance
 MIT Durchsetzungsmechanismus)
    ├─ JA → TIER 1 (Obligatorische Compliance)
    └─ NEIN → Weiter
        ↓
Ist Compliance für eine Zertifizierung ERFORDERLICH, die [Org] hält?
(ISO 27001, SOC 2 etc. erfordert dies)
    ├─ JA → TIER 1 (Obligatorische Compliance)
    └─ NEIN → Weiter
        ↓
Besteht POTENZIELLE KÜNFTIGE Anwendbarkeit?
(Expansionspläne, Wachstumspfad, vorgeschlagene Vorschrift)
    ├─ JA → TIER 2 (Bedingte Anwendbarkeit)
    └─ NEIN → Weiter
        ↓
Übernimmt [Org] FREIWILLIG aus strategischen Gründen?
(Wettbewerbsvorteil, Kundenerwartungen)
    ├─ JA → TIER 2 (Bedingte Anwendbarkeit)
    └─ NEIN → Weiter
        ↓
Ist dies nützlich als ORIENTIERUNG/BENCHMARKING?
(Branchenbeste Praxis, Reifegradbeurteilungsreferenz)
    ├─ JA → TIER 3 (Informativer Verweis)
    └─ NEIN → NICHT IN POL-00 AUFNEHMEN
              (Nicht anwendbar, in „Ausgesiebt" ablegen)
```

## Tier-Mobilität

Vorschriften können sich bei sich ändernden Umständen zwischen Tiers bewegen:

**Tier 2 → Tier 1:**

- [Organisation] expandiert in Jurisdiktion (Potenzial wird Realität)
- Vorgeschlagene Vorschrift wird verabschiedet
- Kundenvertrag hinzugefügt, der Compliance erfordert
- [Organisation] erreicht Schwellenwert, der Anwendbarkeit auslöst

**Tier 1 → Tier 2:**

- [Organisation] verlässt Jurisdiktion oder stellt relevante Betriebstätigkeiten ein
- Vorschrift wird aufgehoben oder wesentlich geändert, um [Organisation] auszuschliessen
- Vertrag läuft aus ohne Erneuerung

**Tier 3 → Tier 2:**

- [Organisation] entscheidet, Framework aus strategischen Gründen freiwillig zu übernehmen

**Beliebiger Tier → Entfernt:**

- Vorschrift wird vollständig aufgehoben
- [Organisation] stellt nach der Erstklassifizierung endgültig Nichtanwendbarkeit fest
- Framework wird ersetzt oder ist nicht mehr nützlich

Tier-Änderungen erfordern eine Neubewertung mit der vollständigen Anwendbarkeitsmethodik und entsprechender Genehmigung (siehe Abschnitt 5).

---

# Dokumentations- und Genehmigungsanforderungen

## Dokumentation der Anwendbarkeitsbewertung

Für jede bewertete Vorschrift (ob als anwendbar bestimmt oder nicht) erstellt und pflegt [Organisation] umfassende Dokumentation:

### Erforderliche Dokumentationselemente

**Vorschriftsidentifikation:**

- Vollständiger Vorschriftsname und gebräuchliche Abkürzung
- Jurisdiktion (Land, Kanton/Bundesland, multijurisdiktionell)
- Herausgebende Behörde (Gesetzgebungskörper, Regulierungsbehörde)
- Inkrafttreten und etwaige Übergangszeiträume
- Quelle, wo identifiziert (Datenbank, Berater, Kunde etc.)

**Bewertungszusammenfassung:**

- **Bewertung des geografischen Geltungsbereichs:**
  - Antwort auf jedes Kriterium G1–G5 (Ja/Nein/Ungewiss)
  - Punktzahl geografische Anwendbarkeit
  - Unterstützende Begründung und Nachweise
- **Bewertung des operativen Geltungsbereichs:**
  - Antwort auf jedes Kriterium O1–O5 (Ja/Nein/Ungewiss)
  - Punktzahl operative Anwendbarkeit
  - Unterstützende Begründung und Nachweise
- **Bewertung des vertraglichen Geltungsbereichs:**
  - Antwort auf jedes Kriterium V1–V4 (Ja/Nein/Ungewiss)
  - Punktzahl vertragliche Anwendbarkeit
  - Unterstützende Begründung und Nachweise

**Gesamtbestimmung:**

- Anwendbarkeitsschlussfolgerung (Anwendbar / Bedingt anwendbar / Nicht anwendbar)
- Tier-Zuweisung (1, 2, 3 oder entfällt)
- Detaillierte Begründung, die die dreidimensionale Bewertung synthetisiert
- Besondere Überlegungen oder Grenzfälle
- Abweichende Meinungen oder Unsicherheitsbereiche

**Unterstützende Nachweise:**

- Links zu oder Kopien des regulatorischen Texts
- Rechtsgutachten oder Memoranda
- Vertragsauszüge (wenn vertraglich bedingt)
- Jurisdiktionsanalyse
- Präzedenzfall aus ähnlichen Vorschriften oder Vergleichsorganisationen

**Bewertungsmetadaten:**

- Name und Rolle des Bewerters
- Bewertungsdatum
- Name und Rolle des Prüfers (falls von Peer überprüft)
- Genehmiger und Genehmigungsdatum/Daten
- Nächstes Überprüfungsdatum

### Dokumentationsvorlagen

**Bewertungsarbeitsbuch 2: Anwendbarkeitsmatrix** stellt eine standardisierte Vorlage für die Dokumentation bereit. Alle Bewertungen werden mit dieser Vorlage dokumentiert, um Konsistenz zu gewährleisten.

Die Vorlage enthält:

- Strukturiertes Formular für die dreidimensionale Bewertung
- Bewertungsformeln
- Entscheidungsbaum für die Tier-Zuweisung
- Genehmigungsunterschriftenfelder
- Versionskontrolle

### Nachweisaufbewahrung

Unterstützende Nachweise werden an die Anwendbarkeitsbewertungsdokumentation angehängt oder dort referenziert und gemäss der Unterlagenaufbewahrungsrichtlinie aufbewahrt (Minimum: Dauer der Anwendbarkeit + 7 Jahre oder gemäss regulatorischer Anforderung).

## Genehmigungsworkflow

### Bewertungs- und Überprüfungsstufen

**Stufe 1: Erstbewertung**

- Durchgeführt von: Compliance-Beauftragter oder designiertes Rechts-/Compliance-Personal
- Aktivitäten: Vollständige dreidimensionale Bewertung abschliessen, Bestimmung entwerfen
- Ergebnis: Entwurf des Anwendbarkeitsbewertungsdokuments
- Zeitplan: Innerhalb von 10 Werktagen nach Auslöseereignis (oder gemäss IMP-5.31.1-Zeitplan)

**Stufe 2: Peer-Review** (Empfohlen für alle; Obligatorisch für Tier 1)

- Durchgeführt von: Zweiter Compliance-/Rechtsexperte
- Aktivitäten: Bewertung auf Vollständigkeit, Logik und Nachweisqualität prüfen
- Ergebnis: Peer-Review-Kommentare, Empfehlung zum Fortfahren oder zur Überarbeitung
- Zeitplan: Innerhalb von 5 Werktagen nach Erstbewertung

**Stufe 3: Rechtliche Überprüfung** (Obligatorisch für Tier 1; Optional für Tier 2/3)

- Durchgeführt von: Interne Rechtsabteilung (oder externe Berater für Jurisdiktionen ohne interne Expertise)
- Aktivitäten: Rechtliche Auslegung validieren, Anwendbarkeitsbestimmung bestätigen
- Ergebnis: Rechtliche Genehmigung oder Überarbeitungsanforderung, ggf. Rechtsgutachten
- Zeitplan: Innerhalb von 10 Werktagen nach Peer-Review

**Stufe 4: ISMS-Manager-Überprüfung** (Alle Tiers)

- Durchgeführt von: ISMS-Manager
- Aktivitäten: ISMS-Implikationen prüfen, Integration mit bestehendem Framework berücksichtigen
- Ergebnis: ISMS-Manager-Genehmigung oder Bedenken
- Zeitplan: Innerhalb von 5 Werktagen nach rechtlicher Überprüfung (oder Stufe 2, wenn keine rechtliche Überprüfung)

**Stufe 5: Genehmigung der Geschäftsleitung** (Obligatorisch für Tier 1; Nicht erforderlich für Tier 2/3)

- Durchgeführt von: Geschäftsleitung (gemäss Definition in POL-5.31.1 Rollen)
- Aktivitäten: Compliance-Verpflichtung anerkennen, Ressourcen zusagen, Aufnahme in Tier 1 genehmigen
- Ergebnis: Genehmigungsunterschrift der Geschäftsleitung
- Zeitplan: Innerhalb von 10 Werktagen nach ISMS-Manager-Überprüfung
- Hinweis: Genehmigung der Geschäftsleitung signalisiert organisatorisches Bekenntnis zur Compliance

### Genehmigungsbefugnis-Matrix

| Tier | Compliance-Beauftragter | Rechtsberater | ISMS-Manager | Geschäftsleitung |
|------|------------------------|---------------|--------------|-----------------|
| **Tier 1** | Bewertet (V) | Prüft & Genehmigt (A) | Prüft & Genehmigt (A) | **Genehmigt** (A) |
| **Tier 2** | Bewertet (V) | Prüft (B) | **Genehmigt** (A) | Informiert (I) |
| **Tier 3** | Bewertet (V) | Optional (B) | **Genehmigt** (A) | Informiert (I) |

V=Verantwortlich, A=Accountable/Genehmigt, B=Beratend, I=Informiert

### Beschleunigter Genehmigungsprozess

In dringenden Situationen (z.B. Kundenvertragsabschluss abhängig von Compliance-Zusage, unmittelbare regulatorische Frist) kann ein beschleunigter Genehmigungsprozess genutzt werden:

- Zeitpläne auf 2–3 Werktage pro Stufe verkürzen
- Parallele Überprüfungsstufen wo möglich
- Mündliche Genehmigungen akzeptabel mit dokumentierter Nachunterzeichnung innerhalb von 5 Werktagen
- Eskalation zur höchsten verfügbaren Instanz, wenn designierter Genehmiger nicht verfügbar
- **Alle beschleunigten Genehmigungen unterliegen einem Post-Genehmigungs-Audit** innerhalb von 30 Tagen zur Validierung der Prozessintegrität

Der beschleunigte Prozess erfordert Autorisierung durch den ISMS-Manager und Dokumentation der Dringlichkeitsbegründung.

### Bestrittene Bestimmungen

Wenn Bewerter, Prüfer oder Genehmiger bei der Anwendbarkeit oder Tier-Zuweisung nicht übereinstimmen:

**Interne Lösung:**

- Compliance-Beauftragter und ISMS-Manager besprechen und suchen Konsens
- Rechtsberater liefert definitive Auslegung in Rechtsangelegenheiten
- Wenn intern kein Konsens erzielt werden kann, an Geschäftsleitung eskalieren

**Externe Lösung:**

- Bei komplexen Rechtsfragen: Externen Rechtsberater für Gutachten einschalten
- Für regulatorische Auslegung: Direkte Anfrage an Regulierungsbehörde erwägen (mit Rechtsberater-Leitlinien)
- Streit, Lösungsprozess und endgültige Entscheidung mit unterstützender Begründung dokumentieren

**Standardposition:**

- Wenn nach Lösungsbemühungen Zweifel bestehen: Standard „Anwendbar" und höherer Tier (Tier 1 über Tier 2, Tier 2 über Tier 3)
- Begründung: Konservativer Ansatz reduziert Risiko der Nichtkonformität
- Neubewertung, wenn zusätzliche Klarheit verfügbar wird

## Aufnahme in ISMS-POL-00

Nach der endgültigen Genehmigung der Anwendbarkeitsbestimmung:

### POL-00-Eintrag

Der ISMS-Manager nimmt die Vorschrift im entsprechenden Tier-Abschnitt in ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen) auf mit folgenden Informationen:

- Vorschrifts-ID (systematisch zugewiesen, z.B. REG-001, REG-002)
- Vorschriftsname
- Jurisdiktion
- Herausgebende Behörde
- Inkrafttreten
- Tier (1, 2 oder 3)
- Anwendbarkeitsstatus (Anwendbar, Bedingt anwendbar)
- Kurze Anwendbarkeitsbegründung (1–2 Sätze)
- Link zur vollständigen Anwendbarkeitsbewertungsdokumentation
- Letztes Überprüfungsdatum
- Nächstes Überprüfungsdatum (jährlich für Tier 1, zweijährlich für Tier 2/3 oder wie bestimmt)
- Verantwortliche Partei (typischerweise Compliance-Beauftragter)

### Versionskontrolle

- POL-00-Versionsnummer erhöhen
- Versionshistorie-Tabelle mit Datum, Autor und Zusammenfassung der Änderung aktualisieren („REG-XXX [Vorschriftsname] zu Tier [X] hinzugefügt")
- Aktualisiertes POL-00 gemäss Verteilerliste an Stakeholder verteilen

### Kommunikation

Compliance-Beauftragter oder ISMS-Manager benachrichtigt relevante Stakeholder:

**Für Tier-1-Ergänzungen:**

- Geschäftsleitung (formelle Benachrichtigung)
- Alle Massnahmenverantwortlichen (breite Sensibilisierung)
- Betroffene Geschäftsbereiche (wenn Vorschrift spezifische Betriebsaktivitäten betrifft)
- Interne Revision (für Auditplanung)
- Kundenbezogene Teams (wenn durch Kunden getriebene Anforderung)

**Für Tier-2/3-Ergänzungen:**

- ISMS-Manager
- Betroffene Massnahmenverantwortliche (gezielte Benachrichtigung)
- Compliance-Team

**Kommunikationsinhalt:**

- Hinzugefügte Vorschrift und Tier
- Übergeordnete Implikationen
- Nächste Schritte (z.B. Anforderungsextraktion geplant)
- Ansprechpartner für Fragen

### Auslösung nachgelagerter Prozesse

Die Aufnahme einer Vorschrift in POL-00 Tier 1 oder 2 löst aus:

- **Anforderungsextraktion** (POL-5.31.3, IMP-5.31.2): Extraktion spezifischer Anforderungen aus der Vorschrift planen
- **Massnahmenzuordnung** (POL-5.31.3, IMP-5.31.3): Nach der Anforderungsextraktion Massnahmen zuordnen
- **Gap-Analyse**: Compliance-Gaps identifizieren
- **Nachweisplanung** (POL-5.31.4, IMP-5.31.5): Nachweisanforderungen bestimmen

ISMS-Manager koordiniert diese nachgelagerten Aktivitäten.

---

# Überprüfungshäufigkeit und Aktualisierungsauslöser

Anwendbarkeitsbestimmungen sind nicht statisch. [Organisation] überprüft und aktualisiert Anwendbarkeitsbewertungen gemäss folgendem Zeitplan und folgenden Auslösern:

## Periodischer Überprüfungsplan

### Jährliche umfassende Überprüfung (Obligatorisch)

**Umfang**: ALLE Vorschriften in ISMS-POL-00 (Tiers 1, 2 und 3)

**Zeitpunkt**: Q4 jeden Kalenderjahres (oder alternativer im ISMS-Management-Review-Zyklus definierter Zeitplan)

**Prozess**:
1. Compliance-Beauftragter überprüft jede Vorschrift in POL-00
2. Bestätigt, dass sich die Umstände von [Organisation] nicht in anwendbarkeitsrelevanter Weise geändert haben
3. Bestätigt, dass die Vorschrift selbst nicht in anwendbarkeitsrelevanter Weise geändert wurde
4. Validiert, dass die Tier-Zuweisung weiterhin angemessen ist
5. Überprüfungsdatum und Ergebnis dokumentieren („Keine Änderung", „Tier geändert", „Entfernt" etc.)
6. Felder „Letztes Überprüfungsdatum" und „Nächstes Überprüfungsdatum" in POL-00 aktualisieren

**Dokumentation**: Zusammenfassungsbericht der jährlichen Überprüfung mit Umfang, Feststellungen und etwaigen Änderungen

**Genehmigung**: Genehmigung des Zusammenfassungsberichts der jährlichen Überprüfung durch ISMS-Manager

### Tierspezifische Überprüfungshäufigkeit

**Tier-1-Vorschriften**:

- Minimum: Jährliche Überprüfung (gemäss 6.1.1)
- Empfohlen: Halbjährliche Überprüfung für schnell entwickelnde Vorschriften
- Obligatorisch: Ereignisgesteuerte Überprüfung (Abschnitt 6.2) hat Vorrang vor geplanten Überprüfungen

**Tier-2-Vorschriften**:

- Minimum: Jährliche Überprüfung (gemäss 6.1.1)
- Alternative: Zweijährliche Überprüfung akzeptabel für stabile Frameworks mit geringer Änderungswahrscheinlichkeit

**Tier-3-Vorschriften**:

- Minimum: Zweijährliche Überprüfung
- Kann „nach Bedarf" basierend auf der Nutzung des Frameworks als Referenz durch [Organisation] überprüft werden

## Ereignisgesteuerte Überprüfungsauslöser

Die Anwendbarkeitsbewertung wird (ausserhalb geplanter Überprüfungen) ausgelöst durch:

### Organisatorische Änderungen

**Geografische Expansion oder Kontraktion:**

- [Organisation] tritt in neue Jurisdiktion ein → Vorschriften in dieser Jurisdiktion überprüfen
- [Organisation] verlässt Jurisdiktion → Vorschriften überprüfen, die von der Präsenz dort abhängig sind
- Auslöser: Innerhalb von 30 Tagen nach Expansions-/Kontraktionsentscheidung oder -ereignis

**Operative Änderungen:**

- Neue Dienstleistungsangebote → Vorschriften für diese Dienste überprüfen
- Eintritt in neuen Branchenvertikalmarkt → Sektorspezifische Vorschriften überprüfen
- Neue verarbeitete Datentypen → Datentypspezifische Vorschriften überprüfen
- Einstellung von Diensten → Prüfen, ob Vorschriften weiterhin anwendbar sind
- Auslöser: Während der Planungsphase (vor dem Start) und innerhalb von 30 Tagen nach operativer Änderung

**Organisatorische Umstrukturierung:**

- Fusion oder Übernahme → Umfassende Überprüfung der kombinierten Verpflichtungen der Einheit
- Veräusserung → Prüfen, ob Verpflichtungen nach der Veräusserung bestehen bleiben
- Änderung des Mutterunternehmens → Prüfen, ob neue Verpflichtungen weitergeleitet werden
- Auslöser: Im Rahmen der M&A-Due-Diligence; innerhalb von 60 Tagen nach Transaktionsabschluss

**Schwellenwertänderungen:**

- [Organisation] überschreitet regulatorischen Schwellenwert (z.B. Anzahl Mitarbeitende, Umsatz, Datenvolumen)
- Auslöser: Kontinuierliche Überwachung; formelle Überprüfung, wenn Schwellenwert überschritten

### Regulatorische Änderungen

**Vorschrift geändert:**

- Änderungen können Geltungsbereich, Anwendbarkeitskriterien oder Anforderungen ändern
- Auslöser: Prozess zur Überwachung regulatorischer Änderungen (POL-5.31.4, IMP-5.31.4) erkennt Änderung
- Massnahme: Auswirkungsbewertung umfasst Neubewertung der Anwendbarkeit, wenn Geltungsbereich geändert

**Neue Vorschrift verabschiedet:**

- Bereits durch Identifikationsprozess abgedeckt (Abschnitt 2)
- Auslöser: Mehrere Quellen (gemäss Abschnitt 2.2)

**Vorschrift aufgehoben oder ersetzt:**

- Vorschrift in POL-00 wird aufgehoben, widerrufen oder durch neuere Vorschrift ersetzt
- Auslöser: Überwachung regulatorischer Änderungen
- Massnahme: In POL-00 als „Ersetzt" kennzeichnen, Anwendbarkeitsbewertung für Ersatzvorschrift durchführen

**Regulatorische Leitlinien oder Auslegung erlassen:**

- Regulierungsbehörde erlässt Leitlinien zur Klärung des Geltungsbereichs oder der Anwendbarkeit
- Gerichtsentscheidung legt Vorschrift auf anwendbarkeitsrelevante Weise aus
- Auslöser: Regulatorische Überwachung oder Rechtsberater-Alert
- Massnahme: Anwendbarkeitsbestimmung im Lichte der neuen Auslegung überprüfen

### Vertragliche Änderungen

**Neuer Kundenvertrag:**

- Vertrag enthält Compliance-Anforderungen → Anwendbarkeitsbewertung für diese Anforderungen
- Auslöser: Vertragsabschluss oder während der Pre-Vertrags-Due-Diligence
- Massnahme: Vertraglich vorgeschriebene Vorschriften bewerten (kann Tier 1 sein, wenn durchsetzbar)

**Vertragsverlängerung oder -änderung:**

- Kunde fügt Compliance-Anforderungen bei Verlängerung hinzu
- Compliance-Verpflichtungen geändert
- Auslöser: Vertragsverlängerungsprozess
- Massnahme: Anwendbarkeit basierend auf aktualisierten Vertragsbedingungen überprüfen

**Vertragsablauf:**

- Grösserer Kundenvertrag läuft ohne Verlängerung aus
- Vertrag war einziger Auslöser für Anwendbarkeit (Kriterium V1)
- Auslöser: Vertragsablaufdatum
- Massnahme: Beurteilen, ob Vorschrift ohne Vertrag weiterhin anwendbar ist (kann von Tier 1 zu Tier 2 oder entfernt werden)

**Neue Lieferantenvereinbarung:**

- Vereinbarung schafft Durchleitungsverpflichtungen
- Auslöser: Lieferantenvertragsabschluss
- Massnahme: Anwendbarkeitsbewertung für weitergeleitete Anforderungen

### Zertifizierungsänderungen

**Neue Zertifizierung angestrebt:**

- [Organisation] entscheidet sich, neue Zertifizierung anzustreben (z.B. SOC 2, PCI DSS v4.0.1)
- Auslöser: Zertifizierungsentscheidung
- Massnahme: Zertifizierungsanforderungen auf anwendbare Vorschriften überprüfen

**Zertifizierungsstandard aktualisiert:**

- Standard mit neuen regulatorischen Referenzen überarbeitet
- Auslöser: Benachrichtigung durch Zertifizierungsstelle oder Normungsgremium
- Massnahme: Aktualisierten Standard auf neue Anwendbarkeit überprüfen

## Eskalation bei Anwendbarkeitsstreitigkeiten

Wenn die Anwendbarkeitsbestimmung bestritten wird (interne Meinungsverschiedenheit oder Herausforderung von externer Seite):

### Interne Streitigkeiten

**Typische Szenarien:**

- Geschäftsbereich behauptet, Vorschrift gilt nicht; Compliance behauptet, sie gilt
- Massnahmenverantwortlicher bestreitet Tier-Zuweisung (z.B. bittet um Tier 2 statt Tier 1 wegen Implementierungsaufwand)
- Recht und Compliance sind sich bei der Auslegung nicht einig

**Lösungsprozess:**
1. **Besprechung**: Streitende Parteien treffen sich, um Positionen und Nachweise zu verstehen
2. **Entscheidung des Compliance-Beauftragten**: Bei Streit auf operativer Ebene trifft Compliance-Beauftragter Bestimmung
3. **Rechtsberater-Überprüfung**: Bei Streitigkeiten zur rechtlichen Auslegung hat Rechtsberater das letzte Wort in Rechtsangelegenheiten
4. **Eskalation an Geschäftsleitung**: Bei Streitigkeiten mit Ressourcenverpflichtungen oder Risikoakzeptanz an Geschäftsleitung eskalieren
5. **Externer Berater**: Bei komplexen Rechtsfragen externen Berater für unabhängiges Gutachten einschalten

**Dokumentation**: Streit muss dokumentiert werden, einschliesslich Positionen, Nachweise, Lösungsprozess und endgültige Entscheidung mit Begründung

**Zeitplan**: Streitigkeiten sollten innerhalb von 30 Tagen nach Identifikation gelöst werden; Zwischenposition „Anwendbar" wird bis zur Lösung aufrechterhalten

### Externe Herausforderungen

**Szenarien:**

- Regulierungsbehörde behauptet, Vorschrift gilt für [Organisation]; [Organisation] glaubt, sie gilt nicht
- Kunde bestreitet Position von [Organisation] zur Anwendbarkeit
- Prüfer stellt Anwendbarkeitsbestimmung in Frage

**Reaktion:**
1. **Nachweise zusammenstellen**: Anwendbarkeitsbewertungsdokumentation und unterstützende Nachweise zusammentragen
2. **Rechtsberater-Überprüfung**: Rechtsberater einschalten, um Position und externe Behauptung zu überprüfen
3. **Externes Rechtsgutachten**: Einholen eines unabhängigen Rechtsgutachtens erwägen
4. **Direkte regulatorische Anfrage**: Mit Rechtsberater-Leitlinien direkte Anfrage an Regulierungsbehörde erwägen
5. **Lösung**: Basierend auf Analyse und Rechtsrat Bestimmung bestätigen oder revidieren
6. **Dokumentieren**: Externe Herausforderung und Lösung gründlich dokumentieren

**Zwischenposition**: Während der Streitlösung, sofern Rechtsberater nicht anderweitig rät, ursprüngliche Bestimmung aufrechterhalten oder konservativere Position einnehmen (als anwendbar behandeln), um Compliance-Risiko zu reduzieren.

## Überprüfungsdokumentation

Alle Überprüfungen (periodisch und ereignisgesteuert) werden dokumentiert:

**Überprüfungsnachweis:**

- Überprüfte Vorschrift
- Art der Überprüfung (Jährlich, Ereignisgesteuert, Streitlösung)
- Überprüfungsdatum
- Name des Prüfers
- Ergebnis (Keine Änderung, Tier geändert, Aus POL-00 entfernt, Zu POL-00 hinzugefügt)
- Begründung für das Ergebnis (wenn geändert)
- Genehmiger und Datum (wenn Bestimmung geändert)

**Überprüfungsprotokoll**: Zentralisiertes Überprüfungsprotokoll pflegen, das alle Überprüfungen erfasst. Unterstützt den Nachweis sorgfältiger laufender Verwaltung der regulatorischen Landschaft.

---

# Dokumentenkontrolle und verwandte Dokumente

## Dokumenteninformationen

| Attribut | Wert |
|----------|------|
| **Dokument-ID** | ISMS-POL-A.5.31.2 |
| **Dokumententitel** | Gesetzliche, gesetzlich vorgeschriebene, regulatorische und vertragliche Anforderungen: Methodik zur regulatorischen Anwendbarkeit |
| **Version** | 1.0 |
| **Status** | Entwurf |
| **Klassifizierung** | INTERN |
| **Eigentümer** | Compliance-Beauftragter |
| **Autor** | [Name] |
| **Inkrafttreten** | [Nach Genehmigung festzulegen] |
| **Überprüfungshäufigkeit** | Jährlich oder bei wesentlichen Änderungen der Methodik oder des Anwendbarkeitsrahmens |
| **Nächstes Überprüfungsdatum** | [12 Monate nach Inkrafttreten] |

## Genehmigung

Diese Richtlinie erfordert die Genehmigung durch folgende Rollen:

| Rolle | Name | Unterschrift | Datum |
|-------|------|-------------|-------|
| **Compliance-Beauftragter** | [Name] | ___________________ | __________ |
| **Rechtsberater** | [Name] | ___________________ | __________ |
| **ISMS-Manager** | [Name] | ___________________ | __________ |
| **Geschäftsleitung** | [Name] | ___________________ | __________ |

## Versionshistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [Datum] | [Name] | Erster Entwurf zur Überprüfung |
| 1.0 | [Datum] | [Name] | Erstgenehmigte Version |

## Verwandte Dokumente

**Vorausgehende Dokumente:**

- **ISMS-POL-A.5.31.1**: Zusammenfassung & Massnahmenausrichtung (Framework-Grundlage)

**Koordinierende Dokumente:**

- **ISMS-POL-00**: Regulatorischer Anwendbarkeitsrahmen (regulatorisches Register, gepflegt mit dieser Methodik)

**Nachgelagerte Dokumente:**

- **ISMS-POL-A.5.31.3**: Anforderungsextraktion & Massnahmenzuordnungsrahmen (nächste Phase nach Anwendbarkeitsbestimmung)
- **ISMS-POL-A.5.31.4**: Änderungsmanagement & Nachweisrahmen (laufendes Management einschliesslich Überwachung regulatorischer Änderungen)

**Implementierungsleitfäden:**

- **ISMS-IMP-A.5.31.2-UG/TG**: Prozess zur Bewertung der regulatorischen Anwendbarkeit (schrittweise Verfahren zur Ausführung dieser Methodik)

**Bewertungswerkzeuge:**

- **Bewertungsarbeitsbuch 1**: Regulatorisches Inventar (umfassende Liste der Vorschriften)
- **Bewertungsarbeitsbuch 2**: Anwendbarkeitsmatrix (strukturierte Bewertungsvorlage)

**Standards:**

- ISO/IEC 27001:2022 – Informationssicherheitsmanagementsysteme – Anforderungen (Massnahme A.5.31)
- ISO/IEC 27002:2022 – Massnahmen für die Informationssicherheit (Abschnitt 5.31)

## Verteilung und Zugang

**Verteilerliste:**

- Geschäftsführungsteam
- Compliance-Beauftragter / Rechtsfunktion
- ISMS-Manager
- Geschäftsentwicklung (für neue Verträge/Kunden)
- Operationsführung (für betriebliche Änderungen, die Überprüfungen auslösen)
- Internes Auditteam

**Zugangsstufe**: INTERN

**Dokumentenstandort**: Dokumentenverwaltungssystem von [Organisation]: [Pfad/URL]

---

# Definitionen

**Anwendbarkeit**: Bestimmung, dass eine Vorschrift für [Organisation] gilt, basierend auf geografischen, operativen oder vertraglichen Kriterien.

**Vertragliche Verpflichtung**: Durch Vertrag (Kunden-, Lieferanten-, Partnervertrag) aufgezwungene Anforderung, die eine durchsetzbare Compliance-Verpflichtung begründet.

**Geografischer Geltungsbereich**: Anwendbarkeit basierend auf dem Tätigkeitsort von [Organisation], dem Aufenthaltsort von Kunden oder extraterritorialen Bestimmungen.

**Rechtliche Verpflichtung**: Durch Gesetz oder Vorschrift auferlegte Anforderung, die rechtlich bindend und durchsetzbar ist.

**Operativer Geltungsbereich**: Anwendbarkeit basierend auf den Dienstleistungen von [Organisation], den verarbeiteten Daten oder den durchgeführten Betriebsaktivitäten.

**Vorschrift**: Allgemeiner Begriff, der Gesetze, Statuten, Verordnungen, Richtlinien, vertragliche Anforderungen und Standards umfasst (regulatorische Anforderungen).

**Drei-Tier-Framework**: Kategorisierungssystem, das Vorschriften als Tier 1 (Obligatorisch), Tier 2 (Bedingt) oder Tier 3 (Informativ) klassifiziert.

**Auslöseereignis**: Umstand, der die Identifikation von Vorschriften oder die Neubewertung der Anwendbarkeit initiiert.

---

**ENDE DES DOKUMENTS**

---

*Diese Richtlinie legt die systematische Methodik von [Organisation] zur Bestimmung der regulatorischen Anwendbarkeit fest, die in ISMS-POL-00 einfliesst und die nachgelagerte Anforderungsextraktion und Massnahmenzuordnung ermöglicht.*

<!-- QA_VERIFIED: 2026-03-28 -->
