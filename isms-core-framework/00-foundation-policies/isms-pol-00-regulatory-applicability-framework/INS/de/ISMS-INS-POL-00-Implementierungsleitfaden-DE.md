# ISMS-INS-POL-00 — Implementierungsleitfaden
## POL-00: Regulatorischer Anwendbarkeitsrahmen

**Datum:** 2026-02-17
**Zweck:** Praktischer Implementierungsleitfaden für Organisationen, die POL-00 einführen
**Zielgruppe:** ISB, Rechts-/Compliance-Officer, DSB, Implementierungsleitung

---

## 1. Was POL-00 tatsächlich bewirkt (Klartextbeschreibung)

POL-00 beantwortet eine einzige Frage: **Welche Vorschriften gelten für diese Organisation, und mit welcher Verbindlichkeit?**

Ohne POL-00 entscheidet jeder ISMS-Richtlinienautor selbständig, ob er auf GDPR, DORA, FINMA oder NIST verweist. Das Ergebnis ist Inkonsistenz — manche Richtlinien zitieren Vorschriften, die gar nicht gelten, andere übergehen geltende Vorschriften, und Auditoren verbringen Stage 1 damit, das Durcheinander zu entwirren.

POL-00 löst dies, indem es drei Stufen einmalig und zentral festlegt:

- **Stufe 1 (Zwingend)** — gilt unabhängig von der Geschäftstätigkeit. Nicht verhandelbar.
- **Stufe 2 (Bedingt)** — gilt nur, wenn bestimmte geschäftliche Auslöser erfüllt sind. Erfordert eine bewusste Feststellung.
- **Stufe 3 (Informativ)** — nur als Best-Practice-Referenz. Keine Compliance-Pflicht.

Alle 53 Annex-A-Kontrollrichtlinien erben diese Kategorisierung durch Verweis auf POL-00. Die Stufenfeststellung wird einmalig durch Rechts-/Compliance-Abteilung getroffen, und alle Richtlinien nutzen diese Feststellung einheitlich.

**Der operative Nutzen**: Wenn eine neue Vorschrift erscheint, aktualisiert man POL-00 (ein einziges Dokument), und die Änderung propagiert sich logisch auf alle Kontrollrichtlinien. Es müssen nicht 53 Richtlinien einzeln angepasst werden.

---

## 2. Die schwierige Aufgabe: Die Stufenfeststellungen für Stufe 2 treffen

Stufe 1 ist für eine Schweizer Organisation unkompliziert — nDSG und ISO 27001 sind bei angestrebter Zertifizierung und Betrieb in der Schweiz praktisch zwingend. GDPR ist zwingend, wenn personenbezogene Daten von EU-Ansässigen verarbeitet werden (für die meisten Schweizer Organisationen ist die Antwort: ja).

**Stufe 2 ist die eigentliche Arbeit.** Diese Feststellungen erfordern Urteilsvermögen, Rechtskenntnisse und eine ehrliche Beurteilung des Geschäftsmodells der Organisation. Fehler in beide Richtungen haben Konsequenzen:

- **Überanwendung** (Stufe 2 angewendet, obwohl kein Auslöser vorliegt): unnötiger Compliance-Aufwand, Übererfüllung, Kosten ohne Nutzen
- **Unteranwendung** (Auslöser übersehen): regulatorisches Risiko, mögliche Durchsetzungsmaßnahmen, Audit-Abweichung

### Entscheidungs-Checkliste für Stufe 2

Jede Vorschrift der Reihe nach durchgehen. Für jede die Auslöserfrage ehrlich beantworten. Bei Unsicherheit trifft Rechts-/Compliance die Feststellung und dokumentiert die Begründung.

---

#### FINMA (Eidgenössische Finanzmarktaufsicht)

**Auslöserfrage:** Ist die Organisation ein FINMA-beaufsichtigtes Unternehmen?

FINMA-beaufsichtigte Unternehmen umfassen: Banken, Versicherungsgesellschaften, Wertpapierhäuser, Börsen, Fondsleitungen, kollektive Kapitalanlagen, Finanzmarktinfrastrukturen, nach FinSA/FinIA regulierte Zahlungsdienstleister.

| Antwort | Stufe | Massnahme |
|---------|-------|-----------|
| Ja — direkt von FINMA beaufsichtigt | Stufe 2 Aktiv | Anforderungen des FINMA-Rundschreibens 2023/1 anwenden; im SoA dokumentieren |
| Ja — ICT-Dienstleister für FINMA-Unternehmen | Stufe 2 Aktiv | FINMA-Auslagerungsregeln gelten; Anforderungen an Unterauslagerung prüfen |
| Nein | Stufe 2 Nicht Aktiv | „Kein FINMA-beaufsichtigtes Unternehmen" in der Regulatorischen Anwendbarkeitsmatrix dokumentieren |

**Häufiger Fehler:** KMU, die IT-Dienstleistungen für Banken erbringen, gehen davon aus, dass FINMA nicht gilt. Wenn die Bank Ihre Dienstleistung als wesentliche Auslagerung gemäß FINMA-Rundschreiben 2023/1 einordnet, fließen die FINMA-Anforderungen vertraglich durch. Prüfen Sie den Rahmendienstleistungsvertrag.

---

#### DORA (Digital Operational Resilience Act)

**Auslöserfrage:** Ist die Organisation ein Finanzunternehmen oder ICT-Drittdienstleister (ITSP) für EU-Finanzunternehmen?

EU-Finanzunternehmen nach DORA umfassen: Banken, Versicherungsgesellschaften, Wertpapierfirmen, Zahlungsinstitute, E-Geld-Institute, Kryptowertedienstleister und andere. Die ITSP-Bestimmungen von DORA gelten für Anbieter kritischer oder wichtiger ICT-Dienstleistungen für diese Unternehmen.

| Antwort | Stufe | Massnahme |
|---------|-------|-----------|
| EU-Finanzunternehmen | Stufe 2 Aktiv | Volle DORA-Anwendbarkeit einschließlich TLPT-Tests |
| ICT-Dienstleister — als kritisch/wichtig eingestuft | Stufe 2 Aktiv | DORA Kapitel V (Aufsichtsrahmen) gilt |
| ICT-Dienstleister — noch nicht eingestuft | Stufe 2 Beobachtung | Überwachen; prüfen ob vertragliche DORA-Anforderungen durch Kundenverträge fließen |
| Keine Verbindung zu EU-Finanzunternehmen | Stufe 2 Nicht Aktiv | Feststellung dokumentieren; jährlich überprüfen |

**DORA-Geltungsdatum:** 17. Januar 2025. Bei Stufe 2 Aktiv sollten Anforderungen bereits umgesetzt sein oder umgesetzt werden.

**Häufiger Fehler:** Schweizer ICT-Anbieter für EU-Banken gehen davon aus, dass DORA nicht gilt, weil sie nicht EU-ansässig sind. DORAás extraterritoriale Reichweite erfasst Nicht-EU-ICT-Anbieter, die EU-Finanzunternehmen bedienen. Prüfen Sie Ihre Kundenliste.

---

#### NIS2 (Richtlinie zur Netzwerk- und Informationssicherheit 2)

**Auslöserfrage:** Ist die Organisation in einem in NIS2 Anhang I oder II aufgeführten Sektor tätig und erfüllt sie die Größenschwelle?

NIS2 gilt für **wesentliche Einrichtungen** (Anhang I: Energie, Verkehr, Bankwesen, Gesundheit, Wasser, digitale Infrastruktur, öffentliche Verwaltung, Weltraum) und **wichtige Einrichtungen** (Anhang II: Postdienste, Abfallwirtschaft, Ernährung, Fertigung, digitale Anbieter, Forschung).

Größenschwelle: mittlere Unternehmen (50+ Mitarbeitende ODER €10 Mio.+ Jahresumsatz) in erfassten Sektoren. Kleinere Unternehmen nur bei ausdrücklicher Bestimmung durch den Mitgliedstaat.

| Antwort | Stufe | Massnahme |
|---------|-------|-----------|
| Erfasster Sektor + Größenschwelle erfüllt | Stufe 2 Aktiv | NIS2-Cybersicherheitsmaßnahmen (Art. 21) und Meldepflichten (Art. 23) gelten |
| Erfasster Sektor + unter Schwelle | Stufe 2 Beobachtung | Überwachen; Mitgliedstaaten können Geltungsbereich ausweiten |
| Nicht erfasster Sektor | Stufe 2 Nicht Aktiv | Feststellung dokumentieren |

**Für Schweizer Organisationen:** NIS2 ist EU-Recht. Es gilt direkt nur, wenn die Organisation EU-Aktivitäten hat oder Dienstleistungen für EU-Einrichtungen im Geltungsbereich erbringt. Die Schweiz hat eine eigene Revision des ISSG (Informationssicherheitsgesetz) — beide beurteilen.

---

#### PCI DSS v4.0.1

**Auslöserfrage:** Speichert, verarbeitet oder überträgt die Organisation Karteninhaberdaten (Zahlungskartennummern, CVV, PINs)?

Dies ist binär. Es gibt keine Mengenschwelle — jede Organisation, die Kartendaten berührt, ist im Geltungsbereich.

| Antwort | Stufe | Massnahme |
|---------|-------|-----------|
| Ja — jegliche Kartendaten werden verarbeitet | Stufe 2 Aktiv | SAQ-Stufe bestimmen; relevante Anforderungen auf die Karteninhaberdatenumgebung (CDE) anwenden |
| Nein — vollständig an PSP ausgelagert (z. B. Stripe, PayPal), keine Kartendaten berühren eigene Systeme | Stufe 2 Reduziert | Nur SAQ-A-Geltungsbereich; Tokenisierungs-/Redirect-Ansatz verifizieren |
| Keine Kartenverarbeitung | Stufe 2 Nicht Aktiv | Feststellung dokumentieren |

**Häufiger Fehler:** Die Annahme, dass die Nutzung eines Zahlungsabwicklers sämtliche PCI-DSS-Pflichten aufhebt. Wenn Ihre Systeme auf eine gehostete Zahlungsseite weiterleiten und nie Kartendaten sehen, gilt SAQ-A (vereinfacht). Wenn Ihre Systeme Kartendaten während der Übertragung sehen, gilt der volle Geltungsbereich.

---

#### EU AI Act

**Auslöserfrage:** Entwickelt, betreibt oder nutzt die Organisation KI-Systeme innerhalb der EU?

| Antwort | Stufe | Massnahme |
|---------|-------|-----------|
| Entwickelt oder betreibt verbotene KI-Systeme | Nicht erlaubt | Vollständiger Stopp |
| Entwickelt oder betreibt Hochrisiko-KI (Anhang III) | Stufe 2 Aktiv | Konformitätsbewertung, Registrierung, technische Dokumentation erforderlich |
| Betreibt Allzweck-KI in Hochrisiko-Kontext | Stufe 2 Aktiv | Pflichten nach Artikel 50 (Transparenz) und Nutzungsfallbewertung |
| Nutzt KI-Tools (z. B. Microsoft Copilot, ChatGPT) als Betreiber | Stufe 2 Beobachtung | Überwachen; Transparenz- und menschliche Aufsichtspflichten gelten |
| Keine KI-Entwicklung oder -Bereitstellung | Stufe 2 Nicht Aktiv | Dokumentieren; jährlich überprüfen — KI-Einführung verändert sich rasch |

**Zeitplan:** Hochrisiko-KI-Pflichten werden ab August 2025 schrittweise eingeführt. Verbote für KI aktiv seit Februar 2025. Compliance-Daten sind moving targets — den Zeitplan der delegierten Rechtsakte prüfen.

---

#### HIPAA / FISMA / CCPA (US-Bundes-/Landesrecht)

Diese gelten nur, wenn die Organisation:
- Geschützte Gesundheitsdaten von US-Personen verarbeitet (HIPAA)
- Eine US-Bundesbehörde oder ein US-Bundesauftragnehmer ist (FISMA)
- Personenbezogene Daten von California-Ansässigen erhebt und die Umsatz-/Datenmengen-Schwelle erfüllt (CCPA)

Für die meisten Schweizer Organisationen ohne US-Aktivitäten sind diese **Stufe 3 (Informativ)**. Feststellung dokumentieren. Bei geplanter US-Marktexpansion überprüfen.

---

## 3. Ersteinrichtung — Ausfüllen der Regulatorischen Anwendbarkeitsmatrix

Die Regulatorische Anwendbarkeitsmatrix (POL-00 Abschnitt 8.2) ist der formelle Nachweis der Stufenfeststellungen. Vor dem Ausfüllen diese Fragen auf Organisationsebene beantworten:

**Zur Organisation:**
1. In der Schweiz registriert? (nDSG = Stufe 1)
2. Verarbeitet personenbezogene Daten von EU-Ansässigen? (GDPR = Stufe 1 oder Stufe 2, abhängig von Volumen/Art)
3. FINMA-beaufsichtigtes Unternehmen oder wesentlicher IT-Dienstleister für ein solches? (FINMA Stufe 2)
4. Erbringt ICT-Dienstleistungen für EU-Finanzunternehmen? (DORA Stufe 2)
5. Tätig in NIS2 Anhang I/II-Sektor mit 50+ Mitarbeitenden oder €10 Mio.+ Umsatz? (NIS2 Stufe 2)
6. Speichert, verarbeitet oder überträgt Zahlungskartendaten? (PCI DSS Stufe 2)
7. Entwickelt, betreibt oder nutzt KI-Systeme in der EU? (EU AI Act Stufe 2 Beobachtung/Aktiv)
8. US-Gesundheitsdaten, Bundesverträge oder California-Kundenbasis? (HIPAA/FISMA/CCPA Stufe 2 oder 3)

**Reihenfolge:**
1. ISB und Rechts-/Compliance gemeinsam die obige Checkliste durcharbeiten
2. Rechts-/Compliance trifft die Stufenfeststellungen für Stufe 2 und dokumentiert die Begründung
3. DSB validiert datenschutzbezogene Feststellungen (GDPR, nDSG, EU AI Act)
4. Matrix wird mit Stufe + Feststellungsbegründung für jede Vorschrift ausgefüllt
5. Geschäftsleitung genehmigt die ausgefüllte Matrix
6. Matrix wird datiert und unterzeichnet — dies wird zum Audit-Nachweis für Stage 1

**Die Matrix muss nicht perfekt sein.** Sie muss bewusst sein. Ein Auditor akzeptiert eine begründete Feststellung, dass DORA nicht gilt, gestützt auf eine dokumentierte Beurteilung der Kundenbasis. Er akzeptiert nicht: „Wir haben nicht daran gedacht."

---

## 4. Das Quartalsüberwachungsprotokoll (in der Praxis)

POL-00 Abschnitt 4.3 schreibt eine quartalsweise Überwachung des regulatorischen Umfelds vor. Dies ist der Nachweis, dass die Stufenfeststellungen aktuell gehalten werden.

**Was Überwachung tatsächlich bedeutet:**

Es bedeutet nicht, jedes Quartal ein Rechtsteam für regulatorische Recherchen zu beauftragen. Es bedeutet:

1. Eine ausgewählte Menge regulatorischer Überwachungsquellen überprüfen (POL-00 Anhang — Quellen für regulatorische Überwachung)
2. Bestätigen, ob im Quartal wesentliche regulatorische Entwicklungen eingetreten sind
3. Beurteilen, ob Entwicklungen die aktuellen Stufenfeststellungen betreffen
4. Die Überprüfung dokumentieren und unterzeichnen

**Vorlage für einen typischen Quartalsprotokoll-Eintrag (keine Änderungen):**

```
REGULATORISCHES ÜBERWACHUNGSPROTOKOLL — Q[X] [JAHR]
Zeitraum: [TT.MM.JJJJ] bis [TT.MM.JJJJ]

Überprüfte Überwachungsquellen:
☑ EDÖB (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter) — Neuigkeiten und Leitlinien
☑ FINMA — Rundschreiben und Leitlinienaktualisierungen
☑ EUR-Lex / Amtsblatt EU — DORA/NIS2/AI Act Durchführungsrechtsakte
☑ PCI Security Standards Council — DSS-Aktualisierungen
☑ ENISA — NIS2-Implementierungshinweise

Ergebnisse:
Es wurden im Berichtsquartal keine wesentlichen regulatorischen Entwicklungen
identifiziert, die die aktuellen Stufenfeststellungen (Stufe 1/2/3) betreffen.

Ausgelöste Bewertung erforderlich: Nein

Geprüft von: [Name Rechts-/Compliance-Officer]          Datum: [TT.MM.JJJJ]
Bestätigt von: [Name ISB]                               Datum: [TT.MM.JJJJ]
```

**Bei Änderungen:** Die Änderung dokumentieren, beurteilen, welche Stufenfeststellungen oder Kontrollrichtlinien betroffen sind, den 6-Schritte-Änderungsprozess gemäß POL-01 Abschnitt 5.2 auslösen und die ausgelöste Bewertungsreferenz festhalten.

**Das Wichtigste am Protokoll:** Es stets am gleichen Datum des Quartals erstellen. Einen wiederkehrenden Kalendertermin setzen. Ein Protokoll mit gleichmäßigen Datumsangaben (Ende März, Juni, September, Dezember) wirkt bewusst. Ein Protokoll mit unregelmäßigen Datumsangaben wirkt nachträglich erstellt.

---

## 5. Ausgelöste Bewertungen — Wann außerhalb des Quartals neu zu bewerten ist

Die folgenden Geschäftsereignisse sollten eine sofortige Neubewertung außerhalb des Quartalszyklus auslösen (POL-00 Abschnitt 5):

| Ereignis | Was zu bewerten ist |
|----------|---------------------|
| Eintritt in neuen Markt (EU, USA usw.) | Neue regulatorische Pflichten in dieser Jurisdiktion |
| Erwerb oder Zusammenschluss mit einem anderen Unternehmen | Regulatorische Pflichten des Zielunternehmens gehen über |
| Einführung eines neuen Produkts mit personenbezogenen Daten | GDPR/nDSG-Geltungsbereich, EU AI Act bei KI-Funktion |
| Beginn der Verarbeitung von Zahlungskartendaten | PCI DSS-Auslöser |
| Vertragsabschluss mit einem EU-Finanzunternehmen | DORA-ITSP-Bestimmungen |
| Erreichen von 50 Mitarbeitenden oder €10 Mio. Umsatz | NIS2-Größenschwelle überschritten |
| Wesentliche regulatorische Aktualisierung (Durchsetzungsmaßnahme, neue Leitlinie) | Betroffene Stufenfeststellung |

Ausgelöste Bewertungen verwenden dieselbe Bewertungsmethodik wie die Quartalsprüfung, werden aber separat dokumentiert. Das Auslöseereignis, das Bewertungsergebnis und etwaige Initiierung eines POL-01-Änderungsprozesses sind festzuhalten.

---

## 6. Verbindungen zu anderen Dokumenten

**→ POL-01 (ISMS-Governance- und Entscheidungsrahmen)**
POL-00 liefert das *Was* (welche Vorschriften gelten). POL-01 regelt den *Prozess* zur Änderung dieser Feststellung. Wenn ein Quartalsprüfungsprotokoll eine wesentliche regulatorische Änderung identifiziert, wird der 6-Schritte-Änderungsprozess gemäß POL-01 Abschnitt 5.2 ausgelöst. Die beiden Richtlinien funktionieren als Paar.

**→ Erklärung zur Anwendbarkeit (SoA)**
Feststellungen der Stufe 1 und Stufe 2 Aktiv beeinflussen die SoA-Kontrollauswahl direkt. DORA aktiv → Resilienzkontrollen (A.5.29, A.5.30, A.8.13, A.8.14) sind wahrscheinlich zwingend. PCI DSS aktiv → Verschlüsselungs- und Zugriffskontrollen (A.8.24, A.8.2, A.5.15) erhalten zusätzliche Begründung. Das SoA sollte POL-00 als Quelle für die Kontrolleinschlussbegründung referenzieren.

**→ Annex-A-Kontrollrichtlinien**
Kontrollrichtlinien müssen nicht individuell alle geltenden Vorschriften aufzählen. Sie verweisen für den regulatorischen Rahmen auf POL-00 und zitieren spezifische Vorschriften nur dort, wo diese eine spezifische Kontrollanforderung treiben (z. B. GDPR Artikel 32 in der A.8.24-Verschlüsselungsrichtlinie).

**→ ISMS-CHK-POL-00 (falls erstellt)**
Ein Compliance-Bewertungsarbeitsbuch für POL-00 würde GOV-05 bis GOV-08 im ISMS-CHK-POL-01-Arbeitsbuch verifizieren — konkret, dass die Quartalsüberwachung durchgeführt wird, ausgelöste Bewertungen dokumentiert sind und SoA-Begründungen vollständig sind. POL-00 hat derzeit kein eigenes Bewertungsarbeitsbuch; diese Anforderungen werden über ISMS-CHK-POL-01 bewertet.

---

## 7. Nachweise für Auditoren

### Stage 1 (Dokumentationsprüfung)

Der Auditor möchte sehen, dass regulatorische Pflichten explizit identifiziert und kategorisiert sind. Nachweise:

- [X] POL-00 v1.0 — genehmigt, unterzeichnet, datiert
- [X] Regulatorische Anwendbarkeitsmatrix (Abschnitt 8.2) — ausgefüllt mit Stufenfeststellungen und Begründung für jede Vorschrift
- [X] Dokumentation der Stufenfeststellungen für Stufe 2 — schriftliche Begründung für Aktiv/Nicht-Aktiv-Entscheidungen für jede bedingte Vorschrift
- [X] Genehmigungsunterschriften — ISB, Rechts-/Compliance, DSB, Geschäftsleitung

**Was Stage-1-Auditoren bemängeln:** Fehlende oder vage Stufenfeststellungen für Stufe 2 („DORA — in Prüfung"), nicht unterzeichnete Matrizen, Inkonsistenz zwischen POL-00-Stufenfeststellungen und SoA-Kontrollauswahl.

### Stage 2 (Operative Wirksamkeit)

Der Auditor möchte sehen, dass POL-00 tatsächlich gepflegt wird. Nachweise:

- [X] Quartalsüberwachungsprotokolle — mindestens 4 Quartale (oder seit ISMS-Einführung, falls weniger als ein Jahr)
- [X] Jedes Protokoll unterzeichnet von Rechts-/Compliance + ISB
- [X] Mindestens ein Nachweis einer ausgelösten Bewertung (falls ein relevantes Geschäftsereignis eingetreten ist)
- [X] Nachweis, dass das SoA nach jeder Änderung der Stufenfeststellungen aktualisiert wurde

**Was Stage-2-Auditoren bemängeln:** Quartalsberichte, die nach Vorlage ohne echte Prüfung aussehen (identischer Text über alle 4 Quartale ohne Variation), fehlende Unterschriften, keine Reaktion auf bekannte regulatorische Entwicklungen (z. B. DORA-Geltungsdatum verstrichen ohne protokollierten Eintrag).

---

## 8. Implementierungshinweise

### 8.1 Das „Nichts geändert"-Quartal ist in Ordnung — aber Sprache variieren

Vier identische Quartalsprotokolle mit kopiertem Text wirken wie eine Checkbox-Übung. Auditoren bemerken dies. Selbst wenn sich nichts Wesentliches geändert hat: variieren, was überprüft wurde, konkrete geprüfte Leitliniendokumente notieren und Entwicklungen erwähnen, die bewertet und als unwesentlich eingestuft wurden.

### 8.2 GDPR und nDSG überschneiden sich — einmal behandeln, nicht zweimal

Für Schweizer Organisationen, die EU-Personendaten verarbeiten, gelten sowohl GDPR als auch nDSG. Sie haben sich überschneidende, aber nicht identische Anforderungen. Der sicherste Ansatz: Den strengeren Standard für jede spezifische Anforderung implementieren (meist GDPR). Dies in der Regulatorischen Anwendbarkeitsmatrix dokumentieren. Keine zwei getrennten Compliance-Programme schreiben — das erzeugt Inkonsistenz und Verwirrung.

### 8.3 Stufe 2 „Beobachtung" ist ein legitimer Status

Nicht jede Stufe-2-Vorschrift ist binär Aktiv/Nicht-Aktiv. „Beobachtung" (Situation wird überwacht, ohne volle Compliance-Pflichten) ist angemessen bei:
- DORA bei Bedienung von Finanzunternehmen über Intermediäre (unklare Exposition)
- EU AI Act, wo KI-Tools genutzt werden, aber die vollständige Risikoeinstufung noch bewertet wird
- NIS2, wo man nahe, aber nicht klar über der Größenschwelle liegt

Die Beobachtungsbegründung dokumentieren. Einen Überprüfungsauslöser setzen. Beobachtungseinträge nicht unbegrenzt stehen lassen — sie sollten sich innerhalb von 12 Monaten zu Aktiv oder Nicht Aktiv auflösen.

### 8.4 Das regulatorische Umfeld entwickelt sich rasch (2025–2026)

Drei wesentliche Stufe-2-Vorschriften befinden sich in der aktiven Umsetzungsphase:
- **DORA** — ab 17. Januar 2025 in Kraft, Durchsetzung läuft
- **EU AI Act** — verbotene KI ab Februar 2025, Hochrisiko-KI ab August 2025
- **NIS2** — Umsetzungsfrist Oktober 2024, Durchsetzung variiert nach Mitgliedstaat

Das Quartalsüberwachungsprotokoll wird allein durch diese drei Vorschriften für die nächsten 2–3 Jahre wahrscheinlich substanzielle Inhalte haben. Überwachung in diesem Zeitraum nicht als Formalität behandeln.

### 8.5 Die Regulatorische Anwendbarkeitsmatrix ist ein Audit-Anker

Auditoren werden bei Stage 1 erheblich Zeit mit POL-00 verbringen, da es jede andere Richtlinie mit regulatorischen Verweisen untermauert. Eine gut ausgefüllte Matrix — mit expliziten Feststellungen, unterzeichneter Begründung und klaren Stufenzuordnungen — schafft einen starken ersten Eindruck und verhindert detailliertes Nachfragen bei einzelnen Kontrollrichtlinien.

Investieren Sie Zeit in die korrekte Erstellung der Matrix. Das zahlt sich im gesamten Audit aus.

---

## 9. Minimale realisierbare Implementierungssequenz

1. **Die 8 Fragen auf Organisationsebene beantworten** (Abschnitt 3) — ISB + Rechts-/Compliance gemeinsam
2. **Regulatorische Anwendbarkeitsmatrix ausfüllen** — zuerst Stufe 1, dann Stufenfeststellungen für Stufe 2 mit schriftlicher Begründung
3. **DSB validiert Datenschutzfeststellungen** — GDPR-, nDSG-, EU-AI-Act-Abschnitte
4. **Geschäftsleitung genehmigt und unterzeichnet die Matrix**
5. **POL-00 selbst genehmigen und unterzeichnen** — vollständige Genehmigungskette (ISB → Rechts-/Compliance → DSB → Geschäftsleitung)
6. **Erstes Quartalsüberwachungsprotokoll erstellen** — auch ein Quartal vor Stage-1-Audit genügt
7. **SoA abgleichen** — bestätigen, dass Kontrollauswahl Stufenfeststellungen 1/2 Aktiv widerspiegelt
8. **POL-00 Abschnitt 7 aktualisieren** — Text zur POL-01-Änderungsmanagement-Integration einfügen (siehe POL-01 Implementierungsleitfaden)
9. **Quartalsüberwachung planen** — wiederkehrenden Kalendertermin, stets gleiche Daten

Schritte 1–6 sind das Minimum für Stage-1-Audit-Bereitschaft. Schritte 7–9 vervollständigen die Integration.

---

## 10. Dateispeicherorte

| Dokument | Speicherort |
|----------|-------------|
| POL-00 Richtlinie | `POL/ISMS-POL-00 - Regulatory Applicability Framework.md` |
| Dieser Implementierungsleitfaden | `INS/de/ISMS-INS-POL-00-Implementierungsleitfaden-DE.md` |
| POL-01 Implementierungsleitfaden | `../isms-pol-01-.../INS/de/ISMS-INS-POL-01-Implementierungsleitfaden-DE.md` |
| Referenzdokumente für Vorschriften | `isms-ref-dora/`, `isms-ref-eu-ai-act/`, usw. |

---

<!-- ISMS-CORE:INS:ISMS-INS-POL-00-DE:framework:INS:00 -->

<!-- QA_VERIFIED: 2026-03-28 -->
