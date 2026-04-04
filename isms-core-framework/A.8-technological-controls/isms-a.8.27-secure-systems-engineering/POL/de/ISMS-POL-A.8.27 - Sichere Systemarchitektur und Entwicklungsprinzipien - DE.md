<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.27-DE:framework:POL:a.8.27 -->
**ISMS-POL-A.8.27 — Richtlinie zur sicheren Systemarchitektur und zu Entwicklungsprinzipien**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Sichere Systemarchitektur und Entwicklungsprinzipien |
| **Dokumententyp** | Richtlinie |
| **Dokument-ID** | ISMS-POL-A.8.27 |
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

**Überprüfungsturnus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Technischer Leiter (TL)
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen)
- ISMS-POL-A.8.25-26-29 (Sicheres Entwicklungsrahmenwerk)
- ISMS-POL-A.8.28 (Sichere Codierung)
- ISMS-POL-A.8.9 (Konfigurationsmanagement)
- ISMS-POL-A.5.8 (Informationssicherheit im Projektmanagement)
- ISMS-IMP-A.8.27.1-UG/TG (Sicherheitsarchitektur-Review-Prozess)
- ISMS-IMP-A.8.27.2-UG/TG (Threat-Modelling-Methodik)
- ISMS-IMP-A.8.27.3-UG/TG (Katalog sicherer Architekturmuster)
- ISMS-IMP-A.8.27.4-UG/TG (Zero-Trust-Implementierungs-Assessment)
- ISO/IEC 27001:2022 Control A.8.27
- INCOSE Systems Engineering Handbook, 5. Auflage (2023)
- NIST SP 800-160 Vol. 1 Rev. 1 – Engineering Trustworthy Secure Systems
- NIST SP 800-160 Vol. 2 Rev. 1 – Developing Cyber-Resilient Systems
- NIST SP 800-207 – Zero Trust Architecture

---

## Zusammenfassung

Diese Richtlinie legt die grundlegenden Anforderungen von [Organisation] an Secure Systems Engineering (SSE) fest – die Disziplin der Integration von Sicherheit in jede Schicht der Systemarchitektur über den gesamten Systemlebenszyklus.

**Zweck**: Definition der Prinzipien, Ansätze und Anforderungen für die Entwicklung vertrauenswürdiger sicherer Systeme. Diese Richtlinie legt fest, WELCHE sicheren Entwicklungsprinzipien gelten und WER für deren Implementierung verantwortlich ist. Implementierungsverfahren (WIE) sind in ISMS-IMP-A.8.27 dokumentiert.

**Anwendungsbereich**: Diese Richtlinie gilt für ALLE Systeme, die von [Organisation] entworfen, entwickelt, erworben, integriert, betrieben und gewartet werden, einschliesslich Informationssystemen, Betriebstechnologie (OT), Cloud-Diensten und von Dritten entwickelten Systemen.

**Grundprinzip**: Sicherheit MUSS beim Systemdesign genauso grundlegend sein wie Systemleistung und Betriebssicherheit. Sicherheit ist kein Zusatz, sondern eine inhärente Eigenschaft gut entwickelter Systeme.

**Schlüsselkonzept**: Diese Richtlinie implementiert „Security by Design and Default" – das Prinzip, dass Sicherheit von Anfang an in Systeme eingebaut werden muss, nicht nachträglich nach dem Deployment.

---

# Anwendungsbereich und Steuerungsausrichtung

## ISO/IEC 27001:2022 Control A.8.27

**ISO/IEC 27001:2022 Anhang A.8.27 – Sichere Systemarchitektur und Entwicklungsprinzipien**

> *Prinzipien für die Entwicklung sicherer Systeme sollten etabliert, dokumentiert, gepflegt und auf alle Informationssystem-Entwicklungsaktivitäten angewendet werden.*

**Kontrollziel**: Sicherstellung, dass Sicherheit in alle Architekturschichten über den gesamten Systemlebenszyklus hinweg eingebaut wird, unter Förderung von „Security by Design", Zero Trust und Defense-in-Depth-Strategien.

**Kontrolltyp**: Präventiv
**Kontrollkategorie**: Technologisch

## Richtlinien-Anwendungsbereich

**Diese Richtlinie gilt für**:

| Kategorie | Umfang |
|-----------|--------|
| **Systeme** | Alle Informationssysteme, Anwendungen, Infrastruktur, Cloud-Dienste, OT/ICS-Systeme |
| **Lebenszyklusphasen** | Konzept, Entwicklung, Produktion, Nutzung, Support, Ausserdienststellung |
| **Architekturschichten** | Geschäft, Daten, Anwendung, Technologie, Sicherheit |
| **Personal** | Systemarchitekten, Ingenieure, Entwickler, Sicherheitsfachleute, Drittentwickler |
| **Prozesse** | Systemdesign, Entwicklung, Integration, Deployment, Betrieb, Ausserbetriebnahme |

**Beziehung zu anderen Kontrollen**:

| Kontrolle | Beziehung |
|-----------|-----------|
| **A.8.25** | Sicherer Entwicklungslebenszyklus – Prozessrahmenwerk, das SSE-Prinzipien implementiert |
| **A.8.26** | Anwendungssicherheitsanforderungen – aus SSE-Prinzipien abgeleitete Anforderungen |
| **A.8.28** | Sichere Codierung – Codierungsstandards, die SSE-Prinzipien implementieren |
| **A.8.29** | Sicherheitstests – Validierung der SSE-Implementierung |
| **A.5.8** | Projektmanagement – SSE-Integration in Projekt-Governance |

## Regulatorische Anwendbarkeit

**Tier 1 – Verbindliche Compliance** (Alle Operationen):

| Regulation | Wesentliche SSE-Anforderungen |
|------------|-------------------------------|
| **Swiss nDSG** | Artikel 8 – Dem Risiko angemessene technische Massnahmen |
| **EU DSGVO** | Artikel 25 – Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen |
| **ISO/IEC 27001:2022** | Control A.8.27 |

**Tier 2 – Bedingte Anwendbarkeit** (Durch Geschäftsaktivitäten ausgelöst):

| Regulation | Auslöser | Anforderung |
|-----------|----------|-------------|
| **DORA** | EU-Finanzdienstleistungen | IKT-Risikomanagement-Rahmenwerk, sichere Architektur |
| **NIS2** | Wesentliche/wichtige Einrichtung | Security-by-Design-Anforderungen |
| **PCI DSS v4.0.1** | Zahlungskartenverarbeitung | Anforderungen an sichere Systementwicklung |
| **FINMA** | Schweizer Finanzinstitut | IT-Architektursicherheitsanforderungen |

Compliance-Bestimmung gemäss ISMS-POL-00 (Regulatorischer Anwendbarkeitsrahmen).

---

# Richtlinienanforderungen

## Grundlegende Sicherheits-Entwicklungsprinzipien

### Kernprinzipien

[Organisation] MUSS die folgenden grundlegenden Prinzipien des Secure Systems Engineering auf ALLE Systementwicklungs- und -beschaffungsaktivitäten anwenden:

**Prinzip 1: Security by Design**

Sicherheit MUSS von den frühesten Phasen der Systemkonzeption integriert werden:

- Sicherheitsanforderungen MÜSSEN während der ersten Konzeptentwicklung identifiziert werden
- Sicherheitsarchitektur MUSS vor Beginn des Detaildesigns definiert werden
- Sicherheitskontrollen MÜSSEN als integraler Systembestandteil konzipiert werden, nicht als nachträgliche Ergänzung
- Sicherheits-Trade-offs MÜSSEN explizit dokumentiert und genehmigt werden

**Prinzip 2: Security by Default**

Systeme MÜSSEN in ihrer Standardkonfiguration sicher sein:

- Standardkonfigurationen MÜSSEN die restriktivsten für den Systemzweck geeigneten Sicherheitseinstellungen implementieren
- Nutzer MÜSSEN keine Massnahmen ergreifen, um das System zu sichern
- Optionale Sicherheitsfunktionen MÜSSEN standardmässig aktiviert sein, sofern keine geschäftliche Rechtfertigung für Deaktivierung besteht
- „Default Deny" MUSS auf Zugriffskontrollen, Netzwerkkommunikation und Systemfunktionen angewendet werden

**Prinzip 3: Defence in Depth**

Mehrere Schichten von Sicherheitskontrollen MÜSSEN implementiert werden:

- Keine einzelne Kontrolle darf der einzige Schutz für kritische Assets sein
- Kontrollen MÜSSEN auf mehreren Architekturschichten implementiert werden (Netzwerk, Plattform, Anwendung, Daten)
- Der Ausfall einer Kontrolle auf einer Schicht darf nicht zur vollständigen Kompromittierung führen
- Mehrschichtige Kontrollen MÜSSEN sich ergänzen, nicht redundant sein

**Prinzip 4: Least Privilege (Minimale Rechte)**

Alle Nutzer, Prozesse und Systeme MÜSSEN mit minimal notwendigen Berechtigungen arbeiten:

- Zugriffsrechte MÜSSEN auf das für autorisierte Funktionen Erforderliche beschränkt sein
- Erhöhte Berechtigungen MÜSSEN nur bei Bedarf gewährt und entzogen werden, wenn nicht mehr benötigt
- Dienstkonten MÜSSEN eng begrenzte Berechtigungen haben
- Administrativer Zugang MUSS vom operativen Zugang getrennt sein

**Prinzip 5: Least Functionality (Minimale Funktionalität)**

Systeme MÜSSEN nur die für ihren vorgesehenen Zweck erforderlichen Fähigkeiten bereitstellen:

- Unnötige Dienste, Protokolle und Funktionen MÜSSEN deaktiviert oder entfernt werden
- Systemfunktionalität MUSS auf dokumentierte Geschäftsanforderungen beschränkt sein
- Angriffsfläche MUSS durch Funktionsreduzierung minimiert werden
- Ungenutzte Ports, Schnittstellen und Fähigkeiten MÜSSEN deaktiviert werden

**Prinzip 6: Fail Secure (Sicheres Versagen)**

Systeme MÜSSEN in einem sicheren Zustand ausfallen:

- Systemausfälle DÜRFEN keine sensiblen Daten oder Funktionen exponieren
- Authentifizierungsfehler MÜSSEN standardmässig den Zugang verweigern
- Fehlerbedingungen DÜRFEN keine sicherheitsrelevanten Informationen preisgeben
- Wiederherstellung nach einem Ausfall MUSS erneute Authentifizierung und -autorisierung erfordern

### Zero-Trust-Architekturprinzipien

[Organisation] MUSS Zero-Trust-Prinzipien für alle Systeme implementieren:

**Never Trust, Always Verify (Kein implizites Vertrauen, immer verifizieren)**:

- Kein implizites Vertrauen basierend auf Netzwerkstandort, Geräteeigentümerschaft oder früherer Authentifizierung
- Jede Zugriffsanfrage MUSS unabhängig von der Quelle authentifiziert und autorisiert werden
- Vertrauen MUSS kontinuierlich bewertet werden, nicht einmalig gewährt und danach vorausgesetzt

**Assume Breach (Von Kompromittierung ausgehen)**:

- Systeme unter der Annahme designen, dass Angreifer möglicherweise bereits Netzwerkzugang haben
- Interner Netzwerktraffic MUSS als potenziell feindlich behandelt werden
- Lateral Movement MUSS durch Segmentierung und Zugriffskontrollen eingeschränkt werden
- Erkennungsfähigkeiten MÜSSEN davon ausgehen, dass Perimeter-Kontrollen versagt haben könnten

**Verify Explicitly (Explizit verifizieren)**:

- Zugriffsenscheidungen MÜSSEN auf allen verfügbaren Datenpunkten basieren:
  - Benutzeridentität und Authentifizierungsstärke
  - Gerätezustand und Compliance-Status
  - Datensensitivität und -klassifizierung
  - Zugriffskontext (Standort, Zeit, Verhaltensmuster)
  - Erkennung von Anfrage-Anomalien

**Least Privilege Access (Minimaler Zugang)**:

- Just-in-Time (JIT)-Zugang für erhöhte Berechtigungen
- Just-Enough-Access (JEA) für alle Zugangsgewährungen
- Risikobasierte bedingte Zugriffsrichtlinien
- Kontinuierliche Zugangsbewertung und -widerruf

**Encryption by Default (Verschlüsselung standardmässig)**:

- Alle Daten in Transit MÜSSEN verschlüsselt werden (TLS 1.2+ Minimum)
- Alle Daten im Ruhezustand MÜSSEN für VERTRAULICH+-Klassifizierung verschlüsselt werden
- Interne Dienst-zu-Dienst-Kommunikation MUSS verschlüsselte Kanäle verwenden
- Verschlüsselungsschlüssel MÜSSEN gemäss ISMS-POL-A.8.24 verwaltet werden

### Defence-in-Depth-Implementierung

[Organisation] MUSS mehrschichtige Sicherheitskontrollen über alle Architekturschichten implementieren:

| Schicht | Sicherheitskontrollen | ISO-27001-Kontroll-Zuordnung |
|---------|-----------------------|------------------------------|
| **Perimeter** | Firewalls, WAF, DDoS-Schutz, sichere Gateways | A.8.20, A.8.21, A.8.22 |
| **Netzwerk** | Segmentierung, Mikro-Segmentierung, Netzwerkzugangskontrolle, IDS/IPS | A.8.20, A.8.22 |
| **Plattform** | Gehärtete Konfigurationen, Patch-Management, Endpoint-Schutz | A.8.1, A.8.8, A.8.9 |
| **Anwendung** | Eingabevalidierung, Ausgabe-Encoding, Authentifizierung, Autorisierung | A.8.25, A.8.26, A.8.28 |
| **Daten** | Verschlüsselung, Maskierung, Zugriffskontrollen, DLP | A.8.10, A.8.11, A.8.12, A.8.24 |
| **Identität** | MFA, Privilegierter Zugangsmanagement, Identitäts-Governance | A.5.15, A.5.16, A.5.18, A.8.2, A.8.5 |
| **Überwachung** | SIEM, Verhaltensanalyse, Bedrohungserkennung, Vorfallsreaktion | A.8.15, A.8.16, A.5.24, A.5.25 |

## Systemarchitekturanforderungen

### Sicherheitsarchitektur-Review

Alle neuen Systeme und wesentliche Änderungen an bestehenden Systemen MÜSSEN einer Sicherheitsarchitektur-Review unterzogen werden:

**Review-Auslöser**:

- Neue Systementwicklung oder -beschaffung
- Wichtige Versions-Upgrades oder -Migrationen
- Architekturänderungen, die Sicherheitsgrenzen betreffen
- Integration neuer externer Dienste oder Datenflüsse
- Änderungen an Authentifizierungs- oder Autorisierungsmechanismen

**Review-Prozess**:

1. Threat Modelling mit strukturierter Methodik:
   - **STRIDE** als primäre Methodik für alle Systeme (verbindlich)
   - **PASTA** für komplexe Systeme, die Angriffssimulation erfordern (optionale Erweiterung)
   - Methodikwahl begründet in ISMS-IMP-A.8.27.2 dokumentiert
2. Validierung der Sicherheitsanforderungen gegen Geschäftsanforderungen
3. Architekturmuster-Review gegen genehmigte Muster
4. Kontroll-Design-Review für Defence in Depth
5. Risikobeurteilung und Restrisikodokumentation
6. ISB- oder Security-Architect-Genehmigung vor Implementierung

**Genehmigungskriterien für Architektur-Review**:

Systeme MÜSSEN folgende Kriterien erfüllen, bevor die Architektur genehmigt wird:

- ✅ Threat Model mit genehmigter Methodik abgeschlossen
- ✅ Alle HOCH- und KRITISCH-Risiken haben genehmigte Behandlungspläne
- ✅ Architektur implementiert genehmigte Muster ODER Abweichungen haben ISB-Ausnahmegenehmigung
- ✅ Defence in Depth über alle Architekturschichten validiert
- ✅ Zero-Trust-Prinzipien für Authentifizierung, Autorisierung und Datenflüsse adressiert
- ✅ Sicherheitsanforderungen auf Geschäftsanforderungen zurückführbar
- ✅ Drittanbieter-Integrationen erfüllen ISMS-POL-A.5.19-23

**Architektur-Review darf NICHT genehmigt werden, wenn**:
- Kritische Risiken ohne Behandlungsplan vorliegen
- Nicht genehmigte Musterabweichungen ohne kompensierende Kontrollen bestehen
- Fehlende Defence-in-Depth-Schichten für VERTRAULICH+-Daten

**Review-Dokumentation**:

- Sicherheitsarchitekturdokument (SAD)
- Threat-Model-Bericht
- Sicherheitsanforderungs-Traceability-Matrix
- Risikobeurteilung und -behandlungsplan
- Architektur-Genehmigungsprotokoll

### Sichere Architekturmuster

[Organisation] MUSS einen Katalog genehmigter sicherer Architekturmuster pflegen:

**Musterkategorien**:

| Kategorie | Beispiele |
|-----------|-----------|
| **Authentifizierung** | SSO-Integration, MFA-Implementierung, Federated Identity |
| **Autorisierung** | RBAC-Implementierung, attributbasierter Zugang, API-Autorisierung |
| **Datenschutz** | Verschlüsselung im Ruhezustand, Verschlüsselung in Transit, Tokenisierung |
| **Netzwerksicherheit** | DMZ-Architektur, Mikro-Segmentierung, API-Gateway |
| **Integration** | Sichere API-Muster, Message-Queue-Sicherheit, Service Mesh |
| **Cloud** | Landing-Zone-Architektur, Workload-Isolation, Cloud-native Sicherheit |

**Mindestinhalt des Musterkatalogs**:

Der Musterkatalog MUSS mindestens umfassen:

- **Authentifizierungsmuster**: SSO-Integration (SAML/OIDC), MFA-Implementierung, API-Schlüsselverwaltung
- **Autorisierungsmuster**: RBAC mit Least Privilege, attributbasierter Zugang für sensitive Daten
- **Datenschutzmuster**: Verschlüsselung im Ruhezustand (AES-256), Verschlüsselung in Transit (TLS 1.3), Tokenisierung für PII
- **Netzwerksicherheitsmuster**: DMZ-Architektur, Mikro-Segmentierung, API-Gateway mit WAF
- **Cloud-Muster**: Landing-Zone-Architektur (pro Cloud-Anbieter), Workload-Isolation, CSPM-Integration

**Musterdokumentationsanforderungen**:
Jedes Muster MUSS dokumentieren:
- Sicherheitsbegründung und Bedrohungsminderung
- Implementierungsschritte und Konfigurationsbeispiele
- Test- und Validierungsverfahren
- Häufige Fallstricke und zu vermeidende Anti-Muster

**Musterkatalog-Speicherort**: [SharePoint/Confluence] – Security Architecture Space

**Muster-Governance**:

- Muster MÜSSEN mit Sicherheitsbegründung dokumentiert sein
- Muster MÜSSEN jährlich auf fortgesetzte Eignung überprüft werden
- Abweichungen von genehmigten Mustern erfordern Security-Architect-Genehmigung
- Neue Muster MÜSSEN durch Threat Modelling vor Genehmigung validiert werden

### Drittsysteme und beschaffte Systeme

Sicherheitsarchitekturprinzipien MÜSSEN auf von Dritten entwickelte und beschaffte Systeme angewendet werden:

**Beschaffungsanforderungen**:

- Sicherheitsarchitekturdokumentation erforderlich vor Beschaffungsgenehmigung
- Lieferantensicherheitsbeurteilung gemäss ISMS-POL-A.5.19-23
- Architekturkompatibilität mit den Sicherheitsstandards von [Organisation]
- Integrationssicherheits-Review vor Deployment

**Anforderungen an Drittentwicklung**:

- Vertragliche Pflicht zur Einhaltung der SSE-Prinzipien von [Organisation]
- Sicherheitsarchitektur-Review beim Design-Meilenstein
- Nachweis sicherer Entwicklungspraktiken
- Sicherheitstests vor Abnahme

**Drittanbieter-Compliance-Verifizierung**:

- **Vor der Beschaffung**: Lieferantensicherheitsbeurteilung gemäss ISMS-POL-A.5.19-23 (Architekturdokumentation überprüft)
- **Vertragliche Anforderungen**: SSE-Prinzipien MÜSSEN in Entwicklungsverträge aufgenommen werden (Referenz ISMS-IMP-A.5.20)
- **Design-Meilenstein-Review**: Security Architect MUSS Architekturdokumentation in der Designphase überprüfen
- **Vorbereitende Abnahmetests**: Sicherheitstestergebnisse erforderlich vor Systemabnahme (Referenz ISMS-POL-A.8.29)
- **Laufende Überwachung**: Jährliche Architektur-Neubewertung für SaaS/Managed Services

**Nicht-Compliance-Behebung**: Nicht-Compliance des Lieferanten mit SSE-Anforderungen löst Problem-Eskalation gemäss Vertragsbedingungen und ISMS-POL-A.5.22 aus.

## Entwicklungsprozess-Integration

### Systemlebenszyklus-Integration

SSE-Prinzipien MÜSSEN in jede Phase des Systemlebenszyklus integriert werden:

| Phase | SSE-Aktivitäten | Verantwortliche Rolle | Gate/Meilenstein |
|-------|----------------|----------------------|-----------------|
| **Konzept** | Sicherheitsziele, Bedrohungskontext, Risikobereitschaft, Compliance-Anforderungen | Systemeigentümer + Security Architect | Konzeptgenehmigung |
| **Entwicklung** | Sicherheitsarchitektur, Threat Modelling, sicheres Design, Sicherheitstests | Security Architect + Entwicklungsteam | Design Freeze |
| **Produktion** | Sicherheitskonfiguration, Härtung, Penetrationstests, Sicherheitsgenehmigung | Security Team + Betrieb | Vorproduktionsgenehmigung |
| **Nutzung** | Sicherheitsüberwachung, Schwachstellenmanagement, Vorfallsreaktion | Systemeigentümer + Security Operations | Vierteljährliche Überprüfung |
| **Support** | Sicherheits-Patching, Konfigurationsmanagement, Zugriffsüberprüfungen | Systemeigentümer + Betrieb | Monatlich/vierteljährlich |
| **Ausserdienststellung** | Datensanitisierung, sichere Ausserbetriebnahme, Zugangs-Widerruf | Systemeigentümer + Security Team | Ausserbetriebnahme-Genehmigung |

### Designprinzipien für vertrauenswürdige sichere Systeme

[Organisation] übernimmt die folgenden Designprinzipien ausgerichtet auf NIST SP 800-160:

**Klare Abstraktionen**: Systemkomponenten MÜSSEN klar definierte Schnittstellen mit klaren Sicherheitsgrenzen und minimaler Komplexität aufweisen.

**Modularität und Schichtung**: Systeme MÜSSEN mit unabhängigen, lose gekoppelten Modulen entwickelt werden, die unabhängig gesichert, aktualisiert und validiert werden können.

**Teilweise geordnete Abhängigkeiten**: Systemkomponenten MÜSSEN klar definierte, azyklische Abhängigkeiten haben, um zirkuläre Vertrauensbeziehungen zu verhindern und systematische Sicherheitsanalyse zu ermöglichen.

**Minimiertes Teilen**: Gemeinsam genutzte Ressourcen MÜSSEN minimiert werden, um die Angriffsfläche zu reduzieren und unerlaubte Informationsflüsse zwischen Komponenten zu verhindern.

**Reduzierte Komplexität**: Systemdesigns SOLLEN Einfachheit bevorzugen; komplexe Systeme sind schwieriger zu sichern, zu verifizieren und zu warten.

**Sichere Entwicklungsfähigkeit**: Systeme MÜSSEN so entwickelt werden, dass Sicherheitsaktualisierungen und -verbesserungen ohne vollständiges Redesign aufgenommen werden können.

**Eigenständige Vertrauenswürdigkeit**: Systeme DÜRFEN sich bei der Sicherheit nicht ausschliesslich auf externe Entitäten verlassen; Sicherheitsmechanismen MÜSSEN in das System eingebaut sein.

---

# Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|-------|---------------|
| **Geschäftsleitung** | SSE-Richtlinie genehmigen, Ressourcen zuweisen, Restrisiken der Architektur akzeptieren |
| **ISB** | Richtlinieneigentümerschaft, SSE-Standards, Architekturrisiko-Akzeptanz, Ausnahmegenehmigung |
| **Technischer Leiter (TL)** | Technische Architektur-Governance, Mustergenehmigung, Technologiestandards |
| **Security Architect** | SSE-Standards-Entwicklung, Architektur-Reviews, Musterkatalog, Threat Modelling |
| **Enterprise Architect** | Integration von Sicherheit in Unternehmensarchitektur, Musterausrichtung |
| **Systemeigentümer** | SSE-Compliance für eigene Systeme, Architekturdokumentation, Risikoeigentümerschaft |
| **Entwicklungsteams** | Implementierung von SSE-Prinzipien, sicheres Design, Threat-Model-Beteiligung |
| **Drittanbieter** | Compliance mit vertraglichen SSE-Anforderungen |

**Eskalationspfad**:

- Architektursicherheitsbedenken: Entwicklungsteam → Security Architect → ISB
- Musterabweichungen: Antragsteller → Security Architect → ISB
- Architekturrisiko-Akzeptanz: Systemeigentümer → Security Architect → ISB → Geschäftsleitung

**SSE-Schulungsanforderungen**:

| Rolle | Schulung | Turnus | Nachweis |
|-------|----------|--------|---------|
| Security Architects | Threat-Modelling-Zertifizierung (z.B. STRIDE Practitioner) | Initial + Auffrischung alle 3 Jahre | Zertifikat + jährliches Threat-Model-Arbeitsergebnis |
| Systemarchitekten | SSE-Prinzipien-Überblick, Musterkatalog-Schulung | Initial + jährliche Auffrischung | Schulungsabschlussprotokoll |
| Entwickler | Grundlagen sicheren Designs (ausgerichtet auf ISMS-POL-A.8.28) | Initial + jährliche Auffrischung | Schulungsabschluss + Assessments zu sicherer Codierung |

---

# Governance und Compliance

## Beurteilungsrahmen

[Organisation] MUSS die SSE-Implementierung verifizieren durch:

| Assessment | Turnus | Eigentümer | Nachweis |
|------------|--------|------------|---------|
| Sicherheitsarchitektur-Reviews | Pro Projektmeilenstein | Security Architect | Review-Berichte, Threat Models |
| Muster-Compliance-Prüfung | Jährlich | Security Team | Musternutzungsanalyse |
| Zero-Trust-Reifegradbeurteilung | Jährlich | ISB | Reifegrad-Scorecard |
| Defence-in-Depth-Validierung | Halbjährlich | Security Team | Kontrollschicht-Analyse |
| Drittanbieter-Architektur-Review | Pro Beschaffung/Engagement | Security Architect | Lieferantenbeurteilungen |

**Zero-Trust-Reifegrad-Beurteilungsmethodik**:

[Organisation] MUSS **CISA Zero Trust Maturity Model v2.0** (oder ein vom ISB genehmigtes gleichwertiges Rahmenwerk) zur Beurteilung der Zero-Trust-Implementierungsreife verwenden.

**Beurteilungsumfang**: Fünf Säulen werden jährlich bewertet:
1. Identität
2. Geräte
3. Netzwerke
4. Anwendungen und Workloads
5. Daten

**Reifegrade** (gemäss CISA-Modell):
- **Traditional** (Stufe 0): Perimeterbasierte Sicherheit
- **Initial** (Stufe 1): Zero-Trust-Prinzipien anerkannt
- **Advanced** (Stufe 2): Zero Trust teilweise implementiert
- **Optimal** (Stufe 3): Zero Trust vollständig implementiert und optimiert

**Ziel-Reifegrad**: [Organisation] strebt **Advanced (Stufe 2)** Reife über alle Säulen innerhalb von 24 Monaten nach Richtliniengenehmigung an.

**Beurteilungsausgabe**: Jährliche Scorecard mit säulenspezifischen Reifegraden und Verbesserungs-Roadmap.

**Governance-Kennzahlen (Vierteljährliches Dashboard)**:

| Kennzahl | Ziel | Messung |
|----------|------|---------|
| % neuer Systeme mit abgeschlossener Architektur-Review | 100 % | Anzahl Systeme mit genehmigter Review / Gesamte neue Systeme |
| Durchschnittliche Zeit von Design bis Architektur-Genehmigung | ≤ 15 Arbeitstage | Mittlere Zeit von Review-Anfrage bis ISB-Genehmigung |
| Anzahl aktiver Architekturausnahmen | ≤ 5 zu jeder Zeit | Anzahl offener Ausnahmen im Register |
| Zero-Trust-Implementierungs-Reifegrad | ≥ Stufe 2 (Advanced) über alle Säulen | Jährliche CISA-ZT-Maturity-Model-Beurteilung |
| Muster-Adoptionsrate für neue Systeme | ≥ 80 % | Systeme mit genehmigten Mustern / Gesamte überprüfte Systeme |
| Kritische/hohe Sicherheitsbefunde aus Architektur-Reviews | < 10 % der Reviews | Reviews mit kritischen/hohen Befunden / Gesamte Reviews |

## Ausnahmemanagement

Ausnahmen zur Architekturrichtlinie erfordern:

- Dokumentierte Geschäftsbegründung
- Risikobeurteilung der Abweichungsauswirkungen
- Spezifikation kompensierender Kontrollen
- Empfehlung des Security Architect
- ISB-Genehmigung
- Zeitlich begrenzte Genehmigung (maximal 12 Monate für Architekturausnahmen)
- Vierteljährliche Überprüfung auf fortgesetzte Notwendigkeit

**Nicht zulässig**:

- Permanente Ausnahmen zu Kern-SSE-Prinzipien
- Ausnahmen, die Defence in Depth eliminieren
- Systeme ohne jegliche Architektur-Sicherheits-Review

---

# ISMS-Integration

## Statement of Applicability

| Kontrolle | Status | Implementierungsreferenz |
|-----------|--------|--------------------------|
| **A.8.27 – Sichere Systemarchitektur und Entwicklungsprinzipien** | Anwendbar | Diese Richtlinie, ISMS-IMP-A.8.27-UG/TG |

## Verwandte Kontrollen

| Kontrolle | Beziehung |
|-----------|-----------|
| **A.8.25-26-29** | SSE-Prinzipien informieren Anforderungen des sicheren Entwicklungslebenszyklus |
| **A.8.28** | Sichere Codierung implementiert SSE-Prinzipien auf Code-Ebene |
| **A.8.9** | Konfigurationsmanagement setzt sichere Baseline-Konfigurationen durch |
| **A.5.8** | Projektmanagement integriert SSE in Projekt-Governance |
| **A.8.31** | Umgebungstrennung implementiert SSE-Architekturmuster |
| **A.8.2-3-5** | Authentifizierung/Zugang implementiert Zero-Trust-Prinzipien |

## Implementierungsressourcen

| Dokument | Zweck |
|----------|-------|
| **ISMS-IMP-A.8.27.1-UG/TG** | Sicherheitsarchitektur-Review-Prozess |
| **ISMS-IMP-A.8.27.2-UG/TG** | Threat-Modelling-Methodik |
| **ISMS-IMP-A.8.27.3-UG/TG** | Katalog sicherer Architekturmuster |
| **ISMS-IMP-A.8.27.4-UG/TG** | Zero-Trust-Implementierungs-Assessment |

## Externe Referenzen

| Referenz | Zweck |
|----------|-------|
| **INCOSE SE Handbook 5. Aufl. (2023)** | Systems-Engineering-Prozessrahmenwerk |
| **NIST SP 800-160 Vol. 1 Rev. 1** | Engineering Trustworthy Secure Systems |
| **NIST SP 800-160 Vol. 2 Rev. 1** | Developing Cyber-Resilient Systems |
| **NIST SP 800-207** | Zero Trust Architecture |
| **NIST SP 800-207A** | Zero Trust for Cloud-Native Applications |
| **OWASP SAMM** | Software Assurance Maturity Model |
| **MITRE ATT&CK** | Bedrohungsbasiertes Architekturdesign |

---

# Definitionen

| Begriff | Definition |
|---------|------------|
| **Secure Systems Engineering (SSE)** | Die Disziplin der Integration von Sicherheitsüberlegungen in alle Phasen des Systemlebenszyklus zur Entwicklung vertrauenswürdiger sicherer Systeme |
| **Security by Design** | Prinzip, dass Sicherheit von Anfang an in Systeme eingebaut wird, nicht nach der Entwicklung hinzugefügt |
| **Security by Default** | Prinzip, dass Systeme ohne Benutzeraktion sofort sicher konfiguriert sind |
| **Defence in Depth** | Mehrschichtiger Sicherheitsansatz, bei dem mehrere Kontrollen Assets schützen, sodass die Kompromittierung einer Schicht nicht zur vollständigen Kompromittierung führt |
| **Zero Trust** | Sicherheitsmodell basierend auf „kein implizites Vertrauen, immer verifizieren", bei dem kein implizites Vertrauen basierend auf Netzwerkstandort oder früherer Authentifizierung gewährt wird |
| **Threat Model** | Strukturierte Analyse potenzieller Bedrohungen, Angriffsvektoren und Gegenmassnahmen für ein System |
| **Sicherheitsarchitektur** | Die Design-Artefakte, die beschreiben, wie Sicherheitskontrollen positioniert sind und wie sie sich zur Gesamtsystemarchitektur verhalten |
| **Vertrauenswürdiges sicheres System** | Ein System, dem vertraut werden kann, dass es innerhalb des definierten Bedrohungskontexts und der Risikobereitschaft sicher betrieben wird |
| **Angriffsfläche** | Die Gesamtheit aller Punkte, an denen ein Angreifer potenziell in ein System eindringen oder Daten extrahieren könnte |

---

# Nachweise zu dieser Richtlinie

**Stufe 1 (Dokumentationsüberprüfung) Nachweise:**

Nachweise, die belegen, dass diese Richtlinie angemessen dokumentiert und genehmigt ist:

- ✅ Dieses Richtliniendokument (ISMS-POL-A.8.27 v1.0)
- ✅ Genehmigungsunterschriften von ISB, TL, Geschäftsleitung
- ✅ Grundlegende SSE-Prinzipien dokumentiert (Abschnitt 2.1)
- ✅ Zero-Trust-Prinzipien definiert (Abschnitt 2.1)
- ✅ Defence-in-Depth-Anforderungen festgelegt (Abschnitt 2.1)
- ✅ Architektur-Review-Anforderungen dokumentiert (Abschnitt 2.2)
- ✅ Sichere Architekturmuster referenziert (Abschnitt 2.2)
- ✅ Lebenszyklus-Integrationsanforderungen definiert (Abschnitt 2.3)
- ✅ Rollen und Verantwortlichkeiten zugewiesen (Abschnitt 3)
- ✅ Externe Rahmenwerksreferenzen dokumentiert (Abschnitt 5.3)

**Stufe 2 (Operative Wirksamkeit) Nachweise:**

Nachweise, die die operative Wirksamkeit dieser Richtlinie belegen:

| Nachweistyp | Repository-Speicherort | Generierungsmethode | Eigentümer | Aufbewahrung |
|-------------|----------------------|---------------------|------------|--------------|
| **Architektur-Review-Aufzeichnungen** | [GRC-Plattform] – Architektur-Review-Modul | Generiert von Security Architect mit Review-Vorlage ISMS-IMP-A.8.27.1-UG/TG | Security Architect | 3 Jahre |
| **Threat Models** | [GRC-Plattform] – Threat-Model-Repository | Erstellt während Architektur-Review mit STRIDE-Vorlage ISMS-IMP-A.8.27.2-UG/TG | Security Architect + Systemeigentümer | Lebensdauer des Systems + 1 Jahr |
| **Musterkatalog** | [Confluence/SharePoint] – Security Architecture Space | Gepflegt von Security Architect, vierteljährliche Updates | Security Architect | Unbegrenzt (lebendes Dokument) |
| **Zero-Trust-Assessment** | [GRC-Plattform] – Compliance-Assessments | Jährliche Selbstbeurteilung mit CISA ZT Maturity Model v2.0 | ISB | 3 Jahre |
| **Defence-in-Depth-Validierung** | [GRC-Plattform] – Kontrollvalidierungsmodul | Halbjährliche Kontrollschicht-Analyse gemäss ISMS-IMP-A.8.27.4-UG/TG | Security Team | 3 Jahre |
| **Schulungsaufzeichnungen** | [LMS] – Learning Management System | SSE-Schulungsabschluss pro Rollenanforderungen verfolgt | HR + ISB | 3 Jahre nach Beschäftigungsende |
| **Drittanbieter-Beurteilungen** | [GRC-Plattform] – Lieferantenrisiko-Modul | Lieferantenarchitektur-Sicherheitsbewertungen gemäss ISMS-POL-A.5.19-23 | Security Architect | Aktiv + 2 Jahre nach Vertragsende |
| **Ausnahmeregister** | [GRC-Plattform] – Risiko- und Ausnahmeregister | Ausnahmeanträge gemäss Abschnitt 4.2 genehmigt | ISB | Aktiv + 2 Jahre nach Schliessung |
| **Kennzahlen-Dashboard** | [GRC-Plattform] – Kennzahlen-Modul | Vierteljährlich automatisiert aus Architektur-Review-Daten | Security Team | 3 Jahre |

**Nachweis-Zugänglichkeit**: Alle Nachweise MÜSSEN internen Prüfern und externen Zertifizierungsprüfern auf Anfrage innerhalb von 2 Arbeitstagen zugänglich sein.

---

# Genehmigungsprotokoll

| Rolle | Name | Datum |
|-------|------|-------|
| **Informationssicherheitsbeauftragter (ISB)** | [Name] | [Date to be set] |
| **Technischer Leiter (TL)** | [Name] | [Date to be set] |
| **Geschäftsleitung** | [Name] | [Date to be set] |

---

**ENDE DES RICHTLINIENDOKUMENTS**

---

*Diese Richtlinie legt die grundlegenden Anforderungen von [Organisation] an Secure Systems Engineering fest – den Grundstein von ISMS CORE. Implementierungsverfahren sind in ISMS-IMP-A.8.27 (UG/TG) dokumentiert.*

<!-- QA_VERIFIED: 2026-03-29 -->
