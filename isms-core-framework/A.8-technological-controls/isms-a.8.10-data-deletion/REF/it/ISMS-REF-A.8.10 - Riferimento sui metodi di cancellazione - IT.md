<!-- ISMS-CORE:REF:ISMS-REF-A.8.10-IT-deletion-methods-reference:framework:REF:a.8.10 -->
**ISMS-REF-A.8.10 — Riferimento sui metodi di cancellazione**
**Standard di sanificazione dei supporti e selezione degli strumenti (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento sui metodi di cancellazione |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-A.8.10 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | RSSI (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI / Operazioni IT | Riferimento tecnico iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: In base alle esigenze (evoluzione della tecnologia e degli strumenti)  
**Prossima data di revisione**: [Data + 12 mesi]  
**Approvatori**: Responsabile delle Operazioni IT / Architettura di sicurezza (riferimento tecnico, nessuna approvazione SGSI richiesta)

**Distribuzione**: Operazioni IT, Ingegneria della sicurezza, Proprietari dei sistemi (per la consapevolezza tecnica dell'implementazione)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del Sistema di Gestione della Sicurezza delle Informazioni (SGSI).
- Questo documento NON definisce controlli o requisiti di cancellazione obbligatori.
- Questo documento NON stabilisce requisiti vincolanti, scadenze, ICP o SLA.
- Questo documento NON impone l'uso, il divieto o la configurazione di specifici strumenti, fornitori o piattaforme di cancellazione.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

Tutti i requisiti, gli obblighi e le decisioni di governance in materia di cancellazione vincolanti sono definiti esclusivamente in **ISMS-POL-A.8.10 (Politica di cancellazione delle informazioni)** e in altri documenti SGSI approvati.

Questo documento serve esclusivamente come riferimento tecnico per:

- Descrivere i metodi di cancellazione e le tecniche di sanificazione dei supporti comunemente utilizzati
- Tracciare l'evoluzione degli standard di settore e la disponibilità degli strumenti
- Supportare la consapevolezza nella selezione dei metodi di cancellazione
- Informare le discussioni tecniche e la pianificazione futura dell'implementazione
- **Questo documento non deve essere utilizzato come prova di audit dell'implementazione**

L'utilizzo di questo documento non implica implementazione, conformità o maturità operativa.

**Dichiarazione di posizionamento critico**:
Questo documento fornisce intenzionalmente dettagli tecnici che vanno oltre quanto richiesto per la documentazione delle politiche ISO/IEC 27001. Il suo scopo è esclusivamente la consapevolezza tecnica. Nessuna conclusione di audit deve essere tratta dalla presenza, assenza o classificazione di qualsiasi metodo, strumento o fornitore di cancellazione elencato nel presente documento.

---

## Scopo e ambito del documento

**Scopo**

Questo documento fornisce una panoramica tecnica dei metodi di cancellazione e delle tecniche di sanificazione dei supporti comunemente utilizzati per la cancellazione delle informazioni. È inteso a supportare:

- La consapevolezza tecnica delle opzioni di cancellazione disponibili
- La comprensione dell'efficacia dei metodi per tipo di supporto
- Il contesto per la selezione del metodo di cancellazione durante l'implementazione
- Le discussioni sulla pianificazione futura dell'implementazione
- I criteri di valutazione degli strumenti

## Cosa NON è questo documento

Questo documento NON:

- Definisce i metodi di cancellazione approvati o vietati da [Organizzazione]
- Stabilisce requisiti di implementazione obbligatori
- Crea obblighi di conformità o criteri di audit
- Sostituisce i requisiti della politica ISMS-POL-A.8.10
- Impone la selezione di strumenti specifici o relazioni con i fornitori
- Stabilisce procedure di cancellazione o processi di verifica

## Relazione con il SGSI

**Relazione con l'Allegato A di POL-A.8.10**: L'Allegato A di ISMS-POL-A.8.10 (Matrice dei metodi di cancellazione approvati) fornisce lo **standard organizzativo vincolante** per la selezione del metodo di cancellazione. Questo riferimento tecnico (ISMS-REF-A.8.10) fornisce ulteriori dettagli tecnici e contesto a supporto dell'allegato alla politica, ma non sostituisce né estende i requisiti della politica.

Questo documento è un **riferimento tecnico non vincolante**. Tutti i requisiti di controllo della cancellazione sono definiti esclusivamente in ISMS-POL-A.8.10.

Le decisioni di implementazione sono documentate attraverso le procedure ISMS-IMP-A.8.10 sulla base della valutazione del rischio, del contesto operativo e dei requisiti normativi.

## Organizzazione dei contenuti

Questo riferimento organizza i metodi di cancellazione per:

- Tipo di supporto (magnetico, a stato solido, cloud, carta, ottico)
- Metodo di sanificazione (Clear — Svuotamento, Purge — Eliminazione, Destroy — Distruzione)
- Panorama degli strumenti e dei fornitori
- Capacità di cancellazione dei provider cloud
- Allineamento agli standard di settore

---

# Framework di sanificazione NIST SP 800-88

## Panoramica

La Pubblicazione speciale NIST 800-88 Revisione 1 ("Linee guida per la sanificazione dei supporti") fornisce una guida autorevole sui metodi di sanificazione dei supporti. Sebbene sia un riferimento informativo (non obbligatorio a meno che non sia richiesto contrattualmente), rappresenta le migliori pratiche di settore.

**Tre categorie di sanificazione**:

1. **Clear (Svuotamento)**: Applicare tecniche logiche per sanificare i dati in tutte le posizioni di archiviazione indirizzabili dall'utente come protezione contro semplici tecniche di recupero dati non invasive
2. **Purge (Eliminazione)**: Applicare tecniche fisiche o logiche per rendere infeasibile il recupero dei dati di destinazione utilizzando tecniche di laboratorio all'avanguardia
3. **Destroy (Distruzione)**: Rendere il supporto inutilizzabile e infeasibile il recupero dei dati di destinazione utilizzando tecniche di laboratorio all'avanguardia

## Fattori per la selezione del metodo

**Destinazione del supporto**:

- Rimane sotto il controllo dell'organizzazione → Il Clear può essere sufficiente (a seconda della classificazione)
- Lascia il controllo dell'organizzazione → Purge come minimo
- Smaltimento / fine vita → Destroy consigliato per i dati sensibili

**Classificazione dei dati**:

- Dati pubblici → Clear sufficiente
- Dati interni → Clear o Purge
- Dati riservati → Purge come minimo
- Dati limitati → Destroy o Purge con verifica

**Intenzione di riutilizzo del supporto**:

- Riutilizzo all'interno dell'organizzazione → Clear o Purge
- Vendita/donazione esterna → Purge o Destroy
- Smaltimento → Destroy

---

# Cancellazione di supporti magnetici (HDD, nastro)

## Hard Disk Drive (HDD)

**Caratteristiche del supporto**:

- Dati memorizzati magneticamente su piatti rotanti
- L'eliminazione standard dei file rimuove solo i puntatori del file system, non i dati effettivi
- I dati rimangono recuperabili fino alla sovrascrittura
- Metodi di sanificazione consolidati

**Metodi Clear**

**Sovrascrittura a passaggio singolo**:

- Scrivere un pattern su tutte le posizioni indirizzabili
- NIST SP 800-88: Il singolo passaggio è sufficiente per i drive moderni
- I vecchi metodi multi-passaggio (DoD 5220.22-M a 7 passaggi) non sono più necessari per NIST
- Strumenti: `shred` (Linux), `sdelete` (Windows), `dd` (Unix/Linux)
- Efficacia: Adeguata per dati non sensibili, riutilizzo interno
- Limitazioni: Non si rivolge ai settori difettosi o alle aree riservate al firmware

**Metodi Purge**

**ATA Secure Erase**:

- Comando integrato nel drive che sovrascrive tutte le posizioni indirizzabili inclusi i settori rimappati
- Implementato dal produttore, sfrutta la conoscenza da parte del controller del drive di tutte le aree di archiviazione
- Comando singolo, esecuzione rapida (tipicamente 1-4 ore per i drive moderni)
- Strumenti: `hdparm` (Linux), Parted Magic, utility del produttore
- Efficacia: Molto elevata per HDD, metodo consigliato
- Verifica: Controllare i dati SMART o lo stato di completamento del comando ATA

**Degaussing**:

- Esporre il drive a un potente campo magnetico per disturbare i domini magnetici
- Rende il drive permanentemente inutilizzabile (non può essere riutilizzato)
- Richiede un degausser della NSA Evaluated Products List (EPL) per i dati classificati
- Efficacia: Molto elevata per i supporti magnetici
- Limitazioni: Drive inutilizzabile dopo il degaussing, attrezzatura costosa
- Caso d'uso: Ambienti ad alta sicurezza, smaltimento di dati classificati

**Metodi Destroy**

**Disintegrazione fisica**:

- Triturare il drive in piccole particelle (≤2 mm consigliato per DIN 66399)
- Incenerimento ad alta temperatura
- Polverizzazione
- Fusione
- Servizi fornitori: Fornitori di distruzione certificati NAID AAA
- Efficacia: Massima, recupero dei dati infeasibile
- Caso d'uso: Dati a massima sensibilità, smaltimento a fine vita

**Cancellazione crittografica**

**Self-Encrypting Drive (SED)**:

- Crittografia dell'intero disco basata su hardware
- Dati crittografati con Data Encryption Key (DEK)
- DEK crittografata con Authentication Key (AK)
- Sanificazione: Distruggere le chiavi crittografiche
- Strumenti: Utility di gestione SED del produttore, sedutil
- Efficacia: Molto elevata SE la crittografia era abilitata dall'implementazione
- Limitazioni: Efficace solo se il drive era crittografato; verificare lo stato della crittografia prima di fare affidamento sulla cancellazione crittografica

## Nastro magnetico

**Caratteristiche del supporto**:

- Supporto ad accesso sequenziale
- Comune per backup e archiviazione
- Più passaggi di lettura/scrittura sullo stesso supporto

**Metodo Clear**

**Sovrascrittura completa del nastro**:

- Scrivere un pattern sull'intera lunghezza del nastro
- Richiede molto tempo (ore per nastro)
- Strumenti: Comandi nativi di sovrascrittura del tape drive
- Efficacia: Adeguata per il riutilizzo interno
- Limitazione: Molto lenta, non si rivolge ai segmenti di nastro danneggiati

**Metodo Purge**

**Degaussing**:

- Metodo preferito per i supporti a nastro
- Veloce (secondi per nastro)
- Rende il nastro inutilizzabile per uso futuro
- Richiede un degausser NSA EPL per dati sensibili
- Efficacia: Molto elevata
- Caso d'uso: Smaltimento di nastri di backup sensibili, decommissioning

**Metodo Destroy**

**Distruzione fisica**:

- Triturazione
- Incenerimento
- Polverizzazione
- Efficacia: Massima
- Caso d'uso: Fine vita, massima sensibilità

---

# Cancellazione di supporti a stato solido (SSD, NVMe, Flash)

## Caratteristiche dei supporti a stato solido

**Perché gli SSD sono diversi**:

- Gli algoritmi di wear-leveling distribuiscono le scritture su tutte le celle
- L'over-provisioning riserva celle di archiviazione non visibili al sistema operativo
- La garbage collection sposta i blocchi di dati
- Il comando TRIM gestisce i blocchi eliminati
- Risultato: La sovrascrittura standard NON sanifica in modo affidabile gli SSD

**Sfide di sanificazione**:

- Non è possibile garantire che tutte le posizioni di archiviazione fisica siano sovrascritte
- Il firmware controlla il posizionamento effettivo dei dati
- Aree nascoste (over-provisioning, rimappatura dei blocchi difettosi)

## Metodi di sanificazione SSD / NVMe

**Metodi Purge**

**ATA Secure Erase / NVMe Sanitize**:

- Comando implementato dal produttore
- SSD: Comando ATA Security Erase
- NVMe: NVMe Sanitize (Crypto Erase o Block Erase)
- Sfrutta la conoscenza del firmware di tutte le celle di archiviazione
- Strumenti: `nvme-cli` (NVMe), `hdparm` (SATA SSD), Parted Magic
- Efficacia: Elevata (se correttamente implementato dal produttore)
- Verifica: Stato di completamento dello strumento, tentativo di campionamento del recupero dati
- Attenzione: La qualità dell'implementazione varia in base al produttore

**Cancellazione crittografica**:

- Self-Encrypting Drive (SED) o FDE basata su software
- Distruggere la chiave di crittografia per rendere i dati inaccessibili
- Molto veloce (secondi)
- Strumenti: Utility SED del produttore, strumenti FDE del sistema operativo (BitLocker, FileVault, LUKS)
- Efficacia: Molto elevata SE il drive era crittografato dall'implementazione
- **Requisito critico**: Verificare che la crittografia fosse abilitata; la crittografia post-implementazione è meno efficace
- Metodo preferito per gli SSD dove la crittografia è abilitata

**Metodo Destroy**

**Distruzione fisica**:

- Triturare in particelle ≤2 mm
- Disintegrazione
- Polverizzazione
- Incenerimento
- Efficacia: Massima, recupero dati infeasibile
- Caso d'uso: Dati ad alta sensibilità, quando Secure Erase non è verificato efficace
- Nota: Costoso per grandi volumi

**NON raccomandato per gli SSD**

❌ **Sovrascrittura standard**: Inefficace a causa del wear-leveling e dell'over-provisioning
❌ **Strumenti di eliminazione a singolo file**: Non sanificano lo spazio eliminato sugli SSD
❌ **Sovrascrittura a più passaggi**: Nessun beneficio aggiuntivo rispetto al singolo passaggio, spreca cicli di scrittura

## Unità flash USB / Schede SD

**Sanificazione**:

- Sfide simili agli SSD (memoria flash, wear-leveling)
- Secure Erase: Se supportato (raro nei drive USB consumer)
- Cancellazione crittografica: Se crittografato (BitLocker To Go, drive con crittografia hardware)
- **Approccio pratico**: La distruzione fisica è spesso il metodo più affidabile
- Triturare o incenerire per i dati sensibili
- Il basso costo dei supporti rende la distruzione economicamente conveniente

---

# Cancellazione dell'archiviazione cloud

## Sfide della cancellazione cloud

**Multi-tenancy**:

- I dati dei clienti sono logicamente separati ma fisicamente co-ubicati
- Rischio di remanenza dei dati o dispersione cross-tenant
- Dipendenza dai controlli di isolamento del provider

**Distribuzione dei dati**:

- Dati replicati in più posizioni geografiche
- Più zone di disponibilità e regioni
- Copie di backup gestite dal provider

**Controllo limitato**:

- Nessun accesso fisico ai supporti di archiviazione
- Dipendenza dalle API di cancellazione e dalle procedure del provider
- Fiducia nell'implementazione del provider

## Metodi di cancellazione cloud

**Eliminazione logica (Clear)**

**Cancellazione basata su API**:

- Utilizzare l'API del provider cloud per eliminare oggetti, volumi, database
- Esempi: AWS S3 DeleteObject, Azure Blob Delete, GCP Storage Delete
- Verifica: Codici di risposta API (200/204 successo)
- Efficacia: Rimuove l'accesso logico, il provider elimina l'archiviazione fisica secondo la propria pianificazione
- Limitazione: Fiducia nel provider per la sanificazione fisica dell'archiviazione

**Cancellazione crittografica (Purge — Preferita)**

**Chiavi di crittografia gestite dal cliente**:

- Crittografare i dati con chiavi gestite dal cliente (CMK)
- AWS: KMS Customer Managed Keys, S3 SSE-C
- Azure: Customer Managed Keys (CMK), Azure Key Vault
- GCP: Customer-Managed Encryption Keys (CMEK)
- Cancellazione: Distruggere le chiavi di crittografia, rendendo i dati inaccessibili
- Verifica: Confermare la cancellazione della chiave nel servizio di gestione delle chiavi
- Efficacia: Molto elevata, i dati sono crittograficamente irrecuperabili
- **Approccio consigliato**: Combinare la cancellazione tramite API con la distruzione della chiave

**Certificati di cancellazione del provider**

Alcuni provider cloud offrono attestazioni di cancellazione:

- AWS: Conferma della cancellazione tramite log CloudTrail
- Azure: Log di audit
- GCP: Cloud Audit Logs
- Certificazione di terze parti: Rapporti SOC 2 Tipo II che coprono i controlli di cancellazione
- Caso d'uso: Prova contrattuale della cancellazione, conformità normativa

## Cancellazione del provider cloud per tipo di servizio

**IaaS (Calcolo, Archiviazione)**:

- Macchine virtuali: Terminare l'istanza + eliminare volumi EBS/dischi gestiti
- Archiviazione oggetti: Eliminare oggetti tramite API + eliminare il bucket + distruggere CMK
- Archiviazione a blocchi: Eliminare volumi + snapshot + backup
- Verifica: Risposte API, conferma dalla console del servizio

**PaaS (Database, Applicazioni)**:

- Database: Eliminare l'istanza del database + backup automatici + snapshot manuali
- Servizi applicativi: Eliminare l'applicazione + archivi dati + log
- Verifica: Conferme di cancellazione specifiche del servizio

**SaaS (Applicazioni)**:

- Cancellazione a livello di applicazione (es. eliminare l'account utente nell'app SaaS)
- Richiedere l'esportazione dei dati prima della cancellazione (portabilità RGPD)
- Ottenere la conferma della cancellazione dal provider SaaS
- Limitazione: Controllo minimo, piena dipendenza dalle procedure del provider

---

# Dispositivi mobili

## Smartphone e tablet

**Approccio alla sanificazione**:

**Dispositivi crittografati** (iOS moderno, Android con crittografia abilitata):
1. Cancellazione remota tramite Mobile Device Management (MDM)
2. Ripristino delle impostazioni di fabbrica
3. Distruzione della chiave di crittografia
4. Verifica: Conferma dalla console MDM, tentativo di accesso al dispositivo
5. Efficacia: Elevata per i dispositivi correttamente crittografati

**Crittografia non abilitata o stato di crittografia sconosciuto**:
1. Distruzione fisica del componente di archiviazione (rimuovere e triturare)
2. Caso d'uso: Dati ad alta sensibilità su dispositivi meno recenti
3. Efficacia: Massima

**Strumenti**:

- Soluzioni MDM: Microsoft Intune, Jamf Pro, VMware Workspace ONE, MobileIron
- Nativi: iOS "Cancella tutto il contenuto e le impostazioni", Android Ripristino impostazioni di fabbrica
- Verifica: Tentativo di check-in MDM dopo la cancellazione

## Laptop e desktop

**Sanificazione**:

- HDD magnetico: ATA Secure Erase o distruzione fisica
- SSD: Cancellazione crittografica (BitLocker, FileVault) o distruzione fisica
- Ibrido (HDD + cache SSD): Sanificare entrambi i componenti
- Approccio: Rimuovere il supporto di archiviazione, sanificare separatamente utilizzando metodi specifici per il supporto

---

# Carta e supporti ottici

## Documenti cartacei

**Standard di triturazione** (DIN 66399):

| Livello di sicurezza | Dimensione delle particelle | Caso d'uso |
|---------------|---------------|------------|
| P-1 | <12 mm a strisce | Rifiuti generici, nessuna riservatezza |
| P-2 | <6 mm a strisce | Documenti interni, bassa sensibilità |
| P-3 | <2 mm a strisce o particelle da 320 mm² | Documenti aziendali riservati |
| **P-4** | <2 mm a strisce o particelle da 160 mm² | **Dati riservati, DCP (minimo consigliato)** |
| **P-5** | <0,8 mm a strisce o particelle da 30 mm² | **DCP altamente sensibili, dati limitati** |
| P-6 | <1 mm a strisce o particelle da 10 mm² | Dati governativi classificati |
| P-7 | Particelle ≤5 mm² | Dati top secret |

**Metodi**:

- Triturazione a taglio incrociato (minimo P-4 o P-5 per i dati sensibili)
- Grandi volumi: Servizio di distruzione in appalto (fornitore certificato NAID AAA)
- Certificato di distruzione richiesto per documenti riservati/limitati

**In loco vs. Fuori sede**:

- Triturazione in loco: Distruzione immediata, catena di custodia mantenuta
- Triturazione fuori sede: Bidoni chiusi a chiave, raccolta programmata, certificato fornito
- Alta sensibilità: Preferire la distruzione testimoniata in loco

## Supporti ottici (CD, DVD, Blu-ray)

**Caratteristiche**:

- Supporti di scrittura unica (non possono essere sovrascritti)
- Richiesta distruzione fisica

**Metodi**:

- Triturazione fisica (piccole particelle)
- Incenerimento
- Disintegrazione
- NON ACCETTABILE: Graffiatura, rottura (i dati sono spesso recuperabili)

---

# Ambienti virtuali

## Macchine virtuali

**Ambito della cancellazione**:

- File del disco virtuale (VMDK, VHD, VHDX, qcow2)
- Snapshot (tutti i file degli snapshot)
- Template (template VM creati da questa VM)
- File di configurazione
- File di swap

**Metodi**:

- **Standard**: Eliminare la VM + tutti i file associati tramite hypervisor
- **Sicuro**: Cancellazione sicura dei file del disco virtuale prima dell'eliminazione della VM
- **Crypto Erase**: Se il disco virtuale è crittografato, distruggere la chiave di crittografia
- Strumenti: Gestione dell'hypervisor (vSphere, Hyper-V, KVM), `shred` per i file del disco

## Container e immagini container

**Ambito della cancellazione**:

- Istanze di container
- Immagini container (locale e registro)
- Volumi persistenti
- Segreti e configurazione

**Metodi**:

- Fermare e rimuovere i container: `docker rm`, `kubectl delete pod`
- Eliminare le immagini: `docker rmi`, eliminazione dal registro
- Eliminare i volumi: `docker volume rm`, `kubectl delete pvc`
- Pulizia del registro: Rimuovere le immagini dal registro container

## Database

**Metodi di cancellazione**:

**Cancellazione logica**:

- `DELETE FROM tabella WHERE ...` (rimuove le righe)
- `DROP TABLE` (rimuove la struttura della tabella e i dati)
- `DROP DATABASE` (rimuove l'intero database)
- Follow-up: `VACUUM` (PostgreSQL), `OPTIMIZE TABLE` (MySQL) per recuperare spazio
- Limitazione: I dati possono persistere nei log delle transazioni, nei file temporanei

**Cancellazione crittografica** (Transparent Data Encryption abilitata):

- Eliminare il database crittografato
- Distruggere la chiave di crittografia
- Efficacia: Elevata per i database con TDE abilitata
- Esempi: SQL Server TDE, Oracle TDE, PostgreSQL pgcrypto

**Cancellazione fisica**:

- Eliminare i file del database dopo la cancellazione logica
- Cancellazione sicura del supporto di archiviazione sottostante
- Includere log delle transazioni, file di backup, file temporanei

**Cancellazione dei backup**:

- Critico: Eliminare i backup del database quando il database di produzione viene eliminato
- Include backup completi, differenziali, log delle transazioni, snapshot

---

# Esempi di strumenti approvati (Informativo)

**⚠️ AVVERTENZA CRITICA**: Gli strumenti e i fornitori elencati in questa sezione sono forniti **esclusivamente a scopo di sensibilizzazione**. La loro inclusione NON costituisce:
- Approvazione o raccomandazione da parte di [Organizzazione]
- Supporto di prodotti o fornitori specifici
- Certificazione che gli strumenti soddisfano i requisiti di [Organizzazione]
- Garanzia di efficacia o idoneità degli strumenti

[Organizzazione] seleziona gli strumenti di cancellazione attraverso una valutazione formale basata sulla valutazione del rischio, i requisiti operativi, la conformità normativa e la validazione del fornitore per ISMS-IMP-A.8.10.2 (Valutazione dei metodi di cancellazione). La selezione degli strumenti NON è definita in questo documento di riferimento.

## Strumenti open source / integrati

**Sovrascrittura**:

- `shred` (Linux) - sovrascrittura di file e drive
- `dd` (Unix/Linux) - scrittura e cancellazione di dischi
- `sdelete` (Windows Sysinternals) - eliminazione sicura
- `wipe` (Linux) - eliminazione sicura dei file

**Secure Erase**:

- `hdparm` (Linux) - ATA Secure Erase per HDD/SSD
- `nvme-cli` (Linux) - comandi NVMe Sanitize
- Parted Magic (Linux avviabile) - suite di sanificazione dei drive

**Crittografia**:

- BitLocker (Windows) - crittografia dell'intero disco
- FileVault (macOS) - crittografia dell'intero disco
- LUKS (Linux) - crittografia del disco
- VeraCrypt - crittografia multipiattaforma

## Strumenti commerciali

**Software di cancellazione enterprise**:

- Blancco Drive Eraser - cancellazione dati certificata, generazione di certificati
- White Canyon WipeDrive - cancellazione di drive multipiattaforma
- DBAN (Darik's Boot and Nuke) - cancellazione HDD gratuita (legacy, non mantenuto)
- Ontrack Eraser - soluzione di cancellazione certificata

**Attrezzatura per la distruzione fisica**:

- Degausser: Garner, Proton Data Security, VS Security Products
- Trituratori: HSM, Whitaker Brothers, SEM, MBM

**Soluzioni MDM**:

- Microsoft Intune
- Jamf Pro (dispositivi Apple)
- VMware Workspace ONE
- MobileIron / Ivanti

## Strumenti nativi cloud

**AWS**:

- AWS CLI (operazioni di eliminazione)
- AWS KMS (gestione e distruzione delle chiavi)
- AWS Backup (eliminazione dei backup)

**Azure**:

- Azure CLI / PowerShell (operazioni di eliminazione)
- Azure Key Vault (gestione delle chiavi)
- Azure Backup (eliminazione dei backup)

**GCP**:

- gcloud CLI (operazioni di eliminazione)
- Cloud KMS (gestione delle chiavi)
- Cloud Backup (eliminazione dei backup)

---

# Capacità di cancellazione dei provider cloud

**Nota sulla pertinenza**: Le capacità dei provider cloud evolvono rapidamente. Questo riferimento riflette le capacità alla data del [Data del documento]. Le organizzazioni DEVONO verificare le attuali capacità di cancellazione del provider durante la valutazione del provider cloud per ISMS-POL-A.8.10 Sezione 2.3 (Valutazione della cancellazione del provider di servizi cloud) e documentare i risultati in ISMS-REF-A.5.23 (Registro dei provider di servizi cloud).

Le seguenti capacità sono fornite esclusivamente a scopo di sensibilizzazione:

## Provider Hyperscale (Tier 1)

**Amazon Web Services (AWS)**:

- API di cancellazione: S3 DeleteObject, EC2 TerminateInstances, RDS DeleteDBInstance
- Crittografia: KMS chiavi gestite dal cliente (CMK)
- Verifica: Log CloudTrail, risposte API
- Certificazioni: SOC 2 Tipo II, ISO 27001, ISO 27017, ISO 27018

**Microsoft Azure**:

- API di cancellazione: Storage Delete, VM Delete, SQL Database Delete
- Crittografia: Customer-Managed Keys (CMK) tramite Azure Key Vault
- Verifica: Log di Azure Monitor, log delle attività
- Certificazioni: SOC 2 Tipo II, ISO 27001, ISO 27017, ISO 27018

**Google Cloud Platform (GCP)**:

- API di cancellazione: Storage Delete, Compute Instance Delete, Cloud SQL Delete
- Crittografia: Customer-Managed Encryption Keys (CMEK)
- Verifica: Cloud Audit Logs, logging Stackdriver
- Certificazioni: SOC 2 Tipo II, ISO 27001, ISO 27017, ISO 27018

**Capacità comuni**:

- Cancellazione programmatica basata su API
- Chiavi di crittografia gestite dal cliente
- Registrazione di audit delle operazioni di cancellazione
- Supporto alla cancellazione multi-regione
- Certificazioni che coprono i controlli di cancellazione

## Altri provider cloud

Per i provider Tier 2-10 per ISMS-REF-A.5.23:

- Valutare le capacità di cancellazione durante la valutazione del fornitore
- Richiedere SLA di cancellazione nel contratto
- Ottenere certificati o attestazioni di cancellazione
- Verificare le procedure di isolamento multi-tenant
- Esaminare i rapporti SOC 2 Tipo II per i controlli di cancellazione

---

# Verifica e validazione

## Metodi di verifica

**Verifica automatizzata**:

- Stato di completamento dello strumento (codici di uscita, log)
- Codici di risposta API (HTTP 200/204 per la cancellazione riuscita)
- Conferma dalla console MDM (cancellazione dei dispositivi mobili)
- Log del sistema di gestione delle chiavi (distruzione della chiave di crittografia)

**Verifica manuale**:

- Campionamento: Selezionare supporti casuali, tentare il recupero dei dati
- Validazione forense: Utilizzare strumenti di recupero sui supporti sanificati
- Ispezione visiva: Verifica della distruzione fisica
- Revisione dei certificati: Certificati di distruzione di terze parti

**Verifica di terze parti**:

- Certificati di distruzione da fornitori certificati
- Rapporti di audit SOC 2 Tipo II (verifica del controllo della cancellazione)
- Attestazioni di cancellazione del provider cloud

## Linee guida per il campionamento

Per operazioni di cancellazione su larga scala:

- Campionare il 5-10% degli eventi di cancellazione
- Campionamento più elevato (10-20%) per i dati ad alta sensibilità
- Concentrare il campionamento su nuovi metodi o strumenti di cancellazione
- Documentare i risultati del campionamento e gli eventuali errori

## Gestione degli errori

Se la verifica non riesce:

- Interrompere immediatamente l'uso del metodo di cancellazione
- Mettere in quarantena il supporto per la ri-sanificazione
- Escalare al team di sicurezza IT
- Utilizzare un metodo di cancellazione più robusto (es. distruzione fisica)
- Documentare l'errore per gli insegnamenti appresi

---

# Riferimento agli standard di settore

**Pubblicazioni speciali NIST**:

- **NIST SP 800-88 Rev. 1**: Linee guida per la sanificazione dei supporti (riferimento principale)
- NIST SP 800-53 Rev. 5: Controlli di sicurezza (famiglia MP - Protezione dei supporti)
- NIST SP 800-171: Protezione delle CUI (requisiti di sanificazione dei supporti)

**Standard ISO**:

- ISO/IEC 27040:2015: Sicurezza dell'archiviazione (linee guida sulla sanificazione)
- ISO/IEC 27555:2021: Linee guida sulla cancellazione delle DCP
- ISO/IEC 27017:2015: Sicurezza dei servizi cloud (requisiti di cancellazione)

**Standard di settore**:

- **DIN 66399**: Distruzione dei supporti dati (livelli di triturazione della carta)
- IEEE 2883-2022: Standard per la sanificazione dell'archiviazione
- ANSI/NAID AAA: Standard di distruzione sicura (fornitori di servizi)

**Riferimenti legacy** (superati ma possono comparire nei contratti):

- DoD 5220.22-M: Sanificazione dei dati (superato da NIST SP 800-88)
- NSA/CSS Manual 130-2: Sanificazione dei dati (dati classificati, superato)

---

# Appendice A: Foglio di lavoro per la selezione del metodo di cancellazione

Le organizzazioni possono utilizzare questo foglio di lavoro durante l'implementazione per documentare le decisioni sui metodi di cancellazione:

**Categoria di dati**: _______________________  
**Livello di classificazione**: ☐ Pubblico ☐ Interno ☐ Riservato ☐ Limitato

**Tipo di supporto**: _______________________  
**Destinazione del supporto**: ☐ Riutilizzo interno ☐ Trasferimento esterno ☐ Smaltimento

**Metodo consigliato** (basato su NIST SP 800-88 e classificazione dei dati):

- Clear: _______________________
- Purge: _______________________
- Destroy: _______________________

**Metodo selezionato**: _______________________  
**Giustificazione**: _______________________

**Strumento/Fornitore**: _______________________  
**Metodo di verifica**: _______________________

**Approvato da**: _______________________  
**Data**: _______________________

**Flusso di approvazione**:
- Fattibilità tecnica esaminata da: _______________________ (Operazioni IT)
- Valutazione del rischio esaminata da: _______________________ (Team di sicurezza)
- Approvazione finale per POL-A.8.10 Sezione 2.2 da: _______________________ (RSSI o delegato)

**Nota**: Questo foglio di lavoro supporta le decisioni di selezione del metodo di cancellazione documentate in ISMS-IMP-A.8.10.2 (Valutazione dei metodi di cancellazione). I fogli di lavoro completati vengono archiviati con le prove di implementazione.

---

**FINE DEL RIFERIMENTO TECNICO**

---

*Questo riferimento tecnico supporta l'implementazione di ISMS-POL-A.8.10. Tutti i requisiti vincolanti sono definiti nel documento di politica.*

<!-- QA_VERIFIED: 2026-04-04 -->
