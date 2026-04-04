<!-- ISMS-CORE:REF:ISMS-REF-A.5.19-23-cloud-service-provider-registry-DE:framework:REF:a.5.19-23 -->
**ISMS-REF-A.5.19-23 — Cloud-Anbieter-Referenzregister**
**Massgebliches Referenzregister für die Bewertung externer Cloud- und SaaS-Anbieter**

---

**Dokumentensteuerung**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Cloud-Anbieter-Referenzregister |
| **Dokumententyp** | Intern – Technische Referenz (Kein ISMS-Dokument) |
| **Dokument-ID** | ISMS-REF-A.5.19-23 |
| **Dokumentenersteller** | Informationssicherheitsbeauftragter (ISB) |
| **Dokumenteneigentümer** | Geschäftsführer (GF) |
| **Genehmigt von** | ISB (Technische Referenz – Keine Genehmigung der Geschäftsleitung erforderlich) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | ISB / IT-Betrieb | Erstregister |

**Überprüfungszyklus**: Halbjährlich (oder bei wesentlichen Änderungen der Anbieter-Landschaft)
**Nächstes Überprüfungsdatum**: [Genehmigungsdatum + 6 Monate]
**Genehmigende**:

- Informationssicherheitsbeauftragter (ISB)
- IT-Betriebsleiter
- Beschaffung/Vendor Management

**Verteilung**: ISMS-Stakeholder, Systemeigentümer, Beschaffung, Vendor Management
**Referenziert in**: ISMS-POL-A.5.19 bis A.5.23, ISMS-POL-A.8.10, Anbieterbewertungen

---

**Zweck**

Dieses Dokument stellt das **massgebliche Referenzregister** von Cloud-Dienstanbietern und SaaS-Plattformen bereit, die in organisatorischen IT-Umgebungen häufig anzutreffen sind.

**Verwendung:**

- Vorausfüllen von Bewertungsarbeitsmappen (A.5.23, A.8.10 usw.)
- Standardisierung der Anbieterkategorisierung im gesamten ISMS
- Ermöglichung konsistenter Anbieterrisikobeurteilung
- Unterstützung von Datenlöschungs- und Aufbewahrungskonformität (A.8.10)

**Wesentlicher Grundsatz:** Dieses Register ist **anbieterneutral für Richtlinienzwecke** — es katalogisiert Anbieter zur Bewertung, nicht zur Empfehlung. Organisationen dokumentieren IHRE spezifische Nutzung und Konfigurationen.

---

# Anbieterklassifizierungsrahmenwerk

**Servicemodelkategorien**

| Code | Modell | Beschreibung |
|------|--------|-------------|
| **IaaS** | Infrastructure as a Service | Virtuelle Maschinen, Speicher, Netzwerk |
| **PaaS** | Platform as a Service | Entwicklungsplattformen, verwaltete Laufzeitumgebungen |
| **SaaS** | Software as a Service | Endbenutzeranwendungen |
| **DBaaS** | Database as a Service | Verwaltete Datenbankdienste |
| **BaaS** | Backup as a Service | Verwaltete Sicherungs- und Wiederherstellungsdienste |
| **SECaaS** | Security as a Service | Verwaltete Sicherheitsdienste |
| **IDaaS** | Identity as a Service | Identitäts- und Zugriffsmanagement |
| **CDN** | Content Delivery Network | Edge-Caching und -Bereitstellung |

## Bewertungspriorität-Stufen

| Stufe | Priorität | Kriterien | Bewertungshäufigkeit |
|-------|-----------|-----------|---------------------|
| **Stufe 1** | Kritisch | Hyperscaler, Kerninfrastruktur | Vierteljährlich |
| **Stufe 2** | Kritisch | Grosse Enterprise-Plattformen | Vierteljährlich |
| **Stufe 3** | Hoch | Infrastruktur- & Sicherheitsanbieter | Halbjährlich |
| **Stufe 4** | Hoch | Sicherungs- & Speicherspezialisten | Halbjährlich |
| **Stufe 5** | Hoch | Kommunikation & Zusammenarbeit | Halbjährlich |
| **Stufe 6** | Mittel | DevOps & Entwicklungsplattformen | Jährlich |
| **Stufe 7** | Mittel | Verwaltete Datenbanken & Analytik | Jährlich |
| **Stufe 8** | Hoch | Sicherheit & Identität (sensibel) | Halbjährlich |
| **Stufe 9** | Hoch | HR & Finanzen (PII-intensiv) | Halbjährlich |
| **Stufe 10** | Regional | Schweizer/EU-Regionalanbieter | Halbjährlich |

## Datensensibilitätsindikatoren

| Indikator | Beschreibung | Löschpriorität |
|-----------|-------------|----------------|
| 🔴 **PII** | Personenbezogene Daten | Kritisch (DSGVO Art. 17) |
| 🟠 **PCI** | Zahlungskartendaten | Kritisch (PCI DSS) |
| 🟡 **CONF** | Vertrauliche Geschäftsdaten | Hoch |
| 🟢 **INT** | Interne Daten | Mittel |
| ⚪ **PUB** | Öffentliche Daten | Niedrig |

---

# Anbieterregister

## Stufe 1: Hyperscaler (Kritisch)

Kernanbieter von Cloud-Infrastruktur mit globaler Präsenz.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Microsoft Azure** | IaaS, PaaS | USA (EU-Regionen) | Compute, Speicher, Datenbanken, KI | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Microsoft 365** | SaaS | USA (EU-Regionen) | Exchange, SharePoint, OneDrive, Teams | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Amazon Web Services (AWS)** | IaaS, PaaS | USA (EU-Regionen) | EC2, S3, RDS, Glacier | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Google Cloud Platform (GCP)** | IaaS, PaaS | USA (EU-Regionen) | Compute, Speicher, BigQuery | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Google Workspace** | SaaS | USA (EU-Regionen) | Gmail, Drive, Docs, Meet | 🔴🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- Alle Stufe-1-Anbieter bieten EU-Datenspeicherort-Optionen
- Auftragsverarbeitungsverträge (AVV) mit SCCs erforderlich
- Löschfähigkeiten gut dokumentiert, aber Aufbewahrung in Backups verifizieren
- Kryptographische Löschung in der Regel verfügbar

---

## Stufe 2: Grosse Enterprise-Anbieter (Kritisch)

Enterprise-Plattformen für den Geschäftsbetrieb.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Oracle Cloud (OCI)** | IaaS, PaaS, SaaS | USA (EU-Regionen) | Datenbank, Compute, ERP, HCM | 🔴🟡 | A.5.23, A.8.10 |
| **IBM Cloud** | IaaS, PaaS | USA (EU-Regionen) | Speicher, KI, Datenbanken | 🟡 | A.5.23, A.8.10 |
| **SAP** | SaaS, PaaS | Deutschland | S/4HANA, SuccessFactors, BTP | 🔴🟡 | A.5.23, A.8.10 |
| **Salesforce** | SaaS | USA (EU-Regionen) | CRM, Marketing, Service Cloud | 🔴🟡 | A.5.23, A.8.10 |
| **ServiceNow** | SaaS | USA (EU-Regionen) | ITSM, Workflows, CMDB | 🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- SAP mit Hauptsitz in der EU (Deutschland) — günstig für DSGVO
- Oracle und Salesforce erfordern sorgfältige AVV-Prüfung
- ServiceNow CMDB kann Infrastrukturgeheimnisse enthalten

---

## Stufe 3: Infrastruktur- & Sicherheitsanbieter (Hoch)

CDN-, Edge-Sicherheits- und alternative IaaS-Anbieter.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Cloudflare** | CDN, Sicherheit, IaaS | USA | CDN, WAF, R2 Speicher, Workers | 🟡 | A.5.23, A.8.10, A.8.23 |
| **Akamai** | CDN, Sicherheit | USA | CDN, WAF, Edge-Sicherheit | 🟡 | A.5.23, A.8.23 |
| **Fastly** | CDN | USA | Edge Compute, CDN | 🟡 | A.5.23 |
| **DigitalOcean** | IaaS | USA | Droplets, Spaces, Datenbanken | 🟡 | A.5.23, A.8.10 |
| **Linode (Akamai)** | IaaS | USA | VMs, Speicher, Kubernetes | 🟡 | A.5.23, A.8.10 |
| **OVHcloud** | IaaS | Frankreich | Hosting, Speicher, Cloud | 🟡 | A.5.23, A.8.10 |
| **Hetzner** | IaaS | Deutschland | Hosting, Speicher, Cloud | 🟡 | A.5.23, A.8.10 |
| **Vultr** | IaaS | USA | VMs, Speicher, Kubernetes | 🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- OVHcloud und Hetzner mit EU-Hauptsitz (DSGVO-freundlich)
- CDN-Anbieter cachen Daten am Edge — Löschpropagierung wichtig
- Cloudflare R2 ist S3-kompatibel — Löschmechanismen verifizieren

---

## Stufe 4: Sicherungs- & Speicherspezialisten (Hoch)

Dedizierte Sicherungs-, Archiv- und Objektspeicheranbieter.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Veeam Cloud Connect** | BaaS | USA/Schweiz | Sicherungs-Repositories | 🔴🟡 | A.5.23, A.8.10 |
| **Commvault** | BaaS | USA | Sicherung, Archivierung, Wiederherstellung | 🔴🟡 | A.5.23, A.8.10 |
| **Rubrik** | BaaS | USA | Sicherung, Ransomware-Wiederherstellung | 🔴🟡 | A.5.23, A.8.10 |
| **Cohesity** | BaaS | USA | Sicherung, Datenverwaltung | 🔴🟡 | A.5.23, A.8.10 |
| **Wasabi** | Speicher | USA | S3-kompatibler Hot-Speicher | 🟡 | A.5.23, A.8.10 |
| **Backblaze B2** | Speicher | USA | S3-kompatibler Speicher | 🟡 | A.5.23, A.8.10 |
| **Dropbox Business** | SaaS | USA | Dateisynchronisation, Zusammenarbeit | 🔴🟡 | A.5.23, A.8.10 |
| **Box** | SaaS | USA | Content Management | 🔴🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- Sicherungsanbieter sind KRITISCH für A.8.10 — Daten bleiben in Sicherungskopien nach primärer Löschung bestehen
- Aufbewahrungsfristen der Sicherung an Löschanforderungen ausrichten
- Unveränderliche Sicherungsfunktionen können mit Löschverpflichtungen in Konflikt stehen
- Veeam hat Schweizer Präsenz (günstig für Schweizer Organisationen)

---

## Stufe 5: Kommunikation & Zusammenarbeit (Hoch)

Messaging-, Videokonferenz- und Team-Kollaborationsplattformen.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Slack** | SaaS | USA | Messaging, Dateien, Integrationen | 🔴🟡 | A.5.23, A.8.10 |
| **Zoom** | SaaS | USA | Video, Aufzeichnungen, Chat | 🔴🟡 | A.5.23, A.8.10 |
| **Cisco Webex** | SaaS | USA | Video, Messaging, Meetings | 🔴🟡 | A.5.23, A.8.10 |
| **Atlassian Cloud** | SaaS | Australien | Jira, Confluence, Bitbucket | 🟡 | A.5.23, A.8.10 |
| **Notion** | SaaS | USA | Workspaces, Dokumentation | 🟡 | A.5.23, A.8.10 |
| **Asana** | SaaS | USA | Projekte, Aufgaben | 🟡 | A.5.23, A.8.10 |
| **Monday.com** | SaaS | Israel | Projekte, Workflows | 🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- Kollaborationsplattformen akkumulieren im Laufe der Zeit erhebliche personenbezogene Daten
- Meeting-Aufzeichnungen erfordern explizite Löschrichtlinien
- Slack/Teams-Nachrichtenaufbewahrung steht häufig im Konflikt mit Löschanforderungen
- Atlassian mit Hauptsitz in Australien — Datenspeicherort verifizieren

---

## Stufe 6: DevOps & Entwicklungsplattformen (Mittel)

Quellcode-, CI/CD- und Container-Plattformen.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **GitHub** | SaaS | USA (Microsoft) | Repos, Actions, Packages | 🟡 | A.5.23, A.8.10 |
| **GitLab** | SaaS/Self-hosted | USA/Niederlande | Repos, CI/CD, Registry | 🟡 | A.5.23, A.8.10 |
| **Bitbucket** | SaaS | Australien (Atlassian) | Repos, Pipelines | 🟡 | A.5.23, A.8.10 |
| **Docker Hub** | SaaS | USA | Container-Images | 🟡 | A.5.23, A.8.10 |
| **JFrog** | SaaS | USA/Israel | Artefakte, Container-Registry | 🟡 | A.5.23, A.8.10 |
| **Terraform Cloud** | SaaS | USA (HashiCorp) | State-Files, Workspaces | 🟡🔴 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- Quellcode-Repositories können Geheimnisse enthalten (API-Schlüssel, Anmeldedaten)
- Terraform-State-Files enthalten häufig sensible Infrastrukturdetails
- Container-Images können eingebettete Geheimnisse enthalten — Löschung muss alle Schichten abdecken
- GitLab hat EU-Einheit (Niederlande) — Datenverarbeitungsort verifizieren

---

## Stufe 7: Datenbanken & Analytik (Mittel)

Verwaltete Datenbank- und Datenanalytikplattformen.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **MongoDB Atlas** | DBaaS | USA | Dokumentdatenbanken | 🔴🟡 | A.5.23, A.8.10 |
| **Snowflake** | SaaS | USA | Data Warehouse | 🔴🟡 | A.5.23, A.8.10 |
| **Databricks** | SaaS | USA | Analytik, Lakehouse | 🔴🟡 | A.5.23, A.8.10 |
| **Elastic Cloud** | SaaS | USA/Niederlande | Elasticsearch, Protokolle | 🔴🟡 | A.5.23, A.8.10, A.8.16 |
| **Redis Cloud** | DBaaS | USA | Cache, Datenbanken | 🟡 | A.5.23, A.8.10 |
| **PlanetScale** | DBaaS | USA | MySQL-kompatibel | 🔴🟡 | A.5.23, A.8.10 |
| **Supabase** | DBaaS | USA | PostgreSQL, Speicher | 🔴🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- Data Warehouses (Snowflake, Databricks) aggregieren oft personenbezogene Daten aus mehreren Quellen
- Elasticsearch-Indizes für Protokollierung können personenbezogene Daten enthalten — Aufbewahrung verifizieren
- Datenbank-Backups und Point-in-Time-Recovery erschweren die Löschung
- Elastic hat EU-Präsenz (Niederlande)

---

## Stufe 8: Sicherheit & Identität (Hoch – Sensibel)

Sicherheitsbetriebs- und Identitätsverwaltungsplattformen.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Okta** | IDaaS | USA | Identität, SSO, MFA | 🔴 | A.5.23, A.8.10, A.5.15 |
| **Auth0** | IDaaS | USA (Okta) | Identität, Benutzerverwaltung | 🔴 | A.5.23, A.8.10, A.5.15 |
| **CrowdStrike** | SECaaS | USA | EDR, Bedrohungsaufklärung | 🟡 | A.5.23, A.8.10 |
| **SentinelOne** | SECaaS | USA/Israel | EDR, XDR | 🟡 | A.5.23, A.8.10 |
| **Splunk Cloud** | SaaS | USA (Cisco) | Protokollaggregation, SIEM | 🔴🟡 | A.5.23, A.8.10, A.8.16 |
| **Datadog** | SaaS | USA | Überwachung, Protokolle, APM | 🟡 | A.5.23, A.8.10, A.8.16 |
| **New Relic** | SaaS | USA | APM, Protokolle, Überwachung | 🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- Identitätsanbieter (Okta, Auth0) speichern PII — kritisch für DSGVO-Löschung
- SIEM/Protokoll-Plattformen aggregieren Daten aus der gesamten Infrastruktur
- EDR-Telemetrie kann sensible Endpunktdaten enthalten
- Protokollaufbewahrungsrichtlinien müssen mit Löschanforderungen abgestimmt werden

---

## Stufe 9: HR & Finanzen (Hoch – PII-intensiv)

Personalwesen- und Finanzverwaltungsplattformen.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Workday** | SaaS | USA | HR, Finanzen, Planung | 🔴 | A.5.23, A.8.10 |
| **ADP** | SaaS | USA | Gehaltsabrechnung, HR | 🔴 | A.5.23, A.8.10 |
| **BambooHR** | SaaS | USA | HR-Verwaltung | 🔴 | A.5.23, A.8.10 |
| **Personio** | SaaS | Deutschland | HR (EU-fokussiert) | 🔴 | A.5.23, A.8.10 |
| **Xero** | SaaS | Neuseeland | Buchhaltung | 🔴🟠 | A.5.23, A.8.10 |
| **QuickBooks Online** | SaaS | USA (Intuit) | Buchhaltung | 🔴🟠 | A.5.23, A.8.10 |
| **Stripe** | SaaS | USA/Irland | Zahlungen | 🔴🟠 | A.5.23, A.8.10 |
| **PayPal** | SaaS | USA | Zahlungen | 🔴🟠 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- HR-Systeme enthalten umfangreiche personenbezogene Daten der Mitarbeitenden — DSGVO-Löschrechte gelten
- Personio mit EU-Hauptsitz (Deutschland) — günstig für DSGVO
- Zahlungsabwickler (Stripe, PayPal) haben PCI DSS-Aufbewahrungsanforderungen
- Finanzsysteme haben gesetzliche Aufbewahrungsanforderungen, die Löschung übersteuern können
- Stripe hat EU-Einheit (Irland)

---

## Stufe 10: Schweizer/EU-Regionalanbieter (Regional)

Anbieter mit Schweizer oder EU-Hauptsitz/Rechenzentren.

| Anbieter | Servicemodell | Hauptsitz | Wesentliche Dienste | Datensensibilität | ISMS-Relevanz |
|----------|---------------|-----------|--------------------|--------------------|---------------|
| **Exoscale** | IaaS | Schweiz | Compute, Speicher, Kubernetes | 🟡 | A.5.23, A.8.10 |
| **Infomaniak** | IaaS, SaaS | Schweiz | Hosting, kDrive, Mail | 🔴🟡 | A.5.23, A.8.10 |
| **Proton (ProtonMail/Drive)** | SaaS | Schweiz | Verschlüsselte E-Mail, Speicher | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Tresorit** | SaaS | Schweiz | Verschlüsselter Speicher | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **STACKIT** | IaaS | Deutschland | Cloud (Schwarz-Gruppe) | 🟡 | A.5.23, A.8.10 |
| **IONOS** | IaaS | Deutschland | Hosting, Cloud | 🟡 | A.5.23, A.8.10 |
| **Scaleway** | IaaS | Frankreich | Cloud, Speicher | 🟡 | A.5.23, A.8.10 |

**Bewertungshinweise:**
- Schweizer Anbieter (Exoscale, Infomaniak, Proton, Tresorit) unterliegen dem Schweizer nDSG
- Keine US CLOUD Act-Exposition für rein schweizerbezogene Anbieter
- Proton und Tresorit verwenden Ende-zu-Ende-Verschlüsselung — Löschung verschlüsselter Daten verifizieren
- Deutsche/Französische Anbieter unterliegen EU DSGVO (günstig)
- STACKIT ist Schwarz-Gruppe (Lidl/Kaufland) — Enterprise-grade Deutsches Cloud

---

# Registerübersicht

## Anbieteranzahl nach Stufe

| Stufe | Kategorie | Anzahl | Priorität |
|-------|-----------|--------|-----------|
| 1 | Hyperscaler | 5 | Kritisch |
| 2 | Enterprise-Anbieter | 5 | Kritisch |
| 3 | Infrastruktur & Sicherheit | 8 | Hoch |
| 4 | Sicherung & Speicher | 8 | Hoch |
| 5 | Zusammenarbeit | 7 | Hoch |
| 6 | DevOps | 6 | Mittel |
| 7 | Datenbanken & Analytik | 7 | Mittel |
| 8 | Sicherheit & Identität | 7 | Hoch |
| 9 | HR & Finanzen | 8 | Hoch |
| 10 | Schweizer/EU-Regional | 7 | Regional |
| **GESAMT** | | **68** | |

## Anbieteranzahl nach Hauptsitzregion

| Region | Anzahl | Hinweise |
|--------|--------|---------|
| USA | 48 | Die meisten erfordern AVV mit SCCs für EU/CH-Daten |
| EU (Deutschland, Frankreich, Niederlande, Irland) | 10 | DSGVO-nativ |
| Schweiz | 4 | nDSG-nativ, kein CLOUD Act |
| Sonstige (Israel, Australien, Neuseeland) | 6 | Angemessenheitsbeschlüsse verifizieren |

## Anbieteranzahl nach Datensensibilität

| Sensibilität | Anzahl | Löschpriorität |
|--------------|--------|----------------|
| 🔴 PII (Personenbezogene Daten) | 42 | Kritisch |
| 🟠 PCI (Zahlungsdaten) | 6 | Kritisch |
| 🟡 Vertraulich | 58 | Hoch |
| 🟢 Intern | 68 | Mittel |

---

# Bewertungsintegration

## Verwandte ISMS-Kontrollen

| Kontrolle | Integrationspunkt |
|-----------|-------------------|
| **A.5.19** | Informationssicherheit in Lieferantenbeziehungen |
| **A.5.20** | Berücksichtigung von Sicherheit in Lieferantenvereinbarungen |
| **A.5.21** | Management der Informationssicherheit in der IKT-Lieferkette |
| **A.5.22** | Überwachung, Überprüfung und Änderungsmanagement von Lieferantendiensten |
| **A.5.23** | Informationssicherheit bei der Nutzung von Cloud-Diensten |
| **A.8.10** | Informationslöschung |
| **A.8.24** | Einsatz von Kryptographie |

## Vorausfüllen von Excel-Arbeitsmappen

Dieses Register muss verwendet werden, um vorzufüllen:

1. **ISMS-IMP-A.5.19-23.x** — Cloud-Dienste-Bewertungsarbeitsmappen
2. **ISMS-IMP-A.8.10.3** — Drittanbieter- & Cloud-Löschungsbewertung
3. **Lieferantenrisikoregister** — Anbieterrisikobeurteilungen
4. **Datenverarbeitungsregister** — DSGVO Art. 30-Aufzeichnungen

## Dropdown-Konfiguration

**Anbietername-Dropdown** (68 Einträge + benutzerdefiniert):
```
Microsoft Azure
Microsoft 365
Amazon Web Services (AWS)
Google Cloud Platform (GCP)
Google Workspace
Oracle Cloud (OCI)
IBM Cloud
SAP
Salesforce
ServiceNow
[... alle 68 Anbieter ...]
[Benutzerdefiniert – in Notizen angeben]
```

**Servicemodell-Dropdown**:
```
IaaS – Infrastructure as a Service
PaaS – Platform as a Service
SaaS – Software as a Service
DBaaS – Database as a Service
BaaS – Backup as a Service
SECaaS – Security as a Service
IDaaS – Identity as a Service
CDN – Content Delivery Network
Hybrid/Mehrfach
```

**Stufen-Dropdown**:
```
Stufe 1 – Hyperscaler (Kritisch)
Stufe 2 – Enterprise (Kritisch)
Stufe 3 – Infrastruktur (Hoch)
Stufe 4 – Sicherung/Speicher (Hoch)
Stufe 5 – Zusammenarbeit (Hoch)
Stufe 6 – DevOps (Mittel)
Stufe 7 – Datenbank (Mittel)
Stufe 8 – Sicherheit (Hoch)
Stufe 9 – HR/Finanzen (Hoch)
Stufe 10 – Regional (Regional)
Benutzerdefiniert
```

---

# Pflege

## Auslöser für Aktualisierungen

Dieses Register muss aktualisiert werden, wenn:

- Ein neuer Cloud-Anbieter von der Organisation übernommen wird
- Ein Anbieter eine wesentliche Änderung erfährt (Übernahme, Richtlinienänderung)
- Neue regulatorische Anforderungen die Anbieterbewertung betreffen
- Der halbjährliche Überprüfungszyklus erreicht wird

**Änderungsprotokoll**

| Datum | Änderung | Autor |
|-------|--------|-------|
| [Datum] | Erstregistererstellung | [Autor] |

---

# Anhang A: Schnellreferenzkarte

```
┌─────────────────────────────────────────────────────────────────────┐
│           SCHNELLREFERENZ CLOUD-ANBIETER-BEWERTUNG                  │
├─────────────────────────────────────────────────────────────────────┤
│  KRITISCH (Vierteljährliche Bewertung)                              │
│  • Stufe 1: Azure, M365, AWS, GCP, Google Workspace                │
│  • Stufe 2: Oracle, IBM, SAP, Salesforce, ServiceNow               │
│                                                                     │
│  HOHE PRIORITÄT (Halbjährliche Bewertung)                          │
│  • Stufe 3: Cloudflare, Akamai, OVH, Hetzner                       │
│  • Stufe 4: Veeam, Rubrik, Wasabi, Dropbox, Box                    │
│  • Stufe 5: Slack, Zoom, Atlassian, Teams                          │
│  • Stufe 8: Okta, CrowdStrike, Splunk, Datadog                     │
│  • Stufe 9: Workday, Personio, Stripe                              │
│                                                                     │
│  MITTLERE PRIORITÄT (Jährliche Bewertung)                          │
│  • Stufe 6: GitHub, GitLab, Docker Hub                             │
│  • Stufe 7: MongoDB, Snowflake, Elastic                            │
│                                                                     │
│  SCHWEIZ/EU BEVORZUGT                                              │
│  • CH: Exoscale, Infomaniak, Proton, Tresorit                      │
│  • DE: SAP, Hetzner, STACKIT, IONOS                               │
│  • FR: OVHcloud, Scaleway                                          │
│  • NL: GitLab, Elastic                                             │
│  • IE: Stripe                                                       │
├─────────────────────────────────────────────────────────────────────┤
│  🔴 PII = DSGVO Art. 17 Löschrechte gelten                         │
│  🟠 PCI = Aufbewahrungsanforderungen für Zahlungskarten             │
│  🟡 CONF = Standardlöschung gemäss Aufbewahrungsrichtlinie          │
└─────────────────────────────────────────────────────────────────────┘
```

---

> *„Für eine erfolgreiche Technologie muss die Realität Vorrang vor der Public Relations haben, denn die Natur lässt sich nicht täuschen."*
*— Richard Feynman*

**Übersetzt für das ISMS:** Das Marketing Ihres Cloud-Anbieters sagt, „wir nehmen Sicherheit ernst." Dieses Register hilft Ihnen zu überprüfen, was das tatsächlich für IHRE Daten bedeutet.

---

**ENDE DES DOKUMENTS**

<!-- QA_VERIFIED: 2026-03-28 -->
