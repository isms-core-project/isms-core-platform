<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.11-FR-data-masking-technical-reference:framework:CTX:a.8.11 -->
**ISMS-CTX-A.8.11 — Référence technique du masquage des données**
**Techniques de masquage, méthodes de découverte et modèles d'implémentation (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence technique du masquage des données |
| **Type de document** | Interne — Référence technique (non SMSI) |
| **Identifiant du document** | ISMS-CTX-A.8.11 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Document évolutif |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | Équipe d'architecture de sécurité | Référence technique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Selon les besoins (évolution des technologies et techniques)  
**Prochaine date de révision** : [Date + 12 mois]

**Distribution** : Ingénierie de sécurité, Ingénierie des données, Équipes de développement, Opérations IT

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement. Il ne fait PAS partie du SMSI et ne remplace PAS ISMS-POL-A.8.11. Les exigences contraignantes sont définies exclusivement dans **ISMS-POL-A.8.11 (Politique de masquage des données)**.

---

# Objectif et portée du document

## Objectif

Ce document fournit une analyse technique approfondie des modèles d'implémentation, techniques et méthodologies de masquage des données couramment rencontrés dans les systèmes d'information modernes. Il vise à soutenir :

- La sensibilisation technique aux options d'implémentation du masquage
- La compréhension des compromis dans la sélection des techniques
- Les conseils pratiques pour la découverte et la classification des données
- Le contexte pour l'évaluation des technologies et des outils (indépendant des fournisseurs)
- La planification de l'implémentation pour les équipes de développement et d'exploitation

## Relation avec le SMSI

Ce document est une **référence technique non contraignante**. Toutes les exigences de contrôle du masquage des données sont définies exclusivement dans ISMS-POL-A.8.11.

## Organisation du contenu

- **Section 2** : Spécifications détaillées des techniques de masquage
- **Section 3** : Méthodologies de découverte des données
- **Section 4** : Paysage des outils de masquage (comparaison indépendante des fournisseurs)
- **Section 5** : Modèles d'implémentation
- **Section 6** : Guides de référence rapide

---

# Spécifications des techniques de masquage

## Techniques de masquage statique des données (SDM)

**Vue d'ensemble** : Le masquage statique des données remplace définitivement les données sensibles dans les bases de données non-production par des données fictives mais réalistes. Les données originales sont écrasées de manière irréversible lors d'un processus de masquage unique.

### Techniques de substitution (remplacement)

**Substitution au niveau des caractères** :

```
Original : "Jean Dupont"
Technique : Remplacer chaque caractère par un caractère aléatoire du même type
Masqué : "Lmpq Tnkui"

Configuration :
- Préservation de la classe de caractères : Lettre→Lettre, Chiffre→Chiffre
- Préservation de la casse : Majuscule→Majuscule, Minuscule→Minuscule
- Préservation de la longueur : Même nombre de caractères
```

**Substitution au niveau des mots** :

```
Original : "Jean Dupont"
Technique : Remplacer par un nom aléatoire issu d'un dictionnaire
Masqué : "Michel Martin"

Configuration :
- Source du dictionnaire : Listes de noms intégrées, bases de données de noms externes
- Contexte culturel : Correspondance d'origine (noms occidentaux, asiatiques, etc.)
- Préservation du genre : Masculin→Masculin, Féminin→Féminin (si déterminable)
- Cohérence : La même entrée produit toujours la même sortie (déterministe)
```

**Substitution préservant le format** :

```
Email original : "jean.dupont@exemple.com"
Technique : Remplacer les parties tout en préservant le format
Masqué : "michel.martin@exemple.com"

Configuration :
- Conserver le domaine pour les tests de délivrabilité
- Remplacer la partie locale par un nom réaliste
- Maintenir les positions "@" et "."
```

**Considérations d'implémentation** :

- **Intégrité référentielle** : Utiliser des algorithmes déterministes (basés sur le hachage) pour garantir que la même entrée produit la même sortie dans toutes les tables
- **Distribution des données** : Maintenir la distribution statistique pour les tests de performance
- **Unicité** : S'assurer que les valeurs masquées restent uniques lorsque les données originales l'étaient
- **Performance** : Traitement par lots pour les grands ensembles de données

### Techniques de mélange (permutation)

**Mélange de colonnes** :

```
Table originale :
ID | Nom            | Email
1  | Jean Dupont    | jean@exemple.com
2  | Alice Martin   | alice@exemple.com
3  | Bob Durand     | bob@exemple.com

Après mélange de la colonne Email :
ID | Nom            | Email
1  | Jean Dupont    | bob@exemple.com
2  | Alice Martin   | jean@exemple.com
3  | Bob Durand     | alice@exemple.com
```

**Configuration** :

- Portée du mélange : Dans une seule table uniquement
- Graine aléatoire : Déterministe pour la répétabilité
- Préservation des contraintes : Éviter les violations de contraintes d'unicité
- Gestion des clés étrangères : Mélanger uniquement les colonnes non-FK

**Cas d'utilisation** : Rupture des liens personne-attribut tout en maintenant la distribution réelle des données.

**Limitations** : Peut ne pas satisfaire les normes de dé-identification réglementaires (RGPD, HIPAA).

### Ajout de variance/bruit (données numériques)

**Bruit additif** :

```
Salaire original : 75 000 €
Technique : Ajouter une variance aléatoire ±10 %
Masqué : 72 345 € ou 81 250 €

Configuration :
- Plage de variance : ±5 % à ±20 % typique
- Distribution : Uniforme, gaussienne
- Préservation du signe : Garder positif/négatif
- Vérification des limites : S'assurer que le résultat reste dans la plage valide
```

**Bruit multiplicatif** :

```
Âge original : 35
Technique : Multiplier par un facteur aléatoire 0,9-1,1
Masqué : 33 ou 38

Configuration :
- Plage du facteur : 0,8-1,2 typique
- Arrondi : Arrondir aux entiers pour l'âge, aux euros entiers pour les montants
```

**Cas d'utilisation** : Montants financiers, âge, taille, poids pour les statistiques.

### Techniques de nullification/suppression

**Nullification complète** :

```
Original : "Mémo interne confidentiel"
Masqué : NULL

Configuration :
- Préserver l'existence de la colonne (NULL vs. supprimer la colonne)
- Gérer les contraintes NOT NULL (utiliser un espace réservé)
```

**Nullification partielle avec espace réservé** :

```
Original : "jean.dupont@exemple.com"
Masqué : "masqué@masqué.com"

Configuration :
- Valeur de l'espace réservé : "MASQUÉ", "EXPURGÉ", chaîne vide
- Compatibilité applicative : S'assurer que les apps gèrent l'espace réservé correctement
```

### Masquage des dates et heures

**Décalage des dates** :

```
Date originale : 15-03-2024
Technique : Ajouter un décalage aléatoire ±180 jours
Masqué : 22-01-2024 ou 10-08-2024

Configuration :
- Plage du décalage : Jours, semaines ou mois
- Cohérence : La même personne obtient le même décalage (déterministe basé sur l'ID)
- Préservation de la séquence : L'ordre des événements est maintenu
```

**Généralisation des dates** :

```
Original : 15-03-2024
Masqué : 01-03-2024 (mars 2024, jour supprimé)
Masqué : T1 2024 (T1 2024, mois supprimé)
Masqué : 2024 (année seulement)
```

## Techniques de masquage dynamique des données (DDM)

**Vue d'ensemble** : Le masquage dynamique applique les règles de masquage en temps réel au point d'accès aux données en fonction du rôle ou du contexte de l'utilisateur. Les données originales restent inchangées en stockage.

### Masquage basé sur les rôles

**DDM au niveau de la base de données** :

```sql
-- Exemple : PostgreSQL avec fonction de masquage

CREATE FUNCTION masquer_email(email TEXT) RETURNS TEXT AS $$
BEGIN
  IF current_user_role() = 'admin' THEN
    RETURN email;  -- L'admin voit l'email complet
  ELSE
    RETURN REGEXP_REPLACE(email, '^(.{2}).*(@.*)$', '\1***\2');
    -- Les utilisateurs réguliers voient : "je***@exemple.com"
  END IF;
END;
$$ LANGUAGE plpgsql;

-- Appliquer à une vue
CREATE VIEW clients_masqués AS
SELECT 
  client_id,
  nom_client,
  masquer_email(email) AS email,
  CASE 
    WHEN current_user_role() = 'admin' THEN telephone
    ELSE '***-***-' || RIGHT(telephone, 4)
  END AS telephone
FROM clients;
```

**DDM au niveau applicatif** :

```python
def get_données_client(client_id, rôle_utilisateur):
    client = db.query(f"SELECT * FROM clients WHERE id={client_id}")
    
    if rôle_utilisateur == 'admin':
        return client
    elif rôle_utilisateur == 'support':
        client.email = masquer_email(client.email)
        client.telephone = masquer_telephone(client.telephone)
        return client
    else:
        client.email = "***@***"
        client.telephone = "***-***-****"
        client.adresse = "[EXPURGÉ]"
        return client

def masquer_email(email):
    parties = email.split('@')
    return f"{parties[0][:2]}***@{parties[1]}"

def masquer_telephone(telephone):
    return f"***-***-{telephone[-4:]}"
```

### Masquage basé sur le contexte

```
Contexte : Écran de détail client → Afficher carte partielle
Contexte : Export rapport financier → Afficher carte complète (utilisateurs autorisés)
Contexte : Notification email → Afficher carte masquée (tous les utilisateurs)

Configuration :
- Détection du contexte : ID écran, type de rapport, format d'export
- Priorité des règles : Les règles de contexte prévalent sur les règles basées sur les rôles
```

### Masquage au niveau des requêtes

```sql
-- Requête utilisateur autorisé :
SELECT nom_client, salaire FROM employés;
-- Retourne : Salaires individuels

-- Requête utilisateur non autorisé :
SELECT 'EXPURGÉ' AS nom_client,
       CASE 
         WHEN COUNT(*) < 10 THEN 'N/A'
         ELSE ROUND(AVG(salaire), -3)
       END AS salaire
FROM employés
GROUP BY département;
-- Retourne : Données agrégées uniquement
```

## Techniques de tokenisation

**Vue d'ensemble** : La tokenisation remplace les données sensibles par des jetons non sensibles tout en stockant les données originales dans un coffre-fort de jetons sécurisé. Les jetons maintiennent le format mais n'ont aucune signification intrinsèque.

### Tokenisation préservant le format

**Tokenisation de carte de crédit** :

```
PAN original : 4532-1234-5678-9010
Jeton : 4532-7821-3456-1098

Configuration :
- Préservation du BIN : Les 6 premiers chiffres (Bank Identification Number) préservés
- Préservation des 4 derniers : 4 derniers chiffres préservés pour la référence client
- Préservation du format : Tirets, longueur maintenus
- Vérification Luhn : Le jeton passe la validation de l'algorithme de Luhn
- Stockage dans le coffre-fort : PAN original stocké chiffré dans le coffre-fort
```

**Modèle d'implémentation** :

```python
class CoffreFortJetons:
    def __init__(self):
        self.jeton_vers_valeur = {}
        self.valeur_vers_jeton = {}
    
    def tokeniser(self, pan, préserver_bin=True, préserver_4_derniers=True):
        if pan in self.valeur_vers_jeton:
            return self.valeur_vers_jeton[pan]
        
        if préserver_bin and préserver_4_derniers:
            bin = pan[:6]
            quatre_derniers = pan[-4:]
            milieu = générer_chiffres_aléatoires(6)
            jeton = f"{bin}{milieu}{quatre_derniers}"
            jeton = ajuster_pour_luhn(jeton)
        else:
            jeton = générer_pan_aléatoire()
        
        self.jeton_vers_valeur[jeton] = chiffrer(pan)
        self.valeur_vers_jeton[pan] = jeton
        
        return jeton
    
    def détokeniser(self, jeton, demandeur_autorisé=True):
        if not demandeur_autorisé:
            raise PermissionError("Détokenisation non autorisée")
        
        journal_audit(f"Détokenisation : jeton={jeton}, utilisateur={utilisateur_courant()}")
        return déchiffrer(self.jeton_vers_valeur[jeton])
```

**Sécurité du coffre-fort de jetons** :

- Chiffrement des données du coffre-fort (AES-256)
- Contrôle d'accès : La détokenisation requiert une autorisation explicite
- Journalisation d'audit de toutes les opérations
- Gestion des clés selon la politique de cryptographie A.8.24

### Tokenisation non préservant le format

```
SSN original : 123-45-6789
Jeton : 8f3d9a21-c8b4-4e7a-9d12-5c6f8a2e4b9d (UUID)

Configuration :
- Format du jeton : UUID, alphanumérique aléatoire
- Garantie d'unicité : Aléatoire cryptographique
```

## Techniques de pseudonymisation (conformité RGPD)

**Vue d'ensemble** : La pseudonymisation remplace les identificateurs directs par des pseudonymes de sorte que les données ne peuvent pas identifier les individus sans informations supplémentaires (clé ou mapping) stockées séparément. Satisfait les exigences du RGPD pour le traitement à risque réduit.

### Pseudonymisation cryptographique

**Pseudonymisation basée sur HMAC** :

```python
import hmac
import hashlib

def pseudonymiser(identifiant, clé_secrète):
    """
    Générer un pseudonyme en utilisant HMAC-SHA256
    Déterministe : Même entrée + clé = même pseudonyme
    """
    pseudonyme = hmac.new(
        key=clé_secrète.encode(),
        msg=identifiant.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return pseudonyme

identifiant_original = "jean.dupont@exemple.com"
clé_secrète = "clé-secrète-spécifique-à-l-organisation"

pseudonyme = pseudonymiser(identifiant_original, clé_secrète)
# Résultat : "8d3f9c2a1b4e5f6d7c8e9a0b1c2d3e4f..."
```

**Pseudonymisation réversible** :

```python
from cryptography.fernet import Fernet

def créer_clé_pseudonymisation():
    return Fernet.generate_key()

def pseudonymiser_réversible(identifiant, clé):
    chiffre = Fernet(clé)
    pseudonyme = chiffre.encrypt(identifiant.encode())
    return pseudonyme.decode()

def dé_pseudonymiser(pseudonyme, clé):
    chiffre = Fernet(clé)
    original = chiffre.decrypt(pseudonyme.encode())
    return original.decode()
```

**Considérations de conformité RGPD** :

- Clé de pseudonymisation stockée séparément des données pseudonymisées (système différent, contrôle d'accès)
- La ré-identification requiert une autorisation explicite au-delà de l'accès aux données
- Rotation des clés : Planifier la rotation périodique (nécessite une re-pseudonymisation)
- Audit : Journaliser toutes les tentatives de ré-identification

### Tables de mapping des pseudonymes

```
Ensemble de données pseudonymisé :
ID_Pseudonyme | Âge | Ville    | Condition_Médicale
PS001         | 45  | Zurich   | Diabète
PS002         | 32  | Genève   | Hypertension

Table de mapping (stockée séparément, accès restreint) :
ID_Pseudonyme | Vrai_Nom
PS001         | Jean Dupont
PS002         | Alice Martin
```

**Configuration** :

- Séparation du stockage : Table de mapping dans un système/base de données séparé
- Contrôle d'accès : Permissions différentes pour les données pseudonymisées vs. le mapping
- Chiffrement : Table de mapping chiffrée au repos
- Audit : Tout accès à la table de mapping journalisé

### k-Anonymat et l-Diversité

**k-Anonymat** : Garantir que chaque combinaison de quasi-identificateurs apparaît au moins k fois.

```
Données originales :
Âge | ZIP   | Condition
25  | 8001  | Grippe
26  | 8002  | Diabète
27  | 8001  | Hypertension

k-Anonymat (k=2) Généralisé :
Tranche d'âge | Zone ZIP    | Condition
20-30          | 8000-8099   | Grippe
20-30          | 8000-8099   | Diabète
20-30          | 8000-8099   | Hypertension
```

**Techniques de généralisation** :

- Âge : Âge exact → Tranches d'âge (20-30, 30-40, etc.)
- ZIP : Code postal à 4 chiffres → Préfixe à 2 chiffres
- Date : Date exacte → Mois ou Trimestre
- Revenu : Montant exact → Tranches de revenu

**l-Diversité** : Étendre le k-anonymat pour garantir la diversité des attributs sensibles.

```
k-Anonymat (k=3) mais pas l-Diverse :
→ Tous les enregistrements ont le même attribut sensible (Diabète)

l-Diversité (l=2) :
Tranche d'âge | Zone ZIP | Condition
20-30          | 8000-8099| Diabète
20-30          | 8000-8099| Grippe
20-30          | 8000-8099| Hypertension
→ Au moins 2 attributs sensibles différents dans le groupe
```

## Techniques d'anonymisation (irréversibles)

**Vue d'ensemble** : L'anonymisation supprime irréversiblement les informations identificatrices de sorte que la ré-identification est impossible même avec des données supplémentaires. Les données anonymisées ne sont plus des données personnelles au sens du RGPD.

### Agrégation et contrôle de divulgation statistique

```
Données individuelles originales :
Employé | Âge | Salaire
Jean    | 35  | 75 000
Alice   | 42  | 82 000
Bob     | 38  | 79 000

Données agrégées (anonymes) :
Tranche d'âge | Nombre d'employés | Salaire moyen
30-40          | 3                 | 78 667

Résultat : Individus non identifiables, utilité des données préservée
```

**Taille minimale du groupe** :

```
Configuration :
- k-anonymat : Minimum 5-10 individus par groupe (norme réglementaire)
- Suppression : Les groupes plus petits que k sont supprimés ou fusionnés
```

### Suppression des données

**Suppression de cellules** :

```
Données originales avec combinaisons rares :
Âge | Ville     | Condition
25  | Willisau  | Maladie rare X  ← 1 seule personne, risque élevé

Supprimé :
Âge | Ville     | Condition
*   | Willisau  | *                ← Supprimé pour protéger l'identité
```

---

# Méthodologies de découverte des données

## Reconnaissance automatique de motifs

**Analyse par expressions régulières** :

```python
MOTIFS = {
    'carte_crédit': r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b',
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'telephone': r'\b(?:\+?\d{1,3}[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b',
    'iban': r'\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b',
}

def analyser_colonne_pour_motifs(données_colonne, taille_échantillon=1000):
    résultats = {}
    échantillon = données_colonne.sample(min(taille_échantillon, len(données_colonne)))
    
    for nom_motif, motif in MOTIFS.items():
        correspondances = échantillon.str.contains(motif, regex=True, na=False)
        pourcentage = (correspondances.sum() / len(échantillon)) * 100
        
        if pourcentage > 10:
            résultats[nom_motif] = pourcentage
    
    return résultats
```

**Reconnaissance d'entités nommées (NER)** :

```python
import spacy

nlp = spacy.load("fr_core_news_sm")

def détecter_entités_pii(texte):
    doc = nlp(texte)
    entités = {'PER': [], 'ORG': [], 'LOC': [], 'DATE': []}
    
    for ent in doc.ents:
        if ent.label_ in entités:
            entités[ent.label_].append(ent.text)
    
    return entités
```

## Analyse des métadonnées de base de données

**Heuristiques sur les noms de colonnes** :

```python
MOTS_CLÉS_SENSIBLES = {
    'DCP': ['nom', 'prenom', 'email', 'telephone', 'adresse', 'nss', 'passeport', 'ddn'],
    'Financier': ['carte', 'compte', 'iban', 'swift', 'solde', 'salaire', 'paiement'],
    'Santé': ['médical', 'diagnostic', 'prescription', 'patient', 'assurance'],
    'Identifiants': ['password', 'secret', 'token', 'clé', 'api_key'],
}

def classifier_colonne_par_nom(nom_colonne):
    nom_minusc = nom_colonne.lower()
    for catégorie, mots_clés in MOTS_CLÉS_SENSIBLES.items():
        if any(mot_clé in nom_minusc for mot_clé in mots_clés):
            return catégorie
    return 'Inconnu'
```

## Profilage et analyse statistique

```python
def profiler_colonne(données_colonne):
    profil = {
        'nb_lignes': len(données_colonne),
        'nb_nulls': données_colonne.isnull().sum(),
        'nb_uniques': données_colonne.nunique(),
        'type_données': str(données_colonne.dtype),
        'ratio_unicité': données_colonne.nunique() / len(données_colonne),
    }
    
    if profil['ratio_unicité'] > 0.95:
        profil['probable_identificateur'] = True
    
    return profil
```

## Outils de découverte des données (catégories indépendantes des fournisseurs)

**Outils de balayage de bases de données** :

- Cloud-native : Azure Purview, AWS Macie, Google DLP API
- On-premises : IBM InfoSphere, Informatica Data Privacy Management
- Open source : DataHub, Amundsen, Apache Atlas

---

# Paysage des outils de masquage

## Matrice des capacités des outils

| Capacité | Base de données native | Outils dédiés | Outils ETL | Niveau applicatif |
|---------|----------------------|---------------|------------|-------------------|
| **Masquage statique** | Limité | Excellent | Bon | Limité |
| **Masquage dynamique** | Bon | Excellent | Non | Excellent |
| **Préservation du format** | Limité | Excellent | Bon | Limité |
| **Intégrité référentielle** | Bon | Excellent | Excellent | Manuel |
| **Performance** | Excellent | Bon | Bon | Variable |
| **Coût** | Faible (inclus) | Élevé | Moyen | Faible (effort de développement) |

## Architectures d'implémentation

**DDM natif à la base de données** :

```
Architecture :
Utilisateur → Application → Base de données (avec DDM) → Données masquées retournées

Avantages : Application centralisée, pas de changements applicatifs
Inconvénients : Implémentation spécifique à la base de données, peut impacter l'optimisation des requêtes
```

**Masquage basé sur un proxy** :

```
Architecture :
Utilisateur → Application → Proxy de masquage → Base de données → Proxy applique le masquage

Avantages : Indépendant de la base de données, gestion centralisée des politiques
Inconvénients : Infrastructure supplémentaire, surcharge de performance
```

---

# Guides de référence rapide

## Arbre de décision pour la sélection des techniques

```
DÉBUT : Besoin de masquer des données sensibles

Q1 : L'utilité des données est-elle requise dans l'environnement masqué ?
    NON → Utiliser : Expurgation/Nullification (plus simple)
    OUI → Continuer

Q2 : Le masquage doit-il être réversible ?
    OUI → Q2a : Qui doit inverser ?
        - Utilisateurs autorisés uniquement → Utiliser : Tokenisation ou Pseudonymisation
        - L'application a besoin de l'intégrité référentielle → Utiliser : Tokenisation

    NON → Continuer

Q3 : Est-ce pour le contrôle d'accès en production ?
    OUI → Utiliser : Masquage dynamique (DDM)
    NON → Continuer (usage non-production)

Q4 : L'intégrité référentielle entre tables doit-elle être préservée ?
    OUI → Utiliser : SDM déterministe
    NON → Utiliser : SDM aléatoire

Q5 : Exigence réglementaire (RGPD, PCI DSS, HIPAA) ?
    - Pseudonymisation RGPD → Pseudonymisation cryptographique
    - Masquage PCI DSS → Tokenisation ou SDM préservant le format
    - Dé-identification HIPAA → Anonymisation
    - Aucune → SDM avec substitution
```

## Scénarios de masquage courants

**Scénario 1 : Base de données de test à partir de la production**

```
Problème : Besoin de données de test réalistes sans exposer les DCP

Solution :
1. Exporter le schéma et les données de production
2. Appliquer le masquage statique (SDM) :
   - Noms : Substitution par des faux noms (déterministe)
   - Emails : Substitution préservant le format
   - Adresses : Remplacement par de fausses adresses valides
   - Téléphones : Chiffres aléatoires préservant le format
   - Dates : Décalage aléatoire cohérent par personne

3. Valider l'intégrité référentielle
4. Charger dans l'environnement de test
```

**Scénario 2 : Analytique avec protection des DCP**

```
Problème : La BI a besoin de données agrégées sans identification individuelle

Solution :
1. Pseudonymiser les identificateurs
2. Généraliser les quasi-identificateurs (âge → tranche, ZIP → préfixe)
3. Agréger les métriques sensibles
4. Implémenter le k-anonymat (k=5 minimum)
5. Supprimer les combinaisons rares
```

**Scénario 3 : Accès en production pour le support client**

```
Problème : Le support a besoin des données clients mais pas des DCP complètes

Solution :
1. Implémenter le DDM en base de données de production
2. Configurer les règles basées sur les rôles :
   - Support : Email partiel (je***@exemple.com), 4 derniers chiffres du téléphone
   - Manager : Email complet, téléphone complet
   - Admin : Tout non masqué

3. Journaliser tous les accès aux champs sensibles
```

## Guide de dépannage

**Problème : Les données masquées perturbent la logique applicative**

```
Cause : Les données masquées ne correspondent pas au format ou aux contraintes attendus
Solutions :
- Utiliser des techniques de masquage préservant le format
- Mettre à jour les règles de validation pour accepter les formats masqués
- Tester les données masquées avec l'application avant déploiement
```

**Problème : Violations d'intégrité référentielle après masquage**

```
Cause : Masquage non déterministe ou masquage incomplet des tables liées
Solutions :
- Utiliser un masquage déterministe (même entrée → même sortie)
- Masquer toutes les tables liées ensemble
- Maintenir le mapping des relations FK pendant le masquage
```

**Problème : Dégradation des performances avec le DDM**

```
Cause : Les fonctions de masquage empêchent l'utilisation des index
Solutions :
- Optimiser les fonctions de masquage
- Revoir les plans d'exécution des requêtes
- Envisager le masquage statique pour les environnements non-production
- Implémenter une couche de cache pour les données masquées fréquemment accédées
```

## Liste de contrôle de conformité

**PCI DSS (Req. 3.4-3.5)** :

- [ ] Numéro de compte primaire (PAN) masqué à l'affichage (max 6 premiers + 4 derniers chiffres)
- [ ] PAN illisible dans les environnements non-production
- [ ] CVV2/CVC2 jamais stocké
- [ ] Solution de masquage empêchant l'accès non autorisé au PAN non masqué
- [ ] Procédures de masquage documentées
- [ ] Validation annuelle de l'efficacité du masquage

**Pseudonymisation RGPD (Art. 32, 89)** :

- [ ] Clé de pseudonymisation stockée séparément des données pseudonymisées
- [ ] La ré-identification requiert des informations non disponibles au sous-traitant
- [ ] Mesures techniques et organisationnelles empêchant la ré-identification non autorisée
- [ ] Pseudonymisation documentée dans l'analyse d'impact sur la protection des données (AIPD)
- [ ] Révision régulière de l'efficacité de la pseudonymisation

**HIPAA Dé-identification (§164.514)** :

- [ ] Méthode Safe Harbor : Supprimer les 18 identificateurs HIPAA, OU
- [ ] Détermination experte : Vérification statistique par expert qualifié
- [ ] Aucune connaissance réelle de la possibilité de ré-identification
- [ ] Code d'enregistrement pour la ré-identification stocké séparément
- [ ] Documentation de la méthode de dé-identification et validation

---

# Meilleures pratiques d'implémentation

## Flux de travail du processus de masquage

```
1. DÉCOUVRIR
   ├─ Inventorier les systèmes et bases de données
   ├─ Analyser pour les motifs de données sensibles
   ├─ Classifier les données par sensibilité
   └─ Identifier les exigences réglementaires

2. CONCEVOIR
   ├─ Sélectionner les techniques de masquage appropriées
   ├─ Définir les règles de masquage par élément de données
   ├─ Planifier la maintenance de l'intégrité référentielle
   └─ Documenter les spécifications de masquage

3. DÉVELOPPER/CONFIGURER
   ├─ Configurer l'outil de masquage ou développer des scripts
   ├─ Implémenter les algorithmes de masquage
   ├─ Configurer les coffres-forts de jetons (si tokenisation)
   └─ Créer les flux d'exécution du masquage

4. TESTER
   ├─ Valider l'efficacité du masquage (données originales absentes)
   ├─ Tester l'intégrité référentielle
   ├─ Vérifier la compatibilité applicative
   ├─ Tests de performance
   └─ Tests de ré-identification (impossible de récupérer l'original)

5. DÉPLOYER
   ├─ Exécuter le masquage initial (SDM) ou activer les règles (DDM)
   ├─ Valider le succès du déploiement
   ├─ Surveiller les erreurs et les performances
   └─ Documenter le déploiement

6. SURVEILLER ET MAINTENIR
   ├─ Tests périodiques d'efficacité
   ├─ Surveiller l'exposition de données non masquées
   ├─ Mettre à jour les règles pour les nouveaux types de données
   ├─ Validation annuelle de conformité
   └─ Réponse aux incidents en cas d'échec du masquage
```

## Pièges courants à éviter

**Piège 1 : Masquer uniquement les DCP « évidentes »**

```
Erreur : Masquer le nom, l'email, le téléphone mais ignorer...
- Nom d'utilisateur (souvent identique à l'email)
- Champs commentaires/notes (peuvent contenir des DCP en texte libre)
- Fichiers journaux (peuvent enregistrer des données sensibles)
- Systèmes de sauvegarde/archivage (environnements oubliés)

Solution : Découverte complète des données dans TOUS les systèmes et formats
```

**Piège 2 : Masquage incohérent entre les environnements**

```
Erreur : Env. dev masqué, mais env. QA a une copie non masquée
Solution : Masquage automatisé dans le pipeline d'approvisionnement des données
```

**Piège 3 : Mentalité « masquer plus tard »**

```
Erreur : Copier la production vers le non-production, planifier de masquer « quand on aura le temps »
Solution : Masquage dans le processus de copie des données, pas de données non masquées en non-production
```

**Piège 4 : Masquage uniquement côté client**

```
Erreur : JavaScript masque les données dans l'UI, mais le backend retourne les données complètes
Solution : Appliquer le masquage côté serveur
```

---

# Glossaire des termes techniques

**Chiffrement préservant le format (FPE)** : Chiffrement qui maintient le format des données originales.

**Algorithme de Luhn** : Formule de somme de contrôle pour la validation des cartes de crédit.

**Quasi-identificateur** : Attribut qui peut identifier des individus lorsqu'il est combiné avec d'autres attributs.

**Attaque de ré-identification** : Tentative de récupérer l'identité originale à partir de données masquées ou anonymisées.

**Sel (cryptographique)** : Données aléatoires ajoutées à l'entrée avant le hachage pour empêcher les attaques par tables arc-en-ciel.

**Coffre-fort de jetons** : Base de données sécurisée stockant le mapping entre jetons et valeurs sensibles originales.

---

**FIN DU RÉFÉRENTIEL TECHNIQUE**

*Ce document est un document évolutif — mis à jour à mesure que les technologies, techniques et meilleures pratiques de masquage évoluent.*

*Rappel : Ce document n'est PAS un document SMSI. Les exigences contraignantes sont dans ISMS-POL-A.8.11.*

<!-- QA_VERIFIED: 2026-04-04 -->
