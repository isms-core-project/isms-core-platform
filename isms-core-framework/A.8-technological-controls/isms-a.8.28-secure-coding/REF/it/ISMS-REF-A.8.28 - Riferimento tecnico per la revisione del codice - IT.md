<!-- ISMS-CORE:REF:ISMS-REF-A.8.28-IT-code-review-technical-reference:framework:REF:a.8.28 -->
**ISMS-REF-A.8.28 — Riferimento tecnico per la revisione del codice**

**Controllo del documento — ISMS-REF-A.8.28**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento tecnico per la revisione del codice |
| **Tipo di documento** | Riferimento tecnico (REF) |
| **Identificativo del documento** | ISMS-REF-A.8.28 |
| **Autore del documento** | Responsabile della sicurezza applicativa |
| **Proprietario del documento** | Responsabile della sicurezza applicativa |
| **Approvato da** | Responsabile della sicurezza applicativa |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Data] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

---

## Avvertenza

**CRITICO**: Si tratta di un documento di riferimento informativo e **NON** fa parte del quadro formale delle politiche SGSI.

Le informazioni contenute forniscono indicazioni tecniche e dettagli metodologici ma **NON stabiliscono requisiti obbligatori**.

**I requisiti di politica vincolanti** sono definiti in **ISMS-POL-A.8.28 (Politica di codifica sicura)**.

**Scopo**: Supportare l'implementazione della revisione del codice fornendo:

- Liste di controllo dettagliate per la revisione del codice di sicurezza
- Confronto tra metodi e indicazioni
- Approcci di revisione basati sul rischio
- Migliori pratiche di implementazione

**Utilizzo**: Riferimento tecnico per i revisori del codice, i Security Champion e i team di sviluppo. Il contenuto potrebbe richiedere aggiornamenti con l'evoluzione dei pattern di vulnerabilità.

---

# Scopo e ambito

## Obiettivo del riferimento

Questo documento fornisce **criteri di sicurezza attuabili** per i revisori del codice. Operazionalizza i requisiti di revisione del codice di ISMS-POL-A.8.28 Sezione 2.3, traducendo la politica in passaggi di revisione pratici.

*«Il primo principio è non ingannare se stessi — e siete la persona più facile da ingannare.» — Richard Feynman*

**Obiettivo**: Consentire ai revisori del codice di identificare i problemi di sicurezza in modo sistematico senza richiedere una profonda competenza in sicurezza per ogni revisione.

## Argomenti trattati

- Lista di controllo di preparazione pre-revisione
- Criteri principali di revisione della sicurezza (autenticazione, validazione degli input, autorizzazione, crittografia, registrazione, gestione degli errori)
- Approccio di revisione basato sul rischio
- Pattern comuni e anti-pattern
- Procedure di escalation

## Relazione con la politica

**ISMS-POL-A.8.28 richiede** (vincolante):

- Revisione del codice tra pari per tutto il codice di produzione
- Criteri di revisione incentrati sulla sicurezza
- Partecipazione dei Security Champion alle revisioni
- Revisione del team di sicurezza applicativa per le modifiche ad alto rischio

**Questo documento REF spiega** (informativo):

- COME eseguire revisioni del codice incentrate sulla sicurezza
- QUALI problemi di sicurezza cercare
- QUANDO escalare ai Security Champion o al team di sicurezza applicativa
- Applicazione della lista di controllo basata sul rischio

---

# Come utilizzare questa lista di controllo

## Non ogni elemento per ogni revisione

**Approccio basato sul rischio**:

**Modifiche ad alto rischio** (utilizzare la lista di controllo completa):

- Autenticazione o modifiche all'autorizzazione
- Implementazione crittografica
- Elaborazione di pagamenti o transazioni finanziarie
- Elaborazione di DCP o esposizione di dati
- Modifiche ai controlli di sicurezza
- Integrazioni di terze parti con dati sensibili

**Modifiche a rischio medio** (concentrarsi sulle sezioni pertinenti):

- Endpoint API → Validazione degli input + Autorizzazione
- Query del database → Prevenzione dell'iniezione SQL
- Operazioni sui file → Prevenzione della traversata del percorso
- Modifiche all'interfaccia web → Prevenzione XSS + CSRF

**Modifiche a basso rischio** (revisione di sicurezza minima):

- Refactoring senza modifiche di funzionalità
- Aggiornamenti della documentazione
- Modifiche alla configurazione (non-sicurezza)
- Modifiche solo ai test

## Punti di integrazione

**Template di Pull Request**:
```markdown
# Lista di controllo per la sicurezza (se applicabile)

- [ ] Validazione degli input presente e corretta
- [ ] Codifica dell'output appropriata al contesto
- [ ] Query SQL parametrizzate
- [ ] Nessun segreto codificato
- [ ] Controlli di autorizzazione presenti
```

**Strumenti di revisione**:

- Collegare gli elementi della lista di controllo nei commenti di revisione (es. «Non supera 3.2.3: rischio di iniezione SQL»)
- Utilizzare le etichette degli strumenti di revisione (security-review-required, security-approved)

## Quando effettuare l'escalation

**Escalation al Security Champion**:

- Elemento della lista di controllo poco chiaro o ambiguo
- Preoccupazione per la sicurezza che va oltre la propria competenza
- Più elementi della lista di controllo non superati
- Pattern di sicurezza complesso che richiede validazione

**Escalation al team di sicurezza applicativa**:

- Vulnerabilità sospetta che richiede validazione esperta
- Preoccupazione di sicurezza a livello architetturale
- Necessità di una sessione di modellazione delle minacce
- Risultato Critico/Alto dagli strumenti automatizzati

**Canali di escalation**:

- Slack: #security-champions o #appsec
- Email: security@[organizzazione].com
- Tag nella PR: @security-champions o @appsec-team

---

# Lista di controllo pre-revisione

**Da completare PRIMA di rivedere il codice** (risparmio di tempo, garanzia di qualità):

- [ ] **Verifiche automatizzate superate**: SAST, SCA, test unitari, linter tutti verdi?
  - *Se no*: Rivedere prima i risultati automatizzati, assicurarsi che siano affrontati o soppressi con giustificazione

- [ ] **Descrizione della modifica chiara**: La descrizione della PR spiega COSA è cambiato e PERCHÉ?
  - *Verificare*: Descrizioni vaghe («bug risolto», «aggiornamenti»), contesto mancante
  - *Azione*: Richiedere chiarimenti se poco chiaro

- [ ] **Livello di rischio identificato**: La PR indica il livello di rischio (Critico/Alto/Medio/Basso)?
  - *Se non identificato*: Valutare il rischio secondo i criteri della Sezione 2.1

- [ ] **Modifiche rilevanti per la sicurezza segnalate**: L'autore della PR identifica le implicazioni di sicurezza?
  - *Verificare*: Autenticazione, autorizzazione, gestione degli input, crittografia, accesso ai dati
  - *Azione*: Se rilevante per la sicurezza ma non segnalato, applicare le sezioni appropriate della lista di controllo

- [ ] **Ambito della modifica ragionevole**: La PR è focalizzata (non modifica 50 file non correlati)?
  - *Se troppo grande*: Richiedere la suddivisione in PR più piccole e rivedibili

- [ ] **Test inclusi**: Le modifiche rilevanti per la sicurezza sono coperte da test?
  - *Verificare*: Test di validazione degli input, test di autorizzazione, casi di test negativi
  - *Riferimento alla politica*: ISMS-POL-A.8.28 Sezione 2.3.1

---

# Lista di controllo principale per la revisione della sicurezza

## Autenticazione e gestione delle sessioni

- [ ] **Controlli di autenticazione presenti**: Tutti gli endpoint protetti verificano l'autenticazione dell'utente
  - *Verificare*: Autenticazione mancante sugli endpoint API, pagine admin, accesso ai dati
  - *Test*: L'endpoint può essere acceduto senza autenticazione?
  - *Riferimento alla politica*: ISMS-POL-A.8.28 Sezione 2.2

- [ ] **Token di sessione sicuri**: Token casuali, imprevedibili, con flag HttpOnly/Secure
  - *Verificare*: ID di sessione prevedibili, token sequenziali, token negli URL
  - *Validare*: Gli attributi dei cookie includono `HttpOnly`, `Secure`, `SameSite=Strict/Lax`

- [ ] **Gestione delle password sicura**: Password con hash mediante bcrypt/Argon2, mai registrate
  - *Verificare*: Password in chiaro, hash debole (MD5, SHA1, SHA256 senza salt)
  - *Validare*: Nessuna password nei registri, messaggi di errore o output di debug
  - *Esempio*: Vedere ISMS-CTX-A.8.28 Python Sezione 2.6

- [ ] **Autenticazione a più fattori (AMF) applicata**: AMF richiesta per gli account privilegiati
  - *Verificare*: Account admin, operazioni finanziarie che bypassano AMF

- [ ] **Timeout di sessione appropriato**: Le sessioni scadono dopo un periodo di inattività
  - *Verificare*: Nessun timeout, timeout eccessivamente lungo (>30 min per le app ad alto rischio)

- [ ] **Funzionalità di disconnessione sicura**: La disconnessione invalida la sessione lato server
  - *Verificare*: Disconnessione solo lato client, sessione ancora valida dopo la disconnessione
  - *Test*: Token di sessione rifiutato dopo la disconnessione

## Validazione degli input

- [ ] **Tutti gli input validati**: Validazione lato server presente per TUTTI gli input utente
  - *Verificare*: Validazione solo lato client, validazione mancante sugli endpoint API
  - *Fonti*: Form, parametri URL, intestazioni, cookie, caricamenti di file, richieste API
  - *Riferimento alla politica*: ISMS-POL-A.8.28 Sezione 2.2

- [ ] **Approccio a lista bianca utilizzato**: La validazione utilizza una lista di autorizzazione (non di blocco)
  - *Verificare*: Pattern a lista nera («rifiutare se contiene X»), liste di blocco incomplete
  - *Corretto*: «Accettare solo se corrisponde a Y» (es. solo alfanumerico)

- [ ] **Iniezione SQL prevenuta**: Query parametrizzate utilizzate, nessuna concatenazione di stringhe
  - *Verificare*: Concatenazione di stringhe in SQL (f-string, +, .format()), costruzione di query dinamiche
  - *Validare*: Tutte le query del database utilizzano istruzioni parametrizzate o ORM in modo sicuro
  - *Esempio*: Vedere ISMS-CTX-A.8.28 Python Sezione 2.2, SQL Sezione 7

- [ ] **Iniezione di comandi prevenuta**: Nessuna chiamata shell diretta con input utente
  - *Verificare*: `os.system()`, `subprocess` con `shell=True`, `eval()`, `exec()`
  - *Validare*: I comandi utilizzano liste di argomenti, non la concatenazione di stringhe
  - *Esempio*: Vedere ISMS-CTX-A.8.28 Python Sezione 2.3

- [ ] **Traversata del percorso prevenuta**: Percorsi dei file validati, nessuna traversata di directory
  - *Verificare*: Concatenazione diretta di input utente ai percorsi dei file
  - *Validare*: Percorsi risolti e validati all'interno della directory consentita
  - *Esempio*: Vedere ISMS-CTX-A.8.28 Python Sezione 2.4

- [ ] **Entità esterna XML (XXE) prevenuta**: Il parsing XML disabilita le entità esterne
  - *Verificare*: Configurazione predefinita del parser XML (spesso vulnerabile)
  - *Validare*: Entità esterne esplicitamente disabilitate nella configurazione del parser
  - *Esempio*: Vedere ISMS-CTX-A.8.28 Java Sezione 4.3

- [ ] **Validazione dei caricamenti di file**: Validazione di tipo, dimensione e contenuto presente
  - *Verificare*: Validazione solo per estensione, nessuna validazione del contenuto, nessun limite di dimensione
  - *Validare*: Validazione del magic number, scansione antimalware, limiti di dimensione applicati

- [ ] **Limiti di lunghezza dell'input**: Lunghezza massima applicata (prevenire buffer overflow, DoS)
  - *Verificare*: Lunghezza dell'input illimitata, limiti eccessivamente grandi

## Codifica dell'output e prevenzione XSS

- [ ] **Prevenzione XSS**: Output codificato per contesto (HTML, JavaScript, URL, CSS)
  - *Verificare*: Input utente non codificato in HTML, `innerHTML`, `dangerouslySetInnerHTML`
  - *Validare*: Escape automatico del framework utilizzato o codifica manuale applicata
  - *Esempio*: Vedere ISMS-CTX-A.8.28 JavaScript Sezione 3.2

- [ ] **Intestazioni Content Security Policy (CSP)**: CSP configurato per mitigare l'impatto XSS
  - *Verificare*: Intestazioni CSP mancanti, CSP eccessivamente permissivo (`unsafe-inline`, `unsafe-eval`)
  - *Validare*: CSP limita le fonti degli script, disabilita gli script inline ove possibile

- [ ] **Protezione CSRF**: Token presenti per le operazioni che modificano lo stato
  - *Verificare*: Token CSRF mancanti su POST/PUT/DELETE/PATCH
  - *Validare*: Token validati lato server, token imprevedibili
  - *Esempio*: Vedere ISMS-CTX-A.8.28 JavaScript Sezione 3.4

- [ ] **Intestazioni di sicurezza HTTP**: Intestazioni di sicurezza configurate correttamente
  - *Verificare*: `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security` mancanti
  - *Validare*: Intestazioni presenti e configurate correttamente

## Autorizzazione e controllo degli accessi

- [ ] **Autorizzazione applicata lato server**: Tutti i controlli di accesso lato server
  - *Verificare*: Autorizzazione solo lato client (elementi UI nascosti), controlli server mancanti
  - *Validare*: Ogni risorsa protetta dispone di un controllo di autorizzazione lato server

- [ ] **Prevenzione IDOR**: Proprietà dell'utente verificata prima dell'accesso alla risorsa
  - *Verificare*: Accesso diretto all'ID senza controllo di proprietà (es. `/api/orders/123` accessibile da qualsiasi utente)
  - *Test*: Un utente può accedere alle risorse di un altro utente cambiando l'ID?

- [ ] **Principio del minimo privilegio**: Le operazioni utilizzano i permessi minimi necessari
  - *Verificare*: Ruoli eccessivamente permissivi, operazioni admin per le attività utente
  - *Validare*: Le connessioni al database utilizzano privilegi limitati, non root/admin

- [ ] **Controllo degli accessi basato sui ruoli (RBAC)**: Ruoli correttamente assegnati e verificati
  - *Verificare*: ID utente codificati invece di ruoli, controlli di ruolo mancanti

- [ ] **Escalation dei privilegi prevenuta**: Nessun modo per elevare i privilegi in modo improprio
  - *Verificare*: Assegnazioni di ruoli controllabili dall'utente, autorizzazione mancante sui cambiamenti di privilegi
  - *Test*: Un utente può assegnarsi il ruolo di admin?

## Crittografia

- [ ] **Solo algoritmi approvati**: AES-256-GCM, RSA-2048+, ECDSA-256+, SHA-256+
  - *Verificare*: DES, 3DES, RC4, MD5, SHA1, RSA-1024, modalità ECB, crittografia personalizzata
  - *Riferimento alla politica*: ISMS-POL-A.8.28 Sezione 2.2, ISMS-POL-A.8.24 (Crittografia)

- [ ] **Nessun segreto codificato**: Credenziali da variabili d'ambiente o gestore di segreti
  - *Verificare*: Chiavi API, password, token, chiavi private nel codice
  - *Strumenti*: Utilizzare uno strumento di scansione dei segreti (Gitleaks, TruffleHog, GitHub Secret Scanning)
  - *Azione*: Se trovati, ruotare immediatamente le credenziali

- [ ] **Generazione casuale sicura**: GNC crittograficamente sicuro utilizzato
  - *Verificare*: `random.random()`, `Math.random()`, seed basati sul tempo per i token di sicurezza
  - *Validare*: Utilizzo di `secrets` (Python), `crypto.randomBytes()` (Node.js), `SecureRandom` (Java)

- [ ] **Gestione delle chiavi di crittografia**: Chiavi archiviate in modo sicuro, non nel codice o nella configurazione
  - *Verificare*: Chiavi di crittografia nelle variabili d'ambiente (meglio ma non ideale), chiavi nel codice
  - *Validare*: Chiavi in un servizio di gestione delle chiavi appropriato (AWS KMS, Azure Key Vault, HashiCorp Vault)

- [ ] **TLS/HTTPS applicato**: Tutte le comunicazioni sensibili tramite HTTPS
  - *Verificare*: HTTP per l'autenticazione, trasmissione di dati sensibili
  - *Validare*: Intestazioni HSTS presenti, nessun contenuto misto

## Gestione degli errori e registrazione

- [ ] **Messaggi di errore generici agli utenti**: Nessuna traccia dello stack, errori SQL, percorsi di file esposti
  - *Verificare*: Messaggi di errore dettagliati che rivelano informazioni di sistema
  - *Validare*: Gli errori lato utente sono generici («Si è verificato un errore»), i dettagli sono registrati lato server

- [ ] **Eventi di sicurezza registrati**: Autenticazione, errori di autorizzazione, errori di validazione degli input registrati
  - *Verificare*: Registrazione degli eventi di sicurezza mancante
  - *Validare*: Dettagli sufficienti per l'indagine sugli incidenti (utente, azione, risultato, timestamp)
  - *Riferimento alla politica*: ISMS-POL-A.8.28 Sezione 2.2

- [ ] **Nessun dato sensibile nei registri**: Password, token, DCP esclusi dai registri
  - *Verificare*: Registrazione completa delle richieste/risposte, registrazione delle password, numeri di carte di credito
  - *Validare*: Dati sensibili oscurati o esclusi

- [ ] **Eccezioni gestite in modo sicuro**: I blocchi catch non espongono informazioni sensibili
  - *Verificare*: Blocchi catch vuoti, eccezioni propagate all'interfaccia utente

## Protezione dei dati

- [ ] **Dati sensibili crittografati**: DCP, dati finanziari, credenziali crittografati a riposo e in transito
  - *Verificare*: Archiviazione in chiaro di dati sensibili
  - *Riferimento alla politica*: ISMS-POL-A.8.24 (Crittografia)

- [ ] **Minimizzazione dei dati**: Solo i dati necessari raccolti e conservati
  - *Verificare*: Raccolta eccessiva di dati, conservazione indefinita

- [ ] **Cancellazione sicura dei dati**: Dati sensibili eliminati in modo sicuro quando non più necessari
  - *Validare*: Non solo contrassegnati come eliminati ma effettivamente rimossi o cancellati crittograficamente
  - *Riferimento alla politica*: ISMS-POL-A.8.10 (Cancellazione delle informazioni)

## Dipendenze di terze parti

- [ ] **Dipendenze analizzate per le vulnerabilità**: Rapporti degli strumenti SCA esaminati
  - *Verificare*: Nuove dipendenze vulnerabili introdotte
  - *Validare*: Nessuna vulnerabilità Critica/Alta nelle dipendenze

- [ ] **Dipendenze da fonti attendibili**: Repository ufficiali utilizzati
  - *Verificare*: Dipendenze da fonti sconosciute o non attendibili
  - *Validare*: Integrità dei pacchetti (checksum, firme)

- [ ] **Versioni delle dipendenze bloccate**: File di blocco presenti e aggiornati
  - *Verificare*: Versioni non bloccate, file di blocco mancanti
  - *Validare*: `package-lock.json`, `requirements.txt`, `Gemfile.lock` confermati

---

# Linee guida per la revisione basata sul rischio

## Modifiche a rischio critico

**Trigger**:

- Modifiche al sistema di autenticazione
- Modifiche al modello di autorizzazione
- Implementazione crittografica
- Elaborazione dei pagamenti
- Modifiche alla gestione dei DCP

**Approccio di revisione**:

- Applicazione completa della lista di controllo (tutte le sezioni)
- Revisione obbligatoria del Security Champion o del team di sicurezza applicativa
- Sessione di modellazione delle minacce (se modifica architettonica)
- Test di penetrazione (se modifica significativa)
- Test estesi inclusi i casi di test negativi

**Approvazione**:

- Responsabile dello sviluppo + Security Champion + Responsabile della sicurezza applicativa

## Modifiche ad alto rischio

**Trigger**:

- Nuovi endpoint API con accesso ai dati
- Modifiche alle query del database
- Funzionalità di caricamento di file
- Integrazioni di terze parti con condivisione di dati
- Modifiche all'interfaccia admin

**Approccio di revisione**:

- Sezioni pertinenti della lista di controllo (focus su validazione degli input, autorizzazione, protezione dei dati)
- Revisione del Security Champion raccomandata
- Test di sicurezza (SAST, DAST)
- Casi di test funzionali e di sicurezza

**Approvazione**:

- Responsabile dello sviluppo + Security Champion

## Modifiche a rischio medio

**Trigger**:

- Modifiche UI con input utente
- Generazione di report con accesso ai dati
- Modifiche alla configurazione che influenzano la sicurezza
- Modifiche alla registrazione o al monitoraggio

**Approccio di revisione**:

- Elementi mirati della lista di controllo (validazione degli input, prevenzione XSS)
- Revisione tra pari con consapevolezza della sicurezza
- Scansione di sicurezza automatizzata

**Approvazione**:

- Revisore tra pari con formazione in sicurezza

## Modifiche a basso rischio

**Trigger**:

- Refactoring senza modifiche di funzionalità
- Aggiornamenti della documentazione
- Modifiche solo ai test
- Stilizzazione UI (CSS) senza modifiche alla logica

**Approccio di revisione**:

- Revisione del codice standard
- Verificare che non vi sia impatto di sicurezza non intenzionale
- Scansione rapida per problemi introdotti accidentalmente

**Approvazione**:

- Revisione tra pari standard

---

# Pattern comuni e anti-pattern

## Pattern sicuri (da incoraggiare)

**Pattern di validazione degli input**:
```python
# Validazione a lista bianca
CAMPI_CONSENTITI = {'nome', 'email', 'eta'}
def valida_input(dati):
    if not all(chiave in CAMPI_CONSENTITI for chiave in dati.keys()):
        raise ErroreValidazione("Campo non valido")
    # Validazione aggiuntiva...
```

**Pattern di autorizzazione**:
```python
# Verifica della proprietà prima dell'accesso alla risorsa
def get_ordine(id_ordine, utente_corrente):
    ordine = Ordine.query.get(id_ordine)
    if ordine.id_utente != utente_corrente.id:
        raise Vietato("Accesso negato")
    return ordine
```

**Pattern di configurazione sicura**:
```python
# Configurazione basata su variabili d'ambiente
CHIAVE_API = os.environ.get('CHIAVE_API')
if not CHIAVE_API:
    raise ErroreConfig("CHIAVE_API deve essere impostata")
```

## Anti-pattern (da scoraggiare)

**Concatenazione di stringhe per SQL**:
```python
# ANTI-PATTERN - Vulnerabilità da iniezione SQL
query = f"SELECT * FROM utenti WHERE id = {id_utente}"
```

**Autorizzazione lato client**:
```javascript
// ANTI-PATTERN - L'autorizzazione deve essere lato server
if (utente.ruolo === 'admin') {
  mostraPannelloAdmin();  // Solo lato client, facilmente aggirabile
}
```

**Hash delle password debole**:
```python
# ANTI-PATTERN - Hash debole
import hashlib
hash = hashlib.md5(password.encode()).hexdigest()
```

---

# Documentazione della revisione

## Template di commento di revisione

```
**Problema di sicurezza: [Tipo di problema]**

**Gravità**: [Critico/Alto/Medio/Basso]

**Problema**: [Breve descrizione del problema di sicurezza]

**Posizione**: [File e numero di riga]

**Rischio**: [Cosa potrebbe fare un attaccante]

**Raccomandazione**: [Come risolvere]

**Riferimento**: ISMS-POL-A.8.28 Sezione [X.Y] / Elemento della lista di controllo [4.X]

**Esempio**: [Esempio di codice o link a ISMS-CTX-A.8.28]
```

## Commento di approvazione della sicurezza

```
**Revisione della sicurezza completata**

Revisionato da: [Nome del Security Champion]
Data: [GG.MM.AAAA]

Sezioni della lista di controllo applicate:

- [X] Autenticazione (4.1)
- [X] Validazione degli input (4.2)
- [X] Autorizzazione (4.4)

Risultati:

- [Problema 1]: Affrontato nel commit [hash]
- [Problema 2]: Rischio accettato con giustificazione [link]

**Approvato per la fusione** senza problemi di sicurezza in sospeso.
```

---

# Procedure di escalation

## Quando effettuare l'escalation

**Al Security Champion**:

- Applicazione della lista di controllo poco chiara
- Necessità di validazione del pattern di sicurezza
- Più elementi della lista di controllo non superati
- Necessità di formazione o indicazioni

**Al team di sicurezza applicativa**:

- Vulnerabilità Critica/Alta sospetta
- Preoccupazione di sicurezza a livello architetturale
- Necessità di modellazione delle minacce
- Risultati degli strumenti che richiedono validazione esperta
- Raccomandazione di test di penetrazione

## Canali di escalation

| Tipo di problema | Canale | Tempo di risposta |
|-----------------|--------|-------------------|
| **Domanda durante la revisione** | Slack #security-champions | < 4 ore (orario lavorativo) |
| **Preoccupazione di sicurezza (non urgente)** | Slack #appsec | < 1 giorno lavorativo |
| **Vulnerabilità di sicurezza (Alta)** | Email security@org.com + Slack | < 4 ore |
| **Vulnerabilità di sicurezza (Critica)** | Processo di risposta agli incidenti | Immediato |

---

# Manutenzione del documento

**Frequenza di aggiornamento**: Trimestrale o quando:

- OWASP Top 10 aggiornato
- Nuovi pattern di vulnerabilità identificati
- Modifiche allo stack tecnologico dell'organizzazione
- Modifiche ai requisiti della politica (aggiornamenti di ISMS-POL-A.8.28)

**Proprietario**: Responsabile della sicurezza applicativa

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | Responsabile della sicurezza applicativa | Riferimento iniziale per la revisione del codice estratto dalla politica consolidata |

---

**FINE DI ISMS-REF-A.8.28**

*Questo riferimento tecnico supporta l'implementazione di ISMS-POL-A.8.28. I requisiti vincolanti sono nella politica, non in questo documento.*
<!-- QA_VERIFIED: 2026-04-04 -->
