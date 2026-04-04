<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.32-DE:operational:OP-POL:a.8.32 -->
**ISMS-OP-POL-A.8.32 — Change Management**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Change Management |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.32 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstfassung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.8.32 — Change management

**Verwandte Annex-A-Controls**:

| Control | Bezug zum Change Management |
|---------|-----------------------------|
| A.5.9 Inventar von Informationen und anderen verbundenen Assets | Asset-Inventar definiert den Änderungsumfang und die Auswirkungsbeurteilung |
| A.5.24–28 Incident Management | Fehlgeschlagene Änderungen können Incident-Response auslösen |
| A.5.37 Dokumentierte Betriebsprozeduren | Prozeduren werden nach Systemänderungen aktualisiert |
| A.8.8 Verwaltung technischer Schwachstellen | Patch-Deployment folgt dem Change-Management-Prozess |
| A.8.9 Konfigurationsmanagement | Konfigurations-Baselines werden nach Änderungen aktualisiert |
| A.8.19 Installation von Software auf Betriebssystemen | Software-Installationen folgen dem Change Management |
| A.8.25–29 Sicherer Entwicklungslebenszyklus | Entwicklungsänderungen folgen dem Change Management |
| A.8.31 Trennung von Umgebungen | Umgebungspromotion wird über den Change-Prozess kontrolliert |
| A.8.33 Testinformationen | Testdaten werden während des Change-Testings geschützt |

**Verwandte interne Richtlinien**:

- Asset-Management-Richtlinie
- Incident-Management-Richtlinie
- Richtlinie für dokumentierte Betriebsprozeduren
- Endpoint-Sicherheitsrichtlinie (Patch-Management)
- Netzwerksicherheitsrichtlinie

---

# Change-Management-Richtlinie

## Zweck

Zweck dieser Richtlinie ist es, das Risiko zu verwalten, das von Änderungen an Informationsverarbeitungssystemen, Applikationen, Infrastruktur und unterstützender Technologie ausgeht, und sicherzustellen, dass Änderungen geplant, bewertet, genehmigt, getestet, implementiert und in kontrollierter Weise dokumentiert werden.

Diese Richtlinie unterstützt den schweizerischen nDSG (revDSG) und die Datenschutzverordnung (DSV), indem sie technische und organisatorische Massnahmen entsprechend dem Risiko implementiert und sicherstellt, dass Änderungen an Systemen, die Personendaten verarbeiten, die Datenschutzmassnahmen nicht beeinträchtigen. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten ausserdem die DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden und Drittbenutzer.

Alle Änderungen an Informationsverarbeitungssystemen, Applikationen, Infrastruktur, Netzwerkgeräten, Cloud-Diensten und unterstützenden Systemen unabhängig vom Deployment-Modell (On-Premises, Cloud, Hybrid).

Dies umfasst Hardware-Änderungen, Software-Änderungen, Konfigurationsänderungen, Infrastrukturänderungen, Datenschema-Änderungen und Sicherheitssystem-Änderungen.

**Nicht im Geltungsbereich**: Inhaltsaktualisierungen von Websites (Text, Bilder), Benutzer-Self-Service-Aktionen (Passwortzurücksetzungen über das genehmigte Portal), routinemässige automatisierte Operationen (geplante Backups, Log-Rotation) und Änderungen, die vollständig von SaaS-Anbietern ausserhalb der Kundenkontrolle verwaltet werden.

## Grundsatz

Alle Änderungen an Informationsverarbeitungssystemen unterliegen formalen Change-Management-Verfahren. Änderungen müssen geplant, auf Auswirkungen und Risiko bewertet, autorisiert, getestet, kommuniziert, kontrolliert implementiert und dokumentiert werden. Notfalländerungen folgen beschleunigten Verfahren unter Beibehaltung von Kontrolle und Aufsicht.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Änderung (Change)** | Jede Hinzufügung, Modifikation oder Entfernung von Informationssystemkomponenten (Hardware, Software, Konfiguration, Daten), die die Informationssicherheit oder Systemverfügbarkeit beeinflussen könnte |
| **Standard Change** | Vorab genehmigte, risikoarme, routinemässige Änderung, die einem dokumentierten Verfahren aus dem Standard-Change-Katalog folgt |
| **Normal Change** | Änderung, die eine vollständige Bewertung, CAB-Review und den Standard-Genehmigungsworkflow erfordert |
| **Emergency Change** | Änderung, die eine beschleunigte Implementierung erfordert, um einen kritischen Vorfall oder aktiv ausgenutzte Schwachstelle zu beheben oder erhebliche Geschäftsauswirkungen zu verhindern |
| **Change Advisory Board (CAB)** | Multidisziplinäre Gruppe, die Expertenreviews, Auswirkungsbeurteilungen und Empfehlungen für Änderungen bereitstellt |
| **Post-Implementation Review (PIR)** | Strukturierte Überprüfung nach der Änderungsimplementierung, die verifiziert, dass die Ziele erreicht wurden, und Erkenntnisse festhält |
| **Fehlgeschlagene Änderung** | Änderung, die aufgrund des Scheiterns bei der Erreichung der Ziele, inakzeptabler Leistungsverschlechterung, Einführung einer Sicherheitsschwachstelle oder Beeinträchtigung kritischer Geschäftsfunktionen zurückgesetzt wird. Eine Änderung, die Korrekturen nach der Implementierung erfordert, ist nicht notwendigerweise «fehlgeschlagen», wenn die ursprüngliche Änderung nicht zurückgesetzt wurde |

---

## Änderungsklassifikation

Alle Änderungen sind in eine der drei Kategorien einzustufen:

| Typ | Risikoniveau | Genehmigung | CAB-Review | Testing |
|-----|-------------|-------------|------------|---------|
| **Standard** | Niedrig | Vorab genehmigt (Katalog) | Nicht erforderlich | Gemäss Katalogverfahren |
| **Normal** | Mittel–Hoch | Serviceeigentümer / CAB / ISB (risikobasiert) | Erforderlich für hohes Risiko | Test in Nicht-Produktionsumgebung erforderlich |
| **Emergency** | Kritisch | ISB oder IT-Operations-Manager | Retrospektiv (innerhalb von 48 Stunden) | Risikoangemessen (kann verkürzt sein) |

Änderungen in Graubereichen sind zur Klassifizierung an den Change Manager zu eskalieren.

---

## Change-Request-Prozess

### Einreichung von Change Requests

Alle im Geltungsbereich liegenden Änderungen sind als formale Change Requests im Change-Management-System einzureichen: **[Angabe: ServiceNow, Jira Service Management, Azure DevOps oder «In Auswahl; interimistisch: Ticketsystem/Tabellenkalkulation»]**.

**Systemzugriff**: Change-Einreichung steht allen IT-Mitarbeitenden zur Verfügung; Change-Genehmigung und CAB-Koordination auf autorisiertes Personal beschränkt.

**Change-ID-Format**: [Angabe: CHG-JJJJMMTT-### oder automatisch vom System generiert].

Jeder Change Request muss mindestens folgende Felder enthalten:

| Feld | Beschreibung |
|------|-------------|
| Change-ID | Vom System zugewiesene eindeutige Kennung |
| Beschreibung | Was geändert wird und warum |
| Geschäftliche Begründung | Grund für die Änderung |
| Betroffene Systeme | Assets, Dienste und betroffene Abhängigkeiten |
| Risikoklassifikation | Niedrig / Mittel / Hoch / Kritisch |
| Implementierungsplan | Schrittweise Vorgehensanweisung |
| Implementierungsfenster | Vorgeschlagenes Datum, Uhrzeit und Dauer |
| Rollback-Plan | Wie die Änderung bei Fehlschlag rückgängig gemacht wird |
| Test-Ansatz | Welche Tests durchgeführt werden |
| Anfordernder und Implementierende Person | Wer angefordert und wer ausführt |
| Kommunikationsplan | Wer informiert werden muss |

### Auswirkungs- und Risikobewertung

Alle Änderungen sind vor der Implementierung auf Auswirkungen zu bewerten:

- **Technische Auswirkungen**: Betroffene Systeme, Abhängigkeiten, Integrationspunkte.
- **Geschäftliche Auswirkungen**: Betroffene Dienste, Benutzerauswirkungen, Störungen des Geschäftsbetriebs.
- **Sicherheitsauswirkungen**: Vertraulichkeits-, Integritäts- und Verfügbarkeitsrisiken. Änderungen, die Systeme betreffen, die Personendaten verarbeiten, müssen eine Beurteilung der datenschutzrechtlichen Auswirkungen umfassen.
- **Compliance-Auswirkungen**: Regulatorische Pflichten, Audit-Kontrollen.
- **Risikoniveau**: Kombination aus Eintrittswahrscheinlichkeit eines Fehlschlags und Ausmass der Auswirkungen.

### Genehmigungsworkflow

Die Genehmigungsinstanz richtet sich nach dem Risikoniveau der Änderung:

| Risikoniveau | Genehmigungsinstanz |
|--------------|---------------------|
| **Niedrig** (Standard Change) | Vorab genehmigt über Standard-Change-Katalog |
| **Mittel** | Serviceeigentümer oder Teamleitung |
| **Hoch** | IT-Operations-Manager und ISB |
| **Kritisch** | Geschäftsleitung |

---

## Change Advisory Board (CAB)

Die Organisation richtet ein Change Advisory Board zur Überprüfung von Normal Changes und Emergency Changes ein.

### CAB-Zusammensetzung

| Rolle | Verantwortlichkeit |
|-------|-------------------|
| **Change Manager** (Vorsitz) | Prozesseigentümerschaft, Terminplanung, Kennzahlen, kontinuierliche Verbesserung |
| **IT-Operations-Vertreter** | Technische Machbarkeit, Infrastrukturauswirkungen |
| **Sicherheitsvertreter** | Sicherheitsrisikobewertung, Compliance-Auswirkungen |
| **Geschäftliche Applikationseigentümer** | Beurteilung der geschäftlichen Auswirkungen (für relevante Änderungen) |
| **Fachexperten** | Technische Expertise nach Bedarf |

### CAB-Betrieb

- **Regelmässige Sitzungen**: **[Angabe: Wöchentlich am [Tag] um [Uhrzeit] MEZ]** (oder entsprechend dem Änderungsvolumen).
- **Sitzungsformat**: [Vor Ort / virtuell / hybrid].
- **Tagesordnung veröffentlicht**: 24 Stunden vor der Sitzung (Change Requests bis [Vortag] 17:00 Uhr für CAB am [Sitzungstag] einzureichen).
- **Notfall-CAB**: Bei Bedarf für dringende Änderungen über [E-Mail/Teams/Slack] einzuberufen; kann mit reduziertem Quorum (Change Manager + ein weiteres Mitglied) fortfahren, mit vollständigem CAB-Retrospektiv innerhalb von **48 Stunden**.
- **Quorum**: Change Manager, IT-Operations-Vertreter, Sicherheitsvertreter und mindestens ein weiteres Mitglied.
- **Aufzeichnungen**: Sitzungsprotokolle sind für alle CAB-Sitzungen zu führen und dokumentieren Datum, Teilnehmende, überprüfte Änderungen, Entscheidungen, Begründungen und Aufgaben. Protokolle werden **3 Jahre** aufbewahrt.

---

## Standard-Change-Katalog

Die Organisation pflegt einen Standard-Change-Katalog mit vorab genehmigten, risikoarmen, routinemässigen Änderungen.

### Katalog-Anforderungen

Jeder Katalogeintrag muss folgende Informationen enthalten:

- Änderungsbeschreibung und Umfang.
- Vorbedingungen und Voraussetzungen.
- Schrittweise Vorgehensanweisung.
- Geschätzte Dauer.
- Rollback-Verfahren (sofern zutreffend).
- Risikobewertung (einmalig bei Katalogaufnahme durchgeführt).

### Katalog-Governance

- Katalog wird **vierteljährlich** durch den Change Manager mit CAB-Beiträgen überprüft.
- Neue Einträge aus erfolgreichen Normal Changes, die wiederholbar und risikoarm sind.
- Einträge werden nach einem Standard-Change-Fehlschlag entfernt oder neu klassifiziert.
- Erfolgsquotenziel: **>95%** für Standard Changes.

Standard Changes müssen weiterhin im Change-Management-System protokolliert werden, um einen Audit-Trail und eine Vorfallskorrelation zu ermöglichen, auch wenn kein CAB-Review erforderlich ist.

### Beispiele aus dem Standard-Change-Katalog

Typische vorab genehmigte Standard Changes umfassen:

| Änderung | Verfahrensreferenz | Geschätzte Dauer | Voraussetzungen |
|----------|---------------------|------------------|-----------------|
| Benutzer zu Active-Directory-Gruppe hinzufügen | IT-SOP-001 | 5 Minuten | Genehmigtes Zugriffsanfrage-Ticket |
| Applikationsserver neu starten (Nicht-Produktion) | IT-SOP-015 | 10 Minuten | Benachrichtigung des Serviceeigentümers |
| SSL-Zertifikat erneuern | IT-SOP-023 | 30 Minuten | Neues Zertifikat erhalten, Backup des alten Zertifikats |
| DNS-Eintrag hinzufügen (interne Domain) | IT-SOP-031 | 10 Minuten | DNS-Änderungsantragsformular ausgefüllt |
| Firewall-Regel für genehmigte Applikation | IT-SOP-045 | 15 Minuten | Vorab-Genehmigung des Security Teams, Regel dokumentiert |

**Keine Standard Changes**: Datenbankschema-Änderungen, OS-Upgrades, Netzwerktopologieänderungen, neue Software-Installationen, Sicherheitskonfigurationsänderungen in der Produktion.

---

## Testing und Validierung

### Testing-Anforderungen

Änderungen sind vor dem Produktions-Deployment zu testen:

| Änderungsrisiko | Erforderliches Testing |
|-----------------|------------------------|
| **Niedrig** (Standard) | Gemäss Katalogverfahren; Verifizierung durch Implementierende |
| **Mittel** | Funktions- und Integrationstests in Nicht-Produktionsumgebung |
| **Hoch** | Funktions-, Integrations-, Performance- und User-Acceptance-Tests |
| **Kritisch** | Vollständige Test-Suite einschliesslich Sicherheitstests und Disaster-Recovery-Validierung |

### Umgebungstrennung

- Änderungen sind in Nicht-Produktionsumgebungen (Entwicklung, Test/QA, Staging) zu testen, bevor sie in Produktion deployed werden.
- Nicht-Produktionsumgebungen sind logisch oder physisch von der Produktion zu trennen, mit separaten Zugangsdaten und Zugriffskontrollen.
- Produktionsdaten dürfen ohne Maskierung oder Anonymisierung gemäss der Richtlinie zur Informationsklassifikation und -behandlung nicht in Testumgebungen verwendet werden.
- Die Promotion vom Test in die Produktion erfordert eine formale Freigabe und verifizierte Testergebnisse.

### Schutz der Produktionsumgebung

Produktionsänderungen dürfen nur durch autorisiertes Personal mit folgenden Kontrollen ausgeführt werden:

- **Funktionstrennung**: Entwickler dürfen ihre eigenen Änderungen nicht ohne unabhängige Überprüfung und Genehmigung durch einen designierten Release-Manager, ein Operations-Team-Mitglied oder das CAB in die Produktion deployen.
- **Peer-Review**: Code-Änderungen erfordern Peer-Review und Genehmigung vor dem Produktions-Deployment (über Pull Request oder äquivalenten Mechanismus).
- **Multi-Faktor-Authentifizierung** ist für den Produktionszugriff erforderlich.
- **Privilegiertes Zugriffsmanagement**: Produktions-Deployment-Konten müssen von Entwicklungskonten getrennt sein.
- **Alle Produktionsänderungen sind Audit-protokolliert** mit Benutzeridentität, Zeitstempel und Änderungsinhalt.

**Ausnahme**: In Organisationen mit weniger als 5 IT-Mitarbeitenden, wo eine vollständige Trennung nicht machbar ist, müssen kompensierende Kontrollen eine erweiterte Protokollierung, monatliche ISB-Überprüfung aller Produktionsänderungen sowie Peer-Review nach der Implementierung umfassen.

---

## Implementierung und Rollback

### Kontrollierte Implementierung

Änderungen sind gemäss dem genehmigten Implementierungsplan mit folgenden Massnahmen durchzuführen:

- Verifizierung der Voraussetzungen und Abhängigkeiten vor dem Start.
- Ausführung der dokumentierten Schritte.
- Echtzeit-Monitoring während der Implementierung.
- Verifizierungstests nach der Implementierung.
- Dokumentation der tatsächlich durchgeführten Schritte und etwaiger Abweichungen.

### Wartungsfenster

Die Organisation legt bevorzugte Änderungsfenster fest, um Betriebsunterbrechungen zu minimieren:

**Bevorzugte Änderungsfenster**:
- **Standardfenster**: [Angabe: z.B. Dienstags und Donnerstags 20:00–23:00 MEZ]
- **Erweitertes Fenster**: [Angabe: z.B. Samstags 08:00–16:00 MEZ]
- **Notfall**: Jederzeit mit ISB-Genehmigung

**Eingeschränkte Zeiträume** (keine Nicht-Notfalländerungen):
- [Unternehmensspezifisch: z.B. «Erste Woche jedes Monats (Finanzabschluss)», «15. Dezember – 5. Januar (Jahresend-Freeze)»]
- Feiertage: Schweizerische Bundesfeiertage
- Wichtige Geschäftsereignisse: im Änderungskalender 90 Tage im Voraus dokumentiert

Änderungen ausserhalb der bevorzugten Fenster erfordern unabhängig vom technischen Risikoniveau die **Genehmigungsinstanz für hohes Risiko** (IT-Operations-Manager + ISB).

### Rollback

Ein Rollback-Verfahren ist vor der Implementierung von Änderungen an Produktionssystemen zu vereinbaren. Rollback wird ausgeführt, wenn:

- Die Änderung ihre Ziele nicht erreicht.
- Eine inakzeptable Leistungsverschlechterung auftritt.
- Eine Sicherheitsschwachstelle eingeführt wird.
- Kritische Geschäftsfunktionen beeinträchtigt werden.

Rollback-Entscheidungsinstanz: dieselbe Genehmigungsinstanz wie für die ursprüngliche Änderung (oder höher für Notfall-Rollbacks).

### Rollback-Testing

Für Änderungen mit **hohem** und **kritischem** Risiko sind Rollback-Verfahren:

- Als Teil des Change Requests zu dokumentieren und zu genehmigen.
- **In Nicht-Produktionsumgebungen zu testen** vor der Produktionsimplementierung (wo machbar).
- Verifiziert als ausführbar innerhalb des definierten Rollback-Fensters.

Das Rollback-Testing verifiziert:

- Rollback-Verfahrensschritte sind korrekt und vollständig.
- Rollback kann innerhalb des Änderungsfensters abgeschlossen werden.
- Datenintegrität wird während des Rollbacks aufrechterhalten.
- Service-Wiederherstellung ist bestätigt.

Wo Rollback-Testing nicht machbar ist (Einwegmigrationen, destruktive Änderungen), ist ein **Vorwärts-Fix-Plan** als Alternative zum Rollback zu dokumentieren.

---

## Kommunikation

### Benachrichtigung der Stakeholder

Betroffene Stakeholder sind über Änderungen zu informieren, einschliesslich:

- Änderungsplan und Zeitpunkt.
- Erwartete Serviceauswirkungen (Dauer, Umfang).
- Erforderliche Benutzeraktionen (sofern zutreffend).
- Kontaktinformationen für Support während der Änderung.

**Geplante Änderungen**: Minimale Vorankündigungsfrist gemäss Organisationsanforderungen (empfohlen: 5 Werktage für hohe Auswirkungen, 2 Werktage für mittlere Auswirkungen).

**Notfalländerungen**: Kommunikation so schnell wie sicher möglich.

**Abschluss der Änderung**: Bestätigung wird an Stakeholder gesendet, wenn die Änderung abgeschlossen ist.

---

## Notfalländerungen

### Kriterien für die Notfallklassifikation

Änderungen dürfen nur dann als Notfall klassifiziert werden, wenn:

- Ein aktiver Sicherheitsvorfall oder eine aktiv ausgenutzte Schwachstelle behoben wird.
- Ein kritischer Service-Ausfall behoben wird.
- Ein drohender Systemausfall verhindert wird.
- Eine dringende regulatorische Anforderung erfüllt wird.
- Eine aktive Datenpanne eingedämmt wird.

Die Notfallklassifikation darf **nicht** für Bequemlichkeit, mangelnde Planung, Routinearbeiten oder gewünschte Funktionen verwendet werden.

### Notfall-Change-Prozess

1. Notfallbegründung dokumentieren (auch wenn kurz).
2. Genehmigung durch ISB oder IT-Operations-Manager (mindestens).
3. Risikoangemessenes Testing (verkürzte Testfälle oder dokumentierte Risikoakzeptanz, wenn Testing nicht machbar ist).
4. Implementierung mit erweitertem Monitoring.
5. Rollback-Plan vor der Ausführung vorhanden.
6. Retrospektives CAB-Review innerhalb von **48 Stunden**.
7. Obligatorische Post-Implementation Review innerhalb von **5 Werktagen**.

### Monitoring von Notfalländerungen

Der Prozentsatz von Notfalländerungen wird monatlich erfasst. Ziel: **<5%** aller Änderungen.

Wenn Notfalländerungen zwei aufeinanderfolgende Monate 5% überschreiten:

1. Ursachenanalyse durch Change Manager innerhalb von **14 Tagen**.
2. Ergebnisse dem CAB und ISB vorgestellt.
3. Korrekturmassnahmen innerhalb von **30 Tagen** implementiert, die Folgendes umfassen können: zusätzliche Schulung zur Änderungsklassifikation, Prozessverbesserungen (z.B. schnellere Genehmigungsworkflows für dringende, aber nicht notfallmässige Änderungen), Ressourcenanpassungen oder Disziplinarmassnahmen bei Missbrauch der Notfallklassifikation.
4. Nachkontrolle nach **60 Tagen** zur Verifizierung der Wirksamkeit.

**Missbrauch der Notfallklassifikation**: Die unangemessene Verwendung der Notfallklassifikation (Bequemlichkeit, mangelnde Planung) stellt einen Richtlinienverstos dar und ist an den ISB zu eskalieren.

---

## Post-Implementation Review (PIR)

Post-Implementation Reviews sind durchzuführen für:

- **Alle Notfalländerungen** (obligatorisch).
- **Alle fehlgeschlagenen Änderungen** (obligatorisch).
- **Normal Changes, die als hoch riskant oder kritisch klassifiziert sind**.

### PIR-Inhalt

- Erreichte Ziele im Vergleich zu den geplanten Ergebnissen.
- Während der Implementierung aufgetretene Probleme.
- Wirksamkeit von Planung und Testing.
- Benutzerrückmeldungen und Serviceauswirkungen.
- Erkenntnisse und Verbesserungsmöglichkeiten.
- Ob die Änderung in den Standard-Change-Katalog aufgenommen werden sollte.

### PIR-Zeitplanung

- Notfalländerungen: innerhalb von **5 Werktagen**.
- Fehlgeschlagene Änderungen: innerhalb von **5 Werktagen**.
- Hochriskante Normal Changes: innerhalb von **14 Werktagen**.

---

## Änderungs-Freeze-Perioden

Zu kritischen Zeiten des Jahres kann die Organisation eine Änderungs-Freeze-Periode verhängen, während der nur Notfalländerungen zulässig sind.

Änderungs-Freeze-Perioden:

- Werden durch das Geschäftsleitung oder den ISB genehmigt.
- Werden allen Stakeholdern im Voraus (mindestens 2 Wochen) kommuniziert.
- Werden im Änderungskalender dokumentiert.
- Beispiele: Jahresend-Finanzabschluss, wichtige Produktlaunches, geschäftliche Hochzeiten, Einreichungsfristen für Regulierungsbehörden.

---

## Aufzeichnungspflichten und Dokumentation

### Änderungsaufzeichnungen

Vollständige Änderungsaufzeichnungen sind zu führen, einschliesslich:

- Alle Change-Request-Informationen.
- Genehmigungsaufzeichnungen mit Zeitstempeln und Genehmigenden.
- CAB-Review-Notizen und Empfehlungen.
- Implementierungsprotokolle und Verifizierungsergebnisse.
- Kommunikationsaufzeichnungen.
- Probleme oder Vorfälle während der Implementierung.
- Rollback-Entscheidungen und -Ausführung (sofern zutreffend).
- Post-Implementation-Review-Ergebnisse.

Änderungsaufzeichnungen sind für mindestens **3 Jahre** für den operativen Referenzbedarf und **7 Jahre** als Audit-Nachweis aufzubewahren.

### Dokumentationsaktualisierungen

Nach Systemänderungen ist folgende Dokumentation innerhalb von **5 Werktagen** zu aktualisieren:

- Systemkonfigurationsdokumentation.
- Netzwerkdiagramme und -topologie.
- Betriebsprozeduren und Runbooks.
- Disaster-Recovery-Verfahren (wenn die Änderung kritische Systeme oder RTO/RPO betrifft).

---

## Integration mit dem Konfigurationsmanagement

Change Management und Konfigurationsmanagement sind komplementäre Disziplinen:

- **Change Management** kontrolliert *wie* Änderungen vorgenommen werden (Genehmigung, Testing, Implementierung).
- **Konfigurationsmanagement** kontrolliert *was* der aktuelle Zustand ist (Baselines, Versionen, Konfigurationselemente).

**Integrationspunkte**:

- Konfigurations-Baselines sind nach genehmigten Änderungen zu aktualisieren.
- Konfigurationsdrift-Erkennung (Ist vs. Baseline) löst Untersuchung und einen korrigierenden Change Request aus.
- Die Configuration Management Database (CMDB) oder ein äquivalentes Inventar ist die massgebliche Quelle für die Auswirkungsbeurteilung (welche Systeme betroffen sind).

Siehe **Konfigurationsmanagement-Richtlinie (A.8.9)** für detaillierte Baseline- und Versionskontrollanforderungen.

---

## Nicht autorisierte Änderungen

Nicht autorisierte Änderungen — Änderungen, die ohne Einhaltung des Change-Management-Prozesses vorgenommen werden — sind:

- Durch Monitoring, Audit-Protokollierung und Konfigurationsmanagement-Tools zu erkennen.
- Zur Bestimmung der Grundursache und Auswirkung zu untersuchen.
- Dem ISB zu melden und an das Management Review Team zu eskalieren.
- Korrektiven Massnahmen zu unterziehen, die je nach Schwere Disziplinarmassnahmen gemäss dem Disziplinarverfahren der Organisation umfassen können.

---

## Change-Incident-Korrelation

Wenn ein Sicherheitsvorfall oder ein Service-Ausfall eintritt, muss der Change Manager:

1. **Aktuelle Änderungen** innerhalb von 48 Stunden vor dem Vorfall-Beginn überprüfen.
2. **Vorfallszeitlinie** mit Änderungsimplementierungs-Zeitstempeln korrelieren.
3. **Potenziell verwandte Änderungen** identifizieren (gleiche Systeme, Abhängigkeiten, Zeitrahmen).
4. **CAB und ISB eskalieren**, wenn eine Änderung als Grundursache vermutet wird.

Wenn eine Änderung als Grundursache eines Vorfalls bestätigt wird:

- **Obligatorische Post-Implementation Review** innerhalb von **3 Werktagen**.
- **Ursachenanalyse** zur Identifikation von Prozesslücken (unzureichendes Testing, übersehene Auswirkungsbeurteilung, unzureichende Genehmigung).
- **Korrekturmassnahmen** zur Vermeidung von Wiederholungen.
- Wenn die Änderung im Standard-Change-Katalog war, ist der Katalogeintrag zu überprüfen und potenziell neu zu klassifizieren oder zu entfernen.

Die änderungsbedingte Vorfallsrate wird als Schlüsselkennzahl erfasst (Ziel: 0 pro Quartal).

---

## Change-Management-Kennzahlen

Das Informationssicherheitsmanagement-Team berichtet dem ISB mindestens vierteljährlich über Change-Management-Kennzahlen:

| Kennzahl | Ziel | Roter Schwellenwert |
|----------|------|---------------------|
| Änderungserfolgsquote (Änderungen ohne Rollback oder Vorfall abgeschlossen) | ≥95% | <85% |
| Anteil Notfalländerungen | <5% | >10% |
| PIR-Abschlussquote (für obligatorische PIRs) | 100% | <80% |
| Nutzung des Standard-Change-Katalogs | ≥30% aller Änderungen | <15% |
| Änderungsbedingte Vorfälle | 0 | >2 pro Quartal |
| Überfällige Änderungen (nach geplantem Implementierungstermin) | 0 | >5 |
| Dokumentationsaktualisierungs-Compliance (innerhalb von 5 Werktagen) | ≥95% | <80% |

Kennzahlen, die rote Schwellenwerte überschreiten, sind an den ISB zur sofortigen Aufmerksamkeit zu eskalieren und beim nächsten Management Review zu berichten.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung von hochriskanten und Notfalländerungen; Ausnahmeautorisierung; Kennzahlenüberprüfung |
| **Change Manager** | Prozesseigentümerschaft; CAB-Vorsitz; Standard-Change-Katalog-Pflege; Kennzahlen-Tracking; kontinuierliche Verbesserung |
| **IT-Operations-Manager** | Genehmigung mittlerer/hochriskanter Änderungen; Notfall-CAB-Vorsitz; Koordination der Änderungsfenster |
| **CAB-Mitglieder** | Änderungsüberprüfung, Auswirkungsbeurteilung, Risikoidentifikation, Genehmigungsempfehlungen |
| **Änderungsanfordernde** | Vollständige Change Requests mit geschäftlicher Begründung und Auswirkungsbeurteilung einreichen |
| **Änderungsimplementierende** | Genehmigte Änderungen gemäss dokumentierten Verfahren ausführen; Verifizierungstests durchführen |
| **Systemeigentümer** | Änderungen an eigenen Systemen genehmigen; Auswirkungsbeurteilung bereitstellen; für Systemverfügbarkeit verantwortlich |

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlich | Häufigkeit |
|---|----------|----------------|-----------|
| 1 | **Change-Management-System**-Aufzeichnungen (alle Change Requests mit erforderlichen Feldern) | Change Manager | *Pro Ereignis; vierteljährlich auditiert* |
| 2 | **CAB-Sitzungsprotokolle** (Teilnehmende, Entscheidungen, Begründungen, Aufgaben) | Change Manager | *Pro Sitzung; 3 Jahre aufbewahrt* |
| 3 | **Standard-Change-Katalog** mit Versionshistorie und vierteljährlichen Überprüfungsaufzeichnungen | Change Manager | *Vierteljährlich überprüft; versionskontrolliert* |
| 4 | **Änderungskalender** mit Freeze-Perioden und geplanten Änderungen | Change Manager | *Fortlaufend gepflegt; monatlich überprüft* |
| 5 | **Post-Implementation-Review**-Aufzeichnungen für Notfall-, fehlgeschlagene und hochriskante Änderungen | Change Manager | *Pro qualifizierender Änderung; Ziel: 100% Abschluss* |
| 6 | **Genehmigungsaufzeichnungen** mit Zeitstempeln, die die angemessene Instanz pro Risikoniveau zeigen | Change Manager | *Pro Änderung; 7 Jahre aufbewahrt* |
| 7 | **Testaufzeichnungen** (Testpläne, Ergebnisse, Freigaben) für Normal Changes und hochriskante Änderungen | IT Operations | *Pro Änderung; 3 Jahre aufbewahrt* |
| 8 | **Notfall-Change-Begründung** und retrospektive CAB-Review-Aufzeichnungen | ISB | *Pro Notfalländerung; monatlich überprüft* |
| 9 | **Change-Management-Kennzahlen**-Berichte | Change Manager | *Vierteljährlich; beim Management Review präsentiert* |
| 10 | **Nicht autorisierte Änderungs**-Untersuchungs- und Korrekturmassnahmen-Aufzeichnungen | ISB | *Pro Ereignis; 3 Jahre aufbewahrt* |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheitsmanagement-Team verifiziert die Einhaltung dieser Richtlinie durch verschiedene Methoden, darunter unter anderem Änderungsaufzeichnungsaudits, CAB-Sitzungsüberprüfungen, PIR-Abschluss-Tracking, Notfalländerungsanalyse, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom Information Security Manager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, kompensierenden Kontrollen und einem definierten Überprüfungsdatum. Ausnahmen sind dem Management Review Team zu berichten.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarisch belangt werden, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen an Change-Management-Standards, technologische Änderungen, neue Risiken, regulatorische Änderungen, PIR-Befunde sowie Erkenntnisse aus änderungsbedingten Vorfällen.

---

# Adressierte Bereiche des ISO 27001-Standards

Change-Management-Richtlinie — ISO 27001-Controls-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Engagement | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Verantwortlichkeiten des Managements |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Klausel 6.3 Planung von Änderungen | 5.37 Dokumentierte Betriebsprozeduren |
| Klausel 7.3 Bewusstsein | 6.3 Sensibilisierung, Schulung und Training zur Informationssicherheit |
| Klausel 8.1 Operative Planung und Kontrolle | 6.4 Disziplinarverfahren |
| | **8.32 Change Management** |
| | 8.9 Konfigurationsmanagement |
| | 8.19 Installation von Software auf Betriebssystemen |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|----------|
| Schweizerischer nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen (Change Management als organisatorische Massnahme zum Schutz von Datenverarbeitungssystemen) |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (sofern anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Change Management als angemessene Massnahme) |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.32 — Change Management |
| ISO/IEC 27002:2022 | Abschnitt 8.32 — Implementierungsleitfaden (9 obligatorische Elemente) |
| NIST SP 800-53 Rev 5 | CM-3 (Configuration Change Control), CM-4 (Impact Analyses), CM-5 (Access Restrictions for Change) |
| CIS Controls v8 | Control 2 (Inventar und Kontrolle von Software-Assets — Safeguard 2.5: Zulassungsliste autorisierter Software) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
