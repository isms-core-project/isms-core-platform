<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.6-7-14-DE:operational:OP-POL:a.7.6-7-14 -->
**ISMS-OP-POL-A.7.6-7-14 — Gesicherte Bereiche und Medienhandhabung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Gesicherte Bereiche und Medienhandhabung |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.7.6-7-14 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstveröffentlichung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Control A.7.6 — Arbeiten in gesicherten Bereichen
- ISO/IEC 27001:2022 Control A.7.7 — Aufgeräumter Schreibtisch und aufgeräumter Bildschirm
- ISO/IEC 27001:2022 Control A.7.14 — Sichere Entsorgung oder Wiederverwendung von Geräten
- ISO/IEC 27002:2022 Abschnitte 7.6, 7.7, 7.14 — Implementierungshinweise
- NIST SP 800-88 Rev. 2 — Leitlinien zur Mediensanierung
- IEEE 2883:2022 — Standard zur Sanitisierung von Speichermedien

**Verwandte Annex-A-Controls**:

| Control | Bezug zu gesicherten Bereichen und Medienhandhabung |
|---------|------------------------------------------------------|
| A.5.10–11 Akzeptable Nutzung und Rückgabe von Werten | Definiert die akzeptable Nutzung von Geräten und Rückgabe von Werten am Ende des Lebenszyklus |
| A.5.12–13 Informationsklassifizierung und Kennzeichnung | Die Klassifizierungsstufe bestimmt die Anforderungen für aufgeräumten Schreibtisch und die Wahl der Entsorgungsmethode |
| A.7.1–2–3 Physische Zugangskontrolle | Steuert den Zutritt zu gesicherten Bereichen; diese Richtlinie regelt das Verhalten innerhalb dieser Bereiche |
| A.7.8–9 Geräteaufstellung und Sicherheit ausserhalb der Betriebsstätten | Physische Platzierung und Schutz von Geräten vor der Entsorgung |
| A.7.10 Speichermedien | Lifecycle-Management von Medien; diese Richtlinie behandelt die Entsorgung am Ende der Lebensdauer |
| A.8.10 Informationslöschung | Logische Löschanforderungen, die physische Entsorgungsmethoden ergänzen |

**Verwandte interne Richtlinien**:

- Richtlinie zur physischen Zugangskontrolle
- Informationsklassifizierungs- und Handhabungsrichtlinie
- Asset-Management-Richtlinie
- Endgerätesicherheitsrichtlinie

---

# Richtlinie zu gesicherten Bereichen und Medienhandhabung

## Zweck

Der Zweck dieser Richtlinie ist es, den Schutz von Informationen in gesicherten Bereichen durch angemessene Arbeitsverfahren sicherzustellen, unbefugten Zugang zu Informationen durch die Regelungen zum aufgeräumten Schreibtisch und aufgeräumten Bildschirm zu verhindern sowie den Datenverlust aus zu entsorgenden oder wiederzuverwendenden Geräten zu verhindern.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz von Personendaten (einschliesslich besonders schützenswerter Personendaten) beim Arbeiten in gesicherten Bereichen und bei der Geräteentsorgung umsetzt. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten zusätzlich die DSGVO-Anforderungen. Beide Rahmenwerke verlangen, dass Personendaten auf Geräten vor der Entsorgung oder Wiederverwendung nicht wiederherstellbar gemacht werden.

Die Controls A.7.6 (Arbeiten in gesicherten Bereichen), A.7.7 (Aufgeräumter Schreibtisch und aufgeräumter Bildschirm) und A.7.14 (Sichere Entsorgung oder Wiederverwendung von Geräten) werden zusammengefasst, da sie komplementäre Aspekte des physischen Informationsschutzes abdecken — vom täglichen Verhalten am Arbeitsplatz bis zur Handhabung von Werten am Ende ihrer Lebensdauer.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle gesicherten Bereiche, einschliesslich Serverräume, Rechenzentren, Security-Operations-Bereiche und eingeschränkte Büros.

Alle Arbeitsbereiche, in denen Informationen verarbeitet werden, einschliesslich Schreibtische, Besprechungsräume, gemeinsam genutzte Räume und Homeoffices.

Alle Geräte mit Speichermedien, einschliesslich Computer, Server, mobile Geräte, Drucker, Kopierer, USB-Sticks und Netzwerkgeräte.

## Grundsatz

Informationen müssen durch geeignete physische und verfahrensmässige Kontrollen während des gesamten Informations-Lebenszyklus vor unbefugtem Zugang, Offenlegung und Wiederherstellung geschützt werden — von der Erstellung und Handhabung in gesicherten Bereichen über die tägliche Arbeitsplatzdisziplin bis zur sicheren Entsorgung am Ende der Lebensdauer.

Entsorgungsmethoden müssen der Sensibilität der gespeicherten Informationen proportional sein, wie durch das Informationsklassifizierungsschema festgelegt.

Nur von der Organisation genehmigte Sanitisierungsmethoden und -tools dürfen für die Medienentsorgung verwendet werden. Die Entsorgung von Geräten mit Personendaten muss den Anforderungen des schweizerischen nDSG zur nicht wiederherstellbaren Vernichtung von Daten entsprechen.

Die Organisation führt ein Register genehmigter Sanitisierungstools (z. B. [Secure-Wipe-Tool]) und genehmigter Vernichtungslieferanten (z. B. [Vernichtungslieferant]). Dieses Register muss jährlich überprüft und bei Änderungen von Tools oder Lieferanten aktualisiert werden.

---

## Arbeiten in gesicherten Bereichen (A.7.6)

ISO/IEC 27001:2022 Annex A.7.6 besagt:

> *Sicherheitsmassnahmen für die Arbeit in gesicherten Bereichen sollten konzipiert und umgesetzt werden.*

### Zugang und Verhalten

Personal, das in gesicherten Bereichen arbeitet, muss folgende Anforderungen einhalten:

- Zugang zu gesicherten Bereichen darf nur autorisiertem Personal auf der Grundlage der Jobrolle und des Need-to-know-Prinzips gewährt werden.
- Personal darf über Aktivitäten in gesicherten Bereichen nur auf Need-to-know-Basis informiert werden.

**Informationsschutz in gesicherten Bereichen — Umfang der Einschränkung**:

- **Verbotene Offenlegungen**: Physische Sicherheitskontrollen (Schlosstypen, Alarmsysteme, Kamerapositionierungen, Zugangscodes); spezifische Inhalte gesicherter Bereiche (Gerätetypen/Modelle, Konfigurationen, gespeicherte Daten); Zugangskontrollverfahren (Badge-Typen, Begleitungsanforderungen, Genehmigungsprozess); Schwachstellen oder Sicherheitslücken in gesicherten Bereichen.
- **Zulässige Offenlegungen**: Allgemeine Existenz gesicherter Bereiche (z. B. „Wir haben einen Serverraum") — gilt nicht als sensibel. Allgemeiner Zweck (z. B. „Dort befindet sich unsere IT-Infrastruktur") — für allgemeines Bewusstsein akzeptabel.
- **Leitlinie**: Mitarbeitende sollten externen Parteien oder nicht autorisierten internen Parteien keine detaillierten Informationen über gesicherte Bereiche preisgeben. Bei Anfragen einer externen Partei (Lieferant, Besucher, Interviewer) an Facilities Manager oder ISB verweisen.
- **Verletzungsumfang**: Versehentliche Offenlegung nicht-sensibler Informationen (z. B. „Der Serverraum befindet sich im zweiten Stock") ist keine Verletzung. Absichtliche Offenlegung von Zugangscodes, Alarm-Deaktivierungsverfahren oder Sicherheitsschwachstellen ist eine Verletzung, die disziplinarischen Massnahmen unterliegt.
- Personal darf ausserhalb der normalen Geschäftszeiten nicht allein in gesicherten Bereichen arbeiten, sofern keine genehmigte Ausnahme mit Kompensationskontrollen vorhanden ist (z. B. Check-in-Verfahren mit Empfang oder Kollegen, CCTV-Überwachung oder Vier-Augen-Prinzip).
- Leere gesicherte Bereiche müssen physisch gesperrt und regelmässig überprüft werden.
- Fotografieren, Filmen, Audioaufnahmen oder andere Aufnahmen in gesicherten Bereichen sind untersagt, sofern nicht ausdrücklich schriftlich vom Eigentümer des gesicherten Bereichs genehmigt.
- Mobiltelefone, Kameras und aufnahmefähige Geräte dürfen nicht in Hochsicherheitsbereiche (z. B. Serverräume) mitgenommen werden, sofern nicht genehmigt.

### Drittpartei-Zugang

- Drittparteien (Auftragnehmer, Lieferanten, Besucher) müssen innerhalb gesicherter Bereiche jederzeit begleitet werden.
- Der Zugang von Drittparteien muss mit Ein- und Austrittszeiten protokolliert werden und ist zeitlich auf die Dauer der spezifischen Aufgabe begrenzt.
- Drittparteien müssen vor dem Betreten gesicherter Bereiche eine Vertraulichkeits- oder Geheimhaltungsvereinbarung unterzeichnen.
- Geräte von Drittparteien dürfen nicht ohne Genehmigung des Eigentümers des gesicherten Bereichs oder des Sicherheitsteams in gesicherte Bereiche mitgebracht werden.

**Inspektionsverfahren für Drittpartei-Geräte** (gesicherte Bereiche):

Gerätekategorien, die eine Genehmigung erfordern: Laptops, Tablets, Smartphones (ausser Basistelefon für Notfallgespräche); externe Speichergeräte (USB-Sticks, externe HDDs); Aufnahmegeräte (Kameras, Audiorekorder); Wireless-Geräte (WLAN-Hotspots, Bluetooth-Geräte, IoT-Gadgets); Testgeräte (Oszilloskope, Netzwerkanalysatoren mit Datenprotokollierung).

Inspektionsverfahren (durch Facilities Manager oder Sicherheitsteam):
1. **Sichtprüfung**: Verifizieren, dass das Gerät der Beschreibung im Genehmigungsantrag entspricht
2. **Wireless-Prüfung**: Sicherstellen, dass Wireless-Funktionen, falls erforderlich, deaktiviert sind (Flugmodus, WLAN aus) — visuelle Bestätigung oder Netzwerkscanner
3. **Aufnahmekontrolle**: Verifizieren, dass keine aktive Aufnahme erfolgt (Kameralinse abgedeckt, Audiorekorder aus)
4. **Protokollierung**: Gerätetyp, Seriennummer, Besuchername, Eintrittszeit, Austrittszeit, Genehmigungsreferenz aufzeichnen

**Hochrisikogeräte** (Speichermedien, Laptops): Zusätzlicher Schritt — Sicherstellen, dass keine Verbindung zum Organisationsnetzwerk besteht. Falls verbunden: sofort trennen und als Vorfall protokollieren. Alternative: Die Organisation stellt Leihgeräte für Arbeit bereit, die Computerzugang erfordert (für längere Besuche bevorzugt).

**Nicht autorisierte Geräte**: Zutritt verweigert; am Empfang bis zur Abreise des Besuchers verwahrt. Besucher vor dem Betreten informiert.

**Notfallausnahme**: Notfallwartungsgeräte (Diagnose-Laptop des Lieferanten für dringende Serverreparatur) können vom ISB mit Kompensationskontrollen genehmigt werden (ganzzeitige Begleitung, keine Netzwerkverbindung, Arbeit per Video aufgezeichnet).

### Informationsschutz in gesicherten Bereichen

- Sensible Informationen dürfen nicht besprochen werden, wenn sie von unbefugten Personen gehört werden können.
- Sensible Dokumente müssen sofort nach dem Drucken von Druckern, Kopierern und Faxgeräten abgeholt werden.

**Handhabung von Whiteboards und Flipcharts in gesicherten Bereichen**:

| Klassifizierung | Handhabungsanforderung |
|----------------|----------------------|
| **VERTRAULICH** | Verboten auf Whiteboards/Flipcharts — nur digitale Präsentation verwenden oder gedruckte Materialien danach einsammeln. Falls VERTRAULICHE Informationen versehentlich geschrieben werden: sofort löschen, gelöschtes Whiteboard fotografieren, um kein Ghost-Image zu verifizieren. Falls Ghost-Image bestehen bleibt, wird das Whiteboard ausser Dienst gestellt und ersetzt. Alternative: Einweg-Papier-Flipcharts, nach der Besprechung eingesammelt und in den vertraulichen Abfall gegeben. |
| **INTERN** | Sofort nach der Besprechung löschen. Besprechungsorganisator verifiziert, dass kein Ghost-Image vorhanden ist (Sichtprüfung). Fotografien von Whiteboards werden als INTERN klassifiziert. |
| **ÖFFENTLICH** | Best Practice, zu löschen; keine Verifizierung erforderlich. |

Besprechungsräume in gesicherten Bereichen: periodischer Whiteboard-Austausch (alle 2 Jahre) oder Verwendung von digitalen Whiteboards ohne Datenpersistenz.
- Lieferanten und externes Wartungspersonal müssen auf den minimal notwendigen Bereich beschränkt werden. Unbeaufsichtigter Zugang zu gesicherten Bereichen darf nicht gestattet werden.

### Inventar gesicherter Bereiche

Die Organisation führt ein Register aller designierten gesicherten Bereiche, einschliesslich:

- Standort und physische Grenzen jedes gesicherten Bereichs
- Bezeichneter Eigentümer des gesicherten Bereichs, verantwortlich für Zugangsentscheidungen
- Klassifizierungsstufe der typischerweise verarbeiteten oder gespeicherten Informationen
- Spezifische zusätzliche Regeln für den Bereich (z. B. keine mobilen Geräte, ausschliesslich begleiteter Zugang)

Dieses Register muss jährlich oder bei organisatorischen Änderungen, die Designierungen gesicherter Bereiche betreffen, überprüft werden.

---

## Aufgeräumter Schreibtisch und aufgeräumter Bildschirm (A.7.7)

ISO/IEC 27001:2022 Annex A.7.7 besagt:

> *Regeln zum aufgeräumten Schreibtisch für Papier und Wechselspeichermedien sowie Regeln zum aufgeräumten Bildschirm für Informationsverarbeitungsanlagen sollten definiert und angemessen durchgesetzt werden.*

### Anforderungen für aufgeräumten Schreibtisch

**Während der Arbeitszeit**:

- Sensible Dokumente müssen in gesperrten Schubladen oder Schränken aufbewahrt werden, wenn sie nicht unmittelbar aktiv genutzt werden.
- Auf den Druck wartende Dokumente müssen sofort über die sichere Druckfreigabe abgeholt werden, sofern verfügbar.
- Nur aktiv bearbeitete Dokumente dürfen auf Schreibtischen liegen. Das Ansammeln klassifizierter Dokumente auf Schreibtischen ist nicht gestattet.

**Ende des Tages / Längere Abwesenheit**:

- Alle sensiblen Dokumente müssen in Schubladen, Schränken oder Safes eingeschlossen werden.
- Wechselspeichermedien (USB-Sticks, externe Festplatten, SD-Karten) müssen in gesperrter Aufbewahrung gesichert werden.
- Zugangskarten, Schlüssel und Token dürfen nicht unbeaufsichtigt auf Schreibtischen liegen gelassen werden.
- Notizbücher und Haftnotizen mit Passwörtern, PINs oder sensiblen Informationen müssen gesichert oder vernichtet werden.

**Klassifizierungsspezifische Anforderungen**:

| Klassifizierung | Während der Arbeitszeit | Ende des Tages | Durchsetzung |
|----------------|------------------------|----------------|--------------|
| **VERTRAULICH** | Bei Unbeaufsichtigung gesperrt (auch kurz) | Gesperrte Aufbewahrung obligatorisch | Obligatorisch — Audit-Ergebnisse werden gemeldet |
| **INTERN** | Verdeckt oder umgedreht bei Unbeaufsichtigung | Gesperrte Aufbewahrung am Tagesende | Obligatorisch — in Schreibtisch-Audits inbegriffen |
| **ÖFFENTLICH** | Keine spezifische Einschränkung | Best Practice zum Aufräumen | Empfehlend — Best Practice |

**Physische Medien und Wechselspeicher**:

- Wechselmedien mit klassifizierten Informationen müssen unabhängig von der Klassifizierungsstufe bei Nichtgebrauch eingeschlossen werden.
- Nicht gekennzeichnete Dokumente werden standardmässig als INTERN behandelt.
- Behälter für vertraulichen Abfall müssen an Arbeitsplätzen oder an zugänglichen Standorten für die sofortige Entsorgung sensibler Papierdokumente bereitgestellt werden.

### Anforderungen für aufgeräumten Bildschirm

**Bildschirmsperre**:

Das Bildschirm-Sperr-Timeout muss über [Endgerät-Management-Tool] (Gruppenrichtlinien, MDM oder gleichwertig) mit folgender abgestufter Richtlinie durchgesetzt werden:

| Arbeitsstationstyp | Inaktivitäts-Timeout | Begründung |
|-------------------|---------------------|------------|
| **Standard-Arbeitsstationen** (Büro, Standardbenutzerzugang) | 5 Minuten | Allgemeine Baseline |
| **Privilegierte Arbeitsstationen** (Admin, Datenbank, Security Operations) | 2 Minuten | Erhöhtes Zugriffsrisiko; sofortige manuelle Sperre (Win+L / Ctrl+Cmd+Q) beim Verlassen des Schreibtisches erforderlich |
| **Arbeitsstationen in gesicherten Bereichen** (Serverräume, SOC, Führungsbüros) | 2 Minuten | Keine Ausnahmen |
| **Remote-Arbeitende / Laptops** | 3 Minuten | Balance zwischen Sicherheit und mobiler Nutzbarkeit |
| **Öffentliche / nicht vertrauenswürdige Standorte** (Flughafen, Café) | 1 Minute empfohlen | Nutzerermessen; richtlinienerzwungenes Maximum 3 Minuten |

**Durchsetzung**: Timeout-Einstellungen werden über [Endgerät-Management-Tool] mit vierteljährlicher Compliance-Überwachung eingesetzt. Nicht-konforme Geräte werden innerhalb von 5 Arbeitstagen zur Behebung markiert.

- Nutzer müssen Bildschirme manuell sperren, wenn sie ihren Arbeitsplatz verlassen, auch kurz, über Tastatürkürzel (Win+L auf Windows, Ctrl+Cmd+Q auf macOS).
- Passwortgeschützte Bildschirmschoner oder Sperrbildschirme müssen auf allen Geräten aktiviert sein.
- Multi-Faktor-Authentifizierung oder sichere biometrische Abfragen sollten für die Entsperrung aktiver Sitzungen auf Geräten, die VERTRAULICHE Daten verarbeiten, verwendet werden.

**Datenschutz und Anzeige**:

**Anforderungen und Durchsetzung für Sichtschutzfilter**:

- **Obligatorisch für**: Laptops, die ausserhalb des Büros genutzt werden (vom IT als Teil des Laptop-Kits ausgegeben); Arbeitsstationen in Grossraumbüros, wo regelmässig auf VERTRAULICHE Daten zugegriffen wird (IT gibt Sichtschutzfilter an betroffene Rollen aus); alle, die an öffentlichen Standorten arbeiten (Flughafen, Zug, Café).
- **Verifizierung**: IT nimmt Sichtschutzfilter in die Laptop-Deployment-Checkliste auf (vom Empfänger unterzeichnet). Jährliches Schreibtisch-Audit umfasst Sichtschutzfilter-Präsenzprüfung für Grossraum-Arbeitsstationen mit VERTRAULICHEM Datenzugang (10%-Stichprobe). Remote-Work-Stichprobenprüfung (via Videoanruf, vierteljährlich, 5%-Stichprobe): Sichtschutzfilterverwendung bei Arbeit ausserhalb des Homeoffice verifizieren.
- **Nicht-Compliance**: Erstmaliges Auftreten — Erinnerung + Sichtschutzfilter ausgegeben falls fehlend. Wiederholte Nicht-Compliance — Eskalation an Manager. Weigerung, ausgegebenen Sichtschutzfilter in Rolle mit VERTRAULICHEM Datenzugang zu verwenden — Widerruf des VERTRAULICHEN Datenzugangs oder Verlegung ins geschlossene Büro.
- **Kosten**: Durch die Organisation finanziert für obligatorische Rollen (privilegierter Zugang, VERTRAULICHE Datenhandler). Optional für andere (persönlicher Kauf).

- Sensible Informationen dürfen nicht auf Bildschirmen angezeigt werden, die für unbefugte Personen, einschliesslich Besucher und Vorbeigehen, sichtbar sind.
- Projektor- und Bildschirmfreigabe-Sitzungen müssen sofort nach der Nutzung beendet werden. Präsentierende müssen sensible Anwendungen vor der Bildschirmfreigabe schliessen.
- Bei virtuellen Besprechungen sollten virtuelle Hintergründe verwendet werden, wo die physische Umgebung sensible Informationen offenbaren könnte (z. B. Whiteboards, Dokumente an Wänden).
- E-Mail- und Messaging-Benachrichtigungs-Pop-ups sollten während Präsentationen und Bildschirmfreigabe-Sitzungen deaktiviert oder minimiert werden.

**Ende des Tages**:

- Alle Anwendungen mit sensiblen Daten müssen geschlossen werden.
- Arbeitsstationen müssen gemäss der IT-Richtlinie abgemeldet oder heruntergefahren werden.
- Remote-Desktop- und VPN-Sitzungen müssen getrennt werden.

**Besprechungsräume**:

- Whiteboards und Flipcharts müssen vor dem Verlassen des Raums gelöscht werden.
- Besprechungsräume mit persistenten Anzeigen (z. B. wandmontierte Bildschirme) dürfen nach Besprechungsende keine sensiblen Inhalte mehr anzeigen.

**Handhabung von gedrucktem Material in Besprechungsräumen**:

- **Vor der Besprechung (Organisator)**: Handout-Anzahl protokollieren (Anzahl gedruckter Kopien); Klassifizierungskennzeichnung auf jedem Handout.
- **Ende der Besprechung (Organisator)**: Eingesammelte vs. verteilte Handouts zählen. Übrig gebliebene Kopien einsammeln und entweder vom Organisator behalten (falls wiederverwendbar) oder in den vertraulichen Abfall gegeben (falls besprechungsspezifisch).
- **Verantwortung der Teilnehmenden**: VERTRAULICHE Handouts an Organisator zurückgeben oder in den vertraulichen Abfall (nicht mitnehmen, sofern nicht autorisiert). INTERNE Handouts können behalten werden, falls für die Arbeit benötigt; sonst zurückgeben oder vertraulicher Abfall.
- **Besprechungsraum-Nachkontrolle** (täglich, Einrichtungen/Reinigungspersonal): Sichtprüfung auf zurückgelassene Dokumente. Gefundene Dokumente werden an [designierten sicheren Sammelplatz] zur Überprüfung durch ISB oder Facilities Manager gebracht. Wiederholte Befunde (gleicher Besprechungsraum, gleicher Organisator) werden an den Manager des Organisators eskaliert.
- **Alternative**: Nur-Digital-Besprechungen für VERTRAULICHE Themen (keine gedruckten Handouts). Präsentation über sicheres Portal geteilt, keine Downloads.

### Durchsetzung und Auditierung

Audits für aufgeräumten Schreibtisch und aufgeräumten Bildschirm müssen **monatlich** (mindestens 1, maximal 2 pro Monat) vom Facilities Manager oder designierten Prüfer durchgeführt werden.

**Randomisierung**:
- Audit-Datum wird zufällig innerhalb des Monats gewählt (1.–28., monatlich variierend). Audit-Zeit wird zufällig innerhalb der Geschäftszeiten gewählt (08:00–18:00, variierend). Keine Vorankündigung — Mitarbeitende werden nur beim Onboarding über die allgemeine monatliche Audit-Anforderung informiert.
- Audit-Standorte: 20% der Schreibtische pro Audit stichprobenartig (monatlich verschiedene Schreibtische; vollständige Abdeckung über 5 Monate).

**Auditverfahren**:
- Prüfer verwendet standardisierte Checkliste (Ja/Nein-Fragen, keine subjektive Bewertung).
- Fotografische Nachweise für nicht-konforme Schreibtische (sensible Inhalte unkenntlich machen, falls sichtbar).
- Zweiter Prüfer überprüft 10% der geprüften Schreibtische stichprobenartig (Qualitätssicherung).

**Abdeckungsziel**: Alle Mitarbeitenden mindestens zweimal pro Jahr geprüft. Hochrisikorollen (VERTRAULICHER Datenzugang): vierteljährlich geprüft.

**Ergebnisse und Eskalation**:
- Nicht-Compliance wird innerhalb von 2 Arbeitstagen an direkte Vorgesetzte gemeldet.
- Wiederholte Nicht-Compliance (drei oder mehr Befunde in einem 6-Monats-Zeitraum) wird an HR für formelle Massnahmen eskaliert.
- Aggregierte Ergebnisse (keine Einzelnamen) werden dem Management Review vierteljährlich gemeldet.
- Audit-Ergebnisse werden als Teil des ISMS-Management-Reviews berichtet.

---

## Sichere Entsorgung oder Wiederverwendung von Geräten (A.7.14)

ISO/IEC 27001:2022 Annex A.7.14 besagt:

> *Geräte mit Speichermedien sollten verifiziert werden, um sicherzustellen, dass sensible Daten und lizenzierte Software vor der Entsorgung oder Wiederverwendung entfernt oder sicher überschrieben wurden.*

### Vorentsorgungsbewertung

Bevor Geräte entsorgt oder wiederverwendet werden, muss folgende Bewertung abgeschlossen werden:

1. **Datenklassifizierungsüberprüfung** — Maximale Datenklassifizierung bestimmen, die jemals auf dem Gerät gespeichert war (nicht nur aktueller Inhalt). Dies bestimmt die erforderliche Entsorgungsmethode.
2. **Lizenzierter Software-Audit** — Lizenzierte Software gemäss Lizenzbedingungen identifizieren und dekommissionieren. Lizenzschlüssel müssen, wo anwendbar, wiederhergestellt oder übertragen werden.
3. **Asset-Record-Aktualisierung** — [Asset-Management-System] aktualisieren, um die geplante Entsorgung oder Neuzuweisung widerzuspiegeln, einschliesslich Entsorgungsgrund und vorgeschlagener Methode.
4. **Personendaten-Prüfung** — Wenn das Gerät Personendaten enthalten haben könnte, muss die Entsorgung den Anforderungen des nDSG Art. 8 zur nicht wiederherstellbaren Datenlöschung entsprechen.

### Sanitisierungsstufen (NIST SP 800-88 Rev. 2)

Die Organisation übernimmt das NIST SP 800-88 Rev. 2-Rahmenwerk für die Mediensanierung, abgestimmt mit den technischen Empfehlungen von IEEE 2883:2022:

| Sanitisierungsstufe | Methode | Beschreibung | Anwendungsfall |
|--------------------|---------|-------------|---------------|
| **Clear (Löschen)** | Logisches Überschreiben | Überschreibt benutzerzugängliche Speicherorte mit nicht-sensiblen Daten über Standard-Lese-/Schreibbefehle. Schützt vor einfacher nicht-invasiver Datenwiederherstellung. | ÖFFENTLICHE Daten; interne Wiederverwendung von Geräten mit geringer Sensibilität |
| **Purge (Bereinigen)** | Kryptografisches Löschen, Block-Erase oder Firmware-Befehle | Macht die Datenwiederherstellung mit modernsten Labortechniken infeasibel. Umfasst kryptografisches Löschen (Verschlüsselungsschlüssel auf selbstverschlüsselnden Festplatten zerstören) und Secure-Erase-Befehle des Herstellers gemäss IEEE 2883. | INTERNE Daten; interne Wiederverwendung; externe Übertragung |
| **Destroy (Vernichten)** | Physische Zerstörung | Macht das Medium physisch unbrauchbar durch Schreddern, Zerlegung, Pulverisierung oder Verbrennung. Die Datenwiederherstellung ist unabhängig vom Aufwand nicht möglich. | VERTRAULICHE Daten; alle externen Entsorgungen sensibler Medien |

### Entsorgungsmethoden nach Gerätetyp und Klassifizierung

| Gerätetyp | VERTRAULICH | INTERN | ÖFFENTLICH |
|-----------|-------------|--------|------------|
| **Festplatten (HDD)** | Physische Zerstörung (Schreddern zu < 2 mm Partikeln oder Degaussing + Schreddern); Vernichtungszertifikat mit Seriennummer erforderlich | Bereinigung: Herstellersicheres Löschen (ATA Secure Erase) gemäss IEEE 2883 ODER Einzelpass-Überschreiben mit Verifizierung über [Secure-Wipe-Tool]; physische Zerstörung ebenfalls akzeptabel | Löschen: Schnellformat und Betriebssystem-Neuinstallation |
| **Solid-State-Drives (SSD)** | Physische Zerstörung (Schreddern/Zerlegung zu < 2 mm Partikeln) | Kryptografisches Löschen (selbstverschlüsselnde Laufwerke mit verifizierter Verschlüsselung) oder Herstellersicheres Löschen gemäss IEEE 2883; physische Zerstörung falls Krypto-Löschen nicht verfügbar oder nicht verifizierbar | Sicherer Löschbefehl |
| **Mobile Geräte** | Physische Zerstörung ODER falls nicht machbar (Leasinggerät): Werksreset + Remote-Wipe + MDM-Abmeldung + ISB-Risikoakzeptanz | Werksreset über MDM (Remote-Wipe) + Gerätewipe über UI (Doppelwipe) + MDM-Abmeldung; Verschlüsselung muss ab Deployment aktiviert gewesen sein (über Asset-Record verifiziert) | Werksreset über Geräte-UI |
| **USB / Wechselmedien** | Physische Zerstörung (Schreddern) | Sicheres Überschreiben oder physische Zerstörung | Formatieren |
| **Drucker / Kopierer** | Interne HDD/SSD-Entfernung + Zerstörung | Interne HDD/SSD-Entfernung + sicheres Wipe | Speicher löschen / Werksreset |
| **Netzwerkgeräte** | Konfig-Wipe + Zerstörung bei vorhandenem Flash-Speicher | Konfig-Wipe + Verifizierung + Werksreset | Konfig-Reset |
| **Virtuelle / Cloud-Speicher** | Client-seitiges Löschen des Verschlüsselungsschlüssels (von Organisation verwaltete Schlüssel) + Cloud-Volume-Löschung + Löschbestätigungsprotokoll | Kryptografisches Löschen (Volume löschen + KMS-Schlüssel löschen) + Löschbestätigungs-Screenshot/-protokoll | Standard-Löschung über Anbieter |

**Begründung für HDD-Entsorgung**: NIST SP 800-88 Rev. 2 (2023) bestätigt, dass ein einziger Überschreibungspass für moderne HDDs (nach 2001 hergestellt) ausreicht; Mehrfach-Überschreiben (z. B. „3-Pass") ist eine ältere Anforderung aus DoD-Standards und ist nicht mehr notwendig. Für INTERNE Klassifizierung sind Purge-Level-Methoden erforderlich — einfache Clear-Level-Methoden sind unzureichend.

**SSD und Flash-Medien — Verifizierung des kryptografischen Löschens**: Traditionelle Überschreibungsmethoden sind für SSDs aufgrund von Wear-Levelling, Over-Provisioning und Write Amplification nicht zuverlässig. Kryptografisches Löschen auf selbstverschlüsselnden Laufwerken (SEDs) ist nur wirksam, wenn: (a) das Laufwerk während seines gesamten Lebenszyklus mit aktivierter Verschlüsselung konfiguriert war (über Asset-Record verifiziert) und (b) der Löschbefehl verifiziert ist. Folgendes Verifizierungsverfahren muss angewendet werden:

1. Bestätigen, dass das Laufwerk ein selbstverschlüsselndes Laufwerk ist (Herstellerdokumentation prüfen, nicht annehmen)
2. Verifizieren, dass die Verschlüsselung während des gesamten Lebenszyklus aktiviert war (Asset-Record)
3. Kryptografischen Löschbefehl über Herstellertool oder ATA Security Erase ausgeben
4. Befehlsabschluss verifizieren (Tool meldet Erfolg)
5. **Verifizierungsschritt**: Datenwiederherstellung mit forensischem Tool an Stichprobe gelöschter Laufwerke versuchen (mindestens 10% pro Charge oder alle Laufwerke bei < 10 Laufwerken). Falls lesbare Daten gefunden → zur physischen Zerstörung eskalieren. Falls keine lesbaren Daten → für Wiederverwendung/Entsorgung freigeben.
6. **Risikoakzeptanz**: Falls Verifizierungs-Forensik nicht machbar ist (Ressourcen-/Zeitbeschränkung): Standard ist physische Zerstörung für INTERNE/VERTRAULICHE SSDs.

**Entsorgung mobiler Geräte — Verschlüsselungsvoraussetzung**: Geräteverschlüsselung muss ab dem Deployment-Tag für alle mobilen Geräte, die INTERNE oder VERTRAULICHE Daten verarbeiten, obligatorisch sein (über [MDM]-Richtlinie durchgesetzt, im Geräteregistrierungsnachweis dokumentiert). Wenn ein Gerät ohne Verschlüsselung eingesetzt wurde (Legacy, nicht-konform): standardmässig physische Zerstörung unabhängig von der Datenklassifizierung, und Root-Cause-Analyse für MDM-Richtlinien-Behebung durchführen.

**Virtuelle und Cloud-Speicher**: Grosse Cloud-Anbieter (AWS, Azure, GCP) stellen keine individuellen Vernichtungszertifikate für virtuellen Speicher aus. Die Organisation verlässt sich auf SOC 2 Type II / ISO 27001-Zertifizierungen des Anbieters und Datenlöschungs-Attestierungen. Risikoakzeptanz für die Vertrauenswürdigkeit der Anbieterlöschprozesse muss jährlich im Management Review dokumentiert werden. Für hochsensible Daten: Verschlüsselung auf Client-Seite vor dem Hochladen (Organisation kontrolliert Schlüssel in On-Premises-HSM oder separatem KMS); bei der Entsorgung von der Organisation verwaltete Schlüssel löschen, dann Cloud-Daten löschen; Schlüssellöschung mit HSM/KMS-Auditprotokoll dokumentieren.

**IoT und eingebettete Geräte**: Geräte mit eingebettetem Speicher, die nicht mit Standard-Tools sanitisiert werden können (z. B. IoT-Sensoren, Gebäudemanagement-Controller, medizinische Geräte), müssen physisch zerstört werden, wenn sie VERTRAULICHE oder INTERNE Daten gespeichert haben. Falls physische Zerstörung nicht möglich ist, muss die Organisation Herstelleranleitungen zur Sanitisierung einholen und die Methode sowie etwaige Restrisiken dokumentieren.

#### Inventar für IoT und eingebettete Geräte

Als Voraussetzung für die Entsorgung führt die Organisation ein Inventar der IoT- und eingebetteten Geräte mit Speicher:

**In-Scope-Geräte**: Gebäudemanagementsysteme (HVAC-Controller, Beleuchtung), physische Sicherheitsgeräte (IP-Kameras, Zugangskontroller, Alarmtableaus), Netzwerkgeräte mit eingebettetem Speicher (Switches, Router, Firewalls), intelligente Bürogeräte (Drucker mit HDDs, Smart Displays, IoT-Sensoren) und Spezialgeräte (medizinische Geräte, Laborgeräte, industrielle Controller).

**Inventaranforderungen** — alle In-Scope-Geräte im [Asset-Management-System] erfasst mit: Gerätetyp, Hersteller, Modell, Seriennummer; Speichertyp und -kapazität (falls bekannt); Datenklassifizierung der verarbeiteten/gespeicherten Informationen; Entsorgungsmethode (Sanitisierungsverfahren oder physische Zerstörung); Entsorgungskontakt (Lieferant, Hersteller, internes Team).

Inventar wird von Einrichtungen + IT-Betrieb geführt, jährlich überprüft. Unbekannte Geräte, die bei Einrichtungsänderungen gefunden werden, werden an ISB zur Bewertung eskaliert; Standard-Annahme: Kann VERTRAULICHE Daten enthalten → physische Zerstörung.

### Wiederverwendungsverfahren

**Interne Wiederverwendung**:

- Alle Daten müssen mit einer genehmigten Methode, die der vorherigen Datenklassifizierung entspricht, sicher gelöscht werden, bevor das Gerät neu zugewiesen wird.
- Lizenzierte Software muss gemäss Lizenzbedingungen übertragen oder entfernt werden.
- [Asset-Management-System] muss mit dem neuen Benutzer, Datum und Sanitisierungsnachweis aktualisiert werden.
- Geräte müssen vor der Neuinbetriebnahme inspiziert und bei Bedarf aufgearbeitet werden.

**Externe Wiederverwendung (Spende oder Verkauf)**:

- Geräte, die VERTRAULICHE Daten gespeichert haben, dürfen nicht extern wiederverwendet werden. Speichermedien müssen physisch zerstört werden.
- Geräte, die INTERNE Daten gespeichert haben, müssen Speichermedien, die auf Purge-Level sanitisiert oder zerstört wurden, vor der externen Übertragung aufweisen.
- Alle Organisationsidentifikatoren (Asset-Tags, Aufkleber, Gravierungen) müssen entfernt werden.
- Werkseinstellungen müssen wiederhergestellt werden.
- Eine Aufzeichnung der externen Übertragung muss geführt werden, einschliesslich Empfänger, Datum und Sanitisierungsnachweis.

### Beweiskette

**Interne Aufbewahrung**:

- Geräte, die auf Sanitisierung oder Zerstörung warten, müssen in einem designierten sicheren Aufbewahrungsbereich aufbewahrt werden, mit Zugang, der auf autorisiertes Entsorgungspersonal beschränkt ist.

**Anforderungen an die Sicherheit des Aufbewahrungsbereichs**:

- **Standort**: Dedizierter gesperrter Raum oder Käfig im IT-Betriebsbereich (nicht mit allgemeiner Lagerung geteilt).
- **Physische Sicherheit (Minimum für alle Klassifizierungen)**: Abschliessbare Tür mit Schlüsselkontrolle (Schlüssel werden nur an autorisiertes Personal ausgegeben — IT-Betriebsleiter, Senior-Techniker, ISB). Zugriffsprotokoll geführt (manuelles An-/Abmelden oder elektronischer Badge-Leser). Bereich bei Unbeaufsichtigung gesperrt.
- **Zusätzliche Sicherheit für VERTRAULICHE Geräte**: Aufbewahrungsbereich innerhalb eines alarmierten gesicherten Bereichs (Serverraum oder Rechenzentrum). 24/7-Kameraüberwachung (Aufzeichnung 30 Tage aufbewahrt). Zwei-Personen-Zugriffsregel (kein Einzelpersonen-Zugang zu VERTRAULICHEN Geräten).
- **Trennung**: VERTRAULICHE Geräte separat von Geräten mit niedrigerer Klassifizierung gelagert (separates Regal, separater Käfig oder klar gekennzeichnete Zone). Geräte in gesperrten antistatischen Taschen oder gesperrten Schränken im Aufbewahrungsbereich (zusätzliche Schicht).
- **Maximale Aufbewahrungszeit**: ÖFFENTLICH/INTERN — 30 Tage. VERTRAULICH — 10 Arbeitstage (beschleunigte Entsorgung erforderlich). Geräte, die die maximale Aufbewahrungszeit überschreiten, werden zur Root-Cause-Untersuchung an ISB eskaliert.
- **Inventar**: Wöchentlich abgeglichen. Aufbewahrungsbereich monatlich durch ISB oder Beauftragte inspiziert.

**Externe Vernichtung**:

Wenn Geräte die Betriebsstätten der Organisation zur Vernichtung durch einen genehmigten Lieferanten verlassen, muss die Beweisketten-Dokumentation enthalten:

- Übergabedatum und -uhrzeit
- Asset-Identifikatoren (Seriennummern, Asset-Tags)
- Anzahl und Art der Gegenstände
- Identität der freigebenden Partei (Organisationsvertreter)
- Identität der empfangenden Partei (Lieferantenvertreter)
- Lieferanten-Transport-Referenz oder Tracking-Nummer
- Voraussichtliches Vernichtungsdatum

Vernichtungszertifikate müssen vom Lieferanten eingeholt werden und individuelle Seriennummern für jeden vernichteten Gegenstand enthalten. Zertifikate müssen mit dem Übergabeprotokoll abgeglichen werden. Diskrepanzen müssen sofort eskaliert und als Sicherheitsereignis protokolliert werden.

**Reaktion auf Diskrepanzen bei Vernichtungszertifikaten**:

Diskrepanztypen: Fehlende Gegenstände (weniger Seriennummern auf Zertifikat als auf Übergabeprotokoll); zusätzliche Gegenstände (Seriennummern nicht auf Übergabeprotokoll); nicht übereinstimmende Gegenstände (Seriennummer entspricht keinem Übergabegegenstand).

| Schritt | Massnahme | Zeitrahmen |
|---------|-----------|------------|
| 1 | IT-Betrieb kontaktiert [Vernichtungslieferant] über Account-Manager (Telefon + E-Mail) | Innerhalb von 24 Stunden nach Diskrepanzentdeckung |
| 2 | Lieferant gibt Klärung (Gegenstand noch im Transit, Zertifikatsfehler usw.) | Innerhalb von 48 Stunden |
| 3 | Falls Lieferant bestätigt, dass Gegenstand nicht vernichtet wurde: Sofortige Eskalation an ISB (potenzielle Datenverletzung — Gerät mit klassifizierten Daten nicht nachweisbar) | Sofort |
| 4 | Lieferant muss Gegenstand innerhalb von 5 Arbeitstagen lokalisieren oder eidesstattliche Erklärung liefern, dass er vernichtet wurde (Zertifikatsfehler) | 5 Arbeitstage |
| 5 | Falls Lieferant nicht lokalisieren oder Vernichtung bestätigen kann: Gerät als verloren/gestohlen annehmen (Worst Case). ISB + Datenschutzberater bestimmen, ob Personendaten auf dem Gerät waren. Regulatorische Meldung falls erforderlich (nDSG Art. 24, DSGVO Art. 33 wo anwendbar). | Sofort nach Feststellung |

**Lieferantenkonsequenzen**: Ungelöste Diskrepanz löst Entfernung des Lieferanten von der genehmigten Lieferantenliste bis zum Untersuchungsergebnis aus. Alle Diskrepanzen im Vernichtungs-Diskrepanzprotokoll dokumentiert, vierteljährlich an Geschäftsleitung gemeldet (auch wenn gelöst).

### Dokumentationsanforderungen

**Entsorgungsnachweise** müssen enthalten:

- Asset-Tag und Seriennummer des Geräts
- Datenklassifizierungsstufe (maximal je gespeichert)
- Sanitisierungsmethode und -tool (z. B. [Secure-Wipe-Tool], physisches Schredder-Modell)
- Datum der Sanitisierung oder Vernichtung
- Operator, der die Sanitisierung durchgeführt hat (Name, Mitarbeitenden-ID)
- **Authentifizierung**: Digitale Unterschrift des Operators oder angemeldeter Benutzername aus [Secure-Wipe-Tool] (automatische Erfassung). Für VERTRAULICHE Werte: Zweipersonenverifizierung (Zeuge Name, Unterschrift, Datum).
- Abschlussstatus und Verifizierungsergebnis
- Person, die die Entsorgung autorisiert
- Vernichtungszertifikat (wo anwendbar, für externe Lieferanten)
- Für VERTRAULICHE Werte: Zweipersonenverifizierung des Wipe/der Vernichtung

**Aufbewahrung**: Entsorgungsnachweise, einschliesslich Vernichtungszertifikate, müssen **7 Jahre** aufbewahrt werden.

### Vernichtungszertifikate

Für alle Geräte, die von externem [Vernichtungslieferant] oder Spezialisten vernichtet werden:

- Ein Vernichtungszertifikat muss für jede Charge oder jeden einzelnen vernichteten Gegenstand eingeholt werden.
- Zertifikate müssen individuelle Seriennummern, nicht nur Chargenidentifikatoren, referenzieren.
- Die Vernichtungsmethode muss auf dem Zertifikat angegeben sein (z. B. Schreddern auf Partikelgrösse, Verbrennung).
- Papierdokumente mit VERTRAULICHEN oder INTERNEN Informationen müssen auf mindestens DIN 66399 Sicherheitsstufe P-4 (oder gleichwertigem Kreuzschnitt-Standard) geschreddert werden.
- Zertifikate müssen mit dem entsprechenden Entsorgungsnachweis abgelegt und 7 Jahre aufbewahrt werden.

### Anforderungen an genehmigte Lieferanten

Die Organisation darf nur Vernichtungslieferanten nutzen, die:

- Relevante Zertifizierungen halten (z. B. ISO 14001 für Umweltmanagement, EN 15713 für Sicherheitsvernichtungsdienste oder gleichwertig).
- Dokumentierte Sanitisierungs- oder Vernichtungsverfahren gemäss NIST SP 800-88 Rev. 2 oder DIN 66399 bereitstellen.
- Individuelle Vernichtungszertifikate mit Seriennummer-Rückverfolgbarkeit ausstellen.
- Regelmässiger Due-Diligence-Überprüfung unterliegen (mindestens jährlich).
- Angemessene Versicherung für Verlust oder Datenverletzung während Transport und Vernichtung unterhalten.

Wo Vor-Ort-Vernichtung verfügbar ist, sollte sie für VERTRAULICHE Medien gegenüber externer Vernichtung bevorzugt werden, um das Beweisketten-Risiko zu minimieren.

---

## SOC 2-Überlegungen

### Nachverfolgung der Kundendatenentsorgung (CC6.5)

Systeme und Geräte, die Kundendaten verarbeitet haben (CRM, Anwendungsserver, Datenbanken, Kundensupport-Laptops), müssen im [Asset-Management-System] beim Deployment mit einem „Kundendaten"-Attribut gekennzeichnet werden. Bei der Entsorgung:

- Der Entsorgungsnachweis muss die Kundendaten-Kennzeichnung referenzieren.
- ISB überprüft vierteljährlich 10% der kundendatengekennzeichneten Entsorgungen stichprobenartig (Wipe-Abschluss verifizieren, Zertifikat eingeholt).
- Prüfpfad: Entsorgungsprotokoll nach „Kundendaten"-Kennzeichnung filterbar für SOC 2-Audit-Stichproben.

### Nachverfolgung der Wechselmedienentsorgung (CC6.7)

**Von der Organisation ausgegebene Wechselmedien** (USB-Sticks, externe HDDs, vom IT ausgegeben): Seriennummern bei Ausgabe im [Asset-Management-System] erfasst. Mitarbeitende unterzeichnen Asset-Bestätigung (verantwortlich für Rückgabe oder sichere Entsorgung nach Verwendung). Bei Mitarbeitendenbeendigung: Rückgabe der Wechselmedien verifiziert (Checklisten-Element im Offboarding-Prozess).

**Persönliche Wechselmedien für die Arbeit (BYOD-USB)**: Generell verboten für VERTRAULICHE/INTERNE Daten (gemäss Richtlinie zur akzeptablen Nutzung). Falls Ausnahme genehmigt: Nutzer verantwortlich für sichere Entsorgung nach Verwendung; Organisation stellt Anleitungen zur sicheren Entsorgung und Zugang zu Vor-Ort-Schredder bereit.

**Verlorene Wechselmedien**: Sofort gemeldet (über Incident-Management). Falls verschlüsselt — geringes Risiko (Verschlüsselungsstatus im Vorfallbericht dokumentieren). Falls unverschlüsselt — Datenverletzungsbewertung erforderlich.

### Personalsicherheit für Entsorgungsoperationen (CC6.1)

Rollen mit Entsorgungsverantwortung (IT-Betrieb, Einrichtungspersonal autorisiert für Aufbewahrungsbereichszugang) unterliegen einer Hintergrundüberprüfung gemäss A.6.1-Anforderungen (mindestens Standard-Screening). Zusätzliche Anforderung für VERTRAULICHE Geräteentsorgung: Erweitertes Screening-Niveau (siehe A.6.1-Screening-Niveautabelle). In der Rollen-zu-Screening-Niveau-Zuordnung dokumentiert (von HR + ISB geführt).

---

## Optional: Zahlungskartendaten-Controls (PCI DSS)

*Nur anwendbar, wenn Zahlungskartendaten verarbeitet werden und PCI-Geltungsbereich besteht.*

Falls PCI-Geltungsbereich besteht, gelten folgende zusätzliche Anforderungen:

- Medien mit Karteninhaberdaten müssen physisch zerstört werden, wenn sie nicht mehr für geschäftliche oder rechtliche Zwecke benötigt werden (PCI DSS Anforderung 9.4).
- Ein Inventar der Medien mit Karteninhaberdaten muss geführt und mindestens jährlich abgeglichen werden.
- Die sichere Entsorgung von Karteninhaberdaten-Medien muss mit Vernichtungszertifikaten dokumentiert werden, die gemäss PCI DSS Anforderung 9.4.7 aufbewahrt werden.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeit |
|-------|-------------------|
| **Geschäftsleitung** | Genehmigt die Richtlinie; stellt Ressourcen für gesicherten Bereichsbetrieb, Entsorgungsinfrastruktur und Lieferantenverträge bereit |
| **ISB** | Richtlinieneigentümerschaft; definiert Sanitisierungsstandards; überwacht die Compliance; genehmigt Entsorgungsausnahmen |
| **Facilities Manager** | Verwaltung gesicherter Bereiche; monatliche Audits für aufgeräumten Schreibtisch; Verwaltung des sicheren Aufbewahrungsbereichs; Koordination des Lieferantenzugangs |
| **IT-Betrieb** | Führt Gerätesanitisierung durch; verifiziert Wipe-Abschluss; führt Entsorgungsnachweise und Wipe-Protokolle; verwaltet [Secure-Wipe-Tool] |
| **Direkte Vorgesetzte** | Stellt Team-Compliance für aufgeräumten Schreibtisch/-bildschirm sicher; genehmigt Geräteentsorgung für ihre Teams; adressiert Audit-Ergebnisse |
| **Beschaffung / Lieferantenmanagement** | Verwaltet [Vernichtungslieferant]-Verträge; verifiziert Lieferantenzertifizierungen; holt Vernichtungszertifikate ein |
| **Alle Mitarbeitenden** | Halten Verhaltensregeln für gesicherte Bereiche ein; halten aufgeräumten Schreibtisch und aufgeräumten Bildschirm; melden verlorene oder unsachgemäss entsorgte Geräte |
| **HR** | Setzt Disziplinarmassnahmen bei wiederholter Nicht-Compliance durch; koordiniert Anforderungen für aufgeräumten Schreibtisch beim Mitarbeitendenausscheiden |

**Eskalationspfad**:

- Verstösse gegen aufgeräumten Schreibtisch: Prüfer --> Direkter Vorgesetzter --> HR (bei wiederholten Verstössen)
- Fragen zur Geräteentsorgung: IT-Betrieb --> ISB
- Vorfälle in gesicherten Bereichen: Sicherheit / Einrichtungen --> ISB --> Geschäftsleitung
- Fehlende Vernichtungszertifikate: IT-Betrieb --> Beschaffung --> ISB

---

## Nachweise für diese Richtlinie

| # | Nachweis | Eigentümer | Häufigkeit | Aufbewahrung |
|---|---------|------------|------------|-------------|
| 1 | Checklisten für aufgeräumten Schreibtisch und aufgeräumten Bildschirm | Facilities Manager | Monatlich | 12 Monate |
| 2 | Zugangsprotokolle für gesicherte Bereiche und Besucherbegleitungsaufzeichnungen | Facilities Manager | Fortlaufend | 12 Monate |
| 3 | Bildschirmsperre-Compliance-Berichte (Endgerät-Management) | IT-Betrieb | Vierteljährlich | 12 Monate |
| 4 | Geräteentsorgungsnachweise (Asset-Tag, Klassifizierung, Methode, Datum, Operator) | IT-Betrieb | Pro Entsorgungsereignis | 7 Jahre |
| 5 | Vernichtungszertifikate vom [Vernichtungslieferant] | Beschaffung | Pro Vernichtungsereignis | 7 Jahre |
| 6 | Sichere Wipe-Verifizierungsprotokolle (Tool-Ausgabe pro Asset) | IT-Betrieb | Pro Wipe-Ereignis | 7 Jahre |
| 7 | Beweisketten-Übergabeprotokolle für externe Vernichtung | IT-Betrieb | Pro Transfer-Ereignis | 7 Jahre |
| 8 | Entsorgungsstatus-Einträge im [Asset-Management-System] | IT-Betrieb | Pro Entsorgungsereignis | Lebensdauer des Asset-Records |
| 9 | Vorfallberichte in gesicherten Bereichen (unbefugter Zugang, Aufnahmen, Alleinarbeit) | ISB | Pro Ereignis | 3 Jahre |
| 10 | Nicht-Compliance-Eskalationsaufzeichnungen für aufgeräumten Schreibtisch | Facilities Manager / HR | Pro Vorfall | 12 Monate |
| 11 | Lieferanten-Due-Diligence-Aufzeichnungen für Vernichtungsdienstleister | Beschaffung | Jährliche Überprüfung | Vertragsdauer + 2 Jahre |
| 12 | Richtlinienbestätigungsaufzeichnungen (Verhalten in gesicherten Bereichen, aufgeräumter Schreibtisch) | HR | Jährlich | Beschäftigungsdauer + 1 Jahr |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Management-Team überprüft die Compliance mit dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf:

- Monatliche Audits für aufgeräumten Schreibtisch und aufgeräumten Bildschirm mit dokumentierten Ergebnissen.
- Vierteljährliche Bildschirmsperre-Timeout-Compliance-Prüfungen über Endgerät-Management-Berichte.
- Halbjährliche Überprüfung der Geräteentsorgungsnachweise gegen das Asset-Register zur Identifizierung nicht erfasster Entsorgungen.
- Jährliche Überprüfung der [Vernichtungslieferant]-Verträge, Zertifizierungen und Vollständigkeit der Vernichtungszertifikate.
- Interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

**Governance-Kennzahlen**:

| Kennzahl | Ziel |
|----------|------|
| Bestehensquote Audit aufgeräumter Schreibtisch | > 95% |
| Bildschirmsperre-Timeout-Compliance | 100% |
| Entsorgung mit Zertifikat (VERTRAULICH) | 100% |
| Sichere Wipe-Verifizierung abgeschlossen | 100% |
| Seriennummer-Übereinstimmungsrate Vernichtungszertifikat | 100% |
| Vorfälle in gesicherten Bereichen (unbefugter Zugang, Aufnahmen) | 0 |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vorab vom ISB genehmigt und dokumentiert werden, mit dokumentierter Risikoakzeptanz, Kompensationskontrollen und einem definierten Überprüfungsdatum von maximal 6 Monaten. Ausnahmen sind dem Management-Review-Team zu melden.

Zulässige Ausnahmen umfassen:

- Verlängertes Bildschirmsperre-Timeout für spezifische betriebliche Anforderungen (z. B. Überwachungs-Dashboards), mit verbesserter physischer Zugangskontrolle.
- Alternative Entsorgungsmethoden für Legacy-Geräte, bei denen Standard-Tools inkompatibel sind, mit dokumentierter Risikoakzeptanz.
- Vorübergehende Lockerung der Anforderungen für aufgeräumten Schreibtisch für Projekt-War-Rooms, mit verbesserter Zugangskontrolle und zeitlich begrenzter Genehmigung.

Ausnahmen dürfen nicht erteilt werden für:

- Eliminierung der Entsorgungsverifizierung für Geräte, die VERTRAULICHE Daten gespeichert haben.
- Permanente Umgehung der Bildschirmsperre-Anforderungen.
- Geräteentsorgung ohne dokumentierte Genehmigung.

## Nicht-Compliance

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen bis hin zur Kündigung des Arbeitsverhältnisses unterliegen.

Die unsachgemässe Entsorgung von Geräten mit Personendaten kann zusätzlich einen Verstoss gegen das schweizerische nDSG darstellen und potenziell zu einer regulatorischen Untersuchung durch den Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB) und, wo anwendbar, EU-Datenschutzbehörden führen.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen der Sanitisierungsstandards (einschliesslich NIST SP 800-88-Updates und IEEE 2883-Revisionen), neue Speichertechnologien (z. B. NVMe, persistenter Speicher), regulatorische Änderungen, Audit-Ergebnisse und Entsorgungsvorfälle.

---

# Abgedeckte Bereiche des ISO 27001-Standards

Richtlinie zu gesicherten Bereichen und Medienhandhabung — ISO 27001-Control-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Politik | 5.4 Managementverantwortlichkeiten |
| Klausel 6.1 Massnahmen zum Umgang mit Risiken | 5.36 Compliance mit Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 6.3 Informationssicherheitsbewusstsein, -schulung und -ausbildung |
| Klausel 7.5 Dokumentierte Informationen | 6.4 Disziplinarverfahren |
| Klausel 8.1 Betriebsplanung und -steuerung | **7.6 Arbeiten in gesicherten Bereichen** |
| Klausel 10.2 Nichtkonformität und Korrekturmassnahmen | **7.7 Aufgeräumter Schreibtisch und aufgeräumter Bildschirm** |
| | **7.14 Sichere Entsorgung oder Wiederverwendung von Geräten** |

# Regulatorischer Rahmen

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen; Personendaten auf Geräten vor der Entsorgung nicht wiederherstellbar machen |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit einschliesslich physischen Schutzes |
| EU DSGVO (soweit anwendbar) | Art. 5(1)(f) — Integrität und Vertraulichkeit; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex A Controls 7.6, 7.7, 7.14 |
| ISO/IEC 27002:2022 | Abschnitte 7.6, 7.7, 7.14 — Implementierungshinweise |
| NIST SP 800-88 Rev. 2 | Leitlinien zur Mediensanierung (Clear, Purge, Destroy) |
| IEEE 2883:2022 | Standard zur Sanitisierung von Speichermedien — technische Methoden für Laufwerke |
| DIN 66399 | Vernichtung von Datenträgern — Sicherheitsstufen für physisches Schreddern |

---

<!-- QA_VERIFIED: 2026-03-29 -->
