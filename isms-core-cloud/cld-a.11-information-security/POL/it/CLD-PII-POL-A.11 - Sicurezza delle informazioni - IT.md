<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.11-IT:cloud:POL:a.11 -->
**CLD-PII-POL-A.11 — Sicurezza delle informazioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Responsabile del trattamento di DCP nel cloud pubblico — Sicurezza delle informazioni |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | CLD-PII-POL-A.11 |
| **Autore del documento** | RSSI / Responsabile Sicurezza Cloud |
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
| 1.0 | [Data da definire] | RSSI / Responsabile Sicurezza Cloud | Politica iniziale per l'implementazione di ISO/IEC 27018:2025 Ed. 3 |

**Ciclo di revisione** : Annuale (o in caso di significativi cambiamenti di infrastruttura, tecnologia o normativi)
**Prossima data di revisione** : [Data di entrata in vigore + 12 mesi]

**Catena di approvazione** :
- Principale: RSSI / Responsabile Sicurezza Cloud
- Secondaria: Responsabile della Protezione dei Dati (RPD)
- Autorità finale: Direzione generale

**Documenti correlati** :
- PRIV-POL-00 (Quadro di applicabilità normativa sulla privacy)
- ISMS-POL-A.5.34 (Privacy e protezione dei DCP)
- ISMS-POL-A.5.15-16-18 (Gestione delle identità e degli accessi)
- ISMS-POL-A.5.19-23 (Relazioni con fornitori e terze parti)
- ISMS-POL-A.8.10 (Cancellazione delle informazioni)
- ISMS-POL-A.8.24 (Utilizzo della crittografia)
- CLD-PII-POL-A.1 (Generalità)
- CLD-PII-POL-A.5 (Minimizzazione dei dati — cancellazione dei file temporanei)
- CLD-PII-POL-A.8 (Apertura, trasparenza — divulgazione dei sub-responsabili del trattamento)
- CLD-PII-POL-A.10 (Accountability — notifica delle violazioni)
- ISO/IEC 27018:2025 Allegato A, Sezione A.11 e Controlli A.11.1–A.11.13
- ISO/IEC 27701:2025 Allegato A.3 (Controlli di sicurezza delle informazioni — A.3.3 fino a A.3.31, applicabili a titolari e responsabili del trattamento, implementati attraverso questa politica)
- ISO/IEC 27002:2022 Controlli 6.2 (termini e condizioni), 8.11 (mascheramento dei dati), 8.12 (prevenzione della perdita di dati), 8.24 (crittografia)
- RGPD Articolo 28(3)(c) (il responsabile del trattamento implementa le misure tecniche e organizzative appropriate ai sensi dell'Articolo 32); Articolo 32 (sicurezza del trattamento)
- LPD svizzera Articolo 9 (condizioni di ingaggio del responsabile del trattamento e obblighi di sicurezza dei dati associati)

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di sicurezza delle informazioni di [Organizzazione] per la protezione dei DCP negli ambienti cloud pubblici — la sezione più completa del set di controlli dell'Allegato A di ISO/IEC 27018:2025, che copre 13 controlli in materia di riservatezza, sicurezza dei supporti fisici, gestione degli accessi, crittografia, registrazione degli audit, gestione dei sub-responsabili del trattamento e remanenza dei dati.

**Perimetro** : Tutti i sistemi, il personale, i processi e i sub-responsabili del trattamento coinvolti nel trattamento dei DCP per conto dei titolari del trattamento dei DCP nell'ambito dei servizi cloud pubblici di [Organizzazione].

**Copertura dei controlli** : Questa politica copre i Controlli A.11.1–A.11.13 di ISO/IEC 27018:2025.

---

# Perimetro e applicabilità

## Enunciati dei controlli ISO/IEC 27018:2025

**A.11.1 — Accordi di riservatezza o non divulgazione** : Il personale con accesso ai DCP è vincolato da obblighi NDA documentati che sopravvivono alla cessazione del rapporto.

**A.11.2 — Restrizione della creazione di copia cartacea** : La stampa di DCP è limitata a finalità legittime documentate; i DCP stampati vengono gestiti in modo sicuro.

**A.11.3 — Controllo e registrazione nei log del ripristino dei dati** : Il ripristino dei DCP dal backup è un'operazione controllata e registrata nei log; i log sono protetti ed esaminati.

**A.11.4 — Protezione dei dati su supporti di archiviazione che lasciano i locali** : I supporti fisici contenenti DCP vengono cifrati o distrutti prima di lasciare l'ambiente controllato.

**A.11.5 — Utilizzo di supporti e dispositivi di archiviazione portatili non cifrati** : I dispositivi portatili non cifrati sono vietati per i DCP; la perdita/il furto viene trattata come incidente DCP.

**A.11.6 — Cifratura dei DCP trasmessi su reti di trasmissione dati pubbliche** : I DCP in transito vengono cifrati con TLS 1.2 minimo, 1.3 preferito; HTTPS è obbligatorio.

**A.11.7 — Smaltimento sicuro delle copie cartacee** : Le copie cartacee dei DCP vengono smaltite mediante triturazione a taglio incrociato o equivalente; lo smaltimento viene documentato.

**A.11.8 — Utilizzo univoco degli ID utente** : A ogni persona con accesso ai DCP viene assegnato un identificatore univoco; nessun account condiviso.

**A.11.9 — Gestione degli ID utente** : Il ciclo di vita degli ID utente è gestito; vengono disattivati tempestivamente alla cessazione o al cambio di ruolo; gli account inattivi vengono esaminati.

**A.11.10 — Registrazioni degli utenti autorizzati** : Registrazioni aggiornate di tutti gli utenti autorizzati dei sistemi DCP; esaminate almeno trimestralmente; disponibili per il titolare del trattamento.

**A.11.11 — Misure contrattuali** : Gli accordi tra responsabile e titolare del trattamento coprono perimetro, sicurezza, notifica delle violazioni, assistenza sui diritti, audit, approvazione dei sub-responsabili del trattamento, restituzione/cancellazione, giurisdizione.

**A.11.12 — Trattamento dei DCP in sub-appalto** : I sub-responsabili del trattamento sono vincolati da obblighi equivalenti tramite contratti vincolanti; periodicamente sottoposti ad audit; il responsabile del trattamento rimane responsabile.

**A.11.13 — Accesso ai dati nello spazio di archiviazione dati precedentemente utilizzato** : Lo spazio di archiviazione riallocato a un nuovo cliente viene cancellato crittograficamente; le procedure di dismissione sono documentate e testate.

## Quadro normativo

**Obbligatorio (Livello 1)** (per PRIV-POL-00):
- **RGPD UE** : Articolo 28(3)(c) (il responsabile del trattamento implementa le misure tecniche e organizzative appropriate ai sensi dell'Articolo 32); Articolo 32 (sicurezza del trattamento — pseudonimizzazione, cifratura, resilienza, ripristino, test)
- **LPD svizzera** : Articolo 9 (condizioni di ingaggio del responsabile del trattamento e obblighi di sicurezza dei dati associati)
- **ISO/IEC 27018:2025** : Controlli A.11.1–A.11.13

---

# Enunciati della politica: Obblighi di riservatezza (A.11.1)

Tutti i dipendenti e i collaboratori di [Organizzazione] con accesso ai sistemi contenenti DCP DEVONO essere vincolati da obblighi di riservatezza e non divulgazione scritti. Gli NDA DEVONO esplicitamente:

- Vietare l'utilizzo secondario, la conservazione personale o la divulgazione non autorizzata dei DCP
- Sopravvivere alla cessazione del rapporto di lavoro o dell'impegno
- Essere firmati prima che venga concesso l'accesso a qualsiasi sistema DCP

Gli NDA sono gestiti conformemente a ISMS-POL-A.6.3 (Accordi di riservatezza). La copertura NDA DEVE essere verificata durante i processi di onboarding e di uscita.

---

# Enunciati della politica: Restrizione delle copie cartacee (A.11.2)

La creazione di copie cartacee (stampe) contenenti DCP è **limitata**. La stampa di DCP richiede:

- Una giustificazione aziendale documentata (es. requisito normativo, pista di audit cartacea)
- L'autorizzazione del responsabile del team competente e la nota del RPD per le stampe ad alto volume
- Il ritiro immediato dalla stampante; i materiali DCP non devono essere lasciati incustoditi in aree condivise

I DCP stampati DEVONO essere gestiti secondo le procedure di scrivania libera ed eliminati conformemente al §11.7 (smaltimento sicuro delle copie cartacee). Ove tecnicamente fattibile, il software di gestione delle stampe o i controlli DLP DEVONO essere configurati per segnalare o limitare i lavori di stampa contenenti DCP; laddove l'applicazione tecnica non sia implementata, il ricorso ai controlli procedurali DEVE essere documentato dal RSSI con il monitoraggio compensativo identificato.

---

# Enunciati della politica: Controllo e registrazione nei log del ripristino dei dati (A.11.3)

Il ripristino dei DCP da backup o archivio è un'**operazione controllata** che richiede:

- Un'autorizzazione di ripristino documentata dal responsabile del team o dal responsabile dell'incidente
- La registrazione nei log di: identità dell'operatore, timestamp, sorgente del backup, portata dei dati ripristinati e riferimento all'autorizzazione
- Log di ripristino protetti contro le manomissioni (write-once o firmati crittograficamente)
- Esame trimestrale dei log di ripristino da parte del RSSI

Gli avvisi automatizzati DEVONO essere configurati per notificare il RSSI in tempo reale degli eventi di ripristino, consentendo il rilevamento di ripristini fuori schema senza attendere l'esame trimestrale dei log. I tentativi di ripristino non pianificati o non autorizzati DEVONO essere trattati come eventi di sicurezza e indagati ai sensi di ISMS-POL-A.5.24-28.

---

# Enunciati della politica: Supporti di archiviazione che lasciano i locali (A.11.4)

I supporti di archiviazione fisici (unità, nastri, supporti rimovibili) contenenti DCP che lasciano le strutture cloud di [Organizzazione] DEVONO essere:

- **Cifrati** utilizzando la cifratura approvata dell'intero disco o del volume con gestione delle chiavi conformemente a ISMS-POL-A.8.24, oppure
- **Fisicamente distrutti** secondo uno standard che impedisca il recupero dei dati (es. distruzione conforme a NIST SP 800-88) prima di lasciare i locali

I movimenti dei supporti DEVONO essere:
- Autorizzati dal RSSI o dal Responsabile Sicurezza Cloud
- Registrati in un registro dei movimenti dei supporti con documentazione della catena di custodia
- Tracciati fino alla destinazione finale (struttura di restituzione o distruzione)

---

# Enunciati della politica: Dispositivi di archiviazione portatili non cifrati (A.11.5)

L'utilizzo di supporti e dispositivi di archiviazione portatili non cifrati per l'archiviazione o il trasferimento di DCP è **vietato**. Questo divieto riguarda le chiavette USB, i dischi rigidi esterni, i laptop, i tablet e i telefoni cellulari.

Laddove i dispositivi portatili siano autorizzati per i DCP:
- La cifratura dell'intero disco che soddisfi gli standard approvati (AES-256 minimo) è **obbligatoria**
- Lo stato di cifratura del dispositivo DEVE essere verificato dall'IT prima che l'accesso ai DCP sia consentito
- La capacità di cancellazione remota DEVE essere abilitata per i dispositivi mobili

**La perdita o il furto** di qualsiasi dispositivo portatile che potenzialmente contenga DCP DEVE essere segnalato immediatamente al RSSI e al RPD e trattato come incidente di sicurezza DCP ai sensi di CLD-PII-POL-A.10.1 e ISMS-POL-A.5.24-28.

---

# Enunciati della politica: Cifratura dei DCP in transito (A.11.6)

I DCP trasmessi su reti pubbliche DEVONO essere cifrati. Requisiti:

- **TLS 1.3 richiesto** per tutte le nuove implementazioni; **TLS 1.2 consentito solo per le integrazioni esistenti** dove TLS 1.3 non è ancora tecnicamente fattibile, soggetto a un piano di remediation documentato e all'approvazione del RSSI
- **HTTPS obbligatorio** su tutte le interfacce web e gli endpoint API che gestiscono DCP; reindirizzamento da HTTP a HTTPS obbligatorio
- I certificati TLS DEVONO essere emessi da autorità di certificazione fidate e rinnovati prima della scadenza (rinnovo automatico preferito)
- La **trasmissione non cifrata** (HTTP semplice, FTP, SMTP senza STARTTLS) di DCP è vietata

Le configurazioni della suite di cifratura DEVONO essere esaminate annualmente rispetto alle best practice attuali (es. BSI TR-02102, NIST SP 800-52). I cifrari deboli (RC4, DES, 3DES, SSL 3.0, TLS 1.0, TLS 1.1) DEVONO essere disabilitati.

---

# Enunciati della politica: Smaltimento sicuro delle copie cartacee (A.11.7)

Le copie cartacee contenenti DCP DEVONO essere smaltite in modo sicuro:

- **Smaltimento individuale** : Triturazione a taglio incrociato al livello DIN 66399 P-5 (dimensione massima delle particelle 30 mm²) per i documenti contenenti DCP o categorie speciali; P-4 è accettabile per i documenti interni generali che non contengono DCP
- **Smaltimento in massa** : Servizi di distruzione certificati con certificato di distruzione fornito al richiedente
- **Contenitori per lo smaltimento** : Contenitori chiusi a chiave e con controllo degli accessi per i materiali DCP in tutti gli spazi di lavoro contenenti DCP

Lo smaltimento DEVE essere documentato. I certificati di distruzione DEVONO essere conservati per 3 anni.

---

# Enunciati della politica: ID utente univoci (A.11.8)

A ogni persona con accesso ai sistemi DCP DEVE essere assegnato un **identificatore utente univoco**. Gli account condivisi, generici o basati sui ruoli NON DEVONO essere utilizzati per accedere ai sistemi in cui i DCP vengono trattati o archiviati.

Gli ID univoci garantiscono che tutte le azioni sui DCP possano essere attribuite a un individuo specifico a fini di audit e accountability. Le eccezioni (es. account di servizio) richiedono l'approvazione del RSSI e controlli compensativi rafforzati (gestione degli accessi privilegiati, registrazione delle sessioni).

---

# Enunciati della politica: Gestione degli ID utente (A.11.9)

Gli identificatori utente per i sistemi DCP DEVONO essere gestiti attraverso un ciclo di vita documentato:

| Fase del ciclo di vita | Requisito |
|-----------------|-------------|
| **Provisioning** | Richiede un'autorizzazione documentata dal responsabile dell'utente e dal proprietario del sistema |
| **Revisione degli accessi** | Tutti gli account dei sistemi DCP esaminati almeno trimestralmente |
| **Cambio di ruolo** | Accesso aggiornato entro 1 giorno lavorativo dalla conferma del cambio di ruolo |
| **Cessazione** | Account disattivato entro 4 ore dalla partenza confermata dalle HR |
| **Account inattivi** | Account inattivi da 30 giorni sui sistemi DCP critici (45 giorni sui sistemi DCP meno sensibili) esaminati; sospesi in attesa di revisione; eliminati in assenza di giustificazione aziendale |

La gestione del ciclo di vita degli ID utente si integra con ISMS-POL-A.5.15-16-18 (IAM).

---

# Enunciati della politica: Registrazioni degli utenti autorizzati (A.11.10)

[Organizzazione] DEVE mantenere un **Registro degli utenti autorizzati** per ogni sistema DCP, che registra:

- Identità e ruolo di ogni individuo
- Portata dell'accesso concesso (lettura, scrittura, admin)
- Data di autorizzazione e responsabile che autorizza
- Data dell'ultima revisione

Il Registro degli utenti autorizzati DEVE essere:
- Esaminato e attestato dai proprietari dei sistemi almeno **trimestralmente**
- Messo a disposizione di qualsiasi titolare del trattamento dei DCP su richiesta — [Organizzazione] DEVE fornire a ciascun titolare del trattamento un **estratto limitato** che mostra solo il personale con accesso ai dati DCP di quel titolare del trattamento, non l'intero registro su tutti i clienti
- Aggiornato entro 1 giorno lavorativo da qualsiasi modifica all'accesso

---

# Enunciati della politica: Misure contrattuali (A.11.11)

Gli accordi di servizio tra [Organizzazione] e i titolari del trattamento dei DCP DEVONO includere disposizioni che disciplinano:

- Perimetro e finalità documentata del trattamento dei DCP
- Obblighi di sicurezza allineati all'Articolo 32 del RGPD e a questa politica
- Requisiti di notifica delle violazioni (notifica al titolare del trattamento entro 24 ore per CLD-PII-POL-A.10.1)
- Obblighi di assistenza ai diritti degli interessati (per CLD-PII-POL-A.2.1 e CLD-PII-POL-A.9)
- Diritti di audit: il titolare del trattamento (o il suo revisore designato) può verificare la conformità di [Organizzazione], esercitabile con un preavviso di almeno 30 giorni, non più di una volta per anno civile salvo che un incidente di sicurezza confermato giustifichi un audit aggiuntivo, e a spese del titolare del trattamento salvo che venga dimostrata una non conformità
- Requisiti di approvazione dei sub-responsabili del trattamento (per CLD-PII-POL-A.8.1)
- Restituzione o cancellazione dei DCP alla cessazione (per CLD-PII-POL-A.10.3)
- Legge applicabile e giurisdizione

Le condizioni contrattuali DEVONO essere riviste quando i requisiti normativi cambiano in modo significativo. Il Responsabile Legale/Conformità mantiene il modello standard di accordo di trattamento.

---

# Enunciati della politica: Trattamento dei DCP in sub-appalto (A.11.12)

[Organizzazione] DEVE imporre a tutti i sub-responsabili del trattamento, tramite contratti vincolanti, **obblighi equivalenti** a quelli di questa politica e dell'intera suite CLD-PII-POL-A.X. I contratti con i sub-responsabili del trattamento DEVONO:

- Rispecchiare gli obblighi di protezione dei dati dell'accordo tra titolare del trattamento e responsabile del trattamento
- Richiedere il consenso scritto preventivo di [Organizzazione] (e, per estensione, del titolare del trattamento dei DCP) prima di qualsiasi ulteriore sub-trattamento
- Includere i diritti di audit di [Organizzazione] sulla conformità del sub-responsabile del trattamento
- Richiedere la notifica delle violazioni a [Organizzazione] entro 12 ore dal rilevamento (consentendo a [Organizzazione] di adempiere al proprio obbligo di notifica al titolare del trattamento entro 24 ore ai sensi di CLD-PII-POL-A.10.1) — questo requisito di 12 ore è una **clausola obbligatoria** in tutti gli accordi con i sub-responsabili del trattamento; il Responsabile Legale/Conformità mantiene il modello standard di accordo con i sub-responsabili del trattamento
- Richiedere la restituzione o lo smaltimento dei DCP alla cessazione dell'impegno del sub-responsabile del trattamento

[Organizzazione] DEVE sottoporre i sub-responsabili del trattamento ad audit almeno annualmente (tramite questionario, revisione dei documenti o audit in loco) e rimane **pienamente responsabile** nei confronti dei titolari del trattamento dei DCP per le violazioni della conformità dei sub-responsabili del trattamento. I risultati degli audit dei sub-responsabili del trattamento DEVONO essere documentati e disponibili per i titolari del trattamento su richiesta.

---

# Enunciati della politica: Spazio di archiviazione dati precedentemente utilizzato (A.11.13)

[Organizzazione] DEVE garantire che i DCP non siano accessibili dallo spazio di archiviazione precedentemente allocato a un altro cliente (**prevenzione della remanenza dei dati**).

Prima che qualsiasi spazio di archiviazione venga riallocato a un nuovo carico di lavoro del cliente:
- Tutti i dati precedenti DEVONO essere **cancellati crittograficamente** (eliminazione delle chiavi di cifratura per i volumi cifrati — il metodo principale per l'archiviazione cloud) o sovrascritti secondo uno standard che impedisca il recupero
- La cancellazione DEVE essere documentata e il registro di dismissione conservato

Le procedure di dismissione DEVONO:
- Coprire tutti i tipi di archiviazione: archiviazione a blocchi (EBS, volumi), archiviazione di oggetti (contenuto dei bucket), archiviazione effimera delle istanze e archiviazione dei database
- Essere testate almeno **annualmente** campionando casualmente lo spazio di archiviazione riallocato e confermando l'assenza di dati residui
- Applicarsi ugualmente alla dismissione fisica dei supporti di archiviazione (vedere A.11.4)

Questo controllo è il fondamento dell'isolamento dei DCP multi-tenant. Qualsiasi violazione DEVE essere trattata come un potenziale incidente di sicurezza DCP.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI / Responsabile Sicurezza Cloud** | È proprietario di questa politica; garantisce che tutti i 13 controlli siano implementati e mantenuti; effettua la revisione annuale della sicurezza; gestisce il programma di movimenti dei supporti e di audit dei sub-responsabili del trattamento |
| **Responsabile della Protezione dei Dati (RPD)** | Esamina la politica annualmente per l'allineamento normativo; fornisce consulenza sulle condizioni contrattuali (A.11.11); supervisiona le valutazioni di adeguatezza dei sub-responsabili del trattamento |
| **Cloud Engineering** | Implementa i controlli tecnici (cifratura, configurazione TLS, cancellazione, registrazione nei log); testa le procedure di dismissione |
| **IT / Gestione delle identità** | Gestisce il ciclo di vita degli ID utente per A.11.8–A.11.10; mantiene il Registro degli utenti autorizzati; applica le politiche di accesso |
| **Responsabile Legale/Conformità** | Mantiene il modello standard di accordo di trattamento; esamina gli accordi con i sub-responsabili del trattamento; fornisce consulenza sulle clausole di giurisdizione e diritti di audit |
| **Risorse Umane** | Attiva la disattivazione degli account utente alla partenza; gestisce il processo di firma degli NDA durante l'onboarding |

---

# Requisiti in materia di prove

| Prova | Descrizione | Conservazione |
|-------|-------------|--------------|
| Registrazioni NDA | NDA firmati per tutto il personale con accesso ai DCP | Durata dell'impegno + 5 anni |
| Log di autorizzazione alle stampe | Registrazioni delle operazioni di stampa DCP autorizzate | 3 anni |
| Log di ripristino dei backup | Eventi di ripristino registrati nei log con registrazioni di autorizzazione | 3 anni |
| Registro dei movimenti dei supporti | Log dei movimenti fisici dei supporti con catena di custodia | 3 anni |
| Registrazioni di configurazione TLS / Cifratura | Documentazione attuale della suite di cifratura e della configurazione TLS | Attuale + versioni precedenti 5 anni |
| Certificati di distruzione | Certificati di smaltimento delle copie cartacee e dei supporti | 3 anni |
| Registro degli utenti autorizzati | Registrazioni degli accessi attestate trimestralmente per sistema DCP | 5 anni |
| Registrazioni degli audit dei sub-responsabili del trattamento | Risultati degli audit annuali per ogni sub-responsabile del trattamento | 5 anni |
| Registrazioni di dismissione dell'archiviazione | Registrazioni della cancellazione crittografica per evento di dismissione dell'archiviazione | 3 anni |
| Risultati dei test di dismissione | Risultati dei test annuali che confermano l'assenza di dati residui nell'archiviazione riallocata | 3 anni |

---

# Considerazioni di audit

I revisori che verificano la conformità a CLD-PII-POL-A.11 dovrebbero aspettarsi di trovare:

- Copertura NDA per tutto il personale con accesso ai DCP — nessuna eccezione
- TLS 1.2+ obbligatorio su tutte le interfacce di rete che gestiscono DCP; TLS 1.0/1.1 disabilitato
- Attestazioni trimestrali del Registro degli utenti autorizzati con rimozione tempestiva dei partenti e di coloro che cambiano ruolo
- Rapporti di audit dei sub-responsabili del trattamento per il periodo di audit che confermano l'applicazione di obblighi equivalenti
- Risultati dei test di dismissione dell'archiviazione che confermano l'assenza di remanenza dei dati tra i tenant
- Log di ripristino dei backup con registrazioni di autorizzazione per tutti gli eventi di ripristino

---

<!-- QA_VERIFIED: 2026-04-04 -->
