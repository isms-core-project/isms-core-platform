<!-- ISMS-CORE:POLICY:AI-POL-A.6.2-DE:ai:POL:a.6.2 -->
**AI-POL-A.6.2 — KI-System-Lebenszyklus**

---

## Dokumentenkontrolle

| Feld | Wert |
|------|------|
| **Dokumenttitel** | KI-System-Lebenszyklus |
| **Dokumenttyp** | Richtlinie |
| **Dokument-ID** | AI-POL-A.6.2 |
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

**Überprüfungszyklus**: Jährlich (oder bei wesentlichen Änderungen der KI-Entwicklungs- und Betriebspraktiken)
**Nächstes Überprüfungsdatum**: [Datum des Inkrafttretens + 12 Monate]

**Genehmigungskette**:

- Primär: KI-Governance-Beauftragter (KI-GB)
- Sekundär: Technischer Direktor (CTO) / KI-Engineering-Leiter
- Compliance: Informationssicherheitsbeauftragter (ISB)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- AI-POL-00 (AIMS — Regulatorischer Anwendbarkeitsrahmen für KI)
- AI-POL-A.6.1 (KI-Entwicklungs-Governance — Ziele und Prozesse vor dem Lebenszyklus)
- AI-POL-A.7.2-6 (Daten für KI-Systeme)
- AI-POL-A.5.2-5 (KI-System-Folgenabschätzung — AISIA muss dem Deployment vorausgehen)
- AI-IMP-A.6.2-UG (KI-System-Lebenszyklus — Benutzerhandbuch)
- AI-IMP-A.6.2-TG (KI-System-Lebenszyklus — Technischer Leitfaden)
- ISO/IEC 42001:2023 Massnahmen A.6.2.2, A.6.2.3, A.6.2.4, A.6.2.5, A.6.2.6, A.6.2.7, A.6.2.8
- ISO/IEC 42001:2023 Anhang B.6.2 (Umsetzungshinweise — KI-System-Lebenszyklus)

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen der [Organisation] für den KI-System-Lebenszyklus fest — einschliesslich Spezifikation, Dokumentation von Design und Entwicklung, Verifizierung und Validierung, Deployment, Betrieb und Monitoring, technische Dokumentation und Ereignisprotokollierung — in Übereinstimmung mit den ISO/IEC 42001:2023-Massnahmen A.6.2.2 bis A.6.2.8.

**Anwendungsbereich**: Alle KI-Systeme im AIMS-Scope über alle Lebenszyklusphasen von der Spezifikation bis zur Ausserbetriebnahme. Massnahmen gelten für KI-Anbieter (vorrangig) und KI-Betreiber, wo diese wesentlichen Einfluss auf das Lebenszyklusmanagement haben.

**Zweck**: Festlegen, WAS in jeder Lebenszyklusphase dokumentiert und kontrolliert werden muss, WER verantwortlich ist und WANN Massnahmen gelten. Umsetzungsdetails sind in AI-IMP-A.6.2-UG und AI-IMP-A.6.2-TG beschrieben.

**Begründung der zusammengefassten Massnahmen**: A.6.2.2 bis A.6.2.8 entsprechen direkt den Phasen des KI-System-Lebenszyklus. Jede Massnahme regelt eine bestimmte Phase: Spezifikation → Design-/Entwicklungsdokumentation → Verifizierung/Validierung → Deployment → Betrieb/Monitoring → technische Dokumentation → Ereignisprotokollierung. Diese sieben Massnahmen sind voneinander abhängig — jede Phase erzeugt Ergebnisse, von denen die nächste Phase abhängt.

---

## Anwendungsbereich und Geltungsbereich

### ISO/IEC 42001:2023-Massnahmen

**Massnahme A.6.2.2 — KI-Systemanforderungen und -spezifikation**
Die Organisation muss Anforderungen für neue KI-Systeme oder wesentliche Verbesserungen bestehender Systeme spezifizieren und dokumentieren.

**Massnahme A.6.2.3 — Dokumentation von KI-Systemdesign und -entwicklung**
Die Organisation muss das KI-Systemdesign und die -entwicklung auf der Grundlage organisatorischer Ziele, dokumentierter Anforderungen und Spezifikationskriterien dokumentieren.

**Massnahme A.6.2.4 — KI-System-Verifizierung und -Validierung**
Die Organisation muss Verifizierungs- und Validierungsmassnahmen für das KI-System definieren und dokumentieren sowie Kriterien für deren Einsatz spezifizieren.

**Massnahme A.6.2.5 — KI-System-Deployment**
Die Organisation muss einen Deployment-Plan dokumentieren und sicherstellen, dass geeignete Anforderungen vor dem Deployment erfüllt sind.

**Massnahme A.6.2.6 — KI-Systembetrieb und -Monitoring**
Die Organisation muss die notwendigen Elemente für den laufenden Betrieb des KI-Systems definieren und dokumentieren. Mindestens sollten Systemleistungsüberwachung, Reparaturen, Updates und Support enthalten sein.

**Massnahme A.6.2.7 — Technische Dokumentation des KI-Systems**
Die Organisation muss bestimmen, welche technische Dokumentation des KI-Systems für jede relevante Kategorie interessierter Parteien, wie Nutzer, Partner, Aufsichtsbehörden, benötigt wird, und diese in angemessener Form bereitstellen.

**Massnahme A.6.2.8 — KI-System — Aufzeichnung von Ereignisprotokollen**
Die Organisation muss bestimmen, in welchen Phasen des KI-System-Lebenszyklus die Aufzeichnung von Ereignisprotokollen aktiviert werden soll, mindestens jedoch bei Nutzung des KI-Systems.

### Regulatorischer Rahmen

**Stufe 1: Verpflichtende Compliance** (gemäss AI-POL-00):

- **EU-KI-Verordnung (Verordnung 2024/1689)**: Artikel 11 (technische Dokumentation), Artikel 12 (Aufzeichnungspflichten und Protokollierung), Artikel 13 (Transparenz und Informationsbereitstellung), Artikel 14 (menschliche Aufsicht), Artikel 15 (Genauigkeit, Robustheit, Cybersicherheit), Artikel 17 (QMS — alle Lebenszyklusphasen)

**Stufe 2: Bedingt** (gemäss AI-POL-00):

- **ISO/IEC 42001:2023**: Massnahmen A.6.2.2–A.6.2.8 — gilt, wenn die AIMS-Zertifizierung im Scope liegt oder vertraglich gefordert ist

---

## Richtlinienaussagen: Anforderungen und Spezifikation (A.6.2.2)

### Anforderung an die KI-Systemspezifikation

Die [Organisation] MUSS Anforderungen für jedes neue KI-System und für wesentliche Verbesserungen bestehender Systeme vor Beginn der Entwicklung oder Verbesserung spezifizieren und dokumentieren.

### Anforderungen an das Spezifikationsdokument

Die KI-Systemspezifikation muss Folgendes dokumentieren:

| Element | Erforderlicher Inhalt |
|---------|----------------------|
| **Vorgesehener Zweck** | Klare Aussage, was das KI-System tun soll, für wen und in welchem Kontext |
| **Funktionale Anforderungen** | Was das System leisten muss (Eingaben, Ausgaben, Entscheidungstypen, Leistungserwartungen) |
| **Nichtfunktionale Anforderungen** | Zuverlässigkeit, Verfügbarkeit, Antwortzeit, Skalierbarkeit, Sicherheit |
| **Anforderungen für verantwortungsvolle KI** | Fairness-Metriken und -Schwellenwerte; Erklärbarkeitsgrad; menschliche Aufsichtsmechanismen; abgeleitet aus AISIA und AI-POL-A.6.1-Zielen |
| **Betriebsbedingungen** | Bedingungen, unter denen das KI-System korrekt funktionieren soll (Annahmen zur Datenverteilung, Umgebungsbedingungen) |
| **Nicht-Scope-Verwendungen** | Explizit dokumentierte Verwendungen, für die das System NICHT konzipiert oder validiert ist |
| **Stakeholder** | Interne und externe Parteien, die mit dem System interagieren oder davon betroffen sein werden |
| **Regulatorische Einschränkungen** | EU-KI-Verordnung Risikoeinstufung; DSGVO Artikel 22-Auslöser; andere anwendbare Verpflichtungen |
| **Integrationsanforderungen** | Wie das KI-System in bestehende Systeme und Prozesse integriert wird |

**Wesentliche Verbesserung** ist definiert als jede Änderung, die: die KI-Systemausgaben wesentlich modifiziert; das System einer neuen Population einführt; den Betriebskontext oder den vorgesehenen Zweck ändert; oder die Modellarchitektur, Trainingsdaten oder Schlüssel-Hyperparameter ändert.

---

## Richtlinienaussagen: Design- und Entwicklungsdokumentation (A.6.2.3)

### Anforderung an die Design- und Entwicklungsdokumentation

Die [Organisation] MUSS das KI-Systemdesign und die -entwicklung dokumentieren und sicherstellen, dass die Dokumentation zur Spezifikation und zu den Zielen für verantwortungsvolle KI rückverfolgbar ist.

### Erforderliche Dokumentation

| Dokumentation | Inhalt |
|--------------|--------|
| **Architekturdokumentation** | Übergeordnete Systemarchitektur; Komponentendiagramm; Datenfluss; Integrationspunkte |
| **Modelldokumentation** | Begründung der Algorithmuswahl; Modellarchitektur; Trainingsansatz; Hyperparameterwahl |
| **Trainingsdatendokumentation** | Verwendete Datensätze; Vorverarbeitungsschritte; Datenteilungsmethodik; Verweis auf A.7-Datenaufzeichnungen |
| **Designentscheidungsprotokoll** | Wichtige Designentscheidungen mit Begründung; gemachte Kompromisse; betrachtete Alternativen |
| **Designentscheidungen für verantwortungsvolle KI** | Wie Fairness-, Transparenz- und Sicherheitsanforderungen im Design adressiert wurden |
| **Versionshistorie** | Alle Modellversionen mit dokumentierten Änderungen; Reproduzierbarkeitsinformationen |

Die Dokumentation muss versionskontrolliert und mit der von ihr beschriebenen KI-Systemversion verknüpft sein.

---

## Richtlinienaussagen: Verifizierung und Validierung (A.6.2.4)

### V&V-Anforderung

Die [Organisation] MUSS Verifizierungs- und Validierungsmassnahmen für jedes KI-System vor dem Deployment definieren und dokumentieren sowie Kriterien spezifizieren, die für die Deployment-Genehmigung erfüllt sein müssen.

### Verifizierung

Die Verifizierung bestätigt, dass das KI-System gemäss Spezifikationen korrekt erstellt wurde:

- Funktionale Tests gegen Spezifikationsanforderungen
- Leistungstests (Genauigkeit, Precision/Recall oder aufgabenspezifische Metriken) gegen definierte Schwellenwerte
- Sicherheitstests — adversariale Eingabetests, Modell-Robustheitsbewertung
- Integrationstests in der Staging-Umgebung

### Validierung

Die Validierung bestätigt, dass das KI-System das richtige Problem löst und für seinen vorgesehenen Zweck geeignet ist:

- Validierung verantwortungsvoller KI — Fairness-Metriken anhand genehmigter Schwellenwerte bewertet; Erklärbarkeit für Zielgruppe validiert
- Validierung des vorgesehenen Verwendungszwecks — Tests mit realen Bedingungen und Grenzfällen
- Out-of-Distribution-Tests — Verhalten dokumentiert, wenn Eingaben ausserhalb der Trainingsverteilung liegen
- Validierung der menschlichen Aufsicht — Override-Mechanismen funktionieren korrekt; Alarmschwellen kalibriert

### Deployment-Kriterien

Jedes KI-System muss dokumentierte Kriterien haben, die vor der Deployment-Genehmigung erfüllt sein müssen. Der KI-GB muss den V&V-Abschluss anhand der Kriterien bestätigen. Ein System, das V&V-Kriterien nicht erfüllt, darf nicht deployt werden.

---

## Richtlinienaussagen: Deployment (A.6.2.5)

### Anforderung an den Deployment-Plan

Die [Organisation] MUSS einen Deployment-Plan für jedes KI-System dokumentieren und sicherstellen, dass alle Vor-Deployment-Anforderungen vor dem operativen Deployment erfüllt sind.

### Inhalt des Deployment-Plans

| Element | Erforderlicher Inhalt |
|---------|----------------------|
| **Deployment-Scope** | Welche Umgebungen, Nutzergruppen und Anwendungsfälle in diesem Deployment abgedeckt sind |
| **Vor-Deployment-Checkliste** | Alle Anforderungen, die vor dem Deployment bestätigt werden müssen (AISIA genehmigt, V&V bestanden, technische Dokumentation bereit, menschliche Aufsicht implementiert, Protokollierung aktiviert) |
| **Rollout-Ansatz** | Gestaffeltes Rollout / Shadow-Modus / vollständiges Deployment — mit Begründung |
| **Rollback-Verfahren** | Wie zum vorherigen Zustand zurückgekehrt werden kann, wenn das Deployment unerwartete Probleme verursacht |
| **Monitoring-Aktivierung** | Wie das operative Monitoring (A.6.2.6) beim Deployment aktiviert wird |
| **Stakeholder-Kommunikation** | Wer über das Deployment informiert werden muss und wie |
| **Deployment-Genehmigung** | Namentlich genannter Genehmiger (KI-GB muss genehmigen) und Genehmigungsdatum |

**Deployment-Gate**: Kein KI-System darf ohne dokumentierte Genehmigung des KI-GB deployt werden, die bestätigt, dass alle Vor-Deployment-Anforderungen erfüllt sind, einschliesslich einer aktuellen AISIA.

---

## Richtlinienaussagen: Betrieb und Monitoring (A.6.2.6)

### Anforderung an das operative Monitoring

Die [Organisation] MUSS die notwendigen Elemente für den laufenden Betrieb und das Monitoring jedes im Scope befindlichen KI-Systems definieren und dokumentieren.

### Obligatorische Monitoring-Elemente

**Leistungsmonitoring**:

- Key Performance Indicators (KPIs) in der Spezifikationsphase definiert (A.6.2.2)
- Monitoring-Häufigkeit dem Anwendungsfall angemessen (kontinuierlich / täglich / wöchentlich)
- Schwellenwerte für Leistungsverschlechterung — bei Unterschreitung wird ein Alarm ausgelöst
- Modelldrift-Erkennung — statistische Überwachung der Eingabedatenverteilung und Ausgabeverteilung

**Monitoring verantwortungsvoller KI**:

- Fairness-Monitoring — Fairness-Metriken werden in der Produktion nach einem definierten Zeitplan gemessen
- Bias-Erkennung — Monitoring auf Entstehung von Bias in der Produktion, der bei V&V nicht vorhanden war
- Wirksamkeit der menschlichen Aufsicht — werden Override-Mechanismen angemessen genutzt?
- Scope-Konformität — wird das KI-System nur für dokumentierte vorgesehene Zwecke verwendet?

**Operatives Monitoring**:

- Systemverfügbarkeit und Uptime
- Antwortzeit und Durchsatz
- Fehlerraten und Ausfallmodi
- Infrastrukturgesundheit (verknüpft mit A.4.5)

**Incident-Alarmierung**:

- Definierte Alarmbedingungen für jede Monitoring-Dimension
- Eskalationspfad von automatisiertem Alarm zu KI-System-Eigentümer zu KI-Risikoverantwortlichem
- Integration in den KI-Incident-Response-Prozess (AI-POL-A.8.2-5)

### Monitoring-Dokumentation

Der Monitoring-Plan für jedes KI-System muss vor dem Deployment dokumentiert werden und alle obligatorischen Monitoring-Elemente abdecken mit:

- Was überwacht wird
- Wie es überwacht wird (Tool, Methode)
- Häufigkeit
- Alarmschwellen
- Eskalationspfad bei Schwellenwertüberschreitung

---

## Richtlinienaussagen: Technische Dokumentation (A.6.2.7)

### Anforderung an die technische Dokumentation

Die [Organisation] MUSS bestimmen, welche technische Dokumentation für jede relevante Kategorie interessierter Parteien benötigt wird, und diese in angemessener Form bereitstellen.

### Kategorien interessierter Parteien und Dokumentationsanforderungen

| Interessierte Partei | Erforderliche Dokumentation |
|---------------------|---------------------------|
| **Interne Operatoren / Nutzer** | Benutzerhandbuch; Spezifikation des vorgesehenen Verwendungszwecks; Grenzen; Betriebsverfahren; Override-Mechanismen |
| **KI-System-Eigentümer / Governance** | Vollständige technische Spezifikation; Modellkarte; V&V-Bericht; AISIA-Zusammenfassung; Monitoring-Plan |
| **IT / Infrastruktur** | Systemarchitektur; Integrationsdokumentation; Infrastrukturanforderungen; Deployment-Runbook |
| **Aufsichtsbehörden** | EU-KI-Verordnung technische Dokumentation (Artikel 11 für Hochrisiko-KI); AISIA-Zusammenfassung; Konformitätsbewertungsdokumentation |
| **Kunden / Partner** | Fähigkeitsbeschreibung; Grenzen; Transparenzhinweis (A.8.2); Incident-Meldungsmechanismus (A.8.3) |
| **Auditoren (intern/extern)** | Vollständiger Dokumentationssatz; V&V-Nachweise; AISIA; SoA-Referenz |

Technische Dokumentation muss versionskontrolliert, mit der beschriebenen KI-Systemversion verknüpft und bei jeder wesentlichen Änderung überprüft werden.

---

## Richtlinienaussagen: Ereignisprotokollierung (A.6.2.8)

### Anforderung an die Ereignisprotokollierung

Die [Organisation] MUSS bestimmen, in welchen Phasen des KI-System-Lebenszyklus die Ereignisprotokollierung aktiviert werden soll. Mindestens muss die Protokollierung aktiv sein, wenn das KI-System im operativen Einsatz ist.

### Obligatorische Protokollierungsphasen

| Lebenszyklusphase | Protokollierungsanforderung |
|------------------|---------------------------|
| **Operativer Einsatz** | OBLIGATORISCH — alle KI-Systeminteraktionen, Eingaben, Ausgaben und Entscheidungen müssen protokolliert werden |
| **Validierung und Testing** | Erforderlich — Testeingaben, Ausgaben und Evaluierungsergebnisse für die Rückverfolgbarkeit protokolliert |
| **Deployment** | Erforderlich — Deployment-Ereignis, Version, Genehmiger, Zeitstempel |
| **Monitoring-Alarme** | Erforderlich — alle Schwellenwertüberschreitungen und Alarmereignisse |
| **Vorfälle** | Erforderlich — alle KI-Vorfallsereignisse für die Post-Incident-Review |
| **Entwicklung** | Best Practice — Modelltraining-Läufe, Hyperparameter-Sets, Evaluierungsmetriken |

### Anforderungen an den Protokollinhalt

Für operative KI-Systemprotokolle muss jeder Ereignisdatensatz mindestens enthalten:

- Zeitstempel (UTC)
- KI-System-Kennung und Version
- Eingabezusammenfassung (oder Eingabe-Hash, wenn die vollständige Eingabeprotokollierung durch Datenschutzverpflichtungen verboten ist)
- Produzierte Ausgabe oder Entscheidung
- Jede angewendete menschliche Übersteuerung (Override)
- Nutzer- oder Sitzungskennung (soweit anwendbar und zulässig)

### Protokollaufbewahrung

KI-System-Ereignisprotokolle müssen aufbewahrt werden für:

- Die Dauer der Betriebszeit des KI-Systems, PLUS
- Mindestens 3 Jahre nach der Ausserbetriebnahme (verlängern, wenn EU-KI-Verordnung oder Branchenregelungen längere Fristen vorschreiben)

### Protokollschutz

KI-System-Ereignisprotokolle sind Audit-Nachweise. Sie müssen:

- Gegen Änderung oder Löschung geschützt sein (unveränderlich oder nur anhängebasiert, soweit durchführbar)
- Zugangskontrolliert sein (nur Lesezugriff für Auditoren; eingeschränkter Schreibzugriff für Protokollverwaltung)
- Gemäss ISMS-Sicherungsanforderungen gesichert sein

---

## Richtlinienaussagen: Ausserbetriebnahme

### Anforderung an die Ausserbetriebnahme

Die [Organisation] MUSS das geplante End-of-Life von KI-Systemen in einer kontrollierten Weise verwalten, die Nachweise erhält, Betroffene schützt und sicherstellt, dass kein Restschaden aus eingestellten Systemen entsteht.

### Bedingungen, die eine Ausserbetriebnahme auslösen

Ein Ausserbetriebnahmeprozess für ein KI-System muss eingeleitet werden, wenn:

- Das KI-System dauerhaft aus dem operativen Einsatz zurückgezogen wird
- Ein Ersatzsystem deployt wird und das bestehende System ausgemustert wird
- Die AISIA des KI-Systems Risiken identifiziert, die nicht angemessen gemindert werden können
- Der vorgesehene Anwendungsfall eingestellt wird
- Eine wesentliche Änderung eine vollständige Neubewertung erfordern würde, die das System nicht erfüllen kann

### Ausserbetriebnahmeprozess

Der KI-System-Eigentümer muss einen vom KI-GB genehmigten, dokumentierten Ausserbetriebnahmeplan ausführen, der Folgendes abdeckt:

| Schritt | Anforderung |
|---------|-------------|
| **Nutzerbenachrichtigung** | Alle Nutzer und betroffenen Parteien mit ausreichend Vorlaufzeit über das geplante Ausserbetriebnahmedatum informieren (mindestens 30 Tage für operative Systeme; gemäss vertraglichen Verpflichtungen für kundenseitige Systeme) |
| **Datenentsorgung** | Das Schicksal aller Trainings-, Betriebs- und Ausgabedaten festlegen: Löschung, Archivierung oder Transfer — gemäss DSGVO-Datenlebenszyklus-Anforderungen dokumentiert |
| **Modellentsorgung** | Löschung von Modellgewichten und zugehörigen Artefakten aus allen Umgebungen bestätigen (Produktion, Staging, Backups) oder Begründung für Aufbewahrung dokumentieren |
| **Zugangssperrung** | Alle Nutzer- und API-Zugriffe auf das System vor oder bei der Ausserbetriebnahme sperren |
| **Protokollaufbewahrung** | Ereignisprotokolle mindestens 3 Jahre nach der Ausserbetriebnahme aufbewahren oder gemäss anwendbarer Regulierung |
| **AISIA-Abschluss** | AISIA mit einem Ausserbetriebnahme-Nachweis abschliessen, die Entsorgungsmethode notieren und bestätigen, dass ausstehende Risiken gelöst sind |
| **EU-KI-Verordnung-Register** | Wenn das System in der EU-KI-Verordnung-Datenbank registriert war, Registrierungsstatus auf «ausser Betrieb» aktualisieren |
| **Drittpartei-Benachrichtigung** | Relevante Drittparteien (KI-Komponentenlieferanten, Datenverarbeiter) über die Ausserbetriebnahme informieren und Bestätigung der Datenlöschung einholen, wo erforderlich |

### Nachweisanforderungen für die Ausserbetriebnahme

Der KI-GB muss pro System einen **Ausserbetriebnahme-Nachweis** aufbewahren, der enthält: Systemidentität, Ausserbetriebnahmedatum, Entsorgungsmethode für Daten und Modellartefakte, Bestätigung der Nutzerbenachrichtigung und AISIA-Abschluss.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|----------------------|
| **KI-GB** | Genehmigung des Deployments (alle Phasen); Eigentümer der Lebenszyklusrichtlinie; Überprüfung der Monitoring-Berichte; Genehmigung technischer Dokumentation für regulatorische Zielgruppen; Genehmigung von Ausserbetriebnahmeplänen |
| **CTO / KI-Engineering-Leiter** | Eigentümer der A.6.2.2-Spezifikation, A.6.2.3-Dokumentation, A.6.2.4-V&V-Prozesse; Sicherstellung, dass Engineering-Praktiken der Richtlinie entsprechen |
| **KI-System-Eigentümer** | Pflege aller Lebenszyklus-Dokumentation für eigene Systeme; Eigentümer des Monitoring-Plans; Reaktion auf Monitoring-Alarme |
| **ISB** | Überprüfung der Sicherheitsdimensionen von V&V (A.6.2.4), Monitoring (A.6.2.6) und Protokollierung (A.6.2.8) |
| **KI-Risikoverantwortlicher** | Akzeptanz verbleibender Risiken aus der V&V; Genehmigung der Risikoakzeptanz beim Deployment |

---

## Nachweisanforderungen

| Nachweis | Beschreibung | Aufbewahrung |
|----------|--------------|--------------|
| KI-Systemspezifikation | Dokumentierte Anforderungen pro KI-Systemversion | Systemdauer + 3 Jahre |
| Design- und Entwicklungsdokumentation | Architektur, Modell, Training, Entscheidungsprotokoll | Systemdauer + 3 Jahre |
| V&V-Nachweise | Testpläne, Testergebnisse, Bestanden/Nicht-bestanden-Ergebnis für Deployment-Kriterien | Systemdauer + 3 Jahre |
| Deployment-Plan und -Genehmigung | Deployment-Plan mit Genehmigung des KI-GB | Systemdauer + 3 Jahre |
| Monitoring-Plan | Dokumentierter Monitoring-Plan mit Schwellenwerten | Systemdauer + 3 Jahre |
| Technische Dokumentation | Versionskontrollierte Dokumentation pro Kategorie interessierter Parteien | Systemdauer + 3 Jahre |
| Ereignisprotokolle | Operative KI-Systemprotokolle | Systemdauer + 3 Jahre nach Ausserbetriebnahme |
| Ausserbetriebnahme-Nachweise | Entsorgungsmethode, Datenlöschungsbestätigung, AISIA-Abschluss, Nutzerbenachrichtigung | 5 Jahre nach Ausserbetriebnahme |

---

## Hinweise für Auditoren

Auditoren, die die Konformität mit A.6.2.2–A.6.2.8 prüfen, sollten folgendes vorfinden:

- Spezifikationsdokumente für alle im Scope befindlichen KI-Systeme, die der Entwicklung vorausgehen
- Design- und Entwicklungsdokumentation, die zu Spezifikationen rückverfolgbar ist
- V&V-Berichte mit dokumentierten Deployment-Kriterien und Bestanden/Nicht-bestanden-Ergebnissen
- Deployment-Genehmigungsunterlagen mit Bestätigung des KI-GB
- Aktive Monitoring-Pläne mit Alarmkonfigurationen
- Technische Dokumentation für jede Kategorie interessierter Parteien verfügbar
- Aktive Ereignisprotokollierung im operativen Einsatz, mit dokumentierter Aufbewahrungsrichtlinie
- Ausserbetriebnahme-Nachweise für ausgemusterte KI-Systeme, einschliesslich Bestätigung der Daten-/Modellentsorgung und AISIA-Abschluss

---

<!-- QA_VERIFIED: 2026-04-15 -->
