<!-- ISMS-CORE:POLICY:ISMS-POL-A.6.7-8-DE:framework:POL:a.6.7-8 -->
**ISMS-POL-A.6.7-8 – Remote-Arbeit und Sicherheitsereignismeldung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Remote-Arbeit und Sicherheitsereignismeldung |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.6.7-8 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Unternehmensleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | INTERN |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstrichtlinie für ISO 27001:2022-Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Gültigkeitsdatum + 12 Monate]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Personalleiter (PL)
- Technisch: IT-Direktor / TL
- Letzte Instanz: Unternehmensleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)
- ISMS-IMP-A.6.7-8.-UG/TGS1 bis .S5 (Implementierungs- und Beurteilungsleitfaden-Suite)
- ISO/IEC 27001:2022 Controls A.6.7, A.6.8
- ISO/IEC 27002:2022 Abschnitte 6.7, 6.8 (Implementierungsleitfaden)
- ISMS-POL-A.5.1-2-6.1-2 (Sichere Beschäftigung und Rollen)
- ISMS-POL-A.6.3 (Bewusstsein und Schulung)
- ISMS-POL-A.5.24-28 (Incident-Management-Lebenszyklus)
- ISMS-POL-A.8.1-7-18-19 (Endpunktsicherheit)

---

## Zusammenfassung für die Unternehmensleitung

Diese Richtlinie legt die Anforderungen von [Organisation] für Remote-Arbeitssicherheit und die Meldung von Informationssicherheitsereignissen gemäss ISO/IEC 27001:2022 Controls A.6.7 und A.6.8 fest.

**Geltungsbereich**: Diese Richtlinie gilt für alle Mitarbeitenden, die remote oder ausserhalb der Räumlichkeiten von [Organisation] arbeiten, alle für Remote-Arbeit verwendeten Geräte (unternehmenseigen und persönlich), alle remote zugegriffenen oder verarbeiteten Informationen sowie für alle Mitarbeitenden, die für die Meldung von Sicherheitsereignissen verantwortlich sind, unabhängig vom Arbeitsort.

**Zweck**: Definition der organisatorischen Anforderungen für sicheres Remote-Arbeiten und zeitnahe Meldung von Sicherheitsereignissen. Diese Richtlinie legt fest, WELCHE Sicherheitsmassnahmen für Remote-Arbeit erforderlich sind, WER remote arbeiten darf und unter welchen Bedingungen, WAS ein meldepflichtiges Sicherheitsereignis darstellt und WER für Meldung und Reaktion verantwortlich ist. Implementierungsverfahren (WIE) sind separat in ISMS-IMP-A.6.7-8 (UG/TG-Varianten) S1 bis S5 dokumentiert.

**Kombinierter Kontroll-Rahmen**: Diese beiden Controls werden als einheitliches Rahmenwerk implementiert, weil:

1. **Remote-Mitarbeitende sind die erste Verteidigungslinie bei der Erkennung von Ereignissen** – im Remote-Betrieb tätige Mitarbeitende beobachten häufig als Erste Sicherheitsanomalien, die ihre Geräte, Verbindungen oder den Datenzugriff betreffen
2. **Einzigartige Remote-Arbeit-Bedrohungen erfordern spezialisierte Meldeverfahren** – Remote-Mitarbeitende sind Bedrohungen ausgesetzt, die in Büroumgebungen nicht vorhanden sind (unsichere Netzwerke, physischer Zugang durch andere Personen, Risiken in öffentlichen Räumen)
3. **ISO 27002:2022 verknüpft sie ausdrücklich** – der Leitfaden zu Remote-Arbeit verlangt, dass Vorfallmeldeverfahren von entfernten Standorten aus zugänglich sind
4. **Gleiche Personalpopulation** – beide Controls richten sich an dieselben Personen und deren Sicherheitsverantwortlichkeiten; kombinierte Schulungen sind wirksamer

**Unabhängigkeit der Anwendbarkeitserklärung**: Obwohl als einheitliches Rahmenwerk implementiert, werden A.6.7 und A.6.8 in der Anwendbarkeitserklärung unabhängig voneinander beurteilt. Jeder Control behält für Audit-Zwecke eigenständige Anforderungen, Nachweiserhebung und Compliance-Bewertung.

**Regulatorische Ausrichtung**: Diese Richtlinie erfüllt die obligatorischen Compliance-Anforderungen gemäss ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit), einschliesslich schweizerischem nDSG (Datenschutz), EU-DSGVO (wo anwendbar), ISO/IEC 27001:2022 und branchenspezifischen Anforderungen, wo anwendbar.

**Bedeutung**: Remote-Arbeit ist zur Standardpraxis geworden und erweitert die organisatorische Angriffsfläche über traditionelle Perimeter-Verteidigungen hinaus. Branchenforschung zeigt, dass Remote-Mitarbeitende einer dreifach höheren Phishing-Exposition ausgesetzt sind, und die durchschnittliche Zeit zur Erkennung einer Datenpanne steigt signifikant, wenn Mitarbeitende ausserhalb überwachter Netzwerke arbeiten. Dieses Rahmenwerk adressiert diese Risiken durch systematische Sicherheitsanforderungen und robuste Meldeverfahren.

---

# Kontrollausrichtung und Geltungsbereich

## ISO/IEC 27001:2022 Control A.6.7 – Remote-Arbeit

**ISO/IEC 27001:2022 Anhang A.6.7 – Remote-Arbeit**

> *Sicherheitsmassnahmen müssen implementiert werden, wenn Mitarbeitende remote arbeiten, um Informationen zu schützen, auf die ausserhalb der Räumlichkeiten der Organisation zugegriffen, die dort verarbeitet oder gespeichert werden.*

**Kontrollziel**: Sicherstellen, dass Remote-Mitarbeitende über die notwendigen Sicherheitskontrollen verfügen, um die Vertraulichkeit, Integrität und Verfügbarkeit organisatorischer Informationen, Verfahren und Systeme vor unbefugtem Zugriff oder Offenlegung zu schützen, wenn sie ausserhalb der Räumlichkeiten von [Organisation] arbeiten.

**Kontrolltyp**: Präventiv
**Kontrollkategorie**: Personenkontrolle
**Sicherheitseigenschaften**: Vertraulichkeit, Integrität, Verfügbarkeit

**Zusammenfassung des ISO/IEC 27002:2022-Leitfadens**:

- Richtlinie zur Remote-Arbeit definiert Bedingungen und Einschränkungen
- Physische Sicherheit des Remote-Arbeitsplatzes adressiert
- Risiko des unbefugten Zugriffs durch Personen, die den Raum teilen
- Sichere Kommunikationskanäle erforderlich
- Multi-Faktor-Authentifizierung für Remote-Zugang
- Verschlüsselung von Daten während der Übertragung und im Ruhezustand
- Bestimmungen für Hardware- und Software-Support
- Backup- und Business-Continuity-Verfahren
- Audit- und Sicherheitsüberwachungsfähigkeiten
- Zugangssperrung und Geräterückgabe bei Kündigung

## ISO/IEC 27001:2022 Control A.6.8 – Meldung von Informationssicherheitsereignissen

**ISO/IEC 27001:2022 Anhang A.6.8 – Meldung von Informationssicherheitsereignissen**

> *Die Organisation muss einen Mechanismus bereitstellen, der es dem Personal ermöglicht, beobachtete oder vermutete Informationssicherheitsereignisse über geeignete Kanäle zeitnah zu melden.*

**Kontrollziel**: Unterstützung einer zeitnahen, konsistenten und effektiven Meldung von Informationssicherheitsereignissen, die vom Personal identifiziert werden können, um sicherzustellen, dass Ereignisse genau dokumentiert werden, um Incident-Response-Aktivitäten und andere Sicherheitsmanagement-Verantwortlichkeiten zu unterstützen.

**Kontrolltyp**: Erkennend
**Kontrollkategorie**: Personenkontrolle
**Sicherheitseigenschaften**: Vertraulichkeit, Integrität, Verfügbarkeit

**Zusammenfassung des ISO/IEC 27002:2022-Leitfadens**:

- Einfache, zugängliche und gut kommunizierte Meldekanäle
- Mehrere Meldeoptionen verfügbar
- Klare Definition meldepflichtiger Ereignisse mit Beispielen
- Meldung in Sicherheitsschulungen einbeziehen
- Nicht-strafende Meldeumgebung
- Systemänderungen, die nicht über das Change-Control-Verfahren verarbeitet wurden (NEU in 2022)
- Vermutete Malware-Infektion (NEU in 2022)
- Mitarbeitende DÜRFEN NICHT versuchen, Schwachstellen selbst zu verifizieren

## Begründung des kombinierten Kontroll-Rahmenwerks

[Organisation] implementiert diese beiden Controls als einheitliches Rahmenwerk, da sie komplementäre Aspekte der Sicherheitsverantwortlichkeiten des Personals darstellen:

**Operative Integration**:

- Remote-Arbeitssicherheit (A.6.7) schafft die Schutzumgebung
- Ereignismeldung (A.6.8) ermöglicht Erkennung, wenn der Schutz versagt
- Remote-Mitarbeitende benötigen von jedem Standort aus zugängliche Meldekanäle
- Ereigniskategorien umfassen Remote-spezifische Szenarien (VPN-Probleme, Gerätediebstahl, verdächtige Netzwerkaktivität)

**Implementierungssynergie**:

- Gemeinsame Schulungsmodule zu Remote-Sicherheit und Ereignismeldung
- Kombinierte Richtlinienbestätigung beim Onboarding
- Einheitliche Nachweissammlung (Schulungsaufzeichnungen, Bestätigungen, Sensibilisierungsmaterialien)
- Einheitliches Governance-Rahmenwerk mit konsistenten Überprüfungszyklen

**Warum eine getrennte Implementierung weniger wirksam wäre**:

- Remote-Mitarbeitende ohne Kenntnisse zur Ereignismeldung schaffen Erkennungslücken
- Von Remote-Standorten aus nicht zugängliche Meldekanäle verzögern die Reaktion
- Fragmentierte Schulungen erhöhen die Belastung und verringern die Behaltensquote
- Separate Richtlinien erzeugen Verwirrung über Verantwortlichkeiten

## Was diese Richtlinie regelt

Diese Richtlinie:

- **Definiert** Anforderungen für sichere Remote-Arbeitsvereinbarungen
- **Legt fest** Autorisierungsanforderungen für Remote-Arbeit
- **Spezifiziert** Anforderungen an die physische Sicherheit für Remote-Arbeitsumgebungen
- **Verpflichtet** zu technischen Sicherheitskontrollen für Remote-Zugang
- **Definiert** Datenverwaltungsanforderungen im Remote-Arbeitskontext
- **Etabliert** Mechanismen und Kanäle für die Meldung von Sicherheitsereignissen
- **Spezifiziert** was ein meldepflichtiges Sicherheitsereignis darstellt
- **Verpflichtet** zu zeitnaher Meldung und einer nicht-strafenden Kultur
- **Weist zu** Verantwortlichkeiten für Remote-Arbeit-Governance und Ereignisreaktion
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00
- **Integriert** mit verwandten Controls (Endpunktsicherheit, Incident Management, Zugangskontrolle)

## Was diese Richtlinie nicht regelt

Diese Richtlinie regelt NICHT:

- **Technische VPN-Konfigurationsverfahren** (siehe ISMS-IMP-A.6.7-8.S2)
- **Schritt-für-Schritt-MFA-Einrichtungsanweisungen** (herstellerspezifisch, siehe IT-Verfahren)
- **Formulare zur Genehmigung von Remote-Arbeit** (siehe Anhang-Vorlagen)
- **Incident-Response-Verfahren im Detail** (siehe ISMS-POL-A.5.24-28)
- **Endpunkt-Härtungsverfahren** (siehe ISMS-POL-A.8.1-7-18-19)
- **HR-Richtlinien zur Remote-Arbeit** (Eignung, Zeitplanung – HR-Bereich)
- **Lokale Arbeitsrechtsverpflichtungen** (ergänzt bestehendes HR-Rahmenwerk)
- **Ereignis-Triage-Verfahren** (siehe ISMS-IMP-A.6.7-8.S4)

**Begründung**: Die Trennung von Richtlinienanforderungen und Implementierungsleitfaden ermöglicht:

- Richtlinienstabilität trotz sich wandelnder Remote-Arbeitstechnologien
- Technische Flexibilität für Plattform- und Tool-Aktualisierungen
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Implementierung)
- Organisationsunabhängigen Ansatz, anwendbar auf jede ISMS-Implementierung

## Geltungsbereich

**Diese Richtlinie gilt für**:

**Personal**:

- Alle Mitarbeitenden, die remote arbeiten (vollzeit, teilzeit, gelegentlich)
- Alle Auftragnehmer und Berater, die von Nicht-[Organisation]-Räumlichkeiten aus arbeiten
- Alle Drittanbieter-Mitarbeitenden mit Remote-Zugang zu den Systemen von [Organisation]
- Alle geschäftlich reisenden Mitarbeitenden, die auf organisatorische Ressourcen zugreifen
- Alle Mitarbeitenden, die Sicherheitsereignisse beobachten oder melden könnten

**Remote-Arbeitsvereinbarungen**:

- Heimarbeit (regelmässig oder gelegentlich)
- Arbeit von Co-Working-Spaces oder gemeinsamen Büros
- Arbeit von Kunden- oder Partnerräumlichkeiten aus
- Arbeit während Reisen (Hotels, Flughäfen, öffentliche Räume)
- Jede Arbeit ausserhalb der kontrollierten Räumlichkeiten von [Organisation]

**Geräte und Ausrüstung**:

- Unternehmenseigene Laptops, Tablets und Mobilgeräte
- Persönliche Geräte für die Arbeit (BYOD), wo erlaubt
- Tragbare Speichermedien mit organisatorischen Daten
- Kommunikationsgeräte, die für organisatorische Zwecke verwendet werden

**Informationen und Systeme**:

- Alle remote zugegriffenen organisatorischen Daten
- Alle über Remote-Verbindungen zugegriffenen organisatorischen Systeme
- Alle Kommunikationen mit organisatorischen Informationen
- Alle ausserhalb der Räumlichkeiten von [Organisation] verarbeiteten Dokumente und Materialien

**Ausserhalb des Geltungsbereichs**:

- Arbeit vor Ort in den kontrollierten Einrichtungen von [Organisation]
- Persönliche Aktivitäten auf persönlichen Geräten ohne organisatorische Daten
- HR-Aspekte von Remote-Arbeit (Eignung, Work-Life-Balance, Zeitplanung)
- Vergütungs- und Ausgabenrichtlinien (separater HR-Bereich)

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)** kategorisiert.

**Tier 1: Obligatorische Compliance**

| Regulierung | Anwendbarkeit | Kernanforderungen |
|-------------|---------------|-------------------|
| **Schweizerisches nDSG** | Alle Schweizer Operationen | Art. 8 – Angemessene technische und organisatorische Massnahmen für Datenschutz in Remote-Umgebungen |
| **EU-DSGVO** | Bei Verarbeitung personenbezogener EU-Daten | Art. 32 – Sicherheit der Verarbeitung muss sich auf Remote-Arbeit erstrecken; Art. 33 – Datenpannen-Meldung innerhalb von 72 Stunden erfordert zeitnahe Ereigniserkennung |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Controls A.6.7 (Remote-Arbeit), A.6.8 (Ereignismeldung) |

**Tier 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | Anforderungen an Remote-Arbeit/Meldung |
|-------------|------------------|---------------------------------------|
| **NIS2-Richtlinie** | Wesentliche/wichtige Einrichtung (EU) | Art. 21 – Cybersicherheitspraktiken einschliesslich Remote-Zugangs-Sicherheit; Art. 23 – Vorfallmeldung innerhalb von 24 Stunden |
| **DORA** | EU-Finanzdienstleistungseinheit | Art. 9 – IKT-Sicherheitsanforderungen erstrecken sich auf Remote-Zugang; Art. 19 – Vorfallmeldung an zuständige Behörden |
| **FINMA-Rundschreiben 2008/21** | Schweizerisch reguliertes Finanzinstitut | Remote-Zugangskontrollen, Vorfallmeldung an FINMA |
| **PCI DSS v4.0.1** | Verarbeitung von Zahlungskartendaten | Req. 12.3.1 – Remote-Zugangs-Sicherheit; Req. 12.10 – Incident Response |

**Tier 3: Informationsleitfaden**

Diese Rahmenwerke informieren die Implementierung, stellen aber keine obligatorische Compliance dar, sofern nicht vertraglich gefordert:

- NIST SP 800-46 Rev 2 – Leitfaden für Unternehmens-Telearbeit, Remote-Zugang und BYOD-Sicherheit
- NIST SP 800-61 Rev 2 – Leitfaden zur Behandlung von Computersicherheitsvorfällen
- CIS Controls v8.1 – Control 4 (Sichere Konfiguration), Control 17 (Incident Response)
- ENISA – Sicherheitsrichtlinien für Telearbeit

**Compliance-Ermittlung**: [Organisation] ermittelt anwendbare Tier-2-Regulierungen durch periodische Geschäftsaktivitätsbewertungen gemäss ISMS-POL-00. Bei Überschneidungen mehrerer Regulierungen gelten die strengsten Anforderungen.

---

# Anforderungen an Remote-Arbeit (Control A.6.7)

## Autorisierung von Remote-Arbeit

[Organisation] MUSS einen formalen Autorisierungsprozess für Remote-Arbeitsvereinbarungen etablieren.

**2.1.1 Autorisierungsanforderungen**

| Anforderung | Beschreibung |
|-------------|-------------|
| **Formale Genehmigung** | Alle regulären Remote-Arbeitsvereinbarungen MÜSSEN vor Beginn formal genehmigt werden |
| **Autorisierungsbefugnis** | Linienvorgesetzte autorisieren Remote-Arbeit; IT-Sicherheit genehmigt technischen Zugang |
| **Risikobeurteilung** | Risikobeurteilung MUSS für Rollen durchgeführt werden, die remote sensible Daten verarbeiten |
| **Risikobeurteilungskriterien** | Beurteilung MUSS mindestens bewerten: (a) Klassifizierungsniveau remote zugegriffener Daten (gemäss A.5.12); (b) Physische Sicherheitsfähigkeit des Remote-Standorts; (c) Netzwerksicherheitslage; (d) Geräte-Sicherheitsbasislinien-Compliance; (e) Regulatorische oder vertragliche Einschränkungen |
| **Verifizierung der Risikobeurteilung** | Angemessenheit der Beurteilung wird durch dokumentierte Kriterien gemäss der organisatorischen Risikomethorik verifiziert (gemäss A.5.7). Detaillierte Beurteilungsverfahren in ISMS-IMP-A.6.7-8.S1 |
| **Dokumentierte Vereinbarung** | Remote-Mitarbeitende MÜSSEN Sicherheitsanforderungen für Remote-Arbeit bestätigen |
| **Periodische Überprüfung** | Remote-Arbeitsautorisierungen MÜSSEN mindestens jährlich überprüft werden |

**2.1.2 Autorisierungskriterien**

Die Autorisierung von Remote-Arbeit MUSS berücksichtigen:

- Eignung der Rolle für Remote-Arbeit
- Datenklassifizierung der zugegriffenen Informationen
- Technische Fähigkeit zur Herstellung sicherer Remote-Verbindungen
- Eignung der physischen Umgebung (Privatsphäre, Sicherheit)
- Regulatorische oder vertragliche Einschränkungen
- Anforderungen an die Geschäftskontinuität

**2.1.3 Widerruf**

Die Remote-Arbeitsautorisierung MUSS widerrufen werden, wenn:

- Das Beschäftigungs- oder Vertragsverhältnis endet
- Die Rolle in eine für Remote-Arbeit ungeeignete Rolle wechselt
- Sicherheitsanforderungen nicht eingehalten werden
- Richtlinienverstösse auftreten
- Geschäftliche Anforderungen die Anwesenheit vor Ort verlangen

## Anforderungen an die physische Sicherheit

[Organisation] MUSS Anforderungen an die physische Sicherheit für Remote-Arbeitsumgebungen definieren.

**2.2.1 Arbeitsplatzanforderungen**

Remote-Mitarbeitende MÜSSEN:

- Bildschirme so positionieren, dass ein unbefugtes Einsehen durch andere verhindert wird
- Sichtschutzfilter verwenden, wenn in gemeinsam genutzten oder öffentlichen Räumen gearbeitet wird
- Arbeitsgeräte sichern, wenn der Arbeitsplatz unbeaufsichtigt ist
- Den Zugang zu Arbeitsgeräten durch Familienmitglieder, Besucher oder andere unbefugte Personen verhindern
- Sensible Dokumente sicher aufbewahren, wenn sie nicht aktiv verwendet werden
- Sensible Dokumente mit genehmigten Methoden vernichten (Aktenvernichtung)

**Verifizierung**: Die Compliance mit der physischen Sicherheit wird durch jährliche Selbstbeurteilungs-Checklisten, ausgelöste Neubewertungen nach Sicherheitsereignissen oder wesentlichen Arbeitsplatzänderungen oder durch Bestätigung bei der Autorisierungserneuerung verifiziert.

**2.2.2 Gerätesicherheit**

Remote-Mitarbeitende MÜSSEN:

- Tragbare Geräte physisch sichern (Kabelschlösser, sichere Aufbewahrung)
- Geräte nie unbeaufsichtigt in öffentlichen Räumen lassen
- Geräte beim Verlassen des Platzes sperren, auch kurzzeitig
- Verlorene oder gestohlene Geräte sofort melden (siehe Abschnitt 3)
- Geräte sicher zwischen Standorten transportieren

**2.2.3 Anforderungen für aufgeräumten Schreibtisch**

Die Richtlinie für aufgeräumten Schreibtisch (gemäss A.7.7) MUSS sich auf Remote-Arbeitsumgebungen erstrecken:

- Sensible Dokumente DÜRFEN NICHT sichtbar sein, wenn sie nicht aktiv verwendet werden
- Arbeitsmaterialien MÜSSEN am Ende jeder Arbeitssitzung gesichert werden
- Gedruckte Materialien MÜSSEN sicher aufbewahrt oder angemessen vernichtet werden

## Technische Sicherheitsanforderungen

[Organisation] MUSS technische Sicherheitskontrollen für den gesamten Remote-Zugang verpflichtend vorschreiben.

**2.3.1 Anforderungen an sichere Verbindungen**

| Anforderung | Obligatorisch für |
|-------------|-------------------|
| **VPN oder Zero-Trust-Zugang** | Alle Verbindungen zu internen Ressourcen |
| **Multi-Faktor-Authentifizierung (MFA)** | Alle Remote-Zugänge zu organisatorischen Systemen |
| **Verschlüsselte Kommunikation** | Alle Datenübertragungen (mindestens TLS 1.2) |
| **Unternehmens-DNS** | Auflösung über organisatorischen DNS bei Verbindung |

**2.3.2 Authentifizierungsanforderungen**

Remote-Zugang-Authentifizierung MUSS erfordern:

- Multi-Faktor-Authentifizierung (MFA) für alle Systemzugänge
- Starke Passwörter gemäss der organisatorischen Passwortrichtlinie (A.5.17)
- Keine Weitergabe oder Speicherung von Anmeldeinformationen an unsicheren Orten
- Sofortige Passwortänderung bei vermutetem Kompromittierungsfall
- Sitzungs-Timeout nach Inaktivitätszeitraum

**2.3.3 Netzwerksicherheitsanforderungen**

Remote-Mitarbeitende MÜSSEN:

- Nur sichere, verschlüsselte drahtlose Netzwerke verwenden (mindestens WPA2/WPA3)
- Öffentliches, ungesichertes WLAN für organisatorische Arbeit ohne VPN-Schutz vermeiden
- Sicherheitskontrollen nicht deaktivieren oder umgehen
- Netzwerksicherheitsbedenken oder -anomalien melden

**Verifizierung**: Die Compliance mit Netzwerksicherheit kann durch Endpunktverwaltungs-Telemetrie (Netzwerk-SSID, Verschlüsselungstyp, VPN-Verbindungsstatus, Zertifikatsgültigkeit), VPN-Verbindungsdurchsetzung oder Benutzerbestätigung bei periodischen Überprüfungen überwacht werden. Wo Telemetrie technisch nicht machbar ist, bietet die Benutzerbestätigung bei der Autorisierungserneuerung angemessene Sicherheit.

## Datenverwaltungsanforderungen

[Organisation] MUSS Datenverwaltungsanforderungen für Remote-Arbeitskontexte definieren.

**2.4.1 Compliance mit der Datenklassifizierung**

Remote-Mitarbeitende MÜSSEN:

- Daten gemäss ihrem Klassifizierungsniveau verarbeiten (gemäss A.5.12–13)
- Eingeschränkte Daten nicht remote verarbeiten, sofern nicht ausdrücklich autorisiert
- Angemessenen Schutz für vertrauliche Daten anwenden
- Sichere Informationsübertragungs-Verfahren befolgen (gemäss A.5.14)

**2.4.2 Datenspeicherungsanforderungen**

| Datenklassifizierung | Remote-Speicherung erlaubt | Bedingungen |
|---------------------|---------------------------|-------------|
| **Öffentlich** | Ja | Standard-Gerätesicherheit |
| **Intern** | Ja | Verschlüsseltes Gerät, sicherer Standort |
| **Vertraulich** | Bedingt | Verschlüsselt, nur genehmigte Geräte, geschäftliche Begründung |
| **Eingeschränkt** | Nein (Standard) | Erfordert ausdrückliche ISB-Genehmigung, erweiterte Kontrollen |

**Bedingter Autorisierungsprozess**: Remotespeicherung vertraulicher Daten erfordert: (a) Schriftliche geschäftliche Begründung vom Linienvorgesetzten; (b) Verifizierung der technischen Kontrollen (Geräteverschlüsselung, sicherer Speicherort); (c) Genehmigung durch IT-Sicherheitsmanager. Eingeschränkte Daten erfordern schriftliche ISB-Genehmigung mit dokumentierten kompensierenden Kontrollen. Alle Genehmigungen MÜSSEN im Ausnahmenregister (Abschnitt 5.4) erfasst werden.

**2.4.3 Datensicherung**

Remote-Mitarbeitende MÜSSEN:

- Arbeitsdateien in genehmigten Cloud- oder Netzwerkstandorten speichern
- Sich für kritische Daten nicht ausschliesslich auf lokale Gerätespeicherung verlassen
- Organisatorische Backup-Richtlinien befolgen

## Geräte- und Ausrüstungssicherheit

[Organisation] MUSS Sicherheitsanforderungen für bei Remote-Arbeit verwendete Geräte definieren.

**2.5.1 Anforderungen an unternehmenseigene Geräte**

Für Remote-Arbeit verwendete unternehmenseigene Geräte MÜSSEN:

- Gemäss der organisatorischen Sicherheitsbasislinie konfiguriert sein (gemäss A.8.9)
- Volle Festplattenverschlüsselung aktiviert haben
- Aktuelle Endpunktschutzsoftware haben (gemäss A.8.7)
- Gemäss dem organisatorischen Zeitplan gepatcht und aktualisiert sein (gemäss A.8.8)
- Remote-Wipe-Fähigkeit aktiviert haben
- Im Geräteinventar registriert sein (gemäss A.5.9)

**2.5.2 Anforderungen an persönliche Geräte (BYOD)**

Wo persönliche Geräte für organisatorische Arbeit erlaubt sind, MÜSSEN sie:

- Von IT-Sicherheit definierte Mindestsicherheitsanforderungen erfüllen
- Organisatorische MDM/EMM-Lösung installiert haben (falls erforderlich)
- Trennung zwischen persönlichen und Arbeitsdaten aufrechterhalten (Containerisierung)
- Remote-Löschung organisatorischer Daten bei Kündigung ermöglichen
- Keine organisatorischen Daten nach Sperrung des Zugangs aufbewahren

**2.5.3 Verbotene Geräte**

Folgendes DARF NICHT für organisatorische Arbeit verwendet werden:

- Gejailbreakte oder gerootete Geräte
- Geräte mit deaktivierten Sicherheitsfunktionen
- Gemeinsam genutzte Geräte, die nicht unter der Kontrolle des Benutzers stehen
- Geräte, die Sicherheitsanforderungen nicht erfüllen können
- Geräte, auf denen End-of-Life-Betriebssysteme ohne Sicherheitsaktualisierungen laufen
- Geräte, die Dritten gehören oder von ihnen kontrolliert werden, die nicht den organisatorischen Sicherheitsrichtlinien unterliegen

## Beendigung von Remote-Arbeit

[Organisation] MUSS Anforderungen für die Beendigung von Remote-Arbeitsvereinbarungen definieren.

**2.6.1 Zugangssperrung**

Bei Beendigung der Remote-Arbeitsautorisierung:

- Remote-Zugangsdaten MÜSSEN sofort gesperrt werden
- VPN- und Remote-Zugangs-Token MÜSSEN deaktiviert werden
- Zugang zu remote zugänglichen Systemen MUSS überprüft und entfernt werden

**2.6.2 Geräterückgabe**

Bei Beendigung des Beschäftigungs- oder Vertragsverhältnisses:

- Alle organisatorischen Geräte MÜSSEN gemäss A.5.11 zurückgegeben werden
- Alle organisatorischen Daten MÜSSEN von persönlichen Geräten entfernt werden
- Rückgabe MUSS verifiziert und dokumentiert werden

---

# Anforderungen an die Sicherheitsereignismeldung (Control A.6.8)

## Meldemechanismen

[Organisation] MUSS zugängliche Mechanismen für die Meldung von Sicherheitsereignissen bereitstellen.

**3.1.1 Anforderungen an Meldekanäle**

| Anforderung | Beschreibung |
|-------------|-------------|
| **Mehrere Kanäle** | Mindestens zwei verschiedene Meldekanäle MÜSSEN verfügbar sein |
| **24/7-Verfügbarkeit** | Mindestens ein Kanal MUSS ausserhalb der Geschäftszeiten verfügbar sein |
| **Remote-Zugänglichkeit** | Alle Kanäle MÜSSEN von Remote-Standorten aus zugänglich sein |
| **Klare Kontaktinformationen** | Meldekontakte MÜSSEN deutlich publiziert sein |
| **Bestätigung** | Alle Meldungen MÜSSEN innerhalb definierter Zeitrahmen bestätigt werden |

**Verifizierung**: Kanalverfügbarkeit wird durch vierteljährliche Tests der Meldekanäle (E-Mail, Telefon, Ticketing), jährliche Incident-Response-Übungen zur Verifizierung der Kanalzugänglichkeit oder kontinuierliche automatisierte Überwachung, wo technisch machbar, verifiziert.

**3.1.2 Standardmässige Meldekanäle**

[Organisation] MUSS die folgenden Meldekanäle aufrechterhalten:

- **Sicherheits-E-Mail**: Dedizierte E-Mail-Adresse für Sicherheitsereignismeldungen
- **Telefon/Hotline**: Kontaktnummer für dringende Sicherheitsangelegenheiten
- **Ticketing-System**: Formelle Ticketeinreichung für nicht dringende Ereignisse
- **Anonyme Option**: Mechanismus für anonyme Meldungen, wo angemessen

**Anonyme Meldung**: Anonyme Meldung MUSS unterstützt werden durch: (a) Dediziertes E-Mail-Alias, das keine Authentifizierung erfordert; (b) Webformular, das ohne Login zugänglich ist; oder (c) Drittanbieter-Hotline, falls implementiert. **Einschränkungen**: Anonyme Meldung kann Rückfragen und detailliertes Feedback ausschliessen. Melder werden ermutigt, Kontaktinformationen bereitzustellen, wo sie sich wohl fühlen, mit Vertraulichkeitszusicherung gemäss Abschnitt 3.4.1.

**3.1.3 Zugänglichkeit von Kanälen**

Meldekanäle MÜSSEN:

- Im Intranet publiziert und in Sicherheitsschulungsmaterialien aufgenommen sein
- In Onboarding-Materialien für Mitarbeitende aufgenommen sein
- In Gemeinschaftsbereichen und auf Anmeldebildschirmen angezeigt werden
- Ohne Systemzugang zugänglich sein (zur Meldung von Zugriffsproblemen)

## Meldepflichtige Ereignisse

[Organisation] MUSS definieren, was ein meldepflichtiges Sicherheitsereignis darstellt.

**3.2.1 Unterscheidung Ereignis vs. Vorfall**

| Begriff | Definition |
|---------|------------|
| **Sicherheitsereignis** | Ein identifiziertes Vorkommen, das auf eine *mögliche* Richtlinienverletzung oder Kontrollversagen hinweist |
| **Sicherheitsvorfall** | Ein Ereignis, das als *signifikante Wahrscheinlichkeit* eingestuft wurde, den Betrieb zu kompromittieren oder die Sicherheit zu bedrohen |

**Mitarbeitende melden EREIGNISSE. Das Sicherheitsteam beurteilt, ob Ereignisse VORFÄLLE darstellen.**

**3.2.2 Kategorien meldepflichtiger Ereignisse**

Mitarbeitende MÜSSEN die folgenden Ereigniskategorien melden:

**Phishing und Social Engineering**:

- Verdächtige E-Mails, die nach Anmeldeinformationen oder sensiblen Informationen fragen
- Verdächtige Telefonanrufe oder Textnachrichten
- Versuchte Manipulation zur Umgehung von Sicherheitskontrollen

**Schadsoftware und Systemkompromittierung**:

- Unerwartetes Systemverhalten oder Leistungsprobleme
- Verdächtige Pop-ups, Nachrichten oder Benachrichtigungen
- Vermutete Malware-Infektion (NEU in ISO 27002:2022)
- Ransomware-Indikatoren

**Unbefugter Zugang**:

- Unbekannte oder unerwartete Anmeldeversuche bei Ihren Konten
- Unbekannte Geräte, die in Ihren Konten angemeldet sind
- Unerwartete Kontosperrungen oder Passwortänderungen
- Verdächtige Privilegiensänderungen

**Datenpannen und -lecks**:

- Fehlgeleitete E-Mails mit sensiblen Informationen
- Unbefugter Datenzugriff oder -exposition
- Verlorene oder gestohlene Dokumente mit organisatorischen Daten
- Vermutete Datenexfiltration

**Physische Sicherheit**:

- Verlorene oder gestohlene Geräte (Laptops, Telefone, USB-Laufwerke)
- Tailgating oder unbefugter physischer Zutritt
- Fehlende Ausrüstung
- Verdächtige Personen in sicheren Bereichen

**Richtlinienverstösse**:

- Beobachtete Umgehung von Sicherheitskontrollen
- Bekannte Sicherheitsrichtlinienverstösse durch andere
- Systemänderungen, die nicht über das Change-Control-Verfahren verarbeitet wurden (NEU in ISO 27002:2022)

**Remote-Arbeit-spezifisch**:

- Vermutete Kompromittierung des Heimnetzwerks
- Unbefugter Zugang zu Arbeitsgeräten durch andere Personen
- VPN- oder Remote-Zugangs-Probleme, die auf einen Angriff hindeuten
- Verdächtige Aktivitäten beim Arbeiten von öffentlichen Orten aus
- Versuche, über nicht genehmigte Geräte auf organisatorische Systeme zuzugreifen
- Verdächtige IT-Support-Anfragen nach Remote-Zugangsdaten
- Konfigurationsänderungen am Heimrouter, die nicht vom Benutzer initiiert wurden
- Physische Beobachtung von Arbeitsmaterialien durch unbefugte Personen

## Meldeverfahren

[Organisation] MUSS klare Meldeverfahren definieren.

**3.3.1 Was zu melden ist**

Meldungen MÜSSEN enthalten (soweit bekannt):

- Datum und Uhrzeit der Beobachtung
- Beschreibung des Ereignisses
- Möglicherweise betroffene Systeme oder Vermögenswerte
- Bereits ergriffene Massnahmen (falls vorhanden)
- Kontaktinformationen für Rückfragen (sofern nicht anonym)
- Allfällige Belege (Screenshots, E-Mail-Header)

**3.3.2 Meldezeitpunkt**

| Ereignisschwere | Meldefrist |
|-----------------|------------|
| **Kritisch** (aktiver Angriff, Datenpanne, Ransomware) | Sofort |
| **Hoch** (verlorenes Gerät, Kompromittierung von Anmeldeinformationen) | Innerhalb von 1 Stunde |
| **Mittel** (Phishing-Versuch, verdächtige Aktivität) | Innerhalb von 4 Stunden |
| **Niedrig** (Richtlinienbedenken, allgemeine Beobachtung) | Innerhalb von 24 Stunden |

**Schweregrad-Bestimmung**: Melder MÜSSEN basierend auf ihrer besten Einschätzung des Schweregrades melden. Wenn Unsicherheit zwischen Schweregraden besteht, beim höheren Schweregrad melden, um eine zeitnahe Reaktion sicherzustellen. Das IT-Sicherheitsteam bewertet den Schweregrad während des ersten Triage neu. Melder DÜRFEN die Meldung nicht verzögern, um die genaue Klassifizierung zu bestimmen.

**3.3.3 Verantwortlichkeiten des Melders**

Meldendes Personal MUSS:

- Zeitnah gemäss den obigen Zeitrahmen melden
- Soweit bekannt genaue Informationen bereitstellen
- Potenzielle Beweise sichern: bei Phishing-E-Mails als Anhang weiterleiten, um Header zu erhalten (nicht im Textkörper weiterleiten oder auf Links klicken); bei Systemanomalien Fehlermeldungen screenshoten und genaue Zeit sowie betroffene Systeme notieren; bei physischen Sicherheitsereignissen fotografieren, wenn sicher möglich. Niemals die persönliche Sicherheit zur Beweissammlung gefährden
- NICHT versuchen, das Ereignis selbst zu untersuchen oder zu verifizieren
- NICHT versuchen, vermutete Schwachstellen zu testen oder auszunutzen
- Mit allfälligen Folgeuntersuchungen kooperieren

## Nicht-strafende Kultur

[Organisation] MUSS eine nicht-strafende Umgebung für die Meldung von Sicherheitsereignissen fördern.

**3.4.1 Grundsätze der nicht-strafenden Kultur**

| Grundsatz | Zusage |
|-----------|--------|
| **Gutgläubigkeitsschutz** | Mitarbeitende, die Ereignisse in gutem Glauben melden, DÜRFEN keine negativen Konsequenzen für den Meldungsakt selbst erfahren |
| **Umgang mit ehrlichen Fehlern** | Ehrliche Fehler, die zeitnah gemeldet werden, MÜSSEN konstruktiv behandelt werden, mit Fokus auf Lernen und Verbesserung |
| **Keine Vergeltung** | Vergeltungsmassnahmen gegen gutgläubige Melder sind verboten und unterliegen Disziplinarmassnahmen |
| **Vertraulichkeit** | Die Identität des Melders MUSS so weit wie möglich geschützt werden |

**3.4.2 Förderung der Meldung**

[Organisation] MUSS:

- Mitarbeitende anerkennen, die vorbildliches Meldeverhalten zeigen
- Gemeldete Ereignisse als Lernmöglichkeiten nutzen, nicht als Auslöser für Bestrafungen
- Den Wert der Meldung durch Bewusstseinsprogramme kommunizieren
- Feedback zu gemeldeten Ereignissen geben, um zu zeigen, dass Massnahmen ergriffen werden

**Verifizierung**: Die Wirksamkeit der nicht-strafenden Kultur kann durch Trends beim Meldevolumen (rückläufige Volumina können auf Angst vor Konsequenzen hinweisen und eine Kulturüberprüfung auslösen), anonyme Mitarbeiterbefragungen zur Meldebereitschaft oder Analyse von Zeit-bis-Meldung-Metriken bewertet werden.

**3.4.3 Ausnahmen**

Grundsätze der nicht-strafenden Kultur schützen NICHT:

- Vorsätzliche Richtlinienverstösse, die erst nach Entdeckung gemeldet werden
- Böswillige Aktivitäten, die als versehentlich getarnt sind
- Wiederholte Fahrlässigkeit nach Schulungen und Verwarnungen
- Falschmeldungen in böser Absicht

## Reaktion und Feedback

[Organisation] MUSS auf Sicherheitsereignismeldungen reagieren.

**3.5.1 Reaktionszeitrahmen**

| Reaktionstyp | Zeitrahmen |
|--------------|------------|
| **Bestätigung** | Innerhalb von 4 Geschäftsstunden |
| **Erstbeurteilung** | Innerhalb von 24 Stunden |
| **Statusaktualisierung an Melder** | Innerhalb von 72 Stunden |
| **Abschlussbenachrichtigung** | Bei Lösung |

**Verifizierung**: Compliance mit Reaktionszeitrahmen wird durch Ticketing-System-Metriken, Berichterstattungs-Dashboards oder periodische Compliance-Audits gemessen.

**3.5.2 Feedback an Melder**

[Organisation] MUSS:

- Den Empfang aller Meldungen bestätigen
- Statusaktualisierungen zu gemeldeten Ereignissen bereitstellen
- Ergebnisse kommunizieren, wo angemessen und erlaubt
- Erkenntnisse nutzen, um den Meldeprozess zu verbessern
- Melder für ihren Beitrag zur organisatorischen Sicherheit danken

**3.5.3 Eskalation**

Ereignisse MÜSSEN gemäss ISMS-POL-A.5.24-28 (Incident-Management-Lebenszyklus) eskaliert werden, wenn:

- Das Ereignis als bestätigter Sicherheitsvorfall eingestuft wird
- Das Ereignis Ressourcen jenseits des ersten Reaktionsteams erfordert
- Das Ereignis regulatorische Meldepflichten hat
- Das Ereignis mehrere Systeme oder Geschäftsbereiche betrifft

---

# Rollen und Verantwortlichkeiten

## Verantwortlichkeitsmatrix

| Rolle | Remote-Arbeit (A.6.7) | Ereignismeldung (A.6.8) |
|-------|-----------------------|------------------------|
| **Unternehmensleitung** | Remote-Arbeit-Richtlinie genehmigen; Ressourcen bereitstellen | Nicht-strafende Kultur fördern; kritische Vorfallbriefings erhalten |
| **ISB** | Sicherheitsanforderungen definieren; Ausnahmen autorisieren; Compliance überprüfen | Meldemechanismen definieren; Reaktion überwachen; an Management berichten |
| **IT-Sicherheitsteam** | Technische Kontrollen implementieren; Compliance überwachen; Risiken beurteilen | Meldungen empfangen; Ereignisse beurteilen; Reaktion koordinieren; Feedback geben |
| **IT Operations** | Remote-Zugang bereitstellen; VPN/MFA aufrechterhalten; Geräte unterstützen | Meldekanäle unterstützen; Eindämmungsmassnahmen implementieren |
| **HR** | Remote-Arbeitsvereinbarungen verwalten; Kündigungen koordinieren | Meldung im Onboarding einschliessen; personalbedingte Vorfälle adressieren |
| **Linienvorgesetzte** | Remote-Arbeit autorisieren; Team-Compliance sicherstellen | Meldung fördern; Team-Bedenken eskalieren |
| **Alle Mitarbeitenden** | Remote-Arbeitsanforderungen einhalten; Geräte und Daten sichern | Ereignisse zeitnah melden; Beweise sichern; mit Untersuchungen kooperieren |

## Wichtige Rollendefinitionen

**4.2.1 ISB (Informationssicherheitsbeauftragter)**

Verantwortlichkeiten:

- Gesamtverantwortung für die Remote-Arbeitssicherheitsrichtlinie
- Hochrisiko-Remote-Arbeitsvereinbarungen genehmigen
- Ereignismeldemechanismen und -verfahren definieren
- Sicherstellen, dass Meldekanäle zugänglich und wirksam sind
- Bedeutende Ereignisse an die Unternehmensleitung melden
- Remote-Arbeit- und Meldeprogramme überprüfen und verbessern

**4.2.2 IT-Sicherheitsteam**

Verantwortlichkeiten:

- Remote-Zugangs-Sicherheitskontrollen implementieren und aufrechterhalten
- Remote-Zugang auf Anomalien überwachen
- Sicherheitsereignismeldungen empfangen und beurteilen
- Incident Response gemäss A.5.24-28 koordinieren
- Feedback an Melder geben
- Sicherheitsereignisdokumentation pflegen
- Periodische Überprüfungen der Remote-Arbeitssicherheit durchführen

**4.2.3 Linienvorgesetzte**

Verantwortlichkeiten:

- Remote-Arbeit für Teammitglieder autorisieren
- Sicherstellen, dass Teammitglieder Remote-Arbeitsanforderungen verstehen
- Eine Kultur des Sicherheitsbewusstseins und der Meldung fördern
- Sicherheitsbedenken an IT-Sicherheit eskalieren
- Nichterfüllung innerhalb ihrer Teams adressieren
- Untersuchungen bei Bedarf unterstützen

**4.2.4 Alle Mitarbeitenden**

Verantwortlichkeiten:

- Autorisierung einholen, bevor remote gearbeitet wird
- Alle Sicherheitsanforderungen für Remote-Arbeit einhalten
- Physische und technische Sicherheit der Arbeitsumgebung aufrechterhalten
- Sicherheitsereignisse zeitnah über die designierten Kanäle melden
- Beweise sichern und mit Untersuchungen kooperieren
- Erforderliche Sicherheitsschulungen abschliessen
- Diese Richtlinie bestätigen und einhalten

---

# Governance und Compliance

## Richtlinienüberprüfung

| Aspekt | Anforderung |
|--------|-------------|
| **Überprüfungshäufigkeit** | Jährlich oder bei wesentlichen Änderungen |
| **Überprüfungsbehörde** | ISB mit Genehmigung der Unternehmensleitung |
| **Ausgelöste Überprüfungen** | Bedeutender Sicherheitsvorfall, regulatorische Änderung, Technologieänderung, organisatorische Umstrukturierung |
| **Überprüfungsumfang** | Richtlinienwirksamkeit, Compliance-Metriken, Vorfalltrends, regulatorische Ausrichtung |

## Compliance-Überwachung

[Organisation] MUSS die Compliance mit dieser Richtlinie überwachen durch:

**Remote-Arbeit-Compliance**:

- Periodische Überprüfung der Remote-Arbeitsautorisierungen
- Technische Compliance-Prüfungen (VPN-Nutzung, MFA-Status, Geräteverschlüsselung)
- Sicherheitsbasislinien-Bewertungen für Remote-Geräte
- Audit von Remote-Zugangs-Protokollen

**Ereignismelde-Compliance**:

- Nachverfolgung der Verfügbarkeit von Meldekanälen
- Analyse von Ereignismelde-Metriken
- Überprüfung von Reaktionszeitrahmen
- Bewertung des Melder-Feedbacks

## Nichterfüllung

**5.3.1 Konsequenzen der Nichterfüllung**

Verstösse gegen diese Richtlinie können folgende Konsequenzen haben:

- Widerruf der Remote-Arbeit-Privilegien
- Obligatorische zusätzliche Sicherheitsschulung
- Disziplinarmassnahmen gemäss HR-Richtlinien
- Kündigung des Beschäftigungs- oder Vertragsverhältnisses bei schwerwiegenden Verstössen
- Rechtliche Massnahmen bei kriminellen Aktivitäten

**5.3.2 Meldung von Nichterfüllung**

Beobachtete Nichterfüllung MUSS gemeldet werden an:

- Linienvorgesetzten (bei Teamproblemen)
- IT-Sicherheit (bei technischen Verstössen)
- HR (bei Personalangelegenheiten)
- ISB (bei bedeutenden oder wiederholten Verstössen)

## Ausnahmenmanagement

**5.4.1 Ausnahmeprozess**

Ausnahmen von dieser Richtlinie erfordern:

- Dokumentierte geschäftliche Begründung
- Risikobeurteilung der Ausnahme
- Kompensierende Kontrollen, wo anwendbar
- Genehmigung durch ISB (oder Delegiertem)
- Zeitlich begrenzte Dauer mit Überprüfungsdatum
- Dokumentation im Ausnahmenregister

**5.4.2 Ausnahmebefugnis**

| Ausnahmetyp | Genehmigungsbehörde |
|-------------|---------------------|
| Standardausnahmen (geringfügige Abweichungen) | IT-Sicherheitsmanager |
| Hochrisiko-Ausnahmen (sensible Daten, verlängerte Dauer) | ISB |
| Richtlinienverzichte (grundlegende Anforderungen) | Unternehmensleitung |

---

# Integration mit anderen Controls

## ISMS-Integration

Diese Richtlinie integriert sich in das Informationssicherheitsmanagementsystem von [Organisation]:

**Risikobeurteilung** (ISO 27001 Klausel 6.1):

- Remote-Arbeitsrisiken werden als Teil der organisatorischen Risikobeurteilung beurteilt
- Wirksamkeit der Ereignismeldung wird bei der Risikobehandlung bewertet
- Risikobehandlungspläne dokumentieren die Kontrollimplementierung

**Anwendbarkeitserklärung** (ISO 27001 Klausel 6.1.3):

- Anwendbarkeit der Controls A.6.7 und A.6.8 in der Anwendbarkeitserklärung von [Organisation] begründet
- Implementierungsstatus für jeden Control separat verfolgt und gemeldet

## Verwandte Controls

| Control | Beziehung |
|---------|-----------|
| **A.5.1-2-6.1-2** (Sichere Beschäftigung & Rollen) | Personalverantwortlichkeiten, Überprüfung, Beschäftigungsbedingungen |
| **A.5.10** (Zulässige Nutzung) | Definiert zulässige Nutzung von Vermögenswerten einschliesslich Remote-Arbeit-Szenarien |
| **A.5.11** (Rückgabe von Vermögenswerten) | Geräterückgabe bei Beendigung von Remote-Arbeit |
| **A.5.17** (Authentifizierungsinformationen) | Passwort- und Authentifizierungsanforderungen |
| **A.5.24-28** (Incident Management) | Eskalationspfad für Sicherheitsereignisse, die zu Vorfällen werden |
| **A.6.3** (Bewusstsein & Schulung) | Schulung zu Remote-Arbeitssicherheit und Ereignismeldung |
| **A.7.7** (Aufgeräumter Schreibtisch) | Anforderungen für aufgeräumten Schreibtisch erstrecken sich auf Remote-Umgebungen |
| **A.8.1-7-18-19** (Endpunktsicherheit) | Gerätesicherheit, Malware-Schutz für Remote-Geräte |
| **A.8.5** (Sichere Authentifizierung) | MFA und Authentifizierungsanforderungen |
| **A.8.20-22** (Netzwerksicherheit) | VPN und Netzwerksicherheit für Remote-Verbindungen |

## Implementierungsressourcen

**Implementierungsleitfaden** (ISMS-IMP-A.6.7-8-Suite):

- ISMS-IMP-A.6.7-8.S1: Beurteilung der Remote-Arbeitsautorisierung und -Richtlinie
- ISMS-IMP-A.6.7-8.S2: Beurteilung technischer Controls (VPN, MFA, Verschlüsselung)
- ISMS-IMP-A.6.7-8.S3: Endpunkt- und physische Sicherheitsbeurteilung
- ISMS-IMP-A.6.7-8.S4: Beurteilung von Ereignismeldemechanismen

**Beurteilungstools**:

- Excel-basierte Beurteilungs-Workbooks mit automatisierten Compliance-Berechnungen
- Nachweisregister für Audit-Dokumentation
- Lückenanalyse-Vorlagen für Behebungsplanung
- Behebungsverfolgung für Verbesserungsmassnahmen

---

# Nachweise für diese Richtlinie

**Nachweise Stufe 1 (Dokumentenüberprüfung):**

Erforderliche Nachweise zur Demonstration, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.6.7-8 v1.0)
- ✅ Genehmigungsunterschriften von ISB, HR-Direktor, Unternehmensleitung
- ✅ Dokumentiertes Verfahren zur Remote-Arbeitsautorisierung
- ✅ Publizierte Dokumentation der Meldekanäle
- ✅ Schulungsmaterialien zu Remote-Arbeit und Ereignismeldung
- ✅ Ausnahmenregister mit dokumentierten Genehmigungen
- ✅ Zugewiesene Rollen und Verantwortlichkeiten

**Nachweise Stufe 2 (Operative Wirksamkeit):**

Erforderliche Nachweise zur Demonstration, dass diese Richtlinie operativ wirksam ist:

- Remote-Arbeitsautorisierungs-Stichproben (genehmigte Vereinbarungen)
- Richtlinienbestätigungsaufzeichnungen von Mitarbeitenden
- Schulungsabschluss-Aufzeichnungen für Remote-Arbeit-/Meldungsschulung
- Technische Compliance-Berichte (VPN-Nutzung, MFA-Registrierung, Geräteverschlüsselungsstatus)
- Beispiel-Sicherheitsereignismeldungen mit Nachweis der Mechanismusnutzung
- Reaktionsaufzeichnungen mit zeitnaher Reaktion auf gemeldete Ereignisse
- Compliance-Metriken-Dashboard mit Richtlinien-Compliance-Niveaus

**Aufbewahrung von Nachweisen:**

- Richtlinienversionen: ISMS-Laufzeit + 3 Jahre
- Autorisierungsaufzeichnungen: Vereinbarungsdauer + 2 Jahre
- Schulungsaufzeichnungen: Beschäftigungsdauer + 2 Jahre
- Ereignismeldungen: Mindestens 3 Jahre (oder gemäss regulatorischer Anforderung)
- Compliance-Beurteilungen: Mindestens 3 Jahre

---

# Anhang A: Anforderungen an Begleitdokumentation

Diese Richtlinie erfordert die Entwicklung und Pflege der folgenden Begleitdokumentation durch [Organisation]. Dies sind operative Dokumente, die von den jeweiligen Prozessverantwortlichen geführt werden und nicht Teil des Kern-ISMS-Richtlinienrahmenwerks sind.

## A.1 Remote-Arbeit-Dokumentation

| Dokumententyp | Zweck | Eigentümer |
|---------------|-------|------------|
| **Formular zur Remote-Arbeitsautorisierung** | Formale Anforderung und Genehmigung für Remote-Arbeitsvereinbarungen | HR |
| **Sicherheitsbestätigung für Remote-Arbeit** | Bestätigung der Sicherheitsanforderungen durch Mitarbeitende | HR/IT-Sicherheit |
| **Remote-Arbeitsvereinbarung** | Bedingungen für Remote-Arbeitsvereinbarungen | HR/Rechtsbeistand |
| **Selbstbeurteilungs-Checkliste für Heimarbeitsplatzsicherheit** | Checkliste für Mitarbeitende zur Beurteilung der Arbeitsplatzsicherheit | IT-Sicherheit |

## A.2 Ereignismelde-Dokumentation

| Dokumententyp | Zweck | Eigentümer |
|---------------|-------|------------|
| **Sicherheitsereignismelde-Formular** | Standardisiertes Formular zur Meldung von Sicherheitsereignissen | IT-Sicherheit |
| **Ereignisklassifizierungsleitfaden** | Leitfaden zu Ereigniskategorien und Schweregraden | IT-Sicherheit |
| **Kurzreferenz der Meldekanäle** | Kontaktinformationen und Meldeverfahren | IT-Sicherheit |
| **Ereignisreaktionsbestätigung** | Vorlage zur Bestätigung empfangener Meldungen | IT-Sicherheit |

## A.3 Referenzmaterialien

Optionale Referenzvorlagen und -beispiele können bereitgestellt werden in:

- ISMS-REF-A.6.7-8 (Referenzmaterialien – falls erstellt)
- Organisatorisches Intranet oder Dokumentenmanagementsystem
- HR-Onboarding-Materialien

**Hinweis**: Das spezifische Format und der Inhalt operativer Formulare und Vorlagen werden von [Organisation] basierend auf ihren operativen Anforderungen, Technologieplattformen und der Organisationskultur bestimmt. Diese Richtlinie definiert, WELCHE Dokumentation erforderlich ist, nicht das spezifische Format.

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Datum] |
| **IT-Leiter (ITL)** | [Name] | [Datum] |
| **Human Resources Director** | [Name] | [Datum] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Datum] |
| **Unternehmensleitung** | [Name] | [Datum] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen für Remote-Arbeit und Meldung von Informationssicherheitsereignissen fest. Implementierungsverfahren, Beurteilungsvorlagen und detaillierte Leitfäden sind in ISMS-IMP-A.6.7-8 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
