<!-- ISMS-CORE:REF:ISMS-REF-NIS2-IT-network-information-security-directive-2:framework:REF:nis2 -->
**ISMS-REF-NIS2 — Riferimento ai requisiti della Direttiva NIS2**
**Requisiti di sicurezza informatica dell'UE per le entità essenziali e importanti (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento ai requisiti NIS2 |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-REF-NIS2 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | RSSI (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale (o in seguito ad aggiornamenti delle leggi di recepimento nazionali)
**Distribuzione**: Team di conformità, RSSI, consulente legale (per le organizzazioni soggette a NIS2)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del SGSI.
- Questo documento NON definisce requisiti obbligatori a meno che [Organizzazione] non sia un'entità regolata da NIS2.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

**Determinazione dell'applicabilità**: I requisiti NIS2 si applicano SOLO SE [Organizzazione] è un'entità essenziale o importante operante nell'UE nei settori coperti, rientra nelle soglie dimensionali (PMI medie/grandi) e opera in uno Stato membro dell'UE che ha recepito NIS2 nel diritto nazionale.

---

# Panoramica e applicabilità NIS2

## Cos'è NIS2?

La **Direttiva (UE) 2022/2555** sulle misure per un livello comune elevato di sicurezza informatica nell'Unione, che sostituisce la Direttiva NIS originale (2016/1148).

**Date chiave**:
- **Entrata in vigore**: 16 gennaio 2023
- **Scadenza di recepimento**: 17 ottobre 2024 (gli Stati membri dell'UE devono recepire nel diritto nazionale)

**Scopo**: Rafforzare la resilienza in materia di sicurezza informatica nei settori critici dell'UE; armonizzare i requisiti tra gli Stati membri; ampliare il perimetro rispetto alla Direttiva NIS originale; istituire un quadro di segnalazione degli incidenti; introdurre misure di vigilanza e di esecuzione.

**Autorità di vigilanza**: Autorità nazionali competenti; team di risposta agli incidenti di sicurezza informatica (CSIRT); punti di contatto unici (SPOC).

## Perimetro e settori coperti

**Entità essenziali** (Allegato I — impatto maggiore, requisiti più severi):

| Settore | Sottosettori |
|---------|--------------|
| Energia | Elettricità, teleriscaldamento/teleraffreddamento, petrolio, gas, idrogeno |
| Trasporti | Trasporto aereo, ferroviario, idrico, stradale |
| Settore bancario | Enti creditizi |
| Infrastrutture dei mercati finanziari | Sedi di negoziazione, controparti centrali, depositari centrali di titoli |
| Sanità | Prestatori di assistenza sanitaria, laboratori di riferimento UE, produttori di medicinali critici |
| Acqua potabile | Fornitori e distributori |
| Acque reflue | Gestione e raccolta |
| Infrastruttura digitale | IXP, fornitori DNS, registri TLD, fornitori cloud, data center, CDN, prestatori di servizi fiduciari, reti pubbliche di comunicazione |
| Gestione dei servizi TIC | Fornitori di servizi gestiti (MSP), fornitori di servizi gestiti di sicurezza (MSSP) |
| Pubblica amministrazione | Entità governative centrali |
| Spazio | Operatori di infrastrutture terrestri a supporto di servizi spaziali |

**Entità importanti** (Allegato II — impatto medio, requisiti proporzionati):

| Settore | Sottosettori |
|---------|--------------|
| Servizi postali e di corriere | |
| Gestione dei rifiuti | |
| Fabbricazione, produzione e distribuzione di sostanze chimiche | |
| Produzione, trasformazione e distribuzione di alimenti | |
| Fabbricazione | Dispositivi medici, prodotti informatici/elettronici/ottici, apparecchiature elettriche, macchinari, veicoli a motore, altri mezzi di trasporto |
| Fornitori digitali | Mercati online, motori di ricerca online, piattaforme di social network |
| Ricerca | Organizzazioni di ricerca |

## Soglie dimensionali

| Dimensione impresa | Dipendenti | Fatturato annuo O Bilancio | Applicabilità NIS2 |
|-------------------|------------|---------------------------|-------------------|
| **Grande** | ≥ 250 | > 50 M€ fatturato O > 43 M€ bilancio | Nel perimetro (se in settore coperto) |
| **Media** | 50-249 | ≤ 50 M€ fatturato E ≤ 43 M€ bilancio | Nel perimetro (se in settore coperto) |
| **Piccola** | 10-49 | ≤ 10 M€ | Generalmente fuori perimetro |
| **Micro** | < 10 | ≤ 2 M€ | Fuori perimetro |

**Eccezioni**: Fornitori unici (anche se piccoli, potrebbero rientrare nel perimetro); pubblica amministrazione (le soglie dimensionali non si applicano).

## Determinazione dell'applicabilità

| Criterio | Stato | Prova |
|----------|-------|-------|
| Opera in uno Stato membro dell'UE | ⬜ Sì ⬜ No | [Paese] |
| Rientra in un settore coperto (Allegato I o II) | ⬜ Sì ⬜ No | [Settore] |
| Soddisfa le soglie dimensionali (media o grande) | ⬜ Sì ⬜ No | [Dipendenti / Fatturato] |
| Designata dall'autorità nazionale | ⬜ Sì ⬜ No ⬜ Sconosciuto | |
| Lo Stato membro ha recepito NIS2 nel diritto nazionale | ⬜ Sì ⬜ No ⬜ In attesa | [Riferimento legge nazionale] |

---

# Articolo 21 — Misure di gestione dei rischi di sicurezza informatica

## Panoramica

L'Articolo 21 stabilisce le **misure minime di gestione dei rischi di sicurezza informatica** che le entità essenziali e importanti devono attuare.

**Principio di proporzionalità**: Le misure devono essere adeguate a natura e portata delle attività, dimensione dell'entità, probabilità e gravità degli incidenti, stato dell'arte della sicurezza informatica.

## Dieci misure minime (Articolo 21(2))

**1. Analisi del rischio e politiche di sicurezza dei sistemi informativi**

Politiche di analisi del rischio e sicurezza dei sistemi informativi; metodologia di valutazione del rischio; revisioni periodiche; documentazione delle decisioni di trattamento del rischio.

**Mappatura ISO 27001:2022**: Clausole 6.1.2, 6.1.3; A.5.1

---

**2. Gestione degli incidenti**

Politiche e procedure per la gestione degli incidenti; rilevamento, classificazione, risposta e ripristino; piani di comunicazione; insegnamenti appresi e miglioramento continuo.

**Specifico NIS2**: Segnalazione degli incidenti alle autorità nazionali (Articolo 23); coordinamento con il CSIRT nazionale.

**Mappatura ISO 27001:2022**: A.5.24; A.5.25; A.5.26; A.5.27

---

**3. Continuità operativa e gestione delle crisi**

Piani di continuità operativa (BCP); piani di ripristino di emergenza (DRP); procedure di gestione delle crisi; capacità di backup e ripristino; test e validazione.

**Enfasi NIS2**: Focus sulla continuità dei servizi essenziali; test regolari (almeno annuali).

**Mappatura ISO 27001:2022**: A.5.29; A.5.30; A.8.13; A.8.14

---

**4. Sicurezza della catena di approvvigionamento**

Misure per proteggere la catena di approvvigionamento; valutazione delle pratiche di sicurezza informatica dei fornitori; requisiti contrattuali; monitoraggio della postura di sicurezza dei fornitori.

**Specifico NIS2**: Focus esplicito sugli aspetti di sicurezza informatica; include sia i fornitori diretti che le dipendenze della catena di approvvigionamento; divulgazione delle vulnerabilità e coordinamento con i fornitori.

**Mappatura ISO 27001:2022**: A.5.19; A.5.20; A.5.21; A.5.22

---

**5. Sicurezza nell'acquisizione, sviluppo e manutenzione di reti e sistemi informativi**

Ciclo di vita dello sviluppo sicuro; requisiti di sicurezza negli acquisti; test di sicurezza prima del dispiegamento; procedure di manutenzione e applicazione delle patch; controlli della gestione dei cambiamenti.

**Mappatura ISO 27001:2022**: A.8.4; A.8.8; A.8.9; A.8.25-8.30

---

**6. Politiche e procedure per valutare l'efficacia delle misure di gestione dei rischi**

Valutazione regolare dell'efficacia dei controlli; audit interni; metriche e ICP di sicurezza; monitoraggio continuo e miglioramento.

**Metodi di valutazione**: Valutazioni interne della sicurezza; valutazioni delle vulnerabilità; test di penetrazione; audit di terzi; revisioni di conformità.

**Mappatura ISO 27001:2022**: Clausole 9.1; 9.2; 9.3; 10.1; 10.2

---

**7. Pratiche di igiene informatica di base e formazione sulla sicurezza informatica**

Programmi di sensibilizzazione e formazione degli utenti; misure di igiene informatica di base; formazione per ruolo; campagne di sensibilizzazione regolari; simulazioni di phishing.

**Misure di igiene informatica**: Politiche di password forti; AMF; consapevolezza del phishing; istruzioni per il lavoro da remoto sicuro; sicurezza dei dispositivi mobili e BYOD.

**Mappatura ISO 27001:2022**: A.6.3

---

**8. Crittografia e cifratura**

Uso della crittografia per proteggere i dati; cifratura dei dati sensibili a riposo e in transito; gestione delle chiavi crittografiche; allineamento con gli standard attuali.

**Standard di implementazione**: TLS 1.2 minimo (TLS 1.3 preferito); AES-256 per i dati a riposo; nessun algoritmo obsoleto (DES, 3DES, MD5, SHA-1).

**Mappatura ISO 27001:2022**: A.8.24

---

**9. Sicurezza delle risorse umane, politiche di controllo degli accessi e gestione degli asset**

**Sicurezza delle risorse umane**: Verifiche dei precedenti per le posizioni sensibili; responsabilità di sicurezza nei contratti di lavoro; procedure di cessazione del rapporto (revoca degli accessi).

**Controllo degli accessi**: Identificazione e autenticazione degli utenti; principio del minimo privilegio; revisioni periodiche degli accessi; gestione degli accessi privilegiati (PAM).

**Gestione degli asset**: Inventario delle risorse informative; classificazione e gestione degli asset; politiche di utilizzo accettabile; procedure di dismissione degli asset.

**Mappatura ISO 27001:2022**: A.5.9-5.18; A.6.1-6.5; A.8.2; A.8.3; A.8.10

---

**10. Autenticazione a più fattori, comunicazioni sicure e sistemi di comunicazione di emergenza**

**AMF (Autenticazione Multi-Fattore)**:
- AMF per l'accesso remoto
- AMF per gli account privilegiati
- AMF per l'accesso a sistemi/dati sensibili
- Autenticazione adattiva basata sul rischio ove appropriato

**Comunicazioni sicure**: Cifratura per voce, video e testo; piattaforme collaborative sicure; cifratura end-to-end per le comunicazioni sensibili; VPN per l'accesso remoto.

**Sistemi di comunicazione di emergenza**: Canali di comunicazione fuori banda per gli incidenti; liste dei contatti di emergenza; metodi di comunicazione alternativi.

**Specifico NIS2**: Questo è uno dei requisiti più prescrittivi di NIS2, che impone esplicitamente AMF e comunicazioni sicure — più specifico delle tipiche implementazioni ISO 27001.

**Mappatura ISO 27001:2022**: A.5.14; A.8.5; A.8.20; A.8.23

## Responsabilità dell'organo di gestione (Articolo 21(3))

Gli Stati membri garantiscono che l'organo di gestione approvi le misure di gestione dei rischi di sicurezza informatica, ne supervisioni l'attuazione e possa essere ritenuto **responsabile** per le infrazioni.

**Specifico NIS2**: La responsabilità esplicita della direzione è unica rispetto a NIS2 e non presente nella norma ISO 27001.

---

# Articolo 23 — Segnalazione degli incidenti

## Scadenze per la segnalazione

| Fase | Tempistica | Contenuto |
|------|-----------|-----------|
| **Allerta precoce** | Senza indugio (≤ 24 ore dalla conoscenza) | Conoscenza dell'incidente significativo; possibile impatto transfrontaliero |
| **Notifica dell'incidente** | Senza indugio (≤ 72 ore dalla conoscenza) | Valutazione iniziale; gravità e impatto; indicatori di compromissione |
| **Rapporto finale** | ≤ 1 mese dalla notifica dell'incidente | Descrizione dettagliata; causa principale; misure di mitigazione applicate |
| **Rapporti intermedi** | Su richiesta del CSIRT/autorità o in caso di cambiamento significativo | Stato aggiornato |

## Criteri per un incidente significativo

Un incidente è considerato **significativo** se:
- Ha causato o potrebbe causare una grave perturbazione operativa
- Ha causato o potrebbe causare considerevoli perdite finanziarie
- Ha interessato o potrebbe interessare altre persone fisiche o giuridiche (clienti, partner)

**Coordinamento**: Le segnalazioni NIS2 possono sovrapporsi alle notifiche di violazione dei dati personali del RGPD e alle segnalazioni DORA per le entità finanziarie.

---

# Sicurezza della catena di approvvigionamento

## Valutazione dei fornitori

**Prima del contratto**: Valutazione della postura di sicurezza informatica del fornitore; certificazioni di sicurezza (ISO 27001, SOC 2, ecc.); storia degli incidenti; valutazione del rischio dei subappaltatori.

**Monitoraggio continuo**: Revisioni periodiche della sicurezza (minimo annuale); obblighi di notifica degli incidenti; diritti di audit sulla sicurezza; performance rispetto agli SLA di sicurezza.

## Requisiti contrattuali

I contratti con i fornitori devono includere: obblighi e standard di sicurezza; requisiti di notifica degli incidenti; diritti di audit e valutazione; protezione dei dati e riservatezza; restrizioni sui subappalti; diritti di risoluzione per violazioni della sicurezza.

---

# Quadro di vigilanza e sanzioni

## Autorità nazionali competenti

Ogni Stato membro designa: un'**autorità competente** responsabile della vigilanza NIS2; un **CSIRT** (Computer Security Incident Response Team); un **punto di contatto unico (SPOC)**.

**Poteri di vigilanza** (Articolo 32): ispezioni in loco e da remoto; audit della sicurezza da parte di revisori qualificati; richieste di informazioni; accesso a dati, documenti e strutture.

## Sanzioni (Articolo 34)

**Entità essenziali** (Allegato I):
- Fino a **10.000.000 €** OPPURE **2% del fatturato mondiale annuo totale** (il maggiore dei due)

**Entità importanti** (Allegato II):
- Fino a **7.000.000 €** OPPURE **1,4% del fatturato mondiale annuo totale** (il maggiore dei due)

**Responsabilità della direzione** (Articolo 21(5)): Gli Stati membri possono ritenere i membri dell'organo di gestione personalmente responsabili; possibile interdizione temporanea da ruoli di gestione.

---

# Mappatura ISO 27001:2022 — NIS2

## Matrice di mappatura dei controlli

| Requisito NIS2 | Articolo NIS2 | Controllo ISO 27001:2022 | Lacuna |
|----------------|---------------|--------------------------|--------|
| Analisi del rischio e politiche di sicurezza | Art. 21(2)(a) | Clausole 6.1.2-6.1.3; A.5.1 | Allineato |
| Gestione degli incidenti | Art. 21(2)(b) | A.5.24-5.27 | NIS2: aggiunge la segnalazione esterna |
| Continuità operativa e crisi | Art. 21(2)(c) | A.5.29-5.30; A.8.13-8.14 | Allineato |
| Sicurezza della catena di approvvigionamento | Art. 21(2)(d) | A.5.19-5.22 | NIS2: focus più esplicito |
| Acquisizione, sviluppo, manutenzione | Art. 21(2)(e) | A.8.4; A.8.8-8.9; A.8.25-8.30 | Allineato |
| Valutazione dell'efficacia | Art. 21(2)(f) | Clausole 9.1-9.3; 10.1-10.2 | Allineato |
| Igiene informatica e formazione | Art. 21(2)(g) | A.6.3 | Allineato |
| Crittografia e cifratura | Art. 21(2)(h) | A.8.24 | Allineato |
| Sicurezza HR, controllo accessi, gestione asset | Art. 21(2)(i) | A.5.9-5.18; A.6.1-6.5; A.8.2-8.3 | Allineato |
| AMF e comunicazioni sicure | Art. 21(2)(j) | A.5.14; A.8.5; A.8.20 | **Specifico NIS2**: requisito AMF prescrittivo |
| Segnalazione incidenti alle autorità | Art. 23 | A.5.5; A.5.26 | **Specifico NIS2**: scadenze obbligatorie |
| Responsabilità organo di gestione | Art. 21(3) | Clausole 5.1-5.2 | **Specifico NIS2**: responsabilità personale |

## Lacune principali tra ISO 27001:2022 e NIS2

1. **Segnalazione normativa degli incidenti con scadenze**: ISO 27001 — gestione interna; NIS2 — segnalazione obbligatoria al CSIRT/autorità entro 24/72 ore
2. **Requisito AMF prescrittivo**: ISO 27001 — autenticazione sicura (metodo flessibile); NIS2 — requisito esplicito di autenticazione a più fattori
3. **Responsabilità della direzione**: ISO 27001 — nessuna disposizione sulla responsabilità legale; NIS2 — l'organo di gestione può essere ritenuto responsabile
4. **Esecuzione e sanzioni**: ISO 27001 — sospensione/ritiro della certificazione; NIS2 — sanzioni finanziarie significative (fino a 10 M€ o 2% del fatturato)

**Insight chiave**: La certificazione ISO 27001:2022 fornisce una solida base per la conformità NIS2. Le lacune principali riguardano il processo di segnalazione degli incidenti e le scadenze, la validazione dell'implementazione AMF, il quadro di supervisione e responsabilità dell'organo di gestione e la registrazione e vigilanza nazionali. Le organizzazioni con ISO 27001 richiedono tipicamente un **10-20% di sforzo aggiuntivo** per raggiungere la conformità NIS2.

---

# Lista di controllo per l'auto-valutazione della conformità NIS2

## Determinazione dell'applicabilità

| Criterio | Stato | Note |
|----------|-------|------|
| Entità essenziale (Allegato I) | ⬜ Sì ⬜ No | [Specificare settore] |
| Entità importante (Allegato II) | ⬜ Sì ⬜ No | [Specificare settore] |
| Soddisfa le soglie dimensionali | ⬜ Sì ⬜ No | [Dipendenti: ___ / Fatturato: ___] |
| Legge di recepimento nazionale in vigore | ⬜ Sì ⬜ No ⬜ In attesa | [Riferimento legge nazionale] |

**Applicabilità NIS2 complessiva**: ⬜ Entità essenziale ⬜ Entità importante ⬜ Non applicabile

## Misure di sicurezza informatica — Articolo 21(2)

| Misura | Stato | Posizione delle prove |
|--------|-------|----------------------|
| (a) Analisi del rischio e politiche di sicurezza | ⬜ Sì ⬜ No ⬜ Parziale | |
| (b) Gestione degli incidenti | ⬜ Sì ⬜ No ⬜ Parziale | |
| (c) Continuità operativa e gestione delle crisi | ⬜ Sì ⬜ No ⬜ Parziale | |
| (d) Sicurezza della catena di approvvigionamento | ⬜ Sì ⬜ No ⬜ Parziale | |
| (e) Sicurezza nell'acquisizione, sviluppo, manutenzione | ⬜ Sì ⬜ No ⬜ Parziale | |
| (f) Procedure per valutare l'efficacia | ⬜ Sì ⬜ No ⬜ Parziale | |
| (g) Igiene informatica di base e formazione | ⬜ Sì ⬜ No ⬜ Parziale | |
| (h) Crittografia e cifratura | ⬜ Sì ⬜ No ⬜ Parziale | |
| (i) Sicurezza HR, controllo accessi, gestione asset | ⬜ Sì ⬜ No ⬜ Parziale | |
| (j) AMF, comunicazioni sicure e di emergenza | ⬜ Sì ⬜ No ⬜ Parziale | |

## Responsabilità dell'organo di gestione — Articolo 21(3)

| Requisito | Stato |
|-----------|-------|
| L'organo di gestione ha approvato le misure di gestione dei rischi | ⬜ Sì ⬜ No |
| L'organo di gestione supervisiona l'attuazione | ⬜ Sì ⬜ No ⬜ Parziale |
| Formazione sulla sicurezza informatica per l'organo di gestione | ⬜ Sì ⬜ No ⬜ Pianificato |
| Reporting periodico sulla sicurezza informatica all'organo di gestione | ⬜ Sì ⬜ No |

## Segnalazione degli incidenti — Articolo 23

| Requisito | Stato |
|-----------|-------|
| Criteri di classificazione degli incidenti definiti | ⬜ Sì ⬜ No ⬜ Parziale |
| Processo di segnalazione al CSIRT/autorità | ⬜ Sì ⬜ No |
| Capacità di allerta precoce (24 ore) | ⬜ Sì ⬜ No |
| Capacità di notifica dell'incidente (72 ore) | ⬜ Sì ⬜ No |
| Capacità di rapporto finale (1 mese) | ⬜ Sì ⬜ No |
| Test del processo di segnalazione degli incidenti condotto | ⬜ Sì ⬜ No ⬜ Pianificato |
| Contatto CSIRT/autorità stabilito | ⬜ Sì ⬜ No |

---

**FINE DEL DOCUMENTO DI RIFERIMENTO TECNICO**

*Questo riferimento tecnico supporta i potenziali requisiti di conformità NIS2 come determinato in ISMS-POL-00.*

*Per le organizzazioni NON soggette a NIS2, questo documento è solo a scopo informativo e NON crea obblighi di conformità.*

<!-- QA_VERIFIED: 2026-04-03 -->
