<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.11-IT-data-masking-technical-reference:framework:CTX:a.8.11 -->
**ISMS-CTX-A.8.11 — Riferimento tecnico sul mascheramento dei dati**
**Tecniche di mascheramento, metodi di scoperta e modelli di implementazione (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento tecnico sul mascheramento dei dati |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-CTX-A.8.11 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Documento vivente |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | Team di architettura della sicurezza | Riferimento tecnico iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: In base alle esigenze (evoluzione delle tecnologie e delle tecniche)  
**Prossima data di revisione**: [Data + 12 mesi]

**Distribuzione**: Ingegneria della sicurezza, Ingegneria dei dati, Team di sviluppo, Operazioni IT

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione. NON fa parte del SGSI e NON sostituisce ISMS-POL-A.8.11. I requisiti vincolanti sono definiti esclusivamente in **ISMS-POL-A.8.11 (Politica di mascheramento dei dati)**.

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce un'analisi tecnica approfondita dei modelli di implementazione, delle tecniche e delle metodologie di mascheramento dei dati comunemente incontrate nei moderni sistemi informativi. È inteso a supportare:

- La consapevolezza tecnica delle opzioni di implementazione del mascheramento
- La comprensione dei compromessi nella selezione delle tecniche
- Le indicazioni pratiche per la scoperta e la classificazione dei dati
- Il contesto per la valutazione delle tecnologie e degli strumenti (indipendente dai fornitori)
- La pianificazione dell'implementazione per i team di sviluppo e operazioni

## Relazione con il SGSI

Questo documento è un **riferimento tecnico non vincolante**. Tutti i requisiti di controllo del mascheramento dei dati sono definiti esclusivamente in ISMS-POL-A.8.11.

## Organizzazione dei contenuti

- **Sezione 2**: Specifiche dettagliate delle tecniche di mascheramento
- **Sezione 3**: Metodologie di scoperta dei dati
- **Sezione 4**: Panorama degli strumenti di mascheramento
- **Sezione 5**: Modelli di implementazione
- **Sezione 6**: Guide di riferimento rapido

---

# Specifiche delle tecniche di mascheramento

## Tecniche di mascheramento statico dei dati (SDM)

**Panoramica**: Il mascheramento statico dei dati sostituisce permanentemente i dati sensibili nei database non di produzione con dati fittizi ma realistici. I dati originali vengono sovrascritti in modo irreversibile durante un processo di mascheramento una tantum.

### Tecniche di sostituzione (sostituzione)

**Sostituzione a livello di caratteri**:

```
Originale: "Mario Rossi"
Tecnica: Sostituire ogni carattere con un carattere casuale dello stesso tipo
Mascherato: "Lmpq Tnkui"

Configurazione:
- Preservazione della classe di caratteri: Lettera→Lettera, Cifra→Cifra
- Preservazione delle maiuscole: Maiuscola→Maiuscola, Minuscola→Minuscola
- Preservazione della lunghezza: Stesso numero di caratteri
```

**Sostituzione a livello di parole**:

```
Originale: "Mario Rossi"
Tecnica: Sostituire con un nome casuale da un dizionario
Mascherato: "Luca Bianchi"

Configurazione:
- Fonte del dizionario: Elenchi di nomi integrati, database di nomi esterni
- Contesto culturale: Corrispondenza di origine (nomi italiani, occidentali, ecc.)
- Preservazione del genere: Maschile→Maschile, Femminile→Femminile (se determinabile)
- Coerenza: Lo stesso input produce sempre lo stesso output (deterministico)
```

**Sostituzione con preservazione del formato**:

```
Email originale: "mario.rossi@esempio.com"
Tecnica: Sostituire le parti preservando il formato
Mascherato: "luca.bianchi@esempio.com"

Configurazione:
- Conservare il dominio per i test di recapitabilità
- Sostituire la parte locale con un nome realistico
- Mantenere le posizioni "@" e "."
```

**Considerazioni sull'implementazione**:

- **Integrità referenziale**: Utilizzare algoritmi deterministici (basati su hash) per garantire che lo stesso input produca lo stesso output in tutte le tabelle
- **Distribuzione dei dati**: Mantenere la distribuzione statistica per i test di prestazioni
- **Unicità**: Garantire che i valori mascherati rimangano univoci quando i dati originali lo erano
- **Prestazioni**: Elaborazione in batch per grandi set di dati

### Tecniche di mescolamento (permutazione)

**Mescolamento di colonne**:

```
Tabella originale:
ID | Nome           | Email
1  | Mario Rossi    | mario@esempio.com
2  | Anna Bianchi   | anna@esempio.com
3  | Luca Verdi     | luca@esempio.com

Dopo il mescolamento della colonna Email:
ID | Nome           | Email
1  | Mario Rossi    | luca@esempio.com
2  | Anna Bianchi   | mario@esempio.com
3  | Luca Verdi     | anna@esempio.com
```

**Configurazione**:

- Ambito del mescolamento: Solo all'interno di una singola tabella
- Seme casuale: Deterministico per la ripetibilità
- Preservazione dei vincoli: Evitare le violazioni dei vincoli di unicità
- Gestione delle chiavi esterne: Mescolare solo le colonne non-FK

**Limitazioni**: Potrebbe non soddisfare gli standard di de-identificazione normativi (RGPD, HIPAA).

### Aggiunta di varianza/rumore (dati numerici)

**Rumore additivo**:

```
Stipendio originale: 75.000 €
Tecnica: Aggiungere una varianza casuale ±10%
Mascherato: 72.345 € o 81.250 €

Configurazione:
- Intervallo di varianza: ±5% a ±20% tipico
- Distribuzione: Uniforme, gaussiana
- Preservazione del segno: Mantenere positivo/negativo
- Verifica dei limiti: Garantire che il risultato rimanga nell'intervallo valido
```

**Rumore moltiplicativo**:

```
Età originale: 35
Tecnica: Moltiplicare per un fattore casuale 0,9-1,1
Mascherato: 33 o 38

Configurazione:
- Intervallo del fattore: 0,8-1,2 tipico
- Arrotondamento: Arrotondare agli interi per l'età, agli euro interi per le valute
```

### Tecniche di nullificazione/soppressione

**Nullificazione completa**:

```
Originale: "Memo interno riservato"
Mascherato: NULL

Configurazione:
- Preservare l'esistenza della colonna (NULL vs. eliminare la colonna)
- Gestire i vincoli NOT NULL (utilizzare un segnaposto)
```

**Nullificazione parziale con segnaposto**:

```
Originale: "mario.rossi@esempio.com"
Mascherato: "mascherato@mascherato.com"

Configurazione:
- Valore del segnaposto: "MASCHERATO", "OSCURATO", stringa vuota
- Compatibilità applicativa: Garantire che le app gestiscano il segnaposto correttamente
```

### Mascheramento di date e orari

**Spostamento delle date**:

```
Data originale: 15-03-2024
Tecnica: Aggiungere uno spostamento casuale ±180 giorni
Mascherato: 22-01-2024 o 10-08-2024

Configurazione:
- Intervallo dello spostamento: Giorni, settimane o mesi
- Coerenza: La stessa persona ottiene lo stesso spostamento (deterministico basato sull'ID)
- Preservazione della sequenza: L'ordine degli eventi è mantenuto
```

**Generalizzazione delle date**:

```
Originale: 15-03-2024
Mascherato: 01-03-2024 (marzo 2024, giorno rimosso)
Mascherato: T1 2024 (T1 2024, mese rimosso)
Mascherato: 2024 (solo anno)
```

## Tecniche di mascheramento dinamico dei dati (DDM)

**Panoramica**: Il mascheramento dinamico applica le regole di mascheramento in tempo reale al punto di accesso ai dati in base al ruolo o al contesto dell'utente. I dati originali rimangono invariati nell'archiviazione.

### Mascheramento basato sui ruoli

**DDM a livello di database**:

```sql
-- Esempio: PostgreSQL con funzione di mascheramento

CREATE FUNCTION maschera_email(email TEXT) RETURNS TEXT AS $$
BEGIN
  IF current_user_role() = 'admin' THEN
    RETURN email;  -- L'admin vede l'email completa
  ELSE
    RETURN REGEXP_REPLACE(email, '^(.{2}).*(@.*)$', '\1***\2');
    -- Gli utenti normali vedono: "ma***@esempio.com"
  END IF;
END;
$$ LANGUAGE plpgsql;

-- Applicare a una vista
CREATE VIEW clienti_mascherati AS
SELECT 
  id_cliente,
  nome_cliente,
  maschera_email(email) AS email,
  CASE 
    WHEN current_user_role() = 'admin' THEN telefono
    ELSE '***-***-' || RIGHT(telefono, 4)
  END AS telefono
FROM clienti;
```

**DDM a livello applicativo**:

```python
def get_dati_cliente(id_cliente, ruolo_utente):
    cliente = db.query(f"SELECT * FROM clienti WHERE id={id_cliente}")
    
    if ruolo_utente == 'admin':
        return cliente
    elif ruolo_utente == 'supporto':
        cliente.email = maschera_email(cliente.email)
        cliente.telefono = maschera_telefono(cliente.telefono)
        return cliente
    else:
        cliente.email = "***@***"
        cliente.telefono = "***-***-****"
        cliente.indirizzo = "[OSCURATO]"
        return cliente

def maschera_email(email):
    parti = email.split('@')
    return f"{parti[0][:2]}***@{parti[1]}"

def maschera_telefono(telefono):
    return f"***-***-{telefono[-4:]}"
```

### Mascheramento basato sul contesto

```
Contesto: Schermata dettaglio cliente → Mostrare carta parziale
Contesto: Esportazione report finanziario → Mostrare carta completa (utenti autorizzati)
Contesto: Notifica email → Mostrare carta mascherata (tutti gli utenti)

Configurazione:
- Rilevamento del contesto: ID schermata, tipo di report, formato di esportazione
- Priorità delle regole: Le regole di contesto prevalgono sulle regole basate sui ruoli
```

### Mascheramento a livello di query

```sql
-- Query utente autorizzato:
SELECT nome_cliente, stipendio FROM dipendenti;
-- Restituisce: Stipendi individuali

-- Stessa query per utente non autorizzato:
SELECT 'OSCURATO' AS nome_cliente,
       CASE 
         WHEN COUNT(*) < 10 THEN 'N/D'
         ELSE ROUND(AVG(stipendio), -3)
       END AS stipendio
FROM dipendenti
GROUP BY dipartimento;
-- Restituisce: Solo dati aggregati
```

## Tecniche di tokenizzazione

**Panoramica**: La tokenizzazione sostituisce i dati sensibili con token non sensibili mantenendo i dati originali in un vault di token sicuro. I token mantengono il formato ma non hanno alcun significato intrinseco.

### Tokenizzazione con preservazione del formato

**Tokenizzazione di carta di credito**:

```
PAN originale: 4532-1234-5678-9010
Token: 4532-7821-3456-1098

Configurazione:
- Preservazione del BIN: Prime 6 cifre (Bank Identification Number) preservate
- Preservazione delle ultime 4: Ultime 4 cifre preservate per il riferimento del cliente
- Preservazione del formato: Trattini, lunghezza mantenuti
- Verifica Luhn: Il token supera la validazione dell'algoritmo di Luhn
- Archiviazione nel vault: PAN originale archiviato crittografato nel vault
```

**Modello di implementazione**:

```python
class VaultToken:
    def __init__(self):
        self.token_a_valore = {}
        self.valore_a_token = {}
    
    def tokenizza(self, pan, preserva_bin=True, preserva_ultimi_4=True):
        if pan in self.valore_a_token:
            return self.valore_a_token[pan]
        
        if preserva_bin and preserva_ultimi_4:
            bin = pan[:6]
            ultimi_4 = pan[-4:]
            mezzo = genera_cifre_casuali(6)
            token = f"{bin}{mezzo}{ultimi_4}"
            token = aggiusta_per_luhn(token)
        else:
            token = genera_pan_casuale()
        
        self.token_a_valore[token] = cifra(pan)
        self.valore_a_token[pan] = token
        
        return token
    
    def detokenizza(self, token, richiedente_autorizzato=True):
        if not richiedente_autorizzato:
            raise PermissionError("Detokenizzazione non autorizzata")
        
        registro_audit(f"Detokenizzazione: token={token}, utente={utente_corrente()}")
        return decifra(self.token_a_valore[token])
```

**Sicurezza del vault di token**:

- Crittografia dei dati del vault (AES-256)
- Controllo degli accessi: La detokenizzazione richiede un'autorizzazione esplicita
- Registrazione di audit di tutte le operazioni
- Gestione delle chiavi secondo la politica di crittografia A.8.24

### Tokenizzazione non preservante il formato

```
CF originale: RSSMRA85M01H501Z
Token: 8f3d9a21-c8b4-4e7a-9d12-5c6f8a2e4b9d (UUID)

Configurazione:
- Formato del token: UUID, alfanumerico casuale
- Garanzia di unicità: Casualità crittografica
```

## Tecniche di pseudonimizzazione (conformità RGPD)

**Panoramica**: La pseudonimizzazione sostituisce gli identificatori diretti con pseudonimi in modo che i dati non possano identificare gli individui senza informazioni aggiuntive (chiave o mapping) conservate separatamente. Soddisfa i requisiti del RGPD per il trattamento a rischio ridotto.

### Pseudonimizzazione crittografica

**Pseudonimizzazione basata su HMAC**:

```python
import hmac
import hashlib

def pseudonimizza(identificatore, chiave_segreta):
    """
    Generare uno pseudonimo usando HMAC-SHA256
    Deterministico: Stesso input + chiave = stesso pseudonimo
    """
    pseudonimo = hmac.new(
        key=chiave_segreta.encode(),
        msg=identificatore.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return pseudonimo

identificatore_originale = "mario.rossi@esempio.com"
chiave_segreta = "chiave-segreta-specifica-organizzazione"

pseudonimo = pseudonimizza(identificatore_originale, chiave_segreta)
# Risultato: "8d3f9c2a1b4e5f6d7c8e9a0b1c2d3e4f..."
```

**Pseudonimizzazione reversibile**:

```python
from cryptography.fernet import Fernet

def crea_chiave_pseudonimizzazione():
    return Fernet.generate_key()

def pseudonimizza_reversibile(identificatore, chiave):
    cifrario = Fernet(chiave)
    pseudonimo = cifrario.encrypt(identificatore.encode())
    return pseudonimo.decode()

def de_pseudonimizza(pseudonimo, chiave):
    cifrario = Fernet(chiave)
    originale = cifrario.decrypt(pseudonimo.encode())
    return originale.decode()
```

**Considerazioni sulla conformità RGPD**:

- Chiave di pseudonimizzazione conservata separatamente dai dati pseudonimizzati
- La re-identificazione richiede un'autorizzazione esplicita oltre all'accesso ai dati
- Rotazione delle chiavi: Pianificare la rotazione periodica (richiede la ri-pseudonimizzazione)
- Audit: Registrare tutti i tentativi di re-identificazione

### Tabelle di mapping degli pseudonimi

```
Set di dati pseudonimizzato:
ID_Pseudonimo | Età | Città    | Condizione_Medica
PS001         | 45  | Zurigo   | Diabete
PS002         | 32  | Ginevra  | Ipertensione

Tabella di mapping (conservata separatamente, accesso limitato):
ID_Pseudonimo | Nome_Reale
PS001         | Mario Rossi
PS002         | Anna Bianchi
```

**Configurazione**:

- Separazione dell'archiviazione: Tabella di mapping in un sistema/database separato
- Controllo degli accessi: Permessi diversi per i dati pseudonimizzati vs. il mapping
- Crittografia: Tabella di mapping crittografata a riposo
- Audit: Tutti gli accessi alla tabella di mapping registrati

### k-Anonimato e l-Diversità

**k-Anonimato**: Garantire che ogni combinazione di quasi-identificatori appaia almeno k volte.

```
Dati originali:
Età | CAP   | Condizione
25  | 6000  | Influenza
26  | 6002  | Diabete
27  | 6000  | Ipertensione

k-Anonimato (k=2) Generalizzato:
Fascia d'età | Area CAP   | Condizione
20-30        | 6000-6099  | Influenza
20-30        | 6000-6099  | Diabete
20-30        | 6000-6099  | Ipertensione
```

**Tecniche di generalizzazione**:

- Età: Età esatta → Fasce d'età (20-30, 30-40, ecc.)
- CAP: Codice postale a 4 cifre → Prefisso a 2 cifre
- Data: Data esatta → Mese o Trimestre
- Reddito: Importo esatto → Fasce di reddito

**l-Diversità**: Estendere il k-anonimato per garantire la diversità degli attributi sensibili.

```
k-Anonimato (k=3) ma non l-Diverso:
→ Tutti i record hanno lo stesso attributo sensibile (Diabete)

l-Diversità (l=2):
Fascia d'età | Area CAP   | Condizione
20-30        | 6000-6099  | Diabete
20-30        | 6000-6099  | Influenza
20-30        | 6000-6099  | Ipertensione
→ Almeno 2 attributi sensibili diversi nel gruppo
```

## Tecniche di anonimizzazione (irreversibili)

**Panoramica**: L'anonimizzazione rimuove irreversibilmente le informazioni identificative in modo che la re-identificazione sia impossibile anche con dati aggiuntivi. I dati anonimizzati non sono più dati personali ai sensi del RGPD.

### Aggregazione e controllo della divulgazione statistica

```
Dati microdata individuali:
Dipendente | Età | Stipendio
Mario      | 35  | 75.000
Anna       | 42  | 82.000
Luca       | 38  | 79.000

Dati aggregati (anonimi):
Fascia d'età | N. dipendenti | Stipendio medio
30-40        | 3             | 78.667

Risultato: Individui non identificabili, utilità dei dati preservata
```

**Dimensione minima del gruppo**:

```
Configurazione:
- k-anonimato: Minimo 5-10 individui per gruppo (standard normativo)
- Soppressione: I gruppi più piccoli di k vengono soppressi o fusi
```

### Soppressione dei dati

**Soppressione di celle**:

```
Dati originali con combinazioni rare:
Età | Città     | Condizione
25  | Willisau  | Malattia rara X  ← 1 sola persona, alto rischio

Soppressi:
Età | Città     | Condizione
*   | Willisau  | *                ← Soppresso per proteggere l'identità
```

---

# Metodologie di scoperta dei dati

## Riconoscimento automatico di pattern

**Analisi tramite espressioni regolari**:

```python
PATTERN = {
    'carta_credito': r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b',
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'telefono': r'\b(?:\+?\d{1,3}[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b',
    'iban': r'\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b',
    'codice_fiscale': r'\b[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]\b',
}

def analizza_colonna_per_pattern(dati_colonna, dimensione_campione=1000):
    risultati = {}
    campione = dati_colonna.sample(min(dimensione_campione, len(dati_colonna)))
    
    for nome_pattern, pattern in PATTERN.items():
        corrispondenze = campione.str.contains(pattern, regex=True, na=False)
        percentuale = (corrispondenze.sum() / len(campione)) * 100
        
        if percentuale > 10:
            risultati[nome_pattern] = percentuale
    
    return risultati
```

**Riconoscimento di entità nominate (NER)**:

```python
import spacy

nlp = spacy.load("it_core_news_sm")

def rileva_entità_dcp(testo):
    doc = nlp(testo)
    entità = {'PER': [], 'ORG': [], 'LOC': [], 'DATE': []}
    
    for ent in doc.ents:
        if ent.label_ in entità:
            entità[ent.label_].append(ent.text)
    
    return entità
```

## Analisi dei metadati del database

**Euristiche sui nomi delle colonne**:

```python
PAROLE_CHIAVE_SENSIBILI = {
    'DCP': ['nome', 'cognome', 'email', 'telefono', 'indirizzo', 'cf', 'passport', 'ddn'],
    'Finanziario': ['carta', 'conto', 'iban', 'swift', 'saldo', 'stipendio', 'pagamento'],
    'Sanitario': ['medico', 'diagnosi', 'prescrizione', 'paziente', 'assicurazione'],
    'Credenziali': ['password', 'segreto', 'token', 'chiave', 'api_key'],
}

def classifica_colonna_per_nome(nome_colonna):
    nome_minus = nome_colonna.lower()
    for categoria, parole_chiave in PAROLE_CHIAVE_SENSIBILI.items():
        if any(parola in nome_minus for parola in parole_chiave):
            return categoria
    return 'Sconosciuto'
```

## Profilazione e analisi statistica

```python
def profila_colonna(dati_colonna):
    profilo = {
        'n_righe': len(dati_colonna),
        'n_null': dati_colonna.isnull().sum(),
        'n_univoci': dati_colonna.nunique(),
        'tipo_dati': str(dati_colonna.dtype),
        'rapporto_unicità': dati_colonna.nunique() / len(dati_colonna),
    }
    
    if profilo['rapporto_unicità'] > 0.95:
        profilo['probabile_identificatore'] = True
    
    return profilo
```

## Strumenti di scoperta dei dati (categorie indipendenti dai fornitori)

**Strumenti di scansione del database**:

- Cloud-native: Azure Purview, AWS Macie, Google DLP API
- On-premises: IBM InfoSphere, Informatica Data Privacy Management
- Open source: DataHub, Amundsen, Apache Atlas

---

# Panorama degli strumenti di mascheramento

## Matrice delle capacità degli strumenti

| Capacità | Database nativo | Strumenti dedicati | Strumenti ETL | Livello applicativo |
|---------|----------------|-------------------|---------------|---------------------|
| **Mascheramento statico** | Limitato | Eccellente | Buono | Limitato |
| **Mascheramento dinamico** | Buono | Eccellente | No | Eccellente |
| **Preservazione del formato** | Limitato | Eccellente | Buono | Limitato |
| **Integrità referenziale** | Buono | Eccellente | Eccellente | Manuale |
| **Prestazioni** | Eccellente | Buono | Buono | Variabile |
| **Costo** | Basso (incluso) | Alto | Medio | Basso (sforzo di sviluppo) |

---

# Guide di riferimento rapido

## Albero decisionale per la selezione delle tecniche

```
INIZIO: Necessità di mascherare i dati sensibili

D1: L'utilità dei dati è richiesta nell'ambiente mascherato?
    NO → Utilizzare: Oscuramento/Nullificazione (più semplice)
    SÌ → Continuare

D2: Il mascheramento deve essere reversibile?
    SÌ → D2a: Chi deve invertire?
        - Solo utenti autorizzati → Tokenizzazione o Pseudonimizzazione
        - L'applicazione ha bisogno di integrità referenziale → Tokenizzazione

    NO → Continuare

D3: È per il controllo degli accessi in produzione?
    SÌ → Mascheramento dinamico (DDM)
    NO → Continuare (uso non-produzione)

D4: L'integrità referenziale tra tabelle deve essere preservata?
    SÌ → SDM deterministico
    NO → SDM casuale

D5: Requisito normativo (RGPD, PCI DSS, HIPAA)?
    - Pseudonimizzazione RGPD → Pseudonimizzazione crittografica
    - Mascheramento PCI DSS → Tokenizzazione o SDM con preservazione del formato
    - De-identificazione HIPAA → Anonimizzazione
    - Nessuno → SDM con sostituzione
```

## Scenari di mascheramento comuni

**Scenario 1: Database di test dalla produzione**

```
Problema: Necessità di dati di test realistici senza esporre le DCP

Soluzione:
1. Esportare schema e dati di produzione
2. Applicare il mascheramento statico (SDM):
   - Nomi: Sostituzione con nomi falsi (deterministico)
   - Email: Sostituzione con preservazione del formato
   - Indirizzi: Sostituzione con indirizzi falsi ma validi
   - Telefoni: Cifre casuali con preservazione del formato
   - Date: Spostamento casuale coerente per persona

3. Validare l'integrità referenziale
4. Caricare nell'ambiente di test
```

**Scenario 2: Analisi con protezione delle DCP**

```
Problema: La BI ha bisogno di dati aggregati senza identificazione individuale

Soluzione:
1. Pseudonimizzare gli identificatori
2. Generalizzare i quasi-identificatori (età → fascia, CAP → prefisso)
3. Aggregare le metriche sensibili
4. Implementare il k-anonimato (k=5 minimo)
5. Sopprimere le combinazioni rare
```

**Scenario 3: Accesso in produzione per il supporto clienti**

```
Problema: Il supporto ha bisogno dei dati del cliente ma non delle DCP complete

Soluzione:
1. Implementare il DDM nel database di produzione
2. Configurare le regole basate sui ruoli:
   - Supporto: Email parziale (ma***@esempio.com), ultimi 4 del telefono
   - Manager: Email completa, telefono completo
   - Admin: Tutto non mascherato

3. Registrare tutti gli accessi ai campi sensibili
```

## Guida alla risoluzione dei problemi

**Problema: I dati mascherati interrompono la logica applicativa**

```
Causa: I dati mascherati non corrispondono al formato o ai vincoli attesi
Soluzioni:
- Utilizzare tecniche di mascheramento con preservazione del formato
- Aggiornare le regole di validazione per accettare i formati mascherati
- Testare i dati mascherati con l'applicazione prima della distribuzione
```

**Problema: Violazioni dell'integrità referenziale dopo il mascheramento**

```
Causa: Mascheramento non deterministico o mascheramento incompleto delle tabelle correlate
Soluzioni:
- Utilizzare il mascheramento deterministico (stesso input → stesso output)
- Mascherare tutte le tabelle correlate insieme
- Mantenere il mapping delle relazioni FK durante il mascheramento
```

**Problema: Degradazione delle prestazioni con il DDM**

```
Causa: Le funzioni di mascheramento impediscono l'uso degli indici
Soluzioni:
- Ottimizzare le funzioni di mascheramento
- Rivedere i piani di esecuzione delle query
- Considerare il mascheramento statico per gli ambienti non di produzione
- Implementare un livello di cache per i dati mascherati frequentemente acceduti
```

## Lista di controllo di conformità

**PCI DSS (Req. 3.4-3.5)**:

- [ ] Numero di conto primario (PAN) mascherato alla visualizzazione (max 6 primi + 4 ultimi)
- [ ] PAN illeggibile negli ambienti non di produzione
- [ ] CVV2/CVC2 mai archiviato
- [ ] Soluzione di mascheramento che impedisce l'accesso non autorizzato al PAN non mascherato
- [ ] Procedure di mascheramento documentate
- [ ] Convalida annuale dell'efficacia del mascheramento

**Pseudonimizzazione RGPD (Art. 32, 89)**:

- [ ] Chiave di pseudonimizzazione conservata separatamente dai dati pseudonimizzati
- [ ] La re-identificazione richiede informazioni non disponibili al responsabile del trattamento
- [ ] Misure tecniche e organizzative che impediscono la re-identificazione non autorizzata
- [ ] Pseudonimizzazione documentata nella valutazione d'impatto sulla protezione dei dati (DPIA)
- [ ] Revisione periodica dell'efficacia della pseudonimizzazione

**De-identificazione HIPAA (§164.514)**:

- [ ] Metodo Safe Harbor: Rimuovere tutti i 18 identificatori HIPAA, OPPURE
- [ ] Determinazione esperta: Verifica statistica da parte di un esperto qualificato
- [ ] Nessuna conoscenza effettiva della possibilità di re-identificazione
- [ ] Codice di record per la re-identificazione conservato separatamente
- [ ] Documentazione del metodo di de-identificazione e convalida

---

# Migliori pratiche di implementazione

## Flusso di lavoro del processo di mascheramento

```
1. SCOPRIRE
   ├─ Inventariare sistemi e database
   ├─ Analizzare per pattern di dati sensibili
   ├─ Classificare i dati per sensibilità
   └─ Identificare i requisiti normativi

2. PROGETTARE
   ├─ Selezionare le tecniche di mascheramento appropriate
   ├─ Definire le regole di mascheramento per elemento di dati
   ├─ Pianificare il mantenimento dell'integrità referenziale
   └─ Documentare le specifiche di mascheramento

3. SVILUPPARE/CONFIGURARE
   ├─ Configurare lo strumento di mascheramento o sviluppare script
   ├─ Implementare gli algoritmi di mascheramento
   ├─ Configurare i vault di token (se si utilizza la tokenizzazione)
   └─ Creare i flussi di esecuzione del mascheramento

4. TESTARE
   ├─ Validare l'efficacia del mascheramento (dati originali assenti)
   ├─ Testare l'integrità referenziale
   ├─ Verificare la compatibilità applicativa
   ├─ Test delle prestazioni
   └─ Test di re-identificazione (impossibile recuperare l'originale)

5. DISTRIBUIRE
   ├─ Eseguire il mascheramento iniziale (SDM) o abilitare le regole (DDM)
   ├─ Validare il successo della distribuzione
   ├─ Monitorare errori e prestazioni
   └─ Documentare la distribuzione

6. MONITORARE E MANTENERE
   ├─ Test periodici di efficacia
   ├─ Monitorare l'esposizione di dati non mascherati
   ├─ Aggiornare le regole per i nuovi tipi di dati
   ├─ Convalida annuale della conformità
   └─ Risposta agli incidenti in caso di errori di mascheramento
```

## Errori comuni da evitare

**Errore 1: Mascherare solo le DCP "ovvie"**

```
Sbagliato: Mascherare nome, email, telefono ma ignorare...
- Nome utente (spesso uguale all'email)
- Campi commenti/note (possono contenere DCP in testo libero)
- File di log (potrebbero registrare dati sensibili)
- Sistemi di backup/archivio (ambienti dimenticati)

Soluzione: Scoperta completa dei dati in TUTTI i sistemi e formati
```

**Errore 2: Mascheramento incoerente tra gli ambienti**

```
Sbagliato: Ambiente dev mascherato, ma ambiente QA ha una copia non mascherata
Soluzione: Mascheramento automatizzato nel pipeline di provisioning dei dati
```

**Errore 3: Mentalità "mascherare dopo"**

```
Sbagliato: Copiare la produzione nel non-produzione, pianificare di mascherare "quando ci sarà tempo"
Soluzione: Mascheramento come parte del processo di copia dei dati
```

**Errore 4: Mascheramento solo lato client**

```
Sbagliato: JavaScript maschera i dati nell'UI, ma il backend restituisce i dati completi
Soluzione: Applicare il mascheramento lato server
```

---

# Glossario dei termini tecnici

**Crittografia con preservazione del formato (FPE)**: Crittografia che mantiene il formato dei dati originali.

**Algoritmo di Luhn**: Formula di checksum per la validazione delle carte di credito.

**Quasi-identificatore**: Attributo che può identificare gli individui quando combinato con altri attributi.

**Attacco di re-identificazione**: Tentativo di recuperare l'identità originale da dati mascherati o anonimizzati.

**Sale (crittografico)**: Dati casuali aggiunti all'input prima dell'hashing per prevenire attacchi con tavole arcobaleno.

**Vault di token**: Database sicuro che archivia il mapping tra token e valori sensibili originali nei sistemi di tokenizzazione.

---

**FINE DEL RIFERIMENTO TECNICO**

*Questo è un documento vivente — aggiornato man mano che le tecnologie, le tecniche e le migliori pratiche di mascheramento evolvono.*

*Promemoria: Questo documento NON è SGSI. I requisiti vincolanti sono in ISMS-POL-A.8.11 (Politica di mascheramento dei dati).*

<!-- QA_VERIFIED: 2026-04-04 -->
