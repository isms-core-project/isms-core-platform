<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.6.7-8-DE:operational:OP-POL:a.6.7-8 -->
**ISMS-OP-POL-A.6.7-8 — Remote-Arbeit und Sicherheitsereignismeldung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Remote-Arbeit und Sicherheitsereignismeldung |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.6.7-8 |
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

- ISO/IEC 27001:2022 Control A.6.7 — Remote working
- ISO/IEC 27001:2022 Control A.6.8 — Information security event reporting
- ISO/IEC 27002:2022 Abschnitte 6.7, 6.8 — Implementierungshinweise

**Verwandte Annex-A-Controls**:

| Control | Bezug zu Remote-Arbeit und Ereignismeldung |
|---------|---------------------------------------------|
| A.5.10 Akzeptable Nutzung von Informationen und anderen verbundenen Werten | Definiert die akzeptable Nutzung von Geräten und Informationen im Kontext der Remote-Arbeit |
| A.5.11 Rückgabe von Werten | Rückgabe von Ausrüstung bei Beendigung der Remote-Arbeit oder des Arbeitsverhältnisses |
| A.5.14 Informationsübertragung | Anforderungen an die sichere Übertragung von Daten aus entfernten Standorten |
| A.5.24-28 Lifecycle des Incident-Managements | Eskalationspfad, wenn gemeldete Ereignisse als Vorfälle bestätigt werden |
| A.6.3 Informationssicherheitsbewusstsein, -schulung und -ausbildung | Schulung zu Sicherheitsanforderungen bei Remote-Arbeit und Meldeverfahren |
| A.8.1 Endbenutzergeräte | Gerätesicherheits-Baselines für Remote- und mobile Endpunkte |
| A.8.5 Sichere Authentifizierung | MFA- und Authentifizierungsanforderungen für den Remote-Zugriff |

**Verwandte interne Richtlinien**:

- Zugangskontrollrichtlinie
- Endgerätesicherheitsrichtlinie
- Incident-Management-Richtlinie
- Informationsklassifizierungs- und Handhabungsrichtlinie
- Informationsübertragungsrichtlinie
- Richtlinie zur akzeptablen Nutzung und Rückgabe von Werten

---

# Richtlinie zur Remote-Arbeit und Sicherheitsereignismeldung

## Zweck

Diese Richtlinie legt die Anforderungen der Organisation an eine sichere Remote-Arbeit und die zeitgerechte Meldung von Informationssicherheitsereignissen fest. Sie definiert die erforderlichen Sicherheitsmassnahmen für Personal, das ausserhalb der Betriebsstätten arbeitet, und stellt allen Mitarbeitenden einen strukturierten Mechanismus zur Meldung beobachteter oder vermuteter Sicherheitsereignisse über geeignete Kanäle zur Verfügung.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem sie technische und organisatorische Massnahmen proportional zum Risiko zum Schutz von Personendaten (einschliesslich besonders schützenswerter Personendaten) in Remote-Arbeitsumgebungen umsetzt. Soweit die Organisation Daten von Personen in der EU/EWR verarbeitet, gelten zusätzlich die DSGVO-Anforderungen.

Diese beiden Controls werden zusammengefasst, weil Remote-Arbeitende die erste Verteidigungslinie bei der Erkennung von Ereignissen sind, Remote-Arbeitende Bedrohungen ausgesetzt sind, die im Büro nicht vorhanden sind, und ISO 27002:2022 ausdrücklich vorschreibt, dass Verfahren zur Vorfallmeldung von entfernten Standorten aus zugänglich sein müssen.

## Geltungsbereich

Alle Mitarbeitenden und Drittnutzer.

Alle betrieblichen und privaten Geräte, die für den Remote-Zugriff auf, die Verarbeitung von oder die Speicherung von Organisationsinformationen genutzt werden.

Alle Remote-Arbeitsvereinbarungen, einschliesslich Homeoffice, Co-Working-Spaces, Kundenstandorte und Arbeit während Reisen.

Alle Personen, die für die Meldung von Sicherheitsereignissen verantwortlich sind, unabhängig vom Arbeitsort.

## Grundsatz

Remote-Arbeit muss formell genehmigt und mit Sicherheitskontrollen proportional zur Klassifizierung der zugegriffenen Informationen versehen sein. Alle Mitarbeitenden müssen beobachtete oder vermutete Informationssicherheitsereignisse unverzüglich und über die vorgesehenen Kanäle melden. Die Organisation fördert eine Kultur ohne Schuldzuweisungen, in der gutgläubige Meldungen geschützt und gefördert werden.

---

# Teil 1 — Remote-Arbeit (A.6.7)

## Genehmigung der Remote-Arbeit

Alle regelmässigen Remote-Arbeitsvereinbarungen müssen vor Beginn formell genehmigt werden.

- **Genehmigungsinstanz**: Der direkte Vorgesetzte genehmigt die Remote-Arbeitsvereinbarung; IT-Sicherheit genehmigt den technischen Zugriff.
- **Risikobewertung**: Für Stellen, die von zu Hause aus auf vertrauliche oder eingeschränkte Daten zugreifen, muss eine Risikobewertung durchgeführt werden. Diese muss mindestens folgende Aspekte berücksichtigen: (a) Klassifizierungsstufe der remote zugegriffenen Daten; (b) physische Sicherheitsfähigkeit des Remote-Standorts; (c) Netzwerksicherheitslage am Remote-Standort; (d) Compliance des Geräts mit der Sicherheits-Baseline; und (e) regulatorische oder vertragliche Einschränkungen.
- **Dokumentierte Bestätigung**: Remote-Arbeitende müssen eine Bestätigung unterzeichnen, dass sie die Sicherheitsanforderungen dieser Richtlinie verstehen und akzeptieren.
- **Jährliche Überprüfung**: Alle Remote-Arbeitsgenehmigungen müssen mindestens jährlich überprüft werden. Die Überprüfungen müssen bestätigen, dass die Genehmigung weiterhin angemessen ist, die Sicherheitsanforderungen eingehalten werden und Änderungen der Rolle, des Datenzugriffs oder des Arbeitsorts berücksichtigt sind.

**Standortgenehmigung**:
- **Standard-Remote-Standorte** (Homeoffice in der Schweiz, etablierter Remote-Arbeitsplatz): Genehmigung des direkten Vorgesetzten ausreichend.
- **Internationale Remote-Arbeit** (Arbeit ausserhalb der Schweiz): Erfordert ISB-Genehmigung + HR-Genehmigung + rechtliche Prüfung (steuerliche, arbeitsrechtliche und datenspeicherungsrechtliche Implikationen).
- **Temporäre Remote-Arbeit von risikoreichen Standorten** (öffentliche Co-Working-Spaces, Cafés, Reisen): Erfordert die Kenntnis des direkten Vorgesetzten; der Zugriff auf vertrauliche Daten von öffentlichen Standorten ist untersagt.

**Standortänderungen**: Dauerhafte Änderungen des Remote-Arbeitsstandorts (z. B. Umzug in ein neues Heim, längere Reisen) sind dem direkten Vorgesetzten und der IT-Sicherheit innerhalb von **14 Tagen** zu melden.

**Widerruf**: Die Remote-Arbeitsgenehmigung wird widerrufen, wenn das Anstellungs- oder Vertragsverhältnis endet, die Rolle auf eine für Remote-Arbeit ungeeignete wechselt, die Sicherheitsanforderungen nicht mehr eingehalten werden, Richtlinienverstösse auftreten oder betriebliche Anforderungen die Anwesenheit vor Ort verlangen.

## Registrierung und Verantwortlichkeiten mobiler Geräte

Mobile Geräte, die für die Remote-Arbeit ausgegeben oder zugelassen wurden, müssen im Inventarverzeichnis erfasst und einer namentlich genannten Person zugewiesen werden.

**Anforderungen an die Geräteregistrierung**:

- Alle mobilen Geräte (betriebliche und genehmigte BYOD-Geräte) müssen im Inventarverzeichnis mit dem zugewiesenen Eigentümer, Gerätetyp, Seriennummer und Verwendungszweck erfasst werden.
- Die zugewiesenen Eigentümer erhalten eine Kopie dieser Richtlinie und werden über ihre Verantwortlichkeiten informiert.
- Auf den Geräten müssen geeignete Verschlüsselung, Virenschutz/Endpunktschutz und Zugriffskontrollen installiert sein.

**Verantwortlichkeiten der zugewiesenen Eigentümer**:

- Sicherstellen, dass Betriebssystem- und Anwendungs-Patches zeitnah eingespielt werden.
- Sicherstellen, dass Verschlüsselung und Endpunktschutz aktiviert und aktuell bleiben.
- Das Gerät nicht unbeaufsichtigt lassen; es physisch sichern, wenn es nicht genutzt wird.
- Nur auf die für die eigene Rolle erforderlichen Organisationsinformationen zugreifen, gemäss der Zugangskontrollrichtlinie.
- Keine Software installieren oder Änderungen vornehmen, die gegen die Informationssicherheitsrichtlinien, Vorschriften oder anwendbares Recht verstossen würden.
- Anderen Personen, einschliesslich Familienangehörigen, keinen Zugang zum zugewiesenen Gerät gestatten.
- Keine Personendaten oder besonders schützenswerte Personendaten (gemäss nDSG) auf dem Gerät speichern, sofern dies nicht genehmigt und im Inventarverzeichnis dokumentiert ist.
- Das mobile Gerät zurückgeben, wenn es nicht mehr benötigt wird, auf Anfrage oder beim Ausscheiden aus der Organisation.

## Remote-Wipe und Backup

- **Remote-Wipe**: Alle betrieblichen mobilen Geräte müssen vor der Ausgabe an den Nutzer mit einer Remote-Wipe-Funktion ausgestattet sein. Die automatische Sperrung muss aktiviert sein (maximal 5 fehlgeschlagene Authentifizierungsversuche).
- **Backup**: Mobile Geräte werden standardmässig nicht in betriebliche Backup-Lösungen aufgenommen. Nutzer müssen Arbeitsdateien an genehmigten Cloud- oder Netzwerkstandorten speichern (z. B. SharePoint, OneDrive for Business, genehmigter Dateiserver). Kritische Arbeitsdaten dürfen nicht ausschliesslich im lokalen Gerätespeicher gespeichert werden.

## Physische Sicherheit

Remote-Arbeitende müssen eine physische Sicherheit proportional zur Klassifizierung der verarbeiteten Informationen gewährleisten:

- **Bildschirmpositionierung**: Bildschirme so ausrichten, dass unbefugtes Einsehen durch andere Personen im Arbeitsbereich verhindert wird.
- **Sichtschutzfilter**: Sichtschutzfilter verwenden, wenn in gemeinsam genutzten oder öffentlichen Bereichen gearbeitet wird (Co-Working-Bereiche, Cafés, öffentliche Verkehrsmittel).
- **Gerätesicherheit**: Arbeitsgeräte sichern, wenn der Arbeitsbereich unbeaufsichtigt ist. Geräte nie in öffentlichen Bereichen unbeaufsichtigt lassen. Geräte sperren, wenn man den Arbeitsplatz verlässt, auch nur kurz.
- **Aufgeräumter Schreibtisch**: Die Regelung zum aufgeräumten Schreibtisch (A.7.7 — siehe Richtlinie zur physischen und umgebungsbezogenen Sicherheit) gilt auch für Remote-Arbeitsumgebungen. Sensible Dokumente dürfen nicht sichtbar liegen bleiben, wenn sie nicht aktiv genutzt werden. Arbeitsmaterialien müssen am Ende jeder Arbeitssitzung gesichert werden.

  **Remote-Anforderungen für aufgeräumten Schreibtisch**:
  - Dokumente in Schublade, Aktenschrank oder gesichertem Homeoffice einschliessen, wenn nicht in Gebrauch.
  - Bildschirme sperren, wenn man den Arbeitsplatz verlässt (Windows+L, Ctrl+Cmd+Q).
  - Keine Arbeitsmaterialien auf Küchentischen, im Wohnzimmer oder anderen gemeinsam genutzten Familienbereichen liegen lassen.
- **Dokumentenvernichtung**: Sensible Dokumente müssen mit genehmigten Methoden entsorgt werden (Aktenvernichter). Ist am Remote-Standort kein Aktenvernichter vorhanden, sind sensible Dokumente für die sichere Vernichtung ins Büro zurückzubringen.
- **Zugang durch Familie und Besucher**: Den Zugang zu Arbeitsgeräten und -dokumenten durch Familienangehörige, Besucher oder andere unbefugte Personen verhindern.

## Technische Sicherheit

Für alle Remote-Zugriffe gelten folgende technische Sicherheitskontrollen:

- **VPN oder Zero Trust**: Alle Verbindungen zu internen Ressourcen der Organisation müssen über ein VPN oder eine gleichwertige Zero-Trust-Architektur erfolgen. Split-Tunnelling darf nur zugelassen werden, wenn eine Risikobewertung ein akzeptables Restrisiko nachweist und auf alle Organisationsressourcen über den verschlüsselten Tunnel zugegriffen wird.

  **Aktuelle Implementierung**: [Angabe: z. B. „Cisco AnyConnect VPN", „Palo Alto GlobalProtect", „Zero Trust über Cloudflare Access / Zscaler" oder „Auswahl laufend; Übergangsregelung: VPN erforderlich"]

  **VPN/Zero-Trust-Anforderungen**:
  - MFA vor Verbindungsaufbau erzwingen.
  - Gerätekonformitätsprüfung (Verschlüsselung, Patches, Endpunktschutz) vor Zugriffsgewährung erzwingen.
  - Sitzungen nach definierter Inaktivitätsdauer beenden (gemäss Sitzungs-Timeout-Anforderungen unten).
  - Alle Verbindungsversuche (erfolgreiche und fehlgeschlagene) protokollieren.
- **Multi-Faktor-Authentifizierung (MFA)**: MFA muss für alle Remote-Zugriffe auf Organisationssysteme vorgeschrieben sein. Dies umfasst VPN-Verbindungen, Cloud-Dienste, E-Mail und jedes System, das interne, vertrauliche oder eingeschränkte Daten enthält.
- **Verschlüsselung während der Übertragung**: Alle Daten, die zwischen Remote-Endpunkten und Organisationssystemen übertragen werden, müssen mindestens mit TLS 1.2 (bevorzugt TLS 1.3) verschlüsselt sein.
- **WLAN-Sicherheit**: Remote-Arbeitende dürfen nur sichere, verschlüsselte drahtlose Netzwerke verwenden (mindestens WPA2, bevorzugt WPA3).

  **Nutzung öffentlicher WLANs**:
  - **Verboten ohne VPN**: Öffentliche, ungesicherte WLANs (Flughäfen, Hotels, Cafés) dürfen für Organisationsarbeit nicht ohne VPN-Schutz genutzt werden.
  - **Mit VPN**: Öffentliche WLANs dürfen mit aktiver VPN-Verbindung nur für den Zugriff auf interne Daten genutzt werden.
  - **Vertrauliche Daten**: Der Zugriff auf vertrauliche Daten über öffentliche WLANs ist auch mit VPN nicht empfohlen; es sollte nach Möglichkeit ein Mobilfunk-Hotspot oder ein vertrauenswürdiges Netzwerk verwendet werden.
  - **Verbotene Aktivitäten im öffentlichen WLAN** (auch mit VPN): Finanztransaktionen, Passwortänderungen für kritische Konten (Mobilfunknetz oder vertrauenswürdiges Netzwerk verwenden).

  **Heimnetzwerksicherheit**: Remote-Arbeitende sollten ihre Heimnetzwerke absichern (Standard-Router-Passwort ändern, WPA3/WPA2 aktivieren, WPS deaktivieren, Router-Firmware-Updates einspielen).
- **Sitzungs-Timeout**: Remote-Zugriffssitzungen müssen nach einer definierten Inaktivitätsdauer getrennt werden (maximal 15 Minuten für Systeme mit vertraulichen oder eingeschränkten Daten; maximal 30 Minuten für andere Systeme).

## Datenhandhabung

Remote-Arbeitende müssen Daten entsprechend ihrer Klassifizierungsstufe gemäss der Informationsklassifizierungs- und Handhabungsrichtlinie behandeln:

| Datenklassifizierung | Remote-Speicherung zulässig | Bedingungen |
|---------------------|----------------------------|-------------|
| **Öffentlich** | Ja | Standardmässige Gerätesicherheit |
| **Intern** | Ja | Verschlüsseltes Gerät erforderlich |
| **Vertraulich** | Bedingt | Verschlüsseltes Gerät, genehmigter Speicherort, Genehmigung des direkten Vorgesetzten |
| **Eingeschränkt** | Nein (Standard) | Erfordert ausdrückliche ISB-Genehmigung mit dokumentierten Kompensationskontrollen |

Remote-Arbeitende müssen die Informationsübertragungsrichtlinie einhalten, wenn sie Organisationsdaten von Remote-Standorten aus senden oder empfangen. Organisationsdaten dürfen nicht in persönliche Cloud-Speicher, persönliche E-Mail-Konten oder nicht genehmigte Dateifreigabedienste übertragen werden.

## Anforderungen an betriebliche und BYOD-Geräte

### Betriebliche Geräte

Vom Unternehmen ausgegebene Geräte für die Remote-Arbeit müssen:

- Gemäss der organisatorischen Sicherheits-Baseline konfiguriert sein.
- Vollständige Festplattenverschlüsselung (FDE) aktiviert haben.
- Aktuelle Endpunktschutz-Software installiert und aktiv haben.
- Gemäss dem organisatorischen Patch-Zeitplan gepatcht und aktualisiert sein.
- Remote-Wipe-Funktion aktiviert haben.
- Im Geräteinventar registriert sein.

### BYOD (Bring Your Own Device)

Es ist nicht die Richtlinie der Organisation, standardmässig die Nutzung persönlicher mobiler Geräte für die Arbeit zuzulassen. Eine Genehmigung des Informationssicherheits-Managements ist erforderlich.

**BYOD-Genehmigungskriterien**:
- Geschäftliche Begründung (temporärer Bedarf, Rollenanforderung, Kostenreduktion).
- Das Gerät erfüllt die Mindestsicherheitsanforderungen (aktuelles Betriebssystem, MDM-kompatibel, kein Jailbreak/Root).
- Datenklassifizierung: BYOD nur für interne und öffentliche Daten erlaubt; vertrauliche Daten erfordern eine Ausnahmegenehmigung des ISB.
- Schulung abgeschlossen und Bestätigung der Verantwortung unterzeichnet.
- MDM- oder Containerisierungslösung installiert, bevor Zugang gewährt wird.

Wenn ein persönliches Gerät genehmigt wird:

- Das Gerät muss im Inventarverzeichnis registriert werden.
- Der Nutzer erhält Schulungen und unterzeichnet eine Bestätigung der Verantwortung.
- Es gelten alle Organisationsrichtlinien, einschliesslich dieser Richtlinie und der Zugangskontrollrichtlinie.
- Eine MDM- (Mobile Device Management) oder Containerisierungslösung muss installiert werden, um persönliche und organisatorische Daten zu trennen.
- Die Organisation behält sich das Recht vor, organisatorische Daten bei Beendigung des Arbeitsverhältnisses oder Zugangs, oder bei Verlust oder Diebstahl, remote vom Gerät zu löschen.
- Ausserhalb des verwalteten Containers dürfen keine Personendaten oder besonders schützenswerte Personendaten (gemäss nDSG) auf dem Gerät gespeichert werden.

### Verbotene Geräte

Folgende Geräte dürfen nicht für Organisationsarbeiten genutzt werden:

- Geräte mit Jailbreak oder Root.
- Geräte mit deaktivierten Sicherheitsfunktionen.
- Gemeinsam genutzte Geräte, die nicht unter der alleinigen Kontrolle des Nutzers stehen.
- Geräte mit abgekündigten Betriebssystemen, die keine Sicherheitsupdates mehr erhalten.
- Geräte, die die von der IT-Sicherheit definierten Mindestsicherheitsanforderungen nicht erfüllen können.

## Beendigung der Remote-Arbeit

Bei Widerruf der Remote-Arbeitsgenehmigung oder Beendigung des Arbeitsverhältnisses:

- Remote-Zugangsdaten werden sofort widerrufen (am selben Tag).
- VPN und Remote-Zugangstoken werden deaktiviert.
- Alle betrieblichen Geräte werden gemäss der Rückgaberichtlinie (A.5.11) zurückgegeben.
- Alle Organisationsdaten werden von persönlichen Geräten entfernt. Bei BYOD-Geräten wird das Remote-Wipe des organisatorischen Containers via MDM durchgeführt.
- Rückgabe und Datenlöschung werden verifiziert und dokumentiert.

---

# Teil 2 — Meldung von Sicherheitsereignissen (A.6.8)

## Meldekanäle

Die Organisation stellt allen Mitarbeitenden zugängliche Mechanismen zur Meldung beobachteter oder vermuteter Informationssicherheitsereignisse zur Verfügung.

**Anforderungen an die Kanäle**:

- Es müssen mindestens **zwei unterschiedliche Meldekanäle** verfügbar sein.
- Mindestens **ein Kanal** muss ausserhalb der Geschäftszeiten (24/7) verfügbar sein.
- Alle Kanäle müssen von Remote-Standorten aus zugänglich sein, ohne dass Zugang zu internen Systemen erforderlich ist (um die Meldung von zugriffsbezogenen Ereignissen zu ermöglichen).

**Standard-Meldekanäle**:

| Kanal | Zweck | Verfügbarkeit |
|-------|-------|---------------|
| **Sicherheits-E-Mail** (z. B. security@[organisation].ch) | Nicht dringende Ereignisse, detaillierte Berichte mit Anhängen | 24/7 (überwacht während Geschäftszeiten) |
| **Telefon / Hotline** | Dringende Ereignisse, aktive Angriffe, verlorene/gestohlene Geräte | 24/7 (Bereitschaft ausserhalb der Geschäftszeiten) |
| **Ticketing-System** | Formelle Ereigniserfassung, Nachverfolgung, Follow-up | Geschäftszeiten |
| **Anonyme Option** (Webformular oder Drittanbieter-Hotline) | Meldungen, bei denen der Meldende anonym bleiben möchte | 24/7 |

**Anonyme Meldungen**:
- **Zweck**: Ermöglicht die Meldung von vermuteten Richtlinienverstössen, Insider-Bedrohungen oder heiklen Anliegen, bei denen der Meldende Repressalien befürchtet.
- **Anonymitätssicherung**: Der anonyme Kanal wird von einem Drittanbieter betrieben (falls zutreffend) oder über ein Webformular ohne personenbezogene Protokollierung. Die Identität des Meldenden wird nicht verfolgt oder protokolliert.
- **Eingeschränkte Nachverfolgung**: Da die Identität des Meldenden unbekannt ist, ist die Nachverfolgung begrenzt. Anonyme Meldende werden ermutigt, das Meldeportal/den Kanal auf Antworten zu prüfen, falls das System eine bidirektionale anonyme Kommunikation unterstützt.
- **Alternative Vorgehensweise**: Meldende können sich auch an HR oder Legal mit Vertraulichkeitsgarantie (nicht vollständige Anonymität) wenden, wenn eine Nachverfolgung erforderlich ist.

Anonyme Meldungen erhalten dieselbe Priorität und Untersuchung wie identifizierte Meldungen.

**Veröffentlichung**: Meldekanäle werden im Intranet veröffentlicht, in die Einarbeitungsunterlagen für Mitarbeitende aufgenommen, in der jährlichen Sicherheitsschulung referenziert und auf Anmeldebildschirmen oder Desktop-Hintergrundbildern angezeigt.

## Meldepflichtige Ereignisse

**Unterschied zwischen Ereignis und Vorfall**:

| Begriff | Definition |
|---------|------------|
| **Sicherheitsereignis** | Ein identifiziertes Vorkommnis, das auf einen *möglichen* Verstoss gegen die Sicherheitsrichtlinie oder einen Kontrollausfall hinweist |
| **Sicherheitsvorfall** | Ein Sicherheitsereignis, das bewertet und als tatsächlich oder potenziell nachteilig für die Vertraulichkeit, Integrität oder Verfügbarkeit von Informationen bestätigt wurde |

**Mitarbeitende melden EREIGNISSE. Das IT-Sicherheitsteam bewertet, ob Ereignisse VORFÄLLE darstellen.** Im Zweifelsfall melden.

**Kategorien meldepflichtiger Ereignisse**:

**Phishing und Social Engineering**:

- Verdächtige E-Mails, die nach Zugangsdaten, Zahlungen oder sensiblen Informationen fragen.
- Verdächtige Telefonanrufe oder Textnachrichten, die Kollegen oder Lieferanten imitieren.
- Versuchte Manipulation zur Umgehung von Sicherheitskontrollen oder zur Erlangung von Zugang.

**Malware und Systemkompromittierung**:

- Unerwartetes Systemverhalten, Leistungseinbussen oder Abstürze.
- Verdächtige Pop-ups, Meldungen oder Benachrichtigungen.
- Vermutete Malware-Infektion (einschliesslich Ransomware-Indikatoren).
- Systemveränderungen, die nicht über das Change-Control-Verfahren verarbeitet wurden.

**Unbefugter Zugriff**:

- Unbekannte oder unerwartete Anmeldeversuche bei Konten.
- Unbekannte Geräte, die bei Konten angemeldet sind.
- Unerwartete Kontosperrungen oder Passwortänderungen.
- Verdächtige Rechteänderungen oder neue Administratorkonten.

**Datenverletzung und -abfluss**:

- Fehlgeleitete E-Mails mit sensiblen oder personenbezogenen Daten.
- Unbefugter Datenzugriff, -offenlegung oder -download.
- Verlorene oder gestohlene Dokumente oder Medien mit Organisationsdaten.
- Vermutete Datenexfiltration.

**Physische Sicherheit**:

- Verlorene oder gestohlene Geräte (Laptops, Telefone, USB-Sticks, Zugangsausweise).
- Tailgating oder unbefugter physischer Zutritt zu gesicherten Bereichen.
- Fehlendes oder beschädigtes Equipment.

**Richtlinienverstösse**:

- Beobachtete Umgehung von Sicherheitskontrollen.
- Bekannte Richtlinienverstösse durch andere.
- Nicht genehmigte Softwareinstallationen oder Konfigurationsänderungen.

**Remote-Arbeit-spezifisch**:

- Vermutete Kompromittierung des Heimnetzwerks oder Routers.
- Unbefugter Zugriff auf das Arbeitsgerät durch Familienmitglieder oder andere.
- VPN- oder Remote-Zugangsausfälle, die auf einen Angriff oder eine Kompromittierung hindeuten.
- Verdächtige Aktivitäten beim Arbeiten von öffentlichen Standorten.
- Gerätediebstahl oder -verlust auf Reisen oder an einem Remote-Standort.
- Verdächtige IT-Support-Anfragen, die nach Remote-Zugangsdaten fragen.
- Konfigurationsänderungen am Heimrouter, die nicht vom Nutzer veranlasst wurden.
- Physisches Einsehen von Arbeitsmaterialien durch unbefugte Personen.

### Verfahren bei verlorenem oder gestohlenem Gerät

Wenn ein Gerät mit Organisationsdaten verloren geht oder gestohlen wird:

1. **Sofort melden** über Telefon/Hotline (Kritischer Schweregrad — sofort melden).
2. **Details angeben**: Gerätetyp, Seriennummer (falls bekannt), letzter bekannter Standort, ungefähre Zeit des Verlusts/Diebstahls, Datenklassifizierung der auf dem Gerät gespeicherten Daten.
3. **Massnahmen des IT-Sicherheitsteams**:
   - Remote-Wipe einleiten (wenn das Gerät eingeschaltet und verbunden ist).
   - VPN und Remote-Zugangsdaten widerrufen.
   - Auf verdächtige Kontoaktivitäten überwachen.
   - Vorfall für die Untersuchung dokumentieren.
4. **Massnahmen des Nutzers**:
   - Passwörter für Konten ändern, auf die vom verlorenen Gerät aus zugegriffen wurde (auf Anweisung des IT-Sicherheitsteams).
   - Polizeianzeige erstatten (bei Diebstahl) und Aktenzeichen dem IT-Sicherheitsteam mitteilen.
   - Nicht versuchen, das Gerät selbst zu bergen (Persönliche Sicherheit hat Vorrang).
5. **Versicherung / Ersatz**: HR für den Geräte-Ersatzprozess kontaktieren.

**Beweissicherung**: Wenn das Gerät später wiedergefunden wird, darf es nicht eingeschaltet oder benutzt werden. Es ist dem IT-Sicherheitsteam für die forensische Analyse zu übergeben.

## Meldeverfahren

**Was in eine Meldung aufzunehmen ist** (soweit bekannt):

- Datum und Uhrzeit der Beobachtung oder Entdeckung des Ereignisses.
- Beschreibung des Vorgefallenen.
- Möglicherweise betroffene Systeme, Anwendungen oder Daten.
- Bereits ergriffene Massnahmen (falls vorhanden).
- Kontaktdaten für die Nachverfolgung (sofern nicht anonym gemeldet wird).
- Etwaige unterstützende Beweise (Screenshots, E-Mail-Header, Fehlermeldungen).

**Meldefristen**:

| Schweregrad des Ereignisses | Beispiele | Meldefrist |
|-----------------------------|-----------|------------|
| **Kritisch** | Aktiver Angriff, bestätigte Datenverletzung, Ransomware, gestohlenes Gerät mit eingeschränkten Daten | Sofort |
| **Hoch** | Verlorenes/gestohlenes Gerät, Kompromittierung von Zugangsdaten, vermutete Malware-Infektion | Innerhalb von 1 Stunde |
| **Mittel** | Phishing-Versuch (nicht angeklickt), verdächtige Aktivität, beobachteter Richtlinienvestoss | Innerhalb von 4 Stunden |
| **Niedrig** | Allgemeine Sicherheitsbedenken, geringfügige Richtlinienabweichung, ungewöhnliche, aber nicht bedrohliche Aktivität | Innerhalb von 24 Stunden |

Bei Unsicherheit über den Schweregrad auf der höheren Stufe melden. Das IT-Sicherheitsteam wird den Schweregrad beim Triage neu bewerten. Die Meldung nicht verzögern, um eine genaue Einstufung vorzunehmen.

**Verantwortlichkeiten der Meldenden**:

- Gemäss den oben genannten Fristen unverzüglich melden.
- Nach bestem Wissen genaue Informationen bereitstellen.
- **Beweise sichern**: Phishing-E-Mails als Anhänge weiterleiten (nicht inline weiterleiten oder auf Links klicken). Anomalien mit Screenshots festhalten und genaue Uhrzeit und betroffene Systeme notieren. Physische Sicherheitsereignisse fotografieren, wenn sicher.
- **NICHT** versuchen, das Ereignis selbst zu untersuchen, zu verifizieren oder zu beheben.
- **NICHT** versuchen, vermutete Schwachstellen zu testen oder auszunutzen.
- Mit einer eventuellen Nachuntersuchung durch das IT-Sicherheitsteam zusammenarbeiten.

## Kultur ohne Schuldzuweisungen

Die Organisation fördert ein nicht-strafendes Umfeld für die Meldung von Sicherheitsereignissen.

| Grundsatz | Verpflichtung |
|-----------|---------------|
| **Schutz bei gutem Glauben** | Mitarbeitende, die Ereignisse in gutem Glauben melden, werden für den Meldevorgang selbst nicht negativ sanktioniert |
| **Umgang mit ehrlichen Fehlern** | Ehrliche Fehler (z. B. Klicken auf einen Phishing-Link), die unverzüglich gemeldet werden, werden konstruktiv behandelt, mit Fokus auf Lernen und Prävention |
| **Kein Vergeltungsverbot** | Repressalien gegen gutgläubige Meldende sind untersagt und werden selbst disziplinarisch geahndet |
| **Vertraulichkeit der Meldenden** | Die Identität der Meldenden wird so weit wie möglich geschützt und nur auf Need-to-know-Basis weitergegeben |

Die Organisation würdigt und fördert vorbildliches Meldeverhalten. Gemeldete Ereignisse werden als Lernchancen, nicht als Anlass für Bestrafungen genutzt.

**Ausnahmen vom Schutz bei gutem Glauben**:

- Absichtliche Richtlinienverstösse, die erst nach Entdeckung durch andere gemeldet werden.
- Bösartige Aktivitäten, die als versehentlich getarnt werden.
- Wiederholte Nachlässigkeit nach Schulungen und formellen Verwarnungen.
- Böswillig erstattete falsche Anzeigen.

## Reaktion und Rückmeldung

Die Organisation reagiert auf alle Sicherheitsereignismeldungen innerhalb definierter Fristen:

| Reaktionstyp | Frist |
|-------------|-------|
| **Bestätigung** (Eingang der Meldung bestätigen) | Innerhalb von 4 Geschäftsstunden |
| **Erstbewertung** (Ereignis klassifiziert, Priorität zugewiesen) | Innerhalb von 24 Stunden |
| **Statusaktualisierung an den Meldenden** | Innerhalb von 72 Stunden |
| **Abschlussmitteilung** | Nach Lösung |

Die Organisation:

- Bestätigt den Eingang aller Meldungen (einschliesslich anonymer Meldungen, wo ein Antwortkanal vorhanden ist).
- Informiert die Meldenden über den Fortschritt und das Ergebnis ihrer Meldungen.
- Kommuniziert aus Ereignissen gezogene Lehren durch Awareness-Updates (ohne Identifizierung der Meldenden).
- Eskaliert Ereignisse in den Incident-Management-Prozess (gemäss A.5.24-28), wenn das Ereignis als bestätigter Sicherheitsvorfall bewertet wird, über die erste Reaktion hinausgehende Ressourcen erfordert, regulatorische Meldepflichten hat oder mehrere Systeme oder Geschäftsbereiche betrifft.

## Meldestatistiken

Die Organisation verfolgt folgende Kennzahlen zur Sicherheitsereignismeldung:

| Kennzahl | Ziel | Überprüfungsfrequenz |
|----------|------|---------------------|
| **Bestätigung innerhalb von 4 Geschäftsstunden** | 100% | Monatlich |
| **Erstbewertung innerhalb von 24 Stunden** | 100% | Monatlich |
| **Ereignisvolumens-Trend** (zunehmendes Bewusstsein oder zunehmende Bedrohung) | Verfolgt | Vierteljährlich |
| **Nutzung der Meldekanäle** (E-Mail, Telefon, Ticketing, anonym) | Ausgewogene Nutzung über alle Kanäle | Vierteljährlich |
| **Rückmeldung der Meldenden** (Zufriedenheit mit Reaktion und Kommunikation) | >80% zufrieden | Jährlich (Umfrage) |
| **Fehlalarmrate** (Ereignisse vs. bestätigte Vorfälle) | Verfolgt | Vierteljährlich |

Kennzahlen werden dem ISB monatlich und dem Management-Review-Team vierteljährlich berichtet.

**In die Awareness-Schulung integrierte Ereignismelde-KPIs**: Die jährliche Schulung umfasst Meldevolumen und Erfolgsgeschichten, um die Kultur ohne Schuldzuweisungen zu stärken.

---

## Schulung und Sensibilisierung zur Ereignismeldung

Alle Mitarbeitenden erhalten Schulungen zur Meldung von Sicherheitsereignissen:

**Erstschulung** (innerhalb von 30 Tagen nach Eintritt oder Rollenwechsel):
- Was ein Sicherheitsereignis im Vergleich zu einem Vorfall darstellt.
- Kategorien meldepflichtiger Ereignisse mit Beispielen.
- Meldekanäle und wann welcher zu verwenden ist.
- Meldefristen nach Schweregrad.
- Kultur ohne Schuldzuweisungen und Schutz bei gutem Glauben.

**Jährliche Auffrischungsschulung**:
- Aktualisierte Bedrohungslandschaft (aktuelle Phishing-Kampagnen, Social-Engineering-Taktiken).
- Erfolgsgeschichten (gemeldete Ereignisse, die Vorfälle verhindert haben).
- Meldestatistiken (Vermittlung, dass Meldungen wertvoll sind).

**Phishing-Simulation**: Vierteljährliche Phishing-Simulationen mit sofortiger Schulung für Nutzer, die klicken; Simulationen werden als Lernmöglichkeiten, nicht als Strafmassnahmen behandelt.

Schulungsabschlüsse werden verfolgt; Ziel: **100% des Personals** absolviert die jährliche Schulung.

---

## Überprüfung der Remote-Work-Compliance

Die Compliance mit der Remote-Work-Sicherheit wird durch Folgendes überprüft:

**Vierteljährliche Compliance-Prüfungen**:
- VPN/MFA-Nutzungsprotokolle (100% der Remote-Arbeitenden greifen via VPN mit MFA zu).
- Geräteverschlüsselungsstatus (100% der registrierten Geräte verschlüsselt).
- Aktueller Endpunktschutz (100% der Geräte mit aktuellem Antivirus/EDR).
- Patch-Compliance (≥95% der Geräte mit aktuellem Betriebssystem und kritischen Patches).

**Jährliche Remote-Work-Überprüfungen**:
- Überprüfung der Remote-Arbeitsgenehmigungen (Bestätigung, dass Genehmigungen aktuell und angemessen sind).
- Audit des BYOD-Geräteinventars (Sicherstellung, dass alle persönlichen Geräte registriert und compliant sind).
- Remote-Arbeitende mit hohem Risiko (Zugriff auf vertrauliche Daten) — Aktualisierung der Risikobewertung.

**Stichprobenprüfungen** (zufällig oder anlassbezogen):
- Die IT-Sicherheit kann Remote-Compliance-Prüfungen durchführen (Screenshots anfordern, die Verschlüsselung, Endpunktschutz und VPN-Verbindung zeigen).
- Nicht-Compliance löst einen Massnahmenplan oder den Entzug der Remote-Work-Privilegien aus.

Compliance-Kennzahlen werden dem ISB vierteljährlich gemeldet.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten |
|-------|---------------------|
| **Geschäftsleitung** | Genehmigt die Remote-Work-Richtlinie; stellt Ressourcen bereit; fördert die Kultur ohne Schuldzuweisungen; erhält Briefings zu kritischen Sicherheitsereignissen |
| **ISB** | Definiert Sicherheitsanforderungen für Remote-Arbeit und Ereignismeldemechanismen; genehmigt Ausnahmen bei hohem Risiko; überwacht die Compliance; berichtet an die Geschäftsleitung |
| **IT-Sicherheitsteam** | Implementiert und unterhält Remote-Zugriffskontrollen; nimmt Ereignismeldungen entgegen und bewertet diese; koordiniert die Reaktion; gibt Rückmeldung an Meldende; pflegt Meldekanäle |
| **IT-Betrieb** | Stellt Remote-Zugang bereit (VPN, MFA, Geräte); unterstützt die Infrastruktur der Meldekanäle; führt Eindämmungsmassnahmen auf Anweisung durch |
| **HR** | Verwaltet Remote-Arbeitsvereinbarungen und -beendigungen; bezieht Ereignismeldung in Onboarding ein; koordiniert personalbezogene Angelegenheiten |
| **Direkte Vorgesetzte** | Genehmigen Remote-Arbeit für Teammitglieder; stellen Team-Compliance sicher; fördern Ereignismeldung; eskalieren Sicherheitsbedenken |
| **Alle Mitarbeitenden** | Halten Remote-Work-Anforderungen ein; sichern Geräte und Daten; melden Ereignisse unverzüglich; sichern Beweise; arbeiten mit Untersuchungen zusammen |

---

## Nachweise

Die folgenden Nachweise belegen die Compliance mit dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit |
|---|---------|------------|------------|
| 1 | **Genehmigungsunterlagen für Remote-Arbeit** (genehmigte Vereinbarungen mit Risikobewertung, sofern zutreffend) | HR / Direkte Vorgesetzte | *Pro Vereinbarung; jährlich überprüft; Aufbewahrungsdauer + 2 Jahre* |
| 2 | **Richtlinienbestätigungen** von Remote-Arbeitenden | HR | *Pro Onboarding / jährliche Erneuerung; Ziel: 100% Abdeckung* |
| 3 | **Geräteinventar** (betriebliche und genehmigte BYOD-Geräte, die Remote-Arbeitenden zugewiesen sind) | IT-Betrieb | *Innerhalb von 5 Arbeitstagen nach Änderung aktualisiert; jährlich geprüft* |
| 4 | **Technische Compliance-Berichte** (VPN-Nutzung, MFA-Registrierung, Geräteverschlüsselung, Patch-Status) | IT-Sicherheit | *Monatlich überprüft; Dashboard kontinuierlich aktualisiert* |
| 5 | **Sicherheitsereignismeldungen** über die vorgesehenen Kanäle | IT-Sicherheit | *Kontinuierlich geführt; mindestens 3 Jahre aufbewahrt* |
| 6 | **Ereignisreaktionsunterlagen** (Bestätigung, Bewertung, Statusaktualisierungen, Abschluss) mit Reaktionszeitkennzahlen | IT-Sicherheit | *Pro Ereignis; Compliance der Reaktionsfristen vierteljährlich überprüft* |
| 7 | **Sicherheitsbewusstseinsnachweise** zu Remote-Work-Sicherheit und Ereignismeldung | HR / IT-Sicherheit | *Jährlich; Abschluss verfolgt; Ziel: 100% der Remote-Arbeitenden* |
| 8 | **Verfügbarkeitsnachweise der Meldekanäle** (Tests und Verfügbarkeit von E-Mail, Telefon, Ticketing, anonymen Kanälen) | IT-Betrieb | *Vierteljährlich getestet; Ergebnisse dokumentiert* |
| 9 | **Geräterückgabe- und Datenlöschunterlagen** bei Beendigung der Remote-Arbeit | IT-Betrieb / HR | *Pro Beendigung; verifiziert und gegengezeichnet* |
| 10 | **Ausnahmenregister** (genehmigte Ausnahmen von dieser Richtlinie mit Begründung und Kompensationskontrollen) | ISB | *Pro Ausnahme aktualisiert; vierteljährlich überprüft; zeitlich begrenzte Einträge bei Ablauf neu bewertet* |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Informationssicherheits-Management-Team überprüft die Compliance mit dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf, Analyse der Remote-Zugriffsprotokolle, Geräte-Compliance-Berichte, Kennzahlen zur Ereignismeldung (Volumen, Aktualität, Reaktionszeiten), interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vorab vom Informationssicherheitsbeauftragten genehmigt und dokumentiert werden, mit dokumentierter Risikoakzeptanz, Kompensationskontrollen und einem definierten Überprüfungsdatum. Ausnahmen sind dem Management-Review-Team zu melden.

## Nicht-Compliance

Ein Mitarbeitender, der gegen diese Richtlinie verstossen hat, kann disziplinarischen Massnahmen bis hin zur Kündigung des Arbeitsverhältnisses unterliegen. Nicht-Compliance mit Remote-Work-Anforderungen kann auch zum Entzug der Remote-Work-Privilegien führen. Das Versäumnis, Sicherheitsereignisse zu melden, geniesst keinen Schutz der Kultur ohne Schuldzuweisungen und kann als Richtlinienverstos behandelt werden.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen der Remote-Work-Muster, neue Bedrohungen für Remote-Arbeitende, regulatorische Änderungen (insbesondere nDSG und DSGVO), technologische Entwicklungen, Trends bei der Ereignismeldung und aus Vorfällen gezogene Lehren.

---

# Abgedeckte Bereiche des ISO 27001-Standards

Richtlinie zur Remote-Arbeit und Sicherheitsereignismeldung — ISO 27001-Control-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Politik | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | 5.36 Compliance mit Richtlinien, Regeln und Standards |
| Klausel 7.3 Bewusstsein | 6.3 Informationssicherheitsbewusstsein, -schulung und -ausbildung |
| Klausel 8.1 Betriebsplanung und -steuerung | 6.4 Disziplinarverfahren |
| | **6.7 Remote-Arbeit** |
| | **6.8 Meldung von Informationssicherheitsereignissen** |
| | 7.9 Sicherheit von Werten ausserhalb des Betriebsgeländes |
| | 8.1 Endbenutzergeräte |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen zum Datenschutz in Remote-Umgebungen |
| Schweizerisches OR Art. 328b | Mitarbeiterdatenverarbeitung auf die für das Arbeitsverhältnis notwendigen Daten beschränkt |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1-3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung muss sich auf Remote-Arbeit erstrecken; Art. 33 — Breach-Benachrichtigung innerhalb von 72 Stunden erfordert zeitnahe Ereigniserkennung |
| ISO/IEC 27001:2022 | Annex A Controls 6.7, 6.8 |
| ISO/IEC 27002:2022 | Abschnitte 6.7, 6.8 — Implementierungshinweise |
| NIST SP 800-46 Rev 2 | Leitfaden zur Unternehmensfernarbeit, Remote-Zugriff und BYOD-Sicherheit |
| CIS Controls v8 | Control 4 (Sichere Konfiguration von Unternehmens-Assets), Control 6 (Access Control Management), Control 17 (Incident Response Management) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
