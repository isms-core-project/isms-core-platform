<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.24-IT:operational:OP-POL:a.8.24 -->
**ISMS-OP-POL-A.8.24 — Uso della crittografia**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Uso della crittografia |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.24 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.24 — Uso della crittografia

**Controlli Allegato A correlati**:

| Controllo | Relazione con la crittografia |
|-----------|-------------------------------|
| A.5.12–13 Classificazione e etichettatura delle informazioni | Determina i requisiti di cifratura per livello di classificazione |
| A.5.14 Trasferimento delle informazioni | Requisiti di cifratura per i dati in transito |
| A.5.23 Sicurezza delle informazioni per i servizi cloud | Cifratura a riposo e in transito per i dati ospitati nel cloud |
| A.5.31 Requisiti legali, normativi e regolamentari | Controlli sull'esportazione, obblighi di cifratura nLPD/GDPR |
| A.8.1 Dispositivi endpoint degli utenti | Cifratura completa del disco, controlli crittografici a livello di dispositivo |
| A.8.5 Autenticazione sicura | Protezione crittografica delle credenziali di autenticazione |
| A.8.10 Cancellazione delle informazioni | Cancellazione crittografica come metodo di eliminazione sicura |
| A.8.13 Backup delle informazioni | Requisiti di cifratura dei backup |
| A.8.20 Sicurezza della rete | TLS/IPsec per la cifratura del trasporto di rete |
| A.8.28 Codifica sicura | Uso di librerie crittografiche approvate nello sviluppo |

**Politiche interne correlate**:

- Politica di classificazione e gestione delle informazioni
- Politica di trasferimento delle informazioni
- Politica di controllo degli accessi
- Politica di backup
- Politica di sviluppo sicuro

---

# Politica sull'uso della crittografia

## Scopo

Lo scopo di questa politica è garantire l'uso corretto ed efficace della crittografia per proteggere la riservatezza, l'integrità e l'autenticità delle informazioni.

Questa politica supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative adeguate al rischio per proteggere i dati personali (compresi i dati personali degni di tutela particolare). Laddove l'organizzazione tratta dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR. La cifratura è una misura tecnica fondamentale per dimostrare la conformità agli obblighi di protezione dei dati nell'ambito di entrambi i quadri normativi.

## Ambito

Le informazioni riservate e personali trattate, archiviate o trasmesse su o nei sistemi e nelle applicazioni di proprietà, gestiti e controllati dall'organizzazione, ritenuti nell'ambito dalla dichiarazione di ambito ISO 27001.

Tutti i dipendenti e gli utenti terzi.

## Principio

Le informazioni sono protette da controlli crittografici basati sulla classificazione stabilita nella Politica di classificazione e gestione delle informazioni e sulla base della valutazione del rischio.

Devono essere utilizzate esclusivamente tecnologie e processi di cifratura approvati dall'organizzazione.

L'esportazione di tecnologie crittografiche o dati cifrati può essere soggetta a restrizioni normative, incluse le disposizioni svizzere sul controllo delle esportazioni e l'Accordo di Wassenaar. Il personale deve richiedere una consulenza al dipartimento legale qualora sia necessaria l'esportazione di tecnologie crittografiche o dati cifrati.

La gestione delle chiavi crittografiche si basa su standard riconosciuti dal settore, tra cui NIST SP 800-57 e le linee guida OWASP sulla gestione delle chiavi. Le chiavi crittografiche sono classificate come Riservato.

---

## Controlli crittografici

### Algoritmi approvati e lunghezze delle chiavi

L'organizzazione utilizzerà i seguenti standard crittografici minimi:

| Caso d'uso | Algoritmo | Requisito minimo |
|------------|-----------|-----------------|
| Cifratura simmetrica | AES | 256 bit |
| Cifratura asimmetrica | RSA | Minimo 2048 bit; 4096 bit raccomandato |
| Cifratura asimmetrica | ECDSA/ECDH | P-256 minimo; P-384 raccomandato |
| Funzioni hash | Famiglia SHA-2 | SHA-256 minimo; SHA-384/SHA-512 per usi ad alta garanzia |
| Firme digitali | RSA | Minimo 2048 bit; 4096 bit raccomandato |
| Firme digitali | ECDSA | P-256 minimo |
| Derivazione delle chiavi | PBKDF2, scrypt, Argon2 | Secondo le linee guida NIST correnti |

**Algoritmi vietati:** MD5, SHA-1, DES, 3DES, RC4, RSA sotto i 2048 bit. Non devono essere utilizzati per nessuno scopo.

L'organizzazione monitorerà gli standard crittografici post-quantistici del NIST (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA) e pianificherà la migrazione man mano che vengono stabilite le tempistiche di adozione. Sarà condotta una valutazione della cripto-agilità per identificare i sistemi e gli archivi dati che richiedono una pianificazione della migrazione PQC, dando priorità alle chiavi a lunga durata e ai dati con periodi di conservazione superiori a 10 anni.

### Transport Layer Security

Tutte le comunicazioni di rete che trasportano dati riservati o personali devono utilizzare trasporti cifrati:

- TLS 1.2 è la versione minima accettabile.
- TLS 1.3 è preferito e deve essere utilizzato ove supportato.
- TLS 1.0 e TLS 1.1 devono essere disabilitati su tutti i sistemi.
- SSL (tutte le versioni) deve essere disabilitato su tutti i sistemi.
- Devono essere abilitati solo i cipher suite che utilizzano AEAD (ad esempio, AES-GCM) ove fattibile.

### Cifratura di dispositivi mobili, laptop e supporti rimovibili

I dispositivi mobili, i laptop e i supporti rimovibili devono avere la cifratura completa del disco abilitata a livello hardware o del sistema operativo.

- La cifratura del dispositivo non deve essere disabilitata.
- L'accesso allo storage cifrato deve essere protetto da password, passphrase, PIN o autenticazione biometrica.
- Solo i supporti rimovibili di proprietà e gestiti dall'organizzazione possono essere utilizzati per archiviare dati riservati.

### Cifratura della posta elettronica

La posta elettronica non deve essere utilizzata per trasferire dati riservati o personali in formato non cifrato, in linea con la Politica di trasferimento delle informazioni.

Laddove i dati riservati devono essere inviati via e-mail, deve essere utilizzato un allegato cifrato con una lunghezza della chiave che soddisfi i requisiti degli algoritmi approvati sopra indicati.

L'organizzazione valuterà e approverà una soluzione di cifratura della posta elettronica adeguata alle proprie esigenze. Fino all'implementazione di una soluzione, come misura transitoria si utilizzeranno allegati di file cifrati con scambio di chiavi fuori banda.

### Cifratura di servizi web e cloud

I servizi web e cloud che trattano, archiviano o trasmettono dati riservati o personali devono implementare TLS 1.2 come minimo per proteggere i dati in transito.

Tutti i server devono disporre di un certificato valido rilasciato da un'Autorità di Certificazione riconosciuta. I proprietari dei sistemi sono responsabili del rinnovo dei certificati e di garantire che i sistemi vengano aggiornati prima della scadenza.

### Cifratura wireless

- WEP non deve essere utilizzato.
- WPA3 è preferito per tutte le reti wireless.
- La modalità WPA2 Enterprise con autenticazione 802.1X e cifratura AES è lo standard minimo accettabile.
- La modalità WPA2 Personal può essere utilizzata per reti non di produzione con una passphrase casuale di almeno 16 caratteri e cifratura AES.

### Cifratura dei backup

I backup contenenti dati riservati o personali devono essere cifrati utilizzando tecnologia di cifratura approvata dall'organizzazione che soddisfi i requisiti minimi degli algoritmi sopra indicati.

La cifratura dei backup non deve basarsi esclusivamente su meccanismi proprietari del fornitore senza documentata garanzia dello standard di cifratura utilizzato.

### Cifratura dei database

I database contenenti informazioni riservate o dati personali devono essere cifrati a riposo a livello applicativo del database o a livello di disco/volume.

Dove viene utilizzata la cifratura completa del disco o del volume, la cancellazione crittografica (distruzione della chiave di cifratura) può essere utilizzata come metodo valido di eliminazione sicura, a condizione che il rischio sia valutato e l'approccio sia documentato e approvato.

### Cifratura dei dati in movimento

Il trasferimento di informazioni riservate e personali deve utilizzare canali cifrati. La cifratura è richiesta per:

- Il trasporto di file sensibili (SFTP, SCP o equivalente trasferimento cifrato).
- Tutto il traffico di rete per l'accesso remoto (VPN o equivalente).
- Query di database o chiamate a servizi web che trasmettono dati sensibili.
- Accesso privilegiato ad apparecchiature di rete o server (SSH; Telnet è vietato).

### Bluetooth

Il Bluetooth non deve essere utilizzato come metodo di comunicazione per dati riservati, personali o altrimenti sensibili non cifrati. Si veda la Politica di trasferimento delle informazioni.

---

## Gestione delle chiavi crittografiche

### Generazione delle chiavi

Le chiavi crittografiche devono essere generate all'interno di moduli crittografici con almeno conformità FIPS 140-2 o FIPS 140-3, o garanzia validata equivalente.

Qualsiasi valore casuale richiesto per la generazione delle chiavi deve essere generato all'interno del modulo crittografico utilizzando un generatore di bit casuali validato.

I moduli crittografici hardware (HSM) sono preferiti rispetto ai moduli software per la protezione delle chiavi di alto valore.

### Distribuzione delle chiavi

Le chiavi devono essere trasportate utilizzando canali sicuri. Il materiale crittografico non deve essere trasmesso in chiaro su alcuna rete.

### Archiviazione delle chiavi

- Le chiavi non devono mai essere archiviate in formato testo in chiaro.
- Le chiavi devono essere archiviate in un vault crittografico, HSM o servizio di gestione delle chiavi (KMS) cloud.
- Le chiavi non devono essere codificate nel codice sorgente, archiviate in file di configurazione in chiaro o condivise tramite e-mail o messaggistica. Questo si estende a chiavi API, token, credenziali di servizio e altri segreti — questi devono essere gestiti tramite una soluzione dedicata di gestione dei segreti (ad esempio, AWS KMS, Azure Key Vault, HashiCorp Vault o equivalente). I segreti non richiedono gli stessi standard di cifratura a riposo delle chiavi di cifratura dei dati, ma non devono mai essere archiviati in chiaro e devono essere ruotati secondo i periodi di rotazione delle chiavi sopra indicati.
- Le chiavi di cifratura delle chiavi (KEK) utilizzate per avvolgere le chiavi archiviate devono essere almeno altrettanto forti delle chiavi che proteggono.
- Le chiavi devono avere protezioni di integrità applicate durante l'archiviazione.

### Controllo degli accessi alle chiavi

L'accesso alle chiavi crittografiche deve seguire il principio del privilegio minimo.

- L'accesso amministrativo e operativo alle chiavi deve essere separato ove possibile.
- L'autenticazione a più fattori (AMF) deve essere richiesta per i custodi delle chiavi.
- Deve essere mantenuto un registro delle persone con accesso al materiale crittografico.

### Rotazione delle chiavi

I periodi di rotazione delle chiavi devono essere definiti in base al tipo di chiave, al rischio e ai requisiti normativi.

Le chiavi devono essere ruotate immediatamente in caso di compromissione sospetta o confermata, indipendentemente dalla rotazione programmata.

**Periodi minimi di rotazione delle chiavi:**

| Tipo di chiave | Durata massima |
|----------------|----------------|
| Certificati TLS/SSL | 398 giorni (secondo il baseline del CA/Browser Forum) |
| Chiavi di cifratura dati simmetriche (AES) | 2 anni (o secondo i limiti del periodo di crittografia NIST SP 800-57) |
| Coppie di chiavi asimmetriche (RSA/ECDSA) | 3 anni |
| Chiavi API e token di servizio | 90 giorni (estendibili a 1 anno con accettazione del rischio documentata) |
| Chiavi di cifratura dei database | 1 anno |

Periodi di rotazione più brevi possono essere richiesti in base alla valutazione del rischio o ai requisiti normativi.

### Deposito e backup delle chiavi

Il materiale crittografico deve essere sottoposto a backup per consentire il recupero dei dati cifrati.

- L'archiviazione delle chiavi di backup deve essere cifrata utilizzando almeno lo stesso livello di garanzia delle chiavi operative.
- Le chiavi di firma non devono essere depositate in garanzia (escrow).
- Le chiavi di cifratura possono essere depositate in garanzia dove i requisiti aziendali lo giustificano.

### Compromissione e recupero delle chiavi

Un piano di recupero in caso di compromissione delle chiavi deve essere documentato, testato annualmente e mantenuto come procedura di riferimento. Il piano deve includere:

- Informazioni di contatto del personale da notificare e di coloro responsabili delle azioni di recupero.
- Il metodo e le procedure di re-keying.
- Un inventario di tutte le chiavi crittografiche e il loro utilizzo.
- Identificazione di tutti i dati o altre chiavi protette dalla chiave compromessa.
- Monitoraggio delle operazioni di re-keying per confermare il completamento.

### Trust store

I trust store devono essere protetti contro l'iniezione di certificati radice non autorizzati. I controlli di accesso devono essere gestiti e applicati per entità e applicazione.

Deve essere implementato un processo sicuro per l'aggiornamento del trust store.

### Librerie crittografiche

Devono essere utilizzate solo librerie crittografiche affidabili che siano attivamente mantenute, regolarmente aggiornate e validate da organizzazioni terze (ad esempio, NIST/FIPS, Common Criteria).

Le implementazioni crittografiche personalizzate non devono essere sviluppate se non specificamente approvate dal RSSI con giustificazione documentata.

---

## Facoltativo: controlli per i dati delle carte di pagamento (PCI DSS)

*Applicabile solo se vengono trattati dati di carte di pagamento ed esiste un ambito PCI.*

Se esiste un ambito PCI, si applicano i seguenti requisiti aggiuntivi:

- Le chiavi segrete e private utilizzate per cifrare/decifrare i dati dei titolari di carta devono essere archiviate cifrate con una chiave di cifratura delle chiavi (KEK) almeno altrettanto forte della chiave di cifratura dei dati, archiviate separatamente dalla chiave di cifratura dei dati, oppure all'interno di un dispositivo approvato PTS o di un HSM.
- La cifratura dell'ambiente dei dati dei titolari di carta deve soddisfare i requisiti PCI DSS in aggiunta a questa politica.

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

- **Inventario crittografico** (algoritmi, lunghezze delle chiavi, protocolli in uso nei sistemi) — *mantenuto trimestralmente dalla sicurezza IT*
- **Risultati delle scansioni della configurazione TLS** (ad esempio, SSL Labs, testssl.sh) — *scansioni automatizzate mensili*
- **Inventario dei certificati e registri di monitoraggio della scadenza** — *monitoraggio automatizzato, rivisto mensilmente*
- **Log di accesso al KMS e tracce di audit sull'utilizzo delle chiavi** — *conservati per 12 mesi, rivisti trimestralmente*
- **Registri di rotazione delle chiavi** — *registrati nel KMS, verificati semestralmente*
- **Documentazione di configurazione della cifratura** per database, backup, endpoint — *rivista annualmente*
- **Piano di recupero in caso di compromissione delle chiavi** (documentato e testato annualmente)

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, audit di configurazione tecnica, scansioni TLS/certificati, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere comunicate al Team di revisione della direzione.

## Non conformità

Un dipendente che si constata abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare le modifiche agli standard crittografici, le minacce emergenti (inclusi gli sviluppi della crittografia post-quantistica), le modifiche normative e le lezioni apprese dagli incidenti.

---

# Aree della norma ISO 27001 trattate

Politica sull'uso della crittografia — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.1 Dispositivi endpoint degli utenti |
| | **8.24 Uso della crittografia** |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati |
| OPDo svizzera | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (cifratura come misura adeguata) |
| ISO/IEC 27001:2022 | Controllo Allegato A 8.24 — Uso della crittografia |
| ISO/IEC 27002:2022 | Sezione 8.24 — Guida all'implementazione dei controlli crittografici |
| NIST SP 800-57 | Raccomandazioni per la gestione delle chiavi |

---

<!-- QA_VERIFIED: 2026-04-03 -->
