<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.15-16-18-DE:framework:POL:a.5.15-16-18 -->
**ISMS-POL-A.5.15-16-18 — Identitäts- und Zugriffsmanagement**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Richtlinie für Identitäts- und Zugriffsmanagement |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.5.15-16-18 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Erstrichtlinie für ISO 27001:2022-Erstzertifizierung |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: IT-Leiter (ITL)
- HR-Integration: Personalleiter (PL)
- Compliance: Rechts-/Compliance-Beauftragter
- Letzte Autorität: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-IMP-A.5.15-16-18.S1-UG/TG (Benutzerinventar & Lebenszyklus-Compliance-Bewertung)
- ISMS-IMP-A.5.15-16-18.S2-UG/TG (Bewertung der Zugriffsrechtsmatrix)
- ISMS-IMP-A.5.15-16-18.S3-UG/TG (Bewertung der Zugriffsüberprüfungsergebnisse)
- ISMS-IMP-A.5.15-16-18.S4-UG/TG (Rollendefinition & SoD-Compliance-Bewertung)
- ISMS-POL-A.8.2-3-5 (Authentifizierung & Privilegierter Zugriff)
- ISO/IEC 27001:2022 Kontrollen A.5.15, A.5.16, A.5.18

---

## Zusammenfassung für die Geschäftsleitung

Diese Richtlinie legt die Anforderungen von [Organisation] an Identitäts- und Zugriffsmanagementkontrollen fest, um eine angemessene Zugriffsverwaltung über den gesamten Identitätslebenszyklus gemäss ISO/IEC 27001:2022 Kontrollen A.5.15, A.5.16 und A.5.18 sicherzustellen.

**Zweck**: Definition der organisatorischen Anforderungen an die IAM-Governance. Diese Richtlinie legt fest, WELCHE IAM-Kontrollen erforderlich sind und WER verantwortlich ist. Umsetzungsverfahren (WIE) sind separat in ISMS-IMP-A.5.15-16-18 (UG/TG-Varianten) dokumentiert.

**Anwendungsbereich**: Diese Richtlinie gilt für alle Benutzeridentitäten (Angestellte, Auftragnehmer, Anbieter, Dienstkonten), alle Identitätssysteme und alle Zugriffstypen unabhängig vom Bereitstellungsmodell oder der Technologie.

**Kombinierter Kontrollansatz**: Diese drei Kontrollen werden als einheitliches Rahmenwerk umgesetzt, da sie untrennbare Aspekte der Identitäts- und Zugriffsgovernance abdecken.

**Regulatorische Ausrichtung**: Diese Richtlinie adressiert verbindliche Compliance-Anforderungen gemäss ISMS-POL-00, einschliesslich des Schweizer nDSG, der EU DSGVO und ISO/IEC 27001:2022.

---

# Anwendungsbereich & Kontrollausrichtung

## ISO/IEC 27001:2022 Kontrollen

**A.5.15 – Zugangskontrolle**: Regeln zur Steuerung des physischen und logischen Zugangs zu Informationen und anderen zugehörigen Werten sollten auf der Grundlage von Geschäfts- und Informationssicherheitsanforderungen festgelegt und umgesetzt werden.

**A.5.16 – Identitätsmanagement**: Der vollständige Lebenszyklus von Identitäten sollte verwaltet werden.

**A.5.18 – Zugriffsrechte**: Zugriffsrechte auf Informationen und andere zugehörige Werte sollten in Übereinstimmung mit der themenspezifischen Richtlinie und den Regeln der Organisation für die Zugangskontrolle bereitgestellt, überprüft, angepasst und entzogen werden.

## Richtlinienanwendungsbereich

**Diese Richtlinie gilt für**:

| Kategorie | Anwendungsbereich |
|-----------|-------------------|
| **Benutzertypen** | Angestellte, Auftragnehmer, Anbieter, Dienstkonten, gemeinsam genutzte Konten (mit Genehmigung), Notfallkonten |
| **Identitätssysteme** | Active Directory, Azure AD/Entra ID, Okta, Google Workspace, LDAP und alle von [Organisation] genutzten Identitätssysteme |
| **Zugriffstypen** | Anwendungs-, System-, Daten-, Netzwerk- und administrativer/privilegierter Zugriff |
| **Personal** | IAM-Team, Sicherheitsteam, HR-Team, IT-Betrieb, Vorgesetzte, Systemeigentümer, alle Mitarbeitenden |

**Diese Richtlinie gilt NICHT für**:

- Physische Zugangskontrollsysteme (abgedeckt in A.7.2)
- Authentifizierungsmechanismen (abgedeckt in A.8.5)
- Implementierung des privilegierten Zugriffsmanagements (abgedeckt in A.8.2)

## Regulatorische Anwendbarkeit

**Stufe 1 – Obligatorische Compliance** (Alle Tätigkeiten):

| Regulierung | Wesentliche IAM-Anforderungen |
|-------------|-------------------------------|
| **Schweizer nDSG** | Art. 8 – Technische und organisatorische Massnahmen für die Zugangskontrolle |
| **EU DSGVO** | Art. 32 – Sicherheit der Verarbeitung einschliesslich Zugriffskontrollen |
| **ISO/IEC 27001:2022** | Kontrollen A.5.15, A.5.16, A.5.18 |

**Stufe 2 – Bedingte Anwendbarkeit** (Durch Geschäftstätigkeit ausgelöst):

- **FINMA**: Wenn [Organisation] eine FINMA-Lizenz besitzt (Rundschreiben 2023/1 Rz. 50–62)
- **DORA**: Wenn [Organisation] ein EU-Finanzunternehmen ist (Art. 6, 28–30)
- **NIS2**: Wenn [Organisation] eine wesentliche oder wichtige Einrichtung ist (Art. 21)
- **PCI DSS v4.0.1**: Wenn [Organisation] Zahlungskartendaten verarbeitet (Anforderungen 7, 8)

Compliance-Feststellung gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen).

---

# Richtlinienaussagen

## Anforderungen an die Zugangskontrolle (A.5.15)

### Grundsätze der Zugangskontrolle

[Organisation] muss Zugangskontrollen auf Basis der folgenden Grundsätze umsetzen:

| Grundsatz | Anforderung |
|-----------|-------------|
| **Geringstmögliche Berechtigung** | Benutzern wird der für ihre Funktion minimal notwendige Zugriff gewährt |
| **Need-to-Know** | Zugriff auf dokumentierten Geschäftsbedarf beschränkt |
| **Aufgabentrennung** | Unvereinbare Zuständigkeiten zur Verhinderung von Betrug/Irrtum getrennt |
| **Tiefenverteidigung** | Mehrere Schichten von Zugangskontrollen umgesetzt |
| **Standardmässige Verweigerung** | Zugriff verweigert, sofern nicht explizit mit Genehmigung gewährt |

### Zugriffsklassifizierung

[Organisation] muss den Zugriff nach folgenden Dimensionen klassifizieren:

| Dimension | Klassifizierungen |
|-----------|-------------------|
| **Benutzertyp** | Angestellter, Auftragnehmer (zeitlich begrenzt), Anbieter (extern), Dienstkonto (nicht-menschlich), Gemeinsam genutzt (ausnahmsweise), Notfall (Break-Glass) |
| **Systemkritikalität** | Kritisch, Hoch, Mittel, Niedrig |
| **Datensensibilität** | Eingeschränkt, Vertraulich, Intern, Öffentlich |
| **Zugriffsstufe** | Lesen, Schreiben, Admin, Privilegiert |

Klassifizierungskriterien sind in ISMS-IMP-A.5.15-16-18.1 definiert.

### Geschäftliche Begründung und Genehmigung

Alle Zugriffsanfragen müssen eine dokumentierte geschäftliche Begründung mit Genehmigungsbefugnis je nach Zugriffstyp enthalten:

| Zugriffstyp | Genehmigungsbefugnis |
|-------------|----------------------|
| **Standard-Benutzerzugriff** | Direkter Vorgesetzter |
| **Zugriff auf sensible Systeme** | Systemeigentümer + Vorgesetzter |
| **Vertrauliche/Eingeschränkte Daten** | Dateneigentümer + ISB |
| **Privilegierter/Admin-Zugriff** | ISB + ITL |
| **Drittanbieter-Zugriff** | Geschäftlicher Sponsor + ISB |
| **Gemeinsames Konto** (ausnahmsweise) | ISB mit kompensierenden Kontrollen |

### Aufgabentrennung

[Organisation] muss eine Aufgabentrennungsmatrix pflegen, die unvereinbare Rollenkombinationen identifiziert (dokumentiert in ISMS-IMP-A.5.15-16-18.3 Anhang A oder [GRC-Plattform SoD-Modul]). SoD-Verletzungen erfordern ISB-genehmigte Ausnahmen mit kompensierenden Kontrollen (protokolliert im Ausnahmenregister gemäss Abschnitt 4.2).

Die Erkennung von SoD-Verletzungen muss monatlich erfolgen (automatisiert über SoD-Prüfskript) mit Berichterstattung an das Sicherheitsteam (Ergebnis in IAM-SoD-Workbook-[JJJJ-MM]). Verletzungen müssen innerhalb von 30 Werktagen behoben oder als Ausnahmen mit ISB-Genehmigung protokolliert werden.

### HR-Integration

Die Zugangskontrolle muss mit HR-Lebenszyklusereignissen integriert werden:

| HR-Ereignis | Zugriffsaktion | Zeitrahmen |
|-------------|---------------|------------|
| **Neueinstellung** | Joiner-Prozess auslösen | Zugriff bis Startdatum bereit |
| **Rollenwechsel** | Mover-Prozess auslösen | Innerhalb von 2 Werktagen |
| **Kündigung** | Leaver-Prozess auslösen | Sofort (bei Kündigung aus wichtigem Grund) oder am selben Werktag |
| **Vertragsende** | Auftragnehmerzugriff entfernen | Am Vertragsendedatum |

Das HR-System ist als massgebliche Quelle für Identitätslebenszyklusereignisse designiert.

---

## Anforderungen an das Identitätsmanagement (A.5.16)

### Identitätslebenszyklus-Rahmenwerk

[Organisation] muss Identitäten durch standardisierte Lebenszyklusprozesse verwalten:

| Prozess | Auslöser | Zeitrahmen | Verantwortlichkeit |
|---------|---------|------------|-------------------|
| **Joiner** | HR-Benachrichtigung über Neueinstellung/Auftragnehmer | Zugriff bis Startdatum bereit | HR löst aus, IAM-Team erstellt, IT stellt bereit |
| **Mover** | HR-Benachrichtigung über Rollenwechsel | Innerhalb von 2 Werktagen | HR löst aus, Vorgesetzter genehmigt, IAM-Team aktualisiert |
| **Leaver** | HR-Benachrichtigung über Kündigung | Sofort bis am selben Werktag | HR löst aus, IAM-Team deaktiviert, IT verifiziert |

Detaillierte Verfahren sind in ISMS-IMP-A.5.15-16-18.2 dokumentiert.

### Anforderungen an Kontotypen

| Kontotyp | Anforderungen |
|----------|--------------|
| **Angestellter** | Dauerhaft bis zur Kündigung, individuelle Rechenschaftspflicht |
| **Auftragnehmer/Anbieter** | Zeitlich begrenzt mit obligatorischem Ablaufdatum (systemseitig erzwungen über Kontoablaufdatum bei Bereitstellung), interner Sponsor erforderlich (vierteljährlich mit Sponsor-Genehmigung erneuert oder automatisch deprovisioniert) |
| **Dienstkonto** | Dokumentierter Eigentümer (gepflegt in [IAM-System/GRC-Plattform]), Passwortrotation (mindestens vierteljährlich, verifiziert über automatisierten Scan oder manuellen Nachweis), privilegierte Kontrollen gemäss A.8.2, Nicht-Compliance im monatlichen IAM-Assessment gemeldet |
| **Gemeinsames Konto** | ISB-Genehmigung erforderlich (dokumentiert im Ausnahmenregister gemäss Abschnitt 4.2), kompensierende Kontrollen obligatorisch (individuelle Nutzungsprotokollierung über [SIEM/Audit-System], Überwachung privilegierter Zugriffe gemäss A.8.2, vierteljährliche Nutzungsprüfung durch ISB), stark abgeraten (Ziel: null gemeinsame Konten oder formelle ISB-genehmigte Ausnahme mit Begründung für jedes), zeitlich begrenzte Genehmigung (jährliche Revalidierung erforderlich) |
| **Notfall/Break-Glass** | Bis zum Katastrophenfall inaktiv, doppelte Autorisierung, Nutzung löst Alarm aus (halbjährlich getestet gemäss BCP-Verfahren, Testnutzung dokumentiert) |

### Verwaltung verwaister Konten

[Organisation] muss verwaiste Konten erkennen und beheben:

- **Erkennung**: Monatlicher Abgleich der Identitätssysteme mit dem HR-System
- **Behebung**: Untersuchung, Benachrichtigung, Deaktivierung, Löschung innerhalb von 30 Tagen
- **Ausnahmen**: ISB-Genehmigung mit dokumentierter Begründung erforderlich

---

## Anforderungen an Zugriffsrechte (A.5.18)

### Zuweisung von Zugriffsrechten

[Organisation] muss Zugriffsrechte zuweisen durch:

- Dokumentierten Anfrage- und Genehmigungsworkflow
- Rollenbasierte Zugangskontrolle (RBAC) als bevorzugte Methode
- Dokumentierte Geschäftsbegründung für alle Zugriffszuweisungen
- Prüfpfad gepflegt (Anfragender, Genehmigender, Zeitstempel, Begründung)

**Bereitstellungsfristen**:

| Anfragetyp | SLA |
|------------|-----|
| **Standardzugriff** | Innerhalb von 2 Werktagen |
| **Sensibler Zugriff** | Innerhalb von 5 Werktagen |
| **Notfallzugriff** | Innerhalb von 4 Stunden |

### Rollenbasierte Zugangskontrolle

[Organisation] muss RBAC umsetzen:

- **Rollenkatalog**: Gepflegt vom IAM-Team in [GRC-Plattform/IAM-System], innerhalb von 10 Werktagen nach organisatorischen Änderungen aktualisiert
- **Rolleneigentümerschaft**: Jeder Rolle ist ein Geschäftseigentümer zugewiesen (dokumentiert in der Rollendefinition)
- **Rollenlebenszyklus**: Neue Rollen erfordern IAM-Team-Genehmigung, Rollenänderungen erfordern Geschäftseigentümer-Genehmigung, veraltete Rollen werden archiviert (nicht gelöscht) für den Prüfpfad
- Rollen spezifischen Zugriffsrechten zugeordnet (Zugriffsberechtigungsmatrix dokumentiert in ISMS-IMP-A.5.15-16-18.3)
- Ziel: 80 % oder mehr Benutzer über Rollen statt direkten Zugriff zugewiesen
- Jährliche Rollenüberprüfung durch Geschäftseigentümer (verfolgt in [GRC-Plattform], Abschluss bis Q1 jährlich erforderlich)

### Zugriffsüberprüfung und Rezertifizierung

[Organisation] muss Zugriffsrechte regelmässig überprüfen:

| Klassifizierung | Häufigkeit | Prüfer |
|-----------------|------------|--------|
| **Kritische Systeme / Privilegierter Zugriff** | Vierteljährlich | ISB + Sicherheitsteam |
| **Hochrisiko-Systeme / Vertrauliche Daten** | Halbjährlich | Systemeigentümer + Vorgesetzte |
| **Standardsysteme / Interne Daten** | Jährlich | Vorgesetzte |
| **Drittanbieter-/Anbieterzugriff** | Vierteljährlich | Geschäftlicher Sponsor + ISB |

Drittanbieter-Zugriffsüberprüfungen umfassen die Validierung, dass die vertragliche Vereinbarung noch aktiv ist und der Zugriff gemäss A.5.20 noch notwendig ist.

Prüfer müssen den Zugriff als angemessen zertifizieren oder die Entfernung beantragen. Unangemessener Zugriff muss innerhalb von 5 Werktagen entfernt werden.

**Nachverfolgung der Zugriffsüberprüfung**:

Wenn unangemessener Zugriff aufgrund technischer Einschränkungen nicht innerhalb von 5 Werktagen entfernt werden kann:

- Vorgesetzte müssen Begründung und kompensierende Kontrollen in [GRC-Plattform] dokumentieren
- ISB-Genehmigung für Ausnahmen von mehr als 10 Werktagen erforderlich
- Ausstehende Entfernungen nach 15 Werktagen an ITL eskaliert
- Anhaltende Nichteinhaltung (>30 Tage) als Sicherheitsvorfall gemäss A.5.24-27 gemeldet

### Entfernung von Zugriffsrechten

[Organisation] muss Zugriff umgehend entfernen:

| Auslöser | Zeitrahmen |
|---------|------------|
| **Kündigung aus wichtigem Grund** | Sofort (innerhalb 1 Stunde) |
| **Freiwillige Kündigung** | Am selben Werktag |
| **Rollenwechsel** | Innerhalb von 2 Werktagen (Zugriff der vorherigen Rolle entfernen) |
| **Zugriffsüberprüfungsergebnis** | Innerhalb von 5 Werktagen |
| **Sicherheitsvorfall** | Sofort |

### Verhinderung von Berechtigungsausweitung

[Organisation] muss Berechtigungsausweitung erkennen und beheben:

**Erkennungsmethodik**:

| Erkennungsmethode | Häufigkeit | Tool/Prozess | Eigentümer |
|------------------|------------|--------------|------------|
| **Rollenbasierte Varianzanalyse** | Vierteljährlich | [IAM-System/GRC-Plattform] vergleicht tatsächlichen Zugriff mit Rollenberechtigungen | IAM-Team |
| **Mover-Prozess-Audit** | Monatlich | Überprüfung von Rollenwechseln zur Verifikation der Entfernung des vorherigen Zugriffs | Sicherheitsteam |
| **Zugriffsberechtigungsüberprüfung** | Halbjährlich | Überprüfung aller direkten (nicht rollenbasierten) Zugriffszuweisungen durch Vorgesetzte | Vorgesetzte |
| **Privilegierter Zugriff-Audit** | Vierteljährlich | Analyse privilegierter Zugriffszuweisungen gegen dokumentierten Bedarf | ISB |

**Erkennungsauslöser**:

- Benutzer hat mehr als 20 % mehr Zugriffsberechtigungen als die Rollendefinition vorsieht (zur Überprüfung markiert)
- Benutzer behält Zugriff aus vorheriger Rolle mehr als 30 Tage nach Mover-Ereignis
- Benutzer hat mehr als 3 direkte Zugriffszuweisungen ausserhalb rollenbasierter Zuteilungen
- Dienstkonto hat Zugriff über den dokumentierten Umfang hinaus

**Behebungsprozess**:

1. Überschüssiger Zugriff identifiziert und in [GRC-Plattform/IAM-System] protokolliert
2. Vorgesetzte benachrichtigt mit 5 Werktagen zur Begründung oder Genehmigung der Entfernung
3. Nicht gerechtfertigter Zugriff innerhalb von 10 Werktagen nach Identifizierung entfernt
4. Wiederholte Berechtigungsausweitung (>2 Vorkommen) löst Prozessverbesserungsüberprüfung aus

**Berichterstattung**: Kennzahlen zur Berechtigungsausweitung im monatlichen IAM-Governance-Dashboard enthalten (Anzahl der Befunde, durchschnittliche Behebungszeit, Wiederholungstäter nach Abteilung)

---

# Rollen & Verantwortlichkeiten

| Rolle | Verantwortlichkeit |
|-------|-------------------|
| **Geschäftsleitung** | Gesamtwirksamkeit des IAM-Programms, Richtliniengenehmigung, Ressourcenzuweisung |
| **ISB** | IAM-Richtlinienumsetzung und Compliance, Ausnahmengenehmigung, vierteljährliche Kennzahlenüberprüfung |
| **ITL** | IAM-Technologieinfrastruktur, Technologieauswahl, IT-Ressourcenzuweisung |
| **PL** | HR-System als massgebliche Identitätsquelle, Auslösen von Joiner/Mover/Leaver-Ereignissen |
| **Sicherheitsteam** | Richtlinienentwicklung, Compliance-Überwachung, Vorfallsuntersuchung, Bewertungen |
| **IAM-Team** | Identitätslebenszyklusprozesse, Identitätssystemwartung, Erkennung verwaister Konten |
| **HR-Team** | Joiner/Mover/Leaver-Benachrichtigungen, genaue Pflege von Mitarbeiterdaten |
| **IT-Betrieb** | Bereitstellung/Entfernung von Zugriffsrechten, technische Umsetzung |
| **Vorgesetzte** | Zugriffsgenehmigung für direkte Mitarbeitende, Zugriffsüberprüfungen, Kündigungsbenachrichtigung |
| **Systemeigentümer** | Definition von Zugriffsanforderungen, systemspezifische Zugriffsüberprüfungen, Genehmigung für sensible Systeme |
| **Interne Revision** | Verifizierung der IAM-Kontrollwirksamkeit, Compliance-Tests |
| **Alle Mitarbeitenden** | Zugriff nur bei Geschäftsbedarf anfordern, Zugriff angemessen nutzen, verdächtige Aktivitäten melden |

Detaillierte RACI-Matrix dokumentiert in ISMS-IMP-A.5.15-16-18.1.

---

# Governance & Compliance

## Bewertungsrahmen

[Organisation] muss die IAM-Kontrollwirksamkeit durch folgende Massnahmen verifizieren:

| Bewertung | Häufigkeit | Eigentümer | Nachweisstelle |
|-----------|------------|------------|----------------|
| Benutzerinventar & Lebenszyklus-Compliance | Monatlich | IAM-Team | IAM-Workbook-[JJJJ-MM] (automatisiert) |
| Zugriffsrechtsmatrix | Monatlich | IAM-Team | [GRC-Plattform/IAM-System-Export] |
| Zugriffsüberprüfungsergebnisse | Vierteljährlich | Sicherheitsteam | [Ticket-System], vierteljährliche Zusammenfassung an ISB |
| Rollen-Compliance & SoD | Vierteljährlich | IAM-Team | IAM-SoD-Workbook-[JJJJ-MM] (automatisiert) |
| IAM-Governance-Dashboard | Monatlich | Sicherheitsteam | [Business-Intelligence-Tool/SharePoint] |

**Nachweisgenerierung und -speicherung**:

- Benutzerinventar & Lebenszyklus-Compliance: Durch Python-Skript generiert, Ergebnis in IAM-Workbook-[JJJJ-MM] gespeichert
- Zugriffsrechtsmatrix: In [GRC-Plattform/IAM-System] gepflegt, monatlich für Sicherheitsteam-Überprüfung exportiert
- Zugriffsüberprüfungsergebnisse: Im [Ticket-System] verfolgt, vierteljährlicher Zusammenfassungsbericht an ISB mit Abschlussrate und Entfernung unangemessener Zugriffe
- Rollen-Compliance & SoD: Durch Python-Skript generiert, Verletzungen im Ausnahmenregister protokolliert, Ergebnis in IAM-SoD-Workbook-[JJJJ-MM]
- IAM-Governance-Dashboard: Monatlich vom Sicherheitsteam mit KPIs aktualisiert (siehe Governance-Kennzahlen unten)

Alle Bewertungsnachweise müssen mindestens 24 Monate gemäss A.5.33 (Schutz von Aufzeichnungen) aufbewahrt werden.

**Erkennungsmodus für Kontrollversagen**:

- **Verpasste Zugriffsüberprüfungen**: IAM-Team verfolgt Abschluss der Überprüfungen in [GRC-Plattform], eskaliert überfällige Überprüfungen nach 10 Werktagen an ISB
- **Nicht erkannte verwaiste Konten**: Sicherheitsteam prüft monatliche Berichte zu verwaisten Konten (mindestens 10 % Stichprobe)
- **Nicht behobene SoD-Verletzungen**: Ausnahmenregister verfolgt offene SoD-Verletzungen, vierteljährliche Überprüfung durch ISB markiert veraltete Einträge (>90 Tage ohne Fortschritt)
- **Verletzungen von Bereitstellungs-/Deprovisionierungs-SLAs**: [Ticket-System] markiert automatisch SLA-Verletzungen, monatlicher Bericht an ITL mit Ursachenanalyse für wiederkehrende Verletzungen
- **Nicht konforme Passwortalterung bei Dienstkonten**: Automatisierter Scan markiert Konten mit Passwörtern, die älter als 90 Tage sind, Bericht an IAM-Team zur Behebung innerhalb von 15 Werktagen

Kontrollversagenereignisse müssen als Vorfälle gemäss ISMS-POL-A.5.24-27 (Vorfallsmanagement) protokolliert werden, wenn sie ein Sicherheitsrisiko darstellen.

**Nachverfolgung der Lückenbehebung**:

IAM-Bewertungsergebnisse (verwaiste Konten, Zugriffsüberprüfungsmängel, SoD-Verletzungen, Bereitstellungsverzögerungen, Nichteinhaltung bei Dienstkonten) müssen:

- Innerhalb von 5 Werktagen nach Identifizierung im [zentralen Lückenregister/GRC-Plattform] protokolliert werden
- Einem verantwortlichen Eigentümer zugewiesen werden (IAM-Team, Vorgesetzter, Systemeigentümer je nach Befundtyp)
- Mit Zielbehebungsterminen basierend auf Risiko verfolgt werden:
  - Kritisch (unmittelbares Sicherheitsrisiko): 5 Werktage
  - Hoch (Kontrollversagen): 15 Werktage
  - Mittel (Kontrollschwäche): 30 Werktage
  - Niedrig (Optimierungsmöglichkeit): 90 Werktage
- Monatlich vom Sicherheitsteam zur Abschlussverifikation überprüft werden
- An ISB eskaliert werden, wenn die Behebung mehr als 30 Tage nach dem Zieltermin überfällig ist

**IAM-Governance-Kennzahlen (Monatliches Dashboard)**:

- Anzahl verwaister Konten und durchschnittliche Behebungszeit (Ziel: <10 Konten, <30 Tage bis zur Behebung)
- Abschlussrate der Zugriffsüberprüfungen nach Typ (Ziel: 100 % innerhalb des Überprüfungszeitraums)
- SLA-Compliance-Rate bei Bereitstellung/Deprovisionierung (Ziel: >95 %)
- RBAC-Adoptionsrate (Anteil der Benutzer über Rollen vs. direkten Zugriff, Ziel: >80 %)
- Anzahl SoD-Verletzungen und Ausnahmengenehmigungs-Status (Ziel: <5 offene Verletzungen, alle mit ISB-genehmigten Ausnahmen)
- Passwort-Alterungs-Compliance-Rate bei Dienstkonten (Ziel: >95 % rotiert innerhalb 90 Tage)
- IAM-Lückenbehebungsstatus (offene Befunde nach Alter und Risikostufe)

Kennzahlen werden monatlich vom Sicherheitsteam, vierteljährlich vom ISB überprüft und in das Management-Review gemäss Klausel 9.3 einbezogen.

Bewertungsverfahren sind in ISMS-IMP-A.5.15-16-18.5 dokumentiert.

## Ausnahmenmanagement

IAM-Richtlinienausnahmen erfordern:

- Dokumentierte Geschäftsbegründung
- Risikobewertung durch das Sicherheitsteam
- ISB-Genehmigung mit kompensierenden Kontrollen
- Dokumentation im Ausnahmenregister
- Jährliche Überprüfung auf fortbestehende Notwendigkeit

Ausnahmeantragsverfahren sind in ISMS-IMP-A.5.15-16-18.1 dokumentiert.

## Vorfallsreaktion

IAM-bezogene Vorfälle (Kontocompromittierung, Ausnutzung verwaister Konten, Privilegienerweiterung) müssen gemäss ISMS-POL-A.5.24-27 (Vorfallsmanagement) behandelt werden.

Notfall-Deprovisionierung muss bei Sicherheitsvorfällen innerhalb 1 Stunde erfolgen.

## Richtlinienüberprüfung

Diese Richtlinie muss überprüft werden:

- **Jährlich** (obligatorisch)
- **Bei Auslösung** durch regulatorische Änderungen, organisatorische Änderungen, Technologieänderungen, Audit-Ergebnisse, Risikobeurteilungsänderungen oder Erkenntnisse aus Vorfällen

Richtlinienänderungen erfordern ISB-Genehmigung; grössere Überarbeitungen erfordern Genehmigung der Geschäftsleitung.

---

# ISMS-Integration

## Anwendbarkeitserklärung

| Kontrolle | Status | Umsetzungsreferenz |
|-----------|--------|-------------------|
| **A.5.15 – Zugangskontrolle** | Anwendbar | Abschnitt 2.1, ISMS-IMP-A.5.15-16-18.1-UG/TG |
| **A.5.16 – Identitätsmanagement** | Anwendbar | Abschnitt 2.2, ISMS-IMP-A.5.15-16-18.2-UG/TG |
| **A.5.18 – Zugriffsrechte** | Anwendbar | Abschnitt 2.3, ISMS-IMP-A.5.15-16-18.3/4 |

## Verwandte Kontrollen

- **A.8.2** (Privilegierte Zugriffsrechte): IAM definiert privilegierte Benutzer, A.8.2 implementiert PAM
- **A.8.5** (Sichere Authentifizierung): IAM erstellt Identitäten, A.8.5 authentifiziert diese
- **A.5.24-27** (Vorfallsmanagement): Kontocompromittierungsvorfälle gemäss Vorfallsrahmenwerk verwaltet

## Umsetzungsressourcen

| Dokument | Zweck |
|----------|-------|
| **ISMS-IMP-A.5.15-16-18.1-UG/TG** | Zugriffssteuerungsgovernance |
| **ISMS-IMP-A.5.15-16-18.2-UG/TG** | Identitätslebenszyklusprozess |
| **ISMS-IMP-A.5.15-16-18.3-UG/TG** | Rollendefinition und -zuweisung |
| **ISMS-IMP-A.5.15-16-18.4-UG/TG** | Zugriffsüberprüfungsprozess |
| **ISMS-IMP-A.5.15-16-18.5-UG/TG** | IAM-Bewertungsverfahren |

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Identität** | Digitale Darstellung eines Benutzers (Person, Dienst, Gerät) mit eindeutigem Identifikator |
| **Zugangskontrolle** | Sicherheitstechnik zur Regulierung, wer Ressourcen einsehen oder nutzen kann |
| **RBAC** | Zugangskontrollmodell, bei dem Berechtigungen Rollen statt Einzelpersonen zugewiesen werden |
| **Geringstmögliche Berechtigung** | Grundsatz, der den minimal notwendigen Zugriff für die Jobfunktion fordert |
| **Aufgabentrennung** | Praxis der Aufteilung kritischer Aufgaben zur Verhinderung von Betrug und Irrtum |
| **Joiner-Prozess** | Onboarding neuer Benutzer einschliesslich Kontoerstellung und Zugriffsprovisionierung |
| **Mover-Prozess** | Verwaltung von Benutzerrollenwechseln einschliesslich Zugriffsanpassung |
| **Leaver-Prozess** | Offboarding einschliesslich Kontodeaktivierung und Zugriffsenternung |
| **Verwaistes Konto** | Konto ohne gültigen Geschäftseigentümer, das Behebung erfordert |
| **Berechtigungsausweitung** | Anhäufung übermässiger Zugriffsrechte im Laufe der Zeit bei Rollenwechseln |
| **Dienstkonto** | Nicht-menschliches Konto für automatisierte Prozesse |
| **Break-Glass-Konto** | Privilegiertes Notfallkonto für Katastrophenszenarien |

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date] |
| **IT-Leiter (ITL)** | [Name] | [Date] |
| **Personalleiter (PL)** | [Name] | [Date] |
| **Rechts-/Compliance-Beauftragter** | [Name] | [Date] |
| **Geschäftsleitung** | [Name] | [Date] |

---

# Nachweise für diese Richtlinie

**Stufe-1-Nachweise (Dokumentationsprüfung):**

Nachweise zum Beleg einer angemessenen Dokumentation und Genehmigung:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.5.15-16-18 v1.0)
- ✅ Genehmigungsunterschriften von ISB, ITL, PL, Rechts-/Compliance-Beauftragtem, Geschäftsleitung (Genehmigungsprotokoll)
- ✅ Grundsätze der Zugangskontrolle und Klassifizierungsrahmen definiert (Abschnitt 2.1)
- ✅ Identitätslebenszyklus-Rahmenwerk (Joiner/Mover/Leaver) dokumentiert (Abschnitt 2.2)
- ✅ Anforderungen an Kontotypen spezifiziert (Angestellter, Auftragnehmer, Dienst, Gemeinsam, Notfall) (Abschnitt 2.2)
- ✅ Zuweisung von Zugriffsrechten und RBAC-Rahmenwerk dokumentiert (Abschnitt 2.3)
- ✅ Häufigkeit und Kriterien der Zugriffsüberprüfung spezifiziert (Abschnitt 2.3)
- ✅ Anforderungen an die Aufgabentrennung definiert (Abschnitt 2.1)
- ✅ Erkennungsmethodik für Berechtigungsausweitung dokumentiert (Abschnitt 2.3)
- ✅ Rollen und Verantwortlichkeiten mit RACI-Referenz zugewiesen (Abschnitt 3)
- ✅ Governance-Rahmenwerk mit Bewertungsplan definiert (Abschnitt 4)
- ✅ Integration mit verwandten Kontrollen dokumentiert (Abschnitt 5)

**Stufe-2-Nachweise (Operative Wirksamkeit):**

Nachweise zur Wirksamkeit dieser Richtlinie im Betrieb:

- **Benutzerinventarberichte**: Monatliche IAM-Workbook-[JJJJ-MM] mit aktiven Identitäten, Kontotypen und Lebenszyklusstatus
- **Zugriffsüberprüfungs-Abschlussprotokoll**: Vierteljährliche/halbjährliche/jährliche Überprüfungsprotokolle im [Ticket-System] mit Prüfer, Entscheid und Zeitstempel für alle im Scope befindlichen Zugriffe
- **Joiner/Mover/Leaver-Prozessnachweise**: Von HR ausgelöste Workflow-Tickets, die die SLA-Einhaltung belegen (Zugriff bis Startdatum bereit, 2-Tage-Mover, Same-Day-Leaver)
- **Protokolle zur Behebung verwaister Konten**: Monatliche Erkennungsberichte mit Zeitstempeln für Untersuchung, Deaktivierung und Löschung (Behebung in <30 Tagen)
- **Berichte zur Aufgabentrennung**: IAM-SoD-Workbook-[JJJJ-MM] mit SoD-Prüfungen, identifizierten Verletzungen und Ausnahmegenehmigungen
- **Analysen der Berechtigungsausweitung**: Vierteljährliche Varianzberichte zum Vergleich von tatsächlichem Zugriff und Rollenberechtigungen mit Behebungsverfolgung
- **IAM-Governance-Dashboard**: Monatliche Kennzahlen (Anzahl verwaister Konten, Abschlussrate Überprüfungen, SLA-Compliance, RBAC-Adoptionsrate, SoD-Verletzungen, Passwort-Compliance)
- **Ausnahmenregister**: Dokumentierte Ausnahmen mit Geschäftsbegründung, ISB-Genehmigung, kompensierenden Kontrollen und jährlicher Revalidierung
- **Dienstkonto-Compliance**: Vierteljährliche Nachweise mit dokumentierten Eigentümern und Passwortrotations-Compliance (>95 % innerhalb 90 Tage)
- **Verifizierung der Zugriffsenternung**: Deprovisionierungs-Prüfpfad mit Zeitstempeln von Kündigung bis Deaktivierung gemäss Richtlinien-SLAs
- **Drittanbieter-Zugriffsüberprüfungen**: Vierteljährliche Sponsor-Bestätigungen zur Bestätigung des fortbestehenden Geschäftsbedarfs und aktiver Vertragsvereinbarungen
- **Bewertungs-Workbook-Ergebnisse**: Abgeschlossene ISMS-IMP-A.5.15-16-18.5-Bewertungs-Workbooks zum Nachweis der Kontrollwirksamkeitstests

## Abgrenzung bei Compliance-Nachweisen

Diese Richtlinie legt **Governance-Anforderungen für Identitäts- und Zugriffsmanagement** fest, die Zugangskontrollgrundsätze, Identitätslebenszyklusprozesse und Zugriffsrechtsverwaltung für alle Benutzertypen und Systeme abdecken.

Sie legt **NICHT** fest:
- **Physische Zugriffskontrollen** (abgedeckt in ISMS-POL-A.7.2 – Physischer Zutritt)
- **Authentifizierungsmechanismen** (abgedeckt in ISMS-POL-A.8.5 – Sichere Authentifizierung)
- **Implementierung des privilegierten Zugriffsmanagements** (abgedeckt in ISMS-POL-A.8.2 – Privilegierte Zugriffsrechte)
- **Spezifische Identitätssystemkonfigurationen** (organisatorische Technologieentscheidungen, in IMP-Verfahren dokumentiert)

Die Abgrenzung ist: **Diese Richtlinie definiert, WER WELCHEN Zugriff bekommt, WANN und WIE er verwaltet wird** → Technische Richtlinien (A.8.x) definieren, WIE der Zugriff authentifiziert und privilegierter Zugriff geschützt wird → Umsetzungsverfahren (IMP) dokumentieren systemspezifische Konfigurationen.

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt Anforderungen fest. Umsetzungsverfahren sind in ISMS-IMP-A.5.15-16-18 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-28 -->
<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.15-16-18-DE:framework:POL:a.5.15-16-18 -->
