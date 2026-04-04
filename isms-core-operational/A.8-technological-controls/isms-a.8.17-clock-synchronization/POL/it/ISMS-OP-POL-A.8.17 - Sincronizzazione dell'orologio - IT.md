<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.17-IT:operational:OP-POL:a.8.17 -->
**ISMS-OP-POL-A.8.17 — Sincronizzazione dell'orologio**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sincronizzazione dell'orologio |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.17 |
| **Creatore del documento** | Responsabile della Sicurezza delle Informazioni (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.17 — Sincronizzazione dell'orologio

**Controlli correlati dell'Annex A**:

| Controllo | Relazione con la sincronizzazione dell'orologio |
|-----------|--------------------------------------------------|
| A.8.15 Registrazione degli eventi | I timestamp accurati sono un prerequisito per registrazioni di log significative |
| A.8.16 Attività di monitoraggio | La correlazione degli eventi dipende dalla sincronizzazione degli orologi tra i sistemi |
| A.5.24–28 Gestione degli incidenti | L'indagine forense richiede una timeline coerente su tutti i sistemi |
| A.5.28 Raccolta delle prove | L'accuratezza dell'orologio costituisce il fondamento dell'ammissibilità legale delle prove digitali |
| A.8.20 Sicurezza della rete | I dispositivi di rete devono essere sincronizzati per la correlazione degli eventi di sicurezza |

**Politiche interne correlate**:

- Politica di registrazione degli eventi (A.8.15)
- Politica delle attività di monitoraggio (A.8.16)
- Politica di gestione degli incidenti
- Politica di sicurezza della rete

---

# Politica di sincronizzazione dell'orologio

## Scopo

Lo scopo di questa politica è garantire che gli orologi di tutti i sistemi di elaborazione delle informazioni rilevanti all'interno dell'organizzazione siano sincronizzati con un'unica fonte di riferimento temporale coerente. I timestamp accurati e coerenti sono essenziali per la correlazione dei log, le indagini sugli incidenti, le prove forensi, la conformità normativa e l'integrità dei sistemi distribuiti.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 mantenendo l'integrità dei dati tramite la timestamping verificabile. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applica anche il GDPR Art. 32 (sicurezza del trattamento). Gli obblighi di registrazione dell'OPDo Art. 4 per il trattamento di dati personali degni di particolare protezione richiedono timestamp accurati per garantire l'integrità e la tracciabilità dei log.

## Ambito di applicazione

Questa politica si applica a tutti i sistemi che generano dati di log o registrazioni sensibili al tempo, inclusi:

- Server e workstation (fisiche e virtuali).
- Infrastruttura di rete (router, switch, firewall, load balancer, controller wireless).
- Dispositivi di sicurezza (IDS/IPS, agenti EDR, sistemi di controllo degli accessi).
- Servizi cloud e piattaforme SaaS.
- Server di database e server applicativi.
- Sistemi di sicurezza fisica (CCTV, lettori di badge) laddove integrati con la registrazione IT.
- Dispositivi IoT e di tecnologia operativa (OT) nell'ambito del SGSI.

Tutti i dipendenti e gli utenti terzi responsabili dell'amministrazione o della distribuzione dei sistemi sono responsabili di garantire la sincronizzazione temporale sui sistemi da loro gestiti.

## Principio

Tutti gli orologi DEVONO sincronizzarsi con un'unica fonte di riferimento temporale approvata dall'organizzazione. I dati temporali DEVONO essere protetti dalla modifica non autorizzata. I timestamp DEVONO essere registrati in un formato coerente per consentire una correlazione affidabile tra sistemi, posizioni e provider di servizi.

---

## Fonti di tempo autorevoli

### Riferimento primario

L'organizzazione DEVE designare una fonte di tempo autorevole primaria:

| Attributo | Requisito |
|-----------|-----------|
| **Fonte primaria** | Server NTP di METAS (Istituto federale svizzero di metrologia): `ntp.metas.ch`, `ntp11.metas.ch`, `ntp12.metas.ch`, `ntp13.metas.ch` — Strato 1, tracciabile a UTC(CH) |
| **Fonte secondaria** | Pool NTP svizzero: `0.ch.pool.ntp.org`, `1.ch.pool.ntp.org`, `2.ch.pool.ntp.org`, `3.ch.pool.ntp.org` |
| **Fonti minime** | Ogni server di tempo interno DEVE sincronizzarsi con almeno **due** fonti esterne indipendenti (per CIS Control 8.4) |
| **Tracciabilità** | La fonte primaria DEVE essere tracciabile a un istituto nazionale di metrologia o a un segnale temporale GPS/GNSS |

### Architettura di tempo interna

L'organizzazione DEVE distribuire server NTP interni in un'architettura a livelli:

| Livello | Ruolo | Configurazione |
|---------|-------|----------------|
| **Strato 2 interno** | Server NTP interni primari sincronizzati direttamente con fonti esterne di Strato 1 (METAS) | Minimo 2 server per ridondanza; separati geograficamente ove fattibile |
| **Strato 3 interno** | Server a livello di sito o di reparto (opzionale per ambienti più grandi) | Sincronizzazione con lo Strato 2 interno; servono i client locali |
| **Client** | Tutti gli endpoint, i server applicativi, i dispositivi di rete | Sincronizzazione con lo Strato 2 o Strato 3 interno tramite NTP |

Per le organizzazioni di piccole dimensioni: il domain controller primario o un server interno designato può fungere da unico server NTP interno, sincronizzato con almeno due fonti esterne.

Laddove l'organizzazione utilizzi oscillatori disciplinati GPS (GPSDO) per l'indipendenza di Strato 0/1 (ad es. reti air-gapped), questi DEVONO essere documentati e mantenuti secondo le specifiche del produttore.

---

## Protocollo di sincronizzazione

### Configurazione NTP

Il Network Time Protocol (NTP) DEVE essere utilizzato per la sincronizzazione temporale su tutti i sistemi aziendali standard.

| Requisito | Specifica |
|-----------|-----------|
| **Protocollo** | NTPv4 (RFC 5905) come minimo |
| **Sicurezza** | Network Time Security (NTS, RFC 8915) DEVE essere abilitato laddove supportato sia dal client che dal server. Laddove NTS non sia supportato, la comunicazione NTP DEVE essere limitata ai server approvati tramite regole del firewall o liste di controllo degli accessi. |
| **Autenticazione** | L'autenticazione NTP con chiave simmetrica o NTS DEVE essere utilizzata tra server interni e fonti esterne |
| **Intervallo di polling** | Predefinito (64-1024 secondi); intervalli più brevi per i sistemi critici se necessario |
| **Regole firewall** | NTP in uscita (UDP 123) consentito solo verso fonti esterne approvate; NTP in entrata limitato ai server interni |

### Precision Time Protocol (PTP)

Laddove sia richiesta un'accuratezza sub-microsecondo (ad es. trading finanziario, controllo industriale, elaborazione di dati ad alta frequenza), DEVE essere distribuito l'IEEE 1588 Precision Time Protocol (PTPv2):

- Sono necessari switch di rete PTP-aware (boundary o transparent clock).
- DEVE essere distribuito un orologio grandmaster PTP (disciplinato GPS).
- PTP è un'aggiunta a — non una sostituzione di — NTP nell'ambito dell'azienda generale.

L'applicabilità del PTP viene determinata durante la progettazione del sistema e documentata nell'architettura del sistema.

---

## Formato dei timestamp

### Formato standard

Tutti i sistemi DEVONO registrare i timestamp in uno dei seguenti formati:

| Formato | Esempio | Caso d'uso |
|---------|---------|------------|
| **UTC** (preferito) | `2026-02-07T14:30:00Z` | Server, database, dispositivi di rete, SIEM, tutta l'infrastruttura |
| **Ora locale con offset UTC** | `2026-02-07T15:30:00+01:00` | Log applicativi, rapporti rivolti all'utente (laddove l'UTC non sia praticabile) |

**Regole obbligatorie:**

- Il formato ISO 8601 / RFC 3339 DEVE essere utilizzato per tutti i timestamp generati automaticamente.
- **UTC è lo standard** per tutta l'infrastruttura, la registrazione e i sistemi di sicurezza.
- L'ora locale con offset UTC esplicito è consentita solo a livello applicativo/di presentazione.
- L'ora locale **senza** offset UTC (ad es. `15:30:00 CET`) **non è accettabile** — le abbreviazioni dei fusi orari sono ambigue (le transizioni CET/CEST creano ore duplicate).
- Le abbreviazioni dei fusi orari con nome NON devono essere utilizzate nei timestamp dei log.

### Ora legale

UTC elimina l'ambiguità dell'ora legale (DST). Durante la transizione autunnale (CEST → CET), l'ora 02:00–03:00 si ripete. I sistemi che utilizzano l'ora locale senza offset non riescono a distinguere tra le due occorrenze. I sistemi che registrano in UTC non sono interessati.

Tutti i sistemi DEVONO utilizzare UTC o offset esplicito per prevenire l'ambiguità dei timestamp legata all'ora legale.

---

## Tolleranze di deriva dell'orologio

### Offset massimo accettabile

I sistemi DEVONO mantenere l'accuratezza dell'orologio entro le seguenti tolleranze:

| Livello del sistema | Offset massimo | Soglia di monitoraggio | Azione |
|---------------------|---------------|------------------------|--------|
| **Critico** (autenticazione, SIEM, finanziario, database) | < 1 ms | Avviso a > 1 ms | Investigare e risincronizzare immediatamente |
| **Aziendale standard** (server, dispositivi di rete) | < 50 ms | Avviso a > 50 ms | Investigare entro 4 ore |
| **Generale** (workstation, stampanti) | < 500 ms | Avviso a > 500 ms | Risincronizzare al prossimo ciclo di polling |
| **Allarme** (qualsiasi sistema) | > 128 ms | Soglia NTP step | Il client NTP eseguirà un aggiustamento a gradino (jump); registrare l'evento |
| **Panico** (qualsiasi sistema) | > 1000 secondi | Soglia di panico NTP | Il daemon NTP termina; richiesto intervento manuale |

### Monitoraggio della deriva

La deriva dell'orologio DEVE essere monitorata continuamente utilizzando strumenti di monitoraggio del sistema (ad es. Prometheus, Nagios, CloudWatch o equivalente):

- Le metriche di offset NTP, jitter e strato DEVONO essere raccolte da tutti i sistemi monitorati.
- Avviso in caso di offset superiore alla soglia del livello del sistema.
- Avviso in caso di cambiamenti di strato (ad es. un server che scende dallo Strato 2 allo Strato 16 indica la perdita della sincronizzazione upstream).
- Gli avvisi di deriva dell'orologio DEVONO essere inoltrati alla piattaforma di monitoraggio centralizzata.
- Analisi delle tendenze mensile della deriva dell'orologio nell'intera infrastruttura.

---

## Sincronizzazione temporale dei servizi cloud

### Fonti di tempo specifiche per provider

Laddove i sistemi vengano eseguiti in ambienti cloud, DEVE essere utilizzato il servizio di sincronizzazione temporale del provider:

| Provider | Servizio di tempo | Accesso | Note |
|----------|------------------|---------|------|
| **AWS** | Amazon Time Sync Service | `169.254.169.123` (link-local) | Orologi atomici + GPS per regione; preconfigurato su Amazon Linux; utilizza la distribuzione graduale dei secondi intercalari |
| **Azure** | VMICTimeSync (PTP hypervisor) | Dispositivo PTP all'interno della VM | Tempo fornito tramite hypervisor, non NTP di rete; chrony raccomandato |
| **GCP** | Google Public NTP | `time.google.com` | Preconfigurato su Compute Engine; utilizza la distribuzione graduale dei secondi intercalari (24 ore) |

### Requisiti per ambienti ibridi

Laddove l'organizzazione operi in ambienti on-premises e cloud:

- **Non mescolare fonti di tempo con e senza distribuzione graduale** all'interno dello stesso ambiente. I provider cloud (AWS, GCP) distribuiscono i secondi intercalari nell'arco di 24 ore; le fonti NTP tradizionali (METAS, pool.ntp.org) utilizzano l'aggiustamento a gradino. La combinazione crea discrepanze temporali durante gli eventi dei secondi intercalari.
- Documentare quale fonte di tempo utilizza ogni ambiente.
- Per le architetture ibride, designare se il tempo cloud o on-premises è autorevole, e configurare di conseguenza la direzione di sincronizzazione.
- Monitorare la deriva dell'orologio delle VM cloud — la pianificazione della virtualizzazione e la migrazione live possono introdurre sfasamenti temporali.

---

## Gestione dei secondi intercalari

Un secondo intercalare è un aggiustamento di un secondo (positivo o negativo) applicato all'UTC per mantenerlo allineato con la rotazione della Terra. Sono stati aggiunti 27 secondi intercalari dal 1972; la pratica dovrebbe essere abolita entro il 2035 (per la Risoluzione CGPM 4, novembre 2022).

### Strategia organizzativa

L'organizzazione DEVE adottare un'**unica strategia coerente per la gestione dei secondi intercalari** in tutti gli ambienti:

| Strategia | Descrizione | Quando utilizzare |
|-----------|-------------|-------------------|
| **Aggiustamento a gradino** (tradizionale) | Inserire o rimuovere un secondo a 23:59:60 UTC | Sistemi on-premises che utilizzano fonti NTP tradizionali (METAS, pool.ntp.org) |
| **Distribuzione graduale** | Distribuire il secondo extra nell'arco di 24 ore regolando leggermente la frequenza dell'orologio | Ambienti cloud che utilizzano servizi di tempo del provider (AWS, GCP) |

**Regole:**

- Non mescolare mai fonti di tempo con aggiustamento a gradino e fonti con distribuzione graduale nello stesso ambiente.
- Documentare la strategia scelta e comunicarla agli amministratori di sistema.
- Testare la gestione dei secondi intercalari in anticipo rispetto a qualsiasi evento di secondo intercalare programmato.
- Monitorare i sistemi per 24 ore dopo un evento di secondo intercalare.
- Una volta aboliti i secondi intercalari (previsto entro il 2035), aggiornare le configurazioni per rimuovere la logica di gestione dei secondi intercalari.

---

## Sicurezza NTP

### Protezione contro gli attacchi basati sul tempo

L'infrastruttura NTP DEVE essere protetta contro spoofing, replay e attacchi denial-of-service:

| Minaccia | Mitigazione |
|----------|-------------|
| **Spoofing NTP** | Abilitare NTS (RFC 8915) o l'autenticazione NTP con chiave simmetrica; limitare le fonti NTP ai server approvati |
| **Attacchi di replay** | NTS fornisce protezione contro il replay tramite cookie univoci per ogni scambio |
| **Amplificazione DDoS** | Disabilitare la monlist NTP (`restrict ... noquery`); limitare l'accesso NTP ai client interni |
| **Modifica non autorizzata** | Configurazioni del server NTP protette da controlli di accesso; le modifiche richiedono l'approvazione della gestione delle modifiche |
| **Punto singolo di guasto** | Minimo due fonti esterne indipendenti; ridondanza del server interno |

### Protezione della configurazione

- I file di configurazione NTP DEVONO essere protetti dalla modifica non autorizzata (permessi dei file, monitoraggio dell'integrità).
- Le modifiche alla configurazione NTP DEVONO seguire il processo di gestione delle modifiche.
- Lo stato del servizio NTP DEVE essere monitorato; il guasto del servizio DEVE generare un avviso.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione dell'architettura di sincronizzazione temporale; punto di escalation per i problemi di deriva persistenti |
| **IT Operations / Team della piattaforma** | Distribuzione e manutenzione del server NTP; configurazione del monitoraggio; configurazione della fonte di tempo cloud; gestione degli eventi dei secondi intercalari |
| **Amministratori di sistema** | Garantire che NTP sia configurato sui sistemi gestiti; segnalare i guasti di sincronizzazione; verificare le impostazioni temporali durante la distribuzione del sistema |
| **Amministratori di rete** | Configurazione NTP sui dispositivi di rete; regole firewall per il traffico NTP; distribuzione di NTS sui dispositivi supportati |
| **Cloud Engineer** | Configurazione della fonte di tempo specifica per il cloud; documentazione della fonte di tempo per l'architettura ibrida; monitoraggio della deriva delle VM cloud |

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| N. | Prova | Responsabile | Frequenza |
|----|-------|--------------|-----------|
| 1 | **Documentazione dell'architettura NTP** (server interni, fonti esterne, gerarchia degli strati, impostazioni di protocollo/sicurezza) | IT Operations | *Documentata; revisionata annualmente e in seguito a modifiche dell'architettura* |
| 2 | **Metrica della conformità NTP** (percentuale di sistemi nell'ambito con configurazione NTP verificata e fonti di tempo approvate) | IT Operations | *Trimestrale; obiettivo: 100% dei sistemi critici, ≥95% di tutti nell'ambito* |
| 3 | **Registrazioni del monitoraggio della deriva dell'orologio** (metriche di offset, jitter e strato; avvisi generati e risolti) | IT Operations | *Monitoraggio continuo; rapporto mensile delle tendenze; avvisi conservati 12 mesi* |
| 4 | **Documentazione della fonte di tempo cloud** (servizio del provider, configurazione, strategia di distribuzione graduale, considerazioni ibride) | Cloud Engineer | *Documentata per ogni servizio cloud; revisionata annualmente* |
| 5 | **Configurazione della sicurezza NTP** (stato NTS, autenticazione, regole firewall, restrizioni di accesso) | IT Operations / Rete | *Configurazione documentata; revisionata annualmente* |
| 6 | **Conformità al formato dei timestamp** (voci di log campione da 5+ sistemi che dimostrano il formato UTC o con offset) | Sicurezza delle informazioni | *Verificato annualmente durante l'audit* |
| 7 | **Documentazione della strategia per i secondi intercalari** (approccio scelto, registrazioni dei test, monitoraggio durante gli eventi) | IT Operations | *Documentata; testata prima di ogni evento di secondo intercalare (o annualmente se nessuno è programmato)* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso audit della configurazione NTP, revisioni del monitoraggio della deriva, verifica del formato dei timestamp, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere riportate al team di revisione della direzione.

I sistemi che non possono supportare NTP (ad es. dispositivi OT legacy, ambienti di test isolati) DEVONO essere documentati con giustificazione, e DEVE essere eseguita una verifica manuale del tempo a una frequenza definita.

## Non conformità

Un dipendente che risulti aver violato questa politica può essere soggetto ad azioni disciplinari, fino al licenziamento.

## Miglioramento continuo

Questa politica viene rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti agli standard NTP, la disponibilità delle fonti di tempo, i servizi di tempo dei provider cloud, gli sviluppi della politica sui secondi intercalari e le lessons learned dagli incidenti di deriva dell'orologio o dalle indagini forensi.

---

# Aree dello standard ISO 27001 trattate

Politica di sincronizzazione dell'orologio — Mapping dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| | 5.37 Procedure operative documentate |
| | 6.3 Sensibilizzazione, educazione e formazione sulla sicurezza delle informazioni |
| | **8.17 Sincronizzazione dell'orologio** |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|-----------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative (integrità dei dati) |
| OPDo svizzero | Art. 4 — Obblighi di registrazione (timestamp accurati richiesti) |
| GDPR UE (se applicabile) | Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Annex A Controllo 8.17 |
| ISO/IEC 27002:2022 | Sezione 8.17 — Indicazioni di implementazione |
| NIST SP 800-53 Rev 5 | AU-8 (Time Stamps), AU-8(1) (Synchronisation with Authoritative Source), SC-45 (System Time Synchronisation) |
| NIST CSF 2.0 | PR.PS-04 (Log records generated for continuous monitoring) |
| CIS Controls v8 | Controllo 8.4 (Standardise Time Synchronisation) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
