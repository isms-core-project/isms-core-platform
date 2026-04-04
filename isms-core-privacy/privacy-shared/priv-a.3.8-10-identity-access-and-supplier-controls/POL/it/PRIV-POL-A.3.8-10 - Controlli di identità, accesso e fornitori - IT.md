<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.8-10-IT:privacy:POL:a.3.8-10 -->
**PRIV-POL-A.3.8-10 — Controlli di identità, accesso e fornitori**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Controlli di identità, accesso e fornitori |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | PRIV-POL-A.3.8-10 |
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
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.8-10-UG / TG
- ISMS-POL-A.5.15-16-18 (Gestione delle identità e degli accessi — parallelo SGSI)
- ISMS-POL-A.5.19-23 (Servizi cloud e relazioni con i fornitori — parallelo SGSI)
- ISO/IEC 27701:2025 Controlli A.3.8, A.3.9, A.3.10
- RGPD Articolo 25 (Privacy by design); Articolo 28 (Contratti responsabili del trattamento); Articolo 32 (Sicurezza)
- LPD svizzera Articolo 7 (Sicurezza dei dati); Articolo 9 (Accordi di trattamento)

**Applicabilità del ruolo** : Questa politica si applica all'organizzazione che agisce sia come **Titolare del trattamento che come Responsabile del trattamento dei DCP**. I controlli A.3.8, A.3.9 e A.3.10 sono controlli condivisi (Tabella A.3).

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione del ciclo di vita delle identità, la governance dei diritti di accesso e gli obblighi di sicurezza delle informazioni negli accordi con i fornitori in relazione al trattamento dei DCP — conformemente ai controlli A.3.8, A.3.9 e A.3.10 di ISO/IEC 27701:2025.

**Perimetro** : Tutte le identità utilizzate per accedere ai DCP o ai sistemi di trattamento dei DCP; tutti i diritti di accesso ai DCP e agli asset associati; tutte le relazioni con i fornitori dove si applicano i requisiti di sicurezza delle informazioni per il trattamento dei DCP.

**Motivazione dei controlli combinati** : A.3.8 (ciclo di vita delle identità), A.3.9 (diritti di accesso) e A.3.10 (sicurezza dei fornitori) formano la triade di governance degli accessi per la protezione dei DCP. Le identità creano gli attori; i diritti di accesso determinano cosa possono raggiungere; gli accordi con i fornitori estendono questi controlli alla supply chain.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27701:2025

**Controllo A.3.8 — Gestione delle identità**
Il controllo A.3.8 richiede che [Organizzazione] gestisca l'intero ciclo di vita di tutte le identità che hanno una relazione con il trattamento dei DCP — coprendo provisioning, modifica, sospensione e disattivazione delle identità umane e non umane.

**Controllo A.3.9 — Diritti di accesso**
Il controllo A.3.9 richiede che [Organizzazione] provveda al provisioning, alla revisione, alla modifica e alla rimozione dei diritti di accesso ai DCP e altri asset associati in conformità con la propria politica di controllo degli accessi.

**Controllo A.3.10 — Gestione della sicurezza delle informazioni negli accordi con i fornitori**
Il controllo A.3.10 richiede che [Organizzazione] stabilisca e concordi requisiti pertinenti di sicurezza delle informazioni per il trattamento dei DCP con ciascun fornitore, calibrati al tipo di relazione.

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 25 (controllo degli accessi come misura di privacy by design); Articolo 28 (i contratti di trattamento devono includere obblighi di sicurezza adeguati); Articolo 32 (misure tecniche appropriate inclusi i controlli degli accessi); Articolo 5(1)(f) (principio di integrità e riservatezza)
- **LPD svizzera** : Articolo 7 (misure tecniche e organizzative di sicurezza); Articolo 9 (gli accordi di trattamento devono garantire protezione equivalente)
- **ISO/IEC 27701:2025** : Controlli A.3.8, A.3.9, A.3.10 (normativi)

---

# Gestione del ciclo di vita delle identità per il trattamento dei DCP (A.3.8)

## Requisiti del ciclo di vita delle identità

[Organizzazione] DEVE gestire l'intero ciclo di vita di tutte le identità che hanno accesso ai DCP o ai sistemi di trattamento dei DCP. La gestione del ciclo di vita delle identità per i DCP DEVE essere coerente con e integrare i requisiti SGSI di gestione delle identità (ISMS-POL-A.5.15-16-18).

### Provisioning delle identità per l'accesso ai DCP

Le identità a cui viene concesso l'accesso ai DCP o ai sistemi di trattamento dei DCP DEVONO essere fornite sulla base di:

- **Finalità aziendale documentata** : Deve esistere una giustificazione aziendale documentata e approvata per l'accesso ai DCP prima del provisioning
- **Allineamento al ruolo** : L'accesso DEVE essere allineato alle responsabilità di trattamento dei DCP documentate del ruolo; l'accesso ai DCP non richiesto per il ruolo NON DEVE essere fornito
- **Privilegio minimo** : Le identità DEVONO essere fornite con il livello minimo di accesso necessario per la finalità documentata (principio del minimo necessario, coerente con RGPD Articolo 5(1)(c) minimizzazione dei dati)
- **Autorità di approvazione** : Il provisioning dell'accesso ai DCP DEVE richiedere l'approvazione del Proprietario dei dati per il dataset DCP rilevante, o del RPD laddove non sia assegnato alcun Proprietario dei dati

### Modifica e sospensione delle identità

Laddove un ruolo cambi, un individuo venga trasferito a una funzione diversa, o le circostanze cambino in modo tale che una finalità di accesso ai DCP precedentemente giustificata non si applichi più: i diritti di accesso ai DCP DEVONO essere modificati o sospesi entro il periodo specificato in PRIV-IMP-A.3.8-10-TG; la notifica dei cambiamenti di ruolo DEVE essere fornita dalla direzione gerarchica al Team Sicurezza IT e documentata; la sospensione (non la cancellazione immediata) DEVE applicarsi laddove un blocco legale o un'indagine richiedano la conservazione dei registri di identità.

### Disattivazione delle identità

Quando il rapporto di lavoro o l'ingaggio di un individuo termina, o la finalità di un account di servizio è terminata: i diritti di accesso ai DCP DEVONO essere rimossi il giorno del termine del lavoro o prima (partenza dei dipendenti, fine del contratto); i registri di disattivazione delle identità DEVONO essere conservati per 3 anni dalla data di disattivazione; laddove la disattivazione sia ritardata per motivi tecnici, l'accesso DEVE essere sospeso immediatamente e la disattivazione completata entro 5 giorni lavorativi; per garantire la tempestiva disattivazione laddove la notifica HR non venga ricevuta, la Sicurezza IT DEVE eseguire una riconciliazione mensile delle identità attive con accesso ai DCP con i record HR correnti; qualsiasi identità senza un record di impiego o ingaggio attivo corrente DEVE essere sospesa in attesa della conferma del RPD.

### Gestione delle identità non umane

Gli account di servizio, applicativi e di elaborazione automatizzata utilizzati nelle pipeline di trattamento dei DCP DEVONO essere: individualmente identificati e registrati nel Registro delle identità; associati a un proprietario umano responsabile (responsabile della gestione del ciclo di vita dell'account di servizio); soggetti a revisione periodica (minimo annualmente) per confermare la necessità continuata; disattivati quando la finalità di trattamento che supportano viene abbandonata.

---

# Diritti di accesso ai DCP e asset associati (A.3.9)

## Requisiti dei diritti di accesso

[Organizzazione] DEVE garantire che i diritti di accesso ai DCP e agli asset associati siano forniti, rivisti, modificati e rimossi in conformità con la politica di controllo degli accessi SGSI (ISMS-POL-A.5.15-16-18) e le estensioni specifiche ai DCP definite in questa politica.

### Principi dei diritti di accesso ai DCP

I diritti di accesso ai DCP DEVONO essere disciplinati da:

1. **Accesso minimo necessario** : L'accesso concesso DEVE essere limitato ai DCP e agli asset associati minimi richiesti per adempiere alla finalità di trattamento documentata
2. **Necessità di trattamento** : L'accesso viene concesso solo laddove esista una necessità documentata e attuale di trattare i DCP specifici
3. **Separazione delle funzioni** : Laddove il trattamento dei DCP coinvolga operazioni ad alto rischio (cancellazione, esportazione, accesso di massa), DEVONO essere implementati controlli di separazione delle funzioni per prevenire abusi da parte di un singolo attore. Il standard minimo è che nessuna identità singola possa avviare e approvare un'operazione DCP ad alto rischio
4. **Accesso a tempo limitato** : Laddove l'accesso venga concesso per un progetto, un'attività o una finalità temporanea specifici, i diritti di accesso DEVONO essere limitati nel tempo e rivisti automaticamente alla scadenza

### Revisione dei diritti di accesso ai DCP

I diritti di accesso ai DCP e ai sistemi di trattamento dei DCP DEVONO essere rivisti: **al minimo annualmente** per tutti i diritti di accesso (certificazione formale); **al cambio di ruolo** per l'individuo interessato; **al cambiamento organizzativo** (ristrutturazione, cambiamenti di unità aziendali) che incide sulle finalità di trattamento; **a seguito di un incidente di privacy** che ha coinvolto accesso non autorizzato o inappropriato ai DCP; **su richiesta del Proprietario dei dati** per il dataset DCP rilevante.

Le revisioni dei diritti di accesso DEVONO essere documentate. I diritti confermati come non più necessari DEVONO essere rimossi entro 5 giorni lavorativi per l'accesso standard e immediatamente per l'accesso privilegiato. I registri di revisione DEVONO essere conservati come prove.

### Accesso privilegiato ai DCP

L'accesso privilegiato ai sistemi di trattamento dei DCP (accesso amministrativo, accesso di massa ai dati, diritti di amministratore di database, accesso di backup e ripristino) richiede: notifica esplicita al RPD e approvazione del Proprietario dei dati prima della concessione; un'identità privilegiata separata (non combinata con l'identità utente standard); registrazione di audit potenziata dell'attività della sessione privilegiata che coinvolge DCP; revisione periodica più frequente (minimo ogni 6 mesi); revoca immediata a qualsiasi indicazione di uso improprio.

### Registro dei diritti di accesso

[Organizzazione] DEVE mantenere un Registro dei diritti di accesso ai DCP che documenta: identità con accesso ai DCP, per dataset e sistema; livello e perimetro di accesso concessi; base di approvazione e identità dell'approvatore; data di concessione e data dell'ultima revisione; data di scadenza (per accessi a tempo limitato). Il Registro è mantenuto dal Team Sicurezza IT con supervisione del RPD.

---

# Sicurezza delle informazioni negli accordi con i fornitori (A.3.10)

## Requisiti di sicurezza dei fornitori per i DCP

[Organizzazione] DEVE stabilire e concordare requisiti pertinenti di sicurezza delle informazioni relativi al trattamento dei DCP con ciascun fornitore, proporzionalmente al tipo di relazione.

### Categorizzazione dei fornitori per i requisiti DCP

| Categoria fornitore | Descrizione | Requisiti minimi |
|--------------------|-------------|-----------------|
| **Responsabile del trattamento dei DCP** | Tratta direttamente i DCP per conto di [Organizzazione] su istruzione | Accordo di trattamento completo per RGPD Articolo 28 / LPD svizzera Articolo 9 + programma di sicurezza DCP |
| **Fornitore adiacente ai DCP** | Ha accesso ai sistemi o agli ambienti contenenti DCP nell'ambito della sua prestazione (es. servizi IT gestiti, infrastruttura cloud, manutenzione) | Obbligo di riservatezza + restrizioni di gestione dei dati + obbligo di notifica degli incidenti |
| **Nessun accesso ai DCP** | Fornisce servizi senza accesso ai DCP o ai sistemi di trattamento dei DCP | Condizioni di sicurezza standard dei fornitori (ISMS-POL-A.5.19-23) — nessun addendum specifico ai DCP richiesto |

### Requisiti obbligatori di sicurezza DCP negli accordi con i fornitori

Per le categorie Responsabile del trattamento dei DCP e Fornitore adiacente ai DCP, i seguenti requisiti di sicurezza delle informazioni relativi al trattamento dei DCP DEVONO essere stabiliti e concordati nell'accordo con il fornitore:

**Obblighi di sicurezza** : Impegno a implementare e mantenere misure tecniche e organizzative di sicurezza appropriate per i DCP, non meno protettive dei propri requisiti di [Organizzazione]; obbligo di trattare i DCP solo su istruzione di [Organizzazione] (per i responsabili del trattamento); divieto di utilizzare i DCP per le proprie finalità del fornitore.

**Riservatezza** : Il personale del fornitore con accesso ai DCP è vincolato da obblighi di riservatezza; gli obblighi di riservatezza sopravvivono alla risoluzione dell'accordo.

**Notifica degli incidenti** : Obbligo di notificare [Organizzazione] di qualsiasi incidente di sicurezza DCP effettivo o sospetto entro il periodo specificato nell'accordo (allineato alle finestre di notifica normativa — massimo 24 ore in caso di rischio di violazione dei dati personali); cooperazione nell'indagine e nella remediation.

**Controllo dei sub-responsabili del trattamento / sub-appaltatori** : Consenso scritto preventivo richiesto prima di ingaggiare sub-responsabili del trattamento con accesso ai DCP di [Organizzazione]; trasmissione di obblighi di sicurezza equivalenti a qualsiasi sub-responsabile.

**Diritti di audit** : Diritto di [Organizzazione] di verificare o valutare le misure di sicurezza DCP del fornitore, o di ricevere rapporti di audit di terze parti (es. certificazione ISO 27001, SOC 2 Tipo II).

**Restituzione e cancellazione** : Alla risoluzione o su richiesta, il fornitore DEVE restituire o cancellare in modo sicuro tutti i DCP, e confermare la cancellazione per iscritto.

**Conformità normativa** : Il fornitore riconosce il quadro normativo applicabile (RGPD, LPD svizzera) e si impegna alla conformità nelle proprie attività di trattamento.

### Revisione degli accordi con i fornitori

Gli accordi con i fornitori relativi ai DCP DEVONO essere rivisti: al minimo annualmente, o al rinnovo del contratto; in caso di significativi cambiamenti nella natura dei DCP trattati dal fornitore; a seguito di un incidente di sicurezza che coinvolge il fornitore; in caso di significativi cambiamenti ai requisiti normativi applicabili; alla notifica di un cambiamento degli accordi di sub-responsabili del trattamento del fornitore.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità per A.3.8–A.3.10 |
|-------|--------------------------------|
| **RPD** | Approva l'accesso privilegiato ai DCP; mantiene la supervisione del Registro dei diritti di accesso; approva gli accordi con i fornitori rilevanti per i DCP; esamina le decisioni di categorizzazione dei fornitori; mantiene il Registro degli accordi di trattamento |
| **Proprietario dei dati** | Approva il provisioning dell'accesso ai DCP per il proprio dataset; conduce o supervisiona le revisioni periodiche dei diritti di accesso; escalation degli accessi non autorizzati a RPD e RSSI |
| **RSSI** | Definisce i requisiti tecnici del ciclo di vita delle identità e del controllo degli accessi; garantisce l'estensione della gestione delle identità SGSI ai DCP per questa politica; esamina i programmi di sicurezza dei fornitori |
| **Team Sicurezza IT** | Mantiene il Registro delle identità e il Registro dei diritti di accesso; esegue il provisioning e la disattivazione degli accessi; conduce le revisioni dei diritti di accesso; implementa i controlli di accesso privilegiato |
| **Legale/Conformità** | Esamina le clausole di sicurezza DCP negli accordi con i fornitori; consulenza sui requisiti contrattuali dell'Articolo 28 |
| **Acquisti / Gestione fornitori** | Garantisce la categorizzazione DCP prima della firma dell'accordo; coinvolge Legale/RPD per gli accordi rilevanti per i DCP; mantiene l'inventario degli accordi con i fornitori |
| **Direzione gerarchica** | Notifica il Team Sicurezza IT dei cambiamenti di ruolo e delle partenze; approva le richieste di accesso ai DCP per i membri del proprio team |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registro delle identità | Tutte le identità (umane e non umane) con accesso ai DCP, incluso lo stato del ciclo di vita | In corso + 3 anni |
| Registro dei diritti di accesso | Diritti di accesso ai DCP per identità, dataset e sistema; registrazioni di approvazione e revisione | In corso + 3 anni |
| Registrazioni di revisione dei diritti di accesso | Prove documentate della certificazione periodica dei diritti di accesso, inclusi i diritti rimossi | 3 anni dalla data della revisione |
| Inventario degli accordi con i fornitori | Elenco di tutti gli accordi con i fornitori con categorizzazione DCP e riferimento alle clausole di sicurezza DCP | In corso + 3 anni |
| Copie degli accordi con i fornitori | Accordi firmati contenenti obblighi di sicurezza DCP | Durata dell'accordo + 3 anni |
| Registrazioni di approvazione dell'accesso privilegiato | Notifiche RPD e approvazioni del Proprietario dei dati per l'accesso privilegiato ai DCP | 3 anni dalla revoca dell'accesso |
| Registrazioni di disattivazione delle identità | Prove della tempestiva rimozione degli accessi alla partenza o al cambio di ruolo | 3 anni dalla data di disattivazione |

---

# Considerazioni di audit

**Per A.3.8 (Gestione delle identità)** : Registro delle identità che copre tutte le identità umane e non umane con accesso ai DCP; prove di approvazione documentata per il provisioning dell'accesso ai DCP; registrazioni di disattivazione delle identità alla partenza o al cambio di ruolo; registrazioni di revisione periodica per le identità non umane.

**Per A.3.9 (Diritti di accesso)** : Registro dei diritti di accesso ai DCP con diritti correnti documentati; prove di revisioni periodiche dei diritti di accesso (minimo annuale); registrazioni di modifica o rimozione dell'accesso a seguito di cambiamenti di ruolo; registrazioni di approvazione e revisione dell'accesso privilegiato; prove di separazione delle funzioni per le operazioni DCP ad alto rischio.

**Per A.3.10 (Accordi con i fornitori)** : Registrazioni di categorizzazione dei fornitori; accordi firmati con i fornitori contenenti requisiti di sicurezza delle informazioni DCP; prove di revisione annuale o innescata degli accordi con i fornitori DCP; registrazioni di approvazione dei sub-responsabili e conferma della trasmissione degli obblighi.

---

<!-- QA_VERIFIED: 2026-04-03 -->
