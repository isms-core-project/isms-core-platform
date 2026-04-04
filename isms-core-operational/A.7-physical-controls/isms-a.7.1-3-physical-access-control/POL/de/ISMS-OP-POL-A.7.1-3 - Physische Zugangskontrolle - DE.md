<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.1-3-DE:operational:OP-POL:a.7.1-3 -->
**ISMS-OP-POL-A.7.1-3 — Physische Zugangskontrolle**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Physische Zugangskontrolle |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.7.1-3 |
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
| 0.1 | [Date] | ISB | Erstveröffentlichung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Controls A.7.1, A.7.2, A.7.3
- ISO/IEC 27002:2022 Abschnitte 7.1, 7.2, 7.3 — Implementierungshinweise
- ISMS-OP-POL-A.7.4-5-11 — Sicherheit der physischen Infrastruktur
- ISMS-OP-POL-A.7.6-7-14 — Informations- und Medienhandhabung
- ISMS-OP-POL-A.7.8-9 — Sicherheit des Gerätestandorts
- ISMS-OP-POL-A.5.15-16-18 — Identitäts- und Zugangsverwaltung
- ISMS-OP-POL-A.5.24-28 — Incident-Management

**Verwandte Annex-A-Controls**:

| Control | Bezug zur physischen Zugangskontrolle |
|---------|---------------------------------------|
| A.7.4 Physische Sicherheitsüberwachung | Überwachung von Perimetern und Zugangspunkten, die in dieser Richtlinie definiert sind |
| A.7.5 Schutz vor physischen und umgebungsbezogenen Bedrohungen | Umgebungsschutz für durch diese Richtlinie gesicherte Bereiche |
| A.7.6 Arbeiten in gesicherten Bereichen | Verhaltensanforderungen in den hier definierten Zonen |
| A.7.8 Geräteaufstellung und -schutz | Gerätepositionierung innerhalb gesicherter Bereiche |
| A.5.15-16-18 Identitäts- und Zugangsverwaltung | Integration von logischen und physischen Zugangskontollen |
| A.5.24-28 Lifecycle des Incident-Managements | Eskalationspfad für physische Sicherheitsereignisse |
| A.6.7 Remote-Arbeit | Remote-Arbeit reduziert den physischen Zugangsbedarf vor Ort |
| A.8.12 Datenverlustprävention | Physische Kontrollen ergänzen technische DLP-Massnahmen |

---

# Richtlinie zur physischen Zugangskontrolle

## Zweck

Diese Richtlinie legt die Anforderungen der Organisation an die physische Zugangskontrolle fest und deckt Sicherheitsperimeter, physische Zutrittskontrollen sowie die Sicherung von Büros, Räumen und Einrichtungen ab. Sie definiert die Sicherheitszonen, Authentifizierungsanforderungen, Besuchermanagementverfahren und Einrichtungsschutzmassnahmen, die notwendig sind, um unbefugten physischen Zugang zu den Betriebsstätten und Informationswerten der Organisation zu verhindern.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz von Personendaten (einschliesslich besonders schützenswerter Personendaten), die in den Betriebsstätten der Organisation gespeichert oder verarbeitet werden, umsetzt. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten zusätzlich die Anforderungen aus DSGVO Art. 32 zur physischen Sicherheit der Verarbeitung.

Die Controls A.7.1 (Physische Sicherheitsperimeter), A.7.2 (Physischer Zutritt) und A.7.3 (Sicherung von Büros, Räumen und Einrichtungen) werden zusammengefasst, weil sie ein integriertes physisches Sicherheitsrahmenwerk bilden: Perimeter definieren Grenzen, Zutrittskontolen schützen die Überschreitung dieser Grenzen, und interne Sicherheitsmassnahmen schützen spezifische Bereiche innerhalb dieser Grenzen.

**Rein cloudbasierte Organisationen**: Organisationen, die ausschliesslich mit Cloud-Infrastruktur ohne eigene oder gemietete Serverräume oder Rechenzentren betrieben werden, müssen diese Richtlinie dennoch auf Büroräume, Co-Working-Spaces und alle Standorte anwenden, an denen Organisationsinformationen physisch zugegriffen oder gespeichert werden. Serverraum- und Rechenzentrumsanforderungen gelten nur, wenn die Organisation solche Einrichtungen kontrolliert; für Rechenzentren Dritter und Colocation gelten die Anforderungen an die Lieferantensicherung.

## Geltungsbereich

Diese Richtlinie gilt für:

- Alle eigenen, gemieteten oder betriebenen Räumlichkeiten, einschliesslich Büros, Rechenzentren und Remote-Standorte.
- Alle Bereiche: öffentliche Empfangsbereiche, allgemeine Bürobereiche, Serverräume, Rechenzentren, sichere Lagerräume und Archivräume.
- Alle Zugangspunkte: Haupteingänge, Nebentüren, Notausgänge, Lade- und Lieferbereiche, Fenster und Dachzugangspunkte.
- Alle Personen: Mitarbeitende, Auftragnehmer, Besucher, Wartungspersonal und Lieferpersonal.

Nicht im Geltungsbereich:

- Physische Sicherheitsüberwachung und Überwachungssysteme (abgedeckt durch A.7.4).
- Umgebungsschutz — Feuer, Wasser, Temperatur (abgedeckt durch A.7.5).
- Geräteaufstellung und Sicherheit ausserhalb der Betriebsstätten (abgedeckt durch A.7.8-9).
- Versorgungseinrichtungen (abgedeckt durch A.7.11).

## Grundsatz

Physische Sicherheit muss nach dem Defense-in-Depth-Prinzip mit konzentrischen Sicherheitszonen gestaltet werden, wobei jede aufeinanderfolgende Zone eine stärkere Authentifizierung und Autorisierung erfordert. Zugang wird nach dem Prinzip der minimalen Rechte gewährt — Mitarbeitende erhalten nur Zugang zu den Zonen, die für ihre Rolle erforderlich sind. Alle physischen Zugriffe müssen protokolliert, regelmässig überprüft und unverzüglich widerrufen werden, wenn sie nicht mehr benötigt werden. Die Organisation fördert eine sicherheitsbewusste Kultur, in der alle Mitarbeitenden erwartet werden, unbekannte Personen in gesicherten Bereichen anzusprechen und physische Sicherheitsbedenken ohne Vergeltungsangst zu melden.

---

## Physische Sicherheitsperimeter (A.7.1)

**ISO/IEC 27001:2022 Annex A.7.1 — Physische Sicherheitsperimeter**:

> *Sicherheitsperimeter sollten definiert und genutzt werden, um Bereiche zu schützen, die Informationen und andere damit verbundene Werte enthalten.*

### Sicherheitszonenmodell

Die Organisation muss Sicherheitszonen anhand folgender Klassifizierung definieren und dokumentieren:

| Zone | Beschreibung | Beispielbereiche | Zugangspopulation |
|------|-------------|-----------------|-------------------|
| **Öffentliche Zone** | Für die allgemeine Öffentlichkeit zugänglich | Empfangshalle, Wartebereiche für Besucher, Aussenanlagen | Alle Personen |
| **Kontrollierte Zone** | Nur autorisiertes Personal | Allgemeine Bürobereiche, Besprechungsräume, Aufenthaltsräume | Mitarbeitende, begleitete Besucher |
| **Eingeschränkte Zone** | Begrenzter Zugang, Need-to-know-Basis | Führungsbüros, HR, Finanzen, Rechtsabteilung, Aktenarchive | Namentlich genannte Personen mit Geschäftsbedarf |
| **Hochsicherheitszone** | Streng kontrollierter Zugang | Serverräume, Rechenzentren, Security Operations, Tresor-/Safezimmer | Namentlich genannte Personen mit ausdrücklicher Genehmigung |

Jede Zone muss auf Grundrissen mit klar markierten Grenzen, Zugangspunkten und den verwendeten Zugangskontrollmechanismen dokumentiert werden.

### Anforderungen an die Perimeterbauweise

**Gebäudeperimeter (extern)**:

- Aussenwände, Dächer und Böden müssen eine dem Risiko angemessene solide Konstruktion aufweisen.
- Aussentüren müssen mit Schlössern und Zugangskontrollmechanismen gesichert sein (z. B. [Zugangskontrollsystem]-Kartenlesegeräte, elektronische Schlösser).
- Fenster müssen gesichert sein, insbesondere im Erdgeschoss; Erdgeschossfenster in der Nähe von eingeschränkten oder Hochsicherheitszonen müssen verstärkt oder mit Sicherheitsverglasung ausgestattet sein.
- Notausgänge müssen alarmiert und überwacht sein; Notausgänge dürfen nicht für den routinemässigen Zugang von aussen nutzbar sein.
- Alle Brandschutztüren an einem Sicherheitsperimeter müssen alarmiert, überwacht und zusammen mit den Wänden auf das erforderliche Widerstandsniveau geprüft werden. Brandschutztüren müssen gemäss den schweizerischen Brandschutzvorschriften ausfallsicher betrieben werden.
- Belüftungsöffnungen und Serviceöffnungen dürfen keinen Umgehungsweg in gesicherte Bereiche bieten.
- Geeignete Einbruchmeldesysteme müssen gemäss anwendbaren nationalen oder internationalen Normen installiert werden (z. B. EN 50131).

**Interne Perimeter (zwischen Zonen)**:

- Trennwände zwischen kontrollierten, eingeschränkten und Hochsicherheitszonen müssen vom Boden bis zur Decke reichen, einschliesslich über abgehängten Decken und unter Doppelböden.
- Zugangspunkte zwischen Zonen müssen angemessene Zugangskontolen aufweisen, die der Zielzone entsprechen.
- Wände von eingeschränkten Zonen und Hochsicherheitszonen müssen visuelles und akustisches Abhören verhindern, soweit die Risikobewertung dies erfordert.

**Perimeterinspektionen**:

- Gebäudeperimeterinspektionen müssen mindestens jährlich durchgeführt werden.
- Perimeter von eingeschränkten Zonen und Hochsicherheitszonen müssen mindestens vierteljährlich und nach jeder Gebäudemodifikation oder jedem Sicherheitsvorfall inspiziert werden.
- Inspektionsergebnisse müssen dokumentiert und alle Mängel innerhalb von 30 Tagen behoben werden (oder sofort, wenn sie ein unmittelbares Risiko darstellen).

### Colocation und gemeinsam genutzte Einrichtungen

Wenn die Organisation in Colocation-Rechenzentren oder gemeinsam genutzten Bürogebäuden betrieben wird:

- Von [Organisation] kontrollierte Bereiche (Cages, Räume, Etagen) müssen klar abgegrenzt und dokumentiert sein.
- Vertragliche Anforderungen an physische Sicherheit, Zugangsprotokollierung und Vorfallbenachrichtigung müssen mit dem Einrichtungsanbieter vereinbart sein.
- Lieferantenabsicherungsnachweise (ISO 27001-Zertifikat, SOC 2 Type II-Bericht oder gleichwertige Bescheinigung) müssen eingeholt und jährlich überprüft werden.
- Wenn die physische Sicherheit des Colocation-Anbieters die Anforderungen dieser Richtlinie nicht erfüllt, müssen eine dokumentierte Risikoakzeptanz mit Kompensationskontrollen aufgezeichnet werden.
- Gemeinsam genutzte Infrastruktur (Aufzüge, Flure, Gemeinschaftsbereiche) darf keinen unkontrollierten Zugang zu den gesicherten Bereichen der Organisation ermöglichen.
- Die Schlüssel- und Kartenverwaltung für den Gebäudezugang in gemeinsam genutzten Einrichtungen muss mit der Gebäudeverwaltung koordiniert werden, wobei [Organisation] ein unabhängiges Verzeichnis aller ausgegebenen Zugangsdaten führt.

**Trennung von Informationsverarbeitungsanlagen**: Von der Organisation verwaltete Informationsverarbeitungsanlagen müssen physisch von denen externer Parteien getrennt sein, die dasselbe Gebäude oder dieselbe Etage nutzen.

---

## Physische Zutrittskontrolle (A.7.2)

**ISO/IEC 27001:2022 Annex A.7.2 — Physischer Zutritt**:

> *Gesicherte Bereiche sollten durch geeignete Zutrittskontollen geschützt werden, um sicherzustellen, dass nur autorisiertes Personal Zugang erhält.*

### Sicherheit von Zugangspunkten

Alle Zugangspunkte zu gesicherten Bereichen müssen geschützt sein:

**Haupteingänge**:

- Während der Geschäftszeiten muss ein besetzter Empfang oder eine gleichwertige Kontrolle (Gegensprechanlage, Videozugang) betrieben werden.
- Ein Zugangskontrollsystem ([Zugangskontrollsystem] — z. B. Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY/Salto oder gleichwertige RFID-Kartenlesegeräte, mobile Zugangsdaten oder biometrische Lesegeräte) muss alle Personen authentifizieren, die über die öffentliche Zone hinausgehen. Wenn Systeme noch ausgewählt werden, müssen die Übergangsregelung und das angestrebte Einführungsdatum dokumentiert werden.
- Anti-Tailgating-Massnahmen müssen an Zugangspunkten zu eingeschränkten Zonen und Hochsicherheitszonen implementiert werden:

| Massnahme | Wirksamkeit | Anwendbarkeit nach Zone |
|-----------|------------|------------------------|
| **Schleusen** (Zweitürverriegelung) | Hoch — physische Prävention | Hochsicherheitszonen (Server, Rechenzentren) |
| **Drehkreuze mit Höhensensoren** | Mittel-Hoch — physische Barriere + Erkennung | Eingeschränkte Zonen |
| **KI-gestützte CCTV** mit Tailgating-Erkennung | Mittel — Erkennung + Alarm | Alle gesicherten Zonen |
| **Sicherheitsbewusstseinsschilder** + Konfrontationskultur | Niedrig-Mittel — verhaltensbasiert | Minimum für alle Zonen |

Aktuelle Implementierung: [Angabe, z. B. „Drehkreuze am Haupteingang; Schleusen am Rechenzentrum; CCTV + Awareness an sekundären Eingängen" oder „Nur Awareness + CCTV; physische Barrieren geplant für [Quartal]"].
- Der Zugang ausserhalb der Geschäftszeiten muss zusätzliche Authentifizierung erfordern und Alerts an das Sicherheitspersonal oder das Bereitschaftsteam auslösen.

### Notfallzugang

**Zugang ausserhalb der Geschäftszeiten** (ausserhalb der Geschäftszeiten — [Angabe, z. B. 06:00–20:00 Mo–Fr]):
- Erfordert Badge-Authentifizierung + PIN (mindestens kontrollierte Zone).
- Erzeugt einen Alert an die Bereitschaft für Einrichtungen/Sicherheitsüberwachung.
- Wenn innerhalb von 15 Minuten keine Antwort auf die Anfrage erfolgt, Eskalation gemäss Vorfall-Verfahren.

**Notfall-Lockdown**:
- Befugnis zur Einleitung eines Lockdowns: GF, COO, Facilities Manager, ISB oder Sicherheitspersonal vor Ort.
- Auslöser für Lockdown: Aktive Bedrohung vor Ort, nahegelegener Vorfall mit Auswirkung auf die Sicherheit, Naturkatastrophe.
- Lockdown-Verfahren: Alle Aussentüren gesperrt (Badge-Zugang deaktiviert); Personal bleibt am Platz; Notfalldienste benachrichtigt; Entwarnung über [Lautsprecheranlage / SMS / E-Mail] kommuniziert.

**Feuerevakuierung und Sicherheit**:
- Brandschutztüren öffnen automatisch bei Feueralarm (ausfallsicher gemäss schweizerischem Brandschutzrecht).
- Das Zugangskontrollsystem wird nach dem Reset des Alarms und der Bestätigung durch die Einrichtungsinspektion wiederhergestellt.
- Evakuierungssammelplatz ausserhalb des gesicherten Perimeters; Wiederzutritt über einen kontrollierten Prozess nach Entwarnung.

**Sekundäre und Notfalleingänge**:

- Seitentüren und sekundäre Eingänge müssen über Zugangskontolen verfügen, die dem Haupteingang für die entsprechende Zone gleichwertig sind.
- Brandschutztüren und Notausgänge müssen alarmiert und überwacht sein. Notausgänge müssen nach aussen öffnen (gemäss Brandschutzvorschriften), aber von aussen ohne Genehmigung nicht zu öffnen sein.
- Dachzugangstüren und Serviceluken müssen gesperrt und alarmiert sein.

### Authentifizierung nach Zone

| Sicherheitszone | Mindest-Authentifizierung | Zusätzliche Anforderungen |
|-----------------|--------------------------|--------------------------|
| **Kontrollierte Zone** | Badge/Karte (RFID, mobile Zugangsdaten) | — |
| **Eingeschränkte Zone** | Badge + PIN | Zugang protokolliert mit Identität und Zeitstempel |
| **Hochsicherheitszone** | Badge + PIN + Biometrie ODER Zwei-Personen-Kontrolle | Zugang protokolliert; CCTV am Eingang; Zugang ausserhalb der Geschäftszeiten erzeugt Alert |

**Anforderungen an das Zugangskontrollsystem**:

- Das Zugangskontrollsystem muss alle Zugangsereignisse (gewährt und abgelehnt) mit Identität, Zeitstempel und Zugangspunkt protokollieren.
- Zugriffsrechte müssen rollenbasiert und auf Need-to-know/Need-to-access-Basis gewährt werden.
- Zugriffsrechte müssen mindestens vierteljährlich überprüft werden; der Zugang zu eingeschränkten Zonen und Hochsicherheitszonen muss vom genehmigenden Manager erneut bestätigt werden.

**Vierteljährlicher Zugriffsüberprüfungsprozess**:

1. **Berichterstellung**: Der Facilities Manager erstellt einen Zugriffsrechte-Bericht aus dem [Zugangskontrollsystem], der alle Personen mit Zonenzugang, gruppiert nach Zone und Abteilung, anzeigt (fällig: 1. Arbeitstag des Überprüfungsmonats).
2. **Manager-Bestätigung**: Direkte Vorgesetzte erhalten die Zugangs-Liste ihres Teams; bestätigen, dass der Zonenzugang jeder Person noch erforderlich ist; identifizieren zu widerrufende Zugänge (fällig: 14 Tage nach Berichtsverteilung).
3. **Widerrufsdurchführung**: Der Facilities Manager widerruft unnötige Zugänge innerhalb von 5 Arbeitstagen nach der Manager-Bestätigung.
4. **Prüfpfad**: Bestätigungsunterlagen (E-Mail-Bestätigungen, unterzeichnete Formulare oder [GRC-Tool]-Workflow-Aufzeichnungen) werden 3 Jahre aufbewahrt.

**Umgang mit Nicht-Antworten**: Manager, die nicht innerhalb von 14 Tagen antworten, erhalten eine Eskalation an den Abteilungsleiter. Der Zugang für nicht bestätigte Nutzer in eingeschränkten Zonen/Hochsicherheitszonen wird bis zur Bestätigung gesperrt.

- Der physische Zugang von Mitarbeitenden bei Kündigung muss am selben Tag der Beendigung des Arbeitsverhältnisses widerrufen werden, koordiniert mit HR.
- Verlorene, gestohlene oder beschädigte Badges müssen sofort gemeldet und gemäss folgender Frist deaktiviert werden:

| Badge-Typ | Deaktivierungsfrist | Zusätzliche Massnahmen |
|-----------|--------------------|-----------------------|
| **Hochsicherheitszone-Badge** | **Sofort** (innerhalb von 30 Minuten nach Meldung) | ISB-Benachrichtigung; Zugangsprotokoll-Überprüfung für 72 Stunden davor; Neuausstellung mit neuer Zugangsdaten-Nummer |
| **Eingeschränkte Zone-Badge** | Innerhalb von 2 Stunden | Zugangsprotokoll-Überprüfung bei verdächtigen Umständen |
| **Kontrollierte Zone-Badge** | Innerhalb von 4 Stunden | Standard-Ersatzverfahren |

**Verlorener Badge ausserhalb der Geschäftszeiten**: Bereitschafts-Einrichtungskontakt sofort für eingeschränkte/Hochsicherheitszonen-Badges benachrichtigen; Deaktivierung erfolgt remote.

- Das Teilen und Verleihen von Badges ist untersagt.
- Temporäre Zugangskarten müssen zeitlich begrenzt sein und automatisch ablaufen.

### Mitarbeitendenzugang

- Der Mitarbeitendenzugang muss auf dem Prinzip der minimalen Rechte basieren, nur Zugang zu den für die Mitarbeitendenrolle erforderlichen Zonen gewähren.
- Zugangsdaten (Badges, Karten, mobile Zugangsdaten) müssen an jeden Mitarbeitenden individuell ausgegeben werden und die Person identifizieren. Badges müssen jederzeit sichtbar auf dem Gelände getragen werden (Umhängeband, Clip oder Badge-Halterung). Verdeckte oder verborgene Badges können vom Sicherheitspersonal angesprochen werden.

**Badge-Anforderungen**:
- Mitarbeitenden-Badges müssen enthalten: Foto, Name, Mitarbeitenden-ID, Zonenzugangskennzeichnung (farbkodiert oder textbasiert).
- Besucher-Badges müssen deutlich von Mitarbeitenden-Badges unterscheidbar sein (auffällige Farbe, „BESUCHER"-Kennzeichnung, kein kodierter Zonenzugang).
- Auftragnehmer-Badges müssen unterscheidbar sein und ein Ablaufdatum enthalten.
- Temporäre Badges (Ersatz für verlorene Dauerbadges) müssen mit „TEMPORÄR" gekennzeichnet sein und nach 7 Tagen automatisch ablaufen.
- Zugangsdaten dürfen nicht geteilt, übertragen oder anderen Personen geliehen werden.
- Der Zugang muss bei Beendigung des Arbeitsverhältnisses sofort widerrufen werden; alle physischen Zugangsdaten müssen deaktiviert und zurückgegeben werden. HR muss die Einrichtungsabteilung über alle Beendigungen am oder vor dem letzten Arbeitstag informieren.
- Rollenwechsel müssen auf physische Zugangsimplikationen bewertet werden; Zugang zu Zonen, die für die neue Rolle nicht mehr erforderlich sind, muss innerhalb von 5 Arbeitstagen widerrufen werden.

**Zugriffsprotokoll-Aufbewahrung**: Protokolle des physischen Zugangskontrollsystems müssen mindestens 12 Monate aufbewahrt werden (oder länger, wenn anwendbare Vorschriften oder Verträge dies erfordern), gegen unbefugte Änderungen geschützt und innerhalb von 2 Arbeitstagen für Audit- und Incident-Response-Zwecke verfügbar sein.

### Besuchermanagement

**Besucherregistrierung**:

- Alle Besucher müssen sich am Empfang anmelden, bevor sie über die öffentliche Zone hinausgehen. Die Registrierung muss im [Besucherverwaltungssystem] (oder im Papier-Besucherlogbuch) erfasst werden und enthalten: Besuchername, Unternehmen/Organisation, Gastgeber (besuchter Mitarbeitender), Datum und Uhrzeit der Ankunft sowie Besuchszweck.
- Besucher müssen einen gültigen Lichtbildausweis vorlegen.
- Besucher-Badges müssen deutlich von Mitarbeitenden-Badges unterscheidbar sein (auffällige Farbe, „BESUCHER"-Kennzeichnung, kein kodierter Zonenzugang).
- Besucher müssen bei der Abreise Badges zurückgeben und sich abmelden. Nicht zurückgegebene Badges müssen bis Ende des Geschäftstages deaktiviert werden.

**Begleitung und Beaufsichtigung**:

- Besucher in kontrollierten Zonen dürfen sich ohne Begleitung bewegen, wenn der Gastgeber den Besuch bestätigt hat und der Besucher-Badge den weiteren Zonenzugang einschränkt.
- Besucher in eingeschränkten Zonen müssen jederzeit von einem autorisierten Mitarbeitenden begleitet werden.
- Besucher in Hochsicherheitszonen müssen jederzeit von einem autorisierten Mitarbeitenden mit ausdrücklichem Zonenzugang begleitet werden, und der Besuch muss vom Zonen-Eigentümer vorab genehmigt werden.
- Der Besucherzugang zu Hochsicherheitszonen muss schriftlich (per E-Mail oder [Besucherverwaltungssystem]-Genehmigung) vor der Ankunft vorab autorisiert werden.

**Aufbewahrung von Besucherprotokollen**:

- Besucherprotokolle müssen mindestens 12 Monate aufbewahrt und gegen unbefugte Änderungen geschützt werden.
- Protokolle müssen innerhalb von 2 Arbeitstagen für Audit- oder Incident-Untersuchungen verfügbar sein.

**Zugang von Auftragnehmern und Wartungspersonal**:

- Auftragnehmer und Wartungspersonal müssen vor der Ankunft vorab autorisiert werden, mit dokumentiertem Arbeitsumfang und Zugangsbereichen.
- Der Auftragnehmerzugang muss zeitlich begrenzt und protokolliert sein.
- Auftragnehmer, die auf eingeschränkte Zonen oder Hochsicherheitszonen zugreifen, müssen begleitet und ihre Arbeit beaufsichtigt werden, wenn sensible Systeme oder Daten zugänglich sind.
- Externe Wartung an Sicherheitssystemen (Alarme, Zugangskontrolle, CCTV) muss unter direkter Aufsicht eines autorisierten Mitarbeitenden durchgeführt werden.

### Liefer- und Ladebereiche

- Der Zugang zu Liefer- und Ladebereichen von ausserhalb des Gebäudes muss auf identifiziertes und autorisiertes Lieferpersonal beschränkt sein.
- Liefer- und Ladebereiche müssen so gestaltet (oder betrieblich verwaltet) werden, dass Lieferpersonal keinen Zugang zu anderen Gebäudebereichen erhält.
- Aussentüren eines Liefer- und Ladebereichs müssen gesichert sein, wenn die Innentüren zu Betriebsbereichen geöffnet sind; beide sollen, wo vermeidbar, nicht gleichzeitig geöffnet sein.
- Eingangsmaterial muss vor dem Transport aus dem Lieferbereich auf Anzeichen von Manipulation untersucht werden.
- Eingangsmaterial muss gemäss den Asset-Management-Verfahren beim Betreten des Geländes registriert werden.
- Ein- und ausgehende Sendungen müssen, wo machbar, physisch getrennt werden.
- Eingangsmaterial muss auf Gefahrstoffe untersucht werden, wenn die Risikobewertung dies erfordert (kontextabhängig: chemische, biologische oder explosive Risiken).

---

## Sicherung von Büros, Räumen und Einrichtungen (A.7.3)

**ISO/IEC 27001:2022 Annex A.7.3 — Sicherung von Büros, Räumen und Einrichtungen**:

> *Die physische Sicherheit von Büros, Räumen und Einrichtungen sollte konzipiert und umgesetzt werden.*

### Allgemeine Bürosicherheit

- Büros müssen ausserhalb der Geschäftszeiten bei Abwesenheit gesperrt sein.
- Die Regelung zum aufgeräumten Schreibtisch muss durchgesetzt werden — sensible Dokumente müssen bei Nichtgebrauch in gesperrten Aufbewahrungsmöglichkeiten gesichert sein.
- Bildschirme müssen so positioniert sein, dass das Einsehen über die Schulter durch Besucher oder Vorbeigehen verhindert wird.
- Aufbewahrungsmöglichkeiten (Schränke, Safes, gesperrte Schubladen) müssen für die Sicherung klassifizierter Dokumente und tragbarer Medien bereitgestellt werden.
- Kritische Einrichtungen sollten so gelegen sein, dass der Zugang durch die Öffentlichkeit vermieden wird, und sollten minimale Hinweise auf ihren Zweck geben, ohne offensichtliche externe Beschilderung, die auf das Vorhandensein von Informationsverarbeitungsaktivitäten hinweist.
- Einrichtungen sollten so konfiguriert sein, dass vertrauliche Informationen oder Aktivitäten von aussen nicht sichtbar oder hörbar sind.

### Sensible Bereiche

Bereiche, die vertrauliche oder eingeschränkte Informationen verarbeiten (z. B. HR, Finanzen, Rechtsabteilung, Führungsbüros) müssen aufweisen:

- Zugangskontolen entsprechend der Zonenklassifizierung (mindestens eingeschränkte Zone).
- Zugangsprotokolle, die geführt und überprüft werden.
- Fenster zu sensiblen Bereichen, die mattiert, abgedeckt oder mit Sichtschutzfolie versehen sind, um visuelle Beobachtung zu verhindern.
- Aufnahme-Geräte (Kameras, Telefone mit Kameras), die eingeschränkt oder verboten sind, sofern nicht ausdrücklich genehmigt.

### Serverräume und Rechenzentren

**Für von [Organisation] kontrollierte Serverräume und Rechenzentren**:

**Zugangskontrolle**:

- Der Zugang muss auf autorisiertes IT-Personal beschränkt sein, mit geführten namentlichen Zugangslisten.
- Multi-Faktor-Authentifizierung muss vorgeschrieben sein (Badge + PIN + Biometrie oder Zwei-Personen-Kontrolle).
- Alle Zugriffe müssen mit Identität und Zeitstempel protokolliert werden.
- Besucher und Auftragnehmer in Serverräumen müssen jederzeit begleitet werden.

**Physische Bauweise**:

- Keine Aussenfehnster.
- Verstärkte Wände, Böden und Decken.
- Raumhohe Trennwände (vom Rohboden bis zur Rohdecke, nicht abgehängte Decke).
- Umgebungsüberwachung (Feuerlöschung, Wassererkennung, Temperatur- und Feuchtigkeitssensoren).
- CCTV-Abdeckung mit Aufzeichnung (Aufbewahrung gemäss ISMS-OP-POL-A.7.4-5-11).

**Zugangsprotokollierung und -überwachung** (Serverräume und Rechenzentren):
- Alle Zugriffe werden mit Identität, Zeitstempel, Ein-/Austrittszeit protokolliert.
- Zugriffsprotokolle werden **wöchentlich** vom IT-Sicherheitsbeauftragten überprüft.
- Anomalien werden untersucht (Zugang ausserhalb der Geschäftszeiten, ungewöhnliche Zugriffsmuster, unerwartete Besucher).
- Zugriffsprotokoll-Aufbewahrung: **3 Jahre** (länger als die Standard-12-Monate aufgrund des Schutzes kritischer Werte).
- Echtzeit-Alerts für: ungeplanter Zugang ausserhalb der Geschäftszeiten, wiederholte fehlgeschlagene Authentifizierungsversuche, Tür offen > 2 Minuten.
- **Korrelation von physischem Zugang und Änderungen**: Wenn Server-/Infrastrukturänderungen auftreten, werden Zugriffsprotokolle überprüft, um zu verifizieren, dass autorisiertes Personal die Arbeit durchgeführt hat.

**Für Rechenzentren Dritter und Colocation**:

- Gleichwertige Schutzmassnahmen müssen durch Lieferantensicherung (ISO 27001-Zertifikat, SOC 2 Type II-Bericht) und vertragliche Sicherheitsanforderungen gewährleistet werden.
- Wo eine genaue Gleichwertigkeit nicht möglich ist, muss eine dokumentierte Risikobehandlung mit Kompensationskontrollen aufgezeichnet werden.

### Besprechungsraumsicherheit

- Besprechungsräume müssen vor sensiblen Gesprächen auf Aufnahmegeräte oder zurückgelassene Materialien überprüft werden.
- Whiteboards und Flipcharts müssen nach Besprechungen gelöscht oder entfernt werden.
- Dokumente dürfen nach Besprechungsende nicht in Besprechungsräumen zurückgelassen werden.
- Videokonferenzgeräte müssen bei Nichtgebrauch gesichert sein; Kameras und Mikrofone müssen zwischen Besprechungen in einem bekannten Aus-Zustand sein.

### Netzwerkzugangspunkte und Verkabelung

- Der physische Zugang zu Netzwerkgeräten (Switches, Router, WLAN-Access-Points, Patch-Panels) muss auf autorisiertes IT-Personal beschränkt sein.
- Netzwerkbuchsen und -ports in öffentlichen Zonen müssen deaktiviert sein oder keinen Zugang zum internen Netzwerk ermöglichen.
- Netzwerkbuchsen und -ports in kontrollierten Zonen, die Zugang zum internen Netzwerk ermöglichen, müssen durch die physischen Zugangskontolen der Zone gesichert sein.
- Besucher dürfen keine Geräte an interne Netzwerkports anschliessen, sofern nicht ausdrücklich genehmigt und begleitet.
- Strom- und Telekommunikationskabel, die Daten übertragen, müssen vor Abhören, Störungen und Beschädigungen geschützt sein.
- Stromkabel müssen von Kommunikationskabeln getrennt werden, um Störungen zu vermeiden.
- Der Zugang zu Kabelräumen und Patch-Panels muss durch physische Zugangskontolen eingeschränkt sein (mindestens eingeschränkte Zone).
- Wo eine unterirdische Kabelführung ins Gebäude möglich ist, sollten Strom- und Telekommunikationsleitungen zu Informationsverarbeitungseinrichtungen unterirdisch verlegt werden.

### Gesicherte Bereiche — Zusätzliche Anforderungen

Zusätzlich zu den zonenbasierten Controls oben gelten folgende Anforderungen für alle designierten gesicherten Bereiche (eingeschränkte Zonen und Hochsicherheitszonen):

- Zugriffsrechte für gesicherte Bereiche gelten standardmässig als verweigert — Zugang wird nur bei ausdrücklicher Genehmigung gewährt.
- Foto-, Video-, Audio- oder andere Aufnahmegeräte (einschliesslich Kameras in mobilen Geräten) dürfen nicht in gesicherten Bereichen zugelassen werden, sofern nicht ausdrücklich vom Zoneneigentümer genehmigt.
- Personal, das in gesicherten Bereichen arbeitet, muss über die spezifischen Sicherheitsanforderungen und Einschränkungen für diesen Bereich informiert werden.
- Das unbeaufsichtigte Arbeiten in Hochsicherheitszonen sollte aus Sicherheitsgründen und zur Vermeidung von Möglichkeiten für böswillige Aktivitäten vermieden werden.

### Schulung und Sensibilisierung

**Jährliche physische Sicherheits-Awareness-Schulung** für alle Mitarbeitenden:
- Badge-Nutzung (sichtbar tragen, nicht teilen, verlorene Badges sofort melden)
- Ansprechen unbekannter Personen (höfliche Anfrage: „Kann ich Ihnen helfen?" oder „Haben Sie eine Begleitung?")
- Tailgating-Prävention (Türen nicht aufhalten, eine Person pro Badge-Scan)
- Regelung zum aufgeräumten Schreibtisch (Dokumente beim Verlassen des Schreibtisches sperren)
- Meldung von physischen Sicherheitsvorfällen (was, wie und wem zu melden)
- Verantwortlichkeiten bei der Besucherbegleitung

**Rollenspezifische Schulungen**:
- **Empfang/Sicherheit**: Besuchermanagementverfahren, Badge-Ausgabe/-Deaktivierung, Notfallverfahren.
- **Einrichtungen**: Betrieb des Zugangskontrollsystems, Zonenverwaltung, Auftragnehmer-Begleitungsanforderungen.
- **IT**: Sicherheit von Netzwerkzugangspunkten, Serverraumzugangsverfahren, Geräteraumsicherheit.

**Schulung für neue Mitarbeitende**: Physische Sicherheitsschulung innerhalb von **5 Arbeitstagen** nach dem Eintrittsdatum, vor der Gewährung des Zonenzugangs.

Schulungsabschlüsse werden verfolgt; Ziel: **95% Abschlussrate** jährlich.

### Physische Sicherheitsbegehungen

Die Compliance mit Büro-, Besprechungsraum- und Einrichtungssicherheitsanforderungen wird durch dokumentierte physische Sicherheitsbegehungen verifiziert:

- **Häufigkeit**: Mindestens vierteljährlich und nach jedem wesentlichen Sicherheitsvorfall oder Einrichtungswechsel.
- **Umfang**: Alle Sicherheitszonen, Zugangspunkte, sensible Bereiche, Serverräume, Kabelräume und Besprechungsräume.
- **Ergebnisse**: Als Nichtkonformitäten oder Verbesserungsmassnahmen mit zugewiesenem Eigentümer, Fälligkeitsdatum und Nachverfolgung bis zum Abschluss dokumentiert.
- **Checkliste**: Eine standardisierte Begehungs-Checkliste muss geführt und für alle Inspektionen verwendet werden.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Geschäftsleitung** | Genehmigt die Richtlinie; stellt Budget für physische Sicherheitsinfrastruktur bereit; erhält Berichte zur physischen Sicherheitslage |
| **ISB** | Richtlinieneigentümerschaft; definiert physische Sicherheitsstandards; überwacht die Compliance; genehmigt Ausnahmen; überprüft physische Sicherheitskennzahlen |
| **Facilities Manager** | Implementiert und unterhält physische Sicherheitskontrollen; verwaltet Zugangskontrollsysteme; koordiniert Gebäudesicherheit; verwaltet Auftragnehmer und Wartung |
| **IT-Sicherheit** | Integriert physische und logische Zugangskontolen; verwaltet die Sicherheit von Netzwerkzugangspunkten; überprüft Serverraumzugang; unterstützt Incident Response |
| **Empfang / Sicherheitspersonal** | Betreibt Besuchermanagement; überwacht Zugangspunkte; reagiert auf Alarme und Alerts; spricht unbekannte Personen an |
| **Direkte Vorgesetzte** | Genehmigen physischen Zugang für Teammitglieder; überprüfen und bestätigen Zugriffsrechte vierteljährlich; melden Abgänge und Rollenwechsel für den Zugangswiderruf |
| **HR** | Benachrichtigt Einrichtungsabteilung über Neueinstellungen, Rollenwechsel und Beendigungen für die Zugangsverwaltung/-widerruf; verwaltet das Onboarding von Auftragnehmern |
| **Alle Mitarbeitenden** | Befolgen Zugangsverfahren; tragen Badges sichtbar; sprechen unbekannte Personen an oder melden sie; melden verlorene Badges und physische Sicherheitsereignisse; halten die Regelung zum aufgeräumten Schreibtisch ein |

**Eskalationspfade**:

### Meldung von physischen Sicherheitsvorfällen

Alle Mitarbeitenden müssen physische Sicherheitsereignisse sofort dem Empfang, dem Facilities Manager oder dem Sicherheitspersonal melden. Meldepflichtige Ereignisse umfassen:

**Kritisch (sofortige Eskalation an ISB)**:
- Unbefugte Person in eingeschränkter Zone oder Hochsicherheitszone entdeckt
- Anzeichen physischen Einbruchs (aufgebrochene Türen, zerbrochene Fenster, manipulierte Schlösser)
- Diebstahl oder vermuteter Diebstahl von Geräten oder Dokumenten
- Physische Drohungen oder Konfrontationen auf dem Gelände
- Entdecktes Badge-Cloning oder -Manipulation

**Hohe Priorität**:
- Erfolgreiches Tailgating in eine gesicherte Zone
- Unbegleiteter Besucher in der kontrollierten Zone
- Absichtlich aufgehaltene Sicherheitstür (bewusste Umgehung)
- Verlorener Badge mit Zugang zur Hochsicherheitszone oder eingeschränkten Zone

**Standardpriorität**:
- Verlorener Badge mit ausschliesslichem Zugang zur kontrollierten Zone
- Besucher ohne Badge hinter dem Empfang
- Einrichtungsmangel (defektes Schloss, fehlerhafter Türsensor)
- Verstoss gegen die Regelung zum aufgeräumten Schreibtisch

**Meldekanäle**: Empfang (während der Öffnungszeiten), Facilities Manager, [Notfallnummer] (ausserhalb der Geschäftszeiten), ISB (für kritische Ereignisse).

**Eskalationspfade**:

- **Physische Sicherheitsvorfälle**: Mitarbeitende/Sicherheitspersonal --> Facilities Manager --> ISB --> Geschäftsleitung
- **Zugriffsanfragen**: Mitarbeitende --> Direkter Vorgesetzter (Genehmigung) --> Facilities Manager (Bereitstellung)
- **Besucherprobleme**: Empfang --> Facilities Manager --> ISB
- **Verlorene/gestohlene Badges**: Mitarbeitende --> Empfang/Einrichtungen (sofortige Deaktivierung) --> IT-Sicherheit (falls Systemzugangsimplikationen)
- **Auftragnehmer-Nichtkonformität**: Begleitung/Vorgesetzte --> Facilities Manager --> Beschaffung/Vertragsverantwortliche

---

## Nachweise für diese Richtlinie

| # | Nachweis | Eigentümer | Häufigkeit | Aufbewahrung |
|---|---------|------------|------------|-------------|
| 1 | **Sicherheitszonendokumentation und Grundrisse** mit Zonengrenzen, Zugangspunkten und Zugangskontrollmechanismen | Facilities Manager | Bei Einrichtungsänderungen aktualisiert; jährlich überprüft | Aktuelle + vorherige Version |
| 2 | **Konfiguration des Zugangskontrollsystems** — Zonenzuweisungen, Authentifizierungsstufen, rollenbasierte Zugriffsregeln | Facilities Manager / IT | Vierteljährlich überprüft | Aktuelle Konfiguration + Änderungsprotokoll |
| 3 | **Zugangsprotokolle** — Ein-/Austritts-Ereignisse mit Identität, Zeitstempel, Zugangspunkt (gewährt und abgelehnt) | [Zugangskontrollsystem] | Fortlaufend; monatlich auf Anomalien überprüft | Mindestens 12 Monate |
| 4 | **Besucherprotokolle** — Registrierungsunterlagen mit Name, Unternehmen, Gastgeber, Datum/Uhrzeit Ein-/Austritt, verifiziertem Ausweis | Empfang / [Besucherverwaltungssystem] | Fortlaufend | Mindestens 12 Monate |
| 5 | **Zugriffsrechte-Überprüfungsunterlagen** — vierteljährliche Überprüfung der Mitarbeitendenzugriffsrechte mit Manager-Bestätigung | Facilities Manager / Direkte Vorgesetzte | Vierteljährlich | 3 Jahre |
| 6 | **Perimeterinspektionsberichte** — dokumentierte Ergebnisse der Gebäude- und Zonen-Perimeterinspektionen | Facilities Manager | Jährlich (Gebäude); vierteljährlich (eingeschränkte/Hochsicherheitszonen) | 3 Jahre |
| 7 | **Physische Sicherheitsbegehungsberichte** — Checklistenergebnisse, Ergebnisse und Massnahmen-Nachverfolgung | Facilities Manager / ISB | Vierteljährlich | 3 Jahre |
| 8 | **Badge-Management-Unterlagen** — Ausgabe, Ersatz, Deaktivierung, Verlust-/Diebstahlmeldungen | Facilities Manager | Pro Ereignis; jährlich geprüft | Beschäftigungsdauer + 1 Jahr |
| 9 | **Auftragnehmer- und Wartungszugangsunterlagen** — Vorabgenehmigung, Umfang, Begleitungsunterlagen | Facilities Manager | Pro Einsatz | 3 Jahre |
| 10 | **Lieferantenabsicherungsunterlagen** für Colocation/gemeinsam genutzte Einrichtungen — Zertifikate, SOC-Berichte, Vertragsbedingungen | ISB / Beschaffung | Jährlich überprüft | Vertragsdauer + 2 Jahre |
| 11 | **Ausnahmenregister** — genehmigte Ausnahmen mit Begründung, Kompensationskontrollen, Ablaufdatum | ISB | Pro Ausnahme aktualisiert; vierteljährlich überprüft | 3 Jahre nach Ausnahmenabschluss |
| 12 | **Physische Sicherheitsvorfallberichte** — unbefugte Zugriffsversuche, Badge-Verluste, Tailgating-Ereignisse, Perimeterdurchbrüche | ISB / Facilities Manager | Pro Vorfall | 3 Jahre |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Management-Team überprüft die Compliance mit dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf: Berichte des Zugangskontrollsystems, Besucherprotokoll-Audits, Ergebnisse von Sicherheitsbegehungen, Abschlussquoten der Zugriffsrechte-Überprüfungen, Badge-Management-Kennzahlen, Lieferantenabsicherungsüberprüfungen, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Kennzahlen**:

| Kennzahl | Ziel | Überprüfungsfrequenz |
|----------|------|---------------------|
| Zugangskontroll-Abdeckung (% der Zugangspunkte mit aktiven Controls) | 100% | Vierteljährlich |
| Fristgerecht abgeschlossene Zugriffsrechte-Überprüfungen | 100% | Vierteljährlich |
| Besucher-Begleitungs-Compliance (eingeschränkte/Hochsicherheitszonen) | 100% | Monatlich |
| Zugang von gekündigten Mitarbeitenden am selben Tag widerrufen | 100% | Pro Ereignis; monatlich geprüft |
| Badge-Verlust/-Diebstahlvorfälle | < 5 pro Quartal | Vierteljährlich |
| Unbefugte Zugriffsversuche (erfolgreich) | 0 | Monatlich |
| Abschluss physischer Sicherheitsbegehungen | 100% planmässig | Vierteljährlich |
| Aktuelle Lieferantenabsicherungsüberprüfungen | 100% | Jährlich |

**Berichterstattung**:
- **Monatliches Dashboard** an ISB: Compliance beim Zugangswiderruf, Badge-Verlust-Vorfälle, unbefugte Zugriffsversuche, Besucher-Begleitungs-Compliance.
- **Vierteljährlicher Bericht** an Geschäftsleitung: Alle Kennzahlen, Trendanalyse, Begehungsergebnisse, Ausnahmenstatus.
- **Jahresbericht** an Management Review: Wirksamkeit des physischen Sicherheitsprogramms, Investitionsempfehlungen, regulatorischer Compliance-Status.

Kennzahlen, die Ziele nicht erreichen, werden sofort an den ISB eskaliert und einen Massnahmenplan mit Eigentümer und Zieldatum umfassen.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vorab vom ISB genehmigt und dokumentiert werden, mit dokumentierter Geschäftsbegründung, Risikobewertung, Kompensationskontrollen und einem definierten Ablaufdatum (maximal 6 Monate, verlängerbar mit Neubewertung). Ausnahmen sind dem Management-Review-Team zu melden.

**Zulässige Ausnahmen** (mit geeigneten Kompensationskontrollen):

- Temporärer Notfallzugang für dringende Reparaturen (mit verstärkter Überwachung und Begleitung).
- Verlängerter Besucherzugang für Prüfer oder Regulatoren (mit dokumentierter Genehmigung und Umfang).
- Alternative Authentifizierungsmethoden für Personal mit Zugänglichkeitsanforderungen.

**Nicht zulässig** als Ausnahmen:

- Permanente Umgehung von Zonen-Authentifizierungsanforderungen.
- Ausnahmen ohne Kompensationskontrollen.
- Ausnahmen vom taggleichen Zugangswiderruf für gekündigte Mitarbeitende.

## Nicht-Compliance

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen bis hin zur Kündigung des Arbeitsverhältnisses unterliegen. Spezifische Nicht-Compliance-Szenarien und Reaktionen:

- **Tailgating oder Tailgating ermöglichen**: Formelle Verwarnung; wiederholter Verstoss löst Disziplinarverfahren aus.
- **Badge teilen oder verleihen**: Sofortige Badge-Deaktivierung; Disziplinarverfahren.
- **Versäumnis, unbekannte Personen anzusprechen oder zu melden**: Durch Awareness-Schulung adressiert.
- **Absichtliches Offenhalten gesicherter Türen**: Sofortige Behebung; formelle Verwarnung bei absichtlichem Handeln.

Bei Auftragnehmern, die gegen die Richtlinie verstossen, kann der Zugang widerrufen und die Auftragnehmerorganisation benachrichtigt werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen:

- Einrichtungsänderungen (Büroumzüge, Renovierungen, neue Standorte, Mietänderungen).
- Physische Sicherheitsvorfälle und Beinahe-Vorfälle (unbefugter Zugang, Tailgating, Perimeterdurchbrüche).
- Audit-Ergebnisse und Begehungsergebnisse.
- Fortschritte in der Zugangskontrolltechnologie (mobile Zugangsdaten, kontaktlose Biometrie, KI-gestützte Anomalieerkennung).
- Regulatorische Änderungen (insbesondere nDSG, kantonale Datenschutzanforderungen und DSGVO-Updates).
- Änderungen der Bedrohungslandschaft (z. B. verstärktes Social Engineering für physischen Zugang).
- Aus Sicherheitsereignissen beim Unternehmen oder in der Branche gezogene Lehren.

Verbesserungsmassnahmen müssen verfolgt, einem Eigentümer zugewiesen und dem ISB und dem Management-Review-Team gemeldet werden.

---

# Abgedeckte Bereiche des ISO 27001-Standards

Richtlinie zur physischen Zugangskontrolle — ISO 27001:2022-Control-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Politik | 5.4 Managementverantwortlichkeiten |
| Klausel 6.1 Massnahmen zum Umgang mit Risiken und Chancen | 5.36 Compliance mit Richtlinien, Regeln und Standards |
| Klausel 6.2 Informationssicherheitsziele | 6.3 Informationssicherheitsbewusstsein, -schulung und -ausbildung |
| Klausel 7.3 Bewusstsein | 6.4 Disziplinarverfahren |
| Klausel 8.1 Betriebsplanung und -steuerung | **7.1 Physische Sicherheitsperimeter** |
| Klausel 9.1 Überwachung, Messung, Analyse, Auswertung | **7.2 Physischer Zutritt** |
| Klausel 10.2 Nichtkonformität und Korrekturmassnahmen | **7.3 Sicherung von Büros, Räumen und Einrichtungen** |
| | 7.4 Physische Sicherheitsüberwachung |
| | 7.6 Arbeiten in gesicherten Bereichen |
| | 7.8 Geräteaufstellung und -schutz |

---

# Regulatorischer Rahmen

| Rahmenwerk | Anwendbarkeit | Relevanz für die physische Zugangskontrolle |
|------------|--------------|---------------------------------------------|
| **Schweizerisches nDSG (revDSG)** | **Obligatorisch** — alle Personendatenverarbeitung | Art. 8 — Dem Risiko angemessene technische und organisatorische Massnahmen; physische Sicherheit der Räumlichkeiten, in denen Personendaten verarbeitet oder gespeichert werden |
| **Schweizerische DSV (Datenschutzverordnung)** | **Obligatorisch** — ergänzt das nDSG | Art. 1-3 — Mindestanforderungen an die Datensicherheit, einschliesslich physischer Zugangskontolen |
| **ISO/IEC 27001:2022** | **Obligatorisch** — Zertifizierungsumfang | Annex A Controls 7.1, 7.2, 7.3 |
| **ISO/IEC 27002:2022** | **Leitlinie** | Abschnitte 7.1, 7.2, 7.3 — Implementierungshinweise für physische Controls |
| **EU DSGVO** | **Bedingt** — bei Verarbeitung von EU/EWR-Personendaten | Art. 32 — Sicherheit der Verarbeitung, einschliesslich physischer Sicherheitsmassnahmen |
| **PCI DSS v4.0** | **Bedingt** — bei Verarbeitung von Zahlungskartendaten | Anforderung 9 — Einschränkung des physischen Zugangs zu Karteninhaberdaten; erfordert badge-kontrollierten Zugang, Besucherprotokolle, Medienvernichtungsverfahren |
| **FINMA Rundschreiben 2023/1** | **Bedingt** — schweizerische regulierte Finanzinstitute | Operatives Risikomanagement einschliesslich physischer Sicherheit der kritischen Infrastruktur |
| **NIST SP 800-53 Rev 5** | **Leitlinie** | PE-Familie — Physische und umgebungsbezogene Schutzkontrollen |
| **CIS Controls v8** | **Leitlinie** | Control 3 (Datenschutz), Control 6 (Access Control Management) — physische Zugangsdimensionen |

---

<!-- QA_VERIFIED: 2026-03-29 -->
