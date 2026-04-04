<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.7-DE:operational:OP-POL:a.5.7 -->
**ISMS-OP-POL-A.5.7 — Bedrohungsintelligenz**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Bedrohungsintelligenz |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.7 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.5.7 — Threat intelligence
- ISO/IEC 27002:2022 Section 5.7 — Umsetzungshinweise
- NIST SP 800-150 — Guide to Cyber Threat Information Sharing
- NIST SP 800-53 Rev 5 PM-16 — Threat Awareness Program
- NIST SP 800-53 Rev 5 RA-3 — Risk Assessment
- NIST SP 800-53 Rev 5 SI-5 — Security Alerts, Advisories and Directives
- FIRST TLP v2.0 — Traffic Light Protocol für den Informationsaustausch
- OASIS STIX v2.1 / TAXII v2.1 — Standards für den Austausch von Bedrohungsinformationen

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zur Bedrohungsintelligenz |
|-----------|---------------------------------|
| A.5.1 Richtlinien für Informationssicherheit | Übergeordneter Richtlinienrahmen für Anforderungen an die Bedrohungsintelligenz |
| A.5.24-28 Vorfallsmanagement | Bedrohungsintelligenz verbessert Erkennung, Untersuchung und Reaktion |
| A.5.30 IKT-Bereitschaft für die Geschäftskontinuität | Bedrohungsintelligenz informiert die Kontinuitätsplanung und Bedrohungsvorsorge |
| A.8.7 Schutz vor Malware | Bedrohungsintelligenz liefert IOCs für die Malware-Erkennung |
| A.8.8 Management technischer Schwachstellen | Ausnutzungsintelligenz priorisiert die Schwachstellenbehebung |
| A.8.15 Protokollierung | Protokolle liefern interne Telemetrie für die Bedrohungsanalyse |
| A.8.16 Überwachungsaktivitäten | Bedrohungsintelligenz liefert Erkennungskontext und Korrelationsregeln |
| A.8.23 Web-Filterung | Bedrohungsintelligenz liefert Feeds zu bösartigen Domains und URLs |

**Verwandte interne Richtlinien**:

- Vorfallsmanagement-Richtlinie
- Risikomanagement-Richtlinie
- Schwachstellenmanagement-Richtlinie
- Protokollierungs-Richtlinie
- Überwachungsaktivitäten-Richtlinie (A.8.16)
- Malware-Schutz-Richtlinie
- Richtlinie zur Informationsklassifizierung und -handhabung

---

# Bedrohungsintelligenz-Richtlinie

## Zweck

Der Zweck dieser Richtlinie ist die Festlegung von Anforderungen an die Sammlung, Analyse und Nutzung von Informationen über aktuelle und aufkommende Informationssicherheitsbedrohungen, um eine proaktive Verteidigung zu ermöglichen, Risikomanagement-Entscheidungen zu informieren und die Fähigkeit der Organisation zur Erkennung, Verhinderung und Reaktion auf Sicherheitsvorfälle zu verbessern.

Bedrohungsintelligenz wandelt rohe Bedrohungsdaten in handlungsrelevantes Wissen um. Ohne strukturierte Bedrohungsintelligenz agiert die Organisation reaktiv — sie reagiert auf Vorfälle, nachdem Schaden entstanden ist, anstatt diese zu antizipieren und zu verhindern. Diese Richtlinie stellt sicher, dass die Organisation ein angemessenes Lagebewusstsein über die für ihre Betriebe, Vermögenswerte und ihren Sektor relevante Bedrohungslandschaft aufrechterhält.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG), indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz der Integrität der Verarbeitung personenbezogener Daten umsetzt. Bedrohungsintelligenz trägt zu den nach Art. 8 nDSG geforderten Datensicherheitsmassnahmen bei, indem sie die proaktive Identifikation von Bedrohungen für Systeme ermöglicht, die personenbezogene Daten verarbeiten. Soweit die Organisation Daten natürlicher Personen im EU/EWR-Raum verarbeitet, gelten auch die Anforderungen aus DSGVO Art. 32 für Sicherheitsmassnahmen einschliesslich Bedrohungsüberwachung.

## Geltungsbereich

Alle Aktivitäten im Zusammenhang mit der Sammlung, Analyse, Produktion, Verbreitung und dem Konsum von Bedrohungsintelligenz in der gesamten Organisation.

Dies umfasst:

- Sammlung von Bedrohungsinformationen aus externen und internen Quellen.
- Analyse und Produktion von Intelligenz auf strategischer, taktischer und operativer Ebene.
- Verbreitung von Intelligenz an geeignete Stakeholder.
- Integration von Bedrohungsintelligenz in Risikobeurteilungsprozesse.
- Integration von Bedrohungsintelligenz mit Vorfallsmanagement und Sicherheitsüberwachung.
- Externer Austausch von Bedrohungsintelligenz mit vertrauenswürdigen Partnern und Gemeinschaften.

**Nicht im Geltungsbereich**: Offensive Cyber-Operationen oder Vergeltungsmassnahmen (verboten); Strafverfolgungsermittlungen (Zusammenarbeit unterstützt, nicht durchgeführt); Schwachstellen-Scanning- und Penetrationstestbetrieb (abgedeckt unter A.8.8); Bedrohungsjagd-Verfahren (abgedeckt unter A.8.16); Geheimdienstoperationen ohne Bezug zur Informationssicherheit.

## Grundsatz

Informationen über Informationssicherheitsbedrohungen sollten gesammelt und analysiert werden, um Bedrohungsintelligenz zu produzieren. Bedrohungsintelligenz muss für die spezifische Bedrohungslandschaft der Organisation relevant, technisch korrekt, auf die organisatorischen Vermögenswerte und das Risikoprofil kontextualisiert und handlungsrelevant sein — sie muss klare Hinweise geben, die es der Organisation ermöglichen, identifizierte Bedrohungen zu erkennen, zu verhindern oder darauf zu reagieren.

Die Organisation muss proportional zu ihrer Grösse, Risikoexposition und ihrem Sektor Bedrohungsintelligenz-Fähigkeiten aufrechterhalten. Nicht jede Organisation benötigt ein dediziertes Security Operations Centre (SOC) oder hauptberufliche Bedrohungsanalysten. Was jede Organisation benötigt, ist ein strukturierter, dokumentierter Prozess, um über für ihre Betriebe relevante Bedrohungen informiert zu bleiben und auf diese Informationen zu reagieren.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Bedrohungsintelligenz** | Informationen über aktuelle oder aufkommende Bedrohungen, die gesammelt, verarbeitet und analysiert wurden, um fundierte Sicherheitsentscheidungen und proaktive Verteidigung zu ermöglichen |
| **Strategische Intelligenz** | Hochrangige Intelligenz, die breite Bedrohungstrends, Motivationen von Bedrohungsakteuren und sektorspezifische Risiken adressiert und Führungsentscheidungen sowie langfristige Sicherheitsstrategien unterstützt |
| **Taktische Intelligenz** | Intelligenz, die Taktiken, Techniken und Verfahren (TTPs) der Angreifer beschreibt und die Planung von Sicherheitsoperationen sowie die Defensivkonfiguration unterstützt |
| **Operative Intelligenz** | Handlungsrelevante technische Intelligenz einschliesslich Kompromittierungsindikatoren (IOCs) und Erkennungssignaturen, die unmittelbare Erkennungs- und Reaktionsoperationen unterstützt |
| **Kompromittierungsindikator (IOC)** | Ein beobachtbares Artefakt — wie eine IP-Adresse, ein Domainname, ein Datei-Hash oder eine E-Mail-Adresse — das anzeigt, dass eine Sicherheitsverletzung stattgefunden hat oder stattfindet |
| **Taktiken, Techniken und Verfahren (TTPs)** | Verhaltensmuster und Methoden, die Bedrohungsakteure bei der Durchführung von Angriffen verwenden, dokumentiert in Frameworks wie MITRE ATT&CK |
| **Traffic Light Protocol (TLP)** | Ein Informationsaustausch-Klassifizierungssystem mit Farbcodes (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR) zur Angabe der erlaubten Weitergabegrenzen |
| **STIX (Structured Threat Information eXpression)** | Eine OASIS-Standardsprache und ein Serialisierungsformat für den strukturierten, maschinenlesbaren Austausch von Cyber-Bedrohungsintelligenz |
| **TAXII (Trusted Automated eXchange of Intelligence Information)** | Ein OASIS-Standardanwendungsprotokoll für den automatisierten Austausch von Cyber-Bedrohungsintelligenz über HTTPS |
| **MITRE ATT&CK** | Eine global zugängliche Wissensbasis über Angreifertaktiken und -techniken basierend auf realen Beobachtungen, gepflegt von der MITRE Corporation |
| **Bedrohungsakteur** | Eine Einzelperson, Gruppe oder Organisation, die böswillige Cyber-Aktivitäten mit identifizierbarer Absicht und Fähigkeit durchführt |
| **OSINT (Open-Source Intelligence)** | Bedrohungsintelligenz aus öffentlich zugänglichen Quellen einschliesslich Sicherheitsblogs, Schwachstellendatenbanken, sozialer Medien und öffentlicher Meldungen |

---

## Intelligenztypen und -ebenen

Die Organisation muss Bedrohungsintelligenz auf drei Ebenen produzieren oder konsumieren, von denen jede ein unterschiedliches Publikum und einen unterschiedlichen Zweck bedient. Nicht alle Organisationen werden Intelligenz auf jeder Ebene intern produzieren; der Konsum aus externen Quellen ist akzeptabel, wo interne Produktionskapazität begrenzt ist.

### Strategische Intelligenz

**Zielgruppe**: Geschäftsleitung, ISB, Risikomanagement.
**Zweck**: Geschäftsentscheidungen, Sicherheitsinvestitionen und langfristige Strategie informieren.

Strategische Intelligenz muss folgendes adressieren:

- Die übergreifende Bedrohungslandschaft, die für den Sektor und die Geographie der Organisation relevant ist.
- Motivationen und Fähigkeiten von Bedrohungsakteuren, die auf die Branche der Organisation abzielen.
- Aufkommende Bedrohungstrends und ihre potenziellen geschäftlichen Auswirkungen.
- Regulatorische und geopolitische Entwicklungen, die das Bedrohungsumfeld beeinflussen.
- Vorfälle bei gleichartigen Organisationen und branchenweite Angriffskampagnen.

**Produktionsfrequenz**: Mindestens vierteljährlich oder ausgelöst durch wesentliche Veränderungen der Bedrohungslandschaft. Wo die Organisation keine strategische Intelligenz intern produziert, muss sie mindestens eine Quelle sektorspezifischer strategischer Bedrohungsberichte abonnieren oder darauf zugreifen (z. B. halbjährliche NCSC-Berichte der Schweiz, CERT-Meldungen oder kommerzielle strategische Intelligenzdienstleistungen).

### Taktische Intelligenz

**Zielgruppe**: Sicherheitsbetriebspersonal, IT-Administratoren, Incident-Responder.
**Zweck**: Defensivkonfigurationen, Erkennungsregeln und Sicherheitsarchitektur informieren.

Taktische Intelligenz muss folgendes adressieren:

- Profile von Bedrohungsakteuren und TTPs, die für den Technologie-Stack der Organisation relevant sind.
- Angriffsmuster und Kampagnenanalyse, die auf den Sektor der Organisation abzielen.
- Malware-Familien und ihre Verhaltensmerkmale.
- Social-Engineering-Techniken und Phishing-Kampagnenmuster.
- Empfohlene Defensivmassnahmen und Erkennungsstrategien.

**Produktionsfrequenz**: Mindestens monatlich oder ausgelöst durch aufkommende Bedrohungen. Wo interne Analysekapazität begrenzt ist, muss die Organisation taktische Intelligenz aus mindestens einer strukturierten Quelle konsumieren (z. B. MITRE ATT&CK, Schweizer NCSC-Meldungen, CERT-Feeds oder kommerzielle Bedrohungsberichte).

### Operative Intelligenz

**Zielgruppe**: Technisches Sicherheitspersonal, Systemadministratoren, SOC-Analysten.
**Zweck**: Sofortige Erkennung und Blockierung bekannter Bedrohungen ermöglichen.

Operative Intelligenz muss folgendes umfassen:

- Kompromittierungsindikatoren (IOCs): bösartige IP-Adressen, Domains, URLs, Datei-Hashes, E-Mail-Adressen.
- Malware-Signaturen und Verhaltensindikatoren.
- Erkennungsregeln und YARA-Regeln.
- Sperrlisten für Firewalls, E-Mail-Gateways und Web-Filter.

**Produktionsfrequenz**: Kontinuierlich über automatisierte Feeds mit regelmässiger Analysten-Überprüfung (täglich, wo ein SOC betrieben wird; mindestens wöchentlich für Organisationen ohne dediziertes SOC).

---

## Quellkategorien

Die Organisation muss Bedrohungsintelligenzquellen über mehrere Kategorien hinweg pflegen, um Abhängigkeit von einer einzigen Quelle zu vermeiden und umfassende Abdeckung zu gewährleisten. Die Anzahl und Tiefe der Quellen muss proportional zur Organisationsgrösse und Risikoexposition sein.

### Erforderliche Quellkategorien

| Kategorie | Beschreibung | Beispiele | Mindestanforderung |
|-----------|-------------|----------|--------------------|
| **Behörden / CERT** | Nationale und sektorspezifische CERT-Meldungen und -Warnungen | Schweizer NCSC (ncsc.admin.ch), GovCERT.ch, CERT-EU, US-CERT/CISA | Mindestens ein nationales CERT-Abonnement |
| **Open-Source Intelligence (OSINT)** | Öffentlich verfügbare Bedrohungsdaten, Schwachstellendatenbanken, Sicherheitsforschung | CVE/NVD, AlienVault OTX, Abuse.ch, VirusTotal, Blogs von Sicherheitsforschern | Mindestens zwei OSINT-Feeds |
| **Interne Telemetrie** | Sicherheitsereignisse und -befunde aus den eigenen Systemen der Organisation | [SIEM]-Warnungen, Firewall-Protokolle, E-Mail-Gateway-Berichte, Endpoint-Detection-Warnungen, Post-Mortem-Analysen von Vorfällen | Alle verfügbaren internen Sicherheitstools-Ausgaben |

### Empfohlene Quellkategorien

| Kategorie | Beschreibung | Beispiele | Wann umzusetzen |
|-----------|-------------|----------|--------------------|
| **Kommerzielle Plattformen** | Kuratierte, validierte Bedrohungsintelligenz mit qualitätsgesichertem SLA | [Threat Intelligence Platform], Recorded Future, Mandiant, CrowdStrike | Wenn Budget vorhanden und Bedrohungsexposition die Investition rechtfertigt |
| **Branchenaustausch (ISAC/ISAO)** | Sektorspezifische Bedrohungsintelligenz, die unter Gleichgesinnten geteilt wird | Financial ISAC (FS-ISAC), Health ISAC, sektorspezifische Austauschgruppen | Wenn ein relevantes ISAC/ISAO für den Sektor der Organisation existiert |
| **Sicherheitsmeldungen von Anbietern** | Bedrohungs- und Schwachstelleninformationen von Technologieanbietern | Microsoft Security Response Centre, AWS Security Bulletins, anbieterspezifische Feeds | Für alle kritischen Technologieanbieter im Einsatz |

### Quellenbewertung

Alle Bedrohungsintelligenzquellen müssen vor der Operationalisierung und danach regelmässig bewertet werden. Die Bewertung muss folgendes berücksichtigen:

- **Zuverlässigkeit**: Die Bilanz der Quelle bei der Bereitstellung genauer Informationen.
- **Aktualität**: Wie schnell Informationen nach dem Aufkommen einer Bedrohung verfügbar sind.
- **Relevanz**: Ob die Quelle für den Sektor, die Geographie und den Technologie-Stack der Organisation relevante Bedrohungen abdeckt.
- **Handlungsrelevanz**: Ob die Informationen konkrete Defensivmassnahmen ermöglichen.
- **Falsch-Positiv-Rate**: Der Anteil von Indikatoren, die sich bei der Untersuchung als gutartig erweisen.

Quellen, die dauerhaft ungenaue, irrelevante oder übermässig störende Informationen liefern, müssen ersetzt oder deprioritiert werden. Die Quellenleistung muss mindestens jährlich überprüft werden.

---

## Management von anbieterspezifischer Intelligenz

Wo die Organisation kommerzielle Bedrohungsintelligenz-Dienste oder -Plattformen abonniert, gelten Anforderungen an das Anbietermanagement.

### Anbieterauswahlkriterien

Kommerzielle Bedrohungsintelligenz-Anbieter müssen anhand folgender Kriterien bewertet werden:

| Kriterium | Bewertungsmethode | Akzeptanzschwelle |
|-----------|------------------|-------------------|
| **Intelligenzqualität** | Überprüfung einer 30-Tage-Stichprobe während der Testphase; Analyse der Falsch-Positiv-Rate | <10% Falsch-Positiv-Rate; >90% Relevanz für den Sektor der Organisation |
| **Aktualität** | Zeit vom Aufkommen der Bedrohung bis zur Feed-Verfügbarkeit | <24 Stunden für kritische IOCs; <72 Stunden für taktische Intelligenz |
| **Quellentransparenz** | Anbieter legt Methoden und Quellen der Intelligenzbeschaffung offen | Methodik dokumentiert; primäre Quellen identifiziert |
| **Datenschutz-Compliance** | Verarbeitung personenbezogener Daten in IOCs durch den Anbieter entspricht nDSG/DSGVO | Datenverarbeitungsvertrag vorhanden; dokumentierte Rechtsgrundlage |
| **Plattformintegration** | Kompatibilität mit Sicherheitstools der Organisation (SIEM, EDR, Firewall) | Standardintegrationsprotokolle unterstützt (STIX/TAXII, API, Syslog) |
| **Anbieterstabilität** | Finanzielle Tragfähigkeit, Kundenstamm, Branchenreputation | Etablierter Anbieter mit >2 Jahren Betrieb; Referenzen verfügbar |

### Laufende Überwachung der Anbieterleistung

| Metrik | Ziel | Überprüfungsfrequenz | Verantwortlicher |
|--------|------|---------------------|-----------------|
| **Feed-Verfügbarkeit** | >99% | Monatlich | IT-Betrieb |
| **Falsch-Positiv-Rate** | <10% | Vierteljährlich | ISB |
| **Beitrag echter Positivmeldungen** | >5 validierte Erkennungen pro Quartal | Vierteljährlich | ISB |
| **Aktualität vs. OSINT-Quellen** | Kommerzieller Feed liefert Intelligenz ≥24 Stunden früher als kostenlose Quellen | Vierteljährlich | ISB |
| **Support-Reaktionsfähigkeit** | Support-Anfragen innerhalb des Anbieter-SLA gelöst | Pro Vorfall | IT-Betrieb |
| **Datenschutz-Compliance** | Keine unbefugten Vorfälle bei der Verarbeitung personenbezogener Daten | Kontinuierlich | Datenschutzbeauftragter |

### Vertragsanforderungen für Anbieter

Verträge mit kommerziellen Bedrohungsintelligenz-Anbietern müssen folgendes enthalten:

- **Service Level Agreement (SLA)** mit Angabe von Verfügbarkeit, Feed-Aktualität und Support-Reaktionszeiten
- **Datenverarbeitungsvertrag (DVV)** zur Regelung personenbezogener Daten in IOCs (Auftragsverarbeiterpflichten gemäss nDSG Art. 9 oder DSGVO Art. 28)
- **Bedingungen zum geistigen Eigentum** mit Klarstellung der erlaubten Nutzung der Intelligenz (nur interne Sicherheit; keine Weitergabe ohne Genehmigung)
- **Kündigung und Datenportabilität** — Möglichkeit, Intelligenzdaten bei Vertragsbeendigung in einem Standardformat zu exportieren
- **Vorfallsbenachrichtigung** — Pflicht des Anbieters, die Organisation über jeden Sicherheitsvorfall, der den Intelligenzdienst betrifft, innerhalb von 24 Stunden zu benachrichtigen

### Jährliche Anbieterüberprüfung

Kommerzielle Intelligenzanbieter müssen jährlich überprüft werden:
- Leistung gegenüber SLAs und Qualitätsmetriken
- Kosten-Nutzen-Analyse (erbrachter Wert vs. Abonnementkosten)
- Vergleich mit alternativen Anbietern oder OSINT-Quellen
- Vertragserneuerungsempfehlung mit dokumentierter Begründung

**Überprüfungsdokumentation wird 3 Jahre aufbewahrt; Erneuerungsentscheidungen werden im Anbieter-Risikoregister dokumentiert.**

---

## Sammlung und Analyse

### Sammlungsprozess

Die Organisation muss einen dokumentierten Prozess für die Sammlung von Bedrohungsintelligenz implementieren, der folgendes umfasst:

1. **Automatisierte Sammlung**: Bedrohungs-Feeds müssen wo möglich automatisch aufgenommen werden, unter Verwendung von Standardprotokollen (STIX/TAXII, wo unterstützt) oder anbieterspezifischen APIs. Automatisierte Feeds müssen zur zentralisierten Verarbeitung an [SIEM] oder [Threat Intelligence Platform] gerichtet werden.

2. **Manuelle Sammlung**: Sicherheitspersonal muss nach einem definierten Zeitplan Meldungsquellen, Sicherheitsnachrichten und Community-Foren überprüfen. Ergebnisse der manuellen Sammlung müssen dokumentiert und in das Bedrohungsintelligenz-Register eingetragen werden.

3. **Interne Sammlung**: Sicherheitsereignisse, Vorfall-Befunde und forensische Analyseergebnisse müssen als interne Bedrohungsintelligenz erfasst werden. Post-Incident-Reviews müssen IOCs und beobachtete TTPs explizit identifizieren und aufzeichnen.

4. **Datenschutz**: Alle gesammelten Intelligenzen müssen den geltenden Datenschutzanforderungen entsprechen. In der Bedrohungsintelligenz enthaltene personenbezogene Daten (z. B. E-Mail-Adressen in Phishing-Indikatoren) dürfen nur für das berechtigte Interesse der Informationssicherheit verarbeitet werden und müssen nur so lange aufbewahrt werden, wie der Indikator operativ relevant ist.

### Analyseprozess

Rohe Bedrohungsdaten müssen vor der Verbreitung analysiert werden, um Qualität und Relevanz zu gewährleisten. Die Analyse muss:

- Informationen nach Möglichkeit durch mehrere Quellen **validieren**.
- Bedrohungen gegen die spezifischen Vermögenswerte, den Technologie-Stack und das Risikoprofil der Organisation **kontextualisieren**.
- Die Wahrscheinlichkeit und den potenziellen Einfluss identifizierter Bedrohungen auf die Organisation **bewerten**.
- Bedrohungen nach Relevanz, Schweregrad und Exposition der Organisation **priorisieren**.
- Handlungsrelevante Empfehlungen oder Erkennungshinweise **produzieren**.

Wo die Organisation keine dedizierten Bedrohungsanalysten hat, muss die Analyseverantwortung dem ISB oder designierten Sicherheitspersonal zugewiesen werden. Die Analyse muss für kleinere Organisationen keine Vollzeitfunktion sein, aber es muss eine dokumentierte, wiederkehrende Aktivität mit klarer Verantwortung sein.

### Qualitätsanforderungen

Alle Bedrohungsintelligenz — ob intern produziert oder aus externen Quellen konsumiert — muss folgende Qualitätskriterien erfüllen, bevor sie genutzt wird:

- **Relevant**: Auf die Bedrohungslandschaft, den Sektor und die Technologieumgebung der Organisation anwendbar.
- **Korrekt**: Durch Bestätigung oder Zuverlässigkeitsbewertung der Quelle validiert.
- **Aktuell**: Zeitgemäss und innerhalb eines Zeitrahmens geliefert, der effektives Handeln ermöglicht.
- **Handlungsrelevant**: Begleitet von klaren Hinweisen zu Erkennungs-, Präventions- oder Reaktionsmassnahmen.

Intelligenz, die diese Kriterien nicht erfüllt, muss gekennzeichnet, untersucht oder verworfen werden. Quellenbeurteilungsunterlagen müssen Qualitätsprobleme dokumentieren.

---

## Lebenszyklusmanagement von Intelligenzdaten

### Aufbewahrungsanforderungen

Bedrohungsintelligenz-Daten müssen gemäss betrieblichen und regulatorischen Anforderungen aufbewahrt werden:

| Intelligenztyp | Aufbewahrungsfrist | Begründung |
|----------------|-------------------|------------|
| **Operative IOCs** (in aktiver Erkennung) | Solange die Bedrohung relevant bleibt; mindestens 90 Tage | Aktive Erkennung erfordert aktuelle Indikatoren |
| **Historische IOCs** (nicht mehr aktiv) | 12 Monate nach Deaktivierung | Historischer Kontext für Vorfallsuntersuchung; Trendanalyse |
| **Strategische und taktische Intelligenzberichte** | 3 Jahre | Audit-Trail für Risikobeurteilung; Reifegradbeurteilung des Programms; historischer Kontext |
| **Interne Intelligenz aus Vorfällen** | Gemäss Vorfallsaufbewahrungsplan (typischerweise 5 Jahre) | Regulatorische Compliance; potenzielle Rechtsverfahren |
| **Quellenbeurteilungsunterlagen** | 3 Jahre | Audit-Trail für Quellenauswahlentscheidungen |
| **Vereinbarungen zum Informationsaustausch** | 7 Jahre nach Beendigung | Gesetzliche Aufbewahrungsanforderungen |

### IOC-Lebenszyklusmanagement

Kompromittierungsindikatoren, die in Erkennungssystemen eingesetzt werden, müssen durch einen Lebenszyklusprozess verwaltet werden:

1. **Aufnahme** — IOC von Quelle erhalten, validiert und klassifiziert (TLP, Bedrohungstyp, Schweregrad)
2. **Bereitstellung** — IOC in relevante Erkennungssysteme eingesetzt (SIEM, EDR, Firewall, Web-Filter)
3. **Aktive Überwachung** — IOC generiert Warnungen bei Übereinstimmung; Warnungen werden priorisiert und untersucht
4. **Überprüfung** — IOCs werden vierteljährlich auf anhaltende Relevanz überprüft:
   - Wurde der Indikator in Warnungen beobachtet? (Aktiv vs. inaktiv)
   - Ist die Bedrohung noch aktuell? (Intelligenquelle aktualisiert oder veraltet?)
   - Ist die Falsch-Positiv-Rate akzeptabel? (Bei >20% Falsch-Positiven, Entfernung erwägen)
5. **Deaktivierung** — IOC wird aus Erkennungssystemen entfernt, wenn nicht mehr relevant
6. **Archivierung** — IOC wird zur Trendanalyse und Vorfallsuntersuchungsreferenz in historische Datenbank verschoben
7. **Löschung** — IOC wird nach Ablauf der Aufbewahrungsfrist dauerhaft gelöscht

**Automatisierung**: Wo technisch machbar, sollte das IOC-Lebenszyklusmanagement durch die Threat-Intelligence-Plattform (TIP) oder SIEM-Funktionalität automatisiert werden. Manuelles IOC-Management ist für Organisationen ohne TIP-Fähigkeit akzeptabel.

### Datenschutzüberlegungen

Wo Bedrohungsintelligenz personenbezogene Daten enthält (z. B. E-Mail-Adressen in Phishing-Indikatoren, IP-Adressen kompromittierter Systeme):

- **Rechtsgrundlage**: Verarbeitung gerechtfertigt unter berechtigtem Interesse für die Informationssicherheit (nDSG Art. 6 Abs. 2; DSGVO Art. 6 Abs. 1 lit. f, sofern anwendbar)
- **Zweckbindung**: Personenbezogene Daten in IOCs werden nur für Bedrohungserkennung und Vorfallsreaktion verarbeitet; nicht für andere Zwecke verwendet
- **Minimierung der Aufbewahrung**: Personenbezogene Daten werden nur so lange wie betrieblich notwendig aufbewahrt; IOCs, die personenbezogene Daten enthalten, werden für die Lebenszyklusüberprüfung priorisiert
- **Zugriffsbeschränkung**: Intelligenzdatenbanken mit personenbezogenen Daten sind auf autorisiertes Sicherheitspersonal beschränkt

**DSFA**: Wenn die Verarbeitung von Bedrohungsintelligenz eine grossmassstäbliche systematische Überwachung oder besondere Kategorien personenbezogener Daten umfasst, kann eine Datenschutz-Folgenabschätzung gemäss nDSG Art. 22 erforderlich sein.

---

## Verbreitung und Austausch

### Interne Verbreitung

Bedrohungsintelligenz muss je nach Intelligenztyp an das geeignete Publikum verteilt werden:

| Intelligenztyp | Empfänger | Format | Frequenz |
|----------------|-----------|--------|----------|
| **Strategisch** | Geschäftsleitung, ISB, Risikomanagement | Briefingdokumente, Quartalsberichte | Vierteljährlich oder bei wesentlichen Änderungen |
| **Taktisch** | IT-Betrieb, Sicherheitsteam, Systemadministratoren | Meldungen, TTP-Zusammenfassungen, Defensivempfehlungen | Monatlich oder bei aufkommenden Bedrohungen |
| **Operativ** | [SIEM] / Sicherheitstools, SOC-Analysten, IT-Administratoren | IOC-Feeds, Erkennungsregeln, Sperrlisten | Kontinuierlich (automatisiert) oder wöchentlich (manuell) |

### Eskalation bei kritischen Bedrohungen

Wenn Bedrohungsintelligenz eine unmittelbare oder aktive Bedrohung identifiziert, die auf die Organisation oder ihren Sektor abzielt:

1. **Sofortige Benachrichtigung** des ISB (innerhalb von 1 Stunde nach Identifikation).
2. **Schnelle Bewertung** der organisatorischen Exposition (innerhalb von 4 Stunden).
3. **Notfall-Briefing** für betroffene Stakeholder mit empfohlenen Massnahmen.
4. **Aktivierung der Vorfallsreaktion**, wenn die Bedrohungsbeurteilung dies rechtfertigt (gemäss Vorfallsmanagement-Richtlinie).

### Externer Austausch

Die Organisation kann Bedrohungsintelligenz mit vertrauenswürdigen externen Parteien vorbehaltlich folgender Kontrollen austauschen:

- **TLP-Klassifizierung**: Alle geteilten Intelligenzen müssen mit dem Traffic Light Protocol v2.0 (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR) klassifiziert werden. Der Austausch darf die vom Urheber zugewiesene TLP-Bezeichnung nicht überschreiten.
- **Austauschvereinbarungen**: Formelle Vereinbarungen (NDA, Informationsaustauschvereinbarung oder Mitgliedschaftsbedingungen) müssen vor dem Austausch mit externen Parteien vorhanden sein.
- **Datenschutz**: Geteilte Intelligenz darf keine personenbezogenen Daten enthalten, die über das für die Bedrohungserkennung Notwendige hinausgehen (z. B. IOCs). Wo personenbezogene Daten geteilt werden, muss eine Rechtsgrundlage gemäss nDSG festgelegt werden.
- **Behördliche Meldung**: Wo die schweizerischen NCSC-Meldepflichten gelten (Betreiber kritischer Infrastruktur — ISG Art. 74b), muss die Organisation relevante Cyber-Vorfälle innerhalb von 24 Stunden gemäss geltenden Anforderungen an das NCSC melden.

### Empfang externer Intelligenz

Beim Empfang von Bedrohungsintelligenz aus externen Quellen:

- **TLP-Kennzeichnungen respektieren**: Mit TLP-Bezeichnungen empfangene Intelligenz darf nicht über die erlaubten Grenzen hinaus geteilt werden.
- **Vor der Nutzung validieren**: Extern empfangene IOCs müssen vor der Bereitstellung in Sperr- oder Erkennungssystemen gegen die Umgebung der Organisation validiert werden, um Falsch-Positivmeldungen zu minimieren.
- **Empfang bestätigen**: Wo der Austausch bidirektional ist, muss die Organisation den Empfang bestätigen und auf Anfrage Rückmeldung zur Intelligenznutzlichkeit geben.

---

## Integration in die Risikobeurteilung

Bedrohungsintelligenz muss den Risikobeurteilungsprozess der Organisation gemäss ISO 27001:2022 Klausel 6.1 informieren. Diese Integration ist obligatorisch — Bedrohungsintelligenz, die keine Risikoentscheidungen beeinflusst, bietet begrenzten Wert.

### Erforderliche Integrationspunkte

- **Wahrscheinlichkeitsbewertung**: Bedrohungsintelligenz über aktive Kampagnen, Ausnutzungsaktivitäten und die Ausrichtung von Bedrohungsakteuren muss die Wahrscheinlichkeitsschätzungen für identifizierte Risiken informieren.
- **Auswirkungsbewertung**: Intelligenz über Angriffstechniken und beobachtete Konsequenzen in gleichartigen Organisationen muss die Auswirkungsbewertungen informieren.
- **Risikoregister-Aktualisierungen**: Wenn Bedrohungsintelligenz neue Bedrohungen oder Änderungen an bestehenden Bedrohungen identifiziert, muss das Risikoregister entsprechend aktualisiert werden. Jede Aktualisierung muss auf die unterstützende Bedrohungsintelligenzquelle verweisen.
- **Kontrollwirksamkeit**: Bedrohungsintelligenz über umgangene oder unwirksame Kontrollen, die in der freien Natur beobachtet wurden, muss eine Neubewertung der Kontrollwirksamkeit der Organisation auslösen.

### Prozess

1. Der ISB oder designiertes Sicherheitspersonal muss strategische und taktische Bedrohungsintelligenz-Outputs mindestens vierteljährlich gegen das aktuelle Risikoregister überprüfen.
2. Durch Intelligenzanalyse identifizierte neue Bedrohungen müssen dem Risikomanagement zur formellen Risikobeurteilung vorgelegt werden.
3. Änderungen der Bedrohungswahrscheinlichkeit oder -auswirkung basierend auf Intelligenz müssen mit nachverfolgbaren Verweisen auf unterstützende Intelligenzberichte dokumentiert werden.
4. Durch Bedrohungsintelligenz beeinflusste Risikobehandlungsentscheidungen müssen im Risikoregister festgehalten werden.

### Datenschutz- und Vertraulichkeitsbedrohungsbewertung

Wo die Organisation personenbezogene Daten verarbeitet, die dem nDSG oder der DSGVO unterliegen, muss die Bedrohungsintelligenz spezifisch Bedrohungen für die Datenvertraulichkeit und den Datenschutz adressieren:

| Bedrohungskategorie | Datenschutzauswirkung | Intelligenzanforderungen |
|--------------------|----------------------|--------------------------|
| **Datenexfiltration** | Unbefugte Weitergabe personenbezogener Daten | IOCs für Datendiebstahl-Malware, Exfiltrationstechniken (DNS-Tunneling, Steganographie), von Angreifern genutzte Infrastruktur für Datenstaging |
| **Credential-Diebstahl** | Unbefugter Zugriff auf Systeme, die personenbezogene Daten verarbeiten | Phishing-Kampagnenindikatoren, Signaturen für Credential-stehlende Malware, kompromittierte Credential-Datenbanken |
| **Insider-Bedrohungen** | Absichtlicher oder versehentlicher Datenmissbrauch | Verhaltens-Indikatoren, Muster des Missbrauchs von privilegiertem Zugriff, Erkennung von Datenzugriffsanomalien |
| **Sicherheitsverletzungen bei Dritten** | Kompromittierung personenbezogener Daten über Auftragsverarbeiter/Anbieter | Intelligenz über kompromittierte Dienstleister, kompromittierte SaaS-Plattformen, Supply-Chain-Datenlecks |

**Auswirkung auf das Risikoregister:**
- Risiken im Zusammenhang mit der Verarbeitung personenbezogener Daten (z. B. "R-DATA-01: Unbefugter Zugriff auf personenbezogene Kundendaten") müssen vierteljährlich gegen Bedrohungsintelligenz-Befunde überprüft werden
- Bedrohungsintelligenz, die auf eine verstärkte Ausrichtung auf Datenverantwortliche im Sektor der Organisation hinweist, muss eine Neubewertung der Angemessenheit der Datenschutzkontrollen auslösen
- Erkennungsregeln für Datenexfiltrationsversuche müssen basierend auf beobachteten Angreifertechniken aktualisiert werden

---

## Integration in das Vorfallsmanagement

Bedrohungsintelligenz muss die Erkennung, Untersuchung und Reaktion auf Vorfälle gemäss den Kontrollen A.5.24-28 verbessern.

### Verbesserung der Erkennung

- IOCs aus Bedrohungsintelligenzquellen müssen in Erkennungssystemen ([SIEM], [EDR], E-Mail-Gateway, Web-Filter) eingesetzt werden, um automatische Warnungen zu ermöglichen.
- TTPs von Bedrohungsakteuren aus taktischer Intelligenz müssen wo möglich in Erkennungsregeln oder Überwachungsanwendungsfälle übersetzt werden.
- Die Wirksamkeit von Erkennungsregeln muss regelmässig überprüft und Regeln basierend auf sich entwickelnder Intelligenz aktualisiert werden.

### Untersuchungsunterstützung

- Wenn ein Sicherheitsvorfall eintritt, muss verfügbare Bedrohungsintelligenz nach verwandten Indikatoren, bekannten Bedrohungsakteurprofilen und Angriffsmustern-Kontext abgefragt werden.
- Bedrohungsintelligenz-Kontext muss in Vorfallsuntersuchungsunterlagen aufgenommen werden, um die Ursachenanalyse und die Attributionsbewertung zu unterstützen.

### Post-Incident-Feedback

- Vorfallsbefunde — einschliesslich neu entdeckter IOCs, beobachteter TTPs und Angreiferinfrastruktur — müssen als interne Bedrohungsintelligenz erfasst werden.
- Post-Incident-Reviews müssen bewerten, ob bestehende Bedrohungsintelligenzquellen ausreichende Frühwarnung gaben und ob Erkennungsregeln wie erwartet funktionierten.
- Lessons Learned müssen in Quellenbeurteilung, Tuning von Erkennungsregeln und Risikoregister-Aktualisierungen einfliessen.

---

## Integration in die Sicherheitsüberwachung

Bedrohungsintelligenz muss mit Sicherheitsüberwachungsfähigkeiten integriert werden, um die Erkennungseffektivität zu verbessern.

### Integrationsanforderungen

- **[SIEM]-Integration**: Operative IOCs müssen für die Korrelation mit internen Sicherheitsereignissen in das [SIEM] aufgenommen werden. Wo die automatische Aufnahme nicht möglich ist, muss die manuelle IOC-Eingabe nach einem definierten Zeitplan durchgeführt werden.
- **Endpoint-Erkennung**: Wo [EDR] oder Endpoint-Schutzplattformen die Integration von Bedrohungsintelligenz-Feeds unterstützen, müssen relevante IOCs in Endpoint-Erkennungssystemen eingesetzt werden.
- **E-Mail-Sicherheit**: Bekannte Phishing-Domains, bösartige Absenderadressen und Anhang-Hashes müssen in E-Mail-Gateway-Filterregeln eingesetzt werden.
- **Web-Filterung**: Bösartige Domains und URLs aus Bedrohungsintelligenz müssen in Web-Filterungs- oder DNS-Sicherheitssystemen eingesetzt werden.
- **Firewall-Regeln**: Bekannte bösartige IP-Adressen und Netzwerkindikatoren müssen vorbehaltlich der Validierung von Falsch-Positivmeldungen in Perimeter- und internen Firewall-Sperrlisten eingesetzt werden.

### Überwachungseffektivität

Die Organisation muss folgendes verfolgen, um die Integrationseffektivität zu bewerten:

- Anzahl der aus Bedrohungsintelligenz-Indikatoren generierten Warnungen.
- Bestätigte echte Positivrate für aus Bedrohungsintelligenz stammende Warnungen.
- Zeit vom Intelligenzempfang bis zur Bereitstellung von Erkennungsregeln.
- Abdeckungslücken zwischen Bedrohungsintelligenz und Überwachungsfähigkeiten.

---

## Integration in Verfügbarkeit und Geschäftskontinuität

Bedrohungsintelligenz muss die Planung der Geschäftskontinuität und den Schutz der Dienstverfügbarkeit gemäss den Kontrollen A.5.29-30 informieren.

### Überwachung von Verfügbarkeitsbedrohungen

Die folgenden Bedrohungskategorien müssen aufgrund ihrer potenziellen Auswirkungen auf die Dienstverfügbarkeit für die Erkennung und Reaktion priorisiert werden:

| Bedrohungstyp | Verfügbarkeitsauswirkung | Erkennungspriorität | Reaktionsmassnahme |
|---------------|------------------------|--------------------|--------------------|
| **Distributed Denial of Service (DDoS)** | Direkte Dienststörung | Hoch | DDoS-Minderungsdienst aktivieren; Datenverkehrsfilterung; Koordination mit vorgelagerten ISP |
| **Ransomware** | Daten- und Systemunverfügbarkeit | Kritisch | Sofortige Eindämmung; Backup-Wiederherstellung; keine Lösegeldzahlung |
| **Wiper-Malware** | Permanente Datenzerstörung | Kritisch | Sofortige Isolierung; forensische Sicherung; Aktivierung der Notfallwiederherstellung |
| **Supply-Chain-Angriffe** | Störung von Drittanbieter-Abhängigkeiten | Hoch | Bewertung alternativer Anbieter; Dienstverschlechterungsverfahren |
| **Ressourcenerschöpfungsangriffe** | Kapazitätsdegradation | Mittel | Kapazitätsskalierung; Rate-Limiting; Blockierung bösartiger Akteure |

### Eingaben für die Kontinuitätsplanung

Bedrohungsintelligenz muss folgende Eingaben für die Geschäftskontinuitäts- und Notfallwiederherstellungsplanung liefern:

1. **Bedrohungsszenarien** — Die jährliche Überprüfung plausibler Bedrohungsszenarien (Ransomware, DDoS, Datenzerstörung) basierend auf beobachteten Branchenvorfällen muss die Geschäftsauswirkungsanalyse (BIA) und Wiederherstellungsstrategien informieren.

2. **Validierung der Wiederherstellungszeitziels (RTO)** — Beobachtete Angriffsgeschwindigkeiten in der realen Welt (z. B. Ransomware-Verschlüsselungszeit, DDoS-Angriffsdauer) müssen mit RTO-Annahmen verglichen werden, um die Wiederherstellbarkeit zu validieren.

3. **Risiken von Drittanbieter-Abhängigkeiten** — Intelligenz über Supply-Chain-Angriffe oder Vorfälle bei Cloud-Dienstleistern muss Überprüfungen von Anbieter-Notfallplänen und Bereitschaft alternativer Anbieter auslösen.

4. **Tabletop-Übungsszenarien** — Jährliche Geschäftskontinuitätsübungen müssen realistische Bedrohungsszenarien einbeziehen, die aus aktueller Bedrohungsintelligenz abgeleitet werden.

**Integrationsprozess:**
- Vierteljährliche Überprüfung verfügbarkeitsbeeinträchtigender Bedrohungen durch ISB und Business Continuity Manager
- Jährliche Aktualisierung der BIA-Bedrohungsannahmen basierend auf Intelligenzbefunden
- Aktualisierungen des Geschäftskontinuitätsplans mit Verweis auf unterstützende Bedrohungsintelligenz dokumentiert

---

## Effektivitätsmessung

Die Organisation muss die Effektivität des Bedrohungsintelligenz-Programms messen, um Investitionen zu rechtfertigen, Verbesserungsmöglichkeiten zu identifizieren und Stakeholdern Wert zu demonstrieren.

### Metriken

Die folgenden Metriken müssen dem ISB vierteljährlich gemeldet werden:

| Metrik | Ziel | Roter Schwellenwert |
|--------|------|---------------------|
| Aktive Bedrohungsintelligenzquellen | Gemäss Mindestanforderungen oben | Unter Minimum in einer erforderlichen Kategorie |
| Abgeschlossene Quellenbeurteilungsüberprüfungen | 100% jährlich | <80% der überprüften Quellen |
| Durch Bedrohungsintelligenz informierte Risikoregister-Aktualisierungen | Mindestens 1 pro Quartal | 0 Aktualisierungen in einem Quartal |
| IOC-Bereitstellung in Erkennungssystemen | Innerhalb von 24 Stunden nach validiertem Empfang | >72 Stunden durchschnittliche Bereitstellungszeit |
| Aus Bedrohungsintelligenz stammende Warnungen (echte Positivrate) | >70% | <50% |
| Strategische Intelligenzbriefings für die Geschäftsleitung | Mindestens vierteljährlich | >1 Quartal verpasst |
| Abgeschlossenes Post-Incident-Bedrohungsintelligenz-Feedback | 100% der P1/P2-Vorfälle | <80% der P1/P2-Vorfälle |

### Jährliche Programmüberprüfung

Der ISB muss eine jährliche Überprüfung des Bedrohungsintelligenz-Programms durchführen:

- Adäquatheit und Leistung des Quell-Portfolios.
- Qualität und Aktualität der Intelligenzproduktion.
- Integrationseffektivität mit Risikobeurteilung, Vorfallsmanagement und Überwachung.
- Ressourcenadäquatheit (Personal, Tools, Budget).
- Reifegradbewertung gegenüber dem Zielreifegrad der Organisation.
- Empfehlungen zur Programmverbesserung.

---

## Tests und Validierung

Die Organisation muss die Effektivität der Bedrohungsintelligenz testen, um zu validieren, dass Intelligenzquellen und Erkennungsintegrationen wie beabsichtigt funktionieren.

### Intelligenzerkennungstests

| Testtyp | Frequenz | Methode | Erfolgskriterien | Verantwortlicher |
|---------|----------|---------|-----------------|-----------------|
| **IOC-Erkennungsvalidierung** | Vierteljährlich | Test-IOCs (nicht bösartige Simulation) in Sicherheitstools einsetzen; Warnungsgenerierung verifizieren | >90% der eingesetzten IOCs lösen erwartete Warnungen aus | IT-Sicherheit |
| **Feed-Integritätsprüfung** | Monatlich | Automatische Aufnahme von Feeds überprüfen; auf veraltete Daten prüfen | Alle Feeds innerhalb von 24 Stunden aktualisiert; keine Aufnahmefehler älter als 48 Stunden | IT-Betrieb |
| **TTP-Erkennungsabdeckung** | Halbjährlich | Erkennungsregeln der Organisation auf MITRE ATT&CK abbilden; Abdeckungslücken identifizieren | >70% der für das Bedrohungsprofil der Organisation relevanten MITRE ATT&CK-Techniken durch Erkennungsregeln abgedeckt | ISB |
| **Falsch-Positiv-Analyse** | Vierteljährlich | 20 aus Bedrohungsintelligenz stammende Warnungen stichprobenweise untersuchen; echte Positivrate ermitteln | >70% echte Positivrate | IT-Sicherheit |
| **Eskalationspfadtest** | Jährlich | Kritisches Bedrohungsszenario simulieren; Eskalation zu ISB und Geschäftsleitung testen | Eskalation innerhalb von 1 Stunde abgeschlossen; alle Stakeholder einbezogen | ISB |
| **Quellennutzenbewertung** | Jährlich | Für jede Intelligenzquelle handlungsrelevante Intelligenz der letzten 12 Monate identifizieren | Jede Quelle produzierte ≥1 handlungsrelevantes Intelligenzelement oder dokumentierten Grund für Beibehaltung | ISB |

### Purple-Team-Übungen

Wo Ressourcen vorhanden sind, sollte die Organisation jährliche Purple-Team-Übungen durchführen:
- **Red Team** simuliert Angriff basierend auf aktueller Bedrohungsintelligenz (realistische Angreifer-TTPs)
- **Blue Team** (Erkennung und Reaktion) versucht mit bedrohungsintelligenz-informierten Erkennungen zu erkennen und zu reagieren
- **Nachbesprechung** identifiziert Lücken in Intelligenzabdeckung, Erkennungsregeln oder Reaktionsverfahren
- **Verbesserungsmassnahmen** dokumentiert und durch Korrekturmassnahmenprozess verfolgt

**Für Organisationen ohne Purple-Team-Fähigkeit:** Tabletop-Übungen, die bedrohungsintelligenz-gesteuerte Vorfallsszenarien simulieren, dienen als akzeptable Alternative.

### Testdokumentation

Alle Testaktivitäten müssen dokumentiert werden mit:
- Testdatum, Umfang und Teilnehmer
- Testergebnisse (bestanden/nicht bestanden, erreichte Metriken, identifizierte Lücken)
- Zugewiesene Korrekturmassnahmen (wo Lücken identifiziert)
- Nachfolgevalidierung von Korrekturmassnahmen

Testdokumentation 3 Jahre aufbewahrt; im jährlichen Programmüberprüfungsbericht aufgeführt.

---

## Bedrohungsintelligenz-Austausch mit Kunden (falls zutreffend)

*Hinweis: Dieser Abschnitt gilt nur, wenn die Organisation Managed Security Services anbietet oder vertragliche Verpflichtungen zum Austausch von Bedrohungsintelligenz mit Kunden hat.*

### Kundenbezogene Intelligenzlieferungen

Wo die Organisation vertraglich zugesagt hat, Kunden Bedrohungsintelligenz zu liefern:

| Lieferung | Frequenz | Inhalt | Zielgruppe |
|-----------|----------|--------|------------|
| **Bedrohungsbriefing** | Vierteljährlich | Strategische Intelligenzzusammenfassung relevant für den Sektor des Kunden; aufkommende Bedrohungen; empfohlene Massnahmen | Sicherheitsführung des Kunden |
| **IOC-Feed** | Kontinuierlich oder täglich | Operative IOCs relevant für die Kundenumgebung | Kunden-SOC oder IT-Sicherheit |
| **Vorfallsbenachrichtigungen** | Sofort | Benachrichtigung über Bedrohungen, die aktiv auf den Sektor oder Technologie-Stack des Kunden abzielen | Sicherheitskontakt des Kunden |
| **Jährlicher Bedrohungsbericht** | Jährlich | Umfassende Analyse der Bedrohungslandschaft; Angriffstrenddaten; sektorspezifische Bedrohungsakteurprofile | Geschäftsleitung des Kunden |

### Kundespezifische Intelligenz

Für Kunden mit dedizierten Servicevereinbarungen muss die Organisation:
- Intelligenz auf den spezifischen Technologie-Stack, die Geographie und das Bedrohungsprofil des Kunden zuschneiden
- Handlungsrelevante Empfehlungen spezifisch für die Kundenumgebung bereitstellen
- Koordination mit dem Sicherheitsteam des Kunden bei der Intelligenzanwendung
- Vertraulichkeit der kundspezifischen Intelligenz wahren (nicht mit anderen Kunden geteilt, es sei denn anonymisiert)

### Feedback-Schleife mit Kunden

- Kunden werden eingeladen, Rückmeldung zu Intelligenznutzlichkeit und Relevanz zu geben
- Kundenfeedback in vierteljährliche Intelligenzprogrammüberprüfung einbezogen
- Anpassungen an Lieferungen basierend auf Kundenbedürfnissen und Feedback

**Nachweis**: Kundenbezogene Intelligenzlieferungen mit Lieferbestätigung dokumentiert; Kundenfeedback aufgezeichnet; Service-Level-Compliance verfolgt.

---

## KMU-Skalierungshinweise

Nicht alle Organisationen haben dedizierte Bedrohungsintelligenz-Teams oder SOC-Fähigkeiten. Die folgenden Hinweise helfen kleineren Organisationen, Bedrohungsintelligenz proportional zu ihren Ressourcen umzusetzen:

### Mindestzweckprogramm (Organisationen ohne dediziertes Sicherheitspersonal)

- Schweizer NCSC-Warnungen und mindestens einen relevanten CERT-Feed abonnieren.
- Mindestens zwei kostenlose OSINT-Bedrohungs-Feeds abonnieren (z. B. Abuse.ch, AlienVault OTX).
- Eine Einzelperson (ISB, IT-Manager oder designierter Sicherheitskontakt) mit der Verantwortung für die wöchentliche Überprüfung von Meldungen beauftragen.
- Strategische Berichte zur Bedrohungslandschaft vom Schweizer NCSC halbjährlich überprüfen.
- Sicherstellung, dass kritische Sicherheitsmeldungen von Anbietern überwacht und befolgt werden.
- Bedrohungsintelligenz-Befunde in einem einfachen Register dokumentieren (Tabellenkalkulation ist akzeptabel).
- Register vierteljährlich gegen das Risikoregister überprüfen.

### Wachstumspfad (Organisationen mit aufkommender Sicherheitsfunktion)

- Kommerzielle Bedrohungsintelligenz-Feeds hinzufügen, die für Sektor und Technologie-Stack relevant sind.
- Automatische IOC-Aufnahme in [SIEM]- oder Firewall-Systeme implementieren.
- Interne taktische Intelligenz aus Post-Mortem-Analysen von Vorfällen beginnen zu produzieren.
- Relevanten Informationsaustauschgemeinschaften (ISAC/ISAO) beitreten, wo verfügbar.
- Formellen Verbreitungsplan und Stakeholder-Briefings etablieren.
- Beobachtete Bedrohungen für strukturierte Analyse auf das MITRE ATT&CK-Framework abbilden.

### Reifes Programm (Organisationen mit dediziertem Sicherheitsbetrieb)

- Dedizierte [Threat Intelligence Platform] für Sammlung, Analyse und Verbreitung einsetzen.
- Dedizierte Bedrohungsanalysten beschäftigen oder unter Vertrag nehmen.
- Intelligenz auf allen drei Ebenen produzieren (strategisch, taktisch, operativ).
- Bedrohungsintelligenz über automatisierte Feeds in alle Sicherheitstools integrieren.
- Aktiv an externen Austauschgemeinschaften teilnehmen.
- Durch Intelligenz informierte Bedrohungsmodellierungsübungen durchführen.

---

## Rollen und Verantwortlichkeiten

| Rolle | Bedrohungsintelligenz-Verantwortlichkeiten |
|-------|------------------------------------------|
| **Geschäftsleitung** | Bedrohungsintelligenz-Richtlinie genehmigen; Ressourcen zuweisen; strategische Intelligenzbriefings erhalten; Austauschvereinbarungen genehmigen |
| **ISB** | Programmeigentümerschaft; Quell-Portfolio-Management; Überwachung der Intelligenzqualität; Eskalation bei kritischen Bedrohungen; jährliche Programmüberprüfung; Ausnahmegenehmigung |
| **IT-Manager / Sicherheitsleitung** | Tägliche Intelligenzsammlung und -überprüfung; IOC-Bereitstellung in Sicherheitstools; Konsum taktischer und operativer Intelligenz; interne Telemetrieanalyse |
| **Risikomanagement** | Bedrohungsintelligenz in Risikobeurteilungen integrieren; Risikoregister basierend auf Intelligenzbefunden aktualisieren; bedrohungsgetriebene Risikoänderungen bewerten |
| **Vorfallsreaktion** | Bedrohungsintelligenz bei Untersuchungen anwenden; IOCs aus Vorfällen extrahieren; Post-Incident-Feedback an Intelligenzfunktion geben |
| **IT-Betrieb** | IOCs in Erkennungs- und Sperrsystemen einsetzen; Feed-Integrationen pflegen; durch Überwachung identifizierte technische Anomalien melden |
| **Alle Mitarbeitenden** | Verdächtige Aktivitäten und potenzielle Sicherheitsereignisse melden; Bedrohungsbewusstseinstraining absolvieren; verbreiteten Meldungen folgen |

### Eskalationspfad

- **Routinemässige Intelligenz**: IT-Manager / Sicherheitsleitung überprüft und handelt. ISB in regelmässigen Berichtsintervallen informiert.
- **Erhöhte Bedrohung**: IT-Manager / Sicherheitsleitung eskaliert innerhalb von 4 Stunden an ISB. ISB bewertet die organisatorische Exposition und bestimmt die Reaktion.
- **Kritische / unmittelbare Bedrohung**: Sofortige Eskalation an ISB. ISB informiert Geschäftsleitung und aktiviert bei Bedarf die Vorfallsreaktion.
- **Regulatorische Meldung**: ISB koordiniert die obligatorische Meldung an das Schweizer NCSC, wo anwendbar (Betreiber kritischer Infrastruktur — innerhalb von 24 Stunden gemäss ISG Art. 74b).

---

## Nachweise (Erweitert für Audit)

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie. **Für SOC 2 Typ II-Audits** werden Auditoren die Betriebseffektivität durch Stichprobenentnahme von Nachweisen aus dem Prüfungszeitraum (typischerweise 12 Monate) testen.

| # | Nachweis | Verantwortlicher | Frequenz | Audit-Trail-Details |
|---|---------|-----------------|----------|---------------------|
| 1 | **Bedrohungsintelligenzquellen-Inventar** | ISB | *Jährliche Überprüfung; bei Änderung aktualisiert* | Inventardokument mit Versionshistorie; Änderungsprotokoll mit Quellenergänzungen/-entfernungen mit Daten und Genehmigungen |
| 2 | **Quellenbeurteilungsunterlagen** | ISB | *Jährlich pro Quelle* | Ausgefüllte Beurteilungsvorlage für jede Quelle; Bewertung dokumentiert; Entscheidung zur Beibehaltung/Ersetzung der Quelle mit Begründung |
| 3 | **Strategische Intelligenzberichte** | ISB | *Mindestens vierteljährlich* | Berichtsdokumente mit Verteilerliste und Lieferbestätigung; Sitzungsprotokoll der Geschäftsleitung mit Empfang und Diskussion |
| 4 | **Taktische Intelligenzmeldungen** | IT-Manager / Sicherheitsleitung | *Mindestens monatlich; ad hoc* | Meldungsdokumente mit Verteilungszeitstempel; Empfangsbestätigung durch wichtige Stakeholder |
| 5 | **IOC-Bereitstellungsunterlagen** | IT-Betrieb | *Pro Bereitstellung* | Bereitstellungstickets oder TIP-Protokolle mit: IOC-Kennung, Quelle, Bereitstellungsdatum/-uhrzeit, Zielsysteme, Bereitstellungsmethode, Validierungstestergebnisse |
| 6 | **Risikoregister-Aktualisierungen** | Risikomanagement | *Pro Aktualisierung* | Risikoregistereinträge mit Zeitstempel "zuletzt aktualisiert"; Feld "Intelligenzquelle" mit dem auslösenden Bedrohungsintelligenzbericht |
| 7 | **Vorfallsuntersuchungsunterlagen** | Vorfallsreaktion | *Pro P1/P2-Vorfall* | Vorfallstickets mit ausgefülltem Abschnitt "Bedrohungsintelligenz-Kontext"; IOC-Korrelationsergebnisse; Bedrohungsakteur-Attributionsbewertung (wo möglich) |
| 8 | **Post-Incident-Bedrohungsintelligenz-Feedback** | Vorfallsreaktion | *Pro P1/P2-Vorfall* | Vorfallspost-mortem-Abschnitt mit Dokumentation: neue entdeckte IOCs, beobachtete TTPs, identifizierte Intelligenslücken, Empfehlungen zur Erkennungsverbesserung |
| 9 | **Externe Austauschvereinbarungen** | ISB | *Pro Vereinbarung; jährliche Überprüfung* | Unterzeichnete NDAs, ISAC-Mitgliedschaftsvereinbarungen, Informationsaustausch-MoUs; jährliche Überprüfungsnotizen, die die Aktualität der Vereinbarungen bestätigen |
| 10 | **TLP-Konformitätsunterlagen** | ISB | *Pro Austauchereignis* | Austauschprotokoll mit: Datum, Empfänger, zugewiesene TLP-Klassifizierung, Genehmigung (bei TLP:AMBER oder höher), Bestätigung der TLP-Kenntnisnahme durch Empfänger |
| 11 | **Anbieterkontrollberichte** | ISB | *Jährlich pro Anbieter* | Anbieterüberprüfungsvorlage mit SLA-Compliance-Daten, Falsch-Positiv-Raten, Kosten-Nutzen-Analyse, Vertragserneuerungsempfehlung mit Genehmigungsunterschrift |
| 12 | **Intelligenztestergebnisse** | IT-Sicherheit | *Pro Test (vierteljährlich/halbjährlich)* | Testberichte mit: Testdatum, Testumfang, Testergebnisse (bestanden/nicht bestanden Metriken), identifizierte Lücken, zugewiesene Korrekturmassnahmen mit Fälligkeitsterminen |
| 13 | **Metrik-Dashboard** | ISB | *Vierteljährlich* | Dashboard-Screenshot oder -Bericht mit allen KPIs; Trenddiagramme für Jahresvergleiche; rot überschrittene Schwellenwerte mit Korrekturmassnahmenstatus hervorgehoben |
| 14 | **Jährliche Programmüberprüfung** | ISB | *Jährlich* | Umfassendes Überprüfungsdokument mit Quellenleistung, Integrationseffektivität, Reifegradbewertung, Ressourcenadäquatheit, Präsentationsfolien für die Geschäftsleitung mit Genehmigungsunterschriften |

### Audit-Trail-Anforderungen

Für den SOC 2 Typ II-Test der Betriebseffektivität ist sicherzustellen:

- **Vollständigkeit**: Alle erforderlichen Nachweise existieren für den gesamten Prüfungszeitraum (typischerweise 12 Monate)
- **Genauigkeit**: Nachweise spiegeln tatsächliche Aktivitäten wider (keine vorlagenhaften Platzhalter)
- **Zeitstempel**: Alle Nachweise klar datiert; elektronische Nachweise enthalten Metadaten mit Erstellungs-/Änderungsdaten
- **Genehmigungen**: Wo die Richtlinie Genehmigung erfordert (z. B. Ausnahmen, Anbieterauswahl, Austauschvereinbarungen), Genehmigung mit Name und Datum des Genehmigers dokumentiert
- **Population vs. Stichprobe**: Auditoren werden typischerweise testen:
  - **Alle** strategischen Berichte (sollten mindestens 4 pro Jahr sein)
  - **Stichprobe** von IOC-Bereitstellungen (20-25 Stichproben)
  - **Alle** als P1/P2 eingestuften Vorfälle (sollten Bedrohungsintelligenz-Kontext haben)
  - **Alle** Quellen (sollten jährliche Bewertung haben)
  - **Alle** Anbieterverträge (sollten jährliche Leistungsüberprüfung haben)

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden überprüfen, einschliesslich, aber nicht beschränkt auf, Audits von Bedrohungsintelligenzquellen, Überprüfungen der Integrationseffektivität, Verbreitungsverfolgung, Risikoregister-Querverweise, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

Die folgenden Metriken müssen dem ISB vierteljährlich gemeldet werden:

| Metrik | Ziel | Roter Schwellenwert |
|--------|------|---------------------|
| Aktive Bedrohungsintelligenzquellen über erforderliche Kategorien | 100% der erforderlichen Kategorien abgedeckt | Jede erforderliche Kategorie mit 0 aktiven Quellen |
| Quellenbeurteilungsüberprüfungen termingerecht abgeschlossen | 100% jährlich | <80% der überprüften Quellen |
| Strategische Intelligenzbriefings geliefert | Mindestens vierteljährlich | >1 aufeinanderfolgendes Quartal verpasst |
| Aktualität der IOC-Bereitstellung | Innerhalb von 24 Stunden nach validiertem Empfang | >72 Stunden durchschnittlich |
| Durch Bedrohungsintelligenz informierte Risikoregister-Aktualisierungen | Mindestens 1 pro Quartal | 0 Aktualisierungen in einem Quartal |
| Abschluss des Post-Incident-Intelligenz-Feedbacks (P1/P2) | 100% | <80% |

**Berichtsanforderungen**:
- **Monatliches ISB-Dashboard**: Aktive Quellen, aktuelle Intelligenz-Highlights, IOC-Bereitstellungsstatus, offene Massnahmen.
- **Vierteljährlicher Bericht an die Geschäftsleitung**: Strategische Bedrohungslandschaft-Zusammenfassung, Metrikstatus, Programmverbesserungsempfehlungen.
- **Jährliche Management-Überprüfung**: Vollständige Programm-Effektivitätsbewertung einschliesslich Reifegradbewertung, Ressourcenadäquatheit und strategische Empfehlungen.

Metriken, die rote Schwellenwerte überschreiten, müssen an den ISB zur sofortigen Beachtung eskaliert und beim nächsten Management-Review gemeldet werden.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss im Voraus vom ISB genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Häufige Ausnahmen umfassen Budget-Einschränkungen, die den Zugang zu kommerziellen Quellen begrenzen, technische Einschränkungen, die die automatische Feed-Integration verhindern, und neu implementierte Programme, die die Zielmetriken noch nicht erreicht haben. Ausnahmen, die eine Ressourcenzuweisung jenseits der Befugnis des ISB erfordern, müssen eine gemeinsame Genehmigung von ISB und Geschäftsleitung erfordern. Ausnahmen müssen zeitlich befristet sein (maximal 12 Monate), vierteljährlich überprüft und dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Beendigung des Arbeitsverhältnisses. Spezifische Bedenken bezüglich der Nichteinhaltung umfassen: Weitergabe von Intelligenz unter Verletzung von TLP-Bezeichnungen; Versäumnis, innerhalb der erforderlichen Fristen auf kritische Bedrohungsmeldungen zu reagieren; Versäumnis, bekannte Bedrohungen über etablierte Kanäle zu melden; und unbefugte Offenlegung von Intelligenzquellen oder -methoden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen müssen Änderungen der Bedrohungslandschaft, neue Intelligenzquellen und -fähigkeiten, Audit-Befunde, regulatorische Änderungen (einschliesslich Schweizer NCSC-Meldepflichten), Integrationseffektivität mit Risikobeurteilung und Vorfallsmanagement, Programmreifegradentwicklung und Lessons Learned aus bedrohungsintelligenz-bezogenen Vorfällen berücksichtigen. Nichtkonformitäten im Zusammenhang mit dieser Richtlinie müssen im ISMS-Korrekturmassnahmenprozess (Klausel 10.2) mit Ursachenanalyse und nachverfolgter Behebung aufgezeichnet und verwaltet werden.

---

# Bereiche des ISO 27001-Standards, die adressiert werden

Bedrohungsintelligenz-Richtlinie — ISO 27001-Kontrollzuordnung

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.3 Organisatorische Rollen, Verantwortlichkeiten und Befugnisse | **5.7 Bedrohungsintelligenz** |
| Klausel 6.1 Massnahmen zum Umgang mit Risiken und Chancen | 5.24 Planung und Vorbereitung des Informationssicherheits-Vorfallsmanagements |
| Klausel 7.3 Bewusstsein | 5.25 Bewertung und Entscheidung über Informationssicherheitsereignisse |
| Klausel 8.1 Operative Planung und Steuerung | 8.7 Schutz vor Malware |
| Klausel 9.1 Überwachung, Messung, Analyse und Bewertung | 8.8 Management technischer Schwachstellen |
| Klausel 10.2 Nichtkonformität und Korrekturmassnahmen | 8.15 Protokollierung |
| | 8.16 Überwachungsaktivitäten |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen (Bedrohungsintelligenz als proaktive Sicherheitsmassnahme zum Schutz der Integrität der Datenverarbeitung) |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1-3 — Mindestanforderungen an die Datensicherheit |
| Schweizerisches ISG Art. 74b | Obligatorische Meldung von Cyber-Vorfällen für Betreiber kritischer Infrastruktur (24-Stunden-Meldung an NCSC, gültig ab April 2025) |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung (angemessene technische und organisatorische Massnahmen einschliesslich Bedrohungserkennung) |
| ISO/IEC 27001:2022 | Annex A Kontrolle 5.7 — Bedrohungsintelligenz |
| ISO/IEC 27002:2022 | Abschnitt 5.7 — Umsetzungshinweise für Bedrohungsintelligenz |
| NIST SP 800-53 Rev 5 | PM-16 (Threat Awareness Program), RA-3 (Risk Assessment), SI-5 (Security Alerts, Advisories and Directives) |
| NIST SP 800-150 | Guide to Cyber Threat Information Sharing |
| NIST CSF 2.0 | ID.RA (Risk Assessment), DE.AE (Adverse Events), DE.CM (Continuous Monitoring) |
| CIS Controls v8 | Kontrolle 13 (Network Monitoring and Defense) — Bedrohungsintelligenz unterstützt Lagewahrnehmung und Erkennung |
| MITRE ATT&CK | Wissensbasis über Angreifertaktiken und -techniken — Strukturierte Taxonomie für die Bedrohungsintelligenzanalyse |
| FIRST TLP v2.0 | Traffic Light Protocol — Standard zur Klassifizierung und Kontrolle des Bedrohungsintelligenz-Austauschs |
| OASIS STIX v2.1 / TAXII v2.1 | Standards für den strukturierten Bedrohungsinformationsaustausch und das automatisierte Austauschprotokoll |

---

## Anhang A: Vorlage für das Bedrohungsintelligenz-Metrik-Dashboard

**Berichtszeitraum:** Q[X] [JAHR]
**Berichtsdatum:** [Date]
**Erstellt von:** [ISB/Sicherheitsleitung]

### Zusammenfassung für die Geschäftsleitung
[2-3 Absätze Zusammenfassung der Bedrohungslandschaft, identifizierte Hauptbedrohungen, ergriffene Massnahmen]

### Status des Quell-Portfolios

| Quellkategorie | Erforderlich | Aktiv | Status | Massnahme erforderlich |
|----------------|-------------|-------|--------|------------------------|
| Behörden/CERT | ≥1 | [X] | Grün | Keine |
| OSINT | ≥2 | [X] | Grün | Keine |
| Interne Telemetrie | Alle | [X] | Grün | Keine |
| Kommerziell | [Wie budgetiert] | [X] | Grün | Keine |
| Anbietermeldungen | Alle kritischen Anbieter | [X] | Gelb | [Anbieter X] Meldungs-Feed nicht überwacht; Massnahme: bis [Datum] abonnieren |

### Wichtige Leistungsindikatoren

| Metrik | Ziel | Q[X] Ist | Trend | Status |
|--------|------|----------|-------|--------|
| Aktive Quellen (alle erforderlichen Kategorien) | 100% | 100% | Stabil | Bestanden |
| Abgeschlossene Quellenbeurteilungen | 100% jährlich | 25% YTD (im Plan) | Aufwärts | Bestanden |
| Gelieferte strategische Briefings | ≥1 pro Quartal | 1 | Stabil | Bestanden |
| Aktualität der IOC-Bereitstellung | <24h Durchschnitt | 18h Durchschnitt | Verbessert | Bestanden |
| Risikoregister-Aktualisierungen aus Intelligenz | ≥1 pro Quartal | 3 | Aufwärts | Bestanden |
| Echte Positivrate (intelligenzgestützte Warnungen) | >70% | 78% | Aufwärts | Bestanden |
| Abschluss des Post-Incident-Feedbacks (P1/P2) | 100% | 100% (2/2 Vorfälle) | Stabil | Bestanden |

### Zusammenfassung der Bedrohungsintelligenz-Aktivitäten

- **Dieses Quartal eingesetzte IOCs:** [X] Indikatoren (Aufschlüsselung: [Y] IP-Adressen, [Z] Domains, [N] Datei-Hashes)
- **Aus Intelligenz generierte Warnungen:** [X] Warnungen; [Y] echte Positivmeldungen, [Z] Falsch-Positivmeldungen
- **Vorfälle mit Intelligenznutzung:** [X] Untersuchungen nutzten Bedrohungsintelligenz-Kontext
- **Intelligenzgesteuerte Risikoaktualisierungen:** [X] Risikoregistereinträge basierend auf Intelligenz aktualisiert
- **Extern geteilte Intelligenz:** [X] Austauchereignisse (alle TLP-konform)

### Wichtigste Bedrohungen dieses Quartals

1. **[Bedrohungsname]** — [Kurze Beschreibung, Relevanz für Organisation, ergriffene Massnahme]
2. **[Bedrohungsname]** — [Kurze Beschreibung, Relevanz für Organisation, ergriffene Massnahme]
3. **[Bedrohungsname]** — [Kurze Beschreibung, Relevanz für Organisation, ergriffene Massnahme]

### Programmverbesserungen dieses Quartals

- [Verbesserungsmassnahme 1 mit Abschlussstatus]
- [Verbesserungsmassnahme 2 mit Abschlussstatus]

### Prioritäten für nächstes Quartal

- [Prioritätsmassnahme 1]
- [Prioritätsmassnahme 2]

**Erstellt von:** [Name, Funktion]
**Überprüft von:** [ISB]
**Verteiler:** Geschäftsleitung, Risikomanagement, IT-Betriebsleiter

---

<!-- QA_VERIFIED: 2026-03-29 -->
