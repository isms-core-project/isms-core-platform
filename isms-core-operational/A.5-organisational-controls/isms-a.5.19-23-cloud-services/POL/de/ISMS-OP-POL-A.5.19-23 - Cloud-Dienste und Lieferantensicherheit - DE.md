<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.19-23-DE:operational:OP-POL:a.5.19-23 -->
**ISMS-OP-POL-A.5.19-23 — Cloud-Dienste und Lieferantensicherheit**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Cloud-Dienste und Lieferantensicherheit |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.19-23 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 0.1 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [Date] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Kontrollen A.5.19–A.5.23 — Sicherheit von Lieferanten und Cloud-Diensten
- ISO/IEC 27002:2022 Kontrollen 5.19–5.23 — Implementierungsleitfaden

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zu Lieferanten- und Cloud-Sicherheit |
|-----------|---------------------------------------------|
| A.5.9 Inventar von Informationen und Assets | Lieferanten und Cloud-Dienste im Asset-Inventar erfasst |
| A.5.12–13 Informationsklassifizierung und -kennzeichnung | Datenklassifizierung bestimmt Sicherheitsanforderungen für Lieferanten |
| A.5.14 Informationsübertragung | Anforderungen an verschlüsselte Übertragung für Lieferantendatenaustausch |
| A.5.15–16–18 Identitäts- und Zugangsverwaltung | Bereitstellung und Widerruf von Lieferantenpersonalzugriffen |
| A.5.24–28 Incident Management | Vorfallsmeldung durch Lieferanten fliesst in den Incident-Management-Prozess ein |
| A.5.30, A.8.13–14 Geschäftskontinuität und Backup | Ausfallszenarien bei Lieferanten, Validierung der Exit-Strategie, unabhängige Backups |
| A.5.31 Gesetzliche, behördliche, regulatorische Anforderungen | Vertragliche Verpflichtungen, nDSG/DSGVO-Auftragsverarbeitungsanforderungen |
| A.5.34 Datenschutz und PII | Datenverarbeitungsverträge, Unterauftragsverarbeiter-Offenlegung, grenzüberschreitende Transfers |
| A.8.8 Schwachstellenmanagement | Patching-Verpflichtungen der Lieferanten, Schwachstellenoffenlegung |
| A.8.10 Datenlöschung | Verifizierung der Datenvernichtung bei Lieferanten bei Vertragsende |
| A.8.24 Einsatz von Kryptografie | Verschlüsselungsanforderungen für Lieferantendaten im Ruhezustand und bei der Übertragung |

**Verwandte interne Richtlinien**:

- Richtlinie zur Informationsklassifizierung und -handhabung
- Richtlinie zum Incident Management
- Richtlinie zur Informationsübertragung
- Richtlinie zum Datenschutz und Schutz von PII
- Richtlinie zur Geschäftskontinuität und Disaster Recovery

---

# Richtlinie für Cloud-Dienste und Lieferantensicherheit

## Zweck

Diese Richtlinie soll die Informationssicherheit bei der Nutzung von Cloud-Diensten verwalten und sicherstellen, dass die Datensicherheitsanforderungen für Drittlieferanten, deren Unterauftragnehmer und die Lieferkette erfüllt werden.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG), indem sie technische und organisatorische Massnahmen entsprechend dem Risiko zum Schutz personenbezogener Daten (einschliesslich besonders schützenswerter Personendaten) bei der Verarbeitung durch externe Lieferanten und Cloud-Dienstleister umsetzt. Soweit die Organisation Daten von Personen in der EU/EEA verarbeitet, gelten auch die DSGVO-Anforderungen. Sicherheitskontrollen für Lieferanten und Cloud-Dienste sind Schlüsselmassnahmen zum Nachweis der Einhaltung der Datenschutzverpflichtungen im Rahmen beider Regelwerke.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle Drittlieferanten und Cloud-Dienstleister, die vertrauliche oder personenbezogene Daten verarbeiten, speichern oder übertragen.

Alle Cloud-Dienste (IaaS, PaaS, SaaS), die von der Organisation genutzt werden.

## Grundsatz

Drittlieferanten und Cloud-Dienstleister sollten die Anforderungen der Organisation, der Gesetzgebung und der Regulierung an die Datensicherheit erfüllen. Lieferantenvertrauen sollte verifiziert, nicht angenommen werden — eine evidenzbasierte Validierung der Sicherheitslage des Lieferanten ist durch systematische Due-Diligence, vertragliche Verpflichtungen und laufende Überwachung erforderlich.

Cloud-Dienstvereinbarungen sind häufig vordefiniert und nicht verhandelbar. Ist dies der Fall, sollte die Organisation prüfen, ob die Standardbedingungen des Anbieters ihre Sicherheitsanforderungen erfüllen, und etwaige Restrisiken dokumentieren. Wenn Bedingungen nicht verhandelbar sind und die Anforderungen nicht erfüllen, sollten Ausgleichskontrollen identifiziert oder ein alternativer Anbieter geprüft werden.

Die Organisation sollte das Modell der geteilten Verantwortung für jeden Cloud-Dienst verstehen und dokumentieren. Sicherheitsverantwortlichkeiten sind zwischen dem Cloud-Dienstleister und der Organisation aufgeteilt, und diese Aufteilung variiert je nach Dienstleistungsmodell (IaaS, PaaS, SaaS). Die Organisation bleibt unabhängig vom Dienstleistungsmodell verantwortlich für die Sicherheit ihrer Daten, das Identitäts- und Zugriffsmanagement sowie den Endpunktschutz. Der Anbieter ist für die Sicherheit der zugrunde liegenden Infrastruktur verantwortlich. Bereiche geteilter Verantwortung sollten explizit dokumentiert und überprüft werden.

**Dokumentation der geteilten Verantwortung sollte umfassen**:

| Verantwortungsbereich | Anbieter verantwortlich | Organisation verantwortlich | Hinweise |
|-----------------------|-------------------------|-----------------------------|----------|
| Physische Rechenzentrumssicherheit | Ja | | Anbieter kontrolliert physischen Zugang |
| Netzwerkinfrastruktur | Ja | | Anbieter sichert zugrunde liegendes Netzwerk |
| Host-Infrastruktur | Ja (IaaS/PaaS/SaaS) | Ja (nur IaaS — OS-Patching) | Bei IaaS verwaltet Organisation das BS |
| Anwendungssicherheit | Ja (nur SaaS) | Ja (IaaS/PaaS) | Bei SaaS ist Anbieter verantwortlich |
| Datenverschlüsselung im Ruhezustand | Ja (Standard) | Ja (Schlüsselverwaltung) | Organisation kann eigene Schlüssel mitbringen (BYOK) |
| Identitäts- und Zugangsverwaltung | | Ja | Organisation immer verantwortlich |
| Datenklassifizierung und -handhabung | | Ja | Organisation immer verantwortlich |
| Endpunktsicherheit | | Ja | Organisation immer verantwortlich |

Modelle der geteilten Verantwortung sollten für jeden **kritischen** Cloud-Dienst dokumentiert und jährlich überprüft werden.

---

## Lieferanten- und Cloud-Dienstregister

Alle Drittlieferanten und Cloud-Dienste sollten im **Lieferanten- und Cloud-Dienstregister** erfasst und aufgezeichnet werden.

**Register-Speicherort**: [GRC-Plattform, Beschaffungssystem oder dediziertes Tabellenblatt in SharePoint/Äquivalent]

**Register-Eigentümer**: [ISB, Beschaffungsmanager oder IT-Manager]

**Zugriff**: Der Zugriff auf das Register ist auf autorisiertes Personal beschränkt (IT-Führung, Informationssicherheitsteam, Beschaffung). Das Register ist als **INTERN** klassifiziert.

**Aktualisierungshäufigkeit**: Das Register sollte mindestens **vierteljährlich** oder bei jeder neuen Lieferantenbeauftragung, Vertragsänderung oder Lieferantenkündigung überprüft und aktualisiert werden.

Lieferanten und Cloud-Dienste sollten auf ihre Kritikalität für das Unternehmen bewertet werden.

Lieferanten und Cloud-Dienste sollten basierend auf den verarbeiteten, gespeicherten oder übertragenen Daten und ihrer Kritikalität für den Geschäftsbetrieb klassifiziert werden:

| Klassifizierung | Kriterien | Überprüfungshäufigkeit |
|-----------------|-----------|------------------------|
| **Kritisch** | Zugriff auf vertrauliche/eingeschränkte Daten ODER Kerngeschäftsbetrieb (Ausfall verursacht sofortige Geschäftsauswirkungen) ODER verarbeitet besonders schützenswerte Personendaten (nDSG Art. 5) | Jährlich |
| **Wichtig** | Zugriff auf interne Daten, aber nicht vertraulich ODER unterstützende Dienste (Ausfall verursacht moderate Störung innerhalb von 24–48 Stunden) ODER begrenzte Verarbeitung personenbezogener Daten | Alle zwei Jahre |
| **Standard** | Kein Datenzugriff oder nur öffentliche Daten ODER Basisdienste (leicht ersetzbar, minimale Geschäftsauswirkungen) | Bei Vertragsverlängerung |

**Beispiele**: Kritisch — Cloud-Hosting-Anbieter, Lohnbuchhaltungsdienstleister, Backup-Dienst, CRM mit Kundendaten. Wichtig — Marketing-Automatisierungstool, Projektmanagement-SaaS, Kollaborationstools. Standard — Büromateriallieferant, physischer Sicherheitsdienst (kein Datenzugriff).

Zusätzlich sollten mindestens folgende Informationen erfasst werden:

- Name und Kontaktdaten des Lieferanten oder Cloud-Dienstes
- Was sie für uns tun (Servicebeschreibung)
- Welche Daten sie verarbeiten, speichern oder übertragen
- Datenklassifizierungsstufe (Öffentlich, Intern, Vertraulich, Eingeschränkt)
- Ob wir einen Vertrag haben und eine Vertragskopie
- Welche Sicherheitsnachweise wir über ihre Datensicherheit haben (Zertifizierungen, Prüfberichte)
- Datenverarbeitungs- und Speicherorte (Land und Region)
- Vertragsablaufdatum und nächstes Überprüfungsdatum
- Unterauftragsverarbeiter des Lieferanten (soweit bekannt)

## Anforderungen an die Informationssicherheit

Lieferanten und Cloud-Dienstleister sollten relevante Informationssicherheitszertifizierungen besitzen, die die erbrachten Dienstleistungen abdecken. Mindestens sollten sie verfügen über:

- Eine ISO-27001-Zertifizierung, **oder**
- Einen SOC-2-Typ-II-Bericht (aktuell, innerhalb von 12 Monaten)

Für Cloud-Dienstleister, die personenbezogene Daten verarbeiten, wird zusätzlich ISO 27018 (PII-Schutz in öffentlichen Clouds) oder gleichwertiger Nachweis von PII-Schutzkontrollen erwartet.

CSA STAR Level 2-Zertifizierung (ISO 27001 + Cloud Controls Matrix) wird als starker Indikator für cloud-spezifische Sicherheitsreife anerkannt.

Wenn ein Lieferant keine anerkannte Zertifizierung vorweisen kann, sollte die Organisation eine dokumentierte Risikobewertung durchführen und, sofern der Lieferant beauftragt wird, Ausgleichskontrollen implementieren und eine Risikoakzeptanz vom Information Security Manager und Risikoeigentümer einholen.

**Mögliche Ausgleichskontrollen**:

- Erweiterte Vertragsbedingungen mit spezifischen Sicherheitsverpflichtungen (Verschlüsselung, Zugriffsprotokollierung, Vorfallsmeldung)
- Jährlich ausgefüllter Sicherheitsfragebogen mit gegen nachfolgende Ergebnisse verifizierten Antworten
- Eingeschränkter Datenzugriff — Lieferant auf nicht-personenbezogene oder nicht-vertrauliche Daten beschränken
- Prüfungsrechte — Recht zur Durchführung von Sicherheitsaudits oder Penetrationstests (wenn vertraglich erreichbar)
- Treuhandvereinbarungen — Code- oder Daten-Escrow für Geschäftskontinuität
- Anforderungen an Cyber-Haftpflichtversicherung

## Audit und Überprüfung

Jeder Lieferant und Cloud-Dienst unterliegt einem Audit und einer Überprüfung der Datensicherheit gemäss folgendem risikobasierten Zeitplan:

| Lieferantenklassifizierung | Überprüfungshäufigkeit | Überprüfungsumfang |
|---------------------------|------------------------|---------------------|
| **Kritisch** (Zugriff auf vertrauliche/eingeschränkte Daten oder Kernbetrieb) | Jährlich | Vollständige Compliance-Überprüfung, SLA-Performance, Zertifizierungsaktualität, Risikoneubeurteilung |
| **Wichtig** (eingeschränkter Datenzugriff oder unterstützende Dienste) | Alle zwei Jahre | Compliance-Validierung, Vertragsstatus, Zertifizierungsprüfung |
| **Standard** (kein Datenzugriff, Basisdienste) | Bei Vertragsverlängerung | Fortbestehender Geschäftsbedarf, grundlegende Sicherheitsprüfung |

Das Niveau von Audit und Überprüfung basiert auf der Risikoeinstufung des Lieferanten und der Sensitivität der betroffenen Daten.

Cloud-Dienstlieferanten unterliegen denselben Audit- und Überprüfungsanforderungen.

### Cloud-Dienst-Audit-Ansatz

Grosse Cloud-Dienstleister (AWS, Azure, Google Cloud, Microsoft 365, Salesforce usw.) erlauben typischerweise keine direkten Kundenaudits aufgrund von Mehrmandantensicherheits- und betrieblichen Skalierungsbeschränkungen.

**Alternative Sicherungsmechanismen** (anstelle von direkten Audits akzeptiert):

- Unabhängige Drittparteiprüfberichte: SOC 2 Typ II, ISO-27001-Zertifizierung, CSA-STAR-Bescheinigung
- Compliance-Zertifizierungen: ISO 27017, ISO 27018 und branchenspezifische Bescheinigungen, wo anwendbar
- Transparenzberichte: vom Anbieter veröffentlichte Sicherheitsdokumentation, Compliance-Matrizen, Unterauftragsverarbeiter-Listen
- Service-Health-Dashboards: Echtzeit-Serviceverfügbarkeit und Vorfallsoffenlegung

Die Organisation sollte die aktuellsten unabhängigen Prüfberichte (**innerhalb von 12 Monaten**) für jeden kritischen Cloud-Dienst jährlich einholen und überprüfen.

Wenn ein Cloud-Anbieter keine unabhängigen Drittparteiprüfberichte bereitstellt, sollte der Dienst ohne ISB-Genehmigung und dokumentierte Restrisikoacceptanz nicht für vertrauliche oder eingeschränkte Daten verwendet werden.

## Risikomanagement

Jeder Lieferant, der vertrauliche oder personenbezogene Daten verarbeitet, sollte in das Risikoregister aufgenommen und über den Risikomanagementprozess der Organisation verwaltet werden.

Cloud-Dienstrisiken sollten die Bewertung folgender Aspekte umfassen:

- Dienstverfügbarkeit und Geschäftsauswirkungen eines Ausfalls
- Datenresidenz und jurisdiktionelle Exposition
- Anbieterabhängigkeit und Machbarkeit des Ausstiegs
- Konzentrationsrisiko (Abhängigkeit von einem einzelnen Anbieter für kritische Dienste) — wenn ein einzelner Anbieter mehr als 50 % der kritischen Dienste oder mehr als 75 % der vertraulichen Daten hostet, sollte dies im Risikoregister mit einem Mitigationsplan oder akzeptiertem Restrisiko vermerkt werden. Mitigationsoptionen umfassen Mehranbieterdiversifikation, Multi-Region-Deployment beim selben Anbieter und validierte Exit-Strategie
- Unterauftragsverarbeiter-Risiko (nachgelagerte Datenverarbeitung)

## Auswahl von Lieferanten und Cloud-Diensten

Lieferanten und Cloud-Dienste sollten basierend auf ihrer Fähigkeit ausgewählt werden, die Geschäftsanforderungen zu erfüllen.

Vor der Beauftragung eines Lieferanten oder Cloud-Dienstleisters sollte eine Datensicherheits-Due-Diligence durchgeführt werden, die umfasst:

- Ein akzeptables Niveau an Datensicherheit mit identifizierten, aufgezeichneten und verwalteten Risiken
- Angemessene Referenzen von bestehenden Kunden
- Angemessene Zertifizierungen (ISO 27001, SOC 2 Typ II oder Äquivalent — siehe Anforderungen an die Informationssicherheit oben)
- Angemessene Lieferantenvereinbarungen und -verträge, die Datensicherheitsanforderungen enthalten
- Rechts- und regulatorische Compliance, einschliesslich nDSG (revDSG) und DSGVO, wo anwendbar
- Bewertung der Datenverarbeitungs- und Speicherorte anhand der Datenresidenzanforderungen der Organisation
- Verifizierung, dass die Standardbedingungen des Anbieters die Sicherheitsanforderungen der Organisation erfüllen (insbesondere für Cloud-Dienste mit nicht verhandelbaren Vereinbarungen)
- Bewertung der Ausstiegsmöglichkeit: Datenexportfähigkeit, unterstützte Formate, Übergangshilfe und alternative Anbieter

## Verträge, Vereinbarungen und Datenverarbeitungsverträge

Ein geeigneter Vertrag, eine geeignete Vereinbarung und/oder ein Datenverarbeitungsvertrag sollte vorhanden und durchsetzbar sein, bevor ein Lieferant oder Cloud-Dienstleister mit der Verarbeitung, Speicherung oder Übertragung vertraulicher oder personenbezogener Daten beauftragt wird.

Verträge und Vereinbarungen sollten mindestens Folgendes adressieren:

- Beschreibung der verarbeiteten, gespeicherten oder übertragenen Daten
- Informationssicherheitsanforderungen und -verpflichtungen
- Anforderungen an die Vorfallsmeldung (siehe Sicherheits-Incident-Management unten)
- Prüfungsrechte, sofern angemessen, praktikabel und erlaubt (es wird anerkannt, dass grosse Cloud-Anbieter typischerweise keine direkten Audits erlauben; unabhängige Drittpartei-Bescheinigung wird als alternatives Beweismittel akzeptiert)
- Anforderungen an Offenlegung und Genehmigung von Unterauftragsverarbeitern
- Datenrückgabe- und -vernichtungsverpflichtungen bei Vertragsbeendigung
- Service-Level-Vereinbarungen zur Verfügbarkeit, Support-Reaktion und Sicherheitsmetriken
- Austrittsbestimmungen einschliesslich Datenexport, Übergangshilfe und Kündigungsfristen

Alle Richtlinien der Organisation gelten für die Nutzung des Lieferanten oder Cloud-Dienstes.

### Anforderungen an Unterauftragnehmer und Unterauftragsverarbeiter

Die Nutzung von Unterauftragnehmern oder Unterauftragsverarbeitern durch Lieferanten sollte vom ISB genehmigt werden. Unterauftragnehmer und Unterauftragsverarbeiter unterliegen denselben Bedingungen und Sicherheitsanforderungen wie der Lieferant.

**Genehmigungsmodelle**:

- **Spezifische Autorisierung**: Die Organisation genehmigt jeden Unterauftragsverarbeiter einzeln (bevorzugt für kritische Lieferanten, die vertrauliche oder eingeschränkte Daten verarbeiten)
- **Allgemeine Autorisierung mit Benachrichtigung**: Die Organisation erteilt generelle Genehmigung für Unterauftragsverarbeiter, die bestimmte Kriterien erfüllen, mit mindestens 30 Tagen Vorankündigung bei Änderungen (akzeptabel für wichtige Lieferanten)

Cloud-Dienstleister sollten ihre Unterauftragsverarbeiter-Liste offenlegen. Die Organisation sollte über Änderungen an Unterauftragsverarbeitern **mindestens 30 Tage im Voraus** benachrichtigt werden und sollte das Recht behalten, Einwände zu erheben, sofern vertraglich erreichbar. Wenn Einwandsrechte nicht erlangt werden können (wie bei grossen Cloud-Anbietern üblich), sollte diese Einschränkung im Risikoregister als Restrisiko mit Ausgleichskontrollen (Verschlüsselung, Zugriffsüberwachung) dokumentiert werden.

### Datenverarbeitungsverträge (nDSG/DSGVO)

Alle Lieferanten, die im Auftrag der Organisation personenbezogene Daten verarbeiten, sollten einen Datenverarbeitungsvertrag haben, der die Anforderungen des schweizerischen nDSG (revDSG) Art. 9 und, wo anwendbar, DSGVO Art. 28 erfüllt.

Der Datenverarbeitungsvertrag sollte adressieren:

- Gegenstand und Dauer der Verarbeitung
- Art und Zweck der Verarbeitung
- Art der personenbezogenen Daten und Kategorien betroffener Personen
- Pflichten und Rechte des Verantwortlichen
- Anforderungen an die Genehmigung von Unterauftragsverarbeitern (spezifisch oder allgemein mit Benachrichtigung)
- Datensicherheitsmassnahmen (technisch und organisatorisch)
- Unterstützung bei Anfragen zu Betroffenenrechten
- Rückgabe oder Löschung von Daten bei Vertragsbeendigung
- Prüfungs- und Inspektionsrechte

### Grenzüberschreitende Datenübermittlungen

Wenn Lieferanten oder Cloud-Dienstleister personenbezogene Daten ausserhalb der Schweiz verarbeiten oder speichern, sollte die Organisation verifizieren, dass im Zielland angemessener Datenschutz gemäss der Angemessenheitsliste des Schweizerischen Bundesrates (Anhang 1 der Datenschutzverordnung) besteht.

Für Übermittlungen in Länder, die nicht auf der Angemessenheitsliste stehen, sollten geeignete Garantien vorhanden sein:

- Standardvertragsklauseln (SCCs), angepasst für die Schweizer Rechtskonformität, **oder**
- Verbindliche unternehmensinterne Datenschutzregeln (BCRs), genehmigt vom EDÖB, **oder**
- Andere anerkannte Übermittlungsmechanismen

Für Übermittlungen in die Vereinigten Staaten sollte die Organisation verifizieren, dass die empfangende Organisation unter dem Swiss-U.S. Data Privacy Framework zertifiziert ist. Wenn der Anbieter in den USA ansässig ist und dem US CLOUD Act unterliegt, sollte eine Jurisdiktionsrisikobewertung dokumentiert werden, einschliesslich Verschlüsselungs- und Schlüsselverwaltungsvereinbarungen sowie der rechtlichen Herausforderungsverpflichtungen des Anbieters.

## Sicherheits-Incident-Management

Lieferanten und Cloud-Dienstleister sollten über einen Sicherheits-Incident-Management-Prozess verfügen.

Sicherheitsvorfälle bei Lieferanten und Cloud-Diensten, die vertrauliche oder personenbezogene Daten betreffen, sollten der Organisation innerhalb der folgenden Zeitrahmen gemeldet werden:

| Lieferantenklassifizierung | Meldezeitrahmen | Hinweise |
|---------------------------|-----------------|----------|
| **Kritisch** | **12 Stunden** (obligatorisch) | Muss vertraglich zugesichert sein |
| **Wichtig** | **24 Stunden** (Ziel) | Bemühen, wo 12 Stunden nicht erreichbar |
| **Standard** | **72 Stunden** (akzeptabel) | Akzeptabel wenn keine Datenschutzverletzung involviert |

Wenn ein Lieferant sich nicht zum 12-Stunden-Zeitrahmen verpflichten kann, sollte dies als Restrisiko mit Ausgleichskontrollen (häufigere Lieferantenüberprüfungen, erweiterte Überwachung, Backup-Anbieter) dokumentiert werden.

Die Meldung sollte mindestens umfassen:

- Beschreibung des Vorfalls
- Betroffene Systeme und Daten
- Ergriffene Eindämmungsmassnahmen
- Geschätzte Auswirkungen und Lösungszeitrahmen

Sicherheitsvorfälle bei Lieferanten und Cloud-Diensten sollten als Teil des Incident-Management-Prozesses der Organisation gemäss der Incident-Management-Richtlinie behandelt werden.

Wenn ein Lieferantenvorfall eine Datenschutzverletzung mit personenbezogenen Daten umfasst, sollte die Organisation die Meldepflichten gemäss nDSG (Meldung beim EDÖB so bald wie möglich) und, wo anwendbar, DSGVO Art. 33 (Meldung bei der Aufsichtsbehörde innerhalb von 72 Stunden) prüfen.

Wenn angemessen, sollte der Incident-Management-Prozess des Lieferanten in Koordination mit den eigenen Verfahren der Organisation verfolgt werden.

## Vertragsende

Bei Vertragsende sollte der Lieferant oder Cloud-Dienstleister schriftlich bestätigen, dass er seine vertraglichen und gesetzlichen Verpflichtungen zur Vernichtung vertraulicher und personenbezogener Informationen der Organisation erfüllt hat.

Wo angemessen, praktikabel und relevant (unter Berücksichtigung der Einschränkungen bei Cloud-Diensten), sollte Folgendes abgeschlossen werden:

- Alle Organisationsdaten werden in einem nutzbaren Format zurückgegeben oder sicher vernichtet, wie von der Organisation angewiesen
- Eine schriftliche Bestätigung der Datenvernichtung wird bereitgestellt, einschliesslich der verwendeten Methode
- Alle Zugriffe auf Organisationssysteme und -informationen werden widerrufen
- Alle Organisationsassets (physisch und logisch) werden zurückgegeben
- Vernichtungszertifikate werden eingeholt, wenn Daten als vertraulich oder eingeschränkt klassifiziert waren

## Änderungen an Cloud-Dienstlieferanten

Änderungen an einem Cloud-Dienstlieferanten erfordern die formale, schriftliche, dokumentierte Genehmigung des GF oder einer delegierten Autorität.

Änderungen sollten der Change-Management-Richtlinie und dem Change-Management-Prozess folgen.

Änderungen an Cloud-Lieferanten sind bedeutende Änderungen und sollten nicht leichtfertig vorgenommen werden. Solche Änderungen sollten als Projekt mit angemessenen Ressourcen, Risikomanagement, Projektmanagement und Stakeholder-Kommunikation behandelt werden.

Die Organisation sollte eine Exit-Strategie für jeden **kritischen** Cloud-Dienst pflegen, um sicherzustellen, dass ein Übergang oder Ausstieg bei Bedarf kontrolliert durchgeführt werden kann.

**Mindestkomponenten der Exit-Strategie**:

- **Datenexportfähigkeit**: dokumentierter Datenexportprozess und unterstützte Formate (CSV, JSON, API, Backup-Wiederherstellung)
- **Übergangszeitrahmen**: geschätzte Zeit für die Migration zu einem alternativen Anbieter (schlimmsten Fall annehmen: erzwungener Ausstieg)
- **Alternative Anbieter**: mindestens ein vorab identifizierter alternativer Anbieter geprüft
- **Übergangskosten**: geschätzte Kosten (Lizenzen, professionelle Dienstleistungen, Datenmigration)
- **Abhängigkeiten**: identifizierte Integrationen und Abhängigkeiten, die eine Neukonfiguration erfordern würden
- **Exit-Tests**: Verifizierung, dass der Datenexport funktioniert (Test jährlich für kritische Dienste durchgeführt)

Exit-Strategien sollten **jährlich** oder bei Vertragsverlängerung überprüft werden.

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

- **Lieferanten- und Cloud-Dienstregister** — vollständig, aktuell, mit Datenklassifizierung und Überprüfungsdaten; *vierteljährlich überprüft*
- **Unterzeichnete Verträge und Datenverarbeitungsverträge** — für alle Lieferanten, die vertrauliche oder personenbezogene Daten verarbeiten; *Vertragsregister geführt durch [Beschaffung/Recht]*
- **Lieferantenzertifizierungen in der Ablage** — ISO 27001, SOC 2 Typ II, CSA STAR (aktuell innerhalb von 12 Monaten); *jährlich für kritische Lieferanten überprüft*
- **Protokolle der Lieferantenüberprüfungen** und Performance-Berichte — *jährliche Überprüfungen für kritisch, zweijährlich für wichtig*
- **Risikoregister-Einträge** — für Lieferanten, die vertrauliche oder personenbezogene Daten verarbeiten; *vierteljährlich überprüft*
- **Vorfallsmeldungsaufzeichnungen** von Lieferanten — *im Incident-Management-System verfolgt*
- **Datenverarbeitungsverträge** mit nDSG/DSGVO-konformen Bedingungen — *bei Vertragsverlängerung oder regulatorischen Änderungen überprüft*
- **Grenzüberschreitende Transfer-Assessments** — Angemessenheitsverifizierung, SCCs oder DPF-Zertifizierung; *für jeden grenzüberschreitenden Lieferanten/Cloud-Dienst dokumentiert*
- **Exit-Strategie-Dokumentation** für kritische Cloud-Dienste — *jährlich überprüft; Exit-Tests für die wichtigsten kritischen Dienste durchgeführt*
- **Unterauftragsverarbeiter-Register** und Änderungsbenachrichtigungsaufzeichnungen — *gemäss DPA-Bedingungen geführt*
- **Datenvernichtungsbestätigungen** bei Vertragsbeendigung — *Vernichtungszertifikate oder schriftliche Bestätigung 2 Jahre aufbewahrt*
- **Dokumentation des Modells der geteilten Verantwortung** — für jeden kritischen Cloud-Dienst; *jährlich überprüft*

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team sollte die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf, Überprüfungen des Lieferantenregisters, Vertragsaudits, Zertifizierungsprüfungen, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie sollte vom Information Security Manager im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz und Ausgleichskontrollen. Ausnahmen sollten dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterworfen werden, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollten Änderungen in der Lieferantenrisikolandschaft, Entwicklungen im Cloud-Dienstmarkt, regulatorische Änderungen (einschliesslich nDSG, DSGVO und neue Regelwerke), Entwicklungen bei Lieferkettenbedrohungen und Erkenntnisse aus Lieferantenvorfällen berücksichtigen.

---

# Bereiche des ISO-27001-Standards, die abgedeckt werden

Richtlinie für Cloud-Dienste und Lieferantensicherheit — ISO-27001-Kontrollmapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | 5.19 Informationssicherheit in Lieferantenbeziehungen |
| Klausel 7.3 Bewusstsein | 5.20 Adressierung von Informationssicherheit in Lieferantenvereinbarungen |
| Klausel 8.1 Operationale Planung und Kontrolle | 5.21 Verwaltung von Informationssicherheit in der IKT-Lieferkette |
| | 5.22 Überwachung, Überprüfung und Änderungsmanagement von Lieferantendienstleistungen |
| | **5.23 Informationssicherheit bei der Nutzung von Cloud-Diensten** |
| | 5.36 Konformität mit Richtlinien, Regeln und Standards |
| | 6.3 Informationssicherheitsbewusstsein, Ausbildung und Schulung |
| | 6.4 Disziplinarischer Prozess |
| | 8.30 Ausgelagerte Entwicklung |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 9 — Auftragsverarbeitervereinbarungen und Unterauftragsverarbeiteranforderungen |
| Schweizer DSV (Datenschutzverordnung) | Anhang 1 — Angemessenheitsliste für grenzüberschreitende Übermittlungen |
| EU DSGVO (soweit anwendbar) | Art. 28 — Auftragsverarbeiterpflichten; Art. 44–50 — Internationale Übermittlungen |
| Swiss-U.S. Data Privacy Framework | Angemessenheitsmechanismus für Übermittlungen an zertifizierte US-Organisationen |
| ISO/IEC 27001:2022 | Annex A Kontrollen 5.19–5.23 |
| ISO/IEC 27002:2022 | Abschnitte 5.19–5.23 — Implementierungsleitfaden |
| ISO/IEC 27017:2026 | Cloud-Sicherheitskontrollen (informativ) |
| ISO/IEC 27018:2025 | Cloud-PII-Schutzrichtlinien (informativ) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
