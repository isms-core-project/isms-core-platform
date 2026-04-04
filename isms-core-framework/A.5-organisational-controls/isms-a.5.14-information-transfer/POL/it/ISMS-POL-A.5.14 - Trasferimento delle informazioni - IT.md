<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.14-IT:framework:POL:a.5.14 -->
**ISMS-POL-A.5.14 — Trasferimento delle informazioni**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Trasferimento delle informazioni |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.14 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Politica iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore dei Sistemi Informativi (DSI)
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.12-13 (Classificazione ed etichettatura delle informazioni)
- ISMS-POL-A.8.24 (Utilizzo della crittografia)
- ISMS-POL-A.5.19-23 (Servizi cloud)
- ISMS-POL-A.6.6 (Accordi di riservatezza e non divulgazione)
- ISMS-IMP-A.5.14.1-UG/TG (Regole e procedure di trasferimento)
- ISMS-IMP-A.5.14.2-UG/TG (Valutazione della sicurezza dei canali)
- ISMS-IMP-A.5.14.3-UG/TG (Registro degli accordi di trasferimento)
- ISO/IEC 27001:2022 Controllo A.5.14

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per il trasferimento sicuro delle informazioni al fine di proteggerle durante la trasmissione attraverso tutti i tipi di canali e strutture di comunicazione.

**Perimetro**: Questa politica si applica a tutti i trasferimenti di informazioni, siano essi elettronici, fisici o verbali, inclusi i trasferimenti all'interno di [Organizzazione] e con parti esterne.

**Scopo**: Definire i requisiti organizzativi per la sicurezza del trasferimento delle informazioni. Questa politica stabilisce QUALI metodi di trasferimento sono approvati e CHI è autorizzato. Le procedure di attuazione (COME) sono documentate separatamente in ISMS-IMP-A.5.14 (varianti UG/TG).

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; FINMA, PCI DSS v4.0.1 (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sul controllo e perimetro

**ISO/IEC 27001:2022 Allegato A.5.14 — Trasferimento delle informazioni**

> *Regole, procedure o accordi per il trasferimento di informazioni devono essere in vigore per tutti i tipi di strutture di trasferimento all'interno dell'organizzazione e tra l'organizzazione e altre parti.*

**Obiettivi del controllo**: Proteggere la riservatezza, l'integrità e la disponibilità delle informazioni durante il trasferimento; garantire metodi di trasferimento appropriati in base alla sensibilità delle informazioni; stabilire accordi di trasferimento con le parti esterne; mantenere la responsabilità e le piste di audit per i trasferimenti.

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Applicabilità | Requisiti chiave |
|-----------|---------------|-----------------|
| **nLPD svizzera Artt. 16-17** | Tutti i trasferimenti di dati personali | Requisiti di trasferimento transfrontaliero |
| **ISO/IEC 27001:2022** | Ambito di certificazione | Controllo A.5.14 — Trasferimento delle informazioni |

**Livello 2 — Applicabilità condizionale**:

| Normativa | Condizione scatenante | Requisiti di trasferimento |
|-----------|----------------------|--------------------------|
| **RGPD dell'UE Artt. 44-49** | Elaborazione di dati personali UE | Garanzie per il trasferimento internazionale dei dati, SCC |
| **FINMA** | Istituto finanziario svizzero regolamentato | Sicurezza avanzata per i trasferimenti di dati finanziari |
| **Segreto bancario svizzero** | Dati dei clienti bancari | Controlli di trasferimento rigorosi |
| **PCI DSS v4.0.1** | Dati di carte di pagamento | Requisiti di cifratura per i dati del titolare della carta |
| **HIPAA** | Dati sanitari statunitensi | Accordi con i Business Associate |

**Livello 3 — Riferimento informativo**: ISO 27002:2022; NIST SP 800-53; CIS Controls v8.1; Linee guida ENISA sulla sicurezza dei trasferimenti di dati.

---

# Enunciati di politica

## Requisiti dei metodi di trasferimento

### Trasferimento elettronico

**Comunicazioni email**:

| Classificazione | Requisito |
|----------------|-----------|
| PUBBLICO | Email aziendale standard consentita |
| INTERNO | Solo email aziendale; i destinatari esterni richiedono una giustificazione aziendale documentata (scopo, destinatario, classificazione, scadenza dell'accesso) |
| RISERVATO | Email cifrata (TLS applicato) o piattaforma sicura di condivisione file |
| LIMITATO | Piattaforma cifrata end-to-end, verifica del destinatario richiesta |

**Controlli di sicurezza email**:

- Transport Layer Security (TLS) obbligatorio per tutta la posta elettronica in uscita
- S/MIME o equivalente per gli allegati RISERVATI/LIMITATI
- Limiti di dimensione email applicati (allegati >25 MB tramite piattaforma di condivisione file sicura)
- Politiche DLP attive per il rilevamento di schemi di dati sensibili
- Avvisi per destinatari esterni visualizzati prima dell'invio

**Trasferimento di file**:

| Metodo | Utilizzo consentito | Limite di classificazione |
|--------|---------------------|--------------------------|
| Condivisione file aziendale (SharePoint/OneDrive) | Trasferimenti interni | Fino a LIMITATO |
| Piattaforma sicura di trasferimento file | Trasferimenti esterni | Fino a LIMITATO |
| SFTP/SCP | Integrazioni di sistema | Fino a RISERVATO |
| Chiavette USB (cifrate) | Solo eccezione | Fino a RISERVATO |
| Condivisione file pubblica (Dropbox, Google Drive) | Mai per dati aziendali | Solo PUBBLICO (uso personale) |

**Trasferimento via web**: HTTPS obbligatorio per tutti i trasferimenti web; validazione dei certificati obbligatoria; le informazioni RISERVATE e LIMITATE DEVONO essere trasferite solo tramite servizi web approvati elencati nel Registro degli strumenti di trasferimento approvati; le altre destinazioni richiedono un'eccezione approvata (ISMS-REG-EXCEPTIONS).

### Trasferimento fisico

**Trasferimento di documenti**:

| Classificazione | Metodo di trasferimento |
|----------------|------------------------|
| PUBBLICO | Posta standard o corriere |
| INTERNO | Posta interna o corriere standard |
| RISERVATO | Busta sigillata, corriere tracciato, firma del destinatario |
| LIMITATO | Confezione doppiamente sigillata, corriere con vincolo, documentazione della catena di custodia |

**Trasferimento di supporti** (USB, hard disk, nastri di backup):

- Tutti i supporti rimovibili cifrati prima del trasferimento
- Inventario dei supporti registrato con numero di tracciamento
- Corriere sicuro con catena di custodia per RISERVATO+
- Supporti LIMITATI: corriere sicuro dedicato, imballaggi a prova di manomissione

**Trasferimento di persona**:

- Verificare l'identità del destinatario prima della consegna
- Documentare il trasferimento con riconoscimento della ricezione
- Informazioni LIMITATE: presenza di un testimone richiesta

### Trasferimento verbale

**Telefono/Videoconferenza**:

| Classificazione | Requisito |
|----------------|-----------|
| PUBBLICO/INTERNO | Sistemi aziendali standard |
| RISERVATO | Partecipanti verificati, nessuna registrazione senza consenso |
| LIMITATO | Solo canali sicuri/cifrati, verifica dei partecipanti |

**Discussioni di persona**: RISERVATO: luogo privato, nessun ascoltatore non autorizzato; LIMITATO: sala sicura, nessun dispositivo elettronico, solo partecipanti con necessità di sapere.

## Requisiti di trasferimento esterno

### Accordi di trasferimento

I trasferimenti esterni di classificazione INTERNO o superiore DEVONO richiedere:

**Elementi minimi dell'accordo**:

- Obblighi di gestione delle informazioni per il destinatario
- Utilizzo consentito e restrizioni alla divulgazione
- Requisiti di restituzione/distruzione
- Obblighi di notifica delle violazioni
- Diritti di audit dove appropriato

**Tipi di accordo**:

| Tipo di trasferimento | Accordo richiesto |
|----------------------|-------------------|
| Trasferimento unico | Riconoscimento di riservatezza |
| Relazione continuativa | NDA (per ISMS-POL-A.6.6) |
| Fornitore/Vendita | Accordo di trattamento dei dati (dove coinvolti dati personali) |
| Dati dei clienti | Accordo di servizio con termini di sicurezza |

### Trasferimenti transfrontalieri

I trasferimenti al di fuori della Svizzera/SEE DEVONO rispettare:

**Requisiti legali**:

- Verifica delle decisioni di adeguatezza (valutazione del paese)
- Clausole contrattuali standard (SCC) dove richiesto
- Misure supplementari per le giurisdizioni ad alto rischio; per i trasferimenti transfrontalieri di dati personali, DEVE essere completato e conservato nel Registro delle prove un documento di Valutazione del trasferimento internazionale (inclusa la base di adeguatezza/SCC, la decisione sulle misure supplementari e il riferimento all'approvazione del RPD)
- Approvazione del RPD per i trasferimenti di dati personali

**Requisiti tecnici**:

- Cifratura in transito obbligatoria
- Verifica della conformità alla residenza dei dati
- Registrazione e monitoraggio dei trasferimenti

**Destinazioni vietate**: Paesi soggetti a sanzioni; giurisdizioni senza protezioni legali adeguate (senza garanzie appropriate).

### Dati di clienti e terze parti

Gestione speciale per i dati appartenenti a parti esterne:

- Classificazione: Minimo RISERVATO per tutti i dati dei clienti
- Trasferimento: Per i requisiti del contratto con il cliente
- Documentazione: Log dei trasferimenti conservati per i requisiti contrattuali/normativi
- Notifica: Informare i proprietari dei dati dei trasferimenti dove richiesto dal contratto

## Controlli di trasferimento

### Autorizzazione

**Matrice di autorizzazione dei trasferimenti**:

| Classificazione | Trasferimento interno | Trasferimento esterno |
|----------------|----------------------|----------------------|
| PUBBLICO | Auto-autorizzato | Auto-autorizzato |
| INTERNO | Auto-autorizzato | Approvazione del responsabile |
| RISERVATO | Approvazione del responsabile | Proprietario delle informazioni + Responsabile |
| LIMITATO | Responsabile di dipartimento | Responsabile di dipartimento + RSSI |

### Registrazione e responsabilità

Tutti i trasferimenti RISERVATI e LIMITATI DEVONO essere registrati:

**Contenuto del log**: Data/ora del trasferimento; identificazione del mittente e del destinatario; descrizione delle informazioni (non il contenuto); metodo di trasferimento utilizzato; riferimento all'autorizzazione.

**Conservazione**: I log dei trasferimenti conservati per un minimo di 2 anni.

### Risposta agli incidenti

Fallimenti di trasferimento o compromissioni sospette: notifica immediata al RSSI per RISERVATO+; indagine per ISMS-POL-A.5.24-28 (Gestione degli incidenti); notifica al proprietario dei dati/Proprietario delle informazioni; le notifiche normative e contrattuali per le violazioni dei dati personali DEVONO essere gestite attraverso il processo di gestione degli incidenti (ISMS-POL-A.5.24-28) e la procedura di notifica delle violazioni della privacy dell'organizzazione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità di trasferimento |
|-------|--------------------------------|
| **Direzione generale** | Approvare la politica di trasferimento; autorizzare i trasferimenti esterni LIMITATI |
| **RSSI** | Definire i requisiti di trasferimento; approvare le piattaforme di trasferimento; supervisione degli incidenti |
| **Operazioni IT** | Implementare l'infrastruttura di trasferimento sicuro; gestire le piattaforme |
| **Proprietari delle informazioni** | Autorizzare i trasferimenti delle informazioni di proprietà; verificare l'adeguatezza del destinatario |
| **Responsabili di dipartimento** | Approvare i trasferimenti dipartimentali; garantire la conformità |
| **Tutto il personale** | Utilizzare metodi di trasferimento approvati; proteggere le informazioni durante il trasferimento |

## Percorso di escalation

- Incertezza sul metodo di trasferimento: Personale → Responsabile → RSSI
- Approvazione trasferimento esterno: Proprietario delle informazioni → Responsabile di dipartimento → RSSI (LIMITATO)
- Incidente di trasferimento: Personale → RSSI → Direzione generale (incidenti significativi)

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Revisione della sicurezza della piattaforma di trasferimento | Trimestrale | Operazioni IT | Report della piattaforma |
| Efficacia della politica DLP | Mensile | RSSI | Report DLP |
| Conformità ai trasferimenti transfrontalieri | Trimestrale | RPD | Documenti di conformità |
| Inventario degli accordi di trasferimento | Annuale | Consulente legale | Registro degli accordi |

**Metriche di governance**:

- Utilizzo del metodo di trasferimento approvato (obiettivo: 100%)
- Tempo di rimedio degli incidenti DLP (obiettivo: <24 ore)
- Conformità ai trasferimenti transfrontalieri (obiettivo: 100%)
- Copertura degli accordi di trasferimento (obiettivo: 100% per le relazioni continuative)

## Revisione della politica

- **Frequenza**: Annuale come minimo
- **Trigger**: Nuove tecnologie di trasferimento, cambiamenti normativi, incidenti di sicurezza
- **Revisori**: RSSI, RPD, Operazioni IT, Consulente legale
- **Approvazione**: Direzione generale

## Gestione delle eccezioni

**Eccezioni consentite**: Metodo di trasferimento alternativo quando il metodo approvato non è disponibile (con controlli compensativi); trasferimenti di emergenza con documentazione post-facto entro 24 ore; trasferimenti di sistemi legacy con piano di mitigazione documentato.

**Non ammissibile**: Trasferimento di informazioni LIMITATE tramite canali non approvati; trasferimenti transfrontalieri senza base legale; uso persistente di metodi di trasferimento non sicuri.

Tutte le eccezioni DEVONO essere registrate nel Registro delle eccezioni (ISMS-REG-EXCEPTIONS).

---

# Implementazione e riferimenti

**Controlli correlati**:

- A.5.12-13 (Classificazione ed etichettatura): Determina i requisiti di sicurezza del trasferimento
- A.5.19-23 (Servizi cloud): Requisiti delle piattaforme di trasferimento basate su cloud
- A.6.6 (Accordi di riservatezza): Accordi di trasferimento esterni
- A.8.24 (Utilizzo della crittografia): Standard di cifratura per i trasferimenti
- A.8.12 (Prevenzione della perdita di dati): Controlli DLP per il monitoraggio dei trasferimenti
- A.8.15 (Registrazione): Requisiti di registrazione dell'attività di trasferimento

**Integrazione dei controlli sovrapposti**: A.5.14 definisce i canali di trasferimento; A.8.24 specifica gli algoritmi; A.8.12 monitora le violazioni delle politiche.

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Trasferimento di informazioni** | Lo spostamento di informazioni da una posizione, sistema o persona a un'altra attraverso qualsiasi mezzo |
| **Struttura di trasferimento** | Qualsiasi tecnologia, apparecchiatura o servizio utilizzato per trasmettere informazioni (sistemi email, condivisione file, corrieri, ecc.) |
| **Trasferimento transfrontaliero** | Trasferimento di informazioni a un destinatario in un paese/giurisdizione diverso |
| **Clausole contrattuali standard (SCC)** | Termini contrattuali approvati dalla Commissione UE per i trasferimenti internazionali di dati |
| **Catena di custodia** | Registro documentato di tutti gli individui che hanno gestito le informazioni durante il trasferimento fisico |
| **Cifratura end-to-end** | Cifratura in cui solo il mittente e il destinatario previsto possono decifrare le informazioni |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per il trasferimento delle informazioni. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.14 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
