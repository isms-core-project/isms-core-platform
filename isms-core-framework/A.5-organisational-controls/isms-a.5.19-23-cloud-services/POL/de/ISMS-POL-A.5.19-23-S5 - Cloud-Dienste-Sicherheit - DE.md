<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S5-DE:framework:POL:a.5.19-23-s5 -->
**ISMS-POL-A.5.19-23-S5 — Cloud-Dienste-Sicherheit**
**Massnahme A.5.23: Informationssicherheit bei der Nutzung von Cloud-Diensten**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Cloud-Dienste-Sicherheit |
| **Dokumenttyp** | Richtlinienabschnitt |
| **Dokument-ID** | ISMS-POL-A.5.19-23-S5 |
| **Dokumentersteller** | Information Security Officer (ISO) |
| **Dokumenteigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | Geschäftsleitung |
| **Erstellungsdatum** | [Datum] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISO | Erstfassung für ISO 27001:2022 Massnahme A.5.23 |

**Überprüfungszyklus**: Jährlich
**Nächstes Überprüfungsdatum**: [Effective Date + 12 months]

**Genehmigungskette**:

- Primär: Informationssicherheitsbeauftragter (ISB)
- Sekundär: Information Security Officer (ISO)
- Technik: Cloud-Architektur-Teamleiter
- Compliance: Legal/Compliance Officer
- Letzte Instanz: Geschäftsleitung

**Verwandte Dokumente**:

- ISMS-POL-00 (Rahmenwerk zur regulatorischen Anwendbarkeit)
- ISMS-POL-A.5.19-23 (Übergeordnete Richtlinie – Lieferanten- und Cloud-Dienste-Sicherheit)
- ISMS-IMP-A.5.19-23.S1-UG/TG (Cloud-Dienste-Inventar & Klassifizierung)
- ISMS-IMP-A.5.19-23.S2-UG/TG (Lieferanten-Due-Diligence & Verträge)
- ISMS-IMP-A.5.19-23.S3-UG/TG (Sichere Konfiguration & Bereitstellung)
- ISMS-IMP-A.5.19-23.S4-UG/TG (Laufende Governance & Risikomanagement)
- ISMS-IMP-A.5.19-23.S5-UG/TG (Compliance-Monitoring-Dashboard)
- ISMS-REF-A.5.23 (Cloud-Anbieter-Referenzregister)
- ISO/IEC 27001:2022 Massnahme A.5.23
- ISO/IEC 27017:2015 (Cloud-Sicherheitskontrollen)
- ISO/IEC 27018:2019 (Cloud-Datenschutz)

---

# Zweck

Dieser Abschnitt definiert Anforderungen für die sichere Beschaffung, Nutzung, Verwaltung und Beendigung von Cloud-Diensten. Er legt das Cloud-Dienste-Lebenszyklusrahmenwerk und Cloud-spezifische Sicherheitskontrollen fest.

**Massnahmenziel (ISO 27002:2022):**
> „Prozesse für die Beschaffung, Nutzung, Verwaltung und den Ausstieg aus Cloud-Diensten sollen entsprechend den Informationssicherheitsanforderungen der Organisation etabliert werden."

**Kritischer Grundsatz – „Die Cloud ist der Computer jemand anderen"**: Cloud-Dienste laufen auf Infrastruktur, die Sie nicht kontrollieren, in Jurisdiktionen, die Sie nicht regieren, mit Zugang durch Personal, das Sie nicht überprüft haben. Das Modell der geteilten Verantwortung bedeutet, dass Sicherheitsversagen im Bereich beider Parteien auftreten können – aber die Compliance- und Reputationsfolgen treffen die [Organisation]. Diese Richtlinie erfordert systematisches Cloud-Lebenszyklusmanagement von der Auswahl bis zum Ausstieg, mit kontinuierlicher Verifizierung, dass die Sicherheitsbehauptungen des Anbieters der operativen Realität entsprechen.

**Zusammenfassung der ISO/IEC 27002:2022-Leitlinien**:

- Die Beschaffung von Cloud-Diensten soll einem risikobasierten Auswahlprozess mit umfassender Sicherheitsbewertung folgen
- Cloud-Dienste-Vereinbarungen sollen Informationssicherheitsanforderungen adressieren und das Modell der geteilten Verantwortung klar definieren
- Das Modell der geteilten Verantwortung soll explizit verstanden, dokumentiert und gemanagt werden
- Cloud-Dienste-Konfiguration soll gemäss Anbieter-Sicherheitsbaselines gesichert werden
- Cloud-Datenresidenz- und Souveränitätsanforderungen sollen gemäss regulatorischen Pflichten (DSGVO, nDSG) durchgesetzt werden
- Cloud-Dienste-Überwachung und -Protokollierung soll mit angemessener Aufbewahrung implementiert werden
- Cloud-Dienste-Exit-Strategie soll geplant und getestet werden, einschliesslich Datenexport und Übergangsverfahren
- Cloud-spezifische Risiken (Multi-Tenancy, Datenvermischung, Jurisdiktion, Anbieterzugang) sollen bewertet und mitigiert werden
- Cloud-Anbieter-Zertifizierungen (SOC 2, ISO 27017, CSA STAR) sollen jährlich verifiziert werden

---

# Geltungsbereich

## Cloud-Dienstemodelle

| Modell | Beschreibung | Verantwortung der [Organisation] |
|--------|-------------|----------------------------------|
| **IaaS** | Infrastructure as a Service | Betriebssystem, Middleware, Anwendungen, Daten |
| **PaaS** | Platform as a Service | Anwendungen, Daten |
| **SaaS** | Software as a Service | Daten, Benutzerkonfiguration |
| **XDR/SECaaS** | Security as a Service | Konfiguration, Richtlinien, Reaktion |
| **FaaS** | Function as a Service | Code, Daten |
| **DaaS** | Desktop as a Service | Benutzerdaten, Endpunktrichtlinien |

## Cloud-Bereitstellungsmodelle

| Modell | Beschreibung | Überlegung |
|--------|-------------|-----------|
| **Öffentlich** | Gemeinsame Infrastruktur, Multi-Tenancy | Datenisolation, Compliance |
| **Privat** | Dedizierte Infrastruktur | Kosten, Verwaltungsaufwand |
| **Hybrid** | Mix aus öffentlich und privat | Integrationskomplexität |
| **Multi-Cloud** | Mehrere Cloud-Anbieter | Portabilität, Konsistenz |
| **Community** | Geteilt von einer bestimmten Gemeinschaft | Governance, geteiltes Risiko |

## Anwendbarkeit

Dieser Abschnitt gilt für alle Cloud-Dienste, die:

- Organisationsdaten verarbeiten, speichern oder übertragen
- Infrastruktur für Organisationssysteme bereitstellen
- Von Organisationsbenutzern aufgerufen werden
- Mit Organisationssystemen integriert sind

---

# Cloud-Dienste-Lebenszyklus

## Lebenszyklusübersicht

```
┌─────────────────────────────────────────────────────────────┐
│                 CLOUD-DIENSTE-LEBENSZYKLUS                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐  │
│  │ AUSWAHL  │ → │IMPLEMEN- │ → │ BETRIEB  │ → │ AUSSTIEG │  │
│  │          │   │TIERUNG   │   │          │   │          │  │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘  │
│       │              │              │              │         │
│       ▼              ▼              ▼              ▼         │
│  • Anforderungen • Konfigur.  • Überwachen  • Ausstieg      │
│  • Bewerten      • Integrieren• Überprüfen    planen         │
│  • Risiko-Bew.   • Migrieren  • Patchen    • Daten export.  │
│  • Vertrag       • Testen     • Vorfälle   • Übergang       │
│  • Genehmigen    • Live-Gang  • Änderungen • Terminieren    │
│                                            • Löschung ver.  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Phasen-Anforderungsübersicht

| Phase | Hauptaktivitäten | Ergebnisse |
|-------|----------------|-----------|
| **Auswahl** | Anforderungen, Bewertung, Risikobewertung | Genehmigter Dienst + Vertrag |
| **Implementierung** | Konfiguration, Integration, Migration | Produktionsbereiter Dienst |
| **Betrieb** | Überwachung, Überprüfung, Incident Response | Laufende Compliance |
| **Ausstieg** | Planung, Datenexport, Beendigung | Sauberer Ausstieg + Datenvernichtung |

---

# Auswahl & Bewertung

## Vorab-Anforderungen für die Auswahl

Vor der Bewertung von Cloud-Diensten:

| Anforderung | Beschreibung |
|-------------|-------------|
| Geschäftsbedarf | Dokumentierte Geschäftsbegründung |
| Datenklassifizierung | Klassifizierung der zu verarbeitenden Daten |
| Compliance-Anforderungen | Regulatorische und vertragliche Pflichten |
| Integrationsanforderungen | Beteiligte Systeme und Datenflüsse |
| Sicherheitsanforderungen | Mindest-Sicherheitskontrollen |

## Cloud-Dienste-Bewertungskriterien

| Kategorie | Bewertungsbereiche |
|-----------|-------------------|
| **Sicherheit** | Zertifizierungen, Kontrollen, Vorfallshistorie |
| **Compliance** | Regulatorische Ausrichtung, Datenresidenz, Audit-Unterstützung |
| **Zuverlässigkeit** | SLA, Betriebszeit-Verlauf, Redundanz |
| **Portabilität** | Datenexport, API-Standards, Lock-in-Risiko |
| **Support** | Verfügbarkeit, Reaktionsfähigkeit, Kompetenz |
| **Lebensfähigkeit** | Finanzielle Stabilität, Marktposition, Roadmap |

## Sicherheitsbewertungs-Checkliste

| Anforderung | Verifizierungsmethode |
|-------------|----------------------|
| ISO 27001 oder SOC 2-Zertifizierung | Zertifikat-/Berichtsprüfung |
| Verschlüsselung im Ruhezustand und bei Übertragung | Technische Dokumentation |
| Multi-Faktor-Authentifizierung | Konfigurationsfähigkeit |
| Zugriffsprotokollierung und Überwachung | Funktionsverifizierung |
| Datenresidenzoptionen | Vertrag und technische Prüfung |
| Störungsmeldeverfaren | Vertrag und Dokumentation |
| Backup- und Wiederherstellungsfähigkeiten | Technische Dokumentation |
| Penetrationstestprogramm | Berichtverfügbarkeit |
| Schwachstellenmanagement | Prozessdokumentation |
| Sub-Auftragsverarbeiter-Transparenz | Sub-Auftragsverarbeiter-Listenprüfung |

## Risikobewertung

Vor der Genehmigung soll eine Risikobewertung durchgeführt werden:

| Risikobereich | Bewertungsfokus |
|---------------|----------------|
| Datenexposition | Welche Daten, welche Klassifizierung, welche Kontrollen |
| Verfügbarkeit | Geschäftsauswirkung bei Dienstausfall |
| Compliance | Regulatorische Implikationen |
| Vendor Lock-in | Wechselkosten und -machbarkeit |
| Konzentration | Abhängigkeit von einzelnem Anbieter |
| Jurisdiktion | Rechts- und Regulierungsrahmen |

## Genehmigungsanforderungen

| Datenklassifizierung | Erforderliche Genehmigung |
|---------------------|--------------------------|
| Eingeschränkt | ISB + Geschäftsverantwortlicher + Recht |
| Vertraulich | ISO + Geschäftsverantwortlicher |
| Intern | Geschäftsverantwortlicher + Sicherheitsprüfung |
| Öffentlich | Geschäftsverantwortlicher |

---

# Implementierung & Konfiguration

## Sichere Konfigurationsprinzipien

| Prinzip | Implementierung |
|---------|----------------|
| **Geringstmögliche Berechtigung** | Minimale Berechtigungen für Benutzer und Dienste |
| **Tiefenverteidigung** | Mehrere Kontrollebenen |
| **Sichere Standards** | Sicher starten, nur mit Genehmigung abweichen |
| **Trennung** | Umgebungen, Daten, Zugang isolieren |
| **Verschlüsselung** | Daten im Ruhezustand und bei Übertragung schützen |
| **Protokollierung** | Umfassende Audit-Trails |

## Konfigurationsanforderungen

| Kontrollbereich | Anforderungen |
|----------------|--------------|
| **Identität & Zugang** | SSO-Integration, MFA durchgesetzt, RBAC implementiert |
| **Datenschutz** | Verschlüsselung aktiviert, Klassifizierung angewendet, DLP konfiguriert |
| **Netzwerksicherheit** | Zugangsbeschränkungen, sichere Konnektivität, Segmentierung |
| **Protokollierung & Überwachung** | Audit-Logs aktiviert, SIEM-Integration, Alarmierung konfiguriert |
| **Backup & Wiederherstellung** | Automatisierte Backups, getestete Wiederherstellung, angemessene Aufbewahrung |
| **Endpunktintegration** | Sicherer Zugang von verwalteten Geräten |

## Implementierungs-Checkliste

| Phase | Aktivitäten |
|-------|------------|
| **Vor der Bereitstellung** | Sicherheitskonfigurationsprüfung, Integrationstest |
| **Bereitstellung** | Stufenweiser Rollout, Validierungstest |
| **Nach der Bereitstellung** | Sicherheitsverifizierung, Überwachungsbestätigung |
| **Dokumentation** | Konfigurationsaufzeichnungen, Runbooks, Zugangsinventar |

## Datenmigrations-Sicherheit

| Anforderung | Beschreibung |
|-------------|-------------|
| Migrationsplan | Dokumentierter Ansatz mit Sicherheitskontrollen |
| Dateninventar | Welche Daten, Klassifizierung, Volumen |
| Sichere Übertragung | Verschlüsselte Übermittlung |
| Validierung | Datenintegritätsverifizierung |
| Altdaten-Bereinigung | Sichere Löschung aus der Quelle (falls anwendbar) |

---

# Betriebsmanagement

## Laufende Sicherheitsaktivitäten

| Aktivität | Häufigkeit | Verantwortlich |
|-----------|-----------|---------------|
| Zugriffsüberprüfung | Vierteljährlich | Geschäftsverantwortlicher + IT |
| Konfigurationsüberprüfung | Halbjährlich | Sicherheit + IT |
| Sicherheitsbewertung | Jährlich | Sicherheit |
| Compliance-Verifizierung | Jährlich | Compliance |
| Backup-Tests | Halbjährlich | IT-Betrieb |
| Incident-Response-Drill | Jährlich | Sicherheit |

## Änderungsmanagement

Cloud-Diensteänderungen sollen dem organisatorischen Änderungsmanagement folgen:

| Änderungstyp | Prozess |
|--------------|---------|
| Anbieterinitiiert | Benachrichtigung prüfen, Auswirkung bewerten, genehmigen/eskalieren |
| Organisationsinitiiert | Änderungsanfrage, Sicherheitsprüfung, Genehmigung, Implementierung |
| Notfall | Beschleunigte Genehmigung, Post-Implementierungs-Überprüfung |

## Störungsmanagement

| Anforderung | Beschreibung |
|-------------|-------------|
| Erkennung | Sicherheitsereignisse über Logs und Alarme überwachen |
| Benachrichtigung | Anbietermeldungen empfangen und verarbeiten |
| Reaktion | Incident-Response-Verfahren durchführen |
| Koordination | Mit Anbieter bei der Untersuchung zusammenarbeiten |
| Wiederherstellung | Dienste und Daten bei Bedarf wiederherstellen |
| Lessons Learned | Kontrollen basierend auf Vorfällen aktualisieren |

## Forensische Bereitschaft

| Anforderung | Beschreibung |
|-------------|-------------|
| Log-Aufbewahrung | Ausreichende Aufbewahrung für Untersuchungen |
| Log-Zugang | Möglichkeit, Logs zur Analyse abzurufen |
| Beweissicherung | Anbieterkooperation für rechtliche Vorbehalte |
| Beweiskette | Dokumentation für Rechtsverfahren |
| Ermittlungsunterstützung | Anbieter-Unterstützung bei Forensik |

---

# Modell der geteilten Verantwortung

## Verständnis der geteilten Verantwortung

```
┌─────────────────────────────────────────────────────────────┐
│         GETEILTE VERANTWORTUNG NACH DIENSTMODELL            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Verantwortung       │  IaaS    │  PaaS    │  SaaS    │      │
│ ────────────────────┼──────────┼──────────┼──────────┤      │
│ Daten               │   SIE    │   SIE    │   SIE    │      │
│ Anwendungen         │   SIE    │   SIE    │ ANBIETER │      │
│ Laufzeit            │   SIE    │ ANBIETER │ ANBIETER │      │
│ Middleware          │   SIE    │ ANBIETER │ ANBIETER │      │
│ Betriebssystem      │   SIE    │ ANBIETER │ ANBIETER │      │
│ Virtualisierung     │ ANBIETER │ ANBIETER │ ANBIETER │      │
│ Infrastruktur       │ ANBIETER │ ANBIETER │ ANBIETER │      │
│ Physisch            │ ANBIETER │ ANBIETER │ ANBIETER │      │
│                                                              │
│ SIE = Verantwortung der [Organisation]                      │
│ ANBIETER = Verantwortung des Cloud-Diensteanbieters         │
└─────────────────────────────────────────────────────────────┘
```

## Verantwortungsdokumentation

Für jeden Cloud-Dienst soll dokumentiert werden:

| Element | Dokumentation |
|---------|--------------|
| Anbieterverantwortlichkeiten | Wozu sich der Anbieter verpflichtet |
| Organisationsverantwortlichkeiten | Was wir tun müssen |
| Gemeinsame Verantwortlichkeiten | Gemeinsame Aktivitäten |
| Lücken | Bereiche, die von keiner Partei abgedeckt werden |
| Kompensierende Kontrollen | Wie Lücken adressiert werden |

---

# Exit-Strategie

## Exit-Planungsanforderungen

**Alle Cloud-Dienste sollen eine dokumentierte Exit-Strategie haben, einschliesslich:**

| Element | Beschreibung |
|---------|-------------|
| Auslöserereignisse | Bedingungen, die einen Ausstieg auslösen würden |
| Datenexport | Wie Daten in nutzbarem Format extrahiert werden |
| Alternativdienste | Identifizierte Alternativen oder interne Optionen |
| Migrationsansatz | Übergeordneter Übergangsplan |
| Zeitschätzung | Erwartete Dauer für den Ausstieg |
| Ressourcenanforderungen | Benötigte Kenntnisse und Aufwand |
| Kostenschätzung | Budget für den Übergang |

## Exit-Strategieoptionen

Exit-Strategien sollen drei primäre Übergangspfade basierend auf Servicekritikalität, Kosten, Zeitrahmen und regulatorischen Anforderungen bewerten. Die [Organisation] soll dokumentieren, welche Exit-Strategie für jeden Cloud-Dienst bei der anfänglichen Risikobewertung angemessen ist und diese jährlich überprüfen.

**Grundsätze der Exit-Strategieauswahl:**

1. **Cloud-zu-Cloud-Migration** – Standard-Exit-Strategie für die meisten Dienste (90 %+)
2. **Hybrid-Cloud-Übergang** – Bei regulatorischen/Kosten-Treibern, die teilweise Rückführung erfordern (5–10 %)
3. **On-Premises-Rückführung** – Vorbehalten für regulatorische Mandate oder aussergewöhnliche Umstände (<5 %)

---

### Cloud-zu-Cloud-Migration (Primäre Exit-Strategie)

Die Migration zu einem alternativen Cloud-Anbieter ist die **Standard-Exit-Strategie** für die meisten Dienste aufgrund niedrigerer Kapitalausgaben, schnellerer Zeitrahmen, erhaltener Elastizität und reduzierten Betriebsaufwands.

**Strategische Begründung:**

| Vorteil | Nutzen |
|---------|--------|
| Kein Infrastrukturkauf | Null CAPEX, Betriebskostenmodell bleibt erhalten |
| Schnellerer Übergang | 1–6 Monate typisch vs. 6–18 Monate für On-Premises |
| Erhaltene Elastizität | Burst-Kapazität, Auto-Skalierung, Pay-per-Use bleibt erhalten |
| Moderne Fähigkeiten | Zugang zu Cloud-nativen Diensten (Container, Serverless, KI/ML) |
| Reduzierer Betriebsaufwand | Vom Anbieter verwaltete Infrastruktur, Patching, Updates |
| Geografische Flexibilität | Multi-Region-Bereitstellung ohne Anlageninfrastrukturinvestition |

**Bewertungsanforderungen:**

| Kriterium | Bewertungsmethode | Dokumentation |
|-----------|------------------|--------------|
| **Alternativanbieter** | 2+ machbare Alternativen identifizieren (AWS, Azure, GCP, OVHcloud, Alibaba Cloud) | Anbieter-Vergleichsmatrix |
| **Dienstparität** | Prüfen, ob Alternative gleichwertige Funktionalität bietet | Dienst-Feature-Mapping |
| **Datenportabilität** | Kompatibilität des Exportformats mit Alternative bestätigen | Datenexport-Testergebnisse |
| **Integrationskompatibilität** | API/Integrations-Neuschreibungsanforderungen bewerten | Integrationsfolgenanalyse |
| **Kostenvergleich** | 3-Jahres-TCO der Alternative vs. aktuellen Anbieter | TCO-Tabelle |
| **Zertifizierungsausrichtung** | Alternative erfüllt Compliance-Anforderungen | Zertifizierungsmatrix |
| **Migrationszeit** | Übergangsdauer einschliesslich Tests schätzen | Projektzeitplan (Gantt) |
| **Proof-of-Concept** | Kritischen Workload beim alternativen Anbieter testen (jährlich gemäss DORA Art. 28.6) | PoC-Testbericht |

**Migrationsphasen (Cloud-zu-Cloud):**

| Phase | Dauer | Aktivitäten | Ergebnisse |
|-------|-------|------------|-----------|
| **Bewertung** | 2–4 Wochen | Alternativanbieter-Evaluation, Kostenanalyse, Risikobewertung | Anbieterauswahl, Migrationsplan |
| **Vorbereitung** | 4–8 Wochen | Kontoeinrichtung, Netzwerkkonnektivität, IAM-Konfiguration | Zielumgebung konfiguriert |
| **Migration** | 4–12 Wochen | Datenmigration, Anwendungsbereitstellung, Integrationstest | Migrierte Dienste in Produktion |
| **Validierung** | 2–4 Wochen | Leistungstest, Sicherheitsvalidierung, Benutzerakzeptanz | Abzeichnung, Quelle ausser Betrieb |
| **Bereinigung** | 1–2 Wochen | Quellumgebung ausser Betrieb, Datenvernichtungsverifizierung | Vernichtungszertifikate |

**Gesamtzeitrahmen: 3–6 Monate typisch für Dienste mittlerer Komplexität**

**Kostenbetrachtungen (Cloud-zu-Cloud):**

| Kostenkategorie | Geschätzter Bereich | Hinweise |
|-----------------|-------------------|---------|
| **Professional Services** | CHF 20K–100K | Beratung, Migrationsunterstützung |
| **Daten-Egress-Gebühren** | CHF 5K–50K | Ausgehende Datenübertragung vom Quell-Anbieter |
| **Parallelbetrieb** | 1–3 Monate Cloud-Kosten | Beide Umgebungen während Migration betreiben |
| **Tests/Validierung** | CHF 10K–30K | Lasttests, Sicherheitsbewertung |
| **Schulung** | CHF 5K–20K | Mitarbeiterschulung für neue Anbieterplattform |
| **GESAMT (einmalig)** | **CHF 40K–200K** | Variiert je Dienstkomplexität und Datenvolumen |

**Wann Cloud-zu-Cloud optimal ist:**

✅ **Dienst ist cloud-nativ** (Container, Microservices, Serverless, verwaltete Datenbanken)
✅ **Workload hat variable Nachfrage** (Traffic-Spitzen, saisonale Muster, unvorhersehbares Wachstum)
✅ **Organisation fehlt On-Premises-Kapazität** (kein Rechenzentrum, begrenzte Infrastrukturpersonal)
✅ **Keine regulatorischen Mandate** für physisches On-Premises-Hosting
✅ **Cloud-TCO bleibt günstig** im Vergleich zu On-Premises über 3–5 Jahre
✅ **Geografische Verteilung erforderlich** (Multi-Region, globaler Niedriglatenz-Zugang)
✅ **Moderne Cloud-Dienste genutzt** (KI/ML, IoT, Analytics, CDN)

**Beispielszenario:**

> **SaaS-Kollaborationsplattform (Microsoft 365 → Google Workspace)**
> - **Dienst**: E-Mail, Kalender, Dateispeicher, Videokonferenzen
> - **Benutzer**: 300 Mitarbeitende
> - **Migrationszeit**: 3 Monate (Planung 4 Wochen, Migration 8 Wochen, Validierung 2 Wochen)
> - **Migrationskosten**: CHF 45K (Beratung CHF 30K, Schulung CHF 10K, parallele Lizenzen CHF 5K)
> - **Ergebnis**: Null CAPEX, erhaltene Cloud-Elastizität, verbesserte Kollaborationsfunktionen

---

### Hybrid-Cloud-Übergang (Teilweise Rückführung)

Der Hybrid-Ansatz behält einige Workloads in der Cloud bei, während ausgewählte Komponenten zur On-Premises-Infrastruktur rückgeführt werden.

**Typische Hybrid-Szenarien:**

| Szenario | Cloud-Komponente | On-Premises-Komponente | Begründung |
|----------|-----------------|----------------------|-----------|
| **Datensouveränität** | Anwendungsebene, Compute, Dev/Test | Datenbank mit sensiblen/regulierten Daten | Regulatorische Datenresidenzanforderungen (revDSG, Branchengesetze) |
| **Kostenoptimierung** | Burst-Kapazität, Nicht-Produktion | Basis-Produktionsworkload | Vorhersehbare Baseline On-Premises, elastischer Überlauf in Cloud |
| **Latenzempfindlich** | Backup/DR, Analytics, Reporting | Echtzeit-Transaktionsverarbeitung | Netzwerklatenz für kritische interaktive Workloads reduzieren |
| **Stufenmigration** | Neue Cloud-native Dienste | Legacy-Systeme in Überarbeitung | Schrittweiser Übergang über 12–24 Monate |
| **Regulatorisch hybrid** | Nicht-kritische Datenverarbeitung | Vertrauliche/eingeschränkte Daten | DSGVO Art. 44–50 Übermittlungsbeschränkungen |

**Kapital- & Betriebskosten (Hybrid-Übergang):**

| Komponente | CAPEX (Jahr 0) | OPEX (jährlich) | Hinweise |
|------------|---------------|----------------|---------|
| **On-Premises-Infrastruktur** | CHF 50K–500K | CHF 30K–100K | Teilinfrastruktur (Compute, Speicher, Netzwerk) |
| **Netzwerkkonnektivität** | CHF 10K–30K | CHF 5K–50K/Jahr | VPN oder Standleitungen (1–10 Gbps) |
| **Hybrid-Management-Tools** | CHF 0–20K | CHF 10K–50K/Jahr | Orchestrierung (Terraform, Ansible), Überwachung |
| **Kenntnisse/Schulung** | CHF 0–30K | CHF 20K–50K | Mitarbeiterschulung für Hybrid-Architekturen |
| **Datensynchronisation** | CHF 5K–20K | CHF 5K–20K | Replikationswerkzeuge, Bandbreitenkosten |
| **Professional Services** | CHF 30K–100K | CHF 10K–30K | Architekturdesign, Implementierungsunterstützung |
| **GESAMT** | **CHF 95K–700K** | **CHF 80K–300K/Jahr** | **3-Jahres-TCO: CHF 335K–1,6M** |

---

### On-Premises-Rückführung (Vollständiger Rückbau)

Vollständige Migration von der Cloud zu im Besitz der [Organisation] befindlicher Infrastruktur. Dies ist die **risikobehaftetste, kostspieligste** Exit-Strategie und sollte nur in Betracht gezogen werden, wenn durch regulatorische Mandate oder aussergewöhnliche Umstände gerechtfertigt.

**⚠️ KRITISCH: On-Premises-Rückführung ist in <5 % der Cloud-Ausstiegsszenarien wirtschaftlich gerechtfertigt.**

**Realistische Szenarien für vollständige Rückführung:**

| Szenario | Begründung | Wahrscheinlichkeit |
|----------|-----------|-------------------|
| **Regulatorisches Mandat** | Gesetzliche Anforderung für physisch kontrollierte On-Premises-Infrastruktur | Niedrig-Mittel |
| **Kosteninversion** | Cloud-Kosten übersteigen On-Premises-TCO über 3–5 Jahre für stabile Hochvolumen-Workloads | Niedrig |
| **Strategische Unabhängigkeit** | Alle externen Abhängigkeiten für kritische Infrastruktur eliminieren | Sehr niedrig |
| **Anbieterausfall** | Cloud-Anbieter-Insolvenz, nicht behebbarer Vorfall, geopolitischer Zugangsvertust | Sehr niedrig |
| **Konzentrationsrisiko** | DORA Art. 28.9 Diversifizierung von einzelnem kritischen Anbieter | Niedrig |

**Kapital- & Betriebskostenschätzungen (Mittelgrosse Organisation, ~300 Mitarbeitende):**

**CAPEX (Jahr 0) – Infrastrukturaufbau:**

| Komponente | Spezifikation | Kostenbereich (CHF) | Lebenszyklus |
|------------|--------------|---------------------|-------------|
| **Compute** | 50 VMs @ 4–8 vCPU, 16–32 GB RAM | 150K–300K | 3–5 Jahre |
| **Speicher** | 100 TB nutzbar (SAN/NAS, RAID 6, gestuft) | 50K–150K | 5 Jahre |
| **Netzwerk** | Core-Switches (10/25 GbE), Firewalls, Load Balancer | 40K–80K | 5 Jahre |
| **Backup** | Backup-Appliances, Deduplizierung, Tape-Library (optional) | 30K–60K | 5 Jahre |
| **Einrichtungen** | Rack-Platz, Stromverteilung, Kühlung (falls Colo) | 0–100K | N/A |
| **Software-Lizenzen** | Virtualisierung (VMware, Hyper-V), Backup (Veeam, Commvault) | 20K–50K | 1–3 Jahre |
| **Professional Services** | Migrationsberatung, Implementierungsunterstützung | 50K–100K | Einmalig |
| **Puffer** | 15–20 % für unerwartete Kosten | 50K–150K | Einmalig |
| **GESAMT CAPEX** | | **CHF 390K–990K** | |

**OPEX (jährlich) – Laufender Betrieb:**

| Komponente | Spezifikation | Kostenbereich (CHF) | Hinweise |
|------------|--------------|---------------------|---------|
| **Personalkosten** | 3–5 VZÄ (Sysadmin, Netzwerk, Sicherheit) @ CHF 100K–120K | 300K–600K | Gehälter, Leistungen, Schulung |
| **Wartung** | Hardware-Support-Verträge (15–20 % des CAPEX jährlich) | 30K–80K | Kritisch für Betriebszeit |
| **Software-Lizenzen** | Virtualisierung, Backup, Überwachung, Sicherheitstools | 30K–100K | Jährliche Verlängerungen |
| **Einrichtungen** | Colo-Miete, Strom, Kühlung (falls kein eigenes RZ) | 30K–100K | |
| **Netzwerk** | WAN-Konnektivität, ISP, Bandbreite | 10K–30K | Multi-homed für Redundanz |
| **Beratung** | Laufende Architektur, Sicherheit, Performance-Optimierung | 20K–50K | |
| **Technologie-Erneuerungs-Reserve** | Rückstellung für 3–5-Jahres-Hardware-Erneuerung | 50K–150K | Amortisierter CAPEX |
| **GESAMT OPEX** | | **CHF 470K–1,11M/Jahr** | |

**5-Jahres-Total-Cost-of-Ownership:**

| Posten | Kosten (CHF) |
|--------|-------------|
| **CAPEX (Jahr 0)** | 390K–990K |
| **OPEX (Jahre 1–5)** | 2,35M–5,55M |
| **Technologie-Erneuerung (Jahr 3–4)** | 200K–500K |
| **GESAMT 5-JAHRES-TCO** | **CHF 2,94M–7,04M** |

**Entscheidungsrahmen: Wann On-Premises-Rückführung gerechtfertigt ist**

Vollständige On-Premises-Rückführung ist wirtschaftlich gerechtfertigt **NUR** wenn eines oder mehrere der folgenden Kriterien zutreffen:

1. **Regulatorisches Mandat**: Gesetzliche Anforderung für physisch kontrollierte, air-gapped Infrastruktur
2. **Kosteninversion**: Jährliche Cloud-Kosten >CHF 500K **UND** stabile, vorhersehbare Baseline ohne Burst-Anforderungen; 3–5-Jahres-TCO On-Premises <70 % der gleichwertigen Cloud-Kosten
3. **Strategische Unabhängigkeit**: Kritische Infrastruktur mit Null externen Abhängigkeiten (Verteidigung, Energieversorgung)
4. **Konzentrationsrisiko**: DORA Art. 28.9, Finanzinstitute reduzieren Hyperscaler-Abhängigkeit

**Für alle anderen Szenarien sind Cloud-zu-Cloud- oder Hybrid-Modelle bevorzugt** aufgrund:
- Niedrigerem TCO für die meisten Workloads (70–80 % der Fälle)
- Schnellerer Implementierung (1/3 des Zeitrahmens)
- Erhaltener Elastizität und Innovationszugang
- Reduzierter Betriebslast

---

### Entscheidungsmatrix

**Vergleichsmatrix:**

| Faktor | Cloud-zu-Cloud | Hybrid | On-Premises |
|--------|--------------|--------|------------|
| **CAPEX** | ✅ Keine Infrastruktur | 🟡 CHF 95K–700K | ❌ CHF 390K–990K |
| **OPEX (jährlich)** | 🟡 CHF 50K–500K+ | 🟡 CHF 80K–300K | ❌ CHF 470K–1,11M |
| **5-Jahres-TCO** | 🟡 CHF 250K–2,5M+ | 🟡 CHF 335K–1,6M | ❌ CHF 2,94M–7,04M |
| **Zeitrahmen** | ✅ 3–6 Monate | 🟡 6–12 Monate | ❌ 9–18 Monate |
| **Risiko** | ✅ Niedrig (bewährtes Muster) | 🟡 Mittel (Komplexität) | ❌ Hoch (Technologieschulden) |
| **Elastizität** | ✅ Erhalten | 🟡 Teilweise | ❌ Verloren (feste Kapazität) |
| **Benötigte Kenntnisse** | ✅ Vorhandene Cloud-Kenntnisse | 🟡 Cloud + On-Premises | ❌ Tiefe On-Premises-Expertise |
| **Betriebskomplexität** | ✅ Niedrig (einzelne Plattform) | 🟡 Mittel (Multi-Plattform) | ❌ Hoch (vollständiger Lebenszyklus) |
| **Regulatorische Flexibilität** | 🟡 Anbieterabhängig | ✅ Hoch (flexible Platzierung) | ✅ Volle Kontrolle |
| **Geschäftskontinuität** | ✅ Anbieter-SLA + Geo-Redundanz | 🟡 Komplex (Multi-Standort) | ❌ Organisation verantwortlich |

**Empfehlungspriorität (90-5-5-Regel):**

| Exit-Strategie | Erwartete Nutzung | Haupttreiber |
|---------------|------------------|-------------|
| **Cloud-zu-Cloud** | 90 %+ der Dienste | Kosten, Geschwindigkeit, Elastizität, Innovation |
| **Hybrid** | 5–10 % der Dienste | Regulatorische Compliance, Latenz, Kostenoptimierung |
| **On-Premises** | <5 % der Dienste | Regulatorisches Mandat, extreme Kosteninversion, strategische Unabhängigkeit |

---

### Querverbindung: Betriebskontinuität & Disaster Recovery

Exit-Strategien adressieren **geplante, freiwillige Übergänge** von Cloud-Diensten. Für **Notfallszenarien** mit Cloud-Anbieter-Ausfall verweisen Sie auf die Betriebskontinuitäts- und Disaster-Recovery-Planung (ISMS-POL-A.5.30-8.13-14).

| Szenariotyp | Planungsrahmenwerk | Zeitrahmen | Beispiel |
|-------------|---------------------|-----------|---------|
| **Geplanter Ausstieg** | Diese Richtlinie (A.5.23) | 3–18 Monate | Vertragsverhandlungsscheitern, Kostenoptimierung |
| **Notfall-Failover** | BC/DR (A.5.30-8.13-14) | Stunden–Tage | Anbieterausfall, Sicherheitsverstoss, geopolitischer Zugangsvertust |

**DORA Artikel 28.6-Anforderung:**

> „Die vertraglichen Vereinbarungen zur Nutzung von IKT-Diensten, die kritische oder wichtige Funktionen unterstützen, müssen [...] Exit-Strategien umfassen [...] sowie eine Verpflichtung des IKT-Drittanbieter-Dienstleisters zur Zusammenarbeit mit dem Finanzunternehmen und den zuständigen Behörden während Exit-Prozessen."

---

### Jährliche Überprüfung & Tests

Die Durchführbarkeit der Exit-Strategie soll jährlich überprüft und getestet werden.

**Jährliche Testanforderungen (DORA Art. 28.6-konform):**

| Exit-Strategietyp | Testanforderung | Nachweise | Häufigkeit |
|------------------|----------------|---------|-----------|
| **Cloud-zu-Cloud** | Teilmenge der Daten exportieren (10–20 % Stichprobe), auf alternativem Anbieter bereitstellen | PoC-Screenshots, Export-Validierungsbericht | Jährlich |
| **Hybrid** | Hybrid-Konnektivität, Datensynchronisationslatenz und Failover-Verfahren testen | Netzwerkleistungsmetriken, Sync-Testergebnisse | Jährlich |
| **On-Premises** | TCO-Kalkulation aktualisieren, Infrastrukturverfügbarkeit verifizieren | TCO-Tabelle, Kapazitätsplanungsbericht | Jährlich |

## Exit-Auslöser

| Auslöser | Reaktion |
|----------|---------|
| Vertragskündigung | Geplanten Ausstieg durchführen |
| Anbieterausfall | Notfall-Ausstiegsverfahren |
| Sicherheitspanne | Risikobasierte Ausstiegsentscheidung |
| Compliance-Versagen | Sofortiger Ausstieg oder Abhilfe |
| Kosten oder Wert | Geplanter Übergang |
| Strategische Änderung | Geplanter Übergang |

## Datenportabilitätsanforderungen

| Anforderung | Beschreibung |
|-------------|-------------|
| Exportformat | Branchenstandard, dokumentierte Formate |
| Exportmethode | Sicherer, zuverlässiger Extraktionsmechanismus |
| Vollständigkeit | Alle Daten, Metadaten, Konfigurationen |
| Validierung | Exportintegritätsverifizierung |
| Zeitrahmen | Angemessenes Zeitfenster für Extraktion |
| Unterstützung | Anbieterunterstützung für Migration |

## Exit-Ausführung

| Phase | Aktivitäten |
|-------|------------|
| **Planung** | Exit-Strategie, Zeitrahmen, Ressourcen bestätigen |
| **Vorbereitung** | Ziel konfigurieren, Migration testen |
| **Ausführung** | Daten exportieren, Dienste migrieren, validieren |
| **Beendigung** | Datenlöschung bestätigen, Konten schliessen |
| **Verifizierung** | Vernichtungszertifikat, Zugangsentfernung |

## Vendor-Lock-in-Mitigierung

| Strategie | Implementierung |
|----------|----------------|
| Standardformate | Portable Datenformate verwenden |
| API-Abstraktion | Tiefe proprietäre Integration vermeiden |
| Multi-Cloud-Fähigkeit | Auf Portabilität ausgelegt |
| Regelmässige Export-Tests | Datierbarkeit der Datenextraktion verifizieren |
| Alternative Bewertung | Bewusstsein für Alternativen aufrechterhalten |

---

# Cloud-spezifische Sicherheitsanforderungen

## Identitäts- & Zugriffsmanagement

| Anforderung | Implementierung |
|-------------|----------------|
| Föderierte Identität | SSO über organisatorischen Identity-Provider |
| MFA-Durchsetzung | Für alle Benutzer erforderlich, für Admins obligatorisch |
| Privilegierter Zugang | Just-in-time, zeitlich begrenzt, überwacht |
| Dienstkonten | Inventar, Anmeldedatenrotation, geringstmögliche Berechtigung |
| Zugriffsüberprüfungen | Regelmässige Zertifizierung von Zugriffsrechten |

## Datenschutz

| Anforderung | Implementierung |
|-------------|----------------|
| Verschlüsselung bei Übertragung | TLS 1.2+ für alle Kommunikationen |
| Verschlüsselung im Ruhezustand | Anbieter- oder kundenverwaltete Schlüssel |
| Schlüsselmanagement | Sichere Schlüsselspeicherung, Rotationsrichtlinie |
| Datenklassifizierung | Labels angewendet, Kontrollen durchgesetzt |
| Datenresidenz | Verarbeitungsstandort dokumentiert und verifiziert |
| Datentrennung | Logische oder physische Isolation nach Anforderung |

## Sicherheitsüberwachung

| Anforderung | Implementierung |
|-------------|----------------|
| Audit-Protokollierung | Alle sicherheitsrelevanten Ereignisse protokolliert |
| Log-Zentralisierung | Logs in organisatorisches SIEM exportiert |
| Alarmierung | Sicherheitsereignisse lösen geeignete Alarme aus |
| Aufbewahrung | Logs gemäss Richtlinie aufbewahrt (mindestens 12 Monate) |
| Bedrohungserkennung | Anbieter- und Organisationserkennung |

---

# Multi-Cloud-Überlegungen

## Multi-Cloud-Herausforderungen

| Herausforderung | Mitigierung |
|-----------------|------------|
| Inkonsistente Kontrollen | Standardisierte Baseline über alle Anbieter |
| Transparenzlücken | Einheitliche Überwachung und Protokollierung |
| Kompetenzanforderungen | Schulung und Dokumentation |
| Komplexität | Klare Architektur und Governance |
| Kostenverwaltung | Zentralisierte Verfolgung und Optimierung |

## Multi-Cloud-Governance

| Element | Anforderung |
|---------|------------|
| Richtlinienkonsistenz | Gleiche Sicherheitsrichtlinien über alle Anbieter |
| Identitätsföderation | Einheitliche Identität über alle Clouds |
| Überwachung | Sicherheitsüberwachung via Zusammenfassungs-Dashboards |
| Incident Response | Koordinierte Reaktionsverfahren |
| Compliance | Konsistente Compliance-Position |

---

# Referenzen

| Dokument | Beziehung |
|----------|----------|
| ISMS-POL-A.5.19-23 | Übergeordnetes Richtlinienrahmenwerk |
| ISMS-POL-A.5.19-23-S1 | Cloud-Anbieter sind Lieferanten |
| ISMS-POL-A.5.19-23-S2 | Cloud-Vertragsanforderungen |
| ISMS-POL-A.5.19-23-S3 | Cloud-Sub-Auftragsverarbeiter-Management |
| ISMS-POL-A.5.19-23-S4 | Cloud-Dienste-Überwachung |
| ISO/IEC 27017 | Cloud-Sicherheitskontrollen |
| ISO/IEC 27018 | Cloud-Datenschutz |

---

**Nächstes Dokument:** ISMS-POL-A.5.19-23-S6 — Bewertungsmethodik & Automatisierung

---

*„Die Cloud ist nur der Computer jemand anderen – aber Sie sind noch immer für Ihre Daten verantwortlich."*
<!-- QA_VERIFIED: 2026-03-28 -->
