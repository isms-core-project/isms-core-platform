<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.8-9-IT:framework:POL:a.7.8-9 -->
**ISMS-POL-A.7.8-9 — Posizionamento e protezione delle apparecchiature**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Posizionamento e protezione delle apparecchiature |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.7.8-9 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale

**Catena di approvazione**: Principale: RSSI; Secondario: Responsabile delle strutture; Autorità finale: Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-POL-A.7.1-3; ISMS-POL-A.7.4-5-11; ISMS-IMP-A.7.8-9-S1–S3-UG/TG; ISO/IEC 27001:2022 Controlli A.7.8, A.7.9.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per il posizionamento e la protezione delle apparecchiature, affrontando sia il posizionamento delle apparecchiature on-premise sia la sicurezza degli asset quando utilizzati fuori sede.

**Approccio a controlli combinati**: I Controlli A.7.8 (Posizionamento e protezione delle apparecchiature) e A.7.9 (Sicurezza degli asset fuori sede) sono implementati insieme perché affrontano aspetti complementari della protezione delle apparecchiature durante il loro ciclo di vita operativo, sia on-premise sia fuori sede.

**Allineamento normativo**: nLPD svizzera (Art. 8); ISO/IEC 27001:2022; RGPD dell'UE, FINMA, DORA, NIS2 (applicabilità condizionale).

---

# Allineamento sul controllo

**A.7.8 — Posizionamento e protezione delle apparecchiature**: Le apparecchiature devono essere posizionate in modo sicuro e protette.

**A.7.9 — Sicurezza degli asset fuori sede**: Gli asset fuori sede devono essere protetti.

---

# Requisiti di posizionamento delle apparecchiature (A.7.8)

## Posizionamento sicuro

Le apparecchiature che elaborano o archiviano informazioni sensibili DEVONO essere posizionate per ridurre i rischi derivanti da minacce fisiche e ambientali e dall'accesso non autorizzato:

**Selezione dell'ubicazione**:

- Le apparecchiature DEVONO essere posizionate in aree con accesso controllato
- Le apparecchiature critiche DEVONO essere lontane dalle aree pubbliche
- Le apparecchiature DEVONO essere posizionate per ridurre al minimo il rischio di osservazione (shoulder surfing)
- Gli schermi che visualizzano informazioni sensibili DEVONO essere posizionati lontano da finestre e aree ad alto traffico

**Considerazioni ambientali**:

- Le apparecchiature DEVONO essere protette da temperature estreme, umidità, polvere e vibrazioni
- Devono essere forniti ventilazione e raffreddamento adeguati; i criteri di accettazione (intervalli di temperatura, obiettivi di autonomia UPS per livello di apparecchiatura) sono definiti in ISMS-IMP-A.7.8-9.1
- Le apparecchiature DEVONO essere sollevate o protette dove esiste un rischio di alluvione
- Il fumo, il cibo e le bevande DEVONO essere vietati vicino alle apparecchiature sensibili

**Misure di sicurezza**:

- Le apparecchiature DEVONO essere in aree con controlli di accesso fisico appropriati
- L'instradamento dei cavi DEVE essere protetto dall'accesso o dal danneggiamento non autorizzato
- Le apparecchiature DEVONO essere chiaramente etichettate con tag asset (tranne dove ciò crea un rischio di sicurezza)

## Protezione dell'alimentazione e della cablatura

**Alimentazione**: Le apparecchiature DEVONO essere protette da guasti di alimentazione utilizzando sistemi UPS appropriati; i cavi di alimentazione DEVONO essere protetti dall'intercettazione o dal danneggiamento; gli interruttori di emergenza dell'alimentazione DEVONO essere posizionati vicino alle sale apparecchiature; le forniture di alimentazione DEVONO essere ridondanti per le apparecchiature critiche.

**Cablatura di rete**: I cavi di rete DEVONO essere protetti dall'intercettazione o dal danneggiamento; i percorsi dei cavi DEVONO essere documentati e rivisti almeno annualmente e in caso di modifiche sostanziali; gli armadi di cablatura DEVONO avere controlli di accesso appropriati.

## Colocation e data center di terze parti

Dove le apparecchiature sono ospitate in colocation o data center di terze parti: [Organizzazione] DEVE garantire che il posizionamento, l'accesso fisico e le protezioni ambientali siano implementate tramite requisiti contrattuali e garanzia periodica (es. report SOC 2, certificazione ISO 27001); le prove di conformità delle terze parti DEVONO essere conservate nel repository Supplier Assurance e collegate al record rilevante.

---

# Sicurezza degli asset fuori sede (A.7.9)

## Autorizzazione e monitoraggio

**Autorizzazione alla rimozione**:

- La rimozione delle apparecchiature dai locali DEVE essere autorizzata dalla direzione appropriata
- I documenti di autorizzazione DEVONO includere: dettagli dell'apparecchiatura, scopo, persona responsabile, data di ritorno prevista
- La rimozione di apparecchiature di alto valore o sensibili richiede l'approvazione del responsabile diretto

**Monitoraggio degli asset**:

- Le apparecchiature rimosse dai locali DEVONO essere registrate nel sistema di gestione degli asset
- La catena di custodia DEVE essere mantenuta quando le apparecchiature vengono trasferite tra persone
- Il ritorno delle apparecchiature DEVE essere verificato e registrato

## Requisiti di protezione fuori sede

**Sicurezza fisica**:

- Le apparecchiature NON DEVONO essere lasciate incustodite in luoghi pubblici
- Le apparecchiature DEVONO essere trasportate in borse anonime
- Le apparecchiature DEVONO essere messe al sicuro nelle casseforti dell'hotel o nell'archiviazione chiusa a chiave quando non in uso
- L'archiviazione in veicoli DEVE essere utilizzata solo quando assolutamente necessario (bagagliaio, non visibile)

**Prevenzione dei furti**:

- Le apparecchiature DEVONO essere fisicamente protette dove possibile (cavi di sicurezza, piastre di bloccaggio)
- Il monitoraggio GPS o i servizi di localizzazione DEVONO essere abilitati sui dispositivi supportati dove legalmente consentito, approvato e proporzionato; la configurazione DEVE ridurre al minimo il monitoraggio dei dipendenti ed essere documentata nella politica interna sulla privacy con un'appropriata nota di trasparenza agli utenti
- La capacità di cancellazione remota DEVE essere configurata su tutti i dispositivi mobili supportati e DEVE essere testata almeno annualmente e dopo modifiche significative al MDM; le prove dei test DEVONO essere conservate
- I numeri di serie delle apparecchiature DEVONO essere registrati per le segnalazioni alla polizia in caso di furto

## Lavoro da remoto

**Requisiti per l'home office**: Le apparecchiature DEVONO essere archiviate in modo sicuro quando non in uso; le connessioni di rete DEVONO essere protette (WiFi cifrato, VPN); i familiari e i visitatori NON DEVONO avere accesso alle apparecchiature organizzative; i blocchi fisici dello schermo DEVONO essere utilizzati quando ci si allontana.

**Spazi pubblici**: Gli schermi per la privacy DEVONO essere utilizzati quando si lavora con informazioni sensibili; il WiFi pubblico DEVE essere utilizzato solo con la protezione VPN; le connessioni Bluetooth e wireless DEVONO essere disabilitate quando non richieste; le apparecchiature NON DEVONO mai essere lasciate incustodite.

## Apparecchiature permanentemente fuori sede

Dove [Organizzazione] dispone apparecchiature permanentemente installate al di fuori dei locali organizzativi (es. appliance edge presso siti di clienti, sensori remoti), è richiesta una protezione avanzata: il rilevamento di manomissioni fisiche DEVE essere implementato; il monitoraggio ambientale DEVE essere continuo; DEVONO essere stabiliti calendari regolari di ispezione fisica; le capacità di monitoraggio e gestione remota DEVONO essere abilitate.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per il posizionamento e la protezione delle apparecchiature |
|-------|---------------------------------------------------------------------------|
| **Direzione generale** | Approvare la politica, allocare risorse per la protezione delle apparecchiature |
| **RSSI** | Proprietà della politica, standard di sicurezza per la protezione delle apparecchiature |
| **Responsabile delle strutture** | Posizionamento on-premise delle apparecchiature, controlli ambientali |
| **Operazioni IT** | Dispiegamento delle apparecchiature, monitoraggio degli asset, gestione remota |
| **Responsabili diretti** | Autorizzare la rimozione delle apparecchiature, garantire la conformità del team |
| **Tutto il personale** | Proteggere le apparecchiature in custodia, segnalare gli incidenti di sicurezza |

---

# Metriche di governance

- Apparecchiature con posizionamento conforme (obiettivo: 100%)
- Apparecchiature fuori sede con monitoraggio (obiettivo: 100%)
- Perdite/furti di apparecchiature (obiettivo: 0)
- Ritorni di apparecchiature in ritardo (obiettivo: <5)
- Capacità di cancellazione remota abilitata (obiettivo: 100% per i dispositivi mobili)

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Posizionamento delle apparecchiature** | Il posizionamento sicuro delle apparecchiature di elaborazione delle informazioni |
| **Asset fuori sede** | Apparecchiature organizzative utilizzate al di fuori delle strutture organizzative |
| **Catena di custodia** | Trasferimento documentato della responsabilità delle apparecchiature tra persone |
| **Cancellazione remota** | Capacità di cancellare i dati da un dispositivo da remoto |
| **Rilevamento di manomissioni** | Meccanismi per rilevare l'accesso fisico non autorizzato alle apparecchiature |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data da definire] |
| **Responsabile delle strutture** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per il posizionamento e la protezione delle apparecchiature. Le procedure di attuazione sono documentate in ISMS-IMP-A.7.8-9 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
