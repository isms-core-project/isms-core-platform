<!-- ISMS-CORE:POLICY:AI-POL-A.7.2-6-DE:ai:POL:a.7.2-6 -->
**AI-POL-A.7.2-6 — Daten für KI-Systeme**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumenttitel** | Daten für KI-Systeme |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | AI-POL-A.7.2-6 |
| **Dokumentersteller** | KI-Governance-Beauftragter (KI-GB) / Datenverwaltungsleiter |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum festzulegen] |
| **Version** | 1.0 |
| **Versionsdatum** | [Datum festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |
| **AIMS-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum festzulegen] | KI-GB / Datenverwaltungsleiter | Erstrichtlinie für die ISO/IEC 42001:2023-Erstzertifizierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen der KI-Datenpraktiken oder anwendbarer Datenschutzregelungen)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: KI-Governance-Beauftragter (KI-GB)
- Sekundär: Datenverwaltungsleiter / Chief Data Officer
- Compliance: Recht / Datenschutzbeauftragter (DSB)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- AI-POL-00 (AIMS — Regulatorischer Anwendbarkeitsrahmen für KI)
- AI-POL-A.4.2-6 (KI-Systemressourcen — Dokumentation der Datenressourcen)
- AI-POL-A.6.2 (KI-System-Lebenszyklus — Daten in Entwicklung und Betrieb)
- AI-IMP-A.7.2-6-UG (Daten für KI-Systeme — Benutzerhandbuch)
- AI-IMP-A.7.2-6-TG (Daten für KI-Systeme — Technischer Leitfaden)
- PRIV-POL-00 (Datenschutzrechtliche Anwendbarkeit — für KI-Daten mit personenbezogenen Daten)
- ISO/IEC 42001:2023 Massnahmen A.7.2, A.7.3, A.7.4, A.7.5, A.7.6
- ISO/IEC 42001:2023 Anhang B.7 (Umsetzungshinweise — Daten für KI-Systeme)

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen der [Organisation] für die Datenverwaltung über den gesamten KI-System-Lebenszyklus fest — einschliesslich Datenverwaltungsprozesse, Datenakquisition und -auswahl, Datenqualität, Datenprovenienz und Datenvorbereitung — in Übereinstimmung mit den ISO/IEC 42001:2023-Massnahmen A.7.2 bis A.7.6.

**Anwendungsbereich**: Alle Daten, die bei der Entwicklung, dem Training, der Validierung, dem Testing und dem Betrieb von KI-Systemen im AIMS-Scope verwendet werden.

**Datenschutzhinweis**: Wenn KI-Daten personenbezogene Daten enthalten oder davon abgeleitet sind, gilt diese Richtlinie in Verbindung mit PRIV-POL-00 und der PIMS-Massnahmensuite. DSGVO Artikel 5 (Datensparsamkeit, Zweckbindung für KI-Trainingsdaten mit personenbezogenen Daten) und Artikel 25 (Datenschutz durch Technikgestaltung) gelten zusätzlich zu den Anforderungen dieser Richtlinie.

**Zweck**: Festlegen, WELCHE Datenverwaltungsanforderungen für KI-Systeme gelten, WER verantwortlich ist und WANN Datenverwaltungsprozesse angewendet werden müssen. Die Umsetzung ist in AI-IMP-A.7.2-6-UG und AI-IMP-A.7.2-6-TG beschrieben.

**Begründung der zusammengefassten Massnahmen**: A.7.2 bis A.7.6 bilden den Datenverwaltungsrahmen für KI. Datenverwaltung (A.7.2) legt die übergeordneten Prozessanforderungen fest; Akquisition (A.7.3) regelt, wie Daten in die KI-Pipeline gelangen; Qualität (A.7.4) setzt die Standards, die Daten erfüllen müssen; Provenienz (A.7.5) stellt sicher, dass Herkunft und Rechte der Daten verfolgt werden; Vorbereitung (A.7.6) regelt die Transformation von Rohdaten in modellfertige Form.

---

## Anwendungsbereich und Geltungsbereich

### ISO/IEC 42001:2023-Massnahmen

**Massnahme A.7.2 — Daten für Entwicklung und Verbesserung von KI-Systemen**
Die Organisation muss Datenverwaltungsprozesse im Zusammenhang mit der Entwicklung von KI-Systemen definieren, dokumentieren und umsetzen.

**Massnahme A.7.3 — Datenakquisition**
Die Organisation muss Einzelheiten zur Akquisition und Auswahl der in KI-Systemen verwendeten Daten bestimmen und dokumentieren.

**Massnahme A.7.4 — Datenqualität für KI-Systeme**
Die Organisation muss Anforderungen an die Datenqualität definieren und dokumentieren sowie sicherstellen, dass die zur Entwicklung und zum Betrieb des KI-Systems verwendeten Daten diese Anforderungen erfüllen.

**Massnahme A.7.5 — Datenprovenienz**
Die Organisation muss einen Prozess zur Aufzeichnung der Provenienz der in ihren KI-Systemen verwendeten Daten über die Lebenszyklen der Daten und des KI-Systems hinweg definieren und dokumentieren.

**Massnahme A.7.6 — Datenvorbereitung**
Die Organisation muss ihre Kriterien für die Auswahl von Datenvorbereitungsansätzen und die zu verwendenden Datenvorbereitungsmethoden definieren und dokumentieren.

### Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss AI-POL-00):

- **EU-KI-Verordnung (Verordnung 2024/1689)**: Artikel 10 — Datenverwaltungsanforderungen für Hochrisiko-KI-Trainingsdaten (Qualitätskriterien, Repräsentativität, Freiheit von Fehlern und Verzerrungen, Datenverwaltungspraktiken); Artikel 11 — die technische Dokumentation muss eine Beschreibung der Trainingsdaten enthalten
- **DSGVO**: Artikel 5 (Zweckbindung, Datensparsamkeit für KI-Trainingsdaten mit personenbezogenen Daten); Artikel 25 (Datenschutz durch Technikgestaltung); Artikel 35 (DSFA, wenn KI-Datenverarbeitung ein hohes Risiko darstellt)

**Stufe 2: Bedingt** (gemäss AI-POL-00):

- **ISO/IEC 42001:2023**: Massnahmen A.7.2–A.7.6 — gilt, wenn die AIMS-Zertifizierung im Scope liegt oder vertraglich gefordert ist

---

## Richtlinienaussagen: Datenverwaltungsprozesse (A.7.2)

### Anforderung an den Datenverwaltungsrahmen

Die [Organisation] MUSS Datenverwaltungsprozesse definieren, dokumentieren und umsetzen, die alle bei der Entwicklung und Verbesserung von KI-Systemen verwendeten Daten regeln. Diese Prozesse müssen in den KI-Entwicklungslebenszyklus integriert sein (AI-POL-A.6.2) und den vollständigen Datenlebenszyklus von der Akquisition bis zur Löschung abdecken.

### Governance des KI-Datenlebenszyklus

Datenverwaltungsprozesse müssen jede Phase des Datenlebenszyklus abdecken:

| Phase | Governance-Anforderung |
|-------|------------------------|
| **Akquisition** | Dokumentierte Akquisitionskriterien und Genehmigungsprozess (A.7.3) |
| **Aufnahme** | Versionskontrollierte Aufnahme mit Provenienzaufzeichnung (A.7.5) |
| **Qualitätsbewertung** | Qualitätskriterien vor Verwendung angewendet (A.7.4) |
| **Vorbereitung** | Dokumentierte Vorbereitungsmethodik (A.7.6) |
| **Speicherung** | Zugangskontrollen, Verschlüsselung, Sicherung gemäss ISMS |
| **Verwendung in Training / Validierung / Betrieb** | Versionsverknüpfung — welche Datensatzversion in welcher Modellversion verwendet wurde |
| **Aktualisierung / Nachtraining** | Auslöserkriterien für Datensatzaktualisierungen und Nachtraining |
| **Archivierung** | Was zu behalten ist, wie lange und in welchem Format |
| **Löschung** | Kriterien und Prozess zur sicheren Löschung; Verweis auf PRIV-POL-00 bei personenbezogenen Daten |

---

## Richtlinienaussagen: Datenakquisition und -auswahl (A.7.3)

### Anforderung an die Datenakquisition

Die [Organisation] MUSS die Einzelheiten der Datenakquisition und -auswahl für jedes KI-System bestimmen und dokumentieren. Keine Daten dürfen ohne dokumentierte Akquisitionsgenehmigung in die KI-Entwicklungspipeline gelangen.

### Dokumentation der Datenakquisition

Für jeden für KI-Zwecke akquirierten Datensatz:

| Feld | Erforderlicher Inhalt |
|------|-----------------------|
| Datensatzkennung | Eindeutiger Name und Version |
| Quelle | Herkunft der Daten (internes System, öffentlicher Datensatz, lizenzierter Datensatz, beauftragte Erhebung, Web Scraping, sonstige) |
| Akquisitionsmethode | Wie die Daten erlangt wurden |
| Rechtsgrundlage / Lizenz | Lizenz, unter der Daten verwendet werden; Eigentumsbestätigung; bei personenbezogenen Daten: Rechtsgrundlage gemäss DSGVO |
| Vorgesehener Verwendungszweck | Für welche KI-Systeme und Lebenszyklusphase(n) die Daten bestimmt sind |
| Umfang und Abdeckung | Was die Daten repräsentieren; was sie nicht repräsentieren |
| Akquisitionsdatum | Wann die Daten erlangt wurden |
| Verantwortlicher Genehmiger | Genehmigung des Datenverwaltungsleiters für die Akquisition |

### Verbotene Datenquellen

Folgendes darf NICHT ohne ausdrückliche dokumentierte Genehmigung des KI-GB und der Rechtsabteilung als KI-Training- oder Betriebsdaten verwendet werden:

- Daten, die durch Web Scraping erlangt wurden, wenn die Nutzungsbedingungen der Website eine solche Nutzung untersagen
- Daten mit personenbezogenen Daten ohne dokumentierte Rechtsgrundlage gemäss DSGVO
- Synthetische Daten, bei denen die Generierungsmethode ohne dokumentierte Abhilfemassnahmen systematische Verzerrungen einführt
- Daten, bei denen Rechte des geistigen Eigentums unklar oder umstritten sind
- Daten, deren Provenienz nicht festgestellt werden kann

---

## Richtlinienaussagen: Datenqualität (A.7.4)

### Anforderung an die Datenqualität

Die [Organisation] MUSS Datenqualitätsanforderungen für jedes KI-System definieren und dokumentieren sowie verifizieren, dass Daten diese Anforderungen vor der Verwendung in Training, Validierung oder Betrieb erfüllen.

### Dimensionen der Datenqualität

Qualitätskriterien müssen für jeden Datensatz entlang folgender Dimensionen definiert werden:

| Dimension | Definition | Bewertungsmethode |
|-----------|-----------|-------------------|
| **Vollständigkeit** | Welcher Anteil der erforderlichen Felder oder Datensätze vorhanden ist | Statistische Vollständigkeitsprüfung |
| **Genauigkeit** | Grad, in dem Daten die reale Entität, die sie beschreiben, korrekt darstellen | Stichprobenentnahme und Validierung gegen Ground Truth |
| **Repräsentativität** | Grad, in dem Daten die Deployment-Population über relevante demografische Dimensionen hinweg repräsentieren | Verteilungsanalyse; Bewertung der demografischen Abdeckung |
| **Aktualität** | Daten sind für den Anwendungsfall ausreichend aktuell; temporaler Drift wird bewertet | Temporale Verteilungsanalyse |
| **Konsistenz** | Daten sind über Quellen hinweg und im Zeitverlauf konsistent | Quellübergreifende Validierung; Konsistenzprüfungen |
| **Freiheit von schädlichen Verzerrungen** | Daten enthalten keine systematischen Verzerrungen, die unfaire KI-Ausgaben erzeugen würden | Bias-Analyse über geschützte Merkmale |
| **Labelqualität** (für überwachtes Lernen) | Labels sind korrekt, konsistent und von qualifizierten Annotierern erstellt | Inter-Annotator-Übereinstimmung; Label-Audit |

### Qualitäts-Gate

Jeder Datensatz muss vor der Verwendung anhand seiner definierten Qualitätskriterien bewertet werden. Datensätze, die Mindestqualitätsschwellen nicht erfüllen, müssen:

1. Für die Verwendung abgelehnt werden, ODER
2. Behoben werden (zusätzliche Datenerhebung, Bereinigung, Augmentierung) mit dokumentierter Behebung, ODER
3. Mit dokumentierter Risikoakzeptanz des KI-Risikoverantwortlichen verwendet werden, mit bekannten Qualitätsgrenzen in der Modellkarte vermerkt

Kein Datensatz darf ohne dokumentierte Qualitätsbewertungsergebnisse in einem KI-System verwendet werden.

---

## Richtlinienaussagen: Datenprovenienz (A.7.5)

### Anforderung an die Datenprovenienz

Die [Organisation] MUSS einen Prozess zur Aufzeichnung und Pflege der Provenienz aller in KI-Systemen verwendeten Daten über die Lebenszyklen sowohl der Daten als auch des KI-Systems hinweg definieren und umsetzen.

### Anforderungen an Provenienz-Aufzeichnungen

Für jeden Datensatz muss eine Provenienz-Aufzeichnung gepflegt werden, die Folgendes verfolgt:

| Element | Inhalt |
|---------|--------|
| Datensatzkennung und Version | Eindeutige Referenz |
| Ursprüngliche Quelle | Woher die Daten stammen (mit Verweis auf die Akquisitionsaufzeichnung) |
| Transformationshistorie | Alle angewendeten Bereinigungen, Normalisierungen, Augmentierungen oder sonstige Transformationen — mit Datum und verantwortlicher Partei |
| Abgeleitete Datensätze | Wenn dieser Datensatz von einem anderen abgeleitet wurde, Verweis auf die übergeordnete Provenienz-Aufzeichnung |
| KI-Systeme, die diesen Datensatz verwenden | Welche KI-Systeme (und Modellversionen) diesen Datensatz genutzt haben |
| Aufbewahrungs- und Löschungsprotokoll | Wann Daten archiviert oder gelöscht wurden und unter welcher Befugnis |

### Versionsverknüpfung

Das Provenienzsystem muss Rückverfolgbarkeit ermöglichen: Für jede eingesetzte KI-Modellversion muss es möglich sein, die genaue(n) Datensatzversion(en) zu identifizieren, die für Training und Validierung verwendet wurden. Diese Rückverfolgbarkeit ist erforderlich für:

- Audit- und Zertifizierungsnachweise
- Vorfallsuntersuchung (Feststellung, ob ein Datenproblem zu einem KI-Vorfall beigetragen hat)
- Regulatorische Compliance (Technische Dokumentation EU-KI-Verordnung Artikel 11)
- Compliance mit dem Recht auf Löschung (DSGVO Artikel 17 — Identifizierung, welche Modelle auf Daten trainiert wurden, die Gegenstand einer Löschungsanfrage sind)

### DSGVO Artikel 17 — Recht auf Löschung für KI-Trainingsdaten

Wenn eine betroffene Person einen gültigen Löschungsantrag gemäss DSGVO Artikel 17 stellt, MUSS die [Organisation]:

1. **Den Quelldatensatz für das Training sofort löschen** — die Daten der Person aus allen Trainingsdatensätzen, Validierungssätzen und zugehörigen Datenspeichern ohne unangemessene Verzögerung entfernen.
2. **Das Restrisiko in den Modellgewichten bewerten** — unter Verwendung der Provenienznachverfolgbarkeit alle KI-Modellversionen identifizieren, die auf den Daten trainiert wurden. Eine technische Bewertung dokumentieren, ob die Daten der Person aus trainierten Modellgewichten wiederherstellbar oder zuzuordnen sind. Bei Standard-Neuronalen-Netzwerk-Architekturen ist eine vollständige Löschung aus den Gewichten in der Regel technisch nicht durchführbar; diese Undurchführbarkeit muss dokumentiert werden.
3. **Der betroffenen Person antworten** — die Löschungsanfrage bestätigen, die Löschung der Quelldaten bestätigen und, wenn die vollständige Löschung aus den Modellgewichten technisch nicht durchführbar ist, diese Einschränkung und die Restrisikobewertung gemäss den anwendbaren DSB-Leitlinien dokumentieren.
4. **Nachtraining oder Ausserdienststellung des Modells auslösen** — wenn die Restrisikobewertung eine signifikante Wahrscheinlichkeit der Identifizierbarkeit der Person aus Modellausgaben identifiziert (z. B. das Modell wurde auf einem kleinen Datensatz trainiert, oder die Person ist ein markanter Datenpunkt), muss der KI-System-Eigentümer beurteilen, ob ein Nachtraining oder eine Ausserdienststellung des Modells erforderlich ist. Der DSB soll bei der Bestimmung des Risikoschwellenwerts beraten.
5. **Alle Löschungsaktionen protokollieren** — die Anfrage, die Bestätigung der Quelldatenlöschung, die Modellbewertung und jede Nachtraining-Entscheidung im KI-Datenverwaltungsregister erfassen. Aufzeichnungen für 5 Jahre aufbewahren.

Wenn die [Organisation] Differential-Privacy-Techniken beim Training einsetzt, muss dies in der AISIA dokumentiert und in Löschungsantworten als Risikomitigationsmassnahme referenziert werden.

---

## Richtlinienaussagen: Datenvorbereitung (A.7.6)

### Anforderung an die Datenvorbereitung

Die [Organisation] MUSS Kriterien für die Auswahl von Datenvorbereitungsansätzen und die zu verwendenden Methoden definieren und dokumentieren. Datenvorbereitungsentscheidungen müssen dokumentiert und reproduzierbar sein.

### Governance der Datenvorbereitung

Die Datenvorbereitung — der Prozess der Transformation von Rohdaten in eine für KI-Modelltraining oder -betrieb geeignete Form — muss:

**Dokumentiert sein**: Jede Vorbereitungspipeline muss dokumentiert sein, einschliesslich:
- Angewendete Vorverarbeitungsschritte (Normalisierung, Kodierung, Imputation, Tokenisierung usw.)
- Feature-Engineering-Entscheidungen mit Begründung
- Filterkriterien (ausgeschlossene Datensätze und warum)
- Angewendete Augmentierungsmethoden (und deren Parameter)
- Stichprobenstrategie, wenn Datenvolumen Stichprobenentnahme erfordern

**Versionskontrolliert sein**: Datenvorbereitungsskripte und -pipelines müssen zusammen mit dem Modellcode versionskontrolliert sein, um die Reproduktion des exakt vorbereiteten Datensatzes aus der Rohquelle zu ermöglichen.

**Bias-bewusst sein**: Datenvorbereitungsentscheidungen müssen auf ihr Potenzial zur Einführung oder Verstärkung von Verzerrungen überprüft werden. Schritte, die unterrepräsentierte Gruppen unverhältnismässig beeinflussen könnten (z. B. Unterabtastung, Imputationsstrategien), müssen mit Begründung und Bias-Impact-Bewertung dokumentiert werden.

**Annotator-Governance** (für beschriftete Daten):

- Annotierungsrichtlinien müssen dokumentiert sein
- Qualifikationen der Annotatoren dokumentiert
- Inter-Annotator-Übereinstimmung gemessen und dokumentiert
- Labelqualität unterhalb akzeptabler Schwellenwerte löst Nachbeschriftung aus

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **KI-GB** | Eigentümer der KI-Datenverwaltungsrichtlinie; Genehmigung der Datenakquisition für hochsensitive Datensätze; Überprüfung von Datenqualitätsproblemen, die vom Datenverwaltungsleiter eskaliert werden |
| **Datenverwaltungsleiter** | Eigentümer und täglicher Betrieb der A.7.x-Prozesse; Genehmigung von Standard-Datenakquisitionen; Pflege der Provenienz-Aufzeichnungen; Vorsitz der Datenqualitäts-Gates |
| **DSB / Datenschutzbeauftragter** | Überprüfung von KI-Daten mit personenbezogenen Daten; Sicherstellung der DSGVO-Compliance für Trainingsdaten; Beratung zu Recht-auf-Löschung-Implikationen |
| **Data Scientists / ML-Ingenieure** | Durchführung von Datenqualitätsbewertungen; Dokumentation der Vorbereitungspipelines; Meldung von Qualitätsproblemen an den Datenverwaltungsleiter |
| **KI-System-Eigentümer** | Sicherstellung, dass Datenverwaltungsaufzeichnungen für eigene KI-Systeme aktuell sind |

---

## Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrung |
|----------|--------------|--------------|
| Datenakquisitions-Aufzeichnungen | Akquisitionsdokumentation pro Datensatz mit Rechtsgrundlage und Genehmigung | Nutzungsdauer des Datensatzes + 5 Jahre |
| Datenqualitätsbewertungs-Aufzeichnungen | Qualitätsbewertungsergebnisse pro Datensatz gegen definierte Kriterien | Nutzungsdauer des Datensatzes + 3 Jahre |
| Datenprovenienz-Aufzeichnungen | Transformationshistorie und Versionsverknüpfungs-Aufzeichnungen | Systemdauer + 5 Jahre nach Ausserbetriebnahme |
| Datenvorbereitungsdokumentation | Pipeline-Dokumentation mit Verweis auf versionskontrollierten Code | Systemdauer + 3 Jahre |
| Qualitäts-Gate-Ergebnisse | Aufzeichnungen der Bestanden/Nicht-bestanden-Entscheidungen bei Qualitäts-Gates mit Genehmigung | Systemdauer + 3 Jahre |

---

## Hinweise für Auditoren

Auditoren, die die Konformität mit A.7.2–A.7.6 prüfen, sollten folgendes vorfinden:

- Dokumentierte Datenverwaltungsprozesse, die den vollständigen Datenlebenszyklus abdecken
- Akquisitions-Aufzeichnungen für alle in im Scope befindlichen KI-Systemen verwendeten Datensätze
- Datenqualitätskriterien pro KI-System definiert und Qualitätsbewertungs-Aufzeichnungen, die die Erfüllung der Kriterien bestätigen
- Datenprovenienz-Aufzeichnungen, die Rückverfolgbarkeit vom eingesetzten Modell zum Trainingsdatensatz ermöglichen
- Datenvorbereitungspipelines dokumentiert und versionskontrolliert
- Belege, dass Datenqualitäts-Gates angewendet werden, bevor Datensätze in die Produktion gelangen

---

<!-- QA_VERIFIED: 2026-04-15 -->
