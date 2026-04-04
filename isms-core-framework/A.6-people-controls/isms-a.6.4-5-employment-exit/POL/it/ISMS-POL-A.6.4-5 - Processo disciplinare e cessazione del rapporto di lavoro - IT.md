<!-- ISMS-CORE:POLICY:ISMS-POL-A.6.4-5-IT:framework:POL:a.6.4-5 -->
**ISMS-POL-A.6.4-5 — Processo disciplinare e cessazione del rapporto di lavoro**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Processo disciplinare e cessazione del rapporto di lavoro |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.6.4-5 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Direttore delle Risorse Umane (DRH) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Direttore delle Risorse Umane (DRH)
- Secondario: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Legale: Consulente legale
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.1-2-6.1-2 (Impiego sicuro e ruoli)
- ISMS-POL-A.5.15-16-18 (Gestione delle identità e degli accessi)
- ISMS-POL-A.6.6 (Accordi di riservatezza e non divulgazione)
- ISMS-IMP-A.6.4-5.S1-UG/TG (Valutazione del processo disciplinare)
- ISMS-IMP-A.6.4-5.S2-UG/TG (Valutazione della cessazione del rapporto di lavoro)
- ISMS-IMP-A.6.4-5.S3-UG/TG (Obblighi post-impiego)
- ISO/IEC 27001:2022 Controlli A.6.4, A.6.5

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione delle violazioni delle politiche di sicurezza attraverso processi disciplinari e per garantire la cessazione sicura del rapporto di lavoro, inclusa la protezione delle informazioni e degli asset organizzativi.

**Perimetro**: Tutti i dipendenti, appaltatori e lavoratori temporanei durante il processo disciplinare e il ciclo di vita della cessazione del rapporto di lavoro, indipendentemente dal motivo della cessazione.

**Allineamento normativo**: Diritto del lavoro svizzero (CO svizzero); nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; FINMA (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sui controlli e perimetro

**ISO/IEC 27001:2022 Allegato A.6.4 — Processo disciplinare**

> *Un processo disciplinare deve essere formalizzato e comunicato per adottare misure nei confronti del personale che ha commesso una violazione della politica di sicurezza delle informazioni.*

**ISO/IEC 27001:2022 Allegato A.6.5 — Responsabilità dopo la cessazione o il cambiamento del rapporto di lavoro**

> *Le responsabilità e i doveri di sicurezza delle informazioni che rimangono validi dopo la cessazione o il cambiamento del rapporto di lavoro devono essere definiti, applicati e comunicati al personale rilevante e alle altre parti interessate.*

---

# Enunciati di politica

## Processo disciplinare (A.6.4)

### Quadro disciplinare

[Organizzazione] DEVE mantenere un processo disciplinare formale per le violazioni delle politiche di sicurezza delle informazioni basato sui seguenti principi: applicazione equa e coerente; proporzionalità alla gravità della violazione; allineamento con il diritto del lavoro applicabile; documentato con prove appropriate; progressivo dove le circostanze lo consentono; risposta tempestiva alle violazioni.

### Categorie di violazioni

| Categoria | Esempi | Risposta tipica |
|-----------|--------|----------------|
| **Minore/Inavvertita** | Violazione accidentale della politica, prima violazione minore | Avviso verbale, formazione aggiuntiva |
| **Moderata** | Violazioni minori ripetute, gestione negligente dei dati | Avviso scritto, formazione correttiva |
| **Grave** | Violazione deliberata della politica, esposizione significativa dei dati | Avviso finale, sospensione, cessazione |
| **Grave violazione** | Furto doloso di dati, sabotaggio, attività criminale | Licenziamento immediato, azione legale |

### Procedure disciplinari

**Indagine**: Incidente segnalato a HR e al Team di sicurezza; valutazione preliminare della gravità; raccolta e preservazione delle prove; indagine (interviste, revisione dei log, analisi forense se necessario); risultati documentati.

**Decisione e azione**: Gravità della violazione determinata; fattori attenuanti/aggravanti considerati; azione disciplinare appropriata selezionata; decisione comunicata al dipendente; azione implementata; monitoraggio di follow-up dove appropriato.

**Giusto processo**: Dipendente informato delle accuse; opportunità di risposta fornita; diritto alla rappresentanza per il diritto del lavoro; processo di appello disponibile; documentazione mantenuta in modo riservato.

### Coinvolgimento del Team di sicurezza

Il Team di sicurezza DEVE essere coinvolto nelle questioni disciplinari quando: la violazione riguarda una violazione della politica di sicurezza delle informazioni; è richiesta un'indagine tecnica (analisi dei log, analisi forense); si raccomanda la revoca dell'accesso o il monitoraggio; vi è il potenziale di un rischio di sicurezza continuativo; potrebbe essere richiesta la notifica legale o normativa.

### Escalation e notifica

| Gravità della violazione | Notifica interna | Notifica esterna |
|--------------------------|-----------------|-----------------|
| Minore | Responsabile di linea, HR | Nessuna |
| Moderata | HR, RSSI | Tipicamente nessuna |
| Grave | HR, RSSI, Legale | Regolatori se richiesto |
| Grave violazione | HR, RSSI, Legale, Direzione generale | Polizia, regolatori se richiesto |

## Cessazione del rapporto di lavoro (A.6.5)

### Requisiti del processo di uscita

[Organizzazione] DEVE implementare processi di uscita sicuri per tutte le cessazioni del rapporto di lavoro:

**Tempistiche di revoca dell'accesso**:

| Tipo di cessazione | Tempistica di revoca dell'accesso |
|-------------------|----------------------------------|
| **Licenziamento immediato** (grave violazione) | Entro 1 ora dalla decisione |
| **Cessazione per causa** | Stesso giorno lavorativo |
| **Dimissioni volontarie** | Ultimo giorno lavorativo, fine del turno |
| **Pensionamento** | Ultimo giorno lavorativo |
| **Fine contratto** | Data di fine contratto |
| **Cambio di ruolo (trasferimento)** | Accesso al ruolo precedente entro 2 giorni lavorativi |

**SLA di revoca dell'accesso**: Il timer di revoca dell'accesso parte quando la decisione di cessazione è registrata nel sistema HR/ticketing autorizzato. Le cessazioni urgenti sono supportate tramite il processo di offboarding in reperibilità definito in ISMS-IMP-A.6.4-5. Se la revoca completa non può essere completata entro lo SLA, vengono applicati immediatamente controlli compensativi (es. disabilitazione IdP, disabilitazione VPN, disabilitazione del badge) e viene registrata una non conformità/eccezione con rimedio monitorato fino alla chiusura.

**Perimetro della revoca dell'accesso**:

| Tipo di accesso | Requisito di revoca |
|----------------|---------------------|
| **Accesso fisico** | Badge disabilitato, chiavi restituite, dati biometrici rimossi |
| **Accesso logico** | Tutti gli account disabilitati (AD, email, applicazioni, VPN, cloud) |
| **Accesso remoto** | VPN, desktop remoto, gestione dispositivi mobili |
| **Accesso a terze parti** | Portali dei fornitori, sistemi dei partner |
| **Accesso delegato** | Accesso alle caselle postali, account condivisi, chiavi API |

### Restituzione degli asset

[Organizzazione] DEVE recuperare tutti gli asset organizzativi: asset fisici (laptop, computer, monitor, dispositivi mobili, supporti di archiviazione, badge di accesso, chiavi, token, documenti, carte di credito aziendali); asset logici (rimozione del software su dispositivi personali se BYOD, dati sui dispositivi personali, credenziali di accesso).

### Obblighi post-impiego

[Organizzazione] DEVE comunicare e applicare gli obblighi continuativi:

**Riservatezza**: Gli obblighi NDA continuano per i termini dell'accordo (per ISMS-POL-A.6.6); i segreti commerciali rimangono protetti a tempo indeterminato; le informazioni dei clienti rimangono riservate.

**Restituzione/Distruzione delle informazioni**: Tutte le informazioni organizzative DEVONO essere restituite o certificate come distrutte; le copie personali sono vietate; la verifica della restituzione o cancellazione delle informazioni organizzative da ubicazioni non organizzative è eseguita tramite procedure legittime e documentate approvate da HR e Legale, limitate a quanto necessario e proporzionato.

### Colloquio di uscita

[Organizzazione] DEVE condurre colloqui di uscita con focus sulla sicurezza: promemoria degli obblighi continuativi di riservatezza; riconoscimento dei termini NDA; conferma della restituzione/cancellazione dei dati; identificazione di eventuali preoccupazioni o questioni in sospeso; firma della documentazione finale.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità disciplinari e di uscita |
|-------|----------------------------------------|
| **DRH/HR** | Proprietà del processo disciplinare, coordinamento del processo di uscita, conformità al diritto del lavoro |
| **RSSI** | Valutazione delle violazioni di sicurezza, verifica della revoca dell'accesso, supporto forense |
| **Consulente legale** | Conformità al diritto del lavoro, supporto al ricorso disciplinare, applicazione NDA |
| **Responsabili di linea** | Avviare le questioni disciplinari, verifica della restituzione degli asset, coordinamento dell'handover |
| **Operazioni IT** | Esecuzione della revoca dell'accesso, recupero degli asset, verifica tecnica |
| **Team IAM** | Disabilitazione degli account, audit degli accessi, esecuzione del processo di uscita |

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Audit di conformità al processo di uscita | Trimestrale | Audit interno | Campione di uscite completate |
| Tempestività della revoca dell'accesso | Mensile | Team IAM | Metriche da cessazione a disabilitazione |
| Tasso di recupero degli asset | Trimestrale | Operazioni IT | Documenti di restituzione degli asset |
| Revisione del processo disciplinare | Annuale | HR | Documentazione dei casi, risultati |

**Metriche di governance**: Accesso revocato entro lo SLA (obiettivo: 100%); asset recuperati entro 5 giorni lavorativi (obiettivo: >95%); colloqui di uscita completati (obiettivo: 100%); account orfani dai dipendenti usciti (obiettivo: 0).

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Azione disciplinare** | Risposta formale a comportamento scorretti o violazioni della politica del dipendente |
| **Grave violazione** | Violazione grave che giustifica il licenziamento immediato senza preavviso |
| **Processo di uscita** | Procedure per l'offboarding del personale in partenza |
| **Congedo retribuito** | Periodo di preavviso in cui il dipendente è retribuito ma non lavora |
| **Colloquio di uscita** | Riunione per documentare la partenza e confermare gli obblighi |
| **Account orfano** | Account utente rimasto dopo la cessazione del rapporto di lavoro |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Direttore delle Risorse Umane (DRH)** | [Nome] | [Data da definire] |
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Consulente legale** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per i processi disciplinari e la cessazione del rapporto di lavoro. Le procedure di attuazione sono documentate in ISMS-IMP-A.6.4-5 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
