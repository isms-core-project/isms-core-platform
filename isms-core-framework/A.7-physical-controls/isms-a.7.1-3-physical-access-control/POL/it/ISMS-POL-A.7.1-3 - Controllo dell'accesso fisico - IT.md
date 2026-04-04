<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.1-3-IT:framework:POL:a.7.1-3 -->
**ISMS-POL-A.7.1-3 — Controllo dell'accesso fisico**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Controllo dell'accesso fisico |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.7.1-3 |
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
- Secondario: Responsabile delle strutture
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.7.4-5-11 (Sicurezza dell'infrastruttura fisica)
- ISMS-POL-A.6.7-8 (Lavoro da remoto e segnalazione)
- ISMS-IMP-A.7.1-3.S1-3-UG/TG (Suite di valutazione)
- ISO/IEC 27001:2022 Controlli A.7.1, A.7.2, A.7.3

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per il controllo dell'accesso fisico, comprendo i perimetri di sicurezza, i controlli di ingresso e la protezione di uffici, sale e strutture.

**Perimetro**: Si applica a tutti i locali, le strutture e le aree di [Organizzazione] in cui gli asset informativi vengono elaborati, archiviati o trasmessi.

**Approccio a controlli combinati**: I Controlli A.7.1 (Perimetri di sicurezza fisica), A.7.2 (Ingresso fisico) e A.7.3 (Protezione di uffici, sale e strutture) sono implementati insieme perché formano un quadro integrato di sicurezza fisica.

**Allineamento normativo**: nLPD svizzera (Art. 8); ISO/IEC 27001:2022; RGPD dell'UE, PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale).

---

# Allineamento sul controllo e perimetro

**A.7.1 — Perimetri di sicurezza fisica**: I perimetri di sicurezza devono essere definiti e utilizzati per proteggere le aree che contengono informazioni e altri asset associati.

**A.7.2 — Ingresso fisico**: Le aree sicure devono essere protette da adeguati controlli di ingresso per garantire che solo il personale autorizzato sia ammesso.

**A.7.3 — Protezione di uffici, sale e strutture**: La sicurezza fisica di uffici, sale e strutture deve essere progettata e implementata.

**Obiettivi del controllo**: Prevenire l'accesso fisico non autorizzato; definire e applicare i confini di sicurezza; garantire che solo il personale autorizzato possa accedere alle aree sicure.

---

# Enunciati di politica

## Perimetri di sicurezza fisica (A.7.1)

### Definizione del perimetro

[Organizzazione] DEVE definire e documentare i perimetri di sicurezza fisica:

**Zone di sicurezza**:

| Zona | Descrizione | Aree di esempio |
|------|-------------|-----------------|
| **Zona pubblica** | Accessibile al pubblico generale | Hall d'ingresso, aree di attesa visitatori |
| **Zona controllata** | Accessibile al personale autorizzato | Uffici generali, sale riunioni |
| **Zona riservata** | Accesso limitato, need-to-know | Uffici dirigenziali, HR, finanza |
| **Zona ad alta sicurezza** | Accesso rigorosamente controllato | Sale server, data center, operazioni di sicurezza |

**Requisiti del perimetro**: I perimetri DEVONO essere chiaramente definiti e documentati; le barriere fisiche DEVONO essere appropriate alla classificazione della zona; non DEVONO esserci lacune nei perimetri; i perimetri DEVONO estendersi dal pavimento al soffitto.

### Costruzione del perimetro

**Perimetro dell'edificio**: Le pareti esterne, i tetti e i pavimenti DEVONO essere di costruzione solida; le porte esterne DEVONO essere protette da serrature e controlli di accesso appropriati; le finestre DEVONO essere protette, specialmente al piano terra.

**Perimetri interni**: Le partizioni tra zone di sicurezza DEVONO arrivare dal pavimento al soffitto; i punti di accesso tra le zone DEVONO avere controlli appropriati.

### Collocazione e strutture condivise

Dove [Organizzazione] opera in strutture di colocation o condivise, i controlli del perimetro fisico DEVONO essere garantiti tramite: delimitazione documentata delle aree controllate da [Organizzazione]; requisiti contrattuali per la sicurezza fisica e la registrazione degli accessi; prove di garanzia del fornitore (es. certificato ISO 27001, report SOC) riviste per ISMS-POL-A.5.19-23.

## Controlli di ingresso fisico (A.7.2)

### Sistemi di controllo degli accessi

**Metodi di autenticazione**:

| Zona di sicurezza | Autenticazione minima |
|-------------------|----------------------|
| **Zona controllata** | Badge/card di accesso |
| **Zona riservata** | Badge + PIN |
| **Zona ad alta sicurezza** | Badge + PIN + biometria OPPURE controllo a due persone |

**Requisiti del controllo degli accessi**:

- I diritti di accesso DEVONO essere basati sul ruolo lavorativo e sul need-to-know
- I diritti di accesso DEVONO essere rivisti trimestralmente
- L'accesso del dipendente cessato DEVE essere revocato immediatamente
- I badge persi DEVONO essere segnalati e disattivati immediatamente
- La condivisione dei badge È VIETATA

### Gestione dei visitatori

**Procedure per i visitatori**:

- Tutti i visitatori DEVONO registrarsi alla reception
- I visitatori DEVONO presentare un documento d'identità
- I badge dei visitatori DEVONO essere chiaramente distinguibili da quelli dei dipendenti
- I visitatori DEVONO essere accompagnati nelle zone riservate e ad alta sicurezza
- I registri dei visitatori DEVONO essere conservati per un minimo di 12 mesi

**Accesso di appaltatori e manutentori**:

- Gli appaltatori DEVONO essere pre-autorizzati prima dell'arrivo
- L'accesso degli appaltatori DEVE essere limitato nel tempo e registrato
- Gli appaltatori nelle zone ad alta sicurezza DEVONO essere accompagnati

## Protezione di uffici, sale e strutture (A.7.3)

### Sicurezza dell'ufficio

**Uffici generali**: Gli uffici DEVONO essere chiusi a chiave quando non occupati (fuori orario); la politica della scrivania libera DEVE essere applicata; i documenti sensibili DEVONO essere conservati in armadietti chiusi a chiave; gli schermi DEVONO essere posizionati per prevenire l'osservazione da parte di terzi.

**Aree sensibili**: Le aree che elaborano informazioni RISERVATE devono avere controlli di accesso aggiuntivi (determinati in base alla classificazione per ISMS-POL-A.5.12-13); i log degli accessi DEVONO essere mantenuti.

**Conservazione dei log degli accessi**: I log del sistema di controllo degli accessi fisici DEVONO essere conservati per almeno 12 mesi, protetti da modifiche non autorizzate e disponibili entro 2 giorni lavorativi per audit e risposta agli incidenti.

### Sale server e data center

**Controllo degli accessi**:

- L'accesso DEVE essere limitato al solo personale IT autorizzato
- È richiesta l'autenticazione a più fattori (AMF)
- Tutti gli accessi DEVONO essere registrati con identità e timestamp
- Il controllo a due persone DEVE essere implementato per le aree di massima sicurezza

**Sicurezza fisica**:

Per le sale server controllate da [Organizzazione]: nessuna finestra esterna; pareti, pavimenti e soffitti rinforzati; monitoraggio ambientale (incendio, acqua, temperatura); copertura CCTV con registrazione.

Per i data center/colocation di terze parti: [Organizzazione] DEVE garantire protezioni equivalenti tramite garanzia del fornitore (ISO 27001, report SOC) e requisiti contrattuali.

### Sale riunioni

- Le sale riunioni DEVONO essere controllate per rilevare dispositivi di registrazione prima di discussioni sensibili
- Le lavagne DEVONO essere cancellate dopo le riunioni
- I documenti NON DEVONO essere lasciati nelle sale riunioni

### Verifica dei controlli

La conformità ai requisiti di ufficio, sala riunioni e area sensibile DEVE essere verificata attraverso sopralluoghi/controlli a campione di sicurezza fisica documentati almeno trimestralmente (e dopo incidenti importanti). I risultati DEVONO essere registrati come non conformità o azioni di miglioramento e monitorati fino alla chiusura per la Clausola 10.2.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per il controllo dell'accesso fisico |
|-------|-----------------------------------------------------|
| **Direzione generale** | Approvare la politica, allocare risorse per la sicurezza fisica |
| **RSSI** | Proprietà della politica, standard di sicurezza fisica, supervisione della conformità |
| **Responsabile delle strutture** | Implementazione della sicurezza fisica, operazioni del sistema di controllo degli accessi |
| **Reception/Sicurezza** | Gestione dei visitatori, monitoraggio, risposta agli incidenti |
| **Responsabili diretti** | Autorizzare l'accesso per i membri del team, garantire la conformità |
| **Tutto il personale** | Seguire le procedure di accesso, segnalare gli incidenti di sicurezza, sfidare le persone sconosciute |

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Audit della sicurezza del perimetro | Annuale | Responsabile delle strutture | Report di ispezione |
| Revisione del sistema di controllo degli accessi | Trimestrale | Sicurezza IT | Configurazione del sistema, log |
| Revisione dei diritti di accesso | Trimestrale | Responsabile delle strutture | Liste di accesso, approvazioni |
| Audit del registro visitatori | Mensile | Team di sicurezza | Registri dei visitatori |
| Test di sicurezza fisica | Annuale | Audit interno | Risultati dei test di penetrazione |

**Metriche di governance**: Copertura del controllo degli accessi (obiettivo: 100% dei punti di ingresso); tentativi di accesso non autorizzato (obiettivo: 0 riusciti); conformità all'accompagnamento dei visitatori (obiettivo: 100%); revisioni degli accessi completate in tempo (obiettivo: 100%); incidenti di perdita/furto di badge (obiettivo: <5 per trimestre).

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Perimetro di sicurezza** | Un confine definito che protegge un'area sicura dall'accesso non autorizzato |
| **Area sicura** | Una ubicazione in cui l'accesso è controllato e limitato al personale autorizzato |
| **Tailgating** | Seguire una persona autorizzata attraverso un punto di accesso senza autenticazione |
| **Controllo a due persone** | Requisito che due persone autorizzate siano presenti per l'accesso |
| **Visitatore** | Qualsiasi persona che non è un dipendente o un appaltatore regolare |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Responsabile delle strutture** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per il controllo dell'accesso fisico. Le procedure di attuazione sono documentate in ISMS-IMP-A.7.1-3 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
