<!-- ISMS-CORE:REF:ISMS-REF-PCI-DSS-IT-payment-card-industry-data-security:framework:REF:pci-dss -->
**ISMS-REF-PCI-DSS — Riferimento ai requisiti PCI DSS**
**Requisiti di sicurezza dei dati del settore delle carte di pagamento (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento ai requisiti PCI DSS |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-PCI-DSS |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | RSSI (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale (o in seguito ad aggiornamenti della versione PCI DSS)
**Distribuzione**: Team di elaborazione dei pagamenti, RSSI, Conformità, Operazioni IT

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del SGSI.
- Questo documento NON definisce requisiti obbligatori a meno che [Organizzazione] non elabori carte di pagamento.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

**Determinazione dell'applicabilità**: I requisiti PCI DSS si applicano SOLO SE [Organizzazione] archivia, elabora o trasmette dati dei titolari di carta (CHD); ha accesso all'Ambiente dei Dati dei Titolari di Carta (CDE); è un esercente che accetta pagamenti con carta di credito/debito; è un fornitore di servizi di pagamento o un elaboratore di pagamenti; oppure è designata dai circuiti di pagamento come soggetta alla conformità.

---

# Panoramica e applicabilità PCI DSS

## Cos'è il PCI DSS?

Il **Payment Card Industry Data Security Standard (PCI DSS)** è uno standard globale di sicurezza delle informazioni progettato per proteggere i dati delle carte di pagamento.

**Organismo di gestione**: PCI Security Standards Council (PCI SSC) — fondato dai principali circuiti di pagamento (Visa, Mastercard, American Express, Discover, JCB).

**Versione attuale**: **PCI DSS v4.0.1** (rilasciato a marzo 2024)
- In vigore dal: 31 marzo 2024
- Nuovi requisiti introdotti gradualmente entro il 31 marzo 2025

## Chi deve conformarsi al PCI DSS?

**Qualsiasi organizzazione che archivia, elabora o trasmette dati dei titolari di carta**:

| Tipo di entità | Descrizione | Esempi |
|---------------|-------------|--------|
| **Esercenti** | Accettano carte di pagamento | Rivenditori, e-commerce, ristoranti, hotel |
| **Fornitori di servizi** | Elaborano, archiviano o trasmettono CHD per conto di esercenti | Gateway di pagamento, elaboratori, hosting provider |
| **Istituti finanziari** | Emettono carte di pagamento o acquisiscono transazioni | Banche, unioni di credito, reti di pagamento |
| **Fornitori POS** | Forniscono sistemi o applicazioni POS | Fornitori di software POS, produttori di terminali |

## Livelli degli esercenti (Visa)

| Livello | Volume di transazioni (annuo) | Requisito di convalida |
|---------|------------------------------|------------------------|
| **Livello 1** | > 6 milioni di transazioni Visa | ROC annuale da parte di QSA + scansioni trimestrali |
| **Livello 2** | 1-6 milioni di transazioni Visa | SAQ annuale + scansioni trimestrali |
| **Livello 3** | 20.000 - 1 milione di transazioni e-commerce Visa | SAQ annuale + scansioni trimestrali |
| **Livello 4** | < 20.000 transazioni e-commerce Visa O < 1 milione totale | SAQ annuale + scansioni trimestrali |

## Dati dei titolari di carta (CHD) e dati di autenticazione sensibili (SAD)

**Dati dei titolari di carta (CHD)**:
- **Numero di conto primario (PAN)**: Il numero della carta di pagamento a 13-19 cifre
- **Nome del titolare**: Nome sulla carta
- **Data di scadenza**: Data di scadenza della carta
- **Codice di servizio**: Codice a 3 cifre sulla banda magnetica

**Dati di autenticazione sensibili (SAD)** — NON devono essere archiviati dopo l'autorizzazione:
- **Dati completi della banda magnetica** (Track 1, Track 2 o dati equivalenti del chip)
- **Codice/valore di verifica della carta** (CVV/CVC/CVV2/CID — codice a 3 o 4 cifre)
- **PIN / Blocco PIN**

**Regola critica**: I SAD NON devono MAI essere archiviati dopo il completamento dell'autorizzazione della transazione, anche se cifrati.

## Ambiente dei Dati dei Titolari di Carta (CDE)

**Definizione**: Le persone, i processi e le tecnologie che archiviano, elaborano o trasmettono dati dei titolari di carta o SAD, inclusi i sistemi connessi.

**Strategie di riduzione del perimetro**:
- **Tokenizzazione**: Sostituire il PAN con un token non sensibile
- **Cifratura punto-a-punto (P2PE)**: Cifrare al punto di ingresso, decifrare fuori dall'ambiente dell'esercente
- **Segmentazione di rete**: Isolare il CDE dal resto della rete
- **Ridurre l'archiviazione**: Non archiviare CHD se non necessario
- **Esternalizzazione**: Usare elaboratori di pagamento validati

## Determinazione dell'applicabilità

| Criterio | Stato | Prova |
|----------|-------|-------|
| Archivia dati dei titolari di carta (PAN) | ⬜ Sì ⬜ No | |
| Elabora dati dei titolari di carta (PAN) | ⬜ Sì ⬜ No | |
| Trasmette dati dei titolari di carta (PAN) | ⬜ Sì ⬜ No | |
| Ha sistemi connessi al CDE | ⬜ Sì ⬜ No | |
| Fornisce servizi a entità che gestiscono CHD | ⬜ Sì ⬜ No | [Tipo di fornitore di servizi] |

---

# Struttura PCI DSS — 6 obiettivi di controllo e 12 requisiti

```
┌────────────────────────────────────────────────────────────────┐
│          STRUTTURA PCI DSS v4.0.1                              │
├────────────────────────────────────────────────────────────────┤
│  COSTRUIRE E MANTENERE UNA RETE E SISTEMI SICURI               │
│    1. Installare e mantenere controlli di sicurezza della rete │
│    2. Applicare configurazioni sicure a tutti i componenti     │
├────────────────────────────────────────────────────────────────┤
│  PROTEGGERE I DATI DEI TITOLARI DI CARTA                       │
│    3. Proteggere i dati di conto archiviati                    │
│    4. Proteggere i CHD con crittografia forte durante la       │
│       trasmissione su reti pubbliche aperte                    │
├────────────────────────────────────────────────────────────────┤
│  MANTENERE UN PROGRAMMA DI GESTIONE DELLE VULNERABILITÀ        │
│    5. Proteggere tutti i sistemi e le reti da software dannoso │
│    6. Sviluppare e mantenere sistemi e software sicuri         │
├────────────────────────────────────────────────────────────────┤
│  IMPLEMENTARE SOLIDE MISURE DI CONTROLLO DEGLI ACCESSI         │
│    7. Limitare l'accesso ai CHD in base al bisogno di sapere   │
│    8. Identificare gli utenti e autenticare l'accesso          │
│    9. Limitare l'accesso fisico ai CHD                         │
├────────────────────────────────────────────────────────────────┤
│  MONITORARE E TESTARE REGOLARMENTE LE RETI                     │
│   10. Registrare e monitorare tutti gli accessi                │
│   11. Testare regolarmente la sicurezza di sistemi e reti      │
├────────────────────────────────────────────────────────────────┤
│  MANTENERE UNA POLITICA DI SICUREZZA DELLE INFORMAZIONI        │
│   12. Supportare la sicurezza con politiche e programmi        │
└────────────────────────────────────────────────────────────────┘
```

---

# Requisiti dettagliati

## Requisito 1: Installare e mantenere controlli di sicurezza della rete

**Sotto-requisiti chiave**: Regole del firewall documentate e giustificate; revisione delle regole almeno ogni 6 mesi; traffico in entrata e in uscita limitato al necessario; firewall tra reti wireless e CDE; protezione WAF per le applicazioni web accessibili da Internet.

**Mappatura ISO 27001:2022**: A.8.20; A.8.21; A.8.22; A.8.23

---

## Requisito 2: Applicare configurazioni sicure a tutti i componenti

**Sotto-requisiti chiave**: Password predefinite dei fornitori cambiate prima della produzione; servizi e protocolli non sicuri rimossi o disabilitati; accesso amministrativo non via console cifrato con crittografia forte; reti wireless sicure con WPA2/WPA3.

**Mappatura ISO 27001:2022**: A.8.9; A.8.19; A.8.1

---

## Requisito 3: Proteggere i dati di conto archiviati

**Sotto-requisiti chiave**:

**Regola critica — Non archiviare SAD dopo l'autorizzazione**:
- I dati della banda magnetica completa NON possono essere archiviati
- Il CVV/CVV2 NON può essere archiviato
- Il PIN NON può essere archiviato
- **Anche se cifrati, questi dati non possono essere archiviati dopo l'autorizzazione**

**Protezione del PAN**:
- Il PAN deve essere mascherato quando visualizzato (prime 6 e ultime 4 cifre al massimo)
- Il PAN deve essere reso illeggibile quando archiviato (cifratura, troncamento, hashing, tokenizzazione)

**Gestione delle chiavi crittografiche**: Procedure per la gestione delle chiavi definite e attuate; chiavi archiviate in modo sicuro; rotazione delle chiavi definita; custodi delle chiavi formalmente designati.

**Mappatura ISO 27001:2022**: A.8.24; A.8.10; A.8.11

---

## Requisito 4: Proteggere i CHD con crittografia forte durante la trasmissione

**Sotto-requisiti chiave**: Crittografia forte e protocolli sicuri proteggono il PAN durante la trasmissione su reti pubbliche aperte; il PAN non viene inviato tramite tecnologie di messaggistica degli utenti finali (email, SMS, chat).

**Standard di cifratura**: TLS 1.2 minimo (TLS 1.3 preferito); nessun SSL, nessuna versione TLS precedente.

**Mappatura ISO 27001:2022**: A.8.24; A.5.14

---

## Requisito 5: Proteggere tutti i sistemi e le reti da software dannoso

**Sotto-requisiti chiave**: Soluzioni anti-malware distribuite su tutti i sistemi comunemente colpiti; anti-malware aggiornato, attivo e in registrazione; meccanismi anti-phishing mantenuti e valutati periodicamente; meccanismi anti-phishing tecnici implementati.

**Mappatura ISO 27001:2022**: A.8.7; A.5.7

---

## Requisito 6: Sviluppare e mantenere sistemi e software sicuri

**Sotto-requisiti chiave**:

**Gestione delle vulnerabilità e delle patch**:
- **Vulnerabilità critiche**: Applicazione delle patch entro 30 giorni (massimo)
- **Vulnerabilità alte**: Secondo la classificazione del rischio (tipicamente 30-90 giorni)
- **Altre vulnerabilità**: Secondo un approccio basato sul rischio

**Sviluppo sicuro**:
- Personale addetto allo sviluppo formato sulla codifica sicura
- Revisioni del codice per il software personalizzato prima della produzione
- Tecniche di ingegneria del software per prevenire vulnerabilità comuni

**Protezione delle applicazioni web pubblicamente accessibili**:
- WAF (Web Application Firewall) o soluzione tecnica automatizzata equivalente
- Tecniche di integrità degli script delle pagine di pagamento

**Mappatura ISO 27001:2022**: A.8.8; A.8.25-8.33

---

## Requisito 7: Limitare l'accesso ai CHD in base al bisogno di sapere

**Sotto-requisiti chiave**: Accesso concesso in base alla classificazione e alla funzione lavorativa; accesso assegnato in base al minimo privilegio; diritti di accesso rivisti almeno ogni 6 mesi; sistema di controllo degli accessi configurato con principio "nega tutto".

**Mappatura ISO 27001:2022**: A.5.15; A.5.18; A.8.2; A.8.3

---

## Requisito 8: Identificare gli utenti e autenticare l'accesso ai componenti

**Sotto-requisiti chiave**:

**AMF (Autenticazione Multi-Fattore)**:
- AMF obbligatoria per tutti gli accessi al CDE
- AMF per tutti gli accessi alla rete dell'entità (remoti e interni)
- AMF per tutti gli accessi amministrativi
- AMF resistente al phishing per il personale con accesso amministrativo *(Nuovo v4.0.1)*
- AMF deve utilizzare fattori di due categorie diverse

**Password e passphrase**:
- Minimo 12 caratteri (o 8 se il sistema non supporta 12) *(Aggiornato v4.0.1)*
- Blocco dell'account dopo 10 tentativi falliti (massimo)

**Gestione degli account**: ID univoco assegnato a ogni persona; account condivisi vietati (salvo approvazione esplicita); account di servizi applicativi gestiti per prevenire l'uso improprio.

**Mappatura ISO 27001:2022**: A.5.16; A.5.17; A.8.5

---

## Requisito 9: Limitare l'accesso fisico ai CHD

**Sotto-requisiti chiave**: Controlli di accesso fisico per limitare l'accesso ai sistemi CDE; procedure di accesso per i visitatori con sistema di badge; log degli accessi fisici rivisti almeno ogni 3 mesi; media contenenti CHD archiviati in luoghi sicuri; media distrutti in modo sicuro quando non più necessari (triturazione, incenerimento, smagnetizzazione); dispositivi POI protetti da manomissione.

**Mappatura ISO 27001:2022**: A.7.1-7.4; A.7.7; A.7.8; A.7.10; A.7.14

---

## Requisito 10: Registrare e monitorare tutti gli accessi

**Sotto-requisiti chiave**:

**Registrazione**: Log di audit abilitati per tutti i componenti; i log di audit catturano: ID utente, tipo di evento, data/ora, successo/fallimento, origine, identità del sistema interessato; log di audit protetti da modifiche non autorizzate; log di audit conservati per almeno 12 mesi (minimo 3 mesi immediatamente disponibili).

**Monitoraggio**: Log rivisti almeno una volta al giorno; meccanismi automatizzati di alerta per anomalie/attività sospette *(Nuovo v4.0.1)*; sincronizzazione temporale implementata (NTP).

**Mappatura ISO 27001:2022**: A.8.15; A.8.16

---

## Requisito 11: Testare regolarmente la sicurezza di sistemi e reti

**Sotto-requisiti chiave**: Scansioni delle vulnerabilità interne almeno ogni 3 mesi; scansioni delle vulnerabilità esterne (ASV) almeno ogni 3 mesi (4 scansioni con esito positivo richieste annualmente); test di penetrazione interni almeno ogni 12 mesi; test di penetrazione esterni almeno ogni 12 mesi; controlli di segmentazione testati (se viene usata la segmentazione della rete per il perimetro); meccanismi di rilevamento delle modifiche (FIM) distribuiti.

**Mappatura ISO 27001:2022**: A.8.8; A.5.7; A.8.34

---

## Requisito 12: Supportare la sicurezza delle informazioni con politiche e programmi

**Sotto-requisiti chiave**: Politica di sicurezza delle informazioni stabilita, documentata, comunicata e rivista almeno annualmente; analisi del rischio mirata eseguita almeno ogni 12 mesi; perimetro PCI DSS documentato e convalidato annualmente; formazione di sensibilizzazione alla sicurezza completata da tutto il personale (all'assunzione e almeno ogni 12 mesi); formazione su phishing e ingegneria sociale fornita *(Nuovo v4.0.1)*; piano di risposta agli incidenti creato e testato almeno annualmente; responsabilità executive ultime per la protezione dei CHD.

**Mappatura ISO 27001:2022**: A.5.1; A.5.36; A.6.3; A.5.24-5.28; A.5.19-5.23

---

# Nuovi requisiti PCI DSS v4.0.1 principali (in vigore dal 31 marzo 2025)

| Categoria | Requisiti chiave |
|-----------|-----------------|
| **Espansione AMF** | AMF da due categorie diverse (Req. 8.3.5); AMF resistente al phishing per amministratori (Req. 8.3.6); AMF per account applicativi/di sistema privilegiati (Req. 8.3.7) |
| **Autenticazione migliorata** | Password minimo 12 caratteri — precedentemente 7 (Req. 8.5.1) |
| **Crittografia** | Hashing con chiave (HMAC) richiesto per l'hashing del PAN (Req. 3.5.1.1); inventario di chiavi e certificati affidabili (Req. 4.2.1.1) |
| **Sicurezza applicazioni web** | NSC tra Internet e applicazioni web/WAF (Req. 1.4.5); tecniche di integrità degli script per le pagine di pagamento (Req. 6.4.2) |
| **Anti-phishing** | Meccanismi anti-phishing mantenuti e valutati (Req. 5.3.2); formazione su phishing e ingegneria sociale (Req. 12.6.3.1) |
| **Registrazione e monitoraggio** | Avvisi automatizzati per anomalie/attività sospette (Req. 10.4.1.1) |

---

# Convalida e conformità

## Metodi di convalida

**Report on Compliance (ROC)**:
- Richiesto per: Esercenti di livello 1, fornitori di servizi
- Eseguito da: Qualified Security Assessor (QSA)
- Frequenza: Annuale

**Self-Assessment Questionnaire (SAQ)**:
- Richiesto per: Esercenti di livello 2-4
- Frequenza: Annuale

**Principali tipi di SAQ**:

| Tipo SAQ | Applicabilità | Requisiti |
|----------|---------------|-----------|
| **SAQ A** | Transazioni senza presenza fisica della carta, completamente esternalizzate | 22 requisiti |
| **SAQ A-EP** | E-commerce, parzialmente esternalizzate | 169 requisiti |
| **SAQ C** | Sistemi applicativi di pagamento connessi a Internet, nessuna archiviazione elettronica | 158 requisiti |
| **SAQ D - Esercente** | Tutti gli altri esercenti che non rientrano nelle categorie precedenti | 337 requisiti |
| **SAQ D - Fornitore di servizi** | Fornitori di servizi ammissibili al SAQ | 337 requisiti |
| **SAQ P2PE** | Terminali hardware che utilizzano soluzioni P2PE validate | 32 requisiti |

**Scansioni trimestrali della rete (ASV)**:
- Richieste per: Tutte le entità con sistemi accessibili da Internet nel CDE
- Eseguite da: Approved Scanning Vendor (ASV)
- Frequenza: Almeno trimestrale
- Criteri di superamento: Nessuna vulnerabilità con punteggio CVSS ≥ 4.0

---

# Mappatura ISO 27001:2022 — PCI DSS

## Matrice di mappatura dei controlli

| Requisito PCI DSS | Controllo ISO 27001:2022 | Lacuna |
|-------------------|--------------------------|--------|
| 1. Controlli di sicurezza della rete | A.8.20-8.23 | PCI DSS: Regole del firewall più prescrittive |
| 2. Configurazioni sicure | A.8.9; A.8.19; A.8.1 | Allineato |
| 3. Proteggere i CHD archiviati | A.8.24; A.8.10; A.8.11 | **Specifico PCI DSS**: Divieto di archiviazione SAD, requisiti di cifratura severi |
| 4. Proteggere i CHD in trasmissione | A.8.24; A.5.14 | PCI DSS: Impone TLS 1.2+, vieta la messaggistica degli utenti finali |
| 5. Proteggere da software dannoso | A.8.7; A.5.7 | PCI DSS: Aggiunge requisiti anti-phishing (v4.0) |
| 6. Sviluppo sicuro | A.8.8; A.8.25-8.33 | PCI DSS: Scadenze prescrittive per le patch (30 giorni per quelle critiche) |
| 7. Limitare l'accesso per bisogno di sapere | A.5.15; A.5.18; A.8.2-8.3 | Allineato |
| 8. Identificare e autenticare | A.5.16-5.17; A.8.5 | **Specifico PCI DSS**: AMF obbligatoria, password da 12 caratteri |
| 9. Limitare l'accesso fisico | A.7.1-7.4; A.7.7-7.8; A.7.10; A.7.14 | PCI DSS: Aggiunge protezione dei dispositivi POI |
| 10. Registrare e monitorare | A.8.15-8.16 | PCI DSS: Conservazione prescrittiva di 12 mesi, revisione giornaliera |
| 11. Testare la sicurezza | A.8.8; A.5.7; A.8.34 | **Specifico PCI DSS**: Scansioni ASV trimestrali, test di penetrazione annuali |
| 12. Politica di sicurezza e programma | A.5.1; A.5.36; A.6.3; A.5.24-5.28; A.5.19-5.23 | PCI DSS: Aggiunge analisi del rischio mirata, responsabilità executive |

## Lacune principali tra ISO 27001:2022 e PCI DSS

1. **Requisiti specifici per i CHD**: ISO 27001 — protezione generale dei dati; PCI DSS — gestione esplicita dei CHD, divieto di archiviazione SAD, mascheramento del PAN
2. **Controlli tecnici prescrittivi**: ISO 27001 — selezione dei controlli basata sul rischio; PCI DSS — controlli obbligatori (firewall, cifratura, AMF, anti-malware)
3. **Frequenza di test e convalida**: ISO 27001 — nessuna frequenza di test obbligatoria; PCI DSS — scansioni ASV trimestrali, test di penetrazione annuali, convalida annuale della conformità
4. **Responsabilità executive**: ISO 27001 — impegno della direzione; PCI DSS — responsabilità ultima della direzione esecutiva (Req. 12.1.4)
5. **Sanzioni in caso di violazione**: Fino a 100.000 $ al mese (i circuiti di pagamento); potenziale perdita della capacità di accettare carte; costi di violazione: 200 $ + per record compromesso

---

# Lista di controllo per l'auto-valutazione della conformità PCI DSS

## Costruire e mantenere reti sicure (Req. 1-2)

| Requisito | Stato | Note |
|-----------|-------|------|
| Regole del firewall documentate e giustificate | ⬜ Sì ⬜ No ⬜ Parziale | |
| Regole del firewall riviste ogni 6 mesi | ⬜ Sì ⬜ No | |
| Segmentazione di rete tra CDE e altre reti | ⬜ Sì ⬜ No ⬜ N/A | |
| Password predefinite dei fornitori cambiate | ⬜ Sì ⬜ No | |
| Servizi non necessari disabilitati | ⬜ Sì ⬜ No ⬜ Parziale | |
| Reti wireless sicure (WPA2/WPA3) | ⬜ Sì ⬜ No ⬜ N/A | |

## Proteggere i dati dei titolari di carta (Req. 3-4)

| Requisito | Stato | Note |
|-----------|-------|------|
| Archiviazione CHD ridotta al minimo | ⬜ Sì ⬜ No | |
| SAD (CVV, banda magnetica, PIN) NON archiviati dopo autorizzazione | ⬜ Sì ⬜ No | |
| PAN mascherato quando visualizzato (prime 6, ultime 4 max) | ⬜ Sì ⬜ No | |
| PAN cifrato o tokenizzato quando archiviato | ⬜ Sì ⬜ No | |
| Chiavi crittografiche protette e gestite | ⬜ Sì ⬜ No ⬜ Parziale | |
| TLS 1.2+ usato per la trasmissione CHD su reti aperte | ⬜ Sì ⬜ No | |
| PAN non inviato tramite messaggistica (email, chat, SMS) | ⬜ Sì ⬜ No | |

## Mantenere un programma di gestione delle vulnerabilità (Req. 5-6)

| Requisito | Stato | Note |
|-----------|-------|------|
| Anti-malware distribuito su tutti i sistemi | ⬜ Sì ⬜ No ⬜ Parziale | |
| Anti-malware aggiornato, attivo e in registrazione | ⬜ Sì ⬜ No | |
| Meccanismi anti-phishing distribuiti | ⬜ Sì ⬜ No ⬜ Parziale | |
| Patch di sicurezza critiche applicate entro 30 giorni | ⬜ Sì ⬜ No | |
| Applicazioni web pubblicamente accessibili protette (WAF) | ⬜ Sì ⬜ No ⬜ N/A | |
| Pratiche di codifica sicura per il software personalizzato | ⬜ Sì ⬜ No ⬜ N/A | |

## Implementare solidi controlli degli accessi (Req. 7-9)

| Requisito | Stato | Note |
|-----------|-------|------|
| Accesso concesso in base al bisogno di sapere | ⬜ Sì ⬜ No ⬜ Parziale | |
| Diritti di accesso rivisti almeno ogni 6 mesi | ⬜ Sì ⬜ No | |
| ID univoci assegnati a ogni persona | ⬜ Sì ⬜ No | |
| Account condivisi vietati (salvo approvazione) | ⬜ Sì ⬜ No | |
| AMF per tutti gli accessi al CDE | ⬜ Sì ⬜ No | |
| AMF per l'accesso remoto alla rete | ⬜ Sì ⬜ No | |
| Password minimo 12 caratteri | ⬜ Sì ⬜ No | |
| Blocco account dopo 10 tentativi falliti | ⬜ Sì ⬜ No | |
| Controlli di accesso fisico per i sistemi CDE | ⬜ Sì ⬜ No ⬜ Parziale | |
| Media con CHD distrutti in modo sicuro | ⬜ Sì ⬜ No | |

## Monitorare e testare le reti (Req. 10-11)

| Requisito | Stato | Note |
|-----------|-------|------|
| Log di audit abilitati per tutti i componenti | ⬜ Sì ⬜ No ⬜ Parziale | |
| Log di audit rivisti almeno una volta al giorno | ⬜ Sì ⬜ No | |
| Log di audit conservati per almeno 12 mesi | ⬜ Sì ⬜ No | |
| Sincronizzazione temporale implementata (NTP) | ⬜ Sì ⬜ No | |
| Scansioni delle vulnerabilità interne ogni 3 mesi | ⬜ Sì ⬜ No | |
| Scansioni vulnerabilità esterne (ASV) ogni 3 mesi — 4 scansioni con esito positivo | ⬜ Sì ⬜ No | |
| Test di penetrazione interni almeno annualmente | ⬜ Sì ⬜ No | |
| Test di penetrazione esterni almeno annualmente | ⬜ Sì ⬜ No | |
| Meccanismi di rilevamento delle modifiche (FIM) distribuiti | ⬜ Sì ⬜ No | |

## Politica di sicurezza delle informazioni (Req. 12)

| Requisito | Stato | Note |
|-----------|-------|------|
| Politica di sicurezza stabilita e pubblicata | ⬜ Sì ⬜ No | |
| Politica rivista almeno annualmente | ⬜ Sì ⬜ No | |
| Analisi del rischio mirata eseguita almeno annualmente | ⬜ Sì ⬜ No | |
| Perimetro PCI DSS documentato e convalidato annualmente | ⬜ Sì ⬜ No | |
| Formazione di sensibilizzazione completata da tutto il personale (annuale) | ⬜ Sì ⬜ No | |
| Formazione su phishing e ingegneria sociale fornita | ⬜ Sì ⬜ No | |
| Verifiche dei precedenti del personale prima dell'assunzione | ⬜ Sì ⬜ No ⬜ Parziale | |
| Fornitori di servizi terzi validati per la conformità PCI | ⬜ Sì ⬜ No ⬜ N/A | |
| Piano di risposta agli incidenti creato e testato annualmente | ⬜ Sì ⬜ No | |

---

**FINE DEL DOCUMENTO DI RIFERIMENTO TECNICO**

*Questo riferimento tecnico supporta i potenziali requisiti di conformità PCI DSS come determinato in ISMS-POL-00.*

*Per le organizzazioni che NON elaborano carte di pagamento, questo documento è solo a scopo informativo e NON crea obblighi di conformità.*

<!-- QA_VERIFIED: 2026-04-03 -->
