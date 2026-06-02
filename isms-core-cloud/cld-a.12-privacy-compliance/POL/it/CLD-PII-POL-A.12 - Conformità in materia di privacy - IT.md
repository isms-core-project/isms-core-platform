<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.12-IT:cloud:POL:a.12 -->
**CLD-PII-POL-A.12 — Conformità in materia di privacy**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Responsabile del trattamento di DCP nel cloud pubblico — Conformità in materia di privacy |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-PII-POL-A.12 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) / RSSI |
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
| 1.0 | [Data da definire] | RPD / RSSI | Politica iniziale per l'implementazione di ISO/IEC 27018:2025 Ed. 3 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti normativi, dell'impronta del servizio o della residenza dei dati)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :
- Principale: Responsabile della Protezione dei Dati (RPD)
- Secondaria: RSSI / Responsabile Sicurezza Cloud
- Autorità finale: Direzione generale

**Documenti correlati** :
- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- ISMS-POL-A.5.34 (Privacy e protezione dei DCP)
- ISMS-POL-A.5.19-23 (Relazioni con fornitori e terze parti)
- CLD-PII-POL-A.1 (Generalità)
- CLD-PII-POL-A.8 (Apertura, trasparenza — divulgazione dei sub-responsabili del trattamento)
- CLD-PII-POL-A.11 (§11.12 — Trattamento dei DCP in sub-appalto)
- ISO/IEC 27018:2025 Allegato A, Sezione A.12 e Controlli A.12.1–A.12.2
- ISO/IEC 27701:2025 Controlli A.2.5.2 (base per il trasferimento di DCP tra giurisdizioni) e A.2.5.3 (paesi e organizzazioni internazionali verso cui i DCP possono essere trasferiti)
- RGPD Articolo 28(3)(a) (il responsabile del trattamento tratta solo su istruzioni documentate); Articoli 44–49 (trasferimenti verso paesi terzi); Articolo 46 (garanzie appropriate per i trasferimenti internazionali)
- LPD svizzera Articoli 16–17 (trasferimenti internazionali di dati personali); Articolo 9(3) (obblighi del responsabile del trattamento in materia di sub-responsabili del trattamento e ubicazioni)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] come responsabile del trattamento di DCP nel cloud pubblico in materia di conformità alla privacy — in particolare l'obbligo di comunicare le ubicazioni geografiche in cui i DCP vengono archiviati, trattati o transitano, di rispettare i requisiti di residenza dei dati imposti dai titolari del trattamento dei DCP, e di documentare e comunicare tutte le destinazioni previste dei DCP, compresi i trasferimenti internazionali e la loro base giuridica — conformemente alla Sezione A.12 e ai Controlli A.12.1 e A.12.2 dell'Allegato A di ISO/IEC 27018:2025.

**Perimetro** : Tutti i DCP trattati da [Organizzazione] per conto dei titolari del trattamento dei DCP, in tutte le regioni di infrastruttura, le zone di disponibilità e le ubicazioni dei sub-responsabili del trattamento.

**Motivazione dei controlli combinati** : A.12.1 e A.12.2 affrontano la dimensione geografica della trasparenza del trattamento dei DCP. A.12.1 stabilisce l'obbligo di comunicare dove risiedono i DCP; A.12.2 stabilisce l'obbligo di identificare tutte le destinazioni verso cui i DCP possono fluire e di documentare la base giuridica di qualsiasi trasferimento al di fuori della giurisdizione del titolare del trattamento. Insieme, questi controlli consentono ai titolari del trattamento dei DCP di adempiere ai propri obblighi di accountability in materia di trasferimenti ai sensi dell'Articolo 44+ del RGPD e della legislazione nazionale equivalente.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27018:2025

**Sezione A.12 — Conformità in materia di privacy (principio)**

La Sezione A.12 stabilisce il principio che un responsabile del trattamento di DCP nel cloud pubblico deve mantenere e comunicare ai titolari del trattamento le ubicazioni geografiche in cui i DCP vengono archiviati, trattati o trasmessi, implementare meccanismi per applicare i requisiti di residenza dei dati, e documentare la base giuridica di qualsiasi trasferimento transfrontaliero.

**Controllo A.12.1 — Ubicazione geografica dei DCP**

Il Controllo A.12.1 richiede che il responsabile del trattamento comunichi tutti i paesi e le regioni coinvolti nel trattamento dei DCP — comprese le ubicazioni dei sub-responsabili del trattamento — fornisca preavviso prima di modificare tali ubicazioni, e applichi tecnicamente qualsiasi restrizione di residenza concordata con il titolare del trattamento.

**Controllo A.12.2 — Destinazione prevista dei DCP**

Il Controllo A.12.2 richiede che il responsabile del trattamento documenti e comunichi tutte le destinazioni previste per i trasferimenti di DCP, incluso il meccanismo di trasferimento applicabile e le garanzie per ciascun flusso transfrontaliero o trans-giurisdizionale.

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 28(3)(a) (il responsabile del trattamento tratta solo in conformità alle istruzioni del titolare del trattamento, incluso sull'ubicazione); Articoli 44–49 (divieto di trasferimenti verso paesi terzi privi di protezione adeguata salvo garanzie appropriate); Articolo 46 (clausole contrattuali standard, norme vincolanti d'impresa, codici di condotta come meccanismi di trasferimento); Articolo 30 (registro delle attività di trattamento comprendente destinatari e paesi terzi)
- **LPD svizzera** : Articoli 16–17 (divieto di trasferimento di dati personali verso paesi senza protezione adeguata; garanzie riconosciute); Articolo 9(3) (obblighi del responsabile del trattamento in materia di sub-appalto e ubicazioni)
- **ISO/IEC 27018:2025** : Controlli A.12.1, A.12.2

---

# Enunciati della politica: Ubicazione geografica dei DCP (A.12.1)

## Divulgazione dell'ubicazione

[Organizzazione] DEVE mantenere un **Registro delle ubicazioni di trattamento dei DCP** che documenta tutti i paesi e le regioni in cui i DCP vengono archiviati, trattati o transitano nell'ambito dell'erogazione dei servizi cloud. Il registro DEVE coprire:

- **Ubicazioni di archiviazione primarie** : Data center e regioni cloud dove risiedono i DCP a riposo
- **Ubicazioni di trattamento** : Regioni di calcolo dove i DCP vengono attivamente trattati
- **Route di transito** : Regioni attraverso cui i DCP possono passare durante operazioni di replica, backup o consegna
- **Ubicazioni dei sub-responsabili del trattamento** : Tutte le ubicazioni geografiche dei sub-responsabili del trattamento ingaggiati ai sensi di CLD-PII-POL-A.11 (§11.12)

Il Registro delle ubicazioni di trattamento dei DCP DEVE essere messo a disposizione dei titolari del trattamento dei DCP su richiesta. Una versione riepilogativa — che copre le ubicazioni primarie di archiviazione e trattamento e i paesi dei sub-responsabili del trattamento, ma omette le informazioni dettagliate sulle route di transito — DEVE essere pubblicata sul portale di fiducia di [Organizzazione] per i titolari del trattamento che operano in regime di autorizzazione generale. I titolari del trattamento autenticati possono richiedere il registro completo tramite il portale di fiducia o direttamente al RPD. I dettagli sulle route di transito vengono forniti solo ai titolari del trattamento autenticati, date le implicazioni di sicurezza della divulgazione pubblica completa.

## Applicazione della residenza dei dati

Laddove un titolare del trattamento dei DCP specifichi requisiti di residenza dei dati nell'accordo di servizio (es. «archiviazione solo UE», «solo Svizzera»), [Organizzazione] DEVE:

- **Applicare tecnicamente** il vincolo di residenza tramite la configurazione dell'infrastruttura (restrizioni regionali, geo-fencing, regole di policy di archiviazione)
- **Documentare** il meccanismo tecnico utilizzato per applicare il vincolo e rendere questa documentazione disponibile al titolare del trattamento su richiesta
- **Verificare** la conformità alla residenza almeno annualmente e in caso di significativi cambiamenti all'infrastruttura, confermando che nessun DCP sia stato archiviato o trattato al di fuori delle regioni concordate

## Notifica di modifiche

Prima di modificare l'ubicazione geografica del trattamento dei DCP — inclusa l'apertura di una nuova regione di servizio, l'aggiunta di un sub-responsabile del trattamento in una nuova giurisdizione o la ricollocazione dell'archiviazione di backup — [Organizzazione] DEVE:

1. Notificare il titolare del trattamento dei DCP interessato in anticipo, con un preavviso minimo di **30 giorni** (salvo che l'accordo di servizio specifichi un periodo più lungo)
2. Identificare la nuova ubicazione e spiegare il motivo operativo del cambiamento
3. Ottenere il consenso preventivo dei titolari del trattamento i cui accordi di servizio richiedono un consenso specifico (e non solo un'autorizzazione generale) per le modifiche all'ubicazione
4. Aggiornare il Registro delle ubicazioni di trattamento dei DCP entro 5 giorni lavorativi dall'entrata in vigore del cambiamento

Le modifiche urgenti all'ubicazione (es. a causa di un guasto al data center o di forza maggiore) DEVONO essere notificate ai titolari del trattamento interessati senza indebito ritardo. [Organizzazione] DEVE inoltre fornire ai titolari del trattamento interessati un riconoscimento scritto provvisorio della deviazione — inclusa la nuova ubicazione temporanea, la durata prevista della deviazione e qualsiasi lacuna temporanea nella residenza — in modo che i titolari del trattamento possano prendere decisioni informate riguardo ai propri obblighi di notifica durante il periodo di lacuna. La documentazione formale retroattiva del cambiamento e della sua giustificazione DEVE essere completata entro 5 giorni lavorativi.

---

# Enunciati della politica: Destinazione prevista dei DCP (A.12.2)

## Documentazione dei trasferimenti

[Organizzazione] DEVE mantenere registrazioni documentate di tutte le **destinazioni previste** verso cui i DCP possono essere trasferiti nell'ambito dell'erogazione dei servizi cloud, inclusi i flussi transfrontalieri o trans-giurisdizionali verso:

- Sub-responsabili del trattamento (che si trovino o meno nel SEE)
- Siti di backup e ripristino di emergenza in paesi terzi
- Infrastruttura di provider cloud in giurisdizioni al di fuori del paese d'origine del titolare del trattamento
- Personale di supporto o operativo che accede ai DCP da remoto dall'esterno della regione di trattamento (gestito tramite architettura di server di salto che mantiene i dati nella regione, o tramite CCS incorporate negli accordi di impiego o di prestazione — il meccanismo specifico di [Organizzazione] DEVE essere documentato nelle registrazioni delle destinazioni di trasferimento)

Per ciascuna destinazione identificata, [Organizzazione] DEVE documentare:

| Elemento | Descrizione |
|---------|-------------|
| **Paese/regione di destinazione** | Giurisdizione del destinatario previsto o dell'ubicazione di trattamento |
| **Finalità del trasferimento** | Motivo operativo del trasferimento (backup, accesso di supporto, replica, ecc.) |
| **Meccanismo di trasferimento** | Base giuridica del trasferimento (decisione di adeguatezza, CCS, BCR, deroga — vedere di seguito) |
| **Garanzie in atto** | Protezioni tecniche e contrattuali applicate (cifratura in transito, DPA/addendum, accordo di trattamento) |
| **Stato di notifica del titolare del trattamento** | Se il titolare del trattamento è stato informato di questa destinazione |

## Meccanismi di trasferimento

Per i trasferimenti di DCP verso paesi al di fuori del SEE o della Svizzera privi di una decisione di adeguatezza, [Organizzazione] DEVE implementare uno dei seguenti meccanismi di trasferimento approvati:

- **Clausole Contrattuali Standard (CCS)** : CCS approvate dalla CE (serie 2021) incorporate negli accordi di sub-responsabile del trattamento e di trattamento dei dati
- **Accordo di Trasferimento Internazionale dei Dati del Regno Unito (IDTA)** : Per i trasferimenti da/verso il Regno Unito — il Responsabile Legale/Conformità deve verificare le linee guida ICO aggiornate sulle versioni IDTA prima dell'esecuzione
- **Clausole standard di protezione dei dati dell'IFPDT svizzero** : Per i trasferimenti soggetti alla LPD svizzera — il Responsabile Legale/Conformità deve confermare il titolo esatto dello strumento e la data di pubblicazione dal sito web dell'IFPDT prima dell'esecuzione
- **Decisione di adeguatezza** : Laddove il paese di destinazione disponga di una decisione di adeguatezza UE o svizzera in vigore al momento del trasferimento
- **Norme vincolanti d'impresa (BCR)** : Ove applicabile per i trasferimenti intra-gruppo

[Organizzazione] NON DEVE trasferire DCP verso un paese terzo senza che uno dei meccanismi di cui sopra sia in atto e documentato. Laddove lo stato di adeguatezza di un paese di destinazione cambi, [Organizzazione] DEVE:

1. **Cessare i nuovi trasferimenti** verso il paese interessato entro **5 giorni lavorativi** dalla scadenza o dall'invalidazione della decisione di adeguatezza
2. **Implementare meccanismi di trasferimento alternativi** (es. CCS) entro **60 giorni**, con supervisione del RPD e notifica ai titolari del trattamento durante tutto il processo
3. **Notificare i titolari del trattamento dei DCP interessati** non appena vengono a conoscenza del cambiamento di adeguatezza, confermando la data di cessazione e il meccanismo alternativo previsto

La separazione tra l'obbligo di cessazione e l'implementazione del meccanismo alternativo riflette la realtà pratica della rinegoziazione degli strumenti con più sub-responsabili del trattamento contemporaneamente, proteggendo al contempo gli interessati da trasferimenti non salvaguardati continuativi.

## Valutazioni d'Impatto del Trasferimento (VIT)

È richiesta una Valutazione d'Impatto del Trasferimento (VIT) prima di trasferire DCP verso qualsiasi paese per cui vi siano ragioni di ritenere che il quadro giuridico locale non fornisca protezioni sostanzialmente equivalenti al RGPD. Gli indicatori che innescano una VIT includono: paesi con programmi di sorveglianza di massa documentati, assenza di un'autorità indipendente per la protezione dei dati o assenza di protezioni dello stato di diritto per i dati dei cittadini stranieri. Il RPD DEVE mantenere un elenco delle giurisdizioni attualmente designate come richiedenti una VIT. La metodologia della VIT segue le Raccomandazioni 01/2020 dell'EDPB sulle misure supplementari. Le VIT completate vengono conservate secondo il piano delle prove e messe a disposizione dei titolari del trattamento su richiesta.

## Modifiche all'ubicazione dei sub-responsabili del trattamento

I sub-responsabili del trattamento sono contrattualmente tenuti a notificare a [Organizzazione] qualsiasi modifica all'ubicazione geografica delle loro operazioni di trattamento dei DCP entro 10 giorni lavorativi dal cambiamento (ai sensi dei requisiti degli accordi con i sub-responsabili del trattamento di CLD-PII-POL-A.11 §11.12). [Organizzazione] DEVE esaminare i dati di ubicazione dei sub-responsabili del trattamento al minimo annualmente nell'ambito dell'audit annuale dei sub-responsabili del trattamento ai sensi di CLD-PII-POL-A.11 §11.12, e aggiornare di conseguenza il Registro delle ubicazioni di trattamento dei DCP.

## Informazioni ai titolari del trattamento

[Organizzazione] DEVE mettere la documentazione dei trasferimenti a disposizione dei titolari del trattamento dei DCP su richiesta. Laddove richiesto da un titolare del trattamento per supportare il proprio registro delle attività di trattamento ai sensi dell'Articolo 30 del RGPD o le proprie valutazioni d'impatto dei trasferimenti, [Organizzazione] DEVE fornire:

- L'elenco completo delle destinazioni di trasferimento per i DCP del titolare del trattamento
- Il meccanismo di trasferimento e il riferimento allo strumento giuridico pertinente (es. riferimento alla clausola CCS, citazione della decisione di adeguatezza) per ciascuna destinazione
- Un riepilogo delle garanzie tecniche supplementari applicate per i trasferimenti verso giurisdizioni ad alto rischio

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **Responsabile della Protezione dei Dati (RPD)** | È proprietario del Registro delle ubicazioni di trattamento dei DCP e della documentazione dei trasferimenti; fornisce consulenza sulle valutazioni di adeguatezza e sulla selezione dei meccanismi di trasferimento; gestisce la notifica ai titolari del trattamento per le modifiche all'ubicazione; esamina annualmente i meccanismi di trasferimento |
| **RSSI / Responsabile Sicurezza Cloud** | Implementa e verifica i controlli tecnici di applicazione della residenza dei dati; supervisiona il monitoraggio delle ubicazioni dei sub-responsabili del trattamento; gestisce le notifiche urgenti di modifiche all'ubicazione |
| **Responsabile Legale/Conformità** | Mantiene i modelli di CCS, IDTA e clausole standard svizzere; fornisce consulenza sullo stato di adeguatezza dei paesi terzi; esamina la documentazione dei trasferimenti per la conformità normativa |
| **Cloud Engineering** | Implementa i vincoli geografici dei dati e i meccanismi di applicazione della residenza; configura l'isolamento regionale per i carichi di lavoro dei clienti; verifica la conformità alla residenza |
| **Acquisti** | Garantisce che le ubicazioni dei sub-responsabili del trattamento vengano acquisite prima della firma del contratto; attiva la revisione del RPD per le ubicazioni nuove o modificate dei sub-responsabili del trattamento |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registro delle ubicazioni di trattamento dei DCP | Registro completo di tutte le ubicazioni di archiviazione, trattamento e transito dei DCP, compresi i sub-responsabili del trattamento | In corso + versioni precedenti per 5 anni |
| Registrazioni di configurazione della residenza dei dati | Documentazione tecnica dei meccanismi di applicazione della residenza per titolare del trattamento | Durata dell'accordo + 5 anni |
| Risultati degli audit di residenza | Risultati degli audit annuali che confermano l'assenza di trattamento dei DCP fuori perimetro | 5 anni |
| Notifiche di modifica dell'ubicazione | Registrazioni dei preavvisi inviati ai titolari del trattamento per le modifiche all'ubicazione | 5 anni |
| Registrazioni delle destinazioni di trasferimento | Documentazione completa delle destinazioni di trasferimento per titolare del trattamento | Durata dell'accordo + 5 anni |
| Strumenti di meccanismo di trasferimento | Copie delle CCS, IDTA, BCR e citazioni delle decisioni di adeguatezza invocate | Durata dell'impegno + 5 anni |
| Registrazioni della Valutazione d'Impatto del Trasferimento | VIT documentate o valutazioni equivalenti per i trasferimenti verso giurisdizioni ad alto rischio | 5 anni |

---

# Considerazioni di audit

I revisori che verificano la conformità a CLD-PII-POL-A.12 dovrebbero aspettarsi di trovare:

- Un Registro delle ubicazioni di trattamento dei DCP aggiornato che copra tutte le ubicazioni di archiviazione, trattamento e transito, compresi i sub-responsabili del trattamento — coerente con l'elenco pubblicato dei sub-responsabili del trattamento (CLD-PII-POL-A.8.1)
- Prove tecniche che i controlli di residenza dei dati siano implementati e applicati per tutti i titolari del trattamento con requisiti di residenza
- Registrazioni della notifica preventiva ai titolari del trattamento per eventuali modifiche all'ubicazione verificatesi nel periodo di audit
- Registrazioni delle destinazioni di trasferimento con meccanismi di trasferimento documentati per tutte le ubicazioni di trattamento extra-SEE/extra-Svizzera — incluse CCS o strumenti equivalenti per ciascuna destinazione in un paese terzo
- Nessun trasferimento di DCP non documentato verso paesi terzi privi di un meccanismo di trasferimento approvato

---

<!-- QA_VERIFIED: 2026-04-04 -->
