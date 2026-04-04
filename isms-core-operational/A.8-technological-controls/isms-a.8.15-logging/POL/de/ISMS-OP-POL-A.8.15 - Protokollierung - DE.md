<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.15-DE:operational:OP-POL:a.8.15 -->
**ISMS-OP-POL-A.8.15 — Protokollierung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Protokollierung |
| **Dokumententyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.15 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstversion der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt von**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.8.15 — Protokollierung
- Siehe auch: ISMS-OP-POL-A.8.16 (Überwachungsaktivitäten), ISMS-OP-POL-A.8.17 (Zeitsynchronisation)

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Protokollierung |
|-----------|--------------------------|
| A.5.7 Bedrohungsintelligenz | Bedrohungsintelligenz informiert Überwachungsregeln und Erkennungsmuster |
| A.5.15–18 Zugangskontrolle und Identitätsverwaltung | Authentifizierungs- und Zugriffsereignisse sind primäre Protokollquellen |
| A.5.24–28 Vorfallmanagement | Protokollanalyse unterstützt Vorfallserkennung, Untersuchung und Beweise |
| A.5.28 Sammlung von Beweisen | Protokolle dienen als forensische Beweise; Integrität muss gewahrt werden |
| A.5.34 Datenschutz und Schutz personenbezogener Daten | Mitarbeiterüberwachung muss Datenschutzanforderungen einhalten |
| A.8.1 Benutzer-Endgeräte | Endpunktereignisse für Sicherheitsüberwachung protokolliert |
| A.8.7 Schutz vor Malware | Malware-Erkennungsereignisse protokolliert und weitergeleitet |
| A.8.8 Management technischer Schwachstellen | Ergebnisse von Schwachstellen-Scans protokolliert |
| A.8.20 Netzwerksicherheit | Netzwerkverkehr und Sicherheitsereignisse protokolliert |

**Verwandte interne Richtlinien**:

- Zugangskontrollrichtlinie
- Richtlinie zum Vorfallmanagement
- Richtlinie zum Datenschutz und Schutz personenbezogener Daten
- Netzwerksicherheitsrichtlinie
- Endpunkt-Sicherheitsrichtlinie
- Richtlinie zur Informationsklassifizierung und -handhabung

---

# Protokollierungsrichtlinie

## Zweck

Zweck dieser Richtlinie ist es, die Identifizierung und Verwaltung von Sicherheitsereignissen durch die Protokollierung von Informationsverarbeitungssystemen zu adressieren. Protokolle liefern die Beweisspur für Vorfallserkennung, Untersuchung, Compliance-Verifikation und forensische Analyse.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) und die Datenschutzverordnung (DSV) durch die Implementierung von Protokollierung als technische und organisatorische Massnahme, die dem Risiko angemessen ist, einschliesslich der spezifischen Protokollierungspflichten gemäss DSV Art. 4 für die Verarbeitung besonders schützenswerter Personendaten. Soweit die Organisation Daten von Personen im EU/EWR-Raum verarbeitet, gelten zudem DSGVO-Anforderungen. Für Überwachungsaktivitäten, siehe ISMS-OP-POL-A.8.16. Für Zeitsynchronisation, siehe ISMS-OP-POL-A.8.17.

## Geltungsbereich

Alle Mitarbeitenden und Drittbenutzer.

Alle Geräte, Systeme und Anwendungen, die zur Verarbeitung, Speicherung oder Übertragung von Organisationsinformationen verwendet werden, die im Geltungsbereich der ISO-27001-Geltungsbereichserklärung definiert sind.

## Grundsatz

Alle Systeme, die vertrauliche oder personenbezogene Informationen verarbeiten, speichern oder übertragen, sollen Protokollierung aktiviert haben, wo Protokollierung möglich und praktikabel ist. Protokolle sollen zentral erfasst, vor Manipulation geschützt, für einen definierten Zeitraum aufbewahrt und regelmässig überprüft werden, um Sicherheitsereignisse zu erkennen.

---

## Ereignisprotokollierung

### Zu protokollierende Ereignisse

Ereignisprotokolle, die Benutzeraktivitäten, Ausnahmen, Fehler und Informationssicherheitsereignisse aufzeichnen, sollen erstellt, aufbewahrt und regelmässig überprüft werden. Folgende Ereignisse sollen protokolliert werden:

| # | Ereigniskategorie | Details |
|---|------------------|---------|
| 1 | **Authentifizierungsereignisse** | Erfolgreiche und abgelehnte Anmelde- und Abmeldeversuche, einschliesslich Fernzugang (VPN, Webanwendungen) |
| 2 | **Daten- und Ressourcenzugriff** | Erfolgreiche und abgelehnte Versuche, auf Dateien, Datenbanken, Anwendungen und Netzwerkressourcen zuzugreifen |
| 3 | **Systemkonfigurationsänderungen** | Änderungen an Systemeinstellungen, Sicherheitsparametern, Netzwerkkonfiguration und Firewall-Regeln |
| 4 | **Nutzung erhöhter Privilegien** | Alle mit administrativen, Root- oder Sudo-Rechten durchgeführten Aktionen |
| 5 | **Systemprogramme und Anwendungen** | Nutzung privilegierter Hilfsprogramme, Wartungstools und Diagnosewerkzeuge |
| 6 | **Dateioperationen** | Erstellung, Änderung, Löschung und Migration von Dateien auf kritischen Systemen |
| 7 | **Zugangskontrollalarme** | Kontosperrungen, Schwellenwertüberschreitungen und Einbruchserkennungsalarme |
| 8 | **Sicherheitssystemänderungen** | Aktivierung, Deaktivierung oder Änderung von Antivirus, Firewall, IDS/IPS und anderen Schutzsystemen |
| 9 | **Identitätsverwaltung** | Erstellung, Änderung, Löschung und Deaktivierung von Benutzerkonten und Berechtigungen |
| 10 | **Anwendungstransaktionen** | Von Benutzern in geschäftskritischen Anwendungen durchgeführte Transaktionen (Finanzsysteme, HR, CRM) |

### Inhalt von Protokolleinträgen

Jeder Protokolleintrag soll mindestens Folgendes enthalten:

| Feld | Beschreibung |
|------|--------------|
| **Benutzer-/Konto-ID** | Das Konto, das die Aktion ausgeführt hat |
| **Zeitstempel** | Datum und Uhrzeit im ISO-8601-Format, synchronisiert mit der Referenzzeitquelle der Organisation |
| **Ereignistyp** | Beschreibung des Vorgefallenen (Anmeldung, Dateizugriff, Konfigurationsänderung usw.) |
| **Erfolg oder Misserfolg** | Ob die Aktion erfolgreich war oder abgelehnt wurde |
| **System-/Geräte-ID** | Hostname, Asset-ID oder IP-Adresse des Systems, auf dem das Ereignis eingetreten ist |
| **Quelladresse** | Quell-IP-Adresse oder Netzwerkstandort (wo anwendbar) |

---

## Zugangskontrolle für Ereignisprotokolle

Ereignisprotokollierung und -überwachung sollen ausschliesslich durch autorisiertes Personal durchgeführt werden.

Ereignisprotokolle und Überwachungssysteme sollen geschützt und der Zugang gemäss der Zugangskontrollrichtlinie eingeschränkt werden. Der Zugang zu Rohprotokollen soll auf das Informationssicherheitsmanagement-Team und autorisiertes IT-Personal beschränkt sein.

Systemadministratoren sollen keine Berechtigung haben, Protokolle ihrer eigenen Aktivitäten zu löschen oder zu deaktivieren. Wo dies technisch nicht durchsetzbar ist, sollen Ausgleichskontrollen implementiert werden (z. B. Weiterleitung von Protokollen an ein zentrales System ausserhalb der Kontrolle des Administrators, periodische Überprüfung der Administratoraktivität durch eine separate Rolle).

---

## Schutz von Ereignisprotokoll-Informationen

Protokollierungseinrichtungen und Protokollinformationen sollen gegen Manipulation und nicht autorisierten Zugang geschützt werden.

Kontrollen sollen schützen gegen:

- **Änderung** aufgezeichneter Protokolleinträge oder Nachrichtentypen.
- **Löschung** von Protokolldateien oder einzelnen Einträgen.
- **Speichererschöpfung**, die zum Verlust von Protokolldaten führt (Protokolle sollen offen ausfallen — bei **80 % Kapazität** alarmieren statt lautlos zu überschreiben). Die Protokollspeicherkapazität soll kontinuierlich überwacht werden, mit automatischen Alarmen bei 80 % und 90 % Schwellenwerten. Bei Erreichen von 90 % Kapazität sollen archivierte Protokolle in den Langzeitspeicher ausgelagert werden und das Plattformteam soll prüfen, ob zusätzliche Kapazität erforderlich ist.
- **Nicht autorisierter Zugang** zu Protokolldaten (Protokolle können personenbezogene Daten enthalten und sind mindestens als INTERN klassifiziert).

Protokollschutz soll erreicht werden durch:

- Weiterleitung von Protokollen an ein **zentralisiertes Protokollierungssystem** getrennt von den Quellsystemen.
- **Nur-Anhängen**- oder **Einmalschreib**-Speicher für Protokolldaten, wo technisch machbar.
- **Kryptografische Integritätsprüfungen** (Hashing) zur Erkennung von Manipulationen, wo für forensische oder rechtliche Zwecke erforderlich.
- **Zugriffskontrollen**, die Protokolländerungen ausschliesslich auf autorisiertes Sicherheitspersonal beschränken.

---

## Zentralisierte Protokollierung

### Zentralisierte Protokollierungsplattform

Die zentralisierte Protokollierungsplattform soll folgende Anforderungen erfüllen:

| Anforderung | Spezifikation |
|-------------|---------------|
| **Plattformtyp** | SIEM, Log-Aggregator oder gleichwertig (z. B. Splunk, Microsoft Sentinel, Elastic SIEM, Wazuh oder gleichwertig) |
| **Bereitstellung** | Getrennt von Quellsystemen; Quellsystem-Administratoren sollen keinen administrativen Zugang haben |
| **Speicher** | Ausreichende Kapazität für definierte Aufbewahrungsfristen; Alarmschwelle bei 80 % Kapazität |
| **Suche** | Volltextsuch- und strukturierte Abfragefähigkeit für Vorfalluntersuchung und Compliance-Abfragen |
| **Alarmierung** | Konfigurierbare Regeln mit Benachrichtigung an das Informationssicherheitsmanagement-Team (E-Mail, SMS, Ticketsystem) |
| **Integrität** | Nur-Anhängen- oder Einmalschreib-Speicher; kryptografische Integritätsprüfungen wo erforderlich |
| **Zugangskontrolle** | Rollenbasierter Zugang; Nur-Lesen für Analysten; administrativer Zugang auf Plattformadministratoren beschränkt |

Protokolle aller kritischen Systeme sollen an die zentralisierte Protokollierungsplattform weitergeleitet werden. Die Plattform soll:

- **Getrennt** von den Systemen sein, die die Protokolle generieren (Quellsystem-Administratoren sollen keinen administrativen Zugang zum zentralen Protokollspeicher haben).
- **Durchsuchbar** sein, um Vorfalluntersuchung und Compliance-Abfragen zu unterstützen.
- **Alarmierungsfähig** sein, um das Informationssicherheitsmanagement-Team über Hochrisiko-Ereignisse zu benachrichtigen.
- **Geschützt** sein mit denselben oder höheren Sicherheitskontrollen wie die Quellsysteme.

Mindestens folgende Systeme sollen in die zentralisierte Protokollierung einbezogen werden:

- Authentifizierungs- und Identitätssysteme (Active Directory, Identitätsanbieter, SSO).
- Firewalls und Netzwerksicherheitsgeräte.
- Server, die vertrauliche oder personenbezogene Daten hosten.
- E-Mail- und Web-Gateways.
- VPN- und Fernzugangssysteme.
- Endpoint-Detection-and-Response-Systeme (EDR).
- Administrative Konsolen für Cloud-Dienste (Microsoft 365, AWS, Azure usw.).

Wo automatisierte zentralisierte Protokollierung für ein spezifisches System nicht machbar ist, soll manuelle Protokollsammlung und -überprüfung in einer definierten Häufigkeit mit dokumentierter Begründung durchgeführt werden.

---

## Administrator- und Betreiberprotokolle

Aktivitäten von Systemadministratoren und Systembetreibern sollen protokolliert werden, und die Protokolle sollen geschützt und regelmässig überprüft werden.

Inhaber privilegierter Konten können in der Lage sein, Protokolle auf Systemen unter ihrer direkten Kontrolle zu manipulieren. Um die Rechenschaftspflicht für privilegierte Benutzer aufrechtzuerhalten:

- Administratorhandlungen sollen in Echtzeit oder nahezu in Echtzeit an das zentralisierte Protokollierungssystem weitergeleitet werden.
- Eine periodische Überprüfung der privilegierten Benutzeraktivität soll durchgeführt werden (mindestens vierteljährlich).
- Anomale privilegierte Aktivitäten (z. B. Zugang ausserhalb der Geschäftszeiten, Massenoperationen, Sicherheitskonfigurationsänderungen) sollen Alarme auslösen.

---

## Zeitsynchronisation

Protokollzeitstempel sollen auf allen Systemen genau und konsistent sein. Zeitsynchronisationsanforderungen sind in **ISMS-OP-POL-A.8.17 — Zeitsynchronisation** definiert. Alle Systeme, die Protokolldaten generieren, sollen den A.8.17-Zeitquellen- und Drifttolerananzforderungen entsprechen.

---

## Ereignisprotokollüberprüfung

### Überprüfungsanforderungen

Die Analyse und Überwachung von Sicherheitsereignissen sollen Verantwortlichkeiten zugeordnet sein.

| Überprüfungstyp | Häufigkeit | Verantwortlich | Umfang |
|----------------|------------|----------------|--------|
| **Automatische Alarmierung** | Echtzeit | Informationssicherheit | Hochrisiko-Ereignisse lösen sofortige Benachrichtigung an das Informationssicherheitsmanagement-Team aus |
| **Sicherheitsereignisüberprüfung** | Wöchentlich | Informationssicherheitsanalyst | Alle Sicherheitsereignisse, Authentifizierungsfehler, Zugriffsanomalien |
| **Privilegierte Aktivitätsüberprüfung** | Vierteljährlich | ISB / Informationssicherheitsbeauftragter | Administrator- und Betreibermassnahmen, Privilege-Eskalationen |
| **Vollständige Protokollüberprüfung** | Monatlich | Informationssicherheit | Trends, Muster und Anomalien über alle Protokollquellen |
| **Protokollquellen-Abdeckungsüberprüfung** | Vierteljährlich | IT-Betrieb | Verifizieren, dass alle im Geltungsbereich befindlichen Systeme Protokolle weiterleiten; Lücken identifizieren |

### Hochrisiko-Ereignisse

Folgende Ereignisse sollen sofortige automatische Alarme auslösen und in den Vorfallmanagementprozess eskaliert werden:

| # | Hochrisiko-Ereignis | Alarmschwelle | Reaktion |
|---|---------------------|---------------|----------|
| 1 | Mehrfache fehlgeschlagene Authentifizierungsversuche | **5 Fehler** innerhalb von 10 Minuten (einzelnes Konto) oder **20 Fehler** innerhalb von 10 Minuten (mehrere Konten von einer einzelnen Quelle) | Kontosperrung; Quelle untersuchen |
| 2 | Erfolgreiche Authentifizierung von unerwarteten Standorten | Anmeldung aus neuem Land oder IP-Bereich nicht in der Baseline | Mit Benutzer verifizieren; aussetzen, wenn nicht bestätigt |
| 3 | Deaktivierung oder Änderung von Sicherheitskontrollen | Jede Änderung an Antivirus, Firewall-Regeln oder Protokollierungskonfiguration | Sofortiger Alarm an Informationssicherheit |
| 4 | Massendatenzugriff, -download oder -löschung | **>500 Dateien** oder **>1 GB** innerhalb von 1 Stunde von einem einzelnen Benutzer abgerufen/heruntergeladen | Untersuchen; Zugang bei Bedarf aussetzen |
| 5 | Erstellung neuer privilegierter Konten oder Privilege-Eskalation | Jedes neue Administrator-/Root-Konto oder jede Privilege-Eskalation | Autorisierung gegen Änderungsaufzeichnungen verifizieren |
| 6 | Erkennung von Malware oder Einbruchsversuchen | Jede bestätigte Erkennung | Vorfallmanagementprozess |
| 7 | Änderung oder Löschung von Protokolldateien | Jeder Versuch | Sofortiger Alarm; forensische Untersuchung |

### Vorfallseskalation aus der Überwachung

Wenn ein Hochrisiko-Ereignis erkannt wird, soll folgender Eskalationsprozess befolgt werden:

1. **Alarm**: Automatischer Alarm generiert und an das Informationssicherheitsmanagement-Team gesendet.
2. **Triage** (innerhalb **30 Minuten** während der Geschäftszeiten; **2 Stunden** ausserhalb der Geschäftszeiten): Analyst bewertet den Alarm, bestimmt, ob es sich um ein echtes Positiv, Falsch-Positiv handelt oder Untersuchung erfordert.
3. **Untersuchung**: Falls als potentielles Sicherheitsereignis bestätigt, wird ein Vorfallsprotokoll gemäss der Richtlinie zum Vorfallmanagement erstellt.
4. **Eskalation**: Als Hoch oder Kritisch klassifizierte Vorfälle werden sofort an den ISB eskaliert.

---

## Aufbewahrung von Ereignisprotokollen

| Protokolltyp | Online (Durchsuchbar) | Archiv (Abrufbar) | Gesamtaufbewahrung |
|-------------|----------------------|-------------------|-------------------|
| Sicherheitsereignisse (Authentifizierung, Zugangskontrolle) | 90 Tage | 9 Monate | **12 Monate** |
| System- und Infrastrukturprotokolle | 90 Tage | 6 Monate | **9 Monate** |
| Anwendungsprotokolle | 90 Tage | 6 Monate | **9 Monate** |
| Firewall- und Netzwerksicherheitsprotokolle | 90 Tage | 9 Monate | **12 Monate** |
| Protokolle zur Verarbeitung besonders schützenswerter Personendaten (DSV Art. 4) | 90 Tage | 9 Monate | **12 Monate** (Minimum gemäss DSV) |
| Finanzprotokolle | 90 Tage | Gemäss gesetzlicher Aufbewahrung | **Gemäss OR Art. 958f** |

**Begründung der Aufbewahrungsfristen**: Sicherheitsereignis- und Firewall-Protokolle werden 12 Monate aufbewahrt, um Vorfalluntersuchungen zu unterstützen (durchschnittliche Verweildauer bei Advanced-Threats beträgt 10–21 Tage, und regulatorische Untersuchungen können sich über 12 Monate erstrecken). System- und Anwendungsprotokolle werden 9 Monate aufbewahrt, um betrieblichen Nutzen mit Speicherkosten in Einklang zu bringen. DSV-Art.-4-Protokolle erfordern mindestens 12 Monate gemäss Verordnung.

### Protokollarchivierung und -abruf

Archivierte Protokolle sollen verschlüsselt, an einem sicheren Ort gespeichert und innerhalb folgender Zeitrahmen abrufbar sein:

| Archivalter | Abrufziel |
|-------------|-----------|
| 0–90 Tage (online) | Sofort (in Plattform durchsuchbar) |
| 91 Tage – 6 Monate | Innerhalb **4 Stunden** |
| 6–12 Monate | Innerhalb **24 Stunden** |
| >12 Monate (falls aus rechtlichen/regulatorischen Gründen aufbewahrt) | Innerhalb **5 Arbeitstagen** |

Abrufverfahren sollen mindestens jährlich getestet werden, um zu verifizieren, dass archivierte Protokolle zugänglich und intakt sind.

Protokolle sollen nicht länger als notwendig aufbewahrt werden. Bei Ablauf der Aufbewahrungsfristen sollen Protokolle gemäss der Richtlinie zur Informationsklassifizierung und -handhabung sicher gelöscht werden.

---

## Schweizerisches nDSG — DSV-Artikel-4-Protokollierungspflichten

Wo die Organisation besonders schützenswerte Personendaten (nDSG Art. 5) automatisiert in grossem Umfang verarbeitet oder Hochrisiko-Profiling durchführt, gelten folgende zusätzliche Protokollierungsanforderungen gemäss DSV Art. 4:

**Zu protokollierende Operationen**: Speicherung, Änderung, Lesen, Weitergabe, Löschung und Vernichtung besonders schützenswerter Personendaten.

**Protokollinhalt**: Identität der Person oder des Systems, das die Verarbeitung durchführt, Art der Verarbeitung sowie Datum und Uhrzeit.

**Protokollspeicherung**: Protokolle der Verarbeitung besonders schützenswerter Personendaten sollen **getrennt** vom Verarbeitungssystem gespeichert, mindestens **1 Jahr** aufbewahrt und der Zugang auf die Verifikation der Datensicherheits-Compliance und die Gewährleistung von Vertraulichkeit, Integrität, Verfügbarkeit und Nachvollziehbarkeit beschränkt werden.

### DSV-Art.-4-Anwendbarkeitsbeurteilung

Die Organisation soll bestimmen, ob DSV Art. 4 anwendbar ist, indem folgende Kriterien bewertet werden:

| Kriterium | Beurteilung |
|-----------|-------------|
| Verarbeitet die Organisation **besonders schützenswerte Personendaten** (nDSG Art. 5)? | Ja / Nein |
| Ist die Verarbeitung **automatisiert** (nicht rein manuell/papierbasiert)? | Ja / Nein |
| Erfolgt die Verarbeitung in **grossem Umfang** (Anzahl betroffener Personen, Datenvolumen, geografische Reichweite)? | Ja / Nein |
| Führt die Organisation **Hochrisiko-Profiling** durch? | Ja / Nein |

Wenn die Antwort auf das erste Kriterium UND eines der verbleibenden Kriterien **Ja** lautet, gelten die Protokollierungspflichten gemäss DSV Art. 4. Wo die Organisation unsicher ist, ob Art. 4 anwendbar ist, wird die Implementierung dieser Protokollierungsanforderungen als Best Practice empfohlen.

---

## Persönliche Privatsphäre

Die Privatsphäre von Mitarbeitenden und Kunden soll gemäss dem schweizerischen nDSG und anwendbaren gesetzlichen Anforderungen bei der Implementierung von Protokollierung respektiert werden.

### Grundsätze zur Mitarbeiterüberwachung

- Protokollierungssysteme sollen **legitimen Sicherheitszwecken** dienen (Bedrohungen erkennen, Vorfälle untersuchen, Compliance verifizieren) — nicht primär zur Überwachung des Mitarbeiterverhaltens.
- Mitarbeitende sollen **im Voraus informiert** werden, dass Protokollierung stattfindet, was protokolliert wird und warum, durch das Informationssicherheitsbewusstseinsprogramm und die Anstellungsdokumentation.
- Es sollen nur die **minimal notwendigen Daten** erfasst und aufbewahrt werden (Datensparsamkeit).
- Der Zugang zu Protokollen, die Mitarbeiterdaten enthalten, soll auf autorisiertes Sicherheits- und Compliance-Personal beschränkt sein — nicht für Vorgesetzte zur allgemeinen Einsichtnahme.
- **Tastatureingabe-Logging** und **kontinuierliche individuelle Aktivitätsüberwachung** sind unverhältnismässig und sollen nicht implementiert werden.
- Wo Protokolle mit personenbezogenen Daten an externe Parteien weitergegeben werden (z. B. Anbieter zur Fehlerbehebung), sollen personenbezogene Identifikatoren maskiert oder anonymisiert werden.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **ISB** | Richtlinieneigentümerschaft; Genehmigung des Überwachungsumfangs; Eskalationspunkt für kritische Alarme; vierteljährliche Überprüfung privilegierter Aktivitäten |
| **Informationssicherheitsanalyst** | Tägliche/wöchentliche Protokollüberprüfung; Alarmtriage; Vorfallseskalation; Pflege von Erkennungsregeln |
| **IT-Betrieb / Plattformteam** | Protokollierungsplattform-Administration; Kapazitätsmanagement; Protokollquellen-Onboarding; NTP-Konfiguration; Archivierung |
| **Systemadministratoren** | Sicherstellen, dass Protokollierung auf verwalteten Systemen aktiviert ist; Mitwirken beim Protokollquellen-Onboarding; Protokollierungsfehler melden |
| **Datenschutzberater** | Beratung zur Anwendbarkeit von DSV Art. 4; Datenschutzauswirkung von Überwachungsaktivitäten; Mitarbeiterbenachrichtigungsanforderungen |

---

## Nachweise

Die folgenden Nachweise demonstrieren die Einhaltung dieser Richtlinie:

| # | Nachweis | Verantwortlich | Häufigkeit |
|---|----------|----------------|------------|
| 1 | **Zentralisierte Protokollierungsplattform**-Konfiguration und Protokollquellen-Inventar | IT-Betrieb | *Protokollquellen-Inventar vierteljährlich überprüft; Konfiguration dokumentiert* |
| 2 | **Muster-Protokolleinträge**, die zeigen, dass erforderliche Felder erfasst werden | Informationssicherheit | *Jährlich während der Revision verifiziert; Stichprobe von 5 Systemen* |
| 3 | **Protokollschutzkontrollen** (Zugangsbeschränkungen, Nur-Anhängen-Speicher, Integritätsprüfungen) | IT-Betrieb | *Konfiguration jährlich überprüft; Zugangsprotokoll 12 Monate aufbewahrt* |
| 4 | **Zeitsynchronisations**-Compliance gemäss ISMS-OP-POL-A.8.17 (NTP-Quelle, Drift-Überwachung, Alarmschwelle) | IT-Betrieb | *Siehe ISMS-OP-POL-A.8.17-Nachweis-Anforderungen* |
| 5 | **Protokollaufbewahrungskonfiguration** entsprechend definierten Aufbewahrungsfristen | IT-Betrieb | *Halbjährlich verifiziert; Archiv-Abruf jährlich getestet* |
| 6 | **Sicherheitsereignisüberprüfungsaufzeichnungen** (wöchentliche Überprüfungen, vierteljährliche privilegierte Aktivitätsüberprüfungen) | Informationssicherheit | *Wöchentliche Überprüfungsprotokolle 12 Monate aufbewahrt; vierteljährliche Überprüfungen beim Management Review vorgestellt* |
| 7 | **Alarmierungsregeln** und Muster-Alarmbenachrichtigungen für Hochrisiko-Ereignisse | Informationssicherheit | *Regeln vierteljährlich überprüft; Muster-Alarme 12 Monate aufbewahrt* |
| 8 | **DSV-Art.-4-Compliance-Aufzeichnungen** (Anwendbarkeitsbeurteilung; Protokolle der Verarbeitung besonders schützenswerter Personendaten getrennt gespeichert) | Datenschutzberater | *Anwendbarkeitsbeurteilung jährlich überprüft; Protokolltrennung vierteljährlich verifiziert* |
| 9 | **Mitarbeiterbenachrichtigungsaufzeichnungen** (Sensibilisierungsschulung, Datenschutzhinweis zur Überwachung) | HR / Informationssicherheit | *Bei Richtlinienänderung aktualisiert; Schulungsabschluss jährlich verfolgt* |
| 10 | **Protokollquellen-Abdeckungsmetrik** (Prozentsatz der im Geltungsbereich befindlichen Systeme, die Protokolle weiterleiten) | IT-Betrieb | *Vierteljährlich; Ziel: 100 % der kritischen Systeme, ≥95 % aller im Geltungsbereich befindlichen Systeme* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheitsmanagement-Team soll die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf, Protokollquellen-Abdeckungsüberprüfungen, Aufbewahrungskonformitätsprüfungen, Protokollüberprüfungsabschluss, interne und externe Revisionen sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll im Voraus vom Informationssicherheitsbeauftragten genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sollen dem Management-Review-Team gemeldet werden.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der Protokollierungsstandards, regulatorischer Anforderungen (einschliesslich DSV-Aktualisierungen) sowie Lessons Learned aus Vorfällen berücksichtigen.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Protokollierungsrichtlinie — Zuordnung der ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Standards |
| Abschnitt 7.3 Bewusstsein | 5.37 Dokumentierte Betriebsverfahren |
| Abschnitt 9.1 Überwachung, Messung, Analyse und Bewertung | 6.3 Informationssicherheitsbewusstsein, -ausbildung und -schulung |
| | 6.4 Disziplinarverfahren |
| | **8.15 Protokollierung** |
| | 8.16 Überwachungsaktivitäten *(siehe ISMS-OP-POL-A.8.16)* |
| | 8.17 Zeitsynchronisation *(siehe ISMS-OP-POL-A.8.17)* |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen; Art. 6 — Verhältnismässigkeit der Überwachung |
| Schweizerische DSV (Datenschutzverordnung) | Art. 4 — Protokollierungspflichten für die Verarbeitung besonders schützenswerter Personendaten |
| Schweizerisches OR (Obligationenrecht) | Art. 328b — Einschränkungen der Mitarbeiterdatenverarbeitung; Art. 958f — Aufbewahrung von Geschäftsunterlagen |
| EU-DSGVO (wo anwendbar) | Art. 32 — Sicherheit der Verarbeitung (Protokollierung als angemessene Massnahme) |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.15 (siehe auch 8.16, 8.17) |
| ISO/IEC 27002:2022 | Abschnitt 8.15 — Implementierungsleitfaden |
| NIST SP 800-53 Rev 5 | AU-2 (Event Logging), AU-3 (Content of Audit Records), AU-6 (Audit Review/Analysis), AU-8 (Time Stamps), AU-9 (Protection of Audit Information), AU-11 (Audit Record Retention) |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| CIS Controls v8 | Control 8 (Audit Log Management) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
