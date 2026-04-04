<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.3-DE:operational:OP-POL:a.5.3 -->
**ISMS-OP-POL-A.5.3 — Aufgabentrennung**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Aufgabentrennung |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.5.3 |
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
| 1.0 | [Datum] | ISB | Erstfassung der operativen Richtlinie für ISO 27001:2022 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.5.3 — Aufgabentrennung
- ISO/IEC 27002:2022 Abschnitt 5.3 — Implementierungsleitfaden
- Schweizerisches Obligationenrecht Art. 728a — Internes Kontrollsystem
- NIST SP 800-53 Rev 5 AC-5 — Aufgabentrennung

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur Aufgabentrennung |
|-----------|---------------------------|
| A.5.1 Richtlinien zur Informationssicherheit | Übergeordneter Richtlinienrahmen, der SoD-Anforderungen regelt |
| A.5.2 Rollen und Verantwortlichkeiten der Informationssicherheit | Rollendefinitionen, die Aufgabentrennung ermöglichen |
| A.5.15 Zugangskontrolle | Zugangskontrollregeln setzen Segregationsgrenzen durch |
| A.5.16 Identitätsmanagement | Eindeutige Identitäten gewährleisten individuelle Verantwortlichkeit |
| A.5.18 Zugriffsrechte | Zugangsprovisionierung implementiert Gegenseitigkeitsausschluss-Einschränkungen |
| A.8.2 Privilegierte Zugriffsrechte | Privilegierte Konten von Standardoperationen getrennt |
| A.8.3 Informationszugangsbeschränkung | Technische Durchsetzung von Segregationsregeln |
| A.8.5 Sichere Authentifizierung | Authentifizierung verifiziert Akteuridentität in jeder Prozessphase |
| A.8.15 Protokollierung | Prüfpfade zeichnen getrennte Aktivitäten zur Verifizierung auf |
| A.8.32 Änderungsmanagement | Änderungsprozess setzt Entwickler-/Tester-/Deployer-Trennung durch |

**Verwandte interne Richtlinien**:

- Identitäts- und Zugangsverwaltungsrichtlinie
- Authentifizierungs- und privilegierte Zugriffsrichtlinie
- Änderungsmanagementrichtlinie
- Protokollierungsrichtlinie
- Richtlinie zur Informationsklassifizierung und -handhabung

---

# Richtlinie zur Aufgabentrennung

## Zweck

Zweck dieser Richtlinie ist die Reduzierung des Risikos von Betrug, Fehler und Umgehung von Informationssicherheitsmassnahmen durch die Sicherstellung, dass widersprüchliche Aufgaben und widersprüchliche Verantwortungsbereiche auf verschiedene Personen oder Rollen aufgeteilt werden. Die Aufgabentrennung verhindert, dass eine einzige Person die vollständige Kontrolle über einen kritischen Prozess hat — von der Einleitung über die Genehmigung bis hin zur Ausführung und Verifizierung.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG), indem sie dem Risiko angemessene organisatorische Massnahmen zum Schutz der Datenverarbeitungsintegrität umsetzt. Die Aufgabentrennung ist eine anerkannte interne Kontrolle gemäss dem Schweizerischen Obligationenrecht Art. 728a, das von ordentlich geprüften Unternehmen ein internes Kontrollsystem verlangt. Sofern die Organisation Daten von Personen im EU/EWR-Raum bearbeitet, gelten zusätzlich die DSGVO-Anforderungen.

## Geltungsbereich

Alle Mitarbeitenden, Auftragnehmer und Drittnutzer, die an Geschäftsprozessen beteiligt sind, bei denen widersprüchliche Aufgaben Betrug, Fehler oder Sicherheitsverletzungen ermöglichen könnten, wenn sie von einer einzigen Person ausgeführt würden.

Dazu gehören:

- Finanztransaktionen, Genehmigungen und Auszahlungen.
- Informationssystemadministration, -entwicklung und -deployment.
- Zugangsprovisionierung, -überprüfung und -entzug.
- Sicherheitsüberwachung, Protokollüberprüfung und Incident Response.
- Beschaffung, Lieferantenmanagement und Vertragsverwaltung.
- Backup-, Wiederherstellungs- und Datenrestaurierungsoperationen.

**Ausserhalb des Geltungsbereichs**: Nicht sensible operative Prozesse mit ausreichender Überwachung; vollständig automatisierte Prozesse mit eingebauten Segregationskontrollen (wo die Segregation durch Automatisierung erreicht wird, müssen die Steuerungskonfiguration und Prüfpfade mindestens jährlich vom ISB oder einem designierten Prüfer validiert werden).

## Grundsatz

Widersprüchliche Aufgaben und widersprüchliche Verantwortungsbereiche sollten getrennt werden. Wo eine vollständige Trennung aufgrund der Grösse der Organisation nicht erreichbar ist, müssen kompensierende Massnahmen — einschliesslich verbesserter Überwachung, Managementüberprüfung, unabhängigem Audit und manipulationsgeschützten Prüfpfaden — implementiert und formell dokumentiert werden.

Alle Segregationsentscheidungen müssen risikobasiert sein und den Wert und die Klassifizierung der beteiligten Werte, das Potenzial für finanzielle Verluste oder Reputationsschäden sowie regulatorische Anforderungen berücksichtigen.

---

## Definitionen

| Begriff | Definition |
|---------|------------|
| **Aufgabentrennung (SoD)** | Die Praxis, Aufgaben und Privilegien auf mehrere Personen aufzuteilen, um zu verhindern, dass eine einzelne Person die vollständige Kontrolle über einen kritischen Prozess hat |
| **Widersprüchliche Aufgaben** | Verantwortlichkeiten, die, wenn sie einer Person kombiniert zugewiesen würden, dieser ermöglichen würden, Fehler oder Betrug zu begehen und zu verbergen, ohne entdeckt zu werden |
| **Kompensierende Massnahme** | Eine alternative Steuerungsmassnahme, die implementiert wird, wenn eine primäre Segregation nicht erreicht werden kann und eine gleichwertige Risikominderung bietet |
| **Gegenseitigkeitsausschluss** | Eine technische Steuerung, die verhindert, dass einem Benutzer gleichzeitig widersprüchliche Rollen in einem Zugangskontrollsystem zugewiesen werden |
| **Vier-Augen-Prinzip** | Eine Anforderung, dass kritische Aktionen die Genehmigung oder Verifizierung durch mindestens zwei autorisierte Personen vor der Ausführung erfordern |
| **SoD-Matrix** | Eine dokumentierte Zuordnung von Rollen, Aufgaben und identifizierten Konflikten zur Planung und Verifizierung der Aufgabentrennung |

---

## Segregationsprinzipien

Alle Geschäftsprozesse und Informationssysteme müssen Aufgabentrennung implementieren, wenn:

- Aktivitäten Finanztransaktionen **von mehr als CHF 10.000** beinhalten, es sei denn, ein niedrigerer Schwellenwert ist in einer abteilungsspezifischen Verfahrensanweisung definiert, die vom Finanzleiter (FL) und ISB auf Basis einer Risikobewertung genehmigt wurde.
- Zugang zu vertraulichen oder eingeschränkten Informationen erforderlich ist.
- Systemadministration oder privilegierter Zugang ausgeübt wird.
- Sicherheitsmassnahmen umgangen, geändert oder deaktiviert werden können.
- Prüfprotokolle oder Compliance-Nachweise geändert oder gelöscht werden können.

**Bestimmung des finanziellen Schwellenwerts**:
- **CHF 10.000** ist der organisatorische Basisschwellenwert, der auf einer Risikobewertung basiert, die Organisationsgrösse, Transaktionsvolumen und Betrugsgefährdungshistorie berücksichtigt.
- Niedrigere Schwellenwerte können für Hochrisikokategorien definiert werden (z. B. CHF 5.000 für Barauszahlungen, CHF 2.000 für Mitarbeiterspesenvergütungen) durch den Finanzleiter (FL) und ISB auf Basis einer abteilungsspezifischen Risikobewertung.
- Höhere Schwellenwerte sind ohne Genehmigung der Geschäftsleitung und kompensierende Massnahmen nicht zulässig.

**Schwellenwertüberprüfung**: Finanzschwellenwerte müssen jährlich vom Finanzleiter (FL) und ISB überprüft und basierend auf Inflation, Organisationswachstum und Neubewertung des Betrugsrisikos angepasst werden.

### Mindestsegregationsstandards

Die folgenden Mindestsegregationsanforderungen gelten:

| Prozesstyp | Mindestsegregationsanforderung |
|------------|--------------------------------|
| **Finanztransaktionen** >CHF 10.000 | Initiator darf nicht der Genehmiger sein |
| **Systemzugriffsanträge** | Antragsteller darf nicht der Genehmiger sein; Genehmiger darf nicht der Provisioner sein |
| **Änderungsmanagement** | Entwickler darf nicht der Tester sein; Tester darf nicht der Deployer sein |
| **Sicherheitsüberwachung** | Systemadministrator darf nicht der Protokollprüfer sein |
| **Backup und Wiederherstellung** | Backup-Operator darf nicht der Wiederherstellungsverifizierer sein |

Wenn eine Person derzeit widersprüchliche Aufgaben innehat, muss der Konflikt innerhalb von 30 Kalendertagen nach Identifikation gelöst werden — entweder durch Neuzuweisung, technischen Gegenseitigkeitsausschluss oder formelle Dokumentation kompensierender Massnahmen.

---

## Identifikation widersprüchlicher Aufgaben

Die Organisation muss eine dokumentierte SoD-Matrix führen, die Aufgabenkombinationen identifiziert, die eine Trennung erfordern. Die folgenden Kategorien bilden die Grundlage:

### Finanzprozesse

Die folgenden Aufgabenkombinationen müssen getrennt werden:

- Zahlungen einleiten UND Zahlungen genehmigen.
- Lieferantenstammdaten erstellen UND Zahlungen an Lieferanten verarbeiten.
- Transaktionen erfassen UND Konten abstimmen.
- Lohnbuchhaltung verwalten UND Lohnauszahlungen genehmigen.
- Budgetplanung UND Budgetgenehmigung.

### IT-Betrieb

Die folgenden Aufgabenkombinationen müssen getrennt werden:

- Code entwickeln UND in die Produktion deployen.
- Systeme administrieren UND Systemprotokolle überprüfen.
- Benutzerkonten erstellen UND Zugriffsanträge genehmigen.
- Backups verwalten UND Datenwiederherstellung autorisieren.
- Sicherheitsmassnahmen konfigurieren UND Sicherheitswirksamkeit prüfen.
- Firewall-Regeln verwalten UND Firewall-Compliance überprüfen.

### Beschaffung und Verträge

Die folgenden Aufgabenkombinationen müssen getrennt werden:

- Lieferanten auswählen UND Verträge verhandeln.
- Käufe genehmigen UND Waren oder Dienstleistungen entgegennehmen.
- Verträge verwalten UND Vertrags-Compliance verifizieren.

### Personalwesen

Die folgenden Aufgabenkombinationen müssen getrennt werden:

- Einstellungsentscheidungen UND Hintergrundüberprüfungsverifizierung.
- Vergütung festlegen UND Lohnbuchhaltung genehmigen.
- Zugang beenden UND Zugangsentzug bestätigen.

Abteilungsleiter müssen die SoD-Matrix jährlich für ihren Bereich überprüfen und neu identifizierte Konflikte dem ISB melden. Der ISB muss die konsolidierte organisatorische SoD-Matrix in [GRC Tool] oder einem äquivalenten Register pflegen.

> **SoD-Matrix-Speicherort**: [Angeben: ServiceNow GRC-Modul, Archer, MetricStream, SharePoint-Register oder «In Auswahl; interim: Excel-Register in kontrolliertem freigegebenem Laufwerk»]
>
> **Ausnahmeregister-Speicherort**: [Dasselbe System wie SoD-Matrix oder separat angeben]
>
> Wo kein dediziertes GRC-Tool eingesetzt ist, muss die Organisation Register in kontrolliertem freigegebenem Speicher mit Versionskontrolle, Zugriffsprotokollierung und vierteljährlicher Integritätsverifizierung durch den ISB führen.

---

## Kompensierende Massnahmen für kleine Teams und KMU

Wo Segregation aufgrund begrenzten Personals nicht vollständig erreicht werden kann — eine häufige Situation in kleinen und mittleren Organisationen — müssen kompensierende Massnahmen implementiert werden, um eine gleichwertige Risikominderung zu bieten.

### Erforderliche kompensierende Massnahmen

Wenn eine vollständige Aufgabentrennung nicht durchführbar ist, müssen **alle fünf** der folgenden kompensierenden Massnahmen für jeden identifizierten Konflikt implementiert werden:

| # | Kompensierende Massnahme | Implementierung |
|---|--------------------------|-----------------|
| 1 | **Verbesserte Überwachung und Protokollierung** | Alle Aktivitäten im widersprüchlichen Prozess müssen mit unveränderlichen Prüfpfaden protokolliert werden. Protokolle erfassen Benutzeridentität, Aktion, Zeitstempel und betroffene Datensätze |
| 2 | **Management-Transaktionsüberprüfung** | Ein am Prozess nicht beteiligter Manager oder erfahrener Kollege muss alle Transaktionen mindestens wöchentlich überprüfen |
| 3 | **Regelmässige unabhängige Überprüfung** | Eine unabhängige Partei (internes Audit, externer Prüfer oder Senior Management) muss den Prozess mindestens quartalsweise überprüfen |
| 4 | **Automatisierte Anomaliemeldungen** | [SIEM] oder gleichwertige Überwachung muss Alarme für ungewöhnliche Muster generieren, z. B. Transaktionen ausserhalb normaler Zeiten, Beträge über Schwellenwerten oder Massenoperationen |
| 5 | **Prüfpfad nach Transaktion mit Manipulationsschutz** | Transaktionsdatensätze müssen so gespeichert werden, dass eine Änderung oder Löschung durch die transaktion durchführende Person verhindert wird |

### Umfang der regelmässigen unabhängigen Überprüfung (Kompensierende Massnahme Nr. 3)

Eine unabhängige Partei muss den Prozess **mindestens quartalsweise** überprüfen. Die Überprüfung umfasst:

**Überprüfungsumfang**:
- **Stichprobentransaktionen** (mindestens 10 % des Transaktionsvolumens oder 20 Transaktionen, je nachdem, was grösser ist).
- **Prüfpfadverifizierung** (bestätigen, dass alle Aktivitäten protokolliert sind; Protokolle unveränderlich).
- **Management-Überprüfungsabschluss** (verifizieren, dass wöchentliche Management-Überprüfungen mit dokumentierter Abzeichnung stattgefunden haben).
- **Anomalieerkennung** (verifizieren, dass automatisierte Alarme funktionieren; ausgelöste Alarme und deren Lösung überprüfen).
- **Prozess-Compliance** (bestätigen, dass der Prozess wie dokumentiert eingehalten wurde).

**Überprüfungsdokumentation**: Jede Quartalsüberprüfung muss einen schriftlichen Bericht mit Umfang, Ergebnissen, identifizierten Problemen und Empfehlungen erstellen. Berichte werden 3 Jahre aufbewahrt.

**Problemeskalation**: Bei der unabhängigen Überprüfung identifizierte Probleme müssen innerhalb von 5 Arbeitstagen an den ISB eskaliert und innerhalb von 30 Kalendertagen gelöst werden.

### Dokumentationsanforderung

Jede kompensierende Massnahmenkonfiguration muss formell dokumentiert werden mit:

- Den spezifischen widersprüchlichen Aufgaben, die nicht getrennt werden können.
- Der geschäftlichen Begründung für die Unmöglichkeit der Trennung.
- Den eingesetzten kompensierenden Massnahmen (alle fünf oben genannten).
- Formeller Risikoakzeptanz, unterzeichnet von der Geschäftsleitung.
- Einem definierten Überprüfungsplan (mindestens quartalsweise).

Die Dokumentation der kompensierenden Massnahmen muss in [GRC Tool] oder einem äquivalenten Register gepflegt werden, das für den ISB und das interne Audit zugänglich ist.

### Neubewertungsauslöser

Kompensierende Massnahmenkonfigurationen müssen neu bewertet werden, wenn:

- Zusätzliche Mitarbeitende eingestellt werden, die getrennte Aufgaben übernehmen könnten.
- Die Organisationsstruktur sich ändert.
- Eine Risikobewertung eine erhöhte Exposition identifiziert.
- Auditbefunde Kontrollschwächen aufzeigen.
- Ein Sicherheitsvorfall im Bereich der kompensierenden Massnahme auftritt.

### Wirksamkeitsverifizierung kompensierender Massnahmen

Die Wirksamkeit kompensierender Massnahmen muss überprüft werden durch:

**Quartalsweise unabhängige Überprüfung** (Kompensierende Massnahme Nr. 3):
- Verifizieren, dass alle fünf kompensierenden Massnahmen wie dokumentiert funktionieren.
- Stichprobentransaktionen zur Bestätigung der Prüfpfadintegrität.
- Management-Überprüfungsabschluss mit dokumentierter Abzeichnung bestätigen.
- Konfiguration und Reaktion auf automatisierte Alarme testen.

**Jährliche Wirksamkeitsbewertung** durch den ISB:
- Alle kompensierenden Massnahmenkonfigurationen überprüfen.
- Bewerten, ob Massnahmen das Segregationsrisiko ausreichend mindern.
- Möglichkeiten zur vollständigen Segregation identifizieren (z. B. neue Einstellung kann getrennte Aufgabe übernehmen).
- Risikoakzeptanzdokumentation aktualisieren.

**Ausfall kompensierender Massnahmen**: Wenn eine kompensierende Massnahme als unwirksam befunden wird, sofortige Benachrichtigung der Geschäftsleitung und Behebung innerhalb von 14 Kalendertagen oder formelle erneute Akzeptanz des Restrisikos.

---

## Technische Segregationskontrollen

Informationssysteme, die getrennte Prozesse unterstützen, müssen folgende technische Kontrollen implementieren:

> **Protokollierungs- und Überwachungssystem**: [Angeben: Splunk, Elastic SIEM, Azure Sentinel oder «Auswahl läuft; interim: zentralisierte Protokollierung auf Syslog-Server mit manueller Überprüfung»]
>
> **Identitätsanbieter**: [Angeben: Azure AD, Okta, Google Workspace oder «Active Directory lokal»]
>
> **ERP/Finanzsystem**: [Angeben: SAP, Oracle, NetSuite oder zutreffendes System]
>
> Wo Systeme in Auswahl oder Übergang sind, Interimsvorgehen und Zieleinführungsdatum dokumentieren.

### Zugangskontrolldurchsetzung

- **Rollenbasierte Zugangskontrolle (RBAC)**: Rollen müssen im Identitätsanbieter oder der Applikation definiert werden, um Aufgabentrennung durchzusetzen. Widersprüchliche Rollen müssen als gegenseitig ausschliessend dokumentiert werden.
- **Gegenseitigkeitsausschluss-Einschränkungen**: Das Zugangskontrollsystem ([Identitätsanbieter / ERP / HR System]) muss verhindern, dass ein einzelner Benutzer gleichzeitig widersprüchliche Rollen innehat. Wo das System Gegenseitigkeitsausschluss nicht nativ unterstützt, muss bei jedem Zugangsprovisionierungsereignis eine manuelle Überprüfung durchgeführt werden.
- **Workflow-Kontrollen**: Mehrstufige Geschäftsprozesse müssen bei jeder Genehmigungsstufe unterschiedliche autorisierte Personen erfordern. Eigengenehmigungen müssen technisch blockiert werden, wo durchführbar, und in allen Fällen durch Richtlinien verboten sein.
- **Privilegiertes Zugriffsmanagement**: Privilegierte Konten müssen von Standardkonten getrennt sein. Keine Person darf eigene Anträge auf erhöhten Zugang genehmigen.

**Verifizierung von Gegenseitigkeitsausschluss-Einschränkungen**:
- **Automatisierte Systeme**: Gegenseitigkeitsausschluss-Einschränkungen müssen **jährlich** getestet werden, indem versucht wird, einem Testbenutzer widersprüchliche Rollen zuzuweisen und zu verifizieren, dass das System die Zuweisung blockiert. Testergebnisse dokumentiert.
- **Manuelle Überprüfungssysteme**: Zugangsprovisionierungschecklisten müssen eine SoD-Konfliktprüfung mit dokumentierter Verifizierung vor der Zugangsgenehmigung umfassen. Der Provisioner muss die SoD-Matrix referenzieren und bestätigen, dass keine Konflikte bestehen.
- **Quartalsweise Zugangsüberprüfung**: Alle Benutzerrollenzuweisungen müssen mit der SoD-Matrix verglichen werden, um Konflikte zu erkennen, die die Provisionierungskontrollen umgangen haben. Befunde werden innerhalb von 30 Kalendertagen behoben.

### Prüfpfadanforderungen

- **Unveränderliche Protokollierung**: Alle Aktivitäten in getrennten Prozessen müssen auf einer zentralisierten Protokollierungsplattform ([SIEM] oder äquivalent) protokolliert werden, die die Prozessteilnehmer nicht ändern oder löschen können.
- **Akteuridentifikation**: Protokolle müssen klar die Person identifizieren, die jede Aktion in jeder Prozessphase durchführt.
- **Zeitstempel- und Aktionsaufzeichnung**: Alle Genehmigungen, Änderungen und Prozessabschlüsse müssen mit genauen Zeitstempeln aufgezeichnet werden.
- **Protokollschutz**: Prüfprotokolle müssen gemäss der Protokollierungsrichtlinie vor Änderung oder Löschung geschützt werden. Akzeptable Implementierungen umfassen einmal beschreibbaren Speicher, eingeschränkten Administratorzugang mit separatem Protokollprüfer, Aufbewahrungssperren oder zentralisierte Protokollaggregation mit Integritätsverifizierung.

---

## Ausnahmemanagement

Ausnahmen von Segregationsanforderungen müssen durch einen formellen Prozess verwaltet werden. Eigengenehmigungen von Segregationsausnahmen sind niemals zulässig.

### Notfallausnahmen (Dauer 24 Stunden oder weniger)

Wenn eine operative Dringlichkeit das vorübergehende Umgehen von Segregationskontrollen erfordert:

1. **Mündliche Genehmigung** durch Abteilungsleiter und ISB (oder ISB-Delegierter) — aufzeichnen, wer genehmigt hat, wann und die spezifische gewährte Ausnahme.
2. **Dokumentation innerhalb von 4 Stunden** nach Ausnahmenutzen über [Notfallausnahmeformular / Ticket-System / E-Mail an ISB] mit:
   - Ausnahme-ID (eindeutiger Bezeichner).
   - Name und Rolle des Antragstellers.
   - Mündliche Genehmiger (Namen, Zeitpunkt der Genehmigung).
   - Geschäftliche Begründung (spezifische operative Dringlichkeit).
   - Gewährte Ausnahme (spezifische kombinierte Aufgaben; Dauer).
   - Während der Ausnahmephase durchgeführte Aktionen.
   - Aktive kompensierende Massnahmen (verbesserte Überwachung, sofortige Nachüberprüfung).
3. **Vollständige Überprüfung innerhalb von 24 Stunden** nach Ausnahmeende — der ISB oder Delegierter muss verifizieren, dass kompensierende Massnahmen wirksam waren und keine Unregelmässigkeiten aufgetreten sind. Überprüfungsabzeichnung dokumentiert.
4. **Kompensierende Massnahmen aktiv** während der Ausnahmeperiode — verbesserte Überwachung und Nachaktivitätsüberprüfung mindestens.

**Notfallausnahmeprotokoll**: Alle Notfallausnahmen müssen im Ausnahmeregister mit dem Flag «Notfall» protokolliert werden.

### Geplante Ausnahmen (Dauer mehr als 24 Stunden)

Wenn eine längerfristige Ausnahme erforderlich ist (z. B. Personalabwesenheit, Projektbeschränkungen):

1. **Formeller Ausnahmeantrag** beim ISB mit geschäftlicher Begründung.
2. **Risikobewertung** der Auswirkungen der Ausnahme auf Betrugs- und Fehlerprävention.
3. **Kompensierende Massnahmen** dokumentiert und genehmigt, bevor die Ausnahme in Kraft tritt.
4. **ISB- und Geschäftsleitungs-Genehmigung** — beide erforderlich.
5. **Maximale Dauer**: 90 Kalendertage. Verlängerung erfordert erneute Bewertung und erneute Genehmigung.

### Nicht zulässig

Folgende Ausnahmen dürfen unter keinen Umständen gewährt werden:

- Dauerhafte Ausnahmen von finanziellen Segregationsanforderungen.
- Ausnahmen, die Prüfpfadfähigkeiten eliminieren oder umgehen.
- Eigengenehmigung der eigenen Segregationsausnahme.

### Ausnahmeregister

Alle Ausnahmen müssen im in [GRC Tool] oder äquivalent geführten Ausnahmeregister aufgezeichnet werden. Jeder Datensatz muss enthalten:

- Betroffene System(e) und Prozess(e).
- Identität und Rolle(n), der/denen die Ausnahme gewährt wurde.
- Zeitfenster (Startdatum und Enddatum).
- Genehmigungsbehörde mit Genehmigungsnachweis.
- Während der Ausnahme aktive kompensierende Massnahmen.
- Ergebnis der Nachausnahme-Überprüfung.
- Abschlussdatum.

Der ISB muss das Ausnahmeregister monatlich überprüfen und aktive Ausnahmen der Geschäftsleitung quartalsweise berichten.

---

## Pflege der SoD-Matrix

### Jahresüberprüfung

Die organisatorische SoD-Matrix muss jährlich überprüft und aktualisiert werden. Die Überprüfung muss:

- Bestätigen, dass alle dokumentierten Konflikte gültig und vollständig bleiben.
- Neue Konflikte identifizieren, die aus organisatorischen Änderungen, neuen Systemen oder neuen Prozessen entstehen.
- Verifizieren, dass kompensierende Massnahmen für ungelöste Konflikte weiterhin wirksam sind.
- Die Matrix aktualisieren, um die aktuelle Organisationsstruktur widerzuspiegeln.

### Quartalsweise Zugriffsrechtsverifizierung

Der IT-Betrieb muss quartalsweise Zugangsberichte vom Identitätsanbieter und Applikationszugangssystemen generieren. Der ISB muss diese Berichte mit der SoD-Matrix vergleichen, um zu verifizieren:

- Keine Person hält widersprüchliche Rollen in Produktionssystemen.
- Gegenseitigkeitsausschluss-Einschränkungen funktionieren korrekt.
- Neue Rollenzuweisungen seit der letzten Überprüfung erzeugen keine undokumentierten Konflikte.

Befunde müssen dokumentiert und Konflikte innerhalb von 30 Kalendertagen nach Entdeckung behoben werden.

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten Aufgabentrennung |
|-------|--------------------------------------|
| **Geschäftsleitung** | Segregationsrichtlinie genehmigen; Restrisiken akzeptieren; kompensierende Massnahmen genehmigen; geplante Ausnahmen genehmigen |
| **ISB** | SoD-Matrix definieren und pflegen; Compliance überwachen; Notfall- und geplante Ausnahmen genehmigen; Ausnahmeregister monatlich überprüfen |
| **Finanzleiter (FL)** | Finanzprozesssegregation beaufsichtigen; finanzielle Kontrollausnahmen gemeinsam mit ISB genehmigen; finanzielle Schwellenwertanpassungen festlegen |
| **Abteilungsleiter** | Segregation innerhalb der Abteilungen implementieren; neue Konflikte identifizieren; Ausnahmen anfragen; wöchentliche Managementüberprüfung kompensierender Massnahmen sicherstellen |
| **HR** | Organisationsstruktur zur Unterstützung der Segregation pflegen; IT über Rollenänderungen benachrichtigen, die Aufgabenzuweisungen betreffen |
| **IT-Betrieb** | Technische Kontrollen implementieren (RBAC, Gegenseitigkeitsausschluss, Workflow); quartalsweise Zugangsberichte generieren; Prüfpfade pflegen |
| **Internes Audit** | Segregationswirksamkeit verifizieren; Angemessenheit kompensierender Massnahmen bewerten; Verstösse melden; quartalsweise unabhängige Überprüfungen durchführen |

### Eskalationspfad

- **Identifizierte Segregationskonflikte**: Abteilungsleiter benachrichtigt ISB. ISB eskaliert an Geschäftsleitung, wenn die Lösung eine organisatorische Änderung erfordert.
- **Ausnahmeanträge**: Antragsteller reicht bei Abteilungsleiter ein. Abteilungsleiter reicht beim ISB ein. ISB holt Geschäftsleitungs-Genehmigung für geplante Ausnahmen ein.
- **Erkannter Verstoss**: Sofortige Benachrichtigung von ISB und internem Audit. Untersuchung wird innerhalb von 24 Stunden eingeleitet.

### Verstossuntersuchungsprozess

Wenn ein Segregationsvestoss erkannt wird:

1. **Sofortige Benachrichtigung** von ISB und internem Audit (innerhalb von 4 Stunden nach Erkennung).
2. **Untersuchung eingeleitet** innerhalb von 24 Stunden durch internes Audit oder vom ISB designierten Ermittler.
3. **Untersuchungsumfang**:
   - Feststellen, ob der Verstoss unbeabsichtigt war (Systemfehlkonfiguration, Zugangsprovisionierungsfehler) oder absichtlich.
   - Alle während der Verletzungsperiode durchgeführten Transaktionen überprüfen.
   - Bewerten, ob Betrug oder Fehler aufgetreten ist.
   - Grundursache identifizieren (Prozessversagen, Schulungslücke, absichtliche Umgehung).
4. **Untersuchungszeitplan**: Innerhalb von 10 Arbeitstagen für administrative Verstösse abschliessen; innerhalb von 5 Arbeitstagen bei vermutetem Betrug.
5. **Abhilfe**: Sofortiger Zugangsentzug bei laufendem Verstoss; Korrekturmassnahmenplan innerhalb von 14 Kalendertagen.
6. **Berichterstattung**: Untersuchungsbericht an ISB, Finanzleiter (FL) und Geschäftsleitung (für Finanzverstösse oder vermuteten Betrug).

**Disziplinarmassnahmen**: Gemäss dem Abschnitt zur Nichteinhaltung der Richtlinie und den Disziplinarverfahren der Organisation.

---

## Schulung und Sensibilisierung

**Jährliche SoD-Sensibilisierungsschulung** muss allen Mitarbeitenden bereitgestellt werden und Folgendes abdecken:
- Zweck der Aufgabentrennung (Betrugs- und Fehlerprävention).
- Beispiele widersprüchlicher Aufgaben (finanziell, IT, Beschaffung).
- Individuelle Verantwortlichkeiten (eigene Arbeit nicht genehmigen, Konflikte melden).
- Ausnahmeprozess (wie Ausnahmen ordnungsgemäss beantragt werden).
- Konsequenzen von SoD-Verstössen (Disziplinarmassnahmen, mögliche Betrugsimplikationen).

**Rollenspezifische Schulung**:
- **Abteilungsleiter**: Wöchentliche Management-Überprüfungsverfahren für Bereiche mit kompensierenden Massnahmen; Identifikation neuer Konflikte.
- **IT-Betrieb**: RBAC-Konfiguration, Implementierung von Gegenseitigkeitsausschluss, Prüfpfadschutz.
- **Finanzteam**: Finanzielle Segregationsanforderungen, Genehmigungsworkflow-Compliance.

Schulungsabschluss wird verfolgt; Ziel: **100 % der Mitarbeitenden mit Segregationsverantwortlichkeiten jährlich geschult**.

---

## Nachweise

Die folgenden Nachweise belegen die Einhaltung dieser Richtlinie:

| # | Nachweis | Eigentümer | Häufigkeit |
|---|---------|------------|------------|
| 1 | **SoD-Matrix** mit Dokumentation aller identifizierten widersprüchlichen Aufgabenkombinationen und Segregationsstatus | ISB | *Jährlich überprüft; bei organisatorischen Änderungen aktualisiert* |
| 2 | **Zugriffsrechtsberichte** mit Rollenzuweisungen über Systeme, verifiziert mit SoD-Matrix | IT-Betrieb | *Quartalsweise generiert; vom ISB überprüft* |
| 3 | **Register der kompensierenden Massnahmen** mit Risikoakzeptanz-Abzeichnung durch Geschäftsleitung | ISB | *Quartalsweise überprüft; bei Auslöseereignissen aktualisiert* |
| 4 | **Ausnahmeregister** mit Genehmigungsnachweis, kompensierenden Massnahmen und Abschlussunterlagen | ISB | *Monatlich überprüft; quartalsweise an Geschäftsleitung berichtet* |
| 5 | **Management-Überprüfungsunterlagen** für Bereiche mit kompensierenden Massnahmen (wöchentliche Transaktionsüberprüfungen) | Abteilungsleiter | *Wöchentlich; 3 Jahre aufbewahrt* |
| 6 | **Unabhängige Überprüfungsberichte** für Bereiche, in denen keine Segregation erreichbar ist | Internes Audit | *Quartalsweise; 3 Jahre aufbewahrt* |
| 7 | **RBAC-Konfigurationsnachweise** mit Gegenseitigkeitsausschluss-Einschränkungen in Zugangskontrollsystemen | IT-Betrieb | *Jährlich oder bei Änderung erfasst; 3 Jahre aufbewahrt* |
| 8 | **Workflow-Genehmigungsunterlagen** mit Mehrparteien-Kontrolle für finanzielle und Systemänderungen | IT-Betrieb | *Pro Transaktion; gemäss Aufbewahrungsplan aufbewahrt* |
| 9 | **Prüfprotokoll-Integritätsverifizierungsunterlagen** für getrennte Prozessprotokollierung | IT-Betrieb | *Monatlich; 3 Jahre aufbewahrt* |
| 10 | **Jahres-SoD-Matrix-Überprüfung** mit Abzeichnung und aktualisierter Matrix | ISB | *Jährlich; 3 Jahre aufbewahrt* |

---

# Richtlinien-Compliance

## Compliance-Messung

Das Information Security Management Team wird die Einhaltung dieser Richtlinie durch verschiedene Methoden verifizieren, darunter unter anderem SoD-Matrix-Überprüfungen, Zugriffsrechtsanalyse gegen die Konfliktmatrix, Wirksamkeitsbewertungen kompensierender Massnahmen, Ausnahmeregisteraudits, interne und externe Audits sowie Rückmeldungen an den Richtlinieneigentümer.

Die folgenden Kennzahlen müssen dem ISB quartalsweise verfolgt und berichtet werden:

| Kennzahl | Ziel | Rotschwelle |
|----------|------|-------------|
| Identifizierte und dokumentierte Segregationskonflikte | 100 % der überprüften Prozesse | <80 % Abdeckung |
| Zeit zur Lösung identifizierter Konflikte | 30 Kalendertage | >60 Kalendertage |
| Aktive Ausnahmen | Minimiert; sinkend | >5 gleichzeitig oder >90 Tage |
| Abschluss der quartalsweisen Überprüfung kompensierender Massnahmen | 100 % | <80 % |
| Jährliche SoD-Matrix-Überprüfung termingerecht abgeschlossen | Ja | Überfällig >30 Tage |

**Berichtsanforderungen**:
- **Monatliches ISB-Dashboard**: Ausnahmeregisterstatus, aktive Ausnahmen, überfällige Konfliktlösungen.
- **Vierteljährlicher Geschäftsleitungs-Bericht**: Kennzahlenstatus, Trendanalyse (gelöste vs. neu identifizierte Konflikte), Wirksamkeitsbewertung kompensierender Massnahmen.
- **Jährlicher Management Review**: Vollständige SoD-Programmwirksamkeitsbewertung einschliesslich Kennzahlentrends, wesentlicher Befunde und Verbesserungsempfehlungen.

Kennzahlen, die Rotschwellen überschreiten, müssen an den ISB zur sofortigen Behandlung eskaliert und im nächsten Management Review berichtet werden.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie muss vom ISB im Voraus genehmigt und mit dokumentierter Risikoakzeptanz, kompensierenden Massnahmen und einem definierten Überprüfungsdatum aufgezeichnet werden. Geplante Ausnahmen erfordern gemeinsame Genehmigung von ISB und Geschäftsleitung. Ausnahmen müssen dem Management-Review-Team gemeldet werden. Dauerhafte Ausnahmen von finanziellen Segregationsanforderungen und Ausnahmen, die Prüfpfadfähigkeiten eliminieren, sind nicht zulässig.

## Nichteinhaltung

Mitarbeitende, die gegen diese Richtlinie verstossen haben, können Disziplinarmassnahmen bis zur Kündigung des Arbeitsverhältnisses unterliegen. Segregationsverstösse, die Finanzprozesse betreffen, müssen dem Finanzleiter (FL) gemeldet werden und können zusätzliche Untersuchungen im Rahmen der Betrugsreaktionsverfahren der Organisation auslösen.

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen berücksichtigen Änderungen der Organisationsstruktur, neue Systeme oder Prozesse, Auditbefunde, regulatorische Änderungen, Ausnahmetrends, Wirksamkeit kompensierender Massnahmen und Erkenntnisse aus segregationsbezogenen Vorfällen. Nichtkonformitäten im Zusammenhang mit dieser Richtlinie müssen aufgezeichnet und durch den ISMS-Korrekturmassnahmenprozess (Klausel 10.2) mit Grundursachenanalyse und nachverfolgter Behebung verwaltet werden.

---

# Abgedeckte Bereiche des ISO 27001 Standards

Richtlinie zur Aufgabentrennung — ISO 27001 Massnahmen-Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Klausel 5.1 Führung und Verpflichtung | 5.1 Richtlinien zur Informationssicherheit |
| Klausel 5.2 Richtlinie | 5.2 Rollen und Verantwortlichkeiten der Informationssicherheit |
| Klausel 5.3 Organisatorische Rollen, Verantwortlichkeiten und Befugnisse | **5.3 Aufgabentrennung** |
| Klausel 6.1 Massnahmen zur Behandlung von Risiken und Chancen | 5.4 Managementverantwortung |
| Klausel 7.3 Bewusstsein | 5.15 Zugangskontrolle |
| Klausel 8.1 Operative Planung und Steuerung | 5.16 Identitätsmanagement |
| Klausel 9.1 Überwachung, Messung, Analyse und Bewertung | 5.18 Zugriffsrechte |
| Klausel 10.2 Nichtkonformität und Korrekturmassnahmen | 8.2 Privilegierte Zugriffsrechte |
| | 8.3 Informationszugangsbeschränkung |
| | 8.15 Protokollierung |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmen | Relevanz |
|--------|----------|
| Schweizerisches nDSG (revDSG) | Art. 8 — Technische und organisatorische Massnahmen (Aufgabentrennung als organisatorische Massnahme zum Schutz der Datenverarbeitungsintegrität) |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen für die Datensicherheit |
| Schweizerisches OR Art. 728a | Internes Kontrollsystem — Prüfer untersuchen Existenz des ICS einschliesslich Aufgabentrennungskontrollen |
| EU DSGVO (soweit anwendbar) | Art. 32 — Sicherheit der Verarbeitung (angemessene technische und organisatorische Massnahmen) |
| ISO/IEC 27001:2022 | Annex A Massnahme 5.3 — Aufgabentrennung |
| ISO/IEC 27002:2022 | Abschnitt 5.3 — Implementierungsleitfaden für Aufgabentrennung |
| NIST SP 800-53 Rev 5 | AC-5 (Aufgabentrennung) — Aufteilung von Missionsaufgaben auf verschiedene Personen oder Rollen |
| CIS Controls v8 | Control 5 (Kontoverwaltung) und Control 6 (Zugangskontrollmanagement) — Massnahmen zur Unterstützung der Aufgabentrennung durch Zugangsverwaltung |
| COSO Internal Control Framework | Prinzip 10 — Aufgabentrennung als Teil der Kontrollaktivitäten |

---

<!-- QA_VERIFIED: 2026-03-29 -->
