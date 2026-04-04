<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.17-DE:framework:POL:a.5.17 -->
**ISMS-POL-A.5.17 — Authentifizierungsinformationen**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Authentifizierungsinformationen |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.17 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] | |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Date to be set] | ISB | Erstrichtlinie für ISO 27001:2022-Zertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- Letzte Autorität: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.5.15-16-18 (Identitäts- und Zugriffsmanagement)
- ISMS-POL-A.8.2-3-5 (Authentifizierung & Privilegierter Zugriff)
- ISMS-POL-A.8.24 (Einsatz von Kryptographie)
- ISMS-IMP-A.5.17.1-UG/TG (Umsetzungsleitfaden Passwortrichtlinie)
- ISMS-IMP-A.5.17.2-UG/TG (MFA-Bereitstellungsbewertung)
- ISMS-IMP-A.5.17.3-UG/TG (Verfahren zur Authentifizierungsverwaltung)
- ISO/IEC 27001:2022 Kontrolle A.5.17

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen von [Organisation] für das Management und den Schutz von Authentifizierungsinformationen fest, um unbefugten Zugriff auf Informationssysteme und Daten zu verhindern.

**Anwendungsbereich**: Diese Richtlinie gilt für alle Authentifizierungsinformationen einschliesslich Passwörter, PINs, kryptographische Schlüssel, Token, biometrische Vorlagen und andere Authentifizierungsgeheimnisse, die für den Zugriff auf Systeme und Daten von [Organisation] verwendet werden.

**Zweck**: Definition der organisatorischen Anforderungen an das Authentifizierungsinformationsmanagement. Diese Richtlinie legt fest, WELCHE Authentifizierungskontrollen erforderlich sind und WER verantwortlich ist. Umsetzungsverfahren (WIE) sind separat in ISMS-IMP-A.5.17 (UG/TG-Varianten) dokumentiert.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen), einschliesslich des Schweizer nDSG, der EU DSGVO und ISO/IEC 27001:2022. Bedingte branchenspezifische Anforderungen (FINMA, PCI DSS v4.0.1, NIS2, DORA) gelten, sofern die Geschäftstätigkeit von [Organisation] deren Anwendbarkeit auslöst.

---

**Kontrollausrichtung & Anwendungsbereich**

**ISO/IEC 27001:2022 Kontrolle A.5.17**

**ISO/IEC 27001:2022 Anhang A.5.17 – Authentifizierungsinformationen**

Authentifizierungsinformationen werden durch definierte Lebenszyklusprozesse ausgegeben, verwaltet, geschützt und widerrufen. Das Personal wird über den sicheren Umgang instruiert und muss dokumentierte Anforderungen zur Vertraulichkeit und Meldung von Kompromittierungen einhalten.

**Kontrollziele**:

- Sicherstellung einer sicheren Zuweisung von Authentifizierungsinformationen durch verifizierte Prozesse
- Schutz von Authentifizierungsinformationen über ihren gesamten Lebenszyklus
- Verhinderung unbefugter Zugriffe durch Credential-Kompromittierung
- Aufrechterhaltung der Rechenschaftspflicht für die Nutzung von Authentifizierungsdaten

**Kontrolltyp**: Präventiv
**Kontrollkategorie**: Organisatorisch

**Diese Richtlinie adressiert**:

- Zuweisung und Verteilung von Authentifizierungsinformationen
- Passwortanforderungen und Komplexitätsstandards
- Anforderungen an Multi-Faktor-Authentifizierung
- Schutz und Handhabung von Authentifizierungsgeheimnissen
- Passwort-Reset- und Wiederherstellungsverfahren

## Was diese Richtlinie regelt

Diese Richtlinie:

- **Definiert** Anforderungen für die sichere Zuweisung von Authentifizierungsinformationen
- **Legt fest** Passwortkomplexitäts- und Lebenszyklusstandards
- **Spezifiziert** MFA-Anforderungen nach Zugriffstyp
- **Referenziert** anwendbare regulatorische Anforderungen gemäss ISMS-POL-00

## Was diese Richtlinie NICHT regelt

Diese Richtlinie regelt NICHT:

- **Technische Implementierung von Authentifizierungsmechanismen** (siehe ISMS-POL-A.8.2-3-5 und ISMS-IMP-A.5.17)
- **Verfahren für das privilegierte Zugriffsmanagement** (siehe ISMS-POL-A.8.2-3-5)
- **Details zur kryptographischen Schlüsselverwaltungsinfrastruktur** (siehe ISMS-POL-A.8.24)
- **Verwaltung des Identitätslebenszyklus** (siehe ISMS-POL-A.5.15-16-18)

**Begründung**: Die Trennung von Richtlinienanforderungen und Umsetzungsanleitungen ermöglicht:

- Stabilität der Richtlinie trotz Technologie- oder Plattformwechseln
- Flexibilität für unterschiedliche Authentifizierungslösungen
- Klare Unterscheidung zwischen Governance (Richtlinie) und Ausführung (Umsetzung)

## Anwendungsbereich

**Diese Richtlinie gilt für**:

- Alle Authentifizierungsinformationen (Passwörter, PINs, Token, Schlüssel, Biometrie)
- Alle Informationssysteme, Anwendungen, Netzwerkgeräte, Cloud-Dienste und Datenbanken
- Alle Mitarbeitenden (Angestellte, Auftragnehmer, Dritte) mit Systemzugriff
- Alle Authentifizierungsprozesse (Zuweisung, Verwaltung, Reset, Widerruf)

**Nicht im Anwendungsbereich**:

- Persönliche Konten ohne Bezug zu Organisationssystemen
- Design und Entwicklung von Authentifizierungsmechanismen (abgedeckt durch A.8.5)
- Kryptographischer Schlüsselverwaltungslebenszyklus (Schlüsselgenerierungsstandards, kryptographische Parameter, HSM/KMS-Kontrollen, Enterprise-PKI-Betrieb) – geregelt durch ISMS-POL-A.8.24

**Abgrenzung des Anwendungsbereichs**: Diese Richtlinie umfasst Ausgabe, Speicherung/Handhabung, Zugangskontrolle, Rotations-/Widerruf-Auslöser und Protokollierung von Authentifizierungsgeheimnissen (einschliesslich API-Schlüssel und für die Authentifizierung verwendete Zertifikate). Kontrollen des kryptographischen Schlüsselverwaltungslebenszyklus werden durch ISMS-POL-A.8.24 geregelt; die Implementierung von Authentifizierungsmechanismen wird durch ISMS-POL-A.8.2-3-5 geregelt.

## Regulatorische Anwendbarkeit

Regulatorische Anforderungen werden gemäss **ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)** kategorisiert.

**Stufe 1: Obligatorische Compliance**

| Regulierung | Anwendbarkeit | Wesentliche Anforderungen |
|-------------|---------------|--------------------------|
| **Schweizer nDSG Art. 8** | Alle Personendatenverarbeitungen | Technische Massnahmen zum Datenschutz |
| **ISO/IEC 27001:2022** | Zertifizierungsumfang | Kontrolle A.5.17 – Authentifizierungsinformationen |

**Stufe 2: Bedingte Anwendbarkeit**

Gilt nur, wenn spezifische Geschäftsbedingungen die Anwendbarkeit auslösen:

| Regulierung | Auslösebedingung | Authentifizierungsanforderungen |
|-------------|-----------------|--------------------------------|
| **EU DSGVO Art. 32** | Verarbeitung europäischer Personendaten | Angemessene Sicherheitsmassnahmen einschliesslich Authentifizierung |
| **FINMA** | Reguliertes Schweizer Finanzinstitut | Verstärkte Authentifizierung für Finanzsysteme |
| **PCI DSS v4.0.1** | Zahlungskartenverarbeitung | Anforderung 8 – Starke Authentifizierung |
| **NIS2** | Wesentliche/wichtige Einrichtung (EU) | Anforderungen an starke Authentifizierung |
| **DORA** | EU-Finanzdienstleistungsunternehmen | IKT-Sicherheit einschliesslich Authentifizierungskontrollen |

**Stufe 3: Orientierende Hinweise**

Diese Rahmenwerke informieren die Umsetzung, begründen aber keine obligatorische Compliance, sofern nicht vertraglich gefordert:

- NIST SP 800-63B (Digitale Identitätsleitlinien – Authentifizierung)
- CIS Controls v8.1 (Kontrolle 5 – Kontoverwaltung, Kontrolle 6 – Zugangskontrolle)
- OWASP-Authentifizierungsleitlinien
- Microsoft Security Baseline-Empfehlungen

**Compliance-Feststellung**: [Organisation] bestimmt anwendbare Stufe-2-Vorschriften durch regelmässige Bewertung der Geschäftstätigkeit. Bei Überschneidung mehrerer Vorschriften gelten die strengsten Authentifizierungsanforderungen.

---

# Richtlinienaussagen

## Zuweisung von Authentifizierungsinformationen

### Anforderungen an die Erstzuweisung

[Organisation] muss Authentifizierungsinformationen durch kontrollierte Prozesse zuweisen:

**Identitätsverifizierung**:

- Benutzeridentität vor der Ausgabe von Authentifizierungsdaten verifizieren
- Out-of-Band-Verifizierung für sensiblen Systemzugriff verwenden
- Verwendete Verifizierungsmethode für den Prüfpfad dokumentieren

**Sichere Verteilung**:

| Authentifizierungstyp | Verteilungsmethode |
|-----------------------|--------------------|
| **Erstpasswörter** | Sicherer Kanal, getrennt vom Benutzernamen, Erzwingung der Änderung bei Erstverwendung |
| **Token/Hardware** | Persönliche Übergabe mit Identitätsverifizierung, unterzeichnete Empfangsbestätigung |
| **Zertifikate** | Sicherer Zertifikatsregistrierungsprozess, verifizierte E-Mail |
| **API-Schlüssel** | Verschlüsselter Kanal, begrenzte Gültigkeit, protokollierte Ausgabe |

**Temporäre Authentifizierung**:

- Temporäre Authentifizierungsinformationen dürfen maximal 24 Stunden gültig sein
- Benutzer müssen temporäre Anmeldedaten bei Erstverwendung ändern
- Das System muss die Ablaufzeit temporärer Anmeldedaten erzwingen

### Verwaltung von Standard-Anmeldedaten

[Organisation] darf keine Standard-Authentifizierungsdaten verwenden:

- Alle vom Anbieter/Hersteller vorgegebenen Standardpasswörter müssen vor der Produktionsinbetriebnahme geändert werden
- Standardkonten müssen deaktiviert oder umbenannt werden, sofern technisch machbar
- Die Verifizierung der Standardanmeldedatenänderung muss in die Inbetriebnahmecheckliste aufgenommen werden

**Bedingungen für „technisch nicht machbar"**: Standardkonten können nicht deaktiviert/umbenannt werden, wenn: (1) Anbieter-Firmware/-Support das Konto erfordert, (2) das System keine Umbenennungsfunktion bietet, (3) die Deaktivierung kritische Funktionen beeinträchtigt. Wo nicht machbar, gelten obligatorische kompensierende Kontrollen: einzigartiges starkes Passwort pro Gerät, Netzwerksegmentierung zur Zugriffsbeschränkung, MFA sofern unterstützt, erweiterte Überwachung/Alarmierung, Hinterlegung der Anmeldedaten in einem Passwort-Tresor und dokumentierte Ausnahme in ISMS-REG-EXCEPTIONS.

## Passwortanforderungen

### Passwortkomplexitätsstandards

[Organisation] muss folgende Passwortanforderungen durchsetzen:

| Anforderung | Standardzugriff | Privilegierter Zugriff | Dienstkonten |
|-------------|-----------------|------------------------|--------------|
| **Mindestlänge** | 12 Zeichen | 16 Zeichen | 24 Zeichen |
| **Komplexität** | 3 von 4 Zeichentypen | 4 von 4 Zeichentypen | Komplex + zufällig |
| **Historie** | 12 Passwörter gespeichert | 24 Passwörter gespeichert | Entf. (Einmalverwendung) |
| **Maximales Alter** | 90 Tage | 60 Tage | 90 Tage oder zertifikatsbasiert |
| **Sperrungsschwelle** | 5 Fehlversuche | 3 Fehlversuche | Alarm bei einzelnem Fehler |

**Zeichentypen**: Grossbuchstaben, Kleinbuchstaben, Zahlen, Sonderzeichen.

**Begründung für Passwortrotation**: Zeitbasierte Rotation wird durch ereignisbasierte Rotationsauslöser ergänzt: (1) vermutete Kompromittierung, (2) Entdeckung gemeinsam genutzter Anmeldedaten, (3) fehlender MFA-Schutz, (4) Personalrollenwechsel mit Änderung des Zugriffsumfangs. Wenn starke MFA und kontinuierliche Überwachung verifiziert sind, kann die Rotation durch dokumentierte Ausnahme mit ISB-Genehmigung verlängert werden. Die festgelegten Intervalle (60/90 Tage) spiegeln die Risikobehandlungsentscheidungen von [Organisation] wider, die Sicherheit und Benutzerfreundlichkeit abwägen.

### Verbotene Passwortpraktiken

Das Personal darf NICHT:

- Passwörter mit anderen Personen teilen (einschliesslich IT-Support)
- Passwörter an ungeschützten Stellen aufschreiben
- Passwörter in Klartextdateien oder Dokumenten speichern
- Dasselbe Passwort für mehrere Systeme verwenden
- Passwörter auf Basis leicht erratbarer Informationen verwenden (Namen, Daten, Wörterbuchwörter)
- Passwörter über unverschlüsselte Kanäle übertragen

### Passwortspeicherung

[Organisation] muss Passwörter sicher speichern:

- Passwörter müssen mit genehmigtem Einweg-Kryptographie-Hashing mit Salt gespeichert werden
- Passwort-Hashing-Algorithmen: bcrypt, Argon2, PBKDF2 (mit geeigneten Parametern)
- Klartextspeicherung von Passwörtern ist VERBOTEN
- Passwortdatenbanken müssen im Ruhezustand verschlüsselt geschützt werden

## Multi-Faktor-Authentifizierung

### MFA-Anforderungen

[Organisation] muss Multi-Faktor-Authentifizierung vorschreiben für:

| Zugriffstyp | MFA-Anforderung |
|-------------|-----------------|
| **Fernzugriff** (VPN, Cloud) | Obligatorisch |
| **Privilegierter/Admin-Zugriff** | Obligatorisch |
| **Kritische Systeme** | Obligatorisch |
| **Zugriff auf Kundendaten** | Obligatorisch |
| **E-Mail (externer Zugriff)** | Obligatorisch |
| **Standard-interner Zugriff** | Risikobasiert gemäss System-Tiering in ISMS-IMP-A.5.17; Entscheidungen in IdP-Richtlinien für bedingten Zugriff erfasst; Abdeckung vierteljährlich überprüft |

### MFA-Faktortypen

Akzeptable Authentifizierungsfaktoren:

| Faktorkategorie | Beispiele | Anforderungen |
|-----------------|-----------|--------------|
| **Etwas, das Sie wissen** | Passwort, PIN, Passphrase | Gemäss Passwortanforderungen |
| **Etwas, das Sie haben** | Hardware-Token, mobiler Authentifikator, Smartcard | Auf einzelnen Benutzer registriert |
| **Etwas, das Sie sind** | Fingerabdruck, Gesichtserkennung | Biometrische Vorlage sicher gespeichert |

MFA-Implementierungen müssen Faktoren aus mindestens zwei verschiedenen Kategorien verwenden.

## Schutz von Authentifizierungsinformationen

### Verantwortlichkeiten der Benutzer

Alle Mitarbeitenden müssen:

- Authentifizierungsinformationen vertraulich behandeln
- Starke, einzigartige Passwörter für jedes System verwenden
- Vermutete Kompromittierungen sofort melden
- Anderen Personen nicht die Nutzung ihrer Anmeldedaten erlauben
- Passwörter sofort ändern, wenn eine Kompromittierung vermutet wird
- Genehmigte Passwort-Manager zur sicheren Speicherung verwenden

### Systemanforderungen

Systeme müssen:

- Passworteingabe auf Bildschirmen maskieren
- Zuvor verwendete Passwörter nicht anzeigen
- Authentifizierungsverkehr im Transit verschlüsseln
- Authentifizierungsereignisse protokollieren (Erfolg und Fehler)
- Bei Authentifizierungsanomalien alarmieren
- Kontosperrung nach Fehlversuchen implementieren

### Gemeinsam genutzte Authentifizierungsinformationen

Gemeinsam genutzte Authentifizierungsinformationen sind NICHT EMPFOHLEN. Wo erforderlich:

- ISB-Genehmigung mit dokumentierter Geschäftsbegründung obligatorisch
- Speicherung in genehmigtem Anmeldedaten-Tresor (nicht in Klartextdokumenten/E-Mail/Chat)
- Benannter Verwahrer für jede gemeinsam genutzte Berechtigung
- Check-out-Protokollierung mit Benutzeridentifikation und Zeitstempel
- Sitzungsaufzeichnung für privilegierte gemeinsame Konten, sofern technisch machbar
- Individuelle Rechenschaftspflicht durch Prüfprotokollierung aufrechterhalten
- Vierteljährliche Überprüfung von Zugriff und Nutzung; jährliche Reauthorisierung erforderlich
- Verfahren in ISMS-IMP-A.5.17 dokumentiert

## Passwort-Reset und Wiederherstellung

### Self-Service-Passwort-Reset

Sofern implementiert, muss der Self-Service-Passwort-Reset:

- MFA-basierte Verifizierung (Authenticator-Push, FIDO2, Hardware-Token) für privilegierte Konten, Fernzugriff und kritische Systeme erfordern
- Wissensbasierte Sicherheitsfragen sind verboten, sofern keine genehmigte Ausnahme mit dokumentierten kompensierenden Kontrollen vorliegt
- E-Mail-/SMS-Verifizierung darf nur für Niedrig-Risiko-Konten verwendet werden, sofern in der Systemrisikobewertung genehmigt und zusätzliche Überwachung vorhanden ist
- Zeitlich begrenzte Reset-Token verwenden (maximale Gültigkeitsdauer 1 Stunde)
- Alle Reset-Aktivitäten einschliesslich der verwendeten Verifizierungsmethode protokollieren
- Benutzer über Passwortänderung über registrierten Kontakt benachrichtigen
- Nicht preisgeben, ob ein Konto existiert

### Helpdesk-unterstützter Passwort-Reset

Von Helpdesk unterstützte Passwort-Resets müssen:

- Benutzeridentität mit vorregistrierten Informationen verifizieren
- Temporäres Passwort mit Änderungserzwingung generieren
- Reset-Anfrage und Verifizierungsmethode dokumentieren
- Neues Passwort über sicheren Kanal mitteilen
- Passwörter dem Support-Personal nach der Ausgabe nicht preisgeben

---

# Rollen und Verantwortlichkeiten

## Verantwortlichkeitsmatrix

| Rolle | Authentifizierungsverantwortlichkeiten |
|-------|---------------------------------------|
| **Geschäftsleitung** | Authentifizierungsrichtlinie genehmigen, Ressourcen für die Umsetzung bereitstellen |
| **ISB** | Richtlinieneigentümerschaft, MFA-Strategie, Ausnahmengenehmigung |
| **IT-Betrieb** | Technische Umsetzung, Systemkonfiguration, Passwortinfrastruktur |
| **IAM-Team** | Benutzerprovisionierung, Anmeldedatenausgabe, Reset-Verfahren |
| **Helpdesk** | Unterstützter Passwort-Reset, Identitätsverifizierung |
| **Systemeigentümer** | Systemspezifische Authentifizierungskonfiguration, Compliance-Verifizierung |
| **Alle Mitarbeitenden** | Schutz der Anmeldedaten, Einhaltung der Richtlinie, Vorfallsmeldung |

## Eskalationspfad

- Fragen zur Authentifizierungsrichtlinie: Mitarbeitende → IAM-Team → ISB
- Ausnahmenanfragen: Antragsteller → Vorgesetzter → ISB
- Authentifizierungsvorfall: Mitarbeitende → Sicherheitsteam → ISB → Geschäftsleitung

---

# Governance & Compliance

## Bewertungsrahmen

| Bewertung | Häufigkeit | Eigentümer | Nachweis |
|-----------|------------|------------|----------|
| Passwortrichtlinien-Compliance | Monatlich | IT-Betrieb | Systemkonfigurationsaudit |
| MFA-Abdeckungsverifizierung | Vierteljährlich | Sicherheitsteam | Zugangssystemberichte |
| Authentifizierungsprotokollüberprüfung | Monatlich | Sicherheitsteam | SIEM-Analyseberichte |
| Scan auf Standard-Anmeldedaten | Vierteljährlich | Sicherheitsteam | Schwachstellenscan-Ergebnisse |
| Überprüfung des Bewusstseins der Benutzer | Jährlich | HR | Schulungsabschlussberichte |

**Governance-Kennzahlen**:

- MFA-Adoptionsrate (Ziel: 100 % für obligatorische Systeme)
- Passwortrichtlinien-Compliance-Rate (Ziel: >98 %)
- Durchschnittliche Passwort-Altersverteilung
- Muster bei fehlgeschlagenen Authentifizierungen
- Volumen der Passwort-Reset-Anfragen und Lösungszeit
- Anzahl der Befunde zu Standard-Anmeldedaten (Ziel: 0)

## Richtlinienüberprüfung

- **Häufigkeit**: Mindestens jährlich
- **Auslöser**: Änderungen der Authentifizierungstechnologie, Sicherheitsvorfälle, regulatorische Aktualisierungen
- **Prüfer**: ISB, IT-Betrieb, IAM-Team
- **Genehmigung**: Geschäftsleitung

## Ausnahmenmanagement

**Zulässige Ausnahmen**:

- Legacy-Systeme, die Passwortkomplexitätsanforderungen nicht erfüllen können (mit dokumentierter Mitigation)
- Systeme, die mit MFA nicht kompatibel sind (mit kompensierenden Kontrollen)
- Dienstkonten, die andere Passwortrichtlinien benötigen (mit erweiterter Überwachung)

**Ausnahmeprozess**:

1. Geschäftsbegründung dokumentieren
2. Risikobewertung durch Sicherheitsteam
3. ISB-Genehmigung mit kompensierenden Kontrollen
4. Zeitlich begrenzte Genehmigung (maximal 90 Tage, verlängerbar)
5. Dokumentation im Ausnahmenregister

**Nicht zulässig**:

- Ausnahmen, die Passwortfreigabe ohne Rechenschaftspflicht erlauben
- Ausnahmen, die MFA für privilegierten Zugriff eliminieren
- Ausnahmen, die Standard-Anmeldedaten im Produktionsbetrieb erlauben

Alle Ausnahmen müssen im Ausnahmenregister (ISMS-REG-EXCEPTIONS) erfasst werden.

## Verknüpfung mit Korrekturmassnahmen

Nichtkonformitäten in Bezug auf diese Richtlinie (z. B. schwache Passwortkonfigurationen, MFA-Lücken, Anmeldedaten-Kompromittierung, Befunde zu Standard-Anmeldedaten) müssen über den ISMS-Korrekturmassnahmenprozess (Klausel 10.2) mit Ursachenanalyse und nachverfolgter Behebung erfasst und verwaltet werden.

---

# Umsetzung & Referenzen

## Integration mit dem ISMS

Diese Richtlinie ist in das Informationssicherheits-Managementsystem von [Organisation] integriert:

**Risikobeurteilung** (ISO 27001 Klausel 6.1):

- Authentifizierungskontrollen werden auf Basis der Risikobeurteilung von [Organisation] ausgewählt
- Bedrohungen durch Anmeldedaten-Kompromittierung informieren Passwort- und MFA-Anforderungen
- Risikobehandlungspläne dokumentieren die Umsetzung von Authentifizierungskontrollen

**Anwendbarkeitserklärung** (ISO 27001 Klausel 6.1.3):

- Anwendbarkeit der Kontrolle A.5.17 in der SoA von [Organisation] begründet
- Umsetzungsstatus verfolgt und berichtet

**Verwandte Kontrollen**:

| Kontrolle | Beziehung |
|-----------|-----------|
| **A.5.15-16-18** | IAM definiert Identitäten; A.5.17 schützt deren Authentifizierung |
| **A.8.2-3-5** | Privilegierter Zugriff erfordert strengere Authentifizierung |
| **A.8.24** | Kryptographischer Schutz von Authentifizierungsinformationen |
| **A.8.12** | DLP erkennt Anmeldedatenlecks |
| **A.8.15** | Protokollierung von Authentifizierungsereignissen |

**Gestapelte Kontrollintegration**:

A.5.17 (Authentifizierungsinformationen) wirkt mit verwandten Kontrollen zusammen und bietet umfassenden Schutz:

| Gestapelte Kontrolle | Integrationspunkt | Beitrag von A.5.17 |
|---------------------|-------------------|-------------------|
| **A.5.15-16-18** (IAM) | Identitätslebenszyklus | A.5.17 schützt Anmeldedaten; IAM verwaltet Identitäten |
| **A.8.2-3-5** (Privilegierter Zugriff) | Admin-Authentifizierung | A.5.17 legt Standards fest; A.8.2 erzwingt strengere Anforderungen |
| **A.8.24** (Kryptographie) | Passwortschutz | A.5.17 schreibt Hashing vor; A.8.24 spezifiziert Algorithmen |

Die Bewertung von A.5.17 sollte gestapelte Kontrollbewertungen für eine vollständige Abdeckung berücksichtigen.

## Umsetzungsressourcen

**Umsetzungsleitfäden** (ISMS-IMP-A.5.17 Suite):

| Dokument-ID | Titel | Zweck |
|-------------|-------|-------|
| **ISMS-IMP-A.5.17.1-UG/TG** | Umsetzungsleitfaden Passwortrichtlinie | Technische Konfigurationsverfahren |
| **ISMS-IMP-A.5.17.2-UG/TG** | MFA-Bereitstellungsbewertung | MFA-Einführung und -Verifizierung |
| **ISMS-IMP-A.5.17.3-UG/TG** | Verfahren zur Authentifizierungsverwaltung | Operative Verfahren für den Anmeldedatenlebenszyklus |

---

# Nachweise für diese Richtlinie

**Stufe-1-Nachweise (Dokumentationsprüfung):**

Erforderliche Stufe-1-Nachweise umfassen:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.17 v1.0)
- ✅ Dokumentierte Genehmigung durch ISB, ITL, Geschäftsleitung
- ✅ Nachweis der Kommunikation an relevante Rollen
- ✅ Passwortkomplexitätsstandards definiert (Passwortanforderungen)
- ✅ MFA-Anforderungen spezifiziert (Multi-Faktor-Authentifizierung)
- ✅ Prozesse zur Erstzuweisung dokumentiert (Zuweisung von Authentifizierungsinformationen)
- ✅ Reset-/Wiederherstellungsverfahren definiert (Passwort-Reset und Wiederherstellung)
- ✅ Benutzerverantwortlichkeiten spezifiziert (Schutz von Authentifizierungsinformationen)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Rollen und Verantwortlichkeiten)

Der Nachweisstatus wird im ISMS-Nachweisregister verfolgt.

**Stufe-2-Nachweise (Operative Wirksamkeit):**

Nachweise zum Beleg der operativen Wirksamkeit dieser Richtlinie:

- Konfigurationsexporte der Passwortrichtlinie mit Komplexitäts-, Verlaufs- und Sperrungseinstellungen
- MFA-Bereitstellungsberichte mit Abdeckung für obligatorische Zugriffstypen
- Authentifizierungsprotokolle mit Ereignisprotokollierung und Anomalieerkennung
- Passwort-Reset-Aufzeichnungen mit Dokumentation der Identitätsverifizierung
- Scan-Ergebnisse für Standard-Anmeldedaten ohne Befunde
- Schulungsabschlussberichte zur Authentifizierungssensibilisierung
- Ausnahmenregister mit ISB-Genehmigung und kompensierenden Kontrollen
- Berichte zu Authentifizierungsvorfällen und Lösungsdokumentation

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Authentifizierungsinformationen** | Daten zur Identitätsverifikation, einschliesslich Passwörter, Token, Schlüssel, Biometrie |
| **Multi-Faktor-Authentifizierung (MFA)** | Authentifizierung, die zwei oder mehr Verifizierungsfaktoren aus verschiedenen Kategorien erfordert |
| **Passwort-Hash** | Einwegige kryptographische Darstellung eines Passworts |
| **Salt** | Zufällige Daten, die Passwörtern vor dem Hashing hinzugefügt werden, um Rainbow-Table-Angriffe zu verhindern |
| **Out-of-Band-Verifizierung** | Identitätsverifizierung über einen separaten Kommunikationskanal |
| **Brute-Force-Angriff** | Versuch, Anmeldedaten durch systematisches Durchprobieren zu erraten |
| **Credential Stuffing** | Angriff unter Verwendung von aus anderen Datenschutzverletzungen geleakten Anmeldedaten |

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **IT-Leiter (ITL)** | [Name] | [Date to be set] |
| **Geschäftsleitung** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen für das Management von Authentifizierungsinformationen fest. Umsetzungsverfahren sind in ISMS-IMP-A.5.17 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.17-DE:framework:POL:a.5.17 -->
