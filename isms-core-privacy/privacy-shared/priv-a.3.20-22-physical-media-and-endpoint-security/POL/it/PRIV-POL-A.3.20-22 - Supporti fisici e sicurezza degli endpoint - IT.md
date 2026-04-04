<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.20-22-IT:privacy:POL:a.3.20-22 -->
**PRIV-POL-A.3.20-22 — Supporti fisici e sicurezza degli endpoint**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Supporti fisici e sicurezza degli endpoint |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.3.20-22 |
| **Autore del documento** | Responsabile della Protezione dei Dati (RPD) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione del prodotto Privacy** | 1.0 |

**Cronologia delle versioni** :

| Versione | Data | Autore | Modifiche |
|---------|------|--------|-----------|
| 1.0 | [Data da definire] | RPD | Politica iniziale per la prima certificazione ISO/IEC 27701:2025 |

**Ciclo di revisione** : Annuale | **Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** : Principale: RPD; Secondaria: RSSI; Legale: Responsabile Legale/Conformità; Autorità finale: Direzione generale.

**Documenti correlati** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.20-22-UG / TG
- ISMS-POL-A.7.8-10 (Scrivania libera, supporti e attrezzature — parallelo SGSI)
- ISMS-POL-A.8.1 (Dispositivi endpoint degli utenti — parallelo SGSI)
- PRIV-POL-A.3.5-7 (Classificazione delle informazioni e trasferimento)
- ISO/IEC 27701:2025 Controlli A.3.20, A.3.21, A.3.22
- RGPD Articolo 32 (sicurezza del trattamento — protezione su endpoint e supporti)
- LPD svizzera Articolo 7 (misure tecniche e organizzative)

**Applicabilità del ruolo** : Questa politica si applica all'organizzazione che agisce sia come **Titolare del trattamento che come Responsabile del trattamento dei DCP**. I controlli A.3.20, A.3.21 e A.3.22 sono controlli condivisi (Tabella A.3).

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione del ciclo di vita dei supporti di archiviazione contenenti DCP, lo smaltimento o il riutilizzo sicuro delle apparecchiature contenenti DCP, e la protezione dei DCP sui dispositivi endpoint degli utenti — conformemente ai controlli A.3.20, A.3.21 e A.3.22 di ISO/IEC 27701:2025.

**Perimetro** : Tutti i supporti di archiviazione contenenti DCP per tutto il loro ciclo di vita; tutte le apparecchiature contenenti supporti di archiviazione con DCP a fine vita o in caso di riassegnazione; tutti i dispositivi endpoint degli utenti su cui i DCP vengono archiviati, trattati o sono accessibili.

**Motivazione dei controlli combinati** : A.3.20 (supporti di archiviazione), A.3.21 (smaltimento delle apparecchiature) e A.3.22 (endpoint) affrontano i DCP a riposo in forma fisica e sui dispositivi. I controlli del ciclo di vita dei supporti prevengono la cattiva gestione durante l'uso attivo; i controlli di smaltimento prevengono l'esposizione residua dei DCP dopo l'uso; i controlli degli endpoint proteggono i DCP sui dispositivi più soggetti a perdita, furto o utilizzo improprio.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27701:2025

**Controllo A.3.20 — Supporti di archiviazione**
Il controllo A.3.20 richiede che [Organizzazione] gestisca i supporti di archiviazione contenenti DCP per tutto il loro ciclo di vita — acquisizione, utilizzo, trasporto e smaltimento — in conformità con lo schema di classificazione dell'organizzazione.

**Controllo A.3.21 — Smaltimento o riutilizzo sicuro delle apparecchiature**
Il controllo A.3.21 richiede che [Organizzazione] verifichi, prima che qualsiasi apparecchiatura contenente supporti di archiviazione venga smaltita o riutilizzata, che tutti i DCP archiviati su quei supporti siano stati rimossi o sovrascritti in modo sicuro.

**Controllo A.3.22 — Dispositivi endpoint degli utenti**
Il controllo A.3.22 richiede che [Organizzazione] protegga i DCP archiviati su, trattati da, o accessibili tramite dispositivi endpoint degli utenti.

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 32 (misure tecniche appropriate per i DCP a riposo — inclusi supporti ed endpoint); Articolo 5(1)(f) (integrità e riservatezza)
- **LPD svizzera** : Articolo 7 (misure tecniche — protezione dei supporti fisici e smaltimento sicuro)
- **ISO/IEC 27701:2025** : Controlli A.3.20, A.3.21, A.3.22 (normativi)

---

# Ciclo di vita dei supporti di archiviazione per i DCP (A.3.20)

## Requisiti dei supporti di archiviazione

[Organizzazione] DEVE gestire i supporti di archiviazione contenenti DCP per tutto il loro ciclo di vita in conformità con lo schema di classificazione definito in PRIV-POL-A.3.5-7.

### Acquisizione e registrazione dei supporti

- Tutti i supporti di archiviazione rimovibili che contengono o potrebbero contenere DCP DEVONO essere registrati nel Registro dei supporti al momento dell'acquisizione
- A ogni supporto registrato DEVE essere assegnato un proprietario (individuo o team responsabile)
- La classificazione del supporto DEVE essere assegnata al primo utilizzo in base al contenuto DCP archiviato

### Supporti in uso

- I supporti di archiviazione contenenti DCP DEVONO essere gestiti in conformità con il livello di classificazione assegnato (per PRIV-POL-A.3.5-7)
- I supporti contenenti DCP LIMITATI (categoria speciale) DEVONO essere cifrati in ogni momento
- I supporti contenenti DCP RISERVATI DEVONO essere cifrati quando vengono trasportati fuori dai locali sicuri
- I supporti contenenti DCP lasciati incustoditi DEVONO essere messi al sicuro (in un'archiviazione chiusa a chiave o in un'apparecchiatura chiusa a chiave) — in linea con i requisiti di scrivania libera di PRIV-POL-A.3.17-19

### Trasporto dei supporti

- Il trasporto di supporti contenenti DCP fuori dai locali sicuri DEVE essere registrato nel log, inclusi destinazione, finalità e data di restituzione
- I supporti contenenti DCP RISERVATI trasportati esternamente DEVONO utilizzare supporti cifrati approvati o un servizio di corriere sicuro approvato
- La perdita di supporti durante il trasporto DEVE essere segnalata immediatamente come incidente DCP per PRIV-POL-A.3.11-12

### Smaltimento dei supporti

- I supporti di archiviazione contenenti DCP NON DEVONO essere smaltiti attraverso i normali flussi di rifiuti
- Prima dello smaltimento, i DCP DEVONO essere rimossi in modo irreversibile utilizzando un metodo appropriato al tipo di supporto: cancellazione crittografica (per supporti completamente cifrati, soggetti alle condizioni di A.3.21), sovrascrittura sicura per **NIST SP 800-88** (lo standard di riferimento principale per la sanitizzazione dei supporti), o distruzione fisica. Nota: gli standard di sovrascrittura multipassaggio come DoD 5220.22-M non sono affidabili per i supporti flash (SSD, USB, eMMC); la cancellazione crittografica per NIST SP 800-88 o la distruzione fisica DEVONO essere utilizzate per tali supporti
- Il metodo di smaltimento DEVE essere documentato nel Registro dei supporti, inclusi il metodo utilizzato, la data e il responsabile
- Lo smaltimento tramite un servizio terzo di distruzione dei supporti DEVE produrre un certificato di distruzione, conservato come prova

---

# Smaltimento e riutilizzo sicuro delle apparecchiature contenenti DCP (A.3.21)

## Requisiti di smaltimento e riutilizzo delle apparecchiature

Prima che qualsiasi apparecchiatura contenente supporti di archiviazione venga smaltita o riutilizzata (all'interno o all'esterno di [Organizzazione]), [Organizzazione] DEVE verificare che tutti i DCP siano stati rimossi o sovrascritti in modo sicuro.

### Verifica pre-smaltimento

Tutte le apparecchiature pianificate per lo smaltimento o la riassegnazione DEVONO subire:

1. **Verifica dell'inventario** : Confermare se i DCP erano o potrebbero essere stati archiviati sui supporti di archiviazione del dispositivo
2. **Cancellazione dei dati** : Sovrascrivere tutta l'archiviazione utilizzando uno standard di cancellazione approvato (per PRIV-IMP-A.3.20-22-TG), o distruggere fisicamente i supporti se la cancellazione non è tecnicamente fattibile
3. **Verifica** : Confermare che la cancellazione sia riuscita (scansione di verifica post-cancellazione)
4. **Documentazione** : Registrare l'identificativo dell'asset del dispositivo, lo stato DCP (DCP presenti/non confermate), il metodo di cancellazione, l'esito della verifica, la data e il responsabile nel Registro di smaltimento

### Standard di cancellazione

Il riferimento principale per la sanitizzazione dei supporti è **NIST SP 800-88 (Guidelines for Media Sanitization)**. Si applicano i seguenti metodi:

- **Cancellazione software (supporti magnetici / HDD)** : Sovrascrittura sicura utilizzando le tecniche Clear o Purge di NIST SP 800-88 appropriate alla sensibilità dei dati. Le tecniche di sovrascrittura multipassaggio (es. DoD 5220.22-M) sono accettabili per gli HDD ma NON DEVONO essere utilizzate come metodo principale per i supporti flash (SSD, USB, eMMC) dove il livellamento dell'usura rende la sovrascrittura inaffidabile
- **Cancellazione crittografica** : La distruzione delle chiavi di cifratura è accettabile come metodo di cancellazione solo laddove la cifratura dell'intero disco fosse confermata attiva dal momento del primo scrittura dei dati su quel supporto, e laddove l'implementazione della cifratura sia validata (es. hardware AES-256). Laddove vi sia incertezza sulla copertura della cifratura, DEVE essere utilizzata la distruzione fisica
- **Distruzione fisica** : Triturazione o smagnetizzazione dei supporti — richiesta per i DCP LIMITATI su supporti flash, e per qualsiasi supporto in cui la cancellazione software non può essere verificata; la distruzione deve essere documentata con il metodo e la persona che conferma

### Riutilizzo all'interno di [Organizzazione]

Prima della riassegnazione di un'apparecchiatura a un altro utente all'interno di [Organizzazione]: tutti i DCP del profilo dell'utente precedente DEVONO essere rimossi; il dispositivo DEVE essere reimpostato alla configurazione di base; DEVE essere creato un nuovo record di accesso utente; l'accesso dell'utente precedente revocato per PRIV-POL-A.3.8-10.

### Smaltimento tramite terze parti

Laddove le apparecchiature vengano smaltite tramite un servizio terzo (riciclatore, rivenditore, associazione di beneficenza): la terza parte DEVE fornire un certificato di distruzione dei dati prima che le apparecchiature lascino la custodia di [Organizzazione]; per le apparecchiature contenenti DCP LIMITATI, è richiesta la distruzione fisica dei supporti (vendita o donazione non consentite senza distruzione confermata); il certificato di distruzione DEVE essere conservato nel Registro di smaltimento per un minimo di 5 anni.

---

# Protezione dei DCP sui dispositivi endpoint degli utenti (A.3.22)

## Requisiti dei dispositivi endpoint per i DCP

[Organizzazione] DEVE garantire che i DCP archiviati su, trattati da, o accessibili tramite dispositivi endpoint degli utenti siano protetti.

### Controlli minimi degli endpoint per i DCP

Tutti i dispositivi endpoint aziendali che archiviano, trattano o accedono ai DCP DEVONO essere configurati con:

- **Cifratura dell'intero disco** : Attiva e applicata; gestione delle chiavi di cifratura per gli standard crittografici (PRIV-POL-A.3.23-31)
- **Blocco dello schermo** : Blocco automatico dopo il periodo di inattività massimo (configurato per PRIV-IMP-A.3.20-22-TG)
- **Capacità di cancellazione remota** : Capacità di cancellazione o blocco remoto registrata per il dispositivo; capacità di cancellazione testata al minimo annualmente
- **Iscrizione alla gestione dei dispositivi** : Iscritto nella soluzione MDM (Mobile Device Management) o UEM (Unified Endpoint Management) aziendale dove tecnicamente fattibile
- **Patch aggiornate** : Patch del sistema operativo e di sicurezza applicate entro i termini definiti in ISMS-POL-A.8.8

### Restrizioni di archiviazione dei DCP sugli endpoint

- Il download o l'archiviazione in massa di DCP sui dispositivi endpoint DEVONO essere limitati a quanto necessario per la funzione lavorativa
- La copia o l'archiviazione di grandi volumi di DCP (esportazione di massa da database o applicazioni) sugli endpoint locali richiede l'approvazione del Proprietario dei dati
- I DCP LIMITATI (categoria speciale) NON DEVONO essere archiviati localmente sugli endpoint se non per necessità operativa con notifica al RPD; laddove archiviati localmente, DEVONO essere in un contenitore cifrato con controlli degli accessi separati dall'accesso generale al file system

### BYOD (Bring Your Own Device)

Laddove i dispositivi personali siano autorizzati ad accedere ai DCP (politica BYOD applicabile): i dispositivi BYOD DEVONO essere iscritti in una soluzione MDM/containerizzazione che crea uno spazio di lavoro DCP gestito, separato dai dati personali; i controlli minimi (cifratura, blocco dello schermo, cancellazione remota) DEVONO applicarsi allo spazio di lavoro gestito; il diritto di [Organizzazione] di cancellare in remoto lo spazio di lavoro gestito DEVE essere concordato per iscritto prima che venga concesso l'accesso ai DCP; i DCP NON DEVONO essere archiviati al di fuori dello spazio di lavoro gestito sui dispositivi BYOD.

### Dispositivi endpoint persi o rubati

La perdita o il furto di un dispositivo endpoint contenente o con accesso ai DCP DEVE essere: segnalato immediatamente al Team Sicurezza IT e al RPD; trattato come un sospetto incidente DCP e gestito per PRIV-POL-A.3.11-12; la cancellazione remota avviata il prima possibile e entro **4 ore** dalla segnalazione della perdita confermata al Team Sicurezza IT. Laddove la cancellazione remota non sia tecnicamente fattibile entro 4 ore (es. il dispositivo è offline), il RPD DEVE essere notificato immediatamente e il ritardo DEVE essere documentato; un'azione compensativa (reimpostazione della password, sospensione dell'account, revoca dell'accesso ai DCP) DEVE essere adottata immediatamente in attesa della conferma della cancellazione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per A.3.20–A.3.22 |
|-------|----------------------------------|
| **RPD** | Definisce i requisiti specifici ai DCP per supporti ed endpoint; notificato dei DCP LIMITATI sugli endpoint; esamina l'adeguatezza del Registro di smaltimento; informato dei dispositivi persi/rubati |
| **RSSI** | Definisce gli standard tecnici di cancellazione, cifratura e gestione degli endpoint; configura MDM/UEM; mantiene il Registro di smaltimento; indaga sui dispositivi persi/rubati |
| **Team Sicurezza IT** | Implementa la cifratura e MDM; esegue lo smaltimento e la cancellazione dei supporti; mantiene il Registro dei supporti e il Registro di smaltimento; avvia la cancellazione remota sui dispositivi persi |
| **Proprietario dei dati** | Approva il download di massa di DCP sugli endpoint; notificato dello smaltimento di supporti contenenti DCP nel proprio dominio |
| **Tutto il personale** | Segnala immediatamente i dispositivi persi o rubati; rispetta i requisiti di schermo libero; limita i DCP al minimo necessario sugli endpoint |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registro dei supporti | Inventario dei supporti rimovibili con DCP, proprietario, classificazione e stato | In corso + 3 anni |
| Log di trasporto dei supporti | Registrazioni dei supporti DCP trasportati fuori dai locali sicuri | 3 anni |
| Registro di smaltimento | Registrazioni di smaltimento delle apparecchiature con stato DCP, metodo di cancellazione, verifica e data | 5 anni |
| Certificati di distruzione | Certificati di distruzione di terze parti per le apparecchiature contenenti DCP | 5 anni |
| Stato di cifratura degli endpoint | Rapporti di configurazione che confermano la cifratura dell'intero disco sui dispositivi aziendali | In corso + 3 anni |
| Registrazioni di iscrizione MDM/UEM | Dispositivi iscritti nella gestione degli endpoint, inclusi gli spazi di lavoro gestiti BYOD | In corso + 3 anni |
| Rapporti di dispositivi persi/rubati | Registrazioni di perdita/furto di dispositivi, azioni di cancellazione remota e valutazioni degli incidenti DCP | 3 anni |

---

# Considerazioni di audit

**Per A.3.20 (Supporti di archiviazione)** : Registro dei supporti con inventario dei supporti DCP; prove che i supporti contenenti DCP siano cifrati (soprattutto DCP LIMITATI); log di trasporto per i supporti spostati fuori dai locali sicuri; registrazioni di smaltimento incluso il metodo di cancellazione e la verifica.

**Per A.3.21 (Smaltimento delle apparecchiature)** : Registro di smaltimento con verifiche dello stato DCP pre-smaltimento; prove del metodo di cancellazione approvato applicato; certificati di distruzione dai servizi di smaltimento di terze parti; nessuno smaltimento di apparecchiature DCP LIMITATI senza distruzione fisica confermata.

**Per A.3.22 (Dispositivi endpoint)** : Rapporti di configurazione della cifratura dell'intero disco; registrazioni di iscrizione MDM/UEM; prove di test di cancellazione remota; accordi scritti BYOD dove i dispositivi personali accedono ai DCP; registrazioni di risposta ai dispositivi persi/rubati con conferma della cancellazione remota.

---

<!-- QA_VERIFIED: 2026-04-03 -->
