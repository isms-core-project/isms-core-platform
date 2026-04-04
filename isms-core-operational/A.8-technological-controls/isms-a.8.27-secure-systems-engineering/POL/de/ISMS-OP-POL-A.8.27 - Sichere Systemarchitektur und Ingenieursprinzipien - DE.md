<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.27-DE:operational:OP-POL:a.8.27 -->
**ISMS-OP-POL-A.8.27 — Sichere Systemarchitektur und Ingenieursprinzipien**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Sichere Systemarchitektur und Ingenieursprinzipien |
| **Dokumenttyp** | Operative Richtlinie |
| **Dokument-ID** | ISMS-OP-POL-A.8.27 |
| **Dokumentersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteigentümer** | Geschäftsführer (GF) |
| **Genehmigt durch** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB | Initiale operative Richtlinie für ISO 27001:2022 |

**Prüfzyklus**: Jährlich
**Nächstes Prüfdatum**: [Effective Date + 12 months]

**Genehmigt durch**: [Informationssicherheitsbeauftragter / Geschäftsleitung]

**Verwandte Dokumente**:

- ISO/IEC 27001:2022 Massnahme A.8.27 — Sichere Systemarchitektur und Ingenieursprinzipien
- ISO/IEC 27002:2022 Abschnitt 8.27 — Implementierungsleitfaden
- NIST SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems
- NIST SP 800-207 — Zero Trust Architecture
- NIST SP 800-53 Rev 5 SA-8 — Security and Privacy Engineering Principles
- CIS Controls v8 — Safeguards 4.1, 16.1–16.14 (Sicherheit von Anwendungssoftware)

**Verwandte Annex-A-Massnahmen**:

| Massnahme | Bezug zur sicheren Systemarchitektur |
|-----------|--------------------------------------|
| A.5.8 Informationssicherheit im Projektmanagement | Anforderungen an die Sicherheitsarchitektur in die Projektsteuerung integriert |
| A.8.25 Sicherer Entwicklungslebenszyklus | Architekturprinzipien prägen den Entwicklungsprozessrahmen |
| A.8.26 Sicherheitsanforderungen an Anwendungen | Aus Architekturprinzipien abgeleitete Sicherheitsanforderungen |
| A.8.28 Sicheres Coding | Coding-Standards implementieren Architekturprinzipien auf Code-Ebene |
| A.8.29 Sicherheitstests in Entwicklung und Abnahme | Tests validieren die korrekte Implementierung der Architekturprinzipien |
| A.8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen | Umgebungssegregation ist ein zentrales Architekturprinzip |
| A.8.9 Konfigurationsmanagement | Konfigurationsbaselines setzen sichere Architekturstandards durch |
| A.8.20–22 Netzwerksicherheit | Netzwerkarchitektur implementiert Segmentierung und Tiefenverteidigung |
| A.8.2–3–5 Authentifizierung und privilegierter Zugriff | Authentifizierungsarchitektur implementiert Zero-Trust-Prinzipien |
| A.5.19–23 Lieferanten und Cloud-Dienste | Drittanbietersysteme unterliegen der Architekturprüfung |

**Verwandte interne Richtlinien**:

- Richtlinie zum sicheren Entwicklungslebenszyklus
- Netzwerksicherheitsrichtlinie
- Richtlinie zur Authentifizierung und zu privilegiertem Zugriff
- Richtlinie zum Konfigurationsmanagement
- Richtlinie zur Informationssicherheit im Projektmanagement
- Richtlinie zum Einsatz von Kryptographie

---

# Richtlinie zur sicheren Systemarchitektur und zu Ingenieursprinzipien

## Zweck

Zweck dieser Richtlinie ist es, die Regeln und Prinzipien für die Konstruktion sicherer Informationssysteme festzulegen und sicherzustellen, dass Sicherheit von Anfang an in die Systemarchitektur eingebaut wird und nicht erst nach dem Deployment hinzugefügt wird. Diese Richtlinie definiert die grundlegenden sicheren Ingenieursprinzipien, die auf alle Aktivitäten zur Systementwicklung, -beschaffung, -integration und -modifikation angewendet werden sollen.

Diese Richtlinie unterstützt das schweizerische nDSG (revDSG), indem Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen (Art. 7) sowie technische und organisatorische Massnahmen entsprechend dem Risiko (Art. 8) implementiert werden. Das nDSG verlangt, dass Entwickler den Schutz und die Achtung der Privatsphäre der betroffenen Personen in die Struktur der Produkte und Dienste integrieren, die Personendaten bearbeiten, und dass das höchste Sicherheitsniveau standardmässig ohne Benutzereingriff aktiviert ist. Sofern die Organisation Daten von Personen im EU/EWR-Raum bearbeitet, gelten auch die DSGVO-Anforderungen (Art. 25 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 32 — Sicherheit der Verarbeitung).

## Geltungsbereich

Alle Informationssysteme, die von der Organisation konzipiert, entwickelt, beschafft, integriert, betrieben und gepflegt werden, einschliesslich:

- Intern entwickelter Anwendungen, APIs und Dienste.
- Infrastruktur- und Plattformarchitektur (on-premises und Cloud).
- Von Drittanbietern entwickelter oder beschaffter Systeme, die in die Umgebung der Organisation integriert sind.
- Cloud-Dienste, SaaS-Plattformen und verwaltete Dienste, bei denen die Organisation die Architektur definiert oder beeinflusst.
- Betriebstechnologie (OT) und industrielle Steuerungssysteme (ICS), sofern anwendbar.

Alle Mitarbeitenden, Auftragnehmer und Drittnutzer, die an der Systemkonzeption, -architektur, -entwicklung und -konstruktion beteiligt sind.

**Nicht im Geltungsbereich**: Eigenständige Endbenutzergeräte, die gemäss der Endgerätesicherheitsrichtlinie (A.8.1-7-18-19) verwaltet werden, sofern sie nicht Teil einer im Rahmen einer Architekturprüfung befindlichen Systemarchitektur sind. Physische Infrastruktur wird durch die Richtlinie zur physischen Sicherheit (A.7.x) geregelt.

## Grundsatz

Prinzipien für die Konstruktion sicherer Systeme sollen eingerichtet, dokumentiert, gepflegt und auf alle Aktivitäten zur Informationssystementwicklung angewendet werden. Sicherheit soll als grundlegende Eigenschaft des Systemdesigns behandelt werden — nicht als nachträgliche oder aufgesetzte Ergänzung.

Alle Architektur- und Konstruktionsentscheidungen sollen risikobasiert sein und den Wert und die Klassifizierung der verarbeiteten Informationen, die für das System relevante Bedrohungslandschaft, regulatorische Anforderungen und die Risikobereitschaft der Organisation berücksichtigen.

Wenn der Organisation dedizierte Sicherheitsarchitekturressourcen fehlen — eine häufige Situation in kleinen und mittelständischen Organisationen — soll der ISB die Funktion des Sicherheitsarchitekten wahrnehmen, und für Hochrisikosysteme soll eine externe Fachprüfung eingeholt werden.

---

## Sichere Ingenieursprinzipien

Die Organisation soll eine Reihe von sicheren Ingenieursprinzipien einrichten, dokumentieren und pflegen, die auf alle Aktivitäten zur Systementwicklung und -beschaffung angewendet werden. Diese Prinzipien sollen jährlich überprüft und aktualisiert werden, um Änderungen in der Bedrohungslandschaft, technologischen Standards und regulatorischen Anforderungen widerzuspiegeln.

### Prinzip 1: Security by Design

Sicherheit soll von den frühesten Phasen der Systemkonzeption an integriert werden:

- Sicherheitsanforderungen sollen während der initialen Konzeptentwicklung zusammen mit den funktionalen Anforderungen identifiziert werden.
- Die Sicherheitsarchitektur soll vor Beginn des Detaildesigns definiert werden.
- Sicherheitsmassnahmen sollen als integrale Systemkomponenten konzipiert werden, nicht als Ergänzungen nach der Fertigstellung der Kernfunktionalität.
- Sicherheitskompromisse sollen explizit dokumentiert werden, mit Risikoakzeptanz, die vom ISB vor dem Fortfahren genehmigt wurde.

### Prinzip 2: Security by Default

Systeme sollen in ihrer Standardkonfiguration sicher sein:

- Standardkonfigurationen sollen die restriktivsten, dem beabsichtigten Zweck des Systems angemessenen Sicherheitseinstellungen implementieren.
- Benutzer sollen keine Massnahmen ergreifen müssen, um das System zu sichern — Sicherheit soll ab der ersten Nutzung aktiv sein.
- Optionale Sicherheitsfunktionen sollen standardmässig aktiviert sein, sofern keine dokumentierte geschäftliche Begründung für ihre Deaktivierung vorliegt.
- Default-Deny soll auf Zugriffskontrollen, Netzwerkkommunikationen und Systemfähigkeiten angewendet werden.
- Administrative Schnittstellen sollen standardmässig deaktiviert oder eingeschränkt sein.
- Anwendungsfunktionen, die erhöhte Privilegien erfordern, sollen explizit aktiviert werden, nicht standardmässig aktiviert sein (z. B. Debug-Logging, Remote-Administration).

**Datenschutz durch Voreinstellung (nDSG Art. 7)**:

- Standardeinstellungen sollen die Erhebung von Personendaten minimieren (Datensparsamkeit).
- Datenschutzfördernde Funktionen sollen standardmässig aktiviert sein (z. B. Datenanonymisierung, Zweckbindungsdurchsetzung).
- Einwilligungsmechanismen sollen standardmässig auf Opt-in, nicht Opt-out eingestellt sein.
- Datenaufbewahrung soll standardmässig auf den kürzestmöglichen Zeitraum eingestellt sein, sofern keine geschäftliche Begründung für eine längere Aufbewahrung vorliegt.

### Prinzip 3: Tiefenverteidigung (Defence in Depth)

Mehrere Sicherheitsmassnahmenschichten sollen implementiert werden, damit kein einzelner Ausfall zu einer vollständigen Kompromittierung führt:

- Keine einzelne Massnahme soll der einzige Schutz für kritische Werte sein.
- Massnahmen sollen auf mehreren Architekturebenen implementiert werden: Netzwerk, Plattform, Anwendung und Daten.
- Der Ausfall einer Massnahmenschicht soll nicht zu einer vollständigen Kompromittierung des Systems führen.
- Schichtweise Massnahmen sollen komplementär sein — jede Schicht adressiert unterschiedliche Angriffsvektoren.

**Schichten der Tiefenverteidigung**:

| Schicht | Sicherheitsmassnahmen |
|---------|----------------------|
| **Perimeter** | Firewalls, Web Application Firewalls (WAF), DDoS-Schutz, sichere Gateways |
| **Netzwerk** | Segmentierung, Netzwerkzugangskontrolle, IDS/IPS, verschlüsselte interne Kommunikation |
| **Plattform** | Gehärtete Konfigurationen, Patch-Management, Endgeräteschutz, Secure Boot |
| **Anwendung** | Eingabevalidierung, Ausgabekodierung, Authentifizierung, Autorisierung, Session-Management |
| **Daten** | Verschlüsselung im Ruhezustand und bei der Übertragung, Zugriffskontrollen, Datenmaskierung, Data Loss Prevention |
| **Identität** | Multi-Faktor-Authentifizierung, Privileged Access Management, Identity Governance |
| **Überwachung** | Zentrale Protokollierung, Verhaltensanalyse, Bedrohungserkennung, Incident Response |

### Prinzip 4: Minimale Rechtevergabe (Least Privilege)

Alle Benutzer, Prozesse und Systeme sollen mit den minimalen Privilegien betrieben werden, die zur Erfüllung ihrer autorisierten Funktion erforderlich sind:

- Zugriffsrechte sollen auf das für die spezifische Aufgabe Erforderliche beschränkt sein.
- Erhöhte Privilegien sollen nur bei Bedarf gewährt und widerrufen werden, wenn sie nicht mehr benötigt werden.
- Dienstkonten sollen über eng begrenzte Berechtigungen verfügen, die auf spezifische Ressourcen und Vorgänge beschränkt sind (kein vollständiger Datenbankzugriff, kein Domain-Administrator).
- Administrativer Zugriff soll vom täglichen Betriebszugriff getrennt werden.

### Prinzip 5: Minimale Funktionalität (Least Functionality)

Systeme sollen nur die für ihren vorgesehenen Zweck erforderlichen Fähigkeiten bereitstellen:

- Unnötige Dienste, Protokolle und Funktionen sollen deaktiviert oder entfernt werden.
- Die Angriffsfläche soll durch Funktionsreduzierung minimiert werden.
- Ungenutzte Ports, Schnittstellen und Fähigkeiten sollen deaktiviert werden.
- Standard-Beispielinhalte, Testseiten und ungenutzte Module sollen vor dem Deployment entfernt werden.

### Prinzip 6: Sicheres Versagen (Fail Secure)

Systeme sollen in einem sicheren Zustand versagen, der keine sensiblen Daten oder Funktionen freilegt:

- Systemausfälle sollen standardmässig den Zugriff verweigern statt ihn zu gewähren.
- Fehlerzustände sollen keine sicherheitsrelevanten Informationen preisgeben (Stack Traces, interne Pfade, Datenbankdetails, Versionsnummern).
- Die Wiederherstellung nach einem Ausfall soll eine erneute Authentifizierung und Autorisierung erfordern.
- Graceful degradation soll Sicherheitsmassnahmen auch bei reduzierter Leistung aufrechterhalten.
- Ausfallsereignisse sollen für die Sicherheitsüberwachung und Incident-Untersuchung protokolliert werden.

**Beispiele für sicheres Versagen**:

Korrekt (sicheres Versagen):

- Datenbankverbindungsausfall: Anwendung gibt generischen Fehler zurück, verweigert Zugriff.
- Authentifizierungsdienst nicht verfügbar: System verweigert Anmeldung, umgeht Authentifizierung nicht.
- Firewall-Regelverarbeitungsfehler: Standard-Deny, Verkehr blockieren.
- Verschlüsselungsschlüssel nicht verfügbar: Datenzugriff verweigert bis Schlüssel wiederhergestellt.

Falsch (unsicheres Versagen — vermeiden):

- Datenbankverbindungsausfall: Anwendung gewährt Zugriff unter der Annahme, dass Anmeldedaten gültig sind.
- Authentifizierungsdienst nicht verfügbar: System erlaubt Anmeldung mit zwischengespeicherten Anmeldedaten ohne Ablaufprüfung.
- Firewall-Regelverarbeitungsfehler: Fail Open, allen Verkehr zulassen.
- Verschlüsselungsschlüssel nicht verfügbar: Daten unverschlüsselt bereitgestellt.

### Prinzip 7: Reduzierte Komplexität

Systemdesigns sollen Einfachheit bevorzugen — komplexe Systeme sind schwerer zu sichern, zu verifizieren und zu pflegen:

- Komponenten sollen gut definierte Schnittstellen mit klaren Sicherheitsgrenzen haben.
- Systeme sollen mit unabhängigen, lose gekoppelten Modulen konzipiert werden, die unabhängig gesichert, aktualisiert und validiert werden können.
- Gemeinsam genutzte Ressourcen sollen minimiert werden, um die Angriffsfläche zu reduzieren und unbefugte Informationsflüsse zwischen Komponenten zu verhindern.
- Abhängigkeiten zwischen Komponenten sollen klar definiert und dokumentiert sein.

**Komplexitätsmanagement**:

Komplexität soll verwaltet werden durch:

- **Modulares Design**: Komponenten mit einem einzigen, klar definierten Zweck.
- **Schnittstellenbegrenzung**: Externe Schnittstellen auf das Notwendigste beschränken (jede externe Integration dokumentieren und begründen).
- **Abhängigkeitsverfolgung**: Abhängigkeitskarte für kritische Systeme pflegen; Ziel: weniger als 10 externe Abhängigkeiten für Tier-1-Systeme.
- **Zyklomatische Komplexität**: Code-Komplexitätsmetriken während der Entwicklung verfolgen (Ziel: weniger als 10 pro Funktion für sicherheitskritischen Code).

**Auslöser für Komplexitätsprüfung**:

- System erfordert mehr als 5 verschiedene Authentifizierungsmechanismen.
- Mehr als 15 externe Systemintegrationen.
- Gemeinsam genutzte Ressourcen zwischen Vertrauensgrenzen ohne Isolation.
- Entwicklungsteam kann den Datenfluss nicht in weniger als 15 Minuten erklären.

---

## Zero-Trust-Architekturprinzipien

Die Organisation soll Zero-Trust-Prinzipien für alle neuen Systeme übernehmen und sie schrittweise auf bestehende Systeme anwenden:

**Niemals vertrauen, immer verifizieren**:

- Kein implizites Vertrauen soll auf der Grundlage des Netzwerkstandorts, der Geräteeigenschaft oder der vorherigen Authentifizierung gewährt werden.
- Jede Zugriffsanfrage soll unabhängig von der Quelle — intern oder extern — authentifiziert und autorisiert werden.
- Vertrauen soll kontinuierlich bewertet werden, nicht nach der initialen Verifizierung als selbstverständlich angenommen werden.

**Kompromittierung annehmen**:

- Systeme sollen in der Annahme konzipiert werden, dass Angreifer möglicherweise bereits Zugang zu internen Netzwerken haben.
- Interner Netzwerkverkehr soll als potenziell feindlich behandelt werden.
- Laterale Bewegungen sollen durch Segmentierung und Zugriffskontrollen eingeschränkt werden.
- Erkennungsfähigkeiten sollen davon ausgehen, dass Perimetermassnahmen versagt haben könnten.
- Endpoint Detection and Response (EDR) soll auf allen verwalteten Geräten eingesetzt werden, um Post-Kompromiss-Aktivitäten zu erkennen.

**Explizit verifizieren**:

- Zugriffsentscheidungen sollen alle verfügbaren Datenpunkte berücksichtigen: Benutzeridentität, Gerätezustand, Datensensibilität, Zugriffskontext (Standort, Zeit, Verhalten) und Anfrageanomalieindikatoren.
- Zugriffsentscheidungen sollen für Audit- und Untersuchungszwecke protokolliert werden.

**Minimale Rechtevergabe beim Zugriff**:

- Just-in-time (JIT)-Zugriff für erhöhte Privilegien — Zugriff nur bei Bedarf gewähren, automatisch widerrufen wenn die Aufgabe abgeschlossen ist.
- Just-enough-access (JEA) für alle Zugriffsgenehmigungen — keine dauerhaften umfangreichen Berechtigungen.
- Risikobasierte Conditional-Access-Richtlinien, die über den Identitätsanbieter durchgesetzt werden.

**Zero-Trust-Implementierungsansatz**:

| Phase | Aktivitäten | Zielzeitrahmen |
|-------|-----------|----------------|
| **Phase 1: Grundlage** | Identitätszentrierte Zugriffssteuerung, MFA für alle Benutzer, Gerätezustandsverifizierung | Innerhalb von 12 Monaten nach Richtliniengenehmigung |
| **Phase 2: Netzwerk** | Mikrosegmentierung für kritische Systeme, verschlüsselte interne Kommunikation, Netzwerkzugangskontrolle | Innerhalb von 24 Monaten |
| **Phase 3: Kontinuierlich** | Kontinuierliche Zugriffsbewertung, Verhaltensanalyse, automatisierte Reaktion auf Anomalien | Innerhalb von 36 Monaten |

**Zero-Trust-Implementierungszeitpläne**: Die angezeigten Zeitpläne gehen von einer mittelgrossen Organisation (50–200 Mitarbeitende) mit moderater technischer Schuld aus. Anpassen basierend auf:

- **Kleine Organisationen (<50 Mitarbeitende)**: Zeitpläne können bei Cloud-nativer Infrastruktur 50 % kürzer sein.
- **Grosse Organisationen (>200 Mitarbeitende)**: Zeitpläne können aufgrund von Legacy-Systemen und organisatorischer Komplexität 50 % länger sein.
- **Grad der technischen Schuld**: Organisationen mit erheblicher On-Premises-Infrastruktur benötigen längere Phase-2-Zeitpläne.

Fortschritte sollen jährlich anhand der organisationsspezifischen Roadmap bewertet werden, nicht anhand absoluter Kalenderdaten.

Von der Organisation wird nicht erwartet, sofortige vollständige Zero-Trust-Reife zu erreichen. Jede Phase soll geplant, mit Ressourcen ausgestattet und überprüft werden. Fortschritte sollen der Geschäftsleitung jährlich gemeldet werden.

---

## Sicherheitsarchitekturdokumentation

Alle als Hoch- oder Mittleres-Risiko klassifizierten Systeme sollen dokumentierte Sicherheitsarchitektur haben. Niedrigrisiko-Systeme sollen mindestens eine ausgefüllte Sicherheitscheckliste haben.

### Dokumentationsanforderungen

**Hochrisikosysteme**:

| Dokument | Inhalt | Verantwortlicher |
|----------|--------|-----------------|
| **Sicherheitsarchitekturdokument (SAD)** | Systemübersicht, Vertrauensgrenzen, Datenflüsse, Sicherheitsmassnahmen je Schicht, Integrationspunkte, Bedrohungskontext | ISB / Sicherheitsarchitekt |
| **Bedrohungsmodell** | Identifizierte Bedrohungen, Angriffsvektoren, Risikobewertungen, Massnahmen, Restrisiken | ISB / Sicherheitsarchitekt |
| **Rückverfolgbarkeitsmatrix für Sicherheitsanforderungen** | Sicherheitsanforderungen, die Designelementen und Testfällen zugeordnet sind | Systemeigentümer |
| **Architecture Decision Records (ADRs)** | Sicherheitsrelevante Designentscheidungen mit Begründung und berücksichtigten Alternativen | Systemeigentümer / Entwicklungsleiter |

**Systeme mit mittlerem Risiko**:

| Dokument | Inhalt | Verantwortlicher |
|----------|--------|-----------------|
| **Sicherheitsarchitekturzusammenfassung** | Vereinfachtes SAD mit Vertrauensgrenzen, Datenflüssen und Schlüsselmassnahmen | Systemeigentümer |
| **Bedrohungsbewertung** | Leichtgewichtige Bedrohungsidentifikation und Massnahmenplanung | ISB |

**Niedrigrisikosysteme**:

- Sicherheitsdesign-Checkliste (ausgefüllt und vom ISB oder Beauftragten abgezeichnet).

**Dokumentenspeicherung**: Sicherheitsarchitekturdokumentation soll in [Architektur-Tool / Confluence / SharePoint] gespeichert werden, mit Zugriff beschränkt auf: ISB, Entwicklungsleiter, Systemeigentümer und Personal mit dokumentiertem, vom ISB genehmigtem Need-to-know. Dokumentation soll versionskontrolliert sein.

**Aktualität der Dokumentation**: Sicherheitsarchitekturdokumentation soll überprüft und aktualisiert werden: wenn wesentliche Änderungen am System vorgenommen werden, wenn neue Bedrohungen identifiziert werden, die das System betreffen, und mindestens jährlich für Hochrisikosysteme.

---

## Architekturprüfungsprozess

Alle neuen Systeme und wesentliche Änderungen an bestehenden Systemen sollen vor der Implementierung einer Sicherheitsarchitekturprüfung unterzogen werden.

### Prüfungsauslöser

Eine Sicherheitsarchitekturprüfung ist erforderlich, wenn:

- Ein neues System entwickelt oder beschafft wird.
- Ein grösseres Versions-Upgrade oder eine Plattformmigration stattfindet.
- Architekturände­rungen Sicherheitsgrenzen oder Vertrauenszonen betreffen.
- Neue externe Dienste oder Datenflüsse integriert werden.
- Authentifizierungs- oder Autorisierungsmechanismen geändert werden.
- Die Datenklassifizierung der verarbeiteten Informationen steigt.
- Ein Sicherheitsincident architektonische Schwächen aufgedeckt hat.

### Prüfungsprozess

| Schritt | Aktivität | Verantwortlicher |
|---------|-----------|-----------------|
| 1. **Einleitung** | Systemeigentümer reicht Architekturprüfungsantrag mit Systemdokumentation ein | Systemeigentümer |
| 2. **Bedrohungsmodellierung** | Bedrohungsmodellierung mit STRIDE-Methodik durchführen (Pflicht für Hochrisiko; empfohlen für mittleres Risiko) | ISB / Sicherheitsarchitekt |
| 3. **Anforderungsvalidierung** | Vollständigkeit der Sicherheitsanforderungen und Ausrichtung auf Geschäftsanforderungen verifizieren | ISB |
| 4. **Musterpüfung** | Architektur gegen genehmigte sichere Muster bewerten; Abweichungen identifizieren | ISB / Sicherheitsarchitekt |
| 5. **Tiefenverteidigungsvalidierung** | Sicherstellen, dass Massnahmen über alle relevanten Architekturschichten implementiert sind | ISB |
| 6. **Risikobeurteilung** | Restrisiken und Behandlungspläne für identifizierte Lücken dokumentieren | ISB / Systemeigentümer |
| 7. **Genehmigung** | ISB genehmigt oder gibt mit erforderlichen Änderungen zurück | ISB |

**Genehmigungskriterien**: Architektur soll nicht genehmigt werden, wenn:

- Die Bedrohungsmodellierung nicht abgeschlossen wurde (Hochrisikosysteme).
- Kritische oder hohe Risiken ohne Behandlungspläne bestehen.
- Tiefenverteidigung für Systeme fehlt, die vertrauliche oder eingeschränkte Daten verarbeiten.
- Abweichungen von genehmigten Architekturmustern keine kompensierenden Massnahmen und ISB-Ausnahmengenehmigung haben.

**Prüfungs-SLA**:

- Hochrisikosysteme (mit vollständigem Bedrohungsmodell): 15 Werktage ab vollständiger Einreichung.
- Systeme mit mittlerem Risiko (Zusammenfassungsprüfung): 10 Werktage.
- Niedrigrisikosysteme (Checklisten-Prüfung): 5 Werktage.

Unvollständige Einreichungen sollen innerhalb von 3 Werktagen mit spezifisch identifizierten Lücken zurückgegeben werden. Die Frist beginnt erneut bei Wiedereinreichung vollständiger Dokumentation.

### Architekturprüfungs-Checkliste (Systeme mit mittlerem und hohem Risiko)

**Identität und Zugriff**:

- [ ] Authentifizierungsmechanismus dokumentiert (SSO, MFA, API-Schlüssel).
- [ ] Autorisierungsmodell definiert (RBAC, ABAC).
- [ ] Trennung des privilegierten Zugriffs implementiert.
- [ ] Berechtigungen von Dienstkonten minimiert.

**Datenschutz**:

- [ ] Datenklassifizierung für alle verarbeiteten Daten identifiziert.
- [ ] Verschlüsselung im Ruhezustand für vertrauliche/eingeschränkte Daten implementiert.
- [ ] Verschlüsselung bei der Übertragung (TLS 1.2+) für alle Netzwerkkommunikationen.
- [ ] Datenaufbewahrung und -löschmechanismen definiert.

**Netzwerksicherheit**:

- [ ] Netzwerksegmentierung dem System-Tier angemessen.
- [ ] Ein- und ausgehende Firewall-Regeln dokumentiert und begründet.
- [ ] API-Gateway oder WAF für internetfähige Anwendungen.
- [ ] Interne Kommunikationen bei Verarbeitung sensibler Daten verschlüsselt.

**Tiefenverteidigung**:

- [ ] Mindestens 3 Massnahmenschichten verifiziert (Netzwerk, Plattform, Anwendung, Daten).
- [ ] Analyse des Single Point of Failure durchgeführt.
- [ ] Komplementäre Massnahmen bestätigt (unterschiedliche Angriffsvektoren adressiert).

**Überwachung und Protokollierung**:

- [ ] Protokollierung von Sicherheitsereignissen konfiguriert.
- [ ] Protokollweiterleitung an zentrale SIEM-/Protokollierungsplattform.
- [ ] Alarmierungsregeln für kritische Ereignisse definiert.
- [ ] Protokollaufbewahrung erfüllt Richtlinienanforderungen.

**Resilienz**:

- [ ] Backup- und Wiederherstellungsverfahren dokumentiert.
- [ ] RPO/RTO definiert und validiert.
- [ ] Notfallwiederherstellungsplan vorhanden (Tier-1-Systeme).
- [ ] Redundanz für kritische Komponenten implementiert.

**Bedrohungsmodellierung** (nur Hochrisiko):

- [ ] STRIDE-Analyse abgeschlossen.
- [ ] Angriffsvektoren dokumentiert.
- [ ] Massnahmen jeder Bedrohung zugeordnet.
- [ ] Restrisiken vom ISB akzeptiert.

**Konformität**:

- [ ] nDSG/DSGVO-Anforderungen bewertet (bei Verarbeitung von Personendaten).
- [ ] Branchenspezifische Regulierungen adressiert (sofern anwendbar).
- [ ] Datenschutz durch Technik und Voreinstellung demonstriert.

### Externe Sicherheitsarchitekturprüfung

Organisationen sollen externe Sicherheitsarchitekturspezialisten einschalten, wenn:

| Auslöser | Begründung |
|----------|-----------|
| **Neues Hochrisikosystem** intern entwickelt ohne vorherige Erfahrung mit sicherer Architektur | Unabhängige Validierung von Bedrohungsmodell und Designentscheidungen |
| **Kryptographisches Systemdesign** (individuelle Implementierungen, Schlüsselmanagement) | Spezialisiertes Kryptographie-Know-how erforderlich |
| **Zahlungsverarbeitungssystem** | PCI-DSS-Konformität und spezialisierte Sicherheitsanforderungen |
| **Zero-Trust-Implementierung** (initiales Design) | Komplexe Architektur erfordert spezialisiertes Zero-Trust-Know-how |
| **Wesentlicher Incident** hat architektonische Schwäche aufgedeckt | Unabhängige Ursachenanalyse und Behebungsleitfaden |
| **Fusions-/Übernahme-Integration** | Drittanbieter-Bewertung der Sicherheitslage der kombinierten Architektur |
| **Regulatorischer Auditbefund** im Zusammenhang mit Architektur | Unabhängige Validierung des Behebungsdesigns |

Externe Prüfer sollen ausgewählt werden anhand von: relevanten Branchenzertifizierungen (CISSP, CCSP oder gleichwertig), nachgewiesener Erfahrung mit ähnlichen Architekturen und Unabhängigkeit von Implementierungslieferanten.

### Bedrohungsmodellierung

Wo eine Bedrohungsmodellierung erforderlich ist, soll die STRIDE-Methodik als primärer Ansatz verwendet werden:

| STRIDE-Kategorie | Bedrohungstyp | Beispiel |
|-----------------|--------------|---------|
| **Spoofing** | Identitätsimitation | Diebstahl von Anmeldedaten, Session-Hijacking |
| **Tampering** | Unautorisierte Modifikation | Datenmanipulation, Konfigurationsänderung |
| **Repudiation** | Bestreiten von Handlungen | Fehlen von Audit-Trails |
| **Information Disclosure** | Datenexposition | Unverschlüsselte Daten, ausführliche Fehlermeldungen |
| **Denial of Service** | Verfügbarkeitsstörung | Ressourcenerschöpfung, Flooding |
| **Elevation of Privilege** | Erlangen unautorisierten Zugriffs | Privilegieneskalation, Injection-Angriffe |

Bedrohungsmodelle sollen aufbewahrt werden für:

- **Aktive Systeme**: Lebenszyklus des Systems plus 3 Jahre nach Ausserbetriebnahme.
- **Wesentliche Incidents**: Bedrohungsmodelle für in Sicherheitsincidents involvierte Systeme sollen dauerhaft aufbewahrt werden (mindestens 7 Jahre).

Bedrohungsmodelle sollen überprüft und aktualisiert werden: bei jedem Major Release, wenn sich die Systemarchitektur wesentlich ändert, wenn neue für das System relevante Bedrohungsintelligenz identifiziert wird, und mindestens jährlich für Hochrisikosysteme.

---

## Sicherheitskriterien für die Technologieauswahl

Bei der Auswahl neuer Technologien, Plattformen, Frameworks oder Drittkomponenten soll Sicherheit ein Auswahlkriterium mit gleichem Gewicht wie funktionale Anforderungen sein.

### Auswahlkriterien

| Kriterium | Anforderung |
|-----------|-------------|
| **Sicherheitslage des Anbieters** | Anbieter liefert Nachweis sicherer Entwicklungspraktiken (z. B. SOC-2-, ISO-27001-Zertifizierung oder gleichwertig) |
| **Schwachstellengeschichte** | Kein Muster nicht behobener kritischer Schwachstellen; nachgewiesene zeitnahe Patch-Bereitstellung |
| **Sichere Standardeinstellungen** | Technologie wird mit sicherer Standardkonfiguration geliefert; erfordert keine umfangreiche Härtung, um einen akzeptablen Zustand zu erreichen |
| **Verschlüsselungsunterstützung** | Unterstützt aktuelle Verschlüsselungsstandards (mindestens TLS 1.2, TLS 1.3 bevorzugt; AES-256 für Daten im Ruhezustand) |
| **Authentifizierungsintegration** | Unterstützt Integration mit dem Identitätsanbieter der Organisation (SAML, OIDC oder gleichwertig) |
| **Protokollierung und Auditierbarkeit** | Stellt Sicherheitsereignisprotokollierung bereit, die mit der Protokollierungsinfrastruktur der Organisation kompatibel ist |
| **Update- und Patch-Mechanismus** | Anbieter stellt regelmässige Sicherheitsupdates mit klarem Advisory-Prozess bereit |
| **End-of-Life-Roadmap** | Klarer Support-Lebenszyklus; keine Technologie am End-of-Life oder innerhalb von 12 Monaten vor End-of-Life soll ausgewählt werden |
| **Regulatorische Konformität** | Technologie unterstützt die Einhaltung der Anforderungen von nDSG, DSGVO (sofern anwendbar) und ISO 27001 |

Technologieauswahlentscheidungen für Hochrisikosysteme sollen mit Sicherheitsbewertungsnachweisen dokumentiert und vom ISB vor der Beschaffung genehmigt werden.

---

## Sicherheitsbaselines

Die Organisation soll Sicherheitsbaselines für jeden System-Tier pflegen, die die erforderlichen Mindestsicherheitsmassnahmen definieren.

### System-Tier-Klassifizierung

| Tier | Beschreibung | Beispielsysteme |
|------|-------------|----------------|
| **Tier 1 — Kritisch** | Systeme, die vertrauliche oder eingeschränkte Daten verarbeiten; internetfähig; kritische Geschäftsfunktion | ERP, CRM mit Kunden-Personendaten, Zahlungssysteme, öffentlich zugängliche Webanwendungen |
| **Tier 2 — Wichtig** | Systeme, die interne Daten verarbeiten; begrenzte externe Exposition; unterstützende Geschäftsfunktion | Interne Kollaborationstools, Projektmanagement, interne Berichterstattung |
| **Tier 3 — Standard** | Systeme, die ausschliesslich öffentliche Daten verarbeiten; keine Personendaten; nicht kritische Funktion | Marketing-Website (statischer Inhalt), interne Wikis (nicht sensibel) |

**Neuklassifizierung des System-Tiers**:

Der System-Tier soll überprüft und potenziell neu klassifiziert werden, wenn:

- **Datenklassifizierung steigt**: System beginnt, vertrauliche oder eingeschränkte Daten zu verarbeiten (z. B. Tier 3 zu Tier 1 umklassifiziert).
- **Internet-Exposition ändert sich**: Internes System wird internetfähig (z. B. Tier 2 zu Tier 1 umklassifiziert).
- **Geschäftskritikalität steigt**: System wird umsatzkritisch oder eine zentrale Betriebsfunktion (z. B. Tier 2 zu Tier 1 umklassifiziert).
- **Sicherheitsincident aufgetreten**: Incident zeigt, dass das System riskanter ist als ursprünglich bewertet.
- **Regulatorischer Umfang erweitert sich**: System beginnt, regulierungsunterliegende Daten zu verarbeiten (PCI DSS, DSGVO).

Eine Neuklassifizierung löst aktualisierte Sicherheitsbaselineanforderungen und eine Architekturprüfung aus. Der Systemeigentümer soll beim Auftreten eines Auslösers eine Neuklassifizierungsprüfung beim ISB beantragen.

### Baselineanforderungen nach Tier

| Massnahmenbereich | Tier 1 (Kritisch) | Tier 2 (Wichtig) | Tier 3 (Standard) |
|-------------------|-------------------|-----------------|-------------------|
| **Authentifizierung** | MFA obligatorisch; SSO-Integration; Session-Timeouts | MFA obligatorisch; SSO-Integration | Passwortrichtlinien-Konformität |
| **Verschlüsselung bei Übertragung** | TLS 1.3 erforderlich (TLS 1.2 Ausnahme mit ISB-Genehmigung) | Mindestens TLS 1.2 | Mindestens TLS 1.2 |
| **Verschlüsselung im Ruhezustand** | AES-256 obligatorisch | AES-256 für Personendaten/sensible Daten | Erforderlich für Systeme, die Personendaten verarbeiten (Namen, E-Mail-Adressen), auch wenn nicht besonders sensibel; nicht erforderlich für wirklich öffentliche Daten |
| **Netzwerksegmentierung** | Dediziertes Segment; Mikrosegmentierung sofern machbar | Vom nicht vertrauenswürdigen Netzwerk segmentiert | Standard-Netzwerkmassnahmen |
| **Protokollierung** | Alle Sicherheitsereignisse an zentrales [SIEM]; Echtzeit-Alarmierung | Sicherheitsereignisse an zentrale Protokollierung | Grundlegende Zugriffsprotokollierung |
| **Schwachstellenscan** | Kontinuierlich oder wöchentlich | Monatlich | Vierteljährlich |
| **Penetrationstest** | Jährlich + vor erstem Release + nach wesentlicher Änderung | Alle 2 Jahre | Risikobasierte Entscheidung |
| **Architekturprüfung** | Pflicht (vollständige Prüfung mit Bedrohungsmodell) | Pflicht (Zusammenfassungsprüfung) | Sicherheitscheckliste |
| **Backup und Wiederherstellung** | RPO und RTO gemäss BIA definiert; jährlich getestet | Regelmässige Backups; Wiederherstellung getestet | Standard-Backup-Richtlinie |
| **Zugriffsprüfung** | Vierteljährlich | Halbjährlich | Jährlich |

Sicherheitsbaselines sollen jährlich vom ISB überprüft und aktualisiert werden, um aktuelle Bedrohungen, Technologieänderungen und regulatorische Anforderungen widerzuspiegeln.

---

## Sichere Architekturmuster

Die Organisation soll einen Katalog genehmigter sicherer Architekturmuster pflegen, auf den Systemarchitekten beim Aufbau neuer Systeme oder der Modifikation bestehender Systeme verweisen sollen.

**Musterkategorien**:

| Kategorie | Beispiele |
|-----------|----------|
| **Authentifizierung** | SSO-Integration (SAML/OIDC), MFA-Implementierung, API-Schlüsselverwaltung, zertifikatbasierte Authentifizierung |
| **Autorisierung** | Rollenbasierte Zugriffskontrolle (RBAC), attributbasierte Zugriffskontrolle (ABAC), API-Autorisierung (OAuth 2.0) |
| **Datenschutz** | Verschlüsselung im Ruhezustand (AES-256), Verschlüsselung bei Übertragung (TLS 1.3), Tokenisierung für Personendaten, Datenmaskierung |
| **Netzwerksicherheit** | DMZ-Architektur, Mikrosegmentierung, API-Gateway mit WAF, VPN/ZTNA für Fernzugriff |
| **Integration** | Sichere API-Muster (REST mit OAuth 2.0), Message-Queue-Sicherheit, Service Mesh mit mTLS |
| **Cloud** | Landing-Zone-Architektur, Workload-Isolation, Cloud-native Sicherheitsmassnahmen, CSPM-Integration |

Jedes genehmigte Muster soll dokumentieren:

- Sicherheitsbegründung und Bedrohungsminderung.
- Implementierungsleitfaden.
- Häufige Fallstricke und Anti-Muster, die vermieden werden sollen.
- Test- und Validierungskriterien.

**Muster-Governance**:

- Genehmigte Muster sollen jährlich auf weiterhin angemessene Aktualität überprüft werden.
- Abweichungen von genehmigten Mustern erfordern die ISB-Genehmigung mit dokumentierter Begründung und kompensierenden Massnahmen.
- Neue Muster sollen durch Bedrohungsmodellierung validiert werden, bevor sie dem Katalog hinzugefügt werden.

**Beispiel eines genehmigten Musters: SSO-Integration mit SAML 2.0**

**Sicherheitsbegründung**:

- Zentralisiert die Authentifizierung und reduziert Anmeldedatenverzweigung.
- Ermöglicht MFA-Durchsetzung beim Identitätsanbieter.
- Stellt Audit-Trail des Anwendungszugriffs bereit.
- Unterstützt Just-in-time-Provisionierung.

**Implementierungsleitfaden**:

1. Anwendung beim Identitätsanbieter registrieren (Azure AD, Okta, Google Workspace).
2. SAML-Assertions so konfigurieren, dass sie erforderliche Attribute enthalten (E-Mail, Gruppen, MFA-Status).
3. SAML-Antwortsignaturen und Zertifikate validieren.
4. Logout-Propagation implementieren (SLO — Single Logout).
5. Session-Timeout gemäss Organisationsrichtlinie setzen (maximal 4 Stunden).

**Häufige Fallstricke**:

- Nicht signierte SAML-Assertions akzeptieren.
- Zertifikatsablauf nicht validieren.
- Assertion-Inhalt ohne Signaturverifizierung vertrauen.
- Logout-Propagation nicht implementieren (Benutzer bleibt nach IdP-Logout in der Anwendung angemeldet).

**Testkriterien**:

- Anmeldung leitet zum Identitätsanbieter weiter.
- MFA-Durchsetzung im Authentifizierungsfluss sichtbar.
- Ungültige SAML-Antwort abgelehnt.
- Session läuft nach Timeout-Zeitraum ab.
- Abmeldung beim Identitätsanbieter meldet Benutzer von der Anwendung ab.

**Referenzimplementierung**: [Link zum Code-Repository / Wiki]

**Speicherort des Musterkatalogs**: [Architektur-Tool / Confluence / SharePoint] — zugänglich für alle Systemarchitekten und Entwickler.

### Häufige Architektur-Anti-Muster, die vermieden werden sollten

| Anti-Muster | Risiko | Alternative |
|-------------|--------|------------|
| **Gemeinsam genutzte Datenbank über Vertrauensgrenzen hinweg** | Laterale Bewegung; Privilegieneskalation via SQL-Injection | Datenbank pro Dienst oder starke Schema-Isolation mit separaten Anmeldedaten |
| **Hart kodierte Geheimnisse in der Konfiguration** | Anmeldedatenexposition in der Versionskontrolle | Secrets-Management-System (Vault, Key Vault, Secrets Manager) |
| **Authentifizierungsumgehung für «interne» Dienste** | Annahme, dass internes Netzwerk vertrauenswürdig ist | Mutual TLS oder OAuth 2.0 für Service-to-Service-Kommunikation |
| **Protokollierung sensibler Daten (Passwörter, Tokens, Personendaten)** | Konformitätsverstoss; Insiderbedrohung | Protokollschwärzung oder Tokenisierung vor der Protokollierung |
| **Einzelnes Admin-Konto für mehrere Dienste** | Keine Rechenschaftspflicht; Anmeldedatenverzweigung | Dienst-spezifische Admin-Konten mit minimaler Rechtevergabe |
| **Nicht authentifizierte Health-Check-Endpunkte, die Systemdetails preisgeben** | Informationsexposition | Authentifizierte Health Checks oder minimale Antwort (nur HTTP 200) |
| **Direkter Datenbankzugriff von der Web-Tier** | SQL-Injection-Verstärkung; keine Tiefenverteidigung | API-/Service-Schicht zwischen Web und Datenbank |
| **Vertrauen auf clientseitige Validierung** | Triviale Umgehung | Serverseitige Validierung; clientseitig nur als UX-Verbesserung |

---

## Drittanbieter- und beschaffte Systeme

Sichere Ingenieursprinzipien sollen auf von Drittanbietern entwickelte und beschaffte Systeme angewendet werden, die in die Umgebung der Organisation integriert sind.

**Vor der Beschaffung**:

- Sicherheitsarchitekturdokumentation soll vor der Beschaffungsgenehmigung überprüft werden.
- Eine Lieferantensicherheitsbewertung soll gemäss der Richtlinie zu Lieferanten und Cloud-Diensten (A.5.19-23) durchgeführt werden.
- Architekturkompatibilität mit den Sicherheitsstandards der Organisation soll verifiziert werden.

**Vertragliche Anforderungen**:

- Von Drittanbietern soll vertraglich verlangt werden, die sicheren Ingenieursprinzipien der Organisation einzuhalten.
- Eine Sicherheitsarchitekturprüfung soll am Design-Meilenstein erforderlich sein.
- Nachweise sicherer Entwicklungspraktiken sollen bereitgestellt werden.
- Sicherheitstestergebnisse sollen vor der Abnahme bereitgestellt werden.

**Nach der Beschaffung**:

- Integrationssicherheitsprüfung vor dem Deployment in die Umgebung der Organisation.
- Jährliche Architektur-Neubewertung für SaaS und verwaltete Dienste.
- Nicht-Konformität des Lieferanten soll eine Problemeskalation gemäss Vertragsbedingungen auslösen.

**Laufende Prüfungsauslöser für Drittanbietersysteme**:

- Grössere Versions-Upgrades (z. B. v2.x auf v3.x).
- Änderungen im Datenpflege-Umfang des Drittanbietersystems.
- Sicherheitsincidents, die das Drittanbietersystem betreffen.
- Jährliche Prüfung für Tier-1-Integrationen.
- Alle 2 Jahre für Tier-2-Integrationen.
- Wenn die SOC-2- oder ISO-27001-Zertifizierung des Anbieters ausläuft.

---

## Begriffsbestimmungen

| Begriff | Definition |
|---------|-----------|
| **Sichere Systemkonstruktion (SSE)** | Die Disziplin der Integration von Sicherheitsüberlegungen in alle Phasen des Systemlebenszyklus zur Erzeugung vertrauenswürdiger Systeme |
| **Security by Design** | Prinzip, dass Sicherheit von Beginn an in Systeme eingebaut wird, nicht nach der Entwicklung hinzugefügt |
| **Security by Default** | Prinzip, dass Systeme ohne Benutzeraktion sofort bei der ersten Nutzung sicher konfiguriert sind |
| **Tiefenverteidigung** | Geschichteter Sicherheitsansatz, bei dem mehrere Massnahmen Werte schützen, sodass die Kompromittierung einer Schicht nicht zu einer vollständigen Kompromittierung führt |
| **Zero Trust** | Sicherheitsmodell basierend auf «niemals vertrauen, immer verifizieren» — kein implizites Vertrauen auf der Grundlage des Netzwerkstandorts oder vorheriger Authentifizierung |
| **Bedrohungsmodell** | Strukturierte Analyse potenzieller Bedrohungen, Angriffsvektoren und Gegenmassnahmen für ein System |
| **Sicherheitsarchitektur** | Designartefakte, die beschreiben, wie Sicherheitsmassnahmen positioniert sind und wie sie sich zur Gesamtsystemarchitektur verhalten |
| **Angriffsfläche** | Die Summe aller Punkte, an denen ein Angreifer potenziell in ein System eindringen oder Daten extrahieren könnte |
| **STRIDE** | Methodik zur Bedrohungsmodellierung, die Bedrohungen als Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service und Elevation of Privilege kategorisiert |
| **Sicherheitsbaseline** | Der Mindestsatz von Sicherheitsmassnahmen, der für einen bestimmten System-Tier oder eine Klassifizierung erforderlich ist |

---

## Rollen und Verantwortlichkeiten

| Rolle | Verantwortlichkeiten im Bereich der sicheren Architektur |
|-------|----------------------------------------------------------|
| **Geschäftsleitung** | Genehmigte Richtlinie zur sicheren Konstruktion; Ressourcen für Architekturprüfungen bereitstellen; architektonische Restrisiken akzeptieren |
| **ISB** | Richtlinieneigentümerschaft; sichere Ingenieursprinzipien definieren und pflegen; Architekturprüfungen durchführen oder in Auftrag geben; Architekturausnahmen genehmigen; Aufsicht über die Bedrohungsmodellierung |
| **Entwicklungsleiter** | Sicherstellen, dass Entwicklungsteams sichere Ingenieursprinzipien anwenden; an Architekturprüfungen teilnehmen; Technologiestandards-Ausrichtung pflegen |
| **Systemeigentümer** | Systeme zur Architekturprüfung einreichen; Sicherheitsarchitekturdokumentation pflegen; systemspezifische Risiken verantworten |
| **Entwickler / Ingenieure** | Sichere Ingenieursprinzipien im Systemdesign und in der Implementierung anwenden; an Bedrohungsmodellierung teilnehmen; genehmigte Architekturmuster verwenden |
| **IT Operations** | Sicherheitsbaselines implementieren und pflegen; Konfigurationsstandards durchsetzen; Architekturprüfung mit Infrastrukturinformationen unterstützen |
| **Drittanbieter** | Vertragliche Anforderungen für sichere Konstruktion einhalten; Architekturdokumentation und Sicherheitstestnachweise bereitstellen |

### Eskalationspfad

- Sicherheitsbedenken in der Architektur: Entwickler/Ingenieur informiert ISB. ISB eskaliert an Geschäftsleitung, wenn Ressourcen- oder Organisationsänderungen erforderlich sind.
- Musterabweichungen: Antragsteller reicht Abweichungsantrag beim ISB ein. ISB genehmigt oder lehnt mit dokumentierter Begründung ab.
- Architektur-Risikoakzeptanz: Systemeigentümer reicht Risikobeurteilung beim ISB ein. Risiken, die die ISB-Akzeptanzschwelle überschreiten, werden an die Geschäftsleitung eskaliert.

---

## Nachweise

Die folgenden Nachweise belegen die Konformität mit dieser Richtlinie:

| # | Nachweis | Verantwortlicher | Häufigkeit |
|---|----------|-----------------|------------|
| 1 | **Dokumentierte sichere Ingenieursprinzipien** (diese Richtlinie und alle unterstützenden Standardsdokumente) | ISB | *Jährlich überprüft; bei Änderungen der Bedrohungslandschaft oder regulatorischen Anforderungen aktualisiert* |
| 2 | **Sicherheitsarchitekturdokumentation** (SAD, Bedrohungsmodelle, Rückverfolgbarkeit der Sicherheitsanforderungen) für Hoch- und Mittleres-Risiko-Systeme | ISB / Systemeigentümer | *Pro System; bei wesentlichen Änderungen aktualisiert; jährlich für Hochrisiko überprüft* |
| 3 | **Architekturprüfungsunterlagen** (Prüfungsanfragen, Befunde, Genehmigung oder Ablehnung mit Begründung) | ISB | *Pro Prüfung; 3 Jahre aufbewahrt* |
| 4 | **Bedrohungsmodellberichte** (STRIDE-Analyse, Risikobewertungen, Massnahmen, Restrisiken) | ISB | *Pro System; für Lebenszyklus des Systems + 3 Jahre aufbewahrt; dauerhaft für in wesentlichen Incidents involvierte Systeme (mindestens 7 Jahre)* |
| 5 | **Genehmigter Architekturmusterkatalog** (dokumentierte Muster mit Sicherheitsbegründung) | ISB / Entwicklungsleiter | *Kontinuierlich gepflegt; jährlich überprüft* |
| 6 | **Sicherheitsbaseline-Konfigurationen** (je System-Tier, mit dokumentierten Mindestmassnahmen) | ISB / IT Operations | *Jährlich überprüft; bei Technologie- oder Bedrohungsänderungen aktualisiert* |
| 7 | **Technologieauswahl-Sicherheitsbewertungen** (Sicherheitsbewertungsunterlagen für neue Technologiebeschaffungen) | ISB | *Pro Beschaffung; 3 Jahre aufbewahrt* |
| 8 | **Architekturausnahmenregister** (Abweichungen von Mustern oder Prinzipien mit ISB-Genehmigung, kompensierenden Massnahmen und Ablaufdaten) | ISB | *Vierteljährlich überprüft; 3 Jahre nach Abschluss aufbewahrt* |
| 9 | **Drittanbieter-Architekturbeurteilungen** (Lieferanten-Sicherheitsarchitekturprüfungen, Integrationssicherheitsprüfungen) | ISB | *Pro Engagement; für Vertragsdauer + 2 Jahre aufbewahrt* |
| 10 | **Zero-Trust-Implementierungsfortschritt** (Reifegradbeurteilung, Roadmap, Phasenabschlussnachweise) | ISB | *Jährlich bewertet; der Geschäftsleitung gemeldet* |
| 11 | **Tiefenverteidigungsvalidierungsunterlagen** (Massnahmenschichten-Analyse, die geschichtete Massnahmen über die Architektur bestätigt) | ISB / IT Operations | *Halbjährlich für Tier-1-Systeme; jährlich für Tier 2* |
| 12 | **Schulungsunterlagen** (Abschluss der Schulung zu sicherer Architektur und Konstruktion für relevantes Personal) | ISB / HR | *Pro Person verfolgt; jährlich überprüft; Ziel: 100 % Abschluss* |

---

# Richtlinienkonformität

## Konformitätsmessung

Das Informationssicherheits-Management-Team überprüft die Einhaltung dieser Richtlinie durch verschiedene Methoden, einschliesslich, aber nicht beschränkt auf Verfolgung des Abschlusses von Architekturprüfungen, Analyse der Musterübernahme, Audits zur Sicherheitsbaseline-Konformität, Bewertungen der Bedrohungsmodellabdeckung, interne und externe Audits sowie Feedback an den Richtlinieneigentümer.

Folgende Kennzahlen sollen dem ISB vierteljährlich gemeldet werden:

| Kennzahl | Zielwert | Rot-Schwellenwert |
|----------|----------|------------------|
| Neue Hochrisikosysteme mit abgeschlossener Architekturprüfung | 100 % | <100 % |
| Neue Systeme mit mittlerem Risiko mit abgeschlossener Architekturprüfung | 100 % | <80 % |
| Abschluss der Architekturprüfung innerhalb des SLA (risikobasiert: 5/10/15 Werktage) | 90 % | <70 % |
| Übernahmerate genehmigter Architekturmuster für neue Systeme | 80 % | <60 % |
| Aktive Architekturausnahmen | Minimiert; abnehmend | >5 gleichzeitig oder eine >12 Monate |
| Sicherheitsbaseline-Konformität (Tier-1-Systeme) | 100 % | <90 % |
| Aktuelle Bedrohungsmodelle für Hochrisikosysteme | 100 % | <80 % |

**Berichtspflichten**:
- **Vierteljährlicher ISB-Bericht**: Status der Architekturprüfungen, Musterübernahme, Status des Ausnahmenregisters, Baseline-Konformität.
- **Jährlicher Geschäftsleitungsbericht**: Zero-Trust-Reifefortschritt, Wirksamkeit des Architekturprogramms, wesentliche Risiken und Ressourcenbedarf.
- **Jährliches Management-Review**: Vollständige Bewertung des sicheren Konstruktionsprogramms einschliesslich Kennzahlentrends, wesentlicher Befunde und Verbesserungsempfehlungen.

Kennzahlen, die rote Schwellenwerte überschreiten, sollen dem ISB zur sofortigen Aufmerksamkeit eskaliert und beim nächsten Management-Review gemeldet werden.

## Ausnahmen

Jede Ausnahme von dieser Richtlinie soll vorab durch den ISB genehmigt und mit dokumentierter Risikoakzeptanz, kompensierenden Massnahmen und einem definierten Prüfdatum erfasst werden. Architekturausnahmen sollen zeitlich begrenzt sein (maximal 12 Monate) und vierteljährlich überprüft werden. Ausnahmen sollen dem Management-Review-Team gemeldet werden. Dauerhafte Ausnahmen von grundlegenden sicheren Ingenieursprinzipien und Ausnahmen, die die Tiefenverteidigung beseitigen, sind nicht zulässig.

## Nichteinhaltung

Ein Mitarbeitender, der gegen diese Richtlinie verstösst, kann disziplinarischen Massnahmen unterliegen, bis hin zur Kündigung des Arbeitsverhältnisses. Systeme, die ohne erforderliche Architekturprüfung deployed wurden, können bis zur Prüfung und Behebung aus der Produktion genommen werden.

## SOC-2-Ausrichtung

Diese Richtlinie unterstützt die Konformität mit den SOC-2-Trust-Services-Kriterien:

| SOC-2-Kriterium | Abdeckung |
|-----------------|----------|
| **CC3.1** (Spezifikation von Zielen) | Sicherheitsziele im Systemdesign |
| **CC5.2** (Allgemeine Massnahmen über Technologie) | Architekturmassnahmen; Architekturänderungen erfordern Change-Control-Genehmigung gemäss der Konfigurationsmanagementrichtlinie (A.8.9) |
| **CC6.1** (Logische Zugangssicherheit) | Authentifizierungsarchitektur, minimale Rechtevergabe, Zero Trust |
| **CC6.6** (Schutz vor externen Bedrohungen) | Tiefenverteidigung, Perimetermassnahmen |
| **CC7.1** (Schwachstellenerkennung) | Schwachstellenscanning in Baselineanforderungen |
| **CC7.2** (Anomalieerkennung) | Überwachungsschicht in der Tiefenverteidigung; Querverweise zur Richtlinie zu Überwachungsaktivitäten (A.8.16) |
| **CC9.2** (Lieferantenrisikomanagement) | Drittanbieter-Architekturprüfung; Querverweise zur Richtlinie zu Lieferanten und Cloud-Diensten (A.5.19-23) |

**SOC-2-Nachweisanforderungen**:

- Architekturprüfungsunterlagen (Nachweis Nr. 3).
- Bedrohungsmodelle (Nachweis Nr. 4).
- Genehmigter Musterkatalog (Nachweis Nr. 5).
- Sicherheitsbaselines (Nachweis Nr. 6).
- Rückverfolgbarkeitsmatrix für Sicherheitsanforderungen für Hochrisikosysteme.
- Nachweis der ISB-Genehmigung für Architekturausnahmen (Nachweis Nr. 8).

## Kontinuierliche Verbesserung

Diese Richtlinie wird im Rahmen des kontinuierlichen Verbesserungsprozesses überprüft und aktualisiert. Überprüfungen sollen Änderungen der sicheren Konstruktionsstandards (NIST SP 800-160, NIST SP 800-207), die Entwicklung der Bedrohungslandschaft und Angriffstechniken, neue Architekturmuster und Technologiestandards, regulatorische Änderungen (nDSG, DSGVO), Erkenntnisse aus Sicherheitsincidents und Architekturprüfungen sowie Auditbefunde berücksichtigen. Nichtkonformitäten im Zusammenhang mit dieser Richtlinie sollen erfasst und durch den ISMS-Korrekturmassnah­menprozess (Abschnitt 10.2) mit Ursachenanalyse und verfolgter Behebung verwaltet werden.

---

# Abgedeckte Bereiche der ISO-27001-Norm

Richtlinie zur sicheren Systemarchitektur und zu Ingenieursprinzipien — Zuordnung zu ISO-27001-Massnahmen

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Abschnitt 5.1 Führung und Verpflichtung | 5.1 Leitlinien für Informationssicherheit |
| Abschnitt 5.2 Richtlinie | 5.4 Managementverantwortung |
| Abschnitt 6.1 Massnahmen zur Behandlung von Risiken und Chancen | 5.8 Informationssicherheit im Projektmanagement |
| Abschnitt 6.2 Informationssicherheitsziele | 5.36 Einhaltung von Richtlinien, Regeln und Normen |
| Abschnitt 7.3 Bewusstsein | 8.25 Sicherer Entwicklungslebenszyklus |
| Abschnitt 8.1 Betriebliche Planung und Steuerung | 8.26 Sicherheitsanforderungen an Anwendungen |
| Abschnitt 9.1 Überwachung, Messung, Analyse und Bewertung | **8.27 Sichere Systemarchitektur und Ingenieursprinzipien** |
| Abschnitt 10.2 Nichtkonformität und Korrekturmassnahmen | 8.28 Sicheres Coding |
| | 8.29 Sicherheitstests in Entwicklung und Abnahme |
| | 8.31 Trennung von Entwicklungs-, Test- und Produktionsumgebungen |
| | 8.9 Konfigurationsmanagement |

**Regulatorischer und rechtlicher Rahmen**:

| Rahmenwerk | Relevanz |
|------------|---------|
| Schweizerisches nDSG (revDSG) | Art. 7 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 8 — Technische und organisatorische Massnahmen entsprechend dem Risiko |
| Schweizerische DSV (Datenschutzverordnung) | Art. 1–3 — Mindestanforderungen an die Datensicherheit |
| EU DSGVO (sofern anwendbar) | Art. 25 — Datenschutz durch Technik und datenschutzfreundliche Voreinstellungen; Art. 32 — Sicherheit der Verarbeitung |
| ISO/IEC 27001:2022 | Annex-A-Massnahme 8.27 — Sichere Systemarchitektur und Ingenieursprinzipien |
| ISO/IEC 27002:2022 | Abschnitt 8.27 — Implementierungsleitfaden für sichere Systemarchitektur |
| NIST SP 800-160 Vol. 1 Rev. 1 | Engineering Trustworthy Secure Systems — grundlegende Systemic-Security-Engineering-Prinzipien |
| NIST SP 800-207 | Zero Trust Architecture — Referenzarchitektur für die Zero-Trust-Implementierung |
| NIST SP 800-53 Rev 5 | SA-8 (Security and Privacy Engineering Principles) — 28 Sicherheitskonstruktionsprinzipien einschliesslich klarer Abstraktionen, Modularität, reduzierter Komplexität |
| CIS Controls v8 | Massnahme 4 (Sichere Konfiguration), Massnahme 16 (Sicherheit von Anwendungssoftware) — Safeguards zur Unterstützung sicherer Architektur |

---

<!-- QA_VERIFIED: 2026-03-29 -->
