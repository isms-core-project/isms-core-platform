<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.30-8.13-14-IT:framework:POL:a.5.30-8.13-14 -->
**ISMS-POL-A.5.30-8.13-14 — Quadro di continuità operativa e ripristino di emergenza**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Quadro di continuità operativa e ripristino di emergenza |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.30-8.13-14 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica iniziale per la prima certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore dei Sistemi Informativi (DSI)
- Tecnico: Responsabile delle Operazioni IT / Coordinatore CO/RE
- Conformità: Responsabile Legale/Conformità
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-IMP-A.5.30-8.13-14-S1-UG/TG (Processo BIA e RPO/RTO)
- ISMS-IMP-A.5.30-8.13-14-S2-UG/TG (Implementazione del backup)
- ISMS-IMP-A.5.30-8.13-14-S3-UG/TG (Implementazione della ridondanza)
- ISMS-IMP-A.5.30-8.13-14-S4-UG/TG (Processo di test di ripristino)
- ISO/IEC 27001:2022 Controlli A.8.13, A.8.14, A.5.30
- ISMS-POL-A.5.19-23 (Fornitori/Servizi cloud)
- ISMS-POL-A.5.24 (Gestione degli incidenti)
- ISMS-POL-A.8.6 (Gestione della capacità)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di Continuità Operativa e Ripristino di Emergenza (CO/RE) al fine di garantire la resilienza organizzativa attraverso capacità sistematiche di backup, ridondanza e continuità delle TIC, conformemente ai Controlli A.8.13, A.8.14 e A.5.30 della norma ISO/IEC 27001:2022.

**Perimetro**: Questa politica si applica a tutti gli asset informativi, i sistemi TIC e i processi aziendali indipendentemente dal modello di dispiegamento (on-premise, cloud, ibrido) o dalla piattaforma tecnologica.

**Approccio a controlli combinati**: Questi tre controlli sono attuati come un quadro CO/RE unificato perché operano come un ecosistema integrato: il backup fornisce la capacità di recupero dei dati (A.8.13), la ridondanza fornisce la capacità di disponibilità del sistema (A.8.14) e la prontezza CO delle TIC fornisce la preparazione complessiva e la governance (A.5.30). Nonostante l'implementazione unificata, ciascun controllo mantiene requisiti distinti ai fini della Dichiarazione di Applicabilità (DdA).

**Principio critico — «Il ripristino non testato equivale ad assenza di ripristino»**: Questo quadro impone test regolari di tutte le capacità di ripristino. Solo il test di ripristino convalida la capacità di recupero.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; DORA (immutabilità, backup fuori sede, ridondanza geografica); NIS2 (conformità alla regola 3-2-1, notifica di incidenti in 24 ore); FINMA; PCI DSS v4.0.1.

---

# Allineamento sui controlli e perimetro

## Controlli ISO/IEC 27001:2022 A.8.13, A.8.14, A.5.30

**A.8.13 — Backup delle informazioni**

> *Copie di backup di informazioni, software e sistemi devono essere mantenute e testate regolarmente conformemente alla politica specifica per argomento concordata.*

**Obiettivo del controllo**: Garantire che informazioni, software e sistemi possano essere recuperati in caso di perdita, danni, corruzione o indisponibilità.

**A.8.14 — Ridondanza delle strutture di elaborazione delle informazioni**

> *Le strutture di elaborazione delle informazioni devono essere implementate con ridondanza sufficiente a soddisfare i requisiti di disponibilità.*

**Obiettivo del controllo**: Garantire la disponibilità delle strutture di elaborazione delle informazioni conformemente ai requisiti organizzativi.

**A.5.30 — Prontezza delle TIC per la continuità operativa**

> *La prontezza delle TIC deve essere pianificata, implementata, mantenuta e testata in base agli obiettivi di continuità operativa e ai requisiti di continuità delle TIC.*

**Obiettivo del controllo**: Garantire che i sistemi TIC siano pronti a supportare la continuità operativa in caso di interruzioni.

## Perimetro

**Asset informativi** (A.8.13): Dati aziendali critici; configurazioni di sistema e infrastruttura-come-codice; software applicativo; configurazioni di sicurezza; tutte le classificazioni dei dati.

**Strutture di elaborazione delle informazioni** (A.8.14): Server on-premise (fisici e virtuali); infrastruttura cloud (IaaS, PaaS, SaaS); ambienti ibridi; infrastruttura di rete; sistemi di storage; sistemi endpoint critici.

**Processi aziendali** (A.5.30): Tutti i processi aziendali dipendenti dalle TIC identificati attraverso la BIA; funzioni aziendali critiche; servizi di terze parti e dipendenze.

**Scenari di direzione del ripristino**: On-premise su on-premise; on-premise su cloud; cloud su on-premise; cloud su cloud alternativo; failover geografico.

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Requisito | Applicabilità |
|-----------|-----------|---------------|
| **nLPD svizzera** | Misure tecniche e organizzative appropriate inclusa la protezione della disponibilità (Art. 8) | Tutto il trattamento di dati personali di [Organizzazione] |
| **RGPD dell'UE** | Capacità di ripristinare la disponibilità e l'accesso ai dati personali in modo tempestivo (Art. 32(1)(c)) | Elaborazione di dati personali UE |
| **ISO/IEC 27001:2022** | Controlli A.8.13, A.8.14, A.5.30 | Ambito di certificazione |

**Livello 2 — Applicabilità condizionale**:

| Normativa | Requisito | Condizione scatenante |
|-----------|-----------|----------------------|
| **DORA** | Politica di continuità operativa delle TIC, politiche di backup, piani di ripristino di emergenza, test (Artt. 11-12) | Operazioni di servizi finanziari UE |
| **NIS2** | Continuità operativa e misure di gestione delle crisi, gestione dei backup (Art. 21) | Designazione come entità essenziale/importante |
| **FINMA** | Gestione della continuità operativa per istituti finanziari | Operazioni di servizi finanziari svizzeri |
| **PCI DSS v4.0.1** | Backup e conservazione dei dati (Requisito 12.10), test di backup/ripristino (Requisito 12.10.7) | Elaborazione di dati di carte di pagamento |

**Requisiti specifici DORA**: Per le entità finanziarie UE soggette a DORA: copie di backup immutabili (Art. 12(4)); archiviazione di backup fuori sede a sufficiente distanza geografica (Art. 12(4)); test annuale del ripristino dei backup (Art. 12(6)); test CO/RE integrato con test di penetrazione basati su minacce (Art. 26).

**Requisiti specifici NIS2**: Implementazione della regola di backup 3-2-1; cifratura dei backup in transito e a riposo; capacità di segnalazione degli incidenti in 24 ore.

---

# Quadro dei requisiti

## Requisiti di backup delle informazioni (A.8.13)

### Ambito del backup

**Sistemi e dati che richiedono il backup**:

| Categoria | Requisito di backup | Motivazione |
|-----------|--------------------|----|
| **Dati aziendali critici** | Backup obbligatorio | La perdita di dati inciderebbe gravemente sulle operazioni |
| **Sistemi di produzione** | Backup obbligatorio (dati + configurazione) | Richiesto per la continuità operativa |
| **Configurazioni infrastruttura critica** | Backup obbligatorio | Richiesto per il ripristino dell'infrastruttura |
| **Dati aziendali importanti** | Backup obbligatorio | La perdita di dati inciderebbe moderatamente sulle operazioni |
| **Sistemi di sviluppo/test** | Backup basato sul rischio | Backup se il costo di ricreazione supera il costo del backup |
| **Dati effimeri** | Nessun backup richiesto | Dati deliberatamente temporanei (cache, log con conservazione) |
| **Sistemi non critici** | Backup basato sul rischio | Backup se il tempo di ripristino non è accettabile |

### Frequenza e RPO del backup per classificazione del sistema

| Livello sistema | Frequenza backup | RPO obiettivo | Motivazione |
|----------------|-----------------|--------------|-------------|
| **Livello 1 (Critico)** | Continuo o orario | ≤ 1 ora | Perdita minima di dati accettabile |
| **Livello 2 (Alto)** | Ogni 4-6 ore | ≤ 6 ore | Perdita limitata di dati accettabile |
| **Livello 3 (Medio)** | Giornaliero | ≤ 24 ore | Perdita di dati giornaliera accettabile |
| **Livello 4 (Basso)** | Settimanale o alla modifica | ≤ 7 giorni | Perdita di dati settimanale accettabile |

### Conservazione dei backup

I backup DEVONO essere conservati conformemente ai seguenti periodi minimi:

| Tipo di backup | Conservazione minima | Considerazioni normative |
|---------------|---------------------|--------------------------|
| **Backup giornalieri** | 30 giorni | La maggior parte delle normative richiede una capacità di ripristino di 30 giorni |
| **Backup settimanali** | 90 giorni | Necessità di conformità e audit trimestrali |
| **Backup mensili** | 12 mesi | Verifica annuale della conformità e analisi storica |
| **Backup annuali** | 7 anni (o per normativa) | Documenti finanziari, conformità fiscale, blocchi legali |

### Regola di backup 3-2-1-1-0 (buona pratica del settore)

| Elemento | Requisito | Motivazione |
|----------|-----------|-------------|
| **3 copie** | Originale + 2 copie di backup | Protezione contro il punto unico di guasto |
| **2 tipi di supporto** | Tecnologie di archiviazione diverse | Protezione contro guasti specifici del supporto |
| **1 copia fuori sede** | Ubicazione geograficamente separata | Protezione contro disastri del sito |
| **1 immutabile/air-gapped** | Write-once-read-many o offline | Protezione contro ransomware e minacce interne |
| **0 errori** | Integrità del backup verificata | Solo i backup verificati sono affidabili |

**Implementazione per i sistemi critici** (Livello 1): I sistemi critici DEVONO implementare la regola 3-2-1-1-0.

**Implementazione per sistemi alti/medi** (Livelli 2-3): I sistemi alti e medi DOVREBBERO implementare come minimo la regola 3-2-1.

### Requisiti fuori sede e di immutabilità

**Requisiti di backup fuori sede**:

| Livello sistema | Requisito fuori sede | Separazione geografica | Frequenza di replica |
|----------------|---------------------|----------------------|---------------------|
| **Livello 1 (Critico)** | Obbligatorio | Min. 100 km o regione diversa | Continua o oraria |
| **Livello 2 (Alto)** | Obbligatorio | Min. 50 km o zona di disponibilità diversa | Giornaliera |
| **Livello 3 (Medio)** | Raccomandato | Ubicazione fisica diversa | Settimanale |
| **Livello 4 (Basso)** | Basato sul rischio | Archiviazione cloud accettabile | Alla modifica |

**Requisiti di backup immutabile**:

**Sistemi critici** (Livello 1): DEVONO implementare backup immutabili utilizzando tecnologia WORM (Write-Once-Read-Many); il periodo di immutabilità DEVE allinearsi alla politica di conservazione (minimo 30 giorni); le tecnologie comprendono: archiviazione a oggetti con object lock (AWS S3 Object Lock, Azure Immutable Blob), nastri WORM, appliance di backup immutabili dedicati.

**Backup offline/air-gapped**: Per i sistemi critici, almeno una copia di backup deve essere fisicamente disconnessa dalla rete, archiviata in un luogo fuori sede sicuro e ruotata periodicamente.

### Requisiti di test dei backup

| Livello sistema | Frequenza test di ripristino | Ambito del test |
|----------------|------------------------------|-----------------|
| **Livello 1** | Trimestrale come minimo | Ripristino completo del sistema in ambiente alternativo |
| **Livello 2** | Semestrale come minimo | Set di dati rappresentativi, sistema completo annualmente |
| **Livello 3** | Annuale come minimo | Verifica del ripristino campione |
| **Livello 4** | In caso di modifica significativa | Ripristino campione o accettazione del rischio |

**Principio critico**: I parametri di successo del backup (backup completato con successo) NON convalidano la capacità di ripristino. Solo il test di ripristino convalida la capacità di recupero.

**Documentazione del test**: Ogni test di ripristino DEVE essere documentato includendo: metadati del test; stato pre-test; esecuzione del test; validazione dei risultati; metriche (durata effettiva, dati recuperati, varianza RTO); artefatti di prova; log dei problemi; firma del Coordinatore CO/RE.

### Monitoraggio del backup

| Elemento di monitoraggio | Requisito | Soglia di avviso |
|--------------------------|-----------|-----------------|
| Successo/Fallimento del backup | Monitoraggio in tempo reale | Avviso immediato in caso di fallimento |
| Durata del backup | Analisi delle tendenze | Avviso se la durata supera la finestra |
| Dimensione del backup | Analisi delle tendenze | Avviso in caso di crescita/riduzione inaspettata |
| Capacità del repository | Monitoraggio della capacità | Avviso all'80% di utilizzo |
| Conformità alla conservazione | Validazione automatizzata | Avviso sulle violazioni della politica di conservazione |

---

## Ridondanza delle strutture di elaborazione delle informazioni (A.8.14)

### Requisiti di ridondanza per criticità del sistema

| Criticità sistema | RTO massimo | Requisito minimo di ridondanza |
|------------------|-------------|-------------------------------|
| **Critico** | ≤ 4 ore | Attivo-attivo o attivo-passivo con failover automatizzato |
| **Alto** | ≤ 24 ore | Standby caldo o standby freddo documentato con ripristino testato |
| **Medio** | ≤ 72 ore | Standby freddo o procedure di ricostruzione documentate |
| **Basso** | > 72 ore | Ripristino basato su backup accettabile |

**Architetture di ridondanza**:

| Architettura | Descrizione | RTO tipico | Caso d'uso |
|-------------|-------------|-----------|-----------|
| **Attivo-attivo** | Più sistemi servono il traffico simultaneamente | Minuti | Sistemi critici che richiedono disponibilità continua |
| **Attivo-passivo** | Sistema standby pronto per failover immediato | Minuti-ore | Sistemi critici con breve interruzione accettabile |
| **Standby caldo** | Ambiente standby parzialmente provisionato | Ore | Sistemi ad alta priorità con RTO moderato |
| **Standby freddo** | Infrastruttura disponibile ma non provisionata | Giorni | Sistemi importanti con RTO più lungo accettabile |

### Analisi del Punto Unico di Guasto (SPUF)

I proprietari dei sistemi DEVONO condurre l'analisi SPUF per i sistemi Critici e Alti al fine di identificare i componenti il cui guasto causerebbe il completo fallimento del sistema.

**Priorità di rimedio SPUF**:

| Livello di rischio SPUF | Requisito di rimedio | Tempistica |
|------------------------|---------------------|-----------|
| **SPUF sistema critico** | Rimedio obbligatorio | 90 giorni o accettazione del rischio |
| **SPUF sistema alto** | Rimedio raccomandato | 180 giorni o accettazione del rischio |
| **SPUF sistema medio** | Decisione basata sul rischio | Valutazione del rischio richiesta |

### Requisiti di failover e switchover

**Test dei meccanismi di failover**:

| Livello sistema | Frequenza del test di failover | Ambito del test |
|----------------|-------------------------------|-----------------|
| **Livello 1 (Critico)** | Trimestrale | Failover completo in ambiente di produzione o simil-produzione |
| **Livello 2 (Alto)** | Semestrale | Test di failover documentato o esercizio tabletop |
| **Livello 3 (Medio)** | Annuale | Esercizio tabletop o validazione della procedura documentata |

### Ridondanza geografica

**Opzioni di ridondanza geografica**:

| Livello di ridondanza | Separazione geografica | Protezione contro | Esempio |
|----------------------|----------------------|------------------|---------|
| **Multi-server** | Stesso data center | Guasto hardware del server | Server in cluster |
| **Multi-rack** | Stesso data center | Guasto alimentazione/raffreddamento nel rack | Server in rack diversi |
| **Multi-zona** | Stessa regione, zone di disponibilità diverse | Interruzione a livello di data center | AWS Multi-AZ, Azure Availability Zones |
| **Multi-regione** | Regioni geografiche diverse | Disastro regionale | AWS us-east-1 + us-west-2 |
| **Multi-cloud** | Provider cloud diversi | Interruzione del provider cloud | AWS + Azure |

---

## Prontezza delle TIC per la continuità operativa (A.5.30)

### Analisi dell'impatto aziendale (BIA)

La BIA DEVE essere condotta per: identificare i processi aziendali critici; determinare le dipendenze TIC per ciascun processo aziendale; quantificare l'impatto delle interruzioni TIC; stabilire il Tempo massimo tollerabile di inattività (MTI), l'Obiettivo di tempo di ripristino (RTO) e l'Obiettivo di punto di ripristino (RPO).

**Frequenza BIA**: Inizialmente durante l'implementazione del SGSI; annualmente come minimo; in caso di cambiamenti aziendali significativi; dopo incidenti gravi.

**Documentazione BIA**: I risultati della BIA DEVONO essere documentati in: Registro della criticità dei sistemi (inventario principale con classificazione Livello 1-4, MTI/RTO/RPO documentati, giustificazione aziendale e firma del proprietario); Mappe delle dipendenze dei processi aziendali; Report di valutazione BIA con approvazioni.

### Strategia di continuità delle TIC

**Strategie di ripristino per livello di sistema**:

| Livello sistema | Strategia di ripristino | Approccio infrastrutturale |
|----------------|------------------------|--------------------------|
| **Livello 1 (Critico)** | Attivo-attivo o standby caldo | Infrastruttura ridondante, failover automatizzato |
| **Livello 2 (Alto)** | Standby caldo o ricostruzione rapida | Risorse pre-provisionate, procedure documentate |
| **Livello 3 (Medio)** | Standby freddo o ripristino da backup | Infrastruttura disponibile, ripristino da backup |
| **Livello 4 (Basso)** | Ricostruzione o ripristino rinviato | Procedure di ricostruzione standard |

### Piani di ripristino delle TIC

I piani di continuità delle TIC DEVONO documentare: criteri di attivazione; ruoli e responsabilità; contatti di emergenza; procedure di ripristino; procedure di comunicazione; priorità di ripristino; procedure di validazione.

**Manutenzione dei piani**: Revisione annuale; aggiornamento dopo gli esercizi di test; aggiornamento dopo gli incidenti gravi; aggiornamento quando i sistemi o l'infrastruttura cambiano significativamente; controllo delle versioni con tracciamento delle modifiche.

### Programma di test CO/RE

**Tipi di test**:

| Tipo di test | Descrizione | Frequenza | Ambito |
|-------------|-------------|-----------|--------|
| **Esercizio tabletop** | Revisione basata sulla discussione | Annuale | Tutti i processi critici |
| **Test dei componenti** | Test del ripristino del singolo sistema | Trimestrale | Sistemi critici |
| **Test DR completo** | Failover completo al sito DR | Annuale | Processi critici end-to-end |
| **Test a sorpresa** | Test non annunciato (opzionale) | Come necessario | Sistemi selezionati |

**Calendario dei test per criticità**:

| Criticità | Requisito di test annuale |
|-----------|--------------------------|
| **Critico** | Test DR completo + 2 test dei componenti |
| **Alto** | Test DR completo o 2 test dei componenti |
| **Medio** | Test dei componenti o esercizio tabletop |
| **Basso** | Esercizio tabletop |

**Conformità DORA**: Le entità finanziarie soggette a DORA devono testare i dispositivi CO almeno annualmente (Art. 11(9)); testare il backup e il ripristino TIC almeno annualmente (Art. 12(6)); integrare i test CO/RE con i test di penetrazione basati su minacce (Art. 26).

---

# Governance e conformità

## Ruoli e responsabilità

| Ruolo | Responsabilità CO/RE |
|-------|---------------------|
| **Amministratore Delegato (AD)** | Responsabilità ultima per la continuità operativa; approvare la strategia CO/RE e il budget; dichiarare i disastri che richiedono l'attivazione del piano |
| **RSSI** | Proprietario della politica CO/RE; approvare i requisiti e l'accettazione del rischio; garantire risorse adeguate; riferire lo stato CO/RE alla direzione generale |
| **DSI** | Responsabilità operativa per la continuità TIC; allocare risorse per l'implementazione del backup/ridondanza |
| **Coordinatore CO/RE** | Gestione quotidiana del programma CO/RE; coordinare il processo BIA; mantenere i piani di ripristino; pianificare e facilitare i test |
| **Amministratore del backup** | Implementare e gestire le soluzioni di backup; configurare i calendari e la conservazione; monitorare i job e risolvere i problemi |
| **Amministratori di sistema/cloud** | Implementare la ridondanza per i sistemi assegnati; configurare i meccanismi di failover; partecipare ai test CO/RE |
| **Proprietari dei sistemi/applicazioni** | Definire i requisiti RTO/RPO; fornire input al processo BIA; approvare le priorità di ripristino dei sistemi; partecipare ai test |
| **Proprietari dei processi aziendali** | Definire i requisiti di continuità operativa; identificare processi e dipendenze critici; approvare RTO/RPO per i processi aziendali |
| **Team di sicurezza** | Monitorare la sicurezza dell'infrastruttura di backup e DR; verificare l'implementazione della cifratura; partecipare ai test CO/RE |
| **Responsabile Legale/Conformità** | Determinare i requisiti normativi CO/RE; garantire la conformità a DORA, NIS2, ecc. |

## Indicatori di prestazione chiave (KPI)

| KPI | Obiettivo | Misurazione |
|-----|-----------|-------------|
| Copertura del backup (% sistemi critici con backup) | 100% | Mensile |
| Tasso di successo del backup | ≥ 99% | Mensile |
| Conformità al test del backup | ≥ 95% | Trimestrale |
| Conformità al RPO (% sistemi che soddisfano il RPO) | 100% critici, ≥ 95% alti | Trimestrale |
| Conformità all'RTO (% sistemi che soddisfano l'RTO nei test) | 100% critici, ≥ 95% alti | Trimestrale |
| Tasso di successo del test DR | ≥ 90% | Annuale |
| Rimedio SPUF (% SPUF critici mitigati) | ≥ 90% | Trimestrale |

## Gestione delle eccezioni

Le eccezioni ai requisiti CO/RE richiedono: presentazione della richiesta di eccezione con giustificazione aziendale; valutazione del rischio da parte del Coordinatore CO/RE + Team di sicurezza; approvazione basata sul livello di rischio (Coordinatore CO/RE → RSSI → RSSI+DSI → Direzione generale); documentazione nel registro delle eccezioni con revisione periodica; tracciamento del rimedio se l'eccezione è temporanea.

## Reportistica

**Report mensili** (Coordinatore CO/RE → RSSI): Tasso di successo del backup per criticità; backup falliti che richiedono indagine; stato della disponibilità della ridondanza; calendario dei test imminenti; problemi aperti e stato del rimedio.

**Report trimestrali** (Coordinatore CO/RE → RSSI + DSI): KPI del programma CO/RE; riepilogo della conformità RPO/RTO; risultati dei test e insegnamenti tratti; analisi delle lacune con prioritizzazione.

**Report annuali** (RSSI → Direzione generale): Valutazione della maturità CO/RE; incidenti gravi ed efficacia del ripristino; conformità ai requisiti normativi; necessità di investimento e raccomandazioni strategiche.

---

# Implementazione e riferimenti

## Integrazione con il SGSI

**Controlli correlati**:

| Controllo | Punto di integrazione |
|-----------|----------------------|
| **A.5.9** (Inventario degli asset) | I sistemi che richiedono backup/ridondanza identificati attraverso l'inventario degli asset |
| **A.8.9** (Gestione della configurazione) | Le configurazioni di sistema vengono sottoposte a backup; IaC abilita la ricostruzione rapida |
| **A.8.15** (Registrazione) | Le operazioni di backup registrate; gli eventi di failover registrati; le operazioni di ripristino registrate |
| **A.8.16** (Monitoraggio) | Il monitoraggio del backup integrato con la piattaforma di monitoraggio organizzativa |

## Suite di risorse di implementazione

| Documento | Scopo | Ambito |
|---------|-------|--------|
| **ISMS-IMP-A.5.30-8.13-14-S1** | Processo BIA e RPO/RTO | Metodologia BIA, classificazione della criticità dei sistemi, determinazione RPO/RTO |
| **ISMS-IMP-A.5.30-8.13-14-S2** | Implementazione del backup | Selezione della soluzione di backup, architettura, pianificazione, conservazione, monitoraggio, procedure di ripristino |
| **ISMS-IMP-A.5.30-8.13-14-S3** | Implementazione della ridondanza | Identificazione SPUF, architettura di ridondanza, meccanismi di failover, ridondanza geografica |
| **ISMS-IMP-A.5.30-8.13-14-S4** | Processo di test di ripristino | Test di ripristino del backup, test di failover, test degli scenari CO/RE, raccolta delle prove |

**Strumenti di valutazione** (classeur Excel): Classeur 1: Inventario e valutazione della copertura del backup; Classeur 2: Analisi della ridondanza; Classeur 3: Matrice di conformità RPO/RTO; Classeur 4: Risultati dei test CO/RE.

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Backup** | Copia di dati, software o configurazione di sistema creata per scopi di ripristino |
| **Ridondanza** | Implementazione di strutture di elaborazione delle informazioni duplicate o alternative per garantire la disponibilità |
| **Continuità operativa (CO)** | Capacità organizzativa di continuare le operazioni aziendali durante e dopo eventi perturbativi |
| **Ripristino di emergenza (RE)** | Processo di ripristino dei sistemi TIC e dei dati dopo una perturbazione |
| **RPO** | Obiettivo di punto di ripristino — quantità massima accettabile di perdita di dati misurata nel tempo |
| **RTO** | Obiettivo di tempo di ripristino — tempo massimo accettabile per ripristinare un sistema dopo una perturbazione |
| **MTI** | Tempo massimo tollerabile di inattività — tempo assoluto massimo in cui un processo aziendale può essere non disponibile |
| **BIA** | Analisi dell'impatto aziendale — processo sistematico per identificare e valutare gli effetti potenziali delle interruzioni |
| **SPUF** | Punto unico di guasto — componente il cui guasto causerebbe il completo fallimento del sistema o del processo |
| **Failover** | Processo di passaggio automatico o manuale a un sistema ridondante o standby |
| **Sito caldo** | Struttura di backup completamente operativa con replica di dati che consente il failover immediato |
| **Sito tiepido** | Struttura di backup con apparecchiature e connettività ma che richiede il ripristino dei dati |
| **Sito freddo** | Struttura di backup con infrastruttura di base ma che richiede l'installazione delle apparecchiature e il ripristino dei dati |
| **Backup immutabile** | Backup che non può essere modificato o eliminato dopo la creazione (WORM) |
| **Backup air-gapped** | Backup fisicamente disconnesso dalla rete |
| **Regola 3-2-1** | Buona pratica del settore: 3 copie dei dati, su 2 tipi di supporto diversi, con 1 copia fuori sede |
| **Regola 3-2-1-1-0** | Regola di backup avanzata che aggiunge 1 copia immutabile/air-gapped e 0 errori nel test di verifica del backup |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data] |
| **Coordinatore CO/RE** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti CO/RE. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.30-8.13-14-S1–S4 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
