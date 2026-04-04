<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.29-DE:operational:OP-POL:a.5.29 -->
**ISMS-OP-POL-A.5.29 — Informationssicherheit bei Störungen**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationssicherheit bei Störungen |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.29 |
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
| 1.0 | [Datum] | ISB | Erste operative Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Kontrolle A.5.29 — Informationssicherheit bei Störungen
- ISO/IEC 22301 — Business-Continuity-Managementsysteme (informativer Verweis)
- NIST SP 800-34 Rev 1 — Contingency Planning Guide for Federal Information Systems (informativer Verweis)
- NIST SP 800-61 Rev 2 — Computer Security Incident Handling Guide (informativer Verweis)

**Verwandte Annex-A-Kontrollen**:

| Kontrolle | Bezug zur Informationssicherheit bei Störungen |
|-----------|------------------------------------------------|
| A.5.24–28 Incident-Management-Lebenszyklus | Sicherheitsvorfälle können Betriebsstörungen auslösen oder damit zusammenfallen |
| A.5.30 IKT-Bereitschaft für Geschäftskontinuität | BC/DR-Planung liefert den operativen Rahmen; A.5.29 liefert die Sicherheitsschicht |
| A.8.13 Informations-Backup | Backup-Schutz ist eine nicht verhandelbare Sicherheitskontrolle bei Störungen |
| A.8.14 Redundanz von Informationsverarbeitungseinrichtungen | Sicherheit des Recovery-Standorts muss dem primären Standort gleichwertig sein |
| A.5.15–16–18 Identitäts- und Zugangsverwaltung | Notfall-Zugriffsverfahren und Zugangskontrolle bei Störungen |
| A.8.15 Protokollierung | Protokollierungskontinuität ist auch bei eingeschränktem Betrieb obligatorisch |
| A.8.16 Überwachungsaktivitäten | Erweiterte Überwachung im erhöhten und eingeschränkten Zustand erforderlich |

**Verwandte interne Richtlinien**:

- Richtlinie zur Geschäftskontinuität und Disaster Recovery
- Richtlinie zum Incident Management
- Richtlinie zur Identitäts- und Zugangsverwaltung
- Protokollierungsrichtlinie
- Richtlinie zu Überwachungsaktivitäten (A.8.16)
- Change-Management-Richtlinie

---

# Richtlinie zur Informationssicherheit bei Störungen

## Zweck

Diese Richtlinie legt Anforderungen zur Aufrechterhaltung von Informationssicherheitskontrollen bei störenden Ereignissen fest. Störungen — sei es durch Naturkatastrophen, Infrastrukturausfälle, Cyberangriffe, Pandemien oder Unterbrechungen in der Lieferkette — schaffen Bedingungen, unter denen Sicherheitskontrollen genau dann am wahrscheinlichsten geschwächt werden, wenn die Bedrohungsexposition am höchsten ist.

**«Sicherheit kennt keinen Urlaub.»** Wenn sich Organisationen auf die Wiederherstellung konzentrieren, nutzen Angreifer die reduzierte Wachsamkeit, abgelenktes Personal und beeinträchtigte Kontrollen aus. Diese Richtlinie stellt sicher, dass die Organisation während aller Phasen von Störungen und der Wiederherstellung eine definierte Mindestsicherheitslage aufrechterhält und überprüft, dass vollständige Sicherheitskontrollen wiederhergestellt sind, bevor zum Normalbetrieb zurückgekehrt wird.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG) Art. 8, indem geeignete technische und organisatorische Sicherheitsmassnahmen auch unter ungünstigen Bedingungen aufrechterhalten werden. Soweit die Organisation Daten von Personen in der EU/EEA verarbeitet, gelten auch die DSGVO-Art.-32-Anforderungen für die laufende Sicherheit der Verarbeitung.

## Geltungsbereich

Diese Richtlinie gilt für:

- Alle störenden Ereignisse, die die Fähigkeit der Organisation zum Normalbetrieb beeinträchtigen, einschliesslich Naturkatastrophen, Infrastrukturausfälle, Cyber-Vorfälle, Pandemien, Unterbrechungen der Lieferkette und zivile Unruhen.
- Alle Informationssysteme, Netzwerke, Anwendungen und Datenverarbeitungseinrichtungen im ISO-27001-Geltungsbereich.
- Alle Business-Continuity- und Disaster-Recovery-Prozesse.
- Alle Mitarbeitenden — Angestellte, Auftragnehmer und Drittnutzer — während der Störungs- und Wiederherstellungsphasen.

## Grundsatz

**Die Sicherheit der Menschen hat stets oberste Priorität.**

Sobald Sicherheit und Wohlergehen des Personals gesichert sind, wird die Kontinuität der Informationssicherheit zur unmittelbaren Priorität. Die Organisation sollte Prozesse planen, implementieren und aufrechterhalten, um das erforderliche Niveau der Informationssicherheit unter ungünstigen Bedingungen zu gewährleisten, einschliesslich Ausgleichskontrollen, wenn Standardsicherheitsmassnahmen nicht aufrechterhalten werden können.

Keine Wiederherstellungsmassnahme, egal wie dringend, rechtfertigt die dauerhafte Entfernung von Kernsicherheitskontrollen. Wo eine vorübergehende Lockerung notwendig ist, sollte sie dokumentiert, zeitlich begrenzt, kompensiert und bis zum Abschluss verfolgt werden.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Störung** | Jedes Ereignis, das den normalen Geschäftsbetrieb unterbricht oder zu unterbrechen droht |
| **Sicherheitslage-Stufe** | Definierter Zustand der Sicherheitskontrollumsetzung (Normal, Erhöht, Eingeschränkt, Notfall, Wiederherstellung) |
| **Mindest-Sicherheits-Baseline** | Nicht verhandelbare Sicherheitskontrollen, die unabhängig vom Betriebsstatus aufrechterhalten werden müssen |
| **Break-Glass-Zugang** | Notfall-Privilegierter-Zugangs-Mechanismus, der aktiviert wird, wenn der normale Zugang nicht verfügbar ist |
| **Sicherheitsschuld** | Sicherheitskontrollen oder -aktivitäten, die während einer Störung verschoben wurden und später behoben werden müssen |
| **Recovery-Standort** | Alternativer Ort (physisch oder Cloud) für die Wiederaufnahme des Betriebs während einer Störung |
| **Ausgleichskontrolle** | Alternative Sicherheitsmassnahme, die implementiert wird, wenn die primäre Kontrolle nicht verfügbar ist |
| **Krisenmanagement-Team** | Funktionsübergreifendes Team, das zur Verwaltung der organisatorischen Reaktion auf eine grössere Störung aktiviert wird |

---

## Mindest-Sicherheits-Baseline

### Nicht verhandelbare Kontrollen

Die folgenden Sicherheitskontrollen sollten jederzeit aufrechterhalten werden, unabhängig vom Störungszustand. Diese Kontrollen unterliegen keiner Lockerung oder Ausnahme:

| Kontrollkategorie | Mindestanforderung | Begründung |
|-------------------|--------------------|------------|
| **Zugangskontrolle** | Authentifizierung für jeden Systemzugriff erforderlich | Verhindert unbefugten Zugriff unter chaotischen Bedingungen |
| **Datenverschlüsselung** | Verschlüsselung im Ruhezustand für vertrauliche und eingeschränkte Daten | Daten bleiben geschützt, wenn Medien während der Wiederherstellung verloren, gestohlen oder exponiert werden |
| **Protokollierung** | Kritische Systemprotokollierung auf allen Stufe-1- und Stufe-2-Systemen fortgesetzt | Prüfpfad für die Post-Incident-Untersuchung und regulatorische Compliance aufrechterhalten |
| **Netzwerksegmentierung** | Kritische Netzwerkgrenzen aufrechterhalten | Verhindert laterale Bewegung, wenn ein Angreifer die Störung ausnutzt |
| **Backup-Schutz** | Backups bleiben verschlüsselt und zugangskontrolliert | Verhindert Backup-Kompromittierung als alternativen Weg zum Datendiebstahl |

### Akzeptable Kontrollen im eingeschränkten Betrieb

Die folgenden Kontrollen können während einer Störung vorübergehend gelockert werden, vorbehaltlich dokumentierter Genehmigung durch den ISB (oder designierten Stellvertreter), Implementierung von Ausgleichskontrollen und Eintragung in das Sicherheitsschulden-Register:

| Kontrollkategorie | Akzeptable Einschränkung | Erforderliche Ausgleichskontrolle | Maximale Dauer |
|-------------------|--------------------------|------------------------------------|----------------|
| **Multi-Faktor-Authentifizierung** | Einzelfaktor, wenn MFA-Infrastruktur nicht verfügbar | Erweiterte Protokollierung, Sitzungszeitlimits, IP-basierte Beschränkungen | Dauer der Störung + 7 Tage |
| **Schwachstellen-Scanning** | Verzögertes geplantes Scanning | Manuelle Überprüfung kritischer Patches; kritische/hohe Patches innerhalb von 72 Std./7 Tagen anwenden | 30 Tage |
| **Sicherheitsüberwachung** | Reduzierter Überwachungsumfang | Fokus auf Stufe-1- und Stufe-2-Systeme; erweiterte manuelle Überprüfung | Dauer der Störung + 14 Tage |
| **Zugriffsüberprüfungen** | Verschobene periodische Überprüfungen | Strengere Genehmigung für neue Zugriffsanfragen während der Störung | 30 Tage |
| **Patch-Management** | Verzögertes Patching für unkritische Schwachstellen | Kritische und hohe Schwachstellen noch innerhalb von 72 Std./7 Tagen gepatcht | 30 Tage für nicht-kritische |

**Obligatorische Verfolgung**: Jede genehmigte Kontrolllockerung sollte sofort einen zeitgebundenen Eintrag im Sicherheitsschulden-Register erstellen, einschliesslich: Eigentümer, geltende Ausgleichskontrollen, Startdatum, Zielschlussdatum und Nachweis des Abschlusses nach der Behebung.

### Niemals akzeptabel

Die folgenden Massnahmen sind auch bei der schwersten Störung verboten. Es gibt keine Ausnahmen:

- **Deaktivierte Protokollierung** auf kritischen Systemen — der Prüfpfad darf niemals unterbrochen werden
- **Entfernung von Authentifizierungsanforderungen** — kein anonymer Zugriff auf irgendein System
- **Entschlüsselung von Daten im Ruhezustand** ohne Neuverschlüsselung — Daten müssen geschützt bleiben
- **Deaktivierung von Firewalls oder IDS/IPS** an kritischen Netzwerkgrenzen
- **Teilen privilegierter Anmeldedaten** ohne individuelle Rechenschaftspflicht — jede Massnahme muss einer Person zugeordnet werden können
- **Umgehung des Change-Managements** für Produktionssysteme ohne Befolgung des Notfall-Änderungsverfahrens (mit obligatorischer Post-Implementierungsüberprüfung innerhalb von 5 Werktagen)

### Notfall-Change-Management bei Störungen

**Standardregel**: Alle Produktionsänderungen erfordern eine Change-Management-Genehmigung gemäss der Change-Management-Richtlinie.

**Notfall-Änderungsausnahme**: Während der Sicherheitslage **Eingeschränkt** oder **Notfall** können Notfalländerungen mit abgekürzter Genehmigung implementiert werden, vorbehaltlich folgender Anforderungen.

**Notfall-Änderungskriterien** (alle müssen erfüllt sein):

1. Änderung ist notwendig, um den kritischen Geschäftsbetrieb wiederherzustellen oder einen aktiven Sicherheitsvorfall zu mindern.
2. Eine Verzögerung bis zur Standardgenehmigung würde erheblichen Schaden verursachen.
3. Änderung wird verbal vom ITL oder ISB (oder designiertem Stellvertreter) genehmigt.
4. Änderung wird sofort in [Change-Management-System / Incident-Ticket] protokolliert.

**Notfall-Änderungsprozess**:

1. **Mündliche Genehmigung**: Änderungsanforderer kontaktiert ITL/ISB über Krisen-Kommunikationsplattform oder Telefon; beschreibt Änderung, Begründung und Rollback-Plan.
2. **Genehmigung**: ITL oder ISB erteilt mündliche Genehmigung; Genehmigung mit Zeitstempel und Name des Genehmigenden protokolliert.
3. **Implementierung**: Änderung mit verbesserter Überwachung implementiert.
4. **Dokumentation**: Innerhalb von 4 Stunden nach Implementierung — Änderungsticket im [Change-Management-System] erstellt mit Details: Was geändert wurde, warum, wer genehmigt hat, Rollback-Plan, tatsächliches Ergebnis.
5. **Post-Implementierungsüberprüfung**: Innerhalb von 5 Werktagen — Änderungsüberprüfungstreffen (ITL, ISB, Änderungsimplementierer, betroffener Systemeigentümer). Bestimmen, ob die Änderung beibehalten, zurückgerollt oder verfeinert werden soll. Erkenntnisse und alle erforderlichen Richtlinien-/Verfahrensaktualisierungen dokumentieren.

**Notfall-Änderungsbeschränkungen**:

- Notfalländerungen dürfen keine Sicherheitskontrollen aus der Liste «Niemals akzeptabel» (Protokollierung, Authentifizierung, Verschlüsselung, Firewalls, Change-Management selbst) deaktivieren.
- Notfalländerungen, die Sicherheitskontrollen umgehen, erfordern speziell die ISB-Genehmigung (nicht nur ITL).
- Notfalländerungen, die das Risiko erhöhen (z. B. Firewall-Regeln öffnen, Authentifizierungsanforderungen reduzieren), erfordern Ausgleichskontrollen, die vor der Implementierung dokumentiert werden.

**Querverweis**: Vollständiges Notfall-Änderungsverfahren in der Change-Management-Richtlinie dokumentiert.

---

## Gestufte Sicherheitslage

Die Organisation sollte auf einer von fünf definierten Sicherheitslage-Stufen betrieben werden. Die aktuelle Sicherheitslage-Stufe bestimmt, welche Kontrollen vollständig aktiv sind, welche eingeschränkt werden können und welche zusätzlichen Massnahmen erforderlich sind.

### Lage-Stufen

| Stufe | Störungszustand | Sicherheitslage | Beispielauslöser |
|-------|-----------------|-----------------|------------------|
| **Normal** | Keine Störung | Vollständige Sicherheitskontrollen betriebsbereit | Täglicher Betrieb |
| **Erhöht** | Kleine Störung | Erweiterte Überwachung, beschleunigtes Patching | Einzelner Systemausfall, kleines Sicherheitsereignis, Wetterwarnung |
| **Eingeschränkt** | Moderate Störung | Kernkontrollen aufrechterhalten, nicht-kritische Kontrollen gemäss Eingeschränkter-Betrieb-Tabelle verschoben | Rechenzentrum-Failover, regionale Störung, erheblicher Cyber-Vorfall |
| **Notfall** | Schwere Störung | Nur Mindest-Baseline, Überlebensmodus | Katastrophe an mehreren Standorten, grosser Ransomware-Angriff, Pandemie-Lockdown |
| **Wiederherstellung** | Rückkehr zur Normalität | Schrittweise Wiederherstellung mit Sicherheitsvalidierung in jeder Phase | Post-Katastrophen-Wiederherstellung, Systemwiederaufbau |

### Übergangsautorität

Übergänge zwischen Lage-Stufen sollten formal autorisiert werden. Mündliche Autorisierung ist in dringenden Situationen zulässig, gefolgt von schriftlicher Bestätigung innerhalb von 4 Stunden.

| Übergang | Erforderliche Autorität | Dokumentation |
|----------|------------------------|---------------|
| Normal zu Erhöht | ISB oder IT-Sicherheitsmanager | Incident-Ticket oder Benachrichtigungs-E-Mail |
| Erhöht zu Eingeschränkt | ISB + ITL (gemeinsam) | Formelle Benachrichtigung der Geschäftsleitung |
| Eingeschränkt zu Notfall | Geschäftsleitung (GF oder Delegierter) | Notfall-Erklärungsdokument |
| Jede Stufe zu Wiederherstellung | ISB | Phasenübergangsaufzeichnung |
| Wiederherstellung zu Normal | ISB (bestätigt von der Geschäftsleitung) | Phasenabschluss-Checkliste und Sicherheitsvalidierungs-Abzeichnung |

Jeder Übergang sollte aufgezeichnet werden mit: Datum/Uhrzeit, autorisierende Person, Begründung, aktueller Zustand, Zielzustand und betroffene Kontrollen.

### Kommunikation der Sicherheitslage-Stufe

Alle Mitarbeitenden sollten über die aktuelle Sicherheitslage-Stufe und die damit verbundenen Anforderungen informiert werden.

**Kommunikationskanäle**:

| Kanal | Nachrichtenformat | Zielgruppe |
|-------|-------------------|------------|
| **E-Mail** | Formelle Ankündigung der Lage-Stufe vom ISB oder GF | Alle Mitarbeitenden |
| **Intranet-Banner** | Sichtbares Banner oben auf der Intranet-Homepage: «AKTUELLE SICHERHEITSLAGE: [STUFE] — [Kurzbeschreibung]» | Alle Mitarbeitenden (beim Zugriff auf das Intranet) |
| **Kollaborationsplattform** (z. B. Slack/Teams) | Angeheftete Nachricht in #allgemein oder #sicherheit | Alle Mitarbeitenden |
| **Krisenmanagement-Team** | Direkte Benachrichtigung über Krisen-Kommunikationsplattform | Krisenteam, Sicherheitsteam, Management |

**Intranet-Banner-Konvention**:

| Lage | Bannerfarbe | Text |
|------|-------------|------|
| **Normal** | Grün | «SICHERHEITSLAGE: NORMAL — Alle Systeme betriebsbereit» |
| **Erhöht** | Gelb | «SICHERHEITSLAGE: ERHÖHT — Kleine Störung; erweiterte Überwachung aktiv» |
| **Eingeschränkt** | Orange | «SICHERHEITSLAGE: EINGESCHRÄNKT — Moderate Störung; Kernkontrollen aktiv; aktualisierte Verfahren befolgen» |
| **Notfall** | Rot | «SICHERHEITSLAGE: NOTFALL — Schwere Störung; nur Mindest-Baseline; auf weitere Anweisungen warten» |
| **Wiederherstellung** | Blau | «SICHERHEITSLAGE: WIEDERHERSTELLUNG — Rückkehr zur Normalität; Sicherheitskontrollen vor Wiederaufnahme des Standardbetriebs validieren» |

**Kommunikationstiming**:

- Sicherheitslage-Stufenübergänge: Sofortige Kommunikation (innerhalb von 1 Stunde nach Autorisierung).
- Statusaktualisierungen bei längeren Störungen: Täglich (mindestens) oder häufiger, wenn sich die Situation weiterentwickelt.
- Rückkehr zur Normalität: Formelle «Entwarnung» nach Abzeichnung der Post-Störungs-Validierung.

Die Kommunikationszustellung sollte verifiziert werden (E-Mail gesendet, Intranet-Banner aktiv, Kollaborationsplattform-Nachricht gepostet). Nichterhalt löst Eskalation zu alternativen Kommunikationsmethoden aus.

---

## BC/DR-Plan-Sicherheitsanforderungen

Alle Business-Continuity- und Disaster-Recovery-Pläne sollten Sicherheitsanforderungen enthalten, die vom ISB überprüft und genehmigt wurden. Sicherheit ist kein nachträglicher Gedanke bei der Kontinuitätsplanung — sie ist eine Designanforderung.

### Sicherheitsüberlegungen in BC/DR-Plänen

BC/DR-Pläne sollten die folgenden vier Bereiche adressieren:

**1. Zugangskontrolle während der Wiederherstellung**

- Wer hat Zugriff auf Recovery-Systeme und -daten (benannte Rollen, kein Pauschalzugriff).
- Wie der Zugriff authentifiziert wird, wenn normale Identitätssysteme nicht verfügbar sind.
- Wie temporärer Zugriff widerrufen wird, wenn die Wiederherstellung abgeschlossen ist.
- Kontrollen für Notfall-Zugriffskonten (siehe Break-Glass-Zugang unten).

**2. Datenschutz während der Wiederherstellung**

- Verschlüsselungsanforderungen für Daten bei der Übertragung zum Recovery-Standort.
- Verschlüsselungsanforderungen für Recovery-Medien (physisch und digital).
- Beweiskettenverfahren für physische Datenbewegung.
- Durchsetzung der Datenklassifizierung in der Recovery-Umgebung.

**3. Kommunikationssicherheit**

- Sichere Kommunikationskanäle für das Krisenmanagement-Team (siehe Krisen-Kommunikationsplattform unten).
- Alternative Kommunikationskanäle, wenn primäre Systeme kompromittiert sind (z. B. Out-of-Band-Telefon, vorab vereinbarte Nachrichtengruppen).
- Authentifizierung von Krisenkommunikation zur Verhinderung von Social Engineering bei Verwirrung.
- Informationsaustauschgrenzen — was extern geteilt werden darf und wer externe Kommunikation genehmigt.

### Krisen-Kommunikationsplattform

**Primärplattform**: [Tool angeben — z. B. Microsoft Teams (mit E2EE), Signal, Wickr, verschlüsseltes Zoom, WhatsApp Business]

**Konfiguration**:

- Ende-zu-Ende-Verschlüsselung aktiviert (verifizieren, dass E2EE aktiv ist).
- Vorkonfigurierter Krisenmanagement-Gruppen-Chat mit allen autorisierten Mitarbeitenden.
- Gruppen-Chat-Name: **«Krisenmanagement-Team — Sicher»**.
- Zugriff auf vorab genehmigte Mitarbeitende beschränkt (keine Ad-hoc-Ergänzungen ohne ISB-Genehmigung während der Krise).

**Backup-Plattform** (wenn primäre nicht verfügbar): [Alternative angeben — z. B. verschlüsselte E-Mail (PGP/S/MIME), vorab vereinbarte Telefonbrücke, Out-of-Band-SMS-Gruppe]

**Authentifizierung während der Krise**:

- Alle Krisen-Kommunikationsteilnehmer sollten sich mit ihren Organisationsanmeldedaten authentifizieren.
- Während der Notfall-Lage, wenn MFA-Infrastruktur nicht verfügbar ist, sollten Teilnehmer vorab gemeinsam genutzte Authentifizierungsphrasen verwenden, um Identität zu verifizieren (monatlich rotierend, verteilt über Offline-Kontaktliste).

**Out-of-Band-Verifizierung**: Für kritische Entscheidungen (z. B. Genehmigung der Notfall-Lage, Break-Glass-Aktivierung) ist eine mündliche Bestätigung per Telefon erforderlich, um Impersonationsangriffe zu verhindern. Telefonnummern werden vierteljährlich verifiziert und in der Offline-Kontaktliste aktualisiert.

**Testen**: Krisen-Kommunikationsplattform vierteljährlich getestet. Tests umfassen Konnektivitätsverifizierung, Verschlüsselungsstatusüberprüfung, Teilnehmerauthentifizierung und Nachrichtenzustellungsbestätigung. Testdokumentation 3 Jahre aufbewahrt.

**4. Drittpartei-Sicherheit**

- Lieferantenzugriffskontrollen bei Recovery-Operationen.
- Auftragnehmer-Sicherheitsanforderungen bei Notfalloperationen.
- Cloud-Service-Sicherheitsverifizierung beim Failover.
- Lieferkettensicherheit für Notfallbeschaffung.

### BC/DR-Plan-Sicherheitsüberprüfung

- Der ISB oder designierter Stellvertreter sollte die Sicherheitsabschnitte aller BC/DR-Pläne überprüfen und genehmigen, bevor die Pläne genehmigt werden.
- Sicherheitsüberprüfung sollte nach jeder Aktualisierung eines BC/DR-Plans erfolgen.
- Mindestens ein sicherheitsspezifisches Testszenario sollte im jährlichen BC/DR-Testen enthalten sein.
- Sicherheitsabweichungen, die beim Testen beobachtet werden, sollten dokumentiert und innerhalb von 30 Tagen behoben werden.

---

## Recovery-Standort-Sicherheit

Recovery-Standorte — ob Hot-, Warm-, Cold-Standby oder Cloud-basierte Disaster-Recovery-Umgebungen — sollten Sicherheitskontrollen aufrechterhalten, die dem primären Standort gleichwertig sind. Eine Recovery-Umgebung mit schwächerer Sicherheit als der primäre Standort schafft eine ausnutzbare Lücke.

| Kontrolle | Anforderung |
|-----------|-------------|
| **Physische Sicherheit** | Dem primären Standort für das behandelte Datenkritikalitätsniveau gleichwertig |
| **Netzwerksicherheit** | Gleiche Segmentierungsregeln, Firewall-Richtlinien und Überwachung |
| **Zugangskontrolle** | Gleiches Authentifizierungs- und Autorisierungsmodell; keine schwächeren Zugriffspfade |
| **Datenschutz** | Gleiche Verschlüsselungsstandards (im Ruhezustand und bei der Übertragung) und Klassifizierungsdurchsetzung |
| **Protokollierung** | Gleichwertige Protokollierungsfähigkeit; Protokolle sollten dasselbe [SIEM] oder Überwachungssystem speisen |
| **Härtung** | Gleiche Konfigurationsbaselines auf Recovery-Infrastruktur angewendet |

### Recovery-Standort-Definition und -Konfiguration

**Primärer Recovery-Standort**: [Typ und Standort angeben]

| Option | Beschreibung | Konfiguration |
|--------|--------------|---------------|
| **Cloud-Disaster-Recovery** (häufigste für KMU) | [z. B. AWS, Azure, Google Cloud] in [z. B. eu-central-1 (Frankfurt), West Europe (Niederlande)] | Hot-Standby (immer verfügbar), Warm-Standby (Hochfahren innerhalb von X Stunden) oder Cold-Standby (manuelle Bereitstellung). Failover-Auslöser: automatisch (Health-Check-Fehler) oder manuell (erklärt von ITL + ISB) |
| **Colocation / sekundäres Rechenzentrum** | [Einrichtungsname, Stadt] | Dedizierte WAN-Verbindung oder verschlüsseltes VPN zum primären Standort |
| **Work-from-Anywhere** (Pandemie/Büro-Nichtverfügbarkeit) | VPN-Zugriff, MFA, Endpunktverschlüsselung, Leitfaden für sicheres Heimnetzwerk | Nur administrative/wissensbasierte Mitarbeiterfunktionen; abhängig von Cloud/Colocation für Infrastruktur-Recovery |

**Aktuelle Konfiguration**: [Angeben, welche Option(en) bereitgestellt sind]

**Sicherheitsäquivalenz-Verifizierung**:

| Sicherheitskontrolle | Verifizierungsmethode |
|----------------------|-----------------------|
| **Physische Sicherheit** | Jährliche Überprüfung der Anbieter-Prüfberichte (SOC 2 Typ II oder ISO 27001); Vor-Ort-Inspektion bei physischer Einrichtung |
| **Netzwerksegmentierung** | Recovery-Standort-Konfiguration verglichen mit primärer Standort-Baseline |
| **Zugangskontrolle** | Authentifizierung (einschliesslich MFA) an Recovery-Systemen testen |
| **Verschlüsselung** | Konfigurationsscan; Zertifikatsverifizierung |
| **Protokollierung** | Protokollweiterleitung an [SIEM] während DR-Test verifizieren |
| **Backup-Schutz** | Wiederherstellungstest aus Recovery-Standort-Backups |

**Failover-Testen**: Jährlicher Failover-Test zum Recovery-Standort. Sicherheitsvalidierung während des Tests sollte bestätigen, dass Authentifizierung funktioniert (einschliesslich MFA), Netzwerksegmentierung durchgesetzt wird, Protokollierung aktiv ist und an [SIEM] weiterleitet, Verschlüsselung verifiziert ist und Zugriffskontrollen dem primären Standort entsprechen. Sicherheitsbefunde dokumentiert und innerhalb von 30 Tagen behoben.

Recovery-Standort-Sicherheit sollte verifiziert werden:

- Bei der ersten Bereitstellung, bevor der Standort als betriebsbereit erklärt wird.
- Jährlich als Teil des BC/DR-Testprogramms.
- Nach wesentlichen Änderungen der Recovery-Infrastruktur.

---

## Notfall-Zugriffsverfahren

### Break-Glass-Zugang

Die Organisation sollte vorkonfigurierte Notfall-Zugriffskonten («Break-Glass-Konten») für Szenarien pflegen, in denen normale Authentifizierungs- oder Zugriffssysteme nicht verfügbar sind.

**Break-Glass-Konto-Anforderungen**:

| Anforderung | Spezifikation |
|-------------|---------------|
| **Kontostatus** | Ruhend (deaktiviert) bis Notfall erklärt wird |
| **Aktivierungsautorität** | ISB, ITL oder GF (dokumentierte Autoritätskette mit designierten Stellvertretern) |
| **Authentifizierung** | Starke Authentifizierung — Anmeldedaten gemäss der unten stehenden Break-Glass-Anmeldedaten-Speicher-Spezifikation sicher gespeichert |
| **Umfang** | Vordefiniert, auf wiederherstellungsessenzielle Systeme beschränkt |
| **Protokollierung** | Alle Aktionen mit manipulationssicherem Prüfpfad protokolliert |
| **Dauer** | Zeitlich begrenzt — Standard 24 Stunden, verlängerbar mit erneuter Genehmigung |
| **Deaktivierung** | Formelle Deaktivierung mit Anmeldedaten-Rotation und vollständiger Aktivitätsüberprüfung |

### Break-Glass-Aktivierungsprozess

1. **Notfall erklärt** durch eine autorisierte Autorität (siehe Übergangautoritäts-Tabelle).
2. **Aktivierungsanfrage dokumentiert** — auch wenn zunächst mündlich, schriftliche Aufzeichnung innerhalb von 4 Stunden.
3. **Zwei-Personen-Aktivierung** — bei kritischen Systemen erfordert Break-Glass mindestens zwei autorisierte Mitarbeitende (Vier-Augen-Prinzip).
4. **ISB und Sicherheitsteam** sofort bei Aktivierung benachrichtigt.
5. **Erweiterte Überwachung aktiviert** — alle Break-Glass-Kontoaktivitäten wo möglich in Echtzeit überwacht.
6. **Zeitlimit angewendet** — 24 Stunden Standard; Verlängerung erfordert explizite erneute Genehmigung mit Begründung.
7. **Deaktivierung und Überprüfung** — nach Notfallauflösung: Konto deaktivieren, Anmeldedaten rotieren, alle durchgeführten Aktionen überprüfen, Befunde dokumentieren.

### Break-Glass-Anmeldedaten-Speicherung und -Zugang

**Speichermethode**: [Gewählte Methode der Organisation aus unten angeben]

**Option 1 — Physischer Safe** (primäre Methode für Hochsicherheitsumgebungen):

- **Standort**: [Gebäudename], [Etage], [Raumnummer] — physisch gesicherter Raum mit eingeschränktem Zugang.
- **Zugangsberechtigung**: GF, ISB, ITL (jeder hat Safe-Kombination oder Schlüssel; zwei für den Zugang erforderlich).
- **Inhalt**: Versiegelte manipulationssichere Umschläge mit Break-Glass-Kontonamen und Initial-Passwörtern, Recovery-Site-VPN-Anmeldedaten, Root-Passwörtern für kritische Systeme (Stufe 0) und Verschlüsselungs-Wiederherstellungsschlüsseln.
- **Umschlagintegrität**: Manipulationssichere Siegel; Umschlagöffnung löst obligatorische Anmeldedaten-Rotation aus.
- **Verifizierung**: Vierteljährliche Verifizierung, dass Safe zugänglich ist und Umschläge intakt sind (nur externe Inspektion; kein Öffnen).

**Option 2 — Passwort-Manager-Notfall-Vault**:

- **Tool**: [z. B. 1Password Emergency Kit, Bitwarden Emergency Access, LastPass Emergency Access].
- **Konfiguration**: Notfall-Vault getrennt vom Standard-Unternehmens-Vault.
- **Zugang**: Notfallzugang designiertem Personal gewährt (GF, ISB, ITL) mit zeitverzögertem Zugang (z. B. 12-Stunden-Wartezeit vor Gewähren des Zugangs).
- **MFA-Bypass**: Notfall-Vault mit offline gespeicherten Wiederherstellungs-Codes zugänglich (gedruckte Karten in versiegelten Umschlägen, gespeichert gemäss Option 1).
- **Testen**: Vierteljährlicher Test des Notfallzugang-Workflows (Zeitverzögerungs-Verifizierung, Zugangsbestätigung, Anmeldedaten-Abruf).

**Option 3 — Split-Knowledge / Secret Sharing** (erweitert):

- **Methode**: Shamir's Secret Sharing oder ähnliche kryptografische Aufteilung.
- **Konfiguration**: Break-Glass-Passwort in 3 Anteile aufgeteilt; beliebige 2 von 3 zur Rekonstruktion erforderlich.
- **Anteilshalter**: GF (Anteil 1), ISB (Anteil 2), ITL (Anteil 3).
- **Speicherung**: Jeder Anteilshalter speichert seinen Anteil in einem persönlichen Safe oder versiegelten Umschlag (Heimtresor, Bankschliessfach).
- **Testen**: Jährlicher Test des Rekonstruktionsprozesses.

**Aktuelle Methode**: [Angeben, welche Option(en) die Organisation verwendet]

**Backup-Zugang** (wenn primäre Methode ausfällt): Wenn Safe nicht zugänglich (Gebäude zerstört) → Passwort-Manager-Notfall-Vault (Cloud-zugänglich). Wenn Passwort-Manager nicht zugänglich (Dienstausfall) → Physischer Safe oder Split-Knowledge.

### Break-Glass-Testen

Break-Glass-Konten und -Verfahren sollten mindestens jährlich getestet werden, um zu verifizieren:

- Anmeldedaten sind zugänglich und funktional.
- Aktivierungsprozess ist allen autorisierten Mitarbeitenden bekannt.
- Protokollierung erfasst alle durchgeführten Aktionen.
- Deaktivierungsprozess funktioniert korrekt.

Testergebnisse sollten dokumentiert werden. Fehlgeschlagene Tests lösen sofortige Behebung aus.

---

## Personalverfügbarkeit

Die Organisation sollte sicherstellen, dass Personal mit Sicherheitsverantwortlichkeiten bei Störungsereignissen verfügbar ist. Störungen treten häufig ausserhalb der Geschäftszeiten auf und können den normalen Zugang zum Arbeitsplatz verhindern.

**Kontinuitätsanforderungen des Sicherheitsteams**:

- Wichtige Sicherheitsrollen sollten designierte Stellvertreter haben, die in einem Nachfolgeplan dokumentiert sind.
- Kontaktinformationen für Sicherheitspersonal sollten offline zugänglich sein — gedruckte Kontaktlisten und/oder verschlüsselte USB — zugänglich, wenn E-Mail, Intranet und andere digitale Systeme nicht verfügbar sind.
- Wo möglich, sollte das Sicherheitspersonal geografisch verteilt sein, um zu vermeiden, dass ein Einzelstandort-Ausfall das gesamte Sicherheitsteam deaktiviert.
- Cross-Training sollte sicherstellen, dass mindestens zwei Personen jede kritische Sicherheitsfunktion ausführen können (Break-Glass-Aktivierung, Protokollüberprüfung, Notfall-Zugriffswiderruf, Sicherheitslagebewertung).
- Bereitschaft sollte für 24/7-Abdeckung eingerichtet werden, wenn die Organisation auf erhöhtem, eingeschränktem oder Notfall-Lageniveau betrieben wird.

### Offline-zugängliche Kontaktliste

**Mehrschichtiger Ansatz für Resilienz**:

**Schicht 1 — Laminierte Karten**:

- Brieftaschengrösse laminierte Karten für alle Krisenmanagement-Team-Mitglieder und Sicherheitspersonal.
- Enthält: Namen, Mobiltelefonnummern, persönliche E-Mail-Adressen (für Out-of-Band-Kontakt), Rolle.
- Vierteljährlich aktualisiert; alte Karten vernichtet (geschreddert). Verteilung: Persönlich übergeben; Mitarbeitende unterzeichnen Empfangsbestätigung.

**Schicht 2 — Verschlüsselter USB-Stick**:

- USB-Stick im Break-Glass-Safe neben den Anmeldedaten gespeichert.
- Enthält: Vollständige Kontaktliste (gesamtes Sicherheitspersonal, erweitertes Krisenteam, Lieferanten-Notrufkontakte).
- Datei verschlüsselt (z. B. VeraCrypt, BitLocker To Go) mit Passwort bekannt bei GF/ISB/ITL.
- Vierteljährlich aktualisiert.

**Schicht 3 — Sicherer Cloud-Speicher** (zugänglich wenn Internet verfügbar):

- Kontaktliste in [sicherem Dokumentenrepository] gespeichert mit Zugang beschränkt auf Krisenmanagement-Team.
- Regelmässig aktualisiert (in Echtzeit bei Personaländerungen).

**Testen**: Vierteljährliche Verifizierung — 3 zufällige Mitarbeitende kontaktiert anhand von Informationen aus laminierten Karten (Telefonnummern auf Funktion prüfen), USB-Stick getestet (Verschlüsselungs-Passwort verifiziert, Datei geöffnet), Cloud-Speicher-Zugang verifiziert. Testergebnisse dokumentiert; Fehlschläge lösen sofortige Aktualisierung aus.

### Sicherheitsteam-Bereitschaftsabdeckung

**Aktivierungsauslöser**: Automatisch aktiviert, wenn die Sicherheitslage zu **Erhöht**, **Eingeschränkt** oder **Notfall** wechselt.

**Abdeckungsmodell**:

| Lage | Abdeckung |
|------|-----------|
| **Normal** | Kein dedizierter Bereitschaftsdienst (nur Unterstützung während der Geschäftszeiten) |
| **Erhöht** | 16×7-Abdeckung (07:00–23:00 MEZ, 7 Tage/Woche) |
| **Eingeschränkt / Notfall** | 24×7-Abdeckung |

**Rotationsplan**:

| Rolle | Abdeckungsverantwortung |
|-------|------------------------|
| **Primärer Bereitschaft** | IT-Sicherheitsanalyst oder IT-Sicherheitsmanager (wöchentlich rotierend) |
| **Backup-Bereitschaft** | ISB oder designiertes Sicherheitsteam-Mitglied |
| **Eskalation** | ISB (24×7 erreichbar während Eingeschränkt/Notfall) |

**Reaktions-SLAs**:

| Schweregrad | Erhöht | Eingeschränkt / Notfall |
|-------------|--------|------------------------|
| **Kritisch** (Break-Glass-Aktivierung, bestätigter Verstoss) | 30 Minuten | 15 Minuten |
| **Hoch** (Sicherheitskontrollausfall, verdächtige Aktivität) | 2 Stunden | 1 Stunde |
| **Mittel** (nicht-kritische Meldung, Hinweis) | 4 Stunden | 2 Stunden |

**Eskalationspfad**: Primärer Bereitschaft → Backup-Bereitschaft (wenn primärer nach 30 Min. für Kritisch, 1 Stunde für Hoch nicht erreichbar) → ISB → Geschäftsleitung.

**Testen**: Monatlicher Bereitschafts-Testanruf während der normalen Geschäftszeiten (Kontaktinformationen und Reaktionszeit verifizieren). Vierteljährlicher Test ausserhalb der Geschäftszeiten (zufällige Zeit; Eskalationspfad auf Funktion prüfen).

---

## Sicherheitsvalidierung nach Störungen

Vor der Rückkehr zur normalen Lage-Stufe sollte die Organisation validieren, dass vollständige Sicherheitskontrollen wiederhergestellt wurden. Der Übergang von der Wiederherstellung zur Normalität ist erst abgeschlossen, wenn die Sicherheitsvalidierung vom ISB abgezeichnet wurde.

### Vier-Phasen-Validierung

| Phase | Zeitrahmen | Validierungsaktivitäten |
|-------|------------|------------------------|
| **Sofort** | 0–24 Stunden nach Störung | Verifizieren, dass nicht verhandelbare Kontrollen betriebsbereit sind; alle Break-Glass-Konten deaktivieren; Protokolle auf Anomalien während der Störung überprüfen; bestätigen, dass kein unbefugter Zugriff stattgefunden hat |
| **Kurzfristig** | 1–7 Tage | Vollständige Sicherheitskontrollvalidierung; Schwachstellen-Scan aller Stufe-1- und Stufe-2-Systeme; Zugriffsüberprüfung (verifizieren, dass keine Restnotfallberechtigungen vorhanden sind); erste Vorfallsanalyse |
| **Mittelfristig** | 1–4 Wochen | Sicherheitsschulden-Behebung (verschobene Patches anwenden, verschobene Kontrollen wiederherstellen); vollständige Zugriffs-Rezertifizierung; Kontrolltesting zur Verifizierung der Wirksamkeit; BC/DR-Plan-Aktualisierung mit Erkenntnissen |
| **Langfristig** | 1–3 Monate | Umsetzung der Erkenntnisse; Richtlinien- und Verfahrensaktualisierungen; Schulungsaktualisierungen; Trendanalyse der Sicherheitslage während der Störung |

### Sicherheitsschulden-Verfolgung

Alle während einer Störung genehmigten Sicherheitslockerungen sollten im Sicherheitsschulden-Register verfolgt werden, bis sie vollständig behoben sind.

**System**: [Tool angeben — z. B. GRC-Plattform (Vanta, Drata, ServiceNow GRC), Jira, Asana, Excel-Register an sicherem Ort gespeichert]

**Eigentümerschaft**: ISB führt Register; zugewiesene Eigentümer beheben individuelle Schuldenelemente.

**Sicherheitsschulden-Register-Format**:

| Feld | Beschreibung |
|------|--------------|
| **Schulden-ID** | Eindeutige Kennung (z. B. DEBT-2025-001) |
| **Gelockerte Kontrolle** | Welche Sicherheitskontrolle wurde eingeschränkt oder verschoben |
| **Geschäftliche Begründung** | Warum war Lockerung notwendig? (verbunden mit spezifischem Störungsereignis) |
| **Ausgleichskontrolle** | Implementierte alternative Sicherheitsmassnahme |
| **Eröffnungsdatum** | Wann die Lockerung genehmigt wurde |
| **Sicherheitslage bei Eröffnung** | Erhöht / Eingeschränkt / Notfall |
| **Genehmiger** | ISB oder autorisierter Stellvertreter |
| **Eigentümer** | Person, die für die Behebung verantwortlich ist |
| **Zielschlussdatum** | Wann vollständige Kontrolle wiederhergestellt sein muss |
| **Aktueller Status** | Offen / In Bearbeitung / Geschlossen |
| **Fortschrittsnotizen** | Aktualisierungen zu Behebungsmassnahmen |
| **Schlussdatum** | Wann die Kontrolle vollständig wiederhergestellt wurde |
| **Schlussverifizierung** | ISB- oder Sicherheitsteam-Verifizierung der Kontrollwiederherstellung |

**Schulden-Lebenszyklus**:

1. **Eröffnung**: Kontrolllockerung während der Störung genehmigt → sofortiger Eintrag in das Register.
2. **Verfolgung**: Wöchentliche Überprüfung bei aktiver Störung; zweiwöchentlich bei Wiederherstellungs-Lage.
3. **Eskalation**: Gemäss unten stehenden Schwellenwerten.
4. **Schliessung**: Kontrolle vollständig wiederhergestellt → Sicherheitsteam verifiziert → Schuld als geschlossen markiert.

**Integration mit der Sicherheitslage**: Der Übergang von Wiederherstellung zu Normal erfordert ein leeres Sicherheitsschulden-Register oder eine dokumentierte Genehmigung der Geschäftsleitung für verbleibende Elemente.

**Berichterstattung**: Sicherheitsschulden-Status in jeder ISMS-Managementüberprüfung während und nach der Störung gemeldet. Metriken: offene Schulden gesamt, Durchschnittsalter, überfällige Schulden, Schliessungsrate.

**Eskalationsschwellenwerte**:

- Sicherheitsschuld älter als **30 Tage** sollte an den ISB mit Behebungsplan und überarbeitetem Zieldatum eskaliert werden.
- Sicherheitsschuld älter als **90 Tage** sollte an die Geschäftsleitung zur Entscheidung eskaliert werden: entweder beschleunigte Behebung mit zusätzlichen Ressourcen genehmigen oder das Restrisiko mit dokumentierter Risikoakzeptanz formal akzeptieren.
- Sicherheitsschuld, die nicht behoben werden kann, sollte in einen permanenten Risikoregister-Eintrag mit Ausgleichskontrollen und jährlicher Überprüfung umgewandelt werden.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten zur Informationssicherheit bei Störungen |
|-------|---------------------------------------------------------------|
| **GF / Geschäftsleitung** | Sicherheitslage-Stufen genehmigen; Notfallmodus autorisieren; Ressourcen für Sicherheit während der Wiederherstellung bereitstellen; Risikoakzeptanzentscheidungen für Sicherheitsschuld über 90 Tage treffen |
| **ISB** | Richtlinieneigentümer; Sicherheitsanforderungen für BC/DR-Pläne definieren; Sicherheitslage-Übergänge genehmigen; Break-Glass-Aktivierung autorisieren; Sicherheitsvalidierung nach Störungen verantworten; Eskalationsstelle für Sicherheitsschuld |
| **BC/DR-Koordinator** | Sicherheitsanforderungen in BC/DR-Pläne integrieren; Koordination mit ISB bei Plan-Sicherheitsüberprüfung; Sicherheitsszenarien in BC/DR-Testen einbeziehen |
| **ITL** | Sicherstellen, dass IT-Recovery mit Sicherheitsanforderungen übereinstimmt; Übergang Erhöht-zu-Eingeschränkt gemeinsam autorisieren; Break-Glass-Aktivierung autorisieren |
| **Sicherheitsteam / IT-Sicherheit** | Sicherheit während der Störung überwachen; Notfallverfahren aktivieren und deaktivieren; Recovery-Standort-Sicherheit validieren; Schwachstellen-Scans und Zugriffsüberprüfungen nach Störungen durchführen |
| **Krisenmanagement-Team** | Sicherheitsüberlegungen in alle Krisenentscheidungen einbeziehen; Kommunikation mit ISB während der gesamten Störung aufrechterhalten (siehe Zusammensetzung unten) |
| **IT-Betrieb** | Sicherheitskontrollen in Recovery-Umgebungen implementieren; Protokollierung während der Wiederherstellung aufrechterhalten; Sicherheitsanomalien während der Wiederherstellung melden |
| **Alle Mitarbeitenden** | Sicherheitsverfahren bei Störungen befolgen; Sicherheitsbedenken über etablierte Kanäle melden; Sicherheitskontrollen nicht ohne Autorisierung umgehen |

### Zusammensetzung des Krisenmanagement-Teams

**Zweck**: Koordination der organisatorischen Reaktion auf grössere Störungen, die den Geschäftsbetrieb und die Informationssicherheit betreffen.

**Aktivierungsauslöser**: Sicherheitslage-Übergang zu **Eingeschränkt** oder **Notfall**; Vorfallsschweregrad P0 (Kritisch) oder P1 (Hoch) mit unternehmensweiten Auswirkungen; oder Erklärung durch GF, ITL oder ISB, dass Krisenmanagement erforderlich ist.

**Kernteam-Mitglieder**:

| Rolle | Verantwortlichkeiten während der Krise |
|-------|----------------------------------------|
| **GF** (Team-Leiter) | Gesamte Krisen-Führung; externe Kommunikation; strategische Entscheidungen; Notfall-Lage autorisieren |
| **ITL** | IT-Recovery-Koordination; Ressourcenallokation; technologische Entscheidungsautorität |
| **ISB** | Informationssicherheitskontinuität; Sicherheitslage-Management; Break-Glass-Autorisierung; Validierung nach Störungen |
| **FL** | Bewertung der finanziellen Auswirkungen; Budget-Autorisierung für Recovery; Versicherungskoordination |
| **HR-Direktor** | Personalssicherheit; Kommunikation an Mitarbeitende; Arbeitskräftekontinuität |
| **Rechtsbeistand** | Regulatorische Benachrichtigung; Haftungsmanagement; Vertragsfragen; rechtliche Verpflichtungen bei Datenschutzverletzungen |
| **Kommunikation / PR** (falls vorhanden) | Externe Kommunikation; Medienverwaltung; Kundenbenachrichtigung |

**Erweitertes Team** (nach Bedarf aktiviert): BC/DR-Koordinator, IT-Betriebsmanager, Sicherheitsteam-Leiter, Facilties-Manager, Schlüssellieferanten.

**Entscheidungsautorität**:

| Entscheidungstyp | Autorität |
|-----------------|-----------|
| Sicherheitslage-Stufenübergänge | GF + ITL + ISB-Zustimmung erforderlich |
| Risikoakzeptanzentscheidungen, externe Kommunikation, Ressourcenallokation über Budget | GF letzte Autorität |
| Sicherheitskontrolllockerungen, Break-Glass-Aktivierung, Sicherheitsschulden-Genehmigung | ISB letzte Autorität |
| Technologie-Recovery-Prioritäten, Systemwiederherstellungssequenzierung | ITL letzte Autorität |

**Besprechungsrhythmus während der Krise**:

| Lage | Häufigkeit |
|------|-----------|
| **Eingeschränkt** | Täglicher Krisenmanagement-Team-Anruf (30 Minuten) bis Wiederherstellung beginnt |
| **Notfall** | Zweimal täglich (morgens und abends) plus Ad-hoc nach Bedarf |
| **Wiederherstellung** | Alle 2–3 Tage bis zur Rückkehr zur Normalität |

Besprechungsprotokoll dokumentiert (auch wenn kurz) für Post-Incident-Überprüfung. Massnahmen mit Eigentümer und Zieldatum verfolgt.

**Nach der Krise**: Formelle Erkenntnissitzung innerhalb von 30 Tagen nach Rückkehr zur Normal-Lage. Erkenntnisse informieren Richtlinienaktualisierungen, BC/DR-Plan-Aktualisierungen und Schulungen.

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| Nr. | Nachweis | Eigentümer | Häufigkeit |
|-----|----------|------------|------------|
| 1 | **BC/DR-Pläne mit ISB-Sicherheitsgenehmigung** (unterzeichnete Überprüfung, die bestätigt, dass Sicherheitsabschnitte angemessen sind) | BC/DR-Koordinator / ISB | *Jährliche Überprüfung; nach Tests und Vorfällen aktualisiert; aktuelle + 2 frühere Versionen aufbewahrt* |
| 2 | **Mindest-Sicherheits-Baseline-Dokumentation** (Definition nicht verhandelbarer Kontrollen und Eingeschränkter-Betrieb-Schwellenwerte) | ISB | *Jährliche Überprüfung; bei Richtlinienänderung aktualisiert; 3 Jahre aufbewahrt* |
| 3 | **Break-Glass-Konto-Inventar** (Kontoliste, Umfang, Anmeldedaten-Speicherort, Aktivierungsautorität) | Sicherheitsteam | *Laufend geführt; vierteljährlich überprüft; 3 Jahre aufbewahrt* |
| 4 | **Break-Glass-Testergebnisse** (jährlicher Test mit Dokumentation der Anmeldedaten-Zugänglichkeit, Aktivierungsprozess, Protokollierung, Deaktivierung) | Sicherheitsteam | *Jährlich mindestens; 3 Jahre aufbewahrt* |
| 5 | **Sicherheitslage-Übergangsaufzeichnungen** (Datum, Autorität, Begründung, betroffene Kontrollen) — falls Störungen aufgetreten sind | ISB | *Pro Ereignis; 5 Jahre aufbewahrt* |
| 6 | **Sicherheitsschulden-Register** (alle Lockerungen während der Störung mit Eigentümer, Ausgleichskontrollen, Zieldatum, Schliessung) | ISB | *Pro Ereignis; monatlich bei aktiver Schuld überprüft; 3 Jahre aufbewahrt* |
| 7 | **Sicherheitsvalidierungsberichte nach Störungen** (Vier-Phasen-Checklisten-Abschluss mit Abzeichnung) — falls Störungen aufgetreten sind | ISB / Sicherheitsteam | *Pro Störungsereignis; 5 Jahre aufbewahrt* |
| 8 | **Recovery-Standort-Sicherheitsbewertung** (jährliche Verifizierung der Sicherheitsäquivalenz mit dem primären Standort) | Sicherheitsteam | *Jährlich; 3 Jahre aufbewahrt* |
| 9 | **Sicherheitspersonal-Kontaktliste und Nachfolgeplan** (offline zugänglich, vierteljährlich getestet) | ISB | *Vierteljährlich überprüft; bei Änderungen aktualisiert* |
| 10 | **BC/DR-Testaufzeichnungen mit sicherheitsspezifischen Szenarien** (Testumfang, Sicherheitsbefunde, Behebungsmassnahmen) | BC/DR-Koordinator / Sicherheitsteam | *Jährlich mindestens; 3 Jahre aufbewahrt* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team sollte die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, einschliesslich, aber nicht beschränkt auf, BC/DR-Plan-Sicherheitsüberprüfungen, Break-Glass-Konto-Tests, Sicherheitslage-Übergangsaufzeichnungen, Sicherheitsschulden-Register-Status, Recovery-Standort-Bewertungen, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

**Governance-Metriken** (mindestens jährlich an die Geschäftsleitung gemeldet):

| Metrik | Ziel |
|--------|------|
| BC/DR-Pläne mit aktueller ISB-Sicherheitsgenehmigung | 100 % |
| Planmässig abgeschlossene Break-Glass-Konto-Tests | 100 % |
| Sicherheitsvorfälle während Störungsereignissen | Trendverfolgung (Ziel: abnehmend) |
| Sicherheitsschulden-Elemente offen über 90 Tage | 0 |
| Recovery-Standort-Sicherheitsbewertungen ohne kritische/hohe Befunde | 100 % |

## Ausnahmen

Jede Ausnahme von dieser Richtlinie sollte vom ISB im Voraus genehmigt und aufgezeichnet werden, mit dokumentierter Risikoakzeptanz, Ausgleichskontrollen und einem definierten Überprüfungsdatum (maximale Dauer der Störung + 7 Tage für Recovery-Ausnahmen; maximal 12 Monate für stehende Ausnahmen). Ausnahmen sollten dem Management-Review-Team gemeldet werden.

Ausnahmen sind nicht für nicht verhandelbare Kontrollen (Zugangskontrolle, Datenverschlüsselung, Protokollierung, Netzwerksegmentierung, Backup-Schutz) zulässig. Ausnahmen, die die Prüfpfad-Fähigkeit eliminieren, sind nicht zulässig.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterworfen werden, bis hin zur Kündigung des Arbeitsverhältnisses.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollten Erkenntnisse aus tatsächlichen Störungen, BC/DR-Testergebnisse, Änderungen der Bedrohungslandschaft, regulatorische Aktualisierungen, Audit-Befunde und neue Best Practices für Sicherheit unter ungünstigen Bedingungen berücksichtigen.

---

# Bereiche des ISO-27001-Standards, die abgedeckt werden

Richtlinie zur Informationssicherheit bei Störungen — ISO-27001-Kontrollmapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien für Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.4 Managementverantwortlichkeiten |
| Klausel 6.2 Informationssicherheitsziele | **5.29 Informationssicherheit bei Störungen** |
| Klausel 7.3 Bewusstsein | 5.30 IKT-Bereitschaft für Geschäftskontinuität |
| Klausel 8.1 Operationale Planung und Kontrolle | 5.36 Konformität mit Richtlinien, Regeln und Standards |
| | 6.3 Informationssicherheitsbewusstsein, Ausbildung und Schulung |
| | 6.4 Disziplinarischer Prozess |
| | 8.13 Informations-Backup |
| | 8.14 Redundanz von Informationsverarbeitungseinrichtungen |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizer nDSG (revDSG) | Art. 8 — Angemessene technische und organisatorische Sicherheitsmassnahmen auch bei Störungen aufrechterhalten |
| Schweizer DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung, einschliesslich Fähigkeit zur Sicherstellung laufender Vertraulichkeit, Integrität, Verfügbarkeit und Resilienz von Verarbeitungssystemen und -diensten |
| ISO/IEC 27001:2022 | Annex A Kontrolle 5.29 — Informationssicherheit bei Störungen |
| ISO/IEC 27002:2022 | Abschnitt 5.29 — Implementierungsleitfaden |
| ISO/IEC 22301 | Business-Continuity-Managementsysteme (informativer Verweis) |
| NIST SP 800-34 Rev 1 | Contingency Planning Guide — Drei-Phasen-Ansatz (Benachrichtigung/Aktivierung, Wiederherstellung, Rekonstituierung) (informativer Verweis) |
| CIS Controls v8 | Kontrolle 17 (Incident Response Management), Kontrolle 11 (Data Recovery) |
| DORA (bedingt) | Art. 11 — IKT-Geschäftskontinuitätsmanagement einschliesslich Sicherheitsanforderungen bei Störungen |
| NIS2 (bedingt) | Art. 21 — Massnahmen für Geschäftskontinuität und Krisenmanagement |
| FINMA (bedingt) | Rundschreiben 2023/1 — Operationale Resilienz für regulierte Schweizer Finanzinstitute |

---

<!-- QA_VERIFIED: 2026-03-29 -->
