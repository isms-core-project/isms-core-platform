<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.6-DE:framework:POL:a.8.6 -->
**ISMS-POL-A.8.6 — Kapazitätsmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zum Kapazitätsmanagement |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.6 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB / Informationssicherheitsmanager | Erstfassung für die ISO 27001:2022-Zertifizierung |

**Überprüfungsrhythmus**: Jährlich (abgestimmt mit Kapazitätsplanungszyklus)
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Technische Überprüfung: IT-Betriebsleiter / Infrastrukturmanager
- Finanzüberprüfung: Finanzleiter (FL)
- Letzte Instanz: IT-Leiter (ITL)

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.8.6.1-UG/TG (Implementierung der Kapazitätsüberwachung)
- ISMS-IMP-A.8.6.2-UG/TG (Kapazitätsprognose und -planung)
- ISMS-IMP-A.8.6.3-UG/TG (Kapazitätsmanagement-Bewertung)
- ISO/IEC 27001:2022 Massnahme A.8.6

---

# Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für das Kapazitätsmanagement fest, um ausreichende Infrastruktur- und Anwendungskapazität gemäss ISO/IEC 27001:2022 Massnahme A.8.6 sicherzustellen.

**Zweck**: Organisatorische Anforderungen für die Governance des Kapazitätsmanagements festlegen. Diese Richtlinie legt fest, WAS für Kapazitätsmanagement-Massnahmen erforderlich sind, WANN Kapazitätsplanung stattfinden muss und WER dafür verantwortlich ist. Implementierungsverfahren (WIE Überwachung, Prognose und Planung durchgeführt werden) sind in der ISMS-IMP-A.8.6-Serie dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00, darunter ISO/IEC 27001:2022 Massnahme A.8.6. Bedingt anwendbare sektorspezifische Anforderungen (FINMA Rundschreiben 2023/1, DORA Art. 11, NIS2 Art. 21) gelten, wenn die Geschäftstätigkeit von [Organisation] deren Anwendbarkeit auslöst.

---

# Geltungsbereich

## Anwendbarkeit

**Diese Richtlinie gilt für**:

**Infrastrukturressourcen**:

- Rechenkapazität (Server, virtuelle Maschinen, Container, Cloud-Instanzen)
- Speicherkapazität (Festplattenspeicher, Datenbankspeicher, Backup-Speicher, Archiv-Speicher)
- Netzwerkkapazität (Bandbreite, Durchsatz, Verbindungen, Load-Balancer-Kapazität)
- Anwendungskapazität (gleichzeitige Nutzer, Transaktionsraten, API-Ratenbegrenzungen)
- Cloud-Kapazität (Cloud-Dienstkontingente, Limits, Instanzanzahlen)
- Physische Infrastruktur (Stromkapazität, Kühlkapazität, Rack-Platz gemäss A.7.11)

**Abdeckung**:

- Alle Infrastruktur, die Produktionsgeschäftsbetriebe unterstützt (verbindlich)
- Entwicklungs-, Test- und Qualitätssicherungsumgebungen (empfohlen)
- Business-Continuity- und Notfallstandorte (gemäss A.5.30)
- Extern gehostete Infrastruktur (wo [Organisation] Kapazitätsmanagement-Verantwortung hat)

**Personal**:

- Geschäftsleitung (Genehmigung des Kapazitätsplanungsbudgets)
- Kapazitätsplanungsteam (Überwachung, Prognose, Planung, Reporting)
- IT-Betriebsteam (tägliche Überwachung, Alarmreaktion)
- Anwendungseigentümer/Systemeigentümer (Geschäftswachstumsprognosen)
- Finanzverantwortlicher/FL (Genehmigung des Kapazitätsbudgets)

**Nicht im Geltungsbereich**:

- Anwendungsleistungsoptimierung (abgedeckt durch Anwendungsoptimierung)
- Softwarelizenzmanagement (abgedeckt durch Asset-Management)

## ISO/IEC 27001:2022 Massnahmenausrichtung

**ISO/IEC 27001:2022 Anhang A.8.6 — Kapazitätsmanagement**

> *Die Nutzung von Ressourcen sollte überwacht und abgestimmt werden, und Prognosen des zukünftigen Kapazitätsbedarfs sollten erstellt werden, um die erforderliche Systemleistung sicherzustellen und Investitionsentscheidungen zu unterstützen.*

**Massnahmenziel**: Sicherstellen, dass ausreichende Ressourcen zur Erfüllung aktueller und zukünftiger Leistungs- und Verfügbarkeitsanforderungen durch Überwachung, Abstimmung und Prognose verfügbar sind.

## Richtlinienintegration

Diese Massnahme integriert sich mit:

- **A.8.16 — Überwachungsaktivitäten**: Kapazitätskennzahlen als Teilmenge der Gesamtüberwachung
- **A.8.14 — Redundanz**: Kapazitätsplanung für Failover-Szenarien
- **A.8.13 — Informations-Backup**: Backup-Speicherkapazitätsplanung
- **A.7.11 — Versorgungseinrichtungen**: Physische Infrastrukturkapazität (Strom, Kühlung)
- **A.5.30 — IKT-Bereitschaft für Business Continuity**: Kapazität des Wiederherstellungsstandorts

---

# Richtlinienaussagen

## Anforderungen an die Kapazitätsüberwachung

[Organisation] muss Kapazitätsüberwachung für alle Infrastruktur- und Anwendungsressourcen, die Geschäftsbetriebe unterstützen, mit folgenden Merkmalen implementieren:

- **Metrik-Erfassungsfrequenz**: Mindestens alle 5 Minuten für Produktionssysteme, alle 15 Minuten für Nicht-Produktionssysteme
- **Datenvollständigkeit**: 99,5 % Metrikverfügbarkeit (ausschliesslich geplanter Wartungsfenster)
- **Alarmzustellung**: Alarme bei Schwellenwertüberschreitung innerhalb von 5 Minuten nach Erkennung zugestellt
- **Abdeckungsverifikation**: Monatliche Bewertung gemäss ISMS-IMP-A.8.6.3

**Überwachungsabdeckungsanforderungen**:

- Produktionssysteme: 100 % Überwachungsabdeckung erforderlich
- Nicht-Produktionssysteme: 90 % Überwachungsabdeckung empfohlen
- Cloud-Infrastruktur: Alle Cloud-Dienste und -Ressourcen überwacht
- Netzwerkinfrastruktur: Bandbreite, Durchsatz und Verbindungen überwacht
- Physische Infrastruktur: Strom- und Kühlkapazität gemäss A.7.11 überwacht

**Datenaufbewahrungsanforderungen**:

- Rohdaten: Mindestens 30 Tage für Vorfalluntersuchungen
- Aggregierte Metriken: Mindestens 12 Monate für Trendanalysen
- Historische Daten: Mindestens 36 Monate für strategische Planung

## Anforderungen an Kapazitätsschwellenwerte

[Organisation] muss Kapazitätsschwellenwerte für alle überwachten Ressourcen definieren und implementieren.

**Schwellenwertrahmen**:

- **Warnschwellenwert**: Löst Kapazitätsplanungsaktivitäten vor Erschöpfung aus
- **Kritischer Schwellenwert**: Löst sofortige Massnahmen zur Verhinderung der Erschöpfung aus
- **Maximale Kapazität**: Absolute Grenze, die eine sofortige Reaktion erfordert

Schwellenwerte werden vierteljährlich überprüft und auf Basis von Fehlalarmraten, Beinahe-Vorfällen und Workload-Musteränderungen angepasst.

## Anforderungen an Kapazitätsalarme

[Organisation] muss Alarmierung für Schwellenwertüberschreitungen implementieren mit:

- Weiterleitung an geeignete Teams basierend auf Schweregrad
- Eskalationsverfahren für nicht bestätigte Alarme
- Integration mit Incident-Management-Prozessen

## Anforderungen an Kapazitätsprognosen

[Organisation] muss Kapazitätsprognosen für alle kritischen Infrastruktur- und Anwendungsressourcen entwickeln.

**Prognoseanforderungen**:

- Kurzfristige Prognosen: 3–6 Monate (taktische Planung)
- Mittelfristige Prognosen: 6–12 Monate (Budgetplanung)
- Langfristige Prognosen: 12–24 Monate (strategische Planung)

**Aktualisierungsfrequenz**:

- Monatlich: Aktualisierungen kurzfristiger Prognosen
- Vierteljährlich: Umfassende Prognoseüberprüfung
- Jährlich: Strategische Prognose abgestimmt mit Budgetzyklus

**Genauigkeitsziel**: Prognosen innerhalb von ±15 % der tatsächlichen Auslastung (vierteljährlich gemessen).

**Ausnahmen beim Genauigkeitsziel**:
- Neue Systeme (erste 6 Monate nach Inbetriebnahme): ±30 % Genauigkeit akzeptabel während Baseline-Ermittlung
- Hoch variable Workloads (Systeme mit > 50 % Auslastungsvarianz): ±25 % Genauigkeit mit ITL-Genehmigung
- Programmreife (erste 12 Monate des Programms): ±20 % Genauigkeitsziel, ab dann ±15 %

**Genauigkeitsmessung**:
- Vierteljährliche Berechnung: (Tatsächliche Auslastung − Prognostizierte Auslastung) / Prognostizierte Auslastung
- Dokumentiert in ISMS-IMP-A.8.6.2-Arbeitsmappe mit Trendanalyse
- Ursachenanalyse erforderlich für Abweichungen > 15 % (innerhalb von 10 Arbeitstagen abgeschlossen)

## Anforderungen an die Kapazitätsplanung

[Organisation] muss einen strukturierten Kapazitätsplanungsprozess implementieren.

**Planungszyklusanforderungen**:

- Monatliche Überprüfung: Kapazitätsalarme, Beinahe-Vorfälle, kurzfristige Prognosen
- Vierteljährliche Planung: Umfassende Planung mit 12-Monats-Horizont
- Jährliches Budget: Langfristige Planung abgestimmt mit Budgetzyklus

**Genehmigungsanforderungen**:

- Routinemässige Kapazität: IT-Direktor/ITL innerhalb des genehmigten Budgets
- Grössere Kapazität: FL-Genehmigung bei Budgetauswirkung
- Notfallkapazität: ITL-Schnellgenehmigung mit Executive-Benachrichtigung

## Anforderungen an Kapazitätsberichte

[Organisation] muss regelmässige Kapazitätsberichte erstellen:

- **Monatlich**: Auslastungszusammenfassung, Vorfälle, Prognosehöhepunkte, Massnahmen
- **Vierteljährlich**: Umfassende Prognosen, Erweiterungspläne, Gesundheits-Scorecard
- **Jährlich**: Strategischer Kapazitätsplan mit mehrjährigen Prognosen

**Berichtsnachweisanforderungen**:
- Berichte werden aus der Überwachungsplattform über ISMS-IMP-A.8.6 Python-Skripte erstellt
- Monatliche Berichte: An IT-Führungsteam geliefert, in GRC-Plattform/SharePoint gespeichert
- Vierteljährliche Berichte: Dem Kapazitätsplanungsausschuss mit Sitzungsprotokollen vorgelegt
- Jahresberichte: Vom ITL genehmigt, in Managementüberprüfung einbezogen (ISO 27001 Abschnitt 9.3)

## Nachweisanforderungen für das Kapazitätsmanagement

[Organisation] muss überprüfbare Nachweise für Kapazitätsmanagement-Aktivitäten führen.

**Überwachungsnachweise**:
- Metrikdaten: 30 Tage Rohdaten, 12 Monate aggregiert, 36 Monate historisch
- Abdeckungsbewertungen: Monatlich gemäss ISMS-IMP-A.8.6.3, aufbewahrt 12 Monate
- Schwellenwertkonfigurationen: Aktuelle Konfiguration mit vierteljährlicher Überprüfungsdokumentation, aufbewahrt 24 Monate

**Prognose-Nachweise**:
- Kapazitätsprognosen: Alle Prognosen aufbewahrt 36 Monate
- Genauigkeitsbewertungen: Vierteljährliche Berechnungen gemäss ISMS-IMP-A.8.6.2, aufbewahrt 36 Monate
- Ursachenanalysen: Abweichungen > 15 % dokumentiert und aufbewahrt 24 Monate

**Planungsnachweise**:
- Sitzungsprotokolle des Kapazitätsplanungsausschusses: Aufbewahrt 36 Monate
- Erweiterungspläne: Genehmigte Pläne aufbewahrt 36 Monate
- Ausnahmeanfragen: Alle Anfragen mit Genehmigungen aufbewahrt bis Behebung + 12 Monate

## Fehlerszenarien und Reaktion im Kapazitätsmanagement

**Fehlschlagen der Prognosegenauigkeit**:
- Bei Prognoseabweichung > 15 %: Infrastrukturmanager führt Ursachenanalyse innerhalb von 10 Arbeitstagen durch
- Analyse dokumentiert: Prognoseannahmen, tatsächlicher vs. prognostizierter Vergleich, Abweichungsursachen, Methodikverbesserungen
- Ergebnisse werden dem Kapazitätsplanungsausschuss vorgestellt und in den nächsten Prognosezyklus einbezogen
- Bei Abweichung > 30 %: ITL-Benachrichtigung erforderlich mit Prozessverbesserungsplan

**Kapazitätserschöpfungsereignisse**:
- Bei Überschreitung des kritischen Kapazitätsschwellenwerts: IT-Betrieb implementiert sofort Gegenmassnahmen gemäss Runbook
- Bei Kapazitätserschöpfung (Dienstauswirkung): Klassifizierung als Priorität-1-Vorfall gemäss ISMS-POL-A.5.24-28
- Post-Incident-Review umfasst: Warum Überwachung/Prognose Erschöpfung nicht verhindert hat, Schwellenwertanpassung, Prozessverbesserungen

**Überwachungsabdeckungslücken**:
- Bei Produktionsabdeckung unter 100 %: Infrastrukturmanager erstellt Behebungsplan innerhalb von 5 Arbeitstagen
- Abschluss erforderlich innerhalb von 30 Tagen für Produktionssysteme, 60 Tagen für Nicht-Produktionssysteme
- Bei Ausfall der Überwachung kritischer Systeme: Sofortige Eskalation an ITL + ISB innerhalb von 4 Stunden
- Notfallbehebung (manuelle Überwachung) innerhalb von 24 Stunden erforderlich

**Integration des Lückenregisters**:
Alle Nichtkonformitäten im Kapazitätsmanagement werden im Lückenregister erfasst mit: Lücken-ID, Massnahmenreferenz (A.8.6), Beschreibung, Risikobewertung, Korrekturmassnahmenplan (wer, was, wann), Verifikationsmethode. Lückenregister monatlich vom IT-Führungsteam überprüft.

---

# Rollen und Verantwortlichkeiten

## Geschäftsleitung (GF, Vorstand)

- Letztendliche Verantwortung für ausreichende Kapazität zur Unterstützung des Geschäftsbetriebs
- Grössere Kapazitätsinvestitionen und strategische Kapazitätspläne genehmigen
- Ausreichende Budgetzuweisung für das Kapazitätsmanagementprogramm sicherstellen

## IT-Leiter (ITL)

- Gesamtverantwortung für Wirksamkeit des Kapazitätsmanagementprogramms
- Sicherstellen, dass Kapazitätspuffer organisatorische Ziele erfüllen:
  - Produktionssysteme: Mindestens 20 % Puffer bei Spitzenauslastung
  - Speichersysteme: Mindestens 3 Monate Puffer bei aktuellem Wachstum
  - Netzwerkbandbreite: Mindestens 30 % Puffer während der Geschäftszeiten
- Kapazitätsanforderungen mit Budgetbeschränkungen abwägen

**Befugnisse**:

- Kapazitätserweiterungspläne innerhalb des Budgets genehmigen
- Notfall-Kapazitätsbeschaffung autorisieren
- IT-Ressourcen für Kapazitätsplanung zuweisen

## Informationssicherheitsbeauftragter (ISB)

- Kapazität für Sicherheitssysteme sicherstellen (SIEM, Protokollierung, Überwachung, EDR)
- Risikobewertung für kapazitätsbezogene Sicherheitsprobleme
- Compliance-Verifikation für Kapazitätsmanagement-Massnahmen (ISO 27001 A.8.6)

**Befugnisse**:

- Kapazitätsplanung für Sicherheitssysteme fordern
- Richtlinie zum Kapazitätsmanagement genehmigen
- Kapazitätsrisiken mit Auswirkungen auf den Sicherheitsstatus eskalieren

## Kapazitätsplanungsteam / Infrastrukturmanager

- Tägliche Ausführung des Kapazitätsmanagementprogramms
- Kapazitätsüberwachung, Prognose und Trendanalyse
- Kapazitätserweiterungsplanung und -koordination
- Kapazitätsreporting an das Management

**Befugnisse**:

- Kapazitätsüberwachung für alle Ressourcen implementieren
- Kapazitätsschwellenwerte und Alarmregeln definieren
- Kapazitätserweiterungspläne empfehlen

## IT-Betriebsteam

- Tägliche Kapazitätsüberwachung und Alarmreaktion
- Sofortige Reaktion auf Kapazitätsvorfälle
- Deployment genehmigter Kapazitätserweiterungen

**Befugnisse**:

- Notfall-Kapazitätsgegenmassnahmen ausführen
- Genehmigte Kapazitätsanpassungen und -optimierungen implementieren
- Kapazitätsprobleme gemäss Verfahren eskalieren

## Anwendungseigentümer / Systemeigentümer

- Geschäftswachstumsprognosen für die Kapazitätsplanung bereitstellen
- An der Kapazitätsplanung für ihre Anwendungen mitwirken
- Budget für Anwendungskapazitätsanforderungen bereitstellen

## Finanzleiter (FL)

- Kapazitätsmanagement-Budgets genehmigen (CapEx und OpEx)
- Finanzreporting über Kapazitätsinvestitionen
- Kostenoptimierungsaufsicht

---

# Governance und Compliance

## Richtlinien-Governance-Rahmen

**Richtlinieneigentümer**: Informationssicherheitsbeauftragter (ISB)
**Richtliniengenehmiger**: IT-Leiter (ITL)
**Richtlinienüberprüfung**: Jährliche Überprüfung abgestimmt mit Kapazitätsplanungszyklus

**Governance-Gremien**:

**Kapazitätsplanungsausschuss** (Operativ):

- Vorsitz: Infrastrukturmanager oder Kapazitätsplanungsmanager
- Kernmitglieder: IT-Betriebsleiter, Anwendungseigentümer, Netzwerkmanager, Cloud-Architekt
- Unternehmensvertreter: Geschäftseinheitsleiter oder Produktmanager (für Wachstumsprognosen)
- Finanzvertreter: Finanzmanager oder Budgetanalyst (für Budgetplanung)
- Häufigkeit: Monatlich
- Zweck: Kapazitätsstatus überprüfen, Prognosen besprechen, Erweiterungen planen, mit Geschäfts-Roadmap abstimmen

**IT-Führungsteam** (Strategisch):

- Mitglieder: ITL, ISB, FL, IT-Direktor
- Häufigkeit: Vierteljährlich
- Zweck: Kapazitätsberichte überprüfen, Budgets genehmigen, strategische Entscheidungen

## Regulatorische Compliance

Diese Richtlinie erfüllt Anforderungen gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)**:

**Stufe 1 — Verbindliche Compliance**:

- **ISO/IEC 27001:2022**: Massnahme A.8.6 (Kapazitätsmanagement)

**Stufe 2 — Bedingte Anwendbarkeit** (wo Geschäftstätigkeit auslöst):

- **FINMA Rundschreiben 2023/1** (Schweizer Finanzinstitute): Operationale IKT-Resilienz
- **DORA Art. 11** (EU-Finanzunternehmen): IKT-Kapazitätsplanung
- **NIS2 Art. 21(2)** (Wesentliche/wichtige Einrichtungen): Business-Continuity-Kapazität

**Stufe 3 — Informationsleitlinien**:

- ITIL 4 Kapazitätsmanagement
- NIST SP 800-53 AU-6

## Richtlinienausnahmen

**Temporäre Ausnahmen — Kritische Systeme** (essenzielle Geschäftsbetriebe gemäss BIA):
- Maximale Dauer: 3 Monate
- Genehmigt durch: ITL + ISB (gemeinsame Genehmigung erforderlich)
- Bedingungen: Kompensierende Massnahmen erforderlich, Risikoakzeptanz dokumentiert, wöchentliche Statusüberprüfung

**Temporäre Ausnahmen — Nicht kritische Systeme**:
- Maximale Dauer: 6 Monate
- Genehmigt durch: IT-Direktor oder ITL
- Bedingungen: Risikoakzeptanz dokumentiert, monatliche Statusüberprüfung

**Dauerhafte Ausnahmen**:

- Genehmigt durch: ITL + ISB + Geschäftsleitung
- Dokumentation: Formelle Risikoakzeptanz, kompensierende Massnahmen
- Überprüfung: Jährliche Neu-Genehmigung erforderlich

## Compliance-Verifikation

**Monatliche Selbstbewertung** (gemäss ISMS-IMP-A.8.6.3):
- **Durchgeführt von**: Infrastrukturmanager oder designiertes Kapazitätsplanungsteam-Mitglied
- **Umfang**: Überwachungsabdeckung %, Schwellenwertkonfiguration, Prognosevollständigkeit, Reporting-Aktualität
- **Ergebnis**: ISMS-IMP-A.8.6.3 Python-generierte Arbeitsmappe mit Bestanden/Nicht-bestanden-Ergebnissen
- **Überprüfung**: Dem IT-Betriebsleiter innerhalb von 10 Arbeitstagen nach Monatsende vorgelegt
- **Verfolgung**: Nichtkonformitäten im Lückenregister erfasst

**Vierteljährliche interne Prüfung**:
- **Durchgeführt von**: Interne Prüfungsfunktion oder ISB-designierter Prüfer (unabhängig vom Kapazitätsplanungsteam)
- **Umfang**: Stichprobe von 3 kritischen Systemen, Überwachungskonfiguration verifizieren, letzte 3 Monate Prognosen überprüfen
- **Ergebnis**: Prüfbericht mit Befunden, Nachweisproben, Empfehlungen
- **Überprüfung**: Dem IT-Führungsteam innerhalb von 15 Arbeitstagen nach Quartalsende vorgelegt

**Jährliche externe Prüfung**:
- **Durchgeführt von**: ISO 27001-Zertifizierungsprüfer
- **Umfang**: Vollständige Massnahmenbewertung gemäss ISO 27001:2022 A.8.6
- **Reaktion**: ISB koordiniert Reaktion, Korrekturmassnahmenpläne innerhalb von 30 Tagen

**Kapazitätsmanagement-Programm KPIs** (vierteljährlich gemeldet):

| KPI-Kategorie | Kennzahl | Ziel |
|--------------|---------|------|
| **Verfügbarkeit** | Kapazitätsbezogene Vorfälle pro Quartal | < 2 |
| **Verfügbarkeit** | Durchschnittliche Zeit bis zur Kapazitätserweiterung | < 30 Tage ab Genehmigung |
| **Verfügbarkeit** | Notfall-Kapazitätsbeschaffungen pro Jahr | < 3 |
| **Genauigkeit** | Prognosegenauigkeit | ± 15 % |
| **Genauigkeit** | Fehlalarmrate | < 10 % |
| **Genauigkeit** | Überwachungsdatenvollständigkeit | > 99 % |
| **Effizienz** | Durchschnittlicher Puffer über Systeme | 15–30 % |
| **Effizienz** | Durchschnittliche Auslastung bei Spitze | 70–85 % |
| **Effizienz** | Budgetabweichung (tatsächlich vs. geplant) | ± 10 % |

KPIs werden vierteljährlich an das IT-Führungsteam und jährlich an das Geschäftsleitung gemeldet.

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Kapazitätsmanagement** | Prozess zur Sicherstellung ausreichender Ressourcen zur Erfüllung aktueller und zukünftiger Leistungs- und Verfügbarkeitsanforderungen |
| **Kapazitätsüberwachung** | Kontinuierliche Messung der Ressourcenauslastung zum Verständnis des Verbrauchs und zur Trendverfolgung |
| **Kapazitätsplanung** | Proaktiver Prozess zur Bestimmung zukünftiger Kapazitätsanforderungen und Entwicklung von Erweiterungsplänen |
| **Kapazitätsschwellenwert** | Definierter Auslastungsgrad, der Alarme oder Massnahmen auslöst, wenn er überschritten wird |
| **Kapazitätsprognose** | Projektion zukünftiger Kapazitätsanforderungen basierend auf Trends und Geschäftsplänen |
| **Puffer (Headroom)** | Verbleibende ungenutzte Kapazität, verfügbar für Wachstum oder unerwarteten Bedarf |

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **IT-Leiter (ITL)** | [Name] | [Date to be set] |
| **Finanzleiter (FL)** | [Name] | [Date to be set] |
| **IT-Betriebsleiter** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Kapazitätsmanagement-Anforderungen fest. Implementierungsverfahren sind in ISMS-IMP-A.8.6.1 (Implementierung der Kapazitätsüberwachung), ISMS-IMP-A.8.6.2 (Kapazitätsprognose und -planung) und ISMS-IMP-A.8.6.3 (Kapazitätsmanagement-Bewertung) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
