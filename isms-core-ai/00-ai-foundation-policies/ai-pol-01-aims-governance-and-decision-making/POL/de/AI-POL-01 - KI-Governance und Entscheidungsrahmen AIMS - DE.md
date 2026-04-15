<!-- ISMS-CORE:POLICY:AI-POL-01-DE:ai:POL:01 -->
**AI-POL-01 — KI-Governance und Entscheidungsrahmen AIMS**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumententitel** | KI-Governance und Entscheidungsrahmen AIMS |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | AI-POL-01 |
| **Dokumentersteller** | KI-Governance-Beauftragter (KI-GB) / Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **AIMS-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|-----------|
| 1.0 | [Datum - 4 Wochen] | KI-GB | Erster Entwurf — AIMS-Governance-Grenzen und Entscheidungsrahmen |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen AIMS- oder regulatorischen Änderungen)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: KI-Governance-Beauftragter (oder designierter ISB, sofern keine dedizierte KI-Governance-Funktion besteht)
- Sekundär: Informationssicherheitsbeauftragter (ISB)
- Compliance: Rechts- / Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- AI-POL-00 (Regulatorischer Anwendbarkeitsrahmen für KI — obligatorische Querverknüpfung)
- ISMS-POL-01 (ISMS-Governance und Entscheidungsrahmen — übergeordnetes Governance-Dokument)
- ISO/IEC 42001:2023 Klausel 4.3 (Festlegung des Anwendungsbereichs des AIMS)
- ISO/IEC 42001:2023 Klausel 5.1 (Führung und Verpflichtung)
- ISO/IEC 42001:2023 Klausel 5.2 (KI-Richtlinie)
- ISO/IEC 42001:2023 Klausel 5.3 (Rollen, Verantwortlichkeiten und Befugnisse)
- ISO/IEC 42001:2023 Klausel 9.2 (Internes Audit)
- ISO/IEC 42001:2023 Klausel 9.3 (Managementbewertung)
- ISO/IEC 42001:2023 Klausel 10.2 (Nichtkonformität und Korrekturmassnahme)

**Verteilung**: Alle AIMS-Stakeholder, KI-System-Eigentümer, KI-Risikoverantwortliche, Compliance-Beauftragte, interne/externe Auditoren
**Referenziert von**: Allen AIMS-Richtliniendokumenten, AIMS-Anwendbarkeitserklärung (SoA), KI-Risikobehandlungsplan

---

## Zusammenfassung

Die vorliegende Richtlinie legt fest, **wo fachliches Urteilsvermögen im KI-Managementsystem (AIMS)** der [Organisation] ausgeübt wird, und stellt sicher, dass:

- **AIMS-Designentscheidungen dokumentiert und genehmigt sind** (Kontrollinterpretation, regulatorische Anwendbarkeit, KI-Risikoakzeptanz)
- **Entscheidungsbefugnisse klar zugewiesen sind** (KI-GB, ISB, Recht, Geschäftsleitung — Kompetenz und Geltungsbereich)
- **AIMS-Kriterien durch kontrollierte Prozesse weiterentwickelt werden** (regulatorische Änderungen, neue Standards, Behördenorientierungen, Audit-Feedback)
- **Die Auditverifizierung objektiv und nachweisbasiert ist** (Auditoren verifizieren das dokumentierte Design, ohne Anforderungen neu zu interpretieren)

**Zweck**: Ermöglichung einer **objektiven Auditverifizierung** durch Verlagerung des fachlichen Urteilsvermögens in die **AIMS-Designphase** (dokumentierte Richtlinien, Risikobewertungen, Anwendbarkeitsentscheidungen) statt in die **Auditdiskussionsphase** (subjektive Interpretation während der Zertifizierung).

**Geltungsbereich**: Sämtliche AIMS-Entscheidungsbefugnisse, Bestimmungen zur regulatorischen KI-Anwendbarkeit, Behandlung von Kontrollausnahmen, Weiterentwicklung der KI-Kriterien und Governance-Überprüfungsprozesse.

**Grundprinzip**: **Die ISO/IEC 42001:2023-Zertifizierung erfordert fachliches Urteilsvermögen in zwei Phasen:**

1. **AIMS-Design** (Verantwortung der Organisation): Interpretation von ISO 42001 im organisatorischen Kontext, Bestimmung der Rollen KI-Anbieter/KI-Betreiber, risikobasierte Kontrollauswahl, Definition der Nachweiszulänglichkeit
2. **AIMS-Verifizierung** (Verantwortung des Auditors): Beurteilung, ob die organisatorische Interpretation ISO 42001 erfüllt, Verifizierung, dass die Implementierung der Dokumentation entspricht

Die vorliegende Richtlinie dokumentiert das organisatorische fachliche Urteilsvermögen (Phase 1), um eine objektive Auditverifizierung (Phase 2) zu ermöglichen.

**Beziehung zu ISMS-POL-01**: Die vorliegende Richtlinie ist das KI-spezifische Pendant zu ISMS-POL-01. Wo Governance-Prinzipien überlappen (Entscheidungseskalation, Kompetenzanforderungen, Änderungskontrolle), hat ISMS-POL-01 Vorrang für die Informationssicherheits-Governance. AI-POL-01 etabliert KI-spezifische Governance-Erweiterungen und die eigenständige Befugnis des KI-GB.

---

## Befugnisse und Governance-Grenzen

### Zweck und Geltungsbereich

Die vorliegende Richtlinie definiert die **Entscheidungsbefugnisse** für die AIMS-Governance und stellt sicher, dass:

- Verantwortlichkeiten für die Interpretation der KI-Compliance klar zugewiesen sind
- Dokumentierte Prozesse für Anwendbarkeit, Ausnahmen und Weiterentwicklung bestehen
- Kompetenzanforderungen für KI-Governance-Entscheidungsträger definiert sind
- Objektive Kriterien für die Auditverifizierung vorliegen

**Die vorliegende Richtlinie legt fest:**

- Befugnissgrenzen für AIMS-Entscheidungen (Abschnitt 2: wer was mit welcher Kompetenz entscheidet)
- Befugnisse für regulatorische und Kontrollanwendbarkeit im KI-Bereich (Abschnitt 3: wer bestimmt, was gilt)
- KI-Risikoakzeptanzprozesse (Abschnitt 4: wie KI-Risiken behandelt werden, die nicht gemindert werden können)
- Änderungssteuerung der AIMS-Kriterien (Abschnitt 5: wie sich das AIMS im Laufe der Zeit weiterentwickelt)
- Überwachung der Governance-Effektivität (Abschnitt 6: wie die Governance-Qualität beurteilt wird)

**Die vorliegende Richtlinie legt NICHT fest:**

- Spezifische Implementierungsanforderungen für KI-Kontrollen (geregelt in AI-POL-A.x.x-Kontrollgruppenrichtlinien und IMP-Dokumenten)
- KI-Risikobewertungsmethodik (geregelt im AIMS-Risikobewertungsverfahren)
- Dokumentenkontrollverfahren (geregelt im Dokumentenkontrollverfahren gemäss Klausel 7.5)
- Internes Auditprogramm (geregelt im Internen Auditverfahren gemäss Klausel 9.2)

**Abgrenzungsprinzip**: Die vorliegende Richtlinie etabliert **Entscheidungsbefugnisse und -prozesse**. Die Entscheidungen selbst werden in **AI-POL-00 (regulatorische Anwendbarkeit), AIMS-SoA (Kontrollanwendbarkeit) und KI-Risikoakzeptanzregister (Risikobehandlungsentscheidungen)** dokumentiert.

**Integration mit ISO/IEC 42001:2023**:

- **Klausel 4.2 (Interessierte Parteien)**: Die vorliegende Richtlinie formalisiert die Befugnis zur Interpretation regulatorischer KI-Anforderungen
- **Klausel 4.3 (Geltungsbereich)**: KI-GB und ISB empfehlen gemeinsam den AIMS-Geltungsbereich; die Geschäftsleitung genehmigt
- **Klausel 5.1 (Führung)**: Etabliert den Entscheidungseskalationspfad, der das Engagement der obersten Führungsebene sicherstellt
- **Klausel 5.2 (KI-Richtlinie)**: KI-GB ist Eigentümer der AIMS-Richtliniensuite; ISB ist Miteigentümer, wo KI- und Sicherheitsverpflichtungen überlappen
- **Klausel 5.3 (Rollen)**: Definiert die Befugniszuweisung für alle AIMS-Rollen
- **Klausel 9.3 (Managementbewertung)**: Liefert den Governance-Rahmen für die jährliche AIMS-Überprüfung
- **Klausel 10.1 (Kontinuierliche Verbesserung)**: Ermöglicht die Verbesserung von Governance-Prozessen durch gewonnene Erkenntnisse

---

## Befugnisse und Kompetenz

### Entscheidungsbefugnisse

| Befugnissebene | Rolle | Entscheidungsbereich | Kompetenzanforderung |
|---------------|------|---------------------|---------------------|
| **Primär** | KI-Governance-Beauftragter (KI-GB) | KI-Kontrolldesign, ISO 42001/KI-Verordnungsinterpretation, AISIA-Befugnis, KI-Risikobewertungsprozess, regulatorische Anwendbarkeit (AI-POL-00 Ebenen 1/2), tägliche AIMS-Entscheidungen | ISO 42001-Kenntnisse, KI-Governance-Expertise (ISO 42001 Lead Implementer/Auditor, IAPP AI Governance Certificate oder gleichwertig), 3+ Jahre KI-Governance-/Risikoerfahrung, Unabhängigkeit von KI-Betriebsfunktionen |
| **Sekundär** | Informationssicherheitsbeauftragter (ISB) | Technische KI-Sicherheitsmassnahmen, Sicherheitsarchitektur von KI-Systemen, Anhang-A-Kontrollen mit Sicherheitsdimension (A.6.2.4, A.6.2.6, A.7.4), Integration mit ISMS | Informationssicherheitsexpertise (CISSP/CISM oder gleichwertig), ISO 27001/42001-Kenntnisse |
| **Tertiär** | Rechts- / Compliance-Beauftragter | Rechtliche Interpretation von KI-Verpflichtungen (EU-KI-Verordnung, DSGVO Art. 22), Überprüfung von Auftragsverarbeiter-/Lieferantenverträgen, Behördenengagement, EU-KI-Verordnungskonformitätsbewertung | Rechtsausbildung, KI-Regulierungskenntnisse, Zugang zu externem KI-Rechtsrat |
| **Technisch** | Chief Technology Officer (CTO) / KI-Engineering-Leitung | KI-Systemarchitekturentscheidungen, Lebenszykluskontrollen (A.6.x), Daten-Governance (A.7.x), technische Dokumentation | Tiefe technische KI/ML-Expertise, verantwortungsvolle KI-Engineering-Praktiken |
| **Genehmigung** | Geschäftsleitung (GF/Vorstand) | Strategische KI-Entscheidungen, AIMS-Geltungsbereichsänderungen, Ressourcenzuweisung, KI-Risikoakzeptanz, Entscheidungen zum KI-Systemportfolio | Treuhänderische Verantwortung für KI-Risiken, Verständnis der ISO 42001-Rechenschaftspflichten, Budgetbefugnis |

**Unabhängigkeit des KI-GB**:

Der KI-GB MUSS unabhängig von KI-Entwicklungs- und Einsatzfunktionen tätig sein:

- Berichtet direkt an den GF oder gleichwertige oberste Führungsebene
- Erhält keine Weisungen von KI-Entwicklungsteams oder dem Produktmanagement zu KI-Governance-Festlegungen
- Hat keinen Interessenkonflikt — verfügt über keine Befugnis über KI-System-Designentscheidungen, die die Governance-Objektivität beeinträchtigen könnte
- Hat Zugang zu allen KI-Systemen, Dokumenten und Prozessen, die zur Wahrnehmung der Governance-Aufgaben erforderlich sind

Sofern keine dedizierte KI-GB-Rolle besteht, übernimmt der ISB die primäre Befugnis mit der Massgabe, dass KI-Sicherheits- und KI-Governance-Verantwortlichkeiten unabhängig voneinander wahrgenommen werden.

**Entscheidungseskalationspfad**:

1. **Routineentscheidungen** (KI-Kontrolldesign, Nachweisformat, AIMS-Dokumentation):
   - **Befugnis**: KI-GB
   - **Dokumentation**: AIMS-POL/IMP-Dokumente, AISIA-Nachweise
   - **Überprüfung**: Internes Audit (Klausel 9.2), jährliche Managementbewertung (Klausel 9.3)

2. **Regulatorische Interpretation** (AI-POL-00-Ebenenzuweisungen, EU-KI-Verordnungsklassifikation, FRIA-Anforderungen der KI-Verordnung):
   - **Befugnis**: KI-GB bestimmt die KI-Anwendbarkeit; ISB implementiert technische Massnahmen; Recht prüft rechtliche Dimensionen
   - **Dokumentation**: Regulatorische Anwendbarkeitsmatrix AI-POL-00
   - **Überprüfung**: Vierteljährliches Monitoring, jährliche Gesamtüberprüfung

3. **KI-Risikoakzeptanz** (KI-Kontrollausschluss oder Akzeptanz von KI-Restrisiken):
   - **Befugnis**: KI-GB schlägt vor (mit KI-Risikobewertung); Geschäftsleitung genehmigt
   - **Dokumentation**: KI-Risikoakzeptanzregister
   - **Überprüfung**: Jährliche Managementbewertung (Klausel 9.3)

4. **Strategische Änderungen** (AIMS-Geltungsbereichsänderung, Änderung der KI-Rollenbestimmung, Erweiterung des KI-Systemportfolios in Hochrisikokategorien):
   - **Befugnis**: Genehmigung der Geschäftsleitung (KI-GB + ISB empfehlen; GF/Vorstand entscheidet)
   - **Dokumentation**: Managementbewertungsaufzeichnungen (Klausel 9.3), Vorstandsprotokolle sofern zutreffend
   - **Überprüfung**: Im Rahmen des organisatorischen strategischen Planungszyklus

**Obligatorische Anforderungen**:

1. Der KI-GB **muss** alle KI-Kontrollimplementierungen vor dem Einsatz genehmigen.
2. Der KI-GB **muss** alle regulatorischen Anwendbarkeitsfestlegungen (AI-POL-00-Ebenenzuweisungen) vor der Veröffentlichung oder Aktualisierung genehmigen.
3. Die Geschäftsleitung **muss** alle KI-Risikoakzeptanzentscheidungen gemäss ISO 42001:2023 Klausel 6.1.3 genehmigen.
4. Der KI-GB **muss** bei jeder neuen KI-Systembeschaffung, -entwicklung oder wesentlichen Änderung konsultiert werden — KI-Governance-Auslöser. Im Sinne der vorliegenden Richtlinie ist eine **wesentliche Änderung** jede Änderung an einem KI-System hinsichtlich des bestimmungsgemässen Einsatzes, der Trainingsmethodik, der Datenquellen, des Ausgabetyps, des Betriebskontexts oder des Einsatzumfangs, die bei der ursprünglichen AISIA und Risikobewertung nicht vorhergesehen wurde. Dies entspricht dem Konzept der **wesentlichen Änderung** der EU-KI-Verordnung (Artikel 3(23)): eine Änderung, die die Einhaltung der geltenden Anforderungen beeinträchtigt oder zu einer Änderung des bewerteten bestimmungsgemässen Zwecks führt. Kontinuierliches Lernverhalten, das vom Anbieter zum Zeitpunkt der ersten Konformitätsbewertung vorherbestimmt wurde, stellt keine wesentliche Änderung dar.
5. Die Entscheidungseskalation **muss** dem oben definierten Pfad folgen.

---

## Fachliches Urteilsvermögen bei der ISO 42001:2023-Zertifizierung

### Phase 1: AIMS-Design (Verantwortung der Organisation)

Das von der Organisation ausgeübte fachliche Urteilsvermögen umfasst:

1. **KI-Rollenbestimmung** (Anbieter, Betreiber oder beides je KI-System):
   - Für jedes KI-System identifizieren, ob die Organisation als KI-Anbieter, KI-Betreiber oder beides handelt
   - Die Festlegung je KI-System im KI-System-Inventar dokumentieren
   - Anwendbare Kontrollen rollenbasiert auswählen — einige Kontrollen gelten primär für Anbieter (z. B. A.6.1.x, A.7.x), andere für alle Rollen
   - Dokumentiert in: KI-System-Inventar, AIMS-SoA

2. **AIMS-Geltungsbereichsbestimmung** (Klausel 4.3):
   - Welche KI-Systeme im AIMS-Geltungsbereich liegen
   - Ob das AIMS mit dem ISO 27001 ISMS integriert oder eigenständig betrieben wird
   - Geografische und organisatorische Grenzen
   - Dokumentiert in: AIMS-Geltungsbereichsdokument

3. **Kontrollauswahl und SoA** (Klausel 6.1.3 / Anhang A):
   - Kontrollen basierend auf KI-Risikobewertung und AISIA-Ergebnissen auswählen
   - Anwendbarkeit aller 36 Anhang-A-Kontrollen bestimmen
   - Ausschlüsse begründen — «nicht anwendbar auf unsere Rolle» oder «Risiko trifft nicht zu» sind gültige Ausschlüsse; «noch nicht implementiert» ist keiner
   - Dokumentiert in: AIMS-SoA, KI-Risikobehandlungsplan, AI-POL-A.x.x-Dokumente

4. **Nachweiszulänglichkeit**:
   - Festlegen, welche Nachweise die Kontrollwirksamkeit belegen (AISIA-Nachweise, KI-Risikoregistereinträge, Testberichte, Monitoring-Protokolle)
   - Nachweishäufigkeit und -aufbewahrung bestimmen
   - Dokumentiert in: Kontroll-IMP-Dokumente (Abschnitt Nachweise)

5. **Regulatorische KI-Anwendbarkeit** (AI-POL-00):
   - Bestimmen, welche KI-Gesetze gelten (Ebenen-1/2/3-Rahmen gemäss AI-POL-00)
   - Auslöser für bedingte Regelungen bewerten (ISO 42001-Zertifizierung, EU-KI-Verordnung-Hochrisikoklassifikation)
   - Dokumentiert in: Regulatorische Anwendbarkeitsmatrix AI-POL-00

### Phase 2: AIMS-Verifizierung (Verantwortung des Auditors)

Das vom Auditor ausgeübte fachliche Urteilsvermögen umfasst:

1. **Beurteilung der Prozessqualität**:
   - Ist die KI-Risikobewertungsmethodik fundiert und konsequent angewendet?
   - Sind die KI-Rollenbestimmungen (Anbieter/Betreiber) angesichts des KI-Systemportfolios angemessen?
   - Sind die Entscheidungsträger gemäss der obigen Befugnistabelle kompetent?

2. **ISO 42001:2023-Konformität**:
   - Erfüllt die organisatorische Interpretation der Anhang-A-Kontrollen die Kontrollziele?
   - Ist die AIMS-SoA vollständig und begründet (alle 36 Anhang-A-Kontrollen dokumentiert)?
   - Werden die obligatorischen Klauseln (4–10) behandelt?

3. **Implementierungseffektivität** (Phase 2):
   - Stimmt die tatsächliche Implementierung mit dem dokumentierten Design überein (POL → IMP → Nachweis-Kette)?
   - Sind die Nachweise ausreichend, um den Kontrollbetrieb zu belegen?
   - Werden Nichtkonformitäten und Korrekturmassnahmen gemäss Klausel 10.2 behandelt?

---

## Protokoll zur Anwendbarkeitsanfechtung

**Zweck**: Strukturierter Prozess zur Beilegung von Meinungsverschiedenheiten über KI-Anwendbarkeitsfestlegungen zwischen Organisation und Auditor.

**Wann dieses Protokoll gilt**:

- Auditor stellt die regulatorische KI-Anwendbarkeit in Frage (z. B. «Ist die EU-KI-Verordnung-Hochrisikoklassifikation gerechtfertigt?»)
- Auditor fechtet die KI-Rollenbestimmung für ein spezifisches KI-System an
- Auditor fechtet einen Kontrollausschluss in der AIMS-SoA an
- Auditor ist der Auffassung, dass eine alternative Kontrolle das ISO 42001:2023-Ziel nicht erfüllt

**Protokollschritte**:

**Schritt 1 — Auditor erhebt Bedenken**: Dokumentiert das spezifische Bedenken — welche Festlegung, welche Nachweise widersprechen, welche ISO 42001-Klausel oder welches Kontrollziel möglicherweise nicht erfüllt ist.

**Schritt 2 — Organisation stellt Dokumentation bereit**:

- Bei **regulatorischer Anwendbarkeit**: Bewertung gemäss AI-POL-00-Methodik; Auslöserbewertung; KI-GB + Rechts-Genehmigungsnachweis
- Bei **Rollenbestimmung**: KI-Systembeschreibung; Inventareintrag; KI-GB-Begründung für Anbieter-/Betreiberklassifikation
- Bei **Kontrollausschluss**: KI-Risikobewertung, die zeigt, warum das Risiko nicht zutrifft oder warum die Kontrolle ausserhalb des organisatorischen Geltungsbereichs liegt; SoA-Begründung; organisatorischer Kontext

**Schritt 3 — Gemeinsame Beurteilung**: Organisation und Auditor beurteilen gemeinsam, ob die dokumentierte Begründung die ISO 42001:2023-Anforderungen erfüllt. Die Diskussion ist faktenbasiert.

**Schritt 4 — Lösung**:

| Ergebnis | Massnahme |
|---------|----------|
| Begründung der Organisation akzeptiert | In Audit-Arbeitspapieren dokumentieren; keine Änderung erforderlich |
| Lücke bestätigt | Organisation löst Korrekturmassnahme aus (Klausel 10.2); SoA/AI-POL-00 aktualisieren sofern zutreffend |
| Ungelöster Dissens | An Streitbeilegungsverfahren der Zertifizierungsstelle eskalieren |

---

## AIMS-Geltungsbereichsbestimmung

### Anforderungen an das Geltungsbereichsdokument

Das AIMS-Geltungsbereichsdokument (gemäss ISO 42001:2023 Klausel 4.3) muss festlegen:

- **KI-Systeme im Geltungsbereich**: Benannte KI-Systeme mit Zweck, Typ und Einsatzkontext
- **Explizit ausgeschlossene KI-Systeme**: Mit dokumentierter Begründung
- **Organisatorische Einheiten**: Welche Abteilungen, Funktionen oder juristischen Personen im Geltungsbereich liegen
- **Geografische Grenzen**: Welche Standorte oder Jurisdiktionen eingeschlossen sind
- **Integration mit ISMS**: Ob AIMS und ISMS Prozesse teilen (Managementbewertung, internes Audit, Kontrolle dokumentierter Informationen)

### KI-System-Inventar

Die [Organisation] muss ein KI-System-Inventar als kontrolliertes Dokument führen. Das Inventar muss für jedes KI-System im Geltungsbereich enthalten:

| Feld | Beschreibung |
|------|-------------|
| KI-System-ID | Eindeutige Kennung |
| KI-Systemname | Gebräuchlicher Name und Version |
| KI-System-Eigentümer | Benannte verantwortliche Person |
| KI-Systemzweck | Bestimmungsgemässer Einsatz und Einsatzkontext |
| KI-Rolle | Anbieter / Betreiber / Beides |
| EU-KI-Verordnung Risikoklassifikation | Verboten / Hochrisiko / Begrenztes Risiko / Minimales Risiko / GPAI |
| AISIA-Referenz | Verweis auf abgeschlossenen AISIA-Nachweis |
| Im AIMS-Geltungsbereich | Ja / Nein (mit Begründung bei Nein) |
| SoA-Referenz | Anwendbarkeitserklärungseintrag |

Das KI-System-Inventar ist zu überprüfen:

- Mindestens jährlich bei der Managementbewertung
- Bei Beschaffung oder Entwicklung eines neuen KI-Systems
- Bei wesentlicher Änderung eines bestehenden KI-Systems (neuer Zweck, neue Population, neuer Einsatzkontext)
- Bei Feststellung einer Änderung der EU-KI-Verordnungsklassifikation

---

## AIMS-Anwendbarkeitserklärung (SoA)

Die [Organisation] muss eine Anwendbarkeitserklärung gemäss ISO 42001:2023 Klausel 6.1.3 erstellen und pflegen. Die SoA muss:

- Alle 36 Anhang-A-Kontrollen auflisten
- Für jede Kontrolle: angeben, ob sie anwendbar (Eingeschlossen) oder nicht anwendbar (Ausgeschlossen) ist
- Für eingeschlossene Kontrollen: Implementierungsstatus und Verweis auf AI-POL-A.x.x-Richtlinie dokumentieren
- Für ausgeschlossene Kontrollen: schriftliche Begründung dokumentieren — ein Ausschluss ist nur gültig, wenn die Kontrolle aufgrund der KI-Rolle, des Geltungsbereichs und der Risikobewertung der Organisation tatsächlich nicht zutrifft; «noch nicht implementiert» ist keine gültige Ausschlussbegründung
- Vor dem ersten Einsatz vom KI-GB genehmigt werden
- Jährlich und nach wesentlichen Änderungen am KI-Systemportfolio oder den regulatorischen Anforderungen überprüft werden

---

## AIMS-Änderungssteuerung

**Auslöser für eine kontrollierte AIMS-Aktualisierung**:

- Neue KI-Regelung erlassen oder wesentlich aktualisiert (EU-KI-Verordnung delegierte Rechtsakte, Schweizer KI-Gesetz)
- Neuer ISO-Standard veröffentlicht, der das AIMS betrifft (ISO 42006, ISO 42005-Aktualisierung)
- Wesentliche Änderung des KI-Systemportfolios (neues Hochrisiko-KI-System, Ausserbetriebnahme eines Systems im Geltungsbereich)
- Interner Auditbefund oder Korrekturmassnahme, die den Richtlinienumfang betrifft
- Managementbewertungsentscheidung

**Änderungsprozess**:

1. KI-GB schlägt Änderung mit dokumentierter Begründung vor
2. ISB und Recht prüfen Sicherheits- und rechtliche Dimensionen
3. Geschäftsleitung genehmigt bei strategischer Entscheidung (Geltungsbereichsänderung, Ressourcenzuweisung)
4. Aktualisierte Richtlinie wird gemäss Klausel 7.4 verteilt und kommuniziert
5. Schulungs- oder Sensibilisierungsaktualisierung wird ausgelöst, wenn die Änderung Personalpflichten betrifft

---

## Managementbewertung (Klausel 9.3)

Der KI-GB muss eine jährliche AIMS-Managementbewertung einberufen oder sicherstellen, mit Beteiligung von:

- Geschäftsleitung (Auftraggeber)
- KI-GB (Vorsitz)
- ISB
- Rechts- / Compliance-Beauftragter
- CTO / KI-Engineering-Leitung (sofern KI-Entwicklung im Geltungsbereich)
- KI-System-Eigentümer (für Systeme im Geltungsbereich)

**Obligatorische Tagesordnungspunkte** (gemäss ISO 42001:2023 Klausel 9.3.2):

1. Status der Massnahmen aus der vorangegangenen Managementbewertung
2. Änderungen des externen/internen Kontexts mit Auswirkungen auf das AIMS
3. Änderungen im KI-Regulierungsumfeld (AI-POL-00-Aktualisierungen)
4. Ergebnisse der KI-Risikobewertung und der AISIA
5. AIMS-Leistungskennzahlen (Fortschritt bei KI-Zielen, Vorfallanzahl/MTTR, SoA-Fortschritt)
6. Interne Auditbefunde
7. Nichtkonformitäten und Korrekturmassnahmen
8. Überprüfung der Ressourcenangemessenheit
9. Möglichkeiten zur kontinuierlichen Verbesserung

**Ergebnis der Managementbewertung** (Klausel 9.3.3):

Dokumentierte Entscheidungen und Massnahmen einschliesslich:

- Entscheidungen zur kontinuierlichen Verbesserung
- AIMS-Geltungsbereichsänderungen
- Ressourcenzuweisungsentscheidungen
- KI-Richtlinienaktualisierungen
- Entscheidungen zum KI-Systemportfolio

Managementbewertungsaufzeichnungen sind als dokumentierte Nachweise gemäss Klausel 7.5 aufzubewahren.

---

## Rollen und Verantwortlichkeiten

| Rolle | AIMS-Governance-Verantwortlichkeiten |
|------|--------------------------------------|
| **KI-GB** | Primäre AIMS-Befugnis; SoA-Eigentümer; AI-POL-00-Eigentümer; AISIA-Prozesseigentümer; regulatorisches Monitoring; Vorsitz der Managementbewertung; Ansprechpartner für die Zertifizierungsstelle |
| **ISB** | Sicherheitsdimensionen der KI-Kontrollen; ISMS/AIMS-Integration; Überwachung der technischen Massnahmen; Sicherheitsüberprüfung A.6.2.4/A.6.2.6 |
| **Recht / Compliance** | KI-Regulierungsmonitoring; Koordination der EU-KI-Verordnungskonformitätsbewertung; KI-Klauseln in KI-Lieferantenverträgen; Engagement mit Aufsichtsbehörden |
| **CTO / KI-Engineering-Leitung** | Implementierung der Kontrollen A.6.x und A.7.x; Dokumentation des KI-Systemlebenszyklus; Generierung technischer Nachweise |
| **KI-System-Eigentümer** | KI-System-Inventareinträge; AISIA-Abschluss für eigene Systeme; operative Kontrollen; Vorfall-Meldung |
| **Geschäftsleitung** | KI-Risikoakzeptanz; Ressourcenzuweisung; AIMS-Geltungsbereichsgenehmigung; Beteiligung an der Managementbewertung |
| **Interner Auditor** | Unabhängiges AIMS-Auditprogramm; Berichterstattung über Befunde; Verifizierung der Korrekturmassnahmen |

---

<!-- QA_VERIFIED: 2026-04-15 -->
