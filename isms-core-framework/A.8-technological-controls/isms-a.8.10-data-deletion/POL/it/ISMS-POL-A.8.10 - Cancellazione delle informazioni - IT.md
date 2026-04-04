<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.10-IT:framework:POL:a.8.10 -->
**ISMS-POL-A.8.10 — Politica di cancellazione delle informazioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di cancellazione delle informazioni |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.10 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → RPD → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.10.1–4-UG/TG; ISMS-FORM-A.8.10-RGPD; ISMS-REF-A.8.10; ISO/IEC 27001:2022 Controllo A.8.10.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli di cancellazione delle informazioni per garantire la cancellazione sistematica delle informazioni quando non più necessarie, conformemente al Controllo A.8.10 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti gli asset informativi indipendentemente dall'ubicazione di archiviazione (on-premise, cloud, terze parti), tutti i tipi di supporti di archiviazione, tutti i sistemi e le applicazioni (inclusa l'infrastruttura di backup), e tutte le categorie di dati durante il loro ciclo di vita.

**Allineamento normativo**: nLPD svizzera (minimizzazione dei dati e diritto alla cancellazione); RGPD dell'UE Art. 17 (Diritto alla cancellazione) dove si elaborano dati personali UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.10

> *Le informazioni archiviate in sistemi informativi, dispositivi o in qualsiasi altro supporto di archiviazione devono essere cancellate quando non più necessarie.*

**Obiettivo del controllo**: Stabilire la politica organizzativa per i controlli di cancellazione delle informazioni garantendo la rimozione sistematica dei dati al soddisfacimento dei requisiti di conservazione, supportando i principi di minimizzazione dei dati, la conformità normativa e la protezione contro la divulgazione non autorizzata.

---

# Enunciati di politica

## Trigger di cancellazione

[Organizzazione] DEVE cancellare le informazioni quando si verifica una delle seguenti condizioni:

**Scadenza del periodo di conservazione**: Le categorie di dati DEVONO avere periodi di conservazione definiti nel Calendario di conservazione (ISMS-REG-CONSERVAZIONE); la cancellazione DEVE avvenire al raggiungimento o entro 30 giorni dalla scadenza; il Calendario di conservazione DEVE essere rivisto annualmente.

**Richieste di cancellazione degli interessati** (RGPD Art. 17, nLPD): Le richieste di cancellazione valide DEVONO essere eseguite entro 30 giorni dalla ricezione; le eccezioni (es. obblighi legali di conservazione in conflitto) DEVONO essere documentate; il RPD DEVE essere coinvolto nelle decisioni di eccezione complesse.

**Chiusura del contratto**: I dati dei clienti DEVONO essere cancellati entro 90 giorni dalla scadenza del contratto salvo che la conservazione sia richiesta per legge; le terze parti DEVONO confermare la cancellazione per iscritto.

**Dismissione dell'asset**: Le apparecchiature contenenti dati DEVONO essere sanificate prima della dismissione (per ISMS-POL-A.7.14); i supporti fisici DEVONO essere distrutti o cancellati in modo sicuro; i certificati di distruzione DEVONO essere ottenuti per i dati Riservati.

## Metodi di cancellazione approvati

**Per tipo di supporto e classificazione dei dati**:

| Supporto | Dati RISERVATI | Dati INTERNI | Dati PUBBLICI |
|---------|---------------|-------------|--------------|
| HDD (magnetico) | Sovrascrittura a 3 passaggi + verifica O distruzione fisica certificata | Sovrascrittura a 1 passaggio + verifica | Cancellazione del sistema di file con verifica |
| SSD/Flash | Cancellazione crittografica + verifica O distruzione fisica | Cancellazione crittografica O cancellazione sicura del produttore | Cancellazione sicura della piattaforma |
| Nastri di backup | Smagnetizzazione certificata O distruzione fisica | Smagnetizzazione O sovrascrittura | Sovrascrittura |
| Archiviazione cloud | Cancellazione certificata dell'API + verifica dal fornitore | Cancellazione tramite API del fornitore | Eliminazione della piattaforma |
| Dispositivi mobili | Ripristino certificato del produttore + verifica | Ripristino alle impostazioni di fabbrica | Ripristino alle impostazioni di fabbrica |
| Documenti cartacei | Tritatura trasversale certificata (≥P-4) | Tritatura standard (≥P-3) | Cestino |

**Standard di riferimento**: I metodi di cancellazione DEVONO allinearsi a: NIST SP 800-88 Rev. 2; ISO/IEC 21964; linee guida del produttore.

## Verifica della cancellazione

[Organizzazione] DEVE verificare che la cancellazione sia avvenuta correttamente.

**Requisiti di verifica**: Scansione post-cancellazione per confermare l'assenza di dati residui (per i dati RISERVATI); documentazione del metodo di cancellazione e dei risultati di verifica; certificati di distruzione conservati per 7 anni per i dati RISERVATI; segnalazione delle anomalie al RSSI entro 24 ore dalla scoperta.

## Cancellazione di terze parti e cloud

**Obblighi contrattuali dei responsabili del trattamento** (RGPD Art. 28): Gli accordi con i responsabili del trattamento DEVONO includere obblighi di cancellazione; la conferma scritta della cancellazione DEVE essere ottenuta entro 30 giorni dalla richiesta; i registri degli obblighi di cancellazione DEVONO essere mantenuti.

**Provider cloud**: I contratti DEVONO specificare i requisiti di cancellazione; i registri di eliminazione del provider (log API, certificati) DEVONO essere conservati come prove; la cancellazione dei dati dal sistema di backup DEVE essere confermata.

## Gestione del blocco legale

Le informazioni soggette a blocco legale (contenzioso o indagine) SONO ESENTATE dalla cancellazione di routine.

**Processo**: Il consulente legale emette il blocco legale con il perimetro documentato; il RSSI garantisce che i sistemi tecnici implementino il blocco; la cancellazione di routine DEVE essere sospesa per gli elementi sotto blocco; il blocco DEVE essere revocato solo dal consulente legale.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; supervisione della conformità |
| **RPD** | Richieste di cancellazione degli interessati; conformità RGPD/nLPD; decisioni di eccezione |
| **Consulente legale** | Calendario di conservazione; gestione del blocco legale; eccezioni normative |
| **Operazioni IT** | Esecuzione tecnica della cancellazione; dispiegamento della cancellazione automatizzata |
| **Proprietari dei dati** | Definizione dei periodi di conservazione; autorizzazione della cancellazione |

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Cancellazione delle informazioni** | Rimozione sistematica dei dati da tutti i sistemi di archiviazione per garantirne l'irrecuperabilità |
| **Blocco legale** | Obbligo di conservazione dovuto a contenzioso o indagine attivi o previsti |
| **Cancellazione crittografica** | Cancellazione sicura tramite distruzione delle chiavi di cifratura |
| **Calendario di conservazione** | Documento che specifica per quanto tempo devono essere conservate le diverse categorie di dati |
| **Smagnetizzazione** | Utilizzo di campi magnetici per cancellare i dati dai supporti magnetici |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **RPD** | [Nome] | [Data] |
| **Responsabile Legale/Conformità** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la cancellazione delle informazioni. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.10 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
