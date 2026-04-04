<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.24-28-DE:framework:POL:a.5.24-28 -->
**ISMS-POL-A.5.24-28 — Incident-Management-Lebenszyklus**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Incident-Management-Lebenszyklus |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.24-28 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstrichtlinie für ISO 27001:2022 Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Inkrafttreten + 12 Monate]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Fachlich: Incident-Response-Manager / CSIRT-Leitung
- Rechtlich: Rechts-/Compliance-Beauftragter
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-REF-A.5.24-28 (Incident-Response-Referenzleitfaden)
- ISMS-IMP-A.5.24-28.-UG/TGS1 bis S5 (Implementierungsbewertungen)
- ISO/IEC 27001:2022 Massnahmen A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
- ISMS-POL-A.8.15 (Protokollierung)
- ISMS-POL-A.8.16 (Überwachungsaktivitäten)
- ISMS-POL-A.6.8 (Meldung von Informationssicherheitsereignissen)
- ISMS-POL-A.5.29-30 (Betriebskontinuität & Notfallwiederherstellung)
- ISMS-POL-A.5.31 (Gesetzliche, behördliche, regulatorische und vertragliche Anforderungen)

---

# Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für die Bewirtschaftung von Informationssicherheitsvorfällen über ihren vollständigen Lebenszyklus gemäss ISO/IEC 27001:2022 Massnahmen A.5.24 bis A.5.28 fest.

**Zweck**: Organisatorische Anforderungen für die Umsetzung und Steuerung des Incident-Managements definieren. Diese Richtlinie legt fest, WELCHE Incident-Management-Fähigkeiten erforderlich sind, WER verantwortlich ist und WANN Massnahmen zu ergreifen sind. Umsetzungsverfahren (WIE Incident Response durchgeführt wird) sind separat in den ISMS-IMP-A.5.24-28 Implementierungsleitfäden (UG/TG-Varianten) dokumentiert.

**Geltungsbereich**: Diese Richtlinie gilt für alle Informationssicherheitsereignisse und -vorfälle, die Informationswerte, Systeme, Netzwerke und Dienste von [Organisation] betreffen – unabhängig von der Quelle (intern, extern, Drittanbieter) oder dem Betriebsmodell (On-Premises, Cloud, Hybrid).

**Kombinierter Massnahmenansatz**: Diese fünf Massnahmen werden als einheitliches Lebenszyklus-Framework umgesetzt:

1. **Planung & Vorbereitung (A.5.24)** – Fähigkeiten etablieren, bevor Vorfälle eintreten
2. **Bewertung & Entscheidung (A.5.25)** – Festlegen, ob ein Ereignis ein reaktionspflichtiger Vorfall ist
3. **Reaktionsbetrieb (A.5.26)** – Eindämmen, beseitigen, Wiederherstellung nach Vorfällen
4. **Beweismittelerhebung (A.5.28)** – Forensische Beweise sichern (parallel zur Reaktion)
5. **Lernen & Verbesserung (A.5.27)** – Erkenntnisse gewinnen, Massnahmen verbessern

Trotz einheitlicher Umsetzung behält jede Massnahme eigenständige Anforderungen für den Anwendbarkeitsnachweis (SoA) bei.

---

# Geltungsbereich & Anwendbarkeit

## Im Geltungsbereich

**Informationssicherheitsvorfälle** mit Auswirkungen auf:

- IT-Systeme, Anwendungen und Datenbanken
- Daten und Informationswerte (alle Klassifikationsstufen)
- Netzwerkinfrastruktur (On-Premises, Cloud, Hybrid)
- Benutzer und Authentifizierungssysteme
- Drittanbietersysteme mit Schnittstellen zu [Organisation]
- Physische Sicherheitsvorfälle mit Auswirkungen auf Informationswerte

**Abgedeckte Vorfallkategorien**:

- Schadsoftware und Ransomware
- Unbefugter Zugriff und Privilegienerweiterung
- Datenschutzverletzungen und Datenexfiltration
- Dienstverweigerung (DoS/DDoS)
- Social Engineering und Phishing
- Insider-Bedrohungen (böswillig, fahrlässig)
- Physische Sicherheitsvorfälle mit IT-Auswirkungen
- Lieferketten- und Drittanbieter-Vorfälle
- Konfigurationsfehler mit Sicherheitsauswirkungen

## Ausserhalb des Geltungsbereichs

Folgende Bereiche erfordern die Genehmigung der Geschäftsleitung und eine dokumentierte Risikoakzeptanz:

- Vorfälle, die ausschliesslich öffentliche (nicht klassifizierte) Informationen ohne geschäftliche Auswirkungen betreffen
- Vorfälle, die durch separate Frameworks verwaltet werden (z. B. Sicherheitsvorfälle, HR-Verstösse ohne Sicherheitskomponente)
- Drittanbieter-Vorfälle mit vertraglicher Übertragung des Incident-Managements

## Anwendbarkeit für Dritte

Drittanbieter, Auftragnehmer und Partner, die auf Systeme von [Organisation] zugreifen oder Daten von [Organisation] verarbeiten, MÜSSEN:

- Sicherheitsereignisse und -vorfälle gemäss den Meldeanforderungen von [Organisation] melden
- Mit den Incident-Response-Aktivitäten von [Organisation] kooperieren
- Anforderungen zur Beweismittelsicherung einhalten
- An Post-Incident-Reviews teilnehmen, wenn Drittanbieter-Handlungen zum Vorfall beigetragen haben

## Regulatorische Anwendbarkeit

Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen):

**Stufe 1: Verbindliche Compliance**

- **Schweizer nDSG (DSG)**: Art. 24 – Datenschutzverletzungsmeldung an EDÖB «so schnell wie möglich» bei hohem Risiko
- **EU DSGVO**: Art. 33-34 – Meldung einer Verletzung an die Aufsichtsbehörde innerhalb von 72 Stunden
- **ISO/IEC 27001:2022**: Massnahmen A.5.24, A.5.25, A.5.26, A.5.27, A.5.28

**Stufe 2: Bedingte Anwendbarkeit**

- PCI DSS v4.0.1, FINMA, DORA, NIS2, HIPAA – Gelten, wenn die Geschäftstätigkeit von [Organisation] die Anwendbarkeit gemäss ISMS-POL-00 auslöst

---

# Richtlinienerklärungen

## Planung & Vorbereitung des Incident-Managements (A.5.24)

[Organisation] MUSS Incident-Management-Fähigkeiten etablieren, BEVOR Vorfälle eintreten.

**PS-3.1.1 Organisatorische Fähigkeit**: [Organisation] MUSS eine Incident-Response-Fähigkeit durch designierte CSIRT- (Computer Security Incident Response Team) und/oder SOC- (Security Operations Center) Funktionen mit definierten Befugnissen und Ressourcen aufbauen.

**PS-3.1.2 Dokumentierte Verfahren**: [Organisation] MUSS Incident-Response-Verfahren dokumentieren und pflegen, die den vollständigen Vorfall-Lebenszyklus abdecken. Verfahren MÜSSEN versionskontrolliert und jährlich überprüft werden.

**PS-3.1.3 Klassifikationsrahmen**: [Organisation] MUSS einen Vorfall-Klassifikationsrahmen erstellen, der Schweregrade und Vorfallkategorien definiert. Der Rahmen MUSS eine konsistente Vorfall-Priorisierung und Eskalation ermöglichen.

**PS-3.1.4 Schulungsanforderungen**: Incident-Response-Personal MUSS geschult sein und Kompetenz nachweisen, bevor es Incident-Response-Aufgaben übernimmt. Kompetenz MUSS durch praktische Planübungen und die Bestätigung des Vorgesetzten über Kenntnisse der Reaktionsverfahren bewertet werden. Mindeststandards für Kompetenz sind in ISMS-IMP-A.5.24-28.S1 definiert. Schulungen MÜSSEN jährlich aufgefrischt werden (maximales Intervall: 12 Monate seit letzter Durchführung).

**PS-3.1.5 Übungsanforderungen**: [Organisation] MUSS mindestens zweimal jährlich Incident-Response-Planübungen (Tabletop Exercises) durchführen, die wesentliche Vorfallszenarien abdecken. Übungsergebnisse MÜSSEN dokumentiert, nach Risiko priorisiert und als Verbesserungsmassnahmen gemäss PS-3.5.3 (Lernen & Verbesserung) verfolgt werden. Kritische Lücken in Fähigkeiten erfordern sofortige Behebung mit Eskalation zur Geschäftsleitung.

**PS-3.1.6 Tools & Technologie**: [Organisation] MUSS Incident-Response-Teams mit geeigneten Tools ausstatten, darunter: (1) Incident-Management-System mit Workflow-Nachverfolgung, (2) forensische Erfassungsfähigkeit, (3) sicherer Kommunikationskanal (verschlüsselt), (4) Zugang zu Überwachungs-/Protokollierungssystemen gemäss A.8.15/A.8.16. Die Tool-Eignung wird jährlich in ISMS-IMP-A.5.24-28.S1 bewertet.

**Verifizierung**: Dokumentierte Verfahren, Schulungsnachweise, Übungsberichte und Tool-Fähigkeiten werden durch die ISMS-IMP-A.5.24-28.S1-Bewertung verifiziert.

## Ereignisbewertung & Entscheidung (A.5.25)

[Organisation] MUSS alle Sicherheitsereignisse systematisch bewerten, um festzustellen, ob sie reaktionspflichtige Vorfälle darstellen.

**PS-3.2.1 Bewertungsanforderung**: Alle durch Überwachung erkannten oder von Benutzern gemeldeten Sicherheitsereignisse MÜSSEN bewertet werden, um festzustellen, ob sie reaktionspflichtige Vorfälle darstellen. Ereignisse MÜSSEN für die Bewertung priorisiert werden nach: (1) automatisierten Schweregradanzeigen aus Überwachungssystemen (A.8.16), (2) Kritikalität des betroffenen Systems gemäss Anlagenregister (A.5.9), (3) Ereignisquelle (SOC-Warnmeldungen werden bei Duplikaten gegenüber Benutzerberichten bevorzugt). Die Ereignispriorisierungsmethodik ist in ISMS-IMP-A.5.24-28.S2 detailliert.

**PS-3.2.2 Schweregradklassifikation**: Allen bestätigten Vorfällen MUSS ein Schweregrad zugewiesen werden, basierend auf den Auswirkungen auf Vertraulichkeit, Integrität und Verfügbarkeit unter Verwendung der in ISMS-REF-A.5.24-28 Abschnitt 1 definierten CIA-Auswirkungsbewertungsmatrix. Die Bewertung berücksichtigt: betroffenes Datenvolumen, Systemkritikalität (gemäss A.5.9 Anlagenregister), Auswirkungen auf Geschäftsprozesse, regulatorische Meldepflicht-Auslöser. Vorfälle mit Schweregrad Kritisch und Hoch MÜSSEN von zwei Analysten unabhängig bewertet werden, um Konsistenz sicherzustellen. Der Schweregrad eines Vorfalls DARF reklassifiziert werden, wenn neue Informationen die Auswirkungsbeurteilung ändern; eine Reklassifizierung auf Hoch/Kritisch erfordert die Genehmigung des Incident-Response-Managers mit rückwirkenden Managementbenachrichtigungen gemäss Abschnitt 5.2.

**PS-3.2.3 Kategorisierung**: Alle Vorfälle MÜSSEN nach Typ klassifiziert werden, unter Verwendung der organisatorischen Vorfallstaxonomie, um geeignete Reaktionsverfahren und Trendanalysen zu ermöglichen.

**PS-3.2.4 Eskalationsanforderungen**: Vorfälle MÜSSEN entsprechend ihrer Schweregrade an geeignete Managementebenen eskaliert werden. Kritische Vorfälle erfordern sofortige Benachrichtigung der Geschäftsleitung.

**PS-3.2.5 Dokumentation**: Alle Ereignisbewertungen MÜSSEN im Incident-Management-System mit Pflichtfeldern dokumentiert werden: (1) Ereignisquelle und Erkennungszeitstempel, (2) CIA-Auswirkungsanalyse mit Bewertung, (3) Schweregrad und Begründung der Einstufung, (4) Vorfallkategorie gemäss Taxonomie, (5) ergriffene Eskalationsmassnahmen mit gesendeten Benachrichtigungen, (6) Name des Genehmigenden und Genehmigungszeitstempel. Das Incident-Management-System MUSS die obligatorische Feldbefüllung vor Abschluss der Bewertung erzwingen.

**Verifizierung**: Bewertungsgenauigkeit, Klassifikationskonsistenz und Einhaltung der Eskalationsanforderungen werden durch die ISMS-IMP-A.5.24-28.S2-Bewertung verifiziert.

## Incident-Response-Betrieb (A.5.26)

[Organisation] MUSS auf bestätigte Vorfälle gemäss dokumentierten Verfahren reagieren.

**PS-3.3.1 Reaktionsdurchführung**: Auf alle bestätigten Vorfälle MUSS gemäss dokumentierten Verfahren reagiert werden, die dem Schweregrad und der Kategorie des Vorfalls entsprechen. Reaktionsverfahren werden basierend auf der Vorfallkategorie (PS-3.2.3) ausgewählt, wobei der Schweregrad (PS-3.2.2) die Ressourcenzuweisung und Eskalation bestimmt. Incident-Response-Playbooks werden in ISMS-REF-A.5.24-28 Abschnitt 3 für jede primäre Vorfallkategorie gepflegt:

- **Schadsoftware/Ransomware**: Isolierung, forensische Abbilderstellung, Schadsoftwareanalyse, Beseitigungsverifizierung
- **Unbefugter Zugriff**: Entzug von Anmeldeinformationen, Sitzungsbeendigung, Zugriffsprotokollüberprüfung, Bewertung der Privilegienerweiterung
- **Datenschutzverletzung**: Umfangsbewertung, Analyse der regulatorischen Meldepflicht (DSGVO/nDSG), Identifizierung betroffener Parteien, Beweismittelsicherung
- **Dienstverweigerung**: Datenverkehrsanalyse, Aktivierung von Abhilfemassnahmen (Rate-Limiting, vorgelagertes Filtering), Priorisierung der Dienstwiederherstellung
- **Social Engineering**: Benutzerbenachrichtigung, Zurücksetzen von Anmeldeinformationen, Stärkung des Sicherheitsbewusstseins, Prävention ähnlicher Angriffe
- **Insider-Bedrohung**: Beweismittelsicherung (Legal Hold), HR-Koordination, Zugangssperre, Bestimmung des Untersuchungsumfangs
- **Physische Sicherheit**: Asset-Rückgewinnung, Zutrittskontrollverifizierung, Überwachungsüberprüfung, Behebung physischer Massnahmen
- **Lieferkette**: Lieferantenbenachrichtigung, Abhängigkeitsbewertung, Aktivierung kompensierender Massnahmen, Vertragsüberprüfung

Bei Vorfällen, die mehrere Kategorien umfassen, wird die primäre Kategorie durch die schwerwiegendste Auswirkung bestimmt (Datenschutzverletzung hat Vorrang vor dem ursprünglichen Zugriffsvektor). Die Playbook-Auswahl wird im Vorfallsdatensatz mit Begründung dokumentiert. Hybride oder neuartige Vorfälle ohne bestehendes Playbook folgen standardmässig dem allgemeinen Incident-Response-Verfahren mit Anleitung des Incident-Response-Managers.

**PS-3.3.2 Eindämmung**: Incident Response MUSS die Eindämmung priorisieren, um den Umfang zu begrenzen und weiteren Schaden zu verhindern. Der Eindämmungsansatz variiert nach Schweregrad, wobei bei Kritisch/Hoch-Vorfällen eine aggressive Eindämmung erfolgt. Die Wirksamkeit der Eindämmung MUSS vor dem Übergang zur Beseitigungsphase verifiziert werden: (1) Keine weiteren Systeme zeigen Kompromittierungsindikatoren, (2) Angriffsvektor ist identifiziert und blockiert, (3) Zugang des Bedrohungsakteurs ist beendet (Entzug von Anmeldeinformationen, Sitzungsbeendigung bestätigt), (4) Überwachung bestätigt keine seitliche Bewegung für mindestens 1 Stunde (Kritisch/Hoch) oder 4 Stunden (Mittel). Bei andauernden ausgefeilten Angriffen kann die Eindämmung iterativ erfolgen, mit Genehmigung des Incident-Response-Managers.

**PS-3.3.3 Beseitigung**: Die Ursache von Vorfällen MUSS beseitigt werden, bevor Systeme in den Produktionsbetrieb zurückgeführt werden. Beseitigungsmassnahmen MÜSSEN vor dem Übergang zur Wiederherstellung verifiziert werden.

**PS-3.3.4 Wiederherstellung**: Betroffene Systeme und Dienste MÜSSEN nach Sicherheitsverifizierung in den Normalbetrieb zurückgeführt werden. Die Wiederherstellung MUSS den Geschäftskritikalitätsprioritäten folgen, die mit den BC/DR-Anforderungen abgestimmt sind. Die Systemwiederherstellungspriorität wird durch die Kritikalitätsbewertungen aus dem Anlagenregister (A.5.9) und die Recovery Time Objectives (RTO) aus den BC/DR-Plänen (A.5.29-30) bestimmt. Prioritätsstufen: (1) Kritische Systeme (RTO < 4 Stunden) – sofortige Wiederherstellung, (2) Hohe Priorität (RTO 4-24 Stunden) – noch am selben Geschäftstag, (3) Mittlere Priorität (RTO 1-3 Tage) – nächster Geschäftstag, (4) Niedrige Priorität (RTO > 3 Tage) – geplante Wiederherstellung. Die Wiederherstellungsreihenfolge berücksichtigt Abhängigkeiten (unterstützende Infrastruktur vor abhängigen Anwendungen wiederherstellen). Wiederherstellungsprioritäten können vom Incident-Response-Manager mit Genehmigung der Geschäftsleitung übersteuert werden, wenn der Vorfallskontext eine Abweichung erfordert.

**PS-3.3.5 Kommunikation**: Vorfallkommunikation MUSS dokumentierten Protokollen für interne Stakeholder, Management, Benutzer und externe Parteien (Regulatoren, Kunden, Strafverfolgungsbehörden) folgen. Kommunikationsprotokolle MÜSSEN festlegen:

- **Interne Stakeholder**: Incident-Response-Team (alle Schweregrade), betroffene Geschäftsbereichsverantwortliche (Mittel+), IT-Betrieb (alle Schweregrade), InfoSec-Management (Hoch+), Geschäftsleitung (Kritisch)
- **Management-Eskalationen**: Gemäss der Eskalationsmatrix in Abschnitt 5.2 mit definiertem Inhalt (Vorfallszusammenfassung, Auswirkungsbewertung, Eindämmungsstatus, voraussichtliche Lösungszeit)
- **Benutzerbenachrichtigungen**: Betroffene Benutzer werden über Dienstunterbrechungen informiert (Mittel+), mit Updates gemäss SLA-Intervallen bei andauernden Vorfällen
- **Externe Parteien**:
  - Regulatoren (DSGVO/nDSG-Verletzungsmeldung gemäss Art. 33/Art. 24) – Rechtsabteilung und DSB koordinieren
  - Kunden (wenn deren Daten betroffen sind) – Kommunikationsteam entwirft, Geschäftsleitung genehmigt
  - Strafverfolgungsbehörden (bei Verdacht auf kriminelle Aktivitäten) – Rechtsbeistand entscheidet und koordiniert
  - Dritte (wenn Lieferanten-Vorfall [Organisation] betrifft) – Lieferantenmanagement koordiniert gemäss A.5.22

Kommunikationsvorlagen für jeden Schweregrad und Stakeholder-Typ werden in ISMS-REF-A.5.24-28 Abschnitt 2 und im Incident-Management-System gepflegt. Alle Kommunikationen für Kritisch/Hoch-Vorfälle erfordern die Genehmigung des Incident-Response-Managers vor dem Versand.

**PS-3.3.6 Reaktionszeitstandards**: [Organisation] MUSS Reaktionszeitstandards (SLAs) nach Schweregrad gemäss Abschnitt 5.1.1 definieren und einhalten. Die SLA-Konformität MUSS monatlich gemessen und in vierteljährlichen Führungsberichten berichtet werden. Verpasste SLAs erfordern eine Ursachenanalyse gemäss PS-3.5.2 (Post-Incident-Review), um systemische Probleme mit Handlungsbedarf zu identifizieren.

**Verifizierung**: Reaktionsdurchführung, SLA-Konformität und Kommunikationseffektivität werden durch die ISMS-IMP-A.5.24-28.S3-Bewertung verifiziert.

## Forensische Beweismittelerhebung & Sicherung (A.5.28)

[Organisation] MUSS Verfahren für die Identifizierung, Erhebung, Erfassung und Sicherung forensischer Beweismittel etablieren.

**PS-3.4.1 Anforderung zur Beweismittelerhebung**: Forensische Beweismittel MÜSSEN für alle Vorfälle mit Schweregrad Kritisch und für Hoch-Vorfälle mit möglichen rechtlichen oder regulatorischen Auswirkungen erhoben werden.

**PS-3.4.2 Zeitpunkt der Erhebung**: Die Beweismittelerhebung beginnt unmittelbar nach der Vorfallserkennung und läuft parallel zu den Reaktionsmassnahmen. Die Beweismittelsicherung DARF NICHT geopfert werden, ausser wenn die Eindämmung aktiver Bedrohungen Vorrang hat.

**PS-3.4.3 Forensisch einwandfreie Methoden**: Beweismittel MÜSSEN mit forensisch einwandfreien Methoden erhoben werden, die die Integrität wahren und eine mögliche rechtliche Verwertbarkeit unterstützen.

**PS-3.4.4 Beweismittelkette (Chain of Custody)**: Alle Beweismittel MÜSSEN eine dokumentierte Beweismittelkette von der Erhebung bis zur Entsorgung aufweisen, einschliesslich Übergaben, Aufbewahrungsorte und Zugriffsaufzeichnungen.

**PS-3.4.5 Beweismittelsicherung**: Beweismittel MÜSSEN sicher mit Zugangskontrollen, Verschlüsselung und Integritätsverifizierung gesichert werden. Aufbewahrungsfristen MÜSSEN den regulatorischen Anforderungen und den Aufbewahrungsrichtlinien von [Organisation] entsprechen.

**PS-3.4.6 Legal Hold**: [Organisation] MUSS Legal-Hold-Verfahren implementieren, wenn Rechtsstreitigkeiten eingeleitet werden oder vernünftigerweise zu erwarten sind, und normale Löschprozesse für relevante Beweismittel aussetzen.

**Verifizierung**: Beweismittelverfahren, Dokumentation der Beweismittelkette und Sicherungskontrollen werden durch die ISMS-IMP-A.5.24-28.S4-Bewertung verifiziert.

## Post-Incident-Lernen & Verbesserung (A.5.27)

[Organisation] MUSS Erkenntnisse aus Vorfällen gewinnen und Massnahmen zur Verbesserung von Sicherheitskontrollen ableiten.

**PS-3.5.1 Anforderung zum Post-Incident-Review**: Post-Incident-Reviews (PIR) MÜSSEN für alle Vorfälle mit Schweregrad Kritisch und Hoch innerhalb definierter Fristen durchgeführt werden. Vorfälle mit Schweregrad Mittel erfordern einen PIR, wenn sie neuartige Angriffstechniken oder erhebliche Kontrollversagen aufzeigen.

**PS-3.5.2 Ursachenanalyse**: Eine Ursachenanalyse MUSS durchgeführt werden, um systemische Grundursachen zu identifizieren – nicht nur unmittelbare Ursachen. Erkenntnisse MÜSSEN präventive Massnahmen beeinflussen.

**PS-3.5.3 Umsetzung von Verbesserungen**: Gewonnene Erkenntnisse MÜSSEN in umsetzbare Verbesserungen mit zugewiesenen Verantwortlichen und Zielabschlussdaten umgesetzt werden. Verbesserungsmassnahmen MÜSSEN bis zur Fertigstellung verfolgt werden.

**PS-3.5.4 Wissensmanagement**: [Organisation] MUSS ein Erkenntnisarchiv pflegen, das für Incident-Response-Personal zugänglich ist. Reaktions-Playbooks MÜSSEN basierend auf gewonnenen Erkenntnissen aktualisiert werden.

**PS-3.5.5 Metriken & Trendanalyse**: [Organisation] MUSS Vorfallmetriken (Volumen, Schweregrad, Reaktionszeiten, SLA-Konformität) verfolgen und vierteljährliche Trendanalysen durchführen, um systemische Probleme zu identifizieren.

**PS-3.5.6 Jährliche Programmüberprüfung**: Das Incident-Management-Programm MUSS jährlich überprüft werden, um die Wirksamkeit zu bewerten, anhand von Standards zu vergleichen und Verfahren, Schulungen und Tools zu aktualisieren.

**Verifizierung**: PIR-Abschluss, Verbesserungsverfolgung und Metrik-Berichterstattung werden durch die ISMS-IMP-A.5.24-28.S5-Bewertung verifiziert.

---

# Rollen & Verantwortlichkeiten

## Geschäftsleitung

- **Accountable** für die Gesamtwirksamkeit des Incident-Management-Programms
- **Genehmigt** die Incident-Management-Richtlinie und wesentliche Verfahrensänderungen
- **Entscheidet** über geschäftskritische Massnahmen (Serviceabschaltung, öffentliche Bekanntmachung, Einbeziehung der Strafverfolgung)
- **Erhält** Statusaktualisierungen bei kritischen Vorfällen, vierteljährliche Metriken, jährliche Programmüberprüfung

## Informationssicherheitsbeauftragter (ISB)

- **Accountable** für die Einhaltung der Incident-Management-Richtlinie und die Programmreife
- **Genehmigt** Verfahren, akzeptiert Restrisiken, weist Budget und Ressourcen zu
- **Entscheidet** über Hoch-/Kritisch-Vorfallseskalationen und externe Einbindung
- **Erhält** alle Vorfallsberichte, PIR-Berichte, wöchentliche Metriken

## Incident-Response-Manager / CSIRT-Leitung

- **Accountable** für den täglichen Incident-Response-Betrieb und die SLA-Konformität
- **Verwaltet** Vorfallbewertung, Reaktionskoordination, Ressourcenzuweisung, Kommunikation, Schulung
- **Genehmigt** Vorfallabschluss, PIR-Planung, Verfahrensaktualisierungen
- **Berichtet** an den ISB über Vorfallstatus, Metriken und Programmzustand

## Incident-Handler / SOC-Analysten

- **Verantwortlich** für Incident-Triage, Untersuchung, Eindämmung, Beseitigung, Wiederherstellung und Dokumentation
- **Führen** Reaktionsverfahren nach Schweregrad und Kategorie durch
- **Eskalieren** Vorfälle gemäss der Eskalationsmatrix
- **Dokumentieren** alle Vorfallsaktivitäten im Incident-Management-System

## Forensik-Spezialisten

- **Accountable** für die Integrität der Beweismittelerhebung und die Beweismittelkette
- **Führen** forensische Analysen und Beweismittelsicherung durch
- **Koordinieren** mit der Rechtsabteilung zur Beweismittelverwertbarkeit und Legal Hold
- **Dokumentieren** alle Beweismittelerhebungen und Übergaben

## IT-Betrieb

- **Verantwortlich** für die Durchführung von Eindämmungs-/Beseitigungs-/Wiederherstellungsmassnahmen an Systemen
- **Koordiniert** die Dienstwiederherstellung mit dem Incident-Response-Team
- **Stellt** technische Unterstützung und Systemzugang für die Vorfallsuntersuchung bereit
- **Setzt** technische Kontrollverbesserungen aus PIR-Empfehlungen um

## Rechtsbeistand

- **Accountable** für Risikovermeidung im Rechtsbereich und regulatorische Compliance
- **Berät** zu rechtlichen Auswirkungen, regulatorischen Meldepflichten, Beweismittelsicherung
- **Koordiniert** Behördenbenachrichtigungen mit dem DSB
- **Verwaltet** Legal-Hold-Verfahren und Verbindung zur Strafverfolgung

## Datenschutzbeauftragter (DSB)

- **Accountable** für Datenschutz-Compliance und Bewertung der Datenschutzverletzungsmeldung
- **Bewertet** Vorfälle auf Meldepflicht gemäss DSGVO/nDSG
- **Koordiniert** Benachrichtigungen der betroffenen Personen bei Bedarf
- **Berät** zu datenschutzrechtlichen Auswirkungen von Vorfällen

## Kommunikationsteam

- **Verantwortlich** für externe Kommunikation und Reputationsmanagement
- **Entwirft** Kommunikation an Benutzer, Kunden und Medien
- **Koordiniert** Botschaften mit der Rechtsabteilung und Geschäftsleitung
- **Führt** genehmigte externe Kommunikation durch

## Gesamtes Personal

- **Verantwortlich** für die Meldung vermuteter Sicherheitsvorfälle gemäss ISMS-POL-A.6.8
- **Kooperiert** mit Incident-Response-Aktivitäten auf Anfrage
- **Absolviert** Sicherheitsbewusstseinstraining einschliesslich Vorfallsmeldung

---

# Governance-Rahmen

## Vorfallschweregradeinteilung

[Organisation] MUSS Schweregrade mit zugehörigen Reaktionsanforderungen definieren:

| Schweregrad | Definition | Reaktionsanforderung |
|-------------|------------|---------------------|
| **Kritisch** | Erhebliche geschäftliche Auswirkung; grossangelegte Verletzung, Ransomware mit Auswirkung auf Produktion, Kompromittierung kritischer Infrastruktur, regulatorische Meldepflicht ausgelöst | Sofortige Reaktion, aggressive Eindämmung, Benachrichtigung der Geschäftsleitung, obligatorischer PIR |
| **Hoch** | Mittlere geschäftliche Auswirkung; gezielter Angriff, bestätigter Datenzugriff, Kompromittierung sensibler Systeme, Dienstbeeinträchtigung | Dringende Reaktion, ISB-Benachrichtigung, obligatorischer PIR |
| **Mittel** | Begrenzte geschäftliche Auswirkung; isolierte Infektion, erfolgloser Angriff, geringfügiger Richtlinienverstoss | Standardreaktion, Teamleiter-Aufsicht, bedingter PIR |
| **Niedrig** | Minimale geschäftliche Auswirkung; blockierter Angriff, geringfügige Anomalie, Informationsereignis | Standardbearbeitung, Stapelverarbeitung akzeptabel, kein PIR erforderlich |

## Reaktionszeitstandards (SLAs)

[Organisation] definiert die folgenden Reaktionszeitstandards nach Schweregrad:

| Schweregrad | Erste Reaktion | Eindämmungsziel | Lösungsziel | Management-Updates |
|-------------|----------------|-----------------|-------------|-------------------|
| **Kritisch** | 15 Minuten | 1 Stunde | 24 Stunden | Echtzeit (stündlich) |
| **Hoch** | 1 Stunde | 4 Stunden | 72 Stunden | Täglich |
| **Mittel** | 4 Stunden | 24 Stunden | 5 Arbeitstage | Wöchentlich (bei andauerndem Vorfall) |
| **Niedrig** | 8 Stunden | 48 Stunden | 10 Arbeitstage | Sammelberichterstattung |

**Erste Reaktion**: Zeit von der Vorfallsbestätigung (PS-3.2.1 Bewertung abgeschlossen) bis zur Zuweisung des Reaktionsteams und Einleitung der Eindämmungsmassnahmen.

**Eindämmungsziel**: Zeit zur Begrenzung des Vorfallumfangs und Verhinderung weiterer Schäden. Das Ziel ist ein Richtwert, keine Garantie – komplexe Vorfälle können Ziele mit dokumentierter Begründung überschreiten.

**Lösungsziel**: Zeit bis zum Abschluss der Beseitigung und Wiederherstellung sowie Rückkehr zum Normalbetrieb. Die Uhr stoppt, wenn der Vorfall vom Incident-Response-Manager abgeschlossen wird.

**Management-Updates**: Häufigkeit der Statusberichte an das Management gemäss Abschnitt 5.3.

Die SLA-Konformität wird monatlich gemessen und in vierteljährlichen Führungsberichten ausgewiesen. Verpasste SLAs erfordern eine Ursachenanalyse gemäss PS-3.5.2 (Post-Incident-Review). SLA-Ziele werden jährlich im Rahmen der Programmüberprüfung (PS-3.5.6) überprüft und auf Basis der operativen Realität und Branchenbenchmarks angepasst.

Detaillierte SLA-Messverfahren sind in ISMS-IMP-A.5.24-28.S3 definiert.

## Eskalationsanforderungen

**Kritische Vorfälle**: Sofortige Eskalation an ISB und Geschäftsleitung
**Hoch-Vorfälle**: Eskalation an Incident-Response-Manager (sofort), ISB (innerhalb definierter Frist)
**Mittel-/Niedrig-Vorfälle**: Teamleiter-Aufsicht; Eskalation bei Schweregrad-Erhöhung oder Lösungsstagnation

Häufigkeit und Inhalt der Managementbenachrichtigungen sind in ISMS-IMP-A.5.24-28.S3 definiert.

## Berichtspflichten

**Operatives Reporting**:

- Kritische Vorfälle: Echtzeit-Statusaktualisierungen an Geschäftsleitung
- Hoch-Vorfälle: Tägliche Statusaktualisierungen an ISB
- Alle Vorfälle: Wöchentliche Zusammenfassung an ISB

**Führungsreporting**:

- Vierteljährliche Vorfallszusammenfassung an Geschäftsleitung (Volumen, Trends, Metriken, Erkenntnisse)
- Jährliche Incident-Management-Programmüberprüfung für Geschäftsleitung

## Integration mit verwandten Massnahmen

Diese Richtlinie integriert sich mit:

| Massnahme | Integrationspunkt |
|-----------|-------------------|
| **A.8.16 (Überwachung)** | Überwachung erkennt Ereignisse, die in die Vorfallbewertung einfliessen |
| **A.8.15 (Protokollierung)** | Protokolle liefern Beweise für Untersuchung und Forensik |
| **A.6.8 (Ereignismeldung)** | Benutzerberichte fliessen in den Bewertungsprozess ein |
| **A.5.29-30 (BC/DR)** | Grosse Vorfälle können die BC/DR-Aktivierung auslösen |
| **A.5.31 (Rechtl./Regulat.)** | Regulatorische Meldepflichten sind integriert |
| **A.5.19-23 (Drittanbieter)** | Drittanbieter-Vorfälle werden gemeldet und koordiniert |

## Richtlinienüberprüfung

- **Häufigkeit**: Mindestens jährlich
- **Auslöser**: Wesentlicher Vorfall mit aufgedeckter Richtlinienlücke, regulatorische Änderungen, Prüfungsergebnisse, organisatorische Veränderungen
- **Prüfer**: ISB (Eigentümer), Incident-Response-Manager (Mitwirkender), Rechtsabteilung (Compliance)
- **Genehmigung**: ISB (fachlich), Geschäftsleitung (strategisch)

Umsetzungsverfahren und Referenzdokumente können ohne Richtlinienrevision aktualisiert werden, wenn Änderungen keine Richtlinienerklärungen betreffen.

---

# Compliance & Ausnahmen

## Compliance-Anforderungen

Gesamtes Personal MUSS diese Richtlinie einhalten. Die Compliance wird überwacht durch:

- Aufzeichnungen und Metriken des Incident-Management-Systems
- Verfolgung von Schulungsabschlüssen
- PIR-Abschlussraten
- Übungsteilnahme
- Abschluss von Verbesserungsmassnahmen

## Ausnahmenmanagement

Ausnahmen zu dieser Richtlinie erfordern:

- Schriftlicher Ausnahmeantrag mit geschäftlicher Begründung
- Risikobewertung der Ausnahme
- Kompensierende Massnahmen (falls zutreffend)
- Genehmigung durch ISB (Minimum); Genehmigung der Geschäftsleitung bei kritischen Kontrollausnahmen
- Zeitlich begrenzte Laufzeit (maximal 12 Monate, Erneuerung erforderlich)
- Dokumentation im ISMS-Ausnahmenregister

Ausnahmen werden jährlich auf ihre weitere Gültigkeit überprüft.

## Nicht-Konformität

Nicht-Konformität mit dieser Richtlinie kann folgende Konsequenzen haben:

- Eskalation an das Management
- Verstärkte Prüfaufmerksamkeit
- Disziplinarmassnahmen gemäss HR-Richtlinien
- Regulatorische Befunde bei Zertifizierungsaudits

---

# Verwandte Dokumente

## Implementierungsleitfäden

| Dokument | Zweck |
|----------|-------|
| **ISMS-IMP-A.5.24-28.S1-UG/TG** | Bewertung des Incident-Management-Frameworks (Governance, Struktur, Verfahren, Schulung, Tools) |
| **ISMS-IMP-A.5.24-28.S2-UG/TG** | Bewertung Ereigniserkennung & Klassifikation (Bewertungsverfahren, Klassifikationsgenauigkeit, Eskalation) |
| **ISMS-IMP-A.5.24-28.S3-UG/TG** | Bewertung Incident-Response-Fähigkeiten (Reaktionsverfahren, SLAs, Playbooks, Kommunikation) |
| **ISMS-IMP-A.5.24-28.S4-UG/TG** | Bewertung Forensische Beweismittelverwaltung (Beweismittelverfahren, Beweismittelkette, Sicherung) |
| **ISMS-IMP-A.5.24-28.S5-UG/TG** | Bewertung Lernen & Kontinuierliche Verbesserung (PIR, Ursachenanalyse, Verbesserungsverfolgung, Metriken) |

## Referenzmaterialien

| Dokument | Zweck |
|----------|-------|
| **ISMS-REF-A.5.24-28 Abschnitt 1** | Vorfallklassifikationstaxonomie (Kategorien, Unterkategorien, Schweregradindikatoren) |
| **ISMS-REF-A.5.24-28 Abschnitt 2** | Kurzreferenz regulatorische Meldepflichten (DSGVO, nDSG, sektorspezifische Anforderungen) |
| **ISMS-REF-A.5.24-28 Abschnitt 3** | Bibliothek forensischer Erhebungstechniken (technische Verfahren, Tools, Vorlagen) |

## Verwandte Richtlinien

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.8.15 (Protokollierung)
- ISMS-POL-A.8.16 (Überwachungsaktivitäten)
- ISMS-POL-A.6.8 (Meldung von Informationssicherheitsereignissen)
- ISMS-POL-A.5.29-30 (Betriebskontinuität & Notfallwiederherstellung)
- ISMS-POL-A.5.31 (Gesetzliche, behördliche, regulatorische und vertragliche Anforderungen)
- ISMS-POL-A.5.19-23 (Drittanbieter-Management)

## Externe Normen

- ISO/IEC 27001:2022 – Massnahmen A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
- ISO/IEC 27002:2022 – Umsetzungshinweise für Incident-Management-Massnahmen
- NIST SP 800-61 Rev. 2 – Computer Security Incident Handling Guide
- ISO/IEC 27035 – Information Security Incident Management

---

# Definitionen

**Informationssicherheitsereignis**: Ein identifiziertes Vorkommnis, das auf eine mögliche Verletzung der Informationssicherheitsrichtlinie oder ein Versagen von Sicherheitsmassnahmen hinweist. Ereignisse können nach Bewertung zu Vorfällen werden oder auch nicht.

**Informationssicherheitsvorfall**: Ein ungewolltes oder unerwartetes Informationssicherheitsereignis mit erheblicher Wahrscheinlichkeit, den Geschäftsbetrieb zu beeinträchtigen und die Informationssicherheit zu bedrohen. Vorfälle erfordern Reaktionsmassnahmen.

**CSIRT (Computer Security Incident Response Team)**: Organisatorisches Team, das für den Empfang, die Überprüfung und die Reaktion auf Informationssicherheitsvorfälle verantwortlich ist.

**SOC (Security Operations Center)**: Team oder Funktion, das/die für die Überwachung, Erkennung, Analyse und Reaktion auf Sicherheitsereignisse und -vorfälle verantwortlich ist.

**Post-Incident-Review (PIR)**: Strukturierte Überprüfung nach Vorfallabschluss zur Dokumentation des Zeitablaufs, Bewertung der Reaktionswirksamkeit, Identifizierung von Erkenntnissen und Empfehlung von Verbesserungen.

**Ursachenanalyse (Root Cause Analysis, RCA)**: Systematische Untersuchung zur Identifizierung der grundlegenden Ursache(n), die das Eintreten eines Vorfalls ermöglicht haben.

**Beweismittelkette (Chain of Custody)**: Dokumentierter Nachweis darüber, wer Beweismittel wann, wo, wie erhoben hat und jede Übergabe von Beweismitteln zwischen Parteien.

**Legal Hold**: Anweisung zur Aufbewahrung aller potenziell relevanten Beweismittel im Zusammenhang mit anhängigen oder vernünftigerweise zu erwartenden Rechtsverfahren.

---

# Nachweise für diese Richtlinie

**Phase 1 (Dokumentenprüfung) Nachweise:**

Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.24-28 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL, Geschäftsleitung
- ✅ Anforderungen an Incident-Management-Fähigkeiten definiert (Abschnitt 3.1 – PS-3.1.1 bis PS-3.1.6)
- ✅ Bewertungs- und Klassifikationsrahmen für Ereignisse dokumentiert (Abschnitt 3.2 – PS-3.2.1 bis PS-3.2.5)
- ✅ Incident-Response-Betriebsverfahren festgelegt (Abschnitt 3.3 – PS-3.3.1 bis PS-3.3.6)
- ✅ Forensische Beweismittelanforderungen dokumentiert (Abschnitt 3.4 – PS-3.4.1 bis PS-3.4.6)
- ✅ Anforderungen für Post-Incident-Lernen festgelegt (Abschnitt 3.5 – PS-3.5.1 bis PS-3.5.6)
- ✅ Vorfallschweregradeinteilung definiert (Abschnitt 5.1)
- ✅ Eskalationsanforderungen dokumentiert (Abschnitt 5.2)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Abschnitt 4)
- ✅ Governance- und Ausnahmeverfahren definiert (Abschnitt 6)
- ✅ Integration mit verwandten Massnahmen dokumentiert (Abschnitt 5.4)

**Phase 2 (Operative Wirksamkeit) Nachweise:**

Nachweise, die belegen, dass diese Richtlinie operativ wirksam ist:

- Vorfallregister, das alle protokollierten Vorfälle mit Klassifikation (Schweregrad, Kategorie) ausweist
- Vorfallzeitachsen mit Nachweis der SLA-Konformität (Erkennung → Eindämmung → Lösung)
- Eskalationsaufzeichnungen mit angemessenen Managementbenachrichtigungen nach Schweregrad
- CSIRT/SOC-Besetzungsaufzeichnungen und Kompetenzverifizierung
- Schulungsabschlussaufzeichnungen für Incident-Response-Personal
- Berichte über Planübungen (Tabletop Exercises, mindestens zweimal jährlich)
- Post-Incident-Review (PIR)-Berichte für alle Vorfälle der Schweregrade Kritisch/Hoch
- Ursachenanalysedokumentation mit Verbesserungsempfehlungen
- Aktualisierungen des Erkenntnisarchivs
- Verfolgung von Verbesserungsmassnahmen bis zur Fertigstellung
- Dokumentation der forensischen Beweismittelkette
- Aufzeichnungen zur Beweismittelsicherung und Integritätsverifizierung
- Regulatorische Meldenachweise (DSGVO 72-Stunden-Frist, nDSG «so schnell wie möglich»)
- Vorfallmetrik-Dashboards (Volumen, Schweregrad, MTTR, SLA-Konformität)
- Vierteljährliche Trendanalyseberichte
- Dokumentation der jährlichen Programmüberprüfung
- Ausgaben der Bewertungsarbeitsmappen ISMS-IMP-A.5.24-28.S1-S5

**Aufbewahrungsorte für Nachweise**:

| Nachweistyp | Aufbewahrungsort |
|-------------|-----------------|
| Schulungsnachweise | HR-Informationssystem / Learning Management System |
| Übungsberichte | Incident-Management-System / Dokumentenablage |
| Tool-Inventar | Configuration Management Database (CMDB) |
| Verfahren | Dokumentenmanagementsystem |
| Kompetenzbewertungen | Vorgesetztenaufzeichnungen im HRIS |
| Vorfallsaufzeichnungen | Incident-Management-System |
| PIR-Berichte | Incident-Management-System / SharePoint |
| SLA-Konformitätsberichte | Business-Intelligence-Dashboard |

## Klarstellung zu Compliance-Nachweisen

Diese Richtlinie etabliert den Incident-Management-Governance-Rahmen (Planungs-, Bewertungs-, Reaktions-, Beweismittel- und Lernanforderungen). Sie legt NICHT fest:

- **Technische Erkennungskontrollen** (behandelt in A.8.16 Überwachungsaktivitäten – Überwachung liefert Ereignisfeeds zur Vorfallbewertung)
- **Protokollierungsinfrastrukturanforderungen** (behandelt in A.8.15 Protokollierung – Protokolle liefern Untersuchungsnachweise)
- **Betriebskontinuitätsverfahren** (behandelt in A.5.29-30 BC/DR – grosse Vorfälle können BC/DR-Aktivierung auslösen)
- **Benutzer-Ereignismeldeverfahren** (behandelt in A.6.8 Meldung von Informationssicherheitsereignissen – Benutzerberichte fliessen in die Bewertung ein)
- **Spezifische Incident-Response-Playbooks** (operatives Detail in ISMS-IMP-A.5.24-28 und ISMS-REF-A.5.24-28)

Die Abgrenzung: POL-A.5.24-28 definiert, WELCHE Incident-Management-Fähigkeiten erforderlich sind und WANN Massnahmen zu ergreifen sind → ISMS-IMP-A.5.24-28.S1-S5 liefert das WIE für die Fähigkeitsbewertung → ISMS-REF-A.5.24-28 liefert technische Referenzmaterialien → verwandte Massnahmen (A.8.15, A.8.16, A.6.8, A.5.29-30) stellen unterstützende Fähigkeiten bereit.

---

# Genehmigungsnachweis

| Rolle | Name | Datum | Unterschrift |
|-------|------|-------|--------------|
| **Dokumenteneigentümer (ISB)** | [Name] | [Datum] | [Unterschrift] |
| **Fachliche Prüfung (Incident-Response-Manager)** | [Name] | [Datum] | [Unterschrift] |
| **Fachliche Prüfung (ITL)** | [Name] | [Datum] | [Unterschrift] |
| **Rechtliche Prüfung (Rechtsbeistand)** | [Name] | [Datum] | [Unterschrift] |
| **Datenschutzprüfung (DSB)** | [Name] | [Datum] | [Unterschrift] |
| **Schlussgenehm. (Geschäftsleitung)** | [Name] | [Datum] | [Unterschrift] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen für das Informationssicherheits-Incident-Management über den vollständigen Lebenszyklus fest (A.5.24-28). Umsetzungsverfahren sind in ISMS-IMP-A.5.24-28 (UG/TG).S1 bis S5 dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
