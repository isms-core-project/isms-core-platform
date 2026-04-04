<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.1-3-IT:operational:OP-POL:a.7.1-3 -->
**ISMS-OP-POL-A.7.1-3 — Controllo degli accessi fisici**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Controllo degli accessi fisici |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.7.1-3 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 0.1 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 0.1 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controlli A.7.1, A.7.2, A.7.3
- ISO/IEC 27002:2022 Sezioni 7.1, 7.2, 7.3 — Linee guida di attuazione
- ISMS-OP-POL-A.7.4-5-11 — Sicurezza delle infrastrutture fisiche
- ISMS-OP-POL-A.7.6-7-14 — Gestione delle informazioni e dei supporti
- ISMS-OP-POL-A.7.8-9 — Sicurezza dell'ubicazione delle attrezzature
- ISMS-OP-POL-A.5.15-16-18 — Gestione delle identità e degli accessi
- ISMS-OP-POL-A.5.24-28 — Gestione degli incidenti

**Controlli correlati dell'Allegato A**:

| Controllo | Relazione con il controllo degli accessi fisici |
|-----------|------------------------------------------------|
| A.7.4 Monitoraggio della sicurezza fisica | Monitoraggio dei perimetri e dei punti di ingresso definiti in questa politica |
| A.7.5 Protezione dalle minacce fisiche e ambientali | Protezione ambientale per le aree protette da questa politica |
| A.7.6 Lavoro in aree sicure | Requisiti comportamentali all'interno delle zone definite in questa politica |
| A.7.8 Ubicazione e protezione delle attrezzature | Posizionamento delle attrezzature all'interno delle aree protette |
| A.5.15-16-18 Gestione delle identità e degli accessi | Integrazione degli accessi logici con i controlli degli accessi fisici |
| A.5.24-28 Ciclo di vita della gestione degli incidenti | Percorso di escalation per gli eventi di sicurezza fisica |
| A.6.7 Lavoro da remoto | Il lavoro da remoto riduce il numero di accessi in sede |
| A.8.12 Prevenzione della perdita di dati | I controlli fisici integrano le misure tecniche di DLP |

---

# Politica sul controllo degli accessi fisici

## Scopo

Questa politica stabilisce i requisiti dell'organizzazione per il controllo degli accessi fisici, coprendo i perimetri di sicurezza, i controlli di ingresso fisico e la messa in sicurezza di uffici, stanze e strutture. Definisce le zone di sicurezza, i requisiti di autenticazione, le procedure di gestione dei visitatori e le misure di protezione delle strutture necessarie per prevenire l'accesso fisico non autorizzato alle sedi organizzative e agli asset informativi.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) archiviati o trattati nelle sedi organizzative. Nei casi in cui l'organizzazione tratti dati di persone nell'UE/SEE, si applicano altresì i requisiti dell'Art. 32 del RGPD per la sicurezza fisica del trattamento.

I Controlli A.7.1 (Perimetri di sicurezza fisica), A.7.2 (Ingresso fisico) e A.7.3 (Messa in sicurezza di uffici, stanze e strutture) sono combinati in quanto formano un quadro integrato di sicurezza fisica: i perimetri definiscono i confini, i controlli di ingresso proteggono l'attraversamento di tali confini e le misure di sicurezza interna proteggono le aree specifiche al loro interno.

**Organizzazioni esclusivamente cloud**: Le organizzazioni che operano interamente su infrastruttura cloud, senza sale server o data center di proprietà o in locazione, devono comunque applicare questa politica alle sedi degli uffici, agli spazi di coworking e a qualsiasi luogo in cui si accede fisicamente a informazioni organizzative o le si archivia. I requisiti per le sale server e i data center si applicano solo dove l'organizzazione controlla tali strutture; per i data center di terze parti e la colocation, si applicano i requisiti di garanzia del fornitore.

## Ambito di applicazione

Questa politica si applica a:

- Tutte le sedi di proprietà, in locazione o gestite, inclusi uffici, data center e siti remoti.
- Tutte le aree: reception pubblica, spazi ufficio generali, sale server, data center, archivi sicuri e locali d'archivio.
- Tutti i punti di ingresso: ingressi principali, porte secondarie, uscite di emergenza, aree di carico e consegna, finestre e punti di accesso al tetto.
- Tutto il personale: dipendenti, collaboratori esterni, visitatori, personale di manutenzione e personale di consegna.

Escluso dall'ambito:

- Sistemi di monitoraggio e sorveglianza della sicurezza fisica (coperti da A.7.4).
- Protezione ambientale — antincendio, acqua, temperatura (coperta da A.7.5).
- Ubicazione delle attrezzature e sicurezza fuori sede (coperta da A.7.8-9).
- Servizi di supporto (coperti da A.7.11).

## Principio

La sicurezza fisica DEVE essere progettata secondo un approccio di difesa in profondità con zone di sicurezza concentriche, dove ogni zona successiva richiede un'autenticazione e un'autorizzazione più robuste. L'accesso DEVE essere concesso secondo il principio del privilegio minimo — il personale riceve l'accesso solo alle zone necessarie per svolgere il proprio ruolo. Tutti gli accessi fisici DEVONO essere registrati, regolarmente riesaminati e prontamente revocati quando non più necessari. L'organizzazione promuove una cultura di consapevolezza della sicurezza in cui tutto il personale è tenuto a interpellare le persone non riconosciute nelle aree protette e a segnalare le preoccupazioni di sicurezza fisica senza timore di ritorsioni.

---

## Perimetri di sicurezza fisica (A.7.1)

**ISO/IEC 27001:2022 Allegato A.7.1 — Perimetri di sicurezza fisica**:

> *I perimetri di sicurezza dovrebbero essere definiti e utilizzati per proteggere le aree che contengono informazioni e altri asset associati.*

### Modello delle zone di sicurezza

L'organizzazione DEVE definire e documentare le zone di sicurezza utilizzando la seguente classificazione:

| Zona | Descrizione | Aree di esempio | Popolazione di accesso |
|------|-------------|-----------------|------------------------|
| **Zona pubblica** | Accessibile al pubblico generale | Ingresso reception, aree di attesa visitatori, spazi esterni | Tutte le persone |
| **Zona controllata** | Solo personale autorizzato | Aree ufficio generali, sale riunioni, aree comuni | Dipendenti, visitatori con accompagnatore |
| **Zona riservata** | Accesso limitato, in base alla necessità di sapere | Uffici dirigenziali, RU, finanza, legale, archivio documenti | Personale nominativo con esigenza aziendale |
| **Zona ad alta sicurezza** | Accesso rigorosamente controllato | Sale server, data center, operazioni di sicurezza, locali blindati/casseforti | Personale nominativo con autorizzazione esplicita |

Ogni zona DEVE essere documentata sulle planimetrie con confini chiaramente marcati, punti di accesso e meccanismi di controllo degli accessi in uso.

### Requisiti di costruzione del perimetro

**Perimetro dell'edificio (esterno)**:

- Le pareti esterne, i tetti e i pavimenti DEVONO essere di costruzione solida appropriata al rischio.
- Le porte esterne DEVONO essere protette da serrature e meccanismi di controllo degli accessi (ad es., lettori di badge del [Sistema di controllo degli accessi], serrature elettroniche).
- Le finestre DEVONO essere protette, in particolare al piano terra; le finestre al piano terra in prossimità di Zone riservate o ad alta sicurezza DEVONO essere rinforzate o dotate di vetri di sicurezza.
- Le uscite di emergenza DEVONO essere allarmate e monitorate; le uscite di emergenza NON DEVONO essere utilizzabili per l'ingresso ordinario dall'esterno.
- Tutte le porte antincendio sul perimetro di sicurezza DEVONO essere allarmate, monitorate e testate congiuntamente alle pareti per stabilire il livello di resistenza richiesto. Le porte antincendio DEVONO funzionare in conformità alle normative antincendio svizzere in modalità failsafe.
- Le aperture di ventilazione e i varchi di servizio NON DEVONO fornire percorsi alternativi di accesso alle aree protette.
- Idonei sistemi di rilevamento delle intrusioni DEVONO essere installati in conformità alle norme nazionali o internazionali applicabili (ad es., EN 50131).

**Perimetri interni (tra zone)**:

- Le pareti divisorie tra Zone controllate, riservate e ad alta sicurezza DEVONO estendersi dal pavimento al soffitto, incluse le aree sopra i soffitti pensili e sotto i pavimenti sopraelevati.
- I punti di accesso tra le zone DEVONO avere controlli degli accessi appropriati corrispondenti alla zona di destinazione.
- Le pareti delle Zone riservate e ad alta sicurezza DEVONO prevenire le intercettazioni visive e audio ove la valutazione del rischio lo richieda.

**Ispezioni del perimetro**:

- Le ispezioni del perimetro dell'edificio DEVONO essere effettuate almeno annualmente.
- I perimetri delle Zone riservate e ad alta sicurezza DEVONO essere ispezionati almeno trimestralmente e dopo qualsiasi modifica edilizia o incidente di sicurezza.
- I risultati delle ispezioni DEVONO essere documentati e le eventuali lacune rimediate entro 30 giorni (o immediatamente se presentano un rischio imminente).

### Strutture di colocation e strutture condivise

Nei casi in cui l'organizzazione operi in data center di colocation o edifici per uffici condivisi:

- Le aree controllate dall'[Organizzazione] (gabbie, stanze, piani) DEVONO essere chiaramente delimitate e documentate.
- Devono essere in vigore requisiti contrattuali per la sicurezza fisica, la registrazione degli accessi e la notifica degli incidenti con il fornitore della struttura.
- Prove di garanzia del fornitore (certificazione ISO 27001, rapporto SOC 2 Type II o attestazione equivalente) DEVONO essere ottenute e riesaminate annualmente.
- Nei casi in cui la sicurezza fisica del fornitore di colocation non soddisfi i requisiti di questa politica, DEVE essere registrata l'accettazione documentata del rischio con controlli compensativi.
- L'infrastruttura condivisa (ascensori, corridoi, aree comuni) NON DEVE fornire accesso non controllato alle aree protette dell'organizzazione.
- La gestione delle chiavi e dei badge per l'accesso all'edificio nelle strutture condivise DEVE essere coordinata con la gestione dell'edificio, con l'[Organizzazione] che mantiene un registro indipendente di tutte le credenziali emesse.

**Separazione delle strutture di elaborazione delle informazioni**: Le strutture di elaborazione delle informazioni gestite dall'organizzazione DEVONO essere fisicamente separate da quelle gestite da terze parti che condividono lo stesso edificio o piano.

---

## Controlli di ingresso fisico (A.7.2)

**ISO/IEC 27001:2022 Allegato A.7.2 — Ingresso fisico**:

> *Le aree sicure dovrebbero essere protette da appropriati controlli di ingresso per garantire che solo il personale autorizzato possa accedervi.*

### Sicurezza dei punti di ingresso

Tutti i punti di ingresso alle aree protette DEVONO essere protetti:

**Ingressi principali**:

- Un banco reception presidiato o un controllo equivalente (citofono, accesso video) DEVE essere operativo durante l'orario lavorativo.
- Un sistema di controllo degli accessi ([Sistema di controllo degli accessi] — ad es., Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY/Salto, o equivalenti lettori di badge RFID, credenziali mobili o lettori biometrici) DEVE autenticare tutto il personale che accede oltre la Zona pubblica. Nei casi in cui i sistemi siano in fase di selezione, l'approccio transitorio e la data di implementazione target DEVONO essere documentati.
- Misure anti-tailgating DEVONO essere implementate ai punti di ingresso delle Zone riservate e ad alta sicurezza:

| Misura | Efficacia | Applicabilità per zona |
|--------|-----------|------------------------|
| **Mantrap** (doppia porta con interlock) | Alta — prevenzione fisica | Zone ad alta sicurezza (server, data center) |
| **Tornelli con sensori di altezza** | Medio-alta — barriera fisica + rilevamento | Zone riservate |
| **CCTV con AI** e rilevamento tailgating | Media — rilevamento + allerta | Tutte le zone protette |
| **Segnaletica di sensibilizzazione alla sicurezza** + cultura della verifica | Bassa-media — comportamentale | Minimo per tutte le zone |

Implementazione corrente: [Specificare, ad es., "Tornelli all'ingresso principale; mantrap al data center; CCTV + sensibilizzazione agli accessi secondari" o "Solo sensibilizzazione + CCTV; barriere fisiche pianificate per [trimestre]"].
- L'accesso fuori orario DEVE richiedere un'autenticazione aggiuntiva e DEVE generare avvisi al personale di sicurezza o al team di reperibilità.

### Accesso di emergenza

**Accesso fuori orario** (al di fuori dell'orario lavorativo — [specificare, ad es., 06:00–20:00 lun–ven]):
- Richiede autenticazione con badge + PIN (minimo Zona controllata).
- Genera avviso al servizio di reperibilità delle strutture / monitoraggio della sicurezza.
- Se la risposta alla verifica non viene ricevuta entro 15 minuti, escalation secondo la procedura di gestione degli incidenti.

**Lockdown di emergenza**:
- Autorità per avviare il lockdown: AD, COO, Responsabile delle strutture, RSSI, o sicurezza in sede.
- Trigger del lockdown: Minaccia attiva in sede, incidente nelle vicinanze che incide sulla sicurezza, calamità naturale.
- Procedura di lockdown: Tutte le porte esterne bloccate (accesso con badge disabilitato); il personale si rifugia in loco; i servizi di emergenza vengono allertati; il via libera viene comunicato tramite [sistema di annunci / SMS / email].

**Evacuazione antincendio e sicurezza**:
- Le porte antincendio si aprono automaticamente all'allarme antincendio (modalità failsafe ai sensi del codice antincendio svizzero).
- Il sistema di controllo degli accessi viene ripristinato dopo il reset dell'allarme e l'ispezione delle strutture conferma la sicurezza.
- Punto di raccolta per l'evacuazione al di fuori del perimetro di sicurezza; rientro tramite processo controllato dopo il via libera.

**Ingressi secondari e di emergenza**:

- Le porte laterali e gli ingressi secondari DEVONO avere controlli degli accessi equivalenti all'ingresso principale per la zona corrispondente.
- Le porte antincendio e le uscite di emergenza DEVONO essere allarmate e monitorate. Le uscite di emergenza DEVONO aprirsi verso l'esterno (ai sensi delle normative antincendio) ma NON DEVONO essere apribili dall'esterno senza autorizzazione.
- Le porte di accesso al tetto e i portelli di servizio DEVONO essere chiusi a chiave e allarmiati.

### Autenticazione per zona

| Zona di sicurezza | Autenticazione minima | Requisiti aggiuntivi |
|-------------------|----------------------|----------------------|
| **Zona controllata** | Badge/tessera di accesso (RFID, credenziale mobile) | — |
| **Zona riservata** | Badge + PIN | Accesso registrato con identità e timestamp |
| **Zona ad alta sicurezza** | Badge + PIN + biometrico, O controllo a due persone | Accesso registrato; CCTV all'ingresso; l'accesso fuori orario genera un avviso |

**Requisiti del sistema di controllo degli accessi**:

- Il sistema di controllo degli accessi DEVE registrare tutti gli eventi di accesso (concessi e negati) con identità, timestamp e punto di ingresso.
- I diritti di accesso DEVONO essere basati sul ruolo e concessi sulla base della necessità di sapere/necessità di accedere.
- I diritti di accesso DEVONO essere riesaminati trimestralmente (come minimo); l'accesso alle Zone riservate e ad alta sicurezza DEVE essere riconfermato dal responsabile autorizzante.

**Processo di revisione trimestrale degli accessi**:

1. **Generazione del rapporto sugli accessi**: Il Responsabile delle strutture genera il rapporto sui diritti di accesso dal [Sistema di controllo degli accessi] con tutto il personale avente accesso alla zona, raggruppato per zona e reparto (scadenza: 1° giorno lavorativo del mese di revisione).
2. **Attestazione del responsabile**: I responsabili diretti ricevono l'elenco degli accessi del proprio team; confermano che l'accesso alla zona di ogni persona sia ancora necessario; identificano gli accessi da rimuovere (scadenza: 14 giorni dopo la distribuzione del rapporto).
3. **Esecuzione della revoca**: Il Responsabile delle strutture revoca gli accessi non necessari entro 5 giorni lavorativi dall'attestazione del responsabile.
4. **Traccia di audit**: I registri di attestazione (conferme email, moduli firmati, o registrazioni di workflow nel [GRC Tool]) sono conservati per 3 anni.

**Gestione della mancata risposta**: I responsabili che non rispondono entro 14 giorni ricevono un'escalation al responsabile di reparto. L'accesso per gli utenti non attestati nelle Zone riservate/ad alta sicurezza viene sospeso in attesa dell'attestazione.

- L'accesso fisico dei dipendenti cessati DEVE essere revocato lo stesso giorno della cessazione del rapporto di lavoro, coordinato con le RU.
- I badge smarriti, rubati o danneggiati DEVONO essere segnalati immediatamente e disattivati secondo la seguente tempistica:

| Tipo di badge | Tempistica di disattivazione | Azioni aggiuntive |
|---------------|------------------------------|-------------------|
| **Badge Zona ad alta sicurezza** | **Immediata** (entro 30 minuti dalla segnalazione) | Notifica al RSSI; revisione del registro accessi nelle 72 ore precedenti; riemissione con nuovo numero di credenziale |
| **Badge Zona riservata** | Entro 2 ore | Revisione del registro accessi in caso di circostanze sospette |
| **Badge Zona controllata** | Entro 4 ore | Processo standard di sostituzione |

**Badge smarrito fuori orario**: Il reperibile delle strutture viene avvisato immediatamente per i badge delle Zone riservate/ad alta sicurezza; la disattivazione viene eseguita da remoto.

- La condivisione e il prestito del badge DEVONO essere vietati.
- I badge di accesso temporaneo DEVONO essere limitati nel tempo e scadere automaticamente.

### Accesso dei dipendenti

- L'accesso dei dipendenti DEVE essere basato sul principio del privilegio minimo, fornendo l'accesso solo alle zone necessarie per il ruolo del dipendente.
- I token di controllo degli accessi (badge, tessere, credenziali mobili) DEVONO essere emessi a ciascun dipendente e DEVONO identificare la persona. I badge DEVONO essere indossati visibilmente in ogni momento all'interno delle sedi (cordino, clip o porta badge). I badge coperti o nascosti possono essere contestati dal personale di sicurezza.

**Requisiti per i badge**:
- I badge dei dipendenti DEVONO includere: foto, nome, ID dipendente, indicatore di accesso alla zona (codificato per colore o testuale).
- I badge dei visitatori DEVONO essere chiaramente distinguibili dai badge dei dipendenti (colore distinto, marcatura "VISITATORE", nessun accesso alla zona codificato).
- I badge dei collaboratori DEVONO essere distinguibili e includere la data di scadenza.
- I badge temporanei (sostituzione per badge permanente smarrito) DEVONO essere contrassegnati con "TEMPORANEO" e scadere automaticamente dopo 7 giorni.
- I token di controllo degli accessi NON DEVONO essere condivisi, trasferiti o prestati ad altri.
- L'accesso DEVE essere revocato immediatamente alla cessazione del rapporto di lavoro; tutti i token di accesso fisico DEVONO essere disabilitati e restituiti. Le RU DEVONO notificare le Strutture di tutte le cessazioni nel giorno lavorativo del termine o prima.
- I cambi di ruolo DEVONO essere valutati per le implicazioni sull'accesso fisico; l'accesso alle zone non più necessarie per il nuovo ruolo DEVE essere revocato entro 5 giorni lavorativi.

**Conservazione dei log di accesso**: I log del sistema di controllo degli accessi fisici DEVONO essere conservati per almeno 12 mesi (o più a lungo ove richiesto dalla normativa applicabile o dal contratto), protetti da modifiche non autorizzate e disponibili entro 2 giorni lavorativi per scopi di audit e risposta agli incidenti.

### Gestione dei visitatori

**Registrazione dei visitatori**:

- Tutti i visitatori DEVONO registrarsi alla reception prima di procedere oltre la Zona pubblica. La registrazione DEVE essere registrata nel [Sistema di gestione dei visitatori] (o nel registro cartaceo dei visitatori) e includere: nome del visitatore, azienda/organizzazione, referente interno (dipendente visitato), data e ora di arrivo e scopo della visita.
- I visitatori DEVONO presentare un documento d'identità fotografico valido.
- I badge dei visitatori DEVONO essere chiaramente distinguibili dai badge dei dipendenti (colore distinto, marcatura "VISITATORE", nessun accesso alla zona codificato).
- I visitatori DEVONO restituire i badge alla partenza e firmare per l'uscita. I badge non restituiti DEVONO essere disattivati entro la fine della giornata lavorativa.

**Accompagnamento e supervisione**:

- I visitatori nelle Zone controllate possono muoversi senza accompagnatore solo se il referente interno ha confermato la visita e il badge del visitatore limita l'ulteriore accesso alla zona.
- I visitatori nelle Zone riservate DEVONO essere accompagnati in ogni momento da un dipendente autorizzato.
- I visitatori nelle Zone ad alta sicurezza DEVONO essere accompagnati in ogni momento da un dipendente autorizzato con accesso esplicito alla zona e la visita DEVE essere pre-approvata dal proprietario della zona.
- L'accesso dei visitatori alle Zone ad alta sicurezza DEVE essere pre-autorizzato per iscritto (email o approvazione nel [Sistema di gestione dei visitatori]) prima dell'arrivo.

**Conservazione del registro dei visitatori**:

- I registri dei visitatori DEVONO essere conservati per un minimo di 12 mesi e protetti da modifiche non autorizzate.
- I registri DEVONO essere disponibili entro 2 giorni lavorativi per audit o indagini su incidenti.

**Accesso di collaboratori e personale di manutenzione**:

- I collaboratori e il personale di manutenzione DEVONO essere pre-autorizzati prima dell'arrivo, con l'ambito del lavoro e le aree di accesso documentati.
- L'accesso dei collaboratori DEVE essere limitato nel tempo e registrato.
- I collaboratori che accedono alle Zone riservate o ad alta sicurezza DEVONO essere accompagnati e il loro lavoro supervisionato ove siano accessibili sistemi o dati sensibili.
- La manutenzione esterna dei sistemi di sicurezza (allarmi, controllo degli accessi, CCTV) DEVE essere eseguita sotto la supervisione diretta di un dipendente autorizzato.

### Aree di carico e consegna

- L'accesso alle aree di carico e consegna dall'esterno dell'edificio DEVE essere limitato al personale di consegna identificato e autorizzato.
- Le aree di carico e consegna DEVONO essere progettate (o gestite operativamente) in modo che il personale di consegna non possa accedere ad altre parti dell'edificio.
- Le porte esterne di un'area di carico e consegna DEVONO essere protette quando le porte interne verso le aree operative sono aperte; ove possibile, non DEVONO essere entrambe aperte contemporaneamente.
- I materiali in arrivo DEVONO essere ispezionati per verificare l'assenza di manomissioni prima di essere spostati dall'area di consegna.
- I materiali in arrivo DEVONO essere registrati ai sensi delle procedure di gestione degli asset all'ingresso nel sito.
- Le spedizioni in entrata e in uscita DEVONO essere fisicamente segregate ove possibile.
- I materiali in arrivo DEVONO essere ispezionati per sostanze pericolose ove la valutazione del rischio lo richieda (specifico del contesto: rischi chimici, biologici o esplosivi).

---

## Messa in sicurezza di uffici, stanze e strutture (A.7.3)

**ISO/IEC 27001:2022 Allegato A.7.3 — Messa in sicurezza di uffici, stanze e strutture**:

> *La sicurezza fisica di uffici, stanze e strutture dovrebbe essere progettata e implementata.*

### Sicurezza generale degli uffici

- Gli uffici DEVONO essere chiusi a chiave quando non occupati fuori dall'orario lavorativo.
- La politica della scrivania libera DEVE essere applicata — i documenti sensibili DEVONO essere messi in sicurezza in archivi chiusi a chiave quando non sono in uso attivo.
- Gli schermi DEVONO essere posizionati per prevenire la lettura indiscreta da parte di visitatori o persone di passaggio.
- Strutture di archiviazione (armadi, casseforti, cassetti con serratura) DEVONO essere messe a disposizione per mettere in sicurezza i documenti classificati e i supporti portatili.
- Le strutture critiche dovrebbero essere ubicate in modo da evitare l'accesso da parte del pubblico e dovrebbero dare il minimo indizio del loro scopo, senza segnaletica esterna evidente che identifichi la presenza di attività di elaborazione delle informazioni.
- Le strutture dovrebbero essere configurate per impedire che le informazioni o le attività riservate siano visibili o udibili dall'esterno.

### Aree sensibili

Le aree che trattano informazioni Riservate o Limitate (ad es., RU, finanza, legale, uffici dirigenziali) DEVONO avere:

- Controlli degli accessi appropriati alla classificazione della zona (minimo Zona riservata).
- Log degli accessi mantenuti e riesaminati.
- Finestre verso aree sensibili opacizzate, coperte o dotate di pellicola privacy per prevenire l'osservazione visiva.
- Dispositivi di registrazione (fotocamere, telefoni con fotocamera) limitati o vietati salvo autorizzazione esplicita.

### Sale server e data center

**Per le sale server e i data center controllati dall'[Organizzazione]**:

**Controllo degli accessi**:

- L'accesso DEVE essere limitato esclusivamente al personale IT autorizzato, con elenchi nominativi degli accessi mantenuti.
- È richiesta l'autenticazione a più fattori (badge + PIN + biometrico, o controllo a due persone).
- Tutti gli accessi DEVONO essere registrati con identità e timestamp.
- I visitatori e i collaboratori nelle sale server DEVONO essere accompagnati in ogni momento.

**Costruzione fisica**:

- Nessuna finestra esterna.
- Pareti, pavimenti e soffitti rinforzati.
- Pareti divisorie a tutta altezza (dalla soletta del pavimento alla soletta del soffitto, non al soffitto pensile).
- Monitoraggio ambientale (soppressione degli incendi, rilevamento acqua, sensori di temperatura e umidità).
- Copertura CCTV con registrazione (conservazione ai sensi di ISMS-OP-POL-A.7.4-5-11).

**Registrazione e monitoraggio degli accessi** (sale server e data center):
- Tutti gli accessi registrati con identità, timestamp, orario di entrata/uscita.
- I log degli accessi riesaminati **settimanalmente** dal Responsabile della sicurezza informatica.
- Le anomalie vengono investigate (accessi fuori orario, schemi di accesso insoliti, visitatori imprevisti).
- Conservazione dei log degli accessi: **3 anni** (superiore ai 12 mesi standard per la protezione degli asset critici).
- Avvisi in tempo reale per: accesso non pianificato fuori orario, tentativi ripetuti di autenticazione falliti, porta tenuta aperta >2 minuti.
- **Correlazione accesso fisico–modifica**: Quando si verificano modifiche a server/infrastrutture, i log degli accessi fisici vengono riesaminati per verificare che il lavoro sia stato eseguito da personale autorizzato.

**Per data center di terze parti e colocation**:

- Protezioni equivalenti DEVONO essere garantite attraverso la garanzia del fornitore (certificazione ISO 27001, rapporto SOC 2 Type II) e requisiti di sicurezza contrattuali.
- Nei casi in cui l'equivalenza esatta non sia fattibile, DEVE essere registrato un trattamento del rischio documentato con controlli compensativi.

### Sicurezza delle sale riunioni

- Le sale riunioni DEVONO essere verificate per la presenza di dispositivi di registrazione o materiali lasciati prima di discussioni sensibili.
- Le lavagne e i fogli di carta DEVONO essere cancellati o rimossi dopo le riunioni.
- I documenti NON DEVONO essere lasciati nelle sale riunioni dopo la conclusione delle riunioni.
- Le attrezzature per le videoconferenze DEVONO essere messe in sicurezza quando non in uso; le fotocamere e i microfoni DEVONO essere in uno stato noto di spegnimento tra una riunione e l'altra.

### Punti di accesso alla rete e cablaggio

- L'accesso fisico alle attrezzature di rete (switch, router, access point wireless, patch panel) DEVE essere limitato al personale IT autorizzato.
- Le prese e le porte di rete nelle Zone pubbliche DEVONO essere disabilitate o NON DEVONO fornire accesso alla rete interna.
- Le prese e le porte di rete nelle Zone controllate che forniscono accesso alla rete interna DEVONO essere protette dai controlli degli accessi fisici alla zona.
- I visitatori NON DEVONO collegare dispositivi alle porte di rete interne salvo autorizzazione esplicita e con accompagnatore.
- Il cablaggio di alimentazione e delle telecomunicazioni che trasporta dati DEVE essere protetto da intercettazioni, interferenze e danni.
- I cavi di alimentazione DEVONO essere segregati dai cavi di comunicazione per prevenire interferenze.
- L'accesso ai locali cavi e ai patch panel DEVE essere limitato dal controllo degli accessi fisici (minimo Zona riservata).
- Ove sia fattibile il cablaggio sotterraneo verso l'edificio, le linee di alimentazione e telecomunicazione verso le strutture di elaborazione delle informazioni dovrebbero essere instradate in modo sotterraneo.

### Aree sicure — Requisiti aggiuntivi

In aggiunta ai controlli basati sulle zone sopra indicati, i seguenti requisiti si applicano a tutte le aree sicure designate (Zone riservate e ad alta sicurezza):

- I diritti di accesso alle aree sicure DEVONO essere predefiniti come rifiutati — l'accesso viene concesso solo previa autorizzazione esplicita.
- Attrezzature fotografiche, video, audio o di altro tipo per la registrazione (incluse le fotocamere nei dispositivi mobili) NON DEVONO essere consentite nelle aree sicure salvo autorizzazione specifica del proprietario della zona.
- Il personale che lavora nelle aree sicure DEVE essere informato dei requisiti e delle restrizioni di sicurezza specifici applicabili a quell'area.
- Il lavoro non supervisionato nelle Zone ad alta sicurezza dovrebbe essere evitato sia per ragioni di sicurezza sia per prevenire opportunità di attività dolose.

### Formazione e consapevolezza

**Formazione annuale sulla consapevolezza della sicurezza fisica** per tutto il personale che copre:
- Utilizzo del badge (indossare visibilmente, non condividere, segnalare immediatamente in caso di smarrimento)
- Verifica delle persone non riconosciute (domanda cortese: "Posso aiutarla?" o "Ha un accompagnatore?")
- Prevenzione del tailgating (non tenere le porte aperte, una persona per ogni passaggio con badge)
- Politica della scrivania libera (chiudere i documenti quando si lascia la postazione)
- Segnalazione degli incidenti di sicurezza fisica (cosa segnalare, come segnalare, a chi)
- Responsabilità dell'accompagnamento dei visitatori

**Formazione specifica per ruolo**:
- **Reception/Sicurezza**: Procedure di gestione dei visitatori, emissione/disattivazione dei badge, procedure di emergenza.
- **Strutture**: Funzionamento del sistema di controllo degli accessi, gestione delle zone, requisiti per l'accompagnamento dei collaboratori.
- **IT**: Sicurezza dei punti di accesso alla rete, procedure di accesso alla sala server, sicurezza del locale attrezzature.

**Formazione dei nuovi assunti**: Formazione sulla sicurezza fisica entro **5 giorni lavorativi** dalla data di inizio, prima della concessione dell'accesso alla zona.

Completamento della formazione monitorato; obiettivo **completamento del 95%** annuale.

### Sopralluoghi di sicurezza fisica

La conformità ai requisiti di sicurezza di uffici, sale riunioni e strutture DEVE essere verificata attraverso sopralluoghi documentati di sicurezza fisica:

- **Frequenza**: Almeno trimestralmente e dopo qualsiasi incidente di sicurezza o modifica delle strutture rilevante.
- **Ambito**: Tutte le zone di sicurezza, i punti di ingresso, le aree sensibili, le sale server, i locali cavi e le sale riunioni.
- **Risultati**: Documentati come non conformità o azioni di miglioramento con proprietario assegnato, data di scadenza e monitorati fino alla chiusura.
- **Checklist**: Una checklist standardizzata per i sopralluoghi DEVE essere mantenuta e utilizzata per tutte le ispezioni.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **Direzione generale** | Approvare la politica; allocare il budget per l'infrastruttura di sicurezza fisica; ricevere rapporti sulla postura di sicurezza fisica |
| **RSSI** | Proprietà della politica; definire gli standard di sicurezza fisica; supervisionare la conformità; approvare le eccezioni; riesaminare le metriche di sicurezza fisica |
| **Responsabile delle strutture** | Implementare e mantenere i controlli di sicurezza fisica; gestire i sistemi di controllo degli accessi; coordinare la sicurezza dell'edificio; gestire collaboratori e manutenzione |
| **Sicurezza informatica** | Integrare i controlli di accesso fisico e logico; gestire la sicurezza dei punti di accesso alla rete; riesaminare l'accesso alla sala server; supportare la risposta agli incidenti |
| **Personale della reception / di sicurezza** | Gestire la gestione dei visitatori; monitorare i punti di ingresso; rispondere ad allarmi e avvisi; verificare le persone non riconosciute |
| **Responsabili diretti** | Autorizzare l'accesso fisico per i membri del team; riesaminare e confermare i diritti di accesso trimestralmente; segnalare i dipendenti in uscita e i cambi di ruolo per la revoca degli accessi |
| **RU** | Notificare le Strutture delle nuove assunzioni, dei cambi di ruolo e delle cessazioni per il provisioning/revoca degli accessi; gestire l'onboarding dei collaboratori |
| **Tutto il personale** | Seguire le procedure di accesso; indossare i badge visibilmente; verificare o segnalare le persone non riconosciute; segnalare badge smarriti ed eventi di sicurezza fisica; rispettare i requisiti della scrivania libera |

**Percorsi di escalation**:

### Segnalazione degli incidenti di sicurezza fisica

Tutto il personale DEVE segnalare immediatamente gli eventi di sicurezza fisica alla reception, al Responsabile delle strutture o al personale di sicurezza. Gli eventi segnalabili includono:

**Critici (escalation immediata al RSSI)**:
- Persona non autorizzata scoperta in una Zona riservata o ad alta sicurezza
- Prove di intrusione fisica (porte forzate, finestre rotte, serrature manomesse)
- Furto o sospetto furto di attrezzature o documenti
- Minacce fisiche o confronti in sede
- Clonazione o manomissione di badge scoperta

**Alta priorità**:
- Tailgating riuscito verso una zona protetta
- Visitatore senza accompagnatore in Zona controllata
- Porta di sicurezza mantenuta aperta deliberatamente (aggiramento)
- Badge smarrito con accesso alla Zona ad alta sicurezza o Zona riservata

**Priorità standard**:
- Badge smarrito con accesso solo alla Zona controllata
- Visitatore senza badge oltre la reception
- Carenza delle strutture (serratura rotta, sensore porta malfunzionante)
- Violazione della politica della scrivania libera

**Canali di segnalazione**: Reception (durante l'orario), Responsabile delle strutture, [numero di emergenza] (fuori orario), RSSI (per eventi critici).

**Percorsi di escalation**:

- **Incidenti di sicurezza fisica**: Dipendente/Personale di sicurezza → Responsabile delle strutture → RSSI → Direzione generale
- **Richieste di accesso**: Dipendente → Responsabile diretto (approvazione) → Responsabile delle strutture (provisioning)
- **Problemi con i visitatori**: Reception → Responsabile delle strutture → RSSI
- **Badge smarriti/rubati**: Dipendente → Reception/Strutture (disattivazione immediata) → Sicurezza informatica (se ci sono implicazioni per l'accesso ai sistemi)
- **Non conformità del collaboratore**: Accompagnatore/Supervisore → Responsabile delle strutture → Responsabile acquisti/contratto

---

## Prove per questa politica

| N. | Prova | Responsabile | Frequenza | Conservazione |
|----|-------|--------------|-----------|---------------|
| 1 | **Documentazione delle zone di sicurezza e planimetrie** che mostrano i confini delle zone, i punti di accesso e i meccanismi di controllo | Responsabile delle strutture | Aggiornato alla modifica della struttura; riesaminato annualmente | Versione corrente + versione precedente |
| 2 | **Configurazione del sistema di controllo degli accessi** — assegnazioni delle zone, livelli di autenticazione, regole di accesso basate sul ruolo | Responsabile delle strutture / IT | Riesaminato trimestralmente | Configurazione corrente + registro delle modifiche |
| 3 | **Log del sistema di controllo degli accessi** — eventi di entrata/uscita con identità, timestamp, punto di ingresso (concessi e negati) | [Sistema di controllo degli accessi] | Continuo; riesaminato mensilmente per anomalie | Minimo 12 mesi |
| 4 | **Registri dei visitatori** — registrazioni con nome, azienda, referente interno, data/ora entrata/uscita, identificazione verificata | Reception / [Sistema di gestione dei visitatori] | Continuo | Minimo 12 mesi |
| 5 | **Registri della revisione dei diritti di accesso** — revisione trimestrale dei diritti di accesso del personale con firma del responsabile | Responsabile delle strutture / Responsabili diretti | Trimestrale | 3 anni |
| 6 | **Rapporti di ispezione del perimetro** — risultati documentati delle ispezioni del perimetro dell'edificio e delle zone | Responsabile delle strutture | Annuale (edificio); trimestrale (Zone riservate/ad alta sicurezza) | 3 anni |
| 7 | **Rapporti dei sopralluoghi di sicurezza fisica** — risultati della checklist, risultanze e monitoraggio della rimediazione | Responsabile delle strutture / RSSI | Trimestrale | 3 anni |
| 8 | **Registri di gestione dei badge** — emissione, sostituzione, disattivazione, segnalazioni di smarrimento/furto | Responsabile delle strutture | Per evento; verificato annualmente | Durata del rapporto di lavoro + 1 anno |
| 9 | **Registri di accesso di collaboratori e personale di manutenzione** — pre-autorizzazione, ambito, registrazioni di accompagnamento | Responsabile delle strutture | Per incarico | 3 anni |
| 10 | **Registri di garanzia del fornitore** per strutture di colocation/condivise — certificati, rapporti SOC, termini contrattuali | RSSI / Approvvigionamenti | Riesaminati annualmente | Durata del contratto + 2 anni |
| 11 | **Registro delle eccezioni** — eccezioni approvate con giustificazione, controlli compensativi, data di scadenza | RSSI | Aggiornato per eccezione; riesaminato trimestralmente | 3 anni dalla chiusura dell'eccezione |
| 12 | **Rapporti sugli incidenti di sicurezza fisica** — tentativi di accesso non autorizzati, smarrimento badge, eventi di tailgating, violazioni del perimetro | RSSI / Responsabile delle strutture | Per incidente | 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo: rapporti del sistema di controllo degli accessi, audit dei registri dei visitatori, risultati dei sopralluoghi di sicurezza fisica, tassi di completamento delle revisioni dei diritti di accesso, metriche di gestione dei badge, revisioni della garanzia del fornitore, audit interni ed esterni, e feedback al proprietario della politica.

**Metriche chiave**:

| Metrica | Obiettivo | Frequenza di revisione |
|---------|-----------|------------------------|
| Copertura del controllo degli accessi (% dei punti di ingresso con controlli attivi) | 100% | Trimestrale |
| Revisioni dei diritti di accesso completate nei tempi previsti | 100% | Trimestrale |
| Conformità all'accompagnamento dei visitatori (Zone riservate/ad alta sicurezza) | 100% | Mensile |
| Accesso dei dipendenti cessati revocato lo stesso giorno | 100% | Per evento; verificato mensilmente |
| Incidenti di smarrimento/furto di badge | < 5 per trimestre | Trimestrale |
| Tentativi di accesso non autorizzato (riusciti) | 0 | Mensile |
| Completamento dei sopralluoghi di sicurezza fisica | 100% secondo il programma | Trimestrale |
| Revisioni della garanzia del fornitore aggiornate | 100% | Annuale |

**Reporting**:
- **Dashboard mensile** al RSSI: Conformità alla revoca degli accessi, incidenti di smarrimento badge, tentativi di accesso non autorizzato, conformità all'accompagnamento dei visitatori.
- **Rapporto trimestrale** alla Direzione generale: Tutte le metriche, analisi dei trend, risultanze dei sopralluoghi, stato delle eccezioni.
- **Rapporto annuale** alla Revisione della direzione: Efficacia del programma di sicurezza fisica, raccomandazioni per gli investimenti in conto capitale, stato della conformità normativa.

Le metriche che non raggiungono gli obiettivi DEVONO essere segnalate immediatamente al RSSI e includere un piano di rimediazione con proprietario e data target.

## Eccezioni

Qualsiasi eccezione a questa politica DEVE essere approvata e registrata in anticipo dal RSSI, con giustificazione aziendale documentata, valutazione del rischio, controlli compensativi e una data di scadenza definita (massimo 6 mesi, rinnovabile con rivalutazione). Le eccezioni DEVONO essere riferite al team di revisione della direzione.

**Eccezioni consentite** (con appropriati controlli compensativi):

- Accesso di emergenza temporaneo per riparazioni urgenti (con monitoraggio potenziato e accompagnamento).
- Accesso esteso dei visitatori per revisori o ispettori normativi (con approvazione documentata e ambito definito).
- Metodi di autenticazione alternativi per il personale con requisiti di accessibilità.

**Non ammissibili** come eccezioni:

- Aggiramento permanente dei requisiti di autenticazione delle zone.
- Eccezioni senza controlli compensativi.
- Eccezioni alla revoca degli accessi lo stesso giorno per i dipendenti cessati.

## Non conformità

Un dipendente che abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. Scenari specifici di non conformità e relative risposte:

- **Tailgating o agevolazione del tailgating**: Avvertimento formale; l'infrazione ripetuta attiva il processo disciplinare.
- **Condivisione o prestito del badge**: Disattivazione immediata del badge; processo disciplinare.
- **Mancata verifica o segnalazione di persone non riconosciute**: Gestita attraverso la formazione sulla consapevolezza.
- **Mantenimento aperto di porte protette**: Rimediazione immediata; avvertimento formale se deliberato.

I collaboratori che non rispettano le regole possono avere l'accesso revocato e l'organizzazione committente viene informata.

## Miglioramento continuo

Questa politica è riesaminata e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO considerare:

- Modifiche alle strutture (trasferimenti di uffici, ristrutturazioni, nuovi siti, variazioni di locazione).
- Incidenti di sicurezza fisica e quasi-incidenti (accessi non autorizzati, tailgating, violazioni del perimetro).
- Risultanze degli audit e dei sopralluoghi.
- Progressi nella tecnologia del controllo degli accessi (credenziali mobili, biometria contactless, rilevamento anomalie con AI).
- Modifiche normative (in particolare nLPD, requisiti cantonali per la protezione dei dati e aggiornamenti del RGPD).
- Cambiamenti nel panorama delle minacce (ad es., aumento dell'ingegneria sociale mirata all'accesso fisico).
- Lezioni apprese dagli eventi di sicurezza fisica dell'organizzazione o segnalati nel settore.

Le azioni di miglioramento DEVONO essere monitorate, assegnate a un proprietario e riferite al RSSI e al team di revisione della direzione.

---

# Aree della norma ISO 27001 trattate

Politica sul controllo degli accessi fisici — Mappatura dei controlli ISO 27001:2022

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.1 Azioni per affrontare rischi e opportunità | 5.36 Conformità alle politiche, norme e standard |
| Clausola 6.2 Obiettivi della sicurezza delle informazioni | 6.3 Consapevolezza, formazione e addestramento sulla sicurezza delle informazioni |
| Clausola 7.3 Consapevolezza | 6.4 Processo disciplinare |
| Clausola 8.1 Pianificazione e controllo operativi | **7.1 Perimetri di sicurezza fisica** |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | **7.2 Ingresso fisico** |
| Clausola 10.2 Non conformità e azioni correttive | **7.3 Messa in sicurezza di uffici, stanze e strutture** |
| | 7.4 Monitoraggio della sicurezza fisica |
| | 7.6 Lavoro in aree sicure |
| | 7.8 Ubicazione e protezione delle attrezzature |

---

# Quadro normativo

| Framework | Applicabilità | Pertinenza per il controllo degli accessi fisici |
|-----------|---------------|--------------------------------------------------|
| **nLPD svizzera (revDSG)** | **Obbligatorio** — tutti i trattamenti di dati personali | Art. 8 — Misure tecniche e organizzative proporzionate al rischio; sicurezza fisica delle sedi dove i dati personali sono trattati o archiviati |
| **OPDo svizzera** | **Obbligatorio** — integra la nLPD | Art. 1-3 — Requisiti minimi per la sicurezza dei dati, inclusi i controlli degli accessi fisici |
| **ISO/IEC 27001:2022** | **Obbligatorio** — ambito di certificazione | Allegato A Controlli 7.1, 7.2, 7.3 |
| **ISO/IEC 27002:2022** | **Orientamento** | Sezioni 7.1, 7.2, 7.3 — Linee guida di attuazione per i controlli fisici |
| **RGPD UE** | **Condizionale** — dove si trattano dati personali di persone UE/SEE | Art. 32 — La sicurezza del trattamento include le misure di sicurezza fisica |
| **PCI DSS v4.0** | **Condizionale** — dove si trattano dati di carte di pagamento | Requisito 9 — Limitare l'accesso fisico ai dati dei titolari di carta; richiede accesso con badge, registri dei visitatori, procedure di distruzione dei supporti |
| **Circolare FINMA 2023/1** | **Condizionale** — istituti finanziari regolamentati svizzeri | Gestione del rischio operativo inclusa la sicurezza fisica delle infrastrutture critiche |
| **NIST SP 800-53 Rev 5** | **Orientamento** | Famiglia PE — Controlli di protezione fisica e ambientale |
| **CIS Controls v8** | **Orientamento** | Controllo 3 (Protezione dei dati), Controllo 6 (Gestione del controllo degli accessi) — dimensioni dell'accesso fisico |

---

<!-- QA_VERIFIED: 2026-04-03 -->
