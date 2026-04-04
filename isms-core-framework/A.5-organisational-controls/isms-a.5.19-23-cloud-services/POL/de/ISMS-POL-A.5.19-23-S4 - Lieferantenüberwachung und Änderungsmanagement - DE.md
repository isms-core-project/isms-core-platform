<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S4-DE:framework:POL:a.5.19-23-s4 -->
**ISMS-POL-A.5.19-23-S4 — Lieferantenüberwachung & Änderungsmanagement**
**Massnahme A.5.22: Überwachung, Überprüfung und Änderungsmanagement von Lieferantendiensten**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Lieferantenüberwachung & Änderungsmanagement |
| **Dokumenttyp** | Richtlinienabschnitt |
| **Dokument-ID** | ISMS-POL-A.5.19-23-S4 |
| **Dokumentersteller** | Information Security Officer (ISO) |
| **Dokumenteigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISO | Erstfassung für ISO 27001:2022 Massnahme A.5.22 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Betrieb: IT-Leiter (ITL)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)
- ISMS-POL-A.5.19-23 (Übergeordnete Richtlinie – Lieferanten- und Cloud-Dienste-Sicherheit)
- ISMS-POL-A.5.19-23-S1 (Grundlagen der Lieferantenbeziehungen)
- ISMS-IMP-A.5.19-23.S4-UG/TG (Laufende Governance & Risikomanagement)
- ISMS-REF-A.5.23 (Cloud-Anbieter-Referenzregister)
- ISO/IEC 27001:2022 Massnahme A.5.22
- ISO/IEC 27036-4 (Cloud-Dienste)

---

# Zweck

Dieser Abschnitt definiert Anforderungen für die laufende Überwachung, regelmässige Überprüfung und das Änderungsmanagement von Lieferantendiensten. Er stellt sicher, dass die Sicherheitslage der Lieferanten kontinuierlich validiert wird und dass Änderungen keine unakzeptablen Risiken einführen.

**Kritischer Grundsatz – „Vertrauen degeneriert mit der Zeit"**: Ein Lieferant, der die anfängliche Due Diligence bestanden hat, bleibt nicht zwangsläufig sicher. Zertifizierungen laufen ab, Sicherheitspraktiken degenerieren, Eigentumsverhältnisse ändern sich und Vorfälle treten auf. Kontinuierliche Überwachung und regelmässige Neubewertung sind keine optionale Aufsicht – sie sind wesentliche Kontrollen, die Degradation erkennen, bevor sie zur Datenpanne wird. Diese Richtlinie erfordert systematische, evidenzbasierte Validierung während des gesamten Lieferantenbeziehungslebenszyklus.

**ISO/IEC 27001:2022 Massnahme A.5.22 – Überwachung, Überprüfung und Änderungsmanagement von Lieferantendiensten**

> *Die Organisation sollte regelmässig Informationssicherheitspraktiken und Dienstleistungserbringung von Lieferanten überwachen, überprüfen, bewerten und Änderungen daran managen.*

**Massnahmenziel**: Laufende Validierung der Lieferantensicherheitslage und kontrolliertes Management von Änderungen an Lieferantendiensten sicherstellen.

**Zusammenfassung der ISO/IEC 27002:2022-Leitlinien**:

- Lieferantenleistung soll kontinuierlich gegen vertragliche Verpflichtungen und SLAs überwacht werden
- Regelmässige Überprüfungen der Lieferantensicherheitspraktiken sollen basierend auf der Lieferantenrisikoeinstufung durchgeführt werden
- Änderungen an Lieferantendiensten sollen durch formale Änderungskontrollverfahren mit Sicherheitsprüfung gemanagt werden
- Lieferanten-Compliance mit Vereinbarungen soll durch Audits, Attestierungen oder Drittanbieter-Zertifizierungen verifiziert werden
- Lieferantenvorfälle und Sicherheitsereignisse sollen verfolgt, analysiert und angemessen behandelt werden
- Lieferantenaudits oder Drittanbieter-Attestierungen (SOC 2, ISO 27001) sollen eingeholt und auf Befunde geprüft werden
- Die Beziehung zu Lieferanten soll durch regelmässige Kommunikation, Überprüfungen und Governance-Meetings aufrechterhalten werden
- Dienstdegradation oder Non-Compliance des Lieferanten soll Eskalations- und Abhilfeverfahren einschliesslich möglicher Kündigung auslösen

---

# Geltungsbereich

## Überwachungsaktivitäten

| Aktivitätstyp | Beschreibung |
|---------------|-------------|
| **Leistungsüberwachung** | SLA-Compliance, Servicequalitätskennzahlen, Verfügbarkeitsverfolgung |
| **Sicherheitsüberwachung** | Sicherheitslagebewertung, Vorfallsverfolgung, Schwachstellenstatus, Zertifizierungsgültigkeit |
| **Compliance-Überwachung** | Zertifizierungsgültigkeit, regulatorische Compliance-Verifizierung, Auditbericht-Überprüfung |
| **Beziehungsüberwachung** | Kommunikationseffektivität, Problemlösung, Interessenvertreterzufriedenheit |
| **Änderungsüberwachung** | Dienst-, Personal-, Eigentums- und Infrastrukturänderungen |

## Anwendbarkeit nach Lieferantenstufe

| Aktivität | Stufe 1 (Kritisch) | Stufe 2 (Hoch) | Stufe 3 (Mittel) | Stufe 4 (Niedrig) |
|----------|--------------------|----------------|------------------|-------------------|
| Leistungsüberwachung | Kontinuierlich (automatisiert) | Monatliche Berichterstattung | Vierteljährlich | Jährlich |
| Sicherheitsbewertung | Jährlich umfassend | Jährlich Standard | Zweijährlich | Nur initial |
| Compliance-Verifizierung | Vierteljährliche Zertifikatsprüfung | Halbjährlich | Jährlich | Bei Verlängerung |
| Beziehungsüberprüfung | Vierteljährliche Governance | Halbjährlich | Jährlich | Bei Bedarf |
| Änderungsprüfung | Alle Änderungen vorab genehmigt | Wesentliche Änderungen geprüft | Nur signifikante | Standardbedingungen |

---

# Überprüfungszyklen

## Überprüfungsplan nach Lieferantenstufe

| Lieferantenstufe | Sicherheitsüberprüfung | Leistungsüberprüfung | Beziehungsüberprüfung |
|-----------------|----------------------|--------------------|-----------------------|
| **Stufe 1 (Kritisch)** | Jährlich umfassend + kontinuierliche Überwachung | Monatliche SLA-Berichte | Vierteljährliche Governance-Meetings |
| **Stufe 2 (Hoch)** | Jährliche Standardbewertung | Vierteljährliche Leistungsüberprüfung | Halbjährliche Beziehungsprüfung |
| **Stufe 3 (Mittel)** | Zweijährlicher Sicherheitsfragebogen | Halbjährlich | Jährliche Überprüfung |
| **Stufe 4 (Niedrig)** | Nur bei Verlängerung | Jährliche Zusammenfassung | Nur bei Verlängerung |

## Auslöser für ungeplante Überprüfungen

Über geplante Überprüfungen hinaus soll bei folgenden Ereignissen sofort eine Überprüfung durchgeführt werden:

| Auslöser | Überprüfungsumfang | Zeitrahmen |
|----------|------------------|-----------|
| Sicherheitsvorfall beim Lieferanten (bestätigt) | Vollständige Sicherheitsprüfung, Vertrags-Compliance | Innerhalb von 48 Stunden |
| Wesentliche Dienständerung (Architektur, Plattform, Standort) | Folgenabschätzung, Neubewertung des Risikos | Vor Implementierung |
| Eigentümerwechsel des Lieferanten (M&A, Akquisition) | Due-Diligence-Auffrischung, Vertragsprüfung | Innerhalb von 30 Tagen |
| Zertifizierungsablauf oder -verlust | Compliance-Prüfung, Risikobewertung | Sofort |
| Wesentliche Vertragsänderung oder -ergänzung | Sicherheitsklauselverifizierung, Folgenanalyse | Vor Abschluss |
| Regulatorische Änderung mit Auswirkung auf Lieferantenpflichten | Compliance-Bewertung, Gap-Analyse | Innerhalb von 60 Tagen |
| Negative Nachrichten oder Reputationsereignis (öffentlicher Vorfall) | Neubewertung des Risikos, Kommunikation mit Lieferanten | Innerhalb von 7 Tagen |
| Wesentliche Organisationsänderung ([Organisation] oder Lieferant) | Beziehungsüberprüfung, Zugriffsvalidierung | Innerhalb von 30 Tagen |
| Wiederholte SLA-Verstösse (3 aufeinanderfolgend oder 6 in 12 Monaten) | Leistungsüberprüfung, Abhilfeplan | Sofort |
| Auditbefund in Bezug auf Lieferanten | Compliance-Prüfung, Behebungsverfolgung | Innerhalb von 14 Tagen |

## Jährlicher Überprüfungskalender

```
┌─────────────────────────────────────────────────────────────┐
│ LIEFERANTENÜBERPRÜFUNGSKALENDER (Beispiel)                  │
├─────────────────────────────────────────────────────────────┤
│ Q1 (Jan–Mär):                                               │
│     • Stufe-1-Lieferanten – Jährliche Sicherheitsbewertung  │
│     • Alle Lieferanten – Zertifizierungsgültigkeitsprüfung  │
│     • Vertragsverlängerungen (Q1-Abläufe)                   │
│                                                             │
│ Q2 (Apr–Jun):                                               │
│     • Stufe-2-Lieferanten – Jährliche Sicherheitsbewertung  │
│     • Stufe-1-Lieferanten – Vierteljährliches Governance-   │
│       Meeting                                               │
│     • Halbjährliche Compliance-Prüfung                      │
│                                                             │
│ Q3 (Jul–Sep):                                               │
│     • Stufe-1-Lieferanten – Vierteljährliches Governance-   │
│       Meeting                                               │
│     • Stufe-3-Lieferanten – Jährliche Überprüfung (falls    │
│       in diesem Jahr fällig)                                │
│     • Vorbereitung auf Jahresabschlussberichterstattung     │
│                                                             │
│ Q4 (Okt–Dez):                                               │
│     • Stufe-1-Lieferanten – Vierteljährliches Governance-   │
│       Meeting                                               │
│     • Alle Lieferanten – Jährliche Registervalidierung      │
│     • Planung für nächsten Überprüfungszyklus               │
│     • Jahresabschluss-Compliance-Berichterstattung          │
└─────────────────────────────────────────────────────────────┘
```

---

# Leistungsüberwachung

## Service Level Monitoring

| Metrikkategorie | Beispiele | Überwachungshäufigkeit | Alarmierungsschwelle |
|-----------------|---------|----------------------|---------------------|
| Verfügbarkeit | Betriebszeit-Prozentsatz, ungeplante Ausfallzeitenvorfälle | Kontinuierlich/Echtzeit | Unter SLA-Ziel |
| Leistung | Reaktionszeit, Durchsatz, Latenz | Kontinuierlich/Echtzeit | >10 % Degradation |
| Support | Ticket-Reaktionszeit, Lösungszeit, Eskalationen | Wöchentliche Aggregation | SLA-Verletzung |
| Kapazität | Ressourcenauslastung, Skalierungsspielraum | Monatliche Trendanalyse | >80 % Auslastung |
| Qualität | Fehlerraten, Transaktionserfolgsrate, Kundenzufriedenheit | Monatliche Überprüfung | Über Baseline |

## SLA-Compliance-Verfolgung

| Element | Anforderung |
|---------|------------|
| Baseline-Festlegung | Vereinbarte SLA-Ziele in Vertrag und Überwachungssystem dokumentieren |
| Messmethodik | Tatsächliche Leistung gegen Ziele anhand objektiver Metriken verfolgen |
| Berichterstattungsrhythmus | Monatliche SLA-Compliance-Berichte vom Lieferanten mit unterstützenden Daten |
| Verletzungsverfolgung | Alle SLA-Verletzungen mit Ursachenanalyse, Folgenabschätzung, Behebung protokollieren |
| Service-Credits | Service-Credits gemäss Vertragsbedingungen für SLA-Versäumnisse verfolgen und einfordern |
| Trendanalyse | Auf Degradationsmuster überwachen, die auf systematische Probleme hinweisen |
| Eskalationsauslöser | Schwellenwerte für Eskalation definieren (z.B. 3 Verletzungen im Quartal) |

## Leistungsüberprüfungsprozess

**Für Lieferanten der Stufe 1 und 2:**

1. **Datenerhebung**: Vom Lieferanten bereitgestellte Berichte + interne Überwachungsdaten sammeln
2. **SLA-Vergleich**: Tatsächliche Leistung gegen vertragliche SLA-Ziele vergleichen
3. **Trendanalyse**: Muster, Degradationstrends, Anomalien identifizieren
4. **Problemdokumentation**: SLA-Verletzungen, Leistungsprobleme, Abhilfeanforderungen dokumentieren
5. **Überprüfungsmeeting**: Befunde im vierteljährlichen/halbjährlichen Lieferantenreview besprechen
6. **Behebungsverfolgung**: Lieferantenverpflichtungen verfolgen und Abschluss verifizieren
7. **Risikoaktualisierung**: Lieferantenrisikobewertung aktualisieren, wenn Leistung erhöhtes Risiko anzeigt
8. **Vertragsprüfung**: Bewerten, ob Leistung Vertragsverlängerung oder -neuverhandlung rechtfertigt

---

# Sicherheitsbewertung

## Bewertungsmethoden

| Methode | Beschreibung | Anwendbarkeit |
|---------|-------------|--------------|
| **Sicherheitsfragebogen** | Standardisierte Bewertung (200–300 Fragen für S1) | Alle Lieferanten mit Daten-/Systemzugang |
| **Nachweisüberprüfung** | Prüfung von Richtlinien, Verfahren, Konfigurationen, Logs | Stufe 1 und 2 |
| **Zertifizierungsprüfung** | Gültige ISO 27001, SOC 2 usw. verifizieren | Stufe 1, 2, 3 (falls anwendbar) |
| **Auditberichtprüfung** | Detaillierte Überprüfung von SOC 2 Type II, ISO-Überwachungsprüfungsergebnissen | Stufe 1 und 2 (erforderlich) |
| **Penetrationstestüberprüfung** | Externe Penetrationstest-Ergebnisse des Lieferanten prüfen | Stufe 1 (jährlich erforderlich) |
| **Schwachstellenbewertungsprüfung** | Schwachstellen-Scan-Ergebnisse des Lieferanten prüfen | Stufe 1 (vierteljährlich erforderlich) |
| **Vor-Ort-Bewertung** | Physischer Besuch und Inspektion von Einrichtungen/Kontrollen | Stufe 1 (risikobasiert, alle 2–3 Jahre) |
| **Technische Sicherheitstests** | Unabhängige Schwachstellen-Scans von lieferantenexponierten Schnittstellen | Stufe 1 (risikobasiert) |

## Bewertungsinhaltsdomänen

| Domäne | Bewertungsbereiche |
|--------|-------------------|
| **Governance & Organisation** | Sicherheitsrichtlinien, Organisationsstruktur, Rollen und Verantwortlichkeiten, Sicherheitsbewusstseinstraining |
| **Zugangskontrolle** | Authentifizierungsmechanismen, Autorisierungsmodelle, privilegiertes Zugriffsmanagement, Zugriffsüberprüfungsprozesse |
| **Datenschutz** | Datenklassifizierung, Verschlüsselung (Übertragung & Ruhezustand), Datenhandhabungsverfahren, Data Loss Prevention |
| **Betriebssicherheit** | Änderungsmanagement, Patch-Management, Konfigurationsmanagement, Backup und Wiederherstellung, Kapazitätsmanagement |
| **Störungsmanagement** | Erkennungsfähigkeiten, Reaktionsverfahren, Meldeprozesse, Post-Incident-Reviews |
| **Betriebskontinuität** | BC/DR-Pläne, Testnachweise, RTO/RPO-Fähigkeiten, geografische Redundanz |
| **Compliance** | Aktuelle Zertifizierungen, regulatorische Compliance-Nachweise, Behebung von Auditbefunden, vertragliche Compliance |
| **Lieferkette** | Sub-Lieferantenmanagement, Software-Abhängigkeiten (SBOM), Schwachstellenmanagement |

## Management von Bewertungsbefunden

| Befundschwere | Beschreibung | Reaktionszeitrahmen | Eskalationspfad |
|---------------|-------------|---------------------|----------------|
| **Kritisch** | Datenpannenrisiko, fehlende kritische Kontrollen, abgelaufene Verschlüsselung | Sofortiger Mitigierungsplan, 7 Tage Behebung | ISB + Geschäftsverantwortlicher + Geschäftsleitung |
| **Hoch** | Wesentliche Kontrolllücken, SLA-Verletzungen, teilweise Compliance | 30 Tage Behebung mit wöchentlichen Fortschrittsupdates | ISO + Geschäftsverantwortlicher + ISB-Benachrichtigung |
| **Mittel** | Kontrollverbesserungen nötig, Dokumentationslücken, geringfügige Non-Compliance | 90 Tage Behebung mit monatlichen Updates | ISO + Geschäftsverantwortlicher |
| **Niedrig** | Best-Practice-Empfehlungen, Dokumentationsverbesserungen | Nächster Überprüfungszyklus oder 6 Monate | Im Bewertungsprotokoll verfolgt |

**Befundverfolgung**: Alle Befunde sollen im Lieferantenmanagementsystem protokolliert werden mit:

- Befundbeschreibung und Nachweis
- Schweregradklassifizierung
- Lieferanten-Abhilfeplan und Zeitrahmen
- Verifizierungsmethode und -kriterien
- Statusverfolgung (Offen → In Bearbeitung → Verifiziert → Geschlossen)
- Abschlusnachweise

## Bewertungsdokumentation

Jede Bewertung soll umfassende Dokumentation erstellen:

| Dokument | Inhalt | Aufbewahrung |
|----------|--------|-------------|
| **Bewertungsbericht** | Umfang, Methodik, Befunde mit Nachweis, Lieferantenantworten | 5 Jahre |
| **Risikobewertungsaktualisierung** | Aktualisierter Lieferantenrisikowert basierend auf Bewertungsbefunden | Aktuell + 3 Jahre |
| **Abhilfeplan** | Erforderliche Massnahmen, zugewiesene Verantwortliche, Zeitrahmen, Verifizierungsmethode | Bis Abschluss + 2 Jahre |
| **Management-Zusammenfassung** | Überblick für Governance-Review-Meetings | 3 Jahre |
| **Compliance-Nachweis** | Geprüfte Zertifizierungen, Auditberichte, Testergebnisse | Aktuell + 3 Jahre |

---

# Compliance-Überwachung

## Zertifizierungsverfolgung

| Aktivität | Häufigkeit | Massnahme bei Ablauf/Versagen |
|-----------|-----------|-------------------------------|
| ISO 27001-Gültigkeitsprüfung | Vierteljährlich | Verlängerungsnachweis innerhalb von 30 Tagen anfordern, ISB-Eskalation wenn >60 Tage abgelaufen |
| SOC 2 Type II-Aktualität | Jährliche Anforderung (30 Tage vor Jahrestag) | Neuen Bericht anfordern, Gap-Risikobewertung bei Verzögerung |
| Cloud-Zertifizierungen (ISO 27017/27018, CSA STAR) | Jährlich | Verlängerung verifizieren, Auswirkung bei Einstellung bewerten |
| Regulatorische Compliance-Attestierungen | Jährlich | Bestätigungsschreiben der Lieferantenleitung anfordern |
| Penetrationstests | Jährlich | Aktuellen Bericht (<12 Monate) anfordern, kritische Befunde auf Behebung verifizieren |

## Anforderungen an Compliance-Nachweise

| Lieferantenstufe | Erforderliche Nachweise | Verifizierungsmethode |
|-----------------|------------------------|----------------------|
| **Stufe 1** | Gültige Zertifizierung + vollständiger Auditbericht + Behebungsnachweise für alle Befunde | Detaillierte Überprüfung, Befundabschluss verifizieren |
| **Stufe 2** | Gültige Zertifizierung + Auditberichtzusammenfassung oder Executive Summary | Auf wesentliche Befunde prüfen, kritische Punkte auf Abschluss verifizieren |
| **Stufe 3** | Gültige Zertifizierung (wenn im Rahmen der Due Diligence behauptet) | Nur Zertifikatverifizierung |
| **Stufe 4** | Nicht erforderlich | N/A |

**Zertifikatverifizierung**: Alle Zertifizierungen sollen bei der ausstellenden Stelle verifiziert werden:

- ISO 27001: IAF/Akkreditierungsstellen-Datenbank prüfen
- SOC 2: CPA-Firm-Lizenz verifizieren, AICPA-Bestätigung bei Bedarf anfordern
- Branchenzertifizierungen: Bei Zertifizierungsstelle verifizieren

## Reaktion auf Compliance-Versagen

| Szenario | Sofortmassnahme | Zeitrahmen | Eskalation |
|----------|----------------|-----------|------------|
| Zertifizierung abgelaufen (kürzlich) | 30-tägige Heilungsfrist, Risikobewertung, kompensierende Kontrollen | Lieferant muss innerhalb von 30 Tagen verlängern | Geschäftsverantwortlicher + ISO |
| Zertifizierung entzogen oder widerrufen | Sofortige Risikobewertung, Dienstaussetzung bis Erneuerung erwägen | 14 Tage zur Lösung oder Ersatzinitiierung | ISB + Geschäftsverantwortlicher |
| Auditversagen (wesentliche Befunde unbehoben) | Befunde überprüfen, Abhilfeplan mit Zeitrahmen fordern | 30 Tage Abhilfeplan, 90 Tage Umsetzung | ISO + Geschäftsverantwortlicher |
| Regulatorischer Verstoss oder Sanktion | Rechtliche Prüfung, Exposition der [Organisation] bewerten, Risikoakzeptanz oder Exit-Strategie dokumentieren | Sofortige Rechtsberatung | Recht + ISB + Geschäftsleitung |
| Wiederholte Non-Compliance (3+ Vorfälle) | Formaler Verbesserungsplan oder Vertragskündigungsinitiierung | 60 Tage Verbesserung oder Übergangsplanung | ISB + Geschäftsleitung |

---

# Änderungsmanagement

## Änderungskategorien

| Änderungstyp | Beschreibung | Benachrichtigung erforderlich | Genehmigung erforderlich |
|--------------|-------------|------------------------------|--------------------------|
| **Dienstleistungsänderungen** | Funktionen, APIs, Schnittstellen | Voranküdigung (30 Tage S1, 14 Tage S2) | Wesentliche Änderungen (S1) |
| **Infrastrukturänderungen** | Plattformmigration, Rechenzentrumsverlagerung, Architekturredesign | Vorherige Genehmigung (S1), Voranküdigung (S2) | S1: Ja, S2: Bei Datenstandortänderung |
| **Sicherheitsänderungen** | Sicherheitskontrollen, Verschlüsselungsmethoden, Zugangsmechanismen | Voranküdigung (S1–S2) | Wesentliche Sicherheitsänderungen (S1) |
| **Personaländerungen** | Schlüsselkontakte, Account Manager, Sicherheitspersonal | Zeitnahe Benachrichtigung (innerhalb von 14 Tagen) | Nein |
| **Eigentümerwechsel** | Akquisition, Fusion, Veräusserung, Kontrollwechsel | Sofortige Benachrichtigung (innerhalb von 48 Stunden) | S1: Ja, S2: Benachrichtigung + Risikoüberprüfung |
| **Sub-Lieferantenänderungen** | Neue oder geänderte Sub-Lieferanten mit Datenzugang | Vorherige Genehmigung (S1), Voranküdigung (S2) | S1: Ja, S2: Bei Datenzugang |
| **Vertragliche Änderungen** | Bedingungen, Preise, SLAs, Datenverarbeitungsbedingungen | Gemäss Vertragsänderungsprozess | Gemäss Vertrag (typischerweise ja) |
| **Regulatorische/Compliance-Änderungen** | Verlust der Zertifizierung, regulatorische Sanktionen, Compliance-Versagen | Sofortige Benachrichtigung | Risikobewertung erforderlich |

## Anforderungen an Änderungsbenachrichtigungen

| Lieferantenstufe | Standard-Benachrichtigung | Genehmigung für wesentliche Änderungen |
|-----------------|--------------------------|----------------------------------------|
| **Stufe 1** | 30 Tage Voranküdigung für alle Änderungen | Schriftliche Genehmigung vor Implementierung wesentlicher Änderungen erforderlich |
| **Stufe 2** | 14 Tage Voranküdigung für wesentliche Änderungen | Benachrichtigung ausreichend, [Organisation] kann innerhalb von 7 Tagen Einspruch erheben |
| **Stufe 3** | Zeitnahe Benachrichtigung über signifikante Änderungen (7 Tage) | Standardvertragsbedingungen gelten |
| **Stufe 4** | Standardvertragsbedingungen gelten | Keine spezifische Anforderung |

## Änderungsprüfungsprozess

```
┌─────────────────────────────────────────────────────────────┐
│ LIEFERANTEN-ÄNDERUNGSPRÜFUNGSPROZESS                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Lieferant informiert [Organisation] über geplante       │
│     Änderung                                                │
│     • Änderungsbeschreibung und Geschäftsbegründung         │
│     • Implementierungszeitplan                              │
│     • Folgenabschätzung (Sicht des Lieferanten)             │
│                         ↓                                   │
│  2. Änderung im Lieferanten-Änderungsregister erfassen      │
│     • Änderungsanfrage-ID zuweisen                          │
│     • An geeigneten Prüfer weiterleiten                     │
│       (Sicherheit/IT/Geschäft)                              │
│                         ↓                                   │
│  3. [Organisation] bewertet Änderungsauswirkung             │
│     • Sicherheitsauswirkung (Kontrollen, Risiken,           │
│       Schwachstellen)                                       │
│     • Betriebliche Auswirkung (Diensterbringung,            │
│       Integration)                                          │
│     • Compliance-Auswirkung (regulatorisch, vertraglich)    │
│     • Geschäftsauswirkung (Kosten, Zeitplan, Funktion)      │
│                         ↓                                   │
│  4. Antwortentscheidung festlegen                           │
│     • GENEHMIGEN: Keine Bedenken, wie geplant fortführen    │
│     • GENEHMIGEN MIT AUFLAGEN: Zusätzl. Kontrollen/Tests    │
│     • ÄNDERUNG ANFORDERN: Anpassungen vor Genehmigung nötig │
│     • ABLEHNEN: Unakzeptables Risiko (Alternative           │
│       aushandeln)                                           │
│                         ↓                                   │
│  5. Entscheidung dem Lieferanten mitteilen (innerh. SLA)    │
│     • Entscheidung mit Begründung                           │
│     • Auflagen oder Anforderungen falls anwendbar           │
│     • Aktualisierter Zeitplan falls modifiziert             │
│                         ↓                                   │
│  6. Dokumentation aktualisieren                             │
│     • Risikobewertung (wenn sich Risikoprofil ändert)       │
│     • Lieferantenregister (Änderung erfassen)               │
│     • Vertragsänderungen (falls anwendbar)                  │
│                         ↓                                   │
│  7. Implementierung verifizieren (nach Änderung)            │
│     • Bestätigen, dass Änderung wie genehmigt abgeschlossen │
│     • Keine unerwarteten Auswirkungen validieren            │
│     • Änderungsanfrage schliessen                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Definition wesentlicher Änderungen

Eine Änderung gilt als **wesentlich**, wenn sie eines der folgenden Kriterien erfüllt:

**Sicherheitsbezogen**:

- Betrifft Sicherheitskontrollen zum Schutz der Daten der [Organisation]
- Ändert Verschlüsselungsmethoden, Schlüsselmanagement oder Authentifizierungsmechanismen
- Modifiziert Zugangskontrollarchitektur oder privilegierte Zugriffsverfahren
- Führt neue Angriffsfläche ein oder erweitert bestehende Angriffsvektoren

**Datenbezogen**:

- Ändert Datenverarbeitungsstandort oder Jurisdiktion (insbesondere EU/CH in nicht-angemessenes Land)
- Modifiziert Datenaufbewahrungs-, Backup- oder Disaster-Recovery-Verfahren
- Ändert Datenhandhabungsprozesse oder führt neue Datenflüsse ein
- Betrifft die Ausübung von Betroffenenrechten oder DSGVO/nDSG-Compliance

**Compliance-bezogen**:

- Beeinträchtigt Compliance mit regulatorischen Anforderungen (DORA, NIS2, DSGVO)
- Führt neue Sub-Lieferanten mit Zugang zu Daten der [Organisation] ein
- Ändert Zertifizierungsumfang oder führt zu Zertifizierungsablauf
- Betrifft vertragliche Sicherheitsverpflichtungen

**Dienstleistungsbezogen**:

- Ändert wesentlich Dienstarchitektur oder Technologie-Stack
- Ändert Dienstverfügbarkeit, Leistung oder Kapazität
- Modifiziert SLA-Verpflichtungen oder führt neue Abhängigkeiten ein
- Betrifft Business-Continuity- oder Disaster-Recovery-Fähigkeiten

**Unternehmensbezogen**:

- Ändert Eigentümerschaft oder Kontrolle der Lieferanteneinheit
- Löst Change-of-Control-Klauseln im Vertrag aus
- Beeinträchtigt Fähigkeit des Lieferanten zur Erfüllung vertraglicher Verpflichtungen

---

# Beziehungsgovernance

## Governance-Struktur nach Lieferantenstufe

| Lieferantenstufe | Governance-Modell | Meetinghäufigkeit | Teilnehmer |
|-----------------|------------------|-------------------|-----------|
| **Stufe 1 (Kritisch)** | Formales Governance-Komitee mit dokumentierter Satzung | Vierteljährlich | [Organisation]: Geschäftsverantwortlicher, ISO, IT; Lieferant: Account Manager, Technischer Leiter, Sicherheit |
| **Stufe 2 (Hoch)** | Regelmässige Geschäftsüberprüfungen mit Sicherheitskomponente | Halbjährlich | [Organisation]: Geschäftsverantwortlicher, ISO; Lieferant: Account Manager |
| **Stufe 3 (Mittel)** | Periodische Check-ins nach Bedarf | Jährlich | [Organisation]: Geschäftsverantwortlicher; Lieferant: Account Manager |
| **Stufe 4 (Niedrig)** | Transaktionsbeziehung | Bei Bedarf | Je nach Transaktion |

## Agenda des vierteljährlichen Governance-Meetings (Stufe 1)

| Tagesordnungspunkt | Geleitet von | Zeitzuteilung |
|---------------------|-------------|---------------|
| **Leistungsüberprüfung** | Geschäftsverantwortlicher | 15 Minuten |
| **SLA-Compliance & Servicequalität** | IT-Betrieb | 15 Minuten |
| **Sicherheitslage-Update** | ISO | 20 Minuten |
| **Vorfallsüberprüfung** (falls vorhanden) | ISO / Geschäftsverantwortlicher | 10 Minuten |
| **Änderungsanfragen & Roadmap** | Lieferant | 15 Minuten |
| **Compliance-Status** (Zertifizierungen, Audits) | ISO | 10 Minuten |
| **Probleme, Risiken und Eskalationen** | Geschäftsverantwortlicher | 15 Minuten |
| **Überprüfung von Massnahmen** | Alle | 10 Minuten |

**Meeting-Dokumentation**: Protokolle sollen Entscheidungen, Massnahmen mit Verantwortlichen und Fälligkeitsterminen sowie Eskalationen dokumentieren.

## Eskalationsverfahren

| Problemtyp | Eskalationsstufe 1 | Eskalationsstufe 2 | Eskalationsstufe 3 |
|------------|-------------------|--------------------|-------------------|
| **Dienstdegradation** | Geschäftsverantwortlicher | IT-Management | ITL |
| **Sicherheitsbedenken** | ISO | ISB | Geschäftsleitung |
| **Compliance-Verstoss** | ISO | ISB + Recht | Geschäftsleitung |
| **Vertragsstreit** | Einkauf | Recht | Geschäftsleitung |
| **Beziehungsabbruch** | Geschäftsverantwortlicher | ITL/ISB | Geschäftsleitung |
| **Finanzproblem** (Abrechnungsstreitigkeiten) | Geschäftsverantwortlicher | Finanzen | FL |

**Eskalationsdokumentation**: Alle Eskalationen sollen mit Problembeschreibung, eingeschlagenem Eskalationspfad, Lösung und Zeitrahmen dokumentiert werden.

---

# Vorfallsüberprüfung

## Lieferantenvorfallskategorien

| Kategorie | Beispiele | Schweregradindikatoren |
|-----------|---------|----------------------|
| **Sicherheitsvorfälle** | Datenpanne, unbefugter Zugang, Malware-Infektion, Anmeldedatenkompromittierung | Datenexposition, Systemkompromittierung, regulatorische Meldepflicht |
| **Dienstvorfälle** | Ungeplanter Ausfall, wesentliche Degradation, Datenverlust, -verfälschung | Dauer, Benutzerauswirkung, SLA-Verletzungsschwere |
| **Compliance-Vorfälle** | Zertifizierungsverlust, regulatorischer Verstoss, Auditversagen | Regulatorische Auswirkung, Vertragsbruch, Reputationsrisiko |
| **Lieferkettenvorfälle** | Sub-Lieferantenpanne, Software-Schwachstelle (Log4Shell-ähnlich), Abhängigkeitskompromittierung | Kaskadenauswirkung, weitreichende Exposition, Behebungskomplexität |
| **Beinahe-Unfälle** | Verhinderte potenzielle Vorfälle, knappe Ereignisse | Lernmöglichkeit, Kontrollvalidierung |

## Vorfallsüberprüfungsprozess

| Schritt | Aktivität | Zeitrahmen | Verantwortlich |
|---------|----------|-----------|---------------|
| **1. Benachrichtigung** | Störungsmeldung vom Lieferanten gemäss Vertragsbedingungen entgegennehmen | Gemäss SLA (4–48 Stunden) | Lieferant → ISO |
| **2. Protokollierung** | Vorfall im Lieferantenvorfallsregister mit anfänglicher Bewertung erfassen | Innerhalb von 4 Stunden | ISO |
| **3. Folgenabschätzung** | Auswirkung auf [Organisation] bewerten (Daten, Systeme, Compliance, Geschäft) | Innerhalb von 24 Stunden | ISO + Geschäftsverantwortlicher |
| **4. Eindämmungsverifizierung** | Verifizieren, dass Lieferant Vorfall eingedämmt hat, Restrisiko bewerten | Innerhalb von 48 Stunden | ISO |
| **5. Ursachenanalyse** | Ursachenanalyse des Lieferanten anfordern und prüfen | Innerhalb von 30 Tagen | Lieferant erstellt, ISO prüft |
| **6. Behebungsüberprüfung** | Behebungsmassnahmen und Präventivmassnahmen des Lieferanten prüfen | Innerhalb von 60 Tagen | ISO |
| **7. Risikonneubewertung** | Lieferantenrisikobewertung aktualisieren, wenn Vorfall auf Kontrollschwäche hinweist | Innerhalb von 30 Tagen nach Abschluss | ISO |
| **8. Lessons Learned** | Lessons Learned dokumentieren, Richtlinien/Verfahren bei Bedarf aktualisieren | Innerhalb von 90 Tagen | ISO + IT |
| **9. Vertragsprüfung** | Vertrags-Compliance bewerten (Benachrichtigungs-Pünktlichkeit, Kooperationsverpflichtungen) | Nach Vorfall | Recht + ISO |

## Post-Incident-Anforderungen nach Lieferantenstufe

| Lieferantenstufe | Erforderliche Post-Incident-Dokumentation |
|-----------------|------------------------------------------|
| **Stufe 1** | Vollständige Ursachenanalyse, detaillierte Chronologie, vollständiger Abhilfeplan, Verifizierungsnachweise, Lessons-Learned-Dokument, Drittanbieter-Forensik (bei Panne) |
| **Stufe 2** | Zusammenfassung der Ursachenanalyse, Behebungsbestätigung, übergeordnete Chronologie, wichtige Befunde und Korrekturmassnahmen |
| **Stufe 3** | Vorfallszusammenfassung, Behebungsbestätigung, grundlegende Korrekturmassnahmen |
| **Stufe 4** | Störungsmeldung und Abschlussbestätigung |

**Vorfallsinduzierte Überprüfungen**: Sicherheitsvorfälle sollen auslösen:

- Sofortige Sicherheitsneubewertung bei kritischem oder hohem Schweregrad
- Vertrags-Compliance-Überprüfung (Benachrichtigungsfristen, Kooperationspflichten)
- Potenzielle Neueinstufung des Lieferantenrisikos
- Erwägung von Kündigungsrechten bei wesentlichem Vertragsbruch

---

# Dokumentation & Berichterstattung

## Erforderliche Dokumentation

| Dokumenttyp | Aktualisierungsauslöser | Aufbewahrungsdauer | Speicherort |
|-------------|------------------------|-------------------|------------|
| **Lieferantenregister** | Bei jeder Änderung | Aktuell + 3 Jahre | Lieferantenmanagementsystem |
| **Bewertungsberichte** | Pro geplanter/ausgelöster Bewertung | 5 Jahre | Dokumentenmanagementsystem |
| **Meeting-Protokolle** | Pro Governance-Meeting | 3 Jahre | Lieferantenordner |
| **Vorfallsaufzeichnungen** | Bei Vorfallseintreten | 5 Jahre | Incident-Management-System |
| **Änderungsaufzeichnungen** | Bei Änderungsanfrage | 3 Jahre | Änderungsmanagementsystem |
| **SLA-Berichte** | Pro Berichtszeitraum (monatlich/vierteljährlich) | 3 Jahre | Leistungsüberwachungssystem |
| **Compliance-Zertifikate** | Bei Erhalt/Erneuerung | Aktuell + 2 Jahre | Compliance-Repository |
| **Auditbefunde** | Bei Bewertung | Bis Abschluss + 3 Jahre | Lieferantenmanagementsystem |

## Management-Berichterstattung

| Bericht | Häufigkeit | Zielgruppe | Inhalt |
|---------|-----------|-----------|--------|
| **Lieferantenrisiko-Übersicht** | Vierteljährlich | ISB, ITL, Management | Gesamte Lieferantenrisikolandschaft, Hochrisikolieferanten, Trends |
| **Kritischer Lieferantenstatus** | Monatlich | ISO, Geschäftsverantwortliche | Stufe-1-Lieferantenleistung, Probleme, Änderungen |
| **Vorfallsübersicht** | Vierteljährlich | ISB, Compliance | Lieferantensicherheitsvorfälle, Auswirkung, Behebungsstatus |
| **Compliance-Status** | Vierteljährlich | ISO, Compliance | Zertifizierungsgültigkeit, Compliance-Befunde, Lücken |
| **Leistungs-Dashboard** | Kontinuierlich | Geschäftsverantwortliche, IT | SLA-Compliance, Servicequalität, Verfügbarkeit |
| **Jährliche Lieferantenüberprüfung** | Jährlich | Geschäftsleitung | Umfassende Lieferantenportfolio-Überprüfung, strategische Empfehlungen |

## Regulatorische Berichterstattung (wo anwendbar)

**DORA-abgedeckte Dienste**:

- IKT-Drittanbieter-Risikoregister mit vierteljährlichen Updates führen
- Wesentliche Änderungen an IKT-Drittanbieter-Vereinbarungen der zuständigen Behörde melden
- Konzentrationsrisikobewertungen jährlich dokumentieren

**NIS2-abgedeckte Dienste**:

- Lieferantenvorfälle in regulatorische Störungsmeldungen einbeziehen (24-Stunden-Frühwarnung)
- Lieferkettensicherheitsmassnahmen im jährlichen Cybersicherheitsbericht dokumentieren
- Nachweise für Lieferantensicherheitsanforderungen und Verifizierung aufbewahren

---

# Referenzen

| Dokument | Beziehung |
|----------|----------|
| **ISMS-POL-A.5.19-23** | Übergeordnetes Richtlinienrahmenwerk |
| **ISMS-POL-A.5.19-23-S1** | Lieferantenklassifizierung bestimmt Überwachungshäufigkeit |
| **ISMS-POL-A.5.19-23-S2** | Vertragsbedingungen werden auf Compliance überwacht |
| **ISMS-POL-A.5.19-23-S3** | Sub-Lieferantenüberwachungsanforderungen |
| **ISMS-IMP-A.5.19-23.S4-UG/TG** | Operative Governance-Bewertungsarbeitsmappe |
| **ISO/IEC 27036-4:2016** | Informationssicherheit in Lieferantenbeziehungen – Cloud-Dienste |

---

**Nächstes Dokument:** ISMS-POL-A.5.19-23-S5 — Cloud-Dienste-Sicherheit (Massnahme A.5.23)

---

*„Überwachung ohne Aktion ist teures Zuschauen. Aktion ohne Überwachung ist blinder Glaube."*
<!-- QA_VERIFIED: 2026-03-28 -->
