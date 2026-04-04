<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.3-DE:framework:POL:a.5.31.3 -->
**ISMS-POL-A.5.31.3 — Anforderungsextraktion & Massnahmenzuordnungsrahmen**
**Gesetzliche, regulatorische und vertragliche Anforderungen**

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Anforderungsextraktion & Massnahmenzuordnungsrahmen |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.31.3 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | INTERN |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|-----------|
| 1.0 | [Datum] | ISB/ISO | Erstes Richtlinien-Framework für die ISO 27001:2022-Erstzertifizierung |

---

# Einleitung & Beziehung zu 5.31.1/5.31.2

## Zweck dieses Richtlinienabschnitts

Dieser Richtlinienabschnitt legt den systematischen Rahmen von [Organisation] für die Umsetzung regulatorischer Verpflichtungen in umsetzbare Sicherheitsmassnahmen mit vollständiger Rückverfolgbarkeit fest. Er definiert die Prozesse, durch die gesetzliche und regulatorische Texte in implementierbare Anforderungen umgewandelt, ISO 27001-Massnahmen zugeordnet und bis zum Nachweis nachverfolgt werden.

**Dies ist die "Übersetzungsschicht"** des regulatorischen Compliance-Frameworks — das entscheidende Bindeglied zwischen der Identifizierung anwendbarer Vorschriften und dem Nachweis der Compliance durch implementierte Massnahmen.

## Progression: Anwendbarkeit → Anforderungen → Massnahmen

Das regulatorische Compliance-Framework folgt einer logischen Abfolge:

**ISMS-POL-A.5.31.1** legte die übergeordnete Framework-Architektur, das Governance-Modell und die Integration mit ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen) fest. Es definierte das "Warum" und die strukturelle Grundlage.

**ISMS-POL-A.5.31.2** definierte die systematische Methodik zur Bestimmung, WELCHE Vorschriften auf [Organisation] anwendbar sind, basierend auf geografischen, operativen und vertraglichen Kriterien. Es beantwortet die Frage: "Welche Gesetze regeln uns?"

**ISMS-POL-A.5.31.3** (dieses Dokument) definiert die systematische Methodik zur Bestimmung, WAS diese anwendbaren Vorschriften verlangen und WIE [Organisation] diese durch ISO 27001-Massnahmen erfüllt. Es beantwortet die Fragen:

- "Welche spezifischen Verpflichtungen ergeben sich aus diesen Vorschriften?"
- "Welche Sicherheitsmassnahmen erfüllen diese Verpflichtungen?"
- "Wo bestehen Lücken in unserer aktuellen Massnahmenimplementierung?"
- "Wie weisen wir die Compliance durch Nachweise nach?"

**ISMS-POL-A.5.31.4** (nachfolgend) wird definieren, wie [Organisation] regulatorische Änderungen überwacht, Framework-Aktualisierungen verwaltet und auditbereite Nachweise aufrechterhält.

## Die Übersetzungsherausforderung

Vorschriften werden in juristischer Sprache von Gesetzgebern und Regulatoren verfasst. Sicherheitsmassnahmen werden in technischer und organisatorischer Sprache von Sicherheitsfachleuten formuliert. Diese beiden Bereiche sprechen verschiedene Sprachen:

**Juristische Sprache**:

- "Der Verantwortliche trifft geeignete technische und organisatorische Massnahmen, um ein dem Risiko angemessenes Schutzniveau zu gewährleisten..."
- Für rechtliche Compliance und Durchsetzung verfasst
- Häufig prinzipienbasiert statt vorschreibend
- Kann technische Konzepte ohne spezifische Implementierungshinweise referenzieren

**Sicherheitsmassnahmen-Sprache**:

- "A.5.15 Zugangskontrolle: Informationen und andere zugehörige Vermögenswerte sollten nur für autorisierte Benutzer zugänglich sein."
- Für Sicherheitspraktiker verfasst
- Auf das WAS der Implementierung fokussiert, nicht auf rechtliche Compliance
- Spezifisch genug, um die Implementierung zu leiten

**Die Übersetzungsherausforderung**: Wie können wir systematisch und reproduzierbar spezifische, umsetzbare Anforderungen aus regulatorischen Texten extrahieren und bestehenden Sicherheitsmassnahmen zuordnen?

Die in diesem Dokument definierte Methodik löst diese Herausforderung durch:
1. **Systematische Anforderungsextraktion** — Parsing regulatorischer Texte in diskrete, umsetzbare Anforderungen
2. **Anforderungskategorisierung** — Gliederung der Anforderungen nach Art (technisch, organisatorisch, berichterstattend, operativ)
3. **Massnahmenzuordnung** — Identifizierung, welche ISO 27001 Annex A-Massnahmen jede Anforderung erfüllen
4. **Lückenanalyse** — Identifizierung von Anforderungen ohne entsprechende Massnahmen
5. **Rückverfolgbarkeit** — Aufrechterhaltung eines vollständigen Prüfpfads von der Vorschrift über die Anforderung zur Massnahme bis zum Nachweis

## Geltungsbereich des Dokuments

Dieser Richtlinienabschnitt gilt für:

- **Alle Vorschriften**, die in ISMS-POL-00 als anwendbar eingestuft sind (Tier 1 obligatorisch und Tier 2 bedingt anwendbare Vorschriften)
- **Alle ISO 27001:2022 Annex A-Massnahmen** (93 Massnahmen in den Bereichen Organisation, Menschen, Physisch und Technologie)
- **Organisationsspezifische Massnahmen**, die erstellt werden, wenn keine Annex A-Massnahme eine Anforderung erfüllt
- **Alle Mitarbeitenden**, die an regulatorischer Compliance, Massnahmenimplementierung und Nachweismanagement beteiligt sind

Dieses Dokument enthält KEINE:

- Rechtlichen Interpretationen spezifischer Vorschriften (dafür ist Rechtsberatung erforderlich)
- Festlegung, welche Vorschriften auf [Organisation] anwendbar sind (geregelt in 5.31.2)
- Operative Verfahren für Extraktion und Zuordnung (geregelt in IMP-5.31.2 und IMP-5.31.3)
- Definition von Nachweismanagementprozessen (geregelt in 5.31.4)

---

# Anforderungsextraktionsprozess

## Methodik der Anforderungsextraktion

Die Anforderungsextraktion ist der systematische Prozess des Parsings regulatorischer Texte zur Identifizierung spezifischer, verbindlicher Verpflichtungen, die [Organisation] erfüllen muss. Dieser Prozess transformiert ausführliche, prinzipienbasierte Rechtstexte in diskrete, umsetzbare Anforderungen, die für die Massnahmenzuordnung geeignet sind.

### Systematisches Lesen regulatorischer Texte

Vorschriften haben eine Struktur, die je nach Jurisdiktion und Typ variiert:

- **Gesetze und Erlasse**: Typischerweise in Kapitel, Abschnitte, Unterabschnitte, Absätze unterteilt
- **Verordnungen und Richtlinien**: In Artikel, Abschnitte, Anhänge, Zeitpläne unterteilt
- **Standards**: In Klauseln, Unterklauseln, Anforderungen, Empfehlungen unterteilt
- **Verträge**: In Abschnitte, Klauseln, Anlagen, Service Level Agreements unterteilt

Jedes Strukturelement kann enthalten:

- **Definitionen** — Bedeutung von Begriffen festlegen (für Glossar extrahieren, nicht als Anforderungen)
- **Grundsätze** — Übergeordnete Ziele (können Anforderungen erzeugen, wenn sie verbindlich gemacht werden)
- **Verpflichtungen** — Spezifische Dinge, die [Organisation] tun MUSS (DIESE sind Anforderungen)
- **Verbote** — Dinge, die [Organisation] NICHT tun darf (negativ formulierte Anforderungen)
- **Verfahren** — Wie Verpflichtungen einzuhalten sind (können operative Anforderungen erzeugen)
- **Berichtspflichten** — Was wann einzureichen ist
- **Strafen** — Konsequenzen bei Nichteinhaltung (informieren Priorisierung, werden nicht als Anforderungen extrahiert)

**Systematischer Leseprozess**:

1. **Gesamte Vorschrift überprüfen**, um Gesamtabsicht und Geltungsbereich zu verstehen
2. **Strukturelle Grenzen identifizieren** (wo eine Anforderung endet, beginnt die nächste)
3. **Jeden Abschnitt/Artikel** auf diskrete Verpflichtungen analysieren
4. **Unterscheiden** zwischen verbindlichen Verpflichtungen, Empfehlungen und Kontextinformationen
5. **Jede verbindliche Verpflichtung** als separate Anforderung extrahieren
6. **Interdependenzen notieren**, wo Anforderungen andere referenzieren oder von ihnen abhängen

**Häufige Fehler**:

- **Überaggregation**: Gesamten Artikel als einzelne Anforderung extrahieren, obwohl er mehrere unterschiedliche Verpflichtungen enthält
- **Unterextraktion**: Anforderungen übersehen, die in Definitions- oder Verfahrenstexten eingebettet sind
- **Interpretationskreisel**: Verpflichtungen hinzufügen, die nicht explizit in der Vorschrift angegeben sind
- **Kontext ignorieren**: Anforderungen extrahieren ohne Verständnis ihres übergeordneten regulatorischen Zwecks

### Identifizierung verbindlicher vs. empfehlender Sprache

Vorschriften verwenden spezifische Sprache, um das Verpflichtungsniveau anzuzeigen. [Organisation] extrahiert VERBINDLICHE Anforderungen für die Compliance und notiert empfehlende Sprache für Kontext und Best-Practice-Orientierung.

**Verbindliche Sprache** (MUSS extrahiert werden):

- **"shall"** — primärer Indikator für eine rechtliche Verpflichtung
- **"must"** — gleichwertig zu "shall", verbindliche Anforderung
- **"is required to"** — explizite Anforderung
- **"will"** — wenn präskriptiv verwendet (z.B. "die Organisation wird implementieren...")
- **"has a duty to"** — begründet Verpflichtung
- **"is obligated to"** — explizite Verpflichtung

**Empfehlende Sprache** (KANN als optional/Best Practice extrahiert werden):

- **"should"** — Empfehlung, nicht verbindlich
- **"is encouraged to"** — freiwillige Massnahme
- **"may"** — erlaubend, optional
- **"can"** — Möglichkeit, keine Anforderung
- **"it is recommended"** — Best-Practice-Orientierung

**Bedingte Sprache** (mit Bedingungen extrahieren):

- **"shall, where applicable"** — verbindlich wenn Bedingung erfüllt
- **"must, if [Bedingung]"** — verbindlich wenn spezifischer Umstand besteht
- **"is required to, in cases where..."** — bedingte Verpflichtung

**Kontext ist entscheidend**: Sprache allein ist nicht ausreichend. Rechtsberatung sollte Extraktionen überprüfen, um zu bestätigen, ob scheinbar empfehlende Sprache im spezifischen regulatorischen Kontext durchsetzbare Verpflichtungen schafft.

**Beispiele für Extraktionsentscheidungen**:

| Regulatorischer Text | Verbindlich? | Extraktionsentscheidung |
|---------------------|-------------|------------------------|
| "Organisations shall implement encryption for data at rest" | Ja (shall) | Extrahieren: "Verschlüsselung für ruhende Daten implementieren" |
| "Organisations should consider multi-factor authentication" | Nein (should) | Als Best Practice notieren, nicht als Anforderung extrahieren |
| "Organisations must conduct annual risk assessments" | Ja (must) | Extrahieren: "Risikobeurteilungen jährlich durchführen" |
| "Organisations may use industry-standard frameworks" | Nein (may) | Als Option notieren, nicht als Anforderung extrahieren |
| "Where personal data is processed, organisations shall obtain consent" | Bedingt (shall, where...) | Extrahieren: "Einwilligung einholen bei Verarbeitung personenbezogener Daten" |

### Granularitätsleitlinien

Anforderungen müssen auf dem richtigen Detaillierungsgrad extrahiert werden — spezifisch genug, um umsetzbar zu sein, aber nicht so vorschreibend, dass Implementierungsflexibilität eliminiert wird.

**Zu grob** (Nicht umsetzbar):

- ❌ "Artikel 32 einhalten"
  - Problem: Keine Orientierung darüber, WAS zu tun ist
  - Kann keinen spezifischen Massnahmen zugeordnet werden
  - Nicht implementierbar

- ❌ "Geeignete Sicherheitsmassnahmen implementieren"
  - Problem: "Geeignet" ist undefiniert
  - Zu vage, um Compliance zu verifizieren
  - Lässt Implementierende im Unklaren

**Zu fein** (Überpräskriptiv):

- ❌ "AES-256-GCM-Verschlüsselung mit PBKDF2-Schlüsselableitung unter Verwendung von 10.000 Iterationen und SHA-256-Hashing für alle ruhenden Daten verwenden"
  - Problem: Eliminiert Flexibilität bei der Implementierung
  - Technologie entwickelt sich; überspezifische Anforderungen werden obsolet
  - Kann mit anderen Vorschriften in Konflikt geraten, die gleichwertige Massnahmen erlauben

- ❌ "Penetrationstest am zweiten Dienstag im März jeden Jahres durchführen"
  - Problem: Unnötig spezifischer Zeitpunkt
  - Vorschrift verlangt wahrscheinlich nur "jährliche" Tests
  - Schafft starre Prozesse, die möglicherweise nicht auf Geschäftsbedürfnisse abgestimmt sind

**Genau richtig** (Umsetzbar mit Flexibilität):

- ✅ "Verschlüsselung für ruhende Daten unter Verwendung branchenüblicher Algorithmen und Schlüssellängen implementieren, die der Sensitivität der Daten angemessen sind"
  - Umsetzbar: Klares WAS (ruhende Daten verschlüsseln)
  - Flexibel: Implementierungswahl des Algorithmus (AES-256, ChaCha20 usw.)
  - Orientierung: "Branchenüblich" und "angemessen zur Sensitivität" geben Grenzen vor
  - Zuordnungsfähig: Kann ISO 27001-Massnahmen zur Verschlüsselung zugeordnet werden

- ✅ "Schwachstellenbeurteilungen aller internetzugewandten Systeme mindestens vierteljährlich durchführen"
  - Umsetzbar: Klares WAS (Schwachstellenbeurteilungen), WELCHE (internetzugewandt), WANN (vierteljährlich mindestens)
  - Flexibel: Wahl der Scanning-Tools, Methodikdetails
  - Verifizierbar: Kann demonstrieren, dass vierteljährliche Scans stattgefunden haben
  - Zuordnungsfähig: Kann ISO 27001-Massnahmen zum Schwachstellenmanagement zugeordnet werden

**Granularitätsentscheidungsrahmen**:

Stellen Sie sich diese Fragen bei der Bestimmung der Extraktionsgranularität:
1. **Kann jemand dies ohne Raten implementieren?** (Falls nein → zu grob)
2. **Lässt dies vernünftige Implementierungsentscheidungen zu?** (Falls nein → zu fein)
3. **Können wir dies einer oder mehreren Massnahmen zuordnen?** (Falls nein → Granularität anpassen)
4. **Können wir Nachweise erheben, um Compliance zu belegen?** (Falls nein → zu vage)
5. **Bleibt diese Anforderung gültig, wenn sich die Technologie weiterentwickelt?** (Falls nein → zu präskriptiv)

**Allgemeines Prinzip**: Anforderungen auf dem Niveau extrahieren, auf dem die Vorschrift TATSÄCHLICH Spezifizität vorschreibt. Wenn die Vorschrift "Verschlüsselung" sagt, nicht "AES-256" hinzufügen. Wenn die Vorschrift "AES-256" sagt, nicht auf "Verschlüsselung" verallgemeinern.

## Anforderungskategorisierung

Nach der Extraktion werden Anforderungen nach ihrer Art kategorisiert, um die Massnahmenzuordnung und Implementierungszuweisung zu erleichtern. Jede Anforderung kann in eine oder mehrere Kategorien fallen.

### Technische Anforderungen

Anforderungen, die spezifische technische Sicherheitsmassnahmen, Systemkonfigurationen oder Technologieimplementierungen vorschreiben.

**Merkmale**:

- Erfordern technische Implementierung (Code, Konfiguration, Systeme)
- Werden häufig von IT-, Sicherheitstechnik- und Entwicklungsteams implementiert
- Können technisch verifiziert werden (Scans, Audits, Tests)

**Beispiele** (generisch):

- "Netzwerksegmentierung implementieren, um sensible Systeme zu isolieren"
- "Anti-Malware-Schutz auf allen Endpunkten einsetzen"
- "Verschlüsselung für Daten bei der Übertragung mit TLS 1.2 oder höher aktivieren"
- "Systeme konfigurieren, um Passwortkomplexitätsanforderungen durchzusetzen"
- "Automatisierte Protokollerfassung und zentralisierte Speicherung implementieren"

**Typische Massnahmenzuordnungen**: Technische Anforderungen werden typischerweise ISO 27001-Massnahmen in folgenden Bereichen zugeordnet:

- **Bereich 8 (Technologische Massnahmen)**: A.8.1 bis A.8.34
- Einige organisatorische Massnahmen mit technischen Elementen (z.B. A.5.15 Zugangskontrolle)

### Organisatorische Anforderungen

Anforderungen, die Richtlinien, Verfahren, Governance-Strukturen, Rollen, Schulungen oder organisatorische Prozesse vorschreiben.

**Merkmale**:

- Erfordern Richtlinien-/Verfahrensdokumentation
- Werden häufig von Rechts-, Compliance-, Personal- und Management-Teams implementiert
- Werden durch Dokumentenüberprüfung und Interviews verifiziert

**Beispiele** (generisch):

- "Informationssicherheitsrichtlinie erstellen und aufrechterhalten, die von der Geschäftsleitung genehmigt wird"
- "Rollen und Verantwortlichkeiten für den Datenschutz definieren"
- "Hintergrundüberprüfungen für Personal mit Zugang zu sensiblen Informationen durchführen"
- "Sicherheitsbewusstseinstraining für alle Mitarbeitenden jährlich anbieten"
- "Verfahren zur Vorfallbehandlung einschliesslich Eskalationspfaden einrichten"

**Typische Massnahmenzuordnungen**: Organisatorische Anforderungen werden typischerweise ISO 27001-Massnahmen in folgenden Bereichen zugeordnet:

- **Bereich 5 (Organisatorische Massnahmen)**: A.5.1 bis A.5.37
- **Bereich 6 (Personalbezogene Massnahmen)**: A.6.1 bis A.6.8

### Berichtspflichten

Anforderungen, die Einreichungen, Meldungen, Offenlegungen oder Berichte an Aufsichtsbehörden, betroffene Personen oder andere externe Parteien vorschreiben.

**Merkmale**:

- Zeitkritisch (spezifische Fristen)
- Nach aussen gerichtet (an Behörden oder Dritte übermittelt)
- Haben oft vorgeschriebene Formate oder Vorlagen
- Nichteinhaltung ist für Regulatoren direkt sichtbar

**Beispiele** (generisch):

- "Aufsichtsbehörde über Verletzungen des Schutzes personenbezogener Daten innerhalb von 72 Stunden nach Kenntnisnahme benachrichtigen"
- "Jährliche Compliance-Bestätigung bis 31. März bei der Regulierungsbehörde einreichen"
- "Betroffene Personen über Sicherheitsvorfälle, die ihre persönlichen Informationen betreffen, ohne unangemessene Verzögerung benachrichtigen"
- "Öffentliches Register der Datenverarbeitungsaktivitäten auf der Website zugänglich machen"
- "Wesentliche Cybersicherheitsereignisse innerhalb von 24 Stunden an den Sektorregulierer melden"

**Typische Massnahmenzuordnungen**: Berichtspflichten werden häufig zugeordnet:

- Vorfallmanagement-Massnahmen (A.5.24 bis A.5.28)
- Compliance-Überwachungsmassnahmen (A.5.31, A.5.36)
- Erfordern häufig EIGENE Prozesse über Annex A hinaus

**Besondere Überlegungen**:

- Berichtspflichten haben oft die strengsten Fristen
- Versäumnis zu melden ist typischerweise ein separater Verstoss
- Erfordern robuste Prozesse und klare Verantwortungszuweisung

### Operative Anforderungen

Anforderungen, die spezifische operative Verfahren, Business-Continuity-Massnahmen, Tests, Überwachung oder laufende operative Aktivitäten vorschreiben.

**Merkmale**:

- Erfordern laufende Ausführung (keine einmalige Implementierung)
- Oft zyklisch (tägliche, monatliche, jährliche Aktivitäten)
- Werden von Operations-, IT- und Security Operations-Teams implementiert
- Werden durch Aktivitätsprotokolle und Nachweise der Ausführung verifiziert

**Beispiele** (generisch):

- "Business-Continuity-Pläne jährlich mit dokumentierten Ergebnissen testen"
- "Sicherheitsereignisprotokolle kontinuierlich auf Kompromittierungsindikatoren überwachen"
- "Tabletop-Übungen für Vorfallbehandlungsverfahren halbjährlich durchführen"
- "Risikobeurteilungen vierteljährlich überprüfen und aktualisieren"
- "Schwachstellenscans von Produktionssystemen monatlich durchführen"

**Typische Massnahmenzuordnungen**: Operative Anforderungen werden typischerweise zugeordnet:

- Test- und Überwachungsmassnahmen (A.8.7 Schutz vor Schadsoftware, A.8.15 Protokollierung, A.8.16 Überwachungsaktivitäten)
- Business-Continuity-Massnahmen (A.5.29 Informationssicherheit bei Störungen, A.5.30 IKT-Bereitschaft für BC)
- Compliance- und Auditmassnahmen (A.5.36 Einhaltung von Richtlinien, A.5.37 Dokumentierte Betriebsverfahren)

### Zweck der Kategorisierung

Die Kategorisierung dient mehreren Zwecken:

**Effizienz der Massnahmenzuordnung**:

- Technische Anforderungen → zuerst Fokus auf Bereich 8-Massnahmen
- Organisatorische Anforderungen → zuerst Fokus auf Bereiche 5 & 6-Massnahmen
- Spart Zeit durch Eingrenzung des Suchraums

**Implementierungszuweisung**:

- Technische Anforderungen → IT/Sicherheitstechnik-Teams
- Organisatorische Anforderungen → Compliance/Rechts/Personal-Teams
- Berichtspflichten → Compliance/Kommunikations-Teams
- Operative Anforderungen → Operations/SOC-Teams

**Nachweisplanung**:

- Technische Anforderungen → Konfigurationsaudits, Scan-Ergebnisse, Systemprotokolle
- Organisatorische Anforderungen → Richtliniendokumente, Schulungsunterlagen, Besprechungsprotokolle
- Berichtspflichten → Einreichungsbestätigungen, Benachrichtigungsprotokolle
- Operative Anforderungen → Aktivitätsprotokolle, Testergebnisse, Überwachungs-Dashboards

**Lückenanalyse**:

- Kategorien helfen zu identifizieren, WO Lücken bestehen (technische Lücken vs. Prozesslücken)
- Informiert den Behebungsansatz (technische Lösung vs. Richtlinienerstellung)

**Hinweis**: Anforderungen können mehrere Kategorien umfassen. Beispiel: "Multi-Faktor-Authentifizierung für alle privilegierten Konten implementieren und aufrechterhalten" ist sowohl technisch (MFA-Implementierung) als auch organisatorisch (Richtlinie, die MFA fordert).

## Struktur des Anforderungsregisters

Das Anforderungsregister ist das massgebliche, zentralisierte Repository aller extrahierten Anforderungen aus anwendbaren Vorschriften. Es bildet die strukturierte Grundlage für Massnahmenzuordnung, Lückenanalyse und Compliance-Berichterstattung.

### Registerfelder

Jeder Anforderungseintrag im Register MUSS die folgenden Felder enthalten:

**Anforderungs-ID** (Eindeutiger Bezeichner)

- **Format**: REG-[VorschriftCode]-[Artikel/Abschnitt]-[Sequenz]
- **Zweck**: Eindeutiger, stabiler Bezeichner für jede Anforderung, der auch bei Aktualisierung des Anforderungstexts konstant bleibt
- **Beispiele**:
  - REG-DP01-32-001 (erste Anforderung aus Datenschutzvorschrift Artikel 32)
  - REG-DP01-32-002 (zweite Anforderung aus demselben Artikel)
  - REG-SEC15-4.2-001 (erste Anforderung aus Sicherheitsstandard Abschnitt 4.2)
- **VorschriftCode**: Kurzcode aus dem ISMS-POL-00-Regulierungsregister

**Vorschrift-ID** (Verknüpfung mit ISMS-POL-00)

- **Zweck**: Verknüpft Anforderung mit übergeordneter Vorschrift im Regulierungsregister
- **Inhalt**: Derselbe VorschriftCode wie in der Anforderungs-ID
- **Verwendung**: Ermöglicht Filterung/Berichterstattung nach Vorschrift, ermöglicht kaskadierende Aktualisierungen bei Vorschriftsänderungen

**Vorschriftname** (Vollständiger Vorschriftname)

- **Zweck**: Menschenlesbare Identifizierung der Quellvorschrift
- **Inhalt**: Vollständiger offizieller Name der Vorschrift
- **Beispiele**:
  - "Datenschutzgesetz 2025"
  - "Cybersicherheitsverordnung (EU) 2024/1234"
  - "Payment Card Industry Data Security Standard v4.0"

**Quellenangabe** (Spezifischer Quellenort)

- **Zweck**: Präziser Verweis auf die STELLE in der Vorschrift, an der diese Anforderung erscheint
- **Inhalt**: Artikel, Abschnitt, Unterabschnitt, Absatz, Klausel nach Bedarf
- **Beispiele**:
  - "Artikel 32, Absatz 1(a)"
  - "Abschnitt 4.2.1"
  - "Anforderung 8.3.2"
  - "Anhang A, Klausel 12"
- **Bedeutung**: Ermöglicht rechtliche Überprüfung, Verifizierung und Zitierung in Compliance-Dokumentation

**Ursprünglicher Anforderungstext** (Wörtliches Zitat)

- **Zweck**: Genaue regulatorische Sprache wie in der Quellvorschrift formuliert
- **Inhalt**: Direktes Zitat, keine Paraphrasierung
- **Bedeutung**: Rechtliche Genauigkeit, ermöglicht Verifizierung, dass die Interpretation dem Original treu ist

**Interpretierte Anforderung** (Umsetzbare Übersetzung)

- **Zweck**: Anforderung in klarer, umsetzbarer Sprache für die Implementierung umformuliert
- **Inhalt**: Was [Organisation] tun MUSS, um zu entsprechen, in angemessener Granularität verfasst
- **Orientierung**: Sollte von Implementierenden ohne juristischen Hintergrund verstanden werden können

**Anforderungskategorie** (Klassifizierung)

- **Zweck**: Art der Anforderung gemäss Abschnitt 2.2
- **Inhalt**: Eine oder mehrere aus: Technisch / Organisatorisch / Berichterstattend / Operativ
- **Format**: Kann Mehrfachauswahl sein (z.B. "Technisch, Organisatorisch" für Anforderungen, die beide umfassen)

**Priorität** (Implementierungsdringlichkeit)

- **Zweck**: Relative Bedeutung für Implementierung und Lückenbehebung
- **Werte**:
  - **Hoch**: Erhebliche rechtliche Konsequenz bei Nichteinhaltung, oder Compliance-Frist steht unmittelbar bevor, oder Tier-1-Vorschrift
  - **Mittel**: Moderate rechtliche Konsequenz, oder angemessener Zeitplan für Compliance
  - **Niedrig**: Geringe Konsequenz oder angestrebte Anforderung
- **Grundlage**: Informiert durch Rechtsberatung, regulatorischen Tier (Tier 1 vs. Tier 2), Durchsetzungshistorie

**Implementierungsfrist** (Compliance-Datum)

- **Zweck**: Wann diese Anforderung implementiert/compliant sein muss
- **Inhalt**: Spezifisches Datum, falls von der Vorschrift angegeben, sonst organisatorisches Zieldatum
- **Verwendung**: Treibt Implementierungsplanung und Zeitplanung der Lückenbehebung

**Implementierungsstatus** (Aktueller Stand)

- **Zweck**: Implementierungsfortschritt verfolgen
- **Werte**:
  - **Nicht begonnen**: Noch keine Implementierungsaktivität
  - **In Bearbeitung**: Implementierung läuft, noch nicht abgeschlossen
  - **Implementiert**: Vollständig implementiert und in Betrieb
  - **Verifiziert**: Implementiert und Compliance verifiziert (Nachweise vorhanden)
  - **N/A**: Anforderung gilt nicht für [Organisation] basierend auf Geltungsbereich/Kontext
- **Aktualisiert durch**: Massnahmenverantwortlicher für die Implementierung

**Verantwortliche Partei** (Eigentümer)

- **Zweck**: Wer für die Implementierung dieser Anforderung verantwortlich ist
- **Inhalt**: Rolle oder benannte Person
- **Beispiele**:
  - "Informationssicherheitsbeauftragter"
  - "IT-Sicherheitsmanager"
  - "Datenschutzbeauftragter"
  - "Massnahmenverantwortlicher A.8.24"

**Zugeordnete Massnahmen** (ISO 27001-Massnahmen)

- **Zweck**: Welche Massnahmen diese Anforderung erfüllen
- **Inhalt**: Liste der Massnahmen-IDs mit Zuordnungstyp
- **Format**: "A.5.15 (P), A.5.16 (S), A.8.2 (Su)"
  - P = Primär, S = Sekundär, Su = Unterstützend
- **Verwendung**: Verknüpft Anforderungen mit Massnahmen, ermöglicht Lückenidentifizierung

**Lückenstatus** (Compliance-Lücke)

- **Zweck**: Ob die Anforderung durch bestehende Massnahmen vollständig erfüllt wird
- **Werte**:
  - **Keine Lücke**: Anforderung vollständig durch zugeordnete Massnahmen erfüllt
  - **Teilweise Lücke**: Zugeordnete Massnahmen bieten teilweise Erfüllung, Verbesserungen erforderlich
  - **Vollständige Lücke**: Keine Massnahmen erfüllen diese Anforderung, neue Massnahme(n) erforderlich
- **Treibt**: Lückenbehebungsaktivitäten (Abschnitt 4)

**Anmerkungen** (Zusätzlicher Kontext)

- **Zweck**: Wichtigen Kontext, rechtliche Nuancen, Implementierungsüberlegungen erfassen
- **Inhalt**: Freitextfeld für Interpretationsnotizen des Rechtsberaters, Abhängigkeiten, Implementierungsherausforderungen

**Extrahiert durch / Datum** (Rückverfolgbarkeit)

- **Zweck**: Wer die Extraktion durchgeführt hat und wann
- **Beispiel**: "Compliance-Analyst / 2025-01-15"

**Überprüft durch / Datum** (Qualitätskontrolle)

- **Zweck**: Wer die Extraktion auf Genauigkeit überprüft hat und wann
- **Beispiel**: "Rechtsberater / 2025-01-20"

**Zuletzt aktualisiert / Aktualisiert durch** (Änderungsverfolgung)

- **Zweck**: Wann der Anforderungseintrag zuletzt geändert wurde und von wem
- **Verwendung**: Prüfpfad, Versionskontrolle, identifiziert veraltete Einträge

### Registerpflege

**Zentralisiertes Repository**:
Das Anforderungsregister SOLLTE in einem strukturierten, durchsuchbaren Format gepflegt werden:

- **Bevorzugt**: Datenbank (ermöglicht komplexe Abfragen, Berichterstattung, Rückverfolgbarkeit)
- **Akzeptabel**: Strukturierte Tabellenkalkulation (Excel/LibreOffice mit Datenvalidierung)
- **Ort**: Zentralisierter Ort für alle Stakeholder mit entsprechenden Zugriffsrechten
- **Werkzeug**: Bewertungsarbeitsmappe 3 bietet standardisierte Vorlage

**Zugangskontrolle**:

- **Lesezugang**: Alle ISMS-Stakeholder, Massnahmenverantwortliche, Auditoren
- **Schreibzugang (Hinzufügen/Bearbeiten)**: Compliance-Beauftragter, Rechtsberater, designierte Anforderungsanalysten
- **Genehmigungsbefugnis**: ISMS-Manager, Rechtsberater (für neue Anforderungen oder Änderungen am Feld "Interpretierte Anforderung")

**Versionskontrolle**:

- **Registerversion**: Gesamtes Register versioniert (z.B. v1.0, v1.1, v2.0)
- **Anforderungsebenenverfolgung**: Jede Anforderung verfolgt ihre eigene Änderungshistorie
- **Änderungsprotokoll**: Separates Protokoll erfasst was, wann, warum geändert wurde
- **Archivierung**: Frühere Registerversionen für mindestens [X Jahre gemäss Aufbewahrungsrichtlinie] aufbewahrt

**Prüfpfad**:
Alle Änderungen am Register MÜSSEN protokolliert werden:

- Datum/Uhrzeit der Änderung
- Benutzer, der die Änderung vorgenommen hat
- Geändertes(e) Feld(er)
- Alter Wert → Neuer Wert
- Änderungsgrund

**Qualitätskontrollprozess**:
1. **Extraktion**: Anforderungsanalyst extrahiert Anforderungen gemäss Abschnitt 2.1
2. **Rechtliche Überprüfung**: Rechtsberater prüft Übersetzung Original → Interpretierte Anforderung auf Genauigkeit
3. **Genehmigung**: ISMS-Manager oder Compliance-Beauftragter genehmigt Hinzufügung zum Register
4. **Veröffentlichung**: Anforderung mit ausgefülltem Feld "Überprüft durch" zum Register hinzugefügt
5. **Periodische Überprüfung**: Alle Anforderungen jährlich oder bei Änderung der Quellvorschrift überprüft

**Wartungsauslöser**:
Das Anforderungsregister MUSS aktualisiert werden, wenn:

- Neue Vorschrift als anwendbar identifiziert wird (aus 5.31.2-Prozess)
- Bestehende Vorschrift geändert wird (aus 5.31.4-Regulierungsmonitoring)
- Vorschrift aufgehoben wird oder ausläuft (Anforderungen archiviert)
- Organisatorischer Geltungsbereich sich ändert (neue Anforderungen werden anwendbar)
- Implementierungsstatus sich ändert
- Lückenbehebung abgeschlossen wurde
- Massnahmenzuordnungen sich ändern

## Extraktionsprinzipien

Diese Prinzipien regeln den Anforderungsextraktionsprozess, um Konsistenz, Genauigkeit und rechtliche Verteidigungsfähigkeit sicherzustellen.

**Prinzip 1: Vollständigkeit**

- ALLE verbindlichen Anforderungen aus anwendbaren Vorschriften extrahieren
- Anforderungen nicht basierend auf Implementierungsleichtigkeit selektiv auswählen
- Wenn eine Anforderung in der Vorschrift vorhanden ist, muss sie im Register vorhanden sein
- Begründung: Regulierungsauditoren werden die gesamte Vorschrift überprüfen; Extraktionslücken sind Compliance-Versäumnisse

**Prinzip 2: Genauigkeit**

- Interpretierte Anforderung muss dem ursprünglichen Anforderungstext treu sein
- Keine Verpflichtungen hinzufügen, die nicht in der regulatorischen Sprache vorhanden sind
- Verpflichtungen nicht durch Interpretation abschwächen
- Geltungsbereich oder Anwendbarkeit nicht durch Paraphrasierung ändern
- Begründung: Rechtliche Verteidigungsfähigkeit erfordert wahrheitsgetreue Darstellung der regulatorischen Absicht

**Prinzip 3: Klarheit**

- Interpretierte Anforderungen in klarer, fachfreier Sprache formulieren
- Zielgruppe: Technische Implementierer und Massnahmenverantwortliche, nicht Juristen
- Mehrdeutige Begriffe ohne Kontext ("angemessen", "geeignet") vermeiden
- Anforderungen umsetzbar machen (spezifisch genug, um implementiert und verifiziert werden zu können)
- Begründung: Implementierende müssen verstehen, was erforderlich ist, ohne juristischen Hintergrund

**Prinzip 4: Rückverfolgbarkeit**

- Jede Anforderung MUSS die Quelle zitieren (Vorschrift-ID, Quellenangabe)
- Jede Interpretation MUSS den ursprünglichen Text bewahren (Feld "Ursprünglicher Anforderungstext")
- Prüfpfad der Extraktion und Überprüfung aufrechterhalten
- Reverse Lookup ermöglichen (bei einer Massnahme alle erfüllten Anforderungen finden)
- Begründung: Auditoren werden Nachweis verlangen, dass extrahierte Anforderungen mit der regulatorischen Quelle übereinstimmen

**Prinzip 5: Konsistenz**

- Konsistente Sprache über Anforderungen aus verschiedenen Vorschriften hinweg verwenden
- Dieselbe Granularitätsleitlinie für alle Extraktionen anwenden
- Dieselbe Kategorisierungslogik für ähnliche Anforderungen verwenden
- Begründung: Inkonsistenz schafft Verwirrung, erschwert die Massnahmenzuordnung

**Prinzip 6: Kein Interpretationsschleichen**

- Keine Anforderungen hinzufügen, die über das von der Vorschrift Vorgeschriebene hinausgehen
- Beispiel: Wenn die Vorschrift "jährliche Überprüfung" sagt, nicht "vierteljährliche Überprüfung" extrahieren
- Compliance-Anforderungen von organisatorischen Best Practices trennen
- Wenn [Organisation] regulatorische Anforderungen übertreffen möchte, dies separat als Organisationsrichtlinie dokumentieren
- Begründung: Das Compliance-Framework muss tatsächliche Verpflichtungen, nicht Ambitionen widerspiegeln

**Prinzip 7: Rechtliche Überprüfung**

- Alle Extraktionen SOLLTEN von qualifizierten Rechtsberatern überprüft werden
- Rechtliche Überprüfung bestätigt: Interpretation ist rechtlich korrekt; keine verbindlichen Anforderungen wurden übersehen; keine Verpflichtungen durch Interpretation hinzugefügt
- Rechtliche Überprüfung dokumentieren (Feld "Überprüft durch")
- Begründung: Anforderungsextraktion hat rechtliche Implikationen; juristische Expertise ist für Genauigkeit unerlässlich

**Prinzip 8: Regulatorischer Kontext**

- Vorschrift in ihrer Gesamtheit betrachten, nicht Artikel für Artikel isoliert
- Anforderungen können Definitionen, Ausnahmen oder Verfahren anderswo in der Vorschrift referenzieren
- Anforderungen im Licht des regulatorischen Zwecks und der Durchsetzungsleitlinien interpretieren
- Regulatorische FAQ, Leitliniendokumente, Durchsetzungsmassnahmen für Klarstellung konsultieren
- Begründung: Vorschriften sind ganzheitliche Instrumente; Kontext ist für korrekte Interpretation wichtig

**Prinzip 9: Aktualisierung bei Vorschriftsänderungen**

- Wenn eine Vorschrift geändert wird, ALLE extrahierten Anforderungen aus dieser Vorschrift überprüfen
- Interpretierte Anforderungen aktualisieren, wenn sich die regulatorische Sprache geändert hat
- Neue Anforderungen hinzufügen, wenn Änderungen neue Verpflichtungen schaffen
- Anforderungen archivieren, wenn Bestimmungen aufgehoben wurden
- Begründung: Die regulatorische Landschaft entwickelt sich weiter; das Compliance-Framework muss aktuell bleiben

**Prinzip 10: Technologie-Lock-in vermeiden**

- Anforderungen nicht präskriptiver extrahieren, als die Vorschrift vorschreibt
- Wenn die Vorschrift "Verschlüsselung" sagt, keinen Algorithmus spezifizieren, es sei denn, die Vorschrift tut es
- Wenn die Vorschrift "branchenüblich" sagt, diese Flexibilität bewahren
- Technologische Weiterentwicklung zulassen
- Begründung: Technologie entwickelt sich schneller als Vorschriften; überspezifische Anforderungen werden obsolet

---

# Massnahmenzuordnungsmethodik

## Zuordnungsansatz

Die Massnahmenzuordnung ist der systematische Prozess der Identifizierung, welche ISO 27001 Annex A-Massnahmen extrahierte regulatorische Anforderungen erfüllen. Sie stellt die kritische Verbindung zwischen dem, was Vorschriften verlangen, und dem, wie [Organisation] diese Anforderungen durch Sicherheitsmassnahmen umsetzt.

### Die Zuordnungsherausforderung

Die Zuordnung regulatorischer Anforderungen zu ISO 27001-Massnahmen stellt mehrere Herausforderungen dar:

**Sprachinkongruenz**:

- Vorschriften verwenden juristische Sprache, die sich auf Verpflichtungen und Strafen konzentriert
- ISO 27001 verwendet Sicherheitsmanagementsprache, die sich auf Risiken und Massnahmen konzentriert
- Dasselbe Konzept wird unterschiedlich beschrieben (Vorschrift: "Verhinderung unbefugten Zugangs" vs. ISO: "Zugangskontrolle")

**Unterschiede im Abstraktionsniveau**:

- Vorschriften können sehr spezifisch sein ("innerhalb von 72 Stunden benachrichtigen") oder sehr allgemein ("geeignete Sicherheitsmassnahmen")
- ISO-Massnahmen sind durchgängig Abstraktionen mittlerer Ebene (was zu tun ist, nicht wie)
- Zuordnung muss diese Abstraktionslücken überbrücken

**Many-to-Many-Beziehungen**:

- Eine Anforderung kann mehrere Massnahmen benötigen, um vollständig erfüllt zu werden
- Eine Massnahme kann mehrere Anforderungen (teilweise oder vollständig) erfüllen
- Überschneidungen und Interdependenzen zwischen Massnahmen

**Fehlende vollständige Ausrichtung**:

- ISO 27001 ist ein allgemeiner ISMS-Standard
- Vorschriften sind spezifisch für Jurisdiktion, Sektor oder Datentyp
- Einige regulatorische Anforderungen haben möglicherweise kein direktes ISO-Massnahmenäquivalent

### Die Zuordnungsfrage

Für jede Anforderung im Anforderungsregister systematisch beantworten:

**"Welche ISO 27001 Annex A-Massnahme(n), wenn ordnungsgemäss implementiert, erfüllen diese Anforderung?"**

Diese Frage hat mehrere mögliche Antworten:

- **Einzelne primäre Massnahme**: Eine Massnahme erfüllt die Anforderung vollständig
- **Mehrere Massnahmen**: Mehrere Massnahmen wirken zusammen, um die Anforderung zu erfüllen
- **Teilweise Massnahmen**: Bestehende Massnahmen erfüllen die Anforderung teilweise, Lücken verbleiben
- **Keine bestehenden Massnahmen**: Anforderung hat keine Annex A-Massnahmenzuordnung (neue Organisationsmassnahme erforderlich)

### Zuordnungsphilosophie

**Prinzip: Bestehende Massnahmen zuerst nutzen**

- Mit ISO 27001 Annex A (93 Massnahmen in 4 Bereichen) beginnen
- Anforderungen wo möglich bestehenden Massnahmen zuordnen
- Kombination bestehender Massnahmen gegenüber neuen Massnahmen bevorzugen
- Nur organisationsspezifische Massnahmen erstellen, wenn keine Annex A-Massnahme(n) passt

**Begründung**:

- ISO 27001-Massnahmen sind gut definiert, industrieüblich und auditorenanerkannt
- Implementierung standardisierter Massnahmen ist einfacher als Design eigener Massnahmen
- Nutzung bestehender Massnahmen reduziert Komplexität

**Prinzip: Many-to-Many-Zuordnungen akzeptieren**

- Komplexe Anforderungen SOLLTEN mehreren Massnahmen zugeordnet werden (umfassende Abdeckung)
- Einfache Massnahmen SOLLTEN mehrere Anforderungen erfüllen (Effizienz)
- Keine Eins-zu-eins-Zuordnungen erzwingen, wo Many-to-Many genauer ist

**Prinzip: Teilweise Zuordnungen dokumentieren**

- Wenn eine Massnahme die Anforderung teilweise erfüllt, als Sekundär oder Unterstützend dokumentieren
- Keine vollständige Erfüllung beanspruchen, wenn Lücken bestehen
- Teilweise Zuordnungen informieren Lückenanalyse und Behebung

## Zuordnungstypen

[Organisation] verwendet ein vierufiges Klassifizierungssystem zur Charakterisierung der Beziehung zwischen einer Anforderung und einer Massnahme.

### Primär (P): Direkte, wesentliche Erfüllung

**Definition**: Massnahme erfüllt die Anforderung DIREKT und WESENTLICH. Wenn diese Massnahme ordnungsgemäss implementiert ist, wird der Grossteil der Verpflichtung der Anforderung erfüllt.

**Merkmale**:

- Der angegebene Zweck der Massnahme stimmt mit der Absicht der Anforderung überein
- Implementierung der Massnahme erreicht Compliance mit der Anforderung
- Massnahme ist der "Haupt"-Weg, wie [Organisation] diese Anforderung erfüllt
- Nachweise der Massnahmenimplementierung dienen als Nachweise der Anforderungserfüllung

**Beispielzuordnungen**:

| Anforderung (Interpretiert) | Primäre Massnahme | Begründung |
|----------------------------|------------------|-----------|
| "Zugangsmassnahmen implementieren, um den Informationszugang auf autorisiertes Personal zu beschränken" | A.5.15 Zugangskontrolle | Massnahme schreibt direkt Zugangseinschränkungen vor |
| "Sensible ruhende Daten verschlüsseln" | A.8.24 Verwendung von Kryptografie | Massnahme behandelt speziell kryptografischen Schutz einschliesslich Verschlüsselung |
| "Hintergrundüberprüfungen für Mitarbeitende mit Zugang zu sensiblen Informationen durchführen" | A.6.1 Überprüfung | Massnahme schreibt Vorabüberprüfung vor |
| "Inventar der Informationsbestände führen" | A.5.9 Inventar der Informationen und sonstiger zugehöriger Werte | Massnahme verlangt direkt ein Asset-Inventar |

**Verwendungshinweis**:

- Jede Anforderung SOLLTE mindestens eine Primärmassnahme haben (wenn keine Primärmassnahme vorhanden → wahrscheinlich eine Lücke)
- Komplexe Anforderungen können mehrere Primärmassnahmen haben, die zusammenwirken

### Sekundär (S): Teilweise oder unterstützende Erfüllung

**Definition**: Massnahme erfüllt die Anforderung TEILWEISE oder UNTERSTÜTZT die Erfüllung, erreicht jedoch allein keine vollständige Compliance. Sekundäre Massnahmen arbeiten neben primären Massnahmen, um umfassende Abdeckung zu gewährleisten.

**Merkmale**:

- Massnahme trägt zur Compliance bei, ist aber für sich allein unzureichend
- Massnahme adressiert einen Aspekt einer vielschichtigen Anforderung
- Massnahme bietet technische oder prozedurale Unterstützung für die Primärmassnahme

**Beispielzuordnungen**:

| Anforderung (Interpretiert) | Primäre Massnahme(n) | Sekundäre Massnahme(n) | Begründung |
|----------------------------|---------------------|----------------------|-----------|
| "Umfassendes Sicherheitsbewusstseinsprogramm für alle Mitarbeitenden implementieren" | A.6.3 Informationssicherheitsbewusstsein, Ausbildung und Training | A.5.2 Informationssicherheitsrollen, A.6.2 Beschäftigungsbedingungen | Primär ist das Bewusstseinsprogramm; sekundäre Massnahmen definieren, wer geschult wird |
| "Sichere Softwareentwicklungspraktiken sicherstellen" | A.8.25 Sicherer Entwicklungslebenszyklus | A.8.8 Verwaltung technischer Schwachstellen, A.8.29 Sicherheitstests | Primär ist der SDLC; Sekundäre Massnahmen adressieren Test- und Schwachstellenmanagementaspekte |
| "Schutz vor Schadsoftware auf allen Systemen" | A.8.7 Schutz vor Schadsoftware | A.8.5 Sichere Authentifizierung, A.8.19 Installation von Software | Primär ist Anti-Malware; Sekundäre reduzieren die Angriffsfläche |

### Unterstützend (Su): Indirekter Beitrag

**Definition**: Massnahme trägt INDIREKT zur Erfüllung der Anforderung bei. Unterstützende Massnahmen schaffen die organisatorische, prozedurale oder technische Grundlage, die primären und sekundären Massnahmen ermöglicht, effektiv zu funktionieren.

**Merkmale**:

- Massnahme steht nicht in direktem Zusammenhang mit dem spezifischen Mandat der Anforderung
- Massnahme bietet Hintergrundkapazität, Grundlage oder Enabler
- Fehlen der unterstützenden Massnahme würde nicht sofort eine Compliance-Lücke schaffen, würde aber die allgemeine Sicherheitslage schwächen

**Verwendungshinweis**:

- Unterstützende Zuordnungen sind optional (Beurteilung verwenden)
- Nicht übermässig verwenden (Risiko, die Zuordnungsmatrix mit tendenziösen Beziehungen zu überladen)

### Nicht Anwendbar (N/A): Keine Beziehung

**Definition**: Massnahme hat keine sinnvolle Beziehung zur Anforderung. Die Massnahme und die Anforderung adressieren völlig unterschiedliche Sicherheitsziele.

**Darstellung in der Zuordnungsmatrix**:

- N/A wird durch eine LEERE Zelle dargestellt (Zelle ist leer, keine Markierung)
- Die Mehrheit der Zellen in der Zuordnungsmatrix wird leer sein

## Struktur der Massnahmenzuordnungsmatrix

Die Massnahmenzuordnungsmatrix ist die visuelle Darstellung der Anforderungs-zu-Massnahmen-Beziehungen. Sie bietet einen Überblick über die Compliance-Abdeckung und ermöglicht die Lückenidentifizierung.

### Matrix-Layout

**Zeilen**: Anforderungen

- Jede Zeile stellt eine Anforderung aus dem Anforderungsregister dar
- Zeilenbezeichner: Anforderungs-ID (z.B. REG-DP01-32-001)
- Zeilen können nach Vorschrift oder Kategorie gruppiert werden

**Spalten**: ISO 27001 Annex A-Massnahmen

- Jede Spalte stellt eine der 93 Annex A-Massnahmen dar
- Spalten nach Bereich organisiert (A.5.x Organisatorisch, A.6.x Personen, A.7.x Physisch, A.8.x Technologisch)

**Zellen**: Zuordnungstyp

- **Werte**: P, S, Su oder leer
  - P = Primäre Zuordnung
  - S = Sekundäre Zuordnung
  - Su = Unterstützende Zuordnung
  - Leer = Nicht anwendbar

**Beispiel-Matrix-Ausschnitt**:

| Anforderungs-ID | Anforderung | A.5.15 Zugangskontrolle | A.5.16 Identitätsverw. | A.8.2 Privilegierter Zugang | A.8.5 Sichere Auth. | ... |
|----------------|-------------|------------------------|----------------------|---------------------------|-------------------|-----|
| REG-DP01-32-001 | Daten at rest verschlüsseln | | | | | ... |
| REG-DP01-32-002 | Zugangsmassnahmen implementieren | **P** | **P** | S | S | ... |
| REG-SEC15-4.2-001 | MFA für privilegierte Konten | | S | **P** | **P** | ... |

### Matrix-Wartung

**Werkzeug**: Bewertungsarbeitsmappe 4 bietet standardisierte Vorlage mit:

- Vorab ausgefüllten 93 Annex A-Massnahmenspalten
- Datenvalidierung (nur P, S, Su, leer erlaubt)
- Bedingter Formatierung für visuelle Hervorhebung
- Formeln zur Lückenerkennung

**Aktualisierungsauslöser**:
Matrix MUSS aktualisiert werden, wenn:

- Neue Anforderung zum Anforderungsregister hinzugefügt wird
- Anforderungsinterpretation sich ändert
- Massnahmenimplementierung sich ändert
- Neue Massnahme zum ISMS hinzugefügt wird
- Massnahme entfernt oder veraltet ist
- Lückenbehebung abgeschlossen ist

## Eins-zu-Viele- und Viele-zu-Eins-Zuordnungen

### Eine Anforderung → Mehrere Massnahmen (Eins-zu-Viele)

**Szenario**: Eine einzelne regulatorische Anforderung schreibt einen umfassenden Sicherheitsansatz vor, den keine einzelne Massnahme erfüllen kann. Mehrere Massnahmen müssen zusammenwirken, um Compliance zu erreichen.

**Beispiel: Umfassendes Zugangsverwaltung**

**Anforderung** (REG-DP01-32-003): "Umfassendes Zugangsverwaltung implementieren, das sicherstellt, dass nur autorisiertes Personal basierend auf dem Geschäftsbedarf auf sensible Informationen zugreift, mit Authentifizierungs-, Autorisierungs- und Auditierfähigkeiten"

**Massnahmenzuordnungen**:

- **A.5.15 Zugangskontrolle** (Primär) — Legt Zugangssteuerungsrichtlinie fest
- **A.5.16 Identitätsverwaltung** (Primär) — Verwaltet Benutzeridentitäten
- **A.5.17 Authentifizierungsinformationen** (Primär) — Verwaltet Anmeldeinformationen
- **A.5.18 Zugriffsrechte** (Primär) — Verwaltet Autorisierung
- **A.8.2 Privilegierte Zugriffsrechte** (Sekundär) — Verwaltet privilegierte Konten
- **A.8.3 Einschränkung des Informationszugriffs** (Sekundär) — Technische Zugangseinschränkungen
- **A.8.5 Sichere Authentifizierung** (Sekundär) — Authentifizierungsmechanismen
- **A.8.15 Protokollierung** (Unterstützend) — Prüfpfad des Zugangs

### Mehrere Anforderungen → Eine Massnahme (Viele-zu-Eins)

**Szenario**: Eine einzelne Massnahme, wenn implementiert, erfüllt mehrere regulatorische Anforderungen gleichzeitig. Dies ist Effizienz in der Praxis — einmal implementieren, mehrere Anforderungen erfüllen.

**Beispiel: Verschlüsselungsmassnahme**

**Massnahme**: A.8.24 Verwendung von Kryptografie

**Erfüllt Anforderungen**:

- REG-DP01-32-001: "Personenbezogene Daten at rest verschlüsseln" (Primär)
- REG-DP01-32-002: "Personenbezogene Daten bei der Übertragung verschlüsseln" (Primär)
- REG-FIN05-15-003: "Zahlungskartendaten durch Verschlüsselung schützen" (Primär)
- REG-HEALTH-12-001: "Elektronische Gesundheitsakten verschlüsseln" (Primär)
- REG-SEC15-4.4-002: "Branchenübliche Verschlüsselung für sensible Daten verwenden" (Primär)

**Interpretation**:

- Eine Verschlüsselungsmassnahmenimplementierung
- Erfüllt Anforderungen aus 5 verschiedenen Vorschriften
- Nachweise der Verschlüsselungsimplementierung dienen als Nachweise für alle 5 Anforderungen
- Effizienz: Einzelne Massnahme, mehrere Compliance-Vorteile

## Über Annex A hinaus: Organisationsspezifische Massnahmen

### Wann keine Annex A-Massnahme passt

Trotz 93 Massnahmen, die einen umfassenden ISMS-Geltungsbereich abdecken, verlangen regulatorische Anforderungen gelegentlich Fähigkeiten, die von keiner Annex A-Massnahme adressiert werden.

**Situationen, die organisationsspezifische Massnahmen erfordern**:

**Sektorspezifische technische Anforderungen**:

- Finanzdienstleistungen: "Transaktionsmonitoring zur Betrugserkennung implementieren"
  - Keine direkte Annex A-Massnahme für Betrugserkennungssysteme
- Gesundheitswesen: "Break-the-Glass-Zugang für medizinische Notfälle implementieren"
  - Notfallzugangsüberschreibung ist sektorspezifisch

**Jurisdiktionsspezifische Berichtspflichten**:

- "Jährliche Cybersicherheitsbestätigung bei Regulator X bis 31. März einreichen"
  - Annex A hat keine Massnahme für regulatorische Einreichungsprozesse

**Vertragliche Verpflichtungen**:

- "Kunden gemäss SLA Abschnitt 12 monatliches Sicherheitsmetriken-Dashboard bereitstellen"
  - Kundenspezifische Berichterstattung ist vertraglich, nicht von Annex A abgedeckt

### Erstellen organisationsspezifischer Massnahmen

Wenn die Lückenanalyse (Abschnitt 4) Anforderungen ohne Annex A-Zuordnung identifiziert, MUSS [Organisation] organisationsspezifische Massnahmen nach folgender Methodik erstellen:

**Schritt 1: Lücke bestätigen**

- Bestätigen, dass KEINE Annex A-Massnahme, auch nicht teilweise, die Anforderung adressiert
- Mit ISMS-Manager, Massnahmenverantwortlichen, Rechtsberatung konsultieren
- Begründung für neue Massnahme dokumentieren

**Schritt 2: Massnahme definieren**

- **Massnahmen-ID**: CTRL-ORG-[Bereich]-[Sequenz]
  - Bereich: ORG (Organisatorisch), PEO (Personen), PHY (Physisch), TEC (Technologisch)
  - Beispiel: CTRL-ORG-TEC-001 (erste organisatorische technologische Massnahme)
- **Massnahmenname**: Klare, präzise Beschreibung
- **Massnahmenziel**: Warum diese Massnahme existiert
- **Massnahmenbeschreibung**: Was die Massnahme tut

**Schritt 3: Implementierung spezifizieren**

- **Implementierungshinweise**: Wie die Massnahme implementiert wird
- **Nachweisanforderungen**: Wie die Massnahmenwirksamkeit demonstriert wird

**Schritt 4: Eigentümerschaft zuweisen**

- **Massnahmenverantwortlicher**: Wer die Massnahme implementiert und aufrechterhält
- **Genehmigung**: Genehmigung der Geschäftsleitung für neue Massnahmen

**Schritt 5: In ISMS integrieren**

- Zur Anwendbarkeitserklärung (SoA) hinzufügen, falls Zertifizierung angestrebt wird
- Zur Massnahmenzuordnungsmatrix hinzufügen (neue Spalte)
- In den Geltungsbereich des internen Audits aufnehmen

**Schritt 6: Im organisatorischen Massnahmenregister dokumentieren**

- Separates Register organisationsspezifischer Massnahmen führen
- Verknüpfung mit regulatorischen Anforderungen, die die Erstellung veranlasst haben

### Governance organisationsspezifischer Massnahmen

**Genehmigungsprozess**:

- Neue organisationsspezifische Massnahmen erfordern Genehmigung der Geschäftsleitung
- Begründung dokumentiert (regulatorische Anforderung, Geschäftsbedarf, Risikominderung)

**Überprüfungszyklus**:

- Organisationsspezifische Massnahmen jährlich überprüfen
- Fortbestehenden Bedarf bestätigen (hat sich die Vorschrift geändert? hat Annex A eine relevante Massnahme in neuerer Version hinzugefügt?)

**Einschränkung**:

- Proliferation organisationsspezifischer Massnahmen vermeiden
- Verbesserung von Annex A-Massnahmen gegenüber Erstellung neuer Massnahmen bevorzugen
- Zu viele organisationsspezifische Massnahmen deuten hin auf: Missverständnis von Annex A oder Überinterpretation von Anforderungen

---

# Lückenanalyseprozess

Die Lückenanalyse ist die systematische Identifizierung regulatorischer Anforderungen, die durch bestehende oder geplante Massnahmen nicht vollständig erfüllt werden. Sie ist der entscheidende "Realitätscheck", der beantwortet: "Wo sind wir nicht compliant?"

## Lückenidentifizierung

### Lückentypen

**Vollständige Lücken**:

- **Definition**: Anforderung hat KEINE zugeordnete Massnahme (keine P-, S- oder Su-Zuordnungen in der Massnahmenzuordnungsmatrix)
- **Schweregrad**: Kritisch — repräsentiert totale Nichteinhaltung mit der Anforderung
- **Identifizierung**: Anforderungszeile in der Matrix ist völlig leer
- **Beispiel**:
  - Anforderung: "Aufsichtsbehörde innerhalb von 72 Stunden über Datenschutzverletzungen benachrichtigen"
  - Aktuelle Massnahmen: [Organisation] hat Vorfallbehandlungsverfahren (A.5.24-A.5.28), aber keinen spezifischen Verletzungsbenachrichtigungsprozess für Aufsichtsbehörden
  - Lücke: Keine Massnahme regelt die 72-Stunden-Benachrichtigungsanforderung

**Teilweise Lücken**:

- **Definition**: Anforderung hat sekundäre oder unterstützende Zuordnungen, aber KEINE primäre Zuordnung, ODER primäre Zuordnung existiert, aber Massnahme implementiert die Anforderung nur teilweise
- **Schweregrad**: Hoch — teilweise Compliance, aber erhebliche Lücken bleiben
- **Beispiel 1** (Keine Primäre):
  - Anforderung: "Penetrationstest aller internetzugewandten Systeme jährlich durchführen"
  - Aktuelle Massnahmen: A.8.8 Verwaltung technischer Schwachstellen (Sekundär — Schwachstellenscanning, kein Penetrationstest)
  - Lücke: Keine Massnahme schreibt speziell Penetrationstests vor

**Umsetzungslücken**:

- **Definition**: Anforderung ist der entsprechenden Massnahme zugeordnet (primäre Zuordnung vorhanden), aber Massnahme ist noch nicht implementiert oder unzureichend implementiert
- **Schweregrad**: Variiert (Hoch wenn Frist naht, Mittel sonst)
- **Beispiel**:
  - Anforderung: "Sicherheitsbewusstseinstraining für alle Mitarbeitenden jährlich durchführen"
  - Zugeordnete Massnahme: A.6.3 Informationssicherheitsbewusstsein (Primär)
  - Aktueller Stand: Richtlinie existiert, aber Training nicht konsistent durchgeführt, keine Verfolgung
  - Lücke: Massnahme definiert, aber nicht effektiv implementiert

### Lückenidentifizierungsprozess

**Schritt 1: Analyse der Massnahmenzuordnungsmatrix**

- Abgeschlossene Massnahmenzuordnungsmatrix überprüfen
- Zeilen (Anforderungen) ohne primäre Zuordnungen identifizieren → vollständige oder teilweise Lücken
- Für jede Anforderung beurteilen: Hat sie eine primäre Zuordnung? Decken sekundäre/unterstützende Zuordnungen teilweise ab?

**Schritt 2: Überprüfung der Massnahmenimplementierung**

- Für Anforderungen mit primären Zuordnungen den Implementierungsstatus der Massnahmen verifizieren
- Quellen: Implementierungsstatus-Feld des Anforderungsregisters, interne Auditberichte, Massnahmeneffektivitätsbewertungen
- Umsetzungslücken identifizieren

**Schritt 3: Nachweisverifizierung**

- Für als "Implementiert" markierte Anforderungen verifizieren, dass Nachweise vorhanden sind
- Kann [Organisation] Compliance durch Dokumentation, Protokolle, Berichte demonstrieren?

**Schritt 4: Stakeholder-Konsultation**

- **Rechtsberatung**: Lückeninterpretation rechtlich bestätigen
- **Massnahmenverantwortliche**: Bestätigen, dass Massnahmen die Anforderung nicht erfüllen können
- **Compliance-Beauftragter**: Lücken nach regulatorischem Risiko priorisieren

**Schritt 5: Lückendokumentation**

- ALLE identifizierten Lücken im Lückenregister dokumentieren
- Lückenregister-Felder:
  - Lücken-ID (eindeutiger Bezeichner)
  - Anforderungs-ID (welche Anforderung nicht erfüllt)
  - Lückentyp (vollständig, teilweise, Umsetzung)
  - Lückenbeschreibung (was fehlt)
  - Risiko/Auswirkung (Konsequenz der Nichteinhaltung)
  - Priorität (Hoch/Mittel/Niedrig)
  - Behebungsplan
  - Verantwortliche Partei
  - Zieldatum
  - Status

## Lückenpriorisierung

### Priorisierungsfaktoren

**Faktor 1: Regulatorischer Tier**

- **Tier 1 Obligatorisch**: Höchste Priorität (rechtliche Verpflichtung, direkte Durchsetzung)
- **Tier 2 Bedingt**: Hohe Priorität wenn Bedingung erfüllt
- **Tier 3 Informativ**: Niedrigere Priorität (Best Practice, nicht rechtlich vorgeschrieben)

**Faktor 2: Schwere der rechtlichen Konsequenz**

- **Strafrechtlich/Erhebliche Bussen**: Höchste Priorität
- **Zivilrechtliche Sanktionen/Moderate Bussen**: Hohe Priorität
- **Reputationsschaden**: Mittel-Hohe Priorität
- **Geringfügige Sanktionen/Verwarnungen**: Niedrigere Priorität

**Faktor 3: Compliance-Frist**

- **Sofort** (Frist abgelaufen oder <30 Tage): Höchste Priorität
- **Kurzfristig** (30-90 Tage): Hohe Priorität
- **Mittelfristig** (90 Tage - 1 Jahr): Mittlere Priorität
- **Langfristig** (>1 Jahr): Niedrigere Priorität

**Faktor 4: Implementierungskomplexität**

- **Schnelle Erfolge** (geringe Komplexität, hohe Auswirkung): Für sofortige Massnahmen priorisieren
- **Komplex, Hohe Auswirkung**: Priorisieren, aber sorgfältig planen
- **Einfach, Geringe Auswirkung**: Mit anderen ähnlichen Lücken bündeln

**Faktor 5: Geschäftsauswirkung**

- **Kundenseitig**: Höhere Priorität (SLA-Verpflichtungen, Kundenvertrauen)
- **Umsatzkritisch**: Höchste Priorität
- **Nicht-kritisch**: Niedrigere Priorität

### Priorisierungsmatrix

**Priorität: KRITISCH** (Sofortiger Handlungsbedarf)

- Vollständige oder teilweise Lücke in Tier-1-Vorschrift
- Frist abgelaufen oder <30 Tage
- Erhebliche rechtliche Konsequenz (strafrechtliche Haftung, grosse Bussen)

**Priorität: HOCH** (Dringend, Behebung planen)

- Vollständige oder teilweise Lücke in Tier-1-Vorschrift
- Frist 30-90 Tage
- Erhebliche rechtliche Konsequenz (zivilrechtliche Sanktionen)

**Priorität: MITTEL** (Planen und Umsetzen)

- Teilweise Lücke in Tier 1, oder vollständige Lücke in Tier 2 (falls anwendbar)
- Frist 90 Tage - 1 Jahr
- Moderate rechtliche Konsequenz

**Priorität: NIEDRIG** (Strategische Planung)

- Nur Umsetzungslücke (Massnahme definiert, Implementierung in Bearbeitung)
- Lücke in Tier 3 (informativ/Best Practice)
- Frist >1 Jahr

**Beispielpriorisierungen**:

| Lückenbeschreibung | Reg. Tier | Frist | Konsequenz | Komplexität | Priorität | Begründung |
|-------------------|----------|-------|-----------|------------|----------|-----------|
| Kein Verletzungsbenachrichtigungsprozess für 72-Std.-Anforderung | Tier 1 | 30 Tage | Grosse Bussen (DSGVO) | Niedrig | KRITISCH | Tier 1, unmittelbare Frist, erhebliche Strafe |
| Teilweise Verschlüsselungsimplementierung (nur at rest) | Tier 1 | 90 Tage | Moderate Bussen | Mittel | HOCH | Tier 1, teilweise Lücke |
| Kein Penetrationstest-Programm | Tier 2 (PCI DSS gilt) | 6 Monate | Verlust Kartenverarbeitungsfähigkeit | Hoch | HOCH | Tier 2, aber geschäftskritisch |
| Inkonsistentes Sicherheitsbewusstseinstraining | Tier 1 | Keine Frist | Gering | Niedrig | MITTEL | Umsetzungslücke, geringe Komplexität |

## Lückenbehebungsansätze

### Behebungsoptionen

**Option 1: Neue Massnahme implementieren**

- **Wann**: Vollständige Lücke, keine bestehende Massnahme adressiert Anforderung
- **Aktion**: Organisationsspezifische Massnahme erstellen und implementieren (gemäss Abschnitt 3.5)

**Option 2: Bestehende Massnahme verbessern**

- **Wann**: Teilweise Lücke, bestehende Massnahme ist nah, aber unvollständig
- **Aktion**: Geltungsbereich erweitern, Fähigkeiten hinzufügen oder Implementierung verbessern

**Option 3: Kombination von Massnahmen implementieren**

- **Wann**: Komplexe Anforderung benötigt mehrere gemeinsam wirkende Massnahmen
- **Aktion**: Mehrere Massnahmen (bestehende Annex A oder neue Organisationsmassnahmen) implementieren

**Option 4: Kompensationsmassnahme implementieren**

- **Wann**: Ideale Massnahme kann nicht implementiert werden (technische, kosten-, betriebliche Einschränkungen), aber alternativer Ansatz erreicht dasselbe Ziel
- **Aktion**: Andere Massnahme implementieren, die die Lücke kompensiert
- **Vorsicht**: Regulatoren/Auditoren können Kompensationsmassnahmen hinterfragen; starke Begründung und Nachweise der Wirksamkeit erforderlich

**Option 5: Risiko akzeptieren**

- **Wann**: Lücke besteht, aber Implementierungskosten/-komplexität übersteigen das Risiko, ODER Lücke hat niedrige Priorität und Ressourcen sind begrenzt
- **Einschränkungen**:
  - KANN NICHT für Tier-1-Pflichtanforderungen (rechtliche Verpflichtung)
  - SOLLTE NICHT für Lücken mit hoher Priorität
  - MUSS bei Änderungen der Umstände erneut bewertet werden

### Behebungsplanung

Für jede Lückenbehebung:

**Behebungsplan entwickeln**:

- Lücken-ID und Beschreibung
- Gewählter Behebungsansatz
- Detaillierte Umsetzungsschritte
- Verantwortliche Partei
- Benötigte Ressourcen (Budget, Personal, Technologie)
- Zeitplan (Startdatum, Meilensteine, Fertigstellungsdatum)

**Genehmigung einholen**:

- Massnahmenverantwortlicher genehmigt Behebungsplan
- ISMS-Manager/Compliance-Beauftragter genehmigt
- Geschäftsleitung genehmigt (bei erheblichen Investitionen oder Risikoakzeptanzen)

**Abschluss verifizieren**:

- Implementierte Massnahme testen
- Nachweise erheben
- Anforderung neu bewerten
- Massnahmenzuordnungsmatrix aktualisieren
- Lückenregister aktualisieren (Status: Geschlossen)

## Lückenverfolgung

### Lückenregister

[Organisation] MUSS ein Lückenregister führen, das alle identifizierten Compliance-Lücken und deren Behebungsstatus dokumentiert.

**Lückenregister-Felder**:

- **Lücken-ID**: Eindeutiger Bezeichner (LÜCKE-JJJJ-###)
- **Identifizierungsdatum**: Wann Lücke identifiziert wurde
- **Anforderungs-ID**: Welche Anforderung nicht erfüllt wird
- **Vorschriftname**: Übergeordnete Vorschrift
- **Lückentyp**: Vollständig, Teilweise, Umsetzung
- **Lückenbeschreibung**: Was fehlt (klar, spezifisch)
- **Risiko/Auswirkung**: Konsequenz der Nichteinhaltung
- **Priorität**: Kritisch/Hoch/Mittel/Niedrig
- **Behebungsansatz**: Neue Massnahme, Verbesserung, Kombination, Kompensation, Risikoakzeptanz
- **Verantwortliche Partei**: Wer die Behebung verantwortet
- **Zieldatum**: Wann Lücke geschlossen wird
- **Status**: Offen, In Bearbeitung, Ausstehende Genehmigung, Geschlossen, Risiko akzeptiert

### Lückenverwaltungsprozess

**Vierteljährliche Lückenüberprüfung**:

- ISMS-Manager, Compliance-Beauftragter, Rechtsberatung überprüfen Lückenregister
- Fortschritt bei Behebungsplänen beurteilen
- Lücken bei veränderten Umständen neu priorisieren
- Überfällige Behebungen identifizieren und eskalieren

**Management-Review-Integration**:

- Lückenmetriken in ISO 27001 Management Review (Klausel 9.3) berichtet
- Metriken: Gesamtlücken, Lücken nach Priorität, in diesem Zeitraum geschlossene Lücken, überfällige Lücken

**Lückenmetriken und KPIs**:

- **Gesamtoffene Lücken** (Anzahl nach Priorität)
- **Mittlere Zeit zur Lückenschliessung** (nach Priorität)
- **Lückenalterung** (Lücken offen >90 Tage, >180 Tage, >1 Jahr)
- **Lückenschliessungsrate** (geschlossene Lücken pro Monat/Quartal)
- **Prozentsatz erfüllter Anforderungen**

---

# Rückverfolgbarkeitsanforderungen

Rückverfolgbarkeit ist die Fähigkeit, Beziehungen zwischen Vorschriften, Anforderungen, Massnahmen und Nachweisen in beide Richtungen (vorwärts und rückwärts) zu verfolgen. Sie ist grundlegend für Auditvorbereitung und Compliance-Nachweis.

## Vorwärts-Rückverfolgbarkeit

### Die Vorwärts-Rückverfolgbarkeitskette

**Definition**: Vorwärts-Rückverfolgbarkeit ist die Fähigkeit, mit einer Vorschrift zu beginnen und bis zu den Nachweisen zu verfolgen, die Compliance demonstrieren.

**Die Vorwärtskette**:
```
Vorschrift (in ISMS-POL-00)
    ↓
Extrahierte Anforderungen (im Anforderungsregister)
    ↓
Zugeordnete Massnahmen (in der Massnahmenzuordnungsmatrix)
    ↓
Implementierte Massnahmen (in Massnahmendokumentation, Richtlinien, Verfahren)
    ↓
Erhobene Nachweise (im Nachweisregister und Repository)
```

**Beispiel Vorwärts-Trace**:

**Ausgangspunkt**: Datenschutzvorschrift Artikel 32 ("Sicherheit der Verarbeitung")

**Schritt 1**: In ISMS-POL-00 identifizieren

- Vorschrift-ID: REG-DP01
- Tier: 1 — Obligatorisch
- Status: Anwendbar

**Schritt 2**: Extrahierte Anforderungen im Anforderungsregister finden

- REG-DP01-32-001: "Verschlüsselung für personenbezogene Daten at rest und bei Übertragung implementieren"
- REG-DP01-32-002: "Zugangsmassnahmen zum Schutz personenbezogener Daten auf autorisiertes Personal beschränken"
- REG-DP01-32-003: "Regelmässige Tests und Bewertungen der Sicherheitsmassnahmen durchführen"

**Schritt 3**: Zugeordnete Massnahmen in der Massnahmenzuordnungsmatrix identifizieren

- REG-DP01-32-001 → A.8.24 Verwendung von Kryptografie (Primär)
- REG-DP01-32-002 → A.5.15 Zugangskontrolle (Primär), A.5.16 Identitätsverwaltung (Primär), A.5.18 Zugriffsrechte (Primär)
- REG-DP01-32-003 → A.5.36 Einhaltung von Richtlinien (Primär), A.8.8 Verwaltung technischer Schwachstellen (Sekundär)

**Schritt 4**: Implementierte Massnahmen überprüfen

- A.8.24: Verschlüsselungsrichtlinie v2.1, Schlüsselverwaltungsverfahren
- A.5.15: Zugangssteuerungsrichtlinie v3.0
- A.5.36: Compliance-Überwachungsverfahren, Penetrationstest-Standard

**Schritt 5**: Nachweise lokalisieren

- A.8.24-Nachweise: Verschlüsselung-at-rest-Konfiguration, TLS-Konfiguration, Schlüsselverwaltungs-Prüfprotokolle
- A.5.15/16/18-Nachweise: Zugangskontrollmatrix, Zugriffsantrags-/Genehmigungsprotokolle
- A.5.36/A.8.8-Nachweise: Jährlicher Penetrationstest-Bericht, vierteljährliche Schwachstellenscan-Ergebnisse

**Ergebnis**: Kann dem Auditor zeigen: "Hier ist die Vorschrift, hier sind die extrahierten Anforderungen, hier sind die implementierten Massnahmen, und hier sind die Nachweise, die belegen, dass sie funktionieren."

### Warum Vorwärts-Rückverfolgbarkeit wichtig ist

- **Auditvorbereitung**: Auditor fragt "Zeigen Sie mir, wie Sie Artikel 32 einhalten" — Vorwärts-Trace liefert vollständige Antwort
- **Regulatorische Anfragen**: Regulator fordert Compliance-Nachweis — systematischer Ansatz sichtbar
- **Executive Reporting**: Management fragt "Sind wir datenschutzkonform?" — Fortschrittsbericht nach Vorschrift möglich
- **Lückenidentifizierung**: Vorwärts-Trace bricht ab, wenn Anforderung keine Massnahmenzuordnung hat

## Rückwärts-Rückverfolgbarkeit

### Die Rückwärts-Rückverfolgbarkeitskette

**Definition**: Rückwärts-Rückverfolgbarkeit ist die Fähigkeit, mit einem Nachweis (oder einer Massnahme) zu beginnen und zurück zu den erfüllten Vorschriften zu verfolgen.

**Die Rückwärtskette**:
```
Nachweise (im Nachweisregister und Repository)
    ↓
Implementierte Massnahme (dokumentiert in Richtlinien, Verfahren)
    ↓
Zugeordnete Anforderungen (in der Massnahmenzuordnungsmatrix)
    ↓
Quellvorschrift (in ISMS-POL-00)
```

**Beispiel Rückwärts-Trace**:

**Ausgangspunkt**: Verschlüsselungsrichtlinie-Dokument (v2.1)

**Schritt 1**: Als Nachweis für Massnahme identifizieren

- Massnahme: A.8.24 Verwendung von Kryptografie
- Nachweistyp: Richtliniendokument

**Schritt 2**: Massnahme in Massnahmenzuordnungsmatrix finden

- A.8.24-Spalte zeigt Zuordnungen zu mehreren Anforderungen:
  - REG-DP01-32-001 (Primär) — Datenschutzvorschrift
  - REG-FIN05-15-003 (Primär) — Finanzvorschrift
  - REG-HEALTH-12-001 (Primär) — Gesundheitsvorschrift
  - REG-SEC15-4.4-002 (Primär) — Sicherheitsstandard

**Schritt 3**: Anforderungen zurück zu Vorschriften verfolgen

- REG-DP01-32-001 → Datenschutzvorschrift Artikel 32
- REG-FIN05-15-003 → Finanzvorschrift Abschnitt 15
- REG-HEALTH-12-001 → Gesundheitsdatensicherheitsgesetz Artikel 12
- REG-SEC15-4.4-002 → Sicherheitsstandard Abschnitt 4.4

**Ergebnis**: Einzelne Verschlüsselungsrichtlinie erfüllt Anforderungen aus VIER verschiedenen Vorschriften. Effizienz durch Wiederverwendung.

### Warum Rückwärts-Rückverfolgbarkeit wichtig ist

- **Nachweiseffizienz**: Wissen, welche Nachweise welche Anforderungen erfüllen; Doppelerhebung vermeiden
- **Massnahmenbegründung**: Erklären, WARUM Massnahmen existieren (welche Vorschriften sie vorschreiben)
- **Auswirkungsanalyse bei Massnahmenänderungen**: Wenn Massnahme geändert oder entfernt wird, sofort betroffene Anforderungen identifizieren
- **Audit-Effizienz**: Bei Auditorüberprüfung von Nachweisen schnell alle erfüllten Vorschriften identifizieren

## Änderungs-Rückverfolgbarkeit

### Arten von Änderungen, die Rückverfolgbarkeit erfordern

**Vorschriftsänderungen**:

- Vorschrift geändert (neue Artikel hinzugefügt, bestehende geändert, Artikel aufgehoben)
- Neue Vorschrift wird anwendbar
- Vorschrift aufgehoben oder läuft aus

**Massnahmenänderungen**:

- Massnahmenimplementierung geändert (technische Änderungen, Geltungsbereichsänderungen)
- Massnahme verbessert oder erweitert
- Massnahme veraltet oder entfernt

**Organisatorische Änderungen**:

- Geschäftserweiterung (neue Dienstleistungen, neue geografische Märkte)
- Fusionen und Übernahmen
- Outsourcing oder Insourcing von Dienstleistungen
- Technologieänderungen (Cloud-Migration, neue Plattformen)

### Änderungsauswirkungsanalyse mittels Rückverfolgbarkeit

**Bei Vorschriftsänderungen**:

1. Geänderte Vorschrift in ISMS-POL-00 identifizieren
2. Vorwärts-Rückverfolgbarkeit nutzen, um alle aus dieser Vorschrift extrahierten Anforderungen zu finden
3. Geänderten regulatorischen Text überprüfen: Sind bestehende Anforderungen noch korrekt? Neue Anforderungen geschaffen? Bestehende Anforderungen obsolet?
4. Massnahmenzuordnungen für betroffene Anforderungen neu bewerten
5. Nachweise bei Änderung von Anforderung oder Massnahmenzuordnungen aktualisieren

**Beispiel**:

- Datenschutzvorschrift Artikel 32 geändert, um "Verschlüsselung unter Verwendung post-quantenkryptografischer Algorithmen innerhalb von 2 Jahren" zu verlangen
- Vorwärts-Trace findet REG-DP01-32-001 ("Verschlüsselung für personenbezogene Daten implementieren")
- Interpretierte Anforderung aktualisieren, um Post-Quanten-Anforderung einzuschliessen
- A.8.24 beurteilen: Aktuelle Implementierung nutzt klassische Algorithmen
- Lücke identifizieren: Migration zu Post-Quanten-Algorithmen planen
- Zum Lückenregister mit 2-jähriger Frist hinzufügen

**Bei Massnahmenänderungen**:

1. Zu ändernde Massnahme identifizieren
2. Rückwärts-Rückverfolgbarkeit nutzen, um alle dieser Massnahme zugeordneten Anforderungen zu finden
3. Auswirkung der Änderung auf jede zugeordnete Anforderung beurteilen
4. Massnahmenzuordnungsmatrix aktualisieren, wenn Zuordnungstypen sich ändern
5. Lückenregister aktualisieren, wenn Lücken entstehen oder geschlossen werden

**Beispiel**:

- A.8.15 (Protokollierung) geändert: Protokollaufbewahrung von 2 Jahren auf 6 Monate reduziert
- Rückwärts-Trace findet zugeordnete Anforderungen:
  - REG-DP01-33-001: "Protokolle mindestens 1 Jahr aufbewahren" (Primäre Zuordnung)
  - REG-FIN05-10-002: "Protokolle von Finanztransaktionen 7 Jahre aufbewahren" (Primäre Zuordnung)
- Auswirkungsbewertung: 6-Monate-Aufbewahrung erfüllt KEINE der Anforderungen → LÜCKEN ENTSTEHEN
- Entscheidung: Massnahmenänderung RÜCKGÄNGIG MACHEN oder differenzierte Aufbewahrung implementieren

### Werkzeuge zur Änderungs-Rückverfolgbarkeit

- **Anforderungsregister-Verknüpfung**: Vorschrift-ID-Feld verknüpft mit ISMS-POL-00
- **Bidirektionalität der Massnahmenzuordnungsmatrix**: Ermöglicht sowohl Vorwärts- als auch Rückwärts-Trace
- **Änderungsprotokoll-Integration**: Kreuzreferenz von Änderungsprotokollen zur Identifizierung zusammenhängender Änderungen

## Prüfpfad

Jede Änderung im regulatorischen Compliance-Framework MUSS protokolliert werden, um eine vollständige, prüfbare Historie zu erstellen.

### Was zu protokollieren ist

**Anforderungsregisteränderungen**:

- Neue Anforderung hinzugefügt (wer, wann, aus welcher Vorschrift)
- Anforderungsinterpretation geändert (alte → neue Interpretation, wer, wann, warum)
- Anforderungsstatus geändert
- Anforderung archiviert

**Massnahmenzuordnungsmatrix-Änderungen**:

- Neue Zuordnung erstellt (Anforderung X → Massnahme Y, Zuordnungstyp P/S/Su, wer, wann)
- Zuordnungstyp geändert (S → P weil Massnahme verbessert)
- Zuordnung entfernt

**Lückenregisteränderungen**:

- Lücke identifiziert
- Lückenpriorität geändert
- Lückenbehebungsplan aktualisiert
- Lückenstatus geändert (Offen → In Bearbeitung → Geschlossen)

### Wo Protokolle gepflegt werden

**Zentralisiertes Compliance-Protokoll** (Optional, aber empfohlen):

- Einzelnes Protokoll für ALLE Compliance-Framework-Änderungen
- Chronologische Aufzeichnung über alle Dokumente hinweg

**Beispieleinträge im zentralisierten Protokoll**:

| Datum | Dokument | Änderungstyp | Beschreibung | Benutzer | Begründung |
|-------|----------|-------------|-------------|---------|-----------|
| 2025-01-15 | Anforderungsregister | Hinzufügen | REG-DP01-32-004 (DSFA-Anforderung) hinzugefügt | Compliance-Analyst | Neue Anforderung aus DSGVO-Leitlinien |
| 2025-01-20 | Zuordnungsmatrix | Ändern | REG-FIN05-23-005 Zuordnung zu CTRL-ORG-TEC-001 von S → P geändert | ISMS-Manager | Betrugserkennungssystem vollständig implementiert |
| 2025-02-01 | Lückenregister | Statusänderung | LÜCKE-2025-003 von Offen → Geschlossen | ISB | Penetrationstest-Programm implementiert |

### Nutzung des Prüfpfads

- **Demonstriert aktives Management**: Zeigt, dass Compliance-Framework nicht statisch "eingestellt und vergessen" ist
- **Unterstützt interne/externe Audits**: Auditoren können Änderungshistorie überprüfen
- **Ermöglicht forensische Überprüfung**: Bei Compliance-Problemen zurückverfolgen, wann und warum Entscheidungen getroffen wurden
- **Regulatorische Verteidigung**: Prüfpfad demonstriert guten Willen; kann Strafen mindern

---

# Umgang mit überlappenden Anforderungen

Mehrere Vorschriften schreiben häufig ähnliche oder identische Sicherheitsmassnahmen vor. Anstatt Implementierungen zu duplizieren, identifiziert [Organisation] Überschneidungen und implementiert nach dem strengsten Standard, um gleichzeitig mehrere Vorschriften zu erfüllen.

## Identifizierung überlappender Anforderungen

### Häufige Überschneidungsszenarien

**Datenschutzvorschriften**:

- DSGVO (EU), CCPA (Kalifornien), FADP (Schweiz), LGPD (Brasilien) verlangen alle:
  - Verschlüsselung personenbezogener Daten
  - Zugangsmassnahmen
  - Verletzungsbenachrichtigung
  - Datensparsamkeit
  - Ähnliche Anforderungen, verschiedene Jurisdiktionen

**Sektorspezifische Vorschriften**:

- Finanzdienstleistungen: Mehrere Regulatoren (BaFin, FINMA, EZB, staatliche Regulatoren) mit überlappenden Cybersicherheitsanforderungen
- Gesundheitswesen: HIPAA, HITECH, staatliche Gesundheitsinformationsgesetze überlappen sich

**Framework-Harmonisierung**:

- Viele Vorschriften referenzieren oder richten sich an ISO 27001, NIST CSF 2.0, CIS Controls
- Implementierung von ISO 27001 erfüllt häufig mehrere regulatorische Anforderungen

### Methoden zur Überschneidungserkennung

**Während der Anforderungsextraktion**:

- Beim Extrahieren aus neuer Vorschrift mit bestehenden Anforderungen im Register vergleichen
- Ähnliche Anforderungen kennzeichnen

**Während der Massnahmenzuordnung**:

- Massnahmenzuordnungsmatrix zeigt Überschneidungen visuell
- A.8.24-Spalte hat primäre Zuordnungen für REG-DP01-32-001, REG-CCPA-15-002, REG-FADP-08-001 → Klare Überschneidung

**Vierteljährliche Überschneidungsanalyse**:

- Anforderungen mit ähnlichem interpretierten Text identifizieren
- Massnahmen identifizieren, die als primäre Massnahmen für 5+ Anforderungen zugeordnet sind

## Identifizierung der strengsten Anforderung

Bei überlappenden Anforderungen MUSS [Organisation] nach dem STRENGSTEN Standard implementieren und damit alle überlappenden Anforderungen erfüllen.

### Warum nach dem strengsten Standard implementieren?

- **Effizienz**: Einmal implementieren, mehrere Anforderungen erfüllen
- **Risikominderung**: Höchster Standard bietet beste Sicherheit; erfüllt alle Vorschriften gleichzeitig
- **Audit-Vereinfachung**: Eine Implementierung zu auditieren, nicht mehrere

### Stringenz-Vergleichsrahmen

**Technische Spezifikationen** (höher/stärker = strenger):

| Anforderung | Technische Spez. | Stringenzvergleich |
|------------|-----------------|-------------------|
| REG-DP01: "Branchenübliche Verschlüsselung verwenden" | Nicht spezifiziert | Weniger streng (vage) |
| REG-FIN05: "AES-128 oder höher verwenden" | AES-128 Minimum | Mittel streng |
| REG-SEC15: "AES-256-Verschlüsselung für ruhende Daten verwenden" | AES-256 erforderlich | **Strengste** |

**Implementierung**: AES-256 verwenden (erfüllt alle drei Anforderungen)

**Prozesskäufigkeiten** (häufiger = strenger):

| Anforderung | Häufigkeit | Stringenzvergleich |
|------------|-----------|-------------------|
| REG-DP01: "Zugriffsrechte periodisch überprüfen" | Nicht spezifiziert | Weniger streng |
| REG-FIN05: "Zugriffsrechte jährlich überprüfen" | Jährlich | Mittel streng |
| REG-PCI: "Zugriffsrechte vierteljährlich überprüfen" | Vierteljährlich | **Strengste** |

**Implementierung**: Vierteljährliche Zugriffsüberprüfungen

**Dokumentationsanforderungen** (umfassender = strenger):

| Anforderung | Dokumentation | Stringenzvergleich |
|------------|--------------|-------------------|
| REG-DP01: "Zugangssteuerungsrichtlinie erstellen" | Nur Richtlinie | Weniger streng |
| REG-FIN05: "Zugangssteuerungsrichtlinie und -verfahren erstellen" | Richtlinie + Verfahren | Mittel streng |
| REG-SEC15: "Richtlinie, Verfahren und technische Standards mit jährlicher Überprüfung" | Richtlinie + Verfahren + Standards + Überprüfung | **Strengste** |

**Fristen und Deadlines** (kürzer = strenger):

| Anforderung | Frist | Stringenzvergleich |
|------------|-------|-------------------|
| REG-DP01: "Betroffene ohne unangemessene Verzögerung benachrichtigen" | Nicht spezifiziert | Weniger streng |
| REG-CCPA: "Betroffene in angemessenem Zeitrahmen benachrichtigen" | Nicht spezifiziert | Weniger streng |
| REG-DSGVO: "Betroffene innerhalb von 72 Stunden benachrichtigen" | 72 Stunden | **Strengste** |

**Implementierung**: 72-Stunden-Benachrichtigungsprozess

### Dokumentation der strengsten Bestimmung

Für jede überlappende Anforderungsmenge:

**Im Anforderungsregister dokumentieren**:

- Im Feld "Anmerkungen" für jede Anforderung in der Überschneidungsmenge:
  - "Überschneidet sich mit [Liste anderer Anforderungs-IDs]"
  - "Strengste Anforderung: [Anforderungs-ID]"
  - "Implementierung folgt dem strengsten Standard"
- Beispiel: REG-DP01-32-001 Anmerkungen: "Überschneidet sich mit REG-FIN05-15-003, REG-SEC15-4.4-002; Strengste: REG-SEC15-4.4-002 (erfordert AES-256); Implementierung nutzt AES-256"

**Überschneidungsregister pflegen** (Optional):

- Felder: Überschneidungsmenge-ID, Anforderungs-IDs in der Überschneidung, strengste Anforderung, Stringenzbegründung, implementierter Standard, gemeinsame Nachweise

## Compliance mit allen anwendbaren Vorschriften nachweisen

### Zuordnungsmatrix zeigt Multi-Vorschrift-Erfüllung

**Interpretation**: A.8.24 (Verwendung von Kryptografie), wenn nach dem REG-SEC15-4.4-002-Standard (AES-256) implementiert, erfüllt VIER regulatorische Anforderungen aus VIER verschiedenen Vorschriften.

**Eine Implementierung**, **ein Nachweissatz**, **vier Vorschriften compliant**.

### Nachweise erfüllen mehrere Anforderungen

**Einzelnes Nachweisdokument, mehrere Verwendungen**:

Beispiel: Verschlüsselungsrichtlinie v2.1

- **Inhalt**: Verlangt AES-256 at rest, TLS 1.3 bei Übertragung, vierteljährliche Schlüsselrotation
- **Massnahme**: Nachweis für A.8.24 (Verwendung von Kryptografie)
- **Erfüllt Anforderungen**:
  - REG-DP01-32-001 (DSGVO Artikel 32 Verschlüsselungsanforderung)
  - REG-FIN05-15-003 (Finanzvorschrift Verschlüsselungsanforderung)
  - REG-HEALTH-12-001 (Gesundheitsdatenverschlüsselungsanforderung)
  - REG-SEC15-4.4-002 (Sicherheitsstandard Verschlüsselungsanforderung)

**Audit-Szenario**:

- **DSGVO-Auditor** fragt: "Wie erfüllen Sie die Verschlüsselungsanforderung aus Artikel 32?" → Verschlüsselungsrichtlinie v2.1, Konfigurationsdokumentation, Schlüsselverwaltungsprotokolle
- **Finanzauditor** fragt: "Wie schützen Sie Finanzdaten?" → DIESELBE Richtlinie v2.1
- **Gesundheitsauditor** fragt: "Wie schützen Sie Gesundheitsakten?" → DIESELBEN Nachweise nochmals
- **Ergebnis**: Eine Richtlinie, drei Audits erfüllt.

### Compliance-Berichterstattung nach Vorschrift

Trotz Nutzung von Überschneidungen kann [Organisation] Compliance-Status nach Vorschrift berichten:

| Vorschrift | Gesamtanforderungen | Erfüllt | Lücken | Compliance % |
|-----------|-------------------|--------|--------|-------------|
| Datenschutzvorschrift (REG-DP01) | 45 | 42 | 3 | 93% |
| Finanzvorschrift (REG-FIN05) | 38 | 38 | 0 | 100% |
| Gesundheitsgesetz (REG-HEALTH) | 22 | 20 | 2 | 91% |
| Sicherheitsstandard (REG-SEC15) | 67 | 63 | 4 | 94% |

**Berichterstattungsflexibilität**:

- Compliance nach Vorschrift berichten (für Regulierungsaudits)
- Compliance nach Massnahme berichten (für ISO 27001-Zertifizierungsaudit)
- Compliance nach Tier berichten (Tier-1- vs. Tier-2-Status)
- Massnahmeneffizienz berichten (Massnahmen, die die meisten Anforderungen erfüllen = hoher ROI)

## Nachweisoptimierung

### Nachweise mit mehreren Anforderungen verknüpfen

**Nachweisregister** enthält Feld: "Erfüllt Anforderungen"

- Mehrfachauswahlfeld, das ALLE von diesen Nachweisen erfüllten Anforderungs-IDs auflistet

**Vor der Erhebung neuer Nachweise**:
1. Prüfen, ob die Anforderung in einer Überschneidungsmenge ist
2. Falls ja, in der Massnahmenzuordnungsmatrix nachsehen, welche Massnahme sie erfüllt
3. Im Nachweisregister nach bestehenden Nachweisen für diese Massnahme suchen
4. Falls bestehende Nachweise die strengste Anforderung erfüllen, erfüllen sie ALLE Anforderungen der Menge
5. Bestehende Nachweise mit neuer Anforderungs-ID markieren
6. KEINE neuen Nachweise erheben

---

# Dokumentensteuerung & verwandte Dokumente

## Dokumentinformationen

**Dokument-ID**: ISMS-POL-A.5.31.3
**Titel**: Anforderungsextraktion & Massnahmenzuordnungsrahmen
**Version**: 1.0
**Gültigkeitsdatum**: [Nach Genehmigung festzulegen]
**Klassifizierung**: INTERN
**Eigentümer**: ISMS-Manager / Compliance-Beauftragter

**Überprüfungsfrequenz**: Jährlich oder bei:

- Erheblichen regulatorischen Änderungen mit Auswirkungen auf mehrere Vorschriften
- Wesentlichen Änderungen des ISO 27001-Standards
- Organisatorischen Änderungen, die den Compliance-Geltungsbereich betreffen
- Methodikverbesserungen, die durch die Nutzung identifiziert wurden

**Nächstes Überprüfungsdatum**: [Gültigkeitsdatum + 12 Monate]

## Verwandte Dokumente

**ISMS-Richtlinienrahmen**:

- **ISMS-POL-A.5.31.1**: Zusammenfassung & Massnahmenausrichtung
  - Bietet Framework-Grundlage und Governance-Struktur
  - Definiert in diesem Dokument referenzierte Rollen
- **ISMS-POL-A.5.31.2**: Methodik zur regulatorischen Anwendbarkeit
  - Bestimmt, WELCHE Vorschriften anwendbar sind (Input für dieses Dokument)
  - Pflegt das ISMS-POL-00-Regulierungsregister
- **ISMS-POL-00**: Regulatorischer Anwendbarkeitsrahmen
  - Masterliste anwendbarer Vorschriften
  - Quelle für Vorschriften, aus denen Anforderungen extrahiert werden
- **ISMS-POL-A.5.31.4**: Change-Management & Nachweisrahmen (nachfolgend)
  - Definiert regulatorische Überwachungs- und Nachweismanagementprozesse

**Implementierungsleitfäden**:

- **ISMS-IMP-A.5.31.3-UG/TG**: Anforderungsextraktionsprozess
  - Schrittweise Betriebsanleitung für die Extraktion von Anforderungen
- **ISMS-IMP-A.5.31.3-UG/TG**: Massnahmenzuordnungsprozess
  - Schrittweise Betriebsanleitung für die Zuordnung von Anforderungen zu Massnahmen

**Bewertungsarbeitsmappen**:

- **Bewertungsarbeitsmappe 3**: Anforderungsextraktionsregister
  - Vorlage für das Anforderungsregister (Abschnitt 2.3)
  - Standardisiertes Format mit Datenvalidierung
- **Bewertungsarbeitsmappe 4**: Massnahmenzuordnungsmatrix
  - Vorlage für die Massnahmenzuordnungsmatrix (Abschnitt 3.3)
  - Vorab ausgefüllt mit 93 Annex A-Massnahmen
  - Bedingte Formatierung für Lückenvisualisierung

**Standards und externe Referenzen**:

- **ISO/IEC 27001:2022**: Informationssicherheitsmanagementsysteme — Anforderungen
  - Annex A: Massnahmenkatalog (93 Massnahmen, die in diesem Dokument referenziert werden)
- **ISO/IEC 27002:2022**: Informationssicherheitsmassnahmen
  - Implementierungshinweise für Annex A-Massnahmen

## Definitionen

**Massnahmenzuordnung**: Prozess der Verknüpfung regulatorischer Anforderungen mit ISO 27001-Massnahmen, die diese Anforderungen erfüllen.

**Lücke**: Regulatorische Anforderung, für die keine Massnahme existiert oder bestehende Massnahmen unzureichend sind.

**Primäre Massnahme (P)**: Massnahme, die eine regulatorische Anforderung direkt und wesentlich erfüllt.

**Anforderungsregister**: Massgebliches Repository aller extrahierten Anforderungen aus anwendbaren Vorschriften.

**Sekundäre Massnahme (S)**: Massnahme, die eine regulatorische Anforderung teilweise erfüllt oder deren Erfüllung unterstützt.

**Unterstützende Massnahme (Su)**: Massnahme, die indirekt zur Erfüllung einer regulatorischen Anforderung beiträgt.

**Rückverfolgbarkeit**: Fähigkeit, vorwärts (Vorschrift → Nachweise) und rückwärts (Nachweise → Vorschrift) durch Anforderungen und Massnahmen zu verfolgen.

---

**ENDE DES DOKUMENTS**

---

*Diese Richtlinie legt die Übersetzungsmethodik von regulatorischen Texten zu umsetzbaren Massnahmen fest und ermöglicht es [Organisation] zu demonstrieren, WIE es regulatorische Anforderungen durch systematische Massnahmenimplementierung erfüllt.*

<!-- QA_VERIFIED: 2026-03-28 -->
