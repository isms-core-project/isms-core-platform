<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.7-DE:framework:POL:a.5.7 -->
**ISMS-POL-A.5.7 — Bedrohungsintelligenz**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie zur Bedrohungsintelligenz |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.7 |
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
| 1.0 | [Datum festzulegen] | ISB | Erstversion für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Inkrafttreten + 12 Monate]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Risiko: Chief Risk Officer (CRO)
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.5.7.1-UG/TG (Bewertung der Quellen für Bedrohungsintelligenz)
- ISMS-IMP-A.5.7.2-UG/TG (Bewertung der Sammlung und Analyse von Geheimdienstinformationen)
- ISMS-IMP-A.5.7.3-UG/TG (Bewertung der Integration und Verteilung von Geheimdienstinformationen)
- ISO/IEC 27001:2022 Kontrolle A.5.7

---

# Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] an Bedrohungsintelligenz fest, um eine proaktive Verteidigung zu ermöglichen, das Risikomanagement zu informieren und die Sicherheitsoperationen gemäss ISO/IEC 27001:2022 Kontrolle A.5.7 zu verbessern.

**Zweck**: Definition der organisatorischen Anforderungen an die Governance der Bedrohungsintelligenz. Diese Richtlinie legt fest, WELCHE Fähigkeiten zur Bedrohungsintelligenz erforderlich sind und WER dafür rechenschaftspflichtig ist. Implementierungsverfahren (WIE) sind gesondert in ISMS-IMP-A.5.7 (UG/TG-Varianten) dokumentiert.

**Geltungsbereich**: Diese Richtlinie gilt für:

- Alle Aktivitäten zur Bedrohungsintelligenz (Sammlung, Analyse, Produktion, Verbreitung)
- Alle Geheimdiensttypen (strategisch, taktisch, operativ)
- Alle Geheimdienstquellen (kommerzielle Plattformen, OSINT, staatliche Feeds, interne Telemetrie)
- Alle Mitarbeitenden von [Organisation], die an Sicherheitsoperationen beteiligt sind
- Alle Sicherheitswerkzeuge mit Integration von Bedrohungsintelligenz

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert obligatorische Compliance-Anforderungen gemäss ISMS-POL-00, einschliesslich Schweizerisches nDSG, EU GDPR und ISO/IEC 27001:2022. Sektorspezifische Anforderungen (PCI DSS v4.0.1, FINMA, DORA, NIS2) gelten, sofern die Geschäftstätigkeiten von [Organisation] die Anwendbarkeit auslösen.

---

# Geltungsbereich

## ISO/IEC 27001:2022 Kontrolle A.5.7

**ISO/IEC 27001:2022 Anhang A.5.7 — Bedrohungsintelligenz**

> *Informationen über Informationssicherheitsbedrohungen sollten gesammelt und analysiert werden, um Bedrohungsintelligenz zu erzeugen.*

**Kontrollziel**: Aufstellung organisatorischer Richtlinien für Bedrohungsintelligenz-Kontrollen, die eine proaktive Bedrohungserkennung ermöglichen, Risikomanagemententscheidungen informieren, Sicherheitsinvestitionen priorisieren und die Wirksamkeit der Incident Response verbessern.

## Richtliniengrenzen

**Diese Richtlinie regelt** (WAS/WER):

- Anforderungen an die Sammlung von Bedrohungsintelligenz aus mehreren Quellentypen
- Anforderungen an die Analyse und Produktion von Geheimdienstinformationen
- Anforderungen an die Verbreitung von Geheimdienstinformationen an Stakeholder
- Integrationsanforderungen mit der Risikobewertung (ISO 27001 Klausel 6.1)
- Integrationsanforderungen mit dem Incident-Management (Kontrollen A.5.24-5.28)
- Organisatorische Rollen und Verantwortlichkeiten
- Ausnahmen und Governance-Rahmenbedingungen

**Diese Richtlinie regelt NICHT** (WIE — siehe ISMS-IMP-A.5.7):

- Technische Implementierungsdetails und Plattformkonfiguration
- Spezifische Tools für Bedrohungsintelligenz oder Lieferantenauswahl
- Detaillierte Analyse-Frameworks und Analysten-Verfahren
- Spezifische KPI-Messmethodiken
- IOC-Deployment-Verfahren
- Kriterien für die Quellenbewertung

## Organisatorischer Abdeckungsbereich

**Im Geltungsbereich**:

- Alle Mitarbeitenden (fest, befristet, Auftragnehmer)
- Alle Sicherheitsoperations- und Incident-Response-Teams
- Alle Risikomanagement- und Compliance-Funktionen
- Drittanbieter mit Zugang zu Bedrohungsintelligenz
- Alle Standorte und Geschäftsbereiche von [Organisation]

**Nicht im Geltungsbereich**:

- Offensive Cyberoperationen oder Vergeltungsmassnahmen (verboten)
- Strafverfolgungsermittlungen (Zusammenarbeit unterstützt, aber nicht selbst durchgeführt)
- Schwachstellenscanning und Penetrationstests (geregelt durch Kontrolle A.8.8)
- Bedrohungsjagd-Operationen (geregelt durch Kontrolle A.8.16)

---

# Richtlinienaussagen

## Sammlung von Bedrohungsintelligenz

[Organisation] MUSS die Sammlung von Bedrohungsintelligenz aus mehreren Quellenkategorien implementieren, um eine umfassende Bedrohungssichtbarkeit zu gewährleisten.

**Erforderliche Quellenkategorien**:

- **Kommerzielle Plattformen**: Kuratierte Bedrohungsintelligenz-Feeds mit Validierung
- **Open-Source Intelligence (OSINT)**: Öffentliche Bedrohungsdaten, Schwachstellendatenbanken
- **Staatliche/CERT-Feeds**: Nationale CERT-Warnungen, Alarme für kritische Infrastrukturen
- **Branchenübergreifender Austausch (ISAC/ISAO)**: Sektorspezifische Bedrohungen und Peer-Zusammenarbeit (empfohlen)
- **Interne Telemetrie**: Warnungen von Sicherheitswerkzeugen, Vorfallsdaten, forensische Erkenntnisse

**Anforderungen an das Quellenmanagement**:

- Alle Quellen MÜSSEN vor der Inbetriebnahme auf Zuverlässigkeit und Glaubwürdigkeit geprüft werden
- Quellen MÜSSEN regelmässig auf Genauigkeit und Leistung validiert werden
- Datenschutzanforderungen MÜSSEN auf alle gesammelten Geheimdienstinformationen angewendet werden
- Externe Weitergabe MUSS durch Traffic Light Protocol (TLP)-Klassifizierungen geregelt werden

**Implementierungsreferenz**: Quelleninventar und Bewertungskriterien dokumentiert in ISMS-IMP-A.5.7.1.

## Analyse und Produktion von Bedrohungsintelligenz

[Organisation] MUSS eine strukturierte Geheimdienstanalyse implementieren, um Rohdaten über Bedrohungen in handlungsrelevante Informationen umzuwandeln.

**Anforderungen an die Geheimdienstproduktion**:

**Strategische Informationen** (für Geschäftsleitung):

- Bewertungen der Bedrohungslandschaft und Trendanalysen
- Risikobasierte Empfehlungen für Sicherheitsinvestitionen
- Mindestens quartalsweise produziert oder durch bedeutende Ereignisse ausgelöst

**Taktische Informationen** (für Sicherheitsoperationen):

- Profile von Bedrohungsakteuren und TTPs
- Kampagnenanalyse und Angriffsmuster
- Mindestens monatlich produziert oder durch aufkommende Bedrohungen ausgelöst

**Operative Informationen** (für technisches Personal):

- Indikatoren für Kompromittierungen (IOCs) zur Erkennung
- Malware-Signaturen und Verhaltensindikatoren
- Kontinuierlich über automatisierte Feeds produziert, mit täglicher Analysten-Überprüfung

**Qualitätsanforderungen**:

- Alle Geheimdienstprodukte MÜSSEN Quellen mit Zuverlässigkeitsbewertung zitieren
- Geheimdienstinformationen MÜSSEN nach Möglichkeit durch mehrere Quellen validiert werden
- Geheimdienstinformationen MÜSSEN mit dem Bedrohungsmodell und den Vermögenswerten von [Organisation] verknüpft werden
- Geheimdienstinformationen MÜSSEN handlungsrelevante Empfehlungen oder Erkennungsanleitungen enthalten
- Geheimdienstinformationen MÜSSEN mithilfe von TLP und internen Klassifizierungsschemata eingestuft werden

**Implementierungsreferenz**: Analyse-Frameworks und Produktionsmetriken dokumentiert in ISMS-IMP-A.5.7.2.

## Verbreitung von Bedrohungsintelligenz

[Organisation] MUSS eine strukturierte Verbreitung von Geheimdienstinformationen implementieren, die sicherstellt, dass die richtigen Informationen die richtigen Stakeholder erreichen.

**Anforderungen an die Verbreitung**:

- Die Geschäftsleitung MUSS strategische Bedrohungsbewertungen erhalten
- Der Sicherheitsbetrieb MUSS operative IOCs und taktische TTPs erhalten
- Das Incident-Response-Team MUSS ermittlungsrelevante Geheimdienstinformationen erhalten
- Das Risikomanagement MUSS Bedrohungsdaten für Risikobeurteilungsaktualisierungen erhalten
- IT-Betrieb MUSS infrastrukturrelevante Blockierungsanleitungen erhalten

**Austauschkontrollen**:

- Externe Weitergabe MUSS durch Traffic Light Protocol (TLP) geregelt werden
- Konsumenten von Geheimdienstinformationen MÜSSEN Feedback zur Wirksamkeit der Informationen geben
- Bidirektionale Feedback-Schleifen MÜSSEN zwischen Konsumenten und Produzenten eingerichtet werden

**Implementierungsreferenz**: Verbreitungs-Tracking und Stakeholder-Engagement dokumentiert in ISMS-IMP-A.5.7.3.

## Integration in die Risikobewertung (OBLIGATORISCH)

Bedrohungsintelligenz MUSS den Risikobewertungsprozess von [Organisation] gemäss ISO 27001:2022 Klausel 6.1 informieren.

**Integrationsanforderungen**:

- Erkenntnisse aus der Bedrohungsintelligenz MÜSSEN Wahrscheinlichkeitsschätzungen für Sicherheitsrisiken informieren
- Aufkommende Bedrohungskampagnen MÜSSEN eine Neubewertung des Risikos auslösen, wenn sie den Sektor von [Organisation] ins Visier nehmen
- Geheimdienstinformationen über die Ausnutzung von Schwachstellen MÜSSEN Auswirkungsbewertungen informieren
- Empfehlungen aus der Bedrohungsintelligenz MÜSSEN die Auswahl und Priorisierung von Kontrollen informieren
- Risikoregister-Aktualisierungen MÜSSEN auf unterstützende Bedrohungsintelligenz-Berichte verweisen

**Dokumentationsanforderungen**:

- Jede Risikobeurteilungsaktualisierung MUSS die Quelle der Bedrohungsintelligenz dokumentieren
- Die Nachvollziehbarkeit zwischen Bedrohungsintelligenz-Berichten und Risikoregistereinträgen MUSS gewährleistet werden

**Implementierungsreferenz**: Integration-Tracking des Risikos dokumentiert in ISMS-IMP-A.5.7.3.

## Integration in das Incident-Management (OBLIGATORISCH)

Bedrohungsintelligenz MUSS die Vorfallserkennung, -untersuchung und -reaktion gemäss Kontrollen A.5.24-5.28 verbessern.

**Integrationsanforderungen**:

- IOCs aus der Bedrohungsintelligenz MÜSSEN in Erkennungswerkzeugen bereitgestellt werden
- TTPs von Bedrohungsakteuren MÜSSEN in Erkennungsregeln übersetzt werden
- Bedrohungsintelligenz MUSS bei Vorfallsuntersuchungen Kontext liefern
- Vorfallserkenntnisse MÜSSEN zur internen Sammlung von Bedrohungsintelligenz beitragen
- Nachbesprechungen nach Vorfällen MÜSSEN die Wirksamkeit der Bedrohungsintelligenz validieren

**Implementierungsreferenz**: Incident-TI-Integrations-Tracking dokumentiert in ISMS-IMP-A.5.7.3.

## Integration in das Schwachstellenmanagement (OPTIONAL)

Wenn [Organisation] Kontrolle A.8.8 (Management technischer Schwachstellen) implementiert, ist die Integration von Bedrohungsintelligenz OPTIONAL, wird jedoch empfohlen.

**Bei Implementierung**:

- Schwachstelleninformationen MÜSSEN CVE-Daten mit dem Ausnutzungsstatus kombinieren
- Geheimdienstinformationen über aktive Ausnutzung MÜSSEN die Priorisierung der Behebung informieren
- CVSS-Werte kombiniert mit Bedrohungsintelligenz MÜSSEN eine risikobasierte Priorisierung ermöglichen

**Implementierungsreferenz**: Bei Implementierung wird die VulnerabilityThreatLink-Integration in ISMS-IMP-A.5.7.2 und ISMS-IMP-A.8.8 dokumentiert.

## Messung der Wirksamkeit

[Organisation] MUSS die Wirksamkeit des Bedrohungsintelligenz-Programms durch objektive Metriken messen.

**Erforderliche Messbereiche**:

- Durch Bedrohungsintelligenz ausgelöste Risikobeurteilungsaktualisierungen
- Durch Bedrohungsintelligenz verhinderte oder erkannte Vorfälle
- Quellengenauigkeit und -leistung
- Anreicherung von Vorfallsuntersuchungen mit Bedrohungsintelligenz
- Durch Bedrohungsintelligenz informierte Sicherheitsentscheidungen
- Zufriedenheit der Stakeholder mit den Geheimdienstprodukten

**Programm-Reife**:

- [Organisation] MUSS die Reife des Bedrohungsintelligenz-Programms jährlich bewerten
- Die Bewertung MUSS Sammlung, Analyse, Verbreitung, Operationalisierung und Governance abdecken

**Implementierungsreferenz**: Wirksamkeitsmetriken und KPI-Tracking dokumentiert im Summary Dashboard.

---

# Rollen und Verantwortlichkeiten

## Verantwortlichkeitsmatrix

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Geschäftsleitung** | Strategische Genehmigung, Ressourcenzuweisung, Richtliniengenehmigung |
| **Informationssicherheitsbeauftragter (ISB)** | Richtlinieneigentümerschaft, Programmaufsicht, Ausnahmengenehmigung |
| **Chief Risk Officer (CRO)** | Integration der Risikobewertung, Genehmigung von TI-gesteuerten Risikoaktualisierungen |
| **Teamleiter Bedrohungsintelligenz** | Programmmanagement, Geheimdienstproduktion, Quellenmanagement |
| **Bedrohungsintelligenz-Analysten** | Sammlung, Analyse, Produktion, Qualitätssicherung |
| **Sicherheitsoperationen (SOC)** | Operationalisierung der Informationen, IOC-Deployment, Optimierung der Erkennung |
| **Incident-Response-Team** | Anwendung von Informationen bei Untersuchungen, IOC-Extraktion |
| **IT-Betrieb** | Technische Implementierung TI-gesteuerter Kontrollen |
| **Risikomanagement-Team** | Risikobeurteilungsaktualisierungen auf Basis von Bedrohungsintelligenz |
| **Compliance/Rechts** | Regulatorische Interpretation, Datenschutz-Compliance |
| **Alle Mitarbeitenden** | Bedrohungsbewusstsein, Meldung verdächtiger Aktivitäten |

## Eskalationspfad

- Operative Probleme: Analyst → Teamleiter TI → Sicherheitsteam → ISB
- Technische Ausnahmen: Teamleiter TI → Sicherheitsteam → ISB
- Compliance-Bedenken: Teamleiter TI → Compliance → ISB → Geschäftsleitung
- Risikobezogene Themen: Teamleiter TI → CRO → ISB → Geschäftsleitung
- Sicherheitsvorfälle: Alle → SOC → Incident Response → ISB

## Schulungsanforderungen

- **Alle Mitarbeitenden**: Jährliches Sicherheitsbewusstseinstraining mit Überblick über die Bedrohungslandschaft
- **TI-Analysten**: Spezialisiertes Training zu Analyse-Frameworks und Berichtserstellung
- **SOC-Personal**: Training zur Operationalisierung von Bedrohungsintelligenz und zum IOC-Deployment
- **Sicherheitsführung**: Strategische Briefings zur Bedrohungsintelligenz

## Business Continuity

[Organisation] MUSS die Kontinuität kritischer Bedrohungsintelligenz-Fähigkeiten sicherstellen:

- Primäre und Ersatz-Analysten für jede Geheimdienstfunktion designiert
- Quellenredundanz für kritische Geheimdienstkategorien
- Dokumentierte Failover-Verfahren für die Bedrohungsintelligenz-Plattform
- Jährliche Business-Continuity-Tests für Bedrohungsintelligenz-Operationen

---

# Compliance und Ausnahmen

## Regulatorische Anwendbarkeit

**Stufe 1: Obligatorische Compliance**

| Regulierung | Wesentliche Anforderungen |
|-------------|--------------------------|
| **Schweizerisches nDSG** | Art. 8 — Technische und organisatorische Massnahmen zur Bedrohungserkennung |
| **EU GDPR** | Art. 32 — Sicherheitsmassnahmen einschliesslich Bedrohungsüberwachung |
| **ISO/IEC 27001:2022** | Kontrolle A.5.7 — Sammlung und Analyse von Bedrohungsintelligenz |

**Stufe 2: Bedingte Anwendbarkeit** (gemäss ISMS-POL-00)

| Regulierung | Auslösebedingung |
|-------------|----------------|
| **FINMA** | Schweizerisches reguliertes Finanzinstitut |
| **DORA** | EU-Finanzdienstleistungsunternehmen |
| **NIS2** | Wesentliche/wichtige Einrichtung (EU) |

**Compliance-Bestimmung**: [Organisation] ermittelt anwendbare Stufe-2-Vorschriften durch periodische Bewertung der Geschäftstätigkeiten. Bei Überlappung mehrerer Vorschriften gelten die strengsten Anforderungen.

## Ausnahmenmanagement

Ausnahmen von Anforderungen der Bedrohungsintelligenz erfordern eine dokumentierte geschäftliche Begründung, Risikobewertung und formelle Genehmigung.

**Ausnahmetypen**:

- Quellenabdeckungsausnahmen (Budgetbeschränkungen)
- Integrationsfristen-Ausnahmen (technische Komplexität)
- Ressourcenausnahmen (unzureichende Personalausstattung)
- KPI-Zielausnahmen (neu implementiertes Programm)

**Ausnahmeanforderungen**:

- Zeitlich begrenzt mit expliziten Ablaufdaten
- Kompensierende Kontrollen dokumentiert und verifiziert
- Quartalsweise Überprüfung der Ausnahmenotwendigkeit
- Nachweis des Fortschritts in Richtung vollständiger Compliance

**Genehmigungsbefugnis**:

- ISB: Quellen-, Integrations- und KPI-Ausnahmen
- ISB + Geschäftsleitung: Ressourcenausnahmen

**Dokumentation**: Ausnahmeanträge und Genehmigungen im Ausnahmenregister geführt.

## Integration der Incident Response

Wenn Bedrohungsintelligenz unmittelbare oder aktive Bedrohungen identifiziert, gelten die Incident-Response-Verfahren gemäss Kontrollen A.5.24-5.28.

**Schweregrad-basierte Reaktion**:

- Kritische/Hohe Schweregrad-Erkenntnisse: Sofortige Eskalation an SOC und Incident Response
- Mittlere/Niedrige Schweregrad-Erkenntnisse: Standardmässiger Verbreitungsprozess für Geheimdienstinformationen
- Notfallbriefings: ISB wird gemäss Vorfallsklassifizierung informiert

**Koordinationsanforderungen**:

- Das Bedrohungsintelligenz-Team unterstützt Vorfallsuntersuchungen
- Das Incident-Response-Team extrahiert IOCs für den Informationsaustausch
- Nachbesprechungen nach Vorfällen bewerten die Wirksamkeit der Bedrohungsintelligenz

---

# Richtlinien-Governance

## Richtlinienüberprüfung

- **Häufigkeit**: Mindestens jährlich
- **Auslöser**: Regulatorische Änderungen, grössere Vorfälle, bedeutende Änderungen der Bedrohungslandschaft, organisatorische Änderungen, Prüfungsergebnisse
- **Überprüfer**: ISB, Teamleiter TI, Sicherheitsteam, Risikomanagement, Compliance
- **Genehmigung**: ISB (technisch), Geschäftsleitung (strategisch)

## Richtlinienaktualisierungen

- **Geringfügig** (Klarstellungen, Referenzen): ISB-Genehmigung, Kommunikation innerhalb von 30 Tagen
- **Wesentlich** (Änderungen des Geltungsbereichs, neue Anforderungen): Vollständige Genehmigungskette
- **Notfall** (kritische Bedrohungen): ISB-Genehmigung, sofortige Kommunikation

## Implementierungsstandards

Aktualisierungen des Implementierungsstandards (ISMS-IMP-A.5.7) erfordern keine Richtlinienrevision. Der Implementierungsleitfaden wird vom Sicherheitsteam quartalsweise mit ISB-Genehmigung überprüft.

---

# Verwandte Dokumente

## ISMS-Integration

Diese Richtlinie ist in das Informationssicherheits-Managementsystem von [Organisation] integriert:

- **Risikobewertung** (Klausel 6.1): Bedrohungsintelligenz informiert Risikoidentifizierung und -analyse
- **Erklärung zur Anwendbarkeit** (Klausel 6.1.3): Anwendbarkeit von Kontrolle A.5.7 dokumentiert
- **Interne Revision** (Klausel 9.2): Bedrohungsintelligenz-Programm im ISMS-Prüfungsumfang einbezogen
- **Kontinuierliche Verbesserung** (Klausel 10): Metriken tragen zur ISMS-Leistungsbewertung bei

## Verwandte Kontrollen

| Kontrolle | Integrationstyp | Beschreibung |
|-----------|-----------------|--------------|
| **A.5.24-5.28** | OBLIGATORISCH | Incident-Management — TI verbessert Erkennung und Reaktion |
| **A.8.16** | OBLIGATORISCH | Überwachungsaktivitäten — TI liefert Erkennungskontext |
| **A.8.8** | OPTIONAL | Schwachstellenmanagement — TI priorisiert Behebung |
| **A.5.19-5.22** | OPTIONAL | Lieferantensicherheit — TI bewertet Drittparteienrisiken |
| **A.5.23** | OPTIONAL | Cloud-Sicherheit — TI deckt cloudspezifische Bedrohungen ab |
| **A.8.23** | OPTIONAL | Web-Filterung — TI liefert Feeds mit bösartigen Domains |

## Implementierungsressourcen

- **ISMS-IMP-A.5.7.1-UG/TG**: Bewertung der Quellen für Bedrohungsintelligenz
- **ISMS-IMP-A.5.7.2-UG/TG**: Bewertung der Sammlung und Analyse von Geheimdienstinformationen
- **ISMS-IMP-A.5.7.3-UG/TG**: Bewertung der Integration und Verteilung von Geheimdienstinformationen

---

# Begriffsbestimmungen

**Bedrohungsintelligenz (Threat Intelligence)**: Sammlung, Analyse und Verbreitung von Informationen über aktuelle oder aufkommende Bedrohungen, die eine proaktive Verteidigung und informierte Sicherheitsentscheidungen ermöglichen.

**Strategische Informationen (Strategic Intelligence)**: Hochrangige Informationen, die breite Bedrohungen und Trends adressieren und Entscheidungen der Führungsebene sowie die langfristige Strategie unterstützen.

**Taktische Informationen (Tactical Intelligence)**: Informationen, die Taktiken, Techniken und Verfahren (TTPs) von Angreifern beschreiben und Sicherheitsoperationen sowie Verteidigungsplanung unterstützen.

**Operative Informationen (Operational Intelligence)**: Handlungsrelevante technische Informationen einschliesslich IOCs und Erkennungsregeln, die unmittelbare Sicherheitsoperationen unterstützen.

**Indikator für Kompromittierung (Indicator of Compromise, IOC)**: Beobachtbares Artefakt, das auf eine stattgefundene oder laufende Sicherheitsverletzung hindeutet (IP-Adressen, Domains, Datei-Hashes).

**Taktiken, Techniken und Verfahren (Tactics, Techniques, and Procedures, TTPs)**: Aktivitätsmuster von Bedrohungsakteuren, dokumentiert in Frameworks wie MITRE ATT&CK.

**Traffic Light Protocol (TLP)**: Standard für den Informationsaustausch, der Farbcodes (ROT, AMBER, AMBER+STRICT, GRÜN, KLAR) verwendet, um Weitergabebeschränkungen anzuzeigen.

**CVSS (Common Vulnerability Scoring System)**: Standard zur Bewertung der Schwere von Schwachstellen (0.0–10.0). CVSS 4.0 ist der aktuelle Standard; CVSS 3.1 bleibt weit verbreitet.

**Bedrohungsakteur (Threat Actor)**: Einzelperson, Gruppe oder Organisation, die bösartige Cyberaktivitäten durchführt.

---

# Nachweise für diese Richtlinie

**Stage 1 (Dokumentationsprüfung) Nachweise:**

Erforderliche Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.7 v1.0)
- ✅ Genehmigungsunterschriften von ISB und Geschäftsleitung
- ✅ Governance-Rahmen für Bedrohungsintelligenz definiert (Abschnitt 2.1)
- ✅ Quellentypen und Sammlungsanforderungen dokumentiert (Abschnitt 2.2)
- ✅ Analyse- und Produktionsanforderungen spezifiziert (Abschnitt 2.3)
- ✅ Verbreitungs- und Stakeholder-Anforderungen dokumentiert (Abschnitt 2.4)
- ✅ Integrationsanforderungen der Risikobewertung definiert (Abschnitt 2.5)
- ✅ Integrationsanforderungen des Incident-Managements spezifiziert (Abschnitt 2.6)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Abschnitt 3)
- ✅ Governance und Ausnahmeverfahren definiert (Abschnitt 3.6)
- ✅ Integration mit verwandten Kontrollen dokumentiert (Abschnitt 4.1)

**Stage 2 (Operative Wirksamkeit) Nachweise:**

Erforderliche Nachweise, die belegen, dass diese Richtlinie operativ wirksam ist:

- Abgeschlossene Bewertungen der Bedrohungsintelligenzquellen gemäss ISMS-IMP-A.5.7.1 (Quelleninventar, Admiralty-Code-Bewertungen, Leistungsvalidierung)
- Informationssammlungs- und Analysebewertungen gemäss ISMS-IMP-A.5.7.2 (Abdeckungsanalyse, MITRE ATT&CK-Mapping, Produktionsmetriken)
- Integrations- und Verbreitungsbewertungen gemäss ISMS-IMP-A.5.7.3 (Werkzeug-Integrationsstatus, IOC-Deployment, Stakeholder-Engagement)
- Durch Bedrohungsintelligenz ausgelöste Risikobeurteilungsaktualisierungen (≥3 Beispiele pro Quartal mit Nachvollziehbarkeit)
- Dokumentation verhinderte Vorfälle (≥3 Beispiele pro Quartal mit Validierungsnachweisen)
- Quellenleistungs-Validierungsberichte (quartalsweise, ≥85 % Genauigkeitsrate)
- Vorfallsanreicherungsnachweise (≥70 % der P1/P2-Vorfälle mit Bedrohungsintelligenz-Kontext)
- TI-gesteuerte Sicherheitsentscheidungen (≥5 Beispiele pro Quartal mit dokumentierten Ergebnissen)
- Betriebsprotokolle und Nutzungsmetriken der Bedrohungsintelligenz-Plattform
- Verteilte strategische, taktische und operative Geheimdienstberichte an Stakeholder
- Informationsaustausch-Vereinbarungen zu Bedrohungsintelligenz (sofern zutreffend)
- Ergebnisse der Business-Continuity-Tests für das Bedrohungsintelligenz-Programm (jährlich)
- Ausnahmegenehmigungen für Abweichungen bei der Bedrohungsintelligenz (falls zutreffend)
- Schulungsabschlussnachweise für Personal im Bereich Bedrohungsintelligenz
- Wirksamkeitsmetriken in Summary Dashboards nachverfolgt

**Klarstellung zu Compliance-Nachweisen:**

Diese Richtlinie legt den Governance-Rahmen für Bedrohungsintelligenz fest (Anforderungen an Sammlung, Analyse, Produktion und Verbreitung). Sie legt NICHT fest:

- **Technische Erkennungskontrollen** (adressiert in A.8.16 Überwachungsaktivitäten — Bedrohungsintelligenz liefert Kontext für Erkennungsregeln)
- **Incident-Response-Verfahren** (adressiert in A.5.24-5.28 Incident-Management — Bedrohungsintelligenz verbessert Untersuchungen)
- **Schwachstellenpriorisierung** (adressiert in A.8.8 Schwachstellenmanagement — VulnerabilityThreatLink-Integration ist optional)
- **Spezifische Bedrohungsakteur-Profile** (operativer Geheimdienst in der Bedrohungsintelligenz-Plattform geführt, nicht in der Richtlinie)
- **Werkzeugauswahl oder Plattformkonfiguration** (Implementierungsentscheidungen auf Basis organisatorischer Anforderungen)

Die Abgrenzung: POL-A.5.7 definiert den Governance-Rahmen für Bedrohungsintelligenz-Fähigkeiten → ISMS-IMP-A.5.7-Paket stellt Bewertungsverfahren bereit → Bedrohungsintelligenz-Plattform implementiert technische Sammlung/Analyse → Andere Kontrollen (A.8.16, A.5.24-28, A.8.8) nutzen Outputs der Bedrohungsintelligenz für ihre jeweiligen Zwecke.

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Datum festzulegen] |
| **IT-Leiter (ITL)** | [Name] | [Datum festzulegen] |
| **Chief Risk Officer (CRO)** | [Name] | [Datum festzulegen] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Datum festzulegen] |
| **Geschäftsleitung** | [Name] | [Datum festzulegen] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die Anforderungen an Bedrohungsintelligenz fest. Implementierungsverfahren sind in ISMS-IMP-A.5.7 (UG/TG) dokumentiert.*

<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.7-DE:framework:POL:a.5.7 -->

<!-- QA_VERIFIED: 2026-03-28 -->
