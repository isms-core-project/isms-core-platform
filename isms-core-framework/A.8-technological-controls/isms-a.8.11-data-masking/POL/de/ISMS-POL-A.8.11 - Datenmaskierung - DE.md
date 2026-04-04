<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.11-DE:framework:POL:a.8.11 -->
**ISMS-POL-A.8.11 — Richtlinie zur Datenmaskierung**
**Datenmaskierung und Pseudonymisierung zum Schutz sensibler Informationen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zur Datenmaskierung |
| **Dokumententyp** | ISMS-Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.11 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Aktiv |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|-----------|
| 1.0 | [Date] | ISB | Erstveröffentlichung für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich oder bei wesentlichen Änderungen
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]
**Genehmiger**: ISB, ITL, DSB, Legal/Compliance Officer, Geschäftsleitung

**Verteilung**: Alle Mitarbeitenden, IT-Betrieb, Entwicklungsteams, Dateneigentümer, Compliance-Beauftragter, interne Revision

---

# Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an die Datenmaskierung, Pseudonymisierung und damit verbundene Techniken zum Schutz sensibler Informationen in nicht produktiven Umgebungen und bei der Steuerung des Produktionszugriffs fest.

**Kernanforderungen**: Sensitive Daten — insbesondere personenbezogene Daten (PII), Finanzdaten, Gesundheitsdaten und Zugangsdaten — müssen in nicht produktiven Umgebungen (Test, Entwicklung, Analyse, Training) maskiert werden. Zugriff auf nicht maskierte Daten in der Produktion ist auf den geringst notwendigen Umfang zu beschränken.

**Anwendungsbereich**: Alle Systeme, Datenbanken, Anwendungen und Umgebungen, in denen [Organisation] sensitive Daten verarbeitet; gilt für alle Mitarbeitenden, Auftragnehmer und Drittanbieter.

---

# Steuerungsausrichtung und Anwendungsbereich

## Primärsteuerung

**ISO 27001:2022 Anhang A Steuerung A.8.11 — Datenmaskierung**:

> Datenmaskierung sollte in Übereinstimmung mit der themenspezifischen Zugangskontrollrichtlinie der Organisation und anderen damit verbundenen themenspezifischen Richtlinien sowie den geschäftlichen Anforderungen unter Berücksichtigung geltender Rechtsvorschriften eingesetzt werden.

Diese Richtlinie setzt A.8.11 unter Berücksichtigung der Anforderungen aus ISO 27701:2019 (Datenschutz-Informationsmanagement) und geltender Datenschutzgesetzgebung um.

## Anwendungsbereich

**Sachlicher Geltungsbereich**: Diese Richtlinie gilt für:

- Alle Datenbanken, die personenbezogene Daten, Finanzdaten, Gesundheitsdaten oder andere sensitive Informationen enthalten
- Alle nicht produktiven Umgebungen, die aus Produktionssystemen bezogene Daten verwenden
- Alle Datenanalyse-, Business-Intelligence- und Berichtsumgebungen mit individuellen Datensätzen
- Alle Dateiexporte, Sicherungen oder Archive mit sensitive Daten
- Alle durch Drittanbieter verarbeiteten Daten, sofern sensitive Informationen involviert sind

**Persönlicher Geltungsbereich**: Diese Richtlinie gilt für:

- Alle Mitarbeitenden von [Organisation] in Bezug auf die Handhabung sensibler Daten
- IT-Betrieb beim Einrichten und Warten von Umgebungen
- Entwicklungsteams bei der Erstellung und dem Test von Applikationen
- Datenwissenschafts- und Analyseteams beim Umgang mit Daten
- Drittanbieter und Auftragnehmer gemäss vertraglicher Vereinbarungen

## Regulatorische Anwendbarkeit

**Tier 1 — Verbindliche Anforderungen (universell für [Organisation])**:

| Regulierung | Relevante Anforderung | Anwendung |
|-------------|----------------------|-----------|
| **Schweizer nDSG** | Art. 8, 25 — Datensparsamkeit und Datenschutz durch Technik | Alle Personendaten |
| **EU DSGVO** | Art. 5(1)(c), 25, 32 — Datenminimierung, Datenschutz durch Technik, Sicherheit | Personendaten von EU-Betroffenen |
| **ISO 27001:2022** | A.8.11 — Datenmaskierung | Alle sensitive Informationen |

**Tier 2 — Bedingte Anforderungen (wenn anwendbar)**:

| Regulierung | Auslöser | Anforderung |
|-------------|---------|-------------|
| **PCI DSS v4.0.1** | Verarbeitung von Kartenzahlungsdaten | Req. 3.4, 3.5 — PAN-Maskierung und -Schutz |
| **HIPAA** | Verarbeitung von US-Gesundheitsdaten | §164.514 — De-Identifizierung; §164.312 — technische Schutzmassnahmen |
| **FINMA** | Beaufsichtigte Finanzdienstleistungen (CH) | Risikobasierte Datenschutzmassnahmen |
| **DORA** | Finanzdienstleistungen in der EU | Art. 9 — IKT-Sicherheit einschliesslich Datenschutz |
| **NIS2** | Kritische oder wichtige Einrichtungen in der EU | Art. 21 — Datenschutzsteuerungen |
| **ISO 27701:2019** | Datenschutz-Informationsmanagement | A.7.4.3, A.8.4.3 — Pseudonymisierung |

*Bedingte Anforderungen gelten gemäss ISMS-POL-00 und dem Risikobewertungsrahmen von [Organisation].*

---

# Richtlinienanforderungen

## Datenklassifizierung und Identifizierungsanforderungen

### Datenklassifizierung und Maskierungsschwellenwert

Die Anforderungen an die Datenmaskierung richten sich nach der Datenklassifizierung gemäss Informationsklassifizierungsrichtlinie von [Organisation] (ISMS-POL-A.5.12):

| Klassifizierungsstufe | Sensitivitätsniveau | Maskierungsanforderung |
|-----------------------|---------------------|----------------------|
| **Eingeschränkt** | Kritisch | Maskierung in ALLEN nicht produktiven Umgebungen obligatorisch; DDM in Produktion für eingeschränkten Rollenzugriff |
| **Vertraulich** | Hoch | Maskierung in nicht produktiven Umgebungen obligatorisch; DDM in Produktion empfohlen |
| **INTERN** | Mittel | Risikobasierte Maskierungsentscheidung; Dateneigentümer entscheidet je nach Kontext |
| **Öffentlich** | Niedrig | Maskierung nicht erforderlich |

### Datenkategorien mit Maskierungspflicht

Folgende Datenkategorien erfordern in allen nicht produktiven Umgebungen Maskierung:

**Personenbezogene Daten (PII)**:

- Vollständige Namen, Geburtsdaten, Nationalidentifikatoren (AHV-Nummer, Passnummern)
- Kontaktinformationen (E-Mail, Telefon, Adressen)
- Finanzidentifikatoren (Kontonummern, IBAN, Kreditkartennummern)
- Biometrische Daten und Gesundheitsdaten
- Standortdaten, die zur Identifizierung geeignet sind

**Finanzdaten**:

- Primäre Kontonummern (PAN) und Kartenzahlungsdaten
- Bankkontonummern und IBAN
- Einzelne Transaktionsbeträge und Gehaltsdaten
- Kreditwürdigkeitsbewertungen und Bonitätsinformationen

**Anmeldedaten und Zugangsdaten**:

- Passwörter, Passphrasen und Hashes
- API-Schlüssel, Tokens und Zertifikate
- Private Schlüssel und kryptografische Geheimnisse
- Multi-Faktor-Authentifizierungskodes

**Proprietäre Geschäftsdaten**:

- Proprietary Algorithmen, Formeln und Quellcode
- Vertragliche und kommerzielle Sensitivinformationen
- Daten zu Fusionen, Übernahmen und strategischen Initiativen

### Bestandsaufnahme sensitiver Daten

[Organisation] muss folgendes führen:

- Inventar aller Systeme und Datenbanken, die sensitive Daten enthalten (Dateneigentümer verantwortlich)
- Karte kritischer Felder mit ihrer Klassifizierungsstufe und dem Maskierungsstatus
- Dokumentation der Datenflüsse zwischen Produktions- und Nicht-Produktionsumgebungen

**Bestandspflege**: Dateneigentümer aktualisieren das Inventar jährlich und bei wesentlichen Systemänderungen. Eingeschränkte oder vertrauliche Datenquellen werden dabei priorisiert.

## Maskierungstechnik-Standards

### Genehmigte Maskierungstechniken

[Organisation] genehmigt folgende Maskierungstechniken basierend auf Anwendungsfall, Datensensitivität und regulatorischen Anforderungen:

| Technik | Beschreibung | Anwendungsfälle | Regulatorische Eignung |
|---------|-------------|----------------|----------------------|
| **Statische Datenmaskierung (SDM)** | Permanenter Ersatz sensitiver Daten in nicht produktiven Datenbanken | Test, Entwicklung, QA-Datenprovisionierung | DSGVO, nDSG, allgemeiner Datenschutz |
| **Dynamische Datenmaskierung (DDM)** | Echtzeit-Maskierung am Zugriffspunkt auf Basis der Benutzerrolle; Originaldaten unverändert gespeichert | Produktionszugriffskontrolle, rollenbasierte Datenanzeige | DSGVO, nDSG, rollenbasierter Datenschutz |
| **Schwärzung** | Vollständige Entfernung oder Ersatz durch Platzhalterzeichen | Dokumentenfreigabe, Felder ohne Testnutzen | Alle Regulierungen |
| **Substitution** | Ersatz durch realistische, aber fiktive Werte unter Beibehaltung von Format und Struktur | Teste mit hohem Datentreue-Bedarf | DSGVO, nDSG, PCI DSS |
| **Tokenisierung** | Ersatz sensitiver Daten durch nicht sensitive Tokens; Originaldaten in gesichertem Vault gespeichert | Kartenzahlungsdaten, Identifikatoren mit Reversibilitätsbedarf | PCI DSS bevorzugt; DSGVO kompatibel |
| **Pseudonymisierung** | Ersatz direkter Identifikatoren durch Pseudonyme; separat gespeicherter Schlüssel zur Re-Identifizierung erforderlich | Analyse, Forschung, Statistik | DSGVO Art. 32(1)(a), Art. 89; nDSG |
| **Anonymisierung** | Irreversibler Entzug aller Identifizierungsinformationen | Externe Datenweitergabe, öffentliche Datensätze, langfristiger Datenerhalt | DSGVO (Daten kein Personenbezug mehr); nDSG |

**Detaillierte Technikspezifikationen**: Algorithmen, Konfigurationsparameter und Implementierungsmuster sind in ISMS-CTX-A.8.11 (Technische Referenz Datenmaskierung, KEIN ISMS-Dokument) dokumentiert.

### Auswahlkriterien für Techniken

Dateneigentümer und das Sicherheitsteam wählen Maskierungstechniken basierend auf folgenden Kriterien aus:

1. **Datensensitivität**: Höhere Klassifizierung erfordert stärkere Maskierung
2. **Reversibilitätsbedarf**: Legitimer Bedarf zur Datenwiederherstellung bestimmt die Technik
3. **Regulatorische Anforderungen**: DSGVO, PCI DSS, HIPAA haben spezifische Technikvorgaben
4. **Datennützlichkeit**: Maskierte Daten müssen für den beabsichtigten Zweck verwendbar sein
5. **Referenzielle Integrität**: Tabellenübergreifende Beziehungen nach der Maskierung aufrechterhalten
6. **Leistungsauswirkungen**: Echtzeit-DDM vs. Batch-SDM-Leistungsanforderungen

**Genehmigungsrahmen und Entscheidungsmatrix**: Vollständige Technikauswahlkriterien, Zulassungsanforderungen und Entscheidungsmatrix sind in Anhang A dokumentiert.

## Umgebungsabdeckungsanforderungen

### Umgebungsklassifizierung und Maskierungsanforderungen

| Umgebungstyp | Klassifizierung | Maskierungsanforderung | Frist |
|--------------|-----------------|----------------------|-------|
| **Produktion** | Produktiv | DDM für Rollenzugriffsbeschränkung auf Eingeschränkte/Vertrauliche Daten | Laufend |
| **Test/QA** | Nicht produktiv | Vollständige Maskierung aller Eingeschränkten und Vertraulichen Daten vor Verwendung | Vor Bereitstellung |
| **Entwicklung** | Nicht produktiv | Vollständige Maskierung; generierte oder maskierte Daten bevorzugt | Vor Bereitstellung |
| **Analyse/BI** | Nicht produktiv | Pseudonymisierung oder Anonymisierung für individuelle Datensätze | Vor Analyse |
| **Training** | Nicht produktiv | Vollständige Maskierung oder synthetische Daten | Vor Verwendung |
| **Sandbox** | Nicht produktiv | Vollständige Maskierung oder synthetische Daten | Vor Verwendung |
| **Sicherung/Archiv** | Nicht produktiv | Maskierung der Ausgangsdaten vor Erstellung der Sicherung; alternativ Verschlüsselung | Vor Sicherung |

### Produktionsumgebung (DDM-Anforderungen)

Für produktive Systeme, die Eingeschränkte oder Vertrauliche Daten enthalten:

- DDM-Regeln müssen auf der Grundlage dokumentierter Benutzerrollen und dem Least-Privilege-Prinzip konfiguriert sein
- DDM muss auf Datenbank- oder Applikationsebene durchgesetzt werden (nicht nur auf Client-Ebene)
- Alle Zugriffe auf maskierte Felder müssen zu Prüfzwecken protokolliert werden
- DDM-Bypass-Versuche sind zu erkennen und zu eskalieren

### Nicht produktive Umgebungen (SDM-Anforderungen)

Für alle nicht produktiven Umgebungen, die aus Produktionssystemen stammende Daten verwenden:

- Sensitive Daten müssen vor dem Verlassen der Produktionsumgebung maskiert werden
- Nicht maskierte Produktionsdaten dürfen nicht in nicht produktive Umgebungen kopiert werden
- Maskierungsprozesse müssen vor Bereitstellung der Daten abgeschlossen sein
- Maskierter Datensatz muss aufgezeichnet und verifiziert werden

## Test- und Validierungsanforderungen

### Testtypen

| Testtyp | Zweck | Häufigkeit | Verantwortlich |
|---------|-------|-----------|---------------|
| **Wirksamkeitstest** | Originaldaten nicht in maskierter Ausgabe vorhanden | Bei jeder Maskierungsoperation | Sicherheitsteam / IT-Betrieb |
| **Referenzielle-Integritäts-Test** | Foreign Keys und Joins nach Maskierung funktionsfähig | Nach SDM-Anwendung | IT-Betrieb |
| **Formatvalidierungstest** | Maskierte Daten bestehen Applikationsvalidierungsregeln | Bei jeder Maskierungsoperation | Entwicklungsteam |
| **Leistungstest** | Akzeptabler DDM-Overhead (typisch <10%) | Jährlich und nach Änderungen | IT-Betrieb |
| **Re-Identifizierungsrisikotest** | Maskierte Daten erlauben keine Identifikation von Einzelpersonen | Jährlich und bei Technikänderungen | Sicherheitsteam / DSB |
| **Regressionstest** | Bestehende Applikationsfunktionen nach Maskierungsänderungen | Nach Maskierungsänderungen | Entwicklungsteam |

### Validierungsmethodik

**Wirksamkeitsvalidierung**:

1. Stichprobenartige Überprüfung des Originaldatensatzes: Kein Originaldatenwert in maskierter Ausgabe vorhanden
2. Reverse-Engineering-Test: Keine bekannte Methode zur Rückgewinnung von Originaldaten aus maskierter Ausgabe
3. Ähnlichkeitsvergleich: Maskierte Werte nicht annähernd identisch mit Originalwerten

**Akzeptanzkriterien**:

- Kein Nachweis nicht maskierter sensitiver Daten (Pass/Fail)
- Referenzielle Integrität zu 100% in geprüften Beziehungen gewahrt
- Alle Applikationsvalidierungsregeln mit maskierten Daten bestanden
- Re-Identifizierungsrisiko unter dem definierten Schwellenwert (k-Anonymität ≥ 5 für DSGVO-Zwecke)
- Leistungsoverhead innerhalb der akzeptablen Grenzen (DDM typisch <10%)

## Protokollierung und Überwachung

### Protokollierungspflichtige Ereignisse

| Ereignistyp | Protokollierungspflicht | Aufbewahrung |
|-------------|------------------------|-------------|
| **Maskierungsoperationen** (SDM) | Datum/Uhrzeit, Umgebung, Datenkategorien maskiert, ausführende Person | 3 Jahre |
| **DDM-Regelanwendungen** | Benutzer, Zeitstempel, angewendete Maskierungsregel, Datenkategorie | 1 Jahr |
| **Ausnahmen (genehmigte)** | Ausnahme-ID, Geltungsbereich, Genehmiger, Ablaufdatum | 5 Jahre |
| **Re-Identifizierungsversuche** | Alle Versuche, Benutzer, Zeitstempel, Ergebnis | 5 Jahre |
| **Maskierungsfehler** | Ereignis, betroffene Systeme, Eskalation | 3 Jahre |
| **De-Tokenisierungsanfragen** | Anforder, Zeitstempel, Token-Referenz, Genehmigung | 5 Jahre |

### Überwachungsanforderungen

- Echtzeit-Warnungen bei Maskierungsfehlern oder nicht autorisiertem Zugriff auf nicht maskierte Daten
- Monatliche Überprüfung der DDM-Regelanwendung für kritische Datenfelder
- Vierteljährliche Überprüfung von Ausnahmen zum Ablauf und erneuerungspflichtigen Fällen
- Jährliche Überprüfung der Maskierungsabdeckung über alle Umgebungen

---

# Rollen und Verantwortlichkeiten

## Rollenmatrix

| Rolle | Verantwortlichkeit |
|-------|-------------------|
| **Geschäftsleitung** | Genehmigung dieser Richtlinie; Ressourcenzuweisung; Rechenschaftspflicht für Compliance auf Unternehmensebene |
| **ISB** | Richtlinienverantwortung; Genehmigung von Ausnahmen (Hoch/Kritisch); Eskalation von Vorfällen; jährliche Überprüfung |
| **DSB** | DSGVO/nDSG-Compliance-Überwachung; Validierung der Pseudonymisierungsadäquanz; Genehmigung bei DSGVO-relevanten Ausnahmen |
| **CDO / Data Governance** | Governance der Datenmaskierungspraxis; Standards für Datenkatalog und -klassifizierung; Compliance-Berichterstattung |
| **Dateneigentümer** | Daten in ihrer Domäne klassifizieren; Maskierungsanforderungen festlegen; Ausnahmen genehmigen (Mittel-Niveau); Wirksamkeit validieren |
| **Sicherheitsteam** | Maskierungssteuerungen implementieren; Konfigurationen auf Compliance prüfen; Vorfallreaktionsunterstützung; Wirksamkeitstests |
| **IT-Betrieb** | Maskierungstechnologien deployen und warten; Datenprovisionierungs-Workflows ausführen; SDM-Prozesse durchführen |
| **Entwicklungsteams** | DDM in Applikationen implementieren; maskierte Daten in nicht produktiven Umgebungen verwenden; Maskierungskompatibilität validieren |
| **Compliance / Revision** | Compliance der Maskierungskontrollen prüfen; regulatorische Anforderungen melden; Ausnahmen eskalieren |
| **Alle Nutzer** | Nicht autorisierten Zugriff auf nicht maskierte Daten melden; Re-Identifizierungsversuche unterlassen |

## RACI-Matrix

| Aktivität | Geschäftsleitung | ISB | DSB | Dateneigentümer | Sicherheitsteam | IT-Betrieb | Entwicklung | Compliance |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Sensitive Daten inventarisieren | I | A | B | V | B | I | I | I |
| Maskierungstechniken auswählen | I | A | B | V | V | B | B | I |
| SDM implementieren | I | A | I | B | B | V | V | I |
| DDM-Regeln konfigurieren | I | A | B | B | B | V | V | I |
| Maskierungswirksamkeit validieren | I | A | B | V | V | B | B | I |
| Ausnahmen genehmigen | A | V | B | V | B | I | I | B |
| Vorfälle bei Maskierungsfehlern melden | I | V | B | B | V | V | B | B |
| Compliance prüfen | I | A | B | B | B | I | I | V |

*V=Verantwortlich, A=Accountable, B=Beratend, I=Informiert*

## Beurteilung und Überprüfung

**Häufigkeit**:

- **Jährlich**: Vollständige Bewertung der Maskierungssteuerungen für alle Hochrisiko-Systeme
- **Quartalsweise**: Überprüfung DDM-Regelkonfigurationen; Status genehmigter Ausnahmen
- **Anlassbezogen**: Nach wesentlichen System- oder Datenstrukturänderungen; nach Datenschutzvorfällen; wenn neue regulatorische Anforderungen die Maskierungspraxis betreffen

**Methodik**: Stichprobenartige Tests, Konfigurationsüberprüfungen, Wirksamkeitsvalidierungen für SDM und DDM-Steuerungen; Verifikation der Bestandsabdeckung.

## Ausnahmemanagement

### Genehmigungsmatrix

| Ausnahmetyp | Genehmigungsbehörde | Maximale Dauer |
|-------------|---------------------|---------------|
| Eingeschränkte Daten in nicht produktiver Umgebung | ISB + Dateneigentümer + Geschäftsleitung | 3 Monate |
| Vertrauliche Daten in nicht produktiver Umgebung | ISB + Dateneigentümer | 6 Monate |
| Verzögerte DDM-Implementierung (Produktion) | ISB + Dateneigentümer | 3 Monate |
| Verwendung einer alternativen Maskierungstechnik | ISB + Sicherheitsteam | 12 Monate |
| Freigabe von teilweise pseudonymisierten Daten | ISB + DSB | 6 Monate |
| Temporäre Maskierungsdeaktivierung für Diagnose | ISB + Dateneigentümer | 24 Stunden |

### Dokumentationsanforderungen

Alle Ausnahmen müssen Folgendes enthalten:

- Eindeutige Ausnahme-ID (EXC-A811-JJJJ-NNN)
- Klarer Umfang: Betroffene Systeme, Datenkategorien, Umgebungen
- Geschäftliche Begründung: Warum Maskierung nicht durchführbar ist
- Risikobeurteilung: Inhärentes Risiko, Bedrohungsszenarien, Compliance-Auswirkungen
- Kompensierende Massnahmen: Alternative Schutzkontrollen, die Risiken mildern
- Überwachungsplan: Überprüfungshäufigkeit und Widerrufsbedingungen
- Genehmigungs-Signaturen: Alle erforderlichen Genehmiger für den Ausnahmetyp

**Ausnahmevorlage**: Standardisiertes Format in Anhang B.

### Überwachung von Ausnahmen

- Alle genehmigten Ausnahmen werden im Ausnahmeregister (ISMS-IMP-A.8.11-3) erfasst
- Vierteljährliche Überprüfung auf ablaufende Ausnahmen (30 Tage vor Ablauf)
- Jährliche Überprüfung aller aktiven Ausnahmen durch den ISB
- Widerruf bei: Eintritt von Ausnahmebedingungen, Sicherheitsvorfall im Zusammenhang mit nicht maskierten Daten, Wegfall der Geschäftsbegründung

## Vorfallreaktion

### Schweregrade

| Vorfalltyp | Schweregrad | Erstreaktion |
|------------|-------------|-------------|
| Nicht maskierte Produktionsdaten in öffentlich zugänglicher Umgebung | Kritisch | Sofortiger Zugangssperr, Vorfallreaktion innerhalb 1 Std. |
| Nicht maskierte Produktionsdaten in interner Test/Dev-Umgebung | Hoch | Zugang sperren, Benachrichtigung innerhalb 4 Std. |
| DDM-Bypass in Produktion durch nicht autorisierten Benutzer | Kritisch | Konto sperren, Protokolle sichern, Vorfallreaktion |
| Gagangsvorsatz zur Re-Identifizierung | Hoch | Kontozugang sperren, forensische Aufbewahrung, HR eskalieren |
| Maskierungsfehler, kein Datenverlust, interne Umgebung | Mittel | Umgebung isolieren, Maskierung erneut anwenden, Überprüfung |
| Unbekannte nicht maskierte Felder entdeckt | Niedrig | Dokumentieren, Maskierung anwenden, Dateneigentümer benachrichtigen |
| Token-Vault-Kompromittierung | Kritisch | Sofortiger Widerruf, Neuausgabe aller Tokens, Vorfallreaktion |

### Reaktionsprozess (7 Schritte)

1. **Erkennen**: Automatisierte Überwachung oder manuelle Identifizierung des Vorfalls
2. **Einschränken**: Zugang zu betroffenen Systemen/Daten sperren
3. **Benachrichtigen**: ISB, DSB, IT-Betrieb und betroffene Dateneigentümer informieren
4. **Bewerten**: Umfang des Vorfalls, betroffene Daten, betroffene Personen ermitteln
5. **Beheben**: Maskierung anwenden, nicht maskierte Daten entfernen, Steuerungen wiederherstellen
6. **Melden**: Vorfall an Aufsichtsbehörde melden, falls DSGVO/nDSG-Meldepflicht gilt
7. **Nachbesprechen**: Ursachenanalyse, Prozess verbessern, Kontrollen verstärken

**Kritische Vorfälle** (Kritisch/Hoch): Vorfallleitung unverzüglich benachrichtigen; Vorfallreaktion innerhalb 1 Stunde aktivieren.

**Meldepflicht**: Bei Nachweis oder begründetem Verdacht auf DSGVO-Datenpannen ist unverzüglich nach Art. 33 DSGVO (72-Stunden-Frist) zu melden; Verletzungen von nDSG-Pflichten gemäss Art. 24 nDSG dem EDÖB zu melden.

## Richtlinien-Governance

### Überprüfungsauslöser

Diese Richtlinie wird überprüft bei:

- Jährlichem planmässigem Überprüfungszyklus
- Wesentlichen Änderungen an Datenmaskierungstechnologien oder -praktiken
- Neue regulatorische Anforderungen mit Auswirkungen auf Maskierungsvorgaben
- Datenschutzvorfall, der systemische Maskierungsmängel aufzeigt
- Wesentlichen Änderungen an Datenverarbeitungsaktivitäten von [Organisation]
- Empfehlungen aus internen oder externen Revisionen

### Dokumentations-Aufbewahrung und Zugang

**Aufbewahrung**:

- Aktuelle Version: Unbegrenzt (bis zur Ablösung)
- Frühere Versionen archiviert: Mindestens 3 Jahre, schreibgeschützt, zeitgestempelt und integritätsgeschützt

**Zugangskontrolle**:

| Rolle | Zugangsstufe |
|-------|-------------|
| **Alle Mitarbeitenden** | Lesen (aktuelle Version) |
| **Sicherheitsteam** | Lesen/Schreiben (aktuelle Version) |
| **ISB** | Lesen/Schreiben (alle Versionen) |
| **DSB** | Lesen (alle Versionen) |
| **Compliance-Beauftragter** | Lesen (alle Versionen) |
| **Interne Revision** | Lesen (alle Versionen) |
| **Externe Prüfer** | Lesen (aktuelle Version, auf Anfrage) |

### Schulung und Sensibilisierung

**Sicherheitsbewusstsein** (Alle Mitarbeitenden):

- Jährliche Sicherheitsbewusstseinsschulung mit Überblick über Datenmaskierung
- Nutzerverantwortlichkeiten beim Umgang mit maskierten Daten
- Erkennen nicht maskierter sensitiver Daten und Meldewege
- Verbot von Re-Identifizierungsversuchen

**Technische Schulung** (IT/Sicherheitsteam):

- Konfiguration und Wartung von Datenmaskierungstechnologien
- Technikauswahl und Implementierung
- Test- und Validierungsverfahren
- Vorfallreaktion bei Maskierungsfehlern

**Dateneigentümer-Schulung** (Dateneigentümer):

- Datenklassifizierung und Maskierungsentscheidungsrahmen
- Beurteilungskriterien für Ausnahmeanträge
- Validierung der Maskierungswirksamkeit in ihren Domänen

**Entwickler-Schulung** (Entwicklungsteams):

- Verwendung maskierter Daten in nicht produktiven Umgebungen
- Implementierung dynamischer Maskierung in Applikationen
- Sichere Entwicklungspraktiken mit sensitiven Daten

---

# Implementierung und Referenzen

## Integration ins ISMS

Diese Richtlinie ist in das Informationssicherheitsmanagementsystem von [Organisation] integriert:

**Risikobeurteilung** (ISO 27001 Klausel 6.1):

- Datenmaskierungssteuerungen werden auf Basis der Risikobeurteilung von [Organisation] ausgewählt
- Datenklassifizierung bestimmt Maskierungsanforderungen
- Risikobehandlungspläne dokumentieren Implementierung der Datenmaskierungssteuerungen
- Restrisiken (wo Maskierung nicht durchführbar) werden dokumentiert und akzeptiert

**Anwendbarkeitserklärung** (ISO 27001 Klausel 6.1.3):

- Anwendbarkeit von Steuerung A.8.11 im SoA von [Organisation] begründet
- Implementierungsstatus verfolgt und berichtet
- Steuerungswirksamkeit durch Beurteilungsprogramm gemessen

**Verwandte Steuerungen**:

| Steuerung | Beziehung zur Datenmaskierung |
|-----------|------------------------------|
| **A.5.12 (Klassifizierung von Informationen)** | Grundlage — Datenklassifizierung steuert Maskierungsentscheidungen |
| **A.5.15 (Zugangskontrolle)** | Ergänzend — Maskierung bietet Defense-in-Depth über Zugangskontrolle hinaus |
| **A.8.3 (Management privilegierter Zugriffsrechte)** | Integration — privilegierte Benutzer können auf nicht maskierte Daten mit Überwachung zugreifen |
| **A.8.10 (Informationslöschung)** | Ergänzend — Löschung ist getrennt von Maskierung |
| **A.8.24 (Kryptografie)** | Ergänzend — Verschlüsselung schützt im Transit/Ruhezustand; Maskierung verbirgt bei Verwendung |
| **A.5.9 (Inventar von Informationen)** | Grundlage — Asset-Inventar identifiziert maskierungspflichtige Systeme |
| **A.5.23 (Cloud-Dienste)** | Integration — Cloud-Datenmaskierungsanforderungen nach Anbietermodell |
| **A.5.7 (Bedrohungsintelligenz)** | Informativ — Bedrohungslandschaft informiert Maskierungsprioritäten |
| **A.5.24 (Vorfallmanagement)** | Integration — Maskierungsfehler als Vorfälle behandelt |

## Implementierungsressourcen

**Implementierungsanleitung** (ISMS-IMP-A.8.11 Suite):

- **ISMS-IMP-A.8.11-1**: Dateninventar und Klassifizierungsbeurteilung
  - Methodik zur Inventarisierung sensitiver Daten
  - Datenklassifizierungsbeurteilung
  - Systeminventar mit sensitiven Daten
  - Zuweisung von Dateneigentümern
  - Evidenzregister

- **ISMS-IMP-A.8.11-2**: Auswahl der Maskierungstechnik und Anforderungen
  - Dokumentation der genehmigten Technikimplementierung
  - Entscheidungsrahmen für Technikauswahl
  - Vergleich statischer vs. dynamischer Maskierung
  - Fähigkeitsbewertung der Tools (herstellerneutral)
  - Konfigurationsstandards

- **ISMS-IMP-A.8.11-3**: Beurteilung der Umgebungsabdeckung
  - Umgebungsinventar und -klassifizierung
  - Lückenanalyse bei der Abdeckung
  - Verifizierung der Maskierungsimplementierung
  - Ausnahmeverfolgung
  - Behebungsplanung

- **ISMS-IMP-A.8.11-4**: Test- und Validierungsrahmen
  - Testmethodik und -verfahren
  - Wirksamkeitsvalidierungskriterien
  - Re-Identifizierungsrisikobeurteilung
  - Regulatorische Compliance-Validierung
  - Vorfallreaktionsverfahren

**Technische Referenz** (KEIN ISMS-Dokument):

- **ISMS-CTX-A.8.11**: Technische Referenz Datenmaskierung
  - Detaillierte Technikspezifikationen zur Maskierung
  - Tiefgehende Datenentdeckungsmethodik
  - Analyse der Maskierungs-Tool-Landschaft (herstellerneutral)
  - Implementierungsmuster und -architekturen
  - Kurzreferenzhandbücher für Praktiker
  - **Hinweis**: Dieses Dokument ist KEIN ISMS-Dokument und legt keine verbindlichen Anforderungen fest

## Regulatorische Zuordnung

Diese Richtlinie behandelt Datenmaskierungsanforderungen aus:

| Anforderungskategorie | Schweizer nDSG | EU DSGVO | ISO 27001 | PCI DSS v4.0.1* | HIPAA* | FINMA* | DORA/NIS2* |
|----------------------|---------------|---------|-----------|---------|--------|--------|------------|
| Datenminimierung | Art. 8, 25 | Art. 5(1)(c) | A.8.11 | Req. 12.3 | §164.514 | Risikobasiert | Art. 21 (NIS2) |
| Pseudonymisierung | Art. 8 | Art. 32(1)(a), Art. 89 | A.8.11 | N/A | §164.514(b) | Risikobasiert | Risikobasiert |
| Maskierung in nicht produktiven Umgebungen | Art. 8 | Art. 25, 32 | A.8.11 | Req. 3.4, 12.3 | §164.514 | Risikobasiert | Risikobasiert |
| Test und Validierung | Art. 8 | Art. 25, 32 | A.8.11 | Req. 11.3 | §164.308(a)(8) | Risikobasiert | Art. 9 (DORA) |
| Zugangsprotokollierung | Art. 8 | Art. 32(1)(d) | A.8.16 | Req. 10 | §164.312(b) | Risikobasiert | Überwachung |
| Vorfallreaktion | Art. 24 | Art. 33-34 | A.5.24 | Req. 12.10 | §164.404 | Vorfallmgmt. | Art. 23 (DORA) |

*Bedingte Anwendbarkeit gemäss ISMS-POL-00

---

# Definitionen

**Anonymisierung**: Irreversibler Prozess zur Entfernung aller identifizierenden Informationen aus Daten, sodass eine Re-Identifizierung auch mit zusätzlichen Daten oder Aufwand nicht möglich ist. Anonymisierte Daten sind unter der DSGVO keine Personendaten mehr.

**Kompensierende Massnahme**: Alternative Sicherheitskontrolle, die implementiert wird, wenn die primäre Steuerung (Maskierung) technisch oder betrieblich nicht durchführbar ist und einen gleichwertigen Risikominderungseffekt bietet.

**Datenklassifizierung**: Prozess der Kategorisierung von Daten nach Sensitivität, Kritikalität und regulatorischen Anforderungen zur Bestimmung geeigneter Schutzmassnahmen einschliesslich Maskierung.

**Datenkustos**: IT-Betriebspersonal, das für den Einsatz und die Pflege technischer Infrastruktur einschliesslich Maskierungslösungen verantwortlich ist. Kustodinnen und Kustodinnen implementieren Anforderungen der Dateneigentümer.

**Datenmaskierung**: Prozess der Verschleierung von Originaldaten durch modifizierten Inhalt (maskierte Werte) zum Schutz sensitiver Informationen unter Beibehaltung von Datenformat und Nutzbarkeit für legitime Zwecke.

**Dateneigentümer**: Geschäfts- oder Funktionsverantwortliche für Daten in ihrer Domäne, zuständig für Datenklassifizierung, Maskierungsanforderungen und Ausnahmegenehmigungen.

**Betroffene Person**: Einzelperson, deren personenbezogene Daten verarbeitet werden (DSGVO/nDSG-Terminologie).

**Dynamische Datenmaskierung (DDM)**: Echtzeit-Maskierung am Punkt des Datenzugriffs auf Basis der Benutzerrolle oder des Kontexts. Originaldaten bleiben im Speicher unverändert; Maskierung erfolgt bei Abfrage oder Abruf.

**Umgebung**: Systemkontext, in dem Daten verarbeitet werden (Produktion, Test, Entwicklung, Analyse, Training, Sandbox, Sicherung, Archiv). Unterschiedliche Umgebungen haben unterschiedliche Maskierungsanforderungen.

**Ausnahme**: Formal genehmigte Abweichung von Richtlinienanforderungen, dokumentiert mit Geschäftsbegründung, Risikobeurteilung, kompensierenden Massnahmen und Zeitbegrenzung.

**Formaterhaltung**: Beibehaltung des ursprünglichen Datenformats und der Datenstruktur in maskierten Daten, um Applikationskompatibilität und weiterhin gültige Validierungsregeln zu gewährleisten.

**Personenbezogene Daten (PII)**: Alle Informationen, die eine Person direkt (Name, ID-Nummer) oder indirekt (Kombination von Merkmalen) identifizieren können.

**Pseudonymisierung**: Ersatz direkter Identifikatoren durch Pseudonyme, sodass Daten ohne zusätzliche Informationen (Schlüssel oder Zuordnungstabelle), die separat aufbewahrt werden, keine Personen identifizieren können. Pseudonymisierte Daten bleiben unter der DSGVO Personendaten, jedoch mit reduziertem Risiko.

**Schwärzung**: Vollständige Entfernung oder Ersatz sensitiver Daten durch Platzhalterzeichen (z.B. `****`, `XXXX`, `[GESCHWÄRZT]`) ohne Ersatzwerte.

**Referenzielle Integrität**: Aufrechterhaltung gültiger Beziehungen zwischen verwandten Daten über Tabellen oder Datensätze hinweg, damit Foreign Keys und Joins nach der Maskierung weiterhin korrekt funktionieren.

**Re-Identifizierung**: Prozess der Ermittlung der ursprünglichen Identität einer betroffenen Person aus anonymisierten oder pseudonymisierten Daten durch Reverse Engineering, Verknüpfung mit externen Daten oder andere Techniken.

**Sensitive Daten**: Alle Informationen, die bei Offenlegung Einzelpersonen oder [Organisation] schaden könnten, einschliesslich PII, Finanzdaten, Gesundheitsdaten, Zugangsdaten und proprietäre Informationen. In der Regel als Vertraulich oder Eingeschränkt klassifiziert.

**Statische Datenmaskierung (SDM)**: Permanenter Ersatz sensitiver Daten durch maskierte Werte in nicht produktiven Datenbanken oder Datensätzen. Originaldaten werden irreversibel ersetzt; Maskierung erfolgt einmalig bei der Datenprovisionierung.

**Substitution**: Ersatz sensitiver Daten durch realistische, aber fiktive Werte, die Datenformat, Struktur und Nützlichkeit für beabsichtigte Zwecke (Test, Entwicklung, Analyse) aufrechterhalten.

**Tokenisierung**: Ersatz sensitiver Daten durch nicht sensitive Tokens (Ersatzwerte); Originaldaten in gesichertem Token-Vault gespeichert, wodurch Reversibilität bei Autorisierung ermöglicht wird.

---

# Anhang A: Genehmigungsrahmen für Maskierungstechniken

**Anwendungsbereich**: Dieser Anhang definiert den Genehmigungsrahmen und die Auswahlkriterien für Datenmaskierungstechniken. Alle genehmigten Techniken sind in Richtlinien-Abschnitt 2.2 aufgeführt. Organisationen wählen Techniken entsprechend ihren Datentypen, Anwendungsfällen und Risikoprofilen aus.

## A.1 Technologie-Genehmigungskriterien

Neue Maskierungstechniken oder Änderungen an genehmigten Techniken müssen folgende Kriterien vor der organisatorischen Genehmigung erfüllen:

**Sicherheitswirksamkeit**:

- Technik muss Originaldaten wirksam verschleiern
- Originaldaten dürfen ohne autorisierten Zugang zu Schlüsseln/Vaults (bei reversiblen Techniken) nicht wiederherstellbar sein
- Technik muss den Sensitivität der Daten angemessenen Re-Identifizierungsangriffen standhalten
- Technik muss auf bewährten Algorithmen oder branchenüblichen Praktiken basieren

**Regulatorische Compliance**:

- Technik muss regulatorische Anforderungen für anwendbare Datentypen erfüllen:
  - DSGVO-Pseudonymisierungsanforderungen (Art. 32(1)(a), Art. 89) bei DSGVO-Konformitätszweck
  - PCI DSS v4.0.1-Maskierungsanforderungen (Req. 3.4, 3.5) bei Zahlungskartendaten
  - HIPAA-De-Identifizierungsstandards (§164.514) bei US-Gesundheitsdaten
  - nDSG-Datenschutzanforderungen (Art. 8) bei Schweizer Personendaten
- Technik muss durch geeignete Stelle validiert sein (Sicherheitsteam, DSB, Compliance)

**Betriebliche Durchführbarkeit**:

- Technik muss in der technischen Umgebung von [Organisation] implementierbar sein
- Technik muss Datennützlichkeit für beabsichtigte Verwendungszwecke aufrechterhalten
- Technik muss Datenformat und referenzielle Integrität wo erforderlich erhalten
- Leistungsauswirkungen müssen für betriebliche Anforderungen akzeptabel sein
- Technik muss durch das technische Personal von [Organisation] wartbar sein

**Dokumentationsanforderungen**:

- Technikspezifikation in ISMS-CTX-A.8.11 (Technische Referenz) dokumentiert
- Anwendungsfälle und Auswahlkriterien dokumentiert
- Test- und Validierungsverfahren definiert
- Bekannte Einschränkungen und Restrisiken dokumentiert

## A.2 Entscheidungsmatrix zur Technikauswahl

**Entscheidungsmatrix**:

| Anwendungsfall | Datensensitivität | Reversibilitätsbedarf | Formaterhaltung | Empfohlene Technik |
|---------------|------------------|----------------------|----------------|--------------------|
| Nicht produktives Testen | Kritisch/Hoch | Nein | Ja | Statische Datenmaskierung (SDM) mit Substitution |
| Nicht produktive Entwicklung | Kritisch/Hoch | Nein | Ja | Statische Datenmaskierung (SDM) mit Substitution |
| Produktiver rollenbasierter Zugriff | Kritisch/Hoch | N/A (Original unverändert) | Ja | Dynamische Datenmaskierung (DDM) |
| Analyse/Berichterstattung | Hoch | Nein | Teilweise | Pseudonymisierung oder Aggregation |
| Externe Datenweitergabe | Kritisch/Hoch | Nein | Optional | Anonymisierung oder starke Pseudonymisierung |
| Kartenzahlungsdaten (nicht produktiv) | Kritisch | Bedingt | Ja | Tokenisierung oder SDM mit PCI-konformer Maskierung |
| Forschung/Statistik (DSGVO) | Hoch | Bedingt | Teilweise | Pseudonymisierung gemäss DSGVO Art. 89 |
| Training/Demonstration | Beliebig sensitiv | Nein | Optional | Schwärzung oder SDM mit Substitution |
| Öffentliche Datenfreigabe | Beliebig sensitiv | Nein | Nein | Anonymisierung (k-Anonymität, l-Diversität) |

**Auswahlüberlegungen**:

1. **Mit Datenklassifizierung beginnen**: Höhere Sensitivität erfordert stärkere Maskierung
2. **Regulatorische Anforderungen berücksichtigen**: DSGVO, PCI DSS v4.0.1, HIPAA haben spezifische Technikvorgaben
3. **Reversibilitätsbedarf beurteilen**: Legitimer Bedarf zur Originaldatenwiederherstellung bestimmt Technik
4. **Datennützlichkeit bewerten**: Maskierte Daten müssen für beabsichtigten Zweck nützlich sein
5. **Leistung berücksichtigen**: Echtzeit-DDM vs. Batch-SDM Leistungsauswirkungen
6. **Referenzielle Integrität validieren**: Tabellenübergreifende Beziehungen müssen nach Maskierung gültig bleiben

## A.3 Technikspezifische Anforderungen

### A.3.1 Statische Datenmaskierung (SDM)

**Verbindliche Anforderungen**:

- SDM muss vor Verlassen der Produktionsumgebung angewendet werden
- SDM muss referenzielle Integrität über verwandte Tabellen aufrechterhalten
- SDM muss Datenformat für Applikationskompatibilität erhalten
- SDM-Prozess muss wiederholbar sein (gleiche Eingabe erzeugt konsistente maskierte Ausgabe)
- Originaldaten dürfen aus der maskierten Ausgabe nicht wiederherstellbar sein

**Qualitätskriterien**:

- Maskierte Daten realistisch genug für Applikationstests
- Datenverteilung ähnlich wie in der Produktion (für Leistungstests)
- Edge Cases und Validierungsregeln mit maskierten Daten getestet

### A.3.2 Dynamische Datenmaskierung (DDM)

**Verbindliche Anforderungen**:

- DDM muss auf Datenbank- oder Applikationsebene durchgesetzt werden (nicht nur Client-seitig)
- DDM-Regeln müssen auf dokumentierten Benutzerrollen und Least-Privilege-Prinzip basieren
- DDM darf nicht durch Benutzer ohne geeignete Autorisierung umgangen werden
- DDM muss alle Zugriffe auf maskierte Felder zu Prüfzwecken protokollieren
- Leistungsauswirkungen müssen bewertet und innerhalb akzeptabler Grenzen liegen

**Qualitätskriterien**:

- Maskierungsregeln auf Geschäftszugangsanforderungen abgestimmt
- Bypass-Versuche erkannt und gemeldet
- Minimale Leistungsbeeinträchtigung (typisch <10%)

### A.3.3 Tokenisierung

**Verbindliche Anforderungen**:

- Token-Vault muss mit Zugangskontrolle und Verschlüsselung gesichert sein
- Tokens müssen bei Bedarf formaterhaltend sein (z.B. Kreditkartenformat)
- Token-zu-Wert-Zuordnung muss eins-zu-eins sein (deterministisch)
- Token-Vault muss separat mit angemessener Sicherheit gesichert werden
- De-Tokenisierung muss explizite Autorisierung erfordern und protokolliert werden

**Qualitätskriterien**:

- Vault-Verfügbarkeit entspricht betrieblichen Anforderungen
- Schlüsselmanagement für Vault-Verschlüsselung folgt Kryptografierichtlinie A.8.24
- Token-Kollisionsrisiko durch geeigneten Token-Raum minimiert

### A.3.4 Pseudonymisierung (DSGVO-Compliance)

**Verbindliche Anforderungen**:

- Pseudonymisierungsschlüssel müssen separat von pseudonymisierten Daten aufbewahrt werden
- Re-Identifizierung muss eine separate Autorisierung über den Datenzugang hinaus erfordern
- Pseudonymisierung muss bei DSGVO-Verwendung die DSGVO-Anforderungen erfüllen (Art. 32(1)(a), Art. 89)
- Pseudonymisierungstechnik muss durch den DSB auf DSGVO-Angemessenheit validiert werden
- Schlüsselmanagement muss Kryptografierichtlinie A.8.24 folgen

**Qualitätskriterien**:

- Pseudonyme über Datensätze hinweg konsistent (gleiche Person = gleiches Pseudonym)
- Re-Identifizierungsrisiko jährlich oder bei Datenstrukturänderungen bewertet
- Geeignet für beabsichtigten Zweck (Forschung, Statistik, berechtigtes Interesse)

### A.3.5 Anonymisierung (irreversibel)

**Verbindliche Anforderungen**:

- Anonymisierung muss irreversibel sein (keine Schlüssel oder Zuordnungen aufbewahrt)
- Re-Identifizierungsrisiko muss mit geeigneter Methodik bewertet werden (k-Anonymität, l-Diversität)
- Direkte Identifikatoren müssen entfernt oder verallgemeinert werden
- Quasi-Identifikatoren müssen auf Verknüpfungsrisiko geprüft werden
- Anonymisierung muss regulatorische Standards erfüllen, wenn für Compliance verwendet (DSGVO, HIPAA)

**Qualitätskriterien**:

- k-Anonymität ≥ 5 (Minimum) für DSGVO-konforme Anonymisierung
- l-Diversität für sensitive Merkmale berücksichtigt
- Verknüpfungsrisiko mit externen Datensätzen bewertet
- Datennützlichkeit für beabsichtigten Analysezweck aufrechterhalten

## A.4 Verbotene Techniken und Anti-Pattern

**Folgendes ist NICHT als Maskierungstechnik akzeptabel**:

| Verbotene Praxis | Begründung |
|------------------|-----------|
| **Einfache Zeichensubstitution** (A→1, B→2) | Trivial reversibel, vorhersagbares Muster |
| **ROT13 oder Caesar-Cipher** | Trivial reversibel, kryptografisch nicht sicher |
| **Nur reversible Kodierung** (Base64, URL-Encoding, Hex) | Keine Maskierung — nur Kodierung, einfach umkehrbar |
| **Selbst entworfene "Verschlüsselung"** | Nicht validierte Sicherheit, wahrscheinlich schwach, für Compliance nicht akzeptiert |
| **Nur Client-seitige Maskierung** (JavaScript, UI-Ebene) | Umgehbar — Daten bleiben im Backend nicht maskiert |
| **Nicht maskierte Produktionsdaten in nicht produktiver Umgebung** | Kernverletzung dieser Richtlinie |
| **Unbegrenzte Verwendung desselben maskierten Datensatzes ohne Aktualisierung** | Veraltete Daten, potenzielle Umgehung über Zeit |

**Begründung**: Diese Praktiken vermitteln den Anschein von Sicherheit ohne tatsächlichen Schutz und stellen „Sicherheitstheater" dar, das einer Prüfung nicht standhält.

## A.5 Technikvalidierung und -tests

Alle Maskierungstechniken müssen validiert werden auf:

1. **Wirksamkeit**: Originaldaten nicht wiederherstellbar (irreversible Techniken) oder nur mit autorisierten Schlüsseln (reversible Techniken)
2. **Formaterhaltung**: Datenformat entspricht dem Original, wo erforderlich
3. **Referenzielle Integrität**: Tabellenübergreifende Beziehungen aufrechterhalten
4. **Regulatorische Compliance**: Technik erfüllt Anforderungen für beabsichtigten Anwendungsfall
5. **Leistung**: Akzeptabler Overhead für betriebliche Anforderungen

**Validierungsverfahren**: Testmethodik dokumentiert in ISMS-IMP-A.8.11-4 (Test- und Validierungsrahmen).

**Technische Spezifikationen**: Detaillierte Technikspezifikationen, Algorithmusparameter und Konfigurationsanleitung in ISMS-CTX-A.8.11 (Technische Referenz Datenmaskierung, KEIN ISMS-Dokument).

---

# Anhang B: Ausnahmeantragsvorlage

**Zweck**: Standardisiertes Format zur Beantragung von Ausnahmen von Datenmaskierungsanforderungen gemäss Richtlinien-Abschnitt 3.3.

## Ausnahmeantrag

**Ausnahme-ID**: [AUTO-GENERIERT: EXC-A811-JJJJ-NNN]
**Antragsdatum**: [DD.MM.JJJJ]
**Beantragt von**: [Name, Titel, Abteilung]
**Dateneigentümer**: [Name, Titel] — muss diese Ausnahme genehmigen

---

## Ausnahmeumfang

**Betroffene Systeme**:

- [Alle betroffenen Systeme, Datenbanken und Applikationen auflisten]

**Betroffene Datenkategorien**:

- [Datenkategorien auflisten: PII, Finanzdaten, Gesundheitsdaten, Zugangsdaten, etc.]
- [Spezifizieren: Tabellennamen, Feldnamen, Datentypen]

**Umgebungen**:

- [ ] Produktion
- [ ] Test/QA
- [ ] Entwicklung
- [ ] Analyse/BI
- [ ] Training
- [ ] Sonstiges: [Angabe]

**Datenklassifizierung**:

- [ ] Eingeschränkt (Kritisch)
- [ ] Vertraulich (Hoch)
- [ ] INTERN (Mittel)

---

## Geschäftliche Begründung

**Warum ist Maskierung nicht durchführbar?**
[Detaillierte Erläuterung — technische, betriebliche oder geschäftliche Gründe]

**Geschäftliche Auswirkung bei Ablehnung der Ausnahme**:
[Betriebliche Auswirkungen, Geschäftsrisiko, Projektverzögerungen etc. beschreiben]

**Dauer der Notwendigkeit**:

- Ausnahme-Startdatum: [DD.MM.JJJJ]
- Ausnahme-Enddatum: [DD.MM.JJJJ] (Maximum: 12 Monate; kürzer bei hoher Sensitivität)
- Weg zur Compliance: [Plan zur Erreichung vollständiger Maskierungs-Compliance beschreiben]

---

## Risikobeurteilung

**Inhärentes Risiko (ohne Maskierung)**:

- Expositionswahrscheinlichkeit: [ ] Niedrig [ ] Mittel [ ] Hoch [ ] Kritisch
- Auswirkung bei Offenlegung: [ ] Niedrig [ ] Mittel [ ] Hoch [ ] Kritisch
- Inhärenter Risikowert: [Wahrscheinlichkeit × Auswirkung]

**Bedrohungsszenarien**:
[Spezifische Bedrohungen durch nicht maskierte Daten in dieser Umgebung auflisten]

**Compliance-Auswirkung**:
[Regulatorische Implikationen beschreiben: DSGVO, PCI DSS v4.0.1, HIPAA, nDSG etc.]

---

## Kompensierende Massnahmen

**Implementierte alternative Schutzmassnahmen**:
[Steuerungen beschreiben, die das Risiko nicht maskierter Daten teilweise mindern]

Beispiele:

- [ ] Verstärkte Zugangskontrolle (Rollen mit Zugang auflisten)
- [ ] Netzwerksegmentierung (Isolation beschreiben)
- [ ] Verstärkte Überwachung und Alarmierung (Protokollierung beschreiben)
- [ ] Datenverschlüsselung bei Ruhezustand und Transit
- [ ] Zeitlich befristeter Zugang (Dauer und Begründung beschreiben)
- [ ] Zusätzliche Prüfprotokollierung (Protokolliertes beschreiben)
- [ ] Nutzerschulung und Bestätigung der akzeptablen Verwendung
- [ ] Datenminimierung (reduzierter Datensatzumfang/Spalten)
- [ ] Sonstiges: [Angabe]

**Wirksamkeit kompensierender Massnahmen**:

- Geschätzte Risikominderung: [Prozentsatz oder qualitative Beurteilung]
- Restrisikobewertung: [Reduziertes Risiko nach kompensierenden Massnahmen]

---

## Überwachung und Compliance

**Überwachungsanforderungen**:
[Wie wird die Einhaltung der Ausnahmebedingungen verifiziert?]

**Überprüfungsplan**:

- [ ] Monatlich (bei kritischer Sensitivität)
- [ ] Quartalsweise (bei hoher Sensitivität)
- [ ] Halbjährlich (bei mittlerer Sensitivität)

**Widerrufsbedingungen**:
[Unter welchen Bedingungen wird diese Ausnahme widerrufen?]

Beispiele:

- Ausfall kompensierender Massnahmen
- Sicherheitsvorfall im Zusammenhang mit nicht maskierten Daten
- Geschäftliche Begründung nicht mehr gültig
- Maskierungslösung verfügbar
- Ausnahmefrist abgelaufen

---

## Genehmigungen

**Genehmigung Dateneigentümer**:

- Name: [Name des Dateneigentümers]
- Unterschrift: ________________
- Datum: [DD.MM.JJJJ]
- Kommentare: [Optional]

**Überprüfung Sicherheitsteam**:

- Prüfer: [Name des Sicherheitsteam-Leiters]
- Risikobeurteilung: [ ] Akzeptabel [ ] Nicht akzeptabel
- Unterschrift: ________________
- Datum: [DD.MM.JJJJ]
- Kommentare/Bedingungen: [Erforderlich bei Genehmigung]

**ISB-Genehmigung** (erforderlich bei hoher/kritischer Sensitivität):

- Name: [ISB Name]
- [ ] Genehmigt [ ] Abgelehnt
- Unterschrift: ________________
- Datum: [DD.MM.JJJJ]
- Bedingungen: [Besondere Genehmigungsbedingungen]

**Genehmigung Geschäftsleitung** (erforderlich bei Produktionsausnahmen):

- Name: [Name der Führungskraft]
- [ ] Genehmigt [ ] Abgelehnt
- Unterschrift: ________________
- Datum: [DD.MM.JJJJ]

---

## Ausnahmeverfolgung

**Ausnahmestatus**:

- [ ] Genehmigung ausstehend
- [ ] Genehmigt
- [ ] Abgelehnt
- [ ] Abgelaufen
- [ ] Widerrufen

**Ausnahme-Überprüfungsprotokoll**:

| Überprüfungsdatum | Prüfer | Status | Kommentare | Nächste Überprüfung |
|-------------------|--------|--------|-----------|---------------------|
| | | | | |

**Ausnahmeabschluss**:

- Abschlussdatum: [DD.MM.JJJJ]
- Grund: [ ] Abgelaufen [ ] Widerrufen [ ] Maskierung implementiert [ ] Sonstiges
- Abschliessende Kommentare: [Erkenntnisse, implementierte Verbesserungen]

---

**Ausnahmedokumentation**: Alle genehmigten Ausnahmen werden im Ausnahmeregister (ISMS-IMP-A.8.11-3 Beurteilung der Umgebungsabdeckung) geführt.

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Datenschutzbeauftragter (DSB)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen fest. Implementierungsverfahren sind in ISMS-IMP-A.8.11 (UG/TG) dokumentiert. Technische Referenzinformationen sind in ISMS-CTX-A.8.11 (KEIN ISMS-Dokument) bereitgestellt.*

<!-- QA_VERIFIED: 2026-03-28 -->
