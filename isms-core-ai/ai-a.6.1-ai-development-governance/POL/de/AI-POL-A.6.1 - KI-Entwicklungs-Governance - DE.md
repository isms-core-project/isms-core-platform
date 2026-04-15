<!-- ISMS-CORE:POLICY:AI-POL-A.6.1-DE:ai:POL:a.6.1 -->
**AI-POL-A.6.1 — KI-Entwicklungs-Governance**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumenttitel** | KI-Entwicklungs-Governance |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | AI-POL-A.6.1 |
| **Dokumentersteller** | KI-Governance-Beauftragter (KI-GB) / Technischer Direktor (CTO) |
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
| 1.0 | [Datum festzulegen] | KI-GB / CTO | Erstrichtlinie für die ISO/IEC 42001:2023-Erstzertifizierung |

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen der KI-Entwicklungsmethodik oder verantwortungsvoller KI-Standards)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: KI-Governance-Beauftragter (KI-GB)
- Sekundär: Technischer Direktor (CTO) / KI-Engineering-Leiter
- Compliance: Informationssicherheitsbeauftragter (ISB)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- AI-POL-00 (AIMS — Regulatorischer Anwendbarkeitsrahmen für KI)
- AI-POL-01 (KI-Governance und Entscheidungsrahmen AIMS)
- AI-POL-A.5.2-5 (KI-System-Folgenabschätzung — AISIA steuert die Massnahmenauswahl)
- AI-POL-A.6.2 (KI-System-Lebenszyklus — operative Lebenszyklus-Kontrollen)
- AI-IMP-A.6.1-UG (KI-Entwicklungs-Governance — Benutzerhandbuch)
- AI-IMP-A.6.1-TG (KI-Entwicklungs-Governance — Technischer Leitfaden)
- ISO/IEC 42001:2023 Massnahmen A.6.1.2, A.6.1.3
- ISO/IEC 42001:2023 Anhang B.6.1 (Umsetzungshinweise — Governance der KI-Systementwicklung)

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen der [Organisation] für die Identifizierung und Integration verantwortungsvoller Entwicklungsziele sowie für die Definition und Dokumentation der Prozesse fest, mit denen KI-Systeme verantwortungsvoll konzipiert und entwickelt werden — in Übereinstimmung mit den ISO/IEC 42001:2023-Massnahmen A.6.1.2 und A.6.1.3.

**Anwendungsbereich**: Alle von der [Organisation] entwickelten KI-Systeme (Rolle als KI-Anbieter); die Ziele, Prozesse und Governance-Praktiken, die den Entwicklungslebenszyklus von der Konzeption bis zur Übergabe für den Einsatz leiten.

**Hinweis zur Anwendbarkeit**: Die A.6.1-Massnahmen gelten primär für Organisationen, die als **KI-Anbieter** tätig sind — jene, die KI-Systeme entwickeln, trainieren oder anderweitig erstellen. Organisationen, die ausschliesslich als KI-Betreiber tätig sind (Nutzung von Dritt-KI ohne Modifikation), müssen dies in der AIMS-SoA dokumentieren und A.6.1 anwenden, wo sie wesentlichen Einfluss auf das Design oder die Konfiguration des KI-Systems haben.

**Zweck**: Festlegen, WELCHE verantwortungsvollen Entwicklungsziele definiert und dokumentiert werden müssen (A.6.1.2), und WELCHE Prozesse für verantwortungsvolles Design und Entwicklung definiert werden müssen (A.6.1.3). Die Umsetzung ist in AI-IMP-A.6.1-UG und AI-IMP-A.6.1-TG beschrieben.

**Begründung der zusammengefassten Massnahmen**: A.6.1.2 und A.6.1.3 bilden die strategische und prozedurale Governance-Ebene für die KI-Entwicklung. Ziele (A.6.1.2) legen die Grundsätze verantwortungsvoller KI fest, die in den Entwicklungszyklus integriert werden müssen; Prozesse (A.6.1.3) definieren WIE diese Grundsätze operativ umgesetzt werden. Beide Massnahmen müssen gemeinsam angewendet werden, um eine wirksame Entwicklungs-Governance zu gewährleisten.

---

## Anwendungsbereich und Geltungsbereich

### ISO/IEC 42001:2023-Massnahmen

**Massnahme A.6.1.2 — Ziele für die verantwortungsvolle Entwicklung von KI-Systemen**
Die Organisation muss Ziele zur Leitung der verantwortungsvollen Entwicklung von KI-Systemen identifizieren und dokumentieren sowie diese Ziele berücksichtigen und Massnahmen zu ihrer Erreichung in den Entwicklungslebenszyklus integrieren.

**Massnahme A.6.1.3 — Prozesse für verantwortungsvolles KI-Systemdesign und -entwicklung**
Die Organisation muss die spezifischen Prozesse für das verantwortungsvolle Design und die Entwicklung des KI-Systems definieren und dokumentieren.

### Was diese Richtlinie abdeckt

- Ziele für verantwortungsvolle KI-Entwicklung, die pro KI-System festzulegen sind
- Prozessanforderungen für verantwortungsvolles KI-Design und -entwicklung
- Integration von AISIA-Ergebnissen in die Entwicklungs-Governance
- Checkpoints für verantwortungsvolle KI im gesamten Entwicklungslebenszyklus

### Was diese Richtlinie NICHT abdeckt

- Operative Lebenszyklus-Kontrollen (Anforderungen, V&V, Deployment, Monitoring — geregelt in AI-POL-A.6.2)
- Datenverwaltungsprozesse (geregelt in AI-POL-A.7.2-6)
- Konformitätsbewertungsverfahren gemäss EU-KI-Verordnung (geregelt in AI-POL-A.8.2-5 und AI-POL-00)

### Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss AI-POL-00):

- **EU-KI-Verordnung (Verordnung 2024/1689)**: Artikel 9 — Anbieter von Hochrisiko-KI müssen ein Qualitätsmanagementsystem einrichten, das Ziele für verantwortungsvolle KI umfasst; Artikel 9(1)(b) — Methodik für Design und Entwicklung; Artikel 10 — Anforderungen an Training, Validierung und Testing für verantwortungsvolle Entwicklung

**Stufe 2: Bedingt** (gemäss AI-POL-00):

- **ISO/IEC 42001:2023**: Massnahmen A.6.1.2, A.6.1.3 — gilt, wenn die AIMS-Zertifizierung im Scope liegt oder vertraglich gefordert ist

**Stufe 3: Informativ** (gemäss AI-POL-00):

- NIST AI RMF: GOVERN 4.x — organisatorische KI-Entwicklungspraktiken; MAP 2.x — Impact-Identifikation in der Entwicklung
- ISO/IEC 23894:2023: Risikomanagementserwägungen während der KI-Entwicklung

---

## Richtlinienaussagen: Ziele für verantwortungsvolle Entwicklung (A.6.1.2)

### Anforderung an Ziele für verantwortungsvolle Entwicklung

Die [Organisation] MUSS Ziele für die verantwortungsvolle Entwicklung jedes KI-Systems identifizieren und dokumentieren. Diese Ziele müssen:

- Vor Entwicklungsbeginn festgelegt werden (nicht rückwirkend)
- Die Grundsätze verantwortungsvoller KI in der KI-Richtlinie (AI-POL-A.2.2-4) widerspiegeln
- Durch die AISIA-Ergebnisse für das KI-System informiert werden (AI-POL-A.5.2-5)
- Als messbare Designkriterien in den Entwicklungslebenszyklus integriert werden, nicht als Wunschvorstellungen
- Vom KI-GB vor Entwicklungsbeginn genehmigt werden

### Kerneigenschaften verantwortungsvoller Entwicklung

Die folgenden Eigenschaften verantwortungsvoller KI müssen als Ziele für jedes von der [Organisation] entwickelte KI-System berücksichtigt werden. Anwendbarkeit und Umsetzungstiefe werden durch die AISIA-Folgenklassifizierung (Niedrig / Mittel / Hoch) bestimmt:

**Fairness und Nichtdiskriminierung**

Das KI-System muss Einzelpersonen und Gruppen gleichmässig behandeln. Die Ziele müssen spezifizieren:

- Welche demografischen Gruppen oder geschützten Merkmale für die Fairness-Bewertung relevant sind
- Welche Fairness-Metrik(en) für den Anwendungsfall geeignet sind (z. B. demografische Parität, Equalised Odds, prädiktive Parität)
- Akzeptable Schwellenwerte für Fairness-Metriken vor dem Deployment — Schwellenwerte werden vom KI-GB in Absprache mit dem CTO und der relevanten Fachexpertise festgelegt, in der AISIA dokumentiert und vor Beginn der V&V genehmigt
- Prozess zur Fairness-Überwachung im Betrieb (A.6.2.6)

**Transparenz und Erklärbarkeit**

Die Ausgaben des KI-Systems müssen in dem Mass interpretierbar sein, das für die menschliche Aufsicht und die Kommunikation mit betroffenen Personen erforderlich ist. Die Ziele müssen spezifizieren:

- Erforderliches Erklärbarkeitsnivaeu (Feature-Importance, Entscheidungsbegründung, lokale Erklärungen) basierend auf Anwendungsfall und Folgenklassifizierung
- Zielgruppe der Erklärungen (interne Operatoren, betroffene Personen, Regulatoren)
- Dokumentation der Modellgrenzen und Bedingungen, unter denen Ausgaben unzuverlässig sein können

**Robustheit und Sicherheit**

Das KI-System muss innerhalb seiner dokumentierten Betriebsbedingungen zuverlässig funktionieren und bei Bedingungen ausserhalb des definierten Betriebsbereichs sicher ausfallen. Die Ziele müssen spezifizieren:

- Definierte Betriebsbedingungen und Anforderungen an die Out-of-Distribution-Erkennung
- Anforderungen an die adversariale Robustheit (wo das KI-System ein Ziel sein könnte)
- Akzeptable Ausfallmodi und ausfallsicheres Verhalten
- Test-Coverage für Grenzfälle und adversariale Eingaben

**Privacy by Design**

Das KI-System muss personenbezogene Daten minimal und durch Design verarbeiten, nicht nachträglich. Die Ziele müssen spezifizieren:

- Datensparsamkeitsanforderungen für Training und Betrieb
- Anonymisierungs- oder Pseudonymisierungsanforderungen
- Anforderungen gemäss DSGVO Artikel 25 (Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen) soweit anwendbar
- Querverweis auf PRIV-POL-00-Verpflichtungen

**Menschliche Aufsicht**

Das Design des KI-Systems muss eine sinnvolle menschliche Aufsicht unterstützen und nicht untergraben. Die Ziele müssen spezifizieren:

- Menschliche Prüfungspunkte, die vor KI-gestützten Entscheidungen mit Auswirkungen auf Personen erforderlich sind
- Override-Mechanismen — Fähigkeit für Menschen, KI-Ausgaben zu übersteuern
- Protokollierungs- und Audit-Trail-Anforderungen zur Unterstützung der menschlichen Aufsicht
- Alarmmechanismen bei anomalem KI-Systemverhalten

**Verantwortlichkeit**

Klare menschliche Verantwortlichkeit für das Verhalten des KI-Systems muss aufrechterhalten werden. Die Ziele müssen spezifizieren:

- Namentlich benannter KI-Risikoverantwortlicher für das KI-System (AI-POL-A.3.2-3)
- Eskalationspfad für KI-Vorfälle
- Audit-Trail-Anforderungen, die KI-Ausgaben mit der produzierenden Systemversion verknüpfen

### Dokumentation der Ziele für verantwortungsvolle Entwicklung

Ziele für verantwortungsvolle Entwicklung müssen in einem **KI-System-Entwicklungsziele-Dokument** für jedes KI-System dokumentiert werden, unterzeichnet von:

- KI-GB (Genehmigung der verantwortungsvollen KI-Governance)
- KI-Risikoverantwortlichem (Risikoakzeptanz)
- CTO / KI-Engineering-Leiter (Bestätigung der technischen Machbarkeit)

Das Dokument muss aktualisiert werden, wenn sich das AISIA-Ergebnis wesentlich ändert.

---

## Richtlinienaussagen: Prozesse für verantwortungsvolles KI-Design und -Entwicklung (A.6.1.3)

### Prozessdefinitionsanforderung

Die [Organisation] MUSS die spezifischen Prozesse für das verantwortungsvolle Design und die Entwicklung jedes KI-Systems definieren und dokumentieren. Diese Prozesse müssen die unter A.6.1.2 definierten Ziele für verantwortungsvolle Entwicklung operationalisieren.

### Erforderliche Prozesse für verantwortungsvolle Entwicklung

**1. Verantwortungsvoller KI-Design-Review**

Vor Entwicklungsbeginn muss ein Design-Review-Prozess validieren, dass:

- Die vorgeschlagene KI-Systemarchitektur die dokumentierten Ziele für verantwortungsvolle KI unterstützt
- Fairness-, Erklärbarkeits- und Datenschutzaspekte in das Design eingebettet sind, nicht nachträglich hinzugefügt
- Der vorgesehene Verwendungszweck klar spezifiziert und Scope-begrenzende Kontrollen designt sind

Der Design-Review muss dokumentiert werden, mit Genehmigung des KI-GB.

**2. Bias- und Fairness-Bewertungsprozess**

Für KI-Systeme mit mittlerer oder hoher Folgenklassifizierung (gemäss AI-POL-A.5.2-5) muss der Entwicklungsprozess umfassen:

- Vor der Entwicklung: Bewertung der Repräsentativität des Datensatzes — repräsentieren die Trainingsdaten die Deployment-Population?
- Während der Entwicklung: Fairness-bewusste Modellauswahl und -training — welche Fairness-Einschränkungen oder -Ziele sind integriert?
- Vor dem Deployment: Fairness-Bewertung anhand genehmigter Metriken und Schwellenwerte
- Nach dem Deployment: Kontinuierliche Fairness-Überwachung (A.6.2.6)

Der Bias-Bewertungsprozess muss pro KI-System dokumentiert werden, mit Aufbewahrung der Nachweise.

**3. Checkpoints für verantwortungsvolle KI-Entwicklung**

Der Entwicklungsprozess muss definierte Checkpoints enthalten, an denen Kriterien für verantwortungsvolle KI bewertet werden, bevor zur nächsten Phase übergegangen wird:

| Checkpoint | Phase | Was verifiziert wird |
|-----------|-------|---------------------|
| Design-Genehmigung | Vor Entwicklungsbeginn | Ziele für verantwortungsvolle KI dokumentiert; AISIA abgeschlossen; Datenquellen genehmigt |
| Datenqualitäts-Gate | Vor dem Modell-Training | Datenrepräsentativität, Qualitätskriterien erfüllt; Herkunft dokumentiert |
| Entwicklungs-Review | Während aktiver Entwicklung | Fairness-, Erklärbarkeits- und Datenschutzmassnahmen wie geplant umgesetzt |
| Prä-Validierungs-Review | Vor V&V (A.6.2.4) | Modelldokumentation vollständig; Testkriterien definiert, einschliesslich Kriterien für verantwortungsvolle KI |
| Prä-Deployment-Genehmigung | Vor Deployment (A.6.2.5) | Alle Ziele für verantwortungsvolle KI bewertet; AISIA aktuell; menschliche Aufsichtsmechanismen implementiert |

Jeder Checkpoint muss ein dokumentiertes Ergebnis erzeugen. Ein System, das einen Checkpoint für verantwortungsvolle KI nicht besteht, darf bis zur Problemlösung nicht in die nächste Phase übergehen.

**4. Dokumentationsprozess für verantwortungsvolle KI**

Während der gesamten Entwicklung muss folgende Dokumentation gepflegt werden:

- **Modellkarte**: Vorgesehener Verwendungszweck, Beschreibung der Trainingsdaten, Evaluierungsergebnisse einschliesslich Fairness-Metriken, bekannte Grenzen, nicht vorgesehene Verwendungen
- **Datenkarte**: Datensatzbeschreibung, Erhebungsmethodik, Repräsentativitätsbewertung, Bias-Analyse
- **Kriteriendokument für verantwortungsvolle KI**: Wie jedes Ziel für verantwortungsvolle KI im Design und in der Entwicklung adressiert wurde

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **KI-GB** | Genehmigung der Ziele für verantwortungsvolle Entwicklung; Genehmigung des Design-Reviews; Durchführung oder Beauftragung von Checkpoint-Reviews für verantwortungsvolle KI; Pflege der Zieldokumentation |
| **CTO / KI-Engineering-Leiter** | Leitung von Design-Reviews für verantwortungsvolle KI; Sicherstellung, dass der Entwicklungsprozess Checkpoints enthält; Sicherstellung, dass Engineering-Teams in verantwortungsvollen KI-Praktiken geschult sind |
| **KI-System-Eigentümer** | Pflege des Entwicklungsziele-Dokuments; Sicherstellung der Vollständigkeit der Checkpoint-Dokumentation |
| **Data Scientists / ML-Ingenieure** | Anwendung fairness-bewusster Techniken; Durchführung von Datensatz-Repräsentativitätsbewertungen; Dokumentation von Modellkarten und Datenkarten |
| **KI-Risikoverantwortlicher** | Akzeptanz des verbleibenden Risikos für verantwortungsvolle KI; Eskalation, wenn Ziele nicht erreicht werden können |

---

## Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrung |
|----------|--------------|--------------|
| Entwicklungsziele-Dokument | KI-systemspezifisches Dokument der Ziele für verantwortungsvolle KI mit Genehmigung | Systemdauer + 3 Jahre |
| Design-Review-Nachweise | Dokumentation der Design-Reviews für verantwortungsvolle KI mit Ergebnissen | Systemdauer + 3 Jahre |
| Checkpoint-Nachweise | Belege für jeden Checkpoint für verantwortungsvolle KI mit Bestanden/Nicht-bestanden-Ergebnis | Systemdauer + 3 Jahre |
| Modellkarten | Modelldokumentation einschliesslich Fairness-Bewertung und Grenzen | Systemdauer + 3 Jahre |
| Datenkarten | Datensatzdokumentation einschliesslich Repräsentativität und Bias-Analyse | Nutzungsdauer der Daten + 3 Jahre |

---

## Hinweise für Auditoren

Auditoren, die die Konformität mit A.6.1.2–A.6.1.3 prüfen, sollten folgendes vorfinden:

- Dokumentierte Ziele für verantwortungsvolle Entwicklung pro KI-System, datierend vor der Entwicklung
- Belege, dass Ziele durch AISIA-Ergebnisse informiert wurden
- Definierten Entwicklungsprozess mit Checkpoints für verantwortungsvolle KI
- Checkpoint-Nachweise, die zeigen, dass Kriterien für verantwortungsvolle KI vor Phasenübergängen bewertet wurden
- Modellkarten und Datenkarten als Output-Artefakte des Entwicklungsprozesses

---

<!-- QA_VERIFIED: [2026-04-15] -->
