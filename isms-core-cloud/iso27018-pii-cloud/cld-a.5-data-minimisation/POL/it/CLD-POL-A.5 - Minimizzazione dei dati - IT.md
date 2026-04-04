<!-- ISMS-CORE:POLICY:CLD-POL-A.5-IT:cloud:POL:a.5 -->
**CLD-POL-A.5 — Minimizzazione dei dati**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Responsabile del trattamento di DCP nel cloud pubblico — Minimizzazione dei dati |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-POL-A.5 |
| **Autore del documento** | RSSI / Responsabile Sicurezza Cloud |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Data da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Cloud** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI / Responsabile Sicurezza Cloud | Politica iniziale per l'implementazione di ISO/IEC 27018:2025 Ed. 3 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti dell'architettura del servizio)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :
- Principale: RSSI / Responsabile Sicurezza Cloud
- Secondaria: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati** :
- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- ISMS-POL-A.5.34 (Privacy e protezione dei DCP)
- ISMS-POL-A.8.10 (Eliminazione delle informazioni)
- CLD-POL-A.4 (Limitazione della raccolta)
- CLD-POL-A.6 (Limitazione dell'utilizzo, della conservazione e della divulgazione)
- CLD-POL-A.11 (Sicurezza delle informazioni — supporti portatili, cifratura, smaltimento)
- ISO/IEC 27018:2025 Annex A, Sezione A.5 e Controllo A.5.1
- ISO/IEC 27701:2025 Controlli A.2.4.2 (responsabile del trattamento — file temporanei) e A.2.4.3 (responsabile del trattamento — restituzione, trasferimento o smaltimento dei DCP)
- RGPD Articolo 5(1)(c) (minimizzazione dei dati); Articolo 5(1)(e) (limitazione della conservazione)
- LPD svizzera Articolo 6(2) (proporzionalità)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] come responsabile del trattamento di DCP nel cloud pubblico in materia di minimizzazione dei dati — specificamente la cancellazione sicura dei file temporanei contenenti DCP generati durante le operazioni di trattamento cloud — conformemente a ISO/IEC 27018:2025 Annex A, Sezione A.5 e Controllo A.5.1.

**Perimetro** : Tutti gli archivi effimeri, temporanei e di lavoro creati dai servizi cloud di [Organizzazione] durante il trattamento dei DCP, inclusi cache, memoria virtuale, file di lavoro e log.

**Motivazione dei controlli combinati** : La Sezione A.5 stabilisce il principio che l'identificazione completa è inutile laddove il trattamento possa essere effettuato su dati anonimizzati o pseudonimizzati. Il Controllo A.5.1 affronta il rischio specifico del cloud che i DCP persistano nell'archiviazione temporanea dopo il completamento del trattamento — un rischio particolarmente significativo negli ambienti cloud multi-tenant in cui l'archiviazione può essere riallocata.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27018:2025

**Sezione A.5 — Minimizzazione dei dati (principio)**

La Sezione A.5 stabilisce il principio che l'identificazione completa degli interessati dovrebbe essere evitata laddove il trattamento possa essere effettuato utilizzando dati anonimizzati, pseudonimizzati o aggregati, e che le tecniche utilizzate dovrebbero essere documentate e riesaminate.

**Controllo A.5.1 — Cancellazione sicura dei file temporanei**

Il Controllo A.5.1 affronta il rischio specifico che i DCP persistano nell'archiviazione temporanea dopo il completamento del trattamento. Richiede che il responsabile del trattamento implementi la cancellazione sicura dei file temporanei — inclusi cache, memoria virtuale, file di lavoro e log — utilizzando metodi che impediscano il recupero, coprendo sia l'archiviazione persistente che quella effimera.

## Cosa questa politica NON copre

- I periodi di conservazione per i principali archivi di DCP a riposo — trattati in CLD-POL-A.6
- Lo smaltimento sicuro dei supporti di archiviazione fisici — trattato in CLD-POL-A.11

## Quadro normativo

**Livello 1: Conformità obbligatoria** (per PRIV-POL-00):

- **RGPD UE** : Articolo 5(1)(c) (minimizzazione dei dati); Articolo 5(1)(e) (limitazione della conservazione — non più a lungo del necessario); Articolo 32(1)(a) (pseudonimizzazione e cifratura come misure di sicurezza appropriate)
- **LPD svizzera** : Articolo 6(2) (proporzionalità); Articolo 9 (obblighi del responsabile del trattamento — misure tecniche appropriate)
- **ISO/IEC 27018:2025** : Controlli A.5 (principio) e A.5.1

---

# Disposizioni della politica: Principio di minimizzazione dei dati (A.5)

## Pseudonimizzazione e anonimizzazione

Laddove la finalità del trattamento possa essere soddisfatta senza identificazione diretta degli interessati, [Organizzazione] DEVE implementare la pseudonimizzazione o l'anonimizzazione come parte della progettazione del servizio. In particolare:

- Le funzioni di analisi e reporting DEVONO utilizzare dati pseudonimizzati o aggregati dove tecnicamente fattibile
- I sistemi di log e telemetria DEVONO minimizzare la cattura di DCP al minimo operativamente necessario
- Gli ambienti di test e sviluppo DEVONO utilizzare dati sintetici o dataset anonimizzati ovunque possibile

Le tecniche di anonimizzazione applicate ai DCP del titolare del trattamento DEVONO essere documentate e sottoposte alla revisione del RPD prima dell'implementazione per confermare che il risultato è genuinamente e irreversibilmente anonimizzato. La valutazione del RPD DEVE essere condotta in conformità con gli orientamenti applicabili delle autorità di controllo (incluso il Parere 05/2014 dell'EDPB sulle tecniche di anonimizzazione, o il suo successore).

---

# Disposizioni della politica: Cancellazione sicura dei file temporanei (A.5.1)

## Tipi di file temporanei nel perimetro

I servizi cloud di [Organizzazione] generano le seguenti categorie di archiviazione temporanea che possono contenere DCP e sono soggette a questa politica:

- **File di cache** : Dati archiviati temporaneamente dai livelli applicativi durante il trattamento attivo
- **File di swap / file di paginazione** : Overflow di memoria del sistema operativo archiviato su disco
- **File di lavoro / spazio di lavoro temporaneo** : File di trattamento intermedi creati durante operazioni batch o in streaming
- **File di log delle applicazioni** : Log del servizio generati durante il trattamento che possono catturare DCP nei payload, nelle tracce di errori o negli output di debug
- **Archiviazione di calcolo effimera** : Archiviazione a blocchi collegata alle istanze di calcolo durante l'esecuzione del job

## Requisito di cancellazione

[Organizzazione] DEVE implementare la cancellazione sicura di tutte le categorie di archiviazione temporanea elencate sopra una volta completata l'operazione di trattamento per cui sono state create. La cancellazione DEVE essere eseguita utilizzando metodi che impediscano il recupero dei dati, in conformità con NIST SP 800-88 (Guidelines for Media Sanitization) o equivalente, inclusi:

- La cancellazione crittografica (eliminazione della chiave di cifratura per i volumi cifrati) — efficace solo laddove i dati siano stati cifrati con una chiave dedicata non replicata o sottoposta a backup al di fuori del perimetro di eliminazione
- La sovrascrittura multipassaggio per l'archiviazione persistente laddove la cancellazione crittografica non sia applicabile
- L'azzeramento sicuro della memoria per i DCP in memoria dopo l'utilizzo

Il meccanismo di cancellazione DEVE essere automatizzato all'interno della pipeline del servizio ove tecnicamente fattibile per eliminare il ricorso a procedure manuali.

## Minimizzazione dei log

I log applicativi e infrastrutturali che catturano DCP DEVONO essere soggetti a:

- **Cattura minima** : Le configurazioni dei log DEVONO essere riesaminate per garantire che i DCP nei payload, nelle intestazioni o nei parametri siano mascherati o esclusi a meno che non siano operativamente essenziali
- **Limiti di conservazione** : I log contenenti DCP DEVONO essere conservati per il periodo operativo richiesto, e in ogni caso non oltre 30 giorni salvo giustificazione operativa documentata — o il massimo definito negli accordi di servizio con il titolare del trattamento dei DCP se inferiore
- **Eliminazione automatizzata** : Le politiche di conservazione dei log DEVONO essere implementate come regole di eliminazione automatizzata, non come processi manuali

## Isolamento dell'archiviazione multi-tenant

Negli ambienti multi-tenant, [Organizzazione] DEVE garantire che l'archiviazione temporanea allocata al trattamento di un titolare del trattamento dei DCP sia:

- Isolata dagli altri tenant durante il trattamento attivo
- Cancellata in modo sicuro prima della riallocazione a qualsiasi altro tenant o carico di lavoro
- Verificabile tramite audit — gli eventi di riallocazione DEVONO essere registrati nei log e disponibili per l'ispezione

Questo aspetto è trattato in dettaglio in CLD-POL-A.11 (§11.13 — Accesso ai dati sullo spazio di archiviazione precedentemente utilizzato). I test di isolamento multi-tenant DEVONO essere eseguiti al minimo annualmente e dopo qualsiasi modifica materiale all'infrastruttura di archiviazione.

## Copertura delle procedure

Le procedure di cancellazione dei file temporanei DEVONO coprire esplicitamente:

- Sia l'archiviazione persistente (SSD, HDD, NVMe) che l'archiviazione effimera (archiviazione di istanza, effimera di container)
- Tutti i livelli di calcolo: bare metal, macchina virtuale, container, funzione serverless (le considerazioni di cancellazione specifiche per il serverless, inclusi l'archiviazione /tmp e la memorizzazione nella cache dei layer, sono trattate nelle procedure di cancellazione a livello di servizio)
- Tutte le regioni geografiche in cui [Organizzazione] gestisce l'infrastruttura cloud

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI / Responsabile Sicurezza Cloud** | Proprietario degli standard di cancellazione dei file temporanei; esamina l'implementazione annualmente; escalate le lacune irrisolte al RPD e alla Direzione generale |
| **Ingegneria Cloud** | Implementa meccanismi di cancellazione automatizzati nelle pipeline dei servizi; garantisce che le configurazioni di minimizzazione dei log siano applicate; testa l'efficacia della cancellazione |
| **Responsabile della Protezione dei Dati (RPD)** | Esamina le valutazioni di anonimizzazione/pseudonimizzazione; conferma che le configurazioni di minimizzazione dei log siano adeguate; fornisce consulenza sugli obblighi di limitazione della conservazione |
| **Operazioni di sicurezza** | Monitora gli eventi anomali di remanenza dei dati; risponde agli incidenti in cui i DCP potrebbero essere persistiti nell'archiviazione temporanea |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Procedure di cancellazione dei file temporanei | Procedure documentate per servizio e tipo di archiviazione, con metodo di cancellazione specificato | In corso + versioni precedenti per 3 anni |
| Registrazioni di configurazione della cancellazione automatizzata | Registrazioni di configurazione tecnica che dimostrano l'implementazione della cancellazione automatizzata | In corso + 3 anni |
| Registrazioni di configurazione della minimizzazione dei log | Configurazioni dei log documentate che confermano la minimizzazione della cattura dei DCP | In corso + versioni precedenti per 3 anni |
| Registrazioni di test di isolamento multi-tenant | Risultati dei test periodici che confermano l'assenza di remanenza di dati tra tenant | 3 anni |
| Revisioni di anonimizzazione del RPD | Valutazioni RPD firmate delle tecniche di anonimizzazione applicate ai DCP del titolare del trattamento | Durata dell'utilizzo + 3 anni |

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-POL-A.5 devono aspettarsi di trovare:

- Procedure di cancellazione dei file temporanei documentate che coprono tutti i tipi di archiviazione e i livelli di calcolo pertinenti
- Prove tecniche che la cancellazione sia automatizzata nelle pipeline dei servizi piuttosto che dipendente da passaggi manuali
- Configurazioni di minimizzazione dei log riesaminate e confermate come escludenti i DCP non necessari
- Risultati dei test che confermano che l'archiviazione riallocata tra tenant non contenga DCP residui del trattamento del tenant precedente

---

<!-- QA_VERIFIED: 2026-04-04 -->
