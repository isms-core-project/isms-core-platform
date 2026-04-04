<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.29-DE:framework:POL:a.5.29 -->
**ISMS-POL-A.5.29 — Informationssicherheit bei Betriebsunterbrechungen**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Informationssicherheit bei Betriebsunterbrechungen |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.29 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Festzulegen] |
| **Version** | 1.0 |
| **Versionsdatum** | [Festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Festzulegen] | ISB | Erstrichtlinie für ISO 27001:2022 Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Inkrafttreten + 12 Monate]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Business-Continuity-Manager
- Integration: IT-Leiter (ITL)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.5.30-8.13-14 (Business-Continuity- & Notfallwiederherstellungs-Framework)
- ISMS-POL-A.5.24-28 (Incident-Management-Lebenszyklus)
- ISMS-POL-A.8.14 (Redundanz von Informationsverarbeitungseinrichtungen)
- ISMS-IMP-A.5.29.1-UG/TG (Bewertung Sicherheitskontrollen bei Unterbrechungen)
- ISMS-IMP-A.5.29.2-UG/TG (Sicherheitsanforderungen im Degraded-Mode)
- ISMS-IMP-A.5.29.3-UG/TG (Sicherheitsverifizierung nach Wiederherstellung)
- ISO/IEC 27001:2022 Massnahme A.5.29

---

## Zusammenfassung

Diese Richtlinie legt die Anforderungen von [Organisation] für die Aufrechterhaltung von Informationssicherheitskontrollen bei störenden Ereignissen fest und stellt sicher, dass die Sicherheit bei Unterbrechung des Normalbetriebs nicht beeinträchtigt wird.

**Geltungsbereich**: Diese Richtlinie gilt für alle störenden Ereignisse, die die Fähigkeit von [Organisation] zum Normalbetrieb beeinträchtigen, einschliesslich Naturkatastrophen, Infrastrukturausfällen, Cyber-Vorfällen, Pandemien, Lieferkettenstörungen und zivilen Unruhen.

**Zweck**: Organisatorische Anforderungen für die Sicherheit bei Unterbrechungen definieren. Diese Richtlinie legt fest, WELCHE Sicherheitskontrollen aufrechterhalten werden müssen und WER für die Sicherheit unter widrigen Bedingungen verantwortlich ist. Umsetzungsverfahren (WIE) sind separat in ISMS-IMP-A.5.29 (UG/TG-Varianten) dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich Schweizer nDSG, EU DSGVO und ISO/IEC 27001:2022. Bedingte sektorspezifische Anforderungen (DORA, NIS2, FINMA) gelten, wenn die Geschäftstätigkeit von [Organisation] die Anwendbarkeit auslöst.

**Kritisches Prinzip – «Sicherheit kennt keine Auszeit»**: Betriebsunterbrechungen schaffen Gelegenheiten für Bedrohungsakteure. Wenn Organisationen sich auf die Wiederherstellung konzentrieren, nutzen Angreifer die verringerte Wachsamkeit aus. Diese Richtlinie stellt sicher, dass Sicherheitskontrollen in allen Phasen der Unterbrechung und Wiederherstellung wirksam bleiben.

---

**Massnahmenausrichtung & Geltungsbereich**

**ISO/IEC 27001:2022 Massnahme A.5.29**

[Organisation] hält definierte Sicherheitskontrollen während Unterbrechungen durch etablierte Baselines, gestufte Sicherheitsniveaus und vorausgeplante Wiederherstellungsverfahren aufrecht, die eine Sicherheitsgefährdung unter widrigen Bedingungen verhindern.

**Massnahmenziele**:

- Sicherstellen, dass Informationssicherheitskontrollen bei störenden Ereignissen wirksam bleiben
- Sicherheitsanforderungen in die BC/DR-Planung integrieren
- Sicherheitsgefährdung im Interesse der Schnelligkeit bei Wiederherstellungsoperationen verhindern
- Einhaltung regulatorischer Pflichten bei Unterbrechungen aufrechterhalten

**Massnahmentyp**: Präventiv, Detektiv, Korrigierend
**Massnahmenkategorie**: Organisatorisch

**Diese Richtlinie adressiert**:

- Mindest-Sicherheitsbaseline bei Unterbrechungen
- Gestufte Sicherheitsniveaus
- Sicherheitsanforderungen für BC/DR-Pläne
- Notfallzugriffsverfahren
- Sicherheitsvalidierung nach Unterbrechungen

## Was diese Richtlinie leistet

Diese Richtlinie:

- **Definiert** Mindestsicherheitskontrollen, die bei Unterbrechungen aufrechterhalten werden müssen
- **Etabliert** gestufte Sicherheitsniveaus, die mit dem Schweregrad der Unterbrechung abgestimmt sind
- **Legt** Sicherheitsanforderungen für BC/DR-Pläne und Wiederherstellungsstandorte fest
- **Verweist** auf anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

## Was diese Richtlinie NICHT leistet

Diese Richtlinie legt NICHT fest:

- **Umfang und Methodik der Business-Continuity-Planung** (siehe ISMS-POL-A.5.30-8.13-14)
- **Redundanzarchitektur für Verarbeitungseinrichtungen** (siehe ISMS-POL-A.8.14)
- **Incident-Response-Verfahren für Sicherheitsereignisse** (siehe ISMS-POL-A.5.24-28)
- **Backup-Verfahren und Datenschutz** (siehe ISMS-POL-A.8.13)

## Geltungsbereich

**Diese Richtlinie gilt für**:

- Alle störenden Ereignisse (Naturkatastrophen, Infrastrukturausfälle, Cyber-Vorfälle, Pandemien)
- Alle Informationssysteme, Netzwerke, Anwendungen und Datenverarbeitungseinrichtungen
- Alle Business-Continuity- und Notfallwiederherstellungsprozesse
- Gesamtes Personal während der Unterbrechungs- und Wiederherstellungsphasen

**Nicht im Geltungsbereich**:

- Business-Continuity-Planungsmethodik (abgedeckt durch A.5.30)
- Redundanzarchitekturentscheidungen (abgedeckt durch A.8.14)
- Sicherheits-Incident-Response-Verfahren (abgedeckt durch A.5.24-28)

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen sind gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Verbindliche Compliance**

| Regulierung | Anwendbarkeit | Kernanforderungen |
|-------------|---------------|-------------------|
| **Schweizer nDSG Art. 8** | Gesamte Personendatenverarbeitung | Geeignete Sicherheitsmassnahmen aufrechterhalten |
| **EU DSGVO Art. 32** | Verarbeitung von EU-Personendaten | Sicherheit der Verarbeitung einschliesslich Verfügbarkeit |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Massnahme A.5.29 – Sicherheit bei Betriebsunterbrechungen |

**Stufe 2: Bedingte Anwendbarkeit**

Nur anwendbar, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | Sicherheitsanforderungen |
|-------------|-----------------|--------------------------|
| **DORA** | EU-Finanzdienstleistungseinheit | Digitale operationelle Resilienz einschliesslich IKT-Vorfällen |
| **NIS2** | Wesentliche/wichtige Einrichtung (EU) | Betriebskontinuität einschliesslich Krisenmanagement |
| **FINMA** | Reguliertes Schweizer Finanzinstitut | Anforderungen an operationelle Resilienz (Rundschreiben 2023/1) |
| **Gesundheitsregelungen** | Gesundheitsbetrieb | Kontinuität des Schutzes von Patientendaten |

**Stufe 3: Informative Orientierung**

Diese Frameworks dienen als Orientierung bei der Umsetzung, stellen jedoch keine verbindlichen Compliance-Anforderungen dar, sofern nicht vertraglich gefordert:

- ISO 22301 (Business-Continuity-Managementsysteme)
- NIST SP 800-34 (Leitfaden zur Notfallplanung)
- BCI Good Practice Guidelines
- ENISA-Leitlinien zur IKT-Servicekontinuität

**Compliance-Feststellung**: [Organisation] bestimmt anwendbare Stufe-2-Regulierungen durch regelmässige Bewertung der Geschäftstätigkeit. Bei Überschneidung mehrerer Regulierungen gelten die strengsten Sicherheitsanforderungen. Regulatorische Pflichten und spezifische Fristen unterliegen dem Regulatorischen Anforderungsregister (Ergebnis von ISMS-POL-00); diese Richtlinie gilt unabhängig vom regulatorischen Auslöser.

---

# Richtlinienerklärungen

## Sicherheitsanforderungen bei Betriebsunterbrechungen

### Mindest-Sicherheitsbaseline

[Organisation] MUSS die folgenden Mindestsicherheitskontrollen unabhängig vom Betriebsstatus aufrechterhalten:

**Kontrollparameter / Quellen der Wahrheit**: Für die Zwecke dieser Richtlinie:
- **Kritische Systeme**: Als Stufe-1 oder Stufe-2 im System-Kritikalitätsregister klassifizierte Systeme, abgeleitet aus der BIA
- **Vertraulich+**: Als VERTRAULICH oder EINGESCHRÄNKT klassifizierte Informationen gemäss ISMS-POL-A.5.12-13 (Datenklassifikationsrichtlinie)
- **Kritische Protokollierung**: Der in der Protokollierungsstandard (ISMS-IMP-A.8.15) definierte Mindestprotokollsatz, geltend für alle Stufe-1-/Stufe-2-Systeme
- **Kritische Grenzen**: Netzwerksegmentierungszonen zum Schutz von Stufe-1-/Stufe-2-Systemen, wie in der Netzwerkarchitektur-Dokumentation definiert

**Nicht verhandelbare Kontrollen** (Müssen jederzeit aufrechterhalten werden):

| Kontrollkategorie | Mindestanforderung | Begründung |
|-------------------|--------------------|------------|
| **Zugriffskontrolle** | Authentifizierung für jeden Systemzugriff erforderlich | Verhindert unbefugten Zugriff bei Chaos |
| **Datenverschlüsselung** | Verschlüsselung ruhender Daten für Vertraulich+-Daten | Daten bleiben geschützt, falls Medien verloren gehen |
| **Protokollierung** | Protokollierung kritischer Systeme fortsetzen | Prüfpfad für Nachuntersuchung |
| **Netzwerksegmentierung** | Kritische Netzwerkgrenzen aufrechterhalten | Verhindert seitliche Bewegung bei Wiederherstellung |
| **Backup-Schutz** | Backups bleiben verschlüsselt und zugangskontrolliert | Verhindert Backup-Kompromittierung für Datendiebstahl |

**Degraded Mode akzeptabel** (Mit dokumentierter Genehmigung und kompensierenden Massnahmen):

| Kontrollkategorie | Akzeptable Verschlechterung | Erforderliche kompensierende Massnahme |
|-------------------|-----------------------------|----------------------------------------|
| **MFA** | Einzelfaktor, wenn MFA-Infrastruktur nicht verfügbar | Verstärkte Protokollierung, Sitzungslimits, IP-Beschränkungen |
| **Schwachstellen-Scanning** | Verzögertes Scanning akzeptabel | Manuelle Prüfung nur kritischer Patches |
| **Sicherheitsüberwachung** | Reduzierter Umfang akzeptabel | Fokus auf kritische Systeme, verstärkte manuelle Prüfung |
| **Zugriffsprüfungen** | Aufgeschobene Prüfungen akzeptabel (max. 30 Tage) | Strengere Genehmigung für neue Zugriffsanfragen |
| **Patch-Management** | Verzögertes Patching akzeptabel (max. 30 Tage für unkritische) | Kritische/hohe Schwachstellen weiterhin innerhalb 72h/7 Tagen |

**Obligatorische Nachverfolgung**: Jede genehmigte Kontrollverschlechterung MUSS sofort einen zeitgebundenen Eintrag im Sicherheits-Schuldenregister oder Ausnahmenregister (ISMS-REG-AUSNAHMEN) erstellen, einschliesslich: Verantwortlicher, kompensierende Massnahmen, Startdatum, Schliessungsfälligkeitsdatum gemäss dieser Richtlinie und Schliessnungsnachweis.

**Nie akzeptabel** (Auch bei Betriebsunterbrechungen):

- Deaktivierte Protokollierung auf kritischen Systemen
- Aufhebung von Authentifizierungsanforderungen
- Entschlüsselung ruhender Daten ohne Wiederverschlüsselung
- Deaktivierung von Netzwerksicherheitskontrollen (Firewalls, IDS/IPS)
- Gemeinsame Nutzung privilegierter Zugangsdaten ohne individuelle Verantwortlichkeit
- Umgehung des Change-Managements für Produktionssysteme (ausser bei deklariertem Notfall gemäss ISMS-IMP-A.8.32 Notfall-Änderungsverfahren, mit Nachimplementierungsprüfung innerhalb von 5 Arbeitstagen)

### Gestufte Sicherheitsniveaus

[Organisation] MUSS Sicherheitsniveaus definieren, die mit dem Schweregrad der Unterbrechung abgestimmt sind:

| Stufe | Unterbrechungsstatus | Sicherheitsniveau | Beispiel |
|-------|---------------------|-------------------|----------|
| **Normal** | Keine Unterbrechung | Alle Sicherheitskontrollen in Betrieb | Tagesbetrieb |
| **Erhöht** | Geringfügige Unterbrechung | Verstärkte Überwachung, beschleunigtes Patching | Einzelsystemausfall, kleinerer Vorfall |
| **Degraded** | Mittlere Unterbrechung | Kernkontrollen aufrechterhalten, Nicht-Kritisches zurückgestellt | Rechenzentrum-Failover, regionaler Ausfall |
| **Notfall** | Schwere Unterbrechung | Nur Mindest-Baseline, Überlebensmodus | Mehrstandortkatastrophe, grösserer Cyber-Angriff |
| **Wiederherstellung** | Rückkehr zum Normalbetrieb | Schrittweise Wiederherstellung mit Sicherheitsvalidierung | Post-Katastrophen-Wiederherstellungsphase |

**Übergangsbefugnisse**:

| Übergang | Erforderliche Befugnis | Dokumentation |
|----------|------------------------|---------------|
| Normal → Erhöht | ISB oder Teamleiter Sicherheit | Incident-Ticket |
| Erhöht → Degraded | ISB + ITL | Formelle Benachrichtigung der Geschäftsleitung |
| Degraded → Notfall | Geschäftsleitung (GF oder Stellvertreter) | Notfalldeklarationsdokument |
| Wiederherstellungsübergänge | ISB-Genehmigung für jede Phase | Phasenabschluss-Checkliste |

## Sicherheitsplanung für BC/DR

### Sicherheitsanforderungen für BC/DR-Pläne

Alle Business-Continuity- und Notfallwiederherstellungspläne MÜSSEN folgendes enthalten:

**Sicherheitsüberlegungen in BC/DR-Plänen**:

1. **Zugriffskontrolle bei der Wiederherstellung**:
   - Wer hat Zugang zu Wiederherstellungssystemen und -daten
   - Wie wird Zugang authentifiziert, wenn normale Systeme nicht verfügbar sind
   - Wie wird Zugang nach Abschluss der Wiederherstellung widerrufen
   - Notfallzugriffskonten und ihre Kontrollen

2. **Datenschutz bei der Wiederherstellung**:
   - Wie Daten bei der Übertragung zum Wiederherstellungsstandort geschützt werden
   - Verschlüsselungsanforderungen für Wiederherstellungsmedien
   - Beweismittelkette für physische Datenbewegungen
   - Durchsetzung der Datenklassifikation in der Wiederherstellungsumgebung

3. **Kommunikationssicherheit**:
   - Sichere Kommunikationskanäle für das Krisenteam
   - Alternative Kommunikation, wenn primäre Kanäle kompromittiert sind
   - Authentifizierung von Krisenkommunikation (Social-Engineering-Prävention)
   - Grenzen der Informationsweitergabe (was extern geteilt werden darf)

4. **Drittanbieter-Sicherheit**:
   - Lieferantenzugriffskontrollen bei der Wiederherstellung
   - Sicherheitsanforderungen für Auftragnehmer im Notfallbetrieb
   - Cloud-Service-Sicherheit bei Failover
   - Lieferkettensicherheit für Notfallbeschaffungen

**Sicherheitsüberprüfung der BC/DR-Pläne**:

- ISB oder Stellvertreter MÜSSEN Sicherheitsabschnitte aller BC/DR-Pläne prüfen und genehmigen
- Sicherheitsüberprüfung MUSS vor Genehmigung des BC/DR-Plans und nach jeder Aktualisierung erfolgen
- Sicherheitsspezifische BC/DR-Testszenarien MÜSSEN in jährliche Tests einbezogen werden
- Sicherheitsabweichungen bei Tests MÜSSEN dokumentiert und behoben werden

### Sicherheit an Wiederherstellungsstandorten

Wiederherstellungsstandorte (Hot, Warm, Cold Sites, Cloud-DR) MÜSSEN folgendes aufrechterhalten:

| Kontrolle | Anforderung |
|-----------|-------------|
| **Physische Sicherheit** | Äquivalent zum Primärstandort für die jeweilige Datenkritikalität |
| **Netzwerksicherheit** | Gleiche Segmentierung, Firewall-Regeln, Überwachung |
| **Zugriffskontrolle** | Gleiche Authentifizierungs- und Autorisierungsmodell |
| **Datenschutz** | Gleiche Verschlüsselungs- und Klassifikationskontrollen |
| **Protokollierung** | Äquivalente Protokollierungsfähigkeit |
| **Härtung** | Gleiche Konfigurationsbaselines |

## Notfallzugriffsverfahren

### Break-Glass-Zugriff

[Organisation] MUSS Notfallzugangsmechanismen für Unterbrechungsszenarien bereithalten:

**Break-Glass-Konto-Anforderungen**:

| Anforderung | Spezifikation |
|-------------|---------------|
| **Kontostatus** | Ruhend (deaktiviert) bis Notfall deklariert |
| **Aktivierungsbefugnis** | ISB, ITL oder GF (dokumentierte Befugniskette) |
| **Authentifizierung** | Starke Authentifizierung (sicher aufbewahrt, mehrere Faktoren) |
| **Umfang** | Vordefiniert, auf wiederherstellungswesentliche Systeme beschränkt |
| **Protokollierung** | Alle Aktionen mit Manipulationsschutz protokolliert |
| **Dauer** | Zeitlich begrenzt (automatische Deaktivierung nach Ende des deklarierten Notfalls) |
| **Deaktivierung** | Formelle Deaktivierung mit Passwortänderung/-rotation |

**Notfallzugriffsprotokoll**: Jede Break-Glass-Aktivierung MUSS im Notfallzugriffsprotokoll erfasst werden mit: Genehmigender, Aktivierender, zugegriffene Systeme, Start-/Endzeit, durchgeführte Aktionen, Bestätigung der Protokollerfassung und Deaktivierungsverifizierung.

**Break-Glass-Aktivierungsprozess**:

1. Notfall von befugter Stelle deklariert
2. Break-Glass-Aktivierungsanfrage dokumentiert (auch mündlich, mit schriftlicher Nacherfassung innerhalb von 4 Stunden)
3. Aktivierung durch designiertes Personal (Vier-Augen-Prinzip für kritische Systeme)
4. Benachrichtigung von ISB und Sicherheitsteam
5. Verstärkte Überwachung aktiviert
6. Zeitlich begrenzter Zugang (Standard: 24 Stunden, verlängerbar mit erneuter Genehmigung)
7. Deaktivierung nach Notfall und vollständige Überprüfung

### Verfügbarkeit des Personals

[Organisation] MUSS die Verfügbarkeit von Sicherheitspersonal bei Unterbrechungen sicherstellen:

**Kontinuität des Sicherheitsteams**:

- Schlüsselsicherheitsrollen haben designierte Stellvertreter (dokumentierter Nachfolgeplan)
- Kontaktinformationen des Sicherheitspersonals offline gepflegt (Ausdruck, verschlüsselter USB)
- Geografische Verteilung des Sicherheitsteams, wo möglich
- Übergreifende Schulung zur Sicherstellung der Abdeckung kritischer Sicherheitsfunktionen
- Bereitschaftsrotation für 24/7-Abdeckung im erhöhten/degradierten/Notfallstatus

## Sicherheitsvalidierung nach Unterbrechungen

### Wiederherstellung der Sicherheitsposition

Vor der Rückkehr zum Normalbetrieb MUSS [Organisation] die Sicherheitsposition validieren:

**Sicherheits-Wiederherstellungs-Checkliste**:

| Phase | Validierungsaktivitäten |
|-------|------------------------|
| **Sofort (0-24h nach Unterbrechung)** | Verifizierung kritischer Sicherheitskontrollen in Betrieb, Deaktivierung Notfallzugang, Protokollprüfung auf Anomalien |
| **Kurzfristig (1-7 Tage)** | Vollständige Sicherheitskontrollvalidierung, Schwachstellen-Scan, Zugriffsprüfung, Vorfallanalyse |
| **Mittelfristig (1-4 Wochen)** | Behebung von Sicherheitsschulden, aufgeschobene Patches angewendet, vollständige Zugangsneubestätigung, Kontrolltest |
| **Langfristig (1-3 Monate)** | Umsetzung von Erkenntnissen, BC/DR-Plan-Updates, Richtlinienaktualisierungen, Schulungsaktualisierungen |

**Verfolgung von Sicherheitsschulden**:

- Alle Sicherheitserleichterungen während der Unterbrechung MÜSSEN im Sicherheitsschuldenregister erfasst werden
- Jeder Schuldeneintrag MUSS Verantwortlichen, Behebungsplan und Zieldatum enthalten
- Sicherheitsschulden älter als 30 Tage MÜSSEN an den ISB eskaliert werden
- Sicherheitsschulden älter als 90 Tage MÜSSEN an die Geschäftsleitung eskaliert oder als dauerhaftes Risiko akzeptiert werden

---

# Rollen und Verantwortlichkeiten

## Verantwortlichkeitsmatrix

| Rolle | Verantwortlichkeiten bei Sicherheit während Unterbrechungen |
|-------|-------------------------------------------------------------|
| **Geschäftsleitung** | Sicherheitsniveaus genehmigen, Notfallmodus autorisieren, Ressourcenzuteilung |
| **ISB** | Sicherheitsanforderungen für BC/DR, Sicherheitsniveauübergänge genehmigen, Validierung nach Unterbrechung |
| **Business-Continuity-Manager** | Sicherheitsanforderungen in BC/DR-Pläne integrieren, mit ISB koordinieren |
| **ITL** | IT-Wiederherstellung mit Sicherheitsanforderungen abgestimmt, Notfallzugangsgenehmigung |
| **Sicherheitsteam** | Sicherheit bei Unterbrechung überwachen, Notfallverfahren aktivieren, Wiederherstellung validieren |
| **Krisenmanagement-Team** | Sicherheitsüberlegungen in Krisenentscheidungen einbeziehen, mit ISB kommunizieren |
| **IT-Betrieb** | Sicherheitskontrollen in Wiederherstellungsumgebungen umsetzen, Sicherheitsprobleme melden |
| **Gesamtes Personal** | Sicherheitsverfahren bei Unterbrechungen befolgen, Sicherheitsbedenken melden |

## Eskalationspfad

- Sicherheitsbedenken bei aktiver Unterbrechung: Sicherheitsteam → ISB → Krisenmanagement-Team
- Sicherheitsvorfälle bei Unterbrechung: Gemäss ISMS-POL-A.5.24-28 mit erhöhter Priorität
- Anfragen zum Sicherheitsniveauübergang: Antragsteller → ISB → Geschäftsleitung (nach Bedarf)

---

# Governance & Compliance

## Bewertungs-Framework

| Bewertung | Häufigkeit | Verantwortlicher | Nachweise |
|-----------|------------|------------------|-----------|
| BC/DR-Plan Sicherheitsüberprüfung | Jährlich + nach Aktualisierungen | ISB | Überprüfungsbericht, Genehmigungsunterschrift |
| Notfallzugangstest | Jährlich | Sicherheitsteam | Testergebnisse, Verfahrensvalidierung |
| Sicherheitskomponente der BC/DR-Tests | Mit BC/DR-Tests (mindestens jährlich) | Sicherheitsteam + BC-Manager | Testszenarien, Befunde, Behebung |
| Sicherheitsbewertung Wiederherstellungsstandort | Jährlich | Sicherheitsteam | Konfigurationsprüfung, Lückenanalyse |
| Verfügbarkeitsübung Sicherheitspersonal | Halbjährlich | ISB | Kontakttestergebnisse, Nachfolgevalidierung |

**Governance-Metriken**:

- BC/DR-Pläne mit ISB-Sicherheitsgenehmigung (Ziel: 100%)
- Abgeschlossene Tests der Notfallzugangsverfahren (Ziel: 100% jährlich)
- Sicherheitsvorfälle bei Unterbrechungsereignissen (Trendverfolgung)
- Sicherheitsschuldenpositionen nach Unterbrechungen (Ziel: 0 Positionen > 90 Tage)
- Befunde der Sicherheitsbewertung am Wiederherstellungsstandort (Ziel: 0 kritische/hohe Befunde)

## Richtlinienüberprüfung

- **Häufigkeit**: Mindestens jährlich
- **Auslöser**: Grösseres Unterbrechungsereignis, BC/DR-Planänderungen, regulatorische Aktualisierungen, Prüfungsergebnisse
- **Prüfer**: ISB, Business-Continuity-Manager, ITL, Krisenmanagement-Team
- **Genehmigung**: Geschäftsleitung

## Ausnahmenmanagement

**Zulässige Ausnahmen**:

- Sicherheitskontrollverschlechterung bei aktiver Unterbrechung (mit dokumentierten kompensierenden Massnahmen)
- Vorab genehmigte Dauerlockerungen für spezifische Szenarien (risikobewertet und zeitlich begrenzt)
- Sicherheitsschulden nach Unterbrechung mit dokumentierten Behebungsplänen

**Ausnahmeprozess**:

1. Geschäftliche Begründung und Unterbrechungskontext dokumentieren
2. Risikobewertung der Sicherheitsauswirkungen
3. ISB-Genehmigung (oder designierter Stellvertreter, wenn ISB nicht verfügbar)
4. Kompensierende Massnahmen dokumentiert
5. Zeitlich begrenzte Genehmigung (Dauer der Unterbrechung + 7 Tage für Wiederherstellung)

**Nicht zulässig**:

- Dauerhafte Ausnahmen von der Mindest-Sicherheitsbaseline
- Ausnahmen, die die Prüfpfadfähigkeit eliminieren
- Ausnahmen ohne kompensierende Massnahmen

Alle Ausnahmen MÜSSEN im Ausnahmenregister (ISMS-REG-AUSNAHMEN) erfasst werden.

## Verknüpfung mit Korrekturmassnahmen

Nichtkonformitäten im Zusammenhang mit dieser Richtlinie (z. B. unzureichende BC/DR-Sicherheitsüberprüfung, ungetesteter Notfallzugang, Akkumulation von Sicherheitsschulden, Lücken am Wiederherstellungsstandort) MÜSSEN durch den ISMS-Korrekturmassnahmenprozess (Abschnitt 10.2) mit Ursachenanalyse und verfolgter Behebung erfasst und verwaltet werden.

---

# Umsetzung & Referenzen

## Integration mit dem ISMS

Diese Richtlinie integriert sich in das Informationssicherheits-Managementsystem von [Organisation]:

**Risikobeurteilung** (ISO 27001 Abschnitt 6.1):

- Unterbrechungsszenarien in der Risikobeurteilung einbezogen
- Sicherheitsanforderungen bei Unterbrechungen durch Auswirkungsanalyse informiert
- Risikobehandlungspläne dokumentieren Sicherheitskontrollen für BC/DR

**Anwendbarkeitsnachweis** (ISO 27001 Abschnitt 6.1.3):

- Anwendbarkeit von Massnahme A.5.29 im SoA von [Organisation] begründet
- Umsetzungsstatus verfolgt und berichtet

**Verwandte Massnahmen**:

| Massnahme | Beziehung |
|-----------|-----------|
| **A.5.30** | Betriebskontinuität – BC/DR-Planung; A.5.29 liefert Sicherheitsanforderungen |
| **A.8.13** | Backup – Datenschutz bei Unterbrechungen |
| **A.8.14** | Redundanz – Sicherheitsanforderungen für Wiederherstellungsstandorte |
| **A.5.24-28** | Incident-Management – Sicherheitsvorfälle bei Unterbrechungen |
| **A.8.15** | Protokollierung – Protokollierungsanforderungen bei Unterbrechungen |
| **A.5.15-16-18** | Zugriffskontrolle – Notfallzugang, Zugriff bei Unterbrechungen |

## Umsetzungsressourcen

**Umsetzungsleitfäden** (ISMS-IMP-A.5.29-Suite):

| Dokument-ID | Titel | Zweck |
|-------------|-------|-------|
| **ISMS-IMP-A.5.29.1-UG/TG** | Sicherheitsanforderungen für BC/DR-Pläne | BC/DR-Sicherheitsintegrations-Verfahren |
| **ISMS-IMP-A.5.29.2-UG/TG** | Notfallzugriffsverfahren | Break-Glass-Aktivierung und -Deaktivierung |
| **ISMS-IMP-A.5.29.3-UG/TG** | Checkliste Sicherheitsvalidierung nach Unterbrechung | Wiederherstellungs-Validierungsverfahren |

---

# Nachweise für diese Richtlinie

**Phase 1 (Dokumentenprüfung) Nachweise:**

Erforderliche Phase-1-Nachweise umfassen:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.29 v1.0)
- ✅ Genehmigte Genehmigung durch ISB, Business-Continuity-Manager, ITL, Geschäftsleitung
- ✅ Nachweis der Kommunikation an relevante Rollen
- ✅ Mindest-Sicherheitsbaseline definiert (Sicherheitsanforderungen bei Betriebsunterbrechungen)
- ✅ Gestufte Sicherheitsniveaus mit Übergangsbefugnissen definiert (Gestufte Sicherheitsniveaus)
- ✅ BC/DR-Plan-Sicherheitsanforderungen festgelegt (Sicherheitsplanung für BC/DR)
- ✅ Notfallzugriffsverfahren definiert (Notfallzugriffsverfahren)
- ✅ Validierungsanforderungen nach Unterbrechung definiert (Sicherheitsvalidierung nach Unterbrechungen)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Rollen und Verantwortlichkeiten)

Nachweisstand wird im ISMS-Nachweisregister verfolgt.

**Phase 2 (Operative Wirksamkeit) Nachweise:**

Nachweise zur Demonstration der operativen Wirksamkeit dieser Richtlinie:

- BC/DR-Pläne mit ISB-Sicherheitsgenehmigungsunterschriften
- Testergebnisse des Notfallzugangs (Break-Glass) und Verfahrensvalidierung
- BC/DR-Testergebnisse mit sicherheitsspezifischen Szenarien
- Sicherheitsbewertungsberichte der Wiederherstellungsstandorte
- Ergebnisse der Verfügbarkeitsübungen für Sicherheitspersonal
- Übergangsaufzeichnungen für Sicherheitsniveaus (falls Unterbrechungen eingetreten)
- Sicherheitsschuldenregister mit Behebungsverfolgung
- Sicherheitsüberprüfungsberichte nach Unterbrechungen (falls eingetreten)
- Schulungsnachweise für Krisenmanagement-Team-Sicherheitsverfahren

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Betriebsunterbrechung** | Jedes Ereignis, das den normalen Geschäftsbetrieb unterbricht oder zu unterbrechen droht |
| **Sicherheitsniveau** | Definierter Zustand der Sicherheitskontrollumsetzung (Normal, Erhöht, Degraded, Notfall, Wiederherstellung) |
| **Break-Glass-Zugriff** | Notfall-Privilegienzugangsmechanismus, der aktiviert wird, wenn normaler Zugang nicht verfügbar ist |
| **Sicherheitsschulden** | Sicherheitskontrollen oder -aktivitäten, die bei Unterbrechungen zurückgestellt wurden und spätere Behebung erfordern |
| **Wiederherstellungsstandort** | Alternativer Standort (physisch oder Cloud) zur Fortführung des Betriebs bei Unterbrechungen |
| **Krisenmanagement-Team** | Funktionsübergreifendes Team, das zur Bewältigung organisatorischer Reaktionen auf grössere Unterbrechungen aktiviert wird |
| **Kompensierende Massnahme** | Alternative Sicherheitsmassnahme, die implementiert wird, wenn die primäre Massnahme nicht verfügbar ist |
| **Mindest-Sicherheitsbaseline** | Nicht verhandelbare Sicherheitskontrollen, die unabhängig vom Betriebsstatus aufrechterhalten werden müssen |

---

# Genehmigungsnachweis

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Festzulegen] |
| **Business-Continuity-Manager** | [Name] | [Festzulegen] |
| **IT-Leiter (ITL)** | [Name] | [Festzulegen] |
| **Geschäftsleitung** | [Name] | [Festzulegen] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen für die Aufrechterhaltung der Informationssicherheit bei Betriebsunterbrechungen fest. Umsetzungsverfahren sind in ISMS-IMP-A.5.29 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
