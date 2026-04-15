<!-- ISMS-CORE:POLICY:AI-POL-00-DE:ai:POL:00 -->
**AI-POL-00 — Regulatorischer Anwendbarkeitsrahmen für KI**
**Massgebliche Referenz für Compliance-Pflichten des KI-Managementsystems**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumententitel** | Regulatorischer Anwendbarkeitsrahmen für KI |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | AI-POL-00 |
| **Dokumentenersteller** | KI-Governance-Beauftragter (KI-GB) / Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |
| **AIMS-Produktversion** | 1.0 |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [Date - 8 weeks] | KI-GB | Ersterstellung — Drei-Stufen-Rahmenwerk, KI-Verordnung + ISO 42001 Geltungsbereich |
| 0.2 | [Date - 6 weeks] | KI-GB + Legal | Sektorspezifische Pflichten ergänzt, ISO 42005:2025 Stufenzuordnung |
| 0.3 | [Date - 4 weeks] | ISB | Abstimmung mit ISMS-POL-00-Methodik; Schweizer KI-Strategie-Kontext |
| 0.4 | [Date - 2 weeks] | KI-GB / Legal / ISB | Stakeholder-Feedback eingearbeitet; Abschnitt zur Regulierungsbeobachtung ergänzt |
| 1.0 | [Datum] | KI-GB / Legal / ISB | Erstgenehmigung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen KI-regulatorischen Änderungen, neuen Standardveröffentlichungen oder Änderungen des Zertifizierungsumfangs)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: KI-Governance-Beauftragter (oder designierter ISB, sofern keine dedizierte KI-Governance-Rolle vorhanden)
- Sekundär: Informationssicherheitsbeauftragter (ISB)
- Compliance: Rechtsbeauftragter / Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- AI-POL-01 — KI-Governance und Entscheidungsrahmen
- ISMS-POL-00 — Regulatorischer Anwendbarkeitsrahmen (ISMS-Basis — obligatorische Querverweisnahme)
- ISO/IEC 42001:2023 Klausel 4.2 (Verstehen der Bedürfnisse und Erwartungen interessierter Parteien)
- ISO/IEC 42001:2023 Klausel 4.3 (Bestimmung des Geltungsbereichs des KI-Managementsystems)
- Alle AIMS-Richtliniendokumente (obligatorische Referenz)

**Verteilung**: Alle AIMS-Stakeholder, KI-Governance-Beauftragte, Richtlinienautoren, KI-System-Eigentümer, Legal/Compliance, Auditoren
**Referenziert durch**: Alle AIMS-Richtliniendokumente (AI-POL-01, alle AI-POL-A.x.x-Kontrollgruppen-Richtlinien)

**Sprachstrategie**: Technische oder regulatorische Begriffe, die international etabliert sind (z.B. EU AI Act, GPAI, ISO/IEC, AISIA, NIST AI RMF), werden in englischer Sprache beibehalten, um Präzision zu wahren und grenzüberschreitende regulatorische Referenzen zu erleichtern.

---

## Zusammenfassung für die Geschäftsleitung

Dieses Dokument bildet die **massgebliche Referenz** für die Interpretation der Anwendbarkeit von KI-Regulierungen und -Rahmenwerken im gesamten KI-Managementsystem (AIMS).

**Zweck**: Beseitigung von Mehrdeutigkeiten und Inkonsistenzen bei der Referenzierung von KI-Gesetzen, -Vorschriften und -Normen in der AIMS-Dokumentation.

**Geltungsbereich**: Alle Verweise auf KI-Gesetze, KI-Vorschriften und KI-Governance-Rahmenwerke in der AIMS-Dokumentation.

**Beziehung zum ISMS**: Diese Richtlinie ist das KI-spezifische Pendant zu **ISMS-POL-00** (Regulatorischer Anwendbarkeitsrahmen). ISMS-POL-00 regelt die Informationssicherheitspflichten. AI-POL-00 regelt die KI-Management- und Governance-Pflichten. Wo Pflichten überschneiden (z.B. DSGVO Artikel 22 — automatisierte Entscheidungsfindung, oder die Sicherheitsanforderungen der KI-Verordnung für Hochrisiko-KI), hat ISMS-POL-00 Vorrang für die Informationssicherheitsdimension; AI-POL-00 regelt die KI-Governance-Dimension. Datenschutzpflichten aus der KI-Verarbeitung personenbezogener Daten werden in Verbindung mit PRIV-POL-00 behandelt.

**Grundprinzip**: **Die KI-regulatorische Anwendbarkeit muss explizit sein, nicht angenommen.** Verweise auf KI-Regulierungen und -Rahmenwerke fallen in drei Kategorien:

1. **Obligatorische Compliance** — Rechtliche Pflichten, die für die Organisation gelten
2. **Bedingte Anwendbarkeit** — Anforderungen, die nur unter bestimmten Umständen gelten
3. **Informative Referenz** — Best Practices und technische Orientierungen

**Verwendung**: Alle AIMS-Richtlinien MÜSSEN einen Abschnitt „Regulatorischer Rahmen" enthalten, der dieses Dokument referenziert und angibt, welcher Stufe jede zitierte Regulierung oder Norm angehört.

**Schlüsselbegriffe**: Definitionen der in dieser Richtlinie verwendeten Begriffe finden sich im **Glossar** am Ende dieses Dokuments.

---

## Richtlinienautorität und Grenzen

### Zweck und Geltungsbereich dieser Richtlinie

Diese Richtlinie definiert die **Identifikation und Anwendbarkeit** von gesetzlichen, behördlichen, regulatorischen und vertraglichen Anforderungen für das KI-Managementsystem der Organisation.

**Diese Richtlinie legt fest:**

- Welche KI-Gesetze und -Normen für die Organisation gelten
- Kategorisierung der KI-Pflichten (Obligatorisch, Bedingt, Informativ)
- Bewertungsmethodik zur Bestimmung der Anwendbarkeit basierend auf der KI-Rolle der Organisation
- Überprüfungs- und Aktualisierungsprozesse bei Änderungen der KI-Regulierungslandschaft

**Diese Richtlinie legt NICHT fest:**

- KI-Risikobehandlungsentscheidungen (behandelt im AIMS-Risikomanagement)
- Kontrollimplementierungsanforderungen (behandelt in Kontrollgruppen-Richtlinien und IMPs)
- Compliance-Status oder Verifikation (behandelt in Compliance-Überwachungsprozessen)
- Informationssicherheitspflichten (behandelt in ISMS-POL-00)
- Datenschutzpflichten für KI-Verarbeitung personenbezogener Daten (behandelt in PRIV-POL-00)

**Abgrenzungsprinzip**: Diese Richtlinie legt die KI-regulatorische Anwendbarkeit fest. Implementierung, Durchsetzung und Verifikation erfolgen über separate AIMS-Prozesse und Kontrollgruppen-Richtlinien.

**Integration mit ISO/IEC 42001:2023:**

- **Klausel 4.2 (Interessierte Parteien)**: KI-regulatorische Anforderungen bilden die primären Pflichten gegenüber interessierten Parteien. Diese Richtlinie identifiziert sie explizit.
- **Klausel 4.3 (Geltungsbereich)**: Die Geltungsbereichsbestimmung wird durch geltende Stufe-1-Pflichten und die KI-Rolle der Organisation (Anbieter, Betreiber oder beides) bestimmt.
- **Klausel 6 (Risikobewertung)**: Regulatorische Pflichten fliessen in das KI-Risikoregister ein. Stufe 1 = Hohe Priorität, Stufe 2 bedingt = Mittlere Priorität, Stufe 3 = Informativer Beitrag.

**Integration mit ISMS-POL-00 und PRIV-POL-00:**

Diese Richtlinie operiert neben ISMS-POL-00 und PRIV-POL-00. Wenn eine KI-Regulierung Informationssicherheitsdimensionen hat (z.B. KI-Verordnung Artikel 15 — Genauigkeit, Robustheit und Cybersicherheit), regelt ISMS-POL-00 die Sicherheitsinterpretation. Wenn eine KI-Regulierung Datenschutzdimensionen hat (z.B. DSGVO Artikel 22 — automatisierte individuelle Entscheidungsfindung), regelt PRIV-POL-00 die Datenschutzinterpretation. AI-POL-00 regelt die KI-Management- und Governance-Interpretation.

---

## Bestimmung der KI-Rolle der Organisation

**Dieser Schritt muss vor Anwendung des regulatorischen Rahmens abgeschlossen werden.** KI-regulatorische Pflichten unterscheiden sich erheblich je nach Rolle der Organisation in der KI-Wertschöpfungskette.

### Durch die EU-KI-Verordnung (Verordnung 2024/1689) definierte Rollen

| Rolle | Definition | Pflichten |
|-------|-----------|----------|
| **KI-Anbieter** | Entwickelt ein KI-System oder ein KI-Modell mit allgemeinem Verwendungszweck mit der Absicht, es unter eigenem Namen oder Markenzeichen auf den Markt zu bringen oder in Betrieb zu nehmen, auch durch Download | Höchste Pflichtenebene — Konformitätsbewertung, technische Dokumentation, Überwachung nach dem Inverkehrbringen |
| **KI-Betreiber** | Verwendet ein KI-System unter eigener Verantwortung für berufliche Zwecke | Anbieteranweisungen umsetzen, GIFA für Hochrisiko-KI durchführen, Protokolle aufbewahren, menschliche Aufsicht sicherstellen |
| **KI-Importeur** | Bringt auf dem EU-Markt ein KI-System in Verkehr, das den Namen einer ausserhalb der EU ansässigen Einheit trägt | Konformität prüfen, Dokumentation aufbewahren, Behörden melden |
| **KI-Händler** | Stellt ein KI-System auf dem EU-Markt bereit, ohne Anbieter oder Importeur zu sein | CE-Kennzeichnung, Dokumentation, Registrierung prüfen |

### Durch ISO/IEC 42001:2023 definierte Rollen

| Rolle | Definition |
|-------|-----------|
| **KI-Anbieter** | Entwickelt, trainiert, betreibt oder wartet KI-Systeme (für interne oder externe Nutzung) |
| **KI-Nutzer / KI-Betreiber** | Integriert oder verwendet von Dritten entwickelte KI-Systeme |
| **Beides** | Die meisten Unternehmensorganisationen — entwickelt intern KI-Fähigkeiten und nutzt gleichzeitig KI-Tools von Drittanbietern |

**Erforderliche Massnahme**: Die Organisation MUSS ihre Rolle(n) im KI-System-Inventar (AI-POL-01) für jedes KI-System im Geltungsbereich dokumentieren. Rollen können je nach KI-System unterschiedlich sein.

---

## Kategorien der regulatorischen Anwendbarkeit

**Obligatorische Compliance**
Gesetzliche oder vertragliche KI-Pflichten, die die Organisation EINHALTEN MUSS. Nichtkonformität führt zu rechtlicher Haftung, regulatorischen Bussen, Untersuchungen durch Aufsichtsbehörden oder Zertifizierungsverlust.

**Merkmale**:

- Durch eine Regulierungsbehörde oder ein Gericht durchsetzbar
- Nichtkonformität hat rechtliche oder finanzielle Konsequenzen (Bussen, Durchsetzungsverfügungen, Marktzugangsbeschränkungen)
- Erfordert dokumentierte Compliance-Nachweise (Konformitätsbewertungen, technische Dokumentation, Vorfallsprotokoll)
- Unterliegt regulatorischen Audits, Inspektionen und Aufsichtsbefugnissen

**Bedingte Anwendbarkeit**
KI-Anforderungen, die nur bei Erfüllung spezifischer Bedingungen gelten (z.B. spezifische KI-Systemtypen, geografische Marktexposition, angestrebte Zertifizierung, Kundenverträge, regulierte Sektoren).

**Merkmale**:

- Anwendbarkeit hängt von KI-Systemmerkmalen, Einsatzkontext oder Marktgeografie ab
- Kann je nach Geschäftstätigkeit oder vertraglichen Anforderungen obligatorisch werden
- Erfordert regelmässige Neubewertung bei Weiterentwicklung der Geschäftstätigkeit und KI-Systeme

**Informative Referenz / Best-Practice-Ausrichtung**
Rahmenwerke und Normen für technische und organisatorische Orientierung, Benchmarking oder freiwillige Ausrichtung. Sie informieren KI-Governance-Praktiken, stellen jedoch keine obligatorischen Compliance-Anforderungen dar.

**Merkmale**:

- Freiwillige Übernahme für Best Practices
- Kein direkter Rechtsdurchsetzungsmechanismus
- Für Orientierungen zur Implementierung verantwortungsvoller KI verwendet
- Kann obligatorisch werden, wenn in Verträgen oder Zertifizierungsanforderungen referenziert

---

## Compliance-Hierarchie

```
┌─────────────────────────────────────────────────────────────────────┐
│              KI-COMPLIANCE-HIERARCHIE                               │
├─────────────────────────────────────────────────────────────────────┤
│  STUFE 1: OBLIGATORISCH (Rechtlich / Vertraglich)                   │
│  • EU-KI-Verordnung (2024/1689) — bei Inverkehrbringen von KI       │
│    auf dem EU-Markt oder Inbetriebnahme von KI in der EU            │
│  • Sektorspezifische KI-Pflichten (DORA, MiFID II, MDR, etc.)       │
│  • DSGVO Artikel 22 — wenn KI automatisierte Entscheidungen über    │
│    Personen mit rechtlichen oder erheblichen Wirkungen trifft       │
│                                                                     │
│  STUFE 2: BEDINGT (Kontextabhängig)                                 │
│  • ISO/IEC 42001:2023 — wenn Zertifizierung angestrebt oder         │
│    vertraglich gefordert wird                                       │
│  • ISO/IEC 42005:2025 — AISIA-Methodik (Begleitung zu 42001,        │
│    gilt wenn 42001-Zertifizierung im Geltungsbereich ist)           │
│  • Konformitätsbewertungspflichten für Hochrisiko-KI-Systeme        │
│    (wenn klassifiziert unter Anhang III der KI-Verordnung)          │
│  • Nationale KI-Gesetze in Märkten, in denen die Organisation tätig │
│                                                                     │
│  STUFE 3: INFORMATIV (Best Practice / Technische Orientierung)      │
│  • NIST AI Risk Management Framework 1.0 (NIST AI RMF)             │
│  • ISO/IEC 23894:2023 (Orientierungen zum KI-Risikomanagement)     │
│  • ISO/IEC 38507:2022 (Governance von KI)                           │
│  • OECD-KI-Grundsätze (2019, überarbeitet 2024)                     │
│  • UNESCO-Empfehlung zur KI-Ethik (2021)                            │
│  • KI-Strategie des Schweizer Bundesrats (2023)                     │
│                                                                     │
│  BEVORSTEHEND (Beobachten — Übernehmen bei Veröffentlichung)        │
│  • Schweizerische nationale KI-Gesetzgebung (erwartet)              │
│  • ISO/IEC 42006 — AIMS-Interne Audit-Orientierungen (in Entw.)     │
│  • EU-KI-Haftungsrichtlinie (in Entwicklung)                        │
└─────────────────────────────────────────────────────────────────────┘
```

> *Sollten Rahmenzeichnungszeichen nicht korrekt dargestellt werden, beachten Sie die nachfolgenden Abschnitte zu Stufendefinitionen.*

---

# Obligatorische Compliance (Stufe 1)

> **Hinweis zur Klassifikation ISO/IEC 42001:2023**: ISO/IEC 42001:2023 ist in diesem Rahmenwerk als **Stufe 2 (Bedingt)** klassifiziert. Es handelt sich nicht um eine rechtlich durchsetzbare Verordnung. Sie wird für [die Organisation] verbindlich, wenn die Zertifizierung aktiv angestrebt wird oder wenn ein Kundenvertrag AIMS-Compliance mit dieser Norm explizit verlangt. Wenn keine dieser Bedingungen zutrifft, fungiert sie als freiwilliges Best-Practice-Rahmenwerk. Vollständige Details finden sich im Abschnitt ISO/IEC 42001:2023 unter Stufe 2.

## EU-Verordnung über Künstliche Intelligenz (Verordnung 2024/1689)

**Anwendbarkeit**: Bei Inverkehrbringen eines KI-Systems auf dem EU-Markt, Inbetriebnahme eines KI-Systems in der EU, oder wenn Ausgaben von KI-Systemen in der EU verwendet werden — unabhängig vom Sitz der Organisation. Gilt vollständig ab dem 2. August 2026 (mit Verboten für KI-Praktiken ab dem 2. Februar 2025, GPAI-Bestimmungen ab dem 2. August 2025).

**Risikoklassifikationsrahmen**:

Die EU-KI-Verordnung wendet einen risikobasierten Ansatz an. Jedes KI-System muss klassifiziert werden:

| Risikoniveau | Definition | Pflichten |
|-------------|-----------|----------|
| **Unannehmbares Risiko** (Verboten) | KI-Systeme, die eine klare Bedrohung für Grundrechte oder die Sicherheit darstellen | Absolutes Verbot — darf nicht auf den Markt gebracht werden. Beispiele: unterschwellige Manipulation, Sozialkreditbewertung, Echtzeit-Fernbiometrie-Identifikation im öffentlichen Raum (ausser engen Strafverfolgungsausnahmen), Ausnutzung von Vulnerabilitäten aufgrund von Alter/Behinderung |
| **Hochrisiko** (Anhang III) | KI-Systeme in regulierten Sektoren oder mit erheblichen Auswirkungen auf Grundrechte | Vollständige Konformitätspflichten — siehe unten |
| **Begrenztes Risiko** | KI-Systeme mit spezifischen Transparenzpflichten | Nutzer über KI-Interaktion informieren (Chatbots, Deepfakes) |
| **Minimales Risiko** | Alle anderen KI-Systeme | Keine obligatorischen Anforderungen; freiwillige Verhaltenskodizes |
| **KI mit allgemeinem Verwendungszweck (GPAI)** | KI-Modelle mit allgemeinen Fähigkeiten (z.B. grosse Sprachmodelle) | Transparenz, Urheberrechts-Compliance; Modelle mit systemischem Risiko haben zusätzliche Pflichten |

**Hochrisiko-KI-Systemkategorien (Anhang III)**:

- Biometrische Identifizierung und Kategorisierung
- Verwaltung und Betrieb kritischer Infrastrukturen
- Bildung und Berufsausbildung (Zugang, Bewertung)
- Beschäftigung, Personalmanagement und Zugang zu selbstständiger Tätigkeit
- Zugang zu und Inanspruchnahme wesentlicher privater und öffentlicher Dienste und Leistungen
- Strafverfolgung
- Migration, Asyl und Grenzkontrollverwaltung
- Rechtspflege und demokratische Prozesse

**Wesentliche Anforderungen für Hochrisiko-KI-Anbieter**:

- Artikel 9: Qualitätsmanagementsystem (QMS) einschliesslich Risikomanagement
- Artikel 10: Anforderungen an Trainings-, Validierungs- und Testdaten
- Artikel 11: Technische Dokumentation (vor Inverkehrbringen)
- Artikel 12: Aufzeichnungspflichten (Protokollierung während der gesamten Betriebslebensdauer)
- Artikel 13: Transparenz und Informationsbereitstellung für Betreiber
- Artikel 14: Massnahmen zur menschlichen Aufsicht
- Artikel 15: Anforderungen an Genauigkeit, Robustheit und Cybersicherheit
- Artikel 16: Anbieterpflichten (Registrierung, CE-Kennzeichnung, Überwachung nach dem Inverkehrbringen)
- Artikel 26: Betreiberpflichten (Grundrechte-Folgenabschätzung für öffentliche Stellen und bestimmte private Betreiber)

**Wesentliche Anforderungen für GPAI-Modellanbieter**:

- Artikel 53: Transparenz und Urheberrechts-Compliance (technische Dokumentation, Trainingsdatenzusammenfassung)
- Artikel 55: Modelle mit systemischem Risiko (gegnerische Tests, Vorfallsmeldung, Cybersicherheitsmassnahmen)

**Auswirkungen auf das AIMS**:

- Das KI-System-Inventar muss jedes System nach der Risikokategorie der EU-KI-Verordnung klassifizieren
- Hochrisiko-Systeme erfordern eine Konformitätsbewertung vor der EU-Marktplatzierung
- Technische Dokumentation gemäss Artikel-11-Anforderungen aufrechtzuerhalten
- AISIA (A.5.2–A.5.5) ist auf die Grundrechte-Folgenabschätzung (GIFA) für Hochrisiko-KI ausgerichtet
- A.6.2.6 (Betrieb und Überwachung) muss Überwachungspflichten nach dem Inverkehrbringen behandeln
- A.8.4 (Kommunikation von Vorfällen) muss die Meldefristen für schwerwiegende Vorfälle der EU-KI-Verordnung behandeln

**Aufsichtsbehörde**: Nationale Marktüberwachungsbehörde jedes EU-Mitgliedstaates; Europäisches KI-Büro (Europäische Kommission) für GPAI-Modelle

**Referenz**: Verordnung (EU) 2024/1689, Amtsblatt der EU, 12. Juli 2024. Anwendungsdaten: verbotene KI-Praktiken ab 2. Februar 2025; GPAI-Bestimmungen ab 2. August 2025; vollständige Anwendung ab 2. August 2026.

---

## DSGVO Artikel 22 — Automatisierte Entscheidungsfindung

**Anwendbarkeit**: Wenn die Organisation KI-Systeme verwendet, um **vollständig automatisierte Entscheidungen** zu treffen, die **rechtliche Wirkungen** haben oder **Personen erheblich beeinflussen** (z.B. automatisiertes Credit-Scoring, automatisiertes Bewerberscreening, automatisierte Leistungsberechtigung, automatisierte Betrugserkennung mit Kontosperrung).

**Wesentliche Anforderungen**:

- Recht, nicht einer vollständig automatisierten Entscheidung mit rechtlichen oder erheblichen Wirkungen unterworfen zu werden (Artikel 22(1))
- Ausnahmen: ausdrückliche Einwilligung, Vertragsnotwendigkeit oder nach Unionsrecht oder nationalem Recht zulässig — alle erfordern Schutzgarantien
- Bei geltenden Ausnahmen: Personen informieren, bedeutsame menschliche Aufsicht implementieren, Recht zur Anfechtung der Entscheidung und zur Erlangung menschlicher Überprüfung vorsehen
- DSFA für systematische automatisierte Verarbeitung erforderlich, die voraussichtlich zu hohem Risiko führt (Artikel 35)

**Auswirkungen auf das AIMS**:

- KI-Systeme, die wichtige automatisierte Entscheidungen treffen, müssen im KI-System-Inventar identifiziert werden
- Obligatorische Kontrollen zur menschlichen Aufsicht (A.6.2.6) für KI-gesteuerte Entscheidungen, die Personen betreffen
- Transparenzoffenlegungen (A.8.2, A.8.5) müssen die Informationspflichten aus DSGVO Artikel 22 erfüllen
- Verweis auf PRIV-POL-00 und PRIV-POL-A.1.3.11 (Automatisierte Entscheidungsfindung) für vollständige Datenschutzpflichten

**Aufsichtsbehörde**: Zuständige EU/EWR-Datenschutzbehörde (DSB)

**Referenz**: Verordnung (EU) 2016/679 Artikel 22; Leitlinien 05/2020 zur automatisierten Einzelentscheidung und Profilerstellung (EDPB)

---

## Sektorspezifische KI-Pflichten

Bestimmte regulierte Sektoren stellen KI-spezifische Pflichten zusätzlich zur EU-KI-Verordnung auf. Die Anwendbarkeit hängt vom Sektor und den Tätigkeiten der Organisation ab.

**Finanzdienstleistungen — DORA (Verordnung 2022/2554)**:

- Artikel 28–30: IKT-Drittparteien-Risikomanagement gilt für KI-Tools und KI-Dienstanbieter
- DORA klassifiziert KI-Tools in kritischen Funktionen als IKT-Drittparteienabhängigkeiten mit vollständigen TPRM-Pflichten
- KI-Systeme im Handel, Risikomanagement oder Kundendienst sind für die Meldung von IKT-Vorfällen relevant
- **Anwendbarkeitsauslöser**: Organisation ist ein DORA-reguliertes Unternehmen (Finanzinstitut, Wertpapierfirma, Versicherungsunternehmen, Krypto-Asset-Dienstleister, etc.)

**Medizinprodukte — MDR (Verordnung 2017/745) und IVDR (Verordnung 2017/746)**:

- KI-gestützte Medizinprodukte und In-vitro-Diagnostika unterliegen der MDR/IVDR-Konformitätsbewertung
- KI-Medizinprodukte-Software (SaMD) kann sowohl nach MDR als auch nach EU-KI-Verordnung als Hochrisiko klassifiziert werden — doppelte Konformitätsbewertung kann erforderlich sein
- **Anwendbarkeitsauslöser**: Organisation entwickelt oder bringt KI-gestützte Medizinprodukte oder Diagnosesoftware in Verkehr

**Luftfahrt, Automobil, Schiene, Maritime (CE-Kennzeichnungsregime)**:

- KI-Systeme in sicherheitskritischen Produkten, die nach bestehender Produktsicherheitsgesetzgebung reguliert sind, können eine doppelte Konformität nach EU-KI-Verordnung und sektorspezifischer Regulierung erfordern
- **Anwendbarkeitsauslöser**: Organisation entwickelt KI-Systeme, die in sicherheitskritische Produkte in diesen Sektoren integriert sind

**Erforderliche Massnahme**: Legal/Compliance MUSS die sektorspezifischen KI-Pflichten jährlich bewerten und die Anwendbarkeitsfeststellungen im regulatorischen Register dokumentieren.

---

# Bedingte Anwendbarkeit (Stufe 2)

Diese Vorschriften und Normen gelten **nur bei Erfüllung spezifischer Bedingungen**.

## ISO/IEC 42001:2023 — KI-Managementsystem

**Norm**: ISO/IEC 42001:2023 (Erste Ausgabe) — Informationstechnologie — Künstliche Intelligenz — Managementsystem

**Anwendbarkeitsauslöser**:

- Die Organisation **strebt die ISO/IEC 42001:2023-Zertifizierung an** (eigenständig oder kombiniert mit ISO 27001)
- Ein Kundenvertrag **verlangt explizit** AIMS-Compliance mit dieser Norm
- Die Organisation **übernimmt ISO 42001 freiwillig** als KI-Governance-Rahmenwerk (in diesem Fall als operativ verbindlich behandeln)

**Klassifikationshinweis**: ISO/IEC 42001:2023 ist in diesem Rahmenwerk als Stufe 2 (Bedingt) klassifiziert. Es handelt sich nicht um eine rechtlich durchsetzbare Verordnung. Sie wird nicht allein dadurch obligatorisch, dass die Organisation KI-Systeme entwickelt oder verwendet — die EU-KI-Verordnung erfüllt diese Funktion für die EU-Marktexposition. Wenn Zertifizierung angestrebt oder vertraglich gefordert wird, wird sie als verbindliche operative Verpflichtung gleichwertig zu Stufe 1 für die Dauer der Zertifizierung behandelt.

**Wesentliche Anforderungen**:

- Klausel 4: Kontext der Organisation (Kontextverständnis, interessierte Parteien, AIMS-Geltungsbereich)
- Klausel 5: Führung (KI-Politik, Rollen und Verantwortlichkeiten, Managementverpflichtung)
- Klausel 6: Planung (KI-Risikobewertung, KI-System-Folgenabschätzung, KI-Ziele)
- Klausel 7: Unterstützung (Ressourcen, Kompetenz, Bewusstsein, Kommunikation, dokumentierte Informationen)
- Klausel 8: Betrieb (Betriebsplanung, Durchführung der KI-Risikobewertung, Risikobehandlung, AISIA-Durchführung)
- Klausel 9: Leistungsbewertung (Überwachung, internes Audit, Managementbewertung)
- Klausel 10: Verbesserung (Nichtkonformität, Korrekturmassnahme, kontinuierliche Verbesserung)
- Anhang A (normativ): 36 Massnahmen in 9 Domänen (A.2–A.10)
- Anhang B (normativ): Umsetzungsleitfaden für alle Massnahmen des Anhangs A

**AIMS-Bereitstellung**: Das vollständige ISO 42001 Anhang A-Massnahmenset wird durch die AI-POL-A.x.x-Kontrollgruppen-Richtlinien in `53-isms-core-ai/` bereitgestellt. Die Anwendbarkeitserklärung (SoA) der Organisation MUSS diese Richtlinien referenzieren.

**Integration mit ISO 27001**: ISO 42001 verwendet die gleiche Struktur der hohen Ebene (HLS/Anhang SL) wie ISO 27001:2022. Organisationen mit ISO 27001-Zertifizierung können AIMS- und ISMS-Prozesse unter einem gemeinsamen Managementsystem integrieren oder kombinieren. Gemeinsame Klauselbereiche (7, 9, 10) können bestehende ISMS-Infrastruktur wiederverwenden.

**Referenz**: ISO/IEC 42001:2023, Informationstechnologie — Künstliche Intelligenz — Managementsystem, Dezember 2023

---

## ISO/IEC 42005:2025 — KI-System-Folgenabschätzung

**Norm**: ISO/IEC 42005:2025 (Erste Ausgabe) — Informationstechnologie — Künstliche Intelligenz — KI-System-Folgenabschätzung

**Anwendbarkeitsauslöser**:

- ISO/IEC 42001:2023 ist im Geltungsbereich (obiger Stufe-2-Auslöser gilt) — ISO 42005:2025 liefert die Methodik für ISO 42001 Klausel 6.1.4 (KI-System-Folgenabschätzung) und Anhang-A-Massnahmen A.5.2–A.5.5
- Die Organisation übernimmt AISIA formal als Teil ihres KI-Governance-Programms
- Kundenverträge oder regulatorische Pflichten (z.B. GIFA-Anforderungen der EU-KI-Verordnung) erfordern eine dokumentierte KI-Folgenabschätzungsmethodik

**Was ISO 42005:2025 abdeckt**:

- Klausel 5: Entwicklung und Implementierung des AISIA-Prozesses (Geltungsbereich, Schwellenwerte, sensible Verwendungen, eingeschränkte Verwendungen, Auswirkungsskalen, Verantwortlichkeiten, Genehmigung, Überwachung und Überprüfung)
- Klausel 6: Dokumentation der KI-System-Folgenabschätzung (KI-Systembeschreibung, Funktionen und Fähigkeiten, Verwendungszweck, Dateninformationen und -qualität, Algorithmus- und Modellinformationen, Einsatzumgebung, betroffene Parteien, tatsächliche und vernünftigerweise vorhersehbare Auswirkungen, Nutzen und Schäden, Massnahmen zur Schadensbehebung)
- Anhang A (informativ): Orientierungen für die Verwendung mit ISO/IEC 42001
- Anhang B (informativ): Orientierungen für die Verwendung mit ISO/IEC 23894 (KI-Risikomanagement)

**Auswirkungen auf das AIMS**:

- Alle AISIA-Vorlagen in `53-isms-core-ai/` MÜSSEN gemäss den Dokumentationsanforderungen von ISO 42005:2025 Klausel 6 erstellt werden
- Die AISIA-Methodik in AIMS-Dokumenten muss ISO 42005:2025 referenzieren, nicht allgemeine Orientierungen
- Die ISO 42005:2025 AISIA ist auf die Grundrechte-Folgenabschätzung (GIFA) der EU-KI-Verordnung ausgerichtet — Organisationen, die beiden unterliegen, SOLLTEN die Querverweise dokumentieren

**Referenz**: ISO/IEC 42005:2025, Informationstechnologie — Künstliche Intelligenz — KI-System-Folgenabschätzung, Mai 2025

---

## Konformitätsbewertung für Hochrisiko-KI-Systeme (EU-KI-Verordnung)

**Anwendbarkeitsauslöser**: Die Organisation handelt als KI-Anbieter oder KI-Betreiber für ein KI-System, das als **Hochrisiko** gemäss Anhang III der EU-KI-Verordnung klassifiziert ist.

**Zusätzlich ausgelöste Pflichten**:

- Konformitätsbewertungsverfahren (Artikel 43) — entweder interne Kontrolle oder Drittparteienbewertung (benannte Stelle) je nach KI-Systemkategorie
- Registrierung in der EU-KI-Verordnungsdatenbank (Artikel 49) vor der Marktplatzierung
- CE-Kennzeichnung und Konformitätserklärung
- Überwachungssystem nach dem Inverkehrbringen (Artikel 72)
- Meldung schwerwiegender Vorfälle an die nationale Behörde (Artikel 73) innerhalb definierter Fristen

**Erforderliche Massnahme**: Für jedes KI-System im Geltungsbereich des EU-Markts nach EU-KI-Verordnungsrisikokategorien klassifizieren und im KI-System-Inventar dokumentieren. Hochrisiko-Klassifikation löst Konformitätsbewertungsplanung aus.

---

# Informative Referenz (Stufe 3)

Diese Rahmenwerke informieren KI-Governance-Praktiken, stellen jedoch keine obligatorischen Compliance-Anforderungen dar. Sie werden für Orientierung, Benchmarking und Best-Practice-Implementierung verwendet.

## NIST AI Risk Management Framework 1.0 (NIST AI RMF)

**Veröffentlicht**: Januar 2023 — National Institute of Standards and Technology (USA)

**Relevanz**: Bietet ein freiwilliges Rahmenwerk für das KI-Risikomanagement mit vier Kernfunktionen: GOVERN, MAP, MEASURE, MANAGE. International als praktische KI-Risikomanagement-Referenz anerkannt, auch ausserhalb der USA.

**Verwendung im AIMS**:

- Die Struktur des KI-Risikoregisters wird durch die NIST AI RMF-Risikotaxonomie (GOVERN, MAP, MEASURE, MANAGE) informiert
- Das NIST AI RMF-Profilkonzept unterstützt die organisationsspezifische KI-Risikopriorisierung
- Querverweise: NIST AI RMF ↔ ISO 42001-Zuordnungen unterstützen Organisationen mit dualem Rahmenwerk

**Referenz**: NIST AI RMF 1.0, NIST AI 100-1, Januar 2023

---

## ISO/IEC 23894:2023 — KI-Risikomanagement

**Veröffentlicht**: Februar 2023

**Relevanz**: Bietet Orientierungen, wie Organisationen Risiken im Zusammenhang mit KI managen können. Erweitert ISO 31000 (Risikomanagement) um KI-spezifische Überlegungen. Referenziert in ISO 42001 Anhang B und ISO 42005 Anhang B.

**Verwendung im AIMS**:

- Die KI-Risikobewertungsmethodik wird durch ISO 23894-Risikoidentifikations- und -analyseorientierungen informiert
- Die KI-Risikotaxonomie wird durch ISO 23894-Kategorien informiert (technisch, operativ, gesellschaftlich)

**Referenz**: ISO/IEC 23894:2023, Informationstechnologie — Künstliche Intelligenz — Orientierungen zum Risikomanagement

---

## ISO/IEC 38507:2022 — KI-Governance für Organisationen

**Veröffentlicht**: April 2022

**Relevanz**: Bietet Orientierungen zu den Governance-Implikationen der KI-Nutzung durch Organisationen. Behandelt, wie Mitglieder des Leitungsorgans KI-Governance ermöglichen, erweitern und weiterentwickeln können. Referenziert in ISO 42001 Anhang B.2.3.

**Verwendung im AIMS**:

- Die Governance-Struktur für KI (A.3.2) wird durch ISO 38507-KI-Governance-Orientierungen auf Vorstandsebene informiert
- Das Rechenschaftsrahmenwerk der Geschäftsleitung ist an ISO 38507-Grundsätzen ausgerichtet

**Referenz**: ISO/IEC 38507:2022, Informationstechnologie — Künstliche Intelligenz — Governance-Implikationen der KI-Nutzung durch Organisationen

---

## OECD-KI-Grundsätze (2019, überarbeitet 2024)

**Veröffentlicht**: Mai 2019 (überarbeitet Juni 2024) — Organisation für wirtschaftliche Zusammenarbeit und Entwicklung

**Relevanz**: Internationale Referenz für verantwortungsvolle KI. Vom G20 übernommen. In nationaler KI-Gesetzgebung einschliesslich der EU-KI-Verordnung weitgehend referenziert. Fünf Grundsätze: inklusives Wachstum und Wohlbefinden; menschenzentrierte Werte und Fairness; Transparenz und Erklärbarkeit; Robustheit und Sicherheit; Rechenschaftspflicht.

**Verwendung im AIMS**:

- Die Grundsätze verantwortungsvoller KI in AI-POL-01 sind an den OECD-KI-Grundsätzen ausgerichtet
- Die Erwägungsgründe der EU-KI-Verordnung referenzieren die OECD-Grundsätze — Ausrichtung reduziert Auslegungslücken

**Referenz**: OECD-KI-Grundsätze, OECD/LEGAL/0449, angenommen am 22. Mai 2019, überarbeitet 2024

---

## KI-Strategie des Schweizer Bundesrats (2023)

**Veröffentlicht**: Dezember 2023 — Schweizer Bundesrat

**Relevanz**: Die Schweizer Regierungs-KI-Strategie legt Grundsätze für verantwortungsvolle KI in der öffentlichen Verwaltung fest und gibt die Richtung für zukünftige Schweizer KI-Gesetzgebung vor. Nicht rechtsverbindlich für den Privatsektor Stand April 2026.

**Schweizer Kontext**: Die Schweiz hat Stand April 2026 kein eigenständiges nationales KI-Gesetz erlassen. Die KI-Governance für Privatsektor-Organisationen wird hauptsächlich durch folgendes geregelt:

- Schweizer nDSG (Bundesgesetz über den Datenschutz, SR 235.1) — gilt für KI-Verarbeitung personenbezogener Daten
- Schweizer ISG (Bundesgesetz über die Informationssicherheit, SR 128) — gilt für KI-Systeme in kritischer nationaler Infrastruktur
- KI-Strategie des Schweizer Bundesrats — freiwillige Grundsätze
- EU-KI-Verordnung — gilt für Schweizer Organisationen, die KI auf dem EU-Markt platzieren

**Beobachten**: Schweizer nationale KI-Gesetzgebung wird erwartet, dem EU-KI-Verordnungsrahmen zu folgen. Überwachungsverantwortung Legal/Compliance zuweisen.

---

# Bevorstehend (Beobachten — Übernehmen bei Veröffentlichung oder Inkrafttreten)

Diese Instrumente befinden sich in der Entwicklung oder werden erwartet. [Die Organisation] MUSS diese beobachten und bei Veröffentlichung oder Inkrafttreten übernehmen.

| Instrument | Status | Erwartete Auswirkung |
|-----------|--------|---------------------|
| **Schweizerische nationale KI-Gesetzgebung** | Erwartet — kein Entwurf veröffentlicht Stand April 2026 | Wahrscheinlich Ausrichtung an EU-KI-Verordnung für CH-Markt-KI-Systeme; AIMS bereits ausgerichtet |
| **ISO/IEC 42006** — Anforderungen für das Auditieren von KI-Managementsystemen | In Entwicklung (ISO/IEC JTC 1/SC 42) | Definiert interne/externe AIMS-Auditanforderungen — AIMS-Auditprogramm bei Veröffentlichung aktualisieren |
| **EU-KI-Haftungsrichtlinie** | In Entwicklung | Kann zivilrechtliche Haftung für KI-Systemschäden einführen; löst Aktualisierungen des AIMS-Risikoregisters aus |
| **Delegierte Rechtsakte der EU-KI-Verordnung** | Erwartet 2025–2026 | Technische Details für Konformitätsbewertung, Normungsmandate, GPAI-Modellschwellenwerte |
| **NIST AI RMF 2.0 / Sektorprofile** | Periodisch erwartet | NIST AI RMF Stufe-3-Referenz bei Veröffentlichung aktualisieren |

**Überwachungsverantwortung**: Rechtsbeauftragter/Compliance-Beauftragter mit Unterstützung des KI-Governance-Beauftragten (KI-GB). Überprüfungszyklus: vierteljährliche Überprüfung, jährliche Richtlinienaktualisierung bei Bedarf.

---

# Bewertungs- und Überprüfungsprozess

## Bestimmung der Anwendbarkeit

Für jedes neu entwickelte oder beschaffte KI-System und bei jedem jährlichen Überprüfungszyklus MÜSSEN der KI-Governance-Beauftragte (KI-GB) und Legal/Compliance:

1. **Die KI-Rolle der Organisation** für das System identifizieren (Anbieter, Betreiber, beides) gemäss den obigen Rollendefinitionen
2. **Stufe-1-Anwendbarkeit bewerten** — Risikoklassifikation nach EU-KI-Verordnung; DSGVO Artikel-22-Auslöser; sektorspezifische Auslöser
3. **Stufe-2-Auslöser bewerten** — Wird ISO 42001-Zertifizierung angestrebt oder vertraglich gefordert? Ist das System nach EU-KI-Verordnung Hochrisiko und erfordert eine Konformitätsbewertung?
4. **Stufe-3-Relevanz überprüfen** — Dokumentieren, welche informativen Rahmenwerke die Implementierung für das System informieren
5. **Das KI-System-Inventar aktualisieren** (AI-POL-01) mit regulatorischen Klassifikationsfeststellungen
6. **Die AIMS-SoA aktualisieren**, wenn neue Pflichten die Kontrollauswahl beeinflussen

## Jährliche Überprüfung

Diese Richtlinie MUSS jährlich vom KI-Governance-Beauftragten und Legal/Compliance überprüft werden. Auslöser für Überprüfung ausserhalb des Zyklus:

- Neue KI-Vorschriften in einer Jurisdiktion erlassen, in der die Organisation tätig ist
- Neue KI-Norm veröffentlicht, die das AIMS-Kontrollrahmenwerk beeinflusst
- Wesentliche Änderung im KI-Portfolio der Organisation (neues KI-System in Hochrisikoklasse)
- Regulatorische Durchsetzungsmassnahme gegen eine Peer-Organisation, die eine neue Pflichteninterpretation aufzeigt

---

# Glossar

| Begriff | Definition |
|---------|-----------|
| **KI-Verordnung** | EU-Verordnung über Künstliche Intelligenz — Verordnung (EU) 2024/1689 über künstliche Intelligenz |
| **KI-Betreiber** | Natürliche oder juristische Person, die ein KI-System unter eigener Verantwortung für berufliche Zwecke verwendet (Definition EU-KI-Verordnung) |
| **KI-Anbieter** | Person oder Einheit, die ein KI-System oder ein GPAI-Modell mit Absicht der EU-Marktplatzierung entwickelt (Definition EU-KI-Verordnung) |
| **KI-System** | Maschinenbasiertes System, das so konzipiert ist, dass es mit unterschiedlichem Masse an Autonomie betrieben wird, das adaptives Verhalten zeigen kann und das — für explizite oder implizite Ziele — aus erhaltenen Eingaben ableitet, wie es Ausgaben wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen generiert (ISO/IEC 42001:2023-Definition, ausgerichtet an Artikel 3 der EU-KI-Verordnung) |
| **AIMS** | KI-Managementsystem — Managementsystem für die verantwortungsvolle Entwicklung, den Einsatz und die Nutzung von KI-Systemen |
| **AISIA** | KI-System-Folgenabschätzung — formale Bewertung der potenziellen Folgen eines KI-Systems für Personen und Gesellschaften (ISO/IEC 42001:2023 Klausel 6.1.4; detailliert in ISO/IEC 42005:2025) |
| **GIFA** | Grundrechte-Folgenabschätzung — gemäss Artikel 26 der EU-KI-Verordnung für Betreiber bestimmter Hochrisiko-KI-Systeme erforderlich, die natürliche Personen betreffen |
| **GPAI** | KI mit allgemeinem Verwendungszweck — KI-Modell, das auf umfangreichen Daten trainiert wurde und mehrere Aufgaben erfüllen kann (z.B. grosse Sprachmodelle); unterliegt spezifischen Pflichten gemäss Titel V der EU-KI-Verordnung |
| **Hochrisiko-KI** | KI-System der Anhang-III-Kategorien der EU-KI-Verordnung, das vollständigen Konformitätspflichten vor der EU-Marktplatzierung unterliegt |
| **Obligatorisch** | Stufe 1 — rechtlich oder vertraglich durchsetzbare Pflicht mit Konsequenzen bei Nichtkonformität |
| **Bedingt** | Stufe 2 — Pflicht, die bei Erfüllung spezifischer Auslöser anwendbar wird |
| **Informativ** | Stufe 3 — freiwilliges Best-Practice-Rahmenwerk, das die AIMS-Implementierung ohne direkte Durchsetzung informiert |
| **SoA** | Anwendbarkeitserklärung — Dokument, das alle 36 ISO 42001 Anhang-A-Massnahmen mit Anwendbarkeitsentscheidungen und Begründungen auflistet |
| **Systemisches Risiko** | Risiko im Zusammenhang mit GPAI-Modellen mit sehr hoher Trainingsrechenleistung (≥10^25 FLOPs), das nachteilige Auswirkungen auf EU-Ebene verursacht |

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
