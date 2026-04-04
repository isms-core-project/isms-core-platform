<!-- ISMS-CORE:REF:ISMS-REF-EU-AI-ACT-DE:framework:REF:eu-ai-act -->
**ISMS-REF-EU-AI-ACT — EU-KI-Gesetz Anforderungsreferenz**
**Anforderungen an Risikomanagement und Compliance für KI-Systeme in der EU (Nicht-ISMS-Technische Referenz)**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | EU-KI-Gesetz Anforderungsreferenz |
| **Dokumententyp** | Intern – Technische Referenz (Nicht ISMS) |
| **Dokument-ID** | ISMS-REF-EU-AI-ACT |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | ISB (Technische Referenz – Keine Genehmigung durch die Geschäftsleitung erforderlich) |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB / KI-Governance-Team | Erstversion der technischen Referenz für EU AI Act (Verordnung 2024/1689) |

**Überprüfungszyklus**: Halbjährlich (Umsetzung des AI Act entwickelt sich schnell)
**Nächstes Überprüfungsdatum**: [Datum + 6 Monate]
**Genehmiger**: ISB / Recht/Compliance / Datenschutzbeauftragter (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verteiler**: KI/ML-Entwicklungsteams, Produktmanagement, Rechtsabteilung, ISB, DSB (für Organisationen, die KI-Systeme entwickeln oder einsetzen)

---

⚠️ **WICHTIG – NICHT-ISMS-TECHNISCHES UNTERSTÜTZUNGSDOKUMENT**

Dieses Dokument dient ausschließlich zu Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist NICHT Teil des Informationssicherheitsmanagementsystems (ISMS).
- Dieses Dokument definiert KEINE verbindlichen Anforderungen, es sei denn, [Organisation] entwickelt oder betreibt KI-Systeme, die EU-Bürger betreffen.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs für Nicht-KI-Organisationen.
- Dieses Dokument schreibt die Übernahme von EU-KI-Gesetz-Anforderungen für Organisationen, die der Verordnung nicht unterliegen, NICHT vor.
- Dieses Dokument setzt KEINE ISMS-Richtlinie ausser Kraft oder erweitert diese.

**Anwendbarkeitsbestimmung**:
Anforderungen des EU AI Act gelten NUR, WENN [Organisation]:

- Anbieter ist (KI-Systeme entwickelt oder auf dem EU-Markt platziert)
- Betreiber ist (KI-Systeme unter eigener Verantwortung in der EU nutzt)
- Importeur oder Distributor von KI-Systemen in der EU ist
- KI-Systeme entwickelt/betreibt, deren Ergebnisse Personen in der EU betreffen (extraterritoriale Anwendung)

Für alle anderen Organisationen dient dieses Dokument ausschließlich als:

- Technische Referenz für potenzielle AI-Act-Anforderungen
- Kontext für die Erweiterung in KI-Entwicklung/-Betrieb
- Bewusstsein für die EU-KI-Regulierungslandschaft
- **Dieses Dokument darf nicht als Prüfnachweis verwendet werden, es sei denn, [Organisation] unterliegt dem AI Act**

Die Verwendung dieses Dokuments impliziert keine Anwendbarkeit des AI Act, keine Compliance-Verpflichtungen und keinen Status der KI-System-Entwicklung/-Bereitstellung.

**Kritischer Positionierungshinweis**:
Dieses Dokument enthält absichtlich regulatorische Details, die über das hinausgehen, was für die meisten Organisationen gilt. Sein Zweck ist ausschließlich die Sensibilisierung für Organisationen, die dem EU AI Act möglicherweise unterliegen, wenn sie KI-Systeme entwickeln oder einsetzen, oder die Dienstleistungen für KI-System-Anbieter/Betreiber erbringen. Aus der Anwesenheit, Abwesenheit oder dem Umsetzungsstand einer im Folgenden aufgeführten AI-Act-Anforderung dürfen keine Prüfungsschlüsse gezogen werden, es sei denn, [Organisation] entwickelt oder betreibt ausdrücklich KI-Systeme, die EU-Bürger betreffen.

---

# Dokumentenzweck und Geltungsbereich

## Zweck

Dieses Dokument bietet einen technischen Überblick über die Anforderungen des EU-Gesetzes über künstliche Intelligenz (Verordnung (EU) 2024/1689). Es dient zur Unterstützung von:

- Bewusstsein für AI-Act-Anforderungen für KI-System-Anbieter und -Betreiber
- Verständnis der risikobasierten Klassifizierung (Inakzeptables Risiko, Hohes Risiko, Begrenztes Risiko, Minimales Risiko)
- Kontext für Organisationen, die KI-Entwicklung oder -Einsatz in Betracht ziehen
- Potenzielle zukünftige Anwendbarkeitsbewertung
- Zuordnung von AI-Act-Anforderungen zu ISO 27001:2022-Kontrollen

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Begründet KEINE verbindlichen Anforderungen für Nicht-KI-Organisationen
- Definiert KEINE Compliance-Verpflichtungen von [Organisation] (siehe POL-00 für regulatorische Anwendbarkeit)
- Schafft KEINE Prüfkriterien, es sei denn, [Organisation] entwickelt/betreibt KI-Systeme
- Ersetzt NICHT die Interpretation durch Rechts- oder Compliance-Berater
- Stellt KEINE Rechtsberatung zur Compliance mit dem EU AI Act dar
- Deckt NICHT alle delegierten Rechtsakte und Durchführungsrechtsakte ab (viele noch in Entwicklung)
- Begründet KEINE KI-Entwicklungs- oder Betriebsverfahren

## Beziehung zum ISMS

Dieses Dokument ist eine **nicht bindende technische Referenz**, SOFERN [Organisation] keine KI-Systeme entwickelt oder betreibt, die EU-Bürger betreffen (wie in ISMS-POL-00 Abschnitt 3.X – EU AI Act festgestellt).

**Wenn [Organisation] KI-Systeme entwickelt/betreibt, die EU-Bürger betreffen:**

- AI-Act-Anforderungen werden gemäß POL-00 zu Tier 1 (Pflichtige Compliance)
- Dieses Dokument bietet Implementierungsleitfaden
- ISMS-Kontrollen müssen AI-Act-Compliance unterstützen (Risikomanagement, Datenverwaltung, Protokollierung, menschliche Aufsicht)
- Konformitätsbewertung erforderlich für KI-Systeme mit hohem Risiko

**Wenn [Organisation] KEINE KI-Systeme entwickelt/betreibt:**

- AI Act verbleibt gemäß POL-00 in Tier 3 (Informationsreferenz)
- Dieses Dokument dient nur zur Sensibilisierung
- Es bestehen keine AI-Act-Compliance-Verpflichtungen
- ISMS-Kontrollen folgen ausschließlich ISO 27001:2022

## Inhaltsorganisation

Diese Referenz organisiert AI-Act-Anforderungen nach:

- Risikobasiertem Klassifizierungssystem (Inakzeptables Risiko, Hohes Risiko, Begrenztes Risiko, Minimales Risiko)
- Anbieterpflichten (Entwickler, Hersteller)
- Betreiberpflichten (Nutzer von KI-Systemen)
- Stufenweisem Umsetzungszeitplan (2025–2027)
- Anforderungen für KI-Modelle für allgemeine Zwecke (GPAI)
- Zuordnung zu ISO 27001:2022 und verwandten Standards
- Governance- und organisatorische Anforderungen

---

# EU AI Act – Überblick und Anwendbarkeit

## Was ist der EU AI Act?

**Verordnung (EU) 2024/1689** zur Festlegung harmonisierter Vorschriften für künstliche Intelligenz (Gesetz über künstliche Intelligenz).

**Schlüsseldaten**:

- **Verabschiedung**: 21. Mai 2024 (Europäisches Parlament)
- **Inkrafttreten**: 1. August 2024 (20 Tage nach Veröffentlichung im Amtsblatt)
- **Stufenweise Umsetzung**: 2025–2027 (siehe Abschnitt 2.6)

**Zweck**:

- Festlegung harmonisierter Regeln für KI-Entwicklung und -Einsatz in der EU
- Risikobasierter Regulierungsansatz (proportional zu KI-System-Risiken)
- Schutz von Grundrechten, Gesundheit, Sicherheit und Demokratie
- Förderung vertrauenswürdiger KI-Innovation
- Stärkung der EU-Wettbewerbsposition im KI-Bereich

**Rechtsgrundlage**: EU-Verordnung (gilt unmittelbar in allen Mitgliedstaaten, keine nationale Umsetzung erforderlich)

**Extraterritoriale Anwendung**: Gilt für Anbieter/Betreiber außerhalb der EU, wenn KI-Systeme Personen in der EU betreffen.

## Schlüsseldefinitionen

**KI-System** (Artikel 3(1)):
Ein maschinenbasiertes System, das so konzipiert ist, dass es mit unterschiedlichem Grad an Autonomie arbeitet und nach der Bereitstellung Anpassungsfähigkeit zeigen kann und das für explizite oder implizite Ziele aus den empfangenen Eingaben ableitet, wie Ausgaben wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen erzeugt werden, die physische oder virtuelle Umgebungen beeinflussen können.

**Anbieter** (Artikel 3(3)):
Eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-System oder ein KI-Modell für allgemeine Zwecke entwickelt oder entwickeln lässt und es unter eigenem Namen oder Warenzeichen auf dem Markt platziert oder in Betrieb nimmt, ob gegen Entgelt oder unentgeltlich.

**Betreiber** (Artikel 3(4)):
Eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-System unter ihrer Verantwortung verwendet, es sei denn, das KI-System wird im Rahmen einer persönlichen nicht-beruflichen Tätigkeit verwendet.

**KI-Modell für allgemeine Zwecke (GPAI)** (Artikel 3(44)):
Ein KI-Modell, das mit einer großen Datenmenge unter Verwendung von Self-Supervision in großem Maßstab trainiert wurde, erhebliche Allgemeinheit aufweist und kompetent eine breite Palette unterschiedlicher Aufgaben ausführen kann, unabhängig davon, wie das Modell auf dem Markt platziert wird, und das in eine Vielzahl von nachgelagerten Systemen oder Anwendungen integriert werden kann.

## Anwendungsbereich (Artikel 2)

**Der AI Act gilt für**:

| Akteur | Geografischer Geltungsbereich | Bedingungen |
|--------|-------------------------------|-------------|
| **Anbieter** | Platzierung von KI-Systemen auf EU-Markt ODER Inbetriebnahme in der EU | Unabhängig vom Standort des Anbieters |
| **Anbieter** | Standort in Drittland | Wenn Ausgaben des KI-Systems in der EU genutzt werden |
| **Betreiber** | Standort in der EU | Bei Nutzung von KI-Systemen |
| **Betreiber** | Standort in Drittland | Wenn Ausgaben des KI-Systems in der EU genutzt werden |
| **Importeure und Distributoren** | In der EU | Vertrieb von KI-Systemen |
| **Produkthersteller** | In der EU | Platzierung KI-enthaltender Produkte auf dem Markt |
| **Bevollmächtigte Vertreter** | Nicht-EU-Anbieter | Im Auftrag nicht-EU-ansässiger Anbieter tätig |

**Ausnahmen** (Artikel 2(3)):

- KI-Systeme, die ausschließlich für militärische, Verteidigungs- oder nationale Sicherheitszwecke entwickelt oder verwendet werden
- KI-Systeme, die ausschließlich für Forschungs-, Entwicklungs- oder Prototyping-Aktivitäten vor der Marktplatzierung entwickelt oder verwendet werden
- Persönlicher nicht-beruflicher Gebrauch

## Risikobasierte Klassifizierung

Der AI Act verwendet eine **vierstufige Risikopyramide**:

```
                   ┌──────────────────┐
                   │  INAKZEPTABLES   │
                   │    VERBOTENES    │
                   │      RISIKO      │
                   └──────────────────┘
                        (Artikel 5)

              ┌────────────────────────────┐
              │       HOHES RISIKO         │
              │  (Strenge Anforderungen)   │
              └────────────────────────────┘
                   (Anhang III + Artikel 6)

        ┌────────────────────────────────────────┐
        │         BEGRENZTES RISIKO              │
        │   (Transparenzpflichten)               │
        └────────────────────────────────────────┘
                     (Artikel 50)

   ┌──────────────────────────────────────────────────┐
   │              MINIMALES RISIKO                    │
   │    (Keine Pflichten – Freiwillige Codes)         │
   └──────────────────────────────────────────────────┘
                     (Meiste KI-Systeme)
```

## Bestimmung der KI-System-Risikoklassifizierung

**Schritt 1**: Ist das KI-System verboten? (Artikel 5 – Inakzeptables Risiko)

**Schritt 2**: Gehört das KI-System zu einer Hochrisikokategorie?

- In Anhang III aufgeführt? ODER
- Sicherheitskomponente eines unter EU-Harmonisierungsrecht fallenden Produkts (Anhang I)?

**Schritt 3**: Hat das KI-System Transparenzanforderungen? (Artikel 50 – Begrenztes Risiko)

**Schritt 4**: Wenn keine der oben genannten Bedingungen zutrifft, liegt minimales Risiko vor (keine spezifischen Anforderungen)

## Stufenweiser Umsetzungszeitplan

| Anforderungskategorie | Wirksamkeitsdatum | Status |
|-----------------------|-------------------|--------|
| **Verbotene KI-Praktiken** (Artikel 5) | 2. Februar 2025 | 6 Monate nach Inkrafttreten |
| **KI-Modelle für allgemeine Zwecke** (Kapitel V) | 2. August 2025 | 12 Monate nach Inkrafttreten |
| **KI-Systeme mit hohem Risiko** (Kapitel III, Abschnitt 2) | 2. August 2026 | 24 Monate nach Inkrafttreten |
| **Hochrisiko-KI in regulierten Produkten** | 2. August 2027 | 36 Monate nach Inkrafttreten |
| **KI-Büro, Governance-Struktur** | Sofort | August 2024 |

**Übergangsfrist für bestehende Systeme**:
KI-Systeme, die vor dem 2. August 2026 bereits auf dem Markt platziert oder in Betrieb genommen wurden, dürfen bis zum 2. August 2030 ohne Compliance weiter genutzt werden (sofern keine wesentlichen Änderungen vorgenommen werden).

---

# Verbotene KI-Praktiken (Artikel 5) – VERBOTEN

## Überblick

Bestimmte KI-Praktiken sind aufgrund inakzeptabler Risiken für Grundrechte, Sicherheit oder Demokratie **verboten**.

**Wirksamkeitsdatum**: 2. Februar 2025

**Strafe bei Verstoss**: Bis zu 35 Millionen Euro oder 7 % des weltweiten Jahresumsatzes (je nachdem, welcher Betrag höher ist)

## Verbotene Praktiken

**Artikel 5(1)(a): Unterschwellige Manipulation**

- KI-Systeme, die unterschwellige Techniken jenseits des Bewusstseins einer Person einsetzen
- Zweck: Wesentliche Verzerrung des Verhaltens in einer Weise, die erheblichen Schaden verursacht oder verursachen kann
- Beispiele: Versteckte Botschaften, unterschwellige Werbung für gefährdete Bevölkerungsgruppen

**Artikel 5(1)(b): Ausnutzung von Schwachstellen**

- KI-Systeme, die Schwachstellen bestimmter Gruppen ausnutzen (Alter, Behinderung, soziale/wirtschaftliche Situation)
- Zweck: Wesentliche Verzerrung des Verhaltens mit erheblichem Schaden
- Beispiele: Räuberisches Targeting von Kindern, älteren Menschen oder wirtschaftlich Benachteiligten

**Artikel 5(1)(c): Social Scoring**

- KI-Systeme zur Bewertung oder Klassifizierung natürlicher Personen auf Basis ihres sozialen Verhaltens oder persönlicher/Persönlichkeitsmerkmale
- Ergebnisse: Nachteilige oder ungünstige Behandlung in Kontexten, die nichts mit der ursprünglichen Datenerhebung zu tun haben, ODER ungerechtfertigt/unverhältnismäßig zum sozialen Verhalten
- Beispiele: Staatliche Sozialbewertungssysteme, weitreichendes Arbeitgeber-Social-Scoring

**Artikel 5(1)(d): Bewertung des Straftatenrisikos**

- KI-Systeme zur Bewertung oder Vorhersage des Risikos, dass eine natürliche Person eine Straftat begeht
- Ausschließlich auf Grundlage von Profiling oder Persönlichkeitsmerkmalen
- Ausnahme: Auf Basis objektiver, überprüfbarer Fakten, die direkt mit der kriminellen Aktivität zusammenhängen
- Beispiele: Predictive Policing ausschließlich auf Basis von Demografie

**Artikel 5(1)(e): Scraping für Gesichtserkennung**

- Ungezielte Extraktion von Gesichtsbildern aus dem Internet oder CCTV
- Zweck: Erstellung oder Erweiterung von Gesichtserkennungsdatenbanken
- Beispiele: Massen-Scraping von Social-Media-Fotos

**Artikel 5(1)(f): Emotionserkennung am Arbeitsplatz/in der Bildung**

- KI-Systeme zur Ableitung von Emotionen am Arbeitsplatz oder in Bildungseinrichtungen
- Ausnahme: Medizinische oder sicherheitsrelevante Gründe
- Beispiele: Überwachung der Mitarbeiterproduktivität durch Emotionserkennung (verboten, sofern nicht sicherheits-/medizinisch)

**Artikel 5(1)(g): Biometrische Kategorisierung**

- KI-Systeme zur biometrischen Kategorisierung, die sensible Attribute ableiten
- Sensible Attribute: Rasse, politische Ansichten, Gewerkschaftsmitgliedschaft, religiöse/philosophische Überzeugungen, Sexualleben, sexuelle Orientierung
- Ausnahme: Kennzeichnung/Filterung rechtmäßig erworbener biometrischer Datensätze (Strafverfolgungsdatenbanken)

**Artikel 5(1)(h): Echtzeit-Fernen-Biometrische Identifikation (RBI) im öffentlichen Raum**

- Verwendung von Echtzeit-RBI-Systemen in öffentlich zugänglichen Räumen zur Strafverfolgung
- Ausnahmen (Artikel 5(2)): Streng notwendige und verhältnismäßige Verwendungen:
  - Gezielte Suche nach vermissten Personen, Entführungsopfern
  - Prävention einer spezifischen, erheblichen, unmittelbaren Bedrohung (Terroranschlag)
  - Lokalisierung/Identifizierung einer Person, die einer schweren Straftat verdächtig ist (definiert in Anhang II)
- Erfordert vorherige richterliche oder unabhängige Verwaltungsgenehmigung (außer im Notfall)

**Zuordnung zu ISO 27001:2022**:

- Artikel-5-Verbote beziehen sich auf Organisationsrichtlinien und ethische KI-Nutzung
- Keine direkte ISO-27001-Kontrolle, aber informiert durch:
  - A.5.1: Richtlinien für Informationssicherheit (ethische Nutzungsrichtlinien)
  - A.5.31: Gesetzliche, regulatorische und vertragliche Anforderungen
  - Klausel 4.1: Verständnis der Organisation und ihres Kontexts (gesellschaftliche Erwartungen)

## Compliance-Anforderungen

**Für alle Organisationen**:
1. **KI-Systeme inventarisieren**: Alle in Entwicklung oder im Betrieb befindlichen KI-Systeme identifizieren
2. **Artikel-5-Bewertung**: Beurteilung, ob KI-Systeme unter verbotene Praktiken fallen
3. **Sofortige Einstellung**: Entwicklung/Betrieb verbotener KI-Systeme bis 2. Februar 2025 einstellen
4. **Dokumentation**: Bewertung und Entscheidungen dokumentieren
5. **Schulung**: Sicherstellen, dass Entwicklungs-/Beschaffungsteams über Artikel-5-Verbote informiert sind

---

# KI-Systeme mit hohem Risiko (Kapitel III, Abschnitt 2)

## Überblick

KI-Systeme mit hohem Risiko unterliegen aufgrund potenzieller erheblicher Risiken für Gesundheit, Sicherheit oder Grundrechte **strengen Anforderungen**.

**Wirksamkeitsdatum**: 2. August 2026 (24 Monate nach Inkrafttreten)

**Strafe bei Nichtkonformität**: Bis zu 15 Millionen Euro oder 3 % des weltweiten Jahresumsatzes (je nachdem, welcher Betrag höher ist)

## Kategorien von KI-Systemen mit hohem Risiko

**Hochrisiko-Anwendungsfälle gemäß Anhang III**:

| Kategorie | Anwendungsfälle | Beispiele |
|-----------|-----------------|-----------|
| **1. Biometrische Identifizierung und Kategorisierung** | Fernbiometrische Identifizierung, biometrische Kategorisierung (Ausnahme sensible Attribute), Emotionserkennung | Gesichtserkennung bei Zutrittskontrolle, biometrische Kategorisierungssysteme |
| **2. Kritische Infrastruktur** | Verwaltung und Betrieb kritischer digitaler Infrastruktur, Straßenverkehr, Wasser, Gas, Heizung, Stromversorgung | KI-gesteuertes Verkehrsmanagement, Stromnetzoptimierung |
| **3. Bildung und Berufsausbildung** | Festlegung von Zugang/Zulassung, Beurteilung von Schülern, Erkennung von Prüfungsbetrug | Automatisierte Universitätszulassungen, KI-gestützte Prüfungsaufsicht |
| **4. Beschäftigung** | Einstellung, Screening, Bewertungs-/Beförderungsentscheidungen, Aufgabenzuweisung, Überwachung/Bewertung der Arbeitsleistung, Kündigung | KI-gestützte Lebenslauf-Screening, Leistungsbewertungssysteme |
| **5. Wesentliche private/öffentliche Dienstleistungen** | Kredit-Scoring, Beurteilung der Berechtigung für öffentliche Unterstützung, Priorisierung von Notfalleinsätzen | Kreditentscheidungsalgorithmen, KI zur Leistungsanspruchsberechtigung |
| **6. Strafverfolgung** | Individuelle Risikobewertung (Opfer, Täter, Rückfälle), Polygraphen, Emotionserkennung, Erkennung von Deepfakes, Bewertung der Glaubwürdigkeit von Beweisen | Rückfallprognosen, KI-gestützte Vernehmung |
| **7. Migration, Asyl, Grenzkontrolle** | Prüfung von Anträgen, Erkennung gefälschter Dokumente, Bewertung von Sicherheits-/Gesundheitsrisiken, Polygraph/Lügendetektor | Automatisierte Visumsprüfung, Dokumentenverifizierungs-KI |
| **8. Rechtspflege/demokratische Prozesse** | Unterstützung von Justizbehörden bei Rechtsrecherche/Interpretation, KI-Beeinflussung von Wahlergebnissen | Rechtsrecherche-KI, Wahlprognose-Systeme |

**Artikel 6(1)**: KI-Systeme, die Sicherheitskomponenten von Produkten sind, die unter EU-Harmonisierungsrecht (Anhang I) fallen, sofern diese Produkte einer Konformitätsbewertung durch Dritte unterzogen werden.

**Beispiele aus Anhang I**:

- Medizinprodukte (Verordnung 2017/745, 2017/746)
- Maschinen (Verordnung 2023/1230)
- Spielzeug (Richtlinie 2009/48/EG)
- Funkanlagen (Richtlinie 2014/53/EU)
- Zivilluftfahrt (Verordnungen 2018/1139, 2019/945)

## Anbieterpflichten für KI-Systeme mit hohem Risiko

**Artikel 9: Risikomanagementsystem**

Anforderungen:

- Risikomanagementsystem einrichten, umsetzen, dokumentieren und aufrechterhalten
- Kontinuierlicher iterativer Prozess über den gesamten KI-System-Lebenszyklus
- Regelmäßige systematische Aktualisierungen

**Risikomanagementprozess**:
1. **Identifizierung und Analyse** bekannter und vernünftigerweise vorhersehbarer Risiken
2. **Schätzung und Bewertung** von Risiken bei bestimmungsgemäßem Gebrauch und vernünftigerweise vorhersehbarem Missbrauch
3. **Bewertung anderer Risiken** auf Basis von Post-Market-Monitoring-Daten
4. **Einführung geeigneter Risikomanagementmaßnahmen** (Artikel 9(4))

**Risikomanagementmaßnahmen** (Artikel 9(4)):

- Beseitigung oder Reduzierung von Risiken (sicherheitstechnische Schutzmaßnahmen durch Design)
- Angemessene Minderungs- und Kontrollmaßnahmen (Schutzmaßnahmen durch Einsatz)
- Informationen an Betreiber (Gebrauchsanweisungen, Warnhinweise)
- Angemessene Schulungen für Betreiber

**Zuordnung zu ISO 27001:2022**:

- Klausel 6.1.2: Informationssicherheits-Risikobewertung
- Klausel 6.1.3: Informationssicherheits-Risikobehandlung
- A.5.7: Bedrohungsintelligenz
- ISO/IEC 23894:2023: Informationstechnologie – Künstliche Intelligenz – Risikomanagement

---

**Artikel 10: Daten und Datenverwaltung**

Anforderungen:

- Trainings-, Validierungs- und Testdatensätze erfüllen **Qualitätskriterien**
- Unterliegen **Data-Governance**- und Managementpraktiken

**Datenqualitätskriterien** (Artikel 10(3)):

- **Relevant, hinreichend repräsentativ und fehlerfrei**
- **Vollständig** für den beabsichtigten Zweck
- **Geeignete statistische Eigenschaften** (z. B. Balance, Abdeckung)
- Merkmale/Elemente des spezifischen geografischen, kontextuellen, funktionalen Settings berücksichtigen
- Design-Entscheidungen, Datenerhebungsvereinbarungen, Datenaufbereitungsoperationen dokumentieren

**Data-Governance-Praktiken** (Artikel 10(2)):

- Relevante Design-Entscheidungen
- Datenerhebungsprozesse
- Datenaufbereitungsoperationen (Annotation, Kennzeichnung, Bereinigung, Anreicherung, Aggregation)
- Annahmen, insbesondere zur Vollständigkeit der Informationen
- Bewertung von Datenverzerrungen und geeignete Abhilfemaßnahmen
- Identifizierung von Datenlücken oder Mängeln, die den beabsichtigten Gebrauch beeinträchtigen

**Besondere Datenkategorien** (Artikel 10(5)):
Wenn KI-System sensible personenbezogene Datenkategorien (Artikel 9 DSGVO: rassische/ethnische Herkunft, politische Meinungen, religiöse Überzeugungen, biometrische Daten, Gesundheitsdaten, Sexualleben/Orientierung) verarbeitet:

- Geeignete Maßnahmen zur Erkennung, Verhinderung und Reduzierung von Verzerrungen
- Schulungen zu Grundrechten und Nichtdiskriminierung

**Zuordnung zu ISO 27001:2022**:

- A.5.12: Klassifizierung von Informationen
- A.5.13: Kennzeichnung von Informationen
- A.5.14: Informationsübertragung (Datensatz-Sharing)
- A.8.11: Datenmaskierung
- DSGVO Artikel 5(1)(d): Grundsatz der Datenrichtigkeit

---

**Artikel 11: Technische Dokumentation**

Anforderungen:

- Technische Dokumentation **vor der Marktplatzierung** erstellen
- Technische Dokumentation **aktuell halten**
- Nationalen zuständigen Behörden auf Anfrage zur Verfügung stellen

**Inhalt der technischen Dokumentation** (Anhang IV):
1. Allgemeine Beschreibung des KI-Systems (beabsichtigter Zweck, Entwickler, Versionen, Marktplatzierungsdaten)
2. Detaillierte Beschreibung der Systemelemente und des Entwicklungsprozesses
3. Detaillierte Informationen zu Überwachung, Funktionsweise und Steuerung
4. Beschreibung des Risikomanagementsystems (Artikel 9)
5. Beschreibung der während des Lebenszyklus vorgenommenen Änderungen
6. Konformitätsnachweis mit Hochrisiko-Anforderungen
7. Detaillierte Beschreibung des Konformitätsbewertungsverfahrens
8. Kopie der EU-Konformitätserklärung
9. Detaillierte Beschreibung des Post-Market-Monitoring-Systems

**Zuordnung zu ISO 27001:2022**:

- A.5.37: Dokumentierte Betriebsverfahren
- Klausel 7.5: Dokumentierte Informationen (ISMS-Dokumentationsanforderungen)

---

**Artikel 12: Aufzeichnung (Protokollierung)**

Anforderungen:

- Automatisch generierte Protokolle über die gesamte Lebensdauer des KI-Systems
- Ermöglicht **Nachverfolgbarkeit** der Systemfunktionsweise
- Dem beabsichtigten Zweck und dem Risikoniveau angemessen

**Protokollierungsanforderungen** (Artikel 12(2)):

- **Protokollierungsdauer**: Dem Systemrisiko angemessen
- **Zeitstempel**: Datum und Uhrzeit jedes Ereignisses
- **Eingabedaten**: Datenbank/Datei, die eine Aktion auslöst
- **Betroffene natürliche Personen**: Identifizierung, soweit technisch möglich

**Zweck**: Überwachung, Untersuchung, Post-Market-Monitoring und Rechenschaftspflicht ermöglichen.

**Zuordnung zu ISO 27001:2022**:

- A.8.15: Protokollierung
- A.8.16: Überwachungsaktivitäten
- ISO/IEC 27018:2019: Schutz personenbezogener Daten in der öffentlichen Cloud (Protokollierungsanforderungen)

---

**Artikel 13: Transparenz und Informationen für Betreiber**

Anforderungen:

- KI-System so gestalten, dass **Transparenz** ermöglicht wird, damit Betreiber:
  - Systemausgaben interpretieren können
  - System angemessen nutzen können

**Gebrauchsanweisungen** (Anhang IV, Abschnitt 2):

- Identität und Kontaktdaten des Anbieters
- Merkmale, Fähigkeiten und Leistungsgrenzen
- Änderungen am KI-System und der Leistung
- Maßnahmen zur menschlichen Aufsicht
- Benötigte Rechen- und Hardware-Ressourcen
- Erwartete Lebensdauer und Wartungsanforderungen

**Zuordnung zu ISO 27001:2022**:

- A.5.37: Dokumentierte Betriebsverfahren (Benutzerdokumentation)

---

**Artikel 14: Menschliche Aufsicht**

Anforderungen:

- KI-System so gestalten, dass **effektive Aufsicht durch natürliche Personen** ermöglicht wird
- Risiken für Gesundheit, Sicherheit, Grundrechte verhindern oder minimieren

**Maßnahmen zur menschlichen Aufsicht** (Artikel 14(4)):

- **Verstehen** der Fähigkeiten und Grenzen des KI-Systems
- **Bewusstsein** für die Tendenz zur Automatisierungsverzerrung
- Systemausgaben korrekt **interpretieren**
- **Entscheidung gegen Nutzung** oder Überstimmen der Ausgabe
- System **eingreifen oder unterbrechen** (Stoppknopf)

**Aufsichtszuständige** (Artikel 14(5)):

- Natürliche Personen, denen Aufsicht übertragen wird, müssen:
  - Notwendige Kompetenz, Schulung und Befugnis haben
  - Ausreichendes Verständnis des KI-Systems mit hohem Risiko besitzen

**Zuordnung zu ISO 27001:2022**:

- A.5.37: Dokumentierte Betriebsverfahren (Verfahren zur menschlichen Aufsicht)
- A.6.3: Bewusstsein, Schulung und Ausbildung zur Informationssicherheit (Aufsichtsschulung)

---

**Artikel 15: Genauigkeit, Robustheit, Cybersicherheit**

Anforderungen:

- **Genauigkeit**: Angemessenes Genauigkeitsniveau über den gesamten Lebenszyklus
- **Robustheit**: Technische und Cybersicherheitsmaßnahmen proportional zu den Risiken
- **Widerstandsfähigkeit**: Gegen Versuche, Nutzung/Leistung durch Dritte zu verändern

**Robustheitsmaßnahmen**:

- Technische Lösungen gegen gegnerische Angriffe
- Modell-Vergiftungsangriffe
- Daten-Vergiftungsangriffe
- Datenschutzangriffe (Modellinversion, Mitgliedschaftsdeduktion)
- Vertraulichkeitsangriffe

**Zuordnung zu ISO 27001:2022**:

- A.8.7: Schutz vor Schadsoftware
- A.8.8: Management technischer Schwachstellen
- A.8.16: Überwachungsaktivitäten (Anomalieerkennung)
- A.8.24: Verwendung von Kryptografie (Modellschutz)
- ISO/IEC 24029-1: Künstliche Intelligenz – Bewertung der Robustheit neuronaler Netze

---

**Artikel 16: Qualitätsmanagementsystem**

Anforderungen:

- Qualitätsmanagementsystem einrichten, das sicherstellt:
  - Compliance mit dem AI Act
  - Umsetzung der Artikel 9–15
  - Post-Market-Monitoring (Artikel 72)

**Inhalt des Qualitätsmanagementsystems**:

- Strategie zur regulatorischen Compliance (Richtlinien, Verfahren)
- Techniken, Verfahren, systematische Maßnahmen (Design, Designkontrolle, Verifizierung, Validierung, Tests)
- Prüf-, Test- und Validierungsverfahren vor, während und nach der Entwicklung
- Technische Spezifikationen (Qualitätsstandards, Codierungsrichtlinien)
- Systeme und Verfahren für das Datenmanagement
- Risikomanagementsystem
- Post-Market-Monitoring-System
- Meldung schwerwiegender Vorfälle und Fehlfunktionen
- Kommunikation mit Behörden, Betreibern
- Systeme und Verfahren zur Aufzeichnungsverwaltung
- Ressourcenmanagement (Fähigkeiten, Schulungspläne)
- Verantwortungsrahmen (Rollen und Verantwortlichkeiten)

**Zuordnung zu ISO 27001:2022**:

- Gesamter Klausel-4–10-ISMS-Rahmen
- ISO 9001:2015 Qualitätsmanagementsystem (ergänzender Standard)

---

**Artikel 43–51: Konformitätsbewertung**

**Vor der Marktplatzierung** eines KI-Systems mit hohem Risiko muss der Anbieter eine Konformitätsbewertung durchführen.

**Optionen der Konformitätsbewertung**:

**Option 1: Interne Kontrolle** (Artikel 43 + Anhang VI):

- Eigene Bewertung des Anbieters (Selbstbewertung)
- Gilt für die meisten Hochrisiko-Systeme gemäß Anhang III

**Option 2: Bewertung durch benannte Stelle** (Artikel 43 + Anhang VII):

- Bewertung durch Dritte (benannte Stelle)
- Erforderlich für:
  - Biometrische Identifizierung/Kategorisierung (Anhang III(1))
  - Bestimmte kritische Infrastruktur (wenn nicht selbst zertifiziert)

**Konformitätsbewertungsprozess** (Anhang VI):
1. Technische Dokumentation erstellt (Artikel 11, Anhang IV)
2. Qualitätsmanagementsystem umgesetzt (Artikel 16)
3. Risikomanagementsystem umgesetzt (Artikel 9)
4. Selbstbewertung oder Drittpartei-Bewertung
5. EU-Konformitätserklärung erstellt (Anhang V)
6. CE-Kennzeichnung angebracht (Artikel 48)

**CE-Kennzeichnung** (Artikel 48):

- KI-Systeme mit hohem Risiko tragen CE-Kennzeichnung
- Zeigt Konformität mit dem AI Act an
- Sichtbar, leserlich und dauerhaft angebracht

**Zuordnung zu ISO 27001:2022**:

- Klausel 9.2: Internes Audit (ähnlich Selbstbewertung)
- Klausel 9.3: Managementbewertung

---

**Artikel 72: Post-Market-Monitoring**

Anforderungen:

- Post-Market-Monitoring-System einrichten und dokumentieren
- Daten zur Leistung über die gesamte Lebensdauer erfassen, dokumentieren, analysieren

**Post-Market-Monitoring-Plan**:

- Strategie zur Erfassung von Leistungsdaten im Realbetrieb
- Methoden zur Analyse schwerwiegender Vorfälle, Fehlfunktionen, Ungenauigkeiten
- Meldungsmechanismen gegenüber Behörden
- Feedbackschleife zum Risikomanagementsystem

**Zuordnung zu ISO 27001:2022**:

- Klausel 9.1: Überwachung, Messung, Analyse und Bewertung
- A.8.16: Überwachungsaktivitäten

---

## Betreiberpflichten für KI-Systeme mit hohem Risiko

**Artikel 26: Betreiberpflichten**

Betreiber (Nutzer) von KI-Systemen mit hohem Risiko müssen:

1. **Gemäß Anweisungen nutzen** (Artikel 26(1))
2. **Menschliche Aufsicht zuweisen** an kompetente natürliche Personen (Artikel 26(2))
3. **Betrieb überwachen** gemäß Gebrauchsanweisungen (Artikel 26(3))
4. **Nutzung aussetzen** bei vermuteten schwerwiegenden Vorfällen oder Fehlfunktionen (Artikel 26(4))
5. **Protokolle aufbewahren**, die automatisch vom System generiert werden (Artikel 26(5))
6. **Eingabedaten verwenden**, die für den beabsichtigten Zweck relevant und repräsentativ sind (Artikel 26(6))
7. **Grundrechtsfolgenabschätzung durchführen** (FRIA) vor Inbetriebnahme (Artikel 27) – für Betreiber in bestimmten Sektoren oder Anwendungen

**Grundrechtsfolgenabschätzung (FRIA)** – Artikel 27:
Erforderlich für Betreiber, die:

- Behörden sind ODER
- EU-Institutionen/Einrichtungen/Agenturen sind ODER
- KI mit hohem Risiko in bestimmten sensiblen Bereichen einsetzen (definiert in Artikel 27(1))

**FRIA-Inhalt**:

- Beschreibung der Betreiberprozesse, in denen KI genutzt wird
- Beschreibung des Nutzungszeitraums und der Häufigkeit
- Kategorien natürlicher Personen und betroffener Gruppen
- Spezifische Schadensrisiken für betroffene Personen
- Beschreibung der Maßnahmen zur menschlichen Aufsicht
- Maßnahmen bei Realisierung von Risiken

**Zuordnung zu ISO 27001:2022**:

- A.5.37: Dokumentierte Betriebsverfahren (Betreiberverfahren)
- Klausel 6.1.2: Informationssicherheits-Risikobewertung (FRIA ähnlich der Risikobewertung)
- DSGVO Artikel 35: Datenschutz-Folgenabschätzung (ähnlich FRIA)

---

# KI-Systeme mit begrenztem Risiko (Artikel 50) – Transparenzpflichten

## Überblick

Bestimmte KI-Systeme stellen ein **begrenztes Risiko** dar, erfordern aber Transparenz, um informierte Entscheidungen zu ermöglichen.

**Wirksamkeitsdatum**: 2. August 2026 (gleich wie Hochrisiko-Systeme)

**Strafe bei Nichtkonformität**: Bis zu 7,5 Millionen Euro oder 1,5 % des weltweiten Jahresumsatzes (je nachdem, welcher Betrag höher ist)

## Transparenzanforderungen

**Artikel 50(1): KI-Systeme mit Interaktion natürlicher Personen**

Wenn KI-System zur direkten Interaktion mit natürlichen Personen vorgesehen ist:

- **Natürliche Personen informieren**, dass sie mit einem KI-System interagieren
- **Ausnahmen**:
  - Aus Umständen und Kontext offensichtlich
  - Durch Gesetz für Strafverfolgung genehmigt (Erkennung, Verhütung, Untersuchung von Straftaten)

**Beispiele**:

- Chatbots (müssen Nutzer darüber informieren, dass sie mit KI interagieren)
- Virtuelle Assistenten
- Automatisierte Telefonsysteme

---

**Artikel 50(2): Emotionserkennungs- und biometrische Kategorisierungssysteme**

Bei Verwendung von Emotionserkennungs- oder biometrischen Kategorisierungssystemen:

- **Natürliche Personen informieren**, die dem System ausgesetzt sind
- **Ausnahme**: Durch Gesetz für Strafverfolgung genehmigt

**Beispiele**:

- Einzelhandels-Emotionserkennung (muss Kunden informieren)
- Vorstellungsgespräch-Emotionsanalyse-Tools
- Flughafen-Biometrische Kategorisierung

---

**Artikel 50(3): KI-generierte Inhalte (Deepfakes)**

Bei der Generierung oder Manipulation von Bild-/Audio-/Videoinhalten (Deepfakes):

- **Offenlegung**, dass Inhalte künstlich generiert oder manipuliert wurden

**Offenlegungsanforderungen**:

- Maschinenlesbares Format (technische Standards in Entwicklung)
- Für durchschnittliche Personen lesbare Offenlegung

**Ausnahmen**:

- Inhalte, die zur Ausübung des Rechts auf freie Meinungsäußerung und künstlerische/literarische/satirische Freiheit erforderlich sind
- Durch Gesetz für Strafverfolgung genehmigt
- Zur Aufdeckung/Entlarvung von Straftaten erforderlich

**Spezifische Typen**:

**Artikel 50(4): KI-generierter Text (ChatGPT-ähnliche Systeme)**

- Offenlegung, dass Ausgaben künstlich generiert oder manipuliert wurden
- Gilt für Systeme, die Text für öffentliche Informationszwecke produzieren
- **Ausnahme**: Text unterlag menschlicher Prüfung/redaktioneller Kontrolle mit redaktioneller Verantwortung

---

**Zuordnung zu ISO 27001:2022**:

- A.5.1: Richtlinien für Informationssicherheit (Transparenzrichtlinien)
- A.5.9: Inventar von Informationen und anderen zugehörigen Assets (KI-System-Inventar)

---

# KI-Systeme mit minimalem Risiko – Freiwillige Maßnahmen

## Überblick

Die meisten KI-Systeme stellen ein **minimales oder kein Risiko** dar und unterliegen **keinen Pflichtanforderungen** gemäß dem AI Act.

**Beispiele**:

- Spam-Filter
- KI-aktivierte Videospiele
- Bestandsverwaltungssysteme
- Empfehlungsmaschinen (E-Commerce)
- Interne Geschäftsanalyse
- KI-Entwicklungstools

## Freiwillige Verhaltenskodizes (Artikel 95)

Anbieter von KI-Systemen mit minimalem Risiko werden **ermutigt**, freiwillig anzuwenden:

- Anforderungen für KI-Systeme mit hohem Risiko (Artikel 9–15)
- Transparenzanforderungen (Artikel 50)
- Von der Industrie entwickelte Verhaltenskodizes

**Vorteile freiwilliger Compliance**:

- Vertrauenswürdigkeit demonstrieren
- Wettbewerbsvorteil
- Vorbereitung auf potenzielle zukünftige Regulierung
- Ausrichtung an ethischen KI-Grundsätzen

---

# KI-Modelle für allgemeine Zwecke (GPAI) – Kapitel V

## Überblick

**KI-Modelle für allgemeine Zwecke** (GPAI) sind Foundation-Modelle, die für ein breites Aufgabenspektrum geeignet sind.

**Beispiele**:

- Große Sprachmodelle (GPT-4, Claude, Gemini, LLaMA)
- Multimodale Modelle (GPT-4V, Gemini)
- Foundation-Modelle zur Bildgenerierung (DALL-E, Stable Diffusion, Midjourney)

**Wirksamkeitsdatum**: 2. August 2025 (12 Monate nach Inkrafttreten)

## Anbieterpflichten für GPAI

**Artikel 53: Pflichten für alle GPAI-Anbieter**

Alle GPAI-Anbieter müssen:

1. **Technische Dokumentation** (Artikel 53(1)(a) + Anhang XI):

   - Allgemeine Beschreibung des Modells (Fähigkeiten, Grenzen)
   - Beschreibung der für das Training verwendeten Daten (Quellen, Kuration)
   - Informationen zu Rechenressourcen (Trainingszeit, Hardware)
   - Beschreibung des Bewertungsprozesses und der Ergebnisse

2. **Informationen für nachgelagerte Anbieter** (Artikel 53(1)(b)):

   - Dokumentation, die nachgelagerten Anbietern (die GPAI in ihre KI-Systeme integrieren) ermöglicht, den AI Act einzuhalten
   - Gebrauchsanweisungen

3. **Urheberrechtsrichtlinie** (Artikel 53(1)(c)):

   - Öffentlich verfügbare Richtlinie zur Identifizierung und Einhaltung der Richtlinie (EU) 2019/790 (Urheberrechtsrichtlinie)
   - Zusammenfassung urheberrechtlich geschützter Inhalte, die für das Training verwendet wurden (soweit verfügbar)

4. **Transparenz** (Artikel 53(1)(d)):

   - Öffentlich verfügbare Zusammenfassung der für das Training verwendeten Inhalte
   - EU-KI-Büro-Vorlage (wird noch entwickelt)

**Artikel 54: GPAI-Modelle mit systemischen Risiken – Zusätzliche Pflichten**

Für GPAI-Modelle mit **systemischen Risiken** (siehe Abschnitt 7.3):

5. **Modellbewertung** (Artikel 54(1)(a)):

   - Gegnerische Tests (Red Teaming)
   - Bewertung und Minderung systemischer Risiken

6. **Verfolgung schwerwiegender Vorfälle** (Artikel 54(1)(b)):

   - Schwerwiegende Vorfälle verfolgen, dokumentieren, dem KI-Büro melden

7. **Cybersicherheit** (Artikel 54(1)(c)):

   - Angemessenes Cybersicherheitsschutzniveau sicherstellen
   - Modellgewichte und andere Parameter vor unbefugtem Zugriff schützen

8. **Energieeffizienz** (Artikel 54(1)(d)):

   - Energieverbrauch während des Trainings melden
   - Energieeffizienz optimieren, soweit möglich

## GPAI-Modelle mit systemischen Risiken

**Definition** (Artikel 51):
GPAI-Modell mit systemischem Risiko, wenn:

- Hochleistungsfähigkeiten (nach Stand der Technik bewertet) ODER
- Erhebliche Auswirkungen auf den EU-Markt (über Modellreichweite bewertet) ODER
- Kumulativer Rechenaufwand für Training ≥ 10^25 FLOPs (Gleitkommaoperationen)

**10^25 FLOPs-Schwellenwert** (Artikel 51(1)(a)):

- Systemisches Risiko wird vermutet, wenn Training ≥ 10^25 FLOPs
- Beispiel: GPT-4 geschätzt ~2–5 × 10^25 FLOPs (würde qualifizieren)

**Einstufung**:

- EU-KI-Büro kann Modelle als systemisches Risiko einstufen
- Anbieter können Kommissionsentscheidung beantragen, wenn Rechenaufwand < 10^25 FLOPs

**Strafe bei Nichtkonformität**: Bis zu 15 Millionen Euro oder 3 % des weltweiten Jahresumsatzes (je nachdem, welcher Betrag höher ist)

## Zuordnung zu ISO 27001:2022 für GPAI

| AI-Act-Anforderung | ISO 27001:2022-Kontrolle | Hinweise |
|--------------------|--------------------------|----------|
| Technische Dokumentation (Artikel 53) | A.5.37, Klausel 7.5 | Dokumentationspraktiken |
| Urheberrechtsrichtlinie (Artikel 53(1)(c)) | A.5.31 Gesetzliche Anforderungen | Urheberrechtseinhaltung |
| Modellbewertung (Artikel 54(1)(a)) | A.8.8 Schwachstellenmanagement | Gegnerische Tests ähnlich Penetrationstests |
| Verfolgung schwerwiegender Vorfälle (Artikel 54(1)(b)) | A.5.24–5.28 Vorfallmanagement | Incident Tracking und Reporting |
| Cybersicherheit (Artikel 54(1)(c)) | A.8.24 Kryptografie, A.8.3 Zugriffsbeschränkung | Schutz von Modellgewichten |

---

# Organisatorische Anforderungen und Governance

## KI-Kompetenz (Artikel 4)

**Anforderung**: Anbieter und Betreiber stellen sicher, dass **mit KI-Systemen arbeitende Mitarbeiter** ein ausreichendes Niveau an KI-Kompetenz haben.

**KI-Kompetenz-Definition**: Fähigkeiten und Kenntnisse zum:

- Verstehen von Fähigkeiten und Grenzen von KI-Systemen
- Korrekte Interpretation von Systemausgaben
- Treffen informierter Entscheidungen zur angemessenen Nutzung

**Umsetzung**:

- Schulungsprogramme für KI-System-Nutzer
- Rollenspezifische Schulungen (Entwickler, Betreiber, Aufsichtspersonal)
- Bewusstsein für Verzerrungen, Ethik, Grundrechte

**Zuordnung zu ISO 27001:2022**:

- A.6.3: Bewusstsein, Schulung und Ausbildung zur Informationssicherheit

---

## Rollen und Verantwortlichkeiten

**Empfohlene Governance-Struktur**:

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **KI-Governance-Board** | Strategische KI-Aufsicht, Richtliniengenehmigung, Risikobereitschaft |
| **Chief AI Officer (CAIO)** oder Äquivalent | KI-Programmleitung, Compliance-Koordination |
| **ISB** | Cybersicherheitsaspekte von KI-Systemen (Artikel 15) |
| **DSB** | DSGVO-Compliance für KI-Verarbeitung personenbezogener Daten |
| **Recht/Compliance** | AI-Act-Compliance, Risikobewertungen, externe Berichterstattung |
| **Produktverantwortliche** | Verantwortlich für spezifische KI-Systeme (Risikomanagement, Dokumentation) |
| **KI-Entwicklungsteams** | Umsetzung technischer Anforderungen (Artikel 9–15) |
| **Menschliches Aufsichtspersonal** | Gemäß Artikel 14 für Hochrisiko-Systeme zugewiesen |

**Zuordnung zu ISO 27001:2022**:

- Klausel 5.3: Organisatorische Rollen, Verantwortlichkeiten und Befugnisse
- A.5.2: Rollen und Verantwortlichkeiten für Informationssicherheit

---

## KI-System-Inventar

**Anforderung**: Inventar aller entwickelten oder eingesetzten KI-Systeme pflegen.

**Inventarinhalt**:

- KI-System-Name und -Version
- Anbieter (interne Entwicklung oder extern)
- Beabsichtigter Zweck und Anwendungsfälle
- Risikoklassifizierung (Inakzeptables Risiko, Hohes Risiko, Begrenztes Risiko, Minimales Risiko)
- Bereitstellungsstatus (Entwicklung, Test, Produktion, Außerbetrieb)
- Regulatorische Verpflichtungen (Konformitätsbewertungsstatus)
- Zugewiesene Betreiberverantwortlichkeiten

**Zuordnung zu ISO 27001:2022**:

- A.5.9: Inventar von Informationen und anderen zugehörigen Assets

---

# Zuordnung ISO 27001:2022 → EU AI Act

## Kontrollzuordnungsmatrix

| AI-Act-Anforderung | AI-Act-Artikel | ISO 27001:2022-Kontrolle | Lückenanalyse |
|--------------------|----------------|--------------------------|---------------|
| Bewertung verbotener Praktiken | Art. 5 | A.5.1, A.5.31 | AI-Act-spezifische Verbote |
| Risikomanagementsystem | Art. 9 | Klausel 6.1.2–6.1.3 | AI Act: Detaillierterer KI-spezifischer Risikoprozess |
| Data Governance | Art. 10 | A.5.12–5.14 | **AI-Act-spezifisch**: Datenqualität, Bias-Minderung |
| Technische Dokumentation | Art. 11 | A.5.37, Klausel 7.5 | AI Act: Umfangreiche KI-System-Dokumentation |
| Protokollierung (Aufzeichnung) | Art. 12 | A.8.15–8.16 | Ausgerichtet |
| Transparenz gegenüber Betreibern | Art. 13 | A.5.37 | AI Act: Detaillierte Gebrauchsanweisungen |
| Menschliche Aufsicht | Art. 14 | A.5.37 | **AI-Act-spezifisch**: Anforderungen an Human-in-the-Loop |
| Genauigkeit, Robustheit, Cybersicherheit | Art. 15 | A.8.7–8.8, A.8.16 | AI Act: KI-spezifischer Schutz gegen gegnerische Angriffe |
| Qualitätsmanagementsystem | Art. 16 | Klausel 4–10 (gesamtes ISMS) | Ergänzend: ISO 9001 + ISO 27001 |
| Konformitätsbewertung | Art. 43–51 | Klausel 9.2–9.3 | **AI-Act-spezifisch**: CE-Kennzeichnung, benannte Stellen |
| Post-Market-Monitoring | Art. 72 | Klausel 9.1, A.8.16 | AI Act: Kontinuierliche Leistungsüberwachung im Realbetrieb |
| Betreiberpflichten | Art. 26 | A.5.37 | AI Act: Betreiber-spezifische Verantwortlichkeiten |
| Transparenz (begrenztes Risiko) | Art. 50 | A.5.1 | **AI-Act-spezifisch**: Nutzer-Offenlegungsanforderungen |
| KI-Kompetenz | Art. 4 | A.6.3 | AI Act: KI-spezifische Schulungen |

## Wesentliche Lücken zwischen ISO 27001:2022 und EU AI Act

**Lücke 1: KI-spezifische Risikobewertung**

- ISO 27001: Allgemeine Informationssicherheits-Risikobewertung
- AI Act: Detailliertes KI-System-Risikomanagement (Verzerrung, Diskriminierung, Sicherheit, Grundrechte)

**Lücke 2: Data Governance für KI**

- ISO 27001: Datenklassifizierung, -schutz
- AI Act: Qualität der Trainings-/Validierungs-/Testdaten, Repräsentativität, Bias-Minderung

**Lücke 3: Anforderungen an menschliche Aufsicht**

- ISO 27001: Keine spezifischen Anforderungen an menschliche Aufsicht
- AI Act: Obligatorische menschliche Aufsicht für Hochrisiko-KI (Artikel 14)

**Lücke 4: Konformitätsbewertung und CE-Kennzeichnung**

- ISO 27001: Zertifizierung durch akkreditierte Stelle
- AI Act: Konformitätsbewertung (Selbstbewertung oder benannte Stelle), CE-Kennzeichnung

**Lücke 5: Transparenz und Erklärbarkeit**

- ISO 27001: Keine Erklärbarkeitsanforderungen
- AI Act: Transparenz gegenüber Betreibern (Artikel 13), Transparenz gegenüber Endnutzern (Artikel 50)

**Lücke 6: Grundrechtsauswirkungen**

- ISO 27001: Keine Grundrechtsbewertung
- AI Act: Grundrechtsfolgenabschätzung (FRIA) für bestimmte Betreiber (Artikel 27)

**Lücke 7: Post-Market-Monitoring spezifisch für KI**

- ISO 27001: Allgemeine Überwachung und Messung
- AI Act: KI-System-Leistungsüberwachung im Realbetrieb, Vorfallsberichterstattung

## AI-Act-Compliance mit ISO-27001-Fundament

**Kernaussage**:
ISO 27001:2022 bietet starke Grundlagenkontrollen für die AI-Act-Compliance, insbesondere für Cybersicherheitsaspekte (Artikel 15). Allerdings führt der AI Act **KI-spezifische Anforderungen** ein, die nicht von ISO 27001 abgedeckt werden:

**Zusätzlich zu berücksichtigende Standards**:

- **ISO/IEC 42001:2023**: KI-Managementsystem (AIMS) – speziell für KI-Governance konzipiert
- **ISO/IEC 23894:2023**: KI-Risikomanagement
- **ISO/IEC 24029-1:2021**: Bewertung der Robustheit neuronaler Netze
- **ISO/IEC TR 24028:2020**: Überblick über Vertrauenswürdigkeit in KI
- **ISO/IEC 38507:2022**: IT-Governance – Governance-Implikationen von KI

Organisationen mit ISO 27001 benötigen in der Regel **40–60 % zusätzlichen Aufwand** zur Erreichung der EU-AI-Act-Compliance für Hochrisiko-Systeme, hauptsächlich in:

- KI-spezifischem Risikomanagement
- Data Governance für Trainings-/Validierungsdaten
- Verfahren zur menschlichen Aufsicht
- Konformitätsbewertung und CE-Kennzeichnung
- Grundrechtserwägungen

---

# Implementierungserwägungen

## AI-Act-Compliance-Fahrplan

**Wenn [Organisation] KI-Systeme entwickelt oder betreibt, die EU-Bürger betreffen**:

**Phase 1: Inventar und Klassifizierung (Monate 1–3)**

- Alle KI-Systeme identifizieren (aktuelle und geplante)
- Jedes KI-System klassifizieren (Inakzeptables Risiko, Hohes Risiko, Begrenztes Risiko, Minimales Risiko)
- Artikel-5-Verbote bewerten (sofortige Maßnahmen bei Verstössen)
- Anbieter- vs. Betreiberrolle für jedes System bestimmen
- GPAI-Modelle identifizieren (falls zutreffend)

**Phase 2: Lückenbewertung (Monate 3–6)**

- Aktuelle KI-Governance und -Dokumentation bewerten
- Lücken gegenüber AI-Act-Anforderungen identifizieren
- Behebungsmaßnahmen priorisieren (verbotene Praktiken zuerst, dann Hochrisiko)
- Budget und Ressourcen schätzen
- Rechtsberatung für komplexe Klassifizierungsentscheidungen hinzuziehen

**Phase 3: Governance und Richtlinien (Monate 6–9)**

- KI-Governance-Struktur einrichten (Rollen, Verantwortlichkeiten)
- KI-Risikomanagement-Rahmen entwickeln (Artikel 9)
- Data-Governance-Richtlinien erstellen (Artikel 10)
- Verfahren zur menschlichen Aufsicht einrichten (Artikel 14)
- KI-Kompetenzskulungsprogramme (Artikel 4)

**Phase 4: Hochrisiko-System-Compliance (Monate 9–18)**

- Technische Anforderungen umsetzen (Artikel 11–15)
- Technische Dokumentation erstellen (Anhang IV)
- Qualitätsmanagementsystem umsetzen (Artikel 16)
- Konformitätsbewertungsvorbereitung durchführen
- Post-Market-Monitoring einrichten

**Phase 5: Konformitätsbewertung (Monate 18–24)**

- Technische Dokumentation abschliessen
- Interne Bewertung durchführen oder benannte Stelle beauftragen
- Identifizierte Nichtkonformitäten beheben
- EU-Konformitätserklärung erstellen
- CE-Kennzeichnung anbringen (bei Hochrisiko-System)

**Phase 6: Bereitstellung und Überwachung (Monat 24+)**

- KI-Systeme mit hohem Risiko konform einsetzen
- Post-Market-Monitoring umsetzen (Artikel 72)
- Kontinuierliche Compliance-Überwachung
- Jährliche Überprüfungen und Aktualisierungen
- Verfahren zur Vorfallsmeldung

**Zeitplanhinweise**:

- Verbotene Praktiken: Sofortiger Handlungsbedarf (2. Februar 2025)
- GPAI: 2. August 2025
- Hochrisiko-Systeme: 2. August 2026
- Übergangsfrist bestehende Systeme: Bis 2. August 2030 (sofern keine wesentliche Änderung)

## Ressourcenanforderungen

**Personal**:

- Chief AI Officer oder Äquivalent
- KI-Governance-Team (funktionsübergreifend)
- Data Scientists/ML-Ingenieure (KI-Entwicklung)
- Rechtsberatung mit AI-Act-Expertise
- Data-Governance-Spezialisten
- Menschliches Aufsichtspersonal (für jedes Hochrisiko-System)
- Compliance-/Auditteam

**Externe Ressourcen**:

- Rechtsberatung (AI-Act-Interpretation)
- Benannte Stellen (falls für Konformitätsbewertung erforderlich)
- KI-Ethikberater
- Externe Auditoren (Qualitätsmanagementsystem)

**Technologie**:

- KI-System-Dokumentationsplattform
- Modell-Governance-Tools (MLOps, Modellregister)
- Data-Governance-Plattformen (Datenqualität, Herkunft)
- Protokollierungs- und Überwachungsinfrastruktur
- Adversarielle Test-Tools (für GPAI mit systemischen Risiken)

## Kostenimplikationen

AI-Act-Compliance-Kosten variieren erheblich je nach:

- Anzahl und Risikoniveau der KI-Systeme
- Anbieter- vs. Betreiberrolle
- Interne KI-Entwicklung vs. Drittanbieter-KI

**Geschätzte Compliance-Kosten**:

**KI-System mit hohem Risiko (Anbieter)**:

- Technische Dokumentation und Qualitätsmanagement: 50.000 € – 200.000 €
- Konformitätsbewertung (benannte Stelle, falls erforderlich): 10.000 € – 50.000 €
- Jährliches Post-Market-Monitoring: 20.000 € – 100.000 €
- Rechts- und Beratungsleistungen: 30.000 € – 100.000 €
- **Gesamte Anfangskosten**: 110.000 € – 450.000 € pro Hochrisiko-System
- **Jährlich laufend**: 50.000 € – 150.000 € pro System

**KI-System mit hohem Risiko (Betreiber)**:

- Grundrechtsfolgenabschätzung: 10.000 € – 30.000 €
- Umsetzung menschlicher Aufsicht: 20.000 € – 50.000 €
- Schulungen und Verfahren: 10.000 € – 30.000 €
- **Gesamte Anfangskosten**: 40.000 € – 110.000 € pro System
- **Jährlich laufend**: 20.000 € – 50.000 €

**GPAI-Modell mit systemischem Risiko**:

- Technische Dokumentation: 100.000 € – 300.000 €
- Adversarielle Tests (Red Teaming): 50.000 € – 200.000 €
- Cybersicherheitsmaßnahmen (Modellschutz): 50.000 € – 150.000 €
- Energieeffizienzberichterstattung: 10.000 € – 30.000 €
- **Gesamte Anfangskosten**: 210.000 € – 680.000 €
- **Jährlich laufend**: 100.000 € – 300.000 €

**Bußgelder bei Nichtkonformität**:

- Verbotene Praktiken: Bis zu 35 Mio. € oder 7 % des Umsatzes
- Hochrisiko-Verstösse: Bis zu 15 Mio. € oder 3 % des Umsatzes
- Verstösse bei begrenztem Risiko: Bis zu 7,5 Mio. € oder 1,5 % des Umsatzes
- Übermittlung unrichtiger Informationen: Bis zu 7,5 Mio. € oder 1,5 % des Umsatzes

---

# Häufige Fallstricke und gewonnene Erkenntnisse

## Häufige AI-Act-Compliance-Herausforderungen

**Herausforderung 1: Identifizierung von KI-Systemen**

- Organisationen unterschätzen die Anzahl der verwendeten KI-Systeme
- KI-Definition ist weit gefasst – umfasst regelbasierte Systeme, statistische Modelle
- In Drittanbieter-Software eingebettete KI wird häufig übersehen

**Herausforderung 2: Unsicherheit bei der Risikoklassifizierung**

- Grenze zwischen hohem Risiko und begrenztem Risiko nicht immer klar
- Anwendungsfall wichtiger als Technologie (gleiches Modell, unterschiedliche Nutzung = unterschiedliches Risiko)
- Anhang-III-Kategorien unterliegen der Interpretation

**Herausforderung 3: Verwirrung bei Anbieter- vs. Betreiberrolle**

- Dieselbe Organisation kann sowohl Anbieter als auch Betreiber sein
- Anpassung von Drittanbieter-KI kann Organisation zum Anbieter machen
- „Wesentliche Änderung" löst Anbieterpflichten aus

**Herausforderung 4: Data Governance für KI**

- Datenqualität und Bias-Minderung beim Training erfordern erheblichen Aufwand
- Legacy-KI-Systeme können Daten-Herkunftsdokumentation fehlen lassen
- Repräsentativität der Daten schwierig zu bewerten und zu validieren

**Herausforderung 5: Umsetzung menschlicher Aufsicht**

- Geeignetes Aufsichtspersonal mit Kompetenz identifizieren
- Ausgewogenheit von Aufsicht und betrieblicher Effizienz
- „Stoppknopf" in Echtzeitsystemen nicht immer technisch machbar

**Herausforderung 6: Konformitätsbewertungsvorbereitung**

- Technische Dokumentation ist umfangreich (Anhang IV)
- Qualitätsmanagementsystem erfordert organisatorische Reife
- Kapazität benannter Stellen anfänglich möglicherweise begrenzt

**Herausforderung 7: GPAI-Modellpflichten**

- Urheberrechts-Compliance für Trainingsdaten schwierig zu überprüfen
- Transparenzzusammenfassungen erfordern standardisierte Formate (noch in Entwicklung)
- Schwellenwert für systemisches Risiko (10^25 FLOPs) kann viele Foundation-Modelle erfassen

## Best Practices

**Praxis 1**: Frühzeitig umfassendes KI-System-Inventar erstellen (nicht auf Fristen warten)
**Praxis 2**: Rechtsberatung für Risikoklassifizierung hinzuziehen (dokumentierte Entscheidungen)
**Praxis 3**: KI-Governance-Struktur vor technischen Anforderungen einrichten
**Praxis 4**: ISO 27001 + ISO 42001 (KI-Managementsystem) zusammen nutzen
**Praxis 5**: Alles dokumentieren (AI Act betont Dokumentation stark)
**Praxis 6**: Menschliche Aufsicht ab der KI-System-Designphase einrichten (nicht nachträglich)
**Praxis 7**: Für GPAI-Anbieter frühzeitig mit EU-KI-Büro in Kontakt treten (Leitlinien noch in Entwicklung)
**Praxis 8**: Freiwillige Compliance für KI mit minimalem Risiko in Betracht ziehen (zukunftssicher)
**Praxis 9**: AI-Act-Compliance in SDLC und Beschaffungsprozesse integrieren
**Praxis 10**: AI-Act-delegierte Rechtsakte und Durchführungsrechtsakte beobachten (viele noch in Entwicklung)

---

# Referenzen und Ressourcen

## Offizielle EU-AI-Act-Ressourcen

**Primäre Verordnung**:

- Verordnung (EU) 2024/1689 (AI Act) – Amtsblatt der EU

**EU-KI-Büro**:

- Website: https://digital-strategy.ec.europa.eu/en/policies/ai-office
- Leitliniendokumente (in Entwicklung)
- Vorlagen für technische Dokumentation und Transparenzzusammenfassungen

**Europäische Kommission**:

- AI-Act-Seiten: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

## Verwandte Standards und Rahmenwerke

**ISO-KI-Standards**:

- **ISO/IEC 42001:2023**: KI-Managementsystem (AIMS) – empfohlen für AI-Act-Compliance
- **ISO/IEC 23894:2023**: KI-Risikomanagement
- **ISO/IEC 24029-1:2021**: Bewertung der Robustheit neuronaler Netze
- **ISO/IEC TR 24028:2020**: Überblick über Vertrauenswürdigkeit in KI
- **ISO/IEC 38507:2022**: IT-Governance – Governance-Implikationen von KI
- **ISO/IEC 23053:2022**: Rahmen für KI-Systeme mit maschinellem Lernen

**Informationssicherheitsstandards**:

- ISO/IEC 27001:2022: Informationssicherheitsmanagement
- ISO/IEC 27002:2022: Informationssicherheitskontrollen
- ISO/IEC 27701:2019: Datenschutzinformationsmanagement

**NIST-KI-Standards** (informationsreferenz):

- NIST AI Risk Management Framework (AI RMF)
- NIST SP 1270: Towards a Standard for Identifying and Managing Bias in AI

## Branchenleitfäden und Ressourcen

**European AI Alliance**:

- Stakeholder-Forum für KI-Politik
- Website: https://futurium.ec.europa.eu/en/european-ai-alliance

**AI Standards Hub**:

- CEN-CENELEC KI-Standardisierungsaktivitäten
- Website: https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/

**Rechts- und Beratungsressourcen**:

- Rechtsberatung mit EU-AI-Act-Expertise hinzuziehen
- KI-Ethikberater für Grundrechtsfolgenabschätzungen
- Benannte Stellen (Liste wird von der Kommission veröffentlicht)

---

# Anhang A: EU-AI-Act-Compliance-Selbstbewertungscheckliste

## KI-System-Inventar

| Frage | Status | Hinweise |
|-------|--------|---------|
| Haben wir alle verwendeten oder entwickelten KI-Systeme identifiziert? | ⬜ Ja ⬜ Nein ⬜ In Bearbeitung | [Systeme auflisten] |
| Haben wir das Risikoniveau jedes KI-Systems klassifiziert? | ⬜ Ja ⬜ Nein ⬜ Teilweise | [Klassifizierungsdokumentation] |
| Haben wir die Anbieter- vs. Betreiberrolle für jedes System bestimmt? | ⬜ Ja ⬜ Nein ⬜ Teilweise | [Rollendokumentation] |
| Entwickeln oder nutzen wir GPAI-Modelle? | ⬜ Ja ⬜ Nein ⬜ Ungewiss | [GPAI-Liste, falls zutreffend] |

## Verbotene Praktiken (Artikel 5)

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Alle KI-Systeme auf Artikel-5-Verbote geprüft | ⬜ Ja ⬜ Nein | | |
| Keine unterschwellige Manipulations-KI bestätigt | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Keine Social-Scoring-KI bestätigt | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Keine Echtzeit-RBI bestätigt (außer Strafverfolgungsausnahme) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Keine Emotionserkennung am Arbeitsplatz/in der Bildung bestätigt (außer Sicherheit/Medizin) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Artikel-5-Bewertung dokumentiert | ⬜ Ja ⬜ Nein | | |

## KI-Systeme mit hohem Risiko – Anbieterpflichten

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Risikomanagementsystem eingerichtet (Artikel 9) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Data-Governance und Qualitätsmaßnahmen (Artikel 10) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Technische Dokumentation erstellt (Artikel 11, Anhang IV) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Automatische Protokollierung umgesetzt (Artikel 12) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Gebrauchsanweisungen bereitgestellt (Artikel 13) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Maßnahmen zur menschlichen Aufsicht konzipiert (Artikel 14) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Genauigkeit, Robustheit, Cybersicherheit adressiert (Artikel 15) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Qualitätsmanagementsystem umgesetzt (Artikel 16) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Konformitätsbewertung durchgeführt | ⬜ Ja ⬜ Nein ⬜ Geplant | | |
| CE-Kennzeichnung angebracht (falls zutreffend) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Post-Market-Monitoring-System eingerichtet (Artikel 72) | ⬜ Ja ⬜ Nein ⬜ N/A | | |

## KI-Systeme mit hohem Risiko – Betreiberpflichten

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Nutzung gemäß Anweisungen (Artikel 26(1)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Menschliche Aufsicht zugewiesen (Artikel 26(2)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Betrieb gemäß Anweisungen überwacht (Artikel 26(3)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Verfahren zur Aussetzung bei schwerwiegendem Vorfall (Artikel 26(4)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Protokolle aufbewahrt (Artikel 26(5)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Eingabedaten relevant und repräsentativ (Artikel 26(6)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| FRIA durchgeführt (Artikel 27, falls zutreffend) | ⬜ Ja ⬜ Nein ⬜ N/A | | |

## KI-Systeme mit begrenztem Risiko

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Chatbot/Virtueller Assistent gibt KI-Interaktion bekannt (Artikel 50(1)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Emotionserkennung/biometrische Kategorisierung informiert Nutzer (Artikel 50(2)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Deepfake-Inhalte offengelegt (Artikel 50(3)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| KI-generierter Text offengelegt (Artikel 50(4)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |

## KI-Modelle für allgemeine Zwecke

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| Technische Dokumentation erstellt (Artikel 53, Anhang XI) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Informationen für nachgelagerte Anbieter (Artikel 53(1)(b)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Urheberrechtsrichtlinie dokumentiert (Artikel 53(1)(c)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Trainingsinhalts-Zusammenfassung veröffentlicht (Artikel 53(1)(d)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| Systemisches Risiko bewertet (≥10^25 FLOPs oder andere Kriterien) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| **Bei systemischem Risiko**: Modellbewertung / Red Teaming (Artikel 54(1)(a)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| **Bei systemischem Risiko**: Verfolgung schwerwiegender Vorfälle (Artikel 54(1)(b)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| **Bei systemischem Risiko**: Cybersicherheit / Modellschutz (Artikel 54(1)(c)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |
| **Bei systemischem Risiko**: Energieeffizienzberichterstattung (Artikel 54(1)(d)) | ⬜ Ja ⬜ Nein ⬜ N/A | | |

## Organisatorische Anforderungen

| Anforderung | Status | Nachweis | Hinweise |
|-------------|--------|----------|---------|
| KI-Governance-Struktur eingerichtet | ⬜ Ja ⬜ Nein ⬜ In Bearbeitung | | |
| KI-Kompetenzschulung für Mitarbeiter (Artikel 4) | ⬜ Ja ⬜ Nein ⬜ Geplant | | |
| KI-System-Inventar gepflegt | ⬜ Ja ⬜ Nein ⬜ In Bearbeitung | | |
| Rollen und Verantwortlichkeiten zugewiesen | ⬜ Ja ⬜ Nein ⬜ Teilweise | | |

---

# Anhang B: Klassifizierungsdiagramm für KI-Systeme mit hohem Risiko

```
┌─────────────────────────────────────────┐
│   Handelt es sich um ein KI-System?     │
│   (Definition gemäß Artikel 3(1))       │
└──────────────┬──────────────────────────┘
               │ JA
               ↓
┌─────────────────────────────────────────┐
│   Ist es nach Artikel 5 verboten?       │
│   (Social Scoring, unterschwellige      │
│    Manipulation, RBI in der             │
│    Öffentlichkeit, usw.)                │
└──────────────┬──────────────────────────┘
               │ NEIN (Bei JA → STOPP, verboten)
               ↓
┌─────────────────────────────────────────┐
│   Ist es in Anhang III aufgeführt?      │
│   (Biometrische ID, kritische Infra.,   │
│    Beschäftigung, Bildung,              │
│    Strafverfolgung, Kredit-Scoring      │
│    usw.)                                │
└──────────────┬──────────────────────────┘
         JA    │   NEIN
               ↓
┌─────────────────────────────────────────┐
│   ODER: Ist es eine Sicherheits-        │
│   komponente eines Produkts nach        │
│   Anhang-I-Recht?                       │
└──────────────┬──────────────────────────┘
         JA    │   NEIN
               ↓
┌─────────────────────────────────────────┐
│   KI-SYSTEM MIT HOHEM RISIKO            │
│                                          │
│   Anforderungen:                         │
│   - Risikomanagement (Art. 9)           │
│   - Data Governance (Art. 10)           │
│   - Technische Dokumentation (Art. 11)  │
│   - Protokollierung (Art. 12)           │
│   - Transparenz (Art. 13)              │
│   - Menschliche Aufsicht (Art. 14)     │
│   - Genauigkeit/Robustheit (Art. 15)   │
│   - QMS (Art. 16)                       │
│   - Konformitätsbewertung (Art. 43–51) │
│   - Post-Market-Monitoring (Art. 72)    │
└──────────────┬──────────────────────────┘
               │
          (Ende – Hohes Risiko)

        (NEIN aus Anhang III/I-Prüfung)
               ↓
┌─────────────────────────────────────────┐
│   Bestehen Transparenzanforderungen?    │
│   - Chatbot/Interaktion mit Menschen?  │
│   - Emotionserkennung/biometr. Kat.?   │
│   - Deepfakes/synthetische Inhalte     │
│     generiert?                          │
│   - Text für öffentliche Info.          │
│     generiert?                          │
└──────────────┬──────────────────────────┘
         JA    │   NEIN
               ↓
┌─────────────────────────────────────────┐
│   KI-SYSTEM MIT BEGRENZTEM RISIKO       │
│                                          │
│   Anforderungen:                         │
│   - Transparenzpflichten (Art. 50)      │
│   - KI-Interaktion/Inhalte offenlegen   │
└──────────────┬──────────────────────────┘
               │
          (Ende – Begrenztes Risiko)

        (NEIN aus Transparenzprüfung)
               ↓
┌─────────────────────────────────────────┐
│   KI-SYSTEM MIT MINIMALEM RISIKO        │
│                                          │
│   Anforderungen:                         │
│   - Keine Pflichtanforderungen           │
│   - Freiwillige Verhaltenskodizes        │
│     (Art. 95)                           │
└─────────────────────────────────────────┘
```

---

**ENDE DER TECHNISCHEN REFERENZ**

---

*Diese technische Referenz unterstützt potenzielle EU-AI-Act-Compliance-Anforderungen, wie in ISMS-POL-00 festgestellt. Alle regulatorischen Anwendbarkeitsbestimmungen und verbindlichen Anforderungen sind in ISMS-POL-00 und genehmigten ISMS-Richtliniendokumenten definiert.*

*Für Organisationen, die KEINE KI-Systeme entwickeln oder betreiben, die EU-Bürger betreffen, dient dieses Dokument ausschließlich zur informativen Sensibilisierung und begründet KEINE Compliance-Verpflichtungen.*

<!-- ISMS-CORE:REF:ISMS-REF-EU-AI-ACT-DE:framework:REF:eu-ai-act -->

<!-- QA_VERIFIED: 2026-03-28 -->
