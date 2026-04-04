<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.10-IT:framework:POL:a.7.10 -->
**ISMS-POL-A.7.10 — Supporti di archiviazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Supporti di archiviazione |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.7.10 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Responsabile delle Operazioni IT
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.12-13 (Classificazione ed etichettatura delle informazioni)
- ISMS-POL-A.7.6-7-14 (Aree sicure e gestione dei supporti)
- ISMS-POL-A.8.10 (Cancellazione delle informazioni)
- ISMS-IMP-A.7.10.1–3-UG/TG (Suite di orientamento all'implementazione)
- ISO/IEC 27001:2022 Controllo A.7.10

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione dei supporti di archiviazione durante il loro ciclo di vita, dall'acquisizione attraverso l'uso, il trasporto e lo smaltimento.

**Perimetro**: Si applica a tutti i supporti di archiviazione utilizzati da [Organizzazione], inclusi i supporti rimovibili, lo storage fisso, lo storage cloud e i documenti cartacei contenenti informazioni sensibili.

**Allineamento normativo**: nLPD svizzera (Art. 8, Art. 6); ISO/IEC 27001:2022; RGPD dell'UE, PCI DSS v4.0.1, FINMA, DORA (applicabilità condizionale).

---

# Allineamento sul controllo e perimetro

**ISO/IEC 27001:2022 Allegato A.7.10 — Supporti di archiviazione**

> *I supporti di archiviazione devono essere gestiti durante il loro ciclo di vita di acquisizione, utilizzo, trasporto e smaltimento in conformità con il sistema di classificazione e i requisiti di gestione dell'organizzazione.*

**Obiettivi del controllo**: Garantire solo la divulgazione, modifica, rimozione o distruzione autorizzata delle informazioni sui supporti di archiviazione; proteggere i supporti durante il loro ciclo di vita; mantenere la responsabilità per i supporti contenenti informazioni sensibili; prevenire la perdita di dati attraverso una gestione impropria.

## Perimetro

**Questa politica si applica a**: Supporti digitali (HDD/SSD, chiavette USB, schede SD, supporti ottici, nastri di backup, storage di rete); documenti fisici (carta, microfilm, microfiches); storage cloud (gestito per A.5.19-23); fasi del ciclo di vita (acquisizione, utilizzo, trasporto, archiviazione, smaltimento); tutto il personale che gestisce supporti di archiviazione.

---

# Enunciati di politica

## Dichiarazione di politica generale

Tutti i supporti di archiviazione contenenti informazioni dell'organizzazione DEVONO essere gestiti per questa politica; l'uso di supporti rimovibili DEVE essere limitato e controllato; i supporti contenenti informazioni sensibili DEVONO essere protetti durante il trasporto; lo smaltimento DEVE garantire che i dati non possano essere recuperati.

## Gestione dei supporti rimovibili

### Autorizzazione e registrazione

**Requisiti di autorizzazione**:

- L'uso di supporti rimovibili DEVE essere autorizzato dalla direzione diretta
- I supporti personali NON DEVONO essere utilizzati per i dati organizzativi
- I supporti rilasciati dall'organizzazione DEVONO essere registrati nel sistema di gestione degli asset

**Supporti approvati**:

- Solo supporti rimovibili approvati dall'organizzazione e cifrati DEVONO essere utilizzati
- I dispositivi USB con cifratura hardware DEVONO essere utilizzati per i dati RISERVATI
- I supporti DEVONO essere approvvigionati attraverso fornitori approvati
- I supporti BYOD SONO VIETATI per i dati RISERVATI/INTERNI

### Requisiti d'uso

- Il trasferimento di dati RISERVATI su supporti rimovibili richiede l'approvazione della direzione
- I dati DEVONO essere cifrati prima del trasferimento su supporti rimovibili
- I log di trasferimento DEVONO essere mantenuti per i dati RISERVATI
- I dati DEVONO essere rimossi dai supporti quando non più necessari

### Inventario dei supporti

**Registrazione**: Tutti i supporti rimovibili DEVONO essere registrati nell'inventario degli asset. La registrazione DEVE includere: tipo di supporto, capacità, utente assegnato, scopo, livello di classificazione.

**Riconciliazione trimestrale**: Il 100% dei supporti rimovibili registrati DEVE essere riconciliato con i registri degli asset; la riconciliazione DEVE verificare la posizione fisica, lo stato di cifratura e l'utente assegnato; le discrepanze DEVONO essere escalate entro 1 giorno lavorativo per le procedure di risposta agli incidenti.

## Trasporto dei supporti di archiviazione

### Trasporto sicuro

**Requisiti del corriere**: I supporti RISERVATI DEVONO utilizzare solo corrieri sicuri approvati; la catena di custodia DEVE essere documentata; il destinatario DEVE verificare e riconoscere la ricezione; DEVE essere utilizzato un imballaggio a prova di manomissione.

**Trasporto personale**: I supporti DEVONO essere trasportati nel bagaglio a mano durante i viaggi (non in stiva); i supporti DEVONO essere cifrati; i supporti NON DEVONO essere lasciati incustoditi durante il trasporto.

## Requisiti di archiviazione

### Archiviazione fisica

| Classificazione | Requisito di archiviazione | Cifratura | Controllo degli accessi |
|----------------|---------------------------|-----------|------------------------|
| **RISERVATO** | Cassaforte/armadietto chiuso a chiave | Obbligatoria (per ISMS-POL-A.8.24) | Solo persone nominate |
| **INTERNO** | Armadietto chiuso a chiave | Raccomandata (per ISMS-POL-A.8.24) | Personale autorizzato |
| **PUBBLICO** | Archiviazione standard | Opzionale | Accesso generale |

**Periodi di conservazione**: I supporti DEVONO essere conservati per i requisiti di conservazione dei dati definiti nel Calendario di conservazione (ISMS-REG-CONSERVAZIONE); i supporti DEVONO essere smaltiti alla scadenza del periodo di conservazione.

**Implementazione della cifratura**: I meccanismi di cifratura specifici della piattaforma (BitLocker/FileVault per endpoint, LUKS per Linux, S3 SSE-KMS per lo storage cloud) sono definiti in ISMS-IMP-A.7.10.2 e DEVONO essere conformi agli standard crittografici in ISMS-POL-A.8.24.

## Smaltimento dei supporti di archiviazione

### Requisiti di smaltimento

Lo smaltimento e la sanificazione DEVONO garantire che le informazioni non possano essere recuperate, utilizzando metodi di sanificazione/distruzione approvati dall'organizzazione appropriati al tipo di supporto e al livello di classificazione.

**Risultati richiesti dello smaltimento per classificazione**:

| Classificazione | Risultato richiesto | Verifica |
|----------------|---------------------|----------|
| **RISERVATO** | Irrecuperabile con qualsiasi mezzo | Certificato di distruzione del fornitore approvato |
| **INTERNO** | Irrecuperabile senza apparecchiature specializzate | Verifica della cancellazione sicura documentata |
| **PUBBLICO** | Eliminazione standard accettabile | Documentazione dello smaltimento |

**Metodi approvati**: I metodi specifici di sanificazione e distruzione per tipo di supporto (HDD, SSD, nastro, ottico, dispositivi mobili) sono definiti in ISMS-IMP-A.7.10.3, allineati ai principi NIST SP 800-88 Rev. 2.

### Riutilizzo interno

Prima che il supporto sia riutilizzato all'interno dell'organizzazione: tutti i dati sensibili DEVONO essere cancellati in modo sicuro; la cancellazione DEVE essere verificata; il supporto DEVE essere ispezionato per l'integrità fisica; i registri degli asset DEVONO essere aggiornati.

### Smaltimento esterno

I supporti smaltiti esternamente DEVONO: avere tutti i dati cancellati in modo sicuro o essere fisicamente distrutti; essere smaltiti attraverso fornitori di smaltimento approvati; avere lo smaltimento documentato con certificati conservati; non essere mai venduti o donati con dati recuperabili.

## Documenti cartacei e supporti fisici

**Distruzione sicura**: I documenti cartacei RISERVATI DEVONO essere tritati trasversalmente (a frammenti incrociati); i documenti cartacei INTERNI DEVONO essere tritati; la tritatura DEVE essere eseguita in sede o da appaltatori approvati.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per i supporti di archiviazione |
|-------|------------------------------------------------|
| **Direzione generale** | Approvare la politica, allocare risorse per la sicurezza dei supporti |
| **RSSI** | Proprietà della politica, standard, supervisione della conformità |
| **Operazioni IT** | Approvvigionamento dei supporti, dispiegamento della cifratura, esecuzione dello smaltimento |
| **Responsabili diretti** | Autorizzare l'uso dei supporti, garantire la conformità del team |
| **Gestione degli asset** | Inventario, monitoraggio e gestione del ciclo di vita dei supporti |
| **Tutto il personale** | Gestire i supporti per politica, segnalare immediatamente le perdite |

---

# Metriche di governance

- Supporti registrati con cifratura (obiettivo: 100%)
- Perdite di supporti (obiettivo: 0)
- Smaltimento con certificati (obiettivo: 100% per RISERVATO)
- Supporti in ritardo di restituzione (obiettivo: <3)
- Completamento dell'audit dei supporti (obiettivo: 100%)

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Supporto di archiviazione** | Qualsiasi dispositivo o materiale in grado di memorizzare dati, in formato digitale e fisico |
| **Supporto rimovibile** | Dispositivi di archiviazione portatili che possono essere rimossi dai sistemi (chiavette USB, unità esterne, dischi ottici) |
| **Sovrascrittura sicura** | Processo di scrittura di pattern sui dati archiviati per prevenirne il recupero |
| **Smagnetizzazione** | Utilizzo di potenti campi magnetici per cancellare dati dai supporti di archiviazione magnetici |
| **Catena di custodia** | Registro cronologico documentato della gestione, trasferimento e archiviazione dei supporti |
| **Certificato di distruzione** | Conferma scritta da un fornitore approvato che il supporto è stato distrutto |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Responsabile delle Operazioni IT** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la gestione dei supporti di archiviazione. Le procedure di attuazione sono documentate in ISMS-IMP-A.7.10 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
