<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.7-IT:cloud:POL:a.7 -->
**CLD-PII-POL-A.7 — Esattezza e qualità**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Responsabile del trattamento di DCP nel cloud pubblico — Esattezza e qualità |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-PII-POL-A.7 |
| **Autore del documento** | RSSI / Responsabile della Protezione dei Dati (RPD) |
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
| 1.0 | [Data da definire] | RSSI / RPD | Politica iniziale per l'implementazione di ISO/IEC 27018:2025 Ed. 3 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti dell'architettura del servizio)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :
- Principale: RSSI / Responsabile Sicurezza Cloud
- Secondaria: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati** :
- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- ISMS-POL-A.5.34 (Privacy e protezione dei DCP)
- CLD-PII-POL-A.2 (Consenso e scelta — cooperazione per i diritti degli interessati)
- CLD-PII-POL-A.6 (Limitazione dell'utilizzo, della conservazione e della divulgazione)
- CLD-PII-POL-A.9 (Partecipazione individuale e accesso)
- ISO/IEC 27018:2025 Annex A, Sezione A.7 (Esattezza e qualità — principio)
- ISO/IEC 27701:2025 Controllo A.2.3.2 (responsabile del trattamento — conformità agli obblighi verso gli interessati, incluso il supporto alla rettifica)
- RGPD Articolo 5(1)(d) (principio di esattezza); Articolo 16 (diritto di rettifica); Articolo 28(3)(e)
- LPD svizzera Articolo 6(4) (esattezza e obblighi di correzione); Articolo 9(2)(c)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] come responsabile del trattamento di DCP nel cloud pubblico in materia di esattezza e qualità — specificamente l'obbligo di mantenere l'integrità dei DCP archiviati nei sistemi cloud, di fornire meccanismi che consentano ai titolari del trattamento dei DCP di correggere, aggiornare o eliminare DCP inesatti, e di evitare di introdurre degradazione della qualità dei dati attraverso le operazioni di trattamento — conformemente a ISO/IEC 27018:2025 Annex A, Sezione A.7.

**Perimetro** : Tutti i DCP archiviati o trattati da [Organizzazione] per conto di titolari del trattamento dei DCP.

**Nota sul principio** : ISO/IEC 27018:2025 Annex A, Sezione A.7 è una sezione di livello di principio senza sub-controlli aggiuntivi al di là del corpo principale dello standard. Questa politica implementa il principio come impegno operativo. La responsabilità principale dell'esattezza dei DCP spetta al titolare del trattamento dei DCP; il ruolo di [Organizzazione] è preservare e non degradare l'esattezza, e fornire strumenti affinché il titolare del trattamento la mantenga.

---

# Perimetro e applicabilità

## ISO/IEC 27018:2025 — Sezione A.7

**Sezione A.7 — Esattezza e qualità (principio)**

La Sezione A.7 stabilisce il principio che un responsabile del trattamento di DCP nel cloud pubblico deve implementare controlli per mantenere l'esattezza e la completezza dei DCP che tratta per conto dei titolari del trattamento, fornire meccanismi che consentano al titolare del trattamento di correggere o aggiornare DCP inesatti, e evitare di introdurre degradazione della qualità attraverso le proprie operazioni di trattamento.

## Cosa questa politica NON copre

- Verificare l'esattezza dei DCP forniti a [Organizzazione] dal titolare del trattamento dei DCP — l'esattezza dei dati di origine è responsabilità del titolare del trattamento
- Gli standard di qualità dei dati per il trattamento proprio del titolare del trattamento — questi sono obblighi del titolare del trattamento ai sensi dell'Articolo 5(1)(d) del RGPD

## Quadro normativo

**Livello 1: Conformità obbligatoria** (per PRIV-POL-00):

- **RGPD UE** : Articolo 5(1)(d) (esattezza — i DCP devono essere esatti e, se necessario, aggiornati; i DCP inesatti devono essere cancellati o rettificati senza indugio); Articolo 16 (diritto di rettifica — il titolare del trattamento deve poter esercitare questo diritto, richiedendo la cooperazione del responsabile del trattamento); Articolo 28(3)(e)
- **LPD svizzera** : Articolo 6(4) (esattezza e obblighi di correzione); Articolo 9(2)(c)
- **ISO/IEC 27018:2025** : Principio Sezione A.7

---

# Disposizioni della politica: Esattezza e qualità (A.7)

## Preservazione dell'integrità dei dati

[Organizzazione] DEVE implementare controlli tecnici che garantiscano che i DCP archiviati nei sistemi cloud non vengano degradati, corrotti o alterati attraverso le operazioni di trattamento, salvo autorizzazione del titolare del trattamento dei DCP. In particolare:

- I sistemi di archiviazione DEVONO implementare verifiche di integrità (es. checksum, hash crittografici) per gli archivi di DCP per rilevare modifiche non autorizzate o accidentali
- Le operazioni di trasformazione eseguite sui DCP durante il trattamento DEVONO essere reversibili ove tecnicamente fattibile; laddove irreversibili, lo stato originale dei DCP DEVE essere preservato in un record separato o in un backup prima della trasformazione
- Le operazioni di backup e replica DEVONO preservare l'esattezza e la completezza dei DCP senza perdita di dati

## Meccanismi di correzione da parte del titolare del trattamento

[Organizzazione] DEVE fornire ai titolari del trattamento dei DCP capacità tecniche per correggere, aggiornare ed eliminare DCP nell'archiviazione cloud. Tali meccanismi DEVONO:

- Consentire la correzione a livello di campo o l'aggiornamento completo del record per gli archivi di DCP strutturati
- Propagare le correzioni alle repliche attive e in sola lettura entro 24 ore, e alle copie di backup entro 72 ore dall'applicazione della correzione — e in ogni caso entro il termine richiesto affinché il titolare del trattamento adempia ai propri obblighi relativi ai diritti degli interessati
- Generare un record di conferma quando le correzioni sono completate, indicando quali record sono stati modificati e il timestamp

## Controlli di qualità

[Organizzazione] DEVE implementare i seguenti controlli di qualità per gli archivi di DCP:

- **Controlli di completezza dei dati** : Identificare e segnalare i record con campi obbligatori mancanti che possano indicare corruzione dei dati o trasferimento incompleto
- **Controlli di coerenza dei dati** : Verificare la coerenza dei DCP negli archivi di dati replicati o distribuiti per rilevare errori di replica
- **Verifica dell'integrità dei backup** : Ripristinare e verificare i dati DCP di backup al minimo trimestralmente per gli archivi di DCP critici, per confermare l'integrità dei backup

I risultati dei controlli di qualità DEVONO essere registrati nei log e riesaminati trimestralmente dal team Cloud Engineering. Un riepilogo dei risultati trimestrali dei controlli di qualità DEVE essere fornito anche al RPD. I problemi materiali di qualità dei dati — definiti come problemi che interessano più dell'1% dei record in un archivio dati, o qualsiasi problema che possa aver inciso su una decisione relativa ai diritti degli interessati o causato la divulgazione di DCP inesatti a una terza parte — DEVONO essere segnalati al titolare del trattamento dei DCP entro 3 giorni lavorativi dall'identificazione. Laddove venga rilevato un guasto all'integrità dei dati, l'incidente DEVE essere escalato in conformità con CLD-PII-POL-A.11 (Sicurezza delle informazioni).

## Inesattezza indotta dal trattamento

Laddove [Organizzazione] esegua operazioni di trasformazione, arricchimento o trattamento dei dati su DCP per conto di un titolare del trattamento, [Organizzazione] DEVE:

- Documentare la logica di trasformazione e il suo effetto sull'esattezza dei DCP
- Ottenere l'autorizzazione del titolare del trattamento per qualsiasi trasformazione che modifichi gli attributi dei DCP e non sia già coperta dall'accordo di servizio o dalla descrizione del trattamento documentata
- Avvisare il titolare del trattamento se un'operazione di trattamento produce risultati che indicano una possibile inesattezza nei dati di origine

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI / Responsabile Sicurezza Cloud** | Proprietario dei controlli di integrità per gli archivi di DCP; garantisce che i meccanismi di correzione siano funzionali; supervisiona il programma di controllo della qualità |
| **Ingegneria Cloud** | Implementa le verifiche di integrità, i meccanismi di correzione e i processi di controllo della qualità; indaga e risolve i problemi di qualità dei dati |
| **Responsabile della Protezione dei Dati (RPD)** | Fornisce consulenza sugli obblighi di esattezza ai sensi del RGPD e della LPD; esamina la documentazione delle capacità verso i titolari del trattamento; monitora le escalation degli incidenti di qualità dei dati |
| **Erogazione del servizio cloud** | Comunica i problemi di esattezza segnalati dai titolari del trattamento all'Ingegneria Cloud; segue la risoluzione e conferma il completamento al titolare del trattamento |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registrazioni di configurazione delle verifiche di integrità | Documentazione tecnica dei meccanismi di verifica dell'integrità per archivio dati | In corso + 3 anni |
| Documentazione dei meccanismi di correzione | Descrizione degli strumenti di correzione, aggiornamento ed eliminazione dei DCP disponibili per i titolari del trattamento per servizio | In corso + versioni precedenti per 3 anni |
| Log dei controlli di qualità | Risultati trimestrali dei controlli di qualità inclusi completezza, coerenza e verifica dei backup | 3 anni |
| Registrazioni degli incidenti di qualità dei dati | Registrazioni dei problemi materiali di qualità dei dati, notifiche ai titolari del trattamento e risoluzione | Durata del contratto + 3 anni |

---

# Considerazioni di audit

Gli auditor che verificano la conformità a CLD-PII-POL-A.7 devono aspettarsi di trovare:

- Documentazione tecnica che conferma l'implementazione delle verifiche di integrità per gli archivi di DCP
- Prove che i titolari del trattamento dei DCP abbiano accesso a meccanismi di correzione, aggiornamento ed eliminazione nei servizi cloud
- Log dei controlli di qualità che coprono il periodo di audit con revisione documentata
- Qualsiasi incidente di qualità dei dati segnalato ai titolari del trattamento con prove di risoluzione

---

<!-- QA_VERIFIED: 2026-04-04 -->
