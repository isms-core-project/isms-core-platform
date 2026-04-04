<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.8-DE:framework:POL:a.5.8 -->
**ISMS-POL-A.5.8 — Informationssicherheit im Projektmanagement**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationssicherheit im Projektmanagement |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.8 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum festzulegen] |
| **Version** | 1.0 |
| **Versionsdatum** | [Datum festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum festzulegen] | ISB | Erstversion des Richtlinienrahmens |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Datum festzulegen]

---

# Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an die Integration von Informationssicherheit in das Projektmanagement fest, um sicherzustellen, dass Sicherheitsrisiken gemäss ISO/IEC 27001:2022 Kontrolle A.5.8 systematisch über den gesamten Projektlebenszyklus hinweg adressiert werden.

**Zweck**: Definition der organisatorischen Anforderungen an die Integration von Informationssicherheit in Projektmanagementprozesse. Diese Richtlinie legt fest, WELCHE Sicherheitsaktivitäten in jeder Projektphase erforderlich sind und WER für die Sicherheitsergebnisse rechenschaftspflichtig ist.

**Geltungsbereich**: Diese Richtlinie gilt für alle von [Organisation] durchgeführten Projekte, unabhängig von Projekttyp, Methodik, Komplexität, Grösse, Dauer oder organisatorischem Umfang, einschliesslich Projekten, die von internen Teams, externen Lieferanten oder hybriden Strukturen verwaltet werden.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert obligatorische Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich Schweizerisches nDSG (Art. 8), EU GDPR (Art. 25) und ISO/IEC 27001:2022. Bedingte sektorspezifische Anforderungen (NIS2, DORA, FINMA) gelten, sofern die Geschäftstätigkeiten von [Organisation] die Anwendbarkeit auslösen.

---

# Geltungsbereich und Anwendbarkeit

## ISO/IEC 27001:2022 Kontrolle A.5.8

> *Informationssicherheit sollte in das Projektmanagement integriert werden.*

**Kontrollziel**: Sicherstellen, dass mit Projekten und Projektlieferergebnissen verbundene Informationssicherheitsrisiken über den gesamten Projektlebenszyklus hinweg systematisch identifiziert, bewertet und behandelt werden.

## Im Geltungsbereich

Diese Richtlinie gilt für:

- **IT-Projekte**: Softwareentwicklung, Systemimplementierung, Infrastruktur-Deployment
- **Geschäftsprojekte**: Prozessumgestaltung, Organisationsänderungen, Fusionen/Akquisitionen
- **Infrastrukturprojekte**: Rechenzentrumsbau, Gebäudemodifikationen, Geräteinstallation
- **Compliance-Projekte**: Regulatorische Umsetzung, Audit-Behebung, Zertifizierungsprogramme
- Projekte aller Grössen und Laufzeiten
- Projekte unabhängig von der Managementmethodik (Agile, Wasserfall, hybrid)
- Projekte, die von internen Teams, externen Lieferanten oder gemischten Teams verwaltet werden
- Alle Projektphasen: Initiierung, Planung, Ausführung, Überwachung/Steuerung, Abschluss

## Nicht im Geltungsbereich

- Routinemässige operative Aktivitäten, die kein Projekt darstellen (laufende Wartung)
- Notfall-Incident-Response-Aktivitäten (geregelt durch A.5.24-27 Incident-Management)
- Geringfügige Änderungen, die über den Change-Control-Prozess verwaltet werden (geregelt durch A.8.32 Änderungsmanagement)

## Regulatorische Anforderungen

**Stufe 1 — Obligatorische Compliance**:

- Schweizerisches nDSG (Art. 8): Angemessene technische und organisatorische Massnahmen
- EU GDPR (Art. 25, 32): Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen
- ISO/IEC 27001:2022: Kontrolle A.5.8 Informationssicherheit im Projektmanagement

**Stufe 2 — Bedingte Anwendbarkeit** (gemäss ISMS-POL-00):

- NIS2, DORA, FINMA Rundschreiben 2008/21, PCI DSS v4.0.1 — gelten, wenn Geschäftsbedingungen die Anwendbarkeit auslösen

---

# Richtlinienaussagen

## Grundsätze der Sicherheitsintegration im Projekt

[Organisation] MUSS Informationssicherheit in alle Projekte nach folgenden Grundsätzen integrieren:

| Grundsatz | Anforderung | Anwendungsbeispiel |
|-----------|-------------|-------------------|
| **Frühzeitige Integration** | Sicherheit MUSS ab der Projektinitiierung berücksichtigt werden, nicht nachträglich ergänzt | Projektcharta enthält Sicherheitsklassifizierung; Sicherheitsressourcen im Projektbudget vor der Planungsphase zugewiesen |
| **Verhältnismässigkeit** | Sicherheitsaufwand MUSS proportional zur Projektrisikoeinstufung sein | Internes Niedrigrisiko-Tool erhält Checklisten-Validierung (2 Stunden); Hochrisiko-Kundenportal erhält Penetrationstests (40 Stunden) |
| **Lebenszyklusabdeckung** | Sicherheitsaktivitäten MÜSSEN in allen Projektphasen stattfinden | Sicherheitsüberprüfung an jedem Phasentor; Sicherheitsanforderungen in Planung, Tests in Ausführung, Übergabe bei Abschluss |
| **Risikobasierung** | Sicherheitsentscheidungen MÜSSEN auf der Risikobewertung basieren | Sicherheitskontrollen auf Basis von Threat-Modeling und Datenklassifizierung ausgewählt, nicht generischen Checklisten |
| **Nachvollziehbare Anforderungen** | Sicherheitsanforderungen MÜSSEN dokumentiert und bis zur Implementierung nachverfolgt werden | Sicherheitsanforderungsregister verknüpft jede Anforderung mit Designelement, Testfall und Deployment-Nachweis |
| **Lessons Learned** | Projektsicherheitserfahrungen MÜSSEN in die kontinuierliche Verbesserung einfliessen | Post-Projekt-Sicherheitsüberprüfung identifiziert Kontrollücken; Erkenntnisse aktualisieren Vorlagen für Sicherheitsanforderungen |

## Anforderung zur Projektklassifizierung

Alle Projekte MÜSSEN auf Basis der Informationssicherheitsauswirkung klassifiziert werden, um proportionale Sicherheitsanforderungen zu bestimmen.

**Klassifizierungsfaktoren und Entscheidungsmatrix**:

Projekte MÜSSEN auf Basis des höchsten anwendbaren Faktors klassifiziert werden:

| Faktor | Hohes Risiko | Mittleres Risiko | Niedriges Risiko |
|--------|-------------|-----------------|-----------------|
| **Datensensitivität** | Kritische/Vertrauliche Daten (PII, Zahlungsdaten, IP, vertrauliche Geschäftsinformationen gemäss A.5.12) | Interne Daten (nicht-öffentliche Geschäftsdaten, Mitarbeiterdaten) | Öffentliche Daten (Marketinginhalte, veröffentlichte Dokumentation) |
| **Systemkritikalität** | RTO < 4 Stunden, umsatzgenerierendes System, kundenseitiger Dienst | RTO 4-24 Stunden, geschäftswichtig, aber nicht umsatzkritisch | RTO > 24 Stunden, operatives Unterstützungssystem |
| **Regulatorischer Umfang** | GDPR/PCI DSS v4.0.1/FINMA direkt anwendbar | Schweizerisches nDSG anwendbar | Keine regulierte Datenverarbeitung |
| **Externe Exposition** | Internetbasiert oder für externe Parteien zugänglich (Kunden, Partner, Öffentlichkeit) | Kontrollierter externer Zugang (VPN, dedizierte Verbindung) | Nur interner Zugang |
| **Technische Komplexität** | Neues Architekturmuster, neuartige Integrationen, benutzerdefinierte Sicherheitskontrollen | Standardarchitektur mit moderater Anpassung | Standard-Deployment, bewährte Architektur |
| **Drittpartei-Beteiligung** | Kritische Funktion ausgelagert (Hosting, Authentifizierung, Zahlungsabwicklung) | Lieferantenverwaltete Komponenten (SaaS-Integration, Managed Services) | Vollständig interne Entwicklung und Hosting |

**Klassifizierungslogik**: Wenn **ein beliebiger Faktor** die Hochrisiko-Kriterien erfüllt → als **Hohes Risiko** einstufen. Wenn **ein beliebiger Faktor** die Mittelrisiko-Kriterien erfüllt (und kein Hochrisikofaktor vorliegt) → als **Mittleres Risiko** einstufen. Wenn **alle Faktoren** die Niedrigrisiko-Kriterien erfüllen → als **Niedriges Risiko** einstufen.

**Klassifizierungsdokumentation**: Klassifizierungsentscheidung und Begründung MÜSSEN in der Projektcharta dokumentiert und gemäss nachstehender Genehmigungsbefugnis genehmigt werden.

**Klassifizierungsstufen**:

| Klassifizierung | Beschreibung | Genehmigungsbefugnis |
|-----------------|-------------|---------------------|
| **Hohes Risiko** | Kritische Informationssicherheitsauswirkung | ISB-Genehmigung erforderlich |
| **Mittleres Risiko** | Moderate Informationssicherheitsauswirkung | Genehmigung des Informationssicherheitsbeauftragten |
| **Niedriges Risiko** | Minimale Informationssicherheitsauswirkung | Projektmanager klassifiziert selbst mit InfoSec-Überprüfung |

Die Klassifizierung MUSS an jedem Phasentor überprüft und aktualisiert werden, wenn sich Umfang, Datensensitivität oder externe Exposition wesentlich ändert.

## Sicherheitsanforderungen an Phasengates

[Organisation] MUSS Sicherheitsüberprüfungen in die Projekt-Governance an folgenden Phasengates integrieren:

| Phasegate | Erforderliche Sicherheitskriterien |
|-----------|----------------------------------|
| **Projektgenehmigung** | Sicherheitsklassifizierung festgelegt; Anfängliche Sicherheitsrisiken identifiziert; Sicherheitsbudget zugewiesen |
| **Planungsgenehmigung** | Sicherheitsanforderungen dokumentiert und genehmigt; Sicherheitsressourcen bestätigt |
| **Ausführungsprüfpunkt** | Sicherheitstests durchgeführt; Kritische Befunde behoben |
| **Deployment-Genehmigung** | Alle Kritischen/Hohen Befunde behoben oder akzeptiert; Sicherheitsübergabedokumentation vollständig |
| **Projektabschluss** | Restrisiken formal akzeptiert; Lessons Learned dokumentiert; Vermögenswerte registriert |

Projekte DÜRFEN NICHT in die nächste Phase übergehen, bis die Sicherheitskriterien der aktuellen Phase erfüllt oder von der zuständigen Behörde formal akzeptiert wurden.

## Identifizierung von Sicherheitsanforderungen

Sicherheitsanforderungen für Projektlieferergebnisse MÜSSEN systematisch nach folgendem Prozess identifiziert werden:

**Prozess zur Anforderungsidentifizierung**:

1. **Anwendbarkeitsbewertung**: Projektmanager prüft mit Unterstützung des InfoSec-Beauftragten jede Sicherheitsanforderungskategorie gegen den Projektumfang:
   - Anwendungssicherheit (A.8.25-28): Anwendbar, wenn das Projekt Softwareentwicklung oder benutzerdefiniertem Code umfasst
   - Datenschutz (A.8.24, GDPR/nDSG): Anwendbar auf Basis der Datenklassifizierung gemäss A.5.12
   - Zugriffskontrolle (A.5.15-18): Anwendbar für alle Projekte (Minimum: Einhaltung der Zugriffskontrollrichtlinie)
   - Infrastruktursicherheit (A.8.20-22): Anwendbar, wenn das Projekt die Netzwerkarchitektur beeinflusst oder Infrastruktur deployt
   - Drittparteiensicherheit (A.5.19-22): Anwendbar, wenn das Projekt externe Lieferanten oder Cloud-Dienste einbezieht
   - Regulatorische Anforderungen (ISMS-POL-00): Anwendbar auf Basis der Stufe-1/2-Analyse

2. **Anforderungsumfang**: Für anwendbare Kategorien werden spezifische Anforderungen ausgewählt basierend auf:
   - Datenklassifizierung (Kritisch/Vertraulich/Intern/Öffentlich gemäss A.5.12)
   - Systemkritikalität (RTO/RPO-Anforderungen gemäss A.5.29-30)
   - Bedrohungsprofil (gemäss A.5.7 Bedrohungsintelligenz und projektspezifischem Threat-Modeling)
   - Regulatorische Verpflichtungen (gemäss ISMS-POL-00 Stufe-1/2-Pflichtanforderungen)

3. **Dokumentation**: Anwendbare Anforderungen MÜSSEN dokumentiert werden in:
   - **Mittel-/Hochrisiko-Projekte**: Sicherheitsanforderungsregister (formales Tracking-Tool)
   - **Niedrigrisiko-Projekte**: Projektrisikoregister (Sicherheitsanforderungen als Risikobehandlungsmassnahmen)

4. **Genehmigung**: Anforderungen MÜSSEN überprüft und genehmigt werden durch:
   - **Hochrisiko-Projekte**: ISB-Genehmigung vor der Projektausführungsphase
   - **Mittelrisiko-Projekte**: InfoSec-Beauftragter-Genehmigung vor der Projektausführungsphase
   - **Niedrigrisiko-Projekte**: InfoSec-Beauftragter bestätigt Vollständigkeit der Anforderungen

**Detaillierte Anforderungsidentifizierungsverfahren, kategoriespezifische Checklisten und Vorlage für das Sicherheitsanforderungsregister sind in ISMS-IMP-A.5.8 bereitgestellt.**

## Anforderung an Sicherheitstests

Alle Projekte MÜSSEN Sicherheitstests umfassen, die proportional zur Projektklassifizierung sind, wobei der Testumfang wie folgt bestimmt wird:

**Sicherheitstestanforderungen nach Klassifizierung**:

- **Hochrisiko-Projekte**:
  - **Obligatorisch**: Externer Penetrationstest (OWASP-Methodik oder gleichwertig), automatisiertes Schwachstellenscanning (wöchentlich während der Entwicklung + finaler Pre-Deployment-Scan), Sicherheitscode-Review für benutzerdefinierten Code (Mindestabdeckung 20 % der Authentifizierungs-, Autorisierungs-, Datenschutz- und kryptografischen Funktionen)
  - **Testkriterien**: Penetrationstests MÜSSEN von einer unabhängigen Drittpartei (nicht das Projektteam) durchgeführt werden. Alle Kritischen Befunde und ≥80 % der Hohen Befunde MÜSSEN vor dem Deployment behoben werden.

- **Mittelrisiko-Projekte**:
  - **Obligatorisch**: Automatisiertes Schwachstellenscanning (finaler Pre-Deployment-Scan), funktionelle Sicherheitstests für Authentifizierung, Autorisierung, Datenvalidierung und Fehlerbehandlung
  - **Bedingt**: Penetrationstest erforderlich, wenn das Projekt internetbasiert ODER regulierte Daten (GDPR/PCI DSS v4.0.1) verarbeitet
  - **Testkriterien**: Alle Kritischen Befunde und ≥70 % der Hohen Befunde MÜSSEN vor dem Deployment behoben werden.

- **Niedrigrisiko-Projekte**:
  - **Obligatorisch**: Sicherheitsvalidierung gegen Sicherheitsanforderungs-Checkliste (Minimum: Zugriffskontrollverifizierung gemäss A.5.15-18, Verschlüsselungsverifizierung gemäss A.8.24, sofern anwendbar)
  - **Optional**: Automatisiertes Schwachstellenscanning (empfohlen, aber nicht obligatorisch)
  - **Testkriterien**: Kritische Befunde MÜSSEN vor dem Deployment behoben werden.

**Dokumentation der Testausreichlichkeit**: Für Mittel-/Hochrisiko-Projekte MUSS die Testadäquanz im Sicherheitsbewertungsbericht dokumentiert und vom InfoSec-Beauftragten (Mittel) oder ISB (Hoch) vor der Deployment-Autorisierung genehmigt werden. Wird das Behebungsziel nicht erreicht, MUSS das Restrisiko formal gemäss Abschnitt Ausnahmenmanagement akzeptiert werden.

**Testnachweise (Scan-Berichte, Penetrationstest-Berichte, Code-Review-Befunde) MÜSSEN gemäss A.5.33 archiviert und in der Sicherheitsübergabedokumentation bereitgestellt werden.**

## Anforderung an die Sicherheitsübergabe

Beim Projektabschluss MUSS eine Sicherheitsübergabedokumentation an den Betrieb übergeben und als vollständig validiert werden, bevor die Projektabschluss-Autorisierung erteilt wird.

**Vollständigkeitskriterien der Sicherheitsübergabe**:

Die Sicherheitsübergabe MUSS folgende Dokumentation umfassen, die dem operativen Eigentümer übergeben und über eine Übergabe-Checkliste als vollständig bestätigt wird:

1. **Sicherheitsarchitektur-Dokumentation**:
   - Sicherheitsdesign des Systems (Vertrauensgrenzen, Authentifizierungs-/Autorisierungsmodell, Verschlüsselungsimplementierung)
   - Datenflussdiagramme mit Datenklassifizierung und Schutzkontrollen
   - Netzwerkarchitektur (Firewall-Regeln, Netzwerksegmentierung, externe Zugangspunkte)
   - Integrationssicherheit (API-Authentifizierung, Drittanbieter-Dienstabhängigkeiten)

2. **Operative Sicherheitsverfahren**:
   - Überwachungsanforderungen (Sicherheitsprotokollquellen, Alarmschwellenwerte, SIEM-Integration)
   - Protokollaufbewahrungsanforderungen (gemäss A.8.15, regulatorische Aufbewahrungsfristen)
   - Sicherungs- und Wiederherstellungsverfahren (gemäss A.8.13, einschliesslich sicherheitsspezifischer Wiederherstellungstests)
   - Incident-Response-Eskalation (Sicherheitsvorfalltypen, Eskalationspfade, Kontaktinformationen)
   - Sicherheits-Patch-Management (Aktualisierungshäufigkeit, Testanforderungen, Rollback-Verfahren)

3. **Akzeptierte Restrisiken**:
   - Formale Risikoakzeptanzunterlagen mit Genehmigungsunterschriften (gemäss Risikoeinstufungs-Befugnis)
   - Kompensierende Kontrollen (sofern zutreffend)
   - Zeitplan für die Neubewertung des Risikos (bei zeitlich begrenzten Akzeptanzen)

4. **Sicherheitstestnachweise**:
   - Abschliessender Schwachstellenscan-Bericht (datiert innerhalb von 7 Tagen des Deployments)
   - Penetrationstest-Bericht (sofern gemäss Sicherheitstestanforderung anwendbar)
   - Behebungsnachweise für Kritische/Hohe Befunde (oder Risikoakzeptanz für ungelöste Befunde)

**Übergabe-Validierungsprozess**: Der Betrieb MUSS die Vollständigkeit der Übergabe über eine unterzeichnete Sicherheitsübergabe-Checkliste (Vorlage in ISMS-IMP-A.5.8) bestätigen, bevor der Projektmanager die Projektabschluss-Autorisierung beantragt. Unvollständige Übergabedokumentation blockiert den Projektabschluss, bis Lücken behoben oder explizit vom operativen Eigentümer und ISB (für Hochrisiko-Projekte) akzeptiert werden.

**Übergabedokumentation wird gemäss A.5.33 Anforderungen an das Dokumentenmanagement archiviert und als operative Basisdokumentation für den Systemlebenszyklus gepflegt.**

---

# Rollen und Verantwortlichkeiten

## Geschäftsleitung

**Verantwortlichkeit**: Gesamte organisatorische Sicherheit, einschliesslich Integration der Projektsicherheit.

**Aufgaben**:

- Genehmigung dieser Richtlinie und Sicherstellung organisatorischer Ressourcen für die Implementierung
- Überprüfung des Sicherheitsstatus von Hochrisiko-Projekten in Management-Reviews
- Akzeptanz von Restrisiken für kritische Projekte

## Informationssicherheitsbeauftragter (ISB)

**Verantwortlichkeit**: Implementierung des Informationssicherheitsprogramms, einschliesslich Projektsicherheitsaufsicht.

**Aufgaben**:

- Genehmigung und Pflege dieser Richtlinie
- Genehmigung von Hochrisiko-Projektklassifizierungen
- Akzeptanz von Sicherheitsrestrisiken für Hochrisiko-Projekte
- Bereitstellung von Sicherheitsressourcen zur Projektunterstützung
- Überwachung von Projektsicherheitsmetriken und Berichterstattung an die Geschäftsleitung
- Genehmigung von Ausnahmen von Sicherheitsanforderungen

**Befugnis**: Projekte mit inakzeptablen Sicherheitsrisiken stoppen oder verzögern; zusätzliche Sicherheitskontrollen vorschreiben.

## Informationssicherheitsbeauftragter / Sicherheitsteam

**Verantwortlichkeit**: Operative Sicherheitsleitlinien und Unterstützung bei der Risikobewertung.

**Aufgaben**:

- Unterstützung von Projektteams bei der Sicherheitsrisikobewertung und Anforderungsidentifizierung
- Überprüfung und Genehmigung von Mittelrisiko-Projektklassifizierungen
- Überprüfung von Sicherheitsanforderungen und Bereitstellung technischer Leitlinien
- Durchführung oder Beauftragung von Sicherheitstests
- Pflege von Vorlagen und Checklisten für Sicherheitsanforderungen

**Befugnis**: Sicherheitsbedenken an den ISB eskalieren; Projektverzögerungen bei ungeminderten Risiken empfehlen.

## Projektmanager

**Verantwortlichkeit**: Gesamter Projekterfolg, einschliesslich Implementierung von Sicherheitsanforderungen.

**Aufgaben**:

- Klassifizierung des Projektsicherheitsrisikos (mit Unterstützung des InfoSec-Beauftragten)
- Sicherstellen, dass Sicherheitsaktivitäten geplant und budgetiert sind
- Durchführung von Sicherheitsaktivitäten in jeder Projektphase
- Pflege des Projektsicherheitsrisikoregisters
- Eskalation von Sicherheitsrisiken und -problemen
- Dokumentation von Sicherheitsaspekten bei Projektabschluss und -übergabe

**Befugnis**: Projektressourcen für Sicherheitsaktivitäten zuweisen; Sicherheitsunterstützung vom InfoSec-Team anfordern.

## Geschäfts-/Produktverantwortlicher

**Verantwortlichkeit**: Geschäftsanforderungen, einschliesslich Sicherheitsanforderungen der Projektlieferergebnisse.

**Aufgaben**:

- Definition von geschäftlichen Sicherheitsanforderungen
- Teilnahme an der Sicherheitsrisikobewertung
- Genehmigung von Sicherheitsanforderungen als Teil des Projektumfangs
- Akzeptanz von Sicherheitsrestrisiken für eigene Systeme/Dienste

## Technischer Leiter / Lösungsarchitekt

**Verantwortlichkeit**: Technisches Design und Implementierung, einschliesslich Sicherheitsarchitektur.

**Aufgaben**:

- Einbindung von Sicherheitskontrollen in die Lösungsarchitektur
- Implementierung von Sicherheitsanforderungen gemäss Spezifikationen
- Unterstützung von Threat-Modeling und Sicherheitsarchitektur-Reviews
- Behebung von Sicherheitsbefunden aus Tests oder Reviews

## Drittanbieter / Auftragnehmer

**Verantwortlichkeit**: Sicherheit der vom Lieferanten gelieferten Komponenten und Dienste gemäss Vertrag.

**Aufgaben**:

- Einhaltung der Sicherheitsanforderungen von [Organisation] in Verträgen
- Teilnahme an Sicherheitsbewertungen und Bereitstellung erforderlicher Nachweise
- Meldung von Sicherheitsvorfällen oder Schwachstellen an [Organisation]

## RACI-Matrix für Projektsicherheitsaktivitäten

| Aktivität | PM | InfoSec | ISB | Geschäftsverantwortl. | Tech. Leiter |
|-----------|----|---------| -----|----------------------|-------------|
| Projektklassifizierung | V | A | I | B | B |
| Identifizierung von Sicherheitsanforderungen | V | A | I | B | B |
| Sicherheitsarchitektur-Design | B | B | I | I | V/A |
| Durchführung von Sicherheitstests | V | B | I | I | V |
| Akzeptanz von Restrisiken | I | B | A (Hoch) | A (Mittel/Nied.) | I |
| Überprüfung der Sicherheitsübergabe | V | A | I | B | B |

V = Verantwortlich (führt die Arbeit durch), A = Accountable (Letztentscheid), B = Beratend (liefert Input), I = Informiert (wird auf dem Laufenden gehalten)

---

# Governance und Ausnahmenmanagement

## Sicherheitsüberprüfungsbefugnis

| Projektklassifizierung | Überprüfungsbefugnis |
|------------------------|---------------------|
| Niedriges Risiko | Selbstbewertung durch Projektmanager |
| Mittleres Risiko | Überprüfung durch Informationssicherheitsbeauftragten erforderlich |
| Hohes Risiko | ISB-Genehmigung erforderlich |

## Eskalation

Sicherheitsbedenken MÜSSEN eskaliert werden innerhalb von:

- 2 Werktagen für Hochrisiko-Projekte
- 5 Werktagen für Mittelrisiko-Projekte

**Eskalationspfad**: Projektmanager → Informationssicherheitsbeauftragter → ISB → Geschäftsleitung

**Eskalationsauslöser**:

Sicherheitsbedenken, die eine Eskalation erfordern, umfassen:

- **Obligatorische Eskalation**:
  - Kritische Sicherheitsbefunde, die nicht vor dem Deployment-Stichtag behoben werden können
  - Sicherheitsanforderungen, die mit Geschäftszielen in Konflikt stehen (Risikoakzeptanz erforderlich)
  - Drittanbieter-Lieferant kann Sicherheitsanforderungen nicht erfüllen
  - Datenschutzverletzung oder Sicherheitsvorfall, der Projektlieferergebnisse betrifft
  - Regulatorische Compliance-Bedenken, die während der Projektausführung identifiziert werden

- **Ermessensabhängige Eskalation**:
  - Sicherheitsarchitektur-Entscheidungen mit erheblichen langfristigen Auswirkungen
  - Budgetbeschränkungen, die die Implementierung von Sicherheitskontrollen beeinflussen
  - Zeitdruck, der Abkürzungen beim Sicherheitstest erfordert

Routinemässige Sicherheitsleitlinien (Anforderungsinterpretation, Kontrollauswahl, Testverfahren) MÜSSEN über die Unterstützung des InfoSec-Beauftragten ohne Eskalation verwaltet werden, sofern die Entscheidungsbefugnis den Projektteam-Umfang nicht übersteigt.

## Ausnahmenmanagement

Ausnahmen von Sicherheitsanforderungen MÜSSEN:

- Mit geschäftlicher Begründung und kompensierenden Kontrollen dokumentiert werden
- Von der zuständigen Behörde auf Basis der Projektklassifizierung genehmigt werden
- Zeitlich begrenzt sein und im Sicherheitsausnahmenregister erfasst werden
- Vom ISB quartalsweise überprüft werden

## Richtlinienüberprüfung

Diese Richtlinie MUSS überprüft werden:

- Jährlich (Minimum) durch den ISB
- Nach schwerwiegenden Projektfehlern mit Sicherheitsursachen
- Bei regulatorischen Änderungen, die die Projektsicherheit betreffen
- Bei wesentlichen organisatorischen Änderungen

---

# Compliance und Überwachung

## Compliance-Anforderungen

| Anforderung | Compliance-Massnahme |
|-------------|---------------------|
| Projektklassifizierung | Alle Projekte innerhalb von 5 Werktagen nach der Initiierung klassifiziert |
| Sicherheitsanforderungen | Für alle Mittel-/Hochrisiko-Projekte vor der Ausführung dokumentiert |
| Sicherheitstests | Vor dem Deployment für alle Projekte abgeschlossen |
| Akzeptanz von Restrisiken | Formal vor dem Projektabschluss dokumentiert |
| Lessons Learned | Für alle Mittel-/Hochrisiko-Projekte erfasst |

## Überwachung und Metriken

[Organisation] MUSS Projektsicherheitsmetriken nachverfolgen, einschliesslich:

- Projekte nach Sicherheitsklassifizierung
- Projekte mit abgeschlossenen Sicherheitsbewertungen
- Sicherheitsbefunde nach Schweregrad und Behebungsstatus
- Gewährte Sicherheitsausnahmen

**Anforderungen an die Metrikberichterstattung**:

- **Monatlicher ISB-Bericht**: Detailliertes Metriken-Dashboard einschliesslich:
  - Projekte nach Klassifizierung und Sicherheitsstatus (auf Kurs / gefährdet / überfällig)
  - Offene Sicherheitsbefunde nach Schweregrad und Alter
  - Gewährte vs. behobene Sicherheitsausnahmen
  - Abschlussraten von Sicherheitstests
  - Erforderliche Massnahmen: ISB überprüft auf Trends, die ein Eingreifen erfordern (z. B. >20 % der Hochrisiko-Projekte mit überfälligen Sicherheitsbewertungen)

- **Quartalsbericht für die Geschäftsleitung**: Zusammenfassung für die Führungsebene einschliesslich:
  - Gesamtprojektanzahl und Anzahl der Hochrisiko-Projekte
  - Kritische Sicherheitsbefunde und Behebungsstatus
  - Sicherheitsausnahmen, die des Bewusstseins der Führungsebene bedürfen
  - Wesentliche Sicherheitsvorfälle, die Projekte betreffen
  - Erforderliche Massnahmen: Geschäftsleitung akzeptiert Restrisiken für kritische Projekte

Metriken werden auf der GRC-Plattform / im Projekt-Dashboard gepflegt und für autorisiertes Personal gemäss Zugriffskontrolle A.5.15-18 zugänglich gemacht.

## Nichteinhaltung

Die Nichteinhaltung dieser Richtlinie kann folgende Konsequenzen haben:

- Projektverzögerungen, bis Sicherheitsanforderungen erfüllt sind
- Eskalation zur Geschäftsleitung
- Disziplinarmassnahmen gemäss HR-Richtlinien von [Organisation]

---

# Verwandte Dokumente

## ISMS-Dokumente

| Dokument-ID | Dokumententitel |
|-------------|----------------|
| ISMS-POL-00 | Regulatorischer Anwendbarkeitsrahmen |
| ISMS-IMP-A.5.8-UG/TG | Informationssicherheit im Projektmanagement — Implementierungsleitfaden |
| ISMS-POL-A.5.15-18 | Identitäts- und Zugangsverwaltung |
| ISMS-POL-A.5.19-22 | Sicherheit in Lieferantenbeziehungen |
| ISMS-POL-A.8.24 | Einsatz von Kryptografie |
| ISMS-POL-A.8.25-28 | Sicherer Entwicklungslebenszyklus |
| ISMS-POL-A.8.32 | Änderungsmanagement |

## Externe Referenzen

| Referenz | Beschreibung |
|----------|-------------|
| ISO/IEC 27001:2022 | Informationssicherheits-Managementsysteme — Anforderungen |
| ISO/IEC 27002:2022 | Informationssicherheitskontrollen — Leitlinien |
| ISO 21500:2021 | Projekt-, Programm- und Portfoliomanagement |
| NIST SP 800-64 | Sicherheitsüberlegungen im System-Entwicklungslebenszyklus |

---

# Nachweise für diese Richtlinie

**Stage 1 (Dokumentationsprüfung) Nachweise:**

Erforderliche Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.8 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL und Geschäftsleitung
- ✅ Projektklassifizierungsrahmen definiert (Abschnitt 2.2)
- ✅ Sicherheitsanforderungen an Phasengates dokumentiert (Abschnitt 2.3)
- ✅ Kategorien der Sicherheitsanforderungen spezifiziert (Abschnitt 2.4)
- ✅ Sicherheitstestanforderungen nach Klassifizierung (Abschnitt 2.5)
- ✅ Sicherheitsübergabeanforderungen dokumentiert (Abschnitt 2.6)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Abschnitt 3)
- ✅ Governance und Ausnahmeverfahren definiert (Abschnitt 4)
- ✅ Integration mit verwandten Kontrollen dokumentiert (Abschnitt 6)

**Stage 2 (Operative Wirksamkeit) Nachweise:**

Erforderliche Nachweise, die belegen, dass diese Richtlinie operativ wirksam ist:

- Projektklassifizierungsgenehmigungen mit dokumentierten Sicherheitsrisiko-Einstufungen (Hoch/Mittel/Niedrig)
- Sicherheitsanforderungsregister für Mittel-/Hochrisiko-Projekte
- Phasegate-Genehmigungsunterlagen mit Sicherheitskriterien-Verifizierung
- Sicherheitstestberichte (Penetrationstests, Schwachstellenscans, Code-Reviews) nach Projektklassifizierung
- Sicherheitsbefunde und Nachverfolgung der Behebung bis zum Abschluss
- Sicherheitsübergabe-Dokumentationspakete
- Risikoakzeptanzunterlagen mit entsprechenden Genehmigungen
- Lessons-Learned-Dokumentation für Mittel-/Hochrisiko-Projekte
- Sicherheitsausnahmenregister mit Genehmigungen und Zeitlimits
- Projektsicherheitsmetriken-Dashboards mit Trends
- Schulungsnachweise für Projektmanager zu Sicherheitsanforderungen
- Ausgaben des Sicherheitsbewertungs-Arbeitsbuchs (aus ISMS-IMP-A.5.8)

## Klarstellung zu Compliance-Nachweisen

Diese Richtlinie legt Anforderungen an die Sicherheitsintegration im Projektmanagement-Governance fest. Sie legt NICHT fest:

- **Spezifische technische Sicherheitskontrollen** (adressiert in technischen Kontrollrichtlinien A.8.x)
- **Projektmanagement-Methodik** (organisatorische Wahl — Agile, Wasserfall, hybrid)
- **Lieferantenauswahlkriterien** (adressiert in A.5.19-22 Sicherheit in Lieferantenbeziehungen)
- **Techniken für Anwendungssicherheitstests** (adressiert in A.8.25-28 Sicherer Entwicklungslebenszyklus)

Die Abgrenzung: POL-A.5.8 definiert, WELCHE Sicherheitsaktivitäten in jeder Projektphase stattfinden müssen und WER genehmigt → ISMS-IMP-A.5.8 liefert, WIE Sicherheitsanforderungen bewertet und Compliance nachverfolgt werden → Technische Kontrollen (A.8.x) definieren spezifische erforderliche Sicherheitsfähigkeiten.

---

# Genehmigungsprotokoll

| Rolle | Name | Unterschrift | Datum |
|-------|------|-------------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | | [Datum festzulegen] |
| **IT-Leiter (ITL)** | [Name] | | [Datum festzulegen] |
| **Chief Operating Officer (COO)** | [Name] | | [Datum festzulegen] |
| **Rechts-/Compliance-Beauftragter** | [Name] | | [Datum festzulegen] |
| **Geschäftsleitung** | [Name] | | [Datum festzulegen] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen an die Integration von Informationssicherheit in das Projektmanagement fest. Implementierungsverfahren, Bewertungsvorlagen und detaillierte Leitlinien sind in ISMS-IMP-A.5.8 (UG/TG) dokumentiert.*

<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.8-DE:framework:POL:a.5.8 -->

<!-- QA_VERIFIED: 2026-03-28 -->
